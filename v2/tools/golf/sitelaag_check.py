"""Vergelijk de markers van nieuwe (niet-geregistreerde) stromen met de sitelaag-sites van dezelfde grondstof.
Een site op 0,3-40 km van een marker is een kandidaat om gelijk te trekken (centroide vs satelliet-gelegd anker)."""
import io, json, math, glob, os, sys

REPO = "C:/automation/Projects/General/grondstoffen-atlas"
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def gc(a, b):
    c = math.sin(math.radians(a[1])) * math.sin(math.radians(b[1])) + math.cos(math.radians(a[1])) * math.cos(math.radians(b[1])) * math.cos(math.radians(a[0] - b[0]))
    return 6371.0088 * math.acos(max(-1, min(1, c)))


reg = json.load(io.open(REPO + "/v2/data/stromen-register.json", encoding="utf-8"))
bekend = {s["bestand"] for s in reg["stromen"]} | {u["bestand"] for u in reg["uitgesloten"]}
nieuw = [p for p in sorted(glob.glob(REPO + "/v2/data/stroomroute-*.json")) if os.path.basename(p) not in bekend]
sites = {}
for p in glob.glob(REPO + "/v2/design/*-sitelaag.json"):
    gs = os.path.basename(p).split("-sitelaag")[0]
    d = json.load(io.open(p, encoding="utf-8"))
    sites[gs] = d.get("sites", [])
n = 0
for p in nieuw:
    sid = os.path.basename(p)[len("stroomroute-"):-5]
    gs = sid.split("-")[0]
    d = json.load(io.open(p, encoding="utf-8"))
    for m in d.get("markers", []):
        pt = [m["lon"], m["lat"]]
        best = None
        for s in sites.get(gs, []):
            if s.get("lat") is None:
                continue
            dd = gc(pt, [s["lon"], s["lat"]])
            if best is None or dd < best[0]:
                best = (dd, s)
        if best and 0.3 < best[0] < 40:
            n += 1
            print(f"{sid:36} marker {m['naam'][:48]:48} ↔ site {best[1]['id']:24} {best[1]['naam'][:28]:28} {best[0]:6.1f} km  [{best[1].get('rol','')}]")
print("kandidaten:", n)
