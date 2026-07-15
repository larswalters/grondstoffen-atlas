# Next actions — Grondstoffen Atlas
*Last updated: 2026-07-15 (M9 · Uranium uitgevoerd; M8 · Zeldzame aardmetalen in voorbereiding)*

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

## M7 · Koper ✅ uitgevoerd (2026-07-14) — LAR-404 t/m 409
`data/copper.js` van "basis" (13/5) → volledig **uitgewerkt** (69 nodes / 50 flows / 5 tensions, goud-niveau).
- [x] Andes-concentraat-trechter (Escondida/Collahuasi/Cerro Verde/Antamina/Las Bambas → Chinese smelters over de Stille Oceaan, `stage: erts`) = de koper-"aha".
- [x] Copperbelt-**kathode** (Tenke/Kolwezi/Kansanshi/Kamoa, SX-EW `stage: raffinaat`) over land via `grens-kasumbalesa` → Durban/Dar/Lobito/Walvis, dan per schip (kobalt-patroon: land-flow mijn→haven + aparte ship-flow haven→markt).
- [x] Concentraat vs. SX-EW-kathode via `stage`; recycling **always-on** (niet achter de toggle).
- [x] **Beursvoorraden-laag** (LAR-408): optionele toggle `type:"exchange"`/`layer:"exchange"` (LME/SHFE/COMEX), default uit — zelfde patroon als de goud-CB-laag; chip "beursvoorraden", koperkleurige spoel-marker (grootte ∝ √voorraad).
- [x] Verificatie headless (LAR-409): koper **145 legs / 0 kapot**; regressie **388 legs / 0 kapot** over alle 10 grondstoffen; toggle +6 nodes/+7 flows; geen console-errors. 4 route-bugs onderweg gefixt (markt-kustpunten + Korea→Japan als ship + beursmagazijnen coastal). `build-standalone.py` (checks + koper) → `atlas-standalone.html` geregenereerd.

**Open (M7 afronden, niet-code):**
- [ ] **Visuele bevestiging op Netlify/mobiel** — alleen Lars (WebGL-screenshot lukt niet headless). Checken: Andes→China-concentraatbundel, Copperbelt-kathode over land, beursvoorraden-toggle + spoel-markers, scheeps-voyages voor koper. (= laatste open stuk van LAR-409.)
- [x] **Code-commit** — gecommit op `main` (lokaal-only): code `233b882` + wrapup-docs `7e46092` (twee aparte commits, Claude-trailer).
- [x] **Linear** LAR-404 t/m 409 → Done (via Linear-MCP).

**Herbruikbaar uit M6+M7:** de optionele-laag-toggle (CB bij goud, beursvoorraden bij koper) is een vast, herbruikbaar
`layer:"..."`-filterpatroon (vier filterplekken + config-size + ui-chip + marker-vorm); het landcorridor-patroon
(Kasumbalesa) = land-flow mijn→haven + aparte ship-flow. **Elke ship-leg moet op een kustpunt (`port`/`coastal`/`wp-`) landen.**

## M9 · Uranium ✅ uitgevoerd (2026-07-15) — LAR-410 t/m 415
`data/uranium.js` van "basis" (9/2) → volledig **uitgewerkt** (38 nodes / 36 flows / 6 tensions). Eerste grondstof met een
bewust *andere vorm*: een **4-staps kernbrandstofketen** (winning → conversie → verrijking → splijtstof → reactor), gemapt
op de 3 bestaande stages, met de **verrijking (~44% Rusland) als `raffinaat`-flessenhals**.
- [x] Ontwerp-skelet `design/uranium.md` (LAR-410/411 research) + commit `d016ab8`.
- [x] **Kaspische oversteek + Dardanellen** (LAR-412): 3 vaarpunten (`wp-kaspisch-n/-m/-z`) + `wp-dardanellen` in `_chokepoints.js` — forceren de Aktau↔Bakoe-watercorridor (ingesloten zee) + de Zwarte-Zee-uitgang. Alleen uranium gebruikt ze.
- [x] `data/uranium.js` (LAR-413): 4-staps keten + Trans-Kaspische route (om Rusland heen) + VVER-lock-in + CANDU-uitzondering. Commit `76c0333`.
- [x] Verificatie headless (LAR-415, deel): uranium **54 legs / 0 kapot** (20 zee + 34 land, 0 straight → de Kaspische oversteek routeert écht over water); regressievrij (5 nulls = bekende `degDist:0` baseline-hops); structuurcheck groen.

**Open (M9 afronden):**
- [ ] **Visuele bevestiging op Netlify/mobiel** (LAR-415, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless). Checken: verrijkings-flessenhals (dun ringetje nodes, Rusland dikst), de twee Kazachstan-routes, de VVER-lock-in-lijn, de CANDU-uitzondering, scheeps-voyages voor uranium.
- [ ] **Militaire-kringloop-toggle** (LAR-414, Backlog) — bewust uitgesteld: de optionele `layer:"secondary"`-laag (down-blended wapen-HEU / strategische voorraden) vereist code in `flows/ui/main/config` (destijds dirty door de M8-sessie). Oppakken zodra de M8-code gecommit is; het `layer:"..."`-filterpatroon is al vast (CB → exchange → secondary).

## Verderop — M8 · Zeldzame aardmetalen / magneet-REE (ontwerp-skelet klaar, ná koper)
**Ontwerp-skelet ligt in `design/zeldzame-aardmetalen.md`** (2026-07-14, herzien 2026-07-15 → **optie 2:
scherpe magneet-REE-framing**, NdPr + Dy/Tb i.p.v. alle 17 elementen) → data-doel `data/rare-earths.js` van
"basis" → "uitgewerkt" (metadata sharpenen: `name`/`symbol=NdPr`/`unit=kt magneet-REO/blurb`, id blijft
`rare-earths`). **Linear-milestone `M8 · Zeldzame aardmetalen` + issues LAR-416 t/m 421 aangemaakt** (Backlog;
spiegelt M6/M7/M9: research × 2 → Myanmar-grenscorridor → data-file → recycling-toggle → verificatie).

**Kern-"aha" (distinct van lithium/koper):** winning breed verspreid, maar scheiding van NdPr/Dy uit het
gemengde erts ~85–90% in Zuid-China (Ganzhou) én NdFeB-magneten ~90%+ China. Drie nieuwe elementen voor de
atlas: (1) **Dy/Tb-landstroom over de grens Myanmar→China** (Kachin → Ruili — nieuw `grens-*`-knelpunt, analoog
aan Kasumbalesa), (2) de **Mountain Pass-rondreis** (VS delft → China scheidt → terug), (3) de
**NdFeB-magneet-flessenhals** downstream. **Hergebruikt schip+land — géén nieuwe render-modus** (net als koper);
recycling-laag = het CB/beursvoorraden-toggle-equivalent. Magneet = stage `product` (de eerdere "4e stage?"-vraag
vervalt in deze framing).
