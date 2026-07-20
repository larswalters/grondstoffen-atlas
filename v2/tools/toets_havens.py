#!/usr/bin/env python
"""toets_havens.py — objectieve kwaliteitstoets op de havenlijst.

WAAROM DIT BESTAAT. Lars zag op de bol stippen op plekken waar geen haven ligt —
een grensovergang in de heuvels, een voorstad, een zandweg — en zei terecht:

    "er zijn er zoveel dat 1 voor 1 controleren niet werkt dus je moet het iets
     anders doen dan controleer ik weer of het dan beter klopt"

Dus moet de machine de objectieve regel bewaken. Deze toets meet per haven of hij
uberhaupt AAN WATER ligt, en vat dat samen in cijfers die voor en na een ingreep
te vergelijken zijn. Zonder zo'n cijfer is "beter" een mening.

WAT ER MIS IS MET DE HUIDIGE BRON. `ports.geojson` uit het pakket `searoute` is
geen havenlijst maar een UN/LOCODE-locatielijst; LOCODE dekt ook vliegvelden,
wegterminals, spoorterminals en grensovergangen. Gemeten: 977 van de 3.962 punten
liggen >10 km landinwaarts, 678 >50 km, diepste 1.771 km (Yining, Xinjiang).

⚠️ MAAR DE LIJST IS ONGEFILTERD, NIET FOUT. Van die 977 diep-landinwaartse punten
zijn er 269 ECHTE RIVIERHAVENS (Chicago, Memphis, Cincinnati, Chongqing, Wuhan,
Kansas City, Boedapest, Bratislava, Straatsburg, Asuncion, Corumba) — precies de
havens die de atlas voor de overslag het hardst nodig heeft. Een toets die alleen
op "ligt landinwaarts" afgaat gooit die weg. Daarom meet deze toets de afstand tot
WATER, niet de afstand tot de kust.

DE MAATSTAF. Per haven: de kleinste van
  (a) de afstand tot de kustlijn  — de rand van de Natural Earth 1:10M landvlakken;
  (b) de afstand tot het riviernet — de rivier-snap uit ports.json.
Een echte haven ligt aan een van beide. Ligt hij aan geen van beide, dan is hij
voor deze atlas inert: er valt niet naartoe en niet vandaan te routeren.

⚠️ Deze toets zegt NIETS over twee andere gebreken, en dat moet zo blijven staan
zodat niemand denkt dat ze zijn opgelost:
  1. de coordinaten zijn plaatscentroides, geen kades — een punt landt op een
     zandweg naast de haven in plaats van aan de steiger;
  2. er is geen enkel attribuut dat een vrachthaven van een jachthaven scheidt.
Allebei vragen een betere bron; filteren lost ze niet op.

Gebruik:
    python tools/toets_havens.py                 # rapport over data/ports.json
    python tools/toets_havens.py --grens 10      # andere afkapwaarde proberen
    python tools/toets_havens.py --lijst 40      # de ergste 40 tonen
"""

import argparse
import json
import math
import os

import numpy as np
from shapely.geometry import shape, Point
from shapely.strtree import STRtree

HIER = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HIER)
DATA = os.path.join(V2, "data")
CACHE = os.path.join(V2, "build-cache")

# Dezelfde vlakken waartegen bake_marnet.py het netwerk verzoent. Dat is geen
# detail: de toets moet tegen DEZELFDE wereld meten als de router, anders meet
# je een verschil tussen twee kaarten in plaats van een fout in de havenlijst.
LANDVLAKKEN = ("ne_10m_land.geojson", "ne_10m_minor_islands.geojson")

# Standaard-afkapwaarde. Ruim genomen: 1:10M-kustlijn is grof, en een haven in
# een estuarium of achter een dam kan er een paar km vandaan liggen zonder dat
# er iets mis is. De rommel die we zoeken zit op honderden km, niet op vijf.
GRENS_KM = 10.0


def laad_land():
    vlakken = []
    for naam in LANDVLAKKEN:
        pad = os.path.join(CACHE, naam)
        if not os.path.exists(pad):
            raise SystemExit(
                f"ontbreekt: {pad}\n"
                "Deze toets meet tegen dezelfde vlakken als de bake; haal ze op "
                "zoals beschreven in de project-CLAUDE.md (build-cache is gitignored)."
            )
        for ft in json.load(open(pad, encoding="utf-8"))["features"]:
            g = shape(ft["geometry"])
            if g.is_valid and not g.is_empty:
                vlakken.append(g)
    return vlakken


def afstand_tot_kust(vlakken, boom, lon, lat):
    """Kilometers tot de dichtstbijzijnde kustlijn, of de haven nu op land of op
    water ligt. Voor een kadepunt is dit ~0; voor Laramie (Wyoming) 1.055."""
    p = Point(lon, lat)
    j = boom.nearest(p)
    g = vlakken[j]
    rand = g.exterior if g.geom_type == "Polygon" else g.boundary
    # graden -> km, met de breedtegraad-correctie op de lon-component. Ruw maar
    # ruim genoeg: we onderscheiden 2 km van 500 km, niet 2,0 van 2,1.
    return rand.distance(p) * 111.0 * max(0.05, math.cos(math.radians(lat)))


def toets(pad_ports, grens_km, toon):
    d = json.load(open(pad_ports, encoding="utf-8"))
    n = d["aantal"]
    heeft_rivier = "afstandRivierKm" in d

    print(f"havenlijst    : {os.path.basename(pad_ports)} · {n:,} punten")
    print(f"bron          : {d.get('bron', 'onbekend')}")
    print(f"afkapwaarde   : {grens_km:.0f} km tot water (kust OF riviernet)\n")

    vlakken = laad_land()
    boom = STRtree(vlakken)
    print(f"landvlakken   : {len(vlakken):,}")

    kust = np.empty(n)
    for i in range(n):
        kust[i] = afstand_tot_kust(vlakken, boom, d["ll"][i * 2], d["ll"][i * 2 + 1])

    rivier = np.array(d["afstandRivierKm"], dtype=float) if heeft_rivier else np.full(n, np.inf)
    rivier[rivier < 0] = np.inf          # -1 = geen riviernet gebakken
    water = np.minimum(kust, rivier)
    zee = np.array(d["afstandKm"], dtype=float)

    print("\n--- verdeling: afstand tot water -------------------------------")
    for g in (1, 2, 5, 10, 25, 50, 100, 250):
        aantal = int((water > g).sum())
        print(f"  verder dan {g:>4} km van water : {aantal:>5,}  ({aantal / n * 100:>5.1f}%)")

    slecht = water > grens_km
    print(f"\n--- oordeel bij {grens_km:.0f} km ----------------------------------------")
    print(f"  AAN WATER (goed)        : {int((~slecht).sum()):>5,}  ({(~slecht).sum() / n * 100:>5.1f}%)")
    print(f"  NIET AAN WATER (inert)  : {int(slecht.sum()):>5,}  ({slecht.sum() / n * 100:>5.1f}%)")

    if heeft_rivier:
        # Waar komt het water vandaan? Dit laat zien hoeveel havens ALLEEN door
        # het riviernet gered worden — dat zijn de binnenhavens, en die zijn de
        # reden dat deze toets niet op "afstand tot de kust" mag draaien.
        via_rivier = (~slecht) & (rivier < kust)
        diep = (~slecht) & (kust > 50)
        print(f"    waarvan gered door het riviernet : {int(via_rivier.sum()):>5,}")
        print(f"    echte binnenhavens (>50 km van de kust, wel aan het riviernet)"
              f" : {int(diep.sum()):>5,}")

    print("\n--- wat deze toets NIET meet -----------------------------------")
    print("  · of het punt op de KADE ligt of op de stadscentroide")
    print("  · of het een vrachthaven is of een jachthaven")
    print("  Beide vragen een betere bron; filteren lost ze niet op.")

    if toon:
        idx = np.argsort(-water)[:toon]
        print(f"\n--- de {toon} punten die het verst van water liggen -------------")
        for i in idx:
            if not np.isfinite(water[i]):
                continue
            print(f"  {d['namen'][i][:24]:<25} {d['landen'][i][:16]:<17} "
                  f"{d['locodes'][i]:<7} water {water[i]:>7.0f} km "
                  f"(kust {kust[i]:>7.0f} · rivier {rivier[i] if np.isfinite(rivier[i]) else -1:>7.1f}) "
                  f"· zee-snap {zee[i]:>7.1f}")

    return water, kust, rivier


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ports", default=os.path.join(DATA, "ports.json"))
    ap.add_argument("--grens", type=float, default=GRENS_KM,
                    help="afkapwaarde in km tot water (default 10)")
    ap.add_argument("--lijst", type=int, default=25,
                    help="hoeveel van de ergste punten tonen (0 = geen)")
    a = ap.parse_args()
    toets(a.ports, a.grens, a.lijst)
