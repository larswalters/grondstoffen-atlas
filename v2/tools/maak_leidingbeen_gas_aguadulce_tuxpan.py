#!/usr/bin/env python3
"""maak_leidingbeen_gas_aguadulce_tuxpan.py - leidingbeen b2 van gas-aguadulce-tuxpan.

Haalt de OSM-ways 921735480 + 1279403582 + 1279403585 (Sur de Texas-Tuxpan Gas Pipeline,
man_made=pipeline, substance gas, 42 inch) via de OSM-API (ODbL), stikt ze in die volgorde tot
een LineString (Naranjos-arm 1279403584 blijft weg) en schrijft een FeatureCollection naar
v2/build-cache/ais/graaf/gas-aguadulce-tuxpan-leiding-sdt.geojson
(--been-geojson "leiding|...|<pad>" in bak_stromen.sh).

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_aguadulce_tuxpan.py
"""
import json
import math
import os
import urllib.request
import xml.etree.ElementTree as ET

WAYS = [921735480, 1279403582, 1279403585]
WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "gas-aguadulce-tuxpan-leiding-sdt.geojson")


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
    return [nodes[n.get("ref")] for n in root.find("way").findall("nd")]


def main():
    pts = []
    for w in WAYS:
        p = haal(w)
        if pts:  # oriënteer zodat het begin aansluit op het eind van het vorige stuk
            if hv(pts[-1], p[0]) > hv(pts[-1], p[-1]):
                p = p[::-1]
            print(f"way {w}: naad {hv(pts[-1], p[0]) * 1000:.0f} m")
            if p[0] == pts[-1]:
                p = p[1:]
        print(f"way {w}: {len(p)} punten")
        pts += p
    km = sum(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"name": "Sur de Texas-Tuxpan Gas Pipeline 42 inch (OSM ways 921735480 + 1279403582 + 1279403585)"},
        "geometry": {"type": "LineString",
                     "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(fc, f)
    print(f"{len(pts)} punten, {km:.1f} km; begin lat,lon {pts[0][1]:.4f},{pts[0][0]:.4f}; "
          f"eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n-> {UIT}")


if __name__ == "__main__":
    main()
