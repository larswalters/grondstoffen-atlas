# Routebrief (licht) · olie — Fos-sur-Mer (SPSE) → Lyon → Feyzin (Frankrijk)

**stroom-id:** `olie-fos-feyzin` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) · **status:** gebakken
**Keten in één zin:** Ruwe olie uit het SPSE-tankenpark bij Fos-sur-Mer (Middellandse-Zeekant van Europa) per **leiding** — de
Pipeline Sud-Européen (SPSE) door de Crau en de Rhônevallei — naar de SPSE-aflevering Lyon en de aftak naar de raffinaderij Feyzin
(TotalEnergies) bij Lyon; ~281 km, geen zee, 5,5% stippel.
**Welke as van het verhaal:** *de Rhône-as van de Middellandse Zee naar het binnenland* — de eerste Franse keten. Feyzin verwerkt
ca. **105 kb/d** (capaciteit, Argus; ≈ 5,4–5,6 Mt/j, Conseil des énergies, peiljaar ~2025) [6][7]; de brief weet niet welk deel via de
SPSE komt (Lyon Capitale: het brut komt per pijp uit Fos) [8]. Het hele SPSE-systeem: 23 Mt/j feitelijk (en.wikipedia, ongedateerd) of
10 Mt/j (fr.wikipedia) — een bronconflict, zie §7 [1][3]. Eenheid kb/d; 105 kb/d is capaciteit van de afnemer, geen leidingdoorzet.

## 1 · Ketenkaart
```
SPSE-tankenpark Fos-sur-Mer `ol-fos-spse` ──(b1 leiding · SPSE via Crau → Rhône-kruising [stippel 10,8 km] → Drôme/Isère →
   Lyon-aflevering `ol-lyon-aflevering` → TRC-aftak [stippel 4,6 km] · 281 km, 260 gepubliceerd)──►
   Raffinerie Feyzin (TotalEnergies) `ol-feyzin-ref` ── stoppunt
```
Geen zeebeen (geen bron voor de herkomst van de lading; het tankenpark is de kop). Aftakken naar Besançon/Cressier en Strasbourg
vallen buiten de keten.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | SPSE-tankenpark Fos → raffinerie Feyzin | Pipeline Sud-Européen (SPSE, 34" PL1) → TRC HC 16" | 260 (Fos–Feyzin 24", [1]); gemeten 265,7 doorgetrokken + 15,4 stippel = 281,1 (+8,1%) [9] | OSM-ways `man_made=pipeline substance=oil` (3 stukken, `maak_leidingbeen_olie_fos_feyzin.py`) | ja, 2 stukken: 10,8 km (Rhône-kruising, geen OSM) en 4,6 km (aftak Lyon-aflevering → Feyzin, niet doorlopend gekarteerd); ook ca. 0,3 km recht gestikt bij de Lyon-aflevering |

OSM-ways in reisvolgorde (alle `operator=Société du Pipeline Sud-Européen`, ondergronds [9]):
- stuk A (40,6 km): 420942590 (4,2 km, tankenpark Fos → noordwaarts, omgekeerd) + 232593022 vanaf 43.4988,4.8932 (de eerste 5 vertices zijn een zijtak naar een logistiek park en vallen af);
- **stippel 1** 43.7942,4.8946 → 43.8894,4.9229 (10,8 km);
- stuk B (223,8 km): 232593024 (105,1) · 514120690 (32,2, "SPSE PL1 34\"") · 232717968 (40,0) · 457397239 · 457397240 (afgekapt bij de Lyon-aflevering, ~30 km) · naad 0,3 km · 1328508024 (TRC HC 16", oil, 17,6 km) tot 45.6478,4.9157;
- **stippel 2** 45.6478,4.9157 → 45.6604,4.8592 (4,6 km);
- stuk C (1,3 km): 232080899 (oil, bron Bing) 45.6604,4.8592 → 45.6625,4.8430.
Niet gebruikt: 457397240 voorbij de Lyon-aflevering (richting Besançon/Jura, 230 km), 232593022-zijtak, SPMR/Trapil (producten, `substance=fuel`), TRC HC 10" 232080898 (parallel aan het 16"-stuk).
Extracts: `fr-provence-alpes-cote-d-azur`, `fr-rhone-alpes` (beide lokaal aanwezig).

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-fos-spse` | kop van de leiding (tankenpark, 40 tanks / 2,26 Mm3) | SPSE-tankenpark Fos-sur-Mer — OSM-eind van way 420942590 | 43.4649, 4.9165 | [1][2][9][10] | bron-gelegd (z15/z16 gezien: twee grote tankenparken met tientallen cilindrische tanks langs de weg bij Fos; de leiding eindigt bij pomp-/afsluitergebouwen aan de zuidwesthoek van het noordoostelijke park; Wikipedia-punt 43.4625,4.9144 ligt 0,4 km ZW in het gebouwencluster tussen beide parken) |
| `ol-lyon-aflevering` | splitsing hoofdleiding en aftak, SPSE-aflevering Lyon | tankenpark oost van Lyon — begin TRC HC 16" (way 1328508024) | 45.6159, 5.1145 | [2][9][10] | bron-gelegd (z15 gezien: 9–11 grote tanks in een omwald park midden in akkers en bos; de leiding komt aan de noordrand; hoofdleiding 457397240 loopt ~0,3 km verder noord) |
| `ol-feyzin-ref` | eind van de leiding / raffinaderij | Raffinerie Feyzin (TotalEnergies) — OSM-eind way 232080899, oostrand zuidelijk tankenpark | 45.6625, 4.8430 | [4][5][9][10] | bron-gelegd (z16 gezien: groot tankenpark + procesinstallaties tussen Rhône-kanaal en A7; het punt ligt aan de A7-zijde van het zuidelijke tankenpark; Wikipedia-middelpunt 45.6719,4.8431 is 1,1 km noordelijker) |

Sitelaag `olie-sitelaag.json` heeft geen Fos- of Feyzin-site; geen hergebruik mogelijk. `ankers_hergebruik`: geen.

## 4 · Via-punten (leiding: geen corridorkeuze; alleen de segmentovergangen en gaten)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | OSM-knoop 420942590 → 232593022 | 43.4988, 4.8932 | tankenpark verbindt hier met de SPSE-hoofdlijn [9] |
| b1 | 2 | begin stippel 1 | 43.7942, 4.8946 | laatste OSM-punt vóór het gat bij de Rhône-kruising |
| b1 | 3 | einde stippel 1 | 43.8894, 4.9229 | OSM-lijn hervat (232593024) |
| b1 | 4 | 232593024 → 514120690 | 44.7798, 4.9621 | naad tussen ways; PL1 34" [9] |
| b1 | 5 | 514120690 → 232717968 | 45.0537, 4.9340 | wayovergang |
| b1 | 6 | 457397240 → TRC | 45.6159, 5.1145 | Lyon-aflevering; hier takt de aftak naar Feyzin af |
| b1 | 7 | begin stippel 2 | 45.6478, 4.9157 | einde TRC HC 16" |
| b1 | 8 | einde stippel 2 | 45.6604, 4.8592 | begin OSM-way 232080899 |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| SPSE-terminal Fos-sur-Mer | Société du Pipeline Sud-Européen (Total 35%, ExxonMobil 22%, SPITP 16%, Shell 13%, BP 12%, Phillips 66 2%) | tankers (tot 400.000 t) → 40 tanks → leiding | 2,26 Mm3 opslag; lossen 15.000 m3/u; 34"-lijn tot 2.600 m3/u (≈ 390 kb/d) [2][3] | [2][3] |
| Raffinerie Feyzin | TotalEnergies | ruwe olie (SPSE) → brandstoffen, petrochemie | 105 kb/d / 5,4–5,6 Mt/j; "Seveso hoog", reconversie loopt, geen sluiting (toets mei 2026) [6][7][11] | [4][6][7] |

## 6 · Stoppunt
De brief stopt in de raffinaderij Feyzin: de leiding eindigt daar en geen bron noemt een volgende afnemer van deze lading; geen
zeebeen vooraf (geen bron voor de tankerherkomst in Fos), geen fase D/E erna.

## 7 · Open punten
- **Twee stippels samen 15,4 km (5,5%):** Rhône-kruising 10,8 km en aftak Lyon-aflevering → Feyzin 4,6 km zijn niet in OSM gekarteerd; geen bron noemt het exacte tracé.
- **Bronconflict 24"-lijn:** fr.wikipedia noemt de 24" Fos–Lyon "actuellement inactive" [3]; en.wikipedia en spse.fr laten Feyzin via Lyon bevoorraden [1][2]. De OSM-ways die we volgen zijn de 34"-lijn (way 514120690) — welke lijn feitelijk Feyzin voedt is niet vastgesteld.
- **Volume:** 105 kb/d is de capaciteit van Feyzin (Argus, ongedateerd) [7]; welk deel via de SPSE komt is niet gebronnen; SPSE-systeem 10 of 23 Mt/j (bronconflict) [1][3].
- **Km is een echte leidinglengte** (260 km, Wikipedia): de ±15%-toets is hier een norm; 281 km = +8,1% (de leiding volgt de 34"-hoofdlijn tot Lyon en de aftak ligt ~20 km oostelijker dan Feyzin).
- **TRC HC 16"** (en parallel 10") is alleen `substance=oil` getagd; dat het de SPSE-aftak naar Feyzin is, volgt uit het begin op 0,3 km van de SPSE-hoofdlijn bij het Lyon-tankenpark en het eind 6 km oostelijk van Feyzin — niet in een bron bevestigd.
- Eindanker ligt op de A7-rand van het raffinaderijterrein; het exacte aansluitpunt in het terrein is niet gevonden.

## 8 · Bronnen
[1] Wikipedia, "South European Pipeline" — Fos–Feyzin 24", 260 km; systeem 23 Mt/j feitelijk, 35 Mt/j max. https://en.wikipedia.org/wiki/South_European_Pipeline
[2] SPSE — 34", 2.600 m3/u; Fos-opslag 2,26 Mm3, 40 tanks; aflevering Lyon voor Feyzin. https://www.spse.fr/en/transportation-and-storage-of-petroleum-products.php
[3] Wikipedia (fr), "Oléoduc sud-européen" — 40 tanks 2,26 Mm3, 24" Fos–Lyon "inactive", aandeelhouders, 10 Mt/j. https://fr.wikipedia.org/wiki/Ol%C3%A9oduc_sud-europ%C3%A9en
[4] Wikipedia, "Feyzin Refinery" — TotalEnergies, 45.674/4.844, op de SPSE. https://en.wikipedia.org/wiki/Feyzin_Refinery
[5] Wikipedia (fr), "Raffinerie de Feyzin" — coördinaat 45,67194/4,84306, in dienst, Seveso hoog. https://fr.wikipedia.org/wiki/Raffinerie_de_Feyzin
[6] Connaissance des énergies — Feyzin ~5,6 Mt brut/j. https://www.connaissancedesenergies.org/les-raffineries-francaises-en-images
[7] Argus Media — Feyzin 105.000 b/d (herstart na brand). https://www.argusmedia.com/es/news-and-insights/latest-market-news/2266842-france-s-feyzin-refinery-restarts-crude-runs
[8] Lyon Capitale — brut via pijp uit Fos-sur-Mer. https://www.lyoncapitale.fr/Actualite/Carburant-amelioration-dans-le-Rhone-stock-et-menace-de-Total
[9] OpenStreetMap (ODbL), Geofabrik-extracts fr-provence-alpes-cote-d-azur en fr-rhone-alpes; eigen pyosmium-scan 2026-10-31, way-ids in §2.
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16) — `v2/build-cache/satcheck/sat-olie-fos-feyzin-fos-tankenpark.png`, `-spse-eind-oosm.png`, `-lyon-aftak.png`, `-feyzin-raffinaderij.png`, `-feyzin-eind.png`.
[11] Haalbaarheidstoets olie-fos-feyzin (intern, 2026-10-31) — Seveso-fiche mei 2026, reconversie loopt.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)
**Bestand:** `v2/data/stroomroute-olie-fos-feyzin.json` (versie 2, punt_formaat lonlat, 20,1 KB, 1.019 punten, 3 markers). Recept: `bash v2/tools/bak_stromen.sh olie-fos-feyzin` (functie `bak_olie_fos_feyzin`); leiding-geojson uit `python v2/tools/maak_leidingbeen_olie_fos_feyzin.py --schrijf` (pyosmium, cache in `v2/build-cache/ais/graaf/olie-fos-feyzin-*`).

| # | modaliteit | been | km | stijl |
|---|---|---|---|---|
| 1 | leiding | SPSE-tankenpark Fos-sur-Mer naar Rhône-kruising (OSM-ways 420942590 + 232593022) | 40,6 | doorgetrokken |
| 2 | leiding | kartering-gat Rhône-kruising 43.7942,4.8946 naar 43.8894,4.9229 | 10,8 | stippel (OSM heeft hier geen leiding) |
| 3 | leiding | SPSE 34 inch naar Lyon-aflevering en TRC HC 16 inch (OSM-ways 232593024, 514120690, 232717968, 457397239/40, 1328508024) | 223,8 | doorgetrokken |
| 4 | leiding | aftak Lyon-aflevering naar Feyzin 45.6478,4.9157 naar 45.6604,4.8592 | 4,6 | stippel (aftak niet doorlopend gekarteerd) |
| 5 | leiding | laatste stuk in de raffinaderij (OSM-way 232080899) | 1,3 | doorgetrokken |

Totaal 281,1 km: 265,7 km gemeten (94,5%) + 15,4 km stippel (5,5%) tegen 260 km gepubliceerd (Fos-Feyzin 24 inch, Wikipedia): +8,1%, binnen de norm van +-15%.
**Markers (3):** SPSE-tankenpark Fos 43.4649,4.9165; SPSE-aflevering Lyon 45.6159,5.1145; Raffinerie Feyzin 45.6625,4.8430 (alle drie 0,003-0,005 km van de lijn).
**Naden:** 0,001-0,005 km (max 5 m). Geen zee, geen haven-aanloop, geen weg, geen lucht, geen kopie.
**Toelichting stippels:** (1) 10,8 km Rhône-kruising: geen OSM-leiding, rechte lijn tussen de laatste en eerste OSM-punt; (2) 4,6 km aftak: de TRC HC 16 inch eindigt 6 km oost van Feyzin, het stuk tot de OSM-aftak in de raffinaderij is niet gekarteerd. Beide zijn "hier reikt het net niet". De eerste 5 vertices van way 232593022 (zijtak naar een logistiek park) zijn bewust weggelaten.
**Toets:** `toets_knikken`: 10 knikken >= 60 gr (1 omkering 157,8 gr bij de Lyon-aflevering, de leiding buigt daar echt), 0 terugloop; de spikes zijn OSM-vertexruis van ondergrondse leidingen (R 3-150 m) en geen routeringsfout. `toets_rechte_benen --min-km 5`: alleen de Rhône-stippel (10,8 km, bedoeld). json.load en modaliteitencheck in orde.
**Lessen:** (a) een leidingketen is haalbaar als OSM de hoofdlijn heeft; de twee gaten zijn klein en benoemd. (b) Het eindanker ligt op de A7-rand van het terrein, niet in het proces. (c) Open: welke lijn (34 inch of de volgens fr.wikipedia inactieve 24 inch) Feyzin voedt, en het aandeel SPSE in de 105 kb/d.
