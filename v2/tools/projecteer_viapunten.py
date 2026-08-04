#!/usr/bin/env python3
"""
projecteer_viapunten.py — schuif een via-punt van een AFRIT naar de DOORGAANDE
RIJBAAN.

WAAROM. Een via-punt dat niet op de doorgaande rijbaan ligt maar op een
verbindingsboog (`highway=*_link`) of op een zijtak, levert een 180°-keerpunt:
de Dijkstra rijdt hem in en er weer uit over dezelfde edge. Gemeten in de
grafietbake van 2026-08-04: zes omkeringen op de twee lange truckbenen, ALLE
exact op een via-punt — Joplin (177,1°), North Little Rock (163,6°), Lenexa
(163,4°) en K-10 × K-7 (180,0° met straal 0 m).

Dezelfde klasse als de dorpsknopen in de lithiumbrief (Balingup, Picton,
Willinge Drive): OSM-knopen liggen 23-143 m náást de highway. De fix daar was
`snoei_keerlussen`, maar dat ruimt de LUS op en niet de OORZAAK — en bij een
knooppunt is de lus vaak langer dan het snoeivenster van 25 m. Beter is het
via-punt zelf goed leggen.

WAT DIT DOET. Zoekt in een lokale Geofabrik-extract de dichtstbijzijnde vertex
op een way die
  * een doorgaande wegklasse draagt (motorway/trunk/primary/secondary), en
  * NADRUKKELIJK GEEN `_link` is — dat ís de afrit, en dat is precies wat we
    willen vermijden, en
  * optioneel een van de opgegeven `ref`-nummers draagt (bv. 49, I 49, I-49).

⚠️ HET VERPLAATST NIETS OP GEVOEL. De uitvoer is een voorstel mét afstand; de
maker zet hem zelf in het profiel. Ligt het voorstel ver weg (>500 m), dan is
er iets anders aan de hand dan een afrit — kijk dan eerst.

⚠️ DIT IS GEEN VERVANGER VAN snoei_keerlussen. Die blijft nodig voor lussen die
uit de geometrie zelf komen; dit gereedschap haalt de oorzaak weg waar die in
een aangewezen punt zit.

Draaien (vanuit de repo-root):
  python v2/tools/projecteer_viapunten.py --extract us-missouri \
      --punt 37.06340,-94.42085 --refs 49 44
  python v2/tools/projecteer_viapunten.py --extract us-kansas \
      --punt 38.94101,-94.85289 --refs 10 7 --straal-km 2
"""

import argparse
import math
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(os.path.dirname(HERE), "build-cache", "geofabrik")

DOORGAAND = ("motorway", "trunk", "primary", "secondary")


def km(a, b):
    """Haversine tussen (lon, lat)-paren."""
    R = 6371.0088
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def _extract_pad(naam):
    for kand in (f"{naam}-latest.osm.pbf", f"{naam}.osm.pbf"):
        p = os.path.join(CACHE, kand)
        if os.path.exists(p):
            return p
    raise SystemExit(f"extract niet gevonden in {CACHE}: {naam}")


def _ref_matcht(ref_tag, refs):
    """OSM schrijft refs als 'I 49', 'US 425', 'K-10', of 'I 49;US 71'."""
    if not refs:
        return True
    if not ref_tag:
        return False
    los = [s.strip() for s in ref_tag.replace("-", " ").split(";")]
    for stuk in los:
        cijfers = "".join(c for c in stuk if c.isdigit())
        if cijfers and cijfers in refs:
            return True
    return False


def zoek(extract, punt, refs, straal_km):
    import osmium

    lon0, lat0 = punt[0], punt[1]
    d = straal_km / 111.0
    bbox = (lon0 - d / max(math.cos(math.radians(lat0)), 0.2), lat0 - d,
            lon0 + d / max(math.cos(math.radians(lat0)), 0.2), lat0 + d)

    class Knopen(osmium.SimpleHandler):
        """Pas 1 — alleen de knopen in het venster; dat is een kleine dict."""

        def __init__(self):
            super().__init__()
            self.pos = {}

        def node(self, n):
            lo, la = n.location.lon, n.location.lat
            if bbox[0] <= lo <= bbox[2] and bbox[1] <= la <= bbox[3]:
                self.pos[n.id] = (lo, la)

    class Wegen(osmium.SimpleHandler):
        """Pas 2 — de ways, gefilterd op klasse, link en ref."""

        def __init__(self, pos):
            super().__init__()
            self.pos = pos
            self.treffers = []

        def way(self, w):
            hw = (w.tags.get("highway") or "").strip()
            if hw not in DOORGAAND:
                return                      # ⚠️ *_link valt hier per definitie af
            if not _ref_matcht(w.tags.get("ref"), refs):
                return
            naam = w.tags.get("ref") or w.tags.get("name") or hw
            for nd in w.nodes:
                p = self.pos.get(nd.ref)
                if p is not None:
                    self.treffers.append((km(p, punt), p, naam, hw, w.id))

    pad = _extract_pad(extract)
    print(f"extract: {os.path.basename(pad)}  ·  venster {straal_km:g} km")
    kn = Knopen()
    kn.apply_file(pad, locations=False)
    print(f"  knopen in het venster: {len(kn.pos):,}")
    wg = Wegen(kn.pos)
    wg.apply_file(pad, locations=False)
    wg.treffers.sort(key=lambda t: t[0])
    return wg.treffers


def main():
    ap = argparse.ArgumentParser(
        description="schuif een via-punt naar de doorgaande rijbaan")
    ap.add_argument("--extract", required=True,
                    help="naam van de Geofabrik-extract, bv. us-missouri")
    ap.add_argument("--punt", required=True, help="LAT,LON van het huidige via-punt")
    ap.add_argument("--refs", nargs="*", default=[],
                    help="wegnummers die de doorgaande route draagt, bv. 49 44")
    ap.add_argument("--straal-km", type=float, default=3.0)
    ap.add_argument("--toon", type=int, default=5)
    a = ap.parse_args()

    lat, lon = (float(x) for x in a.punt.split(","))
    refs = ["".join(c for c in r if c.isdigit()) for r in a.refs]
    refs = [r for r in refs if r]

    treffers = zoek(a.extract, (lon, lat), refs, a.straal_km)
    if not treffers:
        print("  GEEN doorgaande rijbaan gevonden binnen het venster — "
              "vergroot --straal-km of controleer de refs.")
        return

    print(f"  kandidaten op een doorgaande rijbaan (geen *_link):")
    gezien = set()
    n = 0
    for afst, p, naam, hw, wid in treffers:
        sleutel = (round(p[0], 5), round(p[1], 5))
        if sleutel in gezien:
            continue
        gezien.add(sleutel)
        n += 1
        vlag = "" if afst <= 0.5 else "   ⚠️ ver — kijk eerst zelf"
        print(f"    {afst*1000:7.0f} m  ({p[1]:.5f}, {p[0]:.5f})  "
              f"{naam:12s} {hw:10s} way {wid}{vlag}")
        if n >= a.toon:
            break
    beste = treffers[0]
    print()
    print(f"  VOORSTEL voor het profiel (lon, lat):  "
          f"({beste[1][0]:.5f}, {beste[1][1]:.5f})   "
          f"— {beste[0]*1000:.0f} m van het huidige punt")


if __name__ == "__main__":
    main()
