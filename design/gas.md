# Aardgas / LNG — brief (ingevuld ontwerp) — hoort bij `data/gas.js`

*Aangemaakt 2026-07-15 · peiljaar ±2023-2024. Alle volumes in **bcm/jaar** (miljard m³ gas-equivalent),
indicatief en afgerond — bedoeld om verhoudingen te tonen, geen handelsstatistiek. Wereldproductie
≈ **4000 bcm**; internationale LNG-handel ≈ **550 bcm** (~400 Mt LNG). Bronnen: IEA (Gas Market Report,
World Energy Outlook), IGU World LNG Report, EIA, Energy Institute Statistical Review 2024, GIIGNL,
bedrijfsrapportages (QatarEnergy, Cheniere, Equinor, Gazprom/Novatek). Zie §7.
Status: **uitgewerkt-ontwerp** — klaar om 1-op-1 naar `gas.js` te zetten. Milestone (Linear): `M15 · Gas`.*

> **Principe:** we vertellen geen verhaal, we modelleren de werkelijkheid — het plaatje vertelt zichzelf.
> Voor lithium/koper is de vorm "alles door China-raffinage", voor goud "alles door Zwitserland", voor
> olie "het hele net van zeestraten licht op". Voor gas is de vorm **fundamenteel bepaald door de
> natuurkunde: gas is nauwelijks te verplaatsen.** Over land zit het vast in **pijpleidingen** — regionaal,
> vast, *captive* (wie aan het andere eind zit is je enige klant/leverancier). De enige manier om gas
> écht globaal te maken is het **vloeibaar maken tot LNG** (−162 °C) in een handvol peperdure
> exportterminals, het per gekoelde tanker te verschepen en aan de andere kant te *hervergassen*. Die
> **liquefactie-stap is de trechter** (institutioneel/kapitaal, geen zeestraat): pas ná vloeibaarmaking
> is een gasmolecuul een verhandelbare, omleidbare wereldgrondstof — en die capaciteit zit
> geconcentreerd bij drie polen: **VS-Golfkust, Qatar, Australië**. Daaroverheen twee levende verhalen:
> (1) de **Europa-pivot van 2022** — Nord Stream weg, Europa verving ~150 bcm Russische pijp door LNG en
> bouwde FSRU's in maanden; (2) de **Russische pivot naar het oosten** — Power of Siberia + Arctisch LNG,
> de captive Europese markt ingeruild voor de Chinese.

---

## 0. Metadata (→ `REGISTER({...})` in `gas.js`)

| veld | waarde |
|---|---|
| `id` | `gas` |
| `name` | Aardgas |
| `symbol` | CH₄ |
| `color` | `#5BB8D4` (koel gas-/vlamblauw; markers) |
| `flowColor` | `#A9E0EF` (lichter cyaan, voor de bogen tegen de donkere bol) |
| `unit` | `bcm/jaar (indicatief)` (voor de opslaglaag: `bcm voorraad`) |
| `detail` | `uitgewerkt` |
| `blurb` | Aardgas is de grondstof die je nauwelijks kunt verplaatsen. Over land zit het vast in pijpleidingen (regionaal, captive — Rusland↔Europa, Rusland→China, Centraal-Azië→China); écht globaal wordt het pas na vloeibaarmaking tot **LNG** in een handvol dure exportterminals (VS-Golfkust, Qatar, Australië) → dát is de trechter, niet een zeestraat. Sinds 2022 verving Europa Russische pijp door LNG. Qatar's LNG kan alleen via Hormuz. |

## 1. Het verhaal in 3 zinnen
1. **Gas is bijna niet te verplaatsen** → twee gescheiden leversystemen tekenen zich af op de kaart:
   **lage, donkere pijpleiding-bogen** die over land kruipen (captive, regionaal) en **heldere LNG-bogen**
   die de oceanen oversteken via de bestaande zeestraten (globaal). De liquefactie-terminals zijn de
   knopen waar het ene systeem in het andere overgaat — de trechter.
2. **Drie exportpolen domineren de LNG-wereld** (VS-Golfkust = flexibele schaliegas-cargo's; Qatar =
   North Field, alles via Hormuz; Australië → Azië), tegenover **twee vraagbekkens**: het gevestigde
   Aziatische (Japan/Korea/China/India, decennia oud) en het **nieuwe Europese** (sinds 2022).
3. **Twee her-routeringen bewegen live**: Europa dat in 2022 Russische pijp door LNG verving (FSRU's in
   maanden, TTF-prijspiek), en Rusland dat oostwaarts pivot (Power of Siberia + Arctisch LNG) — de kaart
   is geen statisch plaatje maar beweegt mee met oorlog en sancties (zoals olie's Rusland-omleiding).

## 2. De keten & stages (→ `stage`-codes; hergebruikt de bestaande stage-styling)
De drie bestaande stage-codes dragen bij gas het **pijpleiding-vs-LNG-onderscheid** — dat is precies de kern.

| stap | `stage`-code | kleur | booghoogte | inhoud |
|---|---|---|---|---|
| 1. veldgas + **pijpleidinggas** (ruw, captive) | `erts` | dof/donker | laag (kruipt over land) | veld → liquefactie-terminal (korte hop) **én** pijpleidinggas veld → markt (de captive land-arcs) |
| 2. **LNG** (vloeibaar gemaakt — de wereldwijd verhandelbare vorm) | `raffinaat` | volle gas-blauw (#5BB8D4) | midden | liquefactie-terminal → regas-poort/eilandmarkt over zee (de heldere oceaan-arcs = het verhaal) |
| 3. **hervergast, geleverd** (stroom/industrie/verwarming) | `product` | licht, bijna wit | hoog | regas-poort → binnenlandse markt (korte pijp-hop) |

> Bewuste asymmetrie (zoals olie): **pijpleidinggas** blijft `erts` tot aan de markt (er is geen
> liquefactie-transform) → lage donkere land-arcs die de captive relaties tonen. **LNG** doorloopt alle
> drie de stages. Eiland-/kustmarkten (Japan/Korea/Taiwan) krijgen de LNG-tanker rechtstreeks (`raffinaat`
> = de levering); continentale markten (Europa/China/India) landen aan de kust (`raffinaat`) en pijpen
> dan landinwaarts (`product`).

## 3. Nodes (locaties)
> Alle `type`-waarden bestaan al in de rendering-laag: `mine` (gasveld), `refinery` (**liquefactie-terminal**),
> `port` (**regas-/importterminal**), `market`, `reserve` (opslag). **Géén nieuwe marker-styling nodig.**
> Coördinaten: **west = negatief** (gecontroleerd). `share` = grof % van de wereldgasproductie (~4000 bcm)
> voor mijnen. Liquefactie- en regas-terminals dragen `coastal: true` waar ze pal aan de kade liggen zodat
> de LNG-tanker meteen de zee op/af kan.

### 3a. Winning / gasvelden (`type: mine`, met `share`) — de spreiding + het pijp-vs-LNG-verhaal
| id | naam | land | lat | lon | share | tier | operator | note |
|---|---|---|---|---|---|---|---|---|
| gas-us | VS-schalie (Appalachia/Permian/Haynesville) | VS | 31.5 | -93.8 | 24 | 1 | div. (EQT/ExxonMobil e.a.) | grootste producent; schalie voedt de Golfkust-LNG + pijp naar Mexico + binnenlands |
| gas-russia | Rusland (West-Siberië: Nadym-Pur-Taz/Yamal) | Rusland | 66.0 | 76.5 | 16 | 1 | Gazprom/Novatek | 2e producent; historische Europa-pijp, sinds 2022 pivot naar China + Arctisch LNG |
| gas-qatar | Qatar (North Field) | Qatar | 26.3 | 51.9 | 12 | 1 | QatarEnergy | 's werelds grootste gasveld (gedeeld met Iran); alle LNG via Ras Laffan → Hormuz |
| gas-iran | Iran (South Pars) | Iran | 27.6 | 52.0 | 6 | 2 | NIOC | **zelfde veld** als Qatar's North Field; grotendeels binnenlands (sancties, nauwelijks export) |
| gas-australia-nw | Australië NW Shelf/Gorgon/Ichthys | Australië | -19.6 | 116.1 | 9 | 1 | Woodside/Chevron/INPEX | offshore gas → Karratha/Darwin-LNG; top-exporteur naar Azië |
| gas-australia-qld | Australië Queensland (steenkoolgas) | Australië | -26.4 | 150.5 | 3 | 2 | Santos/Shell/Origin | CBM → Gladstone-LNG (Curtis Island) |
| gas-turkmenistan | Turkmenistan (Galkynysh) | Turkmenistan | 38.5 | 62.2 | 2 | 2 | Türkmengaz | 4e reserves ter wereld; **landlocked** → captive pijp naar China |
| gas-norway | Noorwegen (Troll/Ormen Lange) | Noorwegen | 62.0 | 3.6 | 3 | 1 | Equinor | Europa's #1 leverancier **ná** Rusland; subsea-pijp naar VK/Duitsland/België |
| gas-algeria | Algerije (Hassi R'Mel) | Algerije | 32.9 | 3.3 | 2 | 2 | Sonatrach | pijp (Transmed/Medgaz) **én** LNG (Arzew/Skikda) → Zuid-Europa |
| gas-nigeria | Nigeria (Bonny/NLNG) | Nigeria | 4.6 | 7.0 | 2 | 2 | NLNG (NNPC/Shell/TotalEnergies/Eni) | West-Afrikaans LNG → Europa/Azië; associated gas |
| gas-azerbaijan | Azerbeidzjan (Shah Deniz) | Azerbeidzjan | 39.3 | 50.9 | 1 | 3 | BP/SOCAR | Zuidelijke Gascorridor → Turkije/Italië (om Rusland heen) |
| gas-mozambique | Mozambique (Rovuma — Coral FLNG) | Mozambique | -11.0 | 40.7 | 0.5 | 3 | Eni/TotalEnergies | **project/opstartend**; Coral-Sul FLNG draait, onshore Afungi vertraagd (veiligheid) |

> Nuance voor de annotatie: **Iran** zit op hetzelfde veld als Qatar maar exporteert nauwelijks (sancties) —
> een van de scherpste "reserves ≠ export"-contrasten van de atlas (zoals Venezuela bij olie). **Turkmenistan**
> is landlocked → volledig captive aan de Chinese pijp. De VS/Rusland verbruiken het grootste deel zelf.

### 3b. Liquefactie / LNG-exportterminals (`type: refinery`, `coastal: true`) — **de trechter** (gas → LNG = `raffinaat`)
*Hier wordt captive gas een verhandelbare wereldgrondstof. Drie polen dragen het gros: VS-Golfkust (flexibele
cargo's), Qatar/Ras Laffan (het grootste complex), Australië (naar Azië). Een liquefactie-trein kost $10-20 mld.*

| id | naam | land | lat | lon | ~cap bcm/jr | tier | operator | note |
|---|---|---|---|---|---|---|---|---|
| gas-lng-sabinepass | Sabine Pass | VS | 29.73 | -93.87 | 40 | 1 | Cheniere | grootste VS-LNG-terminal (Louisiana); flexibele bestemming-cargo's |
| gas-lng-corpus | Corpus Christi + Golfkust-cluster | VS | 27.83 | -97.05 | 35 | 1 | Cheniere/Venture Global e.a. | Texas/Louisiana-export (+ Calcasieu Pass/Plaquemines/Freeport nieuwbouw) |
| gas-lng-raslaffan | Ras Laffan | Qatar | 25.90 | 51.55 | 110 | 1 | QatarEnergy | 's werelds grootste LNG-complex; **alles via Hormuz**; North Field-uitbreiding onderweg |
| gas-lng-karratha | Karratha (NW Shelf/Pluto) | Australië | -20.60 | 116.77 | 40 | 1 | Woodside | West-Australisch LNG → NO-Azië |
| gas-lng-gladstone | Gladstone (Curtis Island) | Australië | -23.77 | 151.30 | 30 | 2 | Santos/Shell/ConocoPhillips | Queensland CBM-LNG → Azië |
| gas-lng-darwin | Darwin (Ichthys/Bayu-Undan) | Australië | -12.42 | 130.87 | 15 | 2 | INPEX/Santos | Noord-Australisch LNG → Japan (kortste route) |
| gas-lng-sabetta | Sabetta (Yamal LNG) | Rusland | 71.27 | 72.06 | 25 | 2 | Novatek | Arctisch LNG; Noordelijke Zeeroute oost (zomer) / Europa west; Arctic LNG 2 gesanctioneerd |
| gas-lng-sakhalin | Sachalin-2 (Prigorodnoje) | Rusland | 46.63 | 143.40 | 15 | 2 | Gazprom (was Shell) | Russisch Pacific-LNG → Japan/Korea |
| gas-lng-arzew | Arzew/Skikda | Algerije | 35.80 | -0.27 | 20 | 2 | Sonatrach | Algerijns LNG (naast de Med-pijpleidingen) |
| gas-lng-bonny | Bonny Island (NLNG) | Nigeria | 4.42 | 7.16 | 30 | 2 | NLNG | West-Afrikaans LNG → Europa/Azië |
| gas-lng-bintulu | Bintulu (Petronas) | Maleisië | 3.20 | 113.05 | 30 | 2 | Petronas | groot ZO-Aziatisch LNG → Japan/Korea/China |

### 3c. Regas / import-terminals (`type: port`, `coastal: true`) — waar LNG landt en het net in gaat
*Europa (het nieuwe bekken) + China/India landen aan de kust en pijpen landinwaarts. Japan/Korea/Taiwan zijn
zelf kust-/eilandmarkten (zie 3d) → de tanker landt daar rechtstreeks. De Duitse FSRU's zijn hét symbool van 2022.*

| id | naam | land | lat | lon | rol |
|---|---|---|---|---|---|
| gas-regas-nl | Rotterdam/Eemshaven (Gate + EemsEnergy) | Nederland | 53.44 | 6.84 | Noordwest-Europese LNG-gateway |
| gas-regas-de | Wilhelmshaven/Brunsbüttel (FSRU's) | Duitsland | 53.60 | 8.10 | **in maanden gebouwd na 2022** — het symbool van de pivot; Duitsland had 0 LNG-terminals |
| gas-regas-uk | Isle of Grain/Milford Haven | VK | 51.45 | 0.45 | VK-import + doorvoer naar het continent (interconnector) |
| gas-regas-es | Barcelona/Sines (Iberische hub) | Spanje | 41.35 | 2.15 | grootste EU-regascapaciteit, **maar beperkte pijpuitgang noordwaarts** (het "Iberische eiland") |
| gas-regas-cn | Rudong/Yangshan (Oost-China) | China | 32.55 | 121.20 | Chinese LNG-landing (naast de pijp uit Rusland/Centraal-Azië) |
| gas-regas-in | Dahej | India | 21.70 | 72.55 | grootste Indiase regasterminal |

### 3d. Verbruiksmarkten (`type: market`) — waar het gas eindigt (`product`, of `raffinaat` voor eilandmarkten)
*Continentale markten (`gas-mkt-eu`/`-china`/`-india`) zitten landinwaarts en krijgen zowel LNG (via de regas-poort)
als pijpleidinggas. Eiland-/kustmarkten (Japan/Korea/Taiwan, `coastal: true`) krijgen de LNG-tanker rechtstreeks.*

| id | naam | land | lat | lon | tier | coastal | note |
|---|---|---|---|---|---|---|---|
| gas-mkt-eu | NW-Europa (stroom/industrie/verwarming) | Duitsland | 50.9 | 9.0 | 1 | — | **het nieuwe LNG-hart**: LNG via NL/DE/UK + Noorse/Algerijnse/Azerische pijp; TTF-benchmark |
| gas-mkt-china | China (Oost — stroom/industrie) | China | 31.0 | 117.0 | 1 | — | grootste LNG-importeur; LNG-kust + pijp uit Rusland (POS) + Centraal-Azië |
| gas-mkt-india | India (West — stroom/kunstmest) | India | 22.3 | 74.5 | 2 | — | groeiende importeur; gas ↔ kunstmest/ammoniak |
| gas-mkt-japan | Japan (Tokyo Bay) | Japan | 35.43 | 139.95 | 1 | ✓ | decennialang **#1 LNG-importeur** (post-Fukushima); volledig LNG-afhankelijk |
| gas-mkt-korea | Zuid-Korea (Incheon/Gwangyang) | Zuid-Korea | 35.99 | 126.70 | 1 | ✓ | top-3 LNG-importeur; geen eigen productie |
| gas-mkt-taiwan | Taiwan (Yong'an/Taichung) | Taiwan | 22.85 | 120.20 | 2 | ✓ | volledig LNG-afhankelijk, **weinig opslag** = kwetsbaar (blokkade-scenario) |
| gas-mkt-us | VS binnenland (stroom/industrie) | VS | 32.5 | -90.0 | 1 | — | grootste verbruiker; grotendeels **eigen productie** (Henry Hub) |
| gas-mkt-latam | Latijns-Amerika (Brazilië) | Brazilië | -23.6 | -46.4 | 3 | ✓ | LNG-import als backup bij droogte (waterkracht valt weg) |

### 3e. Opslag — **optionele toggle-laag** (`type: reserve`, `layer: reserve`)
*Gas' equivalent van de olie-SPR / goud-CB / koper-beurs. Hergebruikt het bestaande `reserve`-patroon (olie) met
**0 engine-wijziging** (`hasReserves()` is generiek op `n.type==="reserve"`; de "voorraden"-chip + amber tank-marker
verschijnen automatisch). Node-grootte ∝ √voorraad. Stromen (`layer:"reserve"`) = de **zomer-vulling**. Default uit.*

| id | naam | land | lat | lon | voorraad bcm | rol |
|---|---|---|---|---|---|---|
| gas-store-eu | EU-opslag (Rehden/Bergermeer) | Duitsland | 52.75 | 8.60 | ~100 | de **winter-vulgraad** = dé geopolitieke metric na 2022 (EU-mandaat 90% per 1 nov) |
| gas-store-ua | Oekraïne-opslag (West-Oekraïne) | Oekraïne | 48.70 | 24.00 | ~30 | grootste ondergrondse opslag van Europa; strategisch maar risicovol |
| gas-store-us | VS (Golfkust-zoutkoepels + Henry Hub) | VS | 30.20 | -92.10 | ~130 | grootste + meest liquide; zet de Henry Hub-benchmark |
| gas-store-cn | China strategische opslag | China | 38.50 | 117.00 | ~30 | in opbouw; buffer tegen LNG-prijspieken |

## 4. Stromen (flows) — indicatief, bcm/jr
*Modi: **`ship`** (LNG-tanker — bestaande zee-A\*), **`pipeline`** (captive land-arcs + korte veld→terminal- en
regas→markt-hops, bestaande land-A\* uit olie). `via` = regas-poorten/terminals + bestaande `wp-*`-vaarpunten.
**Harde regel:** elke ship-leg landt op een kustpunt (`port`/`coastal:true`/`wp-*`). **Géén nieuw chokepoint** —
gas hergebruikt de bestaande routekaart (4e grondstof na nikkel/olie/zilver-grafiet). Arctic/Med-crossings
empirisch checken bij de bouw (zoals zilver's route-bugs); alleen bij een echte kapotte leg een gas-only vaarpunt.*

### 4a. Veld → liquefactie-terminal (stage `erts`, korte pijp-hop)
| from | to | ~bcm/jr | mode | via | note |
|---|---|---|---|---|---|
| gas-us | gas-lng-sabinepass | 40 | pipeline | — | schaliegas → Golfkust-liquefactie |
| gas-us | gas-lng-corpus | 35 | pipeline | — | schaliegas → Texas-liquefactie |
| gas-qatar | gas-lng-raslaffan | 110 | pipeline | — | North Field → Ras Laffan (offshore → kust) |
| gas-australia-nw | gas-lng-karratha | 40 | pipeline | — | NW Shelf → Karratha |
| gas-australia-qld | gas-lng-gladstone | 30 | pipeline | — | CBM → Curtis Island |
| gas-australia-nw | gas-lng-darwin | 15 | pipeline | — | Ichthys → Darwin (kortste Australië→Japan-route) |
| gas-russia | gas-lng-sabetta | 25 | pipeline | — | Yamal-veld → Arctische liquefactie |
| gas-russia | gas-lng-sakhalin | 15 | pipeline | — | Sachalin-gas → Prigorodnoje |
| gas-algeria | gas-lng-arzew | 20 | pipeline | — | Hassi R'Mel → Arzew-liquefactie |
| gas-nigeria | gas-lng-bonny | 30 | pipeline | — | Nigerdelta-gas → Bonny Island |
| — | gas-lng-bintulu | 30 | pipeline | — | Maleisisch gas → Bintulu (bron als één veld gemodelleerd; zie open punt) |

### 4b. LNG-tankerstromen: liquefactie → regas-poort/eilandmarkt (stage `raffinaat`, `ship`) — **de heldere oceaan-arcs**
| from | to | ~bcm/jr | mode | via | note |
|---|---|---|---|---|---|
| gas-lng-sabinepass | gas-regas-nl | 15 | ship | wp-florida, gas-regas-nl | VS-Golfkust → NW-Europa (de post-2022-pijl) |
| gas-lng-sabinepass | gas-regas-de | 12 | ship | wp-florida, gas-regas-de | **VS → nieuwe Duitse FSRU** — het symbool van de pivot |
| gas-lng-sabinepass | gas-regas-uk | 8 | ship | wp-florida | VS → VK |
| gas-lng-corpus | gas-mkt-japan | 12 | ship | wp-panama, wp-pac-noord, gas-mkt-japan | **VS-Golfkust → Azië via Panama** (het Panama-LNG-verhaal) |
| gas-lng-corpus | gas-mkt-korea | 8 | ship | wp-panama, wp-pac-noord, wp-taiwan | idem → Korea (bij Panama-congestie om de Kaap — note) |
| gas-lng-raslaffan | gas-mkt-japan | 20 | ship | wp-hormuz, wp-malakka, wp-singapore, wp-scs, wp-taiwan, gas-mkt-japan | Qatar → Japan (Hormuz + Malakka, twee straten) |
| gas-lng-raslaffan | gas-mkt-korea | 15 | ship | wp-hormuz, wp-malakka, wp-singapore, wp-scs, wp-taiwan | Qatar → Korea |
| gas-lng-raslaffan | gas-regas-cn | 20 | ship | wp-hormuz, wp-malakka, wp-singapore, wp-scs, gas-regas-cn | Qatar → China |
| gas-lng-raslaffan | gas-regas-in | 18 | ship | wp-hormuz, gas-regas-in | Qatar → India (kort, over de Arabische Zee) |
| gas-lng-raslaffan | gas-regas-nl | 12 | ship | wp-hormuz, wp-bab, wp-rode-zee, wp-suez, wp-gibraltar, gas-regas-nl | Qatar → Europa (Suez) — post-2022-groei |
| gas-lng-karratha | gas-mkt-japan | 18 | ship | wp-lombok, wp-makassar, wp-scs, wp-taiwan, gas-mkt-japan | West-Australië → Japan |
| gas-lng-karratha | gas-regas-cn | 12 | ship | wp-lombok, wp-makassar, wp-scs, gas-regas-cn | West-Australië → China |
| gas-lng-darwin | gas-mkt-japan | 12 | ship | wp-makassar, wp-scs, wp-taiwan, gas-mkt-japan | Darwin → Japan (kortste) |
| gas-lng-gladstone | gas-mkt-korea | 10 | ship | wp-scs, wp-taiwan | Queensland → Korea/Japan (Coral Zee → Pacific) |
| gas-lng-bintulu | gas-mkt-japan | 15 | ship | wp-scs, wp-taiwan, gas-mkt-japan | Maleisië → Japan |
| gas-lng-bintulu | gas-regas-cn | 10 | ship | wp-scs, gas-regas-cn | Maleisië → China |
| gas-lng-sakhalin | gas-mkt-japan | 12 | ship | gas-mkt-japan | Sachalin → Japan (kort; Rusland's Pacific-LNG) |
| gas-lng-sabetta | gas-regas-nl | 10 | ship | gas-regas-nl | Yamal → Europa (west, om Noord-Noorwegen; Barentszzee) |
| gas-lng-sabetta | gas-regas-cn | 6 | ship | gas-regas-cn | Yamal → China via **Noordelijke Zeeroute** (alleen zomer — note; Arctic-route empirisch checken) |
| gas-lng-arzew | gas-regas-es | 12 | ship | gas-regas-es | Algerije → Spanje (kort over de West-Med) |
| gas-lng-bonny | gas-regas-nl | 12 | ship | wp-gibraltar, gas-regas-nl | Nigeria → Europa (Gibraltar) |
| gas-lng-bonny | gas-regas-in | 6 | ship | wp-kaap, gas-regas-in | Nigeria → India/Azië (om de Kaap) |

### 4c. Pijpleidinggas: veld → markt (stage `erts`, `pipeline`) — **de lage, donkere captive land-arcs**
| from | to | ~bcm/jr | mode | via | note |
|---|---|---|---|---|---|
| gas-norway | gas-mkt-eu | 30 | pipeline | — | **Noorwegen = Europa's #1 ná Rusland** (subsea → VK/DE/BE) — de dikke betrouwbare pijl |
| gas-russia | gas-mkt-eu | 8 | pipeline | — | **gekrompen restpijl** (TurkStream + resterende Oekraïne-transit) — sterk verminderd sinds 2022 |
| gas-russia | gas-mkt-china | 22 | pipeline | — | **Power of Siberia** — de oostwaartse pivot (POS-2 gepland); groeiende pijl |
| gas-turkmenistan | gas-mkt-china | 30 | pipeline | — | Centraal-Azië–China-pijp; **captive** (landlocked Turkmenistan, China = enige klant) |
| gas-algeria | gas-mkt-eu | 25 | pipeline | — | Transmed (→ Italië, via Tunesië/Sicilië) + Medgaz (→ Spanje) — Med-crossing empirisch checken |
| gas-azerbaijan | gas-mkt-eu | 10 | pipeline | — | Zuidelijke Gascorridor (Shah Deniz → TANAP → TAP → Italië) — om Rusland heen |
| gas-us | gas-mkt-us | 60 | pipeline | — | binnenlands — grootste verbruik op eigen productie (het pijp-net dat de VS zelfvoorzienend maakt) |

### 4d. Levering: regas-poort → binnenlandse markt (stage `product`, korte `pipeline`-hop) — de hoge lichte arcs
| from | to | ~bcm/jr | mode | via | note |
|---|---|---|---|---|---|
| gas-regas-nl | gas-mkt-eu | 20 | pipeline | — | Rotterdam/Eemshaven → Duits/NW-Europees net |
| gas-regas-de | gas-mkt-eu | 12 | pipeline | — | Duitse FSRU's → binnenlands net |
| gas-regas-uk | gas-mkt-eu | 6 | pipeline | — | VK → continent (interconnector, tweerichting) |
| gas-regas-es | gas-mkt-eu | 4 | pipeline | — | Spanje → Frankrijk — **dun**: de beperkte pijp over de Pyreneeën (het "Iberische eiland") |
| gas-regas-cn | gas-mkt-china | 40 | pipeline | — | Chinese kust-LNG → binnenland |
| gas-regas-in | gas-mkt-india | 18 | pipeline | — | Dahej → Indiase net (stroom/kunstmest) |

### 4e. Opslag-vulling onder de toggle (optioneel — `layer:"reserve"`, stage `erts`, `pipeline`)
*Verschijnt alleen met de toggle aan: de **zomer-vulling** van de opslag (de winter-buffer opbouwen), buiten de
dagelijkse leverstroom om — precies de olie-SPR-nuance. Default uit.*

| from | to | ~bcm/jr | mode | layer | via | note |
|---|---|---|---|---|---|---|
| gas-mkt-eu | gas-store-eu | 12 | pipeline | reserve | — | EU vult in de zomer richting het 90%-mandaat |
| gas-regas-nl | gas-store-eu | 6 | pipeline | reserve | — | LNG-instroom deels de opslag in |
| gas-mkt-eu | gas-store-ua | 4 | pipeline | reserve | — | West-Oekraïense caverns als extra buffer |
| gas-mkt-us | gas-store-us | 15 | pipeline | reserve | — | Henry Hub-zoutkoepels (de meest liquide) |
| gas-mkt-china | gas-store-cn | 6 | pipeline | reserve | — | China bouwt strategische buffer op |

## 5. Knelpunten & de "knijp"
- Gas' knijp is **institutioneel/fysisch, niet één zeestraat**: de **liquefactie-capaciteit** (VS-Golfkust/Qatar/
  Australië) bepaalt hoeveel gas globaal verhandelbaar is. Dat draagt via een `tension`, geen `wp-`.
- **Géén nieuw chokepoint** — gas hergebruikt de bestaande zeestraten volledig: **Hormuz** (Qatar's enige
  uitgang — scherper dan olie, want gas heeft géén Yanbu/Fujairah-bypass), **Malakka/Singapore/SCS/Taiwan**
  (→ NO-Azië), **Suez/Bab/Rode Zee/Gibraltar** (Qatar/Nigeria → Europa), **Panama** (VS-Golfkust → Azië —
  het live congestie-verhaal), **Kaap** (de omleiding), **Lombok/Makassar** (Australië → Azië), plus de olie-
  vaarpunten (`wp-florida` voor de Golfkust-uitgang). Vierde grondstof (na nikkel/olie/zilver) op de bestaande kaart.
- **Empirisch te checken bij de bouw** (zoals zilver's route-bugs, niet vooraf een chokepoint toevoegen):
  1. **Arctische routes** — Yamal (Sabetta 71°N) → Europa (Barentszzee) en → China (Noordelijke Zeeroute langs
     de Siberische kust). Als de zee-A\* over de pool of dwars over land routeert → één gas-only Arctisch
     vaarpunt in een gelabeld blok (sectie J), anders niets.
  2. **Med-crossings** — Algerije → Italië/Spanje (Transmed via Sicilië-straat; Medgaz direct) als `pipeline`
     over land-A\*; als het dwars over land of de zee in schiet → route via een kustpunt of naar `gas-regas-es`.
- De **captive pijpleiding-relaties** (Rusland↔Europa was, Rusland→China, Turkmenistan→China, Norwegen→Europa)
  zijn de land-arcs die de geopolitiek dragen — geen zeestraat maar wél de kern van het verhaal (via `tensions`).

**Tensions (6) — de knijppunten die geen node zijn:**
1. `gas-t-hormuz` — **Qatar's Hormuz-afhankelijkheid**: Qatar's hele LNG-export (~20% van de wereld) moet door
   Hormuz — géén bypass (anders dan olie's Yanbu/Fujairah). De scherpste enkelvoudige zeestraat-afhankelijkheid van de atlas.
2. `gas-t-liquefaction` — **de liquefactie-flessenhals**: gas wordt pas globaal verhandelbaar ná vloeibaarmaking;
   die dure capaciteit zit bij een handvol terminals (VS-Golfkust/Qatar/Australië) → dát is de trechter, niet een straat.
3. `gas-t-europe-pivot` — **de Europa-pivot 2022**: Nord Stream-sabotage + Oekraïne-transit weg → Europa verving
   ~150 bcm Russische pijp door LNG (US/Qatar) + FSRU's in maanden; TTF-prijspiek (najaar 2022).
4. `gas-t-russia-east` — **Rusland's oostwaartse pivot**: Power of Siberia (+ POS-2 gepland) + Arctisch LNG
   (Yamal/Arctic LNG 2, gesanctioneerd) — de Europese captive-markt ingeruild voor de Chinese; pijp is traag te bouwen.
5. `gas-t-price-zones` — **drie prijszones**: Henry Hub (VS, goedkoop) ↔ TTF (Europa) ↔ JKM (Azië); LNG-arbitrage
   koppelt ze, maar transport/terminalcapaciteit houdt ze gescheiden → cargo's varen naar de hoogste prijs.
6. `gas-t-panama` — **Panama-LNG-knelpunt**: VS-Golfkust→Azië-cargo's vechten om kanaal-slots; de droogte van
   2023-24 dwong omleidingen via Suez of de Kaap — een live knelpunt-verhaal (en een gas-eigen accent bovenop olie).

## 6. Emergent plaatje-check (de lat bij oplevering)
1. **Twee zichtbaar verschillende leversystemen**: lage donkere **pijpleiding-arcs** die over land kruipen
   (Noorwegen→EU, Rusland→China, Turkmenistan→China, US-binnenlands) náást heldere **LNG-oceaan-arcs**.
2. **Hormuz gloeit op** als Qatar's enige uitgang — alle Ras Laffan-cargo's wringen erdoorheen (scherper dan
   olie: géén bypass-pijp ernaast).
3. **Drie exportpolen** stralen uit: VS-Golfkust (cargo's fannen zowel oostwaarts naar Europa als westwaarts
   via Panama naar Azië), Qatar (Hormuz → Azië + Suez → Europa), Australië (→ NO-Azië via Lombok/Makassar).
4. **De Europa-pivot**: een waaier LNG-arcs die op de **nieuwe Duitse/Nederlandse FSRU's** landt, met de
   **Russische pijp naar Europa gekrompen tot een dun draadje** en een **dikke nieuwe Power-of-Siberia-pijl** naar China.
5. **Reserves ≠ export**: Iran (zelfde veld als Qatar) met nauwelijks een pijl; Turkmenistan met één captive
   draad naar China.
6. Toggle **opslag** → vier voorraad-nodes (EU/Oekraïne/VS/China) + de **zomer-vul-stromen** (de winterbuffer
   zichtbaar gemaakt) — buiten de dagelijkse leverstroom om (de olie-SPR-nuance).
7. Alles beweegt over **zee (LNG-tanker) + land (pijpleiding)** — géén luchtbogen (dat is goud/PGM).

## 7. Bronnen (peiljaar ±2023-2024)
- **IEA** — Gas Market Report / World Energy Outlook 2024: LNG-handel ~550 bcm, de post-2022 Europese
  vraagverschuiving, de drie prijshubs (Henry Hub/TTF/JKM), Power of Siberia-volumes.
- **IGU World LNG Report 2024** + **GIIGNL Annual Report**: exporteurs-ranking (VS #1 / Qatar / Australië),
  importeurs (China #1 / Japan / Korea), liquefactie- en regascapaciteit per terminal.
- **EIA**: US LNG-export (Sabine Pass/Corpus Christi/Calcasieu Pass/Plaquemines/Freeport), Henry Hub,
  chokepoint-briefs (Hormuz ~20% van LNG, Panama-congestie 2023-24).
- **Energy Institute Statistical Review of World Energy 2024**: productie/consumptie per land (~4000 bcm wereld),
  pijpleiding- vs LNG-handel.
- **Bedrijfs-/bron-specifiek**: QatarEnergy (North Field/Ras Laffan + uitbreiding), Cheniere, Equinor (Noorse
  pijp), Gazprom/Novatek (Yamal/Sabetta/Sachalin/POS), Sonatrach (Transmed/Medgaz), NLNG, Petronas.
- **2022**: Nord Stream-sabotage (sep 2022), EU-gasopslag-mandaat (90% per 1 nov), FSRU-versnelling.

## 8. Open vragen / research-TODO (vóór of tijdens `gas.js`)
- [ ] Volumes zijn indicatief/afgerond in bcm-equivalent; de exacte cargo-verdeling (welk Qatar/US/Australië-
  volume naar welke markt) schommelt met de spotmarkt/arbitrage — als "illustratief" labelen.
- [ ] `gas-lng-bintulu` heeft geen aparte veld-mine (Maleisisch gas gemodelleerd als bron bij de terminal);
  overweeg een `gas-malaysia`-mine als de kaart daar te "leeg" oogt. Idem eventueel Indonesië (Tangguh/Bontang).
- [ ] **Arctic-routes** (Sabetta → Europa/China): empirisch checken of de zee-A\* de Barentszzee/Noordelijke
  Zeeroute vaart of over de pool/land schiet → dan één gas-only Arctisch vaarpunt (gelabeld blok, sectie J).
- [ ] **Med-pijpleidingen** (Algerije → Italië/Spanje): `pipeline` over land-A\* kan de Sicilië-straat/West-Med
  raar routeren → evt. via een kustpunt of naar `gas-regas-es` in plaats van rechtstreeks `gas-mkt-eu`.
- [ ] Opslag-tonnages (EU ~100 bcm werkvolume, US ~130 bcm) zijn ordes van grootte — als "illustratief" labelen.
- [ ] `symbol: CH₄` — controleren dat het teken (₄ subscript) correct rendert in de UI-badge; anders `LNG` of `Gas`.

---

## Build-handoff (naar de bouw-issues)
- **Nieuwe 12e grondstof** — er is nog géén `data/gas.js`: aanmaken + `<script src="data/gas.js">` toevoegen aan
  `index.html` (ná `silver.js`, regel 96) + gas-sanity-check in `build-standalone.py`. Tweede échte toevoeging
  na zilver (M13); dit is het structurele "anders" t.o.v. het basis→uitgewerkt-patroon → aparte registratie-issue.
- **Géén nieuwe marker-types** — `mine`/`refinery`/`port`/`market`/`reserve` bestaan allemaal al (liquefactie =
  `refinery`, regas = `port`, opslag = `reserve`).
- **Géén nieuwe render-modus** — schip + `pipeline` (beide bestaan; `pipeline` kwam met olie). Hergebruikt zee-A\*/
  land-A\* + scheeps-voyages.
- **Géén nieuw chokepoint** (default) — hergebruikt bestaande `wp-*` (Hormuz/Malakka/Suez/Bab/Rode Zee/Gibraltar/
  Panama/Kaap/Lombok/Makassar/SCS/Taiwan/Florida). Vierde grondstof na nikkel/olie/zilver op de bestaande kaart.
  Alléén een gas-only Arctisch vaarpunt appenden (gelabeld blok, sectie J) als de Yamal-route empirisch kapot is.
- **Opslag-laag** — hergebruik de bestaande olie-`reserve`-toggle (`type:"reserve"`/`layer:"reserve"`,
  `showReserves`) met **0 engine-wijziging** (`hasReserves()` generiek — geverifieerd in `src/main.js:23`).
  4 reserve-nodes + 5 `layer:"reserve"`-vul-flows; de "voorraden"-chip + amber tank-marker verschijnen automatisch.
- **Co-locatie-check** — houd gas-nodes in dezelfde cel ~30-45 km uit elkaar (regas-cn vs. mkt-china; regas-in vs.
  mkt-india; store-cn vs. mkt-china) zodat geen `degDist:0`-arc ontstaat.
- **Parallel (sectie J):** een grafiet-sessie loopt (M14). Alléén eigen bestanden stagen (`data/gas.js` +
  `design/gas.md`); `index.html`- en `build-standalone.py`-toevoegingen als losse hunks/blokken, en checken dat
  ze niet dirty zijn van de grafiet-sessie vóór het committen.
