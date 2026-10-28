#!/usr/bin/env python3
"""maak_leidingbeen_olie_haoudelhamra_skikda.py - b1 van olie-haoudelhamra-skikda.

Brief: v2/design/routebrieven/olie-haoudelhamra-skikda.md (b1). OSM-way 379118067
(man_made=pipeline, substance=oil, operator Sonatrach, ongetagd: OK1 of NK1) uit het
lokale Geofabrik-extract `algerije`, letterlijk doorgetrokken van het tankenpark
Haoud el Hamra (31.8836,5.9903) naar het OSM-eind (36.2508,6.4205).

Uitvoer: v2/build-cache/ais/graaf/olie-haoudelhamra-skikda-leiding-ok1.geojson
(FeatureCollection, een LineString, [lon,lat], van Haoud el Hamra naar het OSM-eind).

Draaien:  python -I -X utf8 v2/tools/maak_leidingbeen_olie_haoudelhamra_skikda.py --schrijf
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys

import osmium

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
PBF = os.path.join(WORTEL, "build-cache", "geofabrik", "algerije-latest.osm.pbf")
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "olie-haoudelhamra-skikda-leiding-ok1.geojson")

WAY_ID = 379118067
KOP = (5.9903, 31.8836)      # (lon, lat) anker Haoud el Hamra
R = 6371.0088


def km(a, b):
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def haal_way():
    for obj in (osmium.FileProcessor(PBF).with_locations()
                .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
                .with_filter(osmium.filter.KeyFilter("man_made"))):
        if obj.id != WAY_ID:
            continue
        tags = {t.k: t.v for t in obj.tags}
        pts = [(n.location.lon, n.location.lat) for n in obj.nodes if n.location.valid()]
        return tags, pts
    return None, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()
    tags, pts = haal_way()
    if not pts:
        print(f"way {WAY_ID} niet gevonden in {PBF}")
        return 1
    print(f"way {WAY_ID}: {len(pts)} knopen, tags {tags}")
    if km(pts[0], KOP) > km(pts[-1], KOP):
        pts.reverse()
    lengte = sum(km(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    print(f"lengte {lengte:.1f} km; kop {pts[0][1]:.5f},{pts[0][0]:.5f} ({km(pts[0], KOP):.3f} km van anker); "
          f"eind {pts[-1][1]:.5f},{pts[-1][0]:.5f}")
    if args.schrijf:
        doc = {"type": "FeatureCollection", "features": [{
            "type": "Feature",
            "properties": {
                "naam": "OK1 Haoud el Hamra naar OSM-eind (OSM-way 379118067, ongetagd: OK1 of NK1)",
                "km": round(lengte, 2),
                "punten": len(pts),
                "bron": "OpenStreetMap-bijdragers (ODbL), extract algerije, way 379118067, man_made=pipeline substance=oil",
                "gereedschap": "maak_leidingbeen_olie_haoudelhamra_skikda.py",
            },
            "geometry": {"type": "LineString",
                         "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]},
        }]}
        os.makedirs(os.path.dirname(UIT), exist_ok=True)
        with open(UIT, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False)
        print(f"geschreven: {UIT} ({os.path.getsize(UIT)/1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
