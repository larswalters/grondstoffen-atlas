# Routebrief (licht) · Koper · Mount Milligan → Mackenzie → Vancouver Wharves (Canada)

**stroom-id:** `koper-mountmilligan-vancouver` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** koperconcentraat van de Mount Milligan-mijn (Centerra, BC) per **truck** over een private/forest-service-weg naar het CN-verlaadpunt in **Mackenzie**, dan per **CN-spoor** (Prince George, ex-BC Rail via Quesnel, Williams Lake, Lillooet, Squamish) naar **Vancouver Wharves** (North Vancouver), waar het in bulkschepen gaat. Twee landbenen, stoppunt bij de kade.
**Welke as van het verhaal:** BC-concentraat naar de Pacifische kust. **26,3 kt Cu per jaar** (57,9 Mlb betaalbaar koper verkocht, 2024; omrekening eigen: 57.897 klb x 0,4536) [1]. Afzet 2025 volgens de AIF: ca 140.000 t concentraat, 2026 130.000 t, 2027 120.000 t [1].

## 1 · Ketenkaart
Mount Milligan-concentrator `cu-mountmilligan-laad` ──(b1 truck · Community Connector FSR / Finlay-Causeway FSR → Mackenzie · hemelsbreed 59 km, geen wegkm; OSM-route ca 98)──► Mackenzie Yard `cu-mackenzie-verlaad` ──(b2 spoor · CN → Prince George → ex-BC Rail Quesnel–Williams Lake–Lillooet–Squamish · 942 km gemeten)──► Vancouver Wharves `cu-vancouverwharves-kade` ── stoppunt (geen benoemde afnemer)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `cu-mountmilligan-laad` → `cu-mackenzie-verlaad` | Finlay Philip / North Philip FSR (Centerra AIF [1]); in OSM: Community Connector FSR + Finlay-Causeway FSR (tertiary, deels unpaved), dan Hwy 39 (29 km [4]) naar Mackenzie; de weg naar Mackenzie is privé [6] | **hemelsbreed 59 km, geen wegkm**; indicatie OSRM 97,9 km (toets) en OSM-route ca 98 km, geen bron | maak_stroombeen_weg (extract canada, corridorKlassen, eindToegangPrivaat) | nee; FSR als highway=track: dan stippel met reden |
| b2 | B | spoor | `cu-mackenzie-verlaad` → `cu-vancouverwharves-kade` | CN Mackenzie → Prince George; ex-BC Rail (PGE) Quesnel – Williams Lake – Lillooet – Squamish – North Vancouver [1][5] | **hemelsbreed 666 km, geen spoorkm**; gemeten 942,2 km. Indicatie: North Vancouver–Prince George 744 km (462,5 mijl, 1950s-dienstregeling, eigen omrekening [5]) + Mackenzie–Prince George 184 km weg [7] = ca 928 km, gemeten +1,5% | toets_spoorroute (raw1op1 canada) | nee |

Geen zeebeen, geen haven-aanloop (stoppunt op de kade), geen last-mile-beentje: b1 eindigt op het yard-anker, b2 op het kade-anker. Het Wharves-anker is gedeeld met `zilver-reddog-trail` (daar het zee- en spoorbeen van Red Dog), maar b2 loopt een ander spoor: geen kopie.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-mountmilligan-laad` | mijn / laadplek (concentrator) | Mount Milligan Mine, verwerkingsinstallatie (Centerra) | 55.1099, -124.0130 | [1][6][8] | **bron-gelegd** (z15 gezien: groot concentratorgebouw met opslagloodsen en kleine gebouwen, open pit NW, tailingsvijver NO; kruis in het plantterrein) |
| `cu-mackenzie-verlaad` | overslag truck → spoor | Mackenzie Yard (CN, OSM railway=yard) | 55.3050, -123.1498 | [1][2][9] | **aannemelijk** (z15 gezien: smalle emplacementsbundel met wagons en bedrijventerrein ernaast; de verlaadinstallatie van Centerra is nergens gelokaliseerd, zie §7) |
| `cu-vancouverwharves-kade` | overslag spoor → schip (kade) | Vancouver Wharves, 50 Philip Ave, North Vancouver (Pembina) | 49.3155, -123.1141 | [3] | **aannemelijk, hergebruikt letterlijk** uit `zilver-reddog-trail.md` §3 (`ag-vancouver-wharves`: bulkterminal met loodsen, schip aan de kade; spoor-snap 0,01 km, bevestigd door de spoorrun hier) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Uit de bindende haalbaarheidstoets (lon, lat in het profiel; hier lat, lon). Eerste en laatste punt zijn de ankers. b2 heeft geen via-punt nodig: de router rijdt vanzelf de ex-BC Rail-lijn.
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | oostelijk van de mijn, FSR | 55.1290, -123.9530 | pint de uitgang oostwaarts via de Community Connector FSR i.p.v. de westroute via Fort St. James (North Road / Rainbow FSR [1]) |
| b1 | 2 | FSR halverwege | 55.0980, -123.6470 | pint de zuidelijke bocht van de FSR-corridor (Finlay-Causeway) |
| b1 | 3 | FSR nabij Mackenzie | 55.1150, -123.2480 | pint de aansluiting op de weg naar Mackenzie (Hwy 39-kant) |
| b1 | 4 | toegang Mackenzie | 55.2800, -123.1060 | pint de doorgaande weg Hwy 39, niet een zijtak; 3,5 km voor het yard |
| b2 | - | (geen) | - | CN/BC Rail-corridor gemeten: Prince George 2,2 km, Quesnel 0,4, Williams Lake 0,5, Lillooet 0,3, Squamish 0,3 van de lijn; Fraser Canyon (Kamloops) 97 km ernaast, dus niet gekozen |

## 5 · Verwerkingsknopen
Geen: de Mount Milligan-installatie (ca 62.500 t erts per dag [8]) is het begin; concentraat blijft concentraat tot de kade. Vancouver Wharves is overslag, geen verwerking (4 kaaien, covered storage 500.000 t droge bulk [3]).

## 6 · Stoppunt
De brief stopt op de kade van Vancouver Wharves: Centerra noemt alleen "various smelters and off-take purchasers" en twee meerjarige verkoopcontracten, geen naam of haven [1]; een profielpagina noemt alleen landen (Japan, Korea, Filipijnen) [8]. Fase D en E vervallen.

## 7 · Open punten
- **Wegkilometers niet gebronnen:** hemelsbreed 59 km, geen wegkm; de 98 km is OSRM/OSM, geen bedrijfsopgave. Een profielpagina zegt "40 km west-zuidwest van Mackenzie" [8], wat niet klopt met 59 km hemelsbreed tot het yard; de AIF geeft geen afstand [1].
- **Verlaadplek Mackenzie:** de Centerra-loadout is niet gelokaliseerd; het CN-yard is het aannemelijke punt.
- **Wegtype FSR:** Finlay Philip/North Philip FSR kunnen als highway=track getagd zijn; de OSM-route loopt via tertiary/unclassified stukken (haalbaarheidstoets). Waar de scanner geen pad vindt wordt dat deel een stippel met reden.
- **Spoorkm:** geen gepubliceerde totale lengte; de 928 km-indicatie is eigen optelling (1950s-mijlen + wegafstand) en geen norm.
- **Afnemers:** niet genoemd; stoppunt is de kade.
- **Jaarvolume:** 26,3 kt is verkocht betaalbaar koper; het geproduceerde betaalbare koper (ontwerp: 54,3 Mlb, 24,6 kt) is hier niet apart geverifieerd.
- **Sitelaag:** Mount Milligan en Vancouver Wharves ontbreken in `koper-sitelaag.json` (centraal).

## 8 · Bronnen
[1] Centerra Gold, 40-F FY2024, Mount Milligan-sectie (trucking naar Mackenzie, CN-spoor naar Vancouver Wharves, Finlay Philip/North Philip FSR, 155 km NW van Prince George, 57.897 klb betaalbaar koper 2024, 140 kt concentraat 2025), https://www.sec.gov/Archives/edgar/data/1854640/000110465925028841/tm2510622d1_ex99-1.htm
[2] OSM-station/yard "Mackenzie Yard" (railway=yard, 55.3050, -123.1498), via de haalbaarheidstoets van deze keten (2026-10-31)
[3] Pembina, Vancouver Wharves (125 acre, 4 kaaien, 3 klasse-I-spoorwegen, koperconcentraat-export BC), https://www.pembina.com/operations/facilities/vancouver-wharves/
[4] Wikipedia, "British Columbia Highway 39" (spur, 29 km, naar Mackenzie), https://en.wikipedia.org/wiki/British_Columbia_Highway_39
[5] Wikipedia, "BC Rail" (Squamish – Quesnel-lijn); 462,5 mijl North Vancouver – Prince George uit een 1950s-dienstregeling gevonden via websearch (bron-url niet geopend), https://en.wikipedia.org/wiki/BC_Rail
[6] Mineralsed/BC mine-profielpagina "Mt. Milligan Mine" (40 km WSW van Mackenzie, trucks naar Mackenzie, rail naar Vancouver Wharves; Japan, Korea, Filipijnen; 62.500 t/dag), https://mineralsed.ca/learning-resources/bc-mineral-resources-map/bc-operating-mine-profiles/highland-valley-copper-mine/ ; privé-weg naar Mackenzie: Mining Weekly, "Mt Milligan copper/gold project, Canada", 2013, https://www.miningweekly.com/article/mt-milligan-coppergold-project-canada-2013-09-27 (alleen uit websearch-uittreksel)
[7] Wikipedia, "Mackenzie, British Columbia" (Hwy 39, 28 km van Hwy 97); Prince George – Mackenzie 184 km weg uit een websearch-uittreksel, https://en.wikipedia.org/wiki/Mackenzie,_British_Columbia
[8] Satellietblik `v2/tools/sat_check.py`, Esri World Imagery z15, 2026-10-31: `sat-koper-mountmilligan-vancouver-cu-mountmilligan-laad.png`, `sat-koper-mountmilligan-vancouver-cu-mackenzie-laad.png` in `v2/build-cache/satcheck/`
[9] Spoorrun `toets_spoorroute.mjs` (BAKE_SUFFIX=-raw), Mackenzie Yard → Wharves: 942,2 km, 616 edges, 0 keerpunten, snaps 0,03 en 0,01 km (`spoorroute-koper-mountmilligan-vancouver-mackenzie-wharves.geojson`)
[10] Haalbaarheidstoets `koper-mountmilligan-vancouver` (2026-10-31): bindend aanpassing, via-punten, OSRM 97,9 km

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
`v2/data/stroomroute-koper-mountmilligan-vancouver.json` (84,5 KB, versie 2, lonlat): **2 benen · 1.042,1 km · 4.261 punten · 3 markers**, geen stippel. Recept: `bak_koper_mountmilligan_vancouver()` in `v2/tools/bak_stromen.sh`; profiel `koper-mountmilligan-vancouver-mountmilligan-mackenzie` in `maak_stroombeen_weg.py`.

| # | modaliteit | km gebakken | km brief | afwijking | naad |
|---|---|---|---|---|---|
| b1 | truck (Mount Milligan → Mackenzie Yard) | 96,1 | OSRM-indicatie 97,9 (hemelsbreed 59, geen wegkm) | −1,8% t.o.v. de indicatie (geen norm) | start op anker |
| b2 | spoor (Mackenzie Yard → Vancouver Wharves) | 946,0 (router 942,2) | indicatie 928 (eigen optelling) | +1,9% (router +1,5%) | 0,03 km |

- **b1 weg:** wegscan_puur op de canada-extract (441 s); 5 via-punten snappen op 0,01–0,07 km; plant → weg 0,07 km, weg → yard 0,28 km. First mile over kleine klassen 84,05 km (tertiary/unclassified/service), dus de FSR's zijn in OSM als bevaarbare klasse getagd en het was geen stippel nodig. Omwegcheck: segmenten 5,2 / 24,1 / 35,9 / 24,2 / 6,4 km, geen via-omweg. Geen gepubliceerde wegkm, dus de ±15%-toets is indicatie.
- **b2 spoor:** `toets_spoorroute.mjs` met BAKE_SUFFIX=-raw (1-op-1-net), een run Mackenzie Yard → Wharves, 616 edges, 0 keerpunten; hergebruikt uit de tussenuitvoer van de haalbaarheidstoets (`spoorroute-koper-mountmilligan-vancouver-mackenzie-wharves.geojson`), niet opnieuw gedraaid.
- **Markers:** Mount Milligan 0,0 km, Mackenzie Yard 0,0 km, Vancouver Wharves 0,003 km van de lijn (alle ≤ 0,5 km).
- **Toetsen:** `toets_knikken.py`: spoor 0 knikken, 0 omkeringen; truck 6 spikes (R 14–135 m, o.a. bij de ankers en op 55,237/−123,08), 0 omkeringen, 0 terugloop; `toets_rechte_benen.py`: geen rechte doorgetrokken benen. Naad b1→b2 0,03 km.
- **Geen** zeebeen, haven-aanloop, leiding, lucht, kopie of last-mile-stippel: b1 eindigt op het yard-anker, b2 op de kade, stoppunt op de kade.
- **Lessen/bevindingen:** (1) de FSR-corridor loopt in OSM als doorgaande tertiary/unclassified, dus een wegbeen van 96 km zonder stippel; (2) het Centerra-verlaadpunt blijft ongelokaliseerd (yard-anker aannemelijk); (3) de canada-scan kost 441 s en een reus-slot; (4) sitelaag mist Mount Milligan en Vancouver Wharves (centraal).
