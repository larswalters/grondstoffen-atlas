# Aardolie — ontwerp (op papier)
*Aangemaakt 2026-07-15 · status: volledig ingevulde brief (ontwerp = build in dezelfde sessie).*
*Milestone (Linear): `M10 · Olie`. Data-doel: `data/oil.js` van "basis" (18 nodes / 15 flows) → "uitgewerkt" volgens het lithium/uranium-schema.*

> **De echte vorm (waarom olie interessant is om uit te werken).** Alle eerdere grondstoffen hadden één trechter:
> lithium/koper/REE knijpen bij de **raffinage** (China), goud bij Zwitserland (Ticino), uranium bij de Russische
> **verrijking**. Olie's knijp is **niet één plek maar een héél netwerk van zeestraten** — en het is precies het
> netwerk waar de atlas z'n knelpunten al voor heeft: **Hormuz, Malakka, Bab-el-Mandeb/Suez, Bosporus, Panama, Kaap**.
> Olie is de grondstof die die knelpunten tegelijk laat **oplichten**. Daarbovenop drie levende verhalen: (1) de
> **Hormuz-bypass-pijpleidingen** (Saoedi Oost-West → Yanbu; UAE Habshan → Fujairah) als het fysieke antwoord op de
> Golf-flessenhals; (2) de **Rusland-omleiding sinds 2022** — Europese crude omgeleid naar India/China (Primorsk/
> Novorossiysk/ESPO-Kozmino), een beleidsgedreven her-routering zoals uranium's Trans-Kaspische; (3) de
> **Amerikaanse schalie-ommekeer** — de VS van importeur naar exporteur, een omgekeerde pijl.

> Principe: we vertellen geen verhaal, we modelleren de werkelijkheid nauwkeurig — het plaatje vertelt zichzelf.
> Voor olie is de "aha" dat de **reserves** (Golf, Venezuela, Rusland) en het **verbruik** (Azië, Europa, N-Amerika)
> op verschillende continenten zitten, en dat álle tussenliggende tankerstromen door een handvol zeestraten moeten.
> Zet de bogen goed neer en de kaart tekent vanzelf de geopolitiek van de 20e én 21e eeuw.

## 0. Metadata (→ `REGISTER({...})`)
| veld | waarde |
|---|---|
| `id` | `oil` (blijft) |
| `name` | Aardolie |
| `symbol` | Oil |
| `color` | `#1c1a17` (crude = zwart/donker) · `flowColor` `#E8A838` (amberkleurige stromen op de donkere bol) |
| `unit` | `Mb/d (indicatief)` — miljoen vaten per dag, hele keten optelbaar |
| `detail` | `basis` → `uitgewerkt` |
| `blurb` | Ruwe olie: brandstof, plastics en chemie. Reserves geconcentreerd in de Golf, Venezuela en Rusland; raffinage bij de afzetmarkten. Elke grote stroom moet door een zeestraat — olie is de grondstof waar het hele knelpunten-netwerk (Hormuz, Malakka, Suez, Bosporus, Panama) voor bestaat. |

## 1. Het verhaal in 3 zinnen
1. **Winning ver van verbruik** → lange tankerstromen die door een handvol zeestraten geknepen worden; **Hormuz** (~⅓ van alle olie over zee) is de moeder van alle knelpunten.
2. **De Golf → Azië** is de dikste bundel: Saoedi/Irak/UAE/Koeweit/Iran-crude threadt eerst **Hormuz**, dan **Malakka**, naar China/India/Korea/Japan — twee flessenhalzen achter elkaar (de "Malakka-dilemma").
3. **Twee levende her-routeringen**: de **Hormuz-bypass-pijpleidingen** (Yanbu/Fujairah) en de **Rusland-omleiding** sinds 2022 (Europese crude → India/China) laten zien dat de kaart geen statisch plaatje is maar meebeweegt met sancties en oorlog.

## 2. De keten & stages
Olie is in de kern een **2-staps** keten (ruwe olie → geraffineerde producten); we gebruiken de 3e stage (`product`) voor de **petrochemie** (nafta → kraker → kunststof) — de lichte, hoge boog die laat zien dat olie ook plastic wordt.

| stap | `stage` | kleur | booghoogte | inhoud |
|---|---|---|---|---|
| 1. Winning → ruwe olie (crude) | `erts` | donker/gedempt | laag | crude van veld/terminal → raffinaderij. **Draagt het knelpunten-verhaal.** |
| 2. Raffinage → producten (diesel/benzine/kerosine/nafta) | `raffinaat` | volle amber | midden | export-raffinaderij → verbruiksmarkt |
| 3. Petrochemie → kunststof | `product` | licht | hoog | nafta/ethaan → kraker → plastics (klein, completeert "wat wordt olie") |

*Alle volumes indicatief in **Mb/d**. Wereldproductie ≈ 100 Mb/d; crude over zee ≈ 40 Mb/d. Peiljaar ±2023/24; bronnen: EIA, IEA Oil Market Report, OPEC ASB, BP/Energy Institute Statistical Review, Vortexa/Kpler-stromen (indicatief).*

## 3. Nodes (locaties)

### 3a. Winning / crude-producenten (`type: mine`, `share` ≈ export/productiegewicht)
| id | naam | land | lat | lon | share | note |
|---|---|---|---|---|---|---|
| oil-saoedi | Ghawar/Abqaiq | Saoedi-Arabië | 25.4 | 49.6 | 15 | Grootste crude-**exporteur**; OPEC-swingproducent |
| oil-rusland | West-Siberië | Rusland | 61 | 74 | 12 | Grootste geo-omgeleide exporteur sinds 2022 |
| oil-vs | Permian Basin | VS | 31.9 | -102.3 | 14 | Schalie — de VS werd netto-exporteur (ommekeer) |
| oil-irak | Basra/Rumaila | Irak | 30.5 | 47.4 | 5 | Zuidelijke megavelden → Basra-terminal |
| oil-iran | Khuzestan | Iran | 31.3 | 49.3 | 4 | Export vrijwel volledig naar China (sancties) |
| oil-vae | Abu Dhabi | VAE | 24.0 | 54.0 | 4 | Habshan → Fujairah-pijpleiding (Hormuz-bypass) |
| oil-koeweit | Burgan | Koeweit | 29.1 | 47.9 | 3 | Enorm ondiep veld |
| oil-canada | Athabasca-oliezanden | Canada | 57.0 | -111.5 | 6 | Zware olie; pijpleidingen naar de VS + TMX naar Pacific |
| oil-brazilie | Pré-sal (Santos) | Brazilië | -25.0 | -42.5 | 4 | Offshore diepzee, snelgroeiend |
| oil-nigeria | Nigerdelta (Bonny) | Nigeria | 4.5 | 7.0 | 2 | Lichte zoete crude → Europa/India |
| oil-angola | Cabinda (offshore) | Angola | -6.0 | 12.0 | 1.5 | Offshore → China (groot afnemer) |
| oil-kazachstan | Tengiz/Kashagan | Kazachstan | 46.0 | 53.0 | 2 | **Landlocked** — CPC-pijpleiding vs BTC-bypass |
| oil-noorwegen | Noordzee | Noorwegen | 60.0 | 2.5 | 2 | Europa's eigen crude/gas |
| oil-venezuela | Orinoco-gordel | Venezuela | 9.0 | -63.5 | 1 | **Grootste reserves, ingestorte productie** — de paradox |

### 3b. Export-terminals / havens (`type: port`) — dragen de bypass- en Rusland-verhalen
| id | naam | land | lat | lon | rol |
|---|---|---|---|---|---|
| oil-term-rastanura | Ras Tanura | Saoedi-Arabië | 26.65 | 50.16 | Grootste crude-exportterminal (Perzische Golf → Hormuz) |
| oil-term-yanbu | Yanbu | Saoedi-Arabië | 24.09 | 38.06 | **Oost-West-pijpleiding-terminus (Rode Zee) — Hormuz-bypass** |
| oil-term-fujairah | Fujairah | VAE | 25.12 | 56.33 | **Habshan-Fujairah-terminus (Golf van Oman) — Hormuz-bypass** + bunkerhub |
| oil-term-kharg | Kharg Island | Iran | 29.23 | 50.32 | Iraans export-eiland → China |
| oil-term-primorsk | Primorsk | Rusland | 60.34 | 28.61 | Baltische crude-export (West-Siberië) → omgeleid |
| oil-term-novoros | Novorossiysk | Rusland | 44.72 | 37.80 | Zwarte Zee: Russische + Kazachse (CPC) crude → Bosporus |
| oil-term-kozmino | Kozmino (ESPO) | Rusland | 42.72 | 133.10 | Pacific-terminus van de ESPO-pijp → China/India |
| oil-term-ceyhan | Ceyhan | Turkije | 36.87 | 35.93 | BTC (Azeri/Kazachs) + Kirkuk → Middellandse Zee (Hormuz+Bosporus-bypass) |
| oil-term-corpus | Corpus Christi | VS | 27.80 | -97.40 | Belangrijkste **crude-EXPORT**-terminal (schalie) |
| oil-term-bonny | Bonny | Nigeria | 4.42 | 7.16 | West-Afrikaanse crude-uitgang |

### 3c. Raffinage / verwerking (`type: refinery`)
| id | naam | land | lat | lon | rol |
|---|---|---|---|---|---|
| oil-ref-jamnagar | Jamnagar (Reliance) | India | 22.35 | 69.85 | Grootste raffinaderij ter wereld — export-georiënteerd; grote afnemer Russische crude |
| oil-ref-golfkust | Golfkust (Houston/Port Arthur) | VS | 29.75 | -93.90 | Grootste raffinagecluster; verwerkt zware crude, exporteert product |
| oil-ref-rotterdam | Rotterdam/Pernis (ARA) | Nederland | 51.90 | 4.10 | Europa's raffinage- en handelshub |
| oil-ref-singapore | Jurong | Singapore | 1.26 | 103.70 | Aziatisch raffinage-/handelsknooppunt |
| oil-ref-ulsan | Ulsan | Zuid-Korea | 35.50 | 129.36 | Grote export-raffinaderij (product naar heel Azië) |
| oil-ref-china | Zhoushan/Dalian | China | 30.0 | 122.0 | 2e raffinagenatie, snelst groeiend |
| oil-ref-japan | Chiba (Tokiobaai) | Japan | 35.50 | 140.10 | Grote importraffinage |
| oil-ref-jubail | Jubail (SATORP) | Saoedi-Arabië | 27.0 | 49.6 | Saoedische export-raffinaderij (product) |
| oil-ref-ruwais | Ruwais (ADNOC) | VAE | 24.11 | 52.73 | Grote export-raffinaderij Golf |

### 3d. Verbruiksmarkten (`type: market`) — waar producten landen (raffinaat)
| id | naam | land | lat | lon | note |
|---|---|---|---|---|---|
| oil-mkt-europa | NW-Europa (diesel-tekort) | Duitsland/België | 50.9 | 6.5 | Importeert diesel uit India/Golf/VS/Rusland-was |
| oil-mkt-wafrika | West-Afrika (Lagos) | Nigeria | 6.45 | 3.40 | **Exporteert crude, importeerde product** — de raffinage-paradox (tot Dangote 2024) |
| oil-mkt-latam | Latijns-Amerika | Brazilië | -23.0 | -43.2 | Importeert benzine/diesel uit de VS-Golfkust |
| oil-mkt-oostafrika | Oost-Afrika (Mombasa) | Kenia | -4.05 | 39.67 | Product-importeur uit de Golf/India |

### 3e. Petrochemie-clusters (`type: market`, stage `product`)
| id | naam | land | lat | lon | note |
|---|---|---|---|---|---|
| oil-pchem-jubail | Jubail (SABIC) | Saoedi-Arabië | 27.02 | 49.65 | Nafta/ethaan → kraker → kunststof-export |
| oil-pchem-antwerpen | Antwerpen | België | 51.25 | 4.30 | Europa's grootste petrochemiecluster (bij ARA) |
| oil-pchem-ulsan | Ulsan | Zuid-Korea | 35.52 | 129.38 | Aziatische kunststof-export |
| oil-pchem-ningbo | Ningbo | China | 29.87 | 121.55 | Chinese kraker-nieuwbouw (zelfvoorziening kunststof) |

## 4. Kern-stromen (flows)

**A. Golf → Azië (de dikste bundel; Hormuz + Malakka):**
- Ras Tanura/Kharg/Basra/UAE/Koeweit → China/India/Korea/Japan/Singapore, `via:["wp-hormuz","wp-aceh","wp-malakka","wp-singapore","wp-scs", ...]`. India via `wp-hormuz` direct over de Arabische Zee (geen Malakka).
- **Iran → China** via Hormuz + Malakka (sanctie-stroom, "schaduwvloot").

**B. Golf → Europa (Bab-el-Mandeb + Suez, of om de Kaap):**
- Ras Tanura → Rotterdam `via:["wp-hormuz","wp-bab","wp-rode-zee","wp-suez","wp-gibraltar"]` (en de Kaap-variant als Suez dicht).

**C. Hormuz-bypass-pijpleidingen (het fysieke antwoord):**
- Saoedi: veld → `pipeline` → **Yanbu** (Rode Zee) → schip via Bab/Suez of om de Kaap. Skipt Hormuz.
- UAE: Abu Dhabi → `pipeline` → **Fujairah** (Golf van Oman) → schip. Skipt Hormuz volledig.

**D. Rusland-omleiding (2022→):**
- West-Siberië → **Primorsk** (Baltisch) → `wp-deense-straten` → Noordzee → `wp-gibraltar`/`wp-suez` → **India (Jamnagar)**. De grote nieuwe pijl.
- **ESPO** → **Kozmino** (Pacific) → **China** (kort) + India (via Malakka).
- **Novorossiysk** (Zwarte Zee) → `wp-bosporus`,`wp-dardanellen` → Middellandse Zee → India.
- **Druzhba-pijpleiding** → Midden-Europa (Hongarije/Slowakije, resterende uitzonderingen), `mode:"pipeline"` over land.
- Gekrompen rest-pijl Rusland → Europa (contrast met het India-volume).

**E. VS-schalie-ommekeer (omgekeerde pijl):**
- Permian → **Corpus Christi** → Rotterdam (Atlantic) + Azië (via `wp-panama` of Kaap). De VS die crude/product **exporteert**.
- Canada-oliezanden → `pipeline` → VS-Golfkust (Keystone/Enbridge) + TMX → Pacific → Azië.

**F. West-Afrika / Brazilië / Venezuela:**
- Nigeria/Angola → Europa (Gibraltar) / China (Kaap of Malakka).
- Brazilië pré-sal → China (Kaap/Pacific) + Europa.
- Venezuela → VS-Golfkust (zware crude) + China — de reserves-vs-productie-paradox (dunne pijl ondanks #1 reserves).
- Kazachstan Tengiz → `pipeline` CPC → Novorossiysk (Rusland-afhankelijk) **én** → `pipeline` BTC → Ceyhan (bypass).

**G. Product-trade (raffinaat):**
- Jamnagar/Jubail/Ruwais/Ulsan/VS-Golfkust → NW-Europa (diesel), West-Afrika, Oost-Afrika, Latijns-Amerika.
- De **Nigeria-paradox**: crude eruit, product erin (tot Dangote 2024).

**H. Petrochemie (product):**
- Jubail/Antwerpen/Ulsan/Ningbo: lokale nafta → kraker → kunststof-waaier (lichte, hoge bogen).

## 5. Knelpunten & vaarpunten
- **Bestaande `wp-*` die olie raakt (vrijwel allemaal!):** `wp-hormuz`, `wp-malakka`, `wp-aceh`, `wp-singapore`, `wp-scs`, `wp-bab`, `wp-rode-zee`, `wp-suez`, `wp-gibraltar`, `wp-kaap`, `wp-bosporus`, `wp-dardanellen`, `wp-panama`, `wp-deense-straten`, `wp-lombok`, `wp-taiwan`, `wp-pac-*`, `wp-atl-west`.
- **NIEUW knelpunt: géén.** Dat is olie's eigen aha — het is de grondstof waar het hele knelpunten-net al voor bestaat; olie laat het compleet oplichten. Alleen eventueel een paar **navigatie-vaarpunten** (Golf van Mexico / Caribisch / Arabische Zee) toevoegen als de headless legs-check rechte/kapotte legs toont; oil-only, in een eigen gelabeld blok.
- **Institutionele "knijp" (geen zeestraat), via `tensions`:** de **reserves-concentratie + OPEC+** (Saoedi+Rusland als prijszetters) en de **Rusland-omleiding** (sanctie/prijsplafond-beleid).

## 6. Optionele toggle-laag — strategische voorraden (SPR) — `layer:"reserve"` ✅ GEBOUWD (2026-07-15)
Olie's equivalent van de goud-CB-laag / koper-beursvoorraden / REE-recycling: **strategische petroleumreserves** als optionele toggle (default uit). **Uitgevoerd** in een tweede sessie (LAR-432, commit `86c8c1f`), nadat de parallelle nikkel-sessie klaar was en de gedeelde engine-bestanden vrij waren.
- Nodes (`type:"reserve"`, `stock` = mln vaten → markergrootte, olie-amber tank): **US SPR** (Golfkust-zoutkoepels, Bryan Mound/Big Hill, ~350), **China SPR** (Dalian/kust, ~300), **Japan** (Kiire, ~130), **India** (Mangalore/Padur, ~40), **IEA/EU** (Le Havre, ~90). + 5 vul-flows (`layer:"reserve"`, stage erts) + tension `oil-t-spr`.
- Nuance: buffer tegen aanbodschokken, geen dagelijkse handelsstroom — net als de koper-beursvoorraden.
- **Het vierde optionele-laag-patroon** (goud=CB, koper=exchange, REE=recycle, **olie=reserve**), exact het koper-`exchange`-patroon op 5 plekken (`config`/`main`/`flows`/`markers`/`ui`) + een nieuwe `reserve`-key. Chip "voorraden" verschijnt alleen bij olie (`hasReserves()` generiek). Headless geverifieerd: toggle uit=45/46, aan=50/51 (+5/+5), 0 kapot/0 straight, regressievrij.

## 7. Emergent plaatje (verificatie-lat)
1. **Hormuz gloeit op** als de dikste knoop — bijna alle Golf-crude wringt zich hierdoor, en meteen daarna door **Malakka** naar Oost-Azië (twee ringen achter elkaar).
2. **De Golf → Azië-bundel** is veruit de dikste stroom op de kaart; Europa-stromen zijn dunner en lopen via Bab/Suez of de Kaap.
3. **Twee dunne bypass-pijpleidingen** (Yanbu op de Rode Zee, Fujairah op de Golf van Oman) die om Hormuz heen kruipen — zichtbaar náást de dikke Hormuz-stroom.
4. **De Rusland-omleiding**: een dikke nieuwe boog Rusland → India (Primorsk om Europa heen; ESPO → China), met een gekrompen Rusland → Europa-pijl ernaast.
5. **De VS als exporteur**: pijlen die uit Corpus Christi de Atlantische Oceaan op gaan (omgekeerd t.o.v. de 20e eeuw).
6. **De reserves-paradox**: Venezuela met een dun pijltje ondanks de grootste stip-reserves; de Golf klein op de kaart maar met de dikste stromen.
7. Toggle SPR → een setje voorraaddepots (VS-Golfkust, China, Japan, India) verschijnt, buiten de dagelijkse stromen om.

## 8. Bronnen
EIA (US crude exports, chokepoints-briefs: Hormuz ~20 Mb/d, Malakka), IEA Oil Market Report, OPEC Annual Statistical Bulletin, Energy Institute Statistical Review of World Energy 2024, Kpler/Vortexa-stroomdata (indicatief, post-2022 Rusland-omleiding). Peiljaar ±2023/24.

## 9. Open punten
- Dangote-raffinaderij (Nigeria, 2024) draait de crude-eruit/product-erin-paradox deels om — modelleren als een kantelende pijl of in de note laten.
- Exacte post-2022 Rusland→India/China-tonnage schommelt; volumes indicatief houden.
