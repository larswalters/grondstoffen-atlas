# Routebrief (licht) · Kolen · Benga → Sena-lijn → Beira (Mozambique)

**stroom-id:** `kolen-benga-beira` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** cokes- en thermische kolen van de Benga-mijn (ICVL, Moatize-bekken, Tete) gaan per **spoor** over de Sena-lijn (Moatize, Dona Ana, Sena, Dondo) naar de kolenstapel/terminal in de haven van Beira (Sofala). Geen zeebeen: geen bron noemt een koper of bestemmingshaven op ladingniveau, dus de brief stopt bij de kade.
**Welke as van het verhaal:** de tweede Mozambikaanse kolencorridor, de Sena-lijn naar Beira naast Moatize→Nacala. Benga 0,67 Mt ROM in 2025 (1,24 Mt in 2023) [1]; Beira Coal Terminal 2,38 Mt export in 2024, capaciteit 6 Mt [2]. Eenheid: Mt kolen per jaar.

## 1 · Ketenkaart
```
Benga-mijn `kolen-benga-mijn` (ICVL, Moatize-bekken)
  ──(b1 spoor · last mile zonder net · 6,1 km hemelsbreed, STIPPEL)──►
Moatize-tak `kolen-benga-moataketak` (aansluiting op het spoornet, ~3,6 km W van Moatize-station)
  ──(b2 spoor · Sena-lijn via Moatize, Dona Ana, Sena, Inhaminga-streek, Dondo · 577,5 km gemeten, 590–673 gepubliceerd)──►
Beira-kolenterminal `kolen-beira-terminal` (kolenstapel + band naar de kade, haven van Beira) ── STOPPUNT
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-benga-mijn` → `kolen-benga-moataketak` | last mile (geen net op deze korrel): Benga-aansluiting staat niet in OSM, dichtstbijzijnde spoor 6,1 km | 6,1 hemelsbreed (router-snap 6,14) | stippel | **ja**, 6,1 km, hier reikt het net niet |
| b2 | A | spoor | `kolen-benga-moataketak` → `kolen-beira-terminal` | Sena-lijn: Moatize (route 0,2 km langs station), Dona Ana, Sena (3,3 km), Dondo (0,5 km), Beira | 577,5 gemeten · 590 [3], 600 [4], 660 [5], 673 [6] gepubliceerd (bandbreedte; -2% tot -14%) | toets_spoorroute (`BAKE_SUFFIX=-raw`), één run, geen via-punt | nee |

Fase B (zee) vervalt: geen bron voor een koper of haven op ladingniveau [5]. Geen aparte last mile in de haven: de kolenstapel ligt 0,5 km van het lithium-anker `li-beira-kade` en het spoor snapt op 0,05 km.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-benga-mijn` | mijn / laadplek | Benga-mijn (ICVL, Tete) | -16.1674, 33.6610 | [1][sat] | bron-gelegd (z15 gezien: mijncomplex met gebouwen en opslagterrein tussen twee open pits, haulwegen rondom; GEM geeft de coördinaat als "exact") |
| `kolen-benga-moataketak` | aansluitpunt op het net (geen overslag) | Spoor Moatize-tak, bij de kolen-CHPP W van Moatize | -16.1227, 33.6946 | [sat] | bron-gelegd (z15 gezien: spoor langs een zwarte kolenstapel, route snapt op 0,09 km) |
| `kolen-beira-terminal` | losplek / stoppunt | Beira-kolenterminal, kolenstapel van 800 m met band naar de kade | -19.8118, 34.8385 | [2][sat] | **aannemelijk** (z15 + z16 gezien: zwarte stapel van ~800 m oost-west, band naar de westelijke kade met schepen, spoor van oost; naam "Beira Coal Terminal" niet op de kaart geverifieerd) |

Hergebruik: `li-beira-kade` (-19.8150, 34.8340, Cornelder, uit `lithium-bikita-zhangjiagang.md`) ligt 0,5 km zuidwestelijk en is hier niet gebruikt; `kolen-moatize-mijn` (-16.1537, 33.7207, `kolen-moatize-nacala.md`) is een andere mijn 5 km verderop en wordt NIET hergebruikt.

## 4 · Via-punten
Geen. b2 is één router-run zonder corridorkeuze: de Sena-lijn is de enige spoorlijn Moatize→Beira en de run geeft 0 bochten ≥60 graden. De stations (Moatize, Dona Ana, Sena, Dondo) worden alleen als toets genoemd, niet als via-punt.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Benga-CHPP (kolenwasserij) | ICVL | ROM → cokes- en thermische kolen | ROM 0,67 Mt (2025) | [1][8] |
| Beira-kolenterminal | CFM-haven van Beira | trein → stapel → schip | 6 Mt/j; 2,38 Mt export 2024 | [2][5] |

## 6 · Stoppunt
De brief stopt op de kolenstapel in de haven van Beira: dat is het einde van de Sena-lijn en de exportterminal. Eigenaar ICVL (65% Indiase staatsbedrijven, 35% Tata Steel) leverde in 2014 60% aan India [5], maar geen bron noemt een haven of schip op ladingniveau. Fase D en E vervallen.

## 7 · Open punten
- **Kade/terminal niet bij naam gevonden.** OSM kent de Beira Coal Terminal niet (Nominatim leeg); het anker is een satelliet-gelegde kolenstapel, status aannemelijk. Naam en exacte ligplaats zijn niet geverifieerd.
- **Benga-Beira-koppeling steunt op één bron.** Alleen GEM (via het ketenontwerp, GEM-pagina's geven 403) en Mining Technology [8] koppelen Benga aan Beira; Wikipedia bevestigt alleen de Sena-lijn Moatize-Beira [3][4]. Een 2017-handelsbericht (zoekresultaat, niet geopend) meldt dat ICVL voor cokeskolen Macuse overweegt in plaats van Beira.
- **Kilometers.** Gemeten 577,5 tegen een bandbreedte 590–673 (-2% tot -14%): binnen de ±15%-norm, aan de onderkant bij de langste opgave.
- **Benga-last-mile 6,1 km is hemelsbreed, geen wegkm of spoorkm** (stippel, circa 1% van de keten); de werkelijke aansluiting op het net is niet gevonden.
- **Volume.** 0,67 Mt ROM (2025) en 2,38 Mt (Beira 2024) komen uit GEM via het ketenontwerp en zijn niet zelf herbevraagd; Benga-aandeel in de Beira-export is niet gepubliceerd. Onderbrekingen door overstromingen en de Sena-lijn die in 2014 even stillag na een aanval op een kolentrein [9].

## 8 · Bronnen
[1] Global Energy Monitor, Global Coal Mine Tracker, Benga (coördinaat exact; 0,67 Mt ROM 2025, 1,24 Mt 2023), via het ketenontwerp, niet zelf geopend (403). https://www.gem.wiki/Benga_coal_mine
[2] Global Energy Monitor, Global Coal Terminals Tracker, Beira coal terminal (2,38 Mt export 2024, capaciteit 6 Mt), via het ketenontwerp. https://www.gem.wiki/Beira_coal_terminal
[3] Wikipedia, "Sena railway": 1.067 mm, Dondo naar Mchinji/Chipata, Dona Ana-Moatize-tak 254 km, Moatize-tak voor het Benga-Moatize-kolenbekken. https://en.wikipedia.org/wiki/Sena_railway
[4] Dry Cargo Magazine, "Beira begins shipping coal" (2011-10-01): eerste Moatize-exportkolen via Beira, lijn van circa 600 km. https://www.drycargomag.com/beira-begins-shipping-coal
[5] Biznews, "India group to nearly triple coal output from mine bought from Rio Tinto" (2014-08-01): ICVL 65% / Tata Steel 35%, 5 Mt/j, 60% naar India, Beira capaciteit 6 Mt, spoorcapaciteit circa 6,5 Mt. https://www.biznews.com/africa/india-group-nearly-triple-coal-output-mine-bought-rio-tinto
[6] Freight News, "Delays on Mozambique's Sena line" (2011-08-05): Sena-lijn 673 km. https://www.freightnews.co.za/article/delays-on-mozambiques-sena-line
[7] Wikipedia, "Port of Beira": haven onder CFM, de Sena-lijn eindigt in de haven; 19,817 S 34,833 E. https://en.wikipedia.org/wiki/Port_of_Beira
[8] Mining Technology, "Benga Coal Mine, Mozambique": kolen via de haven van Beira geexporteerd, 1,62 Mt in 2013. https://www.mining-technology.com/projects/benga-coal-mine-mozambique/
[9] Wikipedia, "Benga coal mine": ICVL kocht in juli 2014 het belang van Rio Tinto. https://en.wikipedia.org/wiki/Benga_coal_mine
[sat] Esri World Imagery via `v2/tools/sat_check.py` (z15/z16, 2026-10-30), `v2/build-cache/satcheck/sat-kolen-benga-beira-benga.png` · `…-moataketak.png` · `…-kolenterminal.png` · `…-kolenterminal-z16.png`.
[osm] Nominatim: "Beira Coal Terminal" geen treffer; Cornelder -19,8221/34,8358 (niet gebruikt).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
**Bestand:** `v2/data/stroomroute-kolen-benga-beira.json` (19,0 KB, contract versie 2, lonlat) · **585,3 km, 997 punten, 2 markers** · registersleutel `kolen-bbe` (kolen-bb is bezet).
| been | modaliteit | km | punten | stippel |
|---|---|---|---|---|
| b1 last mile Benga-laadpunt -> Moatize-tak | spoor | 6,1 | 2 | ja (hier reikt het net niet) |
| b2 Sena-lijn Moatize-tak -> Beira-kolenterminal | spoor | 579,2 | 995 | nee, doorgetrokken |

**Recept:** (1) `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs "--van=-16.1227,33.6946" "--naar=-19.8118,34.8385" "--naam=kolen-benga-beira-moatize-beira" --max-snap=60` (zwaar-slot; 577,5 km, 995 punten, snaps 0,09 / 0,05 km, geen via-punt); (2) `bash v2/tools/bak_stromen.sh kolen-benga-beira` (functie `bak_kolen_benga_beira`; `--stippel` b1, `--been-geojson` b2, 2 markers). Geen extract-download (mozambique al in raw1op1), geen zee, haven-aanloop, kopie, lucht, leiding of weg-profiel.

**Toets:** b2 579,2 km tegen 590-673 gepubliceerd (-1,8% tot -14%; binnen de bandbreedte, aan de onderkant); naad b1 -> b2 0,09 km; marker Benga 0,0 km, marker Beira 0,05 km van de lijn; `toets_knikken` 0 knikken, 0 omkeringen; `toets_rechte_benen --min-km 5` meldt alleen de stippel van 6,1 km (bewust, eigen verbinding zonder net).

**Stippel b1:** Benga-aansluiting staat niet in OSM; dichtstbijzijnde spoor ligt 6,1 km hemelsbreed (geen spoorkm). Het ketenverhaal verandert er niet door: de lijn begint bij de mijn.
**Stoppunt:** kolenstapel Beira, status aannemelijk (naam Beira Coal Terminal niet geverifieerd).
**Lessen:** (1) de functie stond al in `bak_stromen.sh` uit de ontwerpfase; bakken was een run, geen herschrijven. (2) De losse `bash -n`-fout die een parallel bakken even toonde (regel in andermans functie) was een tussentijdse edit van een andere agent; een tweede `bash -n` was schoon.
