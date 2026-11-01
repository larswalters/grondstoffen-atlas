#!/usr/bin/env python3
"""maak_leidingbeen_gas_urucu_manaus.py - leidingbeen van gas-urucu-manaus.

Gasoduto Urucu-Coari-Manaus (Petrobras / TUM, 663 km): 15 OSM-ways (man_made=pipeline,
name "Urucu - Manaus Pipeline (Section 1/2/3)" + 3 naamloze stukken met operator Petrobras Transporte SA,
substance=gas) via de OSM-API, gestikt tot een LineString in reisvolgorde Urucu UPGN -> Maua (Manaus).
De zijtakken (Coari Branch, Anama Branch) en de spurs bij Manaus (o.a. 627636056, 257502104, 272093923,
627636053, 627636055, 256765517) horen NIET bij de hoofdlijn en worden niet meegenomen.

Elke way wordt georienteerd op gedeelde node-id; ontbreekt een gedeelde node (naad), dan wint de
dichtstbijzijnde uiteinde-combinatie en wordt de naad gerapporteerd (geen rechte brug getekend: de
LineString loopt gewoon door, de naad zit in de rapportage).

Uitvoer (FeatureCollection) in v2/build-cache/ais/graaf/:
  gas-urucu-manaus-leiding-ucm.geojson

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_urucu_manaus.py [--schrijf]
"""
import argparse
import json
import math
import os
import time
import urllib.request

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf")
# reisvolgorde Urucu -> Maua (de orientatie per way volgt uit de gedeelde nodes)
WAYS = [627453140, 211623377, 310573689, 310573683, 272083194, 321589257, 321589244, 180296516,
        272968886, 310573679, 310573687, 188456610, 627636050, 627636048, 627636049]
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
    for poging in range(4):
        try:
            d = json.load(urllib.request.urlopen(req, timeout=90))
            break
        except Exception:
            if poging == 3:
                raise
            time.sleep(3)
    nodes = {e["id"]: (e["lon"], e["lat"]) for e in d["elements"] if e["type"] == "node"}
    w = [e for e in d["elements"] if e["type"] == "way"][0]
    return w["nodes"], [nodes[i] for i in w["nodes"]], w.get("tags", {})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    a = ap.parse_args()
    pts, eind_node, naden = [], None, []
    for w in WAYS:
        ids, p, tags = haal(w)
        if pts:
            if ids[0] == eind_node:
                pass
            elif ids[-1] == eind_node:
                ids, p = ids[::-1], p[::-1]
            else:  # naad: kies de uiteinde-combinatie die het dichtst bij het huidige eind ligt
                if km(pts[-1], p[-1]) < km(pts[-1], p[0]):
                    ids, p = ids[::-1], p[::-1]
                naden.append((w, round(km(pts[-1], p[0]), 3)))
            if ids[0] == eind_node:
                p = p[1:]
        elif tags.get("name", "").endswith("(Section 1)") is False:
            print("WAARSCHUWING: eerste way is geen Section 1")
        print(f"  way {w}: {len(p)} punten, {lengte(p):.1f} km, {tags.get('name')}, {tags.get('substance')}, {tags.get('location')}")
        pts += p
        eind_node = ids[-1]
    print(f"gestikt: {len(pts)} punten, {lengte(pts):.1f} km; naden (way, km): {naden}")
    print(f"begin {pts[0][1]:.4f},{pts[0][0]:.4f}  einde {pts[-1][1]:.4f},{pts[-1][0]:.4f}")
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"name": "Gasoduto Urucu-Coari-Manaus (Urucu - Manaus Pipeline)", "ways": WAYS},
        "geometry": {"type": "LineString", "coordinates": [[round(x, 7), round(y, 7)] for x, y in pts]}}]}
    if a.schrijf:
        pad = os.path.join(UIT, "gas-urucu-manaus-leiding-ucm.geojson")
        with open(pad, "w", encoding="utf-8") as f:
            json.dump(fc, f)
        print("geschreven:", pad)


if __name__ == "__main__":
    main()
