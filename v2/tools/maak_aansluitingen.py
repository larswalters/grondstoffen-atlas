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

# ⚠️ marnet.bin/json staan BEWUST niet in v2/data — de bol mag het waternet niet
# laden (zie de kop van hecht_marnet.py, en de schone-bol-bake van 2026-07-24).
# Deze tool leest ze daarom uit de build-cache, net als hecht_marnet.py doet via
# --marnet. Ontbreekt de map, dan terugzetten uit de tag:
#     git show pre-ais-net:v2/data/marnet.json > <map>/marnet.json
#     git show pre-ais-net:v2/data/marnet.bin  > <map>/marnet.bin
MARNET_STD = HIER.parent / "build-cache" / "marnet-preais"

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
              "Aanwijzen op 'weg' zou een vrachtwagen tekenen waar een pijp ligt. "
              "✅ SATELLIET-CHECK DOORSTAAN 2026-07-28 (z16, Esri): staat precies naast "
              "de basins waar de slurry de leiding in gaat — Lars bevestigde."),
    dict(id="cu-patache-kade", grondstof="copper", fase="erts", rol="overslag",
         naam="Puerto Patache — Collahuasi-concentraatpier (ligplaats)",
         plek=[-70.19890, -20.80270], modi=["zee"], knooppunt=None,
         bron="SATELLIET-GELEGD op Esri World Imagery (z16, 2026-07-28); herkomst "
              "OSM way man_made=pier bij 'Puerto Patache Collahuasi' (ODbL)",
         noot="De EIGEN terminal van Collahuasi. data/copper.js stuurt deze stroom via "
              "Antofagasta, 120 km noordelijker; de node-noot zegt zelf al 'Patache/"
              "Collahuasi-haven'. Eerste gat dat het routeren blootlegt. "
              "⚠️ 286 m VERPLAATST bij de anker-check van 2026-07-28 (goedkeuring Lars): "
              "het OSM-punt lag op de WALKANT van de steiger, de ligplaats van het schip "
              "ligt aan de kop ervan. Kleinste correctie van de ronde."),
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
         naam="Tongling Nonferrous — kade van de nieuwe kopersmelter",
         plek=[117.77180, 30.98656], modi=["binnen"],
         bron="OSM natural=water-oever bij de kade van de nieuwe Tongling "
              "Nonferrous-verwerkingsplant; kade-tip 117,7717/30,98236 → begin "
              "117,7719/30,99133, smelter erachter op 117,7806/30,98656 (ODbL)",
         noot="⚠️ TWEE KEER VERPLAATST NA LARS' FOTO-CHECK. Eerst stond hij bij een "
              "ánder terrein (117,773/30,939), toen bij de OUDE gesloten smelter "
              "(117,756/30,918). Dit is nu de kade van de NIEUWE, actieve kopersmelter "
              "van de TNMG-groep (Lars wees exact aan: roze = kade, blauw = smelter). Hij "
              "ligt op de oostgeul bij het begin van de splitsing (noordpunt van het "
              "eiland); het schip komt van benedenstrooms de hoofdgeul af, gaat bij de "
              "noordpunt de oostgeul in en zakt naar de kade — zie de oostgeul-lijn in "
              "data/vaarwegen-handmatig.geojson. "
              "✅ SATELLIET-CHECK DOORSTAAN 2026-07-28 (z16, Esri): ongewijzigd."),

    # ======================================================================
    # STROOM B — koperconcentraat Escondida → Jiangxi/Guixi (zee → spoor)
    # ======================================================================
    dict(id="cu-escondida-laad", grondstof="copper", fase="erts", rol="laadplek",
         naam="Escondida — concentrator/indikkers (kop van de slurryleiding)",
         plek=[-69.06000, -24.26200], modi=[],
         bron="SATELLIET-GELEGD op Esri World Imagery (z16, 2026-07-28) op de rij ronde "
              "indikkers naast de concentrator; herkomst OSM way 'Rajo Escondida', "
              "landuse=quarry resource=copper (ODbL)",
         noot="Zelfde verhaal als Collahuasi: concentraat per ±166 km slurry-pijp naar "
              "Coloso. Het spoor Antofagasta–Salta ligt op 6 km, maar rijdt dit "
              "concentraat niet — aanwijzen zou een trein tekenen die er niet is. "
              "⚠️ 1.485 m VERPLAATST bij de anker-check van 2026-07-28 (goedkeuring "
              "Lars): het OSM-punt lag op een bank ÍN de open put. Een put is geen "
              "laadplek — de slurry gaat de pijp in bij de indikkers achter de "
              "concentrator, en dáár begint de stroom (zelfde regel als Collahuasi)."),
    dict(id="cu-coloso-kade", grondstof="copper", fase="erts", rol="overslag",
         naam="Puerto Coloso — Escondida-concentraatpier (laadsteiger)",
         plek=[-70.46520, -23.75690], modi=["zee"], knooppunt="antofagasta",
         bron="SATELLIET-GELEGD op Esri World Imagery (z16, 2026-07-28) op de "
              "laadsteiger met de bulkcarrier eraan; herkomst OSM way 'Coloso', "
              "man_made=pier (ODbL)",
         noot="Escondida's eigen terminal, ±12 km ten zuiden van de haven Antofagasta "
              "waar data/copper.js hem heen stuurt. Hangt wél aan het aangewezen "
              "knooppunt Antofagasta — dáár zit de overslag naar het spoor. "
              "⚠️ 409 m VERPLAATST bij de anker-check van 2026-07-28 (goedkeuring Lars): "
              "het OSM-punt lag op de KUSTWEG bij het dorp Coloso; de laadsteiger steekt "
              "noordwestelijker de zee in."),
    dict(id="cu-beilun-kade", grondstof="copper", fase="erts", rol="overslag",
         naam="Ningbo-Zhoushan — Beilun ertsterminal, losberth (北仑矿石码头)",
         plek=[121.88300, 29.93640], modi=["zee"],
         bron="SATELLIET-GELEGD op Esri World Imagery (z16, 2026-07-28) op de losberth "
              "met de rode ertslossers; herkomst OSM node '北仑矿石码头', "
              "seamark:type=harbour (ODbL)",
         noot="De ertsterminal zelf, niet de containerkades ernaast — precies het "
              "onderscheid waarvoor deze laag bestaat. "
              "⚠️ 1.219 m VERPLAATST bij de anker-check van 2026-07-28 (goedkeuring "
              "Lars): het OSM-punt lag waar de TRANSPORTBAND aan land komt bij het "
              "ertsveld — het eind van de terminal, niet de plek waar het schip ligt. "
              "De losberth ligt noordoostelijker in het water. "
              "⚠️ PRIJS VAN DIE CORRECTIE, GEMETEN: de zee-snap wordt beter (2,4 → "
              "1,3 km) maar de SPOOR-snap slechter (0,2 → 1,3 km) — logisch, want de "
              "berth ligt in het water en het havenspoor eindigt bij het ertsveld. Eén "
              "punt kan niet tegelijk ligplaats én laadspoor zijn; als de spooraanhechting "
              "hier gaat knellen hoort dat een eigen aansluiting te worden (§3.4: de last "
              "mile is een eigen been), niet een compromis-coördinaat tussen de twee. "
              "⚠️ 2026-08-05: de spoorkant IS een eigen aansluiting geworden "
              "(cu-beilun-laadspoor, snap 0,198 km) — precies de tweede aansluiting die "
              "deze noot in 2026-07-28 aankondigde. Dit punt is daarmee zee-only."),
    dict(id="cu-beilun-laadspoor", grondstof="copper", fase="erts", rol="laadplek",
         naam="北仑港站 — laadsporen van het havenstation (Ningbo-Zhoushan)",
         plek=[121.87308, 29.92653], modi=["spoor"],
         bron="SATELLIET-GELEGD op Esri World Imagery (z19, 0,26 m/px, 2026-08-05): bundel "
              "van vijf parallelle sporen met VIER rode rail-mounted portaalkranen en "
              "wagons eronder; coördinaat uit zh.wikipedia 北仑港站 (29°55′35,5″N "
              "121°52′23,1″E), 4,5 m van OSM way 1491021972 (ODbL)",
         noot="HET TWEEDE ANKER VAN DE OVERSLAG BEILUN (werkwijze §2b). cu-beilun-kade is "
              "de losberth in het water, dit is het laadspoor; één punt kon niet allebei "
              "zijn. Dat stond sinds 2026-07-28 als openstaand punt §5.1 in de routebrief "
              "en is hiermee dicht. Routeerpunt = het kopeinde van de bundel "
              "29.92820/121.87380 (landnet-knoop 326694, tevens het beginpunt van het "
              "gebakken spoorbeen); max snap 0,198 km. "
              "⚠️ DATUMTOETS: as-is ligt het punt 4,5 m van het spoor; gelezen als GCJ-02 "
              "en omgerekend verschuift het 485 m NW naar 279,8 m van élk spoor, midden in "
              "een containerstapel. WGS-84 wint eenduidig — zelfde uitslag als bij Tianqi "
              "Jiangsu (zie v2/design/zoek-chinees-adres-recept.md). "
              "⚠️ PRODUCTCONFLICT, OPEN: wat hier satelliet-gelegd is, is een CONTAINER-"
              "emplacement (78万TEU, 中铁联合国际集装箱宁波北仑) terwijl ladder L3 van de "
              "brief 'natte bulk in open wagons' zegt. Geografisch waterdicht, inhoudelijk "
              "voorwaardelijk — een vraag aan de brief, niet aan de satelliet."),
    # ======================================================================
    # STROOM C — koperkathode Lobito → Rotterdam → Rijn → Duisburg
    # ======================================================================
    dict(id="cu-lobito-kade", grondstof="copper", fase="raffinaat", rol="overslag",
         naam="Lobito — Porto do Lobito, kade van de Lobito-corridor",
         plek=[13.54900, -12.34709], modi=["zee"], knooppunt="lobito",
         bron="OSM way 'Porto do Lobito', industrial=port landuse=harbour (ODbL)",
         noot="⚠️ OPEN — NIET SATELLIET-GELEGD. Bij de anker-check van 2026-07-28 bleek "
              "dit punt in het WATER van de baai te liggen. Er ís een eigen "
              "mineralenterminal (Lobito Atlantic Railway, eerste schip 12-07-2024, "
              "kathode naar Baltimore), maar op deze tegels — vermoedelijk van vóór de "
              "bouw — is de ligplaats niet aan te wijzen. Bewust géén verzonnen "
              "coördinaat; blijft staan tot de ligplaats bekend is. "
              "Het zee-eind van de Lobito-corridor; de Benguela-spoorlijn (CFB) ligt er "
              "1,1 km vandaan. Kathode gaat hier recht de Atlantische Oceaan op — zonder "
              "Kaap en zonder Malakka."),
    dict(id="cu-rotterdam-kade", grondstof="copper", fase="raffinaat", rol="overslag",
         naam="Rotterdam — RHB Stevedoring, Waalhaven Noordzijde 4",
         plek=[4.45850, 51.89350], modi=["zee", "binnen"], knooppunt="rotterdam",
         bron="SATELLIET-GELEGD op Esri World Imagery (z16, 2026-07-28) op de kade van "
              "RHB Stevedoring & Warehousing, Waalhaven Noordzijde 4, naast een "
              "afgemeerd schip; aangewezen via de PRODUCTVRAAG (kathode = LME-leverbaar "
              "→ LME-erkend entrepot, 1.060 m kade, non-ferro, colli tot 300 t)",
         noot="⚠️ 4.472 m VERPLAATST bij de anker-check van 2026-07-28 (goedkeuring "
              "Lars) — de grootste misser van de ronde. Het oude punt lag op de DIJK bij "
              "de woonwijk Heijplaat, 4,5 km ten westen van de Waalhaven, en steunde op "
              "'de buren binnen 1 km'. De productvraag loste in één stap op wat vier jaar "
              "'een pier in de Waalhaven' fout stond: kathode is LME-leverbaar metaal, "
              "dus het gaat naar een LME-erkend entrepot, en dat is in de Waalhaven RHB. "
              "Wat voor de pilot telt blijft gelden: ~30 km van de kolenkade op de "
              "Maasvlakte, en een ándere binnenknoop."),
    dict(id="cu-duisburg-kade", grondstof="copper", fase="raffinaat", rol="losplek",
         naam="Duisburg — Duisport Ruhrort, Becken A (kade)",
         plek=[6.75650, 51.45180], modi=["binnen"],
         bron="SATELLIET-GELEGD op Esri World Imagery (z16, 2026-07-28) op de kade met "
              "de stukgoedstapels; herkomst OSM way 'Becken A', harbour=yes (ODbL)",
         noot="Stukgoedbekken van de grootste binnenhaven ter wereld. OSM zegt niet welk "
              "bekken non-ferro doet; het onderscheid dat hier telt is dat kolen 7 km "
              "noordelijker lossen, aan de Schwelgern-pier bij het staalbedrijf. "
              "⚠️ 42 m VERPLAATST bij de anker-check van 2026-07-28: het punt stond net "
              "ín het bekken i.p.v. op de kade — precies de ~50 m die §2 van de "
              "routebrief-werkwijze bedoelt. Lars: correctie akkoord voor nu; wélk "
              "product er over déze kade gaat is nog niet vastgesteld (de productvraag "
              "staat hier dus nog open, anders dan bij de Waalhaven)."),

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
         naam="Jiangxi Copper Guixi — ertslosbundel (贵溪冶炼厂)",
         plek=[117.22600, 28.32710], modi=["spoor"],
         bron="SATELLIET-BEVESTIGD op Esri World Imagery (z18, 2026-07-28): parallelle "
              "sporen met wagons en twee portaalkranen over een losbunker; herkomst "
              "OSM way '贵溪冶炼厂', industrial=processing_plant (ODbL)",
         noot="De grootste kopersmelter ter wereld. Ligt 3,8 km noordelijker dan de "
              "node-coördinaat in data/copper.js (28,30 / 117,20) — op wereldniveau "
              "onzichtbaar, op straatniveau het verschil tussen smelter en veld. "
              "⚠️ DRIFT HERSTELD 2026-07-28: commit 73cf5d2 verplaatste dit punt van het "
              "polygoon-middelpunt naar de ertslosbundel, maar alleen in het GEGENEREERDE "
              "aansluitingen.json — deze lijst bleef op 117,2257/28,3338 staan, 741 m "
              "ernaast. Een regeneratie zou het satelliet-bevestigde punt stil hebben "
              "teruggedraaid; daarom staat de waarheid nu hier."),

    dict(id="cu-guixi-walsdraad", grondstof="copper", fase="raffinaat", rol="losplek",
         naam="江西铜业铜材有限公司 — walsdraadfabriek Guixi (冶金大道 19号)",
         plek=[117.21919, 28.33180], modi=[],
         bron="SATELLIET-GELEGD op Esri World Imagery (z18, 0,53 m/px, 2026-08-05). "
              "Coördinaat uit het nationale emissievergunningregister permit.mee.gov.cn "
              "V3.0, vergunning 913600007363561816001Q (行业类别 铜压延加工): verborgen "
              "velden longitude=117.21919 / latitude=28.33180 ÉN opelngd 117/13/9.08 + "
              "opelatd 28/19/54.48 — decimaal en DMS komen exact overeen",
         noot="EINDE VAN FASE D: de eerste bestemming van de kathode is de eigen "
              "walsdraadfabriek op hetzelfde complex (370 kt/j Φ8 mm walsdraad + 120 kt/j "
              "getrokken draad uit 贵冶牌-kathode). Op z18 ligt het punt op de zuidberm van "
              "de brede oost-west interne hoofdas (闪速大道 = de 物流主轴线 uit het "
              "terreinplan in 赣环监字（2017）第S007号), op de mond van een noord-zuid "
              "inrit; ZW ervan een ommuurd blok met sheddak-hal, ZO ervan vier lange "
              "donkere hallen. Het is een AANSLUITPUNT op die as, géén poort — op z18 is "
              "geen poortgebouw, slagboom of hek-onderbreking zichtbaar. "
              "⚠️ MODI IS BEWUST LEEG. Een weg-aanhechting is hier zinloos: het landnet "
              "heeft wereldwijd 1.883 wegknopen en de dichtstbijzijnde ligt op 341,1 km. "
              "De interne complexweg zit niet in het landnet, wél in OSM (way 1462532976, "
              "highway=service) — daar tekent het bakprofiel koper-guixi-fase-d op. Zelfde "
              "rolverdeling als cu-escondida-laad. Bijvangst: er ligt wél een landnet-"
              "SPOORknoop op 0,156 km; dat is een MEETRESULTAAT en geen bewijs dat de "
              "kathode het spoor op gaat — de modaliteit van de interne overbrenging is "
              "niet gedocumenteerd. "
              "⚠️ ADRES: 冶金大道 19号 (registerveld 生产经营场所地址), NIET 15号 zoals de "
              "routebrief zei — 15号 is het hoofdkantooradres van groep/beursvennootschap/"
              "加工事业部. De collocatie-conclusie klopt, de onderbouwing via 15 niet. "
              "⚠️ NEGATIEF ANKER op 1.749 m OZO: 江西铜业集团铜材有限公司 "
              "(28.32956/117.23688) is een ÁNDERE rechtspersoon (USCC 913606817442997892) "
              "met een eigen werk en eigen vergunning. Beide dragen 行业类别 铜压延加工 en "
              "beide noemen dezelfde 法定代表人 — verwar ze niet."),

    # ======================================================================
    # STROOM E — spodumeenconcentraat Greenbushes → Zhangjiagang (weg → zee → Yangtze)
    # Routebrief: v2/design/routebrieven/lithium-greenbushes-zhangjiagang.md
    # ⚠️ De VIERDE aansluiting uit §6.5 — `li-zjg-tianqi` (poort Tianqi Lithium
    #    Jiangsu, 东新路 5) — staat hier BEWUST NIET: die coördinaat is nog niet
    #    gelegd (§5, punt 5). Een aansluiting zonder satelliet-gelegde plek haalt
    #    precies de Waalhaven-klasse binnen die de werkwijze uitsluit.
    # ======================================================================
    dict(id="li-gb-laadplek", grondstof="lithium", fase="erts", rol="laadplek",
         naam="Greenbushes — concentraatloods / load-out (Talison)",
         plek=[116.05505, -33.86495], modi=["weg"],
         bron="SATELLIET-GELEGD op Esri World Imagery (z18, 2026-07-29): loods met "
              "load-out naast de mijnpoort; herkomst OSM-terrein Talison Greenbushes (ODbL)",
         noot="Waar het SC6-concentraat de roadtrain in gaat; 157 m van de mijnpoort "
              "(zuidkop Maranup Ford Road, -33,86376/116,05413 = OSM way 850829446). "
              "Het register houdt `li-greenbushes` bewust op de mijncentroïde — dit is de "
              "plek op straatniveau (de cu-guixi-spoor-rolverdeling). ⚠️ De wegcorridor "
              "`li-greenbushes-kemerton` in fetch_landnet.py stond 102 m hiervandaan en is "
              "2026-07-30 op deze waarde geconvergeerd (§6.3) — één redactionele waarde per plek."),
    dict(id="li-bun-berth8", grondstof="lithium", fase="erts", rol="overslag",
         naam="Bunbury — Berth 8, scheepslader (Southern Ports)",
         plek=[115.66385, -33.31995], modi=["zee"],
         bron="SATELLIET-GELEGD op Esri World Imagery (z18, 2026-07-29): scheepslader aan "
              "de kade van de binnenhaven; herkomst havenbron Southern Ports Bunbury",
         noot="Truck → zeeschip; hier komt de outload-band (2.000 t/h) van Shed 8-8 uit. "
              "⚠️ `li-port-bunbury` in data/lithium.js stond 2,2 km westelijker IN ZEE vóór "
              "de strandkust en is 2026-07-30 naar dit punt verplaatst (§6.2) — register en "
              "aansluiting vallen hier dus samen, anders dan bij Greenbushes. ⚠️ De "
              "bijbehorende LOSPLEK (Shed 8-8) is niet te leggen: het gebouw is jonger dan "
              "de Esri-opname, ook in de nieuwste Wayback-release (§5, punt 3)."),
    dict(id="li-zjg-kade", grondstof="lithium", fase="erts", rol="overslag",
         naam="Zhangjiagang — droge-bulkkade Zhangjiagang Port Group (张家港港务集团)",
         plek=[120.42050, 31.96800], modi=["binnen"],
         bron="SATELLIET-GELEGD op Esri World Imagery (z18, 2026-07-29): droge-bulkkade met "
              "kranen en stapelveld aan de zuidoever van de Yangtze",
         noot="Yangtze-schip → truck: einde van been 4, begin van de last mile naar Tianqi "
              "Lithium (Jiangsu). Welke van hun 16 ligplaatsen het is doet voor de kaart niet "
              "mee. ⚠️ Twee uitsluitingen uit de productvraag, want beide zijn plausibel én "
              "fout: de bonded-zone-kade bij de fabriek is GEEN ladingkade (patrouille-/"
              "marinabekken met helipad), en de steigers van het chemiepark zijn voor "
              "VLOEISTOF, niet voor droge bulk."),
    dict(id="li-zjg-tianqi", grondstof="lithium", fase="erts", rol="losplek",
         naam="天齐锂业（江苏）— poort 东新路 5, Zhangjiagang",
         plek=[120.45771, 32.01218], modi=[],
         bron="SATELLIET-GELEGD op Esri World Imagery (z18, 2026-08-05); coördinaat uit het "
              "nationale emissievergunningregister permit.mee.gov.cn (verborgen HTML-velden, "
              "decimaal én DMS), vergunning 91320592551155199K001U",
         noot="Einde van been 5 (last mile kade → raffinaderij). ⚠️ DEZE AANSLUITING STOND HIER "
              "BEWUST NIET sinds 2026-07-30: 'een aansluiting op een ongelegd punt ís de "
              "Waalhaven-klasse'. Die reden is vervallen — het punt is nu gelegd. "
              "⚠️ SATELLIET-GELEGD ALS VESTIGINGSPUNT AAN 东新路, NIET ALS GEKARTEERDE DEUR: op "
              "z18 is er een verharde berm met geparkeerde vrachtwagens, géén poortgebouw, géén "
              "slagboom, geen barrier-tag. Dat is de klasse 'een registerpunt is een vestiging, "
              "geen deur'. ⚠️ De UITGAANDE laadplek is niet gevonden; been 6 vertrekt daarom van "
              "ditzelfde punt en het terreinanker 32.01050/120.45650 (218,9 m) is NIET gebruikt. "
              "⚠️ Routeerpunt = projectie op OSM way 432043510 (24,9 m); de dichtstbijzijnde "
              "graafKNOOP ligt 79,5 m WEST, dus de lijn schiet er 75 m voorbij. ⚠️ MODI IS BEWUST LEEG: de gemeten weg-snap is 855 km. Het landnet heeft wereldwijd maar 1.883 wegknopen, dus dat is een MEETRESULTAAT en geen aansluiting — zelfde keuze als cu-guixi-walsdraad (341 km). De straat waarop het been aanhecht zit wél in OSM; daar tekent het bakprofiel op."),
    dict(id="li-wx-lgchem", grondstof="lithium", fase="raffinaat", rol="losplek",
         naam="乐友新能源材料（无锡）— laaddock westgevel (锡梅路 167号)",
         plek=[120.47518, 31.52362], modi=[],
         bron="SATELLIET-GELEGD op Esri World Imagery (z19, 0,25 m/px, 2026-08-05): twee rode "
              "opleggers onder een uitkragende laadluifel aan de westgevel van de noordelijke "
              "hal; 92 m ZW een tweede dock. 68,0 m van het EIA-anker uit het gemeentelijke "
              "milieurapport van Wuxi",
         noot="Einde van been 6 (kathodefabriek van de LG Chem/Huayou-JV). ⚠️ De UITGAANDE "
              "laadplek is niet gevonden: been 7 vertrekt van de ZUIDPOORT 31.52084/120.47492 "
              "(achthoekig poortpaviljoen met slagbomen), 310,1 m hiervandaan. Dat procesgat "
              "blijft bewust zichtbaar. Routeerpunt = 新鸿路 X252 op 126,3 m. ⚠️ MODI IS BEWUST LEEG: de gemeten weg-snap is 815 km. Het landnet heeft wereldwijd maar 1.883 wegknopen, dus dat is een MEETRESULTAAT en geen aansluiting — zelfde keuze als cu-guixi-walsdraad (341 km). De straat waarop het been aanhecht zit wél in OSM; daar tekent het bakprofiel op."),
    dict(id="li-nj-lges", grondstof="lithium", fase="product", rol="losplek",
         naam="LG Energy Solution Nanjing — New Port-campus (恒毅路 17号)",
         plek=[118.87953, 32.16111], modi=[],
         bron="SATELLIET-GELEGD op Esri World Imagery (z18, 2026-08-05): bedrijfsgebouw binnen "
              "het hek, met op dezelfde pass het rode LG-logo-monument ZW ervan; bbox-midden "
              "van OSM way 621624910 (33,97 ha)",
         noot="Einde van been 7 (celfabriek). ⚠️ HET BRIEFPUNT 32.16300/118.87900 WAS FOUT: dat "
              "lag 21,4 m BUITEN de perceelgrens in beboste helling met oude funderingen. Het "
              "stond als 'satelliet-gelegd op z16' — en z16 (2,0 m/px) kán dat verschil niet "
              "zien. ⚠️ OPEN EN BELANGRIJK: de polygoon draagt de PRE-split naam 乐金化学 "
              "(LG Chem), terwijl binnen 750 m twee expliciet LGES-genoemde genummerde percelen "
              "liggen (六工厂 698 m, 九工厂 749 m). Welk perceel de 2170-cellen voor Tesla maakt "
              "is NIET gedocumenteerd — dat is groter dan elk procesgat dat deze keten bewust "
              "laat staan. ⚠️ De uitgaande laadplek is niet gevonden; been 8 vertrekt van de "
              "hoofdpoort 恒谊路 32.15840/118.87950 (301,4 m). ⚠️ MODI IS BEWUST LEEG: de gemeten weg-snap is 785 km. Het landnet heeft wereldwijd maar 1.883 wegknopen, dus dat is een MEETRESULTAAT en geen aansluiting — zelfde keuze als cu-guixi-walsdraad (341 km). De straat waarop het been aanhecht zit wél in OSM; daar tekent het bakprofiel op."),
    dict(id="li-sh-tesla", grondstof="lithium", fase="product", rol="losplek",
         naam="Tesla Giga Shanghai — poort 3 (江山路 5000号, Lingang)",
         plek=[121.76667, 30.87423], modi=[],
         bron="SATELLIET-GELEGD op Esri World Imagery (z19, 0,26 m/px, 2026-08-05): brug over "
              "het kanaal, wachtersgebouw op een verkeerseiland met luifel over de rijstroken, "
              "vrachtwagens in de rij, direct oostelijk de fabrieksapron. 18,2 m BINNEN OSM-way "
              "635670279 (特斯拉上海超级工厂, operator=Tesla (Shanghai))",
         noot="HET EINDE VAN DE KETEN — de tweede stroom van de atlas die van de mijn tot het "
              "eindproduct loopt (na grafiet). ⚠️ HET BRIEFPUNT 30.87390/121.76572 BESTOND NIET "
              "ALS POORT: dat was het REKENKUNDIG MIDDEN VAN VIER OSM-BUSHALTENODES (特斯拉3号门, "
              "alle highway=bus_stop), 1,0 m van de publieke straat 正嘉路 aan de WESTKANT van "
              "het kanaal en 60,9 m BUITEN de fabriekspolygoon — een been dat daar eindigt "
              "eindigt op een openbare weg aan de verkeerde kant van het water. ⚠️ De LOSPLEK "
              "binnen het terrein is niet gedocumenteerd; de keten eindigt op de poort. "
              "⚠️ Verklikker-kalibratie: de bushaltes liggen 98 m van deze poort, dus een "
              "verbodsstraal van 150 m zou het JUISTE antwoord afkeuren — zet hem op 50 m. ⚠️ MODI IS BEWUST LEEG: de gemeten weg-snap is 854 km. Het landnet heeft wereldwijd maar 1.883 wegknopen, dus dat is een MEETRESULTAAT en geen aansluiting — zelfde keuze als cu-guixi-walsdraad (341 km). De straat waarop het been aanhecht zit wél in OSM; daar tekent het bakprofiel op."),

    # ======================================================================
    # GRAFIET — Balama → Nacala → New Orleans → Vidalia → De Soto → Casa Grande
    # De eerste keten van de atlas die van de mijn tot het eindproduct loopt.
    # ⚠️ Fase D/E dragen VANDAAG NUL VOLUME (besluit Lars 2026-08-04): de weg
    # is gemeten, de lading nog niet. Dat staat in de brief en in de node-noten,
    # niet in de lijnstijl.
    # ======================================================================
    dict(id="gr-balama-laadplek", grondstof="graphite", fase="erts", rol="laadplek",
         naam="Balama — bagging + truckbelading op de plant",
         plek=[38.66000, -13.31000], modi=["weg"],
         bron="SATELLIET-GELEGD op Esri World Imagery (z16, 2026-07-28, ankercheck) + "
              "OSM industrieterrein/pits (ODbL)",
         noot="Begin van de keten. Uitgaand vlokconcentraat in 1-t-zakken; het spoor naar "
              "Nacala wordt aantoonbaar NIET gebruikt (Grindrod pit-to-port is expliciet weg)."),
    dict(id="gr-nacala-kade", grondstof="graphite", fase="erts", rol="overslag",
         naam="Porto de Nacala — containerterminal oostoever",
         plek=[40.66730, -14.53830], modi=["zee", "weg"],
         bron="SATELLIET-GELEGD op Esri World Imagery (z16, 2026-07-28)",
         noot="Truck → zeeschip. ⚠️ Het onderzoekspunt (-14.531, 40.652) lag in OPEN WATER "
              "bij de kolen-jetty op de WESToever — nota bene de terminal die volgens de "
              "routebrief niet bij deze stroom hoort. Tweede 'bevestigde' punt dat visueel "
              "fout bleek; alleen een gestitchte pass loste het op. ⚠️ Het Grindrod Cross "
              "Dock (waar de zakken in containers gaan) heeft géén gepubliceerde coördinaat "
              "en is bewust NIET gelegd."),
    dict(id="gr-nola-napoleon", grondstof="graphite", fase="erts", rol="overslag",
         naam="Port of New Orleans — Napoleon Avenue Container Terminal",
         plek=[-90.11200, 29.91230], modi=["zee", "binnen"],
         bron="SATELLIET-GELEGD op Esri World Imagery (z16, 2026-07-28); 489 m verplaatst "
              "vanaf de stadscentroïde",
         noot="Zeeschip → binnenvaart. De oude centroïde werd langs een onafhankelijke weg "
              "ontmaskerd: van 510.752 VS-AIS-tracks kwam er GEEN binnen 0,5 km. Na de "
              "correctie schoof het anker 490 m en het geroutete punt maar 154 m — de "
              "gemeten demonstratie van anker ≠ routeerpunt."),
    dict(id="gr-portallen-kade", grondstof="graphite", fase="erts", rol="overslag",
         naam="Port Allen — IRMT 200-ft bargekade (Slack Water Canal)",
         plek=[-91.24383, 30.43313], modi=["binnen"],
         bron="SATELLIET-GELEGD op Esri World Imagery (z19, 2026-08-04): kadefront 59 m ≈ de "
              "gepubliceerde 200 ft; bevestigd door 51 MarineCadastre-pings binnen 50 m",
         noot="⚠️ DE VONDST VAN DEZE RONDE: de terminal ligt NIET aan de doorgaande vaarweg "
              "maar aan een DOODLOPEND ZIJKANAAL dat er enkele km westelijker vanaf takt. "
              "Daarom moest de ankercheck van 2026-07-28 wel mislukken — die zocht langs de "
              "GIWW. Het oude punt stond 2,08 km fout en hing als losse marker naast de lijn. "
              "Aankomst (been 3) en vertrek (been 4) vallen hier fysiek samen: er is precies "
              "één bargeligplaats — géén compromis-coördinaat maar een gemeten feit. "
              "Routeerpunt in de vaargeul: 30.43293 / -91.24385 (22 m). ⚠️ Voorwaardelijk: "
              "blijft de modus New Orleans → Port Allen truck in plaats van shuttle-barge, "
              "dan is het aankomstanker de terminalpoort en die is niet gelegd."),
    dict(id="gr-vidalia-kade", grondstof="graphite", fase="erts", rol="overslag",
         naam="Port of Vidalia — apron achter de cargo ramp (rivier-mijl 359)",
         plek=[-91.48255, 31.53645], modi=["binnen", "weg"],
         bron="SATELLIET-GELEGD op Esri Wayback-release 22252 (2026-01-29), gelegd 2026-08-04",
         noot="Binnenvaart → truck. ⚠️ Het oude briefpunt (31.538, -91.485) ligt in "
              "BATTURE-BOS: geen kade, geen ramp, geen verharding. De echte faciliteit ligt "
              "~290 m ZO. Alleen een wolkenvrije Wayback-opname toonde dat; op het live beeld "
              "was het niet te zien. Ramp-/transportbandkop = routeerpunt 31.53530 / -91.48090; "
              "max snap 0,45 km (dichtstbijzijnde graafknoop 444 m). ⚠️ Open vraag aan de "
              "brief, niet aan de tegels: deze stroom is CONTAINERvormig terwijl de bestaande "
              "havenfase een cargo ramp + t-dock voor droge BULK is."),
    dict(id="gr-vidalia-fabriek", grondstof="graphite", fase="raffinaat", rol="losplek",
         naam="Syrah Technologies — AAM-fabriek Vidalia",
         plek=[-91.48870, 31.54660], modi=["weg"],
         bron="SATELLIET-GELEGD 2026-07-28 (ankercheck) + DOE/EA-2181 Fig. 1 'Project Center' "
              "31.54653 / -91.48868 (8 m — onafhankelijke tweede bron)",
         noot="Einde fase C, begin fase D. Routeerpunt = de fabriekspoort 31.54796 / -91.48743 "
              "(EA-2181 'Front Gate' + OSM-knoop op 6 m). ⚠️ Het terrein grenst aan D.A. "
              "BIGLANE ROAD, niet aan LA-131 zoals de brief zei. ⚠️ Het UITGAANDE AAM-laaddock "
              "is NIET gelegd: z19 is de fijnste Esri-korrel en toont geen perron. Been 6 "
              "begint daarom bij de poort, niet bij het dock."),
    dict(id="gr-amp1-dock", grondstof="graphite", fase="product", rol="losplek",
         naam="Lucid AMP-1 Casa Grande — inkomende dockrij westgevel",
         plek=[-111.78008, 32.85724], modi=["weg"],
         bron="SATELLIET-GELEGD op Esri World Imagery (z19, 2026-08-04): rij opleggers "
              "kont-aan-gevel over ~330 m + truck-apron; Wayback 32246 identiek aan live",
         noot="Het eind van de keten — de eerste stroom van de atlas die tot een "
              "consumentenproduct loopt. Anker = het MIDDEN van een dockrij van ~330 m, geen "
              "aangewezen deur; welke deuren inkomend zijn is niet publiek. Routeerpunt = "
              "westpoort West Selma Highway 32.85035 / -111.78238. UITGESLOTEN: de autoparking "
              "aan de zuidkant is de UITGAANDE kant, de oostgevel is personeelsparking, het "
              "noordblok is nog in aanbouw. Geen spoor op het terrein (dichtstbijzijnde stomp "
              "193 m buiten de terreingrens) — ondersteunt truck boven intermodaal spoor."),
]

MODI = ("zee", "binnen", "spoor", "weg")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true", help="aansluitingen.json wegschrijven")
    ap.add_argument("--marnet", type=Path, default=MARNET_STD,
                    help="map met marnet.bin + marnet.json (default: "
                         "v2/build-cache/marnet-preais; ze horen NIET in v2/data)")
    args = ap.parse_args()

    if not (args.marnet / "marnet.json").exists():
        print(f"⚠️ geen marnet.json in {args.marnet}\n"
              f"   terugzetten met:  git show pre-ais-net:v2/data/marnet.json > "
              f"{args.marnet / 'marnet.json'}", file=sys.stderr)
        return 1

    ports = json.loads((DATA / "ports.json").read_text(encoding="utf-8"))
    zee_knopen = ports["zeeKnopen"]

    print("marnet lezen…", flush=True)
    m_meta, m_lon, m_lat = mk.lees_knopen(args.marnet / "marnet.json",
                                          args.marnet / "marnet.bin")
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
        "bron": ("coördinaten uit OpenStreetMap (ODbL) via verken_terminals.py; "
                 "de punten met 'SATELLIET-GELEGD' in hun `bron` zijn daarna op "
                 "Esri World Imagery (z16-z18) verlegd volgens routebrief-"
                 "werkwijze §2 — de OSM-herkomst blijft per punt vermeld"),
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
