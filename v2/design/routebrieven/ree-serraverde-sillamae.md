# Routebrief (licht) · Zeldzame aardmetalen · Serra Verde (Minaçu) → Santos → Muuga → Silmet Sillamäe (Estland)

**stroom-id:** `ree-serraverde-sillamae` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Titel (bol):** Zeldzame aardmetalen · Serra Verde (Goiás) → Santos → Muuga → Silmet Sillamäe (Estland; Santos-haven bevestigd, Silmet als consignee afgeleid)
**Keten in één zin:** REE-carbonaat (mixed rare earth carbonate, ionklei) van de Serra Verde-plant bij Minaçu gaat per **truck** (GO-132, BR-010, BR-050, SP-330, SP-348, SP-055; ca. 1.520 km) naar de containerterminal Tecon Santos, per **zeeschip** (MARNET: Atlantische Oceaan, Kanaal, Noordzee, Oostzee) naar zeeknoop 1970 in de Finse Golf, over een stippel-haven-aanloop naar Muuga en per **truck** over weg 1/E20 naar NPM Silmet in Sillamäe. Stoppunt aan de Silmet-poort.
**Welke as van het verhaal:** Braziliaanse ionklei-REE, in 2026 omgebogen van China naar het Westen (Chinese contracten ingekort tot eind 2026, 15-jaars US-SPV-offtake) en in Europa gescheiden door de enige Estse scheider. Zending jan 2026: **19,9 t REE-carbonaat** (product, geen REO; US$ 674.533) [1][2]; Serra Verde 4-5 kt REO per jaar, nameplate 6,4 kt TREO eind 2027 [3][4].
**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** wegprofiel met 11 via-punten (toets: 1.480 km tot Cubatão, ontwerp 1.459 OSRM); wegbeen eindigt op Av. Santos Dumont (geen wegpad in het terminalanker) + stippel last mile 0,98 km; Santos-aanloop is een rechte stippel (6,0 km, `maak_havenaanloop` gaf niets binnen 300 s); zee gemeten 12.170,7 km (ontwerp 12.500); Muuga-stippel is dezelfde richting als `ree-kuantan-narva` b3; alleen het wegbeen Muuga → Silmet is een omgekeerde kopie.

## 1 · Ketenkaart
```
Serra Verde-plant `ree-serraverde-plant` (Pela Ema, Minaçu)
  ──(b1 truck · GO-132/GO-118/BR-010/BR-050/SP-330/SP-348/SP-055 · OSRM 1.478 km, hemelsbreed 1.187 km)──► Av. Santos Dumont (wegeinde)
  ╌╌(b2 stippel · last mile · 0,98 km)╌╌► Tecon Santos `ree-santos-tecon`
  ╌╌(b3 zee-stippel · haven-aanloop Santos · 6,0 km)╌╌► zeeknoop 5100 (-23.9815, -46.3479)
  ──(b4 zee · Atlantische Oceaan–Kanaal–Noordzee–Oostzee · 12.170,7 km, MARNET, aannemelijk)──► zeeknoop 1970 (59.8, 24.7)
  ╌╌(b5 zee-stippel · haven-aanloop Muuga · 37,5 km, KOPIE ree-kuantan-narva b3)╌╌► Muuga-CT `ree-muuga-ct`
  ──(b6 truck · weg 1/E20 · 176,3 km, KOPIE omgekeerd ree-sillamae-newark b1)──► NPM Silmet `ree-silmet-scheiding` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-serraverde-plant` → Av. Santos Dumont (-23.9645, -46.2834) | GO-132 → GO-118/BR-010 → GO-436 → BR-050 → SP-330 → SP-348 → SP-055 (Santos) | hemelsbreed 1.187 km, geen wegkm; OSRM 1.478 km, wegscan 1.520 km (+2,8%) [5][9] | maak_stroombeen_weg (extract brazilie) | nee |
| b2 | A | truck | Av. Santos Dumont → `ree-santos-tecon` | last mile (geen net op deze korrel, terminalpoort) | 0,98 (eigen meting) | rechte stippel | **ja** |
| b3 | B | zee | `ree-santos-tecon` → zeeknoop 5100 | haven-aanloop Santos (kade 6,0 km van de knoop, verplicht) | 6,0 (eigen meting [11]) | rechte stippel | **ja — hier reikt het net niet** |
| b4 | B | zee | zeeknoop 5100 → zeeknoop 1970 | Zuid-Atlantische Oceaan, Kanaal, Noordzee, Oostzee, Finse Golf (aannemelijk: haven en routering niet gebronnen) | 12.170,7 (eigen MARNET-dry-run [11]) | MARNET | nee |
| b5 | B | zee | zeeknoop 1970 → `ree-muuga-ct` | haven-aanloop Muuga | 37,5 | KOPIE stippel `bak_ree_kuantan_narva` b3 (zelfde richting) | **ja** (kade 37,5 km van de knoop) |
| b6 | C | truck | `ree-muuga-ct` → `ree-silmet-scheiding` | weg 94 → Peterburi tee → weg 1/E20 Tallinn-Narva mnt | 176,3 (OSRM 178,4; hemelsbreed 157, geen wegkm) | KOPIE omgekeerd `ree-sillamae-newark-weg-silmet-muuga.geojson` | nee |

*Aannemelijk: één bron* (consignee Silmet afgeleid; Santos is bevestigd door Comex Stat, de terminal en Muuga niet) staat in de beennamen b4-b6 en de titel, niet in de lijnstijl.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-serraverde-plant` | mijn/plant (laadplek) | Mineração Serra Verde, Pela Ema, Minaçu (OSM way 1178009380) | -13.4920, -48.5135 | [6][7] | bron-gelegd (z15 gezien: verwerkingsplant met witte hallen en bezinkvijvers, dagbouwputten N en ZW, haul roads) |
| `ree-santos-tecon` | overslag truck → zee | Tecon Santos (Santos Brasil), Port of Santos | -23.9620, -46.2926 | [8][10] | aannemelijk (z15 gezien: containeryard met portaalkranen aan de oostoever van het kanaal; Comex noemt alleen Porto de Santos, de terminal is een aanname) |
| `ree-muuga-ct` | overslag zee → truck | Muuga-containerterminal (HHLA TK Estonia) | 59.4915, 24.9675 | hergebruik `ree-sillamae-newark.md` §3 | bron-gelegd daar (z16: kranen en containerstapels); haven voor deze lading = aanname |
| `ree-silmet-scheiding` | scheidingsfabriek (losplek, stoppunt) | NPM Silmet OÜ, Sillamäe | 59.4031, 27.7421 | hergebruik `ree-sillamae-narva.md` §3 | bron-gelegd daar (z15: industrieterrein met tankenpark en spoor); consignee afgeleid |

Zeeknoop 5100 (-23.9815, -46.3479) en 1970 (59.8000, 24.7000) zijn MARNET-knopen, geen ankers. Geen last-mile-been aan de Silmet-kant: het wegbeen eindigt op het anker. BTP (-23.9231, -46.3528, 6,5 km van knoop 5100) is het niet-gekozen alternatief.

## 4 · Via-punten (b1; corridor uit de haalbaarheidstoets: via Niquelândia en de BR-010 oost van Brasília, BR-050 naar Uberlândia, SP-330/SP-348 naar de Baixada Santista; het alternatief via BR-153 is niet gemeten)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | GO-132 bij Niquelândia | -14.0319, -48.0818 | op de GO-132, pint de zuidwaartse uitgang uit het plantgebied (OSRM nearest 3 m) |
| b1 | 2 | begin GO-118/BR-010 | -14.1425, -47.5218 | pint de aansluiting op GO-118/BR-010 (OSRM 1 m) |
| b1 | 3 | BR-010 bij Planaltina de Goiás | -15.5006, -47.5245 | houdt de route op de BR-010 ten oosten van Brasília (OSRM 2 m) |
| b1 | 4 | GO-436 bij Cristalina | -16.0507, -47.6174 | pint de GO-436-verbinding naar de BR-050 (OSRM 1 m) |
| b1 | 5 | BR-050 (zuid van Cristalina) | -16.7552, -47.6057 | pint de BR-050 in plaats van de GO-nevenwegen (OSRM 0 m) |
| b1 | 6 | BR-050 bij Araguari | -18.1867, -47.9479 | doorgaande weg, niet door het centrum (OSRM 4 m) |
| b1 | 7 | BR-050 zuid van Uberlândia | -18.8846, -48.2661 | pint de omleiding om Uberlândia (OSRM 6 m) |
| b1 | 8 | SP-330 (Anhanguera) bij Araras/Leme | -22.3595, -47.3949 | pint de Rodovia Anhanguera (SP-330) in São Paulo-staat (OSRM 2 m) |
| b1 | 9 | Campinas-west | -22.9249, -47.1310 | pint de doorgang rond Campinas, geen stadscentrum (OSRM 4 m) |
| b1 | 10 | SP-348 (Bandeirantes) | -23.2543, -46.8711 | pint de Rodovia dos Bandeirantes (OSRM 5 m) |
| b1 | 11 | SP-055 (Rodovia Cônego Domênico Rangoni) bij Cubatão | -23.9005, -46.4539 | pint SP-055 naar Guarujá/Tecon; een via midden in de Imigrantes (SP-160) en in São Paulo-stad gaf geen wegpad |
Het ontwerp zei 3-8 via-punten; de toets heeft er 11 vastgelegd (1.500 km, alle snaps ≤ 0,02 km), die staan hier. Refs voor het profiel: `BR-050, SP-330, BR-010, GO-118`; (lon, lat) in het profiel. `vensterKm` 40, `corridorKlassen [tertiary, unclassified]`, `eindToegangPrivaat` true. Eerste scan ca. 6 min, max 2 tegelijk (extract brazilie).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Serra Verde-plant, Pela Ema | Serra Verde Group (USA Rare Earth neemt over) | ionklei-erts → mixed rare earth carbonate | 4-5 kt REO/j (dec 2025); nameplate fase 1 6,4 kt TREO eind 2027 | [3][4][5] |
| Tecon Santos | Santos Brasil | truck → containerschip | 596.000 m², 2 mln TEU/j | [10] |
| Muuga-CT | HHLA TK Estonia | feeder → truck | 267.752 TEU in 2022 | `ree-sillamae-newark.md` [3] |
| NPM Silmet, Sillamäe | Neo Performance Materials | REE-carbonaat/-concentraat → REE-oxiden | 2 kt/j licht REE | `ree-sillamae-newark.md` [5] |

## 6 · Stoppunt
De brief stopt aan de poort van Silmet: de zending is door Eurostat/Comex als Brazilië → Estland vastgelegd, Silmet is de enige Estse REE-scheider (afgeleide consignee) en geen bron noemt wat er daarna gebeurt of naar welke Europese magneetfabriek de oxiden gaan. Fase D/E vervalt.

## 7 · Open punten
- **Silmet als consignee niet gebronnen.** Eurostat/Comex noemen alleen "Estland"; een Serra Verde-Neo-contract is niet gevonden. De US-SPV-offtake (15 jaar, 100% van de eerste fase) is het hoofdverhaal en Silmet is maar één van de Westerse klanten (jan-feb 2026 ook Canada 9,9 t en VS 2,0 t) [1][2][3]. Vandaar "aannemelijk".
- **Terminal Santos en Muuga zijn aannames.** Comex noemt alleen Porto de Santos (URF 0817800); BTP is het alternatief. Muuga/Sillamäe als Estse haven en een transshipment via Rotterdam zijn niet gebronnen.
- **Een tweede, kleine zending** jan 2026 (948 kg, US$ 32.742) ging via het vliegveld Guarulhos [2]: geen luchtbeen, te klein en zonder bron voor de verdere route.
- **Wegkm niet gepubliceerd:** hemelsbreed 1.187 km, OSRM 1.478 km (voorspelling), wegscan 1.520 km tot Av. Santos Dumont; de ±15%-toets is een indicatie.
- **De Santos-aanloop (b3) is een rechte stippel**; hij kan de landpunt bij de Ponta da Praia raken (1:10M-kust). Idem Muuga-stippel (kopie).
- **Plant is niet de put:** het OSM-polygoon (0,4 km) ligt op de plant; de dagbouwputten liggen 1-2 km N en ZW.
- **Volume is één zending:** geen jaarvolume Brazilië → Estland; 19,9 t is product-carbonaat, REO-gehalte onbekend. Het ontwerp noemt 678 t Serra Verde naar China (2025) en USGS 2,0 kt REO Brazilië; beide niet zelf gecontroleerd.
- **Overlap met `ree-whitemesa-sillamae`** (golf 20) in b5-b6, bewust: dezelfde letterlijke kopieën.

## 8 · Bronnen
[1] Eurostat Comext DS-045409, EE import uit BR, CN 2846: mrt 2026 198,84 x100 kg = 19,88 t, EUR 265.374; jan 2026 0,95 t, EUR 30.378 (eigen query 2026-11-01). https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/ds-045409?freq=M&reporter=EE&partner=BR&product=2846&flow=1
[2] Comex Stat (MDIC), POST api-comexstat.mdic.gov.br/general, heading 2846 export 2026-01..03: Goiás → Estonia via 0817800 Porto de Santos jan 19.884 kg US$ 674.533; via Guarulhos 948 kg; Goiás → Canada via Santos feb 9.936 kg (eigen query 2026-11-01). https://api-comexstat.mdic.gov.br/general
[3] USA Rare Earth, 8-K ex-99.1 (20-04-2026): Serra Verde/Pela Ema, 15-jaars offtake naar een US-gesteunde SPV, nameplate ca. 6.400 t TREO/j eind 2027. https://www.sec.gov/Archives/edgar/data/0001970622/000121390026045339/ea028691001ex99-1.htm
[4] SMM, Serra Verde Cuts Rare Earth Supply Deal Term with China, Eyes West Shift (08-12-2025): 4-5 kt REO/j, 6,5 kt in 2027, China-contract eindigt eind 2026, DFC-lening US$ 465 mln. https://news.metal.com/newscontent/103660406
[5] Reporte Minero (31-08-2026): Pela Ema produceert gemengd REE-carbonaat, 6.400 t/j eind 2027, China-contracten ingekort, 100% eerste productie naar US-entiteit. https://www.reporteminero.cl/noticia/noticias/2026/08/brasil-tierras-raras-pela-ema-desafios-dependencia-china
[6] OpenStreetMap (ODbL) via Nominatim: way 1178009380 Mineração Serra Verde, Minaçu, -13.4920284, -48.5134592 (landuse industrial, bbox ca. 0,4 km). https://nominatim.openstreetmap.org
[7] Wikipedia, Minaçu: Serra Verde Group, Pela Ema ca. 30 km WNW van Minaçu, commerciële productie. https://en.wikipedia.org/wiki/Mina%C3%A7u
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-ree-serraverde-sillamae-{plant,tecon}.png`.
[9] OSRM (router.project-osrm.org, 2026-11-01): Serra Verde → Av. Santos Dumont 1.475,6 km direct; met de 11 via-punten 1.502,4 km; alle via-snaps ≤ 6 m; hemelsbreed 1.187 km (haversine).
[10] Wikipedia, Ports of Brazil en Santos Brasil: Tecon Santos op de linker oever, 596.000 m², 2 mln TEU/j. https://en.wikipedia.org/wiki/Ports_of_Brazil
[11] Eigen MARNET-dry-run (`hecht_marnet.py route`, scratch, 2026-11-01): zeeknoop 5100 → 1970 12.170,7 km (108 edges, 1.274 punten); Tecon-anker op 6,02 km van knoop 5100 (BTP 6,51 km); Muuga-kade op 37,45 km van knoop 1970.
[12] Briefs `ree-kuantan-narva` (b3 Muuga-stippel), `ree-sillamae-newark` (b1 weg, Muuga-anker) en `ree-sillamae-narva` (Silmet-anker): ankers en kopie-benen.

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
`v2/data/stroomroute-ree-serraverde-sillamae.json` (298,2 kB, versie 2, punt_formaat lonlat, 6 benen, 14.258 punten, 4 markers, 13.902,5 km). Functie `bak_ree_serraverde_sillamae` in `v2/tools/bak_stromen.sh`, profiel `ree-serraverde-sillamae-serraverde-santos` in `maak_stroombeen_weg.py`. Naden alle 0,00 km; markers op 0,0 km van hun lijn.

| # | modaliteit | km gemeten | brief | afwijking | stippel |
|---|---|---|---|---|---|
| b1 | truck | 1.511,0 | OSRM 1.478 / wegscan 1.520 (geen wegkm) | +2,2% t.o.v. OSRM, indicatie | nee |
| b2 | truck | 1,0 | 0,98 | - | ja, last mile |
| b3 | zee | 6,0 | 6,0 | - | ja, haven-aanloop Santos |
| b4 | zee | 12.170,7 | 12.170,7 | 0% | nee (aannemelijk) |
| b5 | zee | 37,5 | 37,5 | - | ja, haven-aanloop Muuga |
| b6 | truck | 176,3 | 176,3 (OSRM 178,4) | 0% | nee |

**Recept.** b1: `python v2/tools/wegscan_puur.py --profiel ree-serraverde-sillamae-serraverde-santos` (extract brazilie, venster 40 km, 13 punten = anker + 11 via-punten + wegeinde, corridorKlassen tertiary/unclassified, eindToegangPrivaat; scan 546 s, 1.342.142 way-delen; plant 0,13 km naar de weg, wegeinde 0,02 km). Alle via-snaps ≤ 0,02 km, geen via-punt verplaatst. b2, b3, b5: rechte `--stippel`. b4: `--been zee` MARNET zeeknoop 5100 naar 1970 (snaps 0,000 km, 108 edges). b6: `ree-serraverde-sillamae-weg-muuga-silmet.geojson` = letterlijk omgekeerde coordinatenlijst van `ree-sillamae-newark-weg-silmet-muuga.geojson` (1.581 punten, properties van/naar gewisseld).

**Stippels.** b2: last mile 0,98 km, geen net op deze korrel (het anker ligt op terminalterrein, geen wegpad). b3: Tecon-kade 6,0 km van zeeknoop 5100 (> 5 km), rechte lijn, `maak_havenaanloop` niet opnieuw geprobeerd (brief: niets binnen 300 s); kan de Ponta da Praia raken (1:10M-kust). b5: Muuga-kade 37,5 km van knoop 1970, letterlijke kopie van de stippel-regel in `bak_ree_kuantan_narva` (zelfde richting).

**Toets.** Geen naad > 5 km. `toets_knikken`: b1 44 knikken, 1 omkering van 167,8 graden bij -23,5128 / -46,7270 (scherpe bocht, echt, v=1,9; in de metropool Sao Paulo, 0 terugloop), enkele spikes van 88-90 graden bij -14,1505 / -48,077 (13-50 m, bij via 1 Niquelandia); b6 11 knikken (spikes in de terminalzones Muuga en Silmet, gedeeld met de bron). `toets_rechte_benen`: alleen de stippels b3 en b5 (omwegfactor ~1,0), bedoeld. Lengtetoets b1 is een indicatie (geen gepubliceerde wegkm).

**Lessen.** (1) Het in de brief voorgelegde wegprofiel met 11 via-punten werkte in een keer (1.511 km tegen OSRM 1.478): via-punten uit een OSRM-snap van <= 6 m op de doorgaande weg zijn betrouwbaar. (2) Omgekeerde kopie van een wegbeen: coordinaten omdraaien en van/naar in `benen` wisselen; de bake accepteert dat als vooraf gebakken lijn. (3) Open punten uit §7 blijven staan: Silmet als consignee, Tecon en Muuga zijn aannames, 19,9 t zending zonder jaarvolume, kleine zending via Guarulhos niet getekend.
