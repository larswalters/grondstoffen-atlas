#!/usr/bin/env python3
"""
bake_world.py — bakt Natural Earth 1:10M om tot een compact binair wereldmodel.

Waarom niet gewoon de GeoJSON verschepen: dat is 11,5 MB voor land + eilanden.
Hier gaat het naar ~1,5 MB door drie stappen:

  1. quantiseren   lon/lat naar een raster van 1e-4 graden (~11 m). De mediane
                   puntafstand is 1,5 km, dus 11 m verliest geen enkel detail
                   dat je ooit ziet.
  2. delta-coderen  we slaan per ring het VERSCHIL met het vorige punt op. Die
                   verschillen zijn klein (mediaan ~1,5 km = ~135 eenheden).
  3. varint+zigzag  kleine getallen kosten 1-2 bytes i.p.v. 4.

Uitvoer:
  data/world-10m.bin   de punten
  data/world-10m.json  de index (waar begint/eindigt elke ring)

Draaien:  python v2/tools/bake_world.py
"""

import json
import os
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)
CACHE = os.path.join(V2, "build-cache")
DATA = os.path.join(V2, "data")

SCHAAL = 10000  # 1e-4 graden per eenheid (~11 m op de evenaar)

BRONNEN = [
    ("land", "ne_10m_land.geojson"),
    ("eilanden", "ne_10m_minor_islands.geojson"),
]


def varint(uit, waarde):
    """Zigzag + varint: kleine (ook negatieve) getallen worden 1 byte."""
    zz = (waarde << 1) ^ (waarde >> 31)  # zigzag, werkt op Python-ints
    zz &= 0xFFFFFFFF
    while True:
        byte = zz & 0x7F
        zz >>= 7
        if zz:
            uit.append(byte | 0x80)
        else:
            uit.append(byte)
            break


def iter_ringen(geojson):
    for feat in geojson["features"]:
        geom = feat.get("geometry") or {}
        t = geom.get("type")
        if t == "Polygon":
            for ring in geom["coordinates"]:
                yield ring
        elif t == "MultiPolygon":
            for poly in geom["coordinates"]:
                for ring in poly:
                    yield ring


def main():
    os.makedirs(DATA, exist_ok=True)

    bytes_uit = bytearray()
    ringen_index = []  # [byte-offset, aantal punten] per ring
    totaal_punten = 0
    weggegooid = 0

    for label, bestand in BRONNEN:
        pad = os.path.join(CACHE, bestand)
        if not os.path.exists(pad):
            print(f"[!] ontbreekt: {pad}")
            continue

        with open(pad, "r", encoding="utf-8") as f:
            gj = json.load(f)

        n_ringen = 0
        for ring in iter_ringen(gj):
            # Quantiseren, en direct dubbele punten eruit die door het
            # quantiseren op elkaar vallen (anders krijg je nul-lengte lijnen).
            punten = []
            vorige = None
            for p in ring:
                x = int(round(p[0] * SCHAAL))
                y = int(round(p[1] * SCHAAL))
                if (x, y) != vorige:
                    punten.append((x, y))
                    vorige = (x, y)
                else:
                    weggegooid += 1

            if len(punten) < 3:
                continue  # geen zinnige vorm meer over

            start = len(bytes_uit)
            px, py = 0, 0
            for x, y in punten:
                varint(bytes_uit, x - px)
                varint(bytes_uit, y - py)
                px, py = x, y

            ringen_index.append([start, len(punten)])
            totaal_punten += len(punten)
            n_ringen += 1

        print(f"  {label:<10} {n_ringen:>6,} ringen")

    bin_pad = os.path.join(DATA, "world-10m.bin")
    with open(bin_pad, "wb") as f:
        f.write(bytes_uit)

    meta = {
        "schaal": SCHAAL,
        "punten": totaal_punten,
        "ringen": len(ringen_index),
        "bron": "Natural Earth 1:10M (land + minor islands), publiek domein",
        "index": ringen_index,
    }
    json_pad = os.path.join(DATA, "world-10m.json")
    with open(json_pad, "w", encoding="utf-8") as f:
        json.dump(meta, f, separators=(",", ":"))

    bin_kb = os.path.getsize(bin_pad) / 1024
    json_kb = os.path.getsize(json_pad) / 1024
    print(f"\n  ringen        : {len(ringen_index):,}")
    print(f"  punten        : {totaal_punten:,}  (dubbelen weg: {weggegooid:,})")
    print(f"  world-10m.bin : {bin_kb:,.0f} KB  ({bin_kb * 1024 / totaal_punten:.2f} byte/punt)")
    print(f"  world-10m.json: {json_kb:,.0f} KB")
    print(f"  samen         : {(bin_kb + json_kb) / 1024:.2f} MB   (was 11,5 MB ruw)")


if __name__ == "__main__":
    main()
