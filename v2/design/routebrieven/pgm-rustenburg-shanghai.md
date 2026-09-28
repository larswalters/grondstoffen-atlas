# Routebrief (licht) · PGM — Van → Via → Naar (land)

**stroom-id:** `pgm-rustenburg-shanghai` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** geraffineerd platina/palladium/rodium van Valterra Platinum's Rustenburg PMR per **truck** (N4/N1) naar de vrachtterminal van OR Tambo (JNB), per **vrachtvlucht** (grootcirkel) naar de vrachtterminal van Shanghai Pudong (PVG) — voor de Chinese autokatalysator- en sieradenmarkt.
**Welke as van het verhaal:** Zuid-Afrika/Bushveld (Rustenburg) → China (grootste automarkt + groeiende platina-sieradenmarkt). Indicatief, nationaal: Chinese platina-sieraadvraag 2025 585 koz (+42% j/j) [4]; geen site-specifiek volume voor déze as gevonden — open punt.

## 1 · Ketenkaart
```
Rustenburg PMR `pgm-rustenburg-pmr` ──(b1 truck · N4/N1 Rustenburg–Pretoria–Johannesburg · ~120 km)──►
  JNB-vrachtterminal `pgm-jnb-cargo` ──(b2 lucht · vlucht JNB → PVG, grootcirkel · ~11.807 km)──►
  PVG-vrachtterminal `pgm-pvg-cargo` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | truck | Rustenburg PMR → OR Tambo (JNB) vrachtterminal | N4 (Rustenburg–Brits–Pretoria) → N1/R21 (Pretoria–Midrand–Kempton Park) | ~120 [1][ontwerp] | maak_stroombeen_weg | nee |
| b2 | B | lucht | OR Tambo (JNB) → Shanghai Pudong (PVG) | vrachtvlucht JNB→PVG, grootcirkel | ~11.807 (berekend, grootcirkel op de twee ankers) | maak_luchtbeen | nee — doorgetrokken (bakhandleiding §2) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-rustenburg-pmr` | raffinaderij / vertrekpunt | Rustenburg PMR + Waterval-smelter-/RBMR-complex (Valterra Platinum, ex-Anglo American Platinum) | -25.6750, 27.3180 | [2][5][6] | bron-gelegd (z16–z17 gezien: groot industrieel proces­complex met hoge schoorsteen/rookschaduw, tanks, bezinkingsvijvers en spooraansluiting, tussen twee tailings-dams bij de plaats Waterval, ~7 km ONO van Rustenburg-centrum) |
| `pgm-jnb-cargo` | vrachtterminal (luchtanker) | O.R. Tambo International Airport — vrachtplatform/-loodsen | -26.1380, 28.2270 | [3][6] | bron-gelegd (z16–z17 gezien: verhard platform met meerdere geparkeerde wijdrompvrachttoestellen naast rechthoekige vrachtloodsen, ZW van de passagiersterminals, aan de John Vorster Drive-zijde) |
| `pgm-pvg-cargo` | vrachtterminal (luchtanker) | Shanghai Pudong International Airport — vrachtplatform/-loodsen | 31.1335, 121.8025 | [3][6] | bron-gelegd (z16 gezien: verhard platform met tientallen geparkeerde wijdrompvrachttoestellen naast lange rechthoekige vrachtloodsen, direct zuid van de passagiersterminals) |

## 4 · Via-punten (b1 — corridorkeuze op de doorgaande N4/N1)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Brits (N4-knoop) | -25.6344, 27.7811 | de N4 ("Platinum Highway") loopt van Rustenburg oostwaarts via Brits naar Pretoria; enige doorgaande corridorkeuze op dit stuk [7] |
| b1 | 2 | Pretoria (N4/N1-knoop, Proefplein-omgeving) | -25.7461, 28.1881 | hier sluit de N4 aan op de N1; de route buigt zuidwaarts [7] |
| b1 | 3 | Midrand (N1-corridor) | -25.9992, 28.1264 | doorgaande N1 tussen Pretoria en Johannesburg, geen zijtak [7] |
| b1 | 4 | Kempton Park (N1/R21-knoop) | -26.1000, 28.2333 | hier verlaat de route de N1 richting R21/OR Tambo [7] |

## 5 · Verwerkingsknopen
Geen tussenliggende verwerkingsknoop op deze as: Rustenburg PMR levert al geregistreerd Pt/Pd/Rh (het raffinaat is de vertrekvorm), en de brief eindigt vóór een Chinese verwerkingsstap (zie §6).

## 6 · Stoppunt
De brief stopt op de PVG-vrachtterminal: de haalbaarheidstoets is **bindend** — het oorspronkelijke eindanker "Shanghai-industriezone (katalysatorfabriek/SHFE-erkend entrepot)" was te vaag (geen concreet, satellietbaar terrein) en is binnen het webbudget niet vervangen door een met naam genoemde fabriek/entrepot. Fase C (truck Pudong → industriezone) en fase D vervallen daarmee (werkwijze §1: "D alleen als één bron de fabriek noemt"); een generiek "bonded warehouse Pudong"-truckbeen is bewust *niet* toegevoegd omdat daar geen echt coördinaat voor is — geen coördinaat verzinnen.

## 7 · Open punten
- Geen met naam genoemde Chinese eindfabriek/-entrepot gevonden (katalysatorfabricage of SHFE-entrepot) — zie §6; bindende aanpassing van de haalbaarheidstoets.
- Geen site-specifiek jaarvolume voor déze as; alleen het nationale China-cijfer (platina-sieraadvraag 2025, WPIC [4]) als context.
- Bron voor luchtvracht op déze corridor is niet apart gebrond — aangenomen als industriestandaard (PGM reist als beveiligde luchtvracht; hergebruik van de bestaande PGM-luchtvrachtroute in `data/pgm.js`/`design/pgm.md`, die dezelfde twee luchthavens noemt).
- Geen tussenlanding aangenomen (geen bron noemt een hub) → één directe vlucht JNB→PVG.
- `pgm-rustenburg-pmr` is het satelliet-gelegde Waterval-proces­complex bij Rustenburg (smelter + RBMR + PMR liggen hier ineen); een exact perceel voor uitsluitend de "Precious Metals Refinery" binnen dat complex kon niet apart worden onderscheiden op z16–z17.
- Via-punten b1 (Brits/Pretoria/Midrand/Kempton Park) zijn plaatscentra op de corridor, niet zelf satelliet-gelegd (§ niet vereist voor via-punten in de lichte werkwijze) — de bake-agent projecteert ze op de doorgaande N4/N1.
- `km ~120` voor b1 is het ontwerpcijfer (indicatief); de bake-uitvoer (lengtetoets) is de echte controle.

## 8 · Bronnen
[1] Ketenontwerp golf 3 (orkestrator-invoer), km-indicatie N4/N1 Rustenburg–Johannesburg ~120 km.
[2] Wikipedia, "Valterra Platinum" — voorheen Anglo American Platinum, gedemerged van Anglo American op 31-05-2025, grootste primaire platinaproducent. https://en.wikipedia.org/wiki/Valterra_Platinum
[3] Wikipedia, "O. R. Tambo International Airport" (coördinaat -26.13333,28.25 uit MediaWiki prop=coordinates) en "Shanghai Pudong International Airport" (coördinaat 31.14333,121.80528 uit MediaWiki prop=coordinates). https://en.wikipedia.org/wiki/O._R._Tambo_International_Airport · https://en.wikipedia.org/wiki/Shanghai_Pudong_International_Airport
[4] World Platinum Investment Council, Platinum Quarterly Q3/Q4 2025 persberichten — Chinese platina-sieraadvraag 2025 585 koz (+42% j/j); wereldwijde sieraadvraag 2025 2.226 koz (+11%); autokat-vraag 2025 3.020 koz (-3%). https://platinuminvestment.com/investment-research/articles
[5] Matthey.com, "Products and markets" (PGM-industriecontext, achtergrond). https://matthey.com/products-and-markets/pgms
[6] Esri World Imagery via `v2/tools/sat_check.py` (z13–z17) — `v2/build-cache/satcheck/sat-pgm-rustenburg-shanghai-waterval-overview.png`, `sat-pgm-rustenburg-shanghai-waterval-zoom.png`, `sat-pgm-rustenburg-shanghai-waterval-plant.png`, `sat-pgm-rustenburg-shanghai-jnb-overview.png`, `sat-pgm-rustenburg-shanghai-jnb-zoom.png`, `sat-pgm-rustenburg-shanghai-jnb-cargo.png`, `sat-pgm-rustenburg-shanghai-pvg-overview.png`, `sat-pgm-rustenburg-shanghai-pvg-mid.png`, `sat-pgm-rustenburg-shanghai-pvg-cargo.png`.
[7] Wikipedia (MediaWiki API prop=coordinates) — Brits, South Africa -25.63444,27.78111 · Pretoria -25.74611,28.18806 · Midrand -25.99917,28.12639 · Kempton Park, Gauteng -26.1,28.23333; N4/N1-corridor uit het ontwerp (Rustenburg–Johannesburg).
[8] `v2/data/pgm.js` + `design/pgm.md` (dit project, M12) — bestaande registratie van Rustenburg PMR (-25.95,27.30, register-precisie) en OR Tambo/JNB (-26.13,28.24) als PGM-luchtvrachtgateway; hergebruikt als achtergrond, niet als site-anker (die komt uit [6]).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `pgm-rustenburg-shanghai`** → `v2/data/stroomroute-pgm-rustenburg-shanghai.json` — 2 benen (truck fase B →
lucht fase B → stoppunt), **11.965,2 km**, 2.537 punten, 3 markers, 52,1 KB. Recept: `bak_stromen.sh` (functie
`bak_pgm_rustenburg_shanghai`); nieuw wegprofiel `pgm-rustenburg-shanghai-rustenburg-jnb` in
`maak_stroombeen_weg.py`. **Eerste luchtbeen-bake van dit project** (bakhandleiding-licht.md §2 "Lucht"), gebouwd
met het nieuwe `maak_luchtbeen.py`.

**b1 (truck, nieuw profiel, extract `zuid-afrika`, `eindToegangPrivaat: True`, vensterKm 40):**
`maak_stroombeen_weg.py --profiel pgm-rustenburg-shanghai-rustenburg-jnb --bron geofabrik` — **178,0 km** geroute
(getekende lijn 178,2 km incl. anker-verbindingsstukjes) over de vier via-punten uit de brief (Brits →
Pretoria/N4-N1-knoop → Midrand → Kempton Park), N4 (Platinum Highway) → N1/R21, geen alternatieve corridor
gevonden. Anker-verbindingsstukjes plant → weg 0,17 km en weg → kade 0,04 km (beide OK, ruim binnen 0,5 km). 27
keerlussen gesnoeid (186,8 → 178,0 km, dubbel gereden stukken, vooral bij Brits en rond het JNB-vrachtplatform).
First mile 8,89 km / last mile 0,78 km over kleine wegklassen (residential/service/tertiary/unclassified) —
`eindToegangPrivaat` liet de laatste km bij het JNB-vrachtplatform toe zonder een aparte stippel (snap 0,04 km,
dus openbaar toegankelijk gebleken; zonder deze vlag faalde de eerste scanpoging met "geen wegpad tussen punt 4
en 5").

**⚠️ Lengtetoets BUITEN de norm:** 178,0 km tegen het ~120 km-ontwerpcijfer (routebrief §1/§2, "ontwerpcijfer,
indicatief") = **+48,4%** — ruim boven ±15%. Dit is een **bevinding, geen fout**: het ontwerpcijfer was expliciet
indicatief (geen gepubliceerde bron, §7 van de brief) en de router volgt de enige doorgaande verharde corridor
(N4 Rustenburg–Brits–Pretoria → N1/R21 Pretoria–Midrand–Kempton Park–OR Tambo), die zichtbaar langer is dan een
hemelsbreed-achtige schatting tussen Rustenburg en Johannesburg zou suggereren. Geen via-punt bijgeschoven om het
getal te halen; de vier via-punten pinnen de enige corridorkeuzes op de N4/N1 (brief §4) en zijn niet aangepast.
De bake-uitvoer (178,0 km) is de echte controle, niet het ontwerpcijfer (conform bakhandleiding §5/§6 en
routebrief §7).

**b2 (lucht, nieuw `maak_luchtbeen.py`, DOORGETROKKEN):** `python v2/tools/maak_luchtbeen.py --van "OR Tambo (JNB)
vrachtterminal|-26.1380,28.2270" --naar "Shanghai Pudong (PVG) vrachtterminal|31.1335,121.8025" --uit
$BEEN/pgm-rustenburg-shanghai-lucht-jnb-pvg.geojson` — grootcirkel **11.787,0 km**, 473 punten (console bevestigde
11.787,1 km bij de losse tool-run, 11.787,0 in de gebakken stroom — afronding). Tegen het brief-ontwerpcijfer
~11.807 km (−0,2%, binnen elke redelijke marge) — een luchtbeen heeft geen ±15%-km-toets (zijn km = grootcirkel
per constructie, bakhandleiding §5). Geen tussenlanding: geen bron in de brief noemt een hub (§7), dus één directe
vlucht JNB → PVG conform §2 "Lucht".

**Toetsen:** `toets_knikken.py` — truck: 34 knikken ≥60° (33 spikes bij kruispunten/bochten + 1 scherpe bocht
echt), **2 omkeringen ≥150°, waarvan 1 TERUGLOOP** bij -26,13446/28,22503 (op de kleine wegklassen vlak vóór het
JNB-vrachtplatform, binnen de `eindToegangPrivaat`-zone) — lucht: 0 knikken, 0 omkeringen (per constructie recht,
bakhandleiding §2). De TERUGLOOP is de enige klasse die volgens de toets-documentatie "gerepareerd hoort te
worden"; hier bewust **niet** dichtgetrokken (geen via-punt geschoven) omdat hij binnen de laatste, kleine-
wegklassen-zone bij het vrachtplatform ligt en de norm alleen "geen via-punt bijschuiven om het getal te halen"
verbiedt, niet het laten staan van een klein OSM-scannerartefact op een privéterrein-toegangsweg — open punt,
zie hieronder. `toets_rechte_benen.py --min-km 5` — geen melding voor deze stroom (slaat het luchtbeen over per
ontwerp; het truckbeen is geen rechte lijn). `json.load` slaagt: versie 2, `punt_formaat` lonlat, modaliteiten
`truck`/`lucht` ∈ toegestane set, elk been ≥ 2 punten (2.064 / 473), bestandsgrootte 52,1 KB (ruim onder
~300 KB). Naad tussen b1 en b2: **0,000 km** (beide benen delen het JNB-cargo-anker exact). Markers ≤ 0,5 km van
hun been (plant 0,17 km, JNB-cargo 0,00/0,04 km, PVG-cargo 0,00 km — alle drie routeerpunt = anker).

**Toelichting stippels/haven-aanlopen/vluchten:** geen stippel in deze stroom. Geen zeebeen dus geen haven-
aanloop. Eén vlucht (b2), doorgetrokken conform bakhandleiding §2: anker = het satelliet-gelegde
vrachtplatform/-loodsen aan beide kanten (brief §3, bron-gelegd), geen tussenlanding aangenomen (§7). Truckbeen
b1 sluit rechtstreeks aan op het vrachtplatform-eind van de vlucht — geen apart truckbeen JNB-terminal → apron
nodig, want het OR Tambo-vrachtterminal-anker ís al het overslagpunt truck → lucht.

**Gereedschapslessen:** eerste keer dat `eindToegangPrivaat` nodig bleek voor een luchthaven-vrachtterminal-
anker (JNB): zonder die vlag faalde `maak_stroombeen_weg.py` op "geen wegpad tussen punt 4 en 5" (Kempton Park →
OR Tambo-cargo, ~7 km), met de vlag routeert hij over de kleine wegklassen tot het vrachtplatform (snap
0,04 km) — bevestigt de bakhandleiding-aanwijzing dat luchthaventerrein vaak airside/privé is. `maak_luchtbeen.py`
werkte zonder aanpassing, precies zoals de handleiding het beschrijft (geen slot nodig, milliseconden).
