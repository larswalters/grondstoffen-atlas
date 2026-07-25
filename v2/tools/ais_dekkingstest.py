# ais_dekkingstest.py — luister eerst, bouw dan (LAR-528, de go/no-go van M28).
#
# Verbindt met aisstream.io (wss://stream.aisstream.io/v0/stream) en luistert een
# afgesproken tijd naar PositionReports binnen een aantal vensters. Doel is één
# vraag beantwoorden vóór er drie weken verzameld wordt:
#
#   heeft het open/vrijwillige aisstream-stationsnetwerk bruikbare dekking op de
#   Yangtze (box om Tongling), of alleen op Europa (box om Rotterdam)?
#
# Beslisregel (uit LAR-528):
#   Yangtze bruikbaar volume  -> M28 volledig, Tongling wordt de pilot-corridor.
#   Yangtze leeg, R'dam goed  -> M28 voor Europa; Yangtze houdt het density-raster.
#
# De ruwe berichten gaan ongefilterd naar JSONL — precies het formaat dat de
# collector (LAR-529) straks ook schrijft, zodat deze testdata meteen bruikbaar
# is voor de track-naar-graaf pijplijn (LAR-530) en voor kepler.gl.
#
# Draaien:
#   pip install websockets
#   python v2/tools/ais_dekkingstest.py --minuten 120
#   python v2/tools/ais_dekkingstest.py --vensters tongling --minuten 60
#
# De API-key komt uit (in deze volgorde): --key · $AISSTREAM_API_KEY ·
# v2/build-cache/ais/aisstream.key  (build-cache staat in .gitignore — de key
# komt zo nooit in git terecht).

import argparse
import asyncio
import json
import os
import sys
import time
from collections import defaultdict
from pathlib import Path

try:
    import websockets
except ImportError:
    sys.exit("Ontbrekende afhankelijkheid: pip install websockets")

HIER = Path(__file__).resolve().parent
AIS = HIER.parent / "build-cache" / "ais"
UIT = AIS / "verken"
KEYFILE = AIS / "aisstream.key"

URL = "wss://stream.aisstream.io/v0/stream"

# (zuid, west, noord, oost) in graden. Tongling = de twee geulen om het eiland
# uit LAR-528; rotterdam = de sanity-check (daar MOET het stromen).
VENSTERS = {
    "tongling":  (30.70, 117.60, 31.10, 118.10),
    "rotterdam": (51.75, 3.85, 52.05, 4.60),
}


def lees_key(opgegeven: str | None) -> str:
    if opgegeven:
        return opgegeven.strip()
    uit_env = os.environ.get("AISSTREAM_API_KEY")
    if uit_env:
        return uit_env.strip()
    if KEYFILE.exists():
        return KEYFILE.read_text(encoding="utf-8").strip()
    sys.exit(
        "Geen API-key. Maak er gratis een aan op https://aisstream.io (login via "
        f"GitHub) en zet 'm in {KEYFILE}, in $AISSTREAM_API_KEY of achter --key."
    )


def in_venster(lat: float, lon: float, box) -> bool:
    z, w, n, o = box
    return z <= lat <= n and w <= lon <= o


class Teller:
    """Houdt per venster bij wat er binnenkomt. Alleen tellen — geen oordeel."""

    def __init__(self, namen):
        self.namen = namen
        self.berichten = defaultdict(int)
        self.mmsis = defaultdict(set)
        self.varend = defaultdict(int)      # SOG >= 0,5 kn
        self.stil = defaultdict(int)
        self.lon_bins = defaultdict(lambda: defaultdict(int))
        self.buiten = 0
        self.begin = time.monotonic()

    def tel(self, naam: str, lat: float, lon: float, mmsi, sog) -> None:
        self.berichten[naam] += 1
        self.mmsis[naam].add(mmsi)
        if sog is not None and sog >= 0.5:
            self.varend[naam] += 1
        else:
            self.stil[naam] += 1
        # lon-histogram op 0,02° — bij Tongling verraadt dat of beide geulen
        # om het eiland bevaren worden (twee pieken) of maar één.
        self.lon_bins[naam][round(lon / 0.02) * 0.02] += 1

    @property
    def minuten(self) -> float:
        return max((time.monotonic() - self.begin) / 60.0, 1e-9)

    def regel(self) -> str:
        delen = []
        for naam in self.namen:
            n = self.berichten[naam]
            delen.append(
                f"{naam} {n:,} ber ({n / self.minuten:.1f}/min) · "
                f"{len(self.mmsis[naam])} MMSI"
            )
        return f"[{self.minuten:5.1f} min] " + "  |  ".join(delen)

    def rapport(self) -> None:
        print(f"\n{'=' * 72}\nRAPPORT na {self.minuten:.1f} minuten\n{'=' * 72}")
        for naam in self.namen:
            n = self.berichten[naam]
            print(f"\n== {naam} ==  venster {VENSTERS[naam]}")
            if n == 0:
                print("   LEEG — geen enkele positie ontvangen in dit venster")
                continue
            print(f"   {n:,} berichten · {n / self.minuten:.1f}/min · "
                  f"{len(self.mmsis[naam])} unieke MMSI's")
            print(f"   varend (SOG >= 0,5 kn) {self.varend[naam]:,} · "
                  f"stilliggend {self.stil[naam]:,}")
            bins = sorted(self.lon_bins[naam].items())
            top = max(v for _, v in bins)
            print("   verdeling over lengtegraad (0,02°-bakken):")
            for lon, aantal in bins:
                balk = "#" * max(1, round(40 * aantal / top))
                print(f"     {lon:8.2f}  {aantal:6,}  {balk}")
        if self.buiten:
            print(f"\n({self.buiten:,} berichten buiten elk venster — "
                  "aisstream levert de box ruim)")


async def luister(key: str, namen, teller: Teller, jsonl, seconden: float) -> None:
    boxes = [[[VENSTERS[n][0], VENSTERS[n][1]],
              [VENSTERS[n][2], VENSTERS[n][3]]] for n in namen]
    abonnement = json.dumps({
        "APIKey": key,
        "BoundingBoxes": boxes,
        "FilterMessageTypes": ["PositionReport"],
    })

    einde = time.monotonic() + seconden
    wacht = 1.0
    volgende_log = time.monotonic() + 60

    while time.monotonic() < einde:
        try:
            async with websockets.connect(URL, ping_interval=20) as ws:
                # aisstream verbreekt als het abonnement niet binnen 3 s komt.
                await ws.send(abonnement)
                wacht = 1.0
                print(f"verbonden · luistert op {len(boxes)} venster(s)")

                while time.monotonic() < einde:
                    rest = einde - time.monotonic()
                    rauw = await asyncio.wait_for(ws.recv(), timeout=min(rest, 60))
                    jsonl.write(rauw if isinstance(rauw, str) else rauw.decode())
                    jsonl.write("\n")

                    bericht = json.loads(rauw)
                    if bericht.get("MessageType") != "PositionReport":
                        continue
                    pr = bericht["Message"]["PositionReport"]
                    meta = bericht.get("MetaData", {})
                    lat, lon = pr["Latitude"], pr["Longitude"]
                    mmsi = meta.get("MMSI") or pr.get("UserID")
                    sog = pr.get("Sog")

                    for naam in namen:
                        if in_venster(lat, lon, VENSTERS[naam]):
                            teller.tel(naam, lat, lon, mmsi, sog)
                            break
                    else:
                        teller.buiten += 1

                    if time.monotonic() >= volgende_log:
                        print(teller.regel(), flush=True)
                        jsonl.flush()
                        volgende_log += 60

        except asyncio.TimeoutError:
            # Een minuut stilte is informatie, geen fout — vooral bij Tongling.
            print(teller.regel() + "   (60 s geen bericht)", flush=True)
            volgende_log = time.monotonic() + 60
        except Exception as fout:  # noqa: BLE001 — beta-stream zonder SLA
            if time.monotonic() >= einde:
                break
            print(f"verbinding weg ({type(fout).__name__}: {fout}) — "
                  f"opnieuw over {wacht:.0f}s", flush=True)
            await asyncio.sleep(wacht)
            wacht = min(wacht * 2, 60.0)


def schrijf_csv(jsonl_pad: Path) -> Path:
    """Platte CSV voor kepler.gl (de tussenoplossing uit LAR-535)."""
    csv_pad = jsonl_pad.with_suffix(".csv")
    with jsonl_pad.open(encoding="utf-8") as bron, \
            csv_pad.open("w", encoding="utf-8", newline="") as doel:
        doel.write("mmsi,lat,lon,sog,cog,tijd\n")
        for regel in bron:
            try:
                b = json.loads(regel)
                pr = b["Message"]["PositionReport"]
                meta = b.get("MetaData", {})
            except (json.JSONDecodeError, KeyError):
                continue
            doel.write(f'{meta.get("MMSI", "")},{pr["Latitude"]},'
                       f'{pr["Longitude"]},{pr.get("Sog", "")},'
                       f'{pr.get("Cog", "")},{meta.get("time_utc", "")}\n')
    return csv_pad


def main() -> None:
    p = argparse.ArgumentParser(description="aisstream-dekkingstest (LAR-528)")
    p.add_argument("--minuten", type=float, default=90.0)
    p.add_argument("--vensters", nargs="+", default=list(VENSTERS),
                   choices=list(VENSTERS))
    p.add_argument("--key", default=None)
    p.add_argument("--uit", type=Path, default=UIT,
                   help="map voor de ruwe JSONL (default: v2/build-cache/ais/verken)")
    args = p.parse_args()

    key = lees_key(args.key)
    uit_map = args.uit
    uit_map.mkdir(parents=True, exist_ok=True)
    stempel = time.strftime("%Y-%m-%dT%H%M")
    jsonl_pad = uit_map / f"dekkingstest-{stempel}.jsonl"

    print(f"aisstream-dekkingstest · {args.minuten:.0f} min · "
          f"vensters: {', '.join(args.vensters)}")
    print(f"ruwe berichten -> {jsonl_pad}")

    teller = Teller(args.vensters)
    with jsonl_pad.open("w", encoding="utf-8") as jsonl:
        try:
            asyncio.run(luister(key, args.vensters, teller, jsonl,
                                args.minuten * 60))
        except KeyboardInterrupt:
            print("\nafgebroken — rapport over wat er binnen is")

    teller.rapport()
    if jsonl_pad.stat().st_size:
        csv_pad = schrijf_csv(jsonl_pad)
        print(f"\nkepler.gl-CSV -> {csv_pad}")


if __name__ == "__main__":
    main()
