# Routebrief (licht) · gas — Ras Laffan (Qatar) → Taweelah (Abu Dhabi, VAE)

**stroom-id:** `gas-raslaffan-taweelah` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken
**Keten in één zin:** Veldgas van het North Field komt via twee 36-inch sealines (80 km) aan land in de Dolphin Energy-gasfabriek
in Ras Laffan, gaat als droog gas de 48-inch Dolphin-exportleiding in (364 km gepubliceerd, 377 km in OSM, geheel door de Golf,
dus zonder Hormuz) en wordt ontvangen in de Dolphin-ontvangstfaciliteit bij Taweelah, naast de Taweelah-centrale, voor Abu Dhabi,
Dubai, de Noordelijke Emiraten en (via Al Ain–Fujairah) Oman.
**Welke as van het verhaal:** *Qatars enige pijpexport, en die loopt niet door Hormuz* — al het andere Qatarese gas (LNG) moet door
de Straat. Volume: ca. 2 bcf/d ≈ 20,7 bcm/j (offshore-technology, ontwerp tot 3,2 bcf/d ≈ 33,1 bcm/j; peiljaar ontwerp 2006/07, geen
meting 2025) [3][4]. Wikipedia noemt ook "90,6 bcm/j" [2]: dat is 3,2 *biljoen* ft³ per jaar uit een bron en rijmt niet met 3,2 bcf/d;
niet gebruikt. Hormuz niet gepasseerd, maar de leiding ligt wel binnen de Golf (conflictrisico: zie §7).

## 1 · Ketenkaart
```
North Field-platforms (offshore, 2×36" sealines, 80 km — geen site-anker, fase A-voorloop vervalt) ──►
Dolphin Energy-gasfabriek Ras Laffan `gas-dolphin-plant` (6 compressietreinen, > 2 bcf/d)
  ──(b1 leiding · onshore uitvoer fabriek → kustovergang · ~8,6 km hemelsbreed, STIPPEL: niet gekarteerd)──►
kustovergang/begin OSM-way `gas-dolphin-landfall` (aannemelijk)
  ──(b2 leiding · Dolphin-exportleiding 48" door de Golf · 377,0 km OSM, doorgetrokken)──►
Dolphin-ontvangstfaciliteit Taweelah `gas-taweelah-ontvangst` — stoppunt, invoeding Abu Dhabi/Dubai/Fujairah/Oman
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-dolphin-plant` → `gas-dolphin-landfall` | onshore Ras Laffan, uitvoer van de fabriek naar het begin van de OSM-leiding | hemelsbreed 8,6 km, geen gepubliceerde lengte | `--stippel` | ja: OSM kent tussen fabriek en way-begin geen verbonden pijpleiding; "geen net op deze korrel" [5][6] |
| b2 | A | leiding | `gas-dolphin-landfall` → `gas-taweelah-ontvangst` | Dolphin-exportleiding, 48", OSM-way 220018254 (operator Dolphin Energy, substance gas, submarine) | 364 [3], 370 [4]; gemeten OSM **377,0** (+3,6% / +1,9%) | vooraf gestikt geojson (`maak_leidingbeen_gas_raslaffan_taweelah.py`) | nee |

OSM-way 220018254 heeft 67 punten (grootste segment 84 km: rechte, ondiepe zeebodemligging, geen kartering-gat). Eind van de way
24.7531, 54.6809 ligt 0,08 km van het Taweelah-anker; onshore Dolphin-pijpstukken daar (ways 1244228105–116) zijn < 1 km, niet getekend.
Totaal getekend 385,6 km; stippel 2,2% van de lengte.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-dolphin-plant` | gasfabriek (kop, ontvangst sealines, compressie) | Dolphin Energy Gas Plant, Ras Laffan | 25.9297, 51.5181 | [2][3][6] | bron-gelegd (z15 gezien: groot omheind procescomplex met rijen proces- en compressietreinen, ten noorden van het woongebied Ras Laffan, kust 1 km noordoostelijk; OSM-landuse "Dolphin Energy Gas Plant", centroïde; Wikipedia-punt 25.9253, 51.5161 ligt 0,5 km zuidwestelijk in hetzelfde complex) |
| `gas-dolphin-landfall` | begin OSM-leiding (kustovergang) | begin way 220018254, Ras Laffan-zuid | 25.8531, 51.5269 | [5] | aannemelijk (z16 gezien: omheinde compound met platforms, spoorbundel en snelweg oostelijk; functie niet bevestigd door een bron, alleen het OSM-begin van de Dolphin-way; ligt 8,6 km ZUIDELIJK van de fabriek) |
| `gas-taweelah-ontvangst` | ontvangstfaciliteit (staart, stoppunt) | Dolphin Taweelah Receiving Facility (3 ontvangsttreinen) | 24.7524, 54.6811 | [3][7] | bron-gelegd (z16 gezien: omheinde compound met pijpleidingmanifolds en gebouwen tussen een waterkanaal en een tankpark met grote ronde tanks, naast het Taweelah-centrale/ontziltingscomplex; OSM-naam "Dolphin Taweelah Receiving Facilty" op een slordig getekend vlak, onshore Dolphin-pijpen 0,05–0,3 km van het punt) |

Hergebruik: geen. De sitelaag-site `w-raslaffan` (25.9265, 51.5955, LNG-complex) ligt 7,7 km oostelijk van de Dolphin-fabriek: niet hergebruiken
als anker. De design-coördinaat 25.8531, 51.5269 ("Dolphin Ras Laffan") is dus het OSM-begin van de leiding en niet de fabriek (afwijking, §7).

## 4 · Via-punten
Niet van toepassing: beide benen zijn leiding (OSM-way of stippel), geen corridorkeuze zoals bij weg/spoor.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Dolphin-gasfabriek Ras Laffan | Dolphin Energy (Mubadala 51%, TotalEnergies 24,5%, Occidental 24,5%) | veldgas + vloeistoffen → droog exportgas; etaan naar QatarEnergy, condensaat/propaan/butaan spot | > 2 bcf/d ≈ > 20,7 bcm/j; 6 compressietreinen | [1][2][3] |
| Taweelah-ontvangstfaciliteit | Dolphin Energy | exportgas → UAE-net (en Al Ain–Fujairah, Oman) | 3 parallelle ontvangsttreinen | [2][3] |

## 6 · Stoppunt
De brief stopt bij de Dolphin-ontvangstfaciliteit Taweelah: daarna is het gas anoniem UAE-netgas (Abu Dhabi, Dubai, Noordelijke Emiraten, Fujairah-
centrale, Oman-contract 200 MMcf/d [3]) en bestaat er geen bron die één molecuul aan één afnemer koppelt. Fase D vervalt: de Taweelah-centrale is
alleen als buur genoemd, niet als gedocumenteerde afnemer van deze stroom; fase E vervalt. Optionele vertakking Taweelah → Jebel Ali (76 km OSM) heeft
geen bron en wordt niet getekend.

## 7 · Open punten
- **Afwijking van het ontwerp:** het ontwerp noemt 25.8531, 51.5269 "Dolphin-ontvangst Ras Laffan"; dat is het OSM-begin van de exportleiding, 8,6 km
  ZUIDELIJK van de gasfabriek (OSM "Dolphin Energy Gas Plant" 25.9297, 51.5181, Wikipedia 25.9253, 51.5161). Daarom een kort stippelbeen b1 fabriek →
  way-begin (< 3% van de lengte); een bron voor het onshore tracé ontbreekt.
- **Functie van `gas-dolphin-landfall` niet bevestigd** (kustovergang, pig-/meetstation of ander terrein): alleen de OSM-begin van de way.
- **Way-identificatie** berust op operator-tag Dolphin Energy, 377,0 km tegen 364/370 gepubliceerd en beide uiteinden op de twee Dolphin-sites (geen onafhankelijke lijnkaart).
- **Gepubliceerde lengte wisselt:** 364 [3] tegen 370 km [4]; OSM-polyline 377,0 km (+3,6 / +1,9%), binnen ±15%.
- **Geen meetjaar voor het volume:** 2 bcf/d is ontwerp/aanvang (2007); Oxy/Dolphin-jaarcijfers niet gevonden. Capaciteit 3,2 bcf/d is niet gelijk aan doorzet.
- **Conflictrisico binnen de Golf (2026):** QatarEnergy stopte LNG op 2 maart 2026 na Iraanse aanvallen op Ras Laffan; GRC meldt op 1 juni 2026 dat de
  Dolphin-leiding "fully operational" bleef en Qatar gas aan UAE en Oman bleef leveren [9]. Geen cijfer voor de actuele doorzet gevonden.
- **Sitelaag mist** de Dolphin-fabriek en de Taweelah-ontvangst; gloedgewicht uit deze brief: ca. 20,7 bcm/j (> 2 bcf/d) per site, aanvulling centraal.
- Het North Field/sealine-deel (2×36", 80 km) is niet gekarteerd en niet getekend: geen site-anker voor het veld.

## 8 · Bronnen
[1] Wikipedia, "Dolphin Energy" — opgericht 1999 door Abu Dhabi; Mubadala 51%, Total 24,5%, Occidental 24,5%. https://en.wikipedia.org/wiki/Dolphin_Energy
[2] Wikipedia, "Dolphin Gas Project" — 2×36" sealines 80 km, 48" exportleiding Ras Laffan–Taweelah, Taweelah-ontvangstfaciliteit, Al Ain–Fujairah 182 km,
    Taweelah–Fujairah 244 km, eerste gas 25-6-2007, fabriekscoördinaat 25°55′31″N 51°30′58″E; het cijfer 90,6 bcm/j is daar inconsistent. https://en.wikipedia.org/wiki/Dolphin_Gas_Project
[3] Offshore Technology, "Dolphin Gas Project, Ras Laffan" — 364 km, 48", tot 2 bcf/d (design 3,2 bcf/d), 6 compressietreinen, 3 ontvangsttreinen naast Taweelah Power Station,
    afnemers UAE, Fujairah, Oman 200 MMcf/d. https://www.offshore-technology.com/projects/dolphin/
[4] Global Energy Monitor wiki, "Dolphin Qatar–UAE Natural Gas Pipeline" — 370 km (infobox) / 364 km, 48", 3.200 MMcf/d, status operating. https://www.gem.wiki/Dolphin_Natural_Gas_Pipeline
[5] OpenStreetMap (ODbL), way 220018254 (man_made=pipeline, operator=Dolphin Energy, substance=gas, submarine=yes), 67 punten, 377,0 km; opgehaald via de OSM-API op 2026-10-09.
    https://www.openstreetmap.org/way/220018254
[6] OpenStreetMap (ODbL), way 223674172 "Dolphin Energy Gas Plant" (landuse=industrial, wikidata Q5289627; bbox 25.9155–25.9343 / 51.5069–51.5237). https://www.openstreetmap.org/way/223674172
[7] OpenStreetMap (ODbL), way 360705059 "Dolphin Taweelah Receiving Facilty" en Dolphin Energy-pijpways 1244228105–116 bij Taweelah. https://www.openstreetmap.org/way/360705059
[8] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-gas-raslaffan-taweelah-dolphinplant.png`, `-raslaffan-dolphin.png`, `-raslaffan-z16.png`,
    `-taweelah-dolphin.png`, `-taweelah-z16.png`, `-dolphin-ontvangst.png`.
[9] Gulf Research Center, "Among the Lessons Learned from the Gulf Crisis & Reference to the Recommendation of the April 2026 Gulf Summit", 1 juni 2026 — Dolphin "fully operational". https://www.grc.net/single-commentary/387

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)

**Bestand:** `v2/data/stroomroute-gas-raslaffan-taweelah.json` (2,2 KB, contract versie 2, lonlat) · **functie:** `bak_gas_raslaffan_taweelah` in `v2/tools/bak_stromen.sh` · **recept:** `bash v2/tools/bak_stromen.sh gas-raslaffan-taweelah` (tussenuitvoer `maak_leidingbeen_gas_raslaffan_taweelah.py` -> `v2/build-cache/ais/graaf/gas-raslaffan-taweelah-leiding-dolphin.geojson`, al aanwezig en hergebruikt).

| # | modaliteit | been | km | naad | stippel |
|---|---|---|---|---|---|
| 1 | leiding | onshore Dolphin Ras Laffan-fabriek -> kustovergang (schematisch, niet gekarteerd) | 8,6 | 0 | ja |
| 2 | leiding | Dolphin-exportleiding 48 inch (OSM-way 220018254) Ras Laffan -> Taweelah | 377,0 | 0,004 | nee |

Totaal 385,6 km, 69 punten, 2 markers (`gas-dolphin-plant` 25.9297, 51.5181 op 0,0 km van de lijn; `gas-taweelah-ontvangst` 24.7524, 54.6811 op 0,09 km). Geen marker voor de kustovergang (brief §3). Geen zee, weg, spoor, lucht, via-punten, haven-aanloop of gedeeld been.

**Toets:** b2 377,0 km tegen 364 [3] / 370 [4] = +3,6% / +1,9%, binnen de +/-15% (OSM-geometrie, geen wegkm). Naden 0 en 0,004 km. `toets_rechte_benen`: alleen b1 recht (stippel met reden). `toets_knikken`: 4 knikken van ca. 89 graden, 0 omkeringen, 0 terugloop, allemaal in de eerste ~10 km van het way-begin bij Ras Laffan (OSM-vertex-geometrie van de onshore stukken, geen echte terugloop).

**Toelichting stippel:** b1 is een rechte lijn van 8,6 km: OSM kent tussen de fabriek en het way-begin geen verbonden pijpleiding ("geen net op deze korrel"); de brief geeft er geen bron voor.

**Bevinding (niet gerepareerd):** de OSM-way begint bij het zuidelijke anker (25.8531, 51.5269), loopt eerst onshore noordwestwaarts en passeert de fabriek op 1,2 km (punt 28, ca. 25.94, 51.52) voordat hij de zee in gaat. De stippel b1 loopt dus fabriek -> zuid, en de leiding loopt daarna weer langs de fabriek terug naar het noorden: visueel een kleine lus van enkele km bij Ras Laffan. Eerlijker zou zijn: de leiding ontspringt feitelijk bij de fabriek; dat vraagt een bron voor het onshore tracé of een centrale keuze om b1 te laten vervallen en de way vanaf de fabriek te laten beginnen. Niet doorgevoerd (buiten de lichte werkwijze).

**Lessen:** (1) een OSM-leiding kan zijn begin elders hebben dan de fabriek; check altijd de eerste ~30 punten tegen het fabrieksanker. (2) `bak_stromen.sh` is LF gebleven (0 CRLF), functie direct voor de ankerregel.
