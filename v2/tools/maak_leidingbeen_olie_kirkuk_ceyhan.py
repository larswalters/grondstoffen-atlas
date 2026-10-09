#!/usr/bin/env python3
"""maak_leidingbeen_olie_kirkuk_ceyhan.py - b1 van olie-kirkuk-ceyhan.

Brief: v2/design/routebrieven/olie-kirkuk-ceyhan.md (b1). Het Turkse deel van de
Iraq-Turkey Crude Oil Pipeline (Kirkuk-Ceyhan, ITP), van Fishkhabur (Irak-Turkije-grens)
tot het westelijke OSM-eind bij lon 36.15: OSM-ways met man_made=pipeline, substance=oil
uit het lokale Geofabrik-extract `turkije`. De BTC-leiding (operator BTC Co of naam
met Bak/Tiflis/Ceyhan) loopt parallel en wordt UITGESLOTEN. Stitchen op exacte
coordinaatgelijkheid (BOTAS-ways sluiten op 0 m aan), daarna het kortste pad van de
knoop die het dichtst bij het Fishkhabur-anker ligt naar het westelijke eind.

Uitvoer: v2/build-cache/ais/graaf/olie-kirkuk-ceyhan-leiding-itp.geojson (FeatureCollection,
een LineString, [lon,lat]).

Draaien:  python v2/tools/maak_leidingbeen_olie_kirkuk_ceyhan.py --schrijf
"""
from __future__ import annotations

import argparse
import collections
import heapq
import json
import math
import os
import sys

import osmium

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
PBF = os.path.join(WORTEL, "build-cache", "geofabrik", "turkije-latest.osm.pbf")
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "olie-kirkuk-ceyhan-leiding-itp.geojson")

FISHKHABUR = (42.4221, 37.1335)          # (lon, lat) - anker kop
BBOX = (35.5, 36.5, 42.8, 38.0)          # lon0 lat0 lon1 lat1
R = 6371.0088


def km(a, b):
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def scan():
    ways = []
    for obj in (osmium.FileProcessor(PBF).with_locations()
                .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
                .with_filter(osmium.filter.KeyFilter("man_made"))):
        t = obj.tags
        if t.get("man_made") != "pipeline" or t.get("substance") != "oil":
            continue
        naam = t.get("name") or ""
        if t.get("operator") == "BTC Co" or ("Bak" in naam and "Tiflis" in naam):
            continue
        pts = [(n.location.lon, n.location.lat) for n in obj.nodes if n.location.valid()]
        if len(pts) < 2:
            continue
        if not any(BBOX[0] <= x <= BBOX[2] and BBOX[1] <= y <= BBOX[3] for x, y in pts):
            continue
        ways.append((obj.id, pts))
    return ways


def sleutel(p):
    return (round(p[0], 7), round(p[1], 7))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()

    ways = scan()
    print(f"oil-pipeline-ways (zonder BTC) in venster: {len(ways)}")
    adj = collections.defaultdict(list)
    pos = {}
    for _, p in ways:
        for i in range(len(p) - 1):
            a, b = sleutel(p[i]), sleutel(p[i + 1])
            pos[a], pos[b] = p[i], p[i + 1]
            d = km(p[i], p[i + 1])
            adj[a].append((b, d))
            adj[b].append((a, d))

    # component dat het dichtst bij Fishkhabur ligt
    start = min(pos, key=lambda k: km(pos[k], FISHKHABUR))
    print(f"start-knoop {pos[start][1]:.5f},{pos[start][0]:.5f} op {km(pos[start], FISHKHABUR):.3f} km van het anker")
    comp = {start}
    stapel = [start]
    while stapel:
        u = stapel.pop()
        for v, _ in adj[u]:
            if v not in comp:
                comp.add(v)
                stapel.append(v)
    west = min(comp, key=lambda k: pos[k][0])
    print(f"component {len(comp)} knopen; westelijk eind {pos[west][1]:.5f},{pos[west][0]:.5f}")

    dist = {start: 0.0}
    vorig = {}
    heap = [(0.0, start)]
    klaar = set()
    while heap:
        d, u = heapq.heappop(heap)
        if u in klaar:
            continue
        klaar.add(u)
        if u == west:
            break
        for v, w in adj[u]:
            nd = d + w
            if nd < dist.get(v, 1e18):
                dist[v] = nd
                vorig[v] = u
                heapq.heappush(heap, (nd, v))
    pad = [west]
    while pad[-1] != start:
        pad.append(vorig[pad[-1]])
    pad.reverse()
    print(f"pad: {len(pad)} punten, {dist[west]:.1f} km")

    if args.schrijf:
        coords = [[round(pos[k][0], 5), round(pos[k][1], 5)] for k in pad]
        doc = {"type": "FeatureCollection", "features": [{
            "type": "Feature",
            "properties": {
                "naam": "Iraq-Turkey Crude Oil Pipeline (Kirkuk-Ceyhan), Turks deel Fishkhabur - lon 36.15",
                "km": round(dist[west], 2),
                "punten": len(pad),
                "bron": "OpenStreetMap-bijdragers (ODbL), extract turkije, man_made=pipeline substance=oil, BTC uitgesloten",
                "gereedschap": "maak_leidingbeen_olie_kirkuk_ceyhan.py",
            },
            "geometry": {"type": "LineString", "coordinates": coords},
        }]}
        os.makedirs(os.path.dirname(UIT), exist_ok=True)
        with open(UIT, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False)
        print(f"geschreven: {UIT} ({os.path.getsize(UIT)/1024:.1f} KB)  kop {coords[0][1]},{coords[0][0]}  staart {coords[-1][1]},{coords[-1][0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
