#!/usr/bin/env python3
"""maak_leidingbeen_gas_saihrawl_qalhat.py - leidingbeen van gas-saihrawl-qalhat.

Haalt OSM-way 589407065 (PDO-gasleiding Saih Rawl -> Qalhat/Oman LNG, man_made=pipeline,
substance=gas, usage=transmission, ondergronds, 345 vertices, ~351,7 km) via de OSM-API (ODbL)
en schrijft een FeatureCollection met een LineString naar
v2/build-cache/ais/graaf/gas-saihrawl-qalhat-leiding-omangas.geojson
(--been-geojson "leiding|...|<pad>" in bak_stromen.sh).

Niet verwarren met way 565166565 (Saih Rawl -> Sohar): dat is een andere leiding.

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_saihrawl_qalhat.py
"""
import json
import math
import os
import urllib.request
import xml.etree.ElementTree as ET

WAY = 589407065
WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf",
                   "gas-saihrawl-qalhat-leiding-omangas.geojson")


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
    km = sum(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    grootste = max(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"name": "PDO-gasleiding Saih Rawl - Qalhat (OSM way 589407065)"},
        "geometry": {"type": "LineString",
                     "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(fc, f)
    print(f"{len(pts)} punten, {km:.1f} km, grootste segment {grootste:.1f} km; "
          f"begin lat,lon {pts[0][1]:.4f},{pts[0][0]:.4f}; eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n-> {UIT}")


if __name__ == "__main__":
    main()
