# Routebrief (licht) · koper — Chuquicamata → Mejillones → Tongling (China)

**stroom-id:** `koper-chuquicamata-tongling` (bestand `koper-chuquicamata-china.md`; Chinese eind gekozen: Tongling) · **geschreven:** 2026-09-24 · **werkwijze:** licht (M29) · **status:** concept · **Linear:** LAR-558
**Keten in één zin:** sulfide-concentraat uit de Chuquicamata-concentrator (Codelco, 15 km N van Calama) — het deel dat níet in de eigen flash-smelter op de site gaat — in **rotainers per FCAB-meterspoor** (~275 km: Chuquicamata-tak → Calama → Baquedano → Prat → ramal Mejillones) naar de **TGN-concentraatterminal** (Puerto Angamos, Complejo Portuario Mejillones), per **bulkcarrier** (~19.000 km, MARNET) naar de Yangtze-monding en over het **gedeelde binnenvaartbeen** (Collahuasi-brief b3) naar de TNMG-kade in Tongling.
**Welke as van het verhaal:** "Codelco-concentraat naar Chinese custom smelters". Chuquicamata: **289 ktmf (2024)** [1], 266 ktmf (2025) [2]; Codelco-breed was **34 % van de verkoop 2025 concentraat** op 1,276 Mt betaalbaar koper (≈ 430 kt Cu) [3]; de Chuqui-smelter draait ver onder zijn 180 t/u-nominaal (< 1 Mt concentraat/j) [4][5] — dát restant is de exportstreng. Het Chuqui-exportdeel zelf is niet gepubliceerd (§7).

## 1 · Ketenkaart
Chuquicamata-concentrator `cu-chuqui-laad` ──(b1 spoor · FCAB via Prat · ~275 km)──► TGN-pier Mejillones `cu-mejillones-kade`
──(b2 zee · MARNET · ~19.000 km)──► Yangtze-monding (31.42704, 121.47618) ──(b3 binnenvaart, GEDEELD `koper-collahuasi-tongling` b3 · 516,6 km)──► Tongling-kade (30.98656, 117.7718) → TNMG-smelter (fase C/D staan in de Collahuasi-brief)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `cu-chuqui-laad` (-22.3050, -68.9140) → `cu-mejillones-kade` (-23.0580, -70.3802); het net eindigt in de TGN-rotainer-yard **-23.0693, -70.3787** (routeerpunt staart, OSM way/84036321) | FCAB meterspoor: Chuquicamata-tak (9 km) → San Salvador km 253 → Calama km 238 → Baquedano km 96 → **Prat km 59** → ramal Mejillones | **~275** = 203 hoofdlijn + 69–77 ramal [11][12]; atlas-proefroute Calama→Mejillones 253 km [18] | toets_spoorroute (1-op-1; kop→Prat, Prat→yard) | nee — naad yard→pierkop 1,3 km (< 2 km) |
| b2 | B | zee | `cu-mejillones-kade` → Yangtze-monding 31.42704, 121.47618 | — | ~19.000 (atlas-maat Antofagasta→Shanghai 18.915, MARNET) | MARNET | aanloop: **waarschijnlijk ja** — bij Chili reikt MARNET niet tot de kade (Coloso-precedent 85 km stippel) |
| b3 | C | binnenvaart | Yangtze-monding → Tongling-kade 30.98656, 117.7718 | Yangtze, oostgeul Tongling | 516,6 (gebakken) | **gedeeld been = `koper-collahuasi-tongling` b3** — niet herhalen (§1b samenvloeiing) [17] | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-chuqui-laad` | mijn / laadplek | Chuquicamata-concentrator, FCAB-meterspoor langs de maalhallen (ZW van de pit) | -22.3050, -68.9140 | [2][7] + OSM ways 375832217 / 234178160 [16] | bron-gelegd (z15/z16 gezien: plantcomplex met lange maalhallen, indikkers en een bezinkbekken direct ten ZW van de pit; het spoor ligt per OSM langs de hallen — de rotainer-laadplek zelf is op z16 niet te onderscheiden) |
| `cu-mejillones-kade` | overslag spoor → zee | TGN-pier met shiploader, Puerto Angamos / Complejo Portuario Mejillones | -23.0580, -70.3802 | [7][8][9] + OSM pier way/741288513 [16] | bron-gelegd (z15/z16 gezien: ~700 m-pier NW de baai in, bulkcarrier langszij aan de kop; aan de wortel de rotainer-yard met het spooreinde) |
| Yangtze-monding · Tongling-kade | aanlanding · losplek | bestaande ankers, hergebruikt | 31.42704, 121.47618 · 30.98656, 117.7718 | [17] | gelegd in de Collahuasi-brief — niet opnieuw |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | **Prat** — empalme ramal Mejillones, km 59 van de hoofdlijn (OSM node/1290560415) | -23.4727, -70.1714 | de splitsing Mejillones (TGN) ↔ doorrijden naar Antofagasta (ATI) [11][12] |
| b1 | — | Baquedano (km 96) alleen als controle: kruising met Ferronor; geen alternatief richting Mejillones, dus geen via | -23.3338, -69.8408 | niet nodig, tenzij de router een Ferronor-omweg neemt |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Chuquicamata-smelter, op de site (registerpunt 22.3142 S, 68.8855 W — knoop, geen anker) | Codelco | concentraat → anode/blister; **verwerkt het meeste eigen concentraat**, de rest is deze exportstreng | flash-oven nominaal 180 t/u (≈ 1,4 Mt conc/j); feitelijk 70–80 t/u (2019) en < 1 Mt/j (2024) | [4][5][6] |
| TNMG-smeltercomplex Tongling (金冠铜业 / 金新铜业) | Tongling Nonferrous | concentraat → kathode → folie (fase C/D) | zie Collahuasi-brief | [17]; afnemer: [13][14] (aannemelijk) |

## 6 · Stoppunt
De brief stopt op de Tongling-kade: alles voorbij de aanlanding (oostgeul → kade → smelter → 铜冠铜箔-folie) is al getekend in `koper-collahuasi-tongling` (b3–b5); deze brief voegt alleen de Chileense kop (b1) en het zeebeen (b2) toe.

## 7 · Open punten
- **Afnemer:** geen primaire bron die Tongling (of Jiangxi Copper) als afnemer van *Chuquicamata*-concentraat noemt. Reuters 2023 bevestigt langetermijncontracten met Chinese smelters zonder namen en de overgang naar concentraat + blister/anode vanaf 2025 [13]; de enige naamgevende bron is een beleggersforum-post (Tongling, ~50 kt/j, gekoppeld aan El Teniente) [14]. Tongling is daarom **aannemelijk**; alternatief Beilun-losberth 29.9364, 121.883 → Guixi (Jiangxi Copper) staat als gedeeld been klaar in `koper-escondida-guixi`. Beennaam b2: `… (aannemelijk: één bron)`.
- **Volume:** het exportdeel van Chuquicamata-concentraat is niet gepubliceerd; de FCAB-toezegging van 2019 was ≥ 5 kt/maand [7], TGN kan 4 Mt/j [8]. Cochilco-anuario per divisie/product (Excel) niet geraadpleegd.
- **Laadplek:** de rotainer-laadplek op het Chuqui-terrein is op z16 niet te onderscheiden; het anker ligt op het OSM-spoor langs de concentratorhallen (site-niveau). De export ging historisch via de galpones van ATI/Antofagasta; ATI stopte met concentraatopslag [15] en de Codelco-trein rijdt sinds 2019 naar Mejillones [7] — een restvolume via ATI is niet uitgesloten.
- **Ramal-lengte:** 69 km [12] tegen ~77 km [11]; de ±15 %-toets van de bake dekt beide.
- **Zee-aanloop:** verwacht een haven-aanloop-stippel bij Mejillones (Chili-korrel van MARNET); meten bij de bake, niet dichttrekken.

## 8 · Bronnen
[1] Codelco, *Operational and Financial Report December 31, 2024* — Chuquicamata 248,5 → 289,0 ktmf. https://www.codelco.com/sites/site/docs/20240426/20240426181050/operational_and_financial_report_december_31_2024.pdf
[2] Codelco, *División Chuquicamata* — 266 ktmf (2025), 15 km N van Calama. https://www.codelco.com/chuquicamata
[3] La Tercera, 2026-03-01 — verkoopmix 2025: 51 % kathode, 34 % concentraat, 8 % anode/blister, 7 % calcine; 1,276 Mt. https://www.latercera.com/pulso/noticia/las-reservadas-cifras-con-las-que-la-actual-administracion-se-despide-de-codelco/
[4] Diario Financiero, 2019-07 — flash-oven 70–80 t/u tegen 180 t/u nominaal. https://www.df.cl/empresas/mineria/codelco-retrasa-plena-capacidad-de-fundicion-chuquicamata
[5] Sindicato Chuquicamata, 2024-07-17 — fundición verwerkt < 1 Mt/j; refinería 700 kt anoden. https://sindicatochuquicamata.cl/2024/07/17/codelco-no-tiene-perdon-de-que-no-este-procesando-sus-concentrados-de-forma-directa-la-gran-problematica-de-no-fundir-el-cobre-en-chile/
[6] Wikipedia, *Fundición Chuquicamata* — 22°18′51″S 68°53′08″W; capaciteit 1.400 kt/j. https://en.wikipedia.org/wiki/Fundici%C3%B3n_Chuquicamata
[7] FCAB, 2019-01-29 — bimodaal concentraattransport Codelco Chuquicamata → Puerto de Mejillones; 10 wagons × 2 rotainers × 26,4 t; ≥ 5 kt/maand. https://www.fcab.cl/2019/01/29/fcab-inicia-transporte-bimodal-de-concentrados-de-cobre-en-contenedores/
[8] MundoMaritimo, 2025-04-01 — TGN (filial Puerto Angamos) opent concentraatterminal, US$ 130 M, 4 Mt/j, shiploader, Codelco aanwezig. https://www.mundomaritimo.cl/noticias/puerto-angamos-tgn-inaugura-nuevo-terminal-para-el-embarque-de-concentrados-de-cobre-en-el-norte-de-chile
[9] PortalPortuario, 2024-11-20 — proefverscheping TGN: 10.800 t Codelco-calcine, Handymax, naar China; "los contenedores, que llegan por ferrocarril y camión". https://portalportuario.cl/terminal-graneles-del-norte-realiza-prueba-de-embarque-de-concentrado-de-cobre-ligada-a-proyecto-de-expansion/
[10] Reporte Minero, 2026-02 — Codelco Chuquicamata bezoekt Puerto Angamos; Área de Logística Internacional opereert in de haven. https://www.reporteminero.cl/noticia/noticias/2026/02/codelco-chuquicamata-visita-puerto-angamos-logistica-internacional-exportacion-cobre
[11] es.wikipedia, *Ferrocarril de Antofagasta a Bolivia* — km-tabel: Antofagasta 0 · O'Higgins 35 · **Prat 59 (empalme Mejillones, ~77 km)** · Baquedano 96 · Calama 238 · San Salvador 253 + ramal Chuquicamata 9 km. https://es.wikipedia.org/wiki/Ferrocarril_de_Antofagasta_a_Bolivia
[12] es.wikipedia, *Wikiproyecto Chile/Ferrocarriles — listado de ramales* — ramal Antofagasta–Mejillones 69 km. https://es.wikipedia.org/wiki/Wikiproyecto:Chile/Ferrocarriles/Listado_de_ramales_y_ferrocarriles
[13] Reuters via Mining.com, 2023-09-18 — Codelco beëindigt langetermijn-concentraatcontracten met Chinese klanten vanaf 2025; blister/anode erbij. https://www.mining.com/web/codelco-ends-long-term-mined-copper-deals-to-china-clients-from-2025-sources/
[14] Eastmoney-forumpost, 2025-09-04 (zwak) — Tongling ↔ Codelco El Teniente: "锁定部分铜精矿采购权，年约5万吨". https://caifuhao.eastmoney.com/news/20250904112012831960610
[15] Fundación Terram — ATI stopt concentraatopslag in galpones 4 en 5. https://www.terram.cl/antofagasta-terminal-internacional-galpones-no-seguiran-acopiando-cargamentos-mineros/
[16] OpenStreetMap (ODbL), via `v2/build-cache/raw1op1/chili.geojson` en Overpass: pier *Terminal de Graneles del Norte* way/741288513; station *Prat* node/1290560415; meterspoor door het Chuqui-complex ways 234178160 / 375832217; spoor-spur TGN way/84036321 (eind -23.06927, -70.37867).
[17] `v2/design/routebrieven/koper-collahuasi-tongling.md` — gedeeld been b3, ankers Yangtze-monding / Tongling-kade, verwerkingsknoop TNMG.
[18] atlas, `v2/build-cache/ais/graaf/spoorroute-proef-calama-mejillones.geojson` — proefroute 253 km over het gefilterde SA-net (toets_spoorroute).


## 9 · Gebakken (2026-09-25. lichte werkwijze)

**Stroom `koper-chuqui-tongling`** → `v2/data/stroomroute-koper-chuqui-tongling.json` — 7 benen. 19.856 km. 5 markers: spoor (stippel) 12 km · spoor 276 km · leiding (stippel) 1 km · zee (stippel) 136 km · zee 18.914 km · binnenvaart 516 km.
Recept: `bak_stromen.sh` (functie voor deze stroom). Toelichting: spoor 276.3 km (`toets_spoorroute.mjs`. Chuqui → Prat → Mejillones; gepubliceerd ~275); het mijnemplacement (9 km). de TGN-spur (2.9 km) en de band naar de pierkop (1.3 km) zitten niet in het net → stippels; haven-aanloop Mejillones 135.6 km (stippel); zeebeen MARNET 18.914 km; Chinese deel = gedeeld been met Collahuasi→Tongling.
