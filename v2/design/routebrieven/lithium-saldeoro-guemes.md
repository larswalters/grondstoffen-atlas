# Routebrief (licht) · Lithium · Sal de Oro (Hombre Muerto) → San Antonio de los Cobres → Güemes (Argentinië)

**stroom-id:** `lithium-saldeoro-guemes` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** lithiumfosfaat (tussenproduct, uit pekel) van POSCO's Sal de Oro-operatie op het noordelijke deel van de Salar del Hombre Muerto (Salta/Catamarca) gaat — aannemelijk per **truck** — over de Puna-wegen en RN51 via San Antonio de los Cobres naar Salta en over RN9 naar POSCO's lithiumhydroxidefabriek in het Parque Industrial General Güemes (~422 km, OSM-gemeten, geen gepubliceerde wegkm). Geen zee, geen exportbeen: geen bron noemt de uitvoerroute van het hydroxide.
**Welke as van het verhaal:** de eerste commerciële lithiumhydroxidefabriek van Argentinië, geopend 24-10-2024: **25 kt LiOH/j nameplate ≈ 22 kt LCE/j** (×0,88; peiljaar 2024, nameplate, niet het gerealiseerde tempo) [2][3]; Sal de Oro zelf 48 kt LCE/j na fase II (Plant II, carbonaat, 23 kt LCE) [4].

## 1 · Ketenkaart
```
POSCO Sal de Oro-plant `li-saldeoro-plant` ──(b1 truck · plantweg → RP17/RP27 (Puna) → RN51 via San Antonio de los Cobres
  → Quebrada del Toro → Salta → RN9 · ~422 km OSM, hemelsbreed 224 km, aannemelijk)──► POSCO-hydroxidefabriek `li-guemes-fabriek`
  (Parque Industrial General Güemes) ⏹ stoppunt
```
Vertakking niet getekend: Plant II (carbonaat, op de salar) en de uitvoer van hydroxide (geen bron) [1][4].

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (fosfaat naar Güemes: aannemelijk, één bron; transportvorm niet genoemd) | `li-saldeoro-plant` → `li-guemes-fabriek` | plantweg → RP17/RP27 → RN51 (SAC–Salta) → RN9 | hemelsbreed 224 km, geen wegkm; OSM-meting 421,8 km (indicatie, geen norm) | maak_stroombeen_weg, extract argentina | nee |

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-saldeoro-plant` | mijn/plant (pekel → fosfaat) | POSCO Sal de Oro, noord Salar del Hombre Muerto | -25.2128, -66.9525 | [1][5][11] | onzeker (z16 gezien: blauw bedekt procesgebouw met vijvers, tanks en een landingsstrook ernaast, het enige plantachtige complex in het noorden; exploitant niet aan te wijzen, ligging niet door een bron bevestigd) |
| `li-guemes-fabriek` | fabriek (fosfaat → hydroxide) | POSCO Argentina LiOH-fabriek, Parque Industrial General Güemes | -24.7145, -65.0251 | [1][3][10][11] | aannemelijk (park door bronnen en OSM bevestigd, z16: ommuurd complex met blauwe daken in het zuidelijk deel; een tweede, ongeveer even groot complex ligt 400 m zuidelijker, -24.7180/-65.0218 — welk van de twee POSCO is, staat in geen bron) |

## 4 · Via-punten (b1)
Er is geen echte corridorkeuze: dit is de enige redelijke noordroute; de punten pinnen hem. Zuidroute via Antofagasta de la Sierra (San Antonio de los Cobres ligt daar 309 km vandaan [9]) en Belén/Tucumán is veel langer (niet gemeten). Alle punten snappen op 0,00–0,01 km.
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | RP17 NW van de plant | -25.1187, -67.0320 | verlaat de salar via de noordelijke Puna-weg i.p.v. een zuidroute naar Antofagasta de la Sierra |
| b1 | 2 | Puna-weg (RP27) | -24.3689, -66.9908 | pint de noordwaartse verbinding naar de RN51 |
| b1 | 3 | Puna-weg richting RN51 | -24.0968, -66.7899 | pint de aansluiting op de RN51 |
| b1 | 4 | RN51, zuidrand San Antonio de los Cobres | -24.2278, -66.3187 | RN51 km 156 vanaf Salta [8]; 1,2 km buiten het stadscentrum |
| b1 | 5 | RN51 Quebrada del Toro (Campo Quijano) | -24.8956, -65.6047 | pint de afdaling naar Salta |
| b1 | 6 | Salta oostrand (RN9/circunvalación) | -24.7952, -65.3670 | route om de binnenstad heen, naar RN9 |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Sal de Oro, plant 1 | POSCO Argentina | pekel → lithiumfosfaat | Sal de Oro 48 kt LCE/j na fase II | [1][4] |
| Güemes-fabriek | POSCO Argentina | fosfaat → LiOH (carbonaat/hydroxide) | 25 kt LiOH/j ≈ 22 kt LCE/j | [1][2][3] |

## 6 · Stoppunt
De brief stopt aan de poort in Güemes: de fabriek is zelf de conversieknoop en geen bron noemt een haven, spoor of afnemer voor het hydroxide (alleen "wereldmarkt"); fase D vervalt.

## 7 · Open punten
- **Transportvorm salar → Güemes** staat in geen bron (alleen: het fosfaat wordt "trasladado" [1][5]); truck is de aanname, de lijn is een OSM-route.
- **Geen wegkm gepubliceerd**: 421,8 km is OSM-afgeleid (indicatie, OSRM-controle 438); RN51 SAC–Salta 156 km [8] klopt grof met het gemeten stuk SAC → Campo Quijano (139 km) + Salta-oostrand.
- **Sal de Oro-plantanker onzeker**: meerdere vijvercomplexen in het noorden en zuiden van de salar; exploitant ontbreekt in de beelden.
- **Güemes-pand**: twee gelijkaardige complexen in het zuidpark; keuze aannemelijk, niet gebrond.
- **Volume**: 25 kt LiOH is nameplate; gerealiseerd tempo onbekend. **Exportroute hydroxide** (Chili of Buenos Aires) onbekend, dus geen vervolgbeen.
- Eerste ~210 km lopen over secundaire/onverharde Puna-wegen (OSM tertiary/unclassified/track).

## 8 · Bronnen
[1] El Economista, "Proyecto Sal de Oro" — plant Güemes, fosfaat uit het salar, 25 kt LiOH. https://eleconomista.com.ar/negocios/arranco-construccion-primera-planta-comercial-litio-salta-n51735
[2] Korea JoongAng Daily, 31-10-2024 — opening 24 oktober, 25.000 t LiOH/j, eerste fase van drie. https://www.koreajoongangdaily.com/business/posco-has-eye-on-supply-with-argentina-lithium-plant/11042951
[3] La Capital MdP, 26-10-2024 — Salta-regering: 25.000 t LiOH/j, Parque Industrial Güemes. https://www.lacapitalmdp.com/la-empresa-surcoreana-posco-inauguro-una-planta-de-hidroxido-de-litio-en-salta/
[4] Industrial Info (IIR) — Sal de Oro Plant II, 23 kt LCE, totaal 48 kt LCE/j. https://www.industrialinfo.com/news/article/poscos-sal-de-oro-lithium-plant-adds-to-argentinas-growing-production--363653
[5] Diario Panorama — fosfaat op de salar, trasladado naar Güemes; Plant II carbonaat in aanbouw. https://www.diariopanorama.com/noticia/499455/con-gran-expectativa-salta-inauguro-primera-fabrica-hidroxido-litio-pais
[6] Memo.com.ar, 26-10-2024 — CP1 voltooid, CP2 in La Puna, 25.000 t. https://www.memo.com.ar/economia/hidroxido-litio/
[7] Argentina.gob.ar, bericht 24-10-2024 — eerste commerciële LiOH-fabriek, Parque Industrial Güemes. https://www.argentina.gob.ar/node/446870
[8] Wikipedia (es), "Ruta Nacional 51 (Argentina)" — 283 km, San Antonio de los Cobres km 156. https://es.wikipedia.org/wiki/Ruta_Nacional_51_(Argentina)
[9] Wikipedia (es), "Antofagasta de la Sierra" — 309 km vanaf San Antonio de los Cobres. https://es.wikipedia.org/wiki/Antofagasta_de_la_Sierra
[10] OSM/Nominatim — Parque Industrial General Güemes -24.7035,-65.0331; Wikipedia (en) General Güemes -24.667,-65.05, Salar del Hombre Muerto -25.35,-67.07. https://www.openstreetmap.org
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15/z16): `v2/build-cache/satcheck/sat-lithium-saldeoro-guemes-` + `salar-noord`, `saldeoro-plant`, `plant-anker`, `guemes-park`, `guemes-fabriek`, `fabriek-anker` (.png).
[12] Geofabrik argentina-extract via `wegscan_puur.py`, profiel `lithium-saldeoro-guemes-saldeoro-guemes`: 421,8 km, 0 omkeringen.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)

**Recept:** `bash v2/tools/bak_stromen.sh lithium-saldeoro-guemes` (functie `bak_lithium_saldeoro_guemes`) → `v2/data/stroomroute-lithium-saldeoro-guemes.json` (118,8 KB, versie 2, lonlat).

| # | modaliteit | been | km | naad | stippel |
|---|---|---|---|---|---|
| b1 | truck | POSCO Sal de Oro → POSCO-hydroxidefabriek Güemes (plantweg → RP17/RP27 → RN51 via San Antonio de los Cobres → Salta → RN9; aannemelijk: transportvorm niet gebronnen) | 422,5 (5.545 punten) | n.v.t. | nee |

Totaal 422,5 km, 2 markers (`li-saldeoro-plant` onzeker, `li-guemes-fabriek` aannemelijk), beide op 0,0 km van de lijn.

- **Geometrie:** profiel `lithium-saldeoro-guemes-saldeoro-guemes` (maak_stroombeen_weg.py, bestond al uit de briefronde) via `wegscan_puur.py`, extract argentina; 421,8 km weg + stubs 0,44 km (plant) en 0,33 km (fabriek). Alle via-snaps 0,00–0,01 km, 0 omkeringen. Hergebruikt, niet opnieuw gescand.
- **Km-toets:** er is geen gepubliceerde wegkm. 422,5 km tegen de OSRM-indicatie 438 km = -3,5%; hemelsbreed 224 km (omwegfactor 1,89 door de Puna en de Quebrada del Toro). Dit is een indicatie, geen ±15%-norm.
- **Stippel / haven-aanloop / vlucht / leiding:** geen. Geen zee, geen kopie van een ander been; het stoppunt is de fabriekspoort (brief §6).
- **Knikken:** `toets_knikken.py` 17 knikken ≥ 60 gr, 0 omkeringen en 0 teruglopen (de scherpe punten zijn haarspeldbochten in de Quebrada del Toro en kruispunten bij San Antonio de los Cobres en Salta). `toets_rechte_benen.py` meldt geen recht been.
- **Les:** het wegprofiel uit de briefronde (corridorKlassen breed, eindKlassen met `track`) kon ongewijzigd gebakken worden; ~210 km van het been loopt over OSM-klassen tertiary/unclassified/track, wat de km-toets niet verstoort maar wel de rijdbaarheid in de Puna een aandachtspunt maakt.
- **Open (ongewijzigd uit §7):** transportvorm salar → Güemes niet gebronnen; plantanker onzeker; twee gelijke complexen in Güemes; 25 kt LiOH is nameplate; geen exportbeen voor het hydroxide.
