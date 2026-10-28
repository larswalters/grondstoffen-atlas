#!/usr/bin/env python3
"""maak_leidingbeen_gas_portofmorgan_manhattan.py - leidingbenen van gas-portofmorgan-manhattan.

Northern Border Pipeline (man_made=pipeline, substance gas, 42 inch): vaste lijst OSM-ways, via Overpass
(`way(id:...); out geom;`, met retries) gestikt tot drie LineStrings. Ways die niet op de hoofdleiding
liggen (Canadese stompen, residue lines, Glen Ullin-aftakking, nul-lengte-way) blijven weg.
Schrijft drie FeatureCollections naar v2/build-cache/ais/graaf/:
  gas-portofmorgan-manhattan-leiding-nb1.geojson  Port of Morgan (MT) -> Iowa 41.8525,-92.4312  (23 ways)
  gas-portofmorgan-manhattan-leiding-nb2.geojson  Illinois-Iowa 41.6163,-90.9266 -> 41.4672,-89.1659  (way 1025655071)
  gas-portofmorgan-manhattan-leiding-nb3.geojson  41.4738,-88.5966 -> Manhattan 41.4446,-87.9916  (2 ways)
Bron: OpenStreetMap-bijdragers (ODbL).

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_portofmorgan_manhattan.py
"""
import json
import math
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UITMAP = os.path.join(WORTEL, "build-cache", "ais", "graaf")
NB1 = [468644651, 468644674, 468644681, 468644695, 9726026, 160037547, 468644621, 451340059, 451339998,
       451339993, 451340022, 451339986, 1567324911, 451339995, 18151332, 468915657, 468915655, 468915634,
       468915631, 468915622, 468915615, 468915614, 468922520]
NB2 = [1025655071]
NB3 = [1432429480, 1432558933]
SERVERS = ["https://overpass-api.de/api/interpreter", "https://overpass.private.coffee/api/interpreter"]


def hv(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))


def haal(ids):
    q = "[out:json][timeout:120];way(id:%s);out geom;" % ",".join(map(str, ids))
    data = urllib.parse.urlencode({"data": q}).encode()
    for poging in range(8):
        for s in SERVERS:
            try:
                req = urllib.request.Request(s, data=data, headers={"User-Agent": "grondstoffen-atlas/1.0"})
                d = json.loads(urllib.request.urlopen(req, timeout=180).read())
                ways = {e["id"]: [(p["lon"], p["lat"]) for p in e["geometry"]] for e in d["elements"] if e["type"] == "way"}
                if all(i in ways for i in ids):
                    return ways
            except Exception as e:  # noqa
                print("  overpass-fout", s, str(e)[:80], file=sys.stderr)
        time.sleep(10 * (poging + 1))
    raise SystemExit("Overpass onbereikbaar of ways ontbreken")


def stik(ids, ways):
    pts = []
    for w in ids:
        p = ways[w]
        if pts:
            if hv(pts[-1], p[0]) > hv(pts[-1], p[-1]):
                p = p[::-1]
            naad = hv(pts[-1], p[0]) * 1000
            if naad > 100:
                print(f"  way {w}: naad {naad:.0f} m", file=sys.stderr)
            if naad < 0.5:
                p = p[1:]
        pts += p
    return pts


def schrijf(pts, naam, bestand):
    km = sum(hv(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature", "properties": {"name": naam},
        "geometry": {"type": "LineString", "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
    os.makedirs(UITMAP, exist_ok=True)
    with open(os.path.join(UITMAP, bestand), "w", encoding="utf-8") as f:
        json.dump(fc, f)
    print(f"{bestand}: {len(pts)} punten, {km:.1f} km; begin {pts[0][1]:.4f},{pts[0][0]:.4f}; eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}")
    return km


def main():
    ways = haal(NB1 + NB2 + NB3)
    schrijf(stik(NB1, ways), "Northern Border Pipeline, Port of Morgan (MT) tot Iowa (OSM-ways, 23 stuks)",
            "gas-portofmorgan-manhattan-leiding-nb1.geojson")
    schrijf(stik(NB2, ways), "Northern Border Pipeline, Chicago Project (OSM-way 1025655071)",
            "gas-portofmorgan-manhattan-leiding-nb2.geojson")
    schrijf(stik(NB3, ways), "Northern Border Mainline tot Manhattan (OSM-ways 1432429480 + 1432558933)",
            "gas-portofmorgan-manhattan-leiding-nb3.geojson")


if __name__ == "__main__":
    main()
