#!/usr/bin/env python3
"""maak_rivierbeen.py — een rivierbeen als TEKENGEOMETRIE uit de MARNET-bulklaag.

── WAAROM DIT BESTAAT ─────────────────────────────────────────────────────
M28 zegt: open zee = MARNET, binnenwater = echte AIS-tracks. Dat werkt voor de
Mississippi en de Rijn, want daar liggen tracks. Voor de **Yangtze** liggen ze
er niet — gemeten: Tongling 0 berichten in de dekkingstest, en de Chinese kust
levert alleen Korea/Japan/Taiwan (LAR-528). Een rivierbeen Shanghai → Tongling
kan dus niet uit tracks komen.

Wat er wél ligt is de **bulklaag** van LAR-515: 407.870 km mechanisch gefilterde
rivier- en kanaalgeometrie, bewust als PURE TEKENGEOMETRIE en bewust BUITEN de
routeergraaf (`marnet_zee()` filtert hem er expliciet uit, want anders vaart een
zeeschip door sluizen — de Donau-ring-fout).

Deze tool gebruikt die laag waarvoor hij bedoeld is: hij zoekt één keer het
kortste waterpad tussen twee punten OVER de bulklaag en schrijft dat weg als
GeoJSON. Dat bestand gaat daarna als `--been-geojson` in `hecht_marnet.py route`
— een been van echte riviergeometrie, zonder dat de router ooit een rivier-edge
te zien krijgt.

⚠️ WAAROM DIT GEEN "DE BULKLAAG ROUTEERBAAR MAKEN" IS, en dat onderscheid is de
hele veiligheid van deze aanpak: het pad wordt hier gezocht, één keer, tussen
twee met de hand aangewezen punten, en het resultaat is een lijst coördinaten.
De routeergraaf van `hecht_marnet route` blijft per constructie ongewijzigd; er
is geen enkele run waarin een zeeroute stilletjes een rivier-sluipweg kan
nemen. Zelfde rolverdeling als `maak_stroombeen_weg.py` (dat doet dit voor het
wegennet) en `toets_spoorroute.mjs` (voor het spoor).

⚠️ WAT DIT BEEN NIET IS: een bewijs dat een schip daar past. De bulklaag draagt
geen gabariet en is mechanisch gefilterd, dus dit is de LIGGING van het water,
niet de bevaarbaarheid ervan. Voor de Yangtze onder Nanjing is dat onschuldig
(zeeschepen komen tot Nanjing, binnenvaart tot Chongqing — beide gedocumenteerd);
gebruik het niet om een nieuwe corridor "aan te tonen".

Draaien:
  python v2/tools/maak_rivierbeen.py --marnet v2/build-cache/marnet-preais \\
      --van 31.51,121.4187 --naar 30.98656,117.7718 \\
      --uit v2/build-cache/ais/graaf/rivierbeen-shanghai-tongling.geojson
"""

from __future__ import annotations

import argparse
import heapq
import json
import math
import sys
from pathlib import Path

import numpy as np

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))

import hecht_marnet as hm  # noqa: E402 — lees_marnet hergebruiken

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

R_AARDE = 6371.0


def bulk_masker(m):
    """De edges die tot de BULKLAAG horen — precies het complement van wat
    `marnet_zee()` overhoudt. Uit `meta.vaarwegen[*].bulk`, dezelfde bron."""
    meta = m["meta"]
    bulk = np.zeros(len(m["edge_km"]), bool)
    for v in (meta.get("vaarwegen") or {}).values():
        if v.get("bulk"):
            for e in v.get("edges", ()):
                if e < len(bulk):
                    bulk[e] = True
    return bulk


def dichtstbij(lon, lat, knoop_lon, knoop_lat, toegestaan):
    la, lo = math.radians(lat), math.radians(lon)
    v = np.array([math.cos(la) * math.cos(lo), math.sin(la),
                  math.cos(la) * math.sin(lo)])
    kla, klo = np.radians(knoop_lat), np.radians(knoop_lon)
    vec = np.stack([np.cos(kla) * np.cos(klo), np.sin(kla),
                    np.cos(kla) * np.sin(klo)], axis=1)
    dots = vec @ v
    dots[~toegestaan] = -2.0
    k = int(np.argmax(dots))
    return k, R_AARDE * math.acos(float(np.clip(dots[k], -1.0, 1.0)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--marnet", required=True)
    ap.add_argument("--van", required=True, help="LAT,LON")
    ap.add_argument("--naar", required=True, help="LAT,LON")
    ap.add_argument("--uit", required=True)
    ap.add_argument("--naam", default="rivierbeen")
    args = ap.parse_args()

    m = hm.lees_marnet(args.marnet)
    bulk = bulk_masker(m)
    e_a, e_b, e_km = m["edge_a"], m["edge_b"], m["edge_km"]
    knoop_lon, knoop_lat = m["knoop_lon"], m["knoop_lat"]
    print(f"bulklaag: {int(bulk.sum()):,} van {len(bulk):,} edges · "
          f"{e_km[bulk].sum():,.0f} km")

    # buren alléén over bulk-edges
    buren = {}
    for i in np.flatnonzero(bulk):
        a, b, km = int(e_a[i]), int(e_b[i]), float(e_km[i])
        buren.setdefault(a, []).append((b, km, i, False))
        buren.setdefault(b, []).append((a, km, i, True))
    op_bulk = np.zeros(len(knoop_lon), bool)
    op_bulk[list(buren.keys())] = True

    la_a, lo_a = (float(x) for x in args.van.split(","))
    la_b, lo_b = (float(x) for x in args.naar.split(","))
    ka, da = dichtstbij(lo_a, la_a, knoop_lon, knoop_lat, op_bulk)
    kb, db = dichtstbij(lo_b, la_b, knoop_lon, knoop_lat, op_bulk)
    print(f"van  ({la_a}, {lo_a}): bulk-knoop {ka} op {da:.2f} km")
    print(f"naar ({la_b}, {lo_b}): bulk-knoop {kb} op {db:.2f} km")

    # Dijkstra over de bulklaag
    dist = {ka: 0.0}
    vorig = {}
    pq = [(0.0, ka)]
    while pq:
        d, k = heapq.heappop(pq)
        if d > dist.get(k, math.inf):
            continue
        if k == kb:
            break
        for buur, km, ei, omgekeerd in buren.get(k, ()):
            nd = d + km
            if nd < dist.get(buur, math.inf):
                dist[buur] = nd
                vorig[buur] = (k, ei, omgekeerd)
                heapq.heappush(pq, (nd, buur))
    if kb not in dist:
        sys.exit("GEEN WATERPAD over de bulklaag tussen deze twee punten — "
                 "de rivier valt daar in losse componenten uiteen (LAR-520-klasse). "
                 "Niet dichttrekken met geleende geometrie; splits het been en "
                 "stippel het gat mét reden (werkwijze §7).")

    # pad terugbouwen en de EDGE-GEOMETRIE volgen (niet knoop-naar-knoop: dan
    # verlies je elke meander — dezelfde les als in route_geometrie_comb)
    keten = []
    k = kb
    while k != ka:
        p, ei, omgekeerd = vorig[k]
        keten.append((ei, omgekeerd))
        k = p
    keten.reverse()

    punten = []
    km_tot = 0.0
    g_lon, g_lat, g_start = m["geom_lon"], m["geom_lat"], m["geom_start"]
    for ei, omgekeerd in keten:
        i0, i1 = int(g_start[ei]), int(g_start[ei + 1])
        g = list(zip(g_lon[i0:i1].tolist(), g_lat[i0:i1].tolist()))
        rij = list(reversed(g)) if omgekeerd else list(g)
        if punten and rij and punten[-1] == rij[0]:
            rij = rij[1:]
        punten.extend(rij)
        km_tot += float(e_km[ei])

    uit = Path(args.uit)
    uit.parent.mkdir(parents=True, exist_ok=True)
    uit.write_text(json.dumps({
        "type": "FeatureCollection",
        "bron": "MARNET-bulklaag (LAR-515) — tekengeometrie, geen routeergraaf",
        "features": [{
            "type": "Feature",
            "properties": {"naam": args.naam, "km": round(km_tot, 1),
                           "edges": len(keten)},
            "geometry": {"type": "LineString",
                         "coordinates": [[round(lo, 5), round(la, 5)]
                                         for lo, la in punten]},
        }],
    }, ensure_ascii=False), encoding="utf-8")
    print(f"pad: {km_tot:,.1f} km over {len(keten)} edges · "
          f"{len(punten):,} punten")
    print(f"geschreven: {uit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
