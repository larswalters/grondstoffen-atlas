#!/usr/bin/env python3
"""maak_leidingbeen_olie_unecha_szazhalombatta.py — de vier leidingbenen a1..a4 van olie-unecha-szazhalombatta.

WAAROM DIT BESTAAT. De routebrief (v2/design/routebrieven/olie-unecha-szazhalombatta.md) legt de
Druzhba-1-streng Unecha (RU) -> Mozyr (BY) -> Brody (UA) -> Karpaten -> Slowakije (Transpetrol, Ipel)
-> Barátság I -> MOL Duna, Százhalombatta (HU) vast als OSM `man_made=pipeline substance=oil`-ways.
pyosmium is op deze machine geblokkeerd (beleid toepassingsbeheer), dus de geometrie komt per way-id
uit de OSM-API (api.openstreetmap.org/api/0.6/ways + /nodes, ODbL), met cache op schijf. De ways worden
gestikt op GEDEELDE OSM-NODES (verbonden <=> gedeelde node), niet op afstand: er is dus geen
naadtolerantie nodig en elke aansluiting wordt hier gecontroleerd (naad = 0 m).

Benen (reisvolgorde; ids staan hieronder vast, geen vrij kortste pad — dat zou Druzhba-2 via
Záhony kiezen en die wordt NIET getekend):
  a1  Unecha-knooppunt -> Mozyr           7 ways (314285969 omgekeerd = spur, 137838986, ...)
  a2  Mozyr -> Brody                      1 way  (274735521)
  a3  Brody -> Mukachevo-zuid -> SK/UA-grens bij Budince
                                          580531824 + 54 korte Karpaten-ways + 580531828 + 923057409
  a4  SK/UA-grens -> MOL Duna             564620618 + 793405602 + 793405601 (afgekapt) + 580260776 (vanaf join)
Uitgesloten (Druzhba-2 / Tisza / Odesa-Brody): 580412172, 993324535, 580412171, 1154984406, 566241458,
524599878, 1051144390, 553875773, 1429407850, 579799445, 243984479.

A4-JOIN (afwijking van de brief, zie §9): 793405601 (Slowaaks) en 580260776 (Hongaars) zijn dezelfde buis
twee keer gekarteerd, ~40 m uit elkaar, over ~4,5 km vlak bij de grens (Ipel). Met de naad van de brief
(0,6 km tussen het einde van 793405601 en het begin van 580260776) tekent de lijn daar een
heen-en-weer-spoor. Dit script knipt 793405601 op het eerste punt waar hij de Hongaarse lijn raakt
(<= 100 m) en gaat vanaf het dichtstbijzijnde punt van 580260776 verder. De join-afstand wordt gemeld.

Uitvoer (v2/build-cache/ais/graaf/):
  olie-unecha-szazhalombatta-leiding-a1.geojson .. -a4.geojson
Cache: olie-unecha-szazhalombatta-osmapi-cache.json (ways + nodes; alleen lezen na de eerste run).

Draaien:   python v2/tools/maak_leidingbeen_olie_unecha_szazhalombatta.py --schrijf
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import urllib.request

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../v2
BEEN = os.path.join(WORTEL, "build-cache", "ais", "graaf")
PREFIX = "olie-unecha-szazhalombatta"
CACHE = os.path.join(BEEN, PREFIX + "-osmapi-cache.json")
UA = "grondstoffen-atlas/1.0 (route research; OSM API, ODbL)"

A1 = [314285969, 137838986, 314286194, 314287482, 274735180, 1227331716, 274735017]
A2 = [274735521]
A3 = [580531824, 225572946, 882145406, 882145407, 882145408, 882145409, 882145414, 882145412,
      882145413, 882145410, 882145411, 1267221088, 1267221089, 882145415, 875106706, 875106705,
      875106704, 875106703, 875106702, 875106701, 875106700, 875106707, 1267221090, 1267221091,
      880564102, 880564101, 875106716, 875106715, 880564104, 880564103, 875106708, 875106709,
      875106710, 875106711, 875106712, 875106713, 875106714, 875106699, 882141783, 882141782,
      882141781, 882141780, 882141779, 882141778, 882141777, 882141776, 882141775, 882141774,
      882141773, 882141772, 882141771, 882141770, 882141769, 882141768, 580531828, 923057409]
A4_SK = [564620618, 793405602, 793405601]   # Slowakije (793405601 wordt afgekapt)
A4_HU = 580260776                           # Barátság I (vanaf de join)
JOIN_M = 100.0                              # afkap-drempel: eerste punt van 793405601 binnen 100 m van 580260776

R = 6371.0088


def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def lengte(p):
    return sum(hav(p[i], p[i + 1]) for i in range(len(p) - 1))


def dpl(p, lijn):
    """afstand (km) van punt p tot polylijn (lokaal vlak) en index van het dichtstbijzijnde lijnpunt."""
    kx = 111.32 * math.cos(math.radians(p[0])); ky = 110.57
    best = 1e9
    for i in range(len(lijn) - 1):
        ax, ay = (lijn[i][1] - p[1]) * kx, (lijn[i][0] - p[0]) * ky
        bx, by = (lijn[i + 1][1] - p[1]) * kx, (lijn[i + 1][0] - p[0]) * ky
        dx, dy = bx - ax, by - ay
        L = dx * dx + dy * dy
        t = 0 if L == 0 else max(0, min(1, -(ax * dx + ay * dy) / L))
        best = min(best, math.hypot(ax + t * dx, ay + t * dy))
    return best


def _get(url):
    err = None
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return json.load(urllib.request.urlopen(req, timeout=90))
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(3 * (i + 1))
    raise err


def laad_ways(ids):
    c = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {"ways": {}, "nodes": {}}
    nodig = [i for i in ids if str(i) not in c["ways"]]
    for k in range(0, len(nodig), 100):
        d = _get("https://api.openstreetmap.org/api/0.6/ways.json?ways=" + ",".join(map(str, nodig[k:k + 100])))
        for e in d["elements"]:
            c["ways"][str(e["id"])] = {"nodes": e["nodes"], "tags": e.get("tags", {})}
    nn = sorted({n for i in ids for n in c["ways"][str(i)]["nodes"] if str(n) not in c["nodes"]})
    for k in range(0, len(nn), 700):
        d = _get("https://api.openstreetmap.org/api/0.6/nodes.json?nodes=" + ",".join(map(str, nn[k:k + 700])))
        for e in d["elements"]:
            c["nodes"][str(e["id"])] = [e["lat"], e["lon"]]
    os.makedirs(BEEN, exist_ok=True)
    json.dump(c, open(CACHE, "w", encoding="utf-8"))
    return c


def stik(c, ids, begin_node=None):
    """Stik ways op gedeelde nodes tot één polylijn (lat,lon). Oriëntatie volgt de aansluiting.
    Geeft (punten, nodeketen, rapportregels)."""
    nodes_per_way = {i: list(c["ways"][str(i)]["nodes"]) for i in ids}
    # oriëntatie eerste way: de kant die NIET aansluit op way 2 (of begint op begin_node)
    first = nodes_per_way[ids[0]]
    if begin_node is not None:
        if first[0] != begin_node and first[-1] == begin_node:
            first.reverse()
    elif len(ids) > 1:
        nxt = nodes_per_way[ids[1]]
        if first[0] in (nxt[0], nxt[-1]):
            first.reverse()
    keten = list(first); rap = []
    for i in ids[1:]:
        nd = nodes_per_way[i]
        eind = keten[-1]
        if nd[0] == eind:
            pass
        elif nd[-1] == eind:
            nd = nd[::-1]
        else:
            raise SystemExit(f"way {i} sluit niet aan op een gedeelde node (eindnode {eind}) — stik-fout")
        keten += nd[1:]
        rap.append(i)
    pts = [tuple(c["nodes"][str(n)]) for n in keten]
    return pts, keten


def schrijf(naam, pts, bron, uit):
    coords = [[round(p[1], 5), round(p[0], 5)] for p in pts]
    # dubbele opeenvolgende punten na afronding eruit
    sch = [coords[0]]
    for q in coords[1:]:
        if q != sch[-1]:
            sch.append(q)
    km = lengte([(q[1], q[0]) for q in sch])
    doc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"naam": naam, "km": round(km, 2), "punten": len(sch), "bron": bron,
                       "gereedschap": "maak_leidingbeen_olie_unecha_szazhalombatta.py"},
        "geometry": {"type": "LineString", "coordinates": sch}}]}
    json.dump(doc, open(uit, "w", encoding="utf-8"), ensure_ascii=False)
    return km, len(sch), os.path.getsize(uit) / 1024


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true", help="geojsons wegschrijven (anders alleen rapport)")
    args = ap.parse_args()

    alle = sorted(set(A1 + A2 + A3 + A4_SK + [A4_HU]))
    c = laad_ways(alle)

    bron = "OpenStreetMap-bijdragers (ODbL), OSM-API way-geometrie, man_made=pipeline substance=oil, gestikt op gedeelde nodes"
    res = {}

    # a1: Unecha -> Mozyr (314285969 loopt in OSM van de doorgaande streng naar Unecha: omkeren)
    nd1 = c["ways"]["314285969"]["nodes"]
    start1 = nd1[-1]  # Unecha-eindknoop
    ids1 = A1
    # orientatie: begin bij de Unecha-eindknoop
    p1, k1 = stik(c, ids1, begin_node=start1)
    res["a1"] = (p1, "Druzhba-hoofdstreng Unecha -> Mozyr (RU/BY; OSM-som, geen bronlengte)", ids1)

    p2, k2 = stik(c, A2, begin_node=k1[-1])
    res["a2"] = (p2, "Druzhba zuidtak Mozyr -> Brody (BY/UA; OSM-som)", A2)
    assert k1[-1] == k2[0], "a1/a2 sluiten niet aan"

    p3, k3 = stik(c, A3, begin_node=k2[-1])
    assert k2[-1] == k3[0], "a2/a3 sluiten niet aan"
    res["a3"] = (p3, "Druzhba-1 Brody -> Karpaten -> Mukachevo-zuid -> SK/UA-grens bij Budince (OSM-som)", A3)

    # a4: Slowakije-ways, dan 793405601 afkappen en op 580260776 overstappen
    p4s, k4s = stik(c, A4_SK, begin_node=k3[-1])
    assert k3[-1] == k4s[0], "a3/a4 sluiten niet aan"
    # a4_SK bevat 564620618, 793405602, 793405601 (laatste is de te kappen way)
    n_laatste = len(c["ways"]["793405601"]["nodes"])
    deel_voor = p4s[:len(p4s) - n_laatste + 1]          # t/m het begin van 793405601
    tail = p4s[len(p4s) - n_laatste:]                   # 793405601 volledig
    H = [tuple(c["nodes"][str(n)]) for n in c["ways"][str(A4_HU)]["nodes"]]
    k0 = None
    for k, p in enumerate(tail):
        if dpl(p, H) * 1000 <= JOIN_M and k > 3:
            k0 = k; break
    if k0 is None:
        raise SystemExit("geen join tussen 793405601 en 580260776 binnen 100 m")
    jd = min(range(len(H)), key=lambda j: hav(tail[k0], H[j]))
    join_m = hav(tail[k0], H[jd]) * 1000
    afgekapt_sk = lengte(tail[k0:])
    overgeslagen_hu = lengte(H[:jd + 1])
    p4 = deel_voor[:-1] + tail[:k0 + 1] + H[jd:]
    res["a4"] = (p4, "Druzhba-1 via Slowakije (Transpetrol, Ipel) -> Barátság I -> MOL Duna, Százhalombatta (OSM-som)", A4_SK + [A4_HU])

    print(f"a4-join: 793405601 afgekapt op punt {k0}/{len(tail)-1} ({tail[k0][0]:.5f},{tail[k0][1]:.5f}); "
          f"verder op 580260776 punt {jd}/{len(H)-1} ({H[jd][0]:.5f},{H[jd][1]:.5f}); join {join_m:.0f} m")
    print(f"  weggelaten dubbelgekarteerde stukken: Slowaaks staartje {afgekapt_sk:.2f} km + Hongaars kopstuk {overgeslagen_hu:.2f} km")
    print(f"  (de brief-variant met 0,6 km-naad lengte: 793405601 volledig {lengte(tail):.2f} + 580260776 volledig {lengte(H):.2f} km)")

    tot = 0
    for naam in ("a1", "a2", "a3", "a4"):
        pts, titel, ids = res[naam]
        uit = os.path.join(BEEN, f"{PREFIX}-leiding-{naam}.geojson")
        km_ = lengte(pts)
        tot += km_
        print(f"{naam}: {len(pts)} punten, {km_:.1f} km, van {pts[0][0]:.5f},{pts[0][1]:.5f} naar {pts[-1][0]:.5f},{pts[-1][1]:.5f}  ways={len(ids)}")
        if args.schrijf:
            km, n, kb = schrijf(titel, pts, bron, uit)
            print(f"   geschreven {uit} ({km:.2f} km, {n} punten, {kb:.1f} KB)")
    print(f"totaal {tot:.1f} km")
    # naden tussen de benen (moeten 0 zijn: gedeelde nodes)
    for a, b in (("a1", "a2"), ("a2", "a3"), ("a3", "a4")):
        print(f"naad {a}->{b}: {hav(res[a][0][-1], res[b][0][0])*1000:.1f} m")
    return 0


if __name__ == "__main__":
    sys.exit(main())
