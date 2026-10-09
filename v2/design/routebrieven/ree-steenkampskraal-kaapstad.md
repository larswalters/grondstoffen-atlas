# Routebrief (licht) · Zeldzame aardmetalen · Steenkampskraal → Kaapstad (Zuid-Afrika)

**stroom-id:** `ree-steenkampskraal-kaapstad` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken (2026-10-09, golf 7c; zie §9)
**Keten in één zin:** monazietconcentraat (>50% TREO, thoriumhoudend) van de Steenkampskraal Monazite Mine (Knersvlakte,
Western Cape) gaat per **truck** ~380 km via de gravelweg DR2230 en de **N7** naar de containerterminal van de haven van
Kaapstad (aannemelijk: geen bron noemt de kade); de lijn stopt daar — geen gedocumenteerde afnemer of bestemmingshaven.
**Welke as van het verhaal:** het ontbrekende Zuid-Afrikaanse REE-draadje — "mijn naar wereldmarkt" zonder bekende koper.
Fase 1 opende 2026-10-07 (min. 5 kt concentraat/j; ontwerp 13,4 kt/j ≈ ≥6,7 kt REO/j bij >50% TREO, eigen omrekening);
peiljaar 2026, nog geen gerealiseerd exportcijfer, eerste export gepland vóór eind 2026 [1][3][5][6].

## 1 · Ketenkaart
```
Steenkampskraal-mijn `ree-steenkampskraal-mijn` (concentratieplant, Ptn 1 Steenkamps Kraal 70)
   ──(b1 truck · DR2230 (gravel) → N7 → N1 → Marine Dr/Duncan Rd · ~380 km, aannemelijk: één bron)──►
Kaapstad containerterminal `ree-kaapstad-kade` (Ben Schoeman Dock) ⏹ stoppunt
   ╌╌ niet getekend: zee naar een niet-gedocumenteerde bestemming; "offtakes" in FR/NO/CA zijn alleen landen, geen adres [7]
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-steenkampskraal-mijn` → `ree-kaapstad-kade` | DR2230 → N7 (Vanrhynsdorp–Klawer–Citrusdal–Piketberg) → N1/R27 → Duncan Rd; **aannemelijk: één bron** (geen publicatie voor déze zending) | ~380 (OSRM 380,6; N7 Kaapstad–Vanrhynsdorp 289 km gepubliceerd [4]; hemelsbreed 326,6 km — de 280–300 uit het ontwerp is te laag) | maak_stroombeen_weg (extract zuid-afrika, pure-Python PBF-lezer) | ja, alleen de eerste 2,4 km: mijn → DR2230 (last mile, geen net op deze korrel); de rest doorgetrokken |

Geen zeebeen: er is geen bestemmingshaven, dus geen MARNET-route en geen haven-aanloop. Voor later: de dichtstbijzijnde
MARNET-zeeknoop (5205, -33.8624, 18.4282) ligt 6,1 km van de kade, dus bij een vervolg is een haven-aanloop nodig (>5 km).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-steenkampskraal-mijn` | mijn / concentratieplant (laadplek) | Steenkampskraal Monazite Mine | -30.9795, 18.6295 | [2][8][13] | bron-gelegd (hergebruikt letterlijk uit `ree-sitelaag.json` `w-steenkampskraal`; opnieuw z15 gezien: kaal ontgonnen mijnterrein met gebouwen en hopen, toegangsweg gaat naar het oosten; Wikipedia -30.9861, 18.6291 ligt 0,8 km ZZW) |
| `ree-kaapstad-kade` | overslag truck→(zee), exportkade | Cape Town Container Terminal (CTCT), Ben Schoeman Dock, kadefront oostpunt | -33.9132, 18.4534 | [10][11] | aannemelijk (z15 gezien: containerterminal met kranen en containerstacks, schip langszij aan de kade bij het punt; waar de monazietcontainers feitelijk laden is niet gepubliceerd — multi-purpose terminal in Duncan Dock is het alternatief) |

## 4 · Via-punten (b1; N7 is trunk over het hele tracé — keuze alleen bij de afslag en de stadsrand)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | DR2230/N7-aansluiting | -31.2302, 18.5295 | pint de gravelroute (tertiary, unpaved) naar de N7 i.p.v. een omweg via Bitterfontein/R27-kust (OSRM: afslag na 31,8 km) |
| b1 | 2 | Klawer, N7 (buitenom) | -31.7931, 18.6289 | N7 blijft de doorgaande weg i.p.v. de R27-kustroute via Vredendal/Lambertsbaai |
| b1 | 3 | Citrusdal, N7 | -32.5939, 18.9896 | pint de Cederberg/Piekenierskloof-corridor van de N7 (grootste uitbuiging oostwaarts, ~44 km van de rechte lijn) |
| b1 | 4 | Piketberg, N7/R44-rotonde | -32.9088, 18.7641 | N7 vs R44 via Porterville/Wellington; de N7 blijft de westelijke doorgaande weg |
| b1 | 5 | N7/N1-aansluiting Kaapstad (afrit) | -33.8860, 18.5315 | pint N7→N1 naar de havenstreek i.p.v. de R27 West Coast Road; geen stadscentrum |
| b1 | 6 | N1 bij Paarden Eiland (merge) | -33.8866, 18.5260 | laatste doorgaande weg vóór Marine Drive/Duncan Road naar de terminal |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Steenkampskraal-plant | Steenkampskraal Monazite Mine (SMM) | erts → monazietconcentraat (zwaartekracht + flotatie); later carbonaat | fase 1 min. 5 kt concentraat/j; ontwerp 13,4 kt/j; processingpagina "~10.800 t/j basecase fase 1" | [1][3][5] |

## 6 · Stoppunt
De lijn eindigt bij de containerkade van Kaapstad: geen bron noemt een koper, scheidingsfabriek of bestemmingshaven (alleen
"offtake agreements", landen FR/NO/CA/VS-consortium zonder naam of adres [7]); fase D en E vervallen, de lijn eindigt waar het bewijs eindigt.

## 7 · Open punten
- **Welke kade/haven**: geen bron noemt Kaapstad; de eigen site meldt alleen dat de mijn "dicht bij" Kaapstad en Saldanha ligt [3]. CTCT is een
  aanname (container); radioactief concentraat (Th) kan een andere terminal/haven (Saldanha) betekenen.
- **Afnemer/bestemming** onbekend; Mining Weekly 2025-10-24 (403) niet gelezen. De "Mkango/Rainbow"-lead uit de haalbaarheidstoets is in
  deze ronde niet bevestigd (geen treffer in de zoekresultaten) — niet gebruikt.
- **DR2230** is OSM `tertiary`, `surface=unpaved` (Nominatim) — het wegtool laat tertiary alleen toe met `corridorKlassen`; blijft een gat staan, dan wordt het een stippel "last mile (geen net)".
- **Haventerrein-toegang** (Duncan Rd/Container Rd) kan `access=private` zijn → `eindToegangPrivaat` testen; anders korte stippel naar de kade.
- **Km** komen voor 336,5 km N7 + 12 km havenaanvoer uit OSRM/Wikipedia, niet uit een bedrijfsopgave; de ±15%-toets is een indicatie.
- **Jaarvolume** fase 1 (min. 5 kt) komt uit een niet-leesbaar artikel (betaalmuur; alleen via zoeksamenvatting) — verifiëren.
- Mijnstatus: Wikipedia-coördinaat wijkt 0,8 km af van het sitelaag-anker; het sitelaag-anker is gebruikt (z15 op het terrein).

## 8 · Bronnen
[1] Steenkampskraal Monazite Mine, Processing — ~10.800 t/j concentraat fase 1, carbonaat aan scheiders verkoopbaar. https://www.steenkampskraal.com/processing/
[2] Wikipedia, Steenkampskraal mine — 71 km N van Vanrhynsdorp, -30.98614/18.62907. https://en.wikipedia.org/wiki/Steenkampskraal_mine
[3] NS Energy, Steenkampskraal REE project — toegang via N7 + gravel DR2230, ~330 km van Kaapstad, dicht bij havens Kaapstad/Saldanha. https://www.nsenergybusiness.com/projects/steenkampskraal-rare-earth-elements-mine/
[4] Wikipedia, N7 (South Africa) — 666 km; Citrusdal 161, Klawer 262, Vanrhynsdorp 289 km vanaf Kaapstad. https://en.wikipedia.org/wiki/N7_(South_Africa)
[5] Engineering News, "Steenkampskraal mine opens Phase 1 of monazite concentrate plant", 2026-10-07 — plant geopend, offtakes zonder namen, eerste export vóór eind 2026. https://www.engineeringnews.co.za/article/steenkampskraal-mine-opens-phase-1-of-monazite-concentrate-plant-2026-10-07
[6] Mining Weekly, "Steenkampskraal monazite mine, South Africa – update", 2026-06-26 (betaalmuur; min. 5.000 t/j alleen via zoeksamenvatting). https://www.miningweekly.com/article/steenkampskraal-monazite-mine-south-africa-update-2026-06-26
[7] Mining Weekly, "Steenkampskraal mine fully funded to proceed with next phase", 2025-05-08 (alleen zoeksamenvatting: kwart van het concentraat onder offtake; productafnemers FR/NO/CA). https://www.miningweekly.com/article/steenkampskraal-mine-fully-funded-to-proceed-with-next-phase-2025-05-08
[8] Steenkampskraal, Information Memorandum — Ptn 1 of Steenkamps Kraal No.70, West Coast DC. https://www.steenkampskraal.com/information-memorandum/
[9] OSRM public demo, mijn → kade — 380,6 km (OSM-gebaseerd, geen publicatie). https://router.project-osrm.org/
[10] OpenStreetMap/Nominatim — Cape Town Container Terminal -33.91319/18.45342; Ben Schoeman Dock; DR2230 = tertiary/unpaved. https://nominatim.openstreetmap.org
[11] Esri World Imagery z15 — `v2/build-cache/satcheck/sat-ree-steenkampskraal-kaapstad-{mijn,ctct}.png`. https://www.arcgis.com
[12] Northern Miner — mijn ~350 km NW van Kaapstad (hemelsbreed-orde). https://www.northernminer.com/news/great-western-minerals-looks-to-south-africa-for-rare-earths/1000089696/
[13] `v2/design/ree-sitelaag.json` — `w-steenkampskraal` (-30.9795, 18.6295, bron-gelegd).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Bestand:** `v2/data/stroomroute-ree-steenkampskraal-kaapstad.json` · 81,9 KB · versie 2 · lonlat · 4.001 punten · 2 markers · **379,5 km** totaal.

| # | modaliteit | km | naad | stippel | been |
|---|---|---|---|---|---|
| 1 | truck | 2,4 | 0,00 | ja | Steenkampskraal-mijn last mile naar DR2230 (geen net op deze korrel) |
| 2 | truck | 377,1 | 0,00 | nee | vrachtwagen Steenkampskraal → Kaapstad CTCT (DR2230 → N7 → N1, aannemelijk: één bron) |

**Markers:** Steenkampskraal-mijn (-30.9795, 18.6295) en Kaapstad CTCT-kade (-33.9132, 18.4534), beide 0,0 km van hun lijn. Ankers ongewijzigd uit §3 (mijn bron-gelegd, kade aannemelijk).
**Toets:** weggeometrie 377,1 km tegen 380 gepubliceerd = **-0,8%** (binnen ±15%, maar 380 is OSRM 380,6 + N7 Kaapstad–Vanrhynsdorp 289 km Wikipedia, geen bedrijfsopgave: indicatie, geen norm) · geen naad > 0 km · `toets_knikken`: 7 knikken ≥ 60° (alle spikes bij knooppunten/havenwegen: N7/N1-aansluiting, Paarden Eiland, Duncan Rd, DR2230-aansluiting), **0 omkeringen, 0 terugloop** · `toets_rechte_benen --min-km 5`: geen treffer van deze stroom · json.load, versie 2, lonlat, modaliteit alleen `truck`, elk been ≥ 2 punten.
**Recept:** profiel `ree-steenkampskraal-kaapstad-mijn-ctct` (acht punten, `corridorKlassen ["tertiary"]`, `eindToegangPrivaat`, `trimStaart`, vensterKm 45) via de wrapper `v2/build-cache/ais/graaf/ree-steenkampskraal-kaapstad-wegscan-wrapper.py` (gitignored): een pure-Python PBF-lezer (numpy+zlib) op `zuid-afrika-latest.osm.pbf` die `maak_stroombeen_weg.main()` aanroept met dezelfde `weg_houden`/`corridor_keten`-logica; scan 118 s (181.811 way-delen → 51.801 in het corridorvenster). Geen via-punt snapte > 0 km (alle zes 0,00); alleen het mijnanker snapt 2,39 km. Daarna `bash v2/tools/bak_stromen.sh ree-steenkampskraal-kaapstad`.
**Toelichting stippel:** de mijn ligt 2,39 km van de dichtstbijzijnde meegenomen weg (de toegangsweg naar de mijn zelf is niet als doorgaande klasse gekarteerd); het wegtool tekent die rechte anker-stub mee in het weggeojson. Omdat hij > 2 km is, is hij uit de truck-geometrie geknipt (`…-weg-mijn-ctct-net.geojson`, zelfde lijn zonder het eerste punt) en loopt als stippel "last mile (geen net op deze korrel)". DR2230 zelf (29,1 km tertiary/unpaved, doorgetrokken) is dus wél gevonden, de gravel was geen gat. Weg → kade: 0,04 km, geen stippel. De laatste 1,2 km naar de kade liep over klassen service/tertiary/unclassified en de kade snapte op 0,04 km (`eindToegangPrivaat` stond aan; of hij nodig was is niet apart getest).
**Geen** zeebeen, haven-aanloop, vlucht, leiding, spoor of kopie. Zeeknoop 5205 (-33.8624, 18.4282) ligt nog steeds 6,1 km van de kade: bij een vervolg is een haven-aanloop nodig.
**Afwijkingen van het ontwerp:** geen; het id noemt het werkelijke eindpunt (Kaapstad). Het ontwerp noemde 280–300 km; gemeten wegkm is 377 (hemelsbreed 326,6).
**Lessen:** (1) `--bron overpass` is op 2026-10-09 opnieuw geprobeerd en faalde (reset / HTTP 500); pyosmium blijft geblokkeerd — de PBF-wrapper werkte in één run en is het vaste pad op deze machine. (2) Een mijn zonder gekarteerde toegangsweg levert een rechte anker-stub van > 2 km in het weggeojson: knip hem af en maak er een stippel van, anders staat er een doorgetrokken lijn die "net" suggereert waar het net niet reikt. (3) Het slot-sjabloon met een variabel pad (`rm -rf "$d"`) wordt geweigerd; `rmdir` op een literaal slotpad werkt.
