# Routebrief (licht) · goud — Siguiri (Guinee) → Conakry → Dubai (VAE)

**stroom-id:** `goud-siguiri-dubai` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** Goud uit de Siguiri-mijn (AngloGold Ashanti/SMD, Guinee) gaat per truck over de N1-corridor naar de vrachtterminal van Conakry Int'l (CKY), vliegt als vrachtvlucht (grootcirkel) naar Dubai International Airport (DXB), en gaat per truck naar de DMCC-raffinagezone (Emirates Gold/Kaloti) in Jumeirah Lake Towers — de derde, onafhankelijke West-Afrikaanse lucht-as naar Dubai naast de Ghana- en Mali-assen van deze golf.
**Welke as van het verhaal:** *West-Afrika (Guinee) → Dubai: het "grijze kanaal" wordt zichtbaar naast het industriële.* West-Afrikaans (incl. Guinees) artisanaal én industrieel goud wordt in Swissaid/OECD-ketenonderzoeken breed gerapporteerd als voornamelijk per lucht naar Dubai geëxporteerd [8][9]. Jaarvolume Guinee ≈25-30 t Au/j (USGS MCS 2025, indicatief, peiljaar 2024) [11]; Siguiri-mijn zelf (AngloGold Ashanti 85% + Guinee 15%) produceerde FY2025 289.000 oz **attributable** ≈ 8,99 t Au/j (attributable) ≈ 10,58 t Au/j (100%-mijnbasis) — oorspronkelijke eenheid troy ounce, omgerekend koz ÷ 32,15 = t [1][2]. Zwakste bronbasis van deze golf: geen bedrijfsbron koppelt de Siguiri-mijn specifiek aan een Dubai-luchtvrachtstroom (zie §7).

## 1 · Ketenkaart
```
Siguiri-mijn (AngloGold Ashanti/SMD, Kintinian) `au-siguiri-mijn` ──(b1 truck · N1 Siguiri–Kouroussa–Dabola–
   Mamou–Kindia–Coyah–Conakry · ~850 km ontwerp)──►
Conakry Int'l (CKY), vrachtterminal `au-cky-cargo` ──(b2 lucht · vlucht CKY → DXB, grootcirkel · ~7.100 km)──►
Dubai Intl Airport (DXB), Emirates Air Cargo `au-dxb-cargo` ──(b3 truck · Sheikh Zayed Road (E11) · ~20-29 km)──►
DMCC-raffinagezone / Emirates Gold-Kaloti, Almas Tower `au-dubai-dmcc` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Siguiri-mijn → Conakry (CKY) vrachtterminal | N1, via Kouroussa–Dabola–Mamou–Kindia–Coyah | ~850 [ontwerp]; som via-punten (hemelsbreed) ≈557 km | maak_stroombeen_weg | nee |
| b2 | B | lucht | Conakry (CKY) vrachtterminal → Dubai Intl (DXB) vrachtterminal | vlucht CKY → DXB, grootcirkel | ~7.100 [ontwerp]; grootcirkel wordt bij het bakken exact berekend | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | Dubai Intl (DXB) vrachtterminal → DMCC-raffinagezone | Sheikh Zayed Road (E11), enige doorgaande corridor | ~20 [ontwerp]; anker-tot-anker hemelsbreed ≈29 km | maak_stroombeen_weg | nee |

Fase C reproduceert bewust dezelfde E11-corridor als `diamant-marange-dubai` (DXB-cargo → DMCC/Almas Tower): zelfde
fysieke route, andere grondstof. `au-dxb-cargo` en `au-dubai-dmcc` zijn coördinaat-identiek aan die brief se ankers
(hergebruik, zie §3) — niet opnieuw satelliet-gelegd vanaf nul maar wél met een eigen sat_check-pass bevestigd.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-siguiri-mijn` | mijn / laadplek | Siguiri-mijn (AngloGold Ashanti/SMD), Kintinian, Boure-gebied | 11,5695, -9,3567 | [1][2][3][4] | bron-gelegd (z15 gezien: uitgestrekt open-pit-mijncomplex met meerdere putten, tailings-/waterbekkens en ontginningswegen rond Kintinian — ~26,8 km ten noordwesten van Siguiri-stad, consistent met de gepubliceerde "25 km NW van Siguiri" [1]) |
| `au-cky-cargo` | vrachtterminal / vertrek luchtvracht | Conakry Int'l (Ahmed Sékou Touré, CKY), vracht-/GA-apron | 9,5748, -13,6205 | [5][6][7] | aannemelijk (z17 gezien: gebouwencluster + apron met meerdere kleine vliegtuigen direct naast de terreinweg aan de zuidoostzijde van de startbaan, vlak bij de passagiersterminal; geen expliciete vrachtloods-naambordering zichtbaar — de luchthaven bouwt volgens 2025-nieuwsbericht een nieuwe, aparte vrachtterminal [7], dus dit satellietbeeld kan gedateerd zijn) |
| `au-dxb-cargo` | vrachtterminal / aankomst luchtvracht | Dubai Intl (DXB), Emirates Air Cargo-gebouw, Al Garhoud | 25,2575, 55,3406 | [9][10] | bron-gelegd (z15 gezien, eigen sat_check-pass: groot vrachtgebouw direct aan de apron met tientallen geparkeerde vliegtuigen — coördinaat hergebruikt van `diamant-marange-dubai` `dia-dxb-cargo`, daar al satelliet-bevestigd met OSM-naam "الإمارات للشحن الجوي / Emirates Air Cargo") |
| `au-dubai-dmcc` | raffinage-/handelszone (Emirates Gold/Kaloti, DMCC) | DMCC, Almas Tower, Jumeirah Lake Towers | 25,0691, 55,1412 | [10][12][13] | bron-gelegd (z15 gezien, eigen sat_check-pass: herkenbare torenvoet in het JLT-torencluster rond het meer, met een marina aan de noordwestzijde — coördinaat matcht exact de OSM-polygoon "برج الماس / Almas Tower" [10] en is coördinaat-identiek aan `au-hub-dubai` uit goud.js v1, zoals het ketenontwerp voorschrijft) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Kouroussa | 10,6514, -9,8810 | eerste stadsknoop op de N1 vanaf Siguiri, vóór de doorgaande corridor naar Dabola |
| b1 | 2 | Dabola | 10,7422, -11,1065 | tussenstad op de N1, enige doorgaande route tussen Kouroussa en Mamou |
| b1 | 3 | Mamou | 10,3741, -12,0836 | knooppuntstad op de N1, waar de corridor richting kust ombuigt |
| b1 | 4 | Kindia | 10,0368, -12,8260 | laatste grote tussenstad vóór de kustregio, op de doorgaande N1 |
| b1 | 5 | Coyah | 9,7090, -13,3890 | laatste knoop vóór de aansluiting op de Conakry-stadsrand/luchthavenweg |
| b3 | 1 | Dubai World Trade Centre-interchange | 25,2276, 55,2888 | zelfde E11-interchange als in `diamant-marange-dubai` — enige doorgaande snelweg tussen DXB en JLT |
| b3 | 2 | Mall of the Emirates-interchange | 25,1181, 55,2006 | zelfde tweede vaste interchange, vlak vóór de afslag naar JLT/DMCC |

## 5 · Verwerkingsknopen
*(geen aparte verwerkingsknoop getekend — DMCC/Emirates Gold-Kaloti is de raffinage-/handelszone zelf en is al
anker `au-dubai-dmcc`; Conakry CKY is overslag lucht↔weg, geen bewerking.)*

## 6 · Stoppunt
De brief stopt bij de DMCC-raffinagezone (Emirates Gold/Kaloti, Almas Tower): dit is precies de "naar_site" uit het
ketenontwerp en het punt waar de goudstroom van ruw/doré overgaat naar geraffineerd/verhandeld product. Geen bron
koppelt deze specifieke stroom aan een vervolgbestemming (sieradenfabriek, andere kluis) — fase D en E vervallen.

## 7 · Open punten
- **Geen bedrijfsbron koppelt de Siguiri-mijn specifiek aan een Dubai-luchtvrachtstroom** — het ketenontwerp en de
  haalbaarheidstoets erkennen dit zelf al als de zwakste bronbasis van de golf: de regionale Swissaid/OECD-bevinding
  dat West-Afrikaans (incl. Guinees) goud overwegend per lucht naar Dubai gaat is niet mijn- of bedrijfsspecifiek [8][9].
  Het gedocumenteerde artisanale/smokkelaandeel domineert vermoedelijk de werkelijke luchtstroom uit Guinee; de
  industriële Siguiri→Dubai-relatie blijft aannemelijk, niet bevestigd.
- **`au-cky-cargo` is niet scherp bevestigd als toegewijd vrachtplatform** — het satellietbeeld (z17) toont een
  apron met kleine vliegtuigen en een gebouwencluster naast de terminal, geen duidelijke vrachtloodsen met
  naambordering. De luchthaven bouwt volgens een nieuwsbericht van 2025 een nieuwe, aparte vrachtterminal [7] — het
  huidige beeld kan dus een verouderde situatie tonen. Status blijft *aannemelijk*, niet *bron-gelegd*.
- **Geen gepubliceerde wegkilometrage voor de N1 Siguiri–Conakry-corridor** gevonden binnen het webbudget; de
  ~850 km uit het ketenontwerp is niet onafhankelijk bevestigd, alleen intern plausibel (som via-punten hemelsbreed
  ≈557 km, typisch 30-50% korter dan de werkelijke wegafstand over vijf tussenliggende steden).
- **Geen gepubliceerde vluchtlengte CKY→DXB** — berekende grootcirkel bij het bakken (geen gekarteerd
  luchtwegennet bestaat); een tussenlanding is niet uitgesloten maar door geen bron genoemd, dus aangenomen: één
  directe vlucht.
- **Fase C (DXB→DMCC) hergebruikt de geometrie/via-punten van `diamant-marange-dubai`** zonder eigen, aparte
  bronbevestiging voor dít specifieke goud-traject — wel dezelfde fysieke, enige-doorgaande corridor (E11).
  Ontwerp-km (~20) en anker-tot-anker hemelsbreed (~29 km) wijken merkbaar af; bij het bakken bepaalt de gemeten
  wegroute het definitieve getal.
- **AngloGold Ashanti's aandeel dat specifiek naar Dubai (i.p.v. Zwitserland of andere raffinaderijen) gaat** is
  niet met een bedrijfsbron bevestigd — AngloGold Ashanti's eigen investor-pagina's noemen geen Dubai-specifieke
  afzetroute voor Siguiri-doré binnen het webbudget.
- **Jaarvolume-eenheid:** troy ounce als brongegeven (289.000 oz attributable FY2025); Guinee-totaal 25-30 t/j is
  USGS-indicatief voor heel Guinee (industrieel + artisanaal), niet Siguiri-specifiek.

## 8 · Bronnen
[1] AngloGold Ashanti — "Siguiri, Guinea" (portfolio-pagina): locatie ~850 km NNO van Conakry, 25 km NW van Siguiri-stad, 220 km ZO van Bamako; FY2025-productie 289.000 oz attributable; eigendom AngloGold Ashanti 85% / overheid Guinee 15%; CIL-plant, 11,8 Mt/j doorzet. https://www.anglogoldashanti.com/portfolio/africa/siguiri/
[2] Mining Technology — "Siguiri Gold Mine, Republic of Guinea, West Africa": Boure-gebied, ~40.000 inwoners in 12 dorpen incl. Kintinian, CIL-circuit, 30MW eigen centrale. https://www.mining-technology.com/projects/gold_siguiri/
[3] Wikipedia — "Siguiri": coördinaat 11,41667/-9,16667, stad aan de Niger, Kankan-regio, bekend om goudsmeden. https://en.wikipedia.org/wiki/Siguiri
[4] OpenStreetMap (ODbL) via Nominatim/Photon — "mine d'or" (landuse=quarry), Kintinian, Préfecture de Siguiri, Kankan: 11,5695356/-9,3567154. https://www.openstreetmap.org
[5] Wikipedia — "Ahmed Sékou Touré International Airport" (CKY, ICAO GUCY, ook Gbessia International Airport genoemd), Conakry. https://en.wikipedia.org/wiki/Ahmed_S%C3%A9kou_Tour%C3%A9_International_Airport
[6] OpenStreetMap (ODbL) via Nominatim — "Aéroport International Ahmed Sékou Touré", aerodrome-centrum 9,5765513/-13,6130758. https://www.openstreetmap.org
[7] Aeroport Ahmed Sékou Touré (officiële site) — Fret-pagina, cargo-import/exportproces; Guineelive (21-06-2026) nieuwe fret-tarieven; Africaguinee — Q1-2026 verkeersgroei, cargo-sector +20,85% (4.973 t/eenheden). https://aeroportahmedsekoutoure.com/Corporate/Fret · https://guineelive.com/2026/06/21/aeroport-international-ahmed-sekou-toure-de-nouveaux-tarifs-de-fret-aerien-entrent-en-vigueur/ · https://www.africaguinee.com/aeroport-international-ahmed-sekou-toure-envolee-historique-du-trafic-aerien-au-premier-trimestre-2026/
[8] SWISSAID — "On the trail of African gold" / "Alarming rise in gold imports from Dubai": Afrikaans goud wordt breed per lucht (ruim, koerier of in het ruim) naar Dubai vervoerd; 2.596 t ongedeclareerd Afrika→VAE 2012-2022. https://www.swissaid.ch/en/articles/on-the-trail-of-african-gold/
[9] Mining Weekly (30-05-2024) — "Billions in African gold smuggled to UAE yearly, SWISSAID says"; Ecofin Agency — UAE-goudimport uit Afrika +18% in 2024. https://www.miningweekly.com/article/billions-in-african-gold-smuggled-to-uae-yearly-swissaid-says-2024-05-30 · https://www.ecofinagency.com/news-industry/0611-50175-uae-gold-imports-from-africa-rise-18-in-2024-says-swissaid
[10] OpenStreetMap (ODbL) — "الإمارات للشحن الجوي / Emirates Air Cargo" (building, 25,25745/55,34060, binnen DXB); "برج الماس / Almas Tower" (building=apartments, 25,0690625/55,1411656, JLT) — beide ankers hergebruikt/bevestigd via `diamant-marange-dubai` (`dia-dxb-cargo`, `dia-dmcc`) en via een eigen sat_check-pass in deze brief. https://www.openstreetmap.org
[11] USGS Mineral Commodity Summaries 2025 (Gold) — Guinee-productie indicatief ≈25-30 t Au/jaar, peiljaar ±2024.
[12] Wikipedia — "Dubai Multi Commodities Centre" (DMCC): Almas Tower, Jumeirah Lake Towers, goud-/edelmetalenhandel. https://en.wikipedia.org/wiki/Dubai_Multi_Commodities_Centre
[13] Wikipedia — "Emirates Gold": edelmetaalraffinaderij/muntslagerij gevestigd in Dubai, opgericht 1992, sinds 2024 eigendom van Bright East Holding 1 (ADGM). https://en.wikipedia.org/wiki/Emirates_Gold
[14] OpenStreetMap (ODbL) via Photon — Kouroussa (10,6513609/-9,881002), Dabola (10,742172/-11,106486), Mamou (10,374074/-12,08356), Kindia (10,0368/-12,8260215), Coyah (9,709041/-13,388956) — via-punten op de N1-corridor. https://www.openstreetmap.org
[15] Esri World Imagery via `v2/tools/sat_check.py` (z14-z17, live) — `sat-goud-siguiri-dubai-mijn-kintinian.png`, `-cky-overview.png`, `-cky-cargo-zoom.png`, `-dxb-cargo.png`, `-dmcc.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `goud-siguiri-dubai`** → `v2/data/stroomroute-goud-siguiri-dubai.json` — 3 benen (2 truck, 1 lucht),
**8.225,1 km**, 9.882 punten, 4 markers, 197,5 KB. Recept: `bak_stromen.sh` (functie `bak_goud_siguiri_dubai`);
één nieuw wegprofiel (`goud-siguiri-dubai-siguiri-cky`) in `maak_stroombeen_weg.py`; het luchtbeen met
`maak_luchtbeen.py`, letterlijk volgens `bakhandleiding-licht.md` §2 "Lucht" — doorgetrokken, geen stippel.
Been b3 (DXB→DMCC) hergebruikt de al eerder gebakken geometrie van `diamant-marange-dubai` (dezelfde ankers,
coördinaat-identiek), conform de bak-aanwijzing in de opdracht — geen tweede scan.

**b1 (truck, nieuw profiel `goud-siguiri-dubai-siguiri-cky`, extract `guinee`, vensterKm 60):**
`maak_stroombeen_weg.py --profiel goud-siguiri-dubai-siguiri-cky --bron geofabrik` — **742,7 km** geroute
(getekende lijn 743,0 km incl. anker-verbindingsstukjes) over de N1-corridor via Kouroussa–Dabola–Mamou–
Kindia–Coyah. Alle zes subsnaps 0,04–1,82 km (geen via-punt >5 km mis). Anker-verbindingsstukjes plant → weg
0,29 km en weg → kade 0,04 km (beide OK). 8 kleine keerlussen gesnoeid (744,0 → 742,7 km). Doorgetrokken
(geen stippel) — geen enkel subbeen was korter dan ~2 km of overduidelijk airside/privéterrein.

**b2 (lucht, `maak_luchtbeen.py`):** CKY (9,5748/-13,6205) → DXB (25,2575/55,3406) — **7.447,3 km**
grootcirkel, 299 punten. Doorgetrokken; geen gepubliceerde vluchtlengte (brief §7), grootcirkel is per
constructie de bron. Geen bron noemt een tussenlanding → één directe vrachtvlucht (aanname in §7).

**b3 (truck, geometrie hergebruikt van `diamant-marange-dubai-weg-dxb-dmcc.geojson`):** DXB-vrachtterminal →
DMCC/Almas Tower over Sheikh Zayed Road (E11) — **34,757 km**, 514 punten. Doorgetrokken.

**⚠️ Lengtetoets BUITEN de norm op twee van de drie benen — bevinding, geen fout:**
- **b1:** 742,7 km tegen ~850 km ontwerp = **−12,6%** (binnen de ±15%-norm van `bakhandleiding-licht.md`,
  buiten de ±10%-waarschuwing van het weg-tool). Geen gepubliceerde wegkilometrage voor de N1
  Siguiri–Conakry-corridor gevonden binnen het webbudget; ~850 km was zelf al niet onafhankelijk bevestigd
  (brief §7). Geen via-punt bijgeschoven om het getal te halen.
- **b3:** 34,757 km tegen ~20 km ontwerp = **+73,8%, BUITEN ±15%**. Het ontwerp-getal (~20 km) lag zelf al
  onder de anker-tot-anker hemelsbreed-afstand (~29 km) — voorzien in de bak-aanwijzing van de opdracht. De
  gemeten wegroute (enige doorgaande E11-corridor, dezelfde als `diamant-marange-dubai`) is leidend.

**Toetsen:** `toets_knikken.py` — b1: 12 knikken ≥60° (alle spikes, R 4–52 m, geen echte scherpe bocht); b2
(lucht): 0 knikken; b3: 13 knikken ≥60° (12 spikes + 1 echte scherpe bocht R 5 m + **1 TERUGLOOP** R 4 m bij
25,25382/55,33649, vlak bij het DXB-vrachtterminalanker). **Totaal 25 knikken ≥60°, 2 omkeringen ≥150°,
waarvan 1 terugloop.** De terugloop zit in de van `diamant-marange-dubai` hergebruikte b3-geometrie (niet
eigen scanwerk van deze bake) — gemeld als bevinding, niet gerepareerd (conform "gedeeld been = letterlijke
kopie", `bakhandleiding-licht.md` §6). `toets_rechte_benen.py --min-km 5` — geen melding voor deze stroom
(het luchtbeen wordt per constructie overgeslagen; beide truckbenen zijn geen rechte lijn, omwegfactor >
1,000). `json.load` slaagt: versie 2, `punt_formaat` lonlat, modaliteiten `truck`/`lucht` ∈ toegestane set,
elk been ≥ 2 punten (299–9.069), bestandsgrootte 197,5 KB (ruim onder ~300 KB). Naden tussen alle drie
opeenvolgende benen: **0,000 km** (elk been begint exact waar het vorige eindigt). Markers: alle 4 op de
ankercoördinaat van hun been (≤ 0,1 m).

**Toelichting stippels/haven-aanlopen/vluchten:** geen stippel in deze keten — geen zeebeen, dus geen
haven-aanloop nodig. **Eén vlucht**, doorgetrokken grootcirkel tussen twee satelliet-gelegde vrachtterminals;
`au-cky-cargo` is *aannemelijk* (niet bron-gelegd) — het z17-satellietbeeld toont een GA-apron met kleine
vliegtuigen, geen duidelijke vrachtloodsen, en volgens 2025-nieuws bouwt de luchthaven een nieuwe, aparte
vrachtterminal, dus dit beeld kan gedateerd zijn (brief §3/§7). De overige drie ankers zijn bron-gelegd
(`au-dxb-cargo` en `au-dubai-dmcc` zijn hergebruikte, eerder al satelliet-bevestigde ankers).

**Gereedschapslessen:** het hergebruiken van een eerder gebakken been (`--been-geojson` naar een geojson dat
niet uit deze bake komt) werkt zonder aanpassing — `hecht_marnet.py route` behandelt elk `--been-geojson`
gelijk, ongeacht welke bake het geproduceerd heeft, en meldt het gewoon als "vooraf gebakken lijn". Dat
bevestigt de bak-aanwijzing uit de opdracht: een gedeelde corridor tussen twee stromen van verschillende
grondstoffen hoeft nooit een tweede keer gescand te worden, zolang de ankers coördinaat-identiek zijn. Verder
geen nieuwe tool-issues; `maak_luchtbeen.py` gaf zoals verwacht exact de grootcirkel-km (per constructie geen
afwijking mogelijk).
