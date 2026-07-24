#!/usr/bin/env python3
"""
bake_landnet.py — bakt het landnet naar v2/data/landnet.bin + landnet.json.

M25 / [LAR-491]. Zusje van `binnenwaternet()` uit bake_marnet.py, maar met een
EIGEN bestand en EIGEN (lokale) knoop-ids.

⚠️ WAAROM EEN APART BESTAND EN GEEN VIJFDE NET IN marnet.bin.
`bak_havens()` slicet de knopenlijst hard in tweeën op `zee_knopen` en telt élke
knoop daarboven als water. Spoor ligt in élke haven dichter bij dan de
dichtstbijzijnde zeeknoop, dus landknopen in dezelfde lijst betekent: elke haven
snapt op een spoorknoop en de WPI-positieschoning verplaatst havens naar "aan
het spoor". Dat is stille corruptie van `ports.json` — precies het
Rotterdam-patroon van 2026-07-20. Met een eigen bake ziet `bak_havens` het
landnet nooit.

⚠️ WAAROM LOKALE KNOOP-IDS EN GEEN OFFSET OP SCHIJF.
Een gebakken offset is een stil verlopend getal: bij een marnet-rebake schuift
`marnet.json.knopen` en wijst elke opgeslagen absolute id een net op. Varints
lezen altijd "iets", dus je krijgt plausibele onzin in plaats van een exception.
De offset wordt pas bij het koppelen berekend uit de dán geladen `marnet.json`.

Formaat = letterlijk dat van marnet.bin (drie varint-blokken):
  1. knopen      delta lon/lat (SCHAAL 1e-4 graden), zigzag-varint
  2. edges       a-delta, b-delta, lengte×10, soort (2=spoor, 3=weg),
                 aantalPunten, gabarietvlag (0 = geen maten)
  3. geometrie   punten 2..n als delta's; punt 1 = knoop a

Draaien:  python v2/tools/bake_landnet.py
          python v2/tools/bake_landnet.py --suffix=-t     (veilig proefdraaien)
"""

import argparse
import glob
import hashlib
import json
import math
import os
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import bake_marnet as bm   # noqa: E402 — varint, SCHAAL, gc_km, wrap_lon, BULK_QUANT
import audit_landdekking as audit  # noqa: E402 — de atlas-plaatsen als ankers

V2 = os.path.dirname(HERE)
CACHE = os.path.join(V2, "build-cache")
DATA = os.path.join(V2, "data")

LAND_KNOOP_KM = 10.0        # tussenknoop op lange stukken
LAND_QUANT = bm.BULK_QUANT  # ~1 m; twee vertices hierbinnen zijn hetzelfde punt
SOORT = {"spoor": 2, "weg": 3}

# De drie bestanden die deze bake met geen byte mag aanraken.
ONAANTASTBAAR = ["marnet.bin", "marnet.json", "ports.json"]


def sha(pad):
    if not os.path.exists(pad):
        return "(bestaat niet)"
    h = hashlib.sha256()
    with open(pad, "rb") as f:
        for blok in iter(lambda: f.read(1 << 20), b""):
            h.update(blok)
    return h.hexdigest()[:16]


def laad_lijnen():
    """Alle landnet_*.geojson uit de build-cache → {label: [(props, pts)]}."""
    paden = sorted(glob.glob(os.path.join(CACHE, "landnet_*.geojson")))
    paden = [p for p in paden if "-proef" not in os.path.basename(p)]
    if not paden:
        raise SystemExit("geen landnet_*.geojson in build-cache — draai eerst "
                         "run_landnet_wereld.py")
    per_label = defaultdict(list)
    bronnen = []
    for pad in paden:
        gj = json.load(open(pad, encoding="utf-8"))
        n = 0
        for f in gj["features"]:
            p = f["properties"]
            pts = [(bm.wrap_lon(lo), la) for lo, la in f["geometry"]["coordinates"]]
            if len(pts) > 1:
                per_label[p["label"]].append((p, pts))
                n += 1
        bronnen.append((os.path.basename(pad), n))
        print(f"  {os.path.basename(pad):<34} {n:7,} lijnen")
    return per_label, bronnen


def bouw(per_label):
    """Knopen op ketenuiteinden, kruisingen en elke LAND_KNOOP_KM; de geometrie
    ertussen blijft volledig, dus `edgeKm` is de echte afstand.

    ⚠️ Knoop ≠ hoekpunt. Dat is dezelfde ontkoppeling als bij het riviernet: de
    Donau haalde met knopen op 15 km elke stad binnen ±4 km van haar officiële
    rivierkilometer, omdat de lijn ertussen volledig bewaard blijft.
    """
    q = lambda p: (round(p[0] / LAND_QUANT), round(p[1] / LAND_QUANT))

    # 1 · welke cellen zijn een uiteinde of een kruising?
    tel = defaultdict(int)
    for lijnen in per_label.values():
        for _p, pts in lijnen:
            for p in (pts[0], pts[-1]):
                tel[q(p)] += 1
    binnen_tel = defaultdict(int)
    for lijnen in per_label.values():
        for _p, pts in lijnen:
            for p in pts[1:-1]:
                binnen_tel[q(p)] += 1
    knooppunt = set(tel) | {c for c, n in binnen_tel.items() if n >= 2}

    nodes, knoop_id = [], {}

    def knoop_voor(p):
        k = q(p)
        if k not in knoop_id:
            knoop_id[k] = len(nodes)
            nodes.append((p[0], p[1]))
        return knoop_id[k]

    edges, geometrie, soorten, labels = [], [], [], []
    meta = {}
    for label in sorted(per_label):
        eerste_edge = len(edges)
        km_tot = 0.0
        modus = "weg" if label.startswith("weg") else "spoor"
        for _p, pts in per_label[label]:
            start, sinds = 0, 0.0
            for i in range(1, len(pts)):
                sinds += bm.gc_km(pts[i - 1], pts[i])
                laatste = (i == len(pts) - 1)
                if not (laatste or q(pts[i]) in knooppunt or sinds >= LAND_KNOOP_KM):
                    continue
                stuk = pts[start:i + 1]
                if len(stuk) < 2:
                    continue
                a, b = knoop_voor(stuk[0]), knoop_voor(stuk[-1])
                if a != b:
                    edges.append((a, b))
                    geometrie.append(stuk)
                    soorten.append(SOORT[modus])
                    labels.append(label)
                    km_tot += sinds
                start, sinds = i, 0.0
        meta[label] = {
            "modus": modus,
            "edgeVan": eerste_edge,
            "edgeTot": len(edges),
            "km": round(km_tot, 1),
            "bron": "OSM (ODbL) via Geofabrik-regio-extract",
        }
    return nodes, edges, geometrie, soorten, labels, meta


def componenten(n_knopen, edges):
    ouder = list(range(n_knopen))

    def vind(x):
        while ouder[x] != x:
            ouder[x] = ouder[ouder[x]]
            x = ouder[x]
        return x

    for a, b in edges:
        ra, rb = vind(a), vind(b)
        if ra != rb:
            ouder[rb] = ra
    return [vind(i) for i in range(n_knopen)]


HEAL_LASTMILE_M = 200.0   # naad-cap knoop→knoop: klein op rail, ruim binnen de tier-2-norm (2 km)
HEAL_HOOFD_KM = 1000.0    # "hoofdnet" = component ≥ dit (koppelNetten's spoor-hoofdlijn-drempel)


def vind_lastmile_connectoren(nodes, edges, geometrie, labels):
    """Zoekt de naden die de last-mile-clusters aan het spoornet knopen. OSM tekent
    de spur/siding/yard-ways wél maar knoopt de knopen op de junctie niet altijd
    aan elkaar — bij Tongling hangt de smelter via een 107 m-gaatje aan een 179 km-
    netwerk, dat op zijn beurt via 16 m aan het volgende stuk. Geen echte afstand,
    een OSM-topologie-gat (de LAR-520-klasse).

    ⚠️ TRANSITIEF en VERTEX-op-VERTEX. Niet alleen naar het 1000 km-hoofdnet (dan
    mis je het 179 km-tussennet), maar greedy op de kleinste naad: knoop een
    'besmet' cluster (bevat last-mile-rail) aan het net waar het het dichtst bij
    ligt, propageer de besmetting, herhaal — zo groeit smelter→179 km→hoofdnet aan
    elkaar. De connectoren zijn coördinaatparen van BESTAANDE vertices, dus de
    HERBAKE (bouw) laat ze samenvallen — geen coördinaat-round-trip, geen edge-
    split (die brak eerder de meta), niets verzonnen: alleen naden ≤ cap.

    Geeft een lijst connector-geometrieën [[lon,lat],[lon,lat]] terug.
    """
    if not any(l == "spoor-lastmile" for l in labels):
        return []
    wortel = componenten(len(nodes), edges)
    comp_km = defaultdict(float)
    for i, (a, _b) in enumerate(edges):
        comp_km[wortel[a]] += sum(bm.gc_km(geometrie[i][j], geometrie[i][j + 1])
                                  for j in range(len(geometrie[i]) - 1))
    besmet0 = {wortel[edges[i][0]] for i, l in enumerate(labels) if l == "spoor-lastmile"}

    # cel-venster rond de besmette clusters + alle vertices daarin (per component)
    CEL = 0.002
    venster = set()
    for i, (a, _b) in enumerate(edges):
        if wortel[a] not in besmet0:
            continue
        for lo, la in geometrie[i]:
            ci, cj = round(lo / CEL), round(la / CEL)
            for di in range(-2, 3):
                for dj in range(-2, 3):
                    venster.add((ci + di, cj + dj))
    V = []                     # (comp_root, lon, lat)
    grid = defaultdict(list)
    for i, _e in enumerate(edges):
        for lo, la in geometrie[i]:
            cel = (round(lo / CEL), round(la / CEL))
            if cel in venster:
                grid[cel].append(len(V))
                V.append((wortel[edges[i][0]], lo, la))

    # kandidaat-naden: vertex ↔ vertex van een ANDER component, ≤ cap
    kand = []
    for vi, (rv, lo, la) in enumerate(V):
        ci, cj = round(lo / CEL), round(la / CEL)
        for di in range(-2, 3):
            for dj in range(-2, 3):
                for uj in grid.get((ci + di, cj + dj), ()):
                    if uj <= vi:
                        continue
                    ru, ulo, ula = V[uj]
                    if ru == rv:
                        continue
                    g = bm.gc_km((lo, la), (ulo, ula))
                    if g * 1000 <= HEAL_LASTMILE_M:
                        kand.append((g, (lo, la), (ulo, ula), rv, ru))
    kand.sort(key=lambda k: k[0])

    # greedy union met besmetting-propagatie: verbind alleen als één kant besmet is
    lu = {}
    def lf(x):
        lu.setdefault(x, x)
        while lu[x] != x:
            lu[x] = lu[lu[x]]
            x = lu[x]
        return x
    besmet = set(besmet0)
    conns = []
    for g, p, q, rv, ru in kand:
        a, b = lf(rv), lf(ru)
        if a == b:
            continue
        if a not in besmet and b not in besmet:
            continue
        lu[a] = b
        besmet.add(lf(b))
        conns.append([list(p), list(q)])
    return conns


def drop_onverbonden(nodes, edges, geometrie, soorten, labels, meta):
    """Gooit last-mile/heal-edges weg die ná de heal nóg op een klein (< hoofdnet)
    component liggen. Een losstaand spoortje is schadelijk: een aansluiting kan
    erop snappen i.p.v. op de echte lijn (dat brak Cerrejón→Bolívar). Regel: de
    pass mag alleen VERBINDEN, nooit een nieuw snap-doel maken."""
    w2 = componenten(len(nodes), edges)
    ck2 = defaultdict(float)
    for i, (a, _b) in enumerate(edges):
        ck2[w2[a]] += sum(bm.gc_km(geometrie[i][j], geometrie[i][j + 1])
                          for j in range(len(geometrie[i]) - 1))
    houd = [i for i in range(len(edges))
            if not (labels[i] in ("spoor-lastmile", "spoor-heal")
                    and ck2[w2[edges[i][0]]] < HEAL_HOOFD_KM)]
    gedropt = len(edges) - len(houd)
    if not gedropt:
        return 0
    edges[:] = [edges[i] for i in houd]
    geometrie[:] = [geometrie[i] for i in houd]
    soorten[:] = [soorten[i] for i in houd]
    labels[:] = [labels[i] for i in houd]
    nm = {}
    for idx, lab in enumerate(labels):
        if lab not in nm:
            nm[lab] = {"modus": "weg" if lab.startswith("weg") else "spoor",
                       "edgeVan": idx, "edgeTot": idx + 1, "km": 0.0,
                       "bron": meta.get(lab, {}).get("bron", "")}
        nm[lab]["edgeTot"] = idx + 1
        nm[lab]["km"] += sum(bm.gc_km(geometrie[idx][j], geometrie[idx][j + 1])
                             for j in range(len(geometrie[idx]) - 1))
    for lab in nm:
        nm[lab]["km"] = round(nm[lab]["km"], 1)
    meta.clear()
    meta.update(nm)
    # WEES-KNOPEN opruimen: de drop laat knopen zonder edge achter, en de router
    # snapt een aansluiting op de dichtste KNOOP — een 0-graads wees kaapt zo een
    # snap van de echte lijn (dat brak Cerrejón→Bolívar).
    gebruikt_kn = sorted({a for e in edges for a in e})
    if len(gebruikt_kn) < len(nodes):
        hermap = {oud: nieuw for nieuw, oud in enumerate(gebruikt_kn)}
        nodes[:] = [nodes[o] for o in gebruikt_kn]
        edges[:] = [(hermap[a], hermap[b]) for a, b in edges]
    return gedropt


def schrijf_bin(nodes, edges, geometrie, soorten, pad):
    uit = bytearray()
    x = y = 0
    for lo, la in nodes:
        qx, qy = round(lo * bm.SCHAAL), round(la * bm.SCHAAL)
        bm.varint(uit, qx - x)
        bm.varint(uit, qy - y)
        x, y = qx, qy
    pa = pb = 0
    for i, (a, b) in enumerate(edges):
        bm.varint(uit, a - pa)
        bm.varint(uit, b - pb)
        pa, pb = a, b
        km = sum(bm.gc_km(geometrie[i][j], geometrie[i][j + 1])
                 for j in range(len(geometrie[i]) - 1))
        bm.varint(uit, int(round(km * 10)))
        bm.varint(uit, soorten[i])
        bm.varint(uit, len(geometrie[i]))
        bm.varint(uit, 0)                     # gabarietvlag: spoor draagt geen maten
    n_punten = 0
    for i, (a, _b) in enumerate(edges):
        pts = geometrie[i]
        px, py = round(nodes[a][0] * bm.SCHAAL), round(nodes[a][1] * bm.SCHAAL)
        n_punten += len(pts)
        for lo, la in pts[1:]:
            qx, qy = round(lo * bm.SCHAAL), round(la * bm.SCHAAL)
            bm.varint(uit, qx - px)
            bm.varint(uit, qy - py)
            px, py = qx, qy
    with open(pad, "wb") as f:
        f.write(uit)
    return n_punten


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--suffix", default="")
    args = ap.parse_args()

    voor = {n: sha(os.path.join(DATA, n)) for n in ONAANTASTBAAR}

    print("landnet bakken uit build-cache:")
    per_label, bronnen = laad_lijnen()
    nodes, edges, geometrie, soorten, labels, meta = bouw(per_label)
    print(f"\n  {len(per_label):,} labels · {len(nodes):,} knopen · {len(edges):,} edges")
    # LAST-MILE HEAL, in twee bouw-passes: (1) vind de naden die de last-mile-
    # clusters transitief aan het net knopen, (2) voeg ze als geometrie toe en
    # HERBAK — bouw laat de connector-uiteinden (bestaande vertices) samenvallen,
    # dus alles knoopt schoon aaneen zonder edge-split of coördinaat-round-trip.
    conns = vind_lastmile_connectoren(nodes, edges, geometrie, labels)
    if conns:
        per_label.setdefault("spoor-heal", []).extend(
            ({"label": "spoor-heal", "regio": "heal", "modus": "spoor",
              "gauge": "onbekend", "hs": False}, pts) for pts in conns)
        nodes, edges, geometrie, soorten, labels, meta = bouw(per_label)
    gedropt = drop_onverbonden(nodes, edges, geometrie, soorten, labels, meta)
    print(f"  last-mile heal: {len(conns)} naden gelegd · {gedropt} onverbonden edges gedropt")

    # ⚠️ Datumgrens: MARNET had 15 knopen dubbel op lon ±180. Relevant voor
    # Tsjoekotka en Alaska; wrap_lon is bij het laden al toegepast, dit toetst het.
    fout = [i for i, (lo, _la) in enumerate(nodes) if lo < -180.0 or lo > 180.0]
    assert not fout, f"{len(fout)} knopen buiten [-180,180] — lon-normalisatie stuk"

    for i, (a, b) in enumerate(edges):
        assert 0 <= a < len(nodes) and 0 <= b < len(nodes), f"edge {i} wijst buiten de knopenlijst"

    wortel = componenten(len(nodes), edges)
    comp_km = defaultdict(float)
    graad = defaultdict(int)
    for i, (a, b) in enumerate(edges):
        km = sum(bm.gc_km(geometrie[i][j], geometrie[i][j + 1])
                 for j in range(len(geometrie[i]) - 1))
        comp_km[wortel[a]] += km
        graad[a] += 1
        graad[b] += 1
    n_comp = len(set(wortel))
    graad1 = sum(1 for i in range(len(nodes)) if graad[i] == 1)
    print(f"  {n_comp:,} componenten · grootste {max(comp_km.values()):,.0f} km · "
          f"{graad1:,} doodlopende knopen")

    bin_pad = os.path.join(DATA, f"landnet{args.suffix}.bin")
    n_punten = schrijf_bin(nodes, edges, geometrie, soorten, bin_pad)

    km_totaal = sum(m["km"] for m in meta.values())
    json_pad = os.path.join(DATA, f"landnet{args.suffix}.json")
    with open(json_pad, "w", encoding="utf-8") as f:
        json.dump({
            "schaal": bm.SCHAAL, "knopen": len(nodes), "edges": len(edges),
            "punten": n_punten, "netwerkKm": round(km_totaal, 1),
            "soorten": {"2": "spoor", "3": "weg"},
            "knoopKm": LAND_KNOOP_KM,
            "labels": [dict(naam=k, **v) for k, v in sorted(meta.items())],
            "bron": "OpenStreetMap contributors (ODbL) via Geofabrik-regio-extract",
            "bestanden": [b for b, _n in bronnen],
        }, f, ensure_ascii=False, separators=(",", ":"))

    print(f"\n  landnet{args.suffix}.bin  : {os.path.getsize(bin_pad) / 1024:,.0f} KB")
    print(f"  landnet{args.suffix}.json : {os.path.getsize(json_pad) / 1024:,.0f} KB")
    print(f"  netwerklengte : {km_totaal:,.0f} km · {n_punten:,} punten "
          f"({n_punten / max(km_totaal, 1):.2f}/km · "
          f"{len(nodes) / max(km_totaal, 1):.3f} knopen/km)")
    print(f"  bytes         : {os.path.getsize(bin_pad) / max(len(nodes), 1):.2f}/knoop · "
          f"{os.path.getsize(bin_pad) / max(len(edges), 1):.2f}/edge · "
          f"{os.path.getsize(bin_pad) / max(km_totaal, 1):.2f}/km")

    # --- aanhechting: invoer voor de redacteur, GEEN drempel ----------------
    ankers = []
    for pad in sorted(glob.glob(os.path.join(audit.DATA, "*.js"))):
        if os.path.basename(pad).startswith("_"):
            continue
        grondstof = os.path.basename(pad)[:-3]
        for n in audit.lees_nodes(pad):
            if n["type"] in audit.PLAATS_TYPES:
                n["grondstof"] = grondstof
                ankers.append(n)
    import numpy as np
    xyz = np.array([bm.to3d(lo, la) for lo, la in nodes])
    rijen = []
    for n in ankers:
        v = np.array(bm.to3d(n["lon"], n["lat"]))
        d = xyz @ v
        beste = int(np.argmax(d))
        km = bm.R_AARDE * math.acos(max(-1.0, min(1.0, float(d[beste]))))
        rijen.append({
            "id": n["id"], "naam": n["naam"], "land": n["land"],
            "type": n["type"], "grondstof": n["grondstof"],
            "knoop": beste, "afstandKm": round(km, 2),
            "componentKm": round(comp_km[wortel[beste]], 1),
            "graad": graad[beste],
        })
    aan_pad = os.path.join(DATA, f"landnet-aanhecht{args.suffix}.json")
    with open(aan_pad, "w", encoding="utf-8") as f:
        json.dump({"aantal": len(rijen), "punten": rijen}, f, ensure_ascii=False)
    ver = sorted(rijen, key=lambda r: -r["afstandKm"])
    dichtbij = sum(1 for r in rijen if r["afstandKm"] <= 25)
    print(f"\n  aanhechting   : {dichtbij:,}/{len(rijen):,} atlas-plaatsen ≤25 km van het "
          f"landnet → landnet-aanhecht{args.suffix}.json")
    print("    verste tien (de machine meet, de redacteur oordeelt):")
    for r in ver[:10]:
        print(f"      {r['afstandKm']:8,.1f} km  {r['naam'][:30]:<30} {r['land'][:18]:<18} "
              f"[{r['grondstof']}]")

    # --- de guard die deze hele opzet draagt --------------------------------
    na = {n: sha(os.path.join(DATA, n)) for n in ONAANTASTBAAR}
    print("\n  ONAANGETAST (sha256 vóór → ná):")
    for n in ONAANTASTBAAR:
        gelijk = voor[n] == na[n]
        print(f"    {n:<14} {voor[n]} → {na[n]}  {'OK' if gelijk else '⚠️ VERANDERD'}")
        assert gelijk, f"{n} is veranderd door de landbake — de scheiding is stuk"


if __name__ == "__main__":
    main()
