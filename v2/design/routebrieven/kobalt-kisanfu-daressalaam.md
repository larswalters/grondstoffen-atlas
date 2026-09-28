# Routebrief (licht) · kobalt — KFM Kisanfu-mijn (DRC) → Kasumbalesa → Tunduma → Dar es Salaam → Ningbo

**stroom-id:** `kobalt-kisanfu-daressalaam` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31) · **status:** gebakken
**Keten in één zin:** kobalthydroxide (+ koperkathode) van de **KFM Kisanfu-plant** (CMOC 71,25% / CATL 23,75% / DRC-staat 5%, Lualaba) gaat volledig per **truck** de "derde Congolese uitweg" — mijnweg → **RN39/RN1** (gedeeld eerste stuk met TFM/KCC) → **Kasumbalesa** → Zambiaanse **T2/Great North Road** (Ndola → Kapiri Mposhi → Mpika → Isoka) → **Nakonde/Tunduma** → Tanzaniaanse **T1 Centraal Corridor/TANZAM** (Mbeya → Iringa → Morogoro) → **Port of Dar es Salaam** (Container Terminal II), en per **zeeschip** via Malakka naar de containerkade **Ningbo Beilun** — aannemelijk: generieke bestemming China, niet mijn-specifiek gebrond.
**Welke as van het verhaal:** de Copperbelt-Oost-uitweg via Tanzania, als tegenhanger van de zuidelijke Durban-as (`koper-kolwezi-durban`) en de westelijke Lobito-as. KFM was in H1 2026 de grootste kobalthydroxide-exporteur van de DRC (24.824,78 t hydroxide / 8.410,14 t Co, 20,9% van het DRC-totaal) [6]; de $1,4 mld TAZARA-spoorconcessie (CCECC, sept. 2025) zit nog in de 3-jarige bouwfase, dus deze volledig-truck-keten is de **huidige** situatie, geen omissie [7][8].

## 1 · Ketenkaart
```
KFM Kisanfu-plant `co-kisanfu-laad` ──(b1 truck · mijnweg→RN39/RN1, gedeeld met TFM/KCC · ~290 km hemelsbreed)──►
Kasumbalesa `co-kasumbalesa-grens` (hergebruikt) ──(b2 truck · T2/Great North Road · ~935 km hemelsbreed)──►
Nakonde/Tunduma `co-nakonde-tunduma-grens` ──(b3 truck · T1 Centraal Corridor/TANZAM · ~787 km hemelsbreed)──►
Dar es Salaam CT2 `co-dar-kade` ──(b4 zee · Indische Oceaan→Malakka→Z-Chinese Zee→O-Chinese Zee · ~9.800 km indicatief, aannemelijk: generieke bestemming China)──►
Ningbo Beilun-containerkade `co-ningbo-kade` (hergebruikt) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `co-kisanfu-laad` → `co-kasumbalesa-grens` | mijnweg → RN39 (bij Kisanfu-dorp) → RN39/RN1 Likasi–Lubumbashi (gedeeld eerste stuk met TFM/KCC, zie `koper-kolwezi-durban.md` §4) | geen gepubliceerde bronlengte; eigen via-puntenketen ~289,7 km hemelsbreed — het ontwerp noemde ten onrechte "~90–150 km" (dat cijfer beschrijft vermoedelijk alleen de lokale afstand Kisanfu–Kolwezi/TFM, niet de rit tot Kasumbalesa) | `maak_stroombeen_weg.py` — **nieuw profiel** `kobalt-kisanfu-kasumbalesa`, extract congo-drc; via-punten Likasi/Lubumbashi hergebruikt uit `koper-kolwezi-durban.md` §4 | nee, tenzij `co-kisanfu-laad` > 2 km van het OSM-wegnet blijkt te liggen bij het bakken |
| b2 | A | truck | `co-kasumbalesa-grens` (hergebruikt) → `co-nakonde-tunduma-grens` | T2/Great North Road: Ndola → Kapiri Mposhi → Mpika → Isoka | ~1.750 (Ndola–Tunduma ≈1.900 [3][4] minus het Kasumbalesa–Ndola-stuk) tegen ~934,5 km hemelsbreed (verhouding 1,87, plausibel voor deze bochtige weg via de Kapiri Mposhi-lus) | `maak_stroombeen_weg.py` — nieuw profiel `kobalt-kasumbalesa-nakonde`, extract zambia, refs T2/T3 | nee |
| b3 | A | truck | `co-nakonde-tunduma-grens` → `co-dar-kade` | T1 Centraal Corridor/TANZAM (A7): Mbeya → Iringa → Morogoro | ~950 [ontwerp] tegen ~786,6 km hemelsbreed (verhouding 1,21, plausibel voor een vrij directe hoofdweg) | `maak_stroombeen_weg.py` — nieuw profiel `kobalt-nakonde-daressalaam`, extract tanzania, refs A7/T1 | nee |
| b4 | B | zee | `co-dar-kade` → `co-ningbo-kade` (hergebruikt, zie `kobalt-tfm-quzhou.md` §3) | Indische Oceaan → Straat Malakka → Zuid-Chinese Zee → Oost-Chinese Zee — **aannemelijk: generieke bestemming China** | ~9.800 indicatief; exact bij MARNET-bake (Ningbo-zeeknoop 29.9758,121.9736 hergebruikt uit `kobalt-tfm-quzhou.md` b2) | MARNET `--been "zee\|…\|-6.8394,39.2968\|29.9758,121.9736"` | aanloop: waarschijnlijk (kade ligt in de Kurasini-baai) — meten bij het bakken, > 25 km → `maak_havenaanloop.py` |

Geen last-mile-benen: `co-kisanfu-laad` is het site-anker en tevens het beginpunt van b1 (werkwijze §1).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-kisanfu-laad` | mijn / laadplek (plant) | KFM – Kisanfu Processing Plant (CMOC Kisanfu Mining SARL) | -10.7630, 25.9983 | OSM `landuse=industrial` (haalbaarheidstoets, lokale pyosmium-scan) + eigen `sat_check.py` | **bron-gelegd** (z15 gezien: tankhouse-/procesgebouwen met blauwe en rode daken, tailings-bekkens ZO van het complex, open pit zichtbaar 2,5 km ZW aan de rand van het beeld — bevestigt mijn+plant naast elkaar) |
| `co-kasumbalesa-grens` | grensovergang DRC/Zambia (hergebruikt) | Kasumbalesa grenspost | -12.2658, 27.7959 | `koper-kolwezi-durban.md` §3/§4 | bron-gelegd (hergebruikt anker, niet opnieuw satelliet-gecheckt) |
| `co-nakonde-tunduma-grens` | grensovergang Zambia/Tanzania | Nakonde (ZM) / Tunduma (TZ) one-stop grenspost, aan de T2/TANZAM-weg | -9.3208, 32.7612 | OSM/Nominatim (Nakonde node 2735168295, -9.33145/32.75479; Tunduma node 262107914, -9.31016/32.76753; middelpunt) + eigen `sat_check.py` | **aannemelijk** (z15 gezien: de doorgaande hoofdweg loopt dwars door de dichtbebouwde tweelingstad; geen los aanwijsbaar grensgebouw op dit beeld, dus geen bron-gelegd) |
| `co-dar-kade` | overslag truck → container → zeeschip | Dar es Salaam Port, Container Terminal II (Berth 8-11), Kurasini | -6.8394, 39.2968 | OSM/Nominatim (node 11941611773) + eigen `sat_check.py` | **bron-gelegd** (z15 gezien: containerstapels en meerdere schepen langs de kade op het Kurasini-schiereiland, tegenover de olieterminal/raffinaderij op de oostoever) |
| `co-ningbo-kade` | overslag zeeschip → (onbekend vervolg, hergebruikt) | Beilun Container Terminal Phase 2, Ningbo-Zhoushan | 29.9353, 121.8695 | hergebruikt anker, `kobalt-tfm-quzhou.md` §3 | bron-gelegd (eerder z15 satellietgecheckt) |

## 4 · Via-punten
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Kisanfu-dorp / RN39-aansluiting (spoorstation Kisanfu, óp de RN39) | -10.6881, 25.9404 | hier sluit de mijnweg van de plant aan op de doorgaande RN39 (OSM `railway=station` direct aan de weg, dorp 0,9 km zuidelijker) |
| b1 | 2 | Likasi (RN39 → RN1, hergebruikt) | -10.9806, 26.7355 | zelfde knooppunt als `koper-kolwezi-durban`/`kobalt-tfm-quzhou`; sluit de RN1-westtak (Kolwezi) uit |
| b1 | 3 | Lubumbashi (RN1, hergebruikt) | -11.6642, 27.4827 | zelfde corridor als TFM/KCC; pint de RN1 richting Kasumbalesa |
| b1 | 4 | **Kasumbalesa** — einde been b1 (hergebruikt anker) | -12.2658, 27.7959 | verplichte grenspost |
| b2 | 1 | Ndola (T3 → T2) | -12.9693, 28.6366 | draait van de Copperbelt-T3 op de Great North Road (T2) |
| b2 | 2 | Kapiri Mposhi (T2/T3-kruispunt) | -13.9699, 28.6786 | vaste zuidwaartse T2-lus vóór de weg weer noordoostwaarts naar Tanzania buigt; sluit de kortere T2-tak naar Lusaka uit |
| b2 | 3 | Mpika (T2, wissel Serenje/Chinsali) | -11.8432, 31.4555 | de Great North Road draait hier van zuid-noord naar noordoost richting Chinsali/Isoka/Nakonde |
| b2 | 4 | Isoka | -10.1535, 32.6369 | laatste grote plaats vóór de grens, pint de T2 vlak vóór Nakonde |
| b2 | 5 | **Nakonde/Tunduma** — einde been b2 | -9.3208, 32.7612 | verplichte grenspost |
| b3 | 1 | Mbeya (A7/T1, wissel TANZAM → Centraal Corridor) | -8.9065, 33.4687 | hier draait de weg van de TANZAM-highway (naar Zambia) op de Centrale Corridor oostwaarts naar Dar es Salaam |
| b3 | 2 | Iringa (A7) | -7.7789, 35.6971 | enige verharde doorgaande route, pint de A7 tussen Mbeya en Morogoro |
| b3 | 3 | Morogoro (A7, wissel richting Dar es Salaam) | -6.8162, 37.6694 | laatste grote knoop vóór de kustvlakte; sluit een noordelijke omweg via Dodoma/Arusha uit |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| KFM Kisanfu-plant | CMOC Group 71,25% / CATL 23,75% / DRC-staat 5% | koper-kobalterts → kobalthydroxide (+ koperkathode) | H1 2026: 24.824,78 t hydroxide / 8.410,14 t Co — grootste DRC-hydroxide-exporteur dat halfjaar (20,9% van het DRC-totaal) | [5][6] |

## 6 · Stoppunt
De brief stopt op de Ningbo-kade (`co-ningbo-kade`): geen bron koppelt dit KFM-hydroxide aan een met naam genoemde Chinese raffinaderij (fase D vervalt, werkwijze licht §1); de Chinese bestemming is aannemelijk (generieke marktbestemming), niet mijn-specifiek gebrond. Deze volledig-truck-keten is de **huidige** situatie — de TAZARA-spoorconcessie (3 jaar bouw vanaf sept. 2025) kan een deel van b2/b3 pas op zijn vroegst rond 2028 naar spoor verschuiven [7][8], en dat is een aanstaande wijziging, geen fout in dit ontwerp.

## 7 · Open punten
- **Eigendom gecorrigeerd:** CMOC Group 71,25% / CATL 23,75% / DRC-staat 5% (niet 75%/25% zoals het ontwerp noemde) — bevestigd via twee onafhankelijke bronnen [5][6].
- **`co-kisanfu-laad` nu bron-gelegd** (was in het ontwerp geometrisch afgeleid, niet sat-checked); de exacte expeditiehal binnen het complex is niet apart aangewezen — anker blijft op site-niveau.
- **Been b1-lengte:** geen gepubliceerde bronlengte voor Kisanfu→Kasumbalesa specifiek; de eigen via-puntenketen (~290 km hemelsbreed) vervangt het ontwerp's ondermaatse "90–150 km"-schatting.
- **`co-nakonde-tunduma-grens` blijft aannemelijk:** geen los aanwijsbaar grensgebouw op de satellietpas, alleen de doorgaande hoofdweg door de tweelingstad.
- **KFM-aandeel via Dar es Salaam niet uitgesplitst:** Tanzania Ports Authority's 7,77 Mt DRC-bestemd vrachtvolume (2025/26) is een mix koper/kobalt/overig, niet kobalt- of mijn-specifiek [1][2].
- **Bestemming Ningbo Beilun** blijft aannemelijk — generieke China-bestemming, geen mijn-specifieke bron gevonden.
- **Dar es Salaam haven-aanloop** nog niet gemeten (afstand `co-dar-kade` tot de MARNET-zeeknoop); mogelijk een stippel-haven-aanloop nodig, net als bij Durban in `koper-kolwezi-durban.md`.
- **Grensvertraging Kasumbalesa/Tunduma** (totale doorlooptijd oost 40–55 dagen [3]) blijft het operationele knelpunt tot de $110 mln Kasumbalesa-modernisering (fase 1, mei 2026) volledig werkt — geen geometrisch punt, wel relevant voor de as.

## 8 · Bronnen
[1] African Business, "Rail and port upgrades drive Tanzania transport ambitions", https://african.business/2026/08/trade-investment/rail-and-port-upgrades-drive-tanzania-transport-ambitions
[2] Tanzania Ports Authority (via ontwerp-onderzoek), DRC-bestemd transitvrachtvolume 7,77 Mt in 2025/26 (53% van transitvracht)
[3] DiscoveryAlert, "Transport corridor economics Sub-Saharan Africa 2026" — Ndola-Tunduma ≈1.900 km, doorlooptijd oost 40-55 dagen, Kasumbalesa-modernisering $110 mln fase 1 mei 2026, https://discoveryalert.com.au/transport-corridor-economics-sub-saharan-africa-2026/
[4] Logistics Cluster, "Zambia border crossing Kasumbulesa", https://lca.logcluster.org/232-zambia-border-crossing-kasumbulesa
[5] Mining Technology, "CATL to acquire stake in DRC's Kisanfu copper-cobalt mine in $137m deal" — CMOC 71,25% / CATL 23,75% / DRC-staat 5%, https://www.mining-technology.com/news/catl-acquire-stake-drcs-kisanfu-copper-cobalt-mine-137m-deal/
[6] Energy and Mining SA, "Kisanfu leads DRC cobalt hydroxide exports as CMOC assets reach 31,7% share" (2026-08-30) — H1 2026: 24.824,78 t hydroxide / 8.410,14 t Co, 20,9% van het DRC-totaal, https://www.energyandminingsa.com/2026/08/30/kisanfu-leads-drc-cobalt-hydroxide-exports-as-cmoc-assets-reach-31-7-share/
[7] Railway Technology, "CCECC to revitalise Tanzania-Zambia Railway (TAZARA)" — $1,4 mld, ondertekend 2025-09-29, 3 jaar bouw + 27 jaar exploitatie, https://www.railway-technology.com/news/ccecc-tanzania-zambia-railway-authority/
[8] TAZARA, persbericht "CCECC to invest USD 1.4 billion in TAZARA revitalisation", https://tazarasite.com/press-release-ccecc-invest-usd-14-billion-tazara-revitalisation
[9] Fastmarkets, "Entreprise Générale du Cobalt announces shipments to Swiss traders" — DRC 207.134 t Co (hydroxide) 2025; kobaltproducenten versturen per truck naar Durban of Dar es Salaam, https://www.fastmarkets.com/insights/entreprise-generale-du-cobalt-announces-shipments-to-swiss-traders/
[10] Wikipedia, "Port of Dar es Salaam" — havenpositie 6.8351°Z/39.2938°O, DP World 30-jarige concessie (ondertekend okt. 2023, operationeel apr. 2024), Zambia 37,5% / DRC 30,3% van buitenlandse vracht, https://en.wikipedia.org/wiki/Port_of_Dar_es_Salaam
[11] Wikipedia, "Nakonde" / "Tunduma" / "Mpika" / "Kapiri Mposhi" / "Mbeya" / "Iringa" / "Morogoro" — posities en corridorrol (Great North Road/T2, TANZAM/T1/A7), https://en.wikipedia.org
[12] OpenStreetMap via Nominatim (ODbL) — node-coördinaten Kisanfu-dorp (629101463) en -spoorstation (382786322), Kasumbalesa (1187804129), Likasi (435789385), Lubumbashi (5399777), Ndola (315260631), Kapiri Mposhi (776377628), Mpika (918123116), Isoka (1260451930), Nakonde (2735168295), Tunduma (262107914), Dar es Salaam Container Terminal II (11941611773), opgevraagd 2026-09-28, https://nominatim.openstreetmap.org
[13] `koper-kolwezi-durban.md` — hergebruikte via-punten/geometrie Likasi/Lubumbashi/Kasumbalesa (§3/§4)
[14] `kobalt-tfm-quzhou.md` — hergebruikt anker `co-ningbo-kade` (§3) en Ningbo-zeeknoop (§2, b2)
[15] Esri World Imagery via `v2/tools/sat_check.py` (z15, 5 tegels per punt) — `v2/build-cache/satcheck/sat-kobalt-kisanfu-daressalaam-{plant,mine,nakonde-tunduma,dar-kade}.png`, 2026-09-28

## 9 · Gebakken (2026-09-28, lichte werkwijze)

**Stroom `kobalt-kisanfu-daressalaam`** → `v2/data/stroomroute-kobalt-kisanfu-daressalaam.json` — 7 benen, **14.179,3 km**, 25.541 punten, 5 markers. truck 360,3 + 1.075,2 + 930,1 + 0,4 (stippel) = 2.366,0 km · zee 20,9 (stippel) + 11.780,8 + 11,6 (stippel) = 11.812,4 km.
Recept: `bak_stromen.sh` (functie `bak_kobalt_kisanfu_daressalaam`).

**b1 (truck, nieuw profiel `kobalt-kisanfu-daressalaam-kisanfu-kasumbalesa`, extract congo-drc):** via-punten KFM Kisanfu-plant → Kisanfu-dorp/RN39 → Likasi (hergebruikt) → Lubumbashi (hergebruikt) → Kasumbalesa (hergebruikt anker). **360,3 km, 2.333 punten**, snaps 0,03/0,20/0,00/0,00 km, 16 keerlussen gesnoeid (361,2 → 360,3 km). Tegen de eigen schatting "~290 km hemelsbreed-keten" is dit **+24,2%** — **buiten ±15%, bevinding, niet dichtgetrokken**: er is geen gepubliceerde bronlengte om tegen te toetsen, en een echte weg is per definitie langer dan een hemelsbrede via-puntenketen (die zelf ook maar een schatting was, brief §7).

**b2 (truck, nieuw profiel `kobalt-kisanfu-daressalaam-kasumbalesa-nakonde`, extract zambia):** via-punten Kasumbalesa (hergebruikt) → Ndola → Kapiri Mposhi → Mpika → Isoka → Nakonde/Tunduma. **1.075,2 km, 10.734 punten**, snaps 0,00–0,16 km, 16 keerlussen gesnoeid (1.089,1 → 1.075,2 km). Tegen de brief-schatting "~1.750 km" is dit **−38,6%** — **buiten ±15%, bevinding**: de eigen hemelsbreed-keten (934,5 km) geeft een omwegfactor van **1,15**, plausibel voor deze hoofdweg; de "~1.750 km" (afgeleid via "Ndola–Tunduma ≈1.900 km minus Kasumbalesa–Ndola") is zelf een indirecte aftrekking van twee losse schattingen en blijkt de onwaarschijnlijke waarde — een verwachte ratio van 1,8-1,9 past bij geen enkele hoofdweg van deze lengte. Niet dichtgetrokken; het gemeten getal vervangt de gepubliceerde schatting niet, maar staat als bevinding naast hem.

**b3 (truck, nieuw profiel `kobalt-kisanfu-daressalaam-nakonde-daressalaam`, extract tanzania) — EINDIGT OP DE HAVENPOORT, NIET OP DE KADE:** eerste poging (naar-punt = co-dar-kade zelf) faalde met "geen wegpad tussen punt 3 en 4". Component-scan op de gescande graaf (diagnose-script, geen los repo-tool) wees de oorzaak aan: het interne wegennet van Container Terminal II is in OSM een **geïsoleerd eiland van 34 knopen**, 0,355 km van het doorgaande wegnet, zonder gedeelde vertex — een venster-vergroting (60 → 100 km) loste dit niet op, want het is geen venstermaat-probleem maar een topologiegat. Naar-punt aangepast naar de dichtstbijzijnde hoofdnet-knoop (39,29378/-6,84050, "Dar es Salaam-havenpoort"); daarna: via-punten Nakonde/Tunduma → Mbeya → Iringa → Morogoro → havenpoort. **930,1 km, 11.257 punten**, snaps 0,01–0,16 km, 13 keerlussen gesnoeid (940,6 → 930,1 km). Tegen "~950 km [ontwerp]" is dit **−2,1% [OK]**.

**b3b (truck, nieuw, stippel):** havenpoort → Container Terminal II-kade (`co-dar-kade`), rechte lijn **0,355 km** — emplacement/havenpoort, het interne havenwegennet zit niet in het net (bakhandleiding §2 "Emplacementen, havensporen..."). Naad b3→b3b **0,00 km**.

**b4a (zee, nieuw, stippel) — DE HAVEN-AANLOOP DIE HET ONTWERP AL VERMOEDDE, BLEEK OOK BINNEN DE 25 KM-NORM NODIG:** eerste bake zonder aanloop gaf `co-dar-kade` → `--been zee` direct; console meldde "snap 20,892 km" en de resulterende lijn bleek te **beginnen op de gesnapte MARNET-zeeknoop** (5310, -6,6537/39,3256), niet op de kade — een naad van **20,9 km**, ruim boven de ≤5 km-norm, ondanks dat 20,9 km binnen de --max-snap-grens van 25 km valt (hecht_marnet plakt onder die grens geen stub). `timeout 300 python v2/tools/maak_havenaanloop.py --naam kobalt-kisanfu-daressalaam-dar --van -6.8394,39.2968 --naar -6.65370,39.32560 …` liep vast (**exit 124**) — **geen tweede poging**, terugval op een rechte stippel kade→zeeknoop, **20,9 km, 2 punten**. Naad b3b→b4a en b4a→b4 nu **0,00 km**.

**b4 (zee, nieuw, MARNET):** `--been "zee|…|-6.8394,39.2968|29.9758,121.9736"` — 60 MARNET-edges, **11.780,8 km, 1.208 punten** (lengte-invariant getekende lijn vs. som edge-km: +0,32 km = de naden binnen het been zelf, ruim onder de norm). Tegen de indicatieve "~9.800 km" uit de brief is dit merkbaar hoger (+20%); de brief noemde dit getal zelf al "indicatief, exact bij MARNET-bake" — geen gepubliceerde bronlengte om hard tegen te toetsen, en de gemeten route (Indische Oceaan → Straat Malakka → Zuid-Chinese Zee → Oost-Chinese Zee) is geografisch de verwachte corridor. Niet dichtgetrokken.

**b4b (zee, haven-aanloop, letterlijke kopie, stippel):** exact `v2/build-cache/ais/graaf/kobalt-tfm-quzhou-aanloop-ningbo.geojson` uit `bak_kobalt_tfm_quzhou` (b2a) — geen nieuwe zeeknoop-lookup, geen nieuwe aanloop-run. **11,6 km, 5 punten**, ongewijzigd, 0,00 km over land. Naad b4→b4b **0,00 km**.

**Geen fase D/E:** conform brief §6 — geen bron koppelt dit KFM-hydroxide aan een met naam genoemde Chinese raffinaderij; de Ningbo-bestemming blijft aannemelijk (generieke China-markt).

**Toets:** alle 7 naden **0,00 km**, ruim onder de norm van 5 km. `toets_knikken.py`: **42 knikken ≥60° totaal over de stroom, 0 omkeringen ≥150°, 0 TERUGLOOP** — niets te repareren. `toets_rechte_benen.py --min-km 5`: **1 regel voor deze stroom** — de b4a-haven-aanloop (20,9 km, 🟡 MIDDEL, stippel) — verwacht en verklaard (maak_havenaanloop.py-timeout, hierboven); geen ander been van deze stroom in de uitslag, ook b3b (0,355 km) blijft onder de 5 km-drempel van het tool. json geldig: versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, zee}, alle 7 benen ≥2 punten. **Bevinding: bestandsgrootte 504,0 KB, boven de ~300 KB-richtwaarde** — verklaard door de twee lange 1-op-1-wegprofielen (b2: 10.734 punten, b3: 11.257 punten); niet dichtgetrokken (geen simplificatie gevraagd). Alle 5 markers liggen op 0 m van hun been (elk marker valt samen met een been-uiteinde).

**Gereedschapslessen:**
- **Een "geen wegpad tussen punt i en i+1"-fout op een venster dat al ruim is (100 km) is niet altijd een venstermaat-probleem.** Een component-scan (knopen bereikbaar vanaf elk anker, via een simpele stack-DFS over `_wegen_graaf()`'s `buren`-lijst) toont snel of het een genuine topologische scheiding is — hier een haven-emplacement van 34 knopen dat in OSM geen gedeelde vertex met het publieke wegnet heeft, ondanks een afstand van maar 0,355 km. VensterKm vergroten helpt dan niet en kost alleen een extra scan-ronde.
- **De ≤5 km-naad-norm is strenger dan de ≤25 km `--max-snap`-acceptatie.** Een snap van 20,9 km (< 25 km) laat de bake gewoon doorgaan, maar de resulterende lijn begint op de gesnapte knoop, niet op het anker — dat is een naad, niet een fout, maar hij moet nog steeds gemeten en gedicht worden (hier met een rechte stippel na een mislukte `maak_havenaanloop.py`-poging). "Snapt binnen de norm" en "geen naad" zijn twee verschillende toetsen.
- **Een indirect afgeleide "gepubliceerde" lengte (aftrekking van twee andere schattingen) is niet per se betrouwbaarder dan de eigen hemelsbreed-keten-schatting.** Been b2's gemeten omwegfactor (1,15) is voor een hoofdweg veel plausibeler dan de door de brief verwachte 1,8-1,9 — een signaal dat de "~1.750 km"-aftrekking zelf de zwakke schakel was, niet de gemeten route.
