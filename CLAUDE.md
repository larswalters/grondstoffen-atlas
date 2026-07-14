# Grondstoffen Atlas — project spec

*Categorie: General · Linear-project: "Grondstoffen Atlas" (team Lars / LAR) · Laatst bijgewerkt: 2026-07-14*

> **STATUS VAN DEZE MAP (2026-07-14):** dit is voorlopig alleen de **brain-laag** (spec + `memory/` + `design/`).
> De werkende code staat op het bureaublad (zie sectie C). **M5 is af** (aparte CC-sessie; geverifieerd
> numeriek/geometrisch, nog niet met screenshot). **Beslist (2026-07-14): modulair = bron van waarheid**
> (single-file = gegenereerde build). Open: modulaire code (globe-oud) → deze map + `git init`, en de M5-fixes
> eenmalig porten uit de single-file. Tot dan: deze map niet als code-root gebruiken.

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
- **Huidige code-locatie (bureaublad):** `C:\Users\lars\Desktop\globe\atlas-lithium-kobalt.html` — **single-file**
  (hierin is M5 gedaan, ~138 KB). De **oude modulaire versie** staat als backup in
  `C:\Users\lars\Desktop\globe-oud\grondstoffen-atlas-v2\atlas\` (config.js/_registry.js/src/…), plus nog oudere
  bestanden in `C:\Users\lars\Desktop\globe-oud\files\`.
- **✅ Beslist (2026-07-14): modulair = bron van waarheid** (single-file = gegenereerde build). De modulaire code
  in `globe-oud` wordt de werkbasis (→ deze map). De M5-fixes moeten nog uit de single-file geport worden.
- **Deploy:** Netlify, drag-and-drop (single-file is daarvoor juist handig).
- **Bestandsindeling (modulaire opzet — in `globe-oud`):**
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
4. [ ] Modulaire code (`globe-oud`) **verplaatsen** naar deze map + `git init` (+ evt. GitHub-repo) = werkbasis.
5. [ ] **M5-fixes porten** uit de single-file naar de modulaire code + verifiëren (regressie + visueel Netlify/mobiel).
6. [ ] Daarna: goud als eerste nieuw uitgewerkte grondstof (research → `data/goud.js`).
