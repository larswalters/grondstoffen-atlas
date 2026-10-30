# Routebrief (licht) · gas — Mnazi Bay (Mtwara) → Madimba → Kinyerezi, Dar es Salaam (Tanzania)

**stroom-id:** `gas-mnazibay-daressalaam` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) ·
**status:** gebakken
**Keten in één zin:** Gas uit het Mnazi Bay-veld (Maurel & Prom, TPDC) gaat via de verwerking op het schiereiland Msimbati door een 11 km-leiding
naar de Madimba-gasfabriek (Gasco) en van daar door de 36-inch Mtwara-Dar es Salaam-leiding (Chinees gebouwd, 2015) naar het Kinyerezi-ontvangststation en de
gascentrales van Dar es Salaam. Een twee-benen-pijp, volledig leiding, doorgetrokken; de tekening stopt bij Kinyerezi.
**Welke as van het verhaal:** *Gas-voor-stroom, Oost-Afrika* — Tanzanias eigen gas voedt Dar es Salaams elektriciteit. Volume: Mnazi Bay leverde gemiddeld
89,4 MMcf/d in februari 2025 [4] (≈ 0,9 bcm/j; 1 MMcf/d = 0,0103 bcm/j), operator noemt ~100 MMcf/d uit vijf putten [4]. **Indicatief**: het laagste, gebronde
getal (0,9 bcm/j, peil feb 2025); de leidingcapaciteit (350 MMcf/d verwerking [1]; 210 MMcf/d draagvermogen volgens TPDC 2015 [7]; 784 MMcf/d volgens EAC) is geen doorzet.

## 1 · Ketenkaart
```
Mnazi Bay-verwerking (GPF, Msimbati) `gas-mnazibay-gpf`
  ──(b1 leiding · Manzi–Madimba-leiding, OSM-way 678587791 · 11,3 km, doorgetrokken)──►
Madimba-gasfabriek (Gasco) `gas-madimba-plant`
  ──(b2 leiding · TPDC-leiding Mtwara–Dar, 36", OSM-way 848568587 · 478,7 km OSM / 542 Wikipedia, doorgetrokken)──►
Kinyerezi-ontvangststation / -centrales, Dar es Salaam `gas-kinyerezi-ontvangst` — stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-mnazibay-gpf` → `gas-madimba-plant` | Manzi–Madimba pipeline (OSM name-tag, ondergronds, substance=gas) | OSM **11,3** (way 678587791, 22 punten) [3] | `maak_leidingbeen_gas_mnazibay_daressalaam.py` (OSM-way, vooraf gestikt FeatureCollection) | nee |
| b2 | B | leiding | `gas-madimba-plant` → `gas-kinyerezi-ontvangst` | Mtwara–Dar es Salaam Natural Gas Pipeline (TPDC, 900 mm), OSM-way 848568587 **omgekeerd** (OSM tekent Dar → Madimba) | 542 [1]; 533 (infobox [1]), 532 [7]; OSM **478,7** (−11,7% / −10,2% / −10,0%) [2] | idem, 173 punten; grootste segment 22,9 km (rechte rechtsstrook, geen kartering-gat) | nee |

b1 en b2 sluiten op 0,22 km (way-eind b1 −10.3894,40.3169 ↔ way-begin b2 −10.3874,40.3171, beide binnen de Madimba-omheining): geen stippel. Het way-eind van b2 ligt
0,66 km van het Kinyerezi-anker; geen eigen been (< 2 km). **Songo Songo-tak** (24 inch, 24 km uit Songo Songo, voegt bij Somanga in [1]) is een andere bron en wordt niet getekend.
Lengtetoets ±15%: OSM-geometrie (geen wegkm). Z14-blik midden op b2 (−8.9064,39.2958): rechte, ontboste rechtsstrook door de savanne bevestigt de rechte OSM-segmenten [9].

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-mnazibay-gpf` | gasverwerking (kop) | Mnazi Bay Gas Processing Facility, schiereiland Msimbati | -10.3240, 40.3877 | [3][4] | bron-gelegd (z15 gezien: klein omheind compound met tanks/pads op de westkust-punt van het schiereiland, toegangsweg langs het strand; OSM-begin van de Manzi–Madimba-leiding ligt erop) |
| `gas-madimba-plant` | gasfabriek (overslag) | Madimba Gas Processing Plant (Gasco, 2 treinen) | -10.3874, 40.3171 | [1][2][4] | bron-gelegd (z15 gezien: omheind complex met twee processtreinen en rood/witte gebouwen in de bush, zandweg naar de Mtwara–Lindi-weg; OSM-eind van b2 erop) |
| `gas-kinyerezi-ontvangst` | ontvangststation / gascentrales (staart, stoppunt) | Kinyerezi Receiving Station + Kinyerezi I/II | -6.8589, 39.1508 | [5][6] | bron-gelegd (z16 gezien: twee omheinde gasturbinecomplexen met schoorstenen en ketels, de westelijke = Kinyerezi II (Wikipedia-punt −6.8589,39.1508); een ontboste leidingstrook loopt er langs; het OSM-leiding-eind ligt 0,66 km ZW) |

Hergebruik: geen. De sitelaag (`gas-sitelaag.json`) heeft geen Tanzania-site; deze drie ankers zijn nieuw. Kinyerezi I ligt 0,5 km oostelijker (−6.8583, 39.1550, Wikipedia [5]); het
ontvangststation zelf is niet apart gelokaliseerd (zie §7). Het OSM-eind van b2 (−6.8639, 39.1476) is **geen** anker, alleen het lijn-eind.

## 4 · Via-punten
Niet van toepassing: leiding = OSM-way, geen corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mnazi Bay GPF | Maurel & Prom (operator), Wentworth, TPDC | veldgas → behandeld gas | veld ~130 MMcf/d na 3 nieuwe putten (2025/26); ~100 MMcf/d uit 5 putten (2025) | [4][10] |
| Madimba-gasfabriek | Gasco (TPDC) | gas → exportgas voor de leiding | Madimba + Songo Songo samen 350 MMcf/d verwerking (twee treinen elk) | [1][2] |
| Kinyerezi I + II | Tanesco | gas → elektriciteit | 150 MW + 240 MW | [5][6] |

## 6 · Stoppunt
De tekening stopt bij Kinyerezi: daar eindigt de 36-inch-leiding (TPDC noemt het Kinyerezi Receiving Station als Dar-uiteinde [2]); de verdere verdeling (Ubungo-centrales, de geplande
extensie naar Chalinze, industrie, CNG) is niet als vaste route gedocumenteerd, dus geen fase D/E. Verhaal in één zin: "het eigen gas van Tanzania voedt Dar es Salaams stroom".

## 7 · Open punten
- **Doorzet is indicatief en tegenstrijdig:** 89,4 MMcf/d feb 2025 [4] vs ~100 vs M&P 59,7 MMcf/d (60%-aandeel, 2025) [10]; Citizen/BoT meldt dalende gasproductie in 2023–2025 door waterkracht [11]; capaciteit 210–784 MMcf/d. Niet de leiding-doorzet; op de leiding ligt ook Songo Songo-gas na Somanga.
- **Kinyerezi vs Ubungo:** het Kinyerezi Receiving Station [2] is het gedocumenteerde Dar-eind; de exacte locatie van het station (compound) is niet gevonden, het anker is het centrale-complex (Kinyerezi II), niet het station.
- **Laatste 0,66 km** tussen OSM-leiding-eind en Kinyerezi-anker is niet gekarteerd; geen stippel (< 2 km).
- **OSM 478,7 km tegen 532–542 km gepubliceerd** (−10 tot −12%): de leiding is in OSM met lange rechte segmenten getekend en snijdt waarschijnlijk bochten af; binnen de ±15%-norm, geen wegkm.
- **Stroom-id heeft een spatie** (`dares salaam`): bak-bestanden gebruiken de slug `daressalaam`.
- Een EAC-bron (784 MMcf/d) was niet te openen (verlopen certificaat); capaciteit daarom uit zoekresultaat, niet geverifieerd.

## 8 · Bronnen
[1] Wikipedia, "Mtwara–Dar es Salaam Natural Gas Pipeline" — 533/542 km, 36 inch, Songo Songo-tak 24 inch, 350 MMcf/d Madimba + Songo Songo, CPTDC/Exim, in bedrijf 10-10-2015. https://en.wikipedia.org/wiki/Mtwara%E2%80%93Dar_es_Salaam_Natural_Gas_Pipeline
[2] OpenStreetMap (ODbL), way 848568587 (man_made=pipeline, diameter 900, operator TPDC, substance=gas, 173 punten, 478,7 km), opgehaald 2026-10-30; en TPDC, "Downstream" (Kinyerezi Receiving Station, Ntorya–Madimba 34,2 km). https://www.openstreetmap.org/way/848568587 · https://www.tpdc.co.tz/product-category/downstream
[3] OpenStreetMap (ODbL), way 678587791 "Manzi - Madimba pipeline" (22 punten, 11,3 km), opgehaald 2026-10-30. https://www.openstreetmap.org/way/678587791
[4] Business Daily / The Citizen, "Three new natural gas wells set for drilling in Tanzania", 2025 — Mnazi Bay 89,4 MMcf/d (feb 2025), 100 MMcf/d uit vijf putten, Gasco-Madimba, drie putten +30 MMcf/d. https://www.thecitizen.co.tz/tanzania/news/national/three-new-natural-gas-wells-set-for-drilling-in-tanzania-5003234
[5] Wikipedia, "Kinyerezi I Thermal Power Station" — 150 MW, Tanesco, −6.8583,39.1550. https://en.wikipedia.org/wiki/Kinyerezi_I_Thermal_Power_Station
[6] Wikipedia, "Kinyerezi II Thermal Power Station" — 240 MW, −6.8589,39.1508 (Wikipedia-coördinaat via API). https://en.wikipedia.org/wiki/Kinyerezi_II_Thermal_Power_Station
[7] TanzaniaInvest, "Mtwara-Dar es Salaam Natural Gas Pipeline Inaugurated", 2015 — 532 km, 70 → 80 MMcf/d, tot 210 MMcf/d, Madimba (Gasco). https://tanzaniainvest.com/?p=4938
[8] Offshore Technology, "Mnazi Bay – Dar es Salaam Gas Pipeline" — 542 km, max 36", TPDC, 2015. https://www.offshore-technology.com/marketdata/mnazi-bay-dar-es-salaam-gas-pipeline-tanzania/
[9] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-gas-mnazibay-daressalaam-mnazi.png`, `-madimba.png`, `-dar.png`, `-dar-z16.png`, `-midcheck.png`.
[10] Maurel & Prom, "Activity for the year 2025" (zoekresultaat, pagina niet te openen) — werkbelang 60%, 59,7 MMcf/d in 2025, uitbreiding naar ~130 MMcf/d. https://www.streetinsider.com/Press+Releases/Maurel+%26amp%3B+Prom%3A+Activity+for+the+year+2025/25910554.html
[11] The Citizen, "Tanzania's natural gas output falls further as hydropower expands" — Q2 2025 −24,5% (15.493,5 MMscf), Mnazi Bay 54,7% van de productie 2023. https://www.thecitizen.co.tz/tanzania/news/national/tanzania-s-natural-gas-output-falls-further-as-hydropower-expands-5182074

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
**Bestand:** `v2/data/stroomroute-gas-mnazibay-daressalaam.json` (4,9 KB, versie 2, lonlat). **Functie:** `bak_gas_mnazibay_dares_salaam` in `v2/tools/bak_stromen.sh` (draaien: `bash v2/tools/bak_stromen.sh gas-mnazibay-dares_salaam`, want de generieke dispatch kan een spatie in het id niet aan). Totaal 490,0 km, 195 punten, 3 markers.

| # | modaliteit | km | brief | naad | beschrijving |
|---|---|---|---|---|---|
| 1 | leiding | 11,3 | OSM 11,3 | start | Manzi-Madimba-leiding (OSM way 678587791), doorgetrokken |
| 2 | leiding | 478,7 | 542 gepubliceerd / OSM 478,7 | 0,22 km | Mtwara-Dar-leiding 36 inch (OSM way 848568587 omgekeerd), doorgetrokken |

**Recept:** `python v2/tools/maak_leidingbeen_gas_mnazibay_daressalaam.py` (al gedraaid, beide FeatureCollections in `v2/build-cache/ais/graaf/`), daarna twee `--been-geojson leiding` in reisvolgorde en drie markers. Geen zee, geen haven-aanloop, geen stippel, geen via-punten, geen kopie, geen extract.

**Toets:** b2 is -11,7 % tegen 542 km (Wikipedia) en -10 % tegen 532 (binnen +-15 %, geen wegkm: OSM-geometrie met lange rechte segmenten). Naad b1-b2 0,22 km (beide binnen de Madimba-omheining). Markers 0,0 / 0,0 / 0,66 km van de lijn (Kinyerezi-anker is het centrale-complex, het leiding-eind ligt 0,66 km ZW; < 2 km, geen stippel). toets_knikken: 6 knikken >= 60 graden, 0 omkeringen, 0 terugloop; ze zitten op de OSM-wayeinden (spikes van 8-42 m straal bij Msimbati, Madimba en Kinyerezi) en op een krappe bocht (717 m) bij -8,039/39,065: bronkartering, geen routerfout. Alle benen doorgetrokken, dus niets in toets_rechte_benen.

**Lessen:** (1) Een stroom-id met spatie breekt de generieke dispatch (`bak_gas_mnazibay_dares salaam` is geen geldige functienaam): roep hem aan met een underscore in plaats van de spatie. (2) De leidinggeometrie komt uit een per-keten OSM-tool; geen eigen bochtsnoei nodig.
