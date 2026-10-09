# Kolen · Mine 7 (Brookwood) → Montgomery → McDuffie Coal Terminal, Mobile (Alabama, VS)

**stroom-id:** `kolen-brookwood-mobile` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** cokeskool (hard coking coal) uit de ondergrondse Warrior Met Coal-mijn No. 7 bij Brookwood (Tuscaloosa County,
Alabama) per CSX-spoor via Birmingham en Montgomery (M&M Subdivision) naar de McDuffie Coal Terminal van de Alabama State Port Authority
in Mobile, waar het op oceaanschepen voor Azië, Europa en Zuid-Amerika gaat. Eén spoorbeen, geen zeebeen (geen bron noemt een loshaven).
**Welke as van het verhaal:** VS-Golfkust: Alabama-cokeskool naar de export. Warrior Met 2025: 9,3 Mt staalkool geproduceerd (Mine 7 +
Mine 4 + Blue Creek samen; 10-K FY2025 [1]), 8,7 Mt verkocht; afzet 2025: Azië 48%, Europa 37%, Zuid-Amerika 14%, VS 1% [1].
**Eenheid: Mt kolen per jaar.** Geen split per mijn gepubliceerd; Mine 7 apart is niet te geven (§7).

## 1 · Ketenkaart
```
Mine 7 (Warrior Met, Brookwood AL) `kolen-brookwood-laad`
   ──(b1 spoor · CSX via Birmingham-keerpunt, Montgomery, Evergreen, Flomaton, Bay Minette · 496,1 km gemeten, ~483 km (300 mijl) bij Warrior)──►
McDuffie Coal Terminal, Mobile `kolen-mcduffie-kade` ── stoppunt (geen loshaven genoemd)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-brookwood-laad` → `kolen-mcduffie-kade` | CSX: mijnaansluiting → Birmingham → S&NA South Sub → Montgomery → M&M Sub (Montgomery–Mobile) [1][5] | ~483 km (Warrior: "approximately 300 miles" mijn–haven, geen spoorkm) [1]; M&M Sub Montgomery–Mobile 286,8 km [5] | toets_spoorroute (`BAKE_SUFFIX=-raw`) | nee (snap 0,45 en 0,22 km, < 2 km) |

Gemeten: 496,1 km over 531 edges (hemelsbreed 305,5 km, verhouding 1,62) = +2,7% tegen ~483 km: binnen ±15%. Deelcontrole: Montgomery →
Mobile in het geojson ~292 km tegen 286,8 km gepubliceerd (+1,8%). Het geojson raakt Montgomery, Evergreen, Brewton, Flomaton en Bay Minette op
0,2–0,3 km, dus het volgt de CSX-lijn Montgomery–Mobile. Geen zeebeen: de zeeknoop (MARNET 4923, 30.6698,-87.9991) ligt 3,9 km van de kade (< 5 km).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-brookwood-laad` | mijn / laadlus | Warrior Met Coal Mine No. 7, prepplant en spoorlus, Brookwood (Tuscaloosa Co.) | 33.3215, -87.2428 | [1][2][7] | bron-gelegd (z15 gezien: prepplant met kolenstapels en transportbanden, daaronder een spoorlus met meerdere sporen die naar het zuiden uitloopt; punt op de lus 0,6 km ten zuiden van het 10-K-punt 33.3264, -87.2461, dat midden in het mijncomplex ligt; `sat-kolen-brookwood-mobile-mine7.png`) |
| `kolen-mcduffie-kade` | overslag spoor → zeeschip | McDuffie Coal Terminal (Alabama State Port Authority), McDuffie Island, Mobile | 30.6579, -88.0374 | [3][4][7] | bron-gelegd (z15 gezien: zwarte kolenstapels met treinsporen en scheepsladers langs de kade aan Mobile River/Bay, aparte containerterminal ten noorden; `sat-kolen-brookwood-mobile-mcduffie.png`) |

## 4 · Via-punten (alleen spoorbenen met een corridorkeuze)
Geen. De ontwerpnoot vroeg om 3–6 via-punten tegen de omkering bij Birmingham; die omkering (180°, 33.5096, -86.8124, boogstraal ~36 m) blijft
ook bij een hoge keerstraf staan en komt uit de OSM-topologie, geen via-punt lost haar op. Er is geen corridorkeuze: één CSX-pad Mine 7 → Birmingham
→ Montgomery → Mobile. Montgomery (32.3845, -86.3113) en Flomaton (31.0236, -87.3248) liggen op de route en kunnen als controlepunt dienen.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mine 7 prepplant | Warrior Met Coal | ruwe kool → gewassen cokeskool (Low Vol HCC) | Mine 4 prepplant 1.300 t/u; Mine 7 niet genoemd | [1] |
| McDuffie Coal Terminal | Alabama State Port Authority | trein of schuit → zeeschip | 27,22 Mt/j (GEM); 30 Mst (EIA); 2018: 11 Mst afgehandeld | [3][4] |

## 6 · Stoppunt
De brief stopt bij de McDuffie-kade: Warrior verkoopt "at the loading port" (FOB/CFR, koper regelt verder) en noemt geen losland of haven per lading [1],
dus geen zeebeen.

## 7 · Open punten
- **Mine 7 of Mine 4:** beide worden door CSX bediend en liggen bij Brookwood [1]; geen bron geeft het aandeel per mijn. Mine 4 (33.3303, -87.3256) en
  de Blue Creek-mijn (33.5892, -87.4431, geserveerd door Norfolk Southern, niet CSX [1]) zijn niet getekend.
- **Rail versus schuit:** beide mijnen hebben een bargeload-out op de Black Warrior River naar Mobile [1]; het aandeel is niet gepubliceerd. Alleen
  het spoor is getekend.
- **Omkering Birmingham:** het router-pad loopt eerst 53 km noordoost naar Birmingham, keert en gaat 155 km naar Montgomery. Zo staat het in OSM;
  een bron die de treindienst bevestigt is niet gevonden.
- **Volume per mijn en 2025 vs nameplate:** 9,3 Mt is de som van drie mijnen (Blue Creek startte longwall in okt 2025). Het ontwerp noemde 13 Mst
  nameplate; die is niet gestaafd en niet gebruikt.
- **Kade-ankerrol:** het punt ligt op de kolenstapels van het terminalterrein, niet op de scheepslader; de exacte laadplek is niet gelegd.
- **v1:** `data/coal.js` en `design/kolen.md` hebben geen Alabama-stroom; geen sitelaag-anker te hergebruiken.

## 8 · Bronnen
[1] Warrior Met Coal, Form 10-K FY2025 (SEC EDGAR, 2026): Mines 4 en 7 bij Brookwood, bediend door CSX; bargeload-out Black Warrior River; ~300 miles
mijn-haven Mobile; 9,3 Mt in 2025; Mine 7 33°19'35"N 87°14'46"W; Blue Creek door NS; afzet 48/37/14/1%.
https://www.sec.gov/Archives/edgar/data/1691303/000119312526048914/hcc-20251231.htm
[2] Warrior Met Coal, Form 10-K FY2024: CSX, barge, McDuffie Terminal; 7,5 Mt in 2024; Mine 4 33°19'49"N 87°19'32"W.
https://www.sec.gov/Archives/edgar/data/1691303/000169130325000010/hcc-20241231.htm
[3] Global Energy Monitor, McDuffie Coal Terminal: eigenaar Alabama State Port Authority, 2018 11 Mst cokeskool voor export, geen lat/lon.
https://www.gem.wiki/McDuffie_Coal_Terminal
[4] EIA, Today in Energy: McDuffie (Mobile) 30 Mst capaciteit, vooral cokeskool. https://www.eia.gov/todayinenergy/detail.php?id=32092
[5] Wikipedia, "M&M Subdivision": CSX, Montgomery–Mobile 178,2 mijl (286,8 km). https://en.wikipedia.org/wiki/M%26M_Subdivision
[6] Wikipedia, "Port of Mobile": Alabama State Port Authority beheert de publieke terminals; stadscentroïde 30.71217, -88.04331 (geen anker). https://en.wikipedia.org/wiki/Port_of_Mobile
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-kolen-brookwood-mobile-mine7.png`, `…-mcduffie.png`.
[8] Eigen routerrun `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=33.3215,-87.2428 --naar=30.6579,-88.0374
--naam=kolen-brookwood-mobile-mine7-mcduffie --hoofd-km=1000 --max-snap=60` (3.260.717 spoor-edges): 496,1 km, 1.138 punten, 1 omkering (Birmingham).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)

**Eén been (spoor), 499,9 km · 1.138 punten · 2 markers · `v2/data/stroomroute-kolen-brookwood-mobile.json` (21,5 KB).**

| # | modaliteit | km | punten | naad | toelichting |
|---|---|---|---|---|---|
| 1 | spoor | 499,9 | 1.138 | n.v.t. (enige been) | CSX Mine 7 Brookwood → Birmingham (keerpunt) → Montgomery → M&M Sub → McDuffie Coal Terminal, Mobile |

**Recept:** `bash v2/tools/bak_stromen.sh kolen-brookwood-mobile` (functie `bak_kolen_brookwood_mobile`, `v2/tools/bak_stromen.sh`). Het geojson
`v2/build-cache/ais/graaf/spoorroute-kolen-brookwood-mobile-mine7-mcduffie.geojson` komt uit
`BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=33.3215,-87.2428 --naar=30.6579,-88.0374 --naam=kolen-brookwood-mobile-mine7-mcduffie --hoofd-km=1000 --max-snap=60`
(3.260.717 spoor-edges, 531 edges, snap 0,45 en 0,22 km) en is hergebruikt, niet opnieuw gerund; `hecht_marnet.py route` nam het als `--been-geojson`.
Geen wegprofiel, geen zeebeen, geen haven-aanloop, geen luchtbeen, geen leiding, geen stippel.

**Km-toets:** de router meldt 496,1 km; `hecht_marnet` meet 499,9 km (andere afstandsformule over dezelfde 1.138 punten, +0,8%). Tegen ca 483 km (300 mijl, Warrior
10-K, geen spoorkm) is dat +3,5%, binnen de ±15%-norm (indicatie, want de bron is een mijn-haven-afstand, geen spoorlengte). Deelcontrole Montgomery → Mobile
in het geojson ca 292 km tegen 286,8 km (M&M Sub, Wikipedia) = +1,8%.

**Naden en markers:** één been, dus geen naad. Mine 7-marker 0,38 km van de lijn, McDuffie-marker 0,21 km (beide ≤ 0,5 km). Zeeknoop 4923 ligt 3,9 km van de kade
(< 5 km), dus geen haven-aanloop nodig.

**Knikken:** `toets_knikken.py` vindt 1 omkering (180 graden, 33.5096,-86.8124, Birmingham, boogstraal ~0 m, geen terugloop). Zo staat het in OSM; geen bron
bevestigt de treindienst en geen via-punt lost haar op (§4, §7). `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom.

**Contract:** `json.load` slaagt, versie 2, punt_formaat lonlat, modaliteit spoor, 1.138 punten, 22,1 KB.

**Lessen:** (1) een reeds gerund spoorgeojson hergebruiken scheelt de router (15 s totale bake). (2) De 1-op-1-spoorroute Brookwood → Mobile loopt eerst 53 km
noordoost naar Birmingham en 155 km terug zuidwest naar Montgomery; dat is OSM-topologie, geen routefout, en het blijft een open punt (§7).
