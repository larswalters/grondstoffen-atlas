# Routebrief (licht) · lithium — Bikita → Beira → Zhangjiagang (Zimbabwe → China)

**stroom-id:** `lithium-bikita-zhangjiagang` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat (SC5,0–5,5) en chemisch petaliet van Bikita Minerals (Sinomine) gaan per **truck** (30–34 t, ~42 ritten/dag [10]) over de A9 (Masvingo–Mutare) en de Beira-corridor (Forbes/Machipanda → EN6) naar de general-cargo-terminal van Beira, per **bulkcarrier** (15–25 kt per schip [3]) door het Mozambiquekanaal en Malakka naar de Yangtze-monding en over de Yangtze naar de kade van Zhangjiagang — de Chinese aanlandingshaven is *aannemelijk: één bron* (SunSirs, proefladingen juni 2026 naar Tianjin/Zhangjiagang [3]); de converter (Sinomine Jiangxi, Xinyu) wordt niet getekend.
**Welke as van het verhaal:** as 3 — Zimbabwaans hardrock per truck naar Beira en via Malakka naar de Chinese eigenaar-smelters. Zimbabwe 2025: **28 kt Li** (≈ 149 kt LCE, 10 % van de wereld, USGS [12]) = **1,128 Mt concentraat** geëxporteerd (+11 %) [8]; China-douane 2025: 1.204.072 t uit Zimbabwe = 15 % van 7.750.630 t spodumeenimport [7]. Bikita naamplaat: 300 kt SC/j (≈ 39 kt LCE) + 480 kt petaliet/j (3,9 % Li2O ≈ 46 kt LCE) [2]; exportquota 2026: 200 kt (apr) + 300 kt (jul) = 500 kt concentraat (≈ 50–65 kt LCE, mix onbekend) [4][5]. *Eenheid: kt LCE = kt concentraat × Li2O-gehalte × 2,473; oorspronkelijke eenheden erbij.*

## 1 · Ketenkaart
```
Bikita concentratorplant `li-bk-plant` ──(b1 truck · A9/P4 → Forbes/Machipanda `li-forbes-grens` → EN6 · ~525 km)──► Beira general-cargo-kade `li-beira-kade`
   ──(b2 zee · Mozambiquekanaal → Malakka → Zuid-Chinese Zee · ~10.500 km, MARNET; bestemming aannemelijk: één bron)──► Yangtze-monding `li-yangtze-monding`
   ──(b3 stippel 8,6 km zeenet → bulklaag · b4 Yangtze 135 km · b5 stippel 0,6 km — letterlijke kopie bak_lithium)──► Zhangjiagang-kade `li-zjg-kade` ⏹ stoppunt
   ├── vertakking (niet getekend): deel via Beitbridge → Durban (N1/N3, ~1.450 km; SunSirs: "deels via Durban") en Tianjin als tweede aanlandingshaven [3]
   ├── vertakking (niet getekend): spoor Gwanda → Beitbridge → Chicualacuala → Maputo (Tsingshan, juli 2026) — andere mijn, andere haven [14]
   └── fase C (niet getekend): Zhangjiagang → Sinomine Resource (Jiangxi) Lithium, Xinyu, 60 kt/j carbonaat/hydroxide [11] — landbeen ongedocumenteerd
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (bulk/big bags, 30–34 t) | `li-bk-plant` → `li-beira-kade` | mijnweg → A9/P4 Mutare-Masvingo Highway (Nyika, Birchenough Bridge, Wengezi) → Mutare → N6 Forbes/Machipanda → EN6 (Manica, Chimoio, Inchope, Dondo) → Beira | ~525 (Masvingo–Mutare 298 min ~70 km Masvingo–mijn [13][1] + Mutare–Forbes ~8 + EN6 289 [13]) | maak_stroombeen_weg (extracts zimbabwe + mozambique; refs P4, N6) | nee; haventerrein Beira alleen als OSM de havenstraten mist → korte stippel "eigen terrein" |
| b2 | B | zee (bulkcarrier 15–25 kt) | `li-beira-kade` → `li-yangtze-monding` (routeerpunt 31.4074, 121.4848 = bak_lithium) | Mozambiquekanaal → Malakka → Zuid-Chinese Zee → Taiwanstraat | ~10.500 (MARNET-indicatie ontwerp; 40 dagen [3]) | MARNET; zeeknoop 5265 (-19.8701, 34.7882) op 7,8 km van de kade → geen aanloop | nee — *aannemelijk: één bron* [3] in de beennaam |
| b3 | B | zee (stippel) | MARNET-eindknoop 31.51, 121.4187 → bulklaag 31.4512, 121.4769 | — | 8,6 | letterlijke kopie `bak_lithium` regel `--stippel "zee|overgang zeenet → Yangtze-bulklaag…"` | ja — net reikt niet |
| b4 | B | binnenvaart (zelfde zeeschip) | Yangtze-monding → Zhangjiagang, zuidgeul Shuangshan | Yangtze | 135,2 (gebakken) | letterlijke kopie `$BEEN/rivierbeen-yangtze-zhangjiagang.geojson` | nee |
| b5 | B | binnenvaart (stippel) | 31.9733, 120.4202 → `li-zjg-kade` | — | 0,6 | letterlijke kopie `bak_lithium` aanloop-stippel | ja — anker ≠ routeerpunt |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-bk-plant` | mijn / laadplek | Bikita Minerals — concentratorplant (flotatie + gravitatie), NW van de open pits | -19.9512, 31.4245 | [1][2][15][16] | bron-gelegd (z15 gezien: procesgebouwen, ronde indikkers en een witte concentraatstapel aan een mijnweg, 0,5–1 km NW van de putten; het oudere plant-/dorpcomplex ligt 1,3 km Z op de OSM-landuse-centroïde -19.9639, 31.4270; Wikipedia-punt -19.9572, 31.4360 ligt in de put) |
| `li-forbes-grens` | grensovergang | Forbes Border Post (ZW) / Machipanda (MZ), N6 | -19.0052, 32.7123 | [9][15][16] | bron-gelegd (z15 gezien: wegcorridor door het dal met gebouwen en opstelstroken aan weerszijden van de grens; Machipanda-bebouwing 2 km O) |
| `li-beira-kade` | overslag truck → zee | Beira, general-cargo-terminal Cornelder de Moçambique (670 m, 4 ligplaatsen, 10 m; ferrochroom/graniet/breakbulk) | -19.8150, 34.8340 | [8][15][16] | bron-gelegd (z15 gezien: kadefront met loodsen en stapelveld tussen de kolenterminal (N, zwarte stapel) en de containerstacks (Z); wélke van de vier ligplaatsen spodumeen laadt is niet gebrond) |
| `li-yangtze-monding` | overgang zee → rivier | Yangtze-monding (Wusong/Luojing) | 31.42704, 121.47618 | bestaand anker (koper-tfm-durban) | hergebruik — geometrie via het bak_lithium-routeerpunt 31.4074, 121.4848 |
| `li-zjg-kade` | losplek (stoppunt) | Zhangjiagang — kade Zhangjiagang Port Group (ertsen/hout/staal) | 31.96800, 120.42050 | bestaand anker (lithium-greenbushes-zhangjiagang) | hergebruik; bestemming *aannemelijk: één bron* [3] |

## 4 · Via-punten (alleen b1; lat, lon geprojecteerd op trunk-vertices uit de Geofabrik-extracts [15])
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | mijnafrit op de A9/P4 (Mutare-Masvingo Highway) | -19.9721, 31.4148 | pint de afrit naar het oosten i.p.v. westwaarts naar Masvingo/A4 |
| b1 | 2 | Nyika, A9/P4 | -20.0001, 31.5915 | A9 oost via Birchenough i.p.v. noord via Gutu → Chivhu → A3 (Harare–Mutare) |
| b1 | 3 | Birchenough Bridge (Save-oversteek) | -19.9614, 32.3460 | A9 over de brug naar Mutare i.p.v. A16 naar Chipinge |
| b1 | 4 | Wengezi, A9/P4 | -19.5095, 32.5318 | A9 noord naar Mutare i.p.v. de Chimanimani/Cashel-zijtak |
| b1 | 5 | Forbes Border Post, N6 (= `li-forbes-grens`) | -19.0052, 32.7123 | oost de grens over naar Beira i.p.v. A3 west naar Harare (of Beitbridge → Durban) |
| b1 | 6 | Chimoio, N6-doorgaande weg (N van het centrum) | -19.1283, 33.4838 | pint de EN6 door Manica/Chimoio i.p.v. de EN7-tak (Tete) |
| b1 | 7 | Inchope, EN6 × EN1 | -19.2072, 33.9326 | rechtdoor EN6 naar Beira i.p.v. EN1 zuid naar Maputo |
| b1 | 8 | Dondo, N6 | -19.6165, 34.7460 | pint de N6-inrit van Beira (haven via Av. Samora Machel, 1,8 km van de kade) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Bikita-concentrator (flotatie 330 t/u + gravitatie 220 t/u) | Sinomine Resource Group (Bikita Minerals, sinds 2022) | 2 + 2 Mt erts/j → 300 kt SC (5,0–5,5 % Li2O) + 480 kt petaliet (3,9 %) | ≈ 85 kt LCE/j naamplaat; in bedrijf sinds juli 2023 | [1][2] |
| Bikita lithiumsulfaatfabriek (gepland) | Sinomine | concentraat → 100 kt/j lithiumsulfaat, US$ 400 mln, medio 2027 — verandert het product van deze as | [5][6] |
| Sinomine Resource (Jiangxi) Lithium, Xinyu (niet getekend) | Sinomine | Bikita- en Tanco-concentraat → 60 kt/j batterijkwaliteit Li2CO3 / LiOH | [11] |

## 6 · Stoppunt
De brief stopt op de kade van Zhangjiagang: één bron (SunSirs) noemt Tianjin/Zhangjiagang als aankomsthavens van de Bikita-ladingen, geen bron koppelt een lading aan de fabriek in Xinyu of aan een landcorridor daarheen — fase C is dus niet in één zin gegeven en wordt niet getekend; fase D/E vervalt.

## 7 · Open punten
- **Volume-split Beira/Durban/Tianjin** ongepubliceerd (SunSirs: "deels via Durban"; Tianjin naast Zhangjiagang) — Durban-variant bewust niet getekend.
- **Beira-ligplaats:** general-cargo-terminal is gebrond via de ladingsoort (breakbulk mineralen), de ligplaats zelf niet; geen bron of het concentraat in bulk of in big bags aan boord gaat.
- **Gepubliceerde km b1:** geen bron geeft de rit Bikita → Beira als geheel; ~525 km is een som van deelstukken (via-keten hemelsbreed 465 km, factor 1,13).
- **Xinyu-anker** niet gelegd (MEE-register niet geraadpleegd omdat fase C toch niet getekend wordt).
- **Product verschuift:** exportverbod op concentraat per jan 2027 + sulfaatfabriek Bikita (100 kt, 2027) → deze as draagt binnen een jaar sulfaat i.p.v. concentraat; de stop feb–apr 2026 (verbod na voorraden in Beira) is de tensie `li-t-zimbabwe`.
- **Spoor:** de Maputo-lijn (juli 2026) betreft Gwanda/Tsingshan, niet Bikita — geen spoornet nodig; alleen genoemd.

## 8 · Bronnen
[1] Sinomine Resource Group — Bikita Minerals: 80 km NO van Masvingo, spodumeen- en petalietlijn elk 2 Mt erts/j, productie sinds juli 2023. https://en.sinomine.cn/25/93.html
[2] Mining Zimbabwe, 10-07-2023 — flotatie 330 t/u → 300 kt SC/j (5,0–5,5 % Li2O); gravitatie 220 t/u → 480 kt petaliet/j (3,9 %). https://miningzimbabwe.com/bikita-minerals-breaks-ground-with-new-gravity-separation-and-flotation-plants-launching-trial-productions/
[3] SunSirs, 2026 — Sinomine/Bikita: vertrek Port of Beira 1–8 juni 2026, 40 dagen, aankomst Tianjin/Zhangjiagang 10–18 juli, 15–25 kt per schip, deels via Durban. https://www.sunsirs.com/uk/detail_news-34127.html
[4] Mysteel, 25-08-2026 — quota 200 kt (apr) + 300 kt (jul 2026); transport Bikita-concentraat hersteld. https://www.mysteel.net/news/5138179-flash-sinomine-resource-group-has-restored-normal-transport-operations-for-its-bikita-lithium-concentrate
[5] The Zimbabwean, 08-2026 — extra quotum 300 kt; sulfaatfabriek 100 kt/j medio 2027; concentraatverbod jan 2027. https://www.thezimbabwean.co/2026/08/sinomine-secures-additional-zimbabwe-lithium-export-quota/
[6] Xinhua, 15-05-2026 — Bikita hervat export na vergunning; sulfaatfabriek US$ 400 mln. https://english.news.cn/africa/20260515/f960017d694c4849a429135ceb45690d/c.html
[7] Fastmarkets, 2026 — China-douane 2025: 1.204.072 t uit Zimbabwe van 7.750.630 t (15 %); verbod 25-02-2026. https://www.fastmarkets.com/insights/zimbabwe-imposes-immediate-ban-on-exports-of-raw-minerals-lithium-concentrates/
[8] BU GDP, 23-03-2026 (voorraden in Port of Beira → verbod; sulfaatfabrieken) https://www.bu.edu/gdp/2026/03/23/zimbabwes-lithium-pivot-promises-and-pitfalls-of-mining/ · ADF Magazine, 06-2026 (1,128 Mt SC 2025, +11 %) https://adf-magazine.com/2026/06/zimbabwe-scrutinizes-chinese-lithium-mining/ · World Port Source, Beira general-cargo-terminal 670 m / 4 ligplaatsen / 10 m, ferrochroom-graniet-breakbulk. http://www.worldportsource.com/ports/commerce/MOZ_Port_of_Beira_657.php
[9] Oxpeckers, 04-2025 — Machipanda = hoofdcorridor naar Beira, 30 t-trucks; Beitbridge → Durban als alternatief. https://oxpeckers.org/2025/04/lithium-smugglers/
[10] CNRG, The Weekly 5e editie (bezoek 02-05-2023) — "minstens 42 vrachtwagens per dag met concentraat naar Beira". https://cnrgzim.org/news/the-weekly-5th-edition/
[11] Sinomine Resource (Jiangxi) Lithium, Xinyu — 60 kt/j Li2CO3/LiOH, voeding Bikita + Tanco. https://en.sinomine.cn/fzjg/185.html
[12] USGS, Mineral Commodity Summaries 2026 — lithium: Zimbabwe 28.000 t Li (2025; 20.000 in 2024), wereld 290.000 t. https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-lithium.pdf
[13] Zimbabwe Field Guide — Birchenough Bridge 118 km van Mutare, 181 km van Masvingo op de A9 https://www.zimfieldguide.com/manicaland/birchenough-bridge · Mozambique Expert — EN6 Beira–Machipanda 289 km (Inchope 124, Chimoio, Manica, Machipanda). https://www.mozambiqueexpert.com/en/mozambiques-en6-beira-to-zimbabwe/
[14] Discovery Alert, 07-2026 — spoor Gwanda → Beitbridge → Chicualacuala → Maputo (~1.000 km, Tsingshan); Beira en Durban als wegalternatieven. https://discoveryalert.com/zimbabwe-lithium-rail-route-maputo-port-exports-2026/
[15] OpenStreetMap (ODbL) via Nominatim/Photon en de lokale Geofabrik-extracts zimbabwe/mozambique (pyosmium, trunk-vertices P4/N6) — landuse "Bikita Minerals Mine" -19.9639/31.4270 · "Porto da Beira" -19.8165/34.8374 · "Forbes Border Post" -19.0053/32.7124 · towns Nyika, Machipanda, Chimoio, Inchope, Dondo. Wikipedia Bikita mine 19°57′26″S 31°26′10″E. https://www.openstreetmap.org · https://en.wikipedia.org/wiki/Bikita_mine
[16] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15, live, 2026-09-26) — `v2/build-cache/satcheck/sat-lithium-bikita-zhangjiagang-bikita-z14.png`, `…-bikita-plant-z15.png`, `…-forbes-z15.png`, `…-beira-z15.png`.

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `lithium-bikita-zhangjiagang`** → `v2/data/stroomroute-lithium-bikita-zhangjiagang.json` — 6 benen. 13.619,1 km. 5 markers: truck 526,9 km · truck (stippel) 1,8 km · zee 12.946,0 km · zee (stippel) 8,6 km · binnenvaart 135,2 km · binnenvaart (stippel) 0,6 km.
Recept: `bak_stromen.sh` (functie `bak_lithium_bikita_zhangjiagang`); wegprofiel `lithium-bikita-zhangjiagang-bkplant-beira` in `maak_stroombeen_weg.py`. Toelichting: been 1 (Bikita-plant → N6-havenweg-inrit Beira, A9/P4 → N6/EN6, extracts zimbabwe+mozambique) komt uit één wegscan: 526,5 km getekende weggeometrie tegen ~525 gepubliceerd (som van deelstukken) = **+0,3%**, ruim binnen ±15%. Been 2 (haventerrein Beira, 1,8 km, stippel — zie hieronder). Been 3 is de MARNET-zeerouter Beira-kade → Yangtze-monding-routeerpunt (31,4074/121,4848), 12.946,0 km (geen gepubliceerde km ter vergelijking, alleen "40 dagen"). Benen 4–6 (overgang zeenet→Yangtze-bulklaag, het Yangtze-rivierbeen en de aanloop-stippel naar de Zhangjiagang-kade) zijn **letterlijke kopieën** van `bak_lithium` (Greenbushes→Zhangjiagang) — geen tweede scan/routering.

**Toets-bevindingen (buiten de norm, niet dichtgetrokken):**
- **Haventerrein Beira niet in het net.** Cornelder's havenstraten (`highway=service`, geen access-tag) vormen in OSM een eigen, van het doorgaande net LOSSTAAND clustertje (gemeten: component van 2 knopen, beide ≤0,25 km van de kade — bevestigd met een BFS over de gescande weggraaf). Het wegprofiel eindigt daarom niet op de kade zelf maar op de laatste VERBONDEN knoop, de N6-havenweg-inrit bij Av. Samora Machel (34,848737/-19,823623) — 1,82 km van de kade, vrijwel exact de "1,8 km" die de brief bij via-punt 8 al zelf noemt. De laatste 1,82 km is getekend als stippel "eigen terrein" (been 2).
- **Naad been 2→3 = 7,78 km** — groter dan de norm van ≤5 km. Geen procesfout maar de brief-eigen keuze om bij Beira géén haven-aanloop te tekenen (§2: "zeeknoop 5265 op 7,8 km van de kade → geen aanloop"): het zeebeen begint op MARNET-zeeknoop 5265 (34,7882/-19,8701), de truck-stippel eindigt op de kade zelf (34,8340/-19,8150) — exact de 7,8 km die de brief al gemeten had. Anker ≠ routeerpunt; niet dichtgetrokken met een verzonnen haven-aanloop, want de brief besliste dat expliciet.
- **11 knikken ≥ 60° over het wegbeen** (`toets_knikken.py`), waarvan 1 "omkering" (≥150°, 156,5° bij -19,20662/33,93155, EN6 nabij Inchope) — een scherpe maar ECHTE bocht, geen sluipweg — en de rest OSM-"spike"-artefacten (radius 8–37 m op kleine-klasse-eindwegen bij de mijnafrit en de grens). **0 terugloop**, de enige categorie die reparatie vraagt. Het zeebeen heeft 2 krappe bochten (radius 5–8 km, bij de Yangtze-monding resp. bij Kaap Guardafui) — normaal voor een lange MARNET-polylijn, geen artefact.
- `toets_rechte_benen.py --min-km 5`: alleen been 4 (zee, overgang zeenet→bulklaag, 8,6 km) komt in de verdachtenlijst — al correct gestippeld (letterlijke kopie van `bak_lithium`, dezelfde reden). Been 2 (1,8 km) en been 6 (0,6 km) liggen onder de 5 km-drempel en zijn los daarvan al stippel.
- JSON-vormtoets: `versie` 2, `punt_formaat` `lonlat`, modaliteiten {truck, zee, binnenvaart} (alle toegestaan), elk been ≥2 punten, bestand 154,7 KB (< 300 KB) — allemaal in orde.
- Markers: 4 van de 5 liggen op ≤6 m van hun lijn (Bikita-plant 0 m · Forbes-grens 5,7 m · Beira-kade 0 m · Zhangjiagang-kade 0 m). De Yangtze-monding-marker (bestaand anker, hergebruikt van koper-tfm-durban) ligt op 2,69 km van de lijn — bewust, want de geometrie loopt via het `bak_lithium`-routeerpunt (31,4074/121,4848), niet via het ankerpunt zelf (brief §3: "hergebruik — geometrie via het routeerpunt").

**Gereedschapslessen:** een `eindKlassen`/`eindToegangPrivaat`-uitbreiding op een havenanker kan een punt opleveren dat dichterbij ligt dan het doorgaande net, maar tot een ANDERE, niet-verbonden component behoort (hier: Beira's haven-`service`-wegen, 2 knopen, losstaand). Zichtbaar via een BFS-componentcheck op de gescande weggraaf, niet via de snap-afstand alleen (die was met 0,23–0,25 km juist verleidelijk klein). Bevestigt de klasse uit `koper-caletones-eteo`/`-maitenes` (eindToegangPrivaat) op een nieuwe variant: hier is het probleem geen `access=private`-tag maar een echte topologische breuk in OSM. Het patroon "MARNET-knoop ligt X km van de kade, geen aanloop, naad blijft staan" is al bekend van Beilun (`koper-escondida-guixi`) en Qingdao (`grafiet-balama-laixi`) en wordt hier op een derde stroom herbevestigd.
