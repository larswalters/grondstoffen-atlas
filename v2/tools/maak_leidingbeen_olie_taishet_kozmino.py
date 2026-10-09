#!/usr/bin/env python3
"""maak_leidingbeen_olie_taishet_kozmino.py — de leidingbenen b1 en b2 van olie-taishet-kozmino.

WAAROM DIT BESTAAT. De routebrief (v2/design/routebrieven/olie-taishet-kozmino.md) legt de
ESPO-leiding (ВСТО, Transneft) vast als OSM `man_made=pipeline substance=oil`-ways:
  b1  ESPO-1  Taishet -> Skovorodino-knoop      15 ways, verwacht 2679,7 km
  b2  ESPO-2  Skovorodino -> Perevoznaya        9 ways,  verwacht 2042,9 km
pyosmium is op deze machine geblokkeerd en Overpass onbereikbaar; de geometrie komt dus per way-id uit
de OSM-API (api.openstreetmap.org/api/0.6/ways + /nodes, ODbL), met cache op schijf. De way-volgorde
staat hieronder VAST (geen vrij kortste pad): zo blijven de Komsomolsk-aftakking, de China-spur en
andere ВСТО-ways buiten de lijn. Ways worden gestikt op GEDEELDE OSM-NODES (naad 0 m).

Uitvoer (v2/build-cache/ais/graaf/): olie-taishet-kozmino-leiding-b1.geojson, -b2.geojson
(FeatureCollection met één LineString, coordinates [lon, lat]).
Cache: olie-taishet-kozmino-osmapi-cache.json ({"ways": {...}, "nodes": {...}}).

Draaien:   python v2/tools/maak_leidingbeen_olie_taishet_kozmino.py --schrijf
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
PREFIX = "olie-taishet-kozmino"
CACHE = os.path.join(BEEN, PREFIX + "-osmapi-cache.json")
UA = "grondstoffen-atlas/1.0 (route research; OSM API, ODbL)"

B1 = [290897778, 290891540, 290891539, 290891538, 291166093, 290820311, 291194263, 290912026,
      290912027, 506714839, 506714841, 361384623, 290912028, 271667289, 226953167]
B2 = [174814639, 142436390, 1035963742, 238838736, 1035963741, 578805782, 578805780, 578805781,
      238914784]
B1_BEGIN = 2943913955   # Taishet-NPS, 55.8896, 98.0346
KNOOP = 2794125345      # Skovorodino-knoop, 53.9471, 124.2622
B2_EIND = 2467291581    # Perevoznaya, 42.8068, 133.0972

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
    for k in range(0, len(nodig), 100):
        d = _get("https://api.openstreetmap.org/api/0.6/ways.json?ways=" + ",".join(map(str, nodig[k:k + 100])))
        for e in d["elements"]:
            c["ways"][str(e["id"])] = {"nodes": e["nodes"], "tags": e.get("tags", {})}
    nn = sorted({n for i in ids for n in c["ways"][str(i)]["nodes"] if str(n) not in c["nodes"]})
    for k in range(0, len(nn), 700):
        d = _get("https://api.openstreetmap.org/api/0.6/nodes.json?nodes=" + ",".join(map(str, nn[k:k + 700])))
        for e in d["elements"]:
            c["nodes"][str(e["id"])] = [e["lat"], e["lon"]]
    os.makedirs(BEEN, exist_ok=True)
    json.dump(c, open(CACHE, "w", encoding="utf-8"))
    return c


def stik(c, ids, begin_node):
    """Stik ways op gedeelde nodes, begin bij begin_node; geeft nodeketen."""
    keten = None
    for i in ids:
        nd = list(c["ways"][str(i)]["nodes"])
        if keten is None:
            if nd[0] == begin_node:
                pass
            elif nd[-1] == begin_node:
                nd.reverse()
            else:
                raise SystemExit(f"way {i} begint niet op begin_node {begin_node}")
            keten = nd
            continue
        eind = keten[-1]
        if nd[0] == eind:
            pass
        elif nd[-1] == eind:
            nd.reverse()
        else:
            raise SystemExit(f"way {i} sluit niet aan op een gedeelde node (eindnode {eind}) - stik-fout")
        keten += nd[1:]
    return keten


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
                       "gereedschap": "maak_leidingbeen_olie_taishet_kozmino.py"},
        "geometry": {"type": "LineString", "coordinates": sch}}]}
    json.dump(doc, open(uit, "w", encoding="utf-8"), ensure_ascii=False)
    return km, len(sch), os.path.getsize(uit) / 1024


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true", help="geojsons wegschrijven (anders alleen rapport)")
    args = ap.parse_args()
    c = laad(sorted(set(B1 + B2)))
    bron = ("OpenStreetMap-bijdragers (ODbL), OSM-API way-geometrie, man_made=pipeline substance=oil "
            "(ВСТО, Transneft), gestikt op gedeelde nodes")
    k1 = stik(c, B1, B1_BEGIN)
    assert k1[-1] == KNOOP, f"b1 eindigt op {k1[-1]}, verwacht {KNOOP}"
    k2 = stik(c, B2, KNOOP)
    assert k2[-1] == B2_EIND, f"b2 eindigt op {k2[-1]}, verwacht {B2_EIND}"
    res = {
        "b1": ([tuple(c["nodes"][str(n)]) for n in k1], "ESPO-1 Taishet → Skovorodino (Transneft, OSM-leiding)"),
        "b2": ([tuple(c["nodes"][str(n)]) for n in k2], "ESPO-2 Skovorodino → Perevoznaya (Transneft, OSM-leiding)"),
    }
    for naam in ("b1", "b2"):
        pts, titel = res[naam]
        print(f"{naam}: {len(pts)} punten, {lengte(pts):.1f} km, {pts[0][0]:.4f},{pts[0][1]:.4f} -> {pts[-1][0]:.4f},{pts[-1][1]:.4f}")
        if args.schrijf:
            uit = os.path.join(BEEN, f"{PREFIX}-leiding-{naam}.geojson")
            km, n, kb = schrijf(titel, pts, bron, uit)
            print(f"   geschreven {uit} ({km:.2f} km, {n} punten, {kb:.1f} KB)")
    print(f"naad b1->b2: {hav(res['b1'][0][-1], res['b2'][0][0]) * 1000:.1f} m")
    return 0


if __name__ == "__main__":
    sys.exit(main())
