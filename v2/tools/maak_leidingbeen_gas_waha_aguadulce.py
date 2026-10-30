#!/usr/bin/env python3
"""maak_leidingbeen_gas_waha_aguadulce.py - leidingbeen b1 van gas-waha-aguadulce.

Haalt de 19 OSM-ways met ref=GCX (Gulf Coast Express Pipeline, man_made=pipeline, substance gas,
Kinder Morgan Texas Pipeline LLC) via de OSM-API (ODbL), stikt ze in reisvolgorde (west naar oost)
tot een LineString en schrijft een FeatureCollection naar
v2/build-cache/ais/graaf/gas-waha-aguadulce-leiding-gcx.geojson
(--been-geojson "leiding|...|<pad>" in bak_stromen.sh).

Selectie op ref=GCX, NIET op diameter: Permian Highway (PHP), Whistler (WHL) en Hill Country lopen
door hetzelfde corridor met dezelfde dikte. Kleine stompjes (12,75/16 inch en dubbele ways bij de
kleppen, < 0,3 km) blijven weg; het 42/48 inch hoofdspoor is 570,6 km zonder naad > 51 m.

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_waha_aguadulce.py
"""
import json
import math
import os
import urllib.request
import xml.etree.ElementTree as ET

# reisvolgorde west -> oost; 1104116970 is het 0,0 km-begin op 31.0794,-101.5847
WAYS = [1104116970, 1104120534, 1104120532, 1098316526, 1098316368, 1098316366, 1098316364,
        1098316360, 1098271341, 1098271340, 1066747742, 1080984111, 1080984060, 1065312957,
        1059834555, 1059840794, 1059833143, 1059839951, 1070599581]
WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "gas-waha-aguadulce-leiding-gcx.geojson")


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
    assert tags.get("ref") == "GCX", (way, tags)
    return [nodes[n.get("ref")] for n in root.find("way").findall("nd")]


def main():
    pts = []
    for w in WAYS:
        p = haal(w)
        if pts:  # oriënteer zodat het begin aansluit op het eind van het vorige stuk
            if hv(pts[-1], p[0]) > hv(pts[-1], p[-1]):
                p = p[::-1]
            print(f"way {w}: naad {hv(pts[-1], p[0]) * 1000:.0f} m, {len(p)} punten")
            if p[0] == pts[-1]:
                p = p[1:]
        else:
            print(f"way {w}: {len(p)} punten")
        pts += p
    km = sum(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"name": "Gulf Coast Express Pipeline 42/48 inch (OSM ref=GCX, 19 ways)"},
        "geometry": {"type": "LineString",
                     "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(fc, f)
    print(f"{len(pts)} punten, {km:.1f} km; begin lat,lon {pts[0][1]:.4f},{pts[0][0]:.4f}; "
          f"eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n-> {UIT}")


if __name__ == "__main__":
    main()
