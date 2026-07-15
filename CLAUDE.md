# Grondstoffen Atlas — project spec

*Categorie: General · Linear-project: "Grondstoffen Atlas" (team Lars / LAR) · Laatst bijgewerkt: 2026-07-15 (M11 · Olie uitgevoerd; M10 · Nikkel uitgevoerd; M8/M9)*

> **M11 · OLIE UITGEVOERD (2026-07-15):** `data/oil.js` van "basis" (18/15) → **uitgewerkt** (45 nodes / 46 flows /
> 6 tensions). Olie's vorm is bewust **anders dan alle eerdere**: geen enkele trechter maar het **hele knelpunten-
> netwerk dat tegelijk oplicht** — data bevestigt Hormuz #1 (15 stromen), Malakka, Taiwan, Suez/Bab, Bosporus, Panama,
> Kaap (10 knelpunten). Daarom **géén nieuw chokepoint** (= het eigen aha); wel 3 olie-only navigatie-vaarpunten
> (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`) in `_chokepoints.js`. Drie levende verhalen: de **Hormuz-bypass-
> pijpleidingen** (Saoedi→Yanbu, UAE→Fujairah), de **Rusland-omleiding 2022→** (Europese crude → India/China via
> Primorsk/Novorossiysk/ESPO-Kozmino/Druzhba) en de **Amerikaanse schalie-ommekeer** (Corpus Christi export). Keten op
> 3 stages: erts=ruwe olie / raffinaat=producten / product=petrochemie; schip+pijpleiding, **géén nieuwe render-modus**.
> Optionele **SPR-voorraden-toggle** (`layer:"reserve"`) eerst uitgesteld tijdens de parallelle nikkel-sessie, **daarna
> alsnog gebouwd** (LAR-432 Done, commit `86c8c1f`) = het **vierde** optionele-laag-patroon (goud-CB/koper-beurs/REE-recycling/
> olie-reserve): 5 SPR-nodes (`type:"reserve"`, `stock` mln vaten) + 5 vul-flows + tension, olie-amber tank-marker, chip
> "voorraden" alleen bij olie. Headless: **olie 210 legs / 0 kapot / 0 straight** (232 incl. reserve); toggle uit=45/46,
> aan=50/51; regressievrij. `atlas-standalone.html` geregenereerd (olie- + reserve-checks OK). Commits `1d4ece5` (data) +
> `86c8c1f` (toggle), lokaal-only, Claude-trailer. **Linear M11 · LAR-428..432 Done, 433 In Progress.** Rest = visuele bevestiging Netlify/mobiel (Lars).

> **M10 · NIKKEL UITGEVOERD (2026-07-15):** `data/nickel.js` van "basis" (13/4) → **uitgewerkt** (50 nodes / 46 flows /
> 6 tensions). De nikkel-"aha": de **trechter staat op z'n kop** t.o.v. koper — waar koper/lithium breed graven en in
> China raffineren, heeft **Indonesië in tien jaar de mijn ÉN de raffinage** naar zich toe getrokken via de **exportban
> op ruw erts** (IMIP Morowali / IWIP Weda Bay, Chinees kapitaal Tsingshan/Huayou); het erts blíjft in het land (korte
> mijn→smelter-hops). Plus **twee nikkels** (class-1 batterij/sulfaat vs class-2 roestvrij/NPI, met HPAL→MHP/matte als
> brug), de **prijscrash-shakeout** (BHP Nickel West stilgelegd 2024, Nieuw-Caledonië in crisis), de **LME-nuance**
> (alleen class-1 leverbaar + de 2022-squeeze) en het **Filipijnse ruw-erts-contrast** (geen ban). Schip+land, **géén
> nieuwe render-modus, géén nieuw chokepoint** (hergebruikt Makassar/Lombok/SCS/Taiwan/Deense-Straten/Panama/Saint-Laurent).
> **Beursvoorraden-laag (LME)** hergebruikt de **bestaande** exchange-toggle van koper met **0 engine-wijziging**
> (bevestigd generiek); recycling always-on. Headless: **nikkel 91 legs (63 zee + 18 land + 10 korte hops) / 0 kapot /
> 0 straight**, regressie schoon (0 kapot over alle grondstoffen). `atlas-standalone.html` geregenereerd (nikkel-checks OK).
> Commit `08aa4f5` (lokaal-only, Claude-trailer). **Linear M10 · LAR-422..426 Done, 427 In Progress** (visuele bevestiging =
> Lars). Overige op "basis": grafiet, PGM (olie loopt in een parallelle sessie).

> **M8 · ZELDZAME AARDMETALEN UITGEVOERD (2026-07-15):** `data/rare-earths.js` van "basis" (9/5) → **uitgewerkt**
> (41 nodes / 38 flows / 6 tensions) in de **magneet-REE-framing** (NdPr licht + Dy/Tb zwaar; `symbol: NdPr`,
> `unit: kt magneet-REO/jaar`). De **extreemste trechter** van de atlas: winning breed verspreid, scheiding ~85–90%
> Zuid-China (**Ganzhou**). Vier kern-aha's: Ganzhou-scheidingstrechter, **Dy/Tb-landstroom Myanmar→China** over de
> nieuwe grenscorridor **`grens-ruili`** (`_chokepoints.js`, Kasumbalesa-patroon), de **Mountain-Pass-rondreis**
> (concentraat heen over de Stille Oceaan, oxide terug) en de **NdFeB-magneet-waaier** vanuit China. Nieuwe
> **recycling-toggle** (`layer:"recycle"`, default uit) = het derde optionele-laag-patroon (goud=CB, koper=beurs,
> REE=recycling), bewust via `layer` op flows én nodes zodat koper's always-on recyclers ongemoeid blijven. Headless:
> **rare-earths 90 legs / 0 kapot / 0 straight**, regressievrij. `atlas-standalone.html` geregenereerd (REE-checks OK).
> **Linear M8 · LAR-416..420 Done, 421 In Progress.** Rest = visuele bevestiging Netlify/mobiel (Lars). Repo lokaal-only, `main`.

> **M9 · URANIUM UITGEVOERD (2026-07-15):** `data/uranium.js` van "basis" (9/2) → **uitgewerkt** (38 nodes / 36 flows /
> 6 tensions). Eerste grondstof met een bewust *andere vorm* — een **4-staps kernbrandstofketen** (winning → conversie →
> verrijking → splijtstof → reactor) met de **verrijking (~44% Rusland) als raffinaat-flessenhals**. Nieuw: de
> **Trans-Kaspische route** om Rusland heen (3 Kaspische vaarpunten + Dardanellen in `_chokepoints.js`), de **VVER-lock-in**
> en de **CANDU-uitzondering**. Headless: **uranium 54 legs / 0 kapot**, regressievrij. Commits `d016ab8` (brief) + `76c0333`
> (data). Linear-milestone **M9 + LAR-410..415**. Rest = visuele bevestiging (LAR-415). **Militaire-kringloop-toggle (LAR-414)
> ALSNOG GEBOUWD (2026-07-15, commit `6a6d062`):** het 5e optionele-laag-patroon (`type:"military"`/`layer:"secondary"`, down-blend/
> tails/reserves; Megatons-to-Megawatts) — headless uranium 60 legs / 0 kapot / 0 straight, toggle +4 nodes/+5 flows, chip alleen bij uranium.

> **STATUS VAN DEZE MAP (2026-07-14):** ✅ code-root (modulaire atlas als **git-repo**). **M0–M7 done** (op de
> visuele check na): naast lithium+kobalt+goud is nu **koper volledig uitgewerkt** (`data/copper.js`, 69 nodes/50 flows)
> — de **Andes-concentraat-trechter** → Chinese smelters + de **Copperbelt-kathode** over land (Kasumbalesa), plus een
> nieuwe **beursvoorraden-laag** (LME/SHFE/COMEX-toggle, zelfde patroon als de goud-CB-laag). Headless geverifieerd:
> **koper 145 legs / 0 kapot**, regressie **388 legs / 0 kapot** over alle 10 grondstoffen. **Modulair = bron van
> waarheid**; `build-standalone.py` genereert `atlas-standalone.html`. **Gecommit** (`main`, code `233b882` +
> wrapup-docs `7e46092`, lokaal-only); **Linear LAR-404..409 → Done**. Rest: alleen nog de **visuele bevestiging op
> Netlify/mobiel** (WebGL-screenshot lukt niet headless). Draaien lokaal: `python -m http.server 8732` (launch.json-entry `grondstoffen-atlas`).

## A - What this folder is

De grondstoffen atlas is een **interactieve 3D-wereldbol** die per kritieke grondstof de complete
handelsketen toont: waar het uit de grond komt (mijnen), waar het geraffineerd wordt, waar het
eindproduct gemaakt wordt, en langs welke **echte routes** (zee + land) het reist. De kern van het
verhaal zijn de **knelpunten**: Straat van Malakka, Lombok, Suez, en de structurele afhankelijkheid
van Chinese raffinage.

Geen abstracte bogen door de lucht: schepen varen over water, treinen/trucks over land, en op de
plekken waar alles samenknijpt zie je dat letterlijk gebeuren.

## B - The Goal

- **Waarom:** de geopolitiek van kritieke grondstoffen tastbaar en visueel navolgbaar maken — één
  bol waarop je de afhankelijkheden en knelpunten van de wereldhandel ziet.
- **Werkwijze (belangrijk):** *eerst ontwerpen, dan bouwen.* Per grondstof eerst een lijst met de
  belangrijkste knopen en stromen opstellen, pas daarna in de atlas zetten.
- **Template:** lithium is de volledig uitgewerkte referentie (34 knopen, 31 stromen). Kobalt is de
  tweede. De overige grondstoffen staan op detailniveau "basis" en wachten op uitwerking.
- **Volgende inhoudelijke stap:** eerst M5 (visuele bugs + routecorrecties), daarna nieuwe grondstof-
  ketens uitwerken. Kandidaten: koper (op de roadmap) en **goud** (Lars' huidige focus).

## C - Stack & locatie

- **Tech:** vanilla JS + Three.js. **Geen bundler** — losse globals-bestanden met vaste laadvolgorde
  via `<script>`-tags in `index.html`.
- **Huidige code-locatie:** ✅ **deze projectmap** (`Projects\General\grondstoffen-atlas`, git-repo). De modulaire
  code (config/geo-data/index/style/src/data/textures) is hier de werkbasis. Referenties op het bureaublad:
  single-file `C:\Users\lars\Desktop\globe\atlas-lithium-kobalt.html` (M5-referentie/deploy-build) en de oude
  modulaire backup `C:\Users\lars\Desktop\globe-oud\grondstoffen-atlas-v2\atlas\` — beide **onaangeraakt**, mogen
  weg zodra de repo visueel op Netlify/mobiel bevestigd is.
- **✅ Beslist + uitgevoerd (2026-07-14): modulair = bron van waarheid** (single-file = gegenereerde build). Code
  verplaatst + `git init`; M5-fixes geport (214 legs, 0 kapotte routes geverifieerd).
- **Deploy:** Netlify, drag-and-drop (single-file build daarvoor handig).
- **Bestandsindeling (modulaire opzet — in deze map):**
  - `config.js` — alle instellingen op één plek
  - `geo-data.js` — landpolygonen (`LAND_POLYS`)
  - `index.html` — vaste script-laadvolgorde
  - `src/` — `util.js`, `globe-core.js`, `basemap.js`, `tiles.js`, `searoute.js`, `markers.js`,
    `flows.js`, `voyages.js`, `ui.js`, `main.js`
  - `data/` — `_registry.js`, `_chokepoints.js` + **per grondstof een `.js`** (`lithium.js`,
    `cobalt.js`, `copper.js`, `graphite.js`, `nickel.js`, `oil.js`, `pgm.js`, `rare-earths.js`,
    `uranium.js`) — lithium+kobalt uitgewerkt, de rest op "basis". **Naast elke `.js` een leesbare
    brief `<grondstof>.md`** (bijv. `lithium.md` = het voorbeeld) die je invult vóór je codeert.

## D - Decisions

Zie `memory/decisions.md`. Kernbesluiten: geen bundler (globals + script-tags); A\* over een
1440×720 land/zee-raster voor echte routes; knelpunten worden als water geforceerd; één `data/<grondstof>.js`
per grondstof volgens het lithium-schema; "eerst ontwerpen, dan bouwen".

- **2026-07-14 · modulair = bron van waarheid, uitgevoerd** — code → deze map + `git init`; M5-fixes geport.
- **2026-07-14 · grensovergang als landpunt** — `kind: "grensovergang"` stempelt de LANDkaart open (niet de
  zeekaart); `isSeaPoint` behandelt hem als landpunt. Per-waypoint `openRadius` voor smalle rivieren (Saint-Laurent).
- **2026-07-14 · Seto-brug** als `LAND_LINK` — Shikoku is een apart raster-eiland → landroute Niihama→Osaka.
- **2026-07-14 · M6 luchtroute-modus** — `mode:"air"` = 3e route-type: buiten de A\*-routering om (`&& !airMode`
  in `flows.js`), altijd een opgetilde great-circle-boog (`flat:false` + `arcStyle`-lift, hoogte ∝ afstand), óók
  in route-view. Korte hops blijven road/rail. Reden: goud vliegt écht die boog (voor lithium was hij fout).
- **2026-07-14 · M6 optionele CB-laag via `layer`-filter** — `type:"cb"`-nodes + `layer:"cb"`-flows filteren op
  `filters.showCentralBanks` (default uit); chip alleen bij grondstoffen met CB-data. Herbruikbaar patroon voor
  toekomstige optionele lagen (bv. koper-beursvoorraden). Nieuwe marker-types airport/hub/cb/recycler.
- **2026-07-14 · M6 single-file als gegenereerde build** — `build-standalone.py` lijnt CSS + lokale scripts uit
  `index.html` inline (three.js-CDN blijft extern) → `atlas-standalone.html`. Niet handmatig editen; regenereren.
- **2026-07-14 · M7 koper = schip/land, geen nieuwe render-modus** — hergebruikt zee-A\*/land-A\* (M3) + scheeps-voyages
  (M4). Twee productvormen via `stage`: sulfide-concentraat (`erts` → smelter, de Andes→China-trechter) vs. SX-EW-kathode
  (`raffinaat` al bij de bron, direct als metaal). Recycling **always-on** (net als goud, niet achter de toggle).
- **2026-07-14 · M7 Copperbelt-landcorridor via het kobalt-patroon** — land-flow mijn→haven (`mode: road/rail`,
  `via: ["grens-kasumbalesa"]`) + aparte ship-flow haven→markt. In een ship-flow worden twee opeenvolgende landpunten
  een rechte lijn → splitsen op de haven. **Elke ship-leg moet op een kustpunt (`port`/`coastal`/`wp-`) landen.**
- **2026-07-14 · M7 beursvoorraden-laag** (`type:"exchange"` / `layer:"exchange"`, filter `showExchangeStocks`) — LME/
  SHFE/COMEX als optionele toggle, default uit, exact het CB-laag-patroon (vier filterplekken + config + ui-chip +
  marker). Marker = koperkleurige CylinderGeometry-spoel, grootte ∝ √`stock`. Herbevestigt: optionele lagen zijn een
  herbruikbaar patroon.
- **2026-07-15 · M8 zeldzame aardmetalen voorbereid (magneet-REE-framing)** — ontwerp-skelet `design/zeldzame-aardmetalen.md`;
  framing = **magneet-REE (NdPr + Dy/Tb)** (optie 2 na Lars' "is REE niet te generiek?": REE is intrinsiek een groep,
  winning blijft gemengd erts, scheiding = de knijp). Magneet = stage `product`; schip+land (géén nieuwe render-modus);
  nieuw Myanmar→China `grens-*`-knelpunt bij de bouw; recycling = optionele toggle. Nog niet gebouwd; Linear M8 aan te
  maken (MCP-auth ontbrak). Details in `memory/decisions.md`.
- **2026-07-15 · M9 uranium = 4-staps keten op 3 stages** — winning + conversie = `erts` (feed), **verrijking = `raffinaat`
  (de flessenhals)**, splijtstof = `product`, reactoren = `market`. Node-types alle bestaand → géén nieuwe marker-styling.
  De verrijkings-knijp (~44% Rusland) draagt via een `tension`, geen `wp-` — zoals Ticino bij goud. Schip+land, geen nieuwe modus.
- **2026-07-15 · M9 Kaspische oversteek + Dardanellen** (`_chokepoints.js`) — 3 vaarpunten (`wp-kaspisch-n/-m/-z`) forceren
  een watercorridor Aktau↔Bakoe (Kaspische Zee = ingesloten zee, valt deels als land in het raster); `wp-dardanellen` houdt
  naast `wp-bosporus` de Zwarte-Zee-uitgang open (anders geen weg Poti→Middellandse Zee). Alleen uranium gebruikt ze → geen
  impact op andere grondstoffen. Landlocked-routering (Kazachstan/Niger) = het kobalt/koper-corridorpatroon (land-flow →
  haven + aparte ship-flow). **CANDU-uitzondering** eerlijk gemodelleerd (natuurlijk uranium, geen verrijking). Details in `memory/decisions.md`.
- **2026-07-15 · M9 militaire-kringloop-toggle uitgesteld → ALSNOG GEBOUWD** (LAR-414 Backlog → **Done**, commit `6a6d062`) — de
  optionele `layer:"secondary"`-laag vereiste code in `flows/ui/main/config/markers`, destijds dirty door de parallelle M8-sessie →
  eerst alleen de data-laag. Op Lars' verzoek afgemaakt zodra de engine schoon was: het **5e** optionele-laag-patroon
  (`type:"military"`-nodes + `layer:"secondary"`-flows + `showMilitary`/`hasMilitary()`), exact het olie-`reserve`-patroon in 5 plekken.
  4 military-nodes (Rosatom down-blend/HEU, tails-herverrijking, US DOE, US strategische reserve) + 5 `secondary`-flows (o.a. de
  historische Megatons-to-Megawatts-stroom Rusland→VS via `u-fab-us` `coastal:true`) + tension `u-t-military`. Headless: uranium 60 legs /
  0 kapot / 0 straight; toggle uit→aan +4 nodes/+5 flows; chip alleen bij uranium. Sectie J: alleen mijn 6 bestanden gestaged (PGM/silver-sessie ontzien).
- **2026-07-15 · M8 magneet-REE-framing gebouwd** — `data/rare-earths.js` "uitgewerkt" (41/38/6): `id` blijft `rare-earths`,
  `symbol: NdPr`, `unit: kt magneet-REO/jaar`. Scheiding én magneetfabrieken beide `type:"refinery"` (het `erts`/`raffinaat`/
  `product`-stagekleur draagt het onderscheid concentraat→NdPr/Dy-oxide→NdFeB-magneet); magneet = stage `product` (geen 4e stage).
  Schip+land, géén nieuwe render-modus. Reden: één scherp verhaal (NdPr+Dy/Tb), winning blijft eerlijk gemengd erts → scheiding = de knijp.
- **2026-07-15 · M8 grenscorridor `grens-ruili`** (`_chokepoints.js`, `kind:"grensovergang"`, 24.02/97.85) — Myanmar→China, exact
  het Kasumbalesa-patroon (landpunt, houdt de landkaart open). Draagt de Dy/Tb-landstroom Kachin→Ganzhou; alleen REE gebruikt het.
- **2026-07-15 · M8 recycling-toggle** (`layer:"recycle"`, `showRecycle`, default uit) = het **derde** optionele-laag-patroon (na
  CB en exchange). Bewust `layer:"recycle"` op flows **én** recycler-nodes: de node-gate zit op `node.layer==="recycle"` (niet op
  `type==="recycler"`) en `hasRecycle()` op `f.layer==="recycle"`, zodat **koper's always-on recyclers** (zónder `layer`) ongemoeid
  blijven en alleen REE de toggle/chip krijgt. Vijf plekken: `config.js`/`main.js`/`flows.js`/`markers.js`/`ui.js`.
- **2026-07-15 · M8 co-located nodes ~30–45 km uit elkaar** — twee nodes van dezelfde grondstof in één 0,25°-cel geven een 1-punts
  route (`degDist:0`, onzichtbare arc). Ref/magneet/recycler in dezelfde stad (Baotou/Ganzhou/MP/La Rochelle/Fort Worth) verschoven
  zodat de lokale scheiding→magneet-arcs zichtbaar renderen én de headless-teller schoon op 0 kapot blijft.
- **2026-07-15 · M10 nikkel = de omgekeerde trechter, koper als template** — nikkel is een schip/land-grondstof (géén luchtvracht →
  koper, niet goud, is het model). De "aha" is dat Indonesië via de **exportban op ruw erts** de mijn ÉN de raffinage aan land trok:
  het erts blíjft in het land (korte mijn→smelter-hops, `stage:"erts"`, `mode:"road"`) en gaat pas als NPI/matte/MHP de zee op —
  andersom dan koper/lithium waar het erts/concentraat naar China vaart. Class-1 (batterij/sulfaat) vs class-2 (roestvrij/NPI) gedragen
  via `stage` + `note` + een `tension` (geen 4e stage). Het Filipijnse ruw-erts (`stage:"erts"` naar China, géén ban) = het contrast.
- **2026-07-15 · M10 géén nieuw chokepoint (tweede na koper)** — nikkel draait volledig op de bestaande routekaart (Makassar/Lombok/
  SCS/Taiwan; Deense Straten voor Fins/Baltisch class-1; Panama + Pacific-vaarpunten voor Cuba/NC; de Saint-Laurent-keten voor
  Voisey's Bay→Sudbury). Bewust zo — óók om de gedeelde `_chokepoints.js` niet te raken terwijl de parallelle olie-sessie die dirty had.
- **2026-07-15 · M10 beursvoorraden-laag (LME) = 0 engine-wijziging** — de optionele exchange-toggle van koper (`type:"exchange"`/
  `layer:"exchange"`, `showExchangeStocks`) is generiek: `hasExchangeStocks()` vuurt op elke actieve grondstof met een exchange-node,
  en de flow-gate/marker/chip zijn niet koper-specifiek. Nikkel voegt dus 4 LME-nodes + 5 `layer:"exchange"`-flows toe **zonder één
  `src/*`/`config.js`-regel te wijzigen** — de eerste keer dat een optionele laag puur via de data-laag wordt hergebruikt. Nuance eerlijk
  gemodelleerd: **alleen class-1 is LME-leverbaar** (NPI/MHP/sulfaat niet) → LME-prijs ≠ fysieke markt (de 2022-squeeze als `tension`).
  Recycling **always-on** (koper-patroon, `type:"recycler"` zónder `layer`).
- **2026-07-15 · M11 olie = het knelpunten-netwerk, géén nieuw chokepoint** — olie's vorm is bewust anders dan alle eerdere: geen
  enkele trechter maar het **hele bestaande net van zeestraten dat tegelijk oplicht** (Hormuz #1 met 15 stromen, dan Malakka/Suez/Bab/
  Bosporus/Panama/Kaap). Bewust géén nieuw knelpunt toegevoegd — dat olie het hele net laat oplichten ís de boodschap. Wél 3 kleine
  **navigatie-vaarpunten** (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`) in een gelabeld OIL-blok in `_chokepoints.js`, om de VS/
  Venezuela-routes op het water te houden; olie-only → regressievrij. Keten op de 3 stages met **petrochemie als 3e daad**
  (`erts`=crude → `raffinaat`=producten → `product`=nafta→kraker→kunststof). Schip + `mode:"pipeline"`, géén nieuwe render-modus;
  crude-stromen starten bij de mijn met de export-terminal als 1e via-punt (gathering-leg routeert auto als land). Kust-raffinaderijen `coastal:true`.
- **2026-07-15 · M11 SPR-voorraden-toggle uitgesteld → alsnog gebouwd** (LAR-432 Backlog → **Done**, commit `86c8c1f`) — de
  optionele `layer:"reserve"`-laag (strategische petroleumreserves, olie's CB/beurs/recycling-equivalent) raakt de 5 gedeelde
  engine-bestanden; tijdens de parallelle M10-nikkel-sessie eerst alleen de data-laag gebouwd (zoals uranium's LAR-414, sectie J).
  Zodra de tree schoon was (Lars: "de voorraden bij olie is een goed idee") de toggle alsnog toegevoegd = het **vierde** optionele-laag-
  patroon, exact het koper-`exchange`-patroon (dedicated `type:"reserve"`, `hasReserves()` op `n.type`) + olie-amber tank-marker.
  5 SPR-nodes + 5 vul-flows + tension `oil-t-spr`. Headless: toggle uit=45/46, aan=50/51 (+5/+5), 0 kapot/0 straight, chip alleen bij olie, regressievrij.

## E - Memory Map

De projectgeschiedenis en werkgeheugen leven in `memory/` (6 files, conventie zoals de andere projecten):

- `project-brief.md` — wat het is, huidige baseline, richting, harde grenzen
- `current-strategy.md` — hoe we nu bouwen (architectuur, sjabloon, aanpak per grondstof)
- `next-actions.md` — concrete volgende stappen (M5 + goud-ontwerp)
- `decisions.md` — vastgelegde technische/inhoudelijke keuzes
- `bugs-and-risks.md` — openstaande bugs (M5) en risico's
- `session-summaries.md` — per sessie een samenvatting

Daarnaast `design/`:
- `_brief-template.md` — **herbruikbare template voor de grondstof-brief** (alle nodes/stromen op een rij
  vóór het code wordt; sluit 1-op-1 aan op het `.js`-schema). Kopieer → `data/<grondstof>.md` en vul in.
- `goud.md` — het uitgewerkte goud-ontwerp (wordt bij LAR-397/398 een volledig ingevulde brief).

De browsbare wiki-samenvatting staat onder `Portable LLM brain\wiki\projects\General\grondstoffen-atlas\`.

## F - References

- Linear: project "Grondstoffen Atlas" — https://linear.app/error-logger/project/grondstoffen-atlas-ace3a91b93fb
- Issues M0–M5: LAR-378 t/m LAR-396.

## G - Project-specific overrides

- **Taal:** UI-teksten en annotaties in de atlas zijn **Nederlandstalig**.
- **Geen framework/bundler introduceren** zonder expliciete afstemming — de globals-opzet is bewust.
- Coördinaten zijn `lat`/`lon` (west = negatief). Fouten hierin zijn een terugkerende bron van
  verkeerde routes (zie M5).

## H - Onboarding-checklist

1. [x] M5 door aparte CC-sessie klaar + geverifieerd (2026-07-14); LAR-393/394/395/396 Done.
2. [x] Wiki-pagina + `now.md`-regel + Pinecone-gist (eerste wrapup, 2026-07-14).
3. [x] Beslist: **modulair = bron van waarheid** (single-file = gegenereerde build).
4. [x] Modulaire code **verplaatst** naar deze map + `git init` (2 commits `b9d69fa`, `177bc6b`) = werkbasis. GitHub-remote nog optioneel.
5. [x] **M5-fixes geport** uit de single-file naar de modulaire code + geverifieerd (214 legs, 0 kapotte routes). Visuele check op Netlify/mobiel rest nog (WebGL-screenshot lukte niet).
6. [x] **M6 · Goud uitgevoerd** (2026-07-14): research LAR-397/398 → `data/goud.js` LAR-401 + luchtroute-modus LAR-399 + voyages-lucht LAR-400 + CB-toggle LAR-402. Headless geverifieerd (371 legs/0 kapot). LAR-403 rest = visuele bevestiging Netlify/mobiel.
7. [x] **M7 · Koper uitgevoerd** (2026-07-14): `data/copper.js` "uitgewerkt" (69 nodes/50 flows/5 tensions) — Andes-concentraat-trechter + Copperbelt-kathode over land (Kasumbalesa) + beursvoorraden-laag (LAR-408, `layer:"exchange"`). Headless geverifieerd: koper 145 legs / 0 kapot, regressie 388/0. Rest = visuele bevestiging Netlify/mobiel + code-commit (Lars' seintje) + Linear LAR-404..409 → Done (MCP-auth ontbrak).
8. [x] **M9 · Uranium uitgevoerd** (2026-07-15): `design/uranium.md` (`d016ab8`) → `data/uranium.js` "uitgewerkt" (38 nodes/36 flows/6 tensions) + Kaspische oversteek/Dardanellen in `_chokepoints.js` (`76c0333`). 4-staps keten met verrijking als flessenhals (~44% Rusland) + Trans-Kaspische route + VVER-lock-in + CANDU-uitzondering. Headless: 54 legs/0 kapot, regressievrij. **Linear M9 · Uranium + LAR-410..415** aangemaakt (410-413 Done; 414 Backlog = uitgestelde militaire-kringloop-toggle; 415 In Progress = visuele bevestiging). Rest = visuele bevestiging Netlify/mobiel.
9. [x] **M8 · Zeldzame aardmetalen uitgevoerd** (2026-07-15): `data/rare-earths.js` van "basis" (9/5) → "uitgewerkt" (41 nodes/38 flows/6 tensions), magneet-REE-framing (NdPr+Dy/Tb) + `grens-ruili` (Myanmar→China) in `_chokepoints.js` + recycling-toggle (`layer:"recycle"`, 5 plekken). Ganzhou-scheidingstrechter + Dy/Tb-landstroom + Mountain-Pass-rondreis + NdFeB-waaier. Headless: 90 legs/0 kapot/0 straight, regressievrij. **Linear M8 · LAR-416..420 Done; 421 In Progress** (visuele bevestiging Netlify/mobiel = Lars).
10. [x] **M10 · Nikkel uitgevoerd** (2026-07-15): `data/nickel.js` van "basis" (13/4) → "uitgewerkt" (50 nodes/46 flows/6 tensions) + `design/nikkel.md` + nikkel-checks in `build-standalone.py`. Indonesië-onshoring-trechter (exportban: mijn+raffinage in tien jaar, IMIP/IWIP) + twee nikkels (class-1 batterij vs class-2 roestvrij) + prijscrash-shakeout (Nickel West 2024) + LME-nuance (2022-squeeze). Schip+land, géén nieuw chokepoint; beursvoorraden-laag hergebruikt de bestaande exchange-toggle (**0 engine-wijziging**); recycling always-on. Headless: **nikkel 91 legs / 0 kapot / 0 straight**, regressie schoon. Commit `08aa4f5` (lokaal-only, Claude-trailer). **Linear M10 · LAR-422..426 Done, 427 In Progress**. Overige op basis: grafiet, PGM.
11. [x] **M11 · Olie uitgevoerd** (2026-07-15): `data/oil.js` van "basis" (18/15) → "uitgewerkt" (45 nodes/46 flows/6 tensions) + `design/olie.md` + 4 olie-checks in `build-standalone.py`. Het **knelpunten-netwerk dat tegelijk oplicht** (Hormuz #1 met 15 stromen, Malakka, Suez/Bab, Bosporus, Panama, Kaap) → **géén nieuw chokepoint** (eigen aha), wel 3 olie-only vaarpunten (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`) in `_chokepoints.js`. Drie verhalen: Hormuz-bypass-pijpleidingen (Yanbu/Fujairah) + Rusland-omleiding 2022→ (India/China) + VS-schalie-ommekeer. Keten 3 stages (erts/raffinaat/petrochemie), schip+pijpleiding, géén nieuwe render-modus. Headless: **olie 210 legs / 0 kapot / 0 straight**, regressievrij (baseline 5 = lithium 4 + goud 1). Commit `1d4ece5` (lokaal-only, Claude-trailer). **SPR-voorraden-toggle (`layer:"reserve"`) daarna alsnog gebouwd** (LAR-432 Done, commit `86c8c1f`) = het vierde optionele-laag-patroon; toggle uit=45/46, aan=50/51, chip "voorraden" alleen bij olie. **Linear M11 · LAR-428..432 Done, 433 In Progress**. Overige op basis: grafiet, PGM.

## I - Runbook: "werk grondstof X uit" (self-serve)

Vaste flow om een grondstof van **"basis" → "uitgewerkt"** te brengen, identiek aan hoe goud/koper/uranium/REE zijn gedaan.
Nog op "basis": **grafiet**, **PGM**. Doe de stappen op volgorde; commit code en wrapup-docs apart.

**0. Oriënteer.** Lees `memory/current-strategy.md` (architectuur + sjabloon) + `memory/decisions.md` (de vaste patronen) +
   `design/_brief-template.md`. Kijk naar een recent uitgewerkt bestand als voorbeeld — `data/copper.js` (schip/land + optionele
   toggle) of `data/uranium.js` (tension-knijp + nieuw chokepoint) liggen het dichtst bij de meeste grondstoffen.

**1. Linear vastleggen vóór het codewerk.** Maak (via de Linear-MCP die zónder OAuth werkt — de `331d1eb1…`-server met
   `save_milestone`/`save_issue`, **niet** de auth-vereiste `plugin:engineering:linear`; zie [[linear-mcp-two-surfaces]]) een
   **milestone** `M<n> · <Grondstof>` in project "Grondstoffen Atlas" (team **Lars/LAR**) + de standaard **±6 issues**, gespiegeld op M6/M7/M9:
   - research upstream (winning/mijnbouw) · research downstream (raffinage/consumptie/recycling)
   - het grondstof-eigen **nieuwe element** (nieuw chokepoint/corridor, of een render-modus) — sla over als de grondstof volledig bestaande routes hergebruikt
   - `data/<x>.js` van "basis" → "uitgewerkt"
   - de optionele **toggle-laag** (CB/beurs/recycling-stijl) — alleen als de grondstof er een heeft
   - verificatie (headless) + single-file build + visuele bevestiging Netlify/mobiel
   Research mag inline in de brief (stap 2) — die research-issues gaan Done zodra de brief staat.

**2. Ontwerp eerst (brief).** Kopieer `design/_brief-template.md` → `design/<x>.md` en vul alle knopen/stromen in
   (operators, capaciteiten, `lat`/`lon`, transportmodi, de "aha"/knijp van deze grondstof). Eerst ontwerpen, dan bouwen.

**3. Bouw `data/<x>.js`** volgens het lithium-schema (zie `data/_registry.js` voor het veld-schema):
   - Metadata: `id`/`name`/`symbol`/`color`/`unit`/`blurb`, `detail:"uitgewerkt"`.
   - Nodes (`mine`/`refinery`/`port`/`market` + evt. `recycler`/`exchange`/`cb`), flows met `stage` (`erts`→`raffinaat`→`product`)
     + `mode` (`ship`/`rail`/`road`) + `via:[...]` langs havens en `wp-*`/`grens-*`, en `tensions` voor de knijppunten.
   - **Registratie is er al** voor de bestaande 10 grondstoffen (script-tag in `index.html`). Een *nieuwe 11e* grondstof: voeg een
     `<script src="data/<x>.js">` toe in `index.html` (de build leest die volgorde).
   - **Harde regel:** elke ship-leg moet op een kustpunt landen (`port` / `coastal:true` / `wp-*`), anders valt hij op de landkaart terug
     of vindt geen pad. Landlocked → kobalt/koper-corridorpatroon (land-flow mijn→haven `via:["grens-…"]` + aparte ship-flow haven→markt).
   - Nieuw chokepoint/corridor nodig? Voeg het toe aan `data/_chokepoints.js` (`kind:"grensovergang"` voor een landgrens; `wp-…` + evt.
     `openRadius` voor een zeestraat/ingesloten zee). Twee nodes in dezelfde 0,25°-cel geven een onzichtbare `degDist:0`-arc → ~30–45 km uit elkaar.

**4. Engine-wijziging (alleen als nodig).** Een nieuwe **optionele toggle-laag** = het vaste patroon op vijf plekken
   (`config.js` marker-size · `main.js` filters-default + `has…()` + voyages-gate · `flows.js` flow-gate · `markers.js` node-gate · `ui.js` chip).
   Een nieuwe **render-modus** (zoals goud-lucht) raakt `flows.js`. Zie sectie J vóór je gedeelde `src/*`-bestanden aanraakt bij parallel werk.

**5. Verifieer headless in de draaiende atlas.** Start de dev-server (launch.json-entry, zie sectie J voor de poort), open 'm in de
   Browser-pane, en draai via `javascript_tool` een legs-check die per flow de stops (`from`+`via`+`to`) langs `Routing.sea`/`Routing.land`
   routeert en telt: **doel = <grondstof> X legs / 0 kapot / 0 straight**, plus **regressie** over alle grondstoffen (globaal blijft 5 kapot =
   de bekende `degDist:0` lithium(4)+goud(1)-baseline; nieuwe grondstof voegt 0 toe). Check ook: geen console-warnings (onbekende via-/node-ids),
   toggle aan/uit voegt de juiste flows/nodes toe. Visueel het emergente plaatje bekijken (screenshot); **volledige visuele bevestiging op
   Netlify/mobiel = Lars** (WebGL-screenshot lukt niet betrouwbaar headless).

**6. Build + wrapup.** `python build-standalone.py` (voeg een REE-stijl sanity-check toe voor je grondstof) → `atlas-standalone.html`.
   Dan de **`wrapup`-skill**: die voert de Definition of Done uit (vault-sessiesamenvatting + integratie in projectpagina/`now.md`/`index.md`/
   `log.md`/`timeline.md`, project-`memory/`-sync, `CLAUDE.md`/checklist, Linear op Done, Pinecone-gist, code + docs committen). Commit code en
   wrapup-docs als **twee aparte commits** met de Claude-trailer; repo is **lokaal-only** (geen remote → geen push).

## J - Parallel werken (meerdere sessies tegelijk)

Twee sessies kunnen **verschillende grondstoffen tegelijk** uitwerken (is al gebeurd: M7+M8, en M9 naast M8). Elke grondstof heeft z'n
eigen `data/<x>.js` + `design/<x>.md` — die botsen nooit. Frictie zit alleen op het **gedeelde oppervlak**. Regels:

1. **Stage alleen je eigen bestanden — nooit `git add -A`/`git add .`.** De working tree bevat de half-af bestanden van de andere sessie.
   Voorbeeld: `git add data/<x>.js design/<x>.md` (+ je eigen `_chokepoints.js`-toevoeging als je die deed). Veeg je alles op, dan commit
   je hun onvoltooide werk. Twijfel je of een gewijzigd bestand van jou is? Laat het ongestaged en noem het.
2. **Gedeelde engine-bestanden = `src/*.js`, `config.js`, `data/_chokepoints.js`, `build-standalone.py`.** Raakt jouw grondstof die, en heeft
   de andere sessie ze dirty? **Bouw dan eerst alleen de data-laag en stel de engine-wijziging uit** (zoals uranium's militaire-toggle → LAR-414
   Backlog). Voeg de toggle/modus later toe als de tree schoon is.
3. **Nieuwe chokepoints append je in een eigen, gelabeld blok** in `data/_chokepoints.js` en commit dat vroeg/apart — losse toevoegingen aan het
   eind conflicteren zelden textueel. Alleen jouw grondstof mag ernaar verwijzen (geen impact op de andere 9).
4. **Eigen dev-server-poort per sessie** (launch.json): `grondstoffen-atlas` (8732) · `grondstoffen-atlas-2` (8733) · `-3` (8734) · `-4` (8735).
   Laat niet twee sessies dezelfde poort binden. (Één draaiende server delen kan ook — het is statische file-serving; elke browser-load leest vers.)
5. **Wrapups sequentieel, `git pull --rebase` eerst.** De vault is een gedeelde repo: `log.md`/`index.md`/`timeline.md` mergen automatisch
   (`merge=union`), maar `now.md` en de projectpagina niet — laat één sessie helemaal afwrappen (incl. vault-push) vóór de ander z'n vault-write doet.
   Linear (aparte milestones/issues) en Pinecone zijn onafhankelijk en botsen niet.
6. **Maximale isolatie (optioneel):** geef elke sessie een eigen **git-worktree** (aparte werkmap, eigen branch) → de working trees zijn fysiek
   gescheiden en conflicten komen pas netjes bij het mergen boven i.p.v. als rommelige gedeelde tree. Werkt ook op deze lokaal-only repo; kost een merge-stap.
