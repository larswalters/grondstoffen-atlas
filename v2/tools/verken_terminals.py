#!/usr/bin/env python3
"""verken_terminals.py — de SCOUT voor straatniveau-aansluitingen (M26).

Een aansluiting is de plek waar één grondstof het net raakt: de concentraat-
kade, het laadspoor bij de smelter, de erts-pier. Op ~50 m nauwkeurig, want op
z17 zie je de kade liggen en dan moet de lijn het juiste bekken in — niet 800 m
over de containers (`design/lod-ontwerpbrief.md`).

Deze tool WIJST NIETS AAN. Hij haalt uit OSM op wat er bij een site ligt en zet
de kandidaten op een rij met coördinaat, tags en afstand tot het opgegeven
midden. De redacteur kiest; `maak_aansluitingen.py` meet daarna de snap op de
netten. Zelfde rolverdeling als `maak_knooppunten.py` — de machine meet, de
redacteur oordeelt.

Waarom Overpass en niet de Geofabrik-extracts: dit zijn zeven puntlocaties, geen
wereldbake. Een `around`-query van een paar km kost seconden en komt uit de
cache van `fetch_waterways.overpass()`; een extract downloaden kost gigabytes.

Bron: OpenStreetMap-bijdragers (ODbL) — hoort in de attributie zodra een
coördinaat hieruit in `aansluitingen.json` landt.

Draaien:
  python v2/tools/verken_terminals.py                 # alle sites
  python v2/tools/verken_terminals.py --site patache  # één site
  python v2/tools/verken_terminals.py --schrijf       # dump naar build-cache
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))

import fetch_waterways as fw  # noqa: E402 — overpass() mét schijf-cache

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

UIT = HIER.parent / "build-cache" / "terminals"


# --------------------------------------------------------------------------
# de sites van de pilot — de twee koperstromen uit data/copper.js
# --------------------------------------------------------------------------
# `midden` is een ZOEKMIDDEN, geen antwoord: het zegt alleen waar de tool moet
# kijken. De keuze uit de kandidaten is redactie.

SITES = [
    # --- stroom A: concentraat Collahuasi → Tongling (zee → rivier) ---------
    {"id": "collahuasi", "naam": "Collahuasi — concentrator/laadplek",
     "midden": (-20.97, -68.70), "straal": 9000, "soort": "mijn",
     "waarom": "vertrek van stroom A; concentraat verlaat de mijn per slurry-pijp"},
    {"id": "patache", "naam": "Puerto Patache (Collahuasi-terminal)",
     "midden": (-20.80, -70.185), "straal": 6000, "soort": "kade",
     "waarom": "de eigen concentraatterminal van Collahuasi aan de Stille Oceaan"},
    {"id": "antofagasta", "naam": "Antofagasta — haven",
     "midden": (-23.65, -70.40), "straal": 6000, "soort": "kade",
     "waarom": "wat data/copper.js als via-haven noemt; ter vergelijking met Patache"},
    {"id": "shanghai-yangtze", "naam": "Shanghai — bulkkade aan de Yangtze (Luojing e.o.)",
     "midden": (31.42, 121.49), "straal": 9000, "soort": "kade",
     "waarom": "de overslag zee → rivier van stroom A; Yangshan is container, geen concentraat"},
    {"id": "tongling", "naam": "Tongling Nonferrous — smelter + eigen kade",
     "midden": (30.94, 117.80), "straal": 9000, "soort": "fabriek",
     "waarom": "aankomst van stroom A; de loskade aan de Yangtze bij de smelter"},

    # --- stroom B: concentraat Escondida → Jiangxi (zee → spoor) ------------
    {"id": "escondida", "naam": "Escondida — concentrator/laadplek",
     "midden": (-24.27, -69.07), "straal": 9000, "soort": "mijn",
     "waarom": "vertrek van stroom B; concentraat per 166 km pijpleiding naar Coloso"},
    {"id": "coloso", "naam": "Puerto Coloso (Escondida-terminal)",
     "midden": (-23.755, -70.46), "straal": 6000, "soort": "kade",
     "waarom": "de eigen concentraatterminal van Escondida, ten zuiden van Antofagasta"},
    {"id": "ningbo-beilun", "naam": "Ningbo-Zhoushan — Beilun ertsterminal",
     "midden": (29.94, 121.87), "straal": 10000, "soort": "kade",
     "waarom": "de overslag zee → spoor van stroom B"},
    {"id": "guixi", "naam": "Jiangxi Copper (Guixi) — smelter + laadspoor",
     "midden": (28.30, 117.22), "straal": 9000, "soort": "fabriek",
     "waarom": "aankomst van stroom B; de grootste kopersmelter ter wereld"},

    # --- stroom C: koperkathode Lobito → Rotterdam → Rijn → Duisburg --------
    {"id": "lobito", "naam": "Lobito — kadeterminal van de Lobito-corridor",
     "midden": (-12.35, 13.55), "straal": 7000, "soort": "kade",
     "waarom": "vertrek van stroom C; het Angolese eind van de Copperbelt-corridor"},
    {"id": "rotterdam-metaal", "naam": "Rotterdam — stukgoed/metaalkades (Waalhaven e.o.)",
     "midden": (51.895, 4.395), "straal": 6000, "soort": "kade",
     "waarom": "waar kathode aan land komt — NIET de droge-bulkkade van kolen"},
    {"id": "duisburg", "naam": "Duisburg — Duisport, binnenhavenbekkens",
     "midden": (51.445, 6.725), "straal": 8000, "soort": "losplek",
     "waarom": "aankomst van stroom C én D; grootste binnenhaven ter wereld"},

    # --- stroom D: steenkool Cerrejón → Rotterdam → Rijn → Ruhr ------------
    {"id": "cerrejon", "naam": "Cerrejón — kolenmijn + laadstation",
     "midden": (11.10, -72.60), "straal": 12000, "soort": "mijn",
     "waarom": "vertrek van stroom D; eigen 150 km kolenspoor naar de kust"},
    {"id": "puerto-bolivar", "naam": "Puerto Bolívar — kolenpier van Cerrejón",
     "midden": (12.23, -71.98), "straal": 7000, "soort": "kade",
     "waarom": "het zee-eind van dat kolenspoor"},
    {"id": "rotterdam-bulk", "naam": "Rotterdam — EMO droge-bulkterminal (Maasvlakte)",
     "midden": (51.955, 4.045), "straal": 7000, "soort": "kade",
     "waarom": "de kolenkade — dezelfde haven als stroom C, andere terminal; dát is "
               "waarom de aansluitingenlaag bestaat"},
]


# --------------------------------------------------------------------------
# de query
# --------------------------------------------------------------------------
# Bewust breed: we weten nog niet welke tag de terminal draagt. Chinese en
# Chileense terminals zijn ongelijk getagd — de een als `man_made=pier`, de
# ander alleen als `landuse=industrial` met een naam. Liever twintig kandidaten
# beoordelen dan de juiste missen omdat de tag niet in de lijst stond.

CLAUSES = [
    'way["man_made"~"^(pier|quay|breakwater|works|conveyor|pipeline|storage_tank|silo|crane|gantry_crane)$"]',
    'way["waterway"~"^(dock|berth)$"]',
    'way["industrial"]',
    'way["landuse"~"^(industrial|port|quarry)$"]["name"]',
    'way["harbour"]',
    'way["railway"~"^(rail|yard|siding|industrial|spur)$"]["name"]',
    'way["railway"~"^(yard|siding|industrial|spur)$"]',
    'node["seamark:type"~"^(berth|harbour|mooring|terminal)$"]',
    'node["industrial"]',
    'relation["landuse"~"^(industrial|port)$"]["name"]',
    'relation["man_made"~"^(works|pier)$"]',
]


def query_voor(site) -> str:
    lat, lon = site["midden"]
    r = site["straal"]
    delen = "\n".join(f"  {c}(around:{r},{lat},{lon});" for c in CLAUSES)
    return f"[out:json][timeout:180];\n(\n{delen}\n);\nout tags center;"


def km(lat1, lon1, lat2, lon2) -> float:
    r = math.pi / 180
    d = (math.sin(lat1 * r) * math.sin(lat2 * r)
         + math.cos(lat1 * r) * math.cos(lat2 * r) * math.cos((lon2 - lon1) * r))
    return 6371.0 * math.acos(max(-1.0, min(1.0, d)))


# Tags die iets zeggen over de ROL van het object; de rest is ruis in het rapport.
TOON = ["name", "name:en", "name:zh", "operator", "man_made", "industrial",
        "landuse", "waterway", "harbour", "railway", "seamark:type",
        "seamark:berth:category", "product", "resource", "usage", "service"]


def verken(site, toon_max=40):
    lat0, lon0 = site["midden"]
    print(f"\n{'=' * 78}\n{site['id']} · {site['naam']}")
    print(f"  midden {lat0} / {lon0} · straal {site['straal'] / 1000:.0f} km · {site['waarom']}")
    antwoord = fw.overpass(query_voor(site))
    els = antwoord.get("elements", [])

    rijen = []
    for el in els:
        c = el.get("center") or ({"lat": el.get("lat"), "lon": el.get("lon")})
        if c.get("lat") is None or c.get("lon") is None:
            continue
        tags = el.get("tags", {}) or {}
        rijen.append({
            "type": el["type"], "id": el["id"],
            "lat": round(c["lat"], 5), "lon": round(c["lon"], 5),
            "km": round(km(lat0, lon0, c["lat"], c["lon"]), 2),
            "tags": {k: v for k, v in tags.items() if k in TOON},
            "alle_tags": tags,
        })
    rijen.sort(key=lambda r: r["km"])

    met_naam = [r for r in rijen if r["tags"].get("name") or r["tags"].get("name:en")]
    print(f"  {len(rijen)} objecten · {len(met_naam)} met naam")
    for r in (met_naam or rijen)[:toon_max]:
        t = r["tags"]
        naam = t.get("name:en") or t.get("name") or "(geen naam)"
        rol = " ".join(f"{k}={v}" for k, v in t.items()
                       if k not in ("name", "name:en", "name:zh"))
        print(f"    {r['km']:6.2f} km  {r['lat']:9.5f} {r['lon']:10.5f}  "
              f"{naam[:44]:44s}  {rol[:70]}")
    return rijen


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--site", help="alleen deze site (id)")
    p.add_argument("--schrijf", action="store_true",
                   help="dump de ruwe kandidaten naar build-cache/terminals/")
    p.add_argument("--max", type=int, default=40, help="hoeveel rijen tonen per site")
    a = p.parse_args()

    sites = [s for s in SITES if not a.site or s["id"] == a.site]
    if not sites:
        raise SystemExit(f"onbekende site: {a.site} (kies uit {[s['id'] for s in SITES]})")

    alles = {}
    for s in sites:
        try:
            alles[s["id"]] = verken(s, a.max)
        except Exception as e:  # noqa: BLE001 — één site mag de rest niet slopen
            print(f"  ⚠️ {s['id']} faalde: {e}")

    if a.schrijf:
        UIT.mkdir(parents=True, exist_ok=True)
        for sid, rijen in alles.items():
            pad = UIT / f"{sid}.json"
            pad.write_text(json.dumps(rijen, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"  → {pad} ({len(rijen)} objecten)")


if __name__ == "__main__":
    main()
