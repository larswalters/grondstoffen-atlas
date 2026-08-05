# Routebrief · koper — Escondida → walsdraad Guixi (China)

**stroom-id:** `koper-escondida-guixi`  ·  **geschreven:** 2026-07-28, herschreven naar het mijn-tot-eindproduct-sjabloon + fasen D/E toegevoegd 2026-07-29, **fase-D-ronde uitgevoerd 2026-08-05**  ·  **status brief:** fase A–C in toets geslaagd (spoortoets 2026-07-28) · **fase D GETEKEND als terreinanker-been** (besluit Lars 2026-08-05) · fase E blijft het beargumenteerde stoppunt
**Keten in één zin:** sulfide-concentraat uit Escondida, als slurry per **eigen leiding** (~170 km) naar Puerto Coloso, daar gefilterd en per **bulkcarrier** naar de Beilun-ertsterminal (Ningbo-Zhoushan), over de band naar het laadspoor van 北仑港站 en per **spoor** (corridor B, gebakken been **565,8 km**) naar 贵溪站 en over het aansluitspoor de ertslosbundel van 's werelds grootste kopersmelter op; de **kathode** gaat vervolgens over de interne hoofdas 闪速大道 (**0,7 km, getekend**) naar de **walsdraadfabriek** van 江西铜业铜材有限公司 (walsdraad Φ8 mm + getrokken draad), waarna het product als marktwaaier naar Oost-China vertrekt — het beargumenteerde stoppunt.

---

> [!important] BIJGEWERKT 2026-08-05 — FASE D STAAT OP DE BOL, EN DE OVERSLAG BEILUN IS GESPLITST
>
> **Wat de kaart nu tekent: 9 benen · 19.826,6 km · 3.233 punten · 6 markers** (was 5 benen /
> 19.823,1 km / 4 markers). Lengtes in reisvolgorde: leiding **153,5** (stippel) · leiding
> **0,3** (stippel) · zee **85,1** (stippel) · zee **19.018,4** · zee **1,3** (stippel,
> haven-aanloop Beilun) · leiding **1,2** (stippel, transportband) · leiding **0,3** (stippel,
> ertsveld → laadspoor) · spoor **565,8** · truck **0,7** (fase D).
>
> **⚠️ BEEN 5 HEEFT EEN SUBSTITUUT-KOP, EN DAT IS GEEN DETAIL.** De lijn loopt van het
> **registerpunt van de smelter** (28.33227, 117.22545) naar het **registerpunt van de
> walsdraadfabriek** (28.33180, 117.21919) — dus van *verwerkingsknoop* naar *aansluitpunt*,
> niet van laadplek naar losplek. De **kathode-expeditie is niet gevonden** (§5.5) en krijgt
> geen coördinaat. Wie de kop leest als "hier vertrekt de kathode" leest hem fout.
> **Het gat van 0,584 km tussen been 8 en been 9 ÍS die ontbrekende laadplek** — het is bewust
> zichtbaar en wordt niet dichtgetrokken met een rechte lijn (dat is de klasse die dit project
> bij Waalhaven, Nacala en New Orleans al drie keer heeft betaald).
> ⚠️ Dat gat is **0,584 km en niet de 0,541 die vooraf geschat werd**: die schatting mat tot de
> projectie op de as, terwijl de getekende lijn op het **anker zelf** begint — 43 m verder.
>
> **Been 5 is DOORGETROKKEN, niet gestippeld**, en dat is gemeten: het OSM-net reikt hier tot
> op **8 m** van het staart-anker en **43 m** van het kop-anker. Een stippel betekent in dit
> project precies één ding — *hier reikt het net niet* (werkwijze §7) — en zou hier dus liegen.
>
> **⚠️ DE SCHERPSTE VONDST VAN DE RONDE: `maak_stroombeen_weg.py` KON DIT BEEN NIET LEGGEN.**
> Die tool routeert over een graaf waarvan de knopen de OSM-way-vertices zijn, en
> `way/1462532976` heeft maar **5 vertices over 2.250 m**. De dichtstbijzijnde knoop bij de
> walsdraadfabriek ligt **179 m ten westen** ervan. Uitkomst van de eerste bake: kop-anker →
> projectie (43 m) → **792 m westwaarts, voorbij de fabriek** → **179 m terug oostwaarts** naar
> het anker = **1,01 km**, lengtetoets **+29,0%**. Dat is **overschiet-en-terug op het EINDpunt
> van een been** — dezelfde klasse die op 2026-08-05 bij de grafiet-via-punten is benoemd, maar
> daar op doorgaande punten. Het is geen werkelijkheid (geen truck rijdt langs de poort heen om
> te keren) maar de **korrel van onze eigen graaf**.
> Opgelost met nieuw gereedschap **`v2/tools/knip_osm_been.py`**: één way, twee ankers, géén
> routering — beide ankers loodrecht op de polylijn projecteren en het stuk ertussen eruit
> knippen. De geometrie komt dus nog steeds **uit OSM en niet uit een oog** (dat onderscheid is
> de Tongling-regel). Het tool rapporteert zelf **pad ÷ hemelsbreed** (hier **1,08**), zodat een
> overschiet-en-terug niet meer stil kan passeren.
>
> **De overslag Beilun heeft eindelijk twee ankers** (werkwijze §2b) en het gat van **2.379 m
> is 198 m geworden**. Nieuw: `cu-beilun-laadspoor` **29.92653, 121.87308** (北仑港站,
> satelliet-gelegd z19). `cu-beilun-kade` is **zee-only** geworden. De resterende 198 m is géén
> restfout maar precies *anker ≠ routeerpunt*: het spoorbeen begint 198 m noord van de laadplek
> en dat snappunt is **exact het beginpunt van het gebakken spoorbeen**.
> ⚠️ De formulering "het gat is exact de som van twee snaps" uit een eerdere analyse is **fout**
> en staat hier bewust niet: de hoek tussen de twee snaps is 138,8°, niet 180°.
>
> **Gaten tussen de negen benen:** `0 · 0 · 0 · 0 · 0 · 0 · 0,198 · 0,584 km` — alle onder de
> 0,5 km-eis met precies **één benoemde uitzondering**, het procesgat bij 贵冶. Een tweede
> uitzondering zou een fout zijn. **Alle zes markers liggen ≤ 1 m van de lijn** (punt-tot-segment
> gemeten, niet punt-tot-vertex — die twee mengen was een echte meetfout van de vorige ronde).
>
> **`aansluitingen.json` 25 → 27**, en geen enkele bestaande plek is verschoven (0,0 m).
> `cu-guixi-walsdraad` krijgt **geen enkele modus**: een weg-snap zou **341,1 km** zijn (het
> landnet heeft wereldwijd 1.883 wegknopen) — gemeten, niet aangenomen.
>
> **`toets_knikken.py` 157 → 159 knikken; omkeringen 25 (ongewijzigd), terugloop 3
> (ongewijzigd)**, en de vier andere stromen zijn in de diff **letterlijk ongewijzigd**. De twee
> nieuwe knikken zitten allebei in het fase-D-been — 89,9° op `28.33188, 117.22545` en 89,9° op
> `28.33187, 117.21919` — en dat zijn de twee haakse aansluitingen van de inritten op de
> hoofdas. Geen artefact.
>
> **Adrescorrectie: 冶金大道 15号 → 19号.** Het nationale emissievergunningregister geeft voor
> **beide** Guixi-vennootschappen 19号 in het veld `生产经营场所地址`; 15号 is het
> hoofdkantoor-/administratieve adres van de groep, de beursvennootschap én de 加工事业部. De
> collocatie-conclusie van deze brief klopt dus, maar de onderbouwing via nummer 15 was fout.
>
> **Fase E blijft niet getekend, en de onderbouwing is sterker geworden.** Het gevonden
> CSRC-toezichtstuk documenteert een **kathode**-relatie, geen walsdraad-afzet, en de tegenpartij
> is 江铜华东（浙江）铜材有限公司 in 诸暨/Zhejiang op **508,2 km** — niet 上饶. Dat is een
> **vertakking bij de smelterknoop** (§4), geen fase-E-been.

---

*Volgens `../routebrief-werkwijze.md`. Oorspronkelijk de derde routebrief en de eerste volgens het aangescherpte formaat van 2026-07-28 (kop en staart satelliet-gelegd op z16/z17 vóórdat ze anker werden, de last mile als eigen been, en waar het net niet reikt een stippellijn mét reden); nu doorgetrokken tot het eindproduct conform werkwijze §1a en per 2026-08-05 t/m fase D getekend.*

*Toets-doel: dit is de stroom die LAR-527 "de zware" noemt — het China-spoorbeen heeft het
grootste risico op een verkeerde corridor.*

*Notatie (hard): coördinaten altijd **lat, lon** met **decimale punt**; ankers 5 decimalen, passages 2–4. Elk been draagt een been-id `koper-escondida-guixi-b<n>`; ankers dragen waar mogelijk het id uit `aansluitingen.json`.*

> **✅ UITSLAG (corridortoets 2026-07-28): het spoorbeen KLOPT.** De tweezijdige toets van
> werkwijze §4 slaagt volledig: de lijn raakt élk brief-punt van **corridor B** — Ningbo,
> Yunlong, Fenghua, Shengzhou, Dongyang, Yiwu, Jinhua, Longyou, Quzhou, Jiangshan, Yushan,
> Shangrao, Hengfeng, Yiyang, Guixi — binnen 0,8–6,4 km, mijdt alle punten die alléén op
> corridor A liggen (**Hangzhou 87,4 km** ernaast, Shaoxing 56,5, Yuyao 45,9, Zhuji 31,2) en
> raakt géén van de drie negatieve ankers (Yingtan 14,6 km, Jingdezhen 98,5, Nanchang 136,4).
> De router rijdt dus over de **Yong-Jin-vrachtlijn**, precies zoals de brief voorspelde.
>
> ⚠️ **Het GETAL uit die ronde is achterhaald, het OORDEEL niet.** De 550,5 km kwam uit
> `toets_spoorroute.mjs` — het **meetgereedschap** — op het netstadium van 2026-07-28. Het
> **gebakken** been op de bol meet **565,8 km** (netstadium 2026-07-29, OSM-spoor 1-op-1).
> Tegen de brief-corridor van ~556 km is dat **+1,8%**, niet de −1,0% die hier eerder stond.
> Meet het eindproduct, niet je meetlat — de attributie van het verschil staat bij been 3.
>
> ⚠️ **Correctie op een nog eerdere versie van deze brief.** Die stelde dat de atlas dit been op
> **883 km** mat en dat de lijn daarom op een andere corridor lag. Dat getal komt uit de
> heal-ronde van 2026-07-24 en is **niet** met dit gereedschap tussen deze twee kades
> gemeten; met beide ankersets (oud én satelliet-gelegd) snapt de route op dezelfde
> hoofdnet-knoop. De 883 km hoort bij een andere meting op een ouder netstadium — er was hier
> dus geen corridor-fout.

---

## 1 · Ketenkaart

```
Escondida-concentrator ──(b1 slurryleiding, stippel 153,5 km getekend / ~170 km werkelijk)──►
  cu-escondida-laad      ──(b1' terreinverwerking Coloso, stippel 0,3)──► Puerto Coloso (filter + steiger)
                                                                          cu-coloso-kade
                       ──(b2a haven-aanloop Coloso, stippel 85,1)──►
                       ──(b2 zee, gemeten 19.018,4 km)──►
                       ──(b2b haven-aanloop Beilun, stippel 1,3)──► Beilun-ertsterminal (losberth)
                                                                     cu-beilun-kade   ZEE-ONLY
     OVERSLAG BEILUN, drie zichtbare stappen (werkwijze §2b — twee ankers):
                       ──(o1 transportband losberth → landpunt/ertsveld, stippel 1,2)──►
                                                          cu-beilun-bandlandpunt (terreinstap)
                       ──(o2 ertsveld → laadspoor, stippel 0,3)──► 北仑港站 laadspoor
                                                                   cu-beilun-laadspoor  SPOOR
                       ──(b3 spoor, gebakken 565,8 km, corridor B)──► 贵溪站 (goederenemplacement)
                       ──(b4 last mile aansluitspoor)──► ertslosbundel 贵溪冶炼厂
                                                          cu-guixi-spoor
  ◄── samenvloeiing knoop 贵冶: binnenlands erts Dexing/Yongping komt binnen over de 皖赣 (贵溪北站)
     ⚠️ PROCESGAT 0,584 km — hier hoort de kathode-expeditie; niet gevonden, niet verzonnen (§5.5)
                       ──(b5 truck over 闪速大道 / 物流主轴线, 0,7 km, DOORGETROKKEN)──► walsdraadfabriek
                          kop = registerpunt smelter (SUBSTITUUT)      江西铜业铜材有限公司, 冶金大道 19号
                                                                       cu-guixi-walsdraad
                       ──(b6 weg/spoor, NIET GETEKEND)──► afnemers Oost-China (STOPPUNT: marktwaaier)
  ├── vertakking na knoop 贵冶: ~2/3 kathode per spoor via 贵溪北站 → markt/SHFE (geen eigen brief)
  ├── vertakking na knoop 贵冶: kathode → 22万吨-walsdraadlijn 上饶经开区 (aandeel onbekend)
  ├── vertakking na knoop walsdraad: → 江铜华东电工 (鹰潭高新区, elektromagnetische draad, aandeel onbekend)
  └── bijproduct via 贵溪北站: zwavelzuur (o.a. blocktrein → 分宜) + slak — geen koperstreng
```

| | |
|---|---|
| **Fasen** | A leiding mijn → zeeterminal · B zee · C aanlanding → smelter (incl. last mile) · D kathode → walsdraadfabriek · E walsdraad → markt |
| **Benen** | 6 verhalende benen (`koper-escondida-guixi-b1` … `b6`); op de bol staan daarvan **9 getekende benen** — b1 en b2 vallen uiteen in hun stippel-deelstukken en de overslag Beilun draagt twee eigen terreinbenen. ⚠️ Been-ids ontbreken nog in het gebakken bestand → §5 |
| **Overslagen** | 2 volwaardige drager-wissels (Coloso: leiding→zee · Beilun: zee→spoor), elk met terreinstappen. **Beilun heeft sinds 2026-08-05 zijn twee ankers**: `cu-beilun-kade` (losberth, zee-only) en `cu-beilun-laadspoor` (北仑港站, spoor), met `cu-beilun-bandlandpunt` als terreinstap ertussen |
| **Gedeelde benen** | geen — geen andere brief deelt een been; het traject 义乌→贵溪 is binnen déze brief gedeeld materiaal van corridor A en B |
| **Vertakkingen** | na been 4 (knoop 贵冶): kathode naar markt/SHFE per spoor via 贵溪北站 (~2/3, schatting) · naar 上饶经开区 · **kathode → 江铜华东（浙江）铜材有限公司 in 诸暨/Zhejiang, 508,2 km** (gedocumenteerd in een CSRC-toezichtstuk) · na been 5: naar 鹰潭高新区 — zie §4 |
| **Reële alternatieven** | fase A–C: geen gedocumenteerd — de import voor Guixi landt aan bij Beilun [C8][J1]; er is geen bron voor een Zhangjiagang/Jiangyin-lightering op déze streng (die klasse hoort bij de Yangtze-smelters, zie `koper-collahuasi-tongling`). **Fase D: 江西铜业集团铜材有限公司** (28.32956, 117.23688) — een ándere rechtspersoon met een eigen werk 1.749 m OZO op hetzelfde boulevardadres; aandeel onbekend → §4 |

## 2 · Productvormen per fase — wat beweegt er fysiek

| fase | product | vorm / verpakking | gehalte of specificatie | omzetting in de volgende stap | jaarvolume |
|---|---|---|---|---|---|
| A | sulfide-concentraat | slurry, ~65% vaste stof, in een 9-inch leiding; te Coloso gefilterd tot natte bulk [E1] | ~28–30% Cu | → smelten/converteren/elektrolyse | — (niet in deze brief gemeten) |
| B | zelfde concentraat | natte bulk in de ruimen van een bulkcarrier | idem | → lossen Beilun, band naar ertsveld | — |
| C | zelfde concentraat | bulk in open wagons — ⚠️ **OPEN CONFLICT**: het satelliet-gelegde laadspoor is een **container**emplacement (78万TEU) → §2a L3 | idem | → smelter Guixi | — |
| D | kathode, merk "贵冶牌" | bundels stukgoed (kathodeplaten), SHFE-/LME-klasse | Grade A, ≥99,99% Cu | → walsdraad Φ8 mm (continugieten + walsen) | capaciteit smelter 1,10 mln t/j [J2]; naar de eigen walsdraadfabriek ~0,37 mln t (afgeleid uit [D1]) |
| E | walsdraad + draad | coils walsdraad Φ8 mm (电工用铜线坯) · getrokken ronde draad Φ2,0–3,6 mm | elektrotechnische kwaliteit | → draad/kabel bij afnemers in Oost-China (eindgebruik) | 370 kt walsdraad + 120 kt draad [D1] — ⚠️ dat zijn kt **product**, niet kt Cu-inhoud; voor koper schelen die vrijwel niet (walsdraad is ≥99,9% Cu) maar `data/copper.js` rekent in `kt Cu/jaar (indicatief)`, dus de eenheid hoort erbij te staan |

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
| 5 | de losberth met de rode ertslossers, noordoostelijk van het ertsveld · en, aan de spoorzijde, de laadsporen van 北仑港站 |
| 6 | losberth **29.93640, 121.88300** — satelliet z16 (2026-07-28) · laadspoor **29.92653, 121.87308** — satelliet z19 (0,26 m/px, 2026-08-05): bundel van vijf parallelle sporen met **vier rode rail-mounted portaalkranen** en wagons eronder, 4,5 m van OSM `way/1491021972` |

**Uitsluit:** niet de containerkades ernaast (containers ≠ bulk); concentraat voor binnenland-smelters komt **niet** binnen op een containerhaven op eilanden voor de kust (de Yangshan-klasse); de berth is niet het laadspoor — de **band** verbindt water- en spoorzijde, dus één punt kan niet allebei zijn. *Die laatste uitsluiting is per 2026-08-05 uitgevoerd: er zijn nu twee ankers.*

> ⚠️ **OPEN CONFLICT — CONTAINERS OF BULK? Beslis dit vóór fase C herschreven wordt.**
> Wat op 北仑港站 satelliet-gelegd is, is een **container**emplacement: 78万TEU/jaar, 10,9 ha,
> 2 货场 / 10 装卸线, beheerd door 中铁联合国际集装箱宁波北仑 — containerwagons onder
> rail-mounted portaalkranen. Twee onafhankelijke passes zagen hetzelfde beeld. Stap 1 van deze
> ladder zegt **natte bulk in open wagons**, en dat is niet hetzelfde.
> Chinese bronnen die de containerlezing steunen: het 鹰潭国际陆港 meldt 海铁联运-班列 vanaf
> 宁波北仑 met o.a. **铜精矿** in de lading, en het eerste multimodale importgeval van Jiangxi
> (2026-06-29, 26 t 再生铜原料) ging 『原箱』 — in de originele container — via 贵溪北站.
> **Dit is een vraag aan de brief, niet aan de satelliet.** `cu-beilun-laadspoor` is daarmee
> **geografisch waterdicht en inhoudelijk voorwaardelijk**; die formulering staat ook in de
> `noot` van de aansluiting.
> De enige **bulk**-kandidaat op het beeld: twee bandgalerijen uit het bulkveld eindigen op
> `29.91820, 121.87075` en `29.91765, 121.87050`, pal aan de oostelijke sporen van de bundel —
> maar zonder wagons eronder, zonder laadsilo en zonder perron blijft dat **aannemelijk**, geen
> anker. Eén Wayback-opname mét gondola's eronder maakt er een anker van → §5.

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
| 5 | magazijn-/expeditiehal — **exacte plek nog steeds onbekend** → §5 |
| 6 | **OPEN, en dat blijft zo.** Wat er wél is: het **registerpunt van de smelter** 91360000X12430120H001P (铜冶炼, 冶金大道 19号) op **28.33227, 117.22545**, satelliet-gelegd op z18 midden in het pyro-hart (zwavelzuurtanks en bolvormige opslag NW, procesblokken met pijpenbruggen, stoompluim uit de vlamovenstraat, koeltorens en bezinkbekkens zuid). **Dát punt is de SUBSTITUUT-KOP van been 5 — een registerknoop, géén laadplek.** Reden dat de pass hier stukloopt: Esri heeft bij Guixi **geen z19** (z19 en z20 leveren exact 2.521 byte placeholder, per tegel nagemeten), en Wayback-release 64001 is identiek aan live — het is dus een **zoomplafond**, niet de opnamedatum-faalmodus |

**Uitsluit:** kathode gaat **niet** over de ertslosbundel of de transportband (bulkinfrastructuur); niet in tankwagons (dat is het zwavelzuur [D7]); en voor déze streng niet via 贵溪北站 — wat daar vertrekt is de markt-vertakking en het bijproduct [C7][D6]. **En het registerpunt is niet de expeditie**: een administratief vergunningpunt in het pyro-hart is geen plek waar kathodebundels de deur uit gaan.

> ⚠️ **Eén verleidelijke redenering is expliciet verworpen.** Een eerdere ronde stelde twee
> punten voor in de noordoosthoek van het terrein als "elektrolyse/tankhouse", op de redenering
> *anodeslijkverwerking staat altijd naast de tankhouse, dus dit ís de tankhouse*. Dat draait
> het bewijs om: dezelfde bron (赣环监字（2017）第S007号 p.11) zet dáár juist **一车间** — de
> anodeslijk-/edelmetaalwerkplaats (回转窑/湿法/金银电解, producten 粗金粉 · 海绵铂 · 海绵钯) —
> en zegt zelf dat het slijk vanuit het 电解车间 **naar** 一车间 wordt gebracht, wat afstand
> impliceert. De bron plaatst dus de **buurman**. Geen van die punten wordt anker.
> Wat er uit die ronde wél overeind blijft en de collocatie hard maakt: p.11 verdeelt het
> 198,26 ha-terrein intern in 老厂区 · 新厂区 · 新产业公司 · **铜材公司** · 新材料车间 ·
> 铜达公司.

**L6 · Walsdraadfabriek 江西铜业铜材有限公司 (losplek been 5 + laadplek been 6) — NIEUW, fase D/E**

| stap | antwoord |
|---|---|
| 1 | in: kathodebundels; uit: coils walsdraad Φ8 mm + getrokken draad Φ2,0–3,6 mm |
| 2 | continugiet-/walslijn + draadtrekkerij; expeditie voor coils |
| 3 | 江西铜业铜材有限公司 (opgericht 2002), Guixi-vestiging **冶金大道 19号** — hetzelfde complexadres als de smelter, die in hetzelfde register ook op 19号 staat [D1][D12]. ⚠️ **Correctie 2026-08-05: dit stond hier als 15号.** Het nationale emissievergunningregister geeft voor **beide** Guixi-vennootschappen 19号 in het veld `生产经营场所地址`, en de vergunning-PDF van 江西铜业铜材有限公司 zet ook het `注册地址` op 19号. **15号 is het hoofdkantoor-/administratieve adres** van de groep, de beursvennootschap én de 加工事业部 [D3] — de collocatie-conclusie klopt, de onderbouwing via nummer 15 niet |
| 4 | JCC's eigen verwerkingsfabriek; hoofdgrondstof "贵冶牌"-kathode [D1] |
| 5 | het **aansluitpunt op de interne hoofdas** is gelegd; de exacte hal en de laaddeur blijven onbekend → §5 |
| 6 | **28.33180, 117.21919** — **satelliet-gelegd** (Esri z18, 0,53 m/px, 2026-08-05). Coördinaat uit het nationale emissievergunningregister permit.mee.gov.cn V3.0, vergunning **913600007363561816001Q** (行业类别 铜压延加工): verborgen velden `longitude=117.21919` / `latitude=28.33180` **én** `opelngd 117/13/9.08` + `opelatd 28/19/54.48` — decimaal en DMS komen exact overeen. Op z18 ligt het punt op de zuidberm van de brede oost-west interne hoofdas, op de mond van een noord-zuid inrit; ZW ervan een ommuurd blok met een meerbeukige sheddak-hal, ZO ervan een blok van vier lange donkere hallen. ⚠️ **Geen poort**: er is op deze korrel geen poortgebouw, slagboom of hek-onderbreking te zien, alleen een T-aansluiting |

**Uitsluit:** geen bulkbehandeling (het concentraat-tijdperk is voorbij bij de smelter); geen zeekade (300+ km binnenland); coils vertrekken per vrachtwagen of wagon, niet per band. **En het is niet 江西铜业集团铜材有限公司** (28.32956, 117.23688) — een **ándere rechtspersoon** met een eigen ommuurd werk 1.749 m OZO, eigen poortgebouw aan de boulevard, eigen USCC (913606817442997892, divisiecode 360681 tegen 360000) en een eigen vergunning die 锡及其化合物/总锡 noemt. ⚠️ Verwar de twee niet: **beide** dragen 行业类别 铜压延加工 en **beide** noemen dezelfde 法定代表人 余琪. Dat werk staat als **reëel alternatief** in §4 en als **negatief anker** bij been 5.

> ⚠️ **Welk blok op het complex de fabriek is, blijft open — en dat is een uitkomst, geen
> slordigheid.** Drie onafhankelijke passes wezen drie verschillende dingen aan: een sheddak-hal
> op `28.33135, 117.21828` (~158 × 90 m), vier lange evenwijdige hallen op `28.33135, 117.22020`,
> en een narekening van het officiële functieblok uit fig. 3-1 van 赣环监字（2017）第S007号 op
> ~415 × 210 m rond `28.33125, 117.21996`. Op z18 is te zien waarom ze elkaar niet vinden: er
> liggen **twee aangrenzende blokken** en het registerpunt ligt er tussenin, op de mond van de
> inrit. Geen enkel object op het beeld draagt een label. **Daarom wordt géén blok terreinanker**
> — het registerpunt is het anker, en dat is genoeg voor een been dat op de as aanhecht → §5.

### 2b · De overslagregel in deze keten

Een overslag is elke **drager-wissel** en krijgt twee ankers + terreinstappen (werkwijze §2b). In deze keten: **Coloso** (leiding → zee: filterfabriek → wal-einde → kop laadsteiger, drie satelliet-gelegde punten) en **Beilun** (zee → spoor: losberth → band/ertsveld → 北仑港站-laadspoor). De knopen 贵冶 (been 4→5) en walsdraadfabriek (been 5→6) zijn **verwerkingsknopen**, geen overslagen: het product verandert er.

**✅ De tweede aansluiting bij Beilun is er (2026-08-05).** De zin die hier stond — *"als dat gaat knellen hoort er een tweede aansluiting te komen"* — is **doorgevoerd**. Beilun draagt nu:

| rol | aansluiting | lat, lon | modi | routeerpunt | max snap |
|---|---|---|---|---|---|
| losplek zee (aankomst been 2) | `cu-beilun-kade` | 29.93640, 121.88300 | **`["zee"]`** — was `["zee","spoor"]` | 29.94780, 121.88370 | 1,27 km |
| terreinstap | `cu-beilun-bandlandpunt` | 29.92742, 121.87573 | — (geen eigen aansluiting) | — | — |
| laadplek spoor (vertrek been 3) | `cu-beilun-laadspoor` | 29.92653, 121.87308 | `["spoor"]` | 29.92820, 121.87380 | **0,198 km** |

**Anker ≠ routeerpunt, en de restafstand is dat óók.** Het gat tussen de laadplek en het begin van het spoorbeen is **198 m**, en dat is géén restfout: het spoorbeen begint 198 m **noord** van de laadplek en loopt daarna zuidwaarts er langs op 14,1 m. ⚠️ **Verplaats de kop van het spoorbeen dus niet naar de laadplek** — dan krijg je een overschiet-en-terug-haak, precies de klasse die deze ronde bij het fase-D-been is opgetreden.

⚠️ **Wat dit anker draagt is niet de snap-winst.** Een eerdere analyse voerde als kopbewijs "de spoor-snap gaat van 1,27 km naar 0,198 km" op. Die meting is blind: `cu-beilun-laadspoor` én `cu-beilun-bandlandpunt` scoren allebei tegen **dezelfde** grofkorrelige landnet-knoop 326694 (0,198 resp. 0,205 km), en élk punt binnen ~200 m daarvan scoort hetzelfde — op de rails of ernaast. Wat de spoor-claim werkelijk draagt is de **4,5 m tot OSM `way/1491021972`** plus het z19-beeld.

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
   Φ2,0–3,6 mm** (kt **product**, niet kt Cu-inhoud) met "贵冶牌"-kathode als hoofdgrondstof,
   en zit op hetzelfde complexadres **冶金大道 19号** als de smelter [D1][D12] — het
   productieadres uit het emissievergunningregister, níet de 15号 uit een eerdere versie van
   deze brief (dat is het hoofdkantooradres, zie §2a L6 stap 3). De eerste bestemming is dus
   **geen spoorreis maar een interne overbrenging**, en die overbrenging is sinds 2026-08-05
   gemeten: **0,7 km over `way/1462532976`**, de as die het officiële terreinplan als
   **物流主轴线** tekent en die op de tegels **闪速大道** heet.
6. **Wat wél het spoor op gaat, gaat via 贵溪北站 (皖赣) — en dat is de vertakking, niet deze
   streng.** De smelter sluit met een eigen 专用铁路 aan op de 皖赣铁路 bij 贵溪北站;
   elektrolytkoper, zwavelzuur en slak, samen ~3 mln t/jaar sinds 2013 [C7][D5]. Sinds
   2026-04 rijdt er o.a. een zwavelzuur-blocktrein 贵溪北 → 分宜 [D6].

---

# FASE A · Escondida-concentrator → Puerto Coloso

## Been 1 · slurryleiding — Escondida-concentrator → Puerto Coloso (~170 km, stippel)

**been-id:** `koper-escondida-guixi-b1`
**Modaliteit:** slurryleiding (eigen verbinding)
**Lengte:** gepubliceerd ~170 km [E1] — de enige controle die dit been heeft, want er is geen tracé-geometrie. ⚠️ **Op de bol staat 153,5 km, en dat is niet dezelfde grootheid**: de getekende lijn is de **koorde** tussen de twee ankers (verdicht langs de grootcirkel), de gepubliceerde ~170 km is de **werkelijke leiding**. Omwegfactor **1,108**. Dat verschil staat nergens in de data of in het beenlabel — het staat hier en in §7 punt 1, en het is dus geen lengtefout die je moet "oplossen".
**Getekende deelstukken:** dit verhalende been staat op de bol als **twee** stippelbenen — leiding 153,5 km (concentrator → filterfabriek) en leiding 0,3 km (terminalverwerking Coloso: filterfabriek → laadsteiger)
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
**Lengte:** gemeten **19.104 km** in totaal, sinds 2026-08-05 verdeeld over **drie getekende benen**: stippel-aanloop Coloso **85,1** · geroutete zeebeen **19.018,4** · stippel-aanloop Beilun **1,3** km. Orde-toets: atlas-invariant Antofagasta→Shanghai **18.915 km** (searoute 18.880) [Z1]
**Overslagen onderweg:** geen — bulk vaart **direct**, geen transshipment-hub (bulk is geen lijndienst; de direct-vs-hub-vraag speelt hier niet)
**Routeerpunt kop / staart:** -23.80000, -71.30000 (snap 85,1 km — stippel-aanloop, zie overslagblok) · 29.94780, 121.88370 (snap 1,27 km — het schip ligt in het water vóór de berth) [`aansluitingen.json`]
**⚠️ De haven-aanloop van Beilun wordt sinds 2026-08-05 GETEKEND** als stippel van 1,3 km, mét reden: het MARNET-routeerpunt ligt in de geul en het schip lost aan de berth — het spiegelbeeld van de Coloso-aanloop. Vóór die ronde stond daar een gat.

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
| 1 | aankomst been 2 | losberth met de rode ertslossers (`cu-beilun-kade`, sinds 2026-08-05 **zee-only**) | losplek | 29.93640, 121.88300 | [E3] + satelliet z16, hercontrole z17 2026-08-05 | **satelliet-gelegd** |
| 2 | terrein | transportband-landpunt + overslagtoren; vandaar lopen banden zuidwaarts het bulkveld in (`cu-beilun-bandlandpunt` — terreinstap, géén eigen aansluiting) | verwerkingsstap/opslag | 29.92742, 121.87573 | OSM (ODbL) + satelliet z18 | **satelliet-gelegd** |
| 3 | vertrek been 3 | **北仑港站** — laadsporen van het havenstation (北极星路178号, 10,9 ha, 2 货场 / 10 装卸线, 78万TEU/j, 中铁联合国际集装箱宁波北仑) — `cu-beilun-laadspoor` | laadplek | **29.92653, 121.87308** | [C1] + zh.wikipedia 北仑港站 (29°55′35,5″N 121°52′23,1″E) + satelliet z19 | **satelliet-gelegd** (2026-08-05) |

**Routeerpunt ≠ anker.** Zee: 29.94780, 121.88370 (snap **1,27 km**) · spoor: 29.92820, 121.87380
(snap **0,198 km**; = landnet-knoop 326694 én **exact het beginpunt van het gebakken spoorbeen**)
[`aansluitingen.json`]. De berth ligt in het water en het havenspoor eindigt bij het ertsveld —
één punt kon niet tegelijk ligplaats én laadspoor zijn, en dáárom staan er nu **twee**
aansluitingen (werkwijze §2b), geen compromis-coördinaat.

**⚠️ Het gat van 2.379 m is 198 m geworden — en de eerdere verklaring ervan klopte niet.** Vóór
deze ronde eindigde het zeebeen op `29.9478, 121.8837` en begon het spoorbeen op
`29.9282, 121.8738`, met **2.379,1 m** niets ertussen. De oorzaak was géén fout uiteinde maar
**twee tegengestelde snaps van één aansluiting**: `cu-beilun-kade` snapte 1.269,4 m NNO de geul
in én 1.271,7 m ZW het spoor op. ⚠️ Die twee tellen **niet exact** op tot 2.379 m — de hoek
ertussen is **138,8°**, niet 180° (1.269,4 + 1.271,7 = 2.541,2). Het woord *"exact de som van
twee snaps"* hoort dus niet in deze brief te staan, en staat er niet.

**Datumtoets, expliciet uitgevoerd op het nieuwe anker.** As-is ligt `cu-beilun-laadspoor` 4,5 m
van het spoor; gelezen als GCJ-02 en omgerekend verschuift het punt **485 m NW** naar 279,8 m van
élk spoor, midden in de containerstapel. **WGS-84 wint eenduidig** — zelfde uitslag als bij
Tianqi Jiangsu, en conform de projectregel dat Chinese overheidsbronnen in CGCS2000 ≈ WGS-84
staan en **niet** omgerekend worden.

---

# FASE C · aanlanding → smelter

## Been 3 · spoor — Beilun-ertsterminal → 贵溪站

**been-id:** `koper-escondida-guixi-b3`
**Modaliteit:** spoor  ·  **Brief-gestuurd** (werkwijze §6: geen vrije Dijkstra)
**Lengte:** **565,8 km** — dat is het **gebakken been op de bol**, gemeten aan het eindproduct `stroomroute-koper-escondida-guixi.json` (1.264 punten). Tegen de brief-corridor B van ~556 km is dat **+1,8%**; corridor A 628 km (historische variant).
**⚠️ Lengte-attributie 550,5 → 565,8 km (+2,78%), want dit getal is drie keer verschoven zonder dat de corridor veranderde:** meetlat ↔ eindproduct **+0,8** · bochtstraf + verdichten **+5,3** · 10 m-simplify **−1,3** · junctie-fix **+4,2** · 1-op-1-spoorvervanging **+6,3**. De 550,5 km hoorde bij `toets_spoorroute.mjs` op het netstadium van 2026-07-28; dat was het **meetgereedschap**, niet de lijn die de bol tekent. *Meet het eindproduct, niet je meetlat.*
**Net / bron geometrie:** OSM-spoor **1-op-1** (`spoorroute-nieuw-beilun-guixi.geojson`, commit `76fd530`, straf 100) — de toets van §4 is op het M25-landnet geslaagd en de corridor is bij de 1-op-1-vervanging niet gewijzigd
**Stippel:** nee
**Corridor bij naam:** 北仑支线 → **甬金铁路** (Yong-Jin) → 沪昆铁路 (= corridor B, gemeten); historisch 北仑支线 → 萧甬铁路 → 沪昆/浙赣 (= corridor A)
**Routeerpunt kop / staart:** 29.92820, 121.87380 (max snap **0,198 km** vanaf `cu-beilun-laadspoor` — dit routeerpunt ís het beginpunt van het gebakken been) · 28.32710, 117.22650 (max snap 0,05 km) [`aansluitingen.json`]
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

**Gemeten uitslag corridortoets (2026-07-28, `toets_spoorroute.mjs`):** corridor B, alle
bevestigde punten geraakt, alle negatieve ankers gemeden. Zie het kader bovenaan. Het getal uit
die run (550,5 km) is vervangen door de meting aan het **gebakken** been: **565,8 km**.

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

*Onderzocht 2026-07-29, **getekend 2026-08-05**. De eerste bestemming van de kathode is
**gedocumenteerd op het eigen complex**: 江西铜业铜材有限公司 noemt "贵冶牌"-kathode als
hoofdgrondstof en zit op hetzelfde complexadres (冶金大道 **19号**) als de smelter [D1][D12].
Fase D is dus een **interne overbrenging**, geen spoor- of wegcorridor. Het spoorbeen
贵溪北站 → markt bestaat óók, maar dat is de vertakking (§4), niet deze streng.*

## Been 5 · intern wegtransport — registerpunt 贵冶 (substituut-kop) → walsdraadfabriek 江西铜业铜材有限公司

**been-id:** `koper-escondida-guixi-b5`
**Modaliteit:** `truck` — intern wegtransport op het complex. ⚠️ **Werkaanname, geen bron.** Geen enkele bron beschrijft het voertuig; het been heet `truck` omdat de brief dat als werkaanname noemt en de corridor een weg ís → §5. Bijvangst die het níet beslecht: er ligt een landnet-**spoor**knoop op 0,156 km van de walsdraadfabriek (117.22050, 28.33260) — een **meetresultaat**, geen bewijs dat de kathode het spoor op gaat
**Lengte:** **0,7 km getekend** (4 punten): 613 m over de OSM-way + aanloop kop **43 m** + aanloop staart **8 m** = 664 m deur-tot-deur. Lengtetoets **−1,2%** tegen de eigen vooraf-meting van 0,62 km. **Pad ÷ hemelsbreed = 1,08** → geen terugloop
**Net / bron geometrie:** OSM **`way/1462532976`** (`highway=service`, **géén access-tag**, 2.250 m, **5 vertices**), geknipt tussen de twee ankerprojecties met `v2/tools/knip_osm_been.py`
**Stippel:** **NEE — doorgetrokken.** Gemeten reikt het net tot op **8 m** van het staart-anker en 43 m van het kop-anker. Een stippel betekent in dit project precies één ding, *hier reikt het net niet* (werkwijze §7), en zou hier dus liegen
**Corridor bij naam:** **闪速大道** op de tegels = de **物流主轴线** uit het officiële terreinplan (赣环监字（2017）第S007号, fig. 3-1). De way loopt kaarsrecht oost-west over het hele complex, van 28.33184, 117.23626 (aansluiting op 冶金大道 aan de oostrand) tot 28.33187, 117.21327 aan de westrand
**Routeerpunt kop / staart:** 28.33188, 117.22545 (projectie kop-anker op de as, 43 m) · 28.33187, 117.21919 (projectie staart-anker, 8 m) — beide punt-tot-segment gemeten
**Toets-marge:** verklikkers die op de getekende lijn zijn gedraaid — elk punt tussen lat **28.3310–28.3325** (noordelijker = de private dienstweg of de spoorbundel, zuidelijker = het fabrieksblok) en lon **117.2190–117.2256** (het been mag de as niet oostwaarts uitlopen); nergens binnen **1,0 km** van het negatieve anker 江西铜业集团铜材有限公司 (gemeten minimum bij een correcte lijn: 1,15 km); nergens binnen **1,5 km** van 贵溪北站. ⚠️ Die laatste toets stond op 1,5 km, maar de **verbodsstraal van 贵溪北站 in deze brief blijft 2 km** — het voorstel om hem te verkleinen kwam uit een bevinding die op de geometrie-lens is gesneuveld (§5.14)

> ### ⚠️ DE KOP IS EEN SUBSTITUUT — LEES DIT VÓÓR DE PUNTENLIJST
>
> Been 5 loopt **niet** van laadplek naar losplek maar van **verwerkingsknoop naar
> aansluitpunt**. De kathode-expeditie op het 贵冶-terrein is **niet gevonden** (§5.5) en wordt
> niet vervangen door een gok; in plaats daarvan is het **satelliet-gelegde registerpunt van de
> smelter** als kop genomen. Dat is een administratief vergunningpunt midden in het pyro-hart,
> niet de plek waar kathodebundels de deur uit gaan.
>
> **Waarom dan toch tekenen (besluit Lars 2026-08-05):** beide uiteinden zijn officiële
> productiepunten uit hetzelfde register, beide zijn satelliet-gelegd, en de corridor ertussen
> heeft een **naam uit een officieel terreinplan** én een gemeten OSM-geometrie. Zelfde klasse
> besluit als bij De Soto in de grafietketen: **één** terreinanker in plaats van de twee die
> §2b eist, mét de afwijking expliciet in de tekst.
>
> **En het gat blijft staan.** Tussen been 8 (spoor) en been 9 (fase D) zit **0,584 km** en dat
> gat **ís** het ontbrekende anker. Groeit of verschuift het, dan is er iets misgegaan;
> verdwijnt het, dan is de expeditie gevonden. Wie het dichttrekt met een rechte lijn haalt de
> Waalhaven/Nacala/New Orleans-klasse binnen.
> ⚠️ **0,584 km, niet 0,541.** De schatting vooraf mat tot de projectie op de as; de getekende
> lijn begint op het **anker zelf**, 43 m verder.

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **贵溪冶炼厂 — registerpunt** (91360000X12430120H001P, 铜冶炼, 冶金大道 19号) — **SUBSTITUUT-KOP**, terreinanker/registerknoop, géén laadplek | verwerkingsstap | **28.33227, 117.22545** | [D12] + satelliet z18 | **satelliet-gelegd** |
| 2 | 0,04 | projectie van punt 1 op `way/1462532976` — hier begint de as | routeerpunt | 28.33188, 117.22545 | eigen meting 2026-08-05 | gemeten (43 m) |
| 3 | 0,66 | projectie van punt 4 op dezelfde way — mond van de noord-zuid inrit | routeerpunt | 28.33187, 117.21919 | eigen meting 2026-08-05 | gemeten (8 m) |
| 4 | 0,7 | **江西铜业铜材有限公司 — registerpunt** (913600007363561816001Q, 铜压延加工, 冶金大道 19号); `cu-guixi-walsdraad` | aansluitpunt / eind fase D | **28.33180, 117.21919** | [D12] + satelliet z18 | **satelliet-gelegd** |
| — | — | **Kathode-expeditie / productmagazijn 贵冶** — de wérkelijke kop van dit been | laadplek | **niet gevonden** | — | **open → §5.5** |

**Opmerkingen been 5.** De fabriek bestaat sinds 2002-03-22 [D3]; de productrelatie
("贵冶牌"-kathode als hoofdgrondstof) staat in [D1]. De collocatie staat nu op **drie**
onafhankelijke voeten: beide vennootschappen op 冶金大道 19号 in het emissievergunningregister
[D12], de interne terreinverdeling met **铜材公司** als eigen blok in het provinciale
EIA-toezichtstuk [D13] p.11, en de gemeten OSM-as die beide registerpunten binnen 43 m raakt.
Wat níet gedocumenteerd is: de exacte hallen, de laaddeur en het voertuig van de overbrenging.

### ⚠️ De les van dit been: een router kan een been korter dan zijn eigen knoop-korrel niet leggen

Dit been is **twee keer gebakken**, en de eerste keer was fout op een manier die stil had kunnen
passeren. `maak_stroombeen_weg.py` routeert over een graaf waarvan de knopen de
**OSM-way-vertices** zijn. Dat is precies goed voor een corridor van honderden kilometers, maar
`way/1462532976` heeft **5 vertices over 2.250 m** en de dichtstbijzijnde knoop bij de
walsdraadfabriek ligt **179 m ten westen** ervan. De router kan alleen op een knoop eindigen,
dus kwam eruit:

```
kop-anker → projectie 43 m → 792 m WESTWAARTS, voorbij de fabriek
          → 179 m TERUG oostwaarts naar het anker            = 1,01 km  (lengtetoets +29,0%)
```

Dat is **overschiet-en-terug op het EINDpunt van een been** — dezelfde klasse die op 2026-08-05
bij de grafiet-via-punten is benoemd, maar daar op *doorgaande* punten. Het is **geen
werkelijkheid** (geen truck rijdt langs de poort heen om te keren) maar de **korrel van onze
eigen graaf**; hem laten staan zou een meetfout als geometrie de kaart op schrijven.

**Opgelost met nieuw gereedschap: `v2/tools/knip_osm_been.py`.** Eén way, twee ankers, **géén
routering** — beide ankers loodrecht op de polylijn projecteren en het stuk ertussen eruit
knippen, in reisvolgorde, mét de ankers als eerste en laatste punt. Zelfde GeoJSON-contract dat
`hecht_marnet.py route --been-geojson` leest. De geometrie komt dus **nog steeds uit OSM en niet
uit een oog** — dat onderscheid is de Tongling-regel: een handlijn is er voor het geval dat OSM
de geometrie **niet** heeft, en die heeft hij hier wél. Het tool rapporteert zelf de verhouding
**pad ÷ hemelsbreed** (hier **1,08**), zodat een overschiet-en-terug niet meer stil kan passeren.
⚠️ Dit vervangt `maak_stroombeen_weg.py` niet; gebruik het alléén als het been over precies één
benoemde way loopt én de way-vertices te grof zijn voor de beenlengte.

**Twee nieuwe knikken, en beide zijn echt.** `toets_knikken.py` gaat van 157 naar **159** knikken
≥60°; de twee nieuwe zitten allebei in dit been: **89,9° op `28.33188, 117.22545`** en **89,9° op
`28.33187, 117.21919`**. Dat zijn de haakse aansluitingen van de twee inritten op de hoofdas —
geen artefact. Omkeringen blijven **25** en terugloop blijft **3** (alle drie in
`stroomroute-pilot`); de vier andere stromen zijn in de diff **letterlijk ongewijzigd**.
⚠️ De 150°-drempel van dat gereedschap is op **spoor** geijkt, waar een trein fysiek niet kan
omkeren; op weg en eigen terrein hoort een omkering met **pad ÷ hemelsbreed** beoordeeld te
worden, niet met de drempel alleen.

**Waarom géén stippel en géén handlijn — de drie opties zijn gemeten, niet beredeneerd.** In de
lokale extract (`china-latest.osm.pbf`, eigen bbox-scan 2026-08-05, 55 highway-ways in het
venster) en onafhankelijk in een live Overpass-set:

| OSM-way | klasse | access | lengte | punten | tot smelter-registerpunt | tot walsdraad-registerpunt |
|---|---|---|---|---|---|---|
| **1462532976** | `highway=service` | **geen** | **2.250 m** | 5 | **43 m** | **8 m** |
| 995766131 | `highway=service` | `private` | 785 m | 4 | 2 m | 615 m |
| 1462532977 | `highway=service` | geen | 274 m | 3 | 792 m | 179 m |
| 313248139 / 552438139 | `highway=secondary`, naam **冶金大道** | geen | 3.177 m | — | 1.051 m | 1.663 m |

*(i) stippel valt af* — het net reikt tot op 8 m. *(ii) hand-geplaatste geojson valt af* — die is
er voor het geval dat OSM de geometrie níet heeft (de Tongling-oostgeul); hier heeft OSM hem wél.
*(iii) de way zelf wint*, en de private dienstweg 995766131 valt er per constructie uit — precies
goed, want die loopt het smelterhart in.

**Negatieve ankers been 5:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| **江西铜业集团铜材有限公司** | **28.32956, 117.23688** | **1,0 km** | een **ándere rechtspersoon** met een eigen ommuurd werk 1.749 m OZO (USCC 913606817442997892, divisiecode 360681 tegen 360000, eigen vergunning die 锡及其化合物/总锡 noemt). ⚠️ Beide dragen 行业类别 铜压延加工 en beide noemen dezelfde 法定代表人 余琪 — dit been mag er niet naartoe lopen. Gemeten minimum bij de getekende lijn: **1,15 km** ✅ |
| 贵溪北站 | 28.34611, 117.18917 | **2 km** | wat via 贵溪北 het spoor op gaat is de **markt-vertakking** en het bijproduct [C7][D6], niet de streng naar de eigen walsdraadfabriek. ⚠️ Deze straal is bewust **niet** naar 1,5 km verkleind: dat voorstel kwam uit een bevinding die op de geometrie-lens is gesneuveld (§5) |
| 鹰潭 (stadscentroïde, incl. hightech-zone) | 28.26000, 117.07000 | 5 km | de walsdraadfabriek staat op het 冶金大道-complex in **Guixi**; verwarring met JCC's dráádfabriek 江铜华东电工 in de 鹰潭高新区 ligt voor de hand [D8] — dat is een vertakking (§4), niet dit been |

## Verwerkingsknoop · 江西铜业铜材有限公司 (walsdraad + draad, Guixi)

*Hier hoort de vraag: wat komt er nog NA dit product? Zolang het antwoord "nog een
bewerking elders" is, gaat de brief door — zie fase E.*

| | |
|---|---|
| **anker-id** | **`cu-guixi-walsdraad`** (28.33180, 117.21919) — aangemaakt 2026-08-05, satelliet-gelegd z18, rol *aansluitpunt op de interne hoofdas*. ⚠️ **Géén poort**: op z18 is geen poortgebouw, slagboom of hek-onderbreking zichtbaar, alleen een T-aansluiting van een inrit op de as |
| **modi in `aansluitingen.json`** | **`modi=[]` — geen enkele modus, en dat is gemeten.** Een weg-aanhechting is hier zinloos: het landnet heeft wereldwijd maar **1.883 wegknopen** en de dichtstbijzijnde ligt op **341,1 km** (115.08000, 25.92620). De interne complexweg zit **niet** in het landnet (wél in OSM — daar komt de beengeometrie vandaan). Zelfde rolverdeling als `cu-escondida-laad`. ⚠️ Bijvangst: er ligt wél een landnet-**spoor**knoop op **0,156 km** (117.22050, 28.33260) — dat is een **meetresultaat**, geen bewijs dat de kathode het spoor op gaat; de modaliteit van de interne overbrenging is niet gedocumenteerd (§5) |
| **eigenaar van dit anker** | deze brief |
| **in** | kathode "贵冶牌" (hoofdgrondstof, van de smelter hiernaast) + "江铜牌"-tin [D1] |
| **andere ingaande strengen** | geen gedocumenteerd |
| **uit** | **370 kt/j** walsdraad Φ8 mm (电工用铜线坯) + **120 kt/j** getrokken ronde draad Φ2,0–3,6 mm [D1] — kt **product**, niet kt Cu-inhoud |
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
| 1 | 0 | expeditie walsdraadfabriek (coils Φ8 mm / draad op haspels) | laadplek | — | [D1] | **niet gevonden** → §5 |
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

> ### ⚠️ HET STOPPUNT IS OP 2026-08-05 OPNIEUW GETOETST — EN STAAT STERKER
>
> Een zoekronde vond één kandidaat-fase-E-bestemming en die is bij de weerlegging **gesneuveld
> op een entiteitsfout**, tweemaal:
>
> 1. **De gelijkstelling "江铜华东铜材 = de 上饶-fabriek" is fout.** Het gevonden
>    CSRC-toezichtstuk definieert die naam letterlijk als **江铜华东（浙江）铜材有限公司**, pand
>    浙江省诸暨市陶朱街道迎宾路2号厂房 — **508,2 km** van de uitgever, in **Zhejiang**, niet in
>    上饶. De deelstring 华东铜材 matcht in het register alleen de 上饶-vennootschap omdat in de
>    Zhejiang-naam **（浙江）tússen 华东 en 铜材** staat. Daarmee vervalt de hele
>    herclassificatie die daarop leunde.
> 2. **En het stuk documenteert een KATHODE-relatie, geen walsdraad-afzet.** De keten die erin
>    beschreven staat is 委托加工: JCC-kathode → een van drie 铜材-bedrijven → draad → Nanchang.
>    De genoemde **178 km** hoort bij de **smelter** («距离江铜贵溪冶炼厂仅约178公里 … 最近的
>    **阴极铜**生产商») en heeft bovendien geen onderscheidend vermogen: smelter→Nanchang
>    131,40 km tegen walsdraadfabriek→Nanchang 130,60 km.
> 3. **De volumes veroordelen het been.** 江西铜业**铜材** — de fabriek van déze brief — levert
>    de uitgever alleen 加工服务 van **1,94 / 9,26 / 9,19 / 7,97 万元** per jaar (0,00–0,01% van
>    de inkoop), terwijl 江西铜业**集团**铜材 ~50× meer doet.
>
> **Uitkomst: fase E wordt niet getekend.** Wat er wél uit meegaat is een **vertakking bij de
> smelterknoop** — een gedocumenteerde kathode-stroom naar 江铜华东（浙江）铜材有限公司 in
> 诸暨/Zhejiang op 508,2 km. Die staat in §4, niet als fase-E-been.
> *Wat het stoppunt zou opheffen:* een recente 关联交易-tabel van 江铜铜箔 of JCC waarin een
> **walsdraad**- of draadstroom **mét productieplaats** staat.

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
| 3 | knoop 贵冶 (na b4) | vertakking | kathode → JCC 22万吨-walsdraadlijn, 上饶经开区 (gepland in bedrijf eind 2022) [D10] | deel kathode oostwaarts over de 沪昆-corridor | onbekend → §5 | geen eigen brief. ⚠️ **De herclassificatie van deze rij tot "dochter van de walsdraadfabriek" is teruggedraaid** (2026-08-05): die leunde op de entiteitsverwarring 华东铜材 ↔ 江铜华东（浙江）铜材, zie been 6 |
| 4 | knoop walsdraad (na b5) | vertakking | JCC-draadketen: 江铜华东电工新材料, 鹰潭高新区 — elektromagnetische draad voor nieuwe energie, 100 kt/j gepland (fase 1: 50 kt) [D7][D8] | deel walsdraad/koper naar de draadtak | onbekend → §5 | geen eigen brief |
| 5 | knoop 贵冶 (na b4) | **vertakking (nieuw 2026-08-05)** | **kathode → 江铜华东（浙江）铜材有限公司**, 浙江省诸暨市陶朱街道迎宾路2号厂房 — **508,2 km** oostwaarts; 委托加工-keten JCC-kathode → 铜材 → draad → Nanchang [D14] | kathode, niet walsdraad — daarom een vertakking bij de **smelter**knoop en géén fase-E-been | onbekend → §5 | geen eigen brief |
| 6 | knoop 贵冶 / fase D | **reëel alternatief (nieuw 2026-08-05)** | **江西铜业集团铜材有限公司**, Guixi — **28.32956, 117.23688**, eigen ommuurd werk 1.749 m OZO, andere USCC (913606817442997892), eigen vergunning met tin-signatuur | kathode die op het complex verwerkt wordt maar **niet** bij de fabriek van deze brief | onbekend → §5 | geen eigen brief; staat óók als **negatief anker** bij been 5 (straal 1,0 km) |
| 7 | knoop 贵冶 (na b4) | bijproduct | zwavelzuur + slak via 贵溪北站, o.a. blocktrein 贵溪北 → 分宜 [C7][D6] | bijproduct, geen koperstreng | — | valt buiten de koper-atlas |

**Regel:** één brief = één streng. Deze brief volgt de kathode naar de **eigen
walsdraadfabriek**; de markt-vertakking (rij 2) is substantieel en verdient te zijner tijd
een eigen stroom-id + brief — de puntenlijst wordt hier niet herhaald.

## 5 · Openstaande punten

*Stand 2026-08-05: punt 1 en punt 6 zijn **gesloten**, punt 10 is **grotendeels vervallen**. De
rest is scherper geformuleerd, en er zijn vier punten bijgekomen.*

| # | been | wat | waarom onzeker | wat het zou oplossen |
|---|---|---|---|---|
| ~~1~~ | b2→b3 | ~~北仑港站-laadspoor heeft geen coördinaat~~ | **GESLOTEN 2026-08-05** — `cu-beilun-laadspoor` **29.92653, 121.87308**, satelliet-gelegd z19, 4,5 m van OSM `way/1491021972`, snap spoor 0,198 km | — |
| 2 | b3 | passage-/stationscoördinaten corridor A & B niet ingevuld | de toets draait op het net en is geslaagd; puntcoördinaten waren nooit ingevuld | lage prioriteit; z13-pass per station |
| 3 | b3/b4 | 贵溪站-coördinaat (28.29308, 117.20972) is een zh.wiki-waarde, en het góederenemplacement kan iets verschoven liggen | één bron; nieuw uit research 2026-07-29. ⚠️ Een ronde die dit punt wilde verplaatsen naar de noordrand van de perrongroep is op de geometrie-lens gesneuveld (het ligt 36–41 m aan de **zuid**kant tegen het stationsgebouw) | z16-satellietpass (Esri) op het emplacement |
| 4 | b4/b5 | 贵溪北站-coördinaat (28.34611, 117.18917) idem | één bron (zh.wiki) | z16-satellietpass |
| 5 | b5 | **kathode-laadplek / expeditie** op het 贵冶-terrein: geen coördinaat — **de werkelijke kop van been 5** | ⚠️ **Nu mét de reden, en die is hard:** Esri heeft bij Guixi **geen z19** (z19 en z20 leveren exact 2.521 byte placeholder, per tegel nagemeten) en Wayback-release 64001 is identiek aan live — het is een **zoomplafond**, niet de opnamedatum-faalmodus. 0,53 m/px is de fijnste korrel en een laaddeur ligt daaronder. Geen enkele bron koppelt 电解车间 of 成品库 aan een gebouw. Geprobeerd: permit.mee.gov.cn (geeft één coördinaat per vergunning, geen installatielijst), Chinese zoekopdrachten op 电解车间 / 成品库 / 阴极铜出库 / 装车 / 提货大门 / 厂区平面布置 / 鸟瞰 / 招标 via smm.cn, cnmn.com.cn, jxcc.com, jxgqcg.com, people.cn | een **niet-Esri**-beeldbron op Guixi, óf het 环评/竣工验收-dossier van het 智能化电解车间 (news.cn 2026-01-23) met een 厂区平面布置图 mét 四至. **Zolang dit open staat blijft het procesgat van 0,584 km staan — en dat is bewust** |
| ~~6~~ | b5 | ~~losplek walsdraadfabriek: adres bekend, coördinaat niet~~ | **GESLOTEN 2026-08-05** — `cu-guixi-walsdraad` **28.33180, 117.21919**, satelliet-gelegd z18, uit het emissievergunningregister (decimaal + DMS komen exact overeen). Adres gecorrigeerd naar **冶金大道 19号** | — |
| 7 | b5 | **modaliteit** van de interne overbrenging — het been heet `truck` maar dat is een werkaanname | nergens beschreven. ⚠️ Bijvangst die het níet beslecht: landnet-**spoor**knoop op 0,156 km van de fabriek — meetresultaat, geen bewijs | bedrijfsbron of een beeldbron met kathodetrucks/laadperron |
| 8 | b6 | **expeditiedeur / laadperron van de walsdraadfabriek** (begin fase E) + de modaliteitssplit weg/spoor | zelfde oorzaak als punt 5: 0,53 m/px is te grof. Er ís een **kandidaat** — het verharde voorterrein langs de noordgevel op ~`28.33169, 117.21834` met een rij van 8–10 voertuiggrote rechthoeken — maar er is geen laadperron, geen laaddeur en geen coilstapel zichtbaar. **Status onzeker, dus geen anker** | een fijnere beeldbron; vrachtdocumentatie of spoorwegbron voor de split. Tot die tijd wordt been 6 niet getekend |
| 9 | §4 | aandeel-schatting markt-vertakking (~2/3) en aandelen 上饶 / 鹰潭 / 诸暨 | afgeleid uit capaciteitscijfers, niet uit een verladingsstatistiek | JCC-jaarverslag-segmentatie [D2] of spoorstatistiek 贵溪北 |
| ~~10~~ | b5/b6 | ~~geen enkel fase D/E-anker is satelliet-gelegd~~ | **VERVALLEN 2026-08-05** — beide fase-D-ankers (`cu-guixi-walsdraad` en het smelter-registerpunt) zijn satelliet-gelegd op z18. Wat er van dit punt overblijft staat nu als 5 en 8: de twee **laadplekken** binnen die terreinen zijn niet gelegd, en daarom blijft de regel *"elke laadplek satelliet-gelegd"* in §8 onafgevinkt | zie 5 en 8 |
| 11 | b3 / §2a L3 | **PRODUCTCONFLICT: containers of bulk bij Beilun** | het satelliet-gelegde laadspoor is een **container**emplacement (78万TEU) terwijl ladder L3 stap 1 "natte bulk in open wagons" zegt. `cu-beilun-laadspoor` is daarmee geografisch waterdicht en **inhoudelijk voorwaardelijk** | een beslissing in de brief (niet in de satelliet) vóór fase C als afgesloten geldt; óf één Wayback-opname met gondola's onder de bandgalerijen op `29.91820, 121.87075` / `29.91765, 121.87050` |
| 12 | b5 | **welk blok op het complex 铜材公司 is** — twee tegenstrijdige kandidaten | drie passes wezen drie dingen aan (sheddak-hal `28.33135, 117.21828` · vier lange hallen `28.33135, 117.22020` · narekening functieblok ~415 × 210 m rond `28.33125, 117.21996`); op z18 liggen er **twee aangrenzende blokken** met het registerpunt ertussenin, en niets draagt een label. Daarom wordt **géén blok terreinanker** | een EIA, vergunningbijlage of 竣工验收 van 铜材公司 zélf, met 四至 of oppervlak |
| 13 | alle | **been-ids ontbreken in álle vijf gebakken stromen** | werkwijze §2 eist dat stroomroute-JSON's en markertabellen naar dezelfde `<stroom-id>-b<n>`-ids verwijzen; geen enkel gebakken been draagt er een (sleutels zijn overal `modaliteit/naam/stippel/km/punten`) en `hecht_marnet route` heeft er geen vlag voor. Ook: **brief-been b4** bestaat niet als eigen been in de data, terwijl §3.4 de last mile als eigen been eist | gereedschapswerk — een `--been-id`-vlag op `hecht_marnet.py route` |
| 14 | b3/b4 | de rolverdeling **贵溪站 vs 贵溪北站** rond het smelterterrein | een eigen nameting wijst uit dat het smelterterrein **één** spooraansluiting heeft en dat die bij **贵溪北** ligt (junctie→贵溪北 = 9,024 km, klopt op 0,3% met de 9 km buurstationsafstand van zh.wikipedia), terwijl deze brief "erts binnen via 贵溪站, product uit via 贵溪北" schrijft. Ook: de ertslosbundel ligt aan de **zuid**zijde van het complex, niet de noord (§2a L4 stap 5). ⚠️ Het bijbehorende voorstel om been 4 te splitsen is **verworpen**: het legde 1,97 km spoor neer dat er niet is (14,3 km tegen een gemeten kortste pad van 12,374 km) | dit is **fase-C-materiaal en verdient een eigen ronde** vóór fase C als afgesloten geldt |

## 6 · Conflicten met de projectdata (afwerklijst)

| # | wat | nu | hoort te zijn | bron |
|---|---|---|---|---|
| 1 | `cu-escondida-laad` | -24.27004, -69.07169 (ín de put) | **-24.26200, -69.06000** (concentrator + indikkers = kop van de leiding) | satelliet z16 |
| 2 | `cu-coloso-kade` | -23.76015, -70.46332 (kustweg bij het dorp) | **-23.75690, -70.46520** (kop laadsteiger); filterfabriek -23.75900, -70.46700 | satelliet z17 |
| 3 | `cu-beilun-kade` | 29.92742, 121.87573 (waar de transportband aan land komt; in de oude tabel als lon/lat genoteerd) | **29.93640, 121.88300** (losberth met ertslossers); het bandpunt blijft als begin van de last mile | satelliet z16 |
| 4 | flow `cu-escondida → cu-ref-jiangxi`, `via: [cu-port-antofagasta, cu-port-ningbo]` | via de haven Antofagasta | via **Coloso** (Escondida's eigen terminal, 12 km zuidelijker) | [E3] |
| 5 | ~~spoorbeen Beilun→Guixi~~ | ~~gemeten 883 km~~ | **VERVALLEN** — corridor B bevestigd door de toets van §4; het gebakken been meet **565,8 km** | meting 2026-07-28 + bake 2026-07-29 |
| 6 | leiding-been Escondida→Coloso | ontbreekt / recht | **gestippeld mét reden** (~170 km, eigen verbinding, geen OSM-tracé) | [E1] + werkwijze §7 |
| 7 | `aansluitingen.json` mist fase D-ankers | keten stopt bij `cu-guixi-spoor` (ertskant) | ~~`cu-guixi-kathode-laad`~~ **en** `cu-guixi-walsdraad` | [D1][D12] |
| 8 | `data/copper.js` heeft geen uitgaand been vanaf Guixi | keten eindigt op de smelter | fase D (been 5) toevoegen; de markt-vertakking pas bij een eigen brief | deze brief |
| 9 | **adres walsdraadfabriek** | 冶金大道 **15**号 [D3] | **冶金大道 19号** — het veld `生产经营场所地址` van **beide** Guixi-vennootschappen in het emissievergunningregister, plus het `注册地址` in de vergunning-PDF. 15号 is het hoofdkantoor-/administratieve adres van groep/beursvennootschap/加工事业部 | [D12] |
| 10 | **`cu-beilun-kade` draagt twee modaliteiten** | `modi=["zee","spoor"]` — één punt is tegelijk ligplaats én laadspoor | **`modi=["zee"]`**; de spoorkant wordt een eigen aansluiting `cu-beilun-laadspoor` (werkwijze §2b) | deze brief + satelliet z19 |
| 11 | **projectbanner `CLAUDE.md`** | noemt voor deze stroom nog "leiding 154 → zee 19.104 → trein 551 = 19.809 km" | **9 benen · 19.826,6 km** (trein 565,8) | eigen meting aan het gebakken bestand |

> **✅ 1, 2 en 3 zijn DOORGEVOERD** (2026-07-28, na goedkeuring van Lars): de
> coördinaten staan in `v2/tools/maak_aansluitingen.py` (de redactionele lijst =
> bron van waarheid) en in het daaruit gegenereerde `v2/data/aansluitingen.json`,
> mét de verplaatsing en de reden in de `noot`. Gemeten neveneffect bij Beilun:
> de zee-snap verbeterde (2,4 → 1,3 km) en de spoor-snap verslechterde (0,2 →
> 1,3 km) — de berth ligt in het water, het havenspoor eindigt bij het ertsveld.
> Eén punt kan niet allebei zijn; **dat is per 2026-08-05 opgelost met een tweede
> aansluiting** (rij 10), geen compromis-coördinaat.
>
> **✅ STAND 2026-08-05 — WAT ER DEZE RONDE IS DOORGEVOERD:**
> - **rij 7 · HALF doorgevoerd.** `cu-guixi-walsdraad` staat erin (28.33180, 117.21919,
>   `modi=[]`). **`cu-guixi-kathode-laad` komt er NIET** — die expeditie is niet gevonden
>   (§5.5) en krijgt geen verzonnen coördinaat. Het gat van 0,584 km op de bol is precies
>   dát ontbrekende anker.
> - **rij 8 · doorgevoerd voor de `note`, BEWUST NIET als node.** `cu-ref-jiangxi` staat op
>   28.30 / 117.20 en de walsdraadfabriek ligt daar **4,0 km** vandaan; twee nodes van
>   dezelfde grondstof binnen één 0,25°-cel geven in de v1-render een `degDist: 0`-boog (de
>   M8-les, Baotou/Ganzhou). Bovendien is dit de vastgelegde **rolverdeling**: het register
>   staat op wereldschaal, de aansluiting op straatniveau (besluit 2026-07-30,
>   `li-greenbushes` / `cu-guixi-spoor`). ⚠️ Bij het overnemen van 370/120 kt in `copper.js`:
>   dat zijn kt **product**, en `copper.js` rekent in `kt Cu/jaar (indicatief)` — voor koper
>   schelen die vrijwel niet, maar schrijf het op in plaats van het stil te laten.
> - **rij 9, 10 en 11 · nieuw deze ronde.**
> - **`aansluitingen.json` 25 → 27**, en geen enkele bestaande plek is verschoven (0,0 m —
>   generator↔uitvoer vooraf vergeleken, de `cu-guixi-spoor`-driftles).
> - **4 en 6 staan nog steeds open.**

## 7 · Wat de kaart tekent

*Stand 2026-08-05, gemeten aan `v2/data/stroomroute-koper-escondida-guixi.json`:
**9 benen · 19.826,6 km · 3.233 punten · 6 markers**. Bak-recept: `bak_koper_escondida()` in
`v2/tools/bak_stromen.sh`. ⚠️ Dat recept is **gereconstrueerd, niet teruggevonden** — het bewijs
is "dit commando produceert dat artefact", nooit "dit was het commando van 29 juli"; vier
vrijheidsgraden geven een byte-identiek bestand en het bestand op schijf onderscheidt ze niet.
⚠️ De invoerbestanden liggen in `build-cache/` en zijn ongetrackt: op een verse clone draait dit
recept niet.*

1. **Been 1 — leidingbeen** (stippel, amber): concentrator -24.26200, -69.06000 →
   Coloso-filterfabriek -23.75900, -70.46700 (**153,5 km**) → laadsteiger (**0,3 km**). Label:
   *slurryleiding ~170 km — eigen verbinding, geen net.*
   ⚠️ **Getekend 153,5 ≠ gepubliceerd ~170**: de lijn is de **koorde** tussen twee ankers, de
   ~170 km is de werkelijke leiding (omwegfactor **1,108**). Dat staat nergens in de data of het
   beenlabel, dus het staat hier — het is géén lengtefout om op te lossen.
2. **Been 2 — zeebeen** (zeeschip), sinds 2026-08-05 in **drie** getekende stukken: stippel
   haven-aanloop Coloso **85,1** (MARNET reikt hier niet; Chili heeft nul havens met varend
   AIS-verkeer → dit is de **eindvorm**) · geroutet **19.018,4** · stippel haven-aanloop Beilun
   **1,3** (het MARNET-routeerpunt ligt in de geul, het schip lost aan de berth). Router vrij;
   de Antofagasta-via eruit (conflict 4).
3. **Overslag Beilun — twee terreinbenen** (stippel, `leiding`): transportband losberth →
   landpunt **1,2 km** · ertsveld → laadspoor 北仑港站 **0,3 km**. Beide zijn eigen terrein
   zonder net; ze staan als `leiding` omdat `KLEUR` in `v2/src/stroomroute.js` die modaliteit
   letterlijk beschrijft als *"een EIGEN VERBINDING, geen net … dit been kan per definitie niet
   herrouteren"* — precies wat een transportband is. ⚠️ Wil er ooit een eigen **bandkleur**
   komen, laat dat een expliciete keuze zijn: twee modaliteiten in één kleur maken de legenda
   onwaar.
4. **Been 3 — spoorbeen**: laadspoor 北仑港站 → 贵溪站. **Corridor B**, gebakken
   **565,8 km**; corridor A blijft in deze brief staan als historische variant en toetsmateriaal.
5. **Been 4 — last mile** (kort): 贵溪站 → ertslosbundel 28.32710, 117.22600.
6. **Been 5 — kathode naar de walsdraadfabriek: WORDT GETEKEND** (besluit Lars 2026-08-05),
   als **`truck`, 0,7 km, DOORGETROKKEN** over OSM `way/1462532976` (闪速大道 / 物流主轴线).
   ⚠️ **Geen stippel**, en dat is gemeten: het net reikt tot op **8 m** van het staart-anker.
   ⚠️ **De kop is een substituut** — het registerpunt van de smelter, niet de kathode-expeditie.
   Wie de lijn leest als "hier vertrekt de kathode" leest hem fout; dat hoort in het beenlabel én
   in de node-noot te staan.
7. **Het procesgat van 0,584 km tussen been 8 en been 9 is BEWUST en benoemd.** Het is exact zo
   groot als het ontbrekende anker (de kathode-expeditie, §5.5). Groeit of verschuift het, dan is
   er iets misgegaan; verdwijnt het, dan is het anker gevonden. **Een tweede uitzondering op de
   0,5 km-eis is een fout.** Niet dichttrekken met een rechte lijn.
8. **Been 6 — marktwaaier**: **niet tekenen** — beargumenteerd stoppunt, geen anker. De
   onderbouwing is per 2026-08-05 sterker (zie been 6): de enige kandidaat brak op een
   entiteitsfout en documenteert bovendien een **kathode**-relatie, geen walsdraad-afzet.
9. **Niet tekenen:** de tak Escondida → Chuquicamata (aparte flow) · de markt-vertakking
   van de kathode via 贵溪北站 (krijgt t.z.t. een eigen brief, §4) · de kathode-vertakking naar
   诸暨/Zhejiang (§4 rij 5).

**⚠️ Een gereedschapsles die de kaart raakt, en die vóór deze ronde niet bestond.** Een router
kan een been dat **korter is dan zijn eigen knoop-korrel** niet leggen: `maak_stroombeen_weg.py`
routeert over de OSM-way-vertices, en op een way met 5 vertices over 2.250 m eindigde het
fase-D-been in een **overschiet-en-terug** van 792 m heen en 179 m terug (1,01 km, +29,0%). Dat
is dezelfde klasse als de grafiet-via-punten van 2026-08-05, maar dan op het **EINDpunt** van een
been. Gebruik daar **`v2/tools/knip_osm_been.py`** — één way, twee ankers, géén routering, de
geometrie nog steeds uit OSM en niet uit een oog (de Tongling-regel) — en lees de verhouding
**pad ÷ hemelsbreed** die dat tool zelf rapporteert (hier **1,08**). Zonder die maat passeert een
overschiet-en-terug stil.

## 8 · Toets-checklist

- [x] **Notatie:** alle coördinaten lat, lon met decimale punt; ankers op 5 decimalen
      *(lon/lat-regels uit de oude versie gecorrigeerd: het Beilun-bandpunt in §6 en het
      Guixi-eindpunt in §7 stonden als lon/lat)*
- [x] Elk been heeft een **been-id** (`b1`–`b6`) in déze brief; ankers dragen waar mogelijk het
      `aansluitingen.json`-id. ⚠️ **In de gebakken data ontbreken de been-ids nog** → §5.13
- [ ] Elke laadplek, overslag en losplek **satelliet-gelegd** — fase A–C ✅ (concentrator z16 ·
      Coloso z17 ×3 · Beilun-losberth z16 · bandlandpunt z18 · **laadspoor 北仑港站 z19** ·
      losbundel z18); **fase D: beide registerpunten z18 ✅, maar de twee LAADPLEKKEN binnen die
      terreinen niet** (kathode-expeditie §5.5 · expeditiedeur walsdraad §5.8). **Blijft dus
      onafgevinkt** — een anker dat niet satelliet-gelegd is, is geen anker, ook niet onder druk
- [x] Elke laad-/los-/overslagplek heeft een ingevulde **productvraag** (§2a, ladders L1–L6)
      incl. uitsluitingen — stap 5/6 van L5 en de laaddeur van L6 staan open → §5
- [x] Elke overslag heeft **twee** ankers + terreinstappen — Coloso ✅; **Beilun ✅ sinds
      2026-08-05**: `cu-beilun-kade` (zee-only) + `cu-beilun-laadspoor` (spoor), met
      `cu-beilun-bandlandpunt` als terreinstap ertussen
- [x] **Routeerpunt + max snap** genoteerd bij elk been-uiteinde op water en spoor (b2: 85,1 /
      1,27 km · b3: **0,198** / 0,05 km) en op de interne as (b5: 43 m / 8 m); b6 n.v.t. — niet getekend
- [x] **Dekking:** been 3 gemeten — alle corridor-B-punten geraakt binnen 0,8–6,4 km (marge
      per punt 8 km, zie been-kop); been 5 loopt over de enige way die beide registerpunten
      raakt; fase E niet gerouteerd (wordt niet getekend)
- [x] **Verklikker:** been 3 raakt geen plaats die niet in de brief staat (corridor-A-punten
      gemeden: Hangzhou 87,4 km · Shaoxing 56,5 · Yuyao 45,9 · Zhuji 31,2); been 5 blijft
      binnen lat 28.3310–28.3325 en lon 117.2190–117.2256
- [x] **Gaten tussen de benen:** `0 · 0 · 0 · 0 · 0 · 0 · 0,198 · 0,584 km` — alle ≤ 0,5 km met
      precies **één benoemde uitzondering** (het procesgat bij 贵冶, §7 punt 7)
- [x] **Markers ≤ 1 m van de lijn**, alle zes, **punt-tot-segment** gemeten. ⚠️ Meng die maat
      niet met punt-tot-vertex: bij Guixi is dat 0,8 m tegen 48,9 m, en dat mengen wás een echte
      meetfout in een eerdere ronde
- [x] **`toets_knikken.py` gedift tegen de nulmeting:** 157 → **159** knikken ≥60°, omkeringen
      **25 (ongewijzigd)**, terugloop **3 (ongewijzigd, alle drie in `stroomroute-pilot`)**; de
      vier andere stromen **letterlijk ongewijzigd**. De twee nieuwe knikken zijn de haakse
      inrit-aansluitingen in been 5 (89,9° op `28.33188, 117.22545` en `28.33187, 117.21919`)
- [x] **Regressie op de andere wegprofielen:** `stroombeen-*.geojson` van
      `grafiet-balama-nacala`, `lithium-greenbushes-bunbury` en `grafiet-vidalia-lastmile`
      byte-identiek — `EIND_KLASSEN_DEFAULT` is niet geraakt (het corridor-id hasht hem mee)
- [x] Geen enkel **negatief anker** binnen zijn verbodsstraal geraakt (Yingtan 14,6 km ·
      Jingdezhen 98,5 · Nanchang 136,4) ✅
- [x] Lengte per been binnen tolerantie mét gereedschap + eindpunten + netstadium:
      **been 3 = 565,8 km** (gebakken been, `stroomroute-koper-escondida-guixi.json`,
      laadspoor 北仑港站 ↔ ertslosbundel 贵溪, netstadium 2026-07-29 OSM-spoor 1-op-1) tegen
      ~556 brief-corridor = **+1,8%**; **been 5 = 0,7 km** (`knip_osm_been.py` over OSM
      `way/1462532976`, registerpunt ↔ registerpunt, extract 2026-08-05) tegen de eigen
      vooraf-meting van 0,62 km = **−1,2%**, pad ÷ hemelsbreed **1,08**; been 1 alleen
      bronlengte (~170 km, geen geometrie — de getekende 153,5 km is de koorde)
- [ ] Volumes sluiten over de knopen — plausibel (1,10 mln t kathode ≥ 0,37 mln t eigen
      walsdraad + ~2/3 markt; ~3 mln t spoorafvoer incl. bijproduct) maar aandelen niet hard → §5.9
- [x] Elke stippellijn draagt een **reden** (b1 eigen verbinding · Coloso-aanloop geen AIS ·
      Beilun-aanloop MARNET-knoop in de geul · transportband + ertsveld eigen terrein · b4
      OSM-gat hand-geplaatst). ⚠️ **Been 5 draagt bewust GÉÉN stippel** — het net reikt tot op
      8 m, en een stippel betekent uitsluitend *hier reikt het net niet* (werkwijze §7)
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
Guixi beide **江西省贵溪市冶金大道15号**; 铜材公司 opgericht 2002-03-22. ⚠️ **Dat huisnummer
is het HOOFDKANTOORADRES** van groep, beursvennootschap en 加工事业部; het *productie*adres is
19号 [D12]. De collocatie-conclusie die deze brief uit D3 trok blijft staan, de onderbouwing via
nummer 15 niet · D4 zh.wikipedia
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

**Fase D — ankerbronnen [D12..] (ronde 2026-08-05):**
D12 **Nationaal emissievergunningregister, Ministerie van Ecologie en Milieu** —
`permit.mee.gov.cn` V3.0, endpoint `/perxxgkinfo/syssb/xkgg/xkgg!licenseInformation.action`
(⚠️ het oude pad uit `zoek-chinees-adres-recept.md` is **dood**). Vergunning
**913600007363561816001Q** (江西铜业铜材有限公司, 行业类别 铜压延加工) → verborgen HTML-velden
`longitude=117.21919` / `latitude=28.33180` + `opelngd 117/13/9.08` / `opelatd 28/19/54.48`;
vergunning **91360000X12430120H001P** (江西铜业股份有限公司贵溪冶炼厂, 铜冶炼) → 28.33227,
117.22545. Beide met `生产经营场所地址` = 冶金大道 **19号**. Vergunning-PDF's via
`xkgg!downloadFile.action?fileType=fbfile` (het `正本`; het `副本` rendert leeg) ·
D13 **赣环监字（2017）第S007号** (provinciaal EIA-toezichtstuk, jxcc.com, 67 p.) — §2.1.1
«地理坐标为东经117.225156，北纬28.329914» = **28.32991, 117.22516**, een **tweede, onafhankelijke**
officiële coördinaat van hetzelfde terrein (kruiscontrole op datum én terreingeometrie);
fig. 3-1 tekent de interne 物流主轴线; p.11 verdeelt het 198,26 ha-terrein in 老厂区 · 新厂区 ·
新产业公司 · **铜材公司** · 新材料车间 · 铜达公司 en plaatst 一车间 (anodeslijk/edelmetaal) in de
noordoosthoek · D14 **CSRC-toezichtstuk / prospectus 江铜铜箔** — definieert 江铜华东铜材 als
**江铜华东（浙江）铜材有限公司**, 浙江省诸暨市陶朱街道迎宾路2号厂房 (508,2 km), 委托加工-keten
JCC-**kathode** → 铜材 → draad → Nanchang; 加工服务 van 江西铜业铜材 1,94 / 9,26 / 9,19 /
7,97 万元 per jaar · D15 **zh.wikipedia 北仑港站** — 29°55′35,5″N 121°52′23,1″E; 北极星路178号,
10,9 ha, 2 货场 / 10 装卸线, 78万TEU/j, 中铁联合国际集装箱宁波北仑 · D16 **OpenStreetMap (ODbL)**
— `way/1462532976` (`highway=service`, 2.250 m, 5 vertices, geen access-tag; de interne hoofdas
闪速大道) · `way/1491021972` (laadspoor 北仑港站, 4,5 m van het anker) · `way/995766131`
(`access=private`, loopt het smelterhart in — per constructie uitgesloten) ·
D17 **Esri World Imagery z17–z19** (2026-08-05). ⚠️ Bij Guixi bestaat **z19 niet**: z19/z20
leveren exact 2.521 byte placeholder, en Wayback-release 64001 is identiek aan live — een
**zoomplafond**, geen opnamedatum-probleem.

**Eigen metingen:** satelliet-overlay Esri World Imagery z15–z19 (2026-07-28 / 2026-08-05) ·
`toets_spoorroute.mjs` (corridortoets, netstadium 2026-07-28) · `toets_corridor.py` ·
`knip_osm_been.py` (been 5: 0,7 km, pad ÷ hemelsbreed 1,08) · `toets_knikken.py` (159/25/3) ·
`maak_aansluitingen.py` (27 aansluitingen, 25 bestaande op 0,0 m) · meting aan het gebakken
`v2/data/stroomroute-koper-escondida-guixi.json` (9 benen · 19.826,6 km · 3.233 punten ·
6 markers · gaten `0 · 0 · 0 · 0 · 0 · 0 · 0,198 · 0,584 km` · markers ≤ 1 m punt-tot-segment).
