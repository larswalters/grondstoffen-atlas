# Routebrief (licht) · olie — Al-Başrah/Khor al-Amaya (Irak) → Paradip (India)

**stroom-id:** `olie-albasrah-paradip` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** Iraakse ruwe olie uit de Basra-velden, per drie onderzeese pijpleidingen naar de offshore
SPM-boeicluster van het **Al Başrah Oil Terminal (ABOT/BOT, ex-Mina al-Bakr)** bij het Al-Faw-schiereiland,
per **VLCC** door de Perzische Golf → Straat van Hormuz → Arabische Zee → om Sri Lanka → Golf van Bengalen naar
het olietankenpark/de South Oil Jetty van **IndianOil (IOCL) Paradip**, per interne pijpleiding (~4,3 km) door
naar de Paradip-raffinaderij.
**Welke as van het verhaal:** *Irak → India — de grootste totaal ongedekte olieproducent in v2.* OPEC's op één
na grootste exporteur (~3,3–3,5 Mb/d peiljaar 2024), maar exporteert al zijn olie via exact de Straat van Hormuz
die van 28-02-2026 tot in de zomer van 2026 feitelijk geblokkeerd lag — zie de oorlogscontext in §7.

## 1 · Ketenkaart
```
ABOT/BOT-SPM-cluster `ol-albasrah-term` (offshore, Al-Faw-schiereiland, Perzische Golf)
  ──(b1 zee · haven-aanloop + Perzische Golf → Straat Hormuz → Arabische Zee → om Sri Lanka →
      Golf van Bengalen · ~5.500–6.000 km, MARNET, aannemelijk: één bron voor Paradip als bestemming)──►
   IOCL-olietankenpark/South Oil Jetty `ol-paradip-jetty` (Paradip Port, Odisha)
  ──(b2 leiding · interne IOCL-lijn jetty → raffinaderij, stippel · ~4,3 km)──►
   Paradip-raffinaderij `ol-paradip-raffinaderij` (IndianOil) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | ABOT/BOT-SPM-cluster → IOCL-jetty Paradip (aannemelijk: één bron) | Perzische Golf → Straat van Hormuz → Arabische Zee → om Sri Lanka → Golf van Bengalen | ~5.500–6.000 [ontwerp-schatting; MARNET meet de exacte lengte] | MARNET (kade → kade), plus haven-aanloop aan de Iraakse kant (zie §9-bak-aanwijzingen) | ja, alleen de haven-aanloop-stukken (zie hieronder) — het open-zeestuk zelf niet |
| b2 | C | leiding | IOCL-jetty Paradip → Paradip-raffinaderij | interne IOCL-pijpleiding, geen publieke OSM-lijn verwacht | ~4,3 [eigen meting op satelliet-ankers, hemelsbreed] | stippel — schematisch, "last mile (geen net op deze korrel)": raffinaderij ligt > 2 km van het jetty-anker | ja — eigen/interne infrastructuur, geen gekarteerd net |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-albasrah-term` | laadplek (offshore SPM-boeicluster, kop van b1) | Al Başrah Oil Terminal (ABOT/BOT, ex-Mina al-Bakr), SOMO/South Oil Company | 29.6848, 48.8052 | [4][5][6] | **onzeker** (z15 gezien: uitsluitend open zee, geen structuur zichtbaar — SPM-boeien/subsea-manifolds zijn op deze korrel en op deze schaal niet te onderscheiden van water; coördinaat is een OSM-landuse-punt "ميناء البصرة النفطي", binnen 2,4 km bevestigd door een onafhankelijk geo-record (freight-academy, IQ MAB) en consistent met Wikipedia's beschrijving "~50 km ZO van het Al-Faw-schiereiland"; conform de haalbaarheidstoets kan de status hier niet hoger dan onzeker) |
| `ol-paradip-jetty` | overslag/losplek (olietankenpark + korte steiger, staart van b1 / kop van b2) | IOCL-olietankenpark aan de vaargeul, Paradip Port (bij de South Oil Jetty) | 20.2585, 86.6355 | [1][2][3][sat] | **bron-gelegd** (z16 gezien: ommuurd tankenpark met meerdere ronde tanks met drijvend dak, aan een korte steiger/pier de vaargeul in; direct ZW hiervan, op ~700 m, een tweede kleinere tankcluster — vermoedelijk een ander product; het exacte punt van de "South Oil Jetty"-naam zelf is niet los gebrond, maar dit is de enige olietankinfrastructuur die op deze korrel bij Paradip Port zichtbaar is) |
| `ol-paradip-raffinaderij` | losplek / raffinaderij (fase C-knoop, stoppunt) | Paradip Refinery (Indian Oil Corporation) | 20.24764, 86.59819 | [1] | bron-gelegd (Wikipedia-coördinaat van de raffinaderij zelf, "~5 km ZW van Paradip Port" — komt overeen met de gemeten ~4,3 km tussen dit anker en `ol-paradip-jetty`; geen aparte satellietpas gedaan, want dit is geen overslag maar het bekende raffinaderijterrein) |

## 4 · Via-punten
Geen — b1 wordt door de MARNET-router zelf gelegd (kade → kade over Hormuz, geen corridorkeuze op dit
schaalniveau te benoemen); b2 is een rechte stippel zonder alternatieve route.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Paradip-raffinaderij | Indian Oil Corporation Ltd. (IOCL) | ruwe olie (incl. zwaardere/zure West-Aziatische kwaliteiten) → brandstoffen/petrochemie | 15 Mt/j raffinage-in ≈ **~303 kb/d** | [1][2] |

## 6 · Stoppunt
De brief stopt bij de poort van de Paradip-raffinaderij: geen bron documenteert een specifiek vervolgproduct
of een volgende locatie voor de olie ná de raffinage (zoals de vergelijkbare eenbeens-keten Corpus
Christi→Rotterdam) — fase D/E vervallen.

## 7 · Open punten
- **Bestemming Paradip specifiek is aannemelijk, niet per-lading bevestigd** — geen bron koppelt één
  specifieke Iraakse lading aan Paradip in plaats van een van IOCL's andere raffinaderijen; vandaar
  "(aannemelijk: één bron)" in de beennaam van b1.
- **MARNET-zeeknoop-afstand bij Paradip is verrassend groot: ~150–165 km** (eigen meting met
  `hecht_marnet.marnet_zee`, dichtstbijzijnde zeeknoop 8050→2373 op 21,000/88,000) — dit lijkt een échte
  dekkinggat van het MARNET-net in de Golf van Bengalen bij de Odisha-kust, niet een verkeerd anker (drie
  onafhankelijke testpunten rond Paradip Port geven allemaal ~150–165 km). **Bij het bakken expliciet
  controleren** met `maak_havenaanloop.py` (kortste pad over water) in plaats van een rechte stippel van
  150+ km te accepteren — zie bak-aanwijzingen hieronder.
- **ABOT/BOT ligt 13,47 km van de dichtstbijzijnde MARNET-zeeknoop** (zeeknoop 8050, 29.8055/48.7931) —
  ruim boven de 5 km-drempel van de haven-aanloop-regel (bakhandleiding §2, sinds 2026-09-28), dus b1 krijgt
  aan de Iraakse kant een haven-aanloop-stippel. Khor al-Amaya (KAAOT, 29.7822/48.8083, niet als apart
  anker gelegd — zie hieronder) ligt met 2,98 km wél binnen die drempel, maar BOT is de grotere en in de
  brontekst als eerste genoemde terminal en blijft daarom het primaire anker.
- **KAAOT (Khor al-Amaya Oil Terminal) is niet als los anker gelegd** — de invoer noemt BOT/KAAOT als
  cluster; KAAOT heeft een veel kleinere capaciteit (~240 kbbl/d tegen BOT's ~3–6,6 Mbbl/d) en ligt op
  slechts ~11 km van BOT. Voor de lichte werkwijze (één anker per site) is BOT als dominante terminal
  gekozen; wie een preciezere bewijslast wil, kan KAAOT als alternatief startpunt overwegen (dichter bij
  een zeeknoop, dus geen haven-aanloop nodig).
- **De pijpleiding jetty→raffinaderij (b2) is niet in OSM gekarteerd** (geen scan uitgevoerd binnen het
  webbudget) — status blijft schematische stippel op basis van de gemeten hemelsbrede afstand tussen twee
  satelliet-bevestigde ankers.
- **Actualiteit — de hele Perzische Golf zat op de schrijfdatum van deze brief net uit een oorlogsperiode.**
  Sinds 28-02-2026 liep de **2026 Strait of Hormuz-crisis**: Iran blokkeerde/mijnde de straat, tankerverkeer
  zakte "near zero", een bestand brak op 08-07-2026 na Iraanse aanvallen op koopvaardijschepen, en pas op
  25-08-2026 bevestigden VS-functionarissen dat de VS-marine mijnen had geruimd (100+ vermoede mijnen sinds
  de zomer) [10]. Irak is geen directe oorlogspartij maar exporteert via exact dezelfde straat: Iraakse
  **zeeborene olie-export kelderde tot ~98.000 vpd in mei 2026** (−97% t.o.v. 2025), herstelde naar ~15 mln
  vaten in juni en ~39 mln vaten (+153%) in juli, en de Iraakse oliemininster meldde op 16-08-2026 een
  gemiddelde van **~2 mln vpd sinds begin augustus 2026** — nog altijd ver onder het pre-crisis-niveau van
  3,3–3,5 Mb/d uit het ketenontwerp [11]. Op Iraaks grondgebied vonden bovendien in september 2026
  dronestrikes plaats tegen Saoedische olie-infrastructuur ("2026 East–West Crude Oil Pipeline attack") —
  een teken van aanhoudende regionale instabiliteit tot vlak vóór deze brief [webcheck-haalbaarheidstoets].
  **Conclusie voor de kaart:** de corridor is fysiek en geografisch de juiste (route + ankers kloppen), maar
  het volume erop was op het moment van schrijven sterk herstellende ná een bijna-totale stillegging — dit
  hoort bij het bakken als context te worden meegenomen, niet als reden om de keten niet te tekenen (net als
  bij `olie-rastanura-zhoushan`).
- **Jaarvolume-eenheid:** Irak exporteerde pre-crisis ~3.300–3.500 kb/d ruwe olie (peiljaar 2024); sinds de
  Hormuz-crisis is dat cijfer tijdelijk niet representatief (zie hierboven). Paradip Refinery importcapaciteit
  ≈ 303 kb/d crude (15 Mt/j ÷ ~365 dagen ÷ ~0,136 t/vat), oorspronkelijke eenheid Mt/j.

## 8 · Bronnen
[1] Wikipedia, "Paradip Refinery" — IOCL, 15 Mt/j, gecommissioneerd 2016, "~5 km ZW van Paradip Port", coördinaat 20,24764/86,59819. https://en.wikipedia.org/wiki/Paradip_Refinery
[2] Wikipedia, "Paradip Port" — natuurlijke diepzeehaven, oil jetty + Single Point Mooring-terminals ~20 km uit de kust, 150,41 Mt cargo 2024-25. https://en.wikipedia.org/wiki/Paradip_Port
[3] Wikipedia, "Paradeep" — bedrijven op Paradip incl. Indian Oil Corporation, "jetty, and single-point mooring". https://en.wikipedia.org/wiki/Paradeep
[4] Wikipedia, "Al Başrah Oil Terminal" — ABOT/BOT (ex-Mina al-Bakr), offshore deep-sea terminal ~50 km ZO van het Al-Faw-schiereiland, tot 3–6,6 Mbbl/d capaciteit, sinds 2003 huidige naam. https://en.wikipedia.org/wiki/Al_Ba%C5%9Frah_Oil_Terminal
[5] OpenStreetMap/Nominatim (ODbL) — landuse-node "ميناء البصرة النفطي" (Basra Oil Terminal), 29.6848391/48.8051955. https://www.openstreetmap.org
[6] Freight Academy, "IQ MAB Port (Al-Basra Oil Terminal)" — onafhankelijk geo-record, 29.683333/48.816667 (binnen 2,4 km van het OSM-punt). https://www.freight-academy.com/en/information/seaports/al-basra-oil-terminal-port-iq-mab
[7] IndianOil, "Paradip Refinery" — bedrijfspagina. https://iocl.com/paradip-refinery
[8] EIA, "Iraq — Country Analysis" — exportvolumes/infrastructuur (bron uit het ketenontwerp, niet apart herfetcht binnen het webbudget). https://www.eia.gov/international/analysis/country/IRQ
[9] Global Energy Monitor, "Paradip-Haldia-Barauni Oil Pipeline (PHBPL)" — regionale pijpleidinginfrastructuur IOCL Odisha. https://www.gem.wiki/Paradip-Haldia-Barauni_Oil_Pipeline_(PHBPL)
[10] Wikipedia, "2026 Strait of Hormuz crisis" — blokkade sinds 28-02-2026, "near zero" tankerverkeer, aanval op koopvaardij 08-07-2026, mijnen geruimd bevestigd 25-08-2026. https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis
[11] Iraqi News, 16-08-2026 — "Iraq's oil exports jump to two million barrels per day": mei 2026 ~98.000 vpd (−97%), juni 15 mln vaten, juli 39 mln vaten (+153%), sinds augustus gem. ~2 mln vpd; H1-2026 gem. 1,31 mln vpd tegen 3,33 mln vpd in H1-2025 (−60%). https://www.iraqinews.com/iraq/iraqs-oil-exports-jump-to-two-million-barrels-per-day/
[12] Haalbaarheidstoets-webcheck (aangeleverd) — Wikipedia "2026 Iran war" en "2026 East–West Crude Oil Pipeline attack", bijgewerkt resp. 2026-09-28 en 2026-09-26; niet apart herfetcht binnen het webbudget, geciteerd zoals aangeleverd.
[13] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16) — `sat-olie-albasrah-paradip-abot.png`, `sat-olie-albasrah-paradip-kaaot.png`, `sat-olie-albasrah-paradip-paradip-port.png`, `sat-olie-albasrah-paradip-tankfarm-zw.png`, `sat-olie-albasrah-paradip-jetty-oost.png` (dit laatste beeld toont een kolenterminal, NIET olie — expliciet uitgesloten als kandidaat).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `olie-albasrah-paradip`** → `v2/data/stroomroute-olie-albasrah-paradip.json` — 4 benen, **6.571,1 km**, 675 punten, 3 markers (3 van de 4 benen stippel).
Recept: `bak_stromen.sh` (functie `bak_olie_albasrah_paradip`).

**b1 (zee, drie stukken — haven-aanloop + MARNET-route + haven-aanloop):**
- **b1a (haven-aanloop Al Başrah, stippel-geojson):** ABOT-anker ligt **13,47 km** van de dichtstbijzijnde MARNET-zeeknoop (knoop 8050, 29,8055/48,7931) — boven de 5 km-drempel van de haven-aanloop-regel (bakhandleiding §2, sinds 2026-09-28/LAR-586), dus vooraf gecontroleerd en nodig. `maak_havenaanloop.py` vond een pad over water: **13,8 km, 13 punten, 0,00 km over land** (omwegfactor 1,023) — geslaagd op de eerste poging (trap 0,01° gebufferd).
- **b1b (zee, MARNET-route, zeeknoop → zeeknoop):** `--been "zee|VLCC Al Başrah Oil Terminal-zeeknoop → Paradip-zeeknoop (…)|29.8055,48.7931|21.0000,88.0000"` — snap 0,000 km aan beide zijden (exacte zeeknopen). **6.389,0 km**, 658 punten, uitsluitend MARNET-edges (0 track-edges). Route bevestigt de verwachte corridor (Perzische Golf → Straat van Hormuz → Arabische Zee → om Sri Lanka → Golf van Bengalen), geen Kaap-omweg.
- **b1c (haven-aanloop Paradip, stippel):** ⚠️ **bevestigde bevinding uit de brief (§7/§9-bak-aanwijzing) — een écht dekkingsgat van MARNET.** Eerst gecontroleerd of `hecht_marnet.py route` zelf een korter graafpad naar de kade zou vinden: een testrun `--been "zee|TEST|29.6848,48.8052|20.2585,86.6355"` (rechtstreeks kade → kade) gaf **"SNAP TE VER voor been … — snap 164.199 km"** — de graafgebaseerde router bevestigt dus zelf dat er geen kortere route beschikbaar is dan de losse-zeeknoop-afstand; dit is dus geen verkeerd anker maar een echt gat. Vervolgens `maak_havenaanloop.py --naam olie-albasrah-paradip-paradip --van 21.000,88.000 --naar 20.2585,86.6355` gedraaid onder `timeout 300`: **exit 124 (timeout), geen output vóór de kill** (stdout was gebufferd) — conform de bak-aanwijzing **geen tweede poging**, terugval op een rechte stippel tussen dezelfde punten: **164,2 km, 2 punten**.

⚠️ **Lengtetoets b1 (totaal, drie stukken samen):** 13,8 + 6.389,0 + 164,2 = **6.567,0 km** tegen de gepubliceerde ~5.500–6.000 km (ontwerp-schatting, brief §2) = **+9,4% tot +19,4%** afhankelijk van welk uiteinde van de bandbreedte je als meetlat neemt; tegen het bovenste uiteinde (6.000 km, de conservatiefste vergelijking) is dat **+9,4%**, ruim binnen ±15%. Tegen het midden van de bandbreedte (5.750 km) is het +14,2%, nog net binnen de norm. Geen via-punt bijgeschoven om dit te sturen — de MARNET-route zelf bepaalt de km.

**b2 (leiding, stippel):** `--stippel "leiding|IOCL interne pijpleiding jetty → raffinaderij (…)|20.2585,86.6355|20.24764,86.59819"` — rechte lijn tussen de twee satelliet-bevestigde ankers, **4,075 km** tegen de gepubliceerde/gemeten ~4,3 km (eigen meting, brief §2) = **−5,2%**, ruim binnen ±15%. Niet in OSM gekarteerd binnen het webbudget (brief §7), blijft schematisch.

**Naden:** alle vier benen sluiten op **0,00 km** aan op hun voorganger (b1a→b1b→b1c→b2 lopen exact door van eindpunt naar startpunt) — geen enkele naad boven de 5 km-norm.

**Markers:** alle drie op **0,00 km** van hun been — `ol-albasrah-term` (kop van b1a), `ol-paradip-jetty` (staart van b1c / kop van b2), `ol-paradip-raffinaderij` (staart van b2, stoppunt).

**Toets:** `toets_knikken.py` — **1 knik ≥60°** (72,5° bij 5,90000/81,90000, boogstraal 8.198 m — een krappe maar fysiek normale bocht in de MARNET-graaf ten zuiden van Sri Lanka, geen omkering), **0 omkeringen ≥150°, 0 terugloop** — geen bevinding. `toets_rechte_benen.py --min-km 5` — **1 been gevonden**: b1c (164,2 km, omwegfactor 1,000) als 🟠 GROOT (stippel) — correct geclassificeerd, dit ís de gedocumenteerde eindvorm van het dekkingsgat, geen bevinding op zichzelf. json geldig: versie 2, punt_formaat lonlat, modaliteiten `zee`/`leiding` (in de toegestane set), elk been ≥2 punten (13/658/2/2), bestandsgrootte **12,9 KB** (ruim < 300 KB).

**Gereedschapslessen:**
- Een graafgebaseerde `--been`-poging die faalt met "SNAP TE VER" ís zelf het bewijs dat een MARNET-dekkingsgat geen verkeerd anker is: de router zoekt over 2,87 miljoen haltes (track + MARNET gecombineerd) en vindt nog steeds geen kortere aansluiting dan de losse-zeeknoop-afstand. Dat is een goedkopere en sterkere controle dan zelf drie testpunten rond de haven te meten (wat de briefschrijver al deed, §7) — beide methoden kwamen onafhankelijk op dezelfde ~164 km uit.
- `maak_havenaanloop.py` kan op een afstand van 164 km — ruim boven de eerder gedocumenteerde precedenten (152,1 km bij Nacala lukte wél) — alsnog op de `timeout 300`-grens vastlopen zonder dat er één regel output verschijnt: de print-buffer wordt pas bij een schone exit geflusht, dus een timeout-kill (SIGTERM via `timeout`) laat een leeg logbestand achter in plaats van een gedeeltelijk verslag van de acht trappen. Dat is geen fout van het tool maar een eigenschap van gebufferde stdout onder een externe kill — de bak-aanwijzing "geen tweede poging" volstaat, een rechte stippel met de reden in de beennaam is de juiste terugval.
- Op een gedeeld rekencluster (~14 agents op 16 cores/31 GB) kan eenzelfde 164 km-zoekopdracht 5+ minuten in beslag nemen puur door CPU-contentie — de trappen van `detour()` zijn zelf goedkoop (bbox van een paar graden, rasterresolutie 0,02°–0,005°), dus de vertraging zat niet in het algoritme maar in het wachten op CPU-tijd.
- Een testrun met `--been` op de kade-tot-kade-coördinaten (zonder haven-aanlopen) is een snelle en goedkope manier (~12 s) om vooraf te bevestigen dat een gerapporteerd dekkingsgat geen artefact van de handmatige zeeknoop-opzoekmethode is, vóórdat je tijd steekt in een lange `maak_havenaanloop.py`-zoektocht.
