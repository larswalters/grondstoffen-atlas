#!/usr/bin/env python3
"""maak_leidingbeen_gas_nybro_goleniow.py - drie leidingbenen van gas-nybro-goleniow (Baltic Pipe).

Haalt de OSM-ways (man_made=pipeline, substance=gas; ODbL) via de OSM-API, stikt ze per been in
vaste volgorde (elke way zo gedraaid dat zijn begin het dichtst bij het vorige eind ligt) en
schrijft per been een FeatureCollection met een LineString naar v2/build-cache/ais/graaf/:
  gas-nybro-goleniow-leiding-dk.geojson        Nybro -> Faxe (9 ways, ~280 km)
  gas-nybro-goleniow-leiding-offshore.geojson  Faxe -> Pogorzelica (1 way 1068926050, ~272,7 km, omgedraaid)
  gas-nybro-goleniow-leiding-pl.geojson        Pogorzelica -> Goleniow (9 ways, ~83 km)

Draaien:  PYTHONIOENCODING=utf-8 python v2/tools/maak_leidingbeen_gas_nybro_goleniow.py
"""
import json
import math
import os
import urllib.request
import xml.etree.ElementTree as ET

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf")

BENEN = {
    "dk": ("Baltic Pipe Denemarken, Nybro -> Faxe-landing (OSM-ways, Energinet)",
           [1362960758, 1392067292, 1204845861, 1095495854, 1392191334, 1392191337,
            1392191339, 1055345076, 1192369246]),
    "offshore": ("Baltic Pipe offshore, Faxe -> Pogorzelica (OSM way 1068926050, Gaz-System)",
                 [1068926050]),
    "pl": ("Baltic Pipe Polen, Pogorzelica -> Goleniow (OSM-ways, Gaz-System)",
           [978208595, 1527555072, 976104602, 976104601, 973327088, 979871638, 979871639,
            979871637, 860469159]),
}
# offshore-way loopt in OSM van Pogorzelica naar Faxe; het been loopt de andere kant op
OMDRAAIEN = {"offshore"}


def hv(a, b):
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))


def lengte(p):
    return sum(hv(p[i], p[i + 1]) for i in range(len(p) - 1))


def haal(way):
    url = f"https://api.openstreetmap.org/api/0.6/way/{way}/full"
    req = urllib.request.Request(url, headers={"User-Agent": "grondstoffen-atlas/1.0"})
    root = ET.fromstring(urllib.request.urlopen(req, timeout=90).read())
    nodes = {n.get("id"): (float(n.get("lon")), float(n.get("lat"))) for n in root.findall("node")}
    return [nodes[n.get("ref")] for n in root.find("way").findall("nd")]


def main():
    os.makedirs(UIT, exist_ok=True)
    for sleutel, (naam, ways) in BENEN.items():
        pts, naden = [], []
        for w in ways:
            p = haal(w)
            if sleutel in OMDRAAIEN:
                p = p[::-1]
            elif pts and hv(pts[-1], p[0]) > hv(pts[-1], p[-1]):
                p = p[::-1]
            if pts:
                naden.append(round(hv(pts[-1], p[0]), 2))
            pts.extend(p)
        fc = {"type": "FeatureCollection", "features": [{
            "type": "Feature", "properties": {"name": naam},
            "geometry": {"type": "LineString",
                         "coordinates": [[round(x, 5), round(y, 5)] for x, y in pts]}}]}
        pad = os.path.join(UIT, f"gas-nybro-goleniow-leiding-{sleutel}.geojson")
        with open(pad, "w", encoding="utf-8") as f:
            json.dump(fc, f)
        print(f"{sleutel}: {len(pts)} punten, {lengte(pts):.1f} km, naden {naden}; "
              f"begin lat,lon {pts[0][1]:.4f},{pts[0][0]:.4f}; eind {pts[-1][1]:.4f},{pts[-1][0]:.4f}\n  -> {pad}")


if __name__ == "__main__":
    main()
