#!/usr/bin/env python3
"""maak_leidingbeen_gas_snohvit_incukalns.py - leidingbenen van gas-snohvit-incukalns.

b1 (fase A): Snohvit-pipeline, Snohvit-veld -> Hammerfest LNG (Melkoya). OSM-ways 1118916982 + 174753089
   (Equinor, substance=gas) via de OSM-API, gestikt tot een LineString.
b3 (fase C): Klaipeda -> Incukalns. Component-graaf op gedeelde OSM-nodes over ALLE man_made=pipeline
   substance=gas-ways in de lokale extracts litouwen + letland; kortste pad tussen de component-vertices
   het dichtst bij Klaipeda-FSRU en Incukalns-UGS (patroon maak_leidingbeen_gas_hassirmel_arzew.py).

Bron: OpenStreetMap-bijdragers (ODbL). Uitvoer in v2/build-cache/ais/graaf/:
  gas-snohvit-incukalns-leiding-snohvit.geojson
  gas-snohvit-incukalns-leiding-klaipeda-incukalns.geojson

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_snohvit_incukalns.py [--schrijf]
"""
import argparse
import heapq
import json
import math
import os
import urllib.request
import xml.etree.ElementTree as ET

import osmium

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf")
GF = os.path.join(WORTEL, "build-cache", "geofabrik")
EXTRACTS = ["litouwen", "letland"]
SNOHVIT_WAYS = [1118916982, 174753089]
KLAIPEDA = (21.1375, 55.6647)    # (lon, lat)
INCUKALNS = (24.6968, 57.1690)
R = 6371.0088


def km(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def lengte(p):
    return sum(km(p[i], p[i + 1]) for i in range(len(p) - 1))


def haal(way):
    url = f"https://api.openstreetmap.org/api/0.6/way/{way}/full"
    req = urllib.request.Request(url, headers={"User-Agent": "grondstoffen-atlas/1.0"})
    root = ET.fromstring(urllib.request.urlopen(req, timeout=90).read())
    nodes = {n.get("id"): (float(n.get("lon")), float(n.get("lat"))) for n in root.findall("node")}
    w = root.find("way")
    tags = {t.get("k"): t.get("v") for t in w.findall("tag")}
    return [nodes[n.get("ref")] for n in w.findall("nd")], tags


def snohvit():
    ps = []
    for w in SNOHVIT_WAYS:
        p, tags = haal(w)
        print(f"  way {w}: {len(p)} punten, {lengte(p):.1f} km, tags {tags}")
        ps.append(p)
    # stik: kies de oriëntatie van elke way zo dat de naad minimaal is
    beste = None
    for a in (ps[0], ps[0][::-1]):
        for b in (ps[1], ps[1][::-1]):
            d = km(a[-1], b[0])
            if beste is None or d < beste[0]:
                beste = (d, a + b)
    d, pts = beste
    # richting: begin bij het Snohvit-veld (noord, lat ~71.57), eind Melkoya (lat ~70.686)
    if pts[0][1] < pts[-1][1]:
        pts = pts[::-1]
    return pts, [round(d, 3)]


def bouw_graaf():
    buren, punt, namen, ways = {}, {}, {}, 0
    for ex in EXTRACTS:
        pad = os.path.join(GF, f"{ex}-latest.osm.pbf")
        for obj in (osmium.FileProcessor(pad).with_locations()
                    .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
                    .with_filter(osmium.filter.KeyFilter("man_made"))):
            t = obj.tags
            if t.get("man_made") != "pipeline" or t.get("substance") != "gas":
                continue
            ways += 1
            naam = t.get("name") or t.get("ref") or ""
            vorig = None
            for n in obj.nodes:
                if not n.location.valid():
                    continue
                ref = n.ref
                punt[ref] = (n.location.lon, n.location.lat)
                if naam:
                    namen.setdefault(ref, set()).add(naam)
                if vorig is not None and vorig != ref:
                    d = km(punt[vorig], punt[ref])
                    buren.setdefault(vorig, []).append((ref, d, obj.id))
                    buren.setdefault(ref, []).append((vorig, d, obj.id))
                vorig = ref
    return buren, punt, namen, ways


def componenten(buren, punt):
    gezien, comps = set(), []
    for s in punt:
        if s in gezien:
            continue
        st, c = [s], {s}
        gezien.add(s)
        while st:
            u = st.pop()
            for v, _, _w in buren.get(u, ()):
                if v not in c:
                    c.add(v)
                    gezien.add(v)
                    st.append(v)
        comps.append(c)
    comps.sort(key=len, reverse=True)
    return comps


def dichtstbij(c, punt, doel):
    b, bk = None, 1e18
    for r in c:
        d = km(punt[r], doel)
        if d < bk:
            b, bk = r, d
    return b, bk


def kortste(buren, a, b):
    dist, vorig, heap, gez = {a: 0.0}, {}, [(0.0, a)], set()
    while heap:
        d, u = heapq.heappop(heap)
        if u in gez:
            continue
        gez.add(u)
        if u == b:
            break
        for v, w, wid in buren.get(u, ()):
            nd = d + w
            if nd < dist.get(v, 1e18):
                dist[v] = nd
                vorig[v] = (u, wid)
                heapq.heappush(heap, (nd, v))
    if b not in dist:
        return None, None, None
    pad, ways, u = [b], [], b
    while u != a:
        u, wid = vorig[u]
        pad.append(u)
        ways.append(wid)
    pad.reverse()
    ways.reverse()
    return pad, dist[b], ways


def schrijf(pad, naam, pts, extra=None):
    props = {"naam": naam, "km": round(lengte(pts), 2)}
    props.update(extra or {})
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature", "properties": props,
        "geometry": {"type": "LineString", "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    os.makedirs(UIT, exist_ok=True)
    with open(pad, "w", encoding="utf-8") as f:
        json.dump(fc, f, ensure_ascii=False)
    print(f"  geschreven: {pad} ({os.path.getsize(pad)/1024:.1f} KB)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    a = ap.parse_args()

    print("b1 Snohvit")
    pts, naden = snohvit()
    print(f"  {len(pts)} punten, {lengte(pts):.1f} km, naden {naden}; begin lat,lon {pts[0][1]:.4f},{pts[0][0]:.4f}; "
          f"eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}")
    if a.schrijf:
        schrijf(os.path.join(UIT, "gas-snohvit-incukalns-leiding-snohvit.geojson"),
                "Snohvit-pipeline, Snohvit-veld -> Hammerfest LNG Melkoya (OSM-ways 1118916982+174753089, Equinor)", pts)

    print("b3 Klaipeda -> Incukalns")
    buren, punt, namen, ways = bouw_graaf()
    print(f"  gas-ways: {ways}, vertices {len(punt)}")
    comps = componenten(buren, punt)
    print(f"  componenten: {len(comps)}, grootste {[len(c) for c in comps[:5]]}")
    beste = None
    for i, c in enumerate(comps):
        ra, da = dichtstbij(c, punt, KLAIPEDA)
        rb, db = dichtstbij(c, punt, INCUKALNS)
        if beste is None or da + db < beste[0]:
            beste = (da + db, i, ra, da, rb, db)
    _, i, ra, da, rb, db = beste
    print(f"  beste component {i} ({len(comps[i])} vertices): aansluiting Klaipeda {da:.2f} km, Incukalns {db:.2f} km")
    pad, d, wids = kortste(buren, ra, rb)
    if pad is None:
        print("  GEEN pad")
        return 1
    p = [punt[r] for r in pad]
    uniek = []
    for w in wids:
        if not uniek or uniek[-1] != w:
            uniek.append(w)
    print(f"  pad {len(pad)} punten, {d:.1f} km (hemelsbreed {km(KLAIPEDA, INCUKALNS):.1f}), {len(uniek)} ways: {uniek}")
    print(f"  begin lat,lon {p[0][1]:.5f},{p[0][0]:.5f}; eind {p[-1][1]:.5f},{p[-1][0]:.5f}")
    ns = set()
    for r in pad:
        ns |= namen.get(r, set())
    print(f"  namen op pad: {sorted(ns) or ['(onbenoemd)']}")
    if a.schrijf:
        schrijf(os.path.join(UIT, "gas-snohvit-incukalns-leiding-klaipeda-incukalns.geojson"),
                "Klaipeda -> Incukalns (Litouws-Latvisch gastransmissienet, OSM-graafpad, aannemelijk: een bron)", p,
                {"ways": uniek})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
