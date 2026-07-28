# Routebrief · koper — Escondida → walsdraad Guixi (China)

**stroom-id:** `koper-escondida-guixi`  ·  **geschreven:** 2026-07-28, herschreven naar het mijn-tot-eindproduct-sjabloon + fasen D/E toegevoegd 2026-07-29  ·  **status brief:** fase A–C in toets geslaagd (spoortoets 2026-07-28) · fase D–E concept (satellietpass open)
**Keten in één zin:** sulfide-concentraat uit Escondida, als slurry per **eigen leiding** (~170 km) naar Puerto Coloso, daar gefilterd en per **bulkcarrier** naar de Beilun-ertsterminal (Ningbo-Zhoushan), per **spoor** (corridor B, 550,5 km gemeten) naar 贵溪站 en over het aansluitspoor de ertslosbundel van 's werelds grootste kopersmelter op; de **kathode** gaat vervolgens over het eigen complex naar de **walsdraadfabriek** van 江西铜业铜材有限公司 (walsdraad Φ8 mm + getrokken draad), waarna het product als marktwaaier naar Oost-China vertrekt — het beargumenteerde stoppunt.

*Volgens `../routebrief-werkwijze.md`. Oorspronkelijk de derde routebrief en de eerste volgens het aangescherpte formaat van 2026-07-28 (kop en staart satelliet-gelegd op z16/z17 vóórdat ze anker werden, de last mile als eigen been, en waar het net niet reikt een stippellijn mét reden); nu doorgetrokken tot het eindproduct conform werkwijze §1a.*

*Toets-doel: dit is de stroom die LAR-527 "de zware" noemt — het China-spoorbeen heeft het
grootste risico op een verkeerde corridor.*

*Notatie (hard): coördinaten altijd **lat, lon** met **decimale punt**; ankers 5 decimalen, passages 2–4. Elk been draagt een been-id `koper-escondida-guixi-b<n>`; ankers dragen waar mogelijk het id uit `aansluitingen.json`.*

> **✅ UITSLAG (gemeten 2026-07-28): het spoorbeen KLOPT.** Over het huidige spoornet meet
> Beilun-ertsterminal → Guixi **550,5 km** (143 edges, verhouding 1,13 op de grootcirkel),
> en de tweezijdige toets van werkwijze §4 slaagt volledig: de lijn raakt élk brief-punt van
> **corridor B** — Ningbo, Yunlong, Fenghua, Shengzhou, Dongyang, Yiwu, Jinhua, Longyou,
> Quzhou, Jiangshan, Yushan, Shangrao, Hengfeng, Yiyang, Guixi — binnen 0,8–6,4 km, mijdt
> alle punten die alléén op corridor A liggen (**Hangzhou 87,4 km** ernaast, Shaoxing 56,5,
> Yuyao 45,9, Zhuji 31,2) en raakt géén van de drie negatieve ankers (Yingtan 14,6 km,
> Jingdezhen 98,5, Nanchang 136,4). 550,5 tegen de brief-corridor van ~556 km is **−1,0%**.
> De router rijdt dus over de **Yong-Jin-vrachtlijn**, precies zoals de brief voorspelde.
>
> ⚠️ **Correctie op een eerdere versie van deze brief.** Die stelde dat de atlas dit been op
> **883 km** mat en dat de lijn daarom op een andere corridor lag. Dat getal komt uit de
> heal-ronde van 2026-07-24 en is **niet** met dit gereedschap tussen deze twee kades
> gemeten; met beide ankersets (oud én satelliet-gelegd) snapt de route op dezelfde
> hoofdnet-knoop en komt er 550,5 km uit. De 883 km hoort bij een andere meting op een
> ouder netstadium — er was hier dus geen corridor-fout.

---

## 1 · Ketenkaart

```
Escondida-concentrator ──(b1 slurryleiding, stippel ~170 km)──► Puerto Coloso (filter + laadsteiger)
  cu-escondida-laad                                              cu-coloso-kade
                       ──(b2 zee, gemeten 19.104 km)──► Beilun-ertsterminal (losberth)
                                                         cu-beilun-kade
                       ──(b3 spoor, 550,5 km corridor B)──► 贵溪站 (goederenemplacement)
                       ──(b4 last mile aansluitspoor)──► ertslosbundel 贵溪冶炼厂
                                                          cu-guixi-spoor
  ◄── samenvloeiing knoop 贵冶: binnenlands erts Dexing/Yongping komt binnen over de 皖赣 (贵溪北站)
                       ──(b5 intern wegtransport op het complex, stippel)──► walsdraadfabriek
                                                          江西铜业铜材有限公司, 冶金大道 15
                       ──(b6 weg/spoor, niet getekend)──► afnemers Oost-China (STOPPUNT: marktwaaier)
  ├── vertakking na knoop 贵冶: ~2/3 kathode per spoor via 贵溪北站 → markt/SHFE (geen eigen brief)
  ├── vertakking na knoop 贵冶: kathode → 22万吨-walsdraadlijn 上饶经开区 (aandeel onbekend)
  ├── vertakking na knoop walsdraad: → 江铜华东电工 (鹰潭高新区, elektromagnetische draad, aandeel onbekend)
  └── bijproduct via 贵溪北站: zwavelzuur (o.a. blocktrein → 分宜) + slak — geen koperstreng
```

| | |
|---|---|
| **Fasen** | A leiding mijn → zeeterminal · B zee · C aanlanding → smelter (incl. last mile) · D kathode → walsdraadfabriek · E walsdraad → markt |
| **Benen** | 6 (doorlopend genummerd `koper-escondida-guixi-b1` … `b6`) |
| **Overslagen** | 2 volwaardige drager-wissels (Coloso: leiding→zee · Beilun: zee→spoor), elk met terreinstappen; het vertrek-anker van Beilun (北仑港站-laadspoor) heeft nog geen coördinaat → §5 |
| **Gedeelde benen** | geen — geen andere brief deelt een been; het traject 义乌→贵溪 is binnen déze brief gedeeld materiaal van corridor A en B |
| **Vertakkingen** | na been 4 (knoop 贵冶): kathode naar markt/SHFE per spoor via 贵溪北站 (~2/3, schatting) · naar 上饶经开区 · na been 5: naar 鹰潭高新区 — zie §4 |
| **Reële alternatieven** | geen gedocumenteerd op fase A–C: de import voor Guixi landt aan bij Beilun [C8][J1]; er is geen bron voor een Zhangjiagang/Jiangyin-lightering op déze streng (die klasse hoort bij de Yangtze-smelters, zie `koper-collahuasi-tongling`) |

## 2 · Productvormen per fase — wat beweegt er fysiek

| fase | product | vorm / verpakking | gehalte of specificatie | omzetting in de volgende stap | jaarvolume |
|---|---|---|---|---|---|
| A | sulfide-concentraat | slurry, ~65% vaste stof, in een 9-inch leiding; te Coloso gefilterd tot natte bulk [E1] | ~28–30% Cu | → smelten/converteren/elektrolyse | — (niet in deze brief gemeten) |
| B | zelfde concentraat | natte bulk in de ruimen van een bulkcarrier | idem | → lossen Beilun, band naar ertsveld | — |
| C | zelfde concentraat | bulk in open wagons | idem | → smelter Guixi | — |
| D | kathode, merk "贵冶牌" | bundels stukgoed (kathodeplaten), SHFE-/LME-klasse | Grade A, ≥99,99% Cu | → walsdraad Φ8 mm (continugieten + walsen) | capaciteit smelter 1,10 mln t/j [J2]; naar de eigen walsdraadfabriek ~0,37 mln t (afgeleid uit [D1]) |
| E | walsdraad + draad | coils walsdraad Φ8 mm (电工用铜线坯) · getrokken ronde draad Φ2,0–3,6 mm | elektrotechnische kwaliteit | → draad/kabel bij afnemers in Oost-China (eindgebruik) | 370 kt walsdraad + 120 kt draad [D1] |

### 2a · De productvraag per laad-, overslag- en losplek

*Zes stappen per plek, mét wat de productvorm uitsluit (werkwijze §2a).*

**L1 · Escondida-concentrator (laadplek been 1)**

| stap | antwoord |
|---|---|
| 1 | concentraat als **slurry** (~65% vaste stof) — pompbaar product, geen stortgoed [E1] |
| 2 | concentrator met indikkers + pompstation: de kop van een slurryleiding |
| 3 | BHP Escondida — concentrators Los Colorados / Laguna Seca [E2] |
| 4 | deze stroom = de hele leiding (eigen mijn, eigen leiding, één product) |
| 5 | het indikkerpark direct naast de concentrator |
| 6 | **-24.26200, -69.06000** — satelliet z16 (2026-07-28): rij ronde indikkers zichtbaar |

**Uitsluit:** slurry vertrekt niet per truck of trein (geen laadkuil, geen weegbrug-stroom); een **open put is geen laadplek** — het oude anker lag 1,5 km ZW ín de put, en een leiding begint niet in een put.

**L2 · Puerto Coloso (overslag been 1 → been 2)**

| stap | antwoord |
|---|---|
| 1 | slurry in → **gefilterd nat concentraat** (bulk) uit |
| 2 | filterfabriek + opslag + steiger met scheepslader (trestle de zee in) |
| 3 | Escondida's **eigen** terminal — geen publieke haven [E3] |
| 4 | deze stroom = alles wat de terminal behandelt |
| 5 | de laadsteiger; de ligplaats van de bulkcarrier ligt aan de **kop** |
| 6 | **-23.75690, -70.46520** — satelliet z17 (2026-07-28): steiger met bulkcarrier |

**Uitsluit:** geen containerkade en niet de stadshaven Antofagasta (stukgoed/containers, 13,6 km noordelijker); **slurry eindigt bij de filterfabriek en niet aan de pier** — op het schip gaat gefilterd concentraat, geen pulp.

**L3 · Beilun-ertsterminal (overslag been 2 → been 3, aankomstzijde)**

| stap | antwoord |
|---|---|
| 1 | concentraat, natte bulk in ruimen |
| 2 | gespecialiseerde **ertsterminal**: losberth met brugloskranen + transportband naar een ertsveld |
| 3 | Ningbo-Zhoushan, 北仑矿石码头 [E3][C8] |
| 4 | de ertsligplaatsen bedienen de metallurgie van de Yangtze-delta en het achterland per spoor [C8] |
| 5 | de losberth met de rode ertslossers, noordoostelijk van het ertsveld |
| 6 | **29.93640, 121.88300** — satelliet z16 (2026-07-28) |

**Uitsluit:** niet de containerkades ernaast (containers ≠ bulk); concentraat voor binnenland-smelters komt **niet** binnen op een containerhaven op eilanden voor de kust (de Yangshan-klasse); de berth is niet het laadspoor — de **band** verbindt water- en spoorzijde, dus één punt kan niet allebei zijn.

**L4 · Ertslosbundel 贵溪冶炼厂 (losplek been 4)**

| stap | antwoord |
|---|---|
| 1 | concentraat, bulk in open wagons |
| 2 | losbundel: parallelle sporen, portaalkranen boven een losbunker, silo's |
| 3 | 江铜贵溪冶炼厂 — aansluitsporen vanaf 贵溪站 [C6] |
| 4 | grootste kopersmelter ter wereld, draait grotendeels op ingevoerd concentraat [J1] |
| 5 | de ertslosbundel aan de noordzijde van het complex |
| 6 | **28.32710, 117.22600** — satelliet z18 (2026-07-28): sporen met wagons, twee portaalkranen, silopark |

**Uitsluit:** niet via 贵溪北站 — de 皖赣-kant is de kant van het **uitgaande product en het binnenlandse erts** [C5][C7]; niet het polygoon-middelpunt van het terrein (800 m noordelijker — daar snappen routers op, de oude lus-fout).

**L5 · Kathode-laadplek 贵冶 (laadplek been 5) — NIEUW, fase D**

| stap | antwoord |
|---|---|
| 1 | kathodeplaten "贵冶牌", gebundeld stukgoed |
| 2 | elektrolysehal → strip-/weeg-/bundelstation → productmagazijn/expeditie |
| 3 | 贵溪冶炼厂 (elektrolyse); afvoerkanalen: interne weg naar de walsdraadfabriek, spoor via 贵溪北站 (markt-vertakking), weg |
| 4 | déze streng: de bundels voor de **eigen** walsdraadfabriek — die noemt "贵冶牌"-kathode expliciet als hoofdgrondstof [D1] |
| 5 | magazijn-/expeditiehal — exacte plek onbekend → §5 |
| 6 | **open** — satellietpass z16/z18 nodig → §5 |

**Uitsluit:** kathode gaat **niet** over de ertslosbundel of de transportband (bulkinfrastructuur); niet in tankwagons (dat is het zwavelzuur [D7]); en voor déze streng niet via 贵溪北站 — wat daar vertrekt is de markt-vertakking en het bijproduct [C7][D6].

**L6 · Walsdraadfabriek 江西铜业铜材有限公司 (losplek been 5 + laadplek been 6) — NIEUW, fase D/E**

| stap | antwoord |
|---|---|
| 1 | in: kathodebundels; uit: coils walsdraad Φ8 mm + getrokken draad Φ2,0–3,6 mm |
| 2 | continugiet-/walslijn + draadtrekkerij; expeditie voor coils |
| 3 | 江西铜业铜材有限公司 (opgericht 2002), Guixi-vestiging **冶金大道 15** — hetzelfde complexadres als de smelter/JCC-zetel [D1][D3] |
| 4 | JCC's eigen verwerkingsfabriek; hoofdgrondstof "贵冶牌"-kathode [D1] |
| 5 | adres bekend; exacte hal/laaddeur onbekend → §5 |
| 6 | **open** — satellietpass nodig → §5 |

**Uitsluit:** geen bulkbehandeling (het concentraat-tijdperk is voorbij bij de smelter); geen zeekade (300+ km binnenland); coils vertrekken per vrachtwagen of wagon, niet per band.

### 2b · De overslagregel in deze keten

Een overslag is elke **drager-wissel** en krijgt twee ankers + terreinstappen (werkwijze §2b). In deze keten: **Coloso** (leiding → zee: filterfabriek → wal-einde → kop laadsteiger, drie satelliet-gelegde punten) en **Beilun** (zee → spoor: losberth → band/ertsveld → 北仑港站-laadspoor; het derde punt heeft nog geen coördinaat → §5). De knopen 贵冶 (been 4→5) en walsdraadfabriek (been 5→6) zijn **verwerkingsknopen**, geen overslagen: het product verandert er. **Anker ≠ routeerpunt** is bij Beilun gemeten beleid: de berth ligt in het water en het havenspoor eindigt bij het ertsveld, dus een spoor-snap van 1,3 km is dáár correct, geen fout.

## 3 · Kernfeiten die de vorm van de keten bepalen

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
4. **De aankomstkant was de scherpste onzekerheid — inmiddels gemeten beslecht.** Guixi ligt
   ~550–630 km landinwaarts; het is de grootste kopersmelter ter wereld en draait grotendeels
   op **ingevoerd** concentraat (Peru, Chili, Afrika) [J1]. Welke van de twee spoorcorridors dat
   concentraat rijdt was met open bronnen niet hard te maken — beide staan hieronder mét
   kilometrering, en de toets van 2026-07-28 wees **corridor B** aan (zie het kader bovenaan).
5. **De kathode heeft een gedocumenteerde eerste bestemming óp het eigen complex** (fase D):
   江西铜业铜材有限公司 maakt in Guixi **370 kt/j walsdraad Φ8 mm + 120 kt/j ronde draad
   Φ2,0–3,6 mm** met "贵冶牌"-kathode als hoofdgrondstof, en zit op hetzelfde complexadres
   (冶金大道 15) als de smelter [D1][D3]. De eerste bestemming is dus **geen spoorreis maar
   een interne overbrenging**.
6. **Wat wél het spoor op gaat, gaat via 贵溪北站 (皖赣) — en dat is de vertakking, niet deze
   streng.** De smelter sluit met een eigen 专用铁路 aan op de 皖赣铁路 bij 贵溪北站;
   elektrolytkoper, zwavelzuur en slak, samen ~3 mln t/jaar sinds 2013 [C7][D5]. Sinds
   2026-04 rijdt er o.a. een zwavelzuur-blocktrein 贵溪北 → 分宜 [D6].

---

# FASE A · Escondida-concentrator → Puerto Coloso

## Been 1 · slurryleiding — Escondida-concentrator → Puerto Coloso (~170 km, stippel)

**been-id:** `koper-escondida-guixi-b1`
**Modaliteit:** slurryleiding (eigen verbinding)
**Lengte:** gepubliceerd ~170 km [E1] — de enige controle die dit been heeft, want er is geen tracé-geometrie
**Net / bron geometrie:** geen — geen OSM-tracé (kernfeit 3)
**Stippel:** ja — eigen verbinding, geen net (werkwijze §7); dit is de **eindvorm**
**Corridor bij naam:** Escondida-concentraatleiding (9 inch) [E1]
**Routeerpunt kop / staart:** n.v.t. — eigen verbinding, geen net om op te routeren
**Toets-marge:** n.v.t. (alleen de lengtetoets ~170 km)

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **Escondida-concentrator + indikkerpark** — kop van de slurryleiding (`cu-escondida-laad`) | laadplek | -24.26200, -69.06000 | [E3] + satelliet z16 | **satelliet-gelegd** |
| 2 | — | **Rajo Escondida** (de put zelf) ligt ~1,5 km ZW; erts gaat per truck/band naar de molen, niet de leiding in | referentie (niet aan lijn) | -24.27000, -69.07170 | [E3] | bevestigd |
| 3 | — | Laguna Seca-concentrator (tweede molen op het complex) | referentie (niet aan lijn) | — | [E2] | aannemelijk |
| 4 | ~170 | **Coloso filterfabriek + stockpile** — slurry wordt hier ontwaterd | overslag | -23.75900, -70.46700 | [E3] + satelliet z17 | **satelliet-gelegd** |
| 5 | ~170 | Wal-einde van de laadsteiger (begin van de trestle naar zee) | overslag | -23.75790, -70.46590 | satelliet z17 | **satelliet-gelegd** |
| 6 | ~171 | **Kop van de laadsteiger / scheepslader** — hier ligt de bulkcarrier (`cu-coloso-kade`) | laadplek zee | -23.75690, -70.46520 | satelliet z17 | **satelliet-gelegd** |

**Opmerkingen been 1.** ⚠️ **Twee correcties op de projectdata, allebei door de
satellietregel gevonden.** (a) `cu-escondida-laad` stond op **-24.27004, -69.07169** —
dat ligt op een berm midden **ín de open put**, ~1,5 km van de molen. Een leiding begint
niet in een put. (b) `cu-coloso-kade` stond op **-23.76015, -70.46332**; op de tegels is
dat de **kustweg bij het dorp Coloso**, ~400 m oostelijk van de terminal — de steiger ligt
noordwestelijker en steekt de zee in. Zelfde klasse als de New Orleans-centroïde en het
Nacala-west-jetty-punt: een OSM-treffer is een kandidaat, geen anker.
Lengte-toets: de brief-leiding meet ~170 km [E1].

**Negatieve ankers been 1** — geen: de leiding is een eigen verbinding met maar één
mogelijk tracé-idee; de foutklassen van dit been zaten in de **uiteinden** (de twee
correcties hierboven), niet in een verkeerde corridor.

## Overslag been 1 → been 2 — Puerto Coloso

**Productvraag:** slurry wordt hier ontwaterd; gefilterd concentraat gaat via de steiger op een bulkcarrier — dus filterfabriek + eigen laadsteiger, geen publieke kade (ladder L2 in §2a).

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst been 1 | Coloso filterfabriek + stockpile (einde leiding) | losplek/verwerkingsstap | -23.75900, -70.46700 | [E3] + satelliet z17 | **satelliet-gelegd** |
| 2 | terrein | wal-einde laadsteiger (begin trestle) | passage | -23.75790, -70.46590 | satelliet z17 | **satelliet-gelegd** |
| 3 | vertrek been 2 | kop laadsteiger / scheepslader (`cu-coloso-kade`) | laadplek | -23.75690, -70.46520 | satelliet z17 | **satelliet-gelegd** |

**Routeerpunt ≠ anker.** Zee-routeerpunt (MARNET-raakpunt) **-23.80000, -71.30000**, snap
**85,1 km** [`aansluitingen.json`] — Chili heeft nul havens met varend AIS-verkeer, dus de
haven-aanloop is hier per werkwijze §7 een **stippellijn als eindvorm**, geen tussenstand.

---

# FASE B · zee

## Been 2 · zee — Puerto Coloso → Ningbo-Zhoushan (Beilun-ertsterminal)

**been-id:** `koper-escondida-guixi-b2`
**Modaliteit:** bulkcarrier  ·  **Router:** zee = vrij geroutet (werkwijze §6): kade→kade, alleen sanity-ankers
**Lengte:** gemeten **19.104 km** (atlas-keten `?v=099`, 2026-07-28); orde-toets: atlas-invariant Antofagasta→Shanghai **18.915 km** (searoute 18.880) [Z1]
**Overslagen onderweg:** geen — bulk vaart **direct**, geen transshipment-hub (bulk is geen lijndienst; de direct-vs-hub-vraag speelt hier niet)
**Routeerpunt kop / staart:** -23.80000, -71.30000 (snap 85,1 km — stippel-aanloop, zie overslagblok) · 29.94780, 121.88370 (snap 1,3 km — het schip ligt in het water vóór de berth) [`aansluitingen.json`]

| # | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|
| 1 | **Coloso — kop laadsteiger** (vertrek, `cu-coloso-kade`) | laadplek | -23.75690, -70.46520 | satelliet z17 | **satelliet-gelegd** |
| 2 | Open Stille Oceaan, noordelijke grootcirkel-lane richting Oost-Azië | passage | — | [Z1] | aannemelijk |
| 3 | **Beilun-ertsterminal — losberth met ertslossers** (aankomst, `cu-beilun-kade`) | losplek | 29.93640, 121.88300 | [E3] + satelliet z16 | **satelliet-gelegd** |

**Negatieve ankers been 2** — de reis vaart de noordelijke Pacific-lane; wat bronnen of routers ook suggereren, hier komt de lijn niet:

| punt | lat, lon | straal | reden |
|---|---|---|---|
| Panamakanaal (Gatún-sluizen) | 9.27300, -79.92300 | 500 km | verkeerd halfrond voor deze reis (centroïde-precisie) |
| Straat Magellaan (Punta Arenas) | -53.16300, -70.91700 | 300 km | geen zuidelijke omweg — de lane loopt over de noordelijke grootcirkel [Z1] |
| Kaap Hoorn | -55.98300, -67.26700 | 300 km | idem |
| Haven Antofagasta (stadshaven) | -23.65200, -70.39800 | 5 km | `data/copper.js` stuurt deze stroom via `cu-port-antofagasta`, maar Escondida's concentraat vertrekt van de **eigen** terminal Coloso, 13,6 km hemelsbreed zuidelijker (buiten deze straal) [E3] |

De atlas-invariant voor deze oversteek is de gemeten Antofagasta→Shanghai-lane van
**18.915 km** (searoute 18.880) — Coloso→Beilun hoort in dezelfde orde te liggen [Z1],
en de gemeten 19.104 km ligt dat ook.

## Overslag been 2 → been 3 — Beilun-ertsterminal

**Productvraag:** natte bulk lost aan een gespecialiseerde ertsterminal met brugloskranen; de band brengt het naar het ertsveld waar het op wagons gaat — dus losberth ≠ laadspoor (ladder L3 in §2a).

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst been 2 | losberth met de rode ertslossers (`cu-beilun-kade`) | losplek | 29.93640, 121.88300 | [E3] + satelliet z16 | **satelliet-gelegd** |
| 2 | terrein | transportband-landpunt + ertsveld (het oude OSM-anker; blijft als begin van de spoor-last-mile) | verwerkingsstap/opslag | 29.92742, 121.87573 | OSM (ODbL) | bevestigd |
| 3 | vertrek been 3 | **北仑港站** — laadspoor van het havenstation | laadplek | — | [C1] | bevestigd (coördinaat ontbreekt → §5) |

**Routeerpunt ≠ anker.** Zee: 29.94780, 121.88370 (snap 1,3 km) · spoor: 29.92820, 121.87380
(snap 1,3 km) [`aansluitingen.json`]. De berth ligt in het water en het havenspoor eindigt
bij het ertsveld — één punt kan niet tegelijk ligplaats én laadspoor zijn; als dat gaat
knellen hoort er een **tweede aansluiting** te komen (werkwijze §2b), geen compromis-coördinaat.

---

# FASE C · aanlanding → smelter

## Been 3 · spoor — Beilun-ertsterminal → 贵溪站

**been-id:** `koper-escondida-guixi-b3`
**Modaliteit:** spoor  ·  **Brief-gestuurd** (werkwijze §6: geen vrije Dijkstra)
**Lengte:** gemeten **550,5 km** (`toets_spoorroute.mjs`, Beilun-ertsterminal ↔ 贵溪, netstadium 2026-07-28) / corridor B ~556 km (**−1,0%**) · corridor A 628 km (historische variant)
**Net / bron geometrie:** M25-landnet (OSM) — de toets van §4 is op dit net geslaagd
**Stippel:** nee
**Corridor bij naam:** 北仑支线 → **甬金铁路** (Yong-Jin) → 沪昆铁路 (= corridor B, gemeten); historisch 北仑支线 → 萧甬铁路 → 沪昆/浙赣 (= corridor A)
**Routeerpunt kop / staart:** 29.92820, 121.87380 (max snap 1,3 km — havenspoor eindigt bij het ertsveld) · 28.32710, 117.22650 (max snap 0,05 km) [`aansluitingen.json`]
**Toets-marge:** afwijkend per punt: corridorpassages **8 km** — de geslaagde toets raakte de brief-punten op 0,8–6,4 km; een vaste 2 km had die correcte route afgekeurd (werkwijze §4)

Dit been is **brief-gestuurd**. Er zijn **twee** reële corridors; welke er gereden wordt
was met open bronnen niet te beslissen — beide staan hier met hun officiële kilometrering,
zodat de getekende lijn eenduidig te toetsen is. De meting van 2026-07-28 (kader bovenaan)
wees **corridor B** aan; corridor A blijft staan als historische variant en toetsmateriaal.

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
| 26 | **628** | **贵溪站** (km 451,2) — losstation voor de smelter | losplek / eind spoorbeen | 28.29308, 117.20972 | [C3][C6][D4] | bevestigd (coördinaat aannemelijk, satellietpass open → §5) |

### Corridor B — sinds 2024, via de Yong-Jin-vrachtlijn (~556 km) — GEMETEN DE GEREDEN CORRIDOR

**甬金铁路** (Ningbo–Jinhua/Yiwu) is op **31 december 2023** geopend en rijdt sinds
**10 januari 2024** vracht: 188,3 km van **云龙站** (Yinzhou, Ningbo) via Fenghua,
Shengzhou, Xinchang en Dongyang naar **义乌站**, gebouwd als vrachtlijn voor de
"义甬舟"-corridor en de eerste Chinese lijn voor dubbelhoog-containervervoer [C4].
Daarmee vervalt de omweg over Hangzhou: 云龙 → 义乌 188,3 km, dan 沪昆 westwaarts van
义乌 (km 118,3) naar 贵溪 (km 451,2) = **332,9 km**.

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | 北仑港站 → 云龙站 (aansluiting op de Yong-Jin) | laadplek / kruising | — | [C1][C4] | aannemelijk |
| 2 | ~40 | 奉化 | passage | — | [C4] | aannemelijk |
| 3 | ~100 | 嵊州 / 新昌 | passage | — | [C4] | aannemelijk |
| 4 | ~165 | 东阳 | passage | — | [C4] | aannemelijk |
| 5 | ~223 | **义乌站** — invoegen op de 沪昆 | kruising | — | [C4] | bevestigd |
| 6 | ~276 | 金华 | station | — | [C3] | bevestigd |
| 7 | ~358 | 衢州 | station | — | [C3] | bevestigd |
| 8 | ~468 | 上饶 | station | — | [C3] | bevestigd |
| 9 | **~556** | **贵溪站** | losplek | 28.29308, 117.20972 | [C3][D4] | bevestigd (coördinaat aannemelijk → §5) |

### Negatieve ankers been 3 — de drie manieren waarop dit been fout kan gaan

| punt | lat, lon | straal | reden |
|---|---|---|---|
| 鹰潭 (Yingtan, stadscentroïde) | 28.26000, 117.07000 | 8 km | ligt 20 km **voorbij** Guixi (沪昆 km 471,5 tegen 451,2); een lijn die via Yingtan loopt en terugkeert, of er eindigt, is fout — gemeten blijft de route er 14,6 km vandaan ✅ [C3] |
| 景德镇 (Jingdezhen, aan de Wan-Gan-as) | 29.29000, 117.21000 | 25 km | de 皖赣 is de **binnenlandse** ertslijn, niet de importlijn — gemeten 98,5 km ✅ [C5][C7] |
| 南昌 (Nanchang) | 28.68000, 115.89000 | 50 km | omweg waarop een router kan uitkomen — gemeten 136,4 km ✅ |

1. **鹰潭 (Yingtan) ligt 20 km VOORBIJ Guixi** (沪昆 km 471,5 tegen 451,2). Wie uit het
   oosten komt, passeert Guixi eerst. Een lijn die via Yingtan loopt en terugkeert, of die
   in Yingtan eindigt, is fout. Yingtan is wél het regionale knooppunt en trekt daarom
   routers aan [C3].
2. **皖赣铁路 (Wuhu → Guixi, 539,92 km) is de BINNENLANDSE ertslijn, niet de importlijn.**
   Over die as komt het eigen erts van **Dexing** en **Yongping** naar Guixi, en via
   **贵溪北站** vertrekken juist de producten (elektrolytkoper, zwavelzuur, slak — sinds
   2013 gemiddeld ~3 mln ton/jaar) [C5][C7]. Ingevoerd concentraat uit Ningbo hoort daar
   niet overheen.
3. **Nanchang** (28.68, 115.89) en **Jingdezhen** (29.29, 117.21, aan de Wan-Gan-as) —
   de twee omwegen waarop een router zou kunnen uitkomen. Gemeten: de route blijft er
   136,4 resp. 98,5 km vandaan. ✅

**Gemeten uitslag (2026-07-28, `toets_spoorroute.mjs`):** 550,5 km, corridor B, alle
bevestigde punten geraakt, alle negatieve ankers gemeden. Zie het kader bovenaan.

## Been 4 · last mile — 贵溪站-aansluitspoor → ertslosbundel op het smelterterrein

**been-id:** `koper-escondida-guixi-b4`
**Modaliteit:** spoor (aansluitspoor) — eigen been, geen rechte stub (werkwijze §3.4)
**Stippel:** deels — het door OSM gemiste middenstuk is hand-geplaatst (zie rij 2)
**Routeerpunt kop / staart:** 28.32710, 117.22650 (staart; max snap 0,05 km) · kop = het 贵溪站-emplacement, exacte aansluitwissel **nog te bepalen**

| # | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|
| 1 | **贵溪站 goederenemplacement** — vanaf hier lopen aansluitsporen naar o.a. 江铜贵溪冶炼厂, de brugfabriek van CREC-24, 鹰潭工务机械段, de elektriciteitscentrale en het landbouwbedrijf | kruising | 28.29308, 117.20972 | [C6][D4] | bevestigd (coördinaat aannemelijk, satellietpass open → §5) |
| 2 | Aansluitspoor over het smelterterrein (het door OSM gemiste middenstuk staat hand-geplaatst in `landnet-handmatig.geojson`) | passage | — | [E3] | aannemelijk |
| 3 | **Ertslosbundel Guixi** — meerdere parallelle sporen met wagons, twee portaalkranen boven een losbunker, silo's ten noorden ervan (`cu-guixi-spoor`) | losplek (eind fase C) | 28.32710, 117.22600 | [E3] + satelliet z18 | **satelliet-gelegd** |
| 4 | Polygoon-middelpunt van het smelterterrein, ~800 m noordelijker — dáárop snapte de route eerder naar een noordstreng en tekende een lus om de fabriek | referentie (niet aan lijn) | — | [E3] | bevestigd |
| 5 | **贵溪北站** (Wan-Gan-zijde) — uitgaande producten; niet de aankomstkant van dit been | referentie (niet aan lijn) | 28.34611, 117.18917 | [C7][D5] | aannemelijk (coördinaat zh.wiki, satellietpass open → §5) |

**Bevestigd door de satelliet (z18, 0,53 m/px):** het punt `cu-guixi-spoor` uit
`aansluitingen.json` ligt **exact op de losbundel** — zichtbaar zijn de parallelle sporen
met wagons, twee portaalkranen over een langgerekte bunker, en het silopark erboven. Van
de vier ankers van deze stroom is dit de enige die de check ongewijzigd doorstaat.

## Verwerkingsknoop · 贵溪冶炼厂 (Jiangxi Copper, Guixi-smelter)

| | |
|---|---|
| **anker-id** | `cu-guixi-spoor` (ertslosbundel; de kathode-laadplek heeft nog geen eigen anker → §5/§6) |
| **eigenaar van dit anker** | deze brief |
| **in** | ingevoerd koperconcentraat via Beilun-spoor (deze streng; aandeel Escondida in de mix onbekend) [J1] |
| **andere ingaande strengen** | binnenlands concentraat van de mijnen **Dexing** en **Yongping** over de 皖赣 (贵溪北站) [C5][C7] — geen eigen brief; overig importconcentraat (Peru, Afrika) [J1] |
| **uit** | kathode "贵冶牌", capaciteit **1,10 mln t/jaar** — grootste smelter ter wereld [J2]; dagproductie ~1/8 van het Chinese totaal [J3] |
| **uitgaande strengen** | deze brief (been 5 → eigen walsdraadfabriek, ~0,37 mln t-schaal [D1]) · vertakking markt/SHFE per spoor via 贵溪北站 (~2/3, schatting — §4) · vertakking 上饶经开区 (22万吨-walsdraadlijn [D10]) |
| **verlies / bijproduct** | zwavelzuur en slak — per spoor via 贵溪北站, samen met het elektrolytkoper ~3 mln t/jaar sinds 2013 [C7]; sinds 2026-04 o.a. een zwavelzuur-blocktrein 贵溪北 → 分宜 (12 tankwagons / 780 t per trein) [D6]; edelmetalen (goud/zilver) blijven in de eigen raffinage |

---

# FASE D · kathode → walsdraadfabriek

*Onderzocht 2026-07-29. De eerste bestemming van de kathode is **gedocumenteerd op het
eigen complex**: 江西铜业铜材有限公司 noemt "贵冶牌"-kathode als hoofdgrondstof en zit op
hetzelfde complexadres (冶金大道 15) als de smelter [D1][D3]. Fase D is dus een **interne
overbrenging**, geen spoor- of wegcorridor. Het spoorbeen 贵溪北站 → markt bestaat óók,
maar dat is de vertakking (§4), niet deze streng.*

## Been 5 · intern wegtransport — kathode-expeditie 贵冶 → walsdraadfabriek 江西铜业铜材有限公司

**been-id:** `koper-escondida-guixi-b5`
**Modaliteit:** intern wegtransport op het complex (aanname — zelfde complexadres; geen bron beschrijft het voertuig → §5)
**Lengte:** ~1–2 km (complex-schaal; niet gemeten)
**Net / bron geometrie:** geen — bedrijfsterrein, geen openbaar net
**Stippel:** ja — eigen verbinding op eigen terrein, geen net (werkwijze §7)
**Routeerpunt kop / staart:** nog te bepalen
**Toets-marge:** n.v.t. tot de ankers er zijn

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **Kathode-laadplek 贵冶** — elektrolysehal/productmagazijn, expeditie | laadplek | — | [D1][D3] | **onzeker** (de keten is bevestigd, de plek niet — §5) |
| 2 | — | interne weg over het 冶金大道 15-complex | passage | — | [D3] | aannemelijk |
| 3 | ~1–2 | **Losplek walsdraadfabriek 江西铜业铜材有限公司** | losplek (eind fase D) | — | [D1][D3] | bevestigd (fabriek + adres), coördinaat open → §5 |

**Opmerkingen been 5.** De fabriek bestaat sinds 2002-03-22 en de collocatie met de
smelter staat op twee onafhankelijke registraties (JCC-zetel én 铜材-vestiging beide
冶金大道 15) [D3]; de productrelatie ("贵冶牌"-kathode als hoofdgrondstof) staat in [D1].
Wat níet gedocumenteerd is: de exacte hallen en het voertuig van de overbrenging.
**Geen enkel punt van dit been is satelliet-gelegd — het been wordt nog niet getekend** (§5, §7).

**Negatieve ankers been 5:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| 贵溪北站 | 28.34611, 117.18917 | 2 km | wat via 贵溪北 het spoor op gaat is de **markt-vertakking** en het bijproduct [C7][D6], niet de streng naar de eigen walsdraadfabriek |
| 鹰潭 (stadscentroïde, incl. hightech-zone) | 28.26000, 117.07000 | 5 km | de walsdraadfabriek staat op het 冶金大道-complex in **Guixi**; verwarring met JCC's dráádfabriek 江铜华东电工 in de 鹰潭高新区 ligt voor de hand [D8] — dat is een vertakking (§4), niet dit been |

## Verwerkingsknoop · 江西铜业铜材有限公司 (walsdraad + draad, Guixi)

*Hier hoort de vraag: wat komt er nog NA dit product? Zolang het antwoord "nog een
bewerking elders" is, gaat de brief door — zie fase E.*

| | |
|---|---|
| **anker-id** | — (nog geen; voorstel `cu-guixi-walsdraad` zodra satelliet-gelegd → §6) |
| **eigenaar van dit anker** | deze brief |
| **in** | kathode "贵冶牌" (hoofdgrondstof, van de smelter hiernaast) + "江铜牌"-tin [D1] |
| **andere ingaande strengen** | geen gedocumenteerd |
| **uit** | **370 kt/j** walsdraad Φ8 mm (电工用铜线坯) + **120 kt/j** getrokken ronde draad Φ2,0–3,6 mm [D1] |
| **uitgaande strengen** | fase E: afzetmarkt Shanghai / Jiangsu / Anhui / Shandong / Zhejiang [D1] (marktwaaier = stoppunt) · vertakking: JCC-draadketen 鹰潭高新区 (华东电工, elektromagnetische draad — aandeel onbekend, §4) |
| **verlies / bijproduct** | walsschroot gaat terug de smelter in (aanname, niet gesourcet) |

---

# FASE E · walsdraad → markt

## Been 6 · weg/spoor — walsdraadfabriek → afnemers Oost-China (STOPPUNT)

**been-id:** `koper-escondida-guixi-b6`
**Modaliteit:** weg en/of spoor — de fabriek adverteert "铁路、公路交通便利" (spoor én weg ontsloten) [D1]; de split is niet gedocumenteerd → §5
**Lengte:** — (marktwaaier, geen enkelvoudige bestemming)
**Stippel:** wordt **niet getekend** — een marktwaaier zonder gedocumenteerde losplek levert geen been op
**Direct of via een hub?** Dit is stukgoed over land, geen zeelijndienst — de transshipment-vraag speelt niet; wél is het laadstation (fabriek-expeditie? 贵溪站? 贵溪北站?) onbekend → §5, en "onbekend" betekent hier: **geen rechte lijn tekenen**
**Routeerpunt kop / staart:** nog te bepalen

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | expeditie walsdraadfabriek (coils Φ8 mm / draad op haspels) | laadplek | — | [D1] | bevestigd (fabriek), coördinaat open → §5 |
| 2 | — | afzetmarkt: Shanghai, Jiangsu, Anhui, Shandong, Zhejiang — draad- en kabelfabrikanten, géén gedocumenteerde individuele fabriek | losplek (keten-eind, **markt — GEEN anker**) | — | [D1] | stoppunt beargumenteerd |

**Waar de keten eindigt, en waarom daar.** De keten eindigt bij de expeditie van de
walsdraadfabriek. Een deel van het eindproduct ontstaat al óp deze plek: 120 kt/j wordt
ter plaatse doorgetrokken tot ronde draad Φ2,0–3,6 mm [D1]. De rest (walsdraad Φ8 mm)
waaiert uit over draad- en kabelfabrikanten in Oost-China; [D1] noemt de afzetmarkten
(Shanghai/Jiangsu/Anhui/Shandong/Zhejiang) maar **geen enkele individuele afnemer met
naam en adres**. Gezocht (2026-07-29, web): een gedocumenteerde kabelfabriek-afnemer van
江西铜业铜材-walsdraad — niet gevonden; wat wél bestaat zijn JCC-**eigen** vervolgstappen
elders (华东电工 鹰潭高新区: elektromagnetische draad, 100 kt/j gepland waarvan fase 1
50 kt [D7][D8]; en de 22万吨-walsdraadlijn in 上饶经开区 [D10]), maar zonder gedocumenteerd
aandeel uit déze fabriek — dat zijn vertakkingen in §4, geen strengvervolg. Conform de
fase-E-regel van het sjabloon is dit het **beargumenteerde stoppunt**: een markt-centroïde
is expliciet géén anker en wordt niet getekend.

**Negatieve ankers been 6:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| Yangshan-containerhaven (Shanghai) | 30.61700, 122.06700 | 20 km | er is geen gedocumenteerde export van dit walsdraad; de afzet is **binnenlands** [D1] — een zee-exportbeen tekenen is fout, en de productvorm (coils, binnenlandse levering) hoort niet bij een deepsea-containerhaven op eilanden voor de kust |

---

## 4 · Samenvloeiingen en vertakkingen (overzicht)

| # | been/knoop | soort | met welke stroom | wat gedeeld/afgesplitst wordt | aandeel | status |
|---|---|---|---|---|---|---|
| 1 | knoop 贵冶 (na b4) | samenvloeiing | binnenlands erts Dexing/Yongping over de 皖赣 [C5][C7] | de smelter-knoop zelf; corridor niet in deze brief uitgeschreven | — | geen eigen brief |
| 2 | knoop 贵冶 (na b4) | **vertakking** | kathode per spoor via 贵溪北站 → markt/SHFE-entrepots [C7][D5] | het grootste deel van de kathode | **~2/3 (schatting: 1,10 mln t capaciteit − 0,37 mln t eigen walsdraad)** — hard maken → §5 | geen eigen brief (kandidaat `koper-guixi-markt`) |
| 3 | knoop 贵冶 (na b4) | vertakking | kathode → JCC 22万吨-walsdraadlijn, 上饶经开区 (gepland in bedrijf eind 2022) [D10] | deel kathode oostwaarts over de 沪昆-corridor | onbekend → §5 | geen eigen brief |
| 4 | knoop walsdraad (na b5) | vertakking | JCC-draadketen: 江铜华东电工新材料, 鹰潭高新区 — elektromagnetische draad voor nieuwe energie, 100 kt/j gepland (fase 1: 50 kt) [D7][D8] | deel walsdraad/koper naar de draadtak | onbekend → §5 | geen eigen brief |
| 5 | knoop 贵冶 (na b4) | bijproduct | zwavelzuur + slak via 贵溪北站, o.a. blocktrein 贵溪北 → 分宜 [C7][D6] | bijproduct, geen koperstreng | — | valt buiten de koper-atlas |

**Regel:** één brief = één streng. Deze brief volgt de kathode naar de **eigen
walsdraadfabriek**; de markt-vertakking (rij 2) is substantieel en verdient te zijner tijd
een eigen stroom-id + brief — de puntenlijst wordt hier niet herhaald.

## 5 · Openstaande punten

| # | been | wat | waarom onzeker | wat het zou oplossen |
|---|---|---|---|---|
| 1 | b2→b3 | **北仑港站-laadspoor** (vertrek-anker overslag Beilun) heeft geen coördinaat | het tweede anker van de overslag is verplicht (werkwijze §2b), maar de plek is niet uit bronnen bekend — er wordt géén coördinaat verzonnen | z16-satellietpass over het havenemplacement + [C1] |
| 2 | b3 | passage-/stationscoördinaten corridor A & B niet ingevuld | de toets draait op het net en is geslaagd; puntcoördinaten waren nooit ingevuld | lage prioriteit; z13-pass per station |
| 3 | b3/b4 | 贵溪站-coördinaat (28.29308, 117.20972) is een zh.wiki-waarde, en het góederenemplacement kan iets verschoven liggen | één bron; nieuw uit research 2026-07-29 | z16-satellietpass (Esri) op het emplacement |
| 4 | b4/b5 | 贵溪北站-coördinaat (28.34611, 117.18917) idem | één bron (zh.wiki) | z16-satellietpass |
| 5 | b5 | **kathode-laadplek** op het 贵冶-terrein: geen coördinaat | geen bron wijst de expeditiehal aan | z16/z18-satellietpass over het complex (magazijn aan de elektrolysezijde zoeken) |
| 6 | b5 | **losplek walsdraadfabriek** 江西铜业铜材有限公司: adres bekend (冶金大道 15), coördinaat niet | fabriek en productrelatie zijn gedocumenteerd [D1][D3], de hal niet | z16/z18-satellietpass; daarna anker-id `cu-guixi-walsdraad` aanmaken (§6) |
| 7 | b5 | modaliteit interne overbrenging (aanname: intern wegtransport) | zelfde complexadres maakt het aannemelijk; geen bron beschrijft het voertuig/de route | bedrijfsbron of satellietbeeld (kathodetrucks/laadperron) |
| 8 | b6 | modaliteitssplit weg/spoor + het laadstation van de uitgaande coils | [D1] zegt alleen "spoor én weg ontsloten" | vrachtdocumentatie of spoorwegbron; tot die tijd wordt been 6 niet getekend |
| 9 | §4 | aandeel-schatting markt-vertakking (~2/3) en aandelen 上饶/鹰潭 | afgeleid uit capaciteitscijfers, niet uit een verladingsstatistiek | JCC-jaarverslag-segmentatie [D2] of spoorstatistiek 贵溪北 |
| 10 | b5/b6 | **geen enkel fase D/E-anker is satelliet-gelegd** — nieuwe ankers uit deze research staan hoogstens op "bevestigd"/"aannemelijk" | de satellietpass (Esri z16, 0,01°-grid) moet nog gebeuren, conform werkwijze §2 | de pass draaien; pas daarna tekenen |

## 6 · Conflicten met de projectdata (afwerklijst)

| # | wat | nu | hoort te zijn | bron |
|---|---|---|---|---|
| 1 | `cu-escondida-laad` | -24.27004, -69.07169 (ín de put) | **-24.26200, -69.06000** (concentrator + indikkers = kop van de leiding) | satelliet z16 |
| 2 | `cu-coloso-kade` | -23.76015, -70.46332 (kustweg bij het dorp) | **-23.75690, -70.46520** (kop laadsteiger); filterfabriek -23.75900, -70.46700 | satelliet z17 |
| 3 | `cu-beilun-kade` | 29.92742, 121.87573 (waar de transportband aan land komt; in de oude tabel als lon/lat genoteerd) | **29.93640, 121.88300** (losberth met ertslossers); het bandpunt blijft als begin van de last mile | satelliet z16 |
| 4 | flow `cu-escondida → cu-ref-jiangxi`, `via: [cu-port-antofagasta, cu-port-ningbo]` | via de haven Antofagasta | via **Coloso** (Escondida's eigen terminal, 12 km zuidelijker) | [E3] |
| 5 | ~~spoorbeen Beilun→Guixi~~ | ~~gemeten 883 km~~ | **VERVALLEN** — hermeten op 550,5 km over corridor B, toets §4 geslaagd | meting 2026-07-28 |
| 6 | leiding-been Escondida→Coloso | ontbreekt / recht | **gestippeld mét reden** (~170 km, eigen verbinding, geen OSM-tracé) | [E1] + werkwijze §7 |
| 7 | `aansluitingen.json` mist fase D-ankers | keten stopt bij `cu-guixi-spoor` (ertskant) | nieuwe aansluitingen **`cu-guixi-kathode-laad`** (expeditie smelter) en **`cu-guixi-walsdraad`** (铜材-fabriek) — pas aanmaken ná de satellietpass (§5) | [D1][D3] |
| 8 | `data/copper.js` heeft geen uitgaand been vanaf Guixi | keten eindigt op de smelter | fase D (been 5) toevoegen zodra de ankers satelliet-gelegd zijn; de markt-vertakking pas bij een eigen brief | deze brief |

> **✅ 1, 2 en 3 zijn DOORGEVOERD** (2026-07-28, na goedkeuring van Lars): de
> coördinaten staan in `v2/tools/maak_aansluitingen.py` (de redactionele lijst =
> bron van waarheid) en in het daaruit gegenereerde `v2/data/aansluitingen.json`,
> mét de verplaatsing en de reden in de `noot`. Gemeten neveneffect bij Beilun:
> de zee-snap verbetert (2,4 → 1,3 km) en de spoor-snap verslechtert (0,2 →
> 1,3 km) — de berth ligt in het water, het havenspoor eindigt bij het ertsveld.
> Eén punt kan niet allebei zijn; als dat gaat knellen hoort er een tweede
> aansluiting te komen (§3.4), geen compromis-coördinaat.
> **4 en 6 staan nog open; 7 en 8 zijn nieuw (fase D/E, 2026-07-29).**

## 7 · Wat de kaart moet tekenen

1. **Been 1 — leidingbeen** (stippel, amber): concentrator -24.26200, -69.06000 →
   Coloso-filterfabriek -23.75900, -70.46700. Label: *slurryleiding ~170 km — eigen
   verbinding, geen net.*
2. **Been 2 — zeebeen** (zeeschip): kop laadsteiger Coloso → Beilun-losberth. Router vrij;
   de Antofagasta-via eruit (conflict 4).
3. **Been 3 — spoorbeen**: Beilun-ertsterminal → 贵溪站. **Corridor B** — dat is wat het
   net al rijdt (550,5 km, gemeten) en het klopt met de brief; corridor A blijft in deze
   brief staan als de historische variant en als toetsmateriaal.
4. **Been 4 — last mile** (stippel, kort): 贵溪站 → ertslosbundel 28.32710, 117.22600.
5. **Been 5 — kathode naar de walsdraadfabriek**: **nog niet tekenen** — geen van de
   fase D-ankers is satelliet-gelegd (§5). Zodra dat gebeurd is: kort stippelbeen op het
   complex (eigen terrein, geen net), met de walsdraadfabriek als nieuw keten-eind.
6. **Been 6 — marktwaaier**: **niet tekenen** — beargumenteerd stoppunt, geen anker.
7. **Niet tekenen:** de tak Escondida → Chuquicamata (aparte flow) · de markt-vertakking
   van de kathode via 贵溪北站 (krijgt t.z.t. een eigen brief, §4). *De oude regel "het
   uitgaande product uit Guixi (andere keten) niet tekenen" is hiermee vervangen: fase D
   hoort sinds de werkwijze-uitbreiding van 2026-07-28 (§1a) bij déze brief, maar wordt
   pas getekend ná de satellietpass.*

## 8 · Toets-checklist

- [x] **Notatie:** alle coördinaten lat, lon met decimale punt; ankers op 5 decimalen
      *(lon/lat-regels uit de oude versie gecorrigeerd: het Beilun-bandpunt in §6 en het
      Guixi-eindpunt in §7 stonden als lon/lat)*
- [x] Elk been heeft een **been-id** (`b1`–`b6`); ankers dragen waar mogelijk het `aansluitingen.json`-id
- [ ] Elke laadplek, overslag en losplek **satelliet-gelegd** — geldt voor fase A–C
      (concentrator z16 · Coloso z17 ×3 · Beilun z16 · losbundel z18); **fase D/E nog niet** → §5.10
- [x] Elke laad-/los-/overslagplek heeft een ingevulde **productvraag** (§2a, ladders L1–L6)
      incl. uitsluitingen — stap 5/6 van L5/L6 staan open → §5
- [ ] Elke overslag heeft **twee** ankers + terreinstappen — Coloso ✅; Beilun: vertrek-anker
      北仑港站 zonder coördinaat → §5.1
- [x] **Routeerpunt + max snap** genoteerd bij elk been-uiteinde op water en spoor (b2, b3);
      b5/b6 "nog te bepalen"
- [x] **Dekking:** been 3 gemeten — alle corridor-B-punten geraakt binnen 0,8–6,4 km (marge
      per punt 8 km, zie been-kop); fase D/E niet gerouteerd (wordt niet getekend)
- [x] **Verklikker:** been 3 raakt geen plaats die niet in de brief staat (corridor-A-punten
      gemeden: Hangzhou 87,4 km · Shaoxing 56,5 · Yuyao 45,9 · Zhuji 31,2)
- [x] Geen enkel **negatief anker** binnen zijn verbodsstraal geraakt (Yingtan 14,6 km ·
      Jingdezhen 98,5 · Nanchang 136,4) ✅
- [x] Lengte per been binnen tolerantie mét gereedschap + eindpunten + netstadium: been 3 =
      550,5 km (`toets_spoorroute.mjs`, Beilun-ertsterminal ↔ 贵溪, net 2026-07-28) tegen
      ~556 brief-corridor = −1,0%; been 1 alleen bronlengte (~170 km, geen geometrie)
- [ ] Volumes sluiten over de knopen — plausibel (1,10 mln t kathode ≥ 0,37 mln t eigen
      walsdraad + ~2/3 markt; ~3 mln t spoorafvoer incl. bijproduct) maar aandelen niet hard → §5.9
- [x] Elke stippellijn draagt een **reden** (b1 eigen verbinding · Coloso-aanloop geen AIS ·
      b4 OSM-gat hand-geplaatst · b5 eigen terrein)
- [x] De keten loopt door tot het eindproduct **of het stoppunt is beargumenteerd** — fase E:
      marktwaaier zonder gedocumenteerde individuele afnemer, onderbouwd met wat er wél en
      niet gevonden is (been 6)

## 9 · Bronnen

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
C6 zh.wikipedia *贵溪站* (aansluitsporen naar o.a. 江铜贵溪冶炼厂) · C7 Xinhua 2024-06-02,
*皖赣铁路全线开通运营40周年* (news.cn): 贵溪冶炼厂 sluit per 专用铁路 bij 贵溪北站 aan op de
皖赣; uitgaand elektrolytkoper/zwavelzuur/slak ~3 mln t/jaar sinds 2013 — *(de eerdere
naamloze C7-bron, nu met vindplaats)* · C8 *宁波－舟山港总体规划 2014-2030* (ertsligplaatsen
bedienen de metallurgie van de Yangtze-delta).

**Afnemer/smelter [J..]:** J1 Jiangxi Copper / Guixi Smelter — grootste kopersmelter ter
wereld, feedstock grotendeels ingevoerd concentraat (Peru, Chili, Afrika) · J2 Sina Finance
2025-12-31, *2025年全球铜冶炼行业竞争格局* — 贵溪冶炼厂 capaciteit 110万吨/jaar, hoogste
ter wereld · J3 铜陵市工业和信息化局, *绿色冶炼的行业标杆 贵冶* (gxj.tl.gov.cn) —
dagproductie ~1/8 van het Chinese totaal; eerste smelter met 百万吨-capaciteit.

**Fase D/E — walsdraad & vervolg [D..] (research 2026-07-29):** D1 SMM,
*江铜集团：江山万里 铜路而行* (news.smm.cn/news/101407667) — 江西铜业铜材有限公司:
"以'贵冶牌'阴极铜和'江铜牌'锡锭为主原料"; 370 kt/j Φ8 mm 电工用铜线坯 + 120 kt/j
Φ2,0–3,6 mm 电工用圆铜线; afzet Shanghai/Jiangsu/Anhui/Shandong/Zhejiang; "铁路、公路交通
便利" · D2 JCC-jaarverslagen 2024/2025 (cninfo/SSE) — tien 铜材-verwerkingsfabrieken
waaronder 江西铜业铜材有限公司 en 广州江铜铜材有限公司; productieplan 2025: 2,01 mln t
koperverwerkingsmateriaal · D3 bedrijfsregister/10jqka — JCC-zetel én 铜材-vestiging
Guixi beide **江西省贵溪市冶金大道15号**; 铜材公司 opgericht 2002-03-22 · D4 zh.wikipedia
*贵溪站* — 28°17′35″N 117°12′35″E (28.29308, 117.20972); 沪昆 + 皖赣; beheert 贵溪北站 ·
D5 zh.wikipedia *贵溪北站* — 28°20′46″N 117°11′21″E (28.34611, 117.18917); 皖赣;
goederenstation (1985), alleen 专用线-werk; buurstations 中村 7 km / 贵溪 9 km · D6
中国硫酸网 (liusuan.org) — eerste 公转铁-zwavelzuur-blocktrein 贵溪北 → 分宜, 2026-04-12,
12 tankwagons / 780 t · D7 STCN/Sina Finance, jan 2023 — oprichting 江西江铜华东电工新材料
科技有限公司 (JCC + 鹰潭炬能, kapitaal ¥400 mln) · D8 Sina/aanbestedingsplatforms
(jxgqcg.com, JXTZ2023-nrs.) — 华东电工: 100 kt/j (fase 1: 50 kt) elektromagnetische draad
voor nieuwe energie, productiebasis 鹰潭高新区 · D9 中新网江西 + 大江网 — Yingtan
"世界铜都": 86 koperbedrijven boven schaalgrens, 1,0 mln t smelt- + 1,4 mln t
verwerkingscapaciteit; 鹰潭国际陆港 (import-klaring ter plaatse) · D10 shushangyun-overzicht
van de ¥12,8 mld JCC-investering — 220 kt/j walsdraad **上饶经开区** (gepland in bedrijf
eind 2022) + 100 kt/j lithium-batterijkoperfolie + 30 kt/j gietmateriaal · D11 中国有色金属
加工工业协会 (cnfa.net.cn) — bezoekverslag verwerkingscluster 贵溪/鹰潭: o.a. 中易微连
(Guixi, elektromagnetische draad 60 kt), 云泰铜业 (Guixi), 江冶实业 (鹰潭), 鑫铂瑞 (鹰潭,
kopfolie 40 kt), 广信新材料 — context van de regionale kathode-afzet.

**Eigen metingen:** satelliet-overlay Esri World Imagery z15–z18 (2026-07-28) ·
`toets_spoorroute.mjs` (550,5 km, netstadium 2026-07-28) · `toets_corridor.py` ·
atlas-ketenmeting `?v=099` (zee 19.104 km).
