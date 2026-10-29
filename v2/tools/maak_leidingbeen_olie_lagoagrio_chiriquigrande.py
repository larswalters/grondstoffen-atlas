#!/usr/bin/env python3
"""maak_leidingbeen_olie_lagoagrio_chiriquigrande.py - leidingbenen van olie-lagoagrio-chiriquigrande.

b1: SOTE (Sistema Oleoducto Trans-Ecuatoriano), Lago Agrio -> Balao, gestikt uit OSM-ways (man_made=pipeline,
substance=oil) uit de lokale Geofabrik-extract ecuador. Uitgesloten: ways met Poliducto/Pesados/OCP/San Miguel/
Pascual in de naam. Stikken = kortste pad over een vertex-graaf; een uiteinde mag tot 3 km naar een vertex van een
andere way springen (naadkosten x3); naamloze ways zonder operator kosten x3 (ze kunnen OCP zijn).
RESERVE (niet in de keten, zie brief 7): PTP, Muelle 1-steiger Charco Azul -> Chiriqui Grande (panama-extract).
Uitvoer: FeatureCollection (LineString, [lon,lat], 5 decimalen) in v2/build-cache/ais/graaf/.
Draaien: PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_olie_lagoagrio_chiriquigrande.py
"""
import heapq, json, math, os
from collections import defaultdict
import numpy as np
import osmium

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEO = os.path.join(WORTEL, "build-cache", "geofabrik")
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
R = 6371.0088
TOL_KM = 3.0
PEN_NAAMLOOS = 3.0
EXCL = ("poliducto", "pesados", "ocp", "san miguel", "pascual")


def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def lengte(c):
    return sum(hav(c[i], c[i + 1]) for i in range(len(c) - 1))


class Scan(osmium.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.w = []

    def way(self, w):
        t = w.tags
        if t.get("man_made") == "pipeline" and t.get("substance") == "oil":
            try:
                self.w.append({"id": w.id, "tags": dict(t), "c": [(n.lat, n.lon) for n in w.nodes]})
            except Exception:
                pass


def laad(regio):
    s = Scan()
    s.apply_file(os.path.join(GEO, f"{regio}-latest.osm.pbf"), locations=True)
    return s.w


def stik(ways, start, einde, excl=(), pen=1.0, tol=TOL_KM):
    ws = [w for w in ways if not any(x in w["tags"].get("name", "").lower() for x in excl)]
    V, own, vid = [], [], {}
    for wi, w in enumerate(ws):
        for k, p in enumerate(w["c"]):
            vid[(wi, k)] = len(V)
            V.append(p)
            own.append(wi)
    P = np.array(V)
    own = np.array(own)
    adj = defaultdict(list)
    for wi, w in enumerate(ws):
        t = w["tags"]
        m = 1.0 if (t.get("name") or t.get("operator")) else pen
        c = w["c"]
        for k in range(len(c) - 1):
            a, b = vid[(wi, k)], vid[(wi, k + 1)]
            d = hav(c[k], c[k + 1])
            adj[a].append((b, d * m, wi))
            adj[b].append((a, d * m, wi))
    for wi, w in enumerate(ws):
        for k in (0, len(w["c"]) - 1):
            a = vid[(wi, k)]
            p = V[a]
            x = np.radians(P[:, 1] - p[1]) * math.cos(math.radians(p[0]))
            y = np.radians(P[:, 0] - p[0])
            dist = R * np.hypot(x, y)
            best = {}
            for j in np.where((dist <= tol) & (own != wi))[0]:
                o = int(own[j])
                if o not in best or dist[j] < dist[best[o]]:
                    best[o] = int(j)
            for o, j in best.items():
                adj[a].append((j, dist[j] * 3 + 0.01, None))
                adj[j].append((a, dist[j] * 3 + 0.01, None))
    near = lambda p: int(np.argmin([hav(q, p) for q in V]))
    s, e = near(start), near(einde)
    dist, prev, pq = {s: 0.0}, {}, [(0.0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, 1e18):
            continue
        if u == e:
            break
        for v, c, wi in adj[u]:
            nd = d + c
            if nd < dist.get(v, 1e18):
                dist[v] = nd
                prev[v] = (u, wi)
                heapq.heappush(pq, (nd, v))
    if e not in dist:
        raise SystemExit("geen pad")
    pad, u = [], e
    while u != s:
        p, wi = prev[u]
        pad.append((p, u, wi))
        u = p
    pad.reverse()
    pts = [V[s]]
    ids, naden = [], []
    for p, u, wi in pad:
        if wi is None:
            naden.append(round(hav(V[p], V[u]), 2))
        elif not ids or ids[-1] != ws[wi]["id"]:
            ids.append(ws[wi]["id"])
        pts.append(V[u])
    sch = [pts[0]]
    for q in pts[1:]:
        if q != sch[-1]:
            sch.append(q)
    return sch, ids, [n for n in naden if n > 0.05]


def schrijf(naam, pts, ids, naden, bron, uit):
    coords = [[round(p[1], 5), round(p[0], 5)] for p in pts]
    km = lengte(pts)
    doc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"naam": naam, "km": round(km, 2), "punten": len(coords), "way_ids": ids, "naden_km": naden,
                       "bron": bron},
        "geometry": {"type": "LineString", "coordinates": coords}}]}
    json.dump(doc, open(os.path.join(BEEN, uit), "w", encoding="utf-8"), ensure_ascii=False)
    print(f"{uit}: {km:.1f} km, {len(coords)} punten, {len(ids)} ways, naden>0,05 km: {naden}, "
          f"begin {pts[0][0]:.4f},{pts[0][1]:.4f} eind {pts[-1][0]:.4f},{pts[-1][1]:.4f}")


if __name__ == "__main__":
    os.makedirs(BEEN, exist_ok=True)
    ec = laad("ecuador")
    pts, ids, naden = stik(ec, (0.078, -76.880), (0.9701, -79.6795), excl=EXCL, pen=PEN_NAAMLOOS)
    schrijf("SOTE Lago Agrio -> Balao (OSM-stitch)", pts, ids, naden,
            "OpenStreetMap-bijdragers (ODbL), man_made=pipeline substance=oil, extract ecuador",
            "olie-lagoagrio-chiriquigrande-leiding-lagoagrio-balao.geojson")
    pa = laad("panama")
    pts, ids, naden = stik(pa, (8.2157556, -82.8749695), (8.9540, -82.1192), pen=1.5)
    schrijf("PTP Charco Azul Muelle 1 -> Chiriqui Grande (OSM-stitch, RESERVE)", pts, ids, naden,
            "OpenStreetMap-bijdragers (ODbL), man_made=pipeline substance=oil, extract panama",
            "olie-lagoagrio-chiriquigrande-leiding-ptp-reserve.geojson")
