# Routebrief (licht) · uranium — Orano Tricastin (Pierrelatte) → A7 → A31 → A1/A3 → Framatome ANF Lingen (Duitsland)

**stroom-id:** `uranium-tricastin-lingen` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** verrijkt UF6 uit Georges Besse II (Orano Tricastin, Pierrelatte) gaat per **truck** (alle Lingen-transporten zijn LKW: geen spoor [1]) over de A7 (Rhônedal), de oostelijke rondweg van Lyon (A46), de A6/A31 (Beaune–Dijon–Langres–Nancy–Metz), Luxemburg (A3/A1), de Eifel (A64 Trier, B51/A60, B51, A1), Keulen en de A3/A31 naar de splijtstoffabriek Framatome ANF in Lingen (Ems) — stoppunt.
**Welke as van het verhaal:** *de grootste UF6-aanvoerlijn naar Lingen, over bijna 1.100 km Europese autoweg.* **Volume:** 19 UF6-transporten Tricastin → Lingen in 2017 (urantransport.de) [1]; **tonnage niet gepubliceerd**, indicatie 100-300 t U/j (eigen schatting, geen bronwaarde); eenheid t U/j, peiljaar 2017. In 2022 noemt dezelfde bron Orano Tricastin nog als UF6-leverancier, zonder aantal [1].

## 1 · Ketenkaart
```
Orano Tricastin — Georges Besse II (verrijking), Pierrelatte `u-tricastin`
  ──(b1 D truck · A7 → A46 (Lyon-oost) → A6 → A31 → A3/A1 Luxemburg → A64/B51/A60/B51 → A1 → A3 → A31 → B213 ·
      hemelsbreed 927 km, geen wegkm; OSRM-indicatie 1.125 km · aannemelijk: bron noemt aantal en truck, geen route)──►
Framatome ANF Lingen (UF6 → UO2 → splijtstofelementen) `u-lingen-anf` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | Orano Tricastin → Framatome Lingen | A7 → A46 → A6 → A31 → A3/A1 (Luxemburg) → A64/B51/A60 (Eifel) → A1 → A3 → A31 → B213 | **hemelsbreed 927 km, geen wegkm**; OSRM-indicatie 1.125 km (A46-variant; 1.107 km zonder Lyon-oost) [6] — ±15%-toets = indicatie | maak_stroombeen_weg (8 extracts) | nee — *aannemelijk: één bron, route niet gepubliceerd* [1] |

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-tricastin` | verrijking (kop) | Orano Tricastin — Georges Besse II, Pierrelatte, Drôme | 44.3250, 4.7167 | letterlijk uit `uranium-tricastin-romans.md` §3 / sitelaag `w-tricastin-verrijking` [7] | bron-gelegd (z15 opnieuw gezien: kruis in het zuidwestelijke deel van het grote industriecomplex, onder drie lange witte hallen; Esri toont het complex vervaagd) |
| `u-lingen-anf` | fabriek (staart, stoppunt) | Framatome ANF Brennelementfertigungsanlage, Lingen (Ems), naast KKW Emsland | 52.4804, 7.3315 | letterlijk uit `uranium-stpetersburg-lingen.md` §3 (WP-DE 52.480415/7.331507 [4]) = sitelaag `w-framatome-lingen` | bron-gelegd (z15 opnieuw gezien: omheind terrein met bedrijfsgebouwen midden in bos, ~0,8 km NO van de KKW-gebouwen; één toegangsweg [1]) |

## 4 · Via-punten b1 (8, in reisvolgorde; alle op de doorgaande weg, ontleend aan de OSRM-geometrie [6], routering met deze punten = 1.124,9 km zonder omweg of keerlus)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | A46 (Rocade Est Lyon), NO van Lyon | 45.8061, 4.9239 | de corridorkeuze: Lyon-oost via A46 i.p.v. het centrum (M6/Fourvière-tunnel); haalbaarheidstoets: "A6 Lyon (A46-oost)" |
| b1 | 2 | A31 ten zuiden van Dijon (Beaune–Dijon) | 47.2467, 5.0652 | pint A6 → A31 (Beaune) i.p.v. A6 door naar Parijs; geen stadscentrum |
| b1 | 3 | A31 bij Thionville (Metz–Luxemburg) | 49.3301, 6.1857 | houdt A31 aan Nancy–Metz–Thionville en de grens bij Luxemburg, i.p.v. via Saarbrücken (A4/A8) |
| b1 | 4 | A1 bij Luxemburg (ring, Findel-zijde) | 49.5868, 6.1607 | pint A3 → A1 richting Trier; ring, niet het centrum |
| b1 | 5 | B51 in de Eifel, ten noorden van Prüm | 50.2409, 6.4611 | pint de Eifel-route (A64 Trier → B51/A60 → B51) i.p.v. A48/Koblenz-Rijndal (haalbaarheidstoets: "Trier/B51/A1 Eifel") |
| b1 | 6 | A1 bij Erftstadt (west van Keulen) | 50.8944, 6.8267 | pint A1 tot Keulen (voor de Kölner ring), niet de Rijndalroute A61 |
| b1 | 7 | A3 bij Düsseldorf/Ratingen | 51.2765, 6.9067 | pint A3 noordwaarts i.p.v. A57/A61 |
| b1 | 8 | A31 bij Dorsten (ten noorden van Bottrop) | 51.6631, 6.9233 | pint A31 Bottrop–Gronau–Lingen i.p.v. de Münster/Osnabrück-variant uit het ontwerp (A43/A1/A30; OSRM kiest die niet) |
Extracts: `fr-rhone-alpes`, `fr-bourgogne`, `fr-champagne-ardenne`, `fr-lorraine`, `luxemburg`, `de-rheinland-pfalz`, `de-nrw`, `de-niedersachsen`. Refs: A7, A46, A6, A31, A3, A1, A64, A60, B51, B213. Eerste ca. 50 km A7 delen met `uranium-tricastin-romans`, laatste ca. 20 km met `uranium-stpetersburg-lingen` (samen < 7%): geen kopie nodig (haalbaarheidstoets).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Georges Besse II (Tricastin) | Orano | UF6 (natuurlijk) → verrijkt UF6 | ~12% wereld-SWU ≈ ~7.800 t U feed-eq./j (schatting, sitelaag) | [7] |
| Framatome ANF Lingen | Framatome (ANF GmbH) | UF6 → UO2-poeder → pellets → splijtstofelementen (per truck) | 800 t U/j vergund voor droge conversie, 650 t U/j overige delen; ~80-90% export | [4][2] |

## 6 · Stoppunt
De brief stopt bij Framatome Lingen: het opgedragen eindpunt en de afnemer die [1] voor deze UF6-lading noemt. Fase E vervalt; de uitgaande splijtstofelementen zijn een eigen stroom. Dat Lingen UO2-poeder terug naar Tricastin stuurt (per weg) [3] is een tegenstroom, hier niet getekend.

## 7 · Open punten
- **Route en vervoerder niet gepubliceerd:** [1] noemt alleen "alle Transporte per LKW" en 19 transporten (2017); geen Autobahn, geen tijdvak. De corridor is een routering over OSM (OSRM), geen bronroute; transporten van splijtbaar materiaal kunnen van de snelste route afwijken (aannemelijk, niet bevestigd).
- **Geen wegkm gepubliceerd:** alleen hemelsbreed 927 km tussen de ankers; OSRM-indicatie 1.125 km (+21% tegen hemelsbreed, een gebruikelijke omwegfactor voor Rhône-Moezel-Rijn). De ±15%-toets is een indicatie, geen norm.
- **Ontwerpcorridor via Münster/Osnabrück vervallen:** OSRM rijdt A31 Bottrop–Gronau–Lingen (1.107 km); de Münster/Osnabrück-variant is niet gemeten.
- **Peiljaar 2017**; sinds 2022 meer Russische en Duinkerken-aanvoer naar Lingen ([2], `uranium-stpetersburg-lingen.md` §7). Aandeel Tricastin in 2024-26 onbekend; een historische Bundestag-lijst (1996) noemt andere Lingen-routes (A30/B70/B403, geen Tricastin) [8].
- **Geen tonnage** per relatie; het volume hierboven is een telling van transporten + eigen schatting.
- Het kopanker ligt midden in het complex (vervaagd beeld); poort/loshal niet bepaald, de first mile staat in het wegprofiel (geen last-mile-been). Lingen: last mile ~1,2 km over `tertiary/unclassified` (zie de stpetersburg-lingen-bake).
- Bij de bake: extract-scans van `de-nrw` en `de-niedersachsen` zijn groot (RAM, max. 2 tegelijk); `luxemburg` en vier Franse extracts zijn klein tot middelgroot.

## 8 · Bronnen
[1] urantransport.de, "Brennelementefertigung in Lingen und Transporte dort": 2017 het grootste deel van het UF6 met 19 transporten uit Tricastin/Pierrelatte; 2022 Orano Tricastin als leverancier; geen Gleisanschluss, alle transporten per LKW; terrein "versteckt im Wald", één Zufahrt. https://urantransport.de/hintergrund/brennelementefertigung-in-lingen-und-transporte-dort/
[2] urgewald/AgiEL/Ecodefense, "Lingen-Report" (25-04-2025): Russische aanvoer naar Lingen, context volume 2024 (geen Tricastin-cijfers). https://www.urgewald.org/sites/default/files/media-files/Lingen-Report.pdf
[3] SFRP, "Au coeur de l'uranium" (1-2 feb. 2023, Darras): verrijkt UF6 per weg Tricastin → Romans; UO2-poeder per weg van Framatome Lingen naar Tricastin (via zoekresultaat gelezen). https://sfrp.asso.fr/wp-content/uploads/2023/02/S6_DARRAS_F-1.pdf
[4] Wikipedia DE, "Brennelementfertigungsanlage Lingen": coördinaat 52.480415/7.331507, 800 t U/j conversie, 650 t U/j overig. https://de.wikipedia.org/wiki/Brennelementfertigungsanlage_Lingen
[5] Wikipedia EN, "Nuclear fuel cycle in France": Georges Besse II verricht de verrijking op Tricastin. https://en.wikipedia.org/wiki/Nuclear_fuel_cycle_in_France
[6] OSRM (router.project-osrm.org, 2026-10-31): Tricastin → Lingen 1.107,3 km (A7/Lyon-centrum/A31/B51/A1/A3/A31/B213), met A46-oost 1.124,9 km; de 8 via-punten uit §4 geven 1.124,9 km. http://router.project-osrm.org
[7] Eigen briefs en sitelaag: `uranium-tricastin-romans.md` §3/§4 (`u-tricastin`), `uranium-stpetersburg-lingen.md` §3/§7 (`u-lingen-anf`), `uranium-sitelaag.json` (`w-tricastin-verrijking`, `w-framatome-lingen`). sat_check-beelden in `v2/build-cache/satcheck/`: `sat-uranium-tricastin-lingen-tricastin.png`, `sat-uranium-tricastin-lingen-lingen.png`.
[8] Deutscher Bundestag, Drucksache 14/593 (1999), UF6-transporten naar Lingen 1996 (historisch; alleen via zoekresultaat). https://dserver.bundestag.de/btd/14/005/1400593.pdf
[9] Haalbaarheidstoets (bindend, keten-id `uranium-tricastin-lingen`): corridor A7/A46/A6/A31/A1/B51/A3/A31, extracts incl. `fr-champagne-ardenne`, 7-8 via-punten op autowegen, km = hemelsbreed + OSRM-indicatie — toegepast.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Bestand:** `v2/data/stroomroute-uranium-tricastin-lingen.json` (259,9 KB) · `bash v2/tools/bak_stromen.sh uranium-tricastin-lingen` · functie `bak_uranium_tricastin_lingen`, profiel `uranium-tricastin-lingen-tricastin-lingen` (`maak_stroombeen_weg.py`).
**Benen:** 1 (truck, doorgetrokken) · **1.110,0 km** · 14.128 punten · 2 markers (`u-tricastin` en `u-lingen-anf`, beide 0,0 km van de lijn) · naden: n.v.t. (één been).

| # | mod. | km gemeten | km brief | afwijking | stippel |
|---|---|---|---|---|---|
| b1 | truck | 1.110,0 | OSRM-indicatie 1.107 (1.125 met A46-oost); hemelsbreed 927, geen wegkm | +0,3% t.o.v. 1.107 (-1,3% t.o.v. 1.125) | nee |

**Recept.** `python v2/tools/wegscan_puur.py --profiel uranium-tricastin-lingen-tricastin-lingen` (8 extracts, 10 via-punten uit §3/§4, venster 40 km, refs met en zonder spatie, ca. 20 min scan); daarna de bake. Segmenten: Tricastin→A46 Lyon-oost 186,6 · →Dijon 184,3 · →Thionville 295,0 · →Luxemburg 36,0 · →Prüm 104,9 · →Erftstadt 88,0 · →Ratingen 52,2 · →Dorsten 54,1 · →Lingen 109,0 km; alle snaps ≤ 0,08 km, ankerstukken 0,08 en 0,16 km.
**Toelichting.** De ±15%-toets is hier een indicatie, geen norm (geen gepubliceerde wegkm); de gemeten lijn valt tussen OSRM zonder en met A46-oost. Aannemelijk (één bron, route niet gepubliceerd) staat in de beennaam; het been is doorgetrokken. Geen stippel, haven-aanloop, vlucht, leiding of kopie.
**Bevindingen.** (1) `toets_knikken`: 29 knikken, 5 omkeringen waarvan 2 TERUGLOOP: korte overschiet-en-terug-lussen van ca. 100-200 m op knooppunten (45.7849, 4.8909 bij Lyon/A46; 51.0427, 7.0100 bij Leverkusen/A1); de rest zijn spike-ramplussen (R 4-48 m) en echte bochten; niet gerepareerd. (2) Bestand 259,9 KB (14.128 punten), onder de 300 KB. (3) Eerste ca. 50 km A7 en laatste ca. 20 km delen met tricastin-romans resp. stpetersburg-lingen: bewust geen kopie.
**Lessen.** Duitse en Franse refs staan in OSM met spatie ("A 7"): beide schrijfwijzen in `refs`. Een wegscan over 8 extracts (twee Duitse deelstaten) duurt ca. 20 min met andere scans erbij; draai op de achtergrond met een logbestand.

