#!/usr/bin/env python3
"""maak_leidingbeen_gas_opal_malin.py - leidingbeen b2 van gas-opal-malin.

Haalt de 31 OSM-ways van de Ruby Pipeline (man_made=pipeline, name=Ruby Pipeline, substance gas,
42 inch) via de OSM-API (ODbL), stikt ze in reisvolgorde (oost naar west, Uinta County WY tot Malin OR)
tot een LineString en schrijft een FeatureCollection naar
v2/build-cache/ais/graaf/gas-opal-malin-leiding-ruby.geojson
(--been-geojson "leiding|...|<pad>" in bak_stromen.sh).

Weggelaten: de stationsstukjes (overground/indoor, < 0,1 km, compressor- en meetstations) en way
382912693 (1,1 km, geen substance, zijtak). Selectie dus op naam en lengte, niet op diameter.
Het eerste OSM-punt (41.5727,-110.9166) ligt ca. 53 km hemelsbreed van Opal: dat stuk is niet gekarteerd.

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_opal_malin.py
"""
import json
import math
import os
import urllib.request
import xml.etree.ElementTree as ET

# reisvolgorde oost -> west; 371667159 begint (oostelijk) op 41.5727,-110.9166
WAYS = [371667159, 371848659, 371848655, 371848653, 371848658, 371848657, 371848656, 371667163,
        371667165, 371667169, 371667167, 371667166, 371667170, 371667171, 371667173, 371667175,
        371667176, 371668066, 371668067, 371668068, 371668069, 371668070, 371668071, 371668072,
        371668073, 371845634, 948043134, 946203791, 946177658, 946170581, 209036621]
WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "gas-opal-malin-leiding-ruby.geojson")


def hv(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))


def haal(way):
    url = f"https://api.openstreetmap.org/api/0.6/way/{way}/full"
    req = urllib.request.Request(url, headers={"User-Agent": "grondstoffen-atlas/1.0"})
    root = ET.fromstring(urllib.request.urlopen(req, timeout=120).read())
    nodes = {n.get("id"): (float(n.get("lon")), float(n.get("lat"))) for n in root.findall("node")}
    tags = {t.get("k"): t.get("v") for t in root.find("way").findall("tag")}
    assert tags.get("name") == "Ruby Pipeline", (way, tags)
    return [nodes[n.get("ref")] for n in root.find("way").findall("nd")]


def main():
    pts = []
    for i, w in enumerate(WAYS):
        p = haal(w)
        if pts:  # oriënteer zodat het begin aansluit op het eind van het vorige stuk
            if hv(pts[-1], p[0]) > hv(pts[-1], p[-1]):
                p = p[::-1]
            print(f"way {w}: naad {hv(pts[-1], p[0]) * 1000:.0f} m, {len(p)} punten")
            if p[0] == pts[-1]:
                p = p[1:]
        else:
            # eerste way: oost-einde (41.5727,-110.9166) vooraan
            if p[0][0] < p[-1][0]:
                p = p[::-1]
            print(f"way {w}: {len(p)} punten")
        pts += p
    km = sum(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"name": "Ruby Pipeline 42 inch (OSM name=Ruby Pipeline, 31 ways)"},
        "geometry": {"type": "LineString",
                     "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(fc, f)
    print(f"{len(pts)} punten, {km:.1f} km; begin lat,lon {pts[0][1]:.4f},{pts[0][0]:.4f}; "
          f"eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n-> {UIT}")


if __name__ == "__main__":
    main()
