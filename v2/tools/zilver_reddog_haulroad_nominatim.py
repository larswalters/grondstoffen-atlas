#!/usr/bin/env python3
"""zilver_reddog_haulroad_nominatim.py — b1 van zilver-reddog-trail uit OSM-ways via Nominatim.

WAAROM DIT BESTAAT (2026-10-09, M31 golf 7). Het profiel "zilver-reddog-trail-reddog-delong" in
maak_stroombeen_weg.py is de gewone route, maar die draait niet: pyosmium (osmium) is op deze machine
geblokkeerd door toepassingsbeheer en alle Overpass-spiegels gaven 500/403/verbroken verbinding. Het
net blijft echter OSM: de Red Dog Mine Road (= DMTS-haulroad, highway=tertiary) staat in OSM als zes
benoemde ways, en Nominatim (lookup, polygon_geojson=1) levert hun volledige geometrie. Dit script
haalt die ways op, ketent ze op hun eindpunten (naad < 100 m, anders harde fout) en schrijft één
LineString — mijn-anker aan de ene, Port Site-anker aan de andere kant met een korte ankerstub (zoals
maak_stroombeen_weg.py). Geen coordinaat is verzonnen; elk punt komt uit een OSM-way.

Gebruik (repo-root):  python v2/tools/zilver_reddog_haulroad_nominatim.py
Uitvoer: v2/build-cache/ais/graaf/zilver-reddog-trail-weg-reddog-delong.geojson
"""
import json, math, sys, time, urllib.request
from pathlib import Path

WAYS = [406680950, 406682670, 406680951, 1216571725, 1216571731, 1216384800]  # mijn -> Port Site
MIJN = (-162.8591, 68.0724)      # (lon, lat) ag-reddog-mijn
DELONG = (-164.0424, 67.5817)    # (lon, lat) ag-reddog-delong
UIT = Path("v2/build-cache/ais/graaf/zilver-reddog-trail-weg-reddog-delong.geojson")
H = {"User-Agent": "grondstoffen-atlas-bak/1.0"}


def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[1], a[0], b[1], b[0]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))


def km(c):
    return sum(hav(c[i], c[i + 1]) for i in range(len(c) - 1))


def trim_staart(c, anker):
    """Knip de lijn op de projectie van het anker op de weg (zoals trimStaart in maak_stroombeen_weg.py):
    de laatste OSM-way loopt ~1 km voorbij het Port Site-anker door; zonder knip rijdt het been voorbij
    en keert het terug (overschiet-en-terug, toets_knikken: TERUGLOOP)."""
    kx = math.cos(math.radians(anker[1])) * 111.195
    best = (1e9, 0, 0.0)
    for i in range(len(c) - 1):
        ax, ay = (c[i][0] - anker[0]) * kx, (c[i][1] - anker[1]) * 111.195
        bx, by = (c[i + 1][0] - anker[0]) * kx, (c[i + 1][1] - anker[1]) * 111.195
        dx, dy = bx - ax, by - ay
        L = dx * dx + dy * dy
        t = 0.0 if L == 0 else max(0.0, min(1.0, -(ax * dx + ay * dy) / L))
        d = math.hypot(ax + t * dx, ay + t * dy)
        if d < best[0]:
            best = (d, i, t)
    d, i, t = best
    p = (c[i][0] + (c[i + 1][0] - c[i][0]) * t, c[i][1] + (c[i + 1][1] - c[i][1]) * t)
    print(f"trim: anker {d:.3f} km van de weg; {km(c) - km(c[:i + 1] + [p]):.2f} km voorbij het anker weggeknipt")
    return c[:i + 1] + [p]


def main():
    u = "https://nominatim.openstreetmap.org/lookup?osm_ids=" + ",".join(f"W{i}" for i in WAYS) + \
        "&format=jsonv2&polygon_geojson=1"
    r = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=90))
    ways = {x["osm_id"]: x["geojson"]["coordinates"] for x in r if x["geojson"]["type"] == "LineString"}
    ontbreekt = [i for i in WAYS if i not in ways]
    if ontbreekt:
        sys.exit(f"ways niet teruggekomen uit Nominatim: {ontbreekt}")
    lijn = []
    for i in WAYS:
        c = [tuple(p) for p in ways[i]]
        if not lijn:
            # eerste way: oriënteer zodat het uiteinde dicht bij de mijn aan het begin ligt
            if hav(c[-1], MIJN) < hav(c[0], MIJN):
                c = c[::-1]
            lijn = c
            print(f"W{i}: begin op {hav(lijn[0], MIJN):.3f} km van het mijnanker")
            continue
        if hav(lijn[-1], c[-1]) < hav(lijn[-1], c[0]):
            c = c[::-1]
        naad = hav(lijn[-1], c[0])
        print(f"W{i}: {len(c)} punten, {km(c):.2f} km, naad {naad*1000:.0f} m")
        if naad > 0.1:
            sys.exit(f"naad {naad:.3f} km > 100 m bij W{i}: ketting niet doorlopend")
        lijn.extend(c[1:] if naad < 0.002 else c)
    lijn = trim_staart(lijn, DELONG)
    a0 = hav(MIJN, lijn[0]); a1 = hav(lijn[-1], DELONG)
    print(f"ankerstub mijn {a0:.3f} km · ankerstub Port Site {a1:.3f} km")
    volledig = [MIJN] + lijn + [DELONG]
    tot = km(volledig)
    print(f"totaal {tot:.2f} km (waarvan OSM-ways {km(lijn):.2f}), {len(volledig)} punten")
    UIT.parent.mkdir(parents=True, exist_ok=True)
    UIT.write_text(json.dumps({"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"id": "ag-reddog-delong", "naam": "Red Dog Mine Road = DMTS-haulroad (OSM-ways via Nominatim)",
                       "modaliteit": "truck", "km": round(tot, 3), "kmWeg": round(km(lijn), 3),
                       "kmAanloopVan": round(a0, 3), "kmAanloopNaar": round(a1, 3), "gepubliceerdKm": 84,
                       "osm_ways": WAYS, "bron": "Nominatim lookup polygon_geojson=1 (OSM, ODbL)"},
        "geometry": {"type": "LineString", "coordinates": [[round(x, 6), round(y, 6)] for x, y in volledig]},
    }]}), encoding="utf-8")
    print("geschreven:", UIT)


if __name__ == "__main__":
    main()
