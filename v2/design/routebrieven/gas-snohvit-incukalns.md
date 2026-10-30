# Routebrief (licht) · gas — Snøhvit/Hammerfest LNG (Noorwegen) → Klaipėda → Inčukalns (Letland)

**stroom-id:** `gas-snohvit-incukalns` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) ·
**status:** gebakken
**Keten in één zin:** Snøhvit-veldgas gaat per 143 km onderzeese leiding naar Hammerfest LNG (Melkøya), wordt daar vloeibaar en vaart
als LNG langs de Noorse kust, door Skagerrak, Kattegat en de Grote Belt naar de FSRU Independence in Klaipėda; daar wordt het
geregasificeerd en gaat het door het Litouws-Latvische transmissienet naar de ondergrondse opslag Inčukalns (Conexus).
**Welke as van het verhaal:** Arctisch Noors LNG naar de Baltische ontkoppeling van Russisch gas. Volume: Equinor-contract 2015
540 mcm = 0,54 bcm/j [2], daarna verlaagd (hoogte niet gevonden); Latvenergo 2024–2026 6 ladingen ≈ 6 TWh ≈ 0,2 bcm/j [4]; Hammerfest-
exportcapaciteit 5,75 bcm/j [1]. Werkelijke 2024-stroom onbekend (§7). Indicatie 0,5 bcm/j, peiljaar 2015.

## 1 · Ketenkaart
```
Snøhvit-veld `gas-snohvit-veld` (subsea, 143 km NW van Hammerfest, Equinor)
  ──(b1 leiding · Snøhvit pipeline, 711 mm · 142,5 km OSM, gepubliceerd 160)──►
Hammerfest LNG-fabriek `gas-melkoya-plant` ─(0,5 km eigen terrein, procesgat)─ LNG-steiger `gas-melkoya-kade`
  ──(b2 zee · aanloop 11,7 km stippel · MARNET 2.386 + 63 + 738 km via echte Grote Belt · aanloop 7,6 km stippel)──►
Klaipėda FSRU Independence `gas-klaipeda-fsru`
  ──(b3 leiding · Litouws-Latvisch net via Šiauliai en Panevėžys · 413,1 km OSM-graafpad)──►
Inčukalns UGS `gas-incukalns-ugs` — stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-snohvit-veld` → `gas-melkoya-plant` | Snøhvit pipeline (OSM-ways 1118916982 80,6 km + 174753089 61,9 km; Equinor, substance=gas) | 142,5 OSM tegen 160 [1] (−11%); veldafstand 140 km NW van Hammerfest [1] | OSM-pipeline, vooraf gestikt (`maak_leidingbeen_gas_snohvit_incukalns.py`) | nee |
| b2a | B | zee | `gas-melkoya-kade` → zeeknoop 4043 (70.7897, 23.6009) | haven-aanloop Melkøya (kade 11,7 km van zeeknoop) | 11,7 | rechte stippel | ja: schematisch, 1:10M-kust kent de haven niet (maak_havenaanloop liep in de timeout) |
| b2b | B | zee | zeeknoop 4043 → MARNET-knoop 4504 (55.6000, 10.9000) | Noorse kust, Skagerrak, Kattegat | 2.386,4 MARNET | MARNET | nee |
| b2c | B | zee | knoop 4504 → knoop 6864 (55.0468, 11.0946) | Grote Belt | 62,7 MARNET | MARNET | nee |
| b2d | B | zee | knoop 6864 → zeeknoop 8873 (55.7256, 21.0828) | Baltische Zee langs Bornholm | 738,2 MARNET | MARNET | nee |
| b2e | B | zee | zeeknoop 8873 → `gas-klaipeda-fsru` | haven-aanloop Klaipėda (kade 7,6 km van zeeknoop) | 7,6 | rechte stippel | ja: schematisch, 1:10M-kust kent de haven niet |
| b3 | C | leiding | `gas-klaipeda-fsru` → `gas-incukalns-ugs` | Litouws-Latvisch transmissienet (13 onbenoemde OSM-ways); zie ook Klaipėda–Panevėžys en Riga–Panevėžys [2][7] | 413,1 OSM-graafpad; hemelsbreed 275,5 km, geen gepubliceerde lengte: indicatie, geen norm | OSM-graafpad over extracts litouwen + letland | nee |

Zee b2b–b2d samen 3.187,3 km (MARNET-bake, gemeten 2026-10-30); het ontwerp schatte 3.000–3.200 km. Hammerfest→Klaipėda is aannemelijk (één bron, §7):
zet in de beennaam "(aannemelijk: één bron)". **Grote Belt, niet Øresund:** de router kiest vanzelf Øresund (3.003 km); de drie zeebenen forceren
de Grote Belt via twee vaste MARNET-knopen (bindende ingreep van de haalbaarheidstoets).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-snohvit-veld` | veld (kop) | Snøhvit subsea-template | 71.5715, 21.2277 | [1][8] | aannemelijk (OSM-startknoop van way 1118916982; offshore, niet satelliet-controleerbaar) |
| `gas-melkoya-plant` | LNG-fabriek (b1-eind) | Hammerfest LNG, Melkøya | 70.6860, 23.5843 | [1][8] | bron-gelegd (z15 gezien: dichtbebouwd procesterrein van het eiland met drie grote LNG-tanks en procesblokken; OSM-leidingeinde ligt in de bebouwing) |
| `gas-melkoya-kade` | LNG-steiger (overslag) | Melkøya LNG-steiger | 70.6845, 23.5975 | [8] | bron-gelegd (z15 gezien: aanlegsteiger met platform, 0,5 km zuidoost van de tanks aan open water) |
| `gas-klaipeda-fsru` | FSRU (b2-eind, b3-kop) | FSRU Independence, Kiaulės Nugara-steiger | 55.6647, 21.1375 | [2][3][8] | bron-gelegd (z15 gezien: wit schip langs de steiger op het eiland Kiaulės Nugara in het Klaipėda-kanaal; OSM-leidingstart 55.6647, 21.1367 ligt 0,05 km westelijk) |
| `gas-incukalns-ugs` | ondergrondse opslag (staart, stoppunt) | Inčukalns UGS (Conexus), Vidzeme | 57.1690, 24.6968 | [6][9] | bron-gelegd (z15 gezien: afgebakend installatieterrein met lange hallen, rijen kleine objecten en blauwe daken in bos en akker; OSM-leidingeinde 57.1670, 24.6934 ligt 0,3 km zuidwest) |

Hergebruik: geen — Snøhvit, Melkøya, Klaipėda en Inčukalns staan niet in eerdere brieven, `data/gas.js` of `gas-sitelaag.json`.
Zeeknopen 4043 en 8873 zijn MARNET-knopen (afstand van de kade 11,7 resp. 7,6 km; beide > 5 km, dus haven-aanloop).

## 4 · Via-punten
Niet van toepassing: leiding (OSM-way, graafpad) en zee (MARNET); geen corridorkeuze op land door ons te leggen.
Dat het graafpad via Panevėžys loopt en niet via Pakruojis klopt met het net: Klaipėda–Panevėžys en Riga–Panevėžys zijn de bestaande lijnen en de grensovergang is Kiemėnai [2][7]; OSM heeft geen gasleiding binnen 15 km van Pakruojis.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Hammerfest LNG (Melkøya) | Equinor | veldgas Snøhvit (CO2 afgescheiden en teruggeïnjecteerd) → LNG | 5,75 bcm/j LNG-export [1] | [1] |
| Klaipėda LNG-terminal (FSRU Independence) | KN Energies (FSRU sinds 2024-12 van KN) | LNG → regas, Litouws net | 3,75 bcm/j regas, 170.000 m³ opslag [2] | [2] |
| Kiemėnai-meetstation (grensovergang LT→LV) | Amber Grid / Conexus | Litouws → Latvisch net | 90 GWh/d LT→LV sinds 2023-11 [7] | [7] |
| Inčukalns UGS | Conexus Baltic Grid | transmissiegas → opslag | 4,47 bcm totaal, 2,32 bcm actief, 30 mcm/d afname [6] | [6] |

## 6 · Stoppunt
De brief stopt bij Inčukalns UGS: de bron die Lithuania toegang geeft tot de opslag [2][7] en de bestemming van de Latvenergo-ladingen via Klaipėda [4] vallen hier samen. Daarna is het gas anoniem Baltisch netgas. Fase D/E vervalt (geen bron noemt een afnemer van deze molecule).

## 7 · Open punten
- **Hammerfest → Klaipėda: aannemelijk, één bron.** Eerste lading 2014 (Golar Seal, Hammerfest, Statoil) [3]; contract Equinor verlengd tot eind 2024 en daarna niet verlengd [2] (alleen Wikipedia, geen primaire bron); Latvenergo koopt 2024–2026 zes ladingen via Klaipėda [4], herkomst plant niet genoemd. Een Hammerfest-lading 2022 ging naar Skagen en daarna mogelijk de Baltische Zee [5].
- **Werkelijke doorzet niet gevonden.** Alleen contractvolume 2015 (0,54 bcm), Latvenergo (6 TWh over 3 jaar) en capaciteiten; 1 bcm ≈ 10,4 TWh (Klaipėda 3,75 bcm ≈ 39 TWh). Jaarvolume op de bol = indicatie.
- **Haven-aanlopen beide kades** (Melkøya 11,7 km, Klaipėda 7,6 km) zijn rechte stippels; de Melkøya-lijn snijdt het eiland en de Klaipėda-lijn de Koerse Schoorwal op 1:10M-schaal: schematisch, niet de vaargeul.
- **b3: graafpad is aannemelijk, geen gepubliceerde lengte.** 413,1 km tegen 275,5 hemelsbreed (omwegfactor 1,5); alle 13 ways onbenoemd, twee bochten > 110 graden (Panevėžys, Iecava-regio): één bron (OSM), niet tegen een operator-trace gelegd.
- **Snøhvit-pijp 142,5 km tegen 160** [1]: −11%, OSM-way is de geometrie. Veldanker niet satelliet-controleerbaar.
- **Overlap zeestrook:** 80% met grafiet-skaland-lulea en 58% met gas-sabetta-zeebrugge (binnen 8 km): andere sites en ander product, alleen de corridor.

## 8 · Bronnen
[1] Wikipedia (EN), "Snøhvit" — 140 km NW van Hammerfest, 160 km pijp 680 mm, 5,75 bcm/j LNG-export. https://en.wikipedia.org/wiki/Sn%C3%B8hvit
[2] Wikipedia (EN), "Klaipėda LNG terminal" — FSRU Independence 3,75 bcm/j, Equinor-contract (Snøhvit/Melkøya), verlengd tot eind 2024, Klaipėda–Panevėžys-pijp, toegang tot Inčukalns. https://en.wikipedia.org/wiki/Klaip%C4%97da_LNG_terminal
[3] Offshore Energy, "Lithuania gets its first LNG cargo" (2014-10-28) — Golar Seal, Statoil Hammerfest. https://offshore-energy.biz/2014/10/28/lithuania-gets-its-first-lng-cargo
[4] LNG Prime, "Equinor to supply six LNG cargoes to Latvenergo" (2023-12-14) — 2024–2026, via Klaipėda FSRU, ≈ 6 TWh. https://lngprime.com/?p=100031
[5] LNG Prime, "Equinor ships first Hammerfest LNG cargo since September 2020" (2022-06-07) — Arctic Voyager naar Skagen, mogelijk Litouwen of Polen. https://lngprime.com/lng-terminals/equinor-ships-first-hammerfest-lng-cargo-since-september-2020/53665/
[6] Conexus/Skultė LNG, "Pazemes gazes krātuve" — Inčukalns 4,47 bcm, 2,32 bcm actief, 30 mcm/d, Conexus. https://www.skultelng.lv/en/pazemes_gazes_kratuve/
[7] Conexus Baltic Grid, "Enhancement of Latvia-Lithuania interconnection (ELLI)" — Kiemėnai 90 GWh/d, Panevėžys-compressor, Riga–Panevėžys, Inčukalns-toegang. https://conexus.lv/elli-eng
[8] OpenStreetMap-bijdragers (ODbL) — ways 1118916982, 174753089 (Snøhvit, Equinor, OSM-API); lokale Geofabrik-extracts litouwen en letland (13 ways in het graafpad, §2). https://api.openstreetmap.org/api/0.6/way/174753089/full
[9] Wikidata Q19826411 (Inčukalns underground gas storage) — coördinaat 57.1690, 24.6968; Esri World Imagery via `v2/tools/sat_check.py` (z15, live): `v2/build-cache/satcheck/sat-gas-snohvit-incukalns-melkoya.png`, `-klaipeda.png`, `-incukalns.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
**Recept:** functie `bak_gas_snohvit_incukalns()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh gas-snohvit-incukalns`); uitvoer `v2/data/stroomroute-gas-snohvit-incukalns.json` (36,1 KB, versie 2, lonlat). Geen profiel, geen wegscan, geen via-punten, geen kopie, geen vlucht. Tussenuitvoer: `v2/build-cache/ais/graaf/gas-snohvit-incukalns-leiding-snohvit.geojson` en `-leiding-klaipeda-incukalns.geojson` (beide FeatureCollection, uit `maak_leidingbeen_gas_snohvit_incukalns.py --schrijf`).

| # | modaliteit | km | naad | stippel | been |
|---|---|---|---|---|---|
| 1 | leiding | 142,5 | 0 | nee | Snøhvit-pijp (OSM-ways 1118916982 + 174753089), 727 punten |
| 2 | zee | 11,7 | 0,51 | ja | haven-aanloop Melkøya, rechte lijn |
| 3 | zee | 2.386,4 | 0 | nee | MARNET zeeknoop 4043 naar knoop 4504 (Kattegat), aannemelijk: één bron |
| 4 | zee | 62,7 | 0 | nee | MARNET Grote Belt, knoop 4504 naar 6864 |
| 5 | zee | 738,2 | 0 | nee | MARNET knoop 6864 naar zeeknoop 8873 |
| 6 | zee | 7,6 | 0 | ja | haven-aanloop Klaipėda, rechte lijn |
| 7 | leiding | 413,1 | 0,05 | nee | OSM-graafpad Klaipėda naar Inčukalns, 754 punten |

Totaal 3.762,2 km, 1.824 punten, 5 markers (veld, fabriek, steiger, FSRU, UGS), allemaal op 0,0 km van de lijn behalve Inčukalns 0,3 km (OSM-leidingeinde ligt 0,3 km ZW van het anker, in het installatieterrein).

**Toelichting per stippel/leiding/aanloop:**
- **Melkøya-aanloop (b2a, 11,7 km):** kade ligt 11,7 km van zeeknoop 4043 (> 5 km), dus aanloop; `maak_havenaanloop.py` liep in de timeout, rechte stippel, geen tweede poging. De lijn blijft op open water (0 km over land op 1:10M).
- **Klaipėda-aanloop (b2e, 7,6 km):** kade 7,6 km van zeeknoop 8873; rechte stippel. Op 1:10M snijdt de lijn de Koerse Schoorwal (6,4 km "over land" in de Natural Earth-laag): schematisch, niet de vaargeul in het lagoon.
- **Naad 0,51 km** tussen Hammerfest LNG-fabriek en LNG-steiger = procesgat op eigen terrein, geen been. Naad 0,05 km bij Klaipėda (OSM-leidingstart).
- **Leidingen doorgetrokken:** b1 142,5 km tegen 160 gepubliceerd = -11% (binnen de norm van 15%); b3 413,1 km is een graafpad over 13 onbenoemde ways, GEEN gepubliceerde lengte (hemelsbreed 275,5 km, omwegfactor 1,5): de km-toets is hier een indicatie, geen norm.
- **Zee b3-b5 samen 3.187,3 km**; ontwerp schatte 3.000-3.200. Grote Belt (62,7 km) is één MARNET-edge en snijdt geen land (0 km); Øresund is bewust niet gekozen.
- **Aannemelijk: één bron** staat in de beennaam van b3 (Hammerfest naar Klaipėda); de lijnstijl blijft doorgetrokken.
- **Toetsen:** geen naad > 5 km; 0 omkeringen en 0 teruglopen (`toets_knikken`: 29 knikken >= 60 graden, vooral in het OSM-graafpad b3 en het 1:10M-net rond Klaipėda); `toets_rechte_benen`: alleen de twee stippels en de ene MARNET-edge van de Grote Belt (omwegfactor 0,999, door twee vaste knopen, geen stippel nodig).

**Lessen:** (1) het maakscript leverde beide leidingbenen vooraf als FeatureCollection; de bake was daardoor 21 s en zonder zware runs. (2) Een zeeroute die de router verkeerd kiest (Øresund) forceer je met vaste MARNET-knopen als begin/eind van opeenvolgende `--been`-regels; de knopen zelf zijn de naad, dus 0 km. (3) Twee haven-aanlopen > 5 km tonen de routestippels als zeebeen met `stippel`; de naad blijft dan binnen de norm.
