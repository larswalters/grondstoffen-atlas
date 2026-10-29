#!/usr/bin/env python3
"""maak_leidingbeen_olie_stanley_nederland.py — b1 en b2 van olie-stanley-nederland.

WAAROM DIT BESTAAT. Brief v2/design/routebrieven/olie-stanley-nederland.md: de Dakota Access
Pipeline (DAPL, Stanley ND -> Patoka IL) en de Energy Transfer Crude Oil Pipeline (ETCOP,
Patoka IL -> Nederland TX) staan in OSM als man_made=pipeline-ways (substance=oil). Dit script
stikt per been het kortste pad over GEDEELDE OSM-nodes tussen kop en eind; ways die in twee
extracts staan (grensways) worden op way-id ontdubbeld; ontbrekende naden tussen aparte
componenten worden gestikt tot --tol km (default 3) en gemeld.

pyosmium is op deze machine geblokkeerd; dit script leest de pbf met een kleine
pure-Python-lezer (protobuf + zlib + numpy), zoals maak_leidingbeen_olie_prudhoebay_cherrypoint.py.
Per extract wordt een cache geschreven (olie-stanley-nederland-pbfpipes-<extract>.json) met de
kandidaat-ways inclusief coordinaten; een tweede run is dan meteen klaar.

    python v2/tools/maak_leidingbeen_olie_stanley_nederland.py --verken   # namen per extract
    python v2/tools/maak_leidingbeen_olie_stanley_nederland.py --been b1 --schrijf
    python v2/tools/maak_leidingbeen_olie_stanley_nederland.py --been b2 --schrijf
"""
import sys, zlib, struct, json, math, heapq, os, argparse, re
import numpy as np

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../v2
GEO = os.path.join(WORTEL, "build-cache", "geofabrik")
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
R = 6371.0088
KANDIDAAT = re.compile(r"dakota access|dapl|etco|energy transfer crude|etcop", re.I)

LEGS = {
    "b1": {
        "extracts": ["us-north-dakota", "us-south-dakota", "us-iowa", "us-illinois"],
        "kop": (-102.4601, 48.3043),    # (lon, lat) DAPL-terminal Stanley
        "eind": (-89.0417, 38.7666),    # DAPL-eindpunt bij Patoka
        "naam": "Dakota Access Pipeline (DAPL), Stanley ND -> Patoka IL",
        "uit": "olie-stanley-nederland-leiding-dapl.geojson",
        "neem": re.compile(r"dakota access", re.I),
        "weiger": re.compile(r"vernon|marathon|plains|delivery", re.I),
    },
    "b2": {
        "extracts": ["us-illinois", "us-missouri", "us-kentucky", "us-tennessee", "us-mississippi",
                     "us-arkansas", "us-louisiana", "us-texas"],
        "kop": (-89.0407, 38.7664),     # ETCOP-begin bij Patoka
        "eind": (-93.9949, 29.9952),    # Nederland-terminal TX
        "naam": "Energy Transfer Crude Oil Pipeline (ETCOP), Patoka IL -> Nederland TX",
        "uit": "olie-stanley-nederland-leiding-etcop.geojson",
        "neem": re.compile(r"\betco|energy transfer crude", re.I),
        "weiger": re.compile(r"delivery|dakota access", re.I),
    },
}


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


def parse_ways(raw):
    strings = []; groups = []
    for f, w, v in fields(raw):
        if f == 1:
            for ff, ww, vv in fields(v):
                if ff == 1: strings.append(bytes(vv).decode("utf-8", "replace"))
        elif f == 2:
            groups.append(v)
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
            out.append((int(wid), tags, r))
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
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def scan_extract(slug):
    """kandidaat-ways (naam/operator/ref lijkt op DAPL of ETCOP) met coordinaten, gecachet."""
    cache = os.path.join(BEEN, f"olie-stanley-nederland-pbfpipes-{slug}.json")
    if os.path.exists(cache):
        with open(cache, encoding="utf-8") as f:
            return json.load(f)
    pbf = os.path.join(GEO, f"{slug}-latest.osm.pbf")
    ways = []
    for typ, raw in blobs(pbf):
        if typ == "OSMData" and b"pipeline" in raw:
            ways.extend(parse_ways(raw))
    kand = []
    for wid, tags, refs in ways:
        tekst = " ".join(tags.get(k, "") for k in ("name", "operator", "ref", "description", "alt_name"))
        if KANDIDAAT.search(tekst):
            kand.append((wid, tags, refs))
    print(f"{slug}: {len(ways)} pipeline-ways, {len(kand)} kandidaten", flush=True)
    coords = {}
    if kand:
        want = np.unique(np.concatenate([w[2] for w in kand]))
        for typ, raw in blobs(pbf):
            if typ != "OSMData":
                continue
            for ids, lat, lon in dense_nodes(raw):
                pos = np.searchsorted(want, ids)
                pos[pos >= len(want)] = 0
                m = want[pos] == ids
                for i, la, lo in zip(ids[m], lat[m], lon[m]):
                    coords[int(i)] = (float(lo), float(la))
    out = []
    for wid, tags, refs in kand:
        pts = [[int(r), coords[int(r)][0], coords[int(r)][1]] for r in refs if int(r) in coords]
        out.append({"id": wid, "tags": {k: tags[k] for k in tags if k in
                    ("name", "operator", "ref", "substance", "description", "location", "alt_name")},
                    "nodes": pts})
    with open(cache, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    return out


def verken():
    for slug in sorted({s for L in LEGS.values() for s in L["extracts"]}):
        w = scan_extract(slug)
        print(f"== {slug}: {len(w)} kandidaten")
        tel = {}
        for x in w:
            t = x["tags"]
            sl = sum(km(tuple(x['nodes'][i][1:]), tuple(x['nodes'][i + 1][1:])) for i in range(len(x['nodes']) - 1))
            key = (t.get("name"), t.get("operator"), t.get("substance"))
            a = tel.setdefault(key, [0, 0.0]); a[0] += 1; a[1] += sl
        for k, (n, l) in sorted(tel.items(), key=lambda kv: -kv[1][1]):
            print(f"   {n!s:55.55} | {k[1]!s:35.35} | {k[2]!s:8} | {n_:=n:4} ways {l:8.1f} km" if False else
                  f"   {str(k[0]):55.55} | {str(k[1]):35.35} | {str(k[2]):8} | {n:4} ways {l:8.1f} km")


def bouw(leg, tol):
    L = LEGS[leg]
    seen = {}
    for slug in L["extracts"]:
        for x in scan_extract(slug):
            t = x["tags"]
            naam = t.get("name", "") or ""
            tekst = " ".join([naam, t.get("operator", "") or "", t.get("ref", "") or ""])
            if not L["neem"].search(tekst):
                continue
            if L["weiger"].search(naam):
                continue
            if t.get("substance") != "oil":
                continue
            seen.setdefault(x["id"], x)
    print(f"{leg}: {len(seen)} unieke ways (na ontdubbelen op way-id)")
    coords = {}
    buren = {}
    for x in seen.values():
        r = x["nodes"]
        for n, lo, la in r:
            coords[n] = (lo, la)
        for i in range(1, len(r)):
            if r[i - 1][0] != r[i][0]:
                d = km(coords[r[i - 1][0]], coords[r[i][0]])
                buren.setdefault(r[i - 1][0], []).append((r[i][0], d, "way"))
                buren.setdefault(r[i][0], []).append((r[i - 1][0], d, "way"))
    # componenten + stik-kandidaten (eindpunten) binnen tol km
    comp = {}
    c = 0
    for s in buren:
        if s in comp:
            continue
        stack = [s]; comp[s] = c
        while stack:
            u = stack.pop()
            for v, _, _ in buren[u]:
                if v not in comp:
                    comp[v] = c; stack.append(v)
        c += 1
    eind = [n for n, nb in buren.items() if len(nb) == 1]
    print(f"{len(buren)} nodes, {c} componenten, {len(eind)} loshangende uiteinden")
    stiks = []
    for i in range(len(eind)):
        for j in range(i + 1, len(eind)):
            a, b = eind[i], eind[j]
            if comp[a] != comp[b]:
                d = km(coords[a], coords[b])
                if d <= tol:
                    stiks.append((d, a, b))
    stiks.sort()
    gebruikt = {}
    for d, a, b in stiks:
        if a in gebruikt or b in gebruikt:
            continue
        gebruikt[a] = b; gebruikt[b] = a
        buren[a].append((b, d, "stik")); buren[b].append((a, d, "stik"))
    kop = min(buren, key=lambda k: km(coords[k], L["kop"]))
    ein = min(buren, key=lambda k: km(coords[k], L["eind"]))
    print(f"kop-knoop {coords[kop]} op {km(coords[kop], L['kop']):.3f} km van het anker; "
          f"eind-knoop {coords[ein]} op {km(coords[ein], L['eind']):.3f} km")
    dist = {kop: 0.0}; vor = {}; hp = [(0.0, kop)]; klaar = set()
    while hp:
        d, u = heapq.heappop(hp)
        if u in klaar:
            continue
        klaar.add(u)
        if u == ein:
            break
        for v, w, _ in buren.get(u, ()):
            if d + w < dist.get(v, 1e18):
                dist[v] = d + w; vor[v] = u; heapq.heappush(hp, (d + w, v))
    if ein not in dist:
        print("GEEN pad (verhoog --tol of controleer filters)")
        return None
    pad = [ein]
    while pad[-1] != kop:
        pad.append(vor[pad[-1]])
    pad.reverse()
    stikkm = 0.0; stikken = []
    for u, v in zip(pad, pad[1:]):
        for w, d, typ in buren[u]:
            if w == v and typ == "stik":
                stikkm += d; stikken.append(round(d, 2))
                break
    pts = [[round(coords[n][0], 5), round(coords[n][1], 5)] for n in pad]
    print(f"pad: {dist[ein]:.1f} km, {len(pts)} punten, gestikte naden: {stikken} (som {stikkm:.2f} km)")
    return pts, dist[ein], stikken


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verken", action="store_true")
    ap.add_argument("--been", choices=sorted(LEGS))
    ap.add_argument("--tol", type=float, default=3.0)
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()
    if args.verken:
        verken(); return 0
    if not args.been:
        ap.error("--been b1|b2 of --verken")
    res = bouw(args.been, args.tol)
    if not res:
        return 1
    pts, d, stikken = res
    L = LEGS[args.been]
    if args.schrijf:
        doc = {"type": "FeatureCollection", "features": [{
            "type": "Feature",
            "properties": {"naam": L["naam"], "km": round(d, 1), "punten": len(pts), "gestikte_naden_km": stikken,
                           "bron": "OpenStreetMap-bijdragers (ODbL), Geofabrik-extracts, man_made=pipeline substance=oil",
                           "gereedschap": "maak_leidingbeen_olie_stanley_nederland.py"},
            "geometry": {"type": "LineString", "coordinates": pts}}]}
        uit = os.path.join(BEEN, L["uit"])
        with open(uit, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False)
        print(f"geschreven: {uit} ({os.path.getsize(uit)/1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
