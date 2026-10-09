# Routebrief (licht) · Grafiet · Epanko (Tanzania) → Dar es Salaam → Duisburg (Duitsland)

**stroom-id:** `grafiet-epanko-duisburg` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** vlokgrafietconcentraat van het EcoGraf-project Epanko (Duma TanzGraphite, Ulanga, Morogoro, Tanzania)
gaat per **truck** over Ifakara, Kidatu en Mikumi (T1) naar de kade van Dar es Salaam, per **zeeschip** (haven-aanloop + MARNET,
Suez of Kaap, router kiest) naar Rotterdam RHB en per **binnenvaart** de Rijn op naar Duisburg-Ruhrort Becken A (aannemelijk:
één bron voor de bestemming).
**Welke as van het verhaal:** de eerste Duitse offtake-as uit Oost-Afrika, naast `grafiet-molo-duisburg` (Madagaskar): 20 kt/j
oplopend naar 40 kt/j met een anonieme Duitse trader (FOB Dar es Salaam, 10 jaar, aug 2026) [2] plus een bestaand contract met
tk accelis Trading [6]. Volume: Stage 1 73 kt grafiet/j nameplate (Updated BFS feb 2026), potentieel 87,6 kt/j [1]; **actueel
0 kt/j, pre-FID, peiljaar 2026** — de weg is echt, de lading nog niet (zelfde precedent als Balama).

## 1 · Ketenkaart
```
Epanko-dorp `gr-epanko-dorp` ──(b1 truck · Mahenge-weg → Ifakara → Kidatu → Mikumi → T1 → Dar es Salaam ·
hemelsbreed 355 km, geen wegkm)──► Dar es Salaam-kade `gr-daressalaam-kade` (hergebruikt)
  ──(b2 zee · haven-aanloop, stippel, 19,84 km kade → zeeknoop, letterlijke kopie lindijumbo)──► zeeknoop 5310 (-6.6537, 39.3256)
  ──(b3 zee · MARNET, Suez of Kaap — router kiest · orde 12.000 km via Suez, niet gemeten)──► Rotterdam RHB `gr-rotterdam-rhb`
  ──(b4-b6 binnenvaart · Rijn, letterlijke kopie molo-duisburg b4-b6 · 235,0 km)──► Duisburg Becken A `gr-duisburg-beckena` ⏹
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-epanko-dorp` → `gr-daressalaam-kade` | Mahenge-weg → Ifakara → Kidatu → Mikumi → T1 (Morogoro, Chalinze) → Dar es Salaam | hemelsbreed 355 km, geen gepubliceerde wegkm; Epanko–Ifakara 75 km [5], gemeten 77,2; toets: 494,1 | maak_stroombeen_weg (nieuw profiel, extract `tanzania`) | nee |
| b2 | B | zee | `gr-daressalaam-kade` → zeeknoop 5310 | havenkanaal Dar es Salaam (kade 19,84 km van de zeeknoop) | 19,84 (kopie `grafiet-lindijumbo-qingdao`) | stippel-geojson, kopie | ja — haven-aanloop (LAR-586) |
| b3 | B | zee | zeeknoop 5310 → `gr-rotterdam-rhb` | Indische Oceaan, Rode Zee en Suez of Kaap | orde 12.000 km (Suez) of 17.000 km (Kaap), niet gemeten; toets 12.150 | MARNET | nee |
| b4 | C | binnenvaart | `gr-rotterdam-rhb` → Emmerich-vak (51.7540, 6.3660) | Rijn, kopie `grafiet-molo-duisburg` b4 | 161,1 | `--been` (AIS-graaf rijn) | nee |
| b5 | C | binnenvaart | Emmerich-vak → Wesel-vak (51.4000, 6.7450) | Rijn, kopie b5 (geen AIS-dekking) | 66,6 | `--been-geojson` `rivierbeen-wesel.geojson` | nee |
| b6 | C | binnenvaart | Wesel-vak → `gr-duisburg-beckena` | Rijn, kopie b6 | 7,3 | `--been` (AIS-graaf rijn) | nee |

Geen last-mile-benen: b1 eindigt op het site-anker. Geen fase D/E: de Duitse trader is anoniem en tk accelis heeft geen vestiging in een bron.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-epanko-dorp` | mijn/plant (kop) | Epanko-dorp (OSM-node 7544800946), Ulanga, Morogoro — dorp, geen terrein | -8.7114, 36.6796 | [1][8][10] | **onzeker** (z14 + z15 gezien, `sat-grafiet-epanko-duisburg-epanko-dorp*.png`: akkers, verspreide hutten en beboste heuvels langs een beek, geen mijn, plant of kale pit — pre-FID; een tweede OSM-dorpsknoop ligt op -8.7260, 36.6820) |
| `gr-daressalaam-kade` | overslag truck → zee | Dar es Salaam Port, containerkade (Kurasini-kanaal) | -6.8280, 39.2870 | brief `grafiet-lindijumbo-qingdao` §3 (letterlijk hergebruikt) | bron-gelegd (daar z18: containerstapels, schepen langszij, kranen) |
| `gr-rotterdam-rhb` | overslag zee → binnenvaart | RHB Stevedoring & Warehousing, Waalhaven Noordzijde 4 | 51.8935, 4.4585 | `routebrief-licht.md` §1, `grafiet-molo-duisburg` §3 | bron-gelegd (hergebruikt) |
| `gr-duisburg-beckena` | losplek (entrepot/stoppunt) | Duisburg-Ruhrort, Becken A | 51.4518, 6.7565 | `routebrief-licht.md` §1, `grafiet-molo-duisburg` §3 | aannemelijk (geen bron noemt Duisburg; zelfde aanname als molo) |

## 4 · Via-punten (alleen b1; 3 tussenpunten op de doorgaande weg, geen stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Ifakara (OSM-node 13015709) | -8.1321, 36.6848 | pint de Mahenge-weg naar het Kilombero-dal; de plant staat 75 km van Ifakara [5], de Dar es Salaam–Ifakara-corridor is de genoemde exportroute [5] |
| b1 | 2 | Kidatu (OSM-node 5830657009) | -7.7042, 36.9523 | pint Kidatu als schakel tussen Ifakara en Mikumi (EU-wegcorridor Kidatu–Ifakara, Mahenge–Ifakara–Mikumi [11]) |
| b1 | 3 | Mikumi op T1 | -7.4000, 37.0000 | pint de aansluiting op de doorgaande T1 richting Morogoro en Dar es Salaam; punt uit de haalbaarheidstoets (OSM-dorpsknoop Mikumi ligt 3 km westelijker op -7.4048, 36.9770) |
Bewust weggelaten: Morogoro (-7.0843, 37.4233) en Chalinze (-6.3099, 38.3262) liggen 16 en 36 km naast de weg en forceren een omweg. Refs `T1`, corridorKlassen `tertiary` + `unclassified`, vensterKm 60.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Epanko-plant (nog niet gebouwd) | EcoGraf Limited / Duma TanzGraphite | grafieterts (open pit) → vlokgrafietconcentraat | Stage 1 73 kt/j; SML 25 jaar (maart 2025); potentieel 87,6 kt/j | [1][8] |

## 6 · Stoppunt
De brief stopt bij Duisburg-Ruhrort Becken A (entrepot): de Duitse afnemer is bevestigd maar anoniem (FOB Dar es Salaam) [2] en tk accelis Trading heeft geen vestiging in een bron [6]; een eigen fase-D-anker zou een coördinaat verzinnen. Zelfde patroon als `grafiet-molo-duisburg` en `koper-lobito-duisburg`.

## 7 · Open punten
- **Mijnterrein niet gevonden:** alleen OSM-dorp Epanko; op z14/z15 geen mijn, plant of kale pit (pre-FID, plant nog niet gebouwd). Ca. 3,4 km zuid van het dorp, bij -8.742, 36.690, ligt langs een beek een reeks witte ontginningslittekens met vijvers; niet aan EcoGraf te koppelen (vermoedelijk kleinschalige delving, niet bevestigd), dus **niet** als anker gebruikt. Het mijnanker blijft onzeker; b1 begint op het dorp.
- **Duisburg staat in geen bron:** afnemers zijn tk accelis Trading (ex ThyssenKrupp Metallurgical Products) en een anonieme Duitse trader, FOB Dar es Salaam [2][6]; Duisburg is een entrepot-aanname, zoals in `grafiet-molo-duisburg`.
- **Geen gepubliceerde wegkm voor b1:** bron noemt ~370 km zonder te zeggen of dat weg is [1]; hemelsbreed 355 km; de ±15%-toets is alleen een indicatie. De bron zelf noemt Epanko–Ifakara 75 km; gemeten 77,2.
- **Weggedeelte Ifakara–Kidatu onbevestigd als doorgaande corridor in OSM-klasse tertiary/unclassified;** EU-financiering voor de weg Kidatu–Ifakara/Mikumi wordt overwogen [11], dus de wegkwaliteit is niet bekend. Concentraat gaat volgens oude plannen per truck, rail is overwogen [7].
- **Volume nul:** pre-FID, financiering (KfW-pakket genoemd in een Duits bericht, niet bevestigd) loopt; Epanko hoort in de sitelaag onder `sites_zonder_gewicht` (geen productie).
- **Zeebeen overlapt 87% met `grafiet-molo-duisburg` b3** (alleen de Afrikaanse oostkust-aanvoer verschilt, ca. 1.600 km); Dar-kade en aanloop gedeeld met `grafiet-lindijumbo-qingdao`.
- **Rode Zee structureel onzeker:** de router kiest Suez of Kaap; de brief schat niet vooraf.
- S&P-bericht [6] niet te openen (403); inhoud via zoeksamenvatting, niet zelf gelezen.

## 8 · Bronnen
[1] TanzaniaInvest, "Epanko Graphite Project output increase" — 73 kt/j Stage 1 (Updated BFS feb 2026), 87,6 kt/j (VER 24-09-2026), ~370 km vanaf Dar es Salaam, geen FID, SML maart 2025. https://www.tanzaniainvest.com/mining/epanko-graphite-project-output-increase
[2] GoldInvest, "EcoGraf: German deal for 40,000 metric tons of graphite" (2026-08-12) — 20 kt/j oplopend naar 40 kt/j, 10 jaar, FOB Dar es Salaam, anonieme Duitse trader. https://goldinvest.de/en/ecograf-german-deal-for-40-000-metric-tons-of-graphite
[3] Discovery Alert, "EGR: EcoGraf HF-free German battery facility" — Duitse anodefabriek, locatie niet genoemd, geen logistiek. https://discoveryalert.com/asx-stock-news/mining/egr-ecograf-hffree-german-battery-facility-october-2026/
[4] EcoGraf, nieuwsoverzicht (aug-okt 2026) — offtake, VER, Duitse site, financial close nog te komen. https://www.ecograf.com.au/news
[5] TanzaniaInvest, "Ifakara graphite shaping facility study" — Epanko 75 km van Ifakara; Dar es Salaam–Ifakara-corridor en TAZARA genoemd. https://www.tanzaniainvest.com/mining/ifakara-graphite-shaping-facility-study
[6] S&P Global, "EcoGraf secures German offtake deal for Tanzanian graphite project" (2026-08-12) — tk accelis Trading (ex ThyssenKrupp Metallurgical Products), via zoeksamenvatting. https://www.spglobal.com/energy/en/news-research/latest-news/metals/081226-ecograf-secures-german-offtake-deal-for-tanzanian-graphite-project
[7] Mining Technology, "Epanko graphite project" — concentraat per truck naar Dar es Salaam, rail overwogen; plantbeschrijving. https://www.mining-technology.com/projects/epanko-graphite-project/
[8] Mining Data Online, "Epanko Project" — 63 km ZZ van Ifakara, SML 3 maart 2025, 73 kt/j. https://miningdataonline.com/property/1297/Epanko-Project.aspx
[9] Wikipedia (en), "Mahenge Mountains" — Ulanga District, Morogoro Region, grafietmijnen in ontwikkeling. https://en.wikipedia.org/wiki/Mahenge_Mountains
[10] OpenStreetMap (ODbL) via Photon: Epanko nodes 7544800945 (-8.7260, 36.6820) en 7544800946 (-8.7114, 36.6796); Ifakara 13015709; Kidatu 5830657009; Mikumi 1484695822. https://www.openstreetmap.org
[11] TanzaniaInvest, "EU considers infrastructure funding for EcoGraf's Epanko project" — wegcorridor Mahenge–Ifakara–Mikumi, Kidatu–Ifakara (zoeksamenvatting). https://tanzaniainvest.com/?p=30832
[12] Esri World Imagery via `v2/tools/sat_check.py` (live, 2026-10-09): `v2/build-cache/satcheck/sat-grafiet-epanko-duisburg-epanko-dorp.png` (z14), `-epanko-dorp-z15.png`, `-epanko-dorp2.png`, `-epanko-litteken.png`, `-epanko-litteken-z17.png`.
[13] Eigen briefs `grafiet-lindijumbo-qingdao.md` (Dar-kade, aanloop 19,84 km) en `grafiet-molo-duisburg.md` (Rijn b4-b6, RHB, Becken A); centrale haalbaarheidstoets grafiet-epanko-duisburg (2026-10-09): wegkm 494,1, droogloop 12.901 km.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)

**Stroom `grafiet-epanko-duisburg`** → `v2/data/stroomroute-grafiet-epanko-duisburg.json` — 6 benen,
**12.901,4 km**, 4 markers: truck 495,8 km · zee 20,7 (stippel, haven-aanloop) + 12.149,9 km · binnenvaart
161,1 + 66,6 + 7,3 km. Bestand 161,7 KB. Recept: `bak_stromen.sh` (functie `bak_grafiet_epanko_duisburg`), profiel
`grafiet-epanko-duisburg-epanko-daressalaam` in `maak_stroombeen_weg.py` (b1 via `wegscan_puur.py`, extract `tanzania`).

Toelichting per leg:
- **b1 (truck, doorgetrokken):** vier via-segmenten Epanko-dorp → Ifakara 75,5 km (bron: 75 km) · Ifakara → Kidatu
  65,5 · Kidatu → Mikumi 43,9 · Mikumi → Dar es Salaam-kade 309,2; totaal **494,1 km** gesnoeid (15 keerlussen, 0 km
  dubbel) en **495,8 km** getekend. Via-snaps 1,73 / 0,01 / 0,08 / 0,44 / 0,01 km; wegklassen `tertiary` + `unclassified` en
  ref T1 volstonden, geen via-punt verschoven. Geen gepubliceerde wegkm (hemelsbreed 355 km): de ±15%-toets is alleen een
  indicatie, omwegfactor 1,40 is plausibel voor de Kilombero-dal-route. Plant → weg 1,73 km is een rechte first-mile-verbinding
  (dorpsknoop ligt naast de weg, 5,44 km residential) — geen via-punt bijgeschoven.
- **b2 (zee, stippel):** haven-aanloop Dar es Salaam, letterlijk hetzelfde bestand als `grafiet-lindijumbo-qingdao`
  (`...-aanloop-daressalaam.geojson`; kade 19,84 km rechte lijn, 20,7 km over water, zeeknoop 5310).
- **b3 (zee, MARNET, doorgetrokken):** zeeknoop 5310 → RHB, snaps 0,000 en 0,107 km; **12.149,9 km** (router koos Suez,
  in lijn met brief-orde 12.000 km en haalbaarheidstoets 12.150).
- **b4-b6 (binnenvaart, doorgetrokken, LETTERLIJKE KOPIE van `grafiet-molo-duisburg` b4-b6):** 161,1 + 66,6 + 7,3 = 235,0 km,
  zelfde `GRAAF_RIJN` en `rivierbeen-wesel.geojson`; "aannemelijk: één bron" staat in de beennaam.
- Alle 4 markers uit §3 meegenomen; geen fase D/E, geen luchtbeen, geen leiding, geen spoor.

**Toets-bevindingen (bakhandleiding §5):**
- Naden tussen de benen ≤ 0,07 km (max b4↔b5), ruim binnen de 5 km-norm; zee-snap op de kade is opgelost met de haven-aanloop.
- Markers: Epanko 0,0 km, Dar-kade 0,0 km, RHB 0,11 km van de lijn; **Duisburg Becken A ligt 2,15 km van de lijn** (de
  AIS-graaf snapt het Ruhrort-uiteinde daar, identiek aan molo-duisburg) — anker ≠ routeerpunt, overgenomen zoals daar.
- `toets_knikken.py`: 39 knikken ≥60°, 4 omkeringen (alle in de gekopieerde Rijn-benen), 0 TERUGLOOP; het truckbeen heeft 18 knikken
  en 0 omkeringen. `toets_rechte_benen.py --min-km 5`: geen nieuw recht been van deze stroom.
- Contract: `versie` 2, `punt_formaat` lonlat, modaliteiten {truck, zee, binnenvaart}, elk been ≥ 15 punten, 161,7 KB.

**Lessen:**
- Een eerdere afgebroken poging liet twee TEST-geojsons achter (`...-weg-epanko-daressalaam-TEST.geojson`, `...-weg-test2.geojson`,
  gitignored build-cache); niet gebruikt, de definitieve scan is `...-weg-epanko-daressalaam.geojson`.
- `maak_stroombeen_weg.py` heeft CRLF-regeleinden (anders dan `bak_stromen.sh`, LF): bij een scripted edit het anker met `
` matchen.
- Epanko ontbreekt nog in de grafiet-sitelaag (centraal, pre-FID/zonder gewicht); register-sleutel `gr-ed`.
