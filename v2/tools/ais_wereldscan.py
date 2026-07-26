# ais_wereldscan.py — meet de ECHTE dekking van aisstream, wereldwijd.
#
# Waarom dit bestaat: de pings-debuglaag toont alleen wat de collector binnenkrijgt,
# en die is geabonneerd op een handvol vensters. Alles daarbuiten is donker *omdat we
# er niet om vragen* — niet omdat aisstream er niets heeft. Zolang dat door elkaar
# loopt kunnen we niet kiezen welke corridors uit echte tracks gebouwd kunnen worden.
#
# Daarom: één abonnement op de HELE WERELD ([[-90,-180],[90,180]] — staat zo in
# aisstream's eigen documentatievoorbeeld), en per rastercel tellen wat er binnenkomt.
# Het resultaat is een dekkingskaart van HUN netwerk, onafhankelijk van onze keuzes.
#
# Twee uitvoerbestanden, met opzet allebei:
#   * wereldscan-<stempel>.json  — het raster (klein, dit is het antwoord)
#   * wereldscan-<stempel>.jsonl.gz — elk ruw bericht (dit is meteen een wereldwijde
#     momentopname van tracks; verzamelde data hoort nooit opnieuw te hoeven)
#
# aisstream documenteert ~300 berichten/seconde voor de hele wereld. Het raster
# wordt elke paar minuten tussentijds weggeschreven, zodat een afgebroken run niet
# alles kost.
#
# Draaien (VPS, waar de key staat):
#   python3 ais_wereldscan.py --minuten 60 \
#       --key-file /opt/ais-collector/aisstream.key \
#       --uit /var/lib/ais-collector/wereldscan

import argparse
import asyncio
import gzip
import json
import math
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
WERELD = [[[-90.0, -180.0], [90.0, 180.0]]]
MIN_VRIJ_GB = 2.0

# Class A zendt msg 1/2/3 (= "PositionReport"), Class B msg 18/19. Dat onderscheid
# is geen detail: het bepaalt of een cel dekking hééft of alleen zo lijkt.
KLASSE_A = {"PositionReport"}
KLASSE_B = {"StandardClassBPositionReport", "ExtendedClassBPositionReport"}


def log(*stukken) -> None:
    tijd = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(tijd, *stukken, flush=True)


class Raster:
    """Telt per cel. Bewust dom: alleen tellen, geen oordeel over 'genoeg'."""

    def __init__(self, graden: float):
        self.graden = graden
        self.n = defaultdict(int)
        self.varend = defaultdict(int)
        self.mmsi = defaultdict(set)
        self.alle_mmsi = set()
        self.soorten = defaultdict(int)      # per MessageType
        self.a_ber = defaultdict(int)        # Class A posities per cel
        self.b_ber = defaultdict(int)        # Class B posities per cel
        self.a_mmsi = defaultdict(set)
        self.b_mmsi = defaultdict(set)
        self.zonder_positie = 0
        self.berichten = 0
        self.begin = time.monotonic()
        self.vaste_minuten = None

    def cel(self, lat: float, lon: float) -> str:
        return f"{math.floor(lat / self.graden)},{math.floor(lon / self.graden)}"

    def tel(self, lat: float, lon: float, mmsi, sog, soort: str = "") -> None:
        c = self.cel(lat, lon)
        self.berichten += 1
        self.n[c] += 1
        if sog is not None and sog >= 0.5:
            self.varend[c] += 1
        if soort in KLASSE_A:
            self.a_ber[c] += 1
            if mmsi is not None:
                self.a_mmsi[c].add(mmsi)
        elif soort in KLASSE_B:
            self.b_ber[c] += 1
            if mmsi is not None:
                self.b_mmsi[c].add(mmsi)
        if mmsi is not None:
            self.mmsi[c].add(mmsi)
            self.alle_mmsi.add(mmsi)

    @property
    def minuten(self) -> float:
        if self.vaste_minuten is not None:      # herberekening uit een bestand
            return max(self.vaste_minuten, 1e-9)
        return max((time.monotonic() - self.begin) / 60.0, 1e-9)

    def schrijf(self, pad: Path, gestart: str) -> None:
        cellen = {
            c: [self.n[c], len(self.mmsi[c]), self.varend[c],
                self.a_ber[c], self.b_ber[c],
                len(self.a_mmsi[c]), len(self.b_mmsi[c])]
            for c in sorted(self.n, key=lambda x: -self.n[x])
        }
        alleen_b = sum(1 for c in cellen if not self.a_ber[c] and self.b_ber[c])
        pad.write_text(json.dumps({
            "bron": "aisstream.io · wereldabonnement",
            "gestart_utc": gestart,
            "geschreven_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "minuten": round(self.minuten, 2),
            "raster_graden": self.graden,
            "berichten": self.berichten,
            "unieke_mmsi": len(self.alle_mmsi),
            "cellen_met_data": len(cellen),
            "berichtsoorten": dict(sorted(self.soorten.items(),
                                          key=lambda kv: -kv[1])),
            "zonder_positie": self.zonder_positie,
            "cellen_alleen_classB": alleen_b,
            "veldvolgorde": ["berichten", "unieke_mmsi", "varend",
                             "klasseA_ber", "klasseB_ber",
                             "klasseA_mmsi", "klasseB_mmsi"],
            "cellen": cellen,
        }, ensure_ascii=False), encoding="utf-8")


async def luister(key: str, raster: Raster, rauw, seconden: float,
                  tussenpad: Path, gestart: str, soorten) -> None:
    # ⚠️ GEEN FilterMessageTypes: "PositionReport" is uitsluitend Class A (msg 1/2/3).
    # Class B-transponders komen binnen als StandardClassBPositionReport /
    # ExtendedClassBPositionReport, en walstations zenden zichzelf uit als
    # BaseStationReport. Filteren op PositionReport laat de dekking dus systematisch
    # te somber lijken — precies de vraag die deze scan moet beantwoorden.
    inhoud = {"APIKey": key, "BoundingBoxes": WERELD}
    if soorten:
        inhoud["FilterMessageTypes"] = soorten
    abonnement = json.dumps(inhoud)
    einde = time.monotonic() + seconden
    wacht = 1.0
    volgende_log = time.monotonic() + 60
    volgende_schrijf = time.monotonic() + 300
    vorige_n = 0

    while time.monotonic() < einde:
        try:
            async with websockets.connect(URL, ping_interval=20,
                                          max_size=2**22) as ws:
                await ws.send(abonnement)  # aisstream kapt af zonder abonnement <3 s
                wacht = 1.0
                log("verbonden · abonnement op de HELE wereld")

                while time.monotonic() < einde:
                    rest = einde - time.monotonic()
                    bericht_rauw = await asyncio.wait_for(
                        ws.recv(), timeout=min(rest, 60))
                    if not isinstance(bericht_rauw, str):
                        bericht_rauw = bericht_rauw.decode()
                    if rauw is not None:
                        rauw.write(bericht_rauw)
                        rauw.write("\n")

                    try:
                        b = json.loads(bericht_rauw)
                    except json.JSONDecodeError:
                        continue
                    soort = b.get("MessageType", "?")
                    raster.soorten[soort] += 1
                    meta = b.get("MetaData") or {}
                    lat, lon = meta.get("latitude"), meta.get("longitude")
                    if lat is None or lon is None:
                        raster.zonder_positie += 1
                        continue
                    # Sog zit per berichtsoort onder een andere sleutel; pak 'm
                    # generiek uit de body en laat 'm weg als hij er niet is.
                    body = (b.get("Message") or {}).get(soort) or {}
                    sog = body.get("Sog") if isinstance(body, dict) else None
                    raster.tel(lat, lon, meta.get("MMSI"), sog, soort)

                    nu = time.monotonic()
                    if nu >= volgende_log:
                        per_min = raster.berichten - vorige_n
                        vorige_n = raster.berichten
                        top = " · ".join(
                            f"{s} {n:,}" for s, n in
                            sorted(raster.soorten.items(),
                                   key=lambda kv: -kv[1])[:4])
                        log(f"[{raster.minuten:5.1f} min] {raster.berichten:,} ber "
                            f"({per_min:,}/min) · {len(raster.alle_mmsi):,} MMSI · "
                            f"{len(raster.n):,} cellen | {top}")
                        volgende_log += 60
                    if nu >= volgende_schrijf:
                        raster.schrijf(tussenpad, gestart)
                        if rauw is not None:
                            rauw.flush()
                        volgende_schrijf += 300

        except asyncio.TimeoutError:
            log(f"[{raster.minuten:5.1f} min] 60 s geen bericht — "
                f"{raster.berichten:,} tot nu")
            volgende_log = time.monotonic() + 60
        except Exception as fout:  # noqa: BLE001 — beta-stream zonder SLA
            if time.monotonic() >= einde:
                break
            log(f"verbinding weg ({type(fout).__name__}: {fout}) — "
                f"opnieuw over {wacht:.0f}s")
            await asyncio.sleep(wacht)
            wacht = min(wacht * 2, 60.0)


def main() -> None:
    p = argparse.ArgumentParser(description="wereldwijde aisstream-dekkingsscan")
    p.add_argument("--minuten", type=float, default=60.0)
    p.add_argument("--raster", type=float, default=0.25,
                   help="celgrootte in graden (default 0,25 ~ 25 km)")
    p.add_argument("--key-file", type=Path,
                   default=Path("/opt/ais-collector/aisstream.key"))
    p.add_argument("--uit", type=Path,
                   default=Path("/var/lib/ais-collector/wereldscan"))
    p.add_argument("--geen-rauw", action="store_true",
                   help="alleen het raster wegschrijven, geen ruwe JSONL")
    p.add_argument("--herbereken", type=Path, default=None,
                   help="lees een eerder weggeschreven .jsonl.gz en bouw daar het "
                        "raster uit, zonder te verbinden — zo kost een rijkere "
                        "uitsplitsing achteraf geen nieuwe meettijd")
    p.add_argument("--soorten", nargs="*", default=None,
                   help="berichtsoorten om op te filteren; LEEG LATEN = alles "
                        "(anders mis je Class B en de walstations)")
    args = p.parse_args()

    if args.herbereken:
        raster = Raster(args.raster)
        vroegst = laatst = None
        opener = (gzip.open if args.herbereken.suffix == ".gz" else open)
        with opener(args.herbereken, "rt", encoding="utf-8") as bron:
            for regel in bron:
                try:
                    b = json.loads(regel)
                except json.JSONDecodeError:
                    continue
                soort = b.get("MessageType", "?")
                raster.soorten[soort] += 1
                meta = b.get("MetaData") or {}
                lat, lon = meta.get("latitude"), meta.get("longitude")
                if lat is None or lon is None:
                    raster.zonder_positie += 1
                    continue
                body = (b.get("Message") or {}).get(soort) or {}
                sog = body.get("Sog") if isinstance(body, dict) else None
                raster.tel(lat, lon, meta.get("MMSI"), sog, soort)
                t = meta.get("time_utc")
                if t:
                    if vroegst is None or t < vroegst:
                        vroegst = t
                    if laatst is None or t > laatst:
                        laatst = t
        if vroegst and laatst:
            # "2026-07-26 12:56:08.123 +0000 UTC" -> minuten tussen eerste/laatste
            f = "%Y-%m-%d %H:%M:%S"
            a = datetime.strptime(vroegst[:19], f)
            z = datetime.strptime(laatst[:19], f)
            raster.vaste_minuten = (z - a).total_seconds() / 60.0
        uit = args.herbereken.with_suffix("").with_suffix(".json")
        raster.schrijf(uit, "(herberekend uit " + args.herbereken.name + ")")
        log(f"herberekend · {raster.berichten:,} berichten · "
            f"{len(raster.alle_mmsi):,} MMSI · {len(raster.n):,} cellen -> {uit}")
        return

    key = args.key_file.read_text(encoding="utf-8").strip()
    args.uit.mkdir(parents=True, exist_ok=True)
    if shutil.disk_usage(args.uit).free / 1e9 < MIN_VRIJ_GB:
        sys.exit(f"minder dan {MIN_VRIJ_GB} GB vrij — niet beginnen")

    stempel = time.strftime("%Y-%m-%dT%H%M", time.gmtime())
    grid_pad = args.uit / f"wereldscan-{stempel}.json"
    rauw_pad = args.uit / f"wereldscan-{stempel}.jsonl.gz"
    gestart = datetime.now(timezone.utc).isoformat(timespec="seconds")

    log(f"wereldscan · {args.minuten:.0f} min · raster {args.raster}° · "
        f"soorten: {' '.join(args.soorten) if args.soorten else 'ALLES'}")
    log(f"raster -> {grid_pad}")
    raster = Raster(args.raster)
    rauw = None if args.geen_rauw else gzip.open(rauw_pad, "wt", encoding="utf-8")
    if rauw is not None:
        log(f"ruwe berichten -> {rauw_pad}")
    try:
        asyncio.run(luister(key, raster, rauw, args.minuten * 60,
                            grid_pad, gestart, args.soorten))
    except KeyboardInterrupt:
        log("afgebroken — raster over wat binnen is")
    finally:
        if rauw is not None:
            rauw.close()

    raster.schrijf(grid_pad, gestart)
    log(f"KLAAR · {raster.berichten:,} berichten · {len(raster.alle_mmsi):,} "
        f"unieke MMSI · {len(raster.n):,} cellen met data over "
        f"{raster.minuten:.1f} min")


if __name__ == "__main__":
    main()
