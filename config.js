// config.js — Alles wat je wilt kunnen draaien aan knoppen staat hier.
// Dit bestand als eerste laden; de rest leest eruit.

const CONFIG = {

  // -------------------------------------------------------------- AARDBOL
  globe: {
    radius: 2.4,
    segments: 128,          // was 64 — hogere waarde = rondere bol
    autoRotate: true,
    autoRotateSpeed: 0.0006,
    // Hoe lang na een aanraking mag de bol weer uit zichzelf gaan draaien?
    // 0 = nooit meer. Zodra jij de bol vastpakt is het jóuw bol; hij begint
    // pas weer te draaien als je de pagina ververst.
    autoRotateResumeMs: 0,
    minZoom: 2.75,
    maxZoom: 11,
  },

  // ------------------------------------------------------------- BASISKAART
  // Welke aardbol-textuur je ziet. Wisselbaar in de UI rechtsboven.
  basemap: {
    default: "satelliet",   // "satelliet" | "nacht" | "donker" | "vector"

    // Waar de textures vandaan komen:
    //   "local" = uit de map textures/  (werkt alleen via een lokale server,
    //             zie README — browsers blokkeren file:// textures)
    //   "cdn"   = rechtstreeks van jsDelivr (werkt altijd, ook bij dubbelklik
    //             op index.html, mits je internet hebt)
    source: "cdn",

    localPath: "textures/",
    cdnPath: "https://cdn.jsdelivr.net/npm/three-globe@2.45.2/example/img/",

    files: {
      satelliet: "earth-blue-marble.jpg",   // 4096×2048 echte satellietkaart
      nacht: "earth-night.jpg",             // 4096×2048 stadslichten
      donker: "earth-dark.jpg",             // rustige donkere kaart
      relief: "earth-topology.png",         // bump map -> bergen krijgen reliëf
      water: "earth-water.png",             // specular map -> alleen zee glimt
    },

    reliefStrength: 0.012,   // 0 = plat, hoger = meer reliëf
    showBorders: true,       // scherpe vectorgrenzen bovenop de textuur
    showCoastlines: true,    // idem voor kustlijnen (blijven scherp bij inzoomen)
    showGraticule: false,    // lat/lon-raster
    borderColor: 0xffffff,
    borderOpacity: 0.25,
    coastColor: 0x9fd8ff,
    coastOpacity: 0.22,
  },

  // ---------------------------------------------------------------- TEGELS
  // Scherpe kaart bij inzoomen: zodra de camera dichtbij komt, wordt er een
  // mozaïek van scherpe tegels over de bol gelegd (zie src/tiles.js).
  // Google Earth-tegels mogen niet gebruikt worden; deze bronnen wel, mits je
  // de bron vermeldt (dat gebeurt rechtsonder in beeld).
  tiles: {
    default: "satelliet",       // "satelliet" | "kaart"
    showBelowCameraZ: 8.5,      // hierboven: gewone blue-marble bol. hieronder: tegels.
                                // Was 6.2 — te laat, waardoor je bij normaal gebruik
                                // steeds tussen tegels en blue-marble "oversprong" (LAR-394).
    tilesAcross: 4.5,           // hoeveel scherpe detailtegels je ongeveer over het beeld wilt
    minZ: 3,
    maxZ: 9,                    // hoger = scherper, maar ook meer laden
    maxTiles: 40,               // veiligheidsplafond voor de scherpe detailpatch
    meshDetail: 8,              // gridfijnheid per detailtegel (Mercator-correctie)
    updateInterval: 0.25,       // seconden tussen herberekeningen

    // SHELL — de héle bol krijgt ALTIJD een laag grove tegels (LAR-393).
    // Vroeger lag de scherpe tegelpatch los boven op de blue-marble-textuur, en
    // rond de patch scheen de blue-marble door: twee verschillende kaarten met
    // een zichtbare naad. Nu bedekt de shell de complete bol met dezelfde
    // (Esri/OSM) tegelbron, en ligt de scherpe detailpatch daar in het midden
    // van beeld bovenop. De grens is dan scherp -> minder scherp van DEZELFDE
    // kaart — geen kaartwissel, geen naad. De shell is bovendien stabiel
    // (hangt niet af van waar je kijkt), dus hij flikkert niet bij het draaien.
    shellMinZ: 2,               // grofste shell: 16 tegels over de hele bol (ver uitgezoomd)
    shellMaxZ: 3,               // fijnste shell: 64 tegels (pas als je flink inzoomt)
    shellZBelowDetail: 3,       // shell is zoveel niveaus grover dan de detailpatch
    // Een z=2-tegel beslaat ~90° lengte. Met te weinig onderverdeling zijn de
    // facetten zo plat dat hun koorde ONDER de bol duikt en de basemap eroverheen
    // prikt (de naad die we juist willen weghalen). Daarom veel fijner rasteren
    // dan de kleine detailtegels, plus wat extra lift als marge.
    shellMeshDetail: 24,        // gridfijnheid per SHELL-tegel (grote tegels -> fijn raster nodig)
    shellLift: 1.0016,          // shell iets ruimer boven het oppervlak (marge boven koordezakking)
    detailLift: 1.0026,         // detailpatch nóg hoger -> tekent altijd netjes over de shell

    sources: {
      satelliet: {
        url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        attribution: "Satelliet: Esri, Maxar, Earthstar Geographics",
      },
      kaart: {
        url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        subdomains: ["a", "b", "c"],
        attribution: "Kaart: © OpenStreetMap-bijdragers",
      },
    },
  },

  // ---------------------------------------------------------------- MARKERS
  markers: {
    mine:     { minSize: 0.022, maxSize: 0.075, pulse: true },
    refinery: { size: 0.042 },
    port:     { size: 0.026 },
    market:   { size: 0.038 },
    airport:  { size: 0.019 },   // gateway-luchthavens (goud vliegt); klein/subtiel
    hub:      { size: 0.034 },   // handels- & kluishubs (Londen/NY/Zürich/Shanghai…)
    cb:       { minSize: 0.030, maxSize: 0.080 }, // centrale banken; grootte = voorraad
    exchange: { minSize: 0.028, maxSize: 0.070 }, // beursmagazijnen (koper); grootte = voorraad
    reserve:  { minSize: 0.032, maxSize: 0.085 }, // strategische reserves (olie/SPR); grootte = voorraad
    recycler: { size: 0.026 },   // schroot terug naar raffinage
    waypoint: { size: 0.020 },   // zeestraten/kanalen (knelpunten op de route)
    lift: 0.015,             // hoe ver boven het oppervlak markers zweven

    // MEESCHALEN MET DE CAMERA.
    // Let op: wat telt is de afstand tot het OPPERVLAK (camera.z − straal),
    // niet de camerastand zelf. Van z=5.6 naar z=3.0 lijkt maar een halvering,
    // maar de afstand tot de grond zakt van 3.2 naar 0.6 — een factor 5.
    // Daar rekenen met de camerastand ging mis: markers bleven klodders en
    // labels groeiden uit tot reuzenletters dwars over het continent.
    //   exponent 1.0 = precies even groot op het scherm
    //   exponent < 1 = groeit een beetje mee bij inzoomen (fijner voor vormen)
    zoomScale: { ref: 5.6, exp: 0.85, min: 0.10, max: 1.15 },
    labelScale: { ref: 5.6, exp: 1.0, min: 0.08, max: 1.10 },
    labelSize: 0.0016,       // basisgrootte van de naambordjes

    // LABELS: geen kader meer (dat dekte de kaart af), maar witte letters met
    // een donkere rand — leesbaar op zowel zee als woestijn. Een kort stokje
    // wijst naar de exacte plek, zodat de naam ernáást kan staan.
    // Botsende labels worden verborgen: wie het belangrijkst is, wint.
    label: {
      fontSize: 30,
      leader: 30,            // lengte van het aanwijsstokje (in canvas-px)
      collide: true,         // overlappende labels wegtrekken
      padPx: 3,              // extra marge bij de botsingstest
    },

    // TIERS: welke locaties zie je op welk zoomniveau?
    //   tier 1 = draagt het verhaal, altijd zichtbaar
    //   tier 2 = havens, middelgrote mijnen — verschijnen onder deze camera-z
    //   tier 3 = detail — pas dichtbij
    tierZoom: { 2: 6.4, 3: 4.6 },

    // Labels per tier (voorheen één drempel voor alles -> labelsoep)
    labelZoomByTier: { 1: 5.4, 2: 4.4, 3: 3.6 },
  },

  // ----------------------------------------------------------------- STROMEN
  flows: {
    minWidth: 0.004,         // dikte van de dunste stroom
    maxWidth: 0.020,         // dikte van de dikste stroom
    opacity: 0.30,
    particleSpeed: 0.10,
    particlesPerFlow: 3,     // wordt vermenigvuldigd met het relatieve volume

    // TWEE WEERGAVEN — schakelbaar in de UI:
    //   "route"       = zoals schepen echt varen: laag over het oppervlak,
    //                   langs havens en zeestraten (via-punten). Hierin zie je
    //                   bundeling en knelpunten.
    //   "hemelsbreed" = rechtstreeks van A naar B in een hoge boog, via-punten
    //                   worden genegeerd. Hierin zie je in één oogopslag wie
    //                   met wie handelt.
    viewMode: "route",

    // -- weergave 1: varen over het oppervlak -------------------------------
    // Nauwelijks hoogte; de ketenstappen liggen als dunne lagen boven elkaar
    // zodat kruisende stromen elkaar niet doorsnijden.
    routeStyle: {
      lift: 0.010,                                    // basishoogte (fractie straal)
      stageOffset: { erts: 0, raffinaat: 0.008, product: 0.016 },
      widthScale: 0.80,
    },

    // -- weergave 2: hemelsbreed -------------------------------------------
    arcStyle: {
      lift: 0.22,                                     // was 0.30 — dat vloog het beeld uit
      stageLift: { erts: 0.70, raffinaat: 1.00, product: 1.30 },
      widthScale: 1.00,
    },

    // VAARBANEN: stromen die dezelfde route delen liggen anders exact op
    // elkaar. Elke stroom krijgt een eigen baan, een klein stukje opzij — maar
    // bij elke haven en elk knelpunt knijpen ze wel weer samén, want daar gaan
    // ze allemaal door dezelfde poort. Dat is precies wat je op zee ook ziet.
    lanes: {
      spacing: 0.012,   // afstand tussen twee banen (klein! anders varen ze aan land)
      count: 7,
    },

    modeStyle: {             // per transportmodus
      ship:     { dash: false, label: "scheepvaart" },
      air:      { dash: false, label: "luchtvracht" },   // great-circle-boog (goud); zie flows.js
      pipeline: { dash: true,  label: "pijpleiding" },
      rail:     { dash: true,  label: "spoor" },
      road:     { dash: true,  label: "over land" },
    },

    // KETENSTAP: bepaalt de kleur (zie stageColorOf in util.js).
    // Erts dof en donker, raffinaat de grondstofkleur, product licht.
    stageStyle: {
      erts:      { label: "erts / concentraat" },
      raffinaat: { label: "raffinaat / chemie" },
      product:   { label: "eindproduct" },
    },

    // ZOOM-BANDEN: bij inzoomen worden buizen dunner en bogen platter,
    // zodat je ingezoomd routes ziet in plaats van dikke slierten in de lucht.
    // (De geometrie wordt opnieuw gebouwd zodra je een band-grens passeert.)
    zoomBands: {
      thresholds: [6.4, 4.4],          // camera-z grenzen ver / midden / dichtbij
      far:  { width: 1.00, lift: 1.00 },
      mid:  { width: 0.55, lift: 0.55 },
      near: { width: 0.30, lift: 0.26 },
    },
  },

  // -------------------------------------------------------------------- TIJD
  // "Afspelen": schepen als lichtjes met een spoor, over een periode van
  // enkele maanden. Alleen zinvol in de route-weergave (in hemelsbreed varen
  // er geen schepen — dat zijn luchtlijnen).
  //
  // Frequentie en reisduur zijn GÉÉN willekeurige animatie maar volgen uit de data:
  //   afvaarten/jaar = volume (kt LCE) / ktPerShipment
  //   reisduur       = routelengte (km) / shipSpeedKmPerDay
  // Zo zie je dat Greenbushes → China ruim twee weken varen is, en dat er
  // ongeveer elke twee weken een schip vertrekt.
  time: {
    monthsSpan: 6,           // lengte van de tijdlijn
    secondsPerMonth: 5,      // afspeelsnelheid: 1 maand in 5 seconden
    speeds: [0.5, 1, 2, 4],  // vermenigvuldigers in de UI

    shipSpeedKmPerDay: 620,  // ≈ 14 knopen, snelheid van een bulkcarrier
    ktPerShipment: 4,        // één lading ≈ 4 kt LCE (≈ 30 kt concentraat)
    maxShipsPerRoute: 8,     // veiligheidsplafond voor de drukste routes

    shipSize: 0.010,
    trailPoints: 26,         // lengte van het spoor in punten
    trailSpan: 0.10,         // hoe ver het spoor terugreikt (fractie van de route)
  },

  // -------------------------------------------------------------- ZEEROUTES
  // De atlas zoekt zelf een pad dat alleen over water loopt (A* over een
  // land/zee-raster uit geo-data.js). Daardoor buigen routes vanzelf om Java
  // en Borneo heen en varen ze dóór de zeestraten in plaats van eroverheen.
  searoute: {
    enabled: true,
    cellDeg: 0.25,        // rasterfijnheid; kleiner = nauwkeuriger, trager
    openRadiusDeg: 1.2,   // ZEE: rond elk knelpunt water forceren — anders slibben
                          // smalle straten (Lombok is ~35 km) dicht in het raster
    bridgeRadiusDeg: 0.6, // LAND: rond elke brug/tunnel land forceren, anders kan
                          // de trein niet over de Øresundbrug naar Zweden
    coastPenalty: 1.5,    // kust vermijden, maar niet koste wat kost
    simplify: 3,          // elk n-de rasterpunt gebruiken (vloeiender curve)

    // Landroutes: trein, weg en pijpleiding volgen ook een echt pad, zodat ze
    // niet dwars door de Oostzee of over de Egeiïsche Zee snijden.
    landEnabled: true,

    // Oceaanroutes zijn lang: de Stille Oceaan oversteken is ~10.000 km, en op
    // een raster van 0.25° is dat een enorme zoekruimte. Met een zuivere A*
    // liep de zoektocht tegen zijn limiet aan, gaf op, en viel de route terug
    // op een rechte lijn — dwars over de Salomonseilanden.
    //   heuristicWeight > 1 = gretiger zoeken: iets minder perfect pad, maar
    //   vele malen sneller. Op open zee scheelt dat niets in het resultaat.
    heuristicWeight: 1.35,
    maxExpansions: 1500000,
  },

  // ------------------------------------------------------------------ FOCUS
  // Klik op een locatie, stroom of knelpunt -> al het niet-betrokken werk
  // wordt gedimd. Klik op lege ruimte om te resetten.
  focus: {
    flowDim: 0.05,
    particleDim: 0.04,
    markerDim: 0.14,
    labelHideDimmed: true,
  },

  // -------------------------------------------------------------------- SCENE
  scene: {
    background: 0x070b14,
    stars: 1800,
    atmosphereColor: 0x3a7ca5,
    atmosphereOpacity: 0.13,
    ambientLight: 0.85,
    sunLight: 1.0,
  },
};
