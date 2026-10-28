# Routebrief (licht) · gas — Port of Morgan (Montana) → Northern Border → Manhattan (Illinois)

**stroom-id:** `gas-portofmorgan-manhattan` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) ·
**status:** gebakken
**Keten in één zin:** pijpgas dat bij Port of Morgan (grens Montana/Saskatchewan) de Northern Border Pipeline
(42 inch, TC Energy/ONEOK) op gaat, loopt over ca. 1.870 km door Montana, North Dakota, South Dakota, Minnesota, Iowa
en Illinois naar de aansluitingen bij Manhattan (Chicago-regio). Alleen leiding; geen zee, geen haven-aanloop.
**Welke as van het verhaal:** *Canadees en Bakken-gas naar het Midwesten.* De titel "Canadees pijpgas" is niet eerlijk
(toets): de Canadese aanvoer bij Port of Morgan krimpt, het lijnnet neemt ook Williston/Bakken-gas op. Jaarvolume:
**Port of Morgan-import 4,6 bcm/j in 2025** (161,1 bcf; 2022: 261,5 bcf = 7,4 bcm; −38%) [4]; doorzet van de hele
leiding 23,9 bcm/j in 2004 (845 bcf, 2.377 mmcfd, 88% Canada) [2]; ontwerpcapaciteit 2,4 bcf/d ≈ 24,8 bcm/j [2].
**⚠️ Eindpunt:** het id belooft Manhattan; de lijn eindigt bij het OSM-eind 41.4446, -87.9916 (aannemelijk, niet gezien).

## 1 · Ketenkaart
```
Port of Morgan (grens MT/SK, gasstation) `gas-portofmorgan-kop`
  ──(b1 leiding · Northern Border, 23 OSM-ways · 1.487,7 km)──► Iowa 41.8525, -92.4312
  ──(b2 leiding, stippel · OSM-gat Iowa · 127,6 km hemelsbreed)──► 41.6163, -90.9266
  ──(b3 leiding · Chicago Project, OSM-way 1025655071 · 152,5 km)──► 41.4672, -89.1659
  ──(b4 leiding, stippel · OSM-gat Illinois · 47,4 km hemelsbreed)──► 41.4738, -88.5966
  ──(b5 leiding · Northern Border Mainline, 2 OSM-ways · 56,0 km)──► Manhattan IL `gas-manhattan-eind` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-portofmorgan-kop` → Iowa 41.8525,-92.4312 | Northern Border Pipeline, 42 inch, OSM-ways 468644651 … 468922520 (23 ways, naden max 2,8 km) | 1.487,7 gemeten; tot Ventura IA 1.317 tegen 822 mijl = 1.323 gepubliceerd [2] (−0,5%) | maak_leidingbeen_gas_portofmorgan_manhattan.py → `--been-geojson` | nee |
| b2 | A | leiding | Iowa 41.8525,-92.4312 → 41.6163,-90.9266 | Northern Border (Ventura–Harper, 2 leidingen), niet gekarteerd | hemelsbreed 127,6, geen wegkm | `--stippel "leiding\|…"` | ja — OSM-gat |
| b3 | A | leiding | 41.6163,-90.9266 → 41.4672,-89.1659 | Northern Border, Chicago Project, OSM-way 1025655071 | 152,5 gemeten | idem | nee |
| b4 | A | leiding | 41.4672,-89.1659 → 41.4738,-88.5966 | Northern Border Mainline, niet gekarteerd | hemelsbreed 47,4, geen wegkm | `--stippel "leiding\|…"` | ja — OSM-gat |
| b5 | A | leiding | 41.4738,-88.5966 → `gas-manhattan-eind` | Northern Border Mainline, OSM-ways 1432429480 + 1432558933 | 56,0 gemeten | `--been-geojson` | nee |

**Toets (§5-norm):** totaal gemeten 1.696,2 km doorgetrokken + 175,0 km stippel = **1.871 km** tegen **1.214 mijl = 1.954 km**
Port of Morgan → Manhattan (822 + 147 + 245 mijl, 10-K FY2004 [2]) = **−4,3%** (binnen ±15%; de stippelstukken zijn
hemelsbreed en dus iets korter dan de echte leiding). De 1.412 mijl (2.272 km) van TC Energy [3] is het hele systeem
incl. de 35 mijl naar North Hayden (Indiana) en aanvullende stukken, niet vergelijkbaar. Stippel = 9% van de lengte.
Fase A (Canadese aanvoer Foothills/Empress, Bakken-aftakkingen) wordt niet getekend.

## 3 · Ankers
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-portofmorgan-kop` | kop leiding (grens + gasstation) | Northern Border-begin, Port of Morgan MT | 49.0036, -107.5433 | [1][2][5] | aannemelijk (z15 gezien: omheind gasstation met leidingstroken op akkerland, ca. 0,4 km ten noorden van de grensweg bij 49.000; de station-identiteit komt alleen uit het OSM-wayeinde en niet uit een bron, het kan de Canadese zijde zijn) |
| `gas-manhattan-eind` | eindpunt leiding (aansluitingen ANR en Peoples Gas) | Northern Border Mainline-eind bij Manhattan IL | 41.4446, -87.9916 | [2][5] | aannemelijk (z15 gezien: akkerrand ten noordoosten van Manhattan, geen zichtbaar station of leidingstrook; de 10-K noemt de aansluitingen ANR en Peoples Gas "near Manhattan" [2] zonder coördinaat) |

## 4 · Via-punten
Niet van toepassing: leidingbenen volgen OSM-ways, de twee gaten zijn rechte stippels.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Northern Border Pipeline | TC Energy 50% / ONEOK 50% | Canada (88%), Williston (8%), Dakota Gasification (4%) in 2004 → Midwesten | 2.374 mmcfd tot Ventura IA (≈ 24,5 bcm/j); 16 compressorstations; 2004 doorzet 23,9 bcm | [2][3] |
| Aansluitingen Manhattan IL | ANR Pipeline, Peoples Gas Light & Coke | pijpgas → distributie Chicago | niet gebrond | [2] |

## 6 · Stoppunt
De brief stopt bij Manhattan (Illinois): de 10-K noemt daar de overdracht aan ANR en Peoples Gas (Chicago-distributie), en geen bron volgt het gas verder (fase D/E vervallen).

## 7 · Open punten
- **Canadees pijpgas is geen eerlijke titel.** EIA Port of Morgan: 239,5 / 258,4 / 261,5 / 158,6 / 154,5 / 161,1 bcf voor 2020-2025 [4]; het aandeel Canada daalde van ca. 48% (2018) naar 24% (2020) door Bakken-aanvoer [7]; 2025 niet gebrond. Bison XPress (+0,3 bcf/d Bakken) komt volledig in dienst in 2026 [8]. Het jaarvolume 4,6 bcm is dus alleen de Canadese invoer, niet de doorzet van de leiding.
- **Doorzet na 2004 niet gebrond** (23,9 bcm/j is 2004); de ontwerpcapaciteit is 2,4 à 2,5 bcf/d.
- **Twee OSM-gaten (175 km, 9%)** zijn stippel. De leiding bestaat er wel; in het Iowa-gat liggen losse OSM-stukjes (ways 468924416 en 468924414, 41.8065..41.7904) die 4-5 km ten zuiden van de rechte stippel lopen en niet zijn meegenomen. De stippel is schematisch.
- **Kop is een grenspunt**, niet de Canadese aanvoer (Foothills/Monchy–Empress niet getekend); eind Manhattan niet op satelliet bevestigd.
- **Niet getekend:** het stuk Manhattan → North Hayden (Indiana, 35 mijl), de Ventura-Harper-lussen (tweede leiding, 30 en 36 inch) en het Alliance-systeem (Sherwood ND, 496,8 bcf in 2025), dat een eigen leiding is en niet in dit ontwerp zit.
- **Overlap:** geen met bestaande stromen; Keystone-olie (olie-hardisty-cushing) is een andere leiding door dezelfde staten.

## 8 · Bronnen
[1] Wikipedia, "Northern Border Pipeline" (stub, geen cijfers). https://en.wikipedia.org/wiki/Northern_Border_Pipeline
[2] Northern Border Pipeline Co., Form 10-K FY2004 (SEC; 1.249 mijl: 822 mijl 42 inch tot Ventura IA, Ventura-Harper 147 mijl, Harper-Manhattan 245 mijl, 16 compressorstations, doorzet 2004, aansluitingen ANR/Peoples near Manhattan). https://www.sec.gov/Archives/edgar/data/0001095355/000095012905002313/h23122e10vk.txt
[3] TC Energy, "Northern Border Pipeline" (1.412 mijl / 2.272 km, 50% TC Energy, 50% ONEOK). https://tcenergy.com/operations/natural-gas/northern-border-pipeline
[4] EIA, "U.S. Natural Gas Pipeline Imports by Point of Entry" (Port of Morgan MT 2020-2025, MMcf). https://www.eia.gov/dnav/ng/NG_MOVE_POE1_A_EPG0_IRP_MMCF_A.htm
[5] OpenStreetMap-bijdragers (ODbL) via Overpass (way(id:…); out geom), geraadpleegd 2026-10-28: man_made=pipeline "Northern Border Pipeline" / "Northern Border Mainline"; 34 ways in de corridor, 29 gebruikt. https://overpass-api.de
[6] Esri World Imagery via `v2/tools/sat_check.py` (z15, live, 2026-10-28): `v2/build-cache/satcheck/sat-gas-portofmorgan-manhattan-{portofmorgan,manhattan}.png`.
[7] IHS Markit / S&P Global, samenvatting Northern Border (Canadees aandeel 48% in 2018, 24% in 2020; 2,5 bcf/d). https://prod.azure.ihsmarkit.com/commodityinsights/en/ci/research-analysis/northern-border-pipeline-gas-ethane.html
[8] PGJ Online, april 2026, "Bakken gas capacity set to rise as Bison XPress nears full service" (300.000 Dth/d). https://pgjonline.com/news/2026/april/bakken-gas-capacity-set-to-rise-as-bison-xpress-nears-full-service
[9] S&P Global Platts, jan 2021, "Strong gas production drives Bakken shale flows on Northern Border to new highs" (ca. 2 bcf/d Bakken). https://www.spglobal.com/energy/en/news-research/latest-news/natural-gas/010421-strong-gas-production-drives-bakken-shale-flows-on-northern-border-to-new-highs

## 9 · Bak-noot
### Gebakken (2026-10-28, lichte werkwijze, M31 golf 10)
**Bestand:** `v2/data/stroomroute-gas-portofmorgan-manhattan.json` (43,0 KB, versie 2, lonlat) · **5 benen, 1.871,2 km, 2.008 punten, 2 markers**.
**Recept:** `bash v2/tools/bak_stromen.sh gas-portofmorgan-manhattan` (functie `bak_gas_portofmorgan_manhattan`); leidinggeojsons uit `python v2/tools/maak_leidingbeen_gas_portofmorgan_manhattan.py` (OSM-ways, FeatureCollection) in `v2/build-cache/ais/graaf/gas-portofmorgan-manhattan-leiding-nb1/2/3.geojson`.

| # | modaliteit | km gebakken | brief | punten | opmerking |
|---|---|---|---|---|---|
| b1 | leiding | 1.487,7 | 1.487,7 | 1.670 | doorgetrokken, 23 OSM-ways |
| b2 | leiding, stippel | 127,6 | 127,6 hemelsbreed | 2 | OSM-gat Iowa |
| b3 | leiding | 152,5 | 152,5 | 228 | doorgetrokken, OSM-way 1025655071 |
| b4 | leiding, stippel | 47,4 | 47,4 hemelsbreed | 2 | OSM-gat Illinois |
| b5 | leiding | 56,0 | 56,0 | 106 | doorgetrokken, 2 OSM-ways |

**Toets:** totaal 1.871,2 km tegen 1.954 km (1.214 mijl, 10-K) = -4,2%, binnen +-15% (indicatie: stippels zijn hemelsbreed). Naden 6, 3, 5 en 4 m (max 0,006 km). Markers: kop 2 m, eind 5 m van de lijn. `toets_rechte_benen --min-km 5` meldt alleen de twee stippels (127,6 en 47,4 km) als groot stippelbeen: bedoeld (OSM-gat, de leiding bestaat). `toets_knikken`: 24 knikken, 2 omkeringen, 0 terugloop; ze zitten in OSM-pijpleidinggeometrie (Illinois: trapvormig langs wegenraster, bocht 90 gr op 41.45,-88.19 tot -88.31; kop: 5 m-haarspeld bij 48.9991,-107.5431 op het wayeinde). Geen herstel nodig: het is bron-geometrie en geen route-artefact.
**Stippels met reden:** b2 en b4 = "hier reikt het net niet" (OSM heeft de leiding in dat stuk niet; losse OSM-stukjes in Iowa, ways 468924416 en 468924414, liggen 4-5 km zuidelijker en zijn niet gebruikt). Geen haven-aanloop, geen vlucht, geen wegprofiel, geen letterlijke kopie.
**Lessen:** een leidinggeojson moet een FeatureCollection zijn; het stroom-id noemt Manhattan en de lijn eindigt daar (41.4446,-87.9916, aannemelijk, niet gezien). Titel blijft "Gas, Port of Morgan -> Northern Border -> Manhattan": de Canadese aanvoer is maar een deel van het gas (zie §7).
