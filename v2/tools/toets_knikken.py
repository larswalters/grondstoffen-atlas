"""toets_knikken.py — tel de onmogelijke bochten in de GEBAKKEN stromen.

Waarom dit bestaat, en waarom naast de km-ijking: op 2026-07-28 werd gemeld dat
het spoorbeen Beilun→Guixi van 7 naar 2 knikken ging. Dat cijfer kwam uit
`toets_spoorroute.mjs` — het meetgereedschap — terwijl de lijn die op de bol
staat uit `hecht_marnet.py` komt. Twee artefacten, één gemeten, en het andere is
wat Lars ziet. Deze toets meet daarom UITSLUITEND de gebakken bestanden in
`v2/data/stroomroute-*.json`: precies de punten die de browser tekent.

Dezelfde les als de junctie-telling van 2026-07-29: de lengte-ijking was blind
voor junctieverlies (NL −3,7% en PL +1,2% klopten terwijl 86-88% van de
topologie weg was). Kilometers zeggen niet of de lijn RIJDBAAR is. Een omkering
van 170° met een boogstraal van 4 m is in km bijna gratis en fysiek onmogelijk.

De maat is de BOOGSTRAAL, niet de hoek — dezelfde redenering als in
toets_spoorroute.mjs: 77° met segmenten van 400 m is een krappe maar echte
aansluitboog, 77° met 15 m aan de korte kant is een wissel-spike. R wordt op de
KORTSTE van de twee segmenten gerekend, want daar moet de draai in.

Draaien:
    python v2/tools/toets_knikken.py                 # alle stromen
    python v2/tools/toets_knikken.py --max-omkering 0  # faalt bij >0 omkeringen
"""
import argparse
import glob
import json
import math
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HIER), "data")

KNIK_GR = 60.0      # hieronder is het gewoon een bocht
OMKEER_GR = 150.0   # hierboven rijdt de trein terug waar hij vandaan kwam
MIN_BOOG_M = 150.0  # onder deze straal ontspoort een goederentrein fysiek


def gc_km(a, b):
    R = 6371.0088
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def peiling(a, b):
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    dl = lo2 - lo1
    return math.degrees(math.atan2(
        math.sin(dl) * math.cos(la2),
        math.cos(la1) * math.sin(la2) - math.sin(la1) * math.cos(la2) * math.cos(dl)))


# ⚠️ NIET ELKE OMKERING IS EEN FOUT — toegevoegd 2026-08-04.
# Deze toets is geboren op SPOOR, waar een trein niet kan omkeren, dus daar is
# elke hoek >= 150° per definitie verzonnen geometrie. Op weg en water ligt dat
# anders: een lus op een klaverblad, een duwstel dat in een DOODLOPEND zijkanaal
# omdraait (Port Allen IRMT) en een sluispassage zijn echte 180°-bochten. Bij de
# grafietbake van 2026-08-04 sprongen de omkeringen 12 → 28 en dat leek een
# regressie; gemeten bleken 3 van de 6 op de truckbenen echte artefacten en de
# rest werkelijkheid.
#
# HET ONDERSCHEID IS MEETBAAR. Neem een venster van ±VENSTER punten om de knik
# en deel de afgelegde lijn door de hemelsbrede afstand. Een echte bocht komt
# ergens uit (verhouding ~1,0-2,0); een TERUGLOOP legt dezelfde weg terug en
# blijft dus ter plaatse (gemeten: 3,0 bij North Little Rock, 10,2 bij Napoleon
# Avenue). Alleen die tweede soort hoort gerepareerd te worden.
#
# ⚠️ DE BAND 2,0-3,0 WAS LEEG TOEN DEZE DREMPEL WERD GEKOZEN, EN DAT IS SINDS
#    2026-08-05 NIET MEER ZO. De lithiumbenen 7 en 8 leverden twee omkeringen op
#    die de toets als TERUGLOOP labelt maar die aantoonbaar WERKELIJKHEID zijn:
#      32.06949, 118.93784 · v=2,4 · knooppunt G42 x G2503 bij Nanjing
#      31.01827, 121.15034 · v=2,6 · knooppunt bij Songjiang
#    Beide zijn met Overpass nagekeken: binnen 80 m liggen respectievelijk 2 en 7
#    `motorway_link`-ways. Dat zijn KLAVERBLADLUSSEN — je rijdt er 1.509 m om
#    572 m op te schuiven, en dat is precies wat een vrachtwagen daar doet. De
#    grafietronde stelde dat al vast in woorden ("een klaverbladlus is echt")
#    maar er was toen geen gemeten voorbeeld om de drempel op te ijken.
#
#    De ijkpunten staan nu dus zo:
#      echte bocht        1,0 - 2,0
#      klaverbladlus      2,4 - 2,6   ← NIEUW, gemeten, WERKELIJKHEID
#      echte terugloop    3,0 en 10,2
#    ⚠️ DE DREMPEL BLIJFT BEWUST OP 2,2 STAAN. Hem verhogen naar ~2,8 zou beter
#    scheiden, maar het verandert de uitslag van ÁLLE stromen met terugwerkende
#    kracht (o.a. Port Allen, v=2,2 — een duwstel dat in een doodlopend kanaal
#    keert, en dus vermoedelijk óók werkelijkheid). Dat is een eigen besluit met
#    een eigen meting, geen bijvangst van een bouwronde. Tot dat besluit valt:
#    lees een gemelde terugloop tussen 2,2 en 2,8 als "kijk of het een knooppunt
#    is" en niet als "hier moet iets gerepareerd worden".
TERUGLOOP_V = 2.2
VENSTER = 8


def terugloop_verhouding(punten, i, venster=VENSTER):
    """pad / hemelsbreed over een venster om punt i. Hoog = loopt terug."""
    s = max(0, i - venster)
    e = min(len(punten) - 1, i + venster)
    if e - s < 2:
        return 1.0
    pad = sum(gc_km(punten[j], punten[j + 1]) for j in range(s, e))
    recht = gc_km(punten[s], punten[e])
    return pad / recht if recht > 1e-6 else 99.0


def knikken(punten):
    """[(hoek, boogstraal_m, punt, verhouding)] per richtingswissel >= KNIK_GR.

    `verhouding` wordt alleen berekend voor echte omkeringen (duur genoeg om
    niet voor elke spike te doen) en is 1.0 voor de rest."""
    uit = []
    for i in range(1, len(punten) - 1):
        d1 = gc_km(punten[i - 1], punten[i]) * 1000.0
        d2 = gc_km(punten[i], punten[i + 1]) * 1000.0
        if d1 < 1.0 or d2 < 1.0:          # samenvallende punten: geen richting
            continue
        a = peiling(punten[i - 1], punten[i])
        b = peiling(punten[i], punten[i + 1])
        hoek = abs(((b - a) + 180.0) % 360.0 - 180.0)
        if hoek < KNIK_GR:
            continue
        kort = min(d1, d2)
        straal = (kort / (2.0 * math.sin(math.radians(hoek) / 2.0))
                  if hoek < 179.0 else 0.0)
        v = terugloop_verhouding(punten, i) if hoek >= OMKEER_GR else 1.0
        uit.append((hoek, straal, punten[i], v))
    return uit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-omkering", type=int, default=None,
                    help="faal (exit 1) bij meer omkeringen dan dit over alles")
    ap.add_argument("--bestand", default=None, help="één stroombestand i.p.v. alle")
    args = ap.parse_args()

    paden = ([args.bestand] if args.bestand
             else sorted(glob.glob(os.path.join(DATA, "stroomroute-*.json"))))
    if not paden:
        sys.exit("geen stroomroute-*.json in v2/data — niets te toetsen")

    tot_knik = tot_omkeer = tot_terug = 0
    for pad in paden:
        d = json.load(open(pad, encoding="utf-8"))
        print(f"\n=== {os.path.basename(pad)}  (gebakken {d.get('gemaakt', '?')})")
        for been in d.get("benen", []):
            pts = been["punten"]
            if been.get("stippel") or len(pts) < 3:
                continue                   # een stippel is per definitie recht
            ks = knikken(pts)
            omk = [k for k in ks if k[0] >= OMKEER_GR]
            terug = [k for k in omk if k[3] >= TERUGLOOP_V]
            tot_knik += len(ks)
            tot_omkeer += len(omk)
            tot_terug += len(terug)
            vlag = "  <-- TERUGLOOP" if terug else ""
            print(f"  [{been['modaliteit']:<12}] {been.get('km', 0):8.1f} km · "
                  f"{len(pts):5d} pt · knikken {len(ks)} · omkeringen "
                  f"{len(omk)} (waarvan terugloop {len(terug)}){vlag}")
            for hoek, straal, p, v in sorted(ks, key=lambda x: -x[0]):
                if hoek >= OMKEER_GR:
                    soort = (f"TERUGLOOP (v={v:.1f})" if v >= TERUGLOOP_V
                             else f"scherpe bocht, echt (v={v:.1f})")
                else:
                    soort = "spike" if straal < MIN_BOOG_M else "krappe bocht"
                print(f"        {hoek:5.1f} gr · R {straal:7.0f} m · "
                      f"{p[1]:.5f},{p[0]:.5f} · {soort}")

    print(f"\nTOTAAL: {tot_knik} knikken >= {KNIK_GR:.0f} gr, waarvan "
          f"{tot_omkeer} omkeringen >= {OMKEER_GR:.0f} gr, "
          f"waarvan {tot_terug} TERUGLOOP (de enige die gerepareerd horen te worden)")
    if args.max_omkering is not None and tot_omkeer > args.max_omkering:
        sys.exit(f"FAAL: {tot_omkeer} omkeringen, toegestaan {args.max_omkering}")


if __name__ == "__main__":
    main()
