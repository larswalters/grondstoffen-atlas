#!/usr/bin/env python3
"""maak_leidingbeen_gas_moomba_wilton.py - leidingbeen van gas-moomba-wilton.

Moomba-Sydney Gas Pipeline (man_made=pipeline, operator APA, DN850): een enkele OSM-way (412224720) uit de lokale
Geofabrik-pbf (australie), van Moomba (-28.1157, 140.2062) naar Wilton (-34.2330, 150.7106). Schrijft een FeatureCollection
naar v2/build-cache/ais/graaf/gas-moomba-wilton-leiding-msp.geojson (--been-geojson "leiding|...").
Niet het Horsley Park-verlengstuk (way 1421707510, 50,9 km). Bron: OpenStreetMap-bijdragers (ODbL).

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_moomba_wilton.py
"""
import json
import math
import os

import osmium

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
PBF = os.path.join(WORTEL, "build-cache", "geofabrik", "australie-latest.osm.pbf")
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "gas-moomba-wilton-leiding-msp.geojson")
KETEN = [412224720]


def hv(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))


def main():
    wens = set(KETEN)
    ways = {}
    tags = {}
    fp = osmium.FileProcessor(PBF, osmium.osm.WAY | osmium.osm.NODE).with_locations().with_filter(
        osmium.filter.TagFilter(("man_made", "pipeline")))
    for o in fp:
        if o.is_way() and o.id in wens:
            ways[o.id] = [(n.lon, n.lat) for n in o.nodes]
            tags[o.id] = dict(o.tags)
    pts = []
    for w in KETEN:
        p = ways[w]
        print(f"  way {w}: {sum(hv(p[i], p[i+1]) for i in range(len(p)-1)):.1f} km, {len(p)} nodes, tags {tags[w]}")
        pts += p
    km = sum(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    grootste = max(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature", "properties": {"name": "Moomba-Sydney Gas Pipeline DN850 (OSM way 412224720) Moomba - Wilton"},
        "geometry": {"type": "LineString", "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(fc, f)
    print(f"{len(pts)} punten, {km:.1f} km, grootste segment {grootste:.1f} km; begin {pts[0][1]:.4f},{pts[0][0]:.4f}; "
          f"eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n-> {UIT}")


if __name__ == "__main__":
    main()
