# Routebrief (licht) · uranium — Sint-Petersburg (Rusland) → Duinkerken → Orano Tricastin / Pierrelatte (Frankrijk)

**stroom-id:** `uranium-stpetersburg-pierrelatte` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken (2026-10-09)
**Keten in één zin:** Russisch verrijkt uranium (UF6 in containers/vaten, Rosatom/Tenex, fabriek onbekend) gaat per **zeeschip**
(Baltiyskiy 202, Mikhail Dudin) van de kade van Sint-Petersburg door de Oostzee en de Deense Straten naar Duinkerken en daarna per
**truck** (A25 · A26 · A5 · A31 · A6 · A7) naar Orano Tricastin bij Pierrelatte — stoppunt; reserve-as, tegenhanger van de RepU-as.
**Welke as van het verhaal:** *Russisch verrijkt uranium naar Frankrijk: de leverlijn die de sancties ontloopt.* Pierrelatte 2022/2023;
de zending van 2025 ging naar Romans of Lingen (onbevestigd). **Volume (bovengrens, geen tonnage per zending):** Russisch verrijkt
uranium naar Frankrijk **312 t in 2022** (67% van de Franse import verrijkt uranium, ~359 mln euro; 110 t in 2021) [3]; aandeel **54% in 2023,
24% in 2024** [4]; 2025 één zending tot en met september [4] en ≥112 t volgens douanecijfers in AFP-berichtgeving [7]. Eenheid t verrijkt
uranium (douanemassa, U-inhoud niet gespecificeerd, geen feed-equivalent), peiljaar 2022–2025.

## 1 · Ketenkaart
```
Russische verrijkingsfabriek (niet gedocumenteerd) ──(trein → Isotop-depot nabij SPb → truck, niet getekend [3])──►
Sint-Petersburg-kade `u-stpetersburg-kade` ──(b1 zee · Finse Golf, Oostzee, Deense Straten, Noordzee · MARNET 2.518 km)──►
Duinkerken-kade `u-duinkerken-kade` ──(b2 truck · A25-A1-A26-A5-A31-A6-A46-A7 · hemelsbreed 768 km, geen wegkm · aannemelijk: Pierrelatte 2022/2023)──►
Orano Tricastin, Pierrelatte `u-tricastin` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | Sint-Petersburg-kade → Duinkerken-kade | Finse Golf, Oostzee, Deense Straten, Noordzee, Straat van Dover | MARNET gemeten 2.517,9 km (zeeknopen 6849/6779); grootcirkel 1.993; geen gepubliceerde zeekm | MARNET | aanloop: nee (SPb-kade 4,9 km, Duinkerken-kade 2,3 km van de zeeknoop) |
| b2 | C | truck | Duinkerken-kade → Orano Tricastin | A25 (Lille) → A1/A26 (Arras–Reims) → A5 (Troyes) → A31 (Langres–Dijon) → A6 (Beaune–Mâcon) → A46 (Lyon-oost) → A7 | **hemelsbreed 768 km, geen wegkm** [indicatie; ±15%-toets geldt niet als norm]; OSRM-voorspelling 943–965 km [8] | maak_stroombeen_weg (5 Geofabrik-extracts) | nee — *aannemelijk: Pierrelatte 2022/2023; 2025 Romans of Lingen* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-stpetersburg-kade` | overslag truck → zee (kop) | Petrolesport, Gutujevski-eiland, Sint-Petersburg | 59.8909, 30.2376 | letterlijk uit `uranium-inkai-stpetersburg.md` §3 [10]; Greenpeace noemt alleen "commerciële haven" [3] | bron-gelegd (hergebruikt: z15 containerstapels, kranen, spoorbundel); of déze kade de nucleaire lading krijgt is niet gepubliceerd |
| `u-duinkerken-kade` | overslag zee → truck | Port Est Duinkerken, bulk-/stukgoedkade met loodsen en spoor (eigen keuze) | 51.0440, 2.3569 | geen bron noemt een kade: alleen "port of Dunkirk" [1][2][3][6] | **onzeker** (z17 gezien: kade van een vingerdok met loodsen, graansilo's en spooremplacement, geen containerkranen; vooral een representatief havenpunt) |
| `u-tricastin` | verrijking/ontvangst (staart, stoppunt) | Orano Tricastin, Pierrelatte, Drôme | 44.3250, 4.7167 | letterlijk uit `uranium-tricastin-romans.md` §3 / sitelaag `w-tricastin-verrijking` [10] | bron-gelegd (hergebruikt: kruis in het industriecomplex tussen A7 en het Donzère-Mondragon-kanaal) |

## 4 · Via-punten b2 (op de doorgaande autoroute, nooit in een stadscentrum; punten uit een OSRM-routecontrole, nearest ≤ 5 m van een weg [8])
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | A25 ten westen van Lille | 50.6277, 2.9602 | A25 → Lille i.p.v. A16/A26 via Calais; blijft buiten het centrum |
| b2 | 2 | A1/A26-knoop bij Arras | 50.3136, 2.8972 | pint A26 Arras–Reims i.p.v. A2/A29 via Saint-Quentin |
| b2 | 3 | A26/A4-knoop bij Reims | 49.2397, 3.9683 | randweg Reims, niet door het centrum |
| b2 | 4 | A5-begin bij Troyes | 48.2276, 4.1912 | A26 → A5 Troyes (OSRM-corridor) |
| b2 | 5 | A5/A31 bij Langres | 47.8994, 5.2237 | pint A31 Langres–Dijon i.p.v. A5 via Chaumont/Paris |
| b2 | 6 | A31/A6 bij Beaune | 47.0195, 4.8697 | Dijon–Beaune, daarna A6 zuidwaarts |
| b2 | 7 | A46 Lyon-oost (Genay–Neuville) | 45.8683, 4.9049 | corridorkeuze: Lyon-oostelijke omleiding i.p.v. A6 door het centrum; sluit na Saint-Priest weer aan op A7 (+22 km, bewust) |
| b2 | 8 | A7 bij Tain-l'Hermitage | 45.0679, 4.8709 | houdt A7 aan i.p.v. N7 door Valence; daarna 80 km zuidwaarts naar Pierrelatte |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Russische verrijking (Novouralsk/Zelenogorsk/Seversk/Angarsk, niet aangewezen) | Rosatom/Tenex | verrijkt UF6 → Isotop-depot → haven | niet gespecificeerd | [3] |
| Orano Tricastin (Georges Besse II + eindbestemming van deze zending) | Orano | verrijkt UF6; wat er met déze lading gebeurt is niet gepubliceerd | ~12% wereld-SWU ≈ ~7.800 t U feed-eq./j (fabrieksbreed, sitelaag) | [10] |

## 6 · Stoppunt
De brief stopt bij Orano Tricastin/Pierrelatte: het opgedragen eindpunt en de enige Franse bestemming die een bron voor een Russische SPb-zending noemt (20-03-2023, "une dizaine de camions" [1]; 24-08-2022 richting Rhônevallei "Pierrelatte et Romans" [3]). Fase D vervalt: Framatome bevestigde 01-12-2022 dat de zending van 29-11-2022 voor Romans-sur-Isère was [5] — dat is een eigen stroom (`uranium-tricastin-romans`), geen verlenging van déze lijn. Fase E vervalt.

## 7 · Open punten
- **Russische herkomstfabriek en Isotop-depot onbekend:** de lijn begint op de kade; het depot nabij SPb is niet gelokaliseerd [3].
- **Duinkerken-terminal niet gepubliceerd:** de Greenpeace-blokkade van 02-03-2026 vond plaats in een sluis van de haven (kade niet genoemd) [6][7]; Baltiyskiy 202 voerde 25 containers [1], dus een containerterminal (Terminal des Flandres, OSM way 1480777223, 51.0084, 2.1860, 12 km westelijker) is een even plausibel alternatief [9].
- **Bestemming wisselt:** 2022/2023 Pierrelatte en Rhônevallei (Romans); 13-10-2025 "Romans-sur-Isère of Lingen", Pierrelatte niet genoemd [2]; Lingen valt buiten deze stroom; 29-11-2022 deels per trein [3].
- **Geen wegkm gepubliceerd:** hemelsbreed 768 km; OSRM 943 km direct (via Lyon-centrum) en 965 km via A46-oost [8] — alleen indicatie, geen norm.
- **Volume is een nationale bovengrens**, niet de som van de bekende zendingen; 2025-cijfers (≥112 t) alleen secundair via AFP-berichtgeving [7].
- **Zeecorridor is bijna dezelfde als `uranium-tricastin-seversk`** (tegenrichting, andere kade): bewust reserve; op de bol geen nieuwe zeelijn.
- **SPb-kade 4,9 km van zeeknoop 6849**, net onder de aanloopgrens van 5 km; Ust-Luga (Tenex-terminal) is een tweede Russische uraniumhaven maar geen bron zet deze lading daar — niet getekend.
- **Politiek:** Rosatom-uranium staat in de EU niet onder sancties; Frankrijk blokkeert dat en de aanvoer daalde van 67% (2022) naar 24% (2024) [4].

## 8 · Bronnen
[1] Greenpeace France, persbericht 20-03-2023 (Baltiyskiy 202 uit Sint-Petersburg, 25 containers, Orano, "une dizaine de camions" naar Pierrelatte; Duinkerken, geen kade). https://www.greenpeace.fr/espace-presse/nucleaire-rosatom-livre-une-importante-cargaison-duranium-enrichi-a-la-france/
[2] Greenpeace France, persbericht 14-10-2025 (Mikhail Dudin, 12 vaten, drie Transrad-trucks, Romans-sur-Isère of Lingen). https://www.greenpeace.fr/espace-presse/nouvelle-livraison-duranium-enrichi-russe-framatome-edf-continuent-de-commercer-avec-la-russie/
[3] Greenpeace France, "La Russie, plaque tournante du commerce d'uranium", maart 2023, PDF (p.34 Isotop-depot en truck naar de commerciële haven; tabel 2 en 7: 312 t, 67%, ~359 mln; tijdlijn Mikhail Dudin 23-07, 24-08, 13-09, 29-11-2022). https://cdn.greenpeace.fr/site/uploads/2023/05/Greenpeace-Rapport-La-Russie-plaque-tournante-du-commerce-duranium-mars-2023-1-1.pdf
[4] Greenpeace France, "France-Russia: radioactive trafficking continues", jan. 2026, PDF (aandeel 67%/54%/24%; één invoer jan–sep 2025; zending 18-12-2025). https://cdn.greenpeace.fr/site/uploads/2026/02/Greenpeace-investigation-France-Russia-radioactive-trafficking-continues-2026-EN.pdf
[5] Assemblée nationale, schriftelijke vraag nr. 3961 (Mikhail Dudin in Duinkerken 29-11-2022; Framatome bevestigt Romans). https://questions.assemblee-nationale.fr/dyn/16/questions/QANR5L16QE3961.pdf
[6] Delta FM, "Dunkerque : Greenpeace revendique le blocage d'un cargo russe" (blokkade in de haven van Duinkerken, geen kade). https://www.deltafm.fr/dunkerque-greenpeace-revendique-le-blocage-d-un-cargo-russe
[7] AFP-berichtgeving over de blokkade van 02-03-2026 en de 2025-douanecijfers (≥112 t), alleen via zoekresultaat gelezen, pagina's zelf niet geopend. https://www.linfodurable.fr/commerce-nucleaire-france-russie-4-militants-de-greenpeace-en-garde-vue-apres-le-blocage-dun-cargo
[8] OSRM (router.project-osrm.org, driving), niet-officiële routevoorspelling Duinkerken → Pierrelatte 943,4 km direct en 965,4 km via de acht via-punten (A46-oost); nearest-controle van elk via-punt. Indicatie, geen km-bron.
[9] OpenStreetMap (Nominatim), "Terminal des Flandres, Loon-Plage": way 1480777223, 51.0084, 2.1860 (ODbL). https://nominatim.openstreetmap.org/search?q=Terminal+des+Flandres+Dunkerque&format=jsonv2
[10] Eigen briefs en sitelaag: `uranium-inkai-stpetersburg.md` §3 (`u-stpetersburg-kade`), `uranium-tricastin-romans.md` §3 (`u-tricastin`), `uranium-tricastin-seversk.md` §7 (Duinkerken 2022/2025), `uranium-sitelaag.json`. Eigen sat_check-blik: `v2/build-cache/satcheck/sat-uranium-stpetersburg-pierrelatte-dunkerque-kade.png` (z17).
[haalbaarheidstoets] Bindend invoerdocument (keten-id `uranium-stpetersburg-pierrelatte`): jaar in de brief, volume 312 t, aanloopregel > 5 km, vijf extracts, registratie ná ch1 — toegepast; de Duinkerken-kade is hier met sat_check gelegd (51.0440, 2.3569, MARNET 2.517,9 km).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-uranium-stpetersburg-pierrelatte.json` (221,3 KB, versie 2, lonlat, 2 benen, 3 markers, 12.020 punten) · **recept:** `bak_uranium_stpetersburg_pierrelatte()` in `v2/tools/bak_stromen.sh` (LF) · **profiel:** `uranium-stpetersburg-pierrelatte-duinkerken-tricastin` in `maak_stroombeen_weg.py`.

| # | modaliteit | van → naar | km gemeten | km brief | afwijking | punten | stippel |
|---|---|---|---|---|---|---|---|
| b1 | zee | SPb-kade → Duinkerken-kade | 2.517,9 | MARNET 2.517,9 (grootcirkel 1.993) | 0,0% | 271 | nee |
| b2 | truck | Duinkerken-kade → Orano Tricastin | 950,6 | hemelsbreed 767,6 (geen wegkm); OSRM 943,4-965,4 | +23,8% op hemelsbreed (verwacht), -0,8% / -1,5% t.o.v. OSRM-indicatie | 11.749 | nee |

**Totaal 3.468,5 km.** Naad b1 -> b2: **2,31 km** (zee eindigt op zeeknoop 6779, de kade ligt 2,3 km verderop; < 5 km, geen aanloop, procesgat zoals de brief voorzag). Markers: Tricastin 0,0 km en Duinkerken 0,0 km van de lijn; **SPb-kade 4,90 km** van de lijn (de zee-snap op zeeknoop 6849, onder de aanloopgrens van 5 km: bewust geen aanloop, zie §7).

**Recept b2 (wegscan):** `wegscan_puur.py --profiel uranium-stpetersburg-pierrelatte-duinkerken-tricastin` over vijf extracts (fr-nord-pas-de-calais, fr-picardie, fr-champagne-ardenne, fr-bourgogne, fr-rhone-alpes), venster 40 km, refs A 25 / A 1 / A 26 / A 4 / A 5 / A 31 / A 6 / A 46 / A 7, `eindToegangPrivaat`. Acht via-punten uit §4, alle op de autoroute, alle met snap <= 0,01 km (anker-uiteinden 0,13 en 0,08 km). Segmenten: Duinkerken-Lille 66,1 · Lille-Arras 49,3 · Arras-Reims 158,3 · Reims-Troyes 131,4 · Troyes-Langres 92,6 · Langres-Beaune 112,7 · Beaune-Lyon-oost 145,6 · Lyon-oost-Tain 102,3 · Tain-Tricastin 92,0 km; geen omweg-segment. 169 keerlussen gesnoeid (950,5 -> 950,4 km). De lengtewaarschuwing (+23,8% op hemelsbreed) is de verwachte: de brief gaf geen wegkm, de toets is een indicatie en de lijn valt binnen de OSRM-voorspelling (A46-oost 965,4 km). Eerste mijl 0,55 km (unclassified), laatste mijl 5,28 km (service, tertiary, unclassified) bij het Tricastin-terrein.

**Toets:** `json.load` slaagt, versie 2, `punt_formaat` lonlat, modaliteiten {zee, truck}, elk been >= 2 punten, 221 KB. `toets_rechte_benen.py --min-km 5` meldt geen recht been. `toets_knikken.py`: zee 1 knik (76,8 gr, 6,2 km straal, Oresund); truck 19 knikken, waarvan 2 echte scherpe bochten (A1/A26-knoop Arras 50.3136,2.8972) en **1 terugloop van ~120 m** bij 45.7849,4.8909 (rampelus op het A46/A43-knooppunt bij Saint-Priest; niet bijgeschoven, geen via-punt verplaatst), rest spikes <= 144 m radius rond de ankers en knooppunten.

**Bevindingen / open:** (1) b2 is geen gemeten wegkm: de +-15%-norm geldt niet. (2) SPb-kade 4,9 km van zeeknoop 6849: de lijn begint 4,9 km van de kade in de Finse Golf (net onder de aanloopgrens); een haven-aanloop zou de marker op de lijn brengen. (3) Duinkerken-kade onzeker (eigen keuze); Terminal des Flandres (51.0084,2.1860) is een even plausibel alternatief. (4) Zeecorridor is dezelfde als uranium-tricastin-seversk (tegenrichting): geen nieuwe zeelijn bedacht, maar wel een eigen been op de bol. (5) Fase D (Romans) en E vervallen; Russische fabriek en Isotop-depot niet getekend.

**Lessen:** 5 extracts samen ~480 MB pbf lopen in ~6 minuten door `wegscan_puur.py` (rhone-alpes ~2 min); eindToegangPrivaat was niet nodig voor de snap maar kostte niets. Een via-punt op de A46/A7-aansluiting (Genay-Neuville) gaf geen omweg: het OSRM-ontwerp van de brief klopte.
