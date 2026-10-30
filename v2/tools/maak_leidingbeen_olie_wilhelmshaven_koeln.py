#!/usr/bin/env python3
"""maak_leidingbeen_olie_wilhelmshaven_koeln.py - het leidingbeen a1 van olie-wilhelmshaven-koeln.

De routebrief (v2/design/routebrieven/olie-wilhelmshaven-koeln.md) legt de Nord-West-Oelleitung (NWO,
Wilhelmshaven -> Koeln-regio) vast als 26 OSM-ways (`man_made=pipeline substance=oil`, operator Nord-West
Oelleitung GmbH). Geometrie per way-id uit de OSM-API (api.openstreetmap.org/api/0.6, ODbL; pyosmium is
geblokkeerd), met cache op schijf. Ways worden gestikt op gedeelde nodes; waar OSM de leiding zonder gedeelde
node heeft gekarteerd wordt het dichtstbijzijnde eindpunt-paar recht verbonden en de naad gerapporteerd (max 0,2 km).
Takken (Gelsenkirchen, Hamburg) zijn weggelaten. Geen stippel: kartering-hiaat van een ondergrondse leiding.

Uitvoer (v2/build-cache/ais/graaf/): olie-wilhelmshaven-koeln-leiding-a1.geojson (FeatureCollection)
Draaien:  python v2/tools/maak_leidingbeen_olie_wilhelmshaven_koeln.py --schrijf
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
PREFIX = "olie-wilhelmshaven-koeln"
CACHE = os.path.join(WORTEL, "build-cache", PREFIX + "-osmapi-cache.json")
UA = "grondstoffen-atlas/1.0 (route research; OSM API, ODbL)"

A1 = [37246878, 1170483426, 331053888, 1167228169, 1167982648, 1167228167, 802175179, 1167982649, 1167982650,
      1170470432, 1167982651, 1167982652, 199070486, 1167982653, 1170046316, 95474852, 57882826, 57882823,
      57857300, 56383213, 824960260, 751120616, 165992666, 166970499, 199084814, 945532321]
ANKER_BEGIN = (53.5563, 8.1458)
NAAD_MAX_KM = 1.0
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
    json.dump(c, open(CACHE, "w", encoding="utf-8"))
    return c


def stik(c, ids, anker):
    """Stik ways in volgorde; oriënteer elke way op het uiteinde dat het dichtst bij het vorige eind ligt;
    eerste way op het uiteinde dat het dichtst bij het anker ligt. Geeft (punten, naden[(way, m, gedeeld)])."""
    pts, naden = [], []
    for k, i in enumerate(ids):
        ns = list(c["ways"][str(i)]["nodes"])
        a, b = tuple(c["nodes"][str(ns[0])]), tuple(c["nodes"][str(ns[-1])])
        ref = anker if k == 0 else pts[-1]
        if hav(ref, b) < hav(ref, a):
            ns.reverse()
        wp = [tuple(c["nodes"][str(n)]) for n in ns]
        if pts:
            g = hav(pts[-1], wp[0])
            if g > NAAD_MAX_KM:
                raise SystemExit(f"way {i}: naad {g:.3f} km > {NAAD_MAX_KM} km")
            if g < 1e-6:
                wp = wp[1:]
            else:
                naden.append((i, g * 1000))
        pts.extend(wp)
    return pts, naden


def schrijf(naam, pts, uit):
    coords = [[round(p[1], 5), round(p[0], 5)] for p in pts]
    sch = [coords[0]]
    for q in coords[1:]:
        if q != sch[-1]:
            sch.append(q)
    km = lengte([(q[1], q[0]) for q in sch])
    doc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"naam": naam, "km": round(km, 2), "punten": len(sch),
                       "bron": "OpenStreetMap-bijdragers (ODbL), man_made=pipeline substance=oil operator Nord-West Oelleitung GmbH, gestikt op gedeelde nodes",
                       "gereedschap": "maak_leidingbeen_olie_wilhelmshaven_koeln.py"},
        "geometry": {"type": "LineString", "coordinates": sch}}]}
    json.dump(doc, open(uit, "w", encoding="utf-8"), ensure_ascii=False)
    return km, len(sch)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()
    c = laad(A1)
    os.makedirs(BEEN, exist_ok=True)
    p1, n1 = stik(c, A1, ANKER_BEGIN)
    print(f"a1: {len(p1)} pt, {lengte(p1):.1f} km, {p1[0]} -> {p1[-1]}; naden {[(w, round(m)) for w, m in n1]}")
    if args.schrijf:
        uit = os.path.join(BEEN, f"{PREFIX}-leiding-a1.geojson")
        km, n = schrijf("Nord-West-Oelleitung Wilhelmshaven -> Koeln (OSM-ways, 26 ways gestikt)", p1, uit)
        print(f"geschreven {uit}: {km:.2f} km, {n} punten")
    return 0


if __name__ == "__main__":
    sys.exit(main())
