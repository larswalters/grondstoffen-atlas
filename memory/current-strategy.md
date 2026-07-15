# Current strategy — Grondstoffen Atlas
*Last updated: 2026-07-15 (M8 · Zeldzame aardmetalen uitgevoerd)*

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
- **Optionele lagen via filter (herbruikbaar patroon, nu 3×):** `layer:"cb"`-flows + `type:"cb"`-nodes op
  `filters.showCentralBanks` (goud); `layer:"exchange"` + `type:"exchange"` op `filters.showExchangeStocks` (koper —
  beursvoorraden); sinds M8 `layer:"recycle"` op `filters.showRecycle` (REE — recycling). Alle default uit, in
  `flows.js`/`markers.js`/`main.js` + `ui.js`-chip + `config.js`-marker; de chip verschijnt alleen als een actieve grondstof
  die data heeft. **Nuance bij recycling (M8):** de node-gate zit op `node.layer==="recycle"` (niet op `type==="recycler"`)
  en `hasRecycle()` detecteert op `f.layer==="recycle"` — zo blijft **koper's always-on recycling** (recyclers zónder `layer`)
  ongemoeid en krijgt alleen REE de toggle/chip. Kopieer de vier filterplekken + config + ui-chip + marker-vorm voor elke nieuwe laag.
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
  **uranium** (M9 — 38 nodes/36 flows, 4-staps kernbrandstofketen met verrijking als flessenhals + Trans-Kaspische route + VVER-lock-in + CANDU-uitzondering),
  **zeldzame aardmetalen** (M8 — 41 nodes/38 flows, magneet-REE NdPr+Dy/Tb: Ganzhou-scheidingstrechter + Dy/Tb-landstroom Myanmar→China over `grens-ruili` + Mountain-Pass-rondreis + NdFeB-waaier + recycling-toggle).
- **Basis:** de 4 overige grondstoffen (nikkel/grafiet/PGM/olie) — laden en renderen, maar zonder
  operators/capaciteiten/route-detail.
- **Volgende kandidaten op basis:** nikkel (runner-up), grafiet, PGM, olie — volgens het brief→bouw-sjabloon.

## Nu (2026-07-15 — M8 · Zeldzame aardmetalen uitgevoerd)

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
- **Ook open (uranium, M9):** visuele bevestiging (LAR-415, Lars) + de uitgestelde militaire-kringloop-toggle (LAR-414).
- **Volgende grondstof:** nikkel (runner-up), grafiet, PGM, olie — volgens dezelfde brief→bouw-flow.
