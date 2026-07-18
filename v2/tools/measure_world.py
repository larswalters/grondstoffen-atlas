#!/usr/bin/env python3
"""
measure_world.py — meet hoe fijn de beschikbare wereldmodellen zijn.

Waarom dit bestaat: de atlas kende drie wereldmodellen die het niet eens waren
(satellietbeeld, LAND_POLYS op 1:50M, MARNET's kustlijn) en daardoor werd er
langs elkaar heen gemeten. Voor we de vectorwereld bakken, leggen we objectief
vast wat elk model kan: puntafstand, aantal vormen, en resolutie op de plekken
waar het eerder misging (Japan, Baja, Malakka).

Draaien:  python v2/tools/measure_world.py
"""

import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)
CACHE = os.path.join(V2, "build-cache")

# De plekken waar de oude routelaag structureel de fout in ging.
PROBLEEMPLEKKEN = {
    "Japan (Kanmon/Seto)":      (33.95, 130.95, 2.0),
    "Baja California":          (27.50, -114.50, 3.0),
    "Straat van Malakka":       (2.50, 101.00, 3.0),
    "Straat van Hormuz":        (26.57, 56.25, 1.5),
    "Panamakanaal":             (9.10, -79.70, 1.5),
    "Gibraltar":                (35.95, -5.60, 1.5),
}


def haversine_km(lon1, lat1, lon2, lat2):
    R = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = p2 - p1
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))


def iter_ringen(geojson):
    """Alle ringen (buiten- en binnenringen) uit een GeoJSON met (Multi)Polygon."""
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


def meet(naam, ringen):
    afstanden = []
    punten = 0
    vormen = 0
    for ring in ringen:
        vormen += 1
        punten += len(ring)
        for i in range(len(ring) - 1):
            lon1, lat1 = ring[i][0], ring[i][1]
            lon2, lat2 = ring[i + 1][0], ring[i + 1][1]
            afstanden.append(haversine_km(lon1, lat1, lon2, lat2))

    afstanden.sort()
    n = len(afstanden)

    def pct(p):
        return afstanden[min(n - 1, int(n * p))] if n else 0.0

    print(f"\n--- {naam} ---")
    print(f"  vormen (ringen) : {vormen:,}")
    print(f"  punten          : {punten:,}")
    print(f"  segmenten       : {n:,}")
    print(f"  puntafstand km  : mediaan {pct(0.5):8.3f} | p90 {pct(0.9):8.3f} "
          f"| p99 {pct(0.99):8.3f} | max {afstanden[-1] if n else 0:8.1f}")
    return {"vormen": vormen, "punten": punten, "mediaan_km": pct(0.5)}


def meet_gebied(naam, ringen, lat0, lon0, straal_deg):
    """Hoeveel detail zit er rond één probleemplek?"""
    punten = 0
    afstanden = []
    for ring in ringen:
        vorig = None
        for lon, lat in ((p[0], p[1]) for p in ring):
            binnen = (abs(lat - lat0) <= straal_deg and
                      abs(((lon - lon0 + 180) % 360) - 180) <= straal_deg)
            if binnen:
                punten += 1
                if vorig is not None:
                    afstanden.append(haversine_km(vorig[0], vorig[1], lon, lat))
                vorig = (lon, lat)
            else:
                vorig = None
    afstanden.sort()
    med = afstanden[len(afstanden) // 2] if afstanden else float("nan")
    return punten, med


def laad(pad):
    with open(pad, "r", encoding="utf-8") as f:
        return json.load(f)


def laad_land_polys_uit_v1():
    """LAND_POLYS uit de v1 geo-data.js (1:50M) — puur lezen, niet wijzigen."""
    pad = os.path.join(os.path.dirname(V2), "geo-data.js")
    with open(pad, "r", encoding="utf-8") as f:
        tekst = f.read()
    start = tekst.index("const LAND_POLYS = ") + len("const LAND_POLYS = ")
    eind = tekst.index("\n", start)
    while tekst[eind - 1] != ";":
        eind = tekst.index("\n", eind + 1)
    return json.loads(tekst[start:eind - 1])


def main():
    print("=" * 68)
    print("WERELDMODELLEN — meting", )
    print("=" * 68)

    modellen = {}

    # 1:50M (wat de atlas nu gebruikt)
    try:
        v1 = laad_land_polys_uit_v1()
        ringen_50m = [ring for poly in v1 for ring in poly]
        modellen["1:50M (v1 LAND_POLYS)"] = meet("1:50M — v1 LAND_POLYS", ringen_50m)
    except Exception as e:
        print(f"  [!] 1:50M niet gelezen: {e}")
        ringen_50m = []

    # 1:10M (de kandidaat-waarheid)
    pad10 = os.path.join(CACHE, "ne_10m_land.geojson")
    if not os.path.exists(pad10):
        print(f"\n[!] {pad10} ontbreekt — draai eerst de download.")
        sys.exit(1)
    gj10 = laad(pad10)
    ringen_10m = list(iter_ringen(gj10))
    modellen["1:10M (Natural Earth)"] = meet("1:10M — Natural Earth land", ringen_10m)

    pad_isl = os.path.join(CACHE, "ne_10m_minor_islands.geojson")
    ringen_isl = []
    if os.path.exists(pad_isl):
        ringen_isl = list(iter_ringen(laad(pad_isl)))
        meet("1:10M — kleine eilanden (apart bestand)", ringen_isl)

    # Per probleemplek: hoeveel detail wint 1:10M?
    print("\n" + "=" * 68)
    print("DETAIL PER PROBLEEMPLEK (punten in het gebied / mediane puntafstand)")
    print("=" * 68)
    print(f"{'plek':<26} {'1:50M':>18} {'1:10M':>18}   winst")
    for naam, (lat, lon, straal) in PROBLEEMPLEKKEN.items():
        p50, m50 = meet_gebied(naam, ringen_50m, lat, lon, straal) if ringen_50m else (0, float("nan"))
        p10, m10 = meet_gebied(naam, ringen_10m + ringen_isl, lat, lon, straal)
        winst = (p10 / p50) if p50 else float("inf")
        print(f"{naam:<26} {p50:>7,} pt {m50:>6.1f}km {p10:>7,} pt {m10:>6.1f}km   {winst:>5.1f}x")

    # Wat betekent dit t.o.v. de satelliettextuur?
    print("\n" + "=" * 68)
    print("TER VERGELIJKING — de satelliettextuur")
    print("=" * 68)
    for tex in (4096, 8192, 16384):
        km_per_px = 40075.0 / tex
        print(f"  {tex:>5}px breed  ->  {km_per_px:6.2f} km per pixel op de evenaar")
    print("  (een vectorlijn heeft geen pixelgrootte: die blijft op elke zoom scherp)")


if __name__ == "__main__":
    main()
