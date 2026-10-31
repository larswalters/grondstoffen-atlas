#!/usr/bin/env python3
"""maak_leidingbeen_olie_uzen_samara.py — de leidingbenen b1 en b2 van olie-uzen-samara.

De routebrief (v2/design/routebrieven/olie-uzen-samara.md) legt de Uzen-Atyrau-Samara-hoofdleiding
(KazTransOil / Transneft) vast als twee OSM-ways `man_made=pipeline substance=oil`:
  b1  way 274735631  "Узень - Атырау"   Uzen (43.3586,52.8259) -> Atyrau (47.1752,51.8724)   401 knopen
  b2  way 274735055  "Атырау - Самара"  Atyrau (47.1650,51.8729) -> Samara-knoop (52.9910,50.5372)  161 knopen
De twee ways sluiten niet op een gedeelde node aan (naad ~1,1 km bij Atyrau); beide worden recht
gestikt op het reeds gelegde Atyrau/PS-1-anker (47.1683,51.8731, olie-tengiz-novorossiysk) zodat de
twee benen elkaar op 0 m raken. Die twee korte stukken (~0,8 en ~0,4 km) zijn GEEN OSM-geometrie.

Geometrie komt per way-id uit de OSM-API (api.openstreetmap.org, ODbL), met cache op schijf
(pyosmium is op deze machine geblokkeerd, Overpass onbereikbaar).
Uitvoer (v2/build-cache/ais/graaf/): olie-uzen-samara-leiding-uzen-atyrau.geojson en
olie-uzen-samara-leiding-atyrau-samara.geojson (FeatureCollection met een LineString, [lon, lat]).

Draaien:   python v2/tools/maak_leidingbeen_olie_uzen_samara.py --schrijf
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import urllib.request

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
PREFIX = "olie-uzen-samara"
CACHE = os.path.join(BEEN, PREFIX + "-osmapi-cache.json")
UA = "grondstoffen-atlas/1.0 (route research; OSM API, ODbL)"

WAY_B1 = 274735631      # Узень - Атырау, KR-6, KazTransOil, 1016 mm
WAY_B2 = 274735055      # Атырау - Самара, KazTransOil, 1016 mm
ANKER_ATYRAU = (47.1683, 51.8731)   # olie-tengiz-novorossiysk, ol-atyrau-ps1 (hergebruik)

R = 6371.0088


def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def lengte(p):
    return sum(hav(p[i], p[i + 1]) for i in range(len(p) - 1))


def _get(url):
    err = None
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return json.load(urllib.request.urlopen(req, timeout=90))
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(3 * (i + 1))
    raise err


def laad(ids):
    c = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {"ways": {}, "nodes": {}}
    nodig = [i for i in ids if str(i) not in c["ways"]]
    for i in nodig:
        d = _get(f"https://api.openstreetmap.org/api/0.6/way/{i}/full.json")
        for e in d["elements"]:
            if e["type"] == "node":
                c["nodes"][str(e["id"])] = [e["lat"], e["lon"]]
            elif e["type"] == "way":
                c["ways"][str(e["id"])] = {"nodes": e["nodes"], "tags": e.get("tags", {})}
    os.makedirs(BEEN, exist_ok=True)
    json.dump(c, open(CACHE, "w", encoding="utf-8"))
    return c


def punten(c, way):
    return [tuple(c["nodes"][str(n)]) for n in c["ways"][str(way)]["nodes"]]


def schrijf(naam, pts, bron, uit):
    coords = [[round(p[1], 5), round(p[0], 5)] for p in pts]
    sch = [coords[0]]
    for q in coords[1:]:
        if q != sch[-1]:
            sch.append(q)
    km = lengte([(q[1], q[0]) for q in sch])
    doc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"naam": naam, "km": round(km, 2), "punten": len(sch), "bron": bron,
                       "gereedschap": "maak_leidingbeen_olie_uzen_samara.py"},
        "geometry": {"type": "LineString", "coordinates": sch}}]}
    json.dump(doc, open(uit, "w", encoding="utf-8"), ensure_ascii=False)
    return km, len(sch), os.path.getsize(uit) / 1024


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true", help="geojsons wegschrijven (anders alleen rapport)")
    args = ap.parse_args()
    c = laad([WAY_B1, WAY_B2])
    p1 = punten(c, WAY_B1)
    p2 = punten(c, WAY_B2)
    assert hav(p1[-1], ANKER_ATYRAU) < 2 and hav(p2[0], ANKER_ATYRAU) < 2, "ways liggen niet bij het Atyrau-anker"
    b1 = p1 + [ANKER_ATYRAU]
    b2 = [ANKER_ATYRAU] + p2
    bron = ("OpenStreetMap-bijdragers (ODbL), OSM-API way-geometrie, man_made=pipeline substance=oil "
            "(KazTransOil), way 274735631 resp. 274735055; slotstuk naar het Atyrau/PS-1-anker recht gestikt")
    res = {
        "uzen-atyrau": (b1, "Uzen-Atyrau-Samara-leiding, deel Uzen - Atyrau (KazTransOil, OSM way 274735631)"),
        "atyrau-samara": (b2, "Uzen-Atyrau-Samara-leiding, deel Atyrau - Samara (KazTransOil/Transneft, OSM way 274735055)"),
    }
    for naam, (pts, titel) in res.items():
        print(f"{naam}: {len(pts)} punten, {lengte(pts):.1f} km, "
              f"{pts[0][0]:.4f},{pts[0][1]:.4f} -> {pts[-1][0]:.4f},{pts[-1][1]:.4f}")
        if args.schrijf:
            uit = os.path.join(BEEN, f"{PREFIX}-leiding-{naam}.geojson")
            km, n, kb = schrijf(titel, pts, bron, uit)
            print(f"   geschreven {uit} ({km:.2f} km, {n} punten, {kb:.1f} KB)")
    print(f"OSM-naad way1-eind -> way2-begin: {hav(p1[-1], p2[0]) * 1000:.0f} m; "
          f"gestikt via anker: {hav(p1[-1], ANKER_ATYRAU) * 1000:.0f} + {hav(ANKER_ATYRAU, p2[0]) * 1000:.0f} m")
    print(f"naad b1->b2: {hav(b1[-1], b2[0]) * 1000:.1f} m")
    return 0


if __name__ == "__main__":
    sys.exit(main())
