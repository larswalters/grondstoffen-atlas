# Routebrief (licht) · Olie · Pasadena (Houston) → Colonial Pipeline → Linden (VS)

**stroom-id:** `olie-pasadena-linden` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 12) · **status:** gebakken
**Keten in één zin:** Geraffineerde brandstoffen (benzine op Line 1, distillaat op de parallelle lijn) van de Colonial-kop bij Pasadena aan de Houston Ship Channel per **leiding** (Colonial Pipeline, hoofdlijn, 12 staten) naar het Linden Junction-tankpark in New Jersey, de poort naar New York Harbor. **Raffinaat, geen ruwe olie.**
**Welke as van het verhaal:** *de grootste raffinaatader van de VS* — Colonial: ca. 100 mln US-gallon/dag = ca. 2.380 kb/d [1][2], capaciteit tot 3.000 kb/d [1] (peiljaar 2025 [2]; Wikipedia geeft geen peiljaar [1]). Aanvulling op de ruwe-olie-assen: dit is wat uit de Golfkust-raffinaderijen komt. Eén been, geen stippel.

## 1 · Ketenkaart
```
Pasadena-kop `ol-pasadena-kop` (tankpark Houston Ship Channel)
 ──(b1 leiding · Colonial hoofdlijn: Line 1 benzine tot Greensboro, daarna noordelijke hoofdlijn ·
     TX-LA-MS-AL-GA-SC-NC-VA-MD-DE-PA-NJ · 2.455 km OSM, hemelsbreed 2.245 km)──►
Linden Junction `ol-linden-eind` (tankpark naast NJ Turnpike) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | Pasadena-kop → Linden-eind | Colonial Pipeline Line 1 (benzine) + onbenoemde Colonial-ways; zie §4 voor wat wordt uitgesloten | OSM-pad 2.455,4 km (eigen pyosmium-meting, 12 Geofabrik-extracts); **geen gepubliceerde trunklengte**: Wikipedia geeft alleen het systeem (8.850 km met zijtakken) [1]; hemelsbreed 2.245 km, verhouding 1,09; de ±15%-toets is indicatief | OSM-way (`man_made=pipeline`, `operator=Colonial Pipeline`, `substance=fuel`), gestikt op way-id | nee — 15 naden, grootste 0,071 km |

Beennaam voor de bak: `Colonial Pipeline hoofdlijn Pasadena → Linden (Line 1 benzine, raffinaat; OSM-gestikt)`.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-pasadena-kop` | kop van de leiding / tankpark | Colonial-kop Pasadena TX (Houston Ship Channel) | 29.7203, -95.1799 | [3][4][6] | bron-gelegd (z15 gezien: tankpark met ronde en bolvormige tanks direct ten zuiden van een oost-west pijp-/spoorcorridor, raffinaderij- en terminalindustrie aan het kanaal rondom; OSM-pijpleidingbegin ligt 6 m van dit punt) |
| `ol-linden-eind` | eind van de leiding / afleverpunt NY Harbor | Linden Junction-tankpark NJ | 40.5768, -74.2492 | [1][3][6] | bron-gelegd (z15 gezien: tankpark van ca. 25 ronde tanks aan de oostrand langs de NJ Turnpike, magazijnen noordelijk, een tweede groter tankpark/terminal 2,5 km zuidoost aan de Arthur Kill; OSM-eind ligt 0,5 m van dit punt) |

Beide ankers zijn OSM-eindpunten van de leiding zelf; geen last-mile-been nodig. Beelden: `v2/build-cache/satcheck/sat-olie-pasadena-linden-pasadena.png` en `…-linden.png`.

## 4 · Via-punten en uitgesloten ways (leiding: geen corridorkeuze, wel een strangkeuze)
Een leiding volgt een vaste buis; het risico is het stikken van de verkeerde parallelle lijn. Regel voor de bak: **neem alle ways met `man_made=pipeline` en `operator` ~ "Colonial Pipeline"** en sluit uit (naam bevat): `Line 2`, `Line #2`, `2PA`, `1PA`, `Loop`, `Augusta`, `Roanoke`, `Atlanta`, `Albany`, `Zachary`, `Pasadena to`, `Lateral`, `LSMB`, `out of service`, `Line 8`, `Line 9`, `Line 15…`, `Line 16…`, plus onbenoemde ways met `substance=oil`. "Main Line" mag erbij (zelfde 2.455,4 km). Kortste pad Pasadena → Linden over de rest = zuivere strang.
Controlepunten op het stikpad (geen via-punten; alleen om een verkeerde strang te herkennen; km = afstand langs het pad):
| km | plaats | lat, lon |
|---|---|---|
| 167 | Louisiana-grens (Sabine) | 30.0570, -93.6861 |
| 615 | Collins MS | 31.6273, -89.5429 |
| 1.193 | Atlanta-noord | 33.9564, -84.2858 |
| 1.691 | Greensboro-knoop (Line 1 eindigt hier [4][5]) | 36.1400, -79.8580 |
| 2.142 | Maryland, bij Frederick | 39.3637, -77.0339 |
| 2.293 | Delaware/Pennsylvania-grens | 39.8408, -75.5380 |

Voorwerk: `v2/build-cache/ais/graaf/olie-pasadena-linden-colonial-voorwerk.geojson` (gestikt pad, 6.939 punten, 58 way-id's in de feature-properties; niet het eindproduct).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Pasadena-kop (injectiepunt Line 1) | Colonial Pipeline Company (Brookfield-overname 2025) | raffinaat uit Golfkust-raffinaderijen → leiding | systeem tot 3.000 kb/d | [1][2][4] |
| Linden Junction + Intra-Harbor Transfer | Colonial Pipeline Company | leiding → tankpark → barge naar NY Harbor | niet gebronded | [1] |

## 6 · Stoppunt
Linden Junction: daar eindigt de leiding en begint de verdeling per barge in de haven. Geen bron noemt één raffinaderij of afnemer voor deze lading, dus D/E vervallen. Onderweg gaat raffinaat naar ca. 270 terminals; die zijtakken tekenen we niet.

## 7 · Open punten
- **Rol: raffinaat.** Het product is benzine/distillaat, niet ruwe olie; nieuwe rol binnen de olie-grondstof, benoemd in beennaam en brief.
- **Noordelijk deel is "aannemelijk: één bron".** Line 1 loopt volgens EIA en Colonial alleen Houston → Greensboro [4][5]; ten noorden daarvan zijn de OSM-ways onbenoemd (twee parallelle hoofdlijnen). Het stikpad kan daar elke van beide kiezen; ze liggen in dezelfde corridor, het km-verschil is te verwaarlozen.
- **Geen gepubliceerde trunklengte** voor Houston → Linden gevonden; alleen systeem 8.850 km [1]. Het OSM-pad is een meting zonder externe ijk.
- **Volume zonder peiljaar bij Wikipedia:** 100 mln gallon/dag staat volgens de overnameberichten van 2025 op de site van Colonial [2]; of de overname gesloten is, is niet bevestigd [2].
- Pennsylvania heeft in OSM slechts 165 km Colonial (4 ways) en Delaware 125 km: het stikpad loopt er zonder gat, maar controleer de naden bij het bakken.
- colpipe.com is vanuit deze sessie geblokkeerd (403): geen aflevermatrix of tarieven.

## 8 · Bronnen
[1] Wikipedia, "Colonial Pipeline" — 5.500 mi (8.850 km), Houston → Port of New York and New Jersey, 3 mb/d capaciteit, ca. 1×10^8 gallon/dag, hoofdlijnen 40" en 36", Linden Junction 1964. https://en.wikipedia.org/wiki/Colonial_Pipeline
[2] Overnameberichten Brookfield/Shell, april 2025 (o.a. Gas Processing News) — Brookfield koopt Colonial Enterprises voor ca. 9 mld USD; 100 mln gallon/dag volgens de website van Colonial. https://gasprocessingnews.com/news/2025/04/brookfield-to-acquire-colonial-pipeline-in-9-b-deal-including-debt/
[3] OpenStreetMap (ODbL), Geofabrik-extracts us-texas, -louisiana, -mississippi, -alabama, -georgia, -south-carolina, -north-carolina, -virginia, -maryland, -delaware, -pennsylvania, -new-jersey; eigen pyosmium-scan 2026-10-29 op `man_made=pipeline` + naam/operator Colonial, Dijkstra op way-id. https://www.openstreetmap.org
[4] Colonial Pipeline Company, "Colonial Pipeline 101" (via zoekresultaat; pagina zelf 403) — Line 1 injectie Pasadena, 18–21 dagen naar Linden, Line 1 Houston → Greensboro. https://www.colpipe.com/news/in-the-news/colonial-pipeline-101-know-colonial
[5] EIA, Today in Energy, 8-11-2016 — Line 1 ca. 1,4 mb/d benzine van de Golfkust naar Greensboro NC; voorbij Greensboro andere delen naar MD en NJ, eind Linden. https://www.eia.gov/Todayinenergy/detail.php?id=28692
[6] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `sat-olie-pasadena-linden-pasadena.png`, `sat-olie-pasadena-linden-linden.png`.
[7] Haalbaarheidstoets golf 12 (orkestrator): Line 1 + onbenoemde ways geeft 2.455,4 km; zelf nagerekend 2.455,4 km met 15 naden (zonder "Main Line"), grootste 0,071 km.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 12)

**Stroom `olie-pasadena-linden`** -> `v2/data/stroomroute-olie-pasadena-linden.json` (141,5 KB, versie 2, lonlat) — 1 been, **2.455,4 km**, 6.939 punten, 2 markers, 0 stippel. Recept: `bash v2/tools/bak_stromen.sh olie-pasadena-linden` (functie `bak_olie_pasadena_linden`; geen profiel in `maak_stroombeen_weg.py`, geen router, geen zee, geen haven-aanloop, geen vlucht, geen kopie).

| # | modaliteit | been | km | punten | stippel | naad |
|---|---|---|---|---|---|---|
| 1 | leiding | Colonial Pipeline hoofdlijn Pasadena -> Linden (Line 1 benzine, raffinaat; OSM-gestikt, noordelijk deel aannemelijk: één bron) | 2.455,4 | 6.939 | nee | — (enig been) |

**Markers (beide uit §3):** `ol-pasadena-kop` 29.7203,-95.1799 (0,006 km van de lijn) · `ol-linden-eind` 40.5768,-74.2492 (0,001 km).

**Toets.** Geen gepubliceerde trunklengte, dus de +-15%-toets is alleen indicatief: 2.455,4 km tegen hemelsbreed 2.245 km (verhouding 1,09; geen wegkm). Alle zes controlepunten uit §4 liggen op 0,00-0,01 km van het pad op de verwachte km-stand (167 / 615 / 1.193 / 1.691 / 2.142 / 2.293), dus geen verkeerde strang. Geen naden tussen benen. `toets_knikken`: 81 knikken, 1 omkering (177,9 gr bij 40.5769,-74.2496 = het lijneinde bij het tankpark, echt), 0 terugloop. Geen recht been. json.load ok, versie 2, lonlat, modaliteit alleen leiding, 141,5 KB.

**Toelichting.**
- *Nieuw tool* `v2/tools/maak_leidingbeen_olie_pasadena_linden.py` (patroon `maak_leidingbeen_keystone.py`; pyosmium draaide hier wél): per extract een cache `olie-pasadena-linden-colonialways-<extract>.json` met alle pipeline-ways waarvan name/operator/owner "colonial" bevat (313 unieke ways over 12 extracts, 255 na uitsluiting), ontdubbeld op way-id, nodes op 5 decimalen, naden < 0,15 km, Dijkstra tussen de knopen bij kop (5,9 m) en eind (0,8 m). Eerste scan van alle 12 extracts incl. Texas duurde ruim onder een minuut.
- *Uitsluiting op naam:* Line 2, Line #2, 2PA, 1PA, Loop, Augusta, Roanoke, Atlanta, Albany, Zachary, Pasadena to, Lateral, LSMB, out of service, Line 8, Line 9, Line 15xx, Line 16xx en "Main Line", plus onbenoemde ways met substance=oil. Met "Main Line" erbij komt hetzelfde pad (2.455,4 km) met 17 naden en 7 Main Line-ways; zonder 15 naden, 6.939 punten, 58 way-id's, grootste naad 0,072 km (voorwerk-maat). Gekozen: zonder, want identiek aan het voorwerk.
- *Naden:* 15 stuks, grootste 0,072 km; verder alle benen op gedeelde OSM-nodes. Pennsylvania (4 ways) en Delaware (2 ways) lopen zonder gat.
- *Geen stippel, geen via-punten* (een leiding volgt een vaste buis; het risico is de verkeerde parallelle strang, afgedekt met de controlepunten).
- *Noordelijk deel boven Greensboro is "aannemelijk: één bron"* (onbenoemde ways, twee parallelle hoofdlijnen): staat in de beennaam, niet in de lijnstijl.

**Lessen.**
- Een parallelle strang kiest het kortste pad zelf; de controlepunten op km-stand (§4) zijn de goedkope toets op de goede strang, en ze komen op 0,00-0,01 km uit.
- `bash v2/tools/bak_stromen.sh` leest het bestand tijdens het draaien: een gelijktijdige edit van een andere agent gaf na afloop van mijn bake een leesfout ("er/smelter: No such file", regel ~12112, functie bak_koper_quellaveco_ilo); de eigen output was al geschreven en gecontroleerd.

**Meldingen aan de eigenaar (niet door deze bake aangepast).** Sitelaag olie mist Pasadena-kop en Linden Junction als raffinaat-knopen; Linden-eind valt 2,5 km van een groter tankpark aan de Arthur Kill (zie §3). Registerregel (centraal): sleutel `olie-pl`.
