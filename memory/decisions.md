# Decisions — Grondstoffen Atlas
*Last updated: 2026-07-19 (LAR-486 uitgevoerd — corridor-toets + cache + zone-zee-overgang in de baker)*

Vastgelegde keuzes (nieuwste boven). Elk: besluit + korte reden.

## LAR-486 / NL-pilot-implementatie (2026-07-19) — uitgevoerd, keuze open

- **Zee-overgang: NE-water óf waterweg-zone.** De aansluitknoop van een vaarweg-keten mag NE-"land"
  zijn als hij in een `WATERWEG_ZONES`-bbox ligt (dokbekken/estuarium — het M23-aanloop-principe).
  De Maasmond-knoop 6812 is `zone:nl-delta`; een knoop op land buiten élke zone blijft een harde fout.
  De eerste twee bakes (~40 min elk) strandden op de te strenge water-only-check.
- **Verzoening-cache in de baker.** De M23-herberekening is deterministisch en duur (~35–40 min);
  hij wordt nu na de omleg-stap gecached (`build-cache/verzoening_cache.json`, 19 KB, gekeyd op
  knopen+edges-aantallen) en hergebruikt. Les: bewaarpunt éérst bij dure pijplijnen — M24 bakt
  herhaaldelijk. Volgende bakes (VS/China-pilots) kosten ~1 min.
- **Bake-off-varianten als sets.** `--suffix=-unece` bakt `marnet-unece.bin/json` + `ports-unece.json`
  náást de OSM-set; `marnet.js` kiest per `?vaarwegbron=`. Bin+json+ports horen als set bij elkaar
  omdat de haven-snap aan de knopenlijst van precies die bake hangt. Tijdelijk — weg na de keuze.
- **Stitcher is bron-agnostisch.** `fetch_waterways.py` bouwt uit ruwe segmenten het kortste
  waterpad anker-zee → anker-binnen (dijkstra over de segment-geometrie, uiteinden gestitcht op
  tolerantie, DP-simplify 25 m). Zelfde ankers + andere bron = vergelijkbaar traject; herbruikbaar
  voor Mississippi/Yangtze/wereldwijde uitrol.
- **UNECE-data is niet scriptbaar op te halen** — gis.unece.org zit achter een Cloudflare-challenge;
  de laag (`Transportobservatory/E_Waterways_ITIO`, mét CEMT + `SEA_VESSEL`) is via de Browser-pane
  geëxtraheerd naar `build-cache/unece_eww_nl.geojson`. Weegt zwaar in de bron-keuze ("moeite").
- **Winst-metingen niet vanaf een knoop óp het nieuwe kanaal** (label dicht = knoop geïsoleerd) —
  meet vanaf de oude snap-knoop (Markermeer 6781): haven-tot-Shanghai 19.809 → 19.678 = −131 km.
- **Regressie in twee lagen** (aangescherpt door Lars): nieuwe vaarweg-knopen laten NL-havens
  dichterbij hersnappen, dus totaal-km's mógen verschuiven; het bewijs dat het zeenet niet bewoog
  loopt via routes tussen de **oude knoop-ids** (stabiel — nieuwe knopen komen achteraan): 19.610 /
  8.031 exact.

## M24 / bronnenplan binnenwater (2026-07-19) — plansessie, pilots vastgelegd (LAR-486/487/488)

- **De corridor-toets vervangt de vlak-toets.** Rivieren/kanalen bestaan niet als water in de NE-polygonen
  (dáárom waren de 29 `WATERWEG_ZONES` vrijstellingen en eindigt Yangon als stub). M24-controle: elk ~2 km-monster
  van een binnenwater-edge ligt ≤ ε van een bevaarbare-vaarweg-middellijn (procesintegriteit tegen de eigen bron
  + kruis-vergelijking waar een tweede bron bestaat); de polygoon-toets blijft alleen op de zee-overgang gelden
  (mondings-knoop moet op een MARNET-knoop in NE-water landen).
- **Bake-off beslist de bron (Lars).** Kandidaat-model = het M23-model doorgetrokken (MARNET=geometrie,
  kustlijn=scheidsrechter): OSM als geometrie overal (enige wereldwijde bron mét kanálen + CEMT-klassen in de EU;
  voor China/Myanmar bestaat toch niets officieels), officiële netten als onafhankelijke meetlat — UNECE
  E-waterway-shapefile (EU, Blue Book) en USACE National Waterway Network (VS, public domain). Niet blind gekozen:
  LAR-486 bouwt NZK + Waal twee keer (uit OSM én uit UNECE) en vergelijkt kwaliteit/moeite/beeld op de bol.
  Afgevallen: Natural Earth rivers (géén kanalen — het Noordzeekanaal ontbreekt er letterlijk in) en HydroRIVERS
  (DEM-afgeleid: geen kanalen, geen bevaarbaarheid). Een wereldwijde kant-en-klare bevaarbare-vaarwegen-dataset
  bestaat niet (geverifieerd via websearch; het bekende GIS-gat).
- **Pilot per regio vóór de uitrol** (Lars: *"het maken van de binnenvaartroutes lijkt me veel werk… wel eerst
  pilot per systeem"*): NL/EU (LAR-486) → VS (LAR-487, Mississippi × USACE) → China (LAR-488, Yangtze), elk
  bewijst één controle-situatie (twee onafhankelijke bronnen / USACE-meetlat / géén scheidsrechter). China is
  bewust de zwaarste test en valideert de aanpak voor Paraná/Irrawaddy/Wolga/Mekong/Congo.
- **Einddoel: het complete commercieel bevaarbare net** (Lars: *"ik wil ze wel alvast allemaal mappen zodat als
  we een nieuwe grondstof toevoegen dat we die wegen gewoon kunnen gebruiken"*) — EU CEMT ≥ IV (de vrachtrelevante
  grens; dekt Hengelo/Born), VS het USACE-net (inland gefilterd), elders de bekende commerciële systemen;
  recreatief klasse I–III bewust niet (ruis). Omvang ≈ orde marnet.bin → past ruim in het budget.
- **Beleid binnenvaart-vs-zeeschip: labels nú meebakken** — passage-label per systeem (zoals `suez`/`northwest`)
  + zeevaart-vlag waar zeeschepen echt komen (NZK, Yangtze t/m Nanjing, Seaway). Router blijft permissief;
  filteren is aan M26/M21 via het bestaande `vermijd`-mechanisme. Rebake is de dure stap, labels nu bijna gratis.
- **OSM = ODbL** → "© OpenStreetMap contributors" bij de HUD-credits (naast de Esri-vermelding).

## M23 / MARNET-verzoening (2026-07-18) — LAR-483 uitgevoerd

- **Verzoenen tegen de 1:10M-vectorwereld van v2, niet de 1:50M `geo-data.js`.** Het M22-kernbesluit
  (vector = waarheid) doorgetrokken: routering rekent tegen exact de lijnen die Lars op het scherm ziet.
  LAR-483 noemde nog geo-data.js — dat was vóór M22 bestond.
- **Meren tellen als water in de land-toets** (`ne_10m_lakes` naast land + minor islands). MARNET vaart
  écht over de Grote Meren/Seaway, het IJsselmeer en de Wolga-Don-stuwmeren; zonder meren-als-water leek
  de halve Seaway "kapot" (508 → 243 verdachte edges door deze ene stap). Null Island (NE-artefact op 0,0)
  wordt gefilterd.
- **Drie klassen, drie behandelingen:** *aanloop* (treffer ≤5 km van een knoop: dokbekken/riviermond —
  niets doen) · *binnenwater* (29 zones voor kanalen + rivieren die NE-land niet als water kent — als-is
  bewaren met `soort=1`, M24 verfijnt) · *kapot* (koorde snijdt kaap/eiland — omleggen). Rivieren zijn
  géén bugs; ze verdienen een flag, geen "fix" om het continent heen.
- **Omleggen in vier trappen: 0,02° gebufferd → 0,01° gebufferd → 0,01° kaal → 0,02° kaal.** De kustbuffer
  beschermt tegen koorden die de kust scheren, maar knijpt nauwe straten (Dardanellen, Magellaan, Inside
  Passage, fjorden) dicht — de kale herkansing is verplicht. Resultaat 148/150.
- **Eindtolerantie per uiteinde, gemeten op de oorspronkelijke koorde** (aaneengesloten landtreffers vanaf
  de knoop, gaatjes <3 km, plafond 30 km). Sommige MARNET-knopen liggen zelf in een dokbekken/riviermond;
  een vaste 5 km-tolerantie keurde daar élke correcte omlegging af.
- **Lon-normalisatie in de graafbouw is verplicht.** MARNET heeft 15 knopen dubbel op lon +180 én −180 —
  de trans-Pacific lanes eindigen op +180 en vervolgen op −180. Zonder merge is de Stille Oceaan bij de
  datumgrens doorgeknipt (Yokohama→LA rekende 32.000 km via Suez+Panama).
- **Passage-restricties in de router; default `northwest` dicht — exact searoute's eigen default.** Kortste
  graafpad ≠ commerciële route: zonder restrictie koos Rotterdam→Shanghai de Noordwest-Passage (15,5k km).
  Bewust géén arctis-straf toegevoegd: met alleen deze blokkade wint Suez vanzelf (empirisch). Dit
  mechanisme is meteen M21: "Suez dicht" = `"suez"` toevoegen aan `opties.vermijd`.
- **`route.km` = echte kilometers, niet de strafkilometers** — bij een eventuele kostfactor blijft de
  uitlezing de gevaren afstand.
- **Cache-discipline geldt ook voor data:** `marnet.bin`/`marnet.json`/`ports.json` dragen `?v=` mee met de
  assets (nu 011). Een nieuwe bake zonder bump test tegen de vorige data (dit ging in de sessie bijna mis).
- **Havens gesnapt aan de dichtstbijzijnde knoop bij het bakken** (3.962 stuks, mediaan 31 km) — de route
  begint/eindigt op de graaf; het stukje haven→knoop wordt als recht aanloopstuk getekend.

## M22 / v2 (2026-07-18) — het nieuwe fundament

- **Géén globe-library; Three.js met onze eigen bol.** globe.gl is een wrapper om wat we al hebben; Cesium
  brengt z'n eigen imagery/terrein mee en dus een **vierde wereldmodel** — precies wat M22 wil wegnemen;
  deck.gl zou een tweede renderstack naast Three zetten. De library bepaalt de schoonheid niet: shaders en
  data doen dat.
- **Three r128 → r185, ES-modules met importmap, geen bundler.** Lars koos expliciet voor écht upgraden
  ("zodat we niet nog een keer hoeven te upgraden"). Prijs bewust geaccepteerd: **M26 wordt deels herbouw
  i.p.v. verhuizing**, want `markers.js`/`flows.js`/`voyages.js` draaien op verdwenen r128-API's
  (`outputEncoding`/`sRGBEncoding`). Three levert sinds r150 geen `three.min.js` meer → het globals-patroon
  van v1 vervalt binnen `v2/`.
- **WebGPU bewust NIET.** Koopt doorvoer, geen schoonheid; onze scene is geometrie-/CPU-gebonden. De renderer
  is wel wisselbaar gehouden.
- **De vectorwereld is de bron van waarheid** (door Lars bevestigd: *"nu kunnen we die vectorlijnen als bron
  van waarheid gebruiken"*). Natural Earth **1:10M**; satelliet en tegels zijn een **skin**. Hiermee is de
  drie-wereldmodellen-kwaal structureel weg: routering rekent straks tegen dezelfde lijnen die Lars ziet.
- **Formaat van het wereldmodel:** quantiseren op **1e-4 graden** (~11 m, ruim onder de 1,5 km puntafstand)
  + delta-codering + zigzag-varint = **3,3 byte/punt** → 481.675 punten in **1,64 MB** (was 11,5 MB ruwe
  GeoJSON). Eén `LineSegments` = één draw call.
- **Zoom rekent in HOOGTE boven het oppervlak, niet in afstand tot het middelpunt.** Dat laatste was de
  eigenlijke rem: bij straal 2,4 en `minZoom 2.75` kwam de camera nooit lager dan ~930 km, en de laatste
  900 km waren een handvol stappen. Nu vermenigvuldigt elke stap de hoogte → gelijk gevoel van 22.000 km tot
  1 km. Nabij-vlak schuift mee; `logarithmicDepthBuffer` aan (anders flikkeren tegels en lijnen over dat bereik).
- **Ondergrond en kustlijn zijn losse lagen**, geen of-of-keuze: ondergrond = satelliet | kaart | egaal,
  kustlijn = aan | uit. Default satelliet + kustlijn (Lars' voorkeur, en meteen de beste visuele controle op
  de uitlijning).
- **Esri World Imagery + OpenStreetMap als tegelbronnen, Google uitgesloten.** earth3dmap.com geeft bij
  straatniveau over aan een ingesloten Google Maps; die tegels mogen niet in een eigen 3D-bol. Esri gaat zelf
  tot z19 (~30 cm/px in bewoond gebied) met verplichte bronvermelding — die staat nu in beeld.
- **Belichting en tone mapping horen bij elkaar.** ACES aanzetten zónder de belichting mee te verhogen maakt
  het beeld juist *donkerder* (ACES drukt middentonen). Ingemeten paar: zon 6,0 + belichting 1,6 → zelfde
  gemiddelde helderheid als v1 met **0% uitgebrande pixels** (was 0,03%) en méér doortekening in de
  hooglichten. *Correctie op een eerdere te stellige claim: v1 zette `outputEncoding` wél goed; de winst zit
  in tone mapping + de fysieke belichting van r155+, niet in een kapot kleurdomein.*
- **⚠️ lat/lon → 3D moet EXACT v1's `latLonToVec3` volgen:** `x = cos(lat)·cos(lon)`, `y = sin(lat)`,
  `z = −cos(lat)·sin(lon)`. Het moet tegelijk kloppen met de UV-afbeelding van `THREE.SphereGeometry`
  (lon 0 op +X) én met de markers/routes die in M26 uit v1 komen. Een 90°-fout hier verschuift straks alles.
- **Verificatiepatroon dat werkte:** toets tegen een **onafhankelijke scheidsrechter**, niet tegen je eigen
  aanname. `earth-water.png` als land/water-orakel gaf 80–83% van de kustpunten op een grens vs 4,8% voor
  willekeurige punten — en met de oude (foute) formule 8%, dus de test zakt ook echt bij de fout.
- **De landvulling is VERVALLEN.** Met tegels als oppervlak is er niets meer te vullen; polygoon-vulling is
  alleen nog relevant voor de "egaal"-weergave. Scheelt de triangulatie op een bol (antimeridiaan/Antarctica).

## Architectuur (2026-07-18) — de patch-spiraal doorbroken

- **Vorm, vaarsnelheid en baan-klem zijn ONTKOPPELD.** Eén puntenlijst droeg alle drie, met tegenstrijdige
  eisen: vorm wil weinig punten · vaarsnelheid wil punten gelijkmatig over afstand · de klem wil juist veel
  punten in nauw water. Vereenvoudigen voor de vorm sloopte de klem (banen over Japan); verdichten voor de
  klem liet de schepen schokken en maakte lijnen hoekig. **Elke fix wás een nieuwe bug** — Lars zag dat als
  eerste: *"anders blijven we heen en weer gaan zonder echt een fix."* Na ontkoppeling verbeterde **alles
  tegelijk**: snelheidsvariatie 15,9× → 1,27×, landtreffers 406 → 108, Japan 8 → 0, Baja 21 → 0, Malakka 9 → 0.
  Middelen: `voyages.js` op **`getPointAt`** (booglengte i.p.v. curve-parameter) · `lane_widths.js` schrijft een
  **apart profiel `wp`** per 20 km langs de boog i.p.v. `w` per punt · `flows.js` voegt per-leg profielen samen
  (`mergeProfiles`) · `util.js` leest via booglengte-fractie + hogere `arcLengthDivisions`.
- **Cache-busting hoort in de pipeline** (`tools/stamp_assets.js`, inhouds-hash `?v=<sha1>`). `index.html` laadde
  assets zónder versie terwijl Pages `max-age=600` stuurt → Lars zag **drie fixes lang "geen verschil"** terwijl
  alles wél live stond. Dit was de bron van de meeste frustratie van de sessie, niet de routing zelf.
- **Een antipodale stabilisator moet op een DICHT stuk netwerk liggen.** Bijna-antipodale havenparen hebben een
  wiskundig onbepaalde geodeet; MARNET kiest dan willekeurig (Valparaíso→Ningbo koos zuid terwijl 7 zusters op
  50°N kruisten). Eerste poging via 50°N/180° gaf een **kaarsrechte interpolatie door leeg water** — rond de
  datumgrens heeft MARNET nauwelijks knopen, dus één artefact ingeruild voor een ander. Via **−10°/−80°** (vóór
  Peru, midden op de zusterlane) deelt Valparaíso nu **95 van z'n 100 punten** met Antofagasta→Ningbo.
  Kosten bewust betaald: +2,5% → +5,8% boven de grote cirkel — **vorm boven lengte**.
- **Trapjes horen in de baker opgeruimd, niet in de render.** `detour_around_land()` legt een A\* over een
  0,1°-raster → trapjes van 45°. `simplify_water()` haalt punten weg die <12 km van de lijn buur→buur liggen
  **en** waarvan de kortsluiting over water blijft (zelfde bewijslast als `dezigzag`). Validatie **fijn
  bemonsterd** (≥10 monsters per kortsluiting): met de standaard 12 km-stap glipten de Channel Islands
  (34,01/−119,6) door een segment van 15 km.
- **De restfout is structureel → LAR-483, niet doorpatchen.** Corridors worden per haven-paar gebakken; daardoor
  bundelen routes naar dezelfde bestemming niet en wordt dezelfde kapotte edge steeds opnieuw gerepareerd
  (7 corridors deelden hetzelfde Baja-trapje). **MARNET gemeten:** 15.840 segmenten / 9.646 knopen, segment
  mediaan 83 km maar **max 3.611 km** = een grove graaf, geen waterkaart → kaal over de bol leggen voorkomt
  land-treffers níet; het netwerk moet **één keer** verzoend worden met onze landpolygonen.
- **MARNET blijft de router; AIS wordt een aparte laag** (LAR-482). AIS toont *schepen*, geen *lading*, en
  gratis wereldwijde historische AIS bestaat praktisch niet. Lars' "echte schepen op de bol met een knop"
  is een dichtheidslaag ná M18, geen router-vervanging.
- **Weergave apart houden van routing.** *"Je kan het water niet echt goed onderscheiden op deze kaart"* is
  contrast/basemap (LAR-480), geen routing — bewust gescheiden zodat de sporen niet door elkaar lopen.

## Weergave / interactie (2026-07-17) — LAR-479 + LAR-481

- **2026-07-17 · `tier` stuurt de LABELS, niet de markers (LAR-481).** De tier-LOD verborg in de praktijk alleen de
  handvol context-nodes zónder stroom: `forced` (uit `usedNodeIds`) overrulet tier, en dat gold voor **57 van de 63**
  koper-nodes. Gevolg: Chuquicamata (share 1,6, géén stroom) plofte in beeld terwijl Los Pelambres (1,6, wél stroom)
  bleef staan — zichtbaarheid hing af van of een mijn toevallig een lijntje had, niet van belang. **Waarom deze fix
  en niet "tier écht laten werken":** de labels (met `labelZoomByTier` + botsingsdetectie) zijn wat de kaart werkelijk
  rustig houdt, en voor 57/63 nodes wás "altijd zichtbaar" al het feitelijke gedrag — dit maakt het consistent i.p.v.
  willekeurig. De alternatieve route (stromen óók tieren) is inhoudelijk mooier maar raakt `flows.js` = de M18-pilot-
  code → bewust ná M18. **Gevolg:** `tierZoom` (config) + de `forced`/`usedNodeIds`-uitzondering zijn verwijderd — het
  gevaar dat ze afdekten ("een lijn eindigt in het niets") kán niet meer optreden. ⚠️ **Sectie I van `CLAUDE.md`
  noemde de `usedNodeIds`-gate als vast patroon voor een nieuwe optionele laag — dat klopt niet meer** (gecorrigeerd).
- **2026-07-17 · Het tegelbudget is een noodrem, geen dagelijkse limiet (LAR-479).** `maxTiles: 40` was **kleiner dan
  één patch** (42–72 tegels) → hij liep bij normaal inzoomen áltijd leeg. Budget → **96**, en de patch vult **van het
  midden naar buiten** i.p.v. noord→zuid. *Waarom center-out: bij een budget-hit moet je de tegels langs de bolrand
  verliezen, niet de halve onderkant; de sortering maakt de degradatie symmetrisch en zoomonafhankelijk, zodat een
  toekomstige hit nooit meer als "band" leest.* `shellMaxZ: 3` bewust ongemoeid — de shell is nu nergens meer in beeld,
  dus de oude LAR-394-afweging (meer tegels = zwaarder op mobiel) hoeft niet opnieuw gemaakt.
- **2026-07-17 · Tegel-zoom is breedtegraad-afhankelijk: `cos(lat)` hoort in `detailZoomFor()`.** Een Mercator-tegel
  op 60° breedte beslaat de helft van de grond van eentje op de evenaar; zonder die term vroeg de code hoe noordelijker
  hoe méér tegels aan voor **dezelfde** scherpte. Dat was niet alleen verspilling maar de reden dat hoge breedtegraden
  veel erger waren (Noorwegen 33%/0% dekking vs. China). Met de term is het tegelaantal breedtegraad-onafhankelijk.
- **2026-07-17 · Draaien schaalt met de camera-afstand, geankerd op de STANDAARDZOOM.** Een vaste rad/px maakte de bol
  op volle zoom ~9× te gevoelig (je ziet dan 9× minder wereld). *Waarom geankerd en niet fysisch 1:1: Lars klaagde
  alleen over ingezoomd; echte 1:1-grab zou de standaardzoom 4,4× trager maken op een 900px-scherm — dat is niet
  gevraagd (zie [[feedback-no-shotgun-fixes]]). De **wet** is identiek aan 1:1 (evenredig met d), alleen de gain komt
  uit wat Lars al gewend was.* Knoppen: `dragSpeed` + `dragRefZoom` in `config.js`.

## Koerswijziging — eerst de routes, dan de features (2026-07-17)

- **2026-07-17 · PILOT-BASELINE corrigeert de milestone-diagnose: de 1.090 km-omweg bestaat niet.** Eerlijk gemeten
  (in de draaiende atlas, tegen het werkelijk gerenderde pad mét via-keten): onze bol 20.615 km (zuidom) vs. searoute
  20.384 km = **231 km / 1,1%**. De 1.090 km kwam uit de vergelijking tegen "route A" (kale run zonder via) — exact de
  fout die de harde regel verbiedt. Oorzaak: Antofagasta↔Shanghai is **93% antipodaal** → noordom en zuidom vrijwel
  even lang; `wp-pac-zuid` stabiliseerde een wiskundig onbepaalde geodeet (stond al in `_chokepoints.js`).
  **Herijkte winst M18** (22 koper-zeereizen): lengte **−2,9%** · **trapjes 37→25 bochten** (dé zichtbare winst) ·
  A\*/rasteropbouw uit de runtime · M21 mogelijk. Lars' go op dit herijkte argument: *"MARNET is het meest realistisch."*
- **2026-07-17 · BESLIST (Lars): MARNET beslist — zee-corridors kaal haven→haven, óók echte knelpunten niet meer
  afdwingen.** De pilot vond `wp-taiwan` (marker:true!) in ketens waar het niet hoort: Chili→Shanghai +**1.497 km**
  (noord tot 50°N → omlaag naar de Straat van Taiwan → weer omhoog). De (a)/(b)-lijn op *soort punt* volstaat niet;
  de fout zit in *welke keten*. Dus: `via` op zee-runs verdwijnt volledig (aanloophavens blijven als echte stops);
  knelpunt-passage wordt **afgeleid** uit `traversed_passages` + polyline-nabijheid tot marker:true-punten → daaruit
  de `laneShape`-ankers en gouden ringen, op de plek waar de route er écht langs komt. Spec: zeeroutes.md §8.

- **2026-07-17 · De zee-A\* wordt vervangen door een echt scheepvaart-lanen-netwerk (M18).** Reden: de routing is
  aantoonbaar onrealistisch, en de drie geplande features **staan erop** — een impact-teller op verkeerde routes is
  erger dan geen teller. **Bewijs:** Antofagasta→Shanghai = grote-cirkel 18.526 km · searoute (echte lanen, MARNET)
  18.880 km (+2%) · **onze bol 19.970 km (+8%)** → het handgeplaatste vaarpunt **`wp-pac-zuid`** (lat −26,00 /
  lon −125,00) dwingt **~1.090 km omweg** af (~een week varen). Conservatief gemeten (via-keten als kale
  grote-cirkels; het echte A\*-pad met trapjes is langer).
- **2026-07-17 · Diagnose: drie samenwerkende oorzaken in `searoute.js`** — (1) **`openRadiusDeg: 1.2`** = een schijf
  van ~130 km geforceerd water rond élk knelpunt; bedoeld om smalle straten (~35 km) open te houden in het grove
  raster, maar het zet óók land op "water" → A\* vaart vlak bij een knelpunt dwars over schiereilanden/eilandjes.
  Hoofdboosdoener. (2) **8-richtingen-A\*** → trapjes (Golf→Rotterdam = 33 richtingswissels). (3) **Grof 0,25°-raster
  + `heuristicWeight: 1.35` + géén echte vaarlanen** → het vindt het kortste *watertraject*, niet de lane die schepen
  varen → kaarsrechte runs langs een breedtegraad/meridiaan.
- **2026-07-17 · De `via`-ketens zijn grotendeels handmatige compensatie voor een slechte router.** Onderscheid dat
  we voortaan maken: **echte fysieke doorgangen** (Hormuz/Malakka/Suez/Panama/Bosporus/Lombok/Kaap) = houden, want
  searoute volgt ze by-design én ze zijn `tension`-ankers; **navigatie-hulpjes** (`wp-pac-zuid`/`-west`/`-noord`,
  `wp-golf-mexico`/`-florida`/`-caribisch`) = bestonden alleen om het kale A\* te sturen → kandidaat om te sneuvelen.
  `grens-*` blijft (landkaart). ~~**Open besluit (Lars, bij de pilot):** opruimen (a) of behouden als hint (b).~~
  → **BESLIST 2026-07-17, zie hieronder: (a) opruimen.**
- **2026-07-17 · BESLIST (Lars): via-punten (a) OPRUIMEN — mét ingesloten-water-nuance.** De navigatie-hulpjes op
  **open water** gaan uit de via-ketens van zee-legs; searoute doet de rest. De **ingesloten-water-ketens**
  (`wp-st-laurent-1…4`/`-2b`, `wp-kaspisch-n/-m/-z`, `wp-dardanellen`) worden **individueel empirisch getoetst**
  vóór ze sneuvelen — die forceren een corridor die MARNET mogelijk niet dekt (Saint-Laurent-rivier; Kaspische Zee
  = gesloten zee). Eerst door searoute halen, dán slopen (M13/M17-patroon: toetsen, niet gokken).
  **Redenen:** (1) `wp-pac-zuid` kost ~1.090 km omweg; (2) **valse flessenhals** — `flows.js` zet een anker op elke
  tussenstop (`if (i < stops.length-2) anchors.push(...)`) en `laneShape` maakt de verschuiving nul bij elk anker,
  dus alle Chili/Peru→China-koperstromen knijpen samen op **26°Z/125°W** = open oceaan waar níets is → de kaart
  tekent een knelpunt dat niet bestaat; (3) een handgeprikt A\*-duwtje overrulet MARNET's lane-kennis.
  **Omvang speelde géén rol:** gemeten is (b) 987 legs→381 corridors vs (a) 698 legs→340 corridors = **11% verschil**
  → de dedup vangt het meeste al weg; dit is puur een realisme-besluit. Spec: `design/zeeroutes.md` §8.
- **2026-07-17 · searoute's `restrictions` = de M21-machinerie, empirisch bevestigd.** Golf (Ras Tanura)→Rotterdam:
  normaal **12.066 km** (via Suez) · `restrictions=['suez']` → **20.924 km** om de Kaap (**+73%**, herrouteert zelf) ·
  `restrictions=['ormuz']` → **`length: 0` + UserWarning "No path found"**. Beschikbaar: suez/panama/ormuz/malacca/
  bosporus/babalmandab/gibraltar/sunda/bering/northwest/chili/south_africa.
  ⚠️ **"Geen route" is een geldige én de interessantste uitkomst** (Ras Tanura ligt bínnen de Golf → Hormuz dicht =
  geen alternatief, niet een langere route). Het meldt zich als **0 + warning, geen exception** → moet als
  *isolatie* gerenderd/geteld worden, **nooit als "0 km"** in een impact-teller (M19/M21). Dit is exact het soort
  stille fallback dat de spec verbiedt. Verhaal in één regel: *Suez dicht is duur, Hormuz dicht is: het houdt op.*
- **2026-07-17 · `traversed_passages` bewaart M21's query én controleert onszelf.** `return_passages=True` geeft per
  route de gepasseerde doorgangen (Golf→Rotterdam: `['suez','babalmandab','gibraltar','ormuz']`). → "welke stromen
  raakt knelpunt X?" wordt een **query op de cache** i.p.v. handmatige annotatie, én het is een gratis
  **kruiscontrole** op onze eigen `via`-ketens/`tensions`. Wordt per corridor meegeschreven in `_searoutes.js`
  (kost een paar bytes). Let op de sleutel: het veld heet **`traversed_passages`**, niet `passages`.
- **2026-07-17 · Datamodel `_searoutes.js` vastgelegd** (spec §3–§4): sleutel = **coördinaat-paar** (3 decimalen,
  gesorteerd → richtingsonafhankelijk, robuust bij hernoemde nodes zoals Roberts Bank→Ridley); **precisie 3
  decimalen** (~110 m) → gemeten raming **357 KB** voor 381 corridors (steekproef 12 corridors: 2 dec=319 KB,
  3=357, 4=397, 5=429), **geen extra decimatie** in M18; **fallback = hard falen zichtbaar** (console.warn +
  leg níet renderen → telt als kapot in de legs-check), nooit stil terugvallen op de oude A\*.
  **Verificatie-drempel:** niet "afwijking >15% = fout" maar **">15% zonder doorgang in `traversed_passages` = fout"**
  — Golf→Rotterdam via Suez is +73% en volstrekt correct (grote cirkel gaat dwars over Arabië); de
  `wp-pac-zuid`-signatuur is juist: veel afwijking, géén doorgang.
- **2026-07-17 · M21-netwerk: nu niet bouwen, wél openhouden.** Twee wegen — (a) scenario's vooraf bakken
  (~12 restricties × 381 corridors; runtime blijft dom, maar combinaties exploderen) of (b) MARNET meesturen
  (729 KB geojson + Dijkstra in JS; élke edge live weghaalbaar). **Keuze valt bij M21 zelf**, met de dan gemeten
  omvang. M18 houdt (b) mogelijk door `traversed_passages` mee te schrijven + de generator parametriseerbaar te
  houden op `restrictions`. Niet vooruitbouwen aan iets dat drie milestones verderop ligt.
- **2026-07-17 · Architectuur: precompute at build-time, gededupliceerd per haven-paar.** Eén gedeelde corridor-cache
  over alle 14 grondstoffen (Lars: *"voor veel grondstoffen zijn de routes vrijwel hetzelfde"* → je routeert unieke
  corridors, niet elke flow apart) → polylines in `data/_searoutes.js`, atlas rendert direct. **Netwerk bewaren** voor
  M21 (knelpunt blokkeren = *edge eruit → herrouteren*; een zeestraat ís een edge, geen verzameling rastercellen →
  M21's oude raster-masker-aanpak is hiermee **herijkt**). **Raakt alleen zee-legs**; land/lucht ongemoeid. Runtime
  blijft pure JS; `searoute` wordt een **build-dependency** (`build-standalone.py` is al Python). Bonus: A\* uit de
  runtime = lichter op mobiel.
- **2026-07-17 · Feature-trio hernummerd** — M18→**M19** (knelpunt-stress), M19→**M20** (China-meta-view),
  M20→**M21** (disruptie-simulator), incl. alle kruisverwijzingen. M18 = de fundering.
- **2026-07-17 · Pilot-first met koper.** Bevat de bewezen-foute Antofagasta-corridor + de Andes-trechter + de
  Copperbelt-**land**routes (die ongemoeid moeten blijven → bewijst dat we alleen zee-legs raken). Go/no-go door Lars
  vóór de andere 13.
- **2026-07-17 · Verificatie-regel (nieuw): vergelijk NOOIT tegen een kale origin→dest A\*-run.** De pilot van
  2026-07-16 deed dat en produceerde "route A" (noordelijk over 43°N) — een pad dat de bol **nergens tekent**, want
  de atlas routeert altijd langs de `via`-keten. Lars zag het onmiddellijk (*"ik zie op onze wereldbol niets dat
  route A neemt"*). Vergelijk altijd tegen het pad dat `flows.js` werkelijk rendert.
- **2026-07-17 · Diagnose-les (methodisch): meet niet in een verborgen Browser-pane.** Een "stilstaande tick-loop"
  bleek een artefact van `document.hidden` (rAF pauzeert), geen bug. Workaround: `GLOBE.start()` handmatig aanroepen
  — `animate()` draait z'n body synchroon. Ook uitgesloten: de tegel-patch-centrering klopt wél (`viewCentre()` is de
  exacte inverse van `latLonToVec3`: `atan2(z,-x)` ↔ `theta=(lon+180)`).

## Backlog leeggewerkt — optionele-laag-cleanup (2026-07-16)

- **2026-07-16 · LAR-471 lab-grown-toggle = het 6e optionele-laag-patroon, via `layer` (niet dedicated type).** De
  uitgestelde diamant-toggle gebouwd nu de engine-tree schoon was. Gekozen voor het **recycle-stijl `layer`-patroon**
  (`type:"labgrown"` voor de marker + `layer:"labgrown"` voor de gate op nodes én flows), niet het reserve/military-
  dedicated-type-patroon — want lab-grown is een schaduw-*aanbod* dat de bestaande product-arcs ondergraaft, geen aparte
  voorraadsoort. `hasLabGrown()` vuurt op `f.layer==="labgrown"` (zoals `hasRecycle`). 3 productie-nodes (China/Henan HPHT
  34.75/113.63, India/Surat CVD 21.24/72.95 = náást de natuurlijke slijperij, VS/Washington premium-CVD Diamond Foundry
  47.42/-120.31) + 6 flows die vooral de **VS-verlovingsringmarkt** voeden. Marker = **violette octaëder** (`0xB98BE0`) —
  een fabrieksgemaakte steen, visueel onderscheiden van de natuurlijke mijn/slijperij. 5 engine-plekken (config/main/flows/
  markers/ui), default uit, chip alleen bij diamant. In v1 bleef lab-grown een `tension`; die tension wijst nu naar de
  echte lab-grown nodes/flows.
- **2026-07-16 · LAR-447 recycle-tooltip per-grondstof via een `recycleHint`-resourceveld.** De gedeelde chip-tooltip in
  `ui.js` was hard-coded REE-bewoord ("magneetschroot, <5%") — feitelijk onjuist voor PGM (~25% autokat = katalysatorschroot)
  en grafiet. Fix zonder de engine te vervuilen: een optioneel `recycleHint`-veld op de resource-metadata + een
  `main.recycleHint()` die de hint van de actieve recycle-grondstof doorgeeft in `opts`; `ui.js` valt terug op een generieke
  tekst als er geen hint is. Hints op REE/PGM/grafiet (de 3 met `layer:"recycle"`). Koper (recyclers always-on, géén layer)
  krijgt geen chip → ongemoeid.
- **2026-07-16 · LAR-448 PGM krijgt een TWEEDE optionele toggle (beursvoorraden) — conventie bewust doorbroken.** De issue
  pleitte er zelf tegen ("één toggle per grondstof is de conventie; recycling is voor PGM dominanter"), maar Lars gaf akkoord
  om 'm toch te bouwen. Pt/Pd zíjn beursverhandeld (NYMEX/CME + TOCOM-futures, LPPM-kluizen) → feitelijk valide. Pure data,
  **0 engine-wijziging**: hergebruik van de bestaande koper/nikkel/zilver-`exchange`-toggle (`type:"exchange"` + `layer:
  "exchange"`, `hasExchangeStocks()` is generiek). 3 kluis-nodes (LPPM Londen/NYMEX New York/TOCOM Tokio, `stock` in t 3E) +
  3 `layer:"exchange"`-bufferflows naar de autokat-markten. **PGM is nu de eerste grondstof met twee toggles naast elkaar**
  (recycling + beursvoorraden) — technisch prima want elke laag is onafhankelijk gegate; recycling blijft het dominantere
  verhaal. Precedent: een grondstof mag meerdere optionele lagen dragen.
- **2026-07-16 · verificatie-gotcha: de Browser-pane cachet script-tag-files hardnekkig** (python `http.server` stuurt geen
  no-cache headers → `navigate`/`location.reload()` herladen `data/*.js`/`src/*.js` niet vers). Bevestigd met een
  cache-buster-`fetch` (server hád de nieuwe inhoud). Oplossing: engine-logica gevalideerd via in-memory injectie in
  `RESOURCES`, en een **tweede server-instance op een andere poort** (8733) = schone origin voor de definitieve verse-load-
  verificatie. Les voor volgende sessies: start desnoods een `-2`/`-3`-server voor een gegarandeerd verse load.

## M15 · Gas — uitgevoerd (2026-07-16)

- **2026-07-16 · gas = de natuurkunde: gas is nauwelijks te verplaatsen.** De vorm is bewust anders dan alle eerdere:
  géén enkele trechter maar **twee gescheiden leversystemen** die op de kaart tegen elkaar afsteken — **captive
  pijpleidingen** (lage donkere `erts`-land-arcs: Rusland↔EU was, Power of Siberia→China, Turkmenistan→China, Noorwegen→
  EU, Zuidelijke Gascorridor) vs **LNG** (heldere `raffinaat`-oceaan-arcs). Waarom: over land zit gas vast in een pijp
  (wie aan het andere eind zit is je enige klant/leverancier); écht globaal wordt het pas na vloeibaarmaking.
- **2026-07-16 · de liquefactie-stap is de trechter (niet een zeestraat).** Gas' equivalent van de China-raffinage bij
  lithium: pas ná vloeibaarmaking (−162 °C, een trein kost $10-20 mld) is een molecuul een omleidbare wereldgrondstof.
  Capaciteit bij **drie polen** (VS-Golfkust flexibel / Qatar-Ras Laffan grootste-via-Hormuz / Australië→Azië). Dat draagt
  via een `tension`, geen `wp-`. Liquefactie-terminal = `refinery`, regas-terminal = `port`, opslag = `reserve` → **géén
  nieuwe marker-types**. Schip + `pipeline` (beide bestaan; pipeline kwam met olie) → **géén nieuwe render-modus**.
- **2026-07-16 · géén nieuw chokepoint (4e na nikkel/olie/zilver).** Gas hergebruikt de bestaande routekaart volledig
  (Hormuz/Malakka/Suez/Bab/Rode Zee/Gibraltar/Panama/Kaap/Lombok/Makassar/SCS/Taiwan/Florida). **Empirisch bevestigd** dat
  géén nieuw vaarpunt nodig is: de 2 Arctische Yamal-routes (Sabetta→EU via de Barentszzee 107 pts, →China via de
  Noordelijke Zeeroute 255 pts), de Med-crossing (Arzew→Spanje) en de lange captive-pijpleidingen (POS 55/Turkmenistan 75/
  Azerbeidzjan-Balkan 55 pts) routeren allemaal correct. Qatar's Hormuz-afhankelijkheid is **scherper dan olie** (géén
  Yanbu/Fujairah-bypass — LNG kan alleen over zee weg). Iran = het scherpste reserves≠export (zelfde veld als Qatar).
- **2026-07-16 · opslag-laag hergebruikt de olie-`reserve`-toggle met 0 engine-wijziging.** `hasReserves()` is generiek op
  `n.type==="reserve"` (geverifieerd `src/main.js:23`) + de flow-gate `f.layer==="reserve"` (flows.js) — dus gas voegt
  4 `type:"reserve"`-nodes (EU Rehden/Bergermeer, Oekraïne-caverns, US Henry Hub, China) + 5 `layer:"reserve"`-vul-flows
  toe als **pure data**; de "voorraden"-chip + amber tank-marker verschijnen automatisch. 3e datagedreven hergebruik van
  het reserve/exchange-patroon (na nikkel/zilver-exchange). De EU-winter-vulgraad (90%-mandaat) = gas' geopolitieke metric na 2022.
- **2026-07-16 · nieuwe 12e grondstof — de git-index-race als les (sectie J).** Gas bestond nog niet → nieuw `data/gas.js`
  + `<script>`-tag in `index.html` + 5 gas-checks in `build-standalone.py`. Gebouwd náást 3 andere nieuwe-grondstof-sessies
  (grafiet/kolen/diamant). Een **git-index-race** veegde diamant's gestagede bestanden in mijn eerste commit; teruggedraaid
  met `reset --soft` + `restore --staged` + **`commit --only`**. **Vastgelegde les:** bij een gedeelde working tree +
  index is `git commit <paths>` / `--only` race-bestendiger dan `git add` gevolgd door een kale `git commit`. Milestone
  hernummerd (Gas=M15/Diamant=M16/Kolen=M17). Commits `040d2b7` (data) + `a8378ef` (build-checks), gepusht → live op Pages.

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
