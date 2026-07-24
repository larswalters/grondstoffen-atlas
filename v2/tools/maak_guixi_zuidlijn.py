#!/usr/bin/env python3
"""maak_guixi_zuidlijn.py — HAND-GEPLAATST middenstuk van de 贵溪站-专用线
(de eigen aansluitlijn van station Guixi naar de Jiangxi Copper-smelter).

Waarom hand-geplaatst i.p.v. uit OSM:

  De smelter heeft in het echt TWEE spooraansluitingen (2026-07-24 nagetrokken):
  贵溪站 (zuid, aan de 沪昆-hoofdlijn) heeft blijkens zh.wikipedia een 专用线
  naar de fabriek — erts ín; en 贵溪北 (noord, 皖赣线) doet de treinvorming
  voor uitgaand kathode/zwavelzuur/slak, ±3 Mt/jaar (Xinhua, 40 jaar 皖赣).

  OSM mapt beide UITEINDEN van de zuidelijke 专用线 (de yard-strengen bij het
  station én de fabriekstrengen op ~28.327), maar mist het middenstuk van
  ±2,3 km door de velden — terwijl het tracé op de satellietfoto (Esri World
  Imagery, dezelfde tegels als de atlas) van anker tot anker zichtbaar
  doorloopt. Zonder dit stuk kan de stroom de fabriek alleen via de
  noordwest-keel bereiken en tekent hij een lus om de fabriek heen (Lars'
  screenshots). Dit is dezelfde klasse als de Tongling-oostgeul: de bron mist
  een lijn die er aantoonbaar ligt, dus leggen we hem handmatig, mét bron.

  De EINDPUNTEN zijn letterlijk (op de float) de eindvertices van de gemapte
  OSM-snippers — de bake last uitsluitend op exact gedeelde coördinaten, dus
  precies deze twee punten hechten de lijn per constructie aan het net:
    zuid  [117.220748, 28.306619]  = noordeind way 472264816 (yard-klim)
    noord [117.229789, 28.32701]   = oosteind way 995766154 (fabriekstreng)
  De tussenpunten zijn overgetrokken van de satelliet (z17).

Uitvoer: v2/data/landnet-handmatig.geojson (gecommit, klein).
Bakken:  bake_landnet.laad_lijnen() leest dit bestand automatisch mee.
"""

import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)

# zuid-anker → satelliet-tussenpunten → noord-anker (WGS84 lon/lat)
PUNTEN = [
    [117.220748, 28.306619],   # EXACT: noordeind OSM-way 472264816
    [117.2210, 28.3077],
    [117.2217, 28.3106],
    [117.2226, 28.3129],
    [117.2236, 28.3153],
    [117.2248, 28.3175],
    [117.2260, 28.3195],
    [117.2272, 28.3213],
    [117.2283, 28.3230],
    [117.2292, 28.3245],
    [117.2301, 28.3257],
    [117.229789, 28.32701],    # EXACT: oosteind OSM-way 995766154
]


def gc_km(a, b):
    r = math.pi / 180
    d = (math.sin(a[1] * r) * math.sin(b[1] * r) +
         math.cos(a[1] * r) * math.cos(b[1] * r) * math.cos((b[0] - a[0]) * r))
    return 6371 * math.acos(max(-1.0, min(1.0, d)))


def main():
    km = sum(gc_km(PUNTEN[i], PUNTEN[i + 1]) for i in range(len(PUNTEN) - 1))
    gj = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": {
                "label": "spoor-handmatig",
                "regio": "cn",
                "modus": "spoor",
                "gauge": "1435",
                "naam": "贵溪站-专用线 middenstuk (Jiangxi Copper, hand-geplaatst)",
                "bron": ("satelliet-overtrek Esri World Imagery (z17); uiteinden = "
                         "exacte OSM-vertices ways 472264816/995766154 (ODbL). "
                         "Bestaan 专用线: zh.wikipedia 贵溪站; rol 贵溪北: Xinhua "
                         "皖赣铁路 40 jaar (2024-06-02)."),
                "km": round(km, 3),
            },
            "geometry": {"type": "LineString", "coordinates": PUNTEN},
        }],
    }
    uit = os.path.join(V2, "data", "landnet-handmatig.geojson")
    with open(uit, "w", encoding="utf-8") as f:
        json.dump(gj, f, ensure_ascii=False, indent=1)
    print(f"geschreven: {uit} · {km:.2f} km · {len(PUNTEN)} punten")


if __name__ == "__main__":
    main()
