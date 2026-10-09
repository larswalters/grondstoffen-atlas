# Routebrief (licht) · uranium — Navoi (Oezbekistan) → Sint-Petersburg (Rusland)

**stroom-id:** `uranium-navoi-stpetersburg` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Titel:** Uranium · Navoi → Aktobe → Orenburg → Samara → Moskou → Sint-Petersburg (Oezbeeks yellowcake naar Europa, via Rusland)
**Keten in één zin:** yellowcake (U₃O₈) van Navoiyuran, geëxporteerd vanaf de hydrometallurgische fabriek nr. 1 in Navoi, per **spoor** via Kazachstan (Beyneu–Aktobe) en Rusland (Orenburg–Samara–Moskou) naar de zeehaven van Sint-Petersburg (aannemelijk: geografische afleiding); vandaar naar Europa (Orano, Malvési).
**Welke as van het verhaal:** *Oezbeeks uranium naar Frankrijk, onder Rosatom-transit.* Oezbekistan leverde 2.515 t = 20,6% van de Franse natuurlijk-uraniumimport 2022 [1]; 14–20% over 2022–sept. 2025 [2]. Een contract van Navoiyuran met een Kazachs logistiek bedrijf noemt 500 containers via de haven van Sint-Petersburg naar Malvési [5][6]. Dit is NIET de afgewezen `navoi-alashankou` (China): de bestemming is Europa. Jaarvolume Navoiyuran: ~3.500 t U/j (2015–2019, Greenpeace 2023 p.62 [1]; WNA-schatting 2022: 3.561 t U [3]); route-specifiek tonnage onbekend.

## 1 · Ketenkaart
```
Navoi hydromet-fabriek nr. 1 `u-navoi-hydromet` ──(b1 spoor · Navoi → Nukus → Kungrad → Beyneu → Makat → Kandyagash → Aktobe ·
  aannemelijk · gemeten 1.917 km)──► Aktobe ──(b2 spoor · 271 km)──► Orenburg ──(b3 spoor · 413 km)──► Samara
  ──(b4 spoor · 1.031 km)──► Moskou ──(b5 spoor · 679 km, letterlijke kopie uit uranium-inkai-stpetersburg)──►
Sint-Petersburg-kade `u-stpetersburg-kade` ── stoppunt
```
Vervolg (niet getekend): Sint-Petersburg → Frankrijk (Malvési) volgens het contract [5][6]; zie `uranium-malvesi-tricastin`.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Navoi hydromet → Aktobe | Uzbeekse lijn naar Nukus/Kungrad, Kungrad–Beyneu, Beyneu–Makat–Kandyagash–Aktobe | gemeten 1.917,0 (geen gepubliceerde spoorkm; hemelsbreed 1.298) | toets_spoorroute (BAKE_SUFFIX=-raw; extracts oezbekistan, kazachstan) | nee — *aannemelijk: één bron voor de bestemming* |
| b2 | A | spoor | Aktobe → Orenburg | Aktobe–Orenburg (grensovergang KZ–RU in deze run) | gemeten 270,6 (hemelsbreed 222) | idem (kazachstan, rusland-wolga) | nee — aannemelijk |
| b3 | A | spoor | Orenburg → Samara | Orenburg–Samara | gemeten 412,9 (hemelsbreed 374) | idem (rusland-wolga) | nee — aannemelijk |
| b4 | A | spoor | Samara → Moskou | Samara–Moskou | gemeten 1.030,6 (hemelsbreed 852) | idem (rusland-wolga, rusland-centraal) | nee — aannemelijk |
| b5 | A | spoor | Moskou → Sint-Petersburg-kade | Moskou–Sint-Petersburg | 679,2 (kopie) | **letterlijke kopie** `spoorroute-uranium-inkai-stpetersburg-moskou-stpetersburg.geojson` | nee — aannemelijk |
Totaal gemeten 4.310,3 km tegen hemelsbreed **3.271 km, geen spoorkm** (Navoi–Sint-Petersburg; spoorlengte niet gepubliceerd — de ±15%-toets is hier indicatie, geen norm).  Extracts in totaal: oezbekistan, kazachstan, rusland-wolga, rusland-centraal, rusland-noordwest.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-navoi-hydromet` | fabriek / export-yellowcake (kop b1) | Gidrometallurgiya zavodi (Navoiyuran, fabriek nr. 1), Navoiy | 40.0946, 65.3448 | [1][3][7] | aannemelijk (z16 gezien: ommuurd industrieterrein met spoorbundel direct zuid, fabrieksgebouwen; de fabriek is niet individueel herkenbaar — `sat-uranium-navoi-stpetersburg-hydromet-z16.png`, z15 op 40.0958,65.3475 `…-hydromet.png`) |
| `u-stpetersburg-kade` | overslag spoor → zee (stoppunt) | Petrolesport-containerterminal, Sint-Petersburg | 59.8909, 30.2376 | hergebruikt uit `uranium-inkai-stpetersburg` (z15: containerstapels, kranen, spoorbundel) | bron-gelegd |
Het sitelaag-punt `w-navoi-uchkuduk` (42.1667,63.5667) is een stadscentroïde van de mijn-divisie Noord en blijft ongewijzigd; alle Oezbeekse mijnen sturen yellowcake naar Navoi [1], dus Navoi is het exportpunt.

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1→b2 | 1 | Aktobe (spoorknoop) | 50.2797, 57.2072 | ontmoeting Kazachse westlijn; snap 0,46 km op het hoofdnet |
| b2→b3 | 2 | Orenburg (spoorknoop) | 51.7727, 55.0988 | Russische grens/Orenburg-knoop; snap 1,30 km |
| b3→b4 | 3 | Samara (spoorknoop) | 53.1959, 50.1008 | kruising Wolga; snap 1,43 km (eindstation-knoop, 80 m omkering) |
| b4→b5 | 4 | Moskou (spoorknoop) | 55.7761, 37.6573 | begin Moskou–Sint-Petersburg-hoofdlijn; naad met de kopie 1,5 km |
Binnen b1 geen via: de router kiest zelf (Nukus–Kungrad–Beyneu–Makat). Beyneu–Shalkar–Aktobe (854 km) is langer dan Beyneu–Makat–Aktobe (777 km); de route volgt de kortere.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Hydrometallurgische fabriek nr. 1, Navoi | Navoiyuran (staatsbedrijf sinds jan. 2022) | mijnoplossingen/concentraat per spoor → U₃O₈-export | ~3.300–3.500 t U/j totale productie (2015–2019) | [1][3] |

## 6 · Stoppunt
De brief stopt bij de kade van Sint-Petersburg: het ontwerp-eindpunt, en het laatst gedocumenteerde punt op Russisch grondgebied (Atomspetstrans doet daar het laden/lossen [1]). De vervolgreis naar Malvési [5][6] is een zeeleg met bekende afnemer en hoort in een eigen stroom.

## 7 · Open punten
- **Corridor niet gedocumenteerd**: Greenpeace zegt letterlijk dat de beschikbare informatie het Oezbeekse traject "niet met zekerheid" laat vaststellen, maar dat het "tout du moins partiellement" door Rusland loopt [1]; Atomspetstrans vervoert transit uit Oezbekistan [1]. Het contract noemt Sint-Petersburg → Malvési [5][6], niet de spoorroute ervoor.
- **Mode niet bevestigd**: geen bron noemt spoor voor het Navoi→Rusland-deel; WNA noemt rail voor mijnoplossingen naar Navoi [3]. Spoor is afleiding (spoorwijdte 1520 mm overal, geen bogiewissel).
- **Fabriek niet individueel gezien**: OSM-way 173802119 (Gidrometallurgiya zavodi) ligt op het terrein; het laadspoor is niet aangewezen. De kop snapt 0,19 km op het hoofdnet.
- **Mijnlijn niet gevolgd**: de gemeten b1 passeert Uchkuduk niet (≥150 km ernaast); Navoi→Uchkuduk→Nukus is gemeten 294+441 = 735 km tegen 643 km rechtstreeks naar Nukus. Geen mijn–fabriek-been, want yellowcake wordt in Navoi geëxporteerd, niet in Uchkuduk.
- **Router-omkeringen** (te melden aan de bak-agent, geen via-punt verschuiven): 179,6° bij Makat 47.6443,53.3487 (b1) · 155,9° bij 51.7879,55.0818 (b2) · 171,4° bij Samara 53.1848,50.1117 (b4, 80 m). `toets_knikken.py` kan terugloop melden.
- **Grensovergang KZ–RU** (Orenburg-regio) en Oezbeeks–Kazachse grens liggen in de gemeten naden/runs; geen bron noemt een overgang. Niet als anker gelegd.
- **Zwakke reserve**: het Rosatom-transit en de Franse afnemer steunen op twee Greenpeace-rapporten en één contractmelding; de Sint-Petersburg-kade is de algemene commerciële terminal, geen bevestigd nucleair punt. Volume: WNA noemt voor 2024–2025 hogere cijfers (niet gecontroleerd).

## 8 · Bronnen
[1] Greenpeace France, *La Russie, plaque tournante du commerce d'uranium*, maart 2023 — p.28–30 (Franse import uit Oezbekistan 2022: 2.515.110 kg = 20,58%; Oezbeeks traject onzeker maar deels via Rusland), p.35 (Atomspetstrans transit uit KZ en Oezbekistan; laden/lossen in Sint-Petersburg), p.62 (mijnen sturen yellowcake per spoor naar hydrometallurgische fabriek nr. 1 in Navoi; export 3.300–3.500 t/j 2015–2019). https://cdn.greenpeace.fr/site/uploads/2023/05/Greenpeace-Rapport-La-Russie-plaque-tournante-du-commerce-duranium-mars-2023-1-1.pdf
[2] Greenpeace France, *France–Russia: radioactive trafficking continues*, jan. 2026 — p.5/7: Oezbekistan 14–20% van de Franse natuurlijk-uraniumimport 2022–sept. 2025; deel transiteert Rusland onder Rosatom; Dunkirk/Rotterdam. https://cdn.greenpeace.fr/site/uploads/2026/02/Greenpeace-investigation-France-Russia-radioactive-trafficking-continues-2026-EN.pdf
[3] World Nuclear Association, "Uranium in Uzbekistan" — HMP-1 in Navoi, productie 2022 3.561 t U (schatting), mijnen per spoor met Navoi verbonden; klanten KEPCO, CGN, Itochu. https://world-nuclear.org/information-library/country-profiles/countries-t-z/uzbekistan
[4] Wikipedia, "Navoiy" (MediaWiki API, `prop=coordinates`) — 40.0844, 65.3792. https://en.wikipedia.org/wiki/Navoiy
[5] Fergana, "Kazakhstan to Transport Uzbek Uranium to France via Russia": Kazachs Logistic Centre, 500 containers via de haven van Sint-Petersburg naar Malvési, €9 mln, afronding Q2 2026; noemt geen modaliteit. https://en.fergana.news/news/137148
[6] Kun.uz, 2025-03-24, "Uzbekistan to export uranium to France via Russia under €9M deal" — alleen kop gelezen. https://kun.uz/en/news/2025/03/24/uzbekistan-to-export-uranium-to-france-via-russia-under-9m-deal
[7] OpenStreetMap (ODbL), Nominatim — "Gidrometallurgiya zavodi", Navoiy shahri, way 173802119, 40.0945847/65.3447649. https://nominatim.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-uranium-navoi-stpetersburg-hydromet(-z16).png`.
[9] `v2/design/routebrieven/uranium-inkai-stpetersburg.md` — hergebruikt anker `u-stpetersburg-kade` en been Moskou → Sint-Petersburg (b3c).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Recept:** `bash v2/tools/bak_stromen.sh uranium-navoi-stpetersburg` (functie `bak_uranium_navoi_stpetersburg`) → `v2/data/stroomroute-uranium-navoi-stpetersburg.json` (120,8 KB, versie 2, lonlat). Vier spoorruns (`BAKE_SUFFIX=-raw toets_spoorroute.mjs`, naam `uranium-navoi-stpetersburg-<van>-<naar>`) lagen al in `v2/build-cache/ais/graaf/` en zijn hergebruikt; b5 is een letterlijke kopie.

| been | modaliteit | km (bake, haversine) | km (brief) | punten | stippel |
|---|---|---|---|---|---|
| b1 Navoi hydromet → Aktobe | spoor | 1.925,2 | 1.917,0 | 1.754 | nee |
| b2 Aktobe → Orenburg | spoor | 273,0 | 270,6 | 471 | nee |
| b3 Orenburg → Samara | spoor | 416,2 | 412,9 | 802 | nee |
| b4 Samara → Moskou | spoor | 1.041,6 | 1.030,6 | 2.623 | nee |
| b5 Moskou → Sint-Petersburg-kade | spoor (kopie inkai-stpetersburg b3c) | 679,2 | 679,2 | 1.219 | nee |
| **totaal** | | **4.335,2** | 4.310,3 | 6.869 | |

Het verschil (+0,6%) is rekenmethode (router-km tegen haversine over de punten), geen andere lijn. Hemelsbreed Navoi–Sint-Petersburg 3.271 km, geen spoorkm gepubliceerd: de ±15%-toets is indicatie (4.335/3.271 = 1,33 voor een spoorroute via Aktobe/Orenburg is plausibel).

**Markers (2):** `u-navoi-hydromet` 40.0946,65.3448 (0,19 km van de lijn, aannemelijk) en `u-stpetersburg-kade` 59.8909,30.2376 (0,37 km van de lijn, bron-gelegd, hergebruikt).
**Naden:** b1/b2 0,0 · b2/b3 0,0 · b3/b4 0,0 · b4/b5 1,5 km (Moskou, router-eindpunt tegen de kopie); alle ≤ 5 km. Geen zeebeen, geen haven-aanloop, geen stippel, geen luchtbeen, geen leiding.
**Toetsen:** `toets_knikken.py`: 6 omkeringen, waarvan 5 terugloop: Makat 47.6443,53.3487 (179,6 graden, b1) en 51.7879,55.0818 (156 graden, b2) zijn de in de brief gemelde router-omkeringen; Samara 53.1851,50.1127 (171,4 graden) is een echte scherpe bocht (eindstation-knoop); de drie terugloop-knikken in b5 (Moskou 55.7926,37.6421 en 55.7739,37.5566, Sint-Petersburg 59.8728,30.1949) zitten in de LETTERLIJKE kopie en horen bij uranium-inkai-stpetersburg (daar te herstellen, niet hier). `toets_rechte_benen.py --min-km 5`: geen treffer voor deze stroom. JSON: versie 2, punt_formaat lonlat, 5 benen allemaal spoor met ≥ 2 punten.

**Lessen:** (1) de vier gemeten spoorbenen hadden geen herberekening nodig: de router-uitvoer van de briefschrijver was direct bruikbaar via `--been-geojson`. (2) De Makat-omkering (179,6 graden, straal 0 m) is een echte spoor-spoor-keer (kopspoor/keerdriehoek in het 1-op-1-net), geen via-fout; niet verschoven. (3) Fabriek niet individueel herkenbaar: anker blijft aannemelijk.
**Open (ongewijzigd, zie §7):** corridor/modaliteit niet in een bron; grensovergangen niet gelegd; vervolg Sint-Petersburg → Malvési niet getekend; sitelaag `w-navoi-uchkuduk` blijft stadscentroïde (melden aan orkestrator).
