# Routebrief (licht) · koper — Las Bambas → Matarani → Tongling

**stroom-id:** `koper-lasbambas-matarani` · **geschreven:** 2026-09-24 · **werkwijze:** licht (M29) · **status:** concept
**Keten in één zin:** koperconcentraat van de Las Bambas-concentrator (MMG, Challhuahuacho, Apurímac) per **truck** over de *corredor minero del sur* (PE-3SF → PE-3SY → PE-3SG → PE-34E/34J → PE-34A) naar het overslagstation **Pillones**, per **spoor** (PeruRail, Ferrocarril del Sur via Arequipa) naar de Tisur-concentraatkade **Muelle F** in Matarani, per **zeeschip** naar de Yangtze-monding, en van daar over het **gedeelde Chinese been** van `koper-collahuasi-tongling` (b3, oostgeul) naar de TNMG-kade in Tongling — daar stopt deze brief.
**Welke as van het verhaal:** Andes-concentraat naar Chinese smelters. Las Bambas 2025: **410.834 t koper in concentraat** (+27%, top-10 kopermijn) [1][2]; 125 beladen trucks/dag à 34 t over de corridor [4][5]; offtake voor de hele mijnlevensduur bij China Minmetals Non-Ferrous (CMN) [3].

## 1 · Ketenkaart
```
Las Bambas concentrator ──(b1 truck · corredor minero del sur · ~450 km)──► Pillones (truck→spoor)
  `cu-lasbambas-laad`                                                        `cu-pillones-overslag`
──(b2 spoor · Ferrocarril del Sur, Pillones–Arequipa–Matarani · ~285 km)──► Matarani Muelle F  `cu-matarani-kade`
──(b3 zee · MARNET)──► Yangtze-monding (31.42704, 121.47618)
══ samenvloeiing §1b: vanaf hier = `koper-collahuasi-tongling-b3` (binnenvaart ~550 km, oostgeul) ══► Tongling-kade TNMG
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Las Bambas concentrator → Pillones | corredor minero del sur: PE-3SF (Challhuahuacho–Quehuira–Pte. Ichuray) → **PE-3SY** (Mara–Pte. Sayhua–Ccapacmarca–Yavi Yavi–Velille) → PE-3SG (Velille–Morocacce–Yauri) → PE-34E/34J (Yauri–Negro Mayo–Oscollo–Imata) → PE-34A (Imata–Pillones) [5][8][14] | **~450** [4][6]; 435 [16]; declared corridor Progreso→Pillones 482,2 [7]; oude bake 411,5 [6] | `maak_stroombeen_weg` — profiel `cu-lasbambas-pillones` bestaat al (refs PE-3SF/3SY/3SG/3SW/34E/34J/34A, AP-945, CU-126/138) [6] | nee; plant ↔ PE-3SF ≈ 5–6 km mijnweg → kleine wegklassen ≤ 12 km, anders "last mile (geen net)" |
| b2 | A | spoor | Pillones → Matarani Muelle F | Ferrocarril del Sur (PeruRail): Pillones–Sumbay–Yura–Arequipa–La Joya–Matarani [10] | ~285 (730 totaal [4] − ~450) · 295 [16] | `toets_spoorroute.mjs --van=-15.9842,-71.2184 --naar=-17.0044,-72.1124` | nee; spooruiteinde in de haven 0,5–1,7 km van de kade = naad, geen stippel |
| b3 | B | zee | Matarani Muelle F → Yangtze-monding | — | MARNET meet | MARNET `zee\|…\|-17.0044,-72.1124\|31.42704,121.47618` | aanloop: waarschijnlijk ja (MARNET-korrel W-kust Z-Amerika; Peru: 0 havens met varend AIS) |
| b4 | C | binnenvaart | Yangtze-monding → Tongling-kade | **gedeeld been** = `koper-collahuasi-tongling-b3` (oostgeul) | ~550 rivier-km | hergebruik — niet opnieuw bakken | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-lasbambas-laad` | mijn / laadplek | Las Bambas concentrator (Bechtel-plant), Challhuahuacho | -14.0894, -72.3357 | [1][6][9] | bron-gelegd (z15 gezien: verwerkingscomplex met verdikkers en maalgebouwen, tailings-/waterbekken oostelijk; de corridor-startvertex van de oude bake ligt 5,8 km zuidelijker op PE-3SF) |
| `cu-pillones-overslag` | overslag truck→spoor | Estación de Transferencia Pillones, San Antonio de Chuca (Caylloma) | -15.9842, -71.2184 | [4][5][10] | bron-gelegd (z15 gezien: langgerekte gesloten overslagloods met spoorlus tussen PE-34A en de spoorlijn; OSM-station "Pillones" 250 m NO) |
| `cu-matarani-kade` | overslag spoor→zee | Tisur Muelle F, shiploader-pier, Matarani | -17.0044, -72.1124 | [11][12] | bron-gelegd (z16 gezien: bulkcarrier aan de shiploaderpier, trestle/gesloten band naar de wal, drie gesloten concentraatloodsen ZO; kruis verschoven vanuit het havenbekken -16.9975, -72.1075) |
| `cu-yangtze-monding` | samenvloeiing | Yangtze-monding (bestaand anker) | 31.42704, 121.47618 | §1 werkwijze | bestaand — hergebruikt |
| `cu-tongling-kade` | losplek / smelter | TNMG-kade Tongling (bestaand anker) | 30.98656, 117.7718 | §1 werkwijze | bestaand — hergebruikt |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
*b1: vertices van de gemeten corridor (OSM-vertices, 10 m simplify), telkens ~3 km ná de afslag (regel 2026-08-05), nooit een dorpscentrum.*
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | PE-3SF ná Challhuahuacho, richting Quehuira | -14.1014, -72.2319 | keuze PE-3SF (Quehuira–Pte. Ichuray) i.p.v. PE-3SG zuid via Haquira–Santo Tomás — dat was het EIA-2011-tracé [5] |
| b1 | 2 | Mara (PE-3SY) | -14.0876, -72.1042 | vanaf Pte. Ichuray op PE-3SY; sluit de wegen via Tambobamba uit; blokkadeplek 2022 [13] |
| b1 | 3 | Ccapacmarca (PE-3SY, na Pte. Sayhua) | -14.0059, -71.9957 | corridor blijft PE-3SY, niet CU-138 richting Colquemarca-dorp |
| b1 | 4 | Yavi Yavi (district Colquemarca) | -14.1927, -71.9620 | PE-3SY Muyuorco–Yavi Yavi–Tiendayoc–Huincho [8]; blokkade 2018/19 |
| b1 | 5 | PE-3SG oost van Velille | -14.5101, -71.8590 | ná de samenkomst PE-3SY/PE-3SG: oost naar Yauri, niet west naar Santo Tomás |
| b1 | 6 | PE-34E zuid van Yauri | -14.8222, -71.4165 | afslag zuid (Dv. Tintaya–Negro Mayo), niet PE-3SG NO naar Héctor Tejada/Ayaviri |
| b1 | 7 | Condoroma (PE-34J/34E) | -15.3000, -71.1384 | de enige weg Negro Mayo–Oscollo–Dv. Imata door Condoroma [14]; niet west via Callalli/Sibayo |
| b1 | 8 | PE-34A zuidwest van Imata | -15.8436, -71.1063 | ná de aansluiting op PE-34A: west naar Pillones, niet oost naar Juliaca |
| b2 | — | geen via nodig | — | enige aftakking = Matarani/Mollendo (eigen spoorlaag: knoop -17.0006, -72.0641); wordt door het eindpunt afgedwongen |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| TNMG-smeltercomplex Tongling (金冠 + 金新) — **verwijzing** naar `koper-collahuasi-tongling` §2/§6 | Tongling Nonferrous | concentraat → kathode | 760 + 500 kt/a | die brief |

Geen bron koppelt Las Bambas-concentraat aan een specifieke smelter: de CMN-offtake [3] zegt "Chinese smelters", niet welke. Getekend naar Tongling als gedeeld been (§1b); zie open punt 1.

## 6 · Stoppunt
Bij de Tongling-kade: vanaf de Yangtze-monding is de keten identiek aan Collahuasi→Tongling (fase C–E staan daar uitgeschreven), en een eigen smelter-streng voor Las Bambas zou zonder bron een verzinsel zijn.

## 7 · Open punten
1. **Smelter niet gedocumenteerd** — Tongling is een aanname uit de samenvloeiing; wordt een bron gevonden (MMG-verkoopcijfers per klant), dan hoort die hier.
2. **Gepubliceerde km lopen uiteen per definitie**: truck 435 / 450 / 482,2 (Progreso→Pillones, declared corridor), spoor 285 / 295 — geen primaire fetchbare bron voor het spoorgetal. Bake-toets ±15% tegen 450 resp. 285.
3. **Last mile plant → PE-3SF** (5–6 km mijnweg): OSM-dekking niet gecontroleerd — Overpass was op 2026-09-24 op drie spiegels onbereikbaar.
4. **Spooruiteinde in de haven**: eigen spoorlaag eindigt op -17.0049, -72.0964 (vermoedelijk de Muelle F-spoorontvangst) en -17.0019, -72.1080 (oude haven); naad naar de kade 0,5–1,7 km, onder de 5 km-grens.
5. **MARNET-aanloop Matarani** verwacht; `maak_havenaanloop.py` als het zeebeen niet tot de kade reikt.
6. **Tisur wil het mineraalembarkement verplaatsen/uitbreiden** [15] — het kade-anker kan over een paar jaar verschuiven.
7. **Volumes**: t concentraat (i.p.v. t Cu) niet gevonden; 125 trucks/dag is het EIA-cijfer van 2018 [5], actuele vloot onbekend.
8. **PE-3SY vs PE-3SG**: het EIA-2011-tracé liep via Haquira–Santo Tomás (zo ook de CooperAcción-kaart [7]); de 2e MEIA [5] en RM 054-2019 [8] leggen de trucks op Mara–Ccapacmarca–Velille — dát is getekend; geen negatief anker (lichte werkwijze).

## 8 · Bronnen
[1] MMG, Las Bambas operations page — "In 2025 we reached a production of 410,834 tonnes…"; "transported by road in trucks with closed containers to the transfer station… by rail to the port of Matarani" — https://www.mmg.com/operations/las-bambas/
[2] MMG, 2025 Fourth Quarter Production Report teleconference (2026-01) — https://www.mmg.com/content/uploads/2026/01/MMG-2025-Fourth-Quarter-Production-Report-Teleconference-Transcript.pdf · Annual Results 2025 — https://www.mmg.com/content/uploads/2026/03/MMG_AnnualResults2025_v5_ENG.pdf
[3] MMG, Las Bambas VSA circular (2014) — offtake met CMN voor de hele mijnlevensduur — https://www.mmg.com/wp-content/uploads/attachments/e_2014-04-14_Las_Bambas_VSA.pdf
[4] ProActivo, 2020-01-20 — 730 km tot Matarani, "125 camiones diariamente… sistema bimodal" — https://proactivo.com.pe/las-bambas-transporte-de-minerales-y-avances-en-corredor-vial-sur/
[5] CooperAcción / A. Leyva, 2018, Informe legal carretera Las Bambas — 2e MEIA-route (PE-3SF, AP-115, CU-138, …, PE-3SG, CU-834/835, PE-34E, PE-34J, PE-34), "125 camiones cargados por día", 34 t lading, "Pillones hasta el Puerto de Matarani… por un tercero (PerúRail)" — https://cooperaccion.org.pe/wp-content/uploads/2018/08/Libro-Carretera-Las-Bambas.pdf
[6] projectcorridor `cu-lasbambas-pillones` — `v2/tools/fetch_landnet.py` (gepubliceerdKm 450, 7 via) + `v2/build-cache/landnet_weg.geojson` (411,5 km, 499 vertices)
[7] CooperAcción, 2018, kaart Corredor Vial D.S. 037-2018-PCM — "PE-3S X (Dist. Progreso) hasta… PE-34 A (Estación Pillones)… 482.20 km" — https://cooperaccion.org.pe/wp-content/uploads/2018/05/MAPA-DEL-CORREDOR-VIAL-EN-ESTADO-DE-EMERGENCIA.pdf
[8] RM 054-2019-MTC/01.02, derecho de vía PE-3SW/PE-3SY — trayectoria Emp. PE-3SF (Pte. Ichuray)–Mara–Pte. Sayhua–Ccapacmarca–Muyuorco–Yavi Yavi–Tiendayoc–Huincho–Velille — https://busquedas.elperuano.pe/normaslegales/establecen-derecho-de-via-de-las-rutas-nacionales-pe-3sw-y-p-resolucion-ministerial-no-054-2019-mtc0102-1737278-2/ · PE-3SG — https://es.wikipedia.org/wiki/Ruta_nacional_PE-3S_G
[9] Bechtel, Las Bambas copper concentrator — https://www.bechtel.com/projects/las-bambas-copper-concentrator/
[10] PeruRail Cargo, red operativa — Centro de Transferencia Pillones; Matarani–Mollendo–Arequipa–Juliaca — https://www.perurail.com/es/cargo/red-operativa/
[11] Rumbo Minero, Muelle F Matarani — 3 almacenes (Las Bambas 100.000 t), shiploader 2.000 t/h, fajas vanaf de spoorontvangst — https://www.rumbominero.com/revista/informes/muelle-f-del-puerto-de-matarani-hito-historico-en-infraestructura-minera/
[12] Gestión, Tisur US$ 232 mln Muelle F (Cerro Verde, Antapaccay, Las Bambas) — https://gestion.pe/economia/empresas/tisur-invirtio-us-232-millones-nuevo-muelle-f-puerto-matarani-124754-noticia/
[13] RPP, 2022 — pobladores de Mara bloquean el corredor minero ("donde actualmente se transporta el mineral") — https://rpp.pe/peru/apurimac/las-bambas-pobladores-de-mara-bloquean-el-corredor-minero-como-protesta-contra-la-minera-y-el-mtc-noticia-1413305
[14] Cesel, carretera Yauri–Negromayo–Imata — "Dv. Imata – Oscollo – Negromayo… the only road that crosses… San Antonio de Chuca and Calalli (Caylloma) and Condorama (Espinar)" — https://www.cesel.com.pe/en/proyectos/carretera-yauri-negromayo-imata/
[15] Rumbo Minero — Tisur planea ampliar y reubicar el embarque de minerales — https://www.rumbominero.com/peru/noticias/mineria/puerto-de-matarani-tisur-planea-ampliar-y-reubicar-el-embarque-de-minerales/
[16] `v2/design/wegcorridors.md` §4 (completeness-agent 2026-07-22): "435 km weg (+ 295 km spoor naar Matarani)"
Satellietblik (Esri live, 2026-09-24): `v2/build-cache/satcheck/sat-lb-concentrator.png` (z15) · `sat-lb-pillones.png` (z15) · `sat-lb-matarani.png` (z15, kruis in het bekken) · `sat-lb-matarani-muelleF.png` (z16, kruis op de pier) · `sat-lb-matarani-spoor.png` (z16, spoorontvangst/loodsen).


## 9 · Gebakken (2026-09-25. lichte werkwijze)

**Stroom `koper-lasbambas-tongling`** → `v2/data/stroomroute-koper-lasbambas-tongling.json` — 7 benen. 19.421 km. 5 markers: truck 438 km · spoor (stippel) 5 km · spoor 284 km · zee (stippel) 72 km · zee 18.106 km · binnenvaart 516 km.
Recept: `bak_stromen.sh` (functie voor deze stroom). Toelichting: wegbeen 437.6 km (−2.8% t.o.v. ~450; profiel `koper-lasbambas-pillones`. via de Mara-route). spoor 284.3 km (`toets_spoorroute.mjs`; de spoorlus van Pillones en de havensporen van Matarani zitten niet in het net → stippels van 3.4 en 1.7 km). haven-aanloop Matarani 72.1 km (stippel). zeebeen MARNET; het Chinese deel is het gedeelde been met Collahuasi→Tongling (letterlijke kopie van dat been 5).
