# Routebrief (licht) · kolen — Bogatyr → Presnogorkovskaya → Reftinskaya (Kazachstan → Rusland)

**stroom-id:** `kolen-bogatyr-reftinskaya` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** Ekibastuz-thermisch kolen van de Bogatyr-dagbouw (Bogatyr Komir LLP, Pavlodar) per spoor, in treinen
van ~65 wagons, over het Kazachse net via de Astana-regio naar het overdrachtsstation Presnogorkovskaya vlak vóór de
Russische grens [5], en vandaar over het Russische net (Kurgan → Shadrinsk → Kamyshlov) naar het aflaademplacement van
Reftinskaya GRES (3.800 MW) bij Asbest — een mijn → afnemer-keten over een staatsgrens, zonder zee.
**Welke as van het verhaal:** as 6 — de ene Kazachs-Russische grensoverschrijdende kolenstroom: Reftinskaya is ontworpen op
Ekibastuz-kool [2][4]. **Jaarvolume:** ~10,1 Mt kolen/j in 2022 [1]; contract 10,4 Mt/j tot 31-12-2027 [4]; jan–apr 2024 2,584 Mt
naar Rusland [3] (afgeleide run-rate ≈ 7,8 Mt/j). Peiljaar 2022–2025, eenheid Mt kolen per jaar.

## 1 · Ketenkaart
```
Bogatyr-dagbouw `kolen-bogatyr-laad` ──(b1 spoor · Ekibastuz → Astana-regio → Kokshetau-west · 949,9 km)──►
Presnogorkovskaya `kolen-presnogorkovskaya-grens` ──(b2 spoor · Kurgan → Shadrinsk → Kamyshlov → Asbest · 497,2 km)──►
Reftinskaya-aflaadstation `kolen-reftinskaya-aflaad` ⏹ stoppunt (eigen emplacement 33 km, geen been)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b0 | A | spoor | `kolen-bogatyr-laad` → hoofdnet | mijn-eigen railaansluiting ontbreekt in OSM | 1,1 (gemeten snap) | stippel | ja — "last mile (geen net op deze korrel)" |
| b1 | A | spoor | hoofdnet → `kolen-presnogorkovskaya-grens` | Presnogorkovskaya–Pavlodar-lijn via Astana-regio [5][6]; **aannemelijk: één bron** (KTZ noemt eindstation, corridor = kortste OSM-pad) | hemelsbreed 697 km, geen spoorkm; gemeten 949,9 | toets_spoorroute `-raw`, 2 runs | nee |
| b2 | A | spoor | `kolen-presnogorkovskaya-grens` → `kolen-reftinskaya-aflaad` | Kurgan → Shadrinsk → Kamyshlov → Asbest-tak; **aannemelijk** (geen bron voor de Russische traversal) | hemelsbreed 404 km, geen spoorkm; gemeten 497,2 | toets_spoorroute `-raw`, 3 runs | nee |

Totaal gemeten 1.447,1 km (+1,1 km stippel) tegen hemelsbreed 1.073 km (verhouding 1,35) en 1.428 km wégafstand (opgave
avtodispetcher, geen spoorkm, pagina niet te openen [11]) = +1,3 %. Geen gepubliceerde spoorlengte → de ±15 %-toets is een indicatie.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-bogatyr-laad` | mijn / laadplek | Bogatyr-dagbouw (Bogatyr Komir LLP), Ekibastuz-bekken, Pavlodar | 51.6555, 75.4336 | [1] GEM exact; sitelaag `w-bogatyr` [10] | bron-gelegd (z15 gezien: enorme dagbouwput met banken en haulwegen, GEM-punt ligt in de put zelf; ~3,4 km NO een kolenverlaadcomplex met transportbanden uit de put en sporen onder laadsilo's, niet in het OSM-net — zie §7) |
| `kolen-presnogorkovskaya-grens` | overdrachtsstation (grens) | station Presnogorkovskaya (KTZ), dorp Presnogorkovka, Uzunkol, Kostanay | 54.4375, 66.0726 | [5] KTZ noemt het "on the border with Russia"; OSM `railway=station` [8] | bron-gelegd (z15 gezien: meersporig N–Z-emplacement dwars door het dorp; het station ligt ~35 km vóór de grens: de lijn verlaat de Kazachstan-extract bij 54.7515, 65.9723) |
| `kolen-reftinskaya-aflaad` | losplek / afnemer | Reftinskaya GRES (SGK/Kuzbassenergo), Asbest, Sverdlovsk | 57.1108, 61.7059 | [2] GEM exact; OSM 57.1127, 61.7055 bevestigt | bron-gelegd (z15 gezien: centrale met pluim, twee grote kolenstapels en een brede ontvangstbundel sporen direct oostelijk; router snapt op 0,3 km) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Kokshetau-west, op de lijn naar Presnogorkovskaya (snap 1,2 km op knoop 53.2348, 67.6022) | 53.2342, 67.6203 | kiest de westtak naar Presnogorkovskaya i.p.v. de Petropavlovsk–Petukhovo-oversteek (vrij Dijkstra: 1.438 km via Petropavlovsk, geen Presnogorkovskaya) |
| b2 | 2 | Kurgan–Shadrinsk-lijn (snap 0 km) | 55.9150, 64.0044 | pint de Kurgan–Shadrinsk–Kamyshlov-doorsteek i.p.v. een omweg via Chelyabinsk |
| b2 | 3 | Kamyshlov-regio (snap 1,8 km op knoop 56.3445, 62.4648) | 56.3584, 62.4489 | pint de aansluiting op de Asbest-tak; elk via ligt óp de doorgaande lijn, niet in een centrum |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Bogatyr-dagbouw | Bogatyr Komir LLP (Samruk-Energy 50 % / RUSAL 50 %) | dagbouw → thermisch kolen | 32,5 Mt/j (2024; 2022: 32,5) | [1] |
| Reftinskaya GRES | Kuzbassenergo / SGK (SUEK) | Ekibastuz-kolen → elektriciteit | 3.800 MW; verbruik ~12 Mt/j, ~22 mld kWh/j; 55 treinen van 65 wagons (~4,5 kt/trein) op de keten | [2][4] |

## 6 · Stoppunt
De brief stopt op het aflaadstation van Reftinskaya: de centrale is de enige gebronde afnemer en het eigen emplacement (33 km
spoor [4]) is geen been. Fase D (as/slakken, elektriciteit) en E vervallen: geen bron noemt een vervolglocatie van de lading.

## 7 · Open punten
- **Bogatyr-laadstation niet gelegd:** het verlaadcomplex (51.6855, 75.4740, z16 gezien: banden uit de put, sporen onder laadsilo's) is niet
  door een bron genoemd en ligt 2,7 km van het OSM-hoofdnet; daarom ankert b0 op het GEM-punt met een korte stippel (1,1 km).
- **Spoorkm niet gepubliceerd** voor Ekibastuz → Presnogorkovskaya en Presnogorkovskaya → Asbest; de 949,9/497,2 km zijn router-metingen.
- **Corridor aannemelijk, niet bevestigd:** bron [5] zegt alleen "Ekibastuz-2 → Presnogorkovskaya"; de Astana-regio-doorgang (KTZ-lange treinen
  naar "de hoofdstad") en de Russische traversal Kurgan → Shadrinsk → Kamyshlov zijn het kortste OSM-pad, zonder bron.
- **Presnogorkovskaya ligt ~35 km vóór de grens** (OSM-spoor Kazachstan-extract eindigt 54.7515, 65.9723); het grensstation aan Russische zijde is niet gepind (geen bron, geen gok).
- **b2 eindigt met een 176°-omkering** bij 57.1042, 61.7182 (boogstraal ~88 m): kopmaakplek in het centrale-emplacement, geen sluiproute.
- **Reftinskaya ontbreekt in `kolen-sitelaag.json`** (centraal toevoegen; GEM 3.800 MW, 57.1108/61.7059; verbruik ~12 Mt/j).
- **Volume onzeker:** contract loopt tot 31-12-2027, leveringsstop/-daling in 2024 (jan–apr 2,6 Mt) [3][4]; Reftinskaya zoekt vervanging [2].
- `ruwiki.ru` Reftinskaya-pagina gaf 401; avtodispetcher-pagina toonde een beveiligingscheck — 1.428 km niet zelf geverifieerd.

## 8 · Bronnen
[1] Global Energy Monitor, Bogatyr Coal Mine (Kazakhstan) — 51.655495, 75.4336006; 32,53 Mt (2024), 30,8–34,9 Mt (2017–2024); export Reftinskaya 10,1 Mt (2022). https://www.gem.wiki/Bogatyr_Coal_Mine_(Kazakhstan)
[2] Global Energy Monitor, Reftinskaya GRES power station — 57.110841, 61.705909; 3.800 MW; Kuzbassenergo/SGK/SUEK; Ekibastuz-kool 10,4 Mt/j (april 2025), contract tot 2027. https://www.gem.wiki/Reftinskaya_GRES_power_station
[3] inbusiness.kz, "Богатырский уголь продолжает идти в Россию" (09-05-2024) — jan–apr 2024 2.584 kt naar Rusland (2023: 3.343 kt); tot 10 Mt/j naar Reftinskaya. https://www.inbusiness.kz/ru/news/bogatyrskij-ugol-prodolzhaet-idti-v-rossiyu
[4] inbusiness.kz, "«Богатырь» продолжит греть Россию" (2025) — contract 10,4 Mt/j t/m 31-12-2027; 55 treinen × 65 wagons, 4,5 kt/trein; plant-emplacement 33 km; verbruik ~12 Mt/j. https://www.inbusiness.kz/ru/news/bogatyr-prodolzhit-gret-rossiyu
[5] Kazakhstan Temir Zholy, "About 3 thousand record trains were sent from Ekibastuz-2 station" (03-09-2024) — 97 zware kolentreinen jan–jul 2024 (407 in 2023) naar station Presnogorkovskaya "on the border with Russia". https://www.railways.kz/en/news/about-3-thousand-record-trains-were-sent-ekibastuz-2-station/
[6] Lengiprotrans, Ekibastuz-spoorknoop (alleen zoekresultaat-tekst, pagina niet te openen): Presnogorkovskaya–Pavlodar-lijn via Novoishimskaya. https://lgt.ru/en/node/1266
[7] Wikipedia (ru), Пресногорьковка / Троебратский — dorp in Uzunkol, oblast Kostanay; station Пресногорьковская. https://ru.wikipedia.org/wiki/Пресногорьковка
[8] OpenStreetMap-bijdragers via Photon/Nominatim — railway=station "Пресногорьковская" 54.4375, 66.0726; Petropavl 54.8564, 69.1704; Petukhovo 55.0715, 67.8880 (ODbL). https://www.openstreetmap.org/copyright
[9] Eigen metingen `toets_spoorroute.mjs` (`BAKE_SUFFIX=-raw`, 3.260.717 spoor-edges), 5 runs `spoorroute-kolen-bogatyr-reftinskaya-b1a…b2c.geojson`; vrije run Bogatyr → Reftinskaya: 1.438 km via Petropavlovsk/Petukhovo.
[10] `v2/design/kolen-sitelaag.json`, site `w-bogatyr` (GEM, aannemelijk, 32,53 Mt).
[11] avtodispetcher.ru, Экибастуз → Рефтинский (wegafstand 1.428 km, opgave ontwerp; pagina niet bereikbaar). https://www.avtodispetcher.ru/distance/
[12] Esri World Imagery via `sat_check.py` (z15/z16) — `v2/build-cache/satcheck/sat-kolen-bogatyr-reftinskaya-{bogatyr-laad,bogatyr-laadstation,presnogorkovskaya,reftinskaya}.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Recept:** `bash v2/tools/bak_stromen.sh kolen-bogatyr-reftinskaya` (functie `bak_kolen_bogatyr_reftinskaya`) → `v2/data/stroomroute-kolen-bogatyr-reftinskaya.json`
(37,4 KB, versie 2, `lonlat`). Spoorruns onder `BAKE_SUFFIX=-raw` (3.260.717 spoor-edges), vooraf gebakken in `v2/build-cache/ais/graaf/`
(`spoorroute-kolen-bogatyr-reftinskaya-{b1a,b1b,b2a,b2b,b2c}-….geojson`); bake-log `kolen-bogatyr-reftinskaya-bake.log` ernaast.
Geen wegprofiel, geen zee, geen leiding, geen lucht, geen haven-aanloop, geen gedeelde benen, geen eigen extracts.

| # | modaliteit | been | km gebakken | km brief | naad naar volgende | stippel |
|---|---|---|---|---|---|---|
| b0 | spoor | last mile Bogatyr-dagbouw → hoofdnet (51.6555,75.4336 → 51.6475,75.4437) | 1,1 | 1,1 (snap) | 0,00 | ja: net reikt niet (mijn-railaansluiting ontbreekt in OSM) |
| b1a | spoor | Bogatyr → via Kokshetau-west (53.2342,67.6203) | 751,2 | 746,8 | 0,00 | nee |
| b1b | spoor | via Kokshetau-west → Presnogorkovskaya | 203,6 | 203,1 | 0,00 | nee |
| b2a | spoor | Presnogorkovskaya → via Kurgan-Shadrinsk (55.9150,64.0044) | 243,3 | 241,8 | 0,00 | nee |
| b2b | spoor | via Shadrinsk → via Kamyshlov-regio (56.3584,62.4489) | 114,8 | 114,2 | 0,00 | nee |
| b2c | spoor | via Kamyshlov → Reftinskaya (aflaad, staart 0,3 km van marker) | 142,5 | 141,2 | — | nee |

Totaal **1.456,5 km** in 6 benen (1,1 km stippel, 1.455,4 km doorgetrokken), 2.052 punten, 3 markers. b1 = 954,8 km, b2 = 500,6 km.
**Naden:** alle 0,00 km (max 0,00 km), dus geen haven-aanloop of extra stippel nodig. **Markers:** Bogatyr 0 m, Presnogorkovskaya 16 m,
Reftinskaya 315 m van de lijn (≤ 0,5 km; het GEM-punt ligt op de centrale, de router eindigt op het ontvangstemplacement).

**Toets (handleiding §5):**
- **Km:** er is geen gepubliceerde spoorlengte, dus geen bindende ±15%-toets. De gebakken polylijn-km liggen +0,5% (b1) en +0,7% (b2)
  boven de router-km uit de brief (949,9 / 497,2): de baker meet de getekende lijn, de router telt edge-lengtes. Totaal 1.455,4 km
  tegen 1.428 km wegafstand uit het ontwerp = +1,9% (indicatie, niet geverifieerd).
- **`toets_knikken.py`:** 1 knik ≥ 60° en 1 omkering (176,0°, boogstraal 25 m) bij **57.1042, 61.7182**, gelabeld TERUGLOOP: de kopmaak
  in het Reftinskaya-emplacement die de brief al noemt (§7). Geen andere knikken of omkeringen in b1/b2a/b2b.
- **`toets_rechte_benen.py --min-km 5`:** geen enkel been van deze stroom gevlagd (b0 is 1,1 km en dus onder de drempel; b1/b2
  hebben omwegfactoren 1,34 / 1,22 / 1,16 / 1,08 / 1,47 ten opzichte van de hemelsbreedte van het eigen been).
- **JSON:** `json.load` slaagt, `versie` 2, `punt_formaat` `lonlat`, alle benen `spoor`, elk been ≥ 2 punten, 37,4 KB.

**Toelichting stippel:** alleen b0 (Bogatyr-dagbouw → hoofdnet, 1,1 km): het GEM-putpunt ligt in de dagbouwput zelf, de mijn-eigen
railaansluiting en het verlaadcomplex (51.6855,75.4740, z16, 2,7 km van het net) zijn niet door een bron genoemd en staan niet in OSM.
Er is geen luchtbeen, geen leiding en geen haven-aanloop. "Aannemelijk" (één bron voor het grensstation, geen bron voor de Russische
traversal) staat in de beennamen, niet in de lijnstijl.

**Lessen / aandachtspunten:**
- Een vrije spoorrun Bogatyr → Reftinskaya (1.438 km via Petropavlovsk/Petukhovo) komt niet langs Presnogorkovskaya: het via-punt
  Kokshetau-west (snap 1,2 km) is hier dus corridor-bepalend; de via-snaps van 0–1,8 km liggen alle op de doorgaande lijn.
- De spoorruns waren al gebakken; deze bake heeft ze alleen aan elkaar gehecht (alle naden 0,00 km). De extracts `kazachstan`,
  `rusland-oeral` en `rusland-siberie` waren voldoende, er is niets gedownload.
- Registerregel en sitelaag-actie (Reftinskaya ontbreekt in `kolen-sitelaag.json`) blijven centraal; dit bestand raakt geen register of bundel.

