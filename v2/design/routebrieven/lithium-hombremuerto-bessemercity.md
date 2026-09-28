# Routebrief (licht) · lithium — Salar del Hombre Muerto/Fénix (Argentinië) → Antofagasta → Bessemer City (VS)

**stroom-id:** `lithium-hombremuerto-bessemercity` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** batterijgradig lithiumcarbonaat, al op de salar zelf uit de pekel geproduceerd door Arcadium Lithium's Fénix-operatie, gaat per **truck** over de Andes (Paso de San Francisco) naar de Chileense kust, per **containerschip** via het Panamakanaal naar de VS-Atlantische kust, en per **truck** naar Arcadium's eigen hydroxideconversiefabriek in Bessemer City (North Carolina) — de enige as van de atlas die een Zuid-Amerikaanse bron rechtstreeks aan de Amerikaanse IRA-onshoringketen knoopt.
**Welke as van het verhaal:** Argentijns carbonaat naar VS-eigen hydroxidechemie, via Chili i.p.v. via Buenos Aires — Fénix ≈40–45 kt Li₂CO₃/j (LCE) na de 2023-uitbreidingsfases (peiljaar ~2024, Livent/Arcadium jaarverslagen 2023–2025; indicatief) [7][9]; Bessemer City ≈15 kt LiOH·H₂O/j nameplate sinds de expansie eind 2022 (≈13,2 kt LCE-equivalent) [3][4][5] — hoger dan vaak aangenomen "historisch, in heropbouw"-beeld: de uitbreiding is al voltooid.

## 1 · Ketenkaart
```
Fénix-plant `li-hombremuerto-plant` ──(b1 truck · RN-43/provinciale weg · Paso de San Francisco · ~150–200 km, aannemelijk)──►
grens Paso de San Francisco ──(b2 truck · Ruta 31/23 → Ruta 5 noordwaarts · ~475–525 km, aannemelijk)──► Puerto Antofagasta `li-antofagasta-kade`
──(b3 zee · containerschip · Stille Oceaan → Panamakanaal → Atlantische Oceaan, MARNET beslist · ~9.000–10.000 km, ontwerpschatting)──►
Charleston, Hugh K. Leatherman Terminal `li-charleston-kade` ──(b4 truck · I-26 → I-85 · ~530–560 km)──► Arcadium Bessemer City `li-bessemer-fabriek` ⏹ stoppunt

vertakking (niet getekend): ≈60 % van Fénix' carbonaat verlaat Argentinië via Chileense havens (Antofagasta óf Mejillones), ≈40 % via Buenos Aires [1] — deze brief tekent bewust de Chili-as (corridordiversiteit t.o.v. de bestaande Olaroz→Buenos Aires-keten), niet de exclusieve route
vertakking (niet getekend): Livent/Arcadium gebruikt naast de truckroute ook de heractiveerde smalspoorlijn Pocitos–Antofagasta (Ferronor) voor product/reagentia [13] — rol t.o.v. de truckroute niet gemotiveerd in dit lichte stuk
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (carbonaat in big bags/tankwagens, aannemelijk: één bron) | `li-hombremuerto-plant` → grens Paso de San Francisco | RN-43/provinciale hooggebergteweg via Antofagasta de la Sierra en El Peñón | ~150–200 [ontwerpschatting, niet gepubliceerd op wegniveau] | maak_stroombeen_weg, extract argentina | nee |
| b2 | A | truck | grens Paso de San Francisco → `li-antofagasta-kade` | Ruta 31/Ruta 23 via Diego de Almagro en Chañaral naar Ruta 5 noordwaarts | ~475–525 [ontwerpschatting]; b1+b2 ≈675 km tegen Arcadium/Livent's eigen "675 km driving distance via Route 5" [1] | maak_stroombeen_weg, extract chili | nee |
| b3 | B | zee (containerschip) | `li-antofagasta-kade` → `li-charleston-kade` | Stille Oceaan zuidwaarts → Panamakanaal → Atlantische Oceaan (MARNET kiest het exacte pad) | ~9.000–10.000 [ontwerpschatting] | MARNET | aanloop Antofagasta: ja (bestaand, hergebruik `aanloop-antofagasta.geojson`, 97 km — zie [10]); aanloop Charleston: nee (kade 1,67 km van zeeknoop 9371, eigen meting [12]) |
| b4 | C | truck (containers) | `li-charleston-kade` → `li-bessemer-fabriek` | I-26 westwaarts via Columbia en Spartanburg → I-85 noordwaarts via Gastonia | ~530–560 [ontwerpschatting] | maak_stroombeen_weg, extracts us-south-carolina + us-north-carolina | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-hombremuerto-plant` | mijn / carbonaatplant | Fénix-operatie (Arcadium Lithium/Rio Tinto), Salar del Hombre Muerto, Catamarca | -25.3508, -67.1415 | [9] hergebruik sitelaag-anker `w-li-hombremuerto` | onzeker (z13 in de sitelaag: alleen de witte zoutvlakte zichtbaar, geen fabrieksgebouw te onderscheiden op deze korrel — al een open punt in de sitelaag zelf) |
| `li-antofagasta-kade` | overslag (laden) | Puerto Antofagasta, ATI-kade (frente 2) | -23.6500, -70.4088 | [10] hergebruik uit `lithium-atacama-antofagasta.md` | bron-gelegd (hergebruikt anker; welk sitio de lithiumcontainers laadt is daar al open) |
| `li-charleston-kade` | overslag (lossen) | Hugh K. Leatherman Terminal, SC Ports, North Charleston | 32.8392, -79.9352 | [8][11] Nominatim + satellietblik | bron-gelegd (z17 gezien: containerstapels en twee portaalkranen direct aan de kade, containerschip aangemeerd op het punt) |
| `li-bessemer-fabriek` | fabriek (losplek + conversieknoop) | Arcadium Lithium (ex-Livent), 1115 Bessemer City-Kings Mountain Hwy, Bessemer City NC | 35.2795, -81.3060 | [3][8][11] adres NC DEQ + Nominatim + satellietblik | bron-gelegd (z17 gezien: procesgebouw met torens/tanks midden in het fabriekscomplex, rechtstreeks aan de spoor-/laadzijde met wagons zichtbaar) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Antofagasta de la Sierra (aansluiting RN-40/RN-43) | -26.0592, -67.4066 | pint de zuidwaartse aftakking van de salarwerken naar de grenscorridor i.p.v. een noordelijke uitweg |
| b1 | 2 | El Peñón (laatste plaats vóór de grensklim) | -26.4754, -67.2653 | pint RN-43 westwaarts richting de pas i.p.v. verder zuid over RN-40 |
| b2 | 1 | Diego de Almagro (aansluiting op Ruta 5) | -26.3911, -70.0459 | pint waar de bergcorridor de Chileense hoofdas Ruta 5 bereikt |
| b2 | 2 | Chañaral (Ruta 5 kustcorridor) | -26.3479, -70.6224 | pint de noordwaartse Ruta 5-route i.p.v. een binnenlandse omweg |
| b4 | 1 | Columbia, SC (I-26 richting NW) | 34.0008, -81.0352 | pint de I-26-corridor landinwaarts i.p.v. een kustroute |
| b4 | 2 | Spartanburg, SC (I-26 → I-85) | 34.9498, -81.9320 | pint de overstap van I-26 op I-85 noordwaarts |
| b4 | 3 | Gastonia, NC (I-85 → laatste stuk naar Bessemer City) | 35.2623, -81.1838 | pint de aansluiting vanaf I-85 naar het fabrieksterrein |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Fénix-plant, Salar del Hombre Muerto | Arcadium Lithium (Rio Tinto) | lithiumpekel → batterijgradig Li₂CO₃, continu-proces op de salar zelf | ≈40–45 kt Li₂CO₃/j (LCE), peiljaar ~2024, indicatief | [7][9] |
| Bessemer City-fabriek, NC | Arcadium Lithium (ex-Livent) | Li₂CO₃ (o.a. uit Fénix) → LiOH·H₂O | ≈15 kt LiOH·H₂O/j nameplate (expansie voltooid eind 2022) ≈13,2 kt LCE-equivalent | [3][4][5] |

## 6 · Stoppunt
De brief stopt aan de poort van de Bessemer City-fabriek: dat is zelf de conversieknoop (carbonaat → hydroxide) en het eindpunt van het ketenontwerp — geen bron noemt een specifieke vervolgfabriek voor het hydroxide, fase D vervalt.

## 7 · Open punten
- **Fénix-plant-anker onzeker** — hergebruik van de sitelaag geeft alleen de salarcentroïde; op z13 is geen fabrieksgebouw te onderscheiden. Een nauwere pass (z15/z16) is nodig vóór dit een bron-gelegd anker wordt.
- **b1/b2-corridor is aannemelijk, niet op wegklasse-niveau gebrond** — de via-punten (Antofagasta de la Sierra, El Peñón, Diego de Almagro, Chañaral) zijn plausibele knopen op de kortste route tussen mijn en Ruta 5, maar geen bron citeert het exacte wegtracé; de km-som (675) klopt wel met Arcadium/Livent's eigen "driving distance via Route 5"-opgave [1].
- **Exportverdeling Chili vs Buenos Aires** — SEC-stukken geven ≈60 % via Chileense havens (Antofagasta/Mejillones) en ≈40 % via Buenos Aires [1]; deze brief tekent bewust de Chili-as, niet de exclusieve route van Fénix' productie.
- **Ferronor-smalspoor Pocitos–Antofagasta** — Livent heeft deze lijn heractiveerd voor product/reagentia [13]; welke rol dit spoor speelt t.o.v. de truckroute is in dit lichte stuk niet uitgezocht (`spoornet_nodig: false` in het ketenontwerp).
- **VS-aanlandingshaven niet bevestigd door een Livent/Arcadium-bron** — Charleston/Leatherman Terminal is gekozen op de zeeknoop-afstand (1,67 km, eigen meting [12], ruim onder Wilmington's 5,03 km) en SC Ports' regionale schaal, niet op een bron die zegt dat Bessemer City's import daadwerkelijk via deze kade loopt.
- **ATI-sitio Antofagasta** voor lithiumcontainers blijft open (zelfde punt als in `lithium-atacama-antofagasta.md`).

## 8 · Bronnen
[1] Arcadium Lithium plc, Form 424B3 (SEC, 2023): "approximately 675 kilometers driving distance from the port city of Antofagasta, Chile to the northwest, via national and provincial roadways and then Panamericana Norte Route 5"; 60% export via Chileense havens (Antofagasta/Mejillones), 40% via Buenos Aires. https://www.sec.gov/Archives/edgar/data/1977303/000114036123054020/ny20009544x16_424b3.htm
[2] Arcadium Lithium plc, Form 10-K FY2024 (SEC). https://www.sec.gov/Archives/edgar/data/1977303/000197730325000006/lthm-20241231.htm
[3] North Carolina DEQ, Fact Sheet Livent USA Corporation, permit NCD000771964 (2025-09-18): adres 1115 Kings Mountain Hwy, Bessemer City NC; 900 acres terrein, hoofdplant 68 acres. https://www.deq.nc.gov/ncd000771964liventfactsheet20250918pdf/open
[4] Arcadium Lithium (Livent), persbericht 2022-11-14: "Livent Completes North Carolina Expansion of Largest Lithium Hydroxide Production Site in the United States", capaciteit 15.000 t/j LiOH. https://ir.arcadiumlithium.com/investors/news/news-details/2022/Livent-Completes-North-Carolina-Expansion-of-Largest-Lithium-Hydroxide-Production-Site-in-the-United-States-11-14-2022/
[5] C&EN, "Livent completes expansion of lithium hydroxide plant" (2022). https://cen.acs.org/energy/energy-storage-/Livent-completes-expansion-lithium-hydroxide/100/i41
[6] Wikipedia (en), "San Francisco Pass": grenspas Argentinië–Chili, 4.726 m, coördinaat via MediaWiki API prop=coordinates. https://en.wikipedia.org/wiki/San_Francisco_Pass
[7] USGS, Mineral Commodity Summaries 2026 — Lithium (Argentinië-cijfer, indicatief, niet onafhankelijk gecheckt deze ronde). https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-lithium.pdf
[8] OpenStreetMap (ODbL) via Nominatim: Hugh K. Leatherman Terminal 32.84087,-79.93871; Wando Welch Terminal 32.83577,-79.88292 (verworpen, 5,35 km van de zeeknoop); adres Livent Bessemer City 35.2810592,-81.3067459; Antofagasta de la Sierra -26.0592,-67.4066; El Peñón -26.4754,-67.2653; Diego de Almagro -26.3911,-70.0459; Chañaral -26.3479,-70.6224; Columbia SC 34.0008,-81.0352; Spartanburg SC 34.9498,-81.9320; Gastonia NC 35.2623,-81.1838. https://www.openstreetmap.org
[9] `v2/design/lithium-sitelaag.json`, anker `w-li-hombremuerto`: -25.3508,-67.1415, status onzeker, capaciteit ≈25 kt Li₂CO₃/j (voorzichtiger dan de ~40–45 kt in het ketenontwerp; beide indicatief).
[10] `v2/design/routebrieven/lithium-atacama-antofagasta.md` §3/§9: anker `li-antofagasta-kade` -23.6500,-70.4088 (= `cu-antofagasta-kade`), bestaande haven-aanloop `aanloop-antofagasta.geojson` (97,1 km, zeeknoop -23.80,-71.30).
[11] Esri World Imagery via `v2/tools/sat_check.py` (z16–z17, live): `v2/build-cache/satcheck/sat-lithium-hombremuerto-bessemercity-{charleston-kade,bessemer-fabriek}.png`.
[12] Eigen zeeknoop-meting (bakhandleiding-licht §2-recept, `v2/build-cache/marnet-preais`): Charleston/Leatherman-kade → zeeknoop 9371 (32.85420,-79.93580) op 1,67 km; Wando Welch → zelfde zeeknoop op 5,35 km (verworpen); Wilmington NC → zeeknoop 9365 op 5,03 km (ter controle tegen de haalbaarheidstoets — komt overeen); Antofagasta-kade → zeeknoop 4664 op 92,24 km (bestaand, ongewijzigd).
[13] Haalbaarheidstoets van deze golf (WebSearch 2026-09-28, niet zelf herhaald dit ronde — Dialogue Earth gaf een 403, het volledige SEC-S-4/A-document was te groot om te fetchen): SEC-stukken (S-4/A, 10-K) en Dialogue Earth bevestigen dat Livent de Pocitos–Antofagasta-spoorlijn (Ferronor) heeft heractiveerd voor product/reagentia.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `lithium-hombremuerto-bessemercity`** → `v2/data/stroomroute-lithium-hombremuerto-bessemercity.json` —
**6 benen, 8.703,6 km, 14.931 punten, 6 markers, 313,4 KB.** truck 163,6 + 112,2 (stippel) + 729,2 + 415,4 =
1.420,4 km · zee 97,1 (stippel, haven-aanloop) + 7.186,1 = 7.283,2 km. Recept: `bak_stromen.sh` (functie
`bak_lithium_hombremuerto_bessemercity`).

**b1 (truck, GESPLITST op El Peñón):** `maak_stroombeen_weg.py --profiel
lithium-hombremuerto-bessemercity-hombremuerto-elpenon --bron geofabrik` gaf **163,6 km · 1.650 punten**
(Fénix-plant → El Peñón, RN-43 via Antofagasta de la Sierra; extracts argentina+chili). Een poging het hele been
tot de grens te scannen (`...-hombremuerto-grens`, dezelfde extracts) gaf **tweemaal** "geen wegpad tussen punt 2
en 3" (El Peñón → grens) — eerst met alleen extract `argentina`, toen ook met `chili` erbij: geen doorlopende
OSM-weg over de hooggebergteklim (Paso de San Francisco, ~4.726 m). Het reststuk El Peñón → grens Paso de San
Francisco (**112,2 km, rechte stippel**) is dus precies het geval dat de brief anticipeerde (§2: "geen stippel
verwacht tenzij OSM geen wegpad geeft op deze hoogte") — geen tweede poging voorbij deze twee toetsen.

**b2 (truck, grens → Antofagasta-kade):** `maak_stroombeen_weg.py --profiel
lithium-hombremuerto-bessemercity-grens-antofagasta --bron geofabrik`, extract `chili` — **729,2 km · 8.541
punten** over drie deelstukken (grens → Diego de Almagro 300,7 km · Diego de Almagro → Chañaral 66,6 km ·
Chañaral → Antofagasta-kade 404,9 km na 166 gesnoeide keerlussen). Tegen de ontwerpschatting van ~500 km (midden
van 475–525) is dat **+45,7%, buiten ±15%.** ⚠️ **Geen via-punt bijgeschoven** (werkregel: buiten de norm =
bevinding, niet dichttrekken). De twee deelafstanden komen overeen met de reële hemelsbrede/wegverhouding van een
bergafdaling (~2,0×) resp. de Ruta 5-kustcorridor (~1,35×) — Arcadium/Livent's "675 km via Route 5" (brief bron
[1]) dekt vermoedelijk b1+b2 samen zonder de kustomweg via Chañaral die deze brief bewust tekent, of is een
punt-naar-punt-cijfer op een andere corridor. Blijft staan als bevinding.

**b3 (zee):** haven-aanloop Antofagasta hergebruikt (`aanloop-antofagasta.geojson`, **97,1 km · 46 punten**,
gedeeld met `lithium-atacama-antofagasta`/`koper-aurubis-hamburg`, geen nieuwe run). Zeebeen
`--been "zee|...|-23.800,-71.300|32.8392,-79.9352"`: snap Antofagasta-zeeknoop **0,000 km** (al op de knoop) —
snap Charleston-kade **1,669 km** (eigen meting bevestigt brief[12]: kade 1,67 km van zeeknoop 9371, ruim onder
de 5 km-norm van LAR-586 → terecht geen haven-aanloop aan de Charleston-kant). Resultaat **7.186,1 km · 745
punten** (Stille Oceaan → Panamakanaal → Atlantische Oceaan), lengte-invariant getekende lijn 7.186,138 vs som
edge-km 7.186,600 km = −0,462 km (de naden). Tegen de ontwerpschatting van ~9.500 km (midden van 9.000–10.000) is
dat **−24,4%, buiten ±15%** — een bevinding, geen fout: de gemeten Panama-route (Antofagasta → Panama ~4.300 km +
Panama → Charleston ~2.900 km ≈ 7.200 km hemelsbreed-som) bevestigt onafhankelijk dat 7.186 km de realistische
afstand is en de ontwerpschatting te hoog lag.

**b4 (truck, Charleston → Bessemer City):** `maak_stroombeen_weg.py --profiel
lithium-hombremuerto-bessemercity-charleston-bessemer --bron geofabrik`, extracts `us-south-carolina` +
`us-north-carolina` (1.417 dubbele grensways weggevallen) — **415,4 km · 3.947 punten** (I-26 via Columbia/
Spartanburg → I-85 via Gastonia, 10 kleine keerlussen gesnoeid). Tegen de ontwerpschatting van ~545 km (midden
van 530–560) is dat **−23,8%, buiten ±15%** — eveneens een bevinding: de gemeten interstate-afstand is
waarschijnlijk preciezer dan de ongegronde ontwerpschatting.

**Toets naden:** alle overgangen **0,00 km** behalve been 5 (zee) → been 6 (truck): **1,669 km** — het zeebeen
eindigt op de MARNET-zeeknoop-snap bij Charleston (1,67 km van de kade-anker, ruim onder de 5 km-norm van §5),
geen haven-aanloop vereist. Geen enkele naad boven 5 km.

**`toets_knikken.py`:** 99 knikken ≥60°, **0 omkeringen ≥150°, 0 TERUGLOOP.** Alle 98 spikes op de truckbenen zijn
scherpe OSM-digitaliseringshoekjes (straal 2–90 m, vooral rond kruispunten in Chañaral/Diego de Almagro en bij de
Charleston/Bessemer City-stadsranden) — geen kopmaak-plekken, geen fout. Eén "krappe bocht" op het zeebeen
(71,8°, straal 5.455 m bij 9,1183/-79,8032, de nadering van het Panamakanaal) is een normale routebocht, geen
omkering.

**`toets_rechte_benen.py --min-km 5`:** precies **1 stippel-been** in de uitslag, zoals verwacht —
`El Peñón → grens Paso de San Francisco (112,2 km, omwegfactor 1,000)`, correct gelabeld als stippel (§2:
stippel = "hier reikt het net niet").

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, zee} (binnen de toegestane set),
elk been ≥2 punten (minimum 2, de stippel), bestandsgrootte **313,4 KB** — ⚠️ **iets boven de ~300 KB-richtwaarde**
(+4,5%), veroorzaakt door het lange, dichte weg-been b2 (8.541 punten uit een niet-gesimplificeerde OSM-scan);
geen actie ondernomen (richtwaarde, geen harde limiet).

**Markers:** alle zes markers liggen **exact op de lijn (0,0 m)** — inclusief El Peñón en de grens, want beide
zijn letterlijk het start-/eindpunt van het aangrenzende been (geen aparte snap).

**Open punten die blijven staan (zie ook §7):** Fénix-plant-anker blijft onzeker (geen nauwere satellietpass
gedaan in deze bake-ronde); de b1/b2-corridor blijft aannemelijk op wegklasse-niveau; de exportverdeling
Chili/Buenos Aires en het Ferronor-smalspoor blijven ongebruikt/niet getekend; de Charleston-aanlandingshaven
blijft ongebrond door een Livent/Arcadium-bron. Nieuw open punt: de drie grote km-afwijkingen (b2 +45,7%, b3
−24,4%, b4 −23,8%) zijn alle drie tegen een **ontwerpschatting** getoetst, niet tegen een gepubliceerde bron —
een latere ronde met een echte bron per been zou de norm pas zinvol kunnen toetsen.

**Gereedschapslessen:**
- Een `--profiel`-poging die op "geen wegpad tussen punt N en N+1" stuit, hoeft niet blind herhaald te worden:
  het toevoegen van een buur-extract (hier `chili` naast `argentina`, want het grenspunt ligt letterlijk op de
  landsgrens) is een gerichte tweede toets, geen herhaling, en bevestigt het ontbreken van een doorlopende weg
  in plaats van het te verhullen.
- Een gesplitst been (gemeten stuk + stippel) vraagt **twee losse `PROFIELEN`-sleutels** in
  `maak_stroombeen_weg.py`, niet één profiel met een falend laatste via-punt: het gemeten deel moet als eigen
  `--bron geofabrik`-run met zijn eigen lengtetoets blijven bestaan (hier hernoemd van
  `...-hombremuerto-grens` naar `...-hombremuerto-elpenon`).
- Drie van de vier meetbare benen wijken >20% af van hun ontwerpschatting, in beide richtingen (b2 te laag
  geschat, b3/b4 te hoog geschat) — een teken dat "ontwerpschatting, niet gepubliceerd" in een lichte brief
  letterlijk moet worden genomen: de bake-uitkomst is de eerste harde meting, en drie onafhankelijke ±20%+-
  afwijkingen op dezelfde stroom zijn eerder een signaal over de brief-schattingen dan over de route zelf.
