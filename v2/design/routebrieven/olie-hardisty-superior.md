# Routebrief (licht) · Olie · Hardisty → Clearbrook → Superior (Canada → VS)

**stroom-id:** `olie-hardisty-superior` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) ·
**status:** gebakken
**Keten in één zin:** Canadese oliezandcrude per **pijpleiding** (Enbridge **Line 3**, 36 inch na vervanging) van de
Hardisty-tankopslaghub (Alberta) via Kerrobert, Regina (Saskatchewan), Cromer, Gretna (Manitoba), de grens bij
Neche/Gretna (Noord-Dakota) en Clearbrook (Minnesota) naar de **Enbridge Superior Terminal** (Wisconsin) aan Lake Superior.
**Welke as van het verhaal:** de tweede Canada-VS-corridor naast Keystone (`olie-hardisty-cushing`): Line 3 voedt
het Midwest/Great Lakes-net via Superior. Jaarvolume: **760 kb/d** ontwerpcapaciteit na de vervanging (terug naar de
historische capaciteit; voorheen gemiddeld 390 kb/d), Enbridge via [3][4], peiljaar 2021 (VS-deel operationeel 1 okt. 2021);
**actuele doorvoer niet bevestigd**.

## 1 · Ketenkaart
```
Hardisty-tankopslaghub `ol-hardisty-terminal` (Alberta)
  ──(b1 leiding · Enbridge Line 3 Replacement (1.062 km in OSM) + Lakehead-mainlinecorridor (609 km) · 1.659 km [1];
      Kerrobert → Regina → Cromer → Gretna/Neche → Clearbrook MN)──►
Enbridge Superior Terminal `ol-superior-terminal` (Superior, Wisconsin) ── stoppunt (breakout-terminal)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Hardisty-terminal → Superior Terminal | Enbridge Line 3 (Replacement) plus Lakehead-mainlinecorridor (SK/MB: Line 3 staat daar onder de naam Lakehead Pipeline) | 1.659 km [1][5]; OSM-gestikt **1.674,9 km (+1,0%)** | OSM-pipeline, 93 ways, Dijkstra-stik (`maak_leidingbeen_olie_hardisty_superior.py`) | nee (zes naden 0,02-1,4 km, alle < 2 km) |

Aannemelijk-status: geen — herkomst, route, eindpunt en vervanging zijn bij meerdere bronnen gelijk [1][2][3][4][5].

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-hardisty-terminal` | kop van de leiding | Hardisty-tankopslaghub (Enbridge Hardisty Terminal) | 52.6437, -111.2800 | letterlijk uit `olie-hardisty-cushing.md` §3 [8]; Line 3 begint in Hardisty [1][5] | bron-gelegd (daar z17: tankbatterij van zes ronde tanks langs de leidingcorridor ten zuiden van het dorp) |
| `ol-superior-terminal` | losplek / breakout-terminal (stoppunt) | Enbridge Superior Terminal, Superior (Wisconsin) | 46.6895, -92.0635 | OSM-leidingeinde van Line 3 Replacement (way 1189854768) + Esri z15 [6][7]; Superior is het oostelijke eind van Line 1-4 en 67 [2] | bron-gelegd (z15 gezien: tankenpark met tientallen ronde tanks in gewalde vakken aan beide zijden van het punt, raffinaderij met procesinstallaties ca. 0,5-1 km westelijk, rangeeremplacement; punt ligt 0,4 km van de leidingkop) |

Niet gebruikt: Enbridge-kantoor 46.7215, -92.0985 (OSM-label, geen terminal); stadscentra Hardisty en Superior.

## 4 · Via-punten
*Geen corridorkeuze: een pijpleiding volgt een aangelegde buis, en de gestikte lijn is OSM-geometrie. Controle-punten voor de bake (afstand lijn ↔ plaats, gemeten op de stik):
Kerrobert 1,7 km · Regina 4,7 km · Cromer 0,0 km · Gretna 2,1 km · Clearbrook (MN) 0,35 km — alle langs de corridor [3][4].*

## 5 · Verwerkingsknopen
*Geen: pompstations en de Clearbrook-terminal (breakout-tankage op Line 3/4/2B [2]) zijn geen overslag naar een andere drager; geen marker.*

## 6 · Stoppunt
De brief stopt bij de Superior Terminal: geen bron koppelt déze lading aan één met naam genoemde raffinaderij; Superior is zelf een
breakout-knoop waar Lines 1-4 en 67 eindigen en Lines 5, 6, 14, 61 en 64 beginnen [2] (Murphy/Husky-raffinaderij daar direct gekoppeld aan de
buis [2], maar niet aan deze stroom toegewezen). Fase C/D/E vervallen.

## 7 · Open punten
- **Actuele doorvoer niet bevestigd:** 760 kb/d is de ontwerpcapaciteit [3][4], bron uit 2014-2021; Wikipedia noemt "bijna 800 kb/d" [1].
- **Line 3 staat in OSM in SK en MB (ca. 609 km: Regina - Cromer - Gretna) onder de naam "Lakehead Pipeline"**, niet als "Line 3". Parallelle Enbridge-lijnen (Line 1, 2, 4, 67)
  delen die corridor; de gestikte lijn is daar de corridor, niet bewezen de buis Line 3 zelf.
- **Naden:** Hardisty-ankerpunt 0,46 km van de eerstvolgende way-node plus een brug van 1,38 km naar de kop van de Line 3 Replacement-ways; vijf bruggen 0,02-1,29 km; eind 0,002 km van het Superior-anker.
- **Eenzijdige hemelsbreedte:** hemelsbreed Hardisty-Superior 1.527 km; langste ongebroken OSM-segment 11,2 km (rechte pijpstrekking).
- **Superior-eindraffinaderij en vervolgleidingen** (Line 5, 6, 61 e.a.) niet getekend; geen bron koppelt de lading.

## 8 · Bronnen
[1] Wikipedia, "Enbridge Line 3" — 1.659 km Hardisty-Superior, Canadees deel in dienst dec. 2019, VS-deel 1 okt. 2021, bijna 800 kb/d. https://en.wikipedia.org/wiki/Enbridge_Line_3
[2] Wikipedia, "Lakehead System" — Lines 1-4/67 Edmonton/Hardisty-Superior, Clearbrook-knoop (Line 65, Minnesota Pipeline), Superior = oostelijk eind en start Lines 5/6/14/61/64. https://en.wikipedia.org/wiki/Lakehead_System
[3] NS Energy, "Enbridge Line 3 oil pipeline replacement" — Canadees deel 1.066 km Hardisty-Gretna, VS Neche-Superior, 760.000 bpd, 36 inch, terminals Clearbrook en Superior. https://www.nsenergybusiness.com/projects/enbridge-line-3-oil-pipeline-replacement/
[4] Council of Canadians, "Enbridge seeks 760,000 bpd pipeline to Lake Superior" (2014, bijgewerkt 2022) — Kerrobert, Glenavon, Regina, Cromer, Gretna, Clearbrook; 390 -> 760 kb/d. https://canadians.org/analysis/enbridge-seeks-760000-bpd-pipeline-lake-superior/
[5] Wikipedia, "Line 3 pipeline" — Hardisty-Superior 1.659 km, 34 inch origineel (1968). https://en.wikipedia.org/wiki/Line_3_pipeline
[6] OpenStreetMap-bijdragers (ODbL), lokale Geofabrik-extracts canada, us-north-dakota, us-minnesota, us-wisconsin: `man_made=pipeline`, `substance=oil`, "Enbridge Line 3 Replacement" 332 km (AB/SK) + 199,5 km (MB incl. ND-overlap) + 585 km (MN) + 33 km (WI); "Lakehead Pipeline" 1.121 km (CA); pyosmium-scan 2026-10-30.
[7] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-olie-hardisty-superior-superior.png` (z15, Superior).
[8] Eigen brief `olie-hardisty-cushing.md` §3 (anker Hardisty, satelliet z17).
[9] Aitkin County (MN) correspondentie 2015 (via zoekresultaat, niet opgehaald) — 760 kb/d. https://www.aitkincountymn.gov/board/2015/08-11-2015/correspondence081115.pdf

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
**Bestand:** `v2/data/stroomroute-olie-hardisty-superior.json` (40,0 KB, versie 2, lonlat) · **Recept:** `bak_olie_hardisty_superior()` in `v2/tools/bak_stromen.sh`;
geometrie `python v2/tools/maak_leidingbeen_olie_hardisty_superior.py --schrijf` (cache `olie-hardisty-superior-ways.json`) → `olie-hardisty-superior-leiding-line3.geojson` (FeatureCollection).
Titel: "Olie · Hardisty (Alberta) → Enbridge Line 3 → Superior Terminal (Wisconsin)".

| # | modaliteit | been | km gemeten | km brief | punten | stippel |
|---|---|---|---|---|---|---|
| 1 | leiding | Enbridge Line 3 (Replacement) plus Lakehead-mainlinecorridor, Hardisty naar Superior | 1.674,9 | 1.659 (+1,0%) | 1.915 | nee |

Totaal 1.674,9 km · 1 been · 2 markers (`ol-hardisty-terminal` 52.6437,-111.2800 · `ol-superior-terminal` 46.6895,-92.0635).
**Toets:** km binnen ±15% (+1,0%, brief geeft een echte leidinglengte); geen naden tussen benen (één been; interne OSM-naden 0,02-1,4 km, brief §7);
Superior-marker 0,001 km van de lijn, Hardisty-marker 0,46 km (procesgat tot de eerste way-node, binnen ~0,5 km);
`toets_knikken`: 67 knikken, 2 omkeringen (178 gr bij 49.500,-99.12, "scherpe bocht, echt", v=1,1), 0 terugloop; `toets_rechte_benen`: geen melding voor deze stroom; json.load, versie 2, lonlat, modaliteit {leiding}.
**Toelichting:** leiding doorgetrokken want OSM heeft de buis (93 ways); geen stippel, geen haven-aanloop, geen zee, geen kopie van een andere stroom (alleen het Hardisty-anker is gedeeld met olie-hardisty-cushing).
**Bevindingen/lessen:** (1) in SK en MB (ca. 609 km) heet de buis in OSM "Lakehead Pipeline" en delen parallelle Enbridge-lijnen de corridor: de lijn is daar de corridor, niet bewezen Line 3 zelf; (2) actuele doorvoer niet bevestigd (760 kb/d = ontwerpcapaciteit); (3) stoppunt Superior: geen bron noemt een eindraffinaderij; (4) een vooraf gestikt leidingbeen werkt zonder wegscan of zwaar rekenwerk, de bake duurt minuten.
