# Routebrief (licht) · olie — Permian (Gray Oak-leiding) → Ingleside (Texas, VS)

**stroom-id:** `olie-permian-ingleside` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Titel op de bol:** Olie · Van → Via → Naar (land): Permian (Reagan County, Texas) → Gray Oak-leiding → South Texas Gateway Terminal, Ingleside (VS)
**Keten in één zin:** Permian-schalie-ruwe olie per **pijpleiding** (Gray Oak Pipeline, 30 inch, OSM-gekarteerd van Reagan County via Central Junction naar de Ingleside Gateway Terminal) naar de exportterminal bij Ingleside aan het Corpus Christi Ship Channel — de bron-kant van de VS-schalie-ommekeer die `olie-corpuschristi-rotterdam` aan de zeekant vertelt.
**Welke as van het verhaal:** *de Amerikaanse schalie-ommekeer*, nu van veld naar kade. Jaarvolume: Gray Oak-capaciteit **1.020 kb/d** na fase 2 (mei 2026, RBN via zoekresultaat; pagina 403) — 900 kb/d bij indienstname, +80 kb/d mei 2025 [1][2][6]; de leiding draait al lang "nagenoeg vol", een gemeten doorvoer (kb/d) is **niet gevonden** (peiljaar 2025/26, capaciteit, geen doorvoer). Niet alles gaat naar Ingleside: ook Corpus Christi/Taft en Sweeny worden bediend [1][3].

## 1 · Ketenkaart
```
Gray Oak-leiding, Permian-aanvoer `ol-permian-grayoak-kop` (OSM-begin, Reagan County — routepunt, geen site)
   ──(b1 leiding · Gray Oak Pipeline, 30" · Crane-trunk → Central Junction → Ingleside ·
       687 km OSM-geometrie, 14 ways; hemelsbreed 550 km, geen wegkm)──►
   South Texas Gateway Terminal `ol-ingleside-stg` (Ingleside) ── stoppunt (exportterminal; verder: olie-corpuschristi-rotterdam)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Gray Oak-OSM-begin (31.0795, -101.4827) → South Texas Gateway Terminal (27.8268, -97.1945) | Gray Oak Pipeline "Crane to Central Junction" (+30") → "Central Junction to Ingleside" → "Ingleside Gateway to Ingleside Gateway Terminal" | **687,3 km OSM-gestikt**; gepubliceerd alleen het hele systeem ~850 mijl (~1.368 km, incl. Eagle Ford-/Sweeny-takken en verzamelaars) [1][11] — hier **hemelsbreed 550 km, geen wegkm**; de ±15%-toets is indicatie, geen norm | OSM `man_made=pipeline`, 14 way-id's, eigen stikscript `maak_leidingbeen_olie_permian_ingleside.py` → `--been-geojson "leiding|…"` | nee (eind 0,13 km van het anker, geen last mile) |

Geen fase B–E: dit is een eenbeens-keten (leiding → terminal); de zeekant is `olie-corpuschristi-rotterdam`, een gedeeld terminalanker (zie §3), géén gedeelde lijn.
**Naamfilter:** EPIC Crude (671 km) en Cactus II (541 km) liggen in OSM parallel; alleen ways met naam "Gray Oak Pipeline" (operator-tag Phillips 66 Pipeline, LLC) zijn gebruikt — de bronnen noemen Enbridge als operator, tegenstrijdig: operator hier niet genoemd.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-permian-grayoak-kop` | begin van de gekarteerde leiding — **routepunt, geen site** | Gray Oak-leidingstrook, Reagan County (OSM-ways 1104121268 e.v.) | 31.0795, -101.4827 | [8][9] | aannemelijk (z14 gezien: een rechte, kaal gehouden strook diagonaal NW-ZO door struikland met putlocaties en wegen eromheen, direct onder het kruis — leidingstrook; er lopen meerdere parallel, dus welke buis dit is volgt alleen uit de OSM-naam) |
| `ol-ingleside-stg` | eindpunt / exportterminal | South Texas Gateway Terminal (Gibson Energy), Ingleside — **HERGEBRUIK letterlijk** van `ol-corpuschristi-term` uit `olie-corpuschristi-rotterdam.md` | 27.82677, -97.19447 | [3][5][8] | bron-gelegd (z15 hergezien: tankpark met ~20 tanks aan de steiger-geul, twee tankers afgemeerd; OSM-eindpunt van de leiding ligt 0,13 km ernaast, op hetzelfde perceel) |

De leiding zelf eindigt in OSM bij **27.8277, -97.1937** (way "Ingleside Gateway to Ingleside Gateway Terminal", ondergronds, 19 nodes, aanleg 2019) [8] — binnen het terminalperceel; geen stippel nodig. Er is **geen** upstream-site: de kop in Crane/Winkler/Loving/Reeves County (originatiepunten volgens [3][4]) is in OSM niet gekarteerd.

## 4 · Via-punten
Geen — een leiding volgt één vaste buis; er is geen corridorkeuze. De 14 ways zijn de geometrie (volgorde: 1104121268, 1105284384, 1105284800, 1098449676, 1098271344, 1066747826, 1080984162, 1080983938, 1094702482, 1059837677, 1059836731, 1093594676, 1089472439, 1089472435). Grootste naad tussen ways: 0,90 km. Knooppunt Central Junction ~28.517, -98.189 (uit het ontwerp, ligt op de lijn; niet apart gelegd).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| South Texas Gateway Terminal | Gibson Energy (sinds 1-8-2023; verkopers Buckeye/Phillips 66 Partners/Gray Oak Gateway Holdings) | Permian-ruwe olie (leiding) → VLCC-export | 1 mln b/d vergund, 8,6 mln vaten opslag (20 tanken), 2 deepwater-docks, tot 2,7 mln b/d leidingconnectiviteit naar Permian/Eagle Ford; ~12% VS-crude-export 2023 | [3][5][10] |

## 6 · Stoppunt
De brief stopt bij de Gateway-terminal: een open-access exportterminal zonder genoemde afnemer per lading; het vervolg is de zeeketen `olie-corpuschristi-rotterdam` (zelfde terminalanker, opzet). Fase C/D/E vervallen: geen bron noemt een raffinaderij voor déze Gray Oak-ladingen.

## 7 · Open punten
- **De kop (Crane/Wink/Reeves, ca. 100–300 km stroomopwaarts) is niet gekarteerd** — de lijn begint midden in Reagan County bij 31.0795, -101.4827; geen verzonnen verlenging, geen stippel naar een niet-gelegde site.
- **Geen gemeten Gray Oak-doorvoer**; capaciteit 1.020 kb/d komt uit een niet-leesbare RBN-pagina (zoekresultaat) en wordt met "fase 2 mei 2026" niet door een tweede bron bevestigd.
- **Geen gepubliceerde trunk-lengte**; 850 mijl is het hele systeem. 687 km OSM tegen 550 km hemelsbreed (factor 1,25) lijkt plausibel voor een leiding zonder rechte lijn, maar blijft een schatting.
- **Operator/eigenaar tegenstrijdig** (OSM Phillips 66 Pipeline; persberichten Enbridge; 2018: 75% P66 Partners / 25% Andeavor) — niet genoemd in de beennaam.
- **Niet alle Gray Oak-olie gaat naar Ingleside** (ook Taft/Corpus Christi en Sweeny); de brief claimt het leidingtracé tot Ingleside, niet het aandeel per bestemming.

## 8 · Bronnen
[1] RBN Energy — "Gray Oak Phase 1 expansion complete": 850 mijl, 900 kb/d, +80 kb/d mei 2025, fase 2 (+40 kb/d) → 1,02 mb/d mei 2026 (alleen via zoekresultaat, pagina 403). https://rbnenergy.com/daily-posts/analyst-insight/gray-oak-phase-1-expansion-complete-%E2%80%94-brings-breathing-room-permian-corpus-route
[2] Offshore Technology, 2024 — Enbridge Gray Oak: uitbreiding 80 kb/d (2024) + evt. 40 kb/d, operator Enbridge. https://www.offshore-technology.com/newsletters/enbridge-gray-oak-oil-pipeline
[3] PGJ Online, 2018 — Phillips 66 Gray Oak: originatie Reeves/Loving/Winkler/Crane + Eagle Ford; Corpus Christi- en Sweeny/Freeport-markten; aansluiting op South Texas Gateway Terminal Ingleside; 75/25 JV. https://pgjonline.com/news/2018/04/phillips-66-to-proceed-with-gray-oak-pipeline
[4] Oil & Gas Journal — "West Texas-Gulf Coast crude line proceeds": fase 1 385 kb/d, mogelijk 700 kb/d tot 1 mb/d; aflevering Corpus Christi/Freeport/Houston. https://www.ogj.com/pipelines-transportation/pipelines/article/17297377/west-texas-gulf-coast-crude-line-proceeds
[5] Gibson Energy — South Texas Gateway Terminal: 1 mln b/d, 8,6 mln vaten, 2 docks, ~12% VS-export 2023, 2,7 mln b/d Permian-connectiviteit. https://www.gibsonenergy.com/operations/south-texas-gateway-terminal/
[6] OilPrice.com, 2019 — Gray Oak 900 kb/d; Cactus II (585 kb/d) en EPIC (400 kb/d) als parallelle Permian-Corpus-leidingen. https://oilprice.com/Energy/Energy-General/The-Pipeline-Lifeline-For-Texas-Oil.amp.html
[7] Pipeline Journal, 2024 — Enbridge Gray Oak-uitbreiding 80+40 kb/d. https://pipeline-journal.net/news/enbridge-expand-gray-oak-pipeline-capacity-120000-bpd-2025
[8] OpenStreetMap (ODbL) — 14 ways "Gray Oak Pipeline - Crane to Central Junction / Central Junction to Ingleside / Ingleside Gateway to Ingleside Gateway Terminal" (substance oil, 30"), o.a. https://www.openstreetmap.org/way/1089472435 ; lokaal gelezen uit Geofabrik `us-texas`-extract.
[9] Esri World Imagery via `v2/tools/sat_check.py` (z14 kop, z15 Ingleside) — `v2/build-cache/satcheck/sat-olie-permian-ingleside-kop.png`, `sat-olie-permian-ingleside-ingleside.png`.
[10] Gibson Energy / Canadian Lawyer, 2023 — overname South Texas Gateway Terminal van Buckeye South Texas Gateway Holdings, Gray Oak Gateway Holdings en Phillips 66 Partners Holdings (1-8-2023). https://canadianlawyermag.com/cl-plus/deals/382
[11] Enbridge Form ARS FY2025 — Gray Oak als 850-mijls systeem (alleen via zoekresultaat gezien). https://www.sec.gov/Archives/edgar/data/895728/000119312526117666/ei_form_ars_2025_10-k.pdf

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
**Bestand:** `v2/data/stroomroute-olie-permian-ingleside.json` (contract versie 2, lonlat, 50,5 KB, 1 been, 2 markers). Recept: `bash v2/tools/bak_stromen.sh olie-permian-ingleside` (functie `bak_olie_permian_ingleside`).

| # | modaliteit | been | km | punten |
|---|---|---|---|---|
| b1 | leiding | Gray Oak Pipeline, Permian-aanvoer (Reagan County) → Ingleside Gateway Terminal, OSM 14 ways, doorgetrokken | 687,3 | 2.396 |

**Totaal 687,3 km.** Markers: `ol-permian-grayoak-kop` (31.0795, -101.4827, aannemelijk) en `ol-ingleside-stg` (27.82677, -97.19447, bron-gelegd; letterlijk hergebruik van `ol-corpuschristi-term`).
**Recept:** de lijn is vooraf gestikt met `python v2/tools/maak_leidingbeen_olie_permian_ingleside.py --schrijf` (cache `olie-permian-ingleside-grayoakways-us-texas.json`) naar `v2/build-cache/ais/graaf/olie-permian-ingleside-leiding-grayoak.geojson` (FeatureCollection) en als `--been-geojson "leiding|…"` in `hecht_marnet.py route` gezet; geen router, geen via-punten, geen zee, geen haven-aanloop, geen stippel, geen last mile, geen luchtbeen, geen gedeelde kopie.
**Toets:** km 687,3 tegen hemelsbreed 550,5 (factor 1,25, geen gepubliceerde trunk-lengte: indicatie, geen norm; 850 mijl is het hele systeem). Naden: geen (één been). Markers 0,003 km (kop) en 0,12 km (terminal) van de lijn. `toets_knikken`: 16 knikken >= 60 graden, 0 omkeringen, 0 teruglopen; de scherpe knikken zijn spikes van enkele meters tot enkele tientallen meters op de way-overgangen van OSM (grootste naad tussen ways 0,90 km, langs de lijn) en een krappe bocht (383 m radius) bij 27.9443, -97.3289 — OSM-geometrie, niet gerepareerd.
**Stippels:** geen. De kop (Crane/Wink/Reeves) is niet gekarteerd; de lijn eindigt waar het bewijs eindigt.
**Lessen:** (1) bij een volledig in OSM gekarteerde leiding is de bake triviaal: stik-script + één `--been-geojson`, een FeatureCollection is verplicht; (2) filter op de way-naam, niet op alleen `man_made=pipeline`, omdat EPIC Crude en Cactus II parallel lopen; (3) operator tegenstrijdig (OSM Phillips 66, persberichten Enbridge) en dus niet in de beennaam gezet.
