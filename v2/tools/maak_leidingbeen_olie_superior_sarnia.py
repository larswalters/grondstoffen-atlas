#!/usr/bin/env python3
"""maak_leidingbeen_olie_superior_sarnia.py - b1 van olie-superior-sarnia.

Brief v2/design/routebrieven/olie-superior-sarnia.md. Enbridge Line 5 (Lakehead) staat doorlopend in OSM als
man_made=pipeline (substance=oil, operator Enbridge): 30 ways van de kop bij Superior (Wisconsin) via het Upper Peninsula,
de Straits of Mackinac (way 329360259; 329360261 is de dubbelganger en wordt NIET gebruikt) en Bay City naar het eind op het
tankenpark aan de oostoever van de St. Clair (Ontario). De way-id's komen uit de toets (pbf us-wisconsin/us-michigan);
dit script haalt ze per id uit de OSM-API (geen pbf-scan nodig) en stikt ze aaneen.

    python v2/tools/maak_leidingbeen_olie_superior_sarnia.py --haal      # OSM-API, 30 ways -> cache
    python v2/tools/maak_leidingbeen_olie_superior_sarnia.py --schrijf   # stikken + FeatureCollection
"""
import os, json, math, time, argparse, urllib.request

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../v2
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
CACHE = os.path.join(BEEN, "olie-superior-sarnia-ways.json")
UIT = os.path.join(BEEN, "olie-superior-sarnia-leiding-line5.geojson")
IDS = ("329777044 329230567 329230555 329360259 329393241 329393239 329393240 329393237 329393238 17938019 329421120 "
       "329421119 329421118 329475045 329475042 1030808059 1030808056 1030808055 329521765 329521762 329521758 329591767 "
       "329591766 329591768 329593787 329593786 329647926 329647925 329675102 627763507").split()
NAAM = "Enbridge Line 5 (ruwe olie + NGL), Superior Terminal naar Sarnia via Mackinac (OSM)"
R = 6371.0088


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[1], a[0], b[1], b[0]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def haal():
    uit = {}
    for i in IDS:
        for _ in range(3):
            try:
                r = urllib.request.Request(f"https://api.openstreetmap.org/api/0.6/way/{i}/full.json",
                                           headers={"User-Agent": "grondstoffen-atlas/1.0 (olie-superior-sarnia)"})
                d = json.load(urllib.request.urlopen(r, timeout=60))
                break
            except Exception as e:          # noqa: BLE001
                print("retry", i, e)
                time.sleep(3)
        nodes = {n["id"]: (n["lon"], n["lat"]) for n in d["elements"] if n["type"] == "node"}
        w = [e for e in d["elements"] if e["type"] == "way"][0]
        uit[i] = {"id": int(i), "naam": w["tags"].get("name"), "pts": [list(nodes[n]) for n in w["nodes"]]}
    json.dump(uit, open(CACHE, "w"))
    print("geschreven:", CACHE, len(uit), "ways")


def stik():
    ways = json.load(open(CACHE, encoding="utf-8"))
    pts, naden = [], []
    for i in IDS:                                    # lijst = reisvolgorde Superior -> Sarnia
        p = ways[i]["pts"]
        if pts:
            if km(pts[-1], p[0]) > km(pts[-1], p[-1]):
                p = p[::-1]
            naden.append(round(km(pts[-1], p[0]), 4))
            if p[0] == pts[-1]:
                p = p[1:]
        pts.extend(p)
    tot = sum(km(a, b) for a, b in zip(pts, pts[1:]))
    print(f"stik: {tot:.1f} km, {len(pts)} punten, {len(IDS)} ways; naden max {max(naden):.4f} km")
    print("kop", pts[0], "eind", pts[-1])
    return pts, tot


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--haal", action="store_true")
    ap.add_argument("--schrijf", action="store_true")
    a = ap.parse_args()
    if a.haal:
        haal()
    if a.schrijf:
        pts, tot = stik()
        fc = {"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"name": NAAM, "km": round(tot, 1)},
              "geometry": {"type": "LineString", "coordinates": pts}}]}
        json.dump(fc, open(UIT, "w", encoding="utf-8"))
        print("geschreven:", UIT)


if __name__ == "__main__":
    main()
