# Routebrief (licht) · kolen — Haerwusu → Shenchi-Zuid → Huanghua (China)

**stroom-id:** `kolen-haerwusu-huanghua` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** Shenhua-steenkool uit de dagbouw Haerwusu (Zhungeer, Binnen-Mongolië) gaat per **spoor** over de
Dazhun-lijn en de Zhunchi-lijn (准池铁路, 179,9 km, 2015) naar Shenchi-Zuid, en over de Shuohuang-lijn (朔黄铁路, ~588 km)
naar de kolenterminal van Huanghua (Hebei), de grootste kolenhaven van China — stoppunt, want geen bron noemt een
volgende bestemming.
**Welke as van het verhaal:** *binnenlands "west-kool naar de Bohai-haven" in één eigenaarsketen* (mijn, spoor, haven:
China Energy/Shenhua). Haerwusu: **35 Mt/j** vergunde capaciteit (GEM GCMT 2023) [5], commerciële productie 27,4 Mt in 2016 [6].
Shuohuang: **190 Mt in 2012** [2], sinds zeven jaar >300 Mt/j [8]; Huanghua: **200,04 Mt kolen t/m 6 dec 2024** [9].
Het aandeel van déze mijn in de Shuohuang-stroom is niet gepubliceerd (§7).

## 1 · Ketenkaart
```
Haerwusu-laadlus (silo + keerlus aan de dagbouw) `kolen-haerwusu-laad`
   ──(b1 spoor · Dazhun-lijn → Zhunchi-lijn (Waixigou → Shenchi-Zuid) → Shuohuang-lijn · ~894 km graaf-proef,
       aannemelijk: één bron voor deze mijn → Huanghua)──► Huanghua-kolenterminal `kolen-huanghua-kade` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A+B | spoor | `kolen-haerwusu-laad` → `kolen-huanghua-kade` | Dazhun (Zhungeer → Waixigou, ~125 km afgeleid) → Zhunchi 179,862 km [1] (Waixigou → Shenchi-Zuid) → Shuohuang 588 km [3] (Shenchi-Zuid → Huanghua) | graaf-proef 893,5 km, 0 bochten ≥60°; Shenchi-Zuid → kade 586,6 km tegen 588 [3] (−0,2%), tegen 594 [2] (−1,2%); Zhunchi + Shuohuang gepubliceerd 767,9 km, Dazhun-deel niet | toets_spoorroute (1-op-1-net), één run, geen via | nee — volledig in het 1-op-1-spoornet; aannemelijk staat in de beennaam |

Fase C (last mile) vervalt: het anker ligt op de terminal zelf. Geen zeebeen, geen haven-aanloop, geen fase D/E.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-haerwusu-laad` | laadplek (mijn) | Haerwusu-laadlus Shenhua-Zhunneng, Xuejiawan | 39.7215, 111.2285 | [5][12] | bron-gelegd (z15 gezien: keerlus en silo/kolenwasserij aan de rand van de dagbouw, spoorbundel loopt de put in; het GEM-punt 39.7310, 111.2583 ligt in de put). Spoor snapt op 0,22 km |
| `kolen-huanghua-kade` | overslag spoor → zee (eindpunt) | Huanghua-kolenterminal (Shenhua), Hebei | 38.3135, 117.8751 | [9][10][12] | bron-gelegd (z14 gezien: rijen kolenstapels met treinlus en laadtrestles, kolenpieren met schepen direct oostelijk). Spoor snapt op 0,10 km |
| `kolen-shenchi-zuid` | referentiepunt (geen marker) | Shenchi-Zuid, kruising Zhunchi–Shuohuang | 39.0772, 112.1903 | [11][12] | aannemelijk (z14: tegel deels leeg; spoorcorridor langs de oostrand van de stad). De graaf-route passeert op 0,4 km |

Sitelaag-fout (alleen melden): `w-huanghua` 38.345, 117.775 ligt ~9 km WNW op teruggewonnen land met bebouwing, niet op de terminal.

## 4 · Via-punten
Geen. De Dazhun- en Zhunchi-lijn zijn de enige weg van Zhungeer naar Shenchi-Zuid; een run via het station
(39.0772, 112.1903) geeft 311,3 + 586,6 = 897,9 km en een bocht ≥60° op het via-punt: **één run zonder via is beter**
(893,5 km, 0 bochten). De route passeert Shenchi-Zuid op 0,4 km (route-km ~307) en Suning op 1,6 km (route-km ~713).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Haerwusu-dagbouw | China Shenhua Energy (China Energy 69%) | steenkool (bitumineus, thermisch) → trein | 35 Mt/j vergund; 2016 27,4 Mt | [5][6] |
| Huanghua-kolenhaven | Shenhua-havenbedrijf; exploitant CHN Energy | trein → kolenschip | >200 Mt/j (2024); ontwerpcapaciteit 183 Mt/j [7] | [7][9][10] |

## 6 · Stoppunt
De brief stopt op de kolenterminal van Huanghua: GEM en Mysteel noemen Huanghua als lading-haven, maar geen bron
koppelt de kolen van Haerwusu aan een volgende haven of afnemer.

## 7 · Open punten
- **Koppeling mijn → Huanghua: één bron.** Een zoekresultaat (samenvatting 2026-10-09) zegt dat Haerwusu-kool via Zhunchi en
  Shuohuang naar Huanghua gaat en dat in 2016 20 Mt "准混煤" en 12 Mt Yitai-kool naar die route werden omgelegd [7]; de
  afzonderlijke pagina's [6][8] bevestigen de route zelf niet. Structureel klopt het wel: Zhunchi verbindt Dazhun en
  Shuohuang en is gebouwd voor Mengxi-kolen [1]. Status: aannemelijk.
- **Shuohuang-lengte spreekt zichzelf tegen:** 489 km (tekst) / 594 km (infobox) [2] / 588 km [3]; de toets gebruikt 588.
- **Dazhun-deel (Haerwusu → Waixigou, ~125 km) is afgeleid** (893,5 − 179,9 − 588,5), niet gepubliceerd; Waixigou-coördinaat niet gevonden.
- **Eigendom/exploitant Huanghua:** Wikipedia [10] zegt zowel Shenhua als Qinhuangdao Port Co./Hebei Port Group; Mysteel [9] CHN Energy.
- **Sitelaag-punten ernaast:** `w-haerwusu` (in de put, ~2,6 km van de laadlus) en `w-huanghua` (~9 km): centraal gelijktrekken.
- Het aandeel Haerwusu in de ~200 Mt van Huanghua of in de Shuohuang-stroom is niet gepubliceerd.

## 8 · Bronnen
[1] zh.wikipedia, 准池铁路 — 179,862 km, Waixigou → Shenchi-Zuid, 2015-09-15, 200 Mt/j. https://zh.wikipedia.org/wiki/准池铁路
[2] zh.wikipedia, 朔黄铁路 — 489 km (tekst), 2012: 190 Mt; ~100 Mt naar Huanghua-haven. https://zh.wikipedia.org/wiki/朔黄铁路
[3] en.wikipedia, Shuozhou–Huanghua railway — 588 km Shenchi-Zuid → Gangkou. https://en.wikipedia.org/wiki/Shuozhou%E2%80%93Huanghua_railway
[4] zh.wikipedia, 大准铁路 — Datong → Xuejiawan, 264 km. https://zh.wikipedia.org/wiki/大准铁路
[5] GEM, Haerwusu-dagbouw (zh) — 39.731044, 111.258324; 35 Mtpa; 2018–23 ~35 Mt. https://www.gem.wiki/中国神华能源股份有限公司哈尔乌素分公司（哈尔乌素露天矿）
[6] China Securities Journal, 2017-08-04 — Haerwusu 35 Mt/j, 2016: 27,4 Mt. https://cs.com.cn/ssgs/gsxw/201708/t20170804_5409270.html
[7] WebSearch 2026-10-09 (哈尔乌素 准池铁路 朔黄铁路 黄骅港 外运), samenvatting — route Zhunchi → Shuohuang → Huanghua, 2016-omleiding, Huanghua ontwerpcapaciteit 183 Mt/j; bronpagina niet los bevestigd.
[8] China Securities Journal, 2024-06-04 — Shuohuang >300 Mt/j zeven jaar, Huanghua >200 Mt/j. https://cs.com.cn/esg/202406/t20240604_6414865.html
[9] Mysteel, 2024 — Huanghua 200,04 Mt kolen t/m 6 dec. https://www.mysteel.net/news/5070620-cnh-energy-huanghua-ports-2024-coal-throughput-exceeds-200-mln-t
[10] en.wikipedia, Port of Huanghua — eigendom/exploitatie, 2016 grootste kolenhaven. https://en.wikipedia.org/wiki/Port_of_Huanghua
[11] zh.wikipedia, 神池南站 — 39.07722, 112.19028. https://zh.wikipedia.org/wiki/神池南站
[12] Esri World Imagery via `v2/tools/sat_check.py`; OSM-spoornet via `toets_spoorroute.mjs` (2026-10-09) — `v2/build-cache/satcheck/sat-kolen-haerwusu-huanghua-laad.png`, `-kade.png`, `-shenchi.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-kolen-haerwusu-huanghua.json` (versie 2, punt_formaat lonlat, 40,5 KB) · **functie:** `bak_kolen_haerwusu_huanghua` in `v2/tools/bak_stromen.sh` · titel "Kolen · Haerwusu → Huanghua (China)".

| been | modaliteit | km gebakken | km gepubliceerd | stijl |
|---|---|---|---|---|
| b1 trein Haerwusu → Huanghua (Dazhun-, Zhunchi- en Shuohuang-lijn; aannemelijk: een bron voor deze mijn naar Huanghua) | spoor | 899,4 (router 893,5; 2171 punten) | Zhunchi 179,862 + Shuohuang 588 = 767,9; Dazhun-deel (~125) afgeleid | doorgetrokken |

Totaal 899,4 km, 2 markers (Haerwusu-laadlus 0,22 km, Huanghua-kolenterminal 0,10 km van de lijn). Naden: geen (een been).
**Recept:** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=39.7215,111.2285 --naar=38.3135,117.8751 --naam=kolen-haerwusu-huanghua-haerwusu-huanghua --hoofd-km=1000` (proef van 21:22 hergebruikt, geojson in `build-cache/ais/graaf/`), daarna `bash v2/tools/bak_stromen.sh kolen-haerwusu-huanghua` met `--been-geojson "spoor|…"` en twee `--marker`. Geen via, geen zee, geen weg, geen aanloop, geen stippel, geen kopie.
**Toets:** gemeten totaal 899,4 km (haversine over de punten) tegen 893,5 km routerwaarde (+0,7%) en tegen 767,9 + ~125 = ~893 km uit de bronnen (+0,7%); toets_knikken 0 knikken, 0 omkeringen; markers binnen 0,25 km van de lijn. Langste segmenten 9,5 en 8,8 km (Shenchi-Zuid/Suning, tunnelstukken van de Shuohuang-lijn, geen knik); toets_rechte_benen toont geen rechte been.
**Toelichting:** geen stippel, aanloop, vlucht of leiding. Via-punt bewust weggelaten: een via op Shenchi-Zuid gaf 897,9 km en een bocht >=60 graden (de route passeert het station al op 0,4 km). Aannemelijk blijft alleen in de beennaam (een bron voor mijn naar Huanghua).
**Lessen:** (1) een volledige proef-geojson uit de brieffase kan zonder herrouting in `--been-geojson`; (2) bij een private/doorgaande spoorketen met één corridor is "geen via" de betere keuze dan een via op een station; (3) de functie raakte tijdens de bak een gelijktijdige edit van een andere agent aan het script ("u: command not found" op een regel van andermans functie): niet van mij, de stroom is correct geschreven.
**Gemeld (niet aangepast):** sitelaag `w-haerwusu` ~2,6 km in de put en `w-huanghua` ~9 km naast de terminal: centraal gelijktrekken.
