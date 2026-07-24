#!/usr/bin/env python3
"""maak_tongling_oostgeul.py — HAND-GEPLAATSTE middellijn van de Tongling-oostgeul.

Waarom hand-geplaatst i.p.v. afgeleid uit de watervlakken:

  OSM legt de navigeerbare Yangtze-middellijn bij Tongling langs de WESTgeul om
  het eiland (`waterway=长江`, way 226556520). De kade van de nieuwe Tongling
  Nonferrous-kopersmelter ligt aan de OOSTgeul, tussen het eiland en de stad
  (kade 117,772 / 30,987). Die oostgeul is in OSM alléén `natural=water`-vlak,
  géén eigen `waterway`-lijn — en dat vlak is een gevlochten U rond een
  mid-river zandbank: de kade en de noordoost-junctie liggen beide onderaan en
  hebben in OSM alléén water-verbinding via de top (~27 km "om de lus"). Elke
  automatische afleiding (middellijn_uit_vlakken.py, elke klaring-drempel t/m
  ~30 m) geeft daarom die lange lus, niet de rechte geul waar de schepen in het
  echt varen (Lars' satellietbeeld + rode schets, 2026-07-24).

  Daarom plaatsen we de oostgeul-centerline HANDMATIG langs het werkelijke
  vaarkanaal: kade → recht noordoost langs de oostoever van het eiland → de
  noordoost-junctie op de hoofdgeul (117,897 / 31,0765, hetzelfde aansluitpunt
  dat de router al gebruikt). De router komt van benedenstrooms (Shanghai, NO)
  de hoofdgeul af, gaat bij die junctie de oostgeul in en zakt recht naar de
  kade. Eén aansluitpunt op de hoofdgeul (zoals voorheen) → geen eiland-lus.

Uitvoer: v2/data/vaarwegen-handmatig.geojson (gecommit, klein). Bakken:
    python v2/tools/bake_marnet.py --binnenwater \
        --bulk build-cache/vaarwegen_bulk.geojson \
        --extra-vaarwegen data/vaarwegen-handmatig.geojson \
        --bruggen build-cache/vaarwegen_bruggen.geojson \
        --meren build-cache/vaarwegen_meren.geojson \
        --heal-km 0.25 --corridor-km 2.0
"""

import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)

# Hand-geplaatste centerline langs de werkelijke oostgeul (Lars' rode lijn),
# kade → noordoost-junctie op de Yangtze. Punten liggen op het vaarkanaal
# tussen het eiland en de stad; het middenstuk kruist een mid-river zandbank
# die OSM als land kaart maar die op de satelliet open water is.
LIJN = [
    (117.7718, 30.98656),   # kade (aansluiting cu-tongling-kade)
    (117.780, 30.998),
    (117.792, 31.010),
    (117.804, 31.023),
    (117.816, 31.036),
    (117.830, 31.048),
    (117.847, 31.056),
    (117.865, 31.062),
    (117.881, 31.067),
    (117.897, 31.0765),     # noordoost-junctie op de hoofdgeul (way 226556520)
]


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[1], a[0], b[1], b[0]))
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * 6371 * math.asin(min(1.0, math.sqrt(h)))


def main():
    tot = sum(km(LIJN[i], LIJN[i + 1]) for i in range(len(LIJN) - 1))
    dichtst = min(km((117.7717, 30.98236), p) for p in LIJN)
    print(f"oostgeul (hand-geplaatst): {len(LIJN)} punten · {tot:.1f} km · "
          f"kade-tip op {dichtst:.2f} km")

    feat = {"type": "Feature",
            "properties": {"label": "bulk-cn", "regio": "cn", "zeevaart": False,
                           "signaal": "ship", "km": round(tot, 3),
                           "wayId": "tongling-oostgeul",
                           "bron": "HAND-geplaatste centerline langs de werkelijke "
                                   "Tongling-oostgeul (kade → NO-junctie 117,897/31,0765 "
                                   "op de Yangtze-hoofdgeul). OSM kaart deze oostgeul "
                                   "alleen als natural=water-vlak (gevlochten U rond een "
                                   "zandbank), geen navigeerbare waterway-lijn; automatisch "
                                   "afleiden gaf altijd de 27 km-lus. Plek geverifieerd op "
                                   "satelliet (Lars, 2026-07-24)."},
            "geometry": {"type": "LineString",
                         "coordinates": [[round(p[0], 5), round(p[1], 5)] for p in LIJN]}}
    out = {"type": "FeatureCollection",
           "toelichting": "Handmatig geplaatste vaarweglijnen (niet uit de OSM-fetch). "
                          "Herleiden: tools/maak_tongling_oostgeul.py. Voeg toe met "
                          "bake_marnet.py --extra-vaarwegen.",
           "features": [feat]}
    pad_uit = os.path.join(V2, "data", "vaarwegen-handmatig.geojson")
    json.dump(out, open(pad_uit, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"geschreven: {pad_uit}")


if __name__ == "__main__":
    main()
