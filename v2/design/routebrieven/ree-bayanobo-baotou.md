# Routebrief (licht) · zeldzame aardmetalen — Bayan Obo → Baotou (China)

**stroom-id:** `ree-bayanobo-baotou` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** ijzer-REE-erts van de Bayan Obo-mijn (白云鄂博矿, Binnen-Mongolië) gaat per **trein** over de
包白铁路 (159 km) naar de **veredelingsfabriek van Baogang** (包钢选矿厂) in Baotou, waar het REE-concentraat
(REO 50 %) als co-product van het ijzererts ontstaat; per **truck** door de stad naar de **scheidingsfabriek van
Northern Rare Earth** (北方稀土冶炼分公司, waarschijnlijk de Huamei-dochter in de稀土高新区) — daar stopt de
brief: geen bron noemt de levering aan een specifieke magneetfabriek.
**Welke as van het verhaal:** de Chinese binnenloop — de NdPr-massa van ~70 % van China's winning loopt via
precies deze twee overslagen. Nationale winningsquota 2024 (cumulatief, 2e batch): **270.000 t REO**-erts /
254.000 t scheiding, gedeeld door twee staatsbedrijven (Northern Rare Earth en China Rare Earth Group) [2].
Baogang's selectiecomplex verwerkt het erts tot **~300–450 kt REE-concentraat/jaar** (REO 50 %) [10][13],
verkocht aan Northern Rare Earth tegen een kwartaalprijs (Q1 2025: 18.618 CNY/t excl. belasting) [10]; Northern
verwerkt dat in de 冶炼分公司 tot gemengd carbonaat/chloride (prijs REO 50 %: 39.189 CNY/t, 2024) [4].

## 1 · Ketenkaart
```
Bayan Obo-laadstation `ree-bayanobo-laad` ──(b1 spoor · 包白铁路 · 159 km)──► Baogang-selectie `ree-baogang-selectie`
   (veredeling: ijzer-REE-erts → REE-concentraat REO 50 % + ijzerconcentraat — REE is hier co-product)
   ──(b2 truck · stedelijke wegen Kundulun → 稀土高新区 · ~15 km, aannemelijk)──► Northern RE-scheiding (Huamei)
   `ree-baotou-scheiding` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `ree-bayanobo-laad` → `ree-baogang-selectie` | 包白铁路 (Baotou–Bayan Obo-spoorlijn, 1958, 19 stations) | 159 [5] | `BAKE_SUFFIX=-raw toets_spoorroute` (1-op-1-net, extract `china`) | verwacht: korte emplacement-stippels aan beide uiteinden (mijnpunt buiten het net op ~1,3 km, Baogang op ~2,8 km — Chuqui-klasse) |
| b2 | C | truck (aannemelijk: Northern 冶炼分公司) | `ree-baogang-selectie` → `ree-baotou-scheiding` | stedelijke wegen Baotou: Kundulun (河西-industrie) → 稀土高新区 | geen publicatie; ~15 km hemelsbreed | `maak_stroombeen_weg` (profiel, extract `china`) | nee, tenzij de wegscan geen pad vindt |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-bayanobo-laad` | mijn / laadstation | Bayan Obo-spoorstation (白云鄂博站), kop van de 包白铁路 in de mijnstad | 41.7712, 109.9517 | [6][11] | bron-gelegd (z15 gezien: spoorstation en -knoop middenin de mijnstad, industriële bebouwing en stortterrein/windturbines noordwaarts richting de put) |
| `ree-baogang-selectie` | overslag / veredelingsfabriek (erts wisselt van grondstof) | Baogang-selectiecomplex, ingang 包白铁路 in de Baogang-industriezone (Kundulun) | 40.6790, 109.7550 | [9][11] | bron-gelegd (z14 gezien: spoorlijn komt uit de bergen het uitgestrekte Baogang-industriecomplex binnen, rangeerterrein met loodsen op het punt waar het net van de mijnlijn samenkomt met de fabriekssporen) |
| `ree-baotou-scheiding` | losplek / verwerkingsknoop | Northern Rare Earth 冶炼分公司 — dochter 包头华美稀土高科有限公司 (Huamei), 稀土高新区 | 40.5884, 109.8741 | [9][11] | bron-gelegd (z15 gezien: ommuurd industrieterrein met hallen en ronde tank-/bezinkstructuren aan de westzijde, tussen landbouwpercelen en de stadsrand van de hi-tech zone; OSM-landuse "包头华美稀土高科有限公司" op dezelfde plek) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Geen — b1 volgt één enkelvoudige spoorlijn zonder aftakkingskeuze; b2 is een stedelijke hop van ~15 km zonder
gedocumenteerde corridorsplitsing (de wegscan bepaalt de route).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Baogang-selectiecomplex | 包钢股份 (Baotou Steel) | ijzer-REE-erts (Bayan Obo, ~7,2 Mt/j ontwerpcapaciteit mijn) → REE-concentraat (REO 50 %) + ijzerconcentraat | REE-concentraat ~300 kt/j, oplopend naar ~450 kt/j (2026, +15,4 %) | [10][13] |
| Northern RE 冶炼分公司 (Huamei) | 北方稀土 (China Northern Rare Earth Group) | REE-concentraat (REO 50 %) → gemengd carbonaat/chloride-REE, dochters scheiden verder tot enkelvoudige zouten/oxiden/metalen | onderdeel van Northern's totale winning ≈ het grootste deel van de nationale 270.000 t-quota (twee staatsbedrijven; exacte bedrijfssplitsing niet apart bevestigd) | [2][7][3] |

## 6 · Stoppunt
De brief stopt bij de scheidingsfabriek (Northern RE 冶炼分公司/Huamei): geen bron noemt welke Northern-dochter
het concentraat als eerste ontvangt met een leveringsvolume, en geen bron documenteert de levering van
gescheiden oxide aan een specifieke magneetfabriek (北方稀土磁性材料) — fase D vervalt daarmee volgens de regel
dat een verwerkingsstap alleen getekend wordt als één bron de levering noemt, niet alleen het bestaan van de
ontvangende fabriek.

## 7 · Open punten
- Welke Northern-dochter (冶炼分公司 zelf, of Huamei, of een andere) het concentraat als eerste fysiek ontvangt
  is niet per rechtspersoon gedocumenteerd — Northern zegt alleen "koopt van 包钢股份, verwerkt in de
  冶炼分公司" [7]; het Huamei-anker is de beste OSM/satelliet-kandidaat in de 稀土高新区, niet bevestigd per naam.
- b1 draagt IJZERERTS met REE-inhoud, geen zuiver REE-erts; het REE-concentraat ontstaat pas in de
  veredelingsfabriek. Een deel van het erts komt bovendien uit een stockpile die bij de mijn zelf wordt verwerkt
  (白云博宇分公司, ~10 Mt erts/j volgens een oudere 2012-bron) — niet elk concentraat rijdt dus over dit spoorbeen.
- Emplacement-stippels bij beide spooruiteinden zijn een verwachting op basis van de netdichtheid rond Bayan Obo
  en Baotou, nog niet bevestigd door een bake.
- Nationale winningsquota splitst zich over twee staatsbedrijven (Northern Rare Earth + China Rare Earth Group);
  het exacte tonnage per bedrijf is deze sessie niet apart bevestigd — alleen het nationale totaal (270.000 t) [2].
- Fase D (scheiding → magneetfabriek) en fase E (magneet → eindproduct) zijn niet getekend: geen bron met
  leveringsvolume gevonden binnen het onderzoeksbudget van deze brief.
- Kleuralias: `ree` ontbreekt nog in `GRONDSTOF_KLEUR` (`v2/src/stroomstijl.js`) — centraal werk vóór het bakken,
  buiten de scope van deze brief.

## 8 · Bronnen
[1] NS Energy Business, Bayan Obo Rare Earth Mine — projectpagina, erts wordt ~150 km zuidelijker in Baotou verwerkt. https://www.nsenergybusiness.com/projects/bayan-obo-rare-earth-mine/
[2] MOFCOM (商务部), beleidsnotitie 2024 tweede batch winnings-/scheidingsquota zeldzame aardmetalen — nationaal cumulatief 270.000 t mijnbouw / 254.000 t scheiding, twee staatsbedrijven (incl. Northern Rare Earth). https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=100483
[3] Northern Rare Earth (reht.com), bedrijfsprofiel — groene smelterij fase 1 in bedrijf, grootste REE-grondstofbasis. https://www.reht.com/index/introduce.do?TYPE_CODE=020102&LB=1
[4] 财联社 (cls.cn), 2024 — transactieprijs precipitaat REO 50 %: 39.189 CNY/t. https://www.cls.cn/detail/1179174
[5] 维基百科, 包白铁路 — 全长约159公里, Baotou → Bayan Obo, 1958, 19 stations. https://zh.wikipedia.org/zh-cn/包白铁路
[6] 维基百科, 白云鄂博站 — coördinaten 41°46'16.35"N 109°57'5.97"E, gebouwd 1989, station op de 包白铁路. https://zh.wikipedia.org/zh-hans/白云鄂博站
[7] Shanghai Stock Exchange, mededeling 600111 (2023-03-15) — Northern koopt 稀土精矿 van 包钢股份, verwerkt in de 冶炼分公司 tot 混合碳酸稀土/混合氯化稀土, dochters scheiden verder. http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2023-03-15/600111_20230315_B3J5.pdf
[8] Global Energy Monitor (gem.wiki), Bayan Obo Main Mine — coördinaten 41.798138, 109.962814, operator Baiyun'ebo Iron Ore Mine of Baosteel. https://www.gem.wiki/Bayan_Obo_Main_Mine
[9] OpenStreetMap (ODbL) via Nominatim — landuse "包头钢铁(集团)有限责任公司" centroïde 40.6464/109.7501 (bbox 40.6150–40.6802/109.7096–109.7767); landuse "包头华美稀土高科有限公司" 40.5883/109.8741; suburb/weg "稀土路(街道)" ~40.63/109.86. https://www.openstreetmap.org
[10] 上海有色网 (SMM) — prijsformule Northern/Baogang voor REE-concentraat, Q1 2025 18.618 CNY/t (REO 50 %, excl. belasting), +4,7 % t.o.v. Q4 2024. https://news.smm.cn/news/103207392
[11] Esri World Imagery via `v2/tools/sat_check.py` (z13–z15, live) — `v2/build-cache/satcheck/sat-ree-bayanobo-baotou-mijn.png`, `sat-ree-bayanobo-baotou-baogang-noord.png`, `sat-ree-bayanobo-baotou-huamei.png`.
[12] 维基百科, 白云鄂博铁矿 — mijn 149 km zuiden van Baotou, opgericht 1957, jaarproductie 11 Mt erts. https://zh.wikipedia.org/zh-hans/白云鄂博铁矿
[13] 东方财富/caifuhao, 2025-10-16 — 包钢股份 稀土精矿-productiecapaciteit ~30万吨/j, oplopend naar 45万吨/j (2026, +15,4 %). https://caifuhao.eastmoney.com/news/20251016195049800755110

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `ree-bayanobo-baotou`** → `v2/data/stroomroute-ree-bayanobo-baotou.json` — 2 benen, 170,9 km,
3 markers: spoor 151,6 km (Bayan Obo-laadstation → Baogang-selectiecomplex, 包白铁路) · truck 19,3 km
(Baogang-selectiecomplex → Northern Rare Earth-scheiding Huamei, stedelijke wegen Baotou).
Recept: `bak_stromen.sh` (functie `bak_ree_bayanobo_baotou`).

**b1 (spoor):** `BAKE_SUFFIX=-raw toets_spoorroute.mjs` op het 1-op-1-net (3.260.717 spoor-edges,
console bevestigde de juiste laag). Snap kop 0,22 km / snap staart 0,25 km — beide ruim binnen de
markernorm (≤0,5 km). 151,6 km (gebakken, `hecht_marnet.py`) tegen 159 km gepubliceerd (包白铁路,
zh.wikipedia [5]) = **−4,7%**, binnen ±15%.
**b2 (truck):** nieuw profiel `ree-bayanobo-baotou-baogang-scheiding` (extract `china`, geen refs,
vensterKm 25). 19,3 km tegen de brief's eigen ~15 km hemelsbreed-schatting (geen operator-bron) =
**+28,3%** — buiten ±15%, maar de toets is hier indicatief (§2/§7 van de brief noemt al "geen
publicatie"), dus bevinding, niet dichtgetrokken. Snap anker-tot-weg 0,07 km (Baogang) / 0,02 km
(Huamei).
Naad tussen b1 en b2: 0,25 km (< 5 km-norm).

**Toelichting stippels:** geen. Er zijn GEEN gestippelde beentjes getekend — noch voor het spoor,
noch voor de truckroute. Dit wijkt af van de verwachting in de brief/bak-aanwijzingen ("verwacht:
korte emplacement-stippels aan beide spooruiteinden, resp. ~1,3 en ~2,8 km volgens de
netdichtheids-toets"): de daadwerkelijk gebakken snap is met 0,22/0,25 km veel kleiner dan die
verwachting — de emplacement-stippel-hypothese uit de brief is hiermee **niet bevestigd**; het
1-op-1-net reikt in de praktijk tot vlak bij beide ankers.

**Toets-bevindingen (buiten de norm, niet dichtgetrokken):**
- **Drie TERUGLOOP-omkeringen op het spoorbeen** (`toets_knikken.py`): 180,0° bij 40,63650/109,72840
  (v-ratio ≈39,7) · 180,0° bij 40,66130/109,75200 (v-ratio ≈99,0) · 176,6° bij 41,77500/109,95380
  (v-ratio ≈2,4, vlak bij het Bayan Obo-anker). Alle drie waren al zichtbaar in de eerste
  `toets_spoorroute.mjs`-run ("OMKERING — alleen echt als hier kopgemaakt wordt") en zijn dus een
  eigenschap van het gemeten spoornet, geen routerkeuze van deze bake. Zelfde klasse als
  Jinzhou-Baotou (2026-09-26): mogelijk topologisch afgedwongen door doodlopende sporen/wissels bij
  de mijn en het selectiecomplex — niet nader onderzocht binnen de scope van deze lichte bake.
- **15 spikes op het truckbeen** (60-136°, straal 5-75 m) — stedelijke kruispunten in Baotou, geen
  enkele ≥150° (dus geen omkering/terugloop). Verwacht bij een korte stedelijke hop met veel
  kruisingen; niet gerepareerd.
- `toets_rechte_benen.py --min-km 5`: geen enkel been van deze stroom in de verdachtenlijst.
- Markers: Bayan Obo-laadstation 221,5 m van de lijn (kop-snap 0,22 km, verwacht) · Baogang-selectie
  0,1 m · Northern-scheiding Huamei 0,0 m (beide truckbeen-ankers vallen exact op de routeerlijn).
- JSON-vormtoets: `versie` 2, `punt_formaat` `lonlat`, modaliteit {spoor, truck} (toegestaan), elk
  been ≥2 punten, bestand 14,2 KB (< 300 KB) — allemaal in orde.

**Gereedschapslessen:** de brief-schrijver schatte de emplacement-gaten aan beide spooruiteinden op
basis van een netdichtheids-toets (~1,3/2,8 km); de daadwerkelijke bake (1-op-1-net, `BAKE_SUFFIX=-raw`)
gaf een veel kleinere snap (0,22/0,25 km) — een netdichtheids-schatting vooraf is dus geen vervanging
voor de gemeten snap-afstand ná het bakken, en het is beter geen stippel te tekenen op basis van een
verwachting die de bake zelf tegenspreekt. Verder: de drie terugloop-omkeringen op het spoorbeen waren
al zichtbaar in de allereerste routerconsole (vóór `hecht_marnet`) — die vroege waarschuwing bleek een
betrouwbare voorspeller van wat `toets_knikken.py` ná de bake zou vinden.
