# Routebrief (licht) · nikkel — Weda Bay-mijn → IWIP (Indonesië)

**stroom-id:** `nikkel-wedabay-iwip` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** lateriet-erts gaat per **eigen mijnweg** (~3,6 km hemelsbreed, deels OSM-`unclassified`,
deels stippel) van een actieve dagbouw-put van PT Weda Bay Nickel (Tsingshan 57 % / Eramet 43 %, Halmahera
Tengah) naar het ore-yard van het aangrenzende Indonesia Weda Bay Industrial Park (IWIP) — daar RKEF (NPI/
ferronikkel, Tsingshan) en de Huafei-HPAL (Huayou, MHP) op hetzelfde kustterrein; export naar Chinese
roestvrijstaal-mills bestaat aantoonbaar maar is nergens op fabrieksniveau gebrond, dus de brief stopt hier.
**Welke as van het verhaal:** Indonesische onshoring — het erts verlaat het eiland niet meer, mijn en smelter
liggen op elkaars terrein. **32 Mwmt** extern verkocht 2024 (RKAB), **42 Mwmt** 2025 (na verhoging), **12 Mwmt**
initieel 2026 (−70 %, incl. 3 Mwmt intern) — de mijn stond van mei t/m 09-09-2026 op *care & maintenance* en
herstart sindsdien gefaseerd, zonder betrouwbare 2026-jaarraming [1][2][3].

## 1 · Ketenkaart
```
Weda Bay-put `ni-wedabay-pit` ──(b1 truck · eigen mijnweg, deels stippel · ~3,6 km hemelsbreed)──►
   IWIP-ore-yard `ni-iwip-rkef` (RKEF Tsingshan + Huafei-HPAL Huayou, één kustterrein)
   ├── jetty `ni-iwip-jetty` (marker, ~5 km verderop op hetzelfde terrein — geen been)
   └── vertakking (NIET getekend): NPI/ferronikkel per zeeschip naar Chinese roestvrijstaal-mills
        (Tsingshan Fuqing/Guangqing) — grootste handelscategorie NPI Indonesië→China, geen mill gebrond
   ⏹ stoppunt op ni-iwip-rkef
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-wedabay-pit` → `ni-iwip-rkef` | eigen mijnweg WBN-contractgebied → IWIP-ore-yard; OSM-scan bbox toont 138 `unclassified` / 88 `trunk` / 55 `track` / 29 `tertiary` [7]; benoemde mijnwegen ("Jalan Tambang", "Nickel/Chrome/Furnace Road") staan als `unclassified`/`service` | niet gepubliceerd; **3,6 km hemelsbreed** (satellietmeting, dit document) | maak_stroombeen_weg (`corridorKlassen`: unclassified, tertiary · `eindToegangPrivaat`: true, extract `indonesie`) | deels — kop bij de put is vermoedelijk `track`/`service` (niet gekarteerd als doorgaande weg); daar knipt de bake en wordt het stuk gestippeld "eigen mijnweg (geen net op deze korrel)" |

Geen zeebeen: de NPI-vertakking naar Chinese mills heeft geen gebronde bestemming (ladder 3 in de ontwerptoets)
en wordt niet getekend. Fase C (put → RKEF-smelter binnen het terrein) krijgt geen eigen been — één anker per
site (werkwijze §1).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-wedabay-pit` | mijn / laadfront | actieve dagbouw-put, WBN-contractgebied, Halmahera Tengah | 0.4930, 127.9350 | [4][7][8] | bron-gelegd (z16 gezien: getrapte mijnbanken, spiraalvormige ontsluitingsweg ~600 m ZO, ertshopen en een klein bijgebouw op het aangegeven punt; niet de enige put — WBN werkt acht putten, "Bukit Limber Barat/Timur" groot + zes kleinere [5] — dit is de dichtstbijzijnde bij IWIP die op satelliet actief oogt) |
| `ni-iwip-rkef` | mijn/smelter-ore-yard (fase C/D, één anker) | IWIP-terrein Lelilef — ore-yard/eerste industriecluster van het RKEF- + Huafei-HPAL-complex | 0.4970, 127.9670 | [6][7][8] | bron-gelegd (z15/z16 gezien: industriehallen, ertsopslag en verharde wegen waar de mijnweg de vlakte bereikt; de eigenlijke RKEF-smeltrijen met actieve rookpluimen en de haven liggen 3–5 km oostelijker op hetzelfde aaneengesloten kustterrein — één anker per site, werkwijze §1) |
| `ni-iwip-jetty` | jetty (marker, geen been) | IWIP-havenbekken binnen de golfbreker | 0.4745, 128.0055 | [7][8] | bron-gelegd (z16 gezien: golfbreker met meerdere afgemeerde zeeschepen en een kolenopslag ernaast — de eigen kolencentrales van IWIP) |

## 4 · Via-punten (alleen b1 — korte corridor, beperkte keuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|
| b1 | 1 | knik mijnweg bij het erts-schermstation | 0.4880, 127.9430 | hier gaat de private mijnweg over in het bredere, verharde IWIP-wegennet (z16 gezien: gebouwen/tanks van een erts-voorbewerking) — pint "via het schermstation", niet een kortere sluiproute door bos |
| b1 | 2 | eerste kruising IWIP-industrieweg | 0.4940, 127.9560 | corridor buigt hier oostwaarts het terrein op i.p.v. rechtdoor naar een andere ertsput noordelijker in het contractgebied |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| IWIP RKEF-lijnen | Tsingshan-groep (incl. Eramet/Tsingshan-JV) | lateriet-erts → NPI/ferronikkel | per lijn niet gepubliceerd; parkbrede smeltvraag "> 100 Mwmt erts" | [1][6] |
| Huafei-HPAL | Huayou | lateriet-erts (limoniet) → MHP | nameplate 120 kt Ni + 15 kt Co/j (2023); **sinds april 2026 ~50 % op *care & maintenance*** door hoge zwavelkosten | [9][10] |

## 6 · Stoppunt
De brief stopt op `ni-iwip-rkef`: NPI/ferronikkel is de grootste handelscategorie Indonesië→China (USGS/NBR-
niveau), maar geen bron noemt een specifieke afnemende mill — de vertakking naar Chinese roestvrijstaal-mills
(Tsingshan Fuqing/Guangqing, genoemd in het ontwerp) blijft daarom ongetekend, exact zoals de ontwerptoets
voorschrijft.

## 7 · Open punten
- **Welke put dit exact is:** WBN werkt acht putten (twee grote — Bukit Limber Barat/Timur — en zes kleinere)
  [5]; het satellietanker ligt in een van de kleinere, dichtstbijzijnde putten. Naam van déze put niet gebrond.
- **Gepubliceerde km ontbreekt:** geen bron geeft een lengte voor de mijnweg zelf; 3,6 km is een hemelsbreed-
  satellietmeting, geen gepubliceerd cijfer — de bake-uitvoer (werkelijke padlengte) is de eerste echte meting.
- **Mongabay "~80 km ten zuiden" (12-2024) slaat NIET op deze keten** — nagetrokken: dat artikel gaat over erts
  uit het woud bij **Dodaga, Oost-Halmahera** (O'Hongana Manyawa-gebied), een ander wingebied/bedrijf dan PT
  Weda Bay Nickel, dat rechtstreeks aan IWIP grenst. Correctie op het ontwerpprobleem "Mongabay tegenstrijdig
  met v1-centroïdes" — beide gingen over verschillende erts-toeleveranciers naar IWIP.
- **Ni-inhoud 32/42/12 Mwmt niet gepubliceerd**: bij ~1,5–1,8 % Ni en ~35 % vocht orde 300–400 kt Ni op de
  2024/2025-volumes — expliciet een afleiding, geen bron.
- **Mijnstatus vloeibaar:** stilgelegd (*care & maintenance*) vanaf medio mei 2026 (12 Mwmt-quotum uitgeput),
  herstart 10-09-2026 na goedkeuring, geen betrouwbare volumeraming voor de rest van 2026 [2][3].
- **RKEF-capaciteit per lijn** niet gepubliceerd; alleen de parkbrede vraag ("> 100 Mwmt erts") is bekend.
- **Export-vertakking per land/mill** niet gebrond op fabrieksniveau (zie §6) — niet getekend.
- **De ene pipeline-way in de bbox** (id 1007199328, 0.698/128.253, ongelabeld) is geen ertsleiding-bewijs; niet
  gebruikt (deze keten gebruikt toch geen leiding).

## 8 · Bronnen
[1] Eramet, 11-02-2026 — "reaction to the initial production and sales volumes granted... PT Weda Bay Nickel": 2025 initieel 32 Mwmt, juli 2025 verhoogd naar 42 Mwmt, 2026 initieel 12 Mwmt; parkvraag "> 100 Mwmt". https://www.eramet.com/en/news/eramet-reaction-to-the-initial-production-and-sales-volumes-granted-by-the-indonesian-authorities-to-its-joint-venture-pt-weda-bay-nickel/
[2] MINING.COM, 04-06-2026 — Weda Bay Nickel halt erts-productie na uitputting van het mijnquotum. https://www.mining.com/web/weda-bay-nickel-halts-ore-production-after-mining-quota-runs-out/
[3] Eramet/GlobeNewswire, 10-09-2026 — PT Weda Bay Nickel herstart zijn mijnbouwactiviteiten na 4 maanden care & maintenance, gefaseerd, geen betrouwbare 2026-raming. https://www.globenewswire.com/news-release/2026/09/10/3359197/0/en/pt-weda-bay-nickel-restarts-its-mining-operations.html
[4] Mindat.org, locatie "Weda Bay Mine, Halmahera Island" — 0.47158, 127.94775 (kandidaat, satelliet-gecheckt en 4,3 km verschoven naar de dichtstbijzijnde zichtbaar actieve put). https://www.mindat.org/loc-19225.html
[5] NS Energy Business, Weda Bay Nickel Project — acht putten (Bukit Limber Barat/Timur groot; Nuspera, Uni Uni, Biri-Biri Barat/Timur, Sake Barat, Ake Sake, Tofu Bleuwen klein, ~40 % van de output); mijn ligt ~70 km van Ternate (niet van IWIP). https://www.nsenergybusiness.com/projects/weda-bay-nickel-project/
[6] Wikipedia, Weda Bay Industrial Park — coördinaat 0.47832, 127.98363 (MediaWiki API `prop=coordinates`); RKEF- en HPAL-lijnen op één kustterrein. https://en.wikipedia.org/wiki/Weda_Bay_Industrial_Park
[7] OpenStreetMap (ODbL) via Nominatim + lokale scan — village-node Lelilef Sawai 0.5866272/127.9860048; bbox-scan 0.25–0.75 N / 127.75–128.30 O: 88 trunk / 138 unclassified / 55 track / 29 tertiary, mijnwegnamen als unclassified/service, 1 ongelabelde pipeline-way (niet gebruikt). Overpass zelf was tijdens dit onderzoek onbereikbaar (timeout, beide mirrors). https://www.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16, live) — `v2/build-cache/satcheck/sat-nikkel-wedabay-iwip-park.png`, `-lelilef.png`, `-mindatmine.png`, `-pit-z15.png`, `-pit2-z16.png`, `-jetty-z15.png`, `-jetty2-z16.png`.
[9] Argus Media — Huafei (Huayou) HPAL Weda Bay: 120.000 t/j Ni + 15.000 t/j Co nameplate, productie sinds 2023. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2483610-huayou-vale-commit-to-indonesian-huali-mhp-project
[10] Argus Media, 2026 — Huafei zet de helft van zijn MHP-capaciteit op *care & maintenance* door hoge zwavelkosten. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2820208-indonesia-s-huafei-to-cut-mhp-output-on-sulphur-costs

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `nikkel-wedabay-iwip`** → `v2/data/stroomroute-nikkel-wedabay-iwip.json` — 1 been, 7,9 km, 3 markers: truck 7,9 km.
Recept: `bak_stromen.sh` (functie `bak_nikkel_wedabay_iwip`). Toelichting: één wegscan (profiel `nikkel-wedabay-iwip-pit-rkef`, extract `indonesie`, `corridorKlassen`: unclassified/tertiary/service + `eindToegangPrivaat` aan beide uiteinden) van de put via het erts-schermstation en de eerste IWIP-industrieweg-kruising naar het ore-yard-anker. De scan vond een doorgaand pad over de kleine wegklassen — de vooraf verwachte stippel-knip bij de put (waar OSM mogelijk alleen `track`/`service` heeft) bleek niet nodig; beide uiteinden snappen ruim binnen 0,5 km op de weg (0,12 km resp. 0,39 km). Gemeten lengte 7,4 km weggeometrie (7,9 km met de korte anker-aanlopen) tegen de losse hemelsbrede controle van 3,6 km uit de brief = **+104%**, buiten de ±15%-norm maar bewust géén harde toets (brief §2/bak-aanwijzing: geen gepubliceerde km, het reliëf kan het pad fors verlengen) — blijft als bevinding staan. Eén keerlus gesnoeid (12,1 → 7,4 km dubbel gereden stuk). `toets_knikken.py`: 7 scherpe knikken (spikes, tot 92 m straal — normaal voor een smalle mijnweg), **0 omkeringen, 0 terugloop** — geen reparatie nodig. `toets_rechte_benen.py --min-km 5`: geen bevinding (de lijn is geen rechte koorde). Bestand 3,3 KB, versie 2, `punt_formaat` lonlat, modaliteit `truck` — allemaal binnen de norm. Marker `ni-iwip-jetty` (havenbekken, ~5 km oostelijker op hetzelfde terrein) is marker-alleen, geen been (last-mile-regel). Geen zeebeen getekend: export naar Chinese roestvrijstaal-mills bestaat aantoonbaar maar is nergens op fabrieksniveau gebrond (brief §6) — de keten stopt bewust op `ni-iwip-rkef`.

**Gereedschapslessen:** `trunk` hoeft niet in `corridorKlassen`: die klasse zit al in de default `WEG_HOUD`-set van `fetch_landnet.py` (motorway/trunk/primary/secondary + links) en hoeft alleen als extra kleine klasse toegevoegd als hij ook in `eindKlassen` moet — anders weigert het profiel met "corridorKlasse 'trunk' staat niet in eindKlassen". `gepubliceerdKm` mag geen `None` zijn (de lengtetoets deelt erdoor): bij een ontbrekende publicatie de hemelsbrede satellietmeting als getal invullen en de bevinding in de bronnoot benoemen, `vensterKm` ruim zetten voor het echte toetsdoel.
