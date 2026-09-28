# Routebrief (licht) · kobalt — Mutanda-mijn (DR Congo) → Kasumbalesa/Solwezi/Katima Mulilo → Walvis Bay (Namibië, land)

**stroom-id:** `kobalt-mutanda-walvisbay` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** kobalthydroxide (+ koperkathode) van de **Mutanda-mijn** (Glencore, Lualaba) — die zijn
eigen SX-EW/hydroxide-plant heeft, dus de raffinage zit al bij de bron — gaat volledig per **truck** de
westelijke DRC-uitgang: mijnweg → RN39/RN1 (Likasi/Lubumbashi) → **Kasumbalesa** → Zambische T3
(Chililabombwe/Chingola) → T5 (Solwezi) → het WCL-Trans-Caprivi-tracé (Mutanda(ZM)/Kasempa/Kaoma/Mongu/
Senanga/Sesheke) → grens **Katima Mulilo** → Namibische B8/B1/B2 → **Walvis Bay-haven** — stoppunt, geen
overzeese afnemer gedocumenteerd.
**Welke as van het verhaal:** de Walvis Bay-corridor als derde uitgang naast Kasumbalesa→Durban (TFM) en
Kolwezi→Lobito (Kamoa), nu voor Mutanda i.p.v. nogmaals TFM/Durban. Mutanda produceerde **≈8 kt Co (2024,
Cobalt Institute Market Report)** [2], maar het **DRC-exportquotum 2026 beperkt Mutanda tot 6.700 t Co**;
Glencore's eigen Q1-2026-productie viel **−39% jaar-op-jaar** en boven-quotum materiaal wordt binnenlands
opgeslagen in plaats van geëxporteerd [10][11]. Het aandeel van dit (kleinere, onregelmatigere) volume dat
specifiek via Walvis Bay gaat i.p.v. Durban/Dar es Salaam/Kasumbalesa is in geen bron gekwantificeerd — de
exacte onzekerheid die `koper-sentinel-walvisbay.md` §7 ook al vlagt voor Sentinel-koper.

## 1 · Ketenkaart
```
Mutanda-mijn (+plant) `co-mutanda-laad` ──(b1 truck · RN39/RN1 via Likasi/Lubumbashi · ~290,0 km hemelsbreed)──►
Kasumbalesa-grens (hergebruikt) ──(b2 truck · Zambische T3 via Chililabombwe/Chingola → T5 · ~198,4 km hemelsbreed)──►
Solwezi ──(b3 truck · WCL-Trans-Caprivi-tracé via Mutanda(ZM)/Kasempa/Kaoma/Mongu/Senanga/Sesheke · 906,3 km gemeten)──►
Katima Mulilo-grens (hergebruikt) ──(b4 truck · Namibische B8→B1→B2, letterlijke kopie · 1.421,6 km gemeten)──►
Walvis Bay-haven `co-walvisbay-kade` (hergebruikt) ⏹ stoppunt (geen gedocumenteerde overzeese afnemer)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `co-mutanda-laad` → `co-kasumbalesa-grens` | mijnweg → RN39 (via Likasi) → RN1 (via Lubumbashi) → Kasumbalesa — via-punten hergebruikt uit `koper-kolwezi-durban.md` §4 | ~290,0 km hemelsbreed, geen wegkm (eigen berekening; zelfde soort schatting als `kobalt-kisanfu-daressalaam` b1, die met dezelfde via-punten ~290 km gaf) | `maak_stroombeen_weg` — **nieuw profiel** `kobalt-mutanda-kasumbalesa`, extract `congo-drc` | nee |
| b2 | A | truck | `co-kasumbalesa-grens` (hergebruikt) → Solwezi | Chililabombwe → Chingola op de **T3** (bevestigd: Chililabombwe ligt "op de T3-weg, 17 km zuid van Kasumbalesa, 20 km noord van Chingola" [6]) → **T5** Chingola–Solwezi (bevestigd bestaande weg, Wikipedia [7]) — de constructie uit het ontwerp is hiermee een reëel doorgaand tracé, geen aanname meer | ~198,4 km hemelsbreed, geen wegkm (eigen berekening via Chililabombwe/Chingola-coördinaten [6][9]; tegen ~185 km uit het ontwerp) | `maak_stroombeen_weg` — **nieuw profiel** `kobalt-kasumbalesa-solwezi`, extract `zambia`, refs T3/T5 | nee |
| b3 | A | truck | Solwezi → Katima Mulilo-grens | Solwezi–Mutanda(ZM)–Kasempa–Kaoma–Mongu–Senanga–Sesheke — **zelfde via-puntcoördinaten als `koper-sentinel-walvisbay.md` §4** (WCL-Trans-Caprivi-tracé), ander beginpunt dan Sentinel-mijn | **906,3 km — gemeten wegkm, hergebruikt** uit `koper-sentinel-walvisbay.md` §9 (b1-subtraject Solwezi→grens: Mutanda(ZM) 33,4 + Kasempa 147,3 + Kaoma 219,1 + Mongu 190,6 + Senanga 103,6 + Sesheke 206,4 + grens 5,9 km). **Vervangt de ontwerp-schatting "~416 km"**, die op de door `koper-sentinel-walvisbay.md` §7 al ontkrachte WCL-"371 km"-bronfout berustte (haalbaarheidstoets, bindend) | `maak_stroombeen_weg` — **nieuw profiel** `kobalt-solwezi-katimamulilo`, extract `zambia` — zelfde via-puntenset als `koper-sentinel-walvisbay` b1, ander beginpunt (Solwezi i.p.v. Sentinel-mijn) → geen letterlijke kopie, wel vrijwel identiek tracé | nee |
| b4 | B | truck | Katima Mulilo-grens (hergebruikt) → `co-walvisbay-kade` (hergebruikt) | Namibische **B8** (Katima Mulilo–Rundu–Otavi) → **B1** (Otavi–Otjiwarongo–Karibib) → **B2** (Karibib–Swakopmund–Walvis Bay) — de Walvis Bay-Ndola-Lubumbashi Development Road [3] | **1.421,6 km — gemeten wegkm, LETTERLIJKE KOPIE** van `koper-sentinel-walvisbay.md` b2 | **LETTERLIJKE KOPIE** van `v2/build-cache/ais/graaf/koper-sentinel-walvisbay-weg-katimamulilo-walvisbay.geojson` (functie `bak_koper_sentinel_walvisbay`, been b2) — extract `namibie`, geen nieuw profiel | nee |

Geen zee-been: de brief stopt bij de Walvis Bay-kade (§6). Geen last-mile-benen: `co-mutanda-laad` is het
site-anker en tevens het beginpunt van b1.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-mutanda-laad` | mijn + hydroxide-plant (raffinage al bij de bron) | Mutanda-mijn (Glencore, Lualaba, DR Congo) | -10.7858, 25.8082 | `v2/design/kobalt-sitelaag.json` (`w-mutanda`) [1][15] | **bron-gelegd (hergebruikt)**: sitelaag noteert "satelliet z15: kruis in de open put, SX-EW-plant direct ZW zichtbaar". Nog **geen eigen `sat_check.py`-run onder het stroom-id-prefix van déze keten** — bakhandleiding §0.2, open punt bij het bakken |
| `co-kasumbalesa-grens` | grensovergang DRC/Zambia (hergebruikt) | Kasumbalesa grenspost | -12.2658, 27.7959 | `koper-kolwezi-durban.md` §3/§4, `kobalt-kisanfu-daressalaam.md` §3 | bron-gelegd (hergebruikt anker, niet opnieuw satellietgecheckt) |
| — | via-punt, geen anker | Katima Mulilo-brug (Zambezi), grens Zambia/Namibië | -17.4717, 24.2499 | `koper-sentinel-walvisbay.md` §4 (b1 einde/b2 begin) | bron-gelegd (hergebruikt, Wikipedia "Katima Mulilo Bridge") |
| `co-walvisbay-kade` | overslag / kade (stoppunt, hergebruikt) | Walvis Bay-containerterminal, gereclameerd havenhoofd | -22.9500, 14.4860 | `koper-sentinel-walvisbay.md` §3 (`cu-walvisbay-kade`) | **bron-gelegd**, exacte bulkkade voor kobalthydroxide **aannemelijk** (hergebruikt satellietblik: containerstapels/portaalkranen op het havenhoofd; welke specifieke kade kobalt gebruikt is niet gebrond → open punt, zoals in de bronbrief) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Likasi (RN39 → RN1, hergebruikt) | -10.9806, 26.7355 | zelfde knooppunt als `koper-kolwezi-durban`/`kobalt-kisanfu-daressalaam`; sluit de RN1-westtak (Kolwezi) uit |
| b1 | 2 | Lubumbashi (RN1, hergebruikt) | -11.6642, 27.4827 | zelfde corridor als TFM/KCC/Kisanfu; pint de RN1 richting Kasumbalesa |
| b1 | 3 | **Kasumbalesa** — einde b1 (hergebruikt anker) | -12.2658, 27.7959 | verplichte grenspost DRC/Zambia |
| b2 | 1 | Chililabombwe (T3) | -12.3667, 27.8278 | ligt op de T3, 17 km zuid van Kasumbalesa [6]; sluit geen alternatief uit — enige doorgaande weg vanaf de grens |
| b2 | 2 | Chingola (T3 → T5) | -12.5475, 27.8600 | wisselpunt van de T3 (naar Kitwe/Ndola/Durban) op de T5 (naar Solwezi); pint de westelijke afslag i.p.v. de zuidelijke Durban-route [6][7][9] |
| b2 | 3 | **Solwezi** — einde b2 (T5, provinciehoofdstad) | -12.1433, 26.3858 | einde van de T5 hier gebruikt als aansluiting op het WCL-Trans-Caprivi-tracé richting Mutanda(ZM); eigen live Wikipedia-coordinates-query (correctie op de afgeronde -12.1833 uit `koper-sentinel-walvisbay` §4) [8] |
| b3 | 1 | Mutanda (Zambia) — start WCL-tracé (hergebruikt) | -12.4000, 26.2400 | zelfde punt als `koper-sentinel-walvisbay` §4; sluit de directe Solwezi–Chingola-route (naar Kasumbalesa/Durban) al uit bij b2 |
| b3 | 2 | Kasempa (hergebruikt) | -13.4550, 25.8350 | WCL-tracé, president Hichilema noemt Kasempa expliciet [4] |
| b3 | 3 | Kaoma (hergebruikt) | -14.8000, 24.8000 | WCL-tracé; splitst van de Mongu-noordroute af |
| b3 | 4 | Mongu (hergebruikt) | -15.2775, 23.1319 | WCL-tracé, provinciehoofdstad Western Province — bij het bakken van `koper-sentinel-walvisbay` bleek dit punt 294 m van de doorgaande M10-weg te liggen; hergebruik de gecorrigeerde routeercoördinaat (23,1344278/-15,2764746) uit die bake, niet deze Wikipedia-centroïde |
| b3 | 5 | Senanga (hergebruikt) | -16.1167, 23.2667 | WCL-tracé, laatste grote plaats vóór de Zambezi-vlakte |
| b3 | 6 | Sesheke (hergebruikt) | -17.4667, 24.3000 | Zambiaanse grensstad; sluit de oostelijkere Livingstone/Kazungula-route uit |
| b3 | 7 | **Katima Mulilo-brug** — einde b3 (hergebruikt) | -17.4717, 24.2499 | verplichte grenspost Zambia/Namibië |
| b4 | 1 | Rundu (B8, hergebruikt) | -17.9170, 19.7670 | eerste grote Namibische stad op de B8 |
| b4 | 2 | Otavi (B8→B1, hergebruikt) | -19.6642, 17.3306 | wisselpunt B8 op de B1 |
| b4 | 3 | Otjiwarongo (B1, hergebruikt) | -20.4642, 16.6528 | vaste tussenstop op de corridor naar Karibib |
| b4 | 4 | Karibib (B1→B2, hergebruikt) | -21.9381, 15.8544 | wisselpunt B1 op de B2 richting Walvis Bay |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mutanda-mijn SX-EW/hydroxide-plant (bij de mijn, geen apart been) | Glencore (100%) | koper-kobalterts → kobalthydroxide (+ koperkathode) | ≈8 kt Co (2024) [2]; **2026-exportquotum 6.700 t Co**, Q1-2026-productie −39% j-o-j, boven-quotum materiaal binnenlands opgeslagen [10][11] | [1][2][10][11] |

## 6 · Stoppunt
De brief stopt bij de Walvis Bay-kade (`co-walvisbay-kade`): geen bron noemt een overzeese afnemer of
vervolgbestemming voor dit specifieke volume, exact zoals bij `koper-sentinel-walvisbay.md` §6 — Walvis Bay is
voor Copperbelt-koper/kobalt "een derde uitgang" naast Durban en Lobito, niet gekoppeld aan een benoemde smelter.

## 7 · Open punten
- **Geen bron bevestigt dat kobalthydroxide van Mutanda specifiek over déze corridor gaat.** De bronnen tonen
  alleen dat de Walvis Bay-Ndola-Lubumbashi Development Road een officiële, actief geüpgradede corridor is voor
  Copperbelt-koper/kobalt [3][4], en dat Copperbelt-vrachtverkeer sinds 2026 verdeeld is over meerdere havens i.p.v.
  uitsluitend Durban [5]. Het aandeel via Walvis Bay is niet gekwantificeerd.
- **DRC-exportquotum 2026 verkleint en onregelmatigt het beschikbare volume.** Mutanda's 2026-quotum is 6.700 t Co
  (tegen het 2024-cijfer van 8 kt uit het ontwerp); Glencore's Q1-2026-eigen productie viel −39% j-o-j en
  boven-quotum materiaal wordt binnenlands opgeslagen in plaats van geëxporteerd [10][11] — het actuele
  exportvolume via elke corridor (dus ook Walvis Bay) is kleiner en onregelmatiger dan de ontwerp-aanname.
- **Mutanda-mijncoördinaat is dit seizoen alleen via de sitelaag satelliet-gecheckt**, nog niet met een eigen
  `sat_check.py`-run onder het stroom-id-prefix van déze keten (bakhandleiding §0.2) — bij het bakken nog te doen.
- **Exacte Walvis Bay-kade voor kobalthydroxide** (container- vs. bulkterminal) is niet gebrond — zelfde open punt
  als in `koper-sentinel-walvisbay.md` §7; het anker staat op de containerterminal (grootste, meest zichtbare
  kade).
- **Kasumbalesa→Chililabombwe→Chingola-verbindingsstuk is nu bevestigd als reëel (T3-weg [6]), niet meer een eigen
  constructie zonder bron** — de haalbaarheidstoets vroeg hier expliciet om verificatie; die verificatie is in
  deze brief gedaan. Bij het bakken nog te controleren: de wegklasse van dit stuk (mogelijk tertiary/unclassified,
  net als bij andere Copperbelt-grenstrajecten).

## 8 · Bronnen
[1] Wikipedia, "Mutanda Mine" (open-pit koper-kobaltmijn, Lualaba, DRC; grootste kobaltmijn ter wereld; Glencore 100%), https://en.wikipedia.org/wiki/Mutanda_Mine
[2] Cobalt Institute, Cobalt Market Report 2024 — Mutanda 8 kt Co (2024), zoals reeds gebruikt in `v2/design/kobalt-sitelaag.json` (`w-mutanda`), https://cobaltinstitute.org/
[3] Wikipedia, "Walvis Bay-Ndola-Lubumbashi Development Road" (voorheen Trans-Caprivi Highway/Corridor; volledige routebeschrijving incl. B2/B1/B8 en Zambiaanse M10/T1/T2/T3), https://en.wikipedia.org/wiki/Walvis_Bay-Ndola-Lubumbashi_Development_Road
[4] Infrastructure News, "Fastest Trade Route to Walvis Bay Port Launched by Western Corridor Limited in Zambia" (371 km Mutanda–Kasempa–Kaoma–Mongu–Senanga–Sesheke–Katima Mulilo, citaat president Hichilema), 2025-11-25, https://infrastructurenews.co.za/2025/11/25/fastest-trade-route-to-walvis-bay-port-launched-by-western-corridor-limited-in-zambia/
[5] Freight News, "Copper volumes prompt route diversification" (Copperbelt-vracht nu verdeeld over Dar es Salaam, Walvis Bay, Beira en Durban i.p.v. uitsluitend Durban), 2026-09-03, https://www.freightnews.co.za/article/copper-volumes-prompt-route-diversification-0
[6] Wikipedia, "Chililabombwe" ("de stad ligt op de T3-weg, 20 km ten noorden van Chingola en ongeveer 17 km ten zuiden van de grote grensmarkt Kasumbalesa"), geraadpleegd via Wikipedia-API 2026-09-28, https://en.wikipedia.org/wiki/Chililabombwe
[7] Wikipedia, "T5 road (Zambia)" ("verbindt Chingola in Copperbelt Province met Solwezi en Mwinilunga in North-Western Province"), geraadpleegd via Wikipedia-API 2026-09-28, https://en.wikipedia.org/wiki/T5_road_(Zambia)
[8] Wikipedia, "Solwezi" (coordinates via Wikipedia-API, geraadpleegd 2026-09-28: -12,14333/26,38583), https://en.wikipedia.org/wiki/Solwezi
[9] OpenStreetMap via Nominatim (ODbL) — node-coördinaat Chingola (osm_id 435533865, -12,54749/27,86004), geraadpleegd 2026-09-28, https://nominatim.openstreetmap.org
[10] Kitco News, "Glencore expects DRC cobalt exports to normalize in line with 2026 quotas" (Q1-2026-cobaltproductie −39% j-o-j, 5.800 t; Glencore-quotum 2026 22.800 t gesplitst KCC/Mutanda), 2026-04-30, https://www.kitco.com/news/off-the-wire/2026-04-30/glencore-expects-drc-cobalt-exports-normalize-line-2026-quotas
[11] Discovery Alert, "Glencore DRC Cobalt Export Quotas & Price Impact" (DRC-nationaal quotum 2026 ≈96.600 t; Mutanda-individueel quotum 6.700 t, KCC 16.100 t), 2026-04-30, https://discoveryalert.com.au/glencore-drc-cobalt-export-quotas-price-rally-2026/
[12] `koper-sentinel-walvisbay.md` — hergebruikte via-punten/geometrie/ankers §3/§4, gemeten km §9 (b1-subtraject Solwezi→grens, b2 letterlijke kopie)
[13] `koper-kolwezi-durban.md` — hergebruikte via-punten Likasi/Lubumbashi/Kasumbalesa §3/§4
[14] `kobalt-kisanfu-daressalaam.md` — precedent voor `co-kasumbalesa-grens`-hergebruik en de hemelsbreed-schattingsmethode voor been b1 (identieke via-puntenset Likasi/Lubumbashi, ~290 km)
[15] `v2/design/kobalt-sitelaag.json` (`w-mutanda`) — hergebruikt anker Mutanda-mijn, bron-gelegd (satelliet z15, eerder seizoen)

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Vier benen, alle truck, geen zee-been — 2.891,9 km · 17.167 punten · 4 markers.**

| # | modaliteit | km | naad met vorige | toelichting |
|---|---|---|---|---|
| b1 | truck | 355,1 | 0,00 km (start) | Mutanda-mijn → Likasi → Lubumbashi → Kasumbalesa-grens |
| b2 | truck | 213,1 | 0,00 km | Kasumbalesa-grens → Chililabombwe → Chingola → Solwezi |
| b3 | truck | 902,1 | 0,00 km | Solwezi → Mutanda(ZM) → Kasempa → Kaoma → Mongu → Senanga → Sesheke → grens Katima Mulilo |
| b4 | truck | 1.421,6 | 0,00 km | grens Katima Mulilo → Rundu → Otavi → Otjiwarongo → Karibib → Walvis Bay-kade |

**Recept:** `v2/tools/bak_stromen.sh` functie `bak_kobalt_mutanda_walvisbay()`; profielen
`kobalt-mutanda-walvisbay-mutanda-kasumbalesa` / `-kasumbalesa-solwezi` / `-solwezi-katimamulilo` in
`v2/tools/maak_stroombeen_weg.py` (b1–b3, extracts `congo-drc`/`zambia`/`zambia`); b4 is een
**letterlijke kopie** van `v2/build-cache/ais/graaf/koper-sentinel-walvisbay-weg-katimamulilo-walvisbay.geojson`
(functie `bak_koper_sentinel_walvisbay`, been b2) — geen nieuwe scan.

**Toelichting per been:**
- **b1 — bevinding op de km-toets, geen stippel.** Gemeten weggeometrie **354,8 km** tegen de eigen
  hemelsbreed-schatting van ~290,0 km uit §2 (**+22,3%**, buiten zowel ±15% als ±10%). De brief geeft hier
  géén gepubliceerde wegkm, dus de norm is indicatief (bakhandleiding §5.1) — geen via-punt bijgeschoven om
  het getal te halen. 24 keerlussen gesnoeid (354.8 → 354.8 km netto, dubbel gereden stukken bij Likasi/
  Lubumbashi). Ankersnap Mutanda-mijn 0,29 km (plant → weg), Kasumbalesa-grens 0,00 km — beide binnen de norm.
- **b2 — +7,5% tegen de hemelsbreed-schatting ~198,4 km, binnen de indicatie.** T3 (Kasumbalesa→Chililabombwe→
  Chingola) en T5 (Chingola→Solwezi) bevestigen zich als bevaarbare doorgaande wegen (`corridorKlassen`
  tertiary/unclassified nodig). 22 keerlussen gesnoeid, waarvan één grote bij Chingola (171 punten, 8,56 km
  dubbel gereden — wisselpunt T3↔T5).
- **b3 — -0,4% tegen het hergebruikte gemeten cijfer 906,3 km uit `koper-sentinel-walvisbay` §9.** Reproduceert
  dat cijfer (902,1 km) vrijwel exact met een ander beginpunt (Solwezi i.p.v. Sentinel-mijn, verder identiek
  via-puntentracé). Mongu gebruikt de daar GECORRIGEERDE routeercoördinaat (23,1344278/-15,2764746) — snapt op
  0,00 km, bevestigt dat de correctie ook vanaf dit beginpunt houdt (de Wikipedia-centroïde zou opnieuw op de
  geïsoleerde graafcomponent zijn geland).
- **b4 — letterlijke kopie, geen herbake.** 1.421,6 km / 6.590 punten, byte-identiek aan het bronbestand van
  `koper-sentinel-walvisbay`. Snap-kwaliteit dus identiek aan die eerder gevalideerde stroom.
- **Geen stippels nodig:** alle vier benen zijn reële, bevestigde doorgaande wegen; geen enkel anker of
  via-punt viel buiten het net.
- **Sat-check bij het bakken:** Mutanda-mijn kreeg deze golf zijn **eigen `sat_check.py`-run onder het
  stroom-id-prefix** (`v2/build-cache/satcheck/sat-kobalt-mutanda-walvisbay-co-mutanda-laad.png`, z15,
  0,005°-grid): het kruis valt in de open put, met de SX-EW-plant direct zuidwestelijk zichtbaar — bevestigt
  het hergebruikte sitelaag-anker (`w-mutanda`). Bakhandleiding §0.2-open punt hiermee gesloten.

**Toets (bakhandleiding §5):**
- Km per been ±15%/±10%-norm: b1 buiten norm (bevinding, indicatief — zie hierboven), b2/b3 binnen norm, b4
  = letterlijke kopie (geen eigen toets).
- Naden: alle 4 op 0,00 km — geen enkele > 5 km.
- Markers: alle 4 op 0,0 m van hun lijn (elk marker is zelf een anker/routeerpunt op een been-uiteinde).
- `toets_knikken.py`: 88 knikken ≥ 60°, waarvan 1 omkering ≥ 150° en **0 terugloop** (de enige die
  reparatie zou vragen) — alle scherpe bochten zijn echte weg-spikes (OSM-precisie), geen router-artefact.
- `toets_rechte_benen.py --min-km 5`: geen treffers voor deze stroom (geen been met omwegfactor 1,000 dat
  niet al een stippel is).
- Contract: `versie: 2`, `punt_formaat: lonlat`, alle modaliteiten `truck` (geldig), elk been ≥ 2 punten.
- ⚠️ Bestandsgrootte **350,1 KB**, boven de indicatieve ~300 KB-richtlijn uit bakhandleiding §5.3 — verklaard
  door vier lange benen (17.167 punten totaal, waarvan 6.590 uit de gekopieerde b4); geen van de harde
  contracteisen faalt hierdoor.

**Lessen / open punten voor het vervolg:**
- De hemelsbreed-schatting van b1 (~290 km) bleek 22% te laag tegen de gemeten weggeometrie — dezelfde
  onderschatting-richting als bij een corridor met bochten/omwegen die een rechte lijn niet vangt; voor een
  volgende stroom zonder gepubliceerde wegkm is een ruimere marge (bijv. ±25-30% i.p.v. ±15%) realistischer
  als eerste indicatie.
- De overige open punten uit §7 van deze brief (geen bron bevestigt het exacte aandeel via Walvis Bay i.p.v.
  Durban/Dar es Salaam/Kasumbalesa; het DRC-exportquotum 2026 verkleint het beschikbare volume; de exacte
  Walvis Bay-kade voor kobalthydroxide is aannemelijk, niet gebrond) blijven onveranderd staan — dit is
  geometrie-werk, geen brongeschil.
