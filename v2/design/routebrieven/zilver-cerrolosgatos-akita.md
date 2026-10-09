# Routebrief (licht) · zilver — Cerro Los Gatos → Manzanillo → Akita (Japan)

**stroom-id:** `zilver-cerrolosgatos-akita` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken
**Keten in één zin:** zinkconcentraat met betaalbaar zilver van de Cerro Los Gatos-molen (Chihuahua) per **truck**
(~1.450 km, geen gepubliceerd tracé) naar het Hazesa Terminal in de binnenhaven van Manzanillo, per **zeeschip** via de
Tsugaru-straat naar de Japanse Zee-kust (11.100 km, gemeten), en over eigen terrein naar de Dowa-smelter Akita Seiren
Iijima — **stoppunt** (de smelter is de bestemming van het ontwerp; geen fase D/E).
**Welke as van het verhaal:** *Mexicaans zilver-bijproduct naar een Japanse zinksmelter* — CLG maakte 9,2 Moz = **286 t Ag/j**
(2023, 10-K FY2023 [1]); Dowa (30% LGJV-partner) heeft recht op **100% van het zinkconcentraat** [1][2]. Welk deel van die 286 t
via Akita loopt is niet gepubliceerd (geen volumeclaim voor deze lijn); lood-zilverconcentraat gaat DAP naar Manzanillo en elders heen [3].

## 1 · Ketenkaart
```
CLG-molen `ag-clg-molen` ──(b1 truck · toegangsweg → Fed 24 → Parral → Jiménez → Torreón → Río Grande → Aguascalientes →
   Guadalajara → Colima · hemelsbreed 963 km, geen wegkm; indicatie 1.450 km, aannemelijk)──► Hazesa Terminal `ag-manzanillo-hazesa`
   ──(b2 zee · haven-aanloop Manzanillo, stippel, KOPIE penasquito-onsan · 154,2 km)──► zeeknoop 4859
   ──(b3 zee · MARNET, Grote Oceaan + Tsugaru · 11.099,6 km gemeten)──► zeeknoop 6468 (Akita)
   ──(b4 zee · haven-aanloop Akita, stippel · 8,3 km)──► `ag-akita-kade` ──(b5 truck · last mile, stippel · 0,4 km)──► `ag-akita-smelter` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | CLG-molen → Hazesa Terminal Manzanillo | toegangsweg (40 km verhard, TRS [4]) → MEX 24 → MEX 45 → MEX 49D/49 → MEX 40D → MEX 49/45D → MEX 45/80D → MEX 54D → MEX 110/200D; aannemelijk, geen gepubliceerd tracé | hemelsbreed 963 km, geen wegkm; indicatie route-planner OSRM 1.450 km (OSM-gebaseerd, niet onafhankelijk [8]); toegangsweg ca. 47 (TRS 40 + ~7) | maak_stroombeen_weg, 2 profielen: b1a molen→Fed 24, b1b Fed 24→Hazesa | nee |
| b2 | B | zee (aanloop) | Hazesa-zijde Manzanillo → zeeknoop 4859 (17.9840, -103.4033) | schematisch, over water | 154,2 [gemeten, zilver-penasquito-onsan b2; Hazesa-punt zelf 154,2] | LETTERLIJKE KOPIE stippel uit `bak_zilver_penasquito_onsan` | ja — net reikt niet (kade > 5 km van zeeknoop) |
| b3 | B | zee | zeeknoop 4859 → zeeknoop 6468 (39.7072, 140.0070) | Grote Oceaan, Tsugaru-straat (16 km van het gemeten punt 41.52/140.35) | 11.099,6 [gemeten, hecht_marnet 2026-10-09]; hemelsbreed 10.679 | MARNET | nee |
| b4 | B | zee (aanloop) | zeeknoop 6468 → Akita-kade (39.7745, 140.0480) | schematisch, rivier-/havenbekken Akita | 8,3 [gemeten hemelsbreed; rechte lijn snijdt ~1,4 km 1:10M-land] | maak_havenaanloop.py (timeout 300), terugval rechte stippel | ja — net reikt niet (> 5 km regel) |
| b5 | C | truck | Akita-kade → smelter | eigen terrein, tankpark aan de kade | 0,4 [hemelsbreed] | stippel last mile | ja — site < 2 km, geen net op deze korrel |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-clg-molen` | mijn + molen (laad) | Cerro Los Gatos-molen (LGJV), Satevó, Chihuahua | 27.5392, -106.3340 | [1][4][9] | bron-gelegd (z16 gezien: concentrator met drie witte hallen en een koepeltank naast de enorme tailingsdam; het TRS-districtmidden 27.5714,-106.3592 ligt 3,7 km NW in leeg heuvelland en is dus geen anker) |
| `ag-manzanillo-hazesa` | overslag (bulkterminal) | Hazesa Terminal, binnenhaven Manzanillo | 19.0826, -104.2952 | [2][7][9] | bron-gelegd (z17 gezien: vier grote bulkloodsen op de oostpier van het binnenbekken; OSM-node HAZESA wholesale, contract: FCA Hazesa Terminal via TMC-warehouse) |
| `ag-manzanillo-timsa` | startpunt van de b2-kopie, GEEN marker | binnenhaven Manzanillo (containerkade westzijde) | 19.0810, -104.2975 | zilver-penasquito-onsan §3 | hergebruikt letterlijk; z16 gezien: containerkade met portaalkranen, 0,30 km van Hazesa over het water |
| `ag-akita-kade` | losplek | kade aan het Iijima-havenbekken, Akita | 39.7745, 140.0480 | [6][9] | aannemelijk (z16 gezien: kademuur direct onder het smeltercomplex met witte tanks; geen bron noemt deze kade) |
| `ag-akita-smelter` | smelter (stoppunt) | Akita Seiren Iijima-smelter (Dowa) | 39.7770, 140.0508 | [2][6][9] | bron-gelegd (z15 gezien: groot industriecomplex met blauwe hallen en tankparken, OSM way 341478005) |

## 4 · Via-punten (alleen b1b, Fed 24 → Hazesa; b1a heeft er geen: één toegangsweg)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1b | 1 | Fed 24-aansluiting (kop b1b) | 27.7099, -106.0605 | toegangsweg komt op MEX 24 (TRS: Fed 24 km 81); keuze noord naar Chihuahua of zuid naar Parral [4] |
| b1b | 2 | Parral, MEX 45 | 26.9334, -105.6364 | MEX 24 → MEX 45 oostelijk van de stad; pint Parral–Jiménez tegen de Chihuahua-route |
| b1b | 3 | Jiménez, MEX 49D | 27.0986, -104.8651 | begin tolweg Jiménez–Torreón (MEX 49D) tegenover de vrije MEX 49 |
| b1b | 4 | Gómez Palacio, MEX 40D/49D | 25.6206, -103.5220 | aansluiting aan de rand van de Laguna-conurbatie, niet het centrum |
| b1b | 5 | Río Grande, MEX 49 | 23.8448, -103.0172 | MEX 49 Cuencamé–Río Grande–Fresnillo tegenover Durango-routes |
| b1b | 6 | Aguascalientes-noord, MEX 45 | 22.0367, -102.2812 | **corridorkeuze**: via Aguascalientes–Lagos (MEX 45/80D) en niet via Zacatecas–Jalpa–MEX 54 (route penasquito) |
| b1b | 7 | Guadalajara-zuidwest, MEX 54D | 20.4273, -103.5536 | begin autopista Guadalajara–Colima (omzeilt de stad) |
| b1b | 8 | Colima-zuid, MEX 110 | 19.2129, -103.7222 | laatste knooppunt vóór MEX 200D naar Manzanillo; buiten het centrum |

Alle acht liggen volgens OSRM-snap 1–6 m van een weg [8]; de bak-agent controleert met de snap van maak_stroombeen_weg (> 5 km = fout gelegd).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Akita Seiren Iijima | Dowa-groep (volgens contract) | zinkconcentraat (Mexico e.a.) → zink + bijproducten, betaalbaar Ag terug | niet gevonden | [2][6] |

## 6 · Stoppunt
De brief stopt bij de Akita Seiren Iijima-smelter: het ketenontwerp noemt geen vervolgstap, de smelter is de bestemming van het
zinkconcentraat-contract, en een afnemer van het zilver na Akita is niet gedocumenteerd (geen fase D/E).

## 7 · Open punten
- **Zilver zit vooral in het loodconcentraat (aanname, geen bron):** deze keten volgt het zinkconcentraat (contract: Ag deduct en pay op LBMA, percentages geredigeerd [2]); loodconcentraat 2024 gaat DAP Impala Terminals Manzanillo naar Trafigura, bestemming open [3]. **Aannemelijk: één bron** voor Akita: contract 2019 (looptijd t/m 30-6-2022, verlengbaar) plus 10-K FY2023 [1] en de JV-wijziging van 19-12-2024 die Dowa's zinkrecht versterkt [5]; geen 2025-bron voor zendingen na de overname door First Majestic (16-1-2025).
- **Wegtracé niet gepubliceerd.** Geen echte wegkilometer voor Fed 24 → Manzanillo: hemelsbreed 963 km (via-punten 1.258 km), geen wegkm; OSRM 1.450 km is dezelfde OSM-bron als de bake, dus de ±15%-toets geldt als indicatie en niet als norm. Alleen de toegangsweg heeft een bedrijfsopgave (40 km, TRS [4]). Staart Zacatecas–Colima wijkt af van penasquito b1 (andere corridor via Aguascalientes).
- **Toegangsweg is geen hoofdweg:** OSM klasse unclassified/tertiary [8]; b1a heeft `corridorKlassen ["tertiary","unclassified"]` nodig met klein venster, b1b niet.
- **Manzanillo-naad 0,30 km:** b1 eindigt op Hazesa (oostpier), de b2-kopie begint op de containerkade 0,30 km west over het water; onder de 5 km-norm, kopie blijft letterlijk.
- **Akita-kade niet bron-genoemd;** aanloop b4 haalde 300 s eerder niet (feasibility), dan rechte stippel met reden; die snijdt ~1,4 km 1:10M-land.
- **Sitelaag:** `w-ref-japan` (34.9, 136.6) is een centroïde van Mitsubishi/Dowa, niet Akita; Akita Iijima en CLG ontbreken in `zilver-sitelaag.json` (niet gewijzigd).

## 8 · Bronnen
[1] Gatos Silver, 10-K FY2023 — 9,2 Moz Ag 2023 (10,3 in 2022); Dowa 30% en recht op 100% zinkconcentraat. https://www.sec.gov/Archives/edgar/data/1517006/000162828024005761/gato-20231231.htm
[2] Zinkconcentraatcontract Ocean Partners USA – Operaciones San Jose de Plata, 15-7-2019 (Exhibit 10.9.1): FCA Hazesa Terminal Manzanillo via TMC-warehouse, vracht tot CIF FO Akita, 100% naar Dowa Iijima, Ag-aftrek en betaling op LBMA. https://www.sec.gov/Archives/edgar/data/1517006/000104746920005064/a2242423zex-10_91.htm
[3] Loodconcentraatcontract 697715-P (Trafigura México), 11-1-2024: DAP Impala Terminals Manzanillo, km 1,5 Carretera Manzanillo–Minatitlán. https://www.sec.gov/Archives/edgar/data/1517006/000162828024005761/a2024leadcontractredacte.htm
[4] Gatos Silver, Technical Report Summary CLG (Exhibit 96.1, 2022): 27°34'17"N 106°21'33"W, Fed 24 km 81 + 40 km verharde weg naar San José del Sitio, geen spoor nabij. https://sec.gov/Archives/edgar/data/1517006/000095010322019538/dp184025_ex9601.htm
[5] Gatos Silver, amended JV agreements met Dowa (19-12-2024) en First Majestic-overname (16-1-2025). https://www.barchart.com/story/news/30141116/gatos-silver-amends-joint-venture-agreements-with-dowa-to-obtain-enhanced-management-rights-and-announces-financial-statement-consolidation
[6] OpenStreetMap/Nominatim — 秋田製錬飯島製錬所 (industrial way 341478005, 39.7770/140.0508). https://nominatim.openstreetmap.org/search?q=秋田製錬+飯島製錬所&format=json
[7] OpenStreetMap/Nominatim — HAZESA, Manzanillo (node 12026914279, 19.0826/-104.2952). https://nominatim.openstreetmap.org/search?q=Hazesa+Manzanillo&format=json
[8] OSRM demo-router (OSM-gebaseerd route-planner, 2026-10-09) voor via-punten en indicatie 1.450 km; Nominatim reverse voor wegklasse toegangsweg. https://router.project-osrm.org
[9] Esri World Imagery via `v2/tools/sat_check.py` (z15–z17): `v2/build-cache/satcheck/sat-zilver-cerrolosgatos-akita-molen-z16.png`, `-hazesa.png`, `-manzanillo.png`, `-kade.png`, `-smelter.png`, `-wide.png`.
[10] Eigen controle `hecht_marnet.py route`, zeeknoop 4859 → 6468: 11.099,6 km, 53 MARNET-edges via Tsugaru; zeeknopen via `marnet_zee` (6468 op 8,3 km van de kade).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
`v2/data/stroomroute-zilver-cerrolosgatos-akita.json` · 245,9 KB · 12.698,4 km · 6 benen · 4 markers · versie 2, lonlat, modaliteiten truck/zee. Recept: `bash v2/tools/bak_stromen.sh zilver-cerrolosgatos-akita` (functie `bak_zilver_cerrolosgatos_akita`; profielen `zilver-cerrolosgatos-akita-molen-fed24` en `-fed24-hazesa`, wegscan via `wegscan_puur.py` op de mexico-extract).

| # | modaliteit | km | naad | toelichting |
|---|---|---|---|---|
| b1a | truck | 42,9 | 0 | molen → Fed 24, doorgetrokken; brief ca. 47 (TRS 40 + ~7): -8,7%, binnen ±15%. Molen ligt 0,72 km van de dichtstbijzijnde OSM-weg (rechte ankerverbinding, door het tool als bevinding gemeld); eerste 42 km over tertiary/unclassified |
| b1b | truck | 1.393,0 | 0,00 | Fed 24 → Hazesa, 8 via-punten, alle snaps ≤ 0,1 km; indicatie OSRM 1.450: -3,9% (indicatie, geen norm: geen gepubliceerde wegkm); geen segment met omweg (Jiménez–Gómez Palacio 218,6 km tegen ~210 hemelsbreed) |
| b2 | zee, stippel | 154,2 | 0,30 | LETTERLIJKE KOPIE van de stippel in `bak_zilver_penasquito_onsan` (containerkade → zeeknoop 4859); naad met Hazesa 0,30 km over water, onder de norm |
| b3 | zee | 11.099,6 | 0,00 | MARNET zeeknoop 4859 → 6468 via de Tsugaru-straat; gelijk aan de eerder gemeten 11.099,6 km |
| b4 | zee, stippel | 8,3 | 0,00 | haven-aanloop Akita: `maak_havenaanloop.py` haalde `timeout 300` niet (exit 124), geen tweede poging; rechte stippel, kade 8,3 km van de zeeknoop (> 5 km) |
| b5 | truck, stippel | 0,4 | 0,00 | last mile kade → smelter, binnen de 2 km-drempel, geen net op deze korrel |

Markers (alle 4 op hun lijn, 0,0 km): CLG-molen, Hazesa, Akita-kade (aannemelijk), Akita Seiren Iijima (stoppunt). `ag-manzanillo-timsa` is bewust geen marker (startpunt van de kopie).

**Toets.** Geen naad > 5 km (max 0,30 km). `toets_knikken.py`: 27 knikken, 0 terugloop; de 22 op b1b zijn spikes van enkele meters tot 61 m op knooppunten (Manzanillo-haven, Guadalajara, Aguascalientes), de enige 164 graden-bocht (27.7099, -106.0605) is de verbinding b1a/b1b op het Fed 24-via-punt, ca. 30 m overschot. `toets_rechte_benen.py`: alleen de twee zee-stippels (b2, b4) met omwegfactor 1,00; beide hebben reden in de naam.

**Lessen / bevindingen.** (1) De wegscan van de mexico-extract duurde 292 s (11.214 blokken) en zit nu in de cache. (2) De Akita-aanloop is voor de tweede keer een stippel geworden: de rechte lijn snijdt ca. 1,4 km 1:10M-land; een centrale kade-aanloop met een fijner kustbestand zou dit oplossen. (3) De bestemming Akita blijft "aannemelijk: één bron" (Dowa-zinkcontract 2019, geen 2025-bron); zilver zit mogelijk vooral in het loodconcentraat (aanname, §7). (4) Sitelaag niet gewijzigd: `w-ref-japan` is een centroïde, Akita Iijima en CLG ontbreken.
