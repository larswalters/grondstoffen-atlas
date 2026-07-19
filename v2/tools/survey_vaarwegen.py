#!/usr/bin/env python3
"""
survey_vaarwegen.py — welke vaarweg-NAMEN liggen er in een venster? (M24-uitrol)

Stap 2 van de uitrol-aanpak uit `v2/design/binnenvaart-uitrol.md`: *namen
opzoeken, niet raden*. Een blinde whitelist ("Yangon River") levert nul
segmenten op terwijl OSM `ရန်ကုန်မြစ်` draagt; en één ontbrekende grensnaam
(`Dunaj / Duna`) knipt een keten stilzwijgend doormidden.

Rangschikt op **totale lengte, niet op vertex-aantal** — die fout zette in de
eerste survey de Rijn op plek 6 en liet Donau/Wolga/Paraná/Amazone helemaal
wegvallen: een brede rivier is vaak als vlak gemapt met een spaarzame
middellijn, terwijl een beek een lange fijn-gemapte lijn is.

De lon/lat-strekking per naam is de tweede helft van het antwoord: daaraan zie
je of de namen samen een DOORLOPEND traject dekken of dat er een gat zit.

Draaien:
  python v2/tools/survey_vaarwegen.py --extracts de-nrw,de-rheinland-pfalz \
      --bbox 47.4,5.8,52.0,8.7 --top 25
  python v2/tools/survey_vaarwegen.py --extracts china --bbox ... --bevat 运河
"""

import argparse
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_waterways import extract_pad, km  # noqa: E402 — zelfde regio-sleutels

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def survey(extracts, bbox, soorten, marge=0.15):
    import osmium

    la0, lo0, la1, lo1 = bbox
    per_naam = {}   # naam -> [km, ways, lo_min, la_min, lo_max, la_max]
    for sleutel in extracts:
        pad = extract_pad(sleutel)
        if not os.path.exists(pad):
            raise SystemExit(f"ontbreekt: {pad}\n  haal 'm op met: "
                             f"python v2/tools/fetch_waterways.py geofabrik --download")
        fp = (osmium.FileProcessor(pad)
              .with_locations()
              .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
              .with_filter(osmium.filter.KeyFilter("waterway")))
        for obj in fp:
            if obj.tags.get("waterway") not in soorten:
                continue
            naam = obj.tags.get("name", "")
            if not naam:
                continue
            pts = [(n.location.lon, n.location.lat) for n in obj.nodes
                   if n.location.valid()]
            # alleen het deel dat het venster raakt telt mee
            binnen = [(lo, la) for lo, la in pts
                      if lo0 - marge <= lo <= lo1 + marge and la0 - marge <= la <= la1 + marge]
            if len(binnen) < 2:
                continue
            r = per_naam.setdefault(naam, [0.0, 0, 999.0, 999.0, -999.0, -999.0])
            r[0] += sum(km(a, b) for a, b in zip(binnen, binnen[1:]))
            r[1] += 1
            for lo, la in binnen:
                r[2], r[3] = min(r[2], lo), min(r[3], la)
                r[4], r[5] = max(r[4], lo), max(r[5], la)
    return per_naam


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--extracts", required=True, help="komma-gescheiden regio-sleutels")
    ap.add_argument("--bbox", required=True, help="lat_min,lon_min,lat_max,lon_max")
    ap.add_argument("--soorten", default="river,canal,fairway")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--bevat", default="", help="filter: naam moet deze tekst bevatten")
    ap.add_argument("--min-km", type=float, default=0.0)
    args = ap.parse_args()

    bbox = tuple(float(x) for x in args.bbox.split(","))
    extracts = [s.strip() for s in args.extracts.split(",")]
    soorten = tuple(s.strip() for s in args.soorten.split(","))
    per_naam = survey(extracts, bbox, soorten)

    rijen = [(naam, *r) for naam, r in per_naam.items()
             if r[0] >= args.min_km and (not args.bevat or args.bevat in naam)]
    rijen.sort(key=lambda r: -r[1])
    print(f"\n{len(per_naam):,} benoemde vaarwegen in het venster; "
          f"{len(rijen)} na filter — top {args.top} op LENGTE:\n")
    print(f"{'naam':<42} {'km':>9} {'ways':>6}  strekking lon / lat")
    for naam, lengte, ways, lo0, la0, lo1, la1 in rijen[:args.top]:
        print(f"{naam[:42]:<42} {lengte:9,.1f} {ways:6d}  "
              f"{lo0:7.3f}…{lo1:7.3f} / {la0:6.3f}…{la1:6.3f}")
