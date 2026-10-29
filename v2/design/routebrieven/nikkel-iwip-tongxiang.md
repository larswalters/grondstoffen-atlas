# Routebrief (licht) · nikkel — Halmahera (IWIP/Huafei) → Ningbo → Tongxiang (China)

**stroom-id:** `nikkel-iwip-tongxiang` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** MHP (nikkel-kobalt-tussenproduct) van de Huafei-HPAL op Weda Bay Industrial Park (IWIP, Halmahera Tengah) gaat over eigen parkterrein naar de IWIP-jetty, per **zeeschip** (twee haven-aanlopen) naar de containerkade Ningbo Beilun en per **truck** (letterlijke kopie G60/G92) naar Huayou's Tongxiang-vestiging (Zhejiang) — aannemelijk: één bron, alleen eigendom; geen zendingsbron. Fase D/E vervallen.
**Welke as van het verhaal:** de zwaarste Indonesische nikkel-HPAL als eigen lijn naast `kobalt-wedabay-tongxiang` (zelfde geometrie, andere grondstof; precedent golf 2b `nikkel-morowali-quzhou` naast `kobalt-morowali-quzhou`). Nameplate **120 kt Ni/j** in MHP (+ 15 kt Co/j), peiljaar 2023–2026 [1][2]; **sinds 1 mei 2026 de helft (~60 kt Ni/j) op care and maintenance** wegens zwavelkosten, geen herstartdatum [1]. Groep Huayou verscheepte 236.500 t MHP in 2025 (+30%; product, geen Ni-inhoud, geen Huafei-aandeel) [5].

## 1 · Ketenkaart
```
Huafei-HPAL `ni-iwip-huafei` ──(b1 truck · eigen IWIP-terrein · 4,96 km hemelsbreed, stippel)──► IWIP-jetty `ni-iwip-jetty`
  ──(b2 zee-aanloop · Molukse Zee · 131,99 km tot zeeknoop 9033, stippel, kopie)──► zeeknoop 9033 (0.0961, 129.1306)
  ──(b3 zee · MARNET · Molukse Zee → Sulawesizee → Zuid-Chinese Zee → Straat Taiwan → Oost-Chinese Zee)──► zeeknoop Ningbo (29.9758, 121.9736)
  ──(b4 zee-aanloop · 11,6 km, stippel, kopie)──► Ningbo Beilun-kade `ni-ningbo-kade`
  ──(b5 truck · G60/G92 · 192,2 km gemeten, kopie, aannemelijk: één bron)──► Huayou Tongxiang `ni-tongxiang-raffinaderij` ⏹
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-iwip-huafei` → `ni-iwip-jetty` | eigen IWIP-parkterrein | hemelsbreed 4,96 km, geen wegkm | `--stippel` (zelfde regel als kobalt b1) | ja — eigen terrein, geen net op deze korrel |
| b2 | B | zee (haven-aanloop) | `ni-iwip-jetty` → zeeknoop 9033 | Molukse Zee | 131,99 gemeten (rechte afstand kade–knoop; gebakken kopie 142,3) | `--stippel-geojson` letterlijke kopie `kobalt-wedabay-tongxiang-aanloop-iwip.geojson` | ja — MARNET reikt hier niet (kade 132 km van de knoop) |
| b3 | B | zee | zeeknoop 9033 → zeeknoop Ningbo | Molukse Zee → Sulawesizee → Zuid-Chinese Zee → Straat Taiwan → Oost-Chinese Zee | hemelsbreed 3.408; kopie gebakken 3.764,9; geen publicatie, geen ±15%-toets | MARNET `--been` | nee |
| b4 | B | zee (haven-aanloop) | zeeknoop Ningbo → `ni-ningbo-kade` | Beilun-containerzone | 11,6 (kopie) | `--stippel-geojson` letterlijke kopie `kobalt-tfm-quzhou-aanloop-ningbo.geojson` | ja — kade 10,99 km van de knoop (> 5 km) |
| b5 | C | truck | `ni-ningbo-kade` → `ni-tongxiang-raffinaderij` | G60/G92 Ningbo–Tongxiang | gemeten geometrie 192,2 (kopie); hemelsbreed 146,6; geen gepubliceerde wegkm, geen ±15%-toets | `--been-geojson` letterlijke kopie `kobalt-murrinmurrin-kwinana-weg-ningbo-tongxiang.geojson` | nee — "aannemelijk: één bron" staat in de beennaam |

## 3 · Ankers (één per site en per overslag; alle hergebruikt, geen coördinaat gewijzigd)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-iwip-huafei` | HPAL-plant (= `co-wedabay-huafei` = `ni-iwip-rkef`) | Huafei Nickel Cobalt HPAL, IWIP-ore-yard/industriecluster | 0.4970, 127.9670 | `nikkel-wedabay-iwip.md` §3, `kobalt-wedabay-tongxiang.md` §3 | **aannemelijk** (z15 gezien 2026-10-29: kaal ertsterrein tegen de rand van het industriecluster, direct W van de blauw-gedekte ovenhallen; geen HPAL-gebouw aanwijsbaar, park is één aaneengesloten complex) |
| `ni-iwip-jetty` | overslag parkweg → zee | IWIP-havenbekken, kolen-/ertskade | 0.4745, 128.0055 | `nikkel-wedabay-iwip.md` §3 | bron-gelegd (z15 gezien: kruis op de kade met afgemeerde zeeschepen en kolenkoepels; welke berth MHP laadt is niet te zien) |
| `ni-ningbo-kade` | overslag zee → truck | Beilun Container Terminal Phase 2, Ningbo-Zhoushan | 29.9353, 121.8695 | `kobalt-tfm-quzhou.md` §3 | bron-gelegd (z15 gezien: containerkade met portaalkranen en stapels containers) |
| `ni-tongxiang-raffinaderij` | afnemer ⏹ | Zhejiang Huayou Cobalt, Tongxiang Economic Development Zone | 30.6167, 120.5629 | `kobalt-huayou-gunsan.md` §3, MEE-register | **onzeker** als smelter (z15 gezien: bedrijfscampus met laagbouw in stedelijk blok tussen woonwijken, geen smelter-installatie; past bij hoofdkantoor/campus, zie §7) |

## 4 · Via-punten
Geen nieuwe. b1 is een parkinterne stippel, b2–b4 zijn zee/aanloop, b5 is een letterlijke kopie met de via-punten van `kobalt-huayou-gunsan.md` §4. De sitelaagpunt `w-iwip-hpal` (0.48, 127.985) ligt 2,75 km van `ni-iwip-huafei`; op satelliet ligt die op kuststrook zonder fabriek, dus het startanker blijft staan.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Huafei-HPAL (IWIP) | Huayou-dochter (Argus; verdere aandeelhouders niet geverifieerd) | lateriet-erts → MHP | 120 kt Ni + 15 kt Co/j nameplate; ~50% op care and maintenance sinds 1 mei 2026 | [1][2][4] |
| Huayou Tongxiang | Zhejiang Huayou Cobalt | MHP/tussenproduct → batterijchemicaliën (aannemelijk) | niet gepubliceerd voor Tongxiang | [3] |

## 6 · Stoppunt
De brief stopt bij Huayou Tongxiang: de afname steunt uitsluitend op eigendom (Huayou bezit Huafei en Tongxiang) en geen bron noemt een vervolgfabriek of een zending; blijkt dat onhoudbaar, dan vervalt b5 en eindigt de keten op de Ningbo-kade.

## 7 · Open punten
- **Bestemming niet gebrond:** Argus noemt geen Tongxiang of Quzhou als afnemer [1]; Argus meldt wel MHP in bonded warehouses rond Guangzhou [2]. Quzhou (nikkelsulfaat, `nikkel-morowali-quzhou`) is het sterkere alternatief; Tongxiang volgt het kobalt-patroon.
- **Tongxiang-coördinaat:** `kobalt-sitelaag.json` noemt 30.63/120.56 hoofdkantoor/campus; satelliet bevestigt een campus, geen smelter; de MEE-vergunning wijst naar dezelfde plek. Centrale check nodig.
- **Startanker:** 0.4970, 127.9670 ligt aan de rand van het complex, niet aantoonbaar op de HPAL; sitelaag `w-iwip-hpal` staat 2,75 km elders (niet door mij gewijzigd).
- **Volume:** Huafei-productie 2025 niet apart gepubliceerd (alleen "boven doelstelling" in Huayou-prognose [6] en groep 236,5 kt MHP [5]); startdatum juni 2023 (Argus) of Q1 2024 (Mining Technology).
- **b2/b3/b5 km:** geen gepubliceerde wegkm of zeekm; kopieën gebakken in `kobalt-wedabay-tongxiang`. Duplicaatrisico: alleen de grondstof verschilt; markers `ni-` op dezelfde coördinaten.

## 8 · Bronnen
[1] Argus Media, "Indonesia's Huafei to cut MHP output on sulphur costs", 28 apr 2026 — 120 kt Ni, helft op C&M vanaf 1 mei 2026. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2820208-indonesia-s-huafei-to-cut-mhp-output-on-sulphur-costs
[2] Argus Media, "Huayou, Vale commit to Indonesian Huali MHP project" — Huafei sinds juni 2023, 120 kt Ni + 15 kt Co; MHP in bonded warehouses Guangzhou. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2483610-huayou-vale-commit-to-indonesian-huali-mhp-project
[3] Wikipedia, "Zhejiang Huayou Cobalt" — hoofdkantoor in Tongxiang Economic Development Zone; Quzhou-vestigingen. https://en.wikipedia.org/wiki/Zhejiang_Huayou_Cobalt
[4] Mining Technology, "Capacity addition Indonesia nickel supply 2026" — Huafei-project productiestart Q1 2024. https://www.mining-technology.com/analyst-comment/capacity-addition-indonesia-nickel-supply-2026/
[5] Critical Minerals News, "Huayou Cobalt" — MHP-verscheping 236.500 t in 2025 (+30%). https://critical-minerals-news.com/huayou-cobalt/
[6] Huayou, 2025 Annual Performance Forecast (pdf, via zoekresultaat, niet geopend). https://www.huayou.com/Public/Uploads/uploadfile2/files/20260105/ZhejiangHuayouCobaltCo.Ltd.2025AnnualPerformanceForecast.pdf
[7] Wikipedia, "Weda Bay Industrial Park" — 0°28'42"N 127°59'01"E, Tsingshan/Eramet. https://en.wikipedia.org/wiki/Weda_Bay_Industrial_Park
[8] Huayou, Indonesia Nickel Industry — noemt "Huafei HPAL Hydrometallurgical Project" op Halmahera. https://www.huayou.com/en/products/indonesia-nickel-industry
[9] `v2/design/routebrieven/kobalt-wedabay-tongxiang.md`, `nikkel-wedabay-iwip.md`, `kobalt-tfm-quzhou.md`, `kobalt-huayou-gunsan.md` — hergebruikte ankers en geojsons.
[10] Esri World Imagery via `sat_check.py` z15: `v2/build-cache/satcheck/sat-nikkel-iwip-tongxiang-{huafei-anker,huafei-sitelaag,jetty,ningbo-kade,tongxiang}.png`.
[11] v1: `data/nickel.js` (`ni-ref-iwip`), `design/nikkel.md`; sitelaag `v2/design/nikkel-sitelaag.json` (`w-iwip-hpal`, 120 kt Ni).

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
**Bestand:** `v2/data/stroomroute-nikkel-iwip-tongxiang.json` (28,8 KB, versie 2, punt_formaat lonlat) · functie `bak_nikkel_iwip_tongxiang` in `v2/tools/bak_stromen.sh` · **totaal 4.116,0 km, 1.388 punten, 4 markers, naden 0 km.**
Alles is een letterlijke kopie van de kobalt-keten (`bak_kobalt_wedabay_tongxiang`); geen wegscan, geen profiel in `maak_stroombeen_weg.py`, geen nieuwe haven-aanloop-run.

| # | modaliteit | km (gebakken) | punten | lijnstijl | toelichting |
|---|---|---|---|---|---|
| b1 | truck | 5,0 | 2 | stippel | eigen IWIP-terrein, hemelsbreed 4,96 km (geen wegkm), geen net op deze korrel |
| b2 | zee | 142,3 | 114 | stippel | haven-aanloop IWIP, letterlijke kopie `kobalt-wedabay-tongxiang-aanloop-iwip.geojson`; MARNET reikt niet (kade 131,99 km rechte afstand van zeeknoop 9033) |
| b3 | zee | 3.764,9 | 388 | doorgetrokken | MARNET zeeknoop 9033 → zeeknoop Ningbo; geen publicatie, geen ±15%-toets (hemelsbreed 3.408) |
| b4 | zee | 11,6 | 5 | stippel | haven-aanloop Ningbo Beilun, letterlijke kopie `kobalt-tfm-quzhou-aanloop-ningbo.geojson` (kade 10,99 km van de knoop) |
| b5 | truck | 192,2 | 879 | doorgetrokken | G60/G92, letterlijke kopie `kobalt-murrinmurrin-kwinana-weg-ningbo-tongxiang.geojson`; aannemelijk: één bron (alleen eigendom) staat in de beennaam; geen gepubliceerde wegkm, geen ±15%-toets (hemelsbreed 146,6) |

**Markers (4, alle exact op de lijn, afstand 0 km):** `ni-iwip-huafei` (0.4970,127.9670, aannemelijk), `ni-iwip-jetty` (0.4745,128.0055), `ni-ningbo-kade` (29.9353,121.8695), `ni-tongxiang-raffinaderij` (30.6167,120.5629, onzeker als smelter).
**Recept:** `bash v2/tools/bak_stromen.sh nikkel-iwip-tongxiang` (zwaar-slot, ca. 1 min).
**Toets:** naden 0 km; `toets_knikken.py`: 24 knikken, 0 terugloop (de knikken zitten in de gekopieerde G60/G92-geometrie en de Beilun-kade-omgeving, niet gerepareerd, gedeeld been); `toets_rechte_benen.py --min-km 5`: alleen b1 (stippel, bedoeld); json: versie 2, lonlat, modaliteiten {zee, truck}, elk been ≥ 2 punten.
**Lessen:** (1) bij een duplicaatketen volstaat een functie met letterlijke kopieën, geen runs nodig; (2) b2 heet 131,99 km in de brief (rechte afstand) maar de gebakken kopie is 142,3 km; geen conflict, beide staan in de beennaam/brief; (3) open punten zoals in §7 blijven: bestemming Tongxiang niet gebrond, Tongxiang-anker is een campus, startanker niet aantoonbaar op de HPAL.
