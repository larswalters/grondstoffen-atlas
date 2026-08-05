#!/usr/bin/env python3
"""
toets_rechte_benen.py — de VERDACHTENLIJST: welke gebakken benen zijn een rechte
lijn tussen twee punten, en hoeveel fout kan daarin verstopt zitten?

WAAROM DIT BESTAAT. Op 2026-08-05 bleek de slurryleiding Escondida → Coloso een
kaarsrechte lijn van 153,5 km, terwijl de werkelijke leiding er op zijn slechtste
punt **15,41 km** naast ligt. Beide ANKERS waren satelliet-gelegd en correct —
en juist daardoor viel het jarenlang niet op: de uiteinden klopten, dus zag het
been er goed uit. De les die eruit volgt is generiek:

    TWEE JUISTE ANKERS ZEGGEN NIETS OVER DE LIJN ERTUSSEN.

De maat die het verraadt is de **omwegfactor** (afgelegde lengte ÷ hemelsbrede
afstand tussen de uiteinden). Vergelijk:

    Escondida-leiding, vóór de correctie :    2 punten · factor 1,000   ← fout
    Collahuasi-leiding (OSM-geometrie)   : 1363 punten · factor 1,188   ← goed

Een factor van precies 1,000 betekent: dit been beweert een rechte lijn te zijn.
Soms klópt dat (een schematische haven-aanloop, een overslag van 300 m op één
terrein); soms is het een niet-onderzochte gok van 150 km. Het verschil zit in de
LENGTE — hoe langer de rechte lijn, hoe meer werkelijkheid erin kan verdwijnen.

WAT DIT TOOL NIET DOET. Het weet niet of een rechte lijn juist is; het wijst aan
wáár er een kan schuilen. Een stippel van 85 km die als eindvorm is vastgelegd
(Chili heeft nul havens met varend AIS-verkeer) blijft hier bovenaan staan, en
dat hoort — het oordeel is redactioneel, de meting is mechanisch. Vandaar de
kolom `oordeel`: die vul je in de routebrief in, niet hier.

    python v2/tools/toets_rechte_benen.py [--min-km 5] [--alles]
"""
import argparse
import glob
import json
import math
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # …/v2
DATA = os.path.join(WORTEL, "data")
R = 6371.0088


def km(a, b):
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def beoordeel(been, lengte, factor, punten):
    """Grof gesorteerd naar hoeveel werkelijkheid er in kan verdwijnen."""
    recht = punten <= 2 or factor < 1.005
    if not recht:
        return None
    stippel = bool(been.get("stippel"))
    if lengte >= 25:
        return "🔴 GROOT" if not stippel else "🟠 GROOT (stippel)"
    if lengte >= 5:
        return "🟠 MIDDEL" if not stippel else "🟡 MIDDEL (stippel)"
    return "🟢 KLEIN"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-km", type=float, default=1.0,
                    help="benen korter dan dit niet tonen (default 1 km)")
    ap.add_argument("--alles", action="store_true",
                    help="ook de benen die géén rechte lijn zijn")
    a = ap.parse_args()

    rijen = []
    for pad in sorted(glob.glob(os.path.join(DATA, "stroomroute-*.json"))):
        d = json.load(open(pad, encoding="utf-8"))
        stroom = d.get("stroom") or os.path.basename(pad)
        for i, been in enumerate(d.get("benen", [])):
            pts = been["punten"]
            if len(pts) < 2:
                continue
            lengte = been.get("km") or sum(km(pts[j], pts[j + 1])
                                           for j in range(len(pts) - 1))
            hemel = km(pts[0], pts[-1])
            factor = lengte / hemel if hemel > 0 else float("inf")
            oordeel = beoordeel(been, lengte, factor, len(pts))
            if oordeel is None and not a.alles:
                continue
            if lengte < a.min_km:
                continue
            rijen.append((lengte, oordeel or "—", stroom, i + 1, been["modaliteit"],
                          len(pts), factor, bool(been.get("stippel")), been["naam"]))

    rijen.sort(key=lambda r: -r[0])
    print(f"{'':2}{'km':>9}  {'verdenking':<18} {'stroom':<32} {'been':>4} "
          f"{'mod':<10} {'pt':>5} {'factor':>7}  naam")
    print("─" * 150)
    for lengte, oordeel, stroom, i, mod, n, factor, stippel, naam in rijen:
        f = "∞" if factor == float("inf") else f"{factor:.3f}"
        print(f"  {lengte:9.1f}  {oordeel:<18} {stroom:<32} {i:>4} "
              f"{mod:<10} {n:>5} {f:>7}  {'· ' if stippel else '  '}{naam[:60]}")

    recht = [r for r in rijen if r[1] != "—"]
    groot = [r for r in recht if "GROOT" in r[1]]
    print("─" * 150)
    print(f"{len(recht)} rechte benen ≥ {a.min_km:g} km, samen {sum(r[0] for r in recht):.0f} km · "
          f"waarvan {len(groot)} ≥ 25 km ({sum(r[0] for r in groot):.0f} km)")
    print("· = gestippeld (de kaart claimt hier géén kennis van de lijn)")
    print("\n⚠️ Een rechte lijn is niet per se fout — een haven-aanloop over een net dat er niet "
          "is,\n   of een overslag van 300 m op één terrein, hóórt recht te zijn. Wat dit tool "
          "aanwijst is\n   WAAR een niet-onderzochte aanname kan zitten. Het oordeel hoort in de "
          "routebrief.")
    print("\nUITSLAG VAN DE EERSTE RONDE (2026-08-05), als ijkpunt voor de volgende:")
    print("  · geen enkel DOORGETROKKEN been is nog een rechte lijn — de kaart claimt nergens")
    print("    kennis van een lijn die zij niet heeft;")
    print("  · drie rechte stippels bleken tóch werkelijkheid te verbergen, elk langs een andere")
    print("    weg gemeten (zie memory/bugs-and-risks.md):")
    print("      haven-aanloop Nacala   122,3 km — loopt 17,5 km (14%) OVER LAND")
    print("      Wesel-vak (Rijn)        47,3 km — tot 8,19 km van de ECHTE, gekarteerde Rijn")
    print("      haven-aanloop Coloso    85,1 km — loopt  2,1 km  (3%) over land")
    print("  ⚠️ Twee vervolgtoetsen die dit tool zelf NIET doet en die je erbij moet draaien:")
    print("     (a) kruist een ZEE-been land? (shapely tegen ne_10m_land) — voor een binnenvaart-")
    print("         been is die toets betekenisloos: die ligt per definitie ín het landvlak;")
    print("     (b) ligt er een gekarteerde lijn (rivier, leiding, spoor) tussen de uiteinden?")
    print("         'geen AIS-dekking' zegt niets over of de GEOMETRIE bestaat — dat was de fout")
    print("         bij Escondida (gezocht op substance=slurry) en bij Wesel (gezocht op tracks).")


if __name__ == "__main__":
    main()
