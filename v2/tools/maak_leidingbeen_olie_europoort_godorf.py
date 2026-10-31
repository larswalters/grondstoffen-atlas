#!/usr/bin/env python3
"""maak_leidingbeen_olie_europoort_godorf.py - de leidingbenen a1 en a2 van olie-europoort-godorf.

De routebrief (v2/design/routebrieven/olie-europoort-godorf.md) legt de Rotterdam-Rijn-Pijpleiding (RRP) vast als OSM-ways
(`man_made=pipeline substance=oil`, operator Rotterdam-Rijn Pijpleiding Maatschappij): a1 = ruwe-oliepijp 36 inch
Europoort -> Venlo (10 ways, naam "Rotterdam-Rijn-Pijpleiding Europoort - Venlo"), a2 = 24 inch Venlo -> Koeln-Hurth
(2 ways, naam "Rotterdam-Rhein-Pipeline", ref RRP 8). Geometrie per way-id uit de OSM-API (api.openstreetmap.org/api/0.6, ODbL),
met cache op schijf. Ways worden gestikt op gedeelde nodes; waar OSM zonder gedeelde node kartert (de Hollands Diep-kruising)
wordt het dichtstbijzijnde eindpunt-paar recht verbonden en de naad gerapporteerd. Het slot Hurth -> Godorf staat niet in OSM:
dat wordt in de bak-functie een stippel (geen geojson).

Uitvoer (v2/build-cache/ais/graaf/): olie-europoort-godorf-leiding-a1.geojson, olie-europoort-godorf-leiding-a2.geojson (FeatureCollections)
Draaien:  python v2/tools/maak_leidingbeen_olie_europoort_godorf.py --schrijf
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
PREFIX = "olie-europoort-godorf"
CACHE = os.path.join(WORTEL, "build-cache", PREFIX + "-osmapi-cache.json")
UA = "grondstoffen-atlas/1.0 (route research; OSM API, ODbL)"

A1 = [849066299, 849069178, 972208482, 972208481, 849221217, 849221219, 849069176, 307504353, 319472294, 849069175]
A2 = [139710565, 298322327]
ANKER_BEGIN = (51.9386, 4.1441)
ANKER_VENLO = (51.3789, 6.2160)
NAAD_MAX_KM = 1.5
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


def schrijf(naam, pts, uit, bron):
    coords = [[round(p[1], 5), round(p[0], 5)] for p in pts]
    sch = [coords[0]]
    for q in coords[1:]:
        if q != sch[-1]:
            sch.append(q)
    km = lengte([(q[1], q[0]) for q in sch])
    doc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"naam": naam, "km": round(km, 2), "punten": len(sch),
                       "bron": bron,
                       "gereedschap": "maak_leidingbeen_olie_europoort_godorf.py"},
        "geometry": {"type": "LineString", "coordinates": sch}}]}
    json.dump(doc, open(uit, "w", encoding="utf-8"), ensure_ascii=False)
    return km, len(sch)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()
    c = laad(A1 + A2)
    os.makedirs(BEEN, exist_ok=True)
    p1, n1 = stik(c, A1, ANKER_BEGIN)
    p2, n2 = stik(c, A2, p1[-1])
    print(f"a1: {len(p1)} pt, {lengte(p1):.1f} km, {p1[0]} -> {p1[-1]}; naden {[(w, round(m)) for w, m in n1]}")
    print(f"a2: {len(p2)} pt, {lengte(p2):.1f} km, {p2[0]} -> {p2[-1]}; naden {[(w, round(m)) for w, m in n2]}")
    print(f"naad a1->a2: {hav(p1[-1], p2[0]) * 1000:.0f} m")
    if args.schrijf:
        for nm, pts, naam, bron in (
            ("a1", p1, "Rotterdam-Rijn-Pijpleiding ruwe olie 36 inch Europoort -> Venlo (OSM-ways, 10 gestikt)",
             "OpenStreetMap-bijdragers (ODbL), man_made=pipeline substance=oil operator Rotterdam-Rijn Pijpleiding Maatschappij, gestikt op gedeelde nodes"),
            ("a2", p2, "Rotterdam-Rhein-Pipeline 24 inch Venlo -> Koeln-Hurth (OSM-ways, 2 gestikt)",
             "OpenStreetMap-bijdragers (ODbL), man_made=pipeline substance=oil ref RRP 8 operator Rotterdam-Rijn Pijpleiding Maatschappij")):
            uit = os.path.join(BEEN, f"{PREFIX}-leiding-{nm}.geojson")
            km, n = schrijf(naam, pts, uit, bron)
            print(f"geschreven {uit}: {km:.2f} km, {n} punten")
    return 0


if __name__ == "__main__":
    sys.exit(main())
