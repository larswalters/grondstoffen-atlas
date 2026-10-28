# Routebrief (licht) · Lithium · Goulamina (Mali) → Abidjan → Yangtze-monding (China)

**stroom-id:** `lithium-goulamina-yangtze` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat van de Goulamina-mijn en -plant van Ganfeng (Cercle de Bougouni, Mali) gaat per truck over de RN7/N1/A3-corridor (~1.000 km volgens het bedrijf) naar de SEA-invest-mineraalterminal in de haven van Abidjan en per bulkschip rond Kaap de Goede Hoop naar China; de Chinese haven is niet gebronnd, dus het eindpunt is het conventie-anker Yangtze-monding (*aannemelijk: één bron*).
**Welke as van het verhaal:** *het grootste Malinese lithium, een eigen route naast Bougouni.* Fase 1 is ontworpen op 506 kt spodumeenconcentraat per jaar (naamplaat; productiestart gemeld 2-7-2025) [3][5]; eerste lading 30.000 t vertrok Abidjan eind juni 2025 en volgt sindsdien "consistent" [3][6]. Sitelaag B19 rekent de naamplaat indicatief om naar 75 kt LCE/j (niet gebronnd als feit, peiljaar 2025) [10]. De afzet is vooraf aan Chinese eigenaar-bedrijven verkocht, zonder genoemde haven of ontvanger [3].

## 1 · Ketenkaart
```
Goulamina-plant `li-goulamina-plant` ──(b1 truck · RN7 via Bougouni → Sikasso → Zégoua/Pogo → Ferkessédougou → Bouaké → Yamoussoukro → A3 · ~1.000 km bedrijfsopgave, gemeten 1.084,5)──►
Abidjan SEA-invest Q14 `li-abidjan-sea-invest-q14` ──(b2 zee-stippel · haven-aanloop lagune + Vridi-kanaal · 7,3 km)──► zeeknoop Abidjan
   ──(b3 zee · Kaap Agulhas, Straat van Soenda · 19.262,7 km MARNET; aannemelijk: één bron)──► Yangtze-monding `li-yangtze-monding` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (spodumeenconcentraat, bulk) | `li-goulamina-plant` → `li-abidjan-sea-invest-q14` | RN7 (Bougouni, Sikasso) → grens Zégoua/Pogo → N1 (Ferkessédougou, Bouaké, Yamoussoukro) → A3 | ~1.000 (Leo Lithium: Abidjan "approximately 1,000km" van Goulamina [4]; bedrijfsopgave, afgerond); gemeten 1.084,5 = +8,4% | maak_stroombeen_weg, extracts mali + ivoorkust | nee |
| b2 | B | zee (haven-aanloop) | `li-abidjan-sea-invest-q14` → zeeknoop 5245 (5,2462, -3,9973) | lagune west van het containerterminal → Vridi-kanaal → zee | 7,3 (handmatig gelegd; kade ligt 5,6 km hemelsbreed van de zeeknoop) | handmatige stippel, satelliet z15 (maak_havenaanloop gaf timeout, zie §7) | ja — MARNET reikt niet tot de kade |
| b3 | B | zee (bulkschip, handymax tot 55 kt [4]) | zeeknoop Abidjan → `li-yangtze-monding` | Kaap de Goede Hoop → Straat van Soenda → Zuid-Chinese Zee (MARNET beslist; niet via Malakka: Singapore ligt 510 km ernaast) | 19.262,7 (MARNET-meting; geen gepubliceerde lengte; SMM/Mysteel: 45–60 dagen [3][6]) | MARNET | nee — *bestemming China, haven niet gebronnd* staat in de beennaam |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-goulamina-plant` | mijn / plant (laadplek) | Goulamina-plant, Ganfeng (Lithium du Mali) | 11.3495, -7.9723 | [8][10] hergebruik sitelaag `w-li-goulamina` | bron-gelegd (z15 gezien: processing-plant met gebouwen, tanks en haalwegen; open put ~1 km ONO, tailings-/loogvijver ten ZW) |
| `li-abidjan-sea-invest-q14` | overslag truck → zee | SEA-invest-mineraalterminal (Terminal Vraquier Abidjan), Quai Q14 / Berth 14, Port Autonome d'Abidjan | 5.2946, -4.0125 | [4][7][9] | bron-gelegd (z17 gezien: bulkkade met silo's, grote loods en oranje bulkstapel aan het zuideinde van de Quai Ouest Q6–Q14; Leo-Lithium-loods "at Berth 14" [4]; welk deel van Q14 de Ganfeng-lading laadt is niet gebrond; punt ±15 m van de kaderand) |
| `li-yangtze-monding` | aanlanding China (stoppunt) | Yangtze-monding | 31.42704, 121.47618 | hergebruik uit `lithium-atacama-antofagasta.md` §3 | aannemelijk (conventie-anker; geen Chinese haven of fabriek per lading gebrond; MARNET-eindknoop 31.51, 121.4187 ligt 10,7 km ervandaan) |

## 4 · Via-punten (alleen b1; hergebruikt uit `lithium-bougouni-yangpu.md` §4, alle snaps < 0,3 km)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Sikasso (RN7-knoop) | 11.3166, -5.6778 | RN7 oostwaarts van Bougouni, enige verharde corridor naar de grens (beide lijnen delen het) |
| b1 | 2 | grens Zégoua (ML) / Pogo (CI) | 10.4828, -5.6531 | de ene grensovergang van deze corridor [3] |
| b1 | 3 | Ferkessédougou (A3/N1-knoop) | 9.5940, -5.1976 | N1 zuidwaarts i.p.v. westelijke tak via Korhogo/Daloa |
| b1 | 4 | Yamoussoukro (N1/A3-knoop) | 6.8200, -5.2776 | A3 naar Abidjan (anders dan Bougouni, dat naar Soubré/San Pedro afbuigt); de route passeert Bouaké op 0,2 km |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Goulamina-plant | Ganfeng Lithium (volledige controle sinds juli 2025) | erts → spodumeenconcentraat | fase 1 506 kt/j, fase 2 tot 1 Mt/j gepland | [3][5] |
| SEA-invest-mineraalterminal Abidjan | SEA-invest (concessie Port Autonome d'Abidjan) | lossen, opslag, laden | 9.000 m² loods ≈ 60.000 t op de kade; minimaal 250 kt/j doorvoer; handymax tot 55 kt | [4] |

## 6 · Stoppunt
De brief stopt bij de Yangtze-monding: geen bron noemt de Chinese aanloophaven of de verwerkende fabriek voor deze lading (de afzet is "100% pre-sold" aan Chinese eigenaar-bedrijven [3]); fase D vervalt.

## 7 · Open punten
- **Chinese bestemming niet gebronnd** — SMM zegt alleen "aankomst in een Chinese haven begin augustus" (vertrek 24-6-2025) [6]; Yangtze-monding is een conventie-anker, net als bij `lithium-cirilo-vitoria` en `lithium-bikita-zhangjiagang`. Het zeebeen eindigt op de MARNET-eindknoop, 10,7 km van het anker.
- **Kade in Abidjan is niet pand-precies** — Berth 14 komt uit de ASX-aankondiging van 2022 (loods "adjacent Berth 14") [4]; Q14 uit OSM-kadenummering [8]. Of de Ganfeng-lading in 2025 nog op Q14 laadt is niet gebrond. De Nominatim-"Sea Invest" (5.2770, -4.0077) is een kantoorgebouw ~700 m van het water en is niet gebruikt.
- **Concessiedatum tegenstrijdig**: Ecofin 2025 zegt "sinds 2018" [1], Ecofin 2026 "sinds 2009" [7]; geen invloed op de tekening.
- **Haven-aanloop is handwerk** — `maak_havenaanloop.py` haalde binnen 300 s geen pad (de 1:10M-kust kent lagune en kanaal niet); lijn is op Esri z15 in de lagune en het Vridi-kanaal gelegd en blijft schematisch.
- **Wegkilometers**: 1.084,5 gemeten tegen een afgeronde bedrijfsopgave (+8,4%); Mysteel geeft alleen 6–7 dagen retour [3]. Overlap met `lithium-bougouni-yangpu-weg-plant-sanpedro` (Sikasso → Yamoussoukro) is bewust: andere mijn, haven en eigenaar.
- **Volume** — 2025-productie van 336,6 kt concentraat kwam alleen uit een zoekresultaat (Asian Metal, pagina onleesbaar) en is niet gebruikt. Veiligheidsrisico op de Malinese corridor is niet beoordeeld.

## 8 · Bronnen
[1] Ecofin Agency, "Mali's Lithium Finds a Gateway in Two Ivorian Ports", 24-10-2025 — Ganfeng koos Abidjan, SEA-invest beheert het mineraalterminal. https://www.ecofinagency.com/news/2410-49787-malis-lithium-finds-a-gateway-in-two-ivorian-ports
[2] LogistAfrica, "Ivory Coast: Abidjan and San Pedro Emerge as Key Hubs for Malian Lithium", 30-10-2025 — dienstenovereenkomst met SEA-invest, eerste lading sinds mei 2025. https://logistafrica.com/en/logistic/ivory-coast-abidjan-and-san-pedro-emerge-as-key-hubs-for-malian-lithium/
[3] Mysteel, "Key Lithium Mining Projects in Mali: Goulamina and Bougouni" — 506 kt/j fase 1, eerste 30.000 t juni 2025, retour 6–7 dagen, 100% pre-sold aan Chinese eigenaren. https://www.mysteel.net/analysis/5112006-key-lithium-mining-projects-in-mali-goulamina-and-bougouni
[4] Leo Lithium (ASX), "Port services agreement formalised", 15-11-2022 — SEA-invest, 9.000 m² loods bij Berth 14, 250 kt/j minimum, Abidjan ~1.000 km van Goulamina. https://announcements.asx.com.au/asxpdf/20221115/pdf/45hlg0kl1vnmyg.pdf
[5] Mysteel, "Goulamina spodumene project in Mali has officially commenced production", 3-7-2025 — fase 1 506 kt/j. https://www.mysteel.net/news/5091127-flash-goulamina-spodumene-project-in-mali-has-officially-commenced-production
[6] SMM, Ganfeng Goulamina eerste lading — vertrek 24-6-2025, over de weg naar de exporthaven, aankomst China begin augustus. https://news.metal.com/en/newscontent/103400622
[7] Ecofin Agency, "Abidjan upgrades mineral terminal as regional mining trade accelerates" — SEA-invest ~CFA 20 mld modernisering. https://www.ecofinagency.com/news-infrastructures/1303-53748-abidjan-upgrades-mineral-terminal-as-regional-mining-trade-accelerates
[8] OpenStreetMap (ODbL) via Overpass/Nominatim — "Quai Ouest (Q6-Q14)", Quai Q14 5.2946/-4.0125, Q13 5.2963/-4.0148; Goulamina-mijn 11.3495/-7.9723.
[9] Esri World Imagery via `v2/tools/sat_check.py` (v2/build-cache/satcheck/): `sat-lithium-goulamina-yangtze-plant-z15.png`, `-abidjan-q14-z17.png`, `-abidjan-z16n.png`, `-abidjan-z16.png`, `-abidjan-z15.png`, `-abidjan-z14.png`.
[10] `v2/design/lithium-sitelaag.json` (w-li-goulamina, B19) en `v2/design/routebrieven/lithium-bougouni-yangpu.md` (via-punten); `lithium-atacama-antofagasta.md` §3 (Yangtze-anker).

## 9 · Gebakken (2026-10-28, lichte werkwijze, M31 golf 10)
**Bestand:** `v2/data/stroomroute-lithium-goulamina-yangtze.json` (197,9 KB, versie 2, lonlat, 3 benen, 10.573 punten, 3 markers). **Recept:** functie `bak_lithium_goulamina_yangtze` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh lithium-goulamina-yangtze`); profiel `lithium-goulamina-yangtze-plant-abidjan` in `maak_stroombeen_weg.py`; haven-aanloop `v2/build-cache/ais/graaf/lithium-goulamina-yangtze-aanloop-abidjan.geojson`.

| # | modaliteit | km gemeten | km brief | naad | opmerking |
|---|---|---|---|---|---|
| b1 | truck | 1.084,9 | ~1.000 (bedrijfsopgave) | 0,00 | +8,4% (binnen ±15%), doorgetrokken |
| b2 | zee (stippel) | 7,3 | 7,3 | 0,00 | haven-aanloop Abidjan, handmatig op satelliet |
| b3 | zee | 19.262,7 | 19.262,7 (MARNET) | 0,00 | doorgetrokken; aannemelijk: één bron staat in de beennaam |
| totaal | | 20.354,9 | | max 0,00 | 3 markers |

**Markers:** plant en Abidjan Q14 liggen op de lijn (0,0 km); het Yangtze-anker ligt 4,45 km van de lijn (het zeebeen eindigt op MARNET-knoop 31.51, 121.4187; dezelfde conventie als vitoria en atacama).
**Haven-aanloop:** de kade Q14 ligt 5,6 km van zeeknoop 5245 (5.2462, -3.9973), dus een aanloop (7,3 km, 15 punten, lagune en Vridi-kanaal). `maak_havenaanloop.py` gaf timeout (300 s); daarom handmatig gelegd, schematisch, stippel omdat MARNET de kade niet bereikt. Geen vlucht, geen leiding, geen letterlijke kopie.
**Toets:** `toets_knikken.py` 23 knikken >= 60 graden (21 truck, 2 zee), 0 omkeringen, 0 terugloop; de truckknikken zijn kleine bochten (5-90 m) in de OSM-lijn. `toets_rechte_benen.py` meldt geen recht been. json.load ok, modaliteiten {truck, zee}, elk been >= 2 punten.
**Lessen:** de wegkm in de brief (~1.000) is een afgeronde bedrijfsopgave, de +8,4% is dus een indicatie en geen meetfout; overlap met `lithium-bougouni-yangpu-weg-plant-sanpedro` (Sikasso tot Yamoussoukro) is bewust. Open punten uit §7 blijven staan (Chinese haven niet gebronnd, Q14 niet pand-precies, aanloop handwerk).
