# Routebrief (licht) · Lithium — Greenbushes → Bunbury → Qinzhou-haven (China)

**stroom-id:** `lithium-greenbushes-qinzhou` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat uit de Greenbushes-mijn gaat per truck 83,1 km over de South Western Hwy naar Bunbury Berth 8 (letterlijke kopie van `lithium-greenbushes-zhangjiagang` b1), per bulkcarrier ~6.640 km over MARNET (Sunda/Karimata, Zuid-Chinese Zee, Beibu-golf) naar een droge-bulkkade van het Dalanping-schiereiland in Qinzhou, bij de converter van Albemarle; de lijn eindigt op de kade, de plant is niet gevonden.
**Welke as van het verhaal:** *de tweede Chinese Albemarle-converter naast Zhangjiagang (Tianqi)*: Albemarles eigen Qinzhou-fabriek (carbonaat + hydroxide, ontwerp 25 kt LCE/j) krijgt Greenbushes-concentraat. Volume (peiljaar FY2025): Greenbushes ≈ **200 kt LCE/j** [6], Qinzhou-aandeel ongepubliceerd, geen tonnage in de bron [1].

## 1 · Ketenkaart
```
Greenbushes-loods `li-gb-laadplek` ──(b1 truck · Maranup Ford Rd → South Western Hwy · 83,1 km, KOPIE zhangjiagang b1)──►
Bunbury Berth 8 `li-bun-berth8` ──(b2 zee · Sunda/Karimata → Zuid-Chinese Zee → Beibu-golf · ~6.643 km, MARNET; bestemming aannemelijk: één bron)──►
zeeknoop 5539 (21.5757, 108.6205) ──(b3 haven-aanloop, stippel 9,2 km — maak_havenaanloop time-out)──► Qinzhou-kade `li-qinzhou-kade` ⏹ stoppunt
(plant Albemarle Qinzhou: adres bekend, coördinaat niet gevonden → niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `li-gb-laadplek` → `li-bun-berth8` | Maranup Ford Rd → South Western Hwy (Balingup–Donnybrook–Boyanup–Bunbury) | **83,1 gemeten** (gepubliceerd ±90, −7,9%) [5] | letterlijke kopie `stroombeen-greenbushes-bunbury.geojson` (functie `bak_lithium`, FeatureCollection) | nee |
| b2 | B | zee (bulkcarrier, aannemelijk: één bron voor de bestemming) | `li-bun-berth8` → zeeknoop 5539 | MARNET beslist: Sunda/Karimata, Zuid-Chinese Zee, Beibu-golf (niet Lombok-Makassar) | **6.643,4 gemeten** (proefrun 2026-10-29, 35 edges, 682 pt; hemelsbreed 6.157; geen publicatie) [10] | MARNET; start snapt 4,93 km van de kade (<5 km, bekende open naad, zie §7) | nee |
| b3 | B | zee (stippel) | zeeknoop 5539 → `li-qinzhou-kade` | haven-aanloop | 9,19 hemelsbreed | `maak_havenaanloop.py` gaf na 300 s geen pad (time-out) → rechte `--stippel`, geen land gekruist (NE-toets) | ja — MARNET reikt niet (9,2 km) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-gb-laadplek` | mijn / laadplek | Greenbushes-concentraatloods (Talison) | -33.86495, 116.05505 | hergebruik letterlijk: `lithium-greenbushes-zhangjiagang` §2a(1) | bron-gelegd (z18, aldaar: overdekte loods + truckloop) |
| `li-bun-berth8` | overslag / laadkade | Bunbury Berth 8, scheepslader | -33.31995, 115.66385 | hergebruik letterlijk: `lithium-greenbushes-zhangjiagang` §2a(2) [5] | bron-gelegd (z18, aldaar: bulkcarrier langszij + scheepslader) |
| `li-qinzhou-kade` | losplek (stoppunt) | droge-bulkkade, zuidpunt Dalanping-schiereiland, Qinzhou | 21.6490, 108.6615 | [1][8] + sat z14/z15/z16 | **aannemelijk** (z16 gezien: kade langs de westgevel van een opgespoten landtong met zwarte erts-/kolenhopen, oranje berg, kranen en rijen opslagloodsen; geen bron noemt welke terminal het concentraat krijgt) |
| *(plant)* | converter | Albemarle Qinzhou (广西雅保锂业) | **niet gevonden** | adres [2][3] | open punt, niet getekend |

## 4 · Via-punten
Geen nieuw landbeen: b1 is een kopie (via-punten staan in `lithium-greenbushes-zhangjiagang` §4 en in het profiel `lithium-greenbushes-bunbury`). b2 is zee, b3 een stippel.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Albemarle Qinzhou (ex Guangxi Tianyuan New Energy Materials, overname voltooid 25-10-2022) | Albemarle 100% | spodumeenconcentraat → lithiumcarbonaat + technisch/batterijkwaliteit hydroxide | ontwerp tot 25 kt LCE/j; werkelijk onbekend | [1][4] |

## 6 · Stoppunt
De lijn stopt op de kade: de 10-K zegt dat Talison concentraat naar Qinzhou verscheept en dat de fabriek daar carbonaat/hydroxide maakt [1], maar noemt geen haven, tonnage of terminal, en de plant-coördinaat is nergens vindbaar; er is dus geen gedocumenteerd landbeen en de kade zelf is aannemelijk, niet gebronnen.

## 7 · Open punten
- **Plantanker niet gevonden.** Het adres is niet eenduidig: Albemarle noemt *6 Haitian Road, Qinzhou Port* (postcode 535319) [2]; het handelsregister (36Kr) noemt als bedrijfsadres *钦州港经济技术开发区海豚路6号* (Dolphin Road) en als zetel *中马大街1号, China-Malaysia Qinzhou Industrial Park* [3]. Nominatim en OSM (overpass-api.de en openstreetmap.fr, 2026-10-29) kennen geen weg 海田路/海豚路 en geen Albemarle-object; de zone-centroïde 21.7414,108.5969 [7] is geen anker.
- **Welke kade/terminal** het Greenbushes-concentraat krijgt is niet gevonden; gekozen is de enige droge-bulkterminal op het Dalanping-schiereiland (zuidpunt). Alternatief: de erts-/kolenkade op de westoever (21.708, 108.590; zeeknoop 15,0 km). De bron over Dalanping noemt algemene bulkberths 4/5 (11 Mt/j) [8] zonder lithium.
- **Geen tonnage** voor Qinzhou en geen bron die Qinzhou aan Bunbury koppelt (10-K: "vessels"; ook Meishan en Xinyu liggen inland).
- **Greenbushes heeft al drie ketens** (zhangjiagang, kemerton, kwinana); alleen de zeeleg is nieuw.
- **Bunbury-naad 4,93 km** tussen kade en MARNET-knoop blijft open (1:10M-landmasker lokaal omgekeerd, zie bak_stromen.sh kop `bak_lithium`).
- Zeekilometer is MARNET-uitkomst (route via Sunda/Karimata); geen gepubliceerde scheepsroute-km gevonden.

## 8 · Bronnen
[1] Albemarle 10-K FY2025, Item 2 (Qinzhou "Owned", carbonaat + hydroxide; Talison ships chemical-grade concentrate in vessels to Meishan, Qinzhou, Xinyu). https://www.sec.gov/Archives/edgar/data/915913/000091591326000018/alb-20251231.htm
[2] Albemarle, Chinese mainland (Qinzhou-fabriek, 6 Haitian Road, Qinzhou Port, 535319). https://www.albemarle.com/global/en/chinese-mainland
[3] 36Kr/PitchHub, 广西雅保锂业有限公司 (opgericht 2017-12-18; bedrijfsadres 海豚路6号; zetel 中马大街1号; overname 2022-10 US$200 mln). https://pitchhub.36kr.com/project/2011442007033095
[4] Albemarle, aankondiging overname Guangxi Tianyuan New Energy Materials (2021-09-30): converter nabij Port of Qinzhou, tot 25 kt LCE/j. https://investors.albemarle.com/news-and-events/news/news-details/2021/ALBEMARLE-TO-EXPAND-LITHIUM-PRODUCTION-CAPABILITIES-WITH-ACQUISITION-OF-GUANGXI-TIANYUAN-NEW-ENERGY-MATERIALS-CO.-LTD.-09-30-2021/default.aspx
[5] Brief `lithium-greenbushes-zhangjiagang.md` (§2a, §9: anker Greenbushes, Berth 8, b1 83,1 km, bron Southern Ports/Talison). v2/design/routebrieven/
[6] `v2/design/lithium-sitelaag.json`, `w-li-greenbushes`: ±1,4 Mt SC FY2025 ≈ 200 kt LCE/j.
[7] Nominatim/OSM 2026-10-29: node 钦州港经济技术开发区 21.7414,108.5969; 大榄坪 21.7544,108.6652; way 592323269 钦州保税港区 (Dalanping-schiereiland). https://nominatim.openstreetmap.org
[8] Science and Technology Daily 2024-09-20 (Dalanping-zuid berths 9-10, 100.000 t; bulkberths 4/5, 11 Mt/j) — alleen via zoekresultaat gelezen. https://www.stdaily.com/web/gdxw/2024-09/20/content_232596.html
[9] Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-lithium-greenbushes-qinzhou-overzicht-z12.png`, `…-haven-west-z14.png`, `…-haven-oost-z14.png`, `…-kade-zuidpunt-z15.png`, `…-kade-z16.png`.
[10] Proefrun `hecht_marnet.py route` 2026-10-29 (scratchpad): Bunbury → zeeknoop 5539 6.643,4 km; zeeknoop 5539 = 21.5757,108.6205 op 9,2 km van de kade.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
**Bestand:** `v2/data/stroomroute-lithium-greenbushes-qinzhou.json` (versie 2, lonlat, 37,2 KB) · functie `bak_lithium_greenbushes_qinzhou` in `v2/tools/bak_stromen.sh` · **totaal 6.735,7 km · 1.778 punten · 3 markers.** Titel: Lithium · Greenbushes → Qinzhou-haven (spodumeen SC6.0). Geen wegprofiel, geen extract, geen nieuwe tussenuitvoer.

| # | modaliteit | km gebakken | brief | opmerking |
|---|---|---|---|---|
| b1 | truck | 83,1 (1.094 pt) | 83,1 | letterlijke kopie `stroombeen-greenbushes-bunbury.geojson` (FeatureCollection) |
| b2 | zee (MARNET) | 6.643,4 (682 pt, 35 edges) | 6.643,4 | start snap 4,93 km van Berth 8; eind snap 0,000 km op zeeknoop 5539 |
| b3 | zee, stippel | 9,2 (2 pt) | 9,19 | haven-aanloop, rechte lijn; kruist geen land (ne_10m_land: 0 m snijlengte) |

**Recept:** `hecht_marnet.py route` met `--been-geojson` (b1), `--been` (b2, kade Berth 8 naar zeeknoop 5539), `--stippel` (b3 zeeknoop naar kade). Markers: Greenbushes-loods, Berth 8, Qinzhou-kade; alle drie 0,0 km van de lijn.
**Naden:** b1 naar b2 = 4,93 km (bekende Bunbury-naad, landmasker lokaal omgekeerd, bewust niet dichtgetrokken, onder de 5 km-grens); b2 naar b3 = 0,0 km.
**Stippel:** alleen b3 (MARNET reikt niet, 9,2 km); b2 is doorgetrokken ondanks "aannemelijk: één bron" (staat in de beennaam). Geen lucht, spoor of leiding.
**Toetsen:** `toets_knikken.py` 8 knikken, 0 omkeringen, 0 terugloop (7 spikes liggen in de gekopieerde truckbeen bij Bunbury en de Greenbushes-loods, 1 krappe bocht bij -7,0/104,0 in de Soenda-/Karimata-passage); `toets_rechte_benen.py --min-km 5` meldt alleen de stippel van 9,2 km (MIDDEL, met reden); json.load: versie 2, lonlat, modaliteiten {truck, zee}, elk been >= 2 punten.
**Lessen:** (1) een gekopieerd been vergt geen scan; de hele bak duurde enkele minuten. (2) De zee-leg is een MARNET-uitkomst, geen gepubliceerde km; de brief-proef (6.643,4) kwam exact terug. (3) De plant (Albemarle Qinzhou) blijft open en is niet getekend; de lijn eindigt op de aannemelijke droge-bulkkade.
