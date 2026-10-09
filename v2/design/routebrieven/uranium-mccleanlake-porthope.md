# Routebrief (licht) · uranium — Cigar Lake/McClean Lake → Blind River → Port Hope (Canada)

**stroom-id:** `uranium-mccleanlake-porthope` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** ertsslurry uit de Cigar Lake-mijn (Cameco/Orano-JV, Athabasca-bekken) per **truck** naar de McClean Lake-mill (Orano), uraanconcentraat (yellowcake) per **truck** over Hwy 905 → 102 → 2 en de Yellowhead/Trans-Canada naar de Blind River-raffinaderij, UO3 per truck naar de Port Hope Conversion Facility (Cameco, Ontario).
**Welke as van het verhaal:** de tweede Canadese ertsstroom naar het Blind River/Port Hope-knooppunt (naast `uranium-mcarthurriver-porthope`): Blind River neemt concentraat van mijnen wereldwijd, niet alleen van Key Lake [8]. Cigar Lake/McClean Lake ≈ 7.100 t U/j (2024, 100%-basis, sitelaag `w-cigarlake`, Cameco AR 2024) [12]; Port Hope vergund tot 12.500 t U/j als UF6 [10 §5]. Geen gescheiden cijfer voor het deel dat Port Hope bereikt.

## 1 · Ketenkaart
```
Cigar Lake-mijn `u-cigarlake-mijn` ──(b1 A truck · mijnweg → Hwy 905, ertsslurry · ~70–80 km)──► McClean Lake-mill `u-mccleanlake-mill`
  ──(b2 B truck · Hwy 905 → Hwy 102 → La Ronge → Hwy 2 · ~505 km)──► Hwy 2/165-knooppunt Weyakwin (via-punt, geen anker)
  ──(b3 B truck · Hwy 2 → Prince Albert → Yorkton → Winnipeg → Thunder Bay → Wawa → Sault Ste. Marie · LETTERLIJKE KOPIE McArthur-b2, vanaf Weyakwin)──► Blind River `u-blindriver-raffinaderij`
  ──(b4 C truck · Hwy 17/69/400/401 · 600 km · LETTERLIJKE KOPIE McArthur-b3)──► Port Hope Conversion Facility `u-porthope-conversie` ── stoppunt
```
⚠️ **Afwijking van het ontwerp en de haalbaarheidstoets:** de kopie van McArthur-b2 begint niet bij Points North Landing maar bij het Hwy 2/165-knooppunt Weyakwin (vertex 1259 van dat been). Reden: Points North ligt niet op de route (b1 passeert op ~5 km, b2 op ~14 km) en McArthur-b2 loopt via Pinehouse/Hwy 165 — aanhechten bij Pinehouse zou ~110 km heen-en-terug over Hwy 165 kosten. De kern van de toets (wegverbinding mill → Hwy 905/102 apart toetsen, anders stippel) is uitgevoerd: OSM geeft een doorgaand wegpad, dus géén stippel.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Cigar Lake-mijn → McClean Lake-mill | mijnweg (OSM way 334756939) → Hwy 905 → millweg | ~70 [1] / ~80 [11] | maak_stroombeen_weg (extract canada) | nee |
| b2 | B | truck | McClean Lake-mill → Hwy 2/165 Weyakwin | Hwy 905 (242 km tot Rabbit Lake-kruising) → Hwy 102 (221 km, ~199 vanaf de 905-aansluiting) → La Ronge → Hwy 2; aannemelijk: één bron voor de bestemming Blind River | ~441 + ~22 millweg + ~45 hemelsbreed, geen wegkm [4][5][7] | maak_stroombeen_weg (extract canada) | nee |
| b3 | B | truck | Weyakwin → Blind River-raffinaderij | Hwy 2 → Yellowhead/Trans-Canada 1/17 (**gedeeld, letterlijke kopie** van `uranium-mcarthurriver-porthope` b2 vanaf vertex 1259) | ~3.000 Saskatchewan→Ontario [11] (heel b1–b3 3.159 km) | kopie geojson | nee |
| b4 | C | truck | Blind River → Port Hope | Hwy 17 → 69 → 400 → 401 (**gedeeld, letterlijke kopie** van McArthur-b3) | 600 [11] | kopie geojson | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-cigarlake-mijn` | mijn (kop) | Cigar Lake-mijn (Cameco 54,5% operator / Orano / overige) | 58.0686, -104.5406 | [1][12] | bron-gelegd (z15 gezien: mijn- en verwerkingscomplex met hallen, koelinstallatie, tailings-/waterbekkens en wegen in het boreale woud; kruis op het hoofdcomplex) |
| `u-mccleanlake-mill` | mill (slurry → yellowcake) | McClean Lake-mill (Orano) | 58.3399, -103.8345 | [7] (OSM way 295492082, landuse "works", operator Orano) | bron-gelegd (z15 gezien: mill-gebouwen met reagenstanks en een ronde JEB-tailingsfaciliteit direct NW; toegangsweg zuidwaarts) |
| `u-blindriver-raffinaderij` | raffinaderij | Blind River Refinery (Cameco), 328 Eldorado Road | 46.1810, -83.0174 | hergebruik letterlijk uit `uranium-mcarthurriver-porthope` §3 [10] | bron-gelegd (z15 daar gezien: omheind fabrieksterrein aan de North Channel) |
| `u-porthope-conversie` | conversie | Port Hope Conversion Facility (Cameco), 1 Eldorado Place | 43.9437, -78.2955 | idem [10] | bron-gelegd (z15 daar gezien: compact terrein aan Lake Ontario) |
Haven-aanloop: n.v.t. (geen zee). Beelden: `v2/build-cache/satcheck/sat-uranium-mccleanlake-porthope-{cigarlake-anker,mccleanlake-anker,sitelaag-mcclean}.png` (+ `-cigarlake`, `-mccleanlake-mill`).

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Hwy 905/102-aansluiting (OSM-knoop, ~22 km ZW van Southend) | 56.2643, -103.5545 | enige noord-zuidverbinding: 905 eindigt hier op Hwy 102 [4] |
| b2 | 2 | La Ronge (Hwy 102/2) | 55.1005, -105.2900 | hergebruik uit McArthur-brief; 102 mondt hier uit op Hwy 2 |
| b2 | 3 | Hwy 2/165-knooppunt Weyakwin | 54.7494, -105.6405 | exact vertex 1259 van McArthur-b2: hier sluit de gedeelde kopie naadloos aan |
| b3 | — | Prince Albert · Yorkton · Winnipeg · Thunder Bay · Wawa · Sault Ste. Marie | zie McArthur-brief §4 | ongewijzigd overgenomen (kopie); **Saskatoon wordt in de geometrie niet aangedaan** (dichtste punt 61 km) |
| b4 | — | Sudbury · Parry Sound · Barrie · Vaughan | zie McArthur-brief §4 | ongewijzigd overgenomen (kopie) |
b1 heeft geen via-punten (geen corridorkeuze); Points North Landing (58.2767, -104.0825) is bewust geen via-punt.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| McClean Lake-mill | Orano (operator) | ertsslurry Cigar Lake → yellowcake | Cigar Lake ≈ 7.100 t U/j (100%) | [1][3][12] |
| Blind River | Cameco | concentraat wereldwijd → UO3 | 's werelds grootste commerciële uraanraffinaderij | [8][10] |
| Port Hope Conversion | Cameco | UO3 → UF6 + UO2 | vergund 12.500 t U/j als UF6 | [10] |

## 6 · Stoppunt
De brief stopt bij Port Hope: daarna splitst de lading in UF6 voor verrijking elders en UO2 voor CANDU (al getekend in `uranium-mcarthurriver-porthope`); fase D/E vervallen, geen bron koppelt Cigar Lake-uranium aan een afnemer.

## 7 · Open punten
- **Geen bron voor het traject McClean Lake → Blind River.** Cameco zegt alleen dat Blind River concentraat van mijnen wereldwijd ontvangt [8]; het concentraat gaat naar de JV-partners/kopers [9]. Het aandeel van Orano (en andere partners) hoeft niet naar Blind River te gaan; alleen het Cameco-deel is aannemelijk (institutionele afleiding, "aannemelijk: één bron" in de beennaam).
- b1-lengte: Cameco noemt ~70 km [1], eerdere opgave ~80 km [11]; gemeten 80,1 km (+14% / +0,1%).
- b2: wegkm alleen voor Hwy 905/102 (Wikipedia); het stuk La Ronge–Weyakwin is hemelsbreed, geen wegkm; gemeten 514,1 km tegen ~505 (+1,8%).
- b3 komt niet door Saskatoon (61 km ernaast), terwijl de beennaam van McArthur-b2 "via Saskatoon" noemt en Watershed Sentinel "trucked to Saskatoon" zegt. Bestaand been, niet aangeraakt — te beoordelen bij de centrale controle.
- Sitelaag `w-cigarlake`: het gecombineerde punt 58.0686/-104.5406 is de mijn; het in de notitie genoemde mill-punt 58.2676/-103.7972 ligt op een wit afvalgesteente-/tailingsterrein, ~8 km ZO van de echte mill (58.3399/-103.8345). Niet aangepast (sitelagen zijn centraal).
- Historisch plan: deel van de Cigar Lake-oplossing naar de Rabbit Lake-mill (CIM 2004) [14]; huidige praktijk niet gecontroleerd.
- Eigendom Cigar Lake: Cameco 54,5% (eind 2025) [1] tegen 50% in de sitelaag.

## 8 · Bronnen
[1] Cameco, Cigar Lake (erts per truck naar Orano's McClean Lake-mill, ~70 km; Cameco 54,5%; 58.068707, -104.538177). https://www.cameco.com/businesses/uranium-operations/canada/cigar-lake
[2] Industrial Info, Cigar Lake-berichten (slurry per truck ~70 km naar McClean). https://www.industrialinfo.com/iirenergy/industry-news/article/camecos-cigar-lake-uranium-mine-now-operational-in-saskatchewan--241166
[3] Wikipedia, McClean Lake mine (mine/mill, JEB-pit als tailingsfaciliteit; 58.2611, -103.8025). https://en.wikipedia.org/wiki/McClean_Lake_mine
[4] Wikipedia, Saskatchewan Highway 905 (begint bij Hwy 102, 22 km ZW van Southend; 242 km tot Rabbit Lake-kruising; Points North +33 km). https://en.wikipedia.org/wiki/Saskatchewan_Highway_905
[5] Wikipedia, Saskatchewan Highway 102 (La Ronge–Southend, ~221 km). https://en.wikipedia.org/wiki/Saskatchewan_Highway_102
[6] Wikipedia, Points North Landing (58.27667, -104.0825). https://en.wikipedia.org/wiki/Points_North_Landing
[7] OpenStreetMap via Nominatim: way 295492082 "McClean Lake mill" (operator Orano) 58.34164, -103.83276; way 334756939 (unclassified, unpaved) 58.15504, -104.25887. https://www.openstreetmap.org
[8] Cameco / CNSC, Blind River Refinery (concentraat van mijnen wereldwijd → UO3 → Port Hope). https://www.cnsc-ccsn.gc.ca/eng/uranium/processing/nuclear-facilities/blind-river/
[9] Globe and Mail via Stockwatch, 2026-07-06 (Cigar Lake 660 km NO van Saskatoon; concentraat naar kopers in Ontario, VS, Europa, Azië). https://wwww.stockwatch.com/News/Item/Z-C!CCO-3838591/C/CCO
[10] `v2/design/routebrieven/uranium-mcarthurriver-porthope.md` §2–§5, §7, §9 (ankers, via-punten, kopieerbare benen; bronnen daar [2][8][9]).
[11] Watershed Sentinel, "On the Yellowcake Trail Part Two" (~3.000 km Saskatchewan→Ontario; 600 km Blind River→Port Hope) via [10]; ~80 km slurrytransport volgens het ketenontwerp.
[12] `v2/design/uranium-sitelaag.json`, site `w-cigarlake` (capaciteit, coördinaat, status aannemelijk).
[13] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15), bestanden `sat-uranium-mccleanlake-porthope-*.png`.
[14] CIM, "The Cigar Lake project — mining, ore handling and milling" (2004). https://www.onemine.org/documents/the-cigar-lake-project-mining-ore-handling-and-milling-1463a4ec-6903-4c1d-b800-831570ba9799-

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Recept:** `bash v2/tools/bak_stromen.sh uranium-mccleanlake-porthope` (functie `bak_uranium_mccleanlake_porthope`, vier `--been-geojson` truck, geen stippel, vier markers) → `v2/data/stroomroute-uranium-mccleanlake-porthope.json` (473,9 KB, versie 2, `lonlat`, 23.072 punten). Wegprofielen b1/b2 in `maak_stroombeen_weg.py` (`uranium-mccleanlake-porthope-cigarlake-mccleanlake`, `…-mccleanlake-hwy2`), extract `canada`, scan via het weg-/reus-slot in een eerdere poging; hier hergebruikt (tussenuitvoer volledig, ankers en naden gecontroleerd).

| been | fase | modaliteit | km gemeten | km brief | afwijking | naad | opmerking |
|---|---|---|---|---|---|---|---|
| b1 Cigar Lake → McClean Lake | A | truck | 80,2 | ~80 [11] (Cameco nu ~70 [1]) | +0,3% tegen 80; +14% tegen 70 | — | binnen ±15% |
| b2 McClean Lake → Weyakwin (Hwy 905/102/2) | B | truck | 514,1 | ~505 (441 wegkm + 22 millweg + 45 hemelsbreed, geen wegkm) | +1,8% | 0,00 km | indicatie, geen norm: het stuk La Ronge–Weyakwin heeft alleen een hemelsbrede schatting |
| b3 Weyakwin → Blind River | B | truck | 2.565,1 | ~3.000 Saskatchewan→Ontario (Key Lake, [11]) | n.v.t. (kopie; b1–b3 samen 3.159) | 0,00 km | LETTERLIJKE KOPIE McArthur-b2 vanaf vertex 1259 |
| b4 Blind River → Port Hope | C | truck | 644,1 | 600 [11] | +7,3% | 0,00 km | LETTERLIJKE KOPIE McArthur-b3 |
Totaal **3.803,5 km**, 4 benen, geen stippel, 4 markers, alle op 0 m van de lijn (anker = routeerpunt). Hoogste naad 0,00 km.

**Toelichting.** Geen stippel, geen haven-aanloop, geen vlucht, geen leiding: alle vier de benen zijn openbare weg of mijnweg tot op het anker. b3 is de in de cache bewaarde slice `uranium-mccleanlake-porthope-weg-hwy2-blindriver.geojson` (coördinaten == McArthur-b2[1259:], opnieuw geverifieerd: gelijk); b4 verwijst direct naar het McArthur-bestand, niet gekopieerd. b2 eindigt exact op de McArthur-vertex (54.749415, -105.640502), dus de kopie sluit naadloos aan. Aannemelijk (één bron, geen bron voor McClean → Blind River): staat in de beennaam van b2, niet in de lijnstijl.

**Toets.** `toets_knikken`: 49 knikken ≥ 60°, 2 omkeringen (beide in de gekopieerde b4: 174° bij 43.7167,-79.5188 en 157° bij 44.3993,-79.6985, scherpe bochten met verhouding 1,2, geen terugloop), eigen b1/b2 geen omkering. `toets_rechte_benen` meldt geen recht been (omwegfactoren 1,24–1,57 hemelsbreed). Markers 0 m van hun lijn.

**Bevindingen / lessen.**
- b3 passeert Saskatoon niet (dichtste punt 61,8 km), terwijl de beennaam van McArthur-b2 "via Saskatoon" noemt; hier is de naam bewust zonder Saskatoon gehouden. Bestaand been, niet aangeraakt: centraal beoordelen.
- Sitelaag `w-cigarlake`: het mill-punt 58.2676/-103.7972 ligt ~8 km van de echte mill (58.3399/-103.8345); niet gewijzigd (sitelagen zijn centraal).
- Het stroom-id noemt `porthope` als eindpunt en dat klopt: de lijn eindigt op Port Hope Conversion Facility (43.9437, -78.2955).
- Registerregel voor centraal: sleutel `u-mc` (vrij; bezet: u-ip, u-mp, u-rw, u-ac, u-is, u-pa, u-op, u-sm, u-jh, u-mt, u-ka, u-ps, u-ec).
