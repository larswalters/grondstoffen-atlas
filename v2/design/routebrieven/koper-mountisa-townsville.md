# Routebrief (licht) · koper — Mount Isa-smelter → Copper Refineries, Townsville

**stroom-id:** `koper-mountisa-townsville` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Titel:** Koper · Mount Isa-smelter → Spoor → Copper Refineries Townsville (Australië)
**Keten in één zin:** koperanodes (99,7 % Cu) van de Glencore-kopersmelter in Mount Isa per **spoor** (Great Northern Railway, Mount Isa-lijn, ~1.000 km) naar de IsaKidd-kathoderaffinaderij Copper Refineries in Stuart, Townsville; verwerker → verwerker, daarna stoppunt.
**Welke as van het verhaal:** *Australië als gesloten Glencore-verwerkingsketen* (reserve-as): smelter 200–250 kt anode/jaar (NS Energy: upgrade naar 250 kt; sitelaag 250 kt Cu/j) naar een raffinaderij tot 300 kt kathode/jaar, peiljaar nameplate 2024-2025 [1][2]. **De lading mag nul zijn** (besluit 2026-08-05, "weg is echt, lading nog niet"): de mijnen sloten H2 2025 en de smelter lag in 2026 ~4 maanden stil, herstart niet bevestigd (§7).

## 1 · Ketenkaart
```
Mount Isa-smelter `cu-mountisa-smelter` ──(b1 spoor · Great Northern Railway / Mount Isa-lijn via Cloncurry, Hughenden, Charters Towers · 979,6 km gemeten, "nearly 1,000 km" gepubliceerd)──►
Copper Refineries, Stuart (Townsville) `cu-townsville-raffinaderij` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Mount Isa-smelter → Copper Refineries, Stuart | Great Northern Railway (Mt Isa line): Mount Isa–Duchess–Cloncurry–Julia Creek–Hughenden–Charters Towers–Townsville/Stuart | "nearly 1,000" [3]; Aurizon ~1.000-km-corridor | toets_spoorroute (BAKE_SUFFIX=-raw, extract australie), één run smelter → raffinaderij | nee |

Beennaam: `trein Mount Isa-smelter → Copper Refineries Townsville (aannemelijk: Glencore zegt "rail and road", Great Northern Railway, 1-op-1-net)`.
Spoor-versus-weg is niet gepubliceerd; het spoor is de gedocumenteerde drager (Glencore-wagons, ook de ontsporing 5-12-2025 betrof een Glencore-lading op deze lijn [5]); de weg blijft ongetekend.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-mountisa-smelter` | laadplek anodes (kop b1) | Mount Isa Mines-kopersmelter (Glencore) | -20.7292, 139.4829 | sitelaag `w-mount-isa-smelter` (OSM building "Copper Smelter") [4] | bron-gelegd (z15 gezien: smelterstapels, concentrator- en smeltergebouwen op het industrieterrein ten westen van de spoorlijn; spoor snapt op 0,18 km) |
| `cu-townsville-raffinaderij` | losplek anodes / raffinaderij (staart b1) | Copper Refineries Pty Ltd, 100 Hunter Street, Stuart | -19.3395, 146.8510 | Glencore-adres [1]; Nominatim "Hunter Street, Stuart" -19.3421, 146.8523 (0,3 km) | aannemelijk (z15 gezien: groot industriecomplex met hallen op het adres, rangeerterrein ~1 km oostelijk; geen OSM-object met naam, dus één bron + beeld; spoor snapt op 0,35 km) |

Hergebruik: Townsville-haven Berth 11 (-19.2441, 146.8358, `ag-townsville-haven`, brief zilver-cannington-townsville) is NIET de raffinaderij (1,76 km ernaast Stuart-kant; hier alleen referentie) en wordt niet gebruikt.

## 4 · Via-punten
Geen. De Mount Isa-lijn is de enige spoorverbinding; er is geen corridorkeuze. Eén directe router-run (979,6 km, 707 edges, verhouding 1,25 op de grootcirkel 785 km, 0 bochten ≥60°) loopt via Duchess/Kuridala (zuidboog, -21,34/139,86) en passeert Cloncurry (1,2 km), Yurbi (0,3 km), Hughenden (1,5 km) en Charters Towers (0,8 km). Een gesplitste run via Yurbi (215,3 + 766,5 = 981,8 km) geeft dezelfde lijn (max afwijking 0,5 km) maar een 180°-omkering op de Yurbi-balloonlus; daarom één run.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mount Isa-smelter (ISASMELT) | Glencore | koperconcentraat (eigen + derden) → anode 99,7 %, zwavelzuur | ~200–250 kt anode/j (upgrade naar 250 kt); echte aanvoer lager sinds mijnsluiting H2 2025 | [2][4] |
| Copper Refineries, Stuart | Glencore | anode → kathode 99,995 % (LME grade A "ISA") + slijk met Ag/Au | tot 300 kt kathode/j | [1][2] |

## 6 · Stoppunt
De brief stopt bij de raffinaderij (verwerker → verwerker): Glencore zegt dat kathode en slijk via de haven van Townsville worden geëxporteerd [1], maar geen bron noemt kade, afnemer of bestemming — fase D/E vervallen.

## 7 · Open punten
- **Smelterstatus zwak:** Glencore (07-05-2026) meldt ~4 maanden stilstand "earlier in 2026" (record-regenseizoen, tekort aan regionaal concentraat); herstart niet bevestigd, rebrick RHF1 gestart, RHF2 later in 2026, ISASMELT vroeg 2027 [6]. Steunpakket tot A$600 mln over drie jaar (8-10-2025) houdt smelter en raffinaderij open tot ca. 2028 [7]. Lading dus nul tot onzeker; de weg is echt.
- **Spoor of weg niet gepubliceerd** ("rail and road" [1]); QUBE als wagenexploitant uit de ontwerpbron is niet bevestigd en staat daarom niet in de beennaam.
- **Lijn kwetsbaar:** ontsporing december 2025 sloot de Mount Isa-lijn tijdelijk [5]; dit tekenen we niet.
- **Raffinaderij niet object-bevestigd** (adres + z15, geen OSM-naam); het exacte losspoor/perron op het terrein is niet gezien (z15 volstaat, last mile 0,35 km < 2 km).
- **Kathode-afvoer** naar Townsville-haven en berth onbekend: niet getekend.
- **Overlap:** Yurbi → Stuart (≈766 km, 78 %) ligt op dezelfde rails als `zilver-cannington-townsville` b2; niet letterlijk kopieerbaar (ander eindpunt: haven Berth 11 versus raffinaderij), eigen run. Eigen content: smelter → Yurbi (215 km), verwerker → verwerker, product anode.
- **Km:** spoorkm uit de bron = "nearly 1,000 km" (Wikipedia) en "ongeveer 1.000 km" (Aurizon, uit het ontwerp, niet opnieuw geopend); gemeten 979,6 km = −2 % (binnen ±15 %).

## 8 · Bronnen
[1] Glencore Australia, "Copper refineries" (Townsville, 100 Hunter Street Stuart, tot 300 kt kathode/j, anodes "by rail and road", kathode via Port of Townsville). https://www.glencore.com.au/operations-and-projects/qld-metals/operations/copper-refineries
[2] NS Energy, "Mount Isa Copper Mines" (smelter 250 kt/j, 350 kg-anodes 99,7 %, raffinaderij 300 kt/j IsaKIDD). https://www.nsenergybusiness.com/projects/mount-isa-copper-mines/
[3] Wikipedia, "Great Northern Railway (Mt Isa line)" — "nearly 1,000 kilometres" Townsville–Mount Isa; 5,8 Mt vracht in 2010. https://en.wikipedia.org/wiki/Great_Northern_Railway_(Mt_Isa_line)
[4] Sitelaag `v2/design/koper-sitelaag.json`, `w-mount-isa-smelter` (OSM building "Copper Smelter", 250 kt) en Nominatim/OSM, "Hunter Street, Stuart" (-19.3421, 146.8523). https://nominatim.openstreetmap.org
[5] Argus, december 2025, "Derailment shuts Australian fertilizer, Cu line" (Glencore-lading, lijn tijdelijk dicht). https://www.argusmedia.com/en/news-and-insights/latest-market-news/2762920-derailment-closes-australian-fertilizer-and-copper-line
[6] Glencore Australia, 07-05-2026, "Work starts on Glencore's copper smelter rebrick in Mount Isa" (~4 maanden stil, concentraattekort). https://www.glencore.com.au/media-and-insights/news/work-starts-on-glencores-copper-smelter-rebrick-in-mount-isa
[7] Argus, 08-10-2025, "Australia agrees $395mn aid for Glencore Cu smelter" (A$600 mln, drie jaar, Mount Isa + Townsville). https://www.argusmedia.com/en/news-and-insights/latest-market-news/2739908-australia-agrees-395mn-aid-for-glencore-cu-smelter
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-koper-mountisa-townsville-smelter.png`, `sat-koper-mountisa-townsville-raffinaderij.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Recept:** `bash v2/tools/bak_stromen.sh koper-mountisa-townsville` (functie `bak_koper_mountisa_townsville`), uitvoer `v2/data/stroomroute-koper-mountisa-townsville.json` (33,9 KB, versie 2, lonlat).
- **b1 spoor** · trein Mount Isa-smelter → Copper Refineries Townsville (aannemelijk: Glencore zegt rail and road, Great Northern Railway, 1-op-1-net): **981,4 km** (1.716 punten) tegen "nearly 1,000 km" = -1,9 %. Doorgetrokken, geen stippel. Bron: de eerder gedraaide spoorrouter-run (`BAKE_SUFFIX=-raw`, 979,6 km routerkm; het json telt 981,4 km polyline, verschil is de ankerafstand).
- **Markers (2):** cu-mountisa-smelter (-20.7292, 139.4829; 0,18 km van de lijn), cu-townsville-raffinaderij (-19.3395, 146.8510; 0,35 km van de lijn).
- **Toets:** geen naden (één been), knikken 0, omkeringen 0, toets_rechte_benen geen treffer, json.load ok (versie 2, lonlat, modaliteit spoor, bestand 33,9 KB).
- **Geen** via-punten, zeebeen, haven-aanloop, stippel, kopie of vlucht; stoppunt bij de raffinaderij.
- **Lessen:** een gesplitste run via Yurbi gaf een 180-graden-omkering op de ballonlus, dus één directe run; de lading kan nul zijn (smelter 2026 ~4 maanden stil), de weg is echt. Overlap 78 % met zilver-cannington-townsville b2 is bewust een eigen run.
