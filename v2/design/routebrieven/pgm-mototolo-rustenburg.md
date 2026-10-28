# Routebrief (licht) · PGM — Mototolo via Polokwane-smelter naar Rustenburg (Zuid-Afrika)

**stroom-id:** `pgm-mototolo-rustenburg` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) ·
**status:** gebakken
**Keten in één zin:** PGM-concentraat van de Mototolo-concentrator (Valterra, Eastern Limb, Limpopo) per **truck** over lokale D-wegen
(D1335/D212/D2219/D4268), de **R579** en de **R37** naar de **Valterra Polokwane-smelter** [1][2][3]; de matte per **truck** (aannemelijk:
één bron, modaliteit niet in de bron) over R37 en N1/N4 naar het **ACP** in het Waterval-complex bij Rustenburg [3] — hetzelfde eindanker als
`pgm-rustenburg-pmr`.
**Welke as van het verhaal:** de tweede Oostelijke-rand-voeder van Polokwane naast Modikwa (RESERVE bij uitval van `pgm-modikwa-rustenburg`:
~70% van de lijn is daar identiek aan). Mototolo 2025: 270,8 koz PGM ÷ 32,15 = ~8,4 t PGM/j (Valterra-conventie, zie §7) [4].

## 1 · Ketenkaart
```
Mototolo-concentrator `pgm-mototolo-conc` ──(b1 truck · D1335 → D212 → D2219 → D4268 → R579 → R37 · hemelsbreed 127 km, geen wegkm)──►
  Polokwane-smelter `pgm-polokwane-smelter`
  ──(b2a truck · R37 noordwaarts · LETTERLIJKE KOPIE pgm-modikwa-rustenburg b2a · 13,0 km, aannemelijk)──► R37/N1-aansluiting
  ──(b2b truck · N1 → N4 · LETTERLIJKE KOPIE pgm-modikwa-rustenburg b2b · 359,9 km, aannemelijk)──► Rustenburg ACP/PMR `pgm-rustenburg-pmr` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-mototolo-conc` → `pgm-polokwane-smelter` | D-wegen → R579 → R37 | hemelsbreed 127 km, geen wegkm; OSRM-indicatie 159,1 km [11]; eigen scan 162,9 km [12] | maak_stroombeen_weg (profiel in §9-aanwijzing) | nee |
| b2a | A | truck | smelter → R37/N1-aansluiting (-23.9431, 29.4439) | R37 noord (aannemelijk: één bron) — LETTERLIJKE KOPIE `pgm-modikwa-rustenburg` b2a | 13,0 (kopie) [13] | kopie geojson `pgm-modikwa-rustenburg-weg-smelter-r37n1.geojson` | nee |
| b2b | A | truck | R37/N1-aansluiting → `pgm-rustenburg-pmr` | N1 → N4 (aannemelijk: één bron) — LETTERLIJKE KOPIE `pgm-modikwa-rustenburg` b2b | 359,9 (kopie) [13] | kopie geojson `pgm-modikwa-rustenburg-weg-polokwane-rustenburg.geojson` | nee |

Geen zee-, spoor-, binnenvaart-, leiding- of luchtbeen; geen haven-aanloop; geen fase D/E (geen bron noemt een afnemer ná ACP in deze as).
Naden gemeten op de bestaande bestanden: b1 → b2a 0,00 km, b2a → b2b 0,00 km.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-mototolo-conc` | mijn + concentrator | Mototolo Mine Concentration Plant (Valterra), OSM way 1102546958, ~50 km ZW van Burgersfort | -25.0104, 30.1137 | [2][5][8] | bron-gelegd (z15 gezien: verwerkingsgebouwen en een grote bergingsdam direct ten zuiden; de schachtcomplexen liggen ~2,9 km noordelijker rond -24.985, 30.108) |
| `pgm-polokwane-smelter` | smelter | Valterra Polokwane-smelter (OSM way 804571574), ~14 km ten zuiden van Polokwane — **hergebruikt letterlijk** uit `pgm-modikwa-rustenburg.md` | -24.0281, 29.4694 | [3][13] | bron-gelegd (z15 hier opnieuw gezien: ovengebouw met schoorstenen en rookpluim, slakdam 1 km ZW, R37 op ~1,1 km westelijk) |
| `pgm-rustenburg-pmr` | losplek / converting (ACP) | Waterval-complex, Valterra, Rustenburg — **hergebruikt letterlijk** uit `pgm-unki-rustenburg.md` | -25.6838, 27.3272 | [3][13] | bron-gelegd (overgenomen; z15 gezien bij die brief) |

## 4 · Via-punten (alleen b1; lat, lon; alle uit de OSRM-geometrie [11] en door een OSM-scan op de weg bevestigd [12])
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | D212, Steelpoort-vallei | -24.8949, 30.0828 | pint de noordelijke uitgang via D1335/D212 naar de R555-kruising i.p.v. een zuidelijke of oostelijke omweg |
| b1 | 2 | D2219 (Kgano Royal Road) | -24.7897, 29.9700 | pint de D2219-schakel tussen de R555 en de R579-aansluiting; buiten dorpskernen |
| b1 | 3 | R579 ten noorden van Jane Furse | -24.6155, 29.7246 | pint de R579 noordwaarts i.p.v. de R37 via Burgersfort; ~14 km buiten het dorp |
| b1 | 4 | R579 vlak voor de R37-aansluiting | -24.2613, 29.4705 | houdt de lijn op de R579 tot de aansluiting ten noorden van Lebowakgomo, niet de R518 het stadje in |
| b1 | 5 | R37 richting Polokwane | -24.1066, 29.4660 | pint de R37 noordwaarts naar de smelter (laatste ~9 km gedeeld met `pgm-modikwa-rustenburg` b1) |
| b2a/b2b | — | via-punten van de bron | zie `pgm-modikwa-rustenburg.md` §4 en `pgm-zimplats-rustenburg.md` §4 | ongewijzigd overgenomen (letterlijke kopie) |

Geofabrik-regio: `zuid-afrika` (alle benen).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mototolo-concentrator + chroomterugwinning | Valterra Platinum (drie declines: Lebowa, Borwa, Der Brochen) | UG2-erts → PGM-concentraat | 270,8 koz PGM (2025) | [2][4] |
| Polokwane-smelter | Valterra Platinum | concentraat (o.a. Mogalakwena ~80-90%) → ovenmatte | niet in t/j gepubliceerd | [3][9] |
| Anglo Converter Plant (Waterval) | Valterra Platinum | ovenmatte → converter-matte | niet in t/j gepubliceerd | [3] |

## 6 · Stoppunt
De brief stopt bij ACP Rustenburg (Waterval-complex, hetzelfde anker als de PMR): geen bron in dit onderzoek noemt een gedocumenteerde volgende
locatie of vervoerswijze voor de converter-matte.

## 7 · Open punten
- **BRONCONFLICT smelter.** De haalbaarheidstoets (MRMR 2025, p.71-75, door mij niet zelf geopend: bestand > 10 MB) zegt Mototolo-concentraat → Polokwane. Een Mining Weekly-bericht van 2026-10-09 [9] (alleen via zoekfragment, pagina 403) laat de UG2-voeding van de *Waterval*-smelter komen van onder meer Amandelbult en Mototolo. Gaat het concentraat rechtstreeks naar Waterval, dan is de Polokwane-schakel (b1 + b2) onjuist. Volgens de BINDENDE toets tekenen we de Polokwane-variant, als reserve en met dit voorbehoud.
- **Wegkm niet gepubliceerd.** b1: hemelsbreed 127 km (omwegfactor 1,28 tegen OSRM 159,1 km, scan 162,9 km: +2,4%); de ±15%-toets is een indicatie, de OSRM-bron is dezelfde OSM als onze scan, dus geen onafhankelijke toets. R579 is 171 km lang (Lebowakgomo-Stoffberg) [6]; hier wordt 70,6 km (OSRM) gebruikt.
- **Matte-modaliteit** Polokwane → ACP staat niet in de bron ("transported", [3]); truck is aanname — daarom "aannemelijk" in b2a/b2b.
- **Operationele status.** Op 2026-03-27 legde de DMPR Mototolo stil na een dodelijk ongeval (TMM-deviaties) [10]; of dit is opgeheven is niet gevonden. Der Brochen is een decline in ontwikkeling [2]; de eerdere afwijzing `pgm-derbrochen-rustenburg` is in de repo niet terug te vinden.
- **Klassen:** de eerste ~10 km vanaf de concentrator en de D-wegen lopen over `tertiary`/`unclassified`/`service`; het profiel vraagt `corridorKlassen: ["tertiary","unclassified"]` (scan slaagde, 0,28 km snap aan de smelterkant, laatste 0,9 km `service`).
- **Sitelaag** kent Mototolo niet (`pgm-sitelaag.json`); centraal toevoegen op -25.0104, 30.1137 met ~8,4 t PGM (niet door mij aangepast). Wikipedia noemt het mijnpunt op 24°59'07"S 30°06'28"E (schachtcomplex) [5].
- **Volume:** Valterra IAR 2025 270,8 koz (2024: 276,5 koz) via de haalbaarheidstoets [4]; controle: Q3 2025 66,2 koz (−11%) uit een zoekfragment [4b]. Mix: Valterra "PGM" (de toets noemt 4E+; Valterra rapporteert doorgaans 5E+Au) — niet nagelezen. 270,8 ÷ 32,15 = 8,4 t.
- **Overlap:** b2a+b2b 100% gedeeld met `pgm-modikwa-rustenburg`; b1 deelt ~22 km R37 (R579-aansluiting → smelter) met P1 b1; eigen geometrie 163 km van 536 (30%). b2a loopt eerst ~10 km noordwaarts voor de N1-aansluiting (kopie, niet onderzocht).

## 8 · Bronnen
[1] Valterra Platinum, Ore Reserves and Mineral Resources report 2025, p.71-75 (via de haalbaarheidstoets; niet zelf geopend), https://www.valterraplatinum.com/wp-content/uploads/2026/05/ore-reserves-and-mineral-resources-report-2025.pdf
[2] Valterra Platinum, Mining operations — Mototolo (50 km ZW van Burgersfort; declines Lebowa, Borwa, Der Brochen; concentrator + chroomplant), https://www.valterraplatinum.com/mine-to-market/mining-operations/
[3] SAIMM, Snodgrass e.a., Pyrometallurgy 2024 (concentraten van AAP-, JV- en derden-concentrators per truck naar de smelters; ovenmatte naar het ACP; zelf gelezen), https://www.saimm.co.za/Conferences/files/pyrometallurgy-2024/16_646-Snodgrass.pdf
[4] Valterra Integrated report 2025 (Mototolo 270,8 koz; via de haalbaarheidstoets), https://www.valterraplatinum.com/wp-content/uploads/2026/05/integrated-report-2025.pdf · [4b] Engineering News, Valterra Q3 2025 (Mototolo 66.200 oz; zoekfragment, pagina 403), https://www.engineeringnews.co.za/print-version/valterras-third-quarter-volumes-dip-but-it-expects-these-will-recover-soon-2025-10-28
[5] Wikipedia, Mototolo mine (24°59'07"S 30°06'28"E, Burgersfort), https://en.wikipedia.org/wiki/Mototolo_mine
[6] Wikipedia, R579 road (South Africa) (171 km; begint aan de R37 bij Lebowakgomo), https://en.wikipedia.org/wiki/R579_(South_Africa)
[7] Wikipedia, R37 road (South Africa) (304 km; Polokwane-R579-Lebowakgomo-Burgersfort), https://en.wikipedia.org/wiki/R37_(South_Africa)
[8] OpenStreetMap-contributors (ODbL) via Nominatim: "Mototolo Mine Concentration Plant", way 1102546958 (-25.01035, 30.11366)
[9] Mining Weekly, Jameson cells saving Valterra R203m (Polokwane ~80-90% Mogalakwena; Waterval UG2-voeding; zoekfragment), https://www.miningweekly.com/article/jameson-cells-saving-valterra-platinum-r203m-keeping-3-000-trucks-off-road-2026-10-09
[10] IOL, Valterra onderzocht na dodelijk ongeval bij Mototolo (2026-04-07), https://iol.co.za/news/south-africa/2026-04-07-valterra-platinum-under-investigation-following-workers-death-at-motolotolo-mine-in-limpopo/
[11] OSRM (router.project-osrm.org, 2026-10-28): 159,06 km; D1335 8,8 · D212 13,0 · R555 3,6 · D2219 ~27 · D4268 8,7 · R579 70,6 · R37 22,7 km (eigen indicatie)
[12] Eigen OSM-wegscan (`v2/tools/wegscan_puur.py`, zuid-afrika, 2026-10-28): 162,9 km, via-snaps ≤ 0,01 km, eind-snap 0,28 km; geojson `v2/build-cache/ais/graaf/pgm-mototolo-rustenburg-weg-mototolo-polokwane.geojson`
[13] `v2/design/routebrieven/pgm-modikwa-rustenburg.md` (b2a/b2b, smelteranker) · `pgm-zimplats-rustenburg.md` · `pgm-unki-rustenburg.md` (anker PMR)
[14] Esri World Imagery via `v2/tools/sat_check.py` (z14/z15): `v2/build-cache/satcheck/sat-pgm-mototolo-rustenburg-mototolo.png`, `…-mototolo-z14.png`, `…-smelter.png`

## 9 · Gebakken (2026-10-28, lichte werkwijze, M31 golf 10)
Functie `bak_pgm_mototolo_rustenburg` in `v2/tools/bak_stromen.sh`; profiel `pgm-mototolo-rustenburg-mototolo-polokwane` in `maak_stroombeen_weg.py`; uitvoer `v2/data/stroomroute-pgm-mototolo-rustenburg.json` (85,3 KB, versie 2, lonlat, 3 benen, 3 markers, 536,2 km, 4.141 punten). Draaien: `bash v2/tools/bak_stromen.sh pgm-mototolo-rustenburg`.

| # | modaliteit | km gemeten | brief | naad | geometrie |
|---|---|---|---|---|---|
| b1 | truck | 163,3 | hemelsbreed 127; OSRM 159,1 (indicatie, geen wegkm) | 0 (start op het anker) | eigen wegscan (`wegscan_puur.py`, zuid-afrika, 2.010 punten) |
| b2a | truck | 13,0 | 13,0 (kopie) | 0,000 km | LETTERLIJKE KOPIE `pgm-modikwa-rustenburg-weg-smelter-r37n1.geojson` |
| b2b | truck | 359,9 | 359,9 (kopie) | 0,000 km | LETTERLIJKE KOPIE `pgm-modikwa-rustenburg-weg-polokwane-rustenburg.geojson` |

**Recept b1:** 7 punten (anker, 5 via-punten uit §4, smelter), refs R579 en R37, vensterKm 45, `corridorKlassen` tertiary + unclassified; via-snaps 0,00-0,01 km, eindsnap 0,28 km, 4 keerlussen gesnoeid (163,0 → 162,9 km); eerste 10,0 km over kleine klassen (service/tertiary/unclassified), laatste 0,9 km `service`. De scan-uitvoer was al gemaakt en is met het nieuwe profiel reproduceerbaar herbouwd (zelfde 162,9 km).

**Toets:** b1 +2,6% op de OSRM-indicatie (163,3 tegen 159,1) en +2,4% op de eigen scan van de brief; de ±15%-toets is hier een indicatie (OSRM en scan delen dezelfde OSM-bron). b2a/b2b zijn byte-gelijk aan hun bron. Geen stippel, geen haven-aanloop, geen zee/lucht/leiding; geen naad > 0,001 km; de drie markers liggen op de lijn (0,0 km). `toets_knikken.py`: b1 13 knikken, 0 omkeringen, geen terugloop (spikes van enkele tot ~110 m radius). `toets_rechte_benen.py --min-km 5`: geen bevinding voor deze stroom.

**Bevinding (niet van deze stroom):** de gekopieerde b2b heeft een TERUGLOOP-knik van 150 graden bij -25.70456, 27.25575 (8 m) vlakbij Rustenburg; die zit in de bron `pgm-modikwa-rustenburg` (en `pgm-zimplats-rustenburg`) en is hier bewust niet aangepast (letterlijke kopie). Meld aan de eigenaar van die bron.

**Lessen:** (1) De brief meldde het geojson als al gemaakt, maar het profiel stond nog niet in `maak_stroombeen_weg.py`; zonder profiel is de scan niet herhaalbaar. (2) Een heredoc-naar-python met backslash-regeleinden werd in deze omgeving tot één regel samengetrokken; opgelost door de regeleinden via `chr(92)` te schrijven. (3) `bash bak_stromen.sh` leest het script incrementeel: een gelijktijdige edit door een andere agent gaf achteraf een foutregel ("Geen: No such file") ná een geslaagde bake; het resultaat was niet aangetast.

**Open (centraal):** register (sleutel `pgm-mt`), sitelaag-punt Mototolo (-25.0104, 30.1137, ~8,4 t), bundel, BUNDEL_VERSIE, ?v=; bronconflict smelter (§7) en de DMPR-stillegging blijven open.
