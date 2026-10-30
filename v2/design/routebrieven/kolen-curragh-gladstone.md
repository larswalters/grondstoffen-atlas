# Routebrief (licht) · Kolen · Curragh → Blackwater-systeem → RG Tanna, Gladstone (Australië)

**stroom-id:** `kolen-curragh-gladstone` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Keten in één zin:** cokeskool (en deels thermisch) van de Curragh-mijn (Coronado) bij Blackwater, Queensland, per **spoor** ~300 km over het
Aurizon-Blackwater-systeem (Blackwater → Duaringa → Rocklands/Gracemere → Raglan → Mount Larcom) naar de RG Tanna Coal Terminal in de haven van
Gladstone. Stoppunt = de RG Tanna-kolenopslag: de bron noemt Asië als markt, geen bestemmingshaven of koper per lading, dus **geen zeebeen**.
**Welke as van het verhaal:** *Bowen/Blackwater-cokeskool naar de zeekolenmarkt* — Curragh 10,6 Mt saleable in 2025 (10-K FY2025), waarvan 6,9 Mt cokeskool
verkocht op de zeemarkt (67% van het verkochte volume); thermisch vooral naar Stanwell [3]. Treincontract naar RG Tanna 9,5 Mtpa (8,5 Aurizon + 1,0
Pacific National), naar WICET 2,0 Mtpa [3]. Eenheid Mt kolen per jaar; peiljaar 2025 (kalenderjaar). GEM-ROM 2025: 11,9 Mt [2].

## 1 · Ketenkaart
```
Curragh-mijn, CHPP + laadlus `kolen-curragh-laad`
   ──(b1 spoor · Curragh-lus → Blackwater → Bluff → Duaringa → Rocklands (Gracemere) → Stanwell-zijde → Raglan → Mount Larcom → Callemondah · 304,3 km gemeten, ~300 gepubliceerd)──►
RG Tanna kolenopslag, Gladstone `kolen-rgtanna-terminal` ⏹ stoppunt (kades/shiploaders niet getekend, geen bestemming)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Curragh-laadlus → RG Tanna-kolenopslag | Blackwater-systeem (Aurizon, 1067 mm, 25 kV) naar Callemondah | 304,3 gemeten; gepubliceerd ~300 (+1,4%) [1][2][3] | maak_spoorbeen_raw.py (extract australie, §7) | nee; mijnkop 161 m, terminalstaart 357 m aan het net |

Geen zeebeen, geen haven-aanloop, geen vlucht, geen leiding: geen bron noemt een bestemming voor deze kolen en de kade van RG Tanna ligt aan het eind van het spoor.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-curragh-laad` | mijn / laadplek | Curragh: CHPP, kolenopslag en treinlaadlus | -23.4932, 148.8427 | GEM [2] (-23.493219, 148.842723), [1] | bron-gelegd (z15 gezien: kolenstapels en wasserij met transportbanden, spoorlus ~0,7 km westelijk; kruis op de laadstapel naast de lus) |
| `kolen-rgtanna-terminal` | overslag spoor→zee / losplek | RG Tanna Coal Terminal, kolenopslag | -23.8225, 151.2330 | [3] noemt RGTCT; coördinaat uit de haalbaarheidstoets | bron-gelegd (z15 gezien: kruis midden op de stockyard met de spoorontvangstlijn; twee berths met laadschepen bij de pier ten oosten; een ander terminal met lange pier (vermoedelijk WICET) ~1,5 km westelijk) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Punten liggen op de OSM-spoorlijn (snap 2 tot 6 m), niet in een stadscentrum; zonder via-punten kiest de router dezelfde lijn (304,3 km).
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Blackwater (goederenemplacement, oostzijde) | -23.5859, 148.8996 | pint het Blackwater-systeem naar het oosten, niet noordwaarts naar Gregory/Goonyella-aansluiting [6] |
| b1 | 2 | Duaringa-lijn | -23.7153, 149.6356 | doorgaande lijn naar de kust (Bluff 149,07 ligt ervoor, Duaringa-dorp 3 km verder) [7] |
| b1 | 3 | Rocklands / Gracemere | -23.4416, 150.4741 | knoop met de North Coast Line: hier gaat het systeem zuidwaarts naar Gladstone (Stanwell -23,484, 150,329 ligt voor dit punt) [7] |
| b1 | 4 | Raglan | -23.7158, 150.8175 | pint de NCL-lijn Raglan–Gladstone [7] |
| b1 | 5 | Mount Larcom | -23.8133, 150.9867 | laatste plaats vóór Callemondah/RG Tanna op dezelfde lijn |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Curragh CHPP + laadlus | Coronado Global Resources (100%, sinds 2017) | ROM → cokeskool + thermisch, treinlading | 10,6 Mt saleable 2025; Mammoth-ondergrond sinds dec 2024 | [1][2][3] |
| RG Tanna Coal Terminal | Gladstone Ports Corporation | trein → stockyard → shiploader | 3 bottom-dump stations, 22 stockpiles, 4 berths, 3 shiploaders (zonder bron in [5]); Curragh-contract 9,5 Mtpa | [3][5] |

## 6 · Stoppunt
De brief stopt op de kolenopslag van RG Tanna: de 10-K noemt Aziatische afnemers (Japan, Korea, India) en FOB-verkoop zonder schip of bestemmingshaven per lading [3],
en het ontwerp had een Gwangyang-been zonder bron (geschrapt).

## 7 · Open punten
- **Terminalverdeling:** Curragh gebruikt RG Tanna én WICET (2,0 Mtpa, take-or-pay) [3]; WICET (vermoedelijk het terminal westelijk op de satelliet) is niet getekend, alleen RG Tanna.
- **Aandeel per terminal en volume naar de haven:** 6,9 Mt export is de totale cokeskool, niet per terminal; geen RG Tanna-doorvoer per mijn gevonden.
- **Thermisch naar Stanwell:** deel van de lading gaat per spoor naar Stanwell Power Station (Rocklands-zijde, -23,51, 150,32), niet naar Gladstone; geen eigen been.
- **Geometrie via `maak_spoorbeen_raw`, niet `toets_spoorroute`:** het mijnuiteinde snapt in het gesnoeide net 11 km ernaast (haalbaarheidstoets); de raw-route snapt op 161 m.
- **Jaarcijfers verschillen:** GEM-ROM 11,9 Mt [2] (2025) tegen Wikipedia 7 tot 8,5 Mt (verouderd, capaciteit 2012) [1]; de 10,6 Mt komt uit een filingsamenvatting [3].
- **Gepubliceerde ~300 km** is een ronde opgave (10-K, GEM, Wikipedia), geen operatorlengte; de ±15%-toets is een indicatie.

## 8 · Bronnen
[1] Wikipedia, Curragh coal mine: 30 km NNW van Blackwater, Coronado, cokeskool, Blackwater-systeem en Port of Gladstone, Mammoth dec 2024. https://en.wikipedia.org/wiki/Curragh_coal_mine
[2] Global Energy Monitor, Curragh mine: -23.493219, 148.842723; ROM 2025 11,9 Mt; ~300 km rail naar Port of Gladstone; Stanwell. https://www.gem.wiki/Curragh_mine
[3] Coronado Global Resources, 10-K FY2025 (StockTitan-weergave): 10,6 Mt saleable, 6,9 Mt cokeskool zeemarkt, RGTCT + WICET, 300 km rail, Aurizon 8,5 + Pacific National 1,0 naar RGTCT, 2,0 naar WICET, Stanwell, Azië. https://www.stocktitan.net/sec-filings/CODQL/10-k-coronado-global-resources-inc-files-annual-report-7c1386c56730.html
[4] Coronado 10-Q (2026), Curragh 4,7 Mt H1 2026 en 3,0 Mt Q2 2026: context volume (geen 2025-jaarcijfer). https://last10k.com/sec-filings/codql/0001562762-26-000094.htm
[5] Wikipedia, Port of Gladstone: RG Tanna Coal Terminal (1997), Blackwater en Moura aanvoer, export naar Japan/Korea/India/China. https://en.wikipedia.org/wiki/Port_of_Gladstone
[6] Wikipedia, Blackwater railway system: Aurizon, termini Callemondah en Gregory, RG Tanna en WICET, Stanwell, 1067 mm, 25 kV. https://en.wikipedia.org/wiki/Blackwater_railway_system
[7] Wikipedia API (coordinaten): Blackwater -23.5758/148.8869, Bluff -23.5797/149.0705, Stanwell -23.4836/150.3286, Gracemere -23.4391/150.4558, Raglan -23.7161/150.8188. https://en.wikipedia.org/w/api.php
[8] OpenStreetMap (ODbL) via `v2/build-cache/raw1op1/australie.geojson`, router `v2/tools/maak_spoorbeen_raw.py`. https://www.openstreetmap.org
[9] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-kolen-curragh-gladstone-mijn.png`, `-rgtanna.png`.
[10] Mining Technology, Curragh mine (zoekresultaat): 14 km NW van Blackwater, cokeskool 300 km naar Gladstone, Stanwell. https://www.mining-technology.com/projects/curragh-mine/

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)

**Stroom `kolen-curragh-gladstone`** → `v2/data/stroomroute-kolen-curragh-gladstone.json` (61,4 KB) — 1 been, 304,3 km, 2.856 punten, 2 markers.
Recept: `bak_stromen.sh` (functie `bak_kolen_curragh_gladstone`), spoorbeen uit `v2/build-cache/ais/graaf/spoorroute-kolen-curragh-gladstone-curragh-gladstone.geojson` (maak_spoorbeen_raw.py, extract australie, 5 via-punten uit §4).

| been | modaliteit | km gemeten | gepubliceerd | afwijking | stippel |
|---|---|---|---|---|---|
| b1 | spoor | 304,3 | ~300 (ronde opgave) | +1,4% | nee |

Markers: `kolen-curragh-laad` op 0,16 km van de lijn, `kolen-rgtanna-terminal` op 0,36 km. Geen naden (één been). `toets_knikken`: 0 knikken, 0 omkeringen. Titel: Kolen · Curragh → RG Tanna (Gladstone, Australië).

Toelichting: geen stippel, haven-aanloop, vlucht, leiding of kopie; geen zeebeen omdat geen bron een bestemming of schip noemt (stoppunt §6). De ~300 km is een ronde opgave, dus de ±15%-toets is een indicatie.

Gereedschapslessen: (a) `toets_spoorroute` snapt het mijnuiteinde in het gesnoeide net 11 km ernaast; `maak_spoorbeen_raw.py` op het 1-op-1-net snapt op 161 m, dus voor een mijnkop eerst de raw-router. (b) Een tweede agent bewerkte `bak_stromen.sh` tijdens de bake-run: bash gaf daarna een syntaxfout op een verschoven regel nadat het json al geschreven was; controleer met `bash -n` en het json, de fout is geen bakfout.

