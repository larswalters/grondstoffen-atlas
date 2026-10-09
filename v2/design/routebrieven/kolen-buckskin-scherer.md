# Routebrief (licht) · Kolen — Buckskin (Wyoming) → Orin → Alliance → Memphis → Plant Scherer (Georgia, VS)

**stroom-id:** `kolen-buckskin-scherer` (ontwerp-id was `kolen-blackthunder-scherer`; de bindende haalbaarheidstoets legt de start bij Buckskin) ·
**geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** Powder River-thermische kolen uit de Buckskin-dagbouwmijn (Kiewit, 17 km ten noorden van Gillette) per
BNSF-unit train over de Joint Line naar Orin, via Alliance (Nebraska), Lincoln, Kansas City en Springfield naar Memphis, daar
overdracht aan Norfolk Southern via Sheffield en Chattanooga naar Plant Scherer (Juliette, Georgia) — de grootste kolencentrale
van Noord-Amerika. Eén spoorketen van ca. 3.000 km, geen zee, geen weg, geen fase D/E.
**Welke as van het verhaal:** één kolenstroom dwars door de VS, ver van elke haven, naar een centrale die nog draait. Buckskin ~11 Mt/j
(GEM, 2023 [5]); Scherer-afname onbekend (in 2002 potentieel 12–14 Mt/j [3]; Scherer = ~10% van de productie van Buckskin + Caballo +
Eagle Butte samen [2]). **Eenheid: Mt kolen per jaar.** Geen bron koppelt Buckskin alléén aan Scherer: representatief, aannemelijk (§7).

## 1 · Ketenkaart
```
Buckskin-laadspoor (WY) `kolen-buckskin-laad` ─(b1a spoor · Joint Line · ~248 km)─► Orin ─(b1b · ~270 km)─► Alliance NE
─(b1c · BNSF via Lincoln, Kansas City, Springfield, Thayer · ~1.678 km)─► Memphis `kolen-memphis-overdracht`
─(b2a · NS via Corinth, Sheffield, Huntsville · ~501 km)─► Chattanooga ─(b2b · NS via Dalton, Atlanta · ~346 km)─► Plant Scherer `kolen-scherer-centrale`
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1a | A | spoor | `kolen-buckskin-laad` → Orin | Joint Line (BNSF/UP) [9] | hemelsbreed 197 km, geen gepubliceerde spoorlengte; proef 247,7 | toets_spoorroute | nee (snap 0,91 km, < 2 km) |
| b1b | A | spoor | Orin → Alliance | BNSF-lijn door de North Platte-vallei (route-uitkomst, geen bron) [8] | hemelsbreed 169 km, geen gepubliceerde lengte; proef 269,9 | toets_spoorroute | nee |
| b1c | A | spoor | Alliance → Memphis | BNSF Memphis District [1][4] | hemelsbreed 1.354 km, geen gepubliceerde lengte; proef 1.678,4 | toets_spoorroute | nee |
| b2a | B | spoor | Memphis → Chattanooga | NS Memphis–Corinth–Sheffield–Stevenson [10] | hemelsbreed 433 km, geen gepubliceerde lengte; proef 500,9 | toets_spoorroute | nee |
| b2b | B | spoor | Chattanooga → `kolen-scherer-centrale` | NS Atlanta District [1][10] | hemelsbreed 258 km, geen gepubliceerde lengte; proef 345,5 | toets_spoorroute | nee |

Totaal gemeten proef 3.042,4 km tegen hemelsbreed 2.258 km (verhouding 1,35); geen gepubliceerde spoorlengte: de ±15%-toets geldt als
indicatie, niet als norm. Alle benen heten `… (aannemelijk: één bron voor de koppeling mijn–centrale)` in de beennaam.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-buckskin-laad` | mijn / laadlus | Buckskin Mine (Kiewit), kolensilo's + treinlus | 44.4413, -105.5318 | [5][6] | bron-gelegd (z16 gezien: silo's en transportbanden met een spoorlus van ~1 km die op de oost-westlijn bij 44.437 aansluit, 17 km ten noorden van Gillette; de OSM-quarry 44.4638,-105.5358 ligt 2,5 km noordelijker midden in de pit en is geen anker) |
| `kolen-memphis-overdracht` | overdracht BNSF → NS | Memphis, BNSF/NS-overdracht (yard niet gebrond) | 35.1300, -90.0600 | [4] | aannemelijk (z14 gezien: stedelijk spoor bij de Frisco-brugaanlanding; de bron noemt alleen "Memphis", het yard is niet gelegd) |
| `kolen-scherer-centrale` | losplek / centrale | Plant Scherer (Georgia Power), kolenpark met treinlus | 33.0631, -83.8039 | [1] | bron-gelegd (z15 gezien: vier koeltorens, zwart kolenpark en een spoorlus rond het park; het net eindigt 0,11 km van het punt) |

## 4 · Via-punten (alleen spoorbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1a/b1b | 1 | Orin (Joint Line → Wyoming-lijn) | 42.7700, -104.7200 | einde Joint Line; snap 0,75 km |
| b1b/b1c | 2 | Alliance, op de doorgaande lijn | 42.0943, -102.8774 | zonder dit punt kiest de router de UP-lijn via Kearney (1.830 km Orin–Memphis, tegen 1.948 km via Alliance = BNSF). Verplaatst van de toets-waarde 42.1017, -102.8689: die snapt (0,81 km) op een yardspoor dat alleen vanuit het oosten bereikbaar is en gaf een heen-en-terug-spits van 14,8 km |
| b1c/b2a | 3 | Memphis (overdracht) | 35.1300, -90.0600 | BNSF → NS; snap 0,11 km |
| b2a/b2b | 4 | Chattanooga | 35.0299, -85.2996 | kiest de NS-lijn via Atlanta (Inman) i.p.v. Birmingham; snap 0,00 km |
Vervallen (toets): Kearney (UP), Topeka, Kansas City, Springfield, Sheffield — de route passeert Lincoln, Kansas City, Springfield, Thayer en Sheffield vanzelf.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Plant Scherer | Georgia Power (22,95%), Oglethorpe 30%, FPL 25,35%, MEAG, JEA, Dalton | PRB-kolen → elektriciteit | 4 units, 3.520–3.740 MW; unit 4 gepland uit 2022, unit 3 tot 2035–2038 | [1][2] |

## 6 · Stoppunt
De brief eindigt op het kolenpark van Scherer: de kool wordt verbrand, daarna geen goederenstroom meer (geen fase D/E).

## 7 · Open punten
- **Geen bron koppelt Buckskin aan Scherer als enige.** Casper Star-Tribune (2021): Buckskin, Caballo en Eagle Butte leveren "most" van Scherer [2]; Black Thunder leverde in 2020 >90% van Plant Daniel (Mississippi), niet van Scherer. Buckskin is representatief gekozen; geen aandeel per mijn.
- **Scherer-afname in Mt/j niet gevonden** (EIA-923 niet geraadpleegd); 12–14 Mt/j was de capaciteit in 2002 [3], met unit 4 dicht ligt de afname lager.
- **Buckskin-productie loopt uiteen:** 17,6 Mt (2019), 9,7 Mt (2020) [5], ~11,3 Mt (2023, GEM, alleen via zoeksamenvatting) en een Kiewit-claim van ">27 Mt/j" [6].
- **Memphis-overdracht:** bron noemt alleen de stad [4]; het yard (BNSF Tennessee Yard of NS) is niet gelegd, het anker is een punt op de doorgaande lijn.
- **Corridors Orin–Alliance en Alliance–Memphis zijn route-uitkomsten** van het 1-op-1-net; alleen Memphis, Sheffield, Chattanooga en Atlanta staan in bronnen (railfan [10]). FL PSC-dossier [4] en Power Engineering [3] waren niet te openen en zijn via zoeksamenvattingen gelezen.
- **Terugweg lege treinen** soms via Birmingham [10]; niet getekend. Een route Memphis–Scherer via Birmingham (786 km) zou korter zijn; de router kiest Chattanooga door het via-punt.
- **Sitelaag:** Buckskin ontbreekt in `kolen-sitelaag.json` (w-blackthunder staat als centroïde 43,66/-105,30, aannemelijk); centrale beslissing.
- **Scherer-toekomst:** een omschakeling naar gas of sluiting van unit 3 maakt de stroom tijdelijk (§5).

## 8 · Bronnen
[1] Wikipedia, "Plant Scherer" — 33.063,-83.804; 4 units, eigenaren, PRB via BNSF Memphis District en NS Atlanta District, 2–5 treinen/dag. https://en.wikipedia.org/wiki/Plant_Scherer
[2] Casper Star-Tribune via Wyoming News Exchange, "Biggest U.S. coal plant will halve production" (2021-11) — Buckskin, Caballo, Eagle Butte leveren het merendeel; ~10% van hun productie naar Scherer; Black Thunder >90% van Plant Daniel. https://newslj.com/biggest-us-coal-plant-will-halve-production
[3] Power Engineering / Progressive Railroading, BNSF–Georgia Power-contract (2002-05-21) — BNSF PRB-kolen naar Memphis vanaf 2004, Scherer potentieel 12–14 Mt/j (via zoeksamenvatting, pagina 403). https://www.progressiverailroading.com/RailPrime/Details/BNSF-lands-long-term-coal-contract-with-Georgia-Power-5212002--66620
[4] Florida PSC-dossier 01468-2010 — BNSF PRB → Memphis, interchange NS, NS Memphis → Scherer (via zoeksamenvatting, PDF niet bereikbaar). https://www.floridapsc.com/library/FILINGS/2010/01468-2010/01468-2010.pdf
[5] Mining Data Online, "Buckskin Mine" — 17 km ten noorden van Gillette; ROM-productie 2015–2020 (17,63 Mt in 2019, 9,70 Mt in 2020); GEM Global Coal Mine Tracker (13 Mt capaciteit, 11,3 Mt 2023, via zoeksamenvatting). https://miningdataonline.com/property/1228/Buckskin-Mine.aspx · https://gem.wiki/Buckskin_Mine
[6] Kiewit, Buckskin Mining Company (">27 Mt/j", 406 Mt sinds 1981; pagina 403, via zoeksamenvatting) en Esri World Imagery via `sat_check.py` (z14–z16): `v2/build-cache/satcheck/sat-kolen-buckskin-scherer-{buckskin,buckskin-zuid,buckskin-laad,scherer,memphis}.png`. https://www.kiewit.com/?p=2168
[7] Cowboy State Daily (2026-01-19), "Feds Reject Railroad Mega Merger That Threatened Wyoming Coal" — BNSF levert PRB-kolen over aan NS voor de laatste etappe naar Georgia (via zoeksamenvatting). https://cowboystatedaily.com/2026/01/19/feds-reject-railroad-mega-merger-that-threatened-wyoming-coal/
[8] Wikipedia, "Alliance, Nebraska" — BNSF-lijn uit de PRB naar Alliance en het oosten, grote treinyard in het zuiden van de stad. https://en.wikipedia.org/wiki/Alliance,_Nebraska
[9] Wikipedia, "Powder River Basin" — Joint Line BNSF/UP, 325 Mt in 2005. https://en.wikipedia.org/wiki/Powder_River_Basin
[10] RailPictures.net, bijschriften BNSF-Scherer-treinen (Memphis, Sheffield, Chattanooga, Atlanta, Dalton; lege treinen soms via Birmingham). https://web.railpictures.net/photo/562102
[11] Proefroutes: `toets_spoorroute.mjs` over het 1-op-1-net (`BAKE_SUFFIX=-raw`, 3.260.717 spoor-edges), geojson `v2/build-cache/ais/graaf/spoorroute-kolen-buckskin-scherer-{b1a-buckskin-orin,b1b-orin-alliance,b1c-alliance-memphis,b2a-memphis-chattanooga,b2b-chattanooga-scherer}.geojson`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Stroom-id van het bestand:** `kolen-blackthunder-scherer` (ontwerp-id, blijft staan; titel en beennamen noemen het echte beginpunt Buckskin). Functie `bak_kolen_blackthunder_scherer` in `v2/tools/bak_stromen.sh`, bestand `v2/data/stroomroute-kolen-blackthunder-scherer.json` (125,2 KB, 6.655 punten, 3 markers).

| # | modaliteit | been | km gebakken | brief (proef) | afw. | naad |
|---|---|---|---|---|---|---|
| 1 | spoor | Buckskin → Orin (Joint Line) | 250,1 | 247,7 | +1,0% | n.v.t. |
| 2 | spoor | Orin → Alliance (BNSF, North Platte-vallei) | 271,6 | 269,9 | +0,6% | 0,000 km |
| 3 | spoor | Alliance → Memphis (BNSF Memphis District) | 1.689,2 | 1.678,4 | +0,6% | 0,000 km |
| 4 | spoor | Memphis → Chattanooga (NS via Sheffield) | 504,2 | 500,9 | +0,7% | 0,000 km |
| 5 | spoor | Chattanooga → Plant Scherer (NS via Atlanta) | 350,7 | 345,5 | +1,5% | 0,000 km |

Totaal **3.065,8 km** (brief 3.042,4; het verschil is polylijnlengte tegen router-km), alle vijf doorgetrokken, **geen stippel, geen haven-aanloop, geen luchtbeen, geen leiding**. Markers: `kolen-buckskin-laad` (0,91 km van de lijn = de spoorsnap, geen last-mile-stippel), `kolen-memphis-overdracht` (0,11 km), `kolen-scherer-centrale` (0,11 km). Beennamen dragen "aannemelijk: één bron voor de koppeling mijn–centrale".
**Recept:** vijf `--been-geojson spoor` in reisvolgorde op de al gebakken `spoorroute-kolen-buckskin-scherer-{b1a-buckskin-orin,b1b-orin-alliance,b1c-alliance-memphis,b2a-memphis-chattanooga,b2b-chattanooga-scherer}.geojson` (`toets_spoorroute.mjs`, `BAKE_SUFFIX=-raw`, hoofd-km 1000, max-snap 60, keerstraf 25); niet opnieuw geroutet bij het bakken. De geojson dragen het id `kolen-buckskin-scherer` in de bestandsnaam.
**Toets:** km per been binnen +0,6 tot +1,5% van de proef-km (geen gepubliceerde spoorlengte, dus indicatie, geen norm) · naden 0,000 km · `toets_knikken.py`: 5 knikken >= 60 graden (spikes bij Alliance-Lincoln 41,689,-103,117, Kansas City 39,110,-94,501 en 39,111,-94,496, Memphis 35,127,-90,060; een krappe bocht bij 37,608,-94,601), 0 omkeringen, 0 terugloop · `toets_rechte_benen.py --min-km 5`: geen enkel been van deze stroom · versie 2, `punt_formaat` lonlat, uitsluitend modaliteit spoor, elk been >= 420 punten.
**Lessen:** (1) de geojson van een eerdere toets-run konden onveranderd gebakken worden, een herberekening was niet nodig; (2) de spikes bij Kansas City en Memphis zijn OSM-wissels op een emplacement (R 29 en 48 m), geen omkeringen; (3) het ontwerp-id noemt Black Thunder terwijl het beginpunt Buckskin is: het register-label moet "Buckskin" noemen.

