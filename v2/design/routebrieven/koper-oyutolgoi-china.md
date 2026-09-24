# Routebrief (licht) · koper — Oyu Tolgoi → Ganqimaodu → Feishang (Binnen-Mongolië)

**stroom-id:** `koper-oyutolgoi-feishang` · **geschreven:** 2026-09-24 (LAR-562) · **werkwijze:** licht (M29) ·
**status:** concept
**Keten in één zin:** koperconcentraat (in 2 t-zakken, 16 per truck [4]) gaat per truck over de eigen betonweg van
Oyu Tolgoi ~105 km naar de grenspost Gashuun Sukhait, rijdt door de Chinese poort Ganqimaodu naar de bonded
warehouse "Huafang" ~7 km achter de grens waar de klant het overneemt [5], en vandaar per Chinese truck ~200 km
over G242/G335 naar de smelter van Bayannur Feishang Copper in het Qingshan-industriepark (Urad Achterbanner) —
de enige koperketen van de atlas zónder zee.
**Welke as van het verhaal:** Mongools concentraat over land naar China. OT produceerde in 2025 **345 kt koper
in concentraat** (+61 %) en verkoopt aan de grens ("collected by customers from the Mongolia/China border") [1];
Ganqimaodu importeerde jan–okt 2025 **1,215 Mt koperconcentraat** (¥25,4 mrd, +56 %) [7]; Feishang kocht in 2022
**158,2 kt OT-concentraat** via Ganqimaodu (35 % van zijn 451 kt voeding) [10] — de enige smelter met een
gedocumenteerde OT-levering; de rest van OT's 13 langetermijncontracten gaat via smelters "in diverse
provincies" en handelaren [5] (vertakking, zie §5).

## 1 · Ketenkaart
OT-concentrator/zakkenplant ──(b1 truck · OT-weg · ~105 km)──► Gashuun Sukhait ──(b2 truck · poort Ganqimaodu + G242 · ~7 km)──►
bonded warehouse Huafang ──(b3 truck · G242 甘临一级公路 → G335 承塔线 · ~198 km)──► smelter Feishang (Qingshan) ⏹ stoppunt

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (Mongoolse trucks, 2 t-zakken) | `cu-ot-laad` → `cu-ot-grens` | Oyu Tolgoi–Gashuun Sukhait-weg (OT-betonweg, "~60 mi concrete" [6]) | 105 [3] (Rio/IFC noemen "80 km" = ruwe afstand [2][4]) | maak_stroombeen_weg (profiel bestaat: `cu-oyutolgoi-gashuun`, kop verleggen naar het concentrator-anker) | nee |
| b2 | A | truck (dezelfde trucks rijden door tot de bonded warehouse, "één-stop"-inklaring [8]) | `cu-ot-grens` → `cu-ot-bonded` | grensdoorlaat → poortzone Ganqimaodu → G242 zuidwaarts | ~7 [5] | maak_stroombeen_weg | nee |
| b3 | C | truck (Chinese trucks van de koper; "by truck or train" [5], spoor niet aangetoond) | `cu-ot-bonded` → `cu-ot-smelter` | G242 甘临一级公路 (183 km tot Linhe [9]) tot afrit G335 承塔线, dan G335 west via Bayan Baolige naar Qingshan | ~198 (OSRM over OSM; geen onafhankelijke publicatie — G242-aandeel 132 km, G335 61 km) | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-ot-laad` | laadplek | Oyu Tolgoi concentrator + zakkenplant ("bagging plant") | 43.0480, 106.8360 | [4], OSM industrieterrein | bron-gelegd (z15/z16 gezien: molengebouwen, thickeners, ertsloods met band naar de put; de laadloods zelf niet apart onderscheiden — site-niveau) |
| `cu-ot-grens` | grensovergang | Gashuun Sukhait grenspost (MN) / Ganqimaodu (CN) | 42.4146, 107.5692 | OSM `border_control` | bron-gelegd (z15 gezien: grenspostgebouwen met vrachtwagen-opstelterreinen ten noorden, weg loopt door naar de Chinese poort) |
| `cu-ot-bonded` | overslag | bonded warehouse "Huafang", logistiekzone Ganqimaodu | 42.3740, 107.5990 | [5] (~7 km van de grens), [11] | aannemelijk (z15 gezien: loodsencomplex met opstelterrein naast het spooremplacement, ~5 km hemelsbreed / ~7 km over de weg van de grens; wélke loods Huafang is, is uit geen bron gebleken) |
| `cu-ot-smelter` | losplek / smelter | Bayannur Feishang Copper (巴彦淖尔市飞尚铜业), Qingshan-industriepark | 40.9694, 106.8530 | [12] MEE-register, USCC 91150800772247433C | bron-gelegd (z15 gezien: fabrieksterrein met hallen, tanks en opslag in een industriepark; registerpunt CGCS2000 = WGS-84, niet omgerekend) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | OT-weg ZO van de mijn | 42.9945, 106.9657 | pint de OT-betonweg i.p.v. de Tavan Tolgoi-kolenweg (Ухаахудаг–Гашуунсухайт) die westelijker loopt |
| b1 | 2 | middenstuk OT-weg | 42.7729, 107.3890 | zelfde keuze, corridor tussen de twee grensroutes |
| b1 | 3 | Tsagaan Khad-omgeving | 42.5785, 107.5437 | begin van het laatste (18,6 km) wegvak [3]; kolenweg en OT-weg komen hier samen |
| b2 | 1 | Chinese poort Ganqimaodu | 42.4089, 107.5743 | de doorlaat/douanezone; pint "door de poort" i.p.v. langs S212 om de poortzone heen |
| b3 | 1 | start G242 ten zuiden van de poortzone | 42.3887, 107.5711 | G242 zuid i.p.v. S212 oost |
| b3 | 2 | afrit G242 → G335 | 41.2704, 107.3697 | westelijk af naar G335 i.p.v. doorrijden naar Linhe (+~40 km) |
| b3 | 3 | Bayan Baolige (rayonhoofdplaats Urad Achterbanner) op G335 | 41.0790, 107.0729 | pint de G335-corridor door de hoofdplaats; projecteren op de G335-vertex (via-punt-op-zijtak-regel) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Feishang Copper, Qingshan-industriepark, Urad Achterbanner | Feishang Group (飞尚集团) | koperconcentraat (2022: 451 kt, waarvan 158 kt OT) → ruwkoper/anodeplaat + zwavelzuur; goud/zilver als bijproduct | 100 kt/j ruwkoper (anode), 375 kt/j zwavelzuur; jan–okt 2023 77,6 kt ruwkoper | [10][13][14] |
| Vertakking (niet getekend) | Jinchuan (Jinchang, Gansu) · Tongling (Jinchang-smelter Anhui, Chifeng-smelter Binnen-Mongolië) · Jiangxi Copper (Guixi) · handelaren (o.a. Trafigura) | intentieverklaringen 2004–2010 (150 / 50 / 150 kt/j) en "13 langetermijncontracten, smelters in diverse provincies" — geen enkele levering per smelter gedocumenteerd | — | [5][15][16] |

## 6 · Stoppunt
De brief stopt bij de smelter Feishang: die maakt anodekoper, geen kathode, en geen bron noemt de raffinaderij of fabriek
waar de anodes heen gaan — fase D is dus niet in één zin gegeven en wordt niet getekend.

## 7 · Open punten
- **Huafang-loods:** de bonded warehouse is alleen als "~7 km van de grens" gedocumenteerd [5][11]; het loodsencomplex op
  42.3740, 107.5990 is de beste kandidaat (spooremplacement ernaast), maar de naam is niet aan een gebouw gekoppeld.
- **Laadloods OT:** de zakkenplant/laadhal binnen het concentrator-complex is op z16 niet apart te onderscheiden; anker op site-niveau.
- **Spoor:** de Ganquan-spoorlijn (甘泉铁路, 366,9 km Ganqimaodu → Wanshuiquan-Zuid/Baotou, kolenlijn, 2012) bestaat [17] — dus
  níet naar Linhe zoals aangenomen — en de klant mag "by truck or train" afhalen [5]; geen bron dat OT-concentraat per spoor gaat.
  De grensoverschrijdende lijn Gashuun Sukhait–Ganqimaodu (32,6 km, dubbelspoorbreedte, bouw sinds 2025-05, spoorleggen sinds 2026-09,
  gepland 2027 [18][19]) zal b1/b2 straks vervangen — nu nog truck.
- **Aandeel Feishang:** 158 kt OT-concentraat in 2022 [10]; het huidige aandeel (OT +61 % in 2025) is onbekend, evenals de
  verdeling over de andere twaalf contractanten. De atlasstroom `cu-oyutolgoi → cu-ref-jinchuan` (120, rail) heeft geen bron.
- **Gepubliceerde km b3:** geen publicatie voor poort → Qingshan; de bake-toets loopt tegen de OSRM-lengte (198 km, zelfde bron als de extract).
- **Fase D:** afnemer van Feishangs anodes onbekend.

## 8 · Bronnen
[1] Rio Tinto, Q4 2025 production results (SEC 6-K, 2026-01-21): OT 345 kt koper in concentraat 2025 (+61 %), Q4 104 kt; "collected by customers from the Mongolia/China border" — https://www.sec.gov/Archives/edgar/data/863064/000086306426000006/ex1_2025-q4results.htm
[2] IFC project 29007 Oyu Tolgoi LLC: "80 km North West of the border post and rail head with China at Gashunn Sukhait … trucked along a dedicated new road" — https://disclosures.ifc.org/project-detail/SII/29007/oyu-tolgoi-llc
[3] Oyu Tolgoi LLC, "Construction of 18.6 km road from Tasgaan Khad to Gashuun Sukhait": 105 km weg gepland, 85,5 km gebouwd 2010–2013, laatste 18,6 km vanaf 2015 (pagina inmiddels offline, tekst via zoekindex) — https://www.ot.mn/ws2272197365-en/
[4] E&MJ, "Oyu Tolgoi: A Nation Changer" (2013): "Mongolian trucks leave the Oyu Tolgoi bagging plant for the border, 80 km to the south … bags, each weighing about 2 mt, with 16 bags loaded onto each truck"; eerste konvooi 16 trucks / 576 t — https://www.e-mj.com/features/oyu-tolgoi-a-nation-changer/
[5] Oyu Tolgoi Joint Venture NI 43-101 Technical Report (Entrée Resources, okt. 2021, §23-4): "sales transacted at a third-party warehouse facility at Huafang in China, approximately 7 km from the China-Mongolia border … delivery of the concentrate by truck or train to their respective smelters"; "13 long-term contracts … smelter customers are based in various provinces throughout China" — https://www.sec.gov/Archives/edgar/data/1271554/000127956921001447/ex991.htm
[6] NPR/KUER, "Mongolia's Long Road To Mining Wealth" (2019-07-31): "approximately 60 miles of well-maintained concrete", concentraat in witte zakken onder groen zeil, ~1.100 voertuigen/dag — https://www.kuer.org/2019-07-31/mongolias-long-road-to-mining-wealth
[7] 内蒙古经济网 (2025-11-11): jan–okt 2025 121,5万吨 koperconcentraat / ¥254,4亿 (+56,2 % / +106,9 %); cumulatief 1.006,56万吨 sinds 2013 — https://www.nmgsb.com.cn/system/mengshi/2025/1111352U2025.html · 内蒙古日报 (2025-10-19): jan–sep 107,3万吨 (+59,4 %), "距奥尤陶勒盖铜矿仅70公里" — https://szb.northnews.cn/nmgrb/html/2025-10/19/content_53978_267334.htm
[8] 中国有色网 (2014): "一站式"-inklaring van de Mongoolse mijn tot de Chinese bonded warehouse; 13,93万吨 t/m 2014-03-20 — https://www.cnmn.com.cn/ShowNews1.aspx?id=289154
[9] 中国建筑 (2019-03): G242 甘其毛都口岸至临河一级公路 183 km, 80 km/h, open maart 2019 — https://www.cscec.com/xwzx_new/gsyw_new/201903/2916864.html (内蒙古新闻网: 183,37 km — https://inews.nmgnews.com.cn/system/2019/03/13/012670314.shtml)
[10] 腾讯新闻/巴彦淖尔 (2023-12-28): Feishang 2022: 45,13万吨 concentraat gekocht, waarvan 32,28万吨 import incl. "从甘其毛都口岸进口OT铜精矿15.82万吨"; jan–okt 2023 7,76万吨 ruwkoper — https://news.qq.com/rain/a/20231228A00J8W00
[11] Cover Mongolia (2013-12-30, citeert BDSec/Business Mongolia): "70.2 thousand tonnes were delivered to Huafang bonded warehouse in Gants Mod (Ganqimaodu) border port" — https://covermongolia.blogspot.com/2013/12/
[12] MEE emissievergunningregister, vergunning 91150800772247433C001P (2025-07-22 t/m 2030-07-21, 铜冶炼, 重点管理): longitude 106.85298 / latitude 40.96935 (DMS 106°51'10.73" / 40°58'9.66") — https://permit.mee.gov.cn/perxxgkinfo/syssb/xkgg/xkgg!licenseInformation.action (zoek "飞尚铜业")
[13] 中国有色网 (2012-09-19): Feishang "位于乌拉特后旗青山工业园", 10万吨/j kopersmeltlijn — https://www.cnmn.com.cn/ShowNews1.aspx?id=250625
[14] 百度百科 巴彦淖尔市飞尚铜业有限公司: 青山工业园区, 年产粗铜（阳极板）10万吨、工业硫酸37.5万吨 — https://baike.baidu.com/item/巴彦淖尔市飞尚铜业有限公司/9252504
[15] Ivanhoe Mines/Entrée, OT Integrated Development Plan 2010 (6-K, 2010): Jinchuan "up to 150,000 dmt/a", Tongling "up to 50,000 dmt/a", JCCL MoU 2004 — https://www.sec.gov/Archives/edgar/data/0001271554/000127956910000741/ex991.htm
[16] Mongolian Mining Journal, "Trafigura signs off-take deal for Oyu Tolgoi" (2013) — https://www.mongolianminingjournal.com/a/54057?locale=en
[17] 维基百科 甘泉铁路: 甘其毛都站 → 万水泉南站 (包神铁路), 366,9 km, 电气化单线, 铺通 2012-09-15, kolen uit Tavan Tolgoi — https://zh.wikipedia.org/wiki/甘泉铁路
[18] 维基百科 甘其毛都口岸: 42°24′35″N 107°34′23″E; bouwstart 中蒙甘其毛都至嘎舒苏海图铁路 2025-05-14; eerste koperconcentraat juli 2013 — https://zh.wikipedia.org/zh-hans/甘其毛都口岸
[19] 腾讯新闻 (2026-09-03): 甘其毛都—嘎舒苏海图跨境铁路开始铺轨, 2027 in bedrijf — https://news.qq.com/rain/a/20260903A036W300


## 9 · Gebakken (2026-09-25. lichte werkwijze)

**Stroom `koper-oyutolgoi-feishang`** → `v2/data/stroomroute-koper-oyutolgoi-feishang.json` — 2 benen. 300 km. 4 markers: truck 300 km.
Recept: `bak_stromen.sh` (functie voor deze stroom). Toelichting: één wegscan (profiel `koper-oyutolgoi-feishang`. Mongolië + China). 299.6 km (−3.4% t.o.v. ~310; OT → grens 104 km tegen 105 gepubliceerd) — de eerste bake week 129 km westwaarts uit omdat de OT-weg in OSM `tertiary` is; met `corridorKlassen: tertiary` klopt hij. Gesplitst op het bonded-anker in twee benen (107.9 + 191.7 km).
