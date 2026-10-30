#!/usr/bin/env python3
"""maak_leidingbeen_olie_permian_ingleside.py - b1 van olie-permian-ingleside.

Brief v2/design/routebrieven/olie-permian-ingleside.md: de Gray Oak Pipeline (Permian -> Ingleside) staat
in OSM als man_made=pipeline (substance oil). Dit script scant het Geofabrik-extract us-texas op de 14
way-id's uit het ketenontwerp (EPIC Crude en Cactus II liggen parallel en worden dus NIET gekozen),
cachet ze en stikt ze in de ontwerpvolgorde tot een LineString (FeatureCollection). Naden worden gemeld.

    python v2/tools/maak_leidingbeen_olie_permian_ingleside.py --scan
    python v2/tools/maak_leidingbeen_olie_permian_ingleside.py --schrijf
"""
import sys, os, json, math, argparse

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../v2
GEO = os.path.join(WORTEL, "build-cache", "geofabrik", "us-texas-latest.osm.pbf")
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
CACHE = os.path.join(BEEN, "olie-permian-ingleside-grayoakways-us-texas.json")
UIT = os.path.join(BEEN, "olie-permian-ingleside-leiding-grayoak.geojson")
WAYS = [1104121268, 1105284384, 1105284800, 1098449676, 1098271344, 1066747826, 1080984162,
        1080983938, 1094702482, 1059837677, 1059836731, 1093594676, 1089472439, 1089472435]
NAAM = "Gray Oak Pipeline, Permian-aanvoer (Reagan County) naar Ingleside (OSM-gestikt, 14 ways)"
R = 6371.0088


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[1], a[0], b[1], b[0]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def scan():
    if os.path.exists(CACHE):
        return json.load(open(CACHE, encoding="utf-8"))
    import osmium
    gezocht = set(WAYS)
    uit = {}
    for obj in (osmium.FileProcessor(GEO).with_locations()
                .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
                .with_filter(osmium.filter.KeyFilter("man_made"))):
        if obj.id not in gezocht:
            continue
        t = obj.tags
        pts = [(n.location.lon, n.location.lat) for n in obj.nodes if n.location.valid()]
        uit[obj.id] = {"id": obj.id, "tags": {x.k: x.v for x in t},
                       "pts": [[round(x, 6), round(y, 6)] for x, y in pts]}
    json.dump(uit, open(CACHE, "w", encoding="utf-8"))
    return uit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", action="store_true")
    ap.add_argument("--schrijf", action="store_true")
    a = ap.parse_args()
    ws = scan()
    print(f"{len(ws)} van {len(WAYS)} ways gevonden")
    for wid in WAYS:
        w = ws.get(str(wid)) or ws.get(wid)
        if not w:
            print("ONTBREEKT", wid); continue
        t = w["tags"]
        print(wid, t.get("name"), t.get("operator"), t.get("substance"), len(w["pts"]))
    if not a.schrijf:
        return
    coords = []
    naden = []
    for wid in WAYS:
        w = ws.get(str(wid)) or ws.get(wid)
        pts = [tuple(p) for p in w["pts"]]
        if not coords:
            coords = list(pts); continue
        # oriënteer de volgende way zodat hij aansluit op het huidige eind
        d_vw = km(coords[-1], pts[0]); d_ach = km(coords[-1], pts[-1])
        if d_ach < d_vw:
            pts.reverse(); d_vw = d_ach
        naden.append(d_vw)
        if d_vw < 0.0005:
            pts = pts[1:]
        coords += pts
    lengte = sum(km(coords[i], coords[i + 1]) for i in range(len(coords) - 1))
    print(f"gestikt: {lengte:.1f} km, {len(coords)} punten, grootste naad {max(naden):.3f} km, "
          f"kop {coords[0][1]:.4f},{coords[0][0]:.4f} eind {coords[-1][1]:.4f},{coords[-1][0]:.4f}")
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"naam": NAAM, "way_ids": WAYS, "km": round(lengte, 1)},
        "geometry": {"type": "LineString",
                     "coordinates": [[round(x, 5), round(y, 5)] for x, y in coords]}}]}
    json.dump(fc, open(UIT, "w", encoding="utf-8"))
    print("geschreven:", UIT)


if __name__ == "__main__":
    main()
