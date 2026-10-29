#!/usr/bin/env python3
"""maak_leidingbeen_olie_pasadena_linden.py — b1 van olie-pasadena-linden.

WAAROM DIT BESTAAT. Brief v2/design/routebrieven/olie-pasadena-linden.md: de Colonial Pipeline
(Line 1 + onbenoemde hoofdlijn-ways, Pasadena TX -> Linden NJ) staat in OSM als man_made=pipeline
met operator Colonial. Dit script scant per Geofabrik-extract (pyosmium, patroon
maak_leidingbeen_keystone.py) alle pipeline-ways waarvan name/operator/owner "colonial" bevat,
cachet ze per extract, sluit de zijlijnen uit op naam (lijst in brief par.4), ontdubbelt op way-id
en stikt het kortste pad Pasadena-kop -> Linden-eind over gedeelde nodes (5 decimalen) plus naden
< --tol km (default 0,15), die gemeld worden. Uitvoer: een FeatureCollection met een LineString.

    python v2/tools/maak_leidingbeen_olie_pasadena_linden.py --scan            # caches vullen
    python v2/tools/maak_leidingbeen_olie_pasadena_linden.py --schrijf         # stikken + wegschrijven
"""
import sys, os, json, math, heapq, re, argparse

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../v2
GEO = os.path.join(WORTEL, "build-cache", "geofabrik")
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
R = 6371.0088
EXTRACTS = ["us-texas", "us-louisiana", "us-mississippi", "us-alabama", "us-georgia",
            "us-south-carolina", "us-north-carolina", "us-virginia", "us-maryland",
            "us-delaware", "us-pennsylvania", "us-new-jersey"]
KOP = (-95.1799, 29.7203)     # (lon, lat)
EIND = (-74.2492, 40.5768)
UIT = os.path.join(BEEN, "olie-pasadena-linden-leiding-colonial.geojson")
NAAM = "Colonial Pipeline hoofdlijn Pasadena naar Linden (Line 1 benzine, raffinaat; OSM-gestikt)"
WEIGER = re.compile(r"line\s*#?\s*2|2pa|1pa|loop|augusta|roanoke|atlanta|albany|zachary|pasadena to|"
                    r"lateral|lsmb|out of service|main line|line\s*8\b|line\s*9\b|line\s*15\d\d|line\s*16\d\d", re.I)


def cache_pad(ex):
    return os.path.join(BEEN, f"olie-pasadena-linden-colonialways-{ex}.json")


def scan(ex):
    import osmium
    pad = cache_pad(ex)
    if os.path.exists(pad):
        return json.load(open(pad, encoding="utf-8"))
    uit = []
    src = os.path.join(GEO, f"{ex}-latest.osm.pbf")
    for obj in (osmium.FileProcessor(src).with_locations()
                .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
                .with_filter(osmium.filter.KeyFilter("man_made"))):
        t = obj.tags
        if t.get("man_made") != "pipeline":
            continue
        blob = " ".join(t.get(k, "") for k in ("name", "operator", "owner", "ref", "brand")).lower()
        if "colonial" not in blob:
            continue
        pts = [(n.location.lon, n.location.lat) for n in obj.nodes if n.location.valid()]
        uit.append({"id": obj.id, "name": t.get("name", ""), "operator": t.get("operator", ""),
                    "substance": t.get("substance", ""), "ref": t.get("ref", ""),
                    "tags": {x.k: x.v for x in t},
                    "pts": [[round(x, 6), round(y, 6)] for x, y in pts]})
    json.dump(uit, open(pad, "w", encoding="utf-8"))
    return uit


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[1], a[0], b[1], b[0]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def kies(w):
    naam = w["name"] or ""
    if naam and WEIGER.search(naam):
        return False
    if not naam:
        if w["substance"].lower() == "oil":
            return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", action="store_true")
    ap.add_argument("--schrijf", action="store_true")
    ap.add_argument("--tol", type=float, default=0.15)
    a = ap.parse_args()
    alle = {}
    for ex in EXTRACTS:
        if not os.path.exists(cache_pad(ex)):
            print("scan", ex, flush=True)
        ws = scan(ex)
        print(f"{ex}: {len(ws)} colonial-ways", flush=True)
        for w in ws:
            alle.setdefault(w["id"], w)
    if a.scan and not a.schrijf:
        return
    ways = [w for w in alle.values() if kies(w) and len(w["pts"]) >= 2]
    print(f"{len(alle)} unieke colonial-ways, {len(ways)} na uitsluiting")
    # graaf: nodes op 5 decimalen
    knoop = {}
    adj = {}

    def nid(p):
        k = (round(p[0], 5), round(p[1], 5))
        if k not in knoop:
            knoop[k] = len(knoop)
            adj[knoop[k]] = []
        return knoop[k]
    ends = []   # (nid, wayidx)
    seg = {}    # (u,v) -> way index, om pad terug te leggen
    for wi, w in enumerate(ways):
        ids = [nid(p) for p in w["pts"]]
        pts = [tuple(p) for p in w["pts"]]
        for i in range(len(ids) - 1):
            u, v = ids[i], ids[i + 1]
            if u == v:
                continue
            d = km(pts[i], pts[i + 1])
            adj[u].append((v, d, wi, False))
            adj[v].append((u, d, wi, False))
        ends.append((ids[0], wi)); ends.append((ids[-1], wi))
    inv = {v: k for k, v in knoop.items()}
    # naden tussen uiteinden van verschillende componenten/ways
    nse = 0
    emmer = {}
    for u, wi in ends:
        x, y = inv[u]
        emmer.setdefault((int(x * 50), int(y * 50)), []).append((u, wi))
    for (bx, by), lst in emmer.items():
        kand = []
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                kand += emmer.get((bx + dx, by + dy), [])
        for u, wi in lst:
            for v, wj in kand:
                if u >= v or wi == wj or u == v:
                    continue
                d = km(inv[u], inv[v])
                if d <= a.tol:
                    adj[u].append((v, d, -1, True))
                    adj[v].append((u, d, -1, True))
                    nse += 1
    print("potentiele naden:", nse)

    def dichtste(p):
        best = min(knoop, key=lambda k: km(k, p))
        return knoop[best], km(best, p)
    s, ds = dichtste(KOP)
    t, dt = dichtste(EIND)
    print(f"kop snap {ds*1000:.1f} m, eind snap {dt*1000:.1f} m")
    dist = {s: 0.0}
    prev = {}
    hp = [(0.0, s)]
    while hp:
        d, u = heapq.heappop(hp)
        if d > dist.get(u, 1e18):
            continue
        if u == t:
            break
        for v, w_, wi, naad in adj[u]:
            nd = d + w_
            if nd < dist.get(v, 1e18):
                dist[v] = nd
                prev[v] = (u, wi, naad, w_)
                heapq.heappush(hp, (nd, v))
    if t not in dist:
        print("GEEN PAD"); sys.exit(1)
    pad = [t]
    naden = []
    wayids = []
    u = t
    while u != s:
        p, wi, naad, w_ = prev[u]
        if naad:
            naden.append(w_)
        elif not wayids or wayids[-1] != ways[wi]["id"]:
            wayids.append(ways[wi]["id"])
        pad.append(p); u = p
    pad.reverse(); wayids.reverse()
    coords = [list(inv[n]) for n in pad]
    lengte = sum(km(coords[i], coords[i + 1]) for i in range(len(coords) - 1))
    print(f"pad: {lengte:.1f} km, {len(coords)} punten, {len(wayids)} way-id's, {len(naden)} naden, "
          f"grootste {max(naden) if naden else 0:.3f} km, hemelsbreed {km(KOP, EIND):.0f} km")
    namen = {}
    for wid in wayids:
        w = alle[wid]
        namen.setdefault(w["name"] or "(onbenoemd)", 0)
        namen[w["name"] or "(onbenoemd)"] += 1
    print("namen op pad:", namen)
    if a.schrijf:
        fc = {"type": "FeatureCollection", "features": [{
            "type": "Feature",
            "properties": {"naam": NAAM, "way_ids": wayids, "km": round(lengte, 1)},
            "geometry": {"type": "LineString", "coordinates": [[round(x, 5), round(y, 5)] for x, y in coords]}}]}
        json.dump(fc, open(UIT, "w", encoding="utf-8"))
        print("geschreven:", UIT)


if __name__ == "__main__":
    main()
