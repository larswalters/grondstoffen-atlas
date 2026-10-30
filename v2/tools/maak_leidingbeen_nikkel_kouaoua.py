#!/usr/bin/env python3
"""maak_leidingbeen_nikkel_kouaoua.py — b1 van nikkel-kouaoua-laadkade.

Brief v2/design/routebrieven/nikkel-kouaoua-laadkade.md: de ertsband "La Serpentine de Kouaoua" (SLN, mijn
Mea -> kustlader "Chargement en Mer") staat in OSM als 20 aaneensluitende ways met man_made=goods_conveyor
(18x "La Serpentine de Kouaoua" + 2x "Chargement en Mer", railway=rail). Dit script haalt de ways via de
OSM-API (/map, bbox; Overpass was onbetrouwbaar), rijgt ze over gedeelde nodes aaneen tussen de twee
eindknopen en schrijft een FeatureCollection met een LineString.

    python v2/tools/maak_leidingbeen_nikkel_kouaoua.py --schrijf
"""
import argparse, json, math, os, urllib.request
from collections import defaultdict

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "nikkel-kouaoua-laadkade-leiding-serpentine.geojson")
BBOX = "165.76,-21.46,165.84,-21.395"
R = 6371.0088


def gc(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[1], a[0], b[1], b[0]))
    return R * math.acos(min(1, math.sin(la1) * math.sin(la2) + math.cos(la1) * math.cos(la2) * math.cos(lo1 - lo2)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    a = ap.parse_args()
    url = f"https://api.openstreetmap.org/api/0.6/map.json?bbox={BBOX}"
    req = urllib.request.Request(url, headers={"User-Agent": "grondstoffen-atlas/1.0 (routebrief leidingbeen)"})
    d = json.load(urllib.request.urlopen(req, timeout=90))
    nodes = {e["id"]: (e["lon"], e["lat"]) for e in d["elements"] if e["type"] == "node"}
    ways = {e["id"]: e for e in d["elements"] if e["type"] == "way" and e.get("tags", {}).get("man_made") == "goods_conveyor"}
    adj = defaultdict(list)
    for wid, w in ways.items():
        for x, y in zip(w["nodes"], w["nodes"][1:]):
            adj[x].append((y, wid)); adj[y].append((x, wid))
    eind = [n for n, l in adj.items() if len(l) == 1]
    assert len(eind) == 2, f"verwacht 1 aaneengesloten keten, eindknopen: {eind}"
    kop = min(eind, key=lambda n: nodes[n][1])          # zuidwestelijke eindknoop = Mea (lat -21.4557)
    kop = [n for n in eind if nodes[n][0] < 165.8][0]
    pad, gebruikt, huidig, vorig = [kop], [], kop, None
    while True:
        opties = [(n, w) for n, w in adj[huidig] if n != vorig]
        if not opties:
            break
        n, w = opties[0]
        if w not in gebruikt:
            gebruikt.append(w)
        vorig, huidig = huidig, n
        pad.append(n)
    assert len(set(gebruikt)) == len(ways), (len(set(gebruikt)), len(ways))
    c = [list(nodes[n]) for n in pad]
    km = sum(gc(c[i], c[i + 1]) for i in range(len(c) - 1))
    print(f"{len(ways)} ways, {len(c)} punten, {km:.3f} km; kop {c[0]} (lon,lat) eind {c[-1]}; way-volgorde {gebruikt}")
    if a.schrijf:
        fc = {"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {
            "name": "La Serpentine de Kouaoua + Chargement en Mer (OSM goods_conveyor, 20 ways)", "ways": gebruikt},
            "geometry": {"type": "LineString", "coordinates": c}}]}
        json.dump(fc, open(UIT, "w", encoding="utf-8"))
        print("geschreven:", UIT)


if __name__ == "__main__":
    main()
