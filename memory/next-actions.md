# Next actions — Grondstoffen Atlas
*Last updated: 2026-07-14*

## M5 ✅ afgerond + geverifieerd (2026-07-14)
- LAR-393/394/395/396 → **Done**. Aanpak: Dover + St. Lawrence als knelpunt open geforceerd (kobaltroutes);
  shell-laag + detailpatch (tegelnaad). Regressie 0 kapotte routes. ⚠️ nog niet met screenshot bevestigd.

## Onboarding-restpunten
- [x] Wiki-pagina + `now.md` + eerste Pinecone-gist (2026-07-14).
- [x] **Beslist: modulair = bron van waarheid** (single-file = gegenereerde build). Zie decisions.md.
- [ ] **Modulaire code (`globe-oud\grondstoffen-atlas-v2\atlas`) → `Projects\General\grondstoffen-atlas`** verplaatsen + `git init` (+ evt. GitHub-repo). Dit wordt de werkbasis.
- [ ] **M5-fixes porten** uit `atlas-lithium-kobalt.html` naar de modulaire code: Dover/St.Lawrence-knelpunten in `_chokepoints.js`; shell-laag + detailpatch in de tegel/basemap-laag. Verifiëren (regressie 0 kapotte routes) + visueel op Netlify/mobiel.
- [ ] `atlas-lithium-kobalt.html` / `globe-oud`-restanten opruimen zodra M5 geport + visueel bevestigd.

## Daarna — inhoudelijk: GOUD (Lars' focus) — ontwerp op papier
Ontwerprichting vastgelegd 2026-07-14 (zie decisions.md): volle keten, alle lagen, luchtroutes als aparte modus.
**Linear: milestone `M6 · Goud` — LAR-397 t/m LAR-403** (research → dev → verificatie), staat klaar in de backlog.
- LAR-397 research mijn+raffinage · LAR-398 research hubs/consumptie/CB · LAR-399 luchtroute-modus · LAR-400 voyages-luchtpuntjes · LAR-401 data/goud.js · LAR-402 CB-laag toggle · LAR-403 verificatie+build.

Nodes/lagen om uit te werken (mijn → raffinage → hub/kluis → consumptie → centrale banken → recycling):
- [ ] **Mijnbouw** (wijd verspreid, géén trechter): China, Rusland, Australië, Canada, VS, Kazachstan, Peru,
      Mexico, Ghana, Indonesië (Grasberg), Zuid-Afrika, West-Afrika (Mali/Burkina, artisanaal), Uzbekistan, Brazilië, PNG...
- [ ] **Raffinage**: Zwitserland/Ticino (Valcambi, PAMP, Argor-Heraeus, Metalor) = hoofdtrechter;
      + Perth Mint, India (MMTC-PAMP), Dubai, China-intern, Rand Refinery, Royal Canadian Mint.
- [ ] **Handels-/kluishubs**: Londen (LBMA/BoE), New York (COMEX + NY Fed), Zürich, Shanghai (SGE),
      Dubai, Singapore, Hongkong — inclusief onderlinge stromen (Londen↔Zürich↔NY).
- [ ] **Consumptie**: India + China (sieraden), Midden-Oosten, Turkije; tech (Japan/Korea/Taiwan).
- [ ] **Centrale banken** (optionele laag): voorraden (Fort Knox/NY Fed, BoE, Frankfurt, ...) + huidige
      inkopers (Polen, China, Turkije, India, Kazachstan, Tsjechië, Singapore; Rusland absorbeert eigen mijn).
- [ ] **Recycling**: schroot → raffinage (India, Italië, China, Midden-Oosten).
- [ ] **Luchthaven-nodes**: ZRH, LHR, JFK, HKG, DXB, SIN, DEL/BOM, PVG, FRA, IST, JNB, PER, ACC...

**Vul de brief in:** research (LAR-397/398) levert `data/goud.md` op volgens `design/_brief-template.md`
(alle nodes + stromen), waarna LAR-401 dat 1-op-1 naar `data/goud.js` omzet.

Databehoefte (voor de uitwerking):
- [ ] Volumes/capaciteiten (t/jr) per stroom om bogen + voyages-puntjes te schalen en de teller te vullen.
- [ ] Coördinaten mijnen/raffinaderijen/luchthavens (lat/lon, west negatief — dubbelcheck).

Bouwstappen (na ontwerp + na M5):
- [ ] **Air-route path-generator** (great-circle, opgetilde boog) als derde route-modus naast zee-A\* en land-A\*.
- [ ] `voyages.js` uitbreiden: lichtpuntjes/vliegtuig-glyph over luchtlijnen.
- [ ] Ontwerp omzetten naar `data/goud.js` volgens het lithium-schema + registreren in `_registry.js`.
- [ ] Verifiëren in de atlas (routes plausibel, labels, trechter Ticino zichtbaar) → wrapup.
