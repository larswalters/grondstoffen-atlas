# Routebrief (licht) · lithium — Manono → Kalemie → Kigoma → Dar es Salaam → Ningbo (DR Congo → China)

**stroom-id:** `lithium-manono-ningbo` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**titel op de bol:** Lithium · Manono → Dar es Salaam → Ningbo (DR Congo)
**Keten in één zin:** spodumeenconcentraat van de **Manono Northeast-plant** (Manono Lithium SAS: Zijin-groep 54,9% / Cominière 35,1% / DRC-staat 10% [5][4]) gaat per **truck** over een onverharde weg (RN33, via Kiambi en Nyunzu) naar de meerhaven bij **Kalemie** (Mutowa), per **meerschip** (ca 2.000 t) over het Tanganyikameer naar **Kigoma**, per **spoor** (meterspoor Centraal-lijn) naar **Dar es Salaam**, per **truck** naar de haven (CT2) en per **zeeschip** via Malakka naar **Ningbo-Beilun** — de Chinese losplek is *aannemelijk: bron noemt alleen "Chinese refineries"*.
**Welke as van het verhaal:** de eerste officiële lithiumexport van de DRC (22-07-2026) via de Tanzaniaanse oostroute, als alternatief voor de Lobito-as [3][6]. Volume: **30 kt LCE/j doel 2026** (Skillings [2]); ontwerp ca 1 Mt spodumeenconcentraat/j (SMM [1]) = ca **136 kt LCE** bij SC5,5 (eigen omrekening: 1.000 kt × 5,5% Li2O × 2,473); de eerste ladingen waren proefladingen, volume niet gepubliceerd [1][5].

## 1 · Ketenkaart
```
Manono-plant `li-manono-plant` ──(b1+b3 truck · RN33 via Kiambi–Nyunzu · 433,6 km gemeten, b2 = 0,36 km OSM-gat)──►
Kalemie/Mutowa-haven `li-kalemie-haven` (stand-in) ──(b4 binnenvaart · Tanganyikameer · ca 130 km stippel, meerveer)──►
Kigoma-haven `li-kigoma-haven` ──(b5 spoor · Centraal-lijn via Tabora–Dodoma–Morogoro · 1.246,1 km)──►
Dar-spoor-einde `li-dar-spoor` ──(b6 truck · stadswegen Dar es Salaam · ca 7,5 km)──► havenpoort `li-dar-poort`
──(b7 truck stippel 0,36 km)──► CT2-kade `li-dar-kade` ──(b8 aanloop 20,9 km stippel · b9 zee 11.780,8 km · b10 aanloop 11,6 km stippel)──►
Ningbo-Beilun `li-beilun-kade` ⏹ stoppunt (aannemelijk: één bron)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `li-manono-plant` → Kiambi (RN33) | mijnweg → Bitawana → Kiambi | 80,3 gemeten (toets) | maak_stroombeen_weg, extract congo-drc | nee |
| b2 | A | truck | Kiambi → Kiambi | OSM-gat RN33 (alleen track/path) | 0,36 gemeten | stippel | ja — OSM-wegnet reikt niet |
| b3 | A | truck | Kiambi → `li-kalemie-haven` | RN33 via Kikumba–Mukanza/Nyunzu–Kitatilo–Lukengo | 352,9 gemeten; samen b1+b3 433,6 tegen 440 gepubliceerd (−1,5%) [1][2] | maak_stroombeen_weg, congo-drc, corridorKlassen tertiary | nee |
| b4 | B | binnenvaart | `li-kalemie-haven` → `li-kigoma-haven` | Tanganyikameer, vier schepen ca 2.000 t [3]; hemelsbreed 127,8 km, geen vaarkm gepubliceerd | 129,9 (kortste pad binnen het meer) | stippel-geojson, FeatureCollection | ja — meerveer, eigen verbinding zonder net |
| b5 | C | spoor | `li-kigoma-haven` → `li-dar-spoor` | Centraal-lijn (meterspoor) via Tabora–Dodoma–Morogoro — *aannemelijk: bron zegt "rail en/of road"* [1] | 1.246,1 gemeten tegen ca 1.250 gepubliceerd (SMM [1]) | toets_spoorroute (BAKE_SUFFIX=-raw), een run, geen via | nee (naad meer-spoor ca 0,2 km) |
| b6 | C | truck | `li-dar-spoor` → `li-dar-poort` | stadswegen Dar es Salaam naar Kurasini; hemelsbreed 5,8 km, geen wegkm | 7,5 gemeten (toets) | maak_stroombeen_weg, extract tanzania, vensterKm 12 | nee |
| b7 | C | truck | `li-dar-poort` → `li-dar-kade` | havenemplacement | 0,36 — letterlijke kopie b3b `kobalt-kisanfu-daressalaam` | stippel | ja — OSM-eiland, net reikt niet |
| b8 | C | zee | `li-dar-kade` → zeeknoop 5310 (-6,6537, 39,3256) | haven-aanloop, kade 20,9 km van de zeeknoop (> 5 km) | 20,9 — letterlijke kopie b4a kobalt | stippel | ja — aanloop |
| b9 | C | zee | zeeknoop Dar → zeeknoop Ningbo (29,9758, 121,9736) | Indische Oceaan → Malakka → Zuid- en Oost-Chinese Zee | 11.780,8 — letterlijke kopie b4 kobalt (*aannemelijk: bestemming niet gepubliceerd*) | MARNET | nee |
| b10 | C | zee | zeeknoop Ningbo → `li-beilun-kade` | haven-aanloop | 11,6 — letterlijke kopie b4b kobalt (`kobalt-tfm-quzhou-aanloop-ningbo.geojson`) | stippel-geojson | ja — aanloop |

Geen last-mile-benen: het wegbeen eindigt op het plantanker; `li-manono-plant` ligt op het terrein (z15), de afstand tot de eerste OSM-weg meet de bak.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-manono-plant` | mijn + plant / laadplek | Manono Northeast-plant (Manono Lithium SAS) | -7.2770, 27.4703 | haalbaarheidstoets (kandidaat) + eigen `sat_check` [11] | **bron-gelegd** (z15 gezien: groot procescomplex met blauwe daken en tanks, ommuurd terrein, tailingsbekken 2 km NO; punt ligt aan de westrand van het complex) |
| `li-kalemie-haven` | overslag truck → meerschip (stand-in voor Mutowa) | Kalemie-haven | -5.9462, 29.2017 | OSM [10]; SMM noemt Mutowa [1], Skillings/Chanzo/Model Diplomat Kalemie [2][4][6] | **aannemelijk** (z15 gezien: havenlandtong met kades, loodsen en schepen; Mutowa zelf niet te vinden en in aanbouw) |
| `li-kigoma-haven` | overslag meerschip → spoor | Kigoma-haven (Zijin-concessie sinds aug. 2025 [6]) | -4.8763, 29.6236 | OSM + Wikipedia Kigoma (-4.8833, 29.6333) [9] | **aannemelijk** (z15 gezien: puntje op de landtong, kade met loodsen 0,2–0,4 km ZO; niet op de kade zelf) |
| `li-dar-spoor` | einde spoor → truck | Dar es Salaam Centraal-lijn-einde, Nyerere Road | -6.8431, 39.2412 | haalbaarheidstoets: snapt op OSM-stationsnode 440137926 (-6.8464, 39.2450) [10] | **aannemelijk** (z15 gezien: industrie- en loodsenzone langs Nyerere Road, rangeerterrein 0,6 km ZO) |
| `li-dar-poort` | havenpoort | Dar es Salaam-havenpoort | -6.8405, 39.29378 | hergebruik, `kobalt-kisanfu-daressalaam.md` §3/§9 [11] | bron-gelegd (hergebruik) |
| `li-dar-kade` | overslag truck → zee | Dar es Salaam CT2, Kurasini (Malindi-terminal niet in OSM) | -6.8394, 39.2968 | hergebruik, kobalt-brief [11]; Malindi Terminal = Zijin-concessie [6] | bron-gelegd (hergebruik); voor dit product *aannemelijk* (ligplaats ongebrond) |
| `li-beilun-kade` | losplek (stoppunt) | Beilun Container Terminal Phase 2, Ningbo-Zhoushan | 29.9353, 121.8695 | hergebruik, kobalt-brief [11] | hergebruik; bestemming *aannemelijk: bron noemt "Chinese refineries"* |

## 4 · Via-punten (landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Bitawana (zuidoost van de plant) | -7.5030, 27.8670 | pint de uitrit zuidoostwaarts naar Kiambi i.p.v. een directe lijn oost |
| b1 | 2 | Kiambi, RN33 vóór het OSM-gat | -7.3380, 28.0088 | einde profiel 1; hier houdt het OSM-wegnet op (0,36 km track) |
| b3 | 0 | Kiambi, RN33 na het OSM-gat | -7.3352, 28.0104 | begin profiel 2 (stippel b2 ertussen) |
| b3 | 1 | Kikumba | -6.4260, 28.0490 | pint de RN33 noordwaarts naar Nyunzu |
| b3 | 2 | Mukanza (bij Nyunzu) | -5.9870, 28.0620 | pint het knooppunt Nyunzu; de weg draait hier oostwaarts |
| b3 | 3 | Kitatilo | -5.9660, 28.3810 | pint de oostelijke doorgaande weg i.p.v. een zijtak |
| b3 | 4 | Nkankulubiongo | -5.8050, 28.5830 | pint de noordelijke boog richting het meer |
| b3 | 5 | Lukengo | -5.7750, 29.1080 | pint de aanloop naar Kalemie, daarna zuidwaarts de haven in |

Alle via-punten komen uit de bindende toets (profielen in lon,lat); dorpsnamen uit Nominatim-reverse zoom 14 [10]. Spoor b5: kop en staart snappen op 0,14 km, **geen via nodig**. b6: geen via (vensterKm 12).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Manono Northeast (DMS + flotatie, in inbedrijfstelling) | Manono Lithium SAS (Zijin-groep 54,9 / Cominière 35,1 / DRC 10) | erts → spodumeenconcentraat | doel 30 kt LCE 2026; ontwerp ca 1 Mt concentraat/j | [1][2][4] |
| Mutowa-haven (in aanbouw) | niet gepubliceerd | truck → meerschip | 1 Mt/j, uitbreidbaar naar 1,8 Mt | [1] |
| Kigoma-haven + Malindi Terminal (Dar) | Zijin (concessie aug. 2025) | meerschip → spoor/truck → zeeschip | niet gepubliceerd | [6] |

## 6 · Stoppunt
De brief stopt op de Beilun-kade: geen bron noemt een Chinese raffinaderij of losplek ("not disclosed" [1]), dus fase D vervalt en de Ningbo-bestemming blijft een schematische aanlanding; fase E vervalt.

## 7 · Open punten
- **Eigendom gecorrigeerd:** Zijin-groep 54,9 / Cominière 35,1 / DRC-staat 10, niet 61/39 uit het ontwerp — drie bronnen [2][4][5].
- **Mutowa niet gevonden** (OSM, Nominatim, Wikipedia); Kalemie-haven is het stand-in, de lijn eindigt waar het bewijs eindigt [1][6].
- **Spoor of weg Kigoma → Dar is niet bevestigd** ("rail en/of road" [1]); getekend is het meterspoor. De standaardspoor Tabora–Kigoma is nog in aanbouw [1]; geen bron noemt de spooroperator.
- **Wegkm b1+b3 = 433,6 gemeten** tegen 440 [1][2]; Zijin bouwt een eigen weg Manono–Kalemie van ca 500 km [6], dus het tracé kan veranderen. RN33 heeft een OSM-gat van 0,36 km bij Kiambi (stippel b2).
- **Kalemie → Kigoma:** een rechte lijn ligt 34% buiten het meer; `maak_havenaanloop.py` gaf na 300 s geen pad, dus de stippel volgt het kortste pad binnen ne_10m_lakes (129,9 km, hemelsbreed 127,8) — geen gepubliceerde vaarkm.
- **`li-kigoma-haven` en `li-dar-spoor`** liggen niet op een aangewezen kade/station; plant staat alleen op z15 gezien. Het Dar-spoor-einde is het einde van het OSM-spoornet en niet het stadsstation.
- **Malindi Terminal** is niet in OSM; CT2 en Beilun zijn stand-ins. Jaarvolume is een doel, geen export.

## 8 · Bronnen
[1] SMM Analysis, "DRC's First Official Lithium Export Ships from Manono via Tanzania", 2026 — 22-07 vertrek Mutowa, 440-500 km weg, ca 2.000 t schepen, ca 1.250 km rail en/of road, Malindi, ca 1 Mt/j, Chinese losplek niet bekendgemaakt. https://news.metal.com/en/newscontent/104034103-smm-analysis-drcs-first-official-lithium-export-ships-from-manono-via-tanzania
[2] Skillings, "Congo begins first-ever lithium exports to China as Zijin's Manono project ships concentrate", 2026 — 440 km naar Kalemie, 30 kt LCE doel 2026, eigendom 54,9/35,1/10. https://skillings.net/congo-begins-first-ever-lithium-exports-to-china-as-zijins-manono-project-ships-concentrate/
[3] Mining Focus Africa, "Zijin Mining Expands Critical Minerals Transport Route Through Tanzania", 21-07-2026 — vier schepen ca 2.000 t, Kalemie → Kigoma, Kigoma Port en Malindi Terminal. https://miningfocusafrica.com/?p=13767
[4] The Model Diplomat, "China Wins the Lithium Race at Manono", 2026 — eigendom, productiestart mei 2026, aankomst in China verwacht okt. 2026. https://modeldiplomat.com/story/china-wins-the-lithium-race-at-manono
[5] SMM, "Zijin Mining's First Lithium Concentrate Shipment from DRC", 2026 — 22-07 Mutowa, CEEC-certificering, eigendom, volume niet bekend. https://news.metal.com/en/newscontent/104037242-zijin-minings-first-lithium-concentrate-shipment-from-drc-body
[6] The Chanzo, 21-07-2026, vier schepen ingehuldigd, concessie Kigoma/Malindi aug. 2025, weg Manono–Kalemie ca 500 km. https://thechanzo.com/2026/07/21/zijin-mining-inaugurates-four-ships-serving-dr-congo-mines-as-china-reinforces-eastern-southern-africa-critical-mineral-supply-route-through-tanzania
[7] Wikipedia, "Central Line (Tanzania)" — meterspoor Dar es Salaam–Kigoma via Dodoma; SGR parallel in aanbouw. https://en.wikipedia.org/wiki/Central_Line_(Tanzania)
[8] Wikipedia, "Port of Dar es Salaam" (-6.8351, 39.2938). https://en.wikipedia.org/wiki/Port_of_Dar_es_Salaam
[9] Wikipedia, "Kalemie" (-5.9128, 29.1906) en "Kigoma" (-4.8833, 29.6333). https://en.wikipedia.org/wiki/Kigoma
[10] OpenStreetMap (ODbL) via Nominatim — station Dar es Salaam node 440137926; reverse-lookups van de via-punten (Bitawana, Kiambi, Kikumba, Mukanza, Kitatilo, Nkankulubiongo, Lukengo). https://nominatim.openstreetmap.org
[11] `v2/design/routebrieven/kobalt-kisanfu-daressalaam.md` — hergebruikte ankers en benen b3b, b4a, b4, b4b.
[12] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-lithium-manono-ningbo-{plant,kalemie,kigoma,dar-station}.png`, 2026-10-09; spoorrun `spoorroute-lithium-manono-ningbo-kigoma-dar.geojson` (1.246,1 km, snaps 0,14/0,14 km).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Bestand:** `v2/data/stroomroute-lithium-manono-ningbo.json` (142,7 KB, versie 2, lonlat) · **13.636,7 km** · 10 benen · 7.704 punten · 6 markers · functie `bak_lithium_manono_ningbo` in `v2/tools/bak_stromen.sh` · profielen `lithium-manono-ningbo-{plant-kiambi,kiambi-kalemie,darspoor-darpoort}` in `maak_stroombeen_weg.py`.

| # | modaliteit | km gebakken | brief | naad naar vorige | stippel |
|---|---|---|---|---|---|
| b1 | truck | 80,3 | 80,3 | 0 | nee |
| b2 | truck | 0,36 | 0,36 | 0 | ja, OSM-gat RN33 |
| b3 | truck | 353,0 | 352,9 | 0 | nee |
| b4 | binnenvaart | 130,1 | 129,9 | 0 | ja, eigen verbinding zonder net |
| b5 | spoor | 1.251,7 | 1.246,1 (router) | 0,14 | nee |
| b6 | truck | 7,5 | 7,5 | 0,14 | nee |
| b7 | truck | 0,36 | 0,36 | 0 | ja, kopie b3b kobalt-kisanfu |
| b8 | zee | 20,9 | 20,9 | 0 | ja, aanloop, kopie b4a kobalt-kisanfu |
| b9 | zee | 11.780,8 | 11.780,8 | 0 | nee (MARNET) |
| b10 | zee | 11,6 | 11,6 | 0 | ja, aanloop, kopie kobalt-tfm-quzhou |

**Recept.** b1 en b3 via `wegscan_puur.py` (extract congo-drc, corridorKlassen tertiary/unclassified, vensterKm 40 resp. 50; b1 eerste 2,55 km over residential/unclassified, b3 laatste 1,83 km over kleine klassen), b6 extract tanzania vensterKm 12. b1+b3 = 433,3 km tegen 440 gepubliceerd (SMM, Skillings): -1,5%, binnen de +-15%. b5 is het bestaande spoorresultaat (`BAKE_SUFFIX=-raw`, een run, geen via; de lijn in het json telt 1.251,7 km tegen 1.246,1 routekm, +0,4% door de verdichting). b6 7,5 km tegen hemelsbreed 5,8 km: geen wegkm, indicatie. b7, b8, b9 en b10 zijn letterlijke kopieen van de regels van `kobalt-kisanfu-daressalaam` resp. `kobalt-tfm-quzhou`.

**Toets.** Grootste naad 0,14 km (meer-spoor en spoor-stadsweg, de snaps van de spoorrouter), markers alle 0 m van hun lijn, geen naad > 5 km. `toets_knikken`: 21 knikken, 0 omkeringen, 0 terugloop; de 7 scherpe hoeken zitten allemaal in de stadswegen van b6 (OSM-zigzag op `service`-wegen bij het Dar-spoor-einde en Kurasini, R 4-41 m), de 3 krappe zeebochten (R 4,6-8,4 km) liggen in de Oost-Chinese Zee en voor de Tanzaniaanse kust. `toets_rechte_benen --min-km 5`: alleen b8 (20,9 km, stippel-aanloop, per ontwerp een rechte lijn); b4 is een stippel door vijf meerpunten.

**Toelichting per stippel.** b2: de RN33 bij Kiambi staat in OSM alleen als track, 0,36 km, het wegnet reikt niet. b4: Kalemie-Kigoma is een meerveer (vier schepen van ca 2.000 t) zonder net; de vijf punten volgen het kortste pad binnen `ne_10m_lakes` (gecontroleerd: 0 m buiten het meerpolygoon), 130,1 km tegen hemelsbreed 127,8; `maak_havenaanloop.py` gaf in de brief-ronde na 300 s geen pad en is niet opnieuw geprobeerd. b7: havenemplacement Kurasini, 0,36 km. b8: CT2-kade ligt 20,9 km van zeeknoop 5310 (> 5 km), dus haven-aanloop (rechte lijn, kopie). b10: aanloop Ningbo 11,6 km (kopie, over water).

**Afwijkingen en lessen.** Geen afwijking van het ontwerp: het eindpunt Ningbo-Beilun staat in het id en in de titel. (1) De drie wegprofielen liepen in een keer door met de via-punten uit de brief; geen via-punt verplaatst. (2) Het spoorbeen is niet opnieuw gerouteerd: het geojson van de brief-ronde is hergebruikt. (3) Een meerveer past als `--stippel-geojson "binnenvaart|..."` met een FeatureCollection door lat,lon uit de meerpolygoon-toets; een kale Feature faalt. (4) Aannemelijk (een bron): het spoor Kigoma-Dar (bron zegt rail en/of road), de Dar-kade en Beilun als losplek; dat staat in de beennamen en markernamen, de lijnen zijn doorgetrokken.

