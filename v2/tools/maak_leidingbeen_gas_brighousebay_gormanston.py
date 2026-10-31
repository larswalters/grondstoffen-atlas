#!/usr/bin/env python3
"""maak_leidingbeen_gas_brighousebay_gormanston.py - leidingbeen van gas-brighousebay-gormanston.

UK-Ireland Interconnector 2 (IC2, 30 inch, Gas Networks Ireland): vijf OSM-ways
(man_made=pipeline, name=UK-Ireland Interconnector 2 (IC2), substance=gas) via de OSM-API,
gestikt tot een LineString in reisvolgorde Brighouse Bay -> Gormanston (OSM-volgorde omgedraaid).

Uitvoer (FeatureCollection) in v2/build-cache/ais/graaf/:
  gas-brighousebay-gormanston-leiding-ic2.geojson

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_brighousebay_gormanston.py [--schrijf]
"""
import argparse
import json
import math
import os
import urllib.request

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf")
# volgorde Gormanston -> Brighouse Bay (OSM-richting); wordt daarna omgedraaid
WAYS = [174267017, 902882374, 902882373, 440424760, 440429967]
R = 6371.0088


def km(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def lengte(p):
    return sum(km(p[i], p[i + 1]) for i in range(len(p) - 1))


def haal(way):
    url = f"https://api.openstreetmap.org/api/0.6/way/{way}/full.json"
    req = urllib.request.Request(url, headers={"User-Agent": "grondstoffen-atlas/1.0"})
    d = json.load(urllib.request.urlopen(req, timeout=90))
    nodes = {e["id"]: (e["lon"], e["lat"]) for e in d["elements"] if e["type"] == "node"}
    w = [e for e in d["elements"] if e["type"] == "way"][0]
    return [nodes[i] for i in w["nodes"]], w.get("tags", {})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    a = ap.parse_args()
    pts, naden = [], []
    for w in WAYS:
        p, tags = haal(w)
        print(f"  way {w}: {len(p)} punten, {lengte(p):.1f} km, {tags.get('name')}, {tags.get('substance')}")
        if pts:
            naden.append(km(pts[-1], p[0]))
            if km(pts[-1], p[0]) < 1e-6:
                p = p[1:]
        pts += p
    pts = pts[::-1]  # Brighouse Bay -> Gormanston
    print(f"gestikt: {len(pts)} punten, {lengte(pts):.1f} km; naden (km): {[round(x, 4) for x in naden]}")
    print(f"begin {pts[0][1]:.4f},{pts[0][0]:.4f}  einde {pts[-1][1]:.4f},{pts[-1][0]:.4f}")
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"name": "UK-Ireland Interconnector 2 (IC2)", "ways": WAYS},
        "geometry": {"type": "LineString", "coordinates": [[round(x, 7), round(y, 7)] for x, y in pts]}}]}
    if a.schrijf:
        pad = os.path.join(UIT, "gas-brighousebay-gormanston-leiding-ic2.geojson")
        with open(pad, "w", encoding="utf-8") as f:
            json.dump(fc, f)
        print("geschreven:", pad)


if __name__ == "__main__":
    main()
