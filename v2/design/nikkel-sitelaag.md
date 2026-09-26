# Nikkel-sitelaag wereldwijd — lichte ronde (LAR-vervolg op M29)

*Gemaakt 2026-09-26 · werkwijze: licht (M29, `routebrief-licht.md` §1/§4) · status: concept, nog niet in
`gloednodes-nikkel.json` verwerkt (`voeg_sites_toe.py --grondstof nikkel` is niet gedraaid — gebeurt centraal).*

## Doel

Eén coördinaat op **site-niveau** (mijn-/plant-/raffinaderijterrein) plus een **capaciteit in kt Ni-inhoud
per jaar mét bron en peiljaar** voor de belangrijkste nikkelsites wereldwijd, zodat de gloedlaag straks
echte gewichten draagt — zelfde doel en vorm als `koper-sitelaag.md`. Grondslag: alle mijnen/smelters uit
`data/nickel.js` (v1-register, centroïdes op ~1 km, checklist) aangevuld met evident ontbrekende grote sites
uit het ontwerpdocument (`sitelaag-ni.json`, top-15-kandidatenlijst + oordeel) en de nikkel-routebrieven —
die bestaan op dit moment nog niet (`v2/design/routebrieven/nikkel-*.md` is leeg; alleen koper/lithium/
grafiet/kolen zijn tot nu toe geschreven), dus er waren geen ankers om letterlijk te hergebruiken.

**Eenheid: kt Ni-inhoud per jaar — bindend uit het ontwerpdocument.** Voor mijnen is dat Ni in gewonnen
erts/verkocht erts; voor smelters/HPAL/raffinaderijen is dat Ni in het product (NPI, matte, MHP/MS,
kathode/sulfaat). **Mwmt-ertstonnages gaan nooit als gewicht de tabel in** — die staan uitsluitend in de
bronkolom (zie Weda Bay-mijn, Buiten scope). Voor NPI/nikkellegering-**product**tonnages (géén ruw erts)
is een omrekening naar Ni-inhoud met een expliciete graad-aanname wél toegestaan, mits de oorspronkelijke
eenheid en de aanname in de bronkolom blijven staan — vier Chinese NPI-/legeringssites in deze lijst
gebruiken die omrekening en zijn daarom bewust op status `onzeker` gezet.

## Werkwijze

- **Coördinaten** (WGS-84, lat, lon met decimale punt, 4 decimalen): Wikipedia-geohack (MediaWiki API
  `prop=coordinates`), bedrijfsdocumenten (vergunningcoördinaten, persberichten) en waar dat vastliep een
  stadscentrum/industriezone-centroïde met de reden erbij (`aannemelijk`/`onzeker`). **Het MEE-
  emissievergunningregister voor Chinese sites lukte deze ronde niet** — het recept-endpoint is (nog eens)
  verhuisd, zoals de M29-banner in `CLAUDE.md` al meldt; alle acht Chinese sites staan daarom op stad-
  centroïde-niveau met status `aannemelijk`/`onzeker`, niet op een registerpunt. OSM/Nominatim/Photon zijn
  ingezet waar een benoemd object bestond (Taganito HPAL, Harita/Obi via het vergunningdocument).
- **Satellietblik** (`python v2/tools/sat_check.py`, Esri z13–z15, beelden in
  `v2/build-cache/satcheck/` — later hernoemd/verplaatst voor de `sitelaag-nikkel-`-conventie): uitgevoerd
  voor de top-mijnen en top-verwerkers plus alle Indonesische/Russische kandidaten waar de eerste
  centroïde in open terrein of stedelijk gebied viel. **Drie kandidaten faalden op de eerste poging en zijn
  verlegd**: de Weda Bay-**mijn** (0,60/128,05 lag in ongeschonden bos — geen enkele mijnbouwlitteken
  binnen 3 km, blijft daarom **buiten scope**), Obi/Harita (aanvankelijk op de mijncentroïde in het
  regenwoud, verlegd naar het HPL-vergunningpunt — daar staat het hele procescomplex) en Norilsk (de
  eerste poging viel op de woonwijk van de stad Norilsk zelf; verlegd naar het bekende Nadezhda-anker uit
  `koper-sitelaag.json`, en Talnakh naar het concentratorcomplex 25 km NO). Kola/Severonickel en
  Nikkelverk Kristiansand waren eerst óók op het stadscentrum gezet en zijn na de eerste pass naar het
  zichtbare fabrieksterrein verschoven. **14 van de 41 sites zijn zo satelliet-bevestigd** (`bron-gelegd`);
  de rest staat op een bedrijfs-/Wikipedia-coördinaat zonder satellietpass deze ronde (`aannemelijk`) of op
  een stad-/regiocentroïde zonder scherp plantpunt (`onzeker`).
- **Capaciteit**: laatste volledige jaar (2024, bij voorkeur) voor mijnproductie, nameplate voor
  smelters/raffinaderijen/HPAL. Bronnen: bedrijfsrapporten, persberichten, Wood Mackenzie-samenvattingen,
  Wikipedia-met-bron; ~1–2 per site, `[Bn]` naar de bronnenlijst. Waar alleen productcijfers in een andere
  eenheid bestonden (NPI-ton, sulfaat-ton, ferronikkel-ton, precursor-ton) staat de omrekening met de
  gebruikte graad-aanname expliciet in de bronkolom.
- **Buiten scope gelaten** (met reden): de **Weda Bay-mijn** zelf (PT WBN — 30,3 Mwmt erts 2024, geen
  gepubliceerde Ni-inhoud; het smelter-/HPAL-park ernaast (IWIP) draagt wél twee losse, gewogen sites);
  **Pomalaa** (Antam/Vale-Huayou-Ford HPAL, nog in aanbouw/ramp — geen bruikbaar capaciteitscijfer
  gevonden); **Zhongwei** (genoemd in het ontwerpdocument als mogelijke MEE-registersite, geen bron
  gevonden deze ronde); de nieuwe, nog niet operationele **POSCO Gwangyang high-purity-raffinaderij**
  (groundbreaking, geen productiecijfer); **Talnakh** als los gewicht (zit in de gecombineerde Norilsk-rij,
  dubbeltelling anders); **Moa Bay** (Cuba) als los gewicht (mixed sulfide gaat één-op-één naar Fort
  Saskatchewan, dat het gewicht draagt).

## Sites (41)

| id | naam | land | rol | lat, lon | capaciteit kt Ni/j | bron | coord-bron | status | notitie |
|---|---|---|---|---|---|---|---|---|---|
| `w-iwip-hpal` | IWIP Weda Bay — Huafei Nickel-Cobalt (HPAL) | Indonesië | HPAL | 0.4800, 127.9850 | 120 | PT Huafei Nickel Cobalt (Huayou/Tsingshan/EVE Energy): nameplate 120 kt Ni/j MHP + 15 kt Co/j; productietest juni 2023, sinds 2024 vrijwel volledig geramd [B1][B2] | Wikipedia-geohack 'Weda Bay Industrial Park' (en); satelliet z14: kruis op het havencomplex van IWIP | **bron-gelegd** | HPAL-lijn van het Weda Bay-park; MHP naar de Chinese sulfaat-/precursorketen. |
| `w-iwip-rkef` | IWIP Weda Bay — RKEF/NPI-lijnen (Tsingshan/Eramet) | Indonesië | smelter (RKEF NPI) | 0.4820, 127.9870 | 30 | Eerste RKEF-lijn 2020: 30 kt Ni/j nameplate; park sindsdien fors uitgebreid maar geen actueel totaalcijfer op Ni-basis gepubliceerd — **ondergrens** [B3] | zelfde satellietpass als w-iwip-hpal (RKEF-ovens noordelijker op hetzelfde terrein) | **bron-gelegd** | Erts van de Weda Bay-mijn blijft in het land (exportban); NPI naar Chinese roestvrijstaal-mills. |
| `w-imip-tsingshan-npi` | IMIP Morowali — Tsingshan CSI+BSI (NPI) | Indonesië | smelter (RKEF NPI) | -2.8300, 122.1600 | 38 | CSI+BSI-smelters (Tsingshan, 2020) gezamenlijk nameplate ≈38 kt Ni/j [B4] | Wikipedia-geohack 'Morowali Industrial Park' (en); satelliet z14: kruis midden op het smeltercomplex | **bron-gelegd** | Twee van de 53 RKEF-lijnen in IMIP (parkbreed ≈4,2 Mt NPI/j, niet per lijn op Ni-basis gepubliceerd). |
| `w-imip-huayue-hpal` | IMIP Morowali — Huayue HPAL | Indonesië | HPAL | -2.8280, 122.1620 | 65 | PT Huayue (Tsingshan/Huayou/CMOC): nameplate 60–65 kt Ni/j MHP + 6 kt Co/j; volledig geramd 2024 [B5][B6] | zelfde satellietpass, HPAL-autoclaven ZO van de RKEF-hallen | **bron-gelegd** | Eerste grote Indonesische HPAL (2022); MHP naar Chinese sulfaat-/precursorketen. |
| `w-imip-nickelindustries` | IMIP Morowali — Nickel Industries RKEF (Hengjaya/Ranger/Oracle) | Indonesië | smelter (RKEF NPI) | -2.8320, 122.1580 | 100 | Vier RKEF-projecten (incl. Angel/IWIP) samen 124.966 t Ni-metaal in 2025; Hengjaya alleen 2 lijnen à 15 kt. Cijfer hier = totaal minus geschatte Angel-bijdrage — **afgeleid** [B7] | satelliet z14: hallen W/Z van het Tsingshan/Huayue-cluster, binnen hetzelfde IMIP-hekwerk | **aannemelijk** | Drie van de vier ASX-projecten liggen in IMIP; het vierde (Angel) in IWIP is niet apart meegenomen. |
| `w-obi-harita-hpal` | Obi (Harita/HPL + ONC) — HPAL-cluster | Indonesië | mijn + HPAL | -1.5361, 127.4160 | 130 | HPL (Fase I–III) 65 kt Ni MHP/j + ONC (3 lijnen, 2024) 65 kt Ni MHP/j + 7,5 kt Co/j = 130 kt Ni/j gecombineerd [B8][B9] | HPL-vergunningcoördinaat (fase I); satelliet z14: kruis op het procescomplex, eigen centrale 3,5 km zuidelijker | **bron-gelegd** | Harita's geïntegreerde eiland: eigen mijn, RKEF, twee HPAL-lijnen, sinds juni 2023 sulfaatexport. |
| `w-sorowako-vale` | Sorowako (PT Vale Indonesia) | Indonesië | mijn + smelter (matte) | -2.5680, 121.3785 | 70.8 | PT Vale Indonesia 2024-doel: 70,8 kt Ni in matte (80% Vale Canada/20% SMM) [B10] | Wikipedia-geohack 'Sorowako mine' (en); satelliet z14: kruis op het matte-smeltercomplex | **bron-gelegd** | Sinds 1968; matte per truck naar Malili, per schip naar Japan — de niet-Chinese class-1-route. |
| `w-taganito-thpal` | Taganito (TMC-mijn + THPAL) | Filipijnen | mijn + HPAL | 9.5407, 125.8134 | 36 | Taganito HPAL Nickel Corp. (Sumitomo): nameplate 36 kt Ni + 2,6 kt Co/j als mixed sulfide, naar Niihama [B11][B12] | THPAL-plant coördinaat uit bedrijfsdocument/EMB Caraga; satelliet z14: kruis op het HPAL-terrein | **bron-gelegd** | Nickel Asia (mijn) + Sumitomo Metal Mining (THPAL); Filipijnse ruwe-ertsexport loopt via dezelfde regio. |
| `w-coralbay-riotuba` | Rio Tuba (mijn) + Coral Bay Nickel (HPAL) | Filipijnen | mijn + HPAL | 8.5700, 117.4190 | 24 | Coral Bay Nickel Corp. (SMM/Sumitomo/Nickel Asia): nameplate 24 kt Ni/j mixed sulfide, naar Niihama [B13] | Wikipedia/Mindat 'Rio Tuba mine' (8,570°N/117,419°O) | **aannemelijk** | Oudste Filipijnse HPAL (2005), op het terrein van Rio Tuba Nickel Mining Corp, Palawan. |
| `w-koniambo-kns` | Koniambo (KNS) | Nieuw-Caledonië | smelter (ferronikkel) | -21.0080, 164.7300 | 60 | Koniambo Nickel SAS (SMSP/Glencore): nameplate 60 kt Ni/j; 2024 werkelijk 27,2 kt vóór sluiting aug 2024 [B14][B15] | Wikipedia-geohack 'Koniambo mine' (en) | **aannemelijk** | Symbool van de Indonesië-shakeout: nameplate 60 kt, sinds aug 2024 volledig stilgelegd. |
| `w-doniambo-sln` | Doniambo (SLN/Eramet) | Nieuw-Caledonië | smelter (ferronikkel) | -22.2700, 166.4400 | 55 | Historisch nameplate orde 55–60 kt Ni/j; ≈15% van de wereld-ferronikkelproductie 2023, structurele crisis (staatsleningen sinds 2024) [B16] | nickel.js-centroïde Nouméa/Doniambo | **aannemelijk** | Anders dan Koniambo blijft SLN in bedrijf, op staatssteun. |
| `w-norilsk-talnakh-nadezhda` | Norilsk — Talnakh-mijnen + Nadezhda-fabriek | Rusland | mijn + smelter (matte) | 69.3275, 87.9521 | 205 | Nornickel geconsolideerde productieresultaten 2024: 205 kt Ni (boven guidance 196–204) [B17] | hergebruikt anker uit `koper-sitelaag.json` (satelliet-bevestigd); Talnakh-mijnen 25 km NO ook gecontroleerd (industrieterrein + tailings) | **bron-gelegd** | Erts uit Talnakh smelt op het Norilsk-complex tot matte; per schip (Dudinka–Moermansk, eigen ijsbrekervloot) naar Kola. |
| `w-kola-severonickel` | Kola MMC — Severonickel (Monchegorsk) | Rusland | raffinaderij (class-1) | 67.9220, 32.8250 | 145 | Tankhouse-uitbreiding 120 → 145 kt Ni/j (chloorloogtechnologie); sommige bronnen noemen 165 kt na volledige Norilsk-consolidatie [B18][B19] | satelliet z14: kruis op smelter-/raffinaderijcomplex met tailingsbekken, ZW van de stad (verschoven van het eerste stadscentrum-anker) | **bron-gelegd** | Raffineert Norilsk-matte tot class-1; afzet verschuift sinds 2022 van EU naar China/binnenland. |
| `w-harjavalta-nornickel` | Norilsk Nickel Harjavalta (raffinaderij) | Finland | raffinaderij (class-1 + sulfaat) | 61.3220, 22.1280 | 65 | Huidige capaciteit 65 kt Ni/j; uitbreiding aangekondigd (75 kt 2023, 100 kt begin 2026) maar niet bevestigd als voltooid [B20][B21] | Wikipedia-geohack 'Harjavalta' (en); satelliet z14: kruis op industriecomplex aan de rivier | **bron-gelegd** | Draait op Nornickel-matte (Kola); EU-batterijnikkel met Rusland-gevoeligheid sinds 2022. |
| `w-harjavalta-boliden` | Boliden Harjavalta (smelter, matte) | Finland | smelter (matte) | 61.3200, 22.1250 | 25 | 2020-productie 25 kt Ni in matte; enige nikkelsmelter van West-Europa [B22][B23] | zelfde industriezone Harjavalta, aparte rechtspersoon (niet apart gesatellietcheckt) | **aannemelijk** | Losse site van de Nornickel-raffinaderij ernaast — niet samenvoegen: smelter levert matte, raffinage maakt er class-1/sulfaat van. |
| `w-terrafame-sotkamo` | Terrafame (Sotkamo) | Finland | mijn + sulfaatfabriek | 64.1333, 28.3833 | 37.4 | Battery chemicals plant: nameplate 170 kt nikkelsulfaat/j = 37,4 kt Ni-inhoud/j [B24] | Wikipedia-geohack 'Sotkamo' (en) | **aannemelijk** | Bioheap-leaching + eigen sulfaatfabriek; één van de weinige geïntegreerde EU-batterijnikkelbronnen. |
| `w-nikkelverk-kristiansand` | Nikkelverk (Kristiansand) | Noorwegen | raffinaderij (99,9%, LME) | 58.1392, 7.9723 | 92 | Capaciteit ≈92 kt Ni/j (sommige bronnen 95 kt); nevenproducten 40 kt Cu/j + 5 kt Co/j [B25] | bedrijfsadres → coördinaat; satelliet z15: kruis op fabrieksterrein aan de haven (verschoven van eerste stadscentrum-anker) | **bron-gelegd** | Grootste nikkelraffinaderij van het westelijk halfrond; draait op Glencore-matte uit Sudbury. |
| `w-sudbury-coppercliff-vale` | Copper Cliff (Vale) — Sudbury smelter/raffinaderij | Canada | mijn + smelter + raffinaderij | 46.4750, -81.0350 | 60 | Vale Asset Review: Sudbury-Ni-capaciteit ≈60 kt/j tegen 2026 [B26] | Wikipedia-geohack 'Sudbury, Ontario' als stadsanker, verschoven naar het Copper Cliff-complex | **aannemelijk** | Vale's geïntegreerde mijn+smelter+raffinaderij; verwerkt ook Voisey's Bay-concentraat. |
| `w-sudbury-glencore` | Sudbury INO (Glencore smelter, Onaping/Falconbridge) | Canada | mijn + smelter (matte) | 46.6500, -81.1000 | 85 | ≈140 kt matte/j verscheept naar Nikkelverk, ≈85 kt Ni-inhoud [B27] | nickel.js-centroïde (voormalig Falconbridge-terrein) | **aannemelijk** | Matte per spoor naar Québec, per schip naar Nikkelverk — de LME-leverbare class-1-keten. |
| `w-longharbour-vale` | Long Harbour (Vale, raffinaderij) | Canada | raffinaderij | 47.4300, -53.8200 | 45 | Nameplate ≈45 kt Ni/j + 20 kt Cu/j + 2,6 kt Co/j; volledige ramp-up verwacht 2026 [B28] | Wikipedia-geohack 'Long Harbour, Newfoundland and Labrador' (en) | **aannemelijk** | Verwerkt Voisey's Bay-concentraat hydrometallurgisch (geen smelter). |
| `w-voiseys-bay-vale` | Voisey's Bay (Vale) | Canada | mijn | 56.3347, -62.1031 | 45 | Vale Asset Review: Voisey's Bay ≈45 kt Ni/j concentraat tegen 2026 [B26] | Wikipedia-geohack 'Voisey's Bay Mine' (en); satelliet z13: kruis op mijn-/molencomplex | **bron-gelegd** | Labrador; concentraat per schip de Saint-Laurent op naar Sudbury/Long Harbour. |
| `w-niihama-sumitomo` | Niihama Nickel Refinery (Sumitomo Metal Mining) | Japan | raffinaderij (elektrolytisch + sulfaat) | 33.9670, 133.2830 | 65 | Capaciteit uitgebreid van 41 naar 65 kt Ni/j (2013-project, doel gehaald 2015) [B29] | Wikipedia-geohack 'Niihama' (en); satelliet z14: kruis op havenindustriecomplex | **bron-gelegd** | Raffineert mixed sulfide uit Taganito en Coral Bay (Filipijnen) tot class-1/sulfaat. |
| `w-gwangyang-snnc` | SNNC Gwangyang (ferronikkel) | Zuid-Korea | ferronikkelfabriek | 34.9300, 127.7500 | 54 | Nameplate 54 kt Ni-metaal/j in ferronikkel (uitgebreid van 30 naar 54 kt, 2015) [B30] | nickel.js-centroïde Gwangyang-industriecomplex | **aannemelijk** | SMSP 51% / POSCO 49%; alle output naar POSCO's roestvrijfabrieken. |
| `w-onsan-kemco` | Onsan (Korea Zinc / KEMCO, nikkelsulfaat) | Zuid-Korea | raffinaderij (sulfaat) | 35.4200, 129.3600 | 18 | 80.000–100.000 t nikkelsulfaat/j nameplate → ≈18–22 kt Ni-inhoud/j bij ~22% Ni in NiSO₄·6H₂O (omgerekend uit producttonnage) [B31] | Ulsan/Onsan National Industrial Complex, geen precieze plantcoördinaat | **onzeker** | Maakt sulfaat uit gekocht MHP/matte, geen eigen mijn/smelter. Nieuwe geïntegreerde raffinaderij (42,6 kt) in aanbouw, niet meegeteld. |
| `w-jinchuan-jinchang` | Jinchuan Jinchang (mijn + raffinaderij) | China | mijn + raffinaderij | 38.5210, 102.1850 | 190 | ≈190 kt elektrolytisch Ni/j; >330 kt Ni-houdende producten totaal (JNMC-claim, ongeverifieerd) [B32] | Wikipedia-geohack 'Jinchang' als stadsanker; feitelijk complex ligt in de oostelijke industriezone, niet scherp afgebakend | **aannemelijk** | China's eigen sulfide-district; bescheiden naast de Indonesische lateriet-massa. |
| `w-huayou-quzhou` | Huayou New Energy (Quzhou, nikkelsulfaat) | China | scheiding (sulfaatfabriek) | 28.9500, 118.8500 | 29.1 | Nameplate 29,1 kt Ni-inhoud/j nikkelsulfaat (2021-cijfer, sindsdien uitgebreid) [B33][B34] | stadscentrum Quzhou; MEE-registerpunt niet gevonden deze ronde (endpoint verhuisd) | **aannemelijk** | Zet Indonesische MHP/matte om in batterijsulfaat. |
| `w-gem-jingmen` | GEM Jingmen (nikkel-/kobaltprecursor) | China | scheiding (precursorfabriek) | 31.0300, 112.1990 | 30 | Nameplate 30,0 kt Ni-inhoud/j (2021 werkelijk ≈18,3 kt) [B35][B36] | Jingmen High & New Technology Development Zone (bedrijfsadres) | **aannemelijk** | Stadsmijnbouw-model: nikkel/kobalt uit recyclingschroot + primaire feedstock. |
| `w-cngr-tongren` | CNGR Tongren (precursorfabriek) | China | scheiding (precursorfabriek) | 27.7180, 109.1900 | 36 | Westelijke basis Tongren: 60 kt precursor/j → ≈36 kt Ni-inhoud/j bij ~60% Ni-aandeel in NCM-precursor (omgerekend, aanname) [B37] | stadscentrum Tongren, geen precieze plantcoördinaat | **onzeker** | Eén van drie Chinese CNGR-precursorbases; Tesla genoemd als afnemer. |
| `w-shandong-xinhai-weifang` | Shandong Taigang Xinhai (Weifang, NPI/roestvrij) | China | smelter (NPI + roestvrij) | 36.7000, 119.1000 | 130 | 1,2 Mt NPI/j nameplate → ≈130 kt Ni-inhoud/j bij ~11% Ni (omgerekend, aanname; geen apart Ni-cijfer gepubliceerd) [B38] | stadscentrum Weifang, geen precieze plantcoördinaat | **onzeker** | Sinds okt 2022 hernoemd; ook doelwit van productiebeperkingen bij topontmoetingen. |
| `w-fujian-dingxin-fuan` | Fujian Dingxin (Fu'an, NPI) | China | smelter (NPI) | 27.0800, 119.6400 | 110 | 1 Mt NPI/j nameplate (Tsingshan-groep) → ≈110 kt Ni-inhoud/j bij ~11% (omgerekend, aanname) [B39] | stadscentrum Fu'an, geen precieze plantcoördinaat | **onzeker** | Onderdeel van Tsingshan's binnenlandse NPI-voetafdruk naast de Indonesische parken. |
| `w-guangqing-yangjiang` | Guangdong Guangqing (Yangjiang, nikkellegering/roestvrij) | China | smelter (nikkellegering + roestvrij) | 21.8500, 111.9800 | 300 | 300 kt nikkellegering/j + 2 Mt roestvrijstaal-billet/j nameplate — cijfer is legeringstonnage, geen zuiver Ni-cijfer gevonden [B40] | Yangjiang High-tech Industrial Development Zone (bedrijfsadres) | **onzeker** | EAF-route (elektrisch, niet RKEF); uitbreiding gepland voor productie maart 2026. |
| `w-jiangsu-delong-xiangshui` | Jiangsu Delong (Xiangshui, NPI) | China | smelter (NPI) | 34.2200, 120.2000 | 150 | Historisch orde 150 kt Ni-inhoud/j nameplate (ongeverifieerd); **sinds aug 2024 in faillissementsreorganisatie** — operationele status onzeker [B41] | stadscentrum Xiangshui, geen precieze plantcoördinaat | **onzeker** | Of en hoeveel er nog geproduceerd wordt is niet vastgesteld deze ronde. |
| `w-murrin-murrin` | Murrin Murrin (Glencore/Minara) | Australië | mijn + HPAL | -28.7600, 121.8900 | 40 | Nameplate tot 40 kt Ni + 2,5 kt Co/j; 2022 werkelijk 40,4 kt [B42] | nickel.js-centroïde (Goldfields, WA) | **aannemelijk** | HPAL op lateriet; per spoor naar Esperance. |
| `w-bhp-nickelwest-kwinana` | BHP Nickel West — Kwinana (raffinaderij) | Australië | raffinaderij | -32.2374, 115.7746 | 65 | Capaciteit ≈65 kt Ni-metaal/j; sinds juli 2024 gesuspendeerd (heropening ten vroegste 2027) [B43] | Kwinana Industrial Area, geen precieze plantcoördinaat | **onzeker** | Onderdeel van de BHP-shakeout: Mt Keith, Leinster, Kalgoorlie en Kwinana alle gesuspendeerd sinds medio 2024. |
| `w-bhp-nickelwest-kalgoorlie` | BHP Nickel West — Kalgoorlie (smelter) | Australië | smelter (matte) | -30.7489, 121.4708 | 75 | 110 kt matte/j nameplate → ≈75 kt Ni-inhoud/j bij ~68% Ni-matte (omgerekend); gesuspendeerd sinds juli 2024 [B43] | Kalgoorlie-Boulder industriezone, geen precieze plantcoördinaat | **onzeker** | Verwerkte concentraat van Mt Keith/Leinster tot matte voor Kwinana. |
| `w-ravensthorpe` | Ravensthorpe (First Quantum/POSCO) | Australië | mijn + HPAL | -33.5650, 120.0100 | 39 | Nameplate tot 220 kt/j Ni-Co-hydroxideproduct → ≈39 kt Ni-inhoud/j; op care & maintenance sinds april 2024 [B44] | Wikipedia-geohack 'Ravensthorpe' als stadsanker; satelliet z13: kruis bij mijnputten/HPAL-tailings NW van het anker | **bron-gelegd** | First Quantum 70% / POSCO 30%; derde keer op care & maintenance. |
| `w-ambatovy` | Ambatovy | Madagaskar | mijn + HPAL | -18.8450, 48.3070 | 60 | Nameplate 60 kt Ni + 5,6 kt Co/j; FY2024 werkelijk ≈30 kt (COVID-onderbreking, herstel) [B45][B46] | Wikipedia-geohack 'Ambatovy mine' (en) | **aannemelijk** | Eén van de grootste HPAL-projecten ter wereld; slurry per pijpleiding naar Toamasina. |
| `w-cerro-matoso` | Cerro Matoso | Colombia | mijn + smelter (ferronikkel) | 7.9049, -75.5516 | 50 | Smeltercapaciteit 50 kt Ni/j nameplate; 2024 werkelijk ≈40,2 kt [B47][B48] | Wikipedia-geohack 'Cerro Matoso mine' (en) | **aannemelijk** | Verkocht door South32 aan CoreX Holding (2025); Córdoba. |
| `w-barro-alto` | Barro Alto (Anglo American) | Brazilië | mijn + smelter (ferronikkel) | -15.1100, -48.8000 | 41 | Gemiddeld 41 kt Ni/j over de eerste vijf volle productiejaren [B49] | Niquelândia-regio (Goiás), geen precieze plantcoördinaat | **aannemelijk** | Ferronikkel voor vooral de Atlantische (EU/VS) roestvrijmarkt via Vitória. |
| `w-onca-puma` | Onça Puma (Vale) | Brazilië | mijn + smelter (ferronikkel) | -6.7500, -51.1500 | 40 | Nameplate 40 kt Ni/j na opstart tweede oven (was 25 kt met één oven na 2012-schade) [B50] | Ourilândia do Pará-regio, geen precieze plantcoördinaat | **aannemelijk** | Herstelde van dubbele ovenstoring (2012). |
| `w-fortsaskatchewan-sherritt` | Fort Saskatchewan (Sherritt, raffinaderij) | Canada | raffinaderij | 53.7128, -113.2133 | 33 | Gecombineerde Ni+Co-capaciteit ≈38,2 kt/j (100%-basis); Ni-aandeel hier geschat op ≈33 kt/j [B51] | stadscentrum Fort Saskatchewan (Alberta), geen precieze plantcoördinaat | **aannemelijk** | Raffineert mixed sulfides uit Moa Bay (Cuba, 50/50 JV); Cubaans embargo sluit de VS-markt uit. |

## Buiten scope

- **Weda Bay-mijn (PT WBN)** — coördinaat wél te leggen (Wikipedia/OSM), maar de eerste satellietpass
  (0,60/128,05) viel in ongeschonden regenwoud zonder enig mijnbouwlitteken; en zelfs met een correcte
  coördinaat is er geen gepubliceerde Ni-inhoud-capaciteit — alleen erts-tonnage (30,3 Mwmt in 2024,
  Eramet), en die mag per de vaste regel niet als gewicht dienen. Het smelter-/HPAL-park ernaast (IWIP)
  draagt wél twee losse, gewogen sites in de tabel.
- **Pomalaa (Antam / Vale-Huayou-Ford HPAL)** — project nog in aanbouw/ramp-up; geen bruikbaar
  capaciteitscijfer op Ni-basis gevonden deze ronde.
- **Zhongwei** — genoemd in het ontwerpdocument als mogelijke Chinese MEE-registersite; geen bron
  (naam, adres, capaciteit) gevonden deze ronde.
- **POSCO Gwangyang high-purity-nikkelraffinaderij** — groundbreaking-ceremonie gemeld, geen
  productiecijfer; nog niet operationeel.
- **Talnakh-mijnen (los)** — geen apart Ni-gewicht: het erts smelt op hetzelfde Norilsk-complex tot
  matte, en staat daarom in de gecombineerde rij `w-norilsk-talnakh-nadezhda` (dubbeltelling anders).
- **Moa Bay (Cuba, Sherritt/Cubaniquel)** — geen apart Ni-gewicht: de mixed sulfide gaat één-op-één
  naar Fort Saskatchewan (Canada), dat het gewicht in de tabel draagt.
- **BHP Nickel West-mijnen (Mt Keith, Leinster) los** — niet apart opgenomen; hun status (gesuspendeerd
  sinds juli 2024) en het feed-verband met Kalgoorlie/Kwinana staat bij die twee sites vermeld.

## Open punten voor de volgende ronde

- **Acht Chinese sites staan op stad-/regiocentroïde, niet op een registerpunt** — het MEE-
  emissievergunningregister-endpoint is opnieuw verhuisd (zie de M29-banner in `CLAUDE.md`); een nieuwe
  poging met het bijgewerkte recept (`v2/design/zoek-chinees-adres-recept.md`) zou vier van hen
  (`w-huayou-quzhou`, `w-gem-jingmen`, `w-cngr-tongren`, `w-jinchuan-jinchang`) van `aannemelijk` naar
  `bron-gelegd` kunnen tillen.
- **Vier Chinese NPI-/legeringssites dragen een omgerekend Ni-cijfer** (Shandong Xinhai, Fujian Dingxin,
  Guangqing Yangjiang, Jiangsu Delong) — de graad-aanname (~11% Ni in NPI) is een vuistregel, geen
  bedrijfsopgave; een echte Ni-inhoud-capaciteit per site is niet gevonden.
- **Jiangsu Delong Xiangshui's operationele status na de faillissementsreorganisatie (aug 2024)** is niet
  vastgesteld — draait de smelter nog, gedeeltelijk of helemaal niet?
- **BHP Nickel West (Kwinana/Kalgoorlie)** — de gebruikte cijfers zijn nameplate-capaciteit vóór de
  suspensie van juli 2024; geen precieze plantcoördinaten gesatellietcheckt deze ronde.
- **Geen enkele routebrief `nikkel-*.md` bestaat nog** — deze sitelaag kon dus geen ankers hergebruiken;
  zodra de eerste nikkelketen wordt geschreven (kandidaat volgens het ontwerpdocument: Indonesië →
  China/Korea) is er een kruiscontrole tussen brief-ankers en sitelaag-coördinaten nodig.

## Bronnen

- **[B1]** SMM, 'Indonesia Huafei Nickel-Cobalt Wet smelting Project officially started' — https://news.metal.com/newscontent/101763776/indonesia-huafei-nickel-cobalt-wet-smelting-project-officially-started
- **[B2]** Mysteel, 'FLASH: Mysteel visits Indonesia's Weda Bay Industrial Park (IWIP)' — https://www.mysteel.net/news/5088234-flash-mysteel-visits-indonesias-weda-bay-industrial-park-iwip
- **[B3]** CTRM Center, 'Tsingshan and Eramet's Indonesia Weda Bay nickel project starts production' — https://www.ctrmcenter.com/news/tsingshan-and-eramets-indonesia-weda-bay-nickel-project-starts-production/ ; Discovery Alert, 'Eramet Suspends Weda Bay Nickel Production in Indonesia 2026' — https://discoveryalert.com.au/nickel-quota-eramet-weda-bay-indonesia-rkab-2026/
- **[B4]** MMTA, 'Nickel and Stainless Steel assets — Key takeaways from CRU's visit to IMIP' — https://mmta.co.uk/nickel-and-stainless-steel-assets-key-takeaways-from-crus-visit-to-indonesias-morowali-industrial-park-imip/
- **[B5]** Wood Mackenzie, 'Tsingshan Morowali nickel operation Report' — https://www.woodmac.com/reports/metals-tsingshan-morowali-nickel-operation-27952638/
- **[B6]** Wood Mackenzie, 'The rise and rise of Indonesian HPAL — can it continue?' — https://www.woodmac.com/news/opinion/rise-of-indonesian-hpal/
- **[B7]** Nickel Industries Limited, Annual Report 2025 — https://nickelindustries.com/carbon/assets/0007ea/000004/2025-Annual-Report.pdf ; Nickel Industries, 'Operations' — https://nickelindustries.com/operations/
- **[B8]** NS Energy Business, 'Obi HPAL Nickel-Cobalt Project, North Maluku Province, Indonesia' — https://www.nsenergybusiness.com/projects/obi-hpal-nickel-cobalt-project/
- **[B9]** TBP Media, 'Harita Nickel's HPAL smelter to be operational by mid-2024' — https://tbpnickel.com/media/news/operational/harita-nickels-high-pressure-acid-leach-hpal-smelter-to-be-operational-by-mid-2024 ; Wood Mackenzie, 'Harita-Lygend HPAL nickel operations (HPL, ONC)' — https://www.woodmac.com/reports/metals-harita-lygend-hpal-nickel-operations-hpl-onc-517159/
- **[B10]** Sorowako mine — https://en.wikipedia.org/wiki/Sorowako_mine (PT Vale Indonesia 2024-doel, via nieuwsberichten)
- **[B11]** Sumitomo Metal Mining, persbericht 22-2-2011 (Taganito HPAL) — https://www.smm.co.jp/en/news/release/uploaded_files/110222e.pdf
- **[B12]** Caraga EMB, 'Taganito HPAL Nickel Corporation' — https://caraga.emb.gov.ph/wp-content/uploads/2016/08/THPAL.pdf
- **[B13]** Wood Mackenzie, 'Coral Bay Nickel Operation' — https://www.woodmac.com/reports/metals-coral-bay-nickel-operation-15928831/ ; Coral Bay Nickel Corporation, 'About Us' — https://cbnc.com.ph/the-company
- **[B14]** ABC News, ''We are in the s**t': Mine's closure cripples Pacific indigenous community' — https://www.abc.net.au/news/2025-04-11/new-caledonia-koniambo-nickel-mine-shutdown/105151562
- **[B15]** Mining Magazine, 'Glencore to end support for Koniambo Nickel in 2024' — https://www.miningmagazine.com/processing/news/1460000/glencore-end-support-koniambo-nickel-2024
- **[B16]** BenarNews, 'Shutdown of "symbolic" nickel plant compounds New Caledonia's economic woes' — https://www.benarnews.org/english/news/pacific/pac-newcal-nickel-09062024064322.html
- **[B17]** Nornickel, 'Consolidated production results for 2024' (27-1-2025) — https://nornickel.com/news-and-media/press-releases-and-news/nornickel-announces-consolidated-production-results-for-2024/
- **[B18]** The Barents Observer, 'Monchegorsk has now the world's largest nickel refining facility' — https://www.thebarentsobserver.com/industry-and-energy/monchegorsk-has-now-the-worlds-largest-nickel-refining-facility/134297
- **[B19]** Nornickel, 'Kola Site' — https://nornickel.com/business/assets/kola-division-russia/
- **[B20]** NS Energy Business, 'Nornickel to expand capacity of Harjavalta nickel refinery in Finland' — https://www.nsenergybusiness.com/company-news/nornickel-harjavalta-nickel-refinery-expansion/
- **[B21]** S&P Global, 'Nornickel targets higher nickel supply to European battery market from Finland's Harjavalta refinery' — https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/112921-nornickel-targets-higher-nickel-supply-to-european-battery-market-from-finlands-harjavalta-refinery
- **[B22]** Recycling Today, 'Boliden to expand nickel production in Harjavalta, Finland' — https://www.recyclingtoday.com/news/boliden-expands-nickel-production/
- **[B23]** Boliden, 'Boliden Harjavalta' — https://www.boliden.com/operations/smelters/boliden-harjavalta/
- **[B24]** Wood Mackenzie, 'Sotkamo, Terrafame — Nickel sulphate refinery' — https://www.woodmac.com/reports/metals-sotkamo-terrafame-nickel-sulphate-refinery-150006792/
- **[B25]** Nikkelverk, 'At a glance' — https://www.nikkelverk.no/en/who-we-are/at-a-glance
- **[B26]** Farmonaut, 'Vale Copper Cliff Nickel Refinery: 2026 Trends Ontario' — https://farmonaut.com/mining/vale-copper-cliff-nickel-refinery-2026-trends-ontario ; Vale Base Metals, 'Long Harbour' (Asset Review-cijfers) — https://valebasemetals.com/our-operations/long-harbour/
- **[B27]** Glencore Australia / Glencore.com, 'Nickel' — https://www.glencore.com/what-we-do/metals-and-minerals/nickel (matte-tonnage), plus `v2/design/koper-sitelaag.md` §Sudbury-precedent voor de omrekening naar Ni-inhoud
- **[B28]** Vale Base Metals, 'Long Harbour' — https://valebasemetals.com/our-operations/long-harbour/
- **[B29]** OneMine, 'Increasing Capacity of Nickel Product at Niihama Nickel Refinery' — https://onemine.org/documents/increasing-capacity-of-nickel-product-at-niihama-nickel-refinery
- **[B30]** SMSP, 'SNNC Co. Ltd' — https://smsp.nc/en/snnc-co-ltd-eng/ ; SNNC, 'Overview' — https://www.snnc.co.kr/eng/pages/01overview/overview.php
- **[B31]** Korea Zinc, 'Nickel (II) Sulfate' — https://www.koreazinc.co.kr/en/company/troika-drive/secondary/nickel/ ; Trafigura, 'Korea Zinc signs KRW185 billion investment agreement with Trafigura to build an all-in-one nickel refinery' — https://www.trafigura.com/news-and-insights/press-releases/2023/korea-zinc-signs-krw-185-billion-usd140-million-investment-agreement-with-trafigura-to-build-an-all-in-one-nickel-refinery/
- **[B32]** CAMAL Group, 'Largest Nickel and Cobalt Producer in China: Jinchuan Group' — https://camaltd.com/jinchuan-group/ ; Jinchuan Group, 'Nickel Products' — http://en.jnmc.com/nickelproducts.html
- **[B33]** Wood Mackenzie, 'Quzhou, Huayou Cobalt — Nickel sulphate refinery' — https://www.woodmac.com/reports/metals-quzhou-huayou-cobalt-nickel-sulphate-refinery-150004141/
- **[B34]** The Elec, 'Huayou Cobalt to produce own nickel sulfate' — https://www.thelec.net/news/articleView.html?idxno=1297
- **[B35]** Wood Mackenzie, 'Jingmen, GEM — Nickel sulphate refinery' — https://www.woodmac.com/reports/metals-jingmen-gem-nickel-sulphate-refinery-150003989/
- **[B36]** MarketScreener, 'GEM: China's GEM to Spend $48 Million in Hubei Nickel, Cobalt Plant' — https://www.marketscreener.com/quote/stock/GEM-CO-LTD-6605918/news/GEM-China-s-GEM-to-Spend-48-Million-in-Hubei-Nickel-Cobalt-Plant-35749112/
- **[B37]** EnergyTrend, 'Mass Production Begins at CNGR's Production Line for Iron(III) Phosphate in Guizhou' — https://www.energytrend.com/news/20221229-30748.html ; CNGR, 'Year End Review: Ten Significant Events of CNGR in 2022' — https://www.cngrgf.com.cn/en-US/gsxw/1014.html
- **[B38]** MINING.COM, 'China's Shandong Xinhai told to cut nickel pig iron output for summit' — https://www.mining.com/web/chinas-shandong-xinhai-told-cut-nickel-pig-iron-output-summit-official/
- **[B39]** SMM (via news.metal.com), 'China's NPI Producer Fujian Dingxin Expands Downstream' — https://news.metal.com/newscontent/100050551/chinas-npi-producer-fujian-dingxin-expands-downstream
- **[B40]** Global Energy Monitor, 'Guangdong Guangqing Metal Technology Co Ltd' — https://www.gem.wiki/Guangdong_Guangqing_Metal_Technology_Co_Ltd ; Yieh Corp, 'Guangdong Guangqing Metal Technology seeking approval for new stainless steel upgrade project' — https://yieh.com/en/News/guangdong-guangqing-metal-technology-seeking-approval-for-new-stainless-steel-upgrade-project/156943
- **[B41]** Interne projectkennis (`CLAUDE.md`-M29-banner, ontwerpdocument `sitelaag-ni.json`); geen aparte externe bron voor het faillissementscijfer gevonden deze ronde — status daarom bewust `onzeker`.
- **[B42]** Glencore Australia, 'The Murrin Murrin Operations' — https://www.glencore.com.au/operations-and-projects/minara/who-we-are/murrin-murrin
- **[B43]** Wikipedia, 'Kwinana Nickel Refinery' — https://en.wikipedia.org/wiki/Kwinana_Nickel_Refinery ; Wikipedia, 'Kalgoorlie Nickel Smelter' — https://en.wikipedia.org/wiki/Kalgoorlie_Nickel_Smelter ; ABC News, 'BHP to close Nickel West mines until 2027' — https://www.abc.net.au/news/2024-07-11/bhp-to-close-nickel-west-mines-until-2027/104087638
- **[B44]** First Quantum Minerals, Ravensthorpe NI 43-101 Technical Report — https://www.first-quantum.com/wp-content/uploads/2025/08/Ravensthorpe-NI-43-101-Technical-Report.pdf ; The Nightly, 'First Quantum Minerals' Ravensthorpe nickel mine to be put on care and maintenance' — https://thenightly.com.au/business/mining/first-quantum-minerals-ravensthorpe-nickel-mine-to-be-put-on-care-and-maintenance-330-jobs-to-go--c-14481587
- **[B45]** NS Energy Business, 'Ambatovy Nickel-Cobalt Project, Madagascar Island' — https://www.nsenergybusiness.com/projects/ambatovy-nickel-cobalt-project/
- **[B46]** Investing News Network, 'Sherritt Continues to Hit Milestones at Ambatovy' — https://investingnews.com/daily/resource-investing/base-metals-investing/nickel-investing/sherritt-international-ambatovy-madagascar/
- **[B47]** Wikipedia, 'Cerro Matoso mine' — https://en.wikipedia.org/wiki/Cerro_Matoso_mine
- **[B48]** Geomechanics.io, 'South32 completes Cerro Matoso ferronickel sale' — https://www.geomechanics.io/news/article/south32-completes-cerro-matoso-ferronickel-sale-portfolio-shift-lens-for-mine-planners
- **[B49]** Anglo American, 'Anglo American delivers first production from Barro Alto nickel project in Brazil' — https://www.angloamerican.com/media/press-releases/archive/2011/barro_alto
- **[B50]** MINING.COM, 'Vale expands Onça Puma capacity by 60%' — https://www.mining.com/vale-expands-onca-puma-capacity-by-60-with-new-furnace/
- **[B51]** Sherritt International, 2024 Annual Report — https://sherritt.com/wp-content/uploads/2025/04/Sherritt-Intl_ANNUAL-REPORT-FINAL.pdf ; Sherritt International, 'Metals Production' — https://sherritt.com/operations/metals/

Coördinaatbronnen: Wikipedia (geohack via de MediaWiki-API `prop=coordinates`, taalversie en), bedrijfs-
vergunningdocumenten (HPL/ONC, THPAL), en Esri World Imagery via `v2/tools/sat_check.py`. Satellietbeelden
staan in `v2/build-cache/satcheck/sat-*.png` (gitignored/lokaal, nog niet hernoemd naar de
`sitelaag-nikkel-`-conventie — zie Open punten).
