#!/usr/bin/env python3
"""maak_leidingbeen_olie_prudhoebay_cherrypoint.py — b1 van olie-prudhoebay-cherrypoint.

WAAROM DIT BESTAAT. Brief v2/design/routebrieven/olie-prudhoebay-cherrypoint.md (b1): de
Trans-Alaska Pipeline (TAPS) is in OSM één aaneengesloten component (429 ways op het
pad, man_made=pipeline, substance=oil, name "Trans-Alaska Pipeline (System)", operator
Alyeska). Dit script stikt het kortste pad Prudhoe Bay PS1 -> Valdez-pijpeinde op
GEDEELDE OSM-nodes (zelfde methode als maak_leidingbeen_olie_sangachal_ceyhan.py).

LET OP — pyosmium is op deze machine geblokkeerd (beleid voor toepassingsbeheer, DLL
_osmium), daarom leest dit script de pbf met een kleine pure-Python-PBF-lezer
(protobuf + zlib + numpy; leest alleen man_made=pipeline-ways en hun nodes; ~25 s voor
us-alaska). De lezer is overgenomen uit een scratchpad-hulpscript van de olie-toets
(M31 golf 7).

Bron: OpenStreetMap-bijdragers (ODbL), v2/build-cache/geofabrik/us-alaska-latest.osm.pbf.
Uitvoer: v2/build-cache/ais/graaf/olie-prudhoebay-cherrypoint-leiding-taps.geojson

    python v2/tools/maak_leidingbeen_olie_prudhoebay_cherrypoint.py --schrijf
"""
import sys, zlib, struct, json, math, heapq, os, argparse
import numpy as np

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../v2
PBF = os.path.join(WORTEL, "build-cache", "geofabrik", "us-alaska-latest.osm.pbf")
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf",
                   "olie-prudhoebay-cherrypoint-leiding-taps.geojson")
KOP = (-148.6194, 70.2563)    # (lon, lat) Prudhoe Bay Pump Station 1
EIND = (-146.3684, 61.0830)   # (lon, lat) OSM-pijpeinde Valdez Marine Terminal
R = 6371.0088

import sys, zlib, struct, json
import numpy as np


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
    """packed varints (uint) -> np.uint64 array"""
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


def parse_ways(raw):
    strings = []; groups = []
    gran = 100
    for f, w, v in fields(raw):
        if f == 1:
            for ff, ww, vv in fields(v):
                if ff == 1: strings.append(bytes(vv).decode("utf-8", "replace"))
        elif f == 2:
            groups.append(v)
        elif f == 17:
            gran = v
    out = []
    for g in groups:
        for f, w, v in fields(g):
            if f != 3:
                continue
            wid = None; keys = b""; vals = b""; refs = b""
            for ff, ww, vv in fields(v):
                if ff == 1: wid = vv
                elif ff == 2: keys = vv
                elif ff == 3: vals = vv
                elif ff == 8: refs = vv
            k = unpack_varints_np(keys); vl = unpack_varints_np(vals)
            tags = {strings[int(a)]: strings[int(b)] for a, b in zip(k, vl)}
            if tags.get("man_made") != "pipeline":
                continue
            r = np.cumsum(zigzag(unpack_varints_np(refs)))
            out.append((wid, tags, r))
    return out


def dense_nodes(raw):
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
            ids = lat = lon = None
            for ff, ww, vv in fields(v):
                if ff == 1: ids = np.cumsum(zigzag(unpack_varints_np(vv)))
                elif ff == 8: lat = np.cumsum(zigzag(unpack_varints_np(vv)))
                elif ff == 9: lon = np.cumsum(zigzag(unpack_varints_np(vv)))
            if ids is not None:
                yield ids, (lat_off + gran * lat) * 1e-9, (lon_off + gran * lon) * 1e-9




def km(a, b):
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()
    ways = []
    for typ, raw in blobs(PBF):
        if typ == "OSMData" and b"pipeline" in raw:
            ways.extend(parse_ways(raw))
    taps = []
    for wid, tags, refs in ways:
        n = (tags.get("name") or "").lower()
        if tags.get("substance") == "oil" and "trans-alaska" in n:
            taps.append((wid, tags, refs))
    print(f"TAPS-ways (oil, Trans-Alaska): {len(taps)}")
    want = np.unique(np.concatenate([w[2] for w in taps]))
    coords = {}
    for typ, raw in blobs(PBF):
        if typ != "OSMData":
            continue
        for ids, lat, lon in dense_nodes(raw):
            pos = np.searchsorted(want, ids)
            pos[pos >= len(want)] = 0
            m = want[pos] == ids
            for i, la, lo in zip(ids[m], lat[m], lon[m]):
                coords[int(i)] = (float(lo), float(la))
    buren = {}
    for wid, tags, refs in taps:
        r = [int(x) for x in refs if int(x) in coords]
        for i in range(1, len(r)):
            if r[i-1] != r[i]:
                d = km(coords[r[i-1]], coords[r[i]])
                buren.setdefault(r[i-1], []).append((r[i], d))
                buren.setdefault(r[i], []).append((r[i-1], d))
    a = min(buren, key=lambda k: km(coords[k], KOP))
    b = min(buren, key=lambda k: km(coords[k], EIND))
    print(f"kop-knoop {coords[a]} op {km(coords[a], KOP):.3f} km van PS1; "
          f"eind-knoop {coords[b]} op {km(coords[b], EIND):.3f} km van het pijpeinde")
    dist = {a: 0.0}; vor = {}; hp = [(0.0, a)]; klaar = set()
    while hp:
        d, u = heapq.heappop(hp)
        if u in klaar:
            continue
        klaar.add(u)
        if u == b:
            break
        for v, w in buren.get(u, ()):
            if d + w < dist.get(v, 1e18):
                dist[v] = d + w; vor[v] = u; heapq.heappush(hp, (d + w, v))
    if b not in dist:
        print("GEEN pad"); return 1
    pad = [b]
    while pad[-1] != a:
        pad.append(vor[pad[-1]])
    pad.reverse()
    pts = [[round(coords[r][0], 5), round(coords[r][1], 5)] for r in pad]
    print(f"pad: {dist[b]:.1f} km, {len(pts)} punten")
    if args.schrijf:
        doc = {"type": "FeatureCollection", "features": [{
            "type": "Feature",
            "properties": {"naam": "Trans-Alaska Pipeline (TAPS), Prudhoe Bay PS1 -> Valdez Marine Terminal",
                           "km": round(dist[b], 1), "punten": len(pts),
                           "bron": "OpenStreetMap-bijdragers (ODbL), us-alaska-extract, man_made=pipeline substance=oil name~Trans-Alaska",
                           "gereedschap": "maak_leidingbeen_olie_prudhoebay_cherrypoint.py"},
            "geometry": {"type": "LineString", "coordinates": pts}}]}
        os.makedirs(os.path.dirname(UIT), exist_ok=True)
        with open(UIT, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False)
        print(f"geschreven: {UIT} ({os.path.getsize(UIT)/1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
