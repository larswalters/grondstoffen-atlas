#!/usr/bin/env python3
"""maak_leidingbeen_olie_omisalj_pancevo.py - de twee leidingbenen van olie-omisalj-pancevo (M31 golf 18).

Keten: JANAF-terminal Omisalj (Krk) -> Jadranski naftovod (JANAF) Omisalj-Sisak 36 inch -> Sisak ->
Sisak-Slavonski Brod 28 inch -> Slavonski Brod-Sotin -> Servie-deel (Sotin-Novi Sad-...) -> OSM eindigt ca. 22,5 km voor NIS Pancevo.

  a1  Omisalj -> Sisak : LETTERLIJKE KOPIE van de eerste negen ways van a1 van olie-omisalj-szazhalombatta
      (276522179 ... 275828600, 177 km), gelezen uit de Overpass-cache van die stroom, zelfde stikcode.
  a2  Sisak -> einde OSM-leiding bij Pancevo: 847788794, 1165593222, 879643929, 1057915310, 1055540678,
      1165598505, (naad ~1,2 km door NIS-Novi Sad), 1165601440, 1055818470  (OSM-API, ODbL, cache op schijf).

De stippel 22,5 km van het OSM-einde naar het NIS Pancevo-anker en de eventuele terminal-last-mile staan in bak_stromen.sh.

Draaien: python v2/tools/maak_leidingbeen_olie_omisalj_pancevo.py [--schrijf]
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
PREFIX = "olie-omisalj-pancevo"
CACHE = os.path.join(WORTEL, "build-cache", PREFIX + "-osmapi-cache.json")
CACHE_OMISALJ = os.path.join(BEEN, "olie-omisalj-szazhalombatta-overpass-cache.json")
UA = "grondstoffen-atlas/1.0 (route research; OSM API, ODbL)"
R = 6371.0088

A1 = [276522179, 859729756, 859729755, 859729754, 275847497, 275847496, 263222529, 276191744, 275828600]
A2 = [847788794, 1165593222, 879643929, 1057915310, 1055540678, 1165598505, 1165601440, 1055818470]
NAAD_MAX_KM = 2.0


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


def stik_geom(geoms, ids, begin=None, naad_max_km=NAAD_MAX_KM):
    """geoms: {id: [(lat,lon),...]}; stik in volgorde, oriënteer elke way op het dichtstbijzijnde uiteinde."""
    pts, naden = [], []
    for k, i in enumerate(ids):
        g = list(geoms[i])
        if k == 0:
            if begin is not None and hav(g[-1], begin) < hav(g[0], begin):
                g.reverse()
            pts = g
            continue
        e = pts[-1]
        if hav(e, g[-1]) < hav(e, g[0]):
            g.reverse()
        d = hav(e, g[0])
        if d > naad_max_km:
            raise SystemExit("naad te groot bij way %s: %.3f km" % (i, d))
        if d < 1e-6:
            g = g[1:]
        else:
            naden.append((i, round(d * 1000, 1)))
        pts = pts + g
    return pts, naden


def fc(lijn, naam):
    coords = [[round(p[1], 7), round(p[0], 7)] for p in lijn]
    sch = [coords[0]]
    for q in coords[1:]:
        if q != sch[-1]:
            sch.append(q)
    return {"type": "FeatureCollection", "features": [{
        "type": "Feature", "properties": {"name": naam},
        "geometry": {"type": "LineString", "coordinates": sch}}]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()
    # a1: letterlijke kopie uit de Overpass-cache van olie-omisalj-szazhalombatta (zelfde ways, zelfde stikregel)
    w = json.load(open(CACHE_OMISALJ, encoding="utf-8"))["ways"]
    g1 = {i: [tuple(p) for p in w[str(i)]["geom"]] for i in A1}
    p1, n1 = stik_geom(g1, A1, begin=(45.2208, 14.5331), naad_max_km=0.05)
    # a2: OSM-API
    c = laad(A2)
    g2 = {i: [tuple(c["nodes"][str(n)]) for n in c["ways"][str(i)]["nodes"]] for i in A2}
    p2, n2 = stik_geom(g2, A2, begin=p1[-1])
    for i in A2:
        t = c["ways"][str(i)]["tags"]
        print("way", i, t.get("name"), t.get("substance"), t.get("operator"), t.get("location"),
              "%.1f km" % lengte(g2[i]), g2[i][0], g2[i][-1])
    print("a1: %d pt, %.1f km, %s -> %s, naden %s" % (len(p1), lengte(p1), p1[0], p1[-1], n1))
    print("a2: %d pt, %.1f km, %s -> %s, naden %s" % (len(p2), lengte(p2), p2[0], p2[-1], n2))
    print("naad a1 -> a2: %.0f m" % (hav(p1[-1], p2[0]) * 1000))
    print("totaal doorgetrokken %.1f km" % (lengte(p1) + lengte(p2)))
    print("OSM-einde -> NIS Pancevo (44.8310, 20.6860): %.1f km" % hav(p2[-1], (44.8310, 20.6860)))
    if args.schrijf:
        os.makedirs(BEEN, exist_ok=True)
        for k, l, nm in (("a1", p1, "Jadranski naftovod Omisalj-Sisak (OSM, kopie van olie-omisalj-szazhalombatta)"),
                         ("a2", p2, "Jadranski naftovod Sisak-Slavonski Brod-Sotin-Novi Sad-Pancevo (OSM)")):
            p = os.path.join(BEEN, "%s-leiding-%s.geojson" % (PREFIX, k))
            json.dump(fc(l, nm), open(p, "w", encoding="utf-8"))
            print("geschreven:", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
