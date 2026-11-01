# Routebrief (licht) · Goud — San Albino → Managua → Salt Lake City (Nicaragua → VS)

**stroom-id:** `goud-sanalbino-saltlakecity` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** doré-baren (goud + zilver) van de San Albino-mijn en -plant (Mako Mining, Nueva Segovia, Nicaragua) per beveiligd
wegtransport naar Managua (b1, stippel: geen Nicaragua-extract), per vrachtvlucht (grootcirkel, aannemelijk) naar de vrachtterminal van
Salt Lake City International (SLC), per truck naar Asahi Refining USA, 4601 West 2100 South, Salt Lake City.
**Welke as van het verhaal:** Midden-Amerika → Noord-Amerika — de eerste Nicaraguaanse doré-as op de bol. Volume **ca 1,1 t Au/j**
(35.897 oz herwonnen Au in 2025, ÷ 32,15 = 1,12 t; plant 500 tpd, ~36.000 oz/j in de TR) [1][2]. Klein, maar het enige
gedocumenteerde Midden-Amerikaanse doré-pad naar een raffinaderij.

## 1 · Ketenkaart
```
San Albino-mijn/plant `au-sanalbino-mijn` (TR-positie, onzeker)
  ──(b1 truck, STIPPEL · beveiligingsbedrijf via El Jicaro–NIC-55–NN-16–NIC-29–CA-6–CA-1 · TR 266 km wegopgave; hemelsbreed 172 km)──►
Managua-vrachtterminal (MGA) `au-mga-vrachtterminal` (aannemelijk)
  ──(b2 lucht · vlucht MGA → SLC, grootcirkel, aannemelijk: één bron · 4.058 km)──►
Salt Lake City vrachtterminal (SLC) `au-slc-vrachtterminal` (aannemelijk)
  ──(b3 truck · openbare weg naar South Frontage Road · hemelsbreed 6,5 km, eigen OSM-meting 8,2 km)──►
  ──(b4 truck, stippel · last mile 102 m, letterlijke kopie goud-nevada-saltlakecity)──►
Asahi Refining USA `au-saltlakecity-asahi` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | San Albino → Managua MGA-vrachtterminal | onverharde weg → El Jicaro → NIC-55 → NN-16 → NIC-29 → Ocotal → CA-6 → CA-1 (Pan-American) | 266 TR-wegopgave (193+20+33+13+7, plus onverhard) [1]; hemelsbreed 172 [berekend] | stippel | **ja** — geen Nicaragua/Midden-Amerika-extract op schijf |
| b2 | B | lucht | MGA → SLC | vrachtvlucht MGA → SLC (aannemelijk: één bron, de TR noemt alleen "shipment" vanuit Managua) | 4.058 grootcirkel [berekend] | maak_luchtbeen | nee |
| b3 | C | truck | SLC-vrachtterminal → South Frontage Road (Asahi) | SLC-servicewegen → openbare weg → 2100 South-frontage | **hemelsbreed 6,5 km, geen wegkm**; eigen OSM-meting 8,2 km (indicatie) | maak_stroombeen_weg (us-utah) | nee |
| b4 | C | truck | South Frontage Road → laaddock Asahi | last mile, geen net op deze korrel | 0,102 (kopie) | stippel (kopie) | **ja** — OSM-service-ways van het terrein hangen niet aan het net |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-sanalbino-mijn` | mijn / plant | San Albino-mijn en -plant (Mako Mining), TR-positie 13°41'23"N 86°06'04"W | 13.6897, -86.1011 | [1][2] | **onzeker** (z15 en z13 gezien: alleen heuvels, weiland en bos, geen pit of plant — oud beeld of punt naast de plant; niet verschoven) |
| `au-mga-vrachtterminal` | overslag truck → lucht | Managua Augusto C. Sandino Intl (MGA), vrachtzone aan de Carretera Norte | 12.1452, -86.1764 | [osm][sat] | aannemelijk (z15/z17 gezien: rood-dak magazijn tegen de Carretera Norte, direct erachter het noordelijke platform en de terminal; welk pand de vracht afhandelt is niet bronnen-bevestigd) |
| `au-slc-vrachtterminal` | overslag lucht → truck | Salt Lake City Intl (SLC), vracht-/servicezone ten oosten van de terminal | 40.7812, -111.9778 | [3][4][sat] | aannemelijk (z17 gezien: cluster platte-dak-loodsen met laaddocks en parkeerterrein aan de oostelijke servicestraat naast het platform; Delta heeft hier zijn hub en een vrachtfaciliteit, exact pand niet gebronnd) |
| `au-saltlakecity-asahi` | raffinaderij (stoppunt) | Asahi Refining USA, Inc., 4601 West 2100 South, Salt Lake City UT 84120 | 40.72471, -112.00077 | [6][TR] | bron-gelegd (hergebruikt letterlijk uit `goud-nevada-saltlakecity.md`: laaddock op het OSM-terreincomponent, adres = OSM-huisnummer) |

## 4 · Via-punten
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | — | geen | — | stippel: geen net, dus geen routering; de TR-wegnamen staan in de beennaam |
| b3 | — | geen | — | korte stadsrit; de router (venster 15 km) kiest het kortste pad en snapt op 0,07 km van het SLC-anker en 0,00 km op het routeerpunt South Frontage Road (40.725566, -112.000339); geen corridorkeuze die een via-punt rechtvaardigt |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| San Albino-plant (CIL + gravity/ICU, dry-stack) | Mako Mining | erts → doré-baren | 500 tpd (vergund 1.000 tpd), ~36.000 oz Au/j [1] | [1] |
| Asahi Refining USA, Salt Lake City | Asahi Holdings | doré (Au + Ag) → good-delivery baren | t/j onbekend | [1][6] |

## 6 · Stoppunt
De brief stopt aan de poort van Asahi Refining USA: de TR noemt alleen de raffinage ("ships doré bars … for final refinement"); geen bron
noemt een volgende locatie voor dit goud, dus fase D/E vervalt.

## 7 · Open punten
- **Mijnkop onzeker:** de TR-positie (pit, 15 km van Honduras) is op Esri z13–z15 niet te zien als pit of plant; het punt is niet verschoven.
- **Nicaragua-extract ontbreekt** (Geofabrik Midden-Amerika niet op schijf): b1 is stippel, ca 6% van de lijn. Centraal downloaden zou b1 een
  wegbeen maken (Nicaragua-OSM bevat CA-1/CA-6/NIC-55); de 266 km komt uit de TR, de dirt road El Jicaro → plant (15–20 min rijden) staat niet in OSM-wegklassen.
- **Vlucht MGA → SLC niet gebronnd:** de TR zegt alleen dat de beveiligingsaannemer de baren naar Managua brengt "for shipment to the Asahi
  refinery"; geen lijndienst MGA-SLC bekend, tussenlanding (bijv. Miami of Houston) niet gebronnd — één directe grootcirkel getekend.
- **Asahi-bewijs alleen de TR** (amendement 2024, effective okt 2023); de AIF van 28-04-2026 noemt Asahi niet [2]. Mako verkoopt het goud op
  de dag van verzending tegen spot [1]; een andere raffinaderij vanaf 2024/25 is niet uit te sluiten.
- **SLC-vrachtpand:** Delta vervangt zijn SLC-vrachtfaciliteit in 2027 door een gerenoveerd ex-USPS-pand [3][4]; de huidige locatie is niet gepubliceerd.
- **Volume** = herwonnen oz Au (2025: 35.897; 2024: 39.275) [2]; de baren bevatten ook zilver (~37.614 oz Ag in 2025), niet in t Au.

## 8 · Bronnen
[1] Mako Mining Corp., NI 43-101 TR San Albino (RSI, amendement 2024): 1.1 positie en 227 km ten noorden van Managua, 5.1 toegang (193+20+33+13+7 km), 17.1 "security contractor transports [bars] to Managua for shipment to the Asahi refinery in Salt Lake City", 19.1/19.2 markt en contracten (Refining agreement: Asahi Refining USA, Inc.). https://www.sec.gov/Archives/edgar/data/1784930/000106299326001525/exhibit99-54.htm
[2] Mako Mining, AIF 2025 (6-K, 28-04-2026): recovered Au 39.275 oz (2024), 35.897 oz (2025); noemt Asahi niet. https://www.sec.gov/Archives/edgar/data/1784930/000106299326002209/exhibit99-1.htm
[3] Delta News/Utah Inland Port Authority, 03-11-2025 — Delta Cargo SLC, 48.000 sq ft, ex-USPS-pand, opening 2027. https://news.delta.com/delta-expands-salt-lake-city-presence-state-art-cargo-facility
[4] KSL, "Delta to open new 48,000-square-foot cargo facility in Utah". https://www.ksl.com/article/news/business/a-game-changer-delta-to-open-new-48000-square-foot-cargo-facility-in-utah/51399651
[5] Esri World Imagery via `v2/tools/sat_check.py` (z13–z17, live, 2026-11-01): `v2/build-cache/satcheck/sat-goud-sanalbino-saltlakecity-mijn.png`, `-plant13.png`, `-mga.png`, `-mga17.png`, `-slc.png`, `-slc17.png`.
[6] `v2/design/routebrieven/goud-nevada-saltlakecity.md` — anker Asahi, last-mile-stippel (Utah DAQ-vergunning DAQE-IN103670032-26; Panjiva).
[osm] OpenStreetMap (ODbL) — Carretera Norte/MGA-platform, us-utah-extract voor de eigen 8,2 km-meting (`maak_stroombeen_weg.py`, profiel niet bewaard).
[v1] `data/goud.js`, `design/goud.md` — geen Nicaragua-site; dit is een nieuwe as.

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
Recept: `bash v2/tools/bak_stromen.sh goud-sanalbino-saltlakecity` (functie `bak_goud_sanalbino_saltlakecity`; profiel `goud-sanalbino-saltlakecity-slc-asahi` in `maak_stroombeen_weg.py`) -> `v2/data/stroomroute-goud-sanalbino-saltlakecity.json`, 10,4 KB, versie 2, lonlat, 4 benen, 407 punten, 4 markers, totaal 4.238,6 km.

| # | modaliteit | been | km | punten | stijl |
|---|---|---|---|---|---|
| b1 | truck | San Albino-plant -> Managua MGA-vrachtzone | 171,9 (hemelsbreed; TR 266 wegkm) | 2 | stippel |
| b2 | lucht | vlucht MGA -> SLC (grootcirkel) | 4.058,3 | 164 | doorgetrokken |
| b3 | truck | SLC-vrachtterminal -> South Frontage Road | 8,3 (brief: 6,5 hemelsbreed / 8,2 eigen OSM) | 239 | doorgetrokken |
| b4 | truck | last mile Asahi -> laaddock (kopie goud-nevada-saltlakecity) | 0,1 | 2 | stippel |

Markers (4): au-sanalbino-mijn (onzeker), au-mga-vrachtterminal, au-slc-vrachtterminal (aannemelijk), au-saltlakecity-asahi (bron-gelegd). Alle markers liggen op de eindpunten van hun lijn (0 km); alle naden 0,0 km.

- **b1 stippel**: geen Nicaragua/Midden-Amerika-extract op schijf; rechte lijn tussen de TR-positie en MGA. De TR-wegopgave van 266 km staat in de beennaam; de bol toont 172 km hemelsbreed. Centraal downloaden maakt hier een wegbeen van.
- **b2 vlucht**: `maak_luchtbeen.py`, grootcirkel, doorgetrokken; aannemelijk (een bron, geen lijndienst of tussenlanding gebronnd). Beide eindpunten zijn de aannemelijke vrachtterminals.
- **b3**: us-utah, geen vias, snap 0,07 en 0,00 km; 8,3 km tegen de 7 km indicatie (+17,5%) valt buiten de indicatieve 15%, maar de brief geeft hier geen wegkm: de bake-lengte is leidend. Eind op het gedeelde routeerpunt South Frontage Road.
- **b4**: letterlijke kopie van de last-mile-stippel van goud-nevada-saltlakecity (102 m).
- **Geen zee, geen haven-aanloop, geen via-punten.**
- **Toets knikken**: 0 omkeringen, 4 scherpe hoeken (R 6-15 m, 88-95 graden) op de servicewegen van het SLC-platform in b3; geen terugloop. Bevinding, niet gerepareerd. Rechte-benen-toets markeert alleen b1 (de bedoelde stippel).
- **Lessen**: (1) een bestaande tussenuitvoer (lucht en weg) uit het briefwerk was bruikbaar; het verloren profiel is opnieuw toegevoegd en gaf identiek resultaat (8,2 km, 239 punten). (2) Een stroom met een stippel als eerste been past in dezelfde ketenvolgorde in hecht_marnet (stippel, geojson, geojson, stippel).
