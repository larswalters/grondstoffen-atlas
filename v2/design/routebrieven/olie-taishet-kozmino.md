# Routebrief (licht) · olie — Taishet (Irkutsk) → Skovorodino (Amur) → Kozmino-terminal (Primorje, Rusland)

**stroom-id:** `olie-taishet-kozmino` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** Russische ESPO-ruwe-olie per **leiding** — de Transneft-hoofdleiding Eastern Siberia–Pacific Ocean (ВСТО) van het
Taishet-knooppunt (ESPO-1 begin) noordelijk om het Baikalmeer via Ust-Kut, Lensk, Olekminsk en Aldan naar Skovorodino, daar ESPO-2 langs
Svobodny, Birobidzhan, Khabarovsk, Lesozavodsk en Nachodka naar Perevoznaya, en een korte stippel naar de Kozmino-kade; 4.735 km, zonder zee.
**Welke as van het verhaal:** *de ontbrekende landader onder Kozmino → Dalian* — `olie-kozmino-dalian` begint op dezelfde kade; deze stroom
laat zien waar die ESPO-olie vandaan komt. **~970 kb/d** (Kozmino-laadplan juli 2025: 4 Mt/mnd) [4]; ontwerpcapaciteit van de leiding 1.000
kb/d (2016) tot 1.600 kb/d (2025) [1]; peiljaar 2025. De ESPO-1 Taishet–Skovorodino draagt óók de China-aftakking (Skovorodino–Mohe–Daqing,
~600 kb/d ontwerp) [1], dus het Kozmino-volume is een deel van wat door het Taishet-been gaat; een apart leidingdebiet per been is niet gevonden.

## 1 · Ketenkaart
```
Taishet-knooppunt `ol-taishet-nps` (ESPO-1 begin, Irkutsk; Transneft)
  ──(b1 leiding · ESPO-1 ВСТО via Ust-Kut → Lensk → Olekminsk → Aldan → Tynda-regio · 2.679,7 km OSM, 15 ways, naden 0 m)──►
Skovorodino-knoop `ol-skovorodino-knoop` (splitsing ESPO-1/ESPO-2; China-spur niet getekend)
  ──(b2 leiding · ESPO-2 ВСТО via Svobodny → Birobidzhan → Khabarovsk → Lesozavodsk → Nachodka-regio · 2.042,9 km OSM, 9 ways)──►
Perevoznaya-tankenpark `ol-perevoznaya-tankenpark` (einde OSM-leiding)
  ──(b3 leiding STIPPEL · OSM mist het stuk naar de terminal · ~12,2 km hemelsbreed)──► Kozmino-kade `ol-kozmino-kade` ── stoppunt
```
Elk been is aaneengesloten OSM-`man_made=pipeline` (`substance=oil`, `name=ВСТО`, Транснефть), gestikt op gedeelde OSM-nodes. De kade is hetzelfde
punt als de kop van `olie-kozmino-dalian`: beide stromen lichten daar samen op. Kozmino is sanctiegevoelig (jan-2025 handel tijdelijk bevroren) [5][6]; geen route-impact.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `ol-taishet-nps` → `ol-skovorodino-knoop` | ESPO-1 (ВСТО, Транснефть) Taishet → Ust-Kut → Lensk → Aldan → Skovorodino | 2.679,7 OSM tegen **2.757 gepubliceerd (−2,8%)** [1][7] | OSM-ways 290897778, 290891540, 290891539, 290891538, 291166093, 290820311, 291194263, 290912026, 290912027, 506714839, 506714841, 361384623, 290912028, 271667289, 226953167 | nee |
| b2 | A | leiding | `ol-skovorodino-knoop` → `ol-perevoznaya-tankenpark` | ESPO-2 (ВСТО) Skovorodino → Svobodny → Khabarovsk-regio → Lesozavodsk → Nachodka | 2.042,9 OSM tegen **2.100 gepubliceerd (−2,7%)** [1][7] | OSM-ways 174814639, 142436390, 1035963742, 238838736, 1035963741, 578805782, 578805780, 578805781, 238914784 | nee |
| b3 | A | leiding | `ol-perevoznaya-tankenpark` → `ol-kozmino-kade` | terreinleiding naar de terminal (ESPO-2 eindstuk) | ~12,2 **hemelsbreed, geen leidingkm** | `--stippel "leiding|…"` | **ja — OSM mist dit stuk** |

Geen leg B/C/D/E: de pijp eindigt bij de Kozmino-kade; de zeeleg is `olie-kozmino-dalian` (geen kopie, geen tweede versie). Niet getekend: de
Komsomolsk-aftakking (292 km, óók ВСТО-getagd), de China-aftakking Skovorodino–Mohe (71 km Russisch deel) en andere ВСТО-ways naast de keten.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-taishet-nps` | kop van de keten (ESPO-1 begin) | Taishet-pompstation en tankenpark (Transneft), Irkutsk — OSM-beginknoop van way 290897778 | 55.8896, 98.0346 | [1][7][8] | bron-gelegd (z15 gezien: omheind tankenpark met 9 grote tanks en pompgebouwen, het punt ligt aan de noordrand van het terrein; leidingstrook/zandweg loopt vanuit het noorden naar binnen) |
| `ol-skovorodino-knoop` | splitsing ESPO-1 → ESPO-2 | Skovorodino-knoop (Amur) — gedeelde OSM-node van way 226953167 en 174814639 | 53.9471, 124.2622 | [1][7][8] | aannemelijk (z15 gezien: punt ligt op een bosweg-kruising; het Skovorodino-pompstation met ~12 tanks ligt ~0,9 km WNW, dus binnen 2 km, geen stippel; het punt zelf is leiding, geen site) |
| `ol-perevoznaya-tankenpark` | einde OSM-leiding / pompstation | Perevoznaya (Primorje) — OSM-eindknoop van way 238914784 | 42.8068, 133.0972 | [1][7][8][10] | bron-gelegd (z15 gezien: Transneft-pompstation met tankenpark en bundel van spoor en weg ten westen, het punt ligt 0,1–0,3 km ten oosten van de tanks; OSM kent hier `industrial=oil` Транснефть en tanks met `content=oil`) |
| `ol-kozmino-kade` | losplek / laadkade | Kozmino-exportterminal (Transneft, ESPO-terminus), Nachodka-baai | 42.7185, 133.0090 | [2][9][11] | **hergebruik letterlijk** uit `olie-kozmino-dalian` §3 (bron-gelegd daar, z17: pier met SPM aan de kop, tanker langszij); hier bevestigd z14: pier bij 133.003–133.01 en tankenpark ~1,5 km ZO bij 42.708/133.022 |

## 4 · Via-punten (leiding: geen corridorkeuze — de keten staat vast in way-volgorde, geen vrij kortste pad)
Een vrij kortste-pad-stik zou op de Komsomolsk- en China-aftakking en op parallelle ВСТО-ways kunnen afbuigen; de way-volgorde in §2 is daarom expliciet. Way-overgangen
(allemaal gedeelde node, naad 0 m): b1 op 56.0003, 99.4730 · 56.2682, 100.6738 · 56.4497, 101.5507 · 56.5273, 101.8489 · 56.5169, 102.8618 · 56.3837, 103.9544 ·
56.7074, 104.5707 · 60.6676, 116.3732 (1.221 km-way vanaf hier tot Skovorodino); b2 op 48.9907, 130.9139 · 48.6991, 134.4592 · 48.9578, 135.2071 ·
46.6749, 134.2942 · 45.7535, 133.7464 · 44.3192, 132.7382. Corridor-controle (afstand van de lijn tot de plaats): Ust-Kut 4,9 km · Lensk 12,0 · Olekminsk 12,5 ·
Aldan 6,5 · Tynda 9,2 · Svobodny 16,6 · Birobidzhan 3,3 · Khabarovsk 20,5 · Lesozavodsk 14,8 · Spassk-Dalny 12,1 · Nachodka 12,1; Ussuriysk 55,9 (niet op de lijn).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| ESPO-pijplijn (32 pompstations, 13 met tankenparken) | Transneft | Omsk–Irkutsk-leiding + Oost-Siberische velden → ruwe olie | ontwerp 1.000 kb/d (2016) tot 1.600 kb/d (2025); tankenparken samen 2,67 mln m³ | [1] |
| Skovorodino-pompstation | Transneft | splitsing: ESPO-2 naar Kozmino + China-spur naar Mohe/Daqing | China-spur ~600 kb/d ontwerp | [1] |
| Kozmino-terminal | Transneft | ESPO-leiding → tanker | tankenpark 350.000 m³; ~970 kb/d laadplan juli 2025 | [1][4] |

## 6 · Stoppunt
De brief stopt bij de Kozmino-kade: de pijp eindigt daar, de zeeleg staat al in `olie-kozmino-dalian` en de bestemmingen (China, India) zijn per lading verschillend; fase D/E bestaat niet.

## 7 · Open punten
- **b3 is stippel**: OSM kent het stuk Perevoznaya → Kozmino-terminal niet (11,8–12,2 km); de echte leiding loopt naar het terminal-tankenpark bij 42.708/133.022 en dan naar de pier, de stippel is schematisch.
- **Volume per been** niet gevonden: alleen Kozmino-ladingen (4 Mt in juli 2025 [4]; 41 schepen dec-2024 als record [5]); het ontwerp citeerde 925 kb/d dec-2023 uit [4], maar die pagina geeft juli 2025 (~970 kb/d), dus 925 is niet bevestigd.
- **Km-toets**: 2.679,7 en 2.042,9 zijn OSM-som tegen de Wikipedia-etappelengtes (−2,8% / −2,7%); er is geen operatorlengte per been geopend (Transneft-site [3] niet doorzocht).
- **Skovorodino-marker is een leidingknoop**, niet het pompstation (0,9 km WNW); `ol-taishet-nps` ligt 0,2–0,3 km boven de tanks (einde van de OSM-leiding) — geen procesgat.
- **Sitelaag** (`olie-sitelaag.json`): `w-kozmino` staat op 42.7309/133.0273 (Wikipedia-punt, ~2,0 km van de kade) en Taishet/Skovorodino ontbreken; centraal gelijktrekken.
- **Ways zonder name/operator** (226953167, 290912028, 361384623, 506714841): wel `substance=oil`, aaneengesloten op gedeelde nodes en binnen −2,8% van de gepubliceerde lengte; geen parallelle ВСТО-streng gevonden.
- Eerste claim van het ontwerp "naad ~170 m bij Lensk" bestaat niet: de ways sluiten op gedeelde nodes (0 m).
- Pyosmium is geblokkeerd en Overpass was onbereikbaar; de geometrie komt per way-id uit de OSM-API (zie §8 [7]).

## 8 · Bronnen
[1] Wikipedia, "Eastern Siberia–Pacific Ocean oil pipeline" — route Taishet–Skovorodino (2.757 km, etappe 1), Skovorodino–Kozmino (2.100 km, etappe 2 sinds 25-12-2012), capaciteit, 32 pompstations, China-spur. https://en.wikipedia.org/wiki/Eastern_Siberia%E2%80%93Pacific_Ocean_oil_pipeline
[2] Wikipedia, "Port Kozmino" — terminus ESPO sinds eind 2012, terminal geopend 28-12-2009, Nachodka-baai. https://en.wikipedia.org/wiki/Port_Kozmino
[3] Transneft, officiële site (niet doorzocht). https://www.transneft.ru/en/
[4] OilPrice.com, 25-6-2025 — Kozmino-ladingen juli 2025 ~4 Mt = ~970.000 vaten/dag, +7,5% t.o.v. juni, overwegend China. https://oilprice.com/Latest-Energy-News/World-News/Russia-to-Boost-Exports-of-Chinas-Favorite-Russian-Crude-in-July.html
[5] S&P Global, 2-1-2025 — ESPO-Blend-laadbeurten dec-2024 record (41 schepen), 1 lading naar India (alleen zoekresultaat gelezen, pagina gaf 403). https://www.spglobal.com/commodity-insights/en/news-research/latest-news/crude-oil/010225-russian-espo-blend-crude-loadings-rise-mom-in-dec-to-record-high-1-shipment-to-india
[6] Bloomberg, 22-1-2025, "Oil Tankers Reroute to Russian Pacific Port Hobbled by Sanctions" (alleen titel uit zoekresultaat). https://www.bloomberg.com/news/articles/2025-01-22/oil-tankers-reroute-to-russian-pacific-port-hobbled-by-sanctions
[7] OpenStreetMap (ODbL) via api.openstreetmap.org — way- en node-geometrie van de 24 ways, gemeten 2026-10-09; Taishet-keten teruggelopen via `node/<id>/ways`; km 2.679,7 en 2.042,9. https://www.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-olie-taishet-kozmino-{taishet-tankenpark,skovorodino,perevoznaya}.png`.
[9] Routebrief `olie-kozmino-dalian` §3 — anker `ol-kozmino-kade` 42.7185, 133.0090 (z17); ook Kozmino→China-aandelen (34 van 37 ladingen jan-2025). `v2/design/routebrieven/olie-kozmino-dalian.md`.
[10] OpenStreetMap map-API (bbox 133.00–133.12 / 42.70–42.82, 2026-10-09) — Transneft `industrial=oil` en `storage_tank content=oil` bij Perevoznaya (42.804–42.811 / 133.090–133.096) en Kozmino-tankenpark (42.708 / 133.022); geen `man_made=pipeline substance=oil` buiten way 238914784.
[11] Esri World Imagery z14 `v2/build-cache/satcheck/sat-olie-taishet-kozmino-kozmino-terminal.png` — pier en tankenpark Kozmino (één tegel ontbreekt in het beeld).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
`v2/data/stroomroute-olie-taishet-kozmino.json` (versie 2, lonlat, 59,5 KB) via `bash v2/tools/bak_stromen.sh olie-taishet-kozmino` (functie `bak_olie_taishet_kozmino`).
Titel: *Olie · Taishet (Irkutsk) → ESPO-leiding via Skovorodino en Perevoznaya → Kozmino-terminal (Primorje, Rusland)*. Totaal 4.734,8 km, 2.876 punten, 4 markers; het eindpunt is zoals het id belooft (Kozmino-kade).

| # | modaliteit | been | km | punten | naad | stippel |
|---|---|---|---|---|---|---|
| 1 | leiding | ESPO-1 Taishet → Skovorodino (Transneft, OSM-leiding) | 2.679,7 (gepubliceerd 2.757, −2,8%) | 1.598 | — | nee |
| 2 | leiding | ESPO-2 Skovorodino → Perevoznaya (Transneft, OSM-leiding) | 2.042,9 (gepubliceerd 2.100, −2,7%) | 1.276 | 0 m | nee |
| 3 | leiding | leiding Perevoznaya → Kozmino-terminal (schematisch, OSM mist dit stuk) | 12,2 hemelsbreed | 2 | 6 m | **ja** |

**Markers (4):** ol-taishet-nps 55.8896, 98.0346 · ol-skovorodino-knoop 53.9471, 124.2622 · ol-perevoznaya-tankenpark 42.8068, 133.0972 · ol-kozmino-kade 42.7185, 133.0090 (letterlijk uit `olie-kozmino-dalian`); allemaal ≤ 3 m van de lijn.

**Recept.** `python v2/tools/maak_leidingbeen_olie_taishet_kozmino.py --schrijf` haalt de 24 ways per id uit de OSM-API (cache `olie-taishet-kozmino-osmapi-cache.json`, gezaaid uit de brief-scan), stikt ze in de vaste way-volgorde van §2 op gedeelde nodes en schrijft `olie-taishet-kozmino-leiding-b1.geojson` en `-b2.geojson` (FeatureCollection, één LineString). Assertions op begin- en eindnode (2943913955 → 2794125345 → 2467291581) slagen; naad b1→b2 0,0 m. Daarna `--been-geojson` ×2 plus één `--stippel`.

**Toelichting stippel b3.** OSM kent het stuk Perevoznaya → Kozmino-terminal niet (§7); b3 is een rechte schematische lijn van het Perevoznaya-anker naar de kade, 12,2 km hemelsbreed, geen leidingkm. Geen zeeleg, haven-aanloop, vlucht of kopie: de zeeleg is `olie-kozmino-dalian`, dat op dezelfde kade begint.

**Toets (§5).** km binnen 15% (−2,8% / −2,7%); geen naad > 5 km (max 6 m); markers ≤ 3 m van hun lijn; `toets_knikken`: 186 knikken ≥ 60°, max 96,5°, 0 omkeringen, 0 terugloop (OSM-polylijn, geen routerfout; b1 63 en b2 123); `toets_rechte_benen`: alleen b3 (stippel, bedoeld). `json.load` slaagt, modaliteiten alle `leiding`, elk been ≥ 2 punten.

**Lessen.** (1) Voor een ВСТО-achtige hoofdleiding is een vaste way-lijst met node-stikken beter dan een vrij kortste pad: aftakkingen (Komsomolsk, China) blijven zo buiten de lijn. (2) De OSM-API (ways.json en nodes.json in batches van 100/700) volstaat zonder pyosmium of Overpass. (3) Ways zonder name/operator (226953167, 290912028, 361384623, 506714841) horen wel aaneengesloten bij de keten. (4) Sitelaag: `w-kozmino` staat 2 km van de kade en Taishet/Skovorodino ontbreken; centraal gelijktrekken.
