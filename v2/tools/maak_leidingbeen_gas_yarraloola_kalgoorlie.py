#!/usr/bin/env python3
"""maak_leidingbeen_gas_yarraloola_kalgoorlie.py - leidingbeen van gas-yarraloola-kalgoorlie.

Goldfields Gas Pipeline (man_made=pipeline, substance=gas, operator APA, DN350-400): acht OSM-ways uit de lokale
Geofabrik-pbf (australie), van de lijnkop bij de Pilbara-kust via de DBNGP-aftakking Yarraloola (-21.4450, 115.9557)
naar het eindstation bij Kalgoorlie (-30.8657, 121.4805). Way 186178339 loopt in OSM tegen de reisrichting in en wordt
omgekeerd. Schrijft een FeatureCollection naar v2/build-cache/ais/graaf/gas-yarraloola-kalgoorlie-leiding-ggp.geojson
(--been-geojson "leiding|..."). Niet getekend: Newman-lateral, laterals Wiluna/Mt Keith/Leinster/Parkeston,
Kalgoorlie-Kambalda-leiding (way 579631964). Bron: OpenStreetMap-bijdragers (ODbL).

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_yarraloola_kalgoorlie.py
"""
import json
import math
import os

import osmium

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
PBF = os.path.join(WORTEL, "build-cache", "geofabrik", "australie-latest.osm.pbf")
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "gas-yarraloola-kalgoorlie-leiding-ggp.geojson")
KETEN = [579631963, 106538223, 1421965205, 376247352, 186178339, 218817589, 426111593, 426111599]


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
    ontbreekt = [w for w in KETEN if w not in ways]
    if ontbreekt:
        raise SystemExit(f"ways ontbreken in de pbf: {ontbreekt}")
    pts = []
    naden = []
    for i, w in enumerate(KETEN):
        p = list(ways[w])
        if pts:
            if hv(p[0], pts[-1]) > hv(p[-1], pts[-1]):
                p.reverse()
                print(f"  way {w} omgekeerd")
            naden.append(hv(p[0], pts[-1]))
        else:
            # eerste way: eind moet het dichtst bij de volgende way liggen
            nxt = ways[KETEN[1]]
            d_eind = min(hv(p[-1], nxt[0]), hv(p[-1], nxt[-1]))
            d_start = min(hv(p[0], nxt[0]), hv(p[0], nxt[-1]))
            if d_start < d_eind:
                p.reverse()
                print(f"  way {w} omgekeerd")
        print(f"  way {w}: {sum(hv(p[k], p[k+1]) for k in range(len(p)-1)):.1f} km, {len(p)} nodes, tags {tags[w]}")
        pts += p
    km = sum(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    grootste = max(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature", "properties": {"name": "Goldfields Gas Pipeline DN350-400 (OSM, 8 ways) Yarraloola - Kalgoorlie"},
        "geometry": {"type": "LineString", "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(fc, f)
    print(f"{len(pts)} punten, {km:.1f} km, grootste segment {grootste:.1f} km, grootste naad {max(naden)*1000:.0f} m; "
          f"begin {pts[0][1]:.4f},{pts[0][0]:.4f}; eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n-> {UIT}")


if __name__ == "__main__":
    main()
