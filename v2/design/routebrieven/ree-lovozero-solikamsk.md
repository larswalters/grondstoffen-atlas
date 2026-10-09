# Routebrief (licht) · zeldzame aardmetalen — Lovozero → Olenegorsk → Solikamsk (Rusland)

**stroom-id:** `ree-lovozero-solikamsk` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** loparietconcentraat van het Lovozerski GOK (Rosatom, Karnasurt-mijn bij Revda, Kola) gaat per **truck** (~73 km, aannemelijk) naar het goederenemplacement van Olenegorsk en per **spoor** (~2.770 km, aannemelijk) via Belomorsk, Obozerskaya, Vologda en Kirov naar Solikamsk Magnesium Works (SMZ, kraj Perm), dat er tantaal, niobium, titaan en een collectief REE-concentraat uit haalt. Binnenlands; geen fase D/E.
**Welke as van het verhaal:** *de enige Russische REE-grondstoflijn.* LGOK is Ruslands enige loparietproducent en SMZ zijn enige verwerker [1][2][6]. Jaarvolume: **5,8 kt loparietconcentraat** in 2025 (verdubbeld t.o.v. 2024), doel 12 kt in 2030 [6][7]; REO-gehalte niet gepubliceerd, dus geen kt REO (ontwerp noemde ~6 kt/j, 2025-2026) [7][9].

## 1 · Ketenkaart
```
Lovozerski GOK `ree-lgok-mijn` (Ilma-meer, 5 km ZZW van Revda)
  ──(b1 truck · Revda → 47K-047/47K-043 → Olenegorsk · ~73 km, aannemelijk: geen bron voor spoorkop en modaliteit)──►
Olenegorsk station `ree-olenegorsk-station` (goederenemplacement, Oktoberspoorweg)
  ──(b2 spoor · Murmansk-lijn → Belomorsk–Obozerskaya → Konosha–Vologda–Galich–Sjarja → Kotelnitsj–Kirov–Perm → Kizel–Jajva · 2.770 km, aannemelijk)──►
Solikamsk Magnesium Works `ree-smz-solikamsk` ⏹ stoppunt
```
Niet getekend: de ontmantelde LGOK-bedrijfsspoorlijn Lovozero–Aikuvenn (2007) [8] en 600 mm-smalspoor bij de mijn (geen 1520 mm-net).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-lgok-mijn` → `ree-olenegorsk-station` | mijnweg → Revda → 47K-047 Severny trakt → 47K-043 → rotonde Olenegorsk → Privokzalnoje sjosse | 65 vanaf Revda per weg [8] + ~7,8 mijn→Revda (OSRM) = **~73**; OSRM totaal 76,2 [12]; hemelsbreed 60,9 | maak_stroombeen_weg (rusland-noordwest) | nee |
| b2 | A | spoor | `ree-olenegorsk-station` → `ree-smz-solikamsk` | zie §4: Belomorsk–Obozerskaya–Konosha–Vologda–Buj–Galich–Sjarja–Kotelnitsj–Kirov–Perm–Gubacha–Kizel–Jajva–Berezniki | **hemelsbreed 1.472 km (station–SMZ), geen gepubliceerde spoorkm**; router 2.770 [14] | toets_spoorroute (6 runs, 1-op-1) | nee |

Geen last-mile-benen: spoorsnap 0,25 km (station) en 0,50 km (SMZ). Geen zeebeen, geen haven-aanloop, geen leiding.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-lgok-mijn` | mijn + verrijking (laadplek) | Lovozerski GOK, Karnasurt-mijn aan het Ilma-meer | 67.8888, 34.6177 | [5][11][13] | bron-gelegd (z15 gezien: mijn-/fabriekscomplex met gebouwen en bovengrondse galerij op de oostoever van het Ilma-meer, ontsloten door een weg; het punt ligt op dat complex). Dat het concentraat hier op de truck gaat is aannemelijk |
| `ree-olenegorsk-station` | overslag truck → spoor | Olenegorsk, goederenemplacement (OSM railway=station) | 68.1360, 33.3127 | [8][11][13] | **aannemelijk** (z15 gezien: tien-tal sporen met wagons, emplacement langs de Privokzalnoje sjosse). Geen bron noemt dit als spoorkop; het is het dichtstbijzijnde station volgens [8] |
| `ree-smz-solikamsk` | losplek + verwerker | Solikamsk Magnesium Works (OSM landuse industrial) | 59.6169, 56.7472 | [1][10][11][13] | bron-gelegd (z15 gezien: fabrieksterrein met hallen en schoorstenen, spoorbundel ~0,5 km ten westen) |

⚠️ Het ontwerp-punt `67.8888,34.6177` bleek het mijn-/fabrieksterrein zelf (niet alleen het afzettingsgebied); Revda (67.937, 34.559) is het dorp, geen laadplek. Ook 68.1417,33.2667 uit de haalbaarheidstoets is stadscentrum Olenegorsk, niet het station.

## 4 · Via-punten (alleen b2 — corridorkeuze; b1 volgt één weg)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Belomorsk, hoofdlijn | 64.5355, 34.7656 | Murmansk-lijn tot Belomorsk, daar de aftakking naar Obozerskaya in plaats van door naar Petrozavodsk (ontwerp) |
| b2 | 2 | Obozerskaya, hoofdlijn | 63.4521, 40.3110 | bevestigt de tak Belomorsk–Obozerskaya (snap 0,00 km) |
| b2 | 3 | Vologda, hoofdlijn | 59.2078, 39.8781 | de keuze Konosha–Vologda i.p.v. Kotlas: de vrije route via Kotlas (2.678–2.705 km) heeft een 145°/176°-wissel bij Kotlas en een 2,5 km-heen-en-terug-stomp bij Kirov (58.5129, 49.4467) die `--keerstraf 1000` niet oplost |
| b2 | 4 | Galich, hoofdlijn | 58.3737, 42.3354 | pint Vologda–Buj–Galich–Sjarja i.p.v. een tak via Danilov |
| b2 | 5 | Kotelnitsj, hoofdlijn | 58.2992, 48.3449 | Kirov wordt van het westen genaderd; geen omkering bij Kirov en geen via-punt in Perm (een via in Perm gaf zelf een 176°-keer) |

Runs (kop→via, via→via…, staart): r1 station→1 (537,2) · r2 1→2 (343,3) · r3 2→3 (501,7) · r4 3→4 (177,8) · r5 4→5 (366,8) · r6 5→SMZ (843,2) = **2.770,0 km**, 0 bochten ≥ 60°. Bestanden `spoorroute-ree-lovozero-solikamsk-b2-r1…r6-*.geojson` (r6 = `…-r6-kotelnich-smz`).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Lovozerski GOK (Karnasurt-mijn; Umbozero tot 2009) | Rosatom-Mining Division (sinds 2023) | loparietrijk erts → loparietconcentraat | 5,8 kt concentraat/j (2025); 12 kt in 2030 gepland; 2018: 2,7 kt REE2O3 in gemijnd erts | [1][4][6][7][9] |
| Solikamsk Magnesium Works | Rosatom (aandelen in overdracht) | loparietconcentraat → Ta/Nb-pentachloride/-oxide, titaan en een collectief concentraat van overige REE | niet gepubliceerd | [1][3][6] |

## 6 · Stoppunt
De brief stopt bij SMZ: de bronnen noemen alleen de producten (Ta, Nb, Ti, collectief REE-concentraat), geen afnemer of fabriek met naam en adres, dus fase D/E vervalt.

## 7 · Open punten
- **Modaliteit en spoorkop niet gebronnd.** Geen bron zegt hoe het concentraat de mijn verlaat; truck naar Olenegorsk (dichtstbijzijnde station, 65 km vanaf Revda [8]) en spoor naar Solikamsk is de enige logische keten, beennamen `(aannemelijk: geen bron voor spoorkop en modaliteit)`. Alternatief niet getekend: spoorkop in het Kirovsk/Koashva-gebied (spoorrouter snapt de mijn op 37,6 km, knoop 2431490, 67.6038, 34.1381).
- **b1-geometrie gebakken 2026-10-09** (zie §9): wegscan via Overpass (kumi) gelukt na uren 500-fouten; pyosmium blijft op deze machine geblokkeerd. Eerdere fallback (stippel last mile) niet nodig geweest.
- **Spoorcorridor is keuze, geen bewijs.** Geen bron noemt de route. Gekozen variant is ~65–90 km (+2,6%) langer dan de vrije route via Kotlas, maar zonder omkering. Variant Petrozavodsk–Vologda (ontwerp) niet gemeten.
- **Perm → SMZ**: router 302 km via Kizel–Jajva; ru.wikipedia noemt 368 km vanaf Perm via Tsjoesovskaja [10] (−18%); andere route of andere maat, niet uitgezocht. Geen gepubliceerde spoorkm voor b2: ±15%-toets vervalt, alleen indicatie.
- **SMZ-kopstuk**: spoorsnap 0,50 km, niet gezien dat het emplacement het terrein bereikt.
- **REO-gehalte** van het concentraat niet gepubliceerd; 12 kt (2030) is een doel, geen productie. Ontwerp-claim "SMZ 10–12 kt/j" door mij niet teruggevonden.
- **Sitelaag**: geen Russische site in `ree-sitelaag.json`; v1 `ree-russia` (67.80, 34.60) ligt ~10 km van de mijn. Centraal gelijktrekken.
- Sancties: binnenlandse stroom, geen exportdocumentatie; v1 noemt historische levering aan Silmet, hier niet getekend.

## 8 · Bronnen
[1] Interfax, Rosatom krijgt controle over LGOK; enige loparietproducent, levert aan SMZ. https://interfax.com/newsroom/top-stories/91073/
[2] AKM.ru, Rosatom kreeg controle over het Lovozerski GOK. https://www.akm.ru/news/rosatom_poluchil_kontrol_v_lovozerskom_gok/
[3] www1.ru, 2026-10-04, Karnasurt-mijn bereidt productie 2027 voor; concentraat naar SMZ (Ta, Nb, Ti, REE-concentraat). https://www1.ru/en/news/2026/10/04/pod-zemlei-karnasurta-prolozili-eshhe-3-km-lovozerskii-gok-gotovit-rudnik-k-dobyce-2027-goda.html
[4] www1.ru, 2025-11-12, drie nieuwe winblokken Karnasurt; concentraat naar Solikamsk. https://www1.ru/news/2025/11/12/rosatom-uvelicivaet-dobycu-redkozemelnyx-metallov-na-rudnike-karnasurt-v-murmanskoi-oblasti.html
[5] www1.ru, 2024-11-14, Karnasurt aan het Ilma-meer, 5 km zuidelijk van Revda; 5,2 Mt erts. https://www1.ru/news/2024/11/14/edinstvennoe-predpriiatie-v-strane-po-dobyce-loparita-lovozerskii-gorno-obogatitelnyi-kombinat-nacn.html
[6] 1prime.ru, 2025-08-11, capaciteit tot 12.000 t in 2030; levering aan SMZ. https://1prime.ru/20250811/gok-860545810.html
[7] RuNews24, 2026-09-03, 5,8 kt concentraat in 2025, doel 12 kt. https://runews24.ru/society/03/09/2026/lovozerskij-gok-narashhivaet-proizvodstvo-redkozemelnogo-syirya
[8] ru.wikipedia, Ревда (Мурманская область): station Olenegorsk 65 km per weg; Lovozero–Aikuvenn-spoor in 2007 ontmanteld. https://ru.wikipedia.org/wiki/Ревда_(Мурманская_область)
[9] ru.wikipedia, Ловозерское месторождение: concentraat → SMZ; 2018 REE2O3 2,7 kt. https://ru.wikipedia.org/wiki/Ловозерское_месторождение
[10] ru.wikipedia, Соликамск: eindstation Chusovaya–Solikamsk; 368 km vanaf Perm per spoor. https://ru.wikipedia.org/wiki/Соликамск
[11] OpenStreetMap/Nominatim (ODbL): landuse "Ловозерский ГОК" 67.88880, 34.61773; SMZ 59.61687, 56.74721; station Olenegorsk 68.13601, 33.31273. https://www.openstreetmap.org
[12] OSRM (router.project-osrm.org): mijn → station 76,2 km via 47К-047/47К-043. https://router.project-osrm.org
[13] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-ree-lovozero-solikamsk-{lgok,olenegorsk-stn,smz}.png`.
[14] Eigen metingen `toets_spoorroute.mjs` (BAKE_SUFFIX=-raw, 3.260.717 edges), 2026-10-09.

## 9 · Gebakken
## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)

**Stroom `ree-lovozero-solikamsk`** → `v2/data/stroomroute-ree-lovozero-solikamsk.json` — 7 benen (b1 = 1 truck, b2 = 6 spoorstukken), **2.866,6 km**, 7.405 punten, 3 markers, 131,2 KB. truck 75,9 km + spoor 2.790,7 km; geen stippel. Recept: `bak_stromen.sh` (functie `bak_ree_lovozero_solikamsk`); wegprofiel `ree-lovozero-solikamsk-lgok-olenegorsk` in `maak_stroombeen_weg.py`.

| # | modaliteit | km gebakken | km brief | naad | opmerking |
|---|---|---|---|---|---|
| b1 | truck | 75,9 (scan 75,8) | ~73 (65 wiki + 7,8 OSRM; OSRM 76,2) | — | +3,8% t.o.v. 73, binnen ±15%; doorgetrokken |
| b2-r1 | spoor Olenegorsk → Belomorsk | 540,9 | 537,2 | 0,25 | letterlijk de eerder gemeten geojson |
| b2-r2 | Belomorsk → Obozerskaya | 345,5 | 343,3 | 0,00 | |
| b2-r3 | Obozerskaya → Vologda | 503,3 | 501,7 | 0,00 | |
| b2-r4 | Vologda → Galich | 179,9 | 177,8 | 0,00 | |
| b2-r5 | Galich → Kotelnitsj | 369,4 | 366,8 | 0,00 | |
| b2-r6 | Kotelnitsj → SMZ | 851,7 | 843,2 | 0,00 | |

Som spoor 2.790,7 km tegen routerkm 2.770,0 (+0,7%: de bake meet de getekende polylijn, de router telt netkm). Er is geen gepubliceerde spoorkm; de ±15%-toets geldt niet als norm. Hemelsbreed station–SMZ 1.472 km, dus omwegfactor 1,90 voor de gekozen corridor.

**Markers (3):** LGOK 67.8888,34.6177 (0,00 km van de lijn) · Olenegorsk goederenemplacement 68.1360,33.3127 (0,00 km) · SMZ 59.6169,56.7472 (0,49 km van de lijn: de spoorsnap, niet gezien dat het emplacement het terrein bereikt).

**b1 (truck, wegscan):** `maak_stroombeen_weg.py --profiel ree-lovozero-solikamsk-lgok-olenegorsk --bron overpass`. Pyosmium is door beleid geblokkeerd (niet omzeild); `overpass-api.de` verbrak steeds de verbinding, `overpass.kumi.systems` gaf ruim een half uur HTTP 500 (ook op een klein venster) en leefde daarna weer; de eerste bake stond daarom tijdelijk met een stippel-fallback (60,9 km rechte lijn), die na de geslaagde scan is vervangen (tweede bake, hetzelfde json). Segmenten: mijn → Revda 7,7 · Revda → km 30 22,4 · → km 50 20,5 · → rotonde Olenegorsk 22,7 · → station 2,4 km; snaps 0,00-0,05 km. First mile over kleine klassen 14,8 km (residential/service/tertiary/unclassified), last mile 2,2 km. Ankerverbindingen plant → weg 0,05 km en weg → kade 0,04 km.

**Toets:** naden 0,25 km (truck → spoor, Olenegorsk) en verder 0,00 km, dus ruim onder 5 km. `toets_knikken.py`: 3 knikken ≥ 60° (106,5° / 100,7° / 88,1°, boogstraal 24-39 m, allemaal 'spike'), 0 omkeringen ≥ 150°, 0 terugloop: twee zijn de korte ankerverbindingen (mijn-anker 67.8888,34.6177 en emplacement 68.1360,33.3127, ca. 50-70 m) en één is een wegaansluiting bij 68.0033,34.5860 ten noorden van Revda; geen reparatie nodig. Spoorbenen 0 knikken. `toets_rechte_benen.py --min-km 5`: geen enkel Lovozero-been met omwegfactor 1,000. json: versie 2, punt_formaat lonlat, modaliteiten {truck, spoor}, elk been ≥ 2 punten (minimum 289), 131,2 KB.

**Lessen:**
- Het slot-sjabloon van de orkestrator (`rm -rf "$SLOT"`, en in `neem_slot` ook `rm -rf "$d"`) wordt door de veiligheidscontrole van Claude Code geblokkeerd omdat het pad uit een variabele komt. Werkt wel: slotmappen met een letterlijk pad aanmaken (`mkdir` op `…/slots/weg/slot1`…) en vrijgeven met `rmdir` op een letterlijk pad. Een agent die het sjabloon letterlijk draait, krijgt dus een afgewezen commando.
- `maak_stroombeen_weg.py --bron overpass` kent maar twee spiegels (overpass-api.de, kumi). Een spiegel die op een piepklein venster 200 geeft kan op het echte corridorvenster (~1° breed) nog wel 500 geven; opnieuw proberen met een tussenpoos van een minuut volstond uiteindelijk, de bake werkt dan met dezelfde lijn.
- Een tijdelijke fallback-stippel mag, maar de beennaam moet dan zeggen dat het een procesgat is en geen 'geen net'; hier is dat niet meer nodig.
