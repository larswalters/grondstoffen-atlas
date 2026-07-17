# Next actions — Grondstoffen Atlas
*Last updated: 2026-07-17 (weergave-fixes LAR-479 + LAR-481 bevestigd → terug naar de koper-pilot)*

> **Tussendoor gedaan en afgerond (2026-07-17):** Lars stelde de pilot bewust uit voor drie weergave-bugs —
> *"als we dat eerst fixen voordat we de routes doen lijkt me beter."* Alle drie live én visueel bevestigd
> (*"ze werken zoals het hoort nu"*): **LAR-479** tegel-afkap (`cos(lat)` + budget 96 + midden-naar-buiten),
> **zoom-evenredig draaien**, **LAR-481** marker-LOD (markers verdwijnen niet meer op tier). Commits `297016f`
> + `8dda38e`. **Bijvangst voor de pilot: de ondergrond is nu scherp op élke zoomstand — routes zijn daardoor
> makkelijker te beoordelen dan tijdens de vorige test.**

## ⚠️ NU EERST — pilot-test afronden (LAR-474 In Progress)

1. [ ] **Japan-observatie verifiëren.** Lars ziet op mobiel (screenshot 03:15) de trans-Pacific bundel dwars over
       Honshu. **Hypothese: stale cache** — de curve-fix (`3c801a0`) ging pas minuten vóór de screenshot live
       (Pages CDN 10 min + mobiele browsercache). Eerst: **incognito/verse cache op mobiel**. Nog steeds fout →
       de Tsugaru/Japanse Zee-passage per trans-Pacific corridor plotten (scratchpad `plot_corridors.js` als basis)
       en de polyline + getekende curve daar onderzoeken.
2. [ ] **Lars' idee bespreken: de wereldbal-weergave aanpassen zodat routes duidelijker worden.** Nog te verkennen
       wát precies (contrast/dikte/kleur stromen? satelliet- vs vector-ondergrond? bundeling?). **Vóór de uitrol.**
3. [ ] Pas na visuele go van Lars → **LAR-477 uitrol 13 grondstoffen** (pipeline + checker staan klaar;
       MARNET dekt óók Saint-Laurent/Kaspisch — empirisch getoetst).
4. [ ] Klein cosmetisch (mag wachten): haven-uitvaart-bochtjes punt 1 (110–160°, onder de marker) ·
       Rotterdam→Duitsland laatste-mijl-waaier (4 ship-stromen over land; bestond al vóór de pilot).

## 🧭 M18 · Realistische zeeroutes (searoute) — LAR-473..478 · stand na de pilot-bouwsessie

- [x] **LAR-473 — spec + besluiten** ✅ Done (2026-07-17): `design/zeeroutes.md`, "MARNET beslist", datamodel,
      hard falen, drempel ">15% zonder doorgang".
- [~] **LAR-474 — PILOT koper** ⬅️ **gebouwd, in visuele test** (zie boven). 84 legs / 0 kapot / 24 cache-hits,
      regressie schoon, zeereizen −9,3%.
- [~] LAR-475/476 — generator + engine de facto gebouwd binnen de pilot (voor koper); blijven open tot de uitrol.

**De koers na "inhoudelijk compleet": niet een 15e grondstof, maar route-kwaliteit.** Lars: *"een boot zou daar
nooit zo varen."* De drie feature-milestones **staan** op route-nauwkeurigheid → M18 eerst.

**Waarom (bewezen 2026-07-17):** Antofagasta→Shanghai = grote-cirkel **18.526 km** · searoute (echte lanen)
**18.880 km (+2%)** · **onze bol 19.970 km (+8%)**. Het handgeplaatste vaarpunt **`wp-pac-zuid`** (26°Z) dwingt
**~1.090 km omweg** af. De `via`-ketens zijn grotendeels handmatige compensatie voor een slechte router.
Diagnose in `searoute.js`: `openRadiusDeg: 1.2` (~130 km geforceerd water rond élk knelpunt) + 8-richtingen-A\*
(trapjes; Golf→Rotterdam 33 richtingswissels) + grof raster/gretige heuristiek/**géén echte vaarlanen**.

- [ ] **LAR-473 — spec `design/zeeroutes.md`** (design-first): datamodel corridor-cache, hoe `flows.js` 'm gebruikt,
      fallback-gedrag, netwerk bewaren voor M21, verificatie-criterium (routelengte ÷ grote-cirkel), en **het open
      besluit**: via-punten op zee-legs **(a) opruimen** of **(b) behouden als hint** — **Lars beslist**.
- [ ] **LAR-474 — PILOT: koper volledig op searoute** ⬅️ **START VAN DE VOLGENDE SESSIE.** Baseline → corridors
      extraheren (**mét** `via`-keten!) → searoute draaien → vergelijken → renderen → **go/no-go Lars** vóór de andere 13.
      Koper = beste testcase (bewezen-foute Antofagasta-corridor + Andes-trechter + Copperbelt-**land**routes die
      ongemoeid moeten blijven).
- [ ] **LAR-475 — corridor-cache generator** (Python, build-time): unieke zee-corridors **gededupliceerd per haven-paar**
      over alle 14 → `data/_searoutes.js`. Fouten hard maken, determinisme, bestandsgrootte bewaken.
- [ ] **LAR-476 — engine**: `flows.js` rendert gebakken polylines i.p.v. live A\*; land/lucht ongemoeid; **`laneShape`
      (vaarbanen-waaier) expliciet checken** = de subtielste regressie-val; **netwerk bewaren voor M21**.
- [ ] **LAR-477 — uitrol 13 + via-punten opruimen** (ná pilot-go). Let op: uranium's Kaspische oversteek (ingesloten
      zee) heeft searoute waarschijnlijk niet → expliciet checken, niet stil laten wegvallen. Goud/PGM/diamant = `air`, niet aanraken.
- [ ] **LAR-478 — verificatie + build + visueel** (Lars). IJkpunt: Antofagasta→Shanghai 19.970 → ~18.880 km.

> ⚠️ **Harde regel:** vergelijk **nooit** tegen een kale origin→dest A\*-run. De pilot van 16 juli deed dat →
> "route A", een pad dat de bol nergens tekent (Lars zag het meteen: *"ik zie op onze wereldbol niets dat route A
> neemt"*). Vergelijk altijd tegen wat `flows.js` werkelijk rendert.

**Status:** `searoute` 1.6.0 geïnstalleerd. Pilot-artefacten (`astar_paths.json`, `zeeroutes_vergelijking.html`) in
`…/Temp/claude/C--automation/ec6b9a39-…/scratchpad/`.

**Volgorde daarna:** M19 (knelpunt-stress) → M20 (China-meta-view) → M21 (disruptie-simulator). ⚠️ M21's aanpak is
**herijkt**: knelpunt blokkeren = *edge uit het netwerk halen*, niet een raster-cel-masker.
⚠️ M18 staat in Linear ónder M21 gesorteerd (`sortOrder` niet zetbaar via MCP) — even slepen in de UI.

## 🐛 Losse issues (buiten M18)

- [x] **LAR-479 (High) — tegel-patch wordt afgekapt bij inzoomen** ✅ **Done (2026-07-17), bevestigd door Lars.**
      Twee oorzaken: budget < één patch (40 vs 42–72) mét noord→zuid-vulling, én een ontbrekende `cos(lat)` in
      `detailZoomFor()`. Fix: `cos(lat)` + budget 96 + midden-naar-buiten. Commit `297016f`.
- [x] **Zoom-evenredig draaien** ✅ **Done (2026-07-17), bevestigd door Lars.** Geen issue-nummer — kwam er tijdens
      dezelfde sessie bij (Lars: *"als je een stuk bent ingezoomd dan is het draaien super gevoelig"*). Commit `297016f`.
- [x] **LAR-481 — marker-LOD vuurde averechts** ✅ **Done (2026-07-17), bevestigd door Lars.** `forced` overrulet tier
      voor 57/63 nodes → de LOD raakte alléén de 6 context-mijnen zónder stroom. Markers verdwijnen niet meer op tier;
      `tier` = alleen labels. Commit `8dda38e`.
- [ ] **LAR-480 (Low) — markers-contrast bij inzoomen.** Het is contrast, niet schaal. Richting: halo/outline.
      **Nu relevanter:** de tegels zijn scherper (drukkere ondergrond) én er staan meer markers (LAR-481). Nog steeds
      ná M18 — de zeeroutes veranderen wat er ópstaat.
- [ ] **(Low, geen issue) — mislukte tegel wordt nooit opnieuw geprobeerd** (`ensureTile` early-return + alleen
      `console.warn` → permanent opacity 0). Bijvangst van LAR-479, apart defect. Iets relevanter met `maxTiles: 96`
      (meer gelijktijdige requests), maar niet waargenomen — zie `bugs-and-risks.md`.
- [ ] **(Na M18) — stromen ook tieren?** De tier-LOD is nu de facto uit voor markers. Wil je uitgezoomd écht
      ontdubbelen, dan moeten stromen mee — raakt `flows.js` (= pilot-code) en het beeld van alle 14. Alleen oppakken
      als Lars uitgezoomd te druk vindt (6 extra bolletjes bij koper).

---

## 🎉 Backlog was leeg (2026-07-16) — afgerond
Alle 3 resterende backlog-issues afgerond + gepusht → live op Pages. **Niets meer In Progress/Todo/Backlog in Linear.**
- **LAR-471 · lab-grown-toggle (diamant)** ✅ — het 6e optionele-laag-patroon (`layer:"labgrown"`): 3 productie-nodes
  (China/Henan HPHT, India/Surat CVD, VS/Washington premium-CVD) + 6 flows die de VS-verlovingsringmarkt ondergraven;
  5 engine-plekken + violette octaëder-marker + chip "lab-grown"; default uit, alleen bij diamant. Commit `f6c95f6`.
- **LAR-447 · recycle-tooltip per-grondstof** ✅ — `recycleHint`-veld op de resource + `main.recycleHint()` + generieke
  fallback in `ui.js`; hints op REE (<5% magneet) / PGM (~25% autokat) / grafiet (nascent). Commit `9feb8f2`.
- **LAR-448 · PGM-beursvoorraden-laag** ✅ — PGM's tweede optionele toggle naast recycling (LPPM/NYMEX/TOCOM, pure data,
  0 engine-wijziging, hergebruik exchange-toggle). PGM = eerste grondstof met twee toggles. Commit `9feb8f2`.
- Headless geverifieerd: diamant 41 legs/0 kapot, PGM 52 legs/0 kapot, beide toggles filteren correct, regressievrij.

**Enige open punt:** visuele eindbevestiging op de live URL/mobiel = Lars (violette lab-grown-arcs op de VS-markt bij
diamant + de LPPM/NYMEX/TOCOM-kluismarkers bij PGM). WebGL-screenshot hangt headless.

**Toekomstig werk** = alleen nog een nieuwe **15e grondstof** (zilver/kolen-patroon) óf losse verfijningen — geen
openstaande features meer. Losse hygiëne: bureaublad-originelen (`atlas-lithium-kobalt.html` + `globe-oud`) opruimen.

---


## 🎉 De basis-10 is compleet — nu uitbreiden met nieuwe grondstoffen (14 en groeiend)
Na M14 (grafiet) stond er geen enkele grondstof van de **basis-10** meer op "basis". Daarna komen de **nieuwe
grondstoffen** erbij (niet basis→uitgewerkt maar een nieuw `data/<x>.js` + script-tag + build-check, het zilver-patroon):
zilver (M13), gas (M15), diamant (M16), **kolen (M17)**. Volledig uitgewerkt nu: de basis-10 + zilver + gas + diamant +
kolen = **14** (gas M15 / diamant M16 / kolen M17 = de nieuwe batch, alle drie in parallelle sessies gebouwd + gepusht).
Het brief→bouw-runbook (sectie I) + het nieuwe-grondstof-plumbing-patroon (LAR-436/457/463) blijven de vaste flow.

## M15 · Gas ✅ uitgevoerd (2026-07-16) — LAR-460, 462, 463, 464, 465, 466
Nieuw `data/gas.js` (42 nodes / 51 flows / 6 tensions) + brief `design/gas.md` + `<script>`-tag in `index.html` + 5 gas-checks
in `build-standalone.py`. Aardgas/LNG: **gas is nauwelijks te verplaatsen** → captive pijpleidingen vs de LNG-liquefactie-
trechter (VS-Golfkust/Qatar/Australië); Europa-pivot 2022 + Russische oost-pivot; Qatar via Hormuz (géén bypass, scherper
dan olie). Schip+pipeline, **géén nieuw chokepoint/render-modus/marker-types**; opslag hergebruikt de olie-`reserve`-toggle
(0 engine-wijziging). Headless: **97 legs / 0 kapot / 0 straight**, regressievrij (2 Arctische Yamal-routes + captive-
pijpleidingen routeren correct zonder nieuw vaarpunt). Commits `040d2b7` (data) + `a8378ef` (build-checks), **gepusht → live
op Pages** (git-index-race met de diamant-sessie teruggedraaid met `reset`+`--only`, sectie J). LAR-460/462/463/464/466 Done.
- [ ] **LAR-465** — visuele bevestiging op de live URL/mobiel (https://larswalters.github.io/grondstoffen-atlas/) = **Lars**.
  Checken: de twee leversystemen (donkere pijpleiding-arcs vs. heldere LNG-oceaan-arcs), Hormuz als Qatar's enige uitgang,
  de VS-Golfkust-waaier (oost naar Europa + west via Panama), de gekrompen Rusland→EU-pijl + de dikke Power-of-Siberia→China,
  en de opslag-toggle ("voorraden", default uit).

## M16 · Diamant ✅ uitgevoerd (2026-07-16) — LAR-467 t/m 472
Nieuw `data/diamond.js` (25 nodes / 35 flows / 6 tensions) + brief `design/diamant.md` + `<script>`-tag in `index.html` +
4 diamant-checks in `build-standalone.py`. De scherpste downstream-trechter (Surat ~90-95%) + Antwerpen-G7-certificering +
Alrosa-herrouting; diamant **vliegt** (hergebruik goud/PGM air-mode, 0 engine-wijziging, géén nieuw chokepoint/marker-types).
Headless: 35 legs (27 air + 8 road) / 0 kapot / 0 straight / 0 degen, regressievrij. Commits `72d134c` (feat) + `7d06a0c`
(build), **gepusht → live op Pages**. LAR-467/468/469/470 Done.
- [ ] **LAR-472** — visuele bevestiging op de live URL/mobiel (https://larswalters.github.io/grondstoffen-atlas/) = **Lars**.
- [ ] **LAR-471 (Backlog) — lab-grown-toggle** bouwen zodra de gedeelde engine-tree schoon is: nieuwe optionele laag
  `layer:"labgrown"` + `showLabGrown` op 5 plekken (`config`/`main`/`flows`/`markers`/`ui`); 2-3 productie-nodes (China/Henan
  HPHT + India/Surat CVD) die de Surat-slijperij én de VS-markt ondergraven. Bewust uitgesteld i.v.m. de parallelle sessies
  (zoals uranium's LAR-414 / olie's LAR-432). In v1 leeft lab-grown als `tension`.

## M17 · Kolen ✅ uitgevoerd (2026-07-16) — LAR-455 t/m 459, 461
Nieuw `data/coal.js` (34 nodes / 33 flows / 6 tensions) + brief `design/kolen.md` + `<script>`-tag in `index.html` +
`grens-gashuunsukhait` (Mongolië-Gobi) in `_chokepoints.js` + 5 kolen-checks in `build-standalone.py`. De vorm = **de
binnenlandsheid, géén trechter** (~85% verstookt waar gedolven; ~15% zeehandel); China = swing-koper; twee kolen
(thermisch/cokeskool via note+tension); drie her-routeringen (China-Australië-ban, Rusland-oost-draai, Mongolië-Gobi-
corridor). Schip+land, géén render-modus/marker-types/toggle-laag.
- [x] Research upstream (winning) / downstream (verbruik + staal + zeehandel + her-routeringen) inline in `design/kolen.md` (LAR-455/456).
- [x] Nieuwe-grondstof-plumbing (LAR-457): `data/coal.js` + `<script src="data/coal.js">` in `index.html` + 5 kolen-checks in `build-standalone.py`.
- [x] Nieuw chokepoint `grens-gashuunsukhait` (LAR-458) in een eigen COAL-blok in `_chokepoints.js` (Kasumbalesa/Ruili-patroon).
- [x] `data/coal.js` uitgewerkt (LAR-459): mijnen (binnenlandse reuzen + exportmijnen), havens, markt-centrales/staalhubs, Mongolië-corridor; 6 tensions.
- [x] Verificatie headless (LAR-461, deel): **kolen 111 legs / 0 kapot / 0 straight / 0 degen / 0 unresolved via**, regressievrij. Route-bug gefixt (Roberts Bank ingesloten → Ridley/Prince Rupert). `build-standalone.py` (+5 kolen-checks) → `atlas-standalone.html` geregenereerd.
- [x] Code-commit `75c3483` (repo `main`, Claude-trailer) — **alléén eigen bestanden** gestaged (sectie J: 3 parallelle sessies grafiet/diamant/gas ongemoeid; alléén de coal-regel uit de gedeelde `index.html` via gerichte patch).

**Open (M17 afronden):**
- [ ] **Code-commit `75c3483` pushen** naar GitHub → live op Pages (repo is sinds M13 live). *(Nog niet gepusht — zie onder.)*
- [ ] **Visuele bevestiging op de live URL/mobiel** (LAR-461, In Progress) — alleen Lars (WebGL-screenshot hangt headless), via https://larswalters.github.io/grondstoffen-atlas/. Checken: de grote binnenlandse blokken (China/India/VS/Rusland, dof) vs. de zeehandelslaag; de twee kolen (thermisch→centrales, cokeskool→staalhubs); de Mongolië-Gobi-landcorridor; het naspel van de Australië-ban (export naar India/Japan/Korea).

## M14 · Grafiet ✅ uitgevoerd (2026-07-15) — LAR-449 t/m 454
`data/graphite.js` van "basis" (10/3) → volledig **uitgewerkt** (31 nodes / 26 flows / 6 tensions). De vorm = een
**REE-achtige verwerkingstrechter met TWEE feedstocks**: natuurlijk vlokgrafiet + synthetische naaldcokes convergeren
op de anode-verwerking die **~90%+ in China** zit (Shandong natuurlijk, Binnen-Mongolië synthetisch). Schip+land,
**géén nieuw chokepoint** (4e na nikkel/olie/zilver). Grafiet was het **laatste basis-10-bestand** (bestond al + stond
al in `index.html` → basis→uitgewerkt, géén nieuwe script-tag).
- [x] Research upstream (vlok + naaldcokes) / downstream (verwerkingstrechter + dec-2023 exportcontroles) inline in `design/grafiet.md` (LAR-449/450).
- [x] Ontwerp-brief `design/grafiet.md` (LAR-451): mijnen + naaldcokes-bronnen, anode-verwerkers, havens, gigafabrieken, recyclers, 6 tensions.
- [x] `data/graphite.js` uitgewerkt (LAR-452): 8 natuurlijke vlokmijnen (China #1, Balama/Mozambique, Madagascar, Brazilië, Tanzania, Noorwegen, Oekraïne, Sri Lanka vein) + 2 naaldcokes-bronnen (VS/China) + 8 anode-verwerkers (Shandong/Binnen-Mongolië-trechter + Japan/POSCO/Vidalia/Novonix/Talga/NMG) + 6 havens + 4 gigafabriek-markten + 3 recyclers. Keten erts(vlok+naaldcokes)→raffinaat(gecoat sferisch/gegrafitiseerd anodepoeder)→product(cellen).
- [x] **Recycling-toggle** (LAR-453) = hergebruik van het REE/PGM-`recycle`-patroon met **0 engine-wijziging** (`layer:"recycle"` op nodes én flows); bewust bescheiden (3 recyclers, batterijgrafiet-recycling nog nascent). Chip verschijnt automatisch.
- [x] Verificatie headless (LAR-454, deel): **grafiet 77 legs (57 zee + 20 land) / 0 kapot / 0 straight / 0 warnings**; toggle aan=80 (+3 recycle); regressie schoon (0 kapot over álle grondstoffen). Route-bug gefixt: `gr-ref-japan→gr-mkt-korea-japan` road→ship (Japan→Korea over de Straat van Korea). `build-standalone.py` (+5 grafiet-checks) → `atlas-standalone.html` geregenereerd.
- [x] Code-commit `34b1ed4` (repo `main`, Claude-trailer) — **alléén eigen bestanden** gestaged (`data/graphite.js`, `design/grafiet.md`, `build-standalone.py`, `.claude/launch.json`; sectie J). **Gepusht** naar GitHub → live op Pages.

**Open (M14 afronden):**
- [ ] **Visuele bevestiging op de live URL/mobiel** (LAR-454, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless), nu triviaal via https://larswalters.github.io/grondstoffen-atlas/. Checken: de twee feedstock-stromen (vlok + naaldcokes) die op China convergeren, het emblematische Balama→Vidalia-draadje rond de Kaap, de dunne ex-China buildout-waaier (Talga/Novonix/NMG/POSCO), en de recycling-toggle (default uit).

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

## Verderop — geen grondstoffen meer op "basis" (atlas inhoudelijk compleet)
**Alle 11 uitgewerkt** (lithium, kobalt, goud, koper, uranium, REE, nikkel, olie, PGM, zilver, grafiet). Het brief→bouw-
runbook (sectie I) is voor alle basis-10 + zilver doorlopen. Toekomstig grondstof-werk = alleen nog een *nieuwe 12e+*
grondstof (zoals zilver een nieuw bestand + script-tag + build-check vergt), niet meer een basis→uitgewerkt-upgrade.

**Nog open (niet-inhoudelijk):**
- [ ] **Visuele bevestigingen per milestone** (Lars, In Progress): LAR-415 (uranium), 421 (REE), 427 (nikkel), 433 (olie),
      439 (zilver), 445 (PGM), 454 (grafiet). Nu triviaal via de live GitHub-Pages-URL.
- [ ] **PGM-backlog-afwijkingen:** LAR-447 (recycle-chip-tooltip generiek maken — nu REE-bewoord in de gedeelde `ui.js`,
      raakt nu óók grafiet), LAR-448 (optionele Pt/Pd-exchange-laag — pure data).
- [ ] Bureaublad-originelen opruimen (`atlas-lithium-kobalt.html` + `globe-oud`) ná visuele bevestiging.

**Repo-status (gecorrigeerd 2026-07-15):** de repo is **niet** lokaal-only — hij staat op GitHub (`larswalters/grondstoffen-atlas`)
en draait **live op GitHub Pages** (https://larswalters.github.io/grondstoffen-atlas/); **elke `git push origin main` deployt**.
`atlas-standalone.html` blijft gitignored (gegenereerd). De "lokaal-only"-notities in oudere milestones zijn achterhaald.
