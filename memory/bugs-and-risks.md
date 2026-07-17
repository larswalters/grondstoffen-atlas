# Bugs & risks — Grondstoffen Atlas
*Last updated: 2026-07-17 (pilot-test: curve-sampling-bug gefixt; Japan-observatie open)*

## 🔍 OPEN — Lars ziet trans-Pacific bundel over Japan (mobiel, 2026-07-17 03:15)
- **Symptoom:** screenshot toont de koper-bundel dwars over Honshu richting Korea-straat/China.
- **Hypothese: stale cache** — de curve-fix (`3c801a0`) ging pas minuten vóór de screenshot live; Pages CDN
  cachet 10 min + mobiele browsercache. De curve-verificatie (getekende curve → Natural Earth) zegt dat álle 22
  corridors op water blijven, inclusief het Japan-gebied (route hoort door Tsugaru/Japanse Zee).
- **Morgen:** incognito/verse cache; nog fout → Tsugaru-passage per corridor plotten (`plot_corridors.js` scratchpad).

## ✅ GEFIXT (2026-07-17) — curve-bemonstering sloeg invoerpunten over (`util.js`)
- `makeRouteCurve` bemonsterde uniform (cap 260 = 1 punt/~75 km op trans-Pacific) → de dichte kustpunten van
  MARNET-paden werden overgeslagen → CatmullRom-spline sneed over schiereilanden (Vogelkop), óók toen de data al
  gerepareerd was. Oude A\* maskeerde dit met ~130 km geforceerd water. **Fix: adaptieve bemonstering, elk
  invoerpunt behouden.** Les: **verifieer op de gétekende curve, niet alleen op de polyline-data.**

## ✅ GEFIXT (2026-07-17) — ruwe MARNET-paden: zigzags + landkruisingen (baker)
- Yangtze-monding 140°+105° binnen 50 km (de "rare draai"); Vogelkop-segment 399 km over land; Isla Guadalupe.
- Fix in `tools/bake_searoutes.py`: de-zigzag (alleen als kortsluiting over water) + lokale A\*-omleiding
  (0,1° waterraster, kustbuffer 1 cel) + kanaal-uitzondering Panama/Suez. Checker: `tools/check_corridors.js`.
- Restant (bewust geaccepteerd): haven-uitvaart-bochtjes op punt 1 (110–160°, tientallen km, onder de marker).

## ⚠️ RISICO — GitHub-egress flaky op deze machine (2026-07-17)
- `git push`/`gh`/`curl` naar github.com vallen periodiek weg (Recv failure/TLS timeout), minuten later weer OK.
- Workaround die werkt: **achtergrond-retry-loop** (1 poging/min, max 30) — alle 3 deploys kwamen zo door.

## ✅ GEFIXT (2026-07-17) — LAR-479 tegel-patch werd afgekapt bij inzoomen · commit `297016f`, bevestigd door Lars
- **Symptoom (Lars):** *"het bovenste gedeelte scherp en de onderste wazig … die grens van wazig en scherp beweegt
  mee als ik de wereldbol draai, alsof je echt een sweet spot moet hebben."*
- **Twee samenwerkende oorzaken** (de vorige sessie vond er één; de tweede kwam er bij het fixen bij):
  1. **Budget < één patch.** `updateDetail` vulde rij voor rij van **noord naar zuid** met `budget--` per tegel,
     terwijl een normale patch **42–72** tegels vraagt en `maxTiles` op **40** stond → de zuidelijke rijen kregen
     structureel niets → alleen de shell (`shellMaxZ: 3`, ~20 km/px). De grens bewoog mee omdat de bbox elke update
     rond `viewCentre()` wordt gelegd. **Er was dus geen sweet spot** — je zat altijd in de bug en zag alleen de
     bovenkant ervan. *(De eerdere "camZ 4,0/5,6/6,5 zijn gekapt, de rest niet"-analyse was te optimistisch: door
     oorzaak 2 is vrijwel élke view gekapt.)*
  2. **`detailZoomFor()` miste `cos(lat)`.** Een Mercator-tegel op 60° breedte beslaat de helft van de grond van
     eentje op de evenaar → hoe noordelijker, hoe méér tegels voor dezelfde scherpte. Verspild werk dat het budget
     extra opblies; daarom was Noorwegen **veel** erger dan China.
- **Fix:** `cos(lat)` in `detailZoomFor()` · `maxTiles` 40 → **96** · de patch vult **van het midden naar buiten**
  (sortering op afstand tot `viewCentre`) → het plafond is weer een noodrem i.p.v. een dagelijkse limiet, en bij een
  hit verdwijnen de **buitenste** tegels langs de bolrand i.p.v. de halve onderkant.
- **Bewijs (raycast-grid, 412×915, oude code echt teruggezet via `git stash` op een schone origin):**

  | view | oud (tegels · boven/onder) | nieuw |
  |---|---|---|
  | China camZ 3,6 | 40 (cap) · 100% / 100% | 42 · 100% / 100% |
  | maximale zoom | 40 (cap) · 100% / **50%** | 49 · 100% / 100% |
  | evenaar/Andes | 36 · 100% / 100% | 30 · 100% / 100% |
  | hoge breedte (Noorwegen) | 40 (cap) · **33% / 0%** | 36 · 100% / 100% |

  3 van de 4 oude views zitten **exact op de cap van 40**. Nieuw: 100%/100% op alle 7 views, piek 72 tegels.
- **`shellMaxZ: 3` bewust níét aangeraakt** — de shell is nu nergens meer zichtbaar in beeld, dus de oude
  LAR-394-afweging (meer tegels = zwaarder op mobiel) hoeft niet opnieuw gemaakt.

## 🐛 OPEN (Low) — een mislukte tegel wordt nooit opnieuw geprobeerd (`src/tiles.js`)
- Bijvangst van de LAR-479-analyse, **andere oorzaak, apart defect** — bewust níét meegefixt (scope).
- `ensureTile` doet `if (liveMap.has(id)) return;` en de error-callback alleen `console.warn` → de mesh blijft
  permanent op opacity 0 en herstelt nooit. Op trage/geknepen verbindingen (mobiel, Esri-throttling) een echte kwaal.
- **Nu iets relevanter geworden:** met `maxTiles: 96` kunnen er meer gelijktijdige requests uitstaan dan voorheen.
  Nog niet waargenomen in de praktijk (Lars' bevestiging was schoon), dus geen issue aangemaakt.

## ✅ GEFIXT (2026-07-17) — LAR-481 marker-LOD vuurde averechts · commit `8dda38e`, bevestigd door Lars
- **Symptoom (Lars):** de Norilsk-mijn verschijnt pas bij inzoomen.
- **Dit léék tier-by-design** (staat letterlijk zo in de kop-comment van `markers.js`), maar was het **omgekeerde**:
  `forced` (node hangt aan een zichtbare stroom, uit `usedNodeIds`) overrulet tier volledig, en dat gold voor
  **57 van de 63** koper-nodes; **nul** nodes waren tier 1 zónder stroom. De tier-regel raakte dus **alléén nog de
  6 context-mijnen zónder flows** — mijnen met een eigen smelter ter plekke (Chuquicamata/Calama, KGHM/Głogów,
  Norilsk binnenlands, Aitik, Julong, Cobre Panamá), zelfde klasse als Argyle/Nickel West/Iran.
- **De willekeur:** El Teniente (share 2,1 · tier 2 · stroom) altijd zichtbaar · Norilsk (2,0 · tier 2 · géén stroom)
  pop-in · Los Pelambres (1,6 · tier 2 · stroom) altijd zichtbaar · Chuquicamata (1,6 · tier 2 · géén stroom) pop-in.
  Identieke share, identieke tier, tegengesteld gedrag — zichtbaarheid hing af van of een mijn tóévallig een lijntje
  had. De LOD ontdubbelde niet; hij vuurde alleen op de nodes die dat het minst verdienden.
- **Fix (Lars koos uit 3 opties):** markers verdwijnen niet meer op tier; **`tier` stuurt alleen nog de labels**
  (`labelZoomByTier` + botsingsdetectie) — die houden de kaart werkelijk rustig, niet de bolletjes. `tierZoom`
  (config) + de `forced`/`usedNodeIds`-uitzondering **verwijderd**: het gevaar dat ze afdekten ("een lijn eindigt in
  het niets") kan niet meer optreden. NB-comment op beide plekken.
- **Geverifieerd:** markers-per-zoomstand constant (z 8,0→2,75) · labels blijven gefaseerd (0 → 12 @ z=4 → 29 @
  z=2,75) · **regressie 14 grondstoffen: totale pop-in 0**.
- **Kosten:** uitgezoomd 6 extra bolletjes bij koper. Als dat te druk blijkt → stromen ook tieren, **ná M18**
  (raakt `flows.js` = de pilot-code).

## ✅ GEFIXT (2026-07-17) — draaien was zoom-onafhankelijk (`src/globe-core.js`) · commit `297016f`
- **Symptoom (Lars):** *"als je een stuk bent ingezoomd dan is het draaien super gevoelig."*
- **Oorzaak:** `rotation.y += dx * 0.005` = een vaste hoeveelheid radialen per pixel, ongeacht zoom. Op `minZoom`
  (2,75) zie je ~9× minder wereld, maar draaide een veeg evenveel graden.
- **Fix:** schaalt met de afstand camera→oppervlak (`dragSpeed` + `dragRefZoom` in config), **bewust geankerd op de
  standaardzoom** — Lars klaagde alleen over ingezoomd, en de fysisch "correcte" 1:1-grab zou de standaardzoom 4,4×
  trager maken. Gemeten: 28,65°/100px @ standaard (identiek aan oud) · 3,13° @ volle zoom · ratio **0,109** = exact
  de ratio zichtbare wereld.

## ⚠️ Route-engine: aantoonbaar onrealistisch (2026-07-17) → M18
- **`openRadiusDeg: 1.2`** = ~130 km geforceerd water rond élk knelpunt → A\* vaart dwars over land/eilandjes.
  Hoofdboosdoener achter *"een boot zou daar nooit zo varen"*.
- **8-richtingen-A\*** → trapjes (Golf→Rotterdam = 33 richtingswissels). **Grof raster + gretige heuristiek + géén
  echte vaarlanen** → kaarsrechte runs langs een breedtegraad/meridiaan.
- **`wp-pac-zuid` dwingt een omweg van ~1.090 km af** (Antofagasta→Shanghai +8% vs. grote-cirkel; searoute +2%).
  De `via`-ketens zijn grotendeels handmatige compensatie voor een slechte router.
- **Risico bij M18:** de **vaarbanen-waaier** (`laneShape`, `util.js`) die bij een knelpunt samenknijpt is een
  kernbeeld — die moet ook op gebakken polylines nog kloppen. Subtielste regressie-val. Verder: uranium's Kaspische
  oversteek (ingesloten zee) heeft searoute's netwerk waarschijnlijk niet → expliciet checken.
- **Verificatie-val (kostte de vorige pilot z'n geldigheid):** vergelijk nooit tegen een kale origin→dest A\*-run;
  de atlas routeert altijd langs de `via`-keten.

## M17 · Kolen — geverifieerd headless (2026-07-16)
- Volledig gebouwd + geverifieerd (eigen server poort 8735 = `grondstoffen-atlas-4`): **kolen 111 legs / 0 kapot /
  0 straight / 0 degen / 0 unresolved via** (34 nodes / 33 flows / 6 tensions). Regressie schoon: alle
  op dat moment geladen grondstoffen (12 tijdens de test) op hun bekende baseline; kolen voegt 0 kapot/straight/degen toe.
- **1 route-bug onderweg gevonden + gefixt (zilver-Tacoma→Astoria-echo):** de 2 kapotte legs zaten op `coal-port-vancouver
  → wp-pac-noord`. Empirisch gediagnosticeerd door kandidaat-coördinaten door `Routing.sea` te halen: **Roberts Bank /
  Westshore ligt ingesloten in de Salish Sea** (achter Vancouver Island) en valt dicht in het grove 0,25°-raster
  (robertsbank→open zee = `null`). Verplaatst naar **Ridley Terminal / Prince Rupert** (open kust) — dat is bovendien
  feitelijk dé Canadese cokeskool-exporthaven. Daarna 0 kapot. **Les (herbevestigd):** ingesloten binnenzeeën (Salish Sea,
  Puget Sound, Bohai) sluiten in het grove raster; test een haven-coördinaat door de router vóór je hem vastzet, en kies
  een open-kust-terminal.
- **Risico (parallel werk, sectie J):** deze sessie draaide náást **3** andere (grafiet mid-wrapup, diamant, gas). De
  gedeelde `index.html` kreeg drie script-regels (diamond/coal/gas) in één hunk → alléén de coal-regel gestaged via een
  gerichte `git apply --cached`-patch. `atlas-standalone.html` (gitignored) bevatte tijdens de build ook diamant/gas-data;
  geen probleem want het is een lokaal artefact. **Blijf bij nieuwe grondstoffen selectief stagen (nooit `git add -A`).**

## M14 · Grafiet — geverifieerd headless (2026-07-15)
- Volledig gebouwd + geverifieerd (eigen server poort 8735, `grondstoffen-atlas-4` toegevoegd aan `launch.json`):
  **grafiet 77 legs (57 zee + 20 land) / 0 kapot / 0 straight / 0 warnings** (31 nodes / 26 flows / 6 tensions);
  toggle aan (recycling) = **80 legs** (+3 recycle-flows). Regressie schoon: **0 kapot over álle grondstoffen**.
- **Browser-pane-cache-gotcha (nieuw, belangrijk):** de Browser-pane cachete de oude `graphite.js` (basis 10/3)
  hardnekkig — óók na `location.reload(true)` bleef `getResource('graphite')` de oude data tonen. Dit is een
  **pane-cache, geen codeprobleem**. Workaround die werkte: de verse schijf-data via **synchrone XHR** (`?ts=`-buster)
  ophalen, `window.REGISTER` tijdelijk shadowen om het resource-object te capturen, en de leg-check dáárop draaien
  (repliceert exact de `flows.js`-leglogica: `Routing.sea`/`Routing.land`, `isSeaPoint`, gathering-legs). Voor de
  live render: het verse resource in `RESOURCES` splicen + de grafiet-pill klikken (ATLAS re-render). **Les:** vertrouw
  headless niet op een gewone reload voor verse data-files; fetch+capture of splice-in.
- **1 route-bug onderweg gevonden + gefixt:** `gr-ref-japan → gr-mkt-korea-japan` stond op `mode:"road"`, maar Japan→Korea
  gaat over zee (Straat van Korea) → de landrouter vond geen pad (kapot). Beide punten zijn `coastal` → mode veranderd naar
  `ship` (directe korte zee-hop, géén via). Daarna 0 kapot. **Les (herbevestigd, koper/PGM-echo):** een `road`/`rail`-flow
  tussen twee landen gescheiden door zee is onmogelijk; zulke hops moeten `ship` zijn (beide endpoints `coastal`/`port`).
- **Recycling-toggle hergebruikt met 0 engine-wijziging** (REE/PGM-patroon, 3e datagedreven hergebruik van dít patroon):
  de "recycling"-chip verschijnt automatisch voor grafiet omdat het `layer:"recycle"`-nodes/-flows heeft; toggle uit=23 flows
  (77 legs), aan=26 flows (80 legs). Blurb + 6 tensions renderen, geen console-warnings (geen onbekende via-/node-ids).
- **Co-locatie bewaakt:** grafiet-eigen nodes ~30-45 km uit elkaar gehouden (gr-ref-korea vs gr-mkt-korea-japan ~58 km;
  gr-ref-shandong vs gr-nc-china) → 0 `degDist:0`-arcs (0 degenerate in de check).
- ⚠️ **Visuele bevestiging blijft open (LAR-454)** — WebGL-screenshot lukt niet headless (timeout, zelfde gat als M5–M13).
  Nu triviaal via de live URL: de twee feedstock-stromen die op China convergeren, het Balama→Vidalia-draadje rond de Kaap,
  de ex-China buildout-waaier, de recycling-toggle.
- ✅ **Concurrency (sectie J) schoon:** werktree schoon bij start én vóór commit; grafiet raakt de engine niet
  (0 engine-wijziging) → alléén eigen bestanden gestaged. **Repo-correctie:** de docs zeiden "lokaal-only", maar de repo
  is sinds M13 live op GitHub Pages → deze sessie **wél gepusht** (code + docs).

## M13 · Zilver — geverifieerd headless (2026-07-15)
- Volledig gebouwd + geverifieerd in de draaiende atlas (eigen server poort 8734): **zilver 85 legs / 0 kapot /
  0 straight / 0 warnings** (42 nodes / 37 flows / 6 tensions). Legs-check repliceert exact de `flows.js`-leglogica
  (`Routing.sea`/`Routing.land`, `isSeaPoint`, gathering-legs). Regressie schoon: de andere uitgewerkte grondstoffen
  (kobalt/koper/nikkel/REE/uranium/goud) allemaal 0/0; de bekende baseline (lithium 4× same-cell + grafiet/PGM op "basis")
  ongewijzigd — zilver voegt **0** toe.
- **2 route-bugs onderweg gevonden + gefixt** (empirisch getest vóór de fix, niet gegokt — kandidaat-coördinaten door
  `Routing.sea` gehaald): (1) **VS-raffinage Tacoma → Astoria/Columbia-monding** (47.25/-122.44 → 46.20/-123.90): Puget
  Sound valt in het grove 0,25°-raster dicht → Greens Creek→Tacoma per zee onbereikbaar (0 legs); open Pacific-kust wél (20).
  (2) **China-solar Suzhou-binnenland → Jiangsu-kust Nantong** (31.30/120.60 → 32.00/121.60): het binnenland is per zee
  onbereikbaar → de 2 ship-flows ernaartoe braken; de kustpositie routeert wél (de grote rail-flows werkten al). **Les/risico
  (herbevestigd):** elke ship-endpoint moet op een echt zee-cel liggen; diep-in-baai-steden (Puget Sound) en landinwaartse
  clusters (Jiangsu-solar) falen in het grove raster → verplaats naar de open kust of route via een haven.
- **Exchange-toggle hergebruikt met 0 engine-wijziging** (nikkel-patroon, nu 2e datagedreven hergebruik): de "beursvoorraden"-chip
  verschijnt automatisch voor zilver omdat het exchange-nodes/-flows heeft; toggle uit=34 flows, aan=37; blurb + 6 tensions renderen.
  Geen console-warnings (geen onbekende via-/node-ids).
- **Co-locatie bewaakt:** zilver-eigen nodes rond Shanghai (ref-china/SGE/solar) en Mumbai (markt/haven/recycler) staan ≥1 rastercel
  uit elkaar → geen `degDist:0`-arc.
- ⚠️ **Visuele bevestiging blijft open (LAR-439)** — WebGL-screenshot lukt niet headless (timeout, zelfde gat als M5–M11).
  Op Netlify/mobiel door Lars: de diffuse by-product-mijn-origin (geen winnings-trechter), de convergentie op Peñoles/KGHM/Korea/China,
  de dikke solar-boog SGE→Jiangsu, de India-sieradenstroom, en de kluis-toggle (LBMA/COMEX/SGE) die de aftap toont.
- ⚠️ **Concurrency (sectie J):** een parallelle sessie werkte tegelijk aan uranium's engine-laag op de gedeelde bestanden
  (`config.js`, `src/{flows,main,markers,ui}.js`, `data/uranium.js`, dirty). Zilver raakt de engine niet (0 engine-wijziging) →
  alléén de eigen bestanden gestaged (`data/silver.js` + `design/zilver.md` + `index.html` + `build-standalone.py`); nooit `git add -A`.

## M8 · Zeldzame aardmetalen — geverifieerd headless (2026-07-15)
- Volledig gebouwd + geverifieerd in de draaiende atlas (poort 8732): **rare-earths 90 legs (39 land + 51 zee) / 0 kapot /
  0 straight**. Structuurcheck groen: 41 nodes / 38 flows / 6 tensions, geen dubbele ids, geen onbekende flow-endpoints,
  `grens-ruili` resolvet in de tension. Regressie schoon: globaal 5 kapot = de bekende `degDist:0` lithium(4)+goud(1)-baseline
  (**0 nieuw**); 25 straight = de basis-grondstoffen (nikkel/grafiet/PGM/olie, ongewijzigd).
- **Onderweg gevangen (niet echt kapot):** 5 legs waren aanvankelijk `degDist:0` same-city hops (ref/magneet/recycler in
  dezelfde rastercel: Baotou/Ganzhou/MP/La Rochelle/Fort Worth). Opgelost door die 5 tweede-nodes ~30–45 km binnen dezelfde
  stad te verschuiven → zichtbare korte landroute + teller schoon op 0. **Les/risico:** twee nodes van dezelfde grondstof
  binnen één 0,25°-cel geven een onzichtbare arc; hou co-located functies (scheiding+magneet) minstens een cel uit elkaar.
- **Recycling-toggle** (`layer:"recycle"`) getest: aan → +3 recycle-flows + 3 recycler-nodes; uit → weg; de 4e (MP-recycling,
  `status:"project"`) is extra project-gated (verschijnt alleen met recycling ÉN projecten aan — correct gedrag). cb/beurs-chips
  blijven correct weg bij REE. **Risico-nul t.o.v. koper:** de node-gate op `node.layer==="recycle"` (niet op `type==="recycler"`)
  laat koper's always-on recyclers ongemoeid — geverifieerd dat koper's legs/markers ongewijzigd zijn.
- ⚠️ **Visuele bevestiging blijft open (LAR-421)** — WebGL-canvas laat zich niet volledig headless screenshotten (zelfde gat
  als M5/M6/M7/M9). In de browser-pane wél zichtbaar bevestigd dat de Ganzhou-trechter (met knelpunt-ring), de Myanmar/Vietnam-
  landstromen, de NdFeB-waaier, de Mountain-Pass-Pacific-route en het EU-draadje via Suez renderen. Op Netlify/mobiel te checken
  door Lars: convergeren de scheidings-bogen echt op Zuid-China?, loopt de Dy/Tb-landstroom over Ruili?, is de rondreis VS↔China
  zichtbaar?, waaiert de NdFeB uit naar EV/wind/defensie?, lopen de scheeps-voyages voor REE?

## M9 · Uranium — geverifieerd headless (2026-07-15)
- Uranium volledig gebouwd + geverifieerd in de draaiende atlas (mijn eigen server poort 8743, want 8732 bezet door de
  M8-sessie): **uranium 54 legs / 0 kapot** (20 zee + 34 land, **0 straight** → de nieuwe Kaspische oversteek routeert écht
  over water, geen fallback). Regressie schoon: de 5 overige nulls zijn de bekende `degDist:0` same-city hops uit de
  M5/M6-baseline (lithium 4, goud 1), **niet nieuw**. Structuurcheck groen (geen onbekende node-/via-/tension-ids, geen duplicaten).
- **Nieuwe vaarpunten in `_chokepoints.js`** (`wp-kaspisch-n/-m/-z` + `wp-dardanellen`): alleen uranium verwijst ernaar via
  `via`, dus geen impact op de andere 9 grondstoffen (geverifieerd: hun leg-tellingen ongewijzigd). Risico bij een volgende
  ingesloten-zee-grondstof: dezelfde geforceerd-water-truc, let op contiguïteit (overlappende discs, zie de Saint-Laurent-keten).
- ⚠️ **Visuele bevestiging blijft open (LAR-415)** — WebGL-canvas laat zich niet headless screenshotten (zelfde gat als
  M5/M6). Op Netlify/mobiel te checken: verrijkings-flessenhals (dun ringetje nodes, Rusland dikst)?, de twee Kazachstan-
  routes (Rusland-transit vs. Trans-Kaspische omweg)?, de VVER-lock-in-lijn naar Midden-Europa?, de CANDU-uitzondering?,
  scheeps-voyages voor uranium?
- ✅ **Militaire-kringloop-toggle GEBOUWD (LAR-414 Done, 2026-07-15, commit `6a6d062`)** — de uitgestelde engine-laag afgemaakt
  zodra de gedeelde bestanden schoon waren; het vijfde optionele-laag-patroon (`type:"military"`/`layer:"secondary"`). Headless
  geverifieerd (uranium 60 legs / 0 kapot / 0 straight; toggle +4 nodes/+5 flows; chip alleen bij uranium). Niet meer openstaand.

## M7 · Koper — geverifieerd headless (2026-07-14)
- Koper volledig gebouwd + geverifieerd in de draaiende atlas (poort 8742): **koper 145 zee/land-legs, 0 kapot**;
  regressie **388 legs / 0 kapot** over alle 10 grondstoffen; beursvoorraden-toggle +6 nodes/+7 flows, chip
  "beursvoorraden" verschijnt (CB-chip niet — correct); geen console-errors. Structurele Node-check ook groen
  (geen onbekende ids/via-punten/duplicaten/coördinaatfouten).
- **4 route-bugs onderweg gevonden + gefixt** (route=null over lange afstand → een ship-leg landde op een landinwaarts
  punt): (1) Walvis→VS-markt zonder VS-haven → gereroute naar Rotterdam/Duitsland; (2+3) Japan/Korea-markt landinwaarts
  + Korea→Japan kan niet over land (geen landbrug) → markt kustpunt Nagoya (`coastal:true`) + Onsan→markt naar `ship`;
  (4) beursmagazijnen die per schip beleverd worden → `coastal:true`. **Les/risico:** elke ship-leg moet op een
  kustpunt (`port`/`coastal`/`wp-`) eindigen, anders valt hij op de landkaart terug (of vindt geen pad) — checken bij
  elke nieuwe schip-grondstof.
- ⚠️ **Visuele bevestiging blijft open** — WebGL-canvas laat zich niet headless screenshotten (zelfde gat als M5/M6).
  Op Netlify/mobiel te checken: Andes-concentraatbundel convergeert op de Chinese smelters?, Copperbelt-kathode kruipt
  over land naar de kust (Kasumbalesa)?, beursvoorraden-toggle + koperkleurige spoel-markers?, scheeps-voyages lopen?
- ⚠️ **Concurrency:** een tweede chat werkte deze sessie in dezelfde projectmap aan M8 (zeldzame aardmetalen). Bij
  gedeelde memory/CLAUDE-bestanden chirurgisch bewerken (geen full-file overwrites) om elkaars werk niet te clobberen.

## M6 · Goud — geverifieerd headless (2026-07-14)
- Goud volledig gebouwd + geverifieerd in de draaiende preview: 31 luchtroutes (alle `air`, bogen tillen
  2,5–12,7% op), CB-toggle 31→35 routes + 12 voorraad-nodes, "✈ vluchten"-teller, regressie **371 legs / 0 kapot**
  over alle 10 grondstoffen (lithium/kobalt onaangeraakt). `atlas-standalone.html` laadt schoon.
- ⚠️ **Visuele bevestiging blijft open (LAR-403)** — WebGL-canvas laat zich niet headless screenshotten (zelfde gat
  als M5). Op Netlify/mobiel te checken: Ticino-trechter mooi in beeld?, luchtbogen plausibel (bendten netjes via de
  hubs, geen rare knikken)?, labels/knopen leesbaar?, voyages-vliegtuigjes lopen?
- **Aandachtspunt `atlas-standalone.html`:** gegenereerd artefact (1,4 MB) — overweeg te gitignoren zodat de repo
  niet vervuilt; niet handmatig editen (regenereer via `build-standalone.py`).

## M5-port naar modulaire code — geverifieerd (2026-07-14)
- M5-fixes zitten nu ook in de **modulaire bron van waarheid** (waren alleen in de single-file). Headless
  routeverificatie in de draaiende atlas: **214 legs gerouteerd, 0 kapotte routes**; 3 M5-bugroutes
  geometrisch correct (Antwerpen→Newark + Kaap→Deense Straten via Nauw van Calais, Cuba→Montréal de
  Saint-Laurent op). Eén restfout (kobalt Niihama→Osaka, null-route) gefixt met de **Seto-brug**.
- ⚠️ **Visuele bevestiging blijft open** — preview-screenshot liep vast (WebGL-time-out). Op Netlify/mobiel
  te bekijken (zit al in LAR-403). Dit is de enige rest vóór `globe-oud`/single-file opgeruimd mag worden.

## M5-bugs — OPGELOST + geverifieerd (2026-07-14, aparte CC-sessie) → LAR-393/394/395/396 Done
**Aanpak 395/396** (kobaltroutes Cuba→Canada + Europa→Amerika): Straat van Dover + St. Lawrence als knelpunt
open geforceerd (zelfde patroon als Lombok/Malakka); regressiecheck 0 kapotte routes over alle stromen.
**Aanpak 393/394** (tegelnaad + drempel): shell-laag (hele bol grove tegels) + scherpe detailpatch; blue-marble
prikt nergens meer door. ⚠️ Visueel **niet met screenshot** bevestigd (WebGL-capture liep vast) — numeriek/geometrisch getoetst.
Referentie-symptomen hieronder:
- **LAR-393 (High)** — bol toont **twee verschillende kaarten naast elkaar** bij vaste zoom: de ene helft
  tegellaag (Esri, scherp), de andere basemap-satelliettextuur, met zichtbare naad/overhang. Beeld springt
  vaak van view. Vermoedelijke oorzaak: tegellaag (`tiles.js`, z=6.2) en basemap (`basemap.js`) te
  gescheiden. (Waargenomen op mobiel, 14 juli 2026.)
- **LAR-394 (Medium)** — tegellaag (mooier dan basemap) eerder tonen: drempel `z=6.2` omhoog (~7.5–8),
  evt. standaard actief zodra bol interactief wordt. **Afweging:** eerder tegels = meer tegelverzoeken =
  zwaarder op mobiel.
- **LAR-395 (High)** — kobaltroute **Zuid-Amerika → Noord-Amerika** loopt niet plausibel (knik bij Great
  Lakes/Nova Scotia). Checken: lat/lon omgedraaid of verkeerd teken, haven aan verkeerde kust,
  raster/waypoint. Bestanden: `data/kobalt.js`, `searoute.js`.
- **LAR-396 (High)** — kobaltroute **Europa → Amerika** klopt niet. Transatlantisch is de simpelste route;
  als díé eruitziet als een omweg wijst dat op iets structureels (great-circle vs. rasterpad). Bestand:
  `data/kobalt.js`, `searoute.js`.

## Risico's / aandachtspunten
- **Coördinaatfouten** (lat/lon-swap, verkeerd teken west/oost) zijn een terugkerende bron van verkeerde
  routes. Bij elke nieuwe grondstof checken.
- **Rasterresolutie 0,25°** verliest smalle doorgangen; nieuwe knelpunten moeten expliciet in
  `_chokepoints.js` als water geforceerd worden.
- **Gewogen A\* is niet gegarandeerd optimaal** — bewust ingeruild voor "wel een route vinden". Bij vreemde
  paden eerst hier kijken.
- **Goud-luchtvracht — OPGELOST (M6):** de route-engine was zee/land-A\*; goud kreeg een **3e route-modus**
  (great-circle-boog, `mode:"air"`, buiten het A\*-raster om). Korte hops blijven road/rail. Zie decisions.md.
  Restpunt (niet-blokkerend): het is nu één boog over de via-luchthavens (geen touch-down bij elke hub) en
  voyages gebruikt ship-tempo voor lucht — bewuste v1-vereenvoudiging, later te verfijnen.
- **Mobiele performance:** tegellaag + veel stromen + voyages kunnen zwaar worden; bewaken bij uitbreiding.
- **Modulair vs single-file — OPGELOST:** modulair is nu de bron van waarheid in de projectmap-git-repo, M5-fixes
  geport. Single-file blijft alleen als referentie tot visuele bevestiging.
- **Visuele M5-bevestiging ontbreekt** (screenshot lukt niet in de preview → WebGL-time-out). Bevestig op
  Netlify/mobiel voordat `globe-oud`/single-file definitief weg mag.

## Verholpen (referentie)
- Schaalbug (delen door camerastand i.p.v. afstand tot oppervlak) — opgelost in M2 (`scaleFor()`).
- Lange oceaanroutes vielen terug op rechte lijnen — opgelost met gewogen A\* (M3).
- Zeven Australische stromen als één dikke worm over Lombok — opgelost met vaarbanen (`laneShape`, M3).
