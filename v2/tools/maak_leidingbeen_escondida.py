#!/usr/bin/env python3
"""
maak_leidingbeen_escondida.py — het tracé van de Escondida-concentraatleiding
(mineroducto/concentraducto) van de concentrator naar Puerto Coloso, als
tekengeometrie voor de stroomlaag.

WAAROM DIT BESTAAT. De atlas tekende dit been als een KAARSRECHTE stippel van
153,5 km tussen de twee ankers, omdat OSM het tracé niet als doorlopende leiding
kent. De projecteigenaar zag dat en keurde het af — terecht, en het is meetbaar:
de gepubliceerde leiding is ~170 km (+11% op de koorde), en op de plek waar de
werkelijke leiding het verst van onze rechte lijn af ligt zat er **15,41 km**
tussen. Een rechte lijn was hier dus geen vereenvoudiging maar een fout.

⚠️ HET VERSCHIL MET COLLAHUASI. Die leiding komt uit OSM (`substance=slurry`,
1.363 punten, omwegfactor 1,188) en wordt gebakken door fetch_pijpleidingen.py.
Voor Escondida bestaat die kartering NIET: gemeten op de lokale chili-extract
dekken alle 74 niet-gas-pipeline-ways samen maar **18%** van de lengtegraad-span,
in drie losse clusters. Vandaar dit bestand.

WAT DE BRON IS, PER STUK (en dat verschilt, dus het staat erbij):
  * lon −70,294 … −70,161 (13,96 km) — **echte OSM-kartering**: ways 1530915728
    + 1530915724, `man_made=pipeline` / `location=overground`. Onafhankelijke
    bevestiging: het concentraducto-meetstation "Estación de Monitoreo SFM 3C"
    ligt 8 m van deze lijn.
  * lon −70,161 … −69,105 (~116 km) — **op Esri-satellietbeeld gevolgd** (z13-z17,
    zes banden, 2026-08-05), met langs de weg gevonden bevestigingen: "Estación
    de Bombeo N.º 2" op 172 m, klepstation VS2C op 68 m, "Bombeo N.º 3" op 167 m.
    Tussen lon −69,284 en −69,105 is het pijpenrek zelf zichtbaar als een ladder
    op steunen, los van de weg.
  * lon −70,467 … −70,294 (17,67 km) en −69,105 … −69,060 (4,82 km) — **RECHTE
    OVERBRUGGING, geen waarneming.** Dat zijn geen luiheid maar twee gemeten
    gaten: het westelijke stuk Coloso→La Negra is volgens SEIA deels ingegraven
    en loopt via twee tunnels om Caleta Coloso heen, en op het mijnterrein zelf
    liggen tientallen parallelle pijpenrekken, wegen en banden door elkaar.
    Ze blijven recht en worden hier expliciet benoemd i.p.v. gladgestreken.

⚠️ SYSTEMATISCH VOORBEHOUD, EN DIT MOET JE WETEN VOOR JE HEM "HET TRACÉ" NOEMT.
Over lon −70,16 … −69,29 volgt deze lijn de **as van de gedeelde corridor** —
Ruta Minera, concentraatleiding, waterleiding (acueducto) en de 220 kV-lijn
liggen daar naast elkaar — en niet aantoonbaar de concentraatbuis alléén. De
dwarsonzekerheid is **±100–250 m**, en op het deel lon −69,65 … −69,47 ligt de
buis systematisch ~66–92 m ten ZUIDWESTEN van deze punten. Op wereldschaal is
dat onzichtbaar; op straatniveau is het de resterende fout. Dat is een eerlijke
ruil tegen de 15,41 km die het was, geen eindstand.

REPRODUCEERBAARHEID. De puntenlijst staat hieronder in de broncode, dus dit
been is op een verse clone opnieuw te maken — anders dan de andere gebakken
benen, die van ongetrackte bestanden in build-cache afhangen. Verandert het
tracé (een betere bron, een gevonden SEIA-kaart), dan verandert deze lijst mee
en wordt de stroom herbakken; het gebakken json is de uitvoer, dit bestand het
recept.

Draaien:
    python v2/tools/maak_leidingbeen_escondida.py
Daarna de stroom herbakken:
    bash v2/tools/bak_stromen.sh koper-escondida
"""
import json
import math
import os

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # …/v2
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf",
                   "leidingbeen-escondida-coloso.geojson")

# ── HET TRACÉ, west → oost (Coloso-filterfabriek → Escondida-concentrator) ──
# 126 punten. De twee uiteinden zijn de BESTAANDE ankers uit aansluitingen.json
# en verschuiven niet: cu-coloso-kade's filterfabriek en cu-escondida-laad.
TRACE_WEST_OOST = [
    # ── recht gat 1: Coloso → La Negra (17,67 km, deels ingegraven + tunnels)
    (-70.46700, -23.75900),
    # ── OSM-kartering: ways 1530915728 + 1530915724
    (-70.29369, -23.76861), (-70.28244, -23.76505), (-70.27408, -23.76238),
    (-70.26269, -23.75874), (-70.25394, -23.75597), (-70.24339, -23.75264),
    (-70.23225, -23.74908), (-70.22657, -23.74728), (-70.21770, -23.74635),
    (-70.21714, -23.74627), (-70.20725, -23.74602), (-70.19658, -23.74571),
    (-70.18693, -23.74543), (-70.17626, -23.74512), (-70.16385, -23.74474),
    (-70.16060, -23.74463),
    # ── satelliet-gevolgd, band B1
    (-70.15000, -23.74460), (-70.14000, -23.74430), (-70.13000, -23.74390),
    (-70.12390, -23.74380), (-70.12000, -23.74520), (-70.11000, -23.74890),
    (-70.10000, -23.75290), (-70.09000, -23.75660), (-70.08000, -23.75970),
    (-70.07000, -23.76250), (-70.06000, -23.76560), (-70.05000, -23.76870),
    (-70.04000, -23.77020), (-70.03000, -23.77230), (-70.02000, -23.77490),
    (-70.01000, -23.77740),
    # ── band B2 — het enige stuk waar de buis los van het asfalt zichtbaar is
    (-70.00674, -23.77781), (-69.99611, -23.78052), (-69.98456, -23.78336),
    (-69.97163, -23.78660), (-69.95864, -23.79393), (-69.94943, -23.79999),
    (-69.93719, -23.80809), (-69.92654, -23.81532), (-69.91855, -23.82226),
    (-69.90845, -23.82909), (-69.89848, -23.83568), (-69.88623, -23.84179),
    (-69.87652, -23.84695), (-69.86745, -23.85362), (-69.85818, -23.85961),
    (-69.84830, -23.86592), (-69.84008, -23.87127), (-69.83317, -23.87945),
    (-69.83017, -23.88167),
    # ── band B3
    (-69.82000, -23.88580), (-69.81000, -23.89195), (-69.80000, -23.89755),
    (-69.79000, -23.90340), (-69.78000, -23.90990), (-69.77000, -23.91560),
    (-69.76000, -23.92230), (-69.75000, -23.92880), (-69.74000, -23.93630),
    (-69.73000, -23.94250), (-69.72000, -23.94840), (-69.71000, -23.95550),
    (-69.70000, -23.96150), (-69.69000, -23.96870), (-69.68800, -23.96970),
    (-69.68450, -23.97480), (-69.68000, -23.98000), (-69.67340, -23.98280),
    (-69.67000, -23.98275), (-69.66000, -23.98570), (-69.65000, -23.99250),
    # ── band B4 — ⚠️ hier ligt de buis systematisch ~66-92 m ZUIDWEST hiervan
    (-69.64748, -23.99435), (-69.63496, -24.00235), (-69.62284, -24.01010),
    (-69.61017, -24.01820), (-69.59852, -24.02565), (-69.58650, -24.03334),
    (-69.57699, -24.03921), (-69.56377, -24.04603), (-69.54985, -24.05325),
    (-69.53642, -24.06022), (-69.52017, -24.06726), (-69.50527, -24.07389),
    (-69.49087, -24.08052), (-69.48638, -24.08588),
    # ── band B5
    (-69.47565, -24.09287), (-69.46556, -24.09963), (-69.45537, -24.10673),
    (-69.44251, -24.11151), (-69.42789, -24.11689), (-69.41705, -24.12079),
    (-69.40194, -24.12642), (-69.39208, -24.13013), (-69.38167, -24.13543),
    (-69.36785, -24.14398), (-69.36248, -24.14719), (-69.34576, -24.15501),
    (-69.33874, -24.15845), (-69.32675, -24.16388), (-69.31535, -24.16941),
    (-69.30294, -24.17502), (-69.29206, -24.18009),
    # ── band B6 — de leidingstrook maakt zich hier los van de Ruta Minera
    (-69.28831, -24.18710), (-69.28300, -24.19400), (-69.27294, -24.20411),
    (-69.26161, -24.21131), (-69.25920, -24.21340), (-69.24880, -24.21620),
    (-69.23000, -24.22510), (-69.22000, -24.22850), (-69.21000, -24.23290),
    (-69.20000, -24.23680), (-69.17971, -24.24083), (-69.17000, -24.24040),
    (-69.16000, -24.24040), (-69.15500, -24.24030), (-69.15000, -24.23940),
    (-69.14000, -24.24000), (-69.13000, -24.24070), (-69.12000, -24.24480),
    (-69.11600, -24.24590), (-69.11200, -24.24690), (-69.10500, -24.24800),
    # ── recht gat 2: het mijnterrein zelf (4,82 km)
    (-69.06000, -24.26200),
]

R = 6371.0088


def km(a, b):
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def main():
    # ⚠️ DE STROOM LOOPT MIJN → HAVEN, dus het been gaat OOST → WEST.
    vol = list(reversed(TRACE_WEST_OOST))

    # ⚠️ ALLEEN HET WAARGENOMEN DEEL KOMT IN DIT BESTAND. De twee uiteinden
    # zijn rechte overbruggingen zónder waarneming en horen GESTIPPELD op de
    # kaart — precies zoals de Collahuasi-leiding doorgetrokken staat waar de
    # kartering reikt en gestippeld op de laatste 736 m waar hij ophoudt.
    # Doorgetrokken betekent in dit project: we weten waar de lijn ligt.
    # Die twee stippels worden door bak_stromen.sh als --stippel gelegd; de
    # exacte vlaggen staan hieronder in de uitvoer, zodat recept en uitvoer
    # niet uit elkaar kunnen lopen.
    punten = vol[1:-1]                      # zonder de twee ankerpunten
    lengte = sum(km(punten[i], punten[i + 1]) for i in range(len(punten) - 1))
    recht = km(punten[0], punten[-1])
    gat_oost = km(vol[0], vol[1])           # mijnterrein
    gat_west = km(vol[-2], vol[-1])         # Coloso → La Negra

    print("leidingbeen Escondida → Coloso — ALLEEN HET WAARGENOMEN DEEL")
    print(f"  punten        : {len(punten)}")
    print(f"  lengte        : {lengte:.2f} km")
    print(f"  hemelsbreed   : {recht:.2f} km")
    print(f"  omwegfactor   : {lengte/recht:.3f}  (Collahuasi 1,188 · oude rechte lijn 1,000)")
    print(f"  totaal met de twee stippels: {lengte + gat_oost + gat_west:.2f} km "
          f"({(lengte+gat_oost+gat_west-170)/170*100:+.1f}% tegen de gepubliceerde ~170 km)")
    print("\n  de twee GESTIPPELDE overbruggingen (geen waarneming) — zet ze zo in bak_stromen.sh:")
    print(f'    --stippel "leiding|slurryleiding op het mijnterrein — pijpenrekken door elkaar, '
          f'niet te volgen ({gat_oost:.1f} km)|'
          f'{vol[0][1]:.5f},{vol[0][0]:.5f}|{vol[1][1]:.5f},{vol[1][0]:.5f}"')
    print(f'    --stippel "leiding|slurryleiding La Negra → Coloso — deels ingegraven + twee tunnels '
          f'({gat_west:.1f} km)|'
          f'{vol[-2][1]:.5f},{vol[-2][0]:.5f}|{vol[-1][1]:.5f},{vol[-1][0]:.5f}"')
    print()

    uit = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": {
                "naam": "Escondida — concentraatslurry naar Puerto Coloso (waargenomen deel)",
                "km": round(lengte, 2),
                "punten": len(punten),
                "bron": "OSM ways 1530915728+1530915724 (13,96 km, ODbL) + Esri World "
                        "Imagery z13-z17 gevolgd 2026-08-05 (~116 km). De twee "
                        "onwaargenomen uiteinden zitten NIET in dit bestand: die "
                        "worden gestippeld gelegd door bak_stromen.sh",
                "voorbehoud": "volgt de as van de gedeelde corridor (Ruta Minera + "
                              "leiding + acueducto + 220 kV), niet aantoonbaar de "
                              "concentraatbuis alléén; dwarsonzekerheid ±100-250 m, "
                              "op lon -69,65…-69,47 ligt de buis ~66-92 m ZW",
                "gereedschap": "maak_leidingbeen_escondida.py",
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [[round(lo, 5), round(la, 5)] for lo, la in punten],
            },
        }],
    }
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(uit, f, ensure_ascii=False)
    print(f"  geschreven    : {UIT} ({os.path.getsize(UIT)/1024:.1f} KB)")


if __name__ == "__main__":
    main()
