#!/usr/bin/env python3
"""maak_tongling_oostgeul.py — MIDDELLIJN van de Tongling-oostgeul (noordaanvaart).

Waarom: OSM legt de navigeerbare Yangtze-middellijn bij Tongling langs de
WESTgeul om het eiland, terwijl de kade van de nieuwe Tongling Nonferrous-
kopersmelter aan de OOSTgeul ligt (117,772 / 30,987; kade-tip 30,982 → begin
30,991, smelter op 117,781 / 30,987). Die oostgeul heeft in OSM geen
`waterway`-middellijn, alleen `natural=water`-vlak — het Amazone-geval.

De kade ligt bij het BEGIN van de splitsing (noordpunt van het eiland). Het
schip komt van benedenstrooms (NE) de hoofdgeul af, gaat bij de noordpunt de
oostgeul in en zakt naar de kade. Daarom leiden we ALLEEN de noordaanvaart af
(kade → noordelijke hoofdgeul-knoop): dat geeft een schone route zonder de lus
om het hele eiland die ontstond toen de oostgeul óók aan de zuidkant hing (de
router koos dan de westgeul + zuidjunctie).

Aanpak:
  1. `vaarpad` over de watervlakken (167 m-raster over de noordpunt), van het
     kade-waterpunt naar een échte hoofdgeul-knoop die de router al gebruikt
     (117,897 / 31,077). Zo sluit het noordeinde aan op de graaf.
  2. Water-constrained simplify: een punt wordt alleen weggelaten als de rechte
     buur→buur AANTOONBAAR op watercellen blijft. Geen enkel segment over land
     (Lars' eis: "ze raken land" mag niet).

Uitvoer: v2/data/vaarwegen-handmatig.geojson (gecommit, klein). Bakken:
    python v2/tools/bake_marnet.py --binnenwater \
        --bulk build-cache/vaarwegen_bulk.geojson \
        --extra-vaarwegen data/vaarwegen-handmatig.geojson \
        --bruggen build-cache/vaarwegen_bruggen.geojson \
        --meren build-cache/vaarwegen_meren.geojson \
        --heal-km 0.25 --corridor-km 2.0
"""

import json
import math
import os

import numpy as np

import middellijn_uit_vlakken as mv

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)

BBOX = (30.94, 117.72, 31.14, 117.94)   # noordpunt van het eiland
CEL = 0.0015                            # 167 m — fijn genoeg voor de smalle geul
HAVEN = (117.7695, 30.9865)             # waterpunt vlak west van de kade-tip
NOORD_KNOOP = (117.897, 31.077)         # hoofdgeul-knoop die de router al gebruikt


def km(a, b):
    return 6371 * math.acos(min(1, math.sin(math.radians(a[1])) * math.sin(math.radians(b[1]))
                            + math.cos(math.radians(a[1])) * math.cos(math.radians(b[1]))
                            * math.cos(math.radians(b[0] - a[0]))))


def main():
    lons, lats, masker, klaring = mv.raster(["china"], BBOX, CEL)
    dlon, dlat = lons[1] - lons[0], lats[1] - lats[0]

    def water(lo, la):
        j = int(round((lo - lons[0]) / dlon))
        i = int(round((la - lats[0]) / dlat))
        return 0 <= i < masker.shape[0] and 0 <= j < masker.shape[1] and bool(masker[i, j])

    def wet(a, b):
        n = max(3, int(km(a, b) / 0.04))
        return all(water(a[0] + (b[0] - a[0]) * t / n, a[1] + (b[1] - a[1]) * t / n)
                   for t in range(n + 1))

    def simp(P):
        out = [P[0]]
        i = 0
        while i < len(P) - 1:
            j = len(P) - 1
            while j > i + 1 and not wet(P[i], P[j]):
                j -= 1
            out.append(P[j])
            i = j
        return out

    pad, _ = mv.vaarpad(lons, lats, klaring, HAVEN, NOORD_KNOOP, min_klaring=0.06)
    lijn = simp([tuple(round(x, 5) for x in p) for p in pad])

    droog = [i for i in range(len(lijn) - 1) if not wet(lijn[i], lijn[i + 1])]
    if droog:
        raise SystemExit(f"segment(en) over land: {droog} — raster/ankers checken")
    tot = sum(km(lijn[i], lijn[i + 1]) for i in range(len(lijn) - 1))
    dichtst = min(km((117.7717, 30.98236), p) for p in lijn)
    print(f"oostgeul-noordaanvaart: {len(lijn)} punten · {tot:.1f} km · alles op water · "
          f"kade-tip op {dichtst:.2f} km")

    feat = {"type": "Feature",
            "properties": {"label": "bulk-cn", "regio": "cn", "zeevaart": False,
                           "signaal": "ship", "km": round(tot, 3),
                           "wayId": "tongling-oostgeul-noord",
                           "bron": "middellijn afgeleid uit natural=water (China-extract, "
                                   "ODbL) via middellijn_uit_vlakken.py (vaarpad, 167 m), "
                                   "water-constrained; noordeinde op de hoofdgeul-knoop "
                                   "117,897/31,077 — de kade snapt op het HAVEN-uiteinde"},
            "geometry": {"type": "LineString",
                         "coordinates": [[round(p[0], 5), round(p[1], 5)] for p in lijn]}}
    out = {"type": "FeatureCollection",
           "toelichting": "Handmatig afgeleide vaarweglijnen (niet uit de OSM-fetch). "
                          "Herleiden: tools/maak_tongling_oostgeul.py. Voeg toe met "
                          "bake_marnet.py --extra-vaarwegen.",
           "features": [feat]}
    pad_uit = os.path.join(V2, "data", "vaarwegen-handmatig.geojson")
    json.dump(out, open(pad_uit, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"geschreven: {pad_uit}")


if __name__ == "__main__":
    main()
