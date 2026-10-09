# Routebrief (licht) · gas — Kipoi (Griekenland) → Melendugno (Italië) — Trans Adriatic Pipeline

**stroom-id:** `gas-kipoi-melendugno` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) ·
**status:** gebakken
**Keten in één zin:** Azerbeidzjaans Shah Deniz-gas komt via TANAP bij het Grieks-Turkse grensstation Kipoi (Evros) de Trans Adriatic
Pipeline in en gaat in één doorlopende leiding (Griekenland, Albanië, Adriatische Zee, Italië) naar de Pipeline Receiving Terminal
Melendugno (San Foca, Lecce), waar het Italiaanse gasnet (Snam) overneemt — de laatste schakel van de Zuidelijke Gascorridor.
**Welke as van het verhaal:** Zuidelijke Gascorridor naar Zuid-Europa — 10 bcm/j capaciteit (+1,2 bcm/j sinds 2026) [1][2];
TAP leverde t/m juli 2026 meer dan 60 bcm aan Europa, waarvan 50 bcm aan Italië [2][3]. Het VK/Noorwegen-verhaal (Langeled) heeft hier een
Azerbeidzjaans tegenstuk. Stroomopwaarts (Shah Deniz, SCP, TANAP) is bewust niet getekend (zie §6).

## 1 · Ketenkaart
```
TANAP (niet getekend, aansluiting op Kipoi) ──► Kipoi-grensstation `gas-kipoi-grens`
   ──(b1 leiding · TAP: Griekenland ~554 km → Albanië ~201 km → Adriatische Zee 103 km → Italië ~9 km · 868,1 km OSM)──►
Melendugno PRT `gas-melendugno-prt` — stoppunt (invoeding Snam-net via ~60 km interconnector, niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | leiding | `gas-kipoi-grens` → `gas-melendugno-prt` | Trans Adriatic Pipeline (TAP AG): Evros–Thessaloniki–Kozani–Florina (GR) · Korçë–Fier–Seman (AL) · 103 km zee (max 810 m diep) · San Foca (IT) | 878 gepubliceerd [1] → OSM 868,1 (−1,1%) | OSM-ways `man_made=pipeline`, operator=Trans Adriatic Pipeline AG, substance=gas: 36 ways, exact aaneengesloten (alle naden 0,0 m), gestikt tot één lijn (3.090 punten) | nee |

Landverdeling gemeten op de lijn (indicatief, grens op lon ≈ 20,97): Griekenland ~554 km (gepubliceerd 550), Albanië tot de kust ~201 (215 incl. de
zee-aanlanding), zee 103,4 (105), Italië 8,9 (8). Beennaam voor de bake: *Trans Adriatic Pipeline Kipoi naar Melendugno (Griekenland, Albanië,
Adriatische Zee, Italië; offshore-geometrie indicatief)*. De zeelijn (way 849720568, `location=underwater`) draagt in OSM `source:geometry=aproximate`:
zeker is de aanlanding aan beide kusten, de lijn ertussen is een benadering — gemeten OSM-geometrie, dus doorgetrokken, geen landtoets.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-kipoi-grens` | leiding-kop / grensstation (aansluiting TANAP) | TAP-station Kipoi, Evros, tegen de Grieks-Turkse grens | 40.9702, 26.3093 | [1][4][5] | bron-gelegd (z15 gezien: omheind rechthoekig industrieterrein met installaties, opritten en bredere perimeterweg in landbouwgebied; het punt ligt binnen het terrein; dorp Kipoi ~2 km ZO) |
| `gas-melendugno-prt` | receptieterminal (staart, stoppunt) | TAP Pipeline Receiving Terminal Melendugno (San Foca), Lecce | 40.2754, 18.3138 | [1][4][6] | bron-gelegd (z15 gezien: kaal grindplatform met installaties/gebouwen in olijfgaarden, ~3,5 km ZO van Melendugno-stad; het punt ligt op de westrand van het platform) |

Hergebruik: geen — `gas-sitelaag.json` en eerdere brieven kennen Kipoi/Melendugno niet; beide ankers zijn de OSM-leidinguiteinden, op het terrein bevestigd (kop 0,00 km, staart 0,00 km van de lijn, geen last-mile nodig).
Beelden: `v2/build-cache/satcheck/sat-gas-kipoi-melendugno-kipoi.png`, `sat-gas-kipoi-melendugno-prt.png` [7].

## 4 · Via-punten
Niet van toepassing: één leidingbeen uit aaneengestikte OSM-ways (geen corridorkeuze zoals bij weg/spoor).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kipoi-station | TAP AG (BP 20%, SOCAR 20%, Snam 20%, Fluxys 20%, Enagás 20%) | TANAP-gas → TAP | onderdeel van 10 (+1,2) bcm/j | [1] |
| Melendugno PRT | TAP AG; interconnector naar Snam Rete Gas | TAP-gas → Italiaans net (~60 km naar Brindisi-omgeving) | 10 bcm/j; 2020–jul 2026: 50 bcm naar Italië, rest (60 min 50, eigen rekensom) naar overige Europese afnemers | [1][2][3] |

## 6 · Stoppunt
De brief stopt bij de PRT Melendugno: het Italiaanse invoedingspunt, waarna het gas anoniem Snam-netgas is. Upstream is niet getekend: TANAP
staat in OSM maar voor ~408 km van ~1.850 km, de South Caucasus Pipeline (Sangachal → Georgië) ontbreekt in de lokale Azerbeidzjan-/Georgië-extracts, en
Shah Deniz is offshore — een keten die vooraan grotendeels stippel zou zijn is niet gewenst (golf 4-les). Het begin is dus Kipoi, niet de Kaspische Zee.

## 7 · Open punten
- **Offshore-lijn indicatief:** OSM markeert de 103 km Adriatische-zeelijn als `aproximate`; aanlandingen (40.7937, 19.3728 en 40.3109, 18.3926) zijn de vaste punten.
- **Geen kalenderjaar-volume:** TAP publiceert cumulatieve mijlpalen (50 bcm Europa sep 2025 [3]; >52 bcm eind 2025 [8]; >60 bcm incl. 50 bcm Italië jul 2026 [2]). Gemiddeld ~10,4 bcm/j sinds eind 2020 is mijn eigen rekensom, geen gepubliceerde doorzet; 10 bcm/j is capaciteit.
- **Herkomst:** het gas is Shah Deniz (Azerbeidzjan) via TANAP, maar TAP-flow is in het net fungibel; geen aparte bron voor de molecuul-herkomst per jaar.
- **Interconnector naar Snam** (~60 km, Melendugno → Brindisi) en het Albanese deelplatform zijn niet getekend; alleen de TAP-leiding zelf.
- **Sitelaag mist Kipoi en Melendugno** — centrale aanvulling nodig voor de gloed (gewicht 10 bcm/j capaciteit).
- Albanië-extract ontbreekt lokaal (`albanie-latest.osm.pbf`): de bake gebruikt het vooraf gestikte geojson (zie §9), geen pyosmium-scan.

## 8 · Bronnen
[1] Wikipedia (EN), "Trans Adriatic Pipeline" — 878 km (550 GR / 215 AL / 105 offshore / 8 IT), start Kipoi bij TANAP, aanlanding San Foca, 10 bcm/j, +1,2 bcm/j, aandeelhouders. https://en.wikipedia.org/wiki/Trans_Adriatic_Pipeline
[2] TAP AG, nieuws 10-07-2026, "One flow, two milestones" — >60 bcm naar Europa, waarvan 50 bcm naar Italië. https://www.tap-ag.com/news/news-stories/one-flow-two-milestones-60-bcm-delivered-to-europe-50-bcm-to-italy
[3] World Pipelines, 01-09-2025, "TAP delivers 50 billion cubic metres of natural gas to Europe" — 50 bcm; eerste capaciteitsuitbreiding +1,2 bcm/j vanaf begin 2026. https://www.worldpipelines.com/project-news/01092025/tap-delivers-50-billion-cubic-metres-of-natural-gas-to-europe
[4] OpenStreetMap-bijdragers (ODbL), via api.openstreetmap.org (2026-10-09) — 36 ways (operator Trans Adriatic Pipeline AG, substance=gas), o.a. 1040219169 (Kipoi-kant), 849720568 (offshore, underwater), 849720566 (Italië). https://www.openstreetmap.org/way/849720568
[5] TAP AG, website — Greece-sectie, grensstation/compressor bij Kipoi. https://www.tap-ag.com
[6] Wikipedia (EN) [1] — gas terminal in olijfgaard bij Melendugno, aansluiting Snam bij Brindisi.
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15, live, 2026-10-09).
[8] TAP AG, "TAP marks five years of safe and reliable operations" — >52 bcm naar Europa. https://www.tap-ag.com/news/news-stories/tap-marks-five-years-of-safe-and-reliable-operations
[9] Trend.az, 10-07-2026, "TAP gas supply to Europe reaches 60 bcm". https://www.trend.az/business/energy/4205809.html

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Bestand:** `v2/data/stroomroute-gas-kipoi-melendugno.json` — versie 2, punt_formaat lonlat, 1 been, 3.090 punten, 868,1 km, 2 markers, 60,3 KB.
**Recept:** `bak_gas_kipoi_melendugno()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh gas-kipoi-melendugno`). Geen profiel in `maak_stroombeen_weg.py` (geen weg), geen extract, geen pyosmium.

| # | modaliteit | km | punten | stippel | naad | beschrijving |
|---|---|---|---|---|---|---|
| 1 | leiding | 868,1 | 3.090 | nee (doorgetrokken) | start | Trans Adriatic Pipeline Kipoi naar Melendugno (Griekenland, Albanie, Adriatische Zee, Italie; offshore-geometrie indicatief) |

- **Km-toets:** gemeten 868,1 tegen gepubliceerd 878 (550 GR + 215 AL + 105 zee + 8 IT) = **-1,1%**, ruim binnen ±15%. Totaal 868,1 km.
- **Naden:** één been, dus geen naden. Grootste segment 17,6 km = de offshore-leiding (OSM-vertexafstand, geen gat); `toets_rechte_benen` meldt niets voor deze stroom.
- **Markers:** `gas-kipoi-grens` 0,001 km en `gas-melendugno-prt` 0,006 km van de lijn (norm ≤ ~0,5 km). Beide ankers = de OSM-leidinguiteinden, dus geen last-mile en geen stippel.
- **Toets knikken:** 95 knikken ≥ 60 graden maar **0 omkeringen** en 0 terugloop. De knikken liggen in de OSM-vertexgeometrie van de leiding (o.a. Griekenland-West en Albanië, spikes van 12-70 m radius op enkele vertices); een leiding kan niet 'omkeren' en de gestikte ways sluiten exact aan, dus geen route-fout en niet gerepareerd (leidinggeometrie is gemeten OSM).
- **Doorgetrokken, geen stippel:** de leiding is gemeten OSM-geometrie van kop tot staart; de offshore-lijn (way 849720568, 103,4 km, `location=underwater`) is `source:geometry=aproximate` en staat dus als "indicatief" in de beennaam, niet in de lijnstijl. Geen haven-aanloop, geen zeebeen, geen via-punten, geen gedeeld been.
- **Geojson-vorm:** de vooraf gestikte LineString stond als kale `Feature`; `hecht_marnet.py` (`_spoor_been`) leest alleen een `FeatureCollection` (`KeyError: 'features'`). Het eigen tussenbestand is zonder geometriewijziging (3.090 punten, ongewijzigde coördinaten) in een `FeatureCollection` gewikkeld.
- **Les:** een gestikt OSM-leidingbeen als `--been-geojson` moet een `FeatureCollection` zijn; de eenvoudigste keten (één doorlopende OSM-leiding, twee ankers op de leidinguiteinden) bakt in één run zonder extracts, slots voor weg of aanloop.
- **Registerregel (centraal):** `{"sleutel":"gas-ki","bestand":"stroomroute-gas-kipoi-melendugno.json","grondstof":"gas","label":"Kipoi → Melendugno","aan":true,"noot":"M31 · golf 7 (2026-10-09): Shah Deniz-gas via TANAP bij Kipoi de TAP in, 868 km OSM-leiding door Griekenland, Albanië, de Adriatische Zee en Italië naar de PRT Melendugno"}`.
- **Centraal nog te doen:** sitelaag Kipoi en Melendugno (gewicht 10 bcm/j capaciteit), register, bundel, `BUNDEL_VERSIE`, `?v=`.
