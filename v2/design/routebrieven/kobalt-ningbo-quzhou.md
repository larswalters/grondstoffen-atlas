# Routebrief (licht) · Kobalt · Ningbo Beilun → G1512 → Huayou Quzhou (China)

**stroom-id:** `kobalt-ningbo-quzhou` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** kobaltproducten (MHP uit Indonesië, kobalthydroxide uit de DRC) die op de containerkade van Ningbo Beilun aankomen gaan per **truck** (aannemelijk: één bron) ~362 km over de snelwegen G1512 en G60 naar de kobaltraffinaderij van Huayou in Quzhou, het ontbrekende laatste been van `kobalt-tfm-quzhou`, `kobalt-morowali-quzhou` en `nikkel-morowali-quzhou`; de lijn eindigt op het fabrieksterrein.
**Welke as van het verhaal:** de laatste schakel van de Chinese kobaltketen. Huayou Quzhou raffineert 22 kt Co-inhoud per jaar (3,0 kt sulfaat + 19,1 kt tetroxide; Wood Mackenzie 2021, peiljaar 2021, eenheid kt Co per jaar, via `kobalt-sitelaag.json`) [2][12]; welk deel via Ningbo aankomt is niet uitgesplitst. Huayou's eigen rapport noemt de aanvoerroute: MHP van Huayue/Huafei én ruw DRC-hydroxide gaan via Zhapu of Ningbo naar Quzhou [1].

## 1 · Ketenkaart
```
(zee, andere stromen: Labota-jetty → Ningbo `kobalt-morowali-quzhou` · Durban → Ningbo `kobalt-tfm-quzhou`)
Ningbo Beilun containerkade `co-ningbo-kade`
  ──(b1 truck · G1512 Yongjin + G60 · hemelsbreed 314 km, geen wegkm · aannemelijk: één bron)──► Huayou Quzhou `co-quzhou-huayou` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | `co-ningbo-kade` → `co-quzhou-huayou` | G1512 Ningbo–Jinhua (185,56 km [3]) → G60 Jinhua–Quzhou | hemelsbreed 314 km, geen wegkm; eigen OSM-scan 362,2 km (alleen referentie, geen ±15%-norm) [8] | maak_stroombeen_weg (extract china) | nee |

Beennaam: `Ningbo Beilun → Huayou Quzhou (G1512 + G60; aannemelijk: één bron, MHP en DRC-hydroxide naar Quzhou; Zhapu of Ningbo onbeslist; TFM-lading niet gebrond)`.
Geen zeebeen en geen haven-aanloop: de zee-benen en de 11,6 km aanloop (zeeknoop 5850 → kade) zitten al in de drie stromen die op deze kade eindigen. Geen last-mile-been: het wegbeen eindigt op het site-anker (laatste 0,6 km service-weg valt binnen het profiel).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-ningbo-kade` | overslag zee → weg (hergebruikt) | Beilun Container Terminal Phase 2, Ningbo-Zhoushan | 29.9353, 121.8695 | `kobalt-tfm-quzhou.md` §3 [9]; zelfde punt in [10] | bron-gelegd (z15 gezien: rij portaalkranen langs de pier, containerstapels erachter; `sat-kobalt-ningbo-quzhou-beilun.png`) |
| `co-quzhou-huayou` | raffinaderij (stoppunt) | Quzhou Huayou Cobalt New Material Co., Ltd. (衢州华友钴新材料有限公司), 念辛路18号, Hi-tech Industrial Park fase II, Quzhou | 28.8731, 118.8618 | MEE-emissieregister, USCC 91330800575349959F001P (controlecijfer klopt), decimaal gelijk aan DMS [6][13] | bron-gelegd (z15 gezien: groot chemisch complex met hallen en een tankpark met ronde tanks, het punt ligt midden in het complex, rond het park wegen; `sat-kobalt-ningbo-quzhou-huayou.png`) |

⚠️ `nikkel-morowali-quzhou` legt dit anker op 28.9020, 118.8780, 3,6 km ernaast (onzeker, regio-niveau) [11]; het register-punt hierboven vervangt dat centraal.

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Alle punten liggen op de snelweg (via de eigen scan van OSM gelegd, snap 0,00–0,04 km), niet in een stadscentrum; refs `G1512`, `G60`.
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | G1512-begin, west van Ningbo | 29.8043, 121.4199 | kiest de Yongjin-snelweg; zonder dit punt volgt een route G15/G92 naar Hangzhou en dan G60 (406 km in `nikkel-morowali-quzhou`, 316 km tot Jinhua tegen ~259 km via G1512, eigen scan) |
| b1 | 2 | G1512 bij Shengzhou | 29.5813, 120.8699 | houdt de lijn op de G1512 en buiten Shaoxing |
| b1 | 3 | G1512 bij Dongyang | 29.3167, 120.2652 | idem, tussen Dongyang en Yiwu |
| b1 | 4 | G1512/G60-aansluiting oost van Jinhua | 29.2335, 119.8563 | overgang naar G60, buiten Jinhua-stad |
| b1 | 5 | G60 bij Longyou | 29.0506, 119.1202 | houdt de lijn op G60 naar Quzhou, niet op de provinciale wegen |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ningbo Beilun containerkade | Ningbo Zhoushan Port Group | zee → weg | containerterminal | [9] |
| Huayou Quzhou | Zhejiang Huayou Cobalt | MHP + ruw kobalthydroxide → sulfaat/tetroxide | 22 kt Co/jaar (WoodMac 2021, verouderd) | [1][2][12] |

## 6 · Stoppunt
De lijn stopt op het terrein van Quzhou Huayou Cobalt New Material: geen bron noemt een volgende locatie met naam en adres voor dit sulfaat of tetroxide (fase D vervalt; E vervalt).

## 7 · Open punten
- **Zhapu of Ningbo is niet beslist:** Huayou's rapport noemt beide havens [1]; Ningbo is gekozen omdat drie stromen er al eindigen. Het aandeel dat via Ningbo naar Quzhou gaat is niet gepubliceerd.
- **TFM-lading niet gebrond:** het rapport noemt ruw DRC-hydroxide in het algemeen (route Durban → Zhapu/Ningbo), geen mijn of verkoper; "aannemelijk: één bron" staat daarom in de beennaam.
- **De modaliteit Ningbo → Quzhou staat in geen bron:** truck is aannemelijk; spoor (de Yongjin-lijn naar Jinhua en dan westwaarts) is een alternatief uit het ontwerp dat niet is getekend.
- **Geen wegkilometer gepubliceerd** voor het geheel: alleen G1512 = 185,56 km [3]; voor G60 Jinhua–Quzhou vond ik geen aparte lengte (de 136,8 km van de Hangjinqu-uitbreiding loopt tot de grens met Jiangxi [5]).
- **Het registerpunt is een vestiging, geen poort:** de laatste ~0,6 km loopt over een service-weg in het park.
- **Centraal:** sitelaag kobalt mist de Quzhou-site (22 kt Co, 28.8731, 118.8618) en de knoop `co-quzhou-smelter` in `kobalt-tfm-quzhou`/`kobalt-morowali-quzhou` kan nu dicht; de MEE-coördinaat is hier niet opnieuw opgehaald (overgenomen uit de haalbaarheidstoets).

## 8 · Bronnen
[1] Huayou Cobalt, 2024 Mineral Supply Chain Due Diligence Report, pp. 12–13 (MHP van Huayue/Huafei en DRC-hydroxide naar Quzhou, "Zhapu/Ningbo"; Quzhou-adres) https://www.huayou.com/Public/Uploads/uploadfile/files/20250422/2024-Mineral-Supply-Chain-Due-Diligence-Report.pdf
[2] Wikipedia, Zhejiang Huayou Cobalt (Quzhou Huayou Cobalt New Material, opgericht 2011) https://en.wikipedia.org/wiki/Zhejiang_Huayou_Cobalt
[3] Wikipedia, G1512 Ningbo–Jinhua Expressway, 185,56 km https://en.wikipedia.org/wiki/G1512_Ningbo%E2%80%93Jinhua_Expressway
[4] Wikipedia, G60 Shanghai–Kunming Expressway (Zhejiang: Hangzhou, Jinhua, Quzhou) https://en.wikipedia.org/wiki/G60_Shanghai%E2%80%93Kunming_Expressway
[5] Hangzhou Daily, 杭金衢改扩建二期 (136,786 km tot de Jiangxi-grens) https://hznews.hangzhou.com.cn/chengshi/content/2019-08/06/content_7240437.htm
[6] MEE-emissieregister permit.mee.gov.cn (dataid e889038a46924e6a9804b67b82d4b6ce), via de haalbaarheidstoets van 2026-10-09; `sat-haalb-kobalt-quzhou-huayou.png`
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15), 2026-10-09: `v2/build-cache/satcheck/sat-kobalt-ningbo-quzhou-beilun.png`, `sat-kobalt-ningbo-quzhou-huayou.png`
[8] OpenStreetMap contributors (ODbL), Geofabrik china-latest, eigen scan: route 362,2 km, snaps 0,00–0,04 km, geschreven als `kobalt-ningbo-quzhou-weg-ningbo-quzhou.geojson` (wrapper `kobalt-ningbo-quzhou-wegscan-wrapper.py`)
[9] `v2/design/routebrieven/kobalt-tfm-quzhou.md` §3 en §7  [10] `kobalt-morowali-quzhou.md` §3 en §7
[11] `v2/design/routebrieven/nikkel-morowali-quzhou.md` (b2, anker 28.9020, 118.8780, 406,0 km via G60)
[12] `v2/design/kobalt-sitelaag.json` (WoodMac 2021, 22 kt Co)  [13] `v2/design/zoek-chinees-adres-recept.md`

## 9 · Gebakken
**Bestand:** `v2/data/stroomroute-kobalt-ningbo-quzhou.json` (43,0 KB, contract versie 2, lonlat) · **recept:** `bash v2/tools/bak_stromen.sh kobalt-ningbo-quzhou` (functie `bak_kobalt_ningbo_quzhou`; b1 via het profiel `kobalt-ningbo-quzhou-ningbo-quzhou` in `maak_stroombeen_weg.py`, extract china, gescand met `kobalt-ningbo-quzhou-wegscan-wrapper.py` omdat pyosmium geblokkeerd is).

| # | modaliteit | km (bake) | punten | toets |
|---|---|---|---|---|
| b1 | truck (doorgetrokken) | 362,3 | 2.079 | indicatie: hemelsbreed 314 km (geen wegkm, dus geen norm); wegfactor 1,15 is normaal voor snelwegen; geen gepubliceerde wegkm om tegen te toetsen |

Totaal 362,3 km · 2.079 punten · 2 markers (beide op 0,0 m van de lijn) · geen naden (één been) · geen stippel, geen haven-aanloop, geen kopie, geen vlucht.

- **Wegtool:** zes segmenten, alle snaps 0,00 tot 0,04 km; segment-km 53,6 · 72,6 · 69,6 · 43,8 · 76,9 · 45,8. Alle vijf via-punten uit §4 hielden (op G1512 en G60, niet in een stadscentrum); geen verplaatst of geschrapt. Eindklassen service en tertiary: eerste 2,0 km en laatste 0,6 km over kleine wegen (park Quzhou), zoals in §2 verwacht.
- **Knikken:** `toets_knikken.py` 21 knikken >= 60 graden, 0 omkeringen, 0 terugloop; allemaal korte OSM-spikes (2 tot 174 m) bij kruispunten en de ankerstubs. `toets_rechte_benen.py --min-km 5` meldt niets voor deze stroom.
- **Open punten (zie §7):** modaliteit en aandeel via Ningbo niet gebrond (beennaam draagt "aannemelijk: een bron"); centraal: sitelaag kobalt mist de Quzhou-site en de knoop `co-quzhou-smelter` in `kobalt-tfm-quzhou` en `kobalt-morowali-quzhou` kan dicht; het anker in `nikkel-morowali-quzhou` (28.9020, 118.8780) ligt 3,6 km ernaast.
- **Lessen:** (1) de tussenuitvoer van een eerder afgebroken poging (ruwe pbf-ways, wrapper, geojson) was compleet en consistent met de brief en is hergebruikt; het profiel is daarna alsnog in `maak_stroombeen_weg.py` gezet (CRLF-bestand; `bak_stromen.sh` blijft LF, 0 CRLF); (2) een bake met alleen een vooraf gebakken `--been-geojson` duurt seconden maar laadt toch de AIS-graaf.
