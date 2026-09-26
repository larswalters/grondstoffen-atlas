# Routebrief (licht) · grafiet — Jinzhou → Zhangjiakou → Baotou (China)

**stroom-id:** `grafiet-jinzhou-baotou` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) ·
**status:** gebakken
**Keten in één zin:** naaldcokes/petroleumcokes (synthetische grafiet-feedstock) van CNPC Jinzhou
Petrochemical (Liaoning) per spoor (werkaanname) over de Jingbao-lijn via Shanhaiguan, Zhangjiakou
en Hohhot naar de grafitisatie-/anodematerialenbasis van Shanshan (Jiuyuan Industrial Park, Baotou,
Binnen-Mongolië) — de enige as van de zes zonder zee, en de as met het hoogste ontwerprisico.
**Welke as van het verhaal:** de synthetische trechter op goedkope kolenstroom: Binnen-Mongolië is
één van de grote Chinese grafitisatiepolen (naast Shandong voor natuurlijk vlok); Chinese anode-
bedrijven leverden 990 van 1.040 kt AAM wereldwijd in 2024 (SNE Research, via ontwerp). Bedrijfs-
niveau bewijst de relatie (CNPC–Shanshan kaderakkoord 2021 [1]), geen bron noemt de ontvangende
Shanshan-fabriek — vandaar "aannemelijk" in de beennaam, niet fictie.

## 1 · Ketenkaart
```
CNPC Jinzhou Petrochemical `gr-jinzhou-fabriek` ──(b1 spoor, werkaanname, aannemelijk: kader-
akkoord 2021, fabriek niet genoemd · Jingbao-lijn via Shanhaiguan → Zhangjiakou → Hohhot ·
~1.300 km)──► Shanshan Baotou Jiuyuan `gr-baotou-jiuyuan` ⏹ stoppunt (fase D niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor (werkaanname — bulk naaldcokes gaat in China doorgaans per spoor; truck niet uitgesloten) | `gr-jinzhou-fabriek` → `gr-baotou-jiuyuan` | Jingbao-lijn (京包铁路): Jinzhou → Shanhaiguan → Beijing-omleiding → Zhangjiakou → Jining → Hohhot → Baotou | ~1.300 spoor / ~1.200 weg G1/G6 [ontwerp, niet onafhankelijk gepubliceerd] | `toets_spoorroute.mjs` (BAKE_SUFFIX=-raw, 1-op-1-net) in stukken kop→Zhangjiakou, Zhangjiakou→staart | nee (doorgetrokken; emplacement-uiteinden aan beide kanten waarschijnlijk kort gestippeld — Chuqui/Matarani-les) |

Fase D (Shanshan Baotou → celfabriek, kandidaten CATL Ningde/BYD) is **niet getekend**: Shanshan is
leverancier, maar geen bron koppelt de Baotou-basis aan één celfabriek (ontwerp §risico).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-jinzhou-fabriek` | feedstock (kop, geen mijn-aandeel) | CNPC Jinzhou Petrochemical (中国石油锦州石化), 重庆路2号, Guta, Jinzhou, Liaoning | 41.13159, 121.08583 | [1][13][14][15] | bron-gelegd (z15 gezien: raffinaderijcomplex met een tankenpark en procesinstallaties direct noordelijk van het punt, in de "Shiyou"/petroleum-wijk van Guta; spoordepot en laadspoor grenzen zuidelijk aan het terrein) |
| `gr-baotou-jiuyuan` | grafitisatie-/AAM-basis (staart) | Shanshan (Inner Mongolia Shanshan New Material), Jiuyuan Industrial Park, Baotou, Binnen-Mongolië | 40.60860, 109.67826 | [4][11][12] | aannemelijk (z14 gezien: dichte cluster chemie-/batterijmateriaalfabrieken met een verdampings-/tailingsvijver, past bij de naam "Jiuyuan Industrial Park"; welk perceel exact Shanshan is, is tussen de vele bedrijven in het park niet individueel te onderscheiden) |

## 4 · Via-punten (alleen b1 — corridorkeuze op de Jingbao-lijn)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Shanhaiguan-station | 39.97717, 119.77003 | pint de kustcorridor (Jingha-lijn) richting de Beijing-ring i.p.v. direct landinwaarts vanaf Jinzhou |
| b1 | 2 | Zhangjiakou-station | 40.74952, 114.87661 | de corridorkeuze zelf (via Beijing-ring vs. de Datong–Qinhuangdao-kolenlijn in omgekeerde richting); ook het punt waar de bak-agent de spoorrouter in twee stukken splitst (kop→Zhangjiakou, Zhangjiakou→staart) |
| b1 | 3 | Hohhot-station | 40.83043, 111.65872 | laatste vaste punt op de Jingbao-lijn vóór Baotou; pint de doorgaande hoofdlijn i.p.v. een noordelijker aftakking |

Alternatief (niet gekozen, wel genoemd): Datong-station (40.11910, 113.29634) op de
Datong–Qinhuangdao-kolenlijn in omgekeerde richting — de corridor die het ontwerp als tweede optie
noemt naast de Beijing-ring.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Jinzhou Petrochemical naaldcokesfabriek | CNPC/PetroChina | petroleum (Sinopec/PetroChina-cokes) → naaldcokes/petroleumcokesproduct | 150 kt/j in bedrijf + 400 kt/j in aanbouw (mechanisch gereed okt. 2024) = 350 kt/j product na opstart | [2][3] |
| Shanshan Baotou Jiuyuan | Shanghai Shanshan Technology / Inner Mongolia Shanshan New Material | naaldcokes/petroleumcokes → grafitisatie + AAM (anodemateriaal) | fase 1: 100 kt AAM (in bedrijf sinds aug. 2019); fase 2: +60 kt AAM + 52 kt grafitisatie | [5][11] |

Los, niet op deze as: Shanshan kondigde 2026-09-22 een nieuw 150 kt/j-anodeproject aan in Baotou
**Qingshan** (bouw 2027–28) [6] — een ander perceel dan de bestaande Jiuyuan-basis en daarom niet
als eindpunt van dit been gebruikt (ontwerp §aanpassing).

## 6 · Stoppunt
De brief stopt bij de bestaande Shanshan-basis in Jiuyuan: dat is de enige plek waar het bedrijfs-
niveau-bewijs (kaderakkoord 2021) en een gelegd anker samenkomen. Fase D vervalt — Shanshan levert
aan celfabrieken, maar geen bron noemt welke.

## 7 · Open punten
- **Geen gepubliceerd volume Jinzhou → Baotou.** Het kaderakkoord (2021) bewijst de relatie op
  bedrijfsniveau ("uitgebreid tot alle petroleumcokesproducten", afname sinds 2016 +403%), maar
  welke Shanshan-fabriek (Baotou, Meishan, Anning) de Jinzhou-cokes ontvangt staat nergens met
  naam. Vandaar "aannemelijk" in de beennaam, niet in de lijnstijl (been blijft doorgetrokken).
- **Modaliteit spoor is een werkaanname.** Geen bron noemt expliciet spoor voor dit 1.300 km-
  traject; een wegalternatief (G1/G6, ~1.200 km) is niet uitgesloten. De china-Geofabrik-extract
  is aanwezig voor een eventuele wegscan als het spoorbeen niet aannemelijk blijkt.
- **Exact perceel Shanshan Jiuyuan niet individueel bevestigd** — het Jiuyuan-industriepark bevat
  meerdere chemie-/batterijmateriaalbedrijven; een MEE-registerzoekopdracht op de rechtspersoon
  (recept: `zoek-chinees-adres-recept.md`) is niet gelukt binnen het tijdsbudget van deze ronde.
- **Terugvalregel (ontwerp):** accepteert Lars "aannemelijk (bedrijfsniveau)" niet als voldoende
  bron voor een gemeten, doorgetrokken stroom, dan wordt deze as **geen stroom** maar een
  gloedcluster (Jinzhou/Baotou/Wuhai/Ulanqab) in de sitelaag — dat is een resultaat, geen
  mislukking (Escondida-fase-E-les).
- **Emplacement-uiteinden ontbreken waarschijnlijk in het 1-op-1-spoornet** (laadspoor bij
  Jinzhou, aansluitspoor bij Shanshan Jiuyuan) → korte stippels aan beide zijden zijn normaal
  (Chuqui 9 km / Matarani 1,7 km-les), geen fout van de bake.
- **Capaciteiten gecorrigeerd t.o.v. het ontwerp** (toets §problemen): Jinzhou 150 kt in bedrijf +
  400 kt in aanbouw = 350 kt/j product (niet 170 kt); Shanshan Baotou fase 1 100 kt + fase 2 60 kt
  AAM + 52 kt grafitisatie (niet 100/50 kt). "Binnen-Mongolië is dé grafitisatiepool" is te stellig
  — Shanshans 600 kt geplande capaciteit ligt verdeeld over Binnen-Mongolië, Sichuan en Yunnan [4].

## 8 · Bronnen
[1] CNPC nieuwsbericht, 2021-03-25 — kaderakkoord Jinzhou Petrochemical – Shanghai Shanshan Technology, samenwerking sinds 2016, afname +403%, uitgebreid tot alle petroleumcokesproducten. http://news.cnpc.com.cn/system/2021/03/25/030027986.shtml
[2] 人民网辽宁 (ln.people.com.cn), 2023-12-05 — Jinzhou 150 kt/j in bedrijf + 400 kt/j-installatie in aanbouw, hoofdwerk gereed eind 2023. http://ln.people.com.cn/n2/2023/1205/c400024-40666177.html
[3] 新浪财经 (finance.sina.com.cn), 2024-10-16 — mechanische oplevering okt. 2024, totaal 350 kt/j naaldcokesproduct. https://finance.sina.com.cn/roll/2024-10-16/doc-incsueav7172893.shtml
[4] 经济观察网 (m.eeo.com.cn), 2025-05-15 — Shanshan-leveranciers PetroChina/Sinopec/CNOOC voor naaldcokes/petroleumcokes/gecalcineerde cokes; 600 kt geplande capaciteit verdeeld over Binnen-Mongolië, Sichuan, Yunnan. http://m.eeo.com.cn/2025/0515/726745.shtml
[5] China Daily exchange-partnerpagina, ca. 2022 — Shanshan Baotou fase 2: +60 kt AAM + 52 kt grafitisatie. http://ex.chinadaily.com.cn/exchange/partners/82/rss/channel/cn/columns/sz8srm/stories/WS61d55e4ba3107be497a00d8a.html
[6] 新浪 (k.sina.cn), 2026-09 — nieuw 150 kt/j-anodeproject Baotou Qingshan, bouw 2027–28. https://k.sina.cn/article_1838672663_6d97eb1702001qcna.html
[7] Metal.com nieuwsbericht — Shanshan Technology commissions battery anode materials base in Inner Mongolia (aug. 2019, 100 kt fase 1). https://news.metal.com/newscontent/100957952-Shanshan-Technology-commissions-battery-anode-materials-base-in-Inner-Mongolia
[8] Asian Metal — Jinzhou Petrochemical commissions needle coke project, totaal 350 kt/j na volledige opstart. https://www.asianmetal.com/news/2118697/Jinzhou-Petrochemical-commissions-needle-coke-project/1
[9] Businesswire/ResearchAndMarkets, 2022 — Global and China Needle Coke Industry Report (7 mondiale + 16 Chinese naaldcokesproducenten). https://www.businesswire.com/news/home/20221012005677/en/Global-and-China-Needle-Coke-Industry-Report-2022-2027-Featuring-7-Global-and-16-Chinese-Needle-Coke-Producers---ResearchAndMarkets.com
[10] SNE Research — Chinese anodebedrijven 990 van 1.040 kt wereld-AAM 2024. https://www.sneresearch.com/en/insight/release_view/392/page/0
[11] 百度百科 内蒙古杉杉新材料有限公司 — adres 包头市九原区南绕城46公里处九原工业园区清和路2号, opgericht 2018-01, productie sinds 2019, volledig op capaciteit 2022. https://baike.baidu.com/item/内蒙古杉杉新材料有限公司/51165316
[12] 上海杉杉科技 bedrijfswebsite, 公司概况 — 九原工业园区清和路2号 als adres van de Binnen-Mongolië-basis. https://www.shanshantech.com/en/company-profile
[13] PetroChina Refining and Marketing contactpagina — Jinzhou Petrochemical Company, 2 Chongqing Road, Guta District, Jinzhou City, Liaoning Province. https://www.petrochina.com.cn/ptr/lxxx/201404/ff7f5b80d7a34aa383f1042c117d5dfa.shtml
[14] 百度百科 中国石油天然气股份有限公司锦州石化分公司 — 总部地址 辽宁省锦州市古塔区. https://baike.baidu.com/item/中国石油天然气股份有限公司锦州石化分公司/23440063
[15] OpenStreetMap (ODbL) via Nominatim — 重庆路 in Shiyou Subdistrict/Jingye Subdistrict, Guta, Jinzhou (kandidaatsegmenten getoetst op satelliet); 清和路 + suburb-node "九原工业园区", Jiuyuan District, Baotou; stationsknopen Shanhaiguan/Zhangjiakou/Datong/Hohhot op de Jingbao/Jingha-lijn. https://www.openstreetmap.org
[16] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15, live) — `v2/build-cache/satcheck/sat-grafiet-jinzhou-baotou-jinzhou-cand2.png` (Jinzhou-raffinaderij, gekozen), `sat-grafiet-jinzhou-baotou-jinzhou-cand1.png` (verworpen kandidaat, gewone woonwijk), `sat-grafiet-jinzhou-baotou-baotou-qinghe.png`, `sat-grafiet-jinzhou-baotou-baotou-jiuyuanpark.png` (gekozen).

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `grafiet-jinzhou-baotou`** → `v2/data/stroomroute-grafiet-jinzhou-baotou.json` — 2 benen,
1.153,3 km, 2 markers: spoor 681,0 km (Jinzhou → Zhangjiakou) · spoor 472,3 km (Zhangjiakou → Baotou
Jiuyuan).
Recept: `bak_stromen.sh` (functie `bak_grafiet_jinzhou_baotou`). Toelichting: twee spoorrouter-runs
(`BAKE_SUFFIX=-raw`, 1-op-1-net `raw1op1/china`), gesplitst bij Zhangjiakou-station omdat
`toets_spoorroute.mjs` geen `--via` kent. Been 1 raakt Shanhaiguan-station op 2,4 km (pint de
kustcorridor); been 2 raakt Hohhot-station op 0,4 km (pint de doorgaande Jingbao-hoofdlijn) — beide
bevestigen de gekozen corridor tegenover het alternatief (Datong-lijn). Naad been 1 → 2 = 0,0 km
(beide runs snappen op dezelfde Zhangjiakou-knoop, hoofdnet-knoop 471256). Totaal 1.153,3 km tegen de
indicatieve ~1.300 km uit het ontwerp (niet onafhankelijk gepubliceerd) = **−11,3%**, binnen de door
de brief zelf verruimde marge (tot ~15%, want minder hard bewijs dan bij de andere assen).

**Toets-bevindingen (buiten de norm, niet dichtgetrokken):**
- **Eén TERUGLOOP** (`toets_knikken.py`): 180° bij 41,12240/121,14360, 4,9 km van het Jinzhou-anker,
  ratio pad÷hemelsbreed ≈99. Getest met `--keerstraf` tot 200 km (10× de standaardwaarde 25 km): de
  omkering blijft — dus topologisch afgedwongen door het 1-op-1-net, geen routerkeuze die met een
  hogere straf te vermijden was. Zelfde klasse als de emplacement-stubs bij Chuqui (9 km) en Matarani
  (1,7 km): het laadspoor/rangeerterrein bij Jinzhou hangt kennelijk via een doodlopende spur aan het
  hoofdnet. Niet gerepareerd (geen shotgun-fix); staat hier als bevinding, niet dichtgetrokken.
- Snap Baotou-eind 1,22 km (marker "Shanshan Baotou Jiuyuan" tot de geroutete lijn) — boven de
  0,5 km-norm, maar verwacht: brief §7 zegt al dat het exacte Shanshan-perceel binnen het Jiuyuan
  Industrial Park niet individueel is bevestigd (anker ≠ routeerpunt). Snap Jinzhou-kop 0,09 km, ruim
  binnen de norm.
- Geen aparte gestippelde emplacement-stub getekend aan de uiteinden: de gemeten snapafstanden
  (0,09 / 1,22 km) waren te klein om als eigen `--stippel`-segment te tekenen zoals bij Chuqui
  (9 km)/Matarani (1,7 km) — de anker-tot-lijn-afstand staat hierboven als bevinding in plaats van
  als getekende stippel.
- `toets_rechte_benen.py --min-km 5`: geen enkel been van deze stroom in de verdachtenlijst (beide
  benen zijn echte 1-op-1-spoorgeometrie, geen stippel, omwegfactor ≠ 1,000).
- JSON-vormtoets: `versie` 2, `punt_formaat` `lonlat`, modaliteit {spoor} (toegestaan), elk been
  ≥2 punten, bestand 51,0 KB (< 300 KB) — allemaal in orde.

**Gereedschapslessen:** een out-and-back-terugloop kan **topologisch afgedwongen** zijn door het
1-op-1-spoornet (bevestigd door de keerstraf te verhogen tot 200 km zonder effect op de omkering) —
dus niet elke terugloop is een routerkeuze die om reparatie vraagt, ook al meldt `toets_knikken.py`
een terugloop standaard als "hoort gerepareerd te worden". Bij een geïsoleerd emplacement/laadspoor
is dat repareren niet mogelijk zonder het net zelf aan te vullen (buiten de scope van deze lichte
bake) — het blijft daarom hier gedocumenteerd als bevinding, net als de Chuqui/Matarani-emplacement-
gaten.
