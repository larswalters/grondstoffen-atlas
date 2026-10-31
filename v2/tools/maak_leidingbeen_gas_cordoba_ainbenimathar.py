#!/usr/bin/env python3
"""maak_leidingbeen_gas_cordoba_ainbenimathar.py - GME-keten Cordoba -> Ain Beni Mathar uit OSM-ways.

Twaalf OSM-ways in volgorde (Spanje Al-Andalus, Straat van Gibraltar, Marokko Pedro Duran Farell):
  305990340, 777461438, 331405426, 331373354, 266007641, 331370590, 266354518, 264885392 (Spanje),
  265033883 (Straat, underwater), 265033635, 578918617, 229290151 (Marokko; laatste way geknipt op het
  vertex dichtst bij lat 34.0471, lon -2.1158).
Elke way wordt zo gedraaid dat zijn begin het dichtst bij het huidige eind ligt; naden worden gerapporteerd.
Schrijft een FeatureCollection naar v2/build-cache/ais/graaf/gas-cordoba-ainbenimathar-leiding-gme.geojson
Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_cordoba_ainbenimathar.py
"""
import json, math, os, time, urllib.request
import xml.etree.ElementTree as ET

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf")
WAYS = [305990340, 777461438, 331405426, 331373354, 266007641, 331370590, 266354518, 264885392,
        265033883, 265033635, 578918617, 229290151]
KNIP = (-2.1158, 34.0471)  # (lon, lat) laatste vertex van de laatste way


def hv(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))


def haal(way):
    url = f"https://api.openstreetmap.org/api/0.6/way/{way}/full"
    for poging in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "grondstoffen-atlas/1.0"})
            root = ET.fromstring(urllib.request.urlopen(req, timeout=90).read())
            break
        except Exception as e:
            print("  retry", way, e)
            time.sleep(3)
    else:
        raise SystemExit(f"way {way} niet op te halen")
    nodes = {n.get("id"): (float(n.get("lon")), float(n.get("lat"))) for n in root.findall("node")}
    tags = {t.get("k"): t.get("v") for t in root.find("way").findall("tag")}
    return [nodes[n.get("ref")] for n in root.find("way").findall("nd")], tags


def lengte(p):
    return sum(hv(p[i], p[i + 1]) for i in range(len(p) - 1))


pts, naden, log = [], [], []
for i, w in enumerate(WAYS):
    p, tags = haal(w)
    if i == 0:
        # begin bij de Cordoba-kant: het uiteinde dat het verst van de volgende way ligt
        p2, _ = haal(WAYS[1])
        d_begin = min(hv(p[0], p2[0]), hv(p[0], p2[-1]))
        d_eind = min(hv(p[-1], p2[0]), hv(p[-1], p2[-1]))
        if d_begin < d_eind:
            p = p[::-1]
    else:
        if hv(pts[-1], p[0]) > hv(pts[-1], p[-1]):
            p = p[::-1]
    if w == WAYS[-1]:
        k = min(range(len(p)), key=lambda j: hv(p[j], KNIP))
        log.append(f"  knip way {w} bij vertex {k} ({p[k][1]:.4f},{p[k][0]:.4f}), {hv(p[k], KNIP) * 1000:.0f} m van doel")
        p = p[:k + 1]
    if pts:
        naden.append(round(hv(pts[-1], p[0]) * 1000))
        if naden[-1] < 1:
            p = p[1:]
    log.append(f"  way {w}: {len(p)} punten, {lengte(p):.1f} km, name={tags.get('name')}, operator={tags.get('operator')}, "
               f"location={tags.get('location')}, substance={tags.get('substance')}")
    pts.extend(p)
km = lengte(pts)
fc = {"type": "FeatureCollection", "features": [{
    "type": "Feature", "properties": {"name": "GME Cordoba -> Ain Beni Mathar (OSM-ways, zie maak_leidingbeen_gas_cordoba_ainbenimathar.py)"},
    "geometry": {"type": "LineString", "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
pad = os.path.join(UIT, "gas-cordoba-ainbenimathar-leiding-gme.geojson")
with open(pad, "w", encoding="utf-8") as f:
    json.dump(fc, f)
print("\n".join(log))
print(f"{len(pts)} punten, {km:.1f} km, naden (m) {naden}; begin lat,lon {pts[0][1]:.4f},{pts[0][0]:.4f}; "
      f"eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n  -> {pad}")
