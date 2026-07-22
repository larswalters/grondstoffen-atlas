#!/usr/bin/env python3
"""
fetch_landnet.py — het LANDNET (spoor, later weg) uit de Geofabrik-extracts.

M25 / [LAR-491]. Zusje van `fetch_waterways.py --bulk`, met dezelfde steiger
(parallelle osmium-scan, per-extract cachevingerafdruk, ontdubbeling op way-id)
en drie stappen die water niet nodig had:

  1. KETENVOUWEN — OSM knipt spoor op elke tagwissel (China 238.592 ways →
     ~10.000 ketens). Zonder vouwen wordt het knopenaantal bepaald door het
     aantal way-uiteinden en niet door je knoopinterval: `binnenwaternet()`
     maakt van élk lijn-uiteinde een knoop.
  2. DEDUP VAN PARALLELLE SPOREN — dubbelspoor ligt in OSM als twee losse
     lijnen (`tracks=2` staat in China op 5.406 van 238.592 ways). Zonder
     samenvouwen meet de lengtetoets — onze enige echte controle op land —
     tot 2,4× te veel, én de graaf verdubbelt gratis mee.
  3. COMPONENT-SNOEI MET ANKERS — op land staat de water-snoeiregel op zijn
     kop: Pilbara, Carajás, Zouérat–Nouadhibou en Sishen–Saldanha zijn
     geïsoleerde componenten én precies het onderwerp van deze atlas.

⚠️ EIGEN EXTRACT-REGISTRY. `fw.GEOFABRIK_REGIOS` wordt NIET uitgebreid:
`fw.haal_bulk()` bepaalt zijn invoer als "alles uit GEOFABRIK_REGIOS dat op
schijf staat", dus een uitbreiding daar verandert stilzwijgend de eerstvolgende
waterbake en daarmee `marnet.bin` en `ports.json`. De .pbf's staan in dezelfde
map; onbekende sleutels zijn voor water onzichtbaar.

Draaien:
  python v2/tools/fetch_landnet.py --download          # de 24 ontbrekende extracts
  python v2/tools/fetch_landnet.py --extracts nederland,polen,zambia,cambodia,china
  python v2/tools/fetch_landnet.py --regios eu          # per bulk-regio
"""

import argparse
import hashlib
import json
import math
import os
import sys
import time
import urllib.request
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import fetch_waterways as fw  # noqa: E402 — extract_pad, km, simplify, bulk_regio

CACHE = fw.CACHE
LAND_CACHE = os.path.join(CACHE, "land")
GEOFABRIK = fw.GEOFABRIK

# ---------------------------------------------------------------- constanten
# ⚠️ OPHOGEN bij elke wijziging aan het FILTER of aan wat de scan emitteert.
# Bewust NIET in de vingerafdruk: simplify-tolerantie en alle dedup-parameters —
# die werken pas ná het samenvoegen, dus ze bepalen de cache-inhoud niet. Zaten
# ze erin, dan kostte elke ijkslag een rescan van 74 GB.
LAND_FILTER_VERSIE = 1

RAIL_HOUD = {"rail", "narrow_gauge"}
# `service=*` (yard/siding/spur/crossover) en usage tourism/military eruit.
# ⚠️ NOOIT `usage=main` EISEN: 40-43% van de ways draagt geen usage-tag, en die
# eis sloopt precies Afrika en Zuidoost-Azië. Ontbrekende tag = houden.
RAIL_USAGE_WEG = {"tourism", "military"}

KETEN_SIMPLIFY_KM = 0.10     # ná het vouwen, op de hele keten
# ⚠️ CEL EN STAP ZIJN GEIJKT, NIET GEKOZEN. Twee onafhankelijke gepubliceerde
# meetlatten, tweezijdig (dubbelspoor moet omlaag, enkelspoor mag niet zakken):
#   cel/stap   NL (ProRail 3.223)   Polen (PKP-PLK ~19.300)
#   10/8       3.196  (−0,8%)       19.781  (+2,5%)
#   12/8       3.112  (−3,4%)       19.523  (+1,2%)
#   15/20      3.103  (−3,7%)       19.534  (+1,2%)   ← gekozen
#   20/10      2.937  (−8,9%)       19.149  (−0,8%)
#   40/20      2.827  (−12,3%)      18.887  (−2,1%)
# 15/20 haalt beide binnen 4% én houdt het aantal monsters wereldwijd op ~95M
# (bij stap 8 m zouden dat er 237M zijn). Een kleinere cel vouwt minder doordat
# twee sporen op 4 m afstand vaker in aangrenzende rastercellen vallen — dat is
# een rasterrandeffect, geen fysiek verschil.
DEDUP_CEL_M = 15.0
DEDUP_BAKKEN = 6             # richtingsbakken van 30° over 180°
DEDUP_MONSTER_M = 20.0
DEDUP_SNIPPER_KM = 0.30      # kortere overgebleven run = wisselconfetti
HEAL_KM = 0.15
MIN_COMPONENT_KM = 25.0
ANKER_KM = 25.0              # een component "raakt" een atlas-plaats binnen dit

R = 6371.0

# De extracts die de atlas-audit als ontbrekend aanwees (audit_landdekking.py:
# 79 van 497 plaatsen, 16%). Sleutel -> Geofabrik-pad.
LAND_EXTRA_REGIOS = {
    "zuid-afrika": "africa/south-africa",
    "gcc-staten": "asia/gcc-states",
    "madagaskar": "africa/madagascar",
    "zimbabwe": "africa/zimbabwe",
    "namibie": "africa/namibia",
    "botswana": "africa/botswana",
    "lesotho": "africa/lesotho",
    "marokko": "africa/morocco",
    "algerije": "africa/algeria",
    "benin": "africa/benin",
    "mongolia": "asia/mongolia",
    "oezbekistan": "asia/uzbekistan",
    "turkmenistan": "asia/turkmenistan",
    "griekenland": "europe/greece",
    "fr-poitou-charentes": "europe/france/poitou-charentes",
    "cuba": "central-america/cuba",
    "panama": "central-america/panama",
    "nieuw-caledonie": "australia-oceania/new-caledonia",
    "us-montana": "north-america/us/montana",
    "us-utah": "north-america/us/utah",
    "us-wyoming": "north-america/us/wyoming",
    "us-arizona": "north-america/us/arizona",
    "us-alaska": "north-america/us/alaska",
}

# Bulk-regio voor de nieuwe sleutels (fw.BULK_REGIO_VAN_PAD dekt ze niet allemaal).
EXTRA_REGIO = {
    "zuid-afrika": "af", "madagaskar": "af", "zimbabwe": "af", "namibie": "af",
    "botswana": "af", "lesotho": "af", "marokko": "af", "algerije": "af",
    "benin": "af", "gcc-staten": "as", "mongolia": "as", "oezbekistan": "as",
    "turkmenistan": "as", "griekenland": "eu", "fr-poitou-charentes": "eu",
    "cuba": "na", "panama": "na", "nieuw-caledonie": "oc", "us-montana": "na",
    "us-utah": "na", "us-wyoming": "na", "us-arizona": "na", "us-alaska": "na",
}


def regio_van(sleutel):
    if sleutel in EXTRA_REGIO:
        return EXTRA_REGIO[sleutel]
    return fw.bulk_regio(sleutel)


def extract_pad(sleutel):
    return os.path.join(GEOFABRIK, f"{sleutel}-latest.osm.pbf")


def alle_sleutels():
    """Alles wat op schijf staat: de water-registry + onze eigen aanvulling."""
    uit = [s for s in fw.GEOFABRIK_REGIOS if os.path.exists(extract_pad(s))]
    uit += [s for s in LAND_EXTRA_REGIOS if os.path.exists(extract_pad(s))]
    return sorted(set(uit))


# ------------------------------------------------------------------ download

def download_extra(sleutels=None):
    """Haalt de land-extracts op. ⚠️ Controleert op BESTANDSGROOTTE, niet op
    HTTP-status — een 0-byte-extract faalt niet, hij concludeert stil dat een
    land geen spoor heeft (de 302-redirect-val uit M24)."""
    sleutels = sleutels or sorted(LAND_EXTRA_REGIOS)
    os.makedirs(GEOFABRIK, exist_ok=True)
    ua = {"User-Agent": "grondstoffen-atlas/M25 (github.com/larswalters/grondstoffen-atlas)"}
    totaal = 0
    for i, sleutel in enumerate(sleutels, 1):
        pad = extract_pad(sleutel)
        if os.path.exists(pad) and os.path.getsize(pad) > 1_000_000:
            print(f"  [{i}/{len(sleutels)}] {sleutel:<22} al aanwezig "
                  f"({os.path.getsize(pad) / 1048576:,.0f} MB)")
            continue
        url = f"https://download.geofabrik.de/{LAND_EXTRA_REGIOS[sleutel]}-latest.osm.pbf"
        t0 = time.time()
        tijdelijk = pad + ".deel"
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=120) as r, open(tijdelijk, "wb") as f:
            while True:
                blok = r.read(1 << 20)
                if not blok:
                    break
                f.write(blok)
        mb = os.path.getsize(tijdelijk) / 1048576
        if mb < 0.5:
            os.remove(tijdelijk)
            raise SystemExit(f"{sleutel}: {mb:.2f} MB — dat is geen extract "
                             f"(redirect of foutpagina). URL: {url}")
        os.replace(tijdelijk, pad)
        totaal += mb
        print(f"  [{i}/{len(sleutels)}] {sleutel:<22} {mb:8,.0f} MB in "
              f"{time.time() - t0:4.0f}s", flush=True)
    print(f"  samen {totaal:,.0f} MB opgehaald")


# ---------------------------------------------------------------------- scan

def normaliseer_gauge(ruw):
    """'1435;1520' en '1520;1435' zijn dezelfde infrastructuur — sorteren, anders
    boekt 'eerste waarde wint' ze in twee verschillende labels (gemeten in China:
    39,7 km resp. 4,1 km). Geen gauge = 'x' (onbekend, nooit 'fout')."""
    if not ruw:
        return "x"
    delen = sorted({d.strip() for d in str(ruw).split(";") if d.strip()})
    if not delen:
        return "x"
    schoon = []
    for d in delen:
        try:
            schoon.append(str(int(round(float(d)))))
        except ValueError:
            schoon.append(d)
    return "+".join(sorted(set(schoon)))


def spoor_houden(tags):
    """(houden, reden). Uitsluiting vóór insluiting; ontbrekende tag = houden."""
    soort = (tags.get("railway") or "").strip()
    if soort not in RAIL_HOUD:
        return False, f"railway={soort or '-'}"
    if (tags.get("service") or "").strip():
        return False, "service"
    if (tags.get("usage") or "").strip() in RAIL_USAGE_WEG:
        return False, "usage"
    return True, ""


def vingerafdruk(modus, sleutel):
    st = os.stat(extract_pad(sleutel))
    ruw = repr((LAND_FILTER_VERSIE, modus, sleutel, st.st_size, int(st.st_mtime),
                sorted(RAIL_HOUD), sorted(RAIL_USAGE_WEG)))
    return hashlib.sha1(ruw.encode()).hexdigest()[:16]


def cache_pad(modus, sleutel):
    return os.path.join(LAND_CACHE, f"{modus}-{sleutel}-{vingerafdruk(modus, sleutel)}.json")


def land_scan_extract(taak):
    """Worker: één extract → ways met RUWE punten + de node-ids die het vouwen
    nodig heeft. Module-level (picklebaar bij spawn op Windows), osmium binnen.

    ⚠️ GEEN simplify hier. Douglas-Peucker houdt van twee parallelle ways
    verschillende subsets, waardoor hun onderlinge afstand tot ~100 m kan
    oplopen op een dedup-raster van 40 m én de koorde-hoek buiten de
    richtingsbak valt — beide vouwguards falen dan tegelijk, precies in bogen.
    Simplify gebeurt ná het vouwen, op de hele keten.
    """
    modus, sleutel = taak
    cpad = cache_pad(modus, sleutel)
    if os.path.exists(cpad):
        with open(cpad, encoding="utf-8") as f:
            c = json.load(f)
        return sleutel, c["km"], len(c["ways"]), True

    import osmium

    sleutelfilter = "railway" if modus == "spoor" else "highway"
    fp = (osmium.FileProcessor(extract_pad(sleutel))
          .with_locations()
          .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
          .with_filter(osmium.filter.KeyFilter(sleutelfilter)))

    ways, totaal = [], 0.0
    weg_reden = defaultdict(int)
    for obj in fp:
        houd, reden = spoor_houden(obj.tags)
        if not houd:
            weg_reden[reden] += 1
            continue
        refs, pts = [], []
        for n in obj.nodes:
            if n.location.valid():
                refs.append(n.ref)
                pts.append((n.location.lon, n.location.lat))
        if len(pts) < 2:
            continue
        L = sum(fw.km(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
        if L <= 0:
            continue
        totaal += L
        hs = ((obj.tags.get("highspeed") or "").strip() == "yes")
        if not hs:
            ms = (obj.tags.get("maxspeed") or "").strip()
            try:
                hs = float(ms.split()[0]) >= 200
            except (ValueError, IndexError):
                hs = False
        ways.append({
            "id": obj.id,
            "gauge": normaliseer_gauge(obj.tags.get("gauge")),
            "hs": hs,
            "soort": (obj.tags.get("railway") or "").strip(),
            "refs": refs,
            "pts": [[round(lo, 7), round(la, 7)] for lo, la in pts],
            "km": round(L, 4),
        })

    os.makedirs(LAND_CACHE, exist_ok=True)
    tijdelijk = cpad + ".deel"
    with open(tijdelijk, "w", encoding="utf-8") as f:
        json.dump({"versie": LAND_FILTER_VERSIE, "extract": sleutel,
                   "km": round(totaal, 1), "weg": dict(weg_reden),
                   "ways": ways}, f)
    os.replace(tijdelijk, cpad)
    return sleutel, totaal, len(ways), False


def land_scan(sleutels, modus="spoor", workers=None):
    ontbreekt = [s for s in sleutels if not os.path.exists(extract_pad(s))]
    if ontbreekt:
        raise SystemExit("extracts ontbreken: " + ", ".join(ontbreekt) +
                         "\n  haal ze op met: fetch_landnet.py --download")
    os.makedirs(LAND_CACHE, exist_ok=True)
    workers = workers or max(1, min(14, (os.cpu_count() or 2) - 2))
    gb = sum(os.path.getsize(extract_pad(s)) for s in sleutels) / 1e9
    print(f"landscan ({modus}): {len(sleutels)} extracts, {gb:,.1f} GB, "
          f"{workers} workers", flush=True)

    t0, totaal, uit_cache = time.time(), 0.0, 0
    taken = [(modus, s) for s in sleutels]
    if workers == 1 or len(sleutels) == 1:
        res = (land_scan_extract(t) for t in taken)
    else:
        import multiprocessing as mp
        pool = mp.Pool(workers)
        res = pool.imap_unordered(land_scan_extract, taken)
    for i, (sleutel, L, n, gecached) in enumerate(res, 1):
        totaal += L
        uit_cache += gecached
        print(f"  [{i}/{len(sleutels)}] {sleutel:<26} {L:10,.0f} km · {n:7,} ways"
              f"{' (cache)' if gecached else ''}", flush=True)
    if workers > 1 and len(sleutels) > 1:
        pool.close()
        pool.join()
    print(f"  {totaal:,.0f} km ruw over {len(sleutels)} extracts "
          f"({uit_cache} uit cache) in {time.time() - t0:,.0f} s")


def land_laad(sleutels, modus="spoor"):
    """Caches → één lijst, ontdubbeld op OSM way-id (meeste punten wint).
    Geofabrik knipt ways op de extractrand; zonder dit bepaalt de toevallige
    scanvolgorde waar een grensspoorlijn doorgeknipt wordt."""
    op_id, dubbel = {}, 0
    for sleutel in sleutels:
        with open(cache_pad(modus, sleutel), encoding="utf-8") as f:
            c = json.load(f)
        regio = regio_van(sleutel)
        for w in c["ways"]:
            w["regio"] = regio
            oud = op_id.get(w["id"])
            if oud is None:
                op_id[w["id"]] = w
            else:
                dubbel += 1
                if len(w["pts"]) > len(oud["pts"]):
                    op_id[w["id"]] = w
    ways = list(op_id.values())
    print(f"  {len(ways):,} unieke ways ({dubbel:,} dubbels weggevallen — "
          f"grensspoor in meerdere extracts)")
    return ways


# ------------------------------------------------------------- ketens vouwen

def vouw_ketens(ways):
    """Ways aaneenlassen op OSM node-ids zolang de graad 2 is.

    Een knoop mag alleen doorgelast worden als hij in precies twee ways een
    UITEINDE is en in geen enkele way een BINNENpunt (anders is het een echte
    aftakking midden op een way — gemeten in China: 1.510 zulke cellen).
    Gauge moet compatibel zijn: lassen over een spoorwijdte-breuk heen zou
    Małaszewicze en Dostyk onzichtbaar maken.

    INVARIANT: de totale km verandert niet — dit is een merge, geen simplify.
    """
    eind_tel = defaultdict(int)
    binnen = set()
    for w in ways:
        refs = w["refs"]
        eind_tel[refs[0]] += 1
        eind_tel[refs[-1]] += 1
        for r in refs[1:-1]:
            binnen.add(r)

    per_eind = defaultdict(list)
    for i, w in enumerate(ways):
        per_eind[w["refs"][0]].append(i)
        per_eind[w["refs"][-1]].append(i)

    def gauge_ok(a, b):
        return a == b or a == "x" or b == "x"

    gebruikt = [False] * len(ways)
    ketens = []
    # Deterministisch: altijd in oplopende way-id beginnen.
    volgorde = sorted(range(len(ways)), key=lambda i: ways[i]["id"])

    def buur(w, ref):
        """De unieke nog vrije way die op `ref` aansluit, of None. Graad-2 én
        nergens binnenpunt, want anders is het een echte aftakking."""
        if eind_tel[ref] != 2 or ref in binnen:
            return None
        for k in per_eind[ref]:
            if (not gebruikt[k] and gauge_ok(w["gauge"], ways[k]["gauge"])
                    and ways[k]["hs"] == w["hs"] and ways[k]["regio"] == w["regio"]):
                return k
        return None

    for start in volgorde:
        if gebruikt[start]:
            continue
        gebruikt[start] = True
        w = ways[start]
        pts = [tuple(p) for p in w["pts"]]
        refs = list(w["refs"])
        ids = [w["id"]]

        # naar voren
        while True:
            r = refs[-1]
            j = buur(w, r)
            if j is None:
                break
            gebruikt[j] = True
            nw = ways[j]
            npts = [tuple(p) for p in nw["pts"]]
            nrefs = list(nw["refs"])
            if nrefs[0] != r:
                npts.reverse()
                nrefs.reverse()
            pts.extend(npts[1:])
            refs.extend(nrefs[1:])
            ids.append(nw["id"])

        # naar achteren
        while True:
            r = refs[0]
            j = buur(w, r)
            if j is None:
                break
            gebruikt[j] = True
            nw = ways[j]
            npts = [tuple(p) for p in nw["pts"]]
            nrefs = list(nw["refs"])
            if nrefs[-1] != r:
                npts.reverse()
                nrefs.reverse()
            pts = npts[:-1] + pts
            refs = nrefs[:-1] + refs
            ids.append(nw["id"])

        ketens.append({
            "pts": pts,
            "gauge": w["gauge"],
            "hs": w["hs"],
            "regio": w["regio"],
            "wayIds": sorted(ids),
            "km": sum(fw.km(pts[i], pts[i + 1]) for i in range(len(pts) - 1)),
        })
    return ketens


def keten_invariant(ways, ketens):
    a = sum(w["km"] for w in ways)
    b = sum(k["km"] for k in ketens)
    rel = abs(a - b) / max(a, 1e-9)
    print(f"  ketenvouwen: {len(ways):,} ways → {len(ketens):,} ketens · "
          f"km {a:,.1f} → {b:,.1f} (afwijking {rel:.2e})")
    assert rel < 1e-6, f"KETEN-INVARIANT GESCHONDEN: {a:,.3f} vs {b:,.3f} km"
    return b


# --------------------------------------------------------- dedup dubbelspoor

def _monsters(pts, stap_km):
    """(km_langs, lon, lat, azimut°) elke stap_km langs de polyline."""
    uit = []
    acc = 0.0
    for i in range(len(pts) - 1):
        (lo1, la1), (lo2, la2) = pts[i], pts[i + 1]
        d = fw.km((lo1, la1), (lo2, la2))
        if d <= 0:
            continue
        az = math.degrees(math.atan2(
            (lo2 - lo1) * math.cos(math.radians((la1 + la2) / 2)), la2 - la1)) % 180.0
        n = max(1, int(d / stap_km))
        for k in range(n):
            t = k / n
            uit.append((acc + t * d, lo1 + t * (lo2 - lo1), la1 + t * (la2 - la1), az))
        acc += d
    uit.append((acc, pts[-1][0], pts[-1][1], uit[-1][3] if uit else 0.0))
    return uit


def _snijd(pts, van_km, tot_km):
    """Deelpolyline tussen twee kilometerposities langs `pts`."""
    uit, acc = [], 0.0
    for i in range(len(pts) - 1):
        a, b = pts[i], pts[i + 1]
        d = fw.km(a, b)
        if d <= 0:
            continue
        s, e = acc, acc + d
        if e >= van_km and s <= tot_km:
            t0 = max(0.0, (van_km - s) / d)
            t1 = min(1.0, (tot_km - s) / d)
            p0 = (a[0] + t0 * (b[0] - a[0]), a[1] + t0 * (b[1] - a[1]))
            p1 = (a[0] + t1 * (b[0] - a[0]), a[1] + t1 * (b[1] - a[1]))
            if not uit:
                uit.append(p0)
            if p1 != uit[-1]:
                uit.append(p1)
        acc = e
    return uit


def dedup_parallel(ketens):
    """Vouwt parallel dubbelspoor samen. Beslissing PER MONSTER, niet per keten.

    ⚠️ WAAROM PER MONSTER. Een drempel over de hele keten faalt meetbaar op
    lange ketens: na het vouwen is de langste Chinese keten 2.780 km en die
    haalt nooit een drempel — de dedup wordt blind precies waar het meeste
    dubbelspoor ligt (gemeten China −8,8% tegen −26 à −34% op run-niveau).

    ⚠️ GAUGE ZIT IN DE SLEUTEL. Zonder die term vouwde een gemeten Poolse run
    332,6 km breedspoor weg (21% van het hele 1520-net) doordat een 1435- en
    een 1520-lijn elkaars dubbelganger werden. Twee sporen van verschillende
    spoorwijdte zijn per definitie geen duplicaat.

    Mechanisme: elk monster krijgt sleutel (cel≈40 m, richtingsbak van 30°,
    gauge). Een monster is GEDEKT als een LANGERE keten een monster in dezelfde
    sleutel heeft (±1 richtingsbak). De keten wordt geknipt in runs van
    ongedekte monsters; runs < DEDUP_SNIPPER_KM vallen weg (wisselconfetti).
    De langste keten is per constructie de houder — een doorgaande lijn wint
    van een fragment.
    """
    import numpy as np

    orde = sorted(range(len(ketens)), key=lambda i: (-ketens[i]["km"],
                                                     ketens[i]["wayIds"][0]))
    prio = [0] * len(ketens)
    for p, i in enumerate(orde):
        prio[i] = p

    gauges = sorted({k["gauge"] for k in ketens})
    gid = {g: i for i, g in enumerate(gauges)}
    NG = max(1, len(gauges))
    dlat = DEDUP_CEL_M / 111320.0

    kolom_key, kolom_prio, kolom_keten, kolom_idx, kolom_km = [], [], [], [], []
    monsters_per_keten = []
    for i, k in enumerate(ketens):
        ms = _monsters(k["pts"], DEDUP_MONSTER_M / 1000.0)
        monsters_per_keten.append(ms)
        g = gid[k["gauge"]]
        for j, (km_langs, lo, la, az) in enumerate(ms):
            cy = int(round(la / dlat))
            dlon = dlat / max(0.05, math.cos(math.radians(la)))
            cx = int(round(lo / dlon))
            b = int(az // (180.0 / DEDUP_BAKKEN)) % DEDUP_BAKKEN
            cel = ((cy + 300000) << 21) | (cx + 1000000)
            kolom_key.append(cel * (DEDUP_BAKKEN * NG) + b * NG + g)
            kolom_prio.append(prio[i])
            kolom_keten.append(i)
            kolom_idx.append(j)
            kolom_km.append(km_langs)

    if not kolom_key:
        return ketens, {"km_voor": 0.0, "km_na": 0.0}

    key = np.array(kolom_key, dtype=np.int64)
    pri = np.array(kolom_prio, dtype=np.int64)
    uniek, inv = np.unique(key, return_inverse=True)
    beste = np.full(len(uniek), np.iinfo(np.int64).max, dtype=np.int64)
    np.minimum.at(beste, inv, pri)

    # Gedekt = een LANGERE keten (lagere prio) zit in dezelfde cel, in deze of
    # een aangrenzende richtingsbak. De bak is het laagste veld van de sleutel,
    # dus ±NG schuift precies één bak op; de wrap 0↔5 apart.
    gedekt = np.zeros(len(key), dtype=bool)
    basis = key - (key % (DEDUP_BAKKEN * NG))
    bak = (key % (DEDUP_BAKKEN * NG)) // NG
    rest = key % NG
    for delta in (-1, 0, 1):
        buurbak = (bak + delta) % DEDUP_BAKKEN
        buur = basis + buurbak * NG + rest
        pos = np.searchsorted(uniek, buur)
        pos = np.clip(pos, 0, len(uniek) - 1)
        raak = uniek[pos] == buur
        gedekt |= raak & (beste[pos] < pri)

    keten_arr = np.array(kolom_keten, dtype=np.int64)
    km_arr = np.array(kolom_km, dtype=np.float64)
    uit, weggevouwen = [], []
    km_voor = sum(k["km"] for k in ketens)
    for i, k in enumerate(ketens):
        masker = keten_arr == i
        vlaggen = gedekt[masker]
        kms = km_arr[masker]
        if not vlaggen.any():
            uit.append(k)
            continue
        if vlaggen.all():
            weggevouwen.append((k["km"], k))
            continue
        # runs van ONgedekte monsters
        run_start = None
        stukken = []
        for j, vlag in enumerate(vlaggen):
            if not vlag and run_start is None:
                run_start = kms[j]
            elif vlag and run_start is not None:
                stukken.append((run_start, kms[j]))
                run_start = None
        if run_start is not None:
            stukken.append((run_start, kms[-1]))
        bewaard = 0.0
        for van, tot in stukken:
            if tot - van < DEDUP_SNIPPER_KM:
                continue
            pts = _snijd(k["pts"], van, tot)
            if len(pts) < 2:
                continue
            nk = dict(k)
            nk["pts"] = pts
            nk["km"] = sum(fw.km(pts[a], pts[a + 1]) for a in range(len(pts) - 1))
            bewaard += nk["km"]
            uit.append(nk)
        if bewaard < k["km"] * 0.98:
            weggevouwen.append((k["km"] - bewaard, k))

    km_na = sum(k["km"] for k in uit)
    print(f"  dedup: {km_voor:,.0f} → {km_na:,.0f} km "
          f"({100 * (1 - km_na / max(km_voor, 1e-9)):.1f}% gevouwen) · "
          f"{len(ketens):,} → {len(uit):,} ketens")
    per_gauge_voor, per_gauge_na = defaultdict(float), defaultdict(float)
    for k in ketens:
        per_gauge_voor[k["gauge"]] += k["km"]
    for k in uit:
        per_gauge_na[k["gauge"]] += k["km"]
    print("    km per gauge (een gauge die veel meer verliest dan de rest is de "
          "Polen-fout):")
    for g in sorted(per_gauge_voor, key=lambda x: -per_gauge_voor[x])[:8]:
        v, n = per_gauge_voor[g], per_gauge_na.get(g, 0.0)
        print(f"      {g:<10} {v:9,.0f} → {n:9,.0f} km  ({100 * (1 - n / max(v, 1e-9)):5.1f}%)")
    weggevouwen.sort(key=lambda x: -x[0])
    if weggevouwen:
        print("    langste weggevouwen stukken (kijk deze na op de bol):")
        for km_weg, k in weggevouwen[:8]:
            m = k["pts"][len(k["pts"]) // 2]
            print(f"      {km_weg:8,.1f} km · gauge {k['gauge']:<8} · "
                  f"rond ({m[1]:.3f}, {m[0]:.3f})")
    return uit, {"km_voor": km_voor, "km_na": km_na,
                 "weggevouwen": [(round(a, 2), b["pts"][len(b["pts"]) // 2])
                                 for a, b in weggevouwen]}


# ------------------------------------------------------------- naden helen

def heel_naden(ketens, eps_km=HEAL_KM):
    """Hecht losse ketenuiteinden aan de lijn van een ANDER component (≤eps_km).

    ⚠️ WAAROM DIT NA DE DEDUP MOET. Waar de dedup een keten doormidden knipt
    omdat een parallel spoor de houder is, eindigt het overblijvende stuk op de
    afstand tussen twee sporen — zo'n 4 meter — van die houder. Fysiek is dat
    hetzelfde emplacement, maar er is geen gedeelde vertex, dus de graaf valt er
    uit elkaar. Hetzelfde geldt voor een aftakking die de dedup net niet raakte.

    Hergebruikt letterlijk de tier-1 confluentie-heal van het riviernet
    (`bake_marnet._heal_riviernet`): een uiteinde dat binnen eps_km OP de lijn
    van een ander component projecteert wordt daar aangehecht, waarbij het
    projectiepunt als vertex in de doellijn komt. CROSS-COMPONENT per
    constructie, dus een keten kan zichzelf niet kortsluiten.
    """
    import bake_marnet as bm

    per = {"land": [("", [tuple(p) for p in k["pts"]]) for k in ketens]}
    totaal, langste = 0, 0.0
    for _ronde in range(6):
        n, l, _ = bm._heal_riviernet(per, eps_km)
        totaal += n
        langste = max(langste, l)
        if n == 0:
            break
    for k, (_sig, pts) in zip(ketens, per["land"]):
        k["pts"] = pts
        k["km"] = sum(fw.km(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    print(f"  heal: {totaal:,} naden gelegd (≤{eps_km * 1000:.0f} m, "
          f"langste {langste * 1000:.0f} m, cross-component)")
    return ketens


# ------------------------------------------------------- componenten snoeien

def _ankers():
    """De atlas-plaatsen (mijn/raffinaderij/haven/…) als ankerpunten."""
    import audit_landdekking as audit
    import glob
    uit = []
    for pad in sorted(glob.glob(os.path.join(audit.DATA, "*.js"))):
        if os.path.basename(pad).startswith("_"):
            continue
        for n in audit.lees_nodes(pad):
            if n["type"] in audit.PLAATS_TYPES:
                uit.append((n["lon"], n["lat"], n["naam"]))
    return uit


def snoei_componenten(ketens, ankers=None):
    """Houdt een component als hij een atlas-plaats raakt ÓF ≥ MIN_COMPONENT_KM is.

    ⚠️ OP LAND STAAT DE WATER-SNOEIREGEL OP ZIJN KOP. Bij water mocht een
    component zonder haven weg; op land zijn Pilbara, Carajás, Zouérat–Nouadhibou
    en Sishen–Saldanha juist geïsoleerde componenten én precies het onderwerp van
    deze atlas. Daarom snoeit dit alleen wat én klein én ankerloos is, en wordt
    elke weggesnoeide component geprint — nooit stil.
    """
    q = lambda p: (round(p[0] / 1e-4), round(p[1] / 1e-4))   # ~11 m
    ouder = {}

    def vind(x):
        while ouder.setdefault(x, x) != x:
            ouder[x] = ouder[ouder[x]]
            x = ouder[x]
        return x

    def unie(a, b):
        ra, rb = vind(a), vind(b)
        if ra != rb:
            ouder[rb] = ra

    cel_van_keten = []
    for i, k in enumerate(ketens):
        cellen = {q(p) for p in k["pts"]}
        cel_van_keten.append(cellen)
        eerste = None
        for c in cellen:
            if eerste is None:
                eerste = ("c", c)
                vind(eerste)
            else:
                unie(eerste, ("c", c))
        unie(("k", i), eerste)

    per_comp = defaultdict(lambda: {"km": 0.0, "ketens": [], "cellen": set()})
    for i, k in enumerate(ketens):
        r = vind(("k", i))
        per_comp[r]["km"] += k["km"]
        per_comp[r]["ketens"].append(i)
        per_comp[r]["cellen"] |= cel_van_keten[i]

    ankers = ankers if ankers is not None else _ankers()
    # anker → component: grofmazig zoeken op ~0,25° en dan echt meten
    raakt = set()
    dicht = defaultdict(list)
    for r, c in per_comp.items():
        for (cx, cy) in c["cellen"]:
            dicht[(cx // 2500, cy // 2500)].append(r)
    for lon, lat, naam in ankers:
        gx, gy = int(lon / 1e-4) // 2500, int(lat / 1e-4) // 2500
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for r in dicht.get((gx + dx, gy + dy), ()):
                    raakt.add(r)

    houd, weg = [], []
    for r, c in per_comp.items():
        if c["km"] >= MIN_COMPONENT_KM or r in raakt:
            houd.extend(c["ketens"])
        else:
            weg.append(c)
    uit = [ketens[i] for i in sorted(houd)]
    km_weg = sum(c["km"] for c in weg)
    print(f"  snoei: {len(per_comp):,} componenten → {len(per_comp) - len(weg):,} "
          f"gehouden · {len(weg):,} weg ({km_weg:,.0f} km, "
          f"{100 * km_weg / max(sum(k['km'] for k in ketens), 1e-9):.1f}%) — "
          f"klein ÉN ankerloos")
    for c in sorted(weg, key=lambda x: -x["km"])[:5]:
        k = ketens[c["ketens"][0]]
        m = k["pts"][len(k["pts"]) // 2]
        print(f"    {c['km']:7,.1f} km · rond ({m[1]:.3f}, {m[0]:.3f})")
    return uit


def _simplify_met_knopen(pts, beschermd, q):
    """Douglas-Peucker, maar NOOIT over een aanhechtpunt heen.

    ⚠️ DIT IS DE VAL DIE HET NET DEED VERSPLINTEREN. Waar een zijlijn midden op
    een andere keten aantakt, is dat aanhechtpunt een BINNENvertex van de
    doorgaande keten. Een kale DP gooit die vertex weg (hij ligt per definitie
    vlak bij de rechte lijn), waarna de bake er geen gedeelde knoop meer van
    maakt en de aftakking losraakt. Gemeten: 31.737 componenten met de grootste
    op 3.102 km — een spoornet van een miljoen km hoort in Europa en
    Noord-Amerika juist enorme componenten te hebben.

    Daarom: knip de keten op elke beschermde vertex, simplificeer de stukken
    apart, en las ze weer aaneen. De vorm verandert nauwelijks, de topologie
    blijft per constructie heel.
    """
    snij = [0]
    for i in range(1, len(pts) - 1):
        if q(pts[i]) in beschermd:
            snij.append(i)
    snij.append(len(pts) - 1)
    uit = []
    for a, b in zip(snij, snij[1:]):
        deel = fw.simplify(pts[a:b + 1], KETEN_SIMPLIFY_KM)
        uit.extend(deel if not uit else deel[1:])
    return uit


def schrijf_geojson(ketens, modus, suffix=""):
    """Eén Feature per keten, met het label dat de bake als systeem gebruikt."""
    # Elk ketenUITEINDE is een plek waar een andere keten kan aanhechten; die
    # vertices mogen nooit door de simplify verdwijnen.
    q = lambda p: (round(p[0] / 1e-5), round(p[1] / 1e-5))
    beschermd = set()
    for k in ketens:
        beschermd.add(q(k["pts"][0]))
        beschermd.add(q(k["pts"][-1]))

    features = []
    for k in ketens:
        pts = _simplify_met_knopen([tuple(p) for p in k["pts"]], beschermd, q)
        if len(pts) < 2:
            continue
        label = (f"{modus}-{k['regio']}-{k['gauge']}" +
                 ("-hs" if k.get("hs") else ""))
        features.append({
            "type": "Feature",
            "properties": {
                "label": label, "regio": k["regio"], "modus": modus,
                "gauge": k["gauge"], "hs": bool(k.get("hs")),
                "zeevaart": False,
                "km": round(k["km"], 3),
                "wayIds": k["wayIds"][:50],
            },
            "geometry": {"type": "LineString",
                         "coordinates": [[round(lo, 6), round(la, 6)] for lo, la in pts]},
        })
    pad = os.path.join(CACHE, f"landnet_{modus}{suffix}.geojson")
    with open(pad, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection",
                   "bron": "OpenStreetMap contributors (ODbL) via Geofabrik-regio-extract",
                   "laag": "landnet", "modus": modus,
                   "filterVersie": LAND_FILTER_VERSIE,
                   "dedupCelM": DEDUP_CEL_M, "dedupMonsterM": DEDUP_MONSTER_M,
                   "features": features}, f, ensure_ascii=False)
    punten = sum(len(f["geometry"]["coordinates"]) for f in features)
    km = sum(f["properties"]["km"] for f in features)
    print(f"  geschreven: {os.path.basename(pad)} "
          f"({os.path.getsize(pad) / 1048576:,.1f} MB) · {len(features):,} lijnen · "
          f"{km:,.0f} km · {punten:,} punten ({punten / max(km, 1):.2f}/km)")
    return pad


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--download", action="store_true",
                    help="haal de ontbrekende land-extracts op (24 stuks, 3,5 GB)")
    ap.add_argument("--modus", default="spoor", choices=["spoor", "weg"])
    ap.add_argument("--extracts", help="komma-gescheiden extract-namen")
    ap.add_argument("--regios", help="komma-gescheiden bulk-regio's (eu,na,as,…)")
    ap.add_argument("--workers", type=int)
    ap.add_argument("--geen-dedup", action="store_true",
                    help="sla het samenvouwen van dubbelspoor over (ijken)")
    ap.add_argument("--cel-m", type=float, help="dedup-celmaat in meter (ijken)")
    ap.add_argument("--monster-m", type=float, help="bemonsteringsstap in meter (ijken)")
    ap.add_argument("--schrijf", action="store_true", help="schrijf de geojson weg")
    ap.add_argument("--suffix", default="", help="achtervoegsel voor de uitvoer")
    a = ap.parse_args()

    if a.cel_m:
        DEDUP_CEL_M = a.cel_m
    if a.monster_m:
        DEDUP_MONSTER_M = a.monster_m

    if a.download:
        download_extra()
        sys.exit(0)

    if a.extracts:
        sleutels = [s.strip() for s in a.extracts.split(",") if s.strip()]
    else:
        sleutels = alle_sleutels()
        if a.regios:
            wil = {r.strip() for r in a.regios.split(",")}
            sleutels = [s for s in sleutels if regio_van(s) in wil]

    land_scan(sleutels, a.modus, a.workers)
    ways = land_laad(sleutels, a.modus)
    ketens = vouw_ketens(ways)
    keten_invariant(ways, ketens)
    if not a.geen_dedup:
        ketens, _rap = dedup_parallel(ketens)
    ketens = heel_naden(ketens)
    ketens = snoei_componenten(ketens)
    if a.schrijf:
        schrijf_geojson(ketens, a.modus, a.suffix)
    lang = sorted(ketens, key=lambda k: -k["km"])[:10]
    print("\n  langste ketens:")
    for k in lang:
        m = k["pts"][len(k["pts"]) // 2]
        print(f"    {k['km']:9,.1f} km · {k['regio']} · gauge {k['gauge']:<9}"
              f"{' HS' if k['hs'] else '   '} · rond ({m[1]:.2f}, {m[0]:.2f})")
    punten = sum(len(k["pts"]) for k in ketens)
    km = sum(k["km"] for k in ketens)
    print(f"\n  {km:,.0f} km · {len(ketens):,} ketens · {punten:,} punten "
          f"({punten / max(km, 1):.2f}/km)")
