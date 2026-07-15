# Grafiet — brief (ingevuld ontwerp) — hoort bij `data/graphite.js`

*Peiljaar ±2023-2024. Volumes in **kt/jaar** (duizend ton), indicatief en afgerond — bedoeld om verhoudingen
te tonen, geen handelsstatistiek. Natuurlijk vlokgrafiet ≈ 1,6 Mt/jaar winning; synthetisch anodegrafiet is een
aparte, uit petroleum-naaldcokes gemaakte stroom. Bronnen: USGS Mineral Commodity Summaries 2025 (Graphite
(natural)), Benchmark Mineral Intelligence (anode-/verwerkingsaandeel), IEA Critical Minerals, bedrijfsrapportages
(Syrah, Talga, Novonix, NMG, POSCO Future M, BTR). Zie §7. Status: **uitgewerkt-ontwerp** — klaar voor `graphite.js`.*

> **Principe:** we vertellen geen verhaal, we modelleren de werkelijkheid — het plaatje vertelt zichzelf.
> Voor lithium/koper is de vorm "alles door China-raffinage", voor REE "alles door de Ganzhou-scheiding", voor
> goud "alles door Zwitserland". Voor grafiet is de vorm een **REE-achtige verwerkingstrechter, maar met TWEE
> grondstofstromen die op dezelfde knijp samenkomen**: natuurlijk vlokgrafiet (gedolven) én synthetisch grafiet
> (uit petroleum-**naaldcokes**) moeten allebei worden omgezet tot **gecoat sferisch/gegrafitiseerd anodepoeder**,
> en die verwerkingsstap zit voor **~90%+ in China**. Zelfs Afrikaans/Madagascar-vlok vaart naar China om verwerkt
> te worden — de mijn is niet waar de waarde/knijp zit. In **december 2023** zette China die dominantie om in een
> hefboom via **exportvergunningen** op grafiet-anodemateriaal.

---

## 0. Metadata (→ `REGISTER({...})` in `graphite.js`)

| veld | waarde |
|---|---|
| `id` | `graphite` (bestaat al — basis-10, staat in `index.html`) |
| `name` | Grafiet |
| `symbol` | C |
| `color` | `#78828F` (grafietgrijs; mijn-markers) |
| `flowColor` | `#B6BEC8` (lichter, voor de bogen tegen de donkere bol) |
| `unit` | `kt/jaar (indicatief)` |
| `detail` | `basis` → `uitgewerkt` |
| `blurb` | Grafiet is het anodemateriaal in vrijwel elke lithium-ionbatterij. Twee feedstocks — natuurlijk vlokgrafiet (China #1, Mozambique, Madagascar) en synthetisch grafiet uit petroleum-naaldcokes — komen samen op dezelfde knijp: de omzetting tot gecoat sferisch/gegrafitiseerd anodepoeder zit ~90%+ in China. Zelfs Afrikaans vlok vaart naar China om verwerkt te worden. In december 2023 legde China exportvergunningen op grafiet-anodemateriaal. |

## 1. Het verhaal in 3 zinnen
1. **Grafiet is HET anodemateriaal** (grootste celcomponent naar massa, ~1 kg per kWh) en komt uit twee stromen:
   **natuurlijk vlokgrafiet** (gedolven — China #1 ~65% van natuurlijk, Mozambique/Balama, Madagascar, Brazilië,
   Tanzania) en **synthetisch grafiet** (uit petroleum-**naaldcokes**, gegrafitiseerd bij ~3000 °C).
2. Beide moeten door dezelfde **verwerkingstrechter** — spheronisatie + zuivering (99,95%+) + coating voor
   natuurlijk, grafitisatie voor synthetisch — en die zit **~90%+ in China** (Shandong voor natuurlijk vlok,
   Binnen-Mongolië voor synthetisch met goedkope kolenstroom). **Zelfs ex-China-vlok vaart naar China** om verwerkt
   te worden → de mijn is niet waar de knijp zit (de Ganzhou-REE-parallel).
3. In **december 2023** zette China de verwerkingsdominantie om in een **hefboom** via exportvergunningen op
   grafiet-anodemateriaal; het Westen bouwt ex-China anodecapaciteit (Syrah Vidalia/Louisiana uit Balama-vlok,
   Novonix/Tennessee, Talga/Zweden, NMG/Québec, POSCO/Korea) onder IRA-FEOC + EU-CRMA — maar klein en traag.

## 2. De keten & stages (→ `stage`-codes; hergebruikt de bestaande stage-styling)

| stap | `stage`-code | kleur | booghoogte | inhoud |
|---|---|---|---|---|
| 1. mijn (vlok) / naaldcokes-bron → **feedstock** | `erts` | dof/donkergrijs | laag | vlokgrafiet-concentraat + synthetische naaldcokes → verwerker; óók recyclaat |
| 2. **gecoat sferisch / gegrafitiseerd anodepoeder** | `raffinaat` | vol grafietgrijs (#78828F) | midden | de China-verwerkingstrechter (+ de ex-China buildout) |
| 3. **batterijcel / gigafabriek** | `product` | licht | hoog | anodepoeder → cellenfabriek (EV/opslag) |

## 3. Nodes (locaties)
> Alle `type`-waarden bestaan al: `mine`/`refinery`/`port`/`market`/`recycler`. **Géén nieuwe marker-styling.**
> Coördinaten: **west = negatief** (gecontroleerd). `share` bij natuurlijke mijnen = ~% van natuurlijk vlokgrafiet.
> Synthetische feedstock (naaldcokes) heeft geen mijn-share (het is een petroleum-/koolteer-bijproduct).

### 3a. Winning — natuurlijk vlokgrafiet (`type: mine`, met `share`)
| id | naam | land | lat | lon | share | tier | note |
|---|---|---|---|---|---|---|---|
| gr-china-flake | Heilongjiang (Luobei/Jixi) | China | 47.60 | 130.80 | 65 | 1 | grootste natuurlijk vlok **én** de verwerking; grotendeels binnenlandse keten |
| gr-mozambique | Balama (Twigg/Syrah) | Mozambique | -13.29 | 38.53 | 13 | 1 | grootste ex-China vlokmijn; voedt zowel China als Syrah's eigen Vidalia (VS) |
| gr-madagascar | Molo / Ampanihy | Madagaskar | -23.70 | 44.80 | 6 | 2 | groot, hoogwaardig vlok; grotendeels naar China/Korea voor verwerking |
| gr-brazil | Minas Gerais (Nacional de Grafite) | Brazilië | -17.50 | -42.00 | 7 | 2 | gevestigde producent; deels binnenlands, deels export |
| gr-tanzania | Mahenge / Epanko | Tanzania | -8.70 | 36.70 | 3 | 3 | nieuwe projecten (EcoGraf/Magnis); vlok → Azië voor verwerking |
| gr-norway | Skaland (Senja) | Noorwegen | 69.45 | 17.30 | 1 | 3 | hoogwaardigste vlok van Europa; naar Talga (Zweden) |
| gr-ukraine | Zavallya (Zavalievsky) | Oekraïne | 48.23 | 30.40 | 2 | 3 | Europees vlok, oorlog-verstoord; over land naar EU-verwerking |
| gr-srilanka | Bogala/Kahatagaha (via Colombo) | Sri Lanka | 6.93 | 79.90 | 1 | 3 | **vein-/klompgrafiet** — de zeldzame ~99% zuivere natuurlijke vorm; naar Japan (premium) |

### 3b. Winning — synthetische feedstock (`type: mine`, naaldcokes; geen share)
*Synthetisch grafiet start niet in een mijn maar bij **naaldcokes** (petroleum-cokes uit olieraffinage of koolteerpek
uit staal), dan grafitisatie bij ~3000 °C. Twee bronnen tonen het contrast: premium VS-naaldcokes (deels geëxporteerd)
en Chinese naaldcokes die de Binnen-Mongolië-grafitisatie voedt.*

| id | naam | land | lat | lon | tier | note |
|---|---|---|---|---|---|---|
| gr-nc-us | Naaldcokes VS (Lake Charles/Seadrift) | VS | 30.20 | -93.20 | 2 | premium petroleum-naaldcokes (Phillips 66/Seadrift); binnenlands + export naar Aziatische grafitiseerders; `coastal` |
| gr-nc-china | Naaldcokes China (Liaoning/Shandong) | China | 38.90 | 121.60 | 2 | binnenlandse petroleum-/koolteer-naaldcokes → Binnen-Mongolië-grafitisatie; `coastal` |

### 3c. Verwerking / anodemateriaal (`type: refinery`) — de trechter + de ex-China buildout
| id | naam | land | lat | lon | tier | note |
|---|---|---|---|---|---|---|
| gr-ref-shandong | China — sferisch/natuurlijk anode (Shandong/Qingdao) | China | 36.10 | 120.30 | 1 | **DE trechter voor natuurlijk**: spheronisatie + zuivering 99,95%+ + coating (BTR/Ningbo Shanshan); verwerkt binnenlands + geïmporteerd vlok; `coastal` |
| gr-ref-innermongolia | China — synthetisch anode / grafitisatie (Binnen-Mongolië) | China | 40.60 | 109.00 | 1 | **DE trechter voor synthetisch**: grafitisatie bij ~3000 °C op goedkope kolenstroom (Wuhai/Baotou; BTR/Putailai/Shanshan) |
| gr-ref-japan | Japan — synthetisch anode (Resonac/Mitsubishi Chem) | Japan | 35.00 | 136.90 | 2 | premium synthetisch anode voor hoogwaardige cellen; deels op VS-/Japanse naaldcokes; `coastal` |
| gr-ref-korea | POSCO Future M (Pohang/Sejong) | Zuid-Korea | 36.02 | 129.36 | 2 | grootste ex-China anode; natuurlijk (Mozambique/Tanzania-vlok) + synthetisch; `coastal` |
| gr-ref-vidalia | Syrah Resources — Vidalia | VS (Louisiana) | 31.57 | -91.42 | 1 | **actief sferisch grafiet uit Balama-vlok** — de zeldzame niet-Chinese natuurlijke-anodeknoop; IRA-FEOC; binnenwater → via New Orleans |
| gr-ref-novonix | Novonix — Chattanooga | VS (Tennessee) | 35.05 | -85.30 | 3 | synthetisch anode (VS-naaldcokes); IRA-gedreven |
| gr-ref-sweden | Talga — Luleå (Vittangi) | Zweden | 65.58 | 22.15 | 2 | EU natuurlijk anode (Talnode) uit eigen Vittangi-vlok + Skaland; `coastal` |
| gr-ref-quebec | Nouveau Monde Graphite — Bécancour | Canada | 46.34 | -72.35 | 3 | geïntegreerd natuurlijk anode (Matawinie-mijn → Bécancour); Noord-Amerika |

### 3d. Havens / gateways (`type: port`)
| id | naam | land | lat | lon | rol |
|---|---|---|---|---|---|
| gr-port-nacala | Nacala | Mozambique | -14.54 | 40.67 | Balama-vlok de Indische Oceaan op (China) + rond de Kaap (VS/Vidalia) |
| gr-port-toamasina | Toamasina (Tamatave) | Madagaskar | -18.15 | 49.41 | Madagascar-vlok → Azië |
| gr-port-mtwara | Mtwara | Tanzania | -10.27 | 40.19 | Tanzaniaans vlok → Azië |
| gr-port-vitoria | Vitória | Brazilië | -20.32 | -40.29 | Minas-Gerais-vlok → Azië/VS |
| gr-port-neworleans | New Orleans | VS | 29.95 | -90.07 | Golf-gateway voor Syrah Vidalia (barge de Mississippi op) |
| gr-port-rotterdam | Rotterdam | Nederland | 51.95 | 4.14 | Europese gateway voor Chinees anodepoeder → EU-gigafabrieken |

### 3e. Consumptie / eindmarkt (`type: market`) — gigafabrieken
| id | naam | land | lat | lon | tier | note |
|---|---|---|---|---|---|---|
| gr-mkt-china-battery | China — gigafabrieken (CATL/BYD) | China | 26.66 | 119.55 | 1 | 's werelds grootste anode-/batterijvraag (Ningde, Fujian); `coastal` |
| gr-mkt-korea-japan | Korea/Japan — cellenfabrieken (LG/Samsung SDI/SK/Panasonic) | Zuid-Korea | 35.50 | 129.30 | 2 | premium cellen; leunt op eigen + Chinees anode; `coastal` |
| gr-mkt-eu | EU — gigafabrieken (Duitsland/Hongarije/Polen) | Duitsland | 50.98 | 11.00 | 2 | sterk afhankelijk van Chinees anode; CRMA wil dat terugdringen |
| gr-mkt-us | VS — battery belt (Tesla/Ultium, TN/KY/NV) | VS | 36.50 | -86.60 | 2 | IRA-FEOC dwingt ex-China anode (Syrah/Novonix/NMG) |

### 3f. Recycling — **optionele toggle-laag** (`type: recycler`, `layer: recycle`, default uit)
*Hergebruikt het bestaande REE/PGM-`recycle`-patroon met **0 engine-wijziging**. Batterijgrafiet-terugwinning is nog
**nascent/klein** (het meeste verbruikte grafiet wordt nu verbrand/gestort); Redwood/Li-Cycle/Ascend + de EU-
batterijverordening (gerecycleerd-gehalte-eisen vanaf ~2027) trekken het op gang. Bewust bescheiden gemodelleerd.*

| id | naam | land | lat | lon | note |
|---|---|---|---|---|---|
| gr-rec-us | Redwood Materials (Nevada) | VS | 39.54 | -119.40 | teruggewonnen anodegrafiet → VS-anode; nog opschalend |
| gr-rec-eu | EU-batterijrecycling (Skellefteå) | Zweden | 64.75 | 20.95 | EU-batterijverordening dwingt gerecycleerd-gehalte af |
| gr-rec-china | China-batterijrecycling (Brunp/GEM, Hubei) | China | 30.50 | 114.30 | grootste recyclingbasis; grafiet-terugwinning schaalt |

## 4. Stromen (flows) — indicatief, ~kt/jr
*Modi: **`ship`** (intercontinentaal — bestaande zee-A\*), **`rail`/`road`** (korte hops + binnenland). `via` = havens
(`gr-port-*`) + bestaande `wp-*`-vaarpunten/knelpunten. **Harde regel:** elke ship-leg landt op een kustpunt
(`port`/`coastal`/`wp-*`). **Géén nieuw chokepoint** — grafiet hergebruikt de bestaande routes volledig.*

### 4a. Mijn/feedstock → verwerking (stage `erts`)
| from | to | ~kt/jr | mode | via | note |
|---|---|---|---|---|---|
| gr-china-flake | gr-ref-shandong | 900 | rail | — | binnenlands vlok → Shandong-spheronisatie |
| gr-mozambique | gr-ref-shandong | 220 | ship | gr-port-nacala, wp-moz-noord, wp-aceh, wp-malakka, wp-singapore, wp-scs, wp-taiwan | **ex-China vlok vaart naar China** om verwerkt te worden |
| gr-mozambique | gr-ref-vidalia | 60 | ship | gr-port-nacala, wp-kaap, wp-atl-west, wp-florida, gr-port-neworleans | Balama → Syrah's eigen anodefabriek in Louisiana (het niet-Chinese draadje) |
| gr-madagascar | gr-ref-shandong | 70 | ship | gr-port-toamasina, wp-aceh, wp-malakka, wp-singapore, wp-scs, wp-taiwan | Madagascar-vlok → China-verwerking |
| gr-madagascar | gr-ref-korea | 40 | ship | gr-port-toamasina, wp-aceh, wp-malakka, wp-singapore, wp-scs, wp-taiwan | deels naar POSCO (ex-China alternatief) |
| gr-tanzania | gr-ref-korea | 45 | ship | gr-port-mtwara, wp-aceh, wp-malakka, wp-singapore, wp-scs, wp-taiwan | Tanzaniaans vlok → POSCO |
| gr-brazil | gr-ref-shandong | 60 | ship | gr-port-vitoria, wp-kaap, wp-aceh, wp-malakka, wp-singapore, wp-scs, wp-taiwan | Braziliaans vlok → China (de lange haul om de Kaap) |
| gr-norway | gr-ref-sweden | 15 | rail | — | Skaland → Talga Luleå (Noord-Scandinavië, via Narvik-spoor) |
| gr-ukraine | gr-ref-sweden | 20 | rail | — | Zavallya → EU-verwerking over land (Øresund) |
| gr-srilanka | gr-ref-japan | 12 | ship | wp-malakka, wp-singapore, wp-scs, wp-taiwan | vein-grafiet → Japan (premium); via Colombo |
| gr-nc-us | gr-ref-novonix | 120 | road | — | VS-naaldcokes → US synthetisch anode (binnenlands) |
| gr-nc-us | gr-ref-japan | 90 | ship | wp-golf-mexico, wp-caribisch, wp-panama, wp-pac-noord | premium VS-naaldcokes → Japanse grafitisatie (export) |
| gr-nc-china | gr-ref-innermongolia | 700 | rail | — | Chinese naaldcokes → Binnen-Mongolië-grafitisatie (goedkope kolenstroom) |

### 4b. Verwerking → gigafabriek (stage `product`)
| from | to | ~kt/jr | mode | via | note |
|---|---|---|---|---|---|
| gr-ref-shandong | gr-mkt-china-battery | 700 | rail | — | de dikste boog: Chinees natuurlijk anode → CATL/BYD |
| gr-ref-innermongolia | gr-mkt-china-battery | 650 | rail | — | Chinees synthetisch anode → gigafabrieken |
| gr-ref-shandong | gr-mkt-korea-japan | 180 | ship | wp-taiwan | Chinees anode → Korea/Japan-cellen (nu exportvergunning-plichtig) |
| gr-ref-shandong | gr-mkt-eu | 160 | ship | wp-scs, wp-singapore, wp-malakka, wp-bab, wp-rode-zee, wp-suez, wp-gibraltar, gr-port-rotterdam | Chinees anode → EU-gigafabrieken (de afhankelijkheid) |
| gr-ref-innermongolia | gr-mkt-eu | 120 | ship | gr-ref-shandong, wp-scs, wp-singapore, wp-malakka, wp-bab, wp-rode-zee, wp-suez, wp-gibraltar, gr-port-rotterdam | synthetisch anode → EU (via de oostkust) |
| gr-ref-vidalia | gr-mkt-us | 45 | rail | — | Syrah US anode → battery belt (IRA-conform) |
| gr-ref-novonix | gr-mkt-us | 100 | road | — | US synthetisch anode → cellen |
| gr-ref-quebec | gr-mkt-us | 40 | road | — | NMG Québec anode → VS (Noord-Amerika geïntegreerd) |
| gr-ref-korea | gr-mkt-korea-japan | 130 | road | — | POSCO-anode → Koreaanse cellen |
| gr-ref-japan | gr-mkt-korea-japan | 110 | road | — | Japans synthetisch anode → eigen cellen |
| gr-ref-sweden | gr-mkt-eu | 30 | rail | — | Talga EU-anode → EU-gigafabrieken (de dunne EU-lijn) |

### 4c. Recycling → verwerking (optioneel — `layer:"recycle"`, stage `erts`, default uit)
| from | to | ~kt/jr | mode | layer | via | note |
|---|---|---|---|---|---|---|
| gr-rec-us | gr-ref-novonix | 25 | road | recycle | — | Redwood teruggewonnen grafiet → US-anode |
| gr-rec-eu | gr-ref-sweden | 15 | rail | recycle | — | EU-batterijrecycling → Talga (verordening-gedreven) |
| gr-rec-china | gr-ref-shandong | 40 | rail | recycle | — | China-recycling → verwerking (grootste, schaalt) |

## 5. Knelpunten & de "knijp"
- Grafiet's knijp is de **verwerkingstrechter** (spheronisatie/zuivering/grafitisatie), **~90%+ China** — een
  institutionele/industriële knijp zoals REE-Ganzhou, niet een zeestraat. Draagt via `tensions`, niet via een `wp-*`.
- **Géén nieuw chokepoint / `grens-*` nodig** — grafiet hergebruikt de bestaande zee/land-routes volledig
  (Malakka/Singapore/SCS/Taiwan voor Azië-aanvoer; Kaap + Panama + Golf van Mexico/Florida voor de trans-
  Atlantische Balama→Vidalia-lijn; Suez/Bab/Gibraltar + Rotterdam voor China→EU; Øresund/Narvik-spoor voor de
  Europese vlok). **Vierde grondstof (na nikkel/olie/zilver) die 0 chokepoints toevoegt.**
- Wél zichtbaar: **twee feedstocks (vlok + naaldcokes) die op de China-verwerking convergeren**, en een dunne
  **ex-China buildout** (Vidalia/Talga/Novonix/NMG/POSCO) die er tegenin probeert te bouwen.

## 6. Emergent plaatje-check (de lat bij oplevering)
1. Vlokmijnen verspreid (China/Afrika/Madagascar/Brazilië) + twee naaldcokes-bronnen (VS/China) — **twee
   grondstofstromen** die naar dezelfde verwerkingsknopen lopen.
2. **Alles convergeert op China** (Shandong = natuurlijk, Binnen-Mongolië = synthetisch); zelfs Mozambikaans/
   Madagascar/Braziliaans vlok vaart naar China → de trechter is zichtbaar.
3. Eén emblematisch **niet-Chinees draadje**: Balama (Mozambique) → **Syrah Vidalia (Louisiana)** rond de Kaap.
4. Een dunne **ex-China buildout-waaier** (Talga/Novonix/NMG/POSCO) naar EU/VS/Korea-gigafabrieken.
5. De dikste `product`-bogen lopen **binnen China** (Shandong/Binnen-Mongolië → CATL/BYD).
6. Toggle **recycling** → drie kleine recycler-nodes met aftakkingen terug de verwerking in (default uit).
7. Alles over **zee/land** — géén luchtbogen (dat is goud/PGM).

## 7. Bronnen (peiljaar ±2023-2024)
- **USGS Mineral Commodity Summaries 2025 — Graphite (natural):** wereldwinning natuurlijk ~1,6 Mt; China ~65-70%,
  daarna Mozambique, Madagascar, Brazilië; VS 100% importafhankelijk voor natuurlijk grafiet.
- **Benchmark Mineral Intelligence / IEA Critical Minerals:** China ~90%+ van de anode-/verwerkingscapaciteit
  (spheronisatie, zuivering, grafitisatie); anode = grootste celcomponent naar massa (~1 kg grafiet/kWh).
- **China exportcontroles grafiet (dec 2023):** vergunningsplicht op natuurlijk vlok (sferisch/hoge zuiverheid) +
  synthetisch anodemateriaal — na gallium/germanium (juli 2023), vóór de bredere REE-controles (2025).
- **Bedrijfsrapportages:** Syrah Resources (Balama-mijn + Vidalia-anodefabriek, IRA-FEOC), Talga (Vittangi/Luleå),
  Novonix (Tennessee synthetisch), Nouveau Monde Graphite (Matawinie/Bécancour), POSCO Future M, BTR/Ningbo Shanshan/
  Putailai (Chinese anode-marktleiders).

## 8. Open vragen / research-TODO
- [ ] Volumes zijn indicatief/afgerond; de precieze mijn→verwerker-toewijzing (welk vlok naar welke Chinese stad)
  is plausibel maar niet per contract nagetrokken.
- [ ] Natuurlijk vs synthetisch is ~50/50 in anodes en verschuift richting synthetisch (fast-charge/cycluslevensduur);
  de exacte verhouding per gigafabriek is vereenvoudigd.
- [ ] Naaldcokes-stromen (VS-export naar Azië) zijn illustratief gemodelleerd (2 bronnen); Japan/koolteer-pek-bronnen
  samengevat in notes.
- [ ] Recycling bewust klein gehouden (nascent) — als de EU-verordening bijt kan dit later opgeschaald worden.

---

## Build-handoff (naar de bouw-issues)
- **Bestaand basis-10-bestand** — `data/graphite.js` bestaat al en staat in `index.html`: **basis → uitgewerkt**,
  géén nieuwe `<script>`-tag nodig (anders dan zilver, dat een 11e nieuw bestand was).
- **Géén nieuwe marker-types** — `mine`/`refinery`/`port`/`market`/`recycler` bestaan allemaal al.
- **Géén nieuwe render-modus** — schip+land, hergebruikt zee-A\*/land-A\* + scheeps-voyages (koper/nikkel/zilver-patroon).
- **Géén nieuw chokepoint** — hergebruikt bestaande `wp-*` volledig (vierde grondstof na nikkel/olie/zilver).
- **Recycling-laag** — hergebruik de bestaande `recycle`-toggle (`type:"recycler"` + `layer:"recycle"` op nodes én
  flows) met **0 engine-wijziging** (REE/PGM bevestigden dat de gate generiek is: `node.layer==="recycle"` +
  `hasRecycle()` op `f.layer==="recycle"`). Chip verschijnt automatisch omdat grafiet recycle-data heeft.
- **Co-locatie-check** — houd grafiet-nodes ~30-45 km uit elkaar in dezelfde regio (gr-ref-korea vs gr-mkt-korea-japan;
  gr-ref-shandong vs gr-nc-china) zodat geen `degDist:0`-arc ontstaat.
- **`graphite.js` (bouw-issue):** dit ontwerp 1-op-1 omzetten; `detail:"uitgewerkt"`, `flowColor` toevoegen.
- **build-standalone.py:** grafiet-sanity-checks toevoegen (REE-stijl).
