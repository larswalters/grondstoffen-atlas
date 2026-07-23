#!/usr/bin/env python3
"""maak_aansluitingen.py — bouwt v2/data/aansluitingen.json (M26.1).

Een AANSLUITING is de plek waar één grondstof het net raakt: de concentraatkade,
het laadspoor bij de smelter, de erts-pier. Waar `knooppunten.json` één
aanhechting per modaliteit heeft voor álle lading, heeft deze laag er één per
grondstof — en dát is wat twee lijnen in dezelfde havenmond mogelijk maakt.
Ontwerp: `v2/design/stroom-aansluiting.md`.

Zelfde rolverdeling als `maak_knooppunten.py`: **deze tool wijst niets aan, hij
MEET.** De lijst hieronder is redactie; de coördinaten komen uit OSM via
`verken_terminals.py` (ODbL). Per aansluiting rapporteert de tool de afstand tot
het dichtstbijzijnde knooppunt in elk net, zodat een verkeerd aangewezen kade
zichzelf verraadt — het Mountain-Pass-patroon uit de wegcorridors.

⚠️ De snap-afstand is hier GEEN foutmaat maar een MEETRESULTAAT. Een kade op
40 km van de dichtstbijzijnde MARNET-knoop betekent dat het net daar ophoudt,
niet dat de kade verkeerd staat. Dat verschil zichtbaar maken is precies waarom
de stromen geroute worden (Lars' werkregel).

Draaien:  python v2/tools/maak_aansluitingen.py [--schrijf]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))

import maak_knooppunten as mk  # noqa: E402 — Lezer/lees_knopen/dichtstbij hergebruiken

DATA = HIER.parent / "data"

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


# ==========================================================================
# DE AANSLUITINGEN — dit is de redactionele lijst (pilot: 4 stromen, 2 grondstoffen)
# ==========================================================================
# Velden:
#   id          stabiel, eigen id (géén afgeleide van een haven of LOCODE)
#   grondstof   sleutel uit data/*.js ("copper" / "coal")
#   fase        erts | raffinaat | product — volgt `stage` in de flows
#   rol         laadplek | overslag | losplek
#   plek        [lon, lat] van de KADE/LAADPLEK zelf — straatniveau, uit OSM
#   modi        op welke netten deze aansluiting mag aanhechten
#   knooppunt   optioneel: het aangewezen overslagpunt waar hij bij hoort
#   bron        waar de coördinaat vandaan komt (verplicht, ODbL-attributie)
#
# ⚠️ `plek` is de waarheid; de aanhechting wordt gemeten. Een aansluiting met
# alleen "zee" biedt nooit een spooraanhechting aan, hoe dicht het spoor ook
# ligt — dezelfde redactionele regel als bij het register.

AANSLUITINGEN = [
    # ======================================================================
    # STROOM A — koperconcentraat Collahuasi → Tongling (zee → rivier)
    # ======================================================================
    dict(id="cu-collahuasi-laad", grondstof="copper", fase="erts", rol="laadplek",
         naam="Collahuasi — kop van de slurryleiding (pompstation)",
         plek=[-68.64395, -20.97783], modi=[],
         bron="OSM — kopeinde van de substance=slurry-leiding, 1,9 km van Rajo Ujina "
              "en 2,3 km van het mijncomplex 'Minera Doña Inés de Collahuasi' (ODbL)",
         noot="⚠️ VERPLAATST NA LARS' OBSERVATIE dat de lijn 'op een beetje een raar punt' "
              "begon: dit is nu het KOPEINDE van de leiding zelf, niet de centroïde van het "
              "mijnterrein 2,3 km verderop. Daar loopt de slurry de pijp in; dáár begint de "
              "stroom. MODI IS LEEG en dat is het antwoord op de netvraag: de leiding is een "
              "eigen verbinding, geen gedeeld net (zie design/stroom-aansluiting.md §4a). "
              "Aanwijzen op 'weg' zou een vrachtwagen tekenen waar een pijp ligt."),
    dict(id="cu-patache-kade", grondstof="copper", fase="erts", rol="overslag",
         naam="Puerto Patache — Collahuasi-concentraatpier",
         plek=[-70.19773, -20.80503], modi=["zee"], knooppunt=None,
         bron="OSM way man_made=pier bij 'Puerto Patache Collahuasi' (ODbL)",
         noot="De EIGEN terminal van Collahuasi. data/copper.js stuurt deze stroom via "
              "Antofagasta, 120 km noordelijker; de node-noot zegt zelf al 'Patache/"
              "Collahuasi-haven'. Eerste gat dat het routeren blootlegt."),
    dict(id="cu-shanghai-kade", grondstof="copper", fase="erts", rol="overslag",
         naam="Shanghai/Luojing — Baogang-bulkpier aan de Yangtze",
         plek=[121.47618, 31.42704], modi=["zee", "binnen"], knooppunt="shanghai",
         bron="OSM way 'Baogang Pier', man_made=pier (ODbL)",
         noot="De bulkpier aan de Yangtze zelf. Concentraat voor de Yangtze-smelters komt "
              "niet via Yangshan binnen — dat is een containerhaven op eilanden vóór de "
              "kust, tientallen km van de riviermond, en dát is wat data/copper.js noemt. "
              "In werkelijkheid lossen veel concentraatschepen verder stroomopwaarts "
              "(Zhangjiagang/Jiangyin) of aan de eigen kade van de smelter."),
    dict(id="cu-tongling-kade", grondstof="copper", fase="erts", rol="losplek",
         naam="Tongling Nonferrous — loskade aan de Yangtze",
         plek=[117.77325, 30.93943], modi=["binnen"],
         bron="OSM way man_made=pier bij TNMG First Metallurgical Plant (ODbL)",
         noot="De pier ligt 1,5 km van het smelterterrein (30,92631 / 117,76997); de "
              "smelter zelf heeft geen kade-tag in OSM."),

    # ======================================================================
    # STROOM B — koperconcentraat Escondida → Jiangxi/Guixi (zee → spoor)
    # ======================================================================
    dict(id="cu-escondida-laad", grondstof="copper", fase="erts", rol="laadplek",
         naam="Escondida — Rajo Escondida (start slurry-pijpleiding)",
         plek=[-69.07169, -24.27004], modi=[],
         bron="OSM way 'Rajo Escondida', landuse=quarry resource=copper (ODbL)",
         noot="Zelfde verhaal als Collahuasi: concentraat per ±166 km slurry-pijp naar "
              "Coloso. Het spoor Antofagasta–Salta ligt op 6 km, maar rijdt dit "
              "concentraat niet — aanwijzen zou een trein tekenen die er niet is."),
    dict(id="cu-coloso-kade", grondstof="copper", fase="erts", rol="overslag",
         naam="Puerto Coloso — Escondida-concentraatpier",
         plek=[-70.46332, -23.76015], modi=["zee"], knooppunt="antofagasta",
         bron="OSM way 'Coloso', man_made=pier (ODbL)",
         noot="Escondida's eigen terminal, ±12 km ten zuiden van de haven Antofagasta "
              "waar data/copper.js hem heen stuurt. Hangt wél aan het aangewezen "
              "knooppunt Antofagasta — dáár zit de overslag naar het spoor."),
    dict(id="cu-beilun-kade", grondstof="copper", fase="erts", rol="overslag",
         naam="Ningbo-Zhoushan — Beilun ertsterminal (北仑矿石码头)",
         plek=[121.87573, 29.92742], modi=["zee", "spoor"],
         bron="OSM node '北仑矿石码头', seamark:type=harbour (ODbL)",
         noot="De ertsterminal zelf, niet de containerkades ernaast — precies het "
              "onderscheid waarvoor deze laag bestaat."),
    # ======================================================================
    # STROOM C — koperkathode Lobito → Rotterdam → Rijn → Duisburg
    # ======================================================================
    dict(id="cu-lobito-kade", grondstof="copper", fase="raffinaat", rol="overslag",
         naam="Lobito — Porto do Lobito, kade van de Lobito-corridor",
         plek=[13.54900, -12.34709], modi=["zee"], knooppunt="lobito",
         bron="OSM way 'Porto do Lobito', industrial=port landuse=harbour (ODbL)",
         noot="Het zee-eind van de Lobito-corridor; de Benguela-spoorlijn (CFB) ligt er "
              "1,1 km vandaan. Kathode gaat hier recht de Atlantische Oceaan op — zonder "
              "Kaap en zonder Malakka."),
    dict(id="cu-rotterdam-kade", grondstof="copper", fase="raffinaat", rol="overslag",
         naam="Rotterdam — Waalhaven, stukgoedkade",
         plek=[4.39341, 51.89369], modi=["zee", "binnen"], knooppunt="rotterdam",
         bron="OSM way man_made=pier in de Waalhaven (ODbL)",
         noot="⚠️ OSM tagt deze pier NIET met wat er wordt overgeslagen; de redactionele "
              "keuze steunt op de buren binnen 1 km (ArcelorMittal Staalhandel, "
              "Metaalhandel Ketting, Dutch Trading Consortium) — dit is de metaalhoek van "
              "de Waalhaven. Wat telt voor deze pilot: hij ligt ~30 km van de kolenkade op "
              "de Maasvlakte en hecht op een ándere binnenknoop."),
    dict(id="cu-duisburg-kade", grondstof="copper", fase="raffinaat", rol="losplek",
         naam="Duisburg — Duisport Ruhrort, Becken A",
         plek=[6.75590, 51.45187], modi=["binnen"],
         bron="OSM way 'Becken A', harbour=yes (ODbL)",
         noot="Stukgoedbekken van de grootste binnenhaven ter wereld. OSM zegt niet welk "
              "bekken non-ferro doet; het onderscheid dat hier telt is dat kolen 7 km "
              "noordelijker lossen, aan de Schwelgern-pier bij het staalbedrijf."),

    # ======================================================================
    # STROOM D — steenkool Cerrejón → Puerto Bolívar → Rotterdam → Ruhr
    # ======================================================================
    dict(id="coal-cerrejon-laad", grondstof="coal", fase="raffinaat", rol="laadplek",
         naam="Cerrejón — Complejo Carbonífero, laadzijde",
         plek=[-72.55960, 11.12067], modi=["spoor"],
         bron="OSM way 'Complejo Carbonífero El Cerrejón', landuse=quarry (ODbL)",
         noot="OSM tagt het laadstation zelf niet; de eigen spoorlijn ligt er wél als "
              "'Vía Ferroviaria Albania - Puerto Bolívar' (railway=rail usage=main). "
              "Gemeten: mijn en pier zitten op DEZELFDE spoorcomponent van 158 km — de "
              "echte lijn is ~150 km, dus die component ís deze kolenlijn."),
    dict(id="coal-bolivar-kade", grondstof="coal", fase="raffinaat", rol="overslag",
         naam="Puerto Bolívar — kolenpier van Cerrejón",
         plek=[-71.97693, 12.23912], modi=["zee", "spoor"],
         bron="OSM way 'Terminal de Carbones del Cerrejón', landuse=industrial (ODbL)",
         noot="Het zee-eind van de kolenlijn: hier gaat de trein leeg terug en vertrekt de "
              "capesize. Een van de weinige plekken in de atlas waar spoor en zee elkaar "
              "raken zónder tussenliggende stad."),
    dict(id="coal-rotterdam-kade", grondstof="coal", fase="raffinaat", rol="overslag",
         naam="Rotterdam — EMO, droge-bulkterminal Maasvlakte",
         plek=[4.05354, 51.94109], modi=["zee", "binnen"], knooppunt="rotterdam",
         bron="OSM way 'EMO', landuse=industrial operator=HES International B.V. (ODbL)",
         noot="DE KERN VAN DE PILOT: dezelfde haven als de koperkade hierboven, ~30 km "
              "verderop, en met een eigen aanhechting op het binnenwaternet (knoop 40904 "
              "tegen 40927). Met één aanhechting per haven zijn deze twee stromen niet uit "
              "elkaar te houden."),
    dict(id="coal-duisburg-kade", grondstof="coal", fase="raffinaat", rol="losplek",
         naam="Duisburg — Schwelgern-pier (ThyssenKrupp-staal)",
         plek=[6.72347, 51.51321], modi=["binnen"],
         bron="OSM way man_made=pier bij Schwelgern, met moorings (ODbL)",
         noot="De kolen-/ertskade van het staalbedrijf zelf: Kokerei Schwelgern ligt op "
              "1,3 km, het Erzlager op 1,2 km, ThyssenKrupp Steel op 0,6 km. Cokeskool "
              "gaat hier naar de hoogoven, niet naar een stukgoedbekken."),

    dict(id="cu-guixi-spoor", grondstof="copper", fase="erts", rol="losplek",
         naam="Jiangxi Copper — smelter Guixi (贵溪冶炼厂)",
         plek=[117.22570, 28.33380], modi=["spoor"],
         bron="OSM way '贵溪冶炼厂', industrial=processing_plant (ODbL)",
         noot="De grootste kopersmelter ter wereld. Ligt 3,8 km noordelijker dan de "
              "node-coördinaat in data/copper.js (28,30 / 117,20) — op wereldniveau "
              "onzichtbaar, op straatniveau het verschil tussen smelter en veld."),
]

MODI = ("zee", "binnen", "spoor", "weg")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true", help="aansluitingen.json wegschrijven")
    args = ap.parse_args()

    ports = json.loads((DATA / "ports.json").read_text(encoding="utf-8"))
    zee_knopen = ports["zeeKnopen"]

    print("marnet lezen…", flush=True)
    m_meta, m_lon, m_lat = mk.lees_knopen(DATA / "marnet.json", DATA / "marnet.bin")
    m_vec = mk.eenheidsvectoren(m_lon, m_lat)
    idx = {
        "zee": np.arange(0, zee_knopen),
        "binnen": np.arange(zee_knopen, len(m_lon)),
    }

    print("landnet lezen…", flush=True)
    l_meta, l_lon, l_lat = mk.lees_knopen(DATA / "landnet.json", DATA / "landnet.bin")
    l_vec = mk.eenheidsvectoren(l_lon, l_lat)
    knoop_modus = land_knoop_modus(l_meta)
    idx["spoor"] = np.flatnonzero(knoop_modus == 1)
    idx["weg"] = np.flatnonzero(knoop_modus == 2)
    print(f"  landnet: {idx['spoor'].size:,} spoorknopen · {idx['weg'].size:,} wegknopen")

    register = json.loads((DATA / "knooppunten.json").read_text(encoding="utf-8"))
    bekende_punten = {p["id"] for p in register["punten"]}

    print()
    print(f"{'aansluiting':40s} {'zee':>9s} {'binnen':>9s} {'spoor':>9s} {'weg':>9s}")
    print("-" * 80)

    uit, fouten = [], []
    for e in AANSLUITINGEN:
        lon, lat = e["plek"]
        meting = {}
        for m in MODI:
            vec, lo, la = (m_vec, m_lon, m_lat) if m in ("zee", "binnen") else (l_vec, l_lon, l_lat)
            k, d = mk.dichtstbij(vec, idx[m], lon, lat)
            meting[m] = (k, d, lo, la)

        def cel(m):
            _, d, _, _ = meting[m]
            merk = "*" if m in e["modi"] else " "
            return f"{merk}{d:8.1f}" if d < 1e6 else f"{merk}{'—':>8s}"

        print(f"{e['naam'][:40]:40s} " + " ".join(cel(m) for m in MODI))

        knp = e.get("knooppunt")
        if knp and knp not in bekende_punten:
            fouten.append(f"{e['id']}: knooppunt '{knp}' staat niet in knooppunten.json")

        # ⚠️ `gemeten` is een RAPPORT, geen invoer. De lader in keten.js snapt
        # opnieuw vanaf `plek` — knoop-ids én knoopcoördinaten verschuiven bij
        # elke rebake, de kade niet. Wijkt de browser af van deze getallen, dan
        # is de bake veranderd en niet de redactie; dat verschil moet zichtbaar
        # kunnen worden en daarom staat het hier.
        gemeten = {}
        for m in e["modi"]:
            k, d, lo, la = meting[m]
            if k < 0:
                fouten.append(f"{e['id']}: geen knoop in net '{m}'")
                continue
            gemeten[m] = {
                "bij": [round(float(lo[k]), 5), round(float(la[k]), 5)],
                "snapKm": round(d, 2),
            }

        uit.append({
            "id": e["id"],
            "grondstof": e["grondstof"],
            "fase": e["fase"],
            "rol": e["rol"],
            "naam": e["naam"],
            **({"knooppunt": knp} if knp else {}),
            "plek": [round(lon, 5), round(lat, 5)],
            "modi": list(e["modi"]),
            "gemeten": gemeten,
            "bron": e["bron"],
            **({"noot": e["noot"]} if e.get("noot") else {}),
        })

    print("-" * 80)
    print("* = aangewezen modaliteit · getal = km tot de dichtstbijzijnde knoop in dat net")
    print("  (de snap-afstand is een MEETRESULTAAT, geen fout: ver = daar houdt het net op)")

    if fouten:
        print("\n⚠️ FOUTEN:")
        for f in fouten:
            print("  " + f)
        return 1

    doc = {
        "versie": 1,
        "toelichting": (
            "Aansluitingen per grondstof: de plek waar één grondstof het net raakt "
            "(kade, laadspoor, losplek) op straatniveau. Verfijnt knooppunten.json, "
            "vervangt het niet — een stroom zonder aansluiting valt terug op de "
            "generieke aanhechting van zijn knooppunt. Zie design/stroom-aansluiting.md."
        ),
        "bron": "coördinaten uit OpenStreetMap (ODbL) via verken_terminals.py",
        "aansluitingen": uit,
    }
    print(f"\n{len(uit)} aansluitingen · "
          f"{sum(len(a['gemeten']) for a in uit)} aanhechtingen")
    if args.schrijf:
        pad = DATA / "aansluitingen.json"
        pad.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"geschreven: {pad} ({pad.stat().st_size / 1024:.1f} KB)")
    else:
        print("(niets geschreven — geef --schrijf mee)")
    return 0


def land_knoop_modus(l_meta):
    """Modus per landnet-knoop (1=spoor, 2=weg) uit de label-ranges op de edges.

    Kopie van de leesstap in maak_knooppunten.main(); die zit daar in de body en
    is niet los aan te roepen. Bewust dezelfde volgorde van varint-velden — een
    afwijking hier geeft stil verschoven knopen, niet een foutmelding.
    """
    lezer = mk.Lezer((DATA / "landnet.bin").read_bytes())
    for _ in range(l_meta["knopen"]):
        lezer.volgende(); lezer.volgende()
    n_edges = l_meta["edges"]
    e_a = np.empty(n_edges, dtype=np.int64)
    e_b = np.empty(n_edges, dtype=np.int64)
    a = b = 0
    for i in range(n_edges):
        a += lezer.volgende()
        b += lezer.volgende()
        e_a[i] = a
        e_b[i] = b
        lezer.volgende()          # km
        lezer.volgende()          # soort
        lezer.volgende()          # aantal punten
        if lezer.volgende() == 1:
            for _ in range(4):
                lezer.volgende()

    modus = np.zeros(l_meta["knopen"], dtype=np.uint8)
    for lab in l_meta["labels"]:
        code = 1 if lab["modus"] == "spoor" else 2
        v, t = lab["edgeVan"], min(lab["edgeTot"], n_edges)
        modus[e_a[v:t]] = code
        modus[e_b[v:t]] = code
    return modus


if __name__ == "__main__":
    sys.exit(main())
