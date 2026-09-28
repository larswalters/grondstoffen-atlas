#!/usr/bin/env python3
"""maak_leidingbeen_gas_hassirmel_arzew.py — fase A van gas-arzew-barcelona.

WAAROM DIT BESTAAT. De routebrief (v2/design/routebrieven/gas-arzew-barcelona.md,
b1) vraagt een topologische component-graaf over ALLE `man_made=pipeline
substance=gas`-ways in de lokale Algerije-extract, gebouwd op GEDEELDE OSM-nodes
(dezelfde methode als bak_gas_bonny_zeebrugge b2, maar hier WEL verbonden), om
het kortste/meest aannemelijke pad tussen Hassi R'Mel-gasveld en het Arzew
LNG-complex te vinden — niet aannemen uit de vier gevonden namen alleen, want
728 van 798 gas-relevante ways in de extract zijn onbenoemd.

TWEE NAMEN ZIJN VOORAF BEWEZEN VERKEERDE CORRIDOR (brief §7, dit sessie op
coördinaat gecontroleerd) en worden HARD UITGESLOTEN op way-id, niet op naam:
  * Krechba - In Salah (way 391023450, ~28,1-28,6N/2,1-2,4O — In Salah
    Gas-project, ~500 km te zuidelijk, niets met Arzew-export te maken)
  * GALSI (ways 225282712/379118070/1393655399, ~36,0-36,9N/6,2-8,1O —
    geannuleerd Sardinië/Italië-tracé)
GK3-Borg Chegga (ways 469395884/469395885/485487144) ligt oostelijk van
Hassi R'Mel — hij wordt NIET uitgesloten in de graaf (de Dijkstra mag hem
gebruiken als hij op het kortste pad ligt), maar het rapport meldt expliciet
of hij is opgenomen, zodat dat een zichtbare beslissing is en geen aanname.

Bron: OpenStreetMap-bijdragers (ODbL), lokale Geofabrik-extract
v2/build-cache/geofabrik/algerije-latest.osm.pbf (pyosmium, geen internet nodig).

Uitvoer: v2/build-cache/ais/graaf/gas-arzew-barcelona-leiding-hassirmel-arzew.geojson
(alleen geschreven bij --schrijf en een gevonden pad).

Draaien:
    python v2/tools/maak_leidingbeen_gas_hassirmel_arzew.py --schrijf
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
EXTRACT = os.path.join(WORTEL, "build-cache", "geofabrik", "algerije-latest.osm.pbf")
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf",
                    "gas-arzew-barcelona-leiding-hassirmel-arzew.geojson")

HASSIRMEL = (3.17056, 32.94722)   # (lon, lat) — anker kop
ARZEW = (-0.2395, 35.8078)        # (lon, lat) — anker laadplek

# Hard uitgesloten op way-id (bewezen verkeerde corridor, brief §7).
UITGESLOTEN_WAYS = {
    391023450,                                   # Krechba - In Salah
    225282712, 379118070, 1393655399,            # GALSI
}

R = 6371.0088


def km(a, b):
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def bouw_graaf():
    """Vertices = OSM-node-refs (exacte topologie); edges = opeenvolgende
    punten binnen één way. Geen ronding, geen snap — precies zoals de
    bak_gas_bonny_zeebrugge-b2-methode (component-check op gedeelde nodes)."""
    buren = {}
    punt = {}
    namen = {}          # node-ref -> set(way-namen) voor rapportage
    way_namen = {}
    ways = 0
    genegeerd = 0
    for obj in (osmium.FileProcessor(EXTRACT)
                .with_locations()
                .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
                .with_filter(osmium.filter.KeyFilter("man_made"))):
        t = obj.tags
        if t.get("man_made") != "pipeline" or t.get("substance") != "gas":
            continue
        if obj.id in UITGESLOTEN_WAYS:
            genegeerd += 1
            continue
        ways += 1
        naam = t.get("name") or t.get("ref") or ""
        if naam:
            way_namen[obj.id] = naam
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
                buren.setdefault(vorig, []).append((ref, d))
                buren.setdefault(ref, []).append((vorig, d))
            vorig = ref
    return buren, punt, namen, ways, genegeerd, way_namen


def dichtstbij(kandidaten, punt, doel):
    beste, besteKm = None, float("inf")
    for ref in kandidaten:
        d = km(punt[ref], doel)
        if d < besteKm:
            beste, besteKm = ref, d
    return beste, besteKm


def alle_componenten(buren, punt):
    """Alle samenhangende componenten van de graaf, grootste eerst.

    ⚠️ De globaal dichtstbijzijnde vertex bij een anker ligt vaak op een
    KLEINE geïsoleerde stomp (een paar meter grond bij het veld/complex die
    los in OSM staat) en niet op de doorlopende trunkleiding. Zaaien moet
    daarom PER COMPONENT gebeuren, niet op de absoluut dichtstbijzijnde
    vertex over de hele graaf — anders concludeer je "geen pad" terwijl het
    net er wél is, alleen niet op dat ene losse stompje."""
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

    print(f"extract: {EXTRACT} ({os.path.getsize(EXTRACT)/1e6:.1f} MB)")
    buren, punt, namen, ways, genegeerd, way_namen = bouw_graaf()
    print(f"gas-pipeline-ways meegenomen: {ways} (genegeerd op way-id: {genegeerd})")
    print(f"vertices: {len(punt)}")

    comps = alle_componenten(buren, punt)
    print(f"componenten: {len(comps)} (grootste {len(comps[0])} vertices)")

    # Zaai PER COMPONENT (zie de docstring bij alle_componenten): kies de
    # component die de twee ankers samen het dichtst benadert, niet de
    # absoluut dichtstbijzijnde vertex over de hele graaf.
    beste = None
    for i, c in enumerate(comps):
        ra, da = dichtstbij(c, punt, HASSIRMEL)
        rb, db = dichtstbij(c, punt, ARZEW)
        if beste is None or (da + db) < beste[0]:
            beste = (da + db, i, ra, da, rb, db)
    _, i, a, aKm, b, bKm = beste
    print(f"beste component: index {i}, {len(comps[i])} vertices")
    print(f"  aansluiting Hassi R'Mel: {aKm:.2f} km "
          f"({', '.join(sorted(namen.get(a, []))) or 'onbenoemd'})")
    print(f"  aansluiting Arzew: {bKm:.2f} km "
          f"({', '.join(sorted(namen.get(b, []))) or 'onbenoemd'})")

    pad, lengte = kortste_pad(buren, a, b)
    if pad is None:
        print("⚠️ GEEN aaneengesloten OSM-pad tussen de twee ankers binnen de "
              "gas-pipeline-ways van deze extract — b1 moet dan (deels) stippel worden.")
        return 1

    gk3_ids = {469395884, 469395885, 485487144}
    gk3_namen = {"GK3 - Borg Chegga", "GK3-Borg Chegga"}
    pad_namen = set()
    for ref in pad:
        pad_namen |= namen.get(ref, set())
    gk3_op_pad = bool(pad_namen & gk3_namen)
    print(f"pad: {len(pad)} punten · {lengte:.2f} km "
          f"(hemelsbreed {km(HASSIRMEL, ARZEW):.1f} km, omwegfactor "
          f"{lengte/km(HASSIRMEL, ARZEW):.3f})")
    print(f"namen op het pad: {sorted(pad_namen) or ['(uitsluitend onbenoemde ways)']}")
    print(f"GK3-Borg Chegga op het gevonden pad: {gk3_op_pad}")

    kop = punt[pad[0]]
    staart = punt[pad[-1]]
    print("\n  de twee GESTIPPELDE anker-aansluitingen (geen OSM-way op het terrein):")
    print(f'    --stippel "leiding|gasveld-verzamelnet Hassi R\'Mel → trunkleiding '
          f'(schematisch — geen OSM-way op het veldterrein, {aKm:.1f} km)|'
          f'{HASSIRMEL[1]:.5f},{HASSIRMEL[0]:.5f}|{kop[1]:.5f},{kop[0]:.5f}"')
    print(f'    --stippel "leiding|trunkleiding → Arzew LNG-complex '
          f'(schematisch — geen OSM-way op het complexterrein, {bKm:.1f} km)|'
          f'{staart[1]:.5f},{staart[0]:.5f}|{ARZEW[1]:.5f},{ARZEW[0]:.5f}"')

    if args.schrijf:
        coords = [[round(punt[ref][0], 5), round(punt[ref][1], 5)] for ref in pad]
        doc = {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "properties": {
                    "naam": "Hassi R'Mel-gasveld → Arzew LNG-complex "
                            "(aannemelijk: exacte way-keten bake-werk)",
                    "km": round(lengte, 2),
                    "punten": len(pad),
                    "bron": f"OpenStreetMap-bijdragers (ODbL), {ways} "
                            f"man_made=pipeline substance=gas-ways in de "
                            f"algerije-extract, component-graaf op gedeelde "
                            f"OSM-nodes; Krechba-In Salah + GALSI uitgesloten "
                            f"op way-id",
                    "gk3BorgChegga_opgenomen": gk3_op_pad,
                    "gereedschap": "maak_leidingbeen_gas_hassirmel_arzew.py",
                },
                "geometry": {"type": "LineString", "coordinates": coords},
            }],
        }
        os.makedirs(os.path.dirname(UIT), exist_ok=True)
        with open(UIT, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False)
        print(f"geschreven: {UIT} ({os.path.getsize(UIT)/1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
