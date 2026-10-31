# Routebrief (licht) · grafiet — Chedde (Frankrijk) → Le Havre → Baltimore → St. Marys → Seadrift (Texas, VS)

**stroom-id:** `grafiet-chedde-seadrift` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** nucleair isotroop grafiet NBG-18 (billets) van SGL Carbon in Chedde (Passy, Haute-Savoie) per **truck** naar Le Havre (haven aanname), per **zeeschip** naar Baltimore Seagirt (haven aanname), per **truck** naar SGL Carbon LLC in St. Marys (PA, bewerking tot reactorcomponenten) en per **truck** (aannemelijk) naar de Long Mott-kavel van X-energy/Dow bij Seadrift (Calhoun County, Texas). Geen spoor, leiding of lucht.
**Welke as van het verhaal:** *kernenergie-grafiet voor de Xe-100-reactor van Dow.* **Jaarvolume: geen tonnage gepubliceerd; 0 kt grafiet/j in sitelaag-eenheid, peiljaar 2026** (nieuwe billets starten eind 2026 [1]). Waarde: tweede order ca. US$ 90 mln (2026-10-29) op een 10-jarig raamcontract, eerste 3-jaarsaward > US$ 100 mln [1][2]; Chedde-uitbouw voor billets voor tot 8 Xe-100-reactoren per jaar [2][3].

## 1 · Ketenkaart
```
SGL Chedde, Passy `gr-chedde-sgl` ──(b1 truck · A40 → A6 → A86 zuidwest → A13 → A131 · hemelsbreed 629 km, geen wegkm · haven niet gebronnet)──►
Le Havre-kade `gr-lehavre-kade` ──(b2 haven-aanloop, stippel, 5,4 km)──(b3 zee · MARNET 6.378 km · aannemelijk: haven niet gebronnet)──►
Baltimore Seagirt `gr-baltimore-seagirt` ──(b4 truck · I-695 → I-70 → I-76 → I-99/US-220 → I-80 → PA-255 · hemelsbreed 295 km, geen wegkm)──►
SGL St. Marys (PA) `gr-stmarys-sgl` ──(b5 truck, aannemelijk: een bron noemt project Seadrift, levering niet gebronnet · I-80 → I-71 → I-65 → I-40 → I-30 → US-59 → TX-185 · hemelsbreed 2.186 km, geen wegkm)──►
Long Mott-kavel, Seadrift `gr-seadrift-kavel` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Chedde → Le Havre-kade | A40 (Nantua) → A6 (Beaune, Fontainebleau) → A86 zuidwest → A13 (Mantes, Rouen) → A131 | hemelsbreed 629 km, geen wegkm (OSRM-indicatie 791, geen bron) | maak_stroombeen_weg (profiel `grafiet-chedde-seadrift-chedde-lehavre`) | nee |
| b2 | B | zee | haven-aanloop Le Havre (kade → zeeknoop 3956) | Port 2000 → open water | 5,4 [eigen meting, MARNET-snap] | LETTERLIJKE KOPIE stippel uit `bak_uranium_tricastin_seversk` | **ja** (net reikt niet, schematisch) |
| b3 | B | zee | Le Havre → Baltimore Seagirt | Kanaal, Atlantische Oceaan, Chesapeake Bay | MARNET-droogloop 6.377,8; hemelsbreed 5.935; geen gepubliceerde zeekm | MARNET | aanloop Le Havre ja (b2); Seagirt snapt 2,67 km, nee |
| b4 | C | truck | Seagirt → SGL St. Marys | I-695 W → I-70 → I-70/I-76 (Breezewood) → I-99/US-220 → I-80 (DuBois) → PA-255 | hemelsbreed 295 km, geen wegkm (OSRM-indicatie 429, geen bron) | maak_stroombeen_weg (profiel `grafiet-chedde-seadrift-seagirt-stmarys`) | nee |
| b5 | D | truck | St. Marys → Long Mott-kavel | I-80 → I-76/I-71 → I-65 → I-40 (Memphis) → I-30 → US-59 → TX-185 | hemelsbreed 2.186 km, geen wegkm (OSRM-indicatie 2.595, geen bron) | maak_stroombeen_weg (profiel `grafiet-chedde-seadrift-stmarys-seadrift`) | nee (kavel ~0,5 km van het diagonale TX-35/185-tracé, geen last-mile-stippel verwacht) |
Beennamen: b1/b4 met "haven niet gebronnet"; b3 "zeeschip Le Havre → Baltimore Seagirt (aannemelijk: havens en vervoerwijze niet gebronnet)"; b5 "(aannemelijk: een bron noemt project Seadrift, levering niet gebronnet)". Lijnstijl doorgetrokken, behalve b2.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-chedde-sgl` | fabriek / laadplek | SGL Carbon S.A.S., Zone Industrielle de Chedde, Passy | 45.9263, 6.7285 | [1][2][8] | bron-gelegd (z15 gezien: `sat-grafiet-chedde-seadrift-chedde.png`, kruis op de langgerekte productiehallen aan de Arve, naast de A40-corridor; OSM man_made=works) |
| `gr-lehavre-kade` | overslag weg → zee | Le Havre Port 2000, kade Terminal Porte Océane | 49.4580, 0.1619 | hergebruikt letterlijk uit `uranium-tricastin-seversk.md`; **geen bron noemt de haven of kade** | onzeker (daar z16 gezien: containerkade met portaalkranen; of juist deze terminal en haven gebruikt zijn is onbekend) |
| `gr-baltimore-seagirt` | overslag zee → weg | Seagirt Marine Terminal, Baltimore | 39.2573, -76.5468 | hergebruikt letterlijk uit `nikkel-zimplats-springs.md`; **geen bron noemt de haven** | aannemelijk (daar z15 gezien: containerstacks en STS-kranen langs de zuidwestkade) |
| `gr-stmarys-sgl` | fabriek / bewerking | SGL Carbon LLC, 900 Theresia St., St. Marys (Elk County, PA) | 41.4315, -78.5423 | [1][8] | bron-gelegd (z15 gezien: `sat-grafiet-chedde-seadrift-stmarys.png`, kruis op een lang fabriekscomplex met lange hallen en spoorbundel, ten oosten van de stad) |
| `gr-seadrift-kavel` | afnemer / stoppunt | X-energy/Dow Long Mott Generating Station, grenzend aan Dow Seadrift Operations, bij Seadrift (TX) | 28.5283, -96.7619 | [4][5][6] (één coördinaatbron; GEM geeft 28.5033, -96.7745 = op de Dow-fabriek zelf) | **aannemelijk** (z15 gezien: `sat-grafiet-chedde-seadrift-seadrift-kavel.png`, kruis op open weiland direct NO van het Dow-complex en een schakelstation met samenkomende hoogspanningslijnen; nog niets gebouwd) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze; lat, lon, op de doorgaande rijbaan; gesnapt op OSM-wegvertices uit de lokale extracts, geen centrum)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | A40 bij Nantua | 46.1400, 5.6089 | pint A40 westwaarts (niet A41 naar Lyon) |
| b1 | 2 | A6 bij Beaune | 47.0153, 4.8675 | pint A6 Mâcon–Beaune (niet A5/Troyes) |
| b1 | 3 | A6 ten zuiden van Fontainebleau | 48.3535, 2.5845 | pint A6 naar Parijs |
| b1 | 4 | A86 bij A6-knooppunt | 48.7563, 2.3383 | rond Parijs zuidwest, niet de Périphérique |
| b1 | 5 | A86 bij Vélizy | 48.7792, 2.1999 | idem, westwaarts |
| b1 | 6 | A13 bij Mantes | 48.9775, 1.7142 | pint A13 naar Rouen |
| b1 | 7 | A13 bij Rouen | 49.3288, 1.0882 | A13, niet via de binnenstad |
| b1 | 8 | A131 bij Lillebonne | 49.4631, 0.4859 | pint A131/Tancarville naar Le Havre (niet A29/Pont de Normandie) |
| b4 | 1 | I-695 west van Baltimore | 39.2843, -76.7357 | beltway, niet door het centrum |
| b4 | 2 | I-70 bij Hancock (MD) | 39.6956, -78.1507 | pint I-70 westwaarts |
| b4 | 3 | I-70/I-76 bij Breezewood | 39.9896, -78.2297 | knoop I-70 → I-76 (PA Turnpike) |
| b4 | 4 | I-99/US-220 bij Altoona | 40.5095, -78.3706 | pint I-99 noordwaarts |
| b4 | 5 | I-99/US-220 bij State College | 40.8257, -77.8484 | idem, naar I-80 |
| b4 | 6 | I-80 bij DuBois | 41.1447, -78.7548 | pint de PA-255-toegang (OSRM noemde PA-120) |
| b5 | 1 | I-80 bij DuBois | 41.1447, -78.7548 | idem b4-6, zelfde punt, andere richting |
| b5 | 2 | I-71 bij Medina (OH) | 41.1068, -81.8162 | pint I-80 → I-76 → I-71 |
| b5 | 3 | I-71 bij Carrollton (KY) | 38.6260, -85.1520 | pint I-71 Cincinnati–Louisville |
| b5 | 4 | I-65 bij Bowling Green (KY) | 36.9116, -86.4313 | pint I-65 naar Nashville |
| b5 | 5 | I-40 bij Memphis | 35.1528, -90.0213 | pint de Mississippi-oversteek |
| b5 | 6 | I-30 bij Texarkana | 33.4694, -94.0563 | pint I-30 → US-59 |
| b5 | 7 | US-59 bij Lufkin | 31.3166, -94.7070 | pint US-59 zuidwaarts |
| b5 | 8 | US-59/I-69 bij Victoria | 28.7938, -96.9475 | pint de afslag naar TX-185 |
Profielen: `extracts` b1 fr-rhone-alpes, fr-bourgogne, fr-ile-de-france, fr-haute-normandie; b4 us-maryland, us-pennsylvania; b5 us-pennsylvania, us-ohio, us-kentucky, us-tennessee, us-arkansas, us-texas. `refs` b1 A40 A6 A86 A13 A131; b4 I-695 I-70 I-76 I-99 US-220 I-80 PA-255; b5 I-80 I-76 I-71 I-65 I-40 I-30 US-59 TX-185. Profiel-ankers (lon, lat) = §3.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Chedde | SGL Carbon | NBG-18-billets (uitbreiding, tot 8 Xe-100/j) | niet gepubliceerd in kt | [2][3] |
| St. Marys | SGL Carbon LLC | billets → machinale componenten (capaciteitsuitbreiding) | niet gepubliceerd | [1] |

## 6 · Stoppunt
De keten stopt bij de Long Mott-kavel (Dow Seadrift): de bestemming van het contract is het eerste commerciële Xe-100-project, de reactor wordt daar gebouwd; verder gaat geen grafiet. Fase E vervalt.

## 7 · Open punten
- **Havens niet gebronnet.** Geen bron noemt Le Havre of Baltimore; Fos (~420 km) en Genua (~330 km) liggen dichter bij Chedde. Beide zijn aannames (b1/b3 "aannemelijk"), alleen "billets uit Frankrijk naar SGL-faciliteiten in de VS verscheept" [2][3].
- **Vervoerwijze niet gebronnet** voor alle vier de landbenen en voor de zee (blokken per container of breakbulk onbekend); truck en schip zijn aannames.
- **Levering aan Seadrift niet gebronnet.** SGL noemt Seadrift alleen als project van het raamcontract [1]; waar componenten worden afgeleverd en hoe is onbekend. Valt b5 weg dan wordt het id `grafiet-chedde-stmarys` (centraal).
- **Seadrift-kavel is één coördinaatbron.** GLO-kennisgeving 2025 (centrum 28.528333, -96.761944 [6]; de pagina is inmiddels 404, alleen via zoekresultaat gezien); NRC bevestigt "grenzend aan Seadrift Operations" [4], geen coördinaat. GEM-wiki 28.5033, -96.7745 ligt 3,0 km zuidwestelijk, op de Dow-fabriek zelf; geen bewezen kavelgrens.
- **Hotspot Seadrift is dubbelzinnig:** kavel ligt 3,6 km NO van Seadrift Coke (28.5134, -96.7946, stroom `grafiet-seadrift-monterrey`). Markernaam bevat daarom "Long Mott / Dow Seadrift Operations".
- **A86-westtunnel (Duplex)** is voor licht verkeer; de router kent geen hgv-verbod: controleer b1 bij Vélizy/Rueil op een tunnelpassage en meld hem.
- **b4 volgt PA-255 (via DuBois), OSRM noemde PA-120**; de bake kiest tussen beide, geen bron voor de gereden weg.
- **Jaarvolume onbekend:** geen tonnage, alleen contractwaarden [1][2]; 0 kt is de sitelaag-conventie.
- **Sitelaag-kandidaten (centraal):** SGL Chedde, SGL St. Marys en de Long Mott-kavel staan niet in `grafiet-sitelaag.json`.
- **Geen last mile/spoorvariant:** St. Marys en het Dow-terrein hebben een spoorbundel; spoor is niet gebronnet, dus niet getekend.

## 8 · Bronnen
[1] SGL Carbon, "SGL Carbon and X-energy sign further supply contract", 2026-10-29 (US$ 90 mln, Chedde, St. Marys, Seadrift-project, geen vervoer). https://www.sglcarbon.com/en/newsroom/news/press-report/sgl-carbon-and-x-energy-sign-further-supply-contract/
[2] X-energy, "X-energy and SGL Carbon announce capacity expansion for nuclear-grade graphite", 2026-08-03 (Chedde, US$ 8 mln, 8 reactoren/j, billets naar SGL-faciliteiten in de VS). https://x-energy.com/news/x-energy-sgl-carbon-announce-capacity-expansion-for-nuclear-grade-graphite/
[3] SGL Carbon, persbericht 2026-08-03 (idem; US-sites ongenoemd). https://www.sglcarbon.com/en/newsroom/news/press-report/sgl-carbon-and-x-energy-announce-capacity-expansion-for-nuclear-grade-graphite/
[4] NRC, Federal Register 2026-10073, EA/FONSI Long Mott Generating Station (Docket 50-614): site grenzend aan Seadrift Operations, 4 Xe-100. https://public-inspection.federalregister.gov/2026-10073.pdf
[5] Wikipedia, "Long Mott Generating Station" (Dow-site Seadrift, CP-aanvraag 2025-03-31). https://en.wikipedia.org/wiki/Long_Mott_Generating_Station
[6] Texas General Land Office, kennisgeving Long Mott Energy LLC, 2025-05-19 (centrum 28.528333, -96.761944; pagina 404). https://www.glo.texas.gov/open-government/important-links-and-information/public-notices/notice-and-opportunity-comment-requests-consistency-long-mott-energy-llc
[7] GEM wiki, "Long Mott nuclear power plant" (28.5033, -96.7745). https://www.gem.wiki/Long_Mott_nuclear_power_plant
[8] OSM Nominatim: SGL Carbon S.A.S. Chedde 45.9263, 6.7285 · SGL Carbon St. Marys 41.4315, -78.5423. https://nominatim.openstreetmap.org
[9] Federal Register 2025-07729, NRC-aanvaarding CP-aanvraag Long Mott, 2025-05-16. https://www.govinfo.gov/content/pkg/FR-2025-05-16/html/2025-07729.htm
[10] Eigen briefs: `uranium-tricastin-seversk.md` (Le Havre-kade + aanloop), `nikkel-zimplats-springs.md` (Seagirt) en MARNET-droogloop (zee 6.377,8 km, snaps 5,387 / 2,674 km).
[sat] `v2/build-cache/satcheck/sat-grafiet-chedde-seadrift-{chedde,stmarys,seadrift-kavel}.png`; hergebruikt `sat-uranium-tricastin-seversk-lehavre-kade.png`, `sat-nikkel-zimplats-springs-seagirt.png`.
[via] via-punten gesnapt op ways uit de lokale pbf-caches (v2/build-cache/ais/graaf/*pbfways*) en een eigen scan van fr-*/us-texas/us-maryland.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
Functie `bak_grafiet_chedde_seadrift` in `v2/tools/bak_stromen.sh`; uitvoer `v2/data/stroomroute-grafiet-chedde-seadrift.json` (1053 KB, versie 2, lonlat, 5 benen, 53.314 punten, 10.216,6 km, 5 markers). Titel: "Grafiet · Chedde → Le Havre → Baltimore → St. Marys → Seadrift (Frankrijk → VS)".

| # | modaliteit | km gemeten | indicatie | naad | noot |
|---|---|---|---|---|---|
| b1 | truck | 776,4 | OSRM 791 (-1,8%); hemelsbreed 629 (x1,23) | 0 | A40, A6, A86/N286, A13, A131; geen gepubliceerde wegkm |
| b2 | zee (stippel) | 5,4 | eigen meting 5,4 | 0 | haven-aanloop Le Havre, letterlijke kopie uit uranium-tricastin-seversk |
| b3 | zee | 6.377,8 | droogloop 6.377,8 | 0 | MARNET, snaps 5,387 (Le Havre, via b2) en 2,674 km (Seagirt) |
| b4 | truck | 473,9 | OSRM 429 (+10,5%); hemelsbreed 295 (x1,61) | 2,67 | zee-eind op zeeknoop 4839, weg begint op de kade |
| b5 | truck | 2.583,1 | OSRM 2.595 (-0,5%); hemelsbreed 2.186 (x1,18) | 0 | I-80, I-71, I-65, I-40, I-30, US-59, TX-185 |

**Recept.** Profielen `grafiet-chedde-seadrift-chedde-lehavre` (4 fr-extracts, 9 punten), `-seagirt-stmarys` (us-maryland, us-pennsylvania, 8 punten) en `-stmarys-seadrift` (6 us-extracts, 11 punten) in `maak_stroombeen_weg.py`, gescand met `wegscan_puur.py`. b2 en b3 volgens de brief. Alle benen doorgetrokken behalve b2; geen luchtbeen, spoor of leiding. Km-toets is alleen indicatie (geen gepubliceerde wegkm).

**Toelichting en bevindingen.**
- b5 kreeg een extra via-punt `I-40 ten westen van Nashville` (-87.0245, 36.0768; een OSM-vertex op I-40). Zonder dat punt koos de router vanaf Bowling Green een westelijke route via Russellville en US-79 buiten Nashville om (413,7 km Bowling Green-Memphis) met een terugloop van ~1,4 km bij Bowling Green (via-punt op een afrit). Met het punt volgt de lijn I-65 en I-40 zoals de brief zegt (117,6 + 306,9 km), 0 teruglopen. Dit is een corridorkeuze, geen km-correctie.
- Seadrift-kavel: weg eindigt op 0,67 km van het anker (bevinding > 0,5 km, < 2 km dus geen last-mile-stippel); last mile over kleine klassen 2,47 km.
- A86-Duplex: de gemeten lijn gaat bij Velizy via A86 west en N286 naar de A13 bij Rocquencourt; de Duplex-as (Rueil-Bougival) ligt 2,5 tot 5,5 km van de lijn. Geen tunnelpassage vastgesteld (indicatie op afstand, geen tunneltag in de scancache).
- b4 volgt PA-255 via DuBois (anker 0,04 km); +10,5% op OSRM komt deels door keerlussen die de scanner knipt bij de via-punten Breezewood (11,1 km), State College (7,9) en DuBois (7,3): die via-punten liggen op een afrit of zijtak van de doorgaande weg. Niet bijgeschoven.
- Resterende omkeringen > 150 graden: Baltimore I-695-via (180 graden, 49 m), St. Marys-anker (155 graden), State College (153 graden), Lufkin (168 graden); allemaal korte afrit-bochten (router-diagnose), geen teruglopen.
- Markers: allemaal op 0 km van hun lijn. Seagirt-marker staat 2,67 km van het zee-lijneinde (< 5 km, bevinding, geen aanloop).
- Bestand 1053 KB (b5 29.562 punten, b1 14.870): boven de ~300 KB-richtlijn; centraal noteren.
- Hotspot Seadrift ligt 3,6 km van Seadrift Coke (`grafiet-seadrift-monterrey`); markernaam bevat Long Mott.

**Lessen.** Een lange Amerikaanse corridor met alleen een via-punt per stad kan buiten de genoemde stad omrijden: controleer het segment-km tegen de brief en voeg een via-punt toe op een OSM-vertex van de genoemde weg. Een via-punt op een afrit geeft een knip in `keerlussen gesnoeid`; kies het punt midden op de doorgaande rijbaan.
