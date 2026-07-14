# Next actions — Grondstoffen Atlas
*Last updated: 2026-07-14 (M6 · Goud uitgevoerd; M7 · Koper staat klaar)*

## M6 · Goud ✅ uitgevoerd (2026-07-14)
- [x] Research → brief `data/goud.md` (LAR-397/398).
- [x] Luchtroute-modus: great-circle 3e route-type in `flows.js` + marker-types airport/hub/cb/recycler (LAR-399).
- [x] `voyages.js` uitgebreid naar lucht + resource-bewuste teller "✈ vluchten" (LAR-400).
- [x] `data/goud.js` (73 nodes/48 flows, Ticino-trechter) + registratie in `index.html` (LAR-401).
- [x] Centrale-bank-laag als optionele toggle, default uit (LAR-402).
- [x] Verificatie headless: 371 legs / 0 kapot over alle 10 grondstoffen, regressievrij (deel LAR-403).
- [x] `build-standalone.py` → `atlas-standalone.html` (gegenereerde single-file build).

## LAR-403 ✅ afgerond (2026-07-14) — M6 volledig af
- [x] **Visuele bevestiging** — Lars bekeek de build thuis in de browser: "ziet er cool uit, geen aanmerkingen".
      LAR-403 → Done; alle M6-issues (LAR-397 t/m 403) Done. Lars zet `atlas-standalone.html` zelf op Netlify.
- [ ] Nog te doen (klein): bureaublad-restanten opruimen (`atlas-lithium-kobalt.html`, `globe-oud`) — nu unblocked.

## Openstaand — project-hygiëne
- [ ] **Project-repo committen** — goud.js/goud.md/edits/build-standalone.py staan dirty. Code-commit los van de
      wrapup-docs, op Lars' seintje (agent-trailer). Overweeg `atlas-standalone.html` in `.gitignore` (gegenereerd, 1,4 MB).
- [ ] Optioneel: **GitHub-remote** voor de repo (nu lokaal-only).

## Optionele verfijningen goud (later, niet-blokkerend)
- [ ] Per-leg touch-down bij hubs i.p.v. één boog over de via-punten (nu bulge't de boog in het midden).
- [ ] Air-specifieke voyage-snelheid/`ktPerShipment` (nu ship-tempo uit `config.time`).
- [ ] Eigen CB voor Oezbekistan/Kazachstan; evt. meer mijn-/consumptie-nodes (Lars: "extra nodes kan altijd").

## Daarna — inhoudelijk: KOPER (schip + land, na goud)
**Linear: milestone `M7 · Koper` — LAR-404 t/m LAR-409** (opgezet 2026-07-14), staat klaar in de backlog.
Ontwerp-skelet ligt in `design/koper.md` (volgens `design/_brief-template.md`); research (LAR-404/405) vult het aan.
- LAR-404 research mijn+smelting · LAR-405 research consumptie/schroot/beursvoorraden · LAR-406 concentraat-vs-kathode + Copperbelt-landroutes · LAR-407 data/copper.js · LAR-408 beursvoorraden-toggle · LAR-409 verificatie+build.

**Structuur = goud-skelet, aangepast aan een schip-grondstof:** géén luchtroute-modus/air-voyages (koper
hergebruikt de bestaande zee-A\*/land-A\*-routes uit M3 + de scheeps-voyages uit M4). Kern-"aha" = de
**China-smelttrechter** (~50% wereldraffinage): Andes-concentraat (Chili/Peru) over de Stille Oceaan → Chinese
smelters. Tweede trechter = de **Afrikaanse Copperbelt** (DRC/Zambia → Durban/Dar es Salaam over land, als
kathode). `data/copper.js` gaat van "basis" → "uitgewerkt".

**Herbruikbaar uit M6 voor koper:** de optionele-laag-toggle (nu CB; voor koper de LME/COMEX/SHFE-beursvoorraden,
LAR-408) volgt exact hetzelfde `layer:"..."`-filterpatroon; de brief→bouw-flow is identiek.

## Verderop — M8 · Zeldzame aardmetalen / magneet-REE (ontwerp-skelet klaar, ná koper)
**Ontwerp-skelet ligt in `design/zeldzame-aardmetalen.md`** (2026-07-14, herzien 2026-07-15 → **optie 2:
scherpe magneet-REE-framing**, NdPr + Dy/Tb i.p.v. alle 17 elementen) → data-doel `data/rare-earths.js` van
"basis" → "uitgewerkt" (metadata sharpenen: `name`/`symbol=NdPr`/`unit=kt magneet-REO/blurb`, id blijft
`rare-earths`). **Linear-milestone `M8 · Zeldzame aardmetalen` + issues nog aan te maken** (spiegelt M6/M7:
research × 2 → NdPr/Dy-onderscheid + Myanmar-grenscorridor → data-file → recycling-toggle → verificatie).
LAR-nummers volgen bij aanmaken.

**Kern-"aha" (distinct van lithium/koper):** winning breed verspreid, maar scheiding van NdPr/Dy uit het
gemengde erts ~85–90% in Zuid-China (Ganzhou) én NdFeB-magneten ~90%+ China. Drie nieuwe elementen voor de
atlas: (1) **Dy/Tb-landstroom over de grens Myanmar→China** (Kachin → Ruili — nieuw `grens-*`-knelpunt, analoog
aan Kasumbalesa), (2) de **Mountain Pass-rondreis** (VS delft → China scheidt → terug), (3) de
**NdFeB-magneet-flessenhals** downstream. **Hergebruikt schip+land — géén nieuwe render-modus** (net als koper);
recycling-laag = het CB/beursvoorraden-toggle-equivalent. Magneet = stage `product` (de eerdere "4e stage?"-vraag
vervalt in deze framing).
