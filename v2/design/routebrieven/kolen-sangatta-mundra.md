# Routebrief (licht) · kolen — Sangatta → Tanjung Bara → Mundra (India)

**stroom-id:** `kolen-sangatta-mundra` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** thermische kolen van de KPC-mijn bij Sangatta (Oost-Kalimantan) per **band** (13 km, niet gekarteerd)
naar de eigen laadkade Tanjung Bara Coal Terminal, per **zeeschip** ~6.500 km naar de kolenjetty van Tata Power Mundra
UMPP aan de Golf van Kutch (Gujarat) — jetty zelf niet satelliet-gelokaliseerd, laatste 32,9 km als haven-aanloop-stippel
— tot de kolenopslag van de centrale (aannemelijk: eigen keten via Tata Power-belang in KPC, geen scheepslading met
naam gevonden). Stoppunt = de centrale: kolen wordt daar verstookt, er is geen verder fysiek product om te volgen.
**Welke as van het verhaal:** *Zeehandel thermisch, Indonesië → India* (#1 exporteur 555 Mt → #2 importeur 237 Mt,
IEA Coal 2025 [10]). KPC produceerde 55,0 Mt in 2024 (+3% t.o.v. 53,5 Mt in 2023) [1], de grootste mijn van Indonesië;
TBCT verscheepte >38,1 Mt in 2023 op een nameplate van 24 Mt/j (2013) [2][3]. Mundra UMPP (5×800 MW = 4.150 MW) is
ontworpen op Indonesisch subbitumineus kool en sloot in 2011 een eigen afnameovereenkomst van 10,11 Mtpa (±20%) via
de Singaporese handelaar Trust Energy Resources [4]; los daarvan kocht Tata Power in 2007 30% van KPC + Arutmin mét
een gekoppelde afnametoezegging van ~10 Mt/j "for its power plant at Trombay ... as well as ... Mundra" [8][9]. Beide
cijfers wijzen op dezelfde orde grootte maar zijn geen bewijs van een specifieke lading KPC→Mundra in 2024/25; het
ketenvolume van déze specifieke as is niet gepubliceerd. De centrale lag 2025-07-02 t/m 2026-03-31 stil (tariefgeschil
met GUVNL) en draait sinds 2026-04-01 weer op een nieuwe PPA, na een directive onder de Electricity Act §11 [6][7].

## 1 · Ketenkaart
```
KPC-mijn `kolen-kpc-mijn` ──(b1 band · niet gekarteerd · 13 km, stippel)──► TBCT-kade `kolen-tbct-kade`
   ──(b2 zeeschip · Makassar–Java–Indische Oceaan–Arabische Zee–Golf van Kutch · ~6.500 km, MARNET
      + laatste 32,9 km haven-aanloop over de Golf van Kutch, stippel — kolenjetty niet gelokaliseerd)──►
   Mundra UMPP / CGPL-terrein `kolen-mundra-cgpl` ⏹ stoppunt (kolen → elektriciteit, geen fase D/E)
   └── vertakking (niet getekend): Indonesië → China (Guangdong) is de grootste kolen-zeestroom ter wereld;
       géén gedocumenteerde KPC-lading naar Mundra in 2024/25, alleen de equity-/offtake-koppeling
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | band (overland conveyor) | `kolen-kpc-mijn` → `kolen-tbct-kade` | KPC-conveyor, 2.100 t/u [3] | 13 [3] | stippel via 2 via-punten (§4); Indonesië-extract kent 137 `goods_conveyor`-ways maar geen met naam/operator KPC/Tanjung Bara | ja — band, niet gekarteerd |
| b2 | B | zee | `kolen-tbct-kade` → `kolen-mundra-cgpl` | Straat Makassar → Javazee → Straat Lombok/Sunda → Indische Oceaan → Arabische Zee → Golf van Kutch | ~6.500 hemelsbreed; geen gepubliceerde scheepsroute | MARNET tot zeeknoop 5321 (22,5734/69,4446); laatste 32,9 km haven-aanloop (`maak_havenaanloop`, terugval rechte stippel) | ja — alleen het laatste stuk (Golf van Kutch); TBCT-kant routeert direct (20,1 km tot zeeknoop 5453, geen aanloop nodig) |

Beennaam b2 voor de bol: *"zeeschip Tanjung Bara → Mundra (thermisch; centrale stil jul 2025–mrt 2026, weer in
bedrijf 04-2026)"* — vastgelegd in de toets, bindend overgenomen.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-kpc-mijn` | mijn (kop van de band) | KPC open pit + naaste terreinen, Sangatta | 0.58100, 117.49850 | [1][3][11] | bron-gelegd (z16 gezien: duidelijke dagbouw-traptreden, haalwegen en een spoedwegkruising direct ten oosten van de put — dit is één van de vele KPC-putten in de 90.960 ha-concessie; welke put nu precies de 13 km-band voedt is niet vast te stellen zonder OSM-conveyordata, zie §7) |
| `kolen-tbct-kade` | overslag laadkade (band → zee) | Tanjung Bara Coal Terminal, laadponton aan het einde van de kade/conveyor | 0.53750, 117.65950 | [1][2][11] | bron-gelegd (z16 gezien: een ~1,5 km lange kade/conveyor loopt vanaf de kust de zee in naar een liggende laad­structuur/ponton; op het land eromheen stockpiles en bedrijfsgebouwen zichtbaar) |
| `kolen-mundra-cgpl` | verwerkingsknoop / centrale (losplek + stoppunt) | Coastal Gujarat Power Ltd (Tata Power), Mundra UMPP | 22.82007, 69.51889 | [4][12] | bron-gelegd (OSM-landuse-vlak `way/160685919` "Coastal Gujarat Power Ltd"; z15 gezien: industrieterrein met een ontziltings-/aslagune aan de westzijde en fabrieksgebouwen + een groot donker kolenstockpile-vlak aan de oost-/zuidoostzijde — dit is het CGPL-terrein, geen marktcentroïde, conform de bindende correctie) |

## 4 · Via-punten (alleen b1 — de band heeft geen net)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | haalweg-knoop ten oosten van de put | 0.58200, 117.50800 | eerste vaste punt op de zichtbare haalweg die de put met het oostelijke wegennet verbindt (z16 gezien) |
| b1 | 2 | TBCT-landzijde (stockpile/laadcomplex) | 0.54000, 117.62500 | hier komt de conveyor aan land vóór hij de kade op gaat (z14 gezien: bedrijfsgebouwen + conveyorspoor tussen dit punt en de kade) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Tanjung Bara Coal Terminal | PT Kaltim Prima Coal (KPC) | mijnkolen → scheepslading | nameplate 24 Mt/j, 80.000 t/dag (2013); 38,1 Mt verscheept in 2023 | [2][3] |
| Mundra UMPP (CGPL) | Coastal Gujarat Power Ltd (Tata Power, 100%) | geïmporteerde subbitumineuze kolen → elektriciteit | 5 × 800 MW = 4.150 MW; kolenafname 10,11 Mtpa ±20% (offtake-overeenkomst 2011, Trust Energy Resources) | [4] |

## 6 · Stoppunt
De brief stopt bij de kolenopslag van Mundra UMPP: kolen wordt daar in één stap tot elektriciteit verstookt (géén
cokes/staal-tussenstap zoals bij metallurgische kolen), dus fase D/E bestaat hier per definitie niet — conform de
opmerking in het ontwerp dat de keten bij de afnemer-centrale stopt.

## 7 · Open punten
- **KPC-band (b1) niet gekarteerd:** de Indonesië-extract kent 137 `goods_conveyor`-ways maar geen enkele met een
  naam/operator-tag die naar KPC, Kaltim Prima of Tanjung Bara wijst (bindende toets-uitkomst) → stippel met reden,
  geen route via een geleende way.
- **Welke put voedt de band:** de KPC-concessie omvat meerdere putten over ~20 km N-Z; het OSM-landuse-vlak voor
  "Kaltim Prima Coal / Sangatta coal mine" (`way/1119275782`) beslaat het hele complex. Het anker hierboven ligt op
  een duidelijk zichtbare put het dichtst bij Tanjung Bara; de hemelsbrede afstand tot de kade (~24 km) is groter dan
  de gepubliceerde 13 km conveyor, wat aangeeft dat het exacte laadpunt (wasserij/stockyard) elders binnen de
  concessie ligt — niet gevonden zonder OSM-conveyordata of een nieuwere/gedetailleerdere bron.
- **Mundra-kolenjetty niet gelokaliseerd:** in tegenstelling tot Tanjung Bara (duidelijk zichtbare kade+laadponton)
  is bij Mundra géén aparte kolenjetty te onderscheiden — de kust rond CGPL bestaat uit getijdenkreken/zoutpannen
  zonder zichtbare pier in open water binnen ~5 km van het terrein. Er is dus **geen** coördinaat verzonnen: de
  zeeroute eindigt schematisch op het CGPL-terreinanker via een 32,9 km haven-aanloop-stippel (Golf van Kutch).
  Bronnen noemen wel "a coal jetty 5 km from the project site" [5] maar geven geen coördinaat.
- **Eigen-keten-claim:** Tata Power's KPC-belang (2007, 30% + Arutmin, Arutmin in 2014 verkocht, KPC-belang volgens
  Enerdata behouden [9]) en CGPL's eigen 10,11 Mtpa-offtake (2011, via een Singaporese handelaar, niet rechtstreeks
  van KPC [4]) wijzen beide op een captive/quasi-captive relatie, maar geen bron noemt een scheepslading van KPC naar
  Mundra in 2024/25 — "eigen keten" blijft aannemelijk, geen percentage of tonnage zonder jaarverslag genoemd.
- **Ketenvolume 2024/25** van déze specifieke as (Sangatta → Mundra) is nergens gepubliceerd; de brief draagt
  asvolumes (KPC 55 Mt 2024, TBCT 38,1 Mt 2023, India-import totaal 237 Mt 2024) in plaats van een ketencijfer.
- **Vertakking Indonesië → China** (Guangdong, de grootste kolen-zeestroom ter wereld) is alleen genoemd, niet
  getekend — geen KPC-specifieke bron voor die as in deze ronde.

## 8 · Bronnen
[1] Sxcoal, 2025 — KPC-productie 2023 54,0 Mt (RKAB-doel 53,5 Mt overtroffen), 2024-2026 quotum vlak op 53,5 Mt/j; elders bevestigd op 55,0 Mt voor 2024 (+3%). https://en.sxcoal.com/news/detail/1770994292127961090
[2] Global Energy Monitor, Tanjung Bara Coal Terminal — eigenaar KPC (Bumi Resources 51% / Tata Power 30% / Mountain Netherlands Investments 19%); nameplate 24 Mt/j, 80.000 t/dag (2013); 38,1 Mt verscheept in 2023; 13 km overland conveyor vanaf de Sangatta-mijn; Bengalon-mijn via 22 km wegtransport. https://www.gem.wiki/Tanjung_Bara_Coal_Terminal
[3] Mining Technology, "BP Exploration Coal Mine, Kaltim" — 13 km, 2.100 t/u-conveyor Sangatta → Tanjung Bara; stockpiles Prima/Pinang 60/35 kt bij de mijn, 350/150 kt bij de haven. https://www.mining-technology.com/projects/kaltim/
[4] Global Energy Monitor, Tata Mundra Ultra Mega Power Project — coördinaat 22,8158/69,5281; 5×800 MW (2 × 830 MW geannuleerd); coal offtake-overeenkomst 10,11 Mtpa (±20%) via Trust Energy Resources (Singapore), eerste lading september 2011; kolenjetty "5 km from the project site"; Tata Power 30%-belang in KPC via Bumi Resources genoemd als bron. https://www.gem.wiki/Tata_Mundra_Ultra_Mega_Power_Project
[5] Institution of Civil Engineers, Mundra Ultra Mega Power Plant — "Engineers built a coal jetty at Mundra Port – 5km from the project site – to transport coal to the plant." https://www.ice.org.uk/what-is-civil-engineering/infrastructure-projects/mundra-ultra-mega-power-plant-umpp
[6] Business Standard, 2026-04-01 — Tata Power hervat 4.150 MW Mundra-centrale na 9 maanden stilstand (stopgezet 2025-07-02, herstart 2026-04-01), na nieuwe PPA's met GUVNL. https://www.business-standard.com/industry/news/tata-power-resumes-ops-at-4-150-mw-mundra-thermal-plant-after-9-months-126040101129_1.html
[7] Discovery Alert / ICICI Direct-samenvatting, 2026 — herstart 2026-04-01 volgde op een directive onder §11 Electricity Act 2003 om op volle capaciteit te draaien voor de zomerpiekvraag; stilstand kostte ~₹800 crore aan vaste kosten. https://www.icicidirect.com/research/equity/trending-news/tata-power-resumes-operations-at-4-150-mw-mundra-thermal-power-plant
[8] Bank Indonesia (BI IRU highlight news), 2007 — Tata Power koopt 30% van KPC + Arutmin (Bumi Resources), gekoppeld aan een langetermijn-afnameovereenkomst van ~10 Mt/j "for its power plant at Trombay in India as well as for future power projects, including the recently won Ultra Mega Power Project of 4,000MW at Mundra". https://www.bi.go.id/en/iru/highlight-news/Pages/Tata%20Power.aspx
[9] Enerdata, 2014 — Tata Power verkoopt zijn 30%-belang in PT Arutmin Indonesia aan een Bakrie-entiteit; "Tata Power, however, continues to hold its equity stake in PT Kaltim Prima Coal (KPC)". https://www.enerdata.net/publications/daily-energy-news/tata-power-sells-30-stake-indonesian-coal-mining-company.html
[10] IEA, Coal 2025 — Trade — Indonesië #1 exporteur (555 Mt 2024), India #2 importeur (237 Mt 2024) na China (548 Mt) en vóór Japan (162 Mt). https://www.iea.org/reports/coal-2025/trade
[11] OpenStreetMap (ODbL) via Nominatim lookup — landuse "Kaltim Prima Coal" (`way/1119275782`, centroïde 0,62798/117,45923, bbox 0,5415–0,7156 N / 117,3447–117,6237 O — de hele KPC-concessie) · landuse "Coastal Gujarat Power Ltd" (`way/160685919`, centroïde 22,82007/69,51889). https://www.openstreetmap.org
[12] Wikipedia (MediaWiki API `prop=coordinates`) — "Mundra Thermal Power Station" 22,82278/69,55278 · "Tanjung Bara" (dorp) 0,58602/117,70371 (niet gebruikt als anker — ligt 8+ km van de werkelijke kade, zie satellietcheck) · "Mundra" 22,85/69,73. https://en.wikipedia.org
[13] Esri World Imagery via `v2/tools/sat_check.py` (z12–z16, live) — `v2/build-cache/satcheck/sat-kolen-sangatta-mundra-kpc-plant-zoom.png`, `sat-kolen-sangatta-mundra-tanjungbara-jetty-zoom.png`, `sat-kolen-sangatta-mundra-mundra-cgpl.png`, plus de bredere oriëntatiebeelden (kpc-concessie-centroid, kpc-zuid, mundra-wide, mundra-jetty-search).

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `kolen-sangatta-mundra`** → `v2/data/stroomroute-kolen-sangatta-mundra.json` — 5 benen. 7.535,7 km. 3 markers: truck (stippel) 18,7 km · zee 7.487,0 km · zee (stippel) 30,0 km.
Recept: `bak_stromen.sh` (functie `bak_kolen_sangatta_mundra`). Toelichting: b1 (band Sangatta → TBCT) is drie truck-stippelsegmenten langs de twee via-punten uit brief §4 (mijn→haalweg-knoop 1,1 km, haalweg-knoop→TBCT-landzijde 13,8 km, TBCT-landzijde→kade 3,8 km = 18,7 km totaal) tegen gepubliceerd 13 km (mining-technology.com) — **+43,8%, ver buiten ±15%**, exact het open punt dat de brief zelf al voorzag: het exacte laadpunt/wasserij ligt vermoedelijk elders binnen de ~20 km-lange KPC-concessie, geen via-punt bijgeschoven om het te laten kloppen. b2 (zee) snapt aan de TBCT-kant automatisch op zeeknoop 5453 (21,8 km, < 25 km max-snap, dus per de brief geen aanloop nodig); aan de Mundra-kant reikt MARNET niet tot de kolenjetty (jetty zelf niet satelliet-gelokaliseerd, brief §7) → `maak_havenaanloop.py` gaf een schoon pad van 30,0 km (11 punten, 0,00 km land midden op de lijn, omwegfactor 1,053) als stippel, van zeeknoop 5321 (22,5734/69,4446) naar het CGPL-terreinanker. Het gemeten zeebeen is 7.487,0 km MARNET + 30,0 km aanloop = 7.517,0 km, tegen de brief-schatting ~6.500 km hemelsbreed ("geen gepubliceerde scheepsroute", brief §2) — **+15,6%, net buiten de ±15%-band**, tegen een aannemelijke hemelsbreed-schatting en geen operatorcijfer; de bake meet het exacte getal, dit is geen afwijking om dicht te trekken.

Stippels: (1) band Sangatta → TBCT als drie segmenten (18,7 km totaal, geen net op deze korrel — de Indonesië-extract kent 137 `goods_conveyor`-ways maar geen enkele met een naam/operator-tag naar KPC/Kaltim Prima/Tanjung Bara) · (2) haven-aanloop Mundra (30,0 km, MARNET reikt niet tot de kolenjetty; kolenjetty zelf niet gelokaliseerd op satelliet, getijdenkreken/zoutpannen zonder zichtbare pier). Alle overige geometrie (het zeebeen zelf) is gemeten en doorgetrokken.

Gereedschapslessen: (a) de zee-snap bij Tanjung Bara (21,8 km, < 25 km max-snap) laat een naad van 21,84 km tussen de laatste TBCT-kade-stippel en het eerste getekende zeepunt — de snap zelf wordt niet als aparte lijn getekend (dezelfde klasse als de 5,6 km-snap bij Hay Point in `bak_kolen_goonyella_kalinganagar`), hier ruim boven de 5 km-norm en genoteerd, niet dichtgetrokken. (b) `--stippel` accepteert precies twee punten (VAN/NAAR) — een been met via-punten zoals b1 (2 via-punten uit brief §4) moet als losse opeenvolgende `--stippel`-segmenten worden opgegeven; het tool kent geen multi-punts-stippel (eerste poging met 4 punten in één `--stippel`-regel faalde met een parse-fout, meteen gecorrigeerd naar drie segmenten). (c) `toets_knikken.py`: 0 omkeringen, 0 terugloop, 3 knikken ≥60° op het zeebeen (normale MARNET-routekeuzes, geen fout). `toets_rechte_benen.py --min-km 5`: de drie truck-stippels en de haven-aanloop verschijnen als verwacht (rechte lijnen met reden, geen ongemarkeerde rechte stukken). Toetsen geslaagd: `json.load`/versie 2/punt_formaat lonlat/modaliteiten {truck, zee}/elk been ≥2 punten/bestand 14,7 KB, allemaal binnen de norm. Markers alle 3 op 0,00 km van hun been (elk anker = beeneindpunt).
