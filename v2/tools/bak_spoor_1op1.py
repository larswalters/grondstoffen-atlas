"""Bouw het wereld-landnet uit de 1-op-1 OSM-spoordata.

DE VOLGORDE IS DE HELE FIX, en hij is omgekeerd aan de oude pijplijn:

    oud:  filteren -> dedup -> simplify -> DAARNA knopen zoeken
    nu:   knopen zoeken op de RAUWE punten -> DAARNA geometrie verlichten

In de oude volgorde verschoven dedup en simplify de punten vóórdat de graaf
gebouwd werd, dus raakten gedeelde knopen kwijt en moesten heal-passes ze met
drempels terugraden. Dat is waar de onmogelijke bochten vandaan kwamen: bij
Guixi legde de heal een naad van 40 m die in OSM niet bestaat, en juist die
naad dwong de omkering af.

Nu staat de topologie vast vóórdat er ook maar iets vereenvoudigd wordt. De
simplify daarna raakt UITSLUITEND punten binnen een edge; de uiteinden ZIJN de
knopen en blijven per constructie staan. Vereenvoudigen kan de graaf dus niet
meer breken — het is puur een byte-maatregel op de getekende lijn.

Draaien:  python raw1op1_bak.py [--simplify-m 10] [--suffix -raw]
"""
import os, sys, json, glob, math, time, argparse
from collections import defaultdict

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HIER))
sys.path.insert(0, HIER)
os.chdir(REPO)
import bake_landnet as B

RUW = os.path.join(REPO, "v2", "build-cache", "raw1op1")
CACHE = os.path.join(REPO, "v2", "build-cache")


def dp(punten, tol_m):
    """Douglas-Peucker die de UITEINDEN altijd bewaart. Selecteert bestaande
    punten (verschuift er geen enkele), dus de las-coördinaten blijven exact."""
    if len(punten) < 3 or tol_m <= 0:
        return punten
    tol = tol_m / 1000.0
    houd = [False] * len(punten)
    houd[0] = houd[-1] = True
    stapel = [(0, len(punten) - 1)]
    while stapel:
        a, b = stapel.pop()
        if b <= a + 1:
            continue
        pa, pb = punten[a], punten[b]
        c = math.cos(math.radians((pa[1] + pb[1]) / 2))
        vx, vy = (pb[0] - pa[0]) * c, pb[1] - pa[1]
        vv = vx * vx + vy * vy
        beste, best_d = -1, -1.0
        for i in range(a + 1, b):
            p = punten[i]
            wx, wy = (p[0] - pa[0]) * c, p[1] - pa[1]
            if vv <= 0:
                d = math.hypot(wx, wy)
            else:
                t = max(0.0, min(1.0, (wx * vx + wy * vy) / vv))
                d = math.hypot(wx - t * vx, wy - t * vy)
            if d > best_d:
                beste, best_d = i, d
        if beste > 0 and best_d * 111.32 > tol:
            houd[beste] = True
            stapel.append((a, beste))
            stapel.append((beste, b))
    return [p for p, h in zip(punten, houd) if h]


def anker_xyz():
    """Alle plekken waar een stroom het spoor op moet: de atlas-knopen uit
    data/*.js plus de aangewezen aansluitingen. Een doodlopende tak bij zo'n
    punt is een LAADSPOOR en moet blijven."""
    import audit_landdekking as audit
    pts = []
    for pad in glob.glob(os.path.join(audit.DATA, "*.js")):
        if os.path.basename(pad).startswith("_"):
            continue
        for n in audit.lees_nodes(pad):
            pts.append((n["lon"], n["lat"]))
    aan = os.path.join(B.DATA, "aansluitingen.json")
    if os.path.exists(aan):
        d = json.load(open(aan, encoding="utf-8"))
        rijen = d if isinstance(d, list) else d.get("aansluitingen", [])
        for a in rijen:
            if a.get("plek"):
                pts.append(tuple(a["plek"]))
            for g in (a.get("gemeten") or {}).values():
                if g.get("bij"):
                    pts.append(tuple(g["bij"]))
    return pts


def snoei_bladeren(nodes, edges, geometrie, soorten, labels, straal_km=3.0):
    """Doodlopende takken weg — die kunnen per definitie nooit deel zijn van een
    pad TUSSEN twee punten, dus geen enkele route verandert. Uitzondering: een
    tak binnen `straal_km` van een atlas-plek of aansluiting; dat is precies het
    laadspoor waar een stroom het net op komt.

    Iteratief, want een tak van drie edges wordt pas blad nadat zijn punt weg is.
    """
    import numpy as np
    from scipy.spatial import cKDTree
    ank = anker_xyz()
    boom = cKDTree(np.array([B.bm.to3d(lo, la) for lo, la in ank]))
    knoop_xyz = np.array([B.bm.to3d(lo, la) for lo, la in nodes])
    straal = 2 * math.sin(straal_km / (2 * B.bm.R_AARDE))      # koorde
    beschermd = set(int(i) for i in
                    np.nonzero(boom.query(knoop_xyz, k=1)[0] <= straal)[0])
    print(f"  {len(ank):,} ankers · {len(beschermd):,} knopen beschermd "
          f"(≤{straal_km:.0f} km)", flush=True)

    graad = defaultdict(int)
    for a, b in edges:
        graad[a] += 1
        graad[b] += 1
    levend = [True] * len(edges)
    ronde = 0
    while True:
        ronde += 1
        weg = [i for i, (a, b) in enumerate(edges)
               if levend[i]
               and ((graad[a] == 1 and a not in beschermd)
                    or (graad[b] == 1 and b not in beschermd))]
        if not weg:
            break
        for i in weg:
            levend[i] = False
            a, b = edges[i]
            graad[a] -= 1
            graad[b] -= 1
        print(f"    ronde {ronde}: {len(weg):,} bladeren weg", flush=True)
    houd = [i for i in range(len(edges)) if levend[i]]
    print(f"  edges {len(edges):,} -> {len(houd):,} "
          f"({len(houd)/len(edges)*100:.0f}%)", flush=True)
    return ([edges[i] for i in houd], [geometrie[i] for i in houd],
            [soorten[i] for i in houd], [labels[i] for i in houd])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simplify-m", type=float, default=10.0)
    ap.add_argument("--snoei-km", type=float, default=0.0,
                    help="doodlopende takken snoeien, ankers binnen deze "
                         "straal beschermd (0 = niet snoeien)")
    ap.add_argument("--suffix", default="-raw")
    args = ap.parse_args()
    t0 = time.time()

    per_label = defaultdict(list)
    gezien = set()
    dubbel = 0
    paden = sorted(glob.glob(os.path.join(RUW, "*.geojson")))
    print(f"{len(paden)} extracts inlezen ...", flush=True)
    for n, pad in enumerate(paden, 1):
        gj = json.load(open(pad, encoding="utf-8"))
        for f in gj["features"]:
            p = f["properties"]
            wid = p.get("wayId")
            if wid in gezien:          # extracts overlappen (china ⊂ asia, enz.)
                dubbel += 1
                continue
            gezien.add(wid)
            pts = [(lo, la) for lo, la in f["geometry"]["coordinates"]]
            if len(pts) > 1:
                per_label[p["label"]].append((p, pts))
        if n % 25 == 0:
            print(f"  {n}/{len(paden)} · {len(gezien):,} ways", flush=True)
    print(f"  {len(gezien):,} unieke ways ({dubbel:,} dubbel uit overlappende "
          f"extracts) · {time.time()-t0:.0f} s", flush=True)

    # de wegcorridors en het handwerk blijven ongewijzigd meelopen; de
    # last-mile-inhaak vervalt (die haalde service-spoor lokaal binnen — dat
    # zit nu overal al in)
    for extra in (os.path.join(CACHE, "landnet_weg.geojson"),
                  os.path.join(B.DATA, "landnet-handmatig.geojson")):
        if not os.path.exists(extra):
            continue
        gj = json.load(open(extra, encoding="utf-8"))
        for f in gj["features"]:
            p = f["properties"]
            pts = [(B.bm.wrap_lon(lo), la) for lo, la in f["geometry"]["coordinates"]]
            if len(pts) > 1:
                per_label[p["label"]].append((p, pts))
        print(f"  + {os.path.basename(extra)}: {len(gj['features'])} lijnen", flush=True)

    print("graaf bouwen op de RAUWE punten (exacte las = OSM-topologie) ...", flush=True)
    nodes, edges, geometrie, soorten, labels, meta = B.bouw(per_label)
    print(f"  {len(nodes):,} knopen · {len(edges):,} edges · {time.time()-t0:.0f} s",
          flush=True)

    if args.snoei_km > 0:
        print("doodlopende takken snoeien (kunnen nooit deel van een pad zijn) ...",
              flush=True)
        edges, geometrie, soorten, labels = snoei_bladeren(
            nodes, edges, geometrie, soorten, labels, args.snoei_km)

    voor = sum(len(g) for g in geometrie)
    if args.simplify_m > 0:
        print(f"geometrie verlichten binnen elke edge ({args.simplify_m:.0f} m, "
              f"uiteinden vast) ...", flush=True)
        for i in range(len(geometrie)):
            geometrie[i] = dp(geometrie[i], args.simplify_m)
    na = sum(len(g) for g in geometrie)
    print(f"  punten {voor:,} -> {na:,} ({na/max(voor,1)*100:.0f}%)", flush=True)

    wortel = B.componenten(len(nodes), edges)
    comp_km = defaultdict(float)
    graad = defaultdict(int)
    km_totaal = 0.0
    for i, (a, b) in enumerate(edges):
        km = sum(B.bm.gc_km(geometrie[i][j], geometrie[i][j + 1])
                 for j in range(len(geometrie[i]) - 1))
        comp_km[wortel[a]] += km
        km_totaal += km
        graad[a] += 1
        graad[b] += 1
    print(f"  {len(set(wortel)):,} componenten · grootste {max(comp_km.values()):,.0f} km"
          f" · netwerk {km_totaal:,.0f} km", flush=True)

    bin_pad = os.path.join(B.DATA, f"landnet{args.suffix}.bin")
    n_punten = B.schrijf_bin(nodes, edges, geometrie, soorten, bin_pad)
    with open(os.path.join(B.DATA, f"landnet{args.suffix}.json"), "w",
              encoding="utf-8") as f:
        json.dump({
            "schaal": B.bm.SCHAAL, "knopen": len(nodes), "edges": len(edges),
            "punten": n_punten, "netwerkKm": round(km_totaal, 1),
            "soorten": {"2": "spoor", "3": "weg"}, "knoopKm": B.LAND_KNOOP_KM,
            "labels": [dict(naam=k, **v) for k, v in sorted(meta.items())],
            "bron": "OpenStreetMap contributors (ODbL) — 1-op-1: topologie uit "
                    "gedeelde OSM-nodes, geen dedup/heal; simplify uitsluitend "
                    "binnen een edge",
            "bestanden": ["raw1op1/*.geojson"],
        }, f, ensure_ascii=False, separators=(",", ":"))
    print(f"\n  landnet{args.suffix}.bin : {os.path.getsize(bin_pad)/1024:,.0f} KB"
          f" · {n_punten:,} punten ({n_punten/max(km_totaal,1):.2f}/km)")
    print(f"  klaar in {time.time()-t0:.0f} s")


main()
