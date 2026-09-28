#!/usr/bin/env python3
"""maak_leidingbeen_keystone.py — b1/b2 van olie-hardisty-cushing.

WAAROM DIT BESTAAT. De routebrief (v2/design/routebrieven/olie-hardisty-cushing.md)
vraagt de Keystone-hoofdleiding (Fase 1, Hardisty → Steele City) en de
Keystone-Cushing Extension (Fase 2, Steele City → Cushing) uit lokale
Geofabrik-extracts te stikken, net als bij olie-habshan-chiba/gas-chayanda-
shanghai: pyosmium-scan per extract op `man_made=pipeline` WAY's met een naam
die "keystone" bevat (case-insensitive; dekt zowel "Keystone Pipeline" als een
eventuele aparte "Keystone-Cushing Extension"/"Cushing Extension"-naam-tag),
component-graaf op gedeelde OSM-nodes (per extract — extracts clippen een way
op de grens, dus componenten over land-/staatsgrenzen heen worden NIET
verondersteld gedeeld te zijn en moeten los beoordeeld worden op de
eindpunt-afstand tot het volgende cluster).

Bron: OpenStreetMap-bijdragers (ODbL), lokale Geofabrik-extracts
v2/build-cache/geofabrik/<slug>-latest.osm.pbf (pyosmium, geen internet nodig).

Gebruik:
    python v2/tools/maak_leidingbeen_keystone.py --extract canada \
        --van 52.6437,-111.2800 --naar 40.0369,-97.0231 \
        --uit-prefix v2/build-cache/ais/graaf/olie-hardisty-cushing-leiding-canada

--van/--naar zijn lat,lon en dienen alleen om de gevonden componenten te
sorteren/rapporteren (dichtst bij van / dichtst bij naar); ze bepalen NIET
welke componenten worden geschreven. --min-km filtert ruis (afgeknipte
tak-stompjes, terreinleidingen) uit de lijst die wél geschreven wordt.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys

import osmium

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # …/v2
R = 6371.0088


def km(a, b):
    """a, b = (lon, lat)."""
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def bouw_graaf(extract_pad, naamfilter):
    buren = {}
    punt = {}
    namen = {}
    way_lijst = []  # (way_id, naam, [refs])
    ways = 0
    for obj in (osmium.FileProcessor(extract_pad)
                .with_locations()
                .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
                .with_filter(osmium.filter.KeyFilter("man_made"))):
        t = obj.tags
        if t.get("man_made") != "pipeline":
            continue
        naam = t.get("name") or t.get("ref") or ""
        if naamfilter not in naam.lower():
            continue
        ways += 1
        refs = []
        vorig = None
        for n in obj.nodes:
            if not n.location.valid():
                continue
            ref = n.ref
            punt[ref] = (n.location.lon, n.location.lat)
            namen.setdefault(ref, set()).add(naam)
            refs.append(ref)
            if vorig is not None and vorig != ref:
                d = km(punt[vorig], punt[ref])
                buren.setdefault(vorig, []).append((ref, d))
                buren.setdefault(ref, []).append((vorig, d))
            vorig = ref
        way_lijst.append((obj.id, naam, refs))
    return buren, punt, namen, ways, way_lijst


def componenten(buren, punt):
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


def component_lengte(comp, buren):
    """Som van edge-lengtes binnen dit component (elke edge één keer)."""
    tel = 0.0
    gezien = set()
    for u in comp:
        for v, d in buren.get(u, ()):
            key = (min(u, v), max(u, v))
            if key in gezien:
                continue
            gezien.add(key)
            tel += d
    return tel


def diameter_pad(comp, buren):
    """Langste eenvoudige pad in het component via dubbele BFS (aanname:
    het component is (bijna) een keten zonder aftakkingen, zoals een
    pijpleiding). BFS 1 vanaf een willekeurig punt -> verste knoop A;
    BFS 2 vanaf A -> verste knoop B; het A→B-pad is de diameter."""
    def bfs(start):
        afst = {start: 0.0}
        vorig = {}
        stapel = [start]
        volgorde = [start]
        while stapel:
            u = stapel.pop()
            for v, d in buren.get(u, ()):
                if v not in afst:
                    afst[v] = afst[u] + d
                    vorig[v] = u
                    stapel.append(v)
                    volgorde.append(v)
        verste = max(afst, key=lambda k: afst[k])
        return verste, afst, vorig

    start = next(iter(comp))
    a, _, _ = bfs(start)
    b, afst_b, vorig_b = bfs(a)
    pad = [b]
    u = b
    while u != a:
        u = vorig_b[u]
        pad.append(u)
    pad.reverse()
    return pad, afst_b[b]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--extract", required=True, help="Geofabrik-slug, bv. canada")
    ap.add_argument("--naamfilter", default="keystone")
    ap.add_argument("--van", help="lat,lon — alleen voor rapportage-sortering")
    ap.add_argument("--naar", help="lat,lon — alleen voor rapportage-sortering")
    ap.add_argument("--min-km", type=float, default=0.3)
    ap.add_argument("--uit-prefix", help="pad-prefix; schrijft <prefix>-c<idx>.geojson per component >= --min-km")
    ap.add_argument("--alleen-comp", type=int, help="schrijf via --uit-prefix alleen dit component-indexnummer")
    ap.add_argument("--knip-comp", type=int, help="component-index om te knippen op --knip (interior punt)")
    ap.add_argument("--knip", help="lat,lon — interior punt op het diameter-pad van --knip-comp waarop te knippen")
    ap.add_argument("--knip-helft", choices=["kop", "staart"], help="welke helft (t.o.v. het diameter-pad, index 0 = 'kop') na het knippen wegschrijven")
    ap.add_argument("--knip-uit", help="volledig uitpad voor de geknipte helft (los van --uit-prefix)")
    args = ap.parse_args()

    extract_pad = os.path.join(WORTEL, "build-cache", "geofabrik", f"{args.extract}-latest.osm.pbf")
    print(f"extract: {extract_pad} ({os.path.getsize(extract_pad)/1e6:.1f} MB)")

    buren, punt, namen, ways, way_lijst = bouw_graaf(extract_pad, args.naamfilter.lower())
    print(f"'{args.naamfilter}'-pipeline-ways gevonden: {ways}")
    if ways == 0:
        print("GEEN matchende ways in deze extract.")
        return 1
    for wid, naam, refs in way_lijst:
        print(f"  way/{wid}: '{naam}' ({len(refs)} punten)")

    comps = componenten(buren, punt)
    print(f"componenten: {len(comps)}")

    van = tuple(float(x) for x in args.van.split(",")) if args.van else None
    naar = tuple(float(x) for x in args.naar.split(",")) if args.naar else None

    rijen = []
    for i, c in enumerate(comps):
        lengte = component_lengte(c, buren)
        pad, diam_km = diameter_pad(c, buren)
        kop = punt[pad[0]]
        staart = punt[pad[-1]]
        dvan = km((van[1], van[0]), kop) if van else None
        dnaar = km((naar[1], naar[0]), staart) if naar else None
        rijen.append((i, len(c), lengte, diam_km, pad, kop, staart, dvan, dnaar))

    for i, n, lengte, diam_km, pad, kop, staart, dvan, dnaar in rijen:
        extra = ""
        if dvan is not None:
            extra += f" | tot --van: {dvan:.2f} km (kop) / {km((van[1],van[0]),staart):.2f} km (staart)"
        if dnaar is not None:
            extra += f" | tot --naar: {km((naar[1],naar[0]),kop):.2f} km (kop) / {dnaar:.2f} km (staart)"
        print(f"  comp {i}: {n} vertices, edge-som {lengte:.2f} km, "
              f"diameter-pad {len(pad)} pt / {diam_km:.2f} km, "
              f"kop lat,lon={kop[1]:.5f},{kop[0]:.5f} staart lat,lon={staart[1]:.5f},{staart[0]:.5f}"
              f"{extra}")

    if args.knip_comp is not None and args.knip:
        klat, klon = (float(x) for x in args.knip.split(","))
        _, _, _, _, pad, _, _, _, _ = rijen[args.knip_comp]
        # dichtstbijzijnde padpunt bij (klat, klon)
        beste_j, beste_d = None, float("inf")
        for j, ref in enumerate(pad):
            d = km((klon, klat), punt[ref])
            if d < beste_d:
                beste_j, beste_d = j, d
        print(f"\nknip comp {args.knip_comp} op padindex {beste_j}/{len(pad)-1} "
              f"(afstand tot opgegeven punt: {beste_d*1000:.0f} m, "
              f"punt lat,lon={punt[pad[beste_j]][1]:.5f},{punt[pad[beste_j]][0]:.5f})")
        kop_km = sum(km(punt[pad[j]], punt[pad[j+1]]) for j in range(beste_j))
        staart_km = sum(km(punt[pad[j]], punt[pad[j+1]]) for j in range(beste_j, len(pad)-1))
        print(f"  kop-helft (index 0..{beste_j}): {kop_km:.2f} km, {beste_j+1} punten")
        print(f"  staart-helft (index {beste_j}..{len(pad)-1}): {staart_km:.2f} km, {len(pad)-beste_j} punten")
        if args.knip_helft and args.knip_uit:
            sub = pad[:beste_j+1] if args.knip_helft == "kop" else pad[beste_j:]
            coords = [[round(punt[ref][0], 5), round(punt[ref][1], 5)] for ref in sub]
            lengte = kop_km if args.knip_helft == "kop" else staart_km
            doc = {
                "type": "FeatureCollection",
                "features": [{
                    "type": "Feature",
                    "properties": {
                        "naam": f"Keystone-pipeline component {args.knip_comp} ({args.extract}), "
                                f"{args.knip_helft}-helft na knip",
                        "km": round(lengte, 2),
                        "punten": len(sub),
                        "bron": f"OpenStreetMap-bijdragers (ODbL), extract {args.extract}, "
                                f"man_made=pipeline naam~'{args.naamfilter}', component-graaf, "
                                f"geknipt op lat,lon={klat},{klon}",
                        "gereedschap": "maak_leidingbeen_keystone.py",
                    },
                    "geometry": {"type": "LineString", "coordinates": coords},
                }],
            }
            os.makedirs(os.path.dirname(args.knip_uit), exist_ok=True)
            with open(args.knip_uit, "w", encoding="utf-8") as f:
                json.dump(doc, f, ensure_ascii=False)
            print(f"geschreven: {args.knip_uit} ({os.path.getsize(args.knip_uit)/1024:.1f} KB, {lengte:.2f} km)")

    if args.uit_prefix:
        os.makedirs(os.path.dirname(args.uit_prefix), exist_ok=True)
        for i, n, lengte, diam_km, pad, kop, staart, dvan, dnaar in rijen:
            if diam_km < args.min_km:
                continue
            if args.alleen_comp is not None and i != args.alleen_comp:
                continue
            coords = [[round(punt[ref][0], 5), round(punt[ref][1], 5)] for ref in pad]
            doc = {
                "type": "FeatureCollection",
                "features": [{
                    "type": "Feature",
                    "properties": {
                        "naam": f"Keystone-pipeline component {i} ({args.extract})",
                        "km": round(diam_km, 2),
                        "punten": len(pad),
                        "bron": f"OpenStreetMap-bijdragers (ODbL), extract {args.extract}, "
                                f"man_made=pipeline naam~'{args.naamfilter}', component-graaf "
                                f"op gedeelde OSM-nodes, diameter-pad (BFS×2)",
                        "gereedschap": "maak_leidingbeen_keystone.py",
                    },
                    "geometry": {"type": "LineString", "coordinates": coords},
                }],
            }
            pad_uit = f"{args.uit_prefix}-c{i}.geojson"
            with open(pad_uit, "w", encoding="utf-8") as f:
                json.dump(doc, f, ensure_ascii=False)
            print(f"geschreven: {pad_uit} ({os.path.getsize(pad_uit)/1024:.1f} KB, {diam_km:.2f} km)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
