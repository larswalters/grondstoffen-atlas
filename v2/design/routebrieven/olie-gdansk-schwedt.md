# Routebrief (licht) · olie — Naftoport Gdańsk (Polen) → Rurociąg Pomorski en Przyjaźń via Płock → PCK-raffinaderij Schwedt (Duitsland)

**stroom-id:** `olie-gdansk-schwedt` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) · **status:** gebakken
**Keten in één zin:** Niet-Russische ruwe olie (volgens Unimot uit Zuid-Amerika) die per tanker bij het Naftoport-terminal in Gdańsk wordt gelost, gaat per **leiding** — korte aanvoer naar de PERN-basis Gdańsk, dan de Rurociąg Pomorski (800 mm) naar het PERN-knooppunt Płock en de noordtak van Przyjaźń (Druzhba) naar het PCK-tankenpark in Schwedt (Brandenburg): 679,7 km OSM-som in drie benen, zonder zee en zonder weg.
**Welke as van het verhaal:** *Oostzee-import als vervanging van de Druzhba* — na het Russische Kazachstan-transitverbod van 1-5-2026 vult Gdańsk Schwedt aan. **~40 kb/d (2025)**: ca. 20% van de >10 Mt ruwe olie van PCK in 2025 (≈ 2 Mt/j × 7,33 vat/t ÷ 365) [3]; PERN noemt 2026 +2 Mt/j extra mogelijk (≈ +40 kb/d) [3]. Rostock levert ca. 60% (niet deze keten), Kazachstan ca. 20% (sinds mei 2026 weg). Peiljaar 2025.

## 1 · Ketenkaart
```
Naftoport-tankenpark `ol-naftoport` ──(a1 leiding · aanvoer Naftoport → PERN-basis · 6,6 km hemelsbreed, STIPPEL)──► PERN-basis Gdańsk `ol-pern-gdansk`
  ──(a2 leiding · Rurociąg Pomorski, Gdańsk → Płock · 238,6 km OSM-som, 3 ways)──► PERN-knooppunt Płock `ol-plock-pern`
  ──(a3 leiding · Przyjaźń noordtak, Płock → Konin-regio → Poznań-noord → Schwedt · 441,0 km OSM-som, 12 ways)──►
  PCK-tankenpark Schwedt `ol-pck-schwedt` ── stoppunt
```
Geen zeebeen: geen bron noemt een laadhaven of schip. Geen via-punten: de benen zijn OSM-leidingways (`man_made=pipeline substance=oil`) die op gedeelde nodes aan elkaar gestikt worden.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| a1 | A | leiding | Naftoport-tankenpark → PERN-basis Gdańsk | aanvoerleiding Port Północny → Gdańsk-Rafineryjna (niet in OSM) | 6,6 hemelsbreed, geen bronlengte [2] | rechte stippel, reden in de naam | **ja — geen OSM-way** |
| a2 | B | leiding | PERN-basis Gdańsk → Płock-knooppunt | Rurociąg Pomorski (PERN, 800 mm, 1975, tweerichtings) [10] | **238,6 OSM-som, geen bronlengte** [9][10] | OSM-ways 1122681226 (omgekeerd, 110,8), 1123298008 (omgekeerd, 0,3), 1378110022 (127,5) | nee |
| a3 | B | leiding | Płock-knooppunt → PCK-tankenpark Schwedt | Przyjaźń/Druzhba noordtak (PERN → PCK) [1][11] | **441,0 OSM-som, geen bronlengte** [9] | OSM-ways 578626377, 1122655730 (omg.), 1122655732 (omg.), 1122655733, 1433874907, 1433874903, 1433874905, 1433874904, 578626376, 279727288, 273290090, 1050745426 | nee — 4 naden (0,18 · 0,36 · 0,009 · 0,046 km = 0,6 km) recht gestikt |

Weggelaten: de oostspur way 1122657839 (13 km) uit het ontwerp — hoort niet bij de route. Fase C/D/E vervallen: de pijp eindigt in het PCK-tankenpark; geen bron koppelt deze lading aan een vervolg.
Normen: a2/a3 hebben geen gepubliceerde leidinglengte; de ±15%-toets is een indicatie (hemelsbreed Gdańsk–Schwedt 326,7 km; OSM-som 679,7 km = 2,1 × hemelsbreed, de leiding loopt via Płock).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-naftoport` | losterminal (tankenpark + oliepieren) | Naftoport-terminal, Port Północny Gdańsk — tankenpark ~12 tanks | 54.3925, 18.6995 | [2][6][12] | aannemelijk (z15 gezien: tankenpark van ~12 witte tanks op het terrein tussen kolenterminal en containerterminal, drie oliepieren in zee 0,3–0,9 km oostwaarts; geen bron-coördinaat, dus aannemelijk) |
| `ol-pern-gdansk` | begin Pomorski (basis Gdańsk) | PERN-basis Gdańsk — OSM-beginknoop van way 1122681226 (via einde 10267848909) | 54.3401, 18.7464 | [9][12] | aannemelijk (z15 gezien: pijpeinde met twee kleine tanks aan de zuidrand van het groot raffinaderij-/tankenpark ten zuiden van de Martwa Wisła; of dit de PERN-basis of het raffinaderijterrein is, is niet bevestigd) |
| `ol-plock-pern` | knooppunt Pomorski/Przyjaźń | PERN-knooppunt Płock — OSM-eindknoop way 1378110022 (naad 0,18 km naar 5543614674) | 52.5333, 19.8322 | [9][12] | bron-gelegd (z15 gezien: tankenpark met ~35 tanks in twee groepen in akkerland, het punt ligt aan de westrand van het noordelijke deel, ~0,2 km van de tanks) |
| `ol-pck-schwedt` | eindpunt / losplek raffinaderij | PCK Schwedt — OSM-eindknoop van way 1050745426 | 53.0875, 14.2544 | [3][9][12] | bron-gelegd (z15 gezien: pijpeinde op de zuidoosthoek van een tankenpark met ~60 tanks, rangeerterrein en procesinstallaties westelijk; bos en waterzuivering oostelijk) |

Sitelaag `olie-sitelaag.json` heeft geen Gdańsk-, Płock- of Schwedt-site; geen hergebruik mogelijk. `ankers_hergebruik`: geen.

## 4 · Via-punten (leiding: geen corridorkeuze; alleen de kartering-naden)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| a3 | 1 | naad Płock 12760155262 → 5543614674 (0,18 km) | 52.5333, 19.8322 → 52.5318, 19.8333 | Pomorski eindigt, Przyjaźń begint aan de andere kant van het tankenpark; recht gestikt |
| a3 | 2 | naad 1433874905 → 1433874904 (0,36 km) | 52.3970, 18.4915 → 52.3958, 18.4865 | Konin-regio, OSM-hiaat; recht gestikt |
| a3 | 3 | naad 279727288 → 273290090 (9 m) | 52.9418, 14.1476 | grens Polen/Duitsland; PERN-way wordt Drushba1-way |
| a3 | 4 | naad 273290090 → 1050745426 (46 m) | 53.0580, 14.2271 → 53.0583, 14.2276 | Schwedt, ingang; de Drushba1-way loopt nog 3,9 km door tot het PCK-tankenpark |
Way 1123298008 (0,3 km) is een korte verbindingsway tussen 1122681226 en 1378110022 (gedeelde nodes, geen naad). Parallelle Przyjaźń-lijnen zijn niet uitgesloten behalve de genoemde ways (§7).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Naftoport Gdańsk | PERN Przyjaźń SA 68% (+Orlen e.a.) | tankers → opslag → PERN | doorzet >39 Mt in 2025, steady 2026; 34 Mt/j (Wikipedia); 49 Mt/j na de nieuwe pier (H2 2028) | [2][6] |
| PERN-pijpleiding Gdańsk → Płock | PERN | Pomorski, tweerichting | ~30 Mt/j, voedt ook Płock en Leuna; PERN: +30% nominaal door weerstandsverlager | [4][7] |
| PCK-raffinaderij Schwedt | Rosneft Deutschland (54,2%, Treuhand), Shell 37,5%, Enilive | ruwe olie → benzine, diesel, kerosine (BER per spoor) | 10,33 Mt/j destillatie (≈ 207 kb/d), 11,5 Mt/j nominaal; 2025 >10 Mt | [3][4] |

## 6 · Stoppunt
De brief stopt in het PCK-tankenpark Schwedt: de pijp eindigt daar, PCK is lohnfabrikant voor de aandeelhouders (Berlin/Brandenburg, BER) en geen bron koppelt deze lading aan een specifieke afnemer; vóór Naftoport geen zeebeen omdat geen bron een laadhaven noemt.

## 7 · Open punten
- **Volume niet gemeten voor dit traject**: ~20% van PCK-instroom 2025 (ACE/Bukold) is een afgeleide; geen PERN-jaarverslag of Reuters-cijfer voor Gdańsk-Schwedt gevonden; de Bundesregierung geeft de flows niet vrij [4]. 2026-niveau (na de Kazach-stop, PCK ~80% belading [8]) niet gebronnen.
- **Aanvoer Naftoport → PERN-basis** (6,6 km hemelsbreed, ontwerp zei ~8 km) staat niet in OSM; stippel zonder bronlengte. De werkelijke leidingroute door Port Północny is onbekend.
- **PERN-basis anker** is aannemelijk, niet bevestigd (§3); Naftoport-pieren zijn niet apart als anker gelegd.
- **Flowrichting Pomorski** (omgekeerd Gdańsk → Płock) is niet in een bron bevestigd; wel Unimot en PERN: Gdańsk → PERN → Schwedt [5][7]; Wikipedia noemt de pijp tweerichtings [10].
- **Parallelle Przyjaźń-lijnen** (twee strengen Płock–Schwedt mogelijk) zijn niet uitgesloten behalve de oostspur 1122657839; de gestikte keten is de streng van het ontwerp.
- **Rostock (ca. 60% van de PCK-instroom, MVL-pijp 6,8–7 Mt/j)** en de Kazach-route (ca. 20%) zijn niet deze keten; OSM heeft Rostock-Schwedt niet.
- **Naden** 0,6 km totaal zijn aangenomen kartering-hiaten (ondergronds), niet onafhankelijk bevestigd. Geen bronlengte, dus geen echte ±15%-toets.

## 8 · Bronnen
[1] Wikipedia, "Druzhba pipeline" — noordtak Mozyr → Polen → Schwedt, Płock–Gdańsk-link, Kazach-stop 1-5-2026, Schwedt-MVL-link. https://en.wikipedia.org/wiki/Druzhba_pipeline
[2] Wikipedia, "Naftoport" — Port Gdańsk, 34 Mt/j, PERN 68%, nieuwe terminal tot 49 Mt/j. https://en.wikipedia.org/wiki/Naftoport
[3] S. Bukold / ACE, "Factsheet Die Raffinerie PCK Schwedt", mei 2026 — 2025 >10 Mt, ca. 60% Rostock / 20% Danzig / 20% Kazachstan, 10,33 Mt/j, eigenaren, PERN +2 Mt/j. https://verkehrspolitik.ace.de/content/dam/ace/dokumente/verkehrspolitik/pck-raffinerie-factsheet.pdf
[4] Deutscher Bundestag, hib 638/2026 (13-8-2026) — MVL-pijp tot 7 Mt/j, pijp Danzig ~30 Mt/j (voedt Płock/Leuna), PCK 11,5 Mt/j nominaal, flows geheim. https://www.bundestag.de/1204982
[5] Unimot, 13-7-2026 — Zuid-Amerikaanse ruwe olie via Naftoport Gdańsk en PERN naar PCK Schwedt. https://www.unimot.pl/en/news/polish-unimot-strengthens-diversification-of-crude-oil-and-fuel-supplies-for-the-region-south-american-crude-shipped-via-gdansk-to-schwedt
[6] Baird Maritime, 28-10-2025 — Naftoport >39 Mt 2025, nieuwe pier H2 2028, dekt Schwedt-vraag. https://www.bairdmaritime.com/shipping/ports/polish-oil-terminal-expansion-may-boost-germanys-seaborne-intake
[7] Hydrocarbon Processing, juli 2026 — PERN +30% nominale capaciteit. https://hydrocarbonprocessing.com/news/2026/07/polands-unimot-says-it-will-supply-crude-to-germanys-schwedt-refinery/
[8] Interfax Kazakhstan, 27-8-2026 — Schwedt ~80% belading. https://ns.interfax.kz/en/news/82099
[9] OpenStreetMap (ODbL) — way-geometrie via api.openstreetmap.org/api/0.6/ways.json en nodes.json (15 ways, gemeten 2026-10-28, cache `v2/build-cache/olie-gdansk-schwedt-osmapi-cache.json`). https://api.openstreetmap.org/api/0.6/way/1122681226
[10] Wikipedia, "PERN Przyjaźń SA" — Pomorski 1975, tweerichtings, Płock–Schwedt 1973. https://en.wikipedia.org/wiki/PERN_Przyja%C5%BA%C5%84_SA
[11] Wikipedia (pl), "Rurociąg Przyjaźń" — noordtak Polen, >2 Mt/j naar Schwedt, Gdańsk–Pomorski-gesprekken. https://pl.wikipedia.org/wiki/Rurociąg_„Przyjaźń”
[12] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-olie-gdansk-schwedt-{naftoport-park,pern-baza,plock,pck}.png`.

## 9 · Bak-noot (door de bak-agent)

**Gebakken (2026-10-28, lichte werkwijze, M31 golf 10)** · `v2/data/stroomroute-olie-gdansk-schwedt.json` (20,4 KB, versie 2, lonlat) · totaal **686,9 km**, 985 punten, 4 markers.

| # | modaliteit | km | punten | naad naar vorig been | opmerking |
|---|---|---|---|---|---|
| a1 | leiding (stippel) | 6,6 | 2 | - | rechte lijn Naftoport -> PERN-basis, geen OSM-way |
| a2 | leiding | 238,6 | 353 | 1 m | Rurociag Pomorski, 3 ways gestikt op gedeelde nodes (brief 238,6: 0,0%) |
| a3 | leiding | 441,7 | 630 | 0 m | Przyjazn-noordtak, 12 ways; brief 441,0 (+0,2%, indicatie: geen bronlengte) |

**Recept:** `bash v2/tools/bak_stromen.sh olie-gdansk-schwedt` (functie `bak_olie_gdansk_schwedt`). Benen a2 en a3 komen uit `v2/tools/maak_leidingbeen_olie_gdansk_schwedt.py` (OSM-API per way-id, cache `v2/build-cache/olie-gdansk-schwedt-osmapi-cache.json`; uitvoer `v2/build-cache/ais/graaf/olie-gdansk-schwedt-leiding-a2.geojson` en `-a3.geojson`, FeatureCollection). Geen zee, weg, haven-aanloop of vlucht. Eigen profielen in `maak_stroombeen_weg.py`: geen.

**Stippel:** alleen a1 (6,6 km, hemelsbreed; de aanvoerleiding door Port Polnocny staat niet in OSM, werkelijke route onbekend). a2 en a3 zijn doorgetrokken.

**Leiding-naden (a3):** drie kartering-naden recht gestikt - 364 m (Konin-regio, voor way 1433874904), 9 m (grens PL/DE, way 273290090) en 46 m (Schwedt-ingang, way 1050745426) - plus 176 m kopstuk: a3 begint op het a2-eindpunt (Plock-knoop 12760155262) zodat de overgang tussen de benen 0 m is. Samen 0,6 km, geen stippel (ondergrondse leiding, geen net-gat). Dit is afgerond op de brief (0,18 · 0,36 · 0,009 · 0,046 km).

**Toets:** geen naad > 5 km (max 1 m tussen benen); markers 0,0 / 0,0 / 3 / 3 m van de lijn; `toets_knikken.py`: 8 knikken >= 60 graden (spikes bij 52.94177,14.14756 en 52.39542,18.48544 = de OSM-naden en kartering-kinken), 0 omkeringen, 0 terugloop; `toets_rechte_benen.py`: alleen a1 (stippel, factor 1,004 - bedoeld). Km-toets a2/a3 is een indicatie (geen bronlengte).

**Lessen:** (1) een kale way-lijst met nearest-endpoint-oriëntatie vindt de omgekeerde ways (1122681226, 1123298008, 1122655730, 1122655732) vanzelf; alle aansluitingen delen een node behalve de drie genoemde naden. (2) Open punten uit §7 blijven staan (volume niet gemeten, anker PERN-basis aannemelijk, parallelle Przyjazn-strengen).
