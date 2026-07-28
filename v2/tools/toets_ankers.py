#!/usr/bin/env python3
"""toets_ankers.py — DE VERDACHTENLIJST. Welk anker moet als eerste onder de
satelliet?

── WAAROM DIT BESTAAT ─────────────────────────────────────────────────────
Op 2026-07-28 zijn de kop- en staartankers van vier stromen voor het eerst
stuk voor stuk op een gestitchte Esri-overlay gelegd (routebrief-werkwijze §2).
Uitslag: **10 van de 16 stond fout**, van 42 m tot 4,5 km. Dat is geen toeval
maar een patroon — de corridors ertussen klopten, de uiteinden niet — en de
atlas heeft honderden van zulke punten (`v2/data/aansluitingen.json` plus alle
knopen in `data/*.js`).

Handmatig satelliet-leggen kost ~5 minuten per punt. Dat schaalt niet naar de
hele atlas. Maar het meeste is MECHANISCH te trieren: je hoeft niet te weten
wélke kade het is om te zien dat een kade-anker 4,5 km landinwaarts in een
woonwijk ligt. Deze tool doet die triage en rangschikt de verdachten, zodat het
oog alleen nog naar de kop van de lijst gaat.

⚠️ DEZE TOOL WIJST NIETS AAN EN VERPLAATST NIETS. Hij meet en rangschikt.
Dezelfde rolverdeling als `maak_knooppunten.py` / `maak_aansluitingen.py` /
`verken_terminals.py`: de machine meet, de redacteur oordeelt, de satelliet
beslist. Een hoge score betekent "kijk hier eerst", niet "dit is fout".

── DE VIER TOETSEN (Lars' eigen lijst, aangescherpt op wat meetbaar is) ────
T1 waterrand   ligt een kade-/overslag-/losplek-punt op water of op land, en
               hoe ver van de waterrand? Een kade hoort ~op de rand te liggen.
               Ver op het land = het punt van vandaag (Waalhaven, Napoleon Ave);
               ver ín het water = de andere fout (Lobito, Ruhrort).
T2 haveninfra  afstand tot het dichtstbijzijnde OSM pier/quay/dock/harbour/
               berth-object. Geen haveninfrastructuur binnen 100 m onder een
               "kade" is een sterk signaal.
T3 terrein     wat ligt er ónder het punt? Een kade ligt nooit in
               `landuse=residential`, op `farmland` of in een bos — en nooit
               midden op een `highway`. Een laadplek hoort in het industrie-
               of mijnvlak van zijn eigen site; ligt hij wél in een `quarry`
               maar is er een fabrieksvlak vlakbij, dan staat hij vermoedelijk
               ín de put in plaats van bij de installatie (Escondida).
T4 snap        hoe ver snapt het punt naar zijn EIGEN net.
               ⚠️ MET ÉÉN NUANCE, en die is de eerlijkheid van deze toets: een
               grote ZEE-snap is géén fout maar een meetresultaat — MARNET is
               grof en houdt op bij de kust (Patache 78 km, Coloso 85 km; zie
               de kop van `maak_aansluitingen.py`). Binnenwater, spoor en weg
               zijn wél dekkend, dus dáár telt een snap > 0,5 km wel mee. De
               zee-snap wordt gerapporteerd, niet gescoord.

Elke toets levert punten; de som is de rangorde. Per punt staat erbij WAAROM
hij scoort, want een getal zonder reden stuurt het oog niet.

── DE ZELFTOETS: DE ANKER-CHECK IS HET GELABELDE PROEFWERK ────────────────
`v2/data/ankercheck.json` bevat de 16 punten van 2026-07-28 mét het oordeel van
de satelliet (fout / goed / onbepaald) én de gemeten verplaatsing. Dat is een
gelabelde testverzameling die deze tool niet zelf heeft gemaakt.

    python v2/tools/toets_ankers.py --zelftoets

scoort de OUDE coördinaten en rapporteert of de vier grote missers van die dag
(Waalhaven 4,5 km · Escondida 1,5 km · Beilun 1,2 km · Napoleon Ave 0,5 km)
bovenaan komen. Zo niet, dan is dat een uitslag over de toets — niet over de
ankers. ⚠️ Een 42 m-correctie (Ruhrort) is per constructie NIET te trieren; die
ligt binnen de korrel van elke bron. Dat hoort de tool te zeggen in plaats van
te doen alsof hij alles vangt.

── BRON VAN DE GEOMETRIE ──────────────────────────────────────────────────
OpenStreetMap via Overpass (`fetch_waterways.overpass()`, mét schijf-cache op
de query-inhoud), zelfde keuze en zelfde reden als `verken_terminals.py`: dit
zijn losse puntlocaties verspreid over de wereld, geen wereldbake — een
`around`-query kost seconden, een extract gigabytes. Herhalen is gratis zodra
de cache staat, dus aan de drempels draaien kost geen nieuwe netwerktijd.
Attributie: © OpenStreetMap-bijdragers (ODbL).

Draaien:
  python v2/tools/toets_ankers.py                      # aansluitingen.json
  python v2/tools/toets_ankers.py --bron js            # ook data/*.js-knopen
  python v2/tools/toets_ankers.py --zelftoets          # het proefwerk
  python v2/tools/toets_ankers.py --schrijf            # dump naar build-cache
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import time
from pathlib import Path

import numpy as np

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))

import fetch_waterways as fw            # noqa: E402 — overpass() mét schijf-cache
import maak_knooppunten as mk           # noqa: E402 — lees_knopen/dichtstbij

from shapely.geometry import LineString, Point, Polygon  # noqa: E402
from shapely.ops import unary_union     # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

WORTEL = HIER.parent.parent               # de repo-root
DATA = HIER.parent / "data"               # v2/data
CACHE = HIER.parent / "build-cache"
MARNET_MAP = CACHE / "marnet-preais"      # marnet.bin/json staan sinds M27 niet in v2/data

# ⚠️ 1.200 m, GEMETEN GEKOZEN en niet ruimer. Met 2.000 m liep de query op de
# Yangtze bij Tongling herhaald in een Overpass-504: `rel[natural=water]` moet
# daar de hele rivier-multipolygoon uitvouwen vóór hij hem op de bbox knipt.
# Voor de vraag die deze toets stelt — ligt het punt óp de kade of niet —
# voegt de ruimte daarboven niets toe: wie op 1,2 km geen haveninfrastructuur
# raakt, scoort bij 2 km precies dezelfde maximale verdenking.
STRAAL_M = 1200        # zoekstraal voor water/haven/landgebruik
STRAAL_WEG_M = 60      # "staat het punt op een weg?" — bewust klein en goedkoop


# ==========================================================================
# 1 · WAT WORDT ER GETOETST — de punten verzamelen
# ==========================================================================
# Een anker is hier: id · naam · [lon, lat] · rol · watervlag · modi.
#   rol       laadplek | overslag | losplek  (uit aansluitingen.json, of
#             afgeleid uit het knoop-`type` in data/*.js)
#   water     of dit punt aan het water HOORT te liggen. Dat is geen
#             aanname maar staat in de data: `modi` bevat zee of binnen
#             (aansluiting), of `type == "port"` / `coastal: true` (js-knoop).
#             Zonder die vlag zou een laadspoor bij een smelter (Guixi) langs
#             de kade-lat gelegd worden en per constructie zakken.

ROL_UIT_TYPE = {
    "mine": "laadplek",
    "quarry": "laadplek",
    "port": "overslag",
    "hub": "overslag",
    "airport": "overslag",
    "refinery": "losplek",
    "market": None,          # marktcentroïde: bewust GEEN anker (zie hieronder)
    "recycler": "losplek",
    "exchange": None,        # kluis/beursvoorraad: geen fysieke overslagplek
    "cb": None,
    "reserve": "losplek",
    "military": None,
    "labgrown": "losplek",
}


def ankers_uit_aansluitingen():
    pad = DATA / "aansluitingen.json"
    d = json.loads(pad.read_text(encoding="utf-8"))
    uit = []
    for a in d["aansluitingen"]:
        modi = a.get("modi") or []
        uit.append({
            "id": a["id"], "naam": a["naam"], "plek": a["plek"], "rol": a["rol"],
            "water": bool({"zee", "binnen"} & set(modi)), "modi": modi,
            "bron": "aansluitingen.json",
        })
    return uit


def ankers_uit_js(alleen=None):
    """De knopen uit data/*.js. Geen JS-parser: de bestanden zijn met de hand
    geschreven in één vaste vorm ({ id: "..", type: "..", lat: .., lon: .. }),
    dus een regexp over dat patroon leest ze betrouwbaar — en faalt zichtbaar
    (0 knopen) in plaats van stil, als die vorm ooit verandert."""
    knoop = re.compile(
        r'\{\s*id:\s*"(?P<id>[^"]+)"\s*,\s*type:\s*"(?P<type>[^"]+)"\s*,\s*'
        r'name:\s*"(?P<naam>[^"]*)"(?P<rest>.*?)\}', re.S)
    getal = lambda s, k: (lambda m: float(m.group(1)) if m else None)(
        re.search(rf'\b{k}:\s*(-?[\d.]+)', s))
    uit = []
    for pad in sorted((WORTEL / "data").glob("*.js")):
        if pad.name.startswith("_"):
            continue
        grondstof = pad.stem
        if alleen and grondstof not in alleen:
            continue
        tekst = pad.read_text(encoding="utf-8")
        for m in knoop.finditer(tekst):
            rol = ROL_UIT_TYPE.get(m.group("type"), None)
            if rol is None:
                continue
            lat, lon = getal(m.group("rest"), "lat"), getal(m.group("rest"), "lon")
            if lat is None or lon is None:
                continue
            kust = re.search(r'\bcoastal:\s*true', m.group("rest")) is not None
            uit.append({
                "id": m.group("id"), "naam": f"{m.group('naam')} ({grondstof})",
                "plek": [lon, lat], "rol": rol,
                "water": m.group("type") == "port" or kust,
                "modi": [], "bron": f"data/{pad.name}",
            })
    return uit


PROEFWERK = HIER.parent / "design" / "ankercheck-2026-07-28.json"


def ankers_uit_ankercheck():
    """De 16 punten van de anker-check van 2026-07-28, op hun OUDE coördinaat —
    het gelabelde proefwerk voor de zelftoets.

    ⚠️ Bewust een BEVROREN kopie in v2/design/ en niet het levende
    `v2/data/ankercheck.json`. Dat laatste is een kijklaag die met de kaart
    meebeweegt (het is na het doorvoeren van de correcties teruggebracht tot de
    drie open ligplaatsen); een proefwerk dat meebeweegt met wat je erop wilt
    toetsen bewijst niets meer. Deze kopie is de uitslag van die ene dag: 7
    fout, 6 goed, 3 onbepaald, met de gemeten verplaatsing per punt."""
    d = json.loads(PROEFWERK.read_text(encoding="utf-8"))
    aansl = {a["id"]: a for a in ankers_uit_aansluitingen()}
    uit = []
    for a in d["ankers"]:
        ref = aansl.get(a["id"])
        # De grafiet-ankers staan niet in aansluitingen.json; hun rol/watervlag
        # komt uit de check zelf ("volledig" noemt kade/losplek/plant).
        rol = ref["rol"] if ref else (
            "laadplek" if "plant" in a["volledig"].lower() or "mijn" in a["volledig"].lower()
            else "losplek" if "fabriek" in a["volledig"].lower()
            else "overslag")
        water = ref["water"] if ref else ("kade" in a["volledig"].lower()
                                          or "terminal" in a["volledig"].lower()
                                          or "losplek" in a["volledig"].lower())
        uit.append({
            "id": a["id"], "naam": a["naam"], "plek": a["oud"], "rol": rol,
            "water": water, "modi": ref["modi"] if ref else [],
            "bron": "ankercheck.json (OUDE coördinaat)",
            "oordeel": a["status"], "verplaatsingM": a["afstandM"],
        })
    return uit


# ==========================================================================
# 2 · DE OSM-OMGEVING PER PUNT
# ==========================================================================
# Eén Overpass-query per punt. `out geom(bbox)` KNIPT de geometrie op de bbox —
# zonder die knip levert één aangeraakte `natural=coastline`-way de halve
# Chileense kust en loopt het antwoord in de tientallen MB's.

WATER_CLAUSES = [
    'way["natural"="water"]', 'rel["natural"="water"]',
    'way["waterway"~"^(riverbank|dock)$"]', 'rel["waterway"~"^(riverbank|dock)$"]',
    'way["landuse"="basin"]', 'way["natural"="coastline"]',
]
HAVEN_CLAUSES = [
    'way["man_made"~"^(pier|quay|breakwater)$"]', 'node["man_made"~"^(pier|quay)$"]',
    'way["harbour"]', 'rel["harbour"]', 'way["landuse"="harbour"]',
    'node["seamark:type"~"^(harbour|berth|mooring)$"]',
    'way["seamark:type"~"^(harbour|berth|mooring|dock)$"]',
    'way["industrial"="port"]', 'node["industrial"="port"]',
]
TERREIN_CLAUSES = [
    # Bewust alleen `way` en géén `rel`: landgebruik is in OSM vrijwel altijd
    # een gesloten way, terwijl de relatie-variant de server dwingt tot een
    # multipolygoon-expansie die de query soms omver trekt. De prijs is een
    # enkel als multipolygon gemapt industrieterrein dat we missen — dat kost
    # hooguit een terecht verdachte die te hoog scoort, nooit een gemiste.
    'way["landuse"~"^(industrial|quarry|residential|farmland|forest|commercial|retail|port)$"]',
    'way["natural"="wood"]', 'way["man_made"="works"]', 'way["industrial"]',
]


# ── DE BRON: LOKALE GEOFABRIK-EXTRACTS, OVERPASS ALS TERUGVAL ────────────
# ⚠️ Dit is bewust ANDERS dan `verken_terminals.py`, en de reden is de schaal.
# Die tool bevraagt zeven puntlocaties en kiest daarom Overpass ("een extract
# downloaden kost gigabytes"). Deze tool is bedoeld voor HONDERDEN punten, en
# dan draait het argument om:
#   * Overpass rekent per punt en is een gedeelde publieke dienst. Gemeten op
#     2026-07-28: 504's op twee mirrors, daarna 429 (Too Many Requests) op de
#     derde — bij 16 punten al onbruikbaar, laat staan bij 400.
#   * De extracts STAAN ER AL (184 stuks, 70 GB, van het landnet en de
#     vaarwegen) en kosten dus niets extra. Eén pass over een land meet ALLE
#     ankers in dat land tegelijk — de kosten stijgen met het aantal LANDEN,
#     niet met het aantal punten. Dat is precies de goede kant op.
#   * En het is offline en reproduceerbaar: dezelfde run geeft morgen hetzelfde
#     antwoord, ook als Overpass plat ligt.
# Terugval blijft bestaan (`--osm overpass`) voor een punt in een land waarvan
# geen extract op schijf staat.
#
# ⚠️ WAT DEZE BRON MIST: multipolygoon-RELATIES. De extract-pass leest ways met
# hun knooplocaties; een havenbekken of industrieterrein dat als relatie is
# gemapt telt niet mee. Dat kan een terechte verdachte te hóóg laten scoren
# (geen vlak gevonden onder het punt), nooit een fout punt laten wegzakken —
# de fout valt dus aan de veilige kant. Overpass leest ze wél; wijkt een punt
# opvallend af, dan is `--osm overpass` op dat ene punt de controle.

EXTRACTS = CACHE / "geofabrik"
BBOX_INDEX = CACHE / "geofabrik-bbox.json"

OSM_SLEUTELS = ("natural", "waterway", "landuse", "man_made", "harbour",
                "seamark:type", "industrial", "highway")


def extract_index(ververs=False):
    """{bestand: [zuid, west, noord, oost]} uit de PBF-HEADERS. Een header
    lezen kost geen meetbare tijd (0,00 s per bestand), dus de index is in een
    seconde opgebouwd; hij wordt toch bewaard omdat 184 open/close-rondes op
    een netwerkschijf wél iets kosten."""
    if BBOX_INDEX.exists() and not ververs:
        return json.loads(BBOX_INDEX.read_text(encoding="utf-8"))
    import osmium
    uit = {}
    for p in sorted(EXTRACTS.glob("*.osm.pbf")):
        try:
            r = osmium.io.Reader(str(p))
            b = r.header().box()
            r.close()
            if b.valid():
                uit[p.name] = [b.bottom_left.lat, b.bottom_left.lon,
                               b.top_right.lat, b.top_right.lon]
        except Exception:                        # noqa: BLE001
            continue
    BBOX_INDEX.write_text(json.dumps(uit, indent=1), encoding="utf-8")
    return uit


REGIO_INDEX = CACHE / "geofabrik-regios.json"
GEOFABRIK_INDEX_URL = "https://download.geofabrik.de/index-v1.json"


def regio_polygonen():
    """De ECHTE regiogrenzen van Geofabrik, niet de bbox van het bestand.

    ⚠️ Dit is een correctie op de eerste versie, en de fout was leerzaam: op de
    bbox koos de tool voor Puerto Coloso het ARGENTIJNSE extract (2 elementen
    gevonden in 126 s) omdat de bbox van Chile ook Paaseiland omvat en daardoor
    reusachtig is, terwijl Argentinië's bbox de Chileense kust gewoon
    overlapt. Een bbox is geen gebied — dezelfde klasse fout als "Mongolië ligt
    volledig in de bbox van China" uit M25. Geofabrik publiceert de echte
    regio-multipolygonen in één klein JSON-bestand; dat wordt hier eenmalig
    opgehaald en gecached, en daarna is de keuze exact en offline."""
    if REGIO_INDEX.exists():
        rauw = json.loads(REGIO_INDEX.read_text(encoding="utf-8"))
    else:
        import urllib.request
        req = urllib.request.Request(GEOFABRIK_INDEX_URL, headers={
            "User-Agent": "grondstoffen-atlas/M28 "
                          "(github.com/larswalters/grondstoffen-atlas)"})
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.load(r)
        rauw = {}
        for f in d["features"]:
            pbf = (f["properties"].get("urls") or {}).get("pbf")
            if not pbf:
                continue
            pad = pbf.split("download.geofabrik.de/")[-1]
            pad = pad.replace("-latest.osm.pbf", "")
            rauw[pad] = f["geometry"]
        REGIO_INDEX.parent.mkdir(parents=True, exist_ok=True)
        REGIO_INDEX.write_text(json.dumps(rauw), encoding="utf-8")
        print(f"  geofabrik-regio's opgehaald en gecached: {len(rauw)} regio's")
    from shapely.geometry import shape
    return {pad: shape(g) for pad, g in rauw.items()}


def _sleutel_naar_pad():
    """{lokale bestandsnaam: geofabrik-pad} voor alles wat op schijf staat.
    De twee registries samen (water + de landnet-aanvulling) zijn de bron; een
    derde handmatige lijst zou uit de pas kunnen lopen."""
    import fetch_landnet as fl
    uit = {}
    for reg in (fw.GEOFABRIK_REGIOS, fl.LAND_EXTRA_REGIOS):
        for sleutel, pad in reg.items():
            bestand = f"{sleutel}-latest.osm.pbf"
            if (EXTRACTS / bestand).exists():
                uit[bestand] = pad
    return uit


_REGIO_CACHE = {}


def kies_extract(lon, lat, bbox_index):
    """Het meest SPECIFIEKE extract dat dit punt écht bevat: eerst
    punt-in-polygoon op de Geofabrik-regiogrenzen (kleinste gebied wint, zodat
    us-louisiana van north-america wint), en pas als dat niets geeft terugval
    op de bestands-bbox."""
    if not _REGIO_CACHE:
        try:
            _REGIO_CACHE["poly"] = regio_polygonen()
            _REGIO_CACHE["pad"] = _sleutel_naar_pad()
        except Exception as e:                   # noqa: BLE001
            print(f"  (geofabrik-regio-index niet beschikbaar: {e} — "
                  f"terugval op bestands-bbox)")
            _REGIO_CACHE["poly"] = {}
            _REGIO_CACHE["pad"] = {}
    p = Point(lon, lat)
    treffers = [(_REGIO_CACHE["poly"][pad].area, bestand)
                for bestand, pad in _REGIO_CACHE["pad"].items()
                if pad in _REGIO_CACHE["poly"]
                and _REGIO_CACHE["poly"][pad].contains(p)]
    if treffers:
        return min(treffers)[1]
    kandidaten = [(abs((n - z) * (o - w)), naam)
                  for naam, (z, w, n, o) in bbox_index.items()
                  if z <= lat <= n and w <= lon <= o]
    return min(kandidaten)[1] if kandidaten else None


OSM_CACHE = CACHE / "toets-ankers-osm"


def _cache_sleutel(bestand, vensters):
    import hashlib
    pad = EXTRACTS / bestand
    kern = json.dumps([bestand, int(pad.stat().st_mtime),
                       sorted([list(v) for v in vensters], key=str)])
    return hashlib.sha1(kern.encode()).hexdigest()[:16]


def lees_uit_extract(bestand, vensters):
    """Eén pass over één extract; levert per venster de OSM-elementen in exact
    de vorm die `toets()` van Overpass verwacht ({type, tags, geometry}).

    `vensters` = [(sleutel, zuid, west, noord, oost)]. Een way komt in élk
    venster waarvan de bbox door zijn geometrie geraakt wordt — een kade-way
    van 800 m mag niet wegvallen omdat zijn eerste knoop net buiten het
    vierkant ligt.

    ⚠️ MET SCHIJF-CACHE, en dat is hier geen luxe maar de bruikbaarheid zelf.
    Eén pass over `china-latest.osm.pbf` (1,5 GB) kost ~15 minuten en 3,7 GB
    geheugen, want `with_locations()` bouwt een knooplocatie-index over het hele
    land. Zonder bewaarpunt kost elke draai aan een drempel in §4 dus opnieuw
    een half uur — precies de fout die de verzoening-cache in `bake_marnet.py`
    ooit heeft opgelost (bewaarpunt éérst bij dure pijplijnen). De sleutel bevat
    de bestandstijd én de vensters, dus een nieuw extract of een ander punt
    vervalt de cache vanzelf."""
    sleutel = _cache_sleutel(bestand, vensters)
    pad_cache = OSM_CACHE / f"{sleutel}.json"
    if pad_cache.exists():
        print(" uit cache", end="")
        return json.loads(pad_cache.read_text(encoding="utf-8"))
    import osmium
    pad = EXTRACTS / bestand
    uit = {s: [] for s, *_ in vensters}
    fp = (osmium.FileProcessor(str(pad))
          .with_locations()
          .with_filter(osmium.filter.KeyFilter(*OSM_SLEUTELS)))
    for o in fp:
        tags = {k: v for k, v in o.tags if k in OSM_SLEUTELS}
        if not tags:
            continue
        if o.is_node():
            la, lo = o.location.lat, o.location.lon
            for s, z, w, n, e in vensters:
                if z <= la <= n and w <= lo <= e:
                    uit[s].append({"type": "node", "lat": la, "lon": lo,
                                   "tags": tags})
            continue
        if not o.is_way():
            continue
        try:
            pts = [{"lat": nd.lat, "lon": nd.lon} for nd in o.nodes
                   if nd.location.valid()]
        except Exception:                        # noqa: BLE001 — way zonder locaties
            continue
        if len(pts) < 2:
            continue
        la_min = min(p["lat"] for p in pts); la_max = max(p["lat"] for p in pts)
        lo_min = min(p["lon"] for p in pts); lo_max = max(p["lon"] for p in pts)
        for s, z, w, n, e in vensters:
            if la_min <= n and la_max >= z and lo_min <= e and lo_max >= w:
                uit[s].append({"type": "way", "tags": tags, "geometry": pts})
    OSM_CACHE.mkdir(parents=True, exist_ok=True)
    pad_cache.write_text(json.dumps(uit), encoding="utf-8")
    return uit


def bbox_om(lon, lat, straal_m):
    dlat = straal_m / 110_574.0
    dlon = straal_m / (111_320.0 * max(math.cos(math.radians(lat)), 1e-6))
    return (lat - dlat, lon - dlon, lat + dlat, lon + dlon)


def _vraag(clauses, lon, lat, straal_m):
    zuid, west, noord, oost = bbox_om(lon, lat, straal_m)
    body = "\n".join(f'  {c}(around:{straal_m},{lat:.6f},{lon:.6f});'
                     for c in clauses)
    return (f"[out:json][timeout:180];\n(\n{body}\n);\n"
            f"out geom({zuid:.6f},{west:.6f},{noord:.6f},{oost:.6f});")


def omgeving(lon, lat, straal_m):
    """De OSM-omgeving in DRIE losse vragen, niet één.

    ⚠️ Dat is geen netheid maar bestendigheid, en het is gemeten: als één zware
    clause een 504 uitlokt (de Yangtze-multipolygoon bij Tongling), sleept hij
    in één gecombineerde query ook de goedkope water- en haven-clauses mee de
    afgrond in en verliest het punt ál zijn toetsen. Los gevraagd faalt hooguit
    één familie; de andere twee meten gewoon door en de uitslag zegt eerlijk
    welke toets ontbrak. Elke deelvraag gaat apart de schijf-cache in, dus een
    herstart begint nooit opnieuw en een geslaagde familie hoeft nooit meer
    over de lijn."""
    families = {
        "water": WATER_CLAUSES,
        "haven": HAVEN_CLAUSES,
        "terrein": TERREIN_CLAUSES,
    }
    elementen, ontbreekt = [], []
    for naam, clauses in families.items():
        try:
            elementen += fw.overpass(_vraag(clauses, lon, lat, straal_m)
                                     ).get("elements", [])
        except Exception as e:                   # noqa: BLE001
            print(f"  ⚠️ {naam}-vraag faalde: {type(e).__name__} — toets overgeslagen")
            ontbreekt.append(naam)
    try:
        elementen += fw.overpass(_vraag(['way["highway"]'], lon, lat,
                                        STRAAL_WEG_M)).get("elements", [])
    except Exception:                            # noqa: BLE001
        ontbreekt.append("weg")
    return elementen, ontbreekt


# ==========================================================================
# 3 · METEN — lokale meterprojectie rond het punt
# ==========================================================================
# Op deze schaal (< 3 km) is een equirectangulaire projectie om het punt zelf
# nauwkeurig tot op centimeters, en shapely rekent dan gewoon in meters. Dat is
# de eenvoudigste vorm die niet liegt; een geodetische afstandsfunctie per
# vertex zou hier niets toevoegen behalve rekentijd.

def projectie(lon0, lat0):
    kx = 111_320.0 * math.cos(math.radians(lat0))
    ky = 110_574.0
    return lambda lo, la: ((lo - lon0) * kx, (la - lat0) * ky)


def vormen(elementen, prj, soorten):
    """Elementen → shapely-vormen (Polygon voor gesloten ways, anders LineString).
    Relaties leveren hun member-ways; een gesloten member wordt een vlak, zodat
    een als multipolygon gemapt havenbekken of industrieterrein meedoet."""
    uit = []
    for el in elementen:
        if el.get("tags", {}).get("__soort__") not in soorten:
            continue
        ringen = []
        if el["type"] == "node":
            uit.append((Point(prj(el["lon"], el["lat"])), el))
            continue
        if el["type"] == "way":
            ringen = [el.get("geometry") or []]
        else:                                   # relation
            ringen = [m.get("geometry") or [] for m in el.get("members", [])
                      if m.get("type") == "way"]
        for g in ringen:
            pts = [prj(p["lon"], p["lat"]) for p in g if p]
            if len(pts) < 2:
                continue
            gesloten = len(pts) >= 4 and pts[0] == pts[-1]
            try:
                vorm = Polygon(pts) if gesloten else LineString(pts)
                if gesloten and not vorm.is_valid:
                    vorm = vorm.buffer(0)
                uit.append((vorm, el))
            except Exception:                    # noqa: BLE001 — kapotte ring overslaan
                continue
    return uit


def merk(el):
    """Welke van de drie families is dit element? Bepaald uit de tags, niet uit
    de volgorde in de query — dat blijft kloppen als de query verandert."""
    t = el.get("tags", {}) or {}
    if (t.get("natural") in ("water", "coastline") or t.get("waterway") in ("riverbank", "dock")
            or t.get("landuse") == "basin"):
        return "water"
    if (t.get("man_made") in ("pier", "quay", "breakwater") or "harbour" in t
            or t.get("landuse") == "harbour" or t.get("industrial") == "port"
            or t.get("seamark:type") in ("harbour", "berth", "mooring", "dock")):
        return "haven"
    if t.get("highway"):
        return "weg"
    if (t.get("landuse") or t.get("natural") == "wood" or t.get("man_made") == "works"
            or t.get("industrial")):
        return "terrein"
    return None


# ==========================================================================
# 4 · DE VIER TOETSEN
# ==========================================================================
# De drempels staan hier bij elkaar en zijn bewust grof: dit is een TRIAGE, en
# een fijnere schaal suggereert een precisie die de bronnen niet hebben. Wat
# telt is de VOLGORDE die eruit komt, niet het absolute getal.

def punten_uit(afstand_m, trappen):
    for grens, p in trappen:
        if afstand_m <= grens:
            return p
    return trappen[-1][1] + 1


LANDGEBRUIK_FOUT = {"residential", "farmland", "forest", "commercial", "retail"}
LANDGEBRUIK_GOED = {"industrial", "harbour", "port", "quarry"}


def toets(anker, elementen, ontbreekt=()):
    lon, lat = anker["plek"]
    prj = projectie(lon, lat)
    p0 = Point(0.0, 0.0)
    for el in elementen:                       # merk één keer, hergebruik hem
        el.setdefault("tags", {})["__soort__"] = merk(el)

    water = vormen(elementen, prj, {"water"})
    haven = vormen(elementen, prj, {"haven"})
    terrein = vormen(elementen, prj, {"terrein"})
    wegen = vormen(elementen, prj, {"weg"})

    r = {"score": 0.0, "redenen": [], "meting": {},
         "nietGemeten": sorted(ontbreekt)}

    def scoor(p, waarom):
        r["score"] += p
        if p:
            r["redenen"].append(f"+{p:g} {waarom}")

    # Een familie die niet binnenkwam mag NIET als "niets gevonden" tellen —
    # dat zou een meetfout in een verdenking omzetten, precies de omkering die
    # dit project al twee keer een verkeerde conclusie kostte.
    for f in ontbreekt:
        r["redenen"].append(f"·  {f}-toets niet gemeten (Overpass gaf niets)")

    # ── T1 · waterrand ────────────────────────────────────────────────────
    if anker["water"] and "water" not in ontbreekt:
        randen = [v.exterior if isinstance(v, Polygon) else v for v, _ in water]
        d_rand = min((p0.distance(g) for g in randen), default=float("inf"))
        in_water = any(isinstance(v, Polygon) and v.contains(p0) for v, _ in water)
        r["meting"]["waterrandM"] = None if math.isinf(d_rand) else round(d_rand)
        r["meting"]["inWater"] = in_water
        if math.isinf(d_rand):
            scoor(3, "T1 geen enkel OSM-watervlak binnen de zoekstraal")
        else:
            p = punten_uit(d_rand, [(50, 0), (150, 1), (400, 2), (1000, 3)])
            zijde = "ín het water" if in_water else "op het land"
            if p:
                scoor(p, f"T1 {d_rand:.0f} m van de waterrand, {zijde}")
            if in_water and d_rand > 100:
                scoor(1, "T1 ligt vrij in het water, niet aan een kade")
    else:
        r["meting"]["waterrandM"] = None

    # ── T2 · haveninfrastructuur ──────────────────────────────────────────
    if anker["water"] and "haven" not in ontbreekt:
        d_haven = min((p0.distance(v) for v, _ in haven), default=float("inf"))
        r["meting"]["havenInfraM"] = None if math.isinf(d_haven) else round(d_haven)
        if math.isinf(d_haven):
            scoor(3, "T2 geen pier/kade/haven-object binnen de zoekstraal")
        else:
            p = punten_uit(d_haven, [(100, 0), (300, 1), (1000, 2)])
            if p:
                scoor(p, f"T2 {d_haven:.0f} m tot de dichtstbijzijnde haveninfrastructuur")
    else:
        r["meting"]["havenInfraM"] = None

    # ── T3 · terrein onder het punt ───────────────────────────────────────
    if "terrein" in ontbreekt:
        return r
    onder = [el for v, el in terrein if isinstance(v, Polygon) and v.contains(p0)]
    soorten = {el["tags"].get("landuse") or el["tags"].get("natural")
               or ("works" if el["tags"].get("man_made") == "works" else None)
               for el in onder} - {None}
    r["meting"]["terrein"] = sorted(soorten)
    if anker["water"]:
        mis = soorten & LANDGEBRUIK_FOUT
        if mis:
            scoor(3, f"T3 kade-anker ligt in {'/'.join(sorted(mis))} — dat is geen kade")
        d_weg = min((p0.distance(v) for v, _ in wegen), default=float("inf"))
        r["meting"]["wegM"] = None if math.isinf(d_weg) else round(d_weg)
        if d_weg <= 25 and not (soorten & LANDGEBRUIK_GOED):
            scoor(2, f"T3 ligt {d_weg:.0f} m van een weg-as buiten haven-/industriegebied")
    if anker["rol"] == "laadplek":
        vlak = soorten & {"industrial", "quarry", "works"}
        if not vlak:
            scoor(2, "T3 laadplek ligt niet in een industrie-/mijnvlak")
        elif vlak == {"quarry"}:
            # De put is niet de laadplek: het product gaat de keten in bij de
            # installatie. Alleen verdacht als er ook echt een fabrieksvlak ligt.
            fabriek = any(el["tags"].get("landuse") == "industrial"
                          or el["tags"].get("man_made") == "works"
                          for _, el in terrein)
            if fabriek:
                scoor(2, "T3 laadplek ligt ín het mijnvlak terwijl er een "
                         "fabrieks-/industrievlak naast ligt (put ≠ installatie)")

    return r


# ==========================================================================
# 5 · T4 · de snap naar het eigen net
# ==========================================================================
# ⚠️ De zee-snap wordt WEL gemeten en NIET gescoord. MARNET is een grove
# zeegraaf die bij de kust ophoudt; 78 km bij Patache zegt iets over het net,
# niet over de kade (de kop van maak_aansluitingen.py zegt het al). Binnenwater,
# spoor en weg zijn wél dekkend — daar is ver wél verdacht.

class Netten:
    def __init__(self, marnet_map: Path, data_map: Path):
        self.beschikbaar = {}
        try:
            ports = json.loads((data_map / "ports.json").read_text(encoding="utf-8"))
            meta, lon, lat = mk.lees_knopen(marnet_map / "marnet.json",
                                            marnet_map / "marnet.bin")
            vec = mk.eenheidsvectoren(lon, lat)
            n0 = ports["zeeKnopen"]
            self.beschikbaar["zee"] = (vec, np.arange(0, n0))
            self.beschikbaar["binnen"] = (vec, np.arange(n0, len(lon)))
        except Exception as e:                   # noqa: BLE001
            print(f"  (geen marnet in {marnet_map}: {e} — zee/binnen niet gemeten)")
        try:
            l_meta, l_lon, l_lat = mk.lees_knopen(data_map / "landnet.json",
                                                  data_map / "landnet.bin")
            l_vec = mk.eenheidsvectoren(l_lon, l_lat)
            import maak_aansluitingen as ma
            modus = ma.land_knoop_modus(l_meta)
            self.beschikbaar["spoor"] = (l_vec, np.flatnonzero(modus == 1))
            self.beschikbaar["weg"] = (l_vec, np.flatnonzero(modus == 2))
        except Exception as e:                   # noqa: BLE001
            print(f"  (geen landnet in {data_map}: {e} — spoor/weg niet gemeten)")

    def meet(self, lon, lat, modi):
        uit = {}
        for m in modi:
            if m not in self.beschikbaar:
                continue
            vec, idx = self.beschikbaar[m]
            _, d = mk.dichtstbij(vec, idx, lon, lat)
            uit[m] = round(d, 3)
        return uit


def scoor_snap(r, snaps):
    for m, km in snaps.items():
        r["meting"].setdefault("snapKm", {})[m] = km
        if m == "zee":
            continue                              # gemeten, niet gescoord — zie boven
        p = punten_uit(km, [(0.5, 0), (2.0, 1), (10.0, 2)])
        if p:
            r["score"] += p
            r["redenen"].append(f"+{p:g} T4 snapt {km:.2f} km naar het {m}-net")


# ==========================================================================
# 6 · uitvoer
# ==========================================================================

def main():
    ap = argparse.ArgumentParser(description="verdachtenlijst van ankerpunten")
    ap.add_argument("--bron", choices=["aansluitingen", "js", "beide"],
                    default="aansluitingen")
    ap.add_argument("--grondstof", nargs="*", default=None,
                    help="filter op data/<naam>.js (alleen bij --bron js/beide)")
    ap.add_argument("--zelftoets", action="store_true",
                    help="scoor de OUDE coördinaten uit ankercheck.json en "
                         "toets of de bekende missers bovenaan komen")
    ap.add_argument("--straal", type=int, default=STRAAL_M)
    ap.add_argument("--marnet", default=str(MARNET_MAP))
    ap.add_argument("--val-terug", action="store_true",
                    help="punten zonder lokaal extract alsnog via Overpass "
                         "meten (uit: ze worden gemeld en overgeslagen)")
    ap.add_argument("--osm", choices=["extract", "overpass"], default="extract",
                    help="waar de OSM-omgeving vandaan komt; zie de kop. "
                         "extract = lokale Geofabrik-pbf's (schaalt met het "
                         "aantal LANDEN), overpass = per punt over de lijn")
    # ⚠️ Waarom deze vlag bestaat: `fw.OVERPASS_URLS` staat in een vaste
    # volgorde en de client wacht 180 s per mirror. Ligt de eerste mirror plat,
    # dan kost ELKE query 2 × 180 s vóór hij bij een werkende server is — bij 16
    # punten is dat anderhalf uur wachten op niets. Gemeten 2026-07-28:
    # private.coffee en kumi.systems liepen in een read-timeout, overpass-api.de
    # antwoordde in 3,6 s. De volgorde in fetch_waterways blijft ongemoeid (die
    # klopt op een andere dag weer); dit is de noodknop voor deze run.
    ap.add_argument("--mirror", default=None,
                    help="zet deze Overpass-mirror (substring van de host) "
                         "vooraan, bv. overpass-api.de")
    ap.add_argument("--wacht", type=int, default=60,
                    help="seconden wachten op één mirror vóór de volgende "
                         "(fetch_waterways staat op 180 voor zware bbox-bakes; "
                         "deze vragen zijn klein, dus sneller doorschakelen is "
                         "hier winst)")
    ap.add_argument("--top", type=int, default=0, help="alleen de N verdachtsten tonen")
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()

    fw.OVERPASS_CLIENT_S = args.wacht
    if args.mirror:
        voor = [u for u in fw.OVERPASS_URLS if args.mirror in u]
        if not voor:
            sys.exit(f"--mirror {args.mirror!r} komt in geen van "
                     f"{[u.split('/')[2] for u in fw.OVERPASS_URLS]} voor")
        fw.OVERPASS_URLS = voor + [u for u in fw.OVERPASS_URLS if u not in voor]
        print(f"Overpass-volgorde: "
              f"{[u.split('/')[2] for u in fw.OVERPASS_URLS]}\n")

    if args.zelftoets:
        ankers = ankers_uit_ankercheck()
    else:
        ankers = []
        if args.bron in ("aansluitingen", "beide"):
            ankers += ankers_uit_aansluitingen()
        if args.bron in ("js", "beide"):
            ankers += ankers_uit_js(args.grondstof)
    print(f"{len(ankers)} ankerpunten te toetsen · zoekstraal {args.straal} m\n")

    netten = Netten(Path(args.marnet), DATA)
    print()

    # ── de OSM-omgeving ophalen: per EXTRACT (één pass, alle ankers erin) ──
    omgevingen = {}
    if args.osm == "extract":
        index = extract_index()
        groepen = {}
        for a in ankers:
            groepen.setdefault(kies_extract(*a["plek"], index), []).append(a)
        for bestand, lijst in sorted(groepen.items(), key=lambda kv: str(kv[0])):
            if bestand is None:
                # ⚠️ NIET stilzwijgend terugvallen op Overpass. Bij `--bron js`
                # gaan er 510 punten door deze lus; als daar honderd van in een
                # land zonder extract liggen, zou een automatische terugval een
                # honderdvoudige query-storm op een publieke dienst zijn — en
                # precies dat leverde op de bouwdag 429's op. Ze worden gemeld
                # en overgeslagen; wie ze wél wil meten geeft --val-terug.
                namen = ", ".join(x["naam"][:18] for x in lijst[:6])
                print(f"  geen extract voor {len(lijst)} punt(en) ({namen}"
                      f"{'…' if len(lijst) > 6 else ''})"
                      f"{' → Overpass' if args.val_terug else ' → niet gemeten'}")
                for a in lijst:
                    omgevingen[a["id"]] = (omgeving(*a["plek"], args.straal)
                                           if args.val_terug
                                           else ([], ["water", "haven", "terrein"]))
                continue
            vensters = [(a["id"], *bbox_om(*a["plek"], args.straal)) for a in lijst]
            t0 = time.time()
            print(f"  {bestand:<34} {len(lijst):>2} anker(s) · één pass…",
                  end="", flush=True)
            res = lees_uit_extract(bestand, vensters)
            print(f" {time.time() - t0:5.1f}s · "
                  f"{sum(len(v) for v in res.values()):,} elementen")
            for a in lijst:
                omgevingen[a["id"]] = (res[a["id"]], [])
    else:
        for a in ankers:
            print(f"  {a['naam'][:50]}")
            omgevingen[a["id"]] = omgeving(*a["plek"], args.straal)

    uit = []
    for a in ankers:
        lon, lat = a["plek"]
        elementen, ontbreekt = omgevingen.get(a["id"], ([], ["water", "haven", "terrein"]))
        r = toets(a, elementen, ontbreekt)
        modi = a["modi"] or (["zee"] if a["water"] else ["spoor"])
        scoor_snap(r, netten.meet(lon, lat, modi))
        uit.append({**a, **r})

    uit.sort(key=lambda x: (-x["score"], x["id"]))
    if args.top:
        toon = uit[:args.top]
    else:
        toon = uit

    print("\n" + "=" * 92)
    print("DE VERDACHTENLIJST — hoge score = kijk hier eerst op de satelliet")
    print("=" * 92)
    print(f"{'#':>3} {'score':>6}  {'waterrand':>10} {'haven':>7} {'snap':>18}  anker")
    print("-" * 92)
    for n, x in enumerate(uit, 1):
        if x not in toon:
            continue
        m = x["meting"]
        wr = f"{m['waterrandM']} m" if m.get("waterrandM") is not None else "—"
        hv = f"{m['havenInfraM']} m" if m.get("havenInfraM") is not None else "—"
        sn = " ".join(f"{k}:{v:.2f}" for k, v in (m.get("snapKm") or {}).items())
        oordeel = f"  [{x['oordeel']}]" if "oordeel" in x else ""
        print(f"{n:>3} {x['score']:>6.1f}  {wr:>10} {hv:>7} {sn:>18}  "
              f"{x['naam'][:34]}{oordeel}")
        for reden in x["redenen"]:
            print(f"{'':>21}{reden}")
    print("-" * 92)
    print("waterrand = afstand tot de OSM-waterrand · haven = tot pier/kade/haven-object")
    print("snap = km tot het eigen net (zee wordt gemeten, niet gescoord — MARNET is grof)")
    print("© OpenStreetMap-bijdragers (ODbL)")

    if args.zelftoets:
        zelftoets_uitslag(uit)

    if args.schrijf:
        pad = CACHE / "toets-ankers.json"
        pad.parent.mkdir(parents=True, exist_ok=True)
        pad.write_text(json.dumps(
            {"straalM": args.straal, "bron": "OpenStreetMap (ODbL) via Overpass",
             "ankers": uit}, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"\ngeschreven: {pad}")
    return 0


def zelftoets_uitslag(uit):
    """Het proefwerk: komen de vier grote missers van 2026-07-28 bovenaan?
    ⚠️ De grens ligt op 400 m en niet lager, en dat is geen gemak: onder die
    afstand praat je over de kop-vs-wal van dezelfde steiger (Patache 286 m) of
    over de kade-vs-bekkenrand (Ruhrort 42 m). Zulke correcties liggen binnen de
    korrel van OSM zélf en zijn per constructie niet te trieren — alleen het oog
    op z16 ziet ze. Een toets die beweert ze te vangen zou liegen."""
    groot = [x for x in uit if x.get("verplaatsingM", 0) >= 400]
    goed = [x for x in uit if x.get("oordeel") == "goed"]
    n = len(uit)
    print("\n" + "=" * 92)
    print("ZELFTOETS tegen de anker-check van 2026-07-28")
    print("=" * 92)
    rangen = {x["id"]: i for i, x in enumerate(uit, 1)}
    print(f"  grote missers (≥ 400 m verplaatst), hun rang van {n}:")
    for x in sorted(groot, key=lambda y: -y["verplaatsingM"]):
        print(f"    {rangen[x['id']]:>3}. {x['naam']:<14} "
              f"{x['verplaatsingM']:>5} m verplaatst · score {x['score']:.1f}")
    print(f"  ankers die de satelliet-check DOORSTONDEN, hun rang:")
    for x in sorted(goed, key=lambda y: rangen[y["id"]]):
        print(f"    {rangen[x['id']]:>3}. {x['naam']:<14} · score {x['score']:.1f}")
    if groot and goed:
        slechtste_misser = max(rangen[x["id"]] for x in groot)
        beste_goede = min(rangen[x["id"]] for x in goed)
        print()
        if slechtste_misser < beste_goede:
            print(f"  ✅ GESLAAGD — elke grote misser staat boven elk goedgekeurd anker "
                  f"({slechtste_misser} < {beste_goede}).")
        else:
            print(f"  ⚠️ NIET SCHEIDEND — de slechtste misser staat op {slechtste_misser}, "
                  f"het eerste goede anker op {beste_goede}. De triage moet scherper "
                  f"of de drempels kloppen niet.")
    klein = [x for x in uit if 0 < x.get("verplaatsingM", 0) < 400]
    if klein:
        print("\n  Buiten bereik van deze toets (< 400 m, alleen het oog ziet ze):")
        for x in klein:
            print(f"    {rangen[x['id']]:>3}. {x['naam']:<14} {x['verplaatsingM']:>5} m "
                  f"· score {x['score']:.1f}")


if __name__ == "__main__":
    raise SystemExit(main())
