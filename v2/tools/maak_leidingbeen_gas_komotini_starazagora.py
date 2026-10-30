#!/usr/bin/env python3
"""maak_leidingbeen_gas_komotini_starazagora.py - leidingbeen van gas-komotini-starazagora (IGB/ICGB).

Haalt drie OSM-ways (man_made=pipeline, substance=gas; ODbL) via de OSM-API, stikt ze in vaste
volgorde (elke way zo gedraaid dat zijn begin het dichtst bij het vorige eind ligt) en schrijft een
FeatureCollection met een LineString naar v2/build-cache/ais/graaf/:
  gas-komotini-starazagora-leiding-igb.geojson
    919860052 (omgedraaid, ~31 km) -> 1076969894 (omgedraaid, ~50 km) -> 826478838 (name=ICGB, ~101 km)

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_komotini_starazagora.py
"""
import json
import math
import os
import urllib.request
import xml.etree.ElementTree as ET

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf")

NAAM = "IGB/ICGB DN800 Komotini -> Stara Zagora (OSM-ways, ICGB)"
WAYS = [919860052, 1076969894, 826478838]
# de eerste twee ways lopen in OSM noord->zuid of andersom; we dwingen de reisrichting af via het anker
BEGIN = (25.4864, 41.0621)  # (lon, lat) leiding-kop Komotini


def hv(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))


def lengte(p):
    return sum(hv(p[i], p[i + 1]) for i in range(len(p) - 1))


def haal(way):
    url = f"https://api.openstreetmap.org/api/0.6/way/{way}/full"
    req = urllib.request.Request(url, headers={"User-Agent": "grondstoffen-atlas/1.0"})
    root = ET.fromstring(urllib.request.urlopen(req, timeout=90).read())
    nodes = {n.get("id"): (float(n.get("lon")), float(n.get("lat"))) for n in root.findall("node")}
    return [nodes[n.get("ref")] for n in root.find("way").findall("nd")]


def main():
    os.makedirs(UIT, exist_ok=True)
    pts, naden = [], []
    for i, w in enumerate(WAYS):
        p = haal(w)
        if i == 0:
            if hv(BEGIN, p[0]) > hv(BEGIN, p[-1]):
                p = p[::-1]
        elif hv(pts[-1], p[0]) > hv(pts[-1], p[-1]):
            p = p[::-1]
        if pts:
            naden.append(round(hv(pts[-1], p[0]) * 1000))
        print(f"way {w}: {len(p)} punten, {lengte(p):.1f} km")
        pts.extend(p)
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature", "properties": {"name": NAAM},
        "geometry": {"type": "LineString",
                     "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    pad = os.path.join(UIT, "gas-komotini-starazagora-leiding-igb.geojson")
    with open(pad, "w", encoding="utf-8") as f:
        json.dump(fc, f)
    print(f"igb: {len(pts)} punten, {lengte(pts):.1f} km, naden (m) {naden}; "
          f"begin lat,lon {pts[0][1]:.4f},{pts[0][0]:.4f}; eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n  -> {pad}")


if __name__ == "__main__":
    main()
