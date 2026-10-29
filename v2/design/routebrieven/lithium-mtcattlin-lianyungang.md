# Routebrief (licht) · Lithium — Mt Cattlin → Esperance → Lianyungang (Australië → China)

**stroom-id:** `lithium-mtcattlin-lianyungang` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat van de Mt Cattlin-mijn bij Ravensthorpe (Galaxy Resources, later Allkem/Arcadium) gaat per road train
(Qube) ~187 km over de South Coast Highway naar het Port of Esperance (Berth 3) en daarna per bulkschip (8.840 km, route volgens MARNET) naar Lianyungang
(Jiangsu): de eerste lading (10.000 t, 2 jan 2017, NY Trader 1) is de enige bron voor de zeebestemming, dus **aannemelijk: één bron**.
**Welke as van het verhaal:** *de kleine Westaustralische hardrock-mijn die in 2017 de Esperance-exportroute opende, met China als eerste afnemer* — het
tegenstuk van Mt Marion (zelfde haven, ander landbeen). Volume: **~28 kt LCE/j** (191.570 dmt spodumeenconcentraat ≈ SC6 in 2019 × 0,148), peiljaar 2019 [6];
de mijn staat sinds juli 2025 in care and maintenance [2] — de lijn toont het peiljaar, geen huidige stroom.

## 1 · Ketenkaart
```
Mt Cattlin-plant `li-mtcattlin-plant` ──(b1 truck · South Coast Hwy · 187 km publicatie, 196,8 km gemeten)──► Port of Esperance Berth 3 `li-esperance-kade`
──(b2 zee-stippel · haven-aanloop 70,6 km, schematisch)──► MARNET-zeeknoop 2478 ──(b3 zee · Lombok/Makassar · router 8.840 km, aannemelijk: één bron)──►
Lianyungang-havenmond `li-lianyungang-haven` ⏹ stoppunt (kade/terminal niet gevonden, geen fase D/E)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (concentraat, Qube road trains) | `li-mtcattlin-plant` → `li-esperance-kade` | mijnweg → Ravensthorpe Heavy Haulage Route → South Coast Highway (State Route 1) → Harbour Road (bypass) | **187 km** (Australian Mining Review 2017, mijn→Esperance) [4]; OSRM 197,9 [9]; **hemelsbreed 177 km, geen wegkm**. Gemeten 196,8 = +5,2 % | maak_stroombeen_weg (extract australie) | nee |
| b2 | B | zee (aanloop) | `li-esperance-kade` → MARNET-zeeknoop 2478 (-34.5000, 121.8000) | Esperance-baai, Recherche-archipel | 70,6 km hemelsbreed (kade ↔ zeeknoop) | rechte stippel, schematisch: `maak_havenaanloop.py` gaf in de haalbaarheidstoets een timeout (280 s) — geen tweede poging | **ja** (net reikt niet) |
| b3 | B | zee | zeeknoop 2478 → zeeknoop 5820 (34.7303, 119.5052) | Westkust WA noordwaarts → Lombok → Makassar → Celebeszee → Zuid-Chinese Zee → Taiwanstraat → Gele Zee (router-uitkomst, geen bron) | **router 8.840,6 km** (hemelsbreed ~7.620); geen gepubliceerde zeekm | MARNET (kade→kade) | nee — **aannemelijk: één bron** in de beennaam |

*Geen haven-aanloop bij Lianyungang en geen last mile: de kade is niet gevonden en de lijn eindigt waar het bewijs eindigt (zeeknoop 5820).*

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-mtcattlin-plant` | mijn / concentrator | Mt Cattlin (Galaxy → Allkem → Arcadium), 2,2 km N van Ravensthorpe | -33.5625, 120.0204 | de OSM-mijnpunt (-33.5612, 120.0304) ligt in de put [1]; plant 1 km westelijker, eigen z15-blik [11] | **bron-gelegd** (z15 gezien: kruis op het procesblok — gebouwen, tanks en stapels — tussen de tailingsdam in het westen en de open dagbouwputten in het oosten, binnen het mijnterrein) |
| `li-esperance-kade` | overslag / laadkade | Port of Esperance, Berth 3 | -33.8711, 121.9024 | **hergebruik letterlijk** uit `lithium-mtmarion-esperance.md` §3 (Southern Ports: Berth 3 = iron ore en spodumeen [13]) | **bron-gelegd** (door de brief van Mt Marion, z17: dolphin-pier met bandtrestle en shiploader). Dat Cattlin dezelfde berth gebruikt is niet gebrond — Esperance Port wel [4][5], de berth niet |
| `li-lianyungang-haven` | aanlanding (routeeinde, **geen kade**) | Lianyungang, havenmond = MARNET-zeeknoop 5820 | 34.7303, 119.5052 | knoop 5820 uit `ports.json` (LOCODE CNLYG ligt 5,1 km westelijker, 34.733/119.450) [16]; geen bron noemt een berth | **onzeker** (z14-blik [11]: open haven-/dijkmond naast ertsterminals en een nieuw opgespoten dijkvlak; welke berth de lading kreeg is niet vastgesteld) |

## 4 · Via-punten (b1 — South Coast Highway)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | South Coast Hwy oost van Ravensthorpe | -33.5779, 120.0565 | na de Heavy Haulage Route-afslag; pint **oostwaarts** (Esperance) i.p.v. westwaarts naar Albany; op de highway, buiten het dorp |
| b1 | 2 | South Coast Hwy bij Munglinup | -33.7136, 120.8795 | houdt de lijn op de highway naast de kustwegen (Hopetoun, Munglinup Beach Rd) |
| b1 | 3 | South Coast Hwy, ten oosten van Munglinup | -33.7568, 121.1790 | idem, langs het rechte middenstuk |
| b1 | 4 | South Coast Hwy bij Gibson Soak | -33.6954, 121.4941 | idem; vóór de samenkomst met de Coolgardie–Esperance Hwy |
| b1 | 5 | South Coast Hwy vóór Esperance | -33.7877, 121.7914 | laatste punt voor de haven; buiten de stad |
| b1 | 6 | Harbour Road (bypass, Chadwick) | -33.8462, 121.8866 | **corridorkeuze:** Harbour Rd-bypass naar de haven i.p.v. via de Esplanade door het centrum — letterlijk uit Mt Marion hergebruikt |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mt Cattlin-concentrator | Galaxy Resources (2009–2021), daarna Allkem/Arcadium | erts → spodumeenconcentraat (5,5–6 % Li2O) | 800 kt erts/j nameplate; 191.570 dmt SC in 2019 ≈ 28 kt LCE | [1][4][6] |
| Port of Esperance (Qube-haulage, rotabox-systeem) | Southern Ports / Qube | opslag → bulkschip | 33.000 dmt in 2020; eerste lading 10.000 t | [4][5] |

## 6 · Stoppunt
De brief stopt bij de Lianyungang-havenmond: geen bron noemt de kade of de converter (de latere offtakes zijn Yahua en Sichuan Chengtun, niet in Lianyungang [5]), dus er is geen fase D/E.

## 7 · Open punten
- **Alleen de eerste lading (2017) is bron voor Lianyungang** [2][3][4]; koper niet genoemd, latere afnemers wijken af [5] → beennaam "aannemelijk: één bron".
- **Lianyungang-kade/terminal ongevonden** (geen OSM-, Nominatim- of bronhit; Lianyungang heeft vier havengebieden, Xuwei is niet bevestigd [12]). De lijn eindigt op zeeknoop 5820.
- **Berth op Esperance niet gebrond** voor Cattlin; Berth 3 is een hergebruik uit Mt Marion en aanname.
- **Geen gepubliceerde zeekm**; 8.840 km is router-uitkomst, de Makassar-/Lombok-corridor is routerkeuze, geen bron.
- **Productiejaar 2019** komt uit een zoekresultaat (NS Energy-profiel, niet geopend) en de Wikipedia-infobox [6]; de ontwerpbron "Galaxy Resources (Wikipedia)" bevat het cijfer niet.
- **Mijn stil sinds juli 2025** [2]; Mt Cattlin-pagina noemt eigenaar Arcadium; SEC-resultaten (Q4 2025) niet geopend.
- Aanloop Esperance is een rechte stippel (70,6 km, schematisch) — kan de Recherche-eilanden snijden; tool-timeout, geen tweede poging.
- v1 (`data/lithium.js`, `lithium.md`) kent Mt Cattlin niet; de sitelaag (`lithium-sitelaag.json`) ook niet — kandidaat-site `w-li-mtcattlin` (-33.5625, 120.0204, ~28 kt LCE, peiljaar 2019).

## 8 · Bronnen
[1] Wikipedia, Mt Cattlin mine (spodumeen-tantaal, 2,2 km N van Ravensthorpe; herstart 31-3-2016; eerste lading jan 2017 Esperance → Lianyungang) — https://en.wikipedia.org/wiki/Mt_Cattlin_mine
[2] Wikipedia, Ravensthorpe, Western Australia (10.000 t jan 2017 Esperance → Lianyungang; care and maintenance juli 2025) — https://en.wikipedia.org/wiki/Ravensthorpe,_Western_Australia
[3] ABC Rural, 2017-01-03: eerste lading 10.000 t, NY Trader 1, Esperance 2 jan 2017, Lianyungang, US$6 mln — https://www.abc.net.au/news/rural/rural-news/2017-01-03/galaxy-resources-waves-off-first-lithium-shipment/8159118
[4] Australian Mining Review, 2017-04-03, Galaxy riding the wave (Esperance 187 km vs Bunbury 483 km; Qube-haulage; NY Trader1 → Lianyungang; goedkeuring 26-10-2016) — https://australianminingreview.com.au/features/galaxy-resources-riding-the-wave/
[5] Mining-Technology, Mt Cattlin Lithium Project (haulage via de South Coast Highway door Qube; offtakes Yahua 120 ktpa, Sichuan Chengtun 60 ktpa) — https://www.mining-technology.com/projects/mt-cattlin-lithium-project/
[6] NS Energy Business, Mt Cattlin profiel (191.570 dmt in 2019) — https://www.nsenergybusiness.com/?p=279275 (via zoekresultaat, niet geopend)
[7] Wikipedia, Galaxy Resources (Mt Cattlin; fusie Orocobre → Allkem 2021) — https://en.wikipedia.org/wiki/Galaxy_Resources
[8] Wikipedia, South Coast Highway (592 km, Esperance–Walpole, Highway 1) — https://en.wikipedia.org/wiki/South_Coast_Highway
[9] OSRM (project-osrm.org), plant → havenweg: 197,9 km (South Coast Hwy → Harbour Rd), opgevraagd 2026-10-29 — http://router.project-osrm.org
[10] OpenStreetMap (ODbL) via OSRM-geometrie en `wegscan_puur.py` op de Geofabrik-extract australie
[11] Esri World Imagery via `sat_check.py` — `v2/build-cache/satcheck/sat-lithium-mtcattlin-lianyungang-plant.png` (z15), `…-lianyungang.png` (z14)
[12] Wikipedia, Port of Lianyungang (vier havengebieden Lianyun/Ganyu/Xuwei/Guanyun) — https://en.wikipedia.org/wiki/Port_of_Lianyungang
[13] `v2/design/routebrieven/lithium-mtmarion-esperance.md` §3/§8 — Berth 3-anker en Southern Ports-berthpagina
[14] MARNET (`v2/build-cache/marnet-preais`) — zeeknopen 2478 (70,6 km van Berth 3) en 5820; router-uitkomst 8.840,6 km
[15] `v2/data/ports.json` — Lianyungang LOCODE-positie 34.733, 119.450; zeeknoop 5820 op 5,1 km

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
**Stroom:** `v2/data/stroomroute-lithium-mtcattlin-lianyungang.json` (39,7 KB, versie 2, lonlat) · **totaal 9.108,3 km** · 3 benen · 3 markers · 1.928 punten · functie `bak_lithium_mtcattlin_lianyungang` (`bash v2/tools/bak_stromen.sh lithium-mtcattlin-lianyungang`).

| # | modaliteit | km | naad | stippel | been |
|---|---|---|---|---|---|
| b1 | truck (doorgetrokken, gemeten) | 197,1 (weggeometrie 196,8 + 0,14 plant→weg + 0,15 weg→kade) | start op plant | nee | vrachtwagen (road train) Mt Cattlin → Port of Esperance Berth 3 (South Coast Highway, Harbour Road; gepubliceerd 187 km) |
| b2 | zee, haven-aanloop | 70,6 | 0 | **ja** (schematisch) | haven-aanloop Esperance, Berth 3 → MARNET-zeeknoop 2478 (-34.5000, 121.8000) |
| b3 | zee (MARNET-router) | 8.840,6 | 0 | nee | bulkschip Esperance → Lianyungang (aannemelijk: één bron), zeeknoop 2478 → zeeknoop 5820 |

- **Markers (3):** Mt Cattlin-plant (-33.5625, 120.0204), Port of Esperance Berth 3 (-33.8711, 121.9024) en Lianyungang-havenmond = zeeknoop 5820 (34.7303, 119.5052); alle drie 0,0 km van de lijn.
- **Toets:** b1 196,8 km (weggeometrie) tegen 187 gepubliceerd = **+5,2 %** (OSRM 197,9; hemelsbreed 177 is geen wegkm), binnen ±15 %. Naden 0 (max 0,0 km). `toets_knikken`: 17 knikken >= 60 gr, 0 omkeringen, 0 terugloop; de knikken zitten bij de Harbour Road/havenrotondes (Esperance), de mijnafslag en twee spikes op 1,1 N 119,5 O in b3 (MARNET-router-eigenschap, niet aangeraakt). `toets_rechte_benen --min-km 5`: alleen de bedoelde stippel b2 (70,6 km) wordt gemeld. JSON-check: versie 2, punt_formaat lonlat, modaliteiten {truck, zee}, elk been >= 2 punten.
- **Recept:** profiel `lithium-mtcattlin-lianyungang-cattlin-esperance` in `maak_stroombeen_weg.py` (extract australie, vensterKm 50, refs South Coast Highway / 1 / Harbour Road, corridorKlassen tertiary+unclassified, trimStaart, eindToegangPrivaat, 6 via-punten uit §4 + plant en kade als eindpunten, snaps <= 0,01 km behalve plant 0,14 en kade 0,15). Wegscan via `wegscan_puur.py`, 268 s op de 953 MB pbf; 8 keerlussen gesnoeid (197,0 -> 196,8 km); uitvoer `v2/build-cache/ais/graaf/lithium-mtcattlin-lianyungang-weg-cattlin-esperance.geojson`.
- **Stippel b2 (reden):** Berth 3 ligt 70,6 km van zeeknoop 2478 en `maak_havenaanloop.py` gaf in de haalbaarheidstoets een timeout (280 s); geen tweede poging, dus een rechte stippel "hier reikt het net niet". De rechte lijn kan de Recherche-archipel snijden (schematisch).
- **Geen aanloop/last mile bij Lianyungang:** kade niet gevonden; de lijn eindigt op zeeknoop 5820 (onzeker). Geen kopie, geen lucht, geen leiding.
- **Beennaam b3:** "aannemelijk: één bron" (alleen de eerste lading van jan 2017 noemt Lianyungang); b3 is doorgetrokken, niet gestippeld.
- **Bevinding:** de mijnafslag geeft een scherpe hoek (78 gr, 98 m straal) vlak bij de plant (-33.5761, 120.0121); echte wegbocht van de Heavy Haulage Route, geen terugloop.
- **Les:** een Westaustralisch road-train-been naast Mt Marion vraagt hetzelfde profiel (corridorKlassen voor de mijnweg, Harbour Road-bypass als laatste via); het profiel van Mt Marion is een goede sjabloon. Sitelaag en v1 kennen Mt Cattlin niet (kandidaat `w-li-mtcattlin`).
