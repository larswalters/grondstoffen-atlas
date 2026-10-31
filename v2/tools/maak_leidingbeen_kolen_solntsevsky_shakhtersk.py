#!/usr/bin/env python3
"""maak_leidingbeen_kolen_solntsevsky_shakhtersk.py — b1 van kolen-solntsevsky-shakhtersk.

Brief v2/design/routebrieven/kolen-solntsevsky-shakhtersk.md: de kolenband "Ugolny konveyer" (Vostochnaya
Gornorudnaya Kompaniya, Solntsevsky -> Shakhtersk) staat in OSM als man_made=goods_conveyor. Dit script haalt
de ways per id via de OSM-API (way/<id>/full; Overpass was onbereikbaar), rijgt ze over gedeelde of bijna
gedeelde eindknopen aaneen en schrijft een FeatureCollection met een LineString.

    python v2/tools/maak_leidingbeen_kolen_solntsevsky_shakhtersk.py [--schrijf] [--met-opslag]
"""
import argparse, json, math, os, urllib.request

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "kolen-solntsevsky-shakhtersk-leiding-band.geojson")
HOOFD = [947629124, 1409824697, 1190064790, 947629125, 1409824707]
OPSLAG = [1409824738, 1409824739]
PIER = 1409824738            # band over het opslagterrein/de pier naar de scheepsbelader (tweede band 1409824739 loopt parallel, niet gebruikt)
UIT_PIER = os.path.join(WORTEL, "build-cache", "ais", "graaf", "kolen-solntsevsky-shakhtersk-leiding-pier.geojson")
R = 6371.0088


def gc(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[1], a[0], b[1], b[0]))
    return R * math.acos(min(1, math.sin(la1) * math.sin(la2) + math.cos(la1) * math.cos(la2) * math.cos(lo1 - lo2)))


def haal(wid):
    url = f"https://api.openstreetmap.org/api/0.6/way/{wid}/full.json"
    req = urllib.request.Request(url, headers={"User-Agent": "grondstoffen-atlas/1.0 (routebrief leidingbeen)"})
    d = json.load(urllib.request.urlopen(req, timeout=90))
    nodes = {e["id"]: (e["lon"], e["lat"]) for e in d["elements"] if e["type"] == "node"}
    w = [e for e in d["elements"] if e["type"] == "way"][0]
    return w["tags"], [list(nodes[n]) for n in w["nodes"]]


def rijg(ids):
    delen = {}
    for i in ids:
        t, c = haal(i)
        delen[i] = c
        print(i, t.get("name"), t.get("man_made"), len(c), "punten", f"{sum(gc(c[k], c[k+1]) for k in range(len(c)-1)):.3f} km", c[0], c[-1])
    # greedy: start bij het uiteinde met de laagste lat (zuid = bandbegin Solntsevsky)
    rest = dict(delen)
    start = min(rest, key=lambda i: min(rest[i][0][1], rest[i][-1][1]))
    c = rest.pop(start)
    if c[0][1] > c[-1][1]:
        c = c[::-1]
    volg = [start]; naden = []
    while rest:
        eind = c[-1]
        best = None
        for i, d in rest.items():
            for omk in (False, True):
                dd = d[::-1] if omk else d
                af = gc(eind, dd[0])
                if best is None or af < best[0]:
                    best = (af, i, dd)
        af, i, dd = best
        naden.append((i, round(af * 1000, 1)))
        c = c + dd if af > 0.0005 else c + dd[1:]
        rest.pop(i); volg.append(i)
    return c, volg, naden


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    ap.add_argument("--met-opslag", action="store_true")
    ap.add_argument("--pier", action="store_true", help="schrijf ook de pierband (way 1409824738) als eigen geojson")
    a = ap.parse_args()
    if a.pier:
        t, pc = haal(PIER)
        pkm = sum(gc(pc[k], pc[k + 1]) for k in range(len(pc) - 1))
        print(f"pierband way {PIER}: {len(pc)} punten, {pkm:.3f} km; kop {pc[0]} eind {pc[-1]} (lon,lat)")
        if a.schrijf:
            json.dump({"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {
                "name": "Ugolny konveyer - pierband naar scheepsbelader (OSM way %d)" % PIER, "ways": [PIER]},
                "geometry": {"type": "LineString", "coordinates": pc}}]}, open(UIT_PIER, "w", encoding="utf-8"))
            print("geschreven:", UIT_PIER)
    c, volg, naden = rijg(HOOFD + (OPSLAG if a.met_opslag else []))
    km = sum(gc(c[i], c[i + 1]) for i in range(len(c) - 1))
    print(f"{len(volg)} ways {volg}, {len(c)} punten, {km:.3f} km; naden (m) {naden}; kop {c[0]} (lon,lat) eind {c[-1]}")
    if a.schrijf:
        fc = {"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {
            "name": "Ugolny konveyer (OSM goods_conveyor, %d ways)" % len(volg), "ways": volg},
            "geometry": {"type": "LineString", "coordinates": c}}]}
        json.dump(fc, open(UIT, "w", encoding="utf-8"))
        print("geschreven:", UIT)


if __name__ == "__main__":
    main()
