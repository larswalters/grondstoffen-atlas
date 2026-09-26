# Routebrief (licht) · kolen — Tavan Tolgoi → Gashuunsukhait/Ganqimaodu → Baotou (China)

**stroom-id:** `kolen-tavantolgoi-baotou` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) ·
**status:** gebakken
**Keten in één zin:** cokeskool van de ETT-laadterminal Tavan Tolgoi gaat per spoor 231 km over de
Tavantolgoi–Gashuunsukhait-lijn naar de grens, wordt (zolang de grensspoorlijn nog in aanbouw is) per
truck ~9–10 km overgezet naar de Chinese opslag/spoorzone Ganqimaodu, en vandaar per 甘泉铁路 369 km naar
het spooreindpunt Wanshuiquan-Zuid in Baotou — de enige koperzuster-keten zonder zee, nu voor kolen.
**Welke as van het verhaal:** Mongoolse cokeskool over land naar China. Mongolië leverde in 2025 **60,07 Mt**
cokeskool aan China = **51 %** van diens totale cokeskoolimport (CISA-cijfers via S&P Global) [6]; de
TT-GS-lijn heeft een ontwerpcapaciteit van 30 Mt/j [3]; Ganqimaodu zag jan. 2024 gemiddeld ~1.114
kolentrucks/dag over de weg [7], oplopend richting >1.400/dag in 2026 zolang de grensspoorlijn niet af is [6].

## 1 · Ketenkaart
ETT-laadterminal Tavan Tolgoi ──(b1 spoor · TT-GS-lijn · 231 km)──► Gashuunsukhait-overslag ──(b2 truck ·
grensoverslag · ~9–10 km)──► Ganqimaodu-opslag/spoorzone ──(b3 spoor · 甘泉铁路 · 369 km)──► Wanshuiquan-Zuid
(Baotou) ⏹ stoppunt fase C ──(b4 truck, aannemelijk, gestippeld · ~14 km hemelsbreed)──► Baotou Steel
(aannemelijk: één bron, sxcoal 2017)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-tt-laad` → `kolen-tt-gs` | Tavantolgoi–Gashuunsukhait-spoorlijn (Bodi International, 1520 mm, open sinds 09-2022) | 231 [2][3] (gemeten deze ronde op ruwe coördinaten, 233,6 gepubliceerd [2], −0,9 %) | toets_spoorroute (`BAKE_SUFFIX=-raw`, extract mongolia) | nee |
| b2 | A | truck | `kolen-tt-gs` → `kolen-ganqimaodu-opslag` | grensoverslag Gashuun Sukhait → poort Ganqimaodu; de grensspoorlijn (32,6 km, 1520+1435 mm, 40 Mt/j) is in aanbouw sinds 06-2025, ~10 % klaar 04-2026 [5] — vandaag dus per truck | ~9–10 (afgeleid uit de ankers; geen publicatie) | maak_stroombeen_weg (extracts mongolia + china; via `cu-ot-grens`) | nee |
| b3 | C | spoor | `kolen-ganqimaodu-opslag` → `kolen-baotou-eind` | 甘泉铁路 (Ganqimaodu-station → Wanshuiquan-Zuid op de Baoshen-lijn, 366,9 km, geëlektrificeerd enkelspoor, kolen uit Tavan Tolgoi, spoorleggen voltooid 2012-09-15) [9] | 369 (gemeten deze ronde op ruwe coördinaten, +0,5 % t.o.v. 366,9; anker nu verfijnd naar het exacte OSM-station — definitieve km bij het bakken) | toets_spoorroute (`BAKE_SUFFIX=-raw`, extract china) | nee |
| b4 | D | truck | `kolen-baotou-eind` → `kolen-baotou-baogang` | eigen terrein/laatste kilometers binnen Baotou; geen gekarteerde siding of weg gevonden tussen het spooreindpunt en de fabriekspoort | ~14 (hemelsbreed, geen route gemeten) | stippel | ja — "last mile (geen net op deze korrel), aannemelijk: één bron (sxcoal 2017)" |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-tt-laad` | mijn / laadplek | ETT-laadterminal Tavan Tolgoi ("Tavantolgoi Coal Terminal", automated loading logistics center, in bedrijf sinds mei 2024) | 43.64336, 105.58236 | OSM railway=station "Тавантолгой" + yard, way "Таван-Толгой — Гашуунсухайт" (operator ООО «Тавантолгойская железная дорога») [11]; Montsame [1] | bron-gelegd (z15 gezien: spoorbundel met opstelterrein en industriegebouwen direct naast de lijn, wegkruising ernaast — past bij de laadterminal) |
| `kolen-tt-gs` | overslag (spoor eind MN / truck-transfer) | Gashuunsukhait rail-yard | 42.44558, 107.53063 | OSM buffer_stop/yard-clusters op dezelfde way als hierboven [11] | bron-gelegd (z15 gezien: driehoekig opstelterrein met rijen wagons/voertuigen naast de spoorbundel, vlak vóór de grens) |
| `cu-ot-grens` | grensovergang (hergebruikt) | Gashuun Sukhait grenspost (MN) / Ganqimaodu (CN) | 42.4146, 107.5692 | koper-oyutolgoi-china.md §3 [12]; OSM `border_control` | bron-gelegd (eerder satelliet-gelegd, koperbrief; hier letterlijk hergebruikt) |
| `kolen-ganqimaodu-opslag` | overslag (truck→spoor, kop van 甘泉铁路) | Ganqimaodu-station + opslagloodsen | 42.37414, 107.60964 | OSM railway=station "甘其毛都" [11]; zh-wikipedia 甘泉铁路 (kopstation) [9] | bron-gelegd (z15 gezien: rijen blauwe en rode opslagloodsen direct naast een spoorlijn/kruising — past bij een kolenopslag-/overslagzone; niet aan een specifiek bedrijf gekoppeld) |
| `kolen-baotou-eind` | losplek / spooreindpunt (stoppunt fase C) | Wanshuiquan-Zuid station, Baotou | 40.57750, 109.89105 | OSM railway=station "万水泉南" [11]; zh-wikipedia 甘泉铁路 (eindstation op de Baoshen-lijn) [9] | bron-gelegd (z15 gezien: langwerpige loods/spoorbundel aan de stadsrand, aansluitend op het stedelijk spoornet) |
| `kolen-baotou-baogang` | fabriek (fase D, niet gerouteerd) | Baotou Steel (包钢), staalwerken | 40.65490, 109.75450 | OSM man_made=works "包钢炼钢厂" [11]; sxcoal 2017 noemt Baogang als hoofdafnemer [8] | aannemelijk (z15 gezien: groot zwaar-industrieel complex met hoogovens, tanks en hallen — past bij een staalfabriek; de koppeling van déze kolenstroom aan dit terrein rust op één, gedateerde bron) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Chinese poort Ganqimaodu | 42.4089, 107.5743 | pint "door de douanepoort" i.p.v. een sluiproute om de poortzone heen (hergebruikt uit koper-oyutolgoi-china.md §4) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Baotou Steel (包钢), Kundulun-district | Baotou Iron & Steel (Group) Co. | Mongoolse cokeskool → cokes/ruwijzer (samen met binnenlandse kool en de Wuhai-cokerijen) | onbekend (geen gepubliceerd aandeel) | [8] |

## 6 · Stoppunt
De brief stopt hard bij `kolen-baotou-eind` (Wanshuiquan-Zuid): dat is het bewezen eindpunt van 甘泉铁路
en het spoor is tot hier gemeten. Het vierde been naar Baotou Steel wordt getekend omdat één bron
(sxcoal 2017) de fabriek noemt — precies de "D alleen als één bron de fabriek noemt"-regel — maar zonder
gekarteerde siding of weg erheen; die 14 km blijft daarom gestippeld "last mile" én "aannemelijk" in de
beennaam. Fase E vervalt: geen bron noemt een vervolgbestemming voor Baogangs cokes/ruwijzer.

## 7 · Open punten
- **Afnemer-identiteit:** de enige naamnoeming van Baotou Steel als afnemer is sxcoal 2017 [8]; een
  arxiv-bron uit 2026 noemt Baotou's grondstofmix alleen als "domestic + imported Outer Mongolia" zonder
  bedrijfsnaam — de keten kan eerlijk ook eindigen bij `kolen-baotou-eind` zonder b4.
- **Rail/truck-split op b1/b2:** niet gepubliceerd hoeveel van de 60,07 Mt daadwerkelijk over de TT-GS-lijn
  gaat versus over de parallelle truckweg.
- **Grensspoor in aanbouw:** de grensoverschrijdende lijn Gashuunsukhait–Ganqimaodu (32,6 km) vervangt b2
  zodra hij klaar is (2027 volgens de bouwdatum in [10]); vandaag is b2 nog truck.
- **b4-geometrie:** geen OSM-siding of -weg gevonden tussen Wanshuiquan-Zuid en Baogang; 14 km is
  hemelsbreed, geen gerouteerde afstand.
- **km b1/b3:** gemeten deze ronde op ruwe (niet-satelliet-gelegde) coördinaten; met de nu verfijnde
  ankers (bron-gelegd op de exacte OSM-stations) kunnen de bake-cijfers een paar km afwijken van 231/369.

## 8 · Bronnen
[1] Montsame, "Tavantolgoi Coal Terminal to Commence in the Second Quarter of This Year" (opening automated loading logistics center, mei 2024) — https://www.montsame.mn/en/read/344284
[2] Railway Authority of Mongolia — TT-GS-lijn 233,6 km — https://en.railway.gov.mn/n/56
[3] International Railway Journal, "Mongolia celebrates opening of Tavantolgoi-Gashuunsukhait railway" (1520 mm, capaciteit 30 Mt/j, open 09-2022) — https://www.railjournal.com/freight/mongolia-celebrates-opening-of-tavantolgoi-gashuunsukhait-railway/
[4] AG Metal Miner, "Mongolia rail link to China aims to ease coking coal bottleneck" (2025-04-11) — https://agmetalminer.com/2025/04/11/mongolia-rail-link-china-coking-coal/
[5] Mongolian Mining Journal — grensspoor Gashuunsukhait–Ganqimaodu 32,6 km, 1520+1435 mm, 40 Mt/j, bouwstart 06-2025, ~10 % gereed 04-2026 — https://www.mongolianminingjournal.com/a/74961
[6] S&P Global, "China's Mongolian coking coal demand seen higher in 2026 on blending, supply curbs" — 60,07 Mt Mongoolse cokeskool 2025 = 51 % van China's import; >1.400 trucks/dag verwacht Ganqimaodu 2026 — https://www.spglobal.com/energy/en/news-research/latest-news/metals/061726-ferrous-week-chinas-mongolian-coking-coal-demand-seen-higher-in-2026-on-blending-supply-curbs
[7] Mysteel, "Mongolian coal stocks at China's Ganqimaodu refresh record high" — ~1.114 kolentrucks/dag, jan. 2024 — https://www.mysteel.net/news/5049034-mongolian-coal-stocks-at-chinas-ganqimaodu-refresh-record-high
[8] sxcoal, "China coking coal — key findings from a field trip" — Baotou Steel en de Wuhai-cokerijen als hoofdafnemers van Mongoolse cokeskool (2017) — https://sxcoal.substack.com/p/china-coking-coal-key-findings-from
[9] 维基百科, 甘泉铁路 — Ganqimaodu-station → Wanshuiquan-Zuid, 366,9 km, geëlektrificeerd enkelspoor, kolen uit Tavan Tolgoi, spoorleggen voltooid 2012-09-15 — https://zh.wikipedia.org/wiki/甘泉铁路
[10] 维基百科, 甘其毛都口岸 — grenspost 42°24'35"N 107°34'23"E; bouwstart grensspoorlijn 2025-05-14 — https://zh.wikipedia.org/zh-hans/甘其毛都口岸
[11] OpenStreetMap-bijdragers (via Overpass API) — railway=station "Тавантолгой"/"甘其毛都"/"万水泉南", way "Таван-Толгой — Гашуунсухайт", man_made=works "包钢炼钢厂" (ODbL) — https://www.openstreetmap.org/copyright
[12] koper-oyutolgoi-china.md, v2/design/routebrieven (deze repo) — hergebruikt anker `cu-ot-grens` en via-punt "Chinese poort Ganqimaodu"; bron [17] daar = zh-wikipedia 甘泉铁路 (identiek aan [9] hierboven)

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `kolen-tavantolgoi-baotou`** → `v2/data/stroomroute-kolen-tavantolgoi-baotou.json` — 4 benen, 625,9 km, 6 markers: spoor 227,3 km · truck 13,6 km · spoor 370,6 km · truck (stippel) 14,4 km.
Recept: `bak_stromen.sh` (functie `bak_kolen_tavantolgoi_baotou`). Toelichting per been: b1 (ETT-laadterminal Tavan Tolgoi → Gashuunsukhait rail-yard, `toets_spoorroute.mjs`, `BAKE_SUFFIX=-raw`, extract mongolia) is 227,3 km tegen 233,6 km gepubliceerd (−2,7%, binnen ±15%) — één scherpe bocht (172,8°, ~20 m boogstraal) vlak bij de laadterminal, een echte kopmaak-plek op het opstelterrein (Chuqui/Matarani-klasse, emplacement niet perfect op het 1-op-1-net), geen via-punt bijgeschoven. b2 (Gashuunsukhait-overslag → grenspost → Chinese poort → Ganqimaodu-opslag, `maak_stroombeen_weg.py`, profiel `kolen-tavantolgoi-baotou-tt-gs-ganqimaodu`, extracts mongolia+china) meet 13,6 km — er is geen gepubliceerde lengte (brief: ~9–10 km afgeleid uit de ankers), dus de lengtetoets is indicatief; de via-punten `cu-ot-grens` en "Chinese poort Ganqimaodu" zijn letterlijk hergebruikt uit `koper-oyutolgoi-china.md` (identieke coördinaten, geen nieuwe scan op die punten). b3 (Ganqimaodu-station → Wanshuiquan-Zuid, Baotou, `toets_spoorroute.mjs`, extract china) is 370,6 km tegen 366,9 km gepubliceerd (+1,0%, ruim binnen ±15%), 0 knikken/omkeringen. b4 is een pure redactionele stippel (geen bake-tool): "last mile Baotou Steel (aannemelijk: één bron, sxcoal 2017) — geen gekarteerde siding", 14,4 km hemelsbreed tussen `kolen-baotou-eind` en `kolen-baotou-baogang` (omwegfactor 1,001).

Stippels: (1) b4, last mile Wanshuiquan-Zuid → Baotou Steel (14,4 km) — de brief zegt expliciet dat er geen infrastructuur is gevonden tussen het spooreindpunt en de fabriekspoort; niet geroutet, geen wegscan uitgevoerd (per instructie). Alle overige benen zijn gemeten en doorgetrokken.

Gereedschapslessen: (a) het b2-wegprofiel scoort 16 knikken van het type "spike" (OSM-zigzags in de nauwe grens-/douanezone, veelal <100 m boogstraal) maar 0 omkeringen ≥150° en 0 terugloop (`toets_knikken.py`) — de lijn kronkelt door een dichtbebouwde poortzone maar keert nergens fysiek om; geen via-punt bijgeschoven om het beeld gladder te maken. (b) hergebruik van een bestaand anker (`cu-ot-grens`) en een bestaand via-punt (Chinese poort Ganqimaodu) uit een andere stroom werkte zonder wrijving: beide lagen al binnen het venster van het nieuwe profiel en de scan sloot er zonder handmatige correctie op aan. (c) de spoorbenen b1/b3 zijn nu gemeten op de satelliet-gelegde (in plaats van ruwe) ankers uit §3 van deze brief; de uitkomst (227,3 / 370,6 km) wijkt een paar km af van de eerdere ruwe-coördinaten-meting (231 / 369 km) uit de briefschrijfronde, zoals open punt 5 van §7 al voorzag — beide liggen ruim binnen de ±15%-band. Toetsen geslaagd: `toets_knikken.py` (0 terugloop) · `toets_rechte_benen.py --min-km 5` (alleen b4-stippel gevlagd, verwacht en toegelicht) · markers alle ≤ 0,5 km van de lijn (max 188 m, kop Tavan Tolgoi) · json.load/versie 2/punt_formaat lonlat/modaliteiten {spoor, truck}/elk been ≥2 punten/bestand 17,8 KB, allemaal binnen de norm. Geen naad > 5 km (max 0,23 km, tussen b2 en b3).
