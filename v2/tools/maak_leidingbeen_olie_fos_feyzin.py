#!/usr/bin/env python3
"""maak_leidingbeen_olie_fos_feyzin.py - de leidingbenen van olie-fos-feyzin.

SPSE (Pipeline Sud-Europeen), Fos-sur-Mer -> Lyon -> Feyzin, gestikt uit OSM-ways (man_made=pipeline, substance=oil)
uit de lokale Geofabrik-extracts fr-provence-alpes-cote-d-azur en fr-rhone-alpes (pyosmium, locations=True).
Drie doorgetrokken stukken; de twee gaten tussen die stukken worden in bak_stromen.sh stippels (zie brief):
  A  420942590 (omgekeerd, van het SPSE-tankenpark Fos) + 232593022 vanaf de knoop 43.4987628,4.8931793
     (de eerste 5 vertices van 232593022 zijn een zijtak naar het logistiek park en worden niet gebruikt)
     -> 43.7942,4.8946                                    [gat 1: 10,8 km bij de Rhone-kruising]
  B  232593024 + 514120690 + 232717968 + 457397239 + 457397240 (tot de Lyon-aflevering) + 0,3 km recht
     + TRC HC 16" 1328508024 (Lyon-aflevering -> 45.6477,4.9157)   [gat 2: 4,7 km, aftak niet in OSM]
  C  232080899 (45.6604,4.8592 -> 45.6625,4.8430, eind in de raffinaderij Feyzin)
Uitvoer (v2/build-cache/ais/graaf/): olie-fos-feyzin-leiding-a/b/c.geojson (FeatureCollection, 1 LineString, [lon,lat]).
Draaien: PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_olie_fos_feyzin.py --schrijf
"""
import argparse
import json
import math
import os
import sys

import osmium

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEO = os.path.join(WORTEL, "build-cache", "geofabrik")
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
PREFIX = "olie-fos-feyzin"
CACHE = os.path.join(BEEN, PREFIX + "-osm-cache.json")
R = 6371.0088
REGIOS = {
    "fr-provence-alpes-cote-d-azur": {420942590, 232593022, 232593024},
    "fr-rhone-alpes": {232593024, 514120690, 232717968, 457397239, 457397240, 1328508024, 232080899},
}
JOIN_A = (43.4987628, 4.8931793)   # gedeelde knoop tussen 420942590 en 232593022
TRC_START = (45.6158948, 5.1144415)  # begin TRC HC 16" bij de Lyon-aflevering
MAX_NAAD_KM = 0.5


def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def lengte(p):
    return sum(hav(p[i], p[i + 1]) for i in range(len(p) - 1))


class Scan(osmium.SimpleHandler):
    def __init__(self, ids):
        super().__init__()
        self.ids, self.w = ids, {}

    def way(self, w):
        if w.id in self.ids:
            self.w[str(w.id)] = {"tags": dict(w.tags), "c": [(n.lat, n.lon) for n in w.nodes]}


def laad():
    if os.path.exists(CACHE):
        return json.load(open(CACHE, encoding="utf-8"))
    out = {}
    for regio, ids in REGIOS.items():
        s = Scan(ids)
        s.apply_file(os.path.join(GEO, regio + "-latest.osm.pbf"), locations=True)
        out.update(s.w)
        print(regio, len(s.w), "ways", flush=True)
    os.makedirs(BEEN, exist_ok=True)
    json.dump(out, open(CACHE, "w", encoding="utf-8"))
    return out


def oriënteer(c, begin):
    """Draai de way zodat hij bij `begin` begint (dichtstbijzijnde uiteinde)."""
    return c if hav(c[0], begin) <= hav(c[-1], begin) else c[::-1]


def stik(delen, naden):
    pts = list(delen[0])
    for d in delen[1:]:
        g = hav(pts[-1], d[0])
        if g > MAX_NAAD_KM:
            raise SystemExit(f"naad {g:.3f} km > {MAX_NAAD_KM} km bij {d[0]}")
        if g > 1e-6:
            naden.append(g * 1000)
        else:
            d = d[1:]
        pts.extend(d)
    return pts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()
    W = laad()
    naden = []
    # A
    w1 = oriënteer(W["420942590"]["c"], (43.4649374, 4.9164876))
    w2 = W["232593022"]["c"]
    k = min(range(len(w2)), key=lambda i: hav(w2[i], JOIN_A))
    assert hav(w2[k], JOIN_A) < 0.001, "joinknoop niet gevonden"
    A = stik([w1, w2[k:]], naden)
    # B
    w3 = oriënteer(W["232593024"]["c"], (43.8894, 4.9229))
    w4 = oriënteer(W["514120690"]["c"], w3[-1])
    w5 = oriënteer(W["232717968"]["c"], w4[-1])
    w6 = oriënteer(W["457397239"]["c"], w5[-1])
    w7 = W["457397240"]["c"]
    j = min(range(len(w7)), key=lambda i: hav(w7[i], TRC_START))
    w7 = w7[: j + 1]
    w8 = oriënteer(W["1328508024"]["c"], TRC_START)
    B = stik([w3, w4, w5, w6, w7, w8], naden)
    # C
    C = oriënteer(W["232080899"]["c"], (45.6603878, 4.8591863))
    for nm, p in (("a", A), ("b", B), ("c", C)):
        print(f"{nm}: {len(p)} punten, {lengte(p):.1f} km; {p[0][0]:.4f},{p[0][1]:.4f} -> {p[-1][0]:.4f},{p[-1][1]:.4f}")
    print("naden (m):", [round(n) for n in naden])
    print(f"gat 1: {hav(A[-1], B[0]):.1f} km; gat 2: {hav(B[-1], C[0]):.1f} km")
    tot = lengte(A) + lengte(B) + lengte(C) + hav(A[-1], B[0]) + hav(B[-1], C[0])
    print(f"totaal incl. gaten: {tot:.1f} km tegen 260 gepubliceerd ({(tot / 260 - 1) * 100:+.1f}%)")
    if args.schrijf:
        namen = {"a": "SPSE Fos tankenpark -> Rhone-kruising (OSM-ways 420942590, 232593022)",
                 "b": "SPSE Rhone -> Lyon-aflevering -> TRC HC 16 inch richting Feyzin (OSM-ways 232593024, 514120690, 232717968, 457397240, 1328508024)",
                 "c": "SPSE-aftak Feyzin, laatste stuk in de raffinaderij (OSM-way 232080899)"}
        for nm, p in (("a", A), ("b", B), ("c", C)):
            coords = [[round(q[1], 5), round(q[0], 5)] for q in p]
            sch = [coords[0]] + [c for i, c in enumerate(coords[1:]) if c != coords[i]]
            doc = {"type": "FeatureCollection", "features": [{
                "type": "Feature",
                "properties": {"naam": namen[nm], "km": round(lengte(p), 2), "punten": len(sch),
                               "bron": "OpenStreetMap-bijdragers (ODbL), man_made=pipeline substance=oil",
                               "gereedschap": "maak_leidingbeen_olie_fos_feyzin.py"},
                "geometry": {"type": "LineString", "coordinates": sch}}]}
            uit = os.path.join(BEEN, f"{PREFIX}-leiding-{nm}.geojson")
            json.dump(doc, open(uit, "w", encoding="utf-8"), ensure_ascii=False)
            print("geschreven:", uit, len(sch), "punten")
    return 0


if __name__ == "__main__":
    sys.exit(main())
