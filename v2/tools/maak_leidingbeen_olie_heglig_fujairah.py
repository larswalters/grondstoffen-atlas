#!/usr/bin/env python3
"""maak_leidingbeen_olie_heglig_fujairah.py - leidingbeen b1 van olie-heglig-fujairah.

OSM-way 199993060 (Greater Nile Oil Pipeline, man_made=pipeline, operator GNPOC) via de OSM-API.
Uitvoer: FeatureCollection met een LineString (lon,lat) in
v2/build-cache/ais/graaf/olie-heglig-fujairah-leiding-heglig-bashayer.geojson
Draaien: python v2/tools/maak_leidingbeen_olie_heglig_fujairah.py
"""
import json, math, os, time, urllib.request

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
UIT = os.path.join(BEEN, "olie-heglig-fujairah-leiding-heglig-bashayer.geojson")
UA = "grondstoffen-atlas/1.0 (route research; OSM API, ODbL)"
WAY = 199993060
R = 6371.0088


def get(url):
    err = None
    for i in range(5):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=90))
        except Exception as e:
            err = e
            time.sleep(3 * (i + 1))
    raise err


def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


w = get(f"https://api.openstreetmap.org/api/0.6/way/{WAY}.json")["elements"][0]
nodes = w["nodes"]
pos = {}
for k in range(0, len(nodes), 700):
    ch = sorted(set(nodes[k:k + 700]))
    for e in get("https://api.openstreetmap.org/api/0.6/nodes.json?nodes=" + ",".join(map(str, ch)))["elements"]:
        pos[e["id"]] = (e["lat"], e["lon"])
pts = [pos[n] for n in nodes]
coords = [[round(p[1], 5), round(p[0], 5)] for p in pts]
sch = [coords[0]]
for q in coords[1:]:
    if q != sch[-1]:
        sch.append(q)
km = sum(hav((sch[i][1], sch[i][0]), (sch[i + 1][1], sch[i + 1][0])) for i in range(len(sch) - 1))
doc = {"type": "FeatureCollection", "features": [{
    "type": "Feature",
    "properties": {"naam": "Greater Nile Oil Pipeline (GNPOC) Heglig - Bashayer", "km": round(km, 2), "punten": len(sch),
                   "bron": "OpenStreetMap-bijdragers (ODbL), way %d, man_made=pipeline name=Greater Nile Oil Pipeline" % WAY,
                   "tags": w.get("tags", {})},
    "geometry": {"type": "LineString", "coordinates": sch}}]}
os.makedirs(BEEN, exist_ok=True)
json.dump(doc, open(UIT, "w", encoding="utf-8"), ensure_ascii=False)
print(f"{len(sch)} punten, {km:.1f} km, begin lat,lon {sch[0][1]},{sch[0][0]}, eind {sch[-1][1]},{sch[-1][0]}")
print("tags:", w.get("tags", {}))
print("geschreven:", UIT)
