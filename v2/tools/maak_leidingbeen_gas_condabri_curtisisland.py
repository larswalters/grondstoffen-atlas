#!/usr/bin/env python3
"""maak_leidingbeen_gas_condabri_curtisisland.py - leidingbeen van gas-condabri-curtisisland.

APLNG-hoofdleiding (man_made=pipeline, substance=gas, usage=transmission, 1066 mm / 42 inch, operator APLNG,
ondergronds) van het beginstation bij de Woleebee Lateral (-26.3199, 150.1948) naar Curtis Island: acht OSM-ways
uit de lokale Geofabrik-pbf (australie), gestikt tot een LineString. Schrijft een FeatureCollection naar
v2/build-cache/ais/graaf/gas-condabri-curtisisland-leiding-aplng.geojson (--been-geojson "leiding|...").
Niet de parallelle leidingen naar Gladstone (APA 618217685, Santos/GLNG 618217686): andere operators.
Bron: OpenStreetMap-bijdragers (ODbL).

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_condabri_curtisisland.py
"""
import json
import math
import os

import osmium

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
PBF = os.path.join(WORTEL, "build-cache", "geofabrik", "australie-latest.osm.pbf")
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "gas-condabri-curtisisland-leiding-aplng.geojson")
KETEN = [1358316289, 1358316292, 1358316293, 1358316296, 1358316287, 1358316299, 1356547330, 618217684]


def hv(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))


def main():
    wens = set(KETEN)
    ways = {}
    fp = osmium.FileProcessor(PBF, osmium.osm.WAY | osmium.osm.NODE).with_locations().with_filter(
        osmium.filter.TagFilter(("man_made", "pipeline")))
    for o in fp:
        if o.is_way() and o.id in wens:
            ways[o.id] = [(n.lon, n.lat) for n in o.nodes]
    pts = []
    for w in KETEN:
        p = ways[w]
        if pts:
            if hv(pts[-1], p[0]) > hv(pts[-1], p[-1]):
                p = p[::-1]
            naad = hv(pts[-1], p[0]) * 1000
            print(f"  way {w}: {sum(hv(p[i], p[i+1]) for i in range(len(p)-1)):.1f} km, naad {naad:.0f} m")
            if naad < 0.5:
                p = p[1:]
        else:
            print(f"  way {w}: {sum(hv(p[i], p[i+1]) for i in range(len(p)-1)):.1f} km (begin)")
        pts += p
    km = sum(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    grootste = max(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature", "properties": {"name": "APLNG-hoofdleiding 42 inch (8 OSM-ways) Surat Basin - Curtis Island"},
        "geometry": {"type": "LineString", "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(fc, f)
    print(f"{len(pts)} punten, {km:.1f} km, grootste segment {grootste:.1f} km; begin {pts[0][1]:.4f},{pts[0][0]:.4f}; "
          f"eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n-> {UIT}")


if __name__ == "__main__":
    main()
