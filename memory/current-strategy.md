# Current strategy — Grondstoffen Atlas
*Last updated: 2026-07-15 (M9 · Uranium uitgevoerd; M8 zeldzame aardmetalen voorbereid)*

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
- **Optionele lagen via filter:** `layer:"cb"`-flows + `type:"cb"`-nodes gefilterd op `filters.showCentralBanks`
  (goud); sinds M7 óók `layer:"exchange"` + `type:"exchange"` op `filters.showExchangeStocks` (koper — beursvoorraden).
  Beide default uit, in `flows.js`/`markers.js`/`main.js`; de chip verschijnt alleen als een actieve grondstof die
  data heeft. **Herbruikbaar patroon** voor elke toekomstige optionele laag (kopieer de vier filterplekken + config +
  ui-chip + een marker-vorm).
- **Marker-types:** `mine`/`refinery`/`port`/`market` + (M6) `airport`/`hub`/`cb`/`recycler` + (M7) `exchange`
  (koperkleurige CylinderGeometry-spoel, grootte ∝ √`stock`) in `markers.js`.
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
  **uranium** (M9 — 38 nodes/36 flows, 4-staps kernbrandstofketen met verrijking als flessenhals + Trans-Kaspische route + VVER-lock-in + CANDU-uitzondering).
- **Basis:** de 6 overige grondstoffen (nikkel/grafiet/PGM/olie + zeldzame aarden-basis) — laden en renderen, maar zonder
  operators/capaciteiten/route-detail.
- **Voorbereid (ontwerp-skelet, nog niet gebouwd):** **zeldzame aardmetalen** (M8, `design/zeldzame-aardmetalen.md` —
  magneet-REE-framing NdPr+Dy/Tb, optie 2). Volgens het brief→bouw-sjabloon; bouwen ná koper's visuele bevestiging.
  Linear-milestone M8 nog aan te maken. Overige kandidaten op basis: nikkel (runner-up), grafiet, PGM, olie.

## Nu (2026-07-15 — M9 · Uranium uitgevoerd)

- **Uranium volledig gebouwd + geverifieerd.** `data/uranium.js` (38 nodes/36 flows/6 tensions): 4-staps kernbrandstof-
  keten op de 3 bestaande stages, met de **verrijking (~44% Rusland) als `raffinaat`-flessenhals** (institutionele knijp,
  via een `tension`, zoals Ticino). Nieuw: de **Trans-Kaspische route** om Rusland heen (3 Kaspische vaarpunten +
  Dardanellen in `_chokepoints.js`), de **VVER-lock-in** en de **CANDU-uitzondering**. Node-types alle bestaand → geen
  nieuwe render-modus/marker-styling. Headless: **uranium 54 legs / 0 kapot**, regressievrij. Gecommit (`d016ab8` brief +
  `76c0333` data, `main`, lokaal-only). **Linear M9 · Uranium + LAR-410..415** aangemaakt.
- **Rest:** **visuele bevestiging op Netlify/mobiel** (WebGL-screenshot lukt niet headless — LAR-415, Lars) + de
  bewust uitgestelde **militaire-kringloop-toggle** (LAR-414, oppakken ná de M8-code).
- **Ook eerder klaar:** M7 · Koper (gecommit, LAR-404..409 Done). M8 · Zeldzame aardmetalen op papier voorbereid.
- **Volgende grondstof:** nikkel (runner-up), grafiet, PGM, olie — volgens dezelfde brief→bouw-flow.
