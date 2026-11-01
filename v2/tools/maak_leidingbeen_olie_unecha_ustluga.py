#!/usr/bin/env python3
"""maak_leidingbeen_olie_unecha_ustluga.py — het leidingbeen a1 van olie-unecha-ustluga.

De routebrief (v2/design/routebrieven/olie-unecha-ustluga.md) legt Baltic Pipeline System-2 (Transneft)
Unecha NPS-1 (Bryansk) -> Smolensk -> Andreapol -> Ust-Luga vast als 12 OSM-ways (man_made=pipeline,
substance=oil). pyosmium is geblokkeerd; de geometrie komt per way-id uit de OSM-API (ODbL) met cache op
schijf. Stikken op GEDEELDE OSM-NODES; twee naden zijn open (0,016 en 0,604 km) en worden gestikt
(rechte verbinding), niet gestippeld.

Uitvoer (FeatureCollection): v2/build-cache/ais/graaf/olie-unecha-ustluga-leiding-a1.geojson
Draaien:   python v2/tools/maak_leidingbeen_olie_unecha_ustluga.py --schrijf
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import urllib.request

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
PREFIX = "olie-unecha-ustluga"
CACHE = os.path.join(BEEN, PREFIX + "-osmapi-cache.json")
UA = "grondstoffen-atlas/1.0 (route research; OSM API, ODbL)"
WAYS = [173115751, 282239195, 333885244, 333885251, 318819120, 819499320, 500430998,
        508649116, 508204510, 824058814, 500430997, 333903684]
R = 6371.0088


def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def lengte(p):
    return sum(hav(p[i], p[i + 1]) for i in range(len(p) - 1))


def _get(url):
    err = None
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return json.load(urllib.request.urlopen(req, timeout=90))
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(3 * (i + 1))
    raise err


def laad(ids):
    c = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {"ways": {}, "nodes": {}}
    nodig = [i for i in ids if str(i) not in c["ways"]]
    if nodig:
        d = _get("https://api.openstreetmap.org/api/0.6/ways.json?ways=" + ",".join(map(str, nodig)))
        for e in d["elements"]:
            c["ways"][str(e["id"])] = {"nodes": e["nodes"], "tags": e.get("tags", {})}
    nn = sorted({n for i in ids for n in c["ways"][str(i)]["nodes"] if str(n) not in c["nodes"]})
    for k in range(0, len(nn), 700):
        d = _get("https://api.openstreetmap.org/api/0.6/nodes.json?nodes=" + ",".join(map(str, nn[k:k + 700])))
        for e in d["elements"]:
            c["nodes"][str(e["id"])] = [e["lat"], e["lon"]]
    os.makedirs(BEEN, exist_ok=True)
    json.dump(c, open(CACHE, "w", encoding="utf-8"))
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()
    c = laad(WAYS)
    pt = lambda n: tuple(c["nodes"][str(n)])  # noqa: E731
    keten = list(c["ways"][str(WAYS[0])]["nodes"])
    naden = []
    for i in WAYS[1:]:
        nd = list(c["ways"][str(i)]["nodes"])
        eind = keten[-1]
        if nd[0] == eind:
            naden.append((i, 0.0)); keten += nd[1:]
        elif nd[-1] == eind:
            naden.append((i, 0.0)); keten += nd[::-1][1:]
        else:
            # open naad: kies de oriëntatie met de kortste verbinding
            d0 = hav(pt(eind), pt(nd[0])); d1 = hav(pt(eind), pt(nd[-1]))
            if d1 < d0:
                nd = nd[::-1]; d0 = d1
            naden.append((i, d0)); keten += nd
    pts = [pt(n) for n in keten]
    print(f"{len(WAYS)} ways, {len(pts)} punten, {lengte(pts):.2f} km")
    for i, d in naden:
        if d > 0:
            print(f"open naad vóór way {i}: {d:.3f} km")
    print(f"van {pts[0][0]:.5f},{pts[0][1]:.5f} naar {pts[-1][0]:.5f},{pts[-1][1]:.5f}")
    if args.schrijf:
        coords = [[round(p[1], 5), round(p[0], 5)] for p in pts]
        sch = [coords[0]]
        for q in coords[1:]:
            if q != sch[-1]:
                sch.append(q)
        km = lengte([(q[1], q[0]) for q in sch])
        doc = {"type": "FeatureCollection", "features": [{
            "type": "Feature",
            "properties": {"naam": "Baltic Pipeline System-2 Unecha → Ust-Luga (OSM-som)", "km": round(km, 2),
                           "punten": len(sch),
                           "bron": "OpenStreetMap-bijdragers (ODbL), OSM-API way-geometrie, man_made=pipeline substance=oil",
                           "gereedschap": "maak_leidingbeen_olie_unecha_ustluga.py"},
            "geometry": {"type": "LineString", "coordinates": sch}}]}
        uit = os.path.join(BEEN, PREFIX + "-leiding-a1.geojson")
        json.dump(doc, open(uit, "w", encoding="utf-8"), ensure_ascii=False)
        print(f"geschreven {uit} ({km:.2f} km, {len(sch)} punten, {os.path.getsize(uit)/1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
