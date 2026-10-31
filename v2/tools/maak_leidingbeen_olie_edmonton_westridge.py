#!/usr/bin/env python3
"""maak_leidingbeen_olie_edmonton_westridge.py - b1 van olie-edmonton-westridge.

Brief v2/design/routebrieven/olie-edmonton-westridge.md. Trans Mountain Pipeline (TMPL + TMX) staat in OSM als
man_made=pipeline (substance=oil) in losse ways met wisselende naam/operator (aannemers, naamloos). Dit script
scant de Geofabrik-extract canada binnen lat 48,9-54,2 / lon -123,5..-112,5, selecteert op SUBSTANCE (niet op naam),
stikt met Dijkstra (korting op ways die Trans Mountain heten; bruggen max 1,5 km, 5 km-equivalent per brug) van de
Edmonton-wayeinde-kop naar het Westridge-anker en schrijft een FeatureCollection.

    python v2/tools/maak_leidingbeen_olie_edmonton_westridge.py --scan      # pyosmium, ca. 10 min
    python v2/tools/maak_leidingbeen_olie_edmonton_westridge.py --schrijf   # stikken + geojson
"""
import sys, os, json, math, heapq, argparse

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../v2
PBF = os.path.join(WORTEL, "build-cache", "geofabrik", "canada-latest.osm.pbf")
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
CACHE = os.path.join(BEEN, "olie-edmonton-westridge-ways.json")
NAMEN = os.path.join(BEEN, "olie-edmonton-westridge-namen.json")
UIT = os.path.join(BEEN, "olie-edmonton-westridge-leiding-tmpl.geojson")
BBOX = (48.9, -123.5, 54.2, -112.5)     # lat0, lon0, lat1, lon1
START = (-113.4187, 53.4976)     # (lon, lat) OSM-wayeinde Edmonton, uit de haalbaarheidstoets (aanpassen na de scan)
EIND = (-122.9560, 49.2932)      # ol-westridge-term (lon, lat), letterlijk uit olie-westridge-ulsan
NAAM = "Trans Mountain Pipeline (TMPL + TMX), Edmonton naar Westridge (OSM-gestikt)"
BRUG_MAX = 1.5
R = 6371.0088


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[1], a[0], b[1], b[0]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def scan():
    import osmium
    uit, namen = {}, []
    n = 0
    for obj in (osmium.FileProcessor(PBF).with_locations()
                .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
                .with_filter(osmium.filter.KeyFilter("man_made", "operator", "name"))):
        n += 1
        t = obj.tags
        txt = ((t.get("name") or "") + " " + (t.get("operator") or "")).lower()
        mm = t.get("man_made")
        if mm == "pipeline" or "trans mountain" in txt or "transmountain" in txt:
            pts = [[round(nd.location.lon, 6), round(nd.location.lat, 6)] for nd in obj.nodes if nd.location.valid()]
            if not pts or not any(BBOX[0] <= y <= BBOX[2] and BBOX[1] <= x <= BBOX[3] for x, y in pts):
                continue
            if mm == "pipeline" and t.get("substance") in ("oil", "crude_oil", "fuel", "gas;oil", "oil;gas"):
                uit[str(obj.id)] = {"id": obj.id, "naam": t.get("name"), "operator": t.get("operator"),
                                    "substance": t.get("substance"), "location": t.get("location"), "pts": pts}
            if "trans mountain" in txt or "transmountain" in txt:
                namen.append({"id": obj.id, "man_made": mm, "naam": t.get("name"), "operator": t.get("operator"),
                              "landuse": t.get("landuse"), "substance": t.get("substance"),
                              "p0": pts[0], "pn": pts[-1], "n": len(pts)})
        if n % 2000000 == 0:
            print(n, "ways gezien;", len(uit), "pijp-ways", flush=True)
    json.dump(uit, open(CACHE, "w", encoding="utf-8"))
    json.dump(namen, open(NAMEN, "w", encoding="utf-8"), ensure_ascii=False)
    print("klaar:", len(uit), "pijp-ways,", len(namen), "TM-benoemde ways", flush=True)


def key(p):
    return (round(p[0], 5), round(p[1], 5))


def stik(start=START, eind=EIND):
    ways = json.load(open(CACHE, encoding="utf-8"))
    adj, coord = {}, {}

    def tm(w):
        return "trans mountain" in ((w.get("naam") or "") + " " + (w.get("operator") or "")).lower()

    def add(a, b, d, wid, korting):
        adj.setdefault(a, []).append((b, d, wid, korting))
        adj.setdefault(b, []).append((a, d, wid, korting))
    for wid, w in ways.items():
        kt = tm(w)
        for a, b in zip(w["pts"], w["pts"][1:]):
            ka, kb = key(a), key(b)
            if ka != kb:
                coord[ka], coord[kb] = a, b
                add(ka, kb, km(a, b), wid, kt)
    # bruggen: een wayeinde bindt aan elk vertex van een ANDERE way binnen BRUG_MAX (T-aansluitingen komen voor)
    cel = {}
    for wid, w in ways.items():
        for p in w["pts"]:
            cel.setdefault((int(p[0] * 20), int(p[1] * 20)), []).append((key(p), wid))
    gezien = set()
    for wid, w in ways.items():
        for p in (w["pts"][0], w["pts"][-1]):
            ka = key(p)
            cx, cy = int(p[0] * 20), int(p[1] * 20)
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for kb, wb in cel.get((cx + dx, cy + dy), ()):
                        if wb != wid and kb != ka and (ka, kb) not in gezien and 0 < km(coord[ka], coord[kb]) <= BRUG_MAX:
                            gezien.add((ka, kb)); gezien.add((kb, ka))
                            add(ka, kb, km(coord[ka], coord[kb]), "brug", False)
    s = min(coord, key=lambda k: km(k, start))
    g = min(coord, key=lambda k: km(k, eind))
    dist, prev, pq = {s: 0.0}, {}, [(0.0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, 1e18):
            continue
        if u == g:
            break
        for v, dd, wid, kt in adj.get(u, ()):
            c = d + dd * (0.8 if kt else 1.0) + (5 if wid == "brug" else 0)
            if c < dist.get(v, 1e18):
                dist[v], prev[v] = c, (u, dd, wid)
                heapq.heappush(pq, (c, v))
    pad = [g]
    while pad[-1] != s:
        pad.append(prev[pad[-1]][0])
    pad.reverse()
    totaal, brug, gebruikt = 0.0, [], {}
    for a, b in zip(pad, pad[1:]):
        _, dd, wid = prev[b]
        totaal += dd
        if wid == "brug":
            brug.append(round(dd, 3))
        else:
            gebruikt[wid] = gebruikt.get(wid, 0.0) + dd
    print(f"stik: {totaal:.1f} km, {len(pad)} punten, {len(gebruikt)} ways, bruggen {brug} (som {sum(brug):.2f} km)")
    print(f"start {coord[s]} op {km(coord[s], start):.2f} km van opgegeven start; eind {coord[g]} op {km(coord[g], eind):.3f} km van anker")
    for wid, d in sorted(gebruikt.items(), key=lambda x: -x[1]):
        w = ways[wid]
        print(f"  way {wid}: {d:7.1f} km  naam={w.get('naam')!r} operator={w.get('operator')!r} substance={w.get('substance')}")
    return [list(coord[k]) for k in pad], totaal


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", action="store_true")
    ap.add_argument("--schrijf", action="store_true")
    ap.add_argument("--start", help="lat,lon van de kop (overschrijft START)")
    a = ap.parse_args()
    if a.scan:
        scan()
    if a.schrijf:
        st = START
        if a.start:
            la, lo = map(float, a.start.split(","))
            st = (lo, la)
        pts, tot = stik(st)
        fc = {"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"name": NAAM, "km": round(tot, 1)},
              "geometry": {"type": "LineString", "coordinates": pts}}]}
        json.dump(fc, open(UIT, "w", encoding="utf-8"))
        print("geschreven:", UIT)


if __name__ == "__main__":
    main()
