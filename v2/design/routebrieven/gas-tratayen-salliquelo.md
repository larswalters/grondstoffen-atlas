# Routebrief (licht) · gas — Tratayén (Vaca Muerta) → Gasoducto Perito Moreno → Salliqueló (Argentinië)

**stroom-id:** `gas-tratayen-salliquelo` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Keten in één zin:** Gas uit de schalie van Vaca Muerta (Neuquén) vertrekt bij de gasbehandeling Tratayén in het Gasoducto Perito Francisco Pascasio Moreno (ex Presidente Néstor Kirchner, 36 inch, ENARSA), loopt in één rechte oost-noordoostlijn door Neuquén, Río Negro, La Pampa en Buenos Aires naar het knooppunt Salliqueló en voedt daar de TGS-hoofdleidingen NEUBA II en III richting Buenos Aires. Alleen leiding, geen zee, weg of spoor.
**Welke as van het verhaal:** de eerste grote evacuatieleiding van Vaca Muerta, **21 mln m3/d ≈ 7,7 bcm/j capaciteit** [1][2][3] (2026); ENARSA noemt in mei 2025 "tot 26 mln m3/d" ≈ 9,5 bcm/j [5]. Werkelijke doorzet niet gevonden. Tramo 1 geopend 9-7-2023 [1]; uitbreiding naar 35 mln m3/d (+14) gegund aan TGS okt 2025, werken gestart 9-2-2026, klaar winter 2027 [2][3][4].

## 1 · Ketenkaart
```
Tratayén `gas-tratayen-start` (installatie bij OSM-leidingbegin, gasbehandeling ca. 1,5 km ZW) ──(b1 leiding · GPM tramo 1 · 566,8 km, waarvan 475,4 OSM doorgetrokken + 91,4 stippel)──►
Salliqueló `gas-salliquelo-knoop` (Buenos Aires; aansluiting NEUBA II/III) ═══ stoppunt ═══
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | leiding | `gas-tratayen-start` → `gas-salliquelo-knoop` | Gasoducto Perito Moreno, zes OSM-ways (1370992520, 1437022951, 1370990857, 1373543401, 1435529409, 1435527433) | **566,8** (OSM 475,4 + gaten 91,4) tegen 573 [1] (−1,1%) en 570 [3] (−0,6%) | OSM-way-stitch: zes `gas-tratayen-salliquelo-leiding-s1…s6.geojson` | ja: vijf gaten, reden "OSM-way ontbreekt" |

Zes doorgetrokken stukken (s1 72,7 · s2 0,6 · s3 316,8 · s4 2,7 · s5 16,0 · s6 66,6 km) en vijf stippelgaten ertussen, in reisvolgorde:
| gat | van (lat,lon) | naar (lat,lon) | km hemelsbreed |
|---|---|---|---|
| G1 | -38.1657, -67.8771 | -38.0602, -67.6125 | 25,95 |
| G2 | -38.0573, -67.6071 | -38.0199, -67.5055 | 9,82 |
| G3 | -37.0866, -64.1954 | -37.0816, -64.0254 | 15,09 |
| G4 | -37.0809, -63.9950 | -37.0781, -63.8163 | 15,85 |
| G5 | -37.0761, -63.6387 | -37.0490, -63.3628 | 24,67 |
Eigen PBF-scan (Geofabrik `argentina`, man_made=pipeline): de zes ways sluiten niet op elkaar en in de gaten ligt geen andere pijpleiding binnen 3 km van de rechte lijn. Het leidinggedeelte is dus 83% gemeten, 17% stippel (91,4 van 566,8 km). Fase A (velden Vaca Muerta), D en E vervallen: geen bron noemt één afnemer van deze stroom.

## 3 · Ankers
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-tratayen-start` | begin leiding | Tratayén, begin GPM (OSM-leidingbegin) | -38.4277, -68.5583 | [1][3][6] | aannemelijk (z15 gezien: omheind installatieterrein met leidingwerk en gebouwen aan de corridor, punt op de oostrand; de grote gasbehandeling ligt ca. 1,5 km zuidwestelijk, niet gelegd) |
| `gas-salliquelo-knoop` | einde leiding, stoppunt | Salliqueló, einde OSM-way 1435527433 | -36.8546, -62.6638 | [1][2][6] | aannemelijk (z15 gezien: kruising van leidingstrook en landweg in akkerland, klein omheind terrein met gebouwen ca. 0,5 km noordoost; NEUBA II/III-ways lopen 0,26 km ernaast) |

Hergebruik: geen. Argentinië staat niet in de sitelaag `gas-sitelaag.json` en niet in eerdere gas-brieven.

## 4 · Via-punten
Niet van toepassing: leidingbeen volgt OSM-geometrie, er is geen corridorkeuze door ons.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Tratayén gasbehandeling + compressie | niet gevonden | schaliegas Vaca Muerta → GPM | +1 compressor, installatie wordt 90.000 HP [2] | [2][3] |
| GPM (tramo 1) | ENARSA | Tratayén → Salliqueló, 36 inch, X70 | 21 mln m3/d (+14 gepland, winter 2027) | [1][2][4] |
| Salliqueló | TGS (NEUBA II/III) | GPM → regulated net naar Gran Buenos Aires | +12 mln m3/d en 20 km parallelleiding gepland [2] | [2][6] |

## 6 · Stoppunt
Salliqueló, het einde van tramo 1: dáár stopt de GPM en loopt het gas anoniem door in het TGS-net (NEUBA II/III) naar Gran Buenos Aires. De tweede etappe Salliqueló → San Jerónimo Norte (524 km) is niet gebouwd. Fase D/E vervalt.

## 7 · Open punten
- **Doorzet ontbreekt.** Alleen capaciteit (21 mln m3/d; 26 volgens ENARSA mei 2025 [5]); de besparing van US$ 2,1 mld op LNG-import in 2023 is een projectie. Gloedgewicht = capaciteit 7,7 bcm/j tot er een meting is.
- **Vijf OSM-gaten (91,4 km, 17%)** zijn stippel; de leiding bestaat daar fysiek (573 km gepubliceerd), alleen de kartering mist.
- **Tratayén-anker is de OSM-leidingbegin**, niet de grote gasbehandeling (ca. 1,5 km zuidwest, niet gelegd). De exacte leidingkop op het procesterrein is niet gevonden.
- **Salliqueló:** NEUBA II/III lopen daar parallel en overlappen; de lijn stopt op het OSM-einde van de GPM, niet op het TGS-station.
- Niet in de keten: OSM-way 1172439436 "Gasoducto Nestor Kirchner" (55,6 km, -37.46/-68.31 → -37.66/-67.75), ligt buiten de corridor. Compressorstations La Pampa (Casa de Piedra, Doblas, Chacharamendí) zijn nog niet gebouwd [2], niet gelegd.
- Tooling: geometrie uit een PBF-scan met `osmium.FileProcessor` op `argentina`, geen Overpass; gem.wiki gaf 403, Wikipedia-API gaf 429 (Tratayén/Salliqueló-coördinaten niet daaruit gehaald).

## 8 · Bronnen
[1] Wikipedia (ES), "Gasoducto Perito Francisco Pascasio Moreno": 573 km, 36 inch, tramo Tratayén–Salliqueló geopend 9-7-2023, 21 mln m3/d. https://es.wikipedia.org/wiki/Gasoducto_Presidente_N%C3%A9stor_Kirchner
[2] TGS, persbericht 9-2-2026: start werken, +14 mln m3/d Tratayén–Salliqueló, 3 plants La Pampa + Tratayén 90.000 HP, +12 mln m3/d regulated net, NEUBA III +15.000 HP. https://www.tgs.com.ar/?p=17572
[3] LM Neuquén, "TGS inicia obras en el gasoducto Perito Moreno", 9-2-2026: 570 km, 36 inch, 21 mln m3/d. https://mase.lmneuquen.com/gas/vaca-muerta-tgs-inicia-obras-el-gasoducto-perito-moreno-n1227577
[4] El Economista, "Adjudicaron la ampliación del gasoducto Perito Moreno", 20-10-2025: 21 → 35 mln m3/d, TGS enig bieder. https://eleconomista.com.ar/energia/adjudicaron-ampliacion-podria-transformar-mapa-energetico-argentino-n89629
[5] EconoJournal, ENARSA licitatie uitbreiding, 22-5-2025: "tot 26 mln m3/d" van Neuquén naar Buenos Aires. https://econojournal.com.ar/energia/enarsa-lanzo-la-licitacion-para-la-ampliacion-del-gasoducto-perito-moreno-que-permitira-transportar-mas-gas-de-vaca-muerta/
[6] OpenStreetMap-bijdragers (ODbL), Geofabrik `argentina`, eigen PBF-scan man_made=pipeline (scan `v2/build-cache/ais/graaf/gas-tratayen-salliquelo-pbfscan.json`; ways, namen en gaten uit §2).
[7] Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-gas-tratayen-salliquelo-{tratayen,salliquelo}-z15.png`.
[8] Wikipedia (EN), "Vaca Muerta" en gem.wiki-zoekpagina (403), alleen als startpunt genoemd; websearch-resultaten (La Nación 28-2-2025, Diario Jornada) alleen via zoekresultaat gelezen: https://www.lanacion.com.ar/economia/el-gobierno-licitara-la-ampliacion-del-gasoducto-perito-moreno-por-us700-millones-nid28022025/

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)

**Recept:** `bash v2/tools/bak_stromen.sh gas-tratayen-salliquelo` (functie `bak_gas_tratayen_salliquelo`, alleen `hecht_marnet.py route` met 6 × `--been-geojson` en 5 × `--stippel`; geen zee, geen profiel in `maak_stroombeen_weg.py`) → `v2/data/stroomroute-gas-tratayen-salliquelo.json` (15,3 KB, versie 2, lonlat, 624 punten, 2 markers).

| # | modaliteit | km | geometrie |
|---|---|---|---|
| 1 | leiding | 72,7 | OSM-way 1370992520 (s1), doorgetrokken |
| 2 | leiding | 26,0 | stippel G1, OSM-way ontbreekt |
| 3 | leiding | 0,6 | OSM-way 1437022951 (s2) |
| 4 | leiding | 9,8 | stippel G2 |
| 5 | leiding | 316,8 | OSM-way 1370990857 (s3) |
| 6 | leiding | 15,1 | stippel G3 |
| 7 | leiding | 2,7 | OSM-way 1373543401 (s4) |
| 8 | leiding | 15,9 | stippel G4 |
| 9 | leiding | 16,0 | OSM-way 1435529409 (s5) |
| 10 | leiding | 24,7 | stippel G5 |
| 11 | leiding | 66,6 | OSM-way 1435527433 (s6) |

**Totaal 566,9 km** (doorgetrokken 475,4 + stippel 91,5) tegen 573 [1] (-1,1%) en 570 [3] (-0,5%): binnen ±15%. Markers: Tratayén (-38.4277, -68.5583) en Salliqueló (-36.8546, -62.6638), beide 0,005 en 0,002 km van de lijn.

**Toets:** alle naden 0,000 km (vooraf gestikte geojsons sluiten exact op de stippeluiteinden); `toets_knikken` 0 knikken; `toets_rechte_benen` meldt alleen de vijf stippelgaten (omwegfactor 1,00, bedoeld); json.load, versie 2, lonlat, modaliteit alleen `leiding`, elk been >= 2 punten.

**Stippel (vijf gaten, 91,5 km = 16%):** reden "OSM-way ontbreekt" — de PBF-scan (Geofabrik `argentina`, man_made=pipeline) vond in de gaten geen andere pijpleiding binnen 3 km van de rechte lijn; de leiding bestaat fysiek (573 km gepubliceerd), alleen de kartering mist. Geen haven-aanloop, geen vlucht, geen kopie, geen via-punten (leidingbeen volgt OSM).

**Lessen:** (1) een leidingbeen uit vooraf gestikte geojsons (FeatureCollection) en stippels in reisvolgorde bakt in 16 s en heeft geen zwaar rekenwerk nodig; (2) `bak_stromen.sh` is een groot bestand dat andere agenten tegelijk bewerken: bash las het script tijdens de run en gaf aan het eind een onschuldige regel "g: command not found" (de stroom was toen al geschreven), `bash -n` slaagt daarna; (3) stroom-id en eindpunt kloppen (Salliqueló).

