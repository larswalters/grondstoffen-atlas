# Routebrief (licht) · gas — Mobley (Wetzel County, West Virginia) → Mountain Valley Pipeline → Chatham (Virginia)

**stroom-id:** `gas-mobley-chatham` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) ·
**status:** gebakken
**Keten in één zin:** Appalachen-schaliegas gaat via de Mountain Valley Pipeline (MVP, 42 inch, 303 mijl) van de Equitrans-aansluiting in Wetzel County (WV) naar Transco Compressor Station 165 bij Chatham (Pittsylvania County, VA), waar het de Transco-leiding naar het zuidoosten invoedt; één doorgetrokken OSM-leidingbeen van 487,6 km.
**Welke as van het verhaal:** *Appalachen-gas naar het zuidoosten van de VS.* Volume: capaciteit 2,0 bcf/d ≈ 20,7 bcm/j (eigen omrekening), volle 20-jaarscontracten, in dienst 14 juni 2024 [1][2][3]; werkelijke doorzet bleef in 2024 lager: ca. 0,5 bcf/d (15-30 juni) en bijna 1 bcf/d ≈ 10 bcm/j (juli 2024), door een knelpunt bij Station 165 [4]. Een jaargemiddelde is niet gevonden.

## 1 · Ketenkaart
```
Mobley-complex (Equitrans-aansluiting, ca. 1,6 km ZW van het OSM-begin; niet als anker gelegd, OPEN PUNT)
  ··(niet getekend)··
`gas-mvp-begin` 39.5628,-80.5434 (OSM-leidingbegin op de strook, Wetzel County)
  ──(b1 leiding · MVP 42" · OSM name=Mountain Valley Pipeline, 6 ways · 487,6 km, doorgetrokken)──►
`gas-mvp-station165` 36.8319,-79.3428 (Transco Compressor Station 165, Pittsylvania County bij Chatham) — stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | leiding | `gas-mvp-begin` → `gas-mvp-station165` | Mountain Valley Pipeline, 42", operator Mountain Valley Pipeline LLC | **487,6 OSM**; gepubliceerd 303 mijl = 488 km [1][3] = −0,1% | vooraf gestikt geojson (FeatureCollection) uit 6 OSM-ways, zie hieronder | nee |

OSM-ways (man_made=pipeline, substance gas, diameter 42", operator Mountain Valley Pipeline, LLC; OSM-API 2026-10-31), noord → zuid met eigen lengte: 1235574214 (4,6 km, begin 39.5628,-80.5434) · 1235574206 (20,3) · 627895219 (100,3) · 897721062 (123,7) · 1235543996 (67,0) · 750297699 (171,7, eindigt 36.8319,-79.3428). Som 487,6 km, 6 ways. Naden 34 / 14 / 11 / 14 m (en één tussen 1235543996 en 750297699 van ongeveer 0 m): gewoon stikken, geen stippel, geen naad > 5 km. De drie kleine stompjes uit de pyosmium-telling (Transco-interconnect, 0,4-0,7 km) blijven weg: niet tekenen, het einde ligt op de strook zelf.
Hemelsbreed begin → einde 321 km; 487,6 km is 1,52 maal dat, passend bij een Appalachen-tracé. Geen wegbeen, geen via-punten, geen spoor, geen zee.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-mvp-begin` | begin gekarteerde leiding, Equitrans-aansluiting (nabij Mobley) | OSM-leidingbegin MVP, Wetzel County | 39.5628, -80.5434 | [1][2][6] | aannemelijk (z16 gezien: bosgebied; een smalle strook met leiding loopt west-zuidwest en oost-noordoost door het punt, op het punt zelf een grindterrein met een klein gebouw; de strook is de MVP, dat dit de Equitrans-aansluiting is staat alleen in de bron, niet op het beeld) |
| `gas-mvp-station165` | eind MVP en afleverpunt, Transco Compressor Station 165 bij Chatham | OSM-leidingeinde MVP, Pittsylvania County | 36.8319, -79.3428 | [2][5][6] | bron-gelegd (z16 gezien: uit het bos komt de strook op een ontgraven terrein met leidingapparatuur en een omheind bouwwerk; het compressorstation-complex van Transco ligt zichtbaar 0,4 km oostelijk; het exacte MVP-uiteinde is de kartering, de plek is door twee bronnen genoemd) |

Hergebruik: geen bestaand anker; de zusterstroom `gas-waha-aguadulce` is hetzelfde type zuivere leidingketen (patroon). Sitelaag `gas-sitelaag.json` heeft geen MVP-, Mobley- of Transco-site.
Niet gelegd: het **Mobley-complex** zelf. De OSM-dorpsknoop Mobley ligt op 39.5570,-80.5487 (0,8 km ZW van het begin, dorpscentroïde, geen anker); op z15 ligt een groot omheind installatiecomplex met wegen op ca. 39.553,-80.558, 1,6 km ZW van het begin. De eigenaar is niet bevestigd (de MVP-site noemt alleen Wetzel County).

## 4 · Via-punten
Niet van toepassing: leidingbeen (OSM-way), geen corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| MVP-hoofdleiding (3 compressorstations in Wetzel, Braxton, Fayette County) | Mountain Valley Pipeline LLC (Equitrans/EQT-operator, NextEra, Con Edison Transmission, anderen) | Equitrans-systeem (Wetzel County) → Transco Station 165 | 2,0 bcf/d ≈ 20,7 bcm/j, 20-jaarscontracten voor volle capaciteit | [1][2][3] |
| Transco Compressor Station 165 | Transco (Williams) | MVP-interconnect (mijlpaal 303,5) → Transco Zone 5 naar het zuidoosten | beperkt: ca. 700 MMcf/d extra opname in 2024 door een knelpunt | [4][5] |

## 6 · Stoppunt
De brief stopt bij Transco Station 165: MVP levert er volgens [2][5] af in het Transco-systeem, en vanaf dat punt vermengt het gas zich met ander Transco-gas; geen bron legt dit gas aan één afnemer. Fase D en E vervallen.

## 7 · Open punten
- **Mobley-complex niet gelegd:** de Equitrans-aansluiting zelf is niet apart gevonden; het begin is het OSM-leidingbegin (aannemelijk). Het stuk tot het complex (ca. 1,6 km) is niet getekend.
- **Doorzet onbekend:** 20,7 bcm/j is capaciteit. Gemeten maandwaarden 2024 zijn 0,5 en bijna 1 bcf/d [4]; een jaargemiddelde ontbreekt. De naam "Mobley" staat niet op de MVP-site.
- **Einde is OSM-kartering:** het Transco-eindpunt komt uit OSM plus de FERC-beschrijving, niet uit een coördinaat van Transco zelf.
- **Dubbel gebruik:** Appalachen-ketens uit latere golven kunnen deze leiding ook raken; MVP Boost (aanvraag oktober 2025) en Southgate (naar Noord-Carolina) zijn niet getekend.

## 8 · Bronnen
[1] Mountain Valley Pipeline, project overview (303 mijl, 42 inch, 2 bcf/d, Wetzel County WV → Pittsylvania County VA, interconnects Equitrans en Transco Station 165, 20-jaarscontracten, in dienst 14 juni 2024). https://www.mountainvalleypipeline.info/project-overview
[2] FERC, MVP certification order, 13 okt. 2017 (Transco Interconnect op mijlpaal 303,5 in Pittsylvania County, levert aan Transco Compressor Station 165). https://aglaw.psu.edu/wp-content/uploads/2021/02/MVP-FERC-Certification-Order-Oct.-13-2017.pdf
[3] Wikipedia, "Mountain Valley Pipeline" (303 mijl, 488 km, 2 bcf/d, in dienst 14 juni 2024, eigenaren). https://en.wikipedia.org/wiki/Mountain_Valley_Pipeline
[4] S&P Global via Hellenic Shipping News, "West Virginia natural gas production rises sharply during first full month of MVP", juli 2024 (0,5 bcf/d 15-30 juni, bijna 1 bcf/d juli, knelpunt Station 165). https://www.hellenicshippingnews.com/?p=1050267
[5] EIA Today in Energy 62323, juni 2024 (303 mijl, 2,0 bcf/d, aansluiting op Transco Station 165, Pittsylvania County). https://www.eia.gov/todayinenergy/detail.php?id=62323
[6] OpenStreetMap (ODbL), ways 1235574214, 1235574206, 627895219, 897721062, 1235543996, 750297699 (man_made=pipeline, name=Mountain Valley Pipeline, operator Mountain Valley Pipeline, LLC); OSM-API 2026-10-31. https://www.openstreetmap.org/way/750297699
[7] Nominatim (OSM), 2026-10-31: Mobley (hamlet node 39.5570,-80.5487, Wetzel County); begin 39.5628,-80.5434 = Wetzel County; einde 36.8319,-79.3428 = Pittsylvania County. https://nominatim.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-gas-mobley-chatham-begin.png`, `-begin16.png`, `-mobley.png`, `-station165.png`, `-station165-z16.png`.
[9] Chatham Star-Tribune en Cardinal News 2024 (Transco Compressor Station 165 in het Transco Village-complex bij Chatham). https://cardinalnews.org/2024/03/04/pipeline-expansion-plan-runs-through-pittsylvania-county/

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
- **Bestand:** `v2/data/stroomroute-gas-mobley-chatham.json`, 104,7 KB, versie 2, punt_formaat lonlat, 1 been, 2 markers.
- **Been b1 (leiding, doorgetrokken):** Mountain Valley Pipeline 42 inch, 487,7 km, 5.122 punten. Gepubliceerd 488 km (303 mijl): -0,1%. Naden tussen de 6 ways 32 / 8 / 15 / 15 / 0 m (max 32 m, ruim onder 5 km). Grootste segment 1,02 km. Geen stippel, geen aanloop, geen via-punten, geen zee/weg.
- **Markers:** `gas-mvp-begin` 39.5628,-80.5434 (2,8 m van de lijn, aannemelijk) en `gas-mvp-station165` 36.8319,-79.3428 (4,8 m van de lijn, bron-gelegd).
- **Recept:** `python v2/tools/maak_leidingbeen_gas_mobley_chatham.py` (OSM-API, ways 1235574214, 1235574206, 627895219, 897721062, 1235543996, 750297699, geoorienteerd op naad) schrijft `v2/build-cache/ais/graaf/gas-mobley-chatham-leiding-mvp.geojson` (FeatureCollection); daarna `bash v2/tools/bak_stromen.sh gas-mobley-chatham` (functie `bak_gas_mobley_chatham`, `--been-geojson leiding|...`).
- **Toetsen:** toets_knikken 157 knikken >= 60 gr, 1 omkering (158 gr op 39.3985,-80.4771, door de tool als scherpe bocht, echt geclassificeerd, 0 terugloop); de 156 overige zijn OSM-vertexzigzags van de leidingkartering (spikes van 4-130 m), geen herstelwerk. toets_rechte_benen: geen treffer voor deze stroom.
- **Niet getekend:** het Mobley-complex (ca. 1,6 km ZW van het OSM-begin) en alles na Station 165; MVP Boost en Southgate.
- **Lessen:** (1) bij een zuivere OSM-leidingketen is selecteren op way-id schoner dan op tags: de 3 stompjes bij de Transco-interconnect blijven zo vanzelf weg. (2) De eerste way moet op de naad met de tweede georienteerd worden (de waha-tool neemt de volgorde van de OSM-way aan). (3) De 157 knikken zijn kartering, geen routefout: een leidingbeen hoeft de knikkentoets niet gladgestreken.
