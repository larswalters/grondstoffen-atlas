# Routebrief (licht) · goud — Macraes → Christchurch → Perth Mint (Nieuw-Zeeland → Australië)

**stroom-id:** `goud-macraes-perthmint` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** doré van de Macraes-verwerkingsplant (OceanaGold, Otago, Nieuw-Zeeland) gaat per **truck** over Macraes Road, SH85 en SH1 (334–339 km) naar het vrachtcluster van Christchurch Airport (CHC), vliegt als **vrachtvlucht** (grootcirkel, aannemelijk) naar de vrachtterminal van Perth Airport (PER) en gaat per **truck** (Tonkin Hwy / Great Eastern Hwy, 14,9 km) naar de raffinaderij van The Perth Mint, East Perth.
**Welke as van het verhaal:** *Tasman-doré naar de Perth Mint* — Macraes is de grootste goudmijn van Nieuw-Zeeland; het contract met de Perth Mint is gebronnd (TRS par 19.2). Volume: **4,6 t Au/j** (147 koz in 2025 ÷ 32,15; peiljaar 2025) [1].

## BINDENDE aanpassing op het ketenontwerp (haalbaarheidstoets), en wat ik daarvan afweek
Christchurch (CHC) i.p.v. Dunedin; b1 truck Macraes → CHC; b2 stippel last mile CHC; b3 lucht CHC → PER; b4 omgekeerde kopie van `goud-kalgoorlie-singapore` b2. Verwerkt. Twee kanttekeningen: (1) Dunedin Airport heeft volgens Wikipedia sinds 24-06-2025 weer internationale vluchten (Jetstar Gold Coast); de reden in de toets klopt dus niet meer, maar er is geen vrachtverkeer gevonden, dus CHC blijft [9]. (2) Het mijnanker uit de toets (-45.3762, 170.4504, Wikipedia) ligt in de put; de plant ligt 3,2 km NW daarvan (§3) en het TRS-punt (-45.36, 170.43) valt op de plant.

## 1 · Ketenkaart
```
Macraes-plant `au-macraes-plant` ──(b1 truck · Macraes Rd → SH85 → SH1 · OSRM 339 km, hemelsbreed 267 km, geen wegkm)──►
Air NZ Cargo, Ron Guthrey Rd, CHC `au-chc-cargo` ──(b2 stippel · last mile airside · 0,2 km)──►
CHC-platform (Perimeter Rd) `au-chc-platform`
   ──(b3 lucht · vlucht CHC → PER, grootcirkel, aannemelijk · 5.038 km)──►
Perth Airport vrachtterminal `au-per-cargo` (hergebruikt)
   ──(b4 truck · Tonkin Hwy → Great Eastern Hwy · 14,9 km, kopie omgekeerd)──►
The Perth Mint, East Perth `au-ref-perth` (hergebruikt) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Macraes-plant → Air NZ Cargo (CHC) | Golden Point Rd / Macraes Rd → Dunback → SH85 → Palmerston → SH1 (Oamaru, Waitaki, Timaru, Ashburton, Rakaia) → Pound Rd; aannemelijk, vervoer niet gebronnd | OSRM 338,8 [7]; hemelsbreed 267,1 — geen wegkm gepubliceerd, ±15% = indicatie | maak_stroombeen_weg (nieuw-zeeland) | nee |
| b2 | A | truck | Air NZ Cargo → CHC-platform | last mile airside | 0,22 hemelsbreed | `--stippel` | ja — "last mile (airside/privéterrein, geen net op deze korrel)" |
| b3 | B | lucht | CHC → PER | vlucht CHC → PER (aannemelijk: geen directe vrachtvlucht gevonden) | 5.037,7 grootcirkel (berekend) | maak_luchtbeen | nee — doorgetrokken |
| b4 | C | truck | PER-vrachtterminal → Perth Mint | Tonkin Hwy → Great Eastern Hwy | 14,9 gemeten in `goud-kalgoorlie-singapore` b2 [11] | LETTERLIJKE KOPIE, omgekeerd | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-macraes-plant` | verwerkingsplant / doré-smelt | OceanaGold Macraes-verwerkingsplant (autoclaaf, CIL, smelterij) | -45.3592, 170.4290 | [1] punt -45.36/170.43; [5] OSM landuse "OceanaGold Processing Plant" | bron-gelegd (z16 gezien: compact gebouwen- en tankencluster met pijpen, aan de pitrand, tailings-terrassen ten zuiden; `sat-goud-macraes-perthmint-plant-osm.png`) |
| `au-chc-cargo` | vrachtloods (truck eindigt hier) | Air New Zealand Cargo, Ron Guthrey Road, Christchurch Airport | -43.4926, 172.5467 | [10] OSM building warehouse met naam | aannemelijk (z16 gezien: loodsencluster in het zakelijke terrein ten ZO van de terminal; de naam komt alleen uit OSM; `sat-goud-macraes-perthmint-chc-airnzcargo.png`) |
| `au-chc-platform` | platform / vertrek lucht | CHC Customs/Cargo Inspection, Perimeter Road | -43.4918, 172.5442 | [10] OSM building government | aannemelijk (z16 gezien: gebouwen aan de platformrand met geparkeerde toestellen op ~400 m W; `sat-goud-macraes-perthmint-chc-apron.png`; welk gebouw de goudvracht afhandelt is niet gebronnd) |
| `au-per-cargo` | vrachtterminal PER | Qantas Freight Int'l Terminal, Affleck Road, Ascot | -31.9460, 115.9764 | hergebruikt uit `goud-kalgoorlie-singapore.md` §3 [11] | bron-gelegd (z17 daar) |
| `au-ref-perth` | raffinaderij | The Perth Mint, 310 Hay Street, East Perth | -31.9550, 115.8700 | hergebruikt uit `goud-kalgoorlie-singapore.md` §3 [11][14] | bron-gelegd (z15 daar) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Alle punten zijn wegpunten uit de OSRM-route [7] (maneuver-locaties op OSM-wegen), geen plaatsnamen-centroïden; geen enkel punt ligt in een stadscentrum.
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Dunback, begin SH85 | -45.3843, 170.6288 | Macraes Rd eindigt op SH85; pint de keuze oostwaarts naar Palmerston, niet westwaarts (Middlemarch) of naar Dunedin |
| b1 | 2 | Palmerston, SH85/SH1 | -45.4809, 170.7220 | op SH1; sluit de zuidelijke Dunedin-route uit |
| b1 | 3 | Pukeuri, ten N van Oamaru | -45.0619, 170.9997 | SH1 buiten het centrum van Oamaru |
| b1 | 4 | Waitaki-rivier, SH1 | -44.9135, 171.1006 | SH1 over de Waitaki-brug bij Glenavy |
| b1 | 5 | Timaru-noord, SH1 | -44.3463, 171.2369 | SH1 ten N van Timaru |
| b1 | 6 | Hinds, ten Z van Ashburton | -43.9969, 171.5787 | SH1 op de Canterbury Plains |
| b1 | 7 | Dunsandel / Rakaia-zijde | -43.7517, 172.0286 | SH1 Main South Road |
| b1 | 8 | Templeton, SH1 | -43.6016, 172.3511 | afslag richting Pound Rd naar de luchthaven |
b3, b4: geen via-punten (grootcirkel; b4 is een kopie).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Macraes-plant | OceanaGold | sulfide-erts → doré (Au + Ag) | 6,4 Mt erts/j; 147 koz Au in 2025 | [1] |
| The Perth Mint | overheid West-Australië | doré → LBMA-baren | ~300–400 t Au/j totaal, ook NZ-aanvoer | [11] §5, [12] |

## 6 · Stoppunt
De brief stopt bij de Perth Mint: het eindproduct (LBMA-baar) ontstaat daar; fase D/E vervalt (geen bron die deze doré aan één afnemer koppelt).

## 7 · Open punten
- **Geen bron noemt het vervoer** (modaliteit, luchthaven, vlucht): TRS zegt alleen "shipped to an Australian refinery" [1]; de pers noemt een bewaakte route over de Tasmanzee zonder details [2]. De hele b1–b3-keuze is aannemelijk, niet gebronnd.
- **CHC als luchthaven** is een keuze uit afwegen (Dunedin is geen vrachtluchthaven in de bronnen); CHC heeft vracht naar Sydney, Melbourne, Brisbane (o.a. Qantas Freight) maar **geen gevonden directe vracht naar Perth**; Air NZ vliegt passagiers CHC-PER seizoensgebonden (hervat 30-11-2026) [8]. In de praktijk loopt de lading waarschijnlijk via Sydney of Melbourne; getekend is één vlucht.
- `au-chc-cargo` en `au-chc-platform`: naam alleen uit OSM; welke loods de goudvracht afhandelt is niet gebronnd.
- **Perth Mint-anker:** `au-ref-perth` is in `goud-sitelaag.json` nog "onzeker" (centrum-kruising), in de kalgoorlie-brief "bron-gelegd" op het Hay Street-gebouw; ik hergebruik de brief. Sitelaag niet aangeraakt, melding voor centraal.
- Sitelaag kent geen Nieuw-Zeeland-site; Macraes-plant (`au-macraes-plant`) is kandidaat.
- b1 km is OSRM, geen gepubliceerde wegkm; de plant ligt in een mijnterrein (Golden Point Road is mijnweg: zie bak-aanwijzingen).
- Aandeel doré dat in 2025 echt naar de Perth Mint ging is niet gepubliceerd; 4,6 t is de totale Macraes-productie.

## 8 · Bronnen
[1] OceanaGold, Macraes NI 43-101 TRS 27-03-2026 (par 1: locatie -45,36/170,43, 6,4 Mtpa; 5.1: Palmerston 37 km; 19.2 Perth Mint-contract; 2025 = 147 koz). https://www.sec.gov/Archives/edgar/data/1487326/000162828026021651/exhibit9962-40xf.htm
[2] Money.it, 29-07-2026: 17 kg-baar (zes-miljoenste ounce van Macraes) naar de Perth Mint. https://www.money.it/nuova-zelanda-estratto-lingotto-oro-3-milioni-dollari-perche-lascia-paese
[3] Vozpopuli (alleen zoekfragment gelezen): Macraes-doré naar de Perth Mint, vervoerdetails geheim. https://www.vozpopuli.com/indux/un-lingote-de-oro-de-17-kilos-valorado-en-38-millones-sale-de-nueva-zelanda-bajo-maxima-seguridad-tras-un-hito-en-su-mayor-mina/4035/
[4] Wikipedia, Macraes Mine (-45.3762/170.4504, piektijd). https://en.wikipedia.org/wiki/Macraes_Mine
[5] OpenStreetMap way 1063770256 "OceanaGold Processing Plant" (landuse industrial, ODbL). https://www.openstreetmap.org/way/1063770256
[6] Esri World Imagery via `v2/tools/sat_check.py`: `sat-goud-macraes-perthmint-plant-a.png`, `-plant-osm.png`, `-chc-cargo.png`, `-chc-airnzcargo.png`, `-chc-apron.png` in `v2/build-cache/satcheck/`.
[7] OSRM (router.project-osrm.org), 31-10-2026: plant -> Air NZ Cargo 338,8 km, 4,9 uur; mijnpunt -> CHC 334,3 km. Maneuver-locaties als via-punten.
[8] Wikipedia, Christchurch Airport (vrachtmaatschappijen, Air NZ CHC-PER). https://en.wikipedia.org/wiki/Christchurch_Airport
[9] Wikipedia, Dunedin Airport (internationale vluchten weer sinds 24-06-2025; geen vracht vermeld). https://en.wikipedia.org/wiki/Dunedin_Airport
[10] OSM via Photon (komoot): Air New Zealand Cargo, Ron Guthrey Road (-43.4926/172.5467); Customs/Cargo Inspection, Perimeter Road (-43.4918/172.5442); Emirates SkyCargo (-43.4934/172.5451).
[11] `v2/design/routebrieven/goud-kalgoorlie-singapore.md` (§3 ankers, b2 14,9 km, §5, [7]) en `v2/data/stroomroute-goud-kalgoorlie-singapore.json`.
[12] The Perth Mint, refinery (via [11][7]). https://www.perthmint.com/refinery-treasury/refinery/
[13] Ketenontwerp en haalbaarheidstoets goud-macraes-perthmint (orchestrator, M31 golf 19).
[14] Wikipedia, Perth Mint (310 Hay Street). https://en.wikipedia.org/wiki/Perth_Mint

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
`bash v2/tools/bak_stromen.sh goud-macraes-perthmint` → `v2/data/stroomroute-goud-macraes-perthmint.json` (111,8 KB, versie 2, lonlat): **4 benen · 5.390,4 km · 5.170 punten · 5 markers**, alle naden 0,000 km, alle markers 0,000 km van de lijn.

| # | modaliteit | km | geometrie |
|---|---|---|---|
| b1 | truck | 337,6 | profiel `goud-macraes-perthmint-macraes-chc` (nieuw-zeeland, refs SH85/SH1, venster 40, eindToegangPrivaat); 4.508 punten; lengtetoets -0,5% tegen OSRM 338,8 (geen wegkm, dus indicatie) |
| b2 | truck, stippel | 0,22 | `--stippel`, last mile airside CHC (geen net op deze korrel) |
| b3 | lucht | 5.037,7 | `maak_luchtbeen.py` CHC platform → PER Qantas Freight, doorgetrokken, 203 punten |
| b4 | truck | 14,9 | letterlijke kopie omgekeerd van `goud-kalgoorlie-singapore-weg-perth-percargo.geojson` (457 punten) |

**Recept.** b1: wegscan via `wegscan_puur.py` (90 s scan, 8 via-punten uit §4, plant → SH85 → SH1 → Pound Rd, geen via-snap boven 0,02 km; first mile 4,1 km en last mile 1,3 km over service/unclassified). b2: stippel. b3: grootcirkel. b4: kopie met omgekeerde volgorde (id en naam aangepast, geometrie ongewijzigd). Geen zee, geen haven-aanloop, geen leiding.

**Stippel.** Alleen b2 (0,22 km): het Air NZ Cargo-cluster en het platform liggen airside, er is geen openbare weg ertussen.

**Vlucht.** b3 is een grootcirkel tussen twee vrachtplatforms en dus geen gat. Er is geen directe vracht CHC-PER gevonden (§7); de lading loopt waarschijnlijk via Sydney of Melbourne. Getekend is een enkele vlucht, aannemelijk, niet gebronnd.

**Toetsen.** `toets_knikken.py`: 35 knikken ≥ 60 graden (alle korte spikes van 4–26 m op ankers en kruispunten), 0 omkeringen, 0 terugloop. De wegbenen zijn niet recht (omwegfactor b1 1,26 tegen hemelsbreed 267 km).

**Lessen.** (1) NZ-extract (400 MB) scant in 90 s en snapt alle 8 via-punten op 0,00–0,02 km; de OSRM-maneuverpunten uit de brief werkten zonder bijsturen. (2) `refs` mag SH85/SH1 heten: de ref-voorkeur is zacht en de lengte kwam op -0,5%. (3) Sitelaag: `au-ref-perth` staat nog als onzeker en geen NZ-site; `au-macraes-plant` is kandidaat (centraal).
