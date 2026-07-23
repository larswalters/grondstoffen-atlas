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
import re
import sys

import numpy as np
from shapely import STRtree, box, points as shp_points
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

    def afstand_tot_open_water(self, lon, lat):
        """Kilometers tot de dichtstbijzijnde KUSTLIJN of MEEROEVER (LAR-518).

        Nodig omdat de havenlijst uit `searoute` een UN/LOCODE-locatielijst is en
        dus ook wegterminals, spoorterminals en grensovergangen bevat: Denver,
        Laramie en Alamogordo staan erin alsof het havens zijn. Die zijn niet met
        het oog te vinden (Lars: *"er zijn er zoveel dat 1 voor 1 controleren niet
        werkt"*), maar wel meetbaar: ze liggen honderden km van welk water dan ook.

        ⚠️ MEREN MOETEN MEEDOEN. Natural Earth's landvlakken hebben geen gaten
        voor meren, dus Chicago ligt 895 km van de "kust" terwijl het aan het
        Michiganmeer ligt. Zonder de merentoets gooit dit filter precies de
        Grote-Merenhavens weg — Duluth, Toledo, Milwaukee, Green Bay, Buffalo —
        en dat zijn er genoeg om de Seaway zinloos te maken.

        Rivieren zitten hier bewust NIET in: die afstand wordt apart gemeten als
        de rivier-snap, want dat is een afstand tot de ROUTEERGRAAF en niet tot
        een vlak. Wie wil weten of een haven aan water ligt, neemt de kleinste
        van de twee — en die keuze hoort bij de gebruiker, niet bij de meting.
        """
        p = Point(lon, lat)
        # lon-graden krimpen met de breedtegraad; de klem voorkomt een deling
        # door bijna-nul vlak bij de polen.
        naar_km = 111.0 * max(0.05, math.cos(math.radians(lat)))

        def rand_afstand(vlakken, boom):
            j = boom.nearest(p)
            g = vlakken[j]
            rand = g.exterior if g.geom_type == "Polygon" else g.boundary
            return rand.distance(p) * naar_km

        return min(rand_afstand(self.polys, self.tree),
                   rand_afstand(self.meren, self.meer_tree))


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
VERVOLG_MAX_KM = 5.0    # een vervolgsegment moet vlak op zijn voorganger aansluiten
CORRIDOR_EPS_KM = 0.25  # kwantisering (11 m) + simplify (25 m) blijven hier ruim onder


# ------------------------------------------------------ M24: gabariet (LAR-514)
#
# VIER MATEN PER EDGE — diepgang · breedte · lengte · doorvaarthoogte, in
# DECIMETER, waarbij 0 = ONBEKEND.
#
# Waarom vier maten en niet een klasse-enum of een tonnage (besluit van Lars,
# 2026-07-20): alleen vier maten vangen álle regimes. De Erie valt op HOOGTE
# (4,7 m), de Seaway op LENGTE/BREEDTE, de Poe Lock op LENGTE (366 m), Cape Cod
# op konvooivorm — géén daarvan ís een CEMT-klasse. CEMT blijft bestaan als
# AFGELEID label voor de HUD, zodat niemand vier maten hoeft te verzinnen voor
# de Rijn en niemand een klasse voor de Poe Lock.
#
# ⚠️ HET DRAAGPRINCIPE: bekende maat = harde grens, ONBEKENDE MAAT = GEEN GRENS.
# Een 0 sluit dus niets af. Dat is bewust: een verzonnen maat die te laag staat
# sluit stilzwijgend echte routes af, en dat effect is onvindbaar — je ziet
# alleen dat een route "niet bestaat". Vul daarom liever niets in dan iets dat
# niet uit een noembare bron komt.
#
# WAAROM DEZE TABEL IN DE BAKER STAAT EN NIET IN fetch_waterways.py:
# `cemt` staat wél bij SYSTEMEN, want de fetcher gebruikt die waarde zélf — de
# CEMT-clause selecteert er OSM-ways mee. De vier maten hebben geen enkele
# fetcher-rol: ze komen niet uit OSM maar uit gepubliceerde sluis-, brug- en
# vaargeulgegevens. Ze hier zetten houdt de koppeling eerlijk en scheelt een
# volledige re-fetch elke keer dat er een brughoogte wordt gecorrigeerd.

# CEMT-klasse -> (lengte m, breedte m).
# Bron: ECMT Resolution No. 92/2 (12 juni 1992), *New Classification of Inland
# Waterways* — de officiële tabel (https://www.itf-oecd.org/sites/default/files/
# docs/wat19922e.pdf). Leesregel: een vaarweg van klasse X laat schepen TÓT deze
# maten toe, dus we nemen de BOVENKANT van elk lengtebereik.
#
# ⚠️ ALLEEN LENGTE EN BREEDTE. Diepgang en doorvaarthoogte staan er bewust NIET
# in, en om precies dezelfde reden: de klasse bepaalt ze niet.
#
#   * HOOGTE — de CEMT-tabel geeft ALTERNATIEVEN ("5,25 of 7,00 of 9,10 m")
#     waaruit de waterwegbeheerder er één kiest.
#   * DIEPGANG — de diepgangkolom beschrijft het REFERENTIESCHIP van de klasse,
#     niet de vaarweg. Dat is geen interpretatie maar meetbaar: lengte en
#     breedte lopen monotoon op met de klasse (38,5->285 m en 5,05->34,2 m),
#     diepgang NIET — VIb staat op 4,50 m en VIc op 4,00 m. Een grootheid die
#     DAALT terwijl de klasse stijgt kan onmogelijk "de grens van de klasse"
#     zijn; een VIc-duwstel (2x3, breed en lang) is gewoon ondieper geladen.
#
# Dit is geen theoretisch punt. Met diepgang erin sloot `waal` (VIc -> 4,00 m)
# voor een klasse Va-schip (4,50 m) — de drukste binnenvaartweg van Europa dicht
# voor een gewoon Rijnschip, waardoor R'dam->Nijmegen van 172 km naar 9.405 km
# sprong (de router ging om via zee). Dezelfde foutsoort die dit project al kent
# als "vaargeul-projectdiepte is niet de maximale scheepsdiepgang", nu in de
# vorm "referentieschip is niet de vaarweg".
#
# Diepgang komt daarom ALLEEN uit een echte meting — GABARIET_PER_SYSTEEM.
CEMT_PRESETS = {
    "I":   (38.5,  5.05),   # péniche / Freycinet (250-400 t)
    "II":  (55.0,  6.6),    # Kempenaar (400-650 t)
    "III": (80.0,  8.2),    # Gustav Koenigs (650-1.000 t)
    "IV":  (85.0,  9.5),    # Johann Welker (1.000-1.500 t)
    "Va":  (110.0, 11.4),   # groot Rijnschip (1.600-3.000 t)
    "Vb":  (185.0, 11.4),   # duwstel 1x2 (3.200-6.000 t)
    "VIa": (110.0, 22.8),   # duwstel 2x1
    "VIb": (195.0, 22.8),   # duwstel 2x2 (6.400-12.000 t)
    "VIc": (280.0, 22.8),   # duwstel 2x3 (9.600-18.000 t)
    "VII": (285.0, 34.2),   # duwstel 3x3 (14.500-27.000 t)
}

# Systemen ZONDER CEMT-klasse: de maten per systeem, met bron per waarde.
# Buiten Europa bestaat de CEMT-tag niet, dus deze veertien (6x Mississippi-net,
# 5x China, yangon, amazone) dragen gepubliceerde nationale maten.
#
# Onderzocht 2026-07-20 met 14 parallelle onderzoekers + 28 skeptici (een
# algemene weerlegger en een "poort-jager" per systeem). Volledig rapport en
# alle bronregels: v2/design/gabarit-veld.md §4.
#
# ⚠️ WELKE GEVONDEN MAAT WEL EN NIET IN DE GRAAF KOMT — de scheidslijn die het
# onderzoek zelf als belangrijkste bevinding aanwees:
#
#   ✅ SLUISKOLK-MAAT als lengte/breedte. Een kolk van 600 ft neemt geen schip
#      van 600 ft (manoeuvreermarge), maar niets LANGER dan 182,88 m komt er
#      hoe dan ook doorheen. Als bovengrens is hij dus correct, hooguit iets te
#      ruim — en te ruim is de veilige kant.
#   ✅ GEPUBLICEERDE MAXIMALE SCHEEPSMAAT (diepgang of LOA) — precies wat het
#      veld bedoelt.
#   ✅ BRUGKLARING waar hard gemeten, mét bekend referentievlak.
#
#   ❌ VAARGEUL-PROJECTDIEPTE / 维护水深 NOOIT als maximale diepgang. Dit is de
#      val waar dit veld aan kapot zou gaan. Een onderhouden geuldiepte is een
#      GARANTIE, geen maximum: op de Mississippi is de projectdiepte 9 ft
#      terwijl de USCG in 2023 nog 10-10,5 ft toestond, dus werkelijke schepen
#      steken DIEPER dan het "maximum" dat we zouden invullen. Wie dat als
#      grens wegschrijft sluit echt bestaand verkeer af — stil, want je ziet
#      alleen dat een route niet bestaat. Zelfde foutsoort als de CEMT-
#      diepgangkolom hierboven: een getal dat de vaarweg beschrijft is geen
#      getal dat het schip begrenst.
#   ❌ ALLES ONDER VOORBEHOUD, en alles op een edge die eerst gesplitst of
#      vastgepind moet worden (zie de zes gevallen in §4 van de ontwerpnotitie).
#
# Gevolg: 7 van de 14 systemen krijgen maten, 7 blijven bewust leeg. Leeg is
# veilig — die sluiten niets af en wachten op het splits-/pinwerk.
#
# Waarden in METER; laat een sleutel WEG als er geen bron voor is.
GABARIET_PER_SYSTEEM = {
    # --- Verenigde Staten ---------------------------------------------------
    # New Orleans -> Baton Rouge, het diepstekende zeevaartvak.
    "mississippi": dict(
        # 45 ft. NOAA Coast Pilot 5 hfst. 8 (ed. 12-07-2026) + NOBRA-loodsbulletins
        # via LAMA. Hier vallen projectdiepte en toegestane scheepsdiepgang
        # toevallig samen, dus deze mág wel als scheepsmaat.
        diepgang=13.716,
        # hoogte NIET: de kabels bij Harahan geven 145 ft (44,2 m) op het
        # low-water-vlak maar ~128 ft (39,0 m) bij hoogwater, en voor
        # doorvaarthoogte is juist HOOGwater de harde kant. Twee datums door
        # elkaar leverde in het onderzoek niet alleen een fout getal maar de
        # verkeerde constructie op. Bindt sowieso geen enkel binnenvaartschip.
    ),
    # mississippi-boven (Baton Rouge -> Memphis): BEWUST LEEG. Enige gevonden
    # maat is de 9 ft projectdiepte, en dat is precies de waarde die je niet
    # als maximum mag lezen — zie de waarschuwing hierboven.
    #
    # mississippi-upper (Memphis -> Minneapolis): BEWUST LEEG. De kolken van
    # 56 x 400 ft (USAF/LSAF/LD 1) zijn echt, maar gelden alleen over de
    # laatste ~10 km van een keten van 1.728,7 km; alle andere kolken zijn
    # >= 500 ft. Over de hele edge gelegd sluiten ze vrijwel al het
    # Upper-Mississippi-verkeer af (een duwbak is al ~35 ft breed).
    # → eerst splitsen bij Lock & Dam 2 (Hastings), dat is aantoonbaar 600x110 ft.
    "illinois": dict(
        breedte=33.528,   # 110 ft kolk, alle zeven kolken bevestigd
        lengte=182.88,    # 600 ft kolk; USACE schut 1.200 ft-konvooien in twee keer
        hoogte=14.29,     # 46,9 ft, I-80 Bridge mile 286,9 (Brandon Road Pool)
        # Bron: USACE Rock Island, "Illinois Waterway Locks & Dams" (2018) +
        # USACE Division Bulletin No. II-2016. De hoogte is onafhankelijk
        # gereproduceerd uit de onderkant-staalelevaties van 44 bruggen (±0,1 ft).
        # diepgang NIET: 9 ft is projectdiepte.
    ),
    "chicago-kanaal": dict(
        lengte=182.88,    # 600 ft kolk; drie onafhankelijke bronnen, beide sluizen
        # breedte NIET: onopgelost bronconflict 80 ft (33 CFR 207.420) tegen
        # 50 ft (USACE Water Control Manual mei 2024). Die twee liggen aan
        # weerszijden van CEMT VIb (22,8 m), dus gokken beslist hier de uitkomst.
        # hoogte NIET: de knellende maat van deze edge, maar het enige getal dat
        # eruit komt (~4,9 m) is CONSTRUEERD — gepubliceerde klaring bij het
        # laagst toegestane pand minus de pandbandbreedte uit 33 CFR 207.420.
        # Zo'n getal staat nergens zo gepubliceerd. Zie de open verificaties.
    ),
    "ohio": dict(
        # 9 ft, en hier is het WEL een scheepsmaat: USACE HEC schrijft
        # "navigation by vessels drafting up to nine feet from the downstream
        # sill" — de geul zelf is 12 ft. Let op: dit sluit CEMT-klasse IV
        # (2,80 m) en alles daarboven af, en dat is fysiek juist.
        diepgang=2.7432,
        breedte=33.528,   # 110 ft, LPMS bevestigt WIDTH=CHMBUW=110 bij alle 21 kolken
        lengte=182.88,    # 600 ft bij Emsworth/Dashields/Montgomery (de rest 1.200 ft)
        # hoogte NIET: de Wheeling Suspension Bridge (1849) staat in de USACE
        # IENC op 17,1 m, maar Vertical_Datum is leeg voor alle 727 Ohio-bruggen
        # en de waarde is uit 2006. Een hoogte zonder referentievlak is geen maat.
    ),

    # --- China --------------------------------------------------------------
    # yangtze (Zhenjiang -> Nanjing): BEWUST LEEG. 12,5 m is projectdiepte,
    # 11,36 m staat onder voorbehoud (okt 2024, Nanjing verhoogt actief), en het
    # edge-eindpunt moet eerst hard op Xinshengwei/Longtan worden gepind — één
    # port area verder klapt het gabariet naar 10,5 m en 24 m.
    #
    # yangtze-boven (Nanjing -> Wuhan): BEWUST LEEG, en dat is jammer, want hier
    # zit de mooiste vondst van het onderzoek: de Nanjing Yangtze River Bridge
    # (1968) met 24 m klaring is het FYSIEKE mechanisme waardoor zeeschepen niet
    # boven Nanjing komen. Maar de waarde is conditioneel op waar de Wuhan-knoop
    # ligt: benedenstrooms van de 武汉长江大桥 (1957) is het 24 m, erop of
    # erboven 18 m. Node pinnen, niet gokken.
    "yangtze-chongqing": dict(
        # Kolkmaten van de Drieklovendam: "单个闸室有效尺寸为长280米、宽34米"
        # (CTG). Als bovengrens correct — niets langer dan 280 m of breder dan
        # 34 m passeert de sluis — al varen echte schepen er rond 130-150 m.
        lengte=280.0,
        breedte=34.0,
        # diepgang NIET: 3,5 m is 维护水深 (onderhouden geuldiepte) en geldt
        # bovendien alleen maart t/m juni. De 4,3 m schutdiepgang is een
        # maandelijks besluit van het 长江三峡通航管理局, geen vaste norm.
        # ⚠️ Verwar de sluis niet met de SCHEEPSLIFT ernaast (110,0 x 17,2 m,
        # 2,7 m diep): wie díe maten als trajectgrens invult sluit vrijwel de
        # hele vloot uit.
    ),
    # grand-canal-zuid: BEWUST LEEG — zwakste dossier van de veertien. Alle vier
    # de maten zijn ontwerpnorm of 代表船型 in plaats van gepubliceerd maximum,
    # en de enige harde bron is een Hangzhous verkeersbesluit dat nominaal op
    # 31-05-2026 verliep. Bovendien loopt de doorgaande route sinds 18-07-2023
    # via de 运河二通道-bypass, niet meer door de stadssectie.
    #
    # parelrivier: BEWUST LEEG. 13,0 m is 维护底标高 (geuldiepte), en de harde
    # brugklaring van 60,0 m hangt volledig aan het eindpunt: voorbij het
    # 西基调头区 wordt het 55 m en zakt de diepte naar 9 en dan 8 m.
    #
    # xijiang: BEWUST LEEG tot de edge bij Sixianjiao is gesplitst. Eén gabariet
    # kan geen factor anderhalf in doorvaarthoogte dragen: 7,6 m in de delta
    # (旧五斗大桥, en die heet "旧" = oud, staat mogelijk niet meer) tegen 11,5 m
    # op de Xijiang zelf.

    # --- Rest ---------------------------------------------------------------
    "yangon": dict(
        # Myanma Port Authority, "Yangon Ports" (2024): "the acceptable vessel
        # size is vessels with Draft 9.6 m, LOA 200 m" — expliciet de Inner
        # Harbour, niet Thilawa (10,5 m). Tijgebonden: de Inner Bar bij Monkey
        # Point is ~4,5 m CD en haalt met springtij 9,63 m — vrijwel nul marge.
        diepgang=9.6,
        lengte=200.0,
        # hoogte NIET: de 44 m van de Yangon-Dala-brug komt uit een
        # bekendmaking van sept 2025 die aan de bouwvoortgang hing; de brug
        # opende 06-02-2026 en een bevestiging van ná die datum ontbreekt.
    ),
    "amazone": dict(
        # Marinha do Brasil / CFAOC, NPCF Anexo 1-G (REMAN) tabel 3.1:
        # "CALADO MAX. RECOMENDADO: 11,5 m", beperkt door de Passagem do
        # Tabocal; identiek in Anexo 1-D en 1-E. Absolute bovengrens, GEEN
        # jaarrondgarantie — in de droogte van 2024 zakte het vak
        # Manaus-Itacoatiara naar ~8,5 m.
        diepgang=11.5,
        # lengte/breedte NIET: 305 x 43,5 m is een terminal-autorisatie
        # (Chibatao) die afhangt van de inzet van twee azimutale sleepboten,
        # geen eigenschap van de vaarweg.
    ),
}


def gabariet_voor(label, cemt):
    """Geeft (diepgang, breedte, lengte, hoogte) in DECIMETER; 0 = onbekend.

    Volgorde van herkomst:
      1. een expliciete waarde in GABARIET_PER_SYSTEEM (gemeten/gepubliceerd),
      2. anders de CEMT-preset voor dit systeem (afgeleid),
      3. anders onbekend.
    Een expliciete waarde wint dus altijd van de preset — de preset is een
    generieke klassevertaling, de expliciete waarde is dít traject.
    """
    maten = dict(GABARIET_PER_SYSTEEM.get(label, {}))
    if cemt:
        preset = CEMT_PRESETS.get(cemt)
        if preset is None:
            raise RuntimeError(
                f"{label}: onbekende CEMT-klasse {cemt!r} — vul CEMT_PRESETS aan "
                f"of corrigeer de klasse in fetch_waterways.py:SYSTEMEN")
        lengte, breedte = preset
        maten.setdefault("lengte", lengte)
        maten.setdefault("breedte", breedte)
        # diepgang en hoogte NIET: die volgen niet uit de klasse — zie de
        # waarschuwing bij CEMT_PRESETS. Ze komen alleen uit een echte meting.
    return tuple(
        int(round(maten.get(k, 0) * 10)) for k in ("diepgang", "breedte", "lengte", "hoogte")
    )


def hecht_aan_keten(label, volgt_op, punt, nodes, edge_lijst, status, geometrie, uit):
    """Geeft een knoop op de dichtstbijzijnde plek van een al gebakken keten.

    Een riviernet is geen lijn: de Main mondt 30 km ín `rijn-boven` uit, de
    Nieuwe Merwede takt middenin de Beneden-Merwede af, de Ohio bij Cairo
    middenin de Mississippi. Aanhaken kon eerst alleen op het ketenUITEINDE
    (LAR-487/488); sinds LAR-504 mag het overal.

    Knipt ALTIJD op een BESTAANDE geometrie-vertex, nooit op een geïnterpoleerd
    punt. Daardoor verschuift er geen enkele coördinaat, en blijft de
    corridor-toets die de moederketen al doorstond per constructie geldig — de
    knip voegt een knoop toe, geen geometrie.
    """
    if volgt_op not in uit:
        raise RuntimeError(f"{label}: volgtOp={volgt_op} is nog niet gebakken — "
                           f"zet dat systeem eerder in SYSTEMEN")
    beste_d, beste_ei, beste_vi = 1e18, -1, -1
    for ei in uit[volgt_op]["edges"]:
        for vi, p in enumerate(geometrie[ei]):
            d = gc_km(p, punt)
            if d < beste_d:
                beste_d, beste_ei, beste_vi = d, ei, vi
    if beste_d > VERVOLG_MAX_KM:
        raise RuntimeError(f"{label}: begint {beste_d:.1f} km van keten {volgt_op} "
                           f"(max {VERVOLG_MAX_KM}) — controleer anker_zee")

    (a, b), passage = edge_lijst[beste_ei]
    pts = geometrie[beste_ei]
    if beste_vi == 0:
        return a, beste_d, False
    if beste_vi == len(pts) - 1:
        return b, beste_d, False

    # middenin een edge: knip 'm op deze vertex in tweeën. De eerste helft
    # hergebruikt de edge-index (a -> nieuw), de tweede wordt aangehangen
    # (nieuw -> b) met hetzelfde passage-label en dezelfde soort, zodat de
    # `vermijd`-knop van de moederketen over beide helften blijft gelden.
    nodes.append((round(pts[beste_vi][0], 6), round(pts[beste_vi][1], 6)))
    nieuw = len(nodes) - 1
    edge_lijst[beste_ei] = ((a, nieuw), passage)
    geometrie[beste_ei] = pts[:beste_vi + 1]
    ej = len(edge_lijst)
    edge_lijst.append(((nieuw, b), passage))
    status[ej] = status.get(beste_ei, "")
    geometrie[ej] = pts[beste_vi:]
    uit[volgt_op]["edges"].append(ej)
    return nieuw, beste_d, True


def extra_vaarwegen(land, nodes, edge_lijst, status, geometrie, pad):
    """Hangt vaarweg-ketens uit fetch_waterways.py aan de graaf (in-place).

    Per systeem: zeezijde hechten aan de dichtstbijzijnde ORIGINELE
    MARNET-knoop, dan nieuwe knopen elke ~KETEN_KM met edges soort=1 en
    passage=systeemlabel (het bestaande vermijd-mechanisme = meteen de
    M26/M21-filterknop). Geeft de meta per systeem terug voor marnet.json.

    Een systeem met `volgtOp` hangt niet aan MARNET maar aan het BINNENEINDE
    van dat eerdere systeem (LAR-487/488). Zo krijgt één rivier meerdere
    labels met elk een eigen zeevaart-vlag: de Mississippi is zeevaarbaar tot
    Baton Rouge en daarboven binnenvaart, de Yangtze tot Nanjing. Volgorde in
    fetch_waterways.SYSTEMEN bepaalt de bakvolgorde; een vooruitverwijzing
    faalt luid.
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

        volgt_op = props.get("volgtOp") or ""
        if volgt_op:
            # vervolgsegment of ZIJTAK: aansluiten op de dichtstbijzijnde plek
            # van de voorganger (LAR-504). Geen polygoon-toets — dat punt ligt
            # al op een corridor-getoetste keten, niet op de zee-overgang.
            zeeknoop, aansluit_km, geknipt = hecht_aan_keten(
                label, volgt_op, coords[0], nodes, edge_lijst, status, geometrie, uit)
            overgang = f"{'aftakking' if geknipt else 'keten'}:{volgt_op}"
        else:
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

        # RINGSLUITING (LAR-505): een verbindingskanaal hangt aan BEIDE kanten
        # aan een bestaande keten. `volgtOp` hecht het begin; `sluitAan` hecht
        # het eind. Zonder dit is zo'n kanaal een doodlopende tak waar nooit een
        # route overheen kan — het Amsterdam-Rijnkanaal veranderde niets aan
        # Amsterdam->Nijmegen tot deze hechting erbij kwam.
        # Bewust ná de corridor-toets: het sluitstukje is een verbinding tussen
        # twee ketens, geen gebakken bron-geometrie, en hoort dus net zomin bij
        # die toets als het aansluitstukje aan de zeezijde.
        sluit_aan = props.get("sluitAan") or ""
        sluit_km = None
        if sluit_aan:
            eindknoop, sluit_km, _geknipt = hecht_aan_keten(
                f"{label} (sluiting)", sluit_aan, coords[-1],
                nodes, edge_lijst, status, geometrie, uit)
            if eindknoop != vorige_knoop:
                ei = len(edge_lijst)
                edge_lijst.append(((vorige_knoop, eindknoop), label))
                status[ei] = "binnen:" + label
                geometrie[ei] = [nodes[vorige_knoop], nodes[eindknoop]]
                keten_edges.append(ei)

        km_tot = sum(gc_km(a, b) for a, b in zip(lijn, lijn[1:]))
        # Dezelfde vier maten die per edge de bin in gaan, ook per label in de
        # meta — puur zodat de HUD ze kan tónen (en zodat ze inspecteerbaar zijn
        # zonder de bin te decoderen). De ROUTER leest ze niet hier maar per
        # edge, want een poort zit niet altijd op het hele systeem.
        gab_dm = gabariet_voor(label, props.get("cemt", ""))
        uit[label] = {
            "zeevaart": bool(props.get("zeevaart")),
            "cemt": props.get("cemt", ""),
            "gabariet": {
                k: (v / 10 if v else None)
                for k, v in zip(("diepgang", "breedte", "lengte", "hoogte"), gab_dm)
            },
            "bron": props.get("bron", ""),
            "km": round(km_tot, 1),
            "edges": keten_edges,
            "aansluitKnoop": zeeknoop,
            "aansluitKm": round(aansluit_km, 2),
            "aansluitOvergang": overgang,
            "volgtOp": volgt_op,
            "sluitAan": sluit_aan,
            "sluitKm": None if sluit_km is None else round(sluit_km, 2),
        }
        sluit_tekst = "" if sluit_km is None else f" · sluit op {sluit_aan} ({sluit_km:.2f} km)"
        print(f"  {label:<16} {km_tot:6.1f} km · {len(keten_edges)} edges · aansluiting "
              f"knoop {zeeknoop} ({aansluit_km:.2f} km, {overgang}) · corridor max "
              f"{ergste * 1000:.0f} m · zeevaart={bool(props.get('zeevaart'))}{sluit_tekst}")
    return uit


# ---------------------------------------------------------------- bulklaag (LAR-515)
#
# De bulklaag is PUUR TEKENGEOMETRIE — geen onderdeel van `nodes`/`edge_lijst`.
# Reden (gevonden bij de risicoanalyse van 2026-07-20, gemeten op NL): een
# eerste ontwerp stitchte de bulklaag tot een junction-graaf zoals de
# verhalende ketens, maar dat gaf op NL alleen al 23.189 knopen/edges — MEER
# dan het hele huidige netwerk (10.773/17.024) — want bulkketens zijn extreem
# kort (mediaan 52 m). Zonder topologie bestaat dat risico niet: deze functies
# MUTEREN nodes/edge_lijst/status NOOIT. marnet.bin/marnet.json/ports.json
# blijven daardoor byte-identiek, ook met --bulk. Het resultaat gaat naar een
# apart bestand (marnet-bulk.json) dat de browser los inleest.

BULK_EPS_KM = 0.25   # uitsluiting: bulk binnen 250 m van de verhalende laag vervalt
BULK_MIN_KM = 1.0    # een overgebleven snipper korter dan dit is geen vaarweg meer
BULK_DICHT_KM = 0.2  # verdichtingsstap vóór de STRtree-toets — ZIE snij_bulk()


def _seg_km(p, a, b):
    """Afstand van p tot het SEGMENT a-b in km (met klemming op de uiteinden).

    ⚠️ `_kruis_km()` hierboven meet tot de ONEINDIGE lijn en is hier
    onbruikbaar — die zou willekeurige geometrie wegvagen die toevallig op
    het verlengde van een kort Rijn-segment ligt.
    """
    coslat = math.cos(math.radians(p[1]))
    ax, ay = (a[0] - p[0]) * coslat, a[1] - p[1]
    bx, by = (b[0] - p[0]) * coslat, b[1] - p[1]
    dx, dy = bx - ax, by - ay
    den = dx * dx + dy * dy
    if den < 1e-18:
        return math.hypot(ax, ay) * 111.2
    t = max(0.0, min(1.0, -(ax * dx + ay * dy) / den))
    return math.hypot(ax + t * dx, ay + t * dy) * 111.2


def _lengte_km(pts):
    return sum(gc_km(pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def _verdicht_voor_toets(pts, stap_km=BULK_DICHT_KM):
    """Voegt tussenpunten in zodat geen twee opeenvolgende punten verder dan
    stap_km uit elkaar liggen — puur voor de exclusietoets, niet voor de
    uitvoergeometrie.

    Waarom dit moet: `snij_bulk` toetst per PUNT. Gemeten op NL-bulk na DP
    25 m: mediane vertexafstand 229 m, p99 3.144 m, max 44 km — 84% van de
    kilometers zit in segmenten LANGER dan de 250 m-uitsluitingsstraal zelf.
    Zonder verdichting mist de toets dus grotendeels de dubbele geometrie die
    hij hoort te vinden. Na verdichting op 200 m is elk gat kleiner dan de
    straal en werkt de puntsgewijze toets wél.
    """
    uit = [pts[0]]
    for i in range(1, len(pts)):
        a, b = pts[i - 1], pts[i]
        d = gc_km(a, b)
        if d > stap_km:
            n = int(d / stap_km) + 1
            for k in range(1, n):
                t = k / n
                uit.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
        uit.append(b)
    return uit


def _verhalende_lijnen(nodes, edge_lijst, status, geometrie, uit):
    """Alle polylines waar de bulklaag niet naast mag liggen: de 36 M24-ketens
    (volle DP-resolutie) plus de M23-edges met status `binnen:<zone>` (Suez,
    Panama, Mississippi, Seaway, Wolga-Don, ... — 29 zones).

    ⚠️ De M23-zone-edges hebben GEEN eigen geometrie-entry (die bestaat alleen
    voor omgelegde `kapot`-edges en voor vaarweg-ketens) en vallen dus terug op
    de KOORDE (MARNET-mediaan 83 km, max 3.611 km). De 250 m-band daarrond is
    voor zo'n lange koorde een dunne sliver: de bulk-kopie van bijvoorbeeld het
    Suezkanaal wordt daardoor NIET weggenomen en kan als dubbele lijn
    verschijnen. Bewust geaccepteerd — uitsluiten tegen álle MARNET-zee-edges
    zou willekeurige estuarium- en kustgeometrie wegvreten. Gerapporteerd,
    niet verstopt: zie het `sliver`-aantal in het bakrapport.
    """
    wie = {ei for v in uit.values() for ei in v["edges"]}
    wie |= {ei for ei, s in status.items() if s.startswith("binnen:")}
    lijnen, slivers = [], 0
    for ei in sorted(wie):
        (a, b), _p = edge_lijst[ei]
        lijn = geometrie.get(ei) or [nodes[a], nodes[b]]
        if ei not in geometrie:
            slivers += 1
        lijnen.append(lijn)
    return lijnen, slivers


def snij_bulk(bulk_lijnen, boom, seg_pts, eps_km=BULK_EPS_KM, min_km=BULK_MIN_KM):
    """Knipt uit elke (verdichte) bulk-polyline weg wat < eps_km van de
    verhalende laag ligt. Geeft (runs, rapport) — een run is een aaneen-
    gesloten stuk dat OVERBLIJFT: een zijrivier die de laatste 300 m in de
    Rijn ligt verliest zijn kop, niet zijn hele lichaam.

    Precedent voor de aanpak (grof via STRtree, dan exact nagerekend):
    `middellijn_uit_vlakken.py` liep eerst 5,5 GB en 11+ min met `union_all`
    terwijl van 289.365 vlakken er 1.241 relevant waren. `STRtree.query(...,
    predicate="dwithin")` is gevectoriseerd in C en toetst alleen kandidaten.
    """
    offsets, alle = [], []
    for lijn in bulk_lijnen:
        offsets.append(len(alle))
        alle.extend(lijn)
    offsets.append(len(alle))
    arr = np.array(alle, dtype=float)
    dicht = np.zeros(len(arr), dtype=bool)
    beste = np.full(len(arr), np.inf)
    pts = shp_points(arr)
    paren = 0

    band = 5.0
    for band0 in np.arange(-90.0, 90.0, band):
        wie = np.flatnonzero((arr[:, 1] >= band0) & (arr[:, 1] < band0 + band))
        if not len(wie):
            continue
        cos_min = max(0.1, math.cos(math.radians(max(abs(band0), abs(band0 + band)))))
        eps_deg = 1.5 * eps_km / 111.2 / cos_min
        pi, si = boom.query(pts[wie], predicate="dwithin", distance=eps_deg)
        paren += len(pi)
        for lokaal, s in zip(pi, si):
            i = int(wie[lokaal])
            d = _seg_km(alle[i], *seg_pts[s])
            if d < beste[i]:
                beste[i] = d
            if d <= eps_km:
                dicht[i] = True

    # ⚠️ ALLEEN DE KOP EN DE STAART MOGEN WEG, NOOIT EEN GAT IN HET MIDDEN.
    #
    # Dat is exact wat de docstring hierboven al belooft — *"een zijrivier die
    # de laatste 300 m in de Rijn ligt verliest zijn kop, niet zijn hele
    # lichaam"* — maar de lus knipte een lijn óók doormidden zodra hij ergens
    # halverwege binnen eps langs de verhalende laag schampte. Gemeten op de
    # Yangtze (2026-07-23): de OSM-rivier Zhenjiang→monding (ways 27303391 +
    # 27303398, samen 195,7 km) verloor vijf stukken van 2,1 · 2,1 · 2,2 · 4,6
    # en 5,9 km — precies dáár waar de M23-`yangtze`-zone van MARNET ernaast
    # ligt. De rivier bleef als lijn zichtbaar maar viel in de graaf uit elkaar,
    # en omdat de MARNET-tegenhanger knoop-ids ónder `zeeKnopen` heeft (groep
    # ZEE) kon geen binnenvaartbeen er nog overheen. Gevolg: Shanghai→Tongling
    # week uit naar het Grote Kanaal tot 32,84°N — 616 km met een lus over land.
    #
    # Een gat in het midden is dus geen dubbele geometrie meer, maar een BREUK.
    # Kop en staart afnemen kan geen enkele verbinding verbreken (er hangt per
    # definitie niets meer achter); een gat in het midden doet dat altijd.
    # Daarom houden we interne `dicht`-vertices gewoon staan: de lijn blijft één
    # stuk, met zijn eigen brongeometrie, en er wordt niets bijverzonnen — het
    # is dezelfde way die er in OSM ook doorloopt.
    runs, snippers, hersteld, hersteld_km = [], 0, 0, 0.0
    for li in range(len(bulk_lijnen)):
        i0, i1 = offsets[li], offsets[li + 1]
        kop = i0
        while kop < i1 and dicht[kop]:
            kop += 1
        staart = i1
        while staart > kop and dicht[staart - 1]:
            staart -= 1
        # tellen wat we tegenhouden: elk aaneengesloten `dicht`-blok BINNEN de
        # lijn is een gat dat de oude lus geknipt zou hebben
        i = kop
        had_gat = False
        while i < staart:
            if dicht[i]:
                j = i
                while j < staart and dicht[j]:
                    j += 1
                hersteld_km += _lengte_km(alle[max(kop, i - 1):min(staart, j + 1)])
                had_gat = True
                i = j
            else:
                i += 1
        if had_gat:
            hersteld += 1
        if staart - kop > 1:
            runs.append((li, alle[kop:staart]))
    houd = []
    for li, p in runs:
        if _lengte_km(p) >= min_km:
            houd.append((li, p))
        else:
            snippers += 1

    bewaard = ~dicht
    dichtbij_bewaard = beste[bewaard & np.isfinite(beste)]
    rapport = {
        "vertices": int(len(arr)), "vertices_weg": int(dicht.sum()), "paren": paren,
        "max_weg_m": float(beste[dicht].max() * 1000) if dicht.any() else 0.0,
        "dichtste_bewaard_m": (float(dichtbij_bewaard.min() * 1000)
                               if len(dichtbij_bewaard) else float("inf")),
        "snippers": snippers, "runs": len(houd),
        # wat de kop/staart-regel heeft tegengehouden: lijnen die vroeger
        # doormidden werden geknipt, en hoeveel km binnenwater dat scheelt
        "hersteld": hersteld, "hersteld_km": round(hersteld_km, 1),
    }
    return houd, rapport


# ---------------------------------------------------------- binnenwaternet
#
# ÉÉN binnenwaternet, geen tweede laag ernaast (besluit Lars 2026-07-20:
# *"het rivierennet en binnenwater moet gewoon gemapt worden en bij die lijnen
# kun je toch zetten wat de doorvaartdiepte en breedte en evt hoogte is"*).
#
# ⚠️ HET NET HOEFT NIET AAN MARNET TE HANGEN, en dat is geen tekortkoming maar
# het ontwerp. Van rivier naar zee gaat in werkelijkheid via een OVERSLAGHAVEN
# — drie schepen, niet één. Losse uiteinden zijn dus de verwachte toestand tot
# de havens erop worden aangesloten.
#
# Dat lost bovendien gratis een oud probleem op: de `zeevaart`-vlag en het
# groepslabel `binnenvaart` bestaan alleen om te voorkomen dat een zeeschip
# door sluizen vaart (de Donau-ring: R'dam->Shanghai 18.627 i.p.v. 19.610 km).
# Zijn zee en rivier LOSSE COMPONENTEN, dan kan dat per constructie niet meer —
# er is geen edge waarover een zeeschip het binnenwater op komt.
#
# KNOPEN EN GEOMETRIE ZIJN LOS VAN ELKAAR. Een knoop is een plek om aan te
# takken of aan te haken, geen hoekpunt: tussen twee knopen ligt de VOLLEDIGE
# lijn met alle meanders, en `edgeKm` is de echte vaarafstand. Vandaar dat de
# Donau met knopen op 15 km toch elke stad binnen ±4 km van haar officiële
# rivierkilometer haalt. Een haven wordt straks met `hecht_aan_keten()`
# aangehaakt, en die knipt de edge open op een BESTAANDE vertex — dus de
# knoopafstand begrenst de nauwkeurigheid van een haven niet.

BULK_KNOOP_KM = 10.0    # tussenknoop op lange stukken (topologie zit op de kruisingen)
BULK_QUANT = 1e-5       # ~1 m: twee vertices hierbinnen zijn hetzelfde punt


def _gabariet_uit_signaal(sig):
    """Vertaalt het OSM-bevaarbaarheidssignaal naar maten in METER.

    Alleen wat ondubbelzinnig is. `CEMT:none`, `CEMT:Ia`, `CEMT:V` (Va of Vb?),
    `CEMT:(Vb)` (haakjes = niet officieel) en `CEMT:III;I` worden bewust NIET
    vertaald — bij elkaar een paar tientallen lijnen, en gokken kost meer dan
    het oplevert. Onbekend = geen grens, dus leeg laten is veilig.
    """
    if not sig:
        return {}
    if sig.startswith("CEMT:"):
        klasse = sig[5:].strip()
        preset = CEMT_PRESETS.get(klasse)
        if preset is None:
            return {}
        lengte, breedte = preset
        return {"lengte": lengte, "breedte": breedte}
    if sig.startswith("draft:"):
        # OSM `draft` op een vaarweg = max diepgang van schepen die er kunnen
        # varen. Dat is precies de scheepsmaat die we zoeken (anders dan een
        # vaargeul-projectdiepte, die een garantie is en geen maximum).
        ruw = sig[6:].strip()
        m = re.match(r"^(\d+)'\s*(\d+)\"?$", ruw)          # 13'6"
        if m:
            return {"diepgang": int(m.group(1)) * 0.3048 + int(m.group(2)) * 0.0254}
        try:
            v = float(ruw)
            return {"diepgang": v} if 0 < v < 30 else {}
        except ValueError:
            return {}
    return {}                    # boat / ship / motorboat / usage: geen maat


def _pt_seg_deg(p, a, b):
    """Punt-tot-segment-afstand in het platte lon/lat-vlak (graden). Alleen om
    het juiste segment te kiezen bij het invoegen — geen km-maat."""
    px, py = p
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))


def _voeg_in(pts, npc):
    """Voeg projectiepunt npc in op het dichtstbijzijnde segment van pts, tenzij
    het vrijwel op een bestaande vertex valt (dan verandert er niets)."""
    beste_j, beste_d = 0, 1e18
    for j in range(len(pts) - 1):
        d = _pt_seg_deg(npc, pts[j], pts[j + 1])
        if d < beste_d:
            beste_d, beste_j = d, j
    if gc_km(npc, pts[beste_j]) < 1e-3 or gc_km(npc, pts[beste_j + 1]) < 1e-3:
        return pts                       # valt samen met een uiteinde → geen insert
    return pts[:beste_j + 1] + [npc] + pts[beste_j + 1:]


def _heal_riviernet(lijnen_per_regio, eps_km):
    """Tier-1 confluentie-heal (LAR-520). Een lijn-UITEINDE dat binnen eps_km OP
    de lijn van een ANDER component projecteert wordt daar aangehecht: het
    projectiepunt komt als vertex in de doel-lijn en het uiteinde verschuift
    ernaartoe. `binnenwaternet()` maakt er vanzelf één gedeelde knoop van.

    CROSS-COMPONENT is de kern: binnen je eigen component hechten doet niets én
    is precies waar de meander-sluipweg (valkuil 1) zou ontstaan — dat kan hier
    per constructie niet. Het uiteinde landt bovendien OP echte vaarweggeometrie,
    dus de naad loopt over water (valkuil: geen hemelsbrede sprong). Greedy op de
    kleinste gaten, progressieve union zodat een paar niet twee keer hecht. De
    lengtetoets per corridor blijft de eindcontrole (valkuil 3).

    Muteert lijnen_per_regio in-place. Geeft (n_naden, langste_km, alle_km).
    """
    comp, idx = _lijn_componenten(lijnen_per_regio)
    lines = [lijnen_per_regio[r][l][1] for r, l in idx]
    geoms = [LineString(p) for p in lines]
    boom = STRtree(geoms)
    venster = (eps_km / 111.32) * 1.6      # ruime bbox-marge (lon krapper dan lat)

    kand = []
    for gi, pts in enumerate(lines):
        for eind in (0, -1):
            E = pts[eind]
            bx = box(E[0] - venster, E[1] - venster, E[0] + venster, E[1] + venster)
            beste = None
            for cand in boom.query(bx):
                if cand == gi or comp[cand] == comp[gi]:
                    continue
                ln = geoms[cand]
                npnt = ln.interpolate(ln.project(Point(E)))
                d = gc_km(E, (npnt.x, npnt.y))
                if d <= eps_km and (beste is None or d < beste[0]):
                    beste = (d, cand, (npnt.x, npnt.y))
            if beste:
                kand.append((beste[0], gi, eind, beste[1], beste[2]))
    kand.sort()

    cmap = list(comp)

    def find2(x):
        while cmap[x] != x:
            cmap[x] = cmap[cmap[x]]
            x = cmap[x]
        return x

    used, naden = set(), []
    for d, gi, eind, cand, npc in kand:
        if (gi, eind) in used or find2(gi) == find2(cand):
            continue
        regio, li = idx[gi]
        sig, pts = lijnen_per_regio[regio][li]
        pts = list(pts)
        pts[eind] = npc                      # uiteinde op de doel-lijn
        lijnen_per_regio[regio][li] = (sig, pts)
        cregio, cli = idx[cand]              # projectiepunt als vertex in de doel-lijn
        csig, cpts = lijnen_per_regio[cregio][cli]
        lijnen_per_regio[cregio][cli] = (csig, _voeg_in(cpts, npc))
        used.add((gi, eind))
        cmap[find2(gi)] = find2(cand)
        naden.append(d)

    return len(naden), (max(naden) if naden else 0.0), naden


def _richting(pts, eind, langs_km=1.0):
    """Eenheidsvector die UIT het uiteinde wijst (van binnen naar buiten),
    gemeten over ~langs_km langs de lijn — stabieler dan het laatste segment."""
    seq = pts if eind == 0 else pts[::-1]
    p0 = seq[0]
    pk = seq[-1]
    acc = 0.0
    for i in range(1, len(seq)):
        acc += gc_km(seq[i - 1], seq[i])
        if acc >= langs_km:
            pk = seq[i]
            break
    vx, vy = p0[0] - pk[0], p0[1] - pk[1]
    n = math.hypot(vx, vy) or 1.0
    return (vx / n, vy / n)


def _lijn_componenten(lijnen_per_regio):
    """Union-find over de lijnen: verbonden als een endpoint-cel van de één
    samenvalt met een vertex-cel van de ander — zoals binnenwaternet() knoopt.
    Geeft (root-per-lijn, idx-lijst)."""
    q = lambda p: (round(p[0] / BULK_QUANT), round(p[1] / BULK_QUANT))
    idx, endcells, vcell = [], [], {}
    for regio in sorted(lijnen_per_regio):
        for li, (_sig, pts) in enumerate(lijnen_per_regio[regio]):
            gi = len(idx)
            idx.append((regio, li))
            endcells.append((q(pts[0]), q(pts[-1])))
            for p in pts:
                vcell.setdefault(q(p), []).append(gi)
    par = list(range(len(idx)))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for gi, cells in enumerate(endcells):
        for c in cells:
            for gj in vcell.get(c, ()):
                if gj != gi:
                    ra, rb = find(gi), find(gj)
                    if ra != rb:
                        par[rb] = ra
    return [find(i) for i in range(len(idx))], idx


def _heal_corridors(lijnen_per_regio, eps_km, hoek_max=45.0):
    """Tier-2 corridor-heal (LAR-520). Verbindt twee UITEINDEN van VERSCHILLENDE
    componenten binnen eps_km, maar alléén als ze in elkaars verlengde liggen:
    de naadrichting valt binnen hoek_max° van beide uiteinde-richtingen. Dat
    sluit de meander-sluipweg (valkuil 1: hairpin-uiteinden lopen parallel, niet
    naar elkaar toe) en de dode voorganger (valkuil 3: naad staat dwars op de
    richting) uit — zónder handmatige ijkpunten. Cross-component afgedwongen
    (geen intra-component kortsluiting), greedy op de kleinste gaten.
    """
    comp, idx = _lijn_componenten(lijnen_per_regio)
    lines = [lijnen_per_regio[r][l][1] for r, l in idx]
    geoms = [LineString(p) for p in lines]
    boom = STRtree(geoms)
    venster = (eps_km / 111.32) * 1.6

    def hoek(u, v):
        d = max(-1.0, min(1.0, u[0] * v[0] + u[1] * v[1]))
        return math.degrees(math.acos(d))

    kand = []
    for gi, pts in enumerate(lines):
        for e in (0, -1):
            E = pts[e]
            d1 = _richting(pts, e)
            bx = box(E[0] - venster, E[1] - venster, E[0] + venster, E[1] + venster)
            for gj in boom.query(bx):
                if gj == gi or comp[gj] == comp[gi]:
                    continue
                pj = lines[gj]
                for e2 in (0, -1):
                    F = pj[e2]
                    g = gc_km(E, F)
                    if g > eps_km or g < 1e-6:
                        continue
                    dx, dy = F[0] - E[0], F[1] - E[1]
                    ns = math.hypot(dx, dy) or 1.0
                    s = (dx / ns, dy / ns)
                    d2 = _richting(pj, e2)
                    if hoek(s, d1) <= hoek_max and hoek((-s[0], -s[1]), d2) <= hoek_max:
                        kand.append((g, gi, e, gj, e2, F))
    kand.sort()

    cmap = list(comp)

    def find2(x):
        while cmap[x] != x:
            cmap[x] = cmap[cmap[x]]
            x = cmap[x]
        return x

    used, naden = set(), []
    for g, gi, e, gj, e2, F in kand:
        if (gi, e) in used or (gj, e2) in used or find2(gi) == find2(gj):
            continue
        regio, li = idx[gi]
        sig, pts = lijnen_per_regio[regio][li]
        pts = list(pts)
        pts[e] = F                          # snap dit uiteinde op het andere
        lijnen_per_regio[regio][li] = (sig, pts)
        used.add((gi, e))
        used.add((gj, e2))
        cmap[find2(gi)] = find2(gj)
        naden.append(g)
    return len(naden), (max(naden) if naden else 0.0), naden


def binnenwaternet(nodes, edge_lijst, status, geometrie, vaarwegen_meta,
                   lijnen_per_regio, edge_gabariet, heal_km=0.0, corridor_km=0.0):
    """Hangt het gemapte binnenwater als ECHTE knopen en edges in de graaf.

    Muteert `nodes`/`edge_lijst`/`status`/`geometrie` — anders dan de oude
    bulklaag, die bewust buiten de graaf bleef. Geeft per regio een meta-blok
    terug voor `meta.vaarwegen`.

    Knoopplaatsing: op elk punt waar lijnen elkaar raken (dáár zit de
    topologie) plus een tussenknoop elke BULK_KNOOP_KM op lange stukken. De
    geometrie tussen twee knopen blijft volledig bewaard.

    heal_km > 0 draait eerst de tier-1 confluentie-heal (LAR-520): gemiste
    confluenties waar een uiteinde binnen heal_km OP een andere lijn valt worden
    aangehecht, over water per constructie. Zonder heal (=0) blijft het gedrag
    exact als vóór LAR-520.
    """
    # Itereren tot convergentie: greedy hecht aan het DICHTSTBIJZIJNDE andere
    # component, waardoor een hoofdstroom in de eerste ronde in losse stukken kan
    # mergen die pas een ronde later aan elkaar komen (Cairo-confluentie,
    # Mississippi-delta, Waal-tak). Elke ronde ziet verse componenten; stoppen
    # zodra een ronde niets meer toevoegt. Dezelfde guards, herhaald.
    MAX_RONDES = 6
    if heal_km > 0 or corridor_km > 0:
        tot1 = tot2 = 0
        langste1 = langste2 = 0.0
        for ronde in range(MAX_RONDES):
            n1 = n2 = 0
            if heal_km > 0:
                n1, l1, _ = _heal_riviernet(lijnen_per_regio, heal_km)
                tot1 += n1
                langste1 = max(langste1, l1)
            if corridor_km > 0:
                n2, l2, _ = _heal_corridors(lijnen_per_regio, corridor_km)
                tot2 += n2
                langste2 = max(langste2, l2)
            if n1 + n2 == 0:
                break
        print(f"  heal geconvergeerd in ≤{ronde + 1} rondes:")
        if heal_km > 0:
            print(f"    tier-1 confluentie (≤{heal_km:.2f} km, cross-component): "
                  f"{tot1:,} naden · langste {langste1 * 1000:.0f} m")
        if corridor_km > 0:
            print(f"    tier-2 corridor (≤{corridor_km:.1f} km, collineair): "
                  f"{tot2:,} naden · langste {langste2:.2f} km")

    q = lambda p: (round(p[0] / BULK_QUANT), round(p[1] / BULK_QUANT))

    # 1 · welke gekwantiseerde punten zijn een KRUISING of een UITEINDE?
    raak = {}
    for regio, lijnen in lijnen_per_regio.items():
        for _sig, pts in lijnen:
            for p in (pts[0], pts[-1]):
                raak[q(p)] = raak.get(q(p), 0) + 1
    knooppunt = set(raak)          # elk uiteinde is een knoop; kruisingen vallen samen

    # 2 · knoop-index opbouwen (hergebruik bestaande MARNET-knopen niet: het
    #     binnenwaternet is bewust een eigen component — zie de kop hierboven)
    knoop_id = {}
    def knoop_voor(p):
        k = q(p)
        if k not in knoop_id:
            knoop_id[k] = len(nodes)
            nodes.append((p[0], p[1]))
        return knoop_id[k]

    meta, n_edges = {}, 0
    for regio in sorted(lijnen_per_regio):
        lijnen = lijnen_per_regio[regio]
        eigen, km_tot = [], 0.0
        met_maat = 0
        for sig, pts in lijnen:
            maten = _gabariet_uit_signaal(sig)
            if maten:
                met_maat += 1
            # loop de lijn af en knip op knooppunten / elke BULK_KNOOP_KM
            start = 0
            sinds = 0.0
            for i in range(1, len(pts)):
                sinds += gc_km(pts[i - 1], pts[i])
                laatste = (i == len(pts) - 1)
                if not (laatste or q(pts[i]) in knooppunt or sinds >= BULK_KNOOP_KM):
                    continue
                stuk = pts[start:i + 1]
                if len(stuk) < 2:
                    continue
                a, b = knoop_voor(stuk[0]), knoop_voor(stuk[-1])
                if a != b:
                    ei = len(edge_lijst)
                    edge_lijst.append(((a, b), regio))
                    status[ei] = "binnen:" + regio
                    geometrie[ei] = stuk
                    eigen.append(ei)
                    km_tot += sinds
                    # PER EDGE, niet per label: het riviernet heeft geen
                    # systeem-klasse — elke lijn draagt zijn eigen signaal.
                    if maten:
                        edge_gabariet[ei] = tuple(
                            int(round(maten.get(k, 0) * 10))
                            for k in ("diepgang", "breedte", "lengte", "hoogte"))
                start, sinds = i, 0.0

        meta[regio] = {
            "zeevaart": False,
            "bulk": True,
            "cemt": "",
            "bron": "OSM (ODbL) via Geofabrik-regio-extract",
            "km": round(km_tot, 1),
            "edges": eigen,
            "aansluitKnoop": None,      # bewust los — overslag komt later
            "aansluitKm": None,
            "aansluitOvergang": "geen (overslaghaven volgt)",
            "volgtOp": "",
            "sluitAan": "",
            "sluitKm": None,
            "gabariet": {k: None for k in ("diepgang", "breedte", "lengte", "hoogte")},
        }
        n_edges += len(eigen)
        print(f"  {regio:<10} {km_tot:9,.0f} km · {len(eigen):7,} edges · "
              f"{met_maat:6,}/{len(lijnen):,} lijnen met een maat uit het signaal")
    print(f"  {'samen':<10} {sum(m['km'] for m in meta.values()):9,.0f} km · "
          f"{n_edges:7,} edges · {len(knoop_id):,} nieuwe knopen")
    return meta


def bulklaag(nodes, edge_lijst, status, geometrie, vaarwegen_meta, pad,
             extra_pad=None):
    """Leest vaarwegen_bulk.geojson, sluit dubbele geometrie uit, en geeft een
    losse structuur terug — MUTEERT nodes/edge_lijst/status NIET. Aparte
    uitvoer (marnet-bulk.json), niet marnet.bin: dat garandeert dat de elf
    regressie-invarianten per constructie ongemoeid blijven, niet toevallig.

    `extra_pad` (optioneel) is een klein, GECOMMIT geojson met HANDMATIG
    afgeleide vaarweglijnen die niet uit de OSM-fetch komen — zoals de
    Tongling-oostgeul, die OSM alleen als watervlak kent (middellijn afgeleid
    met middellijn_uit_vlakken.py). De grote `vaarwegen_bulk.geojson` staat in
    build-cache (gitignored, regenereerbaar uit de fetch); deze paar lijnen niet,
    dus ze horen apart en committen mee. Ze worden gewoon aan de bulk toegevoegd.
    """
    gj = json.load(open(pad, encoding="utf-8"))
    features = list(gj["features"])
    if extra_pad and os.path.exists(extra_pad):
        extra = json.load(open(extra_pad, encoding="utf-8"))
        n_extra = len(extra["features"])
        features += extra["features"]
        print(f"  + {n_extra} handmatige vaarweglijn(en) uit "
              f"{os.path.basename(extra_pad)}")
    per_regio = {}
    for f in features:
        p = f["properties"]
        regio = p["label"]                    # 'bulk-eu', 'bulk-cn', ...
        if not regio.startswith("bulk-"):
            raise RuntimeError(f"bulk-label {regio!r} mist het 'bulk-'-voorvoegsel")
        if regio in vaarwegen_meta:
            raise RuntimeError(f"{regio} botst met een verhalend systeemlabel")
        coords = [(wrap_lon(lo), la) for lo, la in f["geometry"]["coordinates"]]
        if len(coords) > 1:
            per_regio.setdefault(regio, []).append((p.get("signaal") or "?", coords))

    verhalend, slivers = _verhalende_lijnen(nodes, edge_lijst, status, geometrie,
                                            vaarwegen_meta)
    seg_pts, segs = [], []
    for lijn in verhalend:
        for i in range(len(lijn) - 1):
            seg_pts.append((lijn[i], lijn[i + 1]))
            segs.append(LineString([lijn[i], lijn[i + 1]]))
    boom = STRtree(segs)
    print(f"\nbulklaag uit {os.path.basename(pad)} — uitsluiting tegen "
          f"{len(verhalend):,} verhalende lijnen / {len(segs):,} segmenten "
          f"({slivers} zonder eigen geometrie, vallen terug op de koorde) "
          f"— eps {BULK_EPS_KM * 1000:.0f} m")

    regios = {}
    for regio in sorted(per_regio):
        lijnen = per_regio[regio]
        bron_km = sum(_lengte_km(p) for _s, p in lijnen)
        verdicht = [_verdicht_voor_toets(p) for _s, p in lijnen]
        houd, rap = snij_bulk(verdicht, boom, seg_pts)
        over_km = sum(_lengte_km(p) for _li, p in houd)
        punten = sum(len(p) for _li, p in houd)

        regios[regio] = {
            "zeevaart": False,
            "bulk": True,
            "cemt": "",
            "bron": gj.get("bron", "OSM (ODbL) via Geofabrik-regio-extract"),
            "km": round(over_km, 1),
            "bronKm": round(bron_km, 1),
            "weggenomenKm": round(bron_km - over_km, 1),
            "polylines": [[[round(lo, 5), round(la, 5)] for lo, la in p]
                          for _li, p in houd],
            # Het bevaarbaarheidssignaal per overgebleven lijn — dít veld draagt
            # de CEMT-klasse of de draft-waarde waar de maten uit volgen. Stond
            # als acceptatiepunt in LAR-515 ("achteraf toevoegen kost een
            # volledige rebake") maar werd de eerste keer weggegooid.
            "signalen": [lijnen[li][0] for li, _p in houd],
        }
        print(f"  {regio:<10} {bron_km:9,.0f} km bron -> {over_km:9,.0f} km over "
              f"(weg {bron_km - over_km:7,.0f} km = "
              f"{100 * (1 - over_km / max(bron_km, 1e-9)):4.1f}%) · "
              f"{len(houd):6,} lijnen · {punten:8,} punten · "
              f"{rap['vertices_weg']:,}/{rap['vertices']:,} vertices dicht · "
              f"{rap['runs']:,} runs (+{rap['snippers']:,} snipper<{BULK_MIN_KM} km weg) · "
              f"max weg {rap['max_weg_m']:.0f} m · dichtste bewaard "
              f"{rap['dichtste_bewaard_m']:.0f} m · {rap['paren']:,} paren getoetst · "
              f"{rap['hersteld']:,} lijnen heel gehouden ({rap['hersteld_km']:,.0f} km "
              f"die vroeger doormidden werd geknipt)")

    return {"regios": regios,
            "filterVersie": gj.get("filterVersie"),
            "extracts": gj.get("extracts", [])}


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


def verzoen_en_bak(vaarwegen_pad=None, bulk_pad=None, suffix="", binnenwater=False,
                   heal_km=0.0, corridor_km=0.0, bruggen_pad=None, meren_pad=None,
                   extra_vaarwegen_pad=None):
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

    # --- M24.6: bulklaag (LAR-515) — PUUR TEKENGEOMETRIE ---------------------
    # Bewust HIER: alles hierboven is de verhalende laag waar de 250 m-
    # uitsluiting tegenaan gedraaid wordt. Deze aanroep muteert nodes/
    # edge_lijst/status/geometrie NIET — marnet.bin/marnet.json/ports.json
    # zijn na deze regel nog exact wat ze hiervoor waren.
    bulk_meta = None
    zee_knopen = None          # None = geen beperking (er is geen binnenwaternet)
    # Per-edge gabariet dat NIET uit een systeemlabel volgt: het riviernet
    # heeft geen klasse per systeem, elke lijn draagt zijn eigen OSM-signaal.
    edge_gabariet = {}
    if bulk_pad:
        bulk_meta = bulklaag(nodes, edge_lijst, status, geometrie,
                             vaarwegen_meta, bulk_pad,
                             extra_pad=extra_vaarwegen_pad)
        if binnenwater:
            # ÉÉN NET: hetzelfde binnenwater gaat nu als echte knopen en edges
            # de graaf in i.p.v. als losse tekenlaag. De 250 m-uitsluiting die
            # hierboven al gedraaid is blijft gelden zolang de handgemaakte
            # ketens er nog liggen — zodra die verdwijnen neemt ze vanzelf
            # niets meer weg en sluit het net gewoon aan.
            #
            # Alles t/m hier is het ZEENET (+ de getoetste ketens); alles daarna
            # is riviernet. Die grens is wat `bak_havens()` gebruikt om elke
            # haven TWEE keer te snappen — een aanhechting per net (LAR-518).
            zee_knopen = len(nodes)
            print("\nbinnenwaternet -> de graaf (LAR-515 -> één net):")
            per_regio = {
                r: [(sig, [tuple(p) for p in pl])
                    for sig, pl in zip(v["signalen"], v["polylines"])]
                for r, v in bulk_meta["regios"].items()
            }
            # LAR-520-vervolg: verbindingsstukken over ongetagd water uit
            # knoop_riviernet.py. Vóór de heal toegevoegd, zodat tier-1/2 de
            # laatste meters van een brug-uiteinde gewoon mee-hecht. Signaal
            # "brug" draagt geen maat → onbekend = géén grens.
            for extra_pad in (bruggen_pad, meren_pad):
                if not extra_pad:
                    continue
                bgj = json.load(open(extra_pad, encoding="utf-8"))
                nb, kmb = 0, 0.0
                for f in bgj["features"]:
                    coords = [(wrap_lon(lo), la)
                              for lo, la in f["geometry"]["coordinates"]]
                    if len(coords) > 1:
                        per_regio.setdefault(f["properties"]["label"], []).append(
                            (f["properties"].get("signaal", "brug"), coords))
                        nb += 1
                        kmb += f["properties"].get("km", 0.0)
                print(f"  verbindingsstukken: {nb:,} ({kmb:,.0f} km) uit "
                      f"{os.path.basename(extra_pad)}")
            vaarwegen_meta.update(
                binnenwaternet(nodes, edge_lijst, status, geometrie,
                               vaarwegen_meta, per_regio, edge_gabariet,
                               heal_km=heal_km, corridor_km=corridor_km))
            # Valkuil 2 (LAR-520): de zee-rivier-scheiding is heilig. Het
            # riviernet krijgt eigen knopen (id >= zee_knopen) en mag NOOIT een
            # zeeknoop raken — de dragende Donau-ring-verdediging.
            rivier_edges = [ei for ei, s in status.items()
                            if s.startswith("binnen:") and vaarwegen_meta.get(
                                s[len("binnen:"):], {}).get("bulk")]
            kruis = sum(1 for ei in rivier_edges
                        if edge_lijst[ei][0][0] < zee_knopen
                        or edge_lijst[ei][0][1] < zee_knopen)
            assert kruis == 0, f"zee↔rivier-scheiding geschonden: {kruis} edges"
            print(f"  zee↔rivier-scheiding OK: 0 van {len(rivier_edges):,} "
                  f"riviernet-edges raakt een zeeknoop")
        else:
            bulk_json_pad = os.path.join(DATA, f"marnet-bulk{suffix}.json")
            with open(bulk_json_pad, "w", encoding="utf-8") as f:
                json.dump(bulk_meta, f, separators=(",", ":"))
            km_tot = sum(v["km"] for v in bulk_meta["regios"].values())
            km_weg = sum(v["weggenomenKm"] for v in bulk_meta["regios"].values())
            print(f"\n  bulklaag      : {km_tot:,.0f} km over {len(bulk_meta['regios'])} "
                  f"regio's (250 m-uitsluiting nam {km_weg:,.0f} km weg)")
            print(f"  {os.path.basename(bulk_json_pad):<20}: "
                  f"{os.path.getsize(bulk_json_pad) / 1024:,.0f} KB")

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
    #              soort (0=zee, 1=binnenwater), aantal geometriepunten,
    #              gabarietvlag (LAR-514: 0 = geen maten, 1 = er volgen er vier:
    #              diepgang, breedte, lengte, hoogte — in DECIMETER, 0=onbekend)
    #   3. geometrie: per edge de punten 2..n als delta's t.o.v. het vorige punt
    #              (punt 1 = knoop a, staat er dus niet nog eens in)
    #
    # De vlag scheelt drie bytes op elke ongemeten edge (~15.900 zee-edges), en
    # maakt het formaat zelfbeschrijvend: geen maten is iets anders dan vier
    # nullen, ook al gedragen ze zich hetzelfde.
    uit = bytearray()
    px = py = 0
    for x, y in node_q:
        varint(uit, x - px)
        varint(uit, y - py)
        px, py = x, y

    # Gabariet per edge (LAR-514): geërfd van het systeem waar de edge bij hoort.
    # Per edge en niet per label, om twee redenen die allebei echt voorkomen:
    # een poort zit vaak in een handvol sluis-edges van een systeem van honderden
    # km (de Seaway-beperking), en labelloze edges — de 16 graad-1-stubs uit
    # LAR-507 — kunnen per definitie niets erven.
    gab_per_edge = {}
    for ei, st in status.items():
        if not st.startswith("binnen:"):
            continue
        label = st[len("binnen:"):]
        meta_vw = vaarwegen_meta.get(label) or {}
        maten = edge_gabariet.get(ei) or gabariet_voor(label, meta_vw.get("cemt", ""))
        if any(maten):
            gab_per_edge[ei] = maten

    vorige_a = vorige_b = 0
    for ei, ((a, b), _p) in enumerate(edge_lijst):
        soort = 1 if status.get(ei, "").startswith("binnen:") else 0
        varint(uit, a - vorige_a)
        varint(uit, b - vorige_b)
        varint(uit, int(round(edge_lengtes[ei] * 10)))
        varint(uit, soort)
        varint(uit, len(edge_geoms[ei]))
        maten = gab_per_edge.get(ei)
        varint(uit, 1 if maten else 0)
        if maten:
            for m in maten:
                varint(uit, m)
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

    bak_havens(nodes, node_q, suffix, zee_knopen=zee_knopen, land=land)
    return onopgelost


def _laad_wpi():
    """NGA World Port Index uit de build-cache (fetch_wpi.py), op LOCODE.

    13 LOCODEs dragen meerdere WPI-havens; de grootste wint (L > M > S > V).
    Geen wpi.json = lege dict — de bake draait dan gewoon zonder verrijking,
    een ontbrekende bron mag de haven-bake niet breken.
    """
    pad = os.path.join(CACHE, "wpi.json")
    if not os.path.exists(pad):
        return {}
    orde = {"L": 3, "M": 2, "S": 1, "V": 0}
    per = {}
    for h in json.load(open(pad, encoding="utf-8"))["havens"]:
        code = (h.get("unloCode") or "").replace(" ", "")
        if not code:
            continue
        oud = per.get(code)
        if oud is None or orde.get(h.get("harborSize"), -1) > orde.get(oud.get("harborSize"), -1):
            per[code] = h
    return per


# Havens die in searoute's lijst ontbreken maar aantoonbaar bestaan — uit de
# WPI (publiek domein), op LOCODE. Saldanha Bay was het enige gat in de vijftien
# grote bulkhavens (toets_havens.py, 2026-07-21).
WPI_EXTRA_HAVENS = ["ZASDB"]

# WPI-vrachtfaciliteiten -> één letter voor het compacte veld. ⚠️ Alleen een
# expliciete "Y" telt: de WPI zet massaal "U" (unknown) — zelfs Rotterdam — en
# onbekend mag nooit als "geen vracht" gelezen worden (het draagprincipe van
# het gabariet-veld geldt hier ook).
WPI_VRACHT = (("loWharves", "W"), ("loContainer", "C"), ("loSolidBulk", "D"),
              ("loLiquidBulk", "V"), ("loOilTerm", "O"), ("loRoro", "R"),
              ("loBreakBulk", "S"))


def bak_havens(nodes, node_q, suffix="", zee_knopen=None, land=None):
    """searoute's havens, gesnapt aan BEIDE netten (LAR-518).

    ⚠️ EEN HAVEN HEEFT TWEE AANHECHTINGEN, en dat is de kern van dit issue.
    Havens snappen op de dichtstbijzijnde knoop, en zodra het riviernet in de
    graaf ligt is dat voor een zeehaven vaak een riviernet-knoop: Rotterdam
    verhuisde van knoop 6818 (0,6 km) naar een riviernet-knoop op 1,1 km en kon
    daarna NIETS meer bereiken — ook Shanghai niet — want het riviernet is
    bewust een eigen component.

    Dat was geen bug maar het bewijs dat een zeehaven ÉN een binnenhaven is.
    Eén snap kan die twee rollen niet dragen, dus snappen we nu twee keer:
    `knoop`/`afstandKm` op het ZEENET (ongewijzigd, alle bestaande zeeroutes
    rekenen hierop) en `knoopRivier`/`afstandRivierKm` op het RIVIERNET. De
    overstap ertussen is de overslag.

    `zee_knopen` = het aantal knopen dat tot het zeenet hoort; alles daarboven
    is riviernet (zie verzoen_en_bak). None = er is geen riviernet gebakken,
    dan blijft alles bij het oude en is er niets om aan te koppelen.

    ⚠️ De rivier-afstand wordt RUW weggeschreven, ook als hij 800 km is. Een
    drempel hoort bij wie hem gebruikt, niet bij de meting — anders verdwijnt
    het verschil tussen "geen binnenwater in de buurt" en "wij vonden het te
    ver", en dat is precies het soort stille beslissing dat later onvindbaar is.
    """
    gj = json.load(open(os.path.join(SR_DATA, "ports.geojson"), encoding="utf-8"))
    havens = []
    for f in gj["features"]:
        lon, lat = f["geometry"]["coordinates"]
        p = f["properties"]
        havens.append((p.get("name") or p.get("port"), p.get("cty") or "", p.get("port") or "", lon, lat))

    # WPI-verrijking (LAR-518 stap "havens op de juiste plek"): join op LOCODE.
    wpi = _laad_wpi()
    bestaand = {h[2] for h in havens}
    for code in WPI_EXTRA_HAVENS:
        w = wpi.get(code)
        if w is None:
            print(f"  ⚠️ WPI-extra {code} niet beschikbaar (draai fetch_wpi.py) — overgeslagen")
        elif code not in bestaand:
            havens.append((w["portName"], (w.get("countryName") or "").replace(" ", "_"),
                           code, float(w["xcoord"]), float(w["ycoord"])))
    havens.sort(key=lambda h: (h[1], h[0]))

    # dichtstbijzijnde knoop in 3D (koorde-afstand = monotone proxy voor grootcirkel)
    grens = len(node_q) if zee_knopen is None else zee_knopen
    zee_xyz = np.array([to3d(lo / SCHAAL, la / SCHAAL) for lo, la in node_q[:grens]])
    riv_xyz = (np.array([to3d(lo / SCHAAL, la / SCHAAL) for lo, la in node_q[grens:]])
               if grens < len(node_q) else None)

    namen, landen, locodes, ll = [], [], [], []
    knoop, afstand = [], []            # zeenet
    knoop_riv, afstand_riv = [], []    # riviernet (-1 = geen riviernet gebakken)
    afstand_water = []                 # tot kustlijn of meeroever (-1 = niet gemeten)
    wpi_maat, wpi_spoor, wpi_vracht = [], [], []
    wpi_afstand = []                   # searoute-punt <-> WPI-punt (-1 = geen match)
    pos_bron = []                      # "locode" | "wpi" — waar de positie vandaan komt

    def waterscore(lo, la):
        """Hoe ver ligt dit punt van bevaarbaar water (kust/meer of riviernet)?
        De maat waarop een positie-verplaatsing beoordeeld wordt."""
        s = land.afstand_tot_open_water(lo, la)
        if riv_xyz is not None:
            dr = float(np.max(riv_xyz @ np.array(to3d(lo, la))))
            s = min(s, R_AARDE * math.acos(max(-1.0, min(1.0, dr))))
        return s

    # Generieke haven-woorden mogen een >200 km-match niet dragen: "Puerto
    # Morelos" vs "Puerto Morro Redondo" deelt alleen "puerto" en is een
    # verkeerde identiteit. Exacte naamgelijkheid blijft altijd geldig, zodat
    # "Santa Fe" (alleen generieke/korte tokens) wél gewoon matcht.
    NAAM_GENERIEK = {"puerto", "porto", "port", "harbor", "harbour", "haven",
                     "bahia", "baie", "saint", "sankt", "nuevo", "nueva", "city"}

    def _naam_matcht(a, w):
        """Delen twee havennamen hun identiteit? Alleen gebruikt als poort bij
        verplaatsingen >200 km: daar betekent een naamverschil geen centroïde-
        vs-kade meer, maar een verkeerde identiteit (dezelfde LOCODE op twee
        verschillende plaatsen in één van de bronnen)."""
        norm = lambda s: (s or "").lower().strip()
        if norm(a) and norm(a) in (norm(w.get("portName")), norm(w.get("alternateName"))):
            return True
        woorden = lambda s: {t for t in norm(s).replace("-", " ").split()
                             if len(t) >= 4} - NAAM_GENERIEK
        return bool(woorden(a) & (woorden(w.get("portName")) | woorden(w.get("alternateName"))))

    verplaatst, geweigerd_naam = [], []
    for hi, (naam, cty, code, lon, lat) in enumerate(havens):
        w = wpi.get(code)
        bron = "wpi" if code in WPI_EXTRA_HAVENS else "locode"
        if w is not None and land is not None:
            wlon, wlat = float(w["xcoord"]), float(w["ycoord"])
            dpos = gc_km((lon, lat), (wlon, wlat))
            # POSITIE-SCHONING (stap 2, "havens op de juiste plek"): de LOCODE-
            # positie is een plaatscentroïde, de WPI-positie is haven-
            # georiënteerd. Onder de kilometer is het verschil resolutieruis
            # (beide bronnen werken op boogminuten); daarboven verhuist de
            # haven naar de WPI-plek — MITS die aan water ligt: dichter bij
            # zee/meer/riviernet dan de oude plek, of hooguit 2 km ervan.
            # Een verplaatsing die het land in schiet is erger dan een
            # centroïde, dus de watertoets is de poortwachter. Boven 200 km
            # komt daar de naamtoets bij: zo repareert USPWM "Portland" wél
            # (Oregon → Maine, allebei Portland) maar blijft een LOCODE die
            # in de WPI op een ándere plaats wijst gewoon staan.
            if (dpos >= 1.0
                    and waterscore(wlon, wlat) <= max(waterscore(lon, lat), 2.0)):
                if dpos > 200 and not _naam_matcht(naam, w):
                    geweigerd_naam.append((dpos, naam, w.get("portName")))
                else:
                    verplaatst.append(dpos)
                    lon, lat = wlon, wlat
                    havens[hi] = (naam, cty, code, lon, lat)
                    bron = "wpi"
        pos_bron.append(bron)
        if w is None:
            wpi_maat.append("")
            wpi_spoor.append("")
            wpi_vracht.append("")
            wpi_afstand.append(-1)
        else:
            wpi_maat.append((w.get("harborSize") or "").strip())
            sp = (w.get("railway") or "").strip()
            wpi_spoor.append(sp if sp in ("S", "M", "L") else "")
            wpi_vracht.append("".join(letter for veld, letter in WPI_VRACHT
                                      if (w.get(veld) or "").strip() == "Y"))
            wpi_afstand.append(round(gc_km((lon, lat),
                                           (float(w["xcoord"]), float(w["ycoord"]))), 1))
        v = np.array(to3d(lon, lat))
        d = zee_xyz @ v
        beste = int(np.argmax(d))
        km = R_AARDE * math.acos(max(-1.0, min(1.0, float(d[beste]))))
        namen.append(naam)
        landen.append(cty)
        locodes.append(code)
        ll.extend([round(lon, 3), round(lat, 3)])
        knoop.append(beste)
        afstand.append(round(km, 1))
        if riv_xyz is None:
            knoop_riv.append(-1)
            afstand_riv.append(-1)
        else:
            dr = riv_xyz @ v
            besteR = int(np.argmax(dr))
            kmR = R_AARDE * math.acos(max(-1.0, min(1.0, float(dr[besteR]))))
            knoop_riv.append(grens + besteR)   # index in de VOLLEDIGE knopenlijst
            afstand_riv.append(round(kmR, 1))
        afstand_water.append(round(land.afstand_tot_open_water(lon, lat), 1)
                             if land is not None else -1)
    uit = {
        "aantal": len(namen),
        "namen": namen,
        "landen": landen,
        "locodes": locodes,
        "ll": ll,
        "knoop": knoop,
        "afstandKm": afstand,
        "knoopRivier": knoop_riv,
        "afstandRivierKm": afstand_riv,
        "afstandWaterKm": afstand_water,
        "wpiMaat": wpi_maat,
        "wpiSpoor": wpi_spoor,
        "wpiVracht": wpi_vracht,
        "wpiAfstandKm": wpi_afstand,
        "posBron": pos_bron,
        "zeeKnopen": grens,
        "bron": "searoute 1.6.0 ports.geojson (= UN/LOCODE-locatielijst, niet gefilterd)"
                + (" + NGA World Port Index Pub 150 (publiek domein) op LOCODE"
                   if wpi else ""),
    }
    pad = os.path.join(DATA, f"ports{suffix}.json")
    with open(pad, "w", encoding="utf-8") as f:
        json.dump(uit, f, ensure_ascii=False, separators=(",", ":"))
    ver = [a for a in afstand if a > 50]
    print(f"  havens        : {len(namen):,} -> {os.path.basename(pad)} ({os.path.getsize(pad) / 1024:,.0f} KB)"
          f" | zee-snap mediaan {np.median(afstand):.0f} km, >50 km: {len(ver)}")
    if riv_xyz is not None:
        ar = np.array(afstand_riv)
        print(f"  {'':14}  | rivier-snap mediaan {np.median(ar):.1f} km · "
              f"≤1 km: {int((ar <= 1).sum()):,} · ≤5 km: {int((ar <= 5).sum()):,} · "
              f"≤25 km: {int((ar <= 25).sum()):,} · >50 km: {int((ar > 50).sum()):,}")
        # Hoeveel havens raken BEIDE netten? Dat is de kandidatenvijver waaruit
        # de aangewezen overslaghavens gekozen worden — niet het criterium zelf
        # (Lars: dan mis je de overslag binnenvaart -> spoor/vrachtwagen).
        az = np.array(afstand)
        print(f"  {'':14}  | raakt BEIDE netten ≤5 km: {int(((az <= 5) & (ar <= 5)).sum()):,} · "
              f"≤25 km: {int(((az <= 25) & (ar <= 25)).sum()):,}")
    if land is not None:
        # ⚠️ De havenpoort: ligt dit punt uberhaupt AAN WATER? De bron is een
        # UN/LOCODE-lijst en bevat dus wegterminals en grensovergangen (Denver,
        # Laramie, Tecate). Met het oog niet te vinden, wel te meten.
        aw = np.array(afstand_water, dtype=float)
        rr = np.array(afstand_riv, dtype=float)
        rr[rr < 0] = np.inf
        water = np.minimum(aw, rr)
        print(f"  {'':14}  | AAN WATER (kust/meer/rivier) ≤10 km: "
              f"{int((water <= 10).sum()):,} · NIET aan water: {int((water > 10).sum()):,} "
              f"({(water > 10).sum() / len(namen) * 100:.1f}%) · verst {water.max():,.0f} km")
    if wpi:
        wm = sum(1 for m in wpi_maat if m)
        ws = sum(1 for s in wpi_spoor if s)
        wv = sum(1 for v in wpi_vracht if v)
        wa = np.array([a for a in wpi_afstand if a >= 0])
        print(f"  {'':14}  | WPI-match: {wm:,} van {len(namen):,} · spoor bevestigd: {ws:,} · "
              f"vracht bevestigd: {wv:,} · positieverschil mediaan {np.median(wa):.1f} km, "
              f">10 km: {int((wa > 10).sum()):,}")
        if verplaatst:
            vp = np.array(verplaatst)
            print(f"  {'':14}  | posities geschoond: {len(vp):,} havens naar de WPI-plek "
                  f"(mediaan {np.median(vp):.1f} km, max {vp.max():.0f} km; "
                  f"watertoets als poortwachter)")
        for dpos, naam, wnaam in sorted(geweigerd_naam, reverse=True):
            print(f"  {'':14}  | ⚠️ NIET verplaatst ({dpos:,.0f} km, naam botst): "
                  f"{naam!r} vs WPI {wnaam!r} — zelfde LOCODE, andere plaats")
    # de LAR-486/518-acceptatiehavens expliciet rapporteren
    for wie in ("Amsterdam", "Nijmegen", "Rotterdam", "Duluth"):
        for i, naam in enumerate(namen):
            if naam == wie and landen[i] in ("Netherlands", "United_states"):
                extra = (f" | rivier {knoop_riv[i]} · {afstand_riv[i]:.1f} km"
                         if riv_xyz is not None else "")
                print(f"    snap {naam:<10} ({landen[i][:2]}): zee {knoop[i]} · "
                      f"{afstand[i]:.1f} km{extra}")
                break


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--analyse", action="store_true", help="alleen het rapport")
    ap.add_argument("--vaarwegen", help="GeoJSON uit fetch_waterways.py (M24/LAR-486): "
                                        "vaarweg-ketens aan de graaf hangen")
    ap.add_argument("--bulk", help="vaarwegen_bulk.geojson uit fetch_waterways.py --bulk "
                                   "(LAR-515): puur tekengeometrie, apart bestand "
                                   "marnet-bulk<suffix>.json, muteert de graaf niet")
    ap.add_argument("--bruggen", help="vaarwegen_bruggen.geojson uit knoop_riviernet.py: "
                                      "verbindingsstukken over ongetagd water (sig 'brug'), "
                                      "alleen zinvol samen met --binnenwater")
    ap.add_argument("--meren", help="vaarwegen_meren.geojson uit knoop_riviernet.py --meren: "
                                    "meer-oversteken over watervlakken (sig 'meer')")
    ap.add_argument("--binnenwater", action="store_true",
                    help="hang het gemapte binnenwater als ECHTE knopen/edges in de graaf "
                         "i.p.v. als losse tekenlaag (één net; losse uiteinden zijn OK, "
                         "aansluiting op zee gaat later via overslaghavens)")
    ap.add_argument("--suffix", default="", help="achtervoegsel voor de uitvoerbestanden "
                                                 "(marnet<suffix>.bin/json, ports<suffix>.json) "
                                                 "— voor de bake-off-variant")
    ap.add_argument("--extra-vaarwegen", help="klein GECOMMIT geojson met handmatig "
                                              "afgeleide vaarweglijnen (bulk-<regio>-features) "
                                              "die niet uit de OSM-fetch komen, bv. de "
                                              "Tongling-oostgeul (data/vaarwegen-handmatig.geojson)")
    ap.add_argument("--heal-km", type=float, default=0.0,
                    help="tier-1 confluentie-heal (LAR-520): hecht een lijn-uiteinde dat "
                         "binnen deze afstand OP een andere lijn projecteert daar aan "
                         "(over water per constructie). 0 = uit (huidig gedrag).")
    ap.add_argument("--corridor-km", type=float, default=0.0,
                    help="tier-2 corridor-heal (LAR-520): verbind twee UITEINDEN van "
                         "verschillende componenten binnen deze afstand als ze collineair "
                         "in elkaars verlengde liggen (richtingstoets). 0 = uit.")
    args = ap.parse_args()
    if args.analyse:
        analyse()
    else:
        verzoen_en_bak(vaarwegen_pad=args.vaarwegen, bulk_pad=args.bulk, suffix=args.suffix,
                       binnenwater=args.binnenwater, heal_km=args.heal_km,
                       corridor_km=args.corridor_km, bruggen_pad=args.bruggen,
                       meren_pad=args.meren, extra_vaarwegen_pad=args.extra_vaarwegen)
