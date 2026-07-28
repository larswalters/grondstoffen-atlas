# Routebrief · koper (concentraat) — Escondida → Guixi (China)

*Derde routebrief volgens `../routebrief-werkwijze.md`, en de eerste volgens het
**aangescherpte** formaat (2026-07-28): kop en staart zijn satelliet-gelegd op z16/z17
vóórdat ze anker werden, de last mile staat als eigen been, en waar het net niet reikt
staat een stippellijn mét reden. Keten: **slurryleiding** (Escondida-concentrator →
Puerto Coloso, ~170 km, eigen verbinding) → **zee** (Coloso → Ningbo-Zhoushan/Beilun,
router) → **spoor** (Beilun-ertsterminal → Guixi, ~550–630 km) → **last mile**
(贵溪站-专uslijn → de ertslosbundel op het smelterterrein).*

*Toets-doel: dit is de stroom die LAR-527 "de zware" noemt — het China-spoorbeen heeft
het grootste risico op een verkeerde corridor. Deze brief levert dat risico ook meteen op:
de atlas mat het spoorbeen in de heal-ronde op **883 km**, terwijl de brief-corridor op
**~628 km** (klassiek) of **~556 km** (sinds 2024) uitkomt. Dat is 41–59% te veel — de
getekende lijn ligt vrijwel zeker op een andere corridor.*

---

## Kernfeiten die de vorm van de keten bepalen

1. **Het concentraat verlaat de mijn als slurry, niet als vrachtwagenlading.** Escondida
   pompt concentraat als pulp met ~65% vaste stof door een **170 km** lange leiding
   (9 inch) naar Puerto Coloso; dáár wordt het gefilterd, opgeslagen en op bulkcarriers
   geladen [E1][E2]. De laadplek is dus de **concentrator met zijn indikkers**, niet de
   put en niet het mijnkantoor.
2. **Coloso is Escondida's eigen terminal**, ~12 km ten zuiden van de haven Antofagasta
   waar `data/copper.js` de stroom heen stuurt. De terminal heeft een eigen laadsteiger
   in zee; er komt geen vrachtwagen of trein aan te pas [E3].
3. **De leiding is een eigen verbinding, geen net.** Er is geen `substance=slurry`-
   kartering richting Coloso (gemeten: geen van de 76 OSM-pijpleidingen komt dichter dan
   16,5 km bij Coloso) — anders dan bij Collahuasi, waar het tracé wél ligt. → **stippel
   mét reden**, conform werkwijze §7. Dit been wordt niet "opgelost", het ís zo.
4. **De aankomstkant is de scherpste onzekerheid.** Guixi ligt ~550–630 km landinwaarts;
   het is de grootste kopersmelter ter wereld en draait grotendeels op **ingevoerd**
   concentraat (Peru, Chili, Afrika) [J1]. Welke van de twee spoorcorridors dat
   concentraat rijdt is met open bronnen niet hard te maken — beide staan hieronder, mét
   hun kilometrering, zodat de getekende lijn tegen allebei te toetsen is.

## Been 1 · slurryleiding — Escondida-concentrator → Puerto Coloso (~170 km, stippel)

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **Escondida-concentrator + indikkerpark** — kop van de slurryleiding | laadplek | -24.2620, -69.0600 | [E3] + satelliet z16 | **satelliet-gelegd** |
| 2 | — | **Rajo Escondida** (de put zelf) ligt ~1,5 km ZW; erts gaat per truck/band naar de molen, niet de leiding in | referentie (niet aan lijn) | -24.2700, -69.0717 | [E3] | bevestigd |
| 3 | — | Laguna Seca-concentrator (tweede molen op het complex) | referentie (niet aan lijn) | — | [E2] | aannemelijk |
| 4 | ~170 | **Coloso filterfabriek + stockpile** — slurry wordt hier ontwaterd | overslag | -23.7590, -70.4670 | [E3] + satelliet z17 | **satelliet-gelegd** |
| 5 | ~170 | Wal-einde van de laadsteiger (begin van de trestle naar zee) | overslag | -23.7579, -70.4659 | satelliet z17 | **satelliet-gelegd** |
| 6 | ~171 | **Kop van de laadsteiger / scheepslader** — hier ligt de bulkcarrier | laadplek zee | -23.7569, -70.4652 | satelliet z17 | **satelliet-gelegd** |

**Opmerkingen been 1.** ⚠️ **Twee correcties op de projectdata, allebei door de
satellietregel gevonden.** (a) `cu-escondida-laad` stond op **-24.27004 / -69.07169** —
dat ligt op een berm midden **ín de open put**, ~1,5 km van de molen. Een leiding begint
niet in een put. (b) `cu-coloso-kade` stond op **-23.76015 / -70.46332**; op de tegels is
dat de **kustweg bij het dorp Coloso**, ~400 m oostelijk van de terminal — de steiger ligt
noordwestelijker en steekt de zee in. Zelfde klasse als de New Orleans-centroïde en het
Nacala-west-jetty-punt: een OSM-treffer is een kandidaat, geen anker.
Lengte-toets: de brief-leiding meet ~170 km [E1]; dat is de enige controle die dit been
heeft, want er is geen tracé-geometrie.

## Been 2 · zee — Puerto Coloso → Ningbo-Zhoushan (Beilun-ertsterminal)

Conform werkwijze §6: kade→kade, de zeerouter doet de rest; alleen sanity-ankers.

| # | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|
| 1 | **Coloso — kop laadsteiger** (vertrek) | laadplek | -23.7569, -70.4652 | satelliet z17 | **satelliet-gelegd** |
| 2 | Open Stille Oceaan, noordelijke grootcirkel-lane richting Oost-Azië | passage | — | [Z1] | aannemelijk |
| 3 | **Beilun-ertsterminal — losberth met ertslossers** (aankomst) | losplek | 29.9364, 121.8830 | [E3] + satelliet z16 | **satelliet-gelegd** |

**Negatieve ankers been 2.** **Géén Panamakanaal** (verkeerd halfrond voor deze reis) ·
**géén Straat Magellaan / Kaap Hoorn** · en — belangrijk voor de kaart — **niet via de
haven Antofagasta**: `data/copper.js` stuurt deze stroom via `cu-port-antofagasta`, maar
Escondida's concentraat gaat via de **eigen** terminal Coloso, 12 km zuidelijker. De
atlas-invariant voor deze oversteek is de gemeten Antofagasta→Shanghai-lane van
**18.915 km** (searoute 18.880) — Coloso→Beilun hoort in dezelfde orde te liggen [Z1].

## Been 3 · spoor — Beilun-ertsterminal → Guixi

Dit been is **brief-gestuurd** (werkwijze §6). Er zijn **twee** reële corridors, en welke
er gereden wordt is met open bronnen niet te beslissen. Beide staan hier met hun
officiële kilometrering, zodat de getekende lijn eenduidig te toetsen is.

### Corridor A — klassiek, via Hangzhou (~628 km)

北仑支线 (35,4 km) → 萧甬铁路 (146,4 km) → 沪昆铁路, voorheen 浙赣铁路 (~446 km).

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **北仑港站** — eindstation van de Beilun-tak, het havenstation zelf | laadplek | — | [C1] | bevestigd |
| 2 | ~8 | 北仑站 (rangeer-/overslagstation voor het havengebied, 1986) | station | — | [C1] | bevestigd |
| 3 | ~18 | 大碶站 | station | — | [C1] | bevestigd |
| 4 | ~27 | 宝幢站 | station | — | [C1] | bevestigd |
| 5 | ~32 | 宁波东站 | station | — | [C1] | bevestigd |
| 6 | 35,4 | **宁波站** — aansluiting Beilun-tak op de 萧甬铁路 | kruising | — | [C1] | bevestigd |
| 7 | 43 | 庄桥 (Xiao-Yong km 139, gerekend vanaf Hangzhou) | station | — | [C2] | bevestigd |
| 8 | 49 | 宁波北 (km 133) | station | — | [C2] | bevestigd |
| 9 | 55 | 慈城 (km 127) | station | — | [C2] | bevestigd |
| 10 | 71 | 丈亭 (km 111) | station | — | [C2] | bevestigd |
| 11 | 83 | **余姚** (km 99) | station | — | [C2] | bevestigd |
| 12 | 115 | **上虞** (km 67) | station | — | [C2] | bevestigd |
| 13 | 144 | **绍兴** (km 38) | station | — | [C2] | bevestigd |
| 14 | 153 | 柯桥 (km 29) | station | — | [C2] | bevestigd |
| 15 | 182 | **杭州南 / Hangzhou** (km 0 van de Xiao-Yong) — draaipunt naar het westen | kruising | — | [C2] | bevestigd |
| 16 | 253 | **诸暨** (Zhe-Gan km 76,2) | station | — | [C3] | bevestigd |
| 17 | 295 | **义乌** (km 118,3) — hier komt corridor B binnen | kruising | — | [C3][C4] | bevestigd |
| 18 | 348 | **金华** (km 171,3) | station | — | [C3] | bevestigd |
| 19 | 400 | 龙游 (km 223,1) | station | — | [C3] | bevestigd |
| 20 | 430 | **衢州** (km 253) | station | — | [C3] | bevestigd |
| 21 | 460 | 江山 (km 282,8) — provinciegrens Zhejiang/Jiangxi even verderop | station | — | [C3] | bevestigd |
| 22 | 508 | 玉山 (km 331,3) | station | — | [C3] | bevestigd |
| 23 | 540 | **上饶** (km 362,8) | station | — | [C3] | bevestigd |
| 24 | 582 | 横峰 (km 404,8) | station | — | [C3] | bevestigd |
| 25 | 598 | 弋阳 (km 421,2) | station | — | [C3] | bevestigd |
| 26 | **628** | **贵溪站** (km 451,2) — losstation voor de smelter | losplek / eind spoorbeen | — | [C3][C6] | bevestigd |

### Corridor B — sinds 2024, via de Yong-Jin-vrachtlijn (~556 km)

**甬金铁路** (Ningbo–Jinhua/Yiwu) is op **31 december 2023** geopend en rijdt sinds
**10 januari 2024** vracht: 188,3 km van **云龙站** (Yinzhou, Ningbo) via Fenghua,
Shengzhou, Xinchang en Dongyang naar **义乌站**, gebouwd als vrachtlijn voor de
"义甬舟"-corridor en de eerste Chinese lijn voor dubbelhoog-containervervoer [C4].
Daarmee vervalt de omweg over Hangzhou: 云龙 → 义乌 188,3 km, dan 沪昆 westwaarts van
义乌 (km 118,3) naar 贵溪 (km 451,2) = **332,9 km**.

| # | km | punt | type | bron | status |
|---|---|---|---|---|---|
| 1 | 0 | 北仑港站 → 云龙站 (aansluiting op de Yong-Jin) | laadplek / kruising | [C1][C4] | aannemelijk |
| 2 | ~40 | 奉化 | passage | [C4] | aannemelijk |
| 3 | ~100 | 嵊州 / 新昌 | passage | [C4] | aannemelijk |
| 4 | ~165 | 东阳 | passage | [C4] | aannemelijk |
| 5 | ~223 | **义乌站** — invoegen op de 沪昆 | kruising | [C4] | bevestigd |
| 6 | ~276 | 金华 | station | [C3] | bevestigd |
| 7 | ~358 | 衢州 | station | [C3] | bevestigd |
| 8 | ~468 | 上饶 | station | [C3] | bevestigd |
| 9 | **~556** | **贵溪站** | losplek | [C3] | bevestigd |

### Negatieve ankers been 3 — de drie manieren waarop dit been fout kan gaan

1. **鹰潭 (Yingtan) ligt 20 km VOORBIJ Guixi** (沪昆 km 471,5 tegen 451,2). Wie uit het
   oosten komt, passeert Guixi eerst. Een lijn die via Yingtan loopt en terugkeert, of die
   in Yingtan eindigt, is fout. Yingtan is wél het regionale knooppunt en trekt daarom
   routers aan [C3].
2. **皖赣铁路 (Wuhu → Guixi, 539,92 km) is de BINNENLANDSE ertslijn, niet de importlijn.**
   Over die as komt het eigen erts van **Dexing** en **Yongping** naar Guixi, en via
   **贵溪北站** vertrekken juist de producten (elektrolytkoper, zwavelzuur, slak — sinds
   2013 gemiddeld ~3 mln ton/jaar) [C5][C7]. Ingevoerd concentraat uit Ningbo hoort daar
   niet overheen.
3. **De 883 km-meting van de atlas past op geen van beide corridors** (+41% op A, +59% op
   B). Dat is de verklikker: de huidige lijn loopt ergens anders — kandidaat-verdachten
   zijn een omweg via Yingtan/Nanchang of via de Wan-Gan-as.

## Been 4 · last mile — 贵溪站-aansluitspoor → ertslosbundel op het smelterterrein

| # | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|
| 1 | **贵溪站 goederenemplacement** — vanaf hier lopen aansluitsporen naar o.a. 江铜贵溪冶炼厂, de brugfabriek van CREC-24, de elektriciteitscentrale en het landbouwbedrijf | kruising | — | [C6] | bevestigd |
| 2 | Aansluitspoor over het smelterterrein (het door OSM gemiste middenstuk staat hand-geplaatst in `landnet-handmatig.geojson`) | passage | — | [E3] | aannemelijk |
| 3 | **Ertslosbundel Guixi** — meerdere parallelle sporen met wagons, twee portaalkranen boven een losbunker, silo's ten noorden ervan | losplek (keten-eind) | 28.3271, 117.2260 | [E3] + satelliet z18 | **satelliet-gelegd** |
| 4 | Polygoon-middelpunt van het smelterterrein, ~800 m noordelijker — dáárop snapte de route eerder naar een noordstreng en tekende een lus om de fabriek | referentie (niet aan lijn) | — | [E3] | bevestigd |
| 5 | **贵溪北站** (Wan-Gan-zijde) — uitgaande producten; niet de aankomstkant van dit been | referentie (niet aan lijn) | — | [C7] | aannemelijk |

**Bevestigd door de satelliet (z18, 0,53 m/px):** het punt `cu-guixi-spoor` uit
`aansluitingen.json` ligt **exact op de losbundel** — zichtbaar zijn de parallelle sporen
met wagons, twee portaalkranen over een langgerekte bunker, en het silopark erboven. Van
de vier ankers van deze stroom is dit de enige die de check ongewijzigd doorstaat.

## Conflicten met de projectdata (afwerklijst)

| # | wat | nu | hoort te zijn | bron |
|---|---|---|---|---|
| 1 | `cu-escondida-laad` | -24.27004 / -69.07169 (ín de put) | **-24.2620 / -69.0600** (concentrator + indikkers = kop van de leiding) | satelliet z16 |
| 2 | `cu-coloso-kade` | -23.76015 / -70.46332 (kustweg bij het dorp) | **-23.7569 / -70.4652** (kop laadsteiger); filterfabriek -23.7590 / -70.4670 | satelliet z17 |
| 3 | `cu-beilun-kade` | 121.87573 / 29.92742 (waar de transportband aan land komt) | **121.8830 / 29.9364** (losberth met ertslossers); het bandpunt blijft als begin van de last mile | satelliet z16 |
| 4 | flow `cu-escondida → cu-ref-jiangxi`, `via: [cu-port-antofagasta, cu-port-ningbo]` | via de haven Antofagasta | via **Coloso** (Escondida's eigen terminal, 12 km zuidelijker) | [E3] |
| 5 | spoorbeen Beilun→Guixi | gemeten **883 km** | **~628 km** (corridor A) of **~556 km** (corridor B) | [C1][C2][C3][C4] |
| 6 | leiding-been Escondida→Coloso | ontbreekt / recht | **gestippeld mét reden** (~170 km, eigen verbinding, geen OSM-tracé) | [E1] + werkwijze §7 |

## Wat de kaart moet tekenen (voorstel)

1. **Leidingbeen** (stippel, amber): concentrator -24,2620/-69,0600 → Coloso-filterfabriek
   -23,7590/-70,4670. Label: *slurryleiding ~170 km — eigen verbinding, geen net.*
2. **Zeebeen** (zeeschip): kop laadsteiger Coloso → Beilun-losberth. Router vrij; de
   Antofagasta-via eruit.
3. **Spoorbeen**: Beilun-ertsterminal → 贵溪站, via-punt→via-punt langs de brief. **Kies
   corridor A tot er een bron voor B is** — A is de historische lijn en B is pas sinds
   2024 open; noteer het verschil (628 vs 556 km) in de noot.
4. **Last mile** (stippel, kort): 贵溪站 → ertslosbundel 117,2260/28,3271.
5. **Niet tekenen:** de tak Escondida → Chuquicamata (aparte flow) en het uitgaande
   product uit Guixi (andere keten).

## Bronnen

**Escondida/Coloso [E..]:** E1 Mining Technology — Escondida (170 km leiding, 9 inch,
pulp 65% vaste stof, filteren te Coloso) · E2 BHP *Chilean copper site tour 2024*
(concentrators Los Colorados / Laguna Seca) · E3 OpenStreetMap (ODbL) + eigen
satelliet-overlay Esri World Imagery z15–z18, gelegd 2026-07-28.

**Zee [Z..]:** Z1 atlas-invariant Antofagasta→Shanghai 18.915 km (searoute 18.880), M23.

**China-spoor [C..]:** C1 zh.wikipedia *北仑支线* (35,4 km; stations 宁波东/宝幢/大碶/
北仑/北仑港; elektrificatie 2015–2019) · C2 zh.wikipedia *萧甬铁路* (146,4 km neerwaarts;
stationskilometrering Hangzhou-Zuid 0 → Ningbo 147) · C3 wikipedia *浙赣铁路* (kilometrering
杭州东 5,1 → 贵溪 451,2 → 鹰潭 471,5 → 株洲 911,5; sinds 2006-12-31 deel van de 沪昆铁路) ·
C4 zh.wikipedia + persberichten *甬金铁路* (188,3 km, geopend 2023-12-31, vracht vanaf
2024-01-10, 云龙 → 义乌) · C5 zh.wikipedia/baike *皖赣铁路* (火龙岗 → 贵溪, 539,92 km) ·
C6 zh.wikipedia *贵溪站* (aansluitsporen naar o.a. 江铜贵溪冶炼厂) · C7 bron over 贵溪北站
(uitgaand elektrolytkoper/zwavelzuur/slak, ~3 mln t/jaar sinds 2013) · C8 *宁波－舟山港总体
规划 2014-2030* (ertsligplaatsen bedienen de metallurgie van de Yangtze-delta).

**Afnemer [J..]:** J1 Jiangxi Copper / Guixi Smelter — grootste kopersmelter ter wereld,
feedstock grotendeels ingevoerd concentraat (Peru, Chili, Afrika).
