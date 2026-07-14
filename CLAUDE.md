# Grondstoffen Atlas — project spec

*Categorie: General · Linear-project: "Grondstoffen Atlas" (team Lars / LAR) · Laatst bijgewerkt: 2026-07-15 (M8 zeldzame aardmetalen voorbereid; M7 · Koper uitgevoerd)*

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
8. [~] **Volgende grondstoffen voorbereid (ontwerp-skelet, nog niet gebouwd):** **M8 · Zeldzame aardmetalen** — `design/zeldzame-aardmetalen.md`, magneet-REE-framing (NdPr+Dy/Tb, optie 2), gecommit (`1a4e808` + reframe `faf0288`). **M9 · Uranium** — `design/uranium.md` (parallelle sessie, `d016ab8`). Linear-milestones M8/M9 nog aan te maken; bouwen ná koper's visuele bevestiging.
