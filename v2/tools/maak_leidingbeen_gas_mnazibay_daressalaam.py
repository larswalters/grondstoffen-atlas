#!/usr/bin/env python3
"""maak_leidingbeen_gas_mnazibay_daressalaam.py - leidingbenen van gas-mnazibay-daressalaam.

Haalt twee OSM-ways (man_made=pipeline, substance=gas, ondergronds) via de OSM-API (ODbL):
  b1  way 678587791  Manzi - Madimba pipeline          (Mnazi Bay-verwerking -> Madimba, ~11,3 km)
  b2  way 848568587  TPDC-gasleiding Mtwara-Dar (900 mm) (Madimba -> Kinyerezi, ~478,7 km;
                    OSM tekent hem van Dar naar Madimba, dus hier OMGEKEERD naar de stroomrichting)
en schrijft per been een FeatureCollection met een LineString naar v2/build-cache/ais/graaf/
(--been-geojson "leiding|...|<pad>" in bak_stromen.sh). Bestandsnamen zonder spatie (het
stroom-id heeft er een, de slug niet): gas-mnazibay-daressalaam-leiding-<been>.geojson.

Niet getekend: de Songo Songo-tak (24 inch, voegt bij Somanga in); die draagt ander gas.

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_mnazibay_daressalaam.py
"""
import json
import math
import os
import urllib.request
import xml.etree.ElementTree as ET

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
MAP = os.path.join(WORTEL, "build-cache", "ais", "graaf")
BENEN = [
    # (way, bestandsdeel, naam, omkeren)
    (678587791, "manzi-madimba", "Manzi - Madimba-gasleiding (OSM way 678587791)", False),
    (848568587, "madimba-kinyerezi",
     "TPDC-gasleiding Madimba - Kinyerezi, 36 inch (OSM way 848568587)", True),
]


def hv(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))


def haal(way):
    url = f"https://api.openstreetmap.org/api/0.6/way/{way}/full"
    req = urllib.request.Request(url, headers={"User-Agent": "grondstoffen-atlas/1.0"})
    root = ET.fromstring(urllib.request.urlopen(req, timeout=90).read())
    nodes = {n.get("id"): (float(n.get("lon")), float(n.get("lat"))) for n in root.findall("node")}
    return [nodes[n.get("ref")] for n in root.find("way").findall("nd")]


def main():
    os.makedirs(MAP, exist_ok=True)
    vorig = None
    for way, deel, naam, omkeren in BENEN:
        pts = haal(way)
        if omkeren:
            pts = pts[::-1]
        km = sum(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
        grootste = max(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
        fc = {"type": "FeatureCollection", "features": [{
            "type": "Feature", "properties": {"name": naam},
            "geometry": {"type": "LineString",
                         "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
        uit = os.path.join(MAP, f"gas-mnazibay-daressalaam-leiding-{deel}.geojson")
        with open(uit, "w", encoding="utf-8") as f:
            json.dump(fc, f)
        naad = f", naad met vorig been {hv(vorig, pts[0]):.3f} km" if vorig else ""
        print(f"{deel}: {len(pts)} punten, {km:.1f} km, grootste segment {grootste:.1f} km; "
              f"begin {pts[0][1]:.4f},{pts[0][0]:.4f}; eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}{naad}\n  -> {uit}")
        vorig = pts[-1]


if __name__ == "__main__":
    main()
