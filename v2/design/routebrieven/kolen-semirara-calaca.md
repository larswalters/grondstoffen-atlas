# Routebrief (licht) · kolen — Semirara (Molave-Narra) → Semirara Port → Calaca (Filipijnen)

**stroom-id:** `kolen-semirara-calaca` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** thermische steenkool uit de Molave-Narra-dagbouw (Semirara-eiland, Antique) per **kolenband** (OSM-gekarteerd, ~7 km)
naar Semirara Port, per **zeeschip** (~317 km: 251 km MARNET via Sibuyan-zee en Verde Island Passage + twee haven-aanlopen) naar de kolenpier
van de Sem-Calaca-centrale (Calaca, Batangas). Stoppunt = de kolenpier: stockyard en centrale liggen er direct achter (aannemelijk: één bron).
**Welke as van het verhaal:** *Filipijnse eilandmijn met eigen centrales.* SMPC verscheepte 16,5 Mt in 2024 (8,4 Mt export, waarvan 7,6 Mt China;
8,0 Mt binnenland, genoemd: cementfabrieken 1,3 Mt en de Calaca-centrales) [4][5]; saleable productie 16 Mt/j sinds 2022 [1]. Het deel dat naar Calaca gaat
is niet gepubliceerd; ruwe bovengrens ~6,7 Mt/j (8,0 − 1,3 cement, afgeleid, niet gemeten).

## 1 · Ketenkaart
```
Molave-Narra-mijn `kolen-semirara-mijn` ──(b1 band · OSM-gekarteerd · 11,2 km, 2 korte stippels)──► Semirara-laadpier `kolen-semirara-pier`
   ──(b2 zee · Sibuyan-zee → Verde Island Passage · 317 km: 60,6 aanloop-stippel + 251,2 MARNET + 5,1 aanloop-stippel)──►
   Calaca-kolenpier `kolen-calaca-kade` ⏹ stoppunt (stockyard + Sem-Calaca 4 units 900 MW direct achter de pier, 0,6 km)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding (band) | `kolen-semirara-mijn` → `kolen-semirara-pier` | SMPC-kolenband, OSM `goods_conveyor`+`resource=coal` | gemeten 11,2 (2,3 + 7,1 + 0,5 + 1,3); hemelsbreed 6,9, geen gepubliceerde bandlengte | `--stippel` mijn→bandbegin · `--been-geojson` OSM-band (7,1 km, 45 punten, ways in §7) · 2× `--stippel` pier-trestle | ja: 2,3 km last mile (mijn 2,3 km van bandbegin) en 1,8 km pier-trestle (band niet gekarteerd); band doorgetrokken |
| b2 | B | zee | `kolen-semirara-pier` → `kolen-calaca-kade` | Tablas/Sibuyan → Verde Island Passage | MARNET 251,2 (zeeknoop 5888 → 5513); hemelsbreed pier→kade 216,7; geen gepubliceerde scheepsroute | MARNET + aanloop-stippels (zie §4) | ja: aanloop Semirara 4 stippels (60,6 km, pier ligt 47 km van zeeknoop 5888, het eiland ligt ertussen) en aanloop Calaca (5,1 km, kade 5,1 km van zeeknoop 5513) |

Fase C (kade → ketelhuis) vervalt: de OSM-polygoon "Calaca Power Plant" (`way/804751668`) grenst aan de stockyard, 0,6 km van de pierkop; geen eigen been.
Beennaam b2 voor de bol: *"zeeschip Semirara → Calaca (SMPC-eigen kool; levering aan Sem-Calaca aannemelijk: eigendom + 2024-persbericht, geen tonnage per lading)"*.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-semirara-mijn` | mijn | Molave-Narra-dagbouw (SMPC), Semirara | 12.1158, 121.3687 | [1] GEM "exact" | bron-gelegd (z14 gezien: uitgestrekte dagbouw met terrassen, haalwegen en spoilvlakten; punt ligt in het mijngebied) |
| `kolen-semirara-pier` | overslag laadpier (band → zee) | Semirara Port, laadpier met bulkcarriers | 12.0554, 121.3556 | [7] OSM `man_made=pier` way 237523737 (12.0552, 121.3528), [8] | bron-gelegd (z16/z17 gezien: ~1,5 km lange trestle de baai in, twee bulkcarriers langszij op lon 121.3535 en 121.3559; wolken over het land erachter; ontwerp zei aannemelijk) |
| `kolen-calaca-kade` | overslag kolenpier (zee → centrale) | Calaca-kolenpier Sem-Calaca, pierkop met schip | 13.9250, 120.7882 | [7] OSM pier way 419007341 (13.9248, 120.7883), [3] | bron-gelegd (z17 gezien: bulkcarrier aan de pier, band langs de pier naar twee kolenkoepels en stapels, centrale erachter) |

(Eerste Calaca-coördinaat in de ontwerp-JSON, 13.9238/120.7855, lag op z15 in open water 300 m westzuidwest van de pier; verschoven naar de pierkop.)

## 4 · Via-punten
Geen via-punten voor landbenen (b1 volgt OSM-ways, geen corridorkeuze). Waterpunten voor de aanloop Semirara, in reisvolgorde pier → zeeknoop 5888 (12.2239, 121.7537):
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b2 | 1 | open water NW van de pier | 12.0690, 121.3460 | z16 gezien: open zee ten noordwesten van de trestle; Ilugao-eiland ligt 1,2 km oost |
| b2 | 2 | west van de mijnkust | 12.1000, 121.3150 | z12/z13: open water, ruim 2 km van de westpunt van het mijngebied (spoilarm 121.34) |
| b2 | 3 | noord van het eiland | 12.1700, 121.3350 | z12/z13 open water; 1,4 km van Liwagao, 2,2 km van Nagubat; daarvandaan 45,9 km rechte stippel naar zeeknoop 5888 (OSM-eilanden 0 km gesneden) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Molave-Narra / Semirara Port | SMPC (DMCI Holdings) | dagbouwkool → band → pier → schip | 16 Mt/j saleable 2022-2024; 16,5 Mt verscheept 2024 | [1][4] |
| Sem-Calaca Power Corp (SCPC), 13.9326, 120.7897 | SMPC, 100% | steenkool → elektriciteit | units 300+300+150+150 = 900 MW; levering uit Semirara: aannemelijk (één bron: eigendom/persbericht) | [2][3][4][9] |

## 6 · Stoppunt
De brief stopt bij de kolenpier van Calaca: kolen wordt er in één stap tot elektriciteit verstookt (geen fase D/E) en de stockyard grenst direct aan de pier.

## 7 · Open punten
- **Levering aan Calaca is aannemelijk, niet bewezen met tonnage:** [4] noemt "Calaca power plants" als binnenlandse afnemer, [2] zegt dat SMPC op eigen brandstof draait; geen bron geeft het Calaca-aandeel.
- **Calaca-aandeel:** ruwe bovengrens ~6,7 Mt/j afgeleid (8,0 Mt binnenland − 1,3 Mt cement); ander binnenlands gebruik niet uitgesplitst. Het 2024-jaarverslag [10] gaf HTTP 403 en is niet gelezen.
- **Schip of bak (barge)?** Geen bron noemt het vaartuigtype Semirara → Calaca; de beennaam zegt "zeeschip" op grond van de bulkcarriers aan beide piers (z16/z17). SLPGC (ontwerp) staat niet in [3]; units 1-4 zijn SCPC.
- **Band op de pier niet gekarteerd:** OSM-band eindigt op 12.0540, 121.3724, de pier begint op 12.0559, 121.3678; pier-trestle is stippel (1,8 km). Begin van de band (12.1064, 121.3871) ligt 2,3 km van het GEM-mijnpunt; welke put voedt de band is niet vastgesteld.
- **Haven-aanloop-tool brak af (300 s) voor Semirara én Calaca:** rechte stippels dus. Semirara-eiland ontbreekt in Natural Earth: de landtoets is blind; waterpunten zijn alleen op satelliet nagekeken. De Calaca-stippel (5,1 km) snijdt in NE 0,24 km "land" (grove kustlijn).
- **OSM-band is gestikt met een eigen Dijkstra** (snap 12 m, springt op enkele plekken tussen twee parallelle bandstrengen): `v2/build-cache/ais/graaf/kolen-semirara-calaca-band-semirara.geojson` is mijn eigen bestand; ways 932321187/185/184/186/188/195/125/123/124/121/119/120/132/130/192/190/194/111/112.
- **Fabrieken van de SLTEC-centrale** (OSM `way/485761448`, 13.9218, 120.8283) liggen 4 km oost en zijn geen SMPC; niet getekend.

## 8 · Bronnen
[1] Global Energy Monitor, Molave-Narra coal mines — 12.1158/121.3687 exact; saleable 16 Mt 2022-2024; ~60% export / 40% binnenland 2021. https://www.gem.wiki/Molave-Narra_coal_mines
[2] Semirara Mining and Power Corporation, homepage — dochters SCPC en SLPGC, 2×300 MW, "runs on its own fuel". https://www.semiraramining.com/
[3] Global Energy Monitor, Calaca power station — 13.9326/120.7897, units 300+300+150+150 MW operating, SCPC 100% SMPC. https://www.gem.wiki/Calaca_power_station
[4] PortCalls, 2025 — 16,5 Mt verscheept 2024, export 8,4 Mt (China 7,6), binnenland 8,0 Mt incl. cement 1,3 Mt en Calaca-centrales; Semirara Coal Corp.-haven. https://portcalls.com/semirara-ships-record-16-5m-mt-of-coal-in-2024/
[5] ABS-CBN, 2025-01-14 — Semirara reports record shipments for 2024 (alleen zoekresultaat-snippet gelezen). https://abs-cbn.com/news/business/2025/1/14/semirara-reports-record-shipments-for-2024-1313
[6] Wikipedia (MediaWiki API, prop=coordinates) — "Semirara Island" 12.0563/121.3853 (niet als anker gebruikt); "Semirara Mining and Power Corporation": 92% nationale productie 2015, DMCI-dochter. https://en.wikipedia.org
[7] OpenStreetMap (ODbL), Geofabrik-extract `filipijnen`, eigen pyosmium-scan — pier ways 237523737, 932321090/91 (Semirara), 419007322/341 (Calaca); 30 `goods_conveyor` ways; `way/804751668` "Calaca Power Plant" (Sem-Calaca Power). https://download.geofabrik.de/asia/philippines.html
[8] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-kolen-semirara-calaca-{mijn,pier,pier-z17,kade,kade-z17,centrale,eiland,eiland-z12,westkust,water-noord}.png`.
[9] Power Philippines, SMPC koopt MGen uit St. Raphael Power Generation (units 5-6 Calaca, geschrapt); Calaca-centrale ex-NPC. https://powerphilippines.com/?p=8185
[10] Semirara Mining and Power, 2024 annual and sustainability report — HTTP 403, niet gelezen. https://www.sustainabilityreports.com/semirara-mining-and-power/2024/annual-and-sustainability-report
[11] MARNET-trial (`hecht_marnet.py route`, 2026-10-29): zeeknoop 5888 → 5513 = 251,2 km; naden 0.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)

Functie `bak_kolen_semirara_calaca()` in `v2/tools/bak_stromen.sh`; uitvoer `v2/data/stroomroute-kolen-semirara-calaca.json` (3,9 KB, contract versie 2, lonlat). Bake: `bash v2/tools/bak_stromen.sh kolen-semirara-calaca`.

**Benen (10 stuks, 328,1 km, naden max 0,01 km):**
| # | modaliteit | km | wat |
|---|---|---|---|
| 1 | leiding | 2,3 | stippel last mile mijn-anker naar bandbegin (geen net op deze korrel) |
| 2 | leiding | 7,1 | OSM-kolenband goed (goods_conveyor, 45 punten), doorgetrokken |
| 3-4 | leiding | 0,5 + 1,3 | stippels pier-trestle (band op de pier niet gekarteerd), samen 1,8 km |
| 5-8 | zee | 1,8 + 4,8 + 8,1 + 45,9 | stippels haven-aanloop Semirara langs drie waterpunten naar zeeknoop 5888 (60,6 km) |
| 9 | zee | 251,2 | MARNET zeeknoop 5888 naar 5513, doorgetrokken, aannemelijk in de beennaam |
| 10 | zee | 5,1 | stippel haven-aanloop Calaca (kade naar zeeknoop 5513) |

**Markers (3):** kolen-semirara-mijn (12.1158, 121.3687), kolen-semirara-pier (12.0554, 121.3556), kolen-calaca-kade (13.9250, 120.7882); alle drie op een beenuiteinde (afstand tot de lijn 0 km).

**Toets:** km MARNET 251,2 = brief; totaal 328,1 = trial in de briefronde. Geen gepubliceerde bandlengte, dus de +-15%-toets is niet van toepassing (gemeten 11,2 km tegen 6,9 hemelsbreed). Naden: nul, grootste 0,01 km. `toets_knikken`: 4 knikken, 0 omkeringen, 0 terugloop (3 spikes in de OSM-band waar de stik tussen twee parallelle strengen springt; 1 krappe bocht in de Verde Island Passage, R 5,3 km). `toets_rechte_benen --min-km 5`: de stippels 45,9 / 8,1 / 5,1 km staan er met reden (aanloop, geen net).

**Recept:** stippel leiding mijn naar bandbegin, been-geojson leiding band (`$BEEN/kolen-semirara-calaca-band-semirara.geojson`, FeatureCollection), 2 stippels leiding pier-trestle, 4 stippels zee pier naar waterpunten 1-3 naar zeeknoop 5888, been zee 5888 naar 5513, stippel zee naar de pierkop. Geen weg, spoor, lucht of gedeeld been; geen profiel in `maak_stroombeen_weg.py`.

**Toelichting stippels:** (a) last mile 2,3 km en pier-trestle 1,8 km: de OSM-band begint 2,3 km van het GEM-mijnpunt en eindigt 0,5 km voor de pier, de trestle is niet gekarteerd. (b) Aanloop Semirara 60,6 km: de pier ligt 47 km van zeeknoop 5888 met het eiland ertussen; `maak_havenaanloop.py` brak af (300 s), dus rechte stippels via drie op satelliet gecontroleerde waterpunten; Semirara ontbreekt in Natural Earth, de landtoets is daar blind. (c) Aanloop Calaca 5,1 km: kade 5,1 km van zeeknoop 5513, snijdt in NE 0,24 km "land" (grove kustlijn).

**Id en eindpunt:** het id belooft Calaca en de lijn eindigt op de Calaca-kolenpier: geen afwijking.

**Lessen:** (1) een band uit OSM stikt met een eigen Dijkstra; de spikes zijn de keuze tussen parallelle strengen, geen routefout. (2) Een eiland dat niet in Natural Earth staat vraagt waterpunten op satelliet voor de aanloop; zonder die punten steekt de stippel het eiland over. (3) De stroom is al in de briefronde getrialed met `hecht_marnet route`; de bake leverde bit-gelijke km (328,1).
