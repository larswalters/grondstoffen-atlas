#!/usr/bin/env python3
"""maak_leidingbeen_gas_westnatuna_sakra.py - leidingbeen van gas-westnatuna-sakra (WNTS).

Haalt OSM way 182146492 (man_made=pipeline, substance=gas, name=West Natuna Transportation System
(WNTS), submarine=yes; ODbL) via de OSM-API en schrijft een FeatureCollection met een LineString naar
v2/build-cache/ais/graaf/gas-westnatuna-sakra-leiding.geojson (volgorde: West Natuna -> Pulau Sakra).

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_westnatuna_sakra.py
"""
import json
import math
import os
import urllib.request
import xml.etree.ElementTree as ET

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf")
WAY = 182146492
NAAM = "West Natuna Transportation System (WNTS), West Natuna -> Pulau Sakra (OSM way 182146492)"


def hv(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))


def main():
    url = f"https://api.openstreetmap.org/api/0.6/way/{WAY}/full"
    req = urllib.request.Request(url, headers={"User-Agent": "grondstoffen-atlas/1.0"})
    root = ET.fromstring(urllib.request.urlopen(req, timeout=90).read())
    nodes = {n.get("id"): (float(n.get("lon")), float(n.get("lat"))) for n in root.findall("node")}
    pts = [nodes[n.get("ref")] for n in root.find("way").findall("nd")]
    # richting: West Natuna (hoge lat, hoge lon) eerst
    if pts[0][1] < pts[-1][1]:
        pts = pts[::-1]
    km = sum(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature", "properties": {"name": NAAM},
        "geometry": {"type": "LineString",
                     "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    os.makedirs(UIT, exist_ok=True)
    pad = os.path.join(UIT, "gas-westnatuna-sakra-leiding.geojson")
    with open(pad, "w", encoding="utf-8") as f:
        json.dump(fc, f)
    print(f"{len(pts)} punten, {km:.1f} km; begin lat,lon {pts[0][1]:.4f},{pts[0][0]:.4f}; "
          f"eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n  -> {pad}")


if __name__ == "__main__":
    main()
