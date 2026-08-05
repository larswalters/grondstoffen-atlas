#!/usr/bin/env python3
"""
knip_osm_been.py — een KORT been uit ÉÉN OSM-way knippen, tussen de projecties
van twee ankers.

WAAROM DIT BESTAAT. `maak_stroombeen_weg.py` routeert over een graaf waarvan de
knopen de OSM-way-vertices zijn. Dat is precies goed voor een corridor van
honderden kilometers, maar het gaat mis zodra een been korter is dan de
knoop-korrel: de router kan alleen op een KNOOP eindigen, en ligt de
dichtstbijzijnde knoop vóórbij de bestemming, dan rijdt de lijn er langs heen en
keert daarna in een rechte stub terug.

GEMETEN GEVAL (2026-08-05, koper fase D, Guixi): `way/1462532976` is de interne
hoofdas van het smeltercomplex — 2.250 m met maar **5** vertices. De
walsdraadfabriek ligt op lon 117.21919; de dichtstbijzijnde way-vertex ligt op
117.21736, **179 m ten westen ervan**. Uitkomst van de bake:

    kop-anker → projectie 43 m → 792 m westwaarts (VOORBIJ de fabriek)
              → 179 m terug oostwaarts naar het anker      = 1,01 km

Dat is **overschiet-en-terug**: dezelfde klasse die op 2026-08-05 bij de
grafiet-via-punten is benoemd, maar dan op het EINDpunt van een been. De 179 m
terugloop is geen werkelijkheid — geen truck rijdt langs de poort heen om te
keren — maar een artefact van onze eigen knoop-korrel. Hem laten staan zou een
meetfout als geometrie de kaart op schrijven.

WAT DIT TOOL DOET. Eén way, twee ankers, geen routering: projecteer beide ankers
loodrecht op de polylijn, knip het stuk ertussen eruit (mét de tussenliggende
vertices, in reisvolgorde) en schrijf dat als GeoJSON-LineString met de ankers
als eerste en laatste punt — hetzelfde contract dat `maak_stroombeen_weg.py`
levert en dat `hecht_marnet.py route --been-geojson` leest.

    python v2/tools/knip_osm_been.py --way 1462532976 \\
        --van  28.33227,117.22545 --naar 28.33180,117.21919 \\
        --id   cu-guixi-fase-d --naam "kathode 贵冶 → walsdraadfabriek" \\
        --uit  v2/build-cache/ais/graaf/stroombeen-guixi-fase-d.geojson

⚠️ DIT IS GEEN VERVANGER VAN `maak_stroombeen_weg.py`. Gebruik dit alléén als
   (a) het been over precies één benoemde way loopt en (b) de way-vertices te
   grof zijn voor de beenlengte. Zodra er een keuze tússen wegen bestaat hoort
   een Dijkstra die keuze te maken, niet een mens die een way-id uitzoekt.
⚠️ DE GEOMETRIE KOMT UIT OSM, NIET UIT EEN OOG. Dat is het hele punt: een
   hand-geplaatste lijn (`vaarwegen-handmatig.geojson`, de Tongling-oostgeul)
   is er voor het geval dat OSM de geometrie NIET heeft. Hier heeft OSM hem wél
   — alleen onze router kon er niet op eindigen.
⚠️ De ankerstukjes (anker → projectie) worden apart gerapporteerd én in de lijn
   opgenomen, net als bij `maak_stroombeen_weg.py`: de lijn begint op het anker
   en eindigt op het anker, zodat de keten geen gat krijgt dat er in
   werkelijkheid niet is. Ze tellen NIET mee in de lengtetoets.

Herkomst: gebouwd tijdens de fase-D-ronde van de koperketen (werkorder
`v2/design/werkorder-koper-guixi-de.md`, sectie C1-alternatief). Bewust in
`v2/tools/` en niet in een scratchpad — dat is de les van `toets_corridor.py`,
dat na één sessie onvindbaar bleek.
"""
import argparse
import json
import math
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

R_AARDE = 6371.0088
OVERPASS = "https://overpass-api.de/api/interpreter"
UA = {"User-Agent": "grondstoffen-atlas/1.0 (knip_osm_been)"}
WORTEL = Path(__file__).resolve().parent.parent          # …/v2
CACHE = WORTEL / "build-cache" / "osmways"


def km(a, b):
    """Grootcirkelafstand in km; punten zijn (lon, lat)."""
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R_AARDE * math.asin(math.sqrt(h))


def haal_way(way_id, ververs=False):
    """Way-geometrie + tags uit Overpass, met schijf-cache (de bron mag niet
    per run veranderen zonder dat je het ziet)."""
    CACHE.mkdir(parents=True, exist_ok=True)
    pad = CACHE / f"way-{way_id}.json"
    if pad.exists() and not ververs:
        return json.loads(pad.read_text(encoding="utf-8"))
    q = f"[out:json][timeout:60];way({way_id});out tags geom;"
    req = urllib.request.Request(
        OVERPASS, data=urllib.parse.urlencode({"data": q}).encode(), headers=UA)
    with urllib.request.urlopen(req, timeout=90) as r:
        d = json.load(r)
    if not d.get("elements"):
        sys.exit(f"way {way_id} niet gevonden in Overpass")
    w = d["elements"][0]
    uit = {"id": way_id, "tags": w.get("tags", {}),
           "punten": [[p["lon"], p["lat"]] for p in w["geometry"]]}
    pad.write_text(json.dumps(uit, ensure_ascii=False), encoding="utf-8")
    return uit


def projecteer(punt, lijn):
    """Loodrechte projectie van `punt` op de polylijn. Geeft
    (afstand_km, index_van_het_segment, t, projectiepunt) terug.

    Vlakke benadering met een lokale meter-schaal — over een been van enkele
    honderden meters is het verschil met een echte geodeet verwaarloosbaar, en
    de afstand die telt (anker → lijn) wordt daarna alsnog met km() gemeten."""
    la0 = math.radians(punt[1])
    mx, my = 111320.0 * math.cos(la0), 110540.0
    best = None
    for i in range(len(lijn) - 1):
        a, b = lijn[i], lijn[i + 1]
        px, py = (punt[0] - a[0]) * mx, (punt[1] - a[1]) * my
        bx, by = (b[0] - a[0]) * mx, (b[1] - a[1]) * my
        L2 = bx * bx + by * by
        t = 0.0 if L2 == 0 else max(0.0, min(1.0, (px * bx + py * by) / L2))
        proj = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
        d = km(punt, proj)
        if best is None or d < best[0]:
            best = (d, i, t, proj)
    return best


def knip(lijn, van, naar):
    """Het stuk van de polylijn tussen de projecties van `van` en `naar`,
    in reisvolgorde, inclusief de twee projectiepunten."""
    dv, iv, tv, pv = projecteer(van, lijn)
    dn, i_n, tn, pn = projecteer(naar, lijn)
    vooruit = (iv, tv) <= (i_n, tn)
    if vooruit:
        tussen = [tuple(p) for p in lijn[iv + 1:i_n + 1]]
        stuk = [pv] + tussen + [pn]
    else:
        tussen = [tuple(p) for p in lijn[i_n + 1:iv + 1]]
        stuk = [pv] + list(reversed(tussen)) + [pn]
    # samenvallende punten wegnemen (een projectie kán op een vertex vallen)
    schoon = [stuk[0]]
    for p in stuk[1:]:
        if km(schoon[-1], p) * 1000 > 0.5:
            schoon.append(p)
    return schoon, (dv, pv), (dn, pn), vooruit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--way", type=int, required=True, help="OSM way-id")
    ap.add_argument("--van", required=True, help="anker kop als 'lat,lon'")
    ap.add_argument("--naar", required=True, help="anker staart als 'lat,lon'")
    ap.add_argument("--id", required=True, help="been-id, bv. cu-guixi-fase-d")
    ap.add_argument("--naam", required=True)
    ap.add_argument("--uit", required=True)
    ap.add_argument("--modaliteit", default="truck")
    ap.add_argument("--gepubliceerd-km", type=float, default=None)
    ap.add_argument("--bronnoot", default="")
    ap.add_argument("--max-aanloop-km", type=float, default=0.25,
                    help="hard maximum voor anker → lijn; erboven stopt het "
                         "tool, want dan is dit de verkeerde way")
    ap.add_argument("--ververs", action="store_true",
                    help="Overpass opnieuw bevragen i.p.v. de cache")
    a = ap.parse_args()

    def punt(s):
        la, lo = (float(x) for x in s.split(","))
        return (lo, la)                      # intern (lon, lat)

    van, naar = punt(a.van), punt(a.naar)
    w = haal_way(a.way, a.ververs)
    lijn = [tuple(p) for p in w["punten"]]
    lengte_way = sum(km(lijn[i], lijn[i + 1]) for i in range(len(lijn) - 1))

    print(f"way {a.way} · {w['tags']}")
    print(f"  {len(lijn)} vertices · {lengte_way*1000:.0f} m "
          f"({lengte_way*1000/max(1, len(lijn)-1):.0f} m per segment)")
    if "access" in w["tags"]:
        print(f"  ⚠️ access={w['tags']['access']} — controleer of dit been "
              f"publiek berijdbaar is")

    stuk, (dv, pv), (dn, pn), vooruit = knip(lijn, van, naar)
    for naam, d in (("kop", dv), ("staart", dn)):
        if d > a.max_aanloop_km:
            sys.exit(f"STOP: {naam}-anker ligt {d*1000:.0f} m van way {a.way} "
                     f"(max {a.max_aanloop_km*1000:.0f} m). Verkeerde way, of "
                     f"het anker hoort hier niet aan te hechten.")

    kmWeg = sum(km(stuk[i], stuk[i + 1]) for i in range(len(stuk) - 1))
    punten = [van] + stuk + [naar]
    schoon = [punten[0]]
    for p in punten[1:]:
        if km(schoon[-1], p) * 1000 > 0.5:
            schoon.append(p)
    kmTot = sum(km(schoon[i], schoon[i + 1]) for i in range(len(schoon) - 1))

    print(f"\n  {a.naam}")
    print(f"  been over de way : {kmWeg*1000:7.0f} m "
          f"({'oost→west' if not vooruit else 'volgorde van de way'})")
    print(f"  aanloop kop      : {dv*1000:7.0f} m  (anker → projectie)")
    print(f"  aanloop staart   : {dn*1000:7.0f} m")
    print(f"  getekende lijn   : {kmTot*1000:7.0f} m · {len(schoon)} punten")
    if a.gepubliceerd_km:
        afw = (kmWeg - a.gepubliceerd_km) / a.gepubliceerd_km * 100
        vlag = "OK" if abs(afw) <= 10 else "⚠️ BUITEN ±10% — bevinding"
        print(f"  lengtetoets      : {kmWeg:.3f} tegen {a.gepubliceerd_km} km "
              f"= {afw:+.1f}%  [{vlag}]")
    # terugloop-controle: pad ÷ hemelsbreed over de hele lijn (de maat uit de
    # grafietronde van 2026-08-05 — een echte bocht komt ergens uit, een
    # terugloop blijft ter plaatse)
    recht = km(schoon[0], schoon[-1])
    verh = kmTot / recht if recht > 0 else float("inf")
    print(f"  pad ÷ hemelsbreed: {verh:.2f} "
          f"({'geen terugloop' if verh < 1.5 else '⚠️ mogelijk overschiet-en-terug'})")

    props = {"id": a.id, "naam": a.naam, "modaliteit": a.modaliteit,
             "km": round(kmTot, 3), "kmWeg": round(kmWeg, 3),
             "kmAanloopVan": round(dv, 3), "kmAanloopNaar": round(dn, 3),
             "osmWay": a.way, "osmTags": w["tags"],
             "gepubliceerdKm": a.gepubliceerd_km, "bronnoot": a.bronnoot,
             "gereedschap": "knip_osm_been.py",
             "waaromNietGeroutet":
                 "de way heeft te weinig vertices voor een been van deze "
                 "lengte; maak_stroombeen_weg.py eindigt op een knoop en "
                 "schiet daardoor voorbij de bestemming (overschiet-en-terug)"}
    uit = {"type": "FeatureCollection", "features": [
        {"type": "Feature", "properties": props,
         "geometry": {"type": "LineString",
                      "coordinates": [[round(lo, 6), round(la, 6)]
                                      for lo, la in schoon]}}]}
    pad = Path(a.uit)
    pad.parent.mkdir(parents=True, exist_ok=True)
    pad.write_text(json.dumps(uit, ensure_ascii=False), encoding="utf-8")
    print(f"\n  geschreven: {pad} · {os.path.getsize(pad)/1024:.1f} KB")


if __name__ == "__main__":
    main()
