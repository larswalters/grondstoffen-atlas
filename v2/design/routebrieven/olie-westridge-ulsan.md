# Routebrief (licht) · olie — Westridge Marine Terminal (Canada) → Ulsan (Zuid-Korea)

**stroom-id:** `olie-westridge-ulsan` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 4) ·
**status:** gebakken
**Keten in één zin:** Canadese oliezandcrude (Cold Lake-type) vanaf de Westridge Marine Terminal (Trans Mountain
Corporation) in Burnaby, BC — de zeeterminus van de in mei 2024 geopende Trans Mountain-uitbreiding — per tanker
over de Straat van Georgia/Juan de Fuca en de Noord-Pacific grote cirkel naar het SK Energy Ulsan-raffinagecomplex
in Zuid-Korea **(aannemelijk: één bron)**.
**Welke as van het verhaal:** RESERVE-as uit golf 2 (spiegelbeeld van de VS-schalie-ommekeer Corpus
Christi→Rotterdam) — door de haalbaarheidstoets al aangemerkt als het **zwakste van de zes olie-ontwerpen**: het
merendeel van de Westridge-lading blijft naar de Amerikaanse westkust gaan, en cargo-niveau bewijs specifiek voor
Ulsan (i.p.v. Yeosu of een andere Aziatische haven) ontbreekt — zie §7.

## 1 · Ketenkaart
```
Westridge Marine Terminal `ol-westridge-term` (Burrard Inlet, Burnaby BC — TMX-zeeterminus)
  ──(b1 zee · Straat van Georgia/Juan de Fuca → grote cirkel Noord-Pacific · ~8.213 km grote cirkel,
      aannemelijk: één bron)──►
Ulsan-raffinagecomplex (SK Energy) `ol-ulsan-sk` (Ulsan, Zuid-Korea) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | Westridge Marine Terminal → Ulsan-raffinagecomplex (SK Energy) (aannemelijk: één bron) | Straat van Georgia/Juan de Fuca → Noord-Pacific grote cirkel | grote cirkel 8.213 km [eigen berekening]; ontwerp-schatting ~8.700 km [ontwerp] | MARNET (kade → kade) | nee — beide kades binnen de 25 km-snapgrens (Westridge 1,4 km, Ulsan 5,4 km); Ulsan > 5 km van zijn zeeknoop → haven-aanloop nodig (LAR-586) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-westridge-term` | laadplek / exportterminal (TMX-zeeterminus) | Westridge Marine Terminal (Trans Mountain Corporation), Burrard Inlet, Burnaby BC | 49.2932, -122.9560 | [4][5][7] | bron-gelegd (z17 gezien: twee offshore dolphin-aanlegsteigers, via een trestle met het wal-tankenpark verbonden; op de opname lagen twee tankers afgemeerd aan de twee berths) |
| `ol-ulsan-sk` | losplek / raffinaderij (stoppunt) | SK Energy Ulsan-raffinagecomplex (Ulsan Complex) | 35.43317, 129.3429 | [6][8] — coördinaat **hergebruikt** uit `v2/data/gloednodes-olie.json` (site-id `w-ulsan`), niet opnieuw gelegd | bron-gelegd (hergebruikt anker; eerder z14 gezien: kruis midden in het Ulsan-industriecomplex, tankenparken/procesinstallaties/havenkom rondom zichtbaar; bij deze ronde herbevestigd op z15: dicht net van procesinstallaties en tankenparken, havenbekken met tankschepen ~1-2 km NO) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
*n.v.t. — deze keten heeft geen landbenen; b1 is een enkel MARNET-geroutet zeebeen zonder corridorkeuze.*

## 5 · Verwerkingsknopen
*Geen verwerkingsknoop in deze brief — het Ulsan-raffinagecomplex is zelf het stoppunt (§6), geen tussenknoop.*

## 6 · Stoppunt
De brief stopt bij het SK Energy Ulsan-raffinagecomplex: dit is de enige Zuid-Koreaanse bestemming waarvoor een
(indirecte) koppeling aan een Trans Mountain/Cold Lake-cargo bestaat (§7). Fase C/D (productstromen vanaf de
raffinaderij) vervallen — geen bron koppelt een specifiek productexportspoor aan deze crude-instroom.

## 7 · Open punten
- **Zwakste bewijslast van de zes olie-assen (expliciet zo gemarkeerd in de haalbaarheidstoets).** Dit is de
  enige olie-as van deze golf waarbij de bestémming zelf onzeker is, niet alleen het volume.
- **SK Energy's aankoop van 550.000 vaten Cold Lake-crude (via handelaar Unipec, geboekt voor levering september
  2024) is de enige directe cargo-koppeling aan SK Energy** [2]. Geen bron noemt expliciet dat déze lading bij de
  Ulsan-raffinaderij is gelost — het bewijs steunt op het feit dat Ulsan Complex SK Energy's grootste (en enige
  grote) raffinaderij is, geen cargo-niveau bevestiging van de losplek zelf.
- **Concurrerend bewijs wijst sterker naar Yeosu (GS Caltex), niet Ulsan.** In dezelfde cargo-familie (september
  2024) nam GS Caltex 300.000 vaten af, expliciet bestemd voor de Yeosu-raffinaderij [2][3]. Dat maakt Yeosu op
  dit moment de béter gedocumenteerde Zuid-Koreaanse Trans Mountain-bestemming dan Ulsan — precies de
  heroverweging die de haalbaarheidstoets vroeg ("herverifieer welke Aziatische bestemming het meeste
  cargobewijs heeft"). De opdracht vroeg specifiek de Ulsan-as, dus die is hier uitgewerkt; `olie-westridge-yeosu`
  is een kandidaat voor een sterker onderbouwde toekomstige as.
- **Geen structureel jaarvolume specifiek voor deze stroom.** Enige harde cijfers: de eenmalige SK Energy-cargo
  (550.000 vaten, sept 2024, eenheid kb) en het landelijke aggregaat Canada→Zuid-Korea — **CAD$411 mln / 4,54 mln
  vaten over mei 2024–sept 2025** (~17 maanden, over vier Zuid-Koreaanse raffinaderijen samen, dus niet
  Ulsan-specifiek) [3]. Westridge/TMX-terminalcapaciteit totaal 890 kb/d (peiljaar 2024), waarvan het merendeel
  naar de VS-westkust gaat (§ ontwerp-risico).
- **Zeeknoop-afstand Ulsan (5,38 km) ligt net boven de 5 km-grens** → bij het bakken een haven-aanloop nodig
  tussen kade en zeeknoop (LAR-586), ook al ligt de kade ruim binnen de 25 km-snapgrens.
- Geen extra Geofabrik-extract nodig (geen landbeen); geen spoornet nodig.

## 8 · Bronnen
[1] Wikipedia, "Trans Mountain pipeline" — TMX-uitbreiding operationeel 1 mei 2024, capaciteit 300.000 → 890.000
    vaten/dag, Westridge Marine Terminal in Burrard Inlet, Burnaby BC. https://en.wikipedia.org/wiki/Trans_Mountain_pipeline
[2] Hydrocarbon Processing, 07-2024, "Japan, S. Korea refiners join China in buying Canadian TMX oil" — GS Caltex
    300.000 vaten (bestemd voor de Yeosu-raffinaderij) + ENEOS (Japan) 250.000 vaten, gedeelde Cold Lake-cargo via
    Chevron, levering sept 2024; SK Energy 550.000-vaten cargo via handelaar Unipec, levering sept 2024 (raffinaderij
    niet met naam genoemd). https://www.hydrocarbonprocessing.com/news/2024/07/japan-s-korea-refiners-join-china-in-buying-canadian-tmx-oil/
[3] DiscoveryAlert, 2026, "Canadian Crude Exports to South Korea Surge Amid Supply Crisis" — GS Caltex testcargo
    sept 2024 (300.000 vaten, gedeeld met ENEOS, → Yeosu); HD Hyundai Oil Bank 548.000 vaten april 2025 (raffinaderij
    niet genoemd); SK Energy in langetermijncontractonderhandelingen; totaal Canada→Zuid-Korea mei 2024–sept 2025:
    CAD$411 mln / 4,54 mln vaten, over vier Zuid-Koreaanse raffinaderijen (SK Energy/GS Caltex/S-Oil/HD Hyundai Oil
    Bank). https://discoveryalert.com/canadian-crude-south-korea-geographic-diversification-2026/
[4] OpenStreetMap/Nominatim (ODbL) — "Westridge Marine Terminal", landuse=industrial, Lochdale, Burnaby BC,
    centroid 49.2886831/-122.9540563. https://www.openstreetmap.org
[5] Trans Mountain Corporation — officiële terminalpagina, bevestigt Westridge Dock als het enige tanker-laadpunt
    van het TMX-systeem. https://www.transmountain.com/westridge-marine-terminal
[6] Zoekresultaat/snippet (Google-index van OGJ/vakpers) — "SK Energy... Ulsan Complex... refining capacity of
    840,000 barrels of crude oil per day", grootste raffinaderij van Zuid-Korea. https://www.ogj.com/refining-processing/refining/article/14115305/sk-energy-adds-new-unit-at-ulsan-refining-complex
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15/z17) — `sat-olie-westridge-ulsan-westridge.png`,
    `sat-olie-westridge-ulsan-westridge-dock.png`.
[8] `v2/data/gloednodes-olie.json` (site-id `w-ulsan`) — SK Energy Ulsan-raffinaderij, 35.43317/129.3429, capaciteit
    840 kb/d (Statista/Korea Times 2023 [B48][B49] binnen die sitelaag), satelliet z14 al gelegd in een eerdere
    sitelaag-ronde (bron-gelegd), hier letterlijk hergebruikt.
[9] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `sat-olie-westridge-ulsan-ulsan-reuse.png`
    (herbevestiging van het hergebruikte anker).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 4)

**Stroom `olie-westridge-ulsan`** → `v2/data/stroomroute-olie-westridge-ulsan.json` — 2 benen, **8.677,4 km**, 897
punten, 2 markers (1 stippel). Recept: `bak_stromen.sh` (functie `bak_olie_westridge_ulsan`).

**b1 (zee, MARNET-route, kade → kade):** `--been "zee|zeeschip Westridge Marine Terminal → Ulsan-raffinagecomplex
(SK Energy) (aannemelijk: één bron)|49.2932,-122.9560|35.43317,129.3429"` — snap Westridge **1,43 km** (ruim
binnen de 5 km-norm, geen haven-aanloop nodig aan de Canadese kant, conform de zeeknoop-check uit de brief), snap
Ulsan **5,38 km** (boven de 5 km-grens, LAR-586-plicht ondanks ruim binnen de 25 km-snapgrens). **8.672,0 km**, 895
punten, tegen de eigen grote-cirkelberekening van 8.213,3 km = **+5,6%**, en tegen de ontwerp-schatting ~8.700 km
= **−0,3%**. Er is geen gepubliceerde ladingroute-lengte om tegen te toetsen (brief §2/§7) — de ±15%-norm geldt
hier dus als indicatie, niet als harde toets, en beide vergelijkingen vallen ruim binnen die indicatie. De
getekende lijn loopt via de Straat van Georgia/Juan de Fuca (zes krappe bochten 68–98° bij de Canadese kust, alle
zes reële navigatie door het nauwe kanaal, geen enkele terugloop) en dan de Noord-Pacific grote cirkel naar Korea
— geen verkeerde-tak-signaal aangetroffen.

**b2 (zee, stippel, haven-aanloop Ulsan):** `maak_havenaanloop.py --van 35.43317,129.3429 --naar
35.46180,129.39080` liep vast op `timeout 300` (exit 124) — geen tweede poging, zoals de bak-aanwijzing
voorschrijft. Terugval: rechte stippel `--stippel "zee|haven-aanloop Ulsan (schematisch — 1:10M-kust kent de kade
niet)|35.46180,129.39080|35.43317,129.3429"`. ⚠️ **Puntvolgorde bewust OMGEDRAAID t.o.v. de letterlijke
bak-aanwijzing** (die gaf kade→zeeknoop, gespiegeld aan de `--van`/`--naar` van de mislukte
`maak_havenaanloop.py`-poging): met kade→zeeknoop eindigt b2 op dezelfde zeeknoop-coördinaat als b1 al bereikte,
wat een naad van 5,38 km tussen b1 en b2 meet én de getekende lijn nooit op het kade-anker laat eindigen (b1 en b2
lopen dan over dezelfde 5,38 km heen en weer i.p.v. door te lopen). Zeeknoop→kade (dit patroon, identiek aan de
bestaande `bak_zilver_penasquito_onsan`-functie voor exact dezelfde Onsan-zeeknoop) sluit b2's eerste punt aan op
b1's laatste punt en laat de lijn eindigen op de kade, waar de marker `ol-ulsan-sk` staat. **5,4 km**, 2 punten.

**Naad tussen b1 en b2: 0,00 km** (na de omgedraaide puntvolgorde) — de haven-aanloop sluit de 5,38 km-snap van
Ulsan volledig, precies de LAR-586-regel.

**Markers:** `ol-westridge-term` (0,00 km van de b1-lijn — startpunt) · `ol-ulsan-sk` (0,00 km — eindpunt van b2,
het kade-anker zelf).

**Toets:** `toets_knikken.py` — 6 knikken ≥60° (98,1° tot 68,2°, allemaal krappe bochten in de Straat van
Georgia/Juan de Fuca bij de Canadese kust, R 1.311–7.234 m), **0 omkeringen ≥150°, 0 terugloop** — geen bevinding.
`toets_rechte_benen.py --min-km 5` — b2 (5,4 km, omwegfactor 1,003) staat op de lijst als 🟡 MIDDEL (stippel):
correct, het is een bewuste rechte stippellijn na een mislukte `maak_havenaanloop.py`-poging, geen bevinding op
zichzelf. json geldig: versie 2, punt_formaat lonlat, modaliteit `zee` (enige modaliteit, in de toegestane set),
elk been ≥2 punten (895/2), bestandsgrootte **17,8 KB** (ruim < 300 KB).

**Toelichting op de stippel:** de haven-aanloop bij Ulsan is uitsluitend "hier reikt het net niet" (MARNET routeert
kade→kade via zeeknopen, niet tot de kade zelf zodra die >5 km van haar zeeknoop ligt); "aannemelijk: één bron"
voor de Ulsan-bestemming staat in de beennaam van b1 en in brief §7, niet in de lijnstijl van b1 zelf (b1 is
volledig doorgetrokken/gemeten, geen stippel).

**Gereedschapslessen:**
- De puntvolgorde van een destination-side haven-aanloop (ná het zeebeen) hoort **zeeknoop → kade** te zijn, niet
  kade → zeeknoop — ook als de mislukte `maak_havenaanloop.py`-poging met `--van kade --naar zeeknoop` liep. De
  `--van`/`--naar`-richting van de aanroep en de puntvolgorde van de resulterende `--stippel`-regel in de
  bak-functie zijn twee losse keuzes; alleen de laatste bepaalt of de naad-toets (b[i-1] laatste punt = b[i] eerste
  punt) een reëel gat meet of een schijngat door de verkeerde richting. Zie het bestaande patroon in
  `bak_zilver_penasquito_onsan` (dezelfde Onsan-zeeknoop, b4: zeeknoop→kade) — dat patroon is nu ook hier gevolgd.
- Een `--stippel` in de verkeerde richting laat de lijn niet op het bestemmingsanker eindigen, ook al is de marker
  zelf op 0 km van een lijnpunt (marker = het been-startpunt, niet het eindpunt) — de naad-toets is hier de
  betrouwbaardere indicator dan de marker-afstand alleen.
