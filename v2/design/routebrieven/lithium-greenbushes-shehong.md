# Routebrief (licht) · Lithium — Greenbushes → Bunbury → Yangtze → Chongqing → Shehong (Sichuan)

**stroom-id:** `lithium-greenbushes-shehong` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat uit de Greenbushes-mijn gaat per truck 83,1 km naar Bunbury Berth 8 (letterlijke kopie `lithium-greenbushes-zhangjiagang` b1), per bulkcarrier 7.606,6 km over MARNET naar de Yangtze-monding (kopie), per binnenschip 2.243,4 km de Yangtze op naar de Guoyuan-bulkkade bij Chongqing (aannemelijk: geen bron voor barge) en per truck ~254 km over de Chongqing-rondweg (G5001) en de G93 naar de Tianqi-fabriek in Shehong; de lijn eindigt op het fabrieksanker.
**Welke as van het verhaal:** *Tianqi (Talison-eigenaar) voert Greenbushes-concentraat naar zijn eigen Sichuan-raffinagekern.* WoodMac bevestigt dat Shehong "spodumene concentrate feedstock from the integrated Greenbushes mine" gebruikt [1]. Volume (peiljaar FY2025): Greenbushes ≈ **200 kt LCE/j** [9]; het Shehong-aandeel is niet gepubliceerd; de fabriek heeft nameplate 14,5 kt carbonaat + 5 kt hydroxide + 4,5 kt chloride (SMM, 2023) [2].

## 1 · Ketenkaart
```
Greenbushes-loods `li-gb-laadplek` ──(b1 truck · Maranup Ford Rd → South Western Hwy · 83,1 km, KOPIE zhangjiagang b1)──►
Bunbury Berth 8 `li-bun-berth8` ──(b2 zee · Lombok/Makassar, Taiwanstraat · 7.606,6 km, KOPIE zhangjiagang b2; aannemelijk: één bron)──►
MARNET-eindknoop (31.51, 121.4187) ──(b3 overgang stippel 8,6 km, KOPIE)──► Yangtze-monding `li-yangtze-monding`
──(b4 binnenvaart · Nanjing, Wuhan, Drie Klovendam · 2.243,4 km bulklaag; aannemelijk: geen bron voor barge)──►
Guoyuan-bulkkade Chongqing `li-guoyuan-bulkkade` ──(b5 truck · G5001 rondweg → G93 via Tongnan, Suining · ~254 km; aannemelijk)──►
Tianqi Lithium Shehong `li-shehong-tianqi` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `li-gb-laadplek` → `li-bun-berth8` | Maranup Ford Rd → South Western Hwy | **83,1 gemeten** (gepubliceerd ±90, −7,9%) [8] | letterlijke kopie `stroombeen-greenbushes-bunbury.geojson` (functie `bak_lithium`) | nee |
| b2 | B | zee | `li-bun-berth8` → MARNET-eindknoop 31.51,121.4187 | Lombok/Makassar, Taiwanstraat (MARNET beslist) | **7.606,6 gemeten** (MARNET; geen publicatie) [8] | letterlijke kopie van de zee-regel in `bak_lithium`; start snapt 4,93 km van de kade (<5 km, bekende Bunbury-naad) | nee |
| b3 | B | zee (overgang) | MARNET-eindknoop → 31.4512,121.4769 | — | 8,6 hemelsbreed | letterlijke kopie van de overgangsstippel in `bak_lithium` | ja — MARNET houdt op |
| b4 | C | binnenvaart (aannemelijk: één bron voor Shehong↔Greenbushes, géén bron voor barge naar Chongqing) | 31.4512,121.4769 → `li-guoyuan-bulkkade` | Yangtze via Nanjing, Wuhan, Drie Klovendam | **2.243,4 gemeten** (268 edges, 11.697 pt); ±2.400 Shanghai–Chongqing is eigen kennis zonder bron, dus −6,5% is een indicatie [7] | `maak_rivierbeen.py` over de bulklaag; eindigt 0,57 km van het anker | nee |
| b5 | C | truck (aannemelijk) | `li-guoyuan-bulkkade` → `li-shehong-tianqi` | G5001 (rondweg) → G85 → G93 (Chengyu-ring) via Tongliang, Tongnan, Suining → Shehong | **geen wegkm gepubliceerd**: hemelsbreed 198 km, geen wegkm; gemeten 254,2 (+28% op hemelsbreed, indicatie, geen norm) | `maak_stroombeen_weg` (extract china), 153,6 km G93 + 58,3 km G5001/G85 | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-gb-laadplek` | mijn / laadplek | Greenbushes-concentraatloods (Talison) | -33.86495, 116.05505 | hergebruik letterlijk: `lithium-greenbushes-zhangjiagang` §2a(1) [8] | bron-gelegd (z18 aldaar: overdekte loods + truckloop) |
| `li-bun-berth8` | overslag truck → zee | Bunbury Berth 8, scheepslader | -33.31995, 115.66385 | hergebruik letterlijk: `lithium-greenbushes-zhangjiagang` §2a(2) [8] | bron-gelegd (z18 aldaar: bulkcarrier langszij + scheepslader) |
| `li-yangtze-monding` | overslag zee → rivier | Yangtze-monding | 31.42704, 121.47618 | hergebruik letterlijk: `lithium-atacama-antofagasta` §3, `lithium-goulamina-yangtze` [8] | aannemelijk (conventie-anker; MARNET-eindknoop 31.51, 121.4187) |
| `li-guoyuan-bulkkade` | overslag binnenschip → truck | Guoyuan-haven, droge-bulkkade, Chongqing | 29.6140, 106.7850 | [4][11] sat z14/z15/z16 | **aannemelijk** (z16 gezien: bulkterminal met stockyards van zwarte en rood-bruine hopen, transportbanden en lagers langs de oever, binnenschepen aan jetties; geen bron noemt lithium op deze terminal; bulklaag-eindpunt 29.609, 106.7839 op 0,57 km) |
| `li-shehong-tianqi` | fabriek / losplek | Tianqi Lithium Shehong, Taihe | 30.9111, 105.3768 | [3][5][11] Photon-punt uit de haalbaarheidstoets + sat z14/z15/z16 | **onzeker** (z16 gezien: industriepark met blauwgedekte fabriekshallen, tanks en wegen in de Fu-bocht, 1,4 km ten noorden van de G93-aansluiting; past bij het voormalige lithiumzoutterrein aan de rivier [3], maar het pand is niet aan te wijzen) |

## 4 · Via-punten (alleen b5; alle punten op de doorgaande snelweg, geen stad, geen zijtak; extract china)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b5 | 1 | G5001 Chongqing-rondweg, NO-zijde | 29.7700, 106.6597 | zonder dit punt kiest de router een route van 44 km over stadsstraten door Chongqing (3 km van Yuzhong) [10] |
| b5 | 2 | G5001/G85 rondweg, noordzijde | 29.7887, 106.4998 | houdt de lijn op de rondweg langs de noordkant i.p.v. door de stad |
| b5 | 3 | G93 ten NW van Chongqing | 29.6817, 106.2979 | afslag van de rondweg op de G93 richting Tongliang (het begin van de G93 ligt in de stad) |
| b5 | 4 | G93 tussen Tongnan en Suining | 30.1667, 105.7960 | doorgaande snelweg (5 km van Tongnan-stad: een via-punt in Tongnan-stad gaf 12,4 km keerlus) |
| b5 | 5 | G93 ten zuiden van Suining | 30.3967, 105.6109 | corridorpunt voor de laatste 73 km naar Shehong (4,7 km van het centrum van Suining) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Greenbushes (Talison) | Tianqi/IGO 51% · Albemarle 49% | erts → spodumeenconcentraat | ≈ 200 kt LCE/j (FY2025) | [9] |
| Tianqi Lithium Shehong (天齐锂业(射洪)有限公司) | Tianqi Lithium | spodumeenconcentraat → lithiumcarbonaat, hydroxide, chloride | 14,5 kt Li2CO3 + 5 kt LiOH + 4,5 kt LiCl (SMM, 2023; peildatum onbekend) | [1][2] |

## 6 · Stoppunt
De lijn stopt op het fabrieksanker in Shehong: WoodMac noemt Greenbushes-concentraat als voeding van de Tianqi-plant in Sichuan [1], maar geen bron noemt een afnemer van het carbonaat of hydroxide, dus fase D en E vervallen.

## 7 · Open punten
- **Barge naar Chongqing is niet gebronnen.** Geen gevonden bron (WoodMac-samenvatting, Tianqi-pagina's) beschrijft de logistiek Bunbury → Shehong. Een zeegaande bulkcarrier haalt Chongqing niet (Drie Klovendam: max 10.000 t [6]; Chongqing: schepen tot 5.000 DWT [4]; winterdiepte rond Chongqing 2,5-3 m [7]); het concentraat zou dus op de Beneden-Yangtze moeten overslaan naar binnenschepen. De overslag is hier schematisch in de monding gelegd. Alternatief (niet getekend): Qinzhou + spoor (Westelijke Land-Zee-corridor), zoals `lithium-greenbushes-qinzhou`.
- **Het Shehong-pand is niet aan te wijzen**: adres is *四川省射洪县太和镇城北* [3]; OSM, Nominatim en Photon kennen geen Tianqi-object (Nominatim 2026-10-30: geen resultaat). Het Photon-punt van de haalbaarheidstoets ligt op een industriepark dat bij het adres past.
- **Wegkm niet gepubliceerd**: 254,2 gemeten tegen een hemelsbreed 198 km; de eerste route (toetsagent: 266 km, eigen run met via-punt-keuze door de stad: 250,2 km) laat zien dat de uitkomst bij de corridorkeuze door Chongqing hangt. De rondweg is gekozen om niet door de stad te sturen; een truckverbod in de stad is niet nagezocht.
- **Rivier-km niet gepubliceerd**: het ±2.400 km Shanghai–Chongqing is eigen kennis; geen bron gevonden (zoekopdracht 2026-10-30). De meting (2.243,4 vanaf 31.4512, 121.4769) is dus een indicatie.
- **Guoyuan-terminal niet bevestigd voor lithium**: Guoyuan is een bulk-/containerhub (railhub) [4]; welke kade dit concentraat ontvangt is niet gevonden. Alternatieven: Jiulongpo en Cuntan.
- **Volume**: het Shehong-aandeel van Greenbushes is niet gepubliceerd (Greenbushes levert ook Zhangjiagang, Kwinana, Kemerton, Qinzhou); de SMM-capaciteit is van 2023 en kan achterhaald zijn.
- **Bunbury-naad 4,93 km** (b1 → b2, kopie) blijft open; Yangtze-anker ligt 4,45 km van de MARNET-eindknoop (conventie).

## 8 · Bronnen
[1] Wood Mackenzie, Asset Report Shehong lithium refinery (Tianqi; Sichuan; carbonaat + hydroxide; voeding uit Greenbushes). https://www.woodmac.com/reports/metals-shehong-lithium-refinery-558993/
[2] SMM, Tianqi Lithium's Net Profit Soared by over 1,000% in 2022 — capaciteitsoverzicht Shehong (14.500 t carbonaat, 5.000 t hydroxide, 4.500 t chloride), 2023-03-31. https://news.metal.com/newscontent/102156591-tianqi-lithiums-net-profit-soared-by-over-1000-in-2022-an-overview-of-its-lithium-product-capacity
[3] Tianqi Lithium, rights issue prospectus 2019-12-13 (adres: 射洪县太和镇城北); 10jqka bedrijfsprofiel (天齐锂业(射洪)有限公司, volledige dochter). https://disc.static.szse.cn/disc/disk02/finalpage/2019-12-13/4f3119f2-e388-4083-9caa-ac2b29795106.PDF · https://basic.10jqka.com.cn/002466/company.html (alleen via zoekresultaat gelezen; de vestiging in 1992 als staats-lithiumzoutfabriek en 2004 Tianqi-overname uit hetzelfde zoekresultaat)
[4] Wikipedia, Port of Chongqing (8 havengebieden; Guoyuan Operations Area = grootste intermodale terminal; schepen tot 5.000 DWT). https://en.wikipedia.org/wiki/Port_of_Chongqing
[5] Wikipedia, Shehong (Taihe = subdistrict). https://en.wikipedia.org/wiki/Shehong · Photon/Nominatim 2026-10-30 (geen Tianqi-object).
[6] Wikipedia, Three Gorges Dam ("Maximum vessel size is 10,000 tons"). https://en.wikipedia.org/wiki/Three_Gorges_Dam
[7] Port Economics, Management and Policy, The Yangtze River System (secties Shanghai–Nanjing–Yichang–Yibin; winterdiepte bij Chongqing). https://porteconomicsmanagement.org/pemp/contents/part2/port-hinterlands-regionalization/yangtze-river-system/
[8] Brieven `lithium-greenbushes-zhangjiagang.md` (§2a, b1, ankers), `lithium-greenbushes-qinzhou.md`, `lithium-atacama-antofagasta.md` §3 (Yangtze-anker); functie `bak_lithium` in `v2/tools/bak_stromen.sh`.
[9] `v2/design/lithium-sitelaag.json`, `w-li-greenbushes` (±1,4 Mt SC FY2025 ≈ 200 kt LCE/j; Albemarle 10-K FY2025 + Exhibit 96.1).
[10] OSM (ODbL) via `wegscan_puur.py`, extract china (Geofabrik): G93, G5001, G85, G75; profiel `lithium-greenbushes-shehong-guoyuan-shehong`.
[11] Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-lithium-greenbushes-shehong-guoyuan-bulkkade-z15.png` (+ `-z16`), `-fabriek-z15.png`, `-tianqi-z16.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)

**Stroom `lithium-greenbushes-shehong`** → `v2/data/stroomroute-lithium-greenbushes-shehong.json` (290,9 KB, versie 2, lonlat) — 5 benen, **10.195,9 km**, 15.403 punten, 5 markers.
| been | modaliteit | km | punten | stijl |
|---|---|---|---|---|
| b1 | truck Greenbushes → Bunbury Berth 8 (letterlijke kopie `stroombeen-greenbushes-bunbury.geojson`) | 83,1 | 1.094 | doorgetrokken |
| b2 | zee Bunbury → Yangtze-monding (MARNET, letterlijke kopie zee-regel `bak_lithium`) | 7.606,6 | 785 | doorgetrokken |
| b3 | zee-overgang MARNET-eindknoop → 31.4512,121.4769 (letterlijke kopie) | 8,6 | 2 | stippel: MARNET houdt op |
| b4 | binnenvaart Yangtze-monding → Guoyuan-bulkkade Chongqing (`maak_rivierbeen.py`, bulklaag) | 2.243,4 | 11.697 | doorgetrokken |
| b5 | truck Guoyuan-bulkkade → Tianqi Shehong (profiel `lithium-greenbushes-shehong-guoyuan-shehong`, extract china, `wegscan_puur.py`) | 254,2 | 1.825 | doorgetrokken |

Markers: li-gb-laadplek, li-bun-berth8, li-yangtze-monding, li-guoyuan-bulkkade, li-shehong-tianqi.
Recept: `bash v2/tools/bak_stromen.sh lithium-greenbushes-shehong` (functie `bak_lithium_greenbushes_shehong`, zwaar-slot, 14 s; b4 en b5 waren vooraf gebakken tussenuitvoer in `v2/build-cache/ais/graaf/lithium-greenbushes-shehong-*`).
Toelichting per stippel/aanloop/vlucht/leiding: alleen b3 is stippel (8,6 km, kopie van `bak_lithium`: MARNET reikt niet tot de Yangtze-bulklaag). Geen haven-aanloop (Bunbury snapt op 4,93 km, <5 km, bekende naad), geen vlucht, geen leiding, geen spoor, geen last-mile-been.
**Toets:** naden 0 behalve Bunbury b1 naar b2 4,93 km (kopie, bekend) en b4 naar b5 0,57 km (rivier-eindpunt tegen kade-anker); b5 254,2 km tegen hemelsbreed 198 km (+28%, indicatie: geen gepubliceerde wegkm, dus geen norm); b4 2.243,4 tegen circa 2.400 eigen kennis (-6,5%, indicatie). Markers op hun lijn (0,0 km) behalve li-yangtze-monding (conventie-anker, 2,69 km van de lijn, hergebruikt letterlijk uit lithium-atacama-antofagasta). `toets_knikken`: 34 knikken, 4 omkeringen, 1 terugloop: de terugloop (29.7808,106.5155, G5001/G85) is een ~0,5 km lange knooppuntlus (lus 306-329 in b5), geen heen-en-weer langs hetzelfde stuk; de overige spikes zitten op knooppunten, ankers en in de Yangtze-meander bij 30.84,110.998 (Yichang).
**Lessen:** (1) via-punten op G5001/G85 en G93 (niet in Chongqing, Tongnan of Suining) houden b5 op 254 km in plaats van 266 km; (2) Chongqing-eindpunt van de rivier ligt 0,57 km van het kade-anker (bulklaag-eindpunt), niet gesloten met een stub; (3) b1-b3 zijn byte-voor-byte hergebruik van de zhangjiagang-lijnen.
Registerregel: sleutel `li-gs`, bestand `stroomroute-lithium-greenbushes-shehong.json`.
