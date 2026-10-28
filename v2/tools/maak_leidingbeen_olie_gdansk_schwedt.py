#!/usr/bin/env python3
"""maak_leidingbeen_olie_gdansk_schwedt.py - de twee leidingbenen a2 en a3 van olie-gdansk-schwedt.

De routebrief (v2/design/routebrieven/olie-gdansk-schwedt.md) legt de Rurociag Pomorski (PERN-basis Gdansk ->
Plock) en de Przyjazn-noordtak (Plock -> PCK Schwedt) vast als OSM `man_made=pipeline substance=oil`-ways.
Geometrie per way-id uit de OSM-API (api.openstreetmap.org/api/0.6, ODbL; pyosmium is geblokkeerd), met cache
op schijf. Ways worden gestikt op gedeelde nodes; waar OSM de leiding zonder gedeelde node heeft gekarteerd
(4 naden, samen ~0,6 km) wordt het dichtstbijzijnde eindpunt-paar recht verbonden en de naad gerapporteerd.
Geen stippel: kartering-hiaat van een ondergrondse leiding, geen net-gat.

  a2  1122681226, 1123298008, 1378110022                 (PERN-basis Gdansk -> Plock)
  a3  578626377, 1122655730, 1122655732, 1122655733, 1433874907, 1433874903, 1433874905, 1433874904,
      578626376, 279727288, 273290090, 1050745426        (Plock -> PCK Schwedt)
Uitgesloten: oostspur 1122657839.

Uitvoer (v2/build-cache/ais/graaf/): olie-gdansk-schwedt-leiding-a2.geojson, -a3.geojson (FeatureCollection)
Draaien:  python v2/tools/maak_leidingbeen_olie_gdansk_schwedt.py --schrijf
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
PREFIX = "olie-gdansk-schwedt"
CACHE = os.path.join(WORTEL, "build-cache", PREFIX + "-osmapi-cache.json")
UA = "grondstoffen-atlas/1.0 (route research; OSM API, ODbL)"

A2 = [1122681226, 1123298008, 1378110022]
A3 = [578626377, 1122655730, 1122655732, 1122655733, 1433874907, 1433874903, 1433874905, 1433874904,
      578626376, 279727288, 273290090, 1050745426]
ANKER_GDANSK = (54.3401, 18.7464)
ANKER_PLOCK = (52.5333, 19.8322)
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
                       "bron": "OpenStreetMap-bijdragers (ODbL), man_made=pipeline substance=oil, gestikt op gedeelde nodes",
                       "gereedschap": "maak_leidingbeen_olie_gdansk_schwedt.py"},
        "geometry": {"type": "LineString", "coordinates": sch}}]}
    json.dump(doc, open(uit, "w", encoding="utf-8"), ensure_ascii=False)
    return km, len(sch)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()
    c = laad(A2 + A3)
    os.makedirs(BEEN, exist_ok=True)
    p2, n2 = stik(c, A2, ANKER_GDANSK)
    p3, n3 = stik(c, A3, ANKER_PLOCK)
    print(f"a2: {len(p2)} pt, {lengte(p2):.1f} km, {p2[0]} -> {p2[-1]}; naden {[(w, round(m)) for w, m in n2]}")
    print(f"a3: {len(p3)} pt, {lengte(p3):.1f} km, {p3[0]} -> {p3[-1]}; naden {[(w, round(m)) for w, m in n3]}")
    print(f"naad a2->a3: {hav(p2[-1], p3[0]) * 1000:.0f} m")
    # a3 begint op de Plock-knoop waar a2 eindigt (de brief-naad van 0,18 km is dan een rechte stukje in a3)
    g = hav(p2[-1], p3[0])
    if 0 < g <= NAAD_MAX_KM:
        p3 = [p2[-1]] + p3
        print(f"a3 krijgt het a2-eindpunt als kop ({g * 1000:.0f} m recht stuk)")
    if args.schrijf:
        for naam, pts, titel in (("a2", p2, "Rurociag Pomorski, PERN-basis Gdansk -> Plock (OSM-ways)"),
                                 ("a3", p3, "Przyjazn noordtak Plock -> PCK Schwedt (OSM-ways, 4 kartering-naden recht verbonden)")):
            uit = os.path.join(BEEN, f"{PREFIX}-leiding-{naam}.geojson")
            km, n = schrijf(titel, pts, uit)
            print(f"geschreven {uit}: {km:.2f} km, {n} punten")
    return 0


if __name__ == "__main__":
    sys.exit(main())
