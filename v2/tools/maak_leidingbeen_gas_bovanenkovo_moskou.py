#!/usr/bin/env python3
"""maak_leidingbeen_gas_bovanenkovo_moskou.py - leidingbenen van gas-bovanenkovo-moskou (M31 golf 16).

Eén doorlopende gas-lijn Bovanenkovo -> Ukhta -> Gryazovets -> KGMO-knoop uit OSM (man_made=pipeline), drie benen:
  A  Bovanenkovo-Ukhta                  ways "Бованенково — Ухта"            (lijn 1)
  B  Ukhta-Gryazovets                   ways "Ухта — Торжок (Ухта — Грязовец)" (= Ukhta-Torzhok 1, deel Ukhta-Gryazovets)
  C  Gryazovets-KGMO                    ways "Грязовец — КГМО"
Selectie op naam voorkomt dat het pad tussen de parallelle lijnen (Ukhta-Torzhok 2/3, SRTO-Torzhok) springt. De ways van
verschillende lijnen delen geen OSM-nodes; tussen B en C zit één naad van ~0,2 km (parallelle strengen op het
Gryazovets-station), gelegd als hulplink van 0,4 km tussen twee vertices.
Bron: OpenStreetMap-bijdragers (ODbL), Geofabrik-extracts rusland-oeral / -noordwest / -centraal.
Uitvoer in v2/build-cache/ais/graaf/ (FeatureCollection per been, punten in reisvolgorde, [lon, lat]):
  gas-bovanenkovo-moskou-leiding-bovanenkovo-ukhta.geojson  / -ukhta-gryazovets.geojson / -gryazovets-kgmo.geojson
Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_bovanenkovo_moskou.py [--schrijf]
"""
import argparse
import heapq
import json
import math
import os
import re

import osmium

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf")
GF = os.path.join(WORTEL, "build-cache", "geofabrik")
EXTRACTS = ["rusland-oeral", "rusland-noordwest", "rusland-centraal"]
NAAM = re.compile(r"^(Бованенково — Ухта|Ухта — Торжок \(Ухта — Грязовец\)|Грязовец — КГМО)$")
START = (68.2650, 70.3193)      # (lon, lat) Bovanenkovo-anker = eerste OSM-punt van de lijn
UKHTA = (53.7242, 63.6703)
GRYAZOVETS = (40.2219, 58.7627)
EIND = (37.4423, 56.3201)       # KGMO-knoop
TOL = 0.4                       # km, hulplink tussen vertices van verschillende ways
R = 6371.0088


def km(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def lengte(p):
    return sum(km(p[i], p[i + 1]) for i in range(len(p) - 1))


def scan():
    ways = {}
    for ex in EXTRACTS:
        pad = os.path.join(GF, f"{ex}-latest.osm.pbf")
        fp = (osmium.FileProcessor(pad).with_locations()
              .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
              .with_filter(osmium.filter.KeyFilter("man_made")))
        n = 0
        for o in fp:
            t = o.tags
            if t.get("man_made") != "pipeline" or not NAAM.match(t.get("name", "")):
                continue
            pts = [(round(x.location.lon, 5), round(x.location.lat, 5)) for x in o.nodes if x.location.valid()]
            if o.id not in ways or len(pts) > len(ways[o.id][1]):
                ways[o.id] = (t.get("name"), pts)
            n += 1
        print(f"  {ex}: {n} ways")
    return ways


def graaf(ways):
    adj = {}
    for wid, (_, pts) in ways.items():
        for a, b in zip(pts, pts[1:]):
            if a == b:
                continue
            d = km(a, b)
            adj.setdefault(a, []).append((b, d, wid))
            adj.setdefault(b, []).append((a, d, wid))
    grid = {}
    for v in adj:
        grid.setdefault((round(v[0] * 40), round(v[1] * 80)), []).append(v)
    naden = 0
    for (gx, gy), vs in grid.items():
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for u in grid.get((gx + dx, gy + dy), ()):
                    for v in vs:
                        if u < v and km(u, v) < TOL and not any(x[0] == u for x in adj[v]):
                            d = km(u, v)
                            adj[u].append((v, d + 5, -1))
                            adj[v].append((u, d + 5, -1))
                            naden += 1
    return adj, naden


def snap(adj, p):
    b = min(adj, key=lambda v: km(v, p))
    return b, km(b, p)


def kortste(adj, a, b):
    dist, vorig, h = {a: 0.0}, {}, [(0.0, a)]
    while h:
        d, u = heapq.heappop(h)
        if u == b:
            break
        if d > dist.get(u, 1e18):
            continue
        for v, w, wid in adj[u]:
            nd = d + w
            if nd < dist.get(v, 1e18):
                dist[v] = nd
                vorig[v] = (u, wid)
                heapq.heappush(h, (nd, v))
    pad, wl = [b], []
    while pad[-1] != a:
        u, wid = vorig[pad[-1]]
        wl.append(wid)
        pad.append(u)
    return pad[::-1], wl[::-1]


def schrijf(pad, naam, pts, extra):
    props = {"naam": naam, "km": round(lengte(pts), 2)}
    props.update(extra)
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature", "properties": props,
        "geometry": {"type": "LineString", "coordinates": [[x, y] for x, y in pts]}}]}
    with open(pad, "w", encoding="utf-8") as f:
        json.dump(fc, f, ensure_ascii=False)
    print(f"  geschreven: {pad} ({os.path.getsize(pad)/1024:.1f} KB)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    a = ap.parse_args()
    ways = scan()
    adj, naden = graaf(ways)
    print(f"  {len(ways)} ways, {len(adj)} vertices, {naden} hulplinks")
    s, ds = snap(adj, START)
    e, de = snap(adj, EIND)
    u, du = snap(adj, UKHTA)
    g, dg = snap(adj, GRYAZOVETS)
    print(f"  snap start {ds:.3f} km, Ukhta {du:.3f}, Gryazovets {dg:.3f}, eind {de:.3f}")
    pad, wl = kortste(adj, s, e)
    iu, ig = pad.index(u), pad.index(g)
    assert 0 < iu < ig < len(pad) - 1
    # per been: eerste punt van been C is het eerste punt NA de hulplink
    nad = [i for i, w in enumerate(wl) if w == -1]
    print(f"  hulplinks op pad: {len(nad)} (index {nad}), totaal {lengte(pad):.1f} km")
    ic = max(ig, nad[-1] + 1) if nad else ig
    legs = [("Bovanenkovo-Ukhta", pad[:iu + 1]), ("Ukhta-Gryazovets", pad[iu:ig + 1]), ("Gryazovets-KGMO", pad[ic:])]
    naam = {
        "Bovanenkovo-Ukhta": "Бованенково — Ухта (Baydaratskaya-baai onderdoor), OSM-ways",
        "Ukhta-Gryazovets": "Ухта — Торжок 1 (Ухта — Грязовец), OSM-ways",
        "Gryazovets-KGMO": "Грязовец — КГМО (DN1220), OSM-ways",
    }
    for i, (k, p) in enumerate(legs):
        ids = sorted({w for w in wl if w != -1 and w > 0})
        print(f"  been {k}: {len(p)} punten, {lengte(p):.1f} km; lat,lon {p[0][1]:.4f},{p[0][0]:.4f} -> {p[-1][1]:.4f},{p[-1][0]:.4f}")
        if a.schrijf:
            schrijf(os.path.join(UIT, f"gas-bovanenkovo-moskou-leiding-{k.lower()}.geojson"), naam[k], p, {})
    print(f"  naad B->C: {km(legs[1][1][-1], legs[2][1][0]):.3f} km")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
