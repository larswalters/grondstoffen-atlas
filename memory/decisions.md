# Decisions — Grondstoffen Atlas
*Last updated: 2026-07-16 (M16 · Diamant uitgevoerd — de nieuwe 12e grondstof; M17 · Kolen)*

Vastgelegde keuzes (nieuwste boven). Elk: besluit + korte reden.

## M16 · Diamant — uitgevoerd (2026-07-16)
- **De vorm = de scherpste DOWNSTREAM-trechter, niet een winnings- of raffinage-knijp.** Winning is verspreid; de knijp zit
  bij de **bewerking**: ~90-95% van álle diamant wordt geslepen/gepolijst in **één stad (Surat, Gujarat)** — scherper nog dan
  de China-raffinage (lithium/koper) of Ganzhou-scheiding (REE). Alle rough-arcs convergeren op Surat = het emergente aha.
- **Antwerpen = een institutioneel knelpunt, gemodelleerd als een fysieke omweg.** Sinds de G7-sanctie op Russische/Alrosa
  diamant (maart 2024) is Antwerpen het verplichte **certificeringsknooppunt**: niet-Russische rough gaat mijn→Antwerpen→Surat,
  terwijl de **Russische rough zichtbaar om Antwerpen heen buigt** via Dubai/direct India. Reden: modelleer de sanctie-
  werkelijkheid als routing, niet als losse tekst — "de stroom buigt om, niet weg". Draagt ook via een `tension` (zoals Ticino/goud).
- **Diamant vliegt → hergebruik van de goud/PGM air-mode, 0 engine-wijziging.** Per kilo extreem waardevol → beveiligde
  luchtvracht (`mode:"air"`, great-circle). **Géén nieuw chokepoint** (zoals PGM), **géén nieuwe marker-types** (`hub`=
  Antwerpen/Dubai/Gaborone/Mumbai, `refinery`=slijperij Surat/China — de ruit-marker past treffend). Alleen korte hops binnen
  een land = `road`. Diamant is de 3e grondstof na koper/nikkel-familie die niets aan de engine/`_chokepoints.js` toevoegt.
- **Lab-grown-toggle = een écht "anders"-punt → aparte, uitgestelde issue (LAR-471).** Kweekdiamant (China/Henan HPHT + India/
  Surat CVD) past niet op een bestaande toggle (recycle/exchange/reserve/military hebben andere semantiek) → een nieuwe optionele
  laag (`layer:"labgrown"`, 5 engine-bestanden). Bewust NIET in v1 gebouwd (parallelle sessies op de gedeelde engine, sectie J),
  zoals uranium's militaire-toggle (LAR-414) en olie's SPR (LAR-432). In v1 leeft lab-grown als `tension` (`dia-t-labgrown`).
- **Route-artefact pragmatisch opgelost:** de ene 2-punts landhop (Dubai→Golf-retail, kust-artefact van het grove 0,25°-raster —
  Dubai valt net als water in `LAND_POLYS`) omgezet naar `air` i.p.v. `road` → 0 straight, consistent want diamant vliegt.
- **Sectie-J-race (4 parallelle sessies) + gas-tag-co-commit.** Mijn gestagede bestanden werden éénmaal meegeveegd in gas'
  brede `git add` en raakten bij de rebase (M15→M17-renummering) weer untracked (inhoud intact; **geen historie herschreven**).
  Bij het afmaken: 2 schone pathspec-commits; de meeliftende `data/gas.js`-tag in `index.html` bewust meegenomen omdat die al
  naar de **gecommitte** gas.js verwees → consistent, geen duplicaat, gas' resume ziet geen diff. **Les:** bij een gedeelde
  staging-index nooit `git add` zonder pathspec; committen met `git commit -- <paths>` isoleert betrouwbaar.

## M17 · Kolen — uitgevoerd (2026-07-16)
- **De vorm = de binnenlandsheid, GÉÉN trechter.** Waar lithium/koper/REE bij de raffinage knijpen, goud bij Zwitserland,
  uranium bij de Russische verrijking, olie het zeestraten-net laat oplichten en zilver een inelastische bijproduct-vraagknijp
  heeft — heeft kolen **géén enkele mondiale flessenhals** omdat het overweldigend **binnenlands** is: ~85% wordt verbrand waar
  gedolven (China ~50% van de wereld, India, VS, Rusland), slechts ~15% van de ~8.700 Mt gaat over zee. Reden: dat ís de
  werkelijkheid van kolen, en het is de scherpst mogelijke tegenpool van de andere grondstoffen — de kaart moet grote binnenlandse
  blokken tonen tegenover een dunne, geopolitiek beladen zeehandelslaag.
- **Stages als KETENPOSITIE (gedolven → verhandeld → verbrand), niet als bewerking.** `erts` = mijn→haven/centrale (dof) ·
  `raffinaat` = de **internationaal verhandelde bulk** (de zeekruisingen + de Mongolië-landcorridor; hier leeft élk ban/her-
  routeringsverhaal) · `product` = eindgebruik (stroom/staal). Gevolg: binnenlandse kolen (alleen erts+product, géén zeekruising)
  leest visueel ánders dan verhandelde kolen (mét de heldere `raffinaat`-zeeboog) → de ~85/15-splitsing wordt zichtbaar. Reden:
  kolen wordt niet geraffineerd zoals metaal; de stages dragen hier de reis, niet een chemische transformatie.
- **Twee kolen (thermisch vs. cokeskool) via `note` + `tension`, NIET via `stage`.** Thermisch→stroom en cokeskool→cokesovens→
  hoogoven-staal zijn parallelle producttypes, geen opeenvolgende stages. Gedragen zoals nikkel z'n class-1/class-2 deed (note +
  een aparte tension), zodat `stage` de ketenpositie blijft. Premium harde cokeskool ~Bowen Basin, India = #1 cokeskool-importeur.
- **China = swing-koper** (grootste producent én importeur) + **drie her-routeringen als institutionele knijp** (tensions, geen `wp-`):
  China-Australië-ban (okt 2020–begin 2023, keten die zichzelf omlegde), Rusland-oost-draai (2022→, EU-embargo → overbelast
  Trans-Siberisch spoor naar de Pacific), Mongolië-Gobi-corridor. Reden: kolens kwetsbaarheid is beleid/vraag, geen zeestraat.
- **Grondstof-eigen "nieuwe element" = één LANDknelpunt `grens-gashuunsukhait`** (Gashuun Sukhait / Ganqimaodu, Mongolië-China-
  Gobi-grens), `kind:"grensovergang"` in een eigen gelabeld COAL-blok in `_chokepoints.js`. Draagt de Mongoolse cokeskool
  (Tavan Tolgoi) over land naar het Chinese staal — exact het `grens-kasumbalesa`/`grens-ruili`-patroon. Alléén kolen verwijst
  ernaar → regressievrij. Kolen = 4e grondstof (na nikkel/olie/zilver) zonder nieuw ZEE-knelpunt.
- **GÉÉN optionele toggle-laag.** Kolen heeft geen zinvol CB/beurs/recycling-equivalent (geen bovengrondse kluisvoorraden;
  kolen wordt verbrand, niet gerecycled). Bewust weggelaten (het runbook staat dit toe: "alleen als de grondstof er een heeft").
  Bonus: houdt de engine schoon tijdens de parallelle diamant-/gas-sessies (sectie J). **Géén nieuwe render-modus/marker-types.**
- **Nieuwe 14e grondstof (registratie-plumbing), net als zilver.** Kolen zit niet in de basis-10 → nieuw `data/coal.js` +
  `<script>`-tag + build-check. Dat structurele verschil met het patroon bewust als **eigen Linear-issue** (LAR-457), zoals
  LAR-436 bij zilver. Reden: het is de enige echte afwijking en verdient een eigen spoor.
- **Route-bug: Canadese haven van Roberts Bank → Ridley/Prince Rupert.** De 2 kapotte legs zaten op `coal-port-vancouver →
  wp-pac-noord`. Empirisch gediagnosticeerd (kandidaten door `Routing.sea`): **Roberts Bank/Westshore ligt ingesloten in de
  Salish Sea** en valt dicht in het grove raster (robertsbank→open zee = null). Verplaatst naar **Ridley Terminal / Prince
  Rupert** (open kust) — dat is bovendien feitelijk dé Canadese cokeskool-exporthaven. Herbevestigt de zilver-Tacoma→Astoria-les:
  test kandidaat-coördinaten door de router vóór je ze vastzet.

## M14 · Grafiet — uitgevoerd (2026-07-15)
- **De vorm = een REE-achtige verwerkingstrechter, met TWEE feedstocks.** Grafiet is HET anodemateriaal in Li-ionbatterijen
  (grootste celcomponent naar massa, ~1 kg/kWh). Twee grondstofstromen komen op dezelfde knijp samen: **natuurlijk vlokgrafiet**
  (gedolven) én **synthetisch grafiet** (uit petroleum-**naaldcokes**, gegrafitiseerd bij ~3000 °C). De omzetting tot gecoat
  sferisch/gegrafitiseerd anodepoeder zit **~90%+ in China** (Shandong natuurlijk, Binnen-Mongolië synthetisch op goedkope
  kolenstroom). Reden voor deze framing: het is de werkelijkheid en de sterkste parallel met REE-Ganzhou — winning is verspreid,
  de *verwerking* is de knijp; zelfs ex-China vlok (Balama/Molo/Minas Gerais) vaart naar China om verwerkt te worden. De twee
  feedstocks zijn gemodelleerd als twee soorten `mine`-nodes (vlok met `share`; naaldcokes zonder share = raffinage-bijproduct).
- **De naaldcokes-bron als `mine`-node (zonder share).** Synthetisch grafiet start niet in een mijn maar bij naaldcokes
  (petroleum-cokes/koolteerpek). Gemodelleerd als 2 `type:"mine"`-nodes (VS Lake Charles premium + China Liaoning) zónder `share`,
  met een `note` dat het een raffinage-bijproduct is. Zo staat de synthetische route eerlijk náást de natuurlijke, beide
  convergerend op de Chinese verwerking. Reden: geen nieuw node-type nodig (0 marker-wijziging), verhaal blijft leesbaar.
- **Levende geopolitiek = de China-exportvergunningen op grafiet (dec 2023)** — gedragen via een `tension` (`gr-t-export-controls`),
  niet via een nieuw route-element. Reden: het is een beleidshefboom bovenop de bestaande verwerkingsdominantie, geen zeestraat.
- **Schip+land, GEEN nieuwe render-modus, GEEN nieuw chokepoint** — vierde grondstof (na nikkel/olie/zilver) die volledig op de
  bestaande routekaart draait (Malakka/Singapore/SCS/Taiwan voor Azië-aanvoer; Kaap + Golf van Mexico/Florida voor de trans-
  Atlantische Balama→Vidalia-lijn; Suez/Bab/Gibraltar + Rotterdam voor China→EU; Øresund/Narvik-spoor voor het Europese vlok).
  Reden: grafiet reist als gewoon industrieel bulkgoed; niets aan `_chokepoints.js` toegevoegd = regressievrij.
- **Recycling-toggle = hergebruik van het REE/PGM-`recycle`-patroon met 0 engine-wijziging.** `type:"recycler"` + `layer:"recycle"`
  op nodes én flows; node-gate op `node.layer==="recycle"`, `hasRecycle()` op `f.layer==="recycle"` (generiek, REE/PGM bevestigden
  dit). **Bewust bescheiden gemodelleerd** (3 recyclers, kleine volumes, default uit): batterijgrafiet-terugwinning is nog nascent
  (meeste verbruikte grafiet wordt nu verbrand/gestort; EU-batterijverordening trekt het pas op gang). De chip verschijnt automatisch.
- **`gr-ref-japan → gr-mkt-korea-japan` van `road` → `ship`** — Japan→Korea gaat over de Straat van Korea; een landroute is
  onmogelijk (was kapot in de check). Beide punten `coastal` → korte directe zee-hop. Herbevestigt de koper/PGM-les.
- **Basis→uitgewerkt, géén nieuwe registratie.** Anders dan zilver (M13, nieuw 11e bestand) bestond `data/graphite.js` al en stond
  het al in `index.html` → alleen het bestand verrijkt, geen script-tag/index-wijziging. Grafiet was het **laatste basis-10-bestand**.
- **Repo-status gecorrigeerd:** de eerdere "repo lokaal-only (geen push)"-besluitregels zijn **achterhaald** — de repo staat sinds
  M13 op GitHub en draait live op GitHub Pages (elke `git push origin main` deployt). Deze sessie is code + docs **wél gepusht**.

## M12 · PGM — uitgevoerd (2026-07-15)
- **PGM vliegt = hergebruik van de goud-air-mode (géén nieuw element).** Geraffineerd Pt/Pd/Rh is per kilo even waardevol als
  goud → beveiligde luchtvracht (`mode:"air"`: great-circle, buiten de A\* om), met **JNB (OR Tambo)** als uitgaande trechter.
  Concentraat/matte-hops binnen een land = `road`/`rail` (land-A\*). Reden: het is de werkelijkheid (edelmetaal-logistiek), en
  het is 0 engine-wijziging — de tijdlijn toont automatisch "✈ vluchten" via `activeHasAir()`. Het grondstof-eigen "nieuwe
  element" is dus bewust géén nieuw element: PGM is de derde grondstof na koper/nikkel die niets aan `_chokepoints.js` toevoegt.
- **De vorm = de scherpste twee-landen/twee-metalen-concentratie.** Zuid-Afrika/Bushveld = Pt/Rh (~70%/~80%), Rusland/Norilsk =
  Pd (~40%, Ni-Cu-bijproduct). De knijp is niet geografisch (een zeestraat) maar **structureel** → gedragen door `tensions`, niet
  door een `wp-`: twee-landen-concentratie, autokat-leiband + Pt↔Pd-substitutie, rodium-spof, palladium/Rusland-sanctie,
  waterstof-hedge (Pt/Ir PEM-elektrolyse), Eskom-stroomcrisis.
- **Recycling = optionele toggle (hergebruik REE-patroon, 0 engine-wijziging).** Autokat-recycling (~25% van het aanbod) via
  dezelfde westerse huizen die de katalysatoren máken (JM/BASF/Umicore/Heraeus/Tanaka): `type:"recycler"` + `layer:"recycle"` op
  nodes én flows, chip via `hasRecycle()`. Reden voor recycling i.p.v. de exchange-laag als PGM's ene optionele toggle: het is
  het dominantere PGM-verhaal (secundair aanbod ~25%). Eén SAMECELL-fix onderweg: de Japan-recycler zat in Tokyo Bay (water) →
  snapte naar Tanaka's cel → verplaatst naar Kanagawa (het `degDist:0`-patroon uit de REE-notities).
- **Afwijkingen bewust als aparte issues (Lars' verzoek).** LAR-447: de gedeelde recycling-chip-tooltip in `ui.js` is nog
  REE-bewoord ("<5% van het aanbod") — onjuist voor PGM (~25%); generiek/per-resource maken (raakt gedeelde `ui.js`, dus niet
  tijdens de parallelle sessie). LAR-448: een optionele **Pt/Pd-exchange-laag** (NYMEX/TOCOM-futures + Zürich/Londen-kluizen) is
  mogelijk als pure data (hergebruik exchange-toggle, 0 engine), maar bewust niet gebouwd — één optionele toggle per grondstof.
- **Sectie J bij parallel werk.** Gebouwd náást een M13-zilver- (+ uranium-toggle-)sessie met de gedeelde build-bestanden dirty
  → alleen `data/pgm.js` + `design/pgm.md` gecommit (`2c4b668`); de single-file build (LAR-446) + `now.md`/project-sync
  uitgesteld tot de tree schoon was, daarna afgemaakt.

## M13 · Zilver — uitgevoerd (2026-07-15)
- **Zilver = de eerste écht nieuwe grondstof (11e), niet een basis-upgrade.** Alle M6–M12 brachten een bestaand `data/<x>.js`
  van "basis" → "uitgewerkt"; zilver bestond nog niet in de atlas. Daarom een aparte registratie-stap: nieuw `data/silver.js` +
  `<script src="data/silver.js">` na `oil.js` in `index.html` + 5 zilver-checks in `build-standalone.py`. Reden om dit als eigen
  Linear-issue (LAR-436) vast te leggen: het is het concrete "anders" t.o.v. het patroon (Lars vroeg verschillen apart te vangen).
- **De vorm = twee-zijdige structurele knijp, GEEN geografisch knelpunt.** Anders dan lithium/koper/REE (China-raffinage), goud
  (Zwitserland), uranium (Russische verrijking) of olie (het zeestraten-net) heeft zilver géén enkele geografische flessenhals.
  De knijp is (1) **aanbod-inelasticiteit** — ~70-75% is bijproduct van zink/lood/koper/goud; en (2) **vraagconcentratie** — de
  Chinese zonnepanelen-industrie. Reden: dat ís de werkelijkheid van zilver; het plaatje vertelt zichzelf (diffuse origin +
  downstream-pull). Het grondstof-eigen "nieuwe element" is dus geen chokepoint maar het **by-product-winning-model** (mijn-nodes =
  eigenlijk zink/lood/koper/goud-mijnen, elk met een `note` over het hoofdmetaal).
- **Schip + land, GEEN nieuwe render-modus, GEEN nieuw chokepoint** (derde na nikkel/olie op de bestaande routekaart). Zilver is
  een industrieel metaal (~1/80 van goud's waarde per gram) → het vaart, het vliegt niet (koper/nikkel-model, NIET goud/lucht).
  Keten op de 3 bestaande stages: `erts` = mijn(bijproduct)→doré/concentraat, `raffinaat` = good-delivery baar (1000 oz),
  `product` = industrieel (solar/elektronica/sieraad). Inland-origins bij een ship-flow met een haven als 1e via-punt
  (gathering-leg routeert auto als land).
- **Kluis-/beursvoorraden = hergebruik van de bestaande exchange-toggle, 0 engine-wijziging** (`type:"exchange"`/`layer:"exchange"`,
  `showExchangeStocks`). Nikkel bewees al dat dit generiek is; zilver is het **tweede** puur-datagedreven hergebruik. 3 exchange-nodes
  (LBMA ~22.000 t / COMEX ~9.000 t registered / SGE ~3.000 t) + 3 `layer:"exchange"`-aftap-flows die het structurele tekort tonen
  (kluis → industrie). Reden geen dedicated `type` (zoals olie-reserve): zilver-kluizen ZIJN beurs-/kluisvoorraden — de koper/nikkel-
  `exchange`-semantiek past exact, dus geen nieuw patroon nodig. Recycling always-on (~15-18%, koper/nikkel-patroon, `type:"recycler"` zonder `layer`).
- **Twee route-bugs empirisch gefixt (niet gegokt).** Kandidaat-coördinaten eerst door `Routing.sea` gehaald, dán verplaatst:
  (1) VS-raffinage Tacoma→Astoria (Puget Sound valt dicht in het grove raster); (2) China-solar Suzhou-binnenland→Jiangsu-kust
  (landinwaarts per zee onbereikbaar). Herbevestigt de vaste regel: elke ship-endpoint moet op een echt zee-cel liggen.
- **Alléén eigen bestanden gecommit (sectie J).** Een parallelle sessie had de gedeelde engine-files dirty (uranium-toggle-werk:
  `config.js`/`src/{flows,main,markers,ui}.js`/`data/uranium.js`). Zilver raakt de engine niet (0 engine-wijziging) → commit `e091848`
  bevat alleen `data/silver.js` + `design/zilver.md` + `index.html` + `build-standalone.py`. Nooit `git add -A`.
- **Verificatie (headless, poort 8734):** zilver **85 legs / 0 kapot / 0 straight / 0 warnings**; regressie schoon. Exchange-chip +
  blurb + 6 tensions renderen. `atlas-standalone.html` geregenereerd (5 zilver-checks OK; gitignored). Visueel = Lars (LAR-439).
- **M12 bleek al PGM.** Bij het aanmaken van de milestone was M12 bezet door "M12 · PGM" (parallelle sessie) → zilver werd **M13**.

## M11 · Olie — uitgevoerd (2026-07-15)
- **Olie's vorm = het knelpunten-netwerk, niet één trechter.** Alle eerdere grondstoffen hadden één knijp (raffinage-China /
  Zwitserland / Russische verrijking). Olie's knijp is een **heel netwerk van zeestraten** — en precies het net dat de atlas al
  had. Reden: dat ís de werkelijkheid; het plaatje vertelt zichzelf zodra alle tankerstromen door hun echte straten lopen.
- **GÉÉN nieuw chokepoint = het eigen aha.** Olie hergebruikt het volledige bestaande knelpunten-net (Hormuz/Malakka/Suez/Bab/
  Bosporus/Panama/Kaap/Gibraltar/Deense-Straten/Dardanellen). Bewust géén nieuw knelpunt toegevoegd — dat olie het hele net
  tegelijk laat oplichten (Hormuz #1 met 15 stromen) ís de boodschap. Wél 3 kleine **navigatie-vaarpunten** (`wp-golf-mexico`/
  `wp-florida`/`wp-caribisch`) in een gelabeld OIL-blok in `_chokepoints.js`, om de VS/Venezuela-routes op het water te houden;
  alleen olie gebruikt ze → geen impact op de andere grondstoffen (regressievrij geverifieerd).
- **Keten op de 3 bestaande stages, mét petrochemie als 3e daad.** `erts` = ruwe olie (crude, draagt het knelpunten-verhaal) →
  `raffinaat` = geraffineerde producten (diesel/benzine, product-trade) → `product` = petrochemie (nafta→kraker→kunststof). Olie
  is in de kern 2-staps (crude→product); de 3e stage benut voor petrochemie zodat "olie wordt ook plastic" zichtbaar wordt.
- **Schip + pijpleiding, géén nieuwe render-modus.** Tankers = zee-A\*; pijpleidingen (`mode:"pipeline"`) = land-A\* (dashed).
  Elke crude-stroom start bij de mijn met de export-terminal als eerste via-punt → de gathering-leg mijn→terminal routeert
  automatisch als land, de rest als zee. Kust-raffinaderijen `coastal:true` zodat de tanker tot de kade vaart.
- **Drie levende her-routeringen als kern-tensions.** (1) De **Hormuz-bypass-pijpleidingen** (Saoedi Oost-West→Yanbu aan de Rode
  Zee; UAE Habshan→Fujairah aan de Golf van Oman) = het fysieke antwoord op de Golf-flessenhals. (2) De **Rusland-omleiding
  2022→**: Europese crude omgeleid naar India/China (Primorsk om Europa heen, ESPO→Kozmino, Novorossiysk door de Bosporus,
  Druzhba over land) — een beleidsgedreven her-routering zoals uranium's Trans-Kaspische, maar andersom. (3) De **Amerikaanse
  schalie-ommekeer**: de VS van importeur naar exporteur (Corpus Christi → Atlantische Oceaan), een omgekeerde pijl.
- **SPR-voorraden-toggle BEWUST UITGESTELD** (LAR-432 Backlog). De optionele `layer:"reserve"`-laag (strategische
  petroleumreserves, olie's equivalent van goud-CB/koper-beursvoorraden/REE-recycling) raakt de 5 gedeelde engine-bestanden
  (config/main/flows/markers/ui) terwijl de **parallelle M10-nikkel-sessie** live was — exact het scenario waarin uranium z'n
  toggle uitstelde (LAR-414). Alleen de **data-laag** gebouwd om botsing te vermijden; het `layer:"..."`-patroon is al vast.
- **SPR-voorraden-toggle ALSNOG GEBOUWD** (LAR-432 Done, commit `86c8c1f`) — zodra de nikkel-sessie klaar was en de tree
  schoon (Lars gaf groen licht: "de voorraden bij olie is een goed idee"). Het **vierde** optionele-laag-patroon; bewust een
  **dedicated `type:"reserve"`** (i.p.v. het REE-`layer`-op-nodes-trucje) omdat geen andere grondstof reserve-nodes heeft →
  `hasReserves()` mag simpel op `n.type==="reserve"` detecteren, net als `hasExchangeStocks()`. 5 SPR-nodes (`stock` in mln
  vaten) + 5 vul-flows + tension `oil-t-spr`; olie-amber tank-marker (grootte ∝ √`stock`). Reden voor de dedicated tank-marker
  i.p.v. hergebruik van de koper-spoel: olie-eigen visuele taal (voorraad-tank), en de koper-spoel leest als "beurs". Headless:
  toggle uit=45/46, aan=50/51 (+5/+5), 0 kapot/0 straight, chip "voorraden" alleen bij olie, regressievrij.
- **Verificatie (headless, mijn eigen server poort 8734 — de nikkel-sessie bezette 8732/8733):** olie **210 legs / 0 kapot /
  0 straight**. Regressie schoon: de globale 5 nulls zijn de bekende `degDist:0` same-city hops (lithium 4 + goud 1), olie voegt
  0 toe. `atlas-standalone.html` geregenereerd (4 olie-checks OK) + zelf geverifieerd. WebGL-screenshot lukt niet headless → visueel = Lars.

## M10 · Nikkel — uitgevoerd (2026-07-15)
- **De omgekeerde trechter; koper als template (niet goud).** Nikkel is een schip/land-grondstof → hergebruikt de zee-A\*/
  land-A\*-routes + scheeps-voyages, géén luchtvracht-modus. De "aha": andersom dan koper/lithium (breed graven, in China
  raffineren) trok **Indonesië via de exportban op ruw erts de mijn ÉN de raffinage aan land**. Modelmatig: het erts blíjft
  in het land (korte hops mijn→smelter, `stage:"erts"`, `mode:"road"`) en gaat pas als NPI/matte/MHP de zee op. Het Filipijnse
  ruw-erts naar China (`stage:"erts"`, géén ban) = het bewuste contrast ernaast.
- **Class-1 vs class-2 via `stage` + `note` + een `tension`, geen 4e stage.** Class-2 (NPI/ferronikkel → roestvrij) en class-1
  (nikkelsulfaat/kathode → batterij) worden gedragen door de bestaande drie stages + de tension "Twee nikkels"; HPAL→MHP en matte
  zijn de bruggen. Reden: consistent met REE/uranium (geen stage-styling voor een 4e stap). IMIP maakt roestvrij ter plekke →
  die flow is `stage:"product"`.
- **Géén nieuw chokepoint (tweede grondstof na koper).** Nikkel draait volledig op de bestaande routekaart (Makassar/Lombok/
  SCS/Taiwan; Deense Straten voor Fins/Baltisch class-1; Panama + Pacific-vaarpunten voor Cuba/NC; de Saint-Laurent-keten voor
  Voisey's Bay→Sudbury). Bewust zo — óók om de gedeelde `_chokepoints.js` niet te raken terwijl de parallelle olie-sessie die dirty had.
- **Beursvoorraden-laag (LME) = 0 engine-wijziging.** De exchange-toggle van koper (`type:"exchange"`/`layer:"exchange"`,
  `showExchangeStocks`) is generiek: `hasExchangeStocks()` vuurt op elke actieve grondstof met een exchange-node; flow-gate/marker/
  chip zijn niet koper-specifiek. Nikkel voegt 4 LME-nodes + 5 `layer:"exchange"`-flows toe **zonder één `src/*`/`config.js`-regel
  te wijzigen** — de eerste optionele laag die puur via de data-laag wordt hergebruikt. Nuance eerlijk gemodelleerd: **alleen class-1
  is LME-leverbaar** (NPI/MHP/sulfaat niet) → LME-prijs ≠ fysieke markt; de 2022-squeeze (Tsingshan) als `tension`. Recycling
  **always-on** (koper-patroon, `type:"recycler"` zónder `layer`).
- **Coastal-markten (koper-fix hergebruikt).** De Aziatische/EU-afzetmarkten die per schip beleverd worden (Foshan/Ningbo/Korea/
  Japan/EU-roestvrij) staan `coastal:true` zodat elke ship-leg op een kustpunt landt i.p.v. op de landkaart terug te vallen.
- **Parallelle-sessie-hygiëne (sectie J).** Een andere sessie werkte tegelijk aan olie (`data/oil.js`/`design/olie.md`/
  `_chokepoints.js` dirty). Alleen mijn eigen 3 bestanden gestaged (`data/nickel.js` + `design/nikkel.md` + `build-standalone.py`),
  nooit `git add -A`; commit `08aa4f5` (lokaal-only, Claude-trailer).

## M8 · Zeldzame aardmetalen (magneet-REE) — uitgevoerd (2026-07-15)
- **Magneet-REE-framing (optie 2), 1-op-1 uit het skelet gebouwd.** `id` blijft `rare-earths` (registratie intact),
  `name` = "Zeldzame aardmetalen (magneet-REE)", `symbol` = `NdPr`, `unit` = "kt magneet-REO/jaar". Reden: REE als één
  verhaal (NdPr licht + Dy/Tb zwaar) i.p.v. de vage 17-elementen-blob; winning blijft eerlijk gemengd erts → scheiding = de knijp.
- **Scheiding én magneetfabrieken beide `type:"refinery"`** (diamant-marker); consumptie = `type:"market"`. Reden: het
  `erts`→`raffinaat`→`product`-stagekleur op de flows draagt het onderscheid concentraat→NdPr/Dy-oxide→NdFeB-magneet.
  Precedent = uranium (conversie/verrijking/fab alle refinery, reactoren market). Magneet = stage `product` (geen 4e stage).
- **Nieuwe grenscorridor `grens-ruili`** (24.02, 97.85; Myanmar→China) in `_chokepoints.js`, `kind:"grensovergang"` — exact
  het Kasumbalesa-patroon (landpunt, houdt de landkaart open, id begint niet met `wp-`). Draagt de Dy/Tb-landstroom
  Kachin→Ganzhou. Enige nieuwe knelpunt; alleen REE gebruikt het → geen impact op de andere grondstoffen.
- **Recycling-toggle via `layer:"recycle"` op flows ÉN nodes** (default uit) — het derde optionele-laag-patroon
  (goud=CB, koper=beursvoorraden, REE=recycling). Reden voor de dubbele `layer`: node-gate op `node.layer==="recycle"`
  (i.p.v. `node.type==="recycler"`) zodat **koper's always-on recyclers** (die géén `layer` hebben) ongemoeid blijven en
  alleen REE de chip/zichtbaarheid krijgt. `hasRecycle()` detecteert op `f.layer==="recycle"` (niet op recycler-type), dus
  koper krijgt geen chip. Vijf plekken: `config.js` (marker-size bestond al) · `main.js` (default + `hasRecycle()` + voyages-gate)
  · `flows.js` (flow-gate) · `markers.js` (node-gate) · `ui.js` (chip).
- **5 co-located nodes ~30–45 km verschoven** (Baotou/Ganzhou ref+mag, MP mijn+scheiding, La Rochelle ref+recycler,
  Fort Worth mag+recycler). Reden: ze zaten in dezelfde 0,25°-rastercel → de router gaf een 1-punts pad (`degDist:0`,
  onzichtbare arc). Verschoven binnen dezelfde stad/regio zodat de lokale scheiding→magneet-arcs zichtbaar renderen én
  de headless-teller schoon op 0 kapot komt i.p.v. de bekende `degDist:0`-baseline uit te breiden.
- **Géén nieuwe render-modus** (schip+land, net als koper); recycling reist over land (`road`). Geen luchtroute-modus.

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
- **Linear M8 aangemaakt** — milestone `M8 · Zeldzame aardmetalen` + **LAR-416 t/m 421** (Backlog), gespiegeld op M9. NB:
  de `331d1eb1`-Linear-MCP bleek wél bereikbaar (dat is een andere server dan de auth-vereiste `plugin:engineering:linear`
  die ik eerst aannam) — eerdere sessie-notitie "MCP-auth ontbrak" was dus onterecht.

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
- **Militaire-kringloop-toggle ALSNOG GEBOUWD** (LAR-414 Done, commit `6a6d062`, 2026-07-15 — Lars vroeg de backlog-toggle af
  te maken). Het **vijfde** optionele-laag-patroon (na goud-CB, koper-exchange, REE-recycle, olie-reserve): `type:"military"`-nodes
  + `layer:"secondary"`-flows + `showMilitary`/`hasMilitary()`, bedraad op exact het olie-reserve-patroon in 5 plekken
  (`config.js` marker · `main.js` filter+has+opts+usedNodeIds · `flows.js` gate · `markers.js` maxMilitaryStock+node-gate+rode-octaëder ·
  `ui.js` chip+label+meta). 4 military-nodes (down-blend Rosatom/HEU, tails-herverrijking, US DOE, US strategische reserve) +
  5 `secondary`-flows (o.a. de historische Megatons-to-Megawatts-stroom Rusland→VS) + tension `u-t-military`. `u-fab-us` op
  `coastal:true` gezet zodat de transatlantische down-blend-ship-leg landt. Headless: uranium 60 legs / 0 kapot / 0 straight;
  toggle uit→aan +4 nodes/+5 flows; chip alleen bij uranium. Nu de code niet meer dirty was (M8/oil gecommit) kon de engine-laag
  eindelijk erbij — sectie J werkte: alleen mijn 6 bestanden gestaged, de parallelle PGM/silver-sessie ontzien.
- **Verificatie (headless, mijn eigen server poort 8743):** uranium **54 legs / 0 kapot** (20 zee + 34 land, **0 straight** →
  de Kaspische oversteek routeert écht over water). Regressie schoon: de 5 overige nulls zijn de bekende `degDist:0` same-city
  hops uit de M5/M6-baseline (lithium 4, goud 1), niet nieuw. Structuurcheck groen. WebGL-screenshot lukt niet headless → visueel = Lars.

## Nog te beslissen (open)
- `atlas-lithium-kobalt.html` / `globe-oud`-restanten opruimen — pas ná **visuele** bevestiging op Netlify/mobiel
  (routeverificatie is al headless gedaan; screenshot lukte niet door WebGL-time-out).
- Evt. **GitHub-remote** voor de nieuwe repo (nu lokaal-only).
