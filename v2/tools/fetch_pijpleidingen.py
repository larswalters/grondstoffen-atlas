#!/usr/bin/env python3
"""fetch_pijpleidingen.py — de SLURRY-LEIDINGEN als echte geometrie (M26.1).

Twee koperstromen in de pilot beginnen met een been dat de atlas niet kan
routeren: het concentraat verlaat Collahuasi en Escondida als slurry door een
pijpleiding, en er is geen pijpleidingnet. Dat been werd daarom als rechte
streepjeslijn getekend — eerlijk over het gát, maar onwaar over de PLAATS: de
echte leiding kronkelt door de Andes en duikt naar de kust.

Deze tool haalt de leiding uit OSM en stikt hem tot één doorlopende lijn.

⚠️ HET RESULTAAT IS TEKENGEOMETRIE, GEEN NET. Precies dezelfde keuze als bij de
bulklaag (LAR-515): geen knopen in de routeergraaf, geen ankers, geen Dijkstra
in de browser. De stroom blijft dus een GAT — je kunt er niet omheen routeren —
maar de lijn ligt wel waar de leiding ligt. Promotie tot echt net is een aparte
beslissing, net als bij de vaarwegen.

Selectie: `man_made=pipeline` MET `substance=slurry` waar OSM dat tagt (dat is
de leiding zelf, niet de water- of brandstofleiding ernaast). Zonder die tag
valt de tool terug op alle pijpleidingen in het venster en zegt dat erbij — de
redacteur oordeelt, zoals overal in dit project.

Bron: OpenStreetMap-bijdragers (ODbL).

Draaien:
  python v2/tools/fetch_pijpleidingen.py            # rapport
  python v2/tools/fetch_pijpleidingen.py --schrijf  # v2/data/pijpleidingen.json
"""

from __future__ import annotations

import argparse
import heapq
import json
import math
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))

import fetch_waterways as fw  # noqa: E402 — overpass() met schijf-cache

DATA = HIER.parent / "data"

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


# --------------------------------------------------------------------------
# de leidingen van de pilot
# --------------------------------------------------------------------------
# `van`/`naar` zijn de AANSLUITINGEN uit aansluitingen.json (mijn → kade); de
# tool zoekt het pad daartussen over de opgehaalde leiding-geometrie.

LEIDINGEN = [
    {
        "id": "cu-collahuasi-patache",
        "naam": "Collahuasi — concentraatslurry naar Puerto Patache",
        "grondstof": "copper",
        "van": (-68.66121, -20.96427),     # mijn/concentrator
        "naar": (-70.19773, -20.80503),    # Collahuasi-pier
        "gepubliceerd_km": 200,
        "noot": "OSM tagt deze leiding met substance=slurry — het is de leiding zelf.",
    },
    {
        "id": "cu-escondida-coloso",
        "naam": "Escondida — concentraatslurry naar Puerto Coloso",
        "grondstof": "copper",
        "van": (-69.07169, -24.27004),     # Rajo Escondida
        "naar": (-70.46332, -23.76015),    # Puerto Coloso
        "gepubliceerd_km": 166,
        "noot": "Rond Escondida liggen veel leidingen zonder substance-tag; let op de "
                "lengtetoets hieronder — die is hier de enige echte controle.",
    },
]

MARGE_GRAAD = 0.30      # venster om beide uiteinden heen
SNAP = 6                # decimalen waarop vertices samenvallen (~0,1 m)


def km(lon1, lat1, lon2, lat2) -> float:
    r = math.pi / 180
    d = (math.sin(lat1 * r) * math.sin(lat2 * r)
         + math.cos(lat1 * r) * math.cos(lat2 * r) * math.cos((lon2 - lon1) * r))
    return 6371.0 * math.acos(max(-1.0, min(1.0, d)))


def venster(a, b):
    la = sorted([a[1], b[1]])
    lo = sorted([a[0], b[0]])
    return (round(la[0] - MARGE_GRAAD, 4), round(lo[0] - MARGE_GRAAD, 4),
            round(la[1] + MARGE_GRAAD, 4), round(lo[1] + MARGE_GRAAD, 4))


def haal(bbox, alleen_slurry: bool):
    la0, lo0, la1, lo1 = bbox
    box = f"({la0},{lo0},{la1},{lo1})"
    clause = ('way["man_made"="pipeline"]["substance"="slurry"]' if alleen_slurry
              else 'way["man_made"="pipeline"]')
    return fw.overpass(f"[out:json][timeout:180];\n({clause}{box};);\nout geom;")


def bouw_graaf(elements):
    """Vertices op gesnapte coördinaat; edges tussen opeenvolgende punten."""
    buren = {}
    punt = {}
    ways = 0
    for el in elements:
        geom = el.get("geometry") or []
        if len(geom) < 2:
            continue
        ways += 1
        vorig = None
        for g in geom:
            sleutel = (round(g["lon"], SNAP), round(g["lat"], SNAP))
            punt[sleutel] = (g["lon"], g["lat"])
            if vorig is not None and vorig != sleutel:
                d = km(vorig[0], vorig[1], sleutel[0], sleutel[1])
                buren.setdefault(vorig, []).append((sleutel, d))
                buren.setdefault(sleutel, []).append((vorig, d))
            vorig = sleutel
    return buren, punt, ways


def dichtstbij(punt, lon, lat):
    beste, besteKm = None, float("inf")
    for s in punt:
        d = km(s[0], s[1], lon, lat)
        if d < besteKm:
            beste, besteKm = s, d
    return beste, besteKm


def kortste_pad(buren, start, doel):
    """Dijkstra; geeft (pad, km) of (None, inf) als er geen doorlopende lijn is."""
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


def verwerk(spec):
    print(f"\n{'=' * 78}\n{spec['id']} · {spec['naam']}")
    bbox = venster(spec["van"], spec["naar"])
    hemelsbreed = km(*spec["van"], *spec["naar"])
    print(f"  venster {bbox} · hemelsbreed {hemelsbreed:.1f} km · "
          f"gepubliceerd ±{spec['gepubliceerd_km']} km")

    for alleen_slurry in (True, False):
        merk = "substance=slurry" if alleen_slurry else "alle pijpleidingen"
        try:
            antwoord = haal(bbox, alleen_slurry)
        except Exception as e:  # noqa: BLE001
            print(f"  [{merk}] overpass faalde: {e}")
            continue
        buren, punt, ways = bouw_graaf(antwoord.get("elements", []))
        print(f"  [{merk}] {ways} ways · {len(punt)} vertices")
        if not punt:
            continue

        a, aKm = dichtstbij(punt, *spec["van"])
        b, bKm = dichtstbij(punt, *spec["naar"])
        pad, lengte = kortste_pad(buren, a, b)
        print(f"     mijn-uiteinde op {aKm:.1f} km · kade-uiteinde op {bKm:.1f} km")
        if pad is None:
            print("     ⚠️ geen doorlopende leiding tussen die twee uiteinden")
            continue

        afwijking = (lengte - spec["gepubliceerd_km"]) / spec["gepubliceerd_km"] * 100
        print(f"     ✅ pad: {len(pad)} punten · {lengte:.1f} km "
              f"({afwijking:+.1f}% t.o.v. gepubliceerd)")
        return {
            "id": spec["id"], "naam": spec["naam"], "grondstof": spec["grondstof"],
            "km": round(lengte, 2),
            "gepubliceerdKm": spec["gepubliceerd_km"],
            "afwijkingPct": round(afwijking, 1),
            "aanloopKm": [round(aKm, 2), round(bKm, 2)],
            "selectie": merk,
            "punten": [[round(punt[s][0], 5), round(punt[s][1], 5)] for s in pad],
            "bron": "OpenStreetMap-bijdragers (ODbL) — man_made=pipeline",
            "noot": spec["noot"],
        }
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()

    uit = []
    for spec in LEIDINGEN:
        r = verwerk(spec)
        if r:
            uit.append(r)

    print(f"\n{len(uit)}/{len(LEIDINGEN)} leidingen gestikt")
    if not uit:
        return 1
    doc = {
        "versie": 1,
        "toelichting": (
            "Slurry-pijpleidingen als TEKENGEOMETRIE, niet als net. De benen die "
            "hierop steunen blijven een gat in de keten (niet herrouteerbaar); wat "
            "verandert is dat de lijn ligt waar de leiding ligt in plaats van "
            "kaarsrecht. Zelfde rolverdeling als de bulklaag (LAR-515)."
        ),
        "bron": "OpenStreetMap-bijdragers (ODbL)",
        "leidingen": uit,
    }
    if args.schrijf:
        pad = DATA / "pijpleidingen.json"
        pad.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"geschreven: {pad} ({pad.stat().st_size / 1024:.1f} KB)")
    else:
        print("(niets geschreven — geef --schrijf mee)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
