# Routebrief (licht) · lithium — Pilgangoora → Port Hedland → Gwangyang (Zuid-Korea)

**stroom-id:** `lithium-pilgangoora-gwangyang` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** hardrock-spodumeenconcentraat van de Pilgan/Ngungaju-plant (Pilbara Minerals, PLS) gaat per **road train** ~120–140 km naar de Utah Point-bulkfaciliteit in Port Hedland, per **bulkcarrier** ~6.000 km via Lombok–Makassar–Zuid-Chinese Zee–Taiwanstraat naar de Gwangyang-haven (Yulchon), en de laatste ~1–2 km per truck naar de hydroxidefabriek van POSCO Pilbara Lithium Solution (P-PLS) — Korea's eerste spodumeen-hydroxidefabriek — met (aannemelijk, één bron) een laatste stap naar de kathodefabriek van POSCO Future M op hetzelfde Yulchon-complex.
**Welke as van het verhaal:** de omweg om China heen — Australisch concentraat rechtstreeks naar een Koreaanse converter i.p.v. via een Chinese raffinaderij. PLS produceerde FY25 754,6 kt spodumeenconcentraat (P1000 → 1 Mt/j capaciteit sinds 2025) [1][10]; P-PLS is genormeerd op 43 kt LiOH/j maar draaide in het juni-kwartaal 2026 op batchbasis: 882 t (trein 1) + 2.679 t (trein 2) = 3,56 kt/kwartaal ≈ **14 kt LiOH/j ≈ 12 kt LCE** [8] — dat gemeten tempo draagt de brief, niet de 43 kt nameplate.

## 1 · Ketenkaart
```
Pilgan/Ngungaju-plant `li-pilgangoora-plant` ──(b1 truck · Great Northern Hwy → Utah Road · ~120–140 km)──►
Utah Point-berth `li-porthedland-utahpoint` (aannemelijk)
   ──(b2 zee · Lombok–Makassar–ZCZ–Taiwanstraat–OCZ · ~6.000 km, MARNET)──►
Gwangyang-kade `li-gwangyang-kade` (onzeker) ──(b3 truck · havenweg Yulchon · ~1,3 km, eigen terrein)──►
P-PLS hydroxidefabriek `li-gwangyang-pls`
   ──(b4 truck · binnen het complex · <1 km, aannemelijk: één bron)──► POSCO Future M kathodefabriek ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (road trains, Qube) | `li-pilgangoora-plant` → `li-porthedland-utahpoint` | mijnweg → Marble Bar Rd → Great Northern Hwy → Utah Road | ~120–140 [2][5] | maak_stroombeen_weg (extract australie; refs GNH/Marble Bar Rd/Utah Rd) | nee |
| b2 | B | zee (bulkcarrier) | `li-porthedland-utahpoint` → `li-gwangyang-kade` | Lombok/Makassar–Zuid-Chinese Zee–Taiwanstraat–Oost-Chinese Zee (MARNET beslist) | ~6.000 hemelsbreed, geen publicatie | MARNET | aanloop: waarschijnlijk aan beide kanten (AU-binnenkant geen graaf; Gwangyang-zeeknoop ~25 km) |
| b3 | C | truck (havenweg, kort) | `li-gwangyang-kade` → `li-gwangyang-pls` | Yulchon-havenweg | ~1,3 (hemelsbreed) | stippel "eigen terrein" (< 2 km, geen net op deze korrel) | ja — eigen terrein |
| b4 | D | truck (aannemelijk: één bron) | `li-gwangyang-pls` → POSCO Future M kathodefabriek | binnen het Yulchon-complex | < 1 | stippel "eigen terrein, aannemelijk" | ja — eigen terrein + aannemelijk |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-pilgangoora-plant` | mijn / concentratorplant | Pilgan-plant, Pilgangoora Operation (PLS) | -21.0595, 118.8956 | [1][2][11] | bron-gelegd (z15 gezien: verwerkingsgebouwen, tanks, twee grote witte tailings-ovals en meerdere open pits met de kenmerkende turquoise/witte pegmatiet-uitgravingen, exact op het OSM-landuse-vlak "Pilgangoora Lithium Mine") |
| `li-porthedland-utahpoint` | laadkade (bulk) | Utah Point Bulk Handling Facility, Port Hedland (Berth 4, Qube/PPA) | -20.3153, 118.5585 | [3][4][6][12] | aannemelijk (z15 gezien: rail/wegknoop met stockyard en een pier die de haven in loopt bij "Utah Point Road"; welke specifieke berthstructuur de lithium-lader is, is op dit beeld niet te onderscheiden — Lumsden Point is vanaf medio 2026 een alternatief, zie §7) |
| `li-gwangyang-kade` | losplek (bulk, vermoedelijk) | Yulchon-havenfront, Gwangyang (Jeollanam-do) | 34.9075, 127.6020 | [7][13] | onzeker (z15 gezien: kade/pier direct naast het industriecomplex met blauwe loodsdaken; welke kade concentraat losbulk afhandelt is niet gedocumenteerd en de nieuwste satellietopname toont mogelijk nog bouwactiviteit) |
| `li-gwangyang-pls` | fabriek (fase C→D) | POSCO Pilbara Lithium Solution (P-PLS), Yulchon-industriecomplex, Suncheon/Gwangyang | 34.9008, 127.5911 | [7][9][13] | bron-gelegd (z14 gezien: industriecomplex met tientallen blauw-/wit-daken hallen op het Yulchon-terrein; adres 율촌산단3로 77 valt binnen dit vlak, individuele hal niet te onderscheiden op dit zoomniveau) |
| `li-gwangyang-futurem` | fabriek (fase D, aannemelijk) | POSCO Future M — kathodefabriek, Yulchon-industriecomplex | 34.8985, 127.5885 | [14] | aannemelijk (adres 율촌포스코미래로 45, één straat verderop dan P-PLS op hetzelfde complex; niet apart satelliet-gelegd) |

## 4 · Via-punten (alleen b1 — corridorkeuzes op de weg)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | mijnweg × Marble Bar Road | -21.00, 118.92 | verlaat het mijnterrein op de enige publieke aansluitweg (i.p.v. een interne pittrack) |
| b1 | 2 | Strelley — Marble Bar Rd × Great Northern Hwy | -20.5162, 118.9512 | pint de afslag naar het NW op de GNH i.p.v. doorrijden naar Marble Bar/Nullagine |
| b1 | 3 | South Hedland (GNH-doorgang) | -20.4088, 118.5987 | corridor blijft op de GNH-doortocht i.p.v. een stadsomleiding |
| b1 | 4 | Utah Road-afslag vanaf GNH | -20.320, 118.565 | "Utah Road = de enige verbinding GNH → Utah Point" [4] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| P-PLS Chemical Facility (Yulchon) | POSCO Pilbara Lithium Solution (POSCO Holdings 82 % / PLS 18 %, optie tot 30 %) | spodumeenconcentraat → LiOH·H2O | nameplate 43 kt LiOH/j (2 treinen); juni-kwartaal 2026 batchbedrijf: 3,56 kt/kwartaal ≈ 14 kt/j ≈ 12 kt LCE | [7][8][9] |

Status: fabriek 1 geopend eind 2023, fabriek 2 (samen 43 kt) voltooid 29-11-2024 [7]; medio 2026 nog op batchbasis, opvoeren richting nameplate niet gedateerd [8].

## 6 · Stoppunt
De brief stopt bij POSCO Future M's kathodefabriek op het Yulchon-complex: dat is de enige met naam genoemde afnemer op locatie (fase D, aannemelijk — één bron zegt dat de hele keten "op één plek" zit [9]); geen bron noemt de battery-cel- of automaker die de kathode afneemt, dus fase E vervalt.

## 7 · Open punten
- **Utah Point-berth niet met naam bevestigd voor lithium:** Qube trucking Pilgangoora → Port Hedland is bevestigd [5], maar geen bron noemt letterlijk welke berth-structuur het concentraat verscheept; vanaf medio 2026 verhuist batterijmetaal mogelijk (deels) naar het nieuwe **Lumsden Point** (eerste wharf medio 2026, tweede later in 2026) [15] — niet getekend, wél hier genoemd.
- **AU-binnenkant zonder MARNET-graaf:** zeeknoop 79 km buitengaats → aanloop via `maak_havenaanloop.py`, terugval rechte stippel.
- **Gwangyang-zeeknoop ~25 km van Yulchon** (op de grens van `--max-snap`) → aanloop nodig; **kade-anker onzeker** (§3) — welke kade concentraat/bulk lost is niet gedocumenteerd.
- **Jaarlijkse tonnage Australië → Korea niet gepubliceerd:** het zeebeen draagt de P-PLS-capaciteit (gemeten 2026-tempo), niet een gemeten ladingstroom; PLS levert ook aan Ganfeng, Yahua en Chengxin onder dezelfde offtake-structuur.
- **Fase D (P-PLS → POSCO Future M) niet apart satelliet-gelegd** — beide fabrieken staan op hetzelfde Yulchon-complex met opeenvolgende straatadressen (율촌산단3로 77 resp. 율촌포스코미래로 45); geen bron geeft het exacte volume dat overgaat.
- **b3/b4 als "eigen terrein"-stippels:** de havenwegen/estatewegen binnen Yulchon zijn niet als publieke corridor gecontroleerd; blijkt bij het bakken of het extract `zuid-korea` ze draagt.

## 8 · Bronnen
[1] PLS, Pilgangoora Operation — 1 Mt/j capaciteit na P1000, 10 % wereld hardrock-aanbod, ~140 km ZO van Port Hedland. https://www.pls.com/assets/pilgangoora-operation
[2] E&MJ/Mining Technology-achtige mijnbeschrijving via PLS-assets; PLS FY26 Full Year Results (record productie). https://www.pls.com/news/pls-fy26-results
[3] Pilbara Ports Authority, Port facilities — Utah Bulk Handling Facility / PH No.4 berth, Qube-multi-user faciliteit. https://www.pilbaraports.com.au/ports/port-of-port-hedland/port-operations/port-facilities
[4] Ventia, Utah Road-upgrade — "Utah Road = de enige verbinding GNH → Utah Point". https://www.ventia.com/newsroom/news/ventia-delivers-critical-upgrade-to-utah-road-for-pilbara-ports-authority
[5] PHIC, Qube/Pilbara Minerals trucking Pilgangoora → Port Hedland (geen specifieke berth genoemd). https://www.phic-hedland.com.au/2024/12/10/qube-pilbara-minerals-keep-on-trucking/
[6] DER (WA), Decision Report L8937/2015/1 — "Port Hedland Berth 4 – Utah Point", site code S0023400. https://www.der.wa.gov.au/images/documents/our-work/licences-and-works-approvals/Decisions_/L8937_2015_1_ODR.pdf
[7] POSCO Newsroom, 29-11-2024 — voltooiing 2e hydroxidefabriek Yulchon, 21.500 t/j, totaal 43.000 t/j. https://newsroom.posco.com/en/posco-holdings-leads-the-charge-in-rechargeable-battery-material-sovereignty-with-the-comprehensive-completion-of-the-korean-lithium-hydroxide-plant/
[8] PLS, June 2026 Quarterly Activities Report — P-PLS batchproductie 882 t (trein 1) + 2.679 t (trein 2). https://www.pls.com/storage/announcements/june-2026-quarterly-activities-report-2026-07-30.pdf
[9] PLS, P-PLS Chemical Facility — PLS 18 % (optie 30 %), POSCO-partner, capaciteit 43.000 t/j LiOH, "eerste commerciële spodumeen-hydroxidefabriek in Zuid-Korea". https://www.pls.com/assets/p-pls-chemical-facility
[10] Argus Media, 2025 — Pilbara Minerals FY25 spodumeenproductie +4 %. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2715512-pilbara-minerals-lifts-spodumene-output-by-4pc-in-fy25
[11] OpenStreetMap (ODbL) via Photon — landuse "Pilgangoora Lithium Mine" -21,05945/118,89557. https://www.openstreetmap.org
[12] World Ports Directory / Marinelink — Port Hedland 20°18'S 118°34'E. https://ports.marinelink.com/ports/port/port-hedland
[13] posco-lithium.com, Directions — adres P-PLS: 전남 순천시 해룡면 율촌산단3로 77, Yulchon-industriecomplex. https://www.posco-lithium.com/page/directions
[14] POSCO Future M, persbericht toegangsweg-naamswijziging — adres kathodefabriek Gwangyang: 율촌포스코미래로 45 (was 율촌산단로 45), zelfde Yulchon-complex als P-PLS. https://www.poscofuturem.com/pr/view.do?num=761
[15] Pilbara Ports Authority, Lumsden Point-project — eerste wharf medio 2026. https://www.pilbaraports.com.au/business-and-trade/current-projects/lumsden
[16] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15, live) — `v2/build-cache/satcheck/sat-lithium-pilgangoora-gwangyang-plant.png`, `sat-lithium-pilgangoora-gwangyang-utahpoint2.png`, `sat-lithium-pilgangoora-gwangyang-yulchon.png`, `sat-lithium-pilgangoora-gwangyang-yulchon-kade.png`.

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `lithium-pilgangoora-gwangyang`** → `v2/data/stroomroute-lithium-pilgangoora-gwangyang.json` — 8 benen, **6.843,1 km**, 1.670 punten, 5 markers. truck 136,5 + 0,4 (stippel) + 8,7 = 145,6 km · zee 80,5 (stippel) + 6.579,7 + 35,8 (stippel) = 6.696,0 km · truck (fase C/D, stippel) 1,2 + 0,3 = 1,5 km.
Recept: `bak_stromen.sh` (functie `bak_lithium_pilgangoora_gwangyang`).

**b1 (truck, twee wegscans + een korte stippel):** profielen `lithium-pilgangoora-gwangyang-plant-southhedland` en `-southhedland-utahpoint` in `maak_stroombeen_weg.py` (extract `australie`, `--bron geofabrik`). ⚠️ De Dijkstra weigerde eerst in één stuk ("geen wegpad tussen punt 1 en 2"): het via-punt "mijnweg × Marble Bar Road" (−21,00/118,92, uit de brief) snapte op een geïsoleerd mijn/Wodgina-wegennetje (247 knopen, unclassified/service met `access=private`) dat zonder `eindToegangPrivaat: True` niet aansluit. Met die vlag én `corridorKlassen: ["unclassified","tertiary","service","residential"]` (de kleine klassen tussen plant en Marble Bar Road liggen buiten de 12 km-eindzone van beide ankers) routeert de eerste helft door: 136,5 km. Ná die fix bleef één gat staan tussen "South Hedland (GNH-doorgang)" en "Utah Road-afslag": de Great Northern Highway bestaat in OSM als **twee componenten die geen knoop delen** — het doorgaande GNH-net (naar de mijn) en het stadsnet van Port Hedland (Wilson St, Utah Road, de haven) — kleinste gemeten afstand tussen beide **0,355 km**, bij (−20,377913;118,575136) ↔ (−20,374731;118,574874), gemeten met een BFS over de gebouwde graaf (niet een wegklasse-fout: beide zijden zijn zelf `trunk`). Opgelost als korte `--stippel` tussen twee aparte wegscans, geen coördinaat verzonnen. b1-totaal **145,6 km tegen 130 gepubliceerd (midden van 120–140) = +12,0%, binnen ±15%**.
**b2 (zee):** kop en staart liggen allebei te ver van een MARNET-zeeknoop voor een directe `--been` (Utah Point 79,7 km, Yulchon 29,7 km — op de grens van `--max-snap` 25 km) → twee geslaagde `maak_havenaanloop.py`-runs (geen timeout, geen terugval nodig): aanloop Utah Point 80,5 km (73 punten, 0,00 km over land) en aanloop Yulchon 35,8 km (32 punten, 0,00 km over land, gebouwd in aankomstrichting zeeknoop→kade zodat de keten-volgorde klopt). Het MARNET-zeebeen zelf komt op **6.579,7 km** (682 punten, 45 MARNET-edges, lengte-invariant getekende lijn vs edge-som −0,208 km = de naden) — **buiten de bak-aanwijzing "5.900–6.300 km"**, een bevinding (+4,4% boven de bovengrens, +9,7% boven de ~6.000 km hemelsbreed uit de brief): MARNET kiest zelf de route (Lombok/Makassar–Zuid-Chinese Zee–Taiwanstraat–Oost-Chinese Zee) en dat commando is niet aangepast om het venster te halen.
**b3/b4 (stippel "eigen terrein"):** kade → P-PLS 1,242 km, P-PLS → POSCO Future M 0,349 km — beide als rechte stippel, geen scan (§7-conventie: "geen net op deze korrel"/"aannemelijk: één bron" staan in de beennaam, niet in de lijnstijl).
**Toets:** naden tussen alle acht opeenvolgende benen **0,000 km** (het naad-script uit de handleiding); `toets_knikken.py` geeft 18 knikken ≥60° over de hele stroom, waarvan **1 terugloop** (172°, straal 7 m, bij −20,40840/118,59852 — een klein residu vlak bij het "South Hedland (GNH-doorgang)"-via-punt, ná de automatische `snoei_keerlussen`-pass die twee grotere lussen op dezelfde plek al verwijderde; km-impact verwaarloosbaar, niet dichtgeschoven); `toets_rechte_benen.py --min-km 5` vindt **geen** been van deze stroom (alle stippels < 5 km, geen ongeteste rechte lijn ≥5 km); json geldig (versie 2, punt_formaat lonlat, alle modaliteiten in {truck, zee}, elk been ≥2 punten, 35,1 KB); alle 5 markers op 0 m van hun been (anker = routeerpunt op elk van de vijf).

**Gereedschapslessen:**
- Een geïsoleerd privé-mijnwegennetje (unclassified/service, `access=private`) sluit alléén aan op het publieke net met `eindToegangPrivaat: True`; zonder die vlag geeft de Dijkstra "geen wegpad" ook al ligt de snap-afstand ruim binnen 25 km — de fout zit in de klasse/toegang, niet in de via-puntligging.
- `corridorKlassen` is soms nodig ver van beide ankers: de standaard-eindzone (12 km) geldt alleen bij plant/kade, en een lang stuk kleine-klasse-weg daartússen (hier ~55 km hemelsbreed tot Marble Bar Road) blijft anders buiten de graaf, zelfs met `eindToegangPrivaat`.
- Twee delen van dezelfde genoemde snelweg (`Great Northern Highway`, `trunk`) kunnen in OSM losse graafcomponenten zijn zonder gedeelde knoop — een BFS-component-check (niet alleen de snap-afstand per via-punt) is de enige manier om dat te vinden vóórdat de Dijkstra het als "geen wegpad" meldt. Bij een klein gemeten gat (hier 0,355 km) is een korte `--stippel` tussen twee aparte wegscans de eerlijke oplossing — geen via-punt verschuiven, geen coördinaat verzinnen.
- Een haven-aanloop die ná een `--been zee` komt (aankomstrichting) moet met `--van`/`--naar` in de **omgekeerde** volgorde (zeeknoop → kade) gedraaid worden: `_geojson_been()` leest de punten letterlijk in bestandsvolgorde en keert niets automatisch om.
- De bak-aanwijzing "toets alleen de bake-uitkomst tegen 5.900–6.300 km" is precies daarom een venster en geen harde eis: MARNET's eigen keuze (6.579,7 km) valt erbuiten zonder dat er iets fout is aan de invoer — dat hoort in §9 te staan, niet te worden dichtgetrokken door een ander vaarpunt te forceren.
