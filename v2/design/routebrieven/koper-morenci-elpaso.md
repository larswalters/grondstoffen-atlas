# Routebrief (licht) · koper — Morenci → Miami-smelter → El Paso (Verenigde Staten)

**stroom-id:** `koper-morenci-elpaso` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** koperconcentraat van de Morenci-concentrator (Freeport-McMoRan, Greenlee County AZ) gaat per
trein over de Clifton Subdivision naar Lordsburg NM en via Bowie en Safford naar de eigen Miami-smelter; de anodes
rijden per spoor (boxcars) terug via Lordsburg en Deming naar de El Paso-raffinaderij. Volledig spoor, geen zee.
**Welke as van het verhaal:** de volledig binnenlandse FCX-keten van het VS-Zuidwesten (mijn → smelter → raffinaderij en
walsdraad). Miami-smelter 2024: 840,6 kt concentraat, 214 kt Cu anode [6]; 2023: 810,9 kt en 222 kt [1]. El Paso-kathode
217,8 kt Cu in 2023, capaciteit ~410 kt [1]. Morenci-aandeel in het concentraat niet gepubliceerd (Morenci is grotendeels SX-EW).

## 1 · Ketenkaart
Morenci-concentrator ──(b1 spoor · Clifton Sub, AZER · 126,2 km)──► Lordsburg ──(b2 spoor · UP Lordsburg-Bowie + AZER
Bowie-Safford-Globe · 293,6 km)──► Miami-smelter ──(b3 spoor · anodes in boxcars · 560,3 km)──► El Paso-raffinaderij ⏹

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `cu-morenci-laad` → Lordsburg (via-punt) | Clifton Subdivision (Arizona Eastern): Clifton, Duncan, Lordsburg [2][4] | 126,2 route (router 125,5); hemelsbreed 96 km, geen gepubliceerde spoorkm | toets_spoorroute | nee |
| b2 | A | spoor | Lordsburg → `cu-miami-smelter` | UP-trackagerechten Lordsburg-Bowie, dan AZER Bowie-Safford-Globe-Miami [2][3] | 293,6 route (router 290,3); AZER Miami-Bowie 133,8 mijl = 215,3 km [2], route 217 km op dat deel (+1%); hemelsbreed 227 km | toets_spoorroute | nee |
| b3 | C | spoor | `cu-miami-smelter` → `cu-elpaso-raffinaderij` | AZER Miami-Globe-Safford-Bowie, UP Sunset Route Lordsburg-Deming-El Paso [2][3] | 560,3 route (router 555,0); hemelsbreed 457 km, geen gepubliceerde spoorkm | toets_spoorroute | nee |

Totaal 980,1 km (gebakken geometrie). b3 herhaalt ~299 km van b2 (Lordsburg-Bowie-Miami: de anodes rijden terug); dat is echt en geen duplicaat
van een andere stroom. Corridor is Clifton-Lordsburg-Bowie-Globe, niet Clifton-Safford (geen spoor Clifton-Safford).

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-morenci-laad` | mijn / concentrator | Morenci-concentrator, spoorkop bij de verdikkertanks | 33.0680, -109.3430 | [1] (Morenci 33.07/-109.35, "railway spur"), [4]; sitelaag `w-morenci` 33.0906,-109.3667 ligt in de put | bron-gelegd (z15 gezien: wit hallencomplex van de concentrator met vier ronde verdikkertanks ten zuiden en terreinspoor; rail-snap 0,09 km) |
| `cu-miami-smelter` | smelter | Miami-smelter (FCX), Miami AZ | 33.4128, -110.8562 | [5]; sitelaag `w-miami-smelter`, hergebruikt letterlijk | bron-gelegd (z15 gezien: smelterterrein met hoge installaties en emplacementssporen, tailingsvijver NO, stad ten zuiden; rail-snap 0,14 km) |
| `cu-elpaso-raffinaderij` | raffinaderij | El Paso-raffinaderij en rod mill (FCX), Rod Mill Road | 31.7645, -106.3922 | [1], OSM Rod Mill Road (0,35 km ernaast) | bron-gelegd (z15 gezien: lange witgedekte tankhuis-hal met bezinkbekkens, tankpark NW, spoorbundel ZO; rail-snap 0,06 km) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1/b2 | 1 | Lordsburg, UP/AZER-aansluiting (spoor, niet in het stadscentrum) | 32.3401, -108.7922 | pint de Clifton Sub naar Lordsburg (b1 eindigt, b2 begint): zonder dit punt zoekt een vrije Dijkstra een Safford-omweg die niet bestaat |
| b3 | — | geen | — | de router volgt zelf Globe, Safford, Bowie, Lordsburg, Deming (toets: elk binnen 1,3 km van de lijn); één corridor |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Morenci-concentrator | Freeport-McMoRan 72%, Sumitomo, anderen | erts → concentraat (plus SX-EW-kathode, niet getekend) | Morenci 100% ≈ 318 kt Cu in 2024 | [1][6] |
| Miami-smelter | Freeport-McMoRan | concentraat → anode (zwavelzuur voor SX-EW) | 810,9 kt concentraat, 222 kt anode (2023) | [1][3] |
| El Paso-raffinaderij + rod mill | Freeport-McMoRan | anode → kathode (+ draad) | 217,8 kt kathode (2023), cap ~410 kt | [1] |

## 6 · Stoppunt
De keten stopt bij de El Paso-raffinaderij: bron [1] noemt rod mills in El Paso en Miami zonder aparte adres- of
coördinaatopgave en geen afnemer van kathode of draad, dus fase D vervalt en E ook.

## 7 · Open punten
- Het Morenci-aandeel in het Miami-concentraat is niet gepubliceerd: [1] zegt "a significant portion" van Morenci, Bagdad,
  Sierrita en Chino; fcx.com noemt Morenci wel bij naam voor treinconcentraat [3]. Overige toeleveranciers (Sierrita, Bagdad, Chino) zijn niet getekend.
- Spoorkm zijn eigen Dijkstra over het 1-op-1-net, geen gepubliceerde routekm; enige maatstaf is AZER Miami-Bowie (215,3 km tegen 217).
- OSM mist de wye bij Bowie: beide benen buigen 176 graden om bij 32.3355,-109.5167 (uitstulping ~3,3 km), blijft staan, voor §9.
  Verder omkeringen bij Clifton 33.0524,-109.2955 (170 graden), Miami-emplacement 33.4120,-110.8663 en het El Paso-raffinaderijspoor
  (31.7304,-106.3618 en 31.7622,-106.3855): procesgaten, niet dichtgetrokken.
- Rod mill El Paso: locatie niet apart gelegd (zelfde terrein aangenomen, niet gezien); geen kathode-/draadafnemer gevonden.
- Rangeerdienst Morenci (FMI Industrial Railroad of Morenci Southern) en ruil bij Clifton komt uit de haalbaarheidstoets, niet uit eigen bron.
- Sitelaag: `w-morenci` (33.0906,-109.3667) ligt in de put, 3,3 km van het spoor; centraal gelijktrekken naar 33.0680,-109.3430 (niet door mij gewijzigd).

## 8 · Bronnen
[1] Freeport-McMoRan, Form 10-K FY2023 (Miami-smelter, El Paso, Morenci-coördinaat, railway spur) — https://www.sec.gov/Archives/edgar/data/831259/000083125924000011/fcx-20231231.htm
[2] Wikipedia, "Arizona Eastern Railway" (Miami-Bowie 133,8 mijl; Clifton Sub naar Lordsburg; trackagerechten Lordsburg-Bowie) — https://en.wikipedia.org/wiki/Arizona_Eastern_Railway
[3] FCX, "Freeport features" (concentraat per trein naar Miami; anode per spoor in boxcars naar El Paso) — https://fcx.com/freeport-features/112823
[4] Wikipedia, "Morenci mine" (spoor voor zwavelzuur en concentraat) — https://en.wikipedia.org/wiki/Morenci_mine
[5] Wikipedia, "Miami, Arizona" (smelter en rod plant) — https://en.wikipedia.org/wiki/Miami,_Arizona
[6] `v2/design/koper-sitelaag.json`, `w-morenci`, `w-miami-smelter` (FCX 10-K 2024: 840,6 kt concentraat, 214 kt anode)
[7] Eigen runs `toets_spoorroute.mjs` (BAKE_SUFFIX=-raw, 3.260.717 spoor-edges), 2026-10-09: `spoorroute-koper-morenci-elpaso-*.geojson`
[8] Satellietblikken Esri z15: `v2/build-cache/satcheck/sat-koper-morenci-elpaso-{morenci,miami,elpaso}.png`

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Recept:** `bash v2/tools/bak_stromen.sh koper-morenci-elpaso` (functie `bak_koper_morenci_elpaso`, LF, 0 CRLF). Drie spoorruns met `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs` (1-op-1-net, `--hoofd-km=100`, prefix `spoorroute-koper-morenci-elpaso-`), daarna `hecht_marnet.py route` met drie `--been-geojson "spoor|..."`. Geen wegscan, geen profiel in `maak_stroombeen_weg.py`, geen zee, geen haven-aanloop, geen stippel, geen kopie, geen luchtbeen. Extracts us-arizona, us-new-mexico, us-texas. Uitvoer `v2/data/stroomroute-koper-morenci-elpaso.json`, 53,3 KB, versie 2, lonlat.

| # | modaliteit | km gebakken | punten | naad naar volgende | toets |
|---|---|---|---|---|---|
| b1 | spoor | 126,2 | 448 | 0,000 km | hemelsbreed 96 km, geen gepubliceerde spoorkm; router 125,5 |
| b2 | spoor | 293,6 | 942 | 0,000 km | AZER Miami-Bowie 215,3 km tegen 217 km op dat deel (+1%); router 290,3 |
| b3 | spoor | 560,3 | 1.318 | — | hemelsbreed 457 km, geen gepubliceerde spoorkm; router 555,0 |

Totaal 980,1 km · 2.708 punten · 3 markers (Morenci 0,10 km, Miami 0,11 km, El Paso 0,06 km van de lijn). Geen naad > 0 m.
Via-punt Lordsburg (32.3401, -108.7922) ligt op de lijn: b1 eindigt en b2 begint daar.

- **Spoorkm:** alleen de AZER-maatstaf (215,3 tegen 217 km) is een gepubliceerd getal; de rest is eigen Dijkstra, dus de ±15%-toets is een indicatie. b3 ligt ~299 km op b2 (anodes rijden terug langs Lordsburg-Bowie-Miami), dat is echt.
- **toets_knikken:** 7 omkeringen, alle 7 terugloop: Clifton 33.0524,-109.2955 (170,6 gr, b1), Bowie 32.3355,-109.5167 (176,0 gr, b2 en b3, wye ontbreekt in OSM, uitstulping ~3,3 km), Miami-emplacement 33.4120,-110.8663 (173,3 gr, b2 en b3), El Paso-raffinaderijspoor 31.7304,-106.3618 (179,8 gr) en 31.7622,-106.3855 (177,4 gr). Procesgaten in OSM, niet dichtgetrokken. `toets_rechte_benen --min-km 5`: geen treffer voor deze stroom.
- **Sitelaag:** `w-morenci` (33.0906, -109.3667) ligt in de put, 3,3 km van het spoor; centraal gelijktrekken naar 33.0680, -109.3430 (niet door mij gewijzigd).
- **Register:** sleutel `cu-me` was vrij (ook `cu-mt`, `cu-sp`, `cu-ti`, `cu-ahe` bestaan).
- **Lessen:** (1) een via-punt op de UP/AZER-aansluiting bij Lordsburg is nodig om een niet-bestaande Safford-omweg van b1 te voorkomen. (2) Een volledig-spoor-keten heeft geen aanloop- of stippelwerk: de tijd zit in het controleren van omkeringen en markers. (3) De bake is deterministisch: een herbake gaf dezelfde benen, km en punten; alleen het tijdstempel verschilt.
