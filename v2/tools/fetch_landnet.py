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

# ⚠️ DE SIMPLIFY BREEKT WAT DE HEAL NET GEDICHT HEEFT. Gemeten op Polen (bake-regel):
# zónder simplify 77 componenten met de grootste op 15.341 km (79%), mét de simplify
# 91 componenten met de grootste op 8.673 km (45%) — en de twee helften raken elkaar
# daarna op 75 plekken, waarvan zes binnen 22 m en één op 0,7 m. Douglas-Peucker gooit
# 96% van de vertices weg (320.157 → 13.774); waar twee ketens elkaar in een gedeelde
# vertex raakten, houden ze er daarna een paar meter tussen over — te veel voor de
# knoopcel van ~1 m, te weinig om als gat te zien. De heal draaide vóór de simplify,
# dus niemand keek er nog naar.
# Herstellen doet de bestaande heal, mits hij ná de simplify nog eens loopt: 148 naden
# (langste 73 m) brengen Polen naar 22 componenten met de grootste op 18.030 km (94%).
HEAL_NA_SIMPLIFY_KM = 0.15
HEAL_HOEK_MAX = 30.0         # graden; een naad loopt door, een kruising niet

# ---------------------------------------------------------------- de wegkant
# ⚠️ WEG KRIJGT BEWUST GEEN WERELDNET. Weg is de enige modus zónder onafhankelijke
# scheidsrechter (spoor heeft NARN/RINF, water USACE/CEMT), en de tags zijn per land
# onvergelijkbaar. Daarom: ~20-40 VERHALENDE CORRIDORS, elk één gelabelde lijn tussen
# twee ankers, met een gepubliceerde weglengte als meetlat. De scope komt van het
# CORRIDORVENSTER — een buffer om de grootcirkel tussen de twee ankers — en niet van
# de wegklasse. Bewust niet de bbox van de leg: die is voor cu-tenke→Durban 1,38 M km².
WEG_HOUD = {"motorway", "trunk", "primary", "secondary",
            "motorway_link", "trunk_link", "primary_link"}
WEG_ACCESS_WEG = {"private", "no"}
WEG_VENSTER_KM = 50.0
WEG_LENGTE_TOLERANTIE = 0.15   # afwijking van de gepubliceerde lengte die nog telt

# ⚠️ LEEG TOT DE REDACTIERONDE. De kandidatenlijst komt uit de 105 `mode:"road"`-legs
# in `data/*.js` (centroïde-endpoints eruit, >150 km, ontdubbeld op nabijheid → 24),
# maar wélke daarvan een echte wegcorridor zijn is een redactiebesluit van Lars —
# niet iets dat de machine mag afleiden. Vorm per corridor:
#   {"id": "cu-copperbelt-durban", "naam": "Copperbelt → Durban",
#    "van": (lon, lat), "naar": (lon, lat), "extracts": [...],
#    "refs": ["N1", "R571"],            # optioneel: houdt de route op de echte weg
#    "gepubliceerdKm": 2700, "bron": "…"}
CORRIDORS = []

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


def weg_houden(tags):
    """(houden, reden) voor de WEGKANT. Zelfde vorm als `spoor_houden`, andere sleutel.

    ⚠️ RUIMER DAN JE ZOU DENKEN, EN DAT IS MET REDEN. `highway=motorway` levert
    gemeten 0 km in Zambia én 0 km in DR Congo — precies het gebied met elf
    landstromen en de bekendste grenspost van de atlas. Een corridor moet dus ook
    over `trunk`/`primary`/`secondary` kunnen lopen. Dat mag hier ruim, omdat de
    wegkant niet wereldwijd wordt gescand maar alleen binnen het CORRIDORVENSTER:
    de scope komt van de aardrijkskunde, niet van de tag.
    """
    soort = (tags.get("highway") or "").strip()
    if soort not in WEG_HOUD:
        return False, f"highway={soort or '-'}"
    if (tags.get("access") or "").strip() in WEG_ACCESS_WEG:
        return False, "access"
    return True, ""


def _venster_sleutel(modus):
    """De corridorvensters horen in de cachevingerafdruk. Zonder dit geeft een
    gewijzigde corridorlijst stilzwijgend het oude scanresultaat terug — dezelfde
    val als een filterwijziging zonder LAND_FILTER_VERSIE-bump."""
    if modus != "weg":
        return ""
    ruw = repr(sorted((c["id"], tuple(corridor_punten(c)),
                       c.get("vensterKm", WEG_VENSTER_KM)) for c in CORRIDORS))
    return hashlib.sha1(ruw.encode()).hexdigest()[:12]


def vingerafdruk(modus, sleutel):
    st = os.stat(extract_pad(sleutel))
    ruw = repr((LAND_FILTER_VERSIE, modus, sleutel, st.st_size, int(st.st_mtime),
                sorted(RAIL_HOUD), sorted(RAIL_USAGE_WEG),
                sorted(WEG_HOUD), sorted(WEG_ACCESS_WEG), _venster_sleutel(modus)))
    return hashlib.sha1(ruw.encode()).hexdigest()[:16]


def cache_pad(modus, sleutel):
    return os.path.join(LAND_CACHE, f"{modus}-{sleutel}-{vingerafdruk(modus, sleutel)}.json")


def _dwarsafstand_km(p, a, b):
    """Afstand van p tot het grootcirkel-SEGMENT a→b (niet tot de volle grootcirkel:
    voorbij een uiteinde telt de afstand tot dat uiteinde, anders is een corridor van
    Kolwezi naar Durban ook 'dichtbij' in Marokko)."""
    k = math.cos(math.radians((a[1] + b[1]) / 2.0)) * 111.320
    ky = 110.574
    ax, ay = (a[0] - p[0]) * k, (a[1] - p[1]) * ky
    bx, by = (b[0] - p[0]) * k, (b[1] - p[1]) * ky
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    if L2 <= 0:
        return math.hypot(ax, ay)
    t = max(0.0, min(1.0, -(ax * dx + ay * dy) / L2))
    return math.hypot(ax + t * dx, ay + t * dy)


def corridor_punten(c):
    """Anker → tussenpunten → anker. ⚠️ HET VENSTER LIGT OM DEZE LIJN, NIET OM DE
    GROOTCIRKEL. Gemeten op de bekendste corridor van de atlas: de truckroute
    Kolwezi→Durban loopt via Lusaka (155 km van de rechte lijn) en Harare (362 km).
    Een buffer van 50 km om de rechte lijn mist de corridor dus volledig — hij zou
    dwars door Mozambique zoeken. De tussenpunten (grensposten, tussensteden) komen
    uit het bronnenonderzoek en zijn wat de corridor tot een corridor maakt."""
    return [tuple(c["van"])] + [tuple(p) for p in c.get("via", [])] + [tuple(c["naar"])]


def _vensters_voor(sleutel):
    """De corridorvensters die dit extract raken, als (punten, straal_km)."""
    uit = []
    for c in CORRIDORS:
        if c.get("extracts") and sleutel not in c["extracts"]:
            continue
        uit.append((corridor_punten(c), float(c.get("vensterKm", WEG_VENSTER_KM))))
    return uit


def _raakt_venster(pts, vensters):
    """Houd een way zodra ÉÉN vertex binnen een venster valt — een weg die het
    venster in- of uitloopt hoort er in zijn geheel bij, anders knip je hem midden
    in de corridor door en valt de routering uit elkaar."""
    for lo, la in pts:
        for punten, straal in vensters:
            for i in range(len(punten) - 1):
                if _dwarsafstand_km((lo, la), punten[i], punten[i + 1]) <= straal:
                    return True
    return False


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
    houd_fn = spoor_houden if modus == "spoor" else weg_houden
    vensters = _vensters_voor(sleutel) if modus == "weg" else None
    cpad = cache_pad(modus, sleutel)
    # ⚠️ BIJ EEN CACHE-HIT NIET HET HELE BESTAND PARSEN. We hebben hier twee getallen
    # nodig, maar `json.load` trok de volledige geometrie het geheugen in — voor China
    # 238.592 ways — en dat maal veertien workers tegelijk gaf `MemoryError: bad
    # allocation` halverwege een wereldrun. Vandaar een sidecar met alleen de twee
    # getallen; ontbreekt die (oude cache), dan één keer alsnog parsen en aanleggen.
    kort = cpad[:-5] + ".kort.json"
    if os.path.exists(cpad):
        if os.path.exists(kort):
            with open(kort, encoding="utf-8") as f:
                k = json.load(f)
            return sleutel, k["km"], k["n"], True
        with open(cpad, encoding="utf-8") as f:
            c = json.load(f)
        km_c, n_c = c["km"], len(c["ways"])
        del c
        with open(kort, "w", encoding="utf-8") as f:
            json.dump({"km": km_c, "n": n_c}, f)
        return sleutel, km_c, n_c, True

    import osmium

    sleutelfilter = "railway" if modus == "spoor" else "highway"
    fp = (osmium.FileProcessor(extract_pad(sleutel))
          .with_locations()
          .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
          .with_filter(osmium.filter.KeyFilter(sleutelfilter)))

    ways, totaal = [], 0.0
    weg_reden = defaultdict(int)
    for obj in fp:
        houd, reden = houd_fn(obj.tags)
        if not houd:
            weg_reden[reden] += 1
            continue
        refs, pts = [], []
        for n in obj.nodes:
            if n.location.valid():
                refs.append(n.ref)
                pts.append((n.location.lon, n.location.lat))
        if vensters is not None and not _raakt_venster(pts, vensters):
            weg_reden["buiten corridorvenster"] += 1
            continue
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
            # ⚠️ `gauge` draagt op de wegkant de WEGKLASSE. Dat is geen woordspel maar
            # de reden dat de rest van de pijplijn ongewijzigd blijft: gauge is overal
            # de sleutel waarop dedup, label en heal onderscheiden, en twee wegen van
            # verschillende klasse horen net zomin samengevouwen te worden als 1435 en
            # 1520. `x` = onbekend, precies als bij spoor.
            "gauge": (normaliseer_gauge(obj.tags.get("gauge")) if modus == "spoor"
                      else (obj.tags.get("highway") or "x").strip()),
            "hs": hs if modus == "spoor" else False,
            "soort": ((obj.tags.get("railway") or "").strip() if modus == "spoor"
                      else (obj.tags.get("highway") or "").strip()),
            "ref": (obj.tags.get("ref") or "").strip() if modus == "weg" else "",
            "naam": (obj.tags.get("name") or "").strip() if modus == "weg" else "",
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
    with open(cpad[:-5] + ".kort.json", "w", encoding="utf-8") as f:
        json.dump({"km": round(totaal, 1), "n": len(ways)}, f)
    return sleutel, totaal, len(ways), False


def land_scan(sleutels, modus="spoor", workers=None):
    ontbreekt = [s for s in sleutels if not os.path.exists(extract_pad(s))]
    if ontbreekt:
        raise SystemExit("extracts ontbreken: " + ", ".join(ontbreekt) +
                         "\n  haal ze op met: fetch_landnet.py --download")
    os.makedirs(LAND_CACHE, exist_ok=True)
    # Ontbrekende sidecars één voor één aanleggen, vóór de pool: het aanleggen zelf
    # is de dure parse, en veertien daarvan tegelijk is precies wat we vermijden.
    ouderwets = [s for s in sleutels
                 if os.path.exists(cache_pad(modus, s))
                 and not os.path.exists(cache_pad(modus, s)[:-5] + ".kort.json")]
    if ouderwets:
        print(f"  cache-index aanleggen voor {len(ouderwets)} extracts…", flush=True)
        for s in ouderwets:
            land_scan_extract((modus, s))
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


def _eenheid(a, b):
    """Eenheidsvector van a naar b, met lon geschaald op de breedtegraad — anders
    meet je hoeken in graden-ruimte en klopt op 60°N geen enkele hoek."""
    k = math.cos(math.radians((a[1] + b[1]) / 2.0))
    vx, vy = (b[0] - a[0]) * k, b[1] - a[1]
    n = math.hypot(vx, vy) or 1.0
    return (vx / n, vy / n)


def _uit_richting(pts, eind, langs_km=0.5):
    """Eenheidsvector die UIT het uiteinde wijst, over ~langs_km langs de lijn."""
    seq = pts if eind == 0 else pts[::-1]
    pk = seq[-1]
    acc = 0.0
    for i in range(1, len(seq)):
        acc += fw.km(seq[i - 1], seq[i])
        if acc >= langs_km:
            pk = seq[i]
            break
    return _eenheid(pk, seq[0])


def _ketencomponenten(lijnen):
    """Union-find over ketens die een knoopcel delen — exact de regel waarmee
    `bake_landnet.bouw()` knopen maakt. Geeft een wortel per keten."""
    import bake_marnet as bm

    q = lambda p: (round(p[0] / bm.BULK_QUANT), round(p[1] / bm.BULK_QUANT))
    par = list(range(len(lijnen)))

    def vind(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    cel = {}
    for gi, pts in enumerate(lijnen):
        for p in pts:
            c = q(p)
            gj = cel.get(c)
            if gj is None:
                cel[c] = gi
            else:
                ra, rb = vind(gi), vind(gj)
                if ra != rb:
                    par[rb] = ra
    return [vind(i) for i in range(len(lijnen))]


def heel_na_simplify(ketens, voor, modus, eps_km=HEAL_NA_SIMPLIFY_KM,
                     hoek_max=HEAL_HOEK_MAX):
    """Herstelt UITSLUITEND de verbindingen die de simplify heeft verbroken.

    ⚠️ DE DRAGENDE REGEL: een naad mag alleen gelegd worden tussen twee ketens die
    vóór de simplify in HETZELFDE component zaten en er ná in verschillende. Daarmee
    kan deze stap per constructie geen enkele verbinding máken die de brongeometrie
    niet al had — geen kruising, geen viaduct, geen tunnel die toevallig binnen 150 m
    passeert. Hij zet alleen terug wat Douglas-Peucker heeft weggegooid.

    Drie guards daar bovenop:
      * ÉÉN MODALITEIT. `ketens` komt uit één modus-run; dat wordt hier hard getoetst.
        Spoor↔weg, spoor↔rivier en spoor↔zee kunnen hier dus niet ontstaan — die
        koppelingen horen bij de aangewezen overslagknooppunten, niet bij een heal.
      * SPOORWIJDTE. 1435 hecht niet aan 1520; alleen gelijke gauge, of één zijde
        onbekend (`x`). Een breuk van spoorwijdte is een overstap, geen naad.
      * RICHTING. Het uiteinde moet in het verlengde van de doellijn liggen (≤hoek_max).
        Een doorgeknipte lijn loopt door; een lijn die er dwars overheen gaat niet.

    Geeft (naden, rapport per afstandsklasse, steekproef) en muteert `ketens` in-place.
    """
    from shapely.geometry import LineString, Point, box  # noqa: E402
    from shapely.strtree import STRtree                  # noqa: E402

    fout = [k for k in ketens if k.get("modus", modus) != modus]
    assert not fout, f"{len(fout)} ketens met een andere modus dan {modus!r} in de heal"

    na = [k["pts"] for k in ketens]
    comp_voor = _ketencomponenten(voor)
    comp_na = _ketencomponenten(na)

    geoms = [LineString(p) for p in na]
    boom = STRtree(geoms)
    venster = (eps_km / 111.32) * 1.6
    cos_max = math.cos(math.radians(hoek_max))

    kand = []
    for gi, pts in enumerate(na):
        for eind in (0, -1):
            E = pts[eind]
            uit = _uit_richting(pts, eind)
            bx = box(E[0] - venster, E[1] - venster, E[0] + venster, E[1] + venster)
            beste = None
            for cand in boom.query(bx):
                cand = int(cand)
                if cand == gi:
                    continue
                if comp_na[cand] == comp_na[gi]:
                    continue                       # al verbonden
                if comp_voor[cand] != comp_voor[gi]:
                    continue                       # ⚠️ bestond vóór de simplify niet
                ga, gb = ketens[gi]["gauge"], ketens[cand]["gauge"]
                if ga != gb and "x" not in (ga, gb):
                    continue                       # spoorwijdte-breuk is geen naad
                ln = geoms[cand]
                s = ln.project(Point(E))
                npnt = ln.interpolate(s)
                # ⚠️ meteen afronden op de precisie waarmee de geojson wegschrijft:
                # het uiteinde verhuist naar npc én npc komt in de doellijn, dus beide
                # moeten letterlijk dezelfde waarde krijgen of de knoopcel valt alsnog
                # net verkeerd uit.
                npc = (round(npnt.x, 6), round(npnt.y, 6))
                d = fw.km(E, npc)
                if d > eps_km:
                    continue
                doel = na[cand]
                j = min(range(len(doel) - 1),
                        key=lambda j: fw.km(npc, doel[j]) + fw.km(npc, doel[j + 1]))
                langs = _eenheid(doel[j], doel[j + 1])
                if abs(uit[0] * langs[0] + uit[1] * langs[1]) < cos_max:
                    continue                       # dwars = kruising, geen naad
                if beste is None or d < beste[0]:
                    beste = (d, cand, npc)
            if beste:
                kand.append((beste[0], gi, eind, beste[1], beste[2]))
    kand.sort()

    cmap = list(comp_na)
    idx = {w: i for i, w in enumerate(sorted(set(comp_na)))}
    par = list(range(len(idx)))

    def vind(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    import bake_marnet as bm

    gebruikt, naden, steekproef = set(), [], []
    for d, gi, eind, cand, npc in kand:
        a, b = vind(idx[cmap[gi]]), vind(idx[cmap[cand]])
        if (gi, eind) in gebruikt or a == b:
            continue
        pts = list(na[gi])
        oud = pts[eind]
        pts[eind] = npc
        na[gi] = pts
        ketens[gi]["pts"] = pts
        na[cand] = bm._voeg_in(na[cand], npc)
        ketens[cand]["pts"] = na[cand]
        gebruikt.add((gi, eind))
        par[b] = a
        naden.append(d)
        if len(steekproef) < 12:
            steekproef.append({
                "m": round(d * 1000, 1), "lat": round(oud[1], 5), "lon": round(oud[0], 5),
                "gauge": f"{ketens[gi]['gauge']}/{ketens[cand]['gauge']}",
                "regio": f"{ketens[gi]['regio']}/{ketens[cand]['regio']}",
            })

    klassen = [("<1 m", 0.0, 0.001), ("1-5 m", 0.001, 0.005), ("5-25 m", 0.005, 0.025),
               ("25-75 m", 0.025, 0.075), ("75-150 m", 0.075, 0.150)]
    rapport = [(nm, sum(1 for d in naden if lo <= d < hi)) for nm, lo, hi in klassen]
    print(f"  heal ná simplify: {len(naden):,} naden hersteld "
          f"(alleen wat de simplify brak; ≤{eps_km * 1000:.0f} m, ≤{hoek_max:.0f}°, "
          f"gelijke spoorwijdte, één modaliteit)")
    for nm, n in rapport:
        if n:
            print(f"    {nm:>9} : {n:>6,}")
    return naden, rapport, steekproef


def _wegen_graaf(ways, refs=None):
    """Vertex-graaf over de gescande wegen. Zelfde vorm als `kortste_waterpad` uit
    M24: elke vertex is een knoop, opeenvolgende vertices zijn verbonden. Wegen
    delen in OSM hun kruisingsknoop exact, dus stitchen is hier niet nodig — en
    juist daarom wél een aparte snap voor de ankers (een mijn ligt niet op de weg).

    `refs` is optioneel de whitelist van wegnummers uit het bronnenonderzoek. Hij
    filtert niet, maar maakt niet-genoemde wegen DUURDER (factor 3). Dat is met
    opzet zachter dan een filter: een corridor die één ongenummerd stuk bevat moet
    niet als 'geen pad' eindigen, maar de route mag er ook niet lichtvaardig van
    afwijken. Zelfde gedachte als de naam-whitelist bij de rivieren, alleen daar
    kon het hard omdat een rivier één naam draagt en een corridor er tien.
    """
    knoop_id, knopen, buren = {}, [], []

    def nid(p):
        s = (round(p[0], 6), round(p[1], 6))
        if s not in knoop_id:
            knoop_id[s] = len(knopen)
            knopen.append(s)
            buren.append([])
        return knoop_id[s]

    for w in ways:
        straf = 1.0
        if refs:
            r = (w.get("ref") or "")
            straf = 1.0 if any(x and x in r.split(";") for x in refs) else 3.0
        pts = [tuple(p) for p in w["pts"]]
        vorige = None
        for p in pts:
            k = nid(p)
            if vorige is not None and vorige != k:
                d = fw.km(knopen[vorige], knopen[k])
                buren[vorige].append((k, d, d * straf))
                buren[k].append((vorige, d, d * straf))
            vorige = k
    return knopen, buren


def _dichtste_knoop(knopen, punt, max_km=25.0):
    beste, best_d = None, max_km
    for i, k in enumerate(knopen):
        d = fw.km(punt, k)
        if d < best_d:
            beste, best_d = i, d
    return beste, best_d


def _dijkstra(knopen, buren, start, doel):
    """Kortste pad op de GESTRAFTE kosten; geeft de vertexlijst en de ECHTE km."""
    import heapq

    dist = {start: 0.0}
    vorig = {}
    pq = [(0.0, start)]
    gezien = set()
    while pq:
        d, u = heapq.heappop(pq)
        if u in gezien:
            continue
        gezien.add(u)
        if u == doel:
            break
        for v, _echt, kost in buren[u]:
            nd = d + kost
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                vorig[v] = u
                heapq.heappush(pq, (nd, v))
    if doel not in gezien:
        return None, 0.0
    pad = [doel]
    while pad[-1] != start:
        pad.append(vorig[pad[-1]])
    pad.reverse()
    pts = [knopen[i] for i in pad]
    km = sum(fw.km(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    return pts, km


def corridor_keten(ways, corridor):
    """Eén corridor → één keten, gerouteerd langs zijn tussenpunten.

    ⚠️ DE TUSSENPUNTEN ZIJN GEEN DECORATIE. Zonder ze zoekt het kortste pad de
    hemelsbrede lijn op, en die klopt voor geen enkele echte corridor: Kolwezi→
    Durban loopt via Lusaka (155 km van de rechte lijn) en Harare (362 km). Elk
    been wordt apart gerouteerd en daarna aaneengeschakeld.

    Geeft (keten_of_None, rapport). Het rapport is wat de redacteur leest: per been
    de gevonden lengte, en aan het eind de vergelijking met de gepubliceerde lengte.
    """
    punten = corridor_punten(corridor)
    knopen, buren = _wegen_graaf(ways, corridor.get("refs"))
    if not knopen:
        return None, {"id": corridor["id"], "fout": "geen wegen in het venster"}

    ankers, snaps = [], []
    for p in punten:
        k, d = _dichtste_knoop(knopen, p)
        if k is None:
            return None, {"id": corridor["id"],
                          "fout": f"punt {p} ligt >25 km van elke weg"}
        ankers.append(k)
        snaps.append(round(d, 2))

    pts, km_tot, benen = [], 0.0, []
    for i in range(len(ankers) - 1):
        deel, km = _dijkstra(knopen, buren, ankers[i], ankers[i + 1])
        if deel is None:
            return None, {"id": corridor["id"],
                          "fout": f"geen wegpad tussen punt {i} en {i + 1}"}
        benen.append(round(km, 1))
        km_tot += km
        pts.extend(deel if not pts else deel[1:])

    gepubliceerd = corridor.get("gepubliceerdKm")
    afwijking = None
    if gepubliceerd:
        afwijking = km_tot / gepubliceerd - 1.0

    keten = {
        "pts": [(round(lo, 6), round(la, 6)) for lo, la in pts],
        "km": km_tot,
        "regio": corridor["id"],
        "gauge": "corridor",
        "hs": False,
        "wayIds": [],
        "modus": "weg",
    }
    return keten, {
        "id": corridor["id"], "naam": corridor.get("naam", corridor["id"]),
        "km": round(km_tot, 1), "benen": benen, "snapsKm": snaps,
        "gepubliceerdKm": gepubliceerd,
        "afwijking": None if afwijking is None else round(100 * afwijking, 1),
        "binnenTolerantie": (None if afwijking is None
                             else abs(afwijking) <= WEG_LENGTE_TOLERANTIE),
        "punten": len(pts),
    }


def schrijf_geojson(ketens, modus, suffix=""):
    """Eén Feature per keten, met het label dat de bake als systeem gebruikt."""
    # Elk ketenUITEINDE is een plek waar een andere keten kan aanhechten; die
    # vertices mogen nooit door de simplify verdwijnen.
    q = lambda p: (round(p[0] / 1e-5), round(p[1] / 1e-5))
    beschermd = set()
    for k in ketens:
        beschermd.add(q(k["pts"][0]))
        beschermd.add(q(k["pts"][-1]))

    # ⚠️ SIMPLIFY EERST, DAN OPNIEUW HELEN — in die volgorde, en niet andersom.
    # De heal in de pijplijn draait vóór dit punt; Douglas-Peucker breekt daarna een
    # deel van die naden weer open (Polen: grootste component 15.341 → 8.673 km).
    # Deze tweede heal zet uitsluitend terug wat hier stuk ging, op de geometrie die
    # de bake ook echt te zien krijgt — dus ná het afronden op 6 decimalen.
    voor = [[tuple(p) for p in k["pts"]] for k in ketens]
    for k, pts in zip(ketens, voor):
        s = _simplify_met_knopen(pts, beschermd, q)
        k["pts"] = ([(round(lo, 6), round(la, 6)) for lo, la in s]
                    if len(s) >= 2 else [(round(lo, 6), round(la, 6)) for lo, la in pts])
    heel_na_simplify(ketens, voor, modus)

    features = []
    for k in ketens:
        pts = k["pts"]
        if len(pts) < 2:
            continue
        k["km"] = sum(fw.km(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
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

    if a.modus == "weg":
        # ⚠️ DE WEGKANT DRAAIT EEN ANDERE PIJPLIJN. Vouwen/dedup/heal/snoei zijn er voor
        # een NET; hier bouwen we geen net maar een handvol verhalende lijnen. Elke
        # corridor wordt apart gerouteerd tussen zijn ankers, langs zijn tussenpunten.
        if not CORRIDORS:
            raise SystemExit("CORRIDORS is leeg — zie v2/design/wegcorridors.md; de lijst "
                             "is een redactiebesluit, geen afleiding.")
        nodig = sorted({s for c in CORRIDORS for s in c.get("extracts", [])})
        if not nodig:
            raise SystemExit("geen extracts opgegeven bij de corridors")
        land_scan(nodig, "weg", a.workers)
        ketens, rapporten = [], []
        for c in CORRIDORS:
            deel = land_laad(c.get("extracts", []), "weg")
            keten, rap = corridor_keten(deel, c)
            rapporten.append(rap)
            if keten:
                ketens.append(keten)
        print("\n  corridors:")
        for r in rapporten:
            if r.get("fout"):
                print(f"    ⚠️  {r['id']:<28} {r['fout']}")
                continue
            meet = ""
            if r["gepubliceerdKm"]:
                vlag = "OK" if r["binnenTolerantie"] else "⚠️"
                meet = (f" · gepubliceerd {r['gepubliceerdKm']:,} km "
                        f"({r['afwijking']:+.1f}% {vlag})")
            print(f"    {r['id']:<28} {r['km']:>8,.1f} km · benen {r['benen']}"
                  f" · snaps {r['snapsKm']}{meet}")
        if a.schrijf:
            schrijf_geojson(ketens, "weg", a.suffix)
        km = sum(k["km"] for k in ketens)
        print(f"\n  {km:,.0f} km · {len(ketens)} corridors van de {len(CORRIDORS)}")
        sys.exit(0)

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
