# Routebrief (licht) · zeldzame aardmetalen — Kachin-ionklei → Pangwa-grens → Tengchong-douane (Myanmar–China)

**stroom-id:** `ree-kachin-ganzhou` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** zware-REE-ionklei (Dy/Tb, als RE-carbonaat/oxalaat in zakken) uit de uitloogputten rond Pangwa (Kachin Special Region 1, Chipwi Township, Myanmar — KIA-gebied sinds okt. 2024) gaat per **truck** over de bergweg naar de grensdoorlaat Pangwa (26.0153, 98.6080) en vandaar door naar de douane/overslagloodsen van Diantan (滇滩镇), Tengchong, Yunnan — **keten korter dan het ontwerp**: de ~2.300 km naar de Ganzhou/Longnan-scheiding is *niet* getekend (zie §6).
**Welke as van het verhaal:** de zware-REE-landstroom over de Myanmar–China-grens — China haalde jan–sep 2025 >28.000 t REO / USD 624 mln uit Myanmar, 74,9 % van zijn REO-import (Eastmoney/中国稀土, okt. 2024) [1][5]; wereldwijd woog Myanmar 22.000–27.000 t REO in 2024/2025 tegen wereld ~390.000 t (USGS MCS 2026) [4].

## 1 · Ketenkaart
```
Pangwa-mijngebied (uitloogputten) ──(b1 truck · Kachin-bergweg → Chinese S-weg · ~57 km hemelsbreed, ~60–110 km over de weg)──►
Diantan-douane (滇滩镇, Tengchong) ⏹ stoppunt — Ganzhou/Longnan-scheiding (~2.300 km verder) niet getekend, zie §6
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-pangwa-mijn` → `ree-diantan-douane` | Kachin-bergweg Pangwa-dal (KIA-gebied) → Chinese zijde S-weg naar Diantan-stad | geen publicatie; hemelsbreed 57,5 km, gepubliceerd traject "~60–110 km" (aanname in het ontwerp, geen bron) [toets] | maak_stroombeen_weg (myanmar + china-extract, corridorKlassen tertiary/unclassified) | ja, gedeeltelijk — OSM-dekking Kachin hangt grotendeels aan `track` (komt de scanner niet door); stippel tussen putten en de doorgaande weg waar geen tertiary/unclassified ligt |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-pangwa-mijn` | mijngebied / verzamelpunt + grensovergang (gecombineerd — mijnen liggen tegen het dorp/de doorlaat aan) | Pangwa (板瓦), uitloogputtengebied + grensdoorlaat naar Diantan | 26.0153, 98.6080 | [8][9] OSM `barrier=border_control` nodes 2540280367/2540280372 (98.6080/98.6076, ~40 m uit elkaar) | bron-gelegd (z14/z15 gezien: dorp met wegen op een rivierterras, aan weerszijden en verderop stroomopwaarts uitgestrekte lichtbruine, kale terreinvlakken langs de rivier — kenmerkend voor uitloogputten/wasplaatsen; nóg twee vergelijkbare nederzettingen met dezelfde kale vlakken liggen 1–4 km oostelijker in dezelfde vallei) |
| `ree-diantan-douane` | douane / overslag land→land (handover aan Chinese kopers) | Diantan (滇滩镇), Tengchong, Yunnan | 25.5292, 98.4097 | [10][11] OSM-plaatsknoop 滇滩镇 (Nominatim/ODbL); [12] gemeentelijke coördinaat-tool 25,594/98,380 voor het naburige "Pang War"/滇滩口岸-punt (7–8 km ervandaan — zelfde stad, ander deel van de vallei, niet gebruikt als anker) | bron-gelegd (z14 gezien: langgerekt stadje in een rivierdal met stuwmeer/reservoir; kale, terrasvormige ontginningsvlakken (mijnbouw/steengroeve) 2–3 km ZO van het centrum — geen aparte douanepoort te onderscheiden op dit zoomniveau, vandaar stadscentrum als anker) |

## 4 · Via-punten
Geen — voor b1 bestaat geen gedocumenteerde corridorkeuze (het Kachin-wegennet is nauwelijks gekarteerd); de bak-agent laat de weg-scan (corridorKlassen tertiary/unclassified, vensterKm ruim) het tracé binnen de vallei kiezen en stippelt waar alleen `track` ligt.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Diantan-douane | Chinese douane/kopers | RE-carbonaat/oxalaat (zakken) → handover aan Chinese opkopers, vervolgvervoer richting binnenland | — (geen volumecijfer per doorlaat; China-breed 74,9 % van de REO-import uit Myanmar, jan–sep 2024) | [5] |
| (niet getekend) China Southern Rare Earth Group, scheiding Ganzhou-regio | China Southern Rare Earth Group (24 dochters, o.a. 赣州稀土（龙南）有色金属 in Longnan) | concentraat/oxide (~70 % groepsbreed uit Myanmar) → gescheiden REO/NdPr/Dy-Tb-oxide | scheidingscapaciteit groep ~8万 t/j (80 kt/j) | [7][13] |

## 6 · Stoppunt
De brief stopt bij de Diantan-douane. De regel "de lijn eindigt waar het bewijs eindigt" verbiedt het doortekenen naar Ganzhou: de afnemer is alleen op **groepsniveau** gedocumenteerd (China Southern Rare Earth Group, 70 % van zijn grondstof uit Myanmar volgens Global Witness [2][13]) en zelfs de best gevonden kandidaat-vestiging — 赣州稀土（龙南）有色金属有限公司 in de Longnan-economiezone — heeft in de gevonden milieueffectrapportage alleen een **halve coördinaat** (lengtegraad 114°48′O, geen breedtegraad) [14]; dat is geen "rechtspersoon met coördinaat" in de zin van de toets. Een tweede, onafhankelijke Global Witness-vondst wijst bovendien op groepsvestigingen in **Longling en Jianghua**, niet expliciet Ganzhou/Longnan, voor de Myanmar-stroom specifiek [15] — een extra reden om niet te kiezen. **Conclusie: b2 wordt niet gebakken; de Ganzhou-scheiding gaat naar de sitelaag als gloednode (rol scheidingsfabriek), niet als lijn.**

## 7 · Open punten
- **Exacte grensdoorlaat-precisie:** de gebruikte coördinaat (26.0153, 98.6080) komt uit twee dicht bijeenliggende OSM `barrier=border_control`-nodes in de Myanmar-extract; aan de Chinese kant is in de scan géén vergelijkbare node gevonden — het Chinese poortpunt zelf (douanegebouw) is niet apart gelegd, alleen de stad Diantan.
- **Naamverwarring "Pangwa":** Wikipedia's "Pang War" geeft 25.594, 98.379 voor een gelijknamige plaats — dat is 7–8 km van Diantan-stad, dus vrijwel zeker een ánder, zuidelijker punt dan de hier gebruikte mijn-/grensnederzetting op 26.0153, 98.6080 (die wél in de Chipwi/Pangwa-mijnbouwbbox 25,75–26,25 N / 98,30–98,75 O valt die uit de eigen OSM-scan kwam). Niet opgelost; beide bestaan mogelijk naast elkaar in Kachin.
- **Ganzhou/Longnan-coördinaat:** alleen lengtegraad gevonden (114°48′O) in een MER-document [14]; breedtegraad niet. Een volledige MEE-registervondst (zoals bij de Feishang-koperbrief) zou b2 alsnog bakbaar maken.
- **Volumeverdeling per doorlaat:** China-brede importcijfers (74,9 % uit Myanmar) zijn niet uit te splitsen naar Pangwa vs. Kan Paik Ti vs. andere poorten.
- **Statusnuance conflict:** poorten dicht okt. 2024 → handel hervat dec. 2024 (KIA-heffing 35.000 CNY/t) → Beijing heropende vier KIA-poorten eind okt. 2025 [3][6]; de stroom valt periodiek stil, dat hoort bij deze kaart, niet bij een storing.
- **v1-correctie (niet in deze opdracht, wel hier genoteerd):** v1's `grens-ruili` (24.02, 97.85) is de Muse–Ruili-poort van de tinstroom (Shan), niet deze REE-poort — `data/rare-earths.js`/`_chokepoints.js` corrigeren is een aparte taak.

## 8 · Bronnen
[1] ISP-Myanmar, *Rare Earth Mining in Myanmar's War-Torn Regions* (juni 2025) — mijnbouw, poorten Pangwa/Phimaw/Kangfang/Kan Paik Ti, volumes. https://ispmyanmar.com/wp-content/uploads/2025/06/Rare-Earth-Mining-in-Myanmars-War-Torn-Regions.pdf
[2] Global Witness, *Myanmar's poisoned mountains* (2022) — 70 % van de grondstof van China Southern Rare Earth (destijds REGCC) komt uit Myanmar. https://globalwitness.org/en/campaigns/transition-minerals/myanmars-poisoned-mountains/
[3] Stimson Center, *Rare Earths and Realpolitik: The Future of Mediation in Myanmar* (2025) — KIA neemt Chipwi/Pangwa okt. 2024, poortsluiting, heropening eind okt. 2025, KIA-heffing. https://www.stimson.org/2025/rare-earths-and-realpolitik-future-of-mediation-myanmar/
[4] USGS, *Mineral Commodity Summaries 2026 — Rare Earths* — Myanmar 27.000 t REO (2024) / 22.000 t (2025); wereld ~390.000 t. https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-rare-earths.pdf
[5] Eastmoney/中国稀土 (okt. 2024, via ISP-Myanmar/persberichten) — China importeerde jan–sep 2024 31.000 t REO uit Myanmar = 74,9 % van de oxide-import. https://ispmyanmar.com/pet-03/
[6] Kachin News Group, *Rare earth export permission granted, say sources close to industry* (2025-04-02). https://kachinnews.com/2025/04/02/rare-earth-export-permission-granted-say-sources-close-to-industry/
[7] 百度百科, *中国南方稀土集团有限公司* — 24 dochterondernemingen, scheidingscapaciteit ~8万 t/j (80 kt/j), geen fabrieksadres. https://baike.baidu.com/item/中国南方稀土集团/19222477
[8] OpenStreetMap (ODbL), Myanmar-extract — `barrier=border_control` nodes 2540280367 / 2540280372, 26.0153/98.6080 en 26.0156/98.6076 (Pangwa–Diantan-doorlaat). https://www.openstreetmap.org
[9] Global Witness, *Myanmar's rare earth boom* (vervolgonderzoek) — meer dan 300 mijnsites rond Pangwa in 2023, saturatie van het landschap rond de grensstad. https://www.globalwitness.org/en/campaigns/natural-resource-governance/fuelling-the-future-poisoning-the-present-myanmars-rare-earth-boom/
[10] OpenStreetMap (ODbL) via Nominatim — plaatsknoop 滇滩镇 (Diantan), 25.5292/98.4097. https://www.openstreetmap.org
[11] Tengchong gemeente, *滇滩镇情简介* — 滇滩镇 grenst 24,7 km aan Kachin, drie uitgangskanalen (火炭洞·板瓦·姊妹山), 板瓦 = Pangwa. https://www.tengchong.gov.cn/info/1731/36596.htm
[12] 经纬度查询-tool (122cha.com), *云南_保山_腾冲经纬度查询* — coördinaat 滇滩口岸/"Pang War" 25,594/98,380 (niet als anker gebruikt, zie §7). https://jingweidu.122cha.com/630093.html
[13] Global Witness, *Myanmar's rare earth boom* — China Southern Rare Earth Group-dochters (REGCC) in Longling en Jianghua gekoppeld aan Myanmar-import; magneetmakers JL Mag en Yantai Zhenghai als afnemers verderop in de keten. https://www.globalwitness.org/en/campaigns/natural-resource-governance/fuelling-the-future-poisoning-the-present-myanmars-rare-earth-boom/
[14] Qixin.com (gehost MER-document), *赣州稀土（龙南）有色金属有限公司 年产2500吨稀土氧化物冶炼分离技术改造项目 环境影响报告书* — locatie Longnan经开区东江新圳工业区, lengtegraad 114°48′O (breedtegraad niet vermeld). https://qxb-img-osscache.qixin.com/qianlima/赣州稀土(龙南)有色金属有限公司年产2500吨稀土氧化物冶炼分离技术改造项目环境影响报告书(公示稿)-附件_376334769_239567812.pdf
[15] Global Witness, zie [13] — zelfde bron, tweede citaat (Longling/Jianghua-vestigingen i.p.v. Ganzhou/Longnan).

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `ree-kachin-ganzhou`** → `v2/data/stroomroute-ree-kachin-ganzhou.json` — 1 been, 118,8 km, 2 markers: truck 118,8 km.
Recept: `bak_stromen.sh` (functie `bak_ree_kachin_ganzhou`). Profiel `ree-kachin-ganzhou-pangwa-diantan` in
`maak_stroombeen_weg.py` (extracts `myanmar` + `china`), geen via-punten (geen gedocumenteerde corridorkeuze,
brief §4) — `corridorKlassen: [tertiary, unclassified]` en `vensterKm: 60` lieten de scan het tracé zelf kiezen.
Lengtetoets: 118,7 km weggeometrie (118,8 km getekend incl. anker-verbindingen ≤ 0,04 km) tegen "geen
publicatie; hemelsbreed 57,5 km, ontwerpaanname ~60–110 km zonder bron" (`gepubliceerdKm: None`, brief §2/§7)
= **geen ±15%-toets mogelijk, alleen referentie**. De uitkomst ligt boven de ongebronde ontwerpschatting, wat
bij bergterrein met veel haarspeldbochten (243 keerlussen gesnoeid, lengte 119,5 → 118,7 km) niet
onaannemelijk is, maar zonder derde bron blijft dit een bevinding en geen afgekeurde meting. Naad: n.v.t.
(één been). Markers op 0,00 km van de lijn (beide ankers zijn het begin-/eindpunt van het been zelf).
`toets_knikken.py`: 95 knikken ≥ 60°, waarvan 1 omkering ≥ 150° en **0 terugloop** (alle 95 zijn spikes op
zeer korte boogstralen, 5–41 m — kopmaak-wisselpunten op smalle bergwegen, geen routerartefact). `toets_rechte_benen.py
--min-km 5`: geen melding (5.076 punten, geen ongestippelde rechte lijn). Contract: versie 2, `punt_formaat
lonlat`, modaliteit `truck`, bestand 98,8 KB.
Geen stippel: modaliteit truck, doorgetrokken over de hele lengte. "Geen gepubliceerde km" en "hemelsbreed
57,5 km" staan in de bronnoot van het profiel, niet in de lijnstijl (brief §2/§7).
Gereedschapslessen: de brief-verwachte OSM-dekkingssplitsing (Kachin-kant grotendeels `track`, Chinese kant
tertiary/unclassified) bleek in de praktijk geen probleem op te leveren — met `corridorKlassen:
[tertiary, unclassified]` en een ruim venster (60 km) vond de scan een doorlopende tertiary/unclassified-route
over de hele 118,7 km, zonder stippelsegment; de brief-aanwijzing "verwacht minstens één stippelsegment" komt
dus niet uit, wat zelf een bevinding is (de Kachin-bergweg is beter gekarteerd dan het ontwerp aannam, of de
scan heeft een alternatieve route gevonden die niet over `track` loopt). Eén tijdelijke draaifout tijdens de
eerste scanpoging (`TypeError` bij het schrijven van het rapport voor een been zonder `gepubliceerdKm`) bleek
niet reproduceerbaar bij een schone herhaling (parallelle wegscans van andere agenten op hetzelfde moment als
waarschijnlijke oorzaak, niet de code zelf) — tweede poging met dezelfde cache leverde een schone run.
Extracts `myanmar` (dun gekarteerd, veel `track`) + `china` (dicht gekarteerd), geen Overpass-terugval nodig.
Niet getekend (bewust, zie §6): de ~2.300 km naar de Ganzhou/Longnan-scheiding — alleen groepsniveau
gedocumenteerd (China Southern Rare Earth Group), geen volledige coördinaat voor de kandidaat-vestiging
(赣州稀土（龙南）有色金属, alleen lengtegraad gevonden). Die scheidingsfabriek hoort later als gloednode (rol
scheidingsfabriek) in de sitelaag, niet als lijn — nog niet uitgevoerd (centraal werk, `voeg_sites_toe.py`-
patroon, wacht op een REE-sitelaag die nog niet bestaat).
