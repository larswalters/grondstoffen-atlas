#!/usr/bin/env python3
"""maak_leidingbeen_olie_omisalj_szazhalombatta.py - de leidingbenen van olie-omisalj-szazhalombatta (M31 golf 12).

Keten: JANAF-terminal Omisalj (eiland Krk) -> Adria-pijpleiding (Jadranski naftovod: Omisalj-Sisak 36 inch,
Sisak-Virje-Gola 28 inch) -> HR/HU-grens bij Gola -> MOL Adria-kooljvezetek (Csurgo, Osijek-Budapest, Sziszek-Budapest)
-> MOL Duna-raffinaderij, Szazhalombatta. Alles OSM man_made=pipeline substance=oil.

Geometrie: Overpass-uitvoer (way-id + geometry), vooraf in een cache gezet (olie-omisalj-szazhalombatta-overpass-cache.json,
ODbL). Ways worden gestikt op EXACT gelijke eindpunten (gedeelde OSM-nodes); expliciete way-volgorde, geen vrij kortste pad
(Barataag II / Druzhba, Virje-Lendava, Sisak-Slavonski Brod, Adria-Wien zijn niet opgenomen).

Benen (uitvoer in v2/build-cache/ais/graaf/):
  a1  Omisalj -> Sisak -> Virje -> Gola -> HR/HU-grens           (HR, 9 + 3 ways)
  a2  HR/HU-grens -> Sziszek-Budapest-einde bij Szazhalombatta   (HU, 8 ways)
De terminal-interne leidingen van Omisalj (OSM-manifold, zigzag van losse stukjes, geen doorlopende lijn) worden NIET getekend:
anker -> begin Omisalj-Sisak (2,1 km) en einde Sziszek-Budapest -> MOL-anker (1,1 km) zijn --stippel in bak_stromen.sh.

Draaien: python v2/tools/maak_leidingbeen_olie_omisalj_szazhalombatta.py --schrijf
"""
import json
import math
import os
import sys

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
PREFIX = "olie-omisalj-szazhalombatta"
CACHE = os.path.join(BEEN, PREFIX + "-overpass-cache.json")
R = 6371.0088

A1 = [276522179, 859729756, 859729755, 859729754, 275847497, 275847496, 263222529, 276191744, 275828600,
      580473505, 1050335120]
A2 = [930166671, 970100735, 970100734, 970087404, 970041355, 969606494, 968260293, 968438280]


def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def lengte(p):
    return sum(hav(p[i], p[i + 1]) for i in range(len(p) - 1))


def stik(ways, ids, begin=None, naad_max_km=0.05):
    """Stik ways in volgorde; elke way wordt zo georienteerd dat hij aansluit op het vorige eind.
    Gelijke eindpunten = 0 m naad; anders wordt de naad (<= naad_max_km) gemeld en met een recht stukje gelegd."""
    lijn, naden = None, []
    for k, i in enumerate(ids):
        g = [tuple(p) for p in ways[str(i)]["geom"]]
        if lijn is None:
            lijn = g if (begin is None or hav(g[0], begin) <= hav(g[-1], begin)) else g[::-1]
            continue
        e = lijn[-1]
        if hav(e, g[0]) <= hav(e, g[-1]):
            d, g2 = hav(e, g[0]), g
        else:
            d, g2 = hav(e, g[-1]), g[::-1]
        if d > naad_max_km:
            raise SystemExit("naad te groot bij way %s: %.3f km" % (i, d))
        naden.append((i, round(d * 1000, 1)))
        lijn = lijn + (g2 if d > 0 else g2[1:])
    return lijn, naden


def fc(lijn, naam):
    return {"type": "FeatureCollection", "features": [{
        "type": "Feature", "properties": {"name": naam},
        "geometry": {"type": "LineString", "coordinates": [[round(p[1], 7), round(p[0], 7)] for p in lijn]}}]}


def main():
    ways = json.load(open(CACHE, encoding="utf-8"))["ways"]
    uit = {}
    uit["a1"], n2 = stik(ways, A1)
    uit["a2"], n3 = stik(ways, A2)
    print("naden a1", n2, "a2", n3)
    for k, l in uit.items():
        print(k, "km %.1f" % lengte(l), "punten", len(l), "begin", l[0], "eind", l[-1])
    gap1 = hav((45.2208, 14.5331), uit["a1"][0])
    gap2 = hav(uit["a1"][-1], uit["a2"][0])
    print("stippel-gat anker Omisalj -> begin Omisalj-Sisak: %.2f km" % gap1)
    print("naad a1 -> a2 (HR/HU-grens): %.3f km" % gap2)
    print("totaal doorgetrokken %.1f km" % sum(lengte(l) for l in uit.values()))
    if "--schrijf" in sys.argv:
        os.makedirs(BEEN, exist_ok=True)
        namen = {"a1": "Adria-pijpleiding Omisalj-Sisak-Virje-Gola (OSM, Jadranski naftovod)",
                 "a2": "Adria-kooljvezetek MOL Gola-Csurgo-Szazhalombatta (OSM)"}
        for k, l in uit.items():
            p = os.path.join(BEEN, "%s-leiding-%s.geojson" % (PREFIX, k))
            json.dump(fc(l, namen[k]), open(p, "w", encoding="utf-8"))
            print("geschreven:", p)


if __name__ == "__main__":
    main()
