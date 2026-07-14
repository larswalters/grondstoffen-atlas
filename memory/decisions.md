# Decisions — Grondstoffen Atlas
*Last updated: 2026-07-14*

Vastgelegde keuzes (nieuwste boven). Elk: besluit + korte reden.

## Architectuur
- **Geen bundler.** Losse globals-bestanden met vaste laadvolgorde via `<script>`-tags in `index.html`.
  Reden: eenvoud, direct te openen/deployen, geen buildstap; standalone single-file voor mobiel mogelijk.
- **Eén bestand per grondstof** in `data/` (`_registry.js` + `_chokepoints.js` + `<grondstof>.js`).
  Reden: elke keten geïsoleerd uit te werken en te reviewen.
- **Lithium = sjabloon.** `data/lithium.js` (34 knopen, 31 stromen) is de referentie voor alle volgende
  grondstoffen. Reden: één consistent schema (knopen/stromen/operators/capaciteiten/transportmodi/NL-annotaties).

## Routering & rendering
- **Echte routes via A\*** over een 1440×720 land/zee-raster (0,25°/cel uit `LAND_POLYS`) i.p.v. bogen
  door de lucht. Reden: het hele punt van de atlas is dat routes fysiek kloppen (schepen over water).
- **Knelpunten als water forceren** (`openRadiusDeg: 1.2`). Reden: in een 0,25°-raster slibben smalle
  straten (Lombok, Makassar) dicht; forceren houdt ze begaanbaar — en ze zijn juist het verhaal.
- **Gewogen A\*** (`heuristicWeight: 1.35`, `maxExpansions: 1500000`). Reden: lange oceaanroutes (10.000+ km)
  raakten de zoeklimiet en vielen terug op rechte lijnen dwars over eilandengroepen. Suboptimaal-maar-
  gevonden > rechte lijn door de Salomonseilanden.
- **`LAND_LINKS`** (Øresund, Storebælt, Fehmarn, Kanaaltunnel, Bosporus) als land forceren. Reden: anders
  kruipen spoorroutes helemaal om de Baltische staten/Finland heen.
- **Vaarbanen** (`laneShape(t)`): zijwaartse verschuiving nul bij elk anker, maximaal ertussenin. Reden:
  parallelle stromen los volgbaar onderweg, maar zichtbaar samengeknepen bij een knelpunt.
- **Schaal op afstand-tot-oppervlak** (`scaleFor()`, `d = camera.z - R`), niet op camerastand. Reden:
  de kernbug waarom inzoomen niets opleverde (factor-5-verschil tussen z-delta en oppervlakte-afstand).
- **Kaderloze labels + botsingsdetectie** (prioriteit `tier × 100 − share`). Reden: achtergrondkaders
  dekten de kaart af; overlappende labels moesten op prioriteit verdwijnen.
- **Autorotatie permanent uit na eerste interactie** (`autoRotateResumeMs: 0`). Reden: een bol die
  onder je handen wegdraait tijdens inzoomen is onbruikbaar.
- **Dover + St. Lawrence als knelpunt open geforceerd** (M5, 2026-07-14) — zelfde patroon als Lombok/Malakka;
  loste de kobaltroutes Cuba→Canada + Europa→Amerika op. Regressie: 0 kapotte routes over alle stromen.
- **Tegelnaad / blue-marble-doorprik opgelost** (M5, 2026-07-14) met een **shell-laag** (hele bol grove tegels)
  + een scherpe **detailpatch**; geverifieerd dat de blue-marble nergens meer doorprikt. Visueel niet met
  screenshot bevestigd (WebGL-capture liep vast) — numeriek/geometrisch getoetst.

## Inhoud
- **Deploy via Netlify** drag-and-drop van de `atlas`-map (+ standalone HTML voor mobiel).
- UI-teksten/annotaties **Nederlandstalig**.

## Goud — ontwerpbesluiten (op papier, 2026-07-14; nog niet gebouwd)
- **Principe:** we vertellen geen verhaal, we modelleren de werkelijkheid nauwkeurig; het plaatje vertelt
  zichzelf. Voor goud is die werkelijkheid anders van vorm dan lithium → automatisch een ander plaatje.
- **Alle lagen meenemen:** mijn → raffinage → handels-/kluishub → consumptie → centrale banken → recycling.
- **Luchtroutes als aparte modus**, parallel aan de bestaande `routes` ↔ `hemelsbreed`-toggle:
  - `hemelsbreed` = directe great-circle-boog (opgetild, hoogte ∝ afstand).
  - `routes` = **echte luchtroutes via luchthaven-nodes** (ZRH, LHR, JFK, HKG, DXB, SIN, DEL/BOM, PVG,
    FRA, IST, JNB, PER, ...), met **weg/spoor-legs** voor de korte Europese hops (Ticino↔Zürich,
    Londen↔Frankfurt) — hergebruikt de bestaande land-A\*.
  - Zee-A\* speelt voor goud vrijwel geen rol.
- **Voyages-playback hergebruiken:** i.p.v. schepen bewegen **lichtpuntjes/vliegtuig-glyphs** over de
  luchtlijnen, met teller "hoeveel goud / hoeveel zendingen" (zelfde `voyages.js`-motor, ander glyph + pad).
- **Great-circle-boog is hier juist correct** (voor lithium was hij "fout"): goud vliegt echt die boog,
  dus de boog klopt met de werkelijkheid — consistent met het plaatje=werkelijkheid-principe.
- **Zwitserland (Ticino) = de visuele trechter** — goud-equivalent van de China-lithium-knijp
  (Valcambi/PAMP/Argor-Heraeus + Metalor). "Knelpunten" bij goud zijn institutioneel: Swiss refining,
  London/NY-kluizen, China's eenrichtings-import.
- **Centrale banken als optionele (toggle-bare) laag:** toont voorraden (node-grootte) én de huidige
  inkoop-/repatriëringsstromen. CB-"koop" is vaak titeloverdracht ín een kluis; sommigen repatriëren wél
  (Polen 2019, Duitsland 2013–17, India 2024) → mix van "node groeit" + repatriëringsvluchten.

## Goud — subkeuzes bevestigd (2026-07-14)
- **Luchthaven-granulariteit:** kleine/artisanale mijnen clusteren naar regionale gateway-luchthavens
  (bv. West-Afrika → Accra/Dubai); niet per mijn een eigen luchthaven. Truthful + node-aantal beheersbaar.
- **Volumes:** per stroom een grofweg ton/jaar-getal verzamelen (research volgende sessie) om bogen +
  voyages-puntjes te schalen en de teller te vullen.

## Architectuur-besluit (2026-07-14): MODULAIR = bron van waarheid
- Lars koos **modulair** als bron van waarheid; de single-file wordt een **gegenereerde deploy-build**
  (mobiel/Netlify), zoals `atlas-standalone.html` in M0. Reden: schoonste per-grondstof-workflow (`data/<x>.js`),
  beste voor git-diffs + agent-edits, eert de M0-splitsing.
- **Gevolg:** de modulaire code in `globe-oud\grondstoffen-atlas-v2\atlas\` wordt de **werkbasis** (→ verplaatsen
  naar `Projects\General\grondstoffen-atlas` + `git init`). De M5-fixes (Dover/St.Lawrence-knelpunten + shell-laag/
  detailpatch tegels) moeten **eenmalig uit de single-file `atlas-lithium-kobalt.html` geport** worden. De single-file
  blijft referentie tot dat gedaan + visueel bevestigd is.

## Nog te beslissen (open)
- Migratie modulaire code (globe-oud) → `Projects\General\grondstoffen-atlas` + `git init` (volgende sessie).
- `atlas-lithium-kobalt.html` / `globe-oud`-restanten opruimen — pas ná M5-port + visuele bevestiging.
