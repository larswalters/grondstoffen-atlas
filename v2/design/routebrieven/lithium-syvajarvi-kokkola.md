# Routebrief (licht) · lithium — Päiväneva/Syväjärvi → Kokkola (Finland)

**stroom-id:** `lithium-syvajarvi-kokkola` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat van Keliber's Päiväneva-concentrator (naast de Syväjärvi-dagbouw, Kaustinen) gaat per **vrachtwagen** over weg 63 en weg 13 naar Keliber's eigen hydroxideraffinaderij in het Kokkola Industrial Park (Ykspihlaja). Eén landbeen, geen zee, geen spoor. Stoppunt = de raffinaderij.
**Welke as van het verhaal:** de eerste gesloten EU-keten van mijn tot hydroxide (Sibanye-Stillwater 80%, Finnish Minerals Group 20%). Nameplate **15 kt LiOH·H₂O/j ≈ 13 kt LCE/j** (×0,88) uit ca. 200 kt concentraat/j, peiljaar 2026; volle productie ca. 2028 [1][2][3]. Raffinaderij nog in inbedrijfstelling [1][6].

## 1 · Ketenkaart
```
Syväjärvi-dagbouw + Päiväneva-concentrator `li-paivaneva-plant` (één site, ~2 km eigen terrein, geen been)
  ──(b1 truck · Malmitie → Rikastetie → weg 63 (Kaustinen) → weg 13 → weg 8/Satamatie · gepubl. 66 km, OSRM 72,5)──►
Keliber-raffinaderij `li-kokkola-raffinaderij` ⏹ stoppunt (battery-grade LiOH·H₂O)
```
Ontwerpwijziging (haalbaarheidstoets, bindend): het aparte truckbeen mijn → concentrator vervalt. Yle: het erts gaat "een paar kilometer" naar Päiväneva [6]; de ontwerp-coördinaat 63.595,23.4754 (Syväjärventie) is een weg 14 km verder west, geen groeve.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | `li-paivaneva-plant` → `li-kokkola-raffinaderij` | Malmitie → Rikastetie → weg 63 Toholammintie/Kaustintie → Kaustinen → weg 13 Kokkolantie → weg 8 Eteläväylä → Satamatie (756) — corridor aannemelijk: enige OSRM-route, door Keliber niet gepubliceerd; modus truck [6] | **gepubliceerd 66** (Keliber via SMM/Mining Weekly, "66 km to Kokkola Industrial Park") [1][2]; OSRM-referentie 72,5 (+9,8%) [7] | maak_stroombeen_weg (extract `finland`) | nee |

## 3 · Ankers (één per site en per overslag; 4 decimalen, lat, lon)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-paivaneva-plant` | mijn + concentrator (laadplek, één site) | Päiväneva-concentrator / Syväjärvi-groeve, Kaustinen (Midden-Österbotten) | 63.6627, 23.8019 | [4][5][8] | aannemelijk (z15/z16 gezien: bos met twee meren (Syväjärvi), een klein grijs verkenningsplatform met bezinkbakje op ~150 m en bosweg; de installaties zelf staan niet op de opname, die dateert van vóór de bouw 2023–2025) |
| `li-kokkola-raffinaderij` | losplek + raffinaderij | Keliber lithiumhydroxidefabriek, Kokkola Industrial Park (Ykspihlaja) | 63.8521, 23.0529 | [8][10] | bron-gelegd (hergebruikt letterlijk uit `lithium-sitelaag.json` `w-li-keliber`; z15 gezien: bouwplaats met gebouwskelet en zandvlakte naast een tankenpark in het industriegebied ten oosten van de haven; OSM-vlak `landuse=industrial` "Keliber", way 1509419282) |

## 4 · Via-punten (b1 — één corridor; punten alleen om de weg vast te pinnen, nooit in een dorps- of stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Rikastetie × weg 63 (km ~10,5) | 63.5831, 23.8712 | pint het verlaten van de concentratorwegen (Malmitie, Rikastetie) op de doorgaande weg 63, niet een bosweg |
| b1 | 2 | weg 63 Toholammintie (km ~15) | 63.5646, 23.8000 | pint de weg 63 westwaarts naar Kaustinen |
| b1 | 3 | weg 13 Kokkolantie, 4 km ten noordwesten van het centrum van Kaustinen (km ~25) | 63.5722, 23.6299 | pint de overstap op weg 13 voorbij het dorpscentrum (centrum 63.548,23.697 omzeild) |
| b1 | 4 | weg 13 Emetstrand/Jyväskylävägen (km ~40) | 63.6479, 23.4017 | pint de weg 13 noordwaarts; punt uit de haalbaarheidstoets, 1 m van de weg |
| b1 | 5 | weg 13 Nedervetilvägen (km ~50) | 63.7241, 23.3133 | pint weg 13 richting Kokkola |
| b1 | 6 | Satamatie (756), rotonde (km ~71) | 63.8381, 23.0735 | pint de aankomst via weg 8/Satamatie de industriezone in, ten zuiden van het centrum |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Syväjärvi-dagbouw + Päiväneva-concentrator | Keliber Oy (Sibanye-Stillwater 80%) | spodumeenerts → spodumeenconcentraat | ca. 200 kt concentraat/j; ertswinning sinds 11-02-2026, concentrator warm in bedrijf sinds april 2026, stabiele productie H2 2026 | [1][2][4] |
| Keliber-raffinaderij Kokkola | Keliber Oy | concentraat → battery-grade LiOH·H₂O | 15 kt LiOH·H₂O/j ≈ 13 kt LCE/j; opstart einde 2026 volgens Yle [6], geen datum volgens SMM [1] | [1][6] |

## 6 · Stoppunt
De brief stopt bij de raffinaderij in Kokkola: geen bron noemt een afnemer van het hydroxide (fase D vervalt), en de keten is bewust "mijn tot hydroxide" op één site-paar.

## 7 · Open punten
- **Wegmodus:** alleen Yle noemt vrachtwagens [6]; SMM noemt alleen de 66 km [1]. Het exacte haaltraject (66 km tegen OSRM 72,5 km) is niet gepubliceerd; de corridor is de enige OSRM-route, geen bedrijfsopgave.
- **Anker Päiväneva** is aannemelijk (coördinaat uit fi.wikipedia [4]): de Esri-opname is van vóór de bouw, dus de concentrator zelf is niet gezien. Syväjärvi-dagbouw en concentrator liggen "een paar km" uiteen [6]; hier één anker.
- **Weinig volume in 2026:** raffinaderij in inbedrijfstelling; Yle noemt einde 2026, SMM (juli 2026) geen datum. De weg is gemeten, de lading nog klein.
- **Sitelaag/v1 voorstel (niet doorgevoerd):** `lithium-sitelaag.json` heeft alleen de raffinaderij (`w-li-keliber`); de mijn/concentrator-site ontbreekt. v1 `li-keliber` (63.50,23.60) ligt ~18 km van het echte Päiväneva-punt. Nu is geen capaciteit apart voor de mijn gebrond.
- **Ontwerpfout gemeld:** Syväjärventie 63.595,23.4754 [8] is een weg in Viiperi, 14 km ten westen; het meer Syväjärvi ligt bij 63.66,23.8056.
- Afnemer en transportbedrijf niet genoemd.

## 8 · Bronnen
[1] SMM News, "Sibanye-Stillwater's Keliber lithium hydroxide project advances to staged production in Finland" (66 km naar Kokkola, 15 kt LiOH/j, mijn feb 2026, concentrator apr 2026). https://news.metal.com/newscontent/104101588-smm-news-sibanye-stillwaters-keliber-lithium-hydroxide-project-advances-to-staged-production-in-finland
[2] Mining Weekly, Keliber update 2025-09-05 en 2025-11-14 (66 km naar het Kokkola Industrial Park, ca. 200 kt concentraat/j; pagina's gaven 403, inhoud via zoekresultaat). https://www.miningweekly.com/article/keliber-lithium-hydroxide-project-finland-update-2025-09-05 · https://www.miningweekly.com/article/keliber-lithium-hydroxide-project-finland-update-2025-11-14
[3] Wikipedia (en), "Keliber" (eigenaren, 15 kt LiOH·H₂O/j, Syväjärvi–Päiväneva–Kokkola, bouw raffinaderij mrt 2023). https://en.wikipedia.org/wiki/Keliber
[4] Wikipedia (fi), "Kaustisen litiumkaivos" (coördinaat 63.66272, 23.80186; Syväjärvi-winning 11-02-2026, Päivänevan rikastamo lente 2026). https://fi.wikipedia.org/wiki/Kaustisen_litiumkaivos
[5] Wikipedia (fi), "Keliber" (Syväjärvi op de grens Kokkola/Kaustinen; raffinaderij bij de haven van Kokkola). https://fi.wikipedia.org/wiki/Keliber
[6] Yle, 12-02-2026, artikel over de start van de Kaustinen-mijn (ertstransport per kuorma-auto naar Kokkola; concentrator lente 2026, chemische fabriek einde 2026). https://yle.fi/a/74-20209826
[7] OSRM (router.project-osrm.org, OSM-wegdata), driving-route 63.6627,23.8019 → 63.8521,23.0529: 72,5 km via weg 63 en weg 13, geen alternatieven; nearest-controle van de via-punten (1–3 m van de weg), opgevraagd 2026-10-09. Geen officiële bronopgave.
[8] OpenStreetMap Nominatim/Photon (ODbL): "Keliber" landuse=industrial, Ykspihlaja (63.8521,23.0529, way 1509419282); Päivänevantie (way 427523663, 63.6500,23.8021); Syväjärventie (way 189297683, Viiperi, 63.5950,23.4754). https://www.openstreetmap.org
[9] Esri World Imagery via `v2/tools/sat_check.py` (live, z15/z16): `v2/build-cache/satcheck/sat-lithium-syvajarvi-kokkola-paivaneva.png`, `…-paivaneva-z16.png`, `…-kokkola-raffinaderij.png`.
[10] `v2/design/lithium-sitelaag.json` `w-li-keliber` (63.8521,23.0529, bron-gelegd z15) en v1 `data/lithium.js` (`li-keliber` → `li-ref-kokkola`, mode road).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-lithium-syvajarvi-kokkola.json` (21,0 KB, versie 2, lonlat) · functie `bak_lithium_syvajarvi_kokkola` in `v2/tools/bak_stromen.sh` · profiel `lithium-syvajarvi-kokkola-paivaneva-kokkola` in `v2/tools/maak_stroombeen_weg.py` · geojson `v2/build-cache/ais/graaf/lithium-syvajarvi-kokkola-weg-paivaneva-kokkola.geojson`.
**Titel:** Lithium · Päiväneva (Kaustinen) → Keliber-raffinaderij Kokkola (Finland).

| # | modaliteit | been | km gemeten | km brief | naad | stippel |
|---|---|---|---|---|---|---|
| b1 | truck | Päiväneva → Keliber Kokkola (Rikastetie → weg 63 → weg 13 → weg 8 → Satamatie; aannemelijk: modus alleen door Yle genoemd) | **72,5** (wegnet 72,1; 1.046 punten) | 66 gepubliceerd (+9,8%); OSRM 72,5 | n.v.t. | nee |

Totaal 72,5 km, 2 markers (beide op 0,0 km van de lijn), geen naad, geen stippel.
**Recept:** extract `finland` via `v2/tools/wegscan_puur.py` (pyosmium geblokkeerd, Overpass uit; ~100 s scan); 6 via-punten uit §4 ongewijzigd; refs 63, 13, 8, 756; `eindToegangPrivaat`; venster 40 km. Snap van de ankers op het wegnet 0,20 km (Päiväneva) en 0,15 km (raffinaderij): geen last-mile-been. Segmentkm: 10,6 · 4,5 · 10,2 · 15,3 · 9,8 · 18,9 · 3,0; geen via-punt gaf een omweg.
**Toets:** lengte +9,3% t.o.v. 66 (binnen 56-76, norm ±15% want 66 is een bedrijfsopgave); eerste mile 10,6 km over `unclassified` (Malmitie/Rikastetie), laatste mile 1,1 km. `toets_knikken`: 11 knikken >= 60 graden (alle spikes van 3-25 m op de wegassen, afslagen en rotondes), 0 omkeringen, 0 terugloop. `toets_rechte_benen`: geen melding. Contract: versie 2, punt_formaat lonlat, modaliteit truck, bestand < 300 KB.
**Toelichting:** geen zee, spoor, leiding of vlucht, dus geen haven-aanloop en geen stippel; geen letterlijke kopie. De 6,5 km (+9,8%) tussen gepubliceerd en gemeten is de OSRM-route: Keliber's 66 km is waarschijnlijk een afgerond of ander haaltraject.
**Lessen:** (1) `wegscan_puur.py` werkt voor Finland zonder wrapper. (2) Het eerste via-punt (63.5831,23.8712) ligt exact op de weg 63-aansluiting; er verschijnt een spike van 3 m, geen probleem. (3) De sitelaag mist nog de mijn/concentrator-site (§7); voorstel blijft centraal.
