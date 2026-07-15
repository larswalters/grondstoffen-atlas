# Current strategy — Grondstoffen Atlas
*Last updated: 2026-07-15 (M13 · Zilver uitgevoerd — de eerste écht nieuwe grondstof)*

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
  **PGM** (M12 — 38 nodes/41 flows, de scherpste twee-landen/twee-metalen-concentratie: Zuid-Afrika/Bushveld = Pt/Rh + Rusland/Norilsk = Pd; **luchtvracht** (hergebruik goud-air-mode, JNB-gateway) — concentraat/matte over land; géén nieuw chokepoint; recycling-toggle hergebruikt van REE met 0 engine-wijziging; 6 tensions incl. autokat-leiband + Pt↔Pd-substitutie, rodium-spof, waterstof-hedge, Eskom-stroomcrisis).
- **Basis:** grafiet — nu de **énige** nog op basis (het laatste van de basis-10); laadt en rendert, maar zonder operators/capaciteiten/route-detail.
- **Volgende kandidaat op basis:** grafiet — volgens het brief→bouw-sjabloon.

## Nu (2026-07-15 — M13 · Zilver uitgevoerd)

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
