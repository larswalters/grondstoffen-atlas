# Session summaries — Grondstoffen Atlas
*Newest first.*

## 2026-07-15 (sessie 11) — M12 · PGM uitgevoerd (data/pgm.js, twee landen/twee metalen + luchtvracht)
- **Taak (Lars):** "begin met het uitwerken van PMG voor de grondstoffen atlas zoals de rest ook is uitgewerkt en volgens hetzelfde patroon … als er dingen anders moeten maak daar dan aparte issues van." PMG = **PGM** (platinagroepmetalen); runbook sectie I gevolgd, **goud** als model (luchtvracht).
- **De vorm (het aha):** de scherpste twee-landen-concentratie van de atlas, gesplitst over **twee metalen**: **Zuid-Afrika/Bushveld** (~70% Pt + ~80% Rh, dichte kluwen schachtmijnen bij Rustenburg + Noord-/Oostrand) en **Rusland/Norilsk** (~40% Pd, Ni-Cu-bijproduct). Een schok in het ene land raakt een *ander* metaal dan een schok in het andere.
- **Gebouwd:** `data/pgm.js` van "basis" (9/3) → **uitgewerkt** (38 nodes / 41 flows / 6 tensions) + brief `design/pgm.md`. Keten `erts` (concentraat/matte, land) → `raffinaat` (geraffineerd metaal, **lucht**) → `product` (autokat/brandstofcel/sieraad/industrie). 6 tensions: twee-landen-concentratie, autokat-leiband + Pt↔Pd-substitutie, rodium-spof (~$29k/oz 2021), palladium/Rusland-sanctie, waterstof-hedge (Pt/Ir PEM-elektrolyse), Eskom-stroomcrisis.
- **Maximaal hergebruik, 0 engine-wijziging:** PGM **vliegt** (per kilo even waardevol als goud) → hergebruik van de **goud-air-mode** (`mode:"air"`, JNB-gateway; tijdlijn toont automatisch "✈ vluchten" via `activeHasAir()`); concentraat/matte over land. **Géén nieuw chokepoint** (derde na koper/nikkel). **Recycling** (~25%, autokat via dezelfde westerse huizen JM/BASF/Umicore/Heraeus/Tanaka) als **optionele toggle** (`layer:"recycle"`, hergebruik van het REE-patroon, 0 engine-wijziging; chip via `hasRecycle()`).
- **Verificatie (headless, poort 8732):** pgm **49 legs / 0 kapot / 0 straight / 0 degenerate arcs**, regressievrij; de lange risico-legs (Zimbabwe→ZA via Beitbridge, Norilsk→Krasnoyarsk, Kevitsa→Umicore om de Oostzee, VK→EU via de Kanaaltunnel) routeren correct; één SAMECELL-collision (Japan-recycler in Tokyo Bay → snapte naar Tanaka's cel) gefixt door de node naar Kanagawa te verplaatsen. Recycle-toggle (36→41 flows) + air-voyage-noun bevestigd.
- **Afwijkingen → aparte issues (op Lars' verzoek):** LAR-446 (single-file build + `atlas-standalone.html` regenereren, tijdelijk uitgesteld i.v.m. de parallelle zilver-sessie → **nu Done**), LAR-447 (recycling-chip-tooltip nog REE-bewoord "<5%", onjuist voor PGM ~25%, raakt `ui.js`), LAR-448 (optionele Pt/Pd-exchange-laag — pure data, bewust niet gebouwd; één toggle per grondstof).
- **Coördinatie (sectie J):** gebouwd náást de parallelle **M13-zilver-sessie** (+ een uranium-toggle-sessie) die de gedeelde `build-standalone.py`/`index.html`/`config.js` dirty hadden. PGM raakt geen engine-bestanden → alleen `data/pgm.js` + `design/pgm.md` gecommit (`2c4b668`); de build + `now.md`/project-sync bewust uitgesteld tot de tree schoon was, daarna afgemaakt.
- **Afgerond:** Linear **M12 · PGM** + LAR-440..448 (5 Done + 445 In Progress = visuele bevestiging Lars; 446 Done na de build; 447/448 Backlog). Vault-wrapup gepusht (`278dddd` conflictvrije delen + deze sync). **Rest = visuele bevestiging Netlify/mobiel (LAR-445, Lars).**

## 2026-07-15 (sessie 10) — M13 · Zilver uitgevoerd (data/silver.js, de eerste écht nieuwe grondstof)
- **Taak (Lars):** "begin met het uitwerken van zilver voor de grondstoffen atlas zoals de rest, volgens hetzelfde patroon; als er dingen anders moeten maak daar aparte issues van — oriënteren, de brief, milestone in Linear, daarna uitvoeren." Runbook sectie I gevolgd; in één sessie gebouwd + geverifieerd + wrapup.
- **Het grote verschil:** zilver is de **eerste écht nieuwe grondstof** sinds de basis-10 (niet basis→uitgewerkt). Nieuw `data/silver.js` (42 nodes / 37 flows / 6 tensions) + brief `design/zilver.md` + `<script src="data/silver.js">` in `index.html` + 5 zilver-checks in `build-standalone.py`. Dit "anders"-punt bewust als eigen Linear-issue (LAR-436).
- **De vorm (het aha) — fundamenteel anders:** zilver heeft géén enkel geografisch knelpunt. De knijp is tweezijdig en structureel: (1) **aanbod-inelasticiteit** — ~70-75% is **bijproduct** van zink/lood/koper/goud (Mexico #1, Peru, China, KGHM-koper Polen, Chili, Australië, Bolivia, Kazachstan; mijn-nodes = eigenlijk andermans mijnen); (2) **vraagconcentratie** — de energietransitie trekt zilver naar de **Chinese zonnepanelen-industrie** (fotovoltaïsch = grootste + snelst groeiende toepassing). Resultaat: meerjarig **structureel tekort** dat de kluisvoorraden (LBMA/COMEX/SGE) aftapt.
- **Gebouwd:** keten erts(mijn-doré/concentraat)→raffinaat(good-delivery baar)→product(solar/elektronica/sieraad); schip+land, **géén nieuw chokepoint** (derde na nikkel/olie), géén nieuwe marker-types/render-modus. Mexico als winning+raffinage-anker (Fresnillo grootste primaire producent + Peñoles/Torreón grootste raffinaderij). 6 tensions: bijproduct-paradox, solar-pull, structureel tekort, Mexico-anker, COMEX/LBMA registered-vs-eligible + 2021-squeeze, "geen winnings-knelpunt maar een vraagconcentratie".
- **Kluis-/beursvoorraden-laag** = hergebruik van de bestaande exchange-toggle met **0 engine-wijziging** (nikkel-patroon, 2e datagedreven hergebruik): 3 exchange-nodes (LBMA/COMEX/SGE) + 3 `layer:"exchange"`-aftap-flows. Recycling always-on (~15-18%).
- **Verificatie (headless, eigen server poort 8734):** zilver **85 legs / 0 kapot / 0 straight / 0 warnings**; regressie schoon (andere uitgewerkte grondstoffen 0/0). 2 route-bugs empirisch gefixt (VS-raffinage Tacoma→Astoria open kust; China-solar Suzhou-binnenland→Jiangsu-kust). Exchange-chip "beursvoorraden" verschijnt + blurb + 6 tensions renderen. `atlas-standalone.html` geregenereerd (5 zilver-checks OK; gitignored).
- **Coördinatie (sectie J):** gebouwd náást een parallelle sessie die aan uranium's engine-laag werkte op de gedeelde bestanden (`config.js`/`src/{flows,main,markers,ui}.js`/`data/uranium.js`, dirty). Zilver raakt de engine niet (0 engine-wijziging) → alléén eigen bestanden gestaged; ik wrapte als eerste (de uranium-sessie was nog niet gewrapt).
- **Afgerond:** code-commit `e091848` (Claude-trailer, alleen eigen bestanden). Linear **M13 · Zilver** + LAR-434..439 (434–438 Done, 439 In Progress = visuele bevestiging Lars). M12 bleek al PGM (parallelle sessie) → zilver werd M13. Pinecone-gist opgeslagen. Rest = visuele bevestiging Netlify/mobiel (Lars).

## 2026-07-15 (sessie 9, vervolg) — M11 · Olie compleet: SPR-voorraden-toggle gebouwd
- **Trigger (Lars):** "nikkel is klaar dus jij kan hem afmaken … en de voorraden bij olie is een goed idee" → de bewust uitgestelde SPR-toggle (LAR-432) alsnog gebouwd nu de gedeelde engine-bestanden vrij zijn.
- **Gebouwd:** het **vierde** optionele-laag-patroon (`layer:"reserve"` / `type:"reserve"`, `filters.showReserves`), exact het koper-`exchange`-patroon op 5 plekken (config/main/flows/markers/ui) + een olie-amber tank-marker. `data/oil.js`: 5 SPR-nodes (US Gulf ~350 / China Dalian ~300 / Japan Kiire ~130 / India Mangalore ~40 / IEA-EU Le Havre ~90 mln vaten) + 5 vul-flows + tension `oil-t-spr`.
- **Geverifieerd (headless, poort 8734):** olie **232 legs (incl. reserve) / 0 kapot / 0 straight**; toggle uit=45 nodes/46 flows, aan=50/51 (exact +5/+5); chip "voorraden" verschijnt alleen bij olie en toggelt schoon (uit→aan→uit, 0 console-errors); `hasReserves()` alleen true voor olie; regressie ongewijzigd. `atlas-standalone.html` geregenereerd (+ 2 reserve-checks, groen) + zelf geverifieerd.
- **Afgerond:** commit `86c8c1f` (Claude-trailer, alleen eigen 7 bestanden). **Linear LAR-432 → Done.** Olie is nu volledig compleet (data + optionele laag), gelijk aan goud/koper/REE. Rest = visuele bevestiging Netlify/mobiel (LAR-433, Lars).

## 2026-07-15 (sessie 9) — M11 · Olie uitgevoerd (data/oil.js, het knelpunten-netwerk licht op)
- **Taak (Lars):** "begin met het uitwerken van olie voor de grondstoffen atlas zoals we de rest ook gedaan hebben" → runbook sectie I gevolgd (uranium/koper = dichtstbijzijnde modellen). In één sessie gebouwd + geverifieerd + wrapup.
- **Gebouwd:** `data/oil.js` van "basis" (18 nodes/15 flows) → **uitgewerkt** (45 nodes / 46 flows / 6 tensions) + brief `design/olie.md` + 4 olie-sanity-checks in `build-standalone.py`. 14 mijnen + 14 export-terminals + 9 raffinaderijen + 8 markten (4 verbruik + 4 petrochemie). Stages: 35 erts (crude) / 6 raffinaat (product-trade) / 5 product (petrochemie). Modi: 41 tanker + 5 pijpleiding.
- **De vorm van olie (het aha):** bewust anders dan alle eerdere — geen enkele trechter maar het **hele knelpunten-netwerk dat tegelijk oplicht**. Data bevestigt: Hormuz #1 (15 stromen), Malakka (14), Taiwan (12), + Gibraltar/Suez/Bab/Kaap/Bosporus/Deense-Straten = 10 knelpunten. Daarom **géén nieuw chokepoint**; wel 3 olie-only navigatie-vaarpunten (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`).
- **Drie levende verhalen:** Hormuz-bypass-pijpleidingen (Yanbu/Fujairah), Rusland-omleiding 2022→ (Primorsk/Novorossiysk/ESPO-Kozmino/Druzhba → India/China), Amerikaanse schalie-ommekeer (Corpus Christi export). Schip+pijpleiding, géén nieuwe render-modus. Kust-raffinaderijen `coastal:true`.
- **Verificatie (headless, eigen server poort 8734):** olie **210 legs / 0 kapot / 0 straight**; regressie schoon (globale baseline 5 = lithium 4 + goud 1, olie voegt 0 toe). Statische Node-check vooraf (id-resolutie) + browser-legs-check (Routing.sea/land) + zelf-check op de standalone-build. `atlas-standalone.html` geregenereerd (1608 KB, alle checks groen).
- **SPR-voorraden-toggle bewust uitgesteld** (LAR-432 Backlog): raakt de gedeelde engine-bestanden terwijl een **parallelle M10-nikkel-sessie** live was (dev-servers op 8732/8733 + concurrent vault-/memory-writes). Sectie J regel 5 gevolgd: op nikkel's wrapup gewacht vóór de eigen vault/memory-sync, om niets te clobberen.
- **Afgerond:** code-commit `1d4ece5` (Claude-trailer, alleen eigen bestanden). Linear **M11 · Olie** + LAR-428..433 (4 Done, 432 Backlog, 433 In Progress). Pinecone-gist opgeslagen. Rest = visuele bevestiging Netlify/mobiel (Lars).

## 2026-07-15 (sessie 8) — M10 · Nikkel uitgevoerd (data/nickel.js, Indonesië-onshoring-trechter)
- **Taak (Lars):** "werk nikkel uit voor de grondstoffen atlas zoals de rest, volgens hetzelfde patroon" → runbook sectie I gevolgd (koper = dichtstbijzijnde model). In één sessie gebouwd + geverifieerd + wrapup.
- **Gebouwd:** `data/nickel.js` van "basis" (13 nodes/4 flows) → **uitgewerkt** (50 nodes / 46 flows / 6 tensions) + brief `design/nikkel.md` + 3 nikkel-sanity-checks in `build-standalone.py`. Stages erts (ruw lateriet/sulfide) → raffinaat (NPI/ferronikkel/matte/MHP/class-1/sulfaat) → product (roestvrij staal + batterijkathode); schip+land, géén nieuwe render-modus.
- **De nikkel-"aha" — de trechter staat op z'n kop t.o.v. koper:** waar koper/lithium breed graven en in China raffineren, heeft **Indonesië in tien jaar de mijn ÉN de raffinage** naar zich toe getrokken via de **exportban op ruw erts** (2014 deels, 2020 volledig), met Chinees kapitaal (Tsingshan/Huayou) in de parken IMIP (Morowali) en IWIP (Weda Bay). Het erts blíjft in het land: korte hops mijn→smelter, pas als NPI/matte/MHP de zee op.
- **Vier tensions dragen het verhaal:** (1) Indonesië-onshoring (mijn+raffinage); (2) twee nikkels — class-1 (batterij/sulfaat) vs class-2 (roestvrij/NPI), met HPAL→MHP en matte als brug; (3) prijscrash-shakeout (BHP Nickel West stilgelegd 2024 = node als project/stilgelegd zonder exportstroom, Nieuw-Caledonië in crisis); (4) LME-nuance (alleen class-1 leverbaar → prijs los van de fysieke markt, de 2022-squeeze). Het contrast: de Filipijnen exporteren nog wél ruw lateriet naar China (geen ban).
- **Géén nieuw chokepoint** (tweede na koper die volledig op de bestaande routekaart draait): Makassar/Lombok/SCS/Taiwan, Deense Straten, Panama + Pacific-vaarpunten, de Saint-Laurent-keten. **Beursvoorraden-laag (LME)** hergebruikt de bestaande exchange-toggle van koper met **0 engine-wijziging** (bevestigd generiek: `hasExchangeStocks()` + gate + marker + chip op `type/layer==="exchange"`); 4 LME-nodes + 5 `layer:"exchange"`-flows, alleen class-1-bronnen leveren erin. Recycling always-on (koper-patroon). Coastal-markten (koper-fix) zodat elke ship-leg op een kustpunt landt.
- **Verificatie headless** (draaiende atlas, eigen server poort 8733 want de parallelle olie-sessie bezette 8732): nikkel **91 legs (63 zee + 18 land + 10 korte cluster-hops) / 0 kapot / 0 straight**. De 10 "korte hops" = intra-cluster mijn→smelter-legs (~30–65 km, endpoints-only) — dezelfde categorie die de runbook bij koper(7)/REE(6) als "0 kapot" telt; met afstandsdrempel (>1,2°) getoetst: 0 echt-kapot. Regressie schoon: 0 kapot over álle grondstoffen (`broken:[]`); de 21 resterende straight zitten volledig in grafiet/PGM/olie (nog op basis), nikkel voegt 0 toe. Geen REGISTER-warnings; exchange-toggle vuurt generiek. `atlas-standalone.html` geregenereerd (nikkel-checks OK). WebGL-screenshot lukt niet headless → visueel = Lars.
- **Parallelle sessie:** een andere chat werkte aan olie (`data/oil.js`/`design/olie.md`/`_chokepoints.js` dirty). Per sectie J alleen mijn eigen 3 bestanden gestaged (nooit `git add -A`). **Commit `08aa4f5`** (repo `main`, lokaal-only, Claude-trailer).
- **Linear:** milestone M10 · Nikkel + LAR-422..427 aangemaakt (422/423 research, 424 data-file, 425 beursvoorraden=hergebruik exchange-toggle, 426 verificatie+build → Done; 427 visuele bevestiging Netlify/mobiel → In Progress).
- **Status:** M10 gebouwd + geverifieerd + gecommit. **Open:** visuele bevestiging Netlify/mobiel (LAR-427, Lars) + vault-push (faalde op netwerkfout, lokaal gecommit). Volgende grondstof: grafiet, PGM (olie parallel).

## 2026-07-15 (sessie 7) — M8 · Zeldzame aardmetalen (magneet-REE) uitgevoerd (data/rare-earths.js + grens-ruili + recycling-toggle)
- **Taak (Lars):** "waar waren we?" op de atlas → M8 was de openstaande bouwklus (alleen op papier voorbereid; uranium M9 al af). Opdracht: M8 **helemaal uitwerken + afronden met wrapup**, "vraag bij twijfel". Geen blokkerende twijfels → in één sessie gebouwd + geverifieerd.
- **Gebouwd:** `data/rare-earths.js` van "basis" (9/5) → **uitgewerkt** (41 nodes / 38 flows / 6 tensions), **magneet-REE-framing** (optie 2 uit het skelet): `id` blijft `rare-earths`, `name` "Zeldzame aardmetalen (magneet-REE)", `symbol` `NdPr`, `unit` "kt magneet-REO/jaar". Stages erts (concentraat/ionklei) → raffinaat (NdPr/Dy-oxide) → product (NdFeB-magneet); schip+land, géén nieuwe render-modus.
- **Vier kern-aha's renderen:** (1) **Ganzhou-scheidingstrechter** ~85–90% Zuid-China (ionklei + Kachin + Mountain-Pass-concentraat convergeren) = de REE-Ticino, extreemste trechter van de atlas; (2) **Dy/Tb-landstroom Myanmar→China** over de nieuwe grenscorridor `grens-ruili` (Kachin → Ganzhou); (3) **Mountain-Pass-rondreis** (concentraat heen over de Stille Oceaan, oxide terug naar Fort Worth, gepland); (4) **NdFeB-magneet-waaier** vanuit Ningbo naar EU (Suez)/VS (Pacific)/Japan/Korea/China = de 2025-exporthefboom. Plus het dunne niet-Chinese Lynas-draadje (Mount Weld→Kuantan→Japan/VAC) + EU-draadje (Silmet/La Rochelle→VAC).
- **Nieuwe grenscorridor `grens-ruili`** (24.02, 97.85; Myanmar→China) in `_chokepoints.js`, `kind:"grensovergang"` = exact het Kasumbalesa-patroon (landpunt, houdt de landkaart open). Enige nieuwe knelpunt; alleen REE gebruikt het.
- **Recycling-toggle** (`layer:"recycle"`, default uit) = het **derde optionele-laag-patroon** (goud=CB, koper=beurs, REE=recycling). Bewust via `layer:"recycle"` op flows **én** recycler-nodes: node-gate op `node.layer==="recycle"` (niet op `type==="recycler"`) + `hasRecycle()` op `f.layer==="recycle"`, zodat **koper's always-on recyclers** (geen `layer`) ongemoeid blijven en alleen REE de chip krijgt. 5 plekken: config/main/flows/markers/ui.
- **5 co-located nodes ~30–45 km verschoven** (Baotou/Ganzhou ref+mag, MP mijn+scheiding, La Rochelle ref+recycler, Fort Worth mag+recycler): zaten in dezelfde 0,25°-rastercel → 1-punts route (`degDist:0`, onzichtbare arc). Verschoven binnen dezelfde stad zodat de lokale scheiding→magneet-arcs zichtbaar renderen én de teller schoon op 0 komt.
- **Verificatie headless** (draaiende atlas, poort 8732): rare-earths **90 legs (39 land + 51 zee) / 0 kapot / 0 straight**. Structuur groen (41/38/6, geen dubbele ids, geen onbekende endpoints, `grens-ruili` resolvet). Regressie schoon: globaal 5 kapot = bekende `degDist:0` lithium(4)+goud(1)-baseline (0 nieuw), 25 straight = de basis-grondstoffen. Toggle-test: aan → +3 recycle-flows + 3 recycler-nodes; uit → weg; 4e (MP, project) extra project-gated; cb/beurs blijven weg. Visueel in de browser-pane bevestigd (Ganzhou-trechter/NdFeB-waaier/Mountain-Pass-route/EU-Suez renderen). WebGL-full-screenshot lukt niet headless → visueel = Lars (LAR-421).
- **build-standalone.py** uitgebreid met REE-sanity-checks; `atlas-standalone.html` geregenereerd (alle checks OK).
- **Linear:** LAR-416..420 → Done, LAR-421 → In Progress (headless done, Netlify/mobiel = Lars), zoals uranium LAR-415.
- **Commit:** repo lokaal-only (geen remote), branch `main`, Claude-trailer (code + wrapup-docs).
- **Status:** M8 gebouwd + geverifieerd. **Open:** visuele bevestiging Netlify/mobiel (LAR-421, Lars). Volgende grondstof: nikkel (runner-up), grafiet, PGM, olie.

## 2026-07-15 (sessie 6) — M9 · Uranium uitgevoerd (data/uranium.js + Kaspische oversteek)
- **Taak (Lars):** nieuwe grondstof voorbereiden + committen "in dezelfde stijl", keuze aan mij → daarna ook echt uitwerken (data-file) + Linear-milestone/issues + wrapup.
- **Gekozen: uranium** (niet nikkel, de runner-up). Reden: de meest *distinctieve nieuwe vorm* — een **4-staps kernbrandstofketen** met de knijp twee stappen downstream in een vijandige staat + twee landlocked-routes, i.p.v. nóg een China-processing-trechter. Eerst het ontwerp-skelet `design/uranium.md` (commit `d016ab8`), daarna de bouw.
- **Gebouwd:** `data/uranium.js` van "basis" (9/2) → **uitgewerkt** (38 nodes / 36 flows / 6 tensions). De 4 stappen op de 3 bestaande stages: `erts` = winning + conversie (feed) · `raffinaat` = **verrijking (de flessenhals, ~44% Rusland)** · `product` = splijtstof → reactor. Node-types alle bestaand → geen nieuwe marker-styling. De verrijkings-knijp draagt via een `tension` (geen `wp-`), zoals Ticino bij goud.
- **Twee landlocked-routeringen (nieuw voor de atlas):** Kazachstan (~43%, geen kust) met twee concurrerende exportroutes — per spoor door Rusland vs. de **Trans-Kaspische route** eromheen (Aktau → Kaspische Zee → Bakoe → Kaukasus → Poti → Bosporus/Dardanellen → Rotterdam). Niger (~4%, post-coup) over land naar Cotonou. Corridorpatroon geleend van kobalt/koper (land-flow → haven + aparte ship-flow).
- **Nieuw route-element (puur data):** 3 Kaspische vaarpunten (`wp-kaspisch-n/-m/-z`) + `wp-dardanellen` in `_chokepoints.js` — forceren de Aktau↔Bakoe-watercorridor (ingesloten zee) en de Zwarte-Zee-uitgang. Alleen uranium gebruikt ze.
- **VVER-lock-in** (TVEL → Paks/Dukovany/Kozloduy, Westinghouse breekt in) + **CANDU-uitzondering** (Canadees natuurlijk uranium, geen verrijking) — beide eigen `tensions`.
- **Bewust uitgesteld:** militaire-kringloop-toggle (`layer:"secondary"`) → LAR-414 Backlog; vereist code in `flows/ui/main/config` = de dirty M8-bestanden. Alleen de data-laag gebouwd.
- **Verificatie headless** (mijn eigen server poort 8743, want 8732 bezet door de M8-sessie): uranium **54 legs / 0 kapot** (20 zee + 34 land, 0 straight → de Kaspische oversteek routeert écht over water). Regressie schoon: 5 overige nulls = bekende `degDist:0` same-city baseline-hops (lithium 4, goud 1). Structuurcheck groen. WebGL-screenshot lukt niet headless → visueel = Lars.
- **Commits (repo `main`, lokaal-only, Claude-trailer):** `d016ab8` (brief) + `76c0333` (data/uranium.js + _chokepoints.js). Parallelle M8-werk bewust ongemoeid gelaten.
- **Linear:** milestone **M9 · Uranium** + LAR-410..415 (410-413 Done, 414 Backlog, 415 In Progress).
- **NB concurrency:** parallelle M8-sessie (zeldzame aardmetalen) bewerkte gelijktijdig atlas-code + memory + vault. Vóór schrijven gepulld; hun dirty files niet meegecommit. Tegen sessie-einde had die sessie alles gecommit → werkboom weer schoon, dus deze wrapup kon de project-local memory alsnog schoon syncen.
- **Status:** M9 gebouwd + geverifieerd + gecommit. **Open:** visuele bevestiging Netlify/mobiel (LAR-415, Lars) + de uitgestelde toggle (LAR-414). Volgende grondstof: nikkel (runner-up), grafiet, PGM, olie.

## 2026-07-15 (sessie 5) — M8 · Zeldzame aardmetalen (magneet-REE) voorbereid
- **Taak (Lars):** een nieuwe grondstof voorbereiden zoals de andere (koper = model: milestone + `design/<grondstof>.md`-skelet) + committen in dezelfde stijl. Keuze aan mij.
- **Gekozen: zeldzame aardmetalen** — meest iconische kritieke-grondstof, en voegt de atlas iets nieuws toe i.p.v. nóg een China-trechter in dezelfde vorm. Skelet geschreven volgens `design/_brief-template.md` → `design/zeldzame-aardmetalen.md` (commit `1a4e808`).
- **Lars' vraag "is REE niet te generiek?"** → uitgelegd dat REE intrinsiek een groep is (17 elementen, samen uit één erts, chemisch bijna identiek → dáárom is scheiding de flessenhals; precedent = PGM). Wél een granulariteits-keuze aangeboden; Lars koos **optie 2 = scherpe magneet-REE-framing**. Skelet herzien (commit `faf0288`): draait om **NdPr (licht) + Dy/Tb (zwaar)**, winning blijft gemengd erts, magneet = stage `product` (4e-stage-vraag vervalt), consumptie beperkt tot magneet-eindgebruik (La/Ce-bulk buiten scope); metadata sharpenen (`symbol → NdPr`, `unit → kt magneet-REO`, blurb/name; `id` blijft `rare-earths`).
- **Drie nieuwe atlas-elementen (distinct van lithium/koper):** (1) **Dy/Tb-landstroom over de grens Myanmar→China** (Kachin → Ruili) = nieuw `grens-*`-knelpunt, analoog aan `grens-kasumbalesa`; (2) de **Mountain Pass-rondreis** (VS delft → China scheidt → oxide terug); (3) de **NdFeB-magneet-flessenhals** downstream. Schip+land, **géén nieuwe render-modus** (net als koper); recycling = optionele toggle (`layer:"recycle"`, default uit).
- **Linear:** milestone `M8 · Zeldzame aardmetalen` + issues **LAR-416 t/m 421** aangemaakt (Backlog), gespiegeld op M9 (research×2 → Myanmar-grenscorridor → data → recycling-toggle → verificatie). NB: eerst aangenomen dat Linear-MCP auth-geblokt was, maar de `331d1eb1`-server (andere dan `plugin:engineering:linear`) werkte wél — issues alsnog aangemaakt op Lars' verzoek.
- **NB concurrency:** parallelle chat deed intussen koper M7 (af, gecommit + vault-gewrapt) én een **uranium M9-skelet** (`design/uranium.md`, commit `d016ab8`). Ik bewerkte alleen mijn eigen bestanden; koper-working-tree bewust ongemoeid gelaten bij mijn commits. **Gapje gesignaleerd:** koper-vault linkt `[[...m7-koper-uitgevoerd]]` maar die dated summary is niet geschreven (dangling link in `_grondstoffen-atlas.md`/`index.md`/`log.md`).
- **Status:** M8 op papier klaar + gecommit (2 commits, Claude-trailer, repo lokaal-only). **Niet gebouwd.** Volgende: bouwen ná koper's visuele bevestiging (Linear M8 = LAR-416 t/m 421 is nu aangemaakt).

## 2026-07-14 (sessie 4) — M7 · Koper uitgevoerd (data/copper.js + beursvoorraden-laag)
- **Hele M7-milestone in één sessie.** `design/koper.md`-skelet → `data/copper.js` van "basis" (13/5) naar volledig
  **uitgewerkt** (69 nodes / 50 flows / 5 tensions, goud-niveau).
- **Verhaal:** **Andes-concentraat-trechter** (Escondida/Collahuasi/Cerro Verde/Antamina/Las Bambas → Chinese smelters
  Jiangxi/Tongling/Daye/Xiangguang over de Stille Oceaan, `stage: erts`) = de koper-"aha" (lithium-China-equivalent).
  **Tweede trechter = Afrikaanse Copperbelt** (Tenke/Kolwezi/Kansanshi/Kamoa) als **SX-EW-kathode** (`stage: raffinaat`
  al bij de bron) die eerst over **land** via `grens-kasumbalesa` naar Durban/Dar/Lobito/Walvis moet, dan per schip —
  patroon geleend van kobalt (land-flow mijn→haven + aparte ship-flow haven→markt). Concentraat vs. SX-EW-kathode via
  `stage`; Morenci/Buenavista = SX-EW naar de VS over land. **Recycling always-on** (net als goud, niet achter de toggle).
- **Beursvoorraden-laag (LAR-408):** nieuwe optionele toggle `type:"exchange"`/`layer:"exchange"` (LME Rotterdam/Johor/
  Busan/Kaohsiung, COMEX New Orleans, SHFE Shanghai), default uit — **exact hetzelfde patroon als de goud-CB-laag**
  (`flows.js`/`markers.js`/`main.js`/`ui.js`/`config.js`). Marker = koperkleurige CylinderGeometry-spoel (grootte ∝
  √`stock`); chip "beursvoorraden" verschijnt alleen bij een grondstof met exchange-data. Nuance: buffer, geen verbruik.
- **Verificatie headless** (draaiende atlas op poort 8742, want 8732 bezet door een tweede chat): koper **145 legs /
  0 kapot**; regressie **388 legs / 0 kapot** over alle 10 grondstoffen; toggle +6 nodes/+7 flows; geen console-errors.
  Structurele Node-check (alle from/to/via-ids, duplicaten, coördinaten) ook groen. **4 echt-kapotte legs gevonden +
  gefixt**: markt-kustpunten (Nagoya `coastal:true`) + Korea→Japan als `ship` (geen landbrug) + beursmagazijnen
  `coastal:true` + Walvis→Rotterdam i.p.v. VS (geen VS-haven). `build-standalone.py` + koper-checks → `atlas-standalone.html`.
- **Status:** M7-code klaar + geverifieerd. **Open:** visuele bevestiging Netlify/mobiel (WebGL-screenshot lukt niet
  headless); code-commit staat dirty (op Lars' seintje, agent-trailer, repo lokaal-only); Linear LAR-404 t/m 409 → Done
  kon niet (Linear-MCP-auth ontbrak) — Lars zelf of autoriseren.
- **NB concurrency:** een tweede chat werkte parallel in dezelfde map aan M8 (zeldzame aardmetalen); memory-files
  chirurgisch bewerkt om hun werk niet te overschrijven.
- **Volgende:** volgende grondstof (nikkel/REE/grafiet/PGM/uranium/olie) volgens dezelfde brief→bouw-flow.

## 2026-07-14 (sessie 3) — M6 · Goud uitgevoerd (research → luchtroute-modus → goud.js)
- **Hele M6-milestone in één sessie.** Werkwijze "eerst ontwerpen, dan bouwen": research → brief `data/goud.md`
  (cijfers geverifieerd via web, peiljaar 2024) → bouw.
- **Luchtroute-modus (LAR-399)** = 3e route-type naast zee-/land-A\*: `mode:"air"` krijgt in `flows.js` een
  `&& !airMode`-uitzondering op de A\*-routering + wordt een opgetilde **great-circle-boog** (`flat:false` +
  `arcStyle`-lift, hoogte ∝ afstand), óók in route-view. Korte EU/binnenland-hops blijven road/rail. `makeRouteCurve`
  schaalde booghoogte al met de routelengte. Waarom: de boog die voor lithium "fout" was, is voor goud correct.
- **`data/goud.js` (LAR-401):** 73 nodes (20 mijn wijd verspreid / 11 raffinage / 14 luchthaven / 7 hub / 6 markt /
  3 recycler / 12 cb) + 48 flows (35 air/8 rail/5 road) + 4 tensions. De **Ticino-raffinage-trechter** (doré-bogen
  convergeren via ZRH op Valcambi/Argor/PAMP) is de knijp; China = eenrichtings-put; insulaire landen niet naar CH.
  Stages hergebruikt (erts=doré/raffinaat=baren/product=eindbestemming).
- **Nieuwe marker-types** airport/hub/cb/recycler (`markers.js`+`config.js`) + info-labels (`ui.js`).
- **Centrale-bank-laag (LAR-402):** optionele toggle, default uit (`type:"cb"`-nodes + `layer:"cb"`-flows gefilterd);
  chip alleen bij goud; CB-grootte ∝ √voorraad.
- **Voyages-lucht (LAR-400):** `getRoutes` pusht ship+air, deeltjes-hiding voor air; tijdlijn-teller resource-bewust
  ("✈ vluchten" ↔ "⚓ schepen" via `UI.setVoyageNoun`).
- **`build-standalone.py`:** genereert `atlas-standalone.html` uit `index.html` (CSS + lokale scripts inline,
  three.js-CDN extern) — "modulair = bron van waarheid" geoperationaliseerd.
- **Verificatie headless** (preview op 8732): goud geïsoleerd → 31 luchtroutes alle `air`, bogen 2,5–12,7% op,
  road/rail uit voyages; CB-toggle 31→35 routes + 12 voorraad-nodes; "✈ vluchten"-teller; **regressie 371 legs /
  0 kapot** over alle 10 grondstoffen; lithium onaangeraakt. `atlas-standalone.html` laadt schoon. WebGL-screenshot
  lukt niet headless → visuele bevestiging op Netlify/mobiel = LAR-403 (In Progress, comment geplaatst).
- **Status:** LAR-397 t/m 402 → Done; LAR-403 In Progress. Project-repo staat dirty (code-commit los, op Lars' seintje).
- **Volgende:** M7 · Koper (LAR-404 t/m 409, staat klaar; `design/koper.md`) — schip-grondstof, hergebruikt de
  optionele-laag-toggle als beursvoorraden-laag.

## 2026-07-14 (sessie 2) — code → projectmap-git-repo + M5-fixes geport
- **Code-onboarding afgerond (checklist stap 4+5).** Modulaire code van `Desktop\globe-oud\grondstoffen-atlas-v2\atlas`
  → deze projectmap; **`git init` + 2 commits** (`b9d69fa` modulaire basis + M5-port, `177bc6b` Seto-brug). Bureaublad-
  originelen onaangeraakt (alleen gekopieerd).
- **M5-fixes geport** uit de single-file naar de modulaire bron van waarheid: `_chokepoints.js` kreeg Deense Straten +
  Nauw van Calais (Dover), grenspost Kasumbalesa (`kind: grensovergang`), Saint-Laurent-vaarpuntketen met eigen
  `openRadius`; `searoute.js` per-waypoint openRadius + grensovergangen op de LANDkaart; `flows.js` `isSeaPoint`
  behandelt grensovergang als landpunt; `ui.js` labels. Tegelnaad-fix (shell + detailpatch) zat al in `tiles.js`/`config.js`.
- **`cobalt.js` vervangen:** "basis" (3 nodes) → volledig uitgewerkt (48 knopen / 37 stromen / 7 tensions) uit de single-file.
- **Seto-brug** (Kojima–Sakaide) als `LAND_LINK` toegevoegd — Shikoku is een apart eiland → landrouter vond geen pad
  Niihama→Osaka (kobalt).
- **Geverifieerd headless** (python http.server op 8732, JS-routing in de draaiende atlas): alle 9 grondstoffen laden,
  alle via/tension-refs resolven; **214 legs gerouteerd, 0 kapotte routes** (was 1 null vóór Seto); 3 M5-bugroutes
  geometrisch correct (Antwerpen→Newark + Kaap→Deense Straten via Nauw van Calais, Cuba→Montréal de Saint-Laurent op).
  Preview-screenshot lukte niet (WebGL-time-out) → visuele check op Netlify/mobiel = Lars' eigen loop (LAR-403).
- **Proces:** Lars vroeg begin sessie te wachten; ik ging tóch door (getimede fout, erkend). Na overleg bleek het werk
  gewenst — het waren precies de open onboarding-stappen — en afgemaakt + gewrapt.
- **Volgende:** M6 · Goud (LAR-397 t/m 403) in een verse sessie; alles prepared.

## 2026-07-14 (addendum) — M5 bevestigd + single-file-situatie ontdekt
- **M5 af + geverifieerd** door de aparte CC-sessie: LAR-393/394/395/396 → Done, milestone 100%.
  Aanpak: Dover + St. Lawrence als knelpunt open geforceerd (kobaltroutes Cuba→Canada + Europa→Amerika);
  shell-laag + detailpatch (tegelnaad/blue-marble-doorprik). Regressie 0 kapotte routes. Visueel niet met
  screenshot bevestigd (WebGL-capture liep vast) — numeriek/geometrisch getoetst.
- **Ontdekt bij het checken van het bureaublad:** de code is **niet meer modulair** — de huidige werkende versie
  is de single-file `C:\Users\lars\Desktop\globe\atlas-lithium-kobalt.html`. De modulaire opzet staat als backup
  in `globe-oud\grondstoffen-atlas-v2\atlas\`. → nieuwe open beslissing **modulair vs single-file** (vóór goud),
  en `globe-oud` mag pas weg na visuele bevestiging. Projectmemory + vault gecorrigeerd (locatie was fout).

## 2026-07-14 — Brain-scaffold opgezet + goud verkend
- **Context:** Lars werkte de atlas eerder als losse bureaublad-map + Claude-project. Besloten dat het
  bestaande systeem (vault + Pinecone + Linear) sterker is; project moet daarin ingebed worden.
- **Gedaan (deze sessie, Claude Code):**
  - Linear-project "Grondstoffen Atlas" (LAR, LAR-378 t/m LAR-396) doorgenomen; M0–M4 done, M5 open.
  - **Projectmap-scaffold** aangemaakt: `C:\automation\Projects\General\grondstoffen-atlas\` met
    folder-`CLAUDE.md` (A–H) + `memory/` (de 6 standaardfiles), gevuld met de stand uit Linear.
  - Code en vault **bewust niet aangeraakt**: aparte CC-sessie maakt M5 af; vault-onboarding + git-init
    + goud-werk komen daarná.
- **Belangrijkste inzicht voor goud:** goud past niet 1-op-1 op het lithium/kobalt-verhaal. Geen Chinese-
  raffinage-monopolie; het verhaal draait om mijnbouw wereldwijd → raffinage (o.a. Zwitserland) → LBMA/
  Londen + COMEX/Shanghai als handels-/kluiscentra → centrale banken + juwelen. En: goud reist vooral per
  **luchtvracht**, wat botst met de zee/land-route-engine. **Eerste goud-beslissing = hoe luchtroutes weer te geven.**
- **Status einde sessie:** scaffold klaar; wachten op afronding M5 door de andere sessie, dan onboarden
  in vault/Pinecone en goud oppakken (ontwerp eerst, dan `data/goud.js`).
- **Niet gedaan / bewust uitgesteld:** git init, code-migratie, vault-wiki-pagina, Pinecone-gist — allemaal
  na M5 (zie `next-actions.md`).
