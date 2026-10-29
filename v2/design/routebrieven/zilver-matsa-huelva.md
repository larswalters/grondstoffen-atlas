# Routebrief (licht) · Zilver · MATSA Aguas Teñidas → Muelle Sur Huelva → Atlantic Copper (Spanje)

**stroom-id:** `zilver-matsa-huelva` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** Cu-, Cu-poly-, Zn- en Pb-concentraat (met zilver als bijproduct) van Sandfire's centrale verwerkingsinstallatie van MATSA (Almonaster la Real, Huelva) per **truck** (HU-6102 → HU-5101 → HU-4100 → N-435 → A-49 → H-30 → N-442, ~90 km) naar de concentraatterminal van Impala Terminals Huelva (ex Onubaport Logistic, MATSA-groep) op de Muelle Ingeniero Juan Gonzalo van het Puerto Exterior; daarna (aannemelijk, één bron) een korte truckrit naar de Atlantic Copper-smelter, waar het zilver in de anodeslijmen belandt. Het zeebeen en de afnemers van de overige concentraten zijn niet gepubliceerd.
**Welke as van het verhaal:** *Iberische Pyrietgordel: bijproduct-zilver in basismetaalconcentraat* — FY25 (jul 2024–jun 2025) 3,081 Moz Ag contained = **≈ 96 t Ag/j** in 498,2 kt concentraat, payable 2,040 Moz = ≈ 63 t Ag/j [2].

## 1 · Ketenkaart
```
MATSA-concentrator, Aguas Teñidas (Sandfire) `ag-matsa-plant`
   ──(b1 truck · HU-6102 → HU-5101 → HU-4100 → N-435 → A-49 → H-30 → N-442 · ~90 km Sandfire / OSM-pad 94 km)──►
Impala Terminals Huelva, nave sur, Muelle Ingeniero Juan Gonzalo `ag-huelva-terminal`
   ──(b2 truck · N-442 → H-30 → Av. Francisco Montenegro · aannemelijk: één bron)──►
Atlantic Copper-smelter, Huelva `ag-atlanticcopper-smelter` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ag-matsa-plant` → `ag-huelva-terminal` | HU-6102, HU-5101, HU-4100 (Valverde-Cabezas Rubias), N-435, A-49 (Quinto Centenario), H-30, N-442 — corridor NIET gepubliceerd, afgeleid uit het OSM-pad (OSRM, alleen als diagnose) [13] | **~90 km** (Sandfire: haven "~90km from site" [1], geen routekm); OSM-pad 94,2 km; hemelsbreed 69,3 km | maak_stroombeen_weg (extract `spanje`, nieuw profiel) | nee |
| b2 | D | truck | `ag-huelva-terminal` → `ag-atlanticcopper-smelter` | N-442 → H-30 → Avenida de Francisco Montenegro; aannemelijk: één bron noemt Atlantic Copper als bestemming [7] | hemelsbreed 10,5 km, geen wegkm; OSM-pad 11,9 km [13] | maak_stroombeen_weg (extract `spanje`) | nee |

Geen zee-, spoor- of leidingbeen: Sandfire zegt alleen dat de concentraten "vanuit de haven van Huelva" worden geëxporteerd [1]; schip, bestemming en smelter overzee zijn niet gepubliceerd, dus niet getekend.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-matsa-plant` | concentrator (kop) | Centrale verwerkingsinstallatie MATSA, complex Aguas Teñidas, Almonaster la Real (4,7 Mtpa) | 37.7770, -6.8543 | [1][12] | bron-gelegd (z16 gezien: twee lange flotatiehallen met dakpatroon, verdikkers en een groot tailingsbekken direct ten zuiden; OSM-label "Minas de Aguas Teñidas" ligt 0,4 km zuidoostelijk op het bekken, 37.7732/-6.8532; Sandfire noemt de plantlocatie zelf niet) |
| `ag-huelva-terminal` | overslag: concentraatterminal / kade | Impala Terminals Huelva SL (ex Onubaport Logistic), "nave de almacenamiento sur" (28.000 m²), Muelle Ingeniero Juan Gonzalo, Puerto Exterior, Palos de la Frontera | 37.1535, -6.8768 | [3][4][5][6][11] | aannemelijk (z14–z17 gezien: de enige grote gesloten opslagloods in de zuiduitbreiding van de Muelle Sur, naast de containerkade met portaalkranen; ±14.000 m² dak tegen 28.000 m² gerapporteerd, dus niet één-op-één gematcht) |
| `ag-atlanticcopper-smelter` | smelter / afnemer (stoppunt) | Atlantic Copper (Freeport-McMoRan), Complejo Metalúrgico, Punta del Sebo, Huelva (60 ha) | 37.2287, -6.9482 | [7][8][9][12] | bron-gelegd (z15 gezien: smeltergebouwen met schoorstenen, concentraat- en grondstofstapels en steigers langs de Odiel; OSM-object "Atlantic Copper" 0 m van het punt) |

## 4 · Via-punten (b1 landbeen; alle op de doorgaande weg, nooit in een kern)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | HU-6102 | 37.7850, -6.8737 | de mijnweg gaat west naar HU-6102 (keuze west of oost) |
| b1 | 2 | HU-5101 | 37.7344, -6.9322 | pint de zuidwaartse HU-5101 naar Calañas |
| b1 | 3 | HU-4100 | 37.5899, -6.8446 | pint de A-496/HU-4100-corridor bij Valverde del Camino (niet via Calañas-centrum) |
| b1 | 4 | N-435 | 37.5239, -6.7961 | aansluiting op de N-435 (Zafra-Huelva) |
| b1 | 5 | A-49 | 37.3229, -6.8456 | oprit op de autovía Sevilla-Huelva (keuze N-435 of A-49) |
| b1 | 6 | H-30 | 37.2776, -6.9218 | Huelva-ringweg ten noorden, vóór de stad |
| b1 | 7 | N-442 | 37.1958, -6.9253 | N-442 zuidwaarts naar het Puerto Exterior (niet het stadscentrum) |
| b2 | 1 | N-442 | 37.1958, -6.9253 | terug noordwaarts op de N-442 (zelfde knoop als b1-7) |

Alle via-punten liggen binnen 3 m van de weg (OSRM nearest, [13]). Hun coördinaten zijn OSRM-manoeuvres, geen eigen satellietlegging: de scan moet de doorgaande rijbaan vinden.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| MATSA-concentrator | Sandfire (100%) | erts (Aguas Teñidas, Magdalena, Sotiel) → Cu-Cu 83,2 · Cu-poly 193,1 · Zn 194,3 · Pb 27,6 kt concentraat (FY25) | geïnstalleerd 4,7 Mtpa; FY25 gemalen 4,53 Mt; 498,2 kt concentraat; Ag 3,081 Moz contained / 2,040 Moz payable | [1][2] |
| Impala Terminals Huelva (concentraatterminal) | MATSA-groep (Impala-naam; eigendom na de Sandfire-overname onbevestigd) | opslag, blending en verzending van Cu- en Zn-concentraat | concessie 135.000 m² aangevraagd (2013); nave sur 28.000 m² (bouw 2015–16) | [3][4][5] |
| Atlantic Copper | Freeport-McMoRan | Cu-concentraat → anodes 99,5% → kathode; anodeslijmen met typisch 8,5% Ag | smelter 330 kt anode/j, raffinaderij 285 kt kathode/j; slijmen verkocht aan gespecialiseerde raffinaderijen | [8][9][10] |

## 6 · Stoppunt
De brief stopt bij de Atlantic Copper-smelter: daar eindigt het concentraat en het zilver gaat in de anodeslijmen, die zonder genoemde afnemer aan "refinerías especializadas" gaan [10]; fase E vervalt. Zou b2 niet bevestigd worden, dan is de kade het stoppunt.

## 7 · Open punten
- **Afnemers van MATSA's concentraten zijn niet gepubliceerd** (Sandfire noemt geen smelter); alleen es.wikipedia noemt Atlantic Copper voor het Aguas Teñidas-kopercondensaat, met een onduidelijk cijfer (2019: "unas 100.000 toneladas de cobre") [7]. Pb-, Zn- en overzeese kopersmelters en het zeebeen ontbreken dus.
- **Weg of haven?** Atlantic Copper ontvangt ook concentraat "por carretera desde explotaciones de la provincia de Huelva" [8]; of MATSA-koper rechtstreeks per weg naar de smelter gaat of via de Impala-terminal, is niet gebrond. b2 is daarom aannemelijk en loopt over b1's staart terug (±8 km overlap).
- **Corridor b1 niet gepubliceerd**; de ~90 km is Sandfire's afstand haven-site, niet als routekm gespecificeerd. OSM-pad 94,2 km, binnen ±15%.
- **Terminal niet 1-op-1 bevestigd**: ligging van Impala's nave sur uit bouwbericht + satelliet; de factsheet (240.000 t statische capaciteit, 550 m privékade, 1 Mt/j) kon niet geopend worden (404). Het kadeanker (waar het schip ligt) is niet apart gelegd, want er is geen zeebeen.
- **Zilveraandeel per concentraat** (Cu-poly, Pb, Cu-Cu) niet gepubliceerd; de 96 t Ag/j is contained in alle concentraten samen.
- **v1 (`data/silver.js`) en de zilver-sitelaag kennen MATSA niet**; een site van ≈ 96 t Ag/j contained ontbreekt in de sitelaag (melding aan de orchestrator).
- Wegen in het port- en smelterterrein kunnen `access=private` dragen (zie bak-aanwijzing eindToegangPrivaat).

## 8 · Bronnen
[1] Sandfire, "MATSA operations" — mijnen Aguas Teñidas/Magdalena (Almonaster la Real), Sotiel (Calañas), plant 4,7 Mtpa, export vanuit Puerto de Huelva "~90km from site". https://www.sandfire.com.au/where-we-operate/matsa/
[2] Sandfire, June 2025 Quarterly Report (29 jul 2025), MATSA-tabel p. 4 en p. 14: concentraat 498.199 t, Ag 3.081 koz contained / 2.040 koz payable (FY25), FY26-raming 3,0 Moz. https://sfr.live.irmau.com/site/pdf/6a1972e0-01ae-4efb-8125-bb3cf4b194ae/June-2025-Quarterly-Report.pdf
[3] Interempresas, "MATSA impulsa un proyecto logístico en el Puerto de Huelva" (9-7-2013) — Onubaport Logistic, ampliación sur muelle Ingeniero Juan Gonzalo, ≈135.000 m². https://interempresas.net/Mineria/Articulos/140242-matsa-impulsa-un-proyecto-logistico-en-el-puerto-de-huelva.html
[4] Cadena de Suministro, "Matsa impulsa una nueva plataforma logística de concentrado de mineral en el puerto de Huelva" (3-7-2013). https://www.cadenadesuministro.es/noticias/matsa-impulsa-una-nueva-plataforma-logistica-de-concentrado-de-mineral-en-el-puerto-de-huelva_1072293_102.html
[5] TR Construya, "Nave de almacenamiento en el Puerto de Huelva" — Impala Terminals Huelva (grupo MATSA), "nave de almacenamiento sur", 28.000 m², afronding eind april 2016. https://trconstruya.es/nave-almacenamiento-puerto-huelva/
[6] eleconomista Empresite, Impala Terminals Huelva SL (ex Onubaport Logistic), "Muelle Ingeniero Juan Gonzalo, Puerto Exterior", centro logístico de concentrados. https://empresite.eleconomista.es/ONUBAPORT-LOGISTIC.html
[7] Wikipedia (es), "Minas de Aguas Teñidas" — concentrado de cobre met bestemming Atlantic Copper. https://es.wikipedia.org/wiki/Minas_de_Aguas_Teñidas
[8] Atlantic Copper, "Materias primas" — concentraat per schip en over de weg uit Huelva, ontvangst in Puerto de Huelva. https://atlantic-copper.es/como-lo-hacemos/materias-primas/
[9] Atlantic Copper, "Complejo Metalúrgico" — 60 ha, 330 kt anode, 285 kt kathode. https://atlantic-copper.es/como-lo-hacemos/complejo-metalurgico/
[10] Atlantic Copper, "Metales preciosos" — anodeslijmen (Ag typisch 8,5%) naar gespecialiseerde raffinaderijen. https://atlantic-copper.es/que-hacemos/metales-preciosos/
[11] Wikipedia (es), "Puerto de Huelva" — Puerto Exterior, Muelle Ingeniero Juan Gonzalo (1972–75). https://es.wikipedia.org/wiki/Puerto_de_Huelva
[12] OpenStreetMap (ODbL) via Nominatim — "Minas de Aguas Teñidas" 37.77316/-6.85318; "Atlantic Copper, Huelva" 37.22867/-6.94823. https://www.openstreetmap.org
[13] OSRM-demoserver over OpenStreetMap (alleen corridordiagnose, geen geometriebron) — plant → terminal 94,2 km, terminal → smelter 11,9 km. https://router.project-osrm.org
[14] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-zilver-matsa-huelva-plant2.png` (z16), `-terminal.png` (z17), `-kade.png` (z15), `-smelter.png` (z15).

## 9 · Gebakken
**Gebakken (2026-10-29, lichte werkwijze, M31 golf 11).** `v2/data/stroomroute-zilver-matsa-huelva.json`, 31,4 KB, contract versie 2, lonlat. Recept: functie `bak_zilver_matsa_huelva` in `v2/tools/bak_stromen.sh`, profielen `zilver-matsa-huelva-matsa-terminal` en `zilver-matsa-huelva-terminal-smelter` in `v2/tools/maak_stroombeen_weg.py` (extract `spanje`, `wegscan_puur.py`).

| # | modaliteit | been | km gemeten | km brief | naad |
|---|---|---|---|---|---|
| 1 | truck | MATSA-concentrator -> Impala-terminal Huelva | 94,6 (weg 94,4) | ~90 (Sandfire), OSM-pad 94,2 | - |
| 2 | truck | Impala-terminal -> Atlantic Copper (aannemelijk: een bron) | 12,7 (weg 12,3) | hemelsbreed 10,5, OSM-pad 11,9, geen wegkm | 0,00 km |

Totaal 107,3 km, 3 markers (de drie ankers uit §3, alle 0,000 km van hun lijn), geen stippel, geen zee-, haven-aanloop-, spoor-, leiding- of luchtbeen, geen kopie.

- **b1**: +4,9% tegen de ~90 km van Sandfire (binnen +-15%) en +0,4% tegen het OSM-pad van 94,2 km; alle acht via-snaps <= 0,06 km. Eerste scan gaf 135,4 km (+50%): HU-5101 is `tertiary` en lag voor het grootste deel > 12 km van de ankers, waardoor de scan het knooppunt met de A-496 (ways 88066040 en 914314667, een gat van 0,2 km) niet kende en 83,7 km omreed via het oosten. Opgelost met `corridorKlassen: ["tertiary"]` in het profiel (de bedoelde knop), geen via-punt bijgeschoven; herscan 94,4 km.
- **b2**: loopt de eerste 7,5 km over de b1-staart (N-442) terug, zoals de brief al vermeldde. Zonder `trimStaart` eindigde de lijn met een overschiet van 0,6 km voorbij de smelter (TERUGLOOP 157 m); met `trimStaart` weg, 12,9 -> 12,3 km. Het anker ligt 0,32 km van de dichtstbijzijnde weg (smelterterrein), als rechte ankerverbinding gerapporteerd.
- **Toetsen**: `toets_knikken.py` 0 terugloop; twee omkeringen van 180/160 graden (R 0-7 m) op het N-442-via-punt (37.19585,-6.92525): het punt snapt op een stompje van ca. 30 m en de lijn gaat daar en terug. Cosmetisch, niet bijgeschoven (de brief legde dit via-punt op OSRM-manoeuvre). `toets_rechte_benen.py --min-km 5`: geen recht been.
- **Lessen**: (1) een `tertiary`-corridor (HU-5101) hoort in `corridorKlassen`, anders hangt de weg los zodra hij verder dan 12 km van de ankers ligt; (2) `trimStaart` ook op het tweede been als het anker op privaat terrein ligt.
- **Open (ongewijzigd)**: afnemers/zeebeen van MATSA-concentraten niet gepubliceerd en dus niet getekend; b2 aannemelijk (een bron); terminal niet 1-op-1 bevestigd; zilver-sitelaag en v1 kennen MATSA niet (ca. 96 t Ag/j contained).
