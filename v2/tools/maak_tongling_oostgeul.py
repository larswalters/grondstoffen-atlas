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

# De oostgeul zoals Lars hem met stippen op de satelliet aanwees (2026-07-24):
# van de ZUID-junctie op de hoofdgeul, noordwaarts dóór de geul langs de kade,
# naar de NOORD-junctie op de hoofdgeul. Beide uiteinden zijn exacte vertices
# van way 226556520 (长江), zodat de bake er een gedeelde knoop van maakt.
# ⚠️ NIET diagonaal oversteken naar de oostelijke junctie (v073-fout: snijdt
# dwars over het eiland) en NIET de 27 km-lus om de top (v070).
# Elk punt is met de hand op de Esri-satelliet (z14, grid 0,01°) in het MIDDEN
# van de vaargeul gelegd — de v074-punten hingen tegen het mid-riviereiland
# (31,05–31,07), de oostoever (31,03) en liepen zuid van de kade over het
# landbouweiland heen (30,93–30,96, daar ligt de geul óóstelijk van het eiland).
LIJN = [
    (117.7373, 30.9102),    # zuid-junctie op de hoofdgeul (vertex [2])
    (117.7480, 30.9230),
    (117.7590, 30.9320),
    (117.7692, 30.9410),
    (117.7713, 30.9540),
    (117.7700, 30.9640),
    (117.7687, 30.9700),
    (117.7690, 30.9790),
    (117.7718, 30.98656),   # kade (aansluiting cu-tongling-kade)
    (117.7700, 30.9990),
    (117.7680, 31.0130),
    (117.7655, 31.0280),
    (117.7648, 31.0430),
    (117.7670, 31.0580),
    (117.7670, 31.0730),
    (117.7660, 31.0880),
    (117.7660, 31.1000),
    (117.7696, 31.1091),    # noord-junctie op de hoofdgeul (vertex [7])
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
                           "bron": "Tongling-oostgeul noordwaarts: kade → door de geul "
                                   "→ junctie op de Yangtze-hoofdgeul bij de NOORDPUNT "
                                   "(117,8016/31,1331, vertex van way 226556520). Punten "
                                   "t/m 31,0975 water-constrained afgeleid uit "
                                   "natural=water (China-extract, ODbL, v070-afleiding); "
                                   "OSM heeft geen waterway-middellijn voor deze geul. "
                                   "Tracé geverifieerd op satelliet (Lars, 2026-07-24)."},
            "geometry": {"type": "LineString",
                         "coordinates": [[round(p[0], 5), round(p[1], 5)] for p in LIJN]}}
    # Knip-instructie: de WEST-arm van way 226556520 (长江) tussen onze twee
    # juncties eruit — OSM legt de hoofdgeul om de westkant van het eiland,
    # maar de schepen varen de oostgeul (Lars' satelliet-check, 2026-07-24).
    # De rivier loopt na de knip via de oostgeul-lijn hierboven door; kop
    # (zuid van vertex [2]) en staart (noord van vertex [7]) blijven staan.
    knip = {"type": "Feature",
            "properties": {"label": "bulk-cn", "knipWayId": 226556520,
                           "bron": "verwijder de west-arm om het Tongling-eiland "
                                   "(schepen varen de oostgeul; zie de lijn hierboven)"},
            "geometry": {"type": "LineString",
                         "coordinates": [[117.7373, 30.9102], [117.7696, 31.1091]]}}
    out = {"type": "FeatureCollection",
           "toelichting": "Handmatig geplaatste vaarweglijnen + knip-instructies "
                          "(niet uit de OSM-fetch). Herleiden: "
                          "tools/maak_tongling_oostgeul.py. Voeg toe met "
                          "bake_marnet.py --extra-vaarwegen.",
           "features": [feat, knip]}
    pad_uit = os.path.join(V2, "data", "vaarwegen-handmatig.geojson")
    json.dump(out, open(pad_uit, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"geschreven: {pad_uit}")


if __name__ == "__main__":
    main()
