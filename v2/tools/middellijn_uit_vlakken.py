#!/usr/bin/env python3
"""middellijn_uit_vlakken.py — vaarwegmiddellijn uit WATERVLAKKEN (M24-uitrol).

Waarom dit bestaat: de rest van de pijplijn stitcht een middellijn uit benoemde
`waterway=river|canal`-LIJNEN. Voor brede rivieren bestaan die lijnen niet. De
Amazone tussen Manaus en Belém — juist waar de zeeschepen varen — heeft geen
enkele benoemde middellijn in OSM, omdat de rivier daar >10 km breed is en als
wátervlak gemapt staat. Zelfde probleem bij de Rio de la Plata, de Wolga-
stuwmeren en elk estuarium.

De aanpak (klassiek, en hij hergebruikt wat M23 al deed met rasters):
  1. watervlakken uit de extract halen (`natural=water` / `waterway=riverbank`,
     inclusief multipolygoon-relaties — grote rivieren zijn bijna altijd relaties)
  2. rasteriseren tot een watermasker
  3. per watercel de KLARING bepalen: afstand tot de dichtstbijzijnde oever
     (exacte Euclidische afstandstransformatie, anisotroop want een graad lon is
     korter dan een graad lat)
  4. alleen cellen met genoeg klaring gelden als bevaarbaar — dat encodeert
     "commercieel bevaarbaar" meteen in de geometrie
  5. Dijkstra van anker naar anker over die cellen, met een milde voorkeur voor
     het midden van de vaargeul
  6. terug naar lon/lat + Douglas-Peucker

Het resultaat is bewust GEEN medial axis: we willen één vaarbare lijn van A naar
B, geen skelet met zijtakken.

Draaien (zelfstandig, voor een test):
  python v2/tools/middellijn_uit_vlakken.py --extract brazilie \
      --bbox -3.6 -60.6 0.2 -47.9 --zee -48.50 -0.72 --binnen -60.02 -3.13
"""

import argparse
import hashlib
import heapq
import json
import math
import os
import sys
import time

import numpy as np
import osmium
import shapely
from scipy.ndimage import distance_transform_edt

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)
GEOFABRIK = os.path.join(V2, "build-cache", "geofabrik")

R_AARDE = 6371.0
MIN_KLARING_KM = 0.15    # halve geulbreedte: <300 m breed telt niet als vaarweg
MIDDEN_ALPHA = 0.6       # hoe sterk de route het midden opzoekt (0 = kortste pad)


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[1], a[0], b[1], b[0]))
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R_AARDE * math.asin(min(1.0, math.sqrt(h)))


# ------------------------------------------------------------- watervlakken

def raster(extracts, bbox, cel_graden, min_cellen=4):
    """Watermasker + klaring (km) per cel, in ÉÉN pass over de extract.

    Elk watervlak wordt meteen in het raster gebrand en daarna weggegooid. De
    eerste versie verzamelde ze allemaal en deed er één `union_all` overheen —
    dat liep op de Amazone naar 5,5 GB en was nog niet klaar na 11 minuten CPU,
    want een venster over het Amazonebekken bevat duizenden meren en
    overstromingsvlaktes. Zo blijft het geheugen vlak (alleen het raster) en
    vervalt de union volledig: OR-en in een boolean array doet hetzelfde werk.

    `with_areas()` blijft nodig — grote rivieren zijn multipolygoon-relaties,
    zelden één gesloten way.
    """
    la0, lo0, la1, lo1 = bbox
    lons = np.arange(lo0, lo1, cel_graden)
    lats = np.arange(la0, la1, cel_graden)
    masker = np.zeros((len(lats), len(lons)), dtype=bool)
    # vlakken die kleiner zijn dan een handvol cellen kunnen nooit vaarweg zijn
    min_opp = (cel_graden ** 2) * min_cellen

    for sleutel in extracts:
        pad = os.path.join(GEOFABRIK, f"{sleutel}-latest.osm.pbf")
        if not os.path.exists(pad):
            raise SystemExit(f"ontbreekt: {pad}")
        t0, n, gebrand = time.time(), 0, 0
        wkb_fab = osmium.geom.WKBFactory()
        for obj in osmium.FileProcessor(pad).with_areas():
            if not isinstance(obj, osmium.osm.Area):
                continue
            t = obj.tags
            if not (t.get("natural") == "water" or t.get("waterway") == "riverbank"):
                continue
            n += 1
            try:
                g = shapely.from_wkb(bytes.fromhex(wkb_fab.create_multipolygon(obj)))
            except Exception:                      # noqa: BLE001 — kapotte ring, overslaan
                continue
            x0, y0, x1, y1 = g.bounds
            if x1 < lo0 or x0 > lo1 or y1 < la0 or y0 > la1:
                continue
            if (x1 - x0) * (y1 - y0) < min_opp:
                continue
            # alleen de cellen binnen de bbox van dít vlak toetsen
            j0 = max(0, int((x0 - lo0) / cel_graden))
            j1 = min(len(lons), int((x1 - lo0) / cel_graden) + 2)
            i0 = max(0, int((y0 - la0) / cel_graden))
            i1 = min(len(lats), int((y1 - la0) / cel_graden) + 2)
            if j1 <= j0 or i1 <= i0:
                continue
            LO, LA = np.meshgrid(lons[j0:j1], lats[i0:i1])
            shapely.prepare(g)
            binnen = shapely.contains_xy(g, LO.ravel(), LA.ravel()).reshape(LA.shape)
            if binnen.any():
                masker[i0:i1, j0:j1] |= binnen
                gebrand += 1
        print(f"  {sleutel:14s} {n:7,d} watervlakken · {gebrand:6,d} geraakt het venster "
              f"· {time.time() - t0:4.0f}s")

    if not masker.any():
        raise SystemExit("geen water in het raster — bbox/tags checken")
    # anisotrope celmaat: een graad lon is cos(lat) korter dan een graad lat
    dy = cel_graden * 111.2
    dx = cel_graden * 111.2 * math.cos(math.radians((la0 + la1) / 2))
    klaring = distance_transform_edt(masker, sampling=(dy, dx))
    return lons, lats, masker, klaring


# ----------------------------------------------------------------- dijkstra

BUREN = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def vaarpad(lons, lats, klaring, anker_zee, anker_binnen,
            min_klaring=MIN_KLARING_KM, alpha=MIDDEN_ALPHA):
    ny, nx = klaring.shape
    dy = (lats[1] - lats[0]) * 111.2
    dx = (lons[1] - lons[0]) * 111.2 * math.cos(math.radians(float(lats.mean())))
    bevaarbaar = klaring >= min_klaring
    if not bevaarbaar.any():
        raise SystemExit(f"geen cel haalt {min_klaring} km klaring — raster te grof?")

    def cel(p):
        j = int(round((p[0] - lons[0]) / (lons[1] - lons[0])))
        i = int(round((p[1] - lats[0]) / (lats[1] - lats[0])))
        i, j = max(0, min(ny - 1, i)), max(0, min(nx - 1, j))
        if bevaarbaar[i, j]:
            return i, j
        # anker ligt net buiten de geul -> pak de dichtstbijzijnde bevaarbare cel
        ii, jj = np.nonzero(bevaarbaar)
        d = ((ii - i) * dy) ** 2 + ((jj - j) * dx) ** 2
        k = int(np.argmin(d))
        return int(ii[k]), int(jj[k])

    start, doel = cel(anker_zee), cel(anker_binnen)
    kost = np.full((ny, nx), np.inf)
    vorige = np.full((ny, nx, 2), -1, dtype=np.int32)
    kost[start] = 0.0
    pq = [(0.0, start[0], start[1])]
    klaar = np.zeros((ny, nx), dtype=bool)
    while pq:
        k, i, j = heapq.heappop(pq)
        if klaar[i, j]:
            continue
        klaar[i, j] = True
        if (i, j) == doel:
            break
        for di, dj in BUREN:
            a, b = i + di, j + dj
            if not (0 <= a < ny and 0 <= b < nx) or klaar[a, b] or not bevaarbaar[a, b]:
                continue
            stap = math.hypot(di * dy, dj * dx)
            # milde voorkeur voor het midden: krap water wordt duurder, maar
            # nooit zo duur dat hij een absurde omweg neemt
            straf = 1.0 + alpha * (min_klaring / max(klaring[a, b], min_klaring))
            nk = k + stap * straf
            if nk < kost[a, b]:
                kost[a, b] = nk
                vorige[a, b] = (i, j)
                heapq.heappush(pq, (nk, a, b))
    if not klaar[doel]:
        raise SystemExit("geen doorlopende vaargeul tussen de ankers "
                         "(min_klaring te hoog, of het water is onderbroken)")

    pad = []
    i, j = doel
    while (i, j) != start:
        pad.append((float(lons[j]), float(lats[i])))
        i, j = vorige[i, j]
    pad.append((float(lons[start[1]]), float(lats[start[0]])))
    pad.reverse()
    klaringen = [float(klaring[
        int(round((p[1] - lats[0]) / (lats[1] - lats[0]))),
        int(round((p[0] - lons[0]) / (lons[1] - lons[0])))]) for p in pad]
    return pad, klaringen


# ----------------------------------------------------------------- simplify

def simplify(pts, tol_km):
    if len(pts) < 3:
        return list(pts)
    coslat = math.cos(math.radians(sum(p[1] for p in pts) / len(pts)))

    def afstand(p, a, b):
        ax, ay = (a[0] - p[0]) * coslat, a[1] - p[1]
        bx, by = (b[0] - p[0]) * coslat, b[1] - p[1]
        ddx, ddy = bx - ax, by - ay
        den = math.hypot(ddx, ddy)
        if den < 1e-12:
            return math.hypot(ax, ay) * 111.2
        return abs(ax * ddy - ay * ddx) / den * 111.2

    houd = [False] * len(pts)
    houd[0] = houd[-1] = True
    stapel = [(0, len(pts) - 1)]
    while stapel:
        i, j = stapel.pop()
        if j <= i + 1:
            continue
        verste, verste_d = -1, -1.0
        for k in range(i + 1, j):
            d = afstand(pts[k], pts[i], pts[j])
            if d > verste_d:
                verste, verste_d = k, d
        if verste_d > tol_km:
            houd[verste] = True
            stapel.append((i, verste))
            stapel.append((verste, j))
    return [p for p, h in zip(pts, houd) if h]


# ----------------------------------------------------------------- hoofdflow

def afleiden(extracts, bbox, anker_zee, anker_binnen, cel_graden=0.004,
             min_klaring=MIN_KLARING_KM, simplify_km=0.25):
    # Bewaarpunt éérst bij dure pijplijnen (de les uit LAR-486): de rasterstap
    # kost bij Brazilië ~13 min omdat osmium twee passes over 2 GB moet doen om
    # de multipolygoon-relaties te reconstrueren. De sleutel bevat alles wat de
    # uitkomst bepaalt, dus hij vervalt vanzelf als er iets aan verandert.
    sleutel = hashlib.sha1(repr((sorted(extracts), bbox, anker_zee, anker_binnen,
                                 cel_graden, min_klaring, simplify_km)).encode()
                           ).hexdigest()[:16]
    cache_map = os.path.join(V2, "build-cache", "middellijnen")
    cache_pad = os.path.join(cache_map, f"{sleutel}.json")
    if os.path.exists(cache_pad):
        c = json.load(open(cache_pad, encoding="utf-8"))
        print(f"  middellijn uit cache ({sleutel}): {c['km']} km · {len(c['lijn'])} punten")
        return [tuple(p) for p in c["lijn"]], c["km"], c["klaringen"]

    print(f"watervlakken rasteren ({', '.join(extracts)}):")
    t0 = time.time()
    lons, lats, masker, klaring = raster(extracts, bbox, cel_graden)
    print(f"  raster {masker.shape[1]}x{masker.shape[0]} @ {cel_graden}° "
          f"(~{cel_graden * 111.2 * 1000:.0f} m) · {masker.sum():,} watercellen · "
          f"{time.time() - t0:.0f}s")
    print(f"  klaring: max {klaring.max():.1f} km · "
          f"cellen >= {min_klaring} km: {(klaring >= min_klaring).sum():,}")
    pad, klaringen = vaarpad(lons, lats, klaring, anker_zee, anker_binnen,
                             min_klaring=min_klaring)
    lengte = sum(km(pad[i], pad[i + 1]) for i in range(len(pad) - 1))
    strak = simplify(pad, simplify_km)
    kl = sorted(klaringen)
    print(f"  vaarpad: {lengte:.1f} km · {len(pad):,} cellen -> {len(strak)} na simplify")
    print(f"  klaring langs de route: min {kl[0]:.2f} · mediaan {kl[len(kl) // 2]:.2f} "
          f"· max {kl[-1]:.2f} km")
    os.makedirs(cache_map, exist_ok=True)
    with open(cache_pad, "w", encoding="utf-8") as f:
        json.dump({"km": round(lengte, 1), "lijn": [list(p) for p in strak],
                   "klaringen": klaringen}, f)
    return strak, lengte, klaringen


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--extract", required=True, help="komma-gescheiden regio-sleutels")
    ap.add_argument("--bbox", nargs=4, type=float, required=True,
                    metavar=("LAT0", "LON0", "LAT1", "LON1"))
    ap.add_argument("--zee", nargs=2, type=float, required=True, metavar=("LON", "LAT"))
    ap.add_argument("--binnen", nargs=2, type=float, required=True, metavar=("LON", "LAT"))
    ap.add_argument("--cel", type=float, default=0.004)
    ap.add_argument("--min-klaring", type=float, default=MIN_KLARING_KM)
    ap.add_argument("--uit", help="schrijf de lijn als GeoJSON naar dit pad")
    a = ap.parse_args()
    lijn, lengte, _ = afleiden([s.strip() for s in a.extract.split(",")],
                               tuple(a.bbox), tuple(a.zee), tuple(a.binnen),
                               cel_graden=a.cel, min_klaring=a.min_klaring)
    if a.uit:
        import json
        with open(a.uit, "w", encoding="utf-8") as f:
            json.dump({"type": "Feature",
                       "properties": {"km": round(lengte, 1), "bron": "OSM-watervlakken"},
                       "geometry": {"type": "LineString",
                                    "coordinates": [[round(lo, 6), round(la, 6)]
                                                    for lo, la in lijn]}}, f)
        print(f"geschreven: {a.uit}")
