# Routebrief (licht) · Goud — El Peñón (Chili) → Santiago (SCL) → Argor-Heraeus, Mendrisio (Zwitserland, aannemelijk)

**stroom-id:** `goud-elpenon-argorheraeus` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) ·
**status:** gebakken
**Keten in één zin:** goud-zilver-doré van de El Peñón-plant (Pan American Silver, Antofagasta-regio, ca. 1.700 m) per truck over de eigen toegangsweg naar Ruta 5 (Longitudinal Norte) en zuidwaarts via Chañaral en de Copiapó-bypass naar de vrachtterminal van Santiago (SCL), per vrachtvlucht (grootcirkel) naar Milaan-Malpensa (MXP) en per truck over A8/A9/A2 naar Argor-Heraeus, Mendrisio.
**Welke as van het verhaal:** Chileense doré naar een Zwitserse raffinaderij. 2025: 115,2 koz goud = **3,6 t Au/j** (115,2 ÷ 32,15) [1]; de AIF noemt contracten met MKS PAMP en Argor-Heraeus zonder verdeling, dus Argor is een keuze (50% kans per zending), geen bron (§7).

## 1 · Ketenkaart
```
El Peñón-plant `au-elpenon-plant`
  ──(b1 truck · mijnweg → Ruta 5 → Chañaral → Copiapó-bypass → Ruta 5 → Vespucio Norte · hemelsbreed 1.008,6 km, indicatie ≈1.293 — aannemelijk)──►
Santiago vrachtterminal (SCL) `au-scl-vrachtterminal` (hergebruikt)  ──(b2 stippel · last mile 0,15 km, airside)──►
  ──(b3 lucht · SCL → MXP, grootcirkel, aannemelijk · 11.863,2 km gemeten)──►
Malpensa Cargo City Sud (MXP) `au-air-mxp` (hergebruikt)
  ──(b4 truck · A8 → A9 → A2 · 76,0 km, omgekeerde kopie goud-argor-mumbai b1)──► Argor-Heraeus `au-ref-argor` (hergebruikt) ── stoppunt
```
Been B uit het ontwerp (vlucht ANF → SCL) **vervalt**: geen ANF-vrachtanker te leggen (§3, §7); het wegbeen gaat rechtstreeks naar SCL (patroon goud-salaresnorte-pamp).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | El Peñón-plant → openbare weg bij SCL (aannemelijk: bron noemt alleen "doré wordt vervoerd", geen modaliteit) | mijnweg (unclassified, paved) → Ruta 5 Norte (asphalt) → Chañaral → Copiapó-bypass → Ruta 5 → Vespucio Norte (70) → Autopista Aeropuerto (72) | hemelsbreed 1.008,6 km, geen wegkm; indicatie 1.293 = 501,6 (OSM-meting plant → Copiapó-bypass) + 791,1 (goud-salaresnorte-pamp, benen via 4 → eind); AIF-bronwaarde 165 km (mijn → Antofagasta) staat los van dit been [1][2] | maak_stroombeen_weg (profiel chili) | nee |
| b2 | A | truck | openbare weg (Osvaldo Croquevielle) → SCL-vrachtterminal | last mile airside | 0,15 hemelsbreed | stippel | **ja**: airside/privéterrein |
| b3 | B | lucht | SCL → MXP (aannemelijk: een van twee contractraffinaderijen, PAMP of Argor) | vrachtvlucht, grootcirkel | 11.863,2 [maak_luchtbeen, proefgedraaid, 476 punten] | maak_luchtbeen | nee, doorgetrokken |
| b4 | C | truck | MXP-vrachtterminal → Argor-Heraeus | A8 → A9 → grens Chiasso → A2 | 76,0 gemeten, omgekeerde kopie [7] | letterlijke kopie geojson | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-elpenon-plant` | mijn / laadplek (plant) | El Peñón, verwerkingsplant (Pan American Silver) | -24.4108, -69.4962 | [3][4] | bron-gelegd (z14 en z15 gezien: gebouwencluster van de plant in het midden, open pit en wand ca. 2 km NNW, drogestapel-/tailingsvlakken ZO, toegangsweg verlaat het complex naar het ZW; `sat-goud-elpenon-argorheraeus-plant.png`, `-plant15.png`) |
| `au-scl-vrachtterminal` | overslag truck → lucht | Santiago (SCL), vrachtzone, Pudahuel (hergebruikt uit goud-salaresnorte-pamp.md) | -33.4105, -70.7874 | [6] | bron-gelegd, loods op pandniveau **onzeker** (daar gezien) |
| `au-air-mxp` | overslag lucht → truck | Milano Malpensa Cargo, Cargo City Sud (hergebruikt uit goud-argor-mumbai.md) | 45.6142, 8.7186 | [7] | bron-gelegd (daar gezien) |
| `au-ref-argor` | raffinaderij | Argor-Heraeus SA, Mendrisio (hergebruikt uit goud-argor-mumbai.md) | 45.8749, 8.9818 | [7] | bron-gelegd (daar gezien) |

Niet gelegd: ANF-vrachtanker. Z15/z16 op Antofagasta (-23.4445, -70.4451 en -23.4490, -70.4395): één baan, een passagiersterminal met vliegtuigbruggen en bijgebouwen van de luchtmachtbasis Cerro Moreno; geen herkenbare vrachtloods (`sat-goud-elpenon-argorheraeus-anf.png`, `-anf16.png`, `-anfterm.png`). Daarom geen anker en geen been B.

## 4 · Via-punten (b1; alle op een OSM-vertex van Ruta 5, geen stadscentrum; 1 en 6 t/m 9 zijn de ankers resp. hergebruik)
| # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|
| 1 | El Peñón-plant (anker) | -24.4108, -69.4962 | begin; OSM-snap 0,06 km op een service-weg met access=no (eindToegangPrivaat) |
| 2 | Ruta 5 Norte, 10 km ZO van de mijnweg-aansluiting | -24.5706, -69.7962 | mijnweg (paved, 39 km) op Ruta 5 in plaats van de noordelijke mijnweg naar de Ruta Minera/B-55 (OSRM-keuze, 127 km tot Ruta 5) |
| 3 | Ruta 5, Z van de B-905-afslag (Cruce Agua Verdes) | -25.5467, -70.0851 | houdt Ruta 5 via Chañaral aan boven de binnenlandse mijnwegen B-905/B-895/C-115-B/C-17 (±455 km tegen ±502 km tot Copiapó) |
| 4 | Ruta 5, 18 km Z van Chañaral | -26.5092, -70.7003 | pint Ruta 5 Chañaral → Copiapó langs de kust (Caldera-zijde), geen sluiproute naar het binnenland; ligt buiten Chañaral |
| 5 | Ruta 5 bypass Copiapó zuidkop (hergebruik goud-salaresnorte-pamp via 4, bindend) | -27.5060, -70.4491 | Ruta 5 zuidwaarts vanaf de bypass |
| 6 | Ruta 5 N van La Serena (hergebruik salaresnorte via 5) | -29.8174, -71.2746 | Ruta 5, geen kustweg/Ruta 41 |
| 7 | Ruta 5 N van Los Vilos (hergebruik via 6) | -31.8403, -71.5156 | kustvariant van Ruta 5 vóór La Ligua |
| 8 | Ruta 5 bij Tiltil (hergebruik via 7) | -32.9352, -70.8138 | Ruta 5 naar Santiago, niet Ruta 68 |
| 9 | Autopista Vespucio Norte (ref 70) (hergebruik via 8) | -33.4053, -70.7821 | de ring naar Autopista Aeropuerto, niet door het centrum |
| 10 | openbare weg Osvaldo Croquevielle (hergebruik) | -33.4108, -70.7890 | eindpunt wegprofiel, 0,15 km van het anker; lukt "geen wegpad", eindig dan op Armando Cortinez Oriente (-33.4084, -70.7917) en verleng de b2-stippel |
Extract b1: chili. Refs b1: 5, 70, 72 (tertiary/unclassified/service als corridorKlassen, want de mijnweg is unclassified; eindToegangPrivaat true; venster 40 km). Dijkstra over de lokale chili-pbf met Ruta 5 bevoorrecht gaf plant → Copiapó-bypass 501,6 km: 1,5 km service, 39,0 km unclassified (paved), 461 km Ruta 5.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| El Peñón | Pan American Silver | erts (1,4 Mt verwerkt 2025) → goud-zilverdoré (Merrill-Crowe) | 115,2 koz Au + 3,9 Moz Ag in 2025; plant ca. 3.600 t erts/dag | [1][2] |
| Argor-Heraeus | Argor-Heraeus SA | doré → LBMA-baren | niet El Peñón-specifiek | [1][7] |

## 6 · Stoppunt
De brief stopt bij Argor-Heraeus: de AIF noemt de raffinaderij als contractafnemer en geen bron noemt een volgende bestemming van deze baren. Fase D/E vervallen.

## 7 · Open punten
- **BINDEND:** Argor is een aanname: de AIF noemt MKS PAMP en Argor-Heraeus zonder verdeling (50% kans per zending); b1 en b3 dragen "aannemelijk" in de naam. Is het PAMP, dan wijzigt het eindpunt (zie goud-salaresnorte-pamp voor SCL → ZRH → PAMP).
- Geen bron voor het vervoer ("the doré is transported to these facilities"): truck naar SCL en een SCL → MXP-vlucht zijn de tekenaanname. Een tussenlanding of een vlucht ANF → Europa is niet gebrond en niet getekend; LATAM Cargo vliegt sinds 23-5-2026 wekelijks een B767-vrachter FRA–ANF (invoer mijnonderdelen, geen doré) [9] en ANF heeft een kleine exportterminal (478 m², koude keten, fruit; locatie alleen op een plattegrondafbeelding) [10]: een ANF-vlucht is een reëel alternatief maar niet te leggen.
- Wegkm niet gebrond voor het hele been: AIF 165 km en Exponor 160 km (bus 2 u 15 min) gelden mijn → Antofagasta [1][2]; eigen meting 141,1 km plant → Ruta 5 bij La Negra + ca. 26 km (OSRM-stappen) tot de stadsrand = 167 km (+1,3%, geen norm). OSRM zelf kiest een noordelijke mijnweg en komt op 197 km naar de ANF-luchthaven [8]; de 39 km paved unclassified naar Ruta 5 (OSM-way 112893890) is dus de keuze van dit been. b1 is een indicatie, geen ±15%-toets.
- Binnenlandse mijnwegen B-905/B-895/C-115-B/C-17 (tertiary, chipseal) naar Copiapó zijn ca. 45 km korter dan Ruta 5; wegklasse en verkeersgebruik niet gebrond, Ruta 5 is gekozen.
- Plant-snap ligt op een service-weg met access=no: lukt het bakken niet, plant-anker dan vervangen door het begin van de mijnweg (-24.4137, -69.5029) met een korte stippel "last mile (geen net op deze korrel)".
- SCL-loods niet pandgenaamd; MXP- en Argor-anker hergebruikt zonder nieuwe check. El Peñón staat niet in `goud-sitelaag.json` (3,6 t/j): centraal toe te voegen.
- Het ontwerp (b4 ≈ 70 km) was een schatting; gemeten is 76,0 km.

## 8 · Bronnen
[1] Pan American Silver, Annual Information Form FY2025 (El Peñón: 115,2 koz Au, 3,9 Moz Ag, 1,4 Mt verwerkt; ca. 165 km ZO van Antofagasta; contracten met MKS PAMP en Argor-Heraeus in Zwitserland; "the doré is transported to these facilities"). https://www.sec.gov/Archives/edgar/data/771992/000077199226000019/aif-2025ye.htm
[2] Exponor, Programa Visita Faena El Peñón 2026 (160 km van Antofagasta; transfer 06:30 → ca. 08:30; ca. 3.600 t erts/dag; 115,2 koz, 3,9 Moz). https://exponor.cl/wp-content/uploads/2026/04/Programa-Visita-Faena-El-Penon-2026_eng.pdf
[3] Wikidata Q16969356, El Peñón mine, P625: -24.410755, -69.496204. https://www.wikidata.org/wiki/Q16969356
[4] Esri World Imagery via `v2/tools/sat_check.py` (live, 2026-10-31): `v2/build-cache/satcheck/sat-goud-elpenon-argorheraeus-plant.png`, `-plant15.png`, `-anf.png`, `-anf16.png`, `-anfterm.png`.
[5] OpenStreetMap (ODbL): lokale Geofabrik chili-pbf (scan 2026-10-31, Dijkstra) en API-tags van way 112893890 (unclassified, paved), 1116408769 (Ruta 5 Norte, asphalt, Longitudinal Norte Portezuelo Las Bombas–Quillagua), 1454583032 (B-905, Cruce Ruta 5–Mina La Pólvora, chipseal). https://www.openstreetmap.org
[6] Routebrief goud-salaresnorte-pamp.md (§3 SCL-anker, §4 via 4–9 en eindpunt, last-mile-stippel; §8 [4] OEC en [5] Panjiva als indirecte bron voor Chileens goud naar Zwitserland per lucht).
[7] Routebrief goud-argor-mumbai.md (MXP- en Argor-anker; b1 76,0 km, `goud-argor-mumbai-weg-argor-mxp.geojson`).
[8] OSRM publieke demo, route plant → Antofagasta-luchthaven: 197,3 km (stappen Ruta Minera, Ruta 5 Norte, B-472, Ruta 26, Ruta 1). https://router.project-osrm.org
[9] Air Cargo Week, LATAM Cargo connects the mining industry in northern Chile with Europe (2026-06-12). https://aircargoweek.com/latam-cargo-connects-the-mining-industry-in-northern-chile-with-europe/
[10] SCL Air Cargo, presentatie Terminal de Exportaciones, Aeropuerto Andrés Sabella Gálvez (478,82 m², 0–8 °C). https://www.al.ms.gov.br/upload/Pdf/2022_06_08_10_06_00_p3-oscar-martinez-da-scl-air-cargo-presentacion-terminla-exportaciones-anf.pdf
[11] Wikipedia, Antofagasta (ca. 1.100 km ten noorden van Santiago, hemelsbreed). https://en.wikipedia.org/wiki/Antofagasta
[12] Eigen berekening: haversine plant → SCL-weg 1.008,6 km; grootcirkel SCL → MXP 11.863,2 km (`maak_luchtbeen.py`).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)
**Bestand:** `v2/data/stroomroute-goud-elpenon-argorheraeus.json` (384,0 KB, versie 2, punt_formaat lonlat) · functie `bak_goud_elpenon_argorheraeus` in `bak_stromen.sh` · profiel `goud-elpenon-argorheraeus-plant-scl` in `maak_stroombeen_weg.py` · **totaal 13.231,1 km, 5 benen, 18.242 punten, 4 markers**. Alle naden 0,000 km.

| # | modaliteit | km | opmerking |
|---|---|---|---|
| b0 | truck, **stippel** | 1,3 (1,287) | El Peñón-plant → eerste openbare mijnwegknoop; plantwegen zijn access=no (niet in de brief, zie afwijking) |
| b1 | truck | 1.290,4 | mijnweg → Ruta 5 → Chañaral → Copiapó-bypass → Vespucio Norte → Osvaldo Croquevielle; 15.977 punten |
| b2 | truck, **stippel** | 0,15 | SCL-vrachtplatform, airside/privéterrein |
| b3 | lucht | 11.863,2 | SCL → MXP grootcirkel, 476 punten, doorgetrokken |
| b4 | truck | 76,0 | letterlijke omgekeerde kopie van `goud-argor-mumbai-weg-argor-mxp.geojson` (coördinaten omgekeerd, van/naar en snaps gewisseld) |

**Toets:** b1 1.290,4 km tegen indicatie 1.293 (−0,2%) en hemelsbreed 1.008,6 (omwegfactor 1,28); dit is een indicatie, geen ±15%-norm, want er is geen gepubliceerde wegkm voor het hele been. Segmenten: mijnweg + Ruta 5 tot via 2 47,9 (waarvan 38,3 km kleine klasse unclassified/service) · 125,2 · 174,7 · 151,6 (Chañaral → Copiapó-bypass) · 305,6 · 249,7 · 165,7 · 65,1 · 5,0; het gemeten stuk plant → Copiapó-bypass is 499,4 km (brief: 501,6 inclusief 1,5 km service). Via-snaps allemaal ≤ 0,01 km. Naad 0 tussen alle benen, markers op 0,0 km van hun lijn. `toets_knikken`: 8 knikken op het Chileense been (3 echte scherpe bochten rond de Vespucio-oprit en SCL, 5 spikes van 5 tot 17 m), 0 terugloop; de 32 knikken op b4 zijn die van de gekopieerde bron. `toets_rechte_benen --min-km 5` noemt deze stroom niet (beide stippels < 5 km).

**Afwijkingen van de brief:**
- **Extra stippel b0 (plant → mijnweg).** De scan met het plant-anker als eerste via-punt gaf "geen wegpad tussen punt 0 en 1": de plant snapte op een andere tak (way 112893890, 0,68 km) omdat de verbinding naar de westelijke mijnweg uit OSM-way 1041555126 (unclassified, paved, **access=no**, 6 knopen) bestaat en door het wegfilter valt (`WEG_ACCESS_WEG = {private, no}`), net als de service-plantwegen 112893889/910151870 (ook access=no). Gevonden via de OSM-API (`/api/0.6/map?bbox=…`). Oplossing: b1 begint op OSM-knoop 1282090468 (way 112891152, −24.4104, −69.5089, een bestaand vertex), b0 is een rechte stippel "last mile (geen net op deze korrel — plantwegen access=no)" van 1,29 km.
- **Het fallbackpunt uit de brief (−24.4137, −69.5029) is NIET gebruikt**: dat punt ligt op de NE-tak (way 112893890), waarvan de samenhangende component alleen noordwaarts de Ruta Minera/B-55 bereikt (nooit Ruta 5). Brief §7 en de bak-aanwijzing moeten daarop gecorrigeerd worden.
- Brief-nuance: de AIF-bronwaarde 165 km (mijn → Antofagasta) is dus niet af te lezen aan b1; de mijnweg naar Ruta 5 is 38,3 km kleine klasse, daarna Ruta 5.

**Recept:** `maak_luchtbeen.py --van "Santiago SCL vrachtterminal|-33.4105,-70.7874" --naar "Malpensa Cargo City Sud MXP|45.6142,8.7186"`; weg-slot1 + `wegscan_puur.py --profiel goud-elpenon-argorheraeus-plant-scl` (chili, ~65 s, 117.750 ways; extract-cache hergebruikt bij de tweede run); b4 met een klein python-script uit `goud-argor-mumbai-weg-argor-mxp.geojson`; zwaar-slot1 + `bash v2/tools/bak_stromen.sh goud-elpenon-argorheraeus`.

**Lessen:** (1) een anker op een access=no-plant (Pan American Silver-sites, Codelco-achtige terreinen) vraagt altijd een eerste openbare knoop plus een stippel; zoek de verbindingsway met de OSM-API in een kleine bbox rond het anker, niet door via-punten te verschuiven. (2) Een brief-fallbackcoördinaat die niet getoetst is op samenhang met het net (hier de NE-tak) is geen fallback; toets met een component-analyse op de `pbfways`-cache. (3) Bestand 384 KB: boven de 300 KB-richtlijn door het lange Chileense been (15.977 punten); noot, geen herbak.

**Open:** Argor blijft een aanname (AIF noemt ook MKS PAMP); El Peñón (3,6 t/j) ontbreekt nog in `goud-sitelaag.json` (centraal); SCL-loods onzeker (hergebruikt); ANF-vrachtanker niet te leggen; binnenlandse mijnwegen B-905/B-895/C-17 (±45 km korter) niet gebrond en niet gekozen.
