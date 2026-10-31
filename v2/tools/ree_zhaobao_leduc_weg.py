#!/usr/bin/env python3
"""ree_zhaobao_leduc_weg.py — wegscan_puur.py voor het profiel ree-zhaobao-leduc-husky-leduc, mét een gatdichter.

WAAROM. De canada-pbf in build-cache (Geofabrik) mist bij Avola (BC, Yellowhead 5, 51.78N -119.32W) drie
trunk-ways die in OSM nu wel bestaan (api.openstreetmap.org, 2026-10-31): 626197240 (YH 5), 58330070 (YH 5, brug) en
626197429 (YH 5). Zonder die ~1,2 km is Hwy 5 doorgesneden en geeft de router "geen wegpad tussen punt 5 en 6".
Dit script draait wegscan_puur ongewijzigd en voegt alleen de ontbrekende trunk/primary-ways (geometrie letterlijk uit de OSM-API,
per kleine bbox rond een gat) aan de way-lijst toe voordat er gerouteerd wordt. Ook bij Jasper (YH 16) mist de pbf ~10 ways. Geen andere tool of profiel wordt geraakt.

Draaien (vanuit de repo-root, PYTHONIOENCODING=utf-8):
    python v2/tools/ree_zhaobao_leduc_weg.py --profiel ree-zhaobao-leduc-husky-leduc
"""
import json
import os
import sys
import urllib.request

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import maak_stroombeen_weg as m  # noqa: E402
import wegscan_puur as W  # noqa: E402

# (west, zuid, oost, noord) — alleen de plekken waar de canada-pbf een trunk/primary-stuk mist (gevonden door "geen wegpad tussen punt i en i+1")
GAT_BBOXEN = [
    (-119.34, 51.775, -119.30, 51.795),   # Avola, YH 5: 3 ways
    (-118.21, 52.85, -118.04, 52.93),     # Jasper, YH 16 / Connaught Dr: ~10 ways
]
KLASSEN = {"motorway", "trunk", "primary", "secondary", "tertiary", "motorway_link", "trunk_link", "primary_link",
           "secondary_link", "tertiary_link"}
UA = {"User-Agent": "grondstoffen-atlas/1.0 (routebrief ree-zhaobao-leduc gatdichter)"}


def haal_bbox(bb):
    w, s_, e, n = bb
    url = f"https://api.openstreetmap.org/api/0.6/map.json?bbox={w},{s_},{e},{n}"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120))
    nodes = {x["id"]: (x["lon"], x["lat"]) for x in d["elements"] if x["type"] == "node"}
    uit = []
    for x in d["elements"]:
        if x["type"] != "way":
            continue
        t = x.get("tags", {})
        if t.get("highway") not in KLASSEN or t.get("access") in ("no", "private"):
            continue
        pts = [[nodes[i][0], nodes[i][1]] for i in x["nodes"] if i in nodes]
        if len(pts) >= 2:
            uit.append({"id": x["id"], "soort": t["highway"], "ref": t.get("ref", ""), "pts": pts,
                        "regio": "osm-api-gatdichter"})
    return uit


_orig = W.uit_pbf


def uit_pbf_met_gat(bb, timeout=0):
    alle = _orig(bb, timeout)
    al = {w["id"] for w in alle}
    n_nieuw = 0
    for gb in GAT_BBOXEN:
        for w in haal_bbox(gb):
            if w["id"] not in al:
                alle.append(w)
                al.add(w["id"])
                n_nieuw += 1
                print(f"  gatdichter: way {w['id']} {w['soort']} {w['ref']} {len(w['pts'])} punten toegevoegd", flush=True)
    print(f"  gatdichter: {n_nieuw} ways uit de OSM-API toegevoegd (de pbf miste ze)", flush=True)
    return alle


if __name__ == "__main__":
    m._ways_uit_overpass = uit_pbf_met_gat
    argv = list(sys.argv[1:])
    if "--bron" in argv:
        i = argv.index("--bron")
        del argv[i:i + 2]
    sys.argv = ["maak_stroombeen_weg.py"] + argv + ["--bron", "overpass"]
    m.main()
