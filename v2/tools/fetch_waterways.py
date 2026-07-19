#!/usr/bin/env python3
"""
fetch_waterways.py — bevaarbare-vaarweg-middellijnen per systeem (M24, LAR-486).

Twee bronnen; de bake-off van LAR-486 vergelijkt ze op hetzelfde traject:
  osm    Overpass API — waterway=river|canal|fairway met een CEMT-tag of een
         naam uit de whitelist, binnen de systeem-bbox.
         Licentie: ODbL — "© OpenStreetMap contributors" hoort in de HUD.
  unece  het E-waterway-netwerk uit de UNECE Blue Book database
         (gis.unece.org, ArcGIS Feature Service / shapefile-export).

De extractie is bron-agnostisch: uit de ruwe segmenten wordt het KORTSTE
WATERPAD gestitcht van anker-zee naar anker-binnen (dijkstra over de
segment-geometrie; uiteinden binnen de stitch-tolerantie gelden als
verbonden). Zelfde ankers + andere bron = zelfde traject, vergelijkbaar.

Uitvoer: v2/build-cache/vaarwegen_<bron>.geojson — één LineString per systeem,
coördinaten beginnen ALTIJD aan de zeezijde. bake_marnet.py leest dit via
--vaarwegen en hangt de ketens aan het MARNET-netwerk.

Draaien:  python v2/tools/fetch_waterways.py osm
          python v2/tools/fetch_waterways.py unece --bestand <pad .geojson/.shp>
"""

import argparse
import hashlib
import heapq
import json
import math
import os
import sys
import time
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)
CACHE = os.path.join(V2, "build-cache")

OVERPASS_URLS = [
    "https://overpass.private.coffee/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass-api.de/api/interpreter",
]
# De publieke mirrors geven onder belasting 504's — óók op queries die minuten
# eerder gewoon slaagden. Eén ronde langs de lijst is dus te weinig; met een
# pauze ertussen komt hij er wel door. Elke geslaagde query gaat de cache in,
# dus een herstart begint nooit opnieuw.
OVERPASS_RONDES = 4
OVERPASS_PAUZE_S = 30
# Twee verschillende klokken, bewust uit elkaar gehouden: de server mag lang
# rekenen, maar wij moeten SNEL kunnen doorschakelen naar een andere mirror.
# Eén gedeelde waarde van 600 s liet een overbelaste mirror de hele run tien
# minuten gijzelen; een zware bbox-query duurt gemeten ~75 s.
OVERPASS_SERVER_S = 300   # [timeout:] in de query zelf
OVERPASS_CLIENT_S = 180   # urllib — daarna de volgende mirror

R_AARDE = 6371.0

# Stitch-tolerantie per bron: OSM-ways delen exacte knopen (kleine marge voor
# fairway->rivier-overgangen); officiële netten hebben grovere segmentatie.
STITCH_KM = {"osm": 0.06, "unece": 0.8}
ANKER_TOL_KM = 6.0    # anker moet binnen deze afstand van de geometrie liggen
SIMPLIFY_KM = 0.025   # Douglas-Peucker ~25 m: bochten blijven, ruis verdwijnt

# bbox = (lat_min, lon_min, lat_max, lon_max) — Overpass-volgorde (Z,W,N,O).
# Ankers als (lon, lat); zeezijde eerst. Havens (searoute): Amsterdam
# (4.904, 52.375) · Nijmegen (5.867, 51.833) · Rotterdam (4.442, 51.904).
#
# `volgt_op` (LAR-487/488): dit systeem hangt niet aan MARNET maar aan het
# binneneinde van dat eerdere systeem — zo draagt één rivier twee labels met
# elk een eigen zeevaart-vlag (Mississippi zeevaarbaar t/m Baton Rouge, de
# Yangtze t/m Nanjing; daarboven binnenvaart). Het vervolgsysteem moet dus
# LATER in deze lijst staan en zijn anker_zee gelijk hebben aan het
# anker_binnen van zijn voorganger.
SYSTEMEN = [
    dict(
        label="noordzeekanaal",
        zeevaart=True,
        cemt="VIb",
        bbox=(52.34, 4.50, 52.52, 5.02),
        namen=["Noordzeekanaal", "Het IJ", "Afgesloten IJ", "Buiten-IJ",
               "Voorzaan", "Zijkanaal G", "Buitenhaven", "IJmuiden"],
        anker_zee=(4.565, 52.463),      # havenmond IJmuiden (vóór de sluizen)
        anker_binnen=(4.904, 52.383),   # Het IJ t.h.v. de haven van Amsterdam
    ),
    dict(
        label="waal",
        zeevaart=False,
        cemt="VIc",
        bbox=(51.70, 3.95, 52.05, 6.00),
        namen=["Nieuwe Waterweg", "Het Scheur", "Scheur", "Nieuwe Maas",
               "Noord", "Beneden-Merwede", "Beneden Merwede",
               "Boven-Merwede", "Boven Merwede", "Waal",
               "Oude Maas", "Dordtsche Kil", "Maasmond", "Calandkanaal"],
        anker_zee=(4.060, 51.985),      # Maasmond / Hoek van Holland
        anker_binnen=(5.860, 51.852),   # Waal t.h.v. Nijmegen (Waalkade)
    ),
    # ---- VS (LAR-487) — MARNET's mississippi-tak eindigt bij New Orleans en
    # loopt daar dood in het Pontchartrainmeer; alles stroomopwaarts ontbreekt.
    # Baton Rouge is het kopeinde van de diepzeevaart (~370 km binnenland),
    # daarboven is het duwbakgebied → tweede label zónder zeevaart-vlag.
    dict(
        label="mississippi",
        zeevaart=True,
        cemt="",
        bbox=(29.85, -91.35, 30.60, -89.90),
        namen=["Mississippi River", "Mississippi"],
        anker_zee=(-90.055, 29.935),    # rivier bij New Orleans (Algiers Point)
        anker_binnen=(-91.190, 30.445),  # haven van Baton Rouge
    ),
    dict(
        label="mississippi-boven",
        zeevaart=False,
        cemt="",
        volgt_op="mississippi",
        bbox=(30.30, -92.00, 35.35, -89.60),
        namen=["Mississippi River", "Mississippi"],
        anker_zee=(-91.190, 30.445),    # = anker_binnen van 'mississippi'
        anker_binnen=(-90.125, 35.125),  # rivier bij Memphis
    ),
    # ---- China (LAR-488) — géén officiële tweede bron; MARNET houdt op bij
    # Zhenjiang (knoop 9668), 78 km vóór Nanjing. Zeeschepen varen echt tot
    # Nanjing (12,5 m-diepwaterkanaal), daarboven binnenvaart.
    dict(
        label="yangtze",
        zeevaart=True,
        cemt="",
        bbox=(31.90, 118.55, 32.45, 119.70),
        namen=["长江", "扬子江", "Yangtze River", "Yangtze"],
        anker_zee=(119.545, 32.195),    # MARNET-uiteinde bij Zhenjiang
        anker_binnen=(118.735, 32.095),  # haven van Nanjing
    ),
    dict(
        label="yangtze-boven",
        zeevaart=False,
        cemt="",
        volgt_op="yangtze",
        bbox=(29.50, 113.90, 32.30, 118.85),
        namen=["长江", "扬子江", "Yangtze River", "Yangtze"],
        anker_zee=(118.735, 32.095),    # = anker_binnen van 'yangtze'
        anker_binnen=(114.300, 30.590),  # haven van Wuhan
    ),
]


def km(a, b):
    """Haversine tussen (lon,lat)-paren."""
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R_AARDE * math.asin(min(1.0, math.sqrt(h)))


# ---------------------------------------------------------------- bron: OSM

def overpass(query):
    """Overpass-antwoord, met een schijf-cache op de query-hash.

    De cache maakt herhalen goedkoop: ankers/simplify aanpassen hoeft niet
    opnieuw over de lijn (dezelfde les als de verzoening-cache in
    bake_marnet.py — bewaarpunt éérst bij dure pijplijnen). De bbox en de
    namen zitten ín de query, dus de sleutel vervalt vanzelf zodra die
    veranderen.
    """
    # Sleutel op de INHOUD van de query (bbox + namen), niet op de
    # instellingenregel: aan een timeout draaien mag nooit opgehaalde data
    # weggooien.
    kern = "\n".join(r for r in query.splitlines() if not r.startswith("[out:"))
    sleutel = hashlib.sha1(kern.encode()).hexdigest()[:16]
    cache_map = os.path.join(CACHE, "overpass")
    cache_pad = os.path.join(cache_map, f"{sleutel}.json")
    if os.path.exists(cache_pad):
        print(f"  overpass uit cache ({sleutel})")
        with open(cache_pad, encoding="utf-8") as f:
            return json.load(f)

    data = urllib.parse.urlencode({"data": query}).encode()
    fout = None
    for ronde in range(OVERPASS_RONDES):
        if ronde:
            print(f"  alle mirrors bezet — ronde {ronde + 1}/{OVERPASS_RONDES} "
                  f"na {OVERPASS_PAUZE_S}s")
            time.sleep(OVERPASS_PAUZE_S)
        for url in OVERPASS_URLS:
            try:
                req = urllib.request.Request(url, data=data, headers={
                    "User-Agent": "grondstoffen-atlas/M24 (github.com/larswalters/grondstoffen-atlas)"})
                with urllib.request.urlopen(req, timeout=OVERPASS_CLIENT_S) as r:
                    antwoord = json.load(r)
                os.makedirs(cache_map, exist_ok=True)
                with open(cache_pad, "w", encoding="utf-8") as f:
                    json.dump(antwoord, f)
                return antwoord
            except Exception as e:  # noqa: BLE001 — mirror proberen, dan pas falen
                fout = e
                print(f"  overpass-mirror faalde ({url.split('/')[2]}): {e}")
    raise RuntimeError(f"alle Overpass-mirrors faalden na {OVERPASS_RONDES} rondes: {fout}")


def segmenten_osm(systeem):
    la0, lo0, la1, lo1 = systeem["bbox"]
    bbox = f"({la0},{lo0},{la1},{lo1})"
    delen = []
    # De CEMT-clause heeft géén naamfilter en scant dus élke waterway in de
    # bbox. Buiten Europa bestaat de tag niet, dus daar is dat pure kosten:
    # de Mississippi-delta (bayous!) liep er op beide mirrors in een timeout.
    # Alleen meenemen als het systeem zelf een CEMT-klasse draagt.
    if systeem.get("cemt"):
        delen.append(f'  way["waterway"~"^(river|canal|fairway)$"]["CEMT"]{bbox};')
    for naam in systeem["namen"]:
        # Exacte tag-match i.p.v. één naam-regex: Overpass indexeert key=value,
        # terwijl een regex een scan over alle waterways in de bbox afdwingt.
        # De oude regex was ^(...)$-geankerd, dus dit selecteert hetzelfde.
        delen.append(f'  way["waterway"~"^(river|canal|fairway)$"]["name"="{naam}"]{bbox};')
    query = ("[out:json][timeout:%d];\n(\n%s\n);\nout geom;\n"
             % (OVERPASS_SERVER_S, "\n".join(delen)))
    antwoord = overpass(query)
    segs = []
    cemt_gezien = {}
    for el in antwoord.get("elements", []):
        geom = el.get("geometry") or []
        if el.get("type") != "way" or len(geom) < 2:
            continue
        tags = el.get("tags") or {}
        pts = [(p["lon"], p["lat"]) for p in geom]
        naam = tags.get("name", "")
        segs.append((pts, naam))
        if tags.get("CEMT"):
            cemt_gezien[naam or f"way/{el.get('id')}"] = tags["CEMT"]
    return segs, cemt_gezien


# ---------------------------------------------------------------- bron: UNECE

def segmenten_bestand(pad, bbox):
    """GeoJSON of shapefile → segmenten binnen de (ruime) bbox."""
    la0, lo0, la1, lo1 = bbox
    marge = 0.15

    def binnen(pts):
        return any(lo0 - marge <= lo <= lo1 + marge and
                   la0 - marge <= la <= la1 + marge for lo, la in pts)

    segs = []
    if pad.lower().endswith((".geojson", ".json")):
        gj = json.load(open(pad, encoding="utf-8"))
        for f in gj.get("features", []):
            g = f.get("geometry") or {}
            props = f.get("properties") or {}
            naam = str(props.get("name") or props.get("NAME") or
                       props.get("Name") or props.get("SECTION_NA") or
                       props.get("EWW") or "")
            delen = []
            if g.get("type") == "LineString":
                delen = [g["coordinates"]]
            elif g.get("type") == "MultiLineString":
                delen = g["coordinates"]
            for deel in delen:
                pts = [(p[0], p[1]) for p in deel]
                if len(pts) >= 2 and binnen(pts):
                    segs.append((pts, naam))
    else:
        import shapefile  # pyshp — alleen nodig voor het shapefile-pad
        sf = shapefile.Reader(pad)
        velden = [f[0] for f in sf.fields[1:]]
        naam_veld = next((v for v in velden if v.lower() in
                          ("name", "naam", "eww", "waterway", "river")), None)
        for sr in sf.iterShapeRecords():
            shp = sr.shape
            if shp.shapeTypeName not in ("POLYLINE", "POLYLINEZ", "POLYLINEM"):
                continue
            naam = str(sr.record[velden.index(naam_veld)]) if naam_veld else ""
            grenzen = list(shp.parts) + [len(shp.points)]
            for i in range(len(grenzen) - 1):
                pts = [(p[0], p[1]) for p in shp.points[grenzen[i]:grenzen[i + 1]]]
                if len(pts) >= 2 and binnen(pts):
                    segs.append((pts, naam))
    return segs


# ---------------------------------------------------------------- stitcher

def kortste_waterpad(segs, anker_zee, anker_binnen, stitch_km):
    """Dijkstra over de segment-geometrie: zeezijde -> binnenzijde.

    Elke vertex is een graaf-knoop; opeenvolgende vertices van een segment zijn
    verbonden. Segment-UITEINDEN worden daarnaast gehecht aan elke vertex
    binnen stitch_km (bronnen delen niet altijd exacte knopen). Het resultaat
    is de kortste route over écht getekende waterweg-geometrie — takken en
    parallelle armen vallen er vanzelf uit.
    """
    knopen = []          # (lon, lat)
    knoop_id = {}
    buren = []           # per knoop: list[(buur, km, segment-index)]

    def nid(p):
        sleutel = (round(p[0], 6), round(p[1], 6))
        if sleutel not in knoop_id:
            knoop_id[sleutel] = len(knopen)
            knopen.append(sleutel)
            buren.append([])
        return knoop_id[sleutel]

    uiteinden = []
    for si, (pts, _naam) in enumerate(segs):
        vorige = None
        for j, p in enumerate(pts):
            k = nid(p)
            if vorige is not None and vorige != k:
                d = km(knopen[vorige], knopen[k])
                buren[vorige].append((k, d, si))
                buren[k].append((vorige, d, si))
            if j == 0 or j == len(pts) - 1:
                uiteinden.append(k)
            vorige = k

    # uiteinden hechten aan nabije vertices (grid-hash, cel ~ stitch-tolerantie)
    cel_graden = max(stitch_km / 70.0, 1e-4)
    grid = {}
    for i, (lo, la) in enumerate(knopen):
        grid.setdefault((int(lo / cel_graden), int(la / cel_graden)), []).append(i)

    def dichtbij(i, straal_km):
        lo, la = knopen[i]
        cx, cy = int(lo / cel_graden), int(la / cel_graden)
        r = max(1, int(straal_km / (cel_graden * 70.0)) + 1)
        for dx in range(-r, r + 1):
            for dy in range(-r, r + 1):
                for j in grid.get((cx + dx, cy + dy), ()):
                    if j != i:
                        yield j

    for i in set(uiteinden):
        for j in dichtbij(i, stitch_km):
            d = km(knopen[i], knopen[j])
            if d <= stitch_km:
                buren[i].append((j, d, -1))
                buren[j].append((i, d, -1))

    def dichtstbij(anker):
        beste, beste_d = -1, 1e18
        for i, p in enumerate(knopen):
            d = km(anker, p)
            if d < beste_d:
                beste, beste_d = i, d
        return beste, beste_d

    start, d_start = dichtstbij(anker_zee)
    doel, d_doel = dichtstbij(anker_binnen)
    if d_start > ANKER_TOL_KM or d_doel > ANKER_TOL_KM:
        raise RuntimeError(
            f"anker te ver van de geometrie: zee {d_start:.1f} km, binnen {d_doel:.1f} km "
            f"(tolerantie {ANKER_TOL_KM} km) — bbox/namenlijst dekt het traject niet")

    afstand = {start: 0.0}
    vorige = {}
    via_seg = {}
    pq = [(0.0, start)]
    klaar = set()
    while pq:
        d, k = heapq.heappop(pq)
        if k in klaar:
            continue
        klaar.add(k)
        if k == doel:
            break
        for buur, dd, si in buren[k]:
            nd = d + dd
            if nd < afstand.get(buur, 1e18):
                afstand[buur] = nd
                vorige[buur] = k
                via_seg[buur] = si
                heapq.heappush(pq, (nd, buur))
    if doel not in klaar:
        raise RuntimeError("geen doorlopend waterpad tussen de ankers gevonden "
                           "(stitch-tolerantie of dekking te krap)")

    pad = [doel]
    seg_volgorde = []
    k = doel
    while k != start:
        seg_volgorde.append(via_seg.get(k, -1))
        k = vorige[k]
        pad.append(k)
    pad.reverse()
    seg_volgorde.reverse()

    coords = [knopen[k] for k in pad]
    namen = []
    for si in seg_volgorde:
        naam = segs[si][1] if si >= 0 else None
        if naam and (not namen or namen[-1] != naam):
            namen.append(naam)
    return coords, afstand[doel], namen, (d_start, d_doel)


# ---------------------------------------------------------------- simplify

def simplify(pts, tol_km=SIMPLIFY_KM):
    """Douglas-Peucker (vlakke benadering met cos(lat) — prima op NL-schaal)."""
    if len(pts) < 3:
        return list(pts)
    coslat = math.cos(math.radians(sum(p[1] for p in pts) / len(pts)))

    def afstand_lijn(p, a, b):
        ax, ay = (a[0] - p[0]) * coslat, a[1] - p[1]
        bx, by = (b[0] - p[0]) * coslat, b[1] - p[1]
        dx, dy = bx - ax, by - ay
        den = math.hypot(dx, dy)
        if den < 1e-12:
            return math.hypot(ax, ay) * 111.2
        return abs(ax * dy - ay * dx) / den * 111.2

    houd = [False] * len(pts)
    houd[0] = houd[-1] = True
    stapel = [(0, len(pts) - 1)]
    while stapel:
        i, j = stapel.pop()
        if j <= i + 1:
            continue
        verste, verste_d = -1, -1.0
        for k in range(i + 1, j):
            d = afstand_lijn(pts[k], pts[i], pts[j])
            if d > verste_d:
                verste, verste_d = k, d
        if verste_d > tol_km:
            houd[verste] = True
            stapel.append((i, verste))
            stapel.append((verste, j))
    return [p for p, h in zip(pts, houd) if h]


# ---------------------------------------------------------------- hoofdflow

def haal(bron, bestand=None):
    features = []
    for systeem in SYSTEMEN:
        label = systeem["label"]
        print(f"\n[{label}] bron={bron}")
        if bron == "osm":
            segs, cemt_gezien = segmenten_osm(systeem)
        else:
            if not bestand:
                raise SystemExit("unece vereist --bestand <pad naar geojson/shapefile>")
            segs, cemt_gezien = segmenten_bestand(bestand, systeem["bbox"]), {}
        print(f"  segmenten: {len(segs)} · vertices: {sum(len(p) for p, _ in segs):,}")
        if not segs:
            raise RuntimeError(f"geen segmenten voor {label} — dekking/filters checken")

        coords, lengte, namen, anker_d = kortste_waterpad(
            segs, systeem["anker_zee"], systeem["anker_binnen"], STITCH_KM[bron])
        strak = simplify(coords)
        print(f"  pad: {lengte:.1f} km · {len(coords)} punten → {len(strak)} na simplify"
              f" · anker-afstanden zee {anker_d[0]:.2f} / binnen {anker_d[1]:.2f} km")
        if namen:
            print(f"  route: {' → '.join(namen[:12])}{' …' if len(namen) > 12 else ''}")
        if cemt_gezien:
            uniek = sorted(set(cemt_gezien.values()))
            print(f"  CEMT-tags gezien: {', '.join(uniek)}")

        features.append({
            "type": "Feature",
            "properties": {
                "label": label,
                "zeevaart": systeem["zeevaart"],
                "cemt": systeem["cemt"],
                "volgtOp": systeem.get("volgt_op", ""),
                "bron": bron,
                "km": round(lengte, 1),
                "route": " → ".join(namen),
                "ankerZee": list(systeem["anker_zee"]),
                "ankerBinnen": list(systeem["anker_binnen"]),
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [[round(lo, 6), round(la, 6)] for lo, la in strak],
            },
        })

    os.makedirs(CACHE, exist_ok=True)
    pad = os.path.join(CACHE, f"vaarwegen_{bron}.geojson")
    bronvermelding = ("OpenStreetMap contributors (ODbL) via Overpass API" if bron == "osm"
                      else "UNECE Blue Book database — E-waterway network (gis.unece.org)")
    with open(pad, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection",
                   "bron": bronvermelding,
                   "features": features}, f, ensure_ascii=False)
    print(f"\ngeschreven: {pad} ({os.path.getsize(pad) / 1024:.0f} KB)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("bron", choices=["osm", "unece"])
    ap.add_argument("--bestand", help="unece: pad naar geojson of shapefile")
    args = ap.parse_args()
    haal(args.bron, args.bestand)
