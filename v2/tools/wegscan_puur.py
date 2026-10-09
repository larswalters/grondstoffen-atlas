#!/usr/bin/env python3
"""wegscan_puur.py — maak_stroombeen_weg.py met een EIGEN pure-Python PBF-lezer als wegbron.

WAAROM DIT BESTAAT (golf 7, 2026-10-09). `pyosmium` kan op deze machine zijn DLL niet laden
(Windows-beleid voor toepassingsbeheer: "Dit bestand is geblokkeerd") en de Overpass-spiegels
geven HTTP 500/406. Het Geofabrik-pad en --bron overpass werken dus niet. Vier agenten schreven
daarom elk een eigen wrapper; dit is die wrapper, één keer, voor elk profiel.

WAT HET DOET. Het draait maak_stroombeen_weg.main() ongewijzigd, met als enige verschil de kraan:
`_ways_uit_overpass` wordt vervangen door een lezer die het .osm.pbf-DATABESTAND rechtstreeks
leest (numpy + zlib; laadt geen geblokkeerde DLL). Zelfde way-vorm (id/soort/ref/pts/regio), zelfde
`fl.weg_houden`-filter (door main gepatcht, dus inclusief de eindklassen en de access-uitsluiting),
zelfde corridorvenster (`fl._raakt_venster`) en dezelfde 12-km-eindklassenbeperking als het
Geofabrik-pad: alleen een andere kraan op dezelfde leiding. Alles stroomafwaarts (corridor_keten,
snoei, lengtetoets, GeoJSON) is letterlijk hetzelfde.

Draaien (vanuit de repo-root, PYTHONIOENCODING=utf-8):
    python v2/tools/wegscan_puur.py --profiel <sleutel>      # alle extracts uit het profiel
    PBF_MAX_BLOBS=300 python v2/tools/wegscan_puur.py ...    # alleen een test: eerste 300 blokken, geen cache

TIJD. ~1,5–5 min per GB pbf (Texas 268 s, Zuid-Afrika ~3 min); het resultaat staat in
v2/build-cache/ais/graaf/<profiel>-pbfways-<hash>.json, een tweede run is dus meteen klaar.
Het is single-threaded: neem een weg-slot (en een reus-slot bij china, india, indonesie, japan,
brazilie, canada, italie, groot-brittannie, australie, de-bayern, us-california, us-texas).

BEPERKING. De lezer verwacht een gesorteerde pbf (nodes vóór ways) met DenseNodes, zoals
Geofabrik ze levert, en leest alleen highway-ways; relaties (bv. verboden afslagen) zijn niet nodig
voor dit gereedschap. Een extract zonder DenseNodes geeft "0 nodes" — dan meldt hij dat luid.
"""
import hashlib
import json
import os
import struct
import sys
import time
import zlib

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import maak_stroombeen_weg as m  # noqa: E402

CACHE_DIR = os.path.join(m.fl.CACHE, "ais", "graaf")


# ── protobuf-primitieven ──────────────────────────────────────────────────────
def rv(buf, i):
    r = 0
    s = 0
    while True:
        b = buf[i]
        i += 1
        r |= (b & 0x7F) << s
        if b < 0x80:
            return r, i
        s += 7


def fields(buf):
    i = 0
    n = len(buf)
    while i < n:
        k, i = rv(buf, i)
        f, w = k >> 3, k & 7
        if w == 0:
            v, i = rv(buf, i)
            yield f, v
        elif w == 2:
            ln, i = rv(buf, i)
            yield f, buf[i:i + ln]
            i += ln
        elif w == 1:
            yield f, buf[i:i + 8]
            i += 8
        elif w == 5:
            yield f, buf[i:i + 4]
            i += 4
        else:
            raise ValueError("wire %d" % w)


def packed_varints(buf):
    out = []
    i = 0
    n = len(buf)
    while i < n:
        v, i = rv(buf, i)
        out.append(v)
    return out


def zz(v):
    return (v >> 1) ^ -(v & 1)


def np_varints(buf):
    b = np.frombuffer(buf, dtype=np.uint8)
    if b.size == 0:
        return np.zeros(0, dtype=np.uint64)
    ends = np.flatnonzero(b < 0x80)
    starts = np.concatenate(([0], ends[:-1] + 1))
    ln = ends - starts + 1
    val = np.zeros(len(ends), dtype=np.uint64)
    for k in range(int(ln.max())):
        mk = ln > k
        val[mk] |= (b[starts[mk] + k].astype(np.uint64) & np.uint64(0x7F)) << np.uint64(7 * k)
    return val


def np_sint(buf):
    v = np_varints(buf)
    return (v >> np.uint64(1)).astype(np.int64) ^ -((v & np.uint64(1)).astype(np.int64))


def blobs(path):
    with open(path, "rb") as f:
        while True:
            h = f.read(4)
            if len(h) < 4:
                return
            hl = struct.unpack(">I", h)[0]
            hdr = f.read(hl)
            typ = None
            ds = 0
            for fn, v in fields(hdr):
                if fn == 1:
                    typ = v.decode()
                elif fn == 3:
                    ds = v
            data = f.read(ds)
            raw = None
            for fn, v in fields(data):
                if fn == 1:
                    raw = v
                elif fn == 3:
                    raw = zlib.decompress(v)
            yield typ, raw


def prim(raw):
    st = []
    groups = []
    gran = 100
    lo = 0
    la = 0
    for fn, v in fields(raw):
        if fn == 1:
            st = [s for f2, s in fields(v) if f2 == 1]
        elif fn == 2:
            groups.append(v)
        elif fn == 17:
            gran = v
        elif fn == 19:
            la = zz(v)
        elif fn == 20:
            lo = zz(v)
    return st, groups, gran, la, lo


# ── de scan ───────────────────────────────────────────────────────────────────
def scan(pbf, bb, houd_fn, regio, max_blobs=None):
    """bb = (west, east, south, north). Eén doorloop: eerst de dense nodes in bb, dan de highway-ways."""
    W, E, S, N = bb
    ids_l, lat_l, lon_l = [], [], []
    node_ids = lat_i = lon_i = None
    ways = []
    t0 = time.time()
    nb = 0
    n_nodes_in = 0
    n_hw = 0
    n_hw_keep = 0
    fase = "nodes"
    for typ, raw in blobs(pbf):
        if typ != "OSMData":
            continue
        nb += 1
        if max_blobs and nb > max_blobs:
            break
        st, groups, gran, la, lo = prim(raw)
        for g in groups:
            for fn, msg in fields(g):
                if fn == 2:  # dense nodes
                    ids = lats = lons = None
                    for f2, v in fields(msg):
                        if f2 == 1:
                            ids = np.cumsum(np_sint(v))
                        elif f2 == 8:
                            lats = np.cumsum(np_sint(v))
                        elif f2 == 9:
                            lons = np.cumsum(np_sint(v))
                    latd = (la + gran * lats) * 1e-9
                    lond = (lo + gran * lons) * 1e-9
                    mk = (lond >= W) & (lond <= E) & (latd >= S) & (latd <= N)
                    if mk.any():
                        ids_l.append(ids[mk])
                        lat_l.append(np.round(latd[mk] * 1e7).astype(np.int32))
                        lon_l.append(np.round(lond[mk] * 1e7).astype(np.int32))
                        n_nodes_in += int(mk.sum())
        if fase == "nodes":
            has_ways = False
            for g in groups:
                for fn, _ in fields(g):
                    if fn == 3:
                        has_ways = True
                        break
                if has_ways:
                    break
            if has_ways:
                fase = "ways"
                if not ids_l:
                    print(f"  ⚠️ 0 nodes in bbox {bb} (geen DenseNodes of de bbox ligt buiten dit extract)", flush=True)
                    return []
                node_ids = np.concatenate(ids_l)
                lat_i = np.concatenate(lat_l)
                lon_i = np.concatenate(lon_l)
                o = np.argsort(node_ids, kind="stable")
                node_ids, lat_i, lon_i = node_ids[o], lat_i[o], lon_i[o]
                ids_l = lat_l = lon_l = None
                print(f"  nodes klaar na {nb} blokken, {time.time() - t0:.0f}s: {len(node_ids):,} nodes in bb", flush=True)
        if fase == "ways" and node_ids is not None:
            try:
                ihw = st.index(b"highway")
            except ValueError:
                continue
            wl = []
            for g in groups:
                for fn, wmsg in fields(g):
                    if fn != 3:
                        continue
                    wid = None
                    ks = vs = None
                    refs = None
                    for f2, v in fields(wmsg):
                        if f2 == 1:
                            wid = v
                        elif f2 == 2:
                            ks = packed_varints(v)
                        elif f2 == 3:
                            vs = packed_varints(v)
                        elif f2 == 8:
                            refs = v
                    if not ks or ihw not in ks or not refs:
                        continue
                    n_hw += 1
                    tags = {st[k].decode("utf-8", "replace"): st[x].decode("utf-8", "replace") for k, x in zip(ks, vs)}
                    houd, _ = houd_fn(tags)
                    if not houd:
                        continue
                    wl.append((wid, tags, np.cumsum(np_sint(refs))))
            if not wl:
                continue
            allref = np.concatenate([w[2] for w in wl])
            idx = np.searchsorted(node_ids, allref).clip(0, len(node_ids) - 1)
            found = node_ids[idx] == allref
            pos = 0
            for wid, tags, r in wl:
                k = len(r)
                f = found[pos:pos + k]
                ix = idx[pos:pos + k]
                pos += k
                if f.sum() < 2:
                    continue
                n_hw_keep += 1
                seg = []
                segs = []
                for j in range(k):
                    if f[j]:
                        seg.append([round(lon_i[ix[j]] * 1e-7, 7), round(lat_i[ix[j]] * 1e-7, 7)])
                    else:
                        if len(seg) >= 2:
                            segs.append(seg)
                        seg = []
                if len(seg) >= 2:
                    segs.append(seg)
                for si, s in enumerate(segs):
                    ways.append({"id": wid if si == 0 else wid * 100 + si,
                                 "soort": (tags.get("highway") or "").strip(),
                                 "ref": (tags.get("ref") or "").strip(),
                                 "pts": s, "regio": regio})
        if nb % 200 == 0:
            print(f"  blok {nb} ({fase}) {time.time() - t0:.0f}s · nodes in bb {n_nodes_in:,} · hw-ways {n_hw:,} · bewaard {len(ways):,}", flush=True)
    print(f"  scan klaar: {nb} blokken, {time.time() - t0:.0f}s, {len(ways):,} way-delen", flush=True)
    return ways


def uit_pbf(bb, timeout=0):
    """Vervangt m._ways_uit_overpass: alle extracts van het profiel, gefilterd op het corridorvenster."""
    profiel = m._PROFIEL_NAAM
    extracts = list(m.CORRIDOR["extracts"])
    sl = hashlib.sha1(repr((bb, extracts, m.VIA_PUNTEN, m.CORRIDOR["vensterKm"], m.EIND_KLASSEN, m.CORRIDOR_KLASSEN,
                            m.EIND_TOEGANG_PRIVAAT, m.EIND_STRAAL_KM, "puur-v1")).encode()).hexdigest()[:12]
    cpad = os.path.join(CACHE_DIR, f"{profiel}-pbfways-{sl}.json")
    max_blobs = int(os.environ.get("PBF_MAX_BLOBS", "0")) or None
    if os.path.exists(cpad) and not max_blobs:
        print(f"  pbf-cache hit: {cpad}", flush=True)
        return json.load(open(cpad, encoding="utf-8"))
    plant, kade = m.CORRIDOR["van"], m.CORRIDOR["naar"]

    def bij_eind(w):
        return any(m.fw.km((lo, la), plant) <= m.EIND_STRAAL_KM or m.fw.km((lo, la), kade) <= m.EIND_STRAAL_KM
                   for lo, la in w["pts"])

    alle = []
    for naam in extracts:
        pbf = m.fl.extract_pad(naam)
        if not os.path.exists(pbf):
            raise SystemExit(f"extract ontbreekt: {pbf} — haal hem met fetch_landnet.py --download")
        print(f"  scan {naam} ({os.path.getsize(pbf) / 1e6:,.0f} MB) in bb {tuple(round(x, 2) for x in bb)}", flush=True)
        ruw = scan(pbf, bb, m.fl.weg_houden, f"pbf-{naam}", max_blobs)
        vensters = m.fl._vensters_voor(naam)
        n0 = len(ruw)
        for w in ruw:
            if w["soort"] in m.EIND_KLASSEN and w["soort"] not in m.CORRIDOR_KLASSEN and not bij_eind(w):
                continue
            if m.fl._raakt_venster(w["pts"], vensters):
                alle.append(w)
        print(f"  {naam}: {n0:,} ruw -> {len(alle):,} ways in het corridorvenster (cumulatief)", flush=True)
    if not alle:
        raise SystemExit("⚠️ geen wegen in het corridorvenster — lege uitvoer is een fout, geen resultaat "
                         "(controleer de extracts in het profiel en de via-punten)")
    if not max_blobs:
        json.dump(alle, open(cpad, "w", encoding="utf-8"))
    return alle


if __name__ == "__main__":
    m._ways_uit_overpass = uit_pbf
    # maak_stroombeen_weg.main() leest sys.argv; dwing de bron op 'overpass' (= de vervangen kraan)
    argv = [a for a in sys.argv[1:]]
    if "--bron" in argv:
        i = argv.index("--bron")
        del argv[i:i + 2]
    sys.argv = ["maak_stroombeen_weg.py"] + argv + ["--bron", "overpass"]
    m.main()
