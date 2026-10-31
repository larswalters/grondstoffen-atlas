#!/usr/bin/env python3
"""maak_leidingbeen_gas_draupner_dunkerque.py - leidingbeen b1 van gas-draupner-dunkerque.

Haalt de 2 OSM-ways van Franpipe (man_made=pipeline, substance gas, 42 inch, operator Gassco)
via de OSM-API (ODbL): 174152585 (Draupner E -> grens, ~800 km) en 903860200 (~33 km tot het
strand bij Duinkerke), stikt ze in reisvolgorde tot een LineString en schrijft een
FeatureCollection naar v2/build-cache/ais/graaf/gas-draupner-dunkerque-leiding-franpipe.geojson
(--been-geojson "leiding|...|<pad>" in bak_stromen.sh).

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_draupner_dunkerque.py
"""
import json
import math
import os
import urllib.request
import xml.etree.ElementTree as ET

WAYS = [174152585, 903860200]   # reisvolgorde: Draupner E (noord) -> Duinkerke
WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "gas-draupner-dunkerque-leiding-franpipe.geojson")


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
    assert tags.get("man_made") == "pipeline", (way, tags)
    print(way, {k: tags.get(k) for k in ("name", "operator", "substance", "diameter", "location")})
    return [nodes[n.get("ref")] for n in root.find("way").findall("nd")]


def main():
    stukken = [haal(w) for w in WAYS]
    a, b = stukken
    d_eind = min(hv(a[-1], b[0]), hv(a[-1], b[-1]))
    d_begin = min(hv(a[0], b[0]), hv(a[0], b[-1]))
    if d_begin < d_eind:
        a = a[::-1]
    if hv(a[-1], b[0]) > hv(a[-1], b[-1]):
        b = b[::-1]
    print(f"naad {hv(a[-1], b[0]) * 1000:.0f} m")
    pts = a + (b[1:] if b[0] == a[-1] else b)
    km = sum(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"name": "Franpipe 42 inch Draupner E -> Duinkerke (OSM, 2 ways)"},
        "geometry": {"type": "LineString",
                     "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(fc, f)
    print(f"{len(pts)} punten, {km:.1f} km; begin lat,lon {pts[0][1]:.4f},{pts[0][0]:.4f}; "
          f"eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n-> {UIT}")


if __name__ == "__main__":
    main()
