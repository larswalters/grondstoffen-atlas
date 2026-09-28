#!/usr/bin/env python3
"""maak_leidingbeen_olie_sangachal_ceyhan.py — b1 van olie-sangachal-ceyhan.

WAAROM DIT BESTAAT. De routebrief (v2/design/routebrieven/olie-sangachal-ceyhan.md,
b1) vraagt de Baku-Tbilisi-Ceyhan (BTC)-hoofdleiding te stikken uit drie lokale
Geofabrik-extracts (azerbeidzjan, georgie, turkije): pyosmium-scan op
`man_made=pipeline` + `substance=oil` + naam ~ btc/baku/bakı/tbilisi/tiflis/ceyhan
(Baku-Supsa expliciet uitgesloten op "supsa"/"სუფსა"), component-graaf op GEDEELDE
OSM-nodes over de drie extracts heen (een grensoverschrijdende way staat in BEIDE
buurextracts met dezelfde node-refs — dat is precies hoe Geofabrik-extracts
clippen, dus samenvoegen op node-id stikt de grens vanzelf dicht zonder los
grens-gerommel), en dan het kortste/meest aannemelijke pad tussen de twee ankers
(Sangachal Terminal / Ceyhan-exportterminal). Zelfde methode als
maak_leidingbeen_gas_hassirmel_arzew.py, nu over drie extracts i.p.v. één.

Bron: OpenStreetMap-bijdragers (ODbL), lokale Geofabrik-extracts
v2/build-cache/geofabrik/{azerbeidzjan,georgie,turkije}-latest.osm.pbf.

Uitvoer: v2/build-cache/ais/graaf/olie-sangachal-ceyhan-leiding-btc[-c<i>].geojson
(bij --schrijf; één bestand per gevonden segment als het pad niet aaneengesloten is).

Draaien:
    python v2/tools/maak_leidingbeen_olie_sangachal_ceyhan.py --schrijf
"""
from __future__ import annotations

import argparse
import heapq
import json
import math
import os
import sys

import osmium

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # …/v2
EXTRACTS = ["azerbeidzjan", "georgie", "turkije"]
UIT_PREFIX = os.path.join(WORTEL, "build-cache", "ais", "graaf",
                           "olie-sangachal-ceyhan-leiding-btc")

SANGACHAL = (49.4813, 40.2013)  # (lon, lat) — anker kop
CEYHAN = (35.9333, 36.8500)     # (lon, lat) — anker staart

NAAMFILTER = ("btc", "baku", "bakı", "tbilisi", "tiflis", "ceyhan",
              "ბაქო", "თბილისი", "ჯეიჰან")
UITSLUITEN = ("supsa", "სუფსა")

R = 6371.0088


def km(a, b):
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def scan_extract(slug):
    pad = os.path.join(WORTEL, "build-cache", "geofabrik", f"{slug}-latest.osm.pbf")
    punt = {}
    namen = {}
    way_namen = {}
    edges = []  # (ref_a, ref_b, km)
    ways = 0
    for obj in (osmium.FileProcessor(pad)
                .with_locations()
                .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
                .with_filter(osmium.filter.KeyFilter("man_made"))):
        t = obj.tags
        if t.get("man_made") != "pipeline" or t.get("substance") != "oil":
            continue
        naam = t.get("name") or t.get("ref") or ""
        naam_l = naam.lower()
        if any(u in naam_l for u in UITSLUITEN):
            continue
        if naam and not any(f in naam_l for f in NAAMFILTER):
            continue
        if not naam:
            continue
        ways += 1
        way_namen[obj.id] = naam
        vorig = None
        for n in obj.nodes:
            if not n.location.valid():
                continue
            ref = n.ref
            punt[ref] = (n.location.lon, n.location.lat)
            namen.setdefault(ref, set()).add(naam)
            if vorig is not None and vorig != ref:
                edges.append((vorig, ref, km(punt[vorig], punt[ref])))
            vorig = ref
    print(f"  {slug}: {os.path.getsize(pad)/1e6:.1f} MB, {ways} matchende ways, {len(punt)} vertices")
    return punt, namen, edges, ways, way_namen


def alle_componenten(buren, punt):
    gezien = set()
    comps = []
    for start in punt:
        if start in gezien:
            continue
        stapel = [start]
        comp = {start}
        gezien.add(start)
        while stapel:
            u = stapel.pop()
            for v, _ in buren.get(u, ()):
                if v not in comp:
                    comp.add(v)
                    gezien.add(v)
                    stapel.append(v)
        comps.append(comp)
    comps.sort(key=len, reverse=True)
    return comps


def dichtstbij(kandidaten, punt, doel):
    beste, besteKm = None, float("inf")
    for ref in kandidaten:
        d = km(punt[ref], doel)
        if d < besteKm:
            beste, besteKm = ref, d
    return beste, besteKm


def kortste_pad(buren, start, doel):
    dist = {start: 0.0}
    vorig = {}
    heap = [(0.0, start)]
    gezien = set()
    while heap:
        d, u = heapq.heappop(heap)
        if u in gezien:
            continue
        gezien.add(u)
        if u == doel:
            break
        for v, w in buren.get(u, ()):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                vorig[v] = u
                heapq.heappush(heap, (nd, v))
    if doel not in dist:
        return None, float("inf")
    pad, u = [doel], doel
    while u != start:
        u = vorig[u]
        pad.append(u)
    pad.reverse()
    return pad, dist[doel]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()

    punt = {}
    namen = {}
    buren = {}
    totaal_ways = 0
    print("scan per extract:")
    for slug in EXTRACTS:
        p, n, edges, ways, _ = scan_extract(slug)
        totaal_ways += ways
        for ref, xy in p.items():
            punt[ref] = xy
        for ref, s in n.items():
            namen.setdefault(ref, set()).update(s)
        for a, b, d in edges:
            buren.setdefault(a, []).append((b, d))
            buren.setdefault(b, []).append((a, d))
    print(f"totaal matchende ways over 3 extracts: {totaal_ways}, vertices: {len(punt)}")

    comps = alle_componenten(buren, punt)
    print(f"componenten: {len(comps)} (grootste {len(comps[0])} vertices)")
    for i, c in enumerate(comps[:10]):
        ra, da = dichtstbij(c, punt, SANGACHAL)
        rb, db = dichtstbij(c, punt, CEYHAN)
        print(f"  comp {i}: {len(c)} vertices | naar Sangachal {da:.1f} km | naar Ceyhan {db:.1f} km")

    # Kies per component de beste (dichtst bij BEIDE ankers samen) — niet de
    # absoluut dichtstbijzijnde vertex over de hele graaf (die kan op een los
    # stompje bij het terrein liggen i.p.v. de doorlopende trunkleiding).
    beste = None
    for i, c in enumerate(comps):
        ra, da = dichtstbij(c, punt, SANGACHAL)
        rb, db = dichtstbij(c, punt, CEYHAN)
        if beste is None or (da + db) < beste[0]:
            beste = (da + db, i, ra, da, rb, db)
    _, i, a, aKm, b, bKm = beste
    print(f"\nbeste component: index {i}, {len(comps[i])} vertices")
    print(f"  aansluiting Sangachal: {aKm:.2f} km ({', '.join(sorted(namen.get(a, []))) or 'onbenoemd'})")
    print(f"  aansluiting Ceyhan: {bKm:.2f} km ({', '.join(sorted(namen.get(b, []))) or 'onbenoemd'})")

    pad, lengte = kortste_pad(buren, a, b)
    if pad is None:
        print("⚠️ GEEN aaneengesloten pad binnen dit component tussen de twee "
              "dichtstbijzijnde vertices — rapporteer per losse component.")
        # Schrijf elk component >= 5 km als los segment, gesorteerd op lat/lon
        # zodat de bak-functie ze in reisvolgorde kan opnemen met stippel-naden.
        if args.schrijf:
            os.makedirs(os.path.dirname(UIT_PREFIX), exist_ok=True)
            for idx, c in enumerate(comps):
                # diameter-pad via dubbele BFS
                def bfs(start):
                    afst = {start: 0.0}
                    vorig = {}
                    stapel = [start]
                    while stapel:
                        u = stapel.pop()
                        for v, dd in buren.get(u, ()):
                            if v not in afst:
                                afst[v] = afst[u] + dd
                                vorig[v] = u
                                stapel.append(v)
                    verste = max(afst, key=lambda k: afst[k])
                    return verste, afst, vorig
                s0 = next(iter(c))
                a2, _, _ = bfs(s0)
                b2, afst_b, vorig_b = bfs(a2)
                p2 = [b2]
                u = b2
                while u != a2:
                    u = vorig_b[u]
                    p2.append(u)
                p2.reverse()
                seglen = afst_b[b2]
                if seglen < 5.0:
                    continue
                coords = [[round(punt[r][0], 5), round(punt[r][1], 5)] for r in p2]
                doc = {
                    "type": "FeatureCollection",
                    "features": [{
                        "type": "Feature",
                        "properties": {
                            "naam": f"BTC-hoofdleiding, component {idx}",
                            "km": round(seglen, 2),
                            "punten": len(p2),
                            "bron": "OpenStreetMap-bijdragers (ODbL), 3 lokale extracts "
                                    "(azerbeidzjan/georgie/turkije), man_made=pipeline "
                                    "substance=oil naam~btc/baku/tbilisi/ceyhan",
                            "gereedschap": "maak_leidingbeen_olie_sangachal_ceyhan.py",
                        },
                        "geometry": {"type": "LineString", "coordinates": coords},
                    }],
                }
                uit = f"{UIT_PREFIX}-c{idx}.geojson"
                with open(uit, "w", encoding="utf-8") as f:
                    json.dump(doc, f, ensure_ascii=False)
                print(f"geschreven: {uit} ({os.path.getsize(uit)/1024:.1f} KB, "
                      f"{seglen:.2f} km, kop {punt[p2[0]][1]:.5f},{punt[p2[0]][0]:.5f} "
                      f"staart {punt[p2[-1]][1]:.5f},{punt[p2[-1]][0]:.5f})")
        return 1

    kop = punt[pad[0]]
    staart = punt[pad[-1]]
    hemelsbreed = km(SANGACHAL, CEYHAN)
    print(f"\npad: {len(pad)} punten · {lengte:.2f} km "
          f"(hemelsbreed {hemelsbreed:.1f} km, omwegfactor {lengte/hemelsbreed:.3f})")
    print(f"aansluiting Sangachal-kant: {aKm:.2f} km — stippel nodig")
    print(f"aansluiting Ceyhan-kant: {bKm:.2f} km — stippel nodig")

    if args.schrijf:
        coords = [[round(punt[ref][0], 5), round(punt[ref][1], 5)] for ref in pad]
        doc = {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "properties": {
                    "naam": "Baku-Tbilisi-Ceyhan (BTC) hoofdleiding (aannemelijk: exacte "
                            "way-keten, component-graaf over 3 extracts)",
                    "km": round(lengte, 2),
                    "punten": len(pad),
                    "bron": f"OpenStreetMap-bijdragers (ODbL), {totaal_ways} man_made=pipeline "
                            f"substance=oil-ways over azerbeidzjan/georgie/turkije, component-graaf "
                            f"op gedeelde OSM-nodes over de extractgrenzen heen",
                    "gereedschap": "maak_leidingbeen_olie_sangachal_ceyhan.py",
                },
                "geometry": {"type": "LineString", "coordinates": coords},
            }],
        }
        uit = f"{UIT_PREFIX}.geojson"
        os.makedirs(os.path.dirname(uit), exist_ok=True)
        with open(uit, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False)
        print(f"geschreven: {uit} ({os.path.getsize(uit)/1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
