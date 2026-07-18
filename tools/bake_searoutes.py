# bake_searoutes.py — bakt de zee-corridors met searoute (MARNET) en schrijft
# data/_searoutes.js. De build-time kant van M18 (design/zeeroutes.md §3).
#
#   python tools/bake_searoutes.py copper          # pilot: alleen koper
#   python tools/bake_searoutes.py                 # alle grondstoffen
#
# Principes (spec §3–§4):
#   - MARNET beslist: corridors kaal haven→haven, geen via-dwang.
#   - Determinisme: gesorteerde sleutels, 3 decimalen, geen tijdstempels.
#   - Fouten hard: een corridor die niet routeert = build FAALT (exit 1) met de
#     coördinaten erbij. Dat zijn de nodes die een handmatig duwtje nodig hebben.
#   - traversed_passages per corridor meegeschreven (M21-query + kruiscontrole).

import heapq
import json
import math
import re
import subprocess
import sys
import warnings
from pathlib import Path

import searoute as sr

warnings.filterwarnings("ignore")  # de no-path-warning vangen we zelf, hard

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "_searoutes.js"
PRECISION = 3  # ~110 m; vastgelegd in design/zeeroutes.md §3

# ---------------------------------------------------------------- LANDMASKER
# Dezelfde landpolygonen als de kaart zelf (geo-data.js, Natural Earth 50m,
# meren als gaten). Nodig voor twee reparaties op het ruwe MARNET-pad:
# 1. DE-ZIGZAG: het netwerk heeft bij haven-aanlopen soms een zigzag van
#    >100 graden binnen tientallen km (Yangtze-monding: 140+105 graden) — de
#    curve slaat daar om. Middenpunt weghalen mag alleen als de kortsluiting
#    over water loopt.
# 2. LAND-OMLEIDING: verre netwerk-knopen geven segmenten die land snijden
#    (Vogelkop-schiereiland, Isla Guadalupe). Lokale A* over een 0,1-graden
#    waterraster legt het segment om het obstakel heen.
# Kanalen (Panama/Suez) zijn land in Natural Earth maar horen bij de route.

CANALS = [(9.0, -79.6), (30.5, 32.3)]  # Panama, Suez


def load_land():
    txt = (ROOT / "geo-data.js").read_text(encoding="utf-8")
    m = re.search(r"const LAND_POLYS = (\[.*?\]);\n", txt, re.S)
    polys = []
    for rings in json.loads(m.group(1)):
        xs = [p[0] for p in rings[0]]
        ys = [p[1] for p in rings[0]]
        polys.append((min(xs), max(xs), min(ys), max(ys), rings))
    return polys


LAND = load_land()


def _in_ring(lon, lat, ring):
    inside = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i][0], ring[i][1]
        xj, yj = ring[j][0], ring[j][1]
        if (yi > lat) != (yj > lat) and lon < (xj - xi) * (lat - yi) / (yj - yi) + xi:
            inside = not inside
        j = i
    return inside


def is_land(lat, lon):
    lon = ((lon + 180) % 360) - 180
    for minx, maxx, miny, maxy, rings in LAND:
        if lon < minx or lon > maxx or lat < miny or lat > maxy:
            continue
        if _in_ring(lon, lat, rings[0]):
            for hole in rings[1:]:
                if _in_ring(lon, lat, hole):
                    return False
            return True
    return False


def near_canal(lat, lon):
    lon = ((lon + 180) % 360) - 180
    return any(abs(lat - cla) < 1.2 and abs(lon - clo) < 1.2 for cla, clo in CANALS)


def seg_land_hit(a, b, step_km=12.0):
    """Eerste landpunt op segment a->b (lat,lon), kanaal-passages uitgezonderd."""
    seg = gc_km({"lat": a[0], "lon": a[1]}, {"lat": b[0], "lon": b[1]})
    n = max(1, math.ceil(seg / step_km))
    for k in range(1, n):
        t = k / n
        lat = a[0] + (b[0] - a[0]) * t
        dl = b[1] - a[1]
        lon = a[1] + dl * t
        if is_land(lat, lon) and not near_canal(lat, lon):
            return (lat, lon)
    return None


def bearing(a, b):
    la1, la2 = math.radians(a[0]), math.radians(b[0])
    dlo = math.radians(b[1] - a[1])
    return math.degrees(math.atan2(
        math.sin(dlo) * math.cos(la2),
        math.cos(la1) * math.sin(la2) - math.sin(la1) * math.cos(la2) * math.cos(dlo)))


def dezigzag(pts, limit_deg=100, max_chord_km=450):
    """Verwijder zigzag-punten: bocht > limit en de kortsluiting blijft op water."""
    pts = list(pts)
    removed = 0
    changed = True
    while changed:
        changed = False
        for i in range(1, len(pts) - 1):
            d = abs(bearing(pts[i - 1], pts[i]) - bearing(pts[i], pts[i + 1]))
            if d > 180:
                d = 360 - d
            if d <= limit_deg:
                continue
            chord = gc_km({"lat": pts[i - 1][0], "lon": pts[i - 1][1]},
                          {"lat": pts[i + 1][0], "lon": pts[i + 1][1]})
            if chord > max_chord_km:
                continue
            if seg_land_hit(pts[i - 1], pts[i + 1]) is None:
                del pts[i]
                removed += 1
                changed = True
                break
    return pts, removed


def detour_around_land(a, b, cell=0.1):
    """Lokale A* over een waterraster in de bbox van het segment (+2 graden)."""
    lo_la, hi_la = sorted((a[0], b[0]))
    lo_lo, hi_lo = sorted((a[1], b[1]))
    lo_la -= 2; hi_la += 2; lo_lo -= 2; hi_lo += 2
    if hi_lo - lo_lo > 180:
        return None  # antimeridiaan-bbox: niet nodig voor de huidige gevallen
    nx = int((hi_lo - lo_lo) / cell) + 1
    ny = int((hi_la - lo_la) / cell) + 1
    water = [[not is_land(lo_la + y * cell, lo_lo + x * cell) or
              near_canal(lo_la + y * cell, lo_lo + x * cell)
              for x in range(nx)] for y in range(ny)]
    # kustbuffer: cellen die aan land grenzen ook dichtzetten, anders scheert de
    # omleiding zó strak langs de kust dat het getekende koord alsnog land raakt
    buffered = [row[:] for row in water]
    for y in range(ny):
        for x in range(nx):
            if not water[y][x]:
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        yy, xx = y + dy, x + dx
                        if 0 <= yy < ny and 0 <= xx < nx:
                            buffered[yy][xx] = False
    # als de buffer start/doel afsnijdt (haven in nauw water) val terug op kaal
    water_buf = buffered
    water = water_buf if any(any(r) for r in water_buf) else water

    def cellof(p):
        return (min(ny - 1, max(0, round((p[0] - lo_la) / cell))),
                min(nx - 1, max(0, round((p[1] - lo_lo) / cell))))

    def snap(c):  # dichtstbijzijnde watercel (haven kan op de kustcel vallen)
        y0, x0 = c
        for r in range(0, 15):
            for dy in range(-r, r + 1):
                for dx in range(-r, r + 1):
                    y, x = y0 + dy, x0 + dx
                    if 0 <= y < ny and 0 <= x < nx and water[y][x]:
                        return (y, x)
        return None

    start, goal = snap(cellof(a)), snap(cellof(b))
    if not start or not goal:
        return None
    coslat = math.cos(math.radians((a[0] + b[0]) / 2))

    def h(c):
        return math.hypot((c[0] - goal[0]), (c[1] - goal[1]) * coslat)

    openq = [(h(start), 0.0, start, None)]
    came, gbest = {}, {start: 0.0}
    while openq:
        _f, g, cur, par = heapq.heappop(openq)
        if cur in came:
            continue
        came[cur] = par
        if cur == goal:
            break
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if not dy and not dx:
                    continue
                y, x = cur[0] + dy, cur[1] + dx
                if not (0 <= y < ny and 0 <= x < nx) or not water[y][x]:
                    continue
                ng = g + math.hypot(dy, dx * coslat)
                if ng < gbest.get((y, x), 1e18):
                    gbest[(y, x)] = ng
                    heapq.heappush(openq, (ng + h((y, x)), ng, (y, x), cur))
    if goal not in came:
        return None
    path, c = [], goal
    while c is not None:
        path.append(c)
        c = came[c]
    path.reverse()
    # om-en-om decimeren en terug naar lat/lon; endpoints laat de aanroeper staan
    return [[lo_la + y * cell, lo_lo + x * cell] for y, x in path[1:-1:2]]


def fix_land_crossings(pts):
    """Vervang segmenten die land snijden door een lokale wateromleiding."""
    fixed = 0
    out = [pts[0]]
    for i in range(len(pts) - 1):
        a, b = pts[i], pts[i + 1]
        if seg_land_hit(a, b) is not None:
            det = detour_around_land(a, b)
            if det:
                out.extend(det)
                fixed += 1
        out.append(b)
    return out, fixed


def _cross_track_km(p, a, b):
    """Loodrechte afstand van p tot de lijn a->b (vlakke benadering, lokaal genoeg)."""
    coslat = math.cos(math.radians(p[0]))
    ax, ay = (a[1] - p[1]) * coslat, a[0] - p[0]
    bx, by = (b[1] - p[1]) * coslat, b[0] - p[0]
    dx, dy = bx - ax, by - ay
    den = math.hypot(dx, dy)
    if den < 1e-9:
        return math.hypot(ax, ay) * 111.2
    return abs(ax * dy - ay * dx) / den * 111.2


def seg_clearance_ok(a, b, min_km, step_km=15.0):
    """Blijft het segment a->b overal minstens min_km van land? Loodrecht geprobed.

    Nodig omdat vereenvoudigen in SMAL water de baanbreedtes sloopt: de lane-klem
    (tools/lane_widths.js + util.js) leest de vrije ruimte per punt, en in de
    Seto-binnenzee waren juist die punten de rem op de waaier. Weghalen liet de
    banen weer over Japan bollen (8 -> 195 landtreffers). In ruim water is er
    niets te verliezen; daar mag getrapte rommel wél weg.
    """
    seg = gc_km({"lat": a[0], "lon": a[1]}, {"lat": b[0], "lon": b[1]})
    n = max(1, math.ceil(seg / step_km))
    for k in range(n + 1):
        t = k / n
        lat = a[0] + (b[0] - a[0]) * t
        lon = a[1] + (b[1] - a[1]) * t
        coslat = max(0.05, math.cos(math.radians(lat)))
        for ang in range(0, 360, 45):
            r = math.radians(ang)
            dlat = math.cos(r) * (min_km / 111.2)
            dlon = math.sin(r) * (min_km / 111.2) / coslat
            if is_land(lat + dlat, lon + dlon) and not near_canal(lat + dlat, lon + dlon):
                return False
    return True


def simplify_water(pts, tol_km=12.0, max_chord_km=400.0, min_clearance_km=0.0):
    """Ruim TRAPJES op: punten die nauwelijks van de rechte lijn afwijken en
    waarvan de kortsluiting over water blijft.

    Waarom: `detour_around_land` legt een A* over een 0,1-graden raster, en zo'n
    raster-pad bestaat uit korte stapjes met hoekjes van 45 graden. Bij Isla
    Guadalupe (Baja) deelden ZEVEN corridors hetzelfde trapje — alle zeven
    wiebelden identiek, de paden liepen door elkaar en de voyage-bolletjes
    schokten. Idem bij de Vogelkop (Papoea) en de Straat van Malakka.

    Een punt gaat er alleen uit als (1) het < tol_km van de lijn buur->buur ligt
    (dus géén echte koerswijziging — die blijven staan), (2) de kortsluiting geen
    land raakt, en (3) de kortsluiting lokaal blijft. Zelfde bewijslast als
    `dezigzag`: nooit blind gladstrijken, altijd tegen de landpolygonen toetsen.
    """
    pts = list(pts)
    removed = 0
    changed = True
    while changed:
        changed = False
        i = 1
        while i < len(pts) - 1:
            a, p, b = pts[i - 1], pts[i], pts[i + 1]
            chord = gc_km({"lat": a[0], "lon": a[1]}, {"lat": b[0], "lon": b[1]})
            # FIJN bemonsteren: de standaard 12 km-stap gaf op een segment van
            # 15 km maar één monsterpunt, en daar glipten de Channel Islands
            # (34,01/-119,6) tussendoor — de kortsluiting werd goedgekeurd en
            # sneed alsnog land. Minstens ~10 monsters per kortsluiting.
            probe_km = min(3.0, max(0.5, chord / 10.0))
            if (chord <= max_chord_km
                    and _cross_track_km(p, a, b) < tol_km
                    and seg_land_hit(a, b, step_km=probe_km) is None
                    and (min_clearance_km <= 0
                         or seg_clearance_ok(a, b, min_clearance_km))):
                del pts[i]
                removed += 1
                changed = True
            else:
                i += 1
    return pts, removed


def gc_km(a, b):
    lo1, la1, lo2, la2 = map(math.radians, [a["lon"], a["lat"], b["lon"], b["lat"]])
    return 6371 * 2 * math.asin(math.sqrt(
        math.sin((la2 - la1) / 2) ** 2
        + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2))


# ---------------------------------------------------------- ANTIPODALE STABILISATIE
# Bij een bijna-antipodaal havenpaar is de grote cirkel wiskundig ONBEPAALD: noordom
# en zuidom zijn even lang, en MARNET's Dijkstra kiest dan willekeurig. Gevolg vóór
# deze fix: 7 van de 8 trans-Pacific koper-corridors kruisten de datumgrens op 50°N
# (de echte, drukke noordelijke lane) maar Valparaíso->Ningbo dook naar 20°Z — dwars
# door de lege zuidelijke Stille Oceaan, terwijl Valparaíso maar ~1.000 km onder
# Antofagasta ligt. Geen varensreden, puur een grafiek-artefact.
#
# Regel: is het paar bijna-antipodaal ÉN trans-Pacific ÉN koos MARNET het zuidelijk
# halfrond, dan bakken we in twee hops via wp-pac-noord (44°N/175°O) — dezelfde
# "stabilisator van een onbepaalde geodeet" die _chokepoints.js al beschrijft, maar
# consistent noordelijk. Stabiele paren blijven onaangeroerd: MARNET beslist.
HALF_CIRCUM_KM = 20015.0
ANTIPODAL_FRAC = 0.85          # >85% van een halve aardomtrek = onbepaald genoeg
# Het stabilisatiepunt moet op een DICHT stuk MARNET liggen, niet in leeg water.
# Eerste poging was 50°N/180° (datumgrens): dat leverde een kaarsrechte diagonaal
# door de open Stille Oceaan (-80/-30, -85/-25, -90/-20, ... exact 5° per stap) —
# één artefact ingeruild voor een ander. Reden: rond de datumgrens heeft MARNET
# nauwelijks knopen, dus interpoleert searoute een rechte lijn.
#
# Dit punt ligt vóór de Peruaanse kust, midden op de lane die de zustercorridors
# (Antofagasta/Callao/Matarani -> Azië) werkelijk varen. Daardoor voegt Valparaíso
# zich ín die lane: vanaf hier zijn de punten identiek aan de zusterroute
# (-84,7/-4,1 · -87,8/-0,2 · -89,6/2,1 · -93,5/6,4 · -97,5/10,2 ...) — onregelmatig
# gespatieerd, dus échte netwerkknopen in plaats van interpolatie.
#
# Kosten: +5,8% boven de grote cirkel (zuidom was +2,5%). Bewust betaald — vorm
# gaat hier boven lengte: dit is de route die schepen varen.
PACIFIC_LANE = {"lat": -10.00, "lon": -80.00}


def _crosses_pacific(a, b):
    """Amerikaanse westkust <-> Oost-Azië (het paar dat de datumgrens moet kruisen)."""
    return (a["lon"] < -60 and b["lon"] > 100) or (b["lon"] < -60 and a["lon"] > 100)


def _lat_at_dateline(pts):
    """Breedtegraad waar de polyline de datumgrens passeert (None = passeert niet)."""
    best, lat = 1e9, None
    for la, lo in pts:
        d = abs(abs(lo) - 180)
        if d < best:
            best, lat = d, la
    return lat if best < 5 else None


def _run(a, b):
    return sr.searoute([a["lon"], a["lat"]], [b["lon"], b["lat"]], units="km",
                       append_orig_dest=True, return_passages=True)


def bake(corridor):
    """searoute over één corridor -> (polyline, passages, km, zigzagsWeg, landFixes) of None.

    Het ruwe MARNET-pad krijgt twee reparaties (zie LANDMASKER hierboven),
    beide gevalideerd tegen de landpolygonen — geen blinde smoothing."""
    a, b = corridor["a"], corridor["b"]
    r = _run(a, b)
    km = r["properties"]["length"]
    if not km or km <= 0:
        return None
    raw = [[lat, lon] for lon, lat in r["geometry"]["coordinates"]]

    # antipodale stabilisatie: alleen als MARNET zuidom koos op een onbepaald paar
    if (_crosses_pacific(a, b)
            and gc_km(a, b) > ANTIPODAL_FRAC * HALF_CIRCUM_KM):
        dl = _lat_at_dateline(raw)
        if dl is not None and dl < 0:
            r1, r2 = _run(a, PACIFIC_LANE), _run(PACIFIC_LANE, b)
            km1 = r1["properties"]["length"]
            km2 = r2["properties"]["length"]
            if km1 and km2 and km1 > 0 and km2 > 0:
                p1 = [[la, lo] for lo, la in r1["geometry"]["coordinates"]]
                p2 = [[la, lo] for lo, la in r2["geometry"]["coordinates"]]
                raw = p1 + p2[1:]          # knooppunt niet dubbel
                km = km1 + km2
                r = {"properties": {"traversed_passages":
                     sorted(set((r1["properties"].get("traversed_passages") or [])
                                + (r2["properties"].get("traversed_passages") or [])))}}
                print(f"  noord-gestabiliseerd: {a['id']} -> {b['id']}"
                      f"  (datumgrens {dl:.0f}° -> zusterlane via Peru)")
    raw, zigzags = dezigzag(raw)
    raw, landfixes = fix_land_crossings(raw)
    raw, smoothed = simplify_water(raw)
    pts, seen = [], None
    for lat, lon in raw:
        p = [round(lat, PRECISION), round(lon, PRECISION)]
        if p != seen:
            pts.append(p)
            seen = p
    passages = sorted(r["properties"].get("traversed_passages") or [])
    return pts, passages, km, zigzags, landfixes, smoothed


def main():
    resources = sys.argv[1:]
    raw = subprocess.run(
        ["node", str(ROOT / "tools" / "extract_corridors.js"), *resources],
        capture_output=True, text=True, check=True).stdout
    corridors = json.loads(raw)
    print(f"corridors te bakken: {len(corridors)}"
          f" ({', '.join(resources) if resources else 'alle grondstoffen'})")

    entries, failures, total_pts = [], [], 0
    tot_zig, tot_fix, tot_smooth = 0, 0, 0
    for c in corridors:
        try:
            res = bake(c)
        except Exception as e:  # searoute kan ook exceptions gooien (punt buiten net)
            res = None
            c["err"] = str(e)
        if res is None:
            failures.append(c)
            continue
        pts, passages, km, zigzags, landfixes, smoothed = res
        total_pts += len(pts)
        tot_zig += zigzags
        tot_fix += landfixes
        tot_smooth += smoothed
        if zigzags or landfixes or smoothed:
            print(f"  gerepareerd: {c['a']['id']} -> {c['b']['id']}"
                  f"  ({zigzags} zigzag-punten weg, {landfixes} land-omleidingen,"
                  f" {smoothed} trapjes glad)")
        ratio = km / max(gc_km(c["a"], c["b"]), 1e-9)
        entries.append((c["key"], pts, passages, c, round(km), round(ratio, 3)))
    if tot_zig or tot_fix or tot_smooth:
        print(f"totaal gerepareerd: {tot_zig} zigzag-punten, {tot_fix} land-omleidingen,"
              f" {tot_smooth} trapjes glad")

    # FOUTEN HARD (spec §4): niet stil doorgaan.
    if failures:
        print(f"\nBUILD FAALT — {len(failures)} corridor(s) niet routeerbaar:")
        for c in failures:
            print(f"  {c['a']['id']} ({c['a']['lat']},{c['a']['lon']}) -> "
                  f"{c['b']['id']} ({c['b']['lat']},{c['b']['lon']})"
                  + (f"  [{c['err']}]" if c.get("err") else ""))
        sys.exit(1)

    # sanity-checks (build-standalone.py-stijl)
    assert entries, "sanity: 0 corridors gebakken"
    suspects = [(k, c, r) for k, _p, pas, c, _km, r in entries
                if r > 1.15 and not pas]
    if suspects:
        print(f"\nLET OP — {len(suspects)} corridor(s) >15% boven grote-cirkel "
              f"zonder doorgang (spec §9, handmatig beoordelen):")
        for k, c, r in suspects:
            print(f"  {c['a']['id']} -> {c['b']['id']}  ratio {r}")

    entries.sort(key=lambda e: e[0])  # determinisme
    lines = [
        "// _searoutes.js — GEGENEREERD door tools/bake_searoutes.py — NIET met de hand bewerken.",
        "//",
        "// Corridor-cache: echte zeeroutes over MARNET (searoute), gebakken at build-time.",
        "// Sleutel: \"lat,lon|lat,lon\" (3 decimalen, paar gesorteerd — richtingsonafhankelijk).",
        "// Waarde: { pts: [[lat,lon],...] van a naar b zoals geëxtraheerd,",
        "//           passages: doorgangen die de route passeert (traversed_passages) }.",
        "// Zie design/zeeroutes.md. flows.js keert de polyline om als de leg andersom loopt.",
        "const SEAROUTES = {",
    ]
    for key, pts, passages, c, km, ratio in entries:
        pts_js = ",".join(f"[{la},{lo}]" for la, lo in pts)
        pas_js = ",".join(f'"{p}"' for p in passages)
        lines.append(
            f'  "{key}": {{ pts: [{pts_js}], passages: [{pas_js}] }},'
            f' // {c["a"]["id"]} -> {c["b"]["id"]}  {km} km  x{ratio}')
    lines.append("};")
    lines.append("")
    lines.append("// Grondstoffen die volledig op de cache draaien (ontbrekende corridor = kapot,")
    lines.append("// nooit stil terugvallen op A*). Andere grondstoffen gebruiken nog Routing.sea.")
    baked = sorted(set(r for _k, _p, _pas, c, _km, _r in entries for r in c["resources"]))
    lines.append("const SEAROUTES_BAKED = { " + ", ".join(f'"{r}": true' for r in baked) + " };")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    kb = OUT.stat().st_size / 1024
    print(f"\nOK: {len(entries)} corridors, {total_pts} punten "
          f"-> {OUT.name} ({kb:.0f} KB)")
    print(f"gedekte grondstoffen: {', '.join(baked)}")


if __name__ == "__main__":
    main()
