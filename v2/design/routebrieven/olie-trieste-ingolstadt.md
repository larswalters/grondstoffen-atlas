# Routebrief (licht) · olie — Triëst (Italië) → TAL via Würmlach (Oostenrijk) → Ingolstadt/Lenting (Duitsland)

**stroom-id:** `olie-trieste-ingolstadt` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**Keten in één zin:** Ruwe olie uit het SIOT-tankenpark bij Triëst (San Dorligo della Valle) per **leiding** — de Transalpine
Pipeline (TAL, 40 inch) via Würmlach, de Felbertauern en Tirol — naar het TAL-tankenpark Lenting bij Ingolstadt (Beieren), 460 km OSM-som in één been, zonder zee.
**Welke as van het verhaal:** *de Zuid-route naar Midden-Europa* — Triëst voedt via één leiding acht raffinaderijen (5 DE, 1 AT, 2 CZ; ~10% van de
Europese bevolking) [3][4]. SIOT loste **41,6 Mt** ruwe olie in 2025 (≈ **835 kb/d**, 422 tankers) [2]; in 2024 40,2 Mt, waarvan Duitsland 28,6 Mt,
Oostenrijk 7,7 Mt, Tsjechië 3,8 Mt [3]. Op dit been (na de Würmlach-aftakking naar Oostenrijk) ≈ 32,4 Mt ≈ **650 kb/d** (2024, eigen omrekening, 7,33 vat/t).
Peiljaar 2025 (kop) / 2024 (been). Herkomst van de Triëster lading: niet gebronnen (§7).

## 1 · Ketenkaart
```
SIOT-tankenpark Triëst `ol-trieste-siot` ──(b1 leiding · TAL 40" · Triëst → Würmlach → Felbertauern → Inndal bij Kufstein → Steinhöring → Lenting ·
   465 km gepubliceerd, 460,5 km OSM, 6 kartering-naden samen 0,85 km)──► TAL-tankenpark Lenting `ol-ingolstadt-tal` ── stoppunt
```
Geen zeebeen (geen bron voor de oorsprong van de lading). De aftakkingen naar Oostenrijk (AWP, Würmlach), Karlsruhe (MiRO, 266 km), Neustadt/Vohburg en
Kralupy–Litvínov vallen buiten de keten.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | SIOT-tankenpark Triëst → TAL-tankenpark Lenting | Transalpine Pipeline / Oleodotto Transalpino / Transalpine Ölleitung | 465 [1][5]; OSM 460,5 (−1,0%) [6] | 19 OSM-ways, `man_made=pipeline substance=oil`, `maak_leidingbeen_olie_trieste_ingolstadt.py` | nee — 6 naden (310, 51, 324, 66, 61, 38 m = 0,85 km) recht verbonden, geen netgat (ondergrondse leiding) |

OSM-ways in reisvolgorde: 290402363 (45,2 km, IT) · 145229247 · 1094455052 · 1094455053 · 432760339 (92,0 km, naar Würmlach/Plöckenpas) · 1333438686 (59,4 km, AT) · 1333706121 ·
1333706120 · 1333706119 · 1333706123 · 1333706124 · 1333706125 · 158910168 (73,5 km, AT→DE) · 168056656 · 168224409 · 168224405 · 155702494 · 169707479 (47,0 km) · 39856317 (3,1 km, eind).
**Niet** 171571174 (16 km zijtak naar het oosten, eindigt op hetzelfde eindpunt). Geen fase B/C/D/E: de pijp eindigt in het tankenpark.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-trieste-siot` | kop van de leiding (tankenpark + pompstation) | SIOT-tankenpark, San Dorligo della Valle (Triëst) — OSM-beginknoop van way 290402363 | 45.6026, 13.8313 | [5][6][7] | bron-gelegd (z15 gezien: gebouwtjes/meetstation aan de NW-rand van een uitgestrekt tankenpark met ~20 cilindrische tanks op een beboste helling; Wikipedia-middelpunt van het park 45,6004/13,8409 ligt 0,8 km ZO; ten NW, over de snelweg, ligt een industriezone) |
| `ol-ingolstadt-tal` | eind van de leiding (tankenpark Lenting) | TAL-tankenpark Lenting/Kösching (Ingolstadt) — OSM-eindknoop van way 39856317 | 48.7941, 11.4746 | [5][6][7] | bron-gelegd (z15 gezien: leidingstrook uit het oosten eindigt op de zuidrand van het TAL-tankenpark met 6 tanks (Wikipedia-coördinaat 48,7962/11,4708, 0,4 km NW) en grenst aan de noordkant van een groot raffinaderij-/tankcomplex; akkerland eromheen) |

Sitelaag `olie-sitelaag.json` heeft geen Triëst- of Ingolstadt-site; geen hergebruik mogelijk. `ankers_hergebruik`: geen.

## 4 · Via-punten (leiding: geen corridorkeuze; alleen de kartering-naden)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | naad 1333438686 → 1333706121 (310 m) | 46.9330, 12.5778 → 46.9357, 12.5765 | Osttirol, OSM-hiaat; recht verbonden [6] |
| b1 | 2 | naad 1333706121 → 1333706120 (51 m) | 47.0473, 12.5155 → 47.0476, 12.5151 | Hohe Tauern, Felbertauern-zone (7,3 km tunnel volgens [5]); OSM-hiaat [6] |
| b1 | 3 | naad 1333706125 → 158910168 (324 m) | 47.5277, 12.1738 → 47.5276, 12.1695 | Inndal ten zuiden van Kufstein; OSM-hiaat [6] |
| b1 | 4 | naad 158910168 → 168056656 (66 m) | 48.1057, 12.0508 → 48.1063, 12.0508 | nabij pompstation Steinhöring (Wikipedia 48,1068/12,0457, ~0,4 km W) [5][6] |
| b1 | 5 | naad 168224405 → 155702494 (61 m) | 48.3929, 11.9395 → 48.3934, 11.9391 | Oberbayern, OSM-hiaat [6] |
| b1 | 6 | naad 155702494 → 169707479 (38 m) | 48.4807, 11.8748 → 48.4809, 11.8745 | Oberbayern (Landkreis Freising), OSM-hiaat [6] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| SIOT-tankenpark San Dorligo/Terminale Marino Triëst | SIOT (Società Italiana per l'Oleodotto Transalpino) | tankers → opslag 2.000.000 m3 → TAL | doorzet 41,6 Mt (2025); operationele capaciteit ~46 Mt; Suezmax aan Jetty 1; TAL+ afgerond [2][3][5] | [2][3][5] |
| TAL-tankenpark Lenting | Deutsche Transalpine Oelleitung GmbH (TAL) | TAL → opslag 318.000 m3 → aftakkingen Neustadt/Vohburg, Gunvor Ingolstadt, MiRO Karlsruhe, Kralupy–Litvínov | 43 Mt/j [1] | [1][5] |

## 6 · Stoppunt
De brief stopt in het TAL-tankenpark Lenting: de leiding eindigt daar en verdeelt de olie over vijf Duitse raffinaderijen en de Tsjechische tak; geen bron koppelt deze lading aan één afnemer of tankerherkomst, dus geen zeebeen vooraf en geen fase D/E erna.

## 7 · Open punten
- **Herkomst van de Triëster lading** (Libië, Azerbeidzjan, Kazachstan, Irak?) niet gebronnen; het tankenpark is het begin, de zee vóór Triëst wordt niet getekend.
- **Kade (Terminale Marino, Zaule-baai)** niet gelegd: geen bron-gelegd kadepunt; de verbinding kade → tankenpark (pijp) is niet gekarteerd en niet getekend.
- **Volume per been** is afgeleid: 650 kb/d = Duitsland + Tsjechië 2024 (28,6 + 3,8 Mt); de kop gaf 835 kb/d in 2025. Eén jaar later dan het been.
- **Naden:** 6 OSM-hiaten (0,85 km) als doorgetrokken lijn gestikt; of dit kartering-omissies zijn is aangenomen (ondergrondse leiding, `location=underground`), niet onafhankelijk bevestigd.
- **Eindanker** ligt op de rand tussen TAL-park en raffinaderijcomplex; welk bedrijf het zuidelijke complex exploiteert (Gunvor Ingolstadt?) is niet bevestigd.
- De ±15%-toets is hier een echte norm: 465 km is een gepubliceerde leidinglengte (geen hemelsbreed); OSM 460,5 km.

## 8 · Bronnen
[1] Wikipedia, "Transalpine Pipeline" — 465 km, 40", capaciteit ~43 Mt/j, 34,9 Mt in 2012. https://en.wikipedia.org/wiki/Transalpine_Pipeline
[2] Adria Ports / Port of Trieste, 2025 — SIOT 41,6 Mt, 422 tankers, +3,5%, TAL+ afgerond. https://www.adriaports.com/en/?p=37607
[3] Il Nordest, SIOT-interview — 2024: 40+ Mt, DE 28,6 / AT 7,7 / CZ 3,8 Mt; 8 raffinaderijen; capaciteit ~46 Mt. https://www.ilnordest.it/economia/imprese/siot-a-pieno-regime-dal-prossimo-anno-priorita-alla-sicurezza-qysdjfof
[4] Ports Europe — SIOT 40,2 Mt in 2024. https://portseurope.com/siot-handles-over-40-2-mln-tons-of-crude-oil-in-trieste-port
[5] Wikipedia (de), "Transalpine Ölleitung" — 465 km, 10 pompstations, tankparken Triëst 2.000.000 m3 en Lenting 318.000 m3 (coördinaten 45,6004/13,8409 en 48,7962/11,4708), raffinaderijen, eigenaren. https://de.wikipedia.org/wiki/Transalpine_Ölleitung
[6] OpenStreetMap-API (ODbL), way-ids hierboven (`name=Oleodotto Transalpino / Transalpine Ölleitung`, `operator=SIOT / Transalpine Ölleitung in Österreich`, `diameter=40"`). https://api.openstreetmap.org/api/0.6/ways.json?ways=290402363,39856317
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-olie-trieste-ingolstadt-siot-tankenpark.png`, `sat-olie-trieste-ingolstadt-tal-ingolstadt.png`.
[8] TAL / SIOT — https://www.tal-oil.com/ (alleen navigatie; geen cijfers).

## 9 · Gebakken

**Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)** · `bash v2/tools/bak_stromen.sh olie-trieste-ingolstadt` (functie `bak_olie_trieste_ingolstadt`) → `v2/data/stroomroute-olie-trieste-ingolstadt.json` (36,8 KB, versie 2, lonlat).

| # | modaliteit | been | km | stippel |
|---|---|---|---|---|
| 1 | leiding | Transalpine Pipeline (TAL, 40 inch) SIOT-tankenpark Triëst → Würmlach → Felbertauern → TAL-tankenpark Lenting/Ingolstadt | 460,5 (1865 punten) | nee |

Totaal 460,5 km tegen 465 gepubliceerd (-1,0%, binnen de ±15%-norm, een echte leidinglengte). Eén been, dus geen naden tussen benen. Markers: 2 (`ol-trieste-siot` 45.6026,13.8313 en `ol-ingolstadt-tal` 48.7941,11.4746), beide 0,002-0,003 km van de lijn (de lijn begint en eindigt op de ankers).

**Recept.** Geen zee, geen router, geen wegscan, geen haven-aanloop, geen stippel, geen kopie. `hecht_marnet.py route` met één `--been-geojson "leiding|…|$BEEN/olie-trieste-ingolstadt-leiding.geojson"` (FeatureCollection, 1 LineString, 19 OSM-ways gestikt door `maak_leidingbeen_olie_trieste_ingolstadt.py`) en twee `--marker`. De lijn is vooraf gebakken en niet over de graaf geroutet.

**Toelichting leiding.** `man_made=pipeline substance=oil`, 40 inch, in OSM volledig gekarteerd; daarom doorgetrokken. De 6 kartering-naden (310, 51, 324, 66, 61, 38 m = 0,85 km) zijn recht verbonden en zitten in de 460,5 km; de leiding ligt ondergronds (Felbertauern-zone: 7,3 km tunnel volgens [5]), dus dit is een kartering-hiaat en geen netgat. Niet bevestigd dat het omissies zijn (§7).

**Toets (handleiding §5).** `json.load` ok, versie 2, `punt_formaat` lonlat, modaliteit {leiding}, 1865 punten, 36,8 KB. `toets_knikken.py`: 24 knikken >= 60 gr, 1 omkering >= 150 gr (154,6 gr op 47.3873,12.4185, Hohe Tauern, "echt (v=1.1)"), 0 terugloop; de rest zijn spikes in de OSM-leidinggeometrie in berggebied. `toets_rechte_benen.py --min-km 5`: geen treffer voor deze stroom.

**Titel.** Het eindpunt valt uit zoals het id belooft (Ingolstadt); geen afwijking van het ontwerp.

**Lessen.** (1) Een leidingbeen dat al als FeatureCollection op schijf staat vraagt alleen een functie met `--been-geojson` en markers: geen slot-zware wegscan nodig, de bake duurt ~1 minuut (zwaar-slot).
