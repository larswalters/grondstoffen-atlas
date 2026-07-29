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


def knikken(punten):
    """[(hoek, boogstraal_m, punt)] voor elke richtingswissel >= KNIK_GR."""
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
        uit.append((hoek, straal, punten[i]))
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

    tot_knik = tot_omkeer = 0
    for pad in paden:
        d = json.load(open(pad, encoding="utf-8"))
        print(f"\n=== {os.path.basename(pad)}  (gebakken {d.get('gemaakt', '?')})")
        for been in d.get("benen", []):
            pts = been["punten"]
            if been.get("stippel") or len(pts) < 3:
                continue                   # een stippel is per definitie recht
            ks = knikken(pts)
            omk = [k for k in ks if k[0] >= OMKEER_GR]
            tot_knik += len(ks)
            tot_omkeer += len(omk)
            vlag = "  <-- OMKERING" if omk else ""
            print(f"  [{been['modaliteit']:<12}] {been.get('km', 0):8.1f} km · "
                  f"{len(pts):5d} pt · knikken {len(ks)} · omkeringen "
                  f"{len(omk)}{vlag}")
            for hoek, straal, p in sorted(ks, key=lambda x: -x[0]):
                soort = ("OMKERING" if hoek >= OMKEER_GR
                         else "spike" if straal < MIN_BOOG_M else "krappe bocht")
                print(f"        {hoek:5.1f} gr · R {straal:7.0f} m · "
                      f"{p[1]:.5f},{p[0]:.5f} · {soort}")

    print(f"\nTOTAAL: {tot_knik} knikken >= {KNIK_GR:.0f} gr, waarvan "
          f"{tot_omkeer} omkeringen >= {OMKEER_GR:.0f} gr")
    if args.max_omkering is not None and tot_omkeer > args.max_omkering:
        sys.exit(f"FAAL: {tot_omkeer} omkeringen, toegestaan {args.max_omkering}")


if __name__ == "__main__":
    main()
