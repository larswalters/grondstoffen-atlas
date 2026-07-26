# bak_aistracks.py — echte scheepstracks als kijk-laag voor de bol.
#
# Leest de JSONL.gz van bouw_tracks.py (één track per regel, landelijk) en
# selecteert wat de bol nodig heeft. Geen vensters meer — de pilot-vensters
# gaven precies de "afgekapte rivier" die Lars op de bol zag.
#
# De selectie is DEKKINGSGEDREVEN, niet volume-gedreven: een track wordt
# opgenomen als hij genoeg nog-onbezette 0,01°-cellen (~1 km) dekt. Zo haalt
# élke zijrivier, elk kanaal en elke havenarm de bol (de eerste track daar is
# per definitie nieuw), terwijl de duizenden herhaal-doorvaarten op de
# hoofdvaarweg niet allemaal meegaan. Op- en afvaart tellen als gescheiden
# celruimtes, zodat beide vaarbanen van een geul gedekt blijven.
#
#   python tools/bak_aistracks.py \
#       --tracks build-cache/ais/tracks/vs-landelijk.jsonl.gz \
#       --uit data/aistracks-pilot.json
#
# Uitvoer (aisnet-patroon, punten als [lon, lat]):
#   {"bron": ..., "lijnen": [{"richting": "op"|"af", "punten": [[lon,lat], ..]}]}

import argparse
import gzip
import json
import math
from pathlib import Path

CEL = 0.01                # ~1 km — de dekkings-korrel
MIN_NIEUW = 6             # cellen die een track nieuw moet dekken om mee te gaan
MAX_PUNTEN = 1_200_000    # puntenbudget van het bol-bestand (na verdunning)
TOL_M = 40.0              # Douglas-Peucker


def dp(punten, tol_m):
    if len(punten) < 3:
        return punten
    cosl = math.cos(math.radians(punten[0][0]))
    m_per_graad = 111_320.0

    def afstand(p, a, b):
        ax, ay = a[1] * cosl, a[0]
        bx, by = b[1] * cosl, b[0]
        px, py = p[1] * cosl, p[0]
        dx, dy = bx - ax, by - ay
        l2 = dx * dx + dy * dy
        if l2 == 0:
            return math.hypot(px - ax, py - ay) * m_per_graad
        t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / l2))
        return math.hypot(px - (ax + t * dx), py - (ay + t * dy)) * m_per_graad

    houden = [0, len(punten) - 1]
    stapel = [(0, len(punten) - 1)]
    while stapel:
        i0, i1 = stapel.pop()
        if i1 - i0 < 2:
            continue
        verste, dmax = -1, tol_m
        for i in range(i0 + 1, i1):
            dist = afstand(punten[i], punten[i0], punten[i1])
            if dist > dmax:
                verste, dmax = i, dist
        if verste >= 0:
            houden.append(verste)
            stapel.append((i0, verste))
            stapel.append((verste, i1))
    return [punten[i] for i in sorted(set(houden))]


def main():
    p = argparse.ArgumentParser(description="Track-selectie bakken voor de bol")
    p.add_argument("--tracks", type=Path, nargs="+", required=True,
                   help="jsonl.gz van bouw_tracks.py")
    p.add_argument("--uit", type=Path, required=True)
    p.add_argument("--max-punten", type=int, default=MAX_PUNTEN)
    p.add_argument("--min-nieuw", type=int, default=MIN_NIEUW)
    p.add_argument("--tol-m", type=float, default=TOL_M)
    args = p.parse_args()

    bezet = {"op": set(), "af": set()}
    lijnen = []
    n_punten = 0
    n_gezien = n_gekozen = 0
    for pad in args.tracks:
        with gzip.open(pad, "rt", encoding="utf-8") as fh:
            for regel in fh:
                t = json.loads(regel)
                n_gezien += 1
                r = ("op" if (t["dlat"] if abs(t["dlat"]) >= abs(t["dlon"])
                              else t["dlon"]) > 0 else "af")
                cellen = {(round(p_[0] / CEL), round(p_[1] / CEL))
                          for p_ in t["punten"]}
                nieuw = cellen - bezet[r]
                # naarmate het budget volloopt wordt de laag kieskeuriger:
                # nieuwe gebieden blijven binnenkomen, herhaling steeds minder
                vol = n_punten / args.max_punten
                drempel = args.min_nieuw + int(vol * vol * 60)
                if len(nieuw) < drempel:
                    continue
                bezet[r] |= cellen
                pts = dp([[p_[0], p_[1]] for p_ in t["punten"]], args.tol_m)
                n_punten += len(pts)
                n_gekozen += 1
                lijnen.append({"richting": r,
                               "punten": [[round(lo, 5), round(la, 5)]
                                          for la, lo in pts]})

    doc = {"bron": "MarineCadastre (NOAA/USACE, publiek domein) — "
                   "dekkingsgedreven selectie via bak_aistracks.py",
           "lijnen": lijnen}
    args.uit.write_text(json.dumps(doc, separators=(",", ":")), encoding="utf-8")
    op = sum(1 for l in lijnen if l["richting"] == "op")
    print(f"{n_gekozen:,} van {n_gezien:,} tracks gekozen "
          f"(op {op:,} · af {n_gekozen-op:,}) · {n_punten:,} punten · "
          f"{args.uit.stat().st_size/1e6:.1f} MB -> {args.uit}")


if __name__ == "__main__":
    main()
