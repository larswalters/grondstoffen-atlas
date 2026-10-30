# Routebrief (licht) · Goud — Salares Norte → Santiago (SCL) → MKS PAMP (Zwitserland, aannemelijk)

**stroom-id:** `goud-salaresnorte-pamp` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) ·
**status:** gebakken
**Keten in één zin:** goud-zilver-doré van Salares Norte (Gold Fields, 4.200–4.900 m, Atacama) per truck via C-13/C-173/C-167 naar
Diego de Almagro, over C-17 en Ruta 31/30 naar Ruta 5 (Panamericana) en zuidwaarts naar de vrachtterminal van Santiago (SCL), per
vrachtvlucht (grootcirkel) naar de vrachtterminal van Zürich (ZRH) en per truck over de A2/Gotthard-as naar MKS PAMP, Castel San Pietro.
**Welke as van het verhaal:** de enige keten vanuit de Chileense Andes en het eerste Chili-goud op de bol. 2025: 12.333 kg goudequivalent
(396,5 koz-eq) = max **12,3 t Au-eq/j** (zuiver goud lager: zilver zit erin) [1][3]; 2026-guidance 525–550 koz-eq = 16,3–17,1 t Au-eq.
Het 20-F zegt: doré gaat naar MKS-raffinaderijen in **India of Zwitserland**; Zwitserland is hier een keuze, geen bron (§7).

## 1 · Ketenkaart
```
Salares Norte-plant `au-salaresnorte-plant`
  ──(b1 truck · C-13/C-173/C-167 → Diego de Almagro → C-17 → Ruta 31/30 → Ruta 5 · 183 km tot DdA [1], rest indicatie)──►
Santiago vrachtterminal (SCL) `au-scl-vrachtterminal`  ──(b2 stippel · last mile 0,15 km, airside)──►
  ──(b3 lucht · SCL → ZRH, grootcirkel, aannemelijk · 11.958 km hemelsbreed)──►
Zürich vrachtplatform (ZRH) `au-zrh-vrachtterminal` (hergebruikt)  ──(b4 stippel · last mile 0,91 km)──►
  ──(b5 truck · A1/A4 → A2 Gotthard · 263,3 km, omgekeerde kopie goud-pamp-shanghai b1)──► MKS PAMP `au-pamp-raffinaderij` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Salares Norte-plant → openbare weg bij SCL (aannemelijk: bron noemt Zwitserland of India, vervoerswijze niet gebrond) | C-13/C-173/C-167 → Diego de Almagro → C-17 → Ruta 31/30 → Ruta 5 (bypass Copiapó) → Vespucio Norte/Autopista Aeropuerto | 183 mijn → Diego de Almagro [1]; Copiapó → Santiago ca. 800 [6]; DdA → Copiapó hemelsbreed 112 km, geen wegkm; totaal hemelsbreed 842 km, geen wegkm (indicatie 1.100–1.200) | maak_stroombeen_weg (profiel chili) | nee |
| b2 | A | truck | openbare weg (Osvaldo Croquevielle) → SCL-vrachtterminal | last mile airside | 0,15 hemelsbreed | stippel | **ja**: airside/privéterrein |
| b3 | B | lucht | SCL → ZRH (aannemelijk: bron noemt Zwitserland of India) | vrachtvlucht, grootcirkel | 11.958 hemelsbreed [berekend] | maak_luchtbeen | nee, doorgetrokken |
| b4 | B | truck | ZRH-vrachtplatform → openbare weg (47,4721, 8,5545) | last mile airside | 0,91 [pamp-shanghai] | stippel | **ja**: airside |
| b5 | C | truck | openbare weg ZRH → MKS PAMP | A1/A4 Knonaueramt → A14 → A2 Gotthard | 263,3 gemeten, omgekeerde kopie [8] | letterlijke kopie geojson | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-salaresnorte-plant` | mijn / laadplek | Salares Norte, verwerkingsplant (Gold Fields) | -26.0220, -68.8917 | [1][2] | bron-gelegd (z16 gezien: molen-/tankcluster met koepel ZO van de dagbouw, kampmodules ten NW; het 20-F-punt -26.0117, -68.8931 ligt midden in de put, 1,15 km NNW; `sat-goud-salaresnorte-pamp-plant.png`) |
| `au-scl-vrachtterminal` | overslag / lucht | Santiago (SCL), internationale vrachtzone, grote loods aan het platform, Pudahuel | -33.4105, -70.7874 | [7] | bron-gelegd, loods op pandniveau **onzeker** (z16 gezien: grote witte loods met laaddocks direct aan het platform ten Z van de passagiersterminal; OSM: bushalte Carga Internacional, TEISA-vrachtwagenparking, Depocargo aan Osvaldo Croquevielle op ~100 m; `-scl-carga16.png`) |
| `au-zrh-vrachtterminal` | overslag / lucht | Zürich Airport vrachtplatform (hergebruikt uit goud-pamp-shanghai.md) | 47.4647, 8.5492 | [8] | bron-gelegd (daar gezien) |
| `au-pamp-raffinaderij` | raffinaderij | MKS PAMP SA, Via alle Zocche 1, Castel San Pietro (hergebruikt) | 45.8546, 9.0025 | [8] | bron-gelegd (daar gezien) |

## 4 · Via-punten (b1, lat, lon; 8 stuks, alle op een OSM-vertex van de genoemde weg, geen stadscentrum)
| # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|
| 1 | C-167, W van de C-173-aansluiting | -26.4043, -69.8901 | de mijnweg bereikt Diego de Almagro alleen via C-167; sluit het centrum uit |
| 2 | C-17 ten Z van Inca de Oro | -26.8938, -69.9199 | kiest de binnenlandroute C-17 → Ruta 31 (±150 km tot Copiapó) boven C-13 west → Ruta 5 kust (±270 km) |
| 3 | Ruta 30, W van Tierra Amarilla (hergebruik koper-caserones) | -27.5015, -70.4088 | komt de Copiapó-vallei in zonder het stadscentrum (Avenida Copayapu) |
| 4 | Ruta 5 Norte, bypass Copiapó zuidkop (hergebruik, bindend) | -27.5060, -70.4491 | Ruta 5 zuidwaarts vanaf de bypass |
| 5 | Ruta 5 Norte, N van La Serena | -29.8174, -71.2746 | pint Ruta 5 (geen kustweg/Ruta 41) vóór de La Serena-Coquimbo-agglomeratie |
| 6 | Ruta 5 Norte, N van Los Vilos | -31.8403, -71.5156 | pint de kustvariant van Ruta 5 vóór La Ligua |
| 7 | Ruta 5 Norte bij Tiltil | -32.9352, -70.8138 | Ruta 5 naar Santiago, niet Ruta 68 |
| 8 | Autopista Vespucio Norte (ref 70) | -33.4053, -70.7821 | de ring naar Autopista Aeropuerto (ref 72), niet door het centrum |
Eindpunt van het wegprofiel: openbare weg Osvaldo Croquevielle (service) -33.4108, -70.7890, 0,15 km van het anker; lukt "geen wegpad", dan het wegprofiel eindigen op Armando Cortinez Oriente (-33.4084, -70.7917) en de b2-stippel verlengen.
Extracts b1: chili. b5: zwitserland. Refs b1: C-13, C-173, C-167, C-17, 31, 30, 5, 70, 72. corridorKlassen: tertiary, unclassified, service; eindToegangPrivaat true; venster 40 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Salares Norte | Gold Fields | erts → goud- en zilverdoré | 396,5 koz-eq 2025; steady state Q4 2025; 2026-guidance 525–550 koz-eq | [1][3] |
| MKS PAMP | MKS PAMP SA | doré → LBMA-baren | Zwitserse raffinage, niet Salares-specifiek | [1][8] |

## 6 · Stoppunt
De brief stopt bij MKS PAMP: het 20-F noemt de raffinaderij als afnemer (FCA, via MKS-agent) en geen bron noemt een volgende bestemming van deze baren. Fase D/E vervallen.

## 7 · Open punten
- **BINDEND:** Zwitserland is een keuze: het 20-F zegt India of Zwitserland; de naam van b1 en b3 draagt "aannemelijk". Blijkt het India, dan wijzigt het eindpunt in de titel. Contract MKS PAMP loopt tot 31-12-2026 (verlenging mogelijk).
- Geen bron voor vervoerswijze of luchthaven; alleen indirect: Chili exporteert zijn goud overwegend naar Zwitserland ($741 mln in 2022) [4] en één handelsrecord noemt goud met lading Santiago per lucht [5]. Copiapó (233 km hemelsbreed) en Caldera zijn reële alternatieven voor het vertrekpunt.
- Een directe vrachtvlucht SCL → ZRH is niet gevonden; één grootcirkel is de tekenaanname (tussenlanding in een hub niet gebrond).
- Het 20-F noemt Caldera als toegang tot de site; de binnenlandroute via Diego de Almagro volgt de OSM-meting (183,3 km) en het 20-F (183 km).
- Wegkilometers DdA → Copiapó en Santiago-aansluiting niet gebrond; b1 niet aan ±15% toetsen maar als indicatie. Gravelweg op 4.500 m: OSM-dekking mijn → C-13 te toetsen; ligt het plant-anker > 2 km van het net, dan stippel "last mile (geen net op deze korrel)".
- SCL-loods niet pandgenaamd; ZRH-platform airside (patroon b4 = goud-pamp-shanghai).

## 8 · Bronnen
[1] Gold Fields, Form 20-F FY2025 (Refining and Marketing, Chile; 183 km DdA; 26°0'42"S 68°53'35"W; toegang vanuit Caldera). https://www.sec.gov/Archives/edgar/data/1172724/000162828026021904/gfi-20251231.htm
[2] Gold Fields, Technical Report Summary Salares Norte 2024 (UTM 510481 E, 7123125 N; 266 km vanaf Copiapó). https://www.sec.gov/Archives/edgar/data/1172724/000117272425000010/a964-technicalreportsummar.htm
[3] Idem [1], productietabel Salares Norte 2025: 12.333 kg, 397 koz; guidance 2026 525–550 koz-eq.
[4] OEC, Gold exports of Chile (Zwitserland grootste bestemming). https://www.oec.world/profile/bilateral-product/gold/reporter/chl
[5] Panjiva, Compania Minera Dayton (goud HS 71081210, Santiago, lucht, 2019). https://panjiva.com/Compania-Minera-Dayton/5781346
[6] Wikipedia, Copiapó (ca. 800 km ten noorden van Santiago). https://en.wikipedia.org/wiki/Copiap%C3%B3
[7] OpenStreetMap (ODbL) via Overpass: wegvertices C-173/C-167/C-17/Ruta 31/30/Ruta 5/Vespucio Norte/Osvaldo Croquevielle, vrachtobjecten SCL. https://www.openstreetmap.org
[8] Routebrief goud-pamp-shanghai.md (ZRH- en PAMP-anker, b1 263,3 km, ZRH-stippel) en goud-yanacocha-ticino.md.
[9] Routebrief koper-caserones-saganoseki.md (via 3 en 4).
Satellietblik (Esri z15/z16, 2026-10-30): `v2/build-cache/satcheck/sat-goud-salaresnorte-pamp-salaresnorte.png`, `-plant.png`, `-scl-carga.png`, `-scl-carga16.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
Stroom `goud-salaresnorte-pamp` gebakken via `bash v2/tools/bak_stromen.sh goud-salaresnorte-pamp` (functie `bak_goud_salaresnorte_pamp`, profiel `goud-salaresnorte-pamp-plant-scl`), uitvoer `v2/data/stroomroute-goud-salaresnorte-pamp.json` (467,3 KB, 22.761 punten, 5 benen, 4 markers, 13.359,9 km).

| # | modaliteit | km gebakken | brief | opmerking |
|---|---|---|---|---|
| b1 | truck, doorgetrokken | 1.137,9 | indicatie 1.100-1.200 (hemelsbreed 842, geen wegkm) | plant -> Diego de Almagro -> C-17/Ruta 31/30 -> Ruta 5 -> Vespucio Norte -> Osvaldo Croquevielle. Plant snapt op 0,06 km (mijnweg is OSM-weg, geen last-mile-stippel nodig). Stuk plant -> via 1 = 163,6 km (20-F: 183 km tot DdA incl. het stuk door de stad, +/-3%). Geen ±15%-norm, wel indicatie: binnen de bandbreedte. |
| b2 | truck, STIPPEL | 0,15 | 0,15 | SCL-vrachtplatform last mile, airside |
| b3 | lucht, doorgetrokken | 11.957,6 | 11.958 | maak_luchtbeen.py, 480 punten, grootcirkel SCL -> ZRH |
| b4 | truck, STIPPEL | 0,91 | 0,91 | ZRH-vrachtplatform last mile, airside (zelfde coordinaten als goud-pamp-shanghai) |
| b5 | truck, doorgetrokken | 263,3 | 263,3 | LETTERLIJKE omgekeerde kopie van `goud-pamp-shanghai-weg-pamp-zrh.geojson` (punten omgedraaid, properties van/naar gewisseld), precedent diamant-gahchokue-gaborone |

Naden: alle 0,00 km (b1 eindigt exact op het b2-beginpunt -33,4108/-70,7890). Markers: alle vier 0,0 km van hun lijn. Geen zee, geen haven-aanloop, geen leiding.
**Recept:** profiel (extract chili, refs C-13 C-173 C-167 C-17 31 30 5 70 72, corridorKlassen tertiary/unclassified/service, eindToegangPrivaat, venster 40 km, gepubliceerdKm None) met de acht via-punten uit §4, gescand met `wegscan_puur.py` (chili, 74 s); `maak_luchtbeen.py --van 'SCL-vrachtterminal|-33.4105,-70.7874' --naar 'ZRH-vrachtterminal|47.4647,8.5492'`; b5 omgekeerd uit het pamp-shanghai-geojson; twee `--stippel`-regels in de bake-functie.
**Toelichting stippels:** b2 en b4 zijn "hier reikt het net niet": een vrachtplatform ligt airside/privéterrein zonder wegpad; het wegbeen eindigt op de dichtstbijzijnde openbare weg (patroon goud-loulo-ticino / goud-pamp-shanghai). De vlucht (b3) is doorgetrokken; "aannemelijk: bron noemt Zwitserland of India" staat in de beennaam, niet in de lijnstijl.
**Toelichting leiding/aanloop:** niet van toepassing.
**Bevindingen:** (1) bestand 467 KB > de ~300 KB-richtlijn: b1 heeft 16.123 punten door de 1.138 km volle OSM-resolutie; niet herbakken, de bundel simplificeert (L0/L1). (2) toets_knikken: 1 "TERUGLOOP" op -26,4045/-69,5906 (een zijspoor van circa 40 m in het OSM-wegnet bij Diego de Almagro, geen omweg) en drie echte haarspeldbochten in de Santiago-knooppunten (Vespucio/Autopista Aeropuerto); de overige knikken zijn spikes < 70 m uit de OSM-geometrie. (3) Alle via-punten snapten op 0,00-0,06 km; geen via-punt verwijderd of verplaatst. (4) De open punten uit §7 blijven staan: Zwitserland is een keuze (India mogelijk), SCL-loods niet op pandniveau, geen directe vrachtvlucht SCL-ZRH gevonden.
**Lessen:** een OSM-gekarteerde mijnweg op 4.500 m (Salares Norte -> C-13) werd gewoon door de wegscan gevonden met eindToegangPrivaat; het 20-F-punt (de put) is geen anker, de plant ZO ervan wel. Een gedeeld been omkeren: properties (van/naar, snap, kleine-klassekm) mee omwisselen.
