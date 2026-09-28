#!/usr/bin/env python3
"""maak_leidingbeen_olie_sumed.py — been b2 van olie-rastanura-sidikerir.

WAAROM DIT BESTAAT. De routebrief (v2/design/routebrieven/olie-rastanura-sidikerir.md,
b2) legt de SUMED-hoofdleiding (Ain Sokhna -> Sidi Kerir) vast als zes benoemde
`man_made=pipeline substance=oil`-ways in de egypte-extract: "sumed 1".."sumed 5" en
"sumed 7" (ids 97801692 / 802304836 / 107701168 / 293024229 / 802304835 / 97808606).
"sumed 6" ontbreekt in deze extract (kaarteringsgat van ~17,5 km tussen sumed 5 en
sumed 7). sumed 8.1/8.2/8.3 (ids 802491218-220, offshore SBM-aansluitleidingen bij
Sidi Kerir) worden NIET meegenomen (brief §7).

Dit script haalt de zes ways letterlijk op (pyosmium, geen internet nodig), stikt ze
op EXACTE OSM-nodecoordinaten (geen snap/ronding) in reisvolgorde Ain Sokhna -> Sidi
Kerir, en schrijft TWEE geojsons (het kaarteringsgat blijft ertussen als eigen
--stippel in bak_stromen.sh):
  segment 1 = sumed 1 + 2 + 3 + 4 + 5 (in die volgorde, elk voorwaarts of
              omgekeerd zodat de ketting doorloopt)
  segment 2 = sumed 7, IN OMGEKEERDE RICHTING (deze way loopt in OSM van Sidi Kerir
              terug naar het gat, dus omgekeerd om Ain Sokhna -> Sidi Kerir te volgen)

Bron: OpenStreetMap-bijdragers (ODbL), lokale Geofabrik-extract
v2/build-cache/geofabrik/egypte-latest.osm.pbf.

Uitvoer:
  v2/build-cache/ais/graaf/olie-rastanura-sidikerir-leiding-sokhna-gat.geojson
  v2/build-cache/ais/graaf/olie-rastanura-sidikerir-leiding-gat-sidikerir.geojson

Draaien:
    python v2/tools/maak_leidingbeen_olie_sumed.py --schrijf
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys

import osmium

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
EXTRACT = os.path.join(WORTEL, "build-cache", "geofabrik", "egypte-latest.osm.pbf")
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
UIT1 = os.path.join(BEEN, "olie-rastanura-sidikerir-leiding-sokhna-gat.geojson")
UIT2 = os.path.join(BEEN, "olie-rastanura-sidikerir-leiding-gat-sidikerir.geojson")

# reisvolgorde Ain Sokhna -> Sidi Kerir
SEGMENT1_IDS = [97801692, 802304836, 107701168, 293024229, 802304835]  # sumed 1..5
SEGMENT2_IDS = [97808606]                                              # sumed 7 (reversed)

NAMEN = {
    97801692: "sumed 1", 802304836: "sumed 2", 107701168: "sumed 3",
    293024229: "sumed 4", 802304835: "sumed 5", 97808606: "sumed 7",
}

R = 6371.0088


def km(a, b):
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def lijnlengte(coords):
    return sum(km(coords[i], coords[i + 1]) for i in range(len(coords) - 1))


def haal_ways(alle_ids):
    """Eén pass over de extract, haal de gevraagde way-ids op met hun
    node-coordinaten (lon, lat) in OSM-volgorde."""
    gevonden = {}
    for obj in (osmium.FileProcessor(EXTRACT)
                .with_locations()
                .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))):
        if obj.id not in alle_ids:
            continue
        coords = []
        for n in obj.nodes:
            if not n.location.valid():
                continue
            coords.append((n.location.lon, n.location.lat))
        gevonden[obj.id] = coords
        if len(gevonden) == len(alle_ids):
            break
    return gevonden


def stik_in_volgorde(ways, ids):
    """Stik een lijst way-id's tot 1 doorlopende coordinatenlijst. Voor elke
    volgende way wordt gekeken welk uiteinde (begin of eind, evt. omgekeerd)
    het dichtst aansluit bij het huidige staarpunt."""
    coords = list(ways[ids[0]])
    for wid in ids[1:]:
        stuk = ways[wid]
        staart = coords[-1]
        kandidaten = [
            (km(staart, stuk[0]), stuk),
            (km(staart, stuk[-1]), list(reversed(stuk))),
        ]
        kandidaten.sort(key=lambda x: x[0])
        afstand, gekozen = kandidaten[0]
        if afstand > 1.0:
            print(f"  ⚠ way {wid} ({NAMEN.get(wid, wid)}): aansluiting "
                  f"{afstand:.3f} km (>1 km, controleer volgorde/richting)")
        coords.extend(gekozen)
    return coords


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()

    print(f"extract: {EXTRACT} ({os.path.getsize(EXTRACT)/1e6:.1f} MB)")
    alle_ids = set(SEGMENT1_IDS) | set(SEGMENT2_IDS)
    ways = haal_ways(alle_ids)
    ontbrekend = alle_ids - set(ways)
    if ontbrekend:
        print(f"⚠ NIET gevonden in de extract: {sorted(ontbrekend)} "
              f"({[NAMEN.get(i, i) for i in ontbrekend]})")
        return 1
    for wid in alle_ids:
        print(f"  way {wid} ({NAMEN.get(wid, wid)}): {len(ways[wid])} punten, "
              f"{lijnlengte(ways[wid]):.2f} km")

    seg1 = stik_in_volgorde(ways, SEGMENT1_IDS)
    seg2 = list(reversed(ways[SEGMENT2_IDS[0]]))  # sumed 7 gereverseerd

    km1 = lijnlengte(seg1)
    km2 = lijnlengte(seg2)
    gat = km(seg1[-1], seg2[0])
    print(f"\nsegment 1 (sumed 1+2+3+4+5): {len(seg1)} punten, {km1:.2f} km")
    print(f"  kop  {seg1[0][1]:.5f},{seg1[0][0]:.5f}")
    print(f"  eind {seg1[-1][1]:.5f},{seg1[-1][0]:.5f}")
    print(f"segment 2 (sumed 7, gereverseerd): {len(seg2)} punten, {km2:.2f} km")
    print(f"  kop  {seg2[0][1]:.5f},{seg2[0][0]:.5f}")
    print(f"  eind {seg2[-1][1]:.5f},{seg2[-1][0]:.5f}")
    print(f"\nkaarteringsgat segment1-eind -> segment2-kop: {gat:.2f} km")
    print(f"totaal (som ways, zonder gat): {km1 + km2:.2f} km")
    print(f"totaal incl. gat: {km1 + km2 + gat:.2f} km "
          f"(tegen gepubliceerd 320 km sumed.org)")

    if args.schrijf:
        os.makedirs(BEEN, exist_ok=True)

        def schrijf(pad, coords, naam, lengte):
            doc = {
                "type": "FeatureCollection",
                "features": [{
                    "type": "Feature",
                    "properties": {
                        "naam": naam,
                        "km": round(lengte, 2),
                        "punten": len(coords),
                        "bron": "OpenStreetMap-bijdragers (ODbL), lokale "
                                "Geofabrik-extract egypte, eigen pyosmium-scan "
                                "(2026-09-28) op man_made=pipeline "
                                "substance=oil name~sumed",
                        "gereedschap": "maak_leidingbeen_olie_sumed.py",
                    },
                    "geometry": {"type": "LineString",
                                 "coordinates": [[round(x, 5), round(y, 5)] for x, y in coords]},
                }],
            }
            with open(pad, "w", encoding="utf-8") as f:
                json.dump(doc, f, ensure_ascii=False)
            print(f"geschreven: {pad} ({os.path.getsize(pad)/1024:.1f} KB)")

        schrijf(UIT1, seg1, "SUMED-hoofdleiding segment 1 (sumed 1+2+3+4+5)", km1)
        schrijf(UIT2, seg2, "SUMED-hoofdleiding segment 2 (sumed 7, gereverseerd)", km2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
