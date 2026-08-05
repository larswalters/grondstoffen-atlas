#!/usr/bin/env python3
"""
maak_havenaanloop.py — een haven-aanloop die OVER WATER blijft, i.p.v. een
rechte lijn die dwars over de kust snijdt.

WAAROM DIT BESTAAT. Waar MARNET niet tot de kade reikt, tekent de stroomlaag een
**schematische** aanloop: een gestippelde rechte lijn van het anker naar de
dichtstbijzijnde zeeknoop. Die stippel is eerlijk over wat hij niet weet — het
net reikt daar niet (werkwijze §7) — maar hij was niet eerlijk over iets anders:
gemeten met `toets_rechte_benen.py` op 2026-08-05 loopt de aanloop van

    Nacala   122,3 km  →  17,5 km (14%) OVER LAND
    Coloso    85,1 km  →   2,1 km  (3%) over land

Een schip vaart niet over een schiereiland. "Schematisch" mag betekenen *we
kennen de vaargeul niet*; het mag niet betekenen *de lijn gaat door land heen*.
Dat is precies de grens die de Escondida-leiding ook overschreed, alleen daar
was de fout 15,41 km en zichtbaar, hier is hij structureel en klein op de kaart.

WAT DIT TOOL DOET. Het zoekt een pad over water tussen de twee punten met de
**bewezen M23-machinerie**: `detour()` uit `bake_marnet.py`, dezelfde functie
die in de verzoeningsronde 148 van de 150 kapotte MARNET-edges omlegde. Niets
gedupliceerd — dit bestand is een dunne aanroeper.

⚠️ DE VIER TRAPPEN ZIJN GEEN OPTIMALISATIE MAAR EEN VOORWAARDE (M23-les): de
kustbuffer beschermt de lijn tegen het scheren langs de kust, maar knijpt een
nauwe doorgang dicht. Dus: 0,02° gebufferd → 0,01° gebufferd → 0,01° kaal →
0,02° kaal, en de eerste die een pad geeft wint.

⚠️ DIT IS EN BLIJFT EEN SCHEMATISCHE AANLOOP. Het pad is de kortste weg over
water, niet de bevaren vaargeul — er zit geen dieptegang, geen betonning en geen
verkeersscheidingsstelsel in. Het been blijft daarom **gestippeld**; wat er
verandert is alleen dat de stippel niet meer door land loopt. Wie de echte geul
wil, heeft AIS-tracks nodig (en juist op deze plekken zijn die er niet: Chili en
Mozambique hebben nul havens met varend AIS-verkeer, gemeten in de wereldscan).

    python v2/tools/maak_havenaanloop.py --naam nacala \\
        --van -14.5383,40.6673 --naar -15.0,41.7 \\
        --uit v2/build-cache/ais/graaf/aanloop-nacala.geojson
"""
import argparse
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import bake_marnet as bm   # noqa: E402 — detour() + LandTester, niet dupliceren

R = 6371.0088
# ⚠️ ALLE TRAPPEN WORDEN GEDRAAID EN DE BESTE WINT — niet de eerste die een pad
# geeft. Bij Nacala gaf de eerste geslaagde trap (0,01° gebufferd) nog 1,4 km
# over land, terwijl een fijnere korrel hem op nul bracht: op 0,01° is één cel
# ~1,1 km en dat is grover dan de landtongen in de baai. "Eerste die werkt" is
# hier dus de verkeerde regel; least-land-then-shortest is de juiste.
TRAPPEN = [(0.02, True), (0.01, True), (0.005, True), (0.0025, True),
           (0.0025, False), (0.005, False), (0.01, False), (0.02, False)]


def km(a, b):
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def over_land_km(punten, land, split=False):
    """Hoeveel km van de lijn ligt op land? Bemonstert elke ~0,5 km.

    ⚠️ MET split=True komt er een TWEEDE getal terug: het deel dat NIET aan een
    uiteinde grenst. Dat onderscheid is het hele punt van deze meting. Een kade
    ligt op de 1:10M-kustlijn per definitie ÓP land — gemeten bij Nacala valt
    het ankerpunt zelf binnen de landpolygoon — dus het eerste stuk vanaf de kade
    telt altijd mee en dat is een artefact van de korrel, geen fout. Wat wél een
    fout is, is landkruising MIDDEN op de lijn: daar snijdt hij een schiereiland
    af waar een schip omheen vaart. Alleen dat tweede getal hoort een alarm te
    zijn (zelfde onderscheid als de M23-classificatie 'aanloop' vs 'kapot').
    """
    import numpy as np
    totaal = 0.0
    midden = 0.0
    for i in range(len(punten) - 1):
        a, b = punten[i], punten[i + 1]
        d = km(a, b)
        n = max(2, int(d / 0.5))
        # ⚠️ ANTIMERIDIAAN. Lineair interpoleren in lengtegraad veegt bij een
        # sprong van 179,9° naar -179,9° dwars over de hele wereld terug — en
        # dan meldt de toets landcontact op plekken waar de route nooit komt.
        # Gemeten fout die dit opleverde: het zeebeen Coloso → Beilun (Chili →
        # China, over de Grote Oceaan) meldde 4,9 km "land" rond 50,010/9,403,
        # dat is bij FRANKFURT. Werk daarom in een doorlopend lon-frame en wikkel
        # pas terug bij het bemonsteren. Zelfde valkuil als de 15 dubbele
        # ±180-knopen in MARNET (M23) — die kostte daar een trans-Pacific route.
        lo_a, lo_b = a[0], b[0]
        if abs(lo_b - lo_a) > 180.0:
            lo_b += 360.0 if lo_b < lo_a else -360.0
        monsters = [((((lo_a + (lo_b - lo_a) * t / n) + 180.0) % 360.0) - 180.0,
                     a[1] + (b[1] - a[1]) * t / n)
                    for t in range(n + 1)]
        raak = land.hits(np.array(monsters))
        stuk = d * (raak.sum() / len(monsters))
        totaal += stuk
        if i not in (0, len(punten) - 2):
            midden += stuk
    return (totaal, midden) if split else totaal


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--naam", required=True)
    ap.add_argument("--van", required=True, help="anker (kade) als 'lat,lon'")
    ap.add_argument("--naar", required=True, help="zeeknoop als 'lat,lon'")
    ap.add_argument("--uit", required=True)
    a = ap.parse_args()

    def punt(s):
        la, lo = (float(x) for x in s.split(","))
        return (lo, la)

    pa, pb = punt(a.van), punt(a.naar)
    print(f"haven-aanloop {a.naam}: {pa[1]:.4f},{pa[0]:.4f} → {pb[1]:.4f},{pb[0]:.4f}")
    print("landpolygonen laden (1:10M, meren tellen als water)…")
    land = bm.LandTester()

    recht = [pa, pb]
    land_recht = over_land_km(recht, land)
    print(f"  rechte lijn : {km(pa, pb):7.1f} km · daarvan {land_recht:5.1f} km OVER LAND "
          f"({land_recht/km(pa,pb)*100:.0f}%)")

    kandidaten = []
    for cel, gebufferd in TRAPPEN:
        pad = bm.detour(pa, pb, land, cell=cel, gebufferd=gebufferd)
        merk = f"cel {cel}° {'gebufferd' if gebufferd else 'kaal':<10}"
        if not pad:
            print(f"  trap {merk} → geen pad")
            continue
        pts = [pa] + list(pad) + [pb]
        lng = sum(km(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
        ol, mid = over_land_km(pts, land, split=True)
        print(f"  trap {merk} → {len(pad):4d} punten · {lng:7.1f} km · "
              f"{ol:5.2f} km over land (waarvan {mid:4.2f} km MIDDEN op de lijn)")
        kandidaten.append((round(mid, 2), round(ol, 2), lng, cel, gebufferd, pts))
    if not kandidaten:
        sys.exit("GEEN PAD OVER WATER GEVONDEN — dat is een bevinding, geen reden om de "
                 "rechte lijn te laten staan. Meld hem in de routebrief.")

    # sorteer op wat écht fout is (land MIDDEN op de lijn), dan op totaal, dan kort
    kandidaten.sort(key=lambda k: (k[0], k[1], k[2]))
    land_midden, land_na, lengte, cel, gebufferd, punten = kandidaten[0]
    print(f"  ── gekozen  : cel {cel}° {'gebufferd' if gebufferd else 'kaal'} "
          f"(minste land midden op de lijn, dan totaal, dan kortst)")
    print(f"  aanloop     : {lengte:7.1f} km · {len(punten)} punten · "
          f"{land_na:.2f} km over land, waarvan {land_midden:.2f} km midden op de lijn")
    print(f"  omwegfactor : {lengte/km(pa,pb):.3f}")
    if land_midden > 0.5:
        print(f"  ⚠️ {land_midden:.1f} km land MIDDEN OP DE LIJN — dat is een echte "
              f"landkruising; meld hem in de routebrief in plaats van hem te verbergen.")
    else:
        print(f"  ✓ geen landkruising midden op de lijn. De {land_na:.2f} km die overblijft "
              f"grenst aan een uiteinde:\n    een kade ligt op de 1:10M-kustlijn per definitie "
              f"óp land — dat is de korrel, geen fout.")

    uit = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {
            "naam": f"haven-aanloop {a.naam} (schematisch, over water)",
            "km": round(lengte, 2), "punten": len(punten),
            "overLandKm": round(land_na, 2),
            "rechteLijnKm": round(km(pa, pb), 2),
            "rechteLijnOverLandKm": round(land_recht, 2),
            "bron": "kortste pad over water via bake_marnet.detour() tegen de "
                    "1:10M-landpolygonen (dezelfde bron als de gerenderde vectorwereld)",
            "voorbehoud": "SCHEMATISCH — kortste weg over water, niet de bevaren "
                          "vaargeul: geen diepgang, betonning of verkeersscheiding. "
                          "Het been blijft gestippeld; alleen de landkruising is weg.",
            "gereedschap": "maak_havenaanloop.py",
        },
        "geometry": {"type": "LineString",
                     "coordinates": [[round(lo, 5), round(la, 5)] for lo, la in punten]},
    }]}
    os.makedirs(os.path.dirname(a.uit), exist_ok=True)
    with open(a.uit, "w", encoding="utf-8") as f:
        json.dump(uit, f, ensure_ascii=False)
    print(f"  geschreven  : {a.uit} ({os.path.getsize(a.uit)/1024:.1f} KB)")


if __name__ == "__main__":
    main()
