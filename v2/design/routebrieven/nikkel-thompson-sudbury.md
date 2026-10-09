# Routebrief (licht) · nikkel — Thompson → Winnipeg → Sudbury (Canada)

**stroom-id:** `nikkel-thompson-sudbury` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**Keten in één zin:** nikkelconcentraat van Vale's Thompson-concentrator (Manitoba) gaat per **spoor** over één doorlopende
lijn van ~2.690 km — Thompson → The Pas → Winnipeg → Hornepayne → Foleyet → Capreol — naar Vale's Copper Cliff-complex in Sudbury
(Ontario). Alleen spoor, geen zee, geen stippel. Aannemelijk (één bron): Vale noemt Sudbury als directe spoorbestemming,
maar zegt niet welk deel erheen gaat en welk deel via Winnipeg of Trois-Rivières naar Long Harbour [2][3]. Stoppunt Copper Cliff.
**Welke as van het verhaal:** de Manitoba-nikkelketen — Canada's tweede nikkelcluster voedt per trein de Ontario-smelter.
**7,9 kt Ni/j** finished nickel uit Thompson-ore (2023; 9,9 in 2022, 5,9 in 2021), Vale 20-F FY2023 [2]. Eenheid: kt Ni per jaar.
(De schatting 19–28 kt uit het ontwerp is achterhaald: die was afgeleid uit "10–15% van Canada" [1], Vale's eigen cijfer is lager.)

## 1 · Ketenkaart
```
Thompson-emplacement `ni-thompson-emplacement` (Vale, load-out aannemelijk)
   ──(b1 spoor · Hudson Bay Railway (HBRY) Thompson-lijn via Wabowden · ~370 km)──► The Pas (53.8245, -101.2506)
   ──(b2 spoor · The Pas → Hudson Bay (SK) → Canora → Portage la Prairie → Winnipeg · ~792 km)──► Winnipeg, Symington Yard (49.8688, -97.0480)
   ──(b3 spoor · hoofdlijn Winnipeg → Sioux Lookout → Hornepayne · ~1.015 km)──► Hornepayne (49.2167, -84.7833)
   ──(b4 spoor · Hornepayne → Foleyet · ~237 km)──► Foleyet (48.2439, -82.4397)
   ──(b5 spoor · Foleyet → Capreol · ~239 km)──► Capreol (46.7058, -80.9214)
   ──(b6 spoor · Capreol → Sudbury → Copper Cliff · ~38 km)──► Copper Cliff-smelter `ni-coppercliff-smelter` ── stoppunt
```
Alternatieven die Vale noemt maar niet getekend zijn: Winnipeg of Trois-Rivières → schip → Long Harbour (Newfoundland) [2][4].

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `ni-thompson-emplacement` → The Pas | HBRY-lijn Thompson–Wabowden–The Pas [6] | OSM-graaf **369,6** · hemelsbreed 305,7 · geen gepubliceerde lengte | toets_spoorroute | nee (snap 0,11 km) |
| b2 | A | spoor | The Pas → Winnipeg (Symington) | via Hudson Bay (SK), Canora en Portage la Prairie (route ligt 1–3 km van die plaatsen, 86–91 km van Dauphin/Swan River); exacte lijn en vervoerder niet gebrond | OSM-graaf **791,8** · hemelsbreed 525,9 · geen gepubliceerde lengte | toets_spoorroute | nee |
| b3 | A | spoor | Winnipeg → Hornepayne | transcontinentale hoofdlijn (ex-Canadian Northern, CN aannemelijk) via Sioux Lookout [9] | OSM-graaf **1.015,2** · hemelsbreed 886,9 · geen gepubliceerde lengte | toets_spoorroute | nee |
| b4 | A | spoor | Hornepayne → Foleyet | ex-Canadian Northern-lijn Winnipeg–Capreol [8] | OSM-graaf **236,9** · hemelsbreed 203,1 | toets_spoorroute | nee |
| b5 | A | spoor | Foleyet → Capreol | idem [8][10] | OSM-graaf **238,7** · hemelsbreed 205,6 | toets_spoorroute | nee |
| b6 | C | spoor | Capreol → `ni-coppercliff-smelter` | CN/Sudbury-net naar het Copper Cliff-complex | OSM-graaf **37,5** · hemelsbreed 27,2 | toets_spoorroute | nee (snap 0,09 km) |
Totaal **2.689,7 km** over 6 runs (hemelsbreed Thompson–Copper Cliff 1.552 km, verhouding 1,73 — het spoor moet om de Canadese Schild).
Geen gepubliceerde spoorkm: de ±15%-toets is hier **een indicatie, geen norm**. Geen last-mile-been aan beide kanten (load-out en smelter liggen < 2 km van het net).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-thompson-emplacement` | concentrator-load-out / kop van het spoor | Thompson-emplacement (Vale-concentraat) | 55.7407, -97.8300 | [1][2][5][11] | aannemelijk (z15 gezien: groot emplacement met tientallen sporen en loodsen aan de zuidoostrand van de stad; de Vale-industrie ligt 1,3 km zuidoostwaarts. Welke spoorstomp de load-out is, is niet te onderscheiden) |
| `ni-coppercliff-smelter` | smelter / losplek | Vale Copper Cliff-complex, Sudbury | 46.4786, -81.0547 | hergebruikt uit `pgm-sudbury-actonuk` [13] | bron-gelegd (daar z15 gezien, nu opnieuw z15: smelter met superschoorsteen, ertsstapels en sporenbundel direct rond het punt) |

## 4 · Via-punten (alleen spoor; elk pint een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1/b2 | 1 | The Pas | 53.8245, -101.2506 | splitsing HBRY-Thompson-lijn en de zuidwaartse corridor; snap 0,21 km |
| b2/b3 | 2 | Winnipeg, Symington Yard (westkant) | 49.8688, -97.0480 | zet de reis op de oostwaartse hoofdlijn in plaats van de omkering op een dood spoor bij 49.861/-97.032 die een vrije run koos; ligt in het rangeerterrein (z14 gezien: groot rangeerterrein, [7]), snap 0,01 km |
| b3/b4 | 3 | Hornepayne | 49.2167, -84.7833 | houdt de route op de ex-Canadian Northern-lijn en voorkomt de omweg via Chapleau (CP-kant, 538 km vanaf Hornepayne in de vrije run); snap 0,69 km |
| b4/b5 | 4 | Foleyet | 48.2439, -82.4397 | tussenstop op de CN-lijn naar Capreol [8]; snap 0,24 km |
| b5/b6 | 5 | Capreol | 46.7058, -80.9214 | laatste knoop vóór Sudbury, divisiepunt [10]; snap 0,27 km |
Geen stadscentra: alle vijf zijn spoorknopen of -terreinen. De zes runs sluiten met naden van 0,00 km en geven bij een 10 km-venster geen omkering ≥ 140°.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Thompson (mijn + concentrator) | Vale Canada | erts (682 kt, 1,9% Ni in 2023) → nikkelconcentraat; smelter en raffinaderij dicht sinds 2018 | 7,9 kt Ni finished/j (2023) | [2][3] |
| Copper Cliff / Sudbury integrated operations | Vale Canada | Thompson-concentraat + eigen en externe feed → matte → nikkel (CCNR) | niet gebrond per feed | [2] |

## 6 · Stoppunt
De brief stopt bij Copper Cliff: wat de smelter verlaat (matte, PGM-residu) staat in `pgm-sudbury-actonuk`; fase D/E vervalt, geen bron noemt een vervolgzending van Thompson-nikkel specifiek.

## 7 · Open punten
- **Verdeling Sudbury / Long Harbour** staat nergens: Vale zegt alleen "Sudbury en/of Long Harbour, afhankelijk van de vraag" [2][3]. De getekende lijn is de directe spoorroute naar Sudbury, geen aandeel. Het jaarvolume (7,9 kt) is voor héél Thompson, niet voor deze lijn alleen.
- **Exacte load-out** in Thompson niet gevonden; `ni-thompson-emplacement` blijft *aannemelijk* (Vale investeerde > 100 mln in de concentraat-load-out [5], de plek zelf niet gebrond).
- **Spoorlijn en vervoerder per been** niet gebrond, behalve HBRY voor The Pas–Thompson [6]; CN voor de rest is aannemelijk (ex-Canadian Northern [8][9]).
- **Winnipeg-knoop** is een toetspunt in het Symington-terrein (Wikipedia-coördinaat van de yard ligt 1,5 km oostelijker [7]), geen gebrond keerpunt.
- **Copper Cliff als bestemming** is afgeleid: Vale noemt "Sudbury integrated operations", geen smelter bij naam. Vale's Port Colborne raffineert volgens het ontwerp geen concentraat.
- **Geen gepubliceerde spoorlengte**: alle km zijn OSM-graaf; `toets_knikken.py` op het gebakken json is nog niet gedraaid.
- **Sitelaag**: Thompson ontbreekt in `nikkel-sitelaag.json`; centraal toe te voegen met 7,9 kt Ni (Vale 20-F FY2023).

## 8 · Bronnen
[1] Vale Base Metals, Thompson Operations — in productie sinds 1961, 10–15% van Canada, concentraat per spoor naar Ontario en Newfoundland. https://valebasemetals.com/our-operations/thompson/
[2] Vale S.A., Form 20-F FY2023 — Thompson: concentraat kan per truck/trein naar Winnipeg, direct per trein naar Sudbury of Trois-Rivières; tabel finished nickel per erts: Thompson 7,9 / 9,9 / 5,9 kt (2023/22/21). https://www.sec.gov/Archives/edgar/data/917851/000129281424001463/valeform20f_2023.htm
[3] Vale S.A., Form 20-F FY2017 — smelter en raffinaderij Thompson uitgefaseerd 2018, concentraat naar Sudbury en Long Harbour. https://www.sec.gov/Archives/edgar/data/0000917851/000104746918002777/a2234766z20-f.htm
[4] Vale S.A., Form 20-F FY2022 — sinds H2 2018 naar Sudbury en/of Long Harbour, afhankelijk van de vraag. https://www.sec.gov/Archives/edgar/data/917851/000129281423001516/valeform20f_2022.htm
[5] Wikipedia, "Thompson, Manitoba" — Inco-stad sinds 1956/57; Vale > 100 mln in de concentraat-load-out. https://en.wikipedia.org/wiki/Thompson,_Manitoba
[6] Wikipedia, "Hudson Bay Railway (1997)" — OmniTRAX-shortline ten noorden van The Pas, Thompson-tak, vervoert ertsen en concentraten. https://en.wikipedia.org/wiki/Hudson_Bay_Railway_(1997)
[7] Wikipedia, "Symington Yard" — CN's grootste rangeerterrein, Winnipeg (49.8654, -97.0283). https://en.wikipedia.org/wiki/Symington_Yard
[8] Wikipedia, "Foleyet" — Canadian Northern-lijn Winnipeg–Capreol, voltooid 1915. https://en.wikipedia.org/wiki/Foleyet
[9] Wikipedia, "Hornepayne" — Canadian Northern-lijn, 49.2167, -84.7833. https://en.wikipedia.org/wiki/Hornepayne
[10] Wikipedia, "Capreol" — divisiepunt van de spoorlijn, 46.7058, -80.9214. https://en.wikipedia.org/wiki/Capreol
[11] Wikipedia, "Thompson station (Manitoba)" — station ~1 km van het centrum bij het industriepark. https://en.wikipedia.org/wiki/Thompson_station_(Manitoba)
[12] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-nikkel-thompson-sudbury-thompson-emplacement.png` (z15), `…-thompson-industrie.png`, `…-winnipeg-wye.png` (z14), `…-coppercliff.png` (z15).
[13] Routebrief `pgm-sudbury-actonuk` §3 — anker Copper Cliff (46.47860, -81.05473, bron-gelegd). `v2/design/routebrieven/pgm-sudbury-actonuk.md`
[14] OSM 1-op-1-spoornet (`v2/build-cache/raw1op1/canada.geojson`) via `toets_spoorroute.mjs`, zes runs 2026-10-09.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Recept:** `bash v2/tools/bak_stromen.sh nikkel-thompson-sudbury` (functie `bak_nikkel_thompson_sudbury`); uitvoer `v2/data/stroomroute-nikkel-thompson-sudbury.json` (95,6 KB, contract versie 2, lonlat, 6 benen, 5.057 punten, 7 markers). De zes spoorruns stonden al op schijf (`spoorroute-nikkel-thompson-sudbury-*.geojson`, `BAKE_SUFFIX=-raw`, 1-op-1-net) en zijn ongewijzigd hergebruikt; geen zee, geen stippel, geen aanloop, geen lucht, geen leiding, geen kopie van een andere stroom.

| # | modaliteit | been | km gebakken | brief (OSM-graaf) | afw. | naad |
|---|---|---|---|---|---|---|
| 1 | spoor | Thompson-emplacement → The Pas (HBRY) | 369,7 | 369,6 | +0,0% | — |
| 2 | spoor | The Pas → Winnipeg Symington | 795,6 | 791,8 | +0,5% | 0,00 |
| 3 | spoor | Winnipeg → Hornepayne | 1.016,4 | 1.015,2 | +0,1% | 0,00 |
| 4 | spoor | Hornepayne → Foleyet | 237,5 | 236,9 | +0,3% | 0,00 |
| 5 | spoor | Foleyet → Capreol | 238,9 | 238,7 | +0,1% | 0,00 |
| 6 | spoor | Capreol → Copper Cliff-complex | 38,2 | 37,5 | +1,9% | 0,00 |
Totaal **2.696,3 km** (brief 2.689,7; het verschil is de gebakken lengte over de volledige polyline tegen de routeKm van de router). De ±15%-toets is hier een indicatie (geen gepubliceerde spoorkm) en wijkt nergens meer dan 2% af omdat de brief zelf uit dezelfde graaf komt.
**Markers (7):** de twee ankers uit §3 plus de vijf via-punten (The Pas, Symington, Hornepayne, Foleyet, Capreol). Afstand marker–lijn 0,00–0,27 km (alle ≤ 0,5 km). De Hornepayne-marker staat op het lijnpunt 49.2205,-84.7758 (0,69 km van het stadspunt uit §4) zodat hij de lijn raakt; het via-punt zelf bleef 49.2167,-84.7833.
**Toets:** `toets_knikken.py`: 0 knikken, 0 omkeringen, 0 terugloop; `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de lijst; geen naad > 0,00 km; modaliteit alleen `spoor`; elk been ≥ 130 punten.
**Lessen:** (1) een lange doorlopende spoorketen met een via-punt per corridorkeuze (rangeerterrein Symington, knoop Hornepayne) geeft schone naden en geen omkeringen; zonder die twee via-punten koos de vrije run een omkering bij Winnipeg en een omweg via Chapleau. (2) Een via-punt dat 0,69 km snapt (Hornepayne) levert een marker-lijnafstand op: zet de marker op het lijnpunt, niet in de stad. (3) Vervoerder en lijnnaam per been blijven aannemelijk (één bron, CN-ex-Canadian Northern); de beennaam zegt dat.
**Open voor centraal:** Thompson aan `nikkel-sitelaag.json` toevoegen (55.7407,-97.8300, 7,9 kt Ni/j); registreren in `stromen-register.json` (sleutel `ni-ts`).
