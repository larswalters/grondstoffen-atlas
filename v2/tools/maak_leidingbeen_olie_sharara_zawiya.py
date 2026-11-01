#!/usr/bin/env python3
"""maak_leidingbeen_olie_sharara_zawiya.py - b1 van olie-sharara-zawiya.

Brief: v2/design/routebrieven/olie-sharara-zawiya.md (b1). Sharara-Zawiya-leiding (30 inch, 1998,
Akakus Oil Operations): het gekarteerde deel van het Sharara-veld tot het OSM-uiteinde bij Zintan,
drie OSM-ways (man_made=pipeline, substance=oil) die per way-id uit de OSM-API komen
(Libie heeft geen Geofabrik-extract), in reisvolgorde gestikt:
    273080145  (497,0 km, Sharara -> noord, omgekeerd)  +
    1109123294 (0,1 km, bovengronds stukje bij het Hamada-stelsel, omgekeerd)  +
    102162888  (125,5 km, richting Zintan, omgekeerd).
Het laatste stuk (Zintan-uiteinde -> Zawiya, ~100 km hemelsbreed) staat niet in OSM en wordt in
bak_stromen.sh een stippel.

Uitvoer: v2/build-cache/ais/graaf/olie-sharara-zawiya-leiding-sharara-zintan.geojson
(FeatureCollection, een LineString, [lon,lat]).

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_olie_sharara_zawiya.py
"""
import json
import math
import os
import urllib.request

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "olie-sharara-zawiya-leiding-sharara-zintan.geojson")
# in reisvolgorde Sharara -> Zintan; de OSM-ways zelf lopen de andere kant op (noord -> zuid)
WAYS = [273080145, 1109123294, 102162888]
R = 6371.0088


def hv(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def haal(way):
    url = f"https://api.openstreetmap.org/api/0.6/way/{way}/full.json"
    req = urllib.request.Request(url, headers={"User-Agent": "grondstoffen-atlas/1.0"})
    d = json.loads(urllib.request.urlopen(req, timeout=90).read().decode("utf-8"))
    nodes = {e["id"]: (e["lon"], e["lat"]) for e in d["elements"] if e["type"] == "node"}
    w = [e for e in d["elements"] if e["type"] == "way"][0]
    tags = w.get("tags", {})
    assert tags.get("man_made") == "pipeline", (way, tags)
    return [nodes[n] for n in w["nodes"]], tags


def main():
    pts, naden = [], []
    for w in WAYS:
        p, tags = haal(w)
        # kies de richting zodat het begin het dichtst bij het eind van het vorige stuk ligt
        if pts:
            if hv(pts[-1], p[0]) > hv(pts[-1], p[-1]):
                p = p[::-1]
        else:
            # eerste way: begin moet het zuidelijkste punt (Sharara) zijn
            if p[0][1] > p[-1][1]:
                p = p[::-1]
        if pts:
            naden.append(round(hv(pts[-1], p[0]), 3))
            if naden[-1] < 0.001:
                p = p[1:]
        print(f"  way {w}: {len(p)} punten, substance={tags.get('substance')}, location={tags.get('location')}")
        pts.extend(p)
    km = sum(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"name": "Sharara-Zawiya-leiding, Sharara -> Zintan-uiteinde (OSM ways 273080145 + 1109123294 + 102162888)"},
        "geometry": {"type": "LineString", "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(fc, f)
    print(f"{len(pts)} punten, {km:.1f} km, naden {naden}; begin lat,lon {pts[0][1]:.4f},{pts[0][0]:.4f}; "
          f"eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n  -> {UIT}")


if __name__ == "__main__":
    main()
