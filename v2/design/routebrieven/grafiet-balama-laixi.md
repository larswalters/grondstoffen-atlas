# Routebrief (licht) · grafiet — Balama → Nacala → Qingdao → Laixi (China)

**stroom-id:** `grafiet-balama-laixi` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** natuurlijk vlokgrafiet (in 1-t-zakken, gecontaineriseerd bij de Grindrod Cross Dock) gaat per **truck** over de N380/N1 van de Balama-plant (Syrah) naar de containerterminal van Nacala, per **containerschip** over de Indische Oceaan, Malakka en de Gele Zee naar de Qianwan-containerhaven van Qingdao (QQCT, aannemelijk), en per **truck** over G22/G15/S214 ~150 km naar de sferisch-grafietfabriek van Qingdao Shinestar (ex-Guangxing Electronic Materials, gelieerd aan contractpartij Langruite) in Nanshu, Laixi — het hart van het Chinese natuurlijk-grafietcluster.
**Welke as van het verhaal:** *ex-China vlok vaart naar China om verwerkt te worden* — de emblematische as van grafiet (China 1.400 van 1.800 kt wereldproductie 2025; ~82 % [4]). **Volume eerlijk gelabeld:** contract Langruite 2018/2019 = min. 48 kt + 12 kt optie, vanaf juni 2019 alleen coarse flake [2][3]; **2025: Balama 67 kt geproduceerd, 55 kt verkocht, géén verkoop aan Chinese anodeklanten** (Syrah AR 2025 [1]); China's import van natuurlijk grafiet uit Mozambique 2024 = US$5,02 mln ≈ 5 kt (UN Comtrade [5]), niet aan Syrah/Laixi toe te schrijven (USGS: een Chinese mijn in Niassa produceert sinds 2025 [4]). Volume voor de kaart: **nul in 2025/26** — de weg is echt, de lading niet (Lars-besluit 2026-08-04). Eenheid: mijn = kt vlokconcentraat/j; verwerker = kt sferisch grafiet (SPG)/j.

## 1 · Ketenkaart
```
Balama-plant `gr-balama-plant` ──(b1 truck · N380 → Metoro → N1 → Namialo → N12 → Nacala · 497,9 km — LETTERLIJKE KOPIE bak_grafiet been 1)──► Nacala containerterminal `gr-nacala-kade`
   ──(aanloop Nacala · $BEEN/aanloop-nacala.geojson 152,1 km stippel over water — LETTERLIJKE KOPIE)──► zeeknoop 2148 (-15.0, 41.7)
   ──(b2 zee · Indische Oceaan → Malakka → Zuid-Chinese Zee → Taiwanstraat → Gele Zee · ≈ 10.040 km hemelsbreed, MARNET)──► QQCT Qianwan-kade `gr-qingdao-qqct-kade` (zeeknoop 5841 op 5,6 km, geen aanloop)
   ──(b3 truck · S7602 → G22 → G15 om de Jiaozhou-baai → afrit Laixi-west → S214 · ~150 km, aannemelijk: één bron, contract 2018)──► Qingdao Shinestar SPG-fabriek, Nanshu `gr-laixi-shinestar` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (Grindrod, gedekte trucks, 1-t-zakken) | `gr-balama-plant` → `gr-nacala-kade` | N380 → Metoro → N1 → Namialo → N12 → Nacala | 497,9 (gebakken; brief grafiet-balama-vidalia ~485) [13] | **kopie** `$BEEN/stroombeen-balama-nacala.geojson` (profiel `grafiet-balama-nacala`) — geen tweede versie | nee |
| — | A | zee (aanloop) | `gr-nacala-kade` → zeeknoop 2148 | Baai van Nacala → open zee | 152,1 (gemeten over water) [13] | **kopie** `$BEEN/aanloop-nacala.geojson` (maak_havenaanloop, bestaat) | ja — MARNET reikt niet (122 km) |
| b2 | B | zee (containerlijndienst, 20-ft-containers) | zeeknoop 2148 → `gr-qingdao-qqct-kade` | Indische Oceaan → Straat Malakka → Zuid-Chinese Zee → Taiwanstraat → Gele Zee → Jiaozhou-baai | ≈ 10.040 hemelsbreed; gepubliceerd: geen (35–40 dagen volgens branche) | MARNET `--been "zee|…|-15.0,41.7|36.0124,120.2070"`; zeeknoop 5841 (36.0313, 120.2646) ligt 5,6 km van de kade → snapt binnen 25 km, geen aanloop | nee (losplek aannemelijk: geen bron noemt de terminal) |
| b3 | C | truck (Chinese trucks, containers/zakken) | `gr-qingdao-qqct-kade` → `gr-laixi-shinestar` | 疏港高架路 → S7601/S7602 港区疏港高速 → G22 青兰高速 → G15 沈海高速 (west om de Jiaozhou-baai, langs Jiaozhou) → afrit Laixi-west → S214 南城路 → Nanshu | ~150 (OSRM over OSM 149,6; geen onafhankelijke publicatie) [11] | maak_stroombeen_weg, extract `china`, profiel `grafiet-balama-laixi-qingdao-nanshu`, refs G22/G15/S214, vensterKm 40 | nee — *aannemelijk: één bron (contract 2018, leveringen 2025 nul)*; kade-stub < 1 km mogelijk (terminalwegen privé) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-balama-plant` | mijn / laadplek | Balama-plant, bagging on-site (Syrah/Twigg) | -13.3100, 38.6600 | [13] bestaand anker | bron-gelegd — hergebruik (z14 gezien [12]: procesfabriek met bezinkvijvers, stortplaats en zonnepark, put ten ZW; ankercheck 2026-07-28) |
| `gr-nacala-kade` | overslag truck → zee (Cross Dock: zak → container; ligplaats) | Porto de Nacala — containerterminal oostoever | -14.5383, 40.6673 | [13] bestaand anker | bron-gelegd — hergebruik (z15 gezien [12]: containerterminal met kadekranen en containeryard op de oostoever, punt op de noordkop van de kade; kolen-jetty westoever bewust niet) |
| `gr-qingdao-qqct-kade` | losplek zee | Qingdao Qianwan Container Terminal (QQCT), ZO-kade van het QQCT-schiereiland, Qianwan | 36.0124, 120.2070 | [10][11] OSM-industrievlak 青岛前湾集装箱码头 (-, 36.0099/120.1924 centroïde) | **aannemelijk** (z15 gezien [12]: doorlopende kraanrij met containerschepen langszij op de ZO-kade van het schiereiland; wélke Qingdao-terminal (QQCT Qianwan vs Dongjiakou) staat in geen bron — gekozen als dichtst bij MARNET-knoop 5841 en de lijnen ex-Afrika) |
| `gr-laixi-shinestar` | verwerkingsknoop / losplek (SPG-fabriek) | 青岛新广星石墨材料有限公司 (Qingdao Shinestar Graphite Materials, ex-青岛广星电子材料), 镇宁路1号, Nanshu, Laixi | 37.0252, 120.3224 | [6] MEE-vergunning 91370285MACJTLFM79001U (longitude 120.32238 / latitude 37.02517; DMS 120°19'20.57" / 37°01'30.61" identiek; CGCS2000 = WGS-84, niet omgerekend); [7] adres | bron-gelegd (z15 gezien [12]: blok blauwdak-fabriekshallen in de industriezone direct ten noorden van Nanshu-stad, aan de weg naar de S214) |

## 4 · Via-punten (alleen b3 — b1 is een kopie, b2 is router)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | S7602 青岛前湾港区2号疏港高速, uitrit havengebied | 36.0449, 120.1528 | pint de westelijke haven-uitvalsweg (2号疏港) i.p.v. 1号疏港/环湾路 langs de baai naar het noorden |
| b3 | 2 | samenvloeiing G22 青兰高速 → G15 沈海高速 | 36.0573, 119.9736 | pint "om de baai heen via G15" i.p.v. de Jiaozhou-baai-brug (G22 oost) → Qingdao-noord → G204 |
| b3 | 3 | G15 ten noorden van Jiaozhou (splitsing) | 36.3890, 120.0259 | pint doorrijden op G15 noord i.p.v. G204/S202 (烟沪线) door Jimo |
| b3 | 4 | afrit G15 → S214 南城路 (Laixi-west) | 36.7634, 120.3366 | pint de afrit naar de S214 i.p.v. doorrijden naar Laixi-stad; S214 loopt rechtstreeks naar Nanshu |
| b3 | 5 | S214 aankomst Nanshu, afslag naar 水晶路/industriezone | 37.0170, 120.3339 | pint de S214-nadering uit het zuiden; laatste ~1,5 km lokale weg naar het registerpunt (eindKlassen) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Grindrod Cross Dock, Nacala (geen eigen been) | Grindrod / Syrah | zakken op truck → 20-ft-containers → containerterminal | 60.000 m², 3.500-TEU-yard; Nacala 2023 opgewaardeerd (walkranen) | [1][13] |
| Qingdao Shinestar (ex-Guangxing), Nanshu | 青岛新广星石墨材料 (opgericht 2023-05 als opvolger van Guangxing, 2010) | vlokgrafiet → sferisch grafiet, hoogzuiver grafiet, alkalinebatterijpoeder, microfijn | ~30 kt/j alle grafietproducten (2019, Guangxing); SPG-aandeel niet gepubliceerd; twee vergunningen (hoofdvestiging + 分厂 op 37.0171, 120.3405), 简化管理 | [6][7][8] |
| Laixi/Nanshu-cluster (context) | 120+ bedrijven | vlok → gezuiverd/sferisch grafiet | > 50 % van de nationale gezuiverd-grafietproductie, 30 % van de nationale handel (2023) | [9] |

## 6 · Stoppunt
De brief stopt bij de SPG-fabriek in Nanshu: geen bron noemt de anodefabrikant die Shinestar/Guangxing-SPG afneemt (fase D niet in één zin gegeven), en de contractpartij Langruite is een handels-/zusterentiteit zonder eigen vergunning of adres in het MEE-register — fase D en E vervallen.

## 7 · Open punten
- **Lading 2025/26 = nul:** Syrah meldt voor 2025 géén natuurlijk-grafietverkoop aan Chinese anodeklanten [1]; of Langruite nog coarse flake (refractair) afneemt is sinds 2019 niet gepubliceerd. De as blijft staan als emblematische route met volume-nul in de beennaam; geen omleiding naar Pemba/Maputo.
- **Losplek Qingdao:** geen bron noemt de terminal; QQCT Qianwan gekozen (5,6 km van zeeknoop 5841; Dongjiakou ligt 22 km van zeeknoop 5836). Op z15 zijn QQCT (schiereiland) en de zuidoever-terminals van Qianwan niet uit een bron te onderscheiden — anker blijft aannemelijk.
- **Langruite** (青岛朗瑞特石墨): geen MEE-vergunning, geen adres gevonden; het anker is de gelieerde Shinestar/Guangxing-vestiging. Registerpunt = vestiging, geen losdock; welke van de twee vergunde locaties (hoofd/分厂, 1,7 km uit elkaar) het vlok verwerkt is onbekend.
- **b3 zonder gepubliceerde km:** de bake-toets loopt tegen OSRM (149,6 km, zelfde OSM-bron); de terminalwegen van QQCT zijn privé (OSRM snapt de start 750 m noordelijker op de openbare weg) → verwacht een korte kade-stub.
- **Transshipment:** containerlijnen ex-Nacala lopen via een hub (Durban/Port Louis/Singapore — niet gebrond); MARNET tekent de directe route.
- **Nacala Cross Dock:** exacte plek binnen het havengebied nog steeds niet gevonden (open sinds grafiet-balama-vidalia §5); geen eigen been.
- De China-import uit Mozambique (US$5,02 mln 2024) kan de nieuwe Chinese Niassa-mijn zijn [4] — een andere keten, niet getekend.

## 8 · Bronnen
[1] Syrah Resources, 2025 Annual Report (mrt 2026): Balama 67 kt geproduceerd (2024: 35 kt), 55 kt verkocht aan derden (2024: 50 kt, US$606/t CIF), 3 × ~10 kt breakbulk Pemba → Indonesië + maiden breakbulk VS + containerzendingen ex-Nacala; "There were no natural graphite sales to Chinese anode customers"; Nacala cross dock, containerlijnen naar Azië/India/Europa/VS. https://www.datocms-assets.com/65260/1774572803-syr_2025_annual_report.pdf
[2] Mining Review, 21-12-2018: bindende termijnovereenkomst Syrah – Qingdao Langruite Graphite, min. 48 kt in 2019 + 12 kt optie, fine + coarse; Langruite (Shandong) = gelieerd aan Qingdao Guangxing Electronic Materials (sferisch grafiet, refractair, spotzaken 2018). https://www.miningreview.com/top-stories/syrah-qingdao-langruite-graphite/
[3] Mining Review, 19-06-2019: Gredmann-overeenkomst (9 kt/maand fines naar China, jun 2019–dec 2021); Langruite-overeenkomst gewijzigd naar uitsluitend coarse flake. https://www.miningreview.com/battery-metals/syrah-resources-secures-graphite-fines-sales-into-china/
[4] USGS, Mineral Commodity Summaries 2026 — Graphite (natural): China 1.400 kt / wereld 1.800 kt (2025e), Mozambique 60 kt (2024: 39), Tanzania 75, Madagaskar 80; Chinese mijn in Niassa gestart 2025, Balama herstart juni 2025; SPG-export China jan–sep 2025 37,4 kt. https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-graphite.pdf
[5] Trading Economics / UN Comtrade: China imports of natural graphite from Mozambique 2024 = US$5,02 mln. https://tradingeconomics.com/china/imports/mozambique/natural-graphite
[6] MEE emissievergunningregister: 青岛新广星石墨材料有限公司 91370285MACJTLFM79001U (2023-10-20 t/m 2028-10-19, 石墨及碳素制品制造, 简化管理) longitude 120.32238 / latitude 37.02517; 分厂 …002Q 120.34051 / 37.01705. https://permit.mee.gov.cn/perxxgkinfo/syssb/xkgg/xkgg!licenseInformation.action (zoek "新广星")
[7] 青岛新广星石墨材料有限公司 — "原名：青岛广星电子材料有限公司", 位于莱西市; adres 青岛莱西市南墅镇镇宁路1号. http://www.qdguangxing.cn/about · CFSMA-ledenlijst (Qingdao Shinestar Graphite Materials, 镇宁路1号) http://zh.cfsma.org.cn/a/397.html
[8] Sohu, 12-04-2019: 青岛广星电子材料 opgericht 2010-08-16, Nanshu/Laixi, ~30.000 t/j grafietproducten (球形石墨, 鳞片石墨, 高纯石墨粉, 碱性电池粉, 微粉). https://www.sohu.com/a/307558035_685190
[9] 青岛日报, 10-10-2023: Laixi/Nanshu = grootste natuurlijk-grafietcluster van China, 120+ bedrijven, > 50 % van de nationale gezuiverd-grafietproductie. https://www.dailyqd.com/guanhai/280324_1.html
[10] Wikipedia (zh): 青岛前湾保税港区 (前湾港 = containerhavengebied van Qingdao, Huangdao); 南墅镇 37.0159/120.32232. https://zh.wikipedia.org/wiki/青岛前湾保税港区 · https://zh.wikipedia.org/wiki/南墅镇
[11] OpenStreetMap (ODbL) via Nominatim: industrievlak 青岛前湾集装箱码头 36.0099/120.1924; 南墅镇 37.0227/120.3288; 胶州湾大桥. OSRM (OSM) QQCT → registerpunt Nanshu 149,6 km via S7602/G22/G15/S214 (stappenlijst = via-punten §4). https://www.openstreetmap.org · https://router.project-osrm.org
[12] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15, live, 2026-09-26): `v2/build-cache/satcheck/sat-grafiet-balama-laixi-qianwan-overzicht.png`, `-qqct-kade.png`, `-nanshu-hoofd.png`, `-nanshu-fenchang.png`, `-balama.png`, `-nacala.png`.
[13] Atlas: `v2/design/routebrieven/grafiet-balama-vidalia.md` (ankers Balama-plant, Nacala-terminal, Cross Dock, N380/N1-corridor) en `bak_grafiet` in `v2/tools/bak_stromen.sh` (been 1 497,9 km, `aanloop-nacala.geojson` 152,1 km naar zeeknoop 2148).
[14] Syrah Q2 2026 quarterly (slides via Investing.com): Balama 2,3 kt in Q2 2026, campagne uitgesteld naar Q3, FY26-guidance 60–80 kt; Vidalia "nears commercial sales". https://www.investing.com/news/company-news/syrah-q2-2026-slides-balama-curtailed-vidalia-nears-commercial-sales-93CH-4807440

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `grafiet-balama-laixi`** → `v2/data/stroomroute-grafiet-balama-laixi.json` — 4 benen. 13.299,7 km. 4 markers: truck 497,9 km · zee (stippel) 152,1 km · zee 12.499,7 km · truck 150,0 km.
Recept: `bak_stromen.sh` (functie `bak_grafiet_balama_laixi`). Toelichting: been 1 (Balama → Nacala, N380/N1, 497,9 km) en de haven-aanloop Nacala (152,1 km, stippel — MARNET reikt hier niet, over water) zijn **letterlijke kopieën** van `bak_grafiet` (Balama→Vidalia) — geen tweede scan/aanloop-poging. Been 2 is de MARNET-zeerouter Nacala-zeeknoop 2148 → QQCT-kade, 12.499,7 km (geen gepubliceerde km ter vergelijking — het gepubliceerde 35–40 dagen-cijfer is geen afstand); QQCT-kade ligt 5,6 km van zeeknoop 5841 en snapt automatisch binnen de 25 km-grens, dus zonder aparte aanloop. Been 4 komt uit één wegscan (profiel `grafiet-balama-laixi-qingdao-nanshu`, extract `china`): 149,2 km getekende weggeometrie tegen 150 gepubliceerd (OSRM 149,6 km, geen onafhankelijke publicatie) = **−0,5%**, ruim binnen ±15%. Alle 4 markers liggen op ≤0,1 m van hun lijn.

**Toets-bevindingen (buiten de norm, niet dichtgetrokken):**
- **Naad been 3→4 = 5,59 km** — groter dan de norm van ≤5 km. Dit is géén procesfout maar de brief-eigen keuze om bij QQCT géén haven-aanloop te tekenen (§2/§7): het zeebeen eindigt op MARNET-zeeknoop 5841 (36,0313 / 120,2646), het wegbeen begint op de QQCT-kade zelf (36,0124 / 120,2070) — precies de 5,6 km die de brief al noemt. Anker ≠ routeerpunt; niet dichtgetrokken met verzonnen geometrie.
- **Anker-verbinding QQCT-kade → weg = 0,74 km** (`maak_stroombeen_weg.py`-uitvoer, "⚠️ > 0,5 km — bevinding"): de terminalwegen van QQCT zijn privé (brief §2/§7 voorzag dit al: "kade-stub < 1 km mogelijk, terminalwegen privé"). Weg → Laixi-fabriekspoort: 0,06 km, binnen de norm.
- **28 knikken ≥ 60° over de twee wegbenen** (`toets_knikken.py`), waarvan 3 "omkeringen" (≥150°) maar **0 terugloop** — de enige categorie die reparatie vraagt. De omkeringen zijn scherpe maar echte bochten (o.a. de afrit bij Laixi-west, 36,7634/120,3366) en OSM-spikes op kleine-klasse-eindwegen; geen sluipweg.
- `toets_rechte_benen.py --min-km 5`: geen enkel been van deze stroom komt in de verdachtenlijst (geen rechte lijn ≥5 km met omwegfactor ≈1,000).
- JSON-vormtoets: `versie` 2, `punt_formaat` `lonlat`, modaliteiten {truck, zee} (beide toegestaan), elk been ≥2 punten, bestand 104,0 KB (< 300 KB) — allemaal in orde.

**Gereedschapslessen:** geen nieuwe. Het patroon "MARNET-knoop ligt X km van de kade, geen aanloop, naad blijft staan" is al bekend van Beilun (koper-escondida-guixi) en wordt hier herbevestigd op een tweede stroom met een truck-aansluitend been i.p.v. spoor/leiding.
