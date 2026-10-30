#!/usr/bin/env python3
"""maak_leidingbeen_olie_hardisty_superior.py - b1 van olie-hardisty-superior.

Brief v2/design/routebrieven/olie-hardisty-superior.md. Enbridge Line 3 staat in OSM als man_made=pipeline
(substance=oil): "Enbridge Line 3 Replacement" (AB/SK ca. 333 km, MB+ND ca. 199 km, MN 585 km, WI 33 km) en op de
overige ca. 650 km (SK/MB) alleen onder de naam "Lakehead Pipeline" in dezelfde corridor. Dit script scant vier Geofabrik-extracts
(canada alleen binnen lat 48,9-53,3 / lon -111,8..-96,5), stikt met Dijkstra (korting 0,5 op Line 3 Replacement,
bruggen max 2 km, kost 5 km-equivalent per brug) van de Hardisty-ankerkop naar het Superior-anker en schrijft een FeatureCollection.

    python v2/tools/maak_leidingbeen_olie_hardisty_superior.py --scan       # pyosmium, ca. 10 min (canada 6,4 GB)
    python v2/tools/maak_leidingbeen_olie_hardisty_superior.py --schrijf    # stikken + geojson
"""
import sys, os, json, math, heapq, argparse

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../v2
GEO = os.path.join(WORTEL, "build-cache", "geofabrik")
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
CACHE = os.path.join(BEEN, "olie-hardisty-superior-ways.json")
UIT = os.path.join(BEEN, "olie-hardisty-superior-leiding-line3.geojson")
EXTRACTS = {"canada": (48.9, -111.8, 53.3, -96.5), "us-north-dakota": None, "us-minnesota": None, "us-wisconsin": None}
NAMEN = ("Enbridge Line 3 Replacement", "Lakehead Pipeline", "Enbridge Lakehead Pipeline")
START = (-111.2800, 52.6437)     # ol-hardisty-terminal (lon, lat), letterlijk uit olie-hardisty-cushing
EIND = (-92.0635, 46.6895)       # ol-superior-terminal
NAAM = "Enbridge Line 3 (Replacement) plus Lakehead-mainlinecorridor, Hardisty naar Superior (OSM-gestikt)"
BRUG_MAX = 2.0
R = 6371.0088


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[1], a[0], b[1], b[0]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def scan():
    import osmium
    uit = {}
    for slug, bbox in EXTRACTS.items():
        pad = os.path.join(GEO, f"{slug}-latest.osm.pbf")
        for obj in (osmium.FileProcessor(pad).with_locations()
                    .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
                    .with_filter(osmium.filter.KeyFilter("man_made"))):
            t = obj.tags
            if t.get("man_made") != "pipeline" or t.get("substance") != "oil" or t.get("name") not in NAMEN:
                continue
            pts = [[round(n.location.lon, 6), round(n.location.lat, 6)] for n in obj.nodes if n.location.valid()]
            if bbox and not any(bbox[0] <= y <= bbox[2] and bbox[1] <= x <= bbox[3] for x, y in pts):
                continue
            uit[str(obj.id)] = {"id": obj.id, "naam": t.get("name"), "extract": slug, "pts": pts}
        print(slug, len(uit), "ways totaal", flush=True)
    json.dump(uit, open(CACHE, "w", encoding="utf-8"))


def key(p):
    return (round(p[0], 5), round(p[1], 5))


def stik():
    ways = json.load(open(CACHE, encoding="utf-8"))
    adj, coord = {}, {}

    def add(a, b, d, wid, l3):
        adj.setdefault(a, []).append((b, d, wid, l3))
        adj.setdefault(b, []).append((a, d, wid, l3))
    for wid, w in ways.items():
        l3 = w["naam"] == "Enbridge Line 3 Replacement"
        for a, b in zip(w["pts"], w["pts"][1:]):
            ka, kb = key(a), key(b)
            if ka != kb:
                coord[ka], coord[kb] = a, b
                add(ka, kb, km(a, b), wid, l3)
    ends = [(key(p), wid) for wid, w in ways.items() for p in (w["pts"][0], w["pts"][-1])]
    for i, (ka, wa) in enumerate(ends):
        for kb, wb in ends[i + 1:]:
            if wa != wb and ka != kb and 0 < km(coord[ka], coord[kb]) <= BRUG_MAX:
                add(ka, kb, km(coord[ka], coord[kb]), "brug", False)
    s = min(coord, key=lambda k: km(k, START))
    g = min(coord, key=lambda k: km(k, EIND))
    for wid, w in ways.items():                      # Hardisty-kop van Line 3 Replacement binnen 2 km van het startpunt
        if w["naam"] == "Enbridge Line 3 Replacement":
            for p in (w["pts"][0], w["pts"][-1]):
                if key(p) != s and km(p, coord[s]) <= BRUG_MAX:
                    add(s, key(p), km(p, coord[s]), "brug", False)
    dist, prev, pq = {s: 0.0}, {}, [(0.0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, 1e18):
            continue
        if u == g:
            break
        for v, dd, wid, l3 in adj.get(u, ()):
            c = d + dd * (0.5 if l3 else 1.0) + (5 if wid == "brug" else 0)
            if c < dist.get(v, 1e18):
                dist[v], prev[v] = c, (u, dd, wid)
                heapq.heappush(pq, (c, v))
    pad = [g]
    while pad[-1] != s:
        pad.append(prev[pad[-1]][0])
    pad.reverse()
    totaal, brug, l3km = 0.0, [], 0.0
    for a, b in zip(pad, pad[1:]):
        _, dd, wid = prev[b]
        totaal += dd
        if wid == "brug":
            brug.append(round(dd, 3))
        elif ways[str(wid)]["naam"] == "Enbridge Line 3 Replacement":
            l3km += dd
    print(f"stik: {totaal:.1f} km, {len(pad)} punten; Line 3 Replacement {l3km:.1f} km, Lakehead {totaal - l3km - sum(brug):.1f} km; bruggen {brug}")
    print(f"start {coord[s]} op {km(coord[s], START):.2f} km van anker; eind {coord[g]} op {km(coord[g], EIND):.3f} km van anker")
    return [list(coord[k]) for k in pad], totaal


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", action="store_true")
    ap.add_argument("--schrijf", action="store_true")
    a = ap.parse_args()
    if a.scan:
        scan()
    if a.schrijf:
        pts, tot = stik()
        fc = {"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"name": NAAM, "km": round(tot, 1)},
              "geometry": {"type": "LineString", "coordinates": pts}}]}
        json.dump(fc, open(UIT, "w", encoding="utf-8"))
        print("geschreven:", UIT)


if __name__ == "__main__":
    main()
