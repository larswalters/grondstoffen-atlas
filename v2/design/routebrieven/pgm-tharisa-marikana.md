# Routebrief (licht) · PGM — Tharisa Mine → Marikana Road D1325 → Skierlik Road D314 → Marikana-smelter/BMR Sibanye (Zuid-Afrika)

**stroom-id:** `pgm-tharisa-marikana` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** PGM-concentraat (derde partij, bijproduct van chroom) van de Tharisa Mine bij Mooinooi/Marikana per **truck** over Marikana Road (D1325) en Skierlik Road (D314) oostwaarts naar het Marikana-smelter/BMR-complex van Sibanye-Stillwater (Wonderkop); stoppunt = smelter (verdere route: `pgm-marikana-brakpan`). **Aannemelijk: één bron** (de koper is bron-gelegd, het leveringspunt Marikana is aanname).
**Looptijd:** deze lijn stroomt nu nog maar **vervalt op 1-1-2027**: Valterra (Rustenburg Platinum Mines) vervangt Sibanye-Stillwater als koper van 50% van het Tharisa-concentraat [1][3]; de reeds gebakken `pgm-tharisa-waterval` neemt dan over (Northam houdt de andere 50%). Einddatum 31-12-2026 volgt uit "from 1 January 2027, replacing Sibanye" [1], geen bron noemt de datum letterlijk.
**Welke as van het verhaal:** de huidige Westelijke-Bushveld-concentraatruil: Tharisa verkoopt de helft van zijn PGM-concentraat aan Sibanye, dat derdenconcentraat in de eigen Marikana-smelter verwerkt. Volume: 153,7 koz 6E FY2026 = 4,78 t 6E/j [2]; de helft = **~2,4 t 6E/j** (mix 6E = Pt+Pd+Rh+Au+Ru+Ir; koz ÷ 32,15 = t; het aandeel is geen gemeten ritvolume).

## 1 · Ketenkaart
```
Tharisa Mine (plant) `pgm-tharisa-plant` ──(b1 truck · Marikana Rd D1325 → Skierlik Rd D314 ·
   OSRM-indicatie 9,4 km, hemelsbreed 6,7 km, geen wegkm · aannemelijk: één bron · tot 31-12-2026)──►
Marikana-smelter/BMR Sibanye `pgm-marikana-bmr` ── stoppunt (smelter; vervolg = pgm-marikana-brakpan)
```
Niet getekend: de andere 50% naar Northam (eigen keten `pgm-zondereinde-*`) en de Valterra-lijn vanaf 2027 (`pgm-tharisa-waterval`).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-tharisa-plant` → `pgm-marikana-bmr` | Marikana Road D1325 (tertiary, noordwaarts) → Skierlik Road D314 (oostwaarts); niet Karee Road D108 | hemelsbreed 6,7 km, geen wegkm; OSRM-indicatie 9,4 km [8] (geen norm; de ±15%-toets is een indicatie) | maak_stroombeen_weg | nee |

Beennaam voor de bak: "PGM-concentraat Tharisa Mine → Marikana Road D1325 → Skierlik Road D314 → Marikana-smelter/BMR Sibanye (aannemelijk: één bron; tot 31-12-2026)". Geen zee-, spoor-, lucht- of leidingbeen, geen haven-aanloop, geen fase D/E: de bron noemt alleen de koper.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-tharisa-plant` | mijn + verwerkingsplant / vertrek | Tharisa Mine Processing Plants (Genesis/Voyager), Mooinooi/Marikana — **hergebruikt letterlijk** uit `pgm-tharisa-waterval.md` | -25.7421, 27.4978 | [2][7][10] | bron-gelegd (z15 opnieuw gezien: plantcomplex met procesgebouwen en bezinkbekkens op het kruis, dagbouwpit direct noord, N4 ~1,1 km zuid) |
| `pgm-marikana-bmr` | smelter + BMR / losplek en stoppunt | Marikana smelter/BMR-complex (Western Platinum), Wonderkop — **hergebruikt letterlijk** uit `pgm-marikana-brakpan.md` | -25.6837, 27.5155 | [4][9][10] | bron-gelegd (z15 opnieuw gezien: lang ovenhal-complex met schoorstenen en opslag op het kruis, groot schakelstation ~0,7 km west, woonwijk noord) |

Het leveringspunt binnen het complex noemt geen bron; site-niveau, geen tweede anker. Het wegeinde snapt ~0,13 km van het anker (geen last-mile-been).

## 4 · Via-punten (in reisvolgorde, alle op de doorgaande weg, niet in een stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Kruising Marikana Road D1325 / Karee Road D108 | -25.6971, 27.4888 | pint de noordelijke uitgang op D1325 (uit de toets; Karee Road D108 gaat hier westwaarts weg) |
| b1 | 2 | D1325 / D314-knik | -25.6902, 27.4904 | pint de overgang van D1325 naar D314 in plaats van een zijtak of het dorp Marikana (-25.698, 27.472) |
| b1 | 3 | Skierlik Road D314 | -25.6904, 27.4951 | pint de oostelijke doorgaande weg naar het complex (OSRM-naamwissel D314 → Skierlik Road) |

Alle drie liggen op de OSRM-route; met deze via-punten 9,386 km, identiek aan de vrije route (9,386 km) [8]. Geofabrik-regio's: `zuid-afrika`. Voor het wegprofiel: `corridorKlassen ["tertiary","unclassified"]`, `refs ["D1325","D314"]`, `vensterKm` ~10, `gepubliceerdKm` 9 (indicatie), zoals `pgm-tharisa-waterval-tharisa-waterval`.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Tharisa Mine (concentrator, chroom + PGM) | Tharisa plc | reef (5,5 Mt gemalen FY2026) → PGM-concentraat (+ chroomconcentraat 1,56 Mt) | 153,7 koz 6E/j FY2026; guidance FY2027 150-170 koz | [2] |
| Marikana smelter | Sibanye-Stillwater (ex-Lonmin) | eigen en derdenconcentraat ("limited amounts for third parties") → converter-matte | ontwerp 13.133 t/mnd, gehaald 11.689 t/mnd (zie `pgm-marikana-brakpan`) | [4] |

## 6 · Stoppunt
De brief stopt bij de Marikana-smelter/BMR: dat is de verwerking van derdenconcentraat bij de huidige koper, en het vervolg (BMR → PMR Brakpan) is al `pgm-marikana-brakpan`, dus naad nul; geen bron noemt een aparte bestemming voor Tharisa-concentraat.

## 7 · Open punten
- **Leveringspunt aanname:** de 20-F noemt Marikana als smelter die "limited amounts for third parties" verwerkt, maar noemt Tharisa niet [4]; SENS, Mining-technology en BusinessDay noemen Sibanye als huidige koper, geen leveringsplaats [1][3][6][12]. Een Sibanye-percentage is niet gelezen: 50% volgt alleen uit "Valterra purchases 50%, replacing Sibanye" [1].
- **Looptijd:** einddatum 31-12-2026 is afgeleid; de lijn is een reserve die op 1-1-2027 vervalt (waterval-keten neemt over). Engineering News-artikel [6] niet gelezen (HTTP 403), alleen via zoekresultaat.
- **Wegkm onbekend:** geen bron voor een echte wegkilometer; 9,4 km is OSRM-indicatie, hemelsbreed 6,7 km. Kort been (kaartlijn van enkele km, vgl. `kroondal-waterval` afgewezen golf 14): bewust gehouden omdat 9,4 km boven het 5 km-naadcriterium ligt en de relatie gebrond is.
- **Overlap:** geen gedeelde geometrie met `pgm-tharisa-waterval` (die gaat westwaarts via Karee Road D108; dit been oostwaarts); alleen het vertrekanker is gedeeld.

## 8 · Bronnen
[1] Tharisa plc, SENS/RNS "Valterra Platinum to purchase 50% of Tharisa Mine PGM concentrate from 1 January 2027" (replacing Sibanye-Stillwater; Northam houdt 50%), 2026-10-15, https://www.tharisa.com/download/sens-rns-tharisa-valterra-offtake-and-chrome-collaboration-15oct26.pdf
[2] Tharisa plc, Q4 FY2026 production report (153,7 koz 6E, 5,5 Mt gemalen, guidance FY2027 150-170 koz), 2026-10-13, https://www.tharisa.com/download/sens-rns-tharisa-q4-fy2026-production-report-13oct26.pdf
[3] Mining-technology, Tharisa/Valterra PGM offtake (Valterra replaces Sibanye, 1-1-2027, geen leveringsplaats), https://www.mining-technology.com/news/tharisa-pgm-offtake-valterra-platinum/
[4] Sibanye-Stillwater Form 20-F FY2025, Exhibit "Marikana operations": "one smelter treating concentrate and recycled material from Marikana and limited amounts for third parties", https://www.sec.gov/Archives/edgar/data/0001786909/000162828026026991/ssw_marikanaxoperationsx.htm
[5] Sibanye-Stillwater Form 20-F FY2025 (hoofddocument, startpunt, niet gelezen), https://www.sec.gov/Archives/edgar/data/1786909/000162828026026991/sbsw-20251231.htm
[6] Engineering News, "Valterra joins Northam as a buyer of Tharisa PGM concentrate", 2026-10-15 (alleen titel/snippet via zoekresultaat; HTTP 403), https://engineeringnews.co.za/article/valterra-joins-northam-as-a-buyer-of-tharisa-pgm-concentrate-2026-10-15
[7] Mining-technology, project Tharisa: 35 km oost van Rustenburg, twee verwerkingsplants Genesis en Voyager, PGM-concentraat uit chroomtails door flotatie, https://www.mining-technology.com/projects/tharisa/
[8] OSRM public demo (router.project-osrm.org), 2026-11-01: plant -> BMR 9,386 km (Marikana Road D1325 ~6,0 km, Marikana Road D314 0,5 km, Skierlik Road D314 2,2 km); met de drie via-punten 9,386 km. Indicatie, geen publicatie.
[9] Wikipedia "Marikana" (Wonderkop 4 km van Marikana; Marikana ~-25.698, 27.472), https://en.wikipedia.org/wiki/Marikana
[10] `v2/design/routebrieven/pgm-tharisa-waterval.md` §3 (anker plant, z15) en `pgm-marikana-brakpan.md` §3 (anker BMR, z17-z18, volumes smelter/BMR).
[11] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-pgm-tharisa-marikana-tharisa-plant.png`, `…-marikana-bmr.png` (z15) en `…-route.png` (z14).
[12] BusinessDay, "Valterra to buy 50% of Tharisa Mine's PGM concentrate", 2026-10-15 (alleen zoekresultaat-snippet), https://www.businessday.co.za/companies/company-strategy/2026-10-15-valterra-to-buy-50-of-tharisa-mines-pgm-concentrate/

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
- **Bestand:** `v2/data/stroomroute-pgm-tharisa-marikana.json` (4,5 KB), versie 2, lonlat, 1 been, 172 punten, 2 markers. Functie `bak_pgm_tharisa_marikana` in `bak_stromen.sh`, profiel `pgm-tharisa-marikana-tharisa-marikana` in `maak_stroombeen_weg.py`.
- **b1 truck** 9,6 km (172 punten), doorgetrokken, geen stippel: plant -> D1325 -> D314 -> BMR. Segmenten via-punt voor via-punt 5,8 / 0,8 / 0,5 / 2,3 km, geen omweg. Lengtetoets +5,1% tegen 9 km-indicatie (geen echte wegkm; hemelsbreed 6,7 km, OSRM 9,4 km); het wegeinde snapt 0,14 km van het BMR-anker, het begin 0,03 km van de plant.
- **Naden:** een been, dus geen naad. **Markers:** pgm-tharisa-plant en pgm-marikana-bmr beide 0,0 km van de lijn.
- **Toets:** `toets_knikken` 4 knikken (alle spikes op 12-82 m schaal), 0 omkeringen, 0 terugloop; `toets_rechte_benen` geen treffer; versie 2 / lonlat / modaliteit truck.
- **Recept:** wegscan `zuid-afrika` (114 s), refs D1325 en D314, corridorKlassen tertiary + unclassified, vensterKm 10; geen haven-aanloop, kopie, lucht of leiding.
- **Lessen:** kort aannemelijk-been (9,6 km, mine-to-smelter naast het eigen vertrekanker); de lijn vervalt 1-1-2027 (Valterra neemt over, keten pgm-tharisa-waterval); beennaam draagt "aannemelijk: één bron; tot 31-12-2026".
