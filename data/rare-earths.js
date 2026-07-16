// ============================================================================
// ZELDZAME AARDMETALEN — MAGNEET-REE (NdPr + Dy/Tb) — volledig uitgewerkte module.
// Peiljaar ±2024. Cijfers indicatief/afgerond, o.b.v. USGS MCS 2025, Adamas
// Intelligence, IEA, en bedrijfsrapportages (Lynas, MP Materials, Neo/Silmet,
// Shin-Etsu, VAC). Eenheid overal: kt magneet-REO/jaar — ALLEEN de NdPr- + Dy/Tb-
// oxide-inhoud (niet de totale REO), zodat de hele keten optelbaar blijft.
// Zie ../design/zeldzame-aardmetalen.md voor de brief.
//
// FRAMING-KEUZE (optie 2): niet "alle 17 elementen" (dan verdrinkt het verhaal in
// de La/Ce-bulk voor glas en katalysatoren), maar de MAGNEET-REE — het handjevol
// dat de geopolitiek draagt: NdPr (licht, de massa van de magneetvraag) plus de
// zware toevoegingen Dy/Tb (maken de magneet hittebestendig). Winning blijft
// eerlijk het GEMENGDE erts — je haalt Nd niet los uit de grond; dát is de crux.
//
// DE VORM VAN REE (nóg extremer dan lithium/koper):
//   - MIJNBOUW breed verspreid over álle continenten — winning is NIET de knijp.
//   - SCHEIDING knijpt samen in ZUID-CHINA (~85-90%, Ganzhou/Sichuan/Baotou):
//     zelfs Amerikaans erts vaart hierheen. Dít is de REE-"aha".
//   - NdFeB-MAGNEETFABRICAGE ~90%+ in China — de echte geopolitieke hefboom
//     (China-exportvergunningen op magneten + zware REE, 2025).
//
// DRIE DINGEN DIE LITHIUM/KOPER NIET HEBBEN:
//   1. Een ZWARE-REE-LANDSTROOM over de grens Myanmar->China (Kachin/Ruili): Dy/Tb
//      komt bijna 100% uit Chinese + Kachin-ionklei. Nieuw grens-knelpunt
//      (grens-ruili in _chokepoints.js, analoog aan Kasumbalesa voor kobalt).
//   2. De emblematische MOUNTAIN-PASS-RONDREIS: de VS delft, China scheidt, het
//      oxide komt terug — "we graven het, maar kunnen het niet scheiden".
//   3. De NdFeB-MAGNEET-FLESSENHALS downstream — de eindstap en de echte hefboom.
//
// STAGES (op de 3 bestaande gemapt):
//   erts       = winning -> gemengd concentraat / ionklei. Dof/donker.
//   raffinaat  = SCHEIDING -> NdPr/Dy-oxide + metaal. Volle REE-kleur (de knijp).
//   product    = NdFeB-MAGNEET -> EV/wind/defensie. Licht.
//
// TRANSPORT is schip + land (hergebruikt de zee-A*/land-A*-routes en de scheeps-
// voyages). GEEN nieuwe render-modus (dat was het goud-stuk).
//
// RECYCLING (type "recycler" + flow/node `layer:"recycle"`) is een OPTIONELE toggle
// die standaard UIT staat — het REE-equivalent van de goud-CB-/koper-beursvoorraden-
// laag. Nuance: recycling is nu <5% van het aanbod, wel strategisch (magneet->magneet).
// ============================================================================

REGISTER({
  id: "rare-earths",
  name: "Zeldzame aardmetalen (magneet-REE)",
  symbol: "NdPr",
  color: "#C9A227",
  flowColor: "#E4C24A",
  detail: "uitgewerkt",
  unit: "kt magneet-REO/jaar (NdPr + Dy/Tb, indicatief)",
  recycleHint: "Magneetschroot terug naar scheiding/magneet tonen (nog <5% van het aanbod)",
  blurb: "De magneetmetalen NdPr + Dy/Tb voor EV-motoren, windturbines en defensie. " +
    "Winning is breed verspreid over álle continenten — maar China scheidt ~85-90% " +
    "van het gemengde erts (Ganzhou/Sichuan/Baotou) en maakt ~90%+ van de NdFeB-" +
    "magneten. Zwaar Dy/Tb komt bijna 100% uit Chinese + Myanmarese ionklei; zelfs " +
    "Amerikaans erts vaart naar China en komt terug.",

  nodes: [
    // ================================================================== MIJNEN
    // Winning -> gemengd concentraat / ionklei. `share` = MAGNEET-relevante fractie
    // (NdPr/Dy-inhoud), niet totale REO: Dy/Tb-rijke ionklei weegt zwaarder dan zijn
    // tonnage, La/Ce-rijk erts lichter. Breed verspreid = winning is niet de knijp.

    // --- China: NdPr (Bayan Obo) + de zware Dy/Tb-ionklei (Zuid-China) -------
    { id: "ree-bayanobo", type: "mine", name: "Bayan Obo", country: "China",
      lat: 41.77, lon: 109.98, share: 40, tier: 1, operator: "China Northern REE",
      status: "actief", capacity: "grootste REE-mijn ter wereld",
      note: "Binnen-Mongolië; bastnäsiet/monaziet, de LICHTE NdPr-bron. Bijproduct van de ijzerertswinning — voedt de Baotou-scheiding vlak ernaast." },
    { id: "ree-southclay", type: "mine", name: "Zuid-China ionklei", country: "China",
      lat: 24.95, lon: 114.80, share: 16, tier: 1, operator: "China Rare Earth Group",
      status: "actief", capacity: "hart van de zware-REE-winning",
      note: "Ionadsorptie-klei in Jiangxi (Ganzhou/Longnan), Guangdong en Fujian — DE Dy/Tb-bron. Lage tonnage, maar magneet-cruciaal: zonder Dy/Tb geen hittebestendige magneet." },

    // --- Myanmar: de zware-REE-landstroom over de grens ---------------------
    { id: "ree-kachin", type: "mine", name: "Kachin (Pangwa/Chipwi)", country: "Myanmar",
      lat: 25.90, lon: 98.30, share: 12, tier: 1, operator: "grensmilitie / informeel",
      status: "actief", capacity: "≈ helft van China's zware-REE-voeding",
      note: "Ionadsorptie-klei in Noord-Myanmar (Kachin). Dy/Tb steekt bijna volledig de grens over naar de Chinese scheiding — LANDLOCKED, via de grenspost Ruili. Milieuschade en conflictfinanciering maken dit de omstreden onderbuik van de magneetketen." },

    // --- VS + Australië: NdPr buiten China (de dunne niet-Chinese poot) ------
    { id: "ree-mountainpass", type: "mine", name: "Mountain Pass", country: "VS",
      lat: 35.48, lon: -115.53, share: 8, tier: 2, operator: "MP Materials",
      status: "actief", capacity: "≈ 45 kt REO/j",
      note: "Californië; bastnäsiet, de enige Amerikaanse REE-mijn. Concentraat voer jarenlang naar China voor de scheiding — de emblematische rondreis. MP bouwt nu eigen scheiding + Fort Worth-magneten (mine-to-magnet)." },
    { id: "ree-mountweld", type: "mine", name: "Mount Weld", country: "Australië",
      lat: -28.98, lon: 122.44, share: 8, tier: 2, operator: "Lynas Rare Earths",
      status: "actief", capacity: "≈ 22 kt REO/j",
      note: "West-Australië (Laverton); monaziet/bastnäsiet, NdPr. Voedt Lynas' scheidingsfabriek in Kuantan (Maleisië) — de enige grote scheiding buiten China. Export via Fremantle." },

    // --- Overige NdPr-relevante winning (breed verspreid, deels marker-only) -
    { id: "ree-vietnam", type: "mine", name: "Lai Chau / Dong Pao", country: "Vietnam",
      lat: 22.30, lon: 103.10, share: 3, tier: 3, operator: "diverse",
      status: "actief", note: "Noord-Vietnam; erts steekt over land de grens over naar de Chinese scheiding (Yunnan)." },
    { id: "ree-brazil", type: "mine", name: "Araxá", country: "Brazilië",
      lat: -19.60, lon: -46.90, share: 2, tier: 3, operator: "diverse",
      status: "actief", note: "Grote reserves (Minas Gerais); nog beperkt magneet-relevante productie." },
    { id: "ree-india", type: "mine", name: "Kustmonaziet", country: "India",
      lat: 17.00, lon: 82.00, share: 2, tier: 3, operator: "IREL (staat)",
      status: "actief", note: "Kustzand-monaziet (Kerala/Odisha), staatsmonopolie; binnenlands verwerkt, klein op magneet-schaal." },
    { id: "ree-russia", type: "mine", name: "Lovozero (Kola)", country: "Rusland",
      lat: 67.80, lon: 34.60, share: 2, tier: 3, operator: "diverse",
      status: "actief", note: "Kola-schiereiland; historisch geleverd aan Silmet (Estland) — nu politiek beladen." },
    { id: "ree-norway", type: "mine", name: "Fen-complex", country: "Noorwegen",
      lat: 59.28, lon: 9.25, share: 1, tier: 3, operator: "REN / staat",
      status: "actief", note: "Groot Europees REE-project (Telemark); zou de EU-scheiding kunnen voeden." },

    // --- Projecten (potentieel): de ambitie om de lus buiten China te sluiten
    { id: "ree-greenland", type: "mine", name: "Kvanefjeld/Tanbreez", country: "Groenland",
      lat: 60.90, lon: -46.00, tier: 3, operator: "diverse", status: "project",
      potential: "grote NdPr-reserves", note: "Enorme reserves, maar vergunning omstreden (uranium-bijproduct). Symbool van de Westerse zoektocht naar niet-Chinese winning." },
    { id: "ree-sweden", type: "mine", name: "Per Geijer (Kiruna)", country: "Zweden",
      lat: 67.85, lon: 20.20, tier: 3, operator: "LKAB", status: "project",
      potential: "grootste bekende REE-vondst EU", note: "LKAB-vondst bij Kiruna; zou (met Silmet) de dunne EU-scheidingsketen kunnen voeden." },
    { id: "ree-malawi", type: "mine", name: "Songwe Hill / Ngualla", country: "Malawi",
      lat: -15.50, lon: 35.30, tier: 3, operator: "Mkango / Peak", status: "project",
      potential: "Afrikaanse NdPr-projecten", note: "Oost-Afrikaanse magneet-REE-projecten (Malawi/Tanzania) die op de Westerse markt mikken." },

    // ================================== SCHEIDING / RAFFINAGE (stage raffinaat)
    // HIER KNIJPT HET SAMEN: Zuid-China ~85-90% van de scheiding. De waarde-
    // toevoegende stap waar de wereld op vastloopt — de REE-Ticino.
    { id: "ree-ref-ganzhou", type: "refinery", name: "Ganzhou (Jiangxi)", country: "China",
      lat: 25.85, lon: 114.93, tier: 1, operator: "China Rare Earth Group",
      capacity: "wereldcentrum zware-REE-scheiding",
      note: "DE FLESSENHALS voor Dy/Tb. Vrijwel alle zware REE ter wereld — Chinees, Myanmarees én Amerikaans concentraat — wordt hier gescheiden. Geen zeestraat, wel een keiharde institutionele knijp." },
    { id: "ree-ref-baotou", type: "refinery", name: "Baotou", country: "China",
      lat: 40.65, lon: 109.82, tier: 1, operator: "China Northern REE",
      note: "Binnen-Mongolië; NdPr-scheiding gekoppeld aan de Bayan Obo-mijn, plus een groot magneetcluster. Het lichte-REE-hart." },
    { id: "ree-ref-sichuan", type: "refinery", name: "Sichuan (Leshan/Mianning)", country: "China",
      lat: 29.00, lon: 103.00, tier: 2, operator: "diverse",
      note: "Derde Chinese scheidingspool (NdPr), gevoed door binnenlands bastnäsiet uit Sichuan en Bayan Obo-erts." },
    { id: "ree-ref-kuantan", type: "refinery", name: "Lynas LAMP (Kuantan)", country: "Maleisië",
      lat: 3.98, lon: 103.42, tier: 1, operator: "Lynas", coastal: true,
      note: "De grootste scheidingsfabriek BUITEN China (Lynas Advanced Materials Plant). Verwerkt Mount Weld-concentraat tot NdPr-oxide — het enige echte niet-Chinese alternatief. Aan de kade in Kuantan." },
    { id: "ree-ref-silmet", type: "refinery", name: "Silmet (Sillamäe)", country: "Estland",
      lat: 59.42, lon: 27.74, tier: 2, operator: "Neo Performance Materials", coastal: true,
      note: "De enige werkende REE-scheiding in de EU (Neo), aan de Oostzee. Klein, maar strategisch: de kiem van een Europese magneetketen." },
    { id: "ree-ref-larochelle", type: "refinery", name: "La Rochelle (Solvay)", country: "Frankrijk",
      lat: 46.16, lon: -1.15, tier: 2, operator: "Solvay", coastal: true,
      note: "Historisch REE-raffinagecomplex aan de Atlantische kust; heropgestart voor magneet-REE (NdPr) om de EU-keten te voeden." },
    { id: "ree-ref-mp", type: "refinery", name: "Mountain Pass (on-site scheiding)", country: "VS",
      lat: 35.25, lon: -115.30, tier: 3, operator: "MP Materials", status: "actief",
      note: "MP scheidt sinds ~2023 een deel van zijn eigen concentraat ter plekke — de eerste stap om de rondreis naar China te doorbreken (mine-to-magnet)." },

    // ===================================== NdFeB-MAGNEETFABRICAGE (stage product)
    // De downstream-flessenhals: ~90%+ van de wereld-NdFeB in China. De echte
    // geopolitieke hefboom (exportvergunningen 2025). Ook niet-Chinese makers
    // (Shin-Etsu, VAC) kopen hun scheiding vaak uit China.
    { id: "ree-mag-ningbo", type: "refinery", name: "Ningbo (magneetcluster)", country: "China",
      lat: 29.87, lon: 121.55, tier: 1, operator: "Yunsheng / Zhenghai / Ningbo Innuovo",
      coastal: true, note: "'s Werelds grootste NdFeB-magneetcluster (Zhejiang, aan zee). Zet Chinees + geïmporteerd oxide om in de magneten voor EV-motoren en windturbines wereldwijd." },
    { id: "ree-mag-baotou", type: "refinery", name: "Baotou (magneten)", country: "China",
      lat: 40.35, lon: 110.20, tier: 2, operator: "diverse",
      note: "Magneetproductie naast de Baotou-scheiding — de geïntegreerde noordelijke NdPr-loop (mijn -> scheiding -> magneet in één regio)." },
    { id: "ree-mag-ganzhou", type: "refinery", name: "Ganzhou (JL MAG e.a.)", country: "China",
      lat: 25.55, lon: 115.25, tier: 2, operator: "JL MAG Rare-Earth",
      note: "Magneetfabrieken bij de zware-REE-scheiding — hier komen Dy/Tb en NdPr samen tot hoogwaardige, hittebestendige magneten." },
    { id: "ree-mag-japan", type: "refinery", name: "Japan (Shin-Etsu/Proterial/TDK)", country: "Japan",
      lat: 34.75, lon: 137.40, tier: 2, operator: "Shin-Etsu / Proterial / TDK",
      coastal: true, note: "De belangrijkste niet-Chinese magneetmakers — hoogwaardig, maar grotendeels op Chinese en Maleisische scheiding. Japan de-riskte vroeg (na de 2010-embargoschok)." },
    { id: "ree-mag-vac", type: "refinery", name: "Vacuumschmelze (Hanau)", country: "Duitsland",
      lat: 50.13, lon: 8.92, tier: 2, operator: "Vacuumschmelze (VAC)",
      note: "Europa's magneetmaker. Bouwt met e-VAC ook een Amerikaanse fabriek — maar hangt vooralsnog aan Chinese/Estse/Franse scheiding." },
    { id: "ree-mag-fortworth", type: "refinery", name: "MP Fort Worth (Texas)", country: "VS",
      lat: 32.75, lon: -97.33, tier: 3, operator: "MP Materials", status: "project",
      potential: "opstartende NdFeB-magneetfabriek", note: "MP's magneetfabriek in Texas (levert o.a. aan GM) — de Amerikaanse poging om de keten binnenlands te sluiten. Nog klein t.o.v. China." },

    // =================================================== HAVENS & CORRIDORS
    { id: "ree-port-longbeach", type: "port", name: "Long Beach", country: "VS",
      lat: 33.75, lon: -118.20, tier: 2,
      note: "Californische uitvoerhaven voor Mountain Pass-concentraat — hier begint de reis over de Stille Oceaan naar de Chinese scheiding." },
    { id: "ree-port-fremantle", type: "port", name: "Fremantle", country: "Australië",
      lat: -32.05, lon: 115.74, tier: 3,
      note: "West-Australische haven; Mount Weld-concentraat scheept hier in richting Lynas Maleisië, via de Indonesische straten." },
    { id: "ree-port-shanghai", type: "port", name: "Shanghai (Yangshan)", country: "China",
      lat: 30.62, lon: 122.07, tier: 2,
      note: "Invoerpoort voor geïmporteerd concentraat (o.a. Mountain Pass); vandaar per spoor het binnenland in naar Ganzhou/Sichuan." },
    { id: "ree-port-tianjin", type: "port", name: "Tianjin", country: "China",
      lat: 38.98, lon: 117.75, tier: 3,
      note: "Noordelijke uitvoerhaven voor de Baotou-regio (oxide + magneten richting Europa)." },
    { id: "ree-port-rotterdam", type: "port", name: "Rotterdam", country: "Nederland",
      lat: 51.95, lon: 4.14, tier: 3,
      note: "Aanlandingshaven voor de Europese magneetketen (VAC); laatste stuk over land naar Hanau." },

    // ============================================================= MARKT / CONSUMPTIE
    // Magneet-eindgebruik (stage product). Géén La/Ce-bulk (glas/katalysator) — dat
    // valt bewust buiten deze magneet-framing.
    { id: "ree-mkt-china-ev", type: "market", name: "China (EV-motoren · elektronica)", country: "China",
      lat: 31.00, lon: 120.50, tier: 1,
      note: "Veruit de grootste magneetvraag: tractiemotoren voor EV's, e-fietsen, airco-compressoren, robotica en elektronica." },
    { id: "ree-mkt-china-wind", type: "market", name: "China (windturbines)", country: "China",
      lat: 34.20, lon: 119.20, tier: 2, coastal: true,
      note: "Direct-drive permanentmagneet-generatoren voor de enorme Chinese wind-uitrol (offshore Jiangsu/Guangdong)." },
    { id: "ree-mkt-eu", type: "market", name: "EU (auto · offshore wind)", country: "Duitsland",
      lat: 50.50, lon: 9.00, tier: 2,
      note: "Europees zwaartepunt: EV-tractiemotoren (Duitse auto-industrie) en direct-drive generatoren voor Noordzee-windparken." },
    { id: "ree-mkt-japan", type: "market", name: "Japan (auto · robotica)", country: "Japan",
      lat: 35.40, lon: 139.60, tier: 3, coastal: true,
      note: "Hoogwaardige motoren en actuatoren (auto, robotica, elektronica) — deels op eigen magneetproductie." },
    { id: "ree-mkt-korea", type: "market", name: "Zuid-Korea (EV · elektronica)", country: "Zuid-Korea",
      lat: 35.10, lon: 129.05, tier: 3, coastal: true,
      note: "EV-motoren en elektronica (Busan/Ulsan); afhankelijk van geïmporteerde Chinese magneten." },
    { id: "ree-mkt-us", type: "market", name: "VS (defensie · EV · wind)", country: "VS",
      lat: 38.90, lon: -77.00, tier: 2,
      note: "F-35 (~400 kg REE per toestel), raketten, sonar én de opkomende EV/wind-vraag. De 2025-magneetexportbeperkingen troffen juist deze afnemer het hardst." },

    // ============================ RECYCLING (optionele toggle-laag, layer:"recycle")
    // Magneetschroot (productie-swarf ~⅓ van elke magneet + end-of-life) terug naar
    // de scheiding/magneet. `layer:"recycle"` -> alleen zichtbaar met de toggle.
    // Nuance: nu <5% van het aanbod, wél strategisch (magneet -> magneet).
    { id: "ree-rec-china", type: "recycler", name: "China (magneetschroot)", country: "China",
      lat: 28.20, lon: 118.50, tier: 3, layer: "recycle",
      note: "Veruit de grootste recyclingstroom: swarf en oude magneten terug naar de Chinese scheiding — China sluit ook de kringloop het snelst." },
    { id: "ree-rec-hypromag", type: "recycler", name: "HyProMag", country: "Verenigd Koninkrijk",
      lat: 52.45, lon: -1.93, tier: 3, layer: "recycle",
      note: "Birmingham/Duitsland: HPMS-recycling van end-of-life-magneten direct terug tot nieuwe NdFeB — een Europese magneet-tot-magneet-route." },
    { id: "ree-rec-solvay", type: "recycler", name: "Solvay (La Rochelle)", country: "Frankrijk",
      lat: 46.45, lon: -0.85, tier: 3, layer: "recycle",
      note: "Solvay recyclet magneetschroot terug in zijn La Rochelle-scheiding — de Europese lus." },
    { id: "ree-rec-mp", type: "recycler", name: "MP Materials (recycling)", country: "VS",
      lat: 32.50, lon: -97.00, tier: 3, layer: "recycle", status: "project",
      note: "MP recyclet productie-swarf uit Fort Worth terug in de eigen scheiding — de Amerikaanse kringloop in opbouw." },
  ],

  // ==========================================================================
  // STROMEN — value in kt magneet-REO/jaar (indicatief). stage bepaalt kleur/hoogte:
  // erts (concentraat/ionklei) dof -> raffinaat (NdPr/Dy-oxide) vol -> product
  // (NdFeB-magneet) licht. `via` = echte route langs havens (ree-port-*) en de
  // universele knelpunten (wp-* / grens-*). Elke ship-leg landt op een kustpunt.
  //
  //  A) CHINA — de binnenlandse lichte (NdPr) + zware (Dy/Tb) scheidingsloops
  //  B) MYANMAR — de zware-REE-landstroom over de grens (Kachin -> Ruili -> Ganzhou)
  //  C) MOUNTAIN-PASS-RONDREIS (concentraat heen over de Stille Oceaan, oxide terug)
  //  D) MOUNT WELD -> LYNAS MALEISIË (de enige scheiding buiten China)
  //  E) CHINEES OXIDE -> CHINESE MAGNETEN -> de NdFeB-waaier naar de wereld
  //  F) CHINEES OXIDE -> NIET-CHINESE MAGNEETMAKERS (Japan/VAC hangen er óók aan)
  //  G) HET DUNNE EU-DRAADJE (Zweden/Noorwegen/Rusland -> Silmet/La Rochelle -> VAC)
  //  H) RECYCLING (layer:"recycle" -> alleen met de toggle)
  // ==========================================================================
  flows: [
    // === A. CHINA — binnenlandse scheidingsloops ============================
    { from: "ree-bayanobo", to: "ree-ref-baotou", value: 22, mode: "rail", stage: "erts",
      note: "Bayan Obo -> Baotou-scheiding: de lichte NdPr-loop, binnenlands over korte afstand (mijn en scheiding liggen naast elkaar)." },
    { from: "ree-bayanobo", to: "ree-ref-sichuan", value: 6, mode: "rail", stage: "erts",
      note: "Deel van het Bayan Obo-erts -> de Sichuan-scheiding (tweede NdPr-pool)." },
    { from: "ree-southclay", to: "ree-ref-ganzhou", value: 12, mode: "road", stage: "erts",
      note: "Zuid-China ionklei -> Ganzhou: de zware Dy/Tb-scheiding, binnenlands." },
    { from: "ree-vietnam", to: "ree-ref-ganzhou", value: 3, mode: "road", stage: "erts",
      note: "Vietnamees erts steekt over land de grens over (Yunnan) naar de Chinese scheiding." },

    // === B. MYANMAR — de zware-REE-landstroom over de grens =================
    { from: "ree-kachin", to: "ree-ref-ganzhou", value: 10, mode: "road", stage: "erts",
      via: ["grens-ruili"],
      note: "Kachin-ionklei (Dy/Tb) over de grenspost RUILI naar de Ganzhou-scheiding — ~de helft van China's zware-REE-voeding. De nieuwe landflessenhals, analoog aan Kasumbalesa voor kobalt." },

    // === C. MOUNTAIN-PASS-RONDREIS (concentraat heen, oxide terug) ==========
    { from: "ree-mountainpass", to: "ree-ref-ganzhou", value: 8, mode: "ship", stage: "erts",
      via: ["ree-port-longbeach", "wp-pac-noord", "wp-taiwan", "ree-port-shanghai"],
      note: "DE RONDREIS, heen: Amerikaans concentraat vaart via Long Beach de Stille Oceaan over naar de Chinese scheiding. 'We graven het, maar kunnen het niet scheiden.'" },
    { from: "ree-ref-ganzhou", to: "ree-mag-fortworth", value: 3, mode: "ship", stage: "raffinaat",
      status: "gepland",
      via: ["ree-port-shanghai", "wp-taiwan", "wp-pac-noord", "ree-port-longbeach"],
      note: "DE RONDREIS, terug: gescheiden oxide vaart terug naar de VS (Fort Worth-magneten) — de lus die MP nu binnenlands probeert te sluiten." },
    { from: "ree-mountainpass", to: "ree-ref-mp", value: 4, mode: "road", stage: "erts",
      note: "Mountain Pass -> eigen scheiding on-site: de eerste stap om de rondreis naar China te doorbreken." },
    { from: "ree-ref-mp", to: "ree-mag-fortworth", value: 3, mode: "road", stage: "raffinaat",
      status: "gepland",
      note: "MP-oxide -> Fort Worth-magneten: de niet-Chinese mine-to-magnet-keten die de VS opbouwt." },

    // === D. MOUNT WELD -> LYNAS MALEISIË (de enige scheiding buiten China) ==
    { from: "ree-mountweld", to: "ree-ref-kuantan", value: 8, mode: "ship", stage: "erts",
      via: ["ree-port-fremantle", "wp-lombok", "wp-makassar", "wp-scs"],
      note: "Mount Weld-concentraat -> Lynas Kuantan, via Fremantle en de Indonesische straten (Lombok/Makassar). De enige echte niet-Chinese scheidingsroute." },
    { from: "ree-ref-kuantan", to: "ree-mag-japan", value: 5, mode: "ship", stage: "raffinaat",
      via: ["wp-scs", "wp-taiwan"],
      note: "Maleisisch NdPr-oxide -> de Japanse magneetmakers (Shin-Etsu): de niet-Chinese scheiding voedt de niet-Chinese magneten." },
    { from: "ree-ref-kuantan", to: "ree-mag-vac", value: 2, mode: "ship", stage: "raffinaat",
      via: ["wp-scs", "wp-singapore", "wp-malakka", "wp-aceh", "wp-bab", "wp-rode-zee", "wp-suez", "wp-gibraltar", "ree-port-rotterdam"],
      note: "Lynas-oxide -> Europa (VAC), via Malakka en Suez: het dunne niet-Chinese draadje naar de Europese magneetmaker." },

    // === E. CHINEES OXIDE -> CHINESE MAGNETEN -> de NdFeB-waaier ============
    { from: "ree-ref-ganzhou", to: "ree-mag-ningbo", value: 12, mode: "rail", stage: "raffinaat",
      note: "Dy/Tb-oxide -> het Ningbo-magneetcluster: de zware toevoeging die de magneet hittebestendig maakt." },
    { from: "ree-ref-baotou", to: "ree-mag-ningbo", value: 8, mode: "rail", stage: "raffinaat",
      note: "NdPr-oxide (Baotou) -> Ningbo." },
    { from: "ree-ref-sichuan", to: "ree-mag-ningbo", value: 6, mode: "rail", stage: "raffinaat",
      note: "Sichuan-NdPr -> Ningbo." },
    { from: "ree-ref-baotou", to: "ree-mag-baotou", value: 10, mode: "road", stage: "raffinaat",
      note: "Baotou: scheiding en magneten in één regio (de geïntegreerde noordelijke loop)." },
    { from: "ree-ref-ganzhou", to: "ree-mag-ganzhou", value: 8, mode: "road", stage: "raffinaat",
      note: "Ganzhou: zware scheiding + magneten samen — hoogwaardige hittebestendige NdFeB." },
    // De waaier: Chinese NdFeB naar élke afnemer (de geopolitieke hefboom)
    { from: "ree-mag-ningbo", to: "ree-mkt-china-ev", value: 20, mode: "road", stage: "product",
      note: "NdFeB -> Chinese EV-tractiemotoren: de grootste enkele magneetvraag ter wereld." },
    { from: "ree-mag-ningbo", to: "ree-mkt-china-wind", value: 10, mode: "road", stage: "product",
      note: "NdFeB -> direct-drive windgeneratoren voor de Chinese wind-uitrol." },
    { from: "ree-mag-baotou", to: "ree-mkt-china-ev", value: 8, mode: "rail", stage: "product",
      note: "Noordelijke magneten -> de Chinese binnenlandse vraag." },
    { from: "ree-mag-ganzhou", to: "ree-mkt-china-ev", value: 7, mode: "road", stage: "product",
      note: "Ganzhou-magneten -> Chinese motoren/elektronica." },
    { from: "ree-mag-ningbo", to: "ree-mkt-eu", value: 6, mode: "ship", stage: "product",
      via: ["wp-taiwan", "wp-scs", "wp-singapore", "wp-malakka", "wp-aceh", "wp-bab", "wp-rode-zee", "wp-suez", "wp-gibraltar", "ree-port-rotterdam"],
      note: "Chinese NdFeB -> de EU-auto-industrie, via Malakka en Suez — de exporthefboom die de 2025-vergunningen blootlegden." },
    { from: "ree-mag-ningbo", to: "ree-mkt-us", value: 5, mode: "ship", stage: "product",
      via: ["wp-taiwan", "wp-pac-noord", "ree-port-longbeach"],
      note: "Chinese NdFeB -> de VS (defensie, EV, wind), over de Stille Oceaan. Precies de afhankelijkheid die de exportbeperkingen van 2025 pijnlijk maakten." },
    { from: "ree-mag-ningbo", to: "ree-mkt-japan", value: 4, mode: "ship", stage: "product",
      via: ["wp-taiwan"],
      note: "Chinese magneten -> Japanse afnemers (bovenop de eigen Japanse productie)." },
    { from: "ree-mag-ningbo", to: "ree-mkt-korea", value: 4, mode: "ship", stage: "product",
      via: ["wp-taiwan"],
      note: "Chinese magneten -> Zuid-Korea (EV/elektronica)." },

    // === F. CHINEES OXIDE -> NIET-CHINESE MAGNEETMAKERS =====================
    { from: "ree-ref-ganzhou", to: "ree-mag-japan", value: 4, mode: "ship", stage: "raffinaat",
      via: ["ree-port-shanghai", "wp-taiwan"],
      note: "Zelfs Shin-Etsu koopt zware-REE-scheiding uit China: Ganzhou-oxide -> Japan." },
    { from: "ree-ref-baotou", to: "ree-mag-vac", value: 3, mode: "ship", stage: "raffinaat",
      via: ["ree-port-tianjin", "wp-taiwan", "wp-scs", "wp-singapore", "wp-malakka", "wp-aceh", "wp-bab", "wp-rode-zee", "wp-suez", "wp-gibraltar", "ree-port-rotterdam"],
      note: "Chinees NdPr-oxide -> VAC (Hanau): Europa's magneetmaker hangt óók aan Chinese scheiding, via Tianjin en Suez." },

    // === G. HET DUNNE EU-DRAADJE ============================================
    { from: "ree-sweden", to: "ree-ref-silmet", value: 2, mode: "rail", stage: "erts",
      status: "gepland",
      note: "Zweeds erts (Per Geijer, project) -> Silmet (Estland), over land om de Oostzee." },
    { from: "ree-russia", to: "ree-ref-silmet", value: 1, mode: "rail", stage: "erts",
      note: "Kola-erts -> Silmet: de historische (nu beladen) Russische voeding van de enige EU-scheiding." },
    { from: "ree-norway", to: "ree-ref-larochelle", value: 1, mode: "rail", stage: "erts",
      note: "Noors Fen-erts -> La Rochelle, over land (via de Deense bruggen)." },
    { from: "ree-ref-silmet", to: "ree-mag-vac", value: 2, mode: "rail", stage: "raffinaat",
      note: "Silmet-oxide -> VAC: het dunne, volledig Europese magneetdraadje." },
    { from: "ree-ref-larochelle", to: "ree-mag-vac", value: 2, mode: "rail", stage: "raffinaat",
      note: "La Rochelle (Solvay, heropstart) -> VAC (Hanau)." },
    { from: "ree-mag-vac", to: "ree-mkt-eu", value: 4, mode: "road", stage: "product",
      note: "Europese NdFeB (VAC) -> de EU-auto-industrie: de lus die Europa binnenlands probeert te sluiten." },
    { from: "ree-mag-japan", to: "ree-mkt-japan", value: 6, mode: "road", stage: "product",
      note: "Japanse magneten -> de eigen hoogwaardige motoren/robotica." },

    // === H. RECYCLING (layer:"recycle" -> alleen met de toggle) =============
    { from: "ree-rec-china", to: "ree-ref-ganzhou", value: 3, mode: "road", stage: "erts", layer: "recycle",
      note: "Chinees magneetschroot -> terug naar de scheiding: magneet -> magneet, de grootste kringloop (China sluit die het snelst)." },
    { from: "ree-rec-hypromag", to: "ree-mag-vac", value: 1, mode: "road", stage: "raffinaat", layer: "recycle",
      note: "HyProMag: end-of-life-magneten direct terug tot nieuwe NdFeB -> VAC. De Europese magneet-tot-magneet-route." },
    { from: "ree-rec-solvay", to: "ree-ref-larochelle", value: 1, mode: "road", stage: "raffinaat", layer: "recycle",
      note: "Solvay recyclet schroot terug in zijn eigen La Rochelle-scheiding." },
    { from: "ree-rec-mp", to: "ree-mag-fortworth", value: 1, mode: "road", stage: "raffinaat", layer: "recycle",
      status: "gepland",
      note: "MP recyclet Fort Worth-swarf terug in de eigen keten — de Amerikaanse kringloop in opbouw." },
  ],

  // ==========================================================================
  // SPANNINGEN — waar de magneet-REE-keten knijpt. Verwijst naar de universele
  // knelpuntenlijst (wp-* / grens-*). flows-verwijzing: "from-id>to-id".
  // ==========================================================================
  tensions: [
    { id: "ree-t-scheiding", type: "concentratie", title: "Scheiding: ~85-90% in Zuid-China",
      lat: 25.85, lon: 114.93,
      nodes: ["ree-ref-ganzhou", "ree-ref-baotou", "ree-ref-sichuan", "ree-ref-kuantan"],
      flows: ["ree-southclay>ree-ref-ganzhou", "ree-kachin>ree-ref-ganzhou",
              "ree-mountainpass>ree-ref-ganzhou", "ree-bayanobo>ree-ref-baotou"],
      metric: "winning breed verspreid · scheiding top-1 (Zuid-China) ≈ 85-90%",
      note: "De kern van REE: de kwetsbaarheid zit niet bij het graven — winning ligt op álle continenten — maar bij de SCHEIDING van het gemengde erts, en die staat voor 85-90% in Zuid-China (Ganzhou/Sichuan/Baotou). Nóg extremer dan lithium: zelfs Amerikaans concentraat vaart hierheen. Een institutionele knijp zonder zeestraat, zoals de Zwitserse goudraffinage. Kuantan (Lynas) is het enige echte alternatief." },

    { id: "ree-t-myanmar", type: "knelpunt", title: "Dy/Tb: over de grens Myanmar -> China",
      lat: 24.60, lon: 97.85,
      nodes: ["ree-kachin", "grens-ruili", "ree-southclay", "ree-ref-ganzhou"],
      flows: ["ree-kachin>ree-ref-ganzhou", "ree-southclay>ree-ref-ganzhou"],
      metric: "zwaar magneet-REE (Dy/Tb) bijna 100% China + Myanmar",
      note: "De scherpste flessenhals is niet licht NdPr maar ZWAAR Dy/Tb — en dat komt bijna uitsluitend uit ionadsorptie-klei in Zuid-China én Kachin (Myanmar). De Myanmarese helft steekt over LAND de grens over bij Ruili, richting de Ganzhou-scheiding: een landknelpunt zoals Kasumbalesa bij kobalt, met milieuschade en conflictfinanciering als beladen onderbuik. Zonder Dy/Tb geen hittebestendige magneet." },

    { id: "ree-t-magneet", type: "beleid", title: "NdFeB-magneten: ~90%+ China + exportvergunningen 2025",
      lat: 29.87, lon: 121.55,
      nodes: ["ree-mag-ningbo", "ree-mag-baotou", "ree-mag-ganzhou"],
      flows: ["ree-mag-ningbo>ree-mkt-eu", "ree-mag-ningbo>ree-mkt-us",
              "ree-mag-ningbo>ree-mkt-japan", "ree-mag-ningbo>ree-mkt-korea"],
      metric: "China maakt ~90%+ van de NdFeB-magneten — de echte hefboom",
      note: "De scheiding is de knijp, maar de downstream MAGNEETFABRICAGE (~90%+ in China) is de geopolitieke HEFBOOM. In 2025 legde China exportvergunningen op magneten en zware REE — en meteen stokte de aanvoer voor autofabrieken en defensie wereldwijd. De NdFeB-waaier vanuit Ningbo naar elke EV-, wind- en defensie-afnemer maakt die afhankelijkheid zichtbaar." },

    { id: "ree-t-mountainpass", type: "structureel", title: "Mountain Pass: delven, niet scheiden",
      lat: 35.48, lon: -115.53,
      nodes: ["ree-mountainpass", "ree-ref-ganzhou", "ree-ref-mp", "ree-mag-fortworth"],
      flows: ["ree-mountainpass>ree-ref-ganzhou", "ree-ref-ganzhou>ree-mag-fortworth",
              "ree-mountainpass>ree-ref-mp"],
      metric: "VS delft ~8% — maar scheidde jarenlang 0%: erts heen, oxide terug",
      note: "Hét symbool van de REE-afhankelijkheid: de enige Amerikaanse mijn stuurde haar concentraat de Stille Oceaan over naar China, dat het scheidde en als oxide terugstuurde. Een rondreis van duizenden kilometers voor een stap die je 'gewoon' zelf zou willen doen. MP bouwt nu on-site scheiding + Fort Worth-magneten om die lus binnenlands te sluiten — de dunne begin-barst." },

    { id: "ree-t-lynas", type: "spof", title: "Lynas: het enige niet-Chinese draadje",
      lat: 3.98, lon: 103.42,
      nodes: ["ree-mountweld", "ree-ref-kuantan", "ree-mag-japan"],
      flows: ["ree-mountweld>ree-ref-kuantan", "ree-ref-kuantan>ree-mag-japan",
              "ree-ref-kuantan>ree-mag-vac"],
      metric: "één mijn (Mount Weld) + één fabriek (Kuantan) = de niet-Chinese scheiding",
      note: "Buiten China loopt de hele niet-Chinese scheiding feitelijk via één draadje: Mount Weld (Australië) -> Lynas Maleisië -> Japan/Europa. Eén mijn en één fabriek dragen de de-risking van de Westerse wereld. Een storing, een vergunningsruzie (Kuantan lag politiek onder vuur om zijn radioactieve reststromen) of een tekort raakt meteen elk niet-Chinees magneetplan." },

    { id: "ree-t-recycle", type: "structureel", title: "Recycling: magneet -> magneet (nog <5%)",
      lat: 49.00, lon: 4.00,
      nodes: ["ree-rec-china", "ree-rec-hypromag", "ree-rec-solvay", "ree-rec-mp"],
      flows: ["ree-rec-china>ree-ref-ganzhou", "ree-rec-hypromag>ree-mag-vac",
              "ree-rec-solvay>ree-ref-larochelle"],
      metric: "nu <5% van het aanbod — wél strategisch (magneet -> magneet)",
      note: "Zet de recycling-laag aan om de kringloop te zien: productie-swarf (~⅓ van elke magneet) en end-of-life-magneten terug naar de scheiding. Nu nog klein (<5%), maar strategisch bij uitstek voor NdFeB: HPMS-technieken (HyProMag) recyclen magneet dírect tot magneet, zonder de Chinese scheiding. China sluit de kringloop het snelst; Europa en de VS proberen bij te benen." },
  ],
});
