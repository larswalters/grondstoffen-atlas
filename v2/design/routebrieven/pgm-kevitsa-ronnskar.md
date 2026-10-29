# Routebrief (licht) · PGM — Kevitsa → Ajos (Kemi) → Rönnskär (Zweden)

**stroom-id:** `pgm-kevitsa-ronnskar` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** Cu-/Ni-concentraat met Pt/Pd-bijproduct van Boliden's Kevitsa-mijn (Sodankylä, Lapland) gaat per **truck** (Vt4/E75 via
Rovaniemi) naar de haven Ajos in Kemi en van daar per **zeeschip** over de Botnische Golf naar de Boliden-smelter Rönnskär (Skelleftehamn);
stoppunt = de smelter. **"Aannemelijk": Boliden noemt Rönnskär als smelter, geen bron noemt vervoerswijze of volume naar Rönnskär.**
**Welke as van het verhaal:** de Nordic zee-as van het enige EU-PGM-bijproduct, en het alternatief voor `pgm-kevitsa-harjavalta` (zelfde begin,
andere zeestraat). Peiljaar **2025**: 33.583 oz Pt + 29.627 oz Pd in concentraat = 63,2 koz = **hoogstens ~1,97 t 2E/j voor héél Kevitsa**
(Pt ~1,04 t + Pd ~0,92 t; geen Rh/Au; koz ÷ 32,15) [3]. Het deel dat naar Rönnskär gaat is **niet gepubliceerd** (§7).

## 1 · Ketenkaart
```
Kevitsa-concentrator `pgm-kevitsa-concentrator` ──(b1 truck · Vt4/E75 · 306,6 km gebakken [~300 wegkm, VR 2018])──► Ajos, Kemi `pgm-ajos-kade`
──(b2 zee · Botnische Golf · MARNET 223,6 km, hemelsbreed 188 km, aannemelijk)──► Rönnskär, Skelleftehamn `pgm-ronnskar-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-kevitsa-concentrator` → `pgm-ajos-kade` | mijnweg → Vt4/E75 (Sodankylä, Rovaniemi, Tervola, Kemi) → Ajos | ~300 wegkm (VR Linked 2018) [6]; gebakken 306,6 (+2,2%) | **letterlijke kopie** `pgm-kevitsa-harjavalta` b1 (`$BEEN/pgm-kevitsa-harjavalta-weg-kevitsa-ajos.geojson`, functie `bak_pgm_kevitsa_harjavalta`) | nee |
| b2 | B | zee | `pgm-ajos-kade` → `pgm-ronnskar-kade` | Botnische Golf, Kemi → Skelleftehamn (aannemelijk: bestemming Rönnskär niet per vervoerswijze gebrond) | **geen gepubliceerde zeekm**; MARNET 223,6 (hemelsbreed 188, verhouding 1,19); ±15%-toets n.v.t. | MARNET (`--been "zee\|…"`) | aanloop: **nee** (Ajos 1,37 km, Rönnskär 1,51 km van de zeeknoop) |

Geen fase C/D: Rönnskär is zelf de smelter. Geen spoorbeen: het alternatief Kemi → Haparanda → Zweedse spoorlijn is niet onderzocht en geen bron noemt het.
Het zeevervoer uit Ajos is **wel gebrond** voor 2013–2014 (Kevitsa-Cu-concentraat per schip uit Ajos, 50.000 t in 2013, 77.000 t in 2014 [4][5]), maar zonder
bestemmingshaven; Kevitsa was toen van First Quantum, Boliden kocht de mijn pas in 2016 (zie [3]).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-kevitsa-concentrator` | mijn + concentrator (kop) | Boliden Kevitsa, Sodankylä | 67.6945, 26.9334 | [1][3][9] | bron-gelegd, **hergebruikt** uit `pgm-kevitsa-harjavalta`; z15 opnieuw gezien: concentratorhallen met silo/koepel en tailingbekken direct zuidoost van de pit; het kruis ligt op de hoofdhal |
| `pgm-ajos-kade` | overslag truck → zee | Port of Kemi, Ajos, kade/pakhuiszone | 65.6650, 24.5210 | [4][5][9] | bron-gelegd, **hergebruikt** uit `pgm-kevitsa-harjavalta`; z15 opnieuw gezien: kruis bij de pakhuizen op de kopse kant van de westpier (kade met kranen, Metsä-hal, havenspoor; tankenpark oostelijk). Welk pakhuis het concentraatpakhuis is blijft onbekend |
| `pgm-ronnskar-kade` | losplek zee / smelter (stoppunt) | Boliden Rönnskär, Skelleftehamn | 64.6704, 21.2699 | [2][7] | bron-gelegd, **hergebruikt** uit `ag-ronnskar-kade` (zilver-garpenberg-ronnskar); z15 opnieuw gezien: smeltercomplex met schoorstenen en tanks op het schiereiland, het kruis ligt aan de noordwestrand bij het rangeerspoor en de opslaghallen; kades langs de oostkant (zeeknoop 8833 op 1,5 km) |

## 4 · Via-punten
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1–2 | Rovaniemi 66.5425, 25.8179 · Tervola 66.0869, 24.7729 | zie links | geërfd van de kopie (`pgm-kevitsa-harjavalta` §4): pinnen Vt4/E75, geen nieuw punt gelegd |
| b2 | — | geen | — | zee = MARNET-router kade → kade; geen corridorkeuze op een zeebeen |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kevitsa | Boliden | erts (10,2 Mt gemalen 2025) → Cu- en Ni-concentraat met Pt, Pd, Au, Co | 63,2 koz Pt+Pd in concentraat 2025; verdeling Cu-/Ni-concentraat en per smelter niet gepubliceerd | [1][3] |
| Ajos (Port of Kemi) | Kemin Satama / Baltic Bulk | concentraat per truck → pakhuis → schip (2013–14 gebrond) | 77.131 t Cu-/Ni-concentraat geëxporteerd in 2014 | [4][5] |
| Rönnskär | Boliden | Cu-/Pb-concentraat → 266 kt Cu, 27 kt Pb, 28 kt Zn-klinker, 191 t Ag, 5 t Au (2025); **productlijst noemt geen Pt/Pd** | niet gepubliceerd; eigen haven en spoor | [2] |

## 6 · Stoppunt
De brief stopt bij de Rönnskär-smelter: Boliden noemt de smelter als bestemming van Kevitsa-concentraat [1], maar geen bron zegt waar Pt/Pd na Rönnskär heen gaat
(productlijst [2] zonder PGM) — geen fase D. Fase E vervalt.

## 7 · Open punten
- **PGM-aandeel naar Rönnskär onbekend**: [1] zegt alleen dat de concentraten Pt, Pd en Au bevatten en naar Harjavalta **en** Rönnskär gaan; [2] noemt geen Pt/Pd.
  Het volume op deze stroom is dus een bovengrens van 0 tot ~1,97 t 2E/j, geen meting; Rönnskär is een kopersmelter en alleen het Cu-concentraat gaat er vermoedelijk heen.
- **Vervoerswijze Kemi → Skelleftehamn niet gebrond**: schip uit Ajos is gebrond voor 2013–14 [4][5], de bestemming daarvan niet. Alternatief per spoor via Haparanda niet onderzocht.
- **Zeekm niet gepubliceerd**: 223,6 km is MARNET (hemelsbreed 188); geen ±15%-toets, alleen een indicatie. Winterijs op de Botnische Golf is niet gemodelleerd.
- **Naad b1 → b2 1,37 km** (kade Ajos → zeeknoop 8836): onder de 5 km-drempel, bewust zonder haven-aanloop; idem Rönnskär 1,51 km.
- **Kevitsa-sluiting**: Boliden's rapport noemt een sluitingsplan en een herziening [3]; peiljaar 2025. Kleine stroom: Kevitsa is ~1% van de wereld-PGM.
- Sitelaag: Kevitsa, Ajos en Rönnskär staan niet in `pgm-sitelaag.json` (centraal: 67.6945,26.9334 · 64.6704,21.2699 · Harjavalta-stroom deelt Ajos).

## 8 · Bronnen
[1] Boliden, "Boliden Kevitsa" — concentraten naar eigen smelters Harjavalta en Rönnskär, bevatten Ni, Cu, Co, Pt, Pd, Au; geen vervoerswijze. https://www.boliden.com/operations/mines/boliden-kevitsa
[2] Boliden, "Boliden Rönnskär" — Cu- en Pb-concentraat van eigen mijnen en externen, productie 2025, eigen haven en spoor (historisch), geen Pt/Pd. https://www.boliden.com/operations/smelters/boliden-ronnskar
[3] Boliden, Summary Report Kevitsa — Mineral Resources and Reserves 31-12-2025: Pt/Pd in concentraat 2025, 10.155 kt gemalen, eigendomsgeschiedenis (2016 verkocht aan Boliden). https://www.boliden.com/4900d3/globalassets/operations/exploration/mineral-resources-and-mineral-reserves-pdf/2025/mineral-resources-and-mineral-reserves-kevitsa-2025-12-31.pdf
[4] Kemin Satama, Vuosikertomus 2013 — Kevitsa Cu-concentraat c. 50.000 t en Ni c. 6.000 t, eerste vientilaivaukset via Baltic Bulk-hal. https://www.portofkemi.fi/wp-content/uploads/2018/07/kemin-satama-vuosikertomus-2013.pdf
[5] Kemin Satama, Vuosikertomus 2014 — ~77.000 t Kevitsa-kuparirikaste "laivalla" via Ajos (+47%), Cu- en Ni-concentraat samen 77.131 t export. https://www.portofkemi.fi/wp-content/uploads/2018/07/kemin-satama-vuosikertomus-2014.pdf
[6] VR Logistiikka/Linked, 2018, "Kellontarkkaa rikasteliikennettä Kevitsasta Kemiin" — ~300 km (via `pgm-kevitsa-harjavalta` [1]; niet opnieuw gelezen). https://logistics.vr.fi/fi/vr-logistiikka/linked/artikkeli/kellontarkkaa-rikasteliikennetta-kevitsasta-kemiin-120420181226/
[7] Routebrief `zilver-garpenberg-ronnskar` — Rönnskär-anker 64.6704,21.2699 (OSM `landuse=industrial "Rönnskärsverken"` 0 m), zeeknoop 8833. `v2/design/routebrieven/zilver-garpenberg-ronnskar.md`
[8] E&MJ, overname Kevitsa door Boliden (via zoeksnippet in `pgm-kevitsa-harjavalta` [7]; 403, niet gelezen) — concentraat naar Harjavalta en Rönnskär. https://www.e-mj.com/leading-developments/boliden-acquiring-first-quantum-s-kevitsa-mine-in-northern-finland/
[9] Routebrief `pgm-kevitsa-harjavalta` — ankers Kevitsa en Ajos, b1-kopie. `v2/design/routebrieven/pgm-kevitsa-harjavalta.md`
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `sat-pgm-kevitsa-ronnskar-kevitsa|ajos|ronnskar.png` in `v2/build-cache/satcheck/`.
[11] Eigen metingen: `hecht_marnet.py route` (testrun naar scratch: truck 306,6 + zee 223,6 = 530,2 km, 5 MARNET-edges, 0 landkruisingen, snaps 1,37/1,51 km); zeeknopen via `hecht_marnet.marnet_zee`.

## 9 · Gebakken

**Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)** · `v2/data/stroomroute-pgm-kevitsa-ronnskar.json` · 77,1 KB · versie 2, lonlat · 3 markers.

| # | modaliteit | km gebakken | punten | naad naar vorig been | stippel |
|---|---|---|---|---|---|
| b1 | truck | 306,6 (brief ~300 wegkm, +2,2%) | 3.915 | - | nee |
| b2 | zee | 223,6 (MARNET, hemelsbreed 188; geen gepubliceerde zeekm) | 26 | 1,37 km (Ajos-kade naar zeeknoop 8836) | nee |

Totaal 530,2 km.

**Recept.** `bash v2/tools/bak_stromen.sh pgm-kevitsa-ronnskar` (functie `bak_pgm_kevitsa_ronnskar`): b1 = `--been-geojson` letterlijke kopie van `pgm-kevitsa-harjavalta-weg-kevitsa-ajos.geojson` (geen eigen profiel, geen wegscan); b2 = `--been "zee|..."` MARNET kade naar kade (5 edges, snaps 1,37 en 1,51 km).

**Toelichting.** Geen stippel, geen haven-aanloop (beide kades onder de 5 km-drempel van hun zeeknoop), geen lucht, leiding of spoor. b2 is "aannemelijk": de vervoerswijze Kemi naar Skelleftehamn is niet gebrond. Winterijs niet gemodelleerd.

**Toets.** Km b1 binnen +-15% van de ~300 wegkm; b2 niet toetsbaar (geen gepubliceerde km). Naad b1-b2 1,37 km (<5). Markers: Kevitsa en Ajos 0,0 km van de lijn, Rönnskär 1,51 km (kade tegenover de zeeknoop-eindpunt van de lijn; procesgat onder de drempel). `toets_knikken`: 8 knikken >= 60 gr, allemaal op b1 en geerfd van de kopie (1 omkering 168,9 gr bij 65.7156,24.6135 = scherpe bocht, echt; 0 terugloop); zee 0. `toets_rechte_benen --min-km 5`: geen melding voor deze stroom.

**Lessen.** Een eerdere poging had de functie al geschreven; vervangen was niet nodig, alleen bakken en toetsen. Hergebruik van b1 en de Rönnskär-kade scheelde een wegscan. Sitelaag mist Kevitsa, Ajos en Rönnskär (centraal).
