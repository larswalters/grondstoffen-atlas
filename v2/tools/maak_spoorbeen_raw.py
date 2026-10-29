#!/usr/bin/env python3
"""
maak_spoorbeen_raw.py — een spoorbeen als GeoJSON uit de RUWE OSM-1-op-1-ways
(`v2/build-cache/raw1op1/<extract>.geojson`), via-punt naar via-punt.

WAAROM (kolen-carmichael-abbotpoint, M31 golf 12). `toets_spoorroute.mjs` routeert over het
bladgesnoeide 1-op-1-net (`landnet-raw.bin`): een doodlopende tak ver van elk bekend anker is daar
weggesnoeid. De 185 km lange Carmichael Rail (mijn -> aansluiting op het Newlands-systeem) is zo'n
tak: het tool valt voor het mijnuiteinde 141 km terug op de Goonyella-kant en tekent een lijn die
niet bij de mijn begint. In de RUWE ways staat de lijn wel, aaneengesloten (zelfde OSM-topologie:
verbonden = gedeelde node). Dit tool doet Dijkstra over precies die ruwe ways, zonder snoei.

Gebruik (vanuit de repo-root):
    python v2/tools/maak_spoorbeen_raw.py --extract australie \
        --van LAT,LON --naar LAT,LON [--via LAT,LON ...] --naam "<beennaam>" --uit <pad>.geojson
Uitvoer: FeatureCollection met een LineString (lon,lat), eerste/laatste punt = de ankers niet; het
begin/einde is de dichtstbijzijnde OSM-node (snap wordt gemeld). Er is geen keerstraf: de console
meldt omkeringen >= 150 graden (spike) zodat een artefact niet stil blijft staan.
"""
import argparse, heapq, json, math, os, sys
from collections import defaultdict

R = 6371.0088


def gc(a, b):
    c = (math.sin(math.radians(a[1])) * math.sin(math.radians(b[1])) +
         math.cos(math.radians(a[1])) * math.cos(math.radians(b[1])) * math.cos(math.radians(a[0] - b[0])))
    return R * math.acos(max(-1.0, min(1.0, c)))


def ll(s):
    la, lo = s.split(",")
    return (float(lo), float(la))          # intern (lon, lat)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--extract", required=True)
    ap.add_argument("--van", required=True)
    ap.add_argument("--naar", required=True)
    ap.add_argument("--via", action="append", default=[])
    ap.add_argument("--naam", required=True)
    ap.add_argument("--uit", required=True)
    ap.add_argument("--marge", type=float, default=1.0, help="graden rond de punten")
    a = ap.parse_args()
    wortel = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bron = os.path.join(wortel, "build-cache", "raw1op1", a.extract + ".geojson")
    punten = [ll(a.van)] + [ll(v) for v in a.via] + [ll(a.naar)]
    bb = (min(p[0] for p in punten) - a.marge, min(p[1] for p in punten) - a.marge,
          max(p[0] for p in punten) + a.marge, max(p[1] for p in punten) + a.marge)
    g = json.load(open(bron, encoding="utf-8"))
    adj = defaultdict(list)
    for f in g["features"]:
        if f["geometry"]["type"] != "LineString":
            continue
        p = f["geometry"]["coordinates"]
        if not any(bb[0] <= q[0] <= bb[2] and bb[1] <= q[1] <= bb[3] for q in p):
            continue
        for u, v in zip(p, p[1:]):
            u = (u[0], u[1]); v = (v[0], v[1]); d = gc(u, v)
            adj[u].append((v, d)); adj[v].append((u, d))
    print(f"ruwe graaf: {len(adj)} knopen in venster")

    def dichtst(pt):
        n = min(adj, key=lambda k: gc(k, pt))
        return n, gc(n, pt)

    lijn = []; totaal = 0.0
    for i in range(len(punten) - 1):
        s, ds = dichtst(punten[i]); t, dt = dichtst(punten[i + 1])
        print(f"deel {i + 1}: snap van {ds * 1000:.0f} m, naar {dt * 1000:.0f} m")
        dist = {s: 0.0}; prev = {}; h = [(0.0, s)]
        while h:
            d, u = heapq.heappop(h)
            if u == t:
                break
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist.get(v, 1e18):
                    dist[v] = nd; prev[v] = u; heapq.heappush(h, (nd, v))
        if t not in dist:
            sys.exit("geen pad tussen de ruwe ways (ander component)")
        pad = [t]
        while pad[-1] in prev:
            pad.append(prev[pad[-1]])
        pad.reverse()
        totaal += dist[t]
        lijn += pad if not lijn else pad[1:]
    # omkeringen
    def hoek(p, q, r):
        ax, ay = q[0] - p[0], q[1] - p[1]; bx, by = r[0] - q[0], r[1] - q[1]
        n = math.hypot(ax, ay) * math.hypot(bx, by)
        if n == 0:
            return 0.0
        return math.degrees(math.acos(max(-1.0, min(1.0, (ax * bx + ay * by) / n))))
    keer = [i for i in range(1, len(lijn) - 1) if hoek(lijn[i - 1], lijn[i], lijn[i + 1]) >= 150]
    print(f"route {totaal:.1f} km, {len(lijn)} punten, omkeringen >= 150 graden: {len(keer)}")
    for i in keer[:10]:
        print("  omkering bij", lijn[i])
    os.makedirs(os.path.dirname(os.path.abspath(a.uit)), exist_ok=True)
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"naam": a.naam, "km": round(totaal, 1), "bron": "OSM ruwe ways " + a.extract},
        "geometry": {"type": "LineString", "coordinates": [[round(x, 6), round(y, 6)] for x, y in lijn]}}]}
    json.dump(fc, open(a.uit, "w", encoding="utf-8"))
    print("geschreven:", a.uit)


if __name__ == "__main__":
    main()
