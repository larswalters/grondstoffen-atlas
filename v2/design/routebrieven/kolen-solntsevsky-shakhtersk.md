# Routebrief (licht) · kolen — Solntsevsky → Ugolny konveyer → Shakhtersk (Rusland)

**stroom-id:** `kolen-solntsevsky-shakhtersk` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** Thermische steenkool uit de Solntsevsky-dagbouw (Uglegorsk, Sachalin) gaat over de 23 km lange gesloten kolenband "Ugolny konveyer" (OSM `goods_conveyor`, doorgetrokken) naar het opslagterrein en de pier van de kolenzeehaven Shakhtersk (zelfde eigenaar, VGK/East Mining Company); de lijn stopt bij de scheepsbelader — geen bron noemt een afnemer of loshaven.
**Welke as van het verhaal:** Sachalin-export: de eerste kolenband naar zee in het Russische Verre Oosten. Volume: 15,2 Mt verkoopbaar in 2024 (GEM, mijn) [1]; ruim 10 Mt over de haven in 2022 [1]; bandcapaciteit 4.000 t/u, plan 20 Mt/j [3]. Eenheid Mt kolen per jaar.

## 1 · Ketenkaart
```
Solntsevsky-pit (niet op de lijn, 6 km) ··· bandbegin `kolen-solntsevsky-bandbegin`
  ──(b1 leiding/band · Ugolny konveyer · 22,5 km, 5 OSM-ways)──► bandeind opslagterrein Shakhtersk
  ──(b2 leiding · stippel over het opslagterrein · 0,3 km)──► pierband
  ──(b3 leiding/band · pier · 1,1 km, OSM-way)──► scheepsbelader `kolen-shakhtersk-kade` ⏹ stoppunt
     └── vertakking (niet getekend): zeeschip → Korea/Japan/China (algemeen, geen haven genoemd) [3]
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding (band) | bandbegin → bandeind | Ugolny konveyer (Угольный конвейер) | 22,5 eigen OSM-som tegen 23 km gepubliceerd [1][2][3] = −2,1% | OSM-ways 947629124, 1409824697, 1190064790, 947629125, 1409824707 gestikt, FeatureCollection | nee |
| b2 | A | leiding (band) | bandeind → pierband | band over het kolenopslagterrein | 0,3 (hemelsbreed) | `--stippel` (niet gekarteerd; belt kruist de kolenstapels) | ja: net reikt niet |
| b3 | A | leiding (band) | pierband → scheepsbelader | pierband (OSM way 1409824738) | 1,1 (OSM) [7] | OSM-way, FeatureCollection | nee |

Som 23,9 km tegen 23 km gepubliceerd = **+4,0%** (de 23 km is de hoofdband; b2+b3 zijn havenbanden [6]). Geen weg-, spoor- of zeebeen: geen via-punten, geen haven-aanloop.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-solntsevsky-bandbegin` | bandbegin / laadpunt | begin Ugolny konveyer, Solntsevsky-concessie | 48.9809, 142.1462 | [2][3][7] | bron-gelegd (z16 gezien: gesloten bandgalerij als lichte streep van NW naar de kruis aan het ZO-einde, naast de doorgaande weg; parallel een tweede langwerpig constructiedek) |
| `kolen-solntsevsky-pit` | mijn (alleen genoemd, geen anker op de lijn) | Solntsevsky open pit, Krasnopolye | 48.9331, 142.1863 | [1] | bron-gelegd (z14 gezien: grote terrasvormige dagbouw; 6,1 km ZO van het bandbegin) |
| `kolen-shakhtersk-kade` | overslag / scheepsbelader | pierkop kolenhaven Shakhtersk (Coal Seaport Shakhtersk) | 49.1632, 142.0538 | [5][6][7] | bron-gelegd (z17 gezien: dubbele bandgalerij op een pier naar de kop bij de golfbreker van stortsteen, kolenopslag en loodsen op de wal) |

Bandeind 49.1642, 142.0715 (OSM-eindknoop, z16 gezien: rand van het kolenopslagterrein met stapels en stacker-banen) is geen apart anker maar het naadpunt b1 → b2.

## 4 · Via-punten
Geen: alle drie de benen zijn leiding/band met OSM-geometrie of een korte stippel; geen corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kolenzeehaven Shakhtersk | Vostochnaya Gornorudnaya Kompaniya / East Mining Company | band → opslag (tot 3 Mt, geautomatiseerd) → scheepsbelader | plan 20 Mt/j; band 4.000 t/u; stacker-reclaimers 3 × 4.000 t/u gepland | [1][3][5] |

## 6 · Stoppunt
De brief stopt op de scheepsbelader van Shakhtersk: GEM en de pers noemen alleen Azië-Pacific (Korea, Japan, China) en Sachalin-GRES-centrales, geen afnemer of loshaven met naam, en Sojitz/Marubeni staan als samenwerkingspartners zonder bestemmingshaven [1][3][4]; dus geen zeebeen.

## 7 · Open punten
- Bandstart (februari 2026) en 4.000 t/u rusten op één persbericht [3]; GEM noemt nog Q3 2025 als geplande oplevering [1]. Geen officiële VGK-aankondiging gevonden.
- Het stuk band over het opslagterrein (0,3 km) en de parallelle pierband (way 1409824739) staan niet of dubbel in OSM; alleen way 1409824738 gebruikt.
- De pit ligt 6,1 km van het bandbegin; de verbinding (mijnweg/haulage) is niet getekend en geen last-mile-been.
- Geen eigen jaarcijfer voor de haven na 2022; 15,2 Mt (2024) is mijnproductie, niet havendoorzet.
- Beste kade-coördinaat is de pierkop; de exacte ligplaats (kadefront aan de ZO-zijde) is niet apart gelegd.

## 8 · Bronnen
[1] Global Energy Monitor, Solntsevsky Coal Mine — 48.933062, 142.186323; 15,2 Mt verkoopbaar 2024 (13,2 in 2023); band 23 km mijn → Shakhtersk; >10 Mt over de haven in 2022; Azië-Pacific + Sachalin-GRES. https://www.gem.wiki/Solntsevsky_Coal_Mine
[2] World Coal, "Vostochnaya Mining Co installs largest main coal conveyor belt in Russia" (09-08-2022) — 23 km, Solntsevsky → Shakhtersk, >70% staalconstructie klaar. https://www.worldcoal.com/handling/09082022/vostochnaya-mining-co-installs-largest-main-coal-conveyor-belt-in-russia/
[3] 1RU/www1.ru, "De langste band van Rusland is opgevoerd" (16-07-2026) — 23 km, start feb 2026, 4.000 t/u, plan 20 Mt/j, export Korea/Japan/China. https://www1.ru/en/news/2026/07/16/samyi-dlinnyi-konveier-v-rossii-razognali-do-predela-on-proizvodit-4-tysiaci-tonn-uglia-v-cas.html
[4] Wikipedia, East Mining Company — eigenaar, 23 km hoofdband, partners Sojitz (dec 2016) en Marubeni (sept 2017). https://en.wikipedia.org/wiki/East_Mining_Company
[5] World Coal, "Shakhtersk coal seaport awaits large-scale modernisation" (02-04-2021) — geautomatiseerd depot tot 3 Mt, drie stacker-reclaimers, nieuwe banen. https://www.worldcoal.com/coal/02042021/shakhtersk-coal-seaport-awaits-large-scale-modernisation/
[6] Dry Bulk Magazine, "Shakhtersk coal port adds extra 2.2 km to conveyor network" (29-06-2018) — havenbanden van opslag naar scheepsbeladers, 4,6 Mt 2017. https://www.drybulkmagazine.com/ports-terminals/29062018/shakhtersk-coal-port-adds-extra-22-km-to-conveyor-network/
[7] OpenStreetMap API (way/<id>/full) — ways 947629124, 1409824697, 1190064790, 947629125, 1409824707 (samen 22,516 km, naden 0–17,6 m) en 1409824738 (1,073 km); script `v2/tools/maak_leidingbeen_kolen_solntsevsky_shakhtersk.py`.
[8] Esri World Imagery via `v2/tools/sat_check.py` (z14–z17) — `v2/build-cache/satcheck/sat-kolen-solntsevsky-shakhtersk-*.png`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Bestand:** `v2/data/stroomroute-kolen-solntsevsky-shakhtersk.json` (3,4 KB, versie 2, punt_formaat lonlat, 124 punten, 2 markers). **Recept:** `bash v2/tools/bak_stromen.sh kolen-solntsevsky-shakhtersk` (functie `bak_kolen_solntsevsky_shakhtersk`); geojsons via `python v2/tools/maak_leidingbeen_kolen_solntsevsky_shakhtersk.py --schrijf --pier`.

| # | modaliteit | been | km | stippel |
|---|---|---|---|---|
| b1 | leiding | Ugolny konveyer, bandbegin naar bandeind (OSM, 5 ways, 116 punten) | 22,5 (gepubliceerd 23: -2,1%) | nee |
| b2 | leiding | band over kolenopslagterrein Shakhtersk (schematisch) | 0,3 | ja: niet in OSM, net reikt niet |
| b3 | leiding | pierband naar scheepsbelader (OSM way 1409824738, 6 punten) | 1,1 | nee |

Totaal 23,9 km tegen 23 km gepubliceerd (+4,0%; de 23 km is de hoofdband, b2 en b3 zijn havenbanden). Markers: Solntsevsky bandbegin (48,9809, 142,1462) en Shakhtersk pierkop scheepsbelader (49,1632, 142,0538); beide 0,003-0,004 km van de lijn. De pit (48,9331, 142,1863) is bewust geen marker (6,1 km van de lijn, kandidaat voor de sitelaag).

**Toelichting.** Alleen leiding/band: geen weg-, spoor- of zeebeen, geen via-punten, geen haven-aanloop, geen luchtbeen, geen letterlijke kopie. b2 is de enige stippel (het stuk band over de kolenstapels staat niet in OSM). Naden 0,004 en 0,005 km. Geen extract gebruikt.
**Toetsen.** toets_knikken: 0 omkeringen, 1 knik van 71 graden bij 49,1621, 142,0558 (de hoek van de OSM-pierband zelf, geen artefact). Km-toets: b1 -2,1% tegen de gepubliceerde 23 km (OSM-som, geen wegkm).
**Lessen.** Een OSM-goods_conveyor is bruikbaar als doorgetrokken leidingbeen; de geojsons waren al gestikt door het script van de brief-fase, dus de bake was één functie plus één run. De parallelle pierband (way 1409824739) is niet gebruikt om een dubbel beeld te vermijden.
