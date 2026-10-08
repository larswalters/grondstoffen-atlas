#!/usr/bin/env python
"""bak_stroombundel.py — de STROMENBUNDEL: één afgeleid artefact uit alle
gebakken stromen, met twee gebakken LOD-niveaus, voor de bol.

WAAROM DIT BESTAAT (2026-10-08, visuele fase / LAR-617, ontwerp in
v2/design/atlas-product-golf1.md). De bol laadde 182 stroomroute-*.json twee
keer (382 verzoeken, 51,7 MB) en tekende elk been als eigen object (~2.300 draw
calls, 12,7 M driehoeken uit 1,06 M punten op meters-korrel) — op een telefoon
9–14 fps. De bron van waarheid blijft `stroomroute-*.json` (besluit 2026-08-06:
bakken is geen deliverable, de routes worden NIET herbakken); dit script leidt
er een compact bundelbestand uit af, zoals `bake_landnet.py` uit de extracts.

WAT HET SCHRIJFT (allemaal in v2/data/):
  stromen.json               de index: per stroom en per been de metadata,
                             de bbox, en de offsets in de bins; sites (gloed);
                             sha1 van alle bronnen (voor --check).
  stromen-basis.bin          L0 (DP 3 km, grootcirkel-verdicht 100 km) en
                             L1 (DP 200 m, verdicht 25 km) van ALLE grondbenen,
                             mét de originele cumulatieve km per punt.
  stromen-fijn-<gs>.bin      per grondstof de volle resolutie (alle bronpunten,
                             verdicht 5 km = exact wat stroomroute.js tekende),
                             lui geladen door de browser bij inzoomen.

CODERING = het landnet.bin-patroon: zigzag-varint (7 bits per byte, little-
endian, continuatiebit 0x80; zigzag even = +, oneven = −), lon/lat gekwantiseerd
op 1e-5° (≈ 1 m), delta per punt binnen een been (eerste punt t.o.v. 0), lon
ONTWIKKELD over de datumgrens (continu > 180° waar nodig; de bol rekent met
sin/cos en is periodiek). Per been: [n] dan n × [Δlon Δlat] (fijn) of
n × [Δlon Δlat Δkm] (basis, km × 100 = 10 m-korrel).

LUCHTBENEN staan niet in de bins: hun boog komt runtime uit beenPunten()
(stroomstijl.js) tussen kop en staart, precies zoals nu. De index draagt
`kopStaart`.

WERKREGEL: elke gebakken of geregistreerde stroom gaat in DEZELFDE commit door
`bash v2/tools/bak_stromen.sh bundel`; `--check` herrekent de sha1's en faalt
luid bij drift (de generator↔uitvoer-klasse: cu-guixi-spoor, 741 m).
Tweemaal draaien is byte-identiek (geen tijdstempel in de uitvoer).

Gebruik (vanuit de repo-root):
  python v2/tools/bak_stroombundel.py            # bakken
  python v2/tools/bak_stroombundel.py --toets    # bakken + tellingen/pariteit
  python v2/tools/bak_stroombundel.py --check    # alleen drift-controle (exit 1)
"""
import argparse
import hashlib
import json
import math
import os
import sys

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HIER, "..", "data"))
REGISTER = os.path.join(DATA, "stromen-register.json")
INDEX = os.path.join(DATA, "stromen.json")
BASIS = os.path.join(DATA, "stromen-basis.bin")

FORMAAT = 1
SCHAAL = 100000          # 1e-5° ≈ 1,1 m
KM_SCHAAL = 100          # 10 m
R_KM = 6371.0
MAX_BENEN = 1024         # de informatietextuur in de browser is 1024 breed

# De niveaus: [naam, DP-tolerantie km, grootcirkel-verdichting km]. De
# verdichting hoort bij de hoogte waarop het niveau getekend wordt: de koorde
# van een segment zakt (L²/8R) onder het oppervlak — 100 km → 0,2 km zakking
# waar 1 css-px ≥ 2,5 km is; 25 km → 12 m; 5 km → 0,5 m (de ijking van
# 2026-07-28 in stroomroute.verdicht()).
NIVEAUS = [("L0", 3.0, 100.0), ("L1", 0.2, 25.0)]
FIJN_VERDICHT_KM = 5.0


# ── varint, zoals landnet.js hem leest ───────────────────────────────────────
def varint(uit, v):
    v = int(v)
    zz = (v << 1) if v >= 0 else ((-v) << 1) - 1
    while True:
        b = zz & 0x7F
        zz >>= 7
        if zz:
            uit.append(b | 0x80)
        else:
            uit.append(b)
            return


# ── meetkunde ────────────────────────────────────────────────────────────────
def ontwikkel_lon(pts):
    """Maak de lon continu over de datumgrens (sprong > 180° → ±360)."""
    uit = [list(pts[0])]
    for p in pts[1:]:
        lon, lat = p[0], p[1]
        vorige = uit[-1][0]
        while lon - vorige > 180:
            lon -= 360
        while lon - vorige < -180:
            lon += 360
        uit.append([lon, lat])
    return uit


def gc_km(a, b):
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    s = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R_KM * math.asin(min(1.0, math.sqrt(s)))


def cum_km(pts):
    c = [0.0]
    for a, b in zip(pts, pts[1:]):
        c.append(c[-1] + gc_km(a, b))
    return c


def douglas_peucker(pts, tol_km):
    """Iteratief, in een lokale equirectangulaire projectie, uiteinden vast.
    Geeft de indices van de bewaarde BRONpunten (er wordt geen punt verzonnen)."""
    n = len(pts)
    if n < 3 or tol_km <= 0:
        return list(range(n))
    arr = np.asarray(pts, float)
    lat_mid = math.radians(float(arr[:, 1].mean()))
    x = (arr[:, 0] - arr[0, 0]) * math.cos(lat_mid) * 111.195
    y = arr[:, 1] * 111.195
    P = np.stack([x, y], 1)
    keep = np.zeros(n, bool)
    keep[0] = keep[-1] = True
    stack = [(0, n - 1)]
    while stack:
        a, b = stack.pop()
        if b - a < 2:
            continue
        A, B = P[a], P[b]
        AB = B - A
        L2 = float(AB @ AB)
        Q = P[a + 1:b]
        if L2 < 1e-12:
            d = np.linalg.norm(Q - A, axis=1)
        else:
            t = np.clip(((Q - A) @ AB) / L2, 0, 1)
            d = np.linalg.norm(Q - (A + t[:, None] * AB), axis=1)
        i = int(np.argmax(d))
        if d[i] > tol_km:
            k = a + 1 + i
            keep[k] = True
            stack.append((a, k))
            stack.append((k, b))
    return [int(i) for i in np.flatnonzero(keep)]


def verdicht(pts, kms, max_km):
    """Grootcirkel-verdichting zoals stroomroute.verdicht(): tussen twee punten
    verder dan max_km uit elkaar komen ceil(d/max_km)−1 tussenpunten op de
    grootcirkel. De km-stand van een tussenpunt wordt lineair tussen de twee
    bronpunten gelegd (zelfde fasering als de volle lijn, besluit 11)."""
    uit = [pts[0]]
    uit_km = [kms[0]]
    for i in range(1, len(pts)):
        (lo1, la1), (lo2, la2) = pts[i - 1], pts[i]
        p1 = (math.radians(la1), math.radians(lo1))
        p2 = (math.radians(la2), math.radians(lo2))
        d = 2 * math.asin(min(1.0, math.sqrt(
            math.sin((p2[0] - p1[0]) / 2) ** 2 +
            math.cos(p1[0]) * math.cos(p2[0]) * math.sin((p2[1] - p1[1]) / 2) ** 2)))
        n = math.ceil((d * R_KM) / max_km)
        if n > 1 and d > 1e-9:
            sd = math.sin(d)
            for k in range(1, n):
                f = k / n
                a = math.sin((1 - f) * d) / sd
                b = math.sin(f * d) / sd
                x = a * math.cos(p1[0]) * math.cos(p1[1]) + b * math.cos(p2[0]) * math.cos(p2[1])
                y = a * math.cos(p1[0]) * math.sin(p1[1]) + b * math.cos(p2[0]) * math.sin(p2[1])
                z = a * math.sin(p1[0]) + b * math.sin(p2[0])
                lon = math.degrees(math.atan2(y, x))
                lat = math.degrees(math.atan2(z, math.hypot(x, y)))
                # terug naar de ontwikkelde lon-tak van het bronsegment
                while lon - lo1 > 180:
                    lon -= 360
                while lon - lo1 < -180:
                    lon += 360
                uit.append([lon, lat])
                uit_km.append(kms[i - 1] + f * (kms[i] - kms[i - 1]))
        uit.append(pts[i])
        uit_km.append(kms[i])
    return uit, uit_km


def niveau_punten(pts, kms, tol_km, verdicht_km):
    idx = douglas_peucker(pts, tol_km)
    sub = [pts[i] for i in idx]
    sub_km = [kms[i] for i in idx]
    return verdicht(sub, sub_km, verdicht_km)


# ── bronnen ──────────────────────────────────────────────────────────────────
def sha1(pad):
    h = hashlib.sha1()
    with open(pad, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def laad_register():
    with open(REGISTER, encoding="utf-8") as f:
        reg = json.load(f)
    op_schijf = sorted(n for n in os.listdir(DATA) if n.startswith("stroomroute-") and n.endswith(".json"))
    bekend = {s["bestand"] for s in reg["stromen"]} | {u["bestand"] for u in reg.get("uitgesloten", [])}
    onbekend = [n for n in op_schijf if n not in bekend]
    ontbreekt = [s["bestand"] for s in reg["stromen"] if s["bestand"] not in op_schijf]
    if onbekend or ontbreekt:
        sys.exit(f"REGISTER KLOPT NIET — niet geregistreerd en niet uitgesloten: {onbekend}; "
                 f"geregistreerd maar niet op schijf: {ontbreekt}. Registreren is een besluit, geen glob.")
    sleutels = [s["sleutel"] for s in reg["stromen"]]
    if len(set(sleutels)) != len(sleutels):
        sys.exit("REGISTER KLOPT NIET — dubbele sleutel")
    return reg


def grondstof_van(stroom_id):
    return str(stroom_id or "").split("-")[0]


# ── bakken ───────────────────────────────────────────────────────────────────
def bak(reg, toets=False):
    bronnen = {}
    stromen_uit = []
    basis_blokken = {naam: bytearray() for naam, _, _ in NIVEAUS}
    basis_tel = {naam: 0 for naam, _, _ in NIVEAUS}
    fijn_blok = {}        # grondstof → bytearray
    fijn_tel = {}         # grondstof → punten
    totalen = {"stromen": 0, "benen": 0, "stippel": 0, "markers": 0, "sites": 0,
               "puntenBron": 0, "puntenFijn": 0}
    km_per_mod_bron = {}
    km_afwijking = []     # (stroom, been, bron km, gemeten km)
    been_index = 0

    for s in reg["stromen"]:
        pad = os.path.join(DATA, s["bestand"])
        bronnen[s["bestand"]] = sha1(pad)
        with open(pad, encoding="utf-8") as f:
            doc = json.load(f)
        if doc.get("versie") != 2 or doc.get("punt_formaat") != "lonlat":
            sys.exit(f"{s['bestand']}: onbekend contract (versie {doc.get('versie')}, {doc.get('punt_formaat')})")
        if grondstof_van(doc.get("stroom")) != s["grondstof"]:
            sys.exit(f"{s['bestand']}: grondstof in het register ({s['grondstof']}) ≠ id-prefix van "
                     f"`stroom` ({doc.get('stroom')}) — de kleur zou stil verkeerd worden (stroomstijl.grondstofVan)")
        gs = s["grondstof"]
        fijn_blok.setdefault(gs, bytearray())
        fijn_tel.setdefault(gs, 0)

        benen_uit = []
        km_mod = {}
        for b in doc.get("benen", []):
            if been_index >= MAX_BENEN:
                sys.exit(f"meer dan {MAX_BENEN} benen — vergroot de informatietextuur in stroomlijn.js én hier")
            mod = b["modaliteit"]
            km_mod[mod] = km_mod.get(mod, 0.0) + float(b.get("km") or 0.0)
            km_per_mod_bron[mod] = km_per_mod_bron.get(mod, 0.0) + float(b.get("km") or 0.0)
            ruw = b.get("punten") or []
            totalen["puntenBron"] += len(ruw)
            entry = {
                "i": been_index, "modaliteit": mod, "naam": b.get("naam", ""),
                "stippel": bool(b.get("stippel")), "km": b.get("km"),
                "vertaktVan": b.get("vertakt_van"),
            }
            if mod == "lucht" or len(ruw) < 2:
                # geen bin-geometrie: de boog komt runtime uit beenPunten()
                entry["kopStaart"] = [[ruw[0][0], ruw[0][1]], [ruw[-1][0], ruw[-1][1]]] if ruw else None
                entry["bbox"] = None
                entry["L0"] = entry["L1"] = entry["fijn"] = None
            else:
                pts = ontwikkel_lon(ruw)
                kms = cum_km(pts)
                lons = [p[0] for p in pts]
                lats = [p[1] for p in pts]
                entry["bbox"] = [round(min(lons), 4), round(min(lats), 4), round(max(lons), 4), round(max(lats), 4)]
                # basis-niveaus
                for naam, tol, vd in NIVEAUS:
                    np_, nk = niveau_punten(pts, kms, tol, vd)
                    n_ = schrijf_been(basis_blokken[naam], np_, nk)
                    entry[naam] = [basis_tel[naam], n_]
                    basis_tel[naam] += n_
                # fijn = alle bronpunten + verdichting 5 km (zoals stroomroute.verdicht)
                fp, fk = verdicht(pts, kms, FIJN_VERDICHT_KM)
                n_ = schrijf_been(fijn_blok[gs], fp, None)
                entry["fijn"] = [fijn_tel[gs], n_]
                fijn_tel[gs] += n_
                totalen["puntenFijn"] += n_
                # toets: de koorde-som van het fijn-niveau tegen de bron-km
                if toets and b.get("km"):
                    gemeten = kms[-1]
                    if abs(gemeten - float(b["km"])) > 0.001 * float(b["km"]) + 0.05:
                        km_afwijking.append((s["sleutel"], b.get("naam", ""), float(b["km"]), gemeten))
            benen_uit.append(entry)
            totalen["benen"] += 1
            if b.get("stippel"):
                totalen["stippel"] += 1
            been_index += 1

        markers = [{"naam": m.get("naam", ""), "lon": m["lon"], "lat": m["lat"]} for m in doc.get("markers", [])]
        totalen["markers"] += len(markers)
        totalen["stromen"] += 1
        stromen_uit.append({
            "sleutel": s["sleutel"], "stroom": doc.get("stroom"), "grondstof": gs,
            "titel": doc.get("titel"), "routebrief": doc.get("routebrief"),
            "kmPerModaliteit": {k: round(v, 1) for k, v in km_mod.items()},
            "benen": benen_uit, "markers": markers,
        })

    # sites uit de gloedbestanden (alleen level = site; normalisatie blijft runtime)
    sites = []
    for naam in sorted(n for n in os.listdir(DATA) if n.startswith("gloednodes-") and n.endswith(".json")):
        pad = os.path.join(DATA, naam)
        bronnen[naam] = sha1(pad)
        with open(pad, encoding="utf-8") as f:
            g = json.load(f)
        gs = naam[len("gloednodes-"):-len(".json")]
        for k in g.get("knopen", []):
            if k.get("level") != "site":
                continue
            sites.append({"grondstof": (k.get("grondstof") or [gs])[0], "lon": k["lon"], "lat": k["lat"],
                          "gewicht": k.get("gewicht") or 1, "naam": k.get("naam", "")})
    totalen["sites"] = len(sites)

    # basis.bin = L0-blok gevolgd door L1-blok; de index draagt de byte-grenzen
    basis = bytearray()
    niveaus = {}
    for naam, tol, vd in NIVEAUS:
        van = len(basis)
        basis += basis_blokken[naam]
        niveaus[naam] = {"tolKm": tol, "verdichtKm": vd, "bestand": "stromen-basis.bin",
                         "byteVan": van, "byteTot": len(basis), "punten": basis_tel[naam]}
    niveaus["fijn"] = {"tolKm": 0, "verdichtKm": FIJN_VERDICHT_KM, "bestand": "stromen-fijn-<grondstof>.bin"}
    totalen["puntenL0"] = basis_tel["L0"]
    totalen["puntenL1"] = basis_tel["L1"]

    fijn_uit = {}
    for gs, blok in sorted(fijn_blok.items()):
        bestand = f"stromen-fijn-{gs}.bin"
        with open(os.path.join(DATA, bestand), "wb") as f:
            f.write(blok)
        fijn_uit[gs] = {"bestand": bestand, "bytes": len(blok), "punten": fijn_tel[gs]}
    with open(BASIS, "wb") as f:
        f.write(basis)

    index = {
        "formaat": FORMAAT,
        "toelichting": "GEGENEREERD door v2/tools/bak_stroombundel.py uit stromen-register.json + stroomroute-*.json "
                       "+ gloednodes-*.json — niet met de hand bewerken; bron van waarheid blijven die bestanden.",
        "codering": {"schaal": SCHAAL, "kmSchaal": KM_SCHAAL, "lonOntwikkeld": True,
                     "basisPunt": ["dlon", "dlat", "dkm"], "fijnPunt": ["dlon", "dlat"]},
        "bron": dict(sorted(bronnen.items())),
        "totalen": totalen,
        "niveaus": niveaus,
        "fijn": fijn_uit,
        "stromen": stromen_uit,
        "sites": sites,
    }
    with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
        json.dump(index, f, ensure_ascii=False, separators=(",", ":"))
    return index, km_per_mod_bron, km_afwijking


def schrijf_been(uit, pts, kms):
    # ⚠️ Opeenvolgende punten die ná kwantisatie samenvallen worden overgeslagen:
    # een segment van lengte nul geeft in de vertex-shader van LineMaterial
    # normalize(vec2(0)) = NaN (review 2026-10-08: 310 zulke segmenten in de
    # fijne bins, uit dubbele bronpunten). De bron blijft ongewijzigd; alleen
    # de bundel slaat het duplicaat over. Geeft het aantal geschreven punten.
    q = []
    for i, p in enumerate(pts):
        qx, qy = round(p[0] * SCHAAL), round(p[1] * SCHAAL)
        if q and q[-1][0] == qx and q[-1][1] == qy:
            continue
        q.append((qx, qy, None if kms is None else round(kms[i] * KM_SCHAAL)))
    varint(uit, len(q))
    x = y = k = 0
    for qx, qy, qk in q:
        varint(uit, qx - x)
        varint(uit, qy - y)
        x, y = qx, qy
        if qk is not None:
            varint(uit, qk - k)
            k = qk
    return len(q)


# ── drift-controle ───────────────────────────────────────────────────────────
def check():
    if not os.path.exists(INDEX):
        print("stromen.json ontbreekt — bak eerst")
        return 1
    with open(INDEX, encoding="utf-8") as f:
        index = json.load(f)
    drift = []
    for naam, h in index["bron"].items():
        pad = os.path.join(DATA, naam)
        if not os.path.exists(pad):
            drift.append(f"{naam}: weg")
        elif sha1(pad) != h:
            drift.append(f"{naam}: gewijzigd sinds de bundel")
    with open(REGISTER, encoding="utf-8") as f:
        reg = json.load(f)
    if [s["sleutel"] for s in reg["stromen"]] != [s["sleutel"] for s in index["stromen"]]:
        drift.append("stromen-register.json: andere stromen/volgorde dan de bundel")
    nieuw = [n for n in os.listdir(DATA) if n.startswith(("stroomroute-", "gloednodes-")) and n.endswith(".json")
             and n not in index["bron"] and n not in {u["bestand"] for u in reg.get("uitgesloten", [])}]
    drift += [f"{n}: nieuw, niet in de bundel" for n in nieuw]
    if drift:
        print("BUNDEL LOOPT ACHTER OP DE BRON — draai `bash v2/tools/bak_stromen.sh bundel`:")
        for d in drift:
            print("  ·", d)
        return 1
    print("bundel is in de pas met de bron (sha1 van", len(index["bron"]), "bestanden)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="alleen drift-controle, exit 1 bij drift")
    ap.add_argument("--toets", action="store_true", help="bakken + tellingen en pariteit")
    args = ap.parse_args()
    if args.check:
        sys.exit(check())

    reg = laad_register()
    index, km_bron, km_afw = bak(reg, toets=args.toets)
    t = index["totalen"]
    print(f"stromen.json: {t['stromen']} stromen · {t['benen']} benen · {t['stippel']} stippel · "
          f"{t['markers']} markers · {t['sites']} sites")
    print(f"punten: bron {t['puntenBron']:,} · L0 {t['puntenL0']:,} · L1 {t['puntenL1']:,} · fijn {t['puntenFijn']:,}")
    print(f"stromen-basis.bin: {os.path.getsize(BASIS):,} B (L0 {index['niveaus']['L0']['byteTot']:,} B)")
    fijn_bytes = sum(v["bytes"] for v in index["fijn"].values())
    print(f"fijn-bins: {len(index['fijn'])} bestanden · {fijn_bytes:,} B samen · "
          f"stromen.json {os.path.getsize(INDEX):,} B")
    if args.toets:
        print("km per modaliteit (bron):", {k: round(v) for k, v in sorted(km_bron.items())})
        if km_afw:
            print(f"⚠️ {len(km_afw)} benen waarvan de koorde-som > 0,1 % van de bron-km afwijkt (de bron-km komt uit de "
                  f"baker van dat been, niet uit de punten; ter info):")
            for s, n, bk, gk in sorted(km_afw, key=lambda r: -abs(r[2] - r[3]))[:8]:
                print(f"   · {s} · {n[:50]} · bron {bk:.1f} · punten {gk:.1f} km")
        # segment-toets: geen segment langer dan 2× de verdichtingsmaat (de datumgrens-val)
        fouten = 0
        for s in index["stromen"]:
            for b in s["benen"]:
                if b.get("bbox") and (b["bbox"][2] - b["bbox"][0] > 360):
                    fouten += 1
                    print("   · bbox breder dan 360°:", s["sleutel"], b["naam"])
        print("bbox-toets:", "ok" if not fouten else f"{fouten} fouten")
    sys.exit(0)


if __name__ == "__main__":
    main()
