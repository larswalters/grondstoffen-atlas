#!/usr/bin/env python3
"""maak_leidingbeen_gas_mobley_chatham.py - leidingbeen b1 van gas-mobley-chatham.

Haalt de 6 OSM-ways van de Mountain Valley Pipeline (man_made=pipeline, substance gas, 42 inch,
operator Mountain Valley Pipeline LLC) via de OSM-API (ODbL), stikt ze in reisvolgorde (noord naar
zuid) tot een LineString en schrijft een FeatureCollection naar
v2/build-cache/ais/graaf/gas-mobley-chatham-leiding-mvp.geojson
(--been-geojson "leiding|...|<pad>" in bak_stromen.sh).

De 3 kleine stompjes (Transco-interconnect, 0,4-0,7 km) blijven weg: selectie op deze 6 way-id's.
Verwacht: 487,6 km, naden 34/14/11/14/0 m, begin 39.5628,-80.5434, eind 36.8319,-79.3428.

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_mobley_chatham.py
"""
import json
import math
import os
import urllib.request
import xml.etree.ElementTree as ET

# reisvolgorde noord -> zuid; 1235574214 is het begin op 39.5628,-80.5434
WAYS = [1235574214, 1235574206, 627895219, 897721062, 1235543996, 750297699]
WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "gas-mobley-chatham-leiding-mvp.geojson")


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
    return [nodes[n.get("ref")] for n in root.find("way").findall("nd")]


def main():
    stukken = [haal(w) for w in WAYS]
    # eerste stuk: oriënteer zodat het uiteinde dat het dichtst bij stuk 2 ligt, achteraan komt
    a, b = stukken[0], stukken[1]
    d_eind = min(hv(a[-1], b[0]), hv(a[-1], b[-1]))
    d_begin = min(hv(a[0], b[0]), hv(a[0], b[-1]))
    if d_begin < d_eind:
        stukken[0] = a[::-1]
    pts = []
    for w, p in zip(WAYS, stukken):
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
        "properties": {"name": "Mountain Valley Pipeline 42 inch (OSM, 6 ways)"},
        "geometry": {"type": "LineString",
                     "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(fc, f)
    print(f"{len(pts)} punten, {km:.1f} km; begin lat,lon {pts[0][1]:.4f},{pts[0][0]:.4f}; "
          f"eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n-> {UIT}")


if __name__ == "__main__":
    main()
