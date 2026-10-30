# Routebrief (licht) · koper — Quebrada Blanca (QB2) → Puerto Patache (Chili)

**stroom-id:** `koper-quebradablanca-patache` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** koperconcentraat van de QB2-concentrator (Teck 60 %, Sumitomo 30 %, Codelco 10 %, ~4.400 m, Tarapacá) als slurry door één eigen **leiding** (~155 km gemeten, Teck: ~165 km) naar het QB2-havengebied bij Punta Patache aan de Pacifische kust; daar stopt de brief (geen bron voor schip of bestemming).
**Welke as van het verhaal:** *Noord-Chili, tweede eigen slurry-as naast Collahuasi* — QB2 draait sinds 2023 en levert 207,8 kt Cu in 2024 (Cochilco via en-Wikipedia [2]; Teck-tabel 208 kt 2024, 190 kt 2025 [1]). Eenheid kt Cu per jaar, peiljaar 2024.

## 1 · Ketenkaart
```
QB2-concentrator `cu-quebradablanca-concentrator`
  ──(b1 leiding · niet gekarteerd · ~21,5 km hemelsbreed, stippel)──► begin OSM-leiding (-21.0007, -69.0444)
  ──(b2 leiding · OSM-ways 1342279216 + 1302386276 + 1342279209 · 133,6 km, doorgetrokken)──► `cu-quebradablanca-haven` (QB2-haventerminal Patache)
  ── stoppunt (geen zeebeen: geen bron voor schip, haven van bestemming of afnemer)
```
Eigen verbinding zonder net (één product, twee punten). Naast de leiding ligt de QB2-zeewaterleiding in dezelfde corridor (Ausenco [8]); die wordt niet getekend.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding (slurry) | concentrator → begin OSM-leiding | slurryleiding westwaarts uit het QB-gebied, niet gekarteerd | hemelsbreed 21,5 km, geen leidingkm | `--stippel "leiding\|…"` | ja — net reikt niet (leiding niet in OSM) |
| b2 | A | leiding (slurry) | begin OSM-leiding → QB2-haventerminal | OSM `man_made=pipeline`, `substance=slurry`, `location=underground` | 133,6 gemeten; Teck totaal ~165 [1][7] | `--been-geojson "leiding\|…"` (3 ways gestikt) | nee — aannemelijk: QB2-toewijzing uit geometrie (zie §7) |

Totaal 155,1 km tegen 165 km Teck = −6,0 % (binnen ±15 %). Teck noemt in de 40-F ~165 km voor de gecombineerde concentraat- én waterleidingen [7]; de Teck-pagina schrijft 165 km voor de concentraatleiding [1]. De ±15 %-toets geldt als indicatie.
Geen haven-aanloop en geen zeebeen: er is geen zeebeen. Geen last-mile-beentje: het landbeen eindigt op het havenanker.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-quebradablanca-concentrator` | mijn / kop van de leiding | QB2-concentrator, ~3 km W van de dagbouw | -20.9925, -68.8375 | [1][2][10][11] | aannemelijk (z15 gezien: molengebouw met indikkers, stockpile-koepel en werkplaats W van de put; geen bron geeft het punt, terugval op het mijncoördinaat -21.0043, -68.8010 [2]) |
| `cu-quebradablanca-haven` | overslag leiding → (zee), stoppunt | QB2-haventerminal Patache = eind van OSM-leiding | -20.7850, -70.1828 | [5][6][11] | bron-gelegd (z15 gezien: havencomplex met gebouwen en schoorsteen aan de kust, een pier naar het W, afvalwaterbekkens O; punt ligt binnen OSM-landuse "Área Puerto Quebrada Blanca Fase 2", operator Teck [6]) |

Niet-anker: de **Collahuasi-steiger** -20.8027, -70.1989 (`cu-patache-kade`) is een andere terminal 2,5 km zuidelijker. De pier-kop ca. -20.7857, -70.1912 is op z15 zichtbaar, maar niet door een bron aan QB2 gebonden; geen anker, wel optioneel eindpunt als een bron hem benoemt. De pier die het ontwerp noemde (-20.7985, -70.1955) is de pier van de kolencentrale, niet van QB.

## 4 · Via-punten
Geen wegbeen, dus geen corridorkeuze. Knopen van de leiding (OSM-vertices, geen via-punten):
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b2 | 1 | begin way 1342279216 | -21.0007, -69.0444 | eind van de niet-gekarteerde stippel, naad 0 m [3] |
| b2 | 2 | junctie 1342279216 / 1302386276 | -20.8172, -69.6991 | ways delen deze knoop (76,9 + 52,5 km) [3][4] |
| b2 | 3 | kust bij Patache | -20.7689, -70.1585 | way 1302386276 eindigt, way 1342279209 begint [4][5] |
| b2 | 4 | eind way 1342279209 = haventerminal | -20.7850, -70.1828 | laatste 4,1 km door het havenvlak [5][6] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| QB2-concentrator | Teck (60 %), Sumitomo (30 %), Codelco (10 %) | erts → Cu-concentraat (slurry) | 207,8 kt Cu (2024); doel 285-315 kt Cu per jaar 2024-26 [9] | [1][2][9] |
| Patache-havenfaciliteit | Teck | slurry → ontwateren → concentraat op schepen | geen cijfer gevonden | [1][7] |

## 6 · Stoppunt
De brief stopt aan het QB2-havenvlak: Teck zegt alleen dat het concentraat "op schepen" naar de markt gaat [1], en Teck noemt geen afnemer of bestemming [7]; zonder bron voor haven van bestemming krijgt de keten geen zeebeen. Fase D en E vervallen.

## 7 · Open punten
- **QB2-toewijzing van de OSM-ways is aannemelijk, niet bewezen:** de ways hebben geen naam of operator. Way 1342279216 loopt tot 20 km van de Collahuasi-lijn weg en eindigt in het QB-gebied; way 1302386276 ligt 0,14-1,1 km naast de Collahuasi-lijn (mediaan 0,21 km), way 1342279209 eindigt binnen het Teck-havenvlak [6]. Geen punt valt binnen 50 m van de Collahuasi-lijn (way 847605767 en 1342279221 zijn Collahuasi, uitgesloten).
- Eerste ~21,5 km vanaf de concentrator niet gekarteerd: rechte stippel, werkelijke corridor kronkelt door het gebergte (indicatie).
- Havenanker: terminal niet onderscheiden van de pier; pier-kop is geen anker. Teck beschrijft de eigen offshore-werken pas voor Q1 2024 [7], het peiljaar-beeld kan ouder zijn.
- Geen bron voor schip, havenbestemming of afnemer van QB2-concentraat: bewust geen zeebeen.
- Teck-leidinglengte 165 km: de 40-F telt concentraat- plus waterleiding [7]; Ausenco noemt 160 km (fase 2-ontwerp, 2012) [8].
- Geen sitelaag-entry voor Quebrada Blanca in koper-sitelaag.json; melden aan de centrale stap.

## 8 · Bronnen
[1] Teck, Quebrada Blanca (60/30/10 %, ~165 km pijpleiding naar de haven, schepen naar de markt, 208 kt in 2024 en 190 kt in 2025). https://www.teck.com/operations/chile/operations/quebrada-blanca
[2] en-Wikipedia, Quebrada Blanca mine (21°0′15,63″S 68°48′3,48″W; 207,8 kt Cu in 2024, bron Cochilco-jaarboek). https://en.wikipedia.org/wiki/Quebrada_Blanca_mine
[3] OpenStreetMap way 1342279216 (pipeline, slurry, underground; 192 punten). https://www.openstreetmap.org/way/1342279216
[4] OpenStreetMap way 1302386276 (pipeline slurry, highway=track; 176 punten). https://www.openstreetmap.org/way/1302386276
[5] OpenStreetMap way 1342279209 (pipeline slurry; 7 punten, eind -20.7850, -70.1828). https://www.openstreetmap.org/way/1342279209
[6] OpenStreetMap way 1035848403 (Área Puerto Quebrada Blanca Fase 2, operator Teck; eindpunt van b2 binnen het polygoon). https://www.openstreetmap.org/way/1035848403
[7] Teck, Annual Information Form FY2023 (165 km concentraat- en waterleidingen; offshore-werken Q1 2024; concentraat overzee of binnenlands verkocht). https://www.sec.gov/Archives/edgar/data/886986/000088698624000003/a2023annualinformationform.htm
[8] Ausenco, Copper concentrate and seawater pipeline system (Punta Patache Norte; 160 km fase 2). https://ausenco.com/projects/copper-concentrate-and-seawater-pipeline-system/
[9] Energiminas, 2023-03-31 (eerste concentraat QB2; 285.000-315.000 t Cu per jaar 2024-26). https://energiminas.com/2023/03/31/teck-quebrada-blanca-fase-2-produjo-su-primer-concentrado-de-cobre
[10] OpenStreetMap via Overpass 2026-10-30: Rajo Quebrada Blanca (way 330489642, -21.0024, -68.8105), industrial way 1342279195 (-21.0015, -68.8372). https://www.openstreetmap.org
[11] Esri World Imagery via `v2/tools/sat_check.py` (z14-z15): `v2/build-cache/satcheck/sat-koper-quebradablanca-patache-conc.png`, `-conc15.png`, `-haven.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)

`bash v2/tools/bak_stromen.sh koper-quebradablanca-patache` → `v2/data/stroomroute-koper-quebradablanca-patache.json` (9,1 KB, versie 2, lonlat), 2 benen, 377 punten, 2 markers.

| # | modaliteit | km | punten | naad | stippel | opmerking |
|---|---|---|---|---|---|---|
| b1 | leiding | 21,5 | 2 | 0 | ja | slurryleiding concentrator → begin OSM-leiding, rechte lijn, net reikt niet (leiding niet in OSM) |
| b2 | leiding | 133,6 | 375 | 0,01 km | nee | 3 OSM-ways gestikt (1342279216 omgekeerd, 1302386276, 1342279209), doorgetrokken |
| | | **155,1** | | | | tegen Teck ~165 km: -6,0 % (indicatie: Teck telt concentraat- plus waterleiding) |

**Markers:** `cu-quebradablanca-concentrator` (-20.9925, -68.8375; 0 km van de lijn) en `cu-quebradablanca-haven` (-20.7850, -70.1828; 0,005 km van de lijn).

**Recept:** functie `bak_koper_quebradablanca_patache` in `v2/tools/bak_stromen.sh`: `--stippel "leiding|…|-20.9925,-68.8375|-21.0007,-69.0444"`, dan `--been-geojson "leiding|…|$BEEN/koper-quebradablanca-patache-leiding-qb2.geojson"`, twee `--marker`. Geen profiel in `maak_stroombeen_weg.py`, geen extract, geen zee, geen haven-aanloop, geen kopie, geen lucht.

**Toelichting per leidingbeen.** b1 is stippel (eigen verbinding zonder net): de eerste 21,5 km is niet gekarteerd, hemelsbreed, geen leidingkm; de werkelijke corridor kronkelt door het gebergte. b2 is doorgetrokken: OSM `man_made=pipeline`, `substance=slurry`; de QB2-toewijzing is aannemelijk (uit geometrie, zie §7), dat staat in de beennaam en niet in de lijnstijl. De naad tussen b1 en b2 is 6 m (afronding van het ankerpunt).

**Toets.** Geen naad > 5 km; geen zee-snap, dus geen haven-aanloop nodig; `toets_knikken`: 6 knikken >= 60 graden (spikes en krappe bochten van 46-947 m radius in de OSM-geometrie, o.a. 87,9 graden bij -20.7732, -70.1814 en spikes bij -20.9923, -69.0627), 0 omkeringen, 0 terugloop; `toets_rechte_benen`: alleen b1 (omwegfactor 1,000) en die is stippel met reden. De ±15 %-toets is alleen indicatief (geen wegbeen).

**Lessen.** (1) Een vooraf gebakken leiding-FeatureCollection met naden 0 m gaat zonder extra stap in `--been-geojson`; (2) het stroom-id noemt het werkelijke eindpunt (Puerto Patache = haventerminal), er is geen zeebeen; (3) de sitelaag heeft geen QB-entry, melden aan de centrale stap.
