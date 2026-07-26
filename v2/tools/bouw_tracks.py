# bouw_tracks.py — van ruwe pings naar losse scheepstracks per corridor (LAR-530, stap 1).
#
# Leest collector-JSONL (aisstream-schema — maakt niet uit of de dag van de VPS
# komt of uit haal_marinecadastre.py) en bouwt per MMSI geordende tracks:
#
#   1. pings per schip sorteren op tijd;
#   2. knippen bij een tijdsprong (> KNIP_MIN) — dat zijn twee losse doorvaarten;
#   3. stilliggen eruit (SOG < VARE_GRENS) — een ligplaats is een plek, geen route;
#      een stilligpauze midden in een reeks knipt de track (aanleggen = einde been);
#   4. GPS-uitschieters eruit: een punt dat een onmogelijke snelheid impliceert
#      (> MAX_KNOPEN tegen beide buren) wordt overgeslagen;
#   5. tracks korter dan MIN_PUNTEN of MIN_KM weg (ruis, manoeuvreren op een kade).
#
# Bewust nog GEEN bundeling of graafbouw — eerst laten zien dat één doorvaart
# één vloeiende lijn in de geul is. De uitvoer is het zaad voor de graaf-stap.
#
# Gebruik:
#   python tools/bouw_tracks.py --bron build-cache/ais/marinecadastre \
#       --venster mississippi-breed --uit build-cache/ais/tracks/mississippi.json
#
# Uitvoer: {"venster": [z,w,n,o], "tracks": [{"mmsi": .., "punten": [[lat,lon,epoch_min], ..]}]}

import argparse
import gzip
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Vensters ruimer dan de collector-health-banen: de rivier moet erin blijven
# (pilot-les: de Mississippi meandert tussen Baton Rouge en Vicksburg west van
# lon -91,5 en viel zo uit het smalle venster — dat leek een dekkingsgat).
VENSTERS = {
    "mississippi-breed": (28.90, -92.50, 35.60, -89.00),
    "ohio-illinois":     (36.50, -90.50, 41.60, -84.00),
    "meren-seaway":      (41.00, -88.00, 47.50, -76.00),
    "rijnmond":          (51.75, 3.85, 52.05, 4.75),
    "rijn-corridor":     (51.15, 4.75, 52.10, 7.00),
}

KNIP_MIN = 30        # minuten zonder ping -> nieuwe track
VARE_GRENS = 0.5     # knopen; onder = stilliggend
MAX_KNOPEN = 40      # sneller dan dit tegen beide buren = GPS-uitschieter
MIN_PUNTEN = 8
MIN_KM = 2.0

POSITIE_SOORTEN = ("PositionReport", "StandardClassBPositionReport",
                   "ExtendedClassBPositionReport")


def km(lat1, lon1, lat2, lon2):
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1) * math.cos(math.radians((lat1 + lat2) / 2))
    return 6371.0 * math.hypot(dlat, dlon)


def lees_pings(bron: Path, venster):
    z, w, n, o = venster
    bestanden = sorted(bron.glob("*.jsonl.gz")) + sorted(bron.glob("*.jsonl"))
    bestanden = [b for b in bestanden if not b.name.startswith("ais-")]
    if not bestanden:
        sys.exit(f"geen jsonl(.gz) in {bron}")
    print(f"{len(bestanden)} dagbestand(en) uit {bron}")
    for pad in bestanden:
        opener = gzip.open if pad.suffix == ".gz" else open
        with opener(pad, "rt", encoding="utf-8", errors="replace") as fh:
            while True:
                try:
                    regel = next(fh)
                except StopIteration:
                    break
                except EOFError:
                    break            # levend gegzipt dagbestand — verwacht
                if "PositionReport" not in regel:
                    continue
                try:
                    b = json.loads(regel)
                    bericht = b["Message"]
                    for soort in POSITIE_SOORTEN:
                        if soort in bericht:
                            pr = bericht[soort]
                            break
                    else:
                        continue
                    lat, lon = pr["Latitude"], pr["Longitude"]
                    if not (z <= lat <= n and w <= lon <= o):
                        continue
                    meta = b["MetaData"]
                    tijd = datetime.strptime(meta["time_utc"][:26],
                                             "%Y-%m-%d %H:%M:%S.%f"
                                             ).replace(tzinfo=timezone.utc)
                except (json.JSONDecodeError, KeyError, ValueError, TypeError):
                    continue
                sog = pr.get("Sog")
                yield (meta.get("MMSI"), lat, lon,
                       int(tijd.timestamp() // 60),
                       sog if sog is not None else 0.0)


def bouw(pings):
    perschip = {}
    for mmsi, lat, lon, t_min, sog in pings:
        if mmsi is None:
            continue
        perschip.setdefault(mmsi, []).append((t_min, lat, lon, sog))

    tracks = []
    for mmsi, rijen in perschip.items():
        rijen.sort()
        huidig = []
        vorige_t = None
        for t_min, lat, lon, sog in rijen:
            if sog < VARE_GRENS:                      # stilliggen knipt de track
                if huidig:
                    tracks.append((mmsi, huidig))
                    huidig = []
                vorige_t = t_min
                continue
            if vorige_t is not None and t_min - vorige_t > KNIP_MIN and huidig:
                tracks.append((mmsi, huidig))
                huidig = []
            # dubbele minuut van hetzelfde schip: eerste wint (1-min-resolutie volstaat)
            if huidig and huidig[-1][2] == t_min:
                continue
            huidig.append((lat, lon, t_min))
            vorige_t = t_min
        if huidig:
            tracks.append((mmsi, huidig))

    # GPS-uitschieters: onmogelijke snelheid tegen béide buren -> punt weg.
    schoon = []
    uitschieters = 0
    for mmsi, punten in tracks:
        gefilterd = []
        for i, (lat, lon, t) in enumerate(punten):
            def te_snel(j):
                la, lo, tj = punten[j]
                dt_uur = max(abs(t - tj), 1) / 60.0
                return km(lat, lon, la, lo) / dt_uur > MAX_KNOPEN * 1.852
            if 0 < i < len(punten) - 1 and te_snel(i - 1) and te_snel(i + 1):
                uitschieters += 1
                continue
            gefilterd.append((lat, lon, t))
        lengte = sum(km(*gefilterd[i][:2], *gefilterd[i + 1][:2])
                     for i in range(len(gefilterd) - 1))
        if len(gefilterd) >= MIN_PUNTEN and lengte >= MIN_KM:
            schoon.append({"mmsi": mmsi, "km": round(lengte, 1),
                           "punten": [[round(la, 5), round(lo, 5), t]
                                      for la, lo, t in gefilterd]})
    schoon.sort(key=lambda tr: -tr["km"])
    return schoon, uitschieters


def main():
    p = argparse.ArgumentParser(description="Pings -> scheepstracks per corridor (LAR-530)")
    p.add_argument("--bron", type=Path, required=True,
                   help="map met collector-JSONL(.gz)-dagen")
    p.add_argument("--venster", required=True,
                   help=f"één van {', '.join(VENSTERS)} of 'z,w,n,o'")
    p.add_argument("--uit", type=Path, required=True)
    args = p.parse_args()

    venster = (VENSTERS.get(args.venster)
               or tuple(float(x) for x in args.venster.split(",")))
    begon = time.monotonic()
    tracks, uitschieters = bouw(lees_pings(args.bron, venster))
    tot_km = sum(t["km"] for t in tracks)
    tot_pt = sum(len(t["punten"]) for t in tracks)
    print(f"{len(tracks):,} tracks · {tot_km:,.0f} km · {tot_pt:,} punten · "
          f"{uitschieters} GPS-uitschieters weg · {time.monotonic()-begon:.0f}s")

    args.uit.parent.mkdir(parents=True, exist_ok=True)
    args.uit.write_text(json.dumps(
        {"venster": list(venster), "bron": str(args.bron.name),
         "tracks": tracks}, separators=(",", ":")), encoding="utf-8")
    print(f"geschreven: {args.uit} ({args.uit.stat().st_size/1e6:.1f} MB)")


if __name__ == "__main__":
    main()
