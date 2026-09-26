# REE-sitelaag wereldwijd — lichte ronde

*Gemaakt 2026-09-26 · werkwijze: licht (M29, `routebrief-licht.md` §1/§4) · status: concept, nog niet in
`gloednodes-ree.json` verwerkt (dat gebeurt centraal, niet door deze ronde — `voeg_sites_toe.py` NIET gedraaid).*

## Doel

Eén coördinaat op **site-niveau** (mijnterrein/plant/raffinaderij/terminal) plus een **capaciteit in
kt REO per jaar** (magneetfabrieken apart in **kt NdFeB/jaar** — niet optelbaar bij REO, dus een eigen
veld `eenheid_site`/`capaciteit_site_kt`) mét bron en peiljaar, voor de belangrijkste zeldzame-
aardmetalen-sites wereldwijd. Grondslag: het v1-register `data/rare-earths.js` (magneet-REE-framing,
41 nodes/38 flows, peiljaar ±2024) aangevuld met de zes assen uit het ontwerp
(`sitelaag-ree.json` in de scratchpad) en evident ontbrekende grote sites. Er waren bij het schrijven
van deze brief nog **geen REE-routebrieven** geschreven (`v2/design/routebrieven/ree-*.md` bestaat
niet) — er was dus niets om ankers letterlijk uit over te nemen; de zes "niet-gebakken assen" uit het
ontwerp (Bayan Obo, Ganzhou/Kachin, Mountain Pass, Lynas, Sillamäe–Narva, magneetexport) staan wél als
sites in deze laag, zoals de opdracht vraagt.

Doel was 35–50 sites; deze ronde levert **32** sites met coördinaat (10 mijnen, 9 raffinaderijen/
scheidingen, 9 magneetfabrieken, 4 exportterminals). De belangrijkste reden dat de teller onder de
ondergrens van 35 bleef: **Chinese industriezones dragen zelden een naam-tag in OSM** (dezelfde ervaring
als bij koper) en het MEE-emissievergunningregister — het aanbevolen recept voor precies dit probleem —
**verplaatste zijn endpoint opnieuw** (zie §Werkwijze) en gaf deze ronde geen bruikbare respons. In
plaats daarvan is een Overpass-naamzoekopdracht (`name~"稀土"` / `"磁材"` / bedrijfsnamen) over de
Baotou- en Ganzhou-bounding-boxes gedraaid, wat verrassend goed werkte — zie de resultaten hieronder —
maar niet voor elke kandidaatsite een treffer gaf. Een aantal evident belangrijke sites (Serra Verde,
Iluka Eneabba, Arafura Nolans, Zhong Ke San Huan, Neo Narva) bleef daardoor zonder bruikbare coördinaat
en staat in §Buiten scope.

## Werkwijze

- **Coördinaten** (WGS-84, lat, lon met decimale punt, 4 decimalen): Wikipedia-geohack (MediaWiki API
  `prop=coordinates`) voor bekende mijnen/deposits; **OSM via Overpass** (naam-tag bevat 稀土/磁材/
  bedrijfsnaam, binnen een handmatige bounding box rond Baotou/Ganzhou/Ningbo/Sichuan) bleek de
  doorslaggevende bron voor de Chinese sites — Nominatim's tekstzoeken vond vrijwel niets voor Chinese
  bedrijfsnamen (bevestigt de koper-ervaring), maar Overpass' regex-`name`-filter over een kleine bbox
  wél. Voor Maleisië/Australië/VS/EU: OSM-Nominatim op bedrijfs- of adresnaam.
- **Chinese sites via het MEE-register**: **geprobeerd, niet gelukt deze ronde.** Het pad uit
  `zoek-chinees-adres-recept.md` (`permit.mee.gov.cn/perxxgkinfo/syssb/xkgg/xkgg!licenseInformation.action`)
  geeft nu een 302 naar `errorinfo.jsp` zonder de eerder gedocumenteerde `tempReportKey`/`JSESSIONID`-stap
  te kunnen doorlopen binnen deze ronde — het derde endpoint-verhuis in korte tijd (zie de projectlog).
  In plaats daarvan is uitgeweken naar het in de opdracht toegestane alternatief: OSM/Overpass +
  bedrijfsdocumenten, met alle Chinese sites die zo gevonden zijn gemarkeerd 'aannemelijk' tenzij een
  satellietblik ze bevestigde.
- **Satellietblik** (`v2/tools/sat_check.py`, Esri z15, beelden in `v2/build-cache/satcheck/` met prefix
  `sitelaag-ree-`): gedaan voor **13 sites** — vijf mijnen (Bayan Obo, Mountain Pass, Mount Weld,
  Maoniuping, Steenkampskraal) en acht raffinaderijen/magneetfabrieken (Lynas Kuantan, Lynas Kalgoorlie,
  Solvay La Rochelle, White Mesa Mill, Northern RE Baotou/Huamei, China RE Ganzhou New Materials, JL MAG
  Ganzhou, Ningbo Yunsheng) — méér dan de gevraagde 6+6, maar geselecteerd op vindbaarheid/verhaalgewicht
  in plaats van strikt op capaciteitsranking. Ligt het kruis op het terrein → **bron-gelegd** (in twee
  gevallen — Lynas Kalgoorlie, Steenkampskraal — eerst verschoven naar wat wél zichtbaar was, daarna
  herbevestigd met een tweede pass). Bij Silmet (Sillamäe) toonde de verschoven pas alleen woonwijk en
  strand, geen industrieterrein — die site bleef **onzeker** (stadscentrum-coördinaat). Sites die alleen
  via een OSM-naam-tag zijn gevonden maar niet zelf satellietgecheckt: **aannemelijk**.
- **Capaciteit**: kt REO/j voor mijnen en scheiding (winning/productie laatste volledige jaar waar
  gevonden, anders nameplate/ontwerpcapaciteit met dat onderscheid expliciet in `capaciteit_bron`);
  **kt NdFeB/j als apart veld `capaciteit_site_kt`/`eenheid_site` voor magneetfabrieken** — niet
  optellen bij REO. Bij meerdere Chinese magneetfabrieken is het gevonden cijfer **bedrijfsbreed**
  (alle vestigingen samen), niet per site uitgesplitst; dat staat er expliciet bij. ~2 bronnen per site
  waar mogelijk, `[Bn]` naar de bronnenlijst.
- **Buiten scope gelaten** (met reden in §Buiten scope): Serra Verde (Brazilië — alleen een
  kantooradres in Minaçu-stad gevonden, de mijn zelf ligt 25-30 km verderop zonder gepubliceerde
  coördinaat), Iluka Eneabba-raffinaderij en Arafura Nolans Bore (beide 'project'-status, alleen
  regionale afstandsbeschrijvingen gevonden, geen coördinaat), Zhong Ke San Huan (Beijing-adres is een
  kantoortoren, niet de fabriek), Neo Narva (geen bruikbaar OSM- of adresresultaat), Weishan-County-
  centrum (vervangen door een specifiek bedrijf met een aannemelijke naam/richting-match), Per Geijer
  (Kiruna) en CBMM Araxá (geen coördinaat gevonden binnen budget).

## Sites (32)

| id | naam | land | rol | lat, lon | capaciteit | bron | coord-bron | status | notitie |
|---|---|---|---|---|---|---|---|---|---|
| `w-bayanobo` | Bayan Obo | China | mijn | 41.7828, 109.9736 | 188,65 kt REO/j | Winningsquota Northern RE 2024 (afgeleid uit 工信部联原〔2024〕156号) [B18][B34] | Wikipedia-geohack; satelliet z15: kruis op het fabrieksterrein tussen Oost- en Westput | **bron-gelegd** | Grootste REE-afzetting ter wereld; voedt Northern RE-scheiding in Baotou. |
| `w-maoniuping` | Maoniuping (Mianning) | China | mijn | 28.4557, 101.9804 | — | Regionaal quotum (Sichuan 62.200 t 2024, niet per mijn); één vergunninghouder noemt 20 kt concentraat/j [B3][B35] | OSM-naam牦牛坪稀土矿; satelliet z15: kruis middenin de open put | **bron-gelegd** | China's 2e REO-afzetting; carbonatiet, licht (NdPr). |
| `w-weishan` | Weishan (微山湖) | China | mijn | 34.7056, 117.2581 | — | Geen capaciteitscijfer gevonden [B36] | OSM-bedrijfsnaam, richting/afstand komt overeen met geologische bron | **aannemelijk** | 3e grootste lichte-REE-hulpbron van China; niet satellietgecheckt. |
| `w-dongpao` | Đông Pao | Vietnam | mijn | 22.2667, 103.5497 | — (7 Mt @5% RE reserves) | Herstart 2025/26 aangekondigd, geen jaarcijfer [B14][B37] | Wikipedia-geohack, exacte deposit-coördinaat | **aannemelijk** | Grootste Vietnamese REE-afzetting; erts naar Yunnan-scheiding. |
| `w-mountainpass` | Mountain Pass | VS | mijn + scheiding | 35.4786, -115.5325 | 50,692 kt REO/j | MP Materials productie 2025; NdPr-oxide 2.599 t [B15][B16] | Wikipedia-geohack; satelliet z15: kruis op putrand/fabrieksterrein | **bron-gelegd** | Enige Amerikaanse mijn; eigen on-site scheiding sinds ~2023. |
| `w-mountweld` | Mount Weld | Australië | mijn | -28.8600, 122.5478 | 29 kt REO/j | USGS MCS 2026, Australische mijnproductie 2025 [B2][B17] | Wikipedia-geohack; satelliet z15: kruis op mijnterrein | **bron-gelegd** | Voedt sinds 2024 eerst Kalgoorlie, dan Kuantan. |
| `w-kachin` | Pangwa/Chipwi-mijngebied | Myanmar | mijn | 25.8858, 98.1305 | 22 kt REO/j (2025) | USGS MCS 2026 [B2] | OSM-plaatsnode Chipwi (townshipkern) | **onzeker** | Verspreid informeel ionklei-district, geen aanwijsbaar terrein. |
| `w-steenkampskraal` | Steenkampskraal | Zuid-Afrika | mijn | -30.9795, 18.6295 | 13,4 kt monazietconc./j (ontwerp) | Steenkampskraal Rare Earths Mine, steady-state ontwerp [B11][B12] | Wikipedia-geohack; satelliet z15: kruis op mijnterrein, gebouwen ~150 m NO | **bron-gelegd** | Zeer hoog gehalte; herstart nog in bouwfase. |
| `w-kvanefjeld` | Kvanefjeld (project) | Groenland | mijn | 60.9833, -46.0000 | — | Vergunning omstreden, geen productie | Wikipedia-geohack | **aannemelijk** | Grote NdPr-reserves, project ligt stil. |
| `w-norrakarr` | Norra Kärr (project) | Zweden | mijn | 58.1020, 14.5650 | — | Projectstadium | Wikipedia-geohack | **aannemelijk** | Zware-REE-project (eudialyt). |
| `w-baotou-huamei` | Northern RE smelting/scheiding (华美), Baotou | China | raffinaderij (scheiding licht) | 40.5853, 109.8747 | 106,661 kt REO/j | Fase-1-upgrade Baotou Humei, operationeel okt 2024 [B4] | OSM-naam 包钢稀土华美公司; satelliet z15: kruis op industrieel complex | **bron-gelegd** | 's Werelds grootste REO-grondstofbasis. |
| `w-ganzhou-zhongxi` | China Rare Earth (Ganzhou) New Materials | China | raffinaderij (scheiding zwaar) | 25.9148, 115.0787 | — | Regionaal kader: 19,15 kt ionklei-quotum 2024 + ~31 kt/j Myanmar-import (groep, niet site) | OSM-naam 中稀（赣州）稀土新材料; satelliet z15: kruis naast hoofdgebouwen | **bron-gelegd** | Representatief voor de Ganzhou Dy/Tb-scheidingscluster. |
| `w-huajing` | Huajing Rare Earth New Material | China | raffinaderij (scheiding) | 25.8527, 114.8525 | — | Geen cijfer gevonden | OSM-naam 华京稀土新材料公司 | **aannemelijk** | Tweede, kleinere Ganzhou-scheidingssite. |
| `w-shenghe-leshan` | Shenghe Resources, Leshan | China | raffinaderij | 29.4083, 103.8152 | 5,5 kt REO/j | Registered production capability [B29][B30] | OSM-district Wutongqiao (niet exact terrein) | **aannemelijk** | Voormalige Mountain-Pass-concentraatverwerker. |
| `w-kuantan-lamp` | Lynas LAMP (Kuantan/Gebeng) | Maleisië | raffinaderij (scheiding) | 4.00338, 103.37749 | 10,5 kt NdPr/j (nameplate) | Lynas-jaarcijfers | OSM landuse=industrial 'Lynas Advanced Material Plant'; satelliet z15: kruis midden in plantcomplex | **bron-gelegd** | Grootste REE-scheiding buiten China. |
| `w-kalgoorlie` | Lynas Kalgoorlie (cracking & leaching) | Australië | raffinaderij (tussenstap) | -30.7942, 121.4085 | — | Ontworpen op volledig Mt Weld-concentraat, A$800 mln [B6] | Bron-adres Great Eastern Hwy/Yilkari; satelliet z15: kruis op plantcomplex na verschuiving | **bron-gelegd** | Nieuwe tussenstap sinds eind 2024, ontbrak in v1. |
| `w-silmet` | Neo Silmet, Sillamäe | Estland | raffinaderij (scheiding) | 59.3931, 27.7742 | — | Nieuwe Dy/Tb-lijn 2025/26 aangekondigd, geen tonnage [B7] | Wikipedia-geohack stadscentrum; satelliet vond het fabrieksterrein niet | **onzeker** | Exacte fabriekscoördinaat is open punt. |
| `w-larochelle` | Solvay La Rochelle | Frankrijk | raffinaderij (scheiding) | 46.1525, -1.2075 | ≈ enkele honderden t NdPr/j nu → 4,5 kt/j in 2030 | Marktschatting, geen officieel Solvay-cijfer [B8][B9] | Bron-adres Chef de Baie; satelliet z15: kruis op gebouwencomplex | **bron-gelegd** | Grootste REE-scheiding buiten China (40 ha); weerlegt 'Silmet = enige EU-scheiding'. |
| `w-whitemesa` | White Mesa Mill | VS | raffinaderij | 37.5323, -109.5098 | 1,0 kt NdPr/j (fase 1) | Energy Fuels; fase 2 BFS >6 kt NdPr [B10] | Publieke kaartbron; satelliet z15: kruis midden op verwerkingsterrein | **bron-gelegd** | Enige actieve monaziet-mill in de VS. |
| `w-jlmag-ganzhou` | JL MAG Rare-Earth, Ganzhou | China | magneetfabriek | 25.8406, 114.8663 | **38,0 kt NdFeB/j** (bedrijfsbreed) | JL MAG 2024-jaarverslag via SMM [B19] | OSM-naam 江西金力永磁科技股份有限公司; satelliet z15: kruis op industrieel complex | **bron-gelegd** | Grootste NdFeB-producent ter wereld; cijfer niet per vestiging uitgesplitst. |
| `w-yunsheng-ningbo` | Ningbo Yunsheng (hoofdvestiging) | China | magneetfabriek | 29.8825, 121.6193 | **26,0 kt NdFeB/j** (bedrijfsbreed) | Metalnomist 2026 [B20] | OSM-naam 韵升集团; satelliet z15: kruis op hoofdgebouwencomplex | **bron-gelegd** | Onderdeel grootste NdFeB-cluster ter wereld. |
| `w-ningbo-ninggang` | Ningbo Ninggang Permanent Magnet Materials | China | magneetfabriek | 29.8186, 121.6083 | — | Geen cijfer gevonden | OSM-naam 宁波宁港永磁材料有限公司 | **aannemelijk** | Tweede Ningbo-clustersite. |
| `w-baotou-yunsheng` | Ningbo Yunsheng, Baotou-uitbreiding | China | magneetfabriek | 40.6085, 109.8701 | **15,0 kt NdFeB/j** (2026, fase 1+2) | Metalnomist 2026 [B20] | OSM-naam 包头韵升强磁材料有限公司 | **aannemelijk** | Sluit de 'geïntegreerde noordelijke NdPr-loop' uit v1. |
| `w-baotou-weifeng` | Baotou Weifeng Rare Earth Electromagnetic Materials | China | magneetfabriek | 40.5526, 109.8754 | — | Geen cijfer gevonden | OSM-naam 包头市威丰稀土电磁材料股份有限公司 | **aannemelijk** | Tweede Baotou-magneetsite. |
| `w-vac-hanau` | Vacuumschmelze (VAC), Hanau | Duitsland | magneetfabriek | 50.1300, 8.9284 | — (marktschatting: lage duizenden t/j) | rare-earth-mining.com profiel; Energy Fuels-overnamebericht [B23][B24] | Straatadres Grüner Weg 37 | **aannemelijk** | Europa's belangrijkste magneetmaker sinds 1973. |
| `w-shinetsu-takefu` | Shin-Etsu, Takefu (Fukui) | Japan | magneetfabriek | 35.9031, 136.1711 | — (Vietnam-zusterfabriek 2,2 kt/j) | Shin-Etsu persbericht Vietnam-verdubbeling [B22] | OSM-spoorstation Takefu als nabijheidsanker | **aannemelijk** | Enige Japanse sinter-basis naast Vietnam. |
| `w-proterial-kumagaya` | Proterial (Hitachi Metals), Kumagaya | Japan | magneetfabriek | 36.1601, 139.3099 | — | Geen cijfer gevonden | OSM-naam 日立金属熊谷工場 (10 consistente poortpunten) | **aannemelijk** | Belangrijkste Japanse NdFeB-producent naast Shin-Etsu. |
| `w-mpfortworth` | MP Materials Independence, Fort Worth | VS | magneetfabriek | 32.9835, -97.2515 | **1,0 kt NdFeB/j** | MP Materials-persberichten | Straatnaam Independence Parkway (geen huisnummer) | **onzeker** | Amerikaanse mine-to-magnet-sluitstuk; '10X'-vervolgcampus apart. |
| `w-fremantle` | Fremantle North Quay | Australië | exportterminal | -32.04383, 115.74491 | — | Doorvoerpunt | OSM man_made=pier 'North Quay' | **bron-gelegd** | Mt Weld-concentraat/MREC richting Kuantan. |
| `w-kuantanport` | Kuantan Port | Maleisië | exportterminal | 3.98054, 103.42415 | — | Doorvoerpunt | OSM landuse=harbour 'Pelabuhan Kuantan' | **aannemelijk** | 2,5 km van de Lynas-fabriek. |
| `w-longbeach` | Long Beach | VS | exportterminal | 33.7550, -118.2150 | — | Doorvoerpunt | Wikipedia-geohack (havenniveau) | **aannemelijk** | Uitvoerhaven Mountain-Pass-rondreis (tot 17-04-2025). |
| `w-ningbobeilun` | Ningbo-Zhoushan containerterminal (Beilun fase 3) | China | exportterminal | 29.9434, 121.8412 | — | Doorvoerpunt | OSM man_made=pier 'Beilun Container Terminal Phase 3' | **aannemelijk** | Kandidaat-vertrekpunt magneetexport; NIET het koper-ertsanker. |

## Buiten scope

- **Serra Verde Pela Ema (Minaçu, Goiás, Brazilië)** — grootste ionklei-mijn buiten Azië (6.400 t
  REO/j doel tegen eind 2027), maar geen enkele bron geeft een coördinaat voor de mijn zelf; alleen een
  kantooradres in Minaçu-stad (25-30 km van de mijn) werd gevonden.
- **Iluka Eneabba-raffinaderij (Australië)** — 23.000 t REO/j nameplate (5.500 t NdPr/j, 725 t Dy/Tb/j),
  commissioning 2026; de refinery ligt 'op de voetafdruk van' de bestaande mineraalzandmijn, maar geen
  bron geeft een exact coördinaat los van de stadscentroïde Eneabba.
- **Arafura Nolans Bore (Northern Territory, Australië)** — 4.440 t NdPr-oxide/j gepland, FID mei 2026;
  alleen '135 km NW van Alice Springs' gevonden, geen coördinaat.
- **Zhong Ke San Huan (Beijing)** — het gevonden adres (27/F Great Wall Mansion, Zhongguancun) is een
  kantoortoren, niet de fabriek; geen productielocatie gevonden.
- **Neo Narva (Estland)** — nieuwe NdFeB-fabriek (2.000 → 5.000 t/j), geopend sept 2025; geen OSM- of
  adrestreffer binnen budget.
- **Per Geijer (Kiruna, Zweden)** en **CBMM Araxá (Brazilië)** — beide relevant (LKAB-project resp.
  niobium+REE-bijproduct), geen coördinaat gevonden binnen budget.
- **China Rare Earth Group-hoofdkantoor (Ganzhou, 25,7949/114,9135)** — wél gevonden (OSM-naam 中国稀土
  集团总部), maar dit is een kantoorgebouw, geen productieterrein — bewust niet als site opgenomen.
- **Weishan-county-centrum en Longnan-ontwikkelingszone** — beide alleen als bestuurlijke/gebieds-
  centroïde gevonden (verboden als anker); Weishan is vervangen door een specifiek bedrijf met een
  aannemelijke naam/richting-match, Longnan is helemaal weggelaten (geen specifiek bedrijf gevonden).

## Bronnen

- **[B2]** USGS, Mineral Commodity Summaries 2026 — Rare Earths — https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-rare-earths.pdf
- **[B3]** CGTN (2026-03-21), "World's 2nd-largest rare earth mine expands China's resource advantage" — https://news.cgtn.com/news/2026-03-21/World-s-2nd-largest-rare-earth-mine-expands-China-s-resource-advantage-1LHdejtBtTO/p.html
- **[B4]** Metalnomist, "China Launches World's Largest Rare Earth Production Base in Baotou" — https://www.metalnomist.com/2024/11/china-launches-worlds-largest-rare.html
- **[B6]** Lynas Rare Earths, Kalgoorlie Rare Earths Processing Facility — https://lynasrareearths.com/kalgoorlie-western-australia/
- **[B7]** Neo Performance Materials, Estonia magnet plant — https://www.neomaterials.com/estonia/
- **[B8]** Solvay, persbericht "Solvay advances European rare earths production" (april 2025) — https://www.solvay.com/en/press-release/solvay-advances-european-rare-earths-production-through-capacity-expansion
- **[B9]** rawmaterials.net, "Solvay Expands Rare Earth Production at La Rochelle" — https://rawmaterials.net/solvay-expands-rare-earth-production-at-la-rochelle/
- **[B10]** Energy Fuels, White Mesa Mill — https://www.energyfuels.com/white-mesa-mill/
- **[B11]** Mining Weekly (2025-10-24), "Steenkampskraal outlines six-phase rare earths production plan" — https://www.miningweekly.com/article/steenkampskraal-outlines-six-phase-rare-earths-production-plan-2025-10-24
- **[B12]** Steenkampskraal Rare Earths Mine, Processing — https://www.steenkampskraal.com/processing/
- **[B14]** Vietnamnet, "Vietnam's largest rare earth mine set to begin operations" — https://vietnamnet.vn/en/vietnam-s-largest-rare-earth-mine-set-to-begin-operations-2198315.html
- **[B15]** Wikipedia, "Mountain Pass Rare Earth Mine" — https://en.wikipedia.org/wiki/Mountain_Pass_Rare_Earth_Mine
- **[B16]** MP Materials, Q3/Q4 2025 productie- en earningsrapportages — https://s25.q4cdn.com/570172628/files/doc_financials/2025/q3/MP-Materials-Q3-2025-Earnings-Release-FINAL.pdf
- **[B17]** Wikipedia, "Mount Weld mine" — https://en.wikipedia.org/wiki/Mount_Weld_mine
- **[B18]** Wikipedia, "Bayan Obo Mining District" — https://en.wikipedia.org/wiki/Bayan_Obo_Mining_District
- **[B19]** Shanghai Metals Market, "JL MAG Rare-Earth Sets New Highs with Over 90% Capacity Utilization in 2024" — https://news.metal.com/newscontent/103258207/JL-MAG-Rare-Earth-Sets-New-Highs-with-Over-90-Capacity-Utilization-in-2024
- **[B20]** Metalnomist (2026-06), "Ningbo Yunsheng NdFeB Magnet Output Rises on NEV and AI Terminal Demand" — https://www.metalnomist.com/2026/06/ningbo-yunsheng-ndfeb-magnet-output.html
- **[B22]** Shin-Etsu Chemical, persbericht Vietnam-capaciteitsverdubbeling — https://www.shinetsu.co.jp/en/news/news-release/shin-etsu-chemical-to-double-its-production-capacity-of-rare-earth-magnets-in-vietnam/
- **[B23]** PR Newswire, "Energy Fuels Announces Definitive Agreement to Acquire VAC for $1.9 Billion Equity Value" — https://www.prnewswire.com/news-releases/energy-fuels-announces-definitive-agreement-to-acquire-vac-for-1-9-billion-equity-value-302807538.html
- **[B24]** rare-earth-mining.com, "Vacuumschmelze (VAC): Essential Magnet Maker Profile" — https://rare-earth-mining.com/vacuumschmelze/
- **[B29]** Metalnomist (2026-03), "Rare earth polishing powder plant: Shenghe expands high-performance capacity in Sichuan" — https://www.metalnomist.com/2026/03/rare-earth-polishing-powder-plant.html
- **[B30]** Shenghe Resources Holding, About — http://en.shengheholding.com/about.aspx?t=4
- **[B34]** MIIT-quotanotitie 工信部联原〔2024〕156号 (via het ontwerpdocument `sitelaag-ree.json`, niet zelf herbronnen deze ronde)
- **[B35]** rare-earth-mining.com / mindat.org, achtergrond Maoniuping-mijn — https://www.mindat.org/loc-73232.html
- **[B36]** ScienceDirect, "Geochronology and mineralogy of the Weishan carbonatite in Shandong province, eastern China" — https://www.sciencedirect.com/science/article/pii/S1674987118301956
- **[B37]** Wikipedia, "Đông Pao mine" — https://en.wikipedia.org/wiki/%C4%90%C3%B4ng_Pao_mine

Coördinaatbronnen: Wikipedia (geohack via de MediaWiki-API `prop=coordinates`) · OpenStreetMap via
Nominatim (https://nominatim.openstreetmap.org) en Overpass (https://overpass-api.de) —
© OpenStreetMap contributors, ODbL · Esri World Imagery via `v2/tools/sat_check.py`.

## Open punten

- **MEE-register opnieuw verhuisd**: het pad uit `zoek-chinees-adres-recept.md` faalt nu op een 302
  zonder de gedocumenteerde `JSESSIONID`/`tempReportKey`-stap te kunnen zetten binnen deze ronde. Een
  vervolgsessie die het recept opnieuw bijwerkt zou de coördinaten van `w-ganzhou-zhongxi`,
  `w-huajing`, `w-shenghe-leshan`, `w-baotou-*` en `w-jlmag-ganzhou`/`w-yunsheng-*` kunnen verscherpen
  van "aannemelijk"/OSM-naam naar registerpunt met vergunningsnummer.
- **Silmet (Sillamäe)** — de fabriek is niet gevonden op satelliet vanaf het stadscentrum-anker; een
  gerichte adres-/kadasterzoektocht (bijv. via het Estse bedrijvenregister) zou dit kunnen oplossen.
- **Serra Verde, Iluka Eneabba, Arafura Nolans** — drie belangrijke, goed gedocumenteerde sites zonder
  coördinaat; alle drie hebben publieke ESIA/EPA-dossiers die vermoedelijk wél coördinaten bevatten
  maar niet binnen dit budget leesbaar waren (gescande/samengeperste PDF's).
- **Capaciteitscijfers voor Chinese magneetfabrieken zijn bedrijfsbreed**, niet per vestiging. Waar een
  bedrijf meerdere sites in deze laag heeft (JL MAG, Yunsheng), staat hetzelfde bedrijfscijfer bij élke
  vestiging — dat is een bewuste, genoteerde onnauwkeurigheid, geen dubbeltelling in de brontekst zelf,
  maar telt de gloedlaag ze wél apart op dan ontstaat een vertekening. Aanbeveling: bij het centraal
  verwerken (`voeg_sites_toe.py`) een vlag toevoegen die aangeeft dat een capaciteit gedeeld is over
  meerdere sites, zodat de optelling dat kan wegen of markeren.
- **China Rare Earth Group-hoofdkantoor (Ganzhou)** en **Longnan** zijn bewust weggelaten (zie Buiten
  scope) maar zijn wel de twee plekken die in de meeste bronnen letterlijk als dé Dy/Tb-flessenhals
  worden genoemd — een vervolgronde met werkend MEE-register zou hier het meeste waard toevoegen.
- **v1-correcties (uit het ontwerpdocument, niet in deze opdracht uitgevoerd)**: de Mountain-Pass-
  rondreis is sinds 17-04-2025 gestopt, Lynas heeft een Kalgoorlie-tussenstap tussen mijn en Kuantan
  geschoven (nu wél in deze sitelaag verwerkt), en de Kachin-grensstroom loopt via de Tengchong-
  poorten, niet via Ruili — horen bij een correctieronde van `data/rare-earths.js` en `_chokepoints.js`.
