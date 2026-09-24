# Routebrief (licht) · koper — Tenke Fungurume (Copperbelt) → Durban → Yangtze-monding

**stroom-id:** `koper-kolwezi-durban` · **geschreven:** 2026-09-24 · **werkwijze:** licht (M29) · **status:** concept · **Linear:** LAR-561
**Keten in één zin:** SX-EW-kathode van de TFM-plant (CMOC, Fungurume) per **truck** over de zuidelijke Copperbelt-uitweg — RN39/RN1 → **Kasumbalesa** → T3/T2 → **Chirundu** → A1/A4 → **Beitbridge** → N1/N3, ~3.000 km — naar de containerkade van **Durban (DCT Pier 2)**, daar in containers, en per **zeeschip** via Malakka naar de **Yangtze-monding**, waar de kathode in de **Shanghai bonded zone** (Waigaoqiao/Yangshan) landt.
**Welke as van het verhaal:** de Copperbelt-uitweg naar het zuiden. TFM + KFM produceerden **741,1 kt Cu** in 2025 (kathode) [1]; TFM exporteert per weg naar Durban én Dar es Salaam [2]; > 80% van de DRC/Zambia-koperexport gaat per truck (Wereldbank 2025) [3]; de DRC is Chinas grootste kathode-leverancier (69,3 kt in aug 2026 [4]; 36,7% van Chinas koperimport in 2024 → 44,7% jan–jul 2026 [16]). Het Durban-aandeel in het TFM-volume is niet gepubliceerd (§7). Zusterketen over het spoor: `koper-lobito-duisburg`.

## 1 · Ketenkaart
TFM-plant, Fungurume ──(b1 truck · RN39/RN1 · T3/T2 · A1/A4 · N1/N3 · ~3.000 km)──► Durban, DCT Pier 2 ──(b2 zee · Malakka · ~13.000 km)──► Yangtze-monding ──► Shanghai bonded zone (aanlanding, geen been)
  ├── zusterketen (eigen brief): Kamoa → Lobito per spoor (`koper-lobito-duisburg`)
  ├── alternatieve corridor, alleen genoemd: Lubumbashi → Dar es Salaam, 2.081 km (T3 → T2-noord via Kapiri Mposhi → Nakonde/Tunduma → T1) [3][5]
**Fase-afwijking (als bij Lobito):** de raffinage zit al bij de bron (SX-EW), dus fase C eindigt niet bij een smelter maar bij een **entrepot** (bonded warehouse). Fase D (walsdraad/kabel in China) is niet gedocumenteerd voor déze kathode → stoppunt §6.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `cu-tfm-laad` → `cu-durban-kade` | DRC **RN39** (Fungurume → Likasi) + **RN1** (Likasi → Lubumbashi → Kasumbalesa) · Zambia **T3** (Kasumbalesa → Chingola/Kitwe/Ndola → Kapiri Mposhi) + **T2** (→ Kabwe → Lusaka → Chirundu) · Zimbabwe **A1** (Chirundu → Harare) + **A4** (OSM-ref R1; Harare → Masvingo → Beitbridge) · RSA **N1** (Beitbridge → Polokwane → Pretoria → Buccleuch) + **N3** (Buccleuch → Durban) | ~3.000 [6]; routeplanner 3.035 [7]; eigen M25-bake 3.068,8 (+2,3%) [6] | maak_stroombeen_weg — profiel `koper-tfm-durban`: extracts congo-drc/zambia/zimbabwe/zuid-afrika, refs RN39 RN1 T3 T2 A1 A4 R1 N1 N3, gepubliceerdKm 3000, vensterKm 75 (de RN39 buigt bij Fungurume 53 km uit), 12 via-punten §4 | nee — beide uiteinden ≤ ~2 km van het net (plantweg TFM; havenwegen Bayhead → Pier 2 via de eindklassen-regel) |
| b2 | B | zee | `cu-durban-kade` → Yangtze-monding 31.42704, 121.47618 | — (Indische Oceaan → Straat Malakka → Zuid-Chinese Zee → Oost-Chinese Zee) | ~13.020 (searoute, kade → monding) | MARNET `--been "zee\|…\|-29.8790,31.0160\|31.42704,121.47618"` | aanloop: waarschijnlijk (kade ligt achterin het Bayhead-bekken, MARNET-knoop Durban buitengaats) → `maak_havenaanloop.py` als het gat > 0,5 km |

Geen last-mile-benen, geen fase-D-been: kathode is de eindvorm van deze streng (§6).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-tfm-laad` | mijn / laadplek | TFM hydrometallurgische plant (SX-EW), Kwatebala, ~6 km NW van Fungurume | -10.5685, 26.1975 | [2][8] — het profielpunt -10.6167, 26.2333 [2] ligt op een **open pit**, 6,5 km ZO van de plant; verschoven naar de plant | **bron-gelegd** (z15 gezien: lange tankhouse-/EW-hallen op het kruis, thickeners en tankparken ten zuiden, leach-vijvers ZW, pit W; de kathode-expeditiehal zelf is niet aangewezen → site-niveau) |
| `cu-durban-kade` | overslag truck → container → zeeschip | Durban Container Terminal **Pier 2**, noordkade (Bayhead) | -29.8790, 31.0160 | [9][10][17] — kathode gaat per flatdeck naar "Bayhead Terminal of containerdepots" [9] en wordt gecontaineriseerd (~22,2 t per 20') [17]; DCT Pier 2 is dé containerkade [10] | **bron-gelegd**, kade-keuze **aannemelijk** (z15 gezien: STS-kranen langs de noordkade, containerstapels, schip langszij; Pier 1 800 m oostelijker; Maydon Wharf = westoever) — geen bron noemt Pier 2 expliciet voor kathode (§7) |
| — | zee-eindpunt | Yangtze-monding (bestaand anker, hergebruikt) | 31.42704, 121.47618 | routebrief-licht §1 | bestaand; aanlanding = Shanghai bonded zone, aannemelijk [11][12] |

## 4 · Via-punten (b1, in reisvolgorde — 5 punten op OSM-node-id gepind via Overpass (24-09) [18], de rest OSM-wegvertices uit de gebakken M25-corridor `cu-copperbelt-durban`; geen stadscentra)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Likasi (RN39 → RN1) | -10.9806, 26.7355 | de RN39 uit Fungurume valt hier op de RN1; sluit RN1-west (Kamina) uit |
| b1 | 2 | Lubumbashi (RN1) | -11.6642, 27.4827 | pint de RN1 door Lubumbashi richting Kasumbalesa (niet de RN5 naar Sakania/Mokambo) |
| b1 | 3 | **Kasumbalesa** — grens DRC/Zambia | -12.2658, 27.7959 | verplichte grenspost; de enige grote kathode-poort (files van dagen) [15] |
| b1 | 4 | Ndola (T3) | -12.9688, 28.6367 | T3 door de Zambiaanse Copperbelt (Chingola–Kitwe–Ndola), niet de T5/Solwezi-omweg |
| b1 | 5 | Kabwe (T2) | -14.4426, 28.4400 | ná Kapiri Mposhi: T2-zuid (Great North Road) i.p.v. T2-noord = de Dar es Salaam-corridor |
| b1 | 6 | Lusaka (T2, Cairo Road — OSM-node 10765278038) | -15.4163, 28.2817 | T2 → Chirundu, niet T1 → Livingstone/Kazungula (Botswana-route) |
| b1 | 7 | **Chirundu** — grens Zambia/Zimbabwe, Zambezi-brug | -16.0338, 28.8471 | verplichte grenspost; sluit Kariba en Kazungula uit |
| b1 | 8 | Harare (A1 → A4) | -17.8362, 31.0467 | de wissel van de A1 op de Masvingo-weg A4; sluit A5 → Bulawayo uit |
| b1 | 9 | Masvingo (A4 = OSM-ref R1, Robert Mugabe Way — OSM-node 6146504328) | -20.0745, 30.8332 | pint de A4/R1; sluit de Bulawayo-omweg (A5/A6) uit |
| b1 | 10 | **Beitbridge** — grens Zimbabwe/RSA, Limpopo-brug (OSM-node 6887614857 óp de brug; way 26998469, N1, bridge=yes) | -22.2244, 29.9865 | verplichte grenspost; sluit Plumtree/Botswana uit |
| b1 | 11 | Polokwane (N1 Polokwane Bypass — OSM-node 6141172488) | -23.9218, 29.4803 | N1-bypass langs Polokwane, niet R521/R101 |
| b1 | 12 | Buccleuch — N1/N3-splitsing (Johannesburg): eerste N3-vertex, Eastern Bypass (OSM-node 21587465; way 626256782, ref N3) | -26.0493, 28.1004 | dwingt de N3 naar Durban af ná het knooppunt; sluit N1-zuid/N12 (Vaal) én de M1/M2 door het centrum uit (§7) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| TFM, Kwatebala-plant (Fungurume) | CMOC 80% / Gécamines 20% | oxide-erts → SX-EW-kathode (+ kobalthydroxide) | > 450 kt Cu/j; TFM + KFM 741,1 kt in 2025 | [1][8] |
| Shanghai bonded zone (Waigaoqiao/Yangshan) — entrepot, geen fabriek | bonded warehouses (non-registered DRC-kathode) | kathode in → kathode uit naar Chinese verwerkers (Entrepot Trade 51,8 kt in aug 2026) | bonded-voorraad Shanghai 197 kt (21-01-2026) … 13,5 kt (27-06-2026) | [11][12] |

## 6 · Stoppunt
De brief stopt in de Shanghai bonded zone: kathode is de eindvorm van deze streng (LME-grade metaal, geen omzetting onderweg), en geen enkele bron koppelt déze DRC-kathode aan een benoemde Chinese walsdraad- of kabelfabriek — fase D wordt alleen getekend als één bron de fabriek noemt (werkwijze licht §1).

## 7 · Open punten
- **Durban-aandeel in het TFM-/Copperbelt-volume:** geen bron; Freight News: verkeer "ooit sterk op Durban geconcentreerd, nu verdeeld over Dar es Salaam, Walvis Bay, Beira en Durban" [5]. Jaarvolume van dít been dus onbekend.
- **De precieze Durban-kade:** "Bayhead Terminal of containerdepots" [9]; depots met mineralen-yards liggen in Bayhead/Mobeni (Bidvest SACD, New Pier 2, Breede Road [13]; UCD 10.000 m² minerals yard, > 75 kt [14]). Of er een depot-stap (stuffing) vóór de kade zit is niet getekend (geen last-mile-been); Maydon Wharf (breakbulk) blijft een alternatief.
- **Laadplek op het TFM-terrein:** de kathode-expeditiehal is niet gevonden; het anker is het plant-hart (site-niveau).
- **Aanlanding China:** Shanghai bonded zone is aannemelijk (grootste bonded-voorraad, DRC grootste leverancier), maar zendingen gaan ook naar Tianjin/Qingdao/Guangzhou [17]; niet getekend.
- **Gepubliceerde km:** geen operator-cijfer; ~3.000 (redactietabel) + routeplanner 3.035 + eigen bake 3.068,8. Reistijd 35–40 dagen rondreis Kolwezi ↔ Durban [5][15].
- **Buccleuch:** het via-punt ligt nu óp de N3 (Eastern Bypass); toets bij het bakken tóch dat de lijn ná Buccleuch de N3 (Heidelberg) blijft volgen en niet via de M1/M2 door het centrum loopt zoals de M25-corridor deed (die had Johannesburg-centrum als via).
- **Zee-aanloop Durban:** de MARNET-knoop ligt vermoedelijk buitengaats; gat meten, > 0,5 km → haven-aanloop-stippel.

## 8 · Bronnen
[1] Metalnomist, "CMOC copper output rose in 2025 on stronger DRC production", 2026-05-29, https://www.metalnomist.com/2026/05/cmoc-copper-output-rose-in-2025-on.html
[2] Lobito Corridor Profile, "Tenke Fungurume Mine" (SX-EW-kathode; export per weg naar Durban en Dar es Salaam; -10.6167, 26.2333), 2026, https://www.lobitocorridor.com/mines/drc/tenke-fungurume/
[3] Ecofin Agency, "Despite billions in rail investment, Southern Africa's copper exports still depend largely on trucking" (Wereldbank 2025: > 80% per truck; DRC 3,1 Mt export 2024), 2026, https://www.ecofinagency.com/news/2409-59190-despite-billions-in-rail-investment-southern-africas-copper-exports-still-depend-largely-on-trucking
[4] SMM, "Imports down, exports up: China's net copper cathode imports fell in August 2026", 2026-09-22, https://news.metal.com/newscontent/104128753-imports-down-exports-up-chinas-net-copper-cathode-imports-fell-in-august-2026-smm-analysis
[5] Freight News, "Copper volumes prompt route diversification", 2026-09-03, https://www.freightnews.co.za/article/copper-volumes-prompt-route-diversification-0
[6] v2/design/wegcorridors.md §2a (Copperbelt → Durban ~3.000 km) + CLAUDE.md, M25-bake 2026-07-22: 3.068,8 km (+2,3%), tussenpunten < 110 m van de weg
[7] Travelmath, driving distance Kolwezi → Durban 3.035 km (routeplanner, geen scheidsrechter), https://www.travelmath.com/distance/from/Kolwezi,+DR+Congo/to/Durban,+South+Africa
[8] CMOC, "The DRC – copper and cobalt" (TFM: Fungurume, Lualaba; koperkathode + kobalthydroxide; > 450 kt/j), https://en.cmoc.com/html/Business/Congo-Cu-Co/
[9] Kweli Logistics, "Zambia Copperbelt trucking: copper backhaul & mining freight" (flatdeck, platen 125 kg; "Durban — Bayhead Terminal or container depots — via Lusaka, Chirundu, Harare, Beitbridge"), https://www.kweli.co.za/blog/zambia-copperbelt-trucking/
[10] Africa Ports, "Port of Durban" (Durban Container Terminal Pier 2, North Quay; Pier 1 sinds 2007; Maydon Wharf multi-purpose), https://africaports.co.za/durban/
[11] SMM, "Weekly copper cathode inventory in China bonded zone" (Shanghai bonded zone), https://news.metal.com/newscontent/102555736-smm-data-weekly-copper-cathode-inventory-in-china-bonded-zone
[12] SMM, "China's copper cathode imports by trade mode in August 2026" (51,8 kt Entrepot Trade by Customs Special Control Area), 2026-09-20, https://news.metal.com/newscontent/104124214-chinas-copper-cathode-imports-by-trade-mode-in-august-2026
[13] Bidvest SACD Durban, containerdepot New Pier 2, 30 Breede Road, Bayhead, https://www.sayellow.com/view/south-africa/south-african-container-depots-sacd-durban-in-durban
[14] United Container Depots, minerals yard Mobeni (10.000 m², > 75.000 t), https://www.ucd.co.za/
[15] Fastmarkets, "African copper, cobalt logistics chain under pressure as truckers avoid DRC" (Kolwezi → Durban 35–40 dagen; 400 km Kolwezi–Kasumbalesa), 2022-04-19, https://www.fastmarkets.com/insights/african-copper-cobalt-logistics-chain-under-pressure-as-truckers-avoid-drc/
[16] Discovery Alert, "Why China's grip on DRC copper is deepening" (DRC 36,7% van Chinas koperimport 2024; 44,7% jan–jul 2026), https://discoveryalert.com/analysis/china-drc-copper-dominance/
[17] copperexporters.com (handelssite, zwak: containerisatie ~22,2 t per 20', laadhavens Dar es Salaam/Durban, aankomst Shanghai/Tianjin/Qingdao/Guangzhou/Shenzhen), https://www.copperexporters.com/515/
[18] OpenStreetMap via Overpass API (ODbL), node-id's en refs opgevraagd 2026-09-24; Likasi/Ndola/Kabwe/Chirundu/Harare gaven timeouts op alle drie de mirrors → corridorvertices.
Satellietblik: `v2/build-cache/satcheck/sat-cu-tfm-laad.png` en `sat-cu-durban-dct2.png` (Esri z15, 3 tegels), 2026-09-24.


## 9 · Gebakken (2026-09-25. lichte werkwijze)

**Stroom `koper-tfm-durban`** → `v2/data/stroomroute-koper-tfm-durban.json` — 3 benen. 16.021 km. 5 markers: truck 2.982 km · zee (stippel) 18 km · zee 13.020 km.
Recept: `bak_stromen.sh` (functie voor deze stroom). Toelichting: het wegbeen kwam uit `maak_stroombeen_weg.py` (profiel `koper-tfm-durban`. 2.982 km = −0.6% t.o.v. ~3.000; de lijn neemt na Buccleuch de N3: 8.3 km van het Johannesburg-centrum. 1.6 km langs Heidelberg); haven-aanloop Durban 17.8 km over water (stippel); zeebeen MARNET tot de Yangtze-monding.
