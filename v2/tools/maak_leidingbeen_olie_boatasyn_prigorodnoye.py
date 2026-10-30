#!/usr/bin/env python3
"""maak_leidingbeen_olie_boatasyn_prigorodnoye.py - b1 van olie-boatasyn-prigorodnoye.

WAAROM DIT BESTAAT. De routebrief (v2/design/routebrieven/olie-boatasyn-prigorodnoye.md) legt de
Trans-Sachalin-oliepijpleiding (Sakhalin Energy) vast als 8 OSM-ways (man_made=pipeline substance=oil).
pyosmium is op deze machine geblokkeerd; de geometrie komt dus per way-id uit de OSM-API
(api.openstreetmap.org, ODbL), met cache op schijf. De way-volgorde staat VAST (geen vrij kortste pad):
zo blijven de gas-parallelleiding, het kuststuk/de lagune en de LNG-ways buiten de lijn. Ways worden
gestikt op GEDEELDE OSM-NODES (naad 0 m).

Uitvoer: v2/build-cache/ais/graaf/olie-boatasyn-prigorodnoye-leiding-b1.geojson (FeatureCollection, [lon, lat]).
Draaien: python v2/tools/maak_leidingbeen_olie_boatasyn_prigorodnoye.py --schrijf
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
PREFIX = "olie-boatasyn-prigorodnoye"
CACHE = os.path.join(BEEN, PREFIX + "-osmapi-cache.json")
UA = "grondstoffen-atlas/1.0 (route research; OSM API, ODbL)"
WAYS = [394946663, 394946660, 394946668, 394946648, 409387387, 394946661, 209135245, 579594727]
OPF = (51.4166, 143.3660)
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
    for k in range(0, len(nodig), 100):
        d = _get("https://api.openstreetmap.org/api/0.6/ways.json?ways=" + ",".join(map(str, nodig[k:k + 100])))
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


def stik(c, ids):
    """Stik ways in vaste volgorde op gedeelde nodes; eerste way gericht met zijn uiteinde dichtst bij de OPF vooraan."""
    eerste = list(c["ways"][str(ids[0])]["nodes"])
    p0 = c["nodes"][str(eerste[0])]
    p1 = c["nodes"][str(eerste[-1])]
    if hav(p1, OPF) < hav(p0, OPF):
        eerste.reverse()
    keten = eerste
    for i in ids[1:]:
        nd = list(c["ways"][str(i)]["nodes"])
        eind = keten[-1]
        if nd[0] == eind:
            pass
        elif nd[-1] == eind:
            nd.reverse()
        else:
            raise SystemExit(f"way {i} sluit niet aan op een gedeelde node (eindnode {eind}) - stik-fout")
        keten += nd[1:]
    return keten


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()
    c = laad(WAYS)
    for i in WAYS:
        t = c["ways"][str(i)]["tags"]
        print(f"  way {i}: {t.get('man_made')} {t.get('substance')} {t.get('operator')} {t.get('name', '')[:40]}")
    keten = stik(c, WAYS)
    pts = [tuple(c["nodes"][str(n)]) for n in keten]
    print(f"b1: {len(pts)} punten, {lengte(pts):.1f} km, {pts[0][0]:.4f},{pts[0][1]:.4f} -> {pts[-1][0]:.4f},{pts[-1][1]:.4f}")
    if args.schrijf:
        coords = [[round(p[1], 5), round(p[0], 5)] for p in pts]
        sch = [coords[0]]
        for q in coords[1:]:
            if q != sch[-1]:
                sch.append(q)
        km = lengte([(q[1], q[0]) for q in sch])
        doc = {"type": "FeatureCollection", "features": [{
            "type": "Feature",
            "properties": {"naam": "Trans-Sachalin-oliepijpleiding OPF Nogliki → Prigorodnoje (Sakhalin Energy, OSM-leiding)",
                           "km": round(km, 2), "punten": len(sch),
                           "bron": "OpenStreetMap-bijdragers (ODbL), OSM-API way-geometrie, man_made=pipeline substance=oil, gestikt op gedeelde nodes",
                           "gereedschap": "maak_leidingbeen_olie_boatasyn_prigorodnoye.py"},
            "geometry": {"type": "LineString", "coordinates": sch}}]}
        uit = os.path.join(BEEN, PREFIX + "-leiding-b1.geojson")
        json.dump(doc, open(uit, "w", encoding="utf-8"), ensure_ascii=False)
        print(f"geschreven {uit} ({km:.2f} km, {len(sch)} punten, {os.path.getsize(uit)/1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
