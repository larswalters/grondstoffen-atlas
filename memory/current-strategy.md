# Current strategy — Grondstoffen Atlas
*Last updated: 2026-07-18 (v2 is de actieve bouwplaats; vectorwereld = bron van waarheid)*

## 🌍 Sinds 2026-07-18 — er zijn TWEE codebases, en `v2/` is de actieve

- **Root van de repo = de bevroren v1-atlas.** Blijft live, wordt niet meer aangeraakt. Vanilla JS + globals
  + Three **r128** via script-tags.
- **`v2/` = de nieuwe bouwplaats.** Three **r185**, **ES-modules met importmap**, geen bundler en geen
  build-stap. Draait mee op Pages onder `…/grondstoffen-atlas/v2/`. **Harde regel: buiten `v2/` niets.**

### De lagenordening in v2 (belangrijker dan de bestandsindeling)
1. **De vectorwereld is de WAARHEID** — waar land ophoudt en water begint. Natural Earth 1:10M, één
   `LineSegments`. Hiertegen wordt geverifieerd en straks gerouteerd.
2. **De tegels zijn een SKIN** — Esri World Imagery (of OSM) op het detailniveau dat bij de kijkhoogte past.
   Mooi en handig om plekken te herkennen, maar geen bewijs: de shell is ~9,8 km/pixel en de bron verschilt
   van Natural Earth.
3. **De weergave staat los van beide** — ondergrond (satelliet/kaart/egaal) en kustlijn (aan/uit) zijn
   onafhankelijke schakelaars.

Dit is de directe voortzetting van het ontkoppelingsprincipe hieronder: **één ding = één verantwoordelijkheid.**
Waar v1 één puntenlijst drie taken liet dragen, laat v2 niet één laag tegelijk "mooi" én "waar" zijn.

### Twee dingen die je moet weten vóór je code schrijft in v2
- **lat/lon → 3D volgt EXACT v1's `latLonToVec3`** (`x = cos(lat)·cos(lon)`, `z = −cos(lat)·sin(lon)`). Het
  moet tegelijk kloppen met de UV-afbeelding van `THREE.SphereGeometry` én met wat in M26 uit v1 komt.
- **Zoom rekent in hoogte boven het oppervlak**, niet in afstand tot het middelpunt. Alles wat met zoom
  schaalt (sleepsnelheid, tegelniveau, de opheffing van de kustlijn) hangt aan `getAltitude()`.

## 🏗️ Het leidende architectuurprincipe sinds 2026-07-18 — ONTKOPPELEN

De atlas zat vast in een patch-spiraal: elke fix brak iets anders. Oorzaak was geen reeks bugs maar **één
gekoppelde structuur** — dezelfde puntenlijst bediende drie taken met tegenstrijdige eisen:

| taak | wil | krijgt sinds 18 juli |
|---|---|---|
| **vorm** van de lijn | weinig punten, alleen echte bochten | eigen geometrie (817 punten) |
| **vaarsnelheid** van de schepen | punten gelijkmatig over afstand | `getPointAt` (booglengte) |
| **baan-klem** (vaarbanen) | juist veel punten in nauw water | eigen profiel `wp`, per 20 km |

**Toets bij elke nieuwe wijziging: raakt dit meer dan één van die drie?** Zo ja, ontkoppel eerst. Het bewijs dat
dit klopt: na de ontkoppeling verbeterde *alles tegelijk* — snelheidsvariatie 15,9× → 1,27× (slechtste 47× → 2,3×),
landtreffers 406 → 108, Japan 8 → 0, Baja 21 → 0, Malakka 9 → 0 — terwijl élke eerdere ronde winst op het ene
inruilde tegen verlies op het andere.

**Vaste pipeline (volgorde telt):**
`bake_searoutes.py` (vorm) → `lane_widths.js` (klem-profiel) → `check_corridors.js` (validatie) →
`stamp_assets.js` (**cache-busting — anders ziet Lars niets veranderen**) → `build-standalone.py` (55 checks).

## 🧩 De volgende structurele stap: één gedeeld netwerk (LAR-483)

Corridors worden nu **per haven-paar** gebakken. Daardoor: routes naar dezelfde bestemming bundelen niet
(Lars: *"lijnen gaan uit elkaar terwijl ze dezelfde bestemming hebben naar China"*), dezelfde kapotte edge wordt
steeds opnieuw gerepareerd (7 corridors deelden hetzelfde Baja-trapje), en antipodale paren kiezen willekeurig
een halfrond. **MARNET gemeten:** 15.840 segmenten / 9.646 knopen, segment mediaan 83 km maar **max 3.611 km** →
een **grove graaf, geen waterkaart**; kaal over de bol leggen voorkomt land-treffers níet. De aanpak is het
netwerk **één keer** verzoenen met onze landpolygonen en daarover routeren — dan erven alle 14 grondstoffen die
waterschoonheid, bundelen routes vanzelf, en werkt M21 native (knelpunt = edge eruit).

## 🖥️ Weergave-laag (2026-07-17, bevestigd) — de ondergrond staat nu
Drie fixes live en door Lars bevestigd; hij pauzeerde de pilot er bewust voor. **Wat dit betekent voor de manier
waarop we verder werken:**
- **De kaart is scherp op élke zoomstand en breedtegraad** (LAR-479: `cos(lat)` + budget 96 + midden-naar-buiten).
  Route-beoordeling op mobiel is daardoor betrouwbaarder dan tijdens de vorige pilot-test — een wazige onderhelft
  kon eerder een routefout maskeren.
- **De bol is bestuurbaar ingezoomd** (draaien schaalt met de camera-afstand). Van dichtbij een corridor volgen is nu
  praktisch mogelijk; dat is precies wat de M18-verificatie vraagt.
- **Markers verdwijnen niet meer op tier; `tier` = alleen labels** (LAR-481). De tier-LOD is dus de facto uit voor
  markers — hou daar rekening mee bij nieuwe nodes: **een node krijgt geen zichtbaarheid meer "gratis" van een flow**
  (de `forced`/`usedNodeIds`-uitzondering bestaat niet meer), maar hij verdwijnt ook nooit meer.
- **Vaste knoppen:** `CONFIG.tiles.maxTiles` (noodrem, 96) · `CONFIG.markers.labelZoomByTier` (het échte declutter-
  mechanisme) · `CONFIG.globe.dragSpeed`/`dragRefZoom` (draaigevoel, geankerd op de startzoom).

## ⚡ Stand van de pilot (2026-07-17, avond) — MIDDEN IN DE TEST
Koper vaart volledig op gebakken MARNET-corridors (22 stuks, 26 KB, `data/_searoutes.js`), 3× live op Pages
(t/m `3c801a0`). **Nog geen go:** Lars ziet op mobiel nog routes over Japan (stale-cache-hypothese, morgen
verifiëren) én wil de wereldbal-weergave duidelijker vóór de uitrol. **Principe aangescherpt: "MARNET beslist"** —
corridors kaal haven→haven, óók echte knelpunten niet meer afgedwongen; knelpunt-ringen + laneShape-ankers worden
**afgeleid uit de geometrie** (≤150 km). De milestone-diagnose is onderweg gecorrigeerd: niet "1.090 km omweg"
(antipodaal → 231 km echt) maar **verkeerd geplaatste via-punten** (`wp-taiwan` +1.497 km) en **trapjes** waren het
probleem; winst nu gemeten: zeereizen −9,3%, ratio 1,203→1,091. Twee diepe render-lessen: corridor-reparaties horen
in de **baker** (de-zigzag + landomleiding met kustbuffer, checker `tools/check_corridors.js`) en de **curve-
bemonstering** mag nooit invoerpunten overslaan (adaptief gemaakt in `util.js` — verifieer op de gétekende curve,
niet alleen op de data).

## 🧭 Nu (2026-07-17) — eerst de routes, dan de features

De atlas is **inhoudelijk compleet** (14 grondstoffen, backlog leeg). De volgende stap is bewust **géén 15e
grondstof** maar **route-kwaliteit** — want de drie geplande features **staan erop**: M19-stress telt verkeerd als een
boot "toevallig" langs Hormuz scheert, en M21-simulator liegt als de routes niet écht door Malakka gaan. *Een
impact-teller op verkeerde routes is erger dan geen teller.*

**De routing is aantoonbaar onrealistisch** (audit 2026-07-17). Antofagasta→Shanghai: grote-cirkel 18.526 km ·
searoute (echte lanen) 18.880 km (+2%) · **onze bol 19.970 km (+8%)** — het handgeplaatste vaarpunt **`wp-pac-zuid`**
(26°Z) dwingt **~1.090 km omweg** af. Drie oorzaken in `searoute.js`: **`openRadiusDeg: 1.2`** (~130 km geforceerd
water rond élk knelpunt → A\* vaart dwars over land) · **8-richtingen-A\*** (trapjes) · **grof raster + gretige
heuristiek + géén echte vaarlanen**. De `via`-ketens blijken grotendeels **handmatige compensatie voor een slechte
router**.

**→ M18 · Realistische zeeroutes (searoute)** = routeren over een **echt scheepvaart-lanen-netwerk** (Eurostat
MARNET via het Python-pakket `searoute` 1.6.0): **precompute at build-time, gededupliceerd per haven-paar** (één
gedeelde corridor-cache over alle 14 → je routeert unieke corridors, niet elke flow), polylines in
`data/_searoutes.js`, atlas rendert direct; **netwerk bewaren** zodat M21 een knelpunt blokkeert als *edge eruit →
herrouteren*; **raakt alleen zee-legs** (land/lucht ongemoeid); runtime blijft pure JS, `searoute` = build-dependency.
Bonus: A\* uit de runtime = lichter op mobiel. **Pilot-first: koper** (LAR-474) → go/no-go Lars → dan de andere 13.

**Volgorde:** M18 → M19 (knelpunt-stress) → M20 (China-meta-view) → M21 (disruptie-simulator).
**Open besluit (Lars, bij de pilot):** via-punten op zee-legs opruimen of behouden als hint.
**Harde regel:** vergelijk nooit tegen een kale origin→dest A\*-run — altijd tegen wat `flows.js` werkelijk rendert.

---

*Eerder (2026-07-16 — M17 · Kolen uitgevoerd; richting 14 uitgewerkt, gas M15/diamant M16 parallel):*

## Architectuur (hoe we bouwen)

> ✅ **Modulair = bron van waarheid, in gebruik.** Onderstaande beschrijft de **modulaire** opzet, die nu als
> git-repo in déze projectmap staat (`Projects\General\grondstoffen-atlas`, 2 commits). De M5-fixes zijn erin
> geport. De single-file `atlas-lithium-kobalt.html` op het bureaublad is nog slechts referentie/deploy-build.

- **Vanilla JS + Three.js, geen bundler.** Losse globals-bestanden, vaste laadvolgorde via
  `<script>`-tags in `index.html`.
- **Scheiding:** `config.js` (instellingen) · `geo-data.js` (`LAND_POLYS`) · `src/` (rendering-modules)
  · `data/` (`_registry.js`, `_chokepoints.js` + één bestand per grondstof).
- **Routering:** A\*-algoritme over een **1440×720 land/zee-raster** (0,25°/cel, opgebouwd uit
  `LAND_POLYS` in ~35 ms). Zeeroutes = zee begaanbaar; landroutes = gespiegeld raster.
  - Knelpunten (`_chokepoints.js`) worden als **water geforceerd** (`openRadiusDeg: 1.2`) zodat smalle
    straten (Lombok, Makassar) begaanbaar blijven.
  - **Gewogen A\*** (`heuristicWeight: 1.35`, `maxExpansions: 1500000`) voor lange oceaanroutes.
  - `LAND_LINKS` (Øresund, Storebælt, Fehmarn, Kanaaltunnel, Bosporus) worden als land geforceerd.
  - **Vaarbanen** (`laneShape(t)` in `util.js`): parallelle stromen waaieren onderweg uit maar knijpen
    bij een knelpunt samen tot één punt — precies het beeld waar de atlas om draait.
- **Rendering-details:** schaal op basis van afstand tot boloppervlak (`scaleFor()` in `markers.js`,
  `Math.pow(d/dref, exp)` met `d = camera.z - R`), kaderloze labels met botsingsdetectie
  (prioriteit `tier × 100 − share`), tegellaag (`tiles.js`, Esri/OSM) onder z=6.2, autorotate uit na
  eerste interactie.
- **Tijd:** `voyages.js` + afspeelbalk — schepen/vluchten bewegen over de tijd langs hun gerouteerde pad.
- **Luchtroute-modus (sinds M6):** een **3e route-type** naast zee-A\*/land-A\*. In `flows.js` krijgt
  `mode:"air"` een `&& !airMode`-uitzondering op de A\*-routering en wordt het een **opgetilde great-circle-boog**
  (`flat:false` + `arcStyle`-lift, hoogte ∝ afstand) — óók in de `routes`-weergave. Korte hops blijven
  `road`/`rail` (land-A\*). `makeRouteCurve` schaalde de booghoogte al met de routelengte. Voyages pusht nu
  ship+air; de tijdlijn-teller is resource-bewust ("✈ vluchten" ↔ "⚓ schepen", via `UI.setVoyageNoun`).
- **Optionele lagen via filter (herbruikbaar patroon, nu 5×):** goud-CB, koper-exchange, REE-recycle, olie-reserve, en sinds
  LAR-414 **uranium-`military`** (`type:"military"`/`layer:"secondary"`/`showMilitary`, de militaire kringloop = down-blend/tails/reserves).
  `layer:"cb"`-flows + `type:"cb"`-nodes op
  `filters.showCentralBanks` (goud); `layer:"exchange"` + `type:"exchange"` op `filters.showExchangeStocks` (koper —
  beursvoorraden); sinds M8 `layer:"recycle"` op `filters.showRecycle` (REE — recycling); sinds M11 `layer:"reserve"` +
  `type:"reserve"` op `filters.showReserves` (olie — strategische voorraden/SPR). Alle default uit, in
  `flows.js`/`markers.js`/`main.js` + `ui.js`-chip + `config.js`-marker; de chip verschijnt alleen als een actieve grondstof
  die data heeft. **Nuance bij recycling (M8):** de node-gate zit op `node.layer==="recycle"` (niet op `type==="recycler"`)
  en `hasRecycle()` detecteert op `f.layer==="recycle"` — zo blijft **koper's always-on recycling** (recyclers zónder `layer`)
  ongemoeid en krijgt alleen REE de toggle/chip. De **olie-reserve-laag (M11)** volgt daarentegen exact het `exchange`-patroon
  (eigen `type:"reserve"`, `hasReserves()` op `n.type==="reserve"`) — een dedicated type dat geen andere grondstof gebruikt.
  Kopieer de vier filterplekken + config + ui-chip + marker-vorm voor elke nieuwe laag.
- **Marker-types:** `mine`/`refinery`/`port`/`market` + (M6) `airport`/`hub`/`cb`/`recycler` + (M7) `exchange`
  (koperkleurige CylinderGeometry-spoel, grootte ∝ √`stock`) + (M11) `reserve` (olie-amber tank-cilinder, grootte ∝ √`stock`) in `markers.js`.
- **Single-file build:** `build-standalone.py` genereert `atlas-standalone.html` uit `index.html` (lijnt CSS +
  lokale scripts inline, houdt three.js-CDN extern). Modulair = bron van waarheid; draai het script na wijzigingen.

## Aanpak per grondstof (het sjabloon)

1. **Ontwerp eerst** (op papier/in de sessie): de belangrijkste knopen (mijnen, havens, raffinaderijen,
   fabrieken) en de stromen ertussen, met operators, capaciteiten, transportmodi.
2. **Dan implementeren** in `data/<grondstof>.js` volgens het **lithium-schema** (`data/lithium.js` =
   referentie: 34 knopen, 31 stromen, NL-annotaties, verhaallijn incl. Chinese-raffinage-afhankelijkheid).
3. Registreren in `data/_registry.js`.

**Brief-template:** gebruik `design/_brief-template.md` als vast invulschema voor stap 1 — kopieer naar
`data/<grondstof>.md` en vul alle nodes/stromen in vóór je de `.js` schrijft. De template sluit 1-op-1 aan
op het node/flow-schema (`lithium.md` = het volledig ingevulde voorbeeld).

## Detailniveaus

- **Volledig:** lithium (template), kobalt, **goud** (M6 — 73 nodes/48 flows, luchtroutes + CB-laag),
  **koper** (M7 — 69 nodes/50 flows, China-smelttrechter + Copperbelt-kathode over land + beursvoorraden-laag),
  **uranium** (M9 — 38 nodes/36 flows, 4-staps kernbrandstofketen met verrijking als flessenhals + Trans-Kaspische route + VVER-lock-in + CANDU-uitzondering),
  **zeldzame aardmetalen** (M8 — 41 nodes/38 flows, magneet-REE NdPr+Dy/Tb: Ganzhou-scheidingstrechter + Dy/Tb-landstroom Myanmar→China over `grens-ruili` + Mountain-Pass-rondreis + NdFeB-waaier + recycling-toggle),
  **nikkel** (M10 — 50 nodes/46 flows, Indonesië-onshoring-trechter: mijn+raffinage in tien jaar via de exportban + class-1/class-2-splitsing + prijscrash-shakeout + LME-nuance; beursvoorraden-toggle hergebruikt met 0 engine-wijziging),
  **olie** (M11 — 45 nodes/46 flows, het knelpunten-netwerk dat tegelijk oplicht: Hormuz #1 + Malakka + Suez/Bab + Bosporus + Panama + Kaap; géén nieuw chokepoint = eigen aha; Hormuz-bypass-pijpleidingen + Rusland-omleiding 2022→ + VS-schalie-ommekeer; 3 stages erts/raffinaat/petrochemie),
  **zilver** (M13 — 42 nodes/37 flows, de **eerste écht nieuwe grondstof**: géén winnings-trechter — ~70-75% bijproduct van zink/lood/koper/goud (aanbod inelastisch) — terwijl de concentratie downstream zit (Chinese zonnepanelen/PV) → structureel tekort dat de kluisvoorraden (LBMA/COMEX/SGE) aftapt; schip+land, géén nieuw chokepoint; exchange-toggle hergebruikt met 0 engine-wijziging),
  **PGM** (M12 — 38 nodes/41 flows, de scherpste twee-landen/twee-metalen-concentratie: Zuid-Afrika/Bushveld = Pt/Rh + Rusland/Norilsk = Pd; **luchtvracht** (hergebruik goud-air-mode, JNB-gateway) — concentraat/matte over land; géén nieuw chokepoint; recycling-toggle hergebruikt van REE met 0 engine-wijziging; 6 tensions incl. autokat-leiband + Pt↔Pd-substitutie, rodium-spof, waterstof-hedge, Eskom-stroomcrisis),
  **grafiet** (M14 — 31 nodes/26 flows, een REE-achtige **verwerkingstrechter met TWEE feedstocks**: natuurlijk vlokgrafiet + synthetische naaldcokes convergeren op de anode-verwerking die ~90%+ in China zit (Shandong natuurlijk, Binnen-Mongolië synthetisch); zelfs ex-China vlok vaart naar China; dec-2023 China-exportvergunningen; dunne ex-China buildout Syrah Vidalia/Talga/Novonix/NMG/POSCO; schip+land, géén nieuw chokepoint (4e na nikkel/olie/zilver); recycling-toggle hergebruikt REE/PGM-patroon met 0 engine-wijziging, bewust bescheiden),
  **diamant** (M16 — 25 nodes/35 flows, de **scherpste downstream-trechter**: winning verspreid maar ~90-95% geslepen in **één stad (Surat)**; Antwerpen = G7-certificeringsknooppunt met Alrosa-herrouting via Dubai/India; De Beers/Alrosa-duopolie + lab-grown-ontwrichting + waarde-vs-volume; diamant **vliegt** = hergebruik goud/PGM air-mode, 0 engine-wijziging, géén nieuw chokepoint/marker-types; lab-grown-toggle bewust apart in backlog LAR-471),
  **gas** (M15 — 42 nodes/51 flows, aardgas/LNG: **gas is nauwelijks te verplaatsen** → twee gescheiden leversystemen (captive **pijpleiding**-arcs Rusland↔EU/Power of Siberia/Turkmenistan/Noorwegen náást heldere **LNG-oceaan**-arcs), met de **liquefactie-stap als trechter** (VS-Golfkust/Qatar/Australië); Qatar via Hormuz (géén bypass, scherper dan olie); Europa-pivot 2022 + Russische oost-pivot + drie prijszones + Panama-LNG-knelpunt; Iran = reserves≠export; schip+pipeline, géén nieuw chokepoint/render-modus/marker-types; opslag-laag hergebruikt de olie-`reserve`-toggle met 0 engine-wijziging).
- Ook nieuw op "uitgewerkt": **kolen** (M17) uit een parallelle sessie → de atlas telt nu **14 grondstoffen** (basis-10 + zilver + gas + diamant + kolen).
- **Basis:** — **geen** meer. Alle basis-10-grondstoffen staan op "uitgewerkt"; de nieuwe grondstoffen (zilver/gas/diamant/kolen) zijn losse toevoegingen.
- **Volgende kandidaat:** géén basis-grondstof meer. Verder grondstof-werk = alleen nog een *nieuwe 12e+* grondstof (nieuw bestand + script-tag + build-check, zoals zilver).

## Nu (2026-07-15 — M14 · Grafiet uitgevoerd — atlas inhoudelijk COMPLEET)

- **Grafiet volledig gebouwd + geverifieerd — het laatste basis-10-bestand.** `data/graphite.js` van "basis" (10/3) →
  **uitgewerkt** (31 nodes / 26 flows / 6 tensions) + brief `design/grafiet.md` + 5 grafiet-checks in `build-standalone.py`.
  Na M14 staat **geen enkele grondstof meer op "basis"** — alle 11 zijn uitgewerkt.
- **De vorm = een REE-achtige verwerkingstrechter met TWEE feedstocks.** Grafiet is HET anodemateriaal in Li-ionbatterijen
  (~1 kg/kWh). **Natuurlijk vlokgrafiet** (China #1, Balama/Mozambique, Madagascar, Brazilië, Tanzania, +Europa/Sri Lanka) én
  **synthetisch grafiet** (uit petroleum-**naaldcokes**, gegrafitiseerd bij ~3000 °C) convergeren op de anode-verwerking die
  **~90%+ in China** zit (Shandong natuurlijk, Binnen-Mongolië synthetisch). **Zelfs ex-China vlok vaart naar China.** Levende
  geopolitiek: de **China-exportvergunningen op grafiet (dec 2023)**. Dunne ex-China buildout: Syrah Vidalia (Louisiana, uit
  Balama-vlok, IRA-FEOC) + Talga/Novonix/NMG/POSCO.
- **Schip+land, géén nieuwe render-modus, géén nieuw chokepoint** (4e na nikkel/olie/zilver). **Recycling-toggle**
  (`layer:"recycle"`, default uit) = hergebruik van het REE/PGM-patroon met **0 engine-wijziging**, bewust bescheiden
  (batterijgrafiet-recycling nog nascent).
- **Verificatie (headless, poort 8735 — eigen `-4`-server):** grafiet **77 legs (57 zee + 20 land) / 0 kapot / 0 straight /
  0 warnings**; toggle aan = 80 legs (+3 recycle); regressie schoon (0 kapot over álle grondstoffen). Route-bug gefixt
  (`gr-ref-japan→gr-mkt-korea-japan` road→ship). Browser-pane cachete de oude data hardnekkig → verse schijf-data via synchrone
  fetch + `REGISTER`-capture geverifieerd. `atlas-standalone.html` geregenereerd (5 grafiet-checks OK). **Code-commit `34b1ed4`**,
  **gepusht** naar GitHub → live op Pages. **Linear M14 · LAR-449..454** (449–453 Done, 454 In Progress).
- **Repo-correctie:** de repo is **niet** lokaal-only — hij staat op GitHub (`larswalters/grondstoffen-atlas`) en draait live op
  **GitHub Pages** (https://larswalters.github.io/grondstoffen-atlas/); elke `git push origin main` deployt. De "lokaal-only"-
  notities in oudere milestones zijn achterhaald.
- **Rest:** alleen visuele bevestiging op de live URL (LAR-454, Lars). **Geen grondstoffen meer op "basis".**

## Eerder (2026-07-15 — M13 · Zilver uitgevoerd)

- **Zilver volledig gebouwd + geverifieerd — de eerste écht nieuwe grondstof.** Anders dan M6–M12 (die een bestaand
  "basis"-bestand naar "uitgewerkt" brachten) bestond zilver nog niet: nieuw `data/silver.js` (42 nodes / 37 flows /
  6 tensions) + brief `design/zilver.md` + `<script src="data/silver.js">` in `index.html` + 5 zilver-checks in
  `build-standalone.py`. De vorm is **fundamenteel anders**: **géén winnings-trechter** — ~70-75% is **bijproduct** van
  zink/lood/koper/goud (aanbod inelastisch; mijn-nodes = eigenlijk andermans mijnen), terwijl de concentratie **downstream
  aan de vraagkant** zit: de energietransitie trekt zilver naar de **Chinese zonnepanelen-industrie** (PV = grootste + snelst
  groeiende toepassing) → een **structureel tekort** dat de kluisvoorraden (LBMA/COMEX/SGE) aftapt.
- **Schip+land, géén nieuwe render-modus, géén nieuw chokepoint** (derde na nikkel/olie op de bestaande routekaart). Keten
  op de 3 stages: erts=mijn(bijproduct)→doré/concentraat → raffinaat=good-delivery baar → product=industrieel (solar/
  elektronica/sieraad). Mexico als winning+raffinage-anker (Fresnillo + Peñoles/Torreón). **Kluis-/beursvoorraden-laag** =
  hergebruik van de bestaande exchange-toggle met **0 engine-wijziging** (nikkel-patroon, 2e datagedreven hergebruik):
  3 exchange-nodes (LBMA/COMEX/SGE) + 3 `layer:"exchange"`-aftap-flows; recycling always-on.
- **Verificatie (headless, poort 8734 — eigen server naast de parallelle uranium-toggle-sessie):** zilver **85 legs / 0 kapot /
  0 straight / 0 warnings**; regressie schoon (andere uitgewerkte grondstoffen 0/0). 2 route-bugs empirisch gefixt (VS-raffinage
  Tacoma→Astoria; China-solar Suzhou→Jiangsu-kust). Exchange-chip "beursvoorraden" + blurb + 6 tensions renderen.
  `atlas-standalone.html` geregenereerd (5 zilver-checks OK). **Code-commit `e091848`** (repo lokaal-only, Claude-trailer;
  alléén eigen bestanden gestaged — de parallelle sessie's engine-files ongemoeid, sectie J). **Linear M13 · LAR-434..438 Done, 439 In Progress.**
- **Rest:** **visuele bevestiging op Netlify/mobiel** (WebGL-screenshot lukt niet headless — LAR-439, Lars).
- **Volgende grondstof:** grafiet (het laatste van de basis-10; PGM/M12 loopt parallel) — zelfde brief→bouw-flow.

## Eerder (2026-07-15 — M11 · Olie uitgevoerd)

- **Olie volledig gebouwd + geverifieerd.** `data/oil.js` van "basis" (18/15) → **uitgewerkt** (45 nodes / 46 flows /
  6 tensions) + brief `design/olie.md`. Olie's "aha" is bewust **anders dan alle eerdere**: geen enkele trechter maar het
  **hele knelpunten-netwerk dat tegelijk oplicht** — Hormuz #1 (15 stromen), Malakka, Taiwan, Suez/Bab, Bosporus, Panama,
  Kaap. Daarom **géén nieuw chokepoint** (olie hergebruikt het volledige bestaande net = het eigen aha); wel 3 olie-only
  navigatie-vaarpunten (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`) in `_chokepoints.js`.
- **Drie levende verhalen bovenop de straten:** de **Hormuz-bypass-pijpleidingen** (Saoedi Oost-West → Yanbu; UAE Habshan →
  Fujairah, `mode:"pipeline"`), de **Rusland-omleiding 2022→** (Europese crude → India/China via Primorsk/Novorossiysk/
  ESPO-Kozmino/Druzhba), en de **Amerikaanse schalie-ommekeer** (Corpus Christi → Atlantische Oceaan). Keten op 3 stages:
  erts=ruwe olie (knelpunten-verhaal) → raffinaat=producten (diesel/benzine) → product=petrochemie (nafta→kraker→kunststof).
  Schip+pijpleiding, **géén nieuwe render-modus**. Kust-raffinaderijen `coastal:true`.
- **Verificatie (headless, poort 8734 — eigen server naast de parallelle nikkel-sessie):** olie **210 legs / 0 kapot /
  0 straight**; regressie schoon (globale baseline 5 = lithium 4 + goud 1, olie voegt 0 toe). `atlas-standalone.html`
  geregenereerd (4 olie-checks OK) + zelf geverifieerd (210/0/0). **Code-commit `1d4ece5`** (repo lokaal-only, Claude-trailer;
  alleen eigen bestanden gestaged). **Linear M11 · LAR-428..433 (4 Done, 432 Backlog, 433 In Progress).**
- **Toegevoegd (na de nikkel-sessie):** de optionele **SPR-voorraden-toggle** (`layer:"reserve"`, LAR-432 **Done**, commit
  `86c8c1f`) — gebouwd zodra de engine-bestanden vrij waren. Het **vierde** optionele-laag-patroon (goud-CB/koper-beurs/
  REE-recycling/olie-reserve), exact het koper-`exchange`-patroon + olie-amber tank-marker. 5 SPR-nodes (US Gulf/China Dalian/
  Japan Kiire/India Mangalore/IEA-EU Le Havre, `stock` in mln vaten) + 5 vul-flows + tension `oil-t-spr`. Headless: olie 232 legs
  / 0 kapot / 0 straight; toggle uit=45/46, aan=50/51; chip "voorraden" alleen bij olie; regressievrij. **Olie is nu volledig
  compleet** (data + optionele laag), gelijk aan goud/koper/REE.
- **Rest:** **visuele bevestiging op Netlify/mobiel** (WebGL-screenshot lukt niet headless — LAR-433, Lars).
- **Volgende grondstof:** grafiet, PGM — zelfde brief→bouw-flow.

## Eerder (2026-07-15 — M10 · Nikkel uitgevoerd)

- **Nikkel volledig gebouwd + geverifieerd.** `data/nickel.js` van "basis" (13/4) → **uitgewerkt** (50 nodes / 46 flows /
  6 tensions) + brief `design/nikkel.md`. De nikkel-"aha": de **trechter staat op z'n kop** t.o.v. koper — **Indonesië heeft
  in tien jaar de mijn ÉN de raffinage** naar zich toe getrokken via de **exportban op ruw erts** (IMIP Morowali / IWIP Weda
  Bay, Chinees kapitaal Tsingshan/Huayou); het erts blíjft in het land (korte mijn→smelter-hops), pas als NPI/matte/MHP de
  zee op. Plus **twee nikkels** (class-1 batterij/sulfaat vs class-2 roestvrij/NPI, HPAL→MHP/matte als brug), de **prijscrash-
  shakeout** (BHP Nickel West stilgelegd 2024, Nieuw-Caledonië in crisis), de **LME-nuance** (alleen class-1 leverbaar + de
  2022-squeeze) en het **Filipijnse ruw-erts-contrast** (geen ban).
- **Schip+land, géén nieuwe render-modus, géén nieuw chokepoint** (tweede grondstof na koper die volledig op de bestaande
  routekaart draait: Makassar/Lombok/SCS/Taiwan/Deense-Straten/Panama/Saint-Laurent). **Beursvoorraden-laag (LME)** hergebruikt
  de bestaande exchange-toggle van koper met **0 engine-wijziging** (eerste keer dat een optionele laag puur via de data-laag
  wordt hergebruikt); recycling always-on (koper-patroon).
- **Verificatie (headless, poort 8733 — eigen server want een parallelle olie-sessie bezette 8732):** nikkel **91 legs
  (63 zee + 18 land + 10 korte hops) / 0 kapot / 0 straight**; regressie schoon (0 kapot over álle grondstoffen).
  `atlas-standalone.html` geregenereerd (nikkel-checks OK). **Code-commit `08aa4f5`** (repo lokaal-only, Claude-trailer).
  **Linear M10 · LAR-422..426 Done, 427 In Progress.**
- **Rest:** **visuele bevestiging op Netlify/mobiel** (WebGL-screenshot lukt niet headless — LAR-427, Lars).
- **Volgende grondstof:** grafiet, PGM (olie loopt in een parallelle sessie) — zelfde brief→bouw-flow.

### Eerder (2026-07-15 — M8 · Zeldzame aardmetalen uitgevoerd)

- **Zeldzame aardmetalen volledig gebouwd + geverifieerd.** `data/rare-earths.js` van "basis" (9/5) → **uitgewerkt**
  (41 nodes/38 flows/6 tensions), **magneet-REE-framing** (NdPr licht + Dy/Tb zwaar; `symbol: NdPr`, `unit: kt magneet-REO/jaar`).
  De extreemste trechter van de atlas: winning breed verspreid, **scheiding ~85–90% Zuid-China** (Ganzhou/Baotou/Sichuan).
  Vier kern-aha's renderen: Ganzhou-scheidingstrechter, **Dy/Tb-landstroom Myanmar→China** over de nieuwe grenscorridor
  **`grens-ruili`** (`_chokepoints.js`, Kasumbalesa-patroon), **Mountain-Pass-rondreis** (concentraat heen over de Stille
  Oceaan, oxide terug), **NdFeB-magneet-waaier** vanuit China. Plus het dunne Lynas-draadje (Mount Weld→Kuantan→Japan/EU).
  Nieuwe **recycling-toggle** (`layer:"recycle"`, default uit) = het derde optionele-laag-patroon.
- **Headless:** rare-earths **90 legs (39 land + 51 zee) / 0 kapot / 0 straight**; regressievrij (5 kapot = bekende
  lithium/goud-baseline). `atlas-standalone.html` geregenereerd (REE-checks OK). **Linear M8 · LAR-416..420 Done, 421 In Progress.**
- **Rest:** **visuele bevestiging op Netlify/mobiel** (WebGL-screenshot lukt niet headless — LAR-421, Lars).
- **Ook open (uranium, M9):** alleen nog de visuele bevestiging (LAR-415, Lars). De militaire-kringloop-toggle (LAR-414) is nu **Done** (commit `6a6d062`, 5e optionele laag `type:"military"`/`layer:"secondary"`; headless 60 legs/0 kapot/0 straight).
- **Volgende grondstof:** nikkel (runner-up), grafiet, PGM, olie — volgens dezelfde brief→bouw-flow.
