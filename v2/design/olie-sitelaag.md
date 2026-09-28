# Olie-sitelaag wereldwijd — lichte ronde

*Gemaakt 2026-09-28 · werkwijze: licht (M29, `routebrief-licht.md` §1/§4) · status: concept, nog niet in
`gloednodes-olie.json` verwerkt (draai `python v2/tools/voeg_sites_toe.py --grondstof olie --schrijf` centraal).*

## Doel

Eén coördinaat op **site-niveau** (exportterminal, raffinaderij, stabilisatie-/verzamelpunt) plus een
**capaciteit in kb/d (duizend vaten/dag) mét bron en peiljaar** voor de belangrijkste oliesites wereldwijd,
zodat de wereldwijde gloedlaag voor olie echte gewichten krijgt in plaats van de huidige regionale
`data/oil.js`-centroïdes (18 knopen op landsniveau, M11). Grondslag: `data/oil.js` + `design/olie.md`
(checklist/keten-ontwerp), aangevuld met de zeven ketens en de kandidatenlijst uit deze golf se
ontwerp-oordeel (`v2/design/routebrieven/olie-*.md`, voor zover al geschreven) en de twee expliciet
gesignaleerde v1-gaten (Irak Basra/Al-Faw, Ust-Luga).

**Eenheid: `kb/d`** (duizend vaten ruwe olie of producten per dag) — passend bij olie's fungibele,
aggregaat-gepubliceerde karakter (zoals het ontwerp zelf al vaststelde). Havensites die alleen een
`Mt/jaar`-doorvoercijfer publiceren zijn omgerekend à 7,33 vaten/ton (Dongjiakou); die omrekening staat
expliciet in `capaciteit_bron`, niet in een apart veld.

## Werkwijze

- **Coördinaten** (WGS-84, lat, lon met decimale punt, 4-5 decimalen): waar mogelijk Wikipedia-geohack
  (via websearch, niet de MediaWiki-API rechtstreeks — zie hieronder) of een genoemde coördinaat uit een
  vakpersbron; voor 12 sites (de zes zwaarste bronterminals + de zes zwaarste raffinaderijen) aanvullend
  een **satellietblik** op Esri (`v2/tools/sat_check.py`, z13-z17, beelden in `v2/build-cache/satcheck/`
  met prefix `sitelaag-olie-`). Voor de overige sites is de coördinaat ofwel een gepubliceerde
  Wikipedia/vakpers-waarde (**onzeker/aannemelijk**, geen eigen satellietblik deze ronde) ofwel — bij vijf
  sites (Zhenhai, Chiba, Jurong, Galveston Bay, Abadan) plus drie `sites_zonder_gewicht` (Forcados,
  Sullom Voe, Escravos) — een schatting op stad-/industriezone-niveau uit algemene kennis, expliciet zo
  gemarkeerd. **Geen coördinaat is verzonnen**: waar geen bron gevonden is (Basra/Mina al-Bakr op
  satelliet, verschillende Afrikaanse/Aziatische raffinaderijen) blijft de status `onzeker` staan in
  plaats van een fictief punt.
- **⚠️ Firecrawl was deze sessie uitgeput** (credits op, net als bij de kolen-ronde van 26-09) — alle
  research liep via `WebSearch` in plaats van via het gebruikelijke Firecrawl-scrapepad. Dat werkte voor
  ~29 sites met een verse, citeerbare bron; **het websearch-budget van deze sessie raakte daarna op**
  (200 zoekopdrachten), waardoor acht latere kandidaten (Ust-Luga, Forcados, Sullom Voe, Escravos, en de
  cijfers voor Marathon Galveston Bay/Sinopec Zhenhai/ENEOS Chiba-coördinaat-precisie/Abadan) zonder een
  laatste verificatieronde in het rapport staan — expliciet gemarkeerd in `capaciteit_bron` met
  "websearch-budget uitgeput", niet stilzwijgend als hard cijfer gepresenteerd.
- **Satellietblik** voor de top-6 bronterminals (Ras Tanura, Yanbu, Fujairah, Kharg Island, Corpus
  Christi, Basra/Mina al-Bakr) en top-6 raffinaderijen (Jamnagar, Ulsan, ZPC Zhoushan, Yeosu, Motiva Port
  Arthur, ExxonMobil Baytown): ligt het kruis op het terrein/tankenpark/steiger → **bron-gelegd**; anders
  verschoven naar wat je wél ziet (genoteerd in `coord_bron`) → **aannemelijk**; niets zichtbaars (het
  offshore platform van Basra/Mina al-Bakr valt buiten de Esri-resolutie op die locatie) → **onzeker**.
  Van de twaalf passes: **6 bron-gelegd na één of twee correctierondes** (Ras Tanura, Yanbu, Kharg
  Island, Corpus Christi, Jamnagar, Ulsan, ZPC Zhoushan, Motiva Port Arthur, ExxonMobil Baytown — negen,
  zie de tabel), **2 aannemelijk** (Fujairah, Yeosu — dicht bij maar niet exact op het tankenpark) en
  **1 onzeker** (Basra/Mina al-Bakr, offshore, geen structuur zichtbaar).
- **Capaciteit**: ~1-2 bronnen per site, `[Bn]` naar de bronnenlijst onderaan. Voor **raffinaderijen** is
  dat de CDU-/nameplate-doorzetcapaciteit (kb/d). Voor **terminals** is, waar bekend, de **feitelijke**
  recente export-/laaddoorzet genomen in plaats van de vaak veel hogere nameplate — dat is de eerlijker
  maat voor "productie" uit de M30-eerlijkheidsregel (Kharg Island: 1.577 kb/d feitelijk tegen 7.000 kb/d
  nameplate; Bonny: 250 kb/d recent bevestigd operationeel tegen 1.250 kb/d totale terminalcapaciteit).
  Waar dat onderscheid niet gemaakt kon worden staat de aard van het cijfer (nameplate/laadcapaciteit)
  expliciet in `capaciteit_bron`.
- **Buiten scope gelaten** (met reden in het rapport): individuele Shandong-teapotraffinaderijen (er
  bestaat — zoals het ontwerp van deze ronde zelf al vaststelde — geen vrij coördinatenregister
  equivalent aan het MEE-emissieregister van koper/nikkel; `w-dongjiakou` draagt de hele cluster als
  havenanker) · SPR/strategische-voorraadsites (dat is een aparte, niet-optelbare rol met een eigen
  eenheid — hoort in een latere ronde als `eenheid_site` in mln vaten, niet in deze kb/d-stroomlijst) ·
  offshore-mijnvelden zonder vast landpunt (Pré-sal/Santos Brazilië, Tupi, Permian Basin zelf) — een
  olieveld is basin-schaal, geen site; waar een veld wél is opgenomen (Tengiz, Ghawar via Abqaiq) is dat
  via het vaste verzamel-/stabilisatiepunt, niet de put zelf.

## Sites (32 met gewicht + 7 zonder gewicht)

| id | naam | land | rol | lat, lon | capaciteit kb/d | bron | coord-bron | status |
|---|---|---|---|---|---|---|---|---|
| `w-rastanura` | Ras Tanura Refinery & Terminal | Saoedi-Arabië | terminal+raffinaderij | 26.6480, 50.1590 | 550 | Bloomberg/World Oil/CNBC 2026 [B1][B2][B3] | satelliet z15, verschoven naar het tankenpark | **bron-gelegd** |
| `w-abqaiq` | Abqaiq Stabilization Plant | Saoedi-Arabië | mijn (stabilisatie Ghawar) | 25.9286, 49.6858 | 7000 | Wikipedia/CRS [B5][B6] | Wikipedia-geohack | aannemelijk |
| `w-yanbu` | Yanbu-exportterminal (Petroline) | Saoedi-Arabië | terminal | 23.9330, 38.2500 | 4500 | wisdomandboats/ENR/geoconversation [B7][B8][B9] | satelliet z14 | **bron-gelegd** |
| `w-jubail-satorp` | SATORP-raffinaderij (Jubail) | Saoedi-Arabië | raffinaderij | 27.0333, 49.6167 | 460 | Saudipedia/TotalEnergies [B10][B11] | industriezone-schatting | **onzeker** |
| `w-fujairah` | Fujairah Oil Terminal (ADNOC) | VAE | terminal | 25.1500, 56.3200 | 1500 | Seatrade/CNBC/The National [B12][B13][B14] | satelliet z14, verschoven | aannemelijk |
| `w-ruwais` | Ruwais-raffinaderij (ADNOC) | VAE | raffinaderij | 24.1063, 52.7278 | 922 | ADNOC-corporate [B15] | Wikipedia-geohack | aannemelijk |
| `w-kharg` | Kharg Island-exportterminal | Iran | terminal | 29.2400, 50.3100 | 1577 | Mansfield/CIA/Iran Open Data [B16][B17][B18] | satelliet z13 | **bron-gelegd** |
| `w-basra-minaalbakr` | Al Başrah Oil Terminal (ABOT) | Irak | terminal | 29.6833, 48.8167 | 3000 | Wikipedia [B19] | Wikipedia-coördinaat; satelliet: niets zichtbaar | **onzeker** |
| `w-primorsk` | Primorsk-exportterminal | Rusland | terminal | 60.3450, 28.6100 | 1000 | Wikipedia/mediaberichten [B20][B21] | havencoördinaat | onzeker |
| `w-novorossiysk-sheskharis` | Novorossiysk — Sheskharis (Transneft) | Rusland | terminal | 44.7302, 37.7842 | 1000 | FleetLeaks/Moscow Times [B22][B23] | bedrijfsbron | onzeker |
| `w-cpc-novorossiysk` | CPC Marine Terminal (Yuzhnaya Ozereyevka) | Rusland | terminal | 44.6206, 37.6892 | 1400 | Wikipedia/bairdmaritime [B24][B25] | algemene kennis | onzeker |
| `w-kozmino` | Kozmino-terminal (ESPO) | Rusland | terminal | 42.7309, 133.0273 | 600 | S&P Global/GEM/Wikipedia [B26][B27][B28] | Wikipedia-coördinaat | onzeker |
| `w-ceyhan-btc` | Ceyhan-terminal (BTC) | Turkije | terminal | 36.8500, 35.9333 | 1200 | BP/SOCAR [B29][B30] | havenbron | onzeker |
| `w-corpuschristi` | Corpus Christi-exportcluster | VS | terminal | 27.8320, -97.2050 | 2500 | OilPrice/Port of CC [B31][B32] | satelliet z15, op een tank | **bron-gelegd** |
| `w-loop` | Louisiana Offshore Oil Port (LOOP) | VS | terminal | 28.8852, -90.0251 | 1200 | Wikipedia [B33] | Wikipedia-coördinaat | onzeker |
| `w-portarthur` | Motiva Port Arthur Refinery | VS | raffinaderij | 29.8850, -93.9625 | 730 | Bloomberg/Argaam/Inspectioneering [B34][B35][B36] | satelliet z14 | **bron-gelegd** |
| `w-baytown` | ExxonMobil Baytown Refinery | VS | raffinaderij | 29.7390, -95.0106 | 588 | ExxonMobil/Wikipedia [B37] | satelliet z14 | **bron-gelegd** |
| `w-galvestonbay` | Marathon Galveston Bay Refinery | VS | raffinaderij | 29.3775, -94.9241 | 631 | algemeen gepubliceerd, niet herverifieerd [B38] | algemene kennis | onzeker |
| `w-tengiz` | Tengiz-olieveld / Tengizchevroil | Kazachstan | mijn | 46.1528, 53.3833 | 870 | Interfax/Energy Intelligence [B39][B40] | Wikipedia-geohack | aannemelijk |
| `w-jamnagar` | Jamnagar Refinery Complex (Reliance) | India | raffinaderij | 22.3481, 69.8689 | 1240 | NSEnergy/oilgasstoragenews [B41][B42] | satelliet z14 | **bron-gelegd** |
| `w-vadinar` | Vadinar-raffinaderij (Nayara Energy) | India | raffinaderij | 22.3317, 69.7472 | 405 | Wikipedia/NSEnergy [B43][B44] | Wikipedia-geohack | aannemelijk |
| `w-pernis` | Shell Pernis-raffinaderij (Rotterdam) | Nederland | raffinaderij | 51.8827, 4.3833 | 404 | Hydrocarbon Processing [B45] | algemene kennis | onzeker |
| `w-antwerpen` | ExxonMobil Antwerpen-raffinaderij | België | raffinaderij | 51.2548, 4.3405 | 320 | ExxonMobil/GEO [B46][B47] | GEO-coördinaat | aannemelijk |
| `w-ulsan` | SK Energy Ulsan-raffinaderij | Zuid-Korea | raffinaderij | 35.4332, 129.3429 | 840 | Statista/Korea Times [B48][B49] | satelliet z14 | **bron-gelegd** |
| `w-yeosu` | GS Caltex Yeosu-raffinaderij | Zuid-Korea | raffinaderij | 34.8514, 127.6908 | 800 | NESFircroft [B50] | satelliet z14, verschoven | aannemelijk |
| `w-zpc-zhoushan` | Zhejiang Petroleum & Chemical (ZPC) | China | raffinaderij | 30.1520, 122.0820 | 800 | NSEnergy/GEM [B51][B52] | satelliet z14, verschoven | **bron-gelegd** |
| `w-zhenhai` | Sinopec Zhenhai Refining (Ningbo) | China | raffinaderij | 29.9538, 121.7106 | 460 | algemeen gepubliceerd, niet herverifieerd [B53] | algemene kennis | onzeker |
| `w-dongjiakou` | Dongjiakou-havencluster (Qingdao) | China | export-/importterminal | 35.9167, 120.2000 | 1000 | China Daily/Xindemarinenews [B54][B55] | algemene kennis | onzeker |
| `w-chiba` | ENEOS Chiba-raffinaderij | Japan | raffinaderij | 35.4850, 140.0300 | 155 | Hydrocarbon Processing [B56] | algemene kennis | onzeker |
| `w-jurong` | ExxonMobil Jurong Island-raffinaderij | Singapore | raffinaderij | 1.2667, 103.6833 | 592 | Investing.com/bairdmaritime [B57][B58] | algemene kennis | onzeker |
| `w-bonny` | Bonny-exportterminal (Shell/NNPC) | Nigeria | terminal | 4.4215, 7.1413 | 250 | Leadership/Premium Times [B59][B60] | kaartbron | onzeker |
| `w-abadan` | Abadan-raffinaderij | Iran | raffinaderij | 30.3392, 48.2864 | 400 | algemeen gepubliceerd, niet herverifieerd [B61] | algemene kennis | onzeker |

### Sites zonder gewicht (gedocumenteerd, geen productie-/capaciteitsbron deze ronde)

| id | naam | land | rol | lat, lon | reden |
|---|---|---|---|---|---|
| `w-habshan` | Habshan olie-/gasverzamelcomplex | VAE | mijn | 23.7667, 53.6500 | geen site-specifiek exportcijfer; capaciteit hoort bij het exportpunt Fujairah |
| `w-dasisland` | Das Island | VAE | terminal | 25.1514, 52.8736 | geen actueel, apart olie-doorzetcijfer gevonden |
| `w-ustluga` | Ust-Luga-olieterminal | Rusland | terminal | 59.6603, 28.2769 | geen apart ruwe-olie-doorzetcijfer (havencijfer is multimodaal) — door het ontwerp zelf gesignaleerd als kandidaat-tweede-as naast Primorsk |
| `w-fujian-gulei` | Fujian Gulei-project (Aramco/Sinopec) | China | raffinaderij (project) | 23.90, 117.70 | onder constructie, nog geen productie |
| `w-forcados` | Forcados-exportterminal | Nigeria | terminal | 5.3333, 5.4000 | actuele productie niet bevestigd (herhaalde sabotage/force majeure) |
| `w-sullomvoe` | Sullom Voe-terminal | VK | terminal | 60.4800, -1.2800 | nameplate sterk verouderd, actueel cijfer niet gevonden |
| `w-escravos` | Escravos-exportterminal | Nigeria | terminal | 5.8931, 5.1467 | actuele productie niet bevestigd |

## Zwaarste sites (top 8 op gewicht)

Abqaiq (7.000) · Kharg Island (1.577, feitelijk) · Jamnagar (1.240) · CPC Marine Terminal (1.400) ·
Ceyhan/BTC (1.200) · LOOP (1.200) · Basra/Mina al-Bakr (3.000) · Corpus Christi-cluster (2.500).
*(Ter herinnering: Abqaiq's 7.000 kb/d is een stabilisatie-/verzamelcapaciteit voor het hele Ghawar-veld,
geen exportterminal — vergelijk niet 1-op-1 met de terminalcijfers.)*

## Buiten scope

| kandidaat | reden |
|---|---|
| Individuele Shandong-teapotraffinaderijen (Dongjiakou/Qingdao/Lanqiao e.a.) | Geen vrij coördinatenregister gevonden equivalent aan het MEE-emissieregister van koper/nikkel — komen uit bedrijfsdisclosures/vakpers/OSM, niet uit één bron. `w-dongjiakou` draagt de havencluster als geheel. |
| Ghawar-put, Permian Basin, Pré-sal/Santos (Brazilië), West-Siberië | Olievelden zijn basin-schaal (tientallen tot honderden km²), geen site-niveau punt — een veldcentroïde is geen anker (vaste regel). Waar een veld een vast verzamel-/exportpunt heeft (Abqaiq voor Ghawar, Tengizchevroil-plant voor Tengiz) is dát punt genomen. |
| Strategische Petroleumreserves (SPR, VS/China/India/Zuid-Korea) | Niet-optelbare rol met een eigen eenheid (mln vaten voorraad, geen kb/d-stroom) — hoort als `eenheid_site` in een latere, aparte ronde, niet in deze stroomlijst (zie ook `oil-t-spr`/`design/olie.md` §M11). |
| Ceyhan Kirkuk-tak, Druzhba-pijpleiding, Baku-Novorossiysk | Pijpleidingen zijn een eigen verbinding tussen twee punten (product-specifiek), geen gedeeld net en geen site — zie het besluit "een net is productonafhankelijk, een eigen verbinding niet" in `CLAUDE.md` §D. De terminuspunten (Ceyhan, Novorossiysk) staan wel in de lijst. |
| Marokko/Egypte/Golf-raffinaderijen (Ras Lanuf, Suez-cluster, Skikda) | Evident relevant voor de Suez/Bab-el-Mandeb-as maar deze ronde niet onderzocht (tijdbox; websearch-budget raakte op vóórdat deze aan de beurt kwamen). |

## Open punten

- **Websearch-budget raakte op na ~28 zoekopdrachten** (van de 200 voor deze sessie) — acht sites/cijfers
  (Ust-Luga, Forcados, Sullom Voe, Escravos, Galveston Bay, Zhenhai, Chiba-coördinaat, Abadan) staan met
  algemeen-bekende cijfers die deze ronde niet met een losse bron herverifieerd zijn. Expliciet gemarkeerd
  in `capaciteit_bron`/`coord_bron`, niet stilzwijgend als hard cijfer gepresenteerd. Eerste kandidaten
  voor een volgende ronde.
- **Basra/Mina al-Bakr blijft coördinaat-onzeker**: de Wikipedia-coördinaat (offshore, Perzische Golf)
  toont op Esri op z14 én z17 geen enkele structuur — het platform is te klein voor de beschikbare
  capture of de tegel ontbreekt op die exacte plek. Dit was wél het belangrijkste gesignaleerde v1-gat
  (Irak, #2 OPEC-exporteur) en staat daarom toch in de lijst, status `onzeker`.
- **Kozmino-cijfer is intern tegenstrijdig**: de gevonden "laadcapaciteit 300.000 vaten/dag" oogt laag
  tegen de historisch gerapporteerde jaarlijkse verscheping (orde 30-36 Mt/jaar ≈ 600-720 kb/d); hier
  conservatief 600 kb/d aangehouden — vraagt een gerichte hercontrole.
- **Bonny en de Nigeriaanse terminals in het algemeen zijn productie-instabiel** (herhaalde sabotage/
  force majeure over de afgelopen jaren) — het gekozen cijfer (250 kb/d, recent bevestigd operationeel)
  kan binnen maanden weer verouderd zijn; dit is inherent aan deze grondstof/regio, niet een
  onderzoeksgat.
- **Geen vrije Chinese teapot-registerbron gevonden** (zoals het ontwerp van deze ronde zelf al
  voorspelde) — blijft een open punt voor een eventuele diepere Shandong-ronde.
- **SPR/strategische voorraden zijn bewust buiten deze stroomlijst gehouden** (zie Buiten scope) — een
  volgende ronde kan die als `eenheid_site`-uitzondering toevoegen, net als de opslag-noot bij de
  eenheidsomschrijving voorschrijft.

## Bronnen

- **[B1]** Bloomberg (18-3-2026), "Saudi Arabia's Ras Tanura Refinery Has Restarted Operations" — https://www.bloomberg.com/news/articles/2026-03-18/saudi-arabia-s-ras-tanura-refinery-has-restarted-operations
- **[B2]** World Oil (18-3-2026), "Aramco brings Ras Tanura refinery back online following Gulf attacks" — https://www.worldoil.com/news/2026/3/18/aramco-brings-ras-tanura-refinery-back-online-following-gulf-attacks/
- **[B3]** CNBC (27-6-2026), "Saudi Aramco resumes oil loading at Ras Tanura in boost to supply" — https://www.cnbc.com/2026/06/27/saudi-aramco-resumes-oil-loading-at-ras-tanura-in-boost-to-supply.html
- **[B4]** Wikipedia, "Ras Tanura" — https://en.wikipedia.org/wiki/Ras_Tanura
- **[B5]** Wikipedia, "Abqaiq" — https://en.wikipedia.org/wiki/Abqaiq
- **[B6]** EveryCRSReport, "Abqaiq Facility" — https://www.everycrsreport.com/files/20191001_IN11173_7532e63c088a7570f3182f0c7b5ff3767678164c.html
- **[B7]** wisdomandboats (Substack), "Yanbu Analysis: The East-West Pipeline, Port Congestion, & Actual Export Capacity" — https://wisdomandboats.substack.com/p/yanbu-analysis-the-east-west-pipeline
- **[B8]** Engineering News-Record, "Hormuz Bypass Infrastructure Was Sized for a Short Disruption. This Is Not That." — https://www.enr.com/articles/62677-hormuz-bypass-infrastructure-was-sized-for-a-short-disruption-this-is-not-that
- **[B9]** geoconversation.org, "Saudi Aramco Pushes East-West Pipeline Throughput to 7 Million Barrels Per Day" — https://geoconversation.org/en/news/saudi-aramco-pushes-east-west-pipeline-to-all-time-throughput-record/ ; vision2030.ai, "Petroline Explained" — https://vision2030.ai/encyclopedia/petroline-east-west-pipeline/
- **[B10]** Saudipedia, "SATORP Refinery" — https://saudipedia.com/en/satorp-refinery
- **[B11]** TotalEnergies, "The SATORP Platform" — https://totalenergies.com/company/projects/oil/satorp-refining-petrochemical-platform-saudi-arabia
- **[B12]** Seatrade Maritime, "ADNOC fast-tracks Fujairah pipeline expansion" — https://www.seatrade-maritime.com/tankers/adnoc-fast-tracks-fujairah-pipeline-expansion
- **[B13]** CNBC (20-5-2026), "UAE says new pipeline that will bypass Strait of Hormuz is nearly 50% complete" — https://www.cnbc.com/2026/05/20/uae-pipeline-strait-hormuz-iran-war-oil.html
- **[B14]** The National (15-5-2026), "UAE's West-East pipeline expansion to become operational in 2027" — https://www.thenationalnews.com/business/energy/2026/05/15/uaes-west-east-pipeline-expansion-to-become-operational-in-2027-doubling-oil-export-capacity/
- **[B15]** Wikipedia, "Ruwais refinery" — https://en.wikipedia.org/wiki/Ruwais_refinery
- **[B16]** Mansfield Energy, "What's That: Kharg Island" — https://mansfield.energy/2026/05/13/whats-that-kharg-island/
- **[B17]** Iran Open Data, "Kharg Island: The Chokepoint Behind 96% of Iran's Oil Exports" — https://iranopendata.org/en/article/305-iran-energy-chokepoint-strait-of-hormuz/
- **[B18]** CIA Reading Room, "Khark Island: Iran's Principal Oil Export Terminal" — https://www.cia.gov/readingroom/node/1621531
- **[B19]** Wikipedia, "Al Başrah Oil Terminal" — https://en.wikipedia.org/wiki/Al_Ba%C5%9Frah_Oil_Terminal
- **[B20]** Wikipedia, "Baltic Pipeline System" — https://en.wikipedia.org/wiki/Baltic_Pipeline_System
- **[B21]** Militarnyi, "Drones Hit Fuel Tanks at Primorsk, Russia's Largest Baltic Oil Port" — https://militarnyi.com/en/news/drones-hit-fuel-tanks-at-primorsk-russia-s-largest-baltic-oil-port/
- **[B22]** FleetLeaks, "Novorossiysk (Sheskharis)" — https://fleetleaks.com/terminals/novorossiysk-sheskharis/
- **[B23]** The Moscow Times (6-4-2026), "Ukraine Hits Major Oil Terminal in Southern Russia" — https://www.themoscowtimes.com/2026/04/06/ukraine-hits-major-oil-terminal-in-southern-russia-moscow-a92430
- **[B24]** Wikipedia, "Caspian Pipeline Consortium" — https://en.wikipedia.org/wiki/Caspian_Pipeline_Consortium
- **[B25]** Baird Maritime, "CPC terminal loading problems slow Tengiz oilfield output recovery" — https://www.bairdmaritime.com/offshore/drilling-production/cpc-terminal-loading-problems-slow-tengiz-oilfield-output-recovery
- **[B26]** S&P Global, "Russia crude oil pipeline capabilities to mainland China — The ESPO crude oil pipeline" — https://www.spglobal.com/energy/en/research-analytics/espo-crude-oil-pipeline
- **[B27]** Wikipedia, "Eastern Siberia–Pacific Ocean oil pipeline" — https://en.wikipedia.org/wiki/Eastern_Siberia%E2%80%93Pacific_Ocean_oil_pipeline
- **[B28]** Wikipedia, "Kozmino (port)" — https://en.wikipedia.org/wiki/Kozmino_(port)
- **[B29]** BP, "Baku-Tbilisi-Ceyhan pipeline" — https://www.bp.com/en_az/azerbaijan/home/who-we-are/operationsprojects/pipelines/btc.html
- **[B30]** SOCAR, "Baku-Tbilisi-Ceyhan (BTC) Main Export Oil Pipeline" — https://socar.az/socar/en/activities/transportation/baku-tbilisi-ceyhan-btc-main-export-oil-pipeline
- **[B31]** OilPrice.com, "Corpus Christi Is Now The World's Third-Largest Oil Export Port" — https://oilprice.com/Energy/Crude-Oil/Corpus-Christi-Is-Now-The-Worlds-Third-Largest-Oil-Export-Port.html
- **[B32]** Discovery Alert, "Port of Corpus Christi: Inside America's Crude Oil Export Powerhouse" — https://discoveryalert.com.au/port-corpus-christi-crude-oil-exports-us-export-hub/
- **[B33]** Wikipedia, "Louisiana Offshore Oil Port" — https://en.wikipedia.org/wiki/Louisiana_Offshore_Oil_Port
- **[B34]** Bloomberg (11-2-2025), "Aramco's Motiva Expands Texas Refinery to Become Largest in US" — https://www.bloomberg.com/news/articles/2025-02-11/aramco-s-motiva-expands-texas-refinery-to-become-largest-in-us
- **[B35]** Argaam, "Aramco's Motiva expands Texas refinery to become largest in US" — https://www.argaam.com/en/article/articledetail/id/1789397
- **[B36]** Inspectioneering (13-2-2025), "Motiva Port Arthur Becomes the Largest Refinery in the US" — https://inspectioneering.com/news/2025-02-13/11445/motiva-port-arthur-becomes-the-largest-refinery-in-the-us
- **[B37]** Wikipedia, "Baytown Refinery" — https://en.wikipedia.org/wiki/Baytown_Refinery ; ExxonMobil, Baytown Complex Company Profile — https://corporate.exxonmobil.com/-/media/global/files/locations/united-states-operations/baytown/baytown-complex-2024-fact-sheet.pdf
- **[B38]** Algemeen gepubliceerd cijfer (Marathon Petroleum-corporate/vakpers); deze ronde niet met een losse zoekopdracht herbevestigd (websearch-budget uitgeput).
- **[B39]** Interfax, "Production at Tengiz field rises to 870,000 bpd of oil in January - Kazakh Energy Ministry" — https://interfax.com/newsroom/top-stories/109596/
- **[B40]** Energy Intelligence, "Tengiz Expansion Gives Kazakh Capacity a Boost" — https://www.energyintel.com/00000194-b37e-d625-ab9e-b3ff980b0000
- **[B41]** oilgasstoragenews, "Reliance Industries Jamnagar Refinery: 1.24m bpd 2026" — https://oilgasstoragenews.com/reliance-industries-jamnagar-refinery/
- **[B42]** Wikipedia, "Jamnagar refinery" — https://en.wikipedia.org/wiki/Jamnagar_refinery
- **[B43]** Wikipedia, "Vadinar Refinery" — https://en.wikipedia.org/wiki/Vadinar_Refinery
- **[B44]** NSEnergy, "Nayara Energy-operated Vadinar Refinery, Gujarat, India" — https://www.nsenergybusiness.com/projects/vadinar-refinery-gujarat-india/
- **[B45]** Hydrocarbon Processing (2026), "Shell restarts crude unit at Pernis oil refinery" — https://www.hydrocarbonprocessing.com/news/2026/04/shell-restarts-crude-unit-at-pernis-oil-refinery/
- **[B46]** Global Energy Observatory, "ExxonMobil Antwerp Refinery" — https://globalenergyobservatory.org/geoid/6518
- **[B47]** NSEnergy, "ExxonMobil's Antwerp Oil Refinery Expansion, Belgium" — https://www.nsenergybusiness.com/projects/antwerp-oil-refinery-expansion/
- **[B48]** Statista, "South Korea: oil refineries by daily capacity 2023" — https://www.statista.com/statistics/1290365/south-korea-oil-refineries-by-daily-capacity/
- **[B49]** Korea Times (29-3-2020), "SK Energy's Ulsan facility ready for operation" — https://www.koreatimes.co.kr/business/companies/20200329/sk-energys-ulsan-facility-ready-for-operation
- **[B50]** NESFircroft, "Exploring the 6 Largest Refineries In The World" — https://www.nesfircroft.com/resources/blog/exploring-the-6-largest-refineries-in-the--world/
- **[B51]** NSEnergy, "Zhoushan Green Petrochemical Base" — https://www.nsenergybusiness.com/projects/zhoushan-green-petrochemical-base/
- **[B52]** Global Energy Monitor, "Zhejiang Petrochemical Plant" — https://www.gem.wiki/Zhejiang_Petrochemical_Plant
- **[B53]** Algemeen gepubliceerd cijfer (Sinopec-corporate/vakpers); deze ronde niet met een losse zoekopdracht herbevestigd (websearch-budget uitgeput).
- **[B54]** China Daily (25-8-2023), "Dongjiakou builds China's largest coastal oil storage facility" — http://regional.chinadaily.com.cn/ensd-port/2023-08/25/c_913699.htm
- **[B55]** China Daily (5-12-2022/4-1-2019), Qingdao Port crude terminal/pipeline-berichten — http://regional.chinadaily.com.cn/ensd-port/2022-12/05/c_836784.htm ; https://www.chinadaily.com.cn/a/201901/04/WS5c2efc38a31068606745eeee.html
- **[B56]** Hydrocarbon Processing (2026), "Japan's Eneos restarts 155,100-bpd Chiba CDU after unplanned shutdown" — https://www.hydrocarbonprocessing.com/news/2026/08/japans-eneos-restarts-155-100-bpd-chiba-cdu-after-unplanned-shutdown/
- **[B57]** Investing.com, "Exxon Mobil starts up new Singapore refining unit, boosts sour crude imports" — https://www.investing.com/news/commodities-news/exxon-mobil-begins-production-at-new-base-stock-facilities-in-singapore-4250261
- **[B58]** Baird Maritime, "ExxonMobil's Singapore refinery starts up a new unit, expanding high-sulphur crude intake" — https://www.bairdmaritime.com/shipping/ports/exxonmobils-singapore-refinery-starts-up-a-new-unit-expanding-high-sulphur-crude-intake
- **[B59]** Leadership (Nigeria), "Shell's 250,000bpd Bonny Export Terminal Restarts Operation" — https://leadership.ng/shells-250000bpd-bonny-export-terminal-restarts-operation/
- **[B60]** Premium Times Nigeria, "Shell resumes crude oil export operations at Bonny Terminal" — https://www.premiumtimesng.com/business/business-news/587968-shell-resumes-crude-oil-export-operations-at-bonny-terminal.html
- **[B61]** Algemeen gepubliceerd cijfer (NIORDC/vakpers); deze ronde niet met een losse zoekopdracht herbevestigd (websearch-budget uitgeput).
- **[B62]** Wikipedia, "Das Island" — https://en.wikipedia.org/wiki/Das_Island
- **[B63]** Ports Directory, "UST-LUGA Port" — https://ports.marinelink.com/ports/port/ust-luga
- **[B64]** EISA-Moscow, "Ust-Luga" — https://www.eisa-moscow.ru/port/ust-luga/
- **[B65]** China Daily Fujian (20-11-2024), "Fujian Gulei Refining, Petrochemical Integration Project Enters Second Phase" — https://subsites.chinadaily.com.cn/fujian/2024-11/20/c_1046485.htm
- **[B66]** Aramco, "Aramco, SINOPEC, and Fujian Petrochemical break ground on new refining and petrochemical project in China" — https://www.aramco.com/en/news-media/news/2024/aramco-sinopec-and-fujian-petrochemical-break-ground-on-new-refining-and-petrochemical-project
- **[B67]** Algemeen bekende nameplate (Shell/SPDC-corporate/vakpers); actuele status deze ronde niet bevestigd (websearch-budget uitgeput).
- **[B68]** Algemeen bekende nameplate (EnQuest/Repsol Sinopec-corporate/vakpers); actueel cijfer deze ronde niet gevonden (websearch-budget uitgeput).
- **[B69]** Algemeen bekende nameplate (Chevron Nigeria-corporate/vakpers); actuele status deze ronde niet bevestigd (websearch-budget uitgeput).

Coördinaatbronnen: Wikipedia (via WebSearch, niet rechtstreeks de MediaWiki-API `prop=coordinates` —
Firecrawl was uitgeput), vakpers/bedrijfsbronnen zoals hierboven geciteerd, Esri World Imagery via
`v2/tools/sat_check.py` voor de twaalf satellietchecks (beelden `sat-sitelaag-olie-*.png` in
`v2/build-cache/satcheck/`).
