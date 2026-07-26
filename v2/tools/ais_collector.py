# ais_collector.py — de verzamelaar die het M28-tracknet voedt (LAR-529).
#
# Draait permanent op de VPS als systemd-service naast de Hermes-gateway, luistert
# op aisstream.io en schrijft ELK ontvangen bericht ongefilterd weg als JSONL,
# één bestand per dag (UTC). Bewust dom: er zit GEEN track-logica in. Tracks
# bouwen, varend/stilliggend knippen en bundelen gebeurt in de aparte
# verwerkingsstap (LAR-530), zodat verzamelde data nooit opnieuw hoeft.
#
# Robuustheid: aisstream is beta zonder SLA, dus auto-reconnect met backoff en
# een periodieke health-regel per venster (berichten/min) — stille uitval van de
# stream moet opvallen in `journalctl`, niet pas weken later in de data. Gaten in
# de stream zijn acceptabel; ze worden in de verwerking gedetecteerd als
# tijdsprong per MMSI.
#
# Schijf: de VPS heeft weinig marge, dus afgesloten dagen worden gegzipt (~10x)
# en er is een harde ondergrens waaronder de collector stopt met schrijven in
# plaats van de schijf vol te laten lopen.
#
# Draaien (VPS):
#   /opt/ais-collector/venv/bin/python /opt/ais-collector/collector.py \
#       --vensters /opt/ais-collector/vensters.json \
#       --uit /var/lib/ais-collector/ais \
#       --key-file /opt/ais-collector/aisstream.key

import argparse
import asyncio
import gzip
import json
import shutil
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    import websockets
except ImportError:
    sys.exit("Ontbrekende afhankelijkheid: pip install websockets")

URL = "wss://stream.aisstream.io/v0/stream"

# Onder deze vrije ruimte stoppen we met schrijven (de stream blijft wel lopen,
# zodat de health-regels doorgaan en het probleem zichtbaar blijft).
MIN_VRIJ_GB = 2.0
HEALTH_SECONDEN = 300


def log(*stukken) -> None:
    """Naar stdout — systemd vangt het op in journald."""
    tijd = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(tijd, *stukken, flush=True)


def vrij_gb(pad: Path) -> float:
    return shutil.disk_usage(pad).free / 1e9


def in_venster(lat: float, lon: float, box) -> bool:
    z, w, n, o = box
    return z <= lat <= n and w <= lon <= o


class Dagbestand:
    """Append-only JSONL per UTC-dag; afgesloten dagen worden gegzipt.

    Met `live_gz` wordt er meteen gegzipt weggeschreven in plaats van pas bij de
    dagwissel. Dat is geen optimalisatie maar een voorwaarde voor het
    wereldabonnement: ruw is dat ~8,5 GB/dag tegen ~1 GB gegzipt, en er staat maar
    ~22 GB vrij op de VPS — ongegzipt loopt de schijf binnen twee dagen tegen de
    ondergrens. gzip staat concatenatie toe, dus append over een herstart heen is
    geldig: elke herstart voegt simpelweg een nieuw member toe.
    """

    def __init__(self, map_pad: Path, live_gz: bool = False):
        self.map = map_pad
        self.map.mkdir(parents=True, exist_ok=True)
        self.live_gz = live_gz
        self.dag = None
        self.fh = None
        self.geblokkeerd = False

    def _sluit(self) -> None:
        if self.fh:
            self.fh.close()
            self.fh = None
            if self.live_gz:
                return                      # al gegzipt weggeschreven
            oud = self.map / f"{self.dag}.jsonl"
            if oud.exists():
                self._gzip(oud)

    @staticmethod
    def _gzip(pad: Path) -> None:
        try:
            with pad.open("rb") as bron, gzip.open(f"{pad}.gz", "wb", 6) as doel:
                shutil.copyfileobj(bron, doel)
            klein = pad.with_suffix(".jsonl.gz").stat().st_size
            log(f"dag afgesloten: {pad.name} -> .gz "
                f"({pad.stat().st_size / 1e6:.0f} MB -> {klein / 1e6:.0f} MB)")
            pad.unlink()
        except OSError as fout:
            log(f"WAARSCHUWING gzip mislukt voor {pad.name}: {fout}")

    def schrijf(self, regel: str) -> None:
        vandaag = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        if vandaag != self.dag:
            self._sluit()
            self.dag = vandaag
            if self.live_gz:
                # Een ongegzipte dag van vóór de omzetting mag niet botsen met de
                # naam van het live-bestand: apart wegzetten en alsnog inpakken.
                plat = self.map / f"{vandaag}.jsonl"
                if plat.exists():
                    deel = self.map / f"{vandaag}-a.jsonl"
                    plat.rename(deel)
                    self._gzip(deel)
                naam = f"{vandaag}.jsonl.gz"
                self.fh = gzip.open(self.map / naam, "at", 6, encoding="utf-8")
            else:
                naam = f"{vandaag}.jsonl"
                self.fh = (self.map / naam).open("a", encoding="utf-8")
            log(f"schrijft nu naar {naam} ({vrij_gb(self.map):.1f} GB vrij)")

        if self.geblokkeerd:
            return
        if vrij_gb(self.map) < MIN_VRIJ_GB:
            self.geblokkeerd = True
            log(f"FOUT schijf bijna vol (<{MIN_VRIJ_GB} GB vrij) — "
                "schrijven gestopt, stream loopt door")
            return

        self.fh.write(regel)
        self.fh.write("\n")

    def flush(self) -> None:
        if self.fh:
            self.fh.flush()


class Gezondheid:
    """Telt per venster, zodat stille uitval opvalt in journalctl."""

    def __init__(self, vensters: dict):
        self.vensters = vensters
        self.reset()

    def reset(self) -> None:
        self.tellers = defaultdict(int)
        self.mmsis = defaultdict(set)
        self.buiten = 0
        self.totaal = 0
        self.sinds = time.monotonic()

    def tel(self, lat: float, lon: float, mmsi) -> None:
        self.totaal += 1
        for naam, box in self.vensters.items():
            if in_venster(lat, lon, box):
                self.tellers[naam] += 1
                self.mmsis[naam].add(mmsi)
                return
        self.buiten += 1

    def rapporteer(self) -> None:
        minuten = max((time.monotonic() - self.sinds) / 60.0, 1e-9)
        # Vensters die niets opleveren (bewuste bewakers zoals tongling) worden
        # apart en compact genoemd: anders verdrinkt bij een stuk of tien
        # corridors het signaal in een rij nullen.
        levend, stil = [], []
        for naam in self.vensters:
            if self.tellers[naam]:
                levend.append(f"{naam} {self.tellers[naam] / minuten:.0f}/min "
                              f"({len(self.mmsis[naam])} MMSI)")
            else:
                stil.append(naam)
        regel = f"health · {self.totaal:,} berichten in {minuten:.0f} min · "
        regel += " · ".join(levend) if levend else "GEEN ENKEL VENSTER LEVERT DATA"
        if stil:
            regel += f" · stil: {', '.join(stil)}"
        if self.buiten:
            regel += f" · buiten vensters {self.buiten:,}"
        log(regel)
        self.reset()


async def verzamel(key: str, vensters: dict, soorten: list,
                   bestand: Dagbestand, wereld: bool = False) -> None:
    # Wereldabonnement: gemeten op 2026-07-26 levert de HELE aisstream-feed
    # ~9.800 berichten/min (588.627 in een uur, 41.812 unieke schepen). Onze 13
    # vensters trokken daar al ~1.600/min van. Vensters zijn bij die verhouding
    # voortijdige zuinigheid: ze kosten later een gemiste corridor die je niet
    # meer kunt terughalen. De vensters blijven bestaan als HEALTH-BANEN, zodat
    # uitval per corridor zichtbaar blijft in journalctl.
    if wereld:
        boxes = [[[-90.0, -180.0], [90.0, 180.0]]]
    else:
        boxes = [[[b[0], b[1]], [b[2], b[3]]] for b in vensters.values()]
    abonnement = json.dumps({
        "APIKey": key,
        "BoundingBoxes": boxes,
        "FilterMessageTypes": soorten,
    })
    gezond = Gezondheid(vensters)
    wacht = 1.0
    volgende_health = time.monotonic() + HEALTH_SECONDEN

    while True:
        try:
            async with websockets.connect(URL, ping_interval=20,
                                          max_queue=4096) as ws:
                # aisstream verbreekt als het abonnement niet binnen 3 s komt.
                await ws.send(abonnement)
                waar = ("de HELE WERELD · health-banen: " if wereld
                        else f"{len(boxes)} venster(s): ")
                log(f"verbonden · {waar}{', '.join(vensters)} · "
                    f"soorten: {', '.join(soorten)}")
                wacht = 1.0

                while True:
                    rauw = await asyncio.wait_for(ws.recv(), timeout=120)
                    regel = rauw if isinstance(rauw, str) else rauw.decode()
                    bestand.schrijf(regel)

                    try:
                        bericht = json.loads(regel)
                        meta = bericht.get("MetaData", {})
                        gezond.tel(meta["latitude"], meta["longitude"],
                                   meta.get("MMSI"))
                    except (json.JSONDecodeError, KeyError, TypeError):
                        # ShipStaticData draagt dezelfde MetaData-velden, maar
                        # een onverwacht bericht mag de collector nooit stoppen.
                        gezond.totaal += 1

                    if time.monotonic() >= volgende_health:
                        gezond.rapporteer()
                        bestand.flush()
                        volgende_health = time.monotonic() + HEALTH_SECONDEN

        except asyncio.TimeoutError:
            log("WAARSCHUWING 120 s geen bericht — verbinding opnieuw opbouwen")
            bestand.flush()
        except Exception as fout:  # noqa: BLE001 — beta-stream zonder SLA
            log(f"verbinding weg ({type(fout).__name__}: {fout}) — "
                f"opnieuw over {wacht:.0f}s")
            bestand.flush()
            await asyncio.sleep(wacht)
            wacht = min(wacht * 2, 300.0)


def main() -> None:
    p = argparse.ArgumentParser(description="AIS-collector (LAR-529)")
    p.add_argument("--vensters", type=Path, required=True,
                   help="JSON: {naam: [zuid, west, noord, oost], ...}")
    p.add_argument("--uit", type=Path, required=True, help="map voor de JSONL")
    p.add_argument("--key-file", type=Path, required=True)
    p.add_argument("--soorten", nargs="+",
                   default=["PositionReport", "ShipStaticData",
                            "StandardClassBPositionReport",
                            "ExtendedClassBPositionReport",
                            "StaticDataReport"],
                   help="ShipStaticData staat er standaard bij: scheepstype is "
                        "nodig voor de terminal-typering (LAR-531) en kost "
                        "nauwelijks volume (1 bericht per schip per 6 min). "
                        "⚠️ PositionReport is UITSLUITEND Class A (msg 1/2/3); "
                        "Class B-transponders komen binnen als "
                        "StandardClassB-/ExtendedClassBPositionReport en hun "
                        "scheepsnaam/-type als StaticDataReport (msg 24). "
                        "Gemeten op 2026-07-26 in een wereldabonnement: mét "
                        "Class B erbij 9.655 ber/min en 8.089 unieke MMSI tegen "
                        "4.465 en 4.269 zonder — ruwweg de helft van de schepen "
                        "was onzichtbaar.")
    p.add_argument("--wereld", action="store_true",
                   help="abonneer op de hele wereld i.p.v. op de vensters; de "
                        "vensters blijven dan health-banen. Vereist --live-gz, "
                        "anders loopt de VPS-schijf binnen twee dagen vol.")
    p.add_argument("--live-gz", action="store_true",
                   help="schrijf meteen gegzipt (~1 GB/dag i.p.v. ~8,5 GB ruw)")
    args = p.parse_args()

    key = args.key_file.read_text(encoding="utf-8").strip()
    vensters = json.loads(args.vensters.read_text(encoding="utf-8"))
    if not vensters:
        sys.exit("Geen vensters gedefinieerd")

    if args.wereld and not args.live_gz:
        sys.exit("--wereld zonder --live-gz vult de schijf: ~8,5 GB/dag ruw "
                 "tegen ~1 GB gegzipt. Zet --live-gz erbij.")

    log(f"AIS-collector start · "
        f"{'WERELD' if args.wereld else str(len(vensters)) + ' venster(s)'} · "
        f"{'gegzipt' if args.live_gz else 'ruw'} · "
        f"{vrij_gb(args.uit.parent):.1f} GB vrij")
    bestand = Dagbestand(args.uit, live_gz=args.live_gz)
    try:
        asyncio.run(verzamel(key, vensters, args.soorten, bestand,
                             wereld=args.wereld))
    except KeyboardInterrupt:
        log("gestopt")
    finally:
        bestand.flush()


if __name__ == "__main__":
    main()
