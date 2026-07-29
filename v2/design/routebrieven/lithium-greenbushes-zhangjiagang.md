# Routebrief · Lithium — Greenbushes (AU) → batterijcel → Tesla Giga Shanghai (CN)

**stroom-id:** `lithium-greenbushes-zhangjiagang`  ·  **geschreven:** 2026-07-29  ·  **status brief:** concept
**Keten in één zin:** spodumeenconcentraat SC6.0 uit de Greenbushes-mijn gaat per truck 90 km over de South
Western Highway naar Bunbury Berth 8, per bulkcarrier over zee de Yangtze op tot Zhangjiagang, per truck de
bonded zone in naar de lithiumfabriek van Tianqi, als batterijkwaliteit carbonaat/hydroxide naar de
kathodefabriek van LG Chem in Wuxi, als kathodepoeder naar de celfabriek van LG Energy Solution in Nanjing,
en als 2170-cel naar Tesla Giga Shanghai.

*Volgens `../routebrief-werkwijze.md`. De brief loopt door tot het EINDPRODUCT — hij stopt niet
bij carbonaat/hydroxide. Elk been draagt dezelfde bewijslast, ook het laatste.*

*Doel: **zelfverificatie**. **Notatie (hard):** coördinaten altijd **lat, lon** met **decimale punt**;
ankers 5 decimalen, passages 2–4. Elk been heeft een **been-id** `lithium-greenbushes-zhangjiagang-b<n>`,
hier afgekort tot `li-gz-b<n>`.*

---

## 1 · Ketenkaart

```
Greenbushes concentraatloods            ──(b1 truck, terrein)──►  mijnpoort South Western Hwy
  li-gb-laadplek                          ──(b2 truck, 90 km)──►  Bunbury Berth 8
                                                                    ├ losplek: Shed 8-8 (li-bun-loods)
                                                                    └ laadplek: scheepslader (li-bun-berth8)
  ├── vertakking bij de mijn: Albemarle-deel (≤50%) → Kemerton / Meishan / Xinyu → eigen brief
  ├── alternatief been 2: Fremantle i.p.v. Bunbury (aandeel onbekend)

Bunbury  ──(b3 zee, ±8.300 km)──►  Yangtze-monding (Wusong)
         ──(b4 Yangtze, ±130 km)──►  Zhangjiagang, droge-bulkkade    li-zjg-kade
                                    ──(b5 truck, ±4 km)──►  Tianqi Lithium (Jiangsu), 东新路 5   li-zjg-tianqi
                                        [verwerkingsknoop: 110 kt spodumeen → 17 kt Li2CO3 (+30 kt LiOH)]
  ├── vertakking: carbonaat naar 德方纳米 (LFP-kathode) → eigen streng, eigen brief

                                    ──(b6 weg, ±70 km)──►  LG Chem kathodefabriek Wuxi   li-wx-lgchem
                                        [verwerkingsknoop: LiOH/Li2CO3 → NCM-kathode, ±50 kt/j]
  ├── vertakking: deel van de Wuxi-kathode gaat naar LG ES Wrocław (PL) → eigen brief

                                    ──(b7 weg, ±180 km)──►  LG Energy Solution Nanjing   li-nj-lges
                                        [verwerkingsknoop: kathode → 2170-cel]
                                    ──(b8 weg, ±300 km)──►  Tesla Giga Shanghai, poort 3  li-sh-tesla
```

| | |
|---|---|
| **Fasen** | A mijn → zeehaven · B zee (incl. Yangtze) · C aanlanding → raffinaderij · D raffinaat → kathodefabriek · E kathode → cel → autofabriek |
| **Benen** | 8 (doorlopend genummerd `li-gz-b1` … `li-gz-b8`) |
| **Overslagen** | 4 (Bunbury · Zhangjiagang-kade · Tianqi-poort/fabriek · elke fabriekswissel D→E) |
| **Gedeelde benen** | geen — dit is de eerste lithiumbrief |
| **Vertakkingen** | bij de mijn (Albemarle-electie ≤50%) · bij Tianqi (LFP-carbonaat naar 德方纳米) · bij Wuxi (kathode naar Wrocław) |
| **Reële alternatieven** | been 2/3: **Fremantle** als exporthaven naast Bunbury (SEC-formulering "Bunbury or Fremantle", aandeel onbekend) |

## 2 · Productvormen per fase — wat beweegt er fysiek

| fase | product | vorm / verpakking | gehalte of specificatie | omzetting in de volgende stap | jaarvolume |
|---|---|---|---|---|---|
| A | spodumeenconcentraat SC6.0 | droge bulk, los gestort in afgedekte roadtrain-kippers | min. **6,0 % Li2O** (chemical grade); daarnaast technical grade | → scheepsruim | **1,5 Mt/j** over de weg Greenbushes→Bunbury (groeit naar 2,1 Mt/j) |
| B | idem | droge bulk in scheepsruim | idem | → kade-stock China | Bunbury is 's werelds grootste lithium-exporthaven |
| C | idem | droge bulk, op het terrein per **transportband** | idem | → 17 kt Li2CO3 | **110.000 t/j** ingaand bij Tianqi Jiangsu |
| D | batterijkwaliteit **lithiumcarbonaat** (en sinds 09-2025 **-hydroxide**) | zakken/big bags op pallet, container of gesloten truck | battery grade | → NCM-kathodepoeder | 17.000 t/j Li2CO3 + 30.000 t/j LiOH |
| E | **NCM-kathodepoeder** | big bags, gesloten truck | high-nickel NCM | → 2170-cel | ±40–50 kt/j kathode (Wuxi) |
| E | **2170-cilindercel** | trays in zeecontainer/truck | 5.300 mAh (Model Y) | → accupakket in de auto | n.b. |

> **Volumecontrole over de knoop:** 110.000 t spodumeen → 17.000 t carbonaat = **6,47 t concentraat per t
> Li2CO3**. Dat is de goede orde voor SC6.0 (theoretisch ±5,3 bij 100 % rendement; de industrie rekent
> 6,5–8). De keten is dus intern consistent: één Handysize-lading van ±30 kt dekt ruwweg een kwartaal
> Tianqi-productie, en Greenbushes' 1,5 Mt/j is ruim 13× het jaarverbruik van deze ene fabriek — de mijn
> voedt méér strengen dan deze (zie §4).

### 2a · De productvraag — van product naar kade

**(1) Laadplek op de mijn — Greenbushes**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Welk product, welke vorm? | Droog concentraatpoeder/zand, los gestort; wordt afgedekt vervoerd (stofklasse) |
| 2 | Welke soort faciliteit? | Overdekte concentraatloods met shovel- of silobelading + weegbrug, aan een truckloop |
| 3 | Welke partijen ter plaatse? | Talison Lithium (Tianqi/IGO 51/49 via TLEA + Albemarle 49 %) is de enige operator op het terrein |
| 4 | Welke hoort bij déze stroom? | Dezelfde loods bedient álle afnemers; de streng splitst pas ná de kade (Albemarle-electie) |
| 5 | Welke plek precies? | De overdekte opslag met aangrenzende truckloop aan de zuidwestkant van het plantcomplex |
| 6 | Coördinaat + satellietbevestiging | **−33.86495, 116.05505** — Esri z18 (z19 niet beschikbaar), 2026-07-29: overdekte loods NE-SW, hardstand, aansluitende truckloop |

**Wat de productvorm UITSLUIT:** dit is géén containerlading en géén stukgoed — dus geen containerterminal,
geen ro-ro, geen kraankade. En het is géén slurry: er ligt geen leiding, de mijn heeft een wegverbinding
(zie kernfeit 1).

**(2) Losplek + laadplek in Bunbury**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Welk product, welke vorm? | Droge bulk, ±1,5 Mt/j, aangevoerd per truck |
| 2 | Welke soort faciliteit? | Bulkopslagloods met inload-band (500 t/h) → outload (2.000 t/h) → **scheepslader** aan een bulkberth |
| 3 | Welke partijen ter plaatse? | Southern Ports (havenbeheer) · Talison (eigen loods) · Alcoa en Worsley (alumina, eigen laders) · Bunge/CBH (graan) |
| 4 | Welke hoort bij déze stroom? | Talison's eigen **Shed 8-8** (55.000 t, €/AU$ 26,4 mln, bouwer Kerman) + de **Berth 8-scheepslader** — de enige combinatie in de haven die spodumeen laadt |
| 5 | Welke kade? | **Berth 8**, binnenhaven, 250 m, 11,6 m diepgang, scheepslader tot 2.000 t/h |
| 6 | Coördinaat + satellietbevestiging | kade **−33.31995, 115.66385** — Esri z18: bulkcarrier langszij mét scheepslader op de kade. ⚠️ De **loods** is op deze capture níet zichtbaar (opname ouder dan de bouw) → §5 |

**Wat de productvorm UITSLUIT:** niet de houtsnipper-/graankade aan de zuidwestzijde (Berth 3, eigen
transportbandsysteem), en niet de alumina-dolfijnen van Alcoa/Worsley (Berth 4/6, gesloten
alumina-laadsysteem). Dit zijn dus **negatieve ankers**, zie been 2.

**(3) Losplek in Zhangjiagang**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Welk product, welke vorm? | Droge bulk uit het scheepsruim, ±110 kt/j voor déze fabriek |
| 2 | Welke soort faciliteit? | Rivierkade met grijperkranen en open/overdekte stockyard — géén chemie-jetty (die is voor vloeistof) |
| 3 | Welke partijen ter plaatse? | Zhangjiagang-havenbedrijven in en om de bonded port area; het chemiepark heeft eigen **vloeistof**-steigers |
| 4 | Welke hoort bij déze stroom? | Nog niet vastgesteld — de bedrijfsdocumentatie zegt alleen dat de fabriek "毗邻海运码头" (grenst aan zeekades) ligt |
| 5 | Welke kade? | **Kandidaatgebied vastgesteld**: de doorgaande kade van de hoofdhaven Zhangjiagang, ±31.970–31.975 / 120.410–120.440 (portaalkranen, stapelvelden, ±6 km van de fabriek). **Niet** het chemiepark bij de fabriek zelf: daar staan alleen T-steigers voor vloeistof |
| 6 | Coördinaat + satellietbevestiging | kandidaat **31.97200, 120.42000** — Esri z15: doorgaande kade met kranen en stapelvelden. **Nog niet op z16 gelegd op een specifieke ligplaats** → §5 |

**Wat de productvorm UITSLUIT:** de T-vormige steigers van het chemiepark (vloeibare bulk, leidingtrestle,
geen stockyard) en de containerterminals. Een grijperkade met stockyard is visueel eenduidig; die moet dus
gevonden worden op een nieuwere opname.

**(4) Losplek fabriek — Tianqi Lithium (Jiangsu)**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Welk product? | Spodumeenconcentraat in, batterijkwaliteit carbonaat/hydroxide uit |
| 2 | Welke soort faciliteit? | Chemische fabriek met ertsopslag (max. 20.000 t), **transportband** als intern transport, zwavelzuurtanks |
| 3 | Welke partijen? | 天齐锂业（江苏）有限公司 — voorheen 银河锂业（江苏） (Galaxy Lithium Jiangsu), overgenomen 2015 |
| 4 | Welke hoort bij déze stroom? | Dezelfde: dit is Tianqi's enige lithiumchemie-basis aan de Yangtze-delta en hij draait op Greenbushes-concentraat |
| 5 | Welk adres? | **扬子江国际化学工业园东新路 5 号**, Zhangjiagang bonded zone; terrein 96.533 m²; buren: oost 江苏国泰超威新材料, west 双狮(张家港)精细化工, zuid 凯凌化工(张家港), noord het dorp 北荫村 |
| 6 | Coördinaat + satellietbevestiging | **nog te leggen op z16** (§5); 东新路 loopt volgens OSM tussen 32.0121, 120.4566 en 32.0152, 120.4677 |

**Wat de productvorm UITSLUIT:** de fabriek ligt volgens haar eigen calamiteitenplan mét een dorp aan de
noordzijde — dus **niet** direct aan de rivieroever. Er is dus een echte last mile tussen kade en poort;
een rechte stub van kade naar fabriek zou fout zijn.

**(5) Losplek fabriek — kathode, Wuxi**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Welk product? | Lithiumhydroxide/-carbonaat in (gepalletiseerd), **ternair (NCM) kathodepoeder** uit |
| 2 | Welke soort faciliteit? | Kathodefabriek: gesloten menglijnen, calcineerovens, droge ruimtes — geen bulkopslag |
| 3 | Welke partijen? | **乐友新能源材料（无锡）有限公司** — JV van LG Chem en Huayou Cobalt (华友钴业), opgericht 29-06-2018, geplaatst kapitaal US$ 285,4 mln |
| 4 | Welke hoort bij déze stroom? | LG Chems enige kathodefabriek in China; het contract Tianqi–LG Chem loopt 2023–2026 |
| 5 | Welk adres? | **无锡市新吴区锡梅路 167 号** (Ximei Road 167, Xinwu-district, Wuxi) |
| 6 | Coördinaat + satellietbevestiging | **nog te leggen** — 锡梅路 loopt volgens OSM van 31.5426, 120.4051 tot 31.5135, 120.4914; huisnummers staan niet in OSM (§5) |

### 2b · De overslagregel

Vier drager-wissels, elk **twee ankers**:

| # | plaats | been in → uit | aankomstanker | vertrekanker |
|---|---|---|---|---|
| 1 | Bunbury | b2 truck → b3 zeeschip | Shed 8-8 (losplek truck) | Berth 8 scheepslader (laadplek schip) |
| 2 | Zhangjiagang | b4 zeeschip → b5 truck | droge-bulkkade (losplek schip) | stockyard/laadplek truck |
| 3 | Tianqi-terrein | b5 truck → verwerking | fabriekspoort/losplek | laadplek uitgaand product |
| 4 | Wuxi / Nanjing | b6→b7 en b7→b8 | fabriekspoort | fabriekspoort |

**Anker ≠ routeerpunt.** Bij Bunbury ligt het anker op de kade en het routeerpunt in de vaargeul van de
binnenhaven (verwachte snap ≤ 300 m). Bij Zhangjiagang idem: de rivierkade tegen een vaargeul die 1–2 km
breed is, dus daar hoort een ruimere maximale snap (≤ 1.500 m) dan aan een binnenhavenkade.

## 3 · Kernfeiten die de vorm van de keten bepalen

1. **Er is géén spoor, en dat is onderzocht en verworpen.** Er ligt 78 km buiten gebruik gestelde
   spoorlijn Greenbushes–Bunbury; de gezamenlijke haalbaarheidsstudie (Talison + WA-regering, uitkomst
   gepubliceerd door Talison) vond geen technische blokkade maar wel dat 38 km volledig vernieuwd moet
   worden, met 76 overwegen en 17 voetgangersoversteken, en dat trucks hoe dan ook de first/last mile
   blijven doen — *"not economically feasible at this time"*. **Het been is dus truck, en dat is een
   besluit, geen aanname.** [T1, T2]
2. **De weg is de flessenhals, en hij is meetbaar:** 1,5 Mt/j tussen mijn en haven ≈ **135
   truckbewegingen per dag** over de South Western Highway, groeiend naar ±200/dag (>70.000 per jaar) bij
   2,1 Mt/j. Donnybrook noemt dat expliciet als knelpunt. [T3]
3. **Bunbury is 's werelds grootste lithium-exporthaven** (Port Hedland tweede, Esperance derde), aldus
   Southern Ports zelf in de PCCC-notulen van 09-08-2023 — hetzelfde document dat de **Berth 8-scheepslader**
   noemt en bevestigt dat Southern Ports meedoet in Talisons spoorstudie. [S1]
4. **De fabriek in Zhangjiagang draait op Greenbushes-erts** en is klein t.o.v. de mijn: 110.000 t
   spodumeen in, 17.000 t batterijkwaliteit carbonaat uit, bijproduct 51.062 t natriumsulfaat; sinds
   **25-09-2025** staat er een tweede lijn van 30.000 t/j lithiumhydroxide naast (investering ±1,8 mrd
   RMB). [Q1, Q2]
5. **De keten na het raffinaat is documenteerbaar tot in de auto.** LG Chem's kathodefabriek in Wuxi
   (opgestart eind 2019, ±40–50 kt/j) levert **zijn volledige volume** aan LG Energy Solution in Nanjing
   en Wrocław; Tesla is de belangrijkste klant van de Nanjing-fabriek en de daar gemaakte 2170-cellen gaan
   naar **Giga Shanghai**. [L1, L2, L3]
6. **De mijn voedt meer strengen dan deze.** Albemarle mag jaarlijks **tot 50 %** van de productie
   afroepen (naar Kemerton/Meishan/Xinyu); de rest gaat via TLEA naar Tianqi. Deze brief beschrijft
   uitsluitend de Tianqi-streng. [A1]

---

# FASE A · Greenbushes → Bunbury

## Been 1 · truck (terrein) — concentraatloods → mijnpoort

**been-id:** `li-gz-b1`
**Modaliteit:** truck (roadtrain), terreinweg
**Lengte:** geschat 1,5–2,5 km — te meten bij de wegcorridor-run
**Net / bron geometrie:** OSM-wegcorridor (kleine wegklassen meenemen binnen 12 km, werkwijze §3.4)
**Stippel:** nee
**Corridor bij naam:** terreinwegen Talison → aansluiting South Western Highway
**Routeerpunt kop / staart:** −33.86495, 116.05505 · nog te bepalen — max snap 200 m
**Toets-marge:** 100 m kop/staart

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **Concentraatloods / load-out** | laadplek | −33.86495, 116.05505 | eigen satellietpass z18 + [C1] | **satelliet-gelegd** |
| 2 | ±0,3 | Weegbrug / terreinlus | verwerkingsstap | — | — | onzeker |
| 3 | ±1,5 | **Mijnpoort op de South Western Highway** | poort | ±−33.8620, 116.0530 | afgeleid uit de tegels | onzeker |

**Opmerkingen been 1.** De loods is op de stitch herkend aan de **vorm** (overdekte opslag + hardstand +
truckloop), niet aan een label: Talison publiceert geen terreinplattegrond. Onafhankelijke steun: de
corridor `li-greenbushes-kemerton` in `v2/tools/fetch_landnet.py` begint op (−33.86455, 116.05406) — dat
ligt **102 m** van dit anker, dus twee onafhankelijke keuzes komen op dezelfde plek uit. De poort is nog
niet gelegd; die valt bij de eerste wegcorridor-run vanzelf op het punt waar de terreinweg de highway raakt.

**Negatieve ankers been 1:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| Open put / afgraving | −33.8560, 116.0620 | 0,5 km | een laadplek ligt nooit ín de put (de Escondida-fout van 28-07) |
| Tailings storage facility | −33.8690, 116.0560 | 0,4 km | afvalberging, geen product |

## Been 2 · truck — Greenbushes → Bunbury Berth 8

**been-id:** `li-gz-b2`
**Modaliteit:** truck (roadtrain), openbare weg
**Lengte:** gepubliceerd **±90 km** (mijn ligt "90 km southeast of the port of Bunbury") — te meten
**Net / bron geometrie:** OSM-wegcorridor
**Stippel:** nee
**Corridor bij naam:** **South Western Highway** (toegang tot de mijn loopt volgens Talison via de
verharde South Western Highway tussen Bunbury en Bridgetown, en via Maranup Ford Road naar de mijn)
**Routeerpunt kop / staart:** mijnpoort · havenpoort — max snap 200 m
**Toets-marge:** default 2 km op passages; de plaatsknopen liggen ín de dorpen die de weg doorkruist

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | Mijnpoort South Western Highway | poort | ±−33.8620, 116.0530 | [C1] | onzeker |
| 2 | ±1,5 | **Greenbushes** (dorp, mijn ligt eraan vast) | passage | −33.8494, 116.0596 | OSM place=town | **bevestigd** |
| 3 | ±9 | **Balingup** | passage | −33.7861, 115.9832 | OSM + corridorvia [C1] | **bevestigd** |
| 4 | ±15 | **Mullalyup** | passage | −33.7431, 115.9452 | OSM place=village | **bevestigd** |
| 5 | ±20 | **Kirup** | passage | −33.7058, 115.8927 | OSM place=town | **bevestigd** |
| 6 | ±25 | Newlands | passage | −33.6681, 115.8765 | OSM place=village | aannemelijk |
| 7 | ±36 | **Donnybrook** | passage | −33.5774, 115.8251 | OSM + [T3] (klachten over truckbewegingen) | **bevestigd** |
| 8 | ±53 | **Boyanup** | passage | −33.4844, 115.7289 | OSM + corridorvia [C1] | **bevestigd** |
| 9 | ±73 | **Picton** (aansluiting havengebied Bunbury) | kruising | −33.3525, 115.6941 | OSM place=suburb | aannemelijk |
| 10 | ±85 | Vittoria (haven-industriegebied) | passage | −33.3202, 115.6734 | OSM place=suburb | aannemelijk |
| 11 | ±90 | **Havenpoort Bunbury binnenhaven** | poort | nog te leggen | — | onzeker |
| 12 | ±91 | **Shed 8-8 — losplek truck** | losplek | nog te leggen (§5) | [K1, S1] | **aannemelijk** |

**Opmerkingen been 2.** Punten 2–8 liggen op één rechte streng langs de South Western Highway; er is maar
één plausibel pad doorheen. Het laatste stuk (Picton → havenpoort) is de **last mile** en is bewust
niet als rechte stub genoteerd: de havenweg moet uit OSM komen (werkwijze §3.4).

**Negatieve ankers been 2** — mét coördinaat + verbodsstraal:

| punt | lat, lon | straal | reden |
|---|---|---|---|
| **Bridgetown** | −33.9575, 116.1350 | 5 km | ligt zuidoostelijk van de mijn: de haven ligt de andere kant op |
| **Kemerton (Albemarle)** | −33.20850, 115.75797 | 5 km | andere streng (Albemarle-electie), geen exporthaven |
| **Kwinana (TLEA)** | −32.21468, 115.77858 | 10 km | andere streng; ook Tianqi, maar hydroxide in Australië |
| **Berth 3 (houtsnippers/graan)** | −33.3235, 115.6590 | 0,4 km | eigen bandsysteem voor snippers/graan; past niet bij deze productvorm |
| **Alcoa/Worsley alumina-dolfijnen** | −33.3210, 115.6655 | 0,4 km | gesloten alumina-laadsysteem, geen spodumeen |

**Reëel alternatief been 2/3:**

| punt | lat, lon | aandeel | reden |
|---|---|---|---|
| **Fremantle** | −32.0430, 115.7400 | onbekend | Albemarle's technisch rapport noemt de export via "Bunbury **or** Fremantle" — dus een deel van het volume vertrekt daar; welk deel is niet gepubliceerd |

## Overslag been 2 → been 3 — Bunbury binnenhaven

**Productvraag:** droge bulk in een bulkopslagloods → outload-band → scheepslader aan een bulkberth; dus
Shed 8-8 + Berth 8, niet de graan-/snipper- of aluminakades (§2a-2).

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst been 2 | **Shed 8-8** (55.000 t, inload 500 t/h) | losplek | nog te leggen (§5) | [K1, S1] | aannemelijk |
| 2 | terrein | outload-band 2.000 t/h → scheepslader | verwerkingsstap | — | [K1] | **bevestigd** |
| 3 | vertrek been 3 | **Berth 8 — scheepslader / ligplaats** | laadplek | **−33.31995, 115.66385** | eigen satellietpass z18 + [S1, S2] | **satelliet-gelegd** |

**Routeerpunt ≠ anker.** Routeerpunt in de binnenhavengeul ±−33.31930, 115.66230; afstand tot het
kade-anker ±160 m. Verwachte maximale snap 300 m.

⚠️ **Wat hier niet klopt en waarom het genoteerd staat:** op de huidige Esri-opname van Bunbury is Shed 8-8
**niet te zien** — het terrein NW van de berth ligt er nog braak bij. De loods is later gebouwd dan de
opname. Dit is een **nieuwe faalwijze van de satellietregel**: een pass kan niet alleen falen omdat het
punt fout is, maar ook omdat de *opname ouder is dan de infrastructuur*. Zie §5.

---

# FASE B · zee (incl. de Yangtze)

## Been 3 · zee — Bunbury → Yangtze-monding

**been-id:** `li-gz-b3`
**Modaliteit:** bulkcarrier (Handysize/Supramax; Berth 8 geeft 250 m × 11,6 m als bovengrens)
**Router:** zee = **vrij geroutet** (werkwijze §6)
**Lengte:** grootcirkel **7.229 km**; verwachte gerouteerde lengte 8.000–8.500 km (verhouding ±1,15) — te meten
**Routeerpunt kop / staart:** −33.31930, 115.66230 · 31.4000, 121.5000 — max snap 2 km

| # | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|
| 1 | **Berth 8, Bunbury** | laadplek | −33.31995, 115.66385 | eigen pass | **satelliet-gelegd** |
| 2 | Straat Lombok | passage (sanity) | −8.75, 115.75 | atlas-knelpunt `wp-lombok`; standaardroute voor diepgeladen bulk uit SW-Australië | aannemelijk |
| 3 | Straat Makassar | passage (sanity) | −2.50, 118.00 | atlas-knelpunt `wp-makassar` | aannemelijk |
| 4 | Zuid-Chinese Zee | passage (sanity) | 15.00, 114.00 | atlas-knelpunt `wp-scs` | aannemelijk |
| 5 | Straat Taiwan | passage (sanity) | 24.50, 119.50 | atlas-knelpunt `wp-taiwan` | aannemelijk |
| 6 | **Yangtze-monding bij Wusong/Baoshan** | overslag (vaarweg-overgang) | 31.4074, 121.4848 | OSM place=city Baoshan | **bevestigd** |

**Negatieve ankers been 3:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| **Yangshan diepzeehaven** | 30.6300, 122.0600 | 20 km | containereiland; droge bulk lost daar niet |
| **Port Hedland** | −20.3100, 118.5800 | 30 km | Pilbara-lithium (Pilgangoora/Wodgina), niet Greenbushes |

**Reëel alternatief been 3:** Straat Soenda (−5,95, 105,90) in plaats van Lombok — korter maar ondieper;
aandeel onbekend, daarom als alternatief genoteerd en niet als negatief anker.

## Been 4 · Yangtze — monding → Zhangjiagang

**been-id:** `li-gz-b4`
**Modaliteit:** hetzelfde zeeschip (géén drager-wissel; Zhangjiagang is zeehaven aan de rivier)
**Brief-gestuurd** (werkwijze §6: binnenwater niet vrij routeren)
**Lengte:** ±130 km — te meten op de MARNET-bulklaag met `maak_rivierbeen.py`
**Stippel:** nee — deze stretch heeft gebakken riviergeometrie (dezelfde bulklaag als Shanghai→Tongling)
**Routeerpunt kop / staart:** 31.4000, 121.5000 · nog te bepalen — max snap 1.500 m

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | Wusongkou / Baoshan | vaarweg-overgang | 31.4074, 121.4848 | OSM | **bevestigd** |
| 2 | ±35 | Taicang (stad) | referentie (niet aan lijn) | 31.4590, 121.1265 | OSM place=city | **bevestigd** |
| 3 | ±90 | Changshu (stad) | referentie (niet aan lijn) | 31.6500, 120.7500 | OSM, bij benadering | aannemelijk |
| 4 | ±130 | **Zhangjiagang — droge-bulkkade (kandidaat)** | losplek | 31.97200, 120.42000 | eigen satellietpass z15 + [Q3] | **onzeker** |

⚠️ **Punt 2 en 3 zijn oriëntatiepunten, geen dekkingspunten.** Taicang en Changshu liggen als stad
10–25 km ten zuiden van de vaargeul; wie ze als passage in de dekkingstoets zet, keurt een correcte route
af. De vaargeul zelf levert de punten zodra het rivierbeen gebakken is (dan komen de havensecties
Taicang-haven en Changshu-haven er als échte passages bij).

**Negatieve ankers been 4:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| **Jiangyin** | 31.9216, 120.2809 | 10 km | ligt stroomopwaarts vóórbij Zhangjiagang: te ver gevaren |
| Chemiesteigers Yangzijiang-chemiepark | 32.0110, 120.4525 | 0,6 km | vloeistofsteigers met leidingtrestle; droge bulk lost daar niet |

---

# FASE C · aanlanding → raffinaderij

## Been 5 · truck (last mile) — kade → Tianqi-poort → losplek

**been-id:** `li-gz-b5`
*Eigen been, geen rechte stub (werkwijze §3.4). Kleine wegklassen tellen mee binnen ±12 km.*
**Lengte:** ±3–5 km — te meten
**Stippel:** nee, mits de kade gevonden is; anders gestippeld **mét reden**

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | Kade / stapelveld Zhangjiagang (kandidaat) | losplek | 31.97200, 120.42000 | eigen satellietpass z15 | **onzeker** |
| 2 | | 东新路 (Dongxin Road) | passage | 32.0121, 120.4566 | OSM way 432043510 | **bevestigd** |
| 3 | | **Poort Tianqi Lithium (Jiangsu), 东新路 5** | poort | nog te leggen (§5) | [Q1] | aannemelijk |
| 4 | | **Ertsopslag op het terrein** (max. 20.000 t, band) | losplek | nog te leggen | [Q1] | aannemelijk |

## Verwerkingsknoop · Tianqi Lithium (Jiangsu) — 天齐锂业（江苏）有限公司

| | |
|---|---|
| **anker-id** | `li-zjg-tianqi` (nieuw; nog niet in `aansluitingen.json`) |
| **eigenaar van dit anker** | deze brief |
| **adres** | 扬子江国际化学工业园东新路 5 号, Zhangjiagang bonded zone · terrein 96.533 m² · 226 medewerkers |
| **buren (四至)** | oost 江苏国泰超威新材料 · west 双狮(张家港)精细化工 · zuid 凯凌化工(张家港) · noord dorp 北荫村 |
| **in** | spodumeenconcentraat **110.000 t/j** (max. opslag 20.000 t), zwavelzuur 38.000 t/j, soda 32.000 t/j |
| **andere ingaande strengen** | mogelijk concentraat uit andere Talison-verschepingen; niet uitgesplitst |
| **uit** | batterijkwaliteit **Li2CO3 17.000 t/j**; sinds 25-09-2025 daarnaast **LiOH·H2O 30.000 t/j** |
| **uitgaande strengen** | deze brief (hydroxide → LG Chem) · LFP-carbonaat → 德方纳米 (eigen brief) · overige klanten |
| **verlies / bijproduct** | natriumsulfaat **51.062 t/j** |
| **historie** | gebouwd als 银河锂业（江苏） (Galaxy Lithium Jiangsu), 2015 door Tianqi overgenomen |

---

# FASE D · raffinaat → kathodefabriek

## Been 6 · weg — Zhangjiagang → LG Chem Wuxi

**been-id:** `li-gz-b6`
**Modaliteit:** truck (gesloten, gepalletiseerd) · **Lengte:** ±70 km — te meten
**Stippel:** nee
**Routeerpunt kop / staart:** poort Tianqi · poort LG Chem Wuxi — max snap 200 m

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | Laadplek Tianqi (uitgaand product) | laadplek | nog te leggen | [Q1] | aannemelijk |
| 2 | ±25 | Zhangjiagang stad | passage | 31.8783, 120.5515 | OSM place=city | **bevestigd** |
| 3 | ±70 | **乐友新能源材料（无锡）— LG Chem/Huayou kathodefabriek**, 锡梅路 167 号, Xinwu, Wuxi | losplek | nog te leggen (§5) | [L1, L4, L5] | **aannemelijk** |

**Waarom déze fabriek** (de zwakste schakel van de brief, expliciet):
* Tianqi's dochter (成都天齐) heeft een **lopend leveringscontract met LG Chem voor lithiumhydroxide,
  01-01-2023 t/m 31-12-2026** [L4]; volumes en leverfabriek zijn niet gepubliceerd.
* LG Chem's enige Chinese kathodefabriek staat in **Wuxi**, ±70 km van Zhangjiagang, en verwerkt
  hydroxide tot high-nickel NCM [L1].
* Tianqi's **hydroxide**-lijn in Zhangjiagang draait pas sinds 25-09-2025 [Q2]; vóór die datum kwam
  Tianqi-hydroxide uit Kwinana of Shehong. Deze streng beschrijft dus expliciet de **situatie ná
  september 2025**.
⚠️ Het contract is bedrijfs-naar-bedrijf, niet fabriek-naar-fabriek. Dit been is daarom **aannemelijk**,
niet bevestigd, en staat als eerste in §5.

**Negatieve ankers been 6:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| Shanghai-havengebied | 31.2300, 121.4800 | 15 km | binnenlands wegtransport hoeft niet via Shanghai |

## Verwerkingsknoop · LG Chem kathodefabriek Wuxi

| | |
|---|---|
| **anker-id** | `li-wx-lgchem` (nieuw) |
| **in** | lithiumhydroxide/carbonaat (deze streng) + nikkel-kobalt-mangaan-precursor (andere strengen, o.a. de JV met Huayou in Quzhou) |
| **uit** | NCM-kathodepoeder, ±40–50 kt/j |
| **uitgaande strengen** | **LG ES Nanjing** (deze brief) · **LG ES Wrocław** (eigen brief) — samen het volledige volume [L1] |
| **bijzonder** | de fabriek draait op ingekochte hernieuwbare stroom (140 GWh) — geen invloed op de lijn, wel op het verhaal |

---

# FASE E · kathode → cel → auto

## Been 7 · weg — Wuxi → LG Energy Solution Nanjing

**been-id:** `li-gz-b7` · **Modaliteit:** truck · **Lengte:** ±180 km — te meten

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | Laadplek LG Chem Wuxi | laadplek | nog te leggen | [L1] | aannemelijk |
| 2 | ±60 | Changzhou | passage | 31.8123, 119.9692 | OSM place=city | **bevestigd** |
| 3 | ±175 | Qixia (Nanjing Economic & Technological Development Zone) | passage | 32.0985, 118.9042 | OSM place=city | **bevestigd** |
| 4 | ±180 | **乐金化学新能源电池有限公司 — celfabriek, Nanjing NEDZ** | losplek | **32.16300, 118.87900** | OSM way 621624910 + eigen satellietpass z16 | **satelliet-gelegd** |

**⚠️ LG heeft twee campussen in Nanjing; deze brief kiest de New Port-campus, met reden:**

| campus | ligging | bron | status |
|---|---|---|---|
| **Qixia / New Port (NEDZ)** — 恒毅路 17 号 | **32.16145, 118.87958** en 32.15027, 118.88596 (twee percelen van dezelfde naam) | OSM `landuse=industrial` **乐金化学新能源电池有限公司** (= LG Chem New Energy Battery, de naam van vóór de afsplitsing van LGES) + vrachtdocumenten "HENGYI RD NO.17, NANJING ECONOMY" | **satelliet-gelegd** — grote productiehallen, eigen poorten, logistiek terrein |
| Jiangning / Binjiang | 31.85052, 118.56654 | OSM/Nominatim "LG新能源", 江宁街道 | bevestigd als LG-locatie, lijn onbekend |

*In dezelfde NEDZ-cluster staan ook LG Display Nanjing (32.15593, 118.88780), LG Electronics
(32.15434, 118.86556), LG Magna e-Powertrain (32.15740, 118.86575) en het LG-personeelsflatgebouw —
het is één LG-terreincomplex, wat de keuze voor deze campus verder steunt.*

## Been 8 · weg — Nanjing → Tesla Giga Shanghai

**been-id:** `li-gz-b8` · **Modaliteit:** truck · **Lengte:** ±300 km — te meten

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | Laadplek LG ES Nanjing | laadplek | nog te leggen | [L2] | aannemelijk |
| 2 | ±110 | Changzhou | passage | 31.8123, 119.9692 | OSM | **bevestigd** |
| 3 | ±230 | Songjiang / Shanghai-west | passage | 31.0344, 121.2232 | OSM place=city | aannemelijk |
| 4 | ±300 | **Tesla Giga Shanghai — poort 3** | poort | **30.87390, 121.76572** | OSM node 特斯拉3号门 | **bevestigd** |
| 5 | ±300,5 | **Tesla Giga Shanghai — terrein** | losplek (keten-eind) | **30.87358, 121.76849** | OSM way 635670279 (特斯拉上海超级工厂 / Tesla Gigafactory 3) | **bevestigd** |

**Waar de keten eindigt, en waarom daar.** Bij de autofabriek: de 2170-cellen uit Nanjing gaan naar Giga
Shanghai en worden daar in het accupakket en de auto ingebouwd [L2]. Wat daarna volgt is
voertuigdistributie naar duizenden dealers — dat is een markt, geen gedocumenteerde volgende locatie, en
een marktcentroïde is per werkwijze **géén anker**. Daarom stopt de brief hier, beargumenteerd.

---

## 4 · Samenvloeiingen en vertakkingen (overzicht)

| # | been | soort | met welke brief | wat gedeeld wordt | eigenaar anker |
|---|---|---|---|---|---|
| 1 | b1/b2 | vertakking | nog te schrijven: `lithium-greenbushes-kemerton` | dezelfde laadplek en dezelfde truckcorridor tot de haven; daarna een andere haven/bestemming (Albemarle-electie ≤50 %) | deze brief |
| 2 | na de verwerkingsknoop Tianqi | vertakking | nog te schrijven: `lithium-zhangjiagang-lfp` (德方纳米) | het Tianqi-anker; carbonaat i.p.v. hydroxide | deze brief |
| 3 | na de verwerkingsknoop Wuxi | vertakking | nog te schrijven: `lithium-wuxi-wroclaw` | het Wuxi-anker; kathode naar Polen i.p.v. Nanjing | deze brief |

**Regel:** één brief = één streng. Alle drie de vertakkingen delen alleen een **anker**, geen been-geometrie —
er is dus (nog) niets dat in twee brieven dubbel uitgeschreven wordt.

## 5 · Openstaande punten

| # | been | wat | waarom onzeker | wat het zou oplossen |
|---|---|---|---|---|
| 1 | b6 | **Welke kathodefabriek krijgt de Zhangjiagang-hydroxide?** | Het Tianqi–LG Chem-contract is bedrijfs-naar-bedrijf; geen bron koppelt de Zhangjiagang-lijn aan de Wuxi-fabriek | Een leverbron per fabriek, óf een besluit van Lars om de brief bij de fabriekspoort van Tianqi te laten stoppen |
| 2 | b4/b5 | **Welke ligplaats in Zhangjiagang** | Het kandidaatgebied is gevonden (hoofdhavenkade 31.970–31.975 / 120.410–120.440), maar geen bron wijst een ligplaats aan; het chemiepark bij de fabriek heeft alleen vloeistofsteigers | Een z16-pass over die kade (welk vak heeft stapelvelden i.p.v. containers) + zo mogelijk een terminalbron |
| 3 | overslag Bunbury | **Shed 8-8 staat niet op de Esri-opname** | De opname is ouder dan de loods. ⚠️ **Esri Wayback is geprobeerd** (release 32246 = 2026-06-30, de nieuwste van 195): dat beeld is voor Bunbury **identiek aan de live laag** — Esri heeft de binnenhaven sindsdien niet ververst, dus dit is niet met Esri op te lossen | Een andere bron: Sentinel-2 (10 m toont een loods van 55.000 t als rechthoek, genoeg om de plek te bepalen, niet om te ankeren) of een havenplattegrond van Southern Ports |
| 4 | b1 | **De mijnpoort** en de exacte terreinroute | Talison publiceert geen terreinplattegrond | De eerste wegcorridor-run: het punt waar de terreinweg de South Western Highway raakt valt er vanzelf uit |
| 5 | b5/b6 | **Twee Chinese fabrieken hebben een ADRES maar nog geen coördinaat** — Tianqi 东新路 5 号 · LG Chem/Huayou 锡梅路 167 号 | OSM kent in China geen huisnummers (`addr:street`-query levert 0) en Nominatim vindt de bedrijfsnamen niet; de straten zelf zijn wél bekend. ⚠️ Een volledige scan over de china-extract vond ze ook niet — OSM heeft ze simpelweg niet (de LG-cluster in Nanjing vond hij wél) | Eén geocodeerslag op een Chinese kaartdienst (Amap/Baidu, API-sleutel nodig), daarna per punt een z16-pass |
| 5b | b7 | **Welke LG-lijn in Nanjing de 2170-cellen maakt** | De New Port-campus is gelegd, maar LGES heeft negen fabrieken op vijf locaties in twee zones; welke hal de cilindercel-lijn draait staat nergens | Een bron die de cilinderlijn aan één campus/hal koppelt — of accepteren op campusniveau (dat is voor de kaart genoeg) |
| 6 | b2 | **Aandeel Fremantle** t.o.v. Bunbury | Albemarle's rapport noemt beide havens zonder verdeling | Een exportstatistiek per haven (Southern Ports vs Fremantle Ports) |
| 7 | b3 | **Lombok of Soenda** | Beide routes worden gevaren; geen bron per reis | AIS-tracks van bulkcarriers Bunbury→Yangtze (de collector dekt dit gebied niet, dus: laag prioriteit) |

## 6 · Conflicten met de projectdata (afwerklijst)

| # | wat | nu | hoort te zijn | bron |
|---|---|---|---|---|
| 1 | `li-greenbushes` in `data/lithium.js` | lat −33.86, lon 116.06 (mijncentroïde) | laadplek −33.86495, 116.05505 (of expliciet als centroïde laten staan mét eigen aansluiting) | eigen satellietpass |
| 2 | `li-port-bunbury` in `data/lithium.js` | lat −33.32, lon 115.64 | Berth 8: −33.31995, 115.66385 — het huidige punt ligt **2,2 km** westelijker, in zee vóór de strandkust | eigen satellietpass |
| 3 | corridor `li-greenbushes-kemerton` in `fetch_landnet.py` | van (116.054060, −33.864550) | 102 m van het nieuwe anker; converge op één redactionele waarde | vergelijk generator↔uitvoer vóór regeneratie |
| 4 | `data/lithium.js` flow `li-greenbushes → li-ref-jiangxi` | via `li-port-ningbo` (Ningbo-Zhoushan) | déze streng landt in **Zhangjiagang**, niet in Ningbo; Ningbo hoort bij een andere raffinaderij-streng | [Q1] |
| 5 | `aansluitingen.json` | geen lithium-aansluitingen | vier nieuwe: `li-gb-laadplek`, `li-bun-berth8`, `li-zjg-kade`, `li-zjg-tianqi` | deze brief |

## 7 · Wat de kaart moet tekenen

1. **b1 + b2** (doorgetrokken, truck-amber): concentraatloods → poort → South Western Highway → Bunbury,
   over echte OSM-weggeometrie; ±90 km.
2. **b3** (doorgetrokken, zee-blauw): Berth 8 → Yangtze-monding, vrij geroutet over MARNET.
3. **b4** (doorgetrokken, rivier-turkoois): Yangtze-monding → Zhangjiagang over de MARNET-bulklaag
   (`maak_rivierbeen.py`, zelfde recept als Shanghai→Tongling).
4. **b5** (doorgetrokken indien kade gevonden, anders **gestippeld mét reden** "kade niet vastgesteld"):
   kade → Tianqi-poort.
5. **b6, b7, b8** (doorgetrokken, weg-amber): Zhangjiagang → Wuxi → Nanjing → Giga Shanghai.
6. **Overslagmarkers**: Bunbury (2), Zhangjiagang (2), Tianqi-poort, Wuxi, Nanjing.
7. **Referentiemarkers** (niet aan de lijn): Kemerton, Kwinana, Fremantle — de andere strengen uit dezelfde mijn.
8. **Kleur = modaliteit** (truck amber · zee blauw · rivier turkoois), conform de vier bestaande stromen.

## 8 · Toets-checklist

- [x] **Notatie:** alle coördinaten lat, lon met decimale punt; ankers op 5 decimalen
- [x] Elk been heeft een **been-id**; ankers dragen een id (nog te registreren in `aansluitingen.json`)
- [ ] Elke laadplek, overslag en losplek heeft status **satelliet-gelegd** — **4 van 9 gelegd**
      (Greenbushes-loods, Berth 8, LG-celfabriek Nanjing, Tesla-poort via OSM); de rest staat in §5
- [x] Elke laad-/los-/overslagplek heeft een ingevulde **productvraag** (§2a) inclusief uitsluitingen
- [x] Elke overslag heeft **twee ankers** + de terreinstappen ertussen
- [x] **Routeerpunt + max snap** genoteerd bij elk been-uiteinde op water
- [ ] **Dekking:** nog niet gedraaid — er is nog geen gebakken stroom
- [ ] **Verklikker:** idem
- [ ] Geen enkel **negatief anker** binnen zijn verbodsstraal geraakt — nog niet gedraaid
- [ ] Lengte per been binnen de tolerantie — alleen been 2 heeft een gepubliceerde waarde (±90 km)
- [x] Volumes sluiten aan over de verwerkingsknoop (110 kt → 17 kt = 6,47:1, §2)
- [x] Elke stippellijn draagt een reden; elk reëel alternatief heeft een aandeel of een openstaand punt
- [x] De keten loopt door tot het eindproduct (fase E eindigt beargumenteerd bij de autofabriek)

## 9 · Bronnen

**Mijn en corridor [T..]:** T1 Talison Lithium, *"Outcome of Joint Feasibility Study into
Greenbushes-to-Bunbury Railway Line"* (78 km, 38 km volledig vervangen, 76 overwegen, "not economically
feasible at this time") · T2 Talison, *Greenbushes Project — Overview* (toegang via de verharde South
Western Highway tussen Bunbury en Bridgetown; concentraat wordt verscheept vanuit Bunbury) · T3
WA-regering / Rail Express / Mining Weekly over de studie (1,5 Mt/j ≈ 135 truckbewegingen/dag, groeiend
naar 2,1 Mt/j ≈ >70.000/jaar, klachten Donnybrook).

**Haven [S.., K..]:** S1 Southern Ports, *Port Community Consultation Committee Bunbury — notulen
09-08-2023* (record spodumeen; "Bunbury is the largest export port of lithium in the world"; Berth
8-scheepslader en -brandbeveiliging; Southern Ports in Talisons spoorstudiegroep) · S2 Southern Ports,
*Port Services and Facilities* (Berth 8: 250 m, 11,6 m, scheepslader tot 2.000 t/h) · K1 Kerman
Contracting, *Spodumene Storage Facility Bunbury Port* (opdrachtgever Talison, 55.000 t, inload 500 t/h,
outload 2.000 t/h, AU$ 26,4 mln) + Belpile (paalfundering op aangeplempt land binnen de haven).

**Mijneigendom [A..]:** A1 Albemarle, *S-K 1300 Technical Report Summary — Greenbushes* en 10-K/8-K
(electie tot 50 % van de jaarproductie; export via Bunbury of Fremantle; chemical grade min. 6,0 % Li2O) ·
IGO/TLEA-mededelingen (TLEA 51/49 Tianqi/IGO; SC6.0 via TLEA naar Tianqi Lithium Corporation).

**Raffinaderij [Q..]:** Q1 天齐锂业（江苏）有限公司, *突发环境事件应急预案* (bedrijfsdocument, PDF op
tianqilithium.com): adres 扬子江国际化学工业园东新路5号, terrein 96.533,4 m², 226 medewerkers, 17.000 t/j
Li2CO3, bijproduct 51.062 t/j Na2SO4, jaarverbruik 110.000 t spodumeen (max. opslag 20.000 t,
transportband), zwavelzuur 38.000 t/j, buren aan vier zijden, oorspronkelijk 银河锂业（江苏） · Q2
Shanghai Securities News / Sina Finance / OFweek (25-09-2025: 30.000 t/j LiOH in bedrijf, ±1,8 mrd RMB) ·
Q3 Wood Mackenzie *Zhangjiagang (Tianqi) lithium refinery* + Australian Mining (Zhangjiagang als
loshaven voor Australisch spodumeenconcentraat).

**Kathode/cel/auto [L..]:** L1 Chemical Engineering + KED Global over LG Chem Wuxi (kathodefabriek sinds
eind 2019, 40–50 kt/j; het volledige volume van Quzhou en Wuxi gaat naar LG ES Nanjing en Wrocław) · L2
The Elec / Batteries News (LG ES Nanjing maakt 2170-cellen voor Tesla Model Y, geleverd aan Giga
Shanghai; LGES China-hoofdkantoor in de Nanjing Economic & Technological Development Zone; negen
fabrieken op vijf locaties) · L3 Baidu Baike / SMM over LG Energy Solution · L4 CnEVPost +
SMM (27-06-2022: 成都天齐 tekent hydroxideleveringscontract met LG Chem, 01-01-2023 t/m 31-12-2026;
volumes niet openbaar) + cnstock/nbd (24-06-2022: carbonaatcontract met 德方纳米, jul 2022 – dec 2024) ·
L5 bedrijfsregisters (企典/外企查) + Huayou-persbericht: 乐友新能源材料（无锡）有限公司, opgericht
29-06-2018, JV LG Chem × 华友钴业, kapitaal US$ 285,36 mln, **无锡市新吴区锡梅路167号**, productie en
verkoop van **三元电池正极材料** (ternair kathodemateriaal) · L6 vrachtdocumentatie (Panjiva/ImportGenius):
*Lg Energy Solution (Nanjing) Co. Ltd., HENGYI RD NO.17, Nanjing Economic Development Zone*; Invest
Nanjing + Pandaily over de twee campussen (Qixia/New Port en Jiangning/Binjiang).

**Eigen metingen [C..]:** C1 eigen satellietpass Esri World Imagery z14–z18 op 2026-07-29 met
`v2/tools/sat_check.py` (Greenbushes-loods, Bunbury Berth 8, Zhangjiagang-waterkant; **z19 is bij
Greenbushes niet beschikbaar**) · OSM-plaatsen en -wegen via Overpass (place=town/village/suburb langs de
South Western Highway; 东新路; Tesla Gigafactory 3 + poort 3) · lokale Geofabrik-extract australie-latest
(`Greenbushes Lithium Mine`, way 258238288) · bestaande corridordefinitie `li-greenbushes-kemerton` in
`v2/tools/fetch_landnet.py`.
