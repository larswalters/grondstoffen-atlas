#!/usr/bin/env python3
"""
bake_marnet.py — verzoent het MARNET-vaarlanen-netwerk ÉÉN KEER met de
1:10M-vectorwereld en bakt het als compact binair bestand voor v2 (LAR-483).

Waarom dit bestaat: corridors werden per haven-paar apart gebakken, waardoor
routes naar dezelfde bestemming niet bundelen, dezelfde kapotte edge steeds
opnieuw gerepareerd werd en antipodale paren willekeurig een halfrond kozen.
De fix: repareer het NETWERK één keer, route daarna haven→haven over de
schone graaf — tegen exact dezelfde kustlijn die v2 rendert (vector = waarheid).

MARNET is een grove graaf, geen waterkaart: segmentlengte mediaan 83 km maar
max 3.611 km. Zo'n koorde snijdt continenten aan. Daarom:
  1. verdichten   elke edge langs de grootcirkel bemonsteren (~10 km), zodat
                  de geometrie de bol volgt en land-toetsing betekenis heeft
  2. toetsen      elke edge fijn bemonsteren (~2 km) tegen de 1:10M-polygonen
                  (shapely STRtree — zelfde bron als v2/data/world-10m.bin)
  3. verzoenen    kanalen/rivieren uitzonderen (die zijn "land" in de polygonen
                  maar horen bij de route); échte landsnijders omleggen
  4. bakken       knopen + edges + geometrie als varint-binair naar v2/data/

Draaien:  python v2/tools/bake_marnet.py --analyse   (alleen rapport)
          python v2/tools/bake_marnet.py             (verzoenen + bakken)

Benodigd in v2/build-cache/ (gitignored, eenmalig downloaden):
  ne_10m_land.geojson, ne_10m_minor_islands.geojson, ne_10m_lakes.geojson
  van https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/
Python-dependencies (alleen build-time): searoute, shapely, numpy.
"""

import argparse
import heapq
import json
import math
import os
import sys

import numpy as np
from shapely import STRtree, points as shp_points
from shapely.geometry import LineString, Point, shape

# Windows-console is cp1252; zonder dit crasht een print met bv. '→'
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)
CACHE = os.path.join(V2, "build-cache")
DATA = os.path.join(V2, "data")

# searoute's data is de bron; het pakket is een build-dependency (runtime = JS)
import searoute
SR_DATA = os.path.join(os.path.dirname(searoute.__file__), "data")

DENS_KM = 10.0   # geometrie-verdichting: punt elke ~10 km langs de grootcirkel
TEST_KM = 2.0    # land-toetsing: monster elke ~2 km
R_AARDE = 6371.0

# ---------------------------------------------------------------- geometrie

def to3d(lon, lat):
    la, lo = math.radians(lat), math.radians(lon)
    return (math.cos(la) * math.cos(lo), math.cos(la) * math.sin(lo), math.sin(la))


def to_ll(v):
    x, y, z = v
    return (math.degrees(math.atan2(y, x)), math.degrees(math.asin(max(-1, min(1, z)))))


def gc_km(a, b):
    """Grootcirkel-afstand tussen (lon,lat)-paren."""
    d = sum(p * q for p, q in zip(to3d(*a), to3d(*b)))
    return R_AARDE * math.acos(max(-1.0, min(1.0, d)))


def slerp_pts(a, b, stap_km):
    """Punten langs de grootcirkel a->b (incl. beide eindpunten), elke ~stap_km.

    In 3D geïnterpoleerd: geen antimeridiaan-problemen, geen platte-kaart-koorden.
    """
    va, vb = to3d(*a), to3d(*b)
    dot = max(-1.0, min(1.0, sum(p * q for p, q in zip(va, vb))))
    hoek = math.acos(dot)
    lengte = R_AARDE * hoek
    n = max(1, math.ceil(lengte / stap_km))
    if hoek < 1e-9:
        return [a, b]
    uit = []
    sin_h = math.sin(hoek)
    for k in range(n + 1):
        t = k / n
        w1 = math.sin((1 - t) * hoek) / sin_h
        w2 = math.sin(t * hoek) / sin_h
        v = tuple(w1 * p + w2 * q for p, q in zip(va, vb))
        uit.append(to_ll(v))
    uit[0] = a
    uit[-1] = b
    return uit


# ---------------------------------------------------------------- landmasker

def _polys_uit(bestand):
    gj = json.load(open(os.path.join(CACHE, bestand), encoding="utf-8"))
    uit = []
    for f in gj["features"]:
        g = shape(f["geometry"])
        onderdelen = [g] if g.geom_type == "Polygon" else list(g.geoms)
        for p in onderdelen:
            # Natural Earth bevat "Null Island" (1 m² op exact 0,0) als
            # georeferentie-anker — geen echt land, weg ermee.
            minx, miny, maxx, maxy = p.bounds
            if abs(minx) < 0.01 and abs(miny) < 0.01 and abs(maxx) < 0.01 and abs(maxy) < 0.01:
                continue
            uit.append(p)
    return uit


class LandTester:
    """Land = binnen de 1:10M-landpolygonen én niet in een meer.

    De landpolygonen zijn exact dezelfde bron als de gerenderde vectorwereld.
    Meren (ne_10m_lakes) doen mee als water omdat MARNET er echte vaarwegen
    doorheen legt: de Grote Meren + Seaway, het IJsselmeer, de stuwmeren in
    het Wolga-Don-systeem. Zonder meren-als-water zou de halve Seaway als
    "kapot" gelden terwijl er niets aan mankeert.
    """

    def __init__(self):
        self.polys = load_land_polys()
        self.tree = STRtree(self.polys)
        self.meren = _polys_uit("ne_10m_lakes.geojson")
        self.meer_tree = STRtree(self.meren)

    def hits(self, lonlat_array):
        """Voor een (n,2) numpy-array van lon/lat: boolean-array 'ligt op land'."""
        pts = shp_points(lonlat_array)
        idx = self.tree.query(pts, predicate="within")
        mask = np.zeros(len(lonlat_array), dtype=bool)
        mask[idx[0]] = True
        if mask.any():
            meer_idx = self.meer_tree.query(pts[mask], predicate="within")
            op_meer = np.zeros(int(mask.sum()), dtype=bool)
            op_meer[meer_idx[0]] = True
            wie = np.flatnonzero(mask)
            mask[wie[op_meer]] = False
        return mask

    def is_land(self, lon, lat):
        return bool(self.hits(np.array([[lon, lat]]))[0])


def load_land_polys():
    polys = _polys_uit("ne_10m_land.geojson")
    polys.extend(_polys_uit("ne_10m_minor_islands.geojson"))
    return polys


# ---------------------------------------------------------------- netwerk

def load_marnet():
    """MARNET → lijst van (coords, passage) per lijn."""
    gj = json.load(open(os.path.join(SR_DATA, "marnet_searoute.geojson"), encoding="utf-8"))
    lijnen = []
    for f in gj["features"]:
        geom = f.get("geometry") or {}
        passage = (f.get("properties") or {}).get("passage")
        if geom.get("type") == "LineString":
            lijnen.append((geom["coordinates"], passage))
        elif geom.get("type") == "MultiLineString":
            for deel in geom["coordinates"]:
                lijnen.append((deel, passage))
    return lijnen


def bouw_graaf(lijnen):
    """Knopen (unieke coördinaten) + ongerichte edges (gededupliceerd).

    Lon wordt genormaliseerd naar [-180, 180): MARNET heeft 15 knopen die
    dubbel bestaan als +180 én -180 — hetzelfde fysieke punt, en precies de
    plek waar de trans-Pacific lanes elkaar horen te raken. Zonder deze wrap
    is de Stille Oceaan bij de datumgrens doorgeknipt en rekent de router
    Yokohama->LA via Suez én Panama (32.000 km) in plaats van rechtdoor.
    """
    node_id = {}
    nodes = []

    def nid(p):
        lon = ((p[0] + 180.0) % 360.0) - 180.0
        sleutel = (round(lon, 6), round(p[1], 6))
        if sleutel not in node_id:
            node_id[sleutel] = len(nodes)
            nodes.append(sleutel)
        return node_id[sleutel]

    edges = {}
    for coords, passage in lijnen:
        for i in range(len(coords) - 1):
            a, b = nid(coords[i]), nid(coords[i + 1])
            if a == b:
                continue
            sleutel = (min(a, b), max(a, b))
            if sleutel not in edges:
                edges[sleutel] = passage
            elif passage and not edges[sleutel]:
                edges[sleutel] = passage
    return nodes, edges


def componenten(nodes, edges):
    """Union-find; geeft component-id per knoop + groottes."""
    ouder = list(range(len(nodes)))

    def vind(x):
        while ouder[x] != x:
            ouder[x] = ouder[ouder[x]]
            x = ouder[x]
        return x

    for a, b in edges:
        ra, rb = vind(a), vind(b)
        if ra != rb:
            ouder[ra] = rb
    groottes = {}
    for i in range(len(nodes)):
        r = vind(i)
        groottes[r] = groottes.get(r, 0) + 1
    return vind, groottes


# ---------------------------------------------------------------- verzoening
#
# Drie klassen (gemeten in de analyse van 2026-07-18):
#   aanloop  treffer binnen ~5 km van een knoop: de knoop ligt in een dokbekken
#            of riviermond, binnen de kustlijnresolutie. Niets aan doen.
#   binnen   echt bevaarbaar binnenwater dat Natural Earth als land kent:
#            kanalen (Suez/Panama) en rivieren (Mississippi, Seaway-rivieren,
#            Wolga-Don, Paraná, Congo, Columbia, Alaska-bargeroutes). Als-is
#            bewaren, geflagd — M24 (binnenwater) verfijnt ze later.
#   kapot    een koorde die een kaap/eiland aansnijdt (Guyana-kust, Menorca,
#            Kamtsjatka, …). Omleggen: lokale A* over een fijn waterraster,
#            daarna trapjes eruit (simplify) met land-bewijs per kortsluiting.

PORT_TOL_KM = 5.0

# (naam, lat_min, lat_max, lon_min, lon_max)
WATERWEG_ZONES = [
    ("suez",              29.7, 31.4,   32.0,  32.7),
    ("panama",             8.7,  9.6,  -80.2, -79.3),
    ("mississippi",       28.8, 30.7,  -91.6, -89.3),
    ("seaway-stlawrence", 44.0, 47.2,  -76.6, -71.2),
    ("seaway-welland",    42.7, 43.6,  -79.9, -78.7),
    ("seaway-detroit",    41.9, 43.3,  -83.7, -82.1),
    ("seaway-stmarys",    46.0, 46.6,  -84.6, -83.9),
    ("wolga-don",         45.4, 49.0,   38.5,  48.6),
    ("parana",           -34.6,-32.4,  -61.2, -58.1),
    ("kuskokwim",         59.7, 63.3, -163.2,-154.8),
    ("kobuk",             66.4, 67.4, -163.6,-157.4),
    ("congo",             -6.3, -5.4,   12.2,  13.7),
    ("columbia",          45.4, 46.5, -123.7,-122.2),
    # rivieren/estuaria naar binnenhavens — MARNET vaart hier écht, maar de
    # vaarweg bestaat niet als water in de NE-polygonen (les van run 1)
    ("elbe-weser",        53.2, 54.0,    8.4,  10.1),   # Hamburg, Bremerhaven
    ("nl-delta",          51.6, 52.0,    3.9,   4.9),   # Haringvliet/Moerdijk
    ("severn",            51.3, 52.0,   -3.1,  -2.1),   # Bristol/Sharpness
    ("gironde",           44.8, 45.6,   -1.2,  -0.4),   # Bordeaux
    ("delaware",          39.4, 40.1,  -75.8, -74.9),   # Philadelphia
    ("hooghly",           21.5, 22.7,   87.7,  88.4),   # Kolkata
    ("yangtze",           31.7, 32.5,  118.4, 121.3),   # Nanjing–Jiangyin
    ("gulf-icw",          29.2, 30.3,  -94.2, -91.9),   # Sabine/Calcasieu/Vermilion
    ("pascagoula",        30.0, 30.5,  -88.8, -88.3),
    ("st-johns",          30.1, 30.5,  -81.8, -81.2),   # Jacksonville
    ("laguna-madre",      25.8, 26.8,  -97.6, -97.0),   # Brownsville
    ("bonny",              4.2,  4.9,    6.9,   7.4),   # Port Harcourt
    ("gabon-estuarium",    0.0,  1.1,    8.5,   9.7),   # Libreville/Owendo
    ("maracaibo",         10.4, 11.3,  -71.8, -71.3),
    ("dnipro-bug",        46.3, 47.1,   30.7,  32.1),   # Mykolaiv/Cherson
    ("khor-abdullah",     29.7, 30.6,   47.7,  48.9),   # Umm Qasr/Basra
    ("aysen",            -45.9,-45.1,  -74.1, -73.4),   # Puerto Chacabuco
]


def in_zone(lon, lat):
    for naam, la0, la1, lo0, lo1 in WATERWEG_ZONES:
        if la0 <= lat <= la1 and lo0 <= lon <= lo1:
            return naam
    return None


def wrap_lon(lon):
    return ((lon + 180.0) % 360.0) - 180.0


def edge_monsters(pa, pb, stap_km=TEST_KM):
    """Monsterpunten + afstand-tot-dichtstbijzijnd-eindpunt langs de edge."""
    lengte = gc_km(pa, pb)
    pts = slerp_pts(pa, pb, stap_km)[1:-1]
    n = len(pts) + 1
    rand = [min(lengte * k / n, lengte - lengte * k / n) for k in range(1, n)]
    return pts, rand, lengte


def polyline_land_ok(land, pts_lijst, tol_eind=(PORT_TOL_KM, PORT_TOL_KM), stap_km=1.0):
    """Toetst een hele polyline fijn; treffers binnen tol van de UITEINDEN mogen.

    De tolerantie is per uiteinde: een knoop die zelf in een lagune of dokbekken
    ligt (binnen de kustlijnresolutie) maakt de eerste kilometers onvermijdelijk
    "land" — dat mag, mits het bij het oorspronkelijke haven-aanloopstuk blijft.
    """
    tol_a, tol_b = tol_eind
    lengtes = [gc_km(pts_lijst[i], pts_lijst[i + 1]) for i in range(len(pts_lijst) - 1)]
    totaal = sum(lengtes)
    monsters = []
    afgelegd = 0.0
    for i in range(len(pts_lijst) - 1):
        stuk = slerp_pts(pts_lijst[i], pts_lijst[i + 1], stap_km)
        n = len(stuk) - 1
        for k in range(1, n):
            monsters.append((stuk[k], afgelegd + lengtes[i] * k / n))
        afgelegd += lengtes[i]
    if not monsters:
        return True
    arr = np.array([[wrap_lon(p[0]), p[1]] for p, _ in monsters])
    mask = land.hits(arr)
    for (p, langs), raak in zip(monsters, mask):
        if raak and langs > tol_a and (totaal - langs) > tol_b:
            return False
    return True


def eind_toleranties(land, pa, pb, stap_km=1.0, gat_km=3.0, plafond_km=30.0):
    """Hoe ver het onvermijdelijke haven-aanloopstuk op land ligt, per uiteinde.

    Gemeten op de OORSPRONKELIJKE koorde: vanaf elk uiteinde doorlopen zolang de
    treffers aaneengesloten zijn (gaatjes < gat_km mogen). Zo krijgt een knoop
    diep in een dokbekken de ruimte die hij nodig heeft, zonder dat een los
    eiland verderop óók door de vingers wordt gezien.
    """
    pts, rand, lengte = edge_monsters(pa, pb, stap_km)
    if not pts:
        return (PORT_TOL_KM, PORT_TOL_KM)
    arr = np.array([[wrap_lon(lo), la] for lo, la in pts])
    mask = land.hits(arr)
    n = len(pts) + 1

    def extent(voorwaarts):
        volgorde = range(len(pts)) if voorwaarts else range(len(pts) - 1, -1, -1)
        laatste = 0.0
        for k in volgorde:
            langs = lengte * (k + 1) / n
            afstand = langs if voorwaarts else (lengte - langs)
            if mask[k]:
                if afstand - laatste > gat_km:
                    break
                laatste = afstand
            elif afstand - laatste > gat_km:
                break
        return laatste

    tol_a = min(plafond_km, max(PORT_TOL_KM, extent(True) + 2.0))
    tol_b = min(plafond_km, max(PORT_TOL_KM, extent(False) + 2.0))
    return (tol_a, tol_b)


def detour(pa, pb, land, cell=0.02, gebufferd=True):
    """Lokale A* over een fijn waterraster in de bbox van de edge (+1,5°).

    Zelfde aanpak als de bewezen `detour_around_land` uit tools/bake_searoutes.py,
    maar: (1) tegen de 1:10M-wereld i.p.v. 1:50M, (2) cel 0,02° of fijner
    (zeestraten), (3) antimeridiaan-bestendig via een verschoven lon-frame,
    (4) het waterraster in één bulk-query, (5) desnoods zónder kustbuffer —
    in een nauwe straat (Dardanellen, fjorden) knijpt de buffer het kanaal
    dicht en is kaal water de enige weg.
    """
    lons = [pa[0], pb[0]]
    shift = 0.0
    if abs(lons[0] - lons[1]) > 180.0:
        # werk in een 0..360-frame zodat de bbox niet om de wereld heen slaat
        shift = 360.0
        lons = [lo + shift if lo < 0 else lo for lo in lons]
    lo0, lo1 = min(lons) - 1.5, max(lons) + 1.5
    la0 = min(pa[1], pb[1]) - 1.5
    la1 = max(pa[1], pb[1]) + 1.5
    la0, la1 = max(-89.0, la0), min(89.0, la1)

    nx = int((lo1 - lo0) / cell) + 1
    ny = int((la1 - la0) / cell) + 1
    if nx * ny > 1_500_000:
        return None  # onwaarschijnlijk groot — liever expliciet falen dan minuten malen

    xs = lo0 + np.arange(nx) * cell
    ys = la0 + np.arange(ny) * cell
    gx, gy = np.meshgrid(xs, ys)
    vlak = np.column_stack([((gx.ravel() + 180.0) % 360.0) - 180.0, gy.ravel()])
    water = ~land.hits(vlak).reshape(ny, nx)

    if gebufferd:
        # kustbuffer van één cel: anders scheert de omleiding zó strak langs de
        # kust dat de getekende grootcirkel-koorde alsnog land raakt
        raster = water.copy()
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dy or dx:
                    raster &= np.roll(np.roll(water, dy, axis=0), dx, axis=1)
        # roll wikkelt randen om — randcellen conservatief dichtzetten
        raster[0, :] = raster[-1, :] = raster[:, 0] = raster[:, -1] = False
    else:
        raster = water

    def celvan(p):
        lo = p[0] + shift if (shift and p[0] < 0) else p[0]
        return (min(ny - 1, max(0, round((p[1] - la0) / cell))),
                min(nx - 1, max(0, round((lo - lo0) / cell))))

    def snap(c):
        y0, x0 = c
        for r in range(0, 40):
            beste = None
            for dy in range(-r, r + 1):
                for dx in range(-r, r + 1):
                    if max(abs(dy), abs(dx)) != r:
                        continue
                    y, x = y0 + dy, x0 + dx
                    if 0 <= y < ny and 0 <= x < nx and raster[y, x]:
                        d = dy * dy + dx * dx
                        if beste is None or d < beste[0]:
                            beste = (d, (y, x))
            if beste:
                return beste[1]
        return None

    start = snap(celvan(pa))
    doel = snap(celvan(pb))
    if not start or not doel:
        return None

    coslat = max(0.05, math.cos(math.radians((pa[1] + pb[1]) / 2)))

    def h(c):
        return math.hypot(c[0] - doel[0], (c[1] - doel[1]) * coslat)

    openq = [(h(start), 0.0, start, None)]
    kwam = {}
    gbest = {start: 0.0}
    while openq:
        _f, g, cur, par = heapq.heappop(openq)
        if cur in kwam:
            continue
        kwam[cur] = par
        if cur == doel:
            break
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if not dy and not dx:
                    continue
                y, x = cur[0] + dy, cur[1] + dx
                if not (0 <= y < ny and 0 <= x < nx) or not raster[y, x]:
                    continue
                ng = g + math.hypot(dy, dx * coslat)
                if ng < gbest.get((y, x), 1e18):
                    gbest[(y, x)] = ng
                    heapq.heappush(openq, (ng + h((y, x)), ng, (y, x), cur))
    if doel not in kwam:
        return None
    pad = []
    c = doel
    while c is not None:
        pad.append(c)
        c = kwam[c]
    pad.reverse()
    # decimeren alleen bij lange paden; in nauw water telt élke cel — de
    # eindpunten vult de aanroeper met de echte knopen in
    stap = 2 if len(pad) > 80 else 1
    return [(wrap_lon(lo0 + x * cell), la0 + y * cell) for y, x in pad[1:-1:stap]]


def _kruis_km(p, a, b):
    """Loodrechte afstand van p tot de lijn a->b (vlak, lokaal genoeg)."""
    coslat = math.cos(math.radians(p[1]))
    ax, ay = (a[0] - p[0]) * coslat, a[1] - p[1]
    bx, by = (b[0] - p[0]) * coslat, b[1] - p[1]
    dx, dy = bx - ax, by - ay
    den = math.hypot(dx, dy)
    if den < 1e-9:
        return math.hypot(ax, ay) * 111.2
    return abs(ax * dy - ay * dx) / den * 111.2


def simplify_water(pts, land, tol_km=12.0, max_koorde_km=400.0):
    """Trapjes eruit: een punt vervalt alleen als het < tol_km van de lijn
    buur->buur ligt én die kortsluiting aantoonbaar over water loopt (fijn
    bemonsterd — de les van de Channel Islands uit de oude baker)."""
    pts = list(pts)
    weg = 0
    veranderd = True
    while veranderd:
        veranderd = False
        i = 1
        while i < len(pts) - 1:
            a, p, b = pts[i - 1], pts[i], pts[i + 1]
            koorde = gc_km(a, b)
            probe = min(2.0, max(0.4, koorde / 12.0))
            if koorde <= max_koorde_km and _kruis_km(p, a, b) < tol_km:
                tussen = slerp_pts(a, b, probe)[1:-1]
                if tussen:
                    arr = np.array([[wrap_lon(q[0]), q[1]] for q in tussen])
                    schoon = not land.hits(arr).any()
                else:
                    schoon = True
                if schoon:
                    del pts[i]
                    weg += 1
                    veranderd = True
                    continue
            i += 1
    return pts, weg


# ---------------------------------------------------------------- analyse

def analyse():
    land = LandTester()
    print(f"landmasker: {len(land.polys):,} polygonen (1:10M land + minor islands)")

    lijnen = load_marnet()
    nodes, edges = bouw_graaf(lijnen)
    print(f"netwerk: {len(nodes):,} knopen · {len(edges):,} edges (gededupliceerd)")

    _, comp_groottes = componenten(nodes, edges)
    top = sorted(comp_groottes.values(), reverse=True)[:8]
    print(f"componenten: {len(comp_groottes)} — grootste: {top}")

    # Elke edge fijn bemonsteren en in één bulk-query tegen het landmasker.
    # Per monster ook de afstand tot het dichtstbijzijnde eindpunt: een treffer
    # vlak bij een knoop is een haven-AANLOOP (knoop ligt in een dokbekken of
    # riviermond, binnen de 1:10M-kustlijnresolutie), geen kapotte edge.
    PORT_TOL_KM = 5.0
    monster_pts = []
    monster_edge = []
    monster_bij_haven = []
    edge_lijst = list(edges.items())
    totaal_km = 0.0
    for ei, ((a, b), _passage) in enumerate(edge_lijst):
        pa, pb = nodes[a], nodes[b]
        lengte = gc_km(pa, pb)
        totaal_km += lengte
        pts = slerp_pts(pa, pb, TEST_KM)[1:-1]  # eindpunten zijn knopen — apart
        n = len(pts) + 1
        for k, p in enumerate(pts, start=1):
            langs = lengte * k / n
            monster_pts.append(p)
            monster_edge.append(ei)
            monster_bij_haven.append(min(langs, lengte - langs) <= PORT_TOL_KM)
    monster_pts = np.array(monster_pts)
    monster_edge = np.array(monster_edge)
    monster_bij_haven = np.array(monster_bij_haven)
    print(f"totale netwerklengte: {totaal_km:,.0f} km · {len(monster_pts):,} monsterpunten (~{TEST_KM} km)")

    mask = land.hits(monster_pts)
    print(f"monsterpunten op land: {mask.sum():,} "
          f"(waarvan {int((mask & monster_bij_haven).sum()):,} binnen {PORT_TOL_KM:.0f} km van een knoop = aanloop)")
    # Aanloop-treffers doen niet mee in de kapot-classificatie.
    mask = mask & ~monster_bij_haven

    # Ook de knopen zelf toetsen (een knoop óp land is een eigen probleemklasse).
    node_arr = np.array(nodes, dtype=float)
    node_land = land.hits(node_arr)
    print(f"knopen op land: {node_land.sum():,} van {len(nodes):,}")

    # Treffers clusteren per 1°-cel zodat je ziet WAAR het pijn doet.
    hit_pts = monster_pts[mask]
    hit_edges = monster_edge[mask]
    clusters = {}
    for (lon, lat), ei in zip(hit_pts, hit_edges):
        cel = (round(lat), round(lon))
        c = clusters.setdefault(cel, {"n": 0, "edges": set()})
        c["n"] += 1
        c["edges"].add(int(ei))

    kapotte_edges = sorted({int(e) for e in hit_edges})
    print(f"edges met land-treffers: {len(kapotte_edges):,} van {len(edge_lijst):,}")
    print("\n--- clusters (1°-cellen, gesorteerd op treffers) ---")
    for (lat, lon), c in sorted(clusters.items(), key=lambda kv: -kv[1]["n"])[:40]:
        vb_edge = edge_lijst[min(c["edges"])]
        (a, b), passage = vb_edge
        pa, pb = nodes[a], nodes[b]
        print(f"  lat {lat:>4} lon {lon:>5} · {c['n']:>4} treffers · {len(c['edges'])} edges"
              f" · vb ({pa[1]:.2f},{pa[0]:.2f})->({pb[1]:.2f},{pb[0]:.2f})"
              f"{' · passage=' + passage if passage else ''}")

    # Verdeling van treffer-fractie per edge: snijdt een edge land 'even aan'
    # (koorde langs een kaap) of ligt hij er grotendeels op (rivier/kanaal)?
    per_edge = {}
    for ei in hit_edges:
        per_edge[int(ei)] = per_edge.get(int(ei), 0) + 1
    totaal_per_edge = {}
    for ei in monster_edge:
        totaal_per_edge[int(ei)] = totaal_per_edge.get(int(ei), 0) + 1
    fracties = [per_edge[e] / max(1, totaal_per_edge[e]) for e in kapotte_edges]
    fr = np.array(fracties)
    print(f"\ntreffer-fractie per kapotte edge: mediaan {np.median(fr):.0%} · "
          f">50% land: {(fr > 0.5).sum()} edges · <10% land: {(fr < 0.1).sum()} edges")

    # Diagnosepunten voor de wateren die géén oceaan zijn in Natural Earth land:
    diag = {
        "Kaspische Zee (41.5N 50.5E)": (50.5, 41.5),
        "Bovenmeer/Superior (47.7N 87.5W)": (-87.5, 47.7),
        "Michiganmeer (43.5N 87.2W)": (-87.2, 43.5),
        "Zwarte Zee (43N 34E)": (34.0, 43.0),
    }
    for naam, (lon, lat) in diag.items():
        print(f"  {'LAND ' if land.is_land(lon, lat) else 'water'} · {naam}")


# ------------------------------------------------------- M24: extra vaarwegen
#
# Binnenwater bestaat niet als water in de NE-polygonen — dáárom waren de
# WATERWEG_ZONES hierboven vrijstellingen. Voor de vaarwegen die we zélf
# toevoegen (LAR-486) geldt daarom de CORRIDOR-TOETS in plaats van de
# vlak-toets: elk gebakken geometriepunt moet <= CORRIDOR_EPS_KM van de
# bron-middellijn (fetch_waterways.py) liggen. De polygoon-toets blijft
# alleen op de zee-overgang gelden: de aansluitknoop moet in NE-water liggen.

KETEN_KM = 15.0         # nieuwe knoop elke ~15 km (havens snappen op knopen)
AANSLUIT_MAX_KM = 30.0  # zeezijde moet zó dicht bij een MARNET-knoop beginnen
CORRIDOR_EPS_KM = 0.25  # kwantisering (11 m) + simplify (25 m) blijven hier ruim onder


def extra_vaarwegen(land, nodes, edge_lijst, status, geometrie, pad):
    """Hangt vaarweg-ketens uit fetch_waterways.py aan de graaf (in-place).

    Per systeem: zeezijde hechten aan de dichtstbijzijnde ORIGINELE
    MARNET-knoop, dan nieuwe knopen elke ~KETEN_KM met edges soort=1 en
    passage=systeemlabel (het bestaande vermijd-mechanisme = meteen de
    M26/M21-filterknop). Geeft de meta per systeem terug voor marnet.json.
    """
    gj = json.load(open(pad, encoding="utf-8"))
    n_orig = len(nodes)
    orig_xyz = np.array([to3d(lo, la) for lo, la in nodes[:n_orig]])
    uit = {}
    print(f"\nextra vaarwegen uit {os.path.basename(pad)}:")
    for f in gj["features"]:
        props = f["properties"]
        label = props["label"]
        coords = [(wrap_lon(lo), la) for lo, la in f["geometry"]["coordinates"]]

        # zee-overgang: dichtstbijzijnde originele knoop (3D-dot = grootcirkel-proxy)
        v = np.array(to3d(*coords[0]))
        d = orig_xyz @ v
        zeeknoop = int(np.argmax(d))
        aansluit_km = R_AARDE * math.acos(max(-1.0, min(1.0, float(d[zeeknoop]))))
        if aansluit_km > AANSLUIT_MAX_KM:
            raise RuntimeError(f"{label}: zeezijde ligt {aansluit_km:.1f} km van de "
                               f"dichtstbijzijnde MARNET-knoop (max {AANSLUIT_MAX_KM})")
        # Polygoon-toets op de zee-overgang, met de M23-nuance: een knoop in een
        # dokbekken/estuarium is NE-"land" maar ligt in een WATERWEG_ZONE — daar
        # vaart MARNET écht (bv. de Maasmond-knoop 6812 in zone nl-delta).
        overgang = "water"
        if land.is_land(*nodes[zeeknoop]):
            zone = in_zone(*nodes[zeeknoop])
            if not zone:
                lo, la = nodes[zeeknoop]
                raise RuntimeError(f"{label}: aansluitknoop {zeeknoop} ({la:.3f},{lo:.3f}) "
                                   f"ligt op land buiten elke waterweg-zone — "
                                   f"zee-overgang ongeldig")
            overgang = f"zone:{zone}"

        # keten bouwen: aansluitknoop -> nieuwe knopen elke ~KETEN_KM -> eindknoop
        lijn = [nodes[zeeknoop]] + coords
        keten_edges = []
        vorige_knoop = zeeknoop
        stuk = [lijn[0]]
        stuk_km = 0.0
        for i in range(1, len(lijn)):
            stuk.append(lijn[i])
            stuk_km += gc_km(lijn[i - 1], lijn[i])
            if stuk_km >= KETEN_KM or i == len(lijn) - 1:
                nodes.append((round(lijn[i][0], 6), round(lijn[i][1], 6)))
                nieuw = len(nodes) - 1
                ei = len(edge_lijst)
                edge_lijst.append(((vorige_knoop, nieuw), label))
                status[ei] = "binnen:" + label
                geometrie[ei] = list(stuk)
                keten_edges.append(ei)
                vorige_knoop = nieuw
                stuk = [lijn[i]]
                stuk_km = 0.0

        # corridor-toets (lokale vlakke projectie — prima op systeemschaal);
        # het aansluitstukje zeeknoop->bronlijn valt buiten de toets.
        lat0 = math.radians(sum(la for _lo, la in coords) / len(coords))
        sx = 111.2 * math.cos(lat0)
        bron_lijn = LineString([(lo * sx, la * 111.2) for lo, la in coords])
        ergste = 0.0
        for ei in keten_edges:
            for lo, la in geometrie[ei]:
                if gc_km((lo, la), coords[0]) <= aansluit_km + 1.0:
                    continue
                d_km = bron_lijn.distance(Point(lo * sx, la * 111.2))
                if d_km > ergste:
                    ergste = d_km
        if ergste > CORRIDOR_EPS_KM:
            raise RuntimeError(f"{label}: corridor-toets faalt — gebakken geometrie "
                               f"ligt {ergste:.2f} km van de bron-middellijn "
                               f"(eps {CORRIDOR_EPS_KM})")

        km_tot = sum(gc_km(a, b) for a, b in zip(lijn, lijn[1:]))
        uit[label] = {
            "zeevaart": bool(props.get("zeevaart")),
            "cemt": props.get("cemt", ""),
            "bron": props.get("bron", ""),
            "km": round(km_tot, 1),
            "edges": keten_edges,
            "aansluitKnoop": zeeknoop,
            "aansluitKm": round(aansluit_km, 2),
            "aansluitOvergang": overgang,
        }
        print(f"  {label:<16} {km_tot:6.1f} km · {len(keten_edges)} edges · aansluiting "
              f"knoop {zeeknoop} ({aansluit_km:.2f} km, {overgang}) · corridor max "
              f"{ergste * 1000:.0f} m · zeevaart={bool(props.get('zeevaart'))}")
    return uit


# ---------------------------------------------------------------- bakken

def varint(uit, waarde):
    """Zigzag + varint, identiek aan bake_world.py."""
    zz = (waarde << 1) ^ (waarde >> 63)
    zz &= 0xFFFFFFFFFFFFFFFF
    while True:
        byte = zz & 0x7F
        zz >>= 7
        if zz:
            uit.append(byte | 0x80)
        else:
            uit.append(byte)
            break


SCHAAL = 10000  # 1e-4 graden per eenheid, zelfde raster als world-10m


def verzoen_en_bak(vaarwegen_pad=None, suffix=""):
    land = LandTester()
    print(f"landmasker: {len(land.polys):,} polygonen + {len(land.meren):,} meren")

    lijnen = load_marnet()
    nodes, edges = bouw_graaf(lijnen)
    edge_lijst = list(edges.items())
    print(f"netwerk: {len(nodes):,} knopen · {len(edge_lijst):,} edges")

    # --- verzoening: classificeren + omleggen (of uit cache) ----------------
    # De verzoening hangt alléén aan het MARNET-netwerk + de NE-polygonen en is
    # deterministisch — maar kost ~35 min (150 omleg-A*'s over fijne rasters).
    # M24 bakt herhaaldelijk (bake-off-varianten, pilots), dus het resultaat
    # wordt gecached in build-cache/ en hergebruikt zolang de graaf gelijk is.
    cache_pad = os.path.join(CACHE, "verzoening_cache.json")
    herbruik = None
    if os.path.exists(cache_pad):
        try:
            c = json.load(open(cache_pad, encoding="utf-8"))
            if c.get("knopen") == len(nodes) and c.get("edges") == len(edge_lijst):
                herbruik = c
        except (json.JSONDecodeError, OSError):
            herbruik = None

    if herbruik:
        status = {int(k): v for k, v in herbruik["status"].items()}
        geometrie = {int(k): [tuple(p) for p in v] for k, v in herbruik["geometrie"].items()}
        onopgelost = list(herbruik["onopgelost"])
        kapot = [ei for ei, s in status.items() if s == "kapot"]
        binnen = [ei for ei, s in status.items() if s.startswith("binnen:")]
        print(f"verzoening uit cache: {len(kapot)} kapot · {len(binnen)} binnenwater · "
              f"{len(kapot) - len(onopgelost)} omgelegd · {len(onopgelost)} onopgelost")
    else:
        monster_pts, monster_edge, monster_rand = [], [], []
        for ei, ((a, b), _p) in enumerate(edge_lijst):
            pts, rand, _lengte = edge_monsters(nodes[a], nodes[b])
            monster_pts.extend(pts)
            monster_edge.extend([ei] * len(pts))
            monster_rand.extend(rand)
        arr = np.array([[wrap_lon(lo), la] for lo, la in monster_pts])
        m_edge = np.array(monster_edge)
        m_rand = np.array(monster_rand)
        mask = land.hits(arr)
        echt = mask & (m_rand > PORT_TOL_KM)

        status = {}   # ei -> "binnen:<zone>" | "kapot"
        for ei in sorted({int(e) for e in m_edge[echt]}):
            eigen = arr[echt & (m_edge == ei)]
            zones = {in_zone(lo, la) for lo, la in eigen}
            if None not in zones:
                status[ei] = "binnen:" + sorted(zones)[0]
            else:
                status[ei] = "kapot"

        kapot = [ei for ei, s in status.items() if s == "kapot"]
        binnen = [ei for ei, s in status.items() if s.startswith("binnen:")]
        print(f"classificatie: {len(kapot)} kapot · {len(binnen)} binnenwater · "
              f"{len(edge_lijst) - len(status)} schoon")

        # Kapotte edges omleggen — pogingen van grof-met-buffer naar
        # fijn-zonder-buffer: de buffer beschermt tegen kust-scheren, maar
        # knijpt nauwe straten (Dardanellen, fjorden, Inside Passage) dicht —
        # daar is fijn en kaal water de enige weg.
        geometrie = {}   # ei -> polyline [(lon,lat), ...] (alleen afwijkend van de koorde)
        onopgelost = []
        for ei in kapot:
            (a, b), _p = edge_lijst[ei]
            pa, pb = nodes[a], nodes[b]
            tol = eind_toleranties(land, pa, pb)
            gelukt = False
            for cell, gebufferd in ((0.02, True), (0.01, True), (0.01, False), (0.02, False)):
                om = detour(pa, pb, land, cell=cell, gebufferd=gebufferd)
                if om is None:
                    continue
                lijn = [pa] + om + [pb]
                lijn, _weg = simplify_water(lijn, land)
                if polyline_land_ok(land, lijn, tol_eind=tol):
                    geometrie[ei] = lijn
                    gelukt = True
                    break
            if not gelukt:
                onopgelost.append(ei)
                print(f"  ONOPGELOST: edge {ei} ({pa[1]:.2f},{pa[0]:.2f})->({pb[1]:.2f},{pb[0]:.2f})"
                      f" tol=({tol[0]:.0f},{tol[1]:.0f})")
        print(f"omgelegd: {len(kapot) - len(onopgelost)} van {len(kapot)} kapotte edges")

        with open(cache_pad, "w", encoding="utf-8") as f:
            json.dump({"knopen": len(nodes), "edges": len(edge_lijst),
                       "status": {str(k): v for k, v in status.items()},
                       "geometrie": {str(k): [[p[0], p[1]] for p in v]
                                     for k, v in geometrie.items()},
                       "onopgelost": onopgelost}, f)
        print(f"verzoening gecached: {os.path.basename(cache_pad)} "
              f"({os.path.getsize(cache_pad) / 1024:,.0f} KB)")

    # --- M24: vaarweg-ketens aanhangen (LAR-486) ----------------------------
    vaarwegen_meta = {}
    if vaarwegen_pad:
        vaarwegen_meta = extra_vaarwegen(land, nodes, edge_lijst, status,
                                         geometrie, vaarwegen_pad)

    # --- geometrie verdichten + kwantiseren ---------------------------------
    def verdicht(lijn):
        uit = []
        for i in range(len(lijn) - 1):
            deel = slerp_pts(lijn[i], lijn[i + 1], DENS_KM)
            if i:
                deel = deel[1:]
            uit.extend(deel)
        return uit

    def q(p):
        return (int(round(wrap_lon(p[0]) * SCHAAL)), int(round(p[1] * SCHAAL)))

    node_q = [q(p) for p in nodes]

    edge_geoms = []
    edge_lengtes = []
    totaal_punten = 0
    for ei, ((a, b), _p) in enumerate(edge_lijst):
        lijn = geometrie.get(ei) or [nodes[a], nodes[b]]
        dicht = verdicht(lijn)
        lengte = sum(gc_km(dicht[i], dicht[i + 1]) for i in range(len(dicht) - 1))
        pts = [node_q[a]]
        for p in dicht[1:-1]:
            kp = q(p)
            if kp != pts[-1]:
                pts.append(kp)
        if node_q[b] != pts[-1]:
            pts.append(node_q[b])
        elif len(pts) == 1:
            pts.append(node_q[b])
        edge_geoms.append(pts)
        edge_lengtes.append(lengte)
        totaal_punten += len(pts)

    # --- wegschrijven --------------------------------------------------------
    # Eén sequentieel bestand, drie blokken (de lezer kent alle aantallen):
    #   1. knopen: delta-gecodeerde lon/lat (zigzag-varint), volgorde = knoop-id
    #   2. edges:  per edge a, b (delta t.o.v. vorige edge), lengte (0,1 km),
    #              soort (0=zee, 1=binnenwater), aantal geometriepunten
    #   3. geometrie: per edge de punten 2..n als delta's t.o.v. het vorige punt
    #              (punt 1 = knoop a, staat er dus niet nog eens in)
    uit = bytearray()
    px = py = 0
    for x, y in node_q:
        varint(uit, x - px)
        varint(uit, y - py)
        px, py = x, y

    vorige_a = vorige_b = 0
    for ei, ((a, b), _p) in enumerate(edge_lijst):
        soort = 1 if status.get(ei, "").startswith("binnen:") else 0
        varint(uit, a - vorige_a)
        varint(uit, b - vorige_b)
        varint(uit, int(round(edge_lengtes[ei] * 10)))
        varint(uit, soort)
        varint(uit, len(edge_geoms[ei]))
        vorige_a, vorige_b = a, b

    for ei in range(len(edge_lijst)):
        pts = edge_geoms[ei]
        px, py = pts[0]
        for x, y in pts[1:]:
            varint(uit, x - px)
            varint(uit, y - py)
            px, py = x, y

    os.makedirs(DATA, exist_ok=True)
    bin_pad = os.path.join(DATA, f"marnet{suffix}.bin")
    with open(bin_pad, "wb") as f:
        f.write(uit)

    passages = {str(ei): p for ei, ((_a, _b), p) in enumerate(edge_lijst) if p}
    bron = ("Eurostat MARNET via searoute 1.6.0; verzoend met Natural Earth 1:10M "
            "(land + minor islands, meren als water) — LAR-483")
    if vaarwegen_meta:
        bron += ("; vaarwegen (M24/LAR-486): "
                 + ", ".join(f"{k} [{v['bron']}]" for k, v in vaarwegen_meta.items()))
    meta = {
        "schaal": SCHAAL,
        "knopen": len(nodes),
        "edges": len(edge_lijst),
        "punten": totaal_punten,
        "netwerkKm": round(sum(edge_lengtes)),
        "soorten": {"0": "zee", "1": "binnenwater"},
        "passages": passages,
        "vaarwegen": vaarwegen_meta,
        "bron": bron,
    }
    json_pad = os.path.join(DATA, f"marnet{suffix}.json")
    with open(json_pad, "w", encoding="utf-8") as f:
        json.dump(meta, f, separators=(",", ":"))

    n_vaarweg = sum(len(v["edges"]) for v in vaarwegen_meta.values())
    print(f"\n  knopen        : {len(nodes):,}")
    print(f"  edges         : {len(edge_lijst):,}  (binnenwater: {len(binnen)} + {n_vaarweg} vaarweg-edges, "
          f"omgelegd: {len(kapot) - len(onopgelost)}, onopgelost: {len(onopgelost)})")
    print(f"  geometrie     : {totaal_punten:,} punten ({DENS_KM:.0f} km-verdichting)")
    print(f"  netwerklengte : {sum(edge_lengtes):,.0f} km")
    print(f"  {os.path.basename(bin_pad):<14}: {os.path.getsize(bin_pad) / 1024:,.0f} KB")
    print(f"  {os.path.basename(json_pad):<14}: {os.path.getsize(json_pad) / 1024:,.0f} KB")

    bak_havens(nodes, node_q, suffix)
    return onopgelost


def bak_havens(nodes, node_q, suffix=""):
    """searoute's havens, gesnapt aan de dichtstbijzijnde netwerk-knoop."""
    gj = json.load(open(os.path.join(SR_DATA, "ports.geojson"), encoding="utf-8"))
    havens = []
    for f in gj["features"]:
        lon, lat = f["geometry"]["coordinates"]
        p = f["properties"]
        havens.append((p.get("name") or p.get("port"), p.get("cty") or "", p.get("port") or "", lon, lat))
    havens.sort(key=lambda h: (h[1], h[0]))

    # dichtstbijzijnde knoop in 3D (koorde-afstand = monotone proxy voor grootcirkel)
    knoop_xyz = np.array([to3d(lo / SCHAAL, la / SCHAAL) for lo, la in node_q])
    namen, landen, locodes, ll, knoop, afstand = [], [], [], [], [], []
    for naam, cty, code, lon, lat in havens:
        v = np.array(to3d(lon, lat))
        d = knoop_xyz @ v
        beste = int(np.argmax(d))
        km = R_AARDE * math.acos(max(-1.0, min(1.0, float(d[beste]))))
        namen.append(naam)
        landen.append(cty)
        locodes.append(code)
        ll.extend([round(lon, 3), round(lat, 3)])
        knoop.append(beste)
        afstand.append(round(km, 1))
    uit = {
        "aantal": len(namen),
        "namen": namen,
        "landen": landen,
        "locodes": locodes,
        "ll": ll,
        "knoop": knoop,
        "afstandKm": afstand,
        "bron": "searoute 1.6.0 ports.geojson",
    }
    pad = os.path.join(DATA, f"ports{suffix}.json")
    with open(pad, "w", encoding="utf-8") as f:
        json.dump(uit, f, ensure_ascii=False, separators=(",", ":"))
    ver = [a for a in afstand if a > 50]
    print(f"  havens        : {len(namen):,} -> {os.path.basename(pad)} ({os.path.getsize(pad) / 1024:,.0f} KB)"
          f" | snap-afstand mediaan {np.median(afstand):.0f} km, >50 km: {len(ver)}")
    # de LAR-486-acceptatiehavens expliciet rapporteren
    for wie in ("Amsterdam", "Nijmegen", "Rotterdam", "Duluth"):
        for i, naam in enumerate(namen):
            if naam == wie and landen[i] in ("Netherlands", "United_states"):
                print(f"    snap {naam:<10} ({landen[i][:2]}): knoop {knoop[i]} · {afstand[i]:.1f} km")
                break


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--analyse", action="store_true", help="alleen het rapport")
    ap.add_argument("--vaarwegen", help="GeoJSON uit fetch_waterways.py (M24/LAR-486): "
                                        "vaarweg-ketens aan de graaf hangen")
    ap.add_argument("--suffix", default="", help="achtervoegsel voor de uitvoerbestanden "
                                                 "(marnet<suffix>.bin/json, ports<suffix>.json) "
                                                 "— voor de bake-off-variant")
    args = ap.parse_args()
    if args.analyse:
        analyse()
    else:
        verzoen_en_bak(vaarwegen_pad=args.vaarwegen, suffix=args.suffix)
