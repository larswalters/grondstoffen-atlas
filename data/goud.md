# Goud — brief (ingevuld ontwerp) — hoort bij `data/goud.js`

*Peiljaar ±2024. Alle volumes in **t/jaar** (metrische ton fijn goud), indicatief en afgerond —
bedoeld om verhoudingen te tonen, geen handelsstatistiek. Wereldmijnproductie ≈ **3.300 t**
(USGS 2024). Bronnen: World Gold Council (WGC), USGS Mineral Commodity Summaries 2025, LBMA,
Metals Focus. Zie §7. Status: **uitgewerkt-ontwerp** — klaar om 1-op-1 naar `goud.js` te zetten (LAR-401).*

> **Principe:** we vertellen geen verhaal, we modelleren de werkelijkheid — het plaatje vertelt
> zichzelf. Voor lithium is de vorm "alles door China"; voor goud is de vorm **anders**: de
> mijnbouw is wijd verspreid (géén enkel land domineert), maar de **raffinage knijpt samen in
> één hoekje Zwitserland (Ticino)**, waarna een kleine ring kluis-/handelshubs de wereld rondstuurt
> en **China een eenrichtings-put** is (goud stroomt naar binnen, niets naar buiten).

---

## 0. Metadata (→ `REGISTER({...})` in `goud.js`)

| veld | waarde |
|---|---|
| `id` | `goud` |
| `name` | Goud |
| `symbol` | Au |
| `color` | `#D4AF37` (goudgeel; markers) |
| `flowColor` | `#F2C94C` (iets lichter, voor de bogen tegen de donkere bol) |
| `unit` | `t/jaar` (voor de CB-laag: `t voorraad`) |
| `detail` | `uitgewerkt` |
| `blurb` | Mijnbouw wijd verspreid over álle continenten, maar de raffinage knijpt samen in Zwitserland (Ticino, ~⅔ van de wereld). Van daaruit een kleine ring kluishubs (Londen/NY/Zürich/Shanghai/Dubai); China is een eenrichtings-put. |

## 1. Het verhaal in 3 zinnen
1. **Geen enkel land domineert de mijnbouw** — China (380 t), Rusland (310 t), Australië (290 t),
   Canada (200 t) en de VS (170 t) lopen dicht op elkaar; geen mijn is groter dan ~2,5% van de wereld.
2. De echte flessenhals zit **één stap ná het graven**: ~65-70% van al het goud wordt geraffineerd
   in **Zwitserland**, en het gros daarvan in vier huizen in **Ticino** (Valcambi, PAMP, Argor-Heraeus)
   + Metalor — doré-bogen uit de hele wereld convergeren op één punt.
3. Vanuit Zwitserland waaieren baren uit naar een handvol **kluis-/handelshubs** die óók onderling
   schuiven (Londen↔Zürich↔New York), naar **India** (sieraden) en via **Hongkong → Shanghai**
   China in — waar het blijft. Een aparte laag toont de **centrale banken** (voorraden + de huidige inkoopgolf).

## 2. De keten & stages (→ `stage`-codes; hergebruikt de bestaande stage-styling)
Goud kent geen "cel/kathode" als lithium; we hergebruiken de drie bestaande codes en vullen ze goud-logisch in.

| stap | `stage`-code | kleur | booghoogte | inhoud |
|---|---|---|---|---|
| 1. mijn → **doré** (semi-ruw) | `erts` | dof/donkergoud | laag | mijn → raffinaderij; óók recyclingschroot → raffinaderij |
| 2. **geraffineerde baren** | `raffinaat` | volle goudkleur (#D4AF37) | midden | raffinaderij → hubs; interbancaire kluisstromen hub↔hub |
| 3. **eindbestemming** | `product` | licht, bijna wit | hoog | hub → consumptie (India/China/Turkije); CB-repatriëring hub → hoofdstad |

## 3. Nodes (locaties)
> ⚠️ **Nieuwe `type`-waarden** (`airport`, `hub`/`vault`, `cb`, `recycler`) bestaan nog niet in de
> rendering-laag → **build-TODO** (marker-stijl geven, §Build). `mine`/`refinery`/`port`/`market` bestaan al.
> Coördinaten: **west = negatief** (gecontroleerd). Shares zijn % van ~3.300 t wereldmijnproductie.

### 3a. Mijnbouw — actief (`type: mine`, met `share`)
*De spreiding ís het verhaal: veel losse stippen, geen trechter. Som hieronder ≈ 40% wereld; de rest is
verspreid klein/artisanaal spul (bewust niet allemaal apart geprikt).*

| id | naam | land | lat | lon | share | tier | operator | ~t/jr | note |
|---|---|---|---|---|---|---|---|---|---|
| au-nevada | Nevada Gold Mines (Carlin/Cortez) | VS | 40.30 | -116.30 | 2.5% | 1 | Barrick/Newmont JV | 84 | grootste complex ter wereld; doré grotendeels in de VS geraffineerd |
| au-muruntau | Muruntau | Oezbekistan | 41.50 | 64.55 | 2.5% | 1 | Navoi MMC (staat) | 83 | grootste open mijn; blijft grotendeels binnenlands |
| au-grasberg | Grasberg | Indonesië | -4.06 | 137.11 | 1.8% | 1 | Freeport/Inalum | 59 | goud als bijproduct van koper; via Gresik-smelter/export |
| au-olimpiada | Olimpiada | Rusland | 59.35 | 92.65 | 1.3% | 1 | Polyus | 44 | Siberië; Rusland absorbeert eigen productie |
| au-boddington | Boddington | Australië | -32.75 | 116.36 | 0.8% | 2 | Newmont | 27 | West-Australië; via Perth |
| au-cadia | Cadia | Australië | -33.46 | 148.98 | 0.7% | 2 | Newmont | 24 | NSW; via Sydney/Perth Mint |
| au-detour | Detour Lake | Canada | 49.90 | -79.70 | 0.7% | 2 | Agnico Eagle | 22 | Ontario |
| au-malartic | Canadian Malartic | Canada | 48.13 | -78.14 | 0.7% | 2 | Agnico Eagle | 22 | Québec |
| au-kalgoorlie | Kalgoorlie Super Pit (Fimiston) | Australië | -30.78 | 121.50 | 0.5% | 2 | Northern Star | 15 | iconische open pit |
| au-penasquito | Peñasquito | Mexico | 24.66 | -101.55 | 0.5% | 2 | Newmont | 16 | poly-metaal (goud+zilver) |
| au-paracatu | Paracatu | Brazilië | -17.22 | -46.87 | 0.5% | 2 | Kinross | 15 | Minas Gerais |
| au-loulo | Loulo-Gounkoto | Mali | 13.00 | -11.60 | 0.6% | 1 | Barrick | 20 | West-Afrika industrieel; naast enorme **artisanale** productie |
| au-tarkwa | Tarkwa | Ghana | 5.30 | -1.99 | 0.5% | 2 | Gold Fields | 17 | Ghana = grootste Afrikaanse producent |
| au-obuasi | Obuasi | Ghana | 6.20 | -1.66 | 0.3% | 3 | AngloGold Ashanti | 11 | heropend ondergronds |
| au-lihir | Lihir | Papoea-N.-Guinea | -3.12 | 152.63 | 0.5% | 2 | Newmont | 18 | vulkaaneiland |
| au-yanacocha | Yanacocha | Peru | -6.98 | -78.51 | 0.3% | 3 | Newmont | 10 | uitgeput rakend; Peru = grote producent |
| au-mponeng | Mponeng (Witwatersrand) | Zuid-Afrika | -26.42 | 27.42 | 0.3% | 2 | Harmony | 8 | diepste mijn ter wereld; ZA raffineert bij Rand Refinery |
| au-shandong | Shandong-cluster (Zhaoyuan) | China | 37.35 | 120.40 | 3.0% | 1 | Shandong Gold/Zijin e.a. | 100 | China #1-producent; binnenlands geraffineerd, insulair |
| au-kazakh | Altyntau (Vasilkovskoye) | Kazachstan | 53.40 | 69.40 | 0.4% | 3 | Altyntau | 13 | goud gaat deels naar de eigen centrale bank |
| au-sudan | Sudan (artisanaal) | Sudan | 18.00 | 34.00 | 0.6% | 2 | artisanaal (informeel) | 20 | grotendeels **gesmokkeld → Dubai**; het "grijze" kanaal |

> Country-nuance om in de note/annotatie te verwerken: **Rusland, China, Oezbekistan en Kazachstan**
> zijn grotendeels *gesloten* systemen — hun mijngoud gaat binnenlands naar raffinage en deels naar de
> eigen centrale bank, niet naar Zwitserland. Dat is precies waarom de convergentie op Ticino uit de
> **rest** van de wereld komt.

### 3b. Mijnbouw — projecten
*(n.v.t. voor goud v1 — de spreiding zit al in de actieve mijnen. Optioneel later: Reko Diq (Pakistan), Porgera-herstart.)*

### 3c. Raffinage (`type: refinery`) — hier knijpt het samen
*Aandelen zijn capaciteit/verwerking; de vier Zwitserse huizen samen ≈ **65-70% van de wereld**.*

| id | naam | land | lat | lon | ~capaciteit t/jr | tier | operator | note |
|---|---|---|---|---|---|---|---|---|
| au-ref-valcambi | Valcambi (Balerna) | Zwitserland | 45.845 | 9.005 | ~2.000 | 1 | Valcambi (Ticino) | grootste ter wereld — **de trechter** |
| au-ref-argor | Argor-Heraeus (Mendrisio) | Zwitserland | 45.87 | 8.98 | ~1.000 | 1 | Argor-Heraeus | Ticino |
| au-ref-pamp | PAMP (Castel San Pietro) | Zwitserland | 45.87 | 9.03 | ~450 | 1 | MKS PAMP | Ticino; premium-baren |
| au-ref-metalor | Metalor (Neuchâtel) | Zwitserland | 46.99 | 6.93 | ~650 | 2 | Metalor | buiten Ticino maar CH; wereldwijde vestigingen |
| au-ref-perth | Perth Mint | Australië | -31.955 | 115.87 | ~400 | 2 | The Perth Mint | raffineert vrijwel alle AU-productie |
| au-ref-rand | Rand Refinery (Germiston) | Zuid-Afrika | -26.23 | 28.16 | ~600 | 2 | Rand Refinery | historisch grootste; Afrika-doré |
| au-ref-mmtc | MMTC-PAMP (Rojka Meo) | India | 28.10 | 76.90 | ~200 | 2 | MMTC-PAMP | India-import + schroot |
| au-ref-dubai | Emirates Gold / Kaloti | VAE | 25.20 | 55.28 | ~500 | 2 | div. (DMCC-zone) | absorbeert Afrikaans/artisanaal goud (Sudan) |
| au-ref-rcm | Royal Canadian Mint | Canada | 45.37 | -75.66 | ~200 | 3 | Royal Canadian Mint | Ottawa; Noord-Amerikaanse doré |
| au-ref-china | China-intern (Zijin/China Gold) | China | 31.23 | 121.47 | ~500 | 2 | Zijin/China Gold | **insulair** — raffineert binnenlands, exporteert niet |
| au-ref-japan | Tanaka / Mitsubishi | Japan | 35.68 | 139.76 | ~150 | 3 | Tanaka Kikinzoku | tech-goud + belegging |

### 3d. Gateway-luchthavens (`type: airport`) — waar het goud de lucht in gaat
*Kleine/artisanale mijnen clusteren naar een regionale gateway. Goud reist als luchtvracht (waarde/gewicht).
Deze nodes zijn `via`-punten in de luchtroutes; ZRH is de grote inkomende trechter naar Ticino.*

| id | naam (IATA) | land | lat | lon | rol |
|---|---|---|---|---|---|
| au-air-zrh | Zürich (ZRH) | Zwitserland | 47.46 | 8.55 | **de inkomende trechter** → weg/spoor naar Ticino-raffinage |
| au-air-lhr | Londen (LHR) | VK | 51.47 | -0.46 | naar LBMA/BoE-kluis |
| au-air-jfk | New York (JFK) | VS | 40.64 | -73.78 | naar COMEX/NY Fed |
| au-air-dxb | Dubai (DXB) | VAE | 25.25 | 55.36 | Afrika-corridor + doorvoer naar India |
| au-air-hkg | Hongkong (HKG) | Hongkong | 22.31 | 113.92 | conduit → Shanghai (China in) |
| au-air-sin | Singapore (SIN) | Singapore | 1.36 | 103.99 | Aziatische kluishub |
| au-air-bom | Mumbai (BOM) | India | 19.09 | 72.87 | grootste sieraden-invoer |
| au-air-del | Delhi (DEL) | India | 28.56 | 77.10 | invoer + MMTC-PAMP |
| au-air-per | Perth (PER) | Australië | -31.94 | 115.97 | uitgang AU (bij Perth Mint) |
| au-air-jnb | Johannesburg (JNB) | Zuid-Afrika | -26.13 | 28.24 | Afrika-gateway (ZA + doorvoer) |
| au-air-acc | Accra (ACC) | Ghana | 5.60 | -0.17 | West-Afrika-gateway |
| au-air-gru | São Paulo (GRU) | Brazilië | -23.43 | -46.47 | Zuid-Amerika-gateway |
| au-air-yyz | Toronto (YYZ) | Canada | 43.68 | -79.63 | uitgang Canada |
| au-air-ist | Istanbul (IST) | Turkije | 41.26 | 28.74 | sieraden + spil naar Midden-Oosten |

### 3e. Handels- & kluishubs (`type: hub`) — klein aantal, schuiven ook onderling
| id | naam | land | lat | lon | tier | rol |
|---|---|---|---|---|---|---|
| au-hub-london | Londen (LBMA + Bank of England) | VK | 51.514 | -0.088 | 1 | prijsbenchmark; BoE-kluis (custodie); OTC-hart |
| au-hub-ny | New York (COMEX + NY Fed) | VS | 40.71 | -74.01 | 1 | futures-benchmark; NY Fed bewaart buitenlands CB-goud |
| au-hub-zurich | Zürich | Zwitserland | 47.37 | 8.54 | 1 | grootbanken + kluizen naast de Ticino-raffinage |
| au-hub-shanghai | Shanghai (SGE) | China | 31.23 | 121.47 | 1 | de put: goud stroomt China in, niet uit |
| au-hub-dubai | Dubai (DMCC) | VAE | 25.07 | 55.14 | 2 | spil Afrika ↔ India; "grijs" goud wordt hier wit |
| au-hub-singapore | Singapore | Singapore | 1.29 | 103.85 | 2 | Aziatische kluishub / doorvoer |
| au-hub-hongkong | Hongkong | Hongkong | 22.32 | 114.17 | 2 | conduit naar Shanghai (China in) |

### 3f. Consumptie (`type: market`)
| id | naam | land | lat | lon | tier | note |
|---|---|---|---|---|---|---|
| au-mkt-india | Mumbai/Delhi (sieraden) | India | 19.08 | 72.88 | 1 | grootste sieraden- + beleggingsvraag (~½ tikje onder China) |
| au-mkt-china | China (sieraden + belegging) | China | 31.23 | 121.47 | 1 | via Shanghai; wereldgrootste vraag |
| au-mkt-turkije | Istanbul/Turkije | Turkije | 41.01 | 28.98 | 2 | sieraden + inflatie-belegging |
| au-mkt-me | Midden-Oosten (Dubai souk) | VAE | 25.27 | 55.30 | 2 | sieraden; overlapt met de Dubai-hub |
| au-mkt-tech | Japan/Korea/Taiwan (tech) | Japan | 35.68 | 139.76 | 3 | elektronica — klein aandeel |
| au-mkt-west | Westerse belegging (baren/munten) | Duitsland | 50.11 | 8.68 | 3 | Duitsland/VS — fysieke belegging |

### 3g. Recycling (`type: recycler`)
*Schroot → terug naar raffinage. Recycling levert wereldwijd ~1.300-1.400 t/jr — een grote "tweede mijn".*

| id | naam | land | lat | lon | note |
|---|---|---|---|---|---|
| au-rec-italie | Arezzo/Vicenza (sieraadschroot) | Italië | 43.46 | 11.88 | Europees sieraadcentrum → Zwitserse raffinage |
| au-rec-india | India (schroot) | India | 28.10 | 76.90 | terug via MMTC-PAMP |
| au-rec-me | Midden-Oosten/Turkije (schroot) | VAE | 25.07 | 55.14 | terug via Dubai |

### 3h. Centrale banken — **optionele toggle-laag** (`type: cb`) — LAR-402
*Node-grootte = voorraad (t). Stromen = huidige inkoop/repatriëring. Peiljaar voorraden ~eind 2024.*

| id | naam | land | lat | lon | voorraad t | rol |
|---|---|---|---|---|---|---|
| au-cb-us | Fed (Fort Knox/West Point/Denver + NY Fed) | VS | 37.13 | -85.95 | ~8.130 | grootste; bewaart ook buitenlands goud (NY Fed) |
| au-cb-de | Bundesbank (Frankfurt) | Duitsland | 50.11 | 8.68 | ~3.350 | repatrieerde 2013-17 uit NY/Parijs |
| au-cb-it | Banca d'Italia (Rome) | Italië | 41.90 | 12.50 | ~2.450 | — |
| au-cb-fr | Banque de France (Parijs) | Frankrijk | 48.86 | 2.35 | ~2.440 | — |
| au-cb-ru | Bank Rusland (Moskou) | Rusland | 55.75 | 37.62 | ~2.330 | absorbeert eigen mijnproductie |
| au-cb-cn | PBoC (Beijing) | China | 39.90 | 116.40 | ~2.280 | koopt gestaag door; ondergerapporteerd |
| au-cb-ch | SNB (Bern) | Zwitserland | 46.95 | 7.44 | ~1.040 | — |
| au-cb-jp | Bank of Japan (Tokio) | Japan | 35.68 | 139.76 | ~846 | — |
| au-cb-in | RBI (Delhi) | India | 28.61 | 77.21 | ~880 | **repatrieerde 100+ t uit BoE in 2024** |
| au-cb-nl | DNB (Amsterdam) | Nederland | 52.37 | 4.90 | ~612 | grootste deel al thuis/NY |
| au-cb-pl | NBP (Warschau) | Polen | 52.23 | 21.01 | ~450 | **grootste koper 2024 (+90 t)**; repatrieerde 2019 uit Londen |
| au-cb-tr | CBRT (Ankara) | Turkije | 39.93 | 32.86 | ~600 | wisselt koper/verkoper (binnenlandse dynamiek) |

## 4. Stromen (flows) — indicatief, ~t/jr
*Modi: **`air`** (intercontinentaal, dominant — nieuwe great-circle-modus), **`road`/`rail`** (korte EU-hops
via land-A*, bv. ZRH→Ticino, Londen↔Frankfurt). `via` = gateway-luchthavens (+ ZRH als trechter).*

### 4a. Mijn-doré → raffinage (stage `erts`) — **de grote convergentie op Ticino**
| from | to | ~t/jr | mode | via | note |
|---|---|---|---|---|---|
| au-boddington | au-ref-perth | 27 | air | au-air-per | AU → Perth Mint |
| au-cadia | au-ref-perth | 24 | air | au-air-per | |
| au-kalgoorlie | au-ref-perth | 15 | air | au-air-per | |
| au-tarkwa | au-ref-valcambi | 17 | air | au-air-acc, au-air-zrh | West-Afrika → Ticino |
| au-obuasi | au-ref-valcambi | 11 | air | au-air-acc, au-air-zrh | |
| au-loulo | au-ref-argor | 20 | air | au-air-acc, au-air-zrh | Mali industrieel |
| au-mponeng | au-ref-rand | 8 | air | au-air-jnb | ZA → Rand Refinery |
| au-detour | au-ref-rcm | 22 | air | au-air-yyz | Canada domestic |
| au-malartic | au-ref-valcambi | 22 | air | au-air-yyz, au-air-zrh | deels naar CH |
| au-nevada | au-ref-metalor | 84 | air | au-air-jfk | VS grotendeels domestic (Metalor US) |
| au-penasquito | au-ref-valcambi | 16 | air | au-air-gru, au-air-zrh | Mexico → CH |
| au-paracatu | au-ref-argor | 15 | air | au-air-gru, au-air-zrh | Brazilië → CH |
| au-yanacocha | au-ref-valcambi | 10 | air | au-air-gru, au-air-zrh | Peru → CH |
| au-lihir | au-ref-perth | 18 | air | au-air-per | PNG → Perth |
| au-grasberg | au-ref-china | 40 | air | au-air-hkg | Indonesië koper-goud → deels China/Gresik |
| au-shandong | au-ref-china | 100 | air | — | China insulair (binnenlands) |
| au-olimpiada | au-cb-ru | 44 | air | — | Rusland absorbeert eigen mijn |
| au-muruntau | au-cb-... | 83 | air | — | Oezbekistan grotendeels binnenlands (evt. eigen CB) |
| au-sudan | au-ref-dubai | 20 | air | au-air-dxb | artisanaal/"grijs" → Dubai wit gewassen |
| au-ref-valcambi (doré-import breed) | — | — | — | — | *(zie mijn-rijen: meerdere continenten convergeren op Valcambi/Argor)* |

### 4b. Geraffineerde baren → hubs (stage `raffinaat`) — uitwaaieren vanuit Zwitserland
| from | to | ~t/jr | mode | via | note |
|---|---|---|---|---|---|
| au-ref-valcambi | au-hub-london | 300 | air | au-air-zrh, au-air-lhr | ZRH → LHR → LBMA/BoE |
| au-ref-valcambi | au-hub-ny | 150 | air | au-air-zrh, au-air-jfk | → COMEX |
| au-ref-argor | au-hub-dubai | 120 | air | au-air-zrh, au-air-dxb | → Dubai |
| au-ref-pamp | au-hub-singapore | 80 | air | au-air-zrh, au-air-sin | → Azië |
| au-ref-valcambi | au-hub-hongkong | 200 | air | au-air-zrh, au-air-hkg | → HK, conduit China |
| au-ref-perth | au-hub-london | 120 | air | au-air-per, au-air-lhr | AU-baren → Londen |
| au-ref-rand | au-hub-london | 150 | air | au-air-jnb, au-air-lhr | ZA-baren → Londen |

### 4c. Interbancaire kluisstromen hub↔hub (stage `raffinaat`)
| from | to | ~t/jr | mode | via | note |
|---|---|---|---|---|---|
| au-hub-london | au-hub-zurich | 250 | air | au-air-lhr, au-air-zrh | Londen ↔ Zürich (de klassieke as) |
| au-hub-zurich | au-hub-ny | 120 | air | au-air-zrh, au-air-jfk | arbitrage/EFP naar COMEX |
| au-hub-london | au-hub-ny | 200 | air | au-air-lhr, au-air-jfk | 2024-2025 grote fysieke verschuiving LDN→NY |

### 4d. Hub → consumptie / China-put (stage `product`)
| from | to | ~t/jr | mode | via | note |
|---|---|---|---|---|---|
| au-hub-hongkong | au-mkt-china | 300 | air | — | **HK → Shanghai/China: eenrichting** |
| au-hub-shanghai | au-mkt-china | 250 | rail | — | binnen China (SGE → sieraden) |
| au-hub-london | au-mkt-india | 200 | air | au-air-lhr, au-air-bom | Londen → India sieraden |
| au-hub-dubai | au-mkt-india | 180 | air | au-air-dxb, au-air-bom | Dubai → India corridor |
| au-hub-dubai | au-mkt-me | 120 | road | — | souk-consumptie |
| au-ref-mmtc | au-mkt-india | 150 | rail | — | binnenlands geraffineerd → sieraden |
| au-hub-zurich | au-mkt-turkije | 90 | air | au-air-zrh, au-air-ist | Turkije sieraden |
| au-ref-japan | au-mkt-tech | 40 | road | — | tech-goud |
| au-ref-valcambi | au-mkt-west | 120 | rail | — | belegging baren/munten Europa |

### 4e. Recycling → raffinage (stage `erts`, feedstock terug)
| from | to | ~t/jr | mode | via | note |
|---|---|---|---|---|---|
| au-rec-italie | au-ref-valcambi | 120 | road | — | Arezzo/Vicenza-schroot → Ticino (kort, over land) |
| au-rec-india | au-ref-mmtc | 100 | rail | — | India-schroot |
| au-rec-me | au-ref-dubai | 90 | road | — | ME/Turkije-schroot → Dubai |

### 4f. Centrale-bank-laag (optioneel — LAR-402, stage `product`)
| from | to | ~t/jr | mode | via | note |
|---|---|---|---|---|---|
| au-hub-london | au-cb-pl | 90 | air | au-air-lhr, au-air-zrh | Polen: grootste koper 2024 + repatriëring |
| au-hub-london | au-cb-in | 100 | air | au-air-lhr, au-air-del | India repatrieerde 100+ t uit BoE (2024) |
| au-hub-shanghai | au-cb-cn | 44 | rail | — | PBoC accumuleert binnenlands |
| au-hub-zurich | au-cb-tr | 20 | air | au-air-zrh, au-air-ist | Turkije (netto wisselend) |
| au-cb-us | au-cb-us | — | — | — | *nuance: veel "koop" is titeloverdracht ín een kluis (blijft in Londen/NY) — als annotatie, niet als boog* |

## 5. Knelpunten & de "knijp"
- Goud kent **geen zeestraat-knelpunt** (het vliegt). De knijp is **institutioneel/geografisch**:
  de **Zwitserse (Ticino) raffinage** — ~⅔ van de wereld door vier huizen. Dít is voor goud wat
  Malakka + Chinese raffinage voor lithium zijn.
- Geen nieuwe `wp-*` uit `_chokepoints.js` nodig (die zijn voor zee/land). Wel: **ZRH als
  verplicht `via`-knooppunt** waar de doré-bogen samenknijpen — dezelfde lane/anker-logica als de
  zeeknelpunten zorgt dan voor het visuele "samenknijpen op één punt".
- Tweede knijp-motief: **China als eenrichtings-put** (pijlen naar binnen via HK/Shanghai, niets terug).

## 6. Emergent plaatje-check (de lat bij oplevering — LAR-403)
1. Mijn-stippen over **álle** continenten, allemaal ongeveer even groot — geen enkel land domineert.
2. Een spectaculaire **convergentie van doré-luchtbogen** uit de hele wereld op **één hoekje Ticino**.
3. Vanuit Zwitserland waaieren baren uit naar een kleine ring hubs (Londen/NY/Zürich/Shanghai/Dubai/
   Singapore/HK) die **ook onderling** verbonden zijn (Londen↔Zürich↔NY).
4. **China = pijlen naar binnen, niets naar buiten** (HK→Shanghai eenrichting).
5. **India = grote consumptie-instroom** (Londen + Dubai) + recycling terug.
6. Toggle **centrale banken** → voorraad-nodes (VS veruit grootst) + de huidige inkoopgolf
   (Polen/India/China) als repatriëringsbogen.
7. Alles beweegt via **luchtbogen** (great-circle); enkele **korte weg/spoor-legs** in Europa/binnenland.

## 7. Bronnen (peiljaar ±2024)
- **USGS Mineral Commodity Summaries 2025 (Gold):** wereldmijnproductie ~3.300 t; landen-ranking
  (China 380, Rusland 310, Australië 290, Canada 200, VS 170 t).
- **World Gold Council** (gold.org/goldhub): productie per land, vraag/aanbod per land, recycling
  (~1.300-1.400 t/jr), sieradenvraag 2024 ~1.877 t, **centrale banken +1.045 t in 2024 (Polen ~90 t voorop)**.
- **Grootste mijnen 2024:** Nevada Gold Mines ~83,9 t; Muruntau ~83 t; Grasberg ~59 t; Olimpiada ~44 t.
- **Zwitserse raffinage:** ~65-70% van het wereldgoud; Valcambi grootste (cap. ~2.000 t), Argor-Heraeus
  (~1.000 t), PAMP, Metalor (swissinfo / refinery-cap-bronnen).
- **CB-voorraden:** IMF/WGC reserve-tabellen (VS ~8.133 t, Duitsland ~3.350 t, Italië/Frankrijk ~2.450 t).
- **LBMA** (Good Delivery, London vaulting) + **Metals Focus** voor hub-/kluisstromen.

## 8. Open vragen / research-TODO (vóór of tijdens `goud.js`)
- [ ] Mijn→gateway-mapping is deels aanname (welke mijn via welke luchthaven/raffinaderij) — plausibel,
  niet per contract nagetrokken. Vooral: hoeveel VS-doré blijft domestic vs. naar CH.
- [ ] Oezbekistan/Muruntau: eigen-CB-afvoer modelleren of gewoon als binnenlandse raffinage? (`au-cb-uz` toevoegen?)
- [ ] Volumes zijn indicatief; interbancaire hub↔hub-stromen (Londen↔Zürich↔NY) zijn ordes van grootte,
  geen gepubliceerde tonnages — als "illustratief" labelen.
- [ ] CB-nuance "titeloverdracht ín kluis vs. fysieke repatriëring" eerlijk annoteren (§4f).
- [ ] Dubai "grijs goud" (Sudan/artisanaal) — hoe expliciet benoemen zonder te beschuldigen.

---

## Build-handoff (naar LAR-399/400/401/402 — geen `.js` in deze issue)
- **Nieuwe `type`-markers** stylen in de rendering-laag: `airport`, `hub`(/`vault`), `cb`, `recycler`.
  (`mine`/`refinery`/`port`/`market` bestaan al.) → deel van LAR-399/401.
- **Luchtroute-modus (LAR-399):** `mode: "air"` mag **niet** door land-A\* (huidige `flows.js` stuurt
  niet-schip-legs naar `Routing.land`). Nieuwe tak: air-leg = **great-circle, opgetilde boog** (hoogte ∝
  afstand), óók in route-view. Korte EU-hops (`road`/`rail`) blijven land-A\*. Great-circle helper hoort
  in `util.js` naast `makeRouteCurve`.
- **Voyages (LAR-400):** vliegtuig-glyph/lichtpuntjes over de luchtlijnen; zelfde motor als de schepen,
  ander pad (great-circle i.p.v. zeeroute) + teller "hoeveel goud / hoeveel zendingen".
- **CB-laag (LAR-402):** aparte toggle; §3h nodes + §4f stromen; default uit zodat v1 de fysieke keten toont.
- **`goud.js` (LAR-401):** dit bestand 1-op-1 omzetten + `REGISTER` + toevoegen aan `index.html`-laadvolgorde.
