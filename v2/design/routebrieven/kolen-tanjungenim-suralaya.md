# Routebrief (licht) · kolen — Tanjung Enim → Tarahan → Suralaya (Indonesië)

**stroom-id:** `kolen-tanjungenim-suralaya` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken (2026-10-09)
**Keten in één zin:** thermische kolen van de PTBA-mijnen bij Tanjung Enim (Zuid-Sumatra) gaan per **spoor** (PTBA/KAI-kolenlijn via Muara Enim,
Baturaja en Martapura, ~420 km) naar PTBA's eigen haven Tarahan in de Baai van Lampung, per **zeeschip** over de Straat Soenda (±100 km) naar de
kolensteiger van PLTU Suralaya (PLN/Indonesia Power, Banten, Java), en per **band** (stippel, < 2 km) naar de ketelhuizen. Stoppunt = de centrale.
**Welke as van het verhaal:** *binnenlandse kolenketen Sumatra → Java* (mijn → haven → centrale, nooit een grens over). Tanjung Enim produceerde
**42,0 Mt in 2024** (GEM [3]; PTBA totaal 43,3 Mt, verkoop 42,9 Mt = 22,6 Mt binnenland + 20,3 Mt export, spoorvervoer 38,2 Mt [4]); Tarahan is
sinds 1986 gebouwd om deze kolen naar Suralaya te schepen en laadt 25 Mt/j [2]. Het volume van déze as is niet gepubliceerd: PTBA → Suralaya was
5,1 Mt in 2008 (6,1 Mt vanaf 2009) [7]; voor 2012 meldt een ESDM-bericht ~12 → ~6 Mt/j [10, alleen via samenvatting]; recent noemt een
PTBA-medewerker Tarahan, Suralaya, Cirebon en Sebalang als bestemmingen zonder tonnage [8]. Het zeebeen is dus *aannemelijk: één bron voor het
havenpaar* — Tarahan → Suralaya is de historische hoofdbestemming [2][1], niet het hele Tarahan-volume (47 % van PTBA's verkoop is export [4]).

## 1 · Ketenkaart
```
PTBA-laademplacement Tanjung Enim `kolen-tanjungenim-laad`
   ──(b1 spoor · PTBA/KAI-kolenlijn via Muara Enim – Baturaja – Martapura – Kotabumi · ~420 km gepubliceerd, 405 km spoornet)──►
Tarahan-kade `kolen-tarahan-kade`
   ──(b2 zee · Baai van Lampung → Straat Soenda · ±100 km gepubliceerd, aannemelijk: één bron; MARNET + 2 haven-aanlopen)──►
Suralaya-kolensteiger `kolen-suralaya-steiger`
   ──(b3 band/last mile · < 1 km · stippel)──► PLTU Suralaya `kolen-suralaya-pltu` ⏹ stoppunt (kolen → elektriciteit, geen fase D/E)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-tanjungenim-laad` → `kolen-tarahan-kade` | PTBA-kolenlijn Tanjung Enim – Muara Enim – Baturaja – Martapura – Kotabumi – Tarahan (KA Babaranjang, KAI); de aftakking richting Kertapati (180 km) is de andere uitvoerlijn en wordt niet gevolgd | 420 [1][2] (spoornet: 405,1 km, −3,6 %) | `toets_spoorroute` 2 runs, 1 via-punt (§4) | nee — lijn zit in het 1-op-1-net; het laatste stuk naar de kade (0,7 km) is naad, geen stippel |
| b2 | B | zee | `kolen-tarahan-kade` → `kolen-suralaya-steiger` | Baai van Lampung → Straat Soenda → Banten-kust | ±100 over zee [2]; hemelsbreed 87; MARNET gemeten 121,9 + aanlopen 8,2 + 10,7 = 140,8 | MARNET zeeknoop → zeeknoop + 2 haven-aanlopen | ja — Tarahan-aanloop (8,2 km, rechte stippel: `maak_havenaanloop` hing 300 s) en Suralaya-aanloop (10,7 km, geroutet, geen land); **aannemelijk: één bron** |
| b3 | C | truck (band) | `kolen-suralaya-steiger` → `kolen-suralaya-pltu` | transportband steiger → kolenopslag (z16 gezien) | 1,0 hemelsbreed, geen wegkm | stippel | ja — last mile (geen net op deze korrel) |

⚠️ **Verwachte afwijking b2 (+41 % t.o.v. ±100 km):** beide zeeknopen liggen aan de verkeerde kant van de straat (Tarahan: 8,2 km NW; Suralaya: 10,7 km O). Dat is netkorrel
van MARNET, geen routefout; de bake meet het getal, er wordt geen via-punt bijgeschoven. Gepubliceerde ±100 km is een afgeronde bron-opgave, geen operator-routelengte.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-tanjungenim-laad` | mijn-/laadplek (kop spoor) | PTBA-treinlaad (TLS) + kolenopslag Tanjung Enim | -3.7340, 103.7908 | [3][11] | bron-gelegd (z16/z17 gezien: wagenemplacement met rijen wagons, brede kolenstapel met transportbanden en spoorbundel naar ZO; ligt 2,5 km ten O van GEM's mijncentroïde -3.7400/103.7683, dat in de dagbouwputten valt) |
| `kolen-tarahan-kade` | overslag spoor → zee | PTBA Unit Pelabuhan Tarahan, kolenkade met shiploader | -5.5183, 105.3441 | [2][11] | bron-gelegd (z17 gezien: bulkcarrier aan de kade onder een shiploader, achter de kade kolenstapels en rangeersporen; spoorknoop op 0,7 km N) |
| `kolen-suralaya-steiger` | losplek zee | kolensteiger PLTU Suralaya (PLN), steigerkop met schip | -5.8833, 106.0295 | [6][11] | bron-gelegd (z16 gezien: ~0,8 km lange steiger NO-waarts met bulker langszij en een transportband over de steiger naar het kolenveld) |
| `kolen-suralaya-pltu` | verwerker / afnemer | PLTU Suralaya (Indonesia Power / PLN), ketelhuizen | -5.8922, 106.0303 | [5][6] | bron-gelegd (z16 gezien: rij ketelhuizen met schoorstenen, kolenopslag N ervan, ontziltingstanks en een kleine haven) |

## 4 · Via-punten (alleen b1 — het spoor)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Baturaja-station (spoor-vertex ≤ 0,1 km) | -4.1273, 104.1620 | de corridorkeuze Kertapati (180 km noord) of Baturaja/Tarahan (420 km) valt bij Prabumulih; dit punt pint de Tarahan-lijn. Vrije Dijkstra gaf al dezelfde 405,1 km, dus de pin verandert niets — hij borgt alleen |
| b1 | – | *controle (niet gepind):* Muara Enim -3.6526/103.7762 · Martapura -4.3164/104.3468 · Blambangan Umpu -4.4982/104.5202 · Kotabumi -4.8219/104.8813 · station Tarahan -5.5019/105.3346 | | route raakt ze op 0,31 · 0,17 · 0,15 · 0,14 · 0,23 km; Kertapati-station (-3.0166/104.7516) wordt op 75 km gemeden; Prabumulih-station (-3.4329/104.2408) op 2,0 km — lijn zonder die stationsemplacement |

Geofabrik-extract: `indonesie` (spoor via het 1-op-1-net `raw1op1/indonesie`). Geen wegbeen, geen extra extracts.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Tarahan-haven | PT Bukit Asam Tbk | trein (23–25 treinen/dag × 60 wagons × 50 t, 4 car dumpers) → stockpile (4, ~860 kt) → 3 jetties (80–205 kDWT) | ladingscapaciteit 25 Mt/j [2]; havenlicentie t/m sep. 2027 [3] | [2][3] |
| PLTU Suralaya | PLN / Indonesia Power (fase I–III); PLN + Barito Pacific (unit 9–10) | steenkool → elektriciteit | 4.025 MW (Wikipedia, 8 units) [5]; GEM telt 6.025 MW incl. unit 9–10 [6]; eigen kolenterminal [6] | [5][6] |

## 6 · Stoppunt
De brief stopt bij de kolenopslag van PLTU Suralaya: kolen wordt daar in één stap verstookt, dus geen fase D/E (zelfde afbakening als `kolen-sangatta-mundra`).

## 7 · Open punten
- **Aandeel Suralaya in het PTBA-volume niet gepubliceerd** (2008: 5,1 → 6,1 Mt [7]; 2012-bericht [10] niet te heropenen). PLN betrekt Suralaya-kolen ook van andere leveranciers (6 bedrijven in 2020) en PTBA levert ook aan Cirebon/Sebalang/Tarahan-PLTU [8] en export [4].
- **Het exacte Tanjung Enim-laadpunt** is niet door één bron aangewezen: het anker volgt OSM's "TLS PTBA" + het wagenemplacement; er zijn meer laadstations rond de mijnen (Banko, Air Laya). Spoorkop is router-vertex op 0,35 km.
- **Zee-knopen scheef (b2):** Tarahan 8,2 km en Suralaya 10,7 km van de MARNET-zeeknoop → aanloop beide kanten verplicht; Tarahan-aanloop is rechte stippel (router hing). Suralaya-aanloop is al gebakken in `v2/build-cache/ais/graaf/kolen-tanjungenim-suralaya-aanloop-suralaya.geojson` (zeeknoop → kade).
- **Sitelaag-centroïde `w-tanjung-enim`** (-3.7400/103.7683, GEM) ligt 2,5 km W van het laadanker; gloed hoort op het laadanker (centraal gelijktrekken).
- **Spoorkm 405,1 vs 420**: gepubliceerd is afgerond/historisch (2006) [1]; −3,6 % is binnen de norm.
- Geen wegbeen, geen leiding, geen vlucht.

## 8 · Bronnen
[1] Petromindo, 2006-06-03 — PTBA/KAI tarief: Tanjung Enim → Tarahan 420 km, → Kertapati 180 km; Suralaya (PLN) = PTBA's hoofdafnemer. https://www.petromindo.com/news/article/ptba-kai-agree-on-new-railway-rate
[2] Univ. Darmajaya (Lampung), "Tentang Perusahaan PT Bukit Asam Unit Pelabuhan Tarahan" — 55 ha, sinds 1986 TUKS voor Tanjung Enim → PLTU Suralaya, 420 km, 3 jetties, 25 Mt/j, 860 kt opslag, Suralaya ±100 km over zee. http://repo.darmajaya.ac.id/22398/7/07.%20BAB%20II.pdf
[3] Global Energy Monitor, PTBA Coal Mines — 41,75 Mt (2023), 42,0 Mt (2024, site-totaal), 47,2 Mt (2025); havens Tarahan/Kertapati/Teluk Bayur; Tarahan-licentie t/m 2027. https://www.gem.wiki/PTBA_Coal_Mines
[4] Kompas Money, 2025-02-04 (+ Tambang.co.id) — PTBA 2024: verkoop 42,9 Mt, binnenland 22,6 / export 20,3 Mt, productie 43,3 Mt, spoorvervoer 38,2 Mt (via zoeksamenvatting; pagina gaf 403). https://money.kompas.com/read/2025/02/04/150000726/penjualan-batu-bara-bukit-asam-cetak-rekor-tembus-429-juta-ton-pada-2024
[5] Wikipedia, Suralaya Power Station — 5°53′32″S 106°01′49″E; 4.025 MW; Indonesia Power. https://en.wikipedia.org/wiki/Suralaya_Power_Station
[6] Global Energy Monitor, Banten Suralaya power station — kolen van Bukit Asam, Zuid-Sumatra; eigen PLN-kolenterminal; units 1–10, eigendom. https://www.gem.wiki/Banten_Suralaya_power_station
[7] detikFinance, 2008-11-24 — PTBA-levering aan PLTU Suralaya 5,1 Mt (2008) → 6,1 Mt (2009). https://finance.detik.com/berita-ekonomi-bisnis/d-1042140/4-perusahaan-pasok-batubara-ke-pltu-suralaya
[8] Kupastuntas, 2022-01-09 — Tarahan-medewerker: PTBA-kolen naar PLTU Tarahan, Suralaya, Cirebon (niet constant), Sebalang; geen tonnage. https://www.kupastuntas.co/2022/01/09/stok-batu-bara-di-lampung-dipastikan-aman-untuk-pembangkit-listrik
[9] Kompas.id, 2025-10 — Tarahan = hoofdverscheepshub PTBA, 56 % binnenland (via zoeksamenvatting, betaalmuur). https://www.kompas.id/artikel/pelabuhan-tarahan-lebih-hijau-dan-efisien-di-tengah-debu-batubara
[10] ESDM/Ditjen Minerba, 2012-10-13 — pasokan PTBA aan Suralaya ~12 → ~6 Mt/j (alleen via zoeksamenvatting; site nu in onderhoud). https://www.minerba.esdm.go.id/berita/minerba/detil/20121013-pasokan-batu-bara-untuk-pltu-suralaya-terancam-kritis
[11] OpenStreetMap (ODbL) via Nominatim/Photon — Tarahan-unit node 12198553056 (-5.5095/105.3429, kantoor, niet de kade); landuse "TLS PTBA" (-3.7331/103.7962); stations Muara Enim, Prabumulih, Baturaja, Martapura, Kotabumi, Tarahan; way 531146249 PLTU Suralaya.
[12] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-kolen-tanjungenim-suralaya-{tls,tls-z16,tls-z17,tarahan,tarahan-z16,tarahan-kade-z17,suralaya,suralaya-z16}.png`.
[13] `toets_spoorroute.mjs` (BAKE_SUFFIX=-raw, 3.260.717 spoor-edges) + `hecht_marnet`/`maak_havenaanloop` meetruns 2026-10-09 — spoor 173,0 + 232,1 = 405,1 km; zee 121,9 km; aanlopen 8,2 en 10,7 km.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Bestand:** `v2/data/stroomroute-kolen-tanjungenim-suralaya.json` (contract v2, 25,3 KB) · **recept:** `bak_kolen_tanjungenim_suralaya()` in `v2/tools/bak_stromen.sh` · geen profiel (geen wegbeen).
**Totaal 549,6 km, 6 benen, 1.299 punten, 4 markers.**

| # | modaliteit | km | naad naar vorig | stippel | been |
|---|---|---|---|---|---|
| 1 | spoor | 174,3 | – | nee | PTBA-kolenlijn Tanjung Enim → Baturaja (1-op-1-net, `-raw`) |
| 2 | spoor | 233,5 | 0,00 | nee | Baturaja → Martapura → Kotabumi → Tarahan (1-op-1-net, `-raw`) |
| 3 | zee | 8,2 | 0,69 | ja | haven-aanloop Tarahan (rechte stippel, `maak_havenaanloop` hing 300 s) |
| 4 | zee | 121,9 | 0,00 | nee | zeeschip Tarahan → Suralaya, MARNET zeeknoop 8961 → 8966 (4 edges, 15 punten) |
| 5 | zee | 10,7 | 0,00 | ja | haven-aanloop Suralaya (geroutet over water, geen land) |
| 6 | truck | 1,0 | 0,00 | ja | band steiger → ketelhuizen (last mile, geen net op deze korrel) |

**Toets.** b1 = 174,3 + 233,5 = 407,8 km tegen 420 gepubliceerd = **-2,9 %** (binnen ±15 %; gepubliceerd is een afgeronde bron-opgave uit 2006, geen
operator-meting). b2 doorgetrokken zeeleg 121,9 km; samen met de aanlopen 140,8 km tegen ±100 km = **+41 %** — verwacht en genoteerd (scheve MARNET-zeeknopen,
8,2 en 10,7 km aan de verkeerde kant van de Straat Soenda), niet dichtgetrokken, geen via-punt. Hemelsbreed kade → kade 87 km. Grootste naad 0,69 km
(spoorstaart → Tarahan-kade; < 5 km, geen stippel nodig). Markers: Tarahan, steiger en centrale 0,0 km van de lijn; Tanjung Enim 0,35 km (spoorkop is een
router-vertex op 0,35 km van het laadanker; anker ≠ routeerpunt, < 0,5 km). `toets_knikken`: 1 knik (73,8°, R 6,4 km, open water in de Straat Soenda), 0 omkeringen, 0 terugloop.
`toets_rechte_benen --min-km 5`: alleen de twee haven-aanlopen (stippel mét reden). `json.load`: versie 2, punt_formaat lonlat, modaliteiten {spoor, zee, truck},
elk been >= 2 punten.

**Recept.** Spoor in twee runs (geen `--via` op de spoorrouter), `BAKE_SUFFIX=-raw` (3.260.717 spoor-edges): TLS (-3.7340,103.7908) → Baturaja-station
(-4.1273,104.1620) en Baturaja → Tarahan-emplacement (-5.5140,105.3435), `--max-snap=30`. Baturaja is het enige via-punt en pint de Tarahan-lijn tegen de
Kertapati-aftakking (180 km noord); een vrije Dijkstra gaf al dezelfde lijn, dus de pin borgt alleen. Geen pin op Muara Enim, Prabumulih of Martapura. Zee: router
kade-zeeknoop → zeeknoop met een stippel-aanloop Tarahan (rechte lijn) en een gerouteerde aanloop Suralaya (`kolen-tanjungenim-suralaya-aanloop-suralaya.geojson`).

**Stippels met reden.** (1) Tarahan-aanloop: kade ligt 8,2 km van zeeknoop 8961, `maak_havenaanloop.py` liep op timeout 300 (exit 124), rechte stippel zonder
tweede poging. (2) Suralaya-aanloop: kade 10,7 km van zeeknoop 8966, geroutet over water (omwegfactor 1,001), blijft stippel omdat het geen waargenomen vaargeul is.
(3) b3: transportband over eigen PLN-terrein, geen net op deze korrel. Geen vlucht, geen leiding, geen wegbeen.

**Lessen / open voor centraal.** (a) Het register-id `kolen-ts` (Tanjung Enim → Suralaya) is vrij; de registerregel wordt centraal gezet. (b) Sitelaag-centroïde
`w-tanjung-enim` (-3.7400,103.7683) ligt 2,5 km W van het laadanker en hoort centraal gelijkgetrokken. (c) Het volume van déze as is niet gepubliceerd: de
beennaam draagt "aannemelijk: één bron voor het havenpaar". (d) Suralaya-capaciteit is tegenstrijdig (Wikipedia 4.025 MW versus GEM 6.025 MW incl. unit 9-10) en
niet opgelost. (e) Prabumulih-stationsemplacement ligt 2,0 km naast het spoorpad (de lijn passeert via de Tanjung Rambang-tak): geen probleem voor de toets,
wel een corridorfeit. (f) Procestip: de slot-opruiming in de agent-shell mag geen `rm -rf "$d"` met een samengestelde variabele zijn (door de veiligheidscheck
geweigerd); `mkdir`-slot met literal-pad-`rmdir` werkt.
