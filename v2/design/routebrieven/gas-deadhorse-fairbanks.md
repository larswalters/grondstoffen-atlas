# Routebrief (licht) · gas — Deadhorse (Alaska North Slope) → Dalton Highway → Fairbanks (VS)

**stroom-id:** `gas-deadhorse-fairbanks` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) ·
**status:** gebakken
**Keten in één zin:** Aardgas uit Prudhoe Bay (Hilcorp) wordt in de LNG-fabriek van Harvest Midstream bij Deadhorse vloeibaar gemaakt en in tankwagens van ca. 14.000 gallon
over de Dalton Highway (AK-11) en de Elliott Highway (AK-2) naar de LNG-opslag van Interior Gas Utility (IGU) aan de zuidkant van Fairbanks gereden. Eén landbeen, de enige gasketen
over de weg in de atlas; de tekening stopt bij de opslagtank.
**Welke as van het verhaal:** *Gas zonder pijp: de Arctische tankwagen* — Fairbanks heeft geen gasleiding naar de bron, dus gaat het gas als LNG 800 km over een grind- en asfaltweg.
Volume: **indicatief 0,006 bcm/j** — 3–4 tankwagens per week van ca. 14.000 gal [1], dat is 2,5 Mgal/j ≈ 5,8 Mm³ gas (1 gal LNG ≈ 2,27 m³ gas, eigen rekensom), peil feb 2026, start okt 2025 [1][5].
Fabriekscapaciteit 150.000 gal/dag ≈ 0,12 bcm/j [1][4] is geen doorzet; het werkelijke volume is ~5% daarvan.

## 1 · Ketenkaart
```
LNG-fabriek Harvest Midstream, pad naast de Spine Road, Deadhorse/Prudhoe Bay `gas-deadhorse-lng` (plek onzeker: Spine Road-vertex, geen fabriek gezien)
  ──(b1 truck · Dalton Highway AK-11 + Elliott Highway AK-2 · 806 km eigen routering / ca. 805 km gepubliceerd, doorgetrokken)──►
IGU-LNG-opslag (5,25 Mgal-tank, zuidkant Fairbanks) `gas-fairbanks-igu` — stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gas-deadhorse-lng` → `gas-fairbanks-igu` | Spine Road → Dalton Highway (AK-11, 666 km) → Elliott Highway (AK-2) → Steese Expressway → zuid-Fairbanks | **806,3** (haalbaarheidsrun, eigen routering, geen OSM-km); gepubliceerd ca. 500 mijl = ca. 805 km [1], +0,2%; Wikipedia: Dalton 666 km [8] + Elliott Dalton-aansluiting → Fox ca. 116 km (152 mi totaal − 80 mi onverhard [9]) + Fox → Fairbanks 16 km ≈ 798 km + laatste kilometers door de stad | `maak_stroombeen_weg.py` (extract `us-alaska`, nieuw profiel) | nee |

Geen stippel: de weg is doorlopend OSM-bekend, beide ankers liggen binnen 0,04 km (kop) en 0,17 km (staart) van een gekarteerde weg; geen last-mile-been (< 2 km).
Lengtetoets ±15%: tegen **805 km** (500 mijl [1]) en tegen de Wikipedia-som van ca. 798 km (zie hierboven). De gepubliceerde 500 mijl is een tijdschriftgetal, geen operator-wegkm.
Tankwagenroute is per bron de Dalton Highway [1][2]; KUAC meldde een IGU-tankwagen met 14.000 gal LNG die in 2026 bij Dalton-mijl 126 verongelukte (uit de haalbaarheidstoets, niet zelf geopend): de route is in gebruik.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-deadhorse-lng` | LNG-fabriek (kop) | Harvest Midstream North Slope LNG-plant, "bij Deadhorse", op een pad naast de Spine Road | 70.2465, -148.3990 | [1][4][5][6][10] | **onzeker**: de fabriek zelf is niet gevonden. Het punt is een OSM-vertex op de **Spine Road** (way 8987826, 36 m); z15 gezien: grindweg door toendra, geen LNG-installatie op het beeld (Esri is ouder dan de bouw 2023-25). Een latere persmelding noemt het pad bij Pump Station 1 (≈ 8 km westelijker, 70.2551, -148.6210) [6]. De lijn begint dus op de Spine Road, niet op de fabriek. |
| `gas-fairbanks-igu` | LNG-opslag (staart, stoppunt) | IGU-opslagtank, zuidkant Fairbanks (5,25 Mgal, gebouwd 2019) | 64.8044, -147.7992 | [7][1][10][11] | **aannemelijk**: bron zegt alleen "zuidkant van de stad" [7]; OSM kent op dit pad één `man_made=gasometer` (way 1280508173, centroïde 64.80439, -147.79917, naast "Gas Court"); z16 gezien: omheind pad met witte koepeltank van ca. 36 m, laadbuizen en bijgebouwen, Tanana-rivier 400 m zuidelijker. Geen bron noemt dit adres. |

Hergebruik: geen. De sitelaag `gas-sitelaag.json` heeft geen Alaska-site; `ol-prudhoe-ps1` (70.2563, -148.6194, brief `olie-prudhoebay-cherrypoint`) is een olieleiding-anker en wordt niet overgenomen. Het IGU-kantoor (64.8462, -147.7810, Photon/OSM) is **geen** opslag en geen anker.
Niet getekend: de Hilcorp-gasleiding naar de fabriek (geen OSM-leiding, geen bron) en twee kleinere IGU-opslagen (150.000 gal bij North Pole, plek niet gevonden).

## 4 · Via-punten (b1, lat, lon, reisvolgorde)
Eén doorgaande weg: er is geen corridorkeuze op de Dalton Highway; de via-punten bewaken alleen de routering (venster) en liggen op de weg (OSM-afstand in haakjes).
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 0 | kop (anker) Spine Road | 70.2465, -148.3990 | begin op de Spine Road bij Deadhorse (36 m) |
| b1 | 1 | Coldfoot, Dalton Hwy | 67.2544, -150.1776 | Brooks Range-doorgang, midden van de 666 km (AK 11, 1 m) |
| b1 | 2 | Yukon-rivierbrug, Dalton Hwy | 65.8787, -149.7185 | enige oeverovergang van de Yukon (AK 11, 5 m) |
| b1 | 3 | Dalton Hwy zuideinde / Elliott Hwy | 65.4906, -148.6613 | overgang naar de Elliott Highway (AK 11, 3 m); route daarna AK-2 → Steese Expressway; geen via in Fairbanks centrum |
| b1 | 4 | staart (anker) IGU-opslag | 64.8044, -147.7992 | 0,17 km van "Tanana Levee"/"Tria Road" (unclassified) |

Profiel (lon, lat in `PROFIELEN`): extract `us-alaska`, `corridorKlassen: ["tertiary","unclassified"]` (haalbaarheidsrun: nodig voor de Spine Road en de laatste km), `vensterKm: 40`, optioneel `refs: ["AK 11","AK 2"]`, `gepubliceerdKm: 805`.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| LNG-fabriek Deadhorse | Harvest Midstream (Hilcorp), commercieel sinds okt-dec 2025 | Prudhoe Bay-gas (CO2-verwijdering, stikstoflus) → LNG | 150.000 gal/dag; voedingsgas ca. 15 MMcf/d | [1][4][5] |
| IGU-opslag Fairbanks | Interior Gas Utility (leveringsovereenkomst 2023, 20 jaar + 2×5) | LNG → opslag/verdamping → leidingnet (Fairbanks 150 mijl, North Pole 85 mijl) | drie opslaglocaties samen 5,5 Mgal (grote tank 5,25 Mgal) | [1][7] |

## 6 · Stoppunt
De tekening stopt bij de IGU-opslagtank in Fairbanks: de volgende stap is verdamping en distributie door het eigen IGU-leidingnet van 235 mijl [1], geen gedocumenteerde externe locatie; dus geen fase D/E. Verhaal in één zin: "een stad zonder gasleiding krijgt zijn gas per tankwagen van de Noordpoolkust".

## 7 · Open punten
- **De LNG-fabriek is niet gevonden.** OSM kent hem niet (pyosmium-scan us-alaska bij Prudhoe, ook geen "Alyeschem"/"Harvest"), de Esri-opname is ouder dan de bouw, en de bronnen zeggen "bij Deadhorse" [1][4][5] en "pad naast de Spine Road, later bij Pump Station 1" [6]. Kop = Spine Road-vertex, onzeker; de werkelijke plek kan ca. 10 km westelijker liggen (±1%, geen effect op de 806 km).
- **Persmelding [6] is een zoekresultaat, niet zelf geopend** (Petroleum News gaf HTTP 403); de Pump Station 1-claim is dus een lead, geen bron.
- **IGU-opslag identiteit:** de gasometer-tank is aannemelijk, niet bevestigd; bronnen noemen geen adres, ook niet voor de twee andere opslagen (North Pole, ca. 150.000 gal) [7].
- **Eigen km van 806,3 komt uit de haalbaarheidsrun** met staart 64.8047, -147.7996 (200 m van een track); met het hier gekozen anker (64.8044, -147.7992, 166 m) kan het getal enkele honderden meters verschillen; bak-agent meet opnieuw.
- **Volume is indicatief:** 3–4 tankwagens/week uit één tijdschriftbron; PGJ noemt "ruim 8 MMcf/d" leveringen (capaciteit, ≈ 0,08 bcm/j) [5], daar is geen operatorcijfer voor het werkelijke jaar.
- **Via 3 en 2 en 1** zijn de waarden uit de haalbaarheidsrun, elk op een OSM-vertex van AK 11 (1–5 m); de brief voegt geen via-punten toe omdat de Dalton Highway geen alternatief heeft.

## 8 · Bronnen
[1] AK Business Magazine, "Energy on the Move", feb 2026 — fabriek tot 150.000 gal LNG/dag, 14.000 gal per tankwagen, 3–4 per week, 500 mijl Dalton Highway, eerste lading okt 2025, IGU 3 opslagen 5,5 Mgal. https://digital.akbizmag.com/issue/february-2026/energy-on-the-move/
[2] KUAC, "Interior Gas Utility nearing start for North Slope natural gas haul", 2025-08-08 — Dalton Highway, doel start 1 sep 2025, 150.000 gal/dag. https://fm.kuac.org/2025-08-08/interior-gas-utility-nearing-start-for-north-slope-natural-gas-haul
[3] KUAC, "IGU to buy first commercial North Slope LNG", 2023-01-18 — 150.000 gal/dag, Harvest Midstream, Titan-fabriek Cook Inlet als oude bron. https://fm.kuac.org/energy-and-environment/2023-01-18/igu-to-buy-first-commercial-north-slope-lng-to-support-growth-in-interior
[4] NS Energy, "Harvest and IGU announce partnership to deliver LNG to Fairbanks", 2023 — bij Deadhorse, voedingsgas ca. 15 MMcf/d uit Prudhoe Bay, ca. 500 mijl truck. https://www.nsenergybusiness.com/news/harvest-and-igu-announce-partnership-to-deliver-lng-to-fairbanks/
[5] Pipeline & Gas Journal, "Harvest Midstream, IGU deliver first LNG from Alaska's North Slope to Fairbanks", okt 2025 — "bij Deadhorse", ruim 8 MMcf/d. https://pgjonline.com/news/2025/october/harvest-midstream-igu-deliver-first-lng-from-alaska-s-north-slope-to-fairbanks
[6] Petroleum News (2023–25, via zoekresultaat; pagina niet te openen, HTTP 403) — pad naast de Spine Road gedeeld met Alyeschem, later bij Pump Station 1. https://petroleumnews.com/pnarchpop/65471709.shtml
[7] KUAC, "Big LNG storage tank will enable utility to expand system", 2019-10-10 — 5,25 Mgal-tank "aan de zuidkant van de stad". https://fm.kuac.org/business/2019-10-10/big-lng-storage-tank-will-enable-utility-to-expand-system-attract-customers-gm-says
[8] Wikipedia, "Dalton Highway" — 414 mi (666 km), begint bij de Elliott Highway, eindigt bij Deadhorse. https://en.wikipedia.org/wiki/Dalton_Highway
[9] Wikipedia, "Elliott Highway" — 152 mi vanaf Fox (10 mi N van Fairbanks), laatste 80 mi onverhard na de Dalton-aansluiting. https://en.wikipedia.org/wiki/Elliott_Highway
[10] OpenStreetMap (ODbL), Geofabrik us-alaska, opgehaald 2026-10-31: Spine Road way 8987826 (secondary, unpaved), Dalton Highway AK 11 (way's 9000339, 9000350, 36768037), gasometer way 1280508173, "Gas Court".
[11] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-gas-deadhorse-fairbanks-{kop,igu-opslag,deadhorse,igutank,fbxzuid,ps1,spinemid,spinepad}.png` en `-wbspine-wb43291.png` (Wayback 2026-10-29: zelfde opname als live).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Uitvoer:** `v2/data/stroomroute-gas-deadhorse-fairbanks.json` (166,3 KB, contract versie 2, lonlat) · 1 been · 808,3 km · 7.778 punten · 2 markers · geen stippel, geen naad (één been).

| # | modaliteit | km gemeten | km bron | afwijking | naam |
|---|---|---|---|---|---|
| b1 | truck | 808,3 | ca. 805 km (500 mijl, AK Business Magazine); Wikipedia-som ca. 798 km | +0,4% (tegen 805), +1,3% (tegen 798) | LNG per tankwagen (14.000 gal) Harvest-fabriek Deadhorse → IGU-opslag Fairbanks (kop onzeker) |

**Recept:** `bash v2/tools/bak_stromen.sh gas-deadhorse-fairbanks` (functie `bak_gas_deadhorse_fairbanks`). b1 = vooraf gescande weg: `python v2/tools/wegscan_puur.py --profiel gas-deadhorse-fairbanks-deadhorse-fairbanks` (extract us-alaska, refs AK 11 en AK 2, `corridorKlassen` tertiary/unclassified, vensterKm 40, 3 via-punten) naar `gas-deadhorse-fairbanks-weg-deadhorse-fairbanks.geojson`, als `--been-geojson truck`. Segmenten: Spine Road → Coldfoot 392,3 · → Yukon-brug 191,2 · → Dalton-zuideinde 89,2 · → IGU 135,4 km; snaps 0,00-0,17 km. Markers: gas-deadhorse-lng 70.2465,-148.3990 en gas-fairbanks-igu 64.8044,-147.7992 (beide 0,0 km van de lijn).

**Toelichting:** geen stippel, geen haven-aanloop, geen vlucht, geen leiding, geen kopie. De kop is een Spine Road-vertex (onzeker): de lijn begint op de weg, niet op de niet-gevonden fabriek. De staart eindigt na 0,17 km rechte ankerverbinding op de IGU-tank; last mile in de stad 3,75 km over kleine klassen. Toets: json.load ok, versie 2, punt_formaat lonlat, modaliteit truck, 7.778 punten. `toets_knikken.py`: 6 knikken >= 60 graden, 0 omkeringen, 0 terugloop (spikes van enkele tot 126 m bij de uiteinden, geen repareerbare lus). `toets_rechte_benen.py`: been niet genoemd. Bestand 166 KB, onder de 300 KB.

**Lessen:** (1) de eigen km komt 1,8 km hoger uit dan de haalbaarheidsrun (806,3) door het gekozen staartanker 166 m verder; binnen de norm; (2) profiel en scan waren in één run klaar (us-alaska 144 MB, 11 s scan); (3) een bak-run vraagt alleen een weg-slot voor de scan en een zwaar-slot voor de bake.
