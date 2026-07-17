# Grondstoffen Atlas — project spec

*Categorie: General · Linear-project: "Grondstoffen Atlas" (team Lars / LAR) · Laatst bijgewerkt: 2026-07-17 (weergave-fixes LAR-479 + LAR-481 bevestigd; M18 koper-pilot nog IN TEST)*

> **✅ WEERGAVE-FIXES BEVESTIGD (2026-07-17) — LAR-479 + LAR-481 Done, live op Pages.** Lars pauzeerde de koper-pilot
> bewust: *"als we dat eerst fixen voordat we de routes doen lijkt me beter."* Drie bugs, alle drie visueel bevestigd
> (*"ze werken zoals het hoort nu"*). **(1) Tegel-afkap (LAR-479)** — twee oorzaken: `maxTiles: 40` was **kleiner dan
> één patch** (42–72 tegels) terwijl `updateDetail` **noord→zuid** vulde → zuidelijke rijen structureel wazig; én
> `detailZoomFor()` miste **`cos(lat)`** (Mercator-tegel op 60° = halve grond → hoge breedten vroegen méér tegels voor
> dezelfde scherpte; Noorwegen 33%/0% dekking). Fix: `cos(lat)` + budget **96** + patch vult **van het midden naar
> buiten**. **(2) Zoom-evenredig draaien** — `dragSpeed`/`dragRefZoom`, geankerd op de startzoom (28,65°/100px
> onveranderd; volle zoom 3,13°). **(3) Marker-LOD vuurde AVERECHTS (LAR-481)** — `forced` overrulet tier voor **57 van
> de 63** koper-nodes → de tier-regel raakte **alléén de 6 context-mijnen zónder stroom**; Chuquicamata plofte in beeld,
> Los Pelambres (zelfde share, wél stroom) niet. **Markers verdwijnen niet meer op tier; `tier` stuurt alleen nog de
> labels.** Regressie 14 grondstoffen: pop-in 0. Commits `297016f` + `8dda38e`.
>
> ⚠️ **Twee engine-feiten die veranderd zijn — voor wie hierna code schrijft:**
> `CONFIG.markers.tierZoom` **bestaat niet meer** (tier ≠ marker-zichtbaarheid; alleen `labelZoomByTier` leeft nog), en
> `main.js` heeft **geen `usedNodeIds()`** meer (de `forced`-uitzondering was overbodig zodra markers niet meer op tier
> verdwijnen). De M16/LAR-471-notitie hieronder noemt de `usedNodeIds`-gate nog als onderdeel van het optionele-laag-
> patroon — **dat was juist tóén, maar geldt niet meer**; sectie I's stappenplan (5 plekken) was er nooit van afhankelijk
> en klopt onverkort. Zie `memory/decisions.md`.

> **🧭 KOERSWIJZIGING (2026-07-17) — EERST DE ROUTES, DAN DE FEATURES.** De atlas is inhoudelijk compleet
> (14 grondstoffen, backlog leeg), maar de volgende stap is bewust **géén 15e grondstof**: de routing is
> **aantoonbaar onrealistisch** en de drie geplande features **staan erop**. Lars: *"een boot zou daar nooit zo
> varen."*
>
> **Diagnose (`searoute.js`, 3 samenwerkende oorzaken):** (1) **`openRadiusDeg: 1.2`** = een schijf van ~130 km
> **geforceerd water** rond élk knelpunt — bedoeld om smalle straten (~35 km) open te houden in het grove raster,
> maar het zet óók land op "water" → A\* vaart vlak bij een knelpunt dwars over schiereilanden/eilandjes
> (**hoofdboosdoener**); (2) **8-richtingen-A\*** → trapjes (Golf→Rotterdam = **33 richtingswissels**); (3) **grof
> 0,25°-raster + `heuristicWeight: 1.35` + géén echte vaarlanen** → het vindt het kortste *watertraject*, niet de
> lane die schepen varen → kaarsrechte runs langs een breedtegraad.
>
> **Hard bewijs — Antofagasta→Shanghai:** grote-cirkel **18.526 km** · **searoute** (echte lanen, noordelijk tot
> 50,7°N) **18.880 km (+2%)** · **onze bol** (zuidelijk via `wp-pac-zuid` op 26°Z) **19.970 km (+8%)** → het
> **handgeplaatste vaarpunt dwingt ~1.090 km omweg af**. De `via`-ketens blijken grotendeels **handmatige
> compensatie voor een slechte router**.
>
> **→ M18 · Realistische zeeroutes (searoute):** routeren over een **echt scheepvaart-lanen-netwerk** (Eurostat
> MARNET, Python-pakket `searoute` 1.6.0 — al geïnstalleerd). **Precompute at build-time, gededupliceerd per
> haven-paar** (één gedeelde corridor-cache over alle 14 — *"routes zijn vaak hetzelfde"* → unieke corridors, niet
> elke flow); polylines in `data/_searoutes.js`, atlas rendert direct; **netwerk bewaren** zodat M21 een knelpunt
> blokkeert als *edge eruit → herrouteren*; **raakt alleen zee-legs** (land/lucht ongemoeid); runtime blijft pure
> JS, `searoute` = **build-dependency**. Bonus: A\* uit de runtime = lichter op mobiel.
>
> **Feature-trio hernummerd:** M18→**M19** (knelpunt-stress) / M19→**M20** (China-meta-view) / M20→**M21**
> (disruptie-simulator). **M21's aanpak is herijkt**: knelpunt blokkeren = *edge uit het netwerk*, niet een
> raster-cel-masker. **Pilot-first: koper** (LAR-474) → go/no-go Lars → dan de andere 13.
>
> **⚠️ Harde regel:** vergelijk **nooit** tegen een kale origin→dest A\*-run. De pilot van 2026-07-16 deed dat →
> "route A", een pad dat de bol **nergens tekent** (Lars: *"ik zie op onze wereldbol niets dat route A neemt"*).
> Vergelijk altijd tegen wat `flows.js` werkelijk rendert.
>
> **Open besluit (Lars, bij de pilot):** via-punten op zee-legs **opruimen** of **behouden als hint**.
> **Linear:** M18 · LAR-473..478 + **LAR-479** (High — tegel-patch wordt bij inzoomen afgekapt door `maxTiles: 40`;
> oorzaak bewezen) + **LAR-480** (Low — markers-contrast). Géén code gewijzigd in deze sessie.
> Zie `memory/decisions.md` + `memory/bugs-and-risks.md`.

> **BACKLOG LEEGGEWERKT (2026-07-16) — LAR-471 + LAR-447 + LAR-448, gepusht → live op Pages.** De 3 resterende
> backlog-issues afgerond. **LAR-471 · lab-grown-toggle (diamant)** = het **6e optionele-laag-patroon** (na goud-CB/koper-
> beurs/REE-recycle/olie-reserve/uranium-military): het `layer:"labgrown"`-patroon (zoals recycle, niet dedicated type) —
> 3 productie-nodes `type:"labgrown"` (China/Henan HPHT, India/Surat CVD, VS/Washington premium-CVD) + 6 flows die vooral de
> **VS-verlovingsringmarkt** ondergraven; 5 engine-plekken (config marker-size `labgrown:{size:0.030}` / main `showLabGrown`+
> `hasLabGrown()`+usedNodeIds-gate / flows-gate / markers-gate + **violette octaëder-marker** 0xB98BE0 / ui-chip "lab-grown"
> + TYPE_LABEL); default uit, chip alleen bij diamant; `dia-t-labgrown`-tension wijst nu naar de echte lab-grown nodes/flows.
> **LAR-447 · recycle-tooltip per-grondstof** = de gedeelde chip-tooltip was hard-coded REE-bewoord ("magneetschroot, <5%"),
> fout voor PGM (~25% autokat)/grafiet → nu via een `recycleHint`-veld op de resource + `main.recycleHint()` + generieke
> fallback in `ui.js` (hints op REE/PGM/grafiet). **LAR-448 · PGM-beursvoorraden-laag** (Lars akkoord ondanks de "één toggle
> per grondstof"-conventie) = PGM's **tweede** optionele toggle naast recycling; pure data, 0 engine-wijziging (hergebruik
> koper/nikkel/zilver-exchange-toggle): 3 kluis-nodes (LPPM/NYMEX/TOCOM) + 3 `layer:"exchange"`-bufferflows naar de autokat-
> markten → **PGM = eerste grondstof met twee toggles naast elkaar**. Headless (poort 8732 + verse load 8733): diamant **41
> legs (31 air+10 road) / 0 kapot / 0 straight / 0 degen** (toggle uit=35/25 aan=41/28, +34 scene-meshes); PGM **52 legs /
> 0 kapot** (exchange-toggle +3/+3; beide chips alleen bij PGM); regressievrij (`totalBroken=0`), 0 console-errors.
> **Cache-gotcha:** de Browser-pane cachet script-tag-files hardnekkig (geen no-cache op python `http.server`) → engine
> gevalideerd via in-memory injectie + een **tweede server-instance op 8733** (schone origin). `build-standalone.py` +4
> checks, `atlas-standalone.html` geregenereerd. Commits `f6c95f6` (feat 471) + `9feb8f2` (fix 447+448), **gepusht**
> (`5d4d469..9feb8f2`) → live op Pages. **Linear LAR-471/447/448 → Done; de backlog is nu leeg.** Toekomstig werk = alleen
> nog een nieuwe 15e grondstof of losse verfijningen. (Stale-notitie gecorrigeerd: M17-kolen stond al op origin/main.)

> **M15 · GAS UITGEVOERD (2026-07-16) — DE NIEUWE 12e GRONDSTOF (aardgas/LNG):** net als zilver (M13)/diamant/kolen een
> échte nieuwe grondstof (niet basis→uitgewerkt): nieuw `data/gas.js` (42 nodes / 51 flows / 6 tensions) + brief
> `design/gas.md` + `<script src="data/gas.js">` in `index.html` + 5 gas-checks in `build-standalone.py`. **De vorm = de
> natuurkunde: gas is nauwelijks te verplaatsen** → twee gescheiden leversystemen op de kaart: lage donkere **pijpleiding-
> arcs** (captive/regionaal — Rusland↔EU was, Power of Siberia→China, Turkmenistan→China, Noorwegen→EU) náást heldere
> **LNG-oceaan-arcs** (globaal). **De liquefactie-stap is de trechter** (institutioneel/kapitaal, geen zeestraat):
> capaciteit bij drie polen (VS-Golfkust/Qatar/Australië). Qatar via **Hormuz** (géén Yanbu/Fujairah-bypass — scherper dan
> olie). Stages: `erts` = veldgas + pijpleidinggas → `raffinaat` = LNG (het verhaal) → `product` = geleverd. Liquefactie=
> `refinery`, regas=`port`, opslag=`reserve`; schip + `pipeline` → **géén nieuwe render-modus/marker-types/chokepoint**
> (4e na nikkel/olie/zilver). 6 tensions (Hormuz, liquefactie-flessenhals, Europa-pivot 2022, Russische oost-pivot, drie
> prijszones, Panama-LNG-knelpunt); Iran = reserves≠export. **Opslag-laag = hergebruik olie-`reserve`-toggle, 0 engine-
> wijziging** (`hasReserves()` generiek, `src/main.js:23`): 4 reserve-nodes + 5 vul-flows; EU-winter-vulgraad = de metric.
> Headless (poort 8736): **gas 97 legs / 0 kapot / 0 straight / 0 onbekende via-ids**, regressievrij; de 2 Arctische Yamal-
> routes + captive-pijpleidingen routeren correct zónder nieuw vaarpunt (empirisch). `atlas-standalone.html` geregenereerd
> (5 gas-checks OK). Commits `040d2b7` (gas.js+gas.md) + `a8378ef` (build-checks), **gepusht → live op Pages** (alléén
> eigen bestanden; git-index-race met de diamant-sessie teruggedraaid met `reset`+`--only` — les: `git commit <paths>`/
> `--only` is race-bestendiger bij een gedeelde tree, sectie J). **Linear M15 · LAR-460/462/463/464/466 Done, 465 In
> Progress** (visueel = Lars). Milestones hernummerd: Gas=M15 / Diamant=M16 / Kolen=M17.

> **M16 · DIAMANT UITGEVOERD (2026-07-16) — DE NIEUWE 12e GRONDSTOF:** net als zilver (M13)/gas (M15) een échte nieuwe
> grondstof (niet basis→uitgewerkt): nieuw `data/diamond.js` (25 nodes / 35 flows / 6 tensions) + brief `design/diamant.md`
> + `<script src="data/diamond.js">` in `index.html` + 4 diamant-checks in `build-standalone.py`. Milestones liepen t/m M14
> (grafiet); M15 was door de gas-sessie bezet → diamant = **M16**. De vorm = **de scherpste DOWNSTREAM-trechter van de
> atlas**: winning verspreid (Rusland/Alrosa #1 op **volume**, Botswana/Debswana #1 op **waarde**, Canada, Angola, Zuid-
> Afrika, Zimbabwe, Namibië-marien, Lesotho; **Argyle gesloten 2020** = schaarste-verhaal; volume-vs-waarde via `note`),
> maar **~90-95% van álle diamant wordt geslepen/gepolijst in één stad: Surat (Gujarat)** — scherper nog dan de China-
> raffinage of Ganzhou-scheiding; alle rough-arcs convergeren op Surat. **Antwerpen** = het verplichte **G7-
> certificeringsknooppunt** (sanctie op Russische/Alrosa diamant, maart 2024) → fysieke omweg mijn→Antwerpen→Surat,
> terwijl de **Alrosa-rough zichtbaar om Antwerpen heen buigt** via Dubai/direct India ("de stroom buigt om, niet weg").
> De Beers-sights via Gaborone. Diamant **vlíégt** (beveiligde koeriers) → **hergebruik van de goud/PGM air-mode**
> (`mode:"air"`), **0 engine-wijziging, géén nieuw chokepoint, géén nieuwe marker-types** (`hub`=Antwerpen/Dubai/Gaborone/
> Mumbai; `refinery`=slijperij Surat/China). Korte hops binnen een land = `road`. Keten 3 stages (erts=rough → raffinaat=
> polished bij Surat → product=sieraad; VS #1 ~50%). 6 tensions: Surat-trechter, De Beers/Alrosa-duopolie, Antwerpen-
> certificering, Alrosa/G7-sanctie, **lab-grown-ontwrichting**, waarde-vs-volume + Botswana-beneficiation. **Twee "anders"-
> punten → aparte issues** (Lars' verzoek): LAR-470 (plumbing, zoals zilvers LAR-436) + de **lab-grown-toggle** (LAR-471,
> `layer:"labgrown"`, 5 engine-bestanden) **bewust in de backlog** i.v.m. de parallelle sessies (zoals uranium's LAR-414 /
> olie's LAR-432); in v1 leeft lab-grown als `tension`. Headless (poort 8734): **diamant 35 legs (27 air + 8 road) /
> 0 kapot / 0 straight / 0 degen**, 0 warnings, regressievrij; 1 kust-artefact-landhop (Dubai→Golf) → `air` voor 0 straight.
> `atlas-standalone.html` geregenereerd (4 diamant-checks OK). Commits `72d134c` (feat) + `7d06a0c` (build), **gepusht →
> live op Pages** (`8497f24..7d06a0c`, fast-forward, alléén eigen commits — 4 parallelle sessies grafiet/kolen/gas/diamant,
> sectie J; de meeliftende `gas.js`-tag verwees al naar de gecommitte gas.js → consistent, geen duplicaat). **Linear M16 ·
> Diamant + LAR-467..472:** 467/468/469/470 Done, 472 In Progress (visueel=Lars), 471 Backlog.

> **M17 · KOLEN UITGEVOERD (2026-07-16) — DE NIEUWE 12e GRONDSTOF:** na zilver (11e) de tweede écht nieuwe grondstof
> (kolen zit niet in de basis-10): nieuw `data/coal.js` (34 nodes / 33 flows / 6 tensions) + brief `design/kolen.md` +
> `<script src="data/coal.js">` in `index.html` + `grens-gashuunsukhait` (Mongolië-Gobi) in `_chokepoints.js` + 5 kolen-
> checks in `build-standalone.py`. De vorm is **fundamenteel anders**: **géén mondiale flessenhals** want kolen is
> overweldigend **binnenlands** — ~85% verstookt waar gedolven (China ~50% van de wereld, India, VS, Rusland), slechts
> ~15% van de ~8.700 Mt gaat over zee. De kaart toont grote binnenlandse blokken (`erts`+`product`) tegenover een dunnere
> **zeehandelslaag** (`raffinaat` = de internationaal verhandelde bulk, waar élk ban/her-routeringsverhaal leeft).
> **China = swing-koper** (grootste producent én importeur). **Twee kolen** (thermisch→stroom vs. cokeskool→staal) via
> `note`+`tension` (nikkel-patroon). **Drie her-routeringen** (tensions): China-Australië-ban (2020-2023), Rusland-oost-
> draai (2022→), Mongolië-Gobi-corridor. Grondstof-eigen "nieuwe element" = **één LANDknelpunt** `grens-gashuunsukhait`
> (Tavan-Tolgoi-cokeskool over de Gobi → Chinees staal; Kasumbalesa/Ruili-patroon; alléén kolen verwijst ernaar →
> regressievrij). Schip+land, **géén nieuwe render-modus, géén nieuwe marker-types, géén optionele toggle-laag** (kolen
> heeft geen zinvol CB/beurs/recycling-equivalent). Kolen = **4e** grondstof (na nikkel/olie/zilver) zonder nieuw **zéé**-
> knelpunt. Headless (poort 8735): **kolen 111 legs / 0 kapot / 0 straight / 0 degen**, regressievrij; route-bug empirisch
> gefixt (Canadese haven Roberts Bank ingesloten in de Salish Sea → **Ridley/Prince Rupert** open kust). Commit `75c3483`
> (lokaal, Claude-trailer, **alléén eigen bestanden** — 3 parallelle sessies grafiet/diamant/gas ongemoeid, sectie J: de
> gedeelde `index.html` kreeg diamond/coal/gas in één hunk → alléén de coal-regel gestaged via `git apply --cached`).
> **Linear M17 · Kolen + LAR-455..459 Done, 461 In Progress** (visuele bevestiging = Lars). De atlas telt nu **14
> grondstoffen** (basis-10 + zilver + gas M15 + diamant M16 + kolen M17); gas + diamant lopen in parallelle sessies.

> **M14 · GRAFIET UITGEVOERD (2026-07-15) — DE ATLAS IS INHOUDELIJK COMPLEET (11/11):** `data/graphite.js` van "basis"
> (10/3) → **uitgewerkt** (31 nodes / 26 flows / 6 tensions) + brief `design/grafiet.md` + 5 grafiet-checks in
> `build-standalone.py`. Grafiet was het **laatste basis-10-bestand** (bestond al + stond al in `index.html` →
> basis→uitgewerkt, géén nieuwe script-tag). De vorm = een **REE-achtige verwerkingstrechter met TWEE feedstocks**:
> **natuurlijk vlokgrafiet** (China #1 ~65%, Balama/Mozambique, Madagascar, Brazilië, Tanzania) én **synthetisch grafiet**
> uit petroleum-**naaldcokes** convergeren op de anode-verwerking die **~90%+ in China** zit (Shandong natuurlijk,
> Binnen-Mongolië synthetisch op goedkope kolenstroom) — **zelfs ex-China vlok vaart naar China** om verwerkt te worden
> (de Ganzhou-REE-parallel). Levende geopolitiek: de **China-exportvergunningen op grafiet (dec 2023)**. Dunne ex-China
> buildout (Syrah Vidalia/Louisiana uit Balama-vlok, Talga/Novonix/NMG/POSCO). Schip+land, **géén nieuwe render-modus,
> géén nieuw chokepoint** (4e na nikkel/olie/zilver); recycling-toggle hergebruikt het REE/PGM-patroon met **0 engine-
> wijziging** (bewust bescheiden, batterijgrafiet-recycling nog nascent). Headless (poort 8735): **grafiet 77 legs
> (57 zee + 20 land) / 0 kapot / 0 straight / 0 warnings**, toggle aan=80, regressie schoon (0 kapot overal). Route-bug
> gefixt (`gr-ref-japan→gr-mkt-korea-japan` road→ship). `atlas-standalone.html` geregenereerd (5 grafiet-checks OK).
> Commit `34b1ed4` (Claude-trailer, **alléén eigen bestanden** — sectie J; **gepusht** → live op GitHub Pages). **Linear
> M14 · Grafiet + LAR-449..454** (449–453 Done, 454 In Progress = visuele bevestiging Lars). **Geen grondstoffen meer op
> "basis".** ⚠️ **Repo-correctie:** de "repo lokaal-only"-notities hieronder zijn achterhaald — de repo staat op GitHub
> (`larswalters/grondstoffen-atlas`) en draait live op **GitHub Pages** (https://larswalters.github.io/grondstoffen-atlas/);
> elke `git push origin main` deployt.

> **M13 · ZILVER UITGEVOERD (2026-07-15):** de **eerste écht nieuwe grondstof** sinds de basis-10 (niet basis→uitgewerkt):
> nieuw `data/silver.js` (42 nodes / 37 flows / 6 tensions) + brief `design/zilver.md` + `<script src="data/silver.js">` in
> `index.html` + 5 zilver-checks in `build-standalone.py`. De vorm is **fundamenteel anders**: zilver heeft **géén enkel
> geografisch knelpunt** — de knijp is tweezijdig en structureel: (1) **aanbod-inelasticiteit** (~70-75% is **bijproduct** van
> zink/lood/koper/goud; mijn-nodes = eigenlijk andermans mijnen, elk met een hoofdmetaal-`note`), (2) **vraagconcentratie** (de
> energietransitie trekt zilver naar de **Chinese zonnepanelen-industrie**; PV = grootste + snelst groeiende toepassing) →
> een **structureel tekort** dat de kluisvoorraden (LBMA/COMEX/SGE) aftapt. Schip+land (industrieel metaal, géén goud-luchtmodus),
> **géén nieuwe render-modus, géén nieuw chokepoint** (derde na nikkel/olie op de bestaande routekaart), géén nieuwe marker-types.
> Keten op de 3 stages: erts=mijn(bijproduct)→doré/concentraat / raffinaat=good-delivery baar / product=industrieel (solar/
> elektronica/sieraad). Mexico als winning+raffinage-anker (Fresnillo + Peñoles/Torreón). **Kluis-/beursvoorraden-laag** =
> hergebruik van de bestaande `exchange`-toggle met **0 engine-wijziging** (nikkel-patroon, 2e datagedreven hergebruik): 3
> exchange-nodes (LBMA/COMEX/SGE) + 3 `layer:"exchange"`-aftap-flows; recycling always-on. Twee route-bugs empirisch gefixt
> (VS-raffinage Tacoma→Astoria open kust; China-solar Suzhou-binnenland→Jiangsu-kust). Headless (poort 8734): **zilver 85 legs /
> 0 kapot / 0 straight / 0 warnings**, regressievrij (andere uitgewerkte grondstoffen 0/0). `atlas-standalone.html` geregenereerd
> (5 zilver-checks OK). Commit `e091848` (lokaal-only, Claude-trailer, **alléén eigen bestanden** — parallelle uranium-toggle-sessie
> op de gedeelde engine-files ongemoeid, sectie J). **Linear M13 · Zilver + LAR-434..438 Done, 439 In Progress** (visuele
> bevestiging Netlify/mobiel = Lars). M12 = PGM (uitgevoerd, zie onder); alleen **grafiet** nog op "basis".

> **M12 · PGM UITGEVOERD (2026-07-15):** `data/pgm.js` van "basis" (9/3) → **uitgewerkt** (38 nodes / 41 flows / 6 tensions).
> De **scherpste twee-landen/twee-metalen-concentratie** van de atlas: **Zuid-Afrika/Bushveld** = Pt/Rh (~70%/~80%, dichte
> kluwen schachtmijnen bij Rustenburg + Noord-/Oostrand), **Rusland/Norilsk** = Pd (~40%, Ni-Cu-bijproduct). PGM **vliegt**
> (per kilo even waardevol als goud) → **hergebruik van de goud-air-mode** (`mode:"air"`, JNB-gateway; tijdlijn toont
> automatisch "✈ vluchten" via `activeHasAir()`); concentraat/matte over land (Beitbridge/Kanaaltunnel/Baltische bruggen).
> **Géén nieuw chokepoint, géén engine-wijziging** (derde na koper/nikkel). **Recycling-toggle** (`layer:"recycle"`, ~25%
> autokat via JM/BASF/Umicore/Heraeus/Tanaka) = hergebruik van het REE-patroon met **0 engine-wijziging** (chip via
> `hasRecycle()`). 6 tensions: twee-landen-concentratie, autokat-leiband + Pt↔Pd-substitutie, rodium-spof, palladium/Rusland-
> sanctie, waterstof-hedge (Pt/Ir PEM-elektrolyse), Eskom-stroomcrisis. Headless (poort 8732): **pgm 49 legs / 0 kapot /
> 0 straight / 0 degenerate arcs**, regressievrij (SAMECELL-fix: Japan-recycler uit Tokyo Bay → Kanagawa). `atlas-standalone.html`
> geregenereerd (4 PGM-checks OK). Commit `2c4b668` (lokaal-only, Claude-trailer, **alléén eigen bestanden** — parallelle
> zilver-/uranium-toggle-sessie ongemoeid, sectie J). **Linear M12 · PGM + LAR-440..448** (5 Done, 445 In Progress = visuele
> bevestiging Lars, 446 Done na de build, 447/448 Backlog = afwijkingen: REE-bewoorde recycle-tooltip + optionele Pt/Pd-exchange-laag).

> **M11 · OLIE UITGEVOERD (2026-07-15):** `data/oil.js` van "basis" (18/15) → **uitgewerkt** (45 nodes / 46 flows /
> 6 tensions). Olie's vorm is bewust **anders dan alle eerdere**: geen enkele trechter maar het **hele knelpunten-
> netwerk dat tegelijk oplicht** — data bevestigt Hormuz #1 (15 stromen), Malakka, Taiwan, Suez/Bab, Bosporus, Panama,
> Kaap (10 knelpunten). Daarom **géén nieuw chokepoint** (= het eigen aha); wel 3 olie-only navigatie-vaarpunten
> (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`) in `_chokepoints.js`. Drie levende verhalen: de **Hormuz-bypass-
> pijpleidingen** (Saoedi→Yanbu, UAE→Fujairah), de **Rusland-omleiding 2022→** (Europese crude → India/China via
> Primorsk/Novorossiysk/ESPO-Kozmino/Druzhba) en de **Amerikaanse schalie-ommekeer** (Corpus Christi export). Keten op
> 3 stages: erts=ruwe olie / raffinaat=producten / product=petrochemie; schip+pijpleiding, **géén nieuwe render-modus**.
> Optionele **SPR-voorraden-toggle** (`layer:"reserve"`) eerst uitgesteld tijdens de parallelle nikkel-sessie, **daarna
> alsnog gebouwd** (LAR-432 Done, commit `86c8c1f`) = het **vierde** optionele-laag-patroon (goud-CB/koper-beurs/REE-recycling/
> olie-reserve): 5 SPR-nodes (`type:"reserve"`, `stock` mln vaten) + 5 vul-flows + tension, olie-amber tank-marker, chip
> "voorraden" alleen bij olie. Headless: **olie 210 legs / 0 kapot / 0 straight** (232 incl. reserve); toggle uit=45/46,
> aan=50/51; regressievrij. `atlas-standalone.html` geregenereerd (olie- + reserve-checks OK). Commits `1d4ece5` (data) +
> `86c8c1f` (toggle), lokaal-only, Claude-trailer. **Linear M11 · LAR-428..432 Done, 433 In Progress.** Rest = visuele bevestiging Netlify/mobiel (Lars).

> **M10 · NIKKEL UITGEVOERD (2026-07-15):** `data/nickel.js` van "basis" (13/4) → **uitgewerkt** (50 nodes / 46 flows /
> 6 tensions). De nikkel-"aha": de **trechter staat op z'n kop** t.o.v. koper — waar koper/lithium breed graven en in
> China raffineren, heeft **Indonesië in tien jaar de mijn ÉN de raffinage** naar zich toe getrokken via de **exportban
> op ruw erts** (IMIP Morowali / IWIP Weda Bay, Chinees kapitaal Tsingshan/Huayou); het erts blíjft in het land (korte
> mijn→smelter-hops). Plus **twee nikkels** (class-1 batterij/sulfaat vs class-2 roestvrij/NPI, met HPAL→MHP/matte als
> brug), de **prijscrash-shakeout** (BHP Nickel West stilgelegd 2024, Nieuw-Caledonië in crisis), de **LME-nuance**
> (alleen class-1 leverbaar + de 2022-squeeze) en het **Filipijnse ruw-erts-contrast** (geen ban). Schip+land, **géén
> nieuwe render-modus, géén nieuw chokepoint** (hergebruikt Makassar/Lombok/SCS/Taiwan/Deense-Straten/Panama/Saint-Laurent).
> **Beursvoorraden-laag (LME)** hergebruikt de **bestaande** exchange-toggle van koper met **0 engine-wijziging**
> (bevestigd generiek); recycling always-on. Headless: **nikkel 91 legs (63 zee + 18 land + 10 korte hops) / 0 kapot /
> 0 straight**, regressie schoon (0 kapot over alle grondstoffen). `atlas-standalone.html` geregenereerd (nikkel-checks OK).
> Commit `08aa4f5` (lokaal-only, Claude-trailer). **Linear M10 · LAR-422..426 Done, 427 In Progress** (visuele bevestiging =
> Lars). Overige op "basis": grafiet, PGM (olie loopt in een parallelle sessie).

> **M8 · ZELDZAME AARDMETALEN UITGEVOERD (2026-07-15):** `data/rare-earths.js` van "basis" (9/5) → **uitgewerkt**
> (41 nodes / 38 flows / 6 tensions) in de **magneet-REE-framing** (NdPr licht + Dy/Tb zwaar; `symbol: NdPr`,
> `unit: kt magneet-REO/jaar`). De **extreemste trechter** van de atlas: winning breed verspreid, scheiding ~85–90%
> Zuid-China (**Ganzhou**). Vier kern-aha's: Ganzhou-scheidingstrechter, **Dy/Tb-landstroom Myanmar→China** over de
> nieuwe grenscorridor **`grens-ruili`** (`_chokepoints.js`, Kasumbalesa-patroon), de **Mountain-Pass-rondreis**
> (concentraat heen over de Stille Oceaan, oxide terug) en de **NdFeB-magneet-waaier** vanuit China. Nieuwe
> **recycling-toggle** (`layer:"recycle"`, default uit) = het derde optionele-laag-patroon (goud=CB, koper=beurs,
> REE=recycling), bewust via `layer` op flows én nodes zodat koper's always-on recyclers ongemoeid blijven. Headless:
> **rare-earths 90 legs / 0 kapot / 0 straight**, regressievrij. `atlas-standalone.html` geregenereerd (REE-checks OK).
> **Linear M8 · LAR-416..420 Done, 421 In Progress.** Rest = visuele bevestiging Netlify/mobiel (Lars). Repo lokaal-only, `main`.

> **M9 · URANIUM UITGEVOERD (2026-07-15):** `data/uranium.js` van "basis" (9/2) → **uitgewerkt** (38 nodes / 36 flows /
> 6 tensions). Eerste grondstof met een bewust *andere vorm* — een **4-staps kernbrandstofketen** (winning → conversie →
> verrijking → splijtstof → reactor) met de **verrijking (~44% Rusland) als raffinaat-flessenhals**. Nieuw: de
> **Trans-Kaspische route** om Rusland heen (3 Kaspische vaarpunten + Dardanellen in `_chokepoints.js`), de **VVER-lock-in**
> en de **CANDU-uitzondering**. Headless: **uranium 54 legs / 0 kapot**, regressievrij. Commits `d016ab8` (brief) + `76c0333`
> (data). Linear-milestone **M9 + LAR-410..415**. Rest = visuele bevestiging (LAR-415). **Militaire-kringloop-toggle (LAR-414)
> ALSNOG GEBOUWD (2026-07-15, commit `6a6d062`):** het 5e optionele-laag-patroon (`type:"military"`/`layer:"secondary"`, down-blend/
> tails/reserves; Megatons-to-Megawatts) — headless uranium 60 legs / 0 kapot / 0 straight, toggle +4 nodes/+5 flows, chip alleen bij uranium.

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
- **Deploy:** ✅ **live op GitHub Pages** — https://larswalters.github.io/grondstoffen-atlas/ (repo `larswalters/grondstoffen-atlas`, public, branch `main` root, met een `.nojekyll` zodat `data/_registry.js`/`data/_chokepoints.js` geserveerd worden). **Elke `git push origin main` werkt de live site bij** (~1-2 min rebuild) — dit is nu de "bekijk-op-elk-apparaat"-deploy (2026-07-15). Netlify (drag-and-drop van de single-file) blijft als alternatief bestaan. NB: directe Google-API-egress is op deze machine geblokkeerd (Drive-upload via SA lukt niet vanaf hier; GitHub werkt wél).
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

- **2026-07-17 · `tier` stuurt de LABELS, niet de markers (LAR-481)** — de tier-LOD verborg in de praktijk alléén de
  context-nodes zónder stroom: `forced` (uit `usedNodeIds`) overrulet tier, en dat gold voor **57 van de 63** koper-
  nodes. Chuquicamata (share 1,6, géén stroom) plofte in beeld terwijl Los Pelambres (1,6, wél stroom) bleef staan →
  zichtbaarheid hing af van een toevallig lijntje, niet van belang. Markers staan er nu altijd; de **labels**
  (`labelZoomByTier` + botsingsdetectie) doen het decluttering-werk — dat is ook wat de kaart werkelijk rustig houdt.
  `tierZoom` + de `forced`/`usedNodeIds`-uitzondering **verwijderd** (het gevaar dat ze afdekten kan niet meer
  optreden). Alternatief "stromen óók tieren" bewust ná M18 (raakt `flows.js` = pilot-code, en alle 14).
- **2026-07-17 · Tegelbudget = noodrem, niet dagelijkse limiet + `cos(lat)` in de tegel-zoom (LAR-479)** — `maxTiles: 40`
  was kleiner dan één patch (42–72) → liep bij normaal inzoomen áltijd leeg, en de noord→zuid-vulling gooide dat verlies
  op de onderste rijen. Budget → **96**, patch vult **van het midden naar buiten** (bij een hit verlies je de bolrand,
  niet de halve onderkant). Losse tweede oorzaak: `detailZoomFor()` miste **`cos(lat)`** → hoe noordelijker, hoe méér
  tegels voor dezelfde scherpte (verspilling én de reden dat hoge breedten veel erger waren). `shellMaxZ: 3` ongemoeid.
- **2026-07-17 · Draaien schaalt met de camera-afstand, geankerd op de STARTZOOM** — een vaste rad/px maakte de bol op
  volle zoom ~9× te gevoelig (je ziet dan 9× minder wereld). Bewust niet fysisch 1:1 gemaakt: Lars klaagde alleen over
  ingezoomd, en 1:1 zou de startzoom 4,4× trager maken. De wet is identiek aan 1:1 (evenredig met camera→oppervlak),
  alleen de gain komt uit het bestaande gevoel. Knoppen: `CONFIG.globe.dragSpeed` + `dragRefZoom`.
- **2026-07-17 · De zee-A\* wordt vervangen door een echt vaarlanen-netwerk (M18)** — de routing is aantoonbaar
  onrealistisch (`wp-pac-zuid` dwingt ~1.090 km omweg af op Antofagasta→Shanghai: onze bol +8% vs. grote-cirkel,
  searoute +2%) en de features M19/M20/M21 stáán erop. Precompute at build-time, **gededupliceerd per haven-paar**;
  netwerk bewaren voor M21 (*edge eruit → herrouteren*); **alleen zee-legs**; `searoute` = build-dependency.
  Pilot-first met koper. **Feature-trio hernummerd** M19/M20/M21. Open besluit (Lars): via-punten opruimen of als hint houden.
- **2026-07-17 (pilot) · "MARNET beslist"** — zee-corridors kaal **haven→haven**, óók echte knelpunten niet meer
  als via afdwingen (de pilot vond `wp-taiwan` in ketens waar het niet hoort: +1.497 km); knelpunt-ringen +
  `laneShape`-ankers worden **afgeleid uit de geometrie** (≤`chokeAnchorKm` 150). Diagnose-correctie: de 1.090 km
  was een route-A-meetfout (antipodaal; echt 231 km) — de winst is **−9,3% + gladheid + M21**, zie `design/zeeroutes.md`.
- **2026-07-17 (pilot) · Corridor-reparaties horen in de baker, verificatie op de gétekende curve** — de-zigzag +
  lokale A\*-landomleiding met kustbuffer (`tools/bake_searoutes.py`), kwaliteitscheck `tools/check_corridors.js`;
  én `util.js` bemonstert curves nu **adaptief** (invoerpunten nooit overslaan — uniforme sampling sneed spline over
  schiereilanden terwijl de data al schoon was). **Pilot-status: gebouwd, in visuele test — Japan-observatie +
  wereldbal-duidelijkheid open (zie `memory/next-actions.md`).**
- **2026-07-17 · Verificatie-regel: vergelijk nooit tegen een kale origin→dest A\*-run** — de atlas routeert altijd
  langs de `via`-keten; een kale run produceert paden die de bol nergens tekent ("route A", 16 juli). Vergelijk tegen
  wat `flows.js` werkelijk rendert. Idem methodisch: meet niet in een verborgen Browser-pane (`document.hidden` →
  rAF pauzeert; `GLOBE.start()` draait z'n body synchroon als workaround).
- **2026-07-16 · LAR-471 lab-grown-toggle = het 6e optionele-laag-patroon, via `layer` (niet dedicated type)** — de
  uitgestelde diamant-toggle gebouwd. Recycle-stijl `layer`-patroon (`type:"labgrown"` marker + `layer:"labgrown"` gate op
  nodes én flows), niet reserve/military-dedicated-type — want lab-grown is schaduw-*aanbod* dat de product-arcs ondergraaft.
  `hasLabGrown()` op `f.layer==="labgrown"`. 3 productie-nodes (Henan-HPHT/Surat-CVD/VS-CVD) + 6 flows naar vooral de VS-markt;
  violette octaëder-marker; 5 engine-plekken; default uit, chip alleen bij diamant.
- **2026-07-16 · LAR-447 recycle-tooltip per-grondstof via `recycleHint`-resourceveld** — de gedeelde `ui.js`-tooltip was
  hard-coded REE-bewoord ("<5% magneetschroot"), fout voor PGM (~25% autokat)/grafiet. `recycleHint`-veld + `main.recycleHint()`
  + generieke fallback; hints op REE/PGM/grafiet. Koper (recyclers zonder layer) ongemoeid.
- **2026-07-16 · LAR-448 PGM krijgt een TWEEDE optionele toggle (beursvoorraden) — conventie bewust doorbroken** — Lars akkoord
  ondanks "één toggle per grondstof". Pure data, 0 engine-wijziging (hergebruik exchange-toggle): 3 kluis-nodes (LPPM/NYMEX/
  TOCOM) + 3 `layer:"exchange"`-flows. PGM = eerste grondstof met twee toggles; precedent: een grondstof mag meerdere lagen dragen.
- **2026-07-16 · verificatie-gotcha: Browser-pane cachet script-tag-files** (geen no-cache op python `http.server`) — valideer
  via in-memory injectie + een tweede server-instance op een andere poort (schone origin), niet via `reload()`.
- **2026-07-16 · M17 kolen = de binnenlands-grondstof, géén trechter** — kolen heeft als eerste grondstof **géén enkele
  mondiale flessenhals**: ~85% wordt verbrand waar gedolven (China ~50%, India, VS, Rusland), ~15% zeehandel. Stages als
  ketenpositie: `erts` = mijn→haven/centrale · `raffinaat` = de **internationaal verhandelde bulk** (zeekruisingen +
  landcorridor, waar élk ban/her-routeringsverhaal leeft) · `product` = stroom/staal → binnenlandse kolen (erts+product)
  leest visueel anders dan verhandelde (mét raffinaat-zeeboog). **Twee kolen** (thermisch/cokeskool) via `note`+`tension`
  (nikkel-patroon, niet via stage). China = swing-koper; drie her-routeringen als tensions (Australië-ban/Rusland-oost-draai/
  Mongolië-corridor). **Géén render-modus/marker-types/toggle-laag.** Nieuwe 14e grondstof (plumbing als eigen issue LAR-457).
- **2026-07-16 · M17 één nieuw LANDknelpunt `grens-gashuunsukhait`** (Mongolië-China-Gobi, `kind:"grensovergang"`) in een eigen
  COAL-blok in `_chokepoints.js` — Kasumbalesa/Ruili-patroon; alléén kolen verwijst ernaar → regressievrij. Kolen = 4e grondstof
  (na nikkel/olie/zilver) zonder nieuw zéé-knelpunt. Route-bug: Canadese haven Roberts Bank ingesloten in de Salish Sea (dicht in
  het grove raster) → verplaatst naar Ridley/Prince Rupert (open kust; empirisch getest, zilver-Tacoma→Astoria-les herbevestigd).

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
- **2026-07-15 · M9 uranium = 4-staps keten op 3 stages** — winning + conversie = `erts` (feed), **verrijking = `raffinaat`
  (de flessenhals)**, splijtstof = `product`, reactoren = `market`. Node-types alle bestaand → géén nieuwe marker-styling.
  De verrijkings-knijp (~44% Rusland) draagt via een `tension`, geen `wp-` — zoals Ticino bij goud. Schip+land, geen nieuwe modus.
- **2026-07-15 · M9 Kaspische oversteek + Dardanellen** (`_chokepoints.js`) — 3 vaarpunten (`wp-kaspisch-n/-m/-z`) forceren
  een watercorridor Aktau↔Bakoe (Kaspische Zee = ingesloten zee, valt deels als land in het raster); `wp-dardanellen` houdt
  naast `wp-bosporus` de Zwarte-Zee-uitgang open (anders geen weg Poti→Middellandse Zee). Alleen uranium gebruikt ze → geen
  impact op andere grondstoffen. Landlocked-routering (Kazachstan/Niger) = het kobalt/koper-corridorpatroon (land-flow →
  haven + aparte ship-flow). **CANDU-uitzondering** eerlijk gemodelleerd (natuurlijk uranium, geen verrijking). Details in `memory/decisions.md`.
- **2026-07-15 · M9 militaire-kringloop-toggle uitgesteld → ALSNOG GEBOUWD** (LAR-414 Backlog → **Done**, commit `6a6d062`) — de
  optionele `layer:"secondary"`-laag vereiste code in `flows/ui/main/config/markers`, destijds dirty door de parallelle M8-sessie →
  eerst alleen de data-laag. Op Lars' verzoek afgemaakt zodra de engine schoon was: het **5e** optionele-laag-patroon
  (`type:"military"`-nodes + `layer:"secondary"`-flows + `showMilitary`/`hasMilitary()`), exact het olie-`reserve`-patroon in 5 plekken.
  4 military-nodes (Rosatom down-blend/HEU, tails-herverrijking, US DOE, US strategische reserve) + 5 `secondary`-flows (o.a. de
  historische Megatons-to-Megawatts-stroom Rusland→VS via `u-fab-us` `coastal:true`) + tension `u-t-military`. Headless: uranium 60 legs /
  0 kapot / 0 straight; toggle uit→aan +4 nodes/+5 flows; chip alleen bij uranium. Sectie J: alleen mijn 6 bestanden gestaged (PGM/silver-sessie ontzien).
- **2026-07-15 · M8 magneet-REE-framing gebouwd** — `data/rare-earths.js` "uitgewerkt" (41/38/6): `id` blijft `rare-earths`,
  `symbol: NdPr`, `unit: kt magneet-REO/jaar`. Scheiding én magneetfabrieken beide `type:"refinery"` (het `erts`/`raffinaat`/
  `product`-stagekleur draagt het onderscheid concentraat→NdPr/Dy-oxide→NdFeB-magneet); magneet = stage `product` (geen 4e stage).
  Schip+land, géén nieuwe render-modus. Reden: één scherp verhaal (NdPr+Dy/Tb), winning blijft eerlijk gemengd erts → scheiding = de knijp.
- **2026-07-15 · M8 grenscorridor `grens-ruili`** (`_chokepoints.js`, `kind:"grensovergang"`, 24.02/97.85) — Myanmar→China, exact
  het Kasumbalesa-patroon (landpunt, houdt de landkaart open). Draagt de Dy/Tb-landstroom Kachin→Ganzhou; alleen REE gebruikt het.
- **2026-07-15 · M8 recycling-toggle** (`layer:"recycle"`, `showRecycle`, default uit) = het **derde** optionele-laag-patroon (na
  CB en exchange). Bewust `layer:"recycle"` op flows **én** recycler-nodes: de node-gate zit op `node.layer==="recycle"` (niet op
  `type==="recycler"`) en `hasRecycle()` op `f.layer==="recycle"`, zodat **koper's always-on recyclers** (zónder `layer`) ongemoeid
  blijven en alleen REE de toggle/chip krijgt. Vijf plekken: `config.js`/`main.js`/`flows.js`/`markers.js`/`ui.js`.
- **2026-07-15 · M8 co-located nodes ~30–45 km uit elkaar** — twee nodes van dezelfde grondstof in één 0,25°-cel geven een 1-punts
  route (`degDist:0`, onzichtbare arc). Ref/magneet/recycler in dezelfde stad (Baotou/Ganzhou/MP/La Rochelle/Fort Worth) verschoven
  zodat de lokale scheiding→magneet-arcs zichtbaar renderen én de headless-teller schoon op 0 kapot blijft.
- **2026-07-15 · M10 nikkel = de omgekeerde trechter, koper als template** — nikkel is een schip/land-grondstof (géén luchtvracht →
  koper, niet goud, is het model). De "aha" is dat Indonesië via de **exportban op ruw erts** de mijn ÉN de raffinage aan land trok:
  het erts blíjft in het land (korte mijn→smelter-hops, `stage:"erts"`, `mode:"road"`) en gaat pas als NPI/matte/MHP de zee op —
  andersom dan koper/lithium waar het erts/concentraat naar China vaart. Class-1 (batterij/sulfaat) vs class-2 (roestvrij/NPI) gedragen
  via `stage` + `note` + een `tension` (geen 4e stage). Het Filipijnse ruw-erts (`stage:"erts"` naar China, géén ban) = het contrast.
- **2026-07-15 · M10 géén nieuw chokepoint (tweede na koper)** — nikkel draait volledig op de bestaande routekaart (Makassar/Lombok/
  SCS/Taiwan; Deense Straten voor Fins/Baltisch class-1; Panama + Pacific-vaarpunten voor Cuba/NC; de Saint-Laurent-keten voor
  Voisey's Bay→Sudbury). Bewust zo — óók om de gedeelde `_chokepoints.js` niet te raken terwijl de parallelle olie-sessie die dirty had.
- **2026-07-15 · M10 beursvoorraden-laag (LME) = 0 engine-wijziging** — de optionele exchange-toggle van koper (`type:"exchange"`/
  `layer:"exchange"`, `showExchangeStocks`) is generiek: `hasExchangeStocks()` vuurt op elke actieve grondstof met een exchange-node,
  en de flow-gate/marker/chip zijn niet koper-specifiek. Nikkel voegt dus 4 LME-nodes + 5 `layer:"exchange"`-flows toe **zonder één
  `src/*`/`config.js`-regel te wijzigen** — de eerste keer dat een optionele laag puur via de data-laag wordt hergebruikt. Nuance eerlijk
  gemodelleerd: **alleen class-1 is LME-leverbaar** (NPI/MHP/sulfaat niet) → LME-prijs ≠ fysieke markt (de 2022-squeeze als `tension`).
  Recycling **always-on** (koper-patroon, `type:"recycler"` zónder `layer`).
- **2026-07-15 · M11 olie = het knelpunten-netwerk, géén nieuw chokepoint** — olie's vorm is bewust anders dan alle eerdere: geen
  enkele trechter maar het **hele bestaande net van zeestraten dat tegelijk oplicht** (Hormuz #1 met 15 stromen, dan Malakka/Suez/Bab/
  Bosporus/Panama/Kaap). Bewust géén nieuw knelpunt toegevoegd — dat olie het hele net laat oplichten ís de boodschap. Wél 3 kleine
  **navigatie-vaarpunten** (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`) in een gelabeld OIL-blok in `_chokepoints.js`, om de VS/
  Venezuela-routes op het water te houden; olie-only → regressievrij. Keten op de 3 stages met **petrochemie als 3e daad**
  (`erts`=crude → `raffinaat`=producten → `product`=nafta→kraker→kunststof). Schip + `mode:"pipeline"`, géén nieuwe render-modus;
  crude-stromen starten bij de mijn met de export-terminal als 1e via-punt (gathering-leg routeert auto als land). Kust-raffinaderijen `coastal:true`.
- **2026-07-15 · M11 SPR-voorraden-toggle uitgesteld → alsnog gebouwd** (LAR-432 Backlog → **Done**, commit `86c8c1f`) — de
  optionele `layer:"reserve"`-laag (strategische petroleumreserves, olie's CB/beurs/recycling-equivalent) raakt de 5 gedeelde
  engine-bestanden; tijdens de parallelle M10-nikkel-sessie eerst alleen de data-laag gebouwd (zoals uranium's LAR-414, sectie J).
  Zodra de tree schoon was (Lars: "de voorraden bij olie is een goed idee") de toggle alsnog toegevoegd = het **vierde** optionele-laag-
  patroon, exact het koper-`exchange`-patroon (dedicated `type:"reserve"`, `hasReserves()` op `n.type`) + olie-amber tank-marker.
  5 SPR-nodes + 5 vul-flows + tension `oil-t-spr`. Headless: toggle uit=45/46, aan=50/51 (+5/+5), 0 kapot/0 straight, chip alleen bij olie, regressievrij.

- **2026-07-15 · M13 zilver = de eerste écht nieuwe grondstof (11e), niet een basis-upgrade** — nieuw `data/silver.js` +
  `<script>`-tag in `index.html` + 5 zilver-checks in `build-standalone.py` (LAR-436, apart issue want het is het concrete
  "anders" t.o.v. het patroon). De vorm: **géén geografisch knelpunt** — de knijp is tweezijdig/structureel (bijproduct-aanbod
  ~70-75% inelastisch + vraagconcentratie in de Chinese zonnepanelen-industrie → tekort dat de kluisvoorraden aftapt). Het
  grondstof-eigen "nieuwe element" is dus geen chokepoint maar het **by-product-winning-model** (mijn-nodes = zink/lood/koper/
  goud-mijnen met hoofdmetaal-`note`). Schip+land (koper/nikkel-model, géén goud-lucht), géén nieuwe render-modus, **géén nieuw
  chokepoint** (derde na nikkel/olie). Keten erts(doré)→raffinaat(good-delivery baar)→product(solar/elektronica/sieraad).
- **2026-07-15 · M13 kluis-/beursvoorraden = exchange-toggle hergebruikt, 0 engine-wijziging** — zilver-kluizen (LBMA/COMEX/SGE)
  ZIJN beurs-/kluisvoorraden → de bestaande koper/nikkel-`exchange`-semantiek (`type:"exchange"`/`layer:"exchange"`,
  `showExchangeStocks`) past exact; géén dedicated `type` nodig (anders dan olie-reserve). 2e puur-datagedreven hergebruik na
  nikkel: 3 exchange-nodes + 3 `layer:"exchange"`-aftap-flows (tonen het tekort), chip "beursvoorraden" verschijnt automatisch.
  Recycling always-on (~15-18%, koper/nikkel-patroon). Details in `memory/decisions.md`.
- **2026-07-15 · M13 twee route-bugs empirisch gefixt** — kandidaat-coördinaten eerst door `Routing.sea` gehaald, dán verplaatst:
  VS-raffinage Tacoma→Astoria (Puget Sound valt dicht in het grove raster) + China-solar Suzhou-binnenland→Jiangsu-kust. Sectie J
  gevolgd: alléén eigen bestanden gecommit (`e091848`) — parallelle sessie's engine-files (uranium-toggle) ongemoeid.
- **2026-07-15 · M12 PGM = luchtvracht (hergebruik goud-air-mode), géén nieuw element** — geraffineerd Pt/Pd/Rh is per kilo even
  waardevol als goud → luchtvracht (`mode:"air"`, JNB-gateway; "✈ vluchten" via `activeHasAir()`); concentraat/matte over land.
  Het grondstof-eigen "nieuwe element" is bewust géén nieuw element: derde grondstof na koper/nikkel die niets aan
  `_chokepoints.js` toevoegt en 0 engine-wijziging vergt. De vorm = de scherpste twee-landen/twee-metalen-concentratie
  (ZA/Bushveld = Pt/Rh, Rusland/Norilsk = Pd); de knijp is structureel (6 tensions), niet geografisch (geen `wp-`).
- **2026-07-15 · M12 recycling-toggle = REE-patroon hergebruikt, 0 engine-wijziging** — autokat-recycling (~25% van het aanbod,
  via dezelfde westerse huizen JM/BASF/Umicore/Heraeus/Tanaka) als optionele toggle: `type:"recycler"` + `layer:"recycle"` op
  nodes én flows, chip via `hasRecycle()`. Bewust recycling (niet de exchange-laag) als PGM's ene toggle = het dominantere PGM-
  verhaal. SAMECELL-fix: Japan-recycler zat in Tokyo Bay → snapte naar Tanaka's cel → verplaatst naar Kanagawa (`degDist:0`).
  Afwijkingen als aparte issues (Lars' verzoek): LAR-447 (recycle-chip-tooltip nog REE-bewoord, raakt gedeelde `ui.js`) + LAR-448
  (optionele Pt/Pd-exchange-laag, pure data). Sectie J: alléén `data/pgm.js`+`design/pgm.md` gecommit (`2c4b668`). Details in `memory/decisions.md`.

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
4. [x] Modulaire code **verplaatst** naar deze map + `git init` = werkbasis. ✅ **GitHub-remote live (2026-07-15):** `larswalters/grondstoffen-atlas` (public) + **GitHub Pages** → https://larswalters.github.io/grondstoffen-atlas/ (elke `git push origin main` deployt).
5. [x] **M5-fixes geport** uit de single-file naar de modulaire code + geverifieerd (214 legs, 0 kapotte routes). Visuele check op Netlify/mobiel rest nog (WebGL-screenshot lukte niet).
6. [x] **M6 · Goud uitgevoerd** (2026-07-14): research LAR-397/398 → `data/goud.js` LAR-401 + luchtroute-modus LAR-399 + voyages-lucht LAR-400 + CB-toggle LAR-402. Headless geverifieerd (371 legs/0 kapot). LAR-403 rest = visuele bevestiging Netlify/mobiel.
7. [x] **M7 · Koper uitgevoerd** (2026-07-14): `data/copper.js` "uitgewerkt" (69 nodes/50 flows/5 tensions) — Andes-concentraat-trechter + Copperbelt-kathode over land (Kasumbalesa) + beursvoorraden-laag (LAR-408, `layer:"exchange"`). Headless geverifieerd: koper 145 legs / 0 kapot, regressie 388/0. Rest = visuele bevestiging Netlify/mobiel + code-commit (Lars' seintje) + Linear LAR-404..409 → Done (MCP-auth ontbrak).
8. [x] **M9 · Uranium uitgevoerd** (2026-07-15): `design/uranium.md` (`d016ab8`) → `data/uranium.js` "uitgewerkt" (38 nodes/36 flows/6 tensions) + Kaspische oversteek/Dardanellen in `_chokepoints.js` (`76c0333`). 4-staps keten met verrijking als flessenhals (~44% Rusland) + Trans-Kaspische route + VVER-lock-in + CANDU-uitzondering. Headless: 54 legs/0 kapot, regressievrij. **Linear M9 · Uranium + LAR-410..415** aangemaakt (410-413 Done; 414 Backlog = uitgestelde militaire-kringloop-toggle; 415 In Progress = visuele bevestiging). Rest = visuele bevestiging Netlify/mobiel.
9. [x] **M8 · Zeldzame aardmetalen uitgevoerd** (2026-07-15): `data/rare-earths.js` van "basis" (9/5) → "uitgewerkt" (41 nodes/38 flows/6 tensions), magneet-REE-framing (NdPr+Dy/Tb) + `grens-ruili` (Myanmar→China) in `_chokepoints.js` + recycling-toggle (`layer:"recycle"`, 5 plekken). Ganzhou-scheidingstrechter + Dy/Tb-landstroom + Mountain-Pass-rondreis + NdFeB-waaier. Headless: 90 legs/0 kapot/0 straight, regressievrij. **Linear M8 · LAR-416..420 Done; 421 In Progress** (visuele bevestiging Netlify/mobiel = Lars).
10. [x] **M10 · Nikkel uitgevoerd** (2026-07-15): `data/nickel.js` van "basis" (13/4) → "uitgewerkt" (50 nodes/46 flows/6 tensions) + `design/nikkel.md` + nikkel-checks in `build-standalone.py`. Indonesië-onshoring-trechter (exportban: mijn+raffinage in tien jaar, IMIP/IWIP) + twee nikkels (class-1 batterij vs class-2 roestvrij) + prijscrash-shakeout (Nickel West 2024) + LME-nuance (2022-squeeze). Schip+land, géén nieuw chokepoint; beursvoorraden-laag hergebruikt de bestaande exchange-toggle (**0 engine-wijziging**); recycling always-on. Headless: **nikkel 91 legs / 0 kapot / 0 straight**, regressie schoon. Commit `08aa4f5` (lokaal-only, Claude-trailer). **Linear M10 · LAR-422..426 Done, 427 In Progress**. Overige op basis: grafiet, PGM.
11. [x] **M11 · Olie uitgevoerd** (2026-07-15): `data/oil.js` van "basis" (18/15) → "uitgewerkt" (45 nodes/46 flows/6 tensions) + `design/olie.md` + 4 olie-checks in `build-standalone.py`. Het **knelpunten-netwerk dat tegelijk oplicht** (Hormuz #1 met 15 stromen, Malakka, Suez/Bab, Bosporus, Panama, Kaap) → **géén nieuw chokepoint** (eigen aha), wel 3 olie-only vaarpunten (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`) in `_chokepoints.js`. Drie verhalen: Hormuz-bypass-pijpleidingen (Yanbu/Fujairah) + Rusland-omleiding 2022→ (India/China) + VS-schalie-ommekeer. Keten 3 stages (erts/raffinaat/petrochemie), schip+pijpleiding, géén nieuwe render-modus. Headless: **olie 210 legs / 0 kapot / 0 straight**, regressievrij (baseline 5 = lithium 4 + goud 1). Commit `1d4ece5` (lokaal-only, Claude-trailer). **SPR-voorraden-toggle (`layer:"reserve"`) daarna alsnog gebouwd** (LAR-432 Done, commit `86c8c1f`) = het vierde optionele-laag-patroon; toggle uit=45/46, aan=50/51, chip "voorraden" alleen bij olie. **Linear M11 · LAR-428..432 Done, 433 In Progress**. Overige op basis: grafiet, PGM.

12. [x] **M13 · Zilver uitgevoerd** (2026-07-15): de **eerste écht nieuwe grondstof** sinds de basis-10 — nieuw `data/silver.js` (42 nodes/37 flows/6 tensions) + `design/zilver.md` + `<script src="data/silver.js">` in `index.html` + 5 zilver-checks in `build-standalone.py`. Géén winnings-trechter: ~70-75% **bijproduct** van zink/lood/koper/goud (aanbod inelastisch); de concentratie zit downstream — de **Chinese zonnepanelen-industrie** trekt zilver weg → **structureel tekort** dat de kluisvoorraden (LBMA/COMEX/SGE) aftapt. Schip+land, géén nieuwe render-modus, **géén nieuw chokepoint** (derde na nikkel/olie). Kluis-/beursvoorraden-laag = hergebruik van de bestaande exchange-toggle (**0 engine-wijziging**, nikkel-patroon); recycling always-on. 2 route-bugs empirisch gefixt (Tacoma→Astoria; solar Suzhou→Jiangsu-kust). Headless: **zilver 85 legs / 0 kapot / 0 straight**, regressievrij. Commit `e091848` (lokaal-only, Claude-trailer, alléén eigen bestanden — sectie J). **Linear M13 · LAR-434..438 Done, 439 In Progress**.

13. [x] **M12 · PGM uitgevoerd** (2026-07-15): `data/pgm.js` van "basis" (9/3) → "uitgewerkt" (38 nodes/41 flows/6 tensions) + `design/pgm.md` + 4 PGM-checks in `build-standalone.py`. De scherpste twee-landen/twee-metalen-concentratie: **Zuid-Afrika/Bushveld = Pt/Rh** + **Rusland/Norilsk = Pd**. PGM **vliegt** → hergebruik van de goud-air-mode (`mode:"air"`, JNB-gateway); concentraat/matte over land. **Géén nieuw chokepoint, géén engine-wijziging** (derde na koper/nikkel). **Recycling-toggle** (`layer:"recycle"`, ~25% autokat via JM/BASF/Umicore/Heraeus/Tanaka) = hergebruik van het REE-patroon met **0 engine-wijziging**. 6 tensions (concentratie, autokat + Pt↔Pd, rodium-spof, palladium/Rusland, waterstof-hedge, Eskom). Headless: **pgm 49 legs / 0 kapot / 0 straight / 0 degenerate arcs**, regressievrij (SAMECELL-fix Japan-recycler → Kanagawa). Commit `2c4b668` (lokaal-only, Claude-trailer, alléén eigen bestanden — sectie J). **Linear M12 · PGM + LAR-440..448** (5 Done, 445 In Progress; 446 Done na de build; 447/448 Backlog = afwijkingen: REE-bewoorde recycle-tooltip + optionele Pt/Pd-exchange-laag). **Alleen grafiet nog op "basis".**

## I - Runbook: "werk grondstof X uit" (self-serve)

Vaste flow om een grondstof uit te werken, identiek aan hoe goud/koper/uranium/REE/zilver/kolen zijn gedaan.
**De basis-10 is compleet** (grafiet/M14 was de laatste). De groei zit nu in **nieuwe grondstoffen** (niet basis→uitgewerkt maar
een nieuw `data/<x>.js` + `<script>`-tag + build-check, het zilver/kolen-patroon — leg dat "anders"-punt als eigen issue vast,
zoals LAR-436/457). Gedaan als nieuwe grondstof: zilver (M13), kolen (M17); diamant + gas lopen parallel. Doe de stappen op
volgorde; commit code en wrapup-docs apart. **Let bij parallel werk streng op sectie J** (alléén eigen bestanden stagen; bij een
gedeelde `index.html` met meerdere nieuwe script-regels in één hunk: stage alléén je eigen regel via `git apply --cached`).

**0. Oriënteer.** Lees `memory/current-strategy.md` (architectuur + sjabloon) + `memory/decisions.md` (de vaste patronen) +
   `design/_brief-template.md`. Kijk naar een recent uitgewerkt bestand als voorbeeld — `data/copper.js` (schip/land + optionele
   toggle) of `data/uranium.js` (tension-knijp + nieuw chokepoint) liggen het dichtst bij de meeste grondstoffen.

**1. Linear vastleggen vóór het codewerk.** Maak (via de Linear-MCP die zónder OAuth werkt — de `331d1eb1…`-server met
   `save_milestone`/`save_issue`, **niet** de auth-vereiste `plugin:engineering:linear`; zie [[linear-mcp-two-surfaces]]) een
   **milestone** `M<n> · <Grondstof>` in project "Grondstoffen Atlas" (team **Lars/LAR**) + de standaard **±6 issues**, gespiegeld op M6/M7/M9:
   - research upstream (winning/mijnbouw) · research downstream (raffinage/consumptie/recycling)
   - het grondstof-eigen **nieuwe element** (nieuw chokepoint/corridor, of een render-modus) — sla over als de grondstof volledig bestaande routes hergebruikt
   - `data/<x>.js` van "basis" → "uitgewerkt"
   - de optionele **toggle-laag** (CB/beurs/recycling-stijl) — alleen als de grondstof er een heeft
   - verificatie (headless) + single-file build + visuele bevestiging Netlify/mobiel
   Research mag inline in de brief (stap 2) — die research-issues gaan Done zodra de brief staat.

**2. Ontwerp eerst (brief).** Kopieer `design/_brief-template.md` → `design/<x>.md` en vul alle knopen/stromen in
   (operators, capaciteiten, `lat`/`lon`, transportmodi, de "aha"/knijp van deze grondstof). Eerst ontwerpen, dan bouwen.

**3. Bouw `data/<x>.js`** volgens het lithium-schema (zie `data/_registry.js` voor het veld-schema):
   - Metadata: `id`/`name`/`symbol`/`color`/`unit`/`blurb`, `detail:"uitgewerkt"`.
   - Nodes (`mine`/`refinery`/`port`/`market` + evt. `recycler`/`exchange`/`cb`), flows met `stage` (`erts`→`raffinaat`→`product`)
     + `mode` (`ship`/`rail`/`road`) + `via:[...]` langs havens en `wp-*`/`grens-*`, en `tensions` voor de knijppunten.
   - **Registratie is er al** voor de bestaande 10 grondstoffen (script-tag in `index.html`). Een *nieuwe 11e* grondstof: voeg een
     `<script src="data/<x>.js">` toe in `index.html` (de build leest die volgorde).
   - **Harde regel:** elke ship-leg moet op een kustpunt landen (`port` / `coastal:true` / `wp-*`), anders valt hij op de landkaart terug
     of vindt geen pad. Landlocked → kobalt/koper-corridorpatroon (land-flow mijn→haven `via:["grens-…"]` + aparte ship-flow haven→markt).
   - Nieuw chokepoint/corridor nodig? Voeg het toe aan `data/_chokepoints.js` (`kind:"grensovergang"` voor een landgrens; `wp-…` + evt.
     `openRadius` voor een zeestraat/ingesloten zee). Twee nodes in dezelfde 0,25°-cel geven een onzichtbare `degDist:0`-arc → ~30–45 km uit elkaar.

**4. Engine-wijziging (alleen als nodig).** Een nieuwe **optionele toggle-laag** = het vaste patroon op vijf plekken
   (`config.js` marker-size · `main.js` filters-default + `has…()` + voyages-gate · `flows.js` flow-gate · `markers.js` node-gate · `ui.js` chip).
   Een nieuwe **render-modus** (zoals goud-lucht) raakt `flows.js`. Zie sectie J vóór je gedeelde `src/*`-bestanden aanraakt bij parallel werk.

**5. Verifieer headless in de draaiende atlas.** Start de dev-server (launch.json-entry, zie sectie J voor de poort), open 'm in de
   Browser-pane, en draai via `javascript_tool` een legs-check die per flow de stops (`from`+`via`+`to`) langs `Routing.sea`/`Routing.land`
   routeert en telt: **doel = <grondstof> X legs / 0 kapot / 0 straight**, plus **regressie** over alle grondstoffen (globaal blijft 5 kapot =
   de bekende `degDist:0` lithium(4)+goud(1)-baseline; nieuwe grondstof voegt 0 toe). Check ook: geen console-warnings (onbekende via-/node-ids),
   toggle aan/uit voegt de juiste flows/nodes toe. Visueel het emergente plaatje bekijken (screenshot); **volledige visuele bevestiging op
   Netlify/mobiel = Lars** (WebGL-screenshot lukt niet betrouwbaar headless).

**6. Build + wrapup.** `python build-standalone.py` (voeg een REE-stijl sanity-check toe voor je grondstof) → `atlas-standalone.html`.
   Dan de **`wrapup`-skill**: die voert de Definition of Done uit (vault-sessiesamenvatting + integratie in projectpagina/`now.md`/`index.md`/
   `log.md`/`timeline.md`, project-`memory/`-sync, `CLAUDE.md`/checklist, Linear op Done, Pinecone-gist, code + docs committen). Commit code en
   wrapup-docs als **twee aparte commits** met de Claude-trailer; repo is **lokaal-only** (geen remote → geen push).

## J - Parallel werken (meerdere sessies tegelijk)

Twee sessies kunnen **verschillende grondstoffen tegelijk** uitwerken (is al gebeurd: M7+M8, en M9 naast M8). Elke grondstof heeft z'n
eigen `data/<x>.js` + `design/<x>.md` — die botsen nooit. Frictie zit alleen op het **gedeelde oppervlak**. Regels:

1. **Stage alleen je eigen bestanden — nooit `git add -A`/`git add .`.** De working tree bevat de half-af bestanden van de andere sessie.
   Voorbeeld: `git add data/<x>.js design/<x>.md` (+ je eigen `_chokepoints.js`-toevoeging als je die deed). Veeg je alles op, dan commit
   je hun onvoltooide werk. Twijfel je of een gewijzigd bestand van jou is? Laat het ongestaged en noem het.
2. **Gedeelde engine-bestanden = `src/*.js`, `config.js`, `data/_chokepoints.js`, `build-standalone.py`.** Raakt jouw grondstof die, en heeft
   de andere sessie ze dirty? **Bouw dan eerst alleen de data-laag en stel de engine-wijziging uit** (zoals uranium's militaire-toggle → LAR-414
   Backlog). Voeg de toggle/modus later toe als de tree schoon is.
3. **Nieuwe chokepoints append je in een eigen, gelabeld blok** in `data/_chokepoints.js` en commit dat vroeg/apart — losse toevoegingen aan het
   eind conflicteren zelden textueel. Alleen jouw grondstof mag ernaar verwijzen (geen impact op de andere 9).
4. **Eigen dev-server-poort per sessie** (launch.json): `grondstoffen-atlas` (8732) · `grondstoffen-atlas-2` (8733) · `-3` (8734) · `-4` (8735).
   Laat niet twee sessies dezelfde poort binden. (Één draaiende server delen kan ook — het is statische file-serving; elke browser-load leest vers.)
5. **Wrapups sequentieel, `git pull --rebase` eerst.** De vault is een gedeelde repo: `log.md`/`index.md`/`timeline.md` mergen automatisch
   (`merge=union`), maar `now.md` en de projectpagina niet — laat één sessie helemaal afwrappen (incl. vault-push) vóór de ander z'n vault-write doet.
   Linear (aparte milestones/issues) en Pinecone zijn onafhankelijk en botsen niet.
6. **Maximale isolatie (optioneel):** geef elke sessie een eigen **git-worktree** (aparte werkmap, eigen branch) → de working trees zijn fysiek
   gescheiden en conflicten komen pas netjes bij het mergen boven i.p.v. als rommelige gedeelde tree. Werkt ook op deze lokaal-only repo; kost een merge-stap.
