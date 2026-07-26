# bak_aistracks.py — een selectie echte scheepstracks als kijk-laag voor de bol.
#
# De bol is de echte toets (niet de matplotlib-plaatjes): liggen de gevaren
# lijnen in de geul op satelliet, zie je op- en afvaart als eigen banen, en
# eindigen benen op de dokken? Deze baker maakt daarvoor v2/data/
# aistracks-pilot.json uit de uitvoer van bouw_tracks.py.
#
# Bewust een SELECTIE, geen alles: de volle trackset is ~200 MB JSON en de
# kijkvraag heeft aan een paar honderd lange doorvaarten per richting genoeg.
# De graaf-stap (LAR-530) rekent straks gewoon op de volledige build-cache-set.
#
#   python tools/bak_aistracks.py \
#       --tracks build-cache/ais/tracks/mississippi.json build-cache/ais/tracks/ohio-illinois.json \
#       --uit data/aistracks-pilot.json
#
# Formaat = het aisnet-pilot-patroon (punten als [lon, lat]) + `richting`:
#   {"bron": ..., "vensters": {naam: [z,w,n,o]}, "lijnen":
#     [{"venster": naam, "richting": "op"|"af", "punten": [[lon,lat], ...]}]}

import argparse
import json
import math
from pathlib import Path

PER_RICHTING = 400        # langste N tracks per venster per richting
TOL_M = 40.0              # Douglas-Peucker; een geul is ~200 m+, dus 40 m is veilig


def dp(punten, tol_m):
    """Douglas-Peucker op [lat, lon]-punten (equirectangulair, prima op geul-schaal)."""
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
    p.add_argument("--tracks", type=Path, nargs="+", required=True)
    p.add_argument("--uit", type=Path, required=True)
    p.add_argument("--per-richting", type=int, default=PER_RICHTING)
    p.add_argument("--tol-m", type=float, default=TOL_M)
    args = p.parse_args()

    vensters = {}
    lijnen = []
    for pad in args.tracks:
        d = json.loads(pad.read_text(encoding="utf-8"))
        naam = pad.stem
        vensters[naam] = d["venster"]
        per = {"op": [], "af": []}
        for t in d["tracks"]:
            r = ("op" if (t["dlat"] if abs(t["dlat"]) >= abs(t["dlon"])
                          else t["dlon"]) > 0 else "af")
            per[r].append(t)
        for r, ts in per.items():
            ts.sort(key=lambda t: -t["km"])
            gekozen = ts[:args.per_richting]
            n_in = sum(len(t["punten"]) for t in gekozen)
            n_uit = 0
            for t in gekozen:
                pts = dp([[p_[0], p_[1]] for p_ in t["punten"]], args.tol_m)
                n_uit += len(pts)
                lijnen.append({"venster": naam, "richting": r,
                               "punten": [[round(lo, 5), round(la, 5)]
                                          for la, lo in pts]})
            print(f"{naam}/{r}: {len(gekozen)} tracks · "
                  f"{n_in:,} -> {n_uit:,} punten (DP {args.tol_m:.0f} m)")

    doc = {"bron": "MarineCadastre (NOAA/USACE, publiek domein) via "
                   "haal_marinecadastre.py + bouw_tracks.py",
           "vensters": vensters, "lijnen": lijnen}
    args.uit.write_text(json.dumps(doc, separators=(",", ":")), encoding="utf-8")
    print(f"geschreven: {args.uit} — {args.uit.stat().st_size/1e6:.1f} MB · "
          f"{len(lijnen)} lijnen")


if __name__ == "__main__":
    main()
