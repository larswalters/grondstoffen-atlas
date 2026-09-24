# Routebrief (licht) · koper — El Teniente → Rotterdam

**stroom-id:** `koper-elteniente-rotterdam` · **geschreven:** 2026-09-24 · **werkwijze:** licht (M29) · **status:** concept · **Linear:** LAR-560
**Keten in één zin:** El Teniente-erts wordt in de Colón-concentrator tot pulp verwerkt, gaat per **leiding** naar de filterplant/smelter **Caletones** (anodes), per **truck** over de Carretera del Cobre naar de spoor-overslag **ETEO/Los Lirios**, per **trein** (Fepasa) via Santiago en de tak San Pedro naar de **Ventanas-raffinaderij** in Puchuncaví (kathode 99,99%), per **truck** naar **Puerto San Antonio**, en per **containerschip door het Panamakanaal** naar **Rotterdam, RHB Waalhaven** — daarna de Rijn op zoals de Lobito-brief tekent.
**Welke as van het verhaal:** Chileense kathode naar Europa — **261.736 t in 2024** (13,8% van 1,894 Mt Chileense kathode-export; NL 40.412 t, IT 47.178, ES 39.290, DE 15.599); 2025: 207.738 t (NL 29.701 t) [20]. Ventanas-kathode gaat "naar Azië, Europa en de VS" [12].

## 1 · Ketenkaart
```
Colón-concentrator ──(b1 leiding · pulp · ~2 km)──► Caletones-smelter ──(b2 truck · H-25 + Ruta 5 · ±75 km)──► ETEO / Los Lirios
  ──(b3 spoor · Red Sur → Santiago → FCSV → tak San Pedro–Ventanas · ±265 km)──► Ventanas-raffinaderij
  ──(b4 truck · F-30-E → Ruta 68 → F-90 · 130 km)──► San Antonio, espigón ──(b5 zee · Panamakanaal · MARNET)──► Rotterdam, RHB Waalhaven
  ──(fase C: Rijn → Duisburg Becken A = been b3 van `koper-lobito-duisburg`, niet opnieuw getekend)──► Duisburg
```
Reëel alternatief (niet getekend): ±de helft van de Ventanas-kathode vertrok via **Valparaíso** (2017: 118.343 t Valparaíso / 110.044 t San Antonio) [17]; Caletones levert óók anodes aan Chuquicamata [1] — die streng valt buiten deze brief.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding (pulp) | Colón-concentrator → Caletones filterplant/smelter | pulpleiding naar espesador N°1 van de Planta de Filtros y Secado in Caletones [1][2] — de leiding zelf is in geen bron benoemd (aannemelijk: pulp kan niet per truck) | n.g.; hemelsbreed 2,1 km | OSM `man_made=pipeline` als hij gekarteerd is (niet geverifieerd, Overpass time-out), anders stippel "leiding" | ja, tenzij OSM-way |
| b2 | A | truck | Caletones → ETEO/Los Lirios | Ruta H-25 Carretera del Cobre (63 km Rancagua-Av. Millán → Caletones/Sewell) [11] + Ruta 5 zuid naar Los Lirios | n.g. als geheel; ±75 km afgeleid (H-25-deel ±55 + Ruta 5 ±15) | maak_stroombeen_weg | nee |
| b3 | A | spoor | ETEO/Los Lirios → Ventanas-raffinaderij | Fepasa: Red Sur (Los Lirios km 88,9) → Santiago → FCSV (Llay-Llay, La Calera) → San Pedro (km 48,8 v. Valparaíso) → Ramal San Pedro–Quintero, tak Ventanas [5][7][8][9][10] | n.g. als geheel; ±265 km afgeleid (88,9 + (187 − 48,8) + tak ≤ 39) | toets_spoorroute, via San Pedro | nee |
| b4 | A | truck | Ventanas-raffinaderij → San Antonio, espigón | F-30-E → Concón → Ruta 68 → F-90 (Casablanca) → G-98-F (Algarrobo) → San Antonio | **130 km** enkele reis (Codelco-pilot elektrische truck, vloot 25 trucks) [16] | maak_stroombeen_weg | nee |
| b5 | B | zee | San Antonio → Rotterdam RHB | **via Panamakanaal** — sanity-ankers Miraflores 8.9971, -79.5919 [21] en Gatún 9.2740, -79.9231 [22]; container (CMA CGM e.a.) [19] | n.g.; MARNET meet | MARNET | aanloop San Antonio: meten |
| — | C | binnenvaart | Rotterdam RHB → Duisburg Becken A | = `koper-lobito-duisburg` b3 (Rijn) [23] | 216 km | bestaand | nee |

## 3 · Ankers (één per site en per overslag; lat, lon)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-elteniente-concentrator` | mijn / concentrator (kop) | Concentrador Colón (indikkers), Machalí | -34.0900, -70.4630 | OSM Colón Alto -34.0869,-70.4528 / Colón Bajo -34.0896,-70.4749 [22]; Codelco [1] | bron-gelegd (z15 gezien: cluster ronde indikkers en hallen van de concentrator, 2 km N van Caletones; de mijn zelf is ondergronds, Teniente 8-spoor lost in de chancadores van Colón [2]) |
| `cu-caletones-smelter` | smelter (b1 los / b2 laad) | Fundición Caletones | -34.1061, -70.4503 | Wikipedia [3]; OSM "Planta Caletones" -34.1066,-70.4506 [22] | bron-gelegd (z15 gezien: smeltercomplex met hallen, tanks en schoorsteen op het kruis) |
| `cu-loslirios-overslag` | overslag truck → spoor | ETEO — Estación de Transferencia El Olivar / Planta de Transferencia Los Lirios | -34.2118, -70.7748 | Codelco 2025 (ETEO, comuna Olivar) [5]; Codelco 2011 + Wikipedia: transferstation Los Lirios, station -34.2274,-70.7848 km 88,9 [6][7] | onzeker (z15 gezien: spooremplacement met loodsen en apron 1,7 km NNO van station Los Lirios, radiaal gebouw ernaast = vermoedelijk Transap-werkplaats [7]; naam op het terrein niet bevestigd) |
| `cu-ventanas-raffinaderij` | raffinaderij (b3 los / b4 laad) | Codelco División Ventanas, Las Ventanas (Puchuncaví) | -32.7596, -71.4816 | OSM "Ex Fundición Ventanas" [22]; Wikipedia -32.7592,-71.4820 [14] | bron-gelegd (z15 gezien: Codelco-complex tussen kustweg F-30-E en kolenopslag, hallen en schoorstenen; de raffinagehal zelf niet apart aangewezen) |
| `cu-sanantonio-kade` | overslag truck → zee | Puerto San Antonio, espigón (Puerto Central / DP World, sitios 4–7 + C1–C2) | -33.5885, -71.6170 | Wikipedia Puerto de San Antonio [18]; Codelco-pilot [16]; historisch El Teniente-koper via TEM = huidige Puerto Central [24] | onzeker (z15 gezien: westkade van het espigón met kranen en apron; STI Molo Sur ligt 400 m W en is het alternatief — welke terminal de kathode laadt is niet gedocumenteerd) |
| `cu-rotterdam-kade` | overslag zee → binnenvaart | Rotterdam — RHB, Waalhaven Noordzijde 4 | 51.8935, 4.4585 | Lobito-brief [23] | hergebruikt, niet opnieuw gelegd |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Rancagua (Av. Millán → Ruta 5) | -34.1702, -70.7407 | H-25 eindigt in Rancagua; pint Ruta 5 zuid naar Los Lirios tegen secundaire wegen door Requínoa [11][22] |
| b3 | 2 | Estación San Pedro (Quillota) | -32.9379, -71.2763 | het aftakpunt van de Ramal San Pedro–Quintero uit de FCSV; zonder dit punt rijdt de router door naar Valparaíso [8][9] |
| b4 | 3 | Concón | -32.9220, -71.5160 | pint de kustweg F-30-E vanuit Puchuncaví tegen F-20/Ruta 5 landinwaarts [22] |
| b4 | 4 | Casablanca (Ruta 68 × F-90) | -33.3206, -71.4101 | pint Ruta 68 → F-90 tegen de kustweg Valparaíso–Quintay–Algarrobo [22] |
| b4 | 5 | Algarrobo | -33.3692, -71.6681 | F-90 komt hier aan de kust; pint G-98-F zuid naar San Antonio [22] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Fundición Caletones | Codelco, División El Teniente | droog concentraat (<9% vocht, uit de filterplant) → anodes 99,7% (+ RAF, zwavelzuur 2.800 t/d) | 1.360–1.400 kt concentraat/j → 400–435 kt anodekoper/j; El Teniente 459.817 t fijn Cu (2021); anodes voor Chuquicamata én Ventanas | [1][3][4][6] |
| ETEO / Los Lirios (overslag, geen verwerking) | Codelco (Fepasa rijdt) | truck → trein: 850 t anodes/d (5 trucks metaal, 30 zuur, 25 concentraat), sinds 2017 | ≈ 310 kt anodes/j naar Puerto Ventanas (Quintero) en San Antonio | [5] |
| Refinería Ventanas | Codelco, División Ventanas | anodes 99,7% (Caletones "principal proveedora"; ook Potrerillos, Chagres, Paipote) → kathode 99,99% | n.g. in primaire bron (open); smelter dicht 31-05-2023, raffinaderij draait door | [12][13][14][15] |

## 6 · Stoppunt
De brief stopt op de kade van RHB Waalhaven: fase C (Rijn naar Duisburg) is al gemeten als been b3 van `koper-lobito-duisburg` en één corridor hoort in één brief; een eigen fase D/E ontbreekt omdat geen bron déze Chileense kathode aan een benoemde fabriek koppelt.

## 7 · Open punten
- ETEO-anker: het emplacement is op satelliet gezien maar niet op naam bevestigd; Codelco zegt "Olivar" [5], Codelco 2011 en Wikipedia zeggen "Los Lirios" [6][7] — station en emplacement liggen 1,7 km uit elkaar op hetzelfde spoor.
- b1: OSM-kartering van de pulpleiding niet geverifieerd (Overpass time-outs); zonder way blijft het stippel "leiding".
- b3: precies eindpunt van de Ventanas-tak binnen het complex (snap-afstand meten bij de bake); Wikipedia noemt de tak "cobre refinado desde la Fundición de Ventanas" [8] — mogelijk gaat ook kathode per spoor weg, maar de gedocumenteerde uitvoer is per truck (2026) [16].
- b4/b5: welke terminal in San Antonio (DP World-espigón vs STI Molo Sur) laadt de kathodecontainers; Valparaíso als reëel alternatief (~50%) [17].
- Rail- en truck-km zijn afgeleid uit kilometreringen/deellengtes, niet als geheel gepubliceerd; de bake-uitvoer is de toets (±15%).
- Raffinagecapaciteit Ventanas (kt kathode/j) niet in een primaire bron gevonden.

## 8 · Bronnen
[1] Codelco — El camino del cobre (pulp → espesador N°1; anodes voor Chuquicamata en Ventanas; lotes naar San Antonio of Valparaíso) https://codelco.com/operaciones/el-camino-del-cobre
[2] Wikipedia (es) — Mina El Teniente (Teniente 8-spoor lost in chancadores Colón; concentraat naar filterplant Caletones) https://es.wikipedia.org/wiki/Mina_El_Teniente
[3] Wikipedia (en) — Fundición Caletones (34.1061°S 70.4503°W; 1.360–1.400 kt conc → 400–435 kt) https://en.wikipedia.org/wiki/Fundici%C3%B3n_Caletones
[4] Codelco — División El Teniente (54 km van Rancagua; 459.817 t fijn Cu 2021) https://codelco.com/operaciones/el-teniente/nosotros/division-el-teniente
[5] Codelco 2025 — ETEO, el corazón logístico en Olivar (850 t anodes/d, 60 trucks/d, Fepasa, sinds 2017, naar Puerto Ventanas (Quintero) en San Antonio) https://www.codelco.com/eteo-el-corazon-logistico-en-olivar-que-conecta-el-cobre-de-el-teniente
[6] Codelco 2011 — Transportando el ácido sulfúrico (trucks → estación de transferencia Los Lirios; trein → Barrancas/San Antonio) https://www.codelco.com/prontus_codelco/site/artic/20110217/pags/20110217211452.html
[7] Wikipedia (es) — Estación Los Lirios (-34.227416, -70.784845; km 88,9; Planta de Transferencia Codelco; Transap-werkplaats) https://es.wikipedia.org/wiki/Estaci%C3%B3n_Los_Lirios
[8] Wikipedia (es) — Estación San Pedro (-32.937917, -71.276337; km 48+843; ramal alleen Fepasa-vracht voor Ventanas-koper) https://es.wikipedia.org/wiki/Estaci%C3%B3n_San_Pedro_(Chile)
[9] Wikipedia (es) — Ramal San Pedro-Quintero (39 km; Ritoque–Quintero opgebroken; vracht sinds 1978) https://es.wikipedia.org/wiki/Ramal_San_Pedro-Quintero
[10] Wikipedia (es) — Ferrocarril Santiago-Valparaíso (187 km; Fepasa) https://es.wikipedia.org/wiki/Ferrocarril_Santiago-Valpara%C3%ADso
[11] Wikipedia (es) — Carretera del Cobre, Ruta H-25 (63 km, Rancagua → Caletones/Sewell, controlepost Maitenes) https://es.wikipedia.org/wiki/Carretera_del_Cobre
[12] El Observador 2024-09-16 — Codelco Ventanas: Caletones "nuestra principal proveedora" van anodes; kathode naar Azië/Europa/VS https://www.observador.cl/codelco-ventanas-expuso-sobre-cierre-de-fundicion-y-desafios-de-su-refineria-de-cobre/
[13] Cooperativa 2023-05-31 — Fundición Ventanas apagó sus hornos (raffinaderij draait door) https://cooperativa.cl/noticias/pais/region-de-valparaiso/ventanas/tras-58-anos-de-operacion-la-fundicion-ventanas-de-codelco-apago-sus/2023-05-31/140052.html
[14] Wikipedia (en) — Fundición Ventanas (-32.7592, -71.4820; elektrolytische raffinaderij niet geraakt door de sluiting) https://en.wikipedia.org/wiki/Fundici%C3%B3n_Ventanas
[15] Codelco — División Ventanas, Nosotros (Las Ventanas, Puchuncaví, 164 km van Santiago; havens Quintero/Valparaíso) https://www.codelco.com/operaciones/ventanas/nosotros/nosotros
[16] PortalPortuario 2026-07-06 — Codelco test elektrische truck Ventanas → Puerto San Antonio (±130 km enkele reis, 260 retour; vloot 25 trucks) https://portalportuario.cl/codelco-inicia-pruebas-con-camion-electrico-para-transportar-cobre-hacia-puerto-de-san-antonio/
[17] PortalPortuario 2017-02-13 — Ventanas-kathode: 118.343 t via Valparaíso, 110.044 t via San Antonio https://portalportuario.cl/la-apuesta-la-sustentabilidad-codelco-ventanas-la-exportacion-cuprifera/
[18] Wikipedia (es) — Puerto de San Antonio (sitios 1–3 STI, 4–7 + C1–C2 Puerto Central, 8 Panul; -33.594413, -71.620801) https://es.wikipedia.org/wiki/Puerto_de_San_Antonio
[19] Diario Financiero 2023-01-11 — Codelco-kathode in containers (CMA CGM) vanuit San Antonio https://www.df.cl/empresas/mineria/roban-cargamento-de-cobre-de-codelco-por-unos-us-4-4-millones-en-puerto
[20] Cochilco — Base de datos Anuario 2000–2025, Tabla 4.11 "Exportaciones de cobre refinado por destino según volumen" (t) https://www.cochilco.cl/web/download/1036/2026/16850/base-de-datos-anuario-de-estadisticas-cochilco-2000-2025.xlsx
[21] Wikipedia (en) — Miraflores Locks (8.99707611°N, 79.5918694°W) https://en.wikipedia.org/wiki/Miraflores_Locks
[22] OpenStreetMap via Nominatim/Overpass (ODbL) — Esclusas de Gatún 9.2739657,-79.9230683; Planta Caletones; Ex Fundición Ventanas; Colón Alto/Bajo; plaatsen Rancagua/Concón/Casablanca/Algarrobo https://nominatim.openstreetmap.org/
[23] Routebrief `koper-lobito-duisburg.md` — Rotterdam RHB 51.8935, 4.4585 en het Rijnbeen naar Duisburg Becken A (v2/design/routebrieven/koper-lobito-duisburg.md)
[24] MundoMaritimo 2003-10-06 — 13.812 t El Teniente-koper (anodes) via San Antonio, terminal TEM, naar Canada https://www.mundomaritimo.cl/noticias/en-el-puerto-de-san-antonio-se-embarcaron-mas-de-13800-toneladas-de-cobre


## 9 · Gebakken (2026-09-25. lichte werkwijze)

**Stroom `koper-elteniente-rotterdam`** → `v2/data/stroomroute-koper-elteniente-rotterdam.json` — 12 benen. 14.459 km. 6 markers: leiding (stippel) 2 km · truck 186 km · truck (stippel) 6 km · spoor (stippel) 1 km · spoor 270 km · zee (stippel) 80 km · zee 13.913 km.
Recept: `bak_stromen.sh` (functie `bak_koper_elteniente`). Toelichting: de Carretera del Cobre heeft in OSM twee gaten — Maitenes–Confluencia staat alleen als geplande weg (2.8 km) en bij Coya ligt 5.6 km H-27 als `track`. dat de scanner niet doorlaat — daarom drie gemeten wegstukken (18.5 + 4.6 + 19.6 km; profielen `koper-caletones-maitenes`. `koper-confluencia-coya`. `koper-coya-eteo`. met Codelco's privé-servicewegen toegelaten in de eindzone via `eindToegangPrivaat`) en twee stippels. Spoor ETEO → Ventanas 269.7 km (`toets_spoorroute.mjs` via San Pedro); truck Ventanas → San Antonio 143.8 km (+10% t.o.v. de 130 km van de Codelco-pilot — bevinding. binnen de lichte ±15%); haven-aanloop San Antonio 80.5 km (stippel; de dichtstbijzijnde MARNET-zeeknoop ligt op 74 km); zeebeen MARNET 13.913 km door het Panamakanaal (1.8 km van Gatún). Twee via-punt-lessen: een via-punt in het voetgangerscentrum van Rancagua snapt op een los stukje `unclassified` ("geen wegpad"); leg via-punten óp de doorgaande weg.
