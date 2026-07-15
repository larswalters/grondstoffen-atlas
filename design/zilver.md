# Zilver — brief (ingevuld ontwerp) — hoort bij `data/silver.js`

*Peiljaar ±2023-2024. Alle volumes in **t/jaar** (metrische ton fijn zilver), indicatief en afgerond —
bedoeld om verhoudingen te tonen, geen handelsstatistiek. Wereldmijnproductie ≈ **26.000 t** (~830 Moz;
USGS/Silver Institute 2024). Bronnen: The Silver Institute / Metals Focus "World Silver Survey", USGS
Mineral Commodity Summaries 2025, LBMA, bedrijfsrapportages (Fresnillo, Peñoles, KGHM). Zie §7.
Status: **uitgewerkt-ontwerp** — klaar om 1-op-1 naar `silver.js` te zetten.*

> **Principe:** we vertellen geen verhaal, we modelleren de werkelijkheid — het plaatje vertelt zichzelf.
> Voor lithium/koper is de vorm "alles door China-raffinage", voor goud "alles door Zwitserland". Voor
> zilver is de vorm **fundamenteel anders**: er is **geen winnings-trechter** — ~70-75% van al het zilver
> valt als **bijproduct** uit zink/lood-, koper- en goudmijnen, dus het aanbod reageert nauwelijks op de
> zilverprijs. De concentratie zit juist **downstream aan de vraagkant**: de energietransitie trekt zilver
> naar de Chinese **zonnepanelen-industrie**, en al enkele jaren op rij is de vraag groter dan het aanbod →
> een **structureel tekort** dat de bovengrondse **kluisvoorraden** (Londen/New York/Shanghai) aftapt.

---

## 0. Metadata (→ `REGISTER({...})` in `silver.js`)

| veld | waarde |
|---|---|
| `id` | `silver` |
| `name` | Zilver |
| `symbol` | Ag |
| `color` | `#B7BFC7` (koel metallic zilvergrijs; markers) |
| `flowColor` | `#DCE2E8` (lichter, voor de bogen tegen de donkere bol) |
| `unit` | `t/jaar` (voor de kluislaag: `t voorraad`) |
| `detail` | `uitgewerkt` |
| `blurb` | De meeste zilver komt niet uit zilvermijnen: ~70-75% valt als bijproduct uit zink/lood-, koper- en goudmijnen (Mexico #1, Peru, China, KGHM-Polen) → het aanbod is inelastisch. Tegelijk stuwt de energietransitie de industriële vraag — zonnepanelen voorop, geconcentreerd in China — naar recordhoogte. Resultaat: een structureel tekort dat de kluisvoorraden (LBMA-Londen, COMEX-New York, Shanghai) aftapt. |

## 1. Het verhaal in 3 zinnen
1. **Zilver heeft geen winnings-trechter:** ~70-75% is **bijproduct** van zink/lood-, koper- en goudmijnen
   (Mexico, Peru, China, KGHM-Polen, Chili, Australië, Bolivia, Kazachstan) — de zilver-stippen zitten
   bovenop andermans mijnen, en je kunt zilver niet "opschalen" zonder meer zink of koper te willen.
2. De echte concentratie zit **downstream aan de vraagkant**: industrie is >50% van de vraag, met
   **zonnepanelen (fotovoltaïsch)** als grootste én snelst groeiende toepassing (~1/5 van de wereldvraag),
   geconcentreerd in de **Chinese zonnecel-industrie** — plus elektronica/EV, sieraden (India) en belegging.
3. Al enkele jaren is de vraag > het aanbod → een **structureel tekort** dat wordt gedicht door de
   bovengrondse **kluisvoorraden** (LBMA-Londen, COMEX-New York, Shanghai) af te tappen; die kluislaag is
   de optionele toggle (hergebruikt het bestaande `exchange`-patroon van koper/nikkel).

## 2. De keten & stages (→ `stage`-codes; hergebruikt de bestaande stage-styling)
Zilver kent geen "cel/kathode"; we hergebruiken de drie bestaande codes en vullen ze zilver-logisch in.

| stap | `stage`-code | kleur | booghoogte | inhoud |
|---|---|---|---|---|
| 1. mijn (bijproduct) → **doré/concentraat** | `erts` | dof/donkergrijs | laag | mijn → smelter/raffinaderij; óók recyclingschroot → raffinage |
| 2. **good-delivery baar** (1000 oz) | `raffinaat` | volle zilverkleur (#B7BFC7) | midden | raffinaderij → kluizen; interbancaire kluisstromen |
| 3. **industrieel eindproduct** | `product` | licht, bijna wit | hoog | kluis/raffinaderij → solar/elektronica/sieraden |

## 3. Nodes (locaties)
> Alle `type`-waarden bestaan al in de rendering-laag: `mine`/`refinery`/`port`/`market`/`recycler`/`exchange`.
> **Géén nieuwe marker-styling nodig.** Coördinaten: **west = negatief** (gecontroleerd). Shares zijn %
> van ~26.000 t wereldmijnproductie. Elke mijn krijgt een `byproduct`-note (van welk hoofdmetaal het valt).

### 3a. Winning (`type: mine`, met `share`) — de spreiding + het bijproduct-verhaal ís de boodschap
*Som hieronder ≈ 45% wereld; de rest is verspreid klein spul (bewust niet allemaal apart geprikt, zoals bij goud).
`note` benoemt telkens het **hoofdmetaal** waar het zilver een bijproduct van is (of "primair").*

| id | naam | land | lat | lon | share | tier | operator | ~t/jr | bijproduct van |
|---|---|---|---|---|---|---|---|---|---|
| ag-fresnillo | Fresnillo/Saucito | Mexico | 23.18 | -102.87 | 4.0% | 1 | Fresnillo plc | 1050 | **primair** (grootste primaire zilverbedrijf ter wereld) |
| ag-penasquito | Peñasquito | Mexico | 24.66 | -101.55 | 2.5% | 1 | Newmont | 650 | goud + zink/lood (poly-metaal) |
| ag-china | China lood-zink/koper-cluster (Yunnan/Henan) | China | 26.60 | 101.80 | 13.0% | 1 | div. (staat + privaat) | 3400 | lood/zink + koper; #2-producent, grotendeels binnenlands |
| ag-uchucchacua | Uchucchacua | Peru | -10.62 | -76.92 | 1.5% | 2 | Buenaventura | 400 | **primair** (+ lood/zink) |
| ag-antamina | Antamina | Peru | -9.53 | -77.05 | 2.0% | 1 | Glencore/BHP/Teck JV | 520 | koper/zink (concentraat draagt het zilver mee) |
| ag-kghm | KGHM (Lubin/Polkowice) | Polen | 51.40 | 16.20 | 5.0% | 1 | KGHM | 1300 | **koper** — grootste bijproduct-zilverbron ter wereld (één bedrijf) |
| ag-chile-cu | Chileense koper (Escondida-cluster) | Chili | -24.27 | -69.07 | 4.0% | 1 | BHP e.a. | 1050 | **koper** (zilver reist mee met het concentraat) |
| ag-cannington | Cannington | Australië | -21.87 | 140.92 | 1.5% | 2 | South32 | 400 | lood/zink (één van 's werelds grootste Ag-mijnen) |
| ag-sancristobal | San Cristóbal | Bolivia | -21.05 | -67.15 | 1.5% | 2 | Sumitomo | 400 | zink/lood |
| ag-kazzinc | Kazzinc (Ridder) | Kazachstan | 50.20 | 83.53 | 1.5% | 2 | Glencore/Kazzinc | 400 | zink/lood + koper |
| ag-greens-creek | Greens Creek | VS (Alaska) | 58.07 | -134.63 | 1.0% | 2 | Hecla | 270 | **primair** (+ zink) |
| ag-us-cu | Bingham Canyon (Kennecott) | VS (Utah) | 40.52 | -112.15 | 1.0% | 3 | Rio Tinto | 260 | koper/goud |
| ag-garpenberg | Garpenberg | Zweden | 60.30 | 16.10 | 1.0% | 3 | Boliden | 260 | zink/lood |
| ag-dukat | Dukat | Rusland | 62.55 | 155.50 | 1.5% | 2 | Polymetal | 400 | **primair**; blijft grotendeels binnenlands |

> Country-nuance voor de annotatie: **China** (#2) en **Rusland** raffineren en verbruiken grotendeels
> binnenlands (gesloten systemen). De niet-Chinese keten convergeert op een handvol raffinaderijen —
> waarvan **Peñoles (Mexico)** en **KGHM (Polen)** veruit de grootste zijn.

### 3b. Winning — projecten
*(n.v.t. voor zilver v1 — de spreiding + het bijproduct-karakter zitten al in de actieve mijnen. Zilver-aanbod
groeit sowieso nauwelijks door nieuwe primaire mijnen: het volgt de zink/koper/goud-cyclus.)*

### 3c. Raffinage / smelters (`type: refinery`) — waar doré/concentraat good-delivery baar wordt
*Zilver komt vrij in twee stromen: primaire doré → edelmetaal-raffinage, én bijproduct in base-metaal-smelters
(zink/koper/lood) die het zilver terugwinnen. Peñoles (Torreón) = 's werelds grootste zilverraffinaderij.*

| id | naam | land | lat | lon | ~cap t/jr | tier | operator | note |
|---|---|---|---|---|---|---|---|---|
| ag-ref-penoles | Met-Mex Peñoles (Torreón) | Mexico | 25.55 | -103.42 | ~1800 | 1 | Industrias Peñoles | **grootste zilverraffinaderij ter wereld** — de niet-Chinese trechter |
| ag-ref-kghm | KGHM Głogów-smelter | Polen | 51.66 | 16.08 | ~1300 | 1 | KGHM | grootste zilver uit één koper-smelter |
| ag-ref-china | China-smelters (Jiangxi/Henan) | China | 28.68 | 115.86 | ~4000 | 1 | div. | **insulair** — raffineert binnenlands + geïmporteerd concentraat |
| ag-ref-korea | Korea Zinc / LS-Nikko (Onsan) | Zuid-Korea | 35.42 | 129.34 | ~2000 | 1 | Korea Zinc | grootste base-metaal-smeltcomplex; zilver uit Zn/Pb-concentraat wereldwijd |
| ag-ref-valcambi | Valcambi (Balerna, Ticino) | Zwitserland | 45.845 | 9.005 | ~600 | 2 | Valcambi | good-delivery baren (ook goud); premium/belegging |
| ag-ref-aurubis | Aurubis (Hamburg) | Duitsland | 53.53 | 10.05 | ~1200 | 2 | Aurubis | Europa's grootste koper-smelter; zilver als bijproduct |
| ag-ref-japan | Mitsubishi/Dowa | Japan | 34.90 | 136.60 | ~500 | 3 | Mitsubishi Materials | tech-zilver + import-concentraat |
| ag-ref-us | Asarco / Amarillo | VS | 35.20 | -101.80 | ~300 | 3 | Grupo México (Asarco) | Noord-Amerikaanse doré + koper-bijproduct |
| ag-ref-boliden | Boliden Rönnskär | Zweden | 64.70 | 21.23 | ~400 | 3 | Boliden | Scandinavisch Zn/Cu-smeltcomplex |

### 3d. Havens / gateways (`type: port`) — waar het zilver de zee op gaat
*Zilver reist als **industrieel metaal over zee/land** — niet door de lucht (het is ~1/80 van goud's waarde per gram).
Havens zijn `via`-punten in de scheepsstromen (hergebruikt de bestaande zee-A\*-routes).*

| id | naam | land | lat | lon | rol |
|---|---|---|---|---|---|
| ag-port-manzanillo | Manzanillo | Mexico | 19.05 | -104.32 | Pacific-uitgang Mexico → Azië |
| ag-port-veracruz | Veracruz | Mexico | 19.16 | -96.13 | Atlantische uitgang Mexico → VS/Europa |
| ag-port-callao | Callao (Lima) | Peru | -12.05 | -77.15 | Peruaans concentraat → Azië/Europa |
| ag-port-antofagasta | Antofagasta/Mejillones | Chili | -23.65 | -70.40 | Chileens + Boliviaans concentraat → Azië |
| ag-port-townsville | Townsville | Australië | -19.25 | 146.82 | Cannington-lood/zilver → Azië |
| ag-port-gdansk | Gdańsk | Polen | 54.35 | 18.65 | Baltische uitgang (KGHM/Kazzinc-baren) |
| ag-port-rotterdam | Rotterdam | Nederland | 51.95 | 4.14 | Europese gateway → Londen/industrie |
| ag-port-shanghai | Shanghai/Ningbo | China | 30.60 | 122.10 | Chinese invoer van concentraat + baren |
| ag-port-nhava | Nhava Sheva (Mumbai) | India | 18.95 | 73.00 | India-invoer (sieraden + solar) |
| ag-port-lb | Los Angeles/Long Beach | VS | 33.74 | -118.26 | VS-westkust invoer/doorvoer |

### 3e. Consumptie / eindmarkt (`type: market`)
| id | naam | land | lat | lon | tier | note |
|---|---|---|---|---|---|---|
| ag-mkt-china-solar | China — zonnepanelen (PV) | China | 31.30 | 120.60 | 1 | **de grootste én snelst groeiende vraag** (Jiangsu/Zhejiang-cluster) |
| ag-mkt-china-elec | China — elektronica/EV | China | 22.55 | 114.06 | 1 | Shenzhen; contacten, connectoren, EV-vermogenselektronica |
| ag-mkt-india | India — sieraden + zilverwerk | India | 19.08 | 72.88 | 1 | grootste sieraden-/beleggingsvraag; nu ook solar |
| ag-mkt-eu | EU — industrie (PV/elektronica) | Duitsland | 50.90 | 7.00 | 2 | fotovoltaïsch + elektronica + auto |
| ag-mkt-us | VS — industrie + belegging | VS | 40.70 | -74.00 | 2 | elektronica, solar, munten/baren |
| ag-mkt-japan-korea | Japan/Korea — elektronica | Japan | 35.68 | 139.76 | 2 | halfgeleiders, contacten |

### 3f. Recycling (`type: recycler`, **always-on** — koper/nikkel-patroon, géén toggle)
*Recycling levert ~15-18% van het totale aanbod (industrieel + fotografisch + sieraadschroot). Terug naar raffinage.*

| id | naam | land | lat | lon | note |
|---|---|---|---|---|---|
| ag-rec-eu | Umicore (Hoboken) | België | 51.17 | 4.35 | e-waste/edelmetaal-recycling → Europese raffinage |
| ag-rec-japan | Japan (urban mining) | Japan | 35.70 | 139.72 | e-waste → Mitsubishi/Dowa |
| ag-rec-us | VS schroot | VS | 40.72 | -74.05 | industrieel + fotografisch → Asarco |
| ag-rec-india | India sieraadschroot | India | 19.10 | 72.85 | terug in de sieradenketen |

### 3g. Kluis-/beursvoorraden — **optionele toggle-laag** (`type: exchange`, `layer: exchange`)
*Hergebruikt het bestaande `exchange`-patroon (koper/nikkel) met **0 engine-wijziging**. Node-grootte ∝ √voorraad.
Stromen (`layer:"exchange"`) = het **aftappen** onder het structurele tekort (kluis → industrie). Default uit.*

| id | naam | land | lat | lon | voorraad t | rol |
|---|---|---|---|---|---|---|
| ag-ex-lbma | LBMA (Londen — kluizen) | VK | 51.51 | -0.09 | ~22000 | grootste bovengrondse voorraad; OTC-hart + prijsbenchmark |
| ag-ex-comex | COMEX (New York — registered) | VS | 40.71 | -74.01 | ~9000 | futures-benchmark; "registered" (leverbaar) vs "eligible" — de nuance |
| ag-ex-sge | Shanghai (SGE/SHFE) | China | 31.23 | 121.47 | ~3000 | Chinese benchmark; voorraad trekt richting de binnenlandse solar-vraag |

## 4. Stromen (flows) — indicatief, ~t/jr
*Modi: **`ship`** (intercontinentaal — bestaande zee-A\*), **`road`/`rail`** (korte hops mijn→smelter, smelter→kluis
over land). `via` = havens + bestaande `wp-*`-vaarpunten/knelpunten. **Harde regel:** elke ship-leg landt op een
kustpunt (`port`/`wp-*`). Géén nieuw chokepoint — zilver hergebruikt de bestaande routes volledig.*

### 4a. Mijn → raffinage/smelter (stage `erts`) — doré + concentraat convergeren op een handvol smelters
| from | to | ~t/jr | mode | via | note |
|---|---|---|---|---|---|
| ag-fresnillo | ag-ref-penoles | 1050 | road | — | Mexico binnenlands → Torreón (de niet-Chinese trechter) |
| ag-penasquito | ag-ref-penoles | 650 | road | — | Mexico binnenlands |
| ag-greens-creek | ag-ref-us | 270 | ship | ag-port-lb | Alaska → VS-raffinage (Asarco) |
| ag-us-cu | ag-ref-us | 260 | road | — | Bingham Canyon koper-bijproduct → Amarillo |
| ag-uchucchacua | ag-ref-korea | 400 | ship | ag-port-callao, wp-pac-noord, wp-scs | Peru primair concentraat → Korea Zinc |
| ag-antamina | ag-ref-china | 520 | ship | ag-port-callao, wp-pac-noord, wp-scs, wp-taiwan | koperconcentraat draagt zilver → Chinese smelter |
| ag-chile-cu | ag-ref-china | 1050 | ship | ag-port-antofagasta, wp-pac-zuid, wp-pac-west, wp-scs, wp-taiwan | Chileens koperconcentraat → China (zilver reist mee) |
| ag-sancristobal | ag-ref-korea | 400 | ship | ag-port-antofagasta, wp-pac-zuid, wp-pac-west, wp-scs | Bolivia → Chileense haven → Korea |
| ag-cannington | ag-ref-korea | 400 | ship | ag-port-townsville, wp-lombok, wp-makassar, wp-scs | Australisch loodconcentraat → Korea/China |
| ag-kghm | ag-ref-kghm | 1300 | road | — | Polen binnenlands (mijn → Głogów-smelter) |
| ag-kazzinc | ag-ref-boliden | 400 | rail | — | Kazachstan → Scandinavische/Europese smelting (deels binnenlands) |
| ag-garpenberg | ag-ref-boliden | 260 | road | — | Zweden binnenlands → Rönnskär |
| ag-china | ag-ref-china | 3400 | road | — | China binnenlands (lood-zink/koper → smelter) |
| ag-dukat | ag-ref-china | 400 | ship | wp-pac-noord, wp-scs | Rusland Verre Oosten → deels export naar Azië |

### 4b. Raffinage → kluis/industrie (stage `raffinaat`) — good-delivery baren uitwaaieren
| from | to | ~t/jr | mode | via | note |
|---|---|---|---|---|---|
| ag-ref-penoles | ag-ex-comex | 900 | ship | ag-port-veracruz, wp-florida | Peñoles → COMEX/VS (grootste bilaterale zilverstroom) |
| ag-ref-penoles | ag-ex-lbma | 500 | ship | ag-port-veracruz, wp-atl-west, ag-port-rotterdam | Peñoles → LBMA Londen |
| ag-ref-kghm | ag-ex-lbma | 700 | road | ag-port-rotterdam | KGHM-baren → Londen (over land + korte zee) |
| ag-ref-valcambi | ag-ex-lbma | 300 | road | — | Zwitserse baren → Londen (belegging) |
| ag-ref-korea | ag-ex-sge | 800 | ship | wp-taiwan | Korea → Shanghai (Aziatische baren) |
| ag-ref-china | ag-ex-sge | 2500 | rail | — | China binnenlands → SGE Shanghai |
| ag-ref-aurubis | ag-mkt-eu | 900 | road | — | Aurubis → Europese industrie (direct) |

### 4c. Interbancaire kluisstromen kluis↔kluis (stage `raffinaat`)
| from | to | ~t/jr | mode | via | note |
|---|---|---|---|---|---|
| ag-ex-lbma | ag-ex-comex | 1500 | ship | ag-port-rotterdam, wp-atl-west | Londen ↔ New York (2021-2024 fysieke verschuiving door de squeeze/premies) |
| ag-ex-lbma | ag-ex-sge | 600 | ship | wp-suez, wp-rode-zee, wp-bab, wp-malakka, wp-scs | Londen → Shanghai (China trekt fysiek metaal aan) |

### 4d. Kluis/raffinage → industriële eindvraag (stage `product`) — de solar-pull
| from | to | ~t/jr | mode | via | note |
|---|---|---|---|---|---|
| ag-ex-sge | ag-mkt-china-solar | 2600 | rail | — | **de grootste pull: SGE → Chinese zonnecel-industrie** |
| ag-ex-sge | ag-mkt-china-elec | 900 | rail | — | → elektronica/EV (Shenzhen) |
| ag-ref-china | ag-mkt-china-solar | 1200 | rail | — | binnenlands geraffineerd → direct de solar-lijn in |
| ag-ex-lbma | ag-mkt-india | 700 | ship | wp-suez, wp-rode-zee, wp-bab, ag-port-nhava | Londen → India (sieraden + solar) |
| ag-ex-comex | ag-mkt-us | 800 | road | — | COMEX → VS-industrie + munten |
| ag-ref-japan | ag-mkt-japan-korea | 500 | road | — | tech-zilver → halfgeleiders |
| ag-ref-korea | ag-mkt-china-solar | 600 | ship | wp-taiwan | Koreaanse baren → Chinese solar (import onder tekort) |

### 4e. Recycling → raffinage (stage `erts`, feedstock terug)
| from | to | ~t/jr | mode | via | note |
|---|---|---|---|---|---|
| ag-rec-eu | ag-ref-aurubis | 500 | road | — | Umicore-e-waste → Europese raffinage |
| ag-rec-japan | ag-ref-japan | 400 | road | — | urban mining → Mitsubishi/Dowa |
| ag-rec-us | ag-ref-us | 400 | road | — | VS-schroot → Asarco |
| ag-rec-india | ag-mkt-india | 300 | road | — | sieraadschroot blijft in de Indiase keten |

### 4f. Kluis-aftap onder het tekort (optioneel — `layer:"exchange"`, stage `product`)
*Deze stromen verschijnen alleen met de toggle aan: het **structureel tekort** getoond als voorraad die de
kluizen verlaat richting de fysieke (industriële) markt. Default uit.*

| from | to | ~t/jr | mode | layer | via | note |
|---|---|---|---|---|---|---|
| ag-ex-lbma | ag-mkt-china-solar | 400 | ship | exchange | wp-suez, wp-rode-zee, wp-bab, wp-malakka, wp-scs | bovengrondse voorraad → solar (het gat dichten) |
| ag-ex-comex | ag-mkt-us | 300 | road | exchange | — | registered stock → industrie |
| ag-ex-sge | ag-mkt-china-solar | 500 | rail | exchange | — | Shanghai-voorraad leegloopt richting solar |

## 5. Knelpunten & de "knijp"
- Zilver heeft **géén enkel geografisch knelpunt** in de keten — anders dan lithium/koper (China-raffinage),
  goud (Zwitserland) of uranium (Russische verrijking). Dat *is* het eigen aha: de "knijp" is **tweezijdig en
  structureel**, niet geografisch:
  1. **Aanbod-inelasticiteit** — ~70-75% is bijproduct; de winning volgt de zink/koper/goud-cyclus, niet de zilverprijs.
  2. **Vraagconcentratie** — de energietransitie trekt zilver naar de **Chinese zonnepanelen-industrie** (de snelst
     groeiende, nu grootste toepassing).
- **Géén nieuwe `wp-*`/`grens-*` nodig** — zilver hergebruikt de bestaande zee/land-routes volledig (Pacific-vaarpunten,
  Panama, Gibraltar, Suez/Rode Zee/Bab, Malakka, Lombok/Makassar, Deense Straten). Derde grondstof (na nikkel/olie)
  die volledig op de bestaande routekaart draait.
- Wél zichtbaar: een lichte **convergentie op een handvol smelters** (Peñoles-Torreón, KGHM-Głogów, Korea Zinc, China)
  en een sterke **downstream-pull** naar China-solar + India-sieraden.

## 6. Emergent plaatje-check (de lat bij oplevering)
1. Mijn-stippen **bovenop andermans mijnen** verspreid over de Amerika's + Polen + Australië + China + Kazachstan —
   geen enkele winnings-trechter; de `note`'s verraden telkens "bijproduct van koper/zink/lood/goud".
2. Doré/concentraat convergeert richting een **klein aantal smelters**, met **Peñoles (Mexico)** en **KGHM (Polen)**
   als de grootste niet-Chinese knopen.
3. Een sterke **downstream-pull**: baren stromen naar de **Chinese zonnecel-industrie** (de dikste `product`-boog)
   + India (sieraden) + EU/VS/Japan (elektronica).
4. **China = grotendeels gesloten** (binnenlandse winning → smelter → SGE → solar), met daar bovenop import onder het tekort.
5. Toggle **kluisvoorraden** → drie grote voorraad-nodes (Londen veruit grootst) + de **aftap-stromen** richting
   industrie (het structurele tekort zichtbaar gemaakt).
6. Alles beweegt over **zee/land** (schepen + korte land-hops) — géén luchtbogen (dat is goud).

## 7. Bronnen (peiljaar ±2023-2024)
- **The Silver Institute / Metals Focus — World Silver Survey 2024:** wereldmijnproductie ~26.000 t (~830 Moz);
  bijproduct-aandeel ~70-75% (lood/zink ~30%, koper ~23%, goud ~15%, primair ~28%); industriële vraag >50% totaal,
  fotovoltaïsch de grootste/snelst groeiende post; meerjarig structureel tekort (vraag > aanbod).
- **USGS Mineral Commodity Summaries 2025 (Silver):** landen-ranking — Mexico #1 (~6.400 t), China #2 (~3.400 t),
  Peru #3 (~3.300 t), + Chili/Polen/Australië/Rusland/Bolivia/Kazachstan.
- **Bedrijfsrapportages:** Fresnillo plc (grootste primaire zilverproducent), Industrias Peñoles / Met-Mex Torreón
  (grootste zilverraffinaderij), KGHM (grootste bijproduct-zilver uit één koper-onderneming), Korea Zinc, Glencore/Antamina.
- **LBMA** (London vaulting-data, good-delivery) + **COMEX** (registered vs eligible warehouse stocks) voor de kluislaag.
- **2021 "silver squeeze"** (r/WallStreetBets): legde het verschil tussen papier- en fysieke markt bloot → de LBMA↔COMEX-verschuiving.

## 8. Open vragen / research-TODO (vóór of tijdens `silver.js`)
- [ ] Volumes zijn indicatief/afgerond; concentraat-routes (welke mijn naar welke smelter) zijn plausibel maar
  niet per contract nagetrokken — vooral hoeveel Peru/Chili-concentraat naar China vs. Korea vs. Japan gaat.
- [ ] China-cluster is als één node gemodelleerd (13% wereld) — evt. later splitsen in lood-zink (Yunnan/Hunan)
  vs. koper-bijproduct als de kaart te "leeg" oogt in China.
- [ ] Kluisvoorraad-tonnages (LBMA ~22.000 t, COMEX ~9.000 t) zijn ordes van grootte — als "illustratief" labelen.
- [ ] Recycling-schroot exact toewijzen aan raffinaderijen is deels aanname (Umicore/Dowa/Asarco plausibel).
- [ ] Overweeg of de `product`-stap (solar/elektronica) verder opgesplitst moet worden of dat één "solar"-boog
  het verhaal al draagt (nu: solar = de dikke boog, elektronica/sieraden = dunner ernaast).

---

## Build-handoff (naar de bouw-issues)
- **Nieuwe 11e grondstof** — er is nog géén `data/silver.js`: aanmaken + `<script src="data/silver.js">`
  toevoegen aan `index.html` (na `oil.js`) + zilver-sanity-check in `build-standalone.py`. Alle voorgaande
  grondstoffen waren basis→uitgewerkt; zilver is de eerste échte toevoeging sinds de basis-10.
- **Géén nieuwe marker-types** — `mine`/`refinery`/`port`/`market`/`recycler`/`exchange` bestaan allemaal al.
- **Géén nieuwe render-modus** — schip+land, hergebruikt zee-A\*/land-A\* + scheeps-voyages (koper/nikkel-patroon).
- **Géén nieuw chokepoint** — hergebruikt bestaande `wp-*` volledig (derde grondstof na nikkel/olie).
- **Kluisvoorraden-laag** — hergebruik de bestaande `exchange`-toggle (`type:"exchange"`/`layer:"exchange"`,
  `showExchangeStocks`) met **0 engine-wijziging** (nikkel bevestigde dat dit generiek is). Voeg 3 exchange-nodes
  + de `layer:"exchange"`-flows toe; de chip verschijnt automatisch omdat zilver exchange-data heeft.
- **Co-locatie-check** — houd nodes van zilver zelf ~30-45 km uit elkaar in dezelfde stad (SGE vs. China-solar-markt;
  India-markt vs. Nhava Sheva-haven vs. recycler) zodat geen `degDist:0`-arc ontstaat.
- **`silver.js` (bouw-issue):** dit bestand 1-op-1 omzetten + `REGISTER` + toevoegen aan `index.html`-laadvolgorde.
