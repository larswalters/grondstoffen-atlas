#!/usr/bin/env python3
"""maak_leidingbeen_olie_trieste_ingolstadt.py - het leidingbeen van olie-trieste-ingolstadt.

De routebrief (v2/design/routebrieven/olie-trieste-ingolstadt.md) legt de Transalpine Pipeline (TAL, 40 inch)
Triest (SIOT-tankenpark, San Dorligo della Valle) -> Würmlach -> Tirol -> Beieren -> TAL-tankenpark
Lenting/Ingolstadt vast als 19 OSM-ways (man_made=pipeline, substance=oil). Geometrie per way-id uit de
OSM-API (api.openstreetmap.org/api/0.6, ODbL), met cache op schijf. Ways worden gestikt op gedeelde nodes;
waar OSM de leiding in stukken heeft gekarteerd zonder gedeelde node (6 hiaten, samen ~0,85 km) wordt het
dichtstbijzijnde eindpunt-paar recht verbonden en de naad gerapporteerd (geen stippel: kartering-hiaat van een
ondergrondse leiding, geen net-gat).

Volgorde (bron: haalbaarheidstoets; 171571174 is een zijtak naar het oosten en wordt NIET gebruikt):
  290402363, 145229247, 1094455052, 1094455053, 432760339, 1333438686, 1333706121, 1333706120, 1333706119,
  1333706123, 1333706124, 1333706125, 158910168, 168056656, 168224409, 168224405, 155702494, 169707479, 39856317

Uitvoer (v2/build-cache/ais/graaf/):  olie-trieste-ingolstadt-leiding.geojson  (FeatureCollection, 1 LineString)
Draaien:  python v2/tools/maak_leidingbeen_olie_trieste_ingolstadt.py --schrijf
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
PREFIX = "olie-trieste-ingolstadt"
CACHE = os.path.join(BEEN, PREFIX + "-osmapi-cache.json")
UA = "grondstoffen-atlas/1.0 (route research; OSM API, ODbL)"

IDS = [290402363, 145229247, 1094455052, 1094455053, 432760339, 1333438686, 1333706121, 1333706120,
       1333706119, 1333706123, 1333706124, 1333706125, 158910168, 168056656, 168224409, 168224405,
       155702494, 169707479, 39856317]
NAAD_MAX_KM = 1.0   # een hiaat groter dan dit is een fout, geen kartering-naad
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
    c = laad(IDS)
    pts = []
    naden = []
    for k, i in enumerate(IDS):
        ns = list(c["ways"][str(i)]["nodes"])
        if k == 0:
            nxt = c["ways"][str(IDS[1])]["nodes"]
            if ns[0] in (nxt[0], nxt[-1]):
                ns.reverse()
        else:
            eind = pts[-1]
            a, b = tuple(c["nodes"][str(ns[0])]), tuple(c["nodes"][str(ns[-1])])
            if hav(eind, b) < hav(eind, a):
                ns.reverse()
        wp = [tuple(c["nodes"][str(n)]) for n in ns]
        if pts:
            g = hav(pts[-1], wp[0])
            if g > 1e-6:
                if g > NAAD_MAX_KM:
                    raise SystemExit(f"way {i}: naad {g:.3f} km > {NAAD_MAX_KM} km")
                naden.append((i, g * 1000))
            if g < 1e-6:
                wp = wp[1:]
        pts.extend(wp)
    km = lengte(pts)
    print(f"{len(pts)} punten, {km:.1f} km; begin {pts[0][0]:.4f},{pts[0][1]:.4f} eind {pts[-1][0]:.4f},{pts[-1][1]:.4f}")
    for i, m in naden:
        print(f"  naad voor way {i}: {m:.0f} m (recht verbonden)")
    print(f"  naden samen {sum(m for _, m in naden) / 1000:.2f} km")
    if args.schrijf:
        coords = [[round(p[1], 5), round(p[0], 5)] for p in pts]
        sch = [coords[0]]
        for q in coords[1:]:
            if q != sch[-1]:
                sch.append(q)
        doc = {"type": "FeatureCollection", "features": [{
            "type": "Feature",
            "properties": {"naam": "TAL Triest -> Würmlach -> Lenting/Ingolstadt (OSM-ways, 6 kartering-naden recht verbonden)",
                           "km": round(km, 2), "punten": len(sch),
                           "bron": "OpenStreetMap-bijdragers (ODbL), man_made=pipeline substance=oil, gestikt op gedeelde nodes",
                           "gereedschap": "maak_leidingbeen_olie_trieste_ingolstadt.py"},
            "geometry": {"type": "LineString", "coordinates": sch}}]}
        uit = os.path.join(BEEN, PREFIX + "-leiding.geojson")
        json.dump(doc, open(uit, "w", encoding="utf-8"), ensure_ascii=False)
        print("geschreven:", uit, f"({len(sch)} punten)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
