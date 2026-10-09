# Routebrief (licht) · koper — Toquepala → Ilo-smelter (Peru)

**stroom-id:** `koper-toquepala-ilo` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** koperconcentraat (±26,5% Cu) uit de Toquepala-concentrator (Southern Copper, Tacna) gaat per eigen SCC-industriespoor (1435 mm, bergspoor van ±3.000 m naar zeeniveau) naar de Ilo-smelter aan de kust (17 km ten noorden van de stad Ilo); de lijn stopt op het smelter-raffinaderijcomplex.
**Welke as van het verhaal:** *Zuid-Peru, eigen mijn-smelter-raffinaderij-spoor* — geen haven-trechter naar China maar een gesloten SCC-keten van mijn tot kathode. Jaarvolume: Toquepala 2024 = 225,2 kt Cu in concentraat (496.428 klb) + 24,1 kt Cu als SX-EW-kathode (kt Cu per jaar, SCC 10-K FY2024 [1]); Ilo smelt 1.230,9 kt concentraat (Toquepala + Cuajone) en maakt 359,4 kt anode en 287,9 kt kathode [1].

## 1 · Ketenkaart
```
Toquepala-concentrator `cu-toquepala-conc` ──(b1 spoor · SCC-industriespoor Toquepala–Ilo · router 187 km)──►
Ilo-smelter/raffinaderij `cu-ilo-smelter` ── stoppunt
```
(Cuajone-concentraat komt via de Cuajone-tak op dezelfde lijn; die tak wordt niet getekend. Kathode via de SCC-haven van Ilo: niet gebrond, niet getekend.)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Toquepala-concentrator → Ilo-smelter | SCC-industriespoor Ilo–Toquepala (1435 mm, enkelspoor, 27 km tunnels) | router 187,1; gepubliceerd 214 km voor de héle lijn incl. Cuajone-tak [1] (215 [2]) — indicatie, geen norm | toets_spoorroute (BAKE_SUFFIX=-raw, extract peru, --hoofd-km=100) | nee |

Been C (smelter → Ilo-haven) vervalt (bindend, haalbaarheidstoets): geen bron noemt de kade van de SCC-haven. Geen zeebeen, geen haven-aanloop.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-toquepala-conc` | laadplek (concentrator, kop b1) | Toquepala-concentrator I+II | -17.2726, -70.6242 | [1][3][4] | bron-gelegd (z15 gezien: verwerkingsfabriek met ronde indikkers, maalgebouwen, transportband en filter/laadgebouwen; het spoorhoofd ligt exact hier, snap 0,00 km) |
| `cu-ilo-smelter` | losplek (smelter + raffinaderij, staart b1) | Fundición de Ilo (SCC) | -17.5050, -71.3590 | [1][5] | aannemelijk (z15 gezien: kustcomplex met smeltgebouwen, tankpark en een 500 m-zuurpier; spoor loopt langs het complex, snap 0,08 km; het 10-K-punt -17.4987/-71.3601 ligt 0,8 km noordelijker op de smeltloodsen) |

De put zelf (-17.2456, -70.6136, sitelaag w-toquepala) is geen anker: 3,2 km van het net, het erts gaat intern per band naar de concentrator. Geen last-mile-been (zie §7).

## 4 · Via-punten
Geen. Het SCC-net is één enkelsporig boomnet (component 252 km, 214 km lijn + emplacementen); tussen kop en staart bestaat geen corridorkeuze (geen parallelle lijn, geen splitsing richting een andere bestemming). Een via-punt zou alleen een zijtak of emplacement kunnen aantrekken. Router: 4 bochten ≥ 60° (111/141/85/122 m straal) rond Toquepala passen bij een bergspoor met keerbochten (niet apart gecontroleerd), geen omkering >= 150 graden.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Toquepala-concentrator I+II | Southern Copper | erts → Cu-concentraat (±26,5% Cu, ≤ 8,5% vocht) per spoor | 120 kt erts/dag; 2024 111,7 kt/dag | [1] |
| Ilo-smelter | Southern Copper | concentraat → anode 99,7% + zwavelzuur (via zuurpier) | 1.376 kt concentraat/j nominaal; 2024 1.230,9 kt gesmolten | [1] |
| Ilo-raffinaderij (Pacocha, -17.5788, -71.3531) | Southern Copper | anode → kathode 99,998% + Ag/Au/Se | 294,8 kt/j nominaal; 2024 287,9 kt | [1] |

## 6 · Stoppunt
De brief stopt op het smelter-raffinaderijcomplex: het 10-K noemt een eigen haven in Ilo en spoorvervoer van producten, maar geen kade, geen schip en geen overzeese afnemer — fase D/E vervallen.

## 7 · Open punten
- **Haven-kade Ilo niet gevonden** (OSM kent alleen Muelle Fiscal en Patio Puerto; 10-K noemt de SCC-haven zonder locatie): been C niet getekend; of kathode per spoor naar de haven gaat is niet gebrond.
- **Gepubliceerde km voor alleen Toquepala–Ilo ontbreekt**: 214/215 km is de hele lijn incl. Cuajone-tak (10-K: spoor Toquepala–Cuajone met buisleiding ernaast, lengte niet genoemd). Router 187,1 + een tak van ±27 km komt op ≈ 214, maar die tak is een afleiding, geen bron. De ±15%-toets (−13% tegen 214) is een indicatie.
- **Het "121 km van Toquepala" uit het 10-K is een wegafstand**, geen spoor (spoor/hemelsbreed-verhouding 2,28).
- **Smelter-anker is het OSM-landuse-punt**, 0,8 km zuidelijker dan de 10-K-coördinaat; blijft aannemelijk.
- 2022: Cuajone-spoor geblokkeerd door protesten, daarna hersteld [1]; geen invloed op de tekening.
- Toquepala-SX-EW-kathode (24,1 kt) gaat niet per se per spoor; niet getekend.

## 8 · Bronnen
[1] Southern Copper Corp., Form 10-K FY2024 — industriespoor 214 km 1435 mm (257 km incl. emplacementen), Toquepala 496.428 klb en SX-EW 53.165 klb, concentraat per spoor naar Ilo, smelter 17 km N van Ilo (17°29,924'S 71°21,608'W), capaciteiten, raffinaderij, zuurpier. https://minedocs.com/28/Southern-Copper-Form-10-K-2024.pdf
[2] Railway Gazette, "Southern Peru" — 215 km, 1435 mm, Ilo–Toquepala–Cuajone, 14 locs / 490 wagons. https://railwaygazette.com/data/southern-peru/53346.article
[3] Wikipedia, "Toquepala mine" — coördinaat -17.2450/-70.6139, SCC, concentraat naar Ilo-smelter. https://en.wikipedia.org/wiki/Toquepala_mine
[4] Esri World Imagery via sat_check.py — `v2/build-cache/satcheck/sat-koper-toquepala-ilo-conc-z15.png`, `-conc.png`, `-railhead.png` (z14–z15).
[5] Esri World Imagery via sat_check.py — `v2/build-cache/satcheck/sat-koper-toquepala-ilo-smelter-z15.png`, `-smelter.png`, `-pacocha.png`, `-haven.png`.
[6] Southern Copper, "Know our history" — spoor en industriehaven Ilo in bedrijf sinds 1960; Toquepala 1960. https://southerncoppercorp.com/eng/know-our-history/
[7] Wikipedia, "Ilo, Peru" — stad -17.6459/-71.3453, smelter ±10 km van de stad. https://en.wikipedia.org/wiki/Ilo,_Peru
[8] `v2/design/koper-sitelaag.json` — w-toquepala (-17.2456, -70.6136), w-ilo (-17.505, -71.359; OSM landuse Fundición de Cobre de Ilo).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Recept:** `bash v2/tools/bak_stromen.sh koper-toquepala-ilo` (functie `bak_koper_toquepala_ilo`). Uitvoer `v2/data/stroomroute-koper-toquepala-ilo.json` (21,6 KB, contract versie 2, lonlat). Het spoorbeen is hergebruikt uit de al gedraaide `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs "--van=-17.2726,-70.6242" "--naar=-17.5050,-71.3590" "--naam=koper-toquepala-ilo-a" --hoofd-km=100 --max-snap=60` (`v2/build-cache/ais/graaf/spoorroute-koper-toquepala-ilo-a.geojson`, FeatureCollection). Geen wegprofiel, geen wegscan, geen haven-aanloop, geen stippel, geen luchtbeen, geen letterlijke kopie.

| # | modaliteit | km | punten | naad | opmerking |
|---|---|---|---|---|---|
| b1 | spoor (doorgetrokken) | 187,1 | 1.082 | n.v.t. | 59 edges, snap 0,00 km (kop) en 0,08 km (staart); hemelsbreed 82,1 km (omwegfactor 2,28, bergspoor) |

Totaal 187,1 km, 1 been, 2 markers (Toquepala-concentrator 0,00 km van de lijn; Ilo-smelter 0,08 km).

**Toets:** km-toets is alleen een indicatie: 187,1 tegen 214 km (hele lijn incl. Cuajone-tak, 10-K) is -12,6%; tegen 215 km (Railway Gazette) -13,0%; geen aparte Toquepala-Ilo-opgave, dus geen norm. Geen naden (een been). `toets_knikken.py`: 4 knikken van 61 tot 67 graden, boogstraal 72 tot 87 m, segmenten van 40 tot 150 m (geen 15 m-wisselspikes), 0 omkeringen, 0 terugloop: passen bij de keerbochten van een bergspoor rond Toquepala (lon -70,66 tot -70,73), niet verder gecontroleerd. `toets_rechte_benen.py`: geen rechte lijnen. json.load, versie 2, punt_formaat lonlat, modaliteit spoor, bestand 21,6 KB: in orde.

**Toelichting:** geen stippel, geen aanloop, geen vlucht, geen leiding. Het SCC-net is een enkelsporig boomnet; de router vindt zonder via-punten één pad. De smelter is aannemelijk (OSM-landuse-punt, 0,8 km zuidelijker dan het 10-K-punt); de lijn stopt op het smelter-raffinaderijcomplex, been C naar de Ilo-haven is niet getekend (kade niet gevonden, bindend uit de haalbaarheidstoets).

**Lessen:** (1) bij een eigen industriespoor met één component van 252 km volstaat `--hoofd-km=100`; de standaard 1.000 km zou naar een ander net springen. (2) Een gepubliceerde lijnlengte voor de hele lijn incl. zijtak is geen norm voor een deelroute; zet dat in de brief en toets op indicatie. (3) Het tussenresultaat van de spoorrouter was compleet (FeatureCollection, 1.082 punten) en is zonder herrun hergebruikt.

