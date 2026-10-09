# Routebrief (licht) · Goud · MKS PAMP (Ticino) → Zürich (ZRH) → JFK (New York, VS)

**stroom-id:** `goud-pamp-newyork` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken
**Keten in één zin:** LBMA-baar-goud (kilo- en 100-oz-baren, COMEX-formaat) van de MKS PAMP-raffinaderij in Castel San Pietro
(Ticino) per **truck** over de Gotthard-as (A2/A4) naar het vrachtplatform van Zürich Airport (ZRH), per **vrachtvlucht**
(grootcirkel) naar de vrachtterminal van JFK (New York). Eindpunt = JFK-vrachtterminal: geen bron noemt een COMEX-kluisadres.
**Welke as van het verhaal:** Zwitserland → VS/COMEX, de tariefangst-aanvoer van dec 2024–mrt 2025: **193 t Au in jan 2025** en
**476 t in H1 2025** uit heel Zwitserland (vrijwel alles in Q1), daarna 0,3 t in aug 2025 [1][2][5]. Markt-as, niet per
raffinaderij gebrond; PAMP wordt alleen als Zwitsers huis genoemd [3]. Een uitschieter, geen structurele handelsroute.

## 1 · Ketenkaart
```
MKS PAMP-raffinaderij `au-pamp-raffinaderij`
  ──(b1 truck · A2 Gotthard → A14/A4 Knonaueramt → A1 · 263,3 km gebakken, kopie van goud-pamp-shanghai b1)──►
Zürich Airport vrachtplatform `au-zrh-vrachtterminal`   (b2: 0,9 km stippel last mile airside, kopie goud-pamp-shanghai b2)
  ──(b3 lucht · vlucht ZRH → JFK, grootcirkel, aannemelijk · 6.309,3 km)──►
JFK South Cargo Area `au-jfk-vrachtterminal` ── stoppunt (COMEX-kluis niet gebrond)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | MKS PAMP → ZRH-vrachtplatform (openbare weg) | A2 (Mendrisio–Bellinzona–Gotthard–Erstfeld) → A14 → A4 Knonaueramt → A1 | **hemelsbreed 182,3 km, geen wegkm**; gebakken 263,3 (OSM-weg, +44% op hemelsbreed: indicatie, geen norm) | **LETTERLIJKE KOPIE** `goud-pamp-shanghai-weg-pamp-zrh.geojson` (= b1 van `goud-pamp-shanghai`) | nee |
| b2 | D | truck | openbare weg (47.472087, 8.554523) → ZRH-vrachtplatform | eigen terrein, airside | 0,9 [berekend] | **LETTERLIJKE KOPIE** van de `--stippel`-regel in `bak_goud_pamp_shanghai` (b2) | **ja** — airside/privéterrein, geen wegpad |
| b3 | D | lucht | ZRH-vrachtplatform → JFK South Cargo Area | vrachtvlucht ZRH → JFK, grootcirkel | 6.309,3 [berekend, `maak_luchtbeen`] | `goud-pamp-newyork-lucht-zrh-jfk.geojson` (254 punten, FeatureCollection, al gemaakt) | nee — doorgetrokken; **aannemelijk: markt-as, niet per raffinaderij of vlucht gebrond** |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-pamp-raffinaderij` | raffinaderij / vertrek | MKS PAMP SA, Via alle Zocche 1, Castel San Pietro | 45.8546, 9.0025 | [7] | **hergebruikt letterlijk** uit `goud-pamp-shanghai.md`: bron-gelegd (daar z16–z17 gezien: industrieel complex met proceshallen en zonnepanelendak op het handelsregisteradres) |
| `au-zrh-vrachtterminal` | overslag truck → lucht | Zürich Airport vrachtplatform | 47.4647, 8.5492 | [7] | **hergebruikt letterlijk**; eigen z16-blik: kruis op een klein verhard platform met één gebouwtje aan het noordeinde van de apron, een passagierspier met wide-bodies direct ZO — geen duidelijke vrachtloods → **aannemelijk, pand onzeker** (zie §7) |
| `au-jfk-vrachtterminal` | overslag lucht → eind | JFK South Cargo Area (Cargo Plaza/South Cargo Road), Queens | 40.6587, -73.7952 | [8] | **hergebruikt letterlijk** (= `dia-jfk-cargo` = `pgm-jfk-cargo`); eigen z16-blik: kruis op de strook lange vrachtloodsen langs de oostrand van een rolbaan, wide-body vrachttoestellen op het apron ervoor, South Cargo Road eronder → bron-gelegd |

## 4 · Via-punten (alleen b1; geen nieuwe scan — kopie van het profiel `goud-pamp-shanghai-pamp-zrh`)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Bellinzona (A2-knoop) | 46.1954, 9.0297 | A2 vóór de Gotthard-klim |
| b1 | 2 | Göschenen (noordportaal Gotthard) | 46.6676, 8.5887 | vaste doorgang, geen alternatieve vrachtcorridor |
| b1 | 3 | Erstfeld (Reuss-dal) | 46.8215, 8.6500 | A2 noordwaarts richting Luzern |
| b1 | 4 | Rotkreuz (A2/A4-knoop) | 47.1408, 8.4313 | hier buigt de route naar Zürich; **Zug bewust niet** (stad, +3 km omweg in de eerste bake) |
| b1 | 5 | openbare weg bij ZRH-vrachtplatform | 47.4721, 8.5545 | eindpunt van het wegbeen; platform zelf airside |
b2 en b3 hebben geen via-punten.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| MKS PAMP-raffinaderij | MKS PAMP SA | doré/schroot/oud goud → LBMA-baren; COMEX vraagt 100-oz of 1-kg baren, herverwerking in Zwitserland | v1: ≈450 t/j nameplate (`data/goud.js`) | [1][3][4][v1] |

## 6 · Stoppunt
De brief stopt bij de JFK-vrachtterminal: geen bron noemt een COMEX-kluisadres (bronnen noemen alleen "vaults near JFK" [4]; de CME-depotenlijst was onbereikbaar) en een kluisanker zou een verzonnen coördinaat zijn. Fase E vervalt.

## 7 · Open punten
- **Jaarvolume:** alleen Zwitserland-totaal → VS (193 t jan, 476 t H1 2025); **PAMP-aandeel niet gepubliceerd**, BAZG-maandreeks niet opgehaald. Peiljaar 2025 = uitschieter (tariefangst, daarna terugstroom na april en 0,3 t in aug na het CBP-schrijven van 31 juli [2][5]).
- **Vlucht ZRH → JFK niet per lading gebrond:** [3] noemt vliegtuigen met goud naar de VS (en terug), [4] vrachtruimen van passagiersvliegtuigen, [9] goud "vaak" tussen Londen/New York/Zürich/Hongkong/Shanghai; geen bron noemt PAMP, ZRH of een vlucht. Één directe vlucht aangenomen. Een vlucht kan ook via een andere Europese hub of Londen lopen.
- **Geen kluisadres** (HSBC 452 Fifth Avenue was een hoorzegen, niet gebrond); **geen last-mile-been JFK → kluis**.
- **ZRH-anker is een reuse met twijfel:** bij mijn eigen z16-blik ligt het kruis niet op een herkenbare vrachtloods. Photon vindt een Swissport-kantoor op Flughofstrasse (47.4395, 8.5647, ≈2,7 km ZZO) — niet beoordeeld. Het anker is in ≥10 brieven hergebruikt en is dus een centrale vraag, geen keten-specifieke; b2 (stippel) blijft letterlijk kopie.
- **b1 wegkm niet gebrond:** 263,3 is OSM-geometrie; eerdere notities noemen ~250 km zonder bron. De ±15%-toets geldt niet als norm.
- **Overlap:** b1+b2 zijn 100% kopie van `goud-pamp-shanghai`; alleen b3 is nieuw (andere eindmarkt). Niet-herhaling van valcambi-londen/argor-mumbai/metalor-istanbul.

## 8 · Bronnen
[1] swissinfo, 2025-02-20 — "Swiss gold exports to US surge to record on tariff fears": 193 t naar de VS in jan 2025 (record sinds 2012), 225 t totaal; COMEX eist 100-oz/kilobaren, Londense 400-oz-baren gaan eerst door Zwitserse raffinage. https://www.swissinfo.ch/eng/swiss-gold-exports-to-us-surge-to-record-on-tariff-fears/88906594
[2] swissinfo, 2025-08-08 — "US tariffs now also apply to Swiss gold bars": H1 2025 476 t / CHF 39 mld (Tamedia op Zwitserse douanecijfers); 1-kg-baar is de meest verhandelde COMEX-eenheid; CBP-brief 31 juli (39%). https://www.swissinfo.ch/eng/trade-policy/us-tariffs-now-also-apply-to-swiss-gold-bars/89802052
[3] Discovery Alert — "Switzerland gold market role 2025 exports": goud per vliegtuig naar de VS dec–mrt om COMEX-posities te dekken, terugvlucht na de uitzondering van april 2025; PAMP genoemd naast Valcambi, Argor-Heraeus, Metalor (geen aandeel). https://discoveryalert.com/news/switzerland-gold-market-role-2025-exports/
[4] Yahoo Finance, 2026-05-12 — "US gold exports surge 285%": herverwerkte baren per vliegtuig naar vaults "near JFK", New Yorkse kluisvoorraad ≈1.350 t; uitvoer via JFK in vrachtruimen van passagiersjets (richting Zürich). https://finance.yahoo.com/markets/commodities/articles/u-gold-exports-surge-285-105026639.html
[5] Kitco, 2025-09-19 — Zwitserse goudexport naar de VS −99% in aug 2025 (0,3 t); Q1 2025 record USD 36 mld. https://www.kitco.com/news/article/2025-09-19/swiss-gold-exports-us-fall-99-august-rise-353-china-after-tariff-shock
[6] Kitco/Reuters, 2025-08-08 — "Some gold players stop flying bars to US on tariff ruling uncertainty" (alleen kop gelezen): een grote Zwitserse raffinaderij pauzeert leveringen. https://www.kitco.com/news/off-the-wire/2025-08-08/some-gold-players-stop-flying-bars-us-tariff-ruling-uncertainty
[7] `v2/design/routebrieven/goud-pamp-shanghai.md` (b1, b2, ankers PAMP en ZRH) en `bak_goud_pamp_shanghai` in `v2/tools/bak_stromen.sh`.
[8] `v2/design/routebrieven/diamant-mumbai-newyork.md` en `pgm-amandelbult-iselin.md` — anker JFK South Cargo Area 40.6587/-73.7952 (OSM Cargo Plaza & Central Cargo Road).
[9] SupplyChainBrain (Bloomberg), 2025-02-03 — "Traders Load US-Bound Planes With Gold and Silver in Tariff Bet": goud in vrachtruimen van passagiersvliegtuigen, ≈14 Moz (≈435 t) naar COMEX-depots sinds de verkiezingsdag, COMEX-goud komt doorgaans van grote Zwitserse raffinaderijen; geen kluisadres. https://www.supplychainbrain.com/articles/41138-traders-load-us-bound-planes-with-gold-and-silver-in-tariff-bet
[v1] `data/goud.js`, `design/goud.md`. Satellietblik: `v2/build-cache/satcheck/sat-goud-pamp-newyork-jfk-cargo.png`, `sat-goud-pamp-newyork-zrh-cargo.png` (Esri z16, 2026-10-09). Hemelsbreed: haversine R 6371,0088.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Recept:** `bash v2/tools/bak_stromen.sh goud-pamp-newyork` (functie `bak_goud_pamp_newyork`). Geen wegscan, geen profiel, geen extract, geen haven-aanloop, geen zeebeen; alle drie de benen zijn vooraf gebakken geojson of een stippel-regel. Uitvoer `v2/data/stroomroute-goud-pamp-newyork.json` (119,2 KB, versie 2, lonlat).

| # | modaliteit | km | punten | stippel | naad naar vorige |
|---|---|---|---|---|---|
| b1 | truck | 263,3 | 6.154 | nee | — |
| b2 | truck | 0,9 | 2 | ja (airside) | 0,000 km |
| b3 | lucht | 6.309,3 | 254 | nee | 0,000 km |

Totaal **6.573,5 km**, 6.410 punten, 3 markers, naden 0 (maximum 0,000 km). De drie markers liggen 0,0 km van hun lijn.

- **b1** is een letterlijke kopie van `goud-pamp-shanghai-weg-pamp-zrh.geojson` (263,3 km, eindigt op de openbare weg 47.472087, 8.554523). De brief geeft geen echte wegkm, dus de ±15%-toets is hier een indicatie: 263,3 tegen hemelsbreed 182,3 km (+44%) over de Gotthard-as. `toets_knikken` meldt 29 knikken en 0 omkeringen op dit been: dezelfde als in goud-pamp-shanghai (kopie), niet nieuw.
- **b2** is een stippel (0,914 km): het ZRH-vrachtplatform ligt airside, zonder aansluiting op het openbare net. Letterlijke kopie van de stippel-regel van goud-pamp-shanghai b2. Stippel betekent hier uitsluitend: hier reikt het net niet.
- **b3** is de vlucht ZRH → JFK, grootcirkel 6.309,3 km (254 punten, `maak_luchtbeen.py`), doorgetrokken; "aannemelijk" staat in de beennaam, niet in de lijnstijl. Begin en eind liggen exact op de twee vrachtterminal-ankers.
- **Geen** haven-aanloop, leiding, spoor of zee in deze keten.

**Lessen:** (1) een gedeeld been uit een eerdere stroom is een kopie van het bestaande geojson, niet van de geometrie: dat levert naad 0 en een identiek km-getal op; (2) het ZRH-anker blijft een centrale vraag (zie §7), de kopie van b2 lost dat niet op; (3) het stroom-id noemt New York en het eindpunt is de JFK-vrachtterminal in Queens, dus id en eindpunt kloppen; geen afwijking van het ontwerp.
