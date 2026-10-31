# Routebrief (licht) · grafiet — Lake Charles → Brunswick County (VS)

**stroom-id:** `grafiet-lakecharles-brunswick` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** groene en gecalcineerde naaldcokes (géén grafiet) uit de specialty coker/calciner van de Phillips 66 Lake Charles Manufacturing Complex (Westlake, Louisiana) gaat per **truck** (werkaanname, modaliteit niet gebronnet) over I-10 → I-65 → I-85 → I-285 → I-20 → I-95 → US-74/76 naar het Mid-Atlantic Industrial Rail Park in Brunswick County (NC), waar Epsilon Advanced Materials een anodefabriek van 30 kt/j wil bouwen.
**Welke as van het verhaal:** *de ex-China buildout, synthetisch, Zuid-oost-corridor.* P66 en Epsilon tekenden op 2025-09-24 een **Agreement in Principle on Key Terms** (geen definitief contract) voor levering van green en calcined needle coke uit Lake Charles aan de NC-fabriek van **30.000 t graphite active anode material (AAM)/j, start 2027, uitbreiding 60.000 t in 2030** [1]. **Jaarvolume vandaag: 0 kt**; gepland 30 kt grafiet-AAM/j (peiljaar 2027, [1]); cokesvolume (kt in) is niet gepubliceerd. De 2027-start is onzeker: groundbreaking opnieuw uitgesteld naar "late 2026" [5] en de Golden LEAF-subsidie vraagt pas uiterlijk 2027-03-31 een bevestiging dat het project doorgaat [6]. Daarom draagt het been **(aannemelijk: één bron, modaliteit niet gebronnet; naaldcokes, geen grafiet; fabriek nog niet gebouwd)** in de naam.

## 1 · Ketenkaart
```
P66 Lake Charles, cokesveld `gr-lakecharles-cokes` ──(b1 truck · US-90 → I-10 → I-12 → I-10 → I-65 → I-85 → I-285 → I-20 → I-95 → I-74/US-74/76 · hemelsbreed 1.487 km, geen wegkm · aannemelijk: één bron)──►
   Epsilon-fabriek, Mid-Atlantic Industrial Rail Park `gr-brunswick-fabriek` (30 kt AAM/j gepland, 2027) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (werkaanname; spoor niet uitgesloten, §7) | `gr-lakecharles-cokes` → `gr-brunswick-fabriek` | I-10 O → I-12 (Baton Rouge–Slidell) → I-10 O (Mobile) → I-65 N → I-85 (Montgomery) → I-285 ZO-Atlanta → I-20 O → I-95 N (Florence) → I-74/US-74 → US-74/76 | hemelsbreed 1.487 km, geen wegkm (OSRM-indicatie 1.691, geen publicatie [11]) | maak_stroombeen_weg (profiel `grafiet-lakecharles-brunswick-lakecharles-brunswick`; kop op privé-terreinwegen → `eindToegangPrivaat`) | nee — *aannemelijk: één bron; modaliteit niet gebronnet; naaldcokes, geen grafiet* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-lakecharles-cokes` | feedstock / laadplek (cokesveld bij de coker) | Phillips 66 Lake Charles Manufacturing Complex, Westlake LA | 30.2420, -93.2770 | [2][8] | hergebruik letterlijk uit `grafiet-lakecharles-desoto.md` (bron-gelegd, z15/z16: zwart cokesveld bij de coker; welke coke en welke poort niet te zien) |
| `gr-brunswick-fabriek` | fabriek (fase D, losplek) | Epsilon Advanced Materials, Mid-Atlantic Industrial Rail Park (US-74/76, grens Brunswick/Columbus County, ~16 km W van Leland); parkcoördinaat, kavel van Epsilon niet bekend | 34.3037, -78.1868 | [3][4][12] | aannemelijk (z15 gezien 2026-10-31: punt ligt aan de zuidrand van US-74/76 naast één grote witte loods en een zandwinput, de rest is bos en kaalgekapt terrein; geen fabriek, geen kavelgrens, niet te zien welke kavel Epsilon is; het eerdere 34.29, -78.19 ligt in bos en is verworpen) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze; alle óp de rijbaan, ná de afslag, nooit in een stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | I-12 oost van Baton Rouge (Walker) | 30.4707, -90.8576 | letterlijke kopie uit `grafiet-lakecharles-desoto.md`: I-12 (noord om Pontchartrain) i.p.v. I-10 door New Orleans |
| b1 | 2 | I-65 N, ná I-10 bij Mobile | 30.6679, -88.1271 | I-65 naar Montgomery i.p.v. I-10 door naar Pensacola/Tallahassee |
| b1 | 3 | I-85 O van de I-65/I-85-knoop (Montgomery) | 32.3585, -86.2500 | I-85 naar Atlanta i.p.v. I-65 door naar Birmingham |
| b1 | 4 | I-285 ZO-Atlanta (Perimeter, zuid van Decatur) | 33.6907, -84.2988 | de ring i.p.v. I-85/I-20 door het centrum van Atlanta |
| b1 | 5 | I-95 N, ná I-20 bij Florence | 34.2072, -79.8315 | I-20 O naar Florence en dan I-95 N i.p.v. I-85 → Charlotte of I-26 → Columbia/Charleston |
| b1 | 6 | I-74/US-74 O van I-95 (Lumberton) | 34.5795, -79.0481 | I-74/US-74 oostwaarts naar Whiteville i.p.v. I-95 door naar Fayetteville (I-40 → Wilmington) |
| b1 | 7 | US-74/76 bypass Whiteville | 34.3508, -78.6990 | US-74/76 naar het park i.p.v. NC-211/US-17 naar de kust |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Lake Charles Manufacturing Complex | Phillips 66 | ruwe olie → o.a. green en calcined needle coke | raffinaderij 264.000 b/d; naaldcokes-capaciteit niet gepubliceerd | [2][8][9] |
| Epsilon NC-fabriek (nog niet gebouwd) | Epsilon Advanced Materials (EAM) | naaldcokes → synthetisch grafiet-anodemateriaal (AAM) | 30 kt AAM/j (2027) → 60 kt (2030); $650 mln, 500 banen; vandaag 0 | [1][3][5] |

## 6 · Stoppunt
De brief stopt bij de poort van de geplande Epsilon-fabriek: geen bron noemt een afnemer van het AAM (alleen "US battery manufacturers and automotive OEMs" [1]), dus fase E vervalt.

## 7 · Open punten
- **Modaliteit niet gebronnet:** geen bron noemt vervoer [1][2]. Spoor is plausibel (CSX Select Site, NCRR legt een CSX-spoor voor ≥ 3.400 wagons/j aan [4][7]); een spoorbeen (~1.850 km, 1 omkering bij Atlanta) zou het truckbeen vervangen en wordt niet getekend zonder bron. Zeevervoer naar Wilmington (18 mijl van het park [4]) is evenmin gebronnet.
- **Kavel:** de plek van Epsilon binnen het park (1.100 acres [4]) is niet gevonden; anker is het parkcoördinaat uit de EDPNC-link (34.303655, -78.186809), aannemelijk. Het park wordt nog klaargemaakt (watertank-subsidie [6]).
- **Contract:** alleen een Agreement in Principle [1]; geen bevestiging dat het definitief is.
- **Fabriek niet gebouwd; start onzeker:** 2023 → 2026 → 2027 en nu groundbreaking "late 2026" [3][5]; volume vandaag 0.
- **Producten zijn naaldcokes (green en calcined), geen grafiet;** cokesvolume (kt in) en rendement cokes → AAM niet gepubliceerd.
- **Geen gepubliceerde wegkm:** hemelsbreed 1.487 km; de ±15 %-toets is hier een indicatie tegen OSRM, niet tegen een publicatie. Eerste ~400 km (Lake Charles → Baton Rouge/Slidell) lopen gelijk aan b1 van `grafiet-lakecharles-desoto` en worden opnieuw gescand.
- **Sitelaag:** Epsilon Brunswick staat niet in `grafiet-sitelaag.json`; kandidaat `w-epsilon-brunswick` (34.3037, -78.1868, 30 kt AAM, aannemelijk) — centraal.

## 8 · Bronnen
[1] Epsilon Advanced Materials, "EAM and Phillips 66 Partner…", 2025-09-24 — Agreement in Principle on Key Terms voor green en calcined needle coke uit Lake Charles; 30.000 t AAM in 2027, 60.000 t in 2030. https://www.epsilonam.com/images/press-release/EAMPL_Press_Release_Sept_24.pdf
[2] Argus Media, 2025-09-29 — P66 levert aan EAM Brunswick County, 30 kt/j, start 2027 (pagina zelf niet leesbaar; via zoekresultaat en `grafiet-lakecharles-desoto.md` [11]). https://www.argusmedia.com/en/news-and-insights/latest-market-news/2736976-eam-p66-sign-us-graphite-anode-coke-supply-deal
[3] Governor of North Carolina + EAM, 2023-10-26 — $649,9 mln, 500 banen, Mid-Atlantic Rail Industrial Park, Brunswick County; groundbreaking 2024, productie 2026, volle capaciteit 2031. https://governor.nc.gov/news/press-releases/2023/10/26/governor-cooper-announces-500-jobs-global-battery-component-supplier-selects-brunswick-county-first · https://www.epsilonam.com/images/press-release/EAM%20-%20NC%20Announcement%20press%20release_Final.pdf
[4] EDPNC, Mid-Atlantic Industrial Rail Park — 1.100 acres, platinum-certified CSX Select Site, Port of Wilmington 18 mijl, I-40 10 mijl; coördinaat 34.303655, -78.186809 alleen in de URL van de Zoom Prospector-link. https://edpnc.com/find-a-site/megasites/mid-atlantic-industrial-rail-park/
[5] Bisnow, 2026-02-03 — groundbreaking uitgesteld naar "late 2026" (EV-subsidie-wijzigingen). https://www.bisnow.com/news/raleigh-durham/industrial/battery-factory-planned-for-north-carolina-delayed-again-133049
[6] WECT, 2026-05-27 — Golden LEAF-subsidie $3 mln voor watertank; Epsilon moet vóór 2027-03-31 melden dat het doorgaat. https://www.wect.com/2026/05/27/brunswick-county-secures-3m-grant-industrial-park-water-tank/
[7] NC Railroad Company, 2023-10-30 — $500.000 voor on-site spoor en CSX-spoor voor de Epsilon-fabriek; ≥ 3.400 extra wagons/j. https://ncrr.com/news/north-carolina-railroad-company-invests-500000-for-new-ev-battery-plant-at-mid-atlantic-industrial-rail-park-in-brunswick-county-n-c/
[8] `v2/design/routebrieven/grafiet-lakecharles-desoto.md` — anker `gr-lakecharles-cokes` 30.2420, -93.2770 (bron-gelegd) en via-punt I-12 Walker; P66-bronnen [3][4][13] daarin.
[9] Phillips 66, Specialties — premium needle cokes uit Humber (VK) en Lake Charles (Louisiana). https://www.phillips66.com/specialties/
[10] Esri World Imagery via `v2/tools/sat_check.py` (live, 2026-10-31) — `v2/build-cache/satcheck/sat-grafiet-lakecharles-brunswick-park.png` (z15); eerder `…-toets-park.png`.
[11] OSRM (router.project-osrm.org, OSM-data), 2026-10-31 — Lake Charles → de zeven via-punten → park 1.690,9 km; I-20 440 km, I-10 349, I-65 274, I-85 238, I-12 138, I-95 80, US-74/76 ~100; geen publicatie.
[12] OpenStreetMap Nominatim reverse, 2026-10-31 — 34.3037, -78.1868 = Brunswick County, North Carolina (ODbL). https://nominatim.openstreetmap.org

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)

**Stroom `grafiet-lakecharles-brunswick`** -> `v2/data/stroomroute-grafiet-lakecharles-brunswick.json` — 1 been, 1.691,8 km, 12.619 punten, 256,9 KB, 2 markers (P66 cokesveld, Epsilon-park). Alleen truck: 1.691,8 km, doorgetrokken, geen stippel, geen zee, geen haven-aanloop, geen lucht.
Recept: `bak_stromen.sh` (functie `bak_grafiet_lakecharles_brunswick`); wegscan via `wegscan_puur.py` met profiel `grafiet-lakecharles-brunswick-lakecharles-brunswick` (`maak_stroombeen_weg.py`), extracts us-louisiana, -mississippi, -alabama, -georgia, -south-carolina, -north-carolina (~25 min scan, bbox 6 staten).
Toets: km 1.691,7 (scan) tegen 1.691 OSRM = +0,0%; dat is OSRM over dezelfde OSM, dus een indicatie en geen onafhankelijke bevestiging (geen gepubliceerde wegkm; hemelsbreed 1.487). Segmenten via-punt naar via-punt: 241,4 / 282,3 / 277,5 / 252,9 / 456,3 / 86,7 / 46,4 / 48,2 km; alle via-snaps <= 0,10 km, geen omweg. Enige naad: geen (1 been). Markers 0,00 en 0,05 km van de lijn. `toets_knikken`: 0 terugloop (28 spike-knikken zijn OSM-ruis op kruisingen); `toets_rechte_benen`: stroom niet in de lijst. json: versie 2, lonlat, modaliteit truck.
Toelichting: kop op privé-terreinwegen P66 (`eindToegangPrivaat: True`, first mile 1,77 km over service/tertiary/unclassified); eind op het EDPNC-parkcoördinaat (aannemelijk), geen last-mile-been. Beennaam draagt "naaldcokes, geen grafiet; aannemelijk: één bron, modaliteit niet gebronnet; fabriek nog niet gebouwd". Geen letterlijke kopie van grafiet-lakecharles-desoto b1: dat been eindigt in Chattanooga, deze scan is eigen (via-punt I-12 Walker wel hergebruikt).
Gereedschapslessen: geen; één poging, `corridorKlassen` niet nodig (alles interstates/US-74).
