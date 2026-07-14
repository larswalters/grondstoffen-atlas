# Next actions — Grondstoffen Atlas
*Last updated: 2026-07-14 (na code-onboarding + M5-port)*

## Onboarding ✅ afgerond (2026-07-14)
- [x] Wiki-pagina + `now.md` + eerste Pinecone-gist.
- [x] **Beslist: modulair = bron van waarheid** (single-file = gegenereerde build). Zie decisions.md.
- [x] **Modulaire code → `Projects\General\grondstoffen-atlas` + `git init`** (2 commits `b9d69fa`, `177bc6b`). Werkbasis staat nu hier.
- [x] **M5-fixes geport** uit `atlas-lithium-kobalt.html`: Dover/Deense Straten/Kasumbalesa/Saint-Laurent in `_chokepoints.js`; grensovergang-logica in `searoute.js`/`flows.js`; labels in `ui.js`; tegelnaad-fix zat al in `tiles.js`. `cobalt.js` → volledig uitgewerkt. Seto-brug voor Niihama→Osaka. **Geverifieerd headless: 214 legs, 0 kapotte routes.**

## Openstaande restpunten (klein)
- [ ] **Visuele bevestiging** op Netlify/mobiel (screenshot lukte niet in de preview → WebGL-time-out). Zit al in LAR-403.
- [ ] `atlas-lithium-kobalt.html` / `globe-oud`-restanten opruimen — pas ná die visuele bevestiging.
- [ ] Optioneel: **GitHub-remote** voor de nieuwe repo (nu lokaal-only).

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
