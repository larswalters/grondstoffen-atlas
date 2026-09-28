# Routebrief (licht) · PGM — Van → Via → Naar (land)

**stroom-id:** `pgm-stillwater-columbus` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** platinagroepmetaal (Pd-dominant 2E: Pd 77% / Pt 23%) als geconcentreerd erts per **truck**
van de Stillwater Mine (Nye, Beartooth-front) over Nye Road/MT-78 naar het Columbus Metallurgical Complex
(smelter + base metal refinery) van Sibanye-Stillwater — daar tot PGM-rijke filter cake, die volgens de eigen
20-F wordt verzonden naar "a third-party refiner" zonder naam of locatie — **stoppunt**, het bewijs eindigt hier.
**Welke as van het verhaal:** de enige actieve PGM-mijnbouw in de VS. Sibanye-Stillwater's Amerikaanse operaties
(Stillwater + East Boulder, beide op de J-M Reef) produceerden peiljaar 2023 ~460–490 koz 2E/jaar (Pd+Pt) ≈
14,3–15,2 t 2E/jaar (koz ÷ 32,15) [2]. East Boulder Mine (Big Timber) voedt dezelfde Columbus-smelter via een
eigen, hier niet gelegde corridor — buiten de scope van het ontwerp (één been, zie §7).

## 1 · Ketenkaart
```
Stillwater Mine, Nye `pgm-stillwater-laad` ──(b1 truck · Nye Road (CR-419) → MT-78 → Columbus · ~64 km)──►
Columbus Metallurgical Complex `pgm-columbus-smelter` (smelter + base metal refinery)
   ═══ knoop: PGM-rijke filter cake (2E) ═══ ── stoppunt (afnemer "a third-party refiner" niet gedocumenteerd)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-stillwater-laad` → `pgm-columbus-smelter` | Nye Road (CR-419, Stillwater River) → **MT-78** (Absarokee) → Columbus (Pike Ave/business route, aansluiting I-90) | ~64 [3][7] (ontwerp gaf ~50 km indicatie, zie §7) | maak_stroombeen_weg — profiel `pgm-stillwater-columbus` | nee — beide uiteinden op het bestaande wegnet (mijn heeft een verharde toegangsweg naar CR-419; smelterterrein grenst direct aan Pike Ave) |

Geen zee-, spoor- of luchtbeen: dit is een enkelvoudig truck-been, fase A → stoppunt bij de smelter (fase B/C
niet gedocumenteerd, zie §6).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-stillwater-laad` | mijn / concentrator (laadplek) | Stillwater Mine (Sibanye-Stillwater), 2562 Nye Road, Nye, Stillwater County | 45.3880, -109.8920 | [1][3][5][6] | bron-gelegd (z15 gezien: mijncomplex met concentrator-/verwerkingsgebouwen, tailings-bekken en dagbouw-/adit-terrein aan de Stillwater River; OSM-landuse "Stillwater Mine" op het complex) |
| `pgm-columbus-smelter` | verwerkingsknoop (smelter + base metal refinery) | Columbus Metallurgical Complex (Sibanye-Stillwater), Columbus, Stillwater County | 45.6330, -109.2400 | [1][4][6] | bron-gelegd (z15 gezien: industrieel perceel met verwerkingsgebouwen direct naast de spoorlijn en de Yellowstone River, zuidrand van Columbus; OSM-landuse "Sibanye Stillwater Smelter and Refinery" exact op het perceel) |

## 4 · Via-punten (b1 — twee echte corridorkeuzes op deze route)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Nye (hamlet) — Nye Road/mijnweg-knoop | 45.4350, -109.8037 | hier voegt de mijntoegangsweg zich bij de doorgaande Stillwater River Road/CR-419 richting Absarokee (geen andere route stroomafwaarts) |
| b1 | 2 | Absarokee — aansluiting op **MT-78** | 45.5211, -109.4426 | hier verlaat de corridor de county road en gaat verder over de staatsweg MT-78 noordwaarts naar Columbus; enige verharde doorgaande route |

Geen derde via-punt: tussen Absarokee en Columbus is MT-78 de enige verharde weg (geen alternatieve corridor
om uit te sluiten), dus minder dan de richtlijn van 3–8 punten is hier eerlijk aan de geografie.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Columbus Metallurgical Complex | Sibanye-Stillwater | gemalen/geconcentreerd 2E-erts (Stillwater + East Boulder) → PGM-rijke filter cake (+ Ni/Cu-bijproduct) | VS-operaties samen ~460–490 koz 2E/jaar (peiljaar 2023) | [2] |

## 6 · Stoppunt
De brief stopt bij de poort van het Columbus Metallurgical Complex: Sibanye-Stillwater's eigen 20-F noemt de
afnemer van de PGM-rijke filter cake alleen als "a third-party refiner", zonder naam of locatie [2]. Volgens de
eerlijkheidsregel van de kaart (haalbaarheidstoets, bindend: "geen aanpassing nodig") wordt hier niet naar een
plausibele raffinaderij doorgetekend — het bewijs eindigt waar de bron eindigt. Fase B/C/D/E vervallen.

## 7 · Open punten
- **Gepubliceerde afstand:** het ontwerp gaf "~50 km" als indicatie; Encyclopedia.com noemt bij de bouw van de
  smelter expliciet "40 miles away" vanaf de mijn [7] (≈ 64 km). De via-punten-optelling (mijn→Nye→Absarokee→
  Columbus, hemelsbreed ~58,5 km) ligt dicht bij die 64 km zodra de rivierbochten meetellen — bij het bakken de
  gepubliceerde 64 km (40 mi) als toetswaarde gebruiken, niet de ontwerp-indicatie van 50 km.
- **East Boulder Mine** (Sibanye-Stillwater, bij Big Timber, MT; OSM-landuse-node 45.5080, -110.0830) voedt
  dezelfde Columbus-smelter maar heeft een eigen, hier niet gelegde corridor (andere county, andere weg) — het
  ontwerp beschrijft één been (Stillwater Mine → Columbus); East Boulder → Columbus is een aparte keten, niet
  in deze brief getekend.
- **Exacte laadplek op het mijnterrein** (concentrator-expeditie) en **losplek op het smelterterrein** zijn niet
  op site-niveau verder aan te wijzen dan het complex zelf (géén grid-pass, conform de lichte werkwijze).
- **Mengverhouding VS-filter cake:** het jaarvolume (§ hierboven) is voor Stillwater + East Boulder samen; het
  aandeel van alleen Stillwater Mine in het volume op dit been is niet apart gepubliceerd.

## 8 · Bronnen
[1] Sibanye-Stillwater, PGM Operations Americas — Stillwater & East Boulder (Nye Road-adres, smelter + base
metal refinery Columbus, "shipped to third-party custom refiners"). https://www.sibanyestillwater.com/business/pgm-operations-americas/stillwater-east-boulder/
[2] Sibanye-Stillwater, Form 20-F FY2023 (via SEC EDGAR) — VS-productie 2E, filter cake naar "a third-party
refiner". https://www.sec.gov/Archives/edgar/data/1786909/000178690924000019/sbsw-20231231.htm
[3] Mining Technology — Stillwater and East Boulder projects (locatie, smeltroute). https://www.mining-technology.com/projects/stillwater-and-east-boulder/
[4] Wikipedia — Columbus, Montana (county seat, Stillwater County). https://en.wikipedia.org/wiki/Columbus,_Montana
[5] Wikipedia — Stillwater Mining Company (mijnen bij Nye/Big Timber, smelter + base metal refinery Columbus,
"shipped to third-party custom refiners for final refining before being sold"). https://en.wikipedia.org/wiki/Stillwater_Mining_Company
[6] OpenStreetMap (ODbL) via Nominatim — landuse "Stillwater Mine" 45.3880/-109.8920 (Mountain View Road,
Stillwater County) · landuse "Sibanye Stillwater Smelter and Refinery" 45.6330/-109.2400 (East 1st Ave S,
Columbus) · hamlet "Nye" 45.4350/-109.8037 · village "Absarokee" 45.5211/-109.4426 · landuse "East Boulder
Mine" 45.5080/-110.0830 (Sweet Grass County). https://www.openstreetmap.org
[7] Encyclopedia.com — Stillwater Mining Company (bedrijfsgeschiedenis: smelter "under construction 40 miles
away" in Columbus). https://www.encyclopedia.com/books/politics-and-business-magazines/stillwater-mining-company
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-pgm-stillwater-columbus-mijn.png`,
`sat-pgm-stillwater-columbus-smelter.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `pgm-stillwater-columbus`** → `v2/data/stroomroute-pgm-stillwater-columbus.json` — 1 been (truck, fase A →
stoppunt), **76,2 km**, 1.203 punten, 2 markers, 26,3 KB. Recept: `bak_stromen.sh` (functie
`bak_pgm_stillwater_columbus`); nieuw wegprofiel `pgm-stillwater-columbus` in `maak_stroombeen_weg.py`. Geen
zee/spoor/lucht/stippel — het eerste enkelvoudige-truckbeen-recept van deze golf (geen haven-aanloop nodig).

**b1 (truck, nieuw profiel, extract `us-montana`, vensterKm 40):** `maak_stroombeen_weg.py --profiel
pgm-stillwater-columbus --bron geofabrik` — **75,9 km** geroute (getekende lijn 76,2 km incl. anker-
verbindingsstukjes) over de twee via-punten uit de opdracht (Nye → Absarokee/MT-78), geen alternatieve corridor
gevonden — de router volgt Nye Road (CR-419) → MT-78, exact de opgegeven keten. Anker-verbindingsstukjes plant →
weg 0,22 km en weg → kade 0,09 km (beide OK, ruim binnen 0,5 km). Eén kleine keerlus gesnoeid (0,43 km, dubbel
gereden stuk bij Nye). First mile 15,48 km over kleine wegklassen (service/tertiary/unclassified — de county
road Nye Road zelf valt hieronder), last mile 1,19 km (residential/service/unclassified in Columbus) — beide
binnen de 12 km-marge van het profiel.

**⚠️ Lengtetoets BUITEN de norm:** 75,9 km (getekend 76,2 km) tegen de toetswaarde 64 km (40 mi, Encyclopedia.com
[7]) = **+18,6% resp. +19,1%** — boven het venster van 54–74 km (±15%). Dit is een **bevinding, geen fout**: de
router volgt de enige verharde doorgaande corridor (Nye Road/CR-419 → MT-78) langs de Stillwater River, en die
corridor is aantoonbaar langer dan de gepubliceerde "40 miles" hemelsbreed-achtige schatting uit Encyclopedia.com
— vermoedelijk een journalistieke afronding op het moment van de smelterbouw (1990) die de rivierbocht bij Nye
niet meetelt. Geen via-punt bijgeschoven om het getal te halen (conform de norm); de twee via-punten pinnen de
enige bestaande corridorkeuzes (Nye Road/CR-419-knoop bij Nye, MT-78-aansluiting bij Absarokee) en zijn niet
aangepast.

**Toetsen:** `toets_knikken.py` — 7 knikken ≥60° (spikes bij scherpe kruispunten/bochten van de county road/MT-78),
**0 omkeringen ≥150°, 0 terugloop** (de enige klasse die gerepareerd hoort te worden) — geen actie nodig.
`toets_rechte_benen.py --min-km 5` — geen melding voor deze stroom (been is geen rechte lijn, omwegfactor > 1,000).
`json.load` slaagt: versie 2, `punt_formaat` lonlat, modaliteit `truck` ∈ toegestane set, been ≥ 2 punten (1.203),
bestandsgrootte 26,3 KB (ruim onder ~300 KB). Geen naad (1 been, geen vertakking).

**Toelichting stippels/haven-aanlopen/vluchten:** geen. Beide uiteinden liggen op het bestaande wegnet zoals de
opdracht voorschreef — mijn heeft een verharde toegangsweg naar CR-419 bij Nye (snap 0,22 km), smelterterrein
grenst direct aan de openbare weg in Columbus (snap 0,09 km). Geen zeebeen dus geen haven-aanloop nodig; geen
bron noemt luchtvracht voor deze stroom dus geen luchtbeen.

**Gereedschapslessen:** geen nieuwe tool-issues. Het profiel-/functiepatroon uit `bakhandleiding-licht.md` §4 werkte
zonder aanpassing voor een enkelvoudig truckbeen (kortste bake van deze golf: één `--been-geojson`, twee markers,
geen `--stippel`/`--stippel-geojson`/vertakking).
