# Routebrief (licht) · zilver — Constancia → Yauri → Matarani (Peru)

**stroom-id:** `zilver-constancia-matarani` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** koperconcentraat (met al het zilver van Hudbay Peru erin, 100% onder de Wheaton-stream) gaat per **truck** van de Constancia-concentrator (Chumbivilcas, Cusco, ~4.200 m) via CU-764, PE-3SG, Yauri, PE-34E/34J en de Interoceánica Sur (PE-34A, Arequipa-omleiding) naar de Tisur-mineralenterminal in Matarani, waar het in een eigen Hudbay-loods wordt gelost en geladen; de lijn stopt op die kade (geen zeebeen: de smelters in China zijn niet met naam gebrond).
**Welke as van het verhaal:** *Cusco-hoogland: een tweede kopercorridor naast Las Bambas, zilver als bijproduct.* Jaarvolume **84,2 t Ag/j (2024)**: 2.708.262 oz [1] x 31,1035 g; 2025 75,1 t (2.415.134 oz, Peru = Constancia + Pampacancha-satelliet) [2]. Constancia-only: "Peru operations" is bij Hudbay alleen Constancia, dus Peru-totaal = Constancia-aandeel.

## 1 · Ketenkaart
```
Constancia-concentrator `ag-constancia-plant` ──(b1 truck · CU-764 → PE-3SG → Yauri → PE-34E/34J → PE-34A · 450–490 km)──►
Tisur Matarani, mineralenterminal `ag-matarani-tisur` ── stoppunt (geen zee, geen smelter met naam)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Constancia-concentrator → Tisur Matarani | CU-764 (10 km onverhard) → PE-3SG (Livitaca-afslag, 70 km naar Yauri) → PE-34E/34J (Yauri, Negro Mayo, Oscollo, Imata) → PE-34A Interoceánica Sur (Yura, Arequipa-omleiding Uchumayo, La Joya) → Matarani [1][3] | echte wegkm: **450** (AIF: "approximately 450 km by road to the Port of Matarani"), **460** (zelfde AIF, B-1), **490** (zelfde AIF, truckbeschrijving) [1]; bake-toets haalbaarheid 471,7 (OSRM 462); hemelsbreed 286, geen wegkm | `maak_stroombeen_weg` (nieuw profiel peru, 7 via-punten) | nee; plant-uiteinde: mijnweg onverhard, kleine klassen incl. `track` binnen 12 km; geen last-mile-been |

Gedeeld met een bestaande stroom: **geen kopie nodig.** Yauri tot Imata (~170 km, PE-34E/34J) valt samen met `koper-lasbambas-tongling` b1 (profiel `koper-lasbambas-pillones`), maar die stroom start bij een andere plant en gaat na Imata naar het spoor bij Pillones; deze rijdt door via Yura en Arequipa naar de kust. Via-punten 2-4 zijn letterlijk de punten van dat profiel.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-constancia-plant` | laadplek (concentrator, kop b1) | Constancia-concentrator (Hudbay, Velille, Chumbivilcas) | -14.4650, -71.7880 | [1][4][sat] | bron-gelegd (z15 gezien: maalgebouwen met verdikkers, tailingsvijver en pit direct ten oosten; Nominatim noemt hier "HR - OP TAJO"; het AIF-projectcentrum -14.45, -71.7833 ligt 1,7 km noordelijker op leeg terrein en is geen anker) |
| `ag-matarani-tisur` | overslag truck → zee, stoppunt | Tisur Matarani, mineralenterminal (shiploader-pier; Hudbay Pier C niet apart geïdentificeerd), hergebruikt letterlijk uit `koper-lasbambas-matarani.md` | -17.0044, -72.1124 | [1][5][6][sat] | aannemelijk (z16 gezien: bulkcarrier aan de shiploader-pier, gesloten bandtrestle naar de wal, drie gesloten loodsen ZO; naam Muelle F, maar de AIF zegt dat de shiploader gedeeld wordt met andere concentraatexporteurs, dus dezelfde laadplek) |

**Pier-vraag (haalbaarheidstoets):** AIF wijst Hudbay "Pier C" toe (75 kt, min. 30 kt gegarandeerd) [1]; Muelle F is voor Cerro Verde, Antapaccay en Las Bambas [5]. Het kandidaatpunt voor C (-16.9992, -72.1076, noordelijke kade) is gecontroleerd op z16 en z17 en **valt af**: dat is de oude hoofdkade met een korrelsilo-batterij en een containerplatform (A/B, geen mineralen). Op de tegels is geen tweede mineraalpier te zien. Daarom het F-punt (0,7 km verder), met de gedeelde shiploader [1] als reden; de truck eindigt toch op de landzijde (eindToegangPrivaat).

## 4 · Via-punten (b1 — op de doorgaande weg, nooit in een stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | plant (kop, anker) | -14.4650, -71.7880 | mijnweg naar CU-764; zonder dit punt kiest de router een zijweg |
| b1 | 2 | PE-34E zuid van Yauri | -14.8222, -71.4165 | afslag zuid (Dv. Tintaya, Negro Mayo), niet PE-3SG NO naar Ayaviri (hergebruikt uit Las Bambas) |
| b1 | 3 | Condoroma (PE-34J/34E) | -15.3000, -71.1384 | de enige weg Negro Mayo-Oscollo-Imata, niet west via Callalli/Sibayo (hergebruikt) |
| b1 | 4 | PE-34A ZW van Imata | -15.8436, -71.1063 | na de aansluiting op PE-34A: west richting Yura, niet oost naar Juliaca (hergebruikt) |
| b1 | 5 | Yura (Interoceánica Sur, tramo 5) | -16.2133, -71.6505 | pint de noordkant van Arequipa; Nominatim: Vía Interoceánica Sur, Yura |
| b1 | 6 | Uchumayo, Arequipa-omleiding | -16.4274, -71.6484 | ten westen van de stad, niet door het centrum (Arequipa ligt op -71.54) |
| b1 | 7 | La Cruz del Cerrito (Mollendo) | -16.8087, -72.0036 | Interoceánica Sur naar de kust, Matarani-tak; Nominatim: Carretera Interoceánica Sur |
Vlaggen voor het profiel: `eindToegangPrivaat` true (haveneindpunt), `trimStaart` true, `vensterKm` 100, `gepubliceerdKm` 475; `eindKlassen` incl. `track`.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Constancia-concentrator | Hudbay Minerals | erts (Constancia + Pampacancha-satelliet) → Cu-concentraat met Ag, Au, Mo | zilver 2.708.262 oz (2024), 2.415.134 oz (2025) | [1][2] |
| Tisur Matarani, Hudbay-loods + Pier C | Tisur (Grupo Romero / Tramarsa) | truck, 37 t per lading, gesloten ontvangst → band 1.200 t/u → shiploader | Pier C 75 kt, min. 30 kt gegarandeerd | [1][5] |

## 6 · Stoppunt
De brief stopt in Matarani: Hudbay zegt alleen dat het merendeel van het Constancia-concentraat naar smelters in China gaat [1]; geen smelter, geen schip en geen bestemmingshaven met naam, dus fase B en verder vervallen, D en E vervallen.

## 7 · Open punten
- **Pier C niet gelegd**: AIF noemt Pier C, op de tegels is alleen de shiploader-pier (F) als mineralenpier te zien; ligging van Hudbay's loods onbekend. Zie §3.
- **Wegkm loopt uiteen** in dezelfde AIF (450 / 460 / 490); de ±15%-toets geldt tegen 475, dus 404-546 km. Toets haalbaarheid 471,7.
- **Volume is het Peru-totaal**, bij Hudbay gelijk aan Constancia; "payable silver" gaat via de stream naar Wheaton, het concentraat (waarin het zilver zit) rijdt naar Matarani. Peiljaar 2024 gehouden; Pampacancha is sinds Q4 2025 uitgeput [2].
- **Zilver komt per mijn nergens apart gepubliceerd als truck-lading**: de lijn toont de concentraatstroom, het zilver is een bijproduct. Smelter niet gebrond.
- **Last mile plant**: mijnweg (onverhard, 10 km CU-764); OSM-dekking niet gecontroleerd.
- **Sitelaag zilver kent Constancia en Matarani niet**; centraal toevoegen (zelfde punten als §3).

## 8 · Bronnen
[1] Hudbay Minerals, Annual Information Form FY2024 (Form 40-F): zilver 2.708.262 oz, 100% stream, Yauri 80 km, Matarani 460 / 490 / "approximately 450" km, CU-764 en PE-3SG, Pier C 75 kt, smelters in China — https://www.sec.gov/Archives/edgar/data/1322422/000106299325006369/exhibit99-1.htm
[2] Hudbay Minerals, AIF FY2025: 2.415.134 oz zilver in Peru, Pampacancha afgerond Q4 2025, Pier C ongewijzigd — https://www.sec.gov/Archives/edgar/data/1322422/000106299326001648/exhibit99-1.htm
[3] OSM via Nominatim reverse (2026-10-30): Interoceánica Sur bij Yura, Uchumayo en Mollendo-La Cruz del Cerrito; plant als "OP TAJO", Velille — https://nominatim.openstreetmap.org
[4] Mining Data Online, Constancia Mine: Hudbay, 52 km NW van Espinar — https://miningdataonline.com/property/1102/Constancia-Mine.aspx
[5] Mundo Marítimo, 2016, Tisur-uitbreiding Matarani: Muelle C mineralen (Constancia), Muelle F 260 m (Cerro Verde, Antapaccay, Las Bambas), shiploader 2.000 t/u — https://mundomaritimo.cl/noticias/la-moderna-expansion-del-complejo-portuario-inaugurado-por-tisur-en-matarani
[6] `v2/design/routebrieven/koper-lasbambas-matarani.md`: anker Muelle F -17.0044, -72.1124 (z16), via-punten 2-4, Rumbo Minero/Gestión over Tisur
[7] Hudbay-zoekresultaat 6-K/40-F 2012-2025 (WebSearch): Pier C toegewezen aan Hudbay, TISUR-operator, gedeelde shiploader — https://www.sec.gov/Archives/edgar/data/1322422/000106299316012465/exhibit99-1.htm
[sat] Esri World Imagery via sat_check.py (2026-10-30), `v2/build-cache/satcheck/`: `sat-zilver-constancia-matarani-plant.png` (z15) · `-tisurC.png` (z16) · `-tisurC17.png` (z17, korrelsilo's, A/B) · `-tisurZ17.png` (z17, containerplatform) · `-tisurF.png` (z16, shiploader-pier)

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
- **Bestand:** `v2/data/stroomroute-zilver-constancia-matarani.json` (151,4 KB, versie 2, lonlat, 1 been, 7.083 punten, 2 markers), titel "Zilver · Constancia-concentrator (Hudbay) → Tisur Matarani (Peru)". Recept: `bak_zilver_constancia_matarani()` in `v2/tools/bak_stromen.sh`.
- **b1 truck, doorgetrokken: 466,3 km** (weglijn 466,0 + 0,03 km plant-verbinding + 0,22 km kade-verbinding) tegen de echte wegkm 475 (Hudbay AIF 450/460/490): -1,9%, binnen de ±15%-norm (en binnen 450-490 behalve de 450-ondergrens). Segmenten: plant-Yauri 86,1 · Yauri-Condoroma 74,5 · Condoroma-Imata 73,2 · Imata-Yura 94,8 · Yura-Uchumayo 40,3 · Uchumayo-Cerrito 67,3 · Cerrito-Matarani 30,2. Alle via-snaps 0,00-0,03 km, de kade-snap 0,22 km.
- **Geometrie:** nieuw profiel `zilver-constancia-matarani-plant-matarani` in `maak_stroombeen_weg.py` (extract peru, vensterKm 100, refs PE-3SG/34E/34J/34A/CU-764, `eindKlassen` incl. `track`, `eindToegangPrivaat`, `trimStaart`), gescand met `wegscan_puur.py` (95 s). First mile over kleine klassen 12,4 km (CU-764 en mijnweg, geen last-mile-stippel nodig), last mile 2,5 km. 24 keerlussen gesnoeid (0,5 km).
- **Via-punten:** de zes uit §4 zonder wijziging; geen snap > 0,03 km, dus niets verplaatst of verwijderd. Geen omweg (segmenten 30-95 km).
- **Naden en markers:** één been, dus geen naad; beide markers liggen op de lijn (0,0 km). Plant-uiteinde en Matarani-uiteinde zijn exact de ankers; de pier ligt in zee, de lijn eindigt op de landzijde 0,22 km van het anker.
- **Geen stippel, geen aanloop, geen vlucht, geen leiding, geen kopie, geen zeebeen:** de brief stopt in Matarani (§6). Geen haven-aanloop nodig (geen zeebeen).
- **Toetsen:** `toets_knikken.py` 19 knikken >= 60 graden (spikes van 4-64 m op kruispunten en haarspeldbochten), 0 omkeringen, 0 teruglopen; `toets_rechte_benen.py` geen treffer voor deze stroom.
- **Open punten blijven:** Pier C van Hudbay niet gelegd (anker = shiploader-pier F, aannemelijk); wegkm loopt uiteen in de AIF (450/460/490); sitelaag zilver kent Constancia en Matarani niet (centraal); smelter in China niet gebrond.
- **Lessen:** de plant-kant lag meteen op de weg (snap 0,03 km); een brief die alle via-punten hergebruikt uit een bestaand profiel (koper-lasbambas-pillones) en de toetspunten van de haalbaarheidscheck levert een eerste-keer-goede scan op. Tijdens het bakken kan een gelijktijdige edit van een andere agent `bak_stromen.sh` kortstondig syntactisch breken; de bake zelf was niet geraakt.
