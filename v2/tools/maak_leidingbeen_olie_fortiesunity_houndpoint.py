#!/usr/bin/env python3
"""maak_leidingbeen_olie_fortiesunity_houndpoint.py — b1, b2 en b3 van olie-fortiesunity-houndpoint.

WAAROM DIT BESTAAT. Brief v2/design/routebrieven/olie-fortiesunity-houndpoint.md (§2 en §4): het
Forties Pipeline System (Ineos FPS, 36 inch) staat in OSM als een reeks man_made=pipeline-ways
(operator Ineos FPS). Dit script leest die ways BIJ ID uit de pbf (ids uit brief §4), zet ze in
reisvolgorde en oriënteert elke way zo dat hij aansluit op het uiteinde van de vorige. Waar twee
opeenvolgende ways niet aansluiten (OSM mist ondergrondse stukken) komt een RECHT stuk (naad,
hemelsbreed) in de lijn en wordt de lengte ervan gemeld; de brief noemt ze 'naden'.
  b1  Forties Unity -> landfall Cruden Bay (onderzees)        ways 903798450, 174743471
  b2  landfall Cruden Bay -> Kinneil Terminal (onshore, 8 naden) ways 1079030566 ... 1449717146
  b3  Kinneil -> Dalmeny -> Hound Point                        ways 868045319 ... 689503549
De b2-lijn eindigt op het begin van b3 (naad 0,25 km); b1 eindigt waar b2 begint (het landfall).
Pure-Python-PBF-lezer (pyosmium is hier geblokkeerd); de lezer komt uit
maak_leidingbeen_olie_johansverdrup_mongstad.py. Scan van het Britse extract: ca 2,5 min.

Bron: OpenStreetMap-bijdragers (ODbL), v2/build-cache/geofabrik/groot-brittannie-latest.osm.pbf.
Uitvoer: v2/build-cache/ais/graaf/olie-fortiesunity-houndpoint-leiding-b{1,2,3}.geojson
(FeatureCollection, een LineString) — zonder --schrijf alleen een rapport.

    python v2/tools/maak_leidingbeen_olie_fortiesunity_houndpoint.py --schrijf
"""
import sys, zlib, struct, json, math, os, argparse
import numpy as np

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../v2
PBF = os.path.join(WORTEL, "build-cache", "geofabrik", "groot-brittannie-latest.osm.pbf")
UITMAP = os.path.join(WORTEL, "build-cache", "ais", "graaf")
R = 6371.0088

# way-ids in reisvolgorde (brief §4)
BENEN = {
    "b1": [903798450, 174743471],
    "b2": [1079030566, 995752750, 1080555747, 1418120450, 1418120452, 1050623035,
           1449978876, 1449978877, 1449717146],
    "b3": [868045319, 868045318, 689506386, 689503549],
}
NAAM = {
    "b1": "Forties-pijpleiding offshore (OSM-ways 903798450 + 174743471), Forties Unity -> Cruden Bay",
    "b2": "Ineos FPS onshore 36 inch, Cruden Bay -> Kinneil Terminal (OSM, met rechte naden)",
    "b3": "Ineos FPS Kinneil -> Dalmeny -> Hound Point (OSM ways 868045319, 868045318, 689506386, 689503549)",
}
KOP = (0.75203, 57.72049)   # (lon, lat) OSM-begin offshore (Forties Unity)


def varint(buf, i):
    r = 0; s = 0
    while True:
        b = buf[i]; i += 1
        r |= (b & 0x7F) << s
        if b < 0x80:
            return r, i
        s += 7


def fields(buf):
    i = 0; n = len(buf)
    while i < n:
        t, i = varint(buf, i)
        f = t >> 3; w = t & 7
        if w == 0:
            v, i = varint(buf, i)
        elif w == 2:
            l, i = varint(buf, i)
            v = buf[i:i + l]; i += l
        elif w == 1:
            v = buf[i:i + 8]; i += 8
        elif w == 5:
            v = buf[i:i + 4]; i += 4
        else:
            raise ValueError("wire %d" % w)
        yield f, w, v


def blobs(path):
    with open(path, "rb") as fh:
        while True:
            h = fh.read(4)
            if len(h) < 4:
                return
            hl = struct.unpack(">I", h)[0]
            hdr = fh.read(hl)
            typ = None; dsz = 0
            for f, w, v in fields(hdr):
                if f == 1: typ = v.decode()
                elif f == 3: dsz = v
            data = fh.read(dsz)
            raw = None
            for f, w, v in fields(data):
                if f == 1: raw = v
                elif f == 3: raw = zlib.decompress(v)
            yield typ, raw


def unpack_varints_np(b):
    a = np.frombuffer(b, dtype=np.uint8)
    if a.size == 0:
        return np.zeros(0, dtype=np.uint64)
    ends = np.flatnonzero(a < 0x80)
    starts = np.concatenate(([0], ends[:-1] + 1))
    lens = ends - starts + 1
    out = np.zeros(len(ends), dtype=np.uint64)
    for k in range(int(lens.max())):
        m = lens > k
        idx = starts[m] + k
        out[m] |= (a[idx].astype(np.uint64) & np.uint64(0x7F)) << np.uint64(7 * k)
    return out


def zigzag(u):
    u = u.astype(np.uint64)
    return ((u >> np.uint64(1)).astype(np.int64)) ^ (-(u & np.uint64(1)).astype(np.int64))


def ways_bij_id(raw, wil):
    """way-id -> refs voor de gewenste ids in dit blok"""
    groups = []
    for f, w, v in fields(raw):
        if f == 2:
            groups.append(v)
    out = {}
    for g in groups:
        for f, w, v in fields(g):
            if f != 3:
                continue
            wid = None; refs = b""
            for ff, ww, vv in fields(v):
                if ff == 1: wid = vv
                elif ff == 8: refs = vv
            if wid in wil:
                out[wid] = np.cumsum(zigzag(unpack_varints_np(refs)))
    return out


def dense_nodes_gewenst(raw, want):
    """alleen de nodes uit `want` (gesorteerde np-array); eerst de ids, pas dan lat/lon"""
    gran = 100; lat_off = 0; lon_off = 0; groups = []
    for f, w, v in fields(raw):
        if f == 2: groups.append(v)
        elif f == 17: gran = v
        elif f == 19: lat_off = v
        elif f == 20: lon_off = v
    for g in groups:
        for f, w, v in fields(g):
            if f != 2:
                continue
            idb = latb = lonb = None
            for ff, ww, vv in fields(v):
                if ff == 1: idb = vv
                elif ff == 8: latb = vv
                elif ff == 9: lonb = vv
            if idb is None:
                continue
            ids = np.cumsum(zigzag(unpack_varints_np(idb)))
            pos = np.searchsorted(want, ids)
            pos[pos >= len(want)] = 0
            m = want[pos] == ids
            if not m.any():
                continue
            lat = np.cumsum(zigzag(unpack_varints_np(latb)))
            lon = np.cumsum(zigzag(unpack_varints_np(lonb)))
            la = (lat_off + gran * lat) * 1e-9
            lo = (lon_off + gran * lon) * 1e-9
            yield ids[m], la[m], lo[m]


def km(a, b):
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))


def lees_ways():
    wil = set()
    for ids in BENEN.values():
        wil.update(ids)
    gevonden = {}
    for typ, raw in blobs(PBF):
        if typ == "OSMData" and b"pipeline" in raw:
            gevonden.update(ways_bij_id(raw, wil))
    ontbreekt = wil - set(gevonden)
    if ontbreekt:
        raise SystemExit(f"ways niet gevonden: {sorted(ontbreekt)}")
    want = np.unique(np.concatenate([gevonden[i] for i in wil]))
    coords = {}
    for typ, raw in blobs(PBF):
        if typ != "OSMData":
            continue
        for ids, lat, lon in dense_nodes_gewenst(raw, want):
            for i, la, lo in zip(ids, lat, lon):
                coords[int(i)] = (float(lo), float(la))
    return {w: [coords[int(r)] for r in refs if int(r) in coords] for w, refs in gevonden.items()}


def stik(ways, ids, start):
    """ways in volgorde, elk georiënteerd op het uiteinde van de vorige; naden = rechte stukken"""
    pts = [start]; naden = []
    for wid in ids:
        c = ways[wid]
        if km(pts[-1], c[0]) > km(pts[-1], c[-1]):
            c = c[::-1]
        d = km(pts[-1], c[0])
        if d > 0.002:
            naden.append([wid, round(d, 2)])
        pts.extend(c)
    return pts, naden


def schoon(pts):
    out = []
    for p in pts:
        q = [round(p[0], 5), round(p[1], 5)]
        if not out or out[-1] != q:
            out.append(q)
    return out


def lengte(pts):
    return sum(km(pts[i-1], pts[i]) for i in range(1, len(pts)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()
    ways = lees_ways()

    # b1: begint bij het OSM-begin offshore; de eerste way-oriëntatie volgt uit KOP
    p1, n1 = stik(ways, BENEN["b1"], KOP)
    p1 = p1[1:]                                  # het startpunt zelf is geen vertex
    landfall = p1[-1]
    # b2: begint op het landfall (einde b1); b3 begint op het begin van way 868045319
    w3 = ways[BENEN["b3"][0]]
    p2, n2 = stik(ways, BENEN["b2"], landfall)
    # b3: oriënteer 868045319 zo dat hij begint bij het uiteinde van b2 (kinneil-west)
    p3, n3 = stik(ways, BENEN["b3"], p2[-1])
    p3 = p3[1:]
    n3 = [x for x in n3 if x[0] != BENEN["b3"][0]]   # die naad hoort bij b2
    # b2 eindigt op het begin van b3 (naad: einde laatste b2-way -> begin 868045319)
    eind_b2_way = p2[-1]
    p2 = p2 + [p3[0]] if km(p2[-1], p3[0]) > 0.002 else p2
    if km(eind_b2_way, p3[0]) > 0.002:
        n2.append(["kinneil-west->868045319 start", round(km(eind_b2_way, p3[0]), 2)])
    uit = {"b1": (p1, n1), "b2": (p2, n2), "b3": (p3, n3)}
    for b, (pts, naden) in uit.items():
        pts = schoon(pts)
        uit[b] = (pts, naden)
        print(f"{b}: {lengte(pts):.1f} km, {len(pts)} punten, naden {naden} "
              f"({sum(x[1] for x in naden):.2f} km), begin {pts[0]}, eind {pts[-1]}")
    if args.schrijf:
        for b, (pts, naden) in uit.items():
            doc = {"type": "FeatureCollection", "features": [{
                "type": "Feature",
                "properties": {"naam": NAAM[b], "km": round(lengte(pts), 1), "punten": len(pts),
                               "naden_km": naden,
                               "bron": "OpenStreetMap-bijdragers (ODbL), groot-brittannie-extract, man_made=pipeline ways bij id",
                               "gereedschap": "maak_leidingbeen_olie_fortiesunity_houndpoint.py"},
                "geometry": {"type": "LineString", "coordinates": pts}}]}
            pad = os.path.join(UITMAP, f"olie-fortiesunity-houndpoint-leiding-{b}.geojson")
            with open(pad, "w", encoding="utf-8") as f:
                json.dump(doc, f, ensure_ascii=False)
            print(f"geschreven: {pad} ({os.path.getsize(pad)/1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
