# Routebrief (licht) · gas — Draupner E (Noordzee, Noorwegen) → Duinkerke Port Ouest (Frankrijk)

**stroom-id:** `gas-draupner-dunkerque` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) ·
**status:** gebakken
**Keten in één zin:** Noors Noordzeegas (vooral Sleipner Oost en Troll Vest [1]) gaat via het riser-platform Draupner E en
Franpipe — één 42-inch onderzeese gasleiding van ~840 km, Gassco/Gassled — naar de aanlanding bij Port Ouest van Duinkerke,
het Franse invoedingspunt van Noors pijpgas; tweelingleiding van Zeepipe (Sleipner → Zeebrugge).
**Welke as van het verhaal:** de derde Noorse pijpgas-as naar Noordwest-Europa en de directe Noorse lijn naar Frankrijk —
**ontwerpcapaciteit 19,6 bcm/j** [1] (terminal 50 miljoen m3/dag ≈ 18,3 bcm/j [4], peiljaar 1998); **werkelijke doorzet onbekend**
(geen gepubliceerd jaartotaal voor Franpipe gevonden, zie §7). Het verhaal is een nieuw land (Frankrijk), niet een nieuwe bron.

## 1 · Ketenkaart
```
Noordzeevelden (fase A vervalt: Sleipner Oost + Troll Vest, diffuus verzameld via het Gassled-net [1])
   ──► Draupner E-riser `gas-draupner-e` ──(b1 leiding · Franpipe 42″ · ~840 km, OSM 2 ways, onderzees)──►
Aanlanding Port Ouest, Duinkerke `gas-dunkerque-aanlanding` — stoppunt (terminal landinwaarts, niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | `gas-draupner-e` → `gas-dunkerque-aanlanding` | Franpipe (42″, 1.067 mm, Gassco/Gassled, in dienst 1998-07-01 [3]) | 840 [1] → gemeten OSM 833,5 (−0,8%) | OSM-ways 174152585 (800,1 km, 102 punten) + 903860200 (33,3 km, 10 punten): man_made=pipeline, name=Franpipe, operator=Gassco, substance=gas [5]; vooraf gestikt met `v2/tools/maak_leidingbeen_gas_draupner_dunkerque.py`, naad 0 m, 111 punten | nee |

Eén doorgetrokken been: de naad tussen de twee ways is 0 m en geen offshore-stuk ontbreekt (grootste vertexafstand 26,3 km =
kartering van een rechte onderzeese leiding, geen gat; omwegfactor 833,5 / 794,5 hemelsbreed = 1,05). Beide uiteinden zijn Gassco-vertices.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-draupner-e` | riser-platform (kop) | Draupner E-riser (Gassco/Gassled), blok 16/11, Noordzee | 58.1845, 2.4463 | [2][3][5] | aannemelijk (OSM-leidingstart, Gassco-way; offshore, niet satelliet-controleerbaar; Wikipedia-coördinaat van het complex S+E, 58.1888 2.4727, ligt 1,6 km oostelijker) |
| `gas-dunkerque-aanlanding` | aanlanding (staart, stoppunt) | Franpipe-aanlanding naast de ingang van Port Ouest, Loon-Plage/Duinkerke | 51.0406, 2.2493 | [5][6] | bron-gelegd (z15 gezien: strand en duin vlak westelijk van de havengeul-ingang van Port Ouest, het OSM-leidingeinde ligt op de dijk/strandrand; landinwaarts industrie en tankenpark; geen terminal op dit punt) |

Hergebruik: geen — Draupner E en Duinkerke staan niet in `gas-sitelaag.json` en niet in eerdere brieven (zelfde Noorse bron als
`gas-karsto-dornum` en `gas-nyhamna-easington`, maar ander land en andere leiding; geen gedeeld been). De Gassco-terminal zelf (OSM-landuse
way 290042835 "Gassco Dunkerque", alt_name "Dunkerque Terminal DA", pipeline=substation, 51.0106, 2.2461, 3,3 km ZZW van de aanlanding)
is op z15 gezien als omheind, zelfstandig terrein met grindplateau in de akkers; **bewust niet als anker gebruikt** (haalbaarheidstoets:
aanlanding als anker, geen terminal) en niet getekend — zie §7.

## 4 · Via-punten
Niet van toepassing: het enige been is een leiding uit aaneengestikte OSM-ways (geen corridorkeuze zoals bij weg/spoor).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Draupner E-riser | Gassco/Gassled (technische dienst Equinor) | Noors drooggas (Statpipe/Zeepipe/Europipe-hub) → Franpipe | knooppunt voor monitoring van druk/volume/kwaliteit; Europipe I, Franpipe en Zeepipe II B hangen aan Draupner E | [2] |
| Dunkerque-ontvangstterminal | Gassled-partners 65% / GDF Suez (Engie) 35% (Wikipedia, oude bron) [1]; geopereerd door Gassco | Franpipe-gas → Franse transportnet (185 km Artère des Hauts-de-France naar Gournay-sur-Aronde, 1998 [4]) | 50 miljoen m3/dag [4]; Franpipe 19,6 bcm/j [1] | [1][4] |

## 6 · Stoppunt
De brief stopt bij de aanlanding bij Port Ouest, het door het ontwerp gevraagde Franse invoedingspunt. Het laatste stuk landinwaarts
(~3,3 km naar de Gassco-terminal) is niet in OSM gekarteerd en niet getekend (kleiner dan 5 km, geen naad); daarna is het gas anoniem
Frans netgas. Fase A vervalt: Sleipner Oost en Troll Vest voeden Franpipe via het Gassled-net, geen eigen veld-anker.

## 7 · Open punten
- **Geen jaarvolume voor Franpipe of het Duinkerke-invoedingspunt gevonden.** 19,6 bcm/j is ontwerp [1]; Gassco meldt alleen netwerktotalen
  (109,1 bcm in 2023 naar BE/UK/FR/DE/DK [7]). Volume = onbekend; ENTSOG/GRTgaz-transparantiedata voor het Duinkerke-invoedingspunt zijn niet doorzocht.
- **Aandeel in de Franse invoer niet gebronnen** — het verhaal is "nieuw land, zelfde bron" (risico uit het ontwerp); geen bron die dit aandeel noemt.
- **Terminal Duinkerke niet getekend:** OSM-landuse "Gassco Dunkerque" (cadastre-bron 2014) 3,3 km ZZW van het leidingeinde; geen operator-document dat dit perceel
  als Franpipe-ontvangstterminal noemt gevonden (aannemelijk-plus). Centraal bij te voegen als marker/anker als dat gewenst is.
- **Draupner E is een OSM-vertex**, geen platformreferentie; 1,6 km van de Wikipedia-coördinaat van het complex, niet satelliet-toetsbaar.
- **Ownership-regel (65/35)** komt uit een gedateerde Wikipedia-regel; Gassled-structuur is sindsdien herzien.
- **Sitelaag mist Draupner E en Duinkerke** — centrale aanvulling nodig voor de gloed (gewicht: 19,6 bcm/j capaciteit).
- Zeepipe I (Sleipner → Zeebrugge, OSM 812 km) is de tweelingleiding en een eigen keten, hier niet getekend.

## 8 · Bronnen
[1] Wikipedia (EN), "Franpipe" — 840 km, Draupner E → Port Ouest Dunkirk, 42″, 19,6 bcm/j, Sleipner Oost + Troll Vest, inhuldiging 1998-10-09, Gassled 65% / GDF Suez 35%.
    https://en.wikipedia.org/wiki/Franpipe
[2] Wikipedia (EN), "Draupner platform" — Draupner S+E, 160 km uit de kust, blok 16/11, coördinaat 58.18878 2.47267; Europipe I, Franpipe, Zeepipe II B aan Draupner E.
    https://en.wikipedia.org/wiki/Draupner_platform
[3] Sokkeldirektoratet (Factpages), "42″ Gas DRAUPNER E, DUNKERQUE" (NPDID 326374) — operator Gassco, Gassled, 42″, 85 m max waterdiepte, in dienst per 01.07.1998.
    https://factpages.sodir.no/en/tuf/pageview/pipeline/all/326374
[4] Oil & Gas Journal, "NorFra line boosts France's gas hub position" (1998) — terminal Dunkirk/Loon-Plage, 65% NorFra-groep / 35% Gaz de France, 50 miljoen m3/dag, 185 km Artère des Hauts-de-France.
    https://www.ogj.com/home/article/17226346/norfra-line-boosts-france39s-gas-hub-position
[5] OpenStreetMap-bijdragers (ODbL), OSM-API 2026-10-31 — ways 174152585 en 903860200 (man_made=pipeline, name=Franpipe, operator=Gassco, substance=gas, diameter 1067, source=Gassco); way 290042835 "Gassco Dunkerque".
    https://www.openstreetmap.org/way/174152585 · https://www.openstreetmap.org/way/903860200 · https://www.openstreetmap.org/way/290042835
[6] Esri World Imagery via `v2/tools/sat_check.py` z15 — `v2/build-cache/satcheck/sat-gas-draupner-dunkerque-aanlanding.png` en `-gassco-terminal.png`.
[7] PGJ Online (Reuters), "Norwegian piped gas exports could rival historic highs in 2024, Gassco says" — 109,1 bcm in 2023 over het hele Gassco-net (geen Franpipe-cijfer).
    https://pgjonline.com/news/2024/august/norwegian-piped-gas-exports-could-rival-historic-highs-in-2024-gassco-says

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)
**Bestand:** `v2/data/stroomroute-gas-draupner-dunkerque.json` (versie 2, lonlat, 2,7 KB) · functie `bak_gas_draupner_dunkerque` in `v2/tools/bak_stromen.sh`.

| # | modaliteit | been | km gemeten | km brief | afwijking | stippel |
|---|---|---|---|---|---|---|
| b1 | leiding | Franpipe Draupner E naar Duinkerke Port Ouest (42 inch, OSM ways 174152585+903860200) | 833,5 (111 punten) | 840 (Wikipedia) | -0,8% | nee |

Totaal 833,5 km, 111 punten, 1 been, 2 markers (`gas-draupner-e` 58.1845,2.4463 en `gas-dunkerque-aanlanding` 51.0406,2.2493, beide ~0 km van de lijn).

**Recept:** `--been-geojson leiding` met het vooraf gestikte `v2/build-cache/ais/graaf/gas-draupner-dunkerque-leiding-franpipe.geojson` (FeatureCollection, herhaalbaar met `python v2/tools/maak_leidingbeen_gas_draupner_dunkerque.py`); geen extracts, via-punten, profiel, MARNET-zeebeen, haven-aanloop, stippel, vlucht of gedeeld been. Geen eigen router-run: hecht_marnet.py nam de lijn letterlijk over.

**Toets:** km binnen 15% van 840; naad 0 km (één been); markers op de lijn; toets_knikken 0 knikken en 0 omkeringen; toets_rechte_benen geen melding (grootste vertexafstand 26,3 km is kartering van een rechte onderzeese leiding, geen gat).

**Leiding-toelichting:** doorgetrokken omdat OSM de leiding volledig kent (man_made=pipeline, operator Gassco, substance gas); het is een onderzees traject en wordt niet satelliet-getoetst. Draupner E blijft aannemelijk (OSM-vertex, 1,6 km van de Wikipedia-coordinaat van het complex). De Gassco-terminal (51.0106,2.2461) is bewust niet getekend: stoppunt is de aanlanding.

**Lessen:** een keten met een vooraf gestikte OSM-leiding is een enkele regel `--been-geojson`; het patroon bak_gas_nyhamna_easington volstaat. Centraal nodig: sitelaag voor Draupner E en Duinkerke, register, bundel.
