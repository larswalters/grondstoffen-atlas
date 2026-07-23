#!/usr/bin/env python3
"""maak_tongling_oostgeul.py — MIDDELLIJN van de Tongling-oostgeul.

Waarom: bij Tongling legt OSM de navigeerbare Yangtze-middellijn langs de
WESTgeul om het eiland, terwijl álle Tongling-piers (incl. de Tongling
Nonferrous koperloskade) aan de OOSTgeul liggen. Die oostgeul heeft in OSM geen
`waterway`-middellijn, alleen `natural=water`-vlak — het Amazone-geval. Zonder
oostgeul-lijn snapt de kade 3,7 km over het eiland op de westgeul (route over
land). Met deze lijn stroomt het schip van benedenstrooms (noord) de oostgeul in
en dokt aan de juiste pier, over water.

Aanpak:
  1. `middellijn_uit_vlakken.vaarpad` over de watervlakken (gecached raster),
     met ankers ín het doorlopende oostgeul-component (comp 8: lat 30,91–31,06).
     Dat geeft een GLAD midden-hugend pad (geen raster-hoeken).
  2. Aan beide uiteinden een aansluiting op de hoofd-Yangtze:
       - zuid op de hoofdgeul-VERTEX (117,7373 / 30,9102) → valt in de graaf
         samen met een knoop, via een nat tussenpunt (117,749 / 30,921) om de
         eilandpunt;
       - noord op de hoofdgeul-LIJN (117,758 / 31,046) → de tier-1 heal
         projecteert dit uiteinde erop (de hoofdgeul zwenkt hier oostwaarts).
  3. ELK segment wordt tegen het watermasker geverifieerd (assert): geen enkel
     stuk mag over land lopen — dat was de eis van Lars ("ze raken land").

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

BBOX = (30.78, 117.66, 31.06, 117.86)
CEL = 0.003
# ankers ín het doorlopende oostgeul-component (comp 8)
ANKER_ZUID = (117.760, 30.920)
ANKER_NOORD = (117.762, 31.045)
# aansluiting op de hoofd-Yangtze
MAIN_ZUID = (117.7373, 30.9102)     # hoofdgeul-vertex → graafknoop
TUSSEN_ZUID = (117.749, 30.921)     # nat punt om de eilandpunt
NOORD_OP_MAIN = (117.758, 31.046)   # op de hoofdgeul-lijn → heal projecteert


def km(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    return 6371 * math.acos(min(1, math.sin(p1) * math.sin(p2)
                            + math.cos(p1) * math.cos(p2) * math.cos(dl)))


def main():
    lons, lats, masker, klaring = mv.raster(["china"], BBOX, CEL)
    dlon, dlat = lons[1] - lons[0], lats[1] - lats[0]

    def water(lo, la):
        j = int(round((lo - lons[0]) / dlon))
        i = int(round((la - lats[0]) / dlat))
        return 0 <= i < masker.shape[0] and 0 <= j < masker.shape[1] and bool(masker[i, j])

    def wet(a, b):
        n = max(3, int(km(a, b) / 0.07))
        return all(water(a[0] + (b[0] - a[0]) * t / n, a[1] + (b[1] - a[1]) * t / n)
                   for t in range(n + 1))

    # gladde middenlijn door de oostgeul
    pad, _ = mv.vaarpad(lons, lats, klaring, ANKER_ZUID, ANKER_NOORD, min_klaring=0.08)
    strak = mv.simplify(mv.strak_trekken(pad, lons, lats, klaring >= 0.08), 0.25)
    # de padvinder-lijn zit ín comp 8; knip de uiteinden op de aansluitpunten
    binnen = [tuple(round(x, 5) for x in p) for p in strak]
    lijn = [MAIN_ZUID, TUSSEN_ZUID] + binnen[1:-1] + [NOORD_OP_MAIN]

    droog = [i for i in range(len(lijn) - 1) if not wet(lijn[i], lijn[i + 1])]
    if droog:
        raise SystemExit(f"segment(en) over land: {droog} — raster/ankers checken")

    # ⚠️ EEN KNOOP BIJ DE PIER, ANDERS SNAPT DE KADE OP DE WESTGEUL.
    # Aansluitingen snappen op KNOPEN, en de bake zet knopen op lijn-UITEINDEN +
    # elke ~10 km. Als één doorlopende lijn heeft de oostgeul bij de pier geen
    # knoop (die valt tussen twee 10 km-knopen), dus de dichtstbijzijnde knoop
    # blijft de westgeul op 3,7 km en de route negeert de oostgeul. Daarom
    # knippen we de lijn in TWEE features op het punt dat het dichtst bij de
    # pier ligt: dat gedeelde uiteinde wordt een knoop (kade snapt erop, ~0,6 km)
    # en de router stroomt van benedenstrooms (noord) de oostgeul in.
    PIER = (117.773, 30.939)
    # dichtstbijzijnde lijn-vertex bij de pier als knippunt
    ksplit = min(range(len(lijn)), key=lambda i: km(PIER, lijn[i]))
    ksplit = max(1, min(len(lijn) - 2, ksplit))     # niet op een uiteinde knippen
    deel_a = lijn[:ksplit + 1]
    deel_b = lijn[ksplit:]
    tot = sum(km(lijn[i], lijn[i + 1]) for i in range(len(lijn) - 1))
    print(f"oostgeul: {len(lijn)} punten · {tot:.1f} km · alles op water · "
          f"pier-knoop op {km(PIER, lijn[ksplit]):.2f} km · gesplitst bij "
          f"({lijn[ksplit][0]:.4f}, {lijn[ksplit][1]:.4f})")

    def maak(coords, deelnaam):
        return {"type": "Feature",
                "properties": {"label": "bulk-cn", "regio": "cn", "zeevaart": False,
                               "signaal": "ship",
                               "km": round(sum(km(coords[i], coords[i + 1])
                                               for i in range(len(coords) - 1)), 3),
                               "wayId": f"tongling-oostgeul-{deelnaam}",
                               "bron": "middellijn afgeleid uit natural=water "
                                       "(China-extract, ODbL) via middellijn_uit_vlakken.py "
                                       "(vaarpad); elk segment op watercellen geverifieerd; "
                                       "gesplitst bij de pier zodat de kade daar op een "
                                       "knoop snapt; zuideinde op hoofdgeul-vertex, "
                                       "noordeinde op de hoofdgeul-lijn (heal projecteert)"},
                "geometry": {"type": "LineString",
                             "coordinates": [[round(p[0], 5), round(p[1], 5)] for p in coords]}}
    out = {"type": "FeatureCollection",
           "toelichting": "Handmatig afgeleide vaarweglijnen (niet uit de OSM-fetch). "
                          "Herleiden: tools/maak_tongling_oostgeul.py. Voeg toe met "
                          "bake_marnet.py --extra-vaarwegen.",
           "features": [maak(deel_a, "zuid"), maak(deel_b, "noord")]}
    pad_uit = os.path.join(V2, "data", "vaarwegen-handmatig.geojson")
    json.dump(out, open(pad_uit, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"geschreven: {pad_uit}")


if __name__ == "__main__":
    main()
