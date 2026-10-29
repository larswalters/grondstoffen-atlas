# Routebrief (licht) · koper — Toromocho → Ferrocarril Central Andino → Callao (Peru)

**stroom-id:** `koper-toromocho-callao` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** koperconcentraat van de Toromocho-concentrator (Minera Chinalco Perú, Morococha/Yauli, Junín, 4.500 m) gaat per **spoor** (Ferrocarril Central Andino: zijlijn naar Ticlio, de Galera-tunnel, Rímac-vallei, Chosica, Lima) naar Callao, waar een transportband het naar de mineraalterminal van Transportadora Callao brengt; de lijn stopt op die kade (stoppunt: geen afnemer gebrond).
**Welke as van het verhaal:** *Hoogste spoorlijn ter wereld als erts-exportader* — Centraal-Andes-concentraat naar de Pacifische kust (Chinalco, China is de genoemde bestemming). Jaarvolume: **182 kt Cu per jaar in 2015** (763,5 kt concentraat met 182.288 t Cu [3]); ontwerp 210 kt Cu/jaar [5], uitbreiding naar 300 kt/jaar was het doel voor 2020 [3]. Recent productiecijfer niet gevonden.

## 1 · Ketenkaart
```
Toromocho-concentrator `cu-toromocho-conc` ──(b1 spoor · FCCA zijlijn → Ticlio → Galera-tunnel → Rímac-vallei → Lima · router 178,1 km)──►
FCCA-emplacement Callao ──(b2 stippel · transportband · 0,48 km)──► Transportadora Callao-mineraalterminal `cu-callao-tcsa` ── stoppunt (geen zeebeen)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `cu-toromocho-conc` → FCCA-emplacement Callao (-12.0503, -77.1402) | Ferrocarril Central Andino: zijlijn plant–Ticlio, Galera-tunnel, Casapalca, San Mateo, Matucana, Chosica, Lima Desamparados, Callao [6][7] | router **178,1**; gepubliceerd Callao–Ticlio **171** [7] + zijlijn ~14 (router, geen bron) = ~185 → −3,7% | toets_spoorroute (BAKE_SUFFIX=-raw, hoofd-km 100) | nee |
| b2 | A | leiding (transportband) | FCCA-emplacement → `cu-callao-tcsa` | faja hermética tubular, 2.000 t/uur [2] | 0,48 (gemeten tussen twee ankers) | stippel (eigen verbinding zonder net) | **ja**: terrein, geen net |

Geen zeebeen (bindend, haalbaarheidstoets): ProActivo noemt alleen "China", geen smelter of haven; Ningbo zou verzonnen zijn [1]. Geen haven-aanloop (geen zeebeen; de TCSA-kade ligt 60,7 km van MARNET-zeeknoop 394, relevant bij een latere zee-uitbreiding). Het stuk plant → spoor (snap 0,26 km) is te kort voor een eigen stippel.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-toromocho-conc` | mijn / laadplek (kop b1) | Toromocho-concentrator, Minera Chinalco Perú | -11.6691, -76.1450 | [3][4][5] | **aannemelijk** (z15 gezien: complex van blauwgedakte hallen en verdikkertanks tegen de tailingsdam, aan de haulroad uit de put 5 km noordelijker; geen bron geeft deze coördinaat; het Wikipedia-mijnpunt -11.6197/-76.1407 ligt in de put — `sat-koper-toromocho-callao-cu-conc2-z14.png`, `-cu-conc3-z15.png`) |
| `cu-callao-tcsa` | overslag / kade (staart b2, stoppunt) | Transportadora Callao, mineraalterminal (muelle centro), Callao | -12.0499, -77.1446 | [2][8][9] | **bron-gelegd**, letterlijk hergebruikt uit `zilver-uchucchacua-callao.md` / `zilver-caylloma-callao.md` (z15 hier: bulkcarriers aan de kade tussen twee containerterminals, havenemplacement oostwaarts — `sat-koper-toromocho-callao-cu-callao-z15.png`) |

Geen ander anker bestond al voor deze plant (sitelaag `koper-sitelaag.json` kent Toromocho niet: kandidaat-site `w-toromocho` op bovenstaand punt, 182 kt Cu/jaar [3], centraal toe te voegen).

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Geen. Er bestaat één spoorverbinding tussen Ticlio en Callao (Rímac-vallei), dus geen corridorkeuze; de vrije Dijkstra vindt hem zonder via-punten (snap kop 0,26 km, staart 0,48 km). De 12 bochten ≥60° (6 omkeringen) zijn de echte zigzags van de Ticlio-lijn (Casapalca–San Mateo-flank), geen foutvia: `toets_knikken` zal ze melden. Router passeert Ticlio-station op 0,95 km (km 14 van b1), Casapalca 0,4 km, Matucana 0,1 km, Chosica 0,2 km, Lima Desamparados 0,3 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Toromocho-concentrator | Minera Chinalco Perú (Chinalco) | erts → Cu-(+Mo-)concentraat | 117.200 t erts/dag, uitbreiding naar 170.000; 2015: 763,5 kt concentraat | [3][4] |
| Transportadora Callao-mineraalterminal | Consorcio Transportadora Callao (Chinalco is lid) | concentraat → scheepslading (gesloten band 2.000 t/uur) | niet gebrond | [2][8] |

## 6 · Stoppunt
De brief stopt op de Callao-kade: ProActivo noemt alleen "China" als bestemming, zonder smelter of haven [1], dus fase B–E vervallen en de lijn eindigt waar het bewijs eindigt.

## 7 · Open punten
- **Zijlijn plant–Ticlio:** en-Wikipedia zegt dat de Ticlio–Morococha-tak "since closed to traffic" is [6]; OSM heeft 14 km spoor van de plant naar Ticlio. Of Chinalco/FCCA hem heropend heeft (er is een spoorverlenging binnen de plant gepland [4]) is niet bevestigd: kop b1 is aannemelijk. Het in de ontwerpfase genoemde "Galera-aansluitpunt" (-11.6203, -76.1842) is dus alleen de railhead als de tak dicht is (dan een stippel van ~4,7 km tussen put en dat punt) — niet gevonden in een bron.
- **FCCA-contract:** een 15-jarig contract voor concentraatvervoer naar Callao (± US$10 mln) kwam alleen uit een zoeksamenvatting van proactivo.com.pe/upr.info; de pagina zelf niet teruggevonden. Wel bevestigd: de band loopt van FCCA-installaties naar de Callao-terminal [2], en NS Energy: concentraat gaat van FCCA naar de haven [3].
- **Terminalnaam:** ProActivo (2013) noemt een "muelle norte"-terminal van Consorcio Transportadora Callao [2]; Wikipedia en de zilverbrieven plaatsen TCSA op het "muelle centro". Eerste ladingen (2014) gingen via Muelle 5 (APM) [1]. Het anker is TCSA; welk muelle Toromocho nu gebruikt is niet bevestigd.
- **Concentrator-coördinaat:** alleen satelliet-gezien (aannemelijk), geen bron met punt.
- **Volume:** 2015 is elf jaar oud; uitbreiding 2024 (170.000 t/dag) niet in een productiecijfer terug te vinden; ontwerp 210 kt is geen productie. Aandeel van het concentraat per spoor tegenover truck niet gekwantificeerd.
- **Afnemer:** China (generiek) — geen zeebeen getekend.

## 8 · Bronnen
[1] ProActivo, "Exportaciones de Toromocho se iniciarán a mediados del 2014" (2013-12-09): concentrator Morococha, bestemming China, eerste lading Muelle 5 APM, mineralenpier Consorcio Transportadora Callao Q1 2014, 170 kt/jaar. https://proactivo.com.pe/exportaciones-de-toromocho-se-iniciaran-a-mediados-del-2014/
[2] ProActivo, "Toromocho arranca a fines del 2013": terminal de embarque in het muelle norte van Callao, hermetische bandsysteem van de FCCA-installaties naar de haven, 2.000 t/uur, Chinalco via Consorcio Transportadora Callao. https://proactivo.com.pe/toromocho-arranca-a-fines-del-2013/
[3] NS Energy Business, Toromocho-projectpagina: concentraat van Ferrovías Central Andina naar de haven van Callao; 2015: 763.500 t concentraat, 182.288 t Cu; 117.000 t/dag; uitbreiding naar ~300 kt Cu (2020). https://www.nsenergybusiness.com/?p=216348
[4] Energiminas, "Toromocho: Senace aprueba inversión de US$119,9 millones de Chinalco" (2023-02-07): uitbreiding van de spoorlijn binnen de plant; districten Morococha en Yauli. https://energiminas.com/toromocho-senace-aprueba-inversion-de-us119-9-millones-de-chinalco/
[5] Wikipedia (EN), "Mount Toromocho": ~140 km ten oosten van Lima, de Central Railroad passeert; Chinalco; 210.000 t Cu/jaar ontwerp. https://en.wikipedia.org/wiki/Mount_Toromocho
[6] Wikipedia (EN), "Ferrocarril Central Andino": route Callao–Lima–Galera-tunnel–La Oroya; tak Ticlio–Morococha (1923) later gesloten; minerale vracht. https://en.wikipedia.org/wiki/Ferrocarril_Central_Andino
[7] Wikipedia (EN), "Ticlio": Ticlio Station op km 171 van de FCCA (normaalspoor 1.435 mm). https://en.wikipedia.org/wiki/Ticlio
[8] `v2/design/routebrieven/zilver-uchucchacua-callao.md`: anker `ag-callao-tcsa` (z18), Wikipedia "Port of Callao", PortalPortuario, Rumbo Minero.
[9] `v2/design/routebrieven/zilver-caylloma-callao.md`: TCSA-kade 60,7 km van MARNET-zeeknoop 394.
[10] OpenStreetMap (ODbL) via Overpass 2026-10-29: FCCA-sporen (`railway=rail`, `operator=Ferrocarril Central Andino S.A.`, normaalspoor) rond Ticlio/Morococha; router `v2/tools/toets_spoorroute.mjs` (1-op-1-net) 178,1 km.
[11] Esri World Imagery via `v2/tools/sat_check.py`, 2026-10-29: `v2/build-cache/satcheck/sat-koper-toromocho-callao-cu-overzicht-z13.png`, `-cu-conc-z14.png`, `-cu-conc2-z14.png`, `-cu-conc3-z15.png`, `-cu-yard-z15.png`, `-cu-callao-z15.png`.
[12] Haalbaarheidstoets M31 golf 13 (workflow-invoer) en v1 `design/koper.md` (Peru: Toromocho genoemd); `data/copper.js` bevat geen Toromocho-record.

## 9 · Bak-noot (voor de bak-agent)

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
**Functie:** `bak_koper_toromocho_callao()` in `v2/tools/bak_stromen.sh`; `bash v2/tools/bak_stromen.sh koper-toromocho-callao` → `v2/data/stroomroute-koper-toromocho-callao.json` (19,3 KB, contract versie 2, lonlat). Titel: Koper · Toromocho → Callao (Peru). Geen profiel in `maak_stroombeen_weg.py`, geen zeebeen, geen haven-aanloop, geen via-punten.

| # | modaliteit | km | punten | naad | beschrijving |
|---|---|---|---|---|---|
| 1 | spoor | 179,1 | 937 | – | trein Toromocho-concentrator naar Callao (FCCA via Ticlio en Galera-tunnel; aannemelijk: zijlijn plant-Ticlio mogelijk gesloten) |
| 2 | leiding (stippel) | 0,5 | 2 | 0,00 | transportband FCCA-terrein naar TCSA-mineraalterminal (faja tubular, schematisch, geen net) |

Totaal 179,6 km, 2 markers (Toromocho-concentrator, aannemelijk; TCSA-terminal, stoppunt). Markerafstand tot de lijn: concentrator 0,26 km (spoorsnap kop), TCSA 0,0 km.

**Recept b1:** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=-11.6691,-76.1450 --naar=-12.0499,-77.1446 --naam=koper-toromocho-callao-toromocho-callao --hoofd-km=100` (1-op-1-net, extract peru) → `spoorroute-koper-toromocho-callao-toromocho-callao.geojson` (FeatureCollection, eindpunt -12.0503,-77.1402), als `--been-geojson "spoor|…"`. Het geojson stond er al uit de briefronde; niet opnieuw gerouteerd.

**Toets:** b1 179,1 km tegen ~185 (Callao-Ticlio 171 + zijlijn ~14 router-schatting): -3,2% (norm ±15%, de 14 km zijlijn is geen bronkm). Naad b1 → b2 0,00 km; geen naad > 5 km. Stippel b2 = eigen verbinding zonder net (terrein), 0,48 km. `toets_rechte_benen --min-km 5`: geen melding voor deze stroom. `toets_knikken`: 12 knikken, 12 omkeringen waarvan 10 als TERUGLOOP gemarkeerd, vrijwel allemaal op de Ticlio-flank (-11.65…-11.90 N, -76.23…-76.52 E): de echte zigzag-keerpunten (retrocesos) van de FCCA tussen Casapalca en Ticlio, geen foutvia. Niet gerepareerd; zou een visuele blik op de bol verdienen.

**Toelichting stippel:** alleen b2 (transportband, eigen terrein). De plant → spoor-snap (0,26 km) is te kort voor een eigen stippel.

**Lessen:** (1) hergebruik van het al gebakken spoor-geojson uit de briefronde spaart een zwaar-slotrun; (2) de bake telt 179,1 km waar de router 178,1 gaf (snap-uiteinden vallen in het geojson, eindpunt -12.0503 i.p.v. ankers); (3) bergspoor met zigzags geeft altijd TERUGLOOP-meldingen in `toets_knikken` die per definitie echt zijn; (4) open punten uit §7 (zijlijn heropend?, concentratorcoördinaat, TCSA-muelle, volume) blijven staan.
