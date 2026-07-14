# Decisions — Grondstoffen Atlas
*Last updated: 2026-07-15 (M9 · Uranium uitgevoerd; M8 · Zeldzame aardmetalen voorbereid)*

Vastgelegde keuzes (nieuwste boven). Elk: besluit + korte reden.

## Architectuur
- **Geen bundler.** Losse globals-bestanden met vaste laadvolgorde via `<script>`-tags in `index.html`.
  Reden: eenvoud, direct te openen/deployen, geen buildstap; standalone single-file voor mobiel mogelijk.
- **Eén bestand per grondstof** in `data/` (`_registry.js` + `_chokepoints.js` + `<grondstof>.js`).
  Reden: elke keten geïsoleerd uit te werken en te reviewen.
- **Lithium = sjabloon.** `data/lithium.js` (34 knopen, 31 stromen) is de referentie voor alle volgende
  grondstoffen. Reden: één consistent schema (knopen/stromen/operators/capaciteiten/transportmodi/NL-annotaties).

## Routering & rendering
- **Echte routes via A\*** over een 1440×720 land/zee-raster (0,25°/cel uit `LAND_POLYS`) i.p.v. bogen
  door de lucht. Reden: het hele punt van de atlas is dat routes fysiek kloppen (schepen over water).
- **Knelpunten als water forceren** (`openRadiusDeg: 1.2`). Reden: in een 0,25°-raster slibben smalle
  straten (Lombok, Makassar) dicht; forceren houdt ze begaanbaar — en ze zijn juist het verhaal.
- **Gewogen A\*** (`heuristicWeight: 1.35`, `maxExpansions: 1500000`). Reden: lange oceaanroutes (10.000+ km)
  raakten de zoeklimiet en vielen terug op rechte lijnen dwars over eilandengroepen. Suboptimaal-maar-
  gevonden > rechte lijn door de Salomonseilanden.
- **`LAND_LINKS`** (Øresund, Storebælt, Fehmarn, Kanaaltunnel, Bosporus) als land forceren. Reden: anders
  kruipen spoorroutes helemaal om de Baltische staten/Finland heen.
- **Vaarbanen** (`laneShape(t)`): zijwaartse verschuiving nul bij elk anker, maximaal ertussenin. Reden:
  parallelle stromen los volgbaar onderweg, maar zichtbaar samengeknepen bij een knelpunt.
- **Schaal op afstand-tot-oppervlak** (`scaleFor()`, `d = camera.z - R`), niet op camerastand. Reden:
  de kernbug waarom inzoomen niets opleverde (factor-5-verschil tussen z-delta en oppervlakte-afstand).
- **Kaderloze labels + botsingsdetectie** (prioriteit `tier × 100 − share`). Reden: achtergrondkaders
  dekten de kaart af; overlappende labels moesten op prioriteit verdwijnen.
- **Autorotatie permanent uit na eerste interactie** (`autoRotateResumeMs: 0`). Reden: een bol die
  onder je handen wegdraait tijdens inzoomen is onbruikbaar.
- **Dover + St. Lawrence als knelpunt open geforceerd** (M5, 2026-07-14) — zelfde patroon als Lombok/Malakka;
  loste de kobaltroutes Cuba→Canada + Europa→Amerika op. Regressie: 0 kapotte routes over alle stromen.
- **Tegelnaad / blue-marble-doorprik opgelost** (M5, 2026-07-14) met een **shell-laag** (hele bol grove tegels)
  + een scherpe **detailpatch**; geverifieerd dat de blue-marble nergens meer doorprikt. Visueel niet met
  screenshot bevestigd (WebGL-capture liep vast) — numeriek/geometrisch getoetst.

## Inhoud
- **Deploy via Netlify** drag-and-drop van de `atlas`-map (+ standalone HTML voor mobiel).
- UI-teksten/annotaties **Nederlandstalig**.

## Goud — ontwerpbesluiten (2026-07-14) — ✅ UITGEVOERD in M6
- **Principe:** we vertellen geen verhaal, we modelleren de werkelijkheid nauwkeurig; het plaatje vertelt
  zichzelf. Voor goud is die werkelijkheid anders van vorm dan lithium → automatisch een ander plaatje.
- **Alle lagen meenemen:** mijn → raffinage → handels-/kluishub → consumptie → centrale banken → recycling.
- **Luchtroutes als aparte modus**, parallel aan de bestaande `routes` ↔ `hemelsbreed`-toggle:
  - `hemelsbreed` = directe great-circle-boog (opgetild, hoogte ∝ afstand).
  - `routes` = **echte luchtroutes via luchthaven-nodes** (ZRH, LHR, JFK, HKG, DXB, SIN, DEL/BOM, PVG,
    FRA, IST, JNB, PER, ...), met **weg/spoor-legs** voor de korte Europese hops (Ticino↔Zürich,
    Londen↔Frankfurt) — hergebruikt de bestaande land-A\*.
  - Zee-A\* speelt voor goud vrijwel geen rol.
- **Voyages-playback hergebruiken:** i.p.v. schepen bewegen **lichtpuntjes/vliegtuig-glyphs** over de
  luchtlijnen, met teller "hoeveel goud / hoeveel zendingen" (zelfde `voyages.js`-motor, ander glyph + pad).
- **Great-circle-boog is hier juist correct** (voor lithium was hij "fout"): goud vliegt echt die boog,
  dus de boog klopt met de werkelijkheid — consistent met het plaatje=werkelijkheid-principe.
- **Zwitserland (Ticino) = de visuele trechter** — goud-equivalent van de China-lithium-knijp
  (Valcambi/PAMP/Argor-Heraeus + Metalor). "Knelpunten" bij goud zijn institutioneel: Swiss refining,
  London/NY-kluizen, China's eenrichtings-import.
- **Centrale banken als optionele (toggle-bare) laag:** toont voorraden (node-grootte) én de huidige
  inkoop-/repatriëringsstromen. CB-"koop" is vaak titeloverdracht ín een kluis; sommigen repatriëren wél
  (Polen 2019, Duitsland 2013–17, India 2024) → mix van "node groeit" + repatriëringsvluchten.

## Goud — subkeuzes bevestigd (2026-07-14)
- **Luchthaven-granulariteit:** kleine/artisanale mijnen clusteren naar regionale gateway-luchthavens
  (bv. West-Afrika → Accra/Dubai); niet per mijn een eigen luchthaven. Truthful + node-aantal beheersbaar.
- **Volumes:** per stroom een grofweg ton/jaar-getal verzamelen (research volgende sessie) om bogen +
  voyages-puntjes te schalen en de teller te vullen.

## Goud — bouwbesluiten (M6, 2026-07-14) — ✅ GEBOUWD + geverifieerd
- **Air = 3e route-modus, geïmplementeerd als arc i.p.v. A\*.** `mode:"air"` krijgt in `flows.js` een
  `&& !airMode`-uitzondering op de land/zee-routering en wordt een **opgetilde great-circle-boog** (`flat:false` +
  `arcStyle`-lift, hoogte ∝ afstand) — óók in route-view. Reden: goud vliegt écht die boog; de A\*-router is voor
  lucht zinloos. Korte EU/binnenland-hops blijven `road`/`rail` (land-A\*). Zero-regressie: lithium/kobalt hebben
  geen air-flows, dus de tak wordt voor hen nooit geraakt.
- **Stages hergebruikt i.p.v. nieuwe codes:** `erts`=doré (mijn→raffinage + recyclingschroot),
  `raffinaat`=baren (raffinage→hubs, hub↔hub), `product`=eindbestemming (consumptie + CB-repatriëring).
  Reden: geen nieuwe stage-styling nodig; sluit aan op de bestaande kleur/hoogte-logica.
- **Centrale-bank-laag = optionele toggle, default UIT** (`type:"cb"`-nodes + `layer:"cb"`-flows). Reden: v1 toont
  de pure fysieke keten; de CB-laag (voorraden + inkoop/repatriëring) is bijzaak die je erbij kunt zetten.
  Chip verschijnt alleen als een actieve grondstof CB-data heeft (geen ruis bij lithium). CB-node-grootte ∝ √voorraad.
- **Insulaire landen niet naar Zwitserland geleid:** Rusland (Olimpiada→eigen CB), Oezbekistan/Muruntau,
  Kazachstan en China-intern blijven binnenlands (node zonder uitgaande boog, of naar de eigen CB in de CB-laag).
  Reden: dat ís de werkelijkheid — de Ticino-convergentie komt uit de rést van de wereld.
- **Single-file = gegenereerde build via script** (`build-standalone.py`) i.p.v. handmatig knippen/plakken. Reden:
  operationaliseert "modulair = bron van waarheid"; reproduceerbaar. Bureaublad-referentie blijft onaangeraakt.
- **Tijdlijn-woordkeus resource-bewust** (`UI.setVoyageNoun`): "✈ vluchten" bij goud, "⚓ schepen" bij zee-grondstoffen.

## Architectuur-besluit (2026-07-14): MODULAIR = bron van waarheid — ✅ UITGEVOERD
- Lars koos **modulair** als bron van waarheid; de single-file wordt een **gegenereerde deploy-build**
  (mobiel/Netlify), zoals `atlas-standalone.html` in M0. Reden: schoonste per-grondstof-workflow (`data/<x>.js`),
  beste voor git-diffs + agent-edits, eert de M0-splitsing.
- **✅ Uitgevoerd (2026-07-14):** modulaire code verplaatst naar `Projects\General\grondstoffen-atlas` +
  **`git init`** (2 commits `b9d69fa`, `177bc6b`). M5-fixes geport uit de single-file (Dover/Deense Straten/
  Kasumbalesa-grensovergang/Saint-Laurent in `_chokepoints.js` + grensovergang-logica in `searoute.js`/`flows.js`
  + labels in `ui.js`; tegelnaad-fix zat al in `tiles.js`/`config.js`). `cobalt.js` vervangen door de volledig
  uitgewerkte versie. Geverifieerd: 214 legs, 0 kapotte routes.

## Grensovergang als landpunt + Seto-brug (2026-07-14)
- **Grensovergangen (`kind: "grensovergang"`, bv. Kasumbalesa) stempelen de LANDkaart open**, niet de zeekaart.
  Reden: een grenspost is een landknelpunt (weg), geen zeestraat; `isSeaPoint` behandelt hem als landpunt zodat
  road/rail-legs erlangs routeren. Id begint bewust NIET met `wp-` (dat markeert zeepunten).
- **Per-waypoint `openRadius`** (Saint-Laurent-keten): smalle rivieren met kleine schijfjes openen i.p.v. de
  globale `openRadiusDeg`, anders forceer je water dwars door een landengte.
- **Seto-brug (Kojima–Sakaide) als `LAND_LINK`.** Reden: Shikoku is een apart eiland in het raster → de landrouter
  vond geen pad Niihama→Osaka (kobalt). Zelfde truc als Øresund/Kanaaltunnel.

## Koper — bouwbesluiten (M7, 2026-07-14) — ✅ GEBOUWD + geverifieerd
- **Schip/land, géén nieuwe render-modus.** Koper hergebruikt de bestaande zee-A\*/land-A\*-routes (M3) + scheeps-
  voyages (M4). De luchtroute-modus was goud-specifiek; koper heeft die niet nodig.
- **Twee productvormen via `stage`.** Sulfide-**concentraat** = `stage: erts` (dof/donker) → moet naar een smelter;
  de Andes→China-trechter. **SX-EW-kathode** (oxide-erts, direct bij de mijn geraffineerd) = `stage: raffinaat` al
  bij de bron → reist meteen als afgewerkt metaal. Reden: dat ís het fysieke onderscheid; het stuurt de stromen en
  het emergent plaatje (donkere concentraatbogen die knijpen bij China vs. volle kathode direct naar de markt).
- **Copperbelt-landcorridor via het kobalt-patroon.** DR Congo/Zambia is landlocked → een **land-flow** mijn→haven
  (`mode: road`/`rail`, `via: ["grens-kasumbalesa"]`) + een **aparte ship-flow** haven→markt. Reden: in een ship-flow
  worden twee opeenvolgende landpunten (mijn→grenspost) een rechte lijn; splitsen op de haven geeft schone land- én
  zee-routering. Exact zoals kobalt Kasumbalesa doet.
- **Recycling ALWAYS-ON, niet achter de toggle.** Koperschroot (~⅓ van het aanbod) = `type: recycler` + `stage: erts`
  feedstock terug naar de smelters, standaard zichtbaar — net als goud. Reden: te belangrijk om te verbergen, en het
  hoort bij de fysieke keten. **Bewuste afwijking** van de emergent-picture-tekst in `design/koper.md` (die schroot
  bij de beursvoorraden-toggle noemde); gedocumenteerd in de brief.
- **Beursvoorraden = optionele toggle-laag, default UIT** (`type:"exchange"`-nodes + `layer:"exchange"`-flows),
  exact hetzelfde patroon als de goud-CB-laag (`flows.js`/`markers.js`/`main.js`/`ui.js`-filter op
  `filters.showExchangeStocks`; chip alleen als een actieve grondstof exchange-data heeft). Marker = koperkleurige
  **CylinderGeometry-spoel**, grootte ∝ √`stock` (kt Cu). Reden: LME/SHFE/COMEX is buffer-/handelsvoorraad, geen
  verbruik — bijzaak die je erbij kunt zetten. Bevestigt "herbruikbaar patroon voor toekomstige optionele lagen".
- **Markt-/magazijnnodes die per schip beleverd worden krijgen `coastal: true`.** Ontdekt tijdens verificatie: een
  zee-leg die op een landinwaarts punt eindigt valt terug op de landkaart (of vindt geen pad). Fixes: Japan/Korea-markt
  → kustpunt Nagoya (`coastal: true`) + Onsan→markt naar `mode: ship` (Korea→Japan kan niet over land, geen landbrug);
  alle beursmagazijnen `coastal: true` (het zijn havenmagazijnen); Walvis→VS gereroute naar Rotterdam (geen VS-haven-
  node). **Les:** elke ship-leg moet op een kustpunt (`port`/`coastal`/`wp-`) landen.

## Zeldzame aardmetalen — voorbereidingsbesluiten (M8, 2026-07-15) — ⏳ ONTWERP-SKELET, nog niet gebouwd
- **Grondstofkeuze: zeldzame aardmetalen** als volgende uitwerking. Reden: meest iconische kritieke-grondstof + voegt
  de atlas iets nieuws toe (niet nóg een China-trechter in dezelfde vorm). Skelet `design/zeldzame-aardmetalen.md`.
- **Magneet-REE-framing (optie 2), na Lars' "is REE niet te generiek?".** Niet "alle 17 elementen" (→ vage blob incl.
  La/Ce-bulk) maar de **magneetmetalen NdPr (licht) + Dy/Tb (zwaar)**. Reden: leest als één stof zoals lithium/kobalt,
  terwijl de winning eerlijk het **gemengde erts** blijft (Nd niet los te winnen — dat ís de crux; scheiding = de knijp).
  REE is intrinsiek een groep (samen uit één erts, chemisch bijna identiek), niet generiek zoals "metalen"; precedent = PGM.
- **Metadata sharpenen** (bij de bouw): `id` blijft `rare-earths` (basis-file + registratie intact), `symbol → NdPr`,
  `unit → kt magneet-REO/jaar` (alleen NdPr + Dy/Tb-oxide-inhoud), scherpere `name`/`blurb`. Mijn-`share` telt de
  magneet-relevante fractie (Dy/Tb-rijke ionklei weegt zwaarder dan tonnage).
- **Magneet = stage `product`** (geen aparte 4e stage) → de eerdere "4e stage?"-open-vraag vervalt in deze framing.
  Consumptie beperkt tot magneet-eindgebruik (EV/wind/defensie); La/Ce-bulk (glas/katalysatoren) buiten scope.
- **Schip+land, géén nieuwe render-modus** (net als koper) — hergebruikt zee-A\*/land-A\* (M3) + scheeps-voyages (M4).
  Recycling (magneetschroot → scheiding) = optionele toggle `layer:"recycle"` (default uit), het CB/beursvoorraden-patroon.
- **Nieuw knelpunt bij de bouw:** grensovergang **Myanmar→China** (Kachin/Ruili) als `grens-*`-punt in `_chokepoints.js`,
  analoog aan `grens-kasumbalesa` (`kind:"grensovergang"`). Draagt de Dy/Tb-landstroom; enige nieuwe chokepoint.
- **Linear M8 niet aangemaakt** (MCP-auth ontbrak): geen valse LAR-nummers verzonnen, milestone/issues "aan te maken".

## Uranium — bouwbesluiten (M9, 2026-07-15) — ✅ GEBOUWD + geverifieerd
- **Grondstofkeuze: uranium** als volgende uitwerking (niet nikkel, de runner-up). Reden: de meest *distinctieve nieuwe
  vorm* — een 4-staps keten met de knijp twee stappen downstream in een vijandige staat + twee landlocked-routes, i.p.v.
  nóg een China-processing-trechter (lithium/koper/REE hebben die al). Zelfde "ander beest"-argument waarmee goud gekozen werd.
- **4-staps keten op de 3 bestaande stages gemapt** (zoals REE de "4e stage?"-vraag oploste): `erts` = winning + conversie
  (feed, dof) · `raffinaat` = **verrijking** (de flessenhals, volle uraankleur) · `product` = splijtstoffabricage → reactor
  (licht). Reactoren = `market`. Reden: geen nieuwe stage-styling; de verrijking wordt zo de visuele `raffinaat`-knijp —
  precies waar het verhaal zit. Node-types alle bestaand (mine/refinery/market/port) → **geen nieuwe marker-styling nodig**.
- **De verrijkings-flessenhals (~44% Rusland) draagt via een `tension`, niet een `wp-`.** Reden: het is een institutionele/
  technologische knijp zónder zeestraat — analoog aan de Zwitserse goudraffinage (Ticino). Winning is breed verspreid en
  juist *niet* de flessenhals.
- **Schip + land, géén nieuwe render-modus** (net als koper/REE) — hergebruikt zee-A\*/land-A\* (M3) + scheeps-voyages (M4).
  Landlocked-routering (Kazachstan/Niger) = het kobalt/koper-corridorpatroon: land-flow mijn→haven + aparte ship-flow haven→markt.
- **Nieuw route-element = de Kaspische oversteek** (het enige "nieuwe" stuk, à la de goud-luchtroute maar veel lichter — puur
  data): 3 vaarpunten (`wp-kaspisch-n/-m/-z`) forceren een watercorridor Aktau↔Bakoe (de Kaspische Zee is een INGESLOTEN zee
  die deels als land in het raster valt), plus **`wp-dardanellen`** naast de bestaande `wp-bosporus` (anders sluit de Zwarte
  Zee zich af en vindt Poti→Middellandse Zee geen uitgang). Toegevoegd aan `_chokepoints.js`; **alleen uranium gebruikt ze**
  → geen impact op andere grondstoffen. Zelfde geforceerd-water-truc als Lombok/Suez, met een vaarpunten-keten zoals Saint-Laurent.
- **CANDU-uitzondering eerlijk gemodelleerd:** Canadees natuurlijk uranium → CANDU-reactoren **zonder verrijking** → slaat de
  Russische knijp volledig over (eigen `tension`). Reden: dat ís de werkelijkheid; het verklaart waarom Canada erts, conversie
  én reactoren in één binnenlandse keten kan houden.
- **VVER-lock-in** als downstream-verhaal: TVEL (Elektrostal) → Paks/Dukovany/Kozloduy (Russische splijtstof voor Russische
  reactorontwerpen in de EU), met Westinghouse (Västerås) die inbreekt = de eerste barst.
- **Militaire-kringloop-toggle BEWUST UITGESTELD** (LAR-414 Backlog). De optionele `layer:"secondary"`-laag (down-blended
  wapen-HEU / strategische voorraden) vereist code in `flows/ui/main/config` — exact de bestanden die de parallelle M8-sessie
  op dat moment dirty had. Om botsing te vermijden alleen de **data-laag** gebouwd. Het `layer:"..."`-filterpatroon is al vast
  en herbruikbaar (CB → exchange → secondary).
- **Verificatie (headless, mijn eigen server poort 8743):** uranium **54 legs / 0 kapot** (20 zee + 34 land, **0 straight** →
  de Kaspische oversteek routeert écht over water). Regressie schoon: de 5 overige nulls zijn de bekende `degDist:0` same-city
  hops uit de M5/M6-baseline (lithium 4, goud 1), niet nieuw. Structuurcheck groen. WebGL-screenshot lukt niet headless → visueel = Lars.

## Nog te beslissen (open)
- `atlas-lithium-kobalt.html` / `globe-oud`-restanten opruimen — pas ná **visuele** bevestiging op Netlify/mobiel
  (routeverificatie is al headless gedaan; screenshot lukte niet door WebGL-time-out).
- Evt. **GitHub-remote** voor de nieuwe repo (nu lokaal-only).
