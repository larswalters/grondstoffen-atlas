# Gas-sitelaag wereldwijd — lichte ronde (M31)

> **Centrale correctie 2026-09-28 (LAR-598):** `w-kochi` (6,8 bcm/j) staat in `sites_zonder_gewicht` — de coördinaat was de stadscentroïde, geen terrein.

*Gemaakt 2026-09-28 · werkwijze: licht (M29, `routebrief-licht.md` §1/§4) · status: concept, nog niet in `gloednodes-gas.json` verwerkt (dat gebeurt centraal, niet door deze agent).*

## Doel

Eén coördinaat op **site-niveau** (terrein van liquefactie- of regasterminal) plus een **capaciteit
in bcm/j mét bron en peiljaar** voor de belangrijkste aardgas/LNG-sites wereldwijd — analoog aan
`koper-sitelaag.md` (mijn/smelter), maar dan liquefactieterminal (= "bron", vloeibaarmaking is de
trechter die captive pijpgas tot verhandelbare wereldgrondstof maakt) en regas-/importterminal (=
"verwerker", waar LNG weer gas wordt en het net in gaat). Grondslag: `data/gas.js` (v1-registerdata,
veldniveau-centroïdes) + `design/gas.md` (checklist), aangevuld met evident ontbrekende grote sites
(vooral Zuid-Korea/Japan-regas, die in `data/gas.js` alleen als brede marktknoop staan) en de
ankers uit de ketens van deze golf. Vijf `gas-*.md`-routebrieven verschenen halverwege deze ronde
(parallelle agents in dezelfde workflow-golf) — waar hun satelliet-bevestigde ankers een site uit
deze lijst raakten (Ras Laffan, Sabine Pass, Corpus Christi, Pluto, Bonny, Zeebrugge, Rudong,
Sodegaura, Gate, Incheon) zijn ze **letterlijk hergebruikt** en is de status waar toepasselijk
opgewaardeerd naar bron-gelegd, in plaats van een tweede, licht afwijkend anker op dezelfde site te
leggen.

## Eenheid

**bcm/j (miljard m³ aardgas per jaar)** voor zowel liquefactie- als regascapaciteit — de
industriestandaard voor pijpgas en het enige getal waarin beide rollen (vloeibaar maken /
hervergassen) en een pijplijncorridor onderling optelbaar zijn. LNG-capaciteit (meestal
gepubliceerd in Mtpa) is omgerekend met **1 Mt LNG ≈ 1,36 bcm/j gas-equivalent**, per site expliciet
genoemd in `capaciteit_bron`. Drie sites (Zeebrugge, Montoir-de-Bretagne, Revithoussa) publiceren
zelf al in bcm/j — dat getal is dan letterlijk overgenomen, niet via Mtpa omgerekend.

Geen `eenheid_site`-uitzonderingen nodig deze ronde: alle 47 gewogen sites zijn terminals met een
Mtpa- of bcm-cijfer. Twee rollen zijn bewust **buiten** de gewogen lijst gehouden (eerlijkheidsregel,
zie hieronder): het offshore-veld→terminal-trunkline-been (draagt geen eigen capaciteitscijfer, dat
zit al in de terminal) en de opslag-/bufferrol (telt in **bcm werkgasvoorraad**, niet in bcm/j
doorzet — één voorbeeldsite, Rehden, staat gedocumenteerd in `sites_zonder_gewicht`).

## Werkwijze

- **Coördinaten** (WGS-84, lat/lon met decimale punt, 4-5 decimalen): primair de **MediaWiki
  Coordinates-API** (`prop=coordinates`) en **Wikidata** (`wbsearchentities` + claim P625) via
  directe `curl`-aanroepen — de Python-`urllib`-client liep herhaaldelijk tegen 429's aan vanaf deze
  sessie-IP, `curl` niet; die asymmetrie is een bruikbare werkregel voor een volgende ronde. Waar
  geen benoemd Wikipedia/Wikidata-object bestond: **OSM via Photon** (`photon.komoot.io`), met
  voorkeur voor een `landuse=industrial`-polygoon met een herkenbare naam (bijv. `袖ヶ浦火力発電所`,
  `Santos Darwin LNG Power Plant`) boven een generieke plaatscentroïde. **Nominatim** gaf op deze
  sessie vrijwel alleen 429's/lege resultaten voor terminalnamen en is niet verder gebruikt.
  **Overpass** niet geprobeerd na eerdere ervaring dat het vanaf deze machine onbereikbaar is
  (bevestigt de bestaande projectregel). Twee Spaanse terminal-coördinaten (Huelva, Cartagena) kwamen
  letterlijk uit een **embedded Google Maps-link** in de Wikipedia-wikitext zelf — een ongebruikelijke
  maar exacte bron.
- **Capaciteit**: waar mogelijk een gepubliceerd Mtpa- of bcm/j-cijfer, ~1-2 bronnen per site,
  `[Bn]` naar de bronnenlijst. **Wikipedia's `List of LNG terminals`** (via `action=parse&prop=wikitext`,
  opgehaald met `curl`) bleek de meest efficiënte bron: één pagina met een Afrika/Australië-tabel
  (met exacte Mtpa-kolommen) en per-land opsommingen met veel capaciteitscijfers direct in de tekst
  — dat leverde in één keer 15+ geverifieerde capaciteitscijfers op zonder losse zoekopdrachten.
  Waar die pagina geen cijfer gaf (met name Zuid-Korea/China/Japan/Spanje) is het **webbudget** (max
  3 `WebSearch`-aanroepen) ingezet op de drie grootste gaten: Japanse JERA-terminals (Futtsu/
  Sodegaura), Koreaanse KOGAS-terminals (Incheon/Pyeongtaek) en Chinese CNOOC/PetroChina-terminals
  (Dapeng/Rudong/Tianjin) — alle drie raak, met bruikbare Mtpa- of bcf-cijfers.
- **Satellietblik** (`python v2/tools/sat_check.py`, Esri z13-z17, beelden in
  `v2/build-cache/satcheck/` met prefix `sitelaag-gas-`) voor de **top-6 liquefactiesites** (Ras
  Laffan, Sabine Pass, Petronas LNG/Bintulu, Nigeria LNG/Bonny, Arzew, Plaquemines — gerangschikt op
  capaciteit) en de **top-6 regassites** (Incheon, Pyeongtaek, Dahej, Grain/Isle of Grain, South
  Hook, Barcelona): ligt het kruis op het tankpark/de steiger → **bron-gelegd**, anders verschoven
  naar wat zichtbaar is (drie sites — Malaysia LNG, Arzew, Barcelona — vroegen zo'n verschuiving van
  enkele honderden meters tot ~1,5 km, telkens genoteerd), niet gezien → **aannemelijk**. Twee sites
  (Gorgon, Tangguh) hebben een coördinaat die een **veld-/eilandcentroïde** is in plaats van het
  exacte terrein en staan daarom bewust op **onzeker**, niet aannemelijk.
- **Eerlijkheidsregel (M30)**: alleen sites met een gebronde capaciteit ÉN aantoonbare productie
  (operationeel, cargo's varen) krijgen gewicht. Projecten die nog geen vol productiejaar achter de
  rug hebben (Golden Pass, Energía Costa Azul), een terminal met sterk gekrompen/onbetrouwbare
  actuele productie (Bontang LNG) en terminals met een coördinaat maar zonder gevonden
  capaciteitscijfer (Huelva, Cartagena, Sagunto, Altamira, Manzanillo) gaan naar
  `sites_zonder_gewicht`. Eén grens is subtieler: **Incheon** (Zuid-Korea) is satelliet-bevestigd op
  het juiste tankpark, maar het enige gevonden capaciteitsgetal (6.270 t/uur) is een piek-
  verwerkingssnelheid, geen gepubliceerd jaarcijfer — op continu-basis doorgerekend geeft het een
  onwaarschijnlijk hoge 54,9 Mt/jaar. Dat getal is **niet** als gewicht gebruikt; Incheon staat
  gedocumenteerd zonder gewicht, met de reden expliciet genoemd (zie de M30-les uit de kobalt-golf:
  een twijfelachtig getal naast harde Mtpa-cijfers valt in de gloed weg of vertekent hem).

## Sites (47 met gewicht)

| id | naam | land | rol | lat, lon | capaciteit bcm/j | bron | coord-bron | status | notitie |
|---|---|---|---|---|---|---|---|---|---|
| `w-raslaffan` | Ras Laffan LNG-complex | Qatar | liquefactie | 25.9265, 51.5955 | 104,7 | 77 Mtpa (2021, 21% wereldaandeel); naar 110→126 Mtpa 2026/27 [B1] | anker hergebruikt uit `gas-raslaffan-chiba.md` (z16) | **bron-gelegd** | 's Werelds grootste LNG-complex; alles door Hormuz. |
| `w-sabinepass` | Sabine Pass LNG Terminal | VS | liquefactie | 29.7541, -93.8741 | 40,8 | 6 trains, 30 Mtpa nameplate [B2] | anker hergebruikt uit `gas-sabinepass-rotterdam.md` (z15) | **bron-gelegd** | Eerste VS-exportterminal (2016); flexibele cargo's. |
| `w-corpuschristi` | Corpus Christi LNG | VS | liquefactie | 27.8797, -97.2645 | 20,4 | Stage 1+2, 15 Mtpa; Stage 3 in opbouw [B2] | anker hergebruikt uit `gas-corpuschristi-incheon.md` (z17) | **bron-gelegd** | — |
| `w-freeport` | Freeport LNG | VS | liquefactie | 28.92537, -95.3263 | 20,4 | 3 trains, 15 Mtpa [B3] | OSM (Photon) | aannemelijk | — |
| `w-cameron` | Cameron LNG | VS | liquefactie | 30.03547, -93.33836 | 16,3 | 3 trains, 12 Mtpa [B4] | Wikidata | aannemelijk | — |
| `w-calcasieu` | Calcasieu Pass LNG | VS | liquefactie | 29.77428, -93.33348 | 13,6 | 18 mid-scale trains, 10 Mtpa [B5] | OSM (Photon) | aannemelijk | — |
| `w-plaquemines` | Plaquemines LNG | VS | liquefactie | 29.60154, -89.8885 | 27,2 | fase 1+2 doel 20 Mtpa, opstartend [B6] | OSM; satelliet z14 | **bron-gelegd** | Opstartend, nog geen vol jaarcijfer. |
| `w-bonny` | Nigeria LNG (Bonny Island) | Nigeria | liquefactie | 4.4258, 7.1531 | 29,9 | 6 trains, 22 Mtpa [B7] | Wikipedia; satelliet z14 | **bron-gelegd** | West-Afrika's grootste LNG-bron. |
| `w-yamal-sabetta` | Yamal LNG (Sabetta) | Rusland | liquefactie | 71.2733, 72.0725 | 23,7 | 3 trains+T4, 17,4 Mtpa [B8] | Wikipedia-geohack | aannemelijk | Arctisch; west+oost route. |
| `w-gorgon` | Gorgon LNG | Australië | liquefactie | -20.79, 115.41 | 21,2 | 3 trains, 15,6 Mtpa [B9] | Wikipedia (veldcentroïde) | **onzeker** | Coördinaat is veld-/complexcentroïde. |
| `w-karratha` | Karratha Gas Plant (NWS) | Australië | liquefactie | -20.58969, 116.77236 | 22,2 | 5 trains, 16,3 Mtpa [B9] | Wikidata | aannemelijk | — |
| `w-wheatstone` | Wheatstone LNG | Australië | liquefactie | -21.6895, 115.0063 | 12,1 | 2 trains, 8,9 Mtpa [B9] | Wikidata | aannemelijk | — |
| `w-ichthys` | Ichthys LNG | Australië | liquefactie | -12.5215, 130.9225 | 11,4 | 2 trains, 8,4 Mtpa [B9] | Wikidata | aannemelijk | 890 km subsea-aanvoer. |
| `w-darwinlng` | Darwin LNG | Australië | liquefactie | -12.52166, 130.86546 | 5,0 | 2 trains, 3,7 Mtpa [B9] | OSM (Photon) | aannemelijk | — |
| `w-pluto` | Pluto LNG | Australië | liquefactie | -20.5905, 116.7755 | 5,8 | 1 trein, 4,3 Mtpa (Train 2 niet meegeteld) [B9] | anker hergebruikt uit `gas-karratha-rudong.md` (z15/z16) | **bron-gelegd** | Onderschat: Train 2 (2023) ontbreekt. |
| `w-prelude` | Prelude FLNG | Australië | liquefactie | -13.78923, 123.3199 | 4,9 | 3,6 Mtpa [B9] | Wikidata | aannemelijk | Drijvend platform. |
| `w-qclng` | Queensland Curtis LNG | Australië | liquefactie | -23.77, 151.196 | 11,6 | 2 trains, 8,5 Mtpa [B9] | Wikidata | aannemelijk | Curtis Island-cluster. |
| `w-glng` | Gladstone LNG | Australië | liquefactie | -23.77021, 151.19549 | 10,6 | 2 trains, 7,8 Mtpa [B9] | Wikidata | aannemelijk | Curtis Island-cluster. |
| `w-aplng` | Australia Pacific LNG | Australië | liquefactie | -23.7554, 151.1896 | 12,2 | 2 trains, 9,0 Mtpa [B9] | Wikidata | aannemelijk | Curtis Island-cluster. |
| `w-malaysialng` | Petronas LNG-complex | Maleisië | liquefactie | 3.2822, 113.0882 | 39,8 | 9 trains, ~29,3 Mtpa (algemeen bekend) [B10] | Wikidata; satelliet z17 | **bron-gelegd** | Cijfer vraagt een verse bronronde. |
| `w-tangguh` | Tangguh LNG | Indonesië | liquefactie | -2.43722, 133.13611 | 15,5 | 3 trains, 11,4 Mtpa (algemeen bekend) [B11] | Wikipedia (veldcentroïde) | **onzeker** | Coördinaat is veldcentroïde, niet het terrein. |
| `w-arzew` | Arzew LNG-complex | Algerije | liquefactie | 35.8078, -0.2395 | 28,4 | GL1Z+GL2Z+GL3Z = 20,9 Mtpa [B12] | Wikipedia (stad); satelliet z16 | **bron-gelegd** | GL4Z (0,9 Mtpa) sinds 2010 dicht. |
| `w-skikda` | Skikda LNG | Algerije | liquefactie | 36.8667, 6.9 | 14,3 | fase1&2 6,0 + nieuwe trein 4,5 = 10,5 Mtpa [B12] | Wikipedia (stad) | aannemelijk | — |
| `w-segas-damietta` | SEGAS LNG (Damietta) | Egypte | liquefactie | 31.46938, 31.74508 | 7,5 | 5,5 Mtpa [B13] | OSM (Photon) | aannemelijk | Periodes stilgelegd door feedgastekort. |
| `w-idku` | Idku LNG (ELNG) | Egypte | liquefactie | 31.34977, 30.31719 | 9,8 | 2 trains, 7,2 Mtpa (algemeen bekend) [B14] | Wikidata | aannemelijk | — |
| `w-angolalng` | Angola LNG (Soyo) | Angola | liquefactie | -6.1196, 12.3366 | 7,1 | 1 trein, 5,2 Mtpa [B15] | Wikidata/OSM | aannemelijk | — |
| `w-omanlng` | Oman LNG + Qalhat LNG | Oman | liquefactie | 22.6599, 59.4057 | 14,6 | 7,4+3,3 = 10,7 Mtpa (algemeen bekend) [B16] | OSM (Photon) | aannemelijk | Twee bedrijven, één terrein. |
| `w-dasisland` | Das Island (ADGAS/ADNOC LNG) | VAE | liquefactie | 25.15, 52.8667 | 7,9 | 3 trains, 5,8 Mtpa (algemeen bekend) [B17] | Wikidata (heel eiland) | **onzeker** | — |
| `w-sakhalin2` | Sakhalin-2 LNG (Prigorodnoje) | Rusland | liquefactie | 46.6275, 142.9028 | 15,8 | 2 trains, 11,6 Mtpa (algemeen bekend) [B18] | Wikipedia-geohack | aannemelijk | — |
| `w-atlanticlng` | Atlantic LNG | Trinidad & Tobago | liquefactie | 10.18389, -61.69361 | 20,4 | 4 trains, 15 Mtpa nameplate [B19] | Wikipedia-geohack | aannemelijk | Feitelijke doorzet lager (feedgastekort). |
| `w-gate` | Gate terminal | Nederland | regas | 51.9711, 4.0689 | 12,0 | 12 bcm/j ontwerpcapaciteit [B20] | anker hergebruikt uit `gas-sabinepass-rotterdam.md` | aannemelijk | Exacte steiger niet scherp gescheiden van de buurterminal (open punt in de brief). |
| `w-southhook` | South Hook LNG Terminal | VK | regas | 51.7168, -5.0778 | 21,2 | 15,6 Mtpa (algemeen bekend) [B21] | Wikipedia; satelliet z16 | **bron-gelegd** | Grootste enkele EU-importterminal. |
| `w-isleofgrain` | Grain LNG | VK | regas | 51.45, 0.68 | 19,6 | ~19,6 bcm/j na 2019-uitbreiding (algemeen bekend) [B22] | Wikipedia; satelliet z14 | **bron-gelegd** | — |
| `w-zeebrugge` | Zeebrugge LNG-terminal | België | regas | 51.3537, 3.2200 | 9,0 | 9 bcm/j (Fluxys) [B23] | anker hergebruikt uit `gas-bonny-zeebrugge.md` (z15/z16) | **bron-gelegd** | — |
| `w-montoir` | Montoir-de-Bretagne | Frankrijk | regas | 47.3028, -2.1417 | 10,0 | 10 bcm/j (Elengy) [B24] | Wikidata | aannemelijk | — |
| `w-revithoussa` | Revithoussa LNG Terminal | Griekenland | regas | 37.9604, 23.4033 | 12,2 | 12,2 bcm/j (DESFA/Wikipedia) [B26] | Wikidata | **onzeker** | Cijfer oogt hoog t.o.v. Grieks gasverbruik. |
| `w-swinoujscie` | Terminal LNG w Świnoujściu | Polen | regas | 53.9092, 14.2947 | 8,3 | 8,3 bcm/j na 2023-uitbreiding (algemeen bekend) [B27] | Wikidata | aannemelijk | — |
| `w-barcelona` | Planta de Barcelona | Spanje | regas | 41.3405, 2.1615 | 13,2 | indicatief ~13,2 bcm/j (algemeen bekend) [B28] | satelliet z16 (kandidaat verschoven) | **bron-gelegd** | Exact adres niet tekstueel gekoppeld. |
| `w-dahej` | Dahej LNG Terminal | India | regas | 21.67498, 72.53532 | 23,8 | 17,5 Mtpa (eind 2018) [B29] | Wikidata; satelliet z14 | **bron-gelegd** | Grootste Indiase regasterminal. |
| `w-hazira` | Hazira Terminal (Shell) | India | regas | 21.08, 72.63 | 6,8 | 5 Mtpa [B29] | Wikipedia-geohack | aannemelijk | — |
| `w-kochi` | Kochi Terminal | India | regas | 9.9667, 76.2167 | 6,8 | 5 Mtpa [B29] | stadscentroïde | **onzeker** | Coördinaat is stadscentroïde. |
| `w-pyeongtaek` | Pyeongtaek LNG Terminal | Zuid-Korea | regas | 37.00242, 126.78434 | 48,8 | 1.721,81 bcf/j = 48,8 bcm/j [B30] | OSM; satelliet z14 | **bron-gelegd** | — |
| `w-rudong` | Rudong LNG Terminal | China | regas | 32.528814, 121.428128 | 9,5 | fase I+II, 7 Mtpa [B31] | GEM-coördinaat, bevestigd door anker `gas-rd-eiland` uit `gas-karratha-rudong.md` (z14/z16) | **bron-gelegd** | — |
| `w-dapeng` | Dapeng LNG Terminal | China | regas | 22.5766, 114.4364 | 9,2 | 6,8 Mtpa [B31] | GEM-coördinaat | aannemelijk | Oudste Chinese importterminal (2006). |
| `w-tianjin` | Tianjin FSRU LNG Terminal | China | regas | 38.9311, 117.8741 | 3,0 | 2,2 Mtpa [B31] | GEM-coördinaat | aannemelijk | Drijvende eenheid (FSRU). |
| `w-sodegaura` | Sodegaura LNG-terminal | Japan | regas | 35.4675, 139.9700 | 32,2 | 27,8→23,7 Mtpa na decommissioning [B32] | anker hergebruikt uit `gas-raslaffan-chiba.md` (z15) | **bron-gelegd** | Grootste opslagcapaciteit van Japan. |
| `w-futtsu` | Futtsu LNG-terminal | Japan | regas | 35.3424, 139.8322 | 13,6 | feitelijke ontvangst ~10 Mtpa/j [B32] | OSM (Photon) | aannemelijk | Nameplate (22,9 Mtpa) veel hoger. |

## Buiten scope (sites_zonder_gewicht, 10 stuks — wel gedocumenteerd, geen gewicht)

- **`w-incheon`** (Zuid-Korea, KOGAS) — anker hergebruikt van `gas-corpuschristi-incheon.md`
  (`gas-incheon-kade`, satelliet z16 aldaar: tanker aan offshore laadplatform, 23 tanks op het
  KOGAS-terrein), maar het enige gevonden capaciteitsgetal (6.270 t/uur regasificatie) is een
  piekverwerkingssnelheid; doorgerekend naar een jaarcijfer (≈55 Mt/j) is dat onwaarschijnlijk hoog
  en niet als gewicht gebruikt. Open punt: een direct gepubliceerd jaardoorzetcijfer vinden —
  Incheon wordt herhaaldelijk "'s werelds grootste LNG-terminal" genoemd en hoort dus waarschijnlijk
  wél zwaar te wegen zodra dat cijfer er is.
- **`w-goldenpass`** (VS) en **`w-costaazul`** (Mexico) — nieuwe liquefactieterminals, eerste
  cargo's in 2025, nog geen vol gebrond productiejaar (eerlijkheidsregel).
- **`w-bontanglng`** (Indonesië) — historisch een van de grootste complexen ter wereld (22,5 Mtpa
  nameplate), maar het aantal actief draaiende trains is sterk gekrompen door dalend veldgas; geen
  betrouwbaar actueel cijfer gevonden.
- **`w-huelva`**, **`w-cartagena-es`**, **`w-sagunto`**, **`w-altamira`** — coördinaat gevonden
  (deels letterlijk uit een Wikipedia-embedded kaartlink), capaciteit niet.
- **`w-manzanillo`** (Mexico) — geen coördinaat gevonden deze ronde.
- **`w-store-rehden`** (Duitsland) — voorbeeld van de opslag-/bufferrol: telt in bcm
  werkgasvoorraad, niet in bcm/j doorzet, en is bewust buiten de gewogen lijst gehouden (de
  M30-les: een percentage/ander-type-getal naast Mtpa-cijfers valt in de gloed weg of vertekent
  hem). `data/gas.js` heeft al vier van dit type node (`gas-store-*`) onder de bestaande
  `reserve`-toggle; deze site staat er ter documentatie naast, niet om die toggle te vervangen.

**Chinese registerbron**: net als bij koper/nikkel is gezocht naar een uniform Chinees register mét
coördinaten (analoog aan het MEE-emissievergunningregister). Voor aardgas/LNG bestaat dat niet: de
~25 Chinese regasterminals (CNOOC/Sinopec/PetroChina) zijn losse, per-provincie aangekondigde
projecten zonder centrale, publiek doorzoekbare coördinatenlijst. De drie Chinese sites in deze
sitelaag (Rudong, Dapeng, Tianjin) komen daarom uit **Global Energy Monitor**-coördinaten (via een
WebSearch-treffer), niet uit een register — een eerlijk genoteerd open punt, geen omissie.

## Bronnen

- **[B1]** Reuters, 'Qatar Petroleum signs deal for mega-LNG expansion' (9-2-2021), via Wikipedia
  'List of LNG terminals' — https://en.wikipedia.org/wiki/List_of_LNG_terminals
- **[B2]** Cheniere Energy — Sabine Pass/Corpus Christi terminal-gegevens, via Wikidata (Q30972616,
  Q30972455) en Wikipedia 'List of LNG terminals'
- **[B3]** Freeport LNG / FERC — Freeport LNG Newsroom, via Wikipedia 'List of LNG terminals'
- **[B4]** Sempra Infrastructure — Cameron LNG project timeline, via Wikipedia 'List of LNG
  terminals' en Wikidata Q30975076
- **[B5]** Venture Global LNG — Calcasieu Pass, via Wikipedia 'List of LNG terminals'
- **[B6]** OilPrice.com, 'Germany Welcomes First LNG Carrier At New Wilhelmshaven Terminal'
  (3-1-2023, ref. Plaquemines-status), via Wikipedia 'List of LNG terminals'; algemene
  2024/2025-berichtgeving over eerste LNG en opstart
- **[B7]** Wikipedia, 'List of LNG terminals' — Afrika-tabel, Nigeria LNG (NNPC Limited)
- **[B8]** Wikipedia, 'Yamal LNG' (Novatek)
- **[B9]** Wikipedia, 'List of LNG terminals' — Australië-tabel (QCLNG/GLNG/APLNG/Karratha/
  Pluto/Wheatstone/Gorgon/Ichthys/Darwin LNG/Prelude), met Woodside/Chevron/Santos/INPEX/
  Shell-bronvermeldingen
- **[B10]** Petronas-communicatie (algemeen bekend, LNG-complex Bintulu, 9 trains) — niet dit keer
  met een verse 2024/2025-bron bevestigd
- **[B11]** BP — Tangguh LNG Train 3 (algemeen bekend) — niet dit keer met een verse bron bevestigd
- **[B12]** Wikipedia, 'List of LNG terminals' — Afrika-tabel, Arzew/Skikda (Sonatrach)
- **[B13]** Wikipedia, 'List of LNG terminals' — SEGAS LNG (Damietta)
- **[B14]** Algemeen bekend — Idku/ELNG (Shell/Petronas/EGAS/EGPC/Engie-JV) — niet dit keer met een
  verse bron bevestigd
- **[B15]** Wikipedia, 'List of LNG terminals' — Angola LNG (Soyo)
- **[B16]** Algemeen bekend — Oman LNG/Qalhat LNG (Sur) — niet dit keer met een verse bron bevestigd
- **[B17]** Algemeen bekend — ADGAS/Das Island (ADNOC LNG) — niet dit keer met een verse bron
  bevestigd
- **[B18]** Algemeen bekend — Sakhalin Energy/Sakhalin-2 (Prigorodnoje) — niet dit keer met een
  verse bron bevestigd
- **[B19]** Wikipedia, 'Atlantic LNG' (Trinidad and Tobago)
- **[B20]** Gasunie/Vopak — gateterminal.com, via Wikipedia 'List of LNG terminals'
- **[B21]** Algemeen bekend — South Hook LNG (Qatar Petroleum/Shell/ExxonMobil-JV) — niet dit keer
  met een verse bron bevestigd
- **[B22]** Algemeen bekend — National Grid Grain LNG (Isle of Grain) — niet dit keer met een verse
  bron bevestigd
- **[B23]** Fluxys — 'Infrastructure in the Zeebrugge zone', via Wikipedia 'List of LNG terminals'
- **[B24]** Elengy (Engie) — Montoir-de-Bretagne, via Wikipedia 'List of LNG terminals' en Wikidata
  Q2387693
- **[B26]** DESFA (DEPA) — Revithoussa, via Wikipedia 'List of LNG terminals' en Wikidata Q7318506
- **[B27]** GAZ-SYSTEM — Świnoujście-uitbreiding 2023 (algemeen bekend) — niet dit keer met een
  verse bron bevestigd
- **[B28]** Enagás — Planta de Barcelona (algemeen bekend) — niet dit keer met een verse bron
  bevestigd
- **[B29]** Wikipedia, 'List of LNG terminals' — India-sectie (Dahej/Hazira/Kochi, Petronet
  LNG/Shell), met bron `thehindubusinessline.com`
- **[B30]** WebSearch (2026-09-28): offshore-technology.com + Korea Times, KOGAS Incheon/Pyeongtaek
  LNG-terminals — https://www.offshore-technology.com/marketdata/pyeongtaek-lng-regasification-terminal-south-korea/ ,
  https://www.koreatimes.co.kr/business/20240630/kogas-bolsters-energy-security-with-worlds-biggest-lng-terminal
- **[B31]** WebSearch (2026-09-28): Global Energy Monitor (gem.wiki) — Rudong (PetroChina), Dapeng
  (CNOOC), Tianjin FSRU (CNOOC) — https://www.gem.wiki/Rudong_LNG_Terminal_(PetroChina) ,
  https://www.lng.cool/en/terminal/rt009 , https://www.gem.wiki/Tianjin_LNG_Terminal_(PipeChina)
- **[B32]** WebSearch (2026-09-28): JOGMEC-journal (oilgas-info.jogmec.go.jp, JERA-hoofdstukken
  2024/2025) + JERA-persbericht (12-6-2026) — Futtsu/Sodegaura LNG-terminals —
  https://oilgas-info.jogmec.go.jp/_res/projects/default_project/_page_/001/010/410/4_32_en_2025_jera.pdf ,
  https://www.jera.co.jp/en/news/information/20260612_2433

Coördinaatbronnen (aanvullend op de [Bn]-lijst): MediaWiki Coordinates-API (`en.wikipedia.org/w/api.php?action=query&prop=coordinates`) ·
Wikidata (`wbsearchentities` + claim P625, via `www.wikidata.org/wiki/Special:EntityData/<Q>.json`) ·
OpenStreetMap via Photon (`photon.komoot.io`) — © OpenStreetMap contributors, ODbL ·
Esri World Imagery via `v2/tools/sat_check.py`.

## Open punten

- **Geen uniform Chinees register met coördinaten** voor LNG-regasterminals (zie hierboven) — de
  drie Chinese sites steunen op Global Energy Monitor, niet op een primair overheidsregister.
- **`w-incheon`** capaciteit: het gevonden getal is een piek-t/uur, geen jaarcijfer — zonder gewicht
  gelaten, ondanks een satelliet-bevestigd anker en Incheons reputatie als 's werelds grootste
  terminal.
- **`w-gorgon`** en **`w-tangguh`**: coördinaten zijn veld-/eilandcentroïdes, geen terreincoördinaat
  — de volgende ronde verdient een gerichte satellietpass om het exacte tankpark te vinden.
- **`w-barcelona`**: satelliet bevestigt een LNG-tankpark op de juiste plek in de haven, maar geen
  tekstuele bron koppelt dat specifieke terrein aan het Enagás-adres — werkt met "aannemelijk"-
  zekerheid, niet volledig sluitend.
- **Zeven Mtpa-cijfers steunen op "algemeen bekend"** in plaats van een vers 2024/2025-document
  (Malaysia LNG, Tangguh, Oman/Qalhat, Das Island, Sakhalin-2, Idku, Skikda-optelling,
  Świnoujście-optelling, South Hook, Isle of Grain, Barcelona) — stuk voor stuk plausibele,
  industrie-brede getallen maar geen van alle dit keer met een primaire bron herbevestigd; een
  volgende ronde met wat webbudget kan dit sluitend maken.
- **Vier Spaanse/Mexicaanse sites zonder capaciteit** (Huelva, Cartagena, Sagunto, Altamira) en
  **één zonder coördinaat** (Manzanillo) — wel gedocumenteerd, wachten op een vervolgronde.
- **Sitelaag ↔ bestaande `data/gas.js`**: dit bestand introduceert 47 site-niveau knopen naast de
  14 bestaande, brede v1-knopen in `data/gas.js` (velden/liquefactie/regas op landniveau). Geen
  van beide is aangepast — de sitelaag is een aparte laag voor de wereldwijde gloed, precies zoals
  bij koper/olie/uranium.
