# Routebrief (licht) · koper — Red Chris → Stewart (Canada)

**stroom-id:** `koper-redchris-stewart` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Titel:** Koper · Red Chris → Highway 37/37A → Stewart Bulk Terminals (Canada)
**Keten in één zin:** Red Chris-concentraat (Newmont/Imperial Metals, Golden Triangle, BC) gaat per **truck** over de Mine Access Road, Highway 37 (Cassiar) en Highway 37A naar het ijsvrije **Stewart** en wordt daar bij de bulkterminal op de kade in zeeschepen voor Aziatische smelters geladen [2][3][4]. De keten stopt op de kade: geen zeebeen, geen benoemde afnemer.
**Welke as van het verhaal:** Noordwest-BC-concentraat naar een Pacifische exporthaven. Volume: **ca 6 kt Cu per jaar** (Newmont, peil Q2 2026, dalend: stockpile-verwerking tijdens een stripping-campagne) [1]; de terminal verwerkt **ca 260 kt Cu- en Au-concentraat per jaar** incl. Red Chris en Brucejack, ruwweg half de capaciteit [3]. Eerste lading 27-02-2015 [2].

## 1 · Ketenkaart
```
Red Chris-concentrator ──(b1 truck · Mine Access Road → Hwy 37 zuid → Meziadin Jct → Hwy 37A west → Dyke Road · hemelsbreed 202 km, geen wegkm)──► Stewart Bulk Terminals, kade ca 2 km ZW van het dorp
  (stop: concentraat gaat per bulkschip naar smelters in Azie [4]; geen bron noemt een haven of smelter, dus geen zeebeen)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Red Chris-concentrator → Stewart Bulk Terminals | Red Chris Mine Access Road (23 km toegangsweg naar Hwy 37 [8]) → BC 37 Cassiar Hwy zuid → Meziadin Junction → BC 37A (65 km [5]) → Dyke Road | **hemelsbreed 202 km, geen wegkm** (indicatie OSRM/OSM 315,6 km = 18,4 mijnweg + 233,5 Hwy 37 + 59,3 Hwy 37A + 2,8 Dyke Road [9]; de ±15%-toets is hier een indicatie) | maak_stroombeen_weg (extracts canada) | nee |
Zee: geen been. Haven-aanloop: nvt (geen zeebeen).

## 3 · Ankers (één per site en per overslag; lat, lon)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-redchris-laad` | mijn / concentrator (kop) | Red Chris, molenhal met concentraatopslag | 57.7297, -129.7650 | OSM "Red Chris Plant" 57.7208,-129.7783 [9]; Newmont [1]; mineralsed.ca [4] | bron-gelegd (z15 gezien: grote lichte molenhal met kleine hallen, transportband uit de dagbouwput en toegangsweg naar het noorden; het OSM-punt ligt 1,3 km ZW op de band/haulroad aan de putrand, het ontwerppunt is dus naar de molen verschoven) |
| `cu-stewart-kade` | overslag truck → zee | Stewart Bulk Terminals / Stewart World Port, kade en loods oostoever | 55.9180, -129.9955 | Wikipedia Stewart: World Port-wharf 2 km ZW van het dorp, terminal 260 kt/j [3]; mining-technology [2]; mineralsed.ca [4] | aannemelijk (z15 gezien: L-vormige pier met lange lichte opslagloods en verharde apron aan de oostoever, 2,0 km ZZW van het dorp, aangesloten op Dyke Road; dat de terminal van Red Chris op precies deze pier ligt is niet met een bedrijfsbron bevestigd, wel past de ligging bij de 2 km-opgave) |

## 4 · Via-punten (alleen landbeen b1; alle punten uit de OSM-wegas via OSRM, op de doorgaande weg)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Mine Access Road x BC 37 (Tatogga) | 57.7094, -129.9949 | pint de afslag zuidwaarts naar Stewart in plaats van noordwaarts via Iskut naar Dease Lake [9] |
| b1 | 2 | BC 37 bij Bob Quinn Lake | 56.9731, -130.2501 | houdt de lange Hwy 37-etappe op de Cassiar Hwy (233 km zonder alternatief, tussenanker tegen een omweg) [5][9] |
| b1 | 3 | Meziadin Junction | 56.1007, -129.3073 | de keuze BC 37 (naar Kitwanga) tegen BC 37A (naar Stewart) [5][6] |
| b1 | 4 | BC 37A, Bear Pass | 56.1062, -129.6695 | houdt de route op BC 37A door het lawinepas-traject; geen andere weg naar Stewart [5] |
| b1 | 5 | BC 37A x Dyke Road | 55.9483, -129.9794 | pint Dyke Road zuidwaarts langs de dijk naar de kade, niet het dorpsraster of de Hyder-weg [9] |
Refs voor het profiel: 37, 37A; extracts: canada; `eindToegangPrivaat: True` (terminalweg/mijnweg privaat), vensterKm 40-75.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Red Chris-concentrator | Newmont (70%) / Imperial Metals (30%) | erts (dagbouw, 10-11 Mt/j) → Cu-Au-concentraat; opslag in bunkers tot het trucken [2][4] | **ca 6 kt Cu/j (Q2 2026)**, 9 koz Au | [1][4] |
| Stewart Bulk Terminals (overslag, geen verwerking) | tot 2025 aparte exploitant; sinds aug 2025 aangekondigde koop door Nisga-a Nation, Tahltan Nation Development LP en Arrow Transportation | truck → bulkschip | ca 260 kt concentraat/j (incl. Brucejack), ca 50% van de capaciteit | [3] |

## 6 · Stoppunt
De brief stopt op de kade van Stewart: de bronnen noemen alleen "smelters overzee/in Azie" [2][4] en geen haven of fabriek, dus er is geen gedocumenteerde volgende locatie en een zeebeen zou een verzonnen bestemming zijn.

## 7 · Open punten
- Wegkm van het geheel niet gepubliceerd (alleen Hwy 37A 65,11 km en Meziadin-Dease Lake ca 333 km [5][6]); de bake-uitvoer (verwacht ca 300-320 km) is een indicatie, geen toets.
- Of "Stewart Bulk Terminals" en de Stewart World Port-pier één en dezelfde installatie zijn is niet expliciet bevestigd; de kade staat daarom op aannemelijk.
- De Newmont-pagina noemt Stewart niet [1]; de route komt uit mining-technology, mineralsed.ca en Wikipedia [2][3][4]. Een 2026-artikel van Mining News North noemt Stewart en Hwy 37A voor "o.a. Red Chris", maar was niet opvraagbaar (alleen zoekresultaat-snippet).
- Volume klein en dalend (6 kt Cu/j); geen concentraattonnage per jaar voor Red Chris apart gevonden.
- Fase D/E: geen afnemer of smelter met naam gevonden.

## 8 · Bronnen
[1] Newmont — Red Chris (6 kt Cu/j en 9 koz Au per Q2 2026, productie daalt door stripping, 70%/30% JV met Imperial Metals) https://operations.newmont.com/canada/red-chris-canada
[2] Mining-technology — Red Chris copper-gold mine (eerste lading naar Stewart Bulk Terminals 27-02-2015, eerste verscheping 11-04-2015; concentraat naar opslag en scheepsbelading Port of Stewart) https://www.mining-technology.com/projects/red-chris-copper-gold-mine-british-columbia/
[3] Wikipedia — Stewart, British Columbia (Stewart Bulk Terminals ca 260 kt Cu/Au-concentraat/j incl. Red Chris en Brucejack; Stewart World Port wharf 2 km ten zuiden van het dorp; Hwy 37A; koop aug 2025) https://en.wikipedia.org/wiki/Stewart,_British_Columbia
[4] Mineralsed.ca — Red Chris Mine (80 km ten zuiden van Dease Lake, 18 km ZO van Iskut; concentraat per truck naar Port of Stewart, bulkcarriers bij Stewart Bulk Terminals, smelters in Azie) https://mineralsed.ca/learning-resources/bc-mineral-resources-map/bc-operating-mine-profiles/red-chris-mine/
[5] Wikipedia — British Columbia Highway 37A (65 km, Meziadin Junction km 65,11 tot Stewart/Hyder) https://en.wikipedia.org/wiki/British_Columbia_Highway_37A
[6] Wikipedia — British Columbia Highway 37 (874,76 km; Kitwanga-Meziadin ca 156 km; Meziadin-Dease Lake ca 333 km) https://en.wikipedia.org/wiki/British_Columbia_Highway_37
[7] Zoekresultaat WebSearch 2026-10-31 (Red Chris: 80 km zuid van Dease Lake; eerste trucklading naar Port of Stewart 27-02-2015; 2026-artikel Mining News North over Stewart-gateway via Hwy 37A, niet opengehaald) https://www.miningnewsnorth.com/story/2026/09/11/news/indigenous-partners-open-stewart-gateway/9865.html
[8] Zoekresultaat WebSearch 2026-10-31 (23-km toegangsweg naar Hwy 37 in de ontwikkelplannen; brontitel in het resultaat niet vermeld, dus indicatie; de OSM-meting geeft 18,4 km vanaf de molen)
[9] OpenStreetMap via OSRM-demo (route molen naar kade 315,6 km, stappen: Mine Access Road 18,4, Cassiar Hwy BC 37 233,5, BC 37A 59,3, Dyke Road 2,8) en Nominatim (Meziadin Junction 56.0999,-129.3044; Iskut 57.8389,-129.9875; Tatogga 57.7151,-129.9872; Red Chris Mine Access Road) https://router.project-osrm.org en https://nominatim.openstreetmap.org
[10] Satellietbeelden Esri World Imagery z14-z15, v2/build-cache/satcheck/sat-koper-redchris-stewart-plant2.png, -kade.png, -kade-ruim.png

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Bestand:** `v2/data/stroomroute-koper-redchris-stewart.json` (versie 2, lonlat, 42,2 KB, 1 been, 1.943 punten, 2 markers). **Functie:** `bak_koper_redchris_stewart` in `v2/tools/bak_stromen.sh`; **profiel:** `koper-redchris-stewart-redchris-stewart` in `v2/tools/maak_stroombeen_weg.py`.

| # | modaliteit | been | km | naad | stippel |
|---|---|---|---|---|---|
| b1 | truck | vrachtwagen Red Chris-concentrator → Stewart Bulk Terminals (Mine Access Road → BC 37 → Meziadin Jct → BC 37A → Dyke Road) | **314,8** | n.v.t. (enig been) | nee, doorgetrokken |

Totaal 314,8 km. Markers: `cu-redchris-laad` (57.7297, -129.7650, bron-gelegd) en `cu-stewart-kade` (55.9180, -129.9955, aannemelijk), beide op 0,00 km van de lijn.

**Km-toets.** De brief geeft geen wegkm (hemelsbreed 202 km); OSRM-indicatie 315,6 km. Gebakken 314,6 km (wegtool) / 314,8 km (json) = -0,3 tot -0,4% tegen de indicatie; dat is een indicatie, geen norm. Deelstukken van het wegtool: mijnweg 18,3 km (brief OSRM 18,4), tot Bob Quinn Lake 93,5, tot Meziadin 139,5, BC 37A tot Bear Pass 25,1, tot Dyke Road 34,3, naar de kade 4,0. BC 37A totaal (Meziadin tot Dyke Road) 59,4 km tegen 65 km Wikipedia tot Hyder; het lijnstuk eindigt voor Stewart-dorp en is dus korter, geen fout.

**Recept.** Eén nieuwe wegscan (`wegscan_puur.py`, extract canada, 410 s): refs 37 en 37A, vensterKm 75, `eindToegangPrivaat`, 5 via-punten uit §4, alle snap 0,00 km. Geen zeebeen, geen haven-aanloop, geen stippel, geen kopie, geen lucht: geen bron noemt haven of smelter, de lijn stopt waar het bewijs stopt (de kade).

**Lessen / afwijkingen.**
- Eerste scan gaf "geen wegpad tussen punt 0 en 1": de 18 km Mine Access Road is OSM `unclassified` en ligt grotendeels buiten de 12-km-eindzone. Oplossing: `corridorKlassen: ["unclassified"]` in het profiel (patroon pgm-lacdesiles). Geen via-punt verplaatst of bijgeschoven.
- `toets_knikken.py` meldt 7 knikken, geen terugloop: de scherpe bocht van 152 graden (R 16 m) bij de kade is de afslag op de pier (echt); de spikes van 70 tot 98 graden (R 20 tot 100 m) liggen bij de ankers (plant-aansluiting 0,10 km, kade 0,03 km) en op de via-punten (Tatogga, Dyke Road), dus aansluitingen en kruispunten op de doorgaande weg, geen omweg.
- Kade-anker blijft aannemelijk (niet bedrijfsbevestigd dat Stewart Bulk Terminals en de World Port-pier één installatie zijn); de Newmont-pagina noemt Stewart niet.
- Geen naden (één been). `toets_rechte_benen` geeft geen melding op dit been.

