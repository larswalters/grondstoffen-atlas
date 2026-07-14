# Lithium — overzicht van wat er in de atlas zit

Hoort bij `data/lithium.js`. Peiljaar ±2024/25. Alle volumes in **kt LCE/jaar**
(lithium carbonate equivalent), indicatief en afgerond — bedoeld om
verhoudingen te tonen, geen handelsstatistiek. Bronnen: USGS Mineral Commodity
Summaries, bedrijfsrapportages, IEA. Wereldproductie ≈ 1.200–1.300 kt LCE.

## Het verhaal in 3 zinnen

1. Australië graaft het meeste erts, Chili en Argentinië pompen pekel — maar
   **±twee derde van de raffinage staat in China**. Daar zit de flessenhals.
2. Vrijwel al het Australische, Zimbabwaanse en Braziliaanse concentraat vaart
   **door de Straat van Malakka** naar Chinese raffinaderijen en komt als
   batterijchemie terug.
3. De VS (IRA) en de EU (CRMA) proberen met wetgeving alternatieve routes af
   te dwingen — die routes bestaan al op de kaart, maar zijn nog dun.

## De keten (en hoe de atlas hem toont)

| stap | stage-code | kleur op de kaart | hoogte boog | eenheid |
|---|---|---|---|---|
| 1. Winning → concentraat / ruwe pekel | `erts` | donker, gedempt | laag (kruipt over het oppervlak) | kt LCE |
| 2. Raffinage → carbonaat / hydroxide | `raffinaat` | volle grondstofkleur (#4FD1C5) | midden | kt LCE |
| 3. Kathode / cellen | `product` | licht, bijna wit | hoog | kt LCE |

## Locaties (nodes)

### Mijnen — actieve productie (share = % wereldproductie)

| id | naam | land | share | tier | opmerking |
|---|---|---|---|---|---|
| li-atacama | Salar de Atacama | Chili | 20% | 1 | rijkste pekel; SQM + Albemarle; staat als concessiepartner |
| li-greenbushes | Greenbushes | Australië | 15% | 1 | grootste hardrock-mijn; rijkste erts (±2% Li2O) |
| li-yichun-mine | Yichun (lepidoliet) | China | 9% | 2 | dure marginale productie — zet de wereldprijs |
| li-bikita | Bikita / Arcadia | Zimbabwe | 9% | 1 | Chinese eigenaren; snelst gegroeide bron |
| li-pilgangoora | Pilgangoora | Australië | 8% | 1 | export via Port Hedland |
| li-qinghai | Qinghai-brines | China | 8% | 2 | lastige pekel, wél binnenlands |
| li-wodgina | Wodgina | Australië | 5% | 2 | Pilbara (nu gescheiden van Mt Marion — lag eerst fout op één punt) |
| li-olaroz | Olaroz / Cauchari | Argentinië | 5% | 2 | Ganfeng bezit salar én raffinaderij |
| li-mt-marion | Mt Marion | Australië | 4% | 2 | bij Kalgoorlie |
| li-sigma | Vale do Jequitinhonha | Brazilië | 4% | 2 | "groen" concentraat |
| li-hombre-muerto | Salar del Hombre Muerto | Argentinië | 3% | 2 | oudste Argentijnse brine |
| li-kathleen-valley | Kathleen Valley | Australië | 2% | 3 | nieuwste grote mijn (2024) |
| li-silver-peak | Silver Peak | VS | 1% | 3 | enige actieve VS-mijn |

Som ≈ 93%; de rest is verspreid klein spul.

### Mijnen — projecten (geen share, wel `potential`)

| id | naam | land | potentie | status |
|---|---|---|---|---|
| li-uyuni | Salar de Uyuni | Bolivia | grootste bekende voorraad | politiek muurvast |
| li-manono | Manono | DR Congo | grootste onontgonnen hardrock | eigendomsconflict |
| li-thacker-pass | Thacker Pass | VS | ±40 kt/j fase 1 | in aanbouw (GM) |
| li-jadar | Jadar | Servië | ±58 kt/j | omstreden, stilgelegd |
| li-barroso | Barroso | Portugal | ±25 kt/j | vergunningstraject |
| li-zinnwald | Zinnwald | Duitsland | ±12 kt/j | vroeg stadium |
| li-keliber | Keliber | Finland | ±15 kt/j | in aanbouw, enige gesloten EU-keten |

### Havens (de plekken waar het erts de zee op gaat)

| id | naam | land | rol |
|---|---|---|---|
| li-port-bunbury | Bunbury | Australië | uitgang Greenbushes |
| li-port-hedland | Port Hedland | Australië | uitgang Pilbara (Pilgangoora, Wodgina) |
| li-port-geraldton | Geraldton | Australië | uitgang binnenland-WA (Mt Marion, Kathleen Valley) |
| li-port-antofagasta | Antofagasta / Angamos | Chili | vrijwel complete Chileense én Argentijnse export |
| li-port-beira | Beira | Mozambique | uitgang Zimbabwe |
| li-port-vitoria | Vitória | Brazilië | uitgang Minas Gerais (Sigma) |
| li-port-ningbo | Ningbo-Zhoushan | China | ingang Chinese oostkust |
| li-port-charleston | Charleston | VS | Atlantische aanlanding voor de chemie in de Carolinas |
| li-port-oakland | Oakland | VS | Pacifische aanlanding; laatste stuk over land naar Nevada |
| li-port-rotterdam | Rotterdam | Nederland | aanlanding Zuid-Amerikaans carbonaat → Duitse chemie |
| li-port-piraeus | Piraeus | Griekenland | Chinese toegangspoort tot Europa (COSCO) |

**Kustfabrieken** (`coastal: true`): Kwinana, Salar del Carmen, Gwangyang en
Naraha staan pál aan de kade. Ze mogen daarom zelf de zee op zonder aparte
haven-node — zonder die vlag trok de atlas een rechte lijn dwars over Japan.

### Raffinage / chemie

| id | naam | land | tier | rol |
|---|---|---|---|---|
| li-ref-jiangxi | Jiangxi (Yichun/Ganzhou) | China | 1 | grootste cluster ter wereld — het zwaartepunt |
| li-ref-sichuan | Sichuan (Suining/Yibin) | China | 1 | tweede cluster, aan kathodefabrieken gekoppeld |
| li-ref-qinghai | Qinghai-raffinage | China | 2 | goedkoop carbonaat uit eigen pekel |
| li-ref-carmen | Salar del Carmen / La Negra | Chili | 1 | carbonaat bij Antofagasta |
| li-ref-gwangyang | Gwangyang (POSCO) | Z-Korea | 1 | de bewuste route om China heen |
| li-ref-kwinana | Kwinana / Kemerton | Australië | 2 | moeizame eigen raffinage |
| li-ref-kings-mountain | Kings Mountain | VS | 2 | heropbouw onder de IRA |
| li-ref-bitterfeld | Bitterfeld (AMG) | Duitsland | 2 | eerste EU-hydroxide, zonder EU-mijn |
| li-ref-naraha | Naraha | Japan | 3 | klein, gevoed uit Argentinië |
| li-ref-becancour | Bécancour | Canada | 3 | gepland |
| li-ref-kokkola | Kokkola | Finland | 3 | gepland (bij Keliber) |

### Markt / cellen

| id | naam | land | tier |
|---|---|---|---|
| li-mkt-catl | Ningde (CATL) | China | 1 |
| li-mkt-byd | Shenzhen (BYD) | China | 2 |
| li-mkt-nevada | Giga Nevada | VS | 1 |
| li-mkt-debrecen | Debrecen / Göd | Hongarije | 1 |
| li-mkt-skelleftea | Skellefteå | Zweden | 3 |

## Stromen (flows) — 32 stuks

**De routes worden automatisch berekend.** De atlas zoekt zelf een pad dat
alleen over water gaat (of, voor trein/weg/pijp, alleen over land). In `via`
staan dus alleen de punten waar de route dóór moét: havens en knelpunten.

De drie grote aanvoerroutes naar Azië:

- **A — Australië → China:** Lombok → Makassar → Zuid-Chinese Zee → Taiwan.
  Lét op: grote bulkschepen uit West-Australië varen **niet** via Malakka.
- **B — Afrika/Brazilië → China:** Malakka → Singapore → Zuid-Chinese Zee.
- **C — Chili/Argentinië → Azië:** dwars over de Stille Oceaan. Geen knelpunt,
  wel de langste route in de hele keten (en bijna antipodaal — zie knelpunten.md).

| van → naar | stap | modus | kt LCE | route |
|---|---|---|---|---|
| Greenbushes → Jiangxi | erts | schip | 110 | Bunbury · **Lombok** · **Makassar** · **Taiwan** · Ningbo |
| Greenbushes → Sichuan | erts | schip | 55 | idem |
| Greenbushes → Kwinana | erts | weg | 20 | — |
| Pilgangoora → Jiangxi | erts | schip | 80 | Hedland · **Lombok** · **Makassar** · **Taiwan** · Ningbo |
| Pilgangoora → Gwangyang | erts | schip | 15 | Hedland · **Lombok** · **Makassar** |
| Wodgina → Sichuan | erts | schip | 55 | Hedland · **Lombok** · **Makassar** · **Taiwan** · Ningbo |
| Mt Marion → Jiangxi | erts | schip | 45 | Geraldton · **Lombok** · **Makassar** · **Taiwan** · Ningbo |
| Kathleen Valley → Jiangxi | erts | schip | 20 | idem |
| Bikita → Jiangxi | erts | schip | 100 | Beira · **Malakka** · **Taiwan** · Ningbo |
| Sigma → Jiangxi | erts | schip | 40 | Vitória · **Kaap** · **Malakka** · **Taiwan** · Ningbo |
| Sigma → Kings Mountain | erts | schip | 10 | Vitória · Atlantic · Charleston |
| Yichun-mijn → Jiangxi | erts | weg | 110 | — |
| Qinghai → Qinghai-raf | erts | pijp | 95 | — |
| Atacama → Carmen | erts | pijp | 245 | — |
| Carmen → Jiangxi | raffinaat | schip | 60 | Antofagasta · Stille Oceaan · **Taiwan** · Ningbo |
| Carmen → Gwangyang | raffinaat | schip | 35 | Antofagasta · Stille Oceaan |
| Carmen → Kings Mountain | raffinaat | schip | 25 | Antofagasta · **Panama** · Charleston |
| Carmen → Bitterfeld | raffinaat | schip | 15 | Antofagasta · **Panama** · Rotterdam |
| Hombre Muerto → Naraha | raffinaat | schip | 10 | Antofagasta · Stille Oceaan |
| Olaroz → Jiangxi | raffinaat | schip | 35 | Antofagasta · Stille Oceaan · **Taiwan** · Ningbo |
| Olaroz → Gwangyang | raffinaat | schip | 15 | Antofagasta · Stille Oceaan |
| Jiangxi → CATL | product | spoor | 120 | — |
| Sichuan → BYD | product | spoor | 80 | — |
| Qinghai-raf → CATL | product | spoor | 40 | — |
| Jiangxi → Debrecen | product | schip | 25 | Ningbo · **Taiwan** · **Malakka** · **Bab el-Mandeb** · **Suez** · Piraeus |
| Gwangyang → Giga Nevada | product | schip | 20 | **Noord-Pacific** · Oakland |
| Kwinana → Giga Nevada | product | schip | 8 | **Lombok** · **Makassar** · Pacific · Oakland |
| Kings Mountain → Giga Nevada | product | spoor | 12 | — |
| Bitterfeld → Debrecen | product | spoor | 5 | — |
| Bitterfeld → Skellefteå | product | spoor | 2 | — |
| Thacker Pass → Kings Mountain | erts | spoor | 20 | *(gepland)* |
| Barroso → Bitterfeld | erts | spoor | 8 | *(gepland)* |
| Keliber → Kokkola | erts | weg | 8 | *(gepland)* |

## Spanningen (in het paneel "Knelpunten & spanningen")

| id | type | titel | kern |
|---|---|---|---|
| li-t-indonesie | knelpunt | Lombok & Makassar | **al het Australische erts** (ruim een derde van de wereldproductie) door twee Indonesische zeestraten |
| li-t-malakka | knelpunt | Straat van Malakka | Zimbabwe en Brazilië naar China — én de Chinese chemie terug naar Europa |
| li-t-raffinage | concentratie | Raffinage ±2/3 in China | winning top-1 ≈35% (AU), raffinage top-1 ≈65–70% (CN) — de kwetsbaarheid zit één stap ná het graven |
| li-t-greenbushes | spof | Greenbushes | 15% van de wereld uit één put, via één haven (Bunbury) |
| li-t-zimbabwe | beleid | Zimbabwaans exportverbod | ruw erts verboden sinds 2022; druk richting verplichte verwerking in eigen land |
| li-t-ira | beleid | IRA / FEOC | VS-subsidie vervalt bij Chinese schakels → dwingt Chili→VS, Brazilië→VS en Korea→Nevada af |

Universele knelpunten zelf staan in `data/knelpunten.md` / `_chokepoints.js`;
hierboven staat alleen de lithium-invulling ervan.

## Nog te checken / bekende gaten

- Cijfers zijn indicatief (±2024/25); vóór publicatie tegen actuele USGS/IEA
  aanhouden — vooral Zimbabwe en Chinese lepidoliet schommelen hard.
- Status Zimbabwaans concentraat-verbod en Chinese exportcontroles op
  raffinagetechnologie: beleid dat snel schuift, actueel verifiëren.
- **Exporthavens** zijn deels aannames: Kathleen Valley en Mt Marion via
  Geraldton, Sigma via Vitória — plausibel, maar niet per contract nagetrokken.
- Recycling ontbreekt nog als ketenstap (Redwood, Li-Cycle) — kandidaat voor
  een vierde stage zodra het volume dat rechtvaardigt.
- Bécancour heeft nog geen aanvoerstroom (Canadese mijnen ontbreken nog).
