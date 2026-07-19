#!/usr/bin/env python3
"""toets_usace.py — de VS-meetlat voor de binnenvaart-pilot (M24, LAR-487).

Rolverdeling uit het M24-bronnenplan, definitief gemaakt bij LAR-486: **OSM
levert de geometrie, het officiële net is de onafhankelijke scheidsrechter.**
Dit script haalt het USACE National Waterway Network op (public domain) en meet
hoe ver onze gebakken middellijn van dat officiële net af ligt.

Waarom dit náást de corridor-toets bestaat: die toets in bake_marnet.py
vergelijkt de gebakken keten met de bron waaruit hij gebakken IS en meet dus per
definitie ~0 m. Hij bewijst procesintegriteit, niet bronkwaliteit. Pas een
tweede, onafhankelijke bron kan zeggen of de bron zélf klopt — dat is precies
wat de UNECE-vergelijking in de NL-pilot deed en wat hier de USACE doet.

Bron: services7.arcgis.com/.../Waterway_Networks/FeatureServer/1 (laag
`Waterway_Network`, 6.859 links). Filters: GEO_CLASS='I' (Inland; de laag bevat
óók 1.454 ocean- en 980 Great-Lakes-links) en FUNC_CLASS<>'N' (non-navigable).

Draaien:  python v2/tools/toets_usace.py
          python v2/tools/toets_usace.py --labels mississippi,mississippi-boven
"""

import argparse
import json
import math
import os
import sys
import time
import urllib.parse
import urllib.request

from shapely.geometry import MultiLineString, Point
from shapely.ops import unary_union

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)
CACHE = os.path.join(V2, "build-cache")

USACE_QUERY = ("https://services7.arcgis.com/n1YM8pTrFmm7L4hs/arcgis/rest/"
               "services/Waterway_Networks/FeatureServer/1/query")

# Ruime corridor: de Mississippi meandert tussen New Orleans en Memphis west
# tot lon -91,66 — een strakke corridor rond -90,06 knipt de rivier kapot.
BBOX_MISSISSIPPI = (-92.0, 29.4, -89.0, 35.6)

PAGINA = 1000       # maxRecordCount van de laag is 2000; 1000 = minder IncompleteRead
POGINGEN = 4


def haal_usace(bbox, waar, velden):
    """Alle features binnen de bbox, gepagineerd.

    Twee valkuilen zitten hierin verwerkt:
      * bij f=geojson staat `exceededTransferLimit` GENEST onder het top-level
        `properties`-object (en `properties` is null als er niets afgekapt is).
        Op de top-level sleutel checken geeft altijd None -> stille truncatie
        op 2.000 features.
      * de native SR van de laag is 4269 (NAD83); zonder expliciete outSR meet
        je tegen NAD83-coordinaten.
    """
    uit = []
    offset = 0
    while True:
        params = {
            "where": waar,
            "geometry": ",".join(str(v) for v in bbox),
            "geometryType": "esriGeometryEnvelope",
            "inSR": "4326",
            "outSR": "4326",
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": velden,
            "returnGeometry": "true",
            "orderByFields": "OBJECTID ASC",
            "resultOffset": str(offset),
            "resultRecordCount": str(PAGINA),
            "f": "geojson",
        }
        url = USACE_QUERY + "?" + urllib.parse.urlencode(params)
        for poging in range(POGINGEN):
            try:
                with urllib.request.urlopen(url, timeout=120) as r:
                    d = json.load(r)
                break
            except Exception as e:  # noqa: BLE001 — IncompleteRead komt intermitterend voor
                if poging == POGINGEN - 1:
                    raise
                print(f"    poging {poging + 1} faalde ({e}) — opnieuw")
                time.sleep(2 * (poging + 1))
        feats = d.get("features") or []
        uit.extend(feats)
        meer = (d.get("properties") or {}).get("exceededTransferLimit")
        if not meer or not feats:
            break
        offset += len(feats)
    return uit


def lijnen_uit(features, riviernaam=None):
    """GeoJSON-features -> lijst polylines [(lon,lat), ...]."""
    lijnen = []
    for f in features:
        props = f.get("properties") or {}
        if riviernaam and (props.get("RIVERNAME") or "").upper() != riviernaam:
            continue
        g = f.get("geometry") or {}
        delen = []
        if g.get("type") == "LineString":
            delen = [g["coordinates"]]
        elif g.get("type") == "MultiLineString":
            delen = g["coordinates"]
        for deel in delen:
            pts = [(p[0], p[1]) for p in deel if len(p) >= 2]
            if len(pts) >= 2:
                lijnen.append(pts)
    return lijnen


def percentiel(gesorteerd, q):
    if not gesorteerd:
        return float("nan")
    i = min(len(gesorteerd) - 1, max(0, int(round(q * (len(gesorteerd) - 1)))))
    return gesorteerd[i]


def toets(labels):
    pad = os.path.join(CACHE, "vaarwegen_osm.geojson")
    if not os.path.exists(pad):
        raise SystemExit(f"{pad} ontbreekt — draai eerst fetch_waterways.py osm")
    onze = {f["properties"]["label"]: f["geometry"]["coordinates"]
            for f in json.load(open(pad, encoding="utf-8"))["features"]}
    ontbreekt = [la for la in labels if la not in onze]
    if ontbreekt:
        raise SystemExit(f"labels ontbreken in vaarwegen_osm.geojson: {ontbreekt}")

    print(f"USACE National Waterway Network ophalen · bbox {BBOX_MISSISSIPPI}")
    feats = haal_usace(BBOX_MISSISSIPPI,
                       "GEO_CLASS='I' AND FUNC_CLASS<>'N'",
                       "RIVERNAME,FUNC_CLASS,WTWY_TYPE,AMILE,BMILE,LENGTH,GEO_CLASS")
    print(f"  inland-links in de corridor: {len(feats)}")

    rivier = [f for f in feats
              if (f.get("properties") or {}).get("RIVERNAME", "").upper() == "MISSISSIPPI RIVER"]
    # AMILE/BMILE zijn niet overal gevuld (twee links in de corridor staan op
    # 0.0). Die nullen als mijlpaal lezen suggereert een gat dat er niet is —
    # de geometrie van die links zit gewoon in de extract.
    mijlen = [v for f in rivier for v in
              (f["properties"].get("AMILE"), f["properties"].get("BMILE")) if v]
    zonder = sum(1 for f in rivier
                 if not (f["properties"].get("AMILE") or f["properties"].get("BMILE")))
    klassen = sorted({(f["properties"].get("FUNC_CLASS") or "?") for f in rivier})
    print(f"  waarvan RIVERNAME='MISSISSIPPI RIVER': {len(rivier)} links · "
          f"river miles {min(mijlen):.0f}–{max(mijlen):.0f}"
          f"{f' (+{zonder} zonder milepost)' if zonder else ''} · FUNC_CLASS {klassen}")
    print(f"  totale USACE-lengte: {sum(f['properties'].get('LENGTH') or 0 for f in rivier):.1f} mijl")
    # FUNC_CLASS is meteen een onafhankelijke toets op de zeevaart-vlag: 'B'
    # (deep + shallow draft) houdt op waar de diepzeevaart ophoudt.
    diep = [f["properties"] for f in rivier if f["properties"].get("FUNC_CLASS") == "B"]
    if diep:
        grens = max(max(p.get("AMILE") or 0, p.get("BMILE") or 0) for p in diep)
        print(f"  deep-draft (FUNC_CLASS='B') t/m river mile {grens:.0f} "
              f"— Baton Rouge ligt op ~229")

    lijnen = lijnen_uit(rivier, "MISSISSIPPI RIVER")
    if not lijnen:
        raise SystemExit("geen USACE-Mississippi-geometrie — filters/bbox checken")

    # lokale vlakke projectie (km), gedeeld door beide kanten
    alle_lat = [la for lijn in lijnen for _lo, la in lijn]
    lat0 = math.radians(sum(alle_lat) / len(alle_lat))
    sx, sy = 111.2 * math.cos(lat0), 111.2
    usace = unary_union(MultiLineString([[(lo * sx, la * sy) for lo, la in lijn]
                                         for lijn in lijnen]))

    print("\nafstand van ONZE OSM-middellijn tot het USACE-net:")
    totaal = []
    for label in labels:
        d = sorted(usace.distance(Point(lo * sx, la * sy)) * 1000.0   # -> meter
                   for lo, la in onze[label])
        totaal.extend(d)
        print(f"  {label:<20} {len(d):5d} punten · mediaan {percentiel(d, .5):6.0f} m · "
              f"p90 {percentiel(d, .9):6.0f} m · p95 {percentiel(d, .95):6.0f} m · "
              f"max {d[-1]:7.0f} m")
    totaal.sort()
    print(f"  {'SAMEN':<20} {len(totaal):5d} punten · mediaan {percentiel(totaal, .5):6.0f} m · "
          f"p90 {percentiel(totaal, .9):6.0f} m · p95 {percentiel(totaal, .95):6.0f} m · "
          f"max {totaal[-1]:7.0f} m")
    boven = [x for x in totaal if x > 500]
    print(f"\n  punten >500 m van het officiele net: {len(boven)} "
          f"({100.0 * len(boven) / len(totaal):.2f}%)")

    # De beslissende controle. Puntafstanden zeggen niets over de vraag of onze
    # lijn een OMWEG maakt — een verkeerd gevolgde oxbow ligt overal dicht bij
    # ergens. De totale lengte wél: die moet de officiele vaarafstand zijn.
    onze_km = sum(f["properties"]["km"] for f in
                  json.load(open(pad, encoding="utf-8"))["features"]
                  if f["properties"]["label"] in labels)
    print(f"\n  lengte onze ketens : {onze_km:8.1f} km = {onze_km / 1.609344:7.1f} river miles")
    print(f"  USACE-links in bbox: {sum(f['properties'].get('LENGTH') or 0 for f in rivier):8.1f} "
          f"mijl (mile {min(mijlen):.0f}-{max(mijlen):.0f}, ruimer dan onze ketens)")
    return totaal


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--labels", default="mississippi,mississippi-boven",
                    help="komma-gescheiden systeemlabels uit vaarwegen_osm.geojson")
    args = ap.parse_args()
    toets([s.strip() for s in args.labels.split(",") if s.strip()])
