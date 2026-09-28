# Routebrief (licht) · zeldzame aardmetalen — Longnan-ionenklei → Longnan-scheiding → JL MAG Ganzhou (China intern)

**stroom-id:** `ree-longnan-ganzhou` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** ionenklei-uitloogput bij Guanxi (关西镇), Longnan, per **truck** over de provinciale/county-weg
naar de scheidingsfabriek 赣州稀土（龙南）有色金属有限公司 in de Longnan-ontwikkelingszone, en vandaar per **truck**
over de Longnan–Ganzhou-corridor (G106/S32) naar de JL MAG Rare-Earth magneetfabriek in Ganzhou.
**Welke as van het verhaal:** de binnenlandse Zuid-Chinese ionenklei-as — mijnbouwquotum China Rare Earth Group
2024 (nationaal, alle ionklei-regio's incl. Longnan/Dingnan) 81.350 t REO [1]; JL MAG-magneetcapaciteit
38.000 t NdFeB/j (bedrijfsbreed: Ganzhou + Baotou + Ningbo) [11].

## 1 · Ketenkaart
```
Longnan-uitloogput (ionenklei, bij Guanxi 关西镇) `ree-longnan-uitloogput`
   ──(b1 truck · county-weg Guanxi → S225 → Longnan-ontwikkelingszone · ~20 km, aannemelijk: geen gepubliceerde km)──►
Longnan-scheidingsfabriek — 赣州稀土（龙南）有色金属有限公司 `ree-longnan-scheiding`
   ──(b2 truck · G106 / Longnan–Ganzhou-expressway (S32) via Xinfeng · ~130-160 km, aannemelijk: geen gepubliceerde km)──►
JL MAG Rare-Earth magneetfabriek, Ganzhou `ree-ganzhou-jlmag` (hergebruikt: `w-jlmag-ganzhou`, REE-sitelaag) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-longnan-uitloogput` → `ree-longnan-scheiding` | county-weg vanaf Guanxi (关西镇) naar provinciale weg S225, door Longnan-stad naar de ontwikkelingszone | hemelsbreed 15,5 km; aannemelijk ~20 km over de weg (aanname, geen bron) | maak_stroombeen_weg (extract `china`) | mogelijk kort stippel bij de put zelf (site ligt in bergterrein, laatste stuk mogelijk `track`) |
| b2 | C | truck | `ree-longnan-scheiding` → `ree-ganzhou-jlmag` | G106 / Longnan–Ganzhou-expressway (S32) via Xinfeng (信丰) | hemelsbreed 110,5 km; aannemelijk ~130-160 km over de weg (aanname, geen bron — ontwerp noemde 180-220 km ongebrond, zie §7) | maak_stroombeen_weg (extract `china`) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-longnan-uitloogput` | mijn / uitloogput (ionenklei) | grote kale, in contourlijnen getraceerde uitloogput-heuvel, ~2,3 km NO van Guanxi-stad (关西镇), Longnan | 24.8685, 114.9660 | [2][3][8] Zudong-REO-district (grootste regolith-hosted HREE-afzetting ter wereld, N24°45'–24°54' / E114°48'–115°00'); satelliet z17 | bron-gelegd (z17 gezien: uitgestrekte kale, roodbruine heuvel met karakteristieke horizontale terrasgroeven — het klassieke ionenklei-uitloogpatroon, aansluitend op een weg langs de rivier ten oosten van de put) |
| `ree-longnan-scheiding` | scheidingsfabriek | 赣州稀土（龙南）有色金属有限公司 (Ganzhou Rare Earth (Longnan) Non-ferrous Metals Co., Ltd.), Longnan-ontwikkelingszone | 24.84829, 114.81439 | [4][5][9] nationaal emissievergunningregister (permit.mee.gov.cn, decimaal én DMS 114°48'51.8"/24°50'53.8", exact overeenkomend); satelliet z16 | bron-gelegd (z16 gezien: fabriekscomplex met blauwe loodsdaken middenin een industrieterrein vol soortgelijke complexen, Longnan-ontwikkelingszone) |
| `ree-ganzhou-jlmag` | magneetfabriek | JL MAG Rare-Earth, Ganzhou (hergebruikt anker `w-jlmag-ganzhou`) | 25.8406, 114.8663 | [10][11] OSM-naam-tag 江西金力永磁科技股份有限公司; al satelliet-gelegd in de REE-sitelaag (z15: industrieel gebouwencomplex, Ganzhou-ontwikkelingszone) | bron-gelegd (hergebruikt, niet opnieuw gecheckt) |

## 4 · Via-punten (alleen waar een corridorkeuze bestaat)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Guanxi-stad (关西镇) | 24.8420, 114.9431 | doorgaande county-weg vanaf de put komt hier op de weg naar Longnan-stad; enige aannemelijke doorgaande richting |
| b2 | 1 | Xinfeng-stad (信丰) | 25.2784, 114.9721 | Longnan–Ganzhou-corridor (G106/S32) loopt via Xinfeng; pint de noordelijke route i.p.v. een westelijker alternatief via Quannan/Dayu |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Longnan-scheidingsfabriek | China Rare Earth Group (via Ganzhou Rare Earth Mining Co.) | ionenklei-uitloogconcentraat (carbonaat/oxalaat) → gescheiden RE-oxiden | 2.500 t REO/j (na technische renovatie), totaal actief vermogen 596 mln yuan (2023) | [4][5] |
| JL MAG Ganzhou | 江西金力永磁科技股份有限公司 | RE-oxide/legering → NdFeB-magneet-blanks | 38.000 t NdFeB/j (bedrijfsbreed: Ganzhou+Baotou+Ningbo, niet per vestiging uitgesplitst) | [11] |

## 6 · Stoppunt
De brief stopt bij de JL MAG-magneetfabriek in Ganzhou: dat is het in het ketenontwerp aangewezen eindpunt
(fase D vervalt — geen bron noemt een specifieke afnemersfabriek voor de magneet-blanks van déze vestiging;
JL MAG's eigen jaarverslag geeft alleen een bedrijfsbreed cijfer). Fase E is niet in één zin te onderbouwen en
vervalt.

## 7 · Open punten
- **Geen enkelvoudig startanker in absolute zin:** de gekozen put (24.8685, 114.9660) is één van >2.500 verspreide
  uitloogputten in het Zudong-district; gekozen als grootste/bekendste bevestigde locatie binnen het gedocumenteerde
  depositgebied (§3), niet omdat dit dé put is die naar de Longnan-scheiding rijdt — welk specifiek putcluster
  fysiek bij déze scheidingsfabriek levert is niet gepubliceerd.
- **Drie namen uit het ketenontwerp gedisambigueerd tot één:** de haalbaarheidstoets wees
  赣州稀土（龙南）有色金属有限公司 aan; "Longnan Heli" en "Dingnan Dahua" zijn niet teruggevonden als aparte,
  onafhankelijk gelegde entiteiten in het emissievergunningregister en worden losgelaten. Wél gevonden, mogelijk
  dezelfde rol maar NIET gebruikt als anker: **龙南龙钇重稀土科技股份有限公司** (稀土金属冶炼, "重点管理"),
  24.81884, 114.78459 (MEE-register) — eveneens een actieve REE-smelt-/scheidingsvergunning in Longnan, ~3 km
  ZW van het gekozen anker. Onzeker welke van de twee (of beide) daadwerkelijk aan JL MAG levert.
- **Km fase A en C zijn hemelsbreed-afgeleide aannames**, geen gepubliceerde routelengte gevonden voor beide
  benen; het ketenontwerp noemde voor b2 "180-220 km" zonder bron — de hemelsbreed-afstand (110,5 km) en de
  corridor via Xinfeng suggereren eerder ~130-160 km. Bakstap moet dit met een echte wegscan vaststellen.
- **Longnan/Dingnan-specifiek jaarvolume ontbreekt**: 81.350 t REO (2024) is het nationale ionklei-mijnbouwquotum
  van China Rare Earth Group voor àlle regio's (Guangdong/Guangxi/Fujian/Yunnan incl. Longnan/Dingnan); geen
  regionale uitsplitsing gevonden. JL MAG's 38 kt NdFeB/j is bedrijfsbreed, niet Ganzhou-specifiek.
- **Laatste stuk van b1** (put → doorgaande weg) kan buiten `tertiary`/`unclassified` vallen — bergterrein,
  mogelijk alleen `track` gekarteerd; bakstap toetst dit en stippelt zo nodig het laatste stukje.

## 8 · Bronnen
[1] Ontwerpnotitie/工信部联原〔2024〕156号 (via ketenontwerp) — nationaal ionklei-mijnbouwquotum China Rare Earth Group 2024, 81.350 t REO.
[2] Xu, C. et al., "The Genesis of Regolith-Hosted Heavy Rare Earth Element Deposits: Insights from the World-Class Zudong Deposit, Jiangxi" — Economic Geology 114(3), 2019. https://pubs.geoscienceworld.org/segweb/economicgeology/article-abstract/114/3/541/570391
[3] USGS MRDATA — "Longnan (Zudong?)" REE-depositrecord #323, Longnan Co., Ganzhou, Jiangxi. https://mrdata.usgs.gov/ree/show-ree.php?rec_id=323
[4] Nationaal emissievergunningregister (permit.mee.gov.cn/perxxgkinfo) — 赣州稀土（龙南）有色金属有限公司, longitude/latitude 114.81439/24.84829 (decimaal + DMS 114°48'51.8"/24°50'53.8", overeenstemmend), 行业类别 稀土金属冶炼. https://permit.mee.gov.cn/perxxgkinfo/syssb/xkgg/xkgg!licenseInformation.action
[5] 百度百科, 赣州稀土（龙南）有色金属有限公司 — opgericht 2013-02-25, dochter van China Rare Earth Group via Ganzhou Rare Earth Mining Co., 2.500 t/j scheidingscapaciteit na renovatie, geregistreerd in Longnan-ontwikkelingszone. https://baike.baidu.com/item/赣州稀土（龙南）有色金属有限公司/20964531
[6] Qixin.com (gehost MER-document) — 赣州稀土（龙南）有色金属有限公司 年产2500吨稀土氧化物冶炼分离技术改造项目 (eerdere, onvolledige coördinaat-vondst; nu vervangen door [4]). https://qxb-img-osscache.qixin.com/qianlima/赣州稀土(龙南)有色金属有限公司年产2500吨稀土氧化物冶炼分离技术改造项目环境影响报告书(公示稿)-附件_376334769_239567812.pdf
[7] Nationaal emissievergunningregister (permit.mee.gov.cn/perxxgkinfo) — 龙南龙钇重稀土科技股份有限公司, longitude/latitude 114.78459/24.81884 (decimaal + DMS overeenstemmend), 行业类别 稀土金属冶炼, 重点管理 (zie §7, niet als anker gebruikt).
[8] Mindat.org — Zudong Mine, Longnan REE deposits, Longnan Co., Ganzhou, Jiangxi (locatiebeschrijving, niet zelf gefetcht — 403; alleen als zoektreffer bevestigd). https://www.mindat.org/loc-225147.html
[9] OpenStreetMap (ODbL) via Overpass — plaatsknoop 关西镇 (Guanxi), 24.8420/114.9431; 信丰县 (Xinfeng), 25.2784/114.9721; grenspolygonen 龙南市 en 定南县. https://www.openstreetmap.org
[10] OpenStreetMap (ODbL) — naam-tag 江西金力永磁科技股份有限公司 (JL MAG Ganzhou), zoals gebruikt in `v2/design/ree-sitelaag.json` (anker `w-jlmag-ganzhou`).
[11] JL MAG 2024-jaarverslag (via SMM, zie `v2/design/ree-sitelaag.json` bron `w-jlmag-ganzhou`) — bedrijfsbrede NdFeB-blankcapaciteit 38.000 t/j eind 2024 (Ganzhou+Baotou+Ningbo).
[12] rare-earth-mining.com, "China Rare Earth Group" — achtergrond groepsstructuur, geen Longnan-faciliteitsdetails gevonden bij fetch. https://rare-earth-mining.com/china-rare-earth-group/

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom:** `ree-longnan-ganzhou` · **bestand:** `v2/data/stroomroute-ree-longnan-ganzhou.json` (43,2 KB) ·
**functie:** `bak_ree_longnan_ganzhou()` in `v2/tools/bak_stromen.sh` · **registerregel:** `{ sleutel: "ree-lg", bestand: "stroomroute-ree-longnan-ganzhou.json", grondstof: "ree", aan: true }`

| # | modaliteit | km | punten | naad met vorige been | stippel? |
|---|---|---|---|---|---|
| b1 | truck | 26,7 | 348 | — (1e been) | nee |
| b2 | truck | 145,8 | 1.679 | 0,00 km | nee |
| **totaal** | | **172,5** | **2.027** | | 3 markers |

Beide benen zijn `truck`-only, gebakken met `maak_stroombeen_weg.py --profiel <sleutel> --bron geofabrik` op de
`china`-extract (profielen `ree-longnan-ganzhou-uitloogput-scheiding` en `ree-longnan-ganzhou-scheiding-ganzhou`
in `v2/tools/maak_stroombeen_weg.py`), en als `--been-geojson` in `hecht_marnet.py route` opgenomen (geen
routering over de zee-/spoorgraaf — de geometrie komt letterlijk uit de gescande wegbestanden). Geen zeebenen,
dus geen haven-aanloop nodig; geen stippel-benen.

**Km-toets (§7-schattingen, aannemelijk-marge, referentie geen harde toets):**
- **b1** (uitloogput → scheidingsfabriek): gemeten **24,5 km** weggeometrie (26,7 km getekende lijn incl.
  anker-verbindingsstukjes) tegen de brief-verwachting "~20 km, ±15% = 17-23 km" — **licht buiten** die marge
  (+22,5% t.o.v. 20 km). Dit is een **bevinding, geen afgekeurde meting**: de brief zelf noemt de 20 km al als
  "aannemelijk, geen bron" (hemelsbreed 15,5 km), en de weg maakt bij Guanxi-stad een reële omweg (via de county-
  weg naar de S225) die de hemelsbreed-schatting niet ving.
- **b2** (scheidingsfabriek → Xinfeng → JL MAG Ganzhou): gemeten **145,7 km** weggeometrie (145,8 km getekende
  lijn) tegen "~130-160 km, aannemelijk" (het ketenontwerp noemde ongebrond 180-220 km, verworpen in de brief) —
  **binnen** de brede aannemelijke marge (110-190 km volgens de bak-aanwijzing van de brief), zoals bij
  `ree-kachin-ganzhou` §9 voor een vergelijkbaar ongebrond geval gedaan.

**Markers (3, alle ≤ 0,5 km van hun lijn — routeerpunt = anker):**
- `ree-longnan-uitloogput` (24,8685 / 114,9660) — kop van b1, snap 0,00 km (beginpunt).
- `ree-longnan-scheiding` (24,84829 / 114,81439) — staart van b1 = kop van b2, naad 0,00 km.
- `ree-ganzhou-jlmag` (25,8406 / 114,8663) — staart van b2 (hergebruikt anker `w-jlmag-ganzhou`, niet opnieuw
  satelliet-gelegd, conform de bak-aanwijzing).

**Toets (bakhandleiding-licht §5):** `toets_knikken.py` — 51 knikken ≥ 60° (allemaal OSM-spikes/krappe bochten op
een normale wegkartering), **0 omkeringen ≥ 150°**, **0 terugloop**. `toets_rechte_benen.py --min-km 5` — geen van
beide benen verschijnt in de lijst van verdachte rechte stukken (omwegfactor 1,000). `json.load` slaagt,
`versie` 2, `punt_formaat` `lonlat`, alle modaliteiten `truck` (bekende set), elk been ≥ 2 punten, bestandsgrootte
43,2 KB (ruim onder de ~300 KB-norm). Naad tussen b1 en b2: **0,00 km** (zelfde punt, geen overslag).

**Anker-verbindingsstukjes (buiten de lengtetoets, gerapporteerd door het weg-tool):**
- b1: put → dichtstbijzijnde wegvertex **2,02 km** — ⚠️ boven de gebruikelijke 0,5 km-norm. Bevinding, geen
  dichtgetrokken gat: de put ligt in het Zudong-uitloogdistrict op een heuvel met terrasgroeven, en de scan vond
  pas op 2,02 km een tertiary/unclassified-wegvertex. Geen `track`-segment gevonden dat de scanner niet doorkwam
  (anders dan verwacht in de bak-aanwijzing van de brief); het corridorvenster (30 km) en de verruimde eindklassen
  (incl. `track`) namen dit al mee, dus geen tweede poging of stippel nodig — het stuk staat gewoon getekend.
  b1 kop → weg 2,02 km · weg → kade 0,19 km [OK].
- b2: scheidingsfabriek → weg 0,19 km [OK] · weg → JL MAG-kade 0,01 km [OK].

**Gereedschapslessen:**
- Geen enkele van de twee benen leverde een "geen wegpad"-fout op (anders dan verwacht in de bak-aanwijzing voor
  b1); de verruimde `eindKlassen` (incl. `track`) en het ruime venster (30 resp. 50 km) vingen het bergterrein
  zonder tweede poging.
- b2 werd standaard gescand met `corridorKlassen: tertiary/unclassified` (niet eerst geprobeerd op
  trunk/primary/motorway zoals de bak-aanwijzing voorstelde) — de scan vond op de bredere klasse meteen een
  volledige verbinding via Xinfeng (145,7 km, binnen de aannemelijke marge), dus een aparte trunk/primary-poging
  was niet nodig.
- Beide profielen zijn `--been-geojson`-benen (vooraf gebakken lijn, niet geroutet over de MARNET/spoor/track-
  graaf in `hecht_marnet.py route`) — exact het patroon van de andere truck-only REE-benen in deze werkwijze.

**Open punten (ongewijzigd t.o.v. §7, bevestigd bij het bakken):** het putcluster-niveau bewijs, de twee actieve
Longnan-smeltvergunningen (slechts één als anker gebruikt), en fase D/E (vervallen, geen bron) blijven staan zoals
in §7 beschreven — de bakstap heeft geen van deze drie onzekerheden kunnen oplossen.
