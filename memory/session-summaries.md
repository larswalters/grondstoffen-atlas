# Session summaries — Grondstoffen Atlas
*Newest first.*

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
