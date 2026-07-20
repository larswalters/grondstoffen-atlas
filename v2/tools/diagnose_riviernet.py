#!/usr/bin/env python3
"""
diagnose_riviernet.py — waarom is het binnenwaternet 10.670 losse fragmenten? (LAR-520)

De diagnose die het issue voorschrijft VÓÓR er een naadmechanisme komt: geen
shotgun-naadradius, maar eerst de gatverdeling tussen component-uiteinden meten.
Volgt de geest van `diagnose_keten.py`, maar op het HELE riviernet i.p.v. één keten.

Wat het meet, op de ECHTE bake (`data/marnet.bin` + `data/marnet.json`), dus op
exact de graaf die naar de browser gaat en die de 10.670 componenten oplevert:

  1. de componenten van het bulk-riviernet (aantal, km- en knoop-verdeling, top-20)
  2. de gatverdeling: per component-uiteinde (graad-1-knoop) de hemelsbrede afstand
     tot de dichtstbijzijnde knoop van een ANDER component
  3. de naadradius-sweep: hoeveel componenten blijven er over als je alle gaten
     ≤ r aan elkaar naait, voor r = 0,25 … 10 km (reproduceert de panel-indicatie
     2 km → 2.594 · 5 km → 1.668, of corrigeert 'm met een gemeten getal)
  4. de acceptatie-ankers: in welk component vallen Rotterdam, Nijmegen, Duisburg,
     New Orleans, Baton Rouge, Memphis, Cincinnati — en wat is het gat ertussen
  5. de zee↔rivier-scheiding: 0 edges tussen zeenet en riviernet (valkuil 2)

⚠️ De gaten hier zijn HEMELSBREED. Een naad hoort over water te lopen (valkuil 1);
dat is mechanisme-werk, niet deze meting. Dit rapport zegt WELKE gaten er zijn en
hoe groot — niet welke je veilig mag naaien.

Het riviernet = de edges van de 8 `bulk-*`-regio's in `meta.vaarwegen` (bulk:true).
Dat isoleert het zuiver van het zeenet én van de oude M23-binnenwaterzones
(Suez/Panama/Seaway zijn soort=1 maar hangen juist wél aan het zeenet).

Draaien:
  python v2/tools/diagnose_riviernet.py
"""

import json
import math
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(V2, "data")

R_AARDE = 6371.0088


def gc_km(a, b):
    lo1, la1 = a
    lo2, la2 = b
    p1, p2 = math.radians(la1), math.radians(la2)
    dp = math.radians(la2 - la1)
    dl = math.radians(lo2 - lo1)
    x = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R_AARDE * math.asin(min(1.0, math.sqrt(x)))


def naar_3d(lo, la):
    lon, lat = math.radians(lo), math.radians(la)
    cl = math.cos(lat)
    return (cl * math.cos(lon), math.sin(lat), -cl * math.sin(lon))


# --- marnet.bin lezen (blok 1 knopen + blok 2 edges; blok 3 geometrie overslaan) ---
class Lezer:
    def __init__(self, buf):
        self.b = buf
        self.p = 0

    def volgende(self):
        res, factor = 0, 1
        while True:
            byte = self.b[self.p]
            self.p += 1
            res += (byte & 0x7F) * factor
            if not (byte & 0x80):
                break
            factor *= 128
        half = res >> 1
        return half if res % 2 == 0 else -half - 1


def _suffix():
    if "--suffix" in sys.argv:
        return sys.argv[sys.argv.index("--suffix") + 1]
    return ""


def laad_graaf(met_geometrie=False):
    sf = _suffix()
    meta = json.load(open(os.path.join(DATA, f"marnet{sf}.json"), encoding="utf-8"))
    buf = open(os.path.join(DATA, f"marnet{sf}.bin"), "rb").read()
    schaal = meta["schaal"]
    n_knopen, n_edges = meta["knopen"], meta["edges"]
    lz = Lezer(buf)

    nodes = [None] * n_knopen
    node_int = [None] * n_knopen            # gekwantiseerde ints (voor blok 3)
    x = y = 0
    for i in range(n_knopen):
        x += lz.volgende()
        y += lz.volgende()
        nodes[i] = (x / schaal, y / schaal)
        node_int[i] = (x, y)

    edge_a = [0] * n_edges
    edge_b = [0] * n_edges
    edge_km = [0.0] * n_edges
    edge_soort = [0] * n_edges
    geom_n = [0] * n_edges
    a = b = 0
    for i in range(n_edges):
        a += lz.volgende()
        b += lz.volgende()
        edge_a[i], edge_b[i] = a, b
        edge_km[i] = lz.volgende() / 10.0
        edge_soort[i] = lz.volgende()
        geom_n[i] = lz.volgende()           # aantal geometriepunten
        if lz.volgende() == 1:              # gabarietvlag → 4 maten volgen
            for _ in range(4):
                lz.volgende()

    geometrie = None
    if met_geometrie:
        # blok 3: per edge de punten 2..n als delta's; punt 1 = knoop a.
        geometrie = [None] * n_edges
        for i in range(n_edges):
            px, py = node_int[edge_a[i]]
            pts = [(px / schaal, py / schaal)]
            for _ in range(geom_n[i] - 1):
                px += lz.volgende()
                py += lz.volgende()
                pts.append((px / schaal, py / schaal))
            geometrie[i] = pts
    return meta, nodes, edge_a, edge_b, edge_km, edge_soort, geometrie


# --- union-find -------------------------------------------------------------
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1
        return True


def histo(waarden, randen, label):
    print(f"\n  {label}:")
    n = len(waarden)
    ws = sorted(waarden)
    lo = 0
    for hi in randen:
        c = sum(1 for w in ws if lo <= w < hi)
        bar = "#" * int(60 * c / max(n, 1))
        print(f"    {lo:5.1f}–{hi:<5.1f} km  {c:6,}  {bar}")
        lo = hi
    c = sum(1 for w in ws if w >= lo)
    print(f"    {lo:5.1f}+      km  {c:6,}  {'#' * int(60 * c / max(n, 1))}")
    if ws:
        med = ws[len(ws) // 2]
        print(f"    mediaan {med:.2f} km · p90 {ws[int(0.9 * len(ws))]:.2f} · "
              f"max {ws[-1]:.2f} km")


def main():
    diep = "--projectie" in sys.argv
    meta, nodes, edge_a, edge_b, edge_km, edge_soort, geometrie = laad_graaf(diep)
    vw = meta["vaarwegen"]

    # 1 · het bulk-riviernet: welke edges, welke knopen -----------------------
    bulk_edges = []
    for r, v in vw.items():
        if v.get("bulk"):
            bulk_edges.extend(v["edges"])
    bulk_edges = sorted(set(bulk_edges))
    rivier_knopen = set()
    for ei in bulk_edges:
        rivier_knopen.add(edge_a[ei])
        rivier_knopen.add(edge_b[ei])

    print("=" * 78)
    print("RIVIERNET-DIAGNOSE (LAR-520) — op data/marnet.bin (?v=039)")
    print("=" * 78)
    print(f"bulk-riviernet: {len(bulk_edges):,} edges · {len(rivier_knopen):,} knopen · "
          f"{sum(edge_km[ei] for ei in bulk_edges):,.0f} km")

    # 2 · componenten ---------------------------------------------------------
    dsu = DSU(len(nodes))
    for ei in bulk_edges:
        dsu.union(edge_a[ei], edge_b[ei])

    comp_knopen = {}
    for k in rivier_knopen:
        comp_knopen.setdefault(dsu.find(k), []).append(k)
    comp_km = {}
    for ei in bulk_edges:
        c = dsu.find(edge_a[ei])
        comp_km[c] = comp_km.get(c, 0.0) + edge_km[ei]

    comps = sorted(comp_knopen, key=lambda c: comp_km.get(c, 0), reverse=True)
    kms = sorted((comp_km.get(c, 0.0) for c in comps))
    print(f"\ncomponenten: {len(comps):,}")
    print(f"  km-mediaan {kms[len(kms) // 2]:.2f} · "
          f"gemiddeld {sum(kms) / len(kms):.1f} · grootste {kms[-1]:,.0f} km")

    # graad binnen het riviernet (voor uiteinden = graad-1-knopen)
    graad = {k: 0 for k in rivier_knopen}
    for ei in bulk_edges:
        graad[edge_a[ei]] += 1
        graad[edge_b[ei]] += 1

    # havens per component: ports.json heeft al de riviersnap (knoopRivier +
    # afstandRivierKm) uit LAR-518. Een haven telt mee voor een component als
    # haar riviersnap ≤ DREMPEL km ligt (het issue rekent op 25 km).
    ports = json.load(open(os.path.join(DATA, f"ports{_suffix()}.json"), encoding="utf-8"))
    DREMPEL = 25.0
    comp_havens = {}
    knoop_comp = {}
    for k in rivier_knopen:
        knoop_comp[k] = dsu.find(k)
    haven_in_comp = 0
    for kr, dr in zip(ports["knoopRivier"], ports["afstandRivierKm"]):
        if kr is None or dr is None or dr > DREMPEL:
            continue
        c = knoop_comp.get(kr)
        if c is None:
            continue
        comp_havens[c] = comp_havens.get(c, 0) + 1
        haven_in_comp += 1
    print(f"\n  havens (≤{DREMPEL:.0f} km riviersnap): {haven_in_comp:,} van {ports['aantal']:,} "
          f"vallen in {len(comp_havens):,} componenten")
    print(f"  → {ports['aantal'] - haven_in_comp:,} havens hebben geen riviercomponent "
          f"binnen {DREMPEL:.0f} km (kunnen nu geen binnenvaartroute krijgen)")

    print("\n  top-20 componenten (km · knopen · uiteinden · havens):")
    for c in comps[:20]:
        ks = comp_knopen[c]
        uit = sum(1 for k in ks if graad[k] == 1)
        print(f"    {comp_km.get(c, 0):9,.1f} km · {len(ks):6,} knopen · "
              f"{uit:4} uiteinden · {comp_havens.get(c, 0):3} havens")

    # 3 · KDTree over de riviernet-knopen -------------------------------------
    try:
        from scipy.spatial import cKDTree
        import numpy as np
    except ImportError:
        print("\n⚠️ scipy/numpy nodig voor de gatverdeling. `pip install scipy numpy`.")
        return

    rk = list(rivier_knopen)
    idx_van = {k: i for i, k in enumerate(rk)}
    pts3d = np.array([naar_3d(*nodes[k]) for k in rk])
    boom = cKDTree(pts3d)
    comp_van = [dsu.find(k) for k in rk]

    # koorde-straal voor een grootcirkel van r km op de eenheidsbol
    def koorde(r_km):
        return 2 * math.sin(min(math.pi, r_km / R_AARDE) / 2)

    # uiteinden = graad-1-knopen; plus alle knopen van piepkleine componenten
    uiteinden = [i for i, k in enumerate(rk) if graad[k] == 1]
    print(f"\n  uiteinden (graad-1-knopen): {len(uiteinden):,}")

    # gatverdeling: per uiteinde de dichtstbijzijnde knoop van een ander component
    gaten = []
    MAXR = 10.0
    for i in uiteinden:
        d, j = boom.query(pts3d[i], k=8)
        for dist, jj in zip(d, j):
            if comp_van[jj] != comp_van[i]:
                gaten.append(gc_km(nodes[rk[i]], nodes[rk[jj]]))
                break
    histo(gaten, [0.05, 0.1, 0.25, 0.5, 1, 2, 3, 5], "gatverdeling per uiteinde (hemelsbreed)")

    # 4 · naadradius-sweep ----------------------------------------------------
    # alle cross-component paren (uiteinde -> willekeurige knoop) binnen MAXR,
    # als kleinste gat per componentpaar; daarna union-find sweepen over r.
    paar_gat = {}
    for i in uiteinden:
        buren = boom.query_ball_point(pts3d[i], koorde(MAXR))
        ci = comp_van[i]
        for jj in buren:
            cj = comp_van[jj]
            if cj == ci:
                continue
            d = gc_km(nodes[rk[i]], nodes[rk[jj]])
            sleutel = (ci, cj) if ci < cj else (cj, ci)
            if sleutel not in paar_gat or d < paar_gat[sleutel]:
                paar_gat[sleutel] = d

    # zelfde, maar ALLEEN uiteinde↔uiteinde (beide graad-1): de VEILIGE naad —
    # twee losse uiteinden die elkaar naderen zijn vrijwel altijd één doorgaande
    # vaarweg die OSM niet op één node legde. Endpoint→midlijn is riskanter
    # (kan een meander kortsluiten), dus die splitsen we eruit.
    uit_set = set(uiteinden)
    paar_gat_uu = {}
    for i in uiteinden:
        buren = boom.query_ball_point(pts3d[i], koorde(MAXR))
        ci = comp_van[i]
        for jj in buren:
            if jj not in uit_set or comp_van[jj] == ci:
                continue
            d = gc_km(nodes[rk[i]], nodes[rk[jj]])
            sleutel = (ci, comp_van[jj]) if ci < comp_van[jj] else (comp_van[jj], ci)
            if sleutel not in paar_gat_uu or d < paar_gat_uu[sleutel]:
                paar_gat_uu[sleutel] = d

    def sweep_tel(pairs, r):
        sweep = DSU(len(nodes))
        for ei in bulk_edges:
            sweep.union(edge_a[ei], edge_b[ei])
        for (ca, cb), d in pairs.items():
            if d <= r:
                sweep.union(ca, cb)
        return len({sweep.find(k) for k in rivier_knopen})

    print(f"\n  naadradius-sweep — componenten na naaien:")
    print(f"    {'r (km)':>8}  {'alle gaten':>12}  {'uiteinde↔uiteinde':>18}")
    for r in (0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 10.0):
        print(f"    {r:8.2f}  {sweep_tel(paar_gat, r):12,}  {sweep_tel(paar_gat_uu, r):18,}")

    # 5 · acceptatie-ankers ---------------------------------------------------
    ankers = {
        "Rotterdam":   (4.45, 51.91),
        "Nijmegen":    (5.85, 51.85),
        "Duisburg":    (6.73, 51.45),
        "New Orleans": (-90.06, 29.95),
        "Baton Rouge": (-91.19, 30.44),
        "Memphis":     (-90.06, 35.13),
        "Cincinnati":  (-84.51, 39.09),
    }
    print("\n  acceptatie-ankers (dichtstbijzijnde riviernet-knoop):")
    anker_comp = {}
    for naam, (lo, la) in ankers.items():
        d, i = boom.query(naar_3d(lo, la))
        k = rk[i]
        c = comp_van[i]
        anker_comp[naam] = c
        print(f"    {naam:<12} snap {gc_km((lo, la), nodes[k]):6.2f} km → "
              f"component {comp_km.get(c, 0):8,.1f} km / {len(comp_knopen[c]):,} knopen")

    def zelfde(a, b):
        return "JA" if anker_comp[a] == anker_comp[b] else "nee"
    print("\n  in één component?")
    print(f"    Rotterdam ↔ Nijmegen : {zelfde('Rotterdam', 'Nijmegen')}")
    print(f"    Rotterdam ↔ Duisburg : {zelfde('Rotterdam', 'Duisburg')}")
    print(f"    New Orleans ↔ Baton Rouge : {zelfde('New Orleans', 'Baton Rouge')}")
    print(f"    New Orleans ↔ Memphis     : {zelfde('New Orleans', 'Memphis')}")
    print(f"    New Orleans ↔ Cincinnati  : {zelfde('New Orleans', 'Cincinnati')}")

    # 6 · zee↔rivier-scheiding (valkuil 2) ------------------------------------
    zee_knopen = set()
    for ei in range(len(edge_a)):
        if edge_soort[ei] == 0:
            zee_knopen.add(edge_a[ei])
            zee_knopen.add(edge_b[ei])
    overlap = rivier_knopen & zee_knopen
    kruis = sum(1 for ei in bulk_edges
                if edge_a[ei] in zee_knopen or edge_b[ei] in zee_knopen)
    print(f"\n  zee↔rivier-scheiding: {len(overlap)} gedeelde knopen · "
          f"{kruis} bulk-edges die een zeeknoop raken  (moet 0/0 zijn)")

    # 7 · projectie: landt een uiteinde OP de lijn van een ander component? -----
    # Dat is de tier-1-toets: niet hemelsbreed uiteinde↔uiteinde, maar het
    # uiteinde geprojecteerd op de brongeometrie van een ANDER component. Klein
    # = een gemiste confluentie/breuk in dezelfde vaarweg (over water per
    # constructie, veilig te naaien); dit onderscheidt zich van een sluipweg.
    if geometrie is None:
        print("\n(voor de projectie-analyse: draai met --projectie)")
        return
    from shapely import STRtree
    from shapely.geometry import LineString, Point

    lijnen, lijn_comp = [], []
    for ei in bulk_edges:
        g = geometrie[ei]
        if len(g) >= 2:
            lijnen.append(LineString(g))
            lijn_comp.append(dsu.find(edge_a[ei]))
    boom_l = STRtree(lijnen)
    RAD_DEG = 0.02                          # ~2 km bbox-venster om te filteren

    proj = []
    for i in uiteinden:
        p = Point(nodes[rk[i]])
        ci = comp_van[i]
        best = None
        for li in boom_l.query(p.buffer(RAD_DEG)):
            if lijn_comp[li] == ci:
                continue
            ln = lijnen[li]
            np_ = ln.interpolate(ln.project(p))
            d = gc_km((p.x, p.y), (np_.x, np_.y))
            if best is None or d < best[0]:
                best = (d, lijn_comp[li])
        if best is not None:
            proj.append((best[0], ci, best[1]))

    dists = [d for d, _c, _t in proj]
    histo(dists, [0.05, 0.1, 0.25, 0.5, 1.0], "uiteinde → projectie op de lijn van een ander component")

    print("\n  tier-1 heal-sweep (componenten na naaien van uiteinden die ≤ r OP een andere lijn landen):")
    print(f"    {'r (km)':>8}  {'componenten':>12}")
    for r in (0.05, 0.1, 0.25, 0.5, 1.0):
        heal = DSU(len(nodes))
        for ei in bulk_edges:
            heal.union(edge_a[ei], edge_b[ei])
        # union op componenten via een representatieve knoop per component
        rep = {}
        for k in rivier_knopen:
            rep.setdefault(dsu.find(k), k)
        for d, ci, ct in proj:
            if d <= r:
                heal.union(rep[ci], rep[ct])
        over = len({heal.find(k) for k in rivier_knopen})
        print(f"    {r:8.2f}  {over:12,}")


if __name__ == "__main__":
    main()
