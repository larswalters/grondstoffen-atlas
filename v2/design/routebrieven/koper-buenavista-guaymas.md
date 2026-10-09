# Routebrief (licht) · koper — Buenavista (Cananea) → Guaymas (Mexico)

**stroom-id:** `koper-buenavista-guaymas` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** koperconcentraat (~24 % Cu) van de concentrators van Buenavista del Cobre (Grupo México/Southern Copper, Cananea, Sonora)
per **trein** (aannemelijk: één bron; SCC zegt "truck of spoor") over de Cananea-tak naar Nogales en de Sonora-hoofdlijn
(Nogales–Imuris–Benjamín Hill–Hermosillo–Empalme) naar het mineralenemplacement van het Puerto de Guaymas aan de Zee van Cortés — één landbeen, geen zeebeen.
**Welke as van het verhaal:** Mexicaans concentraat naar de exporthaven aan de Pacific-kant, het contrapunt van de Andes-assen. Buenavista 2024:
**954,5 Mlb = 433 kt Cu** gemijnd, waarvan **769,3 Mlb = 349 kt Cu in concentraat** en 185,2 Mlb = 84 kt als SX-EW-kathode [1]; het deel dat naar Guaymas gaat (versus smelter La Caridad) is niet gepubliceerd.

## 1 · Ketenkaart
```
Buenavista-concentrators `cu-buenavista-kop` ──(b1 spoor · Cananea-tak → Nogales → Sonora-hoofdlijn · OSM-pad 553 km, hemelsbreed 343)──► Puerto de Guaymas, mineralenemplacement `cu-guaymas-haven` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `cu-buenavista-kop` → `cu-guaymas-haven` | Cananea–Nogales-tak (Ferromex/Grupo México) → Sonora-hoofdlijn Nogales–Santa Ana–Benjamín Hill–Hermosillo–Empalme–Guaymas [1][4][5] | hemelsbreed 343 km, OSM-pad 553 km, geen gepubliceerde spoorkm; ±15 %-toets is indicatie. Historisch (Wikipedia): Cananea–Nogales-lijn 122 km + Guaymas–Nogales 426,1 km = 548 km → OSM +0,8 % [4] | toets_spoorroute (4 runs, extract mexico) | nee |

Beennaam voor de bak: `trein (aannemelijk: één bron: SCC 10-K zegt truck of spoor naar La Caridad of Guaymas)`. Geen zeebeen, geen haven-aanloop, geen stippel (kop snap 0,00 km, staart snap 0,18 km).
Gemeten tussenstanden (OSM-pad, `BAKE_SUFFIX=-raw`, `--hoofd-km=100`): Cananea→Nogales (km 139) · kop→V1 151,7 · V1→V2 129,0 · V2→V3 133,9 · V3→Guaymas 138,1 = **552,7 km** (identiek aan één vrije run, 466 edges).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-buenavista-kop` | mijn/concentrator (kop van het spoor) | Buenavista del Cobre, concentrators + verdikkers, Cananea | 30.9722, -110.3140 | [1][8][9] | bron-gelegd (z15 gezien: concentratorcomplex met procesgebouwen en vier ronde verdikkers/bekkens, de dagbouwput ligt aan de westkant; OSM-spoor snap 0,00 km). Let op: sitelaag `w-buenavista` (30.9606, -110.3314) is de put, 2,1 km WZW — de keten start bewust bij de concentrators |
| `cu-guaymas-haven` | overslag trein → schip (stoppunt) | Puerto de Guaymas, mineralenemplacement (schiereiland) | 27.9208, -110.8713 | [1][2][3][8][9] | aannemelijk (z15 gezien: spoorplaats met treinen en donkere bulkstapels op het havenschiereiland, bulkcarrier aan de ZO-kade; z17: 150 m ten NO van een lange tongdak-loods naast de tankopslag = "Instalación de Concentrados" op de ASIPONA-plattegrond [3]. Welke concessionaris die loods exploiteert en welke kade Grupo México gebruikt is niet bevestigd) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | V1 | Nogales-zuid, op de hoofdlijn (14 km ten Z van de stad, snap 0,00) | 31.1817, -110.9719 | Cananea-tak komt bij Nogales op de Sonora-hoofdlijn; punt ligt buiten het stadscentrum; pint de oversteek Cananea-tak → hoofdlijn [1][4][5] |
| b1 | V2 | Benjamín Hill, op de hoofdlijn (1,7 km NW van het station, snap 0,43) | 30.1842, -111.1135 | splitsing met de lijn naar Mexicali/Sonora-Baja California [2]: houdt de route op de zuidtak naar Hermosillo |
| b1 | V3 | Hermosillo-zuid, op de hoofdlijn (4 km ten Z van de stad, snap 0,00) | 29.0341, -110.9283 | pint de passage Hermosillo; punt niet in het centrum |
Runs: kop→V1 → V1→V2 → V2→V3 → V3→staart, in reisvolgorde; naden 0,00 km (alle uiteinden snappen op dezelfde knoop).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Buenavista-concentrators 1 + 2 | Southern Copper (Grupo México) | sulfide-erts → koperconcentraat ~24 % Cu | 349 kt Cu in concentraat in 2024 (≈ 1,45 Mt concentraat, eigen berekening 349 kt ÷ 24 %) | [1] |
| Puerto de Guaymas, mineralenemplacement | ASIPONA Guaymas; concessionaris onbevestigd (Mexicana de Cobre, Grupo México, staat als cesionario "minerales y fluidos") | trein → bulkcarrier | haven 2025: 5,0 Mt totaal, 2,45 Mt granel mineral (alle mineralen, geen koper-split); 15 km havenspoor binnen het terrein | [2][3] |

## 6 · Stoppunt
De brief stopt op het mineralenemplacement van het Puerto de Guaymas: SCC noemt de afnemers alleen als klanten "in de VS, Europa, Azië en Zuid-Amerika" [1], geen bron koppelt Buenavista-concentraat aan een smelter of schip na de haven — fase D en E vervallen.

## 7 · Open punten
- **Spoor of truck, en aandeel Guaymas:** SCC schrijft "per truck of spoor naar La Caridad of Guaymas" [1]; geen modaliteit- of aandeelcijfer. Bovengrens: 349 kt Cu ≈ 1,45 Mt concentraat tegen 2,45 Mt granel mineral in de haven (2025, inclusief ijzererts, kolen e.d.) [3] — een groot deel kan dus niet allemaal via Guaymas.
- **Kade/loods van het concentraat niet gevonden:** [3] toont "Instalación de Concentrados" (privé) en lijst Mexicana de Cobre als cesionario; het koppelen van beide is een gevolgtrekking. Het Grupo México-zwavelzuurincident (2019) lag volgens Expansión "tussen de muelles 5 en 6" [7], een vloeistoffenfaciliteit, niet bewezen als de concentraatkade. Geen kade-stippel getekend.
- **Cananea-tak niet met bedrijfskm bevestigd:** het historische ontwerp voegde bij Imuris aan (122 km, [4]); het OSM-pad loopt via Nogales (Cananea→Nogales-station ~139 km, +14 % tegen 122) en past bij SCC "railway to Agua Prieta and Nogales" [1]. Via Imuris zou de route ~475 km zijn (122 + ~351); OSM kent die verbinding niet.
- **Kopmaak-spoor:** bij de kop meet de router een omkering van 174° (30.9805, -110.3206) = een ~0,6 km lang stomp-/kopmaakspoor binnen het concentratorterrein, geen routefout; bak laat het staan (bevinding).
- Sitelaag: `w-buenavista` ligt op de put (2,1 km van de concentrators); centraal beslissen of dat gelijkgetrokken wordt.
- Fase D (afnemer na de haven) en volume naar Guaymas zijn niet gedocumenteerd.

## 8 · Bronnen
[1] Southern Copper, Form 10-K FY2024 (productietabel Buenavista 954,5 Mlb; concentraat 769,3 Mlb; "Concentrates are then sent by trucks or by railroad to the La Caridad smelter or to the Guaymas port"; "Buenavista is also connected by railway to Agua Prieta and Nogales"; Marine Terminal in Guaymas). https://www.sec.gov/Archives/edgar/data/1001838/000155837025002017/scco-20241231x10k.htm
[2] ASIPONA Guaymas, presentatie VI Conferencia Hemisférica 2024 (15 km havenspoor, koperconcentraat onder granel mineral, Ferromex-kaart). https://www.gob.mx/cms/uploads/attachment/file/882820/1.17_ASIPONA_Presentaci_nVIConfHemisf__ASIPONA_GUAYMAS_.pdf
[3] ASIPONA Guaymas, "Puerto en modernización" (hb.pdf: plattegrond met "10 Instalación de Concentrados", cesionarios incl. Mexicana de Cobre, vrachtcijfers 2025). https://www.puertodeguaymas.com.mx/descargas/hb.pdf
[4] es.wikipedia, "Ferrocarril de Sonora" (Guaymas–Nogales 426,1 km; Cananea–Nogales 122 km, rechte lijn 75 km, aansluiting bij Imuris gepland; Cananea–Naco 61,9 km). https://es.wikipedia.org/wiki/Ferrocarril_de_Sonora
[5] es.wikipedia, "Ferrocarril Cananea-Río Yaqui y Pacífico" (tramo Cananea–Nogales). https://es.wikipedia.org/wiki/Ferrocarril_Cananea-Río_Yaqui_y_Pacífico
[6] es.wikipedia, "Estación de Nogales (Sonora)" (ramales die Nogales met Cananea, Naco, Agua Prieta en Nacozari verbonden). https://es.wikipedia.org/wiki/Estación_de_Nogales_(Sonora)
[7] Expansión, "Grupo México: derrame de ácido sulfúrico en el Mar de Cortés" (terminal marítima de Guaymas, Metalúrgica de Cobre, tussen muelles 5 en 6). https://politica.expansion.mx/mexico/2019/07/11/grupo-mexico-derrame-acido-sulfurico-en-el-mar-de-cortes
[8] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-koper-buenavista-guaymas-kop.png` (z15), `…-guaymas.png` (z15), `…-schuur.png` (z17).
[9] OpenStreetMap-spoor 1-op-1 (Geofabrik extract Mexico, ODbL) via `toets_spoorroute.mjs`: `v2/build-cache/ais/graaf/spoorroute-koper-buenavista-guaymas-{kop-nogales,nogales-benjaminhill,benjaminhill-hermosillo,hermosillo-guaymas}.geojson`.
[10] Dry Cargo, "Minerals terminal confirmed for Guaymas" (2009: Cortez Transfert, andere partij, geen Grupo México). https://www.drycargomag.com/minerals-terminal-confirmed-for-guaymas
[11] `v2/design/koper-sitelaag.json`, site `w-buenavista` (put 30.9606, -110.3314; capaciteit 433 kt Cu).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Functie:** `bak_koper_buenavista_guaymas` in `v2/tools/bak_stromen.sh` · **uitvoer:** `v2/data/stroomroute-koper-buenavista-guaymas.json` (22,1 KB, versie 2, `lonlat`) · **registerregel (centraal):** `cu-bv`.
**Recept:** vier `--been-geojson "spoor|…"`-regels uit de vooraf gebakken spoorruns (`toets_spoorroute.mjs`, `BAKE_SUFFIX=-raw`, extract mexico, `--hoofd-km=100`, 3.260.717 spoor-edges), in reisvolgorde kop → V1 Nogales-zuid → V2 Benjamín Hill → V3 Hermosillo-zuid → Guaymas; twee markers (kop, haven). Geen herrouting: de geojsons zijn hergebruikt (identiek aan de brief).

| # | modaliteit | km (bake) | punten | naad | beschrijving |
|---|---|---|---|---|---|
| b1 | spoor | 153,0 | 463 | – | concentrators → Nogales-zuid (Cananea-tak) |
| b2 | spoor | 129,5 | 264 | 0,00 | Nogales-zuid → Benjamín Hill |
| b3 | spoor | 135,9 | 236 | 0,00 | Benjamín Hill → Hermosillo-zuid |
| b4 | spoor | 138,2 | 124 | 0,00 | Hermosillo-zuid → Puerto de Guaymas |
| | | **556,6** | 1.087 | max 0,00 | geen stippel, geen zee, geen wegprofiel, geen kopie |

**Markers:** `Buenavista del Cobre — concentrators + verdikkers` (30.9722, -110.3140) 0,00 km van de lijn · `Puerto de Guaymas — mineralenemplacement, stoppunt (aannemelijk)` (27.9208, -110.8713) 0,18 km van de lijn (staartsnap).
**Toets (±15% als indicatie):** bake 556,6 km tegen het OSM-pad 552,7 km (+0,7%, verschil = sommatie van de vier geometrieën tegen de routerkm) en tegen de historische bouwlengtes 122 + 426,1 = 548 km (+1,6%); hemelsbreed 343 km, geen gepubliceerde actuele spoorkm, dus de toets is een indicatie en geen norm. Naden 0,00 km. `toets_knikken.py`: 1 omkering van 174,5° bij 30.9805,-110.3206 (R 139 m, kopmaak-/stompspoor ~0,6 km in het concentratorterrein, ook met `--keerstraf=300` niet te vermijden; bevinding, niet dichtgetrokken). `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom. `json.load` ok, versie 2, `lonlat`, modaliteit alleen `spoor`, elk been ≥ 2 punten.
**Toelichting:** geen stippel (kop snap 0,00 km, staart 0,18 km), geen haven-aanloop (geen zeebeen), geen vlucht, geen leiding. De modaliteit "trein" is aannemelijk (één bron: SCC 10-K "truck of spoor") en staat in de beennaam, het been is doorgetrokken.
**Lessen / bevindingen:** (1) het kopmaakspoor blijft zichtbaar als spike op de kaart; (2) de Cananea-tak loopt in OSM via Nogales (139 km, +14% tegen de historische 122 km), niet via Imuris; (3) de kade/loods in Guaymas is niet gevonden, het stoppunt is het emplacement en er is geen kade-marker; (4) sitelaag `w-buenavista` (30.9606, -110.3314) ligt op de put, 2,1 km WZW van het concentratoranker, centraal beslissen over gelijktrekken; (5) de sloten-snippet van de kaart gebruikt `rm -rf "$d"` op een variabele, wat de veiligheidscontrole blokkeert: slot nemen/vrijgeven kan zonder `rm -rf` (`rm -f sinds; rmdir`), dezelfde mapstructuur.
