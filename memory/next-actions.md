# Next actions — Grondstoffen Atlas
*Last updated: 2026-07-15 (M13 · Zilver uitgevoerd — de eerste écht nieuwe grondstof)*

## M13 · Zilver ✅ uitgevoerd (2026-07-15) — LAR-434 t/m 439
**De eerste écht nieuwe grondstof sinds de basis-10** (niet basis→uitgewerkt maar een nieuw `data/silver.js`
(42 nodes / 37 flows / 6 tensions) + `<script>`-tag in `index.html` + zilver-checks in `build-standalone.py`).
De vorm is fundamenteel anders: **géén winnings-trechter** — ~70-75% bijproduct van zink/lood/koper/goud
(aanbod inelastisch), terwijl de concentratie **downstream** zit (Chinese zonnepanelen/PV) → structureel
tekort dat de kluisvoorraden (LBMA/COMEX/SGE) aftapt. Schip+land, **géén nieuw chokepoint** (derde na nikkel/olie).
- [x] Research by-product-winning / solar-vraag inline in `design/zilver.md` (LAR-434/435).
- [x] **Zilver als 11e grondstof geregistreerd** (LAR-436): `data/silver.js` + `<script src="data/silver.js">` na `oil.js` in `index.html` + 5 zilver-sanity-checks in `build-standalone.py`.
- [x] `data/silver.js` uitgewerkt (LAR-437): by-product-mijn-nodes (elk met hoofdmetaal-`note`), convergentie op Peñoles(Mexico)/KGHM(Polen)/Korea/China, solar-pull SGE→Jiangsu, 6 tensions. Keten erts(doré)→raffinaat(good-delivery baar)→product(solar/elektronica/sieraad).
- [x] **Kluis-/beursvoorraden-laag** (LAR-438) = hergebruik van de bestaande exchange-toggle met **0 engine-wijziging** (nikkel-patroon); 3 exchange-nodes (LBMA/COMEX/SGE) + 3 `layer:"exchange"`-aftap-flows; COMEX registered-vs-eligible + 2021-squeeze-nuance. Recycling always-on.
- [x] Verificatie headless (LAR-439, deel): **zilver 85 legs / 0 kapot / 0 straight / 0 warnings**; regressie schoon (andere uitgewerkte grondstoffen 0/0). 2 route-bugs gefixt (VS-raffinage Tacoma→Astoria; China-solar Suzhou→Jiangsu-kust) na empirisch testen. Exchange-chip + blurb + 6 tensions renderen. `build-standalone.py` (+5 zilver-checks) → `atlas-standalone.html` geregenereerd.
- [x] Code-commit `e091848` (repo `main`, lokaal-only, Claude-trailer) — **alléén eigen bestanden** gestaged (parallelle uranium-toggle-sessie op de gedeelde engine-files ongemoeid, sectie J).

**Open (M13 afronden):**
- [ ] **Visuele bevestiging op Netlify/mobiel** (LAR-439, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless). Checken: de diffuse mijn-origin bovenop andermans mijnen (geen winnings-trechter), de convergentie op Peñoles/KGHM/Korea/China, de dikke `product`-boog SGE→Chinese zonnecel-industrie, de India-sieradenstroom, en de kluis-toggle (LBMA/COMEX/SGE) die de aftap onder het tekort toont.

## M12 · PGM ✅ uitgevoerd (2026-07-15) — LAR-440 t/m 448
`data/pgm.js` van "basis" (9/3) → volledig **uitgewerkt** (38 nodes / 41 flows / 6 tensions). De scherpste twee-landen-
concentratie van de atlas, gesplitst over twee metalen: **Zuid-Afrika/Bushveld** = Pt/Rh, **Rusland/Norilsk** = Pd. PGM
**vliegt** (hergebruik goud-air-mode); **géén nieuw chokepoint, géén engine-wijziging** (derde na koper/nikkel).
- [x] Research upstream/downstream inline in `design/pgm.md` (LAR-440/441): ZA ~60% 3E (Pt/Rh), Rusland ~25% (Pd), Zimbabwe/NA/Finland; raffinage (Rustenburg PMR/Springs/Krasnoyarsk/Columbus + westerse huizen JM/BASF/Umicore/Heraeus/Tanaka); autokat + waterstof + recycling.
- [x] **PGM = luchtvracht, géén nieuw chokepoint** (LAR-442): hergebruik van de goud-air-mode (`mode:"air"`, JNB-gateway; "✈ vluchten" via `activeHasAir()`), concentraat/matte over land (Beitbridge/Kanaaltunnel/Baltische bruggen). Het grondstof-eigen "nieuwe element" is bewust géén nieuw element.
- [x] `data/pgm.js` uitgewerkt (LAR-443): 16 mijnen (8 ZA-Bushveld + Norilsk + Zimbabwe + Noord-Amerika + Kevitsa) / 9 raffinage-nodes / JNB-gateway / 8 markten / 4 recyclers. 6 tensions (concentratie, autokat + Pt↔Pd, rodium-spof, palladium/Rusland, waterstof-hedge, Eskom).
- [x] **Recycling-toggle** (LAR-444) = hergebruik van het REE-patroon met **0 engine-wijziging**; 4 recycler-nodes + 5 `layer:"recycle"`-flows (~25% autokat-recycling via de westerse huizen); chip via `hasRecycle()`.
- [x] Verificatie headless (LAR-445, deel): **pgm 49 legs / 0 kapot / 0 straight / 0 degenerate arcs**, regressievrij; lange risico-legs routeren correct; SAMECELL-fix (Japan-recycler uit Tokyo Bay → Kanagawa). `build-standalone.py` (+ 4 PGM-checks) → `atlas-standalone.html` geregenereerd (LAR-446).
- [x] Code-commit `2c4b668` (repo `main`, lokaal-only, Claude-trailer) — **alléén eigen bestanden** gestaged (parallelle zilver-/uranium-toggle-sessie op de gedeelde build-bestanden ongemoeid, sectie J).

**Open (M12 afronden):**
- [ ] **Visuele bevestiging op Netlify/mobiel** (LAR-445, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless). Checken: de dichte Bushveld-kluwen + de zware Norilsk-punt (twee bronnen), de hoge **luchtbogen** (géén zeeroutes) naar de westerse huizen + Azië, de recycling-retourbogen met de toggle aan, het dunne waterstof-draadje naast de autokat-bundel, scheeps-… nee: **vlucht**-voyages voor PGM.
- [ ] **Afwijkingen (Backlog):** LAR-447 (recycling-chip-tooltip generiek maken, nu REE-bewoord — raakt gedeelde `ui.js`), LAR-448 (optionele Pt/Pd-exchange-laag — pure data, hergebruik exchange-toggle).

## M11 · Olie ✅ uitgevoerd (2026-07-15) — LAR-428 t/m 433
`data/oil.js` van "basis" (18/15) → volledig **uitgewerkt** (45 nodes / 46 flows / 6 tensions). Olie's vorm is bewust
ANDERS dan alle eerdere: geen enkele trechter maar het **hele knelpunten-netwerk dat tegelijk oplicht** — Hormuz #1
(15 stromen), Malakka, Taiwan, Suez/Bab, Bosporus, Panama, Kaap (10 knelpunten). **Géén nieuw chokepoint** = het eigen aha.
- [x] Research upstream/downstream inline in `design/olie.md` (LAR-428/429): producenten + reserves≠productie (OPEC+), raffinage/product-trade/petrochemie.
- [x] **3 olie-only navigatie-vaarpunten** (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`) in een gelabeld OIL-blok in `_chokepoints.js` (LAR-430) — houden de VS/Venezuela-routes op het water; geen nieuw knelpunt (olie hergebruikt het hele bestaande net).
- [x] `data/oil.js` uitgewerkt (LAR-431): crude (erts) → raffinage; producten (raffinaat) → markt; petrochemie (product). Drie levende verhalen: Hormuz-bypass-pijpleidingen (Yanbu/Fujairah), Rusland-omleiding 2022→ (Primorsk/Novorossiysk/ESPO-Kozmino/Druzhba → India/China), Amerikaanse schalie-ommekeer (Corpus Christi). Kust-raffinaderijen `coastal:true`.
- [x] Verificatie headless (LAR-433, deel): **olie 210 legs / 0 kapot / 0 straight**; regressie schoon (baseline 5 = lithium 4 + goud 1, olie voegt 0 toe). Knelpunt-gebruik bevestigt het plaatje: Hormuz #1 (15), Malakka (14), Taiwan (12). `build-standalone.py` (+ 4 olie-checks) → `atlas-standalone.html` geregenereerd + zelf geverifieerd (210/0/0).
- [x] Code-commit `1d4ece5` (repo `main`, lokaal-only, Claude-trailer) — alleen mijn eigen bestanden gestaged (parallelle nikkel-sessie ontzien).
- [x] **Optionele SPR-voorraden-toggle** (LAR-432, Done) — gebouwd zodra de nikkel-sessie klaar was en de engine-bestanden vrij waren. `layer:"reserve"` = het **vierde** optionele-laag-patroon (goud-CB, koper-beurs, REE-recycling, olie-reserve), exact het koper-`exchange`-patroon op 5 plekken (config/main/flows/markers/ui) + olie-amber tank-marker. 5 SPR-nodes (US Gulf/China Dalian/Japan Kiire/India Mangalore/IEA-EU Le Havre, `stock` in mln vaten) + 5 vul-flows + tension `oil-t-spr`. Headless: olie 232 legs / 0 kapot / 0 straight; toggle uit=45/46, aan=50/51 (+5/+5); chip "voorraden" alleen bij olie; regressievrij. Commit `86c8c1f`.

**Open (M11 afronden):**
- [ ] **Visuele bevestiging op Netlify/mobiel** (LAR-433, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless). Checken: gloeit Hormuz als dikste knoop, dan Malakka erachter?; de Golf→Azië-bundel als dikste stroom; de twee dunne bypass-pijpleidingen (Yanbu/Fujairah) om Hormuz heen; de dikke Rusland→India-omleiding náást de gekrompen Rusland→Europa-pijl; de VS-exportpijlen uit Corpus Christi; het dunne Venezuela-pijltje (reserves-paradox); de **voorraden-toggle** (SPR-tanks US/China/Japan/India/EU); scheeps-voyages voor olie.

## M10 · Nikkel ✅ uitgevoerd (2026-07-15) — LAR-422 t/m 427
`data/nickel.js` van "basis" (13/4) → volledig **uitgewerkt** (50 nodes / 46 flows / 6 tensions). Schip+land, géén nieuwe
render-modus, **géén nieuw chokepoint** (tweede na koper die volledig op de bestaande routekaart draait).
- [x] Research upstream/downstream inline in `design/nikkel.md` (LAR-422/423): Indonesië-onshoring + class-1/class-2 + shakeout + LME.
- [x] `data/nickel.js` uitgewerkt (LAR-424): Indonesië-onshoring-trechter (erts blijft in het land = korte mijn→smelter-hops), twee nikkels (class-1 batterij vs class-2 roestvrij, HPAL→MHP/matte als brug), prijscrash-shakeout (Nickel West stilgelegd 2024), Filipijns ruw-erts-contrast. Coastal-markten (koper-fix).
- [x] **Beursvoorraden-laag (LME)** = hergebruik van de bestaande exchange-toggle met **0 engine-wijziging** (LAR-425); 4 LME-nodes + 5 `layer:"exchange"`-flows; nuance: alleen class-1 leverbaar + de 2022-squeeze. Recycling always-on.
- [x] Verificatie headless (LAR-426): **nikkel 91 legs (63 zee + 18 land + 10 korte hops) / 0 kapot / 0 straight**; regressie schoon (0 kapot over alle grondstoffen). `build-standalone.py` (+ nikkel-checks) → `atlas-standalone.html` geregenereerd.
- [x] Code-commit `08aa4f5` (repo `main`, lokaal-only, Claude-trailer) — alleen mijn 3 bestanden gestaged (parallelle olie-sessie ontzien).

**Open (M10 afronden):**
- [ ] **Visuele bevestiging op Netlify/mobiel** (LAR-427, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless). Checken: de Indonesische korte-hops-kluwen, de twee waaiers naar China (roestvrij + batterij) door Makassar/Lombok, de Filipijnse ruw-erts-contrastboog, het dunnere "oude wereld"-class-1-web, de scheeps-voyages, en de beursvoorraden-toggle (LME) aan/uit.
- [ ] **Vault push** — de vault-`git pull`/`push` faalde op een netwerkfout; lokaal gecommit, push zodra de verbinding terug is.

## M8 · Zeldzame aardmetalen ✅ uitgevoerd (2026-07-15) — LAR-416 t/m 421
`data/rare-earths.js` van "basis" (9/5) → volledig **uitgewerkt** (41 nodes / 38 flows / 6 tensions), **magneet-REE-framing**
(NdPr + Dy/Tb; `symbol: NdPr`, `unit: kt magneet-REO/jaar`). Schip+land, géén nieuwe render-modus.
- [x] Research → skelet `design/zeldzame-aardmetalen.md` 1-op-1 omgezet (LAR-416/417).
- [x] **Nieuwe grenscorridor `grens-ruili`** (Myanmar→China, `kind:"grensovergang"`) in `_chokepoints.js` — draagt de Dy/Tb-landstroom Kachin→Ganzhou (LAR-418).
- [x] `data/rare-earths.js` uitgewerkt (LAR-419): Ganzhou-scheidingstrechter + Mountain-Pass-rondreis + NdFeB-waaier + Lynas-draadje + EU-draadje.
- [x] **Recycling-toggle** (`layer:"recycle"`, default uit) bedraad over config/main/flows/markers/ui (LAR-420) — het derde optionele-laag-patroon; via `layer` op flows én nodes zodat koper's always-on recyclers ongemoeid blijven.
- [x] Verificatie headless (LAR-421, deel): **rare-earths 90 legs (39 land + 51 zee) / 0 kapot / 0 straight**; regressie schoon (5 kapot = bekende lithium/goud-baseline); toggle-test bevestigd. `build-standalone.py` (+ REE-checks) → `atlas-standalone.html` geregenereerd.

**Open (M8 afronden):**
- [ ] **Visuele bevestiging op Netlify/mobiel** (LAR-421, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless). Checken: convergeren de scheidings-bogen op Zuid-China?, loopt de Dy/Tb-landstroom over Ruili?, zichtbaar de Mountain-Pass-rondreis VS↔China?, de NdFeB-waaier naar EV/wind/defensie?, scheeps-voyages voor REE?, recycling-toggle aan/uit.
- [ ] **Code-commit** — 7 gewijzigde bestanden (`data/rare-earths.js`, `data/_chokepoints.js`, `src/{flows,main,markers,ui}.js`, `build-standalone.py`) + de wrapup-docs; repo lokaal-only (geen remote), branch `main`, Claude-trailer.

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
- [x] **Militaire-kringloop-toggle** (LAR-414, **Done** — commit `6a6d062`, 2026-07-15) — de uitgestelde backlog-toggle afgemaakt zodra de engine-bestanden schoon waren. Het **vijfde** optionele-laag-patroon (`type:"military"`/`layer:"secondary"`/`showMilitary`), exact het olie-reserve-patroon in 5 plekken. 4 military-nodes (down-blend Rosatom/HEU, tails, US DOE, US reserve) + 5 `secondary`-flows (o.a. Megatons-to-Megawatts Rusland→VS) + tension `u-t-military`. Headless: uranium 60 legs / 0 kapot / 0 straight; toggle uit→aan +4/+5; chip alleen bij uranium.

## Verderop — volgende grondstof (grafiet)
**Tien uitgewerkt** (lithium, kobalt, goud, koper, uranium, REE, nikkel, olie, **PGM (M12)**, **zilver (M13, nieuwe 11e)**); nog op "basis": **grafiet** — nu de énige, het laatste van de basis-10.
Zelfde brief→bouw-flow: `design/_brief-template.md` → `design/<grondstof>.md` →
`data/<grondstof>.js` van "basis" → "uitgewerkt" → headless legs-check → build → wrapup.

**Los, klein:** de uranium-restpunt LAR-415 (visuele bevestiging Netlify/mobiel, Lars) — LAR-414 (militaire-kringloop-toggle)
is nu **Done**. Verder het opruimen van de bureaublad-originelen (`atlas-lithium-kobalt.html` + `globe-oud`) ná Lars' visuele
bevestiging. `atlas-standalone.html` blijft gitignored (gegenereerd); repo blijft lokaal-only (GitHub-remote optioneel).
