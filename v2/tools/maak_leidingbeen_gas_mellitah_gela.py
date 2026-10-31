#!/usr/bin/env python3
"""maak_leidingbeen_gas_mellitah_gela.py - Greenstream (Mellitah -> Gela) uit OSM-ways.

Ways 310845241 (onderzee, Agip Gas BV, ~501 km) + 310833747 (onshore Gela, Eni, ~1,2 km), gestikt.
Way 310835025 is Snam Gela-Enna (geen Greenstream) en wordt weggelaten.
Schrijft een FeatureCollection naar v2/build-cache/ais/graaf/gas-mellitah-gela-leiding-greenstream.geojson
Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_mellitah_gela.py
"""
import json, math, os, urllib.request
import xml.etree.ElementTree as ET

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf")
WAYS = [310845241, 310833747]


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


pts, naden = [], []
for w in WAYS:
    p = haal(w)
    if pts and hv(pts[-1], p[0]) > hv(pts[-1], p[-1]):
        p = p[::-1]
    if pts:
        naden.append(round(hv(pts[-1], p[0]), 3))
        if naden[-1] < 0.001:
            p = p[1:]
    pts.extend(p)
km = sum(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
fc = {"type": "FeatureCollection", "features": [{
    "type": "Feature", "properties": {"name": "Greenstream Mellitah -> Gela (OSM ways 310845241 + 310833747)"},
    "geometry": {"type": "LineString", "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
pad = os.path.join(UIT, "gas-mellitah-gela-leiding-greenstream.geojson")
with open(pad, "w", encoding="utf-8") as f:
    json.dump(fc, f)
print(f"{len(pts)} punten, {km:.1f} km, naden {naden}; begin lat,lon {pts[0][1]:.4f},{pts[0][0]:.4f}; eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n  -> {pad}")
