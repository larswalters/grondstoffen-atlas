#!/usr/bin/env python3
"""maak_tongling_oostgeul.py — leidt de MIDDELLIJN van de Tongling-oostgeul af.

Waarom: bij Tongling ligt de Yangtze-navigatielijn in OSM langs de WESTgeul om
het eiland heen, terwijl álle Tongling-piers (incl. de Tongling Nonferrous
loskade) aan de OOSTgeul liggen. Die oostgeul heeft in OSM geen `waterway`-
middellijn, alleen `natural=water`-vlak — precies het Amazone-geval. Zonder
oostgeul-lijn snapt de kade 3,7 km over het eiland op de westgeul (route over
land). Met deze lijn volgt het schip de oostgeul en dokt aan de juiste pier.

Aanpak = `middellijn_uit_vlakken.py`: watervlakken → raster → klaring → per
breedtegraad het zwaartepunt van de OOST-watercluster (lon 117,755–117,800; de
uitschieter naar het Nanhu-meer geklemd) → Douglas-Peucker → uiteinden vastgezet
op de exacte hoofd-Yangtze-vertices (zodat ze in de graaf samenvallen).

Uitvoer: v2/data/vaarwegen-handmatig.geojson (gecommit, klein). Daarna bakken met
    python v2/tools/bake_marnet.py --binnenwater \
        --bulk build-cache/vaarwegen_bulk.geojson \
        --extra-vaarwegen data/vaarwegen-handmatig.geojson \
        --bruggen build-cache/vaarwegen_bruggen.geojson \
        --meren build-cache/vaarwegen_meren.geojson \
        --heal-km 0.25 --corridor-km 2.0

Deterministisch (raster gecached op extract+bbox+cel); geen netwerk nodig zodra
de china-extract er is.
"""

import json
import math
import os

import numpy as np

import middellijn_uit_vlakken as mv

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)

BBOX = (30.78, 117.66, 31.06, 117.86)   # la0, lo0, la1, lo1 — het eiland + tips
CEL = 0.003
# de exacte hoofd-Yangtze-vertices (way 226556520) waar de oostgeul aanknoopt,
# zodat de bake ze op dezelfde knoop kwantiseert (BULK_QUANT ~1 m)
ZUID = [117.73542, 30.89364]
NOORD = [117.73949, 31.04238]
LON_MIN, LON_MAX = 117.755, 117.800     # oost-cluster; > LON_MAX = Nanhu-meer


def lengte_km(P):
    s = 0.0
    for i in range(len(P) - 1):
        a, b = P[i], P[i + 1]
        s += 6371 * math.acos(min(1, math.sin(math.radians(a[1])) * math.sin(math.radians(b[1]))
             + math.cos(math.radians(a[1])) * math.cos(math.radians(b[1]))
             * math.cos(math.radians(b[0] - a[0]))))
    return s


def dp(P, tol_km):
    if len(P) < 3:
        return P

    def d(p, a, b):
        cx = math.cos(math.radians(p[1]))
        ax, bx, px = a[0] * cx, b[0] * cx, p[0] * cx
        ay, by, py = a[1], b[1], p[1]
        dx, dy = bx - ax, by - ay
        if dx == dy == 0:
            return math.hypot(px - ax, py - ay) * 111.32
        t = max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
        return math.hypot(px - ax - t * dx, py - ay - t * dy) * 111.32

    dmax, idx = 0, 0
    for i in range(1, len(P) - 1):
        dd = d(P[i], P[0], P[-1])
        if dd > dmax:
            dmax, idx = dd, i
    if dmax > tol_km:
        return dp(P[:idx + 1], tol_km)[:-1] + dp(P[idx:], tol_km)
    return [P[0], P[-1]]


def main():
    lons, lats, masker, klaring = mv.raster(["china"], BBOX, CEL)
    pts = []
    for i in range(masker.shape[0]):
        lat = lats[i]
        if lat < 30.90 or lat > 31.043:
            continue
        rij = np.flatnonzero(masker[i] & (klaring[i] > 0.08))
        oost = [j for j in rij if LON_MIN <= lons[j] <= LON_MAX]
        if not oost:
            continue
        w = klaring[i][oost]
        lon_c = float(np.average(lons[np.array(oost)], weights=w))
        pts.append([round(lon_c, 4), round(float(lat), 4)])

    lijn = dp([ZUID] + pts + [NOORD], 0.15)
    print(f"oostgeul: {len(lijn)} punten · {lengte_km(lijn):.1f} km")

    feat = {"type": "Feature",
            "properties": {"label": "bulk-cn", "regio": "cn", "zeevaart": False,
                           "signaal": "ship", "km": round(lengte_km(lijn), 3),
                           "wayId": "tongling-oostgeul-afgeleid",
                           "bron": "middellijn afgeleid uit natural=water (China-extract, "
                                   "ODbL) met middellijn_uit_vlakken.py — OSM heeft de "
                                   "Tongling-oostgeul alleen als watervlak, niet als "
                                   "navigatielijn"},
            "geometry": {"type": "LineString", "coordinates": lijn}}
    uit = {"type": "FeatureCollection",
           "toelichting": "Handmatig afgeleide vaarweglijnen die NIET uit de OSM-fetch "
                          "komen. De grote vaarwegen_bulk.geojson staat in build-cache "
                          "(gitignored, regenereerbaar). Deze paar committen mee. Voeg toe "
                          "aan de bake met --extra-vaarwegen. Herleiden: "
                          "tools/maak_tongling_oostgeul.py.",
           "features": [feat]}
    pad = os.path.join(V2, "data", "vaarwegen-handmatig.geojson")
    json.dump(uit, open(pad, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"geschreven: {pad}")


if __name__ == "__main__":
    main()
