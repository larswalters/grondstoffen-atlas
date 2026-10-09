# Routebrief (licht) · Olie · Allen → Puerto Rosales (Argentinië)

**stroom-id:** `olie-allen-puertorosales` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**Keten in één zin:** Vaca Muerta-ruwe olie (Neuquén-schalie) gaat vanaf het Oldelval-pompstation Allen (Río Negro) per **leiding** (Oldelval Allen–Puerto Rosales,
L1 uit 1961, ± 513 km door Río Negro, La Pampa en Buenos Aires) naar het tankenpark van Oiltanking Ebytem bij Puerto Rosales (Bahía Blanca-estuarium); daar eindigt het bewijs.
**Welke as van het verhaal:** *Vaca Muerta bereikt de Atlantische kust* — **416 kb/d** gemiddeld Allen → Puerto Rosales in **2025** (66.139 m³/d), +27% op 2024 in de
totale Oldelval-doorzet; capaciteit na Duplicar 86.000 m³/d ≈ **541 kb/d** [1]. Argentinië exporteerde in 2025 ~230 kb/d ruwe olie (VS ~118, Chili ~90 kb/d) [2].

## 1 · Ketenkaart
```
Oldelval-pompstation Allen `ol-allen-station` (Río Negro, -38.9349/-67.6717)
   ──(b1 leiding · Oldelval Allen–Puerto Rosales L1 (OSM-way 1011117980) · 512,8 km OSM / 525 km Duplicar-lijn gepubliceerd · doorgetrokken)──►
Tankenpark Puerto Rosales `ol-rosales-tankpark` (Oiltanking Ebytem, Bahía Blanca, -38.9223/-62.0520) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Allen-station → Puerto Rosales-tankenpark | Oldelval Allen–Puerto Rosales L1 (1961); L2 (1969, way 1011117979) en de Duplicar-lijn (2025) liggen ernaast | 525 (Duplicar-lijn) [1]; OSM-way L1 512,8 km = −2,3% [4] | één OSM-way (`man_made=pipeline`, `substance=oil`, `location=underground`), 211 punten, max segment 36,2 km; FeatureCollection | nee |

Fase B (laadleidingen naar de monoboeien Punta Ancla / Punta Cigüeña, of naar de nieuwe steiger) wordt niet getekend: geen coördinaat en geen offshore-leiding in OSM (§7). Geen zeebeen, geen via-punten, geen last-mile.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-allen-station` | kop: pompstation / leidingbegin (aansluiting van de Neuquén-aanvoer) | Oldelval-station Allen | -38.9349, -67.6717 | [4][5][11] | bron-gelegd (z15 gezien: twee omheinde terreinen, noordoost met ± 10 witte ronde tanks en pompgebouwen, zuidwest een nieuwer station met twee donkere tanks; kruis ligt tussen beide op de leidingstrook met meerdere parallelle zandsporen die oost-zuidoost wegtrekken) |
| `ol-rosales-tankpark` | overslag leiding → tankopslag/zeeterminal (stoppunt) | Puerto Rosales-tankenpark (Oiltanking Ebytem) | -38.9223, -62.0520 | [4][6][7][11] | bron-gelegd (z15 gezien: groot tankenpark met ± 30 witte tanks aan de kust van het estuarium, kruis aan de noordwesthoek bij de pomp-/gebouwengroep; vanaf het park loopt een steiger van ± 2 km naar het zuidwesten met een tanker aan het eind) |

*Opmerking ankers.* Het OSM-leidingeind ligt op het tankenpark van **Oiltanking Ebytem (OTE)**, niet op een Oldelval-terrein: Oldelval vervoert, OTE slaat op en laadt [6][7]. De Wikipedia-coördinaat
van Puerto Rosales (-38.9236, -62.0729) is de civiele havensteiger 1,9 km westelijker [3] en wordt niet gebruikt. Nieuwe markers dus noemen: "Terminal Puerto Rosales (Oiltanking Ebytem)".

## 4 · Via-punten
Niet van toepassing: één doorlopende OSM-way, geen corridorkeuze (ondergrondse leiding, geen alternatief tracé).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Oldelval Allen–Puerto Rosales | Oldelval (Pampa Energía 2,1% direct; overige aandeelhouders niet in bron) | ruwe olie Neuquén → Puerto Rosales | 86.000 m³/d ≈ 541 kb/d (98.000 m³/d met DRA); doorzet 2025 416 kb/d | [1] |
| Terminal Puerto Rosales | Oiltanking Ebytem (OTE) | pijplijn → tankopslag → tanker | opslag 780.000 m³ (6 nieuwe tanks van 50.000 m³); steiger 2 posities Aframax/Suezmax, 20–25 schepen/maand | [6][7] |

## 6 · Stoppunt
De brief stopt bij het tankenpark van Puerto Rosales: de bestemming per lading (VS, Chili, Brazilië, Europa) is niet aan één lading of terminal te koppelen — alleen het nationale exportaggregaat is gebronnen [2] — en geen bron geeft een coördinaat van de monoboeien of de steigerposities.

## 7 · Open punten
- **Monoboeien Punta Ancla en Punta Cigüeña:** OTE-materiaal noemt ze (2.400 m³/u gezamenlijk) [8], maar er is geen coördinaat in OSM of bron en geen offshore-leiding in OSM → fase B vervalt. Begin 2025 waren beide buiten bedrijf na een lekkage/storing; de steiger (opgeleverd juni 2025) vervangt ze deels [6][7]. Het steigereind (≈ -38.9395, -62.0655, tanker zichtbaar op z15) is **niet** vastgelegd en niet getekend.
- **Puesto Hernández → Allen** (Duplicar Norte, 207 km Auca Mahuida → Allen, gelast, in aanbouw) staat niet in OSM [9]; de keten begint daarom bij Allen.
- **Welke fysieke buis:** OSM kent L1 en L2 (20 m uit elkaar, 512,8 resp. 513,0 km); de Duplicar-lijn (525 km) is niet apart gekarteerd. De lijn staat getekend op L1 als representatief tracé. De afwijking −2,3% tegen 525 is dus geen meetfout maar een andere buis.
- **Bestemming na de terminal niet gebronnen** (VS ~51%, Chili ~39% van de nationale export, indicatief [2]); geen zeebeen. De zeeknoop bij Bahía Blanca is niet gemeten (pas relevant bij een zeebeen: haven-aanloop).
- Zijtak Oldelval–Trafigura-raffinaderij Bahía Blanca (14", 11 km) [10] en de raffinaderij-aftakkingen (Plaza Huincul, Luján de Cuyo) niet getekend: andere stromen.
- **VMOS** (Vaca Muerta Oil Sur, naar Punta Colorada, Río Negro) draait nog niet volledig; hoort bij een eigen keten.
- **20-F zelf niet gelezen:** het jaarvolume komt van de Pampa Energía-IR-pagina met de 20-F-cijfers [1]; peiljaar 2025.

## 8 · Bronnen
[1] Pampa Energía IR, "Oleoductos del Valle (Oldelval)" (stand 31-12-2025) — Duplicar 525 km (Río Negro, La Pampa, Buenos Aires), capaciteit 86.000 m³/d (540.940 b/d), 98.000 m³/d met DRA, Allen → Puerto Rosales 66.139 m³/d (416.014 b/d) in 2025, nieuw terminalstation Puerto Rosales, Pampa 2,1%. https://ri.pampa.com/en/our-assets/oil-and-gas/midstream/oleoductos-del-valle-oldelval/
[2] DEF Online, "Vaca Muerta récord: cuáles son las cifras de las exportaciones de petróleo" (09-11-2025) — export gem. 230.000 b/d jan–sep 2025, VS ~118.000 b/d, Chili ~90.000 b/d via OTASA. https://defonline.com.ar/energia-mineria/vaca-muerta-record-cuales-son-las-cifras-de-las-exportaciones-de-petroleo-y-sus-principales-destinos/
[3] Wikipedia (es), "Puerto Rosales" — civiele haven Punta Alta, ruwe-olie-overslagterminal, coördinaat -38.9236/-62.0729. https://es.wikipedia.org/wiki/Puerto_Rosales
[4] OpenStreetMap (ODbL), way 1011117980 "Oleoducto Allen - Puerto Rosales L1" (`man_made=pipeline`, `substance=oil`, start_date 1961, v5), OSM-API 2026-10-09: 211 punten, 512,8 km, begin -38.93494/-67.67173, eind -38.92235/-62.05200. https://www.openstreetmap.org/way/1011117980
[5] OpenStreetMap (ODbL), way 1011117979 "… L2" (1969): 201 punten, 513,0 km, begin -38.93505/-67.67177, eind -38.92371/-62.05281. https://www.openstreetmap.org/way/1011117979
[6] LM Neuquén (MásE), Oiltanking-steiger bij Puerto Rosales (30-06-2025) — 2 posities Aframax/Suezmax, ± 2.000 m uit de kust, 780.000 m³ opslag, 20–25 schepen/maand, eerste lading Seaways Eagle 70.000 t. https://mase.lmneuquen.com/economia/la-nueva-terminal-oiltanking-ya-exporta-crudo-vaca-muerta-n1197523
[7] LM Neuquén, "las reformas Oiltanking Puerto Rosales exportar más petróleo" — zes tanks van 50.000 m³, 480.000 → 780.000 m³ (zoekresultaat-samenvatting, pagina niet geopend). https://mase.lmneuquen.com/petroleo/las-reformas-oiltanking-puerto-rosales-exportar-mas-petroleo-n1101121
[8] Oiltanking Ebytem (OTE), investeerderspresentatie — monoboeien Punta Ancla en Punta Cigüeña, 2.400 m³/u (zoekresultaat-samenvatting, pdf niet geopend). https://www.bancoprovincia.com.ar/CDN/Get/OTE_Presentacion
[9] Noticias NQN (22-09-2026), Duplicar Norte / akkoord Río Negro–Oldelval — 207 km Auca Mahuida → Allen (zoekresultaat-samenvatting). https://www.noticiasnqn.com.ar/amp/noticias/2026/09/22/353671-duplicar-norte-avanza-en-rio-negro-el-acuerdo-con-oldelval-para-ampliar-el-transporte-de-petroleo
[10] LM Neuquén, "Oldelval y Trafigura inauguraron el oleoducto de derivación a la refinería Bahía Blanca" (zoekresultaat-samenvatting). https://mase.lmneuquen.com/petroleo/oldelval-y-trafigura-inauguraron-el-oleoducto-derivacion-la-refineria-bahia-blanca-n1216558
[11] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15): `v2/build-cache/satcheck/sat-olie-allen-puertorosales-allen-kop.png`, `-allen-z14.png`, `-rosales-eind.png`, `-rosales-z14.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Resultaat:** `v2/data/stroomroute-olie-allen-puertorosales.json` (5,3 KB, contract versie 2, lonlat) · 1 been · **512,8 km** · 211 punten · 2 markers · geen stippel, geen naad.

| # | modaliteit | been | km | stippel |
|---|---|---|---|---|
| 1 | leiding | Oldelval Allen - Puerto Rosales L1 (OSM-way 1011117980) | 512,8 | nee (doorgetrokken) |

**Markers:** `ol-allen-station` (-38.9349, -67.6717) en `ol-rosales-tankpark` (-38.9223, -62.0520), 0,005 en 0,006 km van de lijn.
**Recept:** `bash v2/tools/bak_stromen.sh olie-allen-puertorosales` (functie `bak_olie_allen_puertorosales`). De geometrie komt uit `python v2/tools/maak_leidingbeen_olie_allen_puertorosales.py` (OSM-API: way 1011117980 plus nodes, FeatureCollection met één LineString; uitvoer `olie-allen-puertorosales-leiding-allen-rosales.geojson`). Geen weg-, spoor- of zeeprofiel nodig.
**Toets:** lengte 512,8 tegen 525 gepubliceerd = -2,3% (binnen ±15%; de brief geeft de Duplicar-lijn, de getekende L1 is een andere buis). Naden 0 km (één been). `toets_knikken` 0 knikken, 0 omkeringen; json.load ok (versie 2, lonlat, modaliteit leiding, 211 punten); bestand 5,3 KB.
**Leiding:** doorgetrokken omdat OSM de buis heeft (`man_made=pipeline`, `substance=oil`, `location=underground`, start_date 1961). L2 (way 1011117979) en de Duplicar-lijn liggen er 20 m naast en zijn niet apart getekend: L1 is het representatieve tracé.
**Niet getekend (zoals in de brief):** fase B (monoboeien Punta Ancla / Punta Ciguena, steiger) en elke zeeverbinding; geen haven-aanloop nodig (geen zeebeen), geen via-punten, geen last-mile.
**Lessen:** een leiding die als één OSM-way bestaat is met een kort API-script af (geen wegscan, geen slot nodig); het tankenpark is het stoppunt, de civiele steiger van Puerto Rosales ligt 1,9 km westelijker en is niet het anker.
