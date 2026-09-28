# Routebrief (licht) · uranium — McArthur River/Key Lake → Port Hope → BWXT Peterborough

**stroom-id:** `uranium-mcarthurriver-porthope` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31) · **status:** gebakken
**Keten in één zin:** natuurlijk uranium (geen verrijking — CANDU-uitzondering) van de McArthur River-mijn/Key Lake-mill (Cameco, Athabasca-bekken, Saskatchewan) per **truck** dwars door Canada naar de Blind River-raffinaderij en de Port Hope Conversion Facility (Ontario), vandaar naar de BWXT-pelletpers in Toronto en de BWXT-splijtstoffabriek in Peterborough (CANDU-bundels voor OPG).
**Welke as van het verhaal:** de binnenlandse Canadese CANDU-uitzondering op de wereldwijde Rusland-verrijkingsknijp — dit erts wordt nooit verrijkt. McArthur River/Key Lake nameplate ≈18 miljoen lb U3O8/jr (~6.900 tU) (Cameco jaarverslag 2015 [7]); **2025-guidance neerwaarts bijgesteld naar 14-15 Mlbs** (~5.350-5.670 tU) door vertraging in de beschikbaarheid van mobiele mijnbouwapparatuur — de mijn draait, niet op volle capaciteit [13][14]. Port Hope Conversion Facility is vergund tot 12,5 Mkg U als UF6 + 2,8 Mkg U als UO2/jr [9].

## 1 · Ketenkaart
```
McArthur River-mijn `u-mcarthurriver-mijn` ──(b1 A truck · eigen mijnweg, Athabasca-bekken · 80 km)──► Key Lake-mill `u-keylake-mill`
  ──(b2 B truck · Hwy 914→2→16→Trans-Canada, Saskatoon–Winnipeg–Sault Ste. Marie · ~3.000 km)──► Blind River-raffinaderij `u-blindriver-raffinaderij`
  ──(b3 C truck · Hwy 17, Sault Ste. Marie–Sudbury–Parry Sound–Barrie–Toronto · 600 km)──► Port Hope Conversion Facility `u-porthope-conversie`
  ──(b4 D truck · Hwy 401 · ~112 km, bron-gelegd)──► BWXT Toronto (pelletpers) `u-bwxt-toronto`
  ──(b5 D truck · Hwy 401 → 115/7 · ~145 km, bron-gelegd)──► BWXT Peterborough (bundelfabriek) `u-bwxt-peterborough` ── stoppunt
```
⚠️ **Afwijking van het ketenontwerp:** het ontwerp gaf één been D (Port Hope → BWXT Peterborough, "aannemelijk: één bron"). Onderzoek (drie onafhankelijke bronnen [3][4][5]) toont een tussenstap: Port Hope levert UO2-poeder aan **BWXT Toronto**, dat het tot pellets perst/sintert en pas dán naar Peterborough voor bundelmontage stuurt. Been D is daarom in twee gemeten stukken gesplitst — precies het controlepunt uit de haalbaarheidstoets.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | McArthur River-mijn → Key Lake-mill | eigen mijnweg, Athabasca-bekken | 80 [1] | maak_stroombeen_weg (extract canada) | nee |
| b2 | B | truck | Key Lake-mill → Blind River-raffinaderij | Hwy 914 → 2 → 16 (Yellowhead) → Trans-Canada 1/17, via Saskatoon–Winnipeg | ~3.000 [2] | maak_stroombeen_weg (extract canada) | nee |
| b3 | C | truck | Blind River-raffinaderij → Port Hope Conversion Facility | Hwy 17, Sault Ste. Marie–Sudbury–Parry Sound–Barrie–Toronto-omleiding | 600 [2] | maak_stroombeen_weg (extract canada) | nee |
| b4 | D | truck | Port Hope Conversion Facility → BWXT Toronto (pelletpers) | Hwy 401 | ~112 [webcheck, grootcirkel 97 km × wegfactor; 3][4] | maak_stroombeen_weg (extract canada) | nee |
| b5 | D | truck | BWXT Toronto (pelletpers) → BWXT Peterborough (bundelfabriek) | Hwy 401 → Hwy 115/7 | ~145 [webcheck, grootcirkel 113 km × wegfactor; 3][4][5] | maak_stroombeen_weg (extract canada) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-mcarthurriver-mijn` | mijn (kop) | McArthur River-mijn (Cameco 70% / Orano 30%), Athabasca-bekken | 57.7626, -105.0508 | [1][6][12] | bron-gelegd (z14 gezien: verwerkingscomplex met hallen en toegangswegen in het boreale woud, landingsbaan 1 km NO; OSM-landuse "McArthur River Mine") |
| `u-keylake-mill` | mill (uraanconcentraat/yellowcake) | Key Lake-mill (Cameco), Athabasca-bekken | 57.2130, -105.6740 | [1][7][12] | bron-gelegd (z16 gezien: verwerkingsgebouw met tanks en opslagloodsen naast een groen/grijs tailings-bekken; OSM-landuse "Key Lake Mine" omsluit terrein + open pits oostelijk) |
| `u-blindriver-raffinaderij` | raffinaderij (concentraat → UO3) | Blind River Refinery (Cameco), 328 Eldorado Road | 46.1810, -83.0174 | [8][12] | bron-gelegd (z15 gezien: omheind fabrieksterrein met hallen en een bekken aan de North Channel van Lake Huron, naast de Blind River Golf Club; OSM-landuse "Cameco") |
| `u-porthope-conversie` | conversie (UO3 → UF6 + UO2-poeder) | Port Hope Conversion Facility (Cameco), 1 Eldorado Place | 43.9437, -78.2955 | [9][12] | bron-gelegd (z15 gezien: compact fabrieksterrein direct aan de Lake Ontario-kustlijn met kleine havenaanleg, spoor evenwijdig aan de kust) |
| `u-bwxt-toronto` | pelletpers (UO2-poeder → gesinterde pellets) | BWXT Nuclear Energy Canada — Toronto, 1025 Lansdowne Avenue | 43.6679, -79.4466 | [10][11][12] | bron-gelegd (z16 gezien: fabriekscomplex met platte bedrijfsdaken tussen spoorlijn en straat, wijk Wallace Emerson; OSM-kantoorpunt "BWXT Nuclear Energy Canada") |
| `u-bwxt-peterborough` | fabriek (bundelassemblage — stoppunt) | BWXT Nuclear Energy Canada — Peterborough, 1160 Monaghan Road | 44.2955, -78.3308 | [10][12] | bron-gelegd (z15 gezien: groot industrieel complex zuid van het centrum aan de westoever nabij de Otonabee-rivier; OSM-landuse "BWXT Nuclear Energy Canada") |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Points North Landing (Hwy 905/102-knooppunt) | 58.2689, -104.0800 | zuidelijk vertrekpunt van de mijnweg-corridor, enige aansluiting op het provinciale wegennet |
| b2 | 2 | La Ronge (Hwy 102/2-knooppunt) | 55.1005, -105.2900 | corridor buigt hier van het noord-zuid-tracé naar Hwy 2 richting Prince Albert |
| b2 | 3 | Prince Albert (Hwy 2/55/3-knooppunt) | 53.2020, -105.7559 | laatste stad vóór Saskatoon, waar de route de Yellowhead-corridor opzoekt |
| b2 | 4 | Saskatoon (Hwy 16-knooppunt) | 52.1318, -106.6608 | gebronde overslagplaats — "trucked from mills to Saskatoon" [2] |
| b2 | 5 | Yorkton (Yellowhead Hwy 16) | 51.2120, -102.4612 | Yellowhead i.p.v. Trans-Canada Hwy 1 via Regina = kortste Saskatoon–Winnipeg |
| b2 | 6 | Winnipeg (Hwy 1/17-knooppunt) | 49.8955, -97.1385 | hier voegt de Yellowhead-route weer samen met Trans-Canada Hwy 1/17 oostwaarts |
| b2 | 7 | Thunder Bay (Hwy 17-knooppunt) | 48.4064, -89.2598 | enige doorgaande wegcorridor langs de noordoever van Lake Superior |
| b2 | 8 | Sault Ste. Marie (Hwy 17-knooppunt) | 46.5127, -84.3330 | laatste knooppunt vóór de afslag naar Blind River — hier het gedocumenteerde ongeval met een uraanconcentraat-truck [2] |
| b3 | 1 | Sudbury (Hwy 17/69-knooppunt) | 46.4927, -80.9912 | corridor verlaat hier Hwy 17 (oostwaarts naar Ottawa) en neemt de Georgian Bay-route (Hwy 69) zuidwaarts |
| b3 | 2 | Parry Sound (Hwy 69/400-knooppunt) | 45.3436, -80.0337 | aansluiting van Hwy 69 op de doorgetrokken Hwy 400 |
| b3 | 3 | Barrie (Hwy 400/11-knooppunt) | 44.3893, -79.6901 | laatste grote knooppunt vóór de GTA |
| b3 | 4 | Vaughan (Hwy 400/401-knooppunt) | 43.7942, -79.5268 | overstap van Hwy 400 op Hwy 401 oostwaarts naar Port Hope |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Key Lake-mill | Cameco | erts (via McArthur River, geen eigen mijnbouw meer sinds 2018) → uraanconcentraat (U3O8) | nameplate ≈18 Mlbs/jr (~6.900 tU); 2025-guidance 14-15 Mlbs | [1][7][13][14] |
| Blind River-raffinaderij | Cameco | uraanconcentraat (wereldwijd, niet alleen Key Lake) → UO3 | 's werelds grootste commerciële uraanraffinaderij (sinds 1983) | [8] |
| Port Hope Conversion Facility | Cameco | UO3 → UF6 (verrijking, elders) + UO2-poeder (CANDU, onverrijkt) | vergund 12,5 Mkg U als UF6 + 2,8 Mkg U als UO2/jr | [9] |
| BWXT Toronto | BWXT Nuclear Energy Canada | UO2-poeder (Port Hope) → gesinterde UO2-pellets | Klasse IB-brandstoffabriek | [3][4][11] |
| BWXT Peterborough | BWXT Nuclear Energy Canada | UO2-pellets (Toronto) + zirkoniumbuizen (BWXT Arnprior) → CANDU-splijtstofbundels | ~67.000 sq ft; ~25% van Ontario's elektriciteit | [10] |

## 6 · Stoppunt
De brief stopt bij BWXT Peterborough: de bundels gaan naar OPG's Darlington/Pickering-centrales, maar geen bron koppelt een specifieke lading aan één centrale — fase E vervalt.

## 7 · Open punten
- Geen Cameco-cijfer voor b2/b3 apart; Watershed Sentinel geeft "~3.000 km" (Saskatchewan→Ontario) en "600 km" (Blind River→Port Hope) [2] — geen preciezer bedrijfscijfer gevonden binnen het zoekbudget.
- Corridor b2 is afgeleid uit de enige logische hoofdwegverbinding (Cameco noemt alleen "via Saskatoon"); via-punten zijn knooppuntsteden, niet gebrond per stuk snelweg.
- **Cameco Fuel Manufacturing (CFM)**, eveneens in Port Hope (200 Dorset Street East), is een APARTE splijtstofbundel-lijn van Cameco zelf (eigen pellets + assemblage, levert Bruce Power) — bewust niet getekend: andere klant/reactoreigenaar dan de BWXT/OPG-lijn van dit ontwerp. Dit was precies het controlepunt uit de haalbaarheidstoets en is hiermee beantwoord.
- BWXT Arnprior (zirkoniumbuizen) convergeert bij Peterborough maar is geen apart been (zijtoevoer, geen stroom binnen deze opdracht).
- km b4/b5 zijn webcheck-schattingen (grootcirkel × wegfactor); nog niet gemeten door het wegtool.
- 2025-productiedip (18 → 14-15 Mlbs) is een risiconotitie, geen afwijzingsgrond — CANDU-natuurlijk-uranium blijft een onomstreden technisch feit [13][14].

## 8 · Bronnen
[1] Cameco, McArthur River/Key Lake. https://www.cameco.com/businesses/uranium-operations/canada/mcarthur-river-key-lake
[2] Watershed Sentinel, "On the Yellowcake Trail Part Two: Uranium Mining in Canada" — ~3.000 km Saskatchewan→Ontario, 600 km Blind River→Port Hope, ongeval Hwy 17 met uraanconcentraat-truck. https://watershedsentinel.ca/article/yellowcake-road-part-2-uranium-mining-in-canada/
[3] CCNR, "Health Implications of Pelleting Operations at the BWXT-Peterborough Plant" — UO2-poeder Port Hope → BWXT Toronto (persen/sinteren) → BWXT Peterborough (bundelmontage). https://ccnr.org/Report_pack_GE.pdf
[4] WISE Uranium Project, "Uranium Enrichment and Fuel Fabrication — Current Issues (Canada)". https://www.wise-uranium.org/eopcdn.html
[5] BWXT, "Peterborough — BWXT Nuclear Energy Canada" — componenten uit Toronto (pellets) en Arnprior (buizen) samengevoegd in Peterborough. https://www.bwxt.com/bwxt-nec/about/peterborough
[6] Wikipedia, "McArthur River uranium mine" — 57°45′40″N 105°03′06″W. https://en.wikipedia.org/wiki/McArthur_River_uranium_mine
[7] Cameco, jaarverslag 2015 — McArthur River Mine/Key Lake Mill. https://www.cameco.com/annual_report/2015/mda/our-operations-and-projects/uranium-operating-properties/mcarthur-river-mine-key-lake-mill/
[8] Cameco, Refining: Blind River — 328 Eldorado Road, sinds 1983 's werelds grootste commerciële uraanraffinaderij. https://www.cameco.com/businesses/fuel-services/refining-blind-river
[9] Cameco, jaarverslag 2015 — Port Hope Conversion Services, vergunde capaciteit. https://www.cameco.com/annual_report/2015/mda/our-operations-and-projects/fuel-services/port-hope-conversion-services/
[10] BWXT, "BWXT in Peterborough" — 1160 Monaghan Rd, 67.000 sq ft, ~25% van Ontario's stroom. https://www.bwxt.com/bwxt-nec/bwxt-peterborough/
[11] BWXT, "BWXT in Toronto" — 1025 Lansdowne Avenue. https://www.bwxt.com/bwxt-nec/bwxt-toronto/
[12] OpenStreetMap (ODbL) via Nominatim — landuse "McArthur River Mine" 57.76263/-105.05078 · landuse "Key Lake Mine" · landuse "Cameco" (Blind River) 46.18103/-83.01738 · adrespunt "1, Eldorado Place" 43.94367/-78.29549 · kantoorpunt "BWXT Nuclear Energy Canada" (Toronto) 43.66793/-79.44656 · landuse "BWXT Nuclear Energy Canada" (Peterborough) 44.29547/-78.33083. https://www.openstreetmap.org
[13] Cameco, 6-K FY2025 (SEC EDGAR) — McArthur River/Key Lake 2025-guidance neerwaarts naar 14-15 Mlbs. https://www.sec.gov/Archives/edgar/data/1009001/ (dex991.htm, FY2025)
[14] Global News, "Cameco's McArthur River uranium mine..." — 2025-productieterugval, oorzaak mobiele-apparatuur-beschikbaarheid. https://globalnews.ca/news/8606834/cameco-mcarthur-river-uranium-mine
[15] Esri World Imagery via `v2/tools/sat_check.py` (z14-z16) — `v2/build-cache/satcheck/sat-uranium-mcarthurriver-porthope-{mcarthurriver,keylake-mill2,blindriver,porthope,bwxttoronto,bwxtpeterborough}.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze)

**Stroom `uranium-mcarthurriver-porthope`** → `v2/data/stroomroute-uranium-mcarthurriver-porthope.json` — 5 benen, alle truck. 3.917,4 km. 6 markers, allemaal exact (0,000 km) op de lijn — elk marker is tevens een routeerpunt (ankers = de vijf via-punt-uiteinden).
Recept: `bak_stromen.sh` (functie `bak_uranium_mcarthurriver_porthope`).

Per been (gemeten tegen de brief-tabel, §2):
1. b1 — McArthur River-mijn → Key Lake-mill (eigen mijnweg): **80,5 km** tegen 80 gepubliceerd = **+0,5%** [OK]. Extract `canada`, `corridorKlassen` ruim gezet (tertiary/unclassified/service) — de mijnweg door het boreale woud draagt geen secondary-klasse.
2. b2 — Key Lake-mill → Blind River-raffinaderij: **2.945,2 km** tegen ~3.000 (Watershed Sentinel) = **-1,8%** [OK]. Twee correcties op de bak-aanwijzing, geen enkele op de brieftekst zelf en geen coördinaat verzonnen: (a) het via-punt "Points North Landing" (Hwy 905, 58,2689/-104,0800) heeft in OSM géén wegverbinding met Hwy 914/Key Lake — de eerste scanpoging faalde met "geen wegpad tussen punt 0 en 1", ook met `corridorKlassen` ruim. Nagemeten (osmium op de canada-extract): Hwy 914 loopt van de mijnen zuidwaarts tot een knooppunt met Hwy 165 ten zuiden van Pinehouse (55,2348/-106,7898, exact OSM-eindpunt); Wikipedia bevestigt onafhankelijk "[Highway 914] begins at Highway 165 south of Pinehouse … does not intersect with any provincially-owned highways between Highway 165 and Key Lake Mine." Via-punt vervangen door dat knooppunt. (b) Thunder Bay → Sault Ste. Marie sneed over Lake Superior heen (geen wegpad binnen het 90 km-venster om de rechte lijn, want de échte Hwy 17 volgt de noordoever ver buiten die band) — Wawa (Hwy 17-knooppunt, coördinaat via Nominatim) toegevoegd als extra via-punt. (c) `toets_knikken.py` ving daarna één echte TERUGLOOP (179,4°, v=29,5) bij het Saskatoon-via-punt: dat punt (52,1318/-106,6608) lag in het stadscentrum en snapte op een doodlopende straat, terwijl de doorgaande Hwy 16 hier als Circle Drive (trunk) 2,6 km noordelijker loopt (osmium-check op de landscan-cache) — via-punt verschoven naar die gemeten Circle Drive-coördinaat (52,1579/-106,6606); niet bijgeschoven om een km-toets te halen, die stond al binnen norm.
3. b3 — Blind River-raffinaderij → Port Hope Conversion Facility: **644,1 km** tegen 600 (Watershed Sentinel) = **+7,3%** [OK].
4. b4 — Port Hope Conversion Facility → BWXT Toronto (pelletpers): **111,8 km** tegen ~112 (webcheck) = **-0,3%** [OK].
5. b5 — BWXT Toronto (pelletpers) → BWXT Peterborough (bundelfabriek): **135,8 km** tegen ~145 (webcheck) = **-6,5%** [OK]. Geen extra via-punt nodig gebleken — de Dijkstra vond de Hwy 401→115/7-knik zelf zonder omweg. Dit been vormt samen met b4 de AFWIJKING uit het ontwerp (§1): Toronto ligt zuidwestelijk van zowel Port Hope als Peterborough, dus de twee sub-benen tekenen samen een zichtbare lus/driehoek op de bol — dat is de geometrische waarheid, geen bakfout.

Alle vijf naden tussen opeenvolgende benen: **0,00 km** (elk been begint exact op het eindpunt van het vorige).

Stippels: geen. Alle vijf benen zijn eigen/openbare weg met gekarteerde OSM-geometrie tot op beide ankers.

Toetsen: `toets_knikken.py` — 87 knikken ≥60° (bijna allemaal spikes op kruisingen/rotondes bij de zes ankers en via-punten, straal meestal <150 m), **2 omkeringen ≥150°** (b3, bij Vaughan/Barrie — "scherpe bocht, echt", verhouding 1,2, geen sluipweg) en **0 TERUGLOOP** (ná de Saskatoon-correctie hierboven). `toets_rechte_benen.py --min-km 5`: dit stroom-id komt niet voor in de verdachtenlijst — geen been ≥5 km met een omwegfactor rond 1,0. `json.load` slaagt, `versie` 2, `punt_formaat` `lonlat`, modaliteit uitsluitend `truck` (5×), elk been ≥2 punten (358–16.817 punten per been).
⚠️ **Bestandsgrootte buiten de richtwaarde:** 511,6 KB tegen de richtwaarde <~300 KB — bevinding, niet dichtgetrokken. Oorzaak: been b2 alleen al is 2.945 km/16.817 punten dichte, rauw gescande OSM-weggeometrie (geen kunstmatige verdichting); de andere vier benen zijn samen ~100 KB.

Gereedschapslessen:
- **Een bak-aanwijzing kan geografisch fout zijn zonder dat de brieftekst zelf fout is** — de brieftabel (§2/§4) noemt Points North Landing als brongegeven van de opdracht, maar geen enkele brief-voetnoot claimt een gemeten wegverbinding daar; de fout zat in de tussenstap (bak-aanwijzing), niet in het onderzoek van de briefschrijver. Nagaan met een onafhankelijke bron (Wikipedia) vóór een via-punt te vervangen, niet alleen op het OSM-scanresultaat vertrouwen.
- **"Geen wegpad" tussen twee via-punten is geen wegklasse-probleem per definitie** — `corridorKlassen` ruimer zetten hielp hier niets, want de weg naar het verkeerde punt bestaat gewoon niet. Eerst met een gerichte osmium-query (`ref`/`name`-filter op de lokale extract) controleren of het via-punt überhaupt op een gekarteerde weg ligt, vóór de klassenfilter te verbreden.
- **Een rechte lijn tussen twee via-punten kan een baai/meer oversnijden** — Thunder Bay → Sault Ste. Marie sneed recht over Lake Superior; het venster (buffer om de rechte lijn) moet dan breder zijn dan de kortste afstand ÓF een tussenstad op de kustweg toevoegen. Een extra, goed-gebronde via-punt is hier de goedkopere fix dan het venster wereldwijd op te hogen.
- **`toets_knikken.py`'s TERUGLOOP-signaal is precies en bruikbaar als reparatie-instructie** — het wees zelf de exacte coördinaat en verhouding (v=29,5) aan van een via-punt dat in een stadscentrum lag i.p.v. op de doorgaande ringweg; de osmium-cache van de eigen landscan (in `v2/build-cache/land/weg-canada-*.json`) volstond om de juiste Circle Drive-coördinaat te vinden zonder een nieuwe wereldwijde scan.
- **`snoei_keerlussen` vangt niet elke dubbel-gereden lus** — de eerste (foute) Saskatoon-lijn had een lus van bijna-identieke maar niet exact dubbele punten (sub-meter afwijking tussen heen- en terugpad), waardoor de exacte-duplicaat-pruning hem liet staan; `toets_knikken.py` (dat op hoek+ratio kijkt, niet op exacte coördinaatgelijkheid) ving hem wél.
