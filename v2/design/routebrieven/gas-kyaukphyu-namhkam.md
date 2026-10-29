# Routebrief (licht) · gas — Kyaukphyu (Maday) → Mandalay-corridor → Namhkam (Myanmar)

**stroom-id:** `gas-kyaukphyu-namhkam` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** Shwe-gas (offshore Rakhine-bekken, ~60 km uit de kust) wordt bij Kyaukphyu aangeland op Maday Island, gaat per **gasleiding** (CNPC/MOGE, parallel aan een olieleiding) over het Myanmarese binnenland — langs Mandalay en Pyin Oo Lwin — naar het laatste gekarteerde punt bij Namhkam, ~25 km voor de Chinese grens bij Ruili. De Malakka-omzeiling: gas van de Golf van Bengalen naar Yunnan zonder schip.
**Welke as van het verhaal:** ca. **4 bcm/j** werkelijk (24 bcm naar China 2013-2019 [6], CNPC-afname volgens Interfax via Irrawaddy [5]); capaciteit 12 bcm/j [1]; Shwe produceert ~20 mcm/d ≈ 7,3 bcm/j [2]. Peiljaar niet scherp, zie §7.

## 1 · Ketenkaart
```
Shwe-veld (offshore, ~60 km uit Kyaukphyu [2]) — niet getekend, geen brongegeven platformcoordinaat
  ──(b0 subzee-aanvoer naar Maday — NIET GETEKEND)──►
Kyaukphyu/Maday-gasaanlanding `gas-kyaukphyu-terminal` (CNPC/MOGE, Maday Island, Rakhine)
  ──(b1 leiding · onderzees/landfall-stuk Maday → OSM-leidingbegin · 8,0 km · STIPPEL, schematisch)──►
OSM-leidingbegin op het vasteland (19.3691, 93.7606) — routepunt, geen site
  ──(b2 leiding · Myanmar-China-gasleiding via Magway, Mandalay, Pyin Oo Lwin · 740,8 km OSM, 37 ways)──►
OSM-leidingeinde `gas-namhkam-leidingeinde` (Namhkam, Shan, open akker) ═══ stoppunt ═══ (~25 km voor Ruili)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-kyaukphyu-terminal` → OSM-leidingbegin | onderzees/landfall Maday → vasteland | 8,0 hemelsbreed; Wikipedia noemt 5,3 km onderzees [1] | `--stippel` rechte lijn | **ja: offshore/landfall niet gekarteerd** |
| b2 | A | leiding | OSM-leidingbegin → `gas-namhkam-leidingeinde` | Myanmar-China pipeline (Rakhine, Magway, Mandalay, Shan) | **740,8** OSM [7]; tegen 793 Myanmar-sectie tot Ruili [3] en 771 [1]: -6,6% / -3,9% (stopt 25 km voor de grens, zie §6) | `--been-geojson` OSM gestikt (FeatureCollection) | nee |

Doorgetrokken 740,8 km; stippel 8,0 km = 1,1% van de getekende 748,8 km. Plus ~25 km hemelsbreed tot Ruili [9] ≈ 774 km, dus -2,4% tegen 793. Fase B (grensovergang Ruili) **vervalt**: geen gas-way van het china-extract oostelijk van 97,7 E.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-kyaukphyu-terminal` | gasaanlanding / leidingbegin | Maday Island, Kyaukphyu (CNPC/MOGE) | 19.3646, 93.6844 | [1][3][8] | aannemelijk (z15 gezien: tankpark met ~12 ronde tanks, kantoor- en procesgebouwen en twee steigers naar het NO op de oostpunt van het eiland; de tanks horen bij de olieterminal, een apart gasstation is niet aanwijsbaar; Wikipedia-coordinaat 19.36444/93.68444 ligt op de rand van het complex) |
| (routepunt) | OSM-leidingbegin vasteland | geen site, geen marker | 19.3691, 93.7606 | [7][8] | OSM-vertex (z15 gezien: rand van een beboste heuvelrug aan rijstakkers, geen installatie; 8,0 km oostelijk van Maday) |
| `gas-namhkam-leidingeinde` | stoppunt (OSM-leidingeinde) | ten westen van Namhkam, Shan | 23.8653, 97.6724 | [7][8] | onzeker als site (z15 gezien: open akkers en dorpen, rivier ~2 km ZO; geen station of compound; de lijn eindigt waar OSM eindigt) |

## 4 · Via-punten
Niet van toepassing (leidingbenen: OSM-geometrie of stippel, geen corridorkeuze door ons). Corridor-controle op het gestikte pad, hemelsbreed tot Wikipedia-centra [9]: Pyin Oo Lwin 3,7 km (pad-km 466), Mandalay 24,3 km (pad-km 429), Muse en Ruili 26,8 resp. 25,2 km voorbij het eind. Dit klopt met de routebeschrijving in [1] (Mandalay, Pyin Oo Lwin, Namkham).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Shwe-gasproject (blokken A-1/A-3) | POSCO International 51%, MOGE, ONGC Videsh, GAIL, KOGAS | offshore gas → subzee-pijp naar Kyaukphyu | ~20 mcm/d (≈7,3 bcm/j); fase 2 (COOEC, 2027) | [2] |
| Maday/Kyaukphyu-aanlanding | CNPC 50,9% / MOGE | subzee-gas → landleiding | 12 bcm/j naar China + ~1 bcm/j Myanmar [3]; ontwerp tot 13 | [1][3] |

## 6 · Stoppunt
OSM-leidingeinde bij Namhkam (23.8653, 97.6724), ~25 km voor Ruili: het china-extract kent geen gas-way oostelijk van 97,7 E en geen bron legt een Chinees grensstation, dus de lijn eindigt waar het bewijs eindigt. Fase D/E vervallen (geen bron noemt een afnemer op deze korrel).

## 7 · Open punten
- **Id noemt Namhkam, niet Ruili:** het Chinese deel (~43 km, grens Ruili) is niet gekarteerd; geen grensanker, geen stippel naar Ruili.
- **b0 niet getekend:** Shwe-platformcoordinaat en de subzee-aanvoer naar Maday niet gebrond. Wikipedia noemt 5,3 km onderzees met vastelandlanding op 19.3573, 93.7343 [1]; het OSM-pad begint 3,1 km oostelijker (19.3691, 93.7606): getekend 8,0 km schematisch, geen waarheid.
- **228 km van het pad (11 ways, waarvan 83 km wel de naam draagt; zonder naam o.a. 1503506869, 1503506870, 1503506872, 1503506874) heeft geen substance-tag**; in de gestikte set staan geen olie-ways, maar de parallelle olieleiding deelt de corridor, geometrie praktisch gelijk. 512,6 km draagt `substance=gas`, 289,0 km draagt de naam "Myanmar - China pipeline".
- **Begin van de gasleiding:** [3] noemt Ramree Island/Kyaukphyu voor gas en Maday voor olie, Wikipedia [1] Maday voor beide; het tankpark op Maday hoort bij de olieterminal.
- **Volume vaag:** 4 bcm/j (Interfax, ca. 2019-2020, [5] niet rechtstreeks te lezen: 403) tegen ~7,3 bcm/j (20 mcm/d [2], zonder peiljaar) tegen 12 bcm/j capaciteit; Irrawaddy noemt een eerste jaar op ~15% van de capaciteit. Gloedgewicht: werkelijk 4 bcm/j.
- **Burgeroorlog (sinds 2021):** delen (Arakan, noordelijk Shan) wisselen van controle; doorzet onzeker [1].
- Wikipedia noemt 771 km bij de olieleiding [1], [3] noemt 793 km voor de Myanmar-sectie: km-toets is indicatie, geen norm.

## 8 · Bronnen
[1] Wikipedia, "Sino-Myanmar pipelines" (route, gas sinds 21-10-2013, Maday 19.3644/93.6844, 5,3 km onderzees, CNPC 50,9%/MOGE, 12 bcm/j) https://en.wikipedia.org/wiki/Sino-Myanmar_pipelines
[2] Wikipedia, "Shwe Gas project" (60 km offshore, ~20 mcm/d, eigenaren, fase 2 COOEC 2024-2027) https://en.wikipedia.org/wiki/Shwe_Gas_project
[3] Offshore Technology, "The pipeline will reduce China's energy import costs" (793 km Myanmar-sectie, 2.520 km totaal, 13 bcm/j, Ramree/Maday) https://www.offshore-technology.com/projects/-myanmar-china-pipelines/
[4] Natural Gas World, "China-Myanmar Pipeline Has Supplied 1.87 Bcm of Gas to China" (cumulatief tot 27-7-2014) https://www.naturalgasworld.com/china-myanmar-pipeline-has-supplied-1.87-bcm-of-gas-to-china-13106
[5] The Irrawaddy, business/65885 (CNPC-afname ~4 bcm/j volgens Interfax; alleen via zoekresultaat, pagina 403) https://www.irrawaddy.com/business/65885.html
[6] Global Times, "China-Myanmar energy projects going full steam", 17-1-2020 (24 bcm naar China 2013-2019; alleen via zoekresultaat, 403) https://www.pressreader.com/china/global-times/20200117/282372631563850
[7] OpenStreetMap-bijdragers (ODbL), Geofabrik-extract myanmar, `man_made=pipeline`: 37 ways gestikt Kyaukphyu-Namhkam (o.a. 1330247451, 1322457108, 233730818, 1503506853); https://www.openstreetmap.org/way/1322457108
[8] Esri World Imagery via `v2/tools/sat_check.py`, z15: `sat-gas-kyaukphyu-namhkam-maday.png`, `-pijpbegin.png`, `-namhkam-eind.png` in `v2/build-cache/satcheck/`.
[9] Wikipedia API (coordinaten): Mandalay 21.9831/96.0844, Pyin Oo Lwin 22.0346/96.4587, Muse 23.9792/97.9047, Ruili 24.018/97.856.
[10] Ketenontwerp + haalbaarheidstoets M31 golf 11 (workflow-invoer, orkestrator): pad 740,8 km, 37 ways, naden 0; dry-run `hecht_marnet route` 748,8 km, 2 markers.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
**Bestand:** `v2/data/stroomroute-gas-kyaukphyu-namhkam.json` (33,0 KB, versie 2, punt_formaat lonlat), 2 benen, 2 markers, totaal 748,8 km.
**Recept:** functie `bak_gas_kyaukphyu_namhkam()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh gas-kyaukphyu-namhkam`); geen wegscan, geen profiel; leidinggeometrie is het vooraf gestikte OSM-pad `v2/build-cache/ais/graaf/gas-kyaukphyu-namhkam-leiding-kyaukphyu-namhkam.geojson` (FeatureCollection, 37 ways).

| # | modaliteit | been | km gemeten | km brief | stijl |
|---|---|---|---|---|---|
| b1 | leiding | Maday-eiland naar OSM-leidingbegin vasteland (19.3646,93.6844 naar 19.3691,93.7606) | 8,0 | 8,0 hemelsbreed (Wikipedia 5,3 onderzees) | STIPPEL (offshore/landfall niet gekarteerd) |
| b2 | leiding | Myanmar-China gasleiding Kyaukphyu naar Namhkam (OSM) | 740,8 (1.670 punten) | 740,8 OSM; 793 Offshore Tech, 771 Wikipedia | doorgetrokken |

**Toets:** b2 740,8 km is de OSM-lengte zelf (-6,6% tegen 793, -3,9% tegen 771; stopt 25 km voor de grens, dus indicatie en geen norm). Naden: b1 naar b2 0,002 km. Beide markers liggen op de lijn (0,0 km). `toets_knikken`: 27 bochten van 60 gr of meer (spikes en krappe bochten in bergterrein Rakhine/Magway/Shan), 0 omkeringen, 0 terugloop; geen reparatie nodig. `toets_rechte_benen` meldt alleen de stippel b1 (bedoeld). Geen zee, weg, spoor, lucht, haven-aanloop of kopie.
**Toelichting stippel:** alleen b1 (1,1% van de keten): de onderzeese aanvoer en het landfall bij Maday staan niet in OSM; de lijn is schematisch en geen waarheid (Wikipedia-landfall 19.3573,93.7343 ligt 3,1 km van het OSM-begin). Het routepunt 19.3691,93.7606 heeft bewust geen marker.
**Toelichting leiding:** 228 km (11 ways) draagt geen substance-tag; de parallelle olieleiding deelt de corridor. Het Chinese deel (~25 km tot Ruili) is niet gekarteerd; de lijn eindigt waar OSM eindigt.
**Lessen:** (1) een vooraf gestikt OSM-pad dat als FeatureCollection op schijf staat bakt in één run (12 s router-laad, geen slot-wachttijd); (2) bij een bijna-100%-OSM-leiding blijft de stippel beperkt tot het offshore-stuk, en het routepunt waar de stippel in de OSM-lijn overgaat krijgt geen marker.
