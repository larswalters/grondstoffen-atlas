// ============================================================================
// AARDOLIE (Oil) — volledig uitgewerkte module. Peiljaar ±2023/24.
// Cijfers indicatief/afgerond, o.b.v. EIA (chokepoint-briefs), IEA Oil Market
// Report, OPEC Annual Statistical Bulletin, Energy Institute Statistical Review
// en Kpler/Vortexa-stroomdata. Eenheid overal: Mb/d (miljoen vaten per dag,
// indicatief), zodat de hele keten optelbaar blijft. Zie ../design/olie.md.
//
// DE VORM VAN OLIE (bewust ANDERS dan alle eerdere grondstoffen):
//   Lithium/koper/REE knijpen bij de RAFFINAGE (China), goud bij Zwitserland,
//   uranium bij de Russische VERRIJKING — telkens ÉÉN trechter. Olie's knijp is
//   geen enkele plek maar een HEEL NETWERK VAN ZEESTRATEN, en het is precies het
//   netwerk waar de atlas z'n knelpunten al voor heeft: HORMUZ, MALAKKA, BAB-EL-
//   MANDEB/SUEZ, BOSPORUS, PANAMA, KAAP. Olie is de grondstof die ze allemaal
//   tegelijk laat OPLICHTEN. Daarom voegt deze module GEEN nieuw knelpunt toe —
//   dat is het eigen aha: het hele net bestond al voor de olie.
//
// DE KETEN, gemapt op de 3 stages:
//   erts       = ruwe olie (crude): veld/terminal -> raffinaderij. Draagt het
//                knelpunten-verhaal. Dof/donker.
//   raffinaat  = geraffineerde producten (diesel/benzine/kerosine): export-
//                raffinaderij -> verbruiksmarkt. Volle amber.
//   product    = petrochemie (nafta -> kraker -> kunststof). Licht, hoge boog.
//
// DRIE LEVENDE VERHALEN BOVENOP DE ZEESTRATEN:
//   1. De HORMUZ-BYPASS-PIJPLEIDINGEN: Saoedi Oost-West -> Yanbu (Rode Zee) en
//      UAE Habshan -> Fujairah (Golf van Oman). Het fysieke antwoord op de Golf-
//      flessenhals: crude die Hormuz overslaat (mode "pipeline" over land).
//   2. De RUSLAND-OMLEIDING sinds 2022: Europese crude omgeleid naar India/China
//      (Primorsk/Novorossiysk over zee, ESPO-Kozmino naar de Pacific, Druzhba
//      over land). Een beleidsgedreven her-routering zoals uranium's Trans-Kaspische.
//   3. De AMERIKAANSE SCHALIE-OMMEKEER: de VS van importeur naar EXPORTEUR — een
//      omgekeerde pijl die uit Corpus Christi de Atlantische Oceaan op gaat.
//
// TRANSPORT = tanker over zee + pijpleiding over land. Hergebruikt de zee-A*/
// land-A*-routes en de scheeps-voyages. Géén nieuwe render-modus. Wel drie kleine
// navigatie-vaarpunten in _chokepoints.js (Golf van Mexico / Florida / Caribisch)
// om de Amerikaanse en Venezolaanse routes op het water te houden — alleen olie
// gebruikt ze.
// ============================================================================

REGISTER({
  id: "oil",
  name: "Aardolie",
  symbol: "Oil",
  color: "#1c1a17",
  flowColor: "#E8A838",
  detail: "uitgewerkt",
  unit: "Mb/d (indicatief)",
  blurb: "Ruwe olie: brandstof, plastics en chemie. Reserves geconcentreerd in de " +
    "Golf, Venezuela en Rusland; raffinage bij de afzetmarkten (VS, China, India, " +
    "Europa, Oost-Azië). Vrijwel elke grote stroom moet door een zeestraat — olie " +
    "is de grondstof waar het hele knelpunten-netwerk (Hormuz, Malakka, Suez, " +
    "Bosporus, Panama) voor bestaat. Bovenop de straten: de Hormuz-bypass-" +
    "pijpleidingen, de Rusland-omleiding naar India/China (2022→) en de " +
    "Amerikaanse schalie-ommekeer van importeur naar exporteur.",

  nodes: [
    // ================================================================== MIJNEN
    // Winning -> ruwe olie. `share` ≈ productie-/exportgewicht (markergrootte).
    { id: "oil-saoedi", type: "mine", name: "Ghawar / Abqaiq", country: "Saoedi-Arabië",
      lat: 25.40, lon: 49.60, share: 15, tier: 1, operator: "Saudi Aramco", status: "actief",
      note: "Grootste conventionele olieveld ter wereld (Ghawar) + de Abqaiq-verwerking. Saoedi-Arabië is de grootste crude-EXPORTEUR en de OPEC+-swingproducent die de prijs stuurt. Export via Ras Tanura (Hormuz) én — de bypass — via de Oost-West-pijpleiding naar Yanbu aan de Rode Zee." },
    { id: "oil-rusland", type: "mine", name: "West-Siberië", country: "Rusland",
      lat: 61.00, lon: 74.00, share: 12, tier: 1, operator: "Rosneft/Lukoil e.a.", status: "actief",
      note: "Samotlor e.a. Sinds de EU-boycot en het G7-prijsplafond (2022) grotendeels OMGELEID: crude die vroeger naar Europa ging, gaat nu naar India en China — via de Baltische havens, de Zwarte Zee, de ESPO-pijp naar de Pacific en de Druzhba-pijp over land." },
    { id: "oil-vs", type: "mine", name: "Permian Basin", country: "VS",
      lat: 31.90, lon: -102.30, share: 14, tier: 1, operator: "diverse (schalie)", status: "actief",
      note: "West-Texas schalie-olie. Maakte de VS van de grootste IMPORTEUR tot netto-EXPORTEUR (na het opheffen van het exportverbod in 2015). De omgekeerde pijl: crude gaat nu vanuit Corpus Christi de Atlantische Oceaan op." },
    { id: "oil-irak", type: "mine", name: "Rumaila / Basra", country: "Irak",
      lat: 30.50, lon: 47.40, share: 5, tier: 1, operator: "Basra Oil Company", status: "actief",
      note: "Zuidelijke megavelden; export via de Basra-terminals in de Perzische Golf — dus door Hormuz." },
    { id: "oil-iran", type: "mine", name: "Khuzestan", country: "Iran",
      lat: 31.30, lon: 49.30, share: 4, tier: 2, operator: "NIOC", status: "actief",
      note: "Grote zuidwestelijke velden. Onder Amerikaanse sancties gaat de export vrijwel volledig naar CHINA, met een 'schaduwvloot' tankers — nog steeds door Hormuz en Malakka." },
    { id: "oil-vae", type: "mine", name: "Abu Dhabi", country: "VAE",
      lat: 24.00, lon: 54.00, share: 4, tier: 2, operator: "ADNOC", status: "actief",
      note: "Onshore + offshore Golf-velden. De VAE heeft de belangrijkste Hormuz-bypass: de Habshan-Fujairah-pijpleiding naar de Golf van Oman, buiten de straat om." },
    { id: "oil-koeweit", type: "mine", name: "Burgan", country: "Koeweit",
      lat: 29.10, lon: 47.90, share: 3, tier: 2, operator: "KPC", status: "actief",
      note: "Enorm ondiep veld; export via Mina al-Ahmadi — door Hormuz naar Azië." },
    { id: "oil-canada", type: "mine", name: "Athabasca-oliezanden", country: "Canada",
      lat: 57.00, lon: -111.50, share: 6, tier: 1, operator: "diverse", status: "actief",
      note: "Zware olie uit Alberta. Bijna volledig LANDLOCKED richting één afnemer: per pijpleiding (Enbridge/Keystone) naar de Amerikaanse raffinaderijen. De nieuwe TMX-pijp (2024) naar Vancouver opent voor het eerst een Pacific-uitgang naar Azië." },
    { id: "oil-brazilie", type: "mine", name: "Pré-sal (Santos-bekken)", country: "Brazilië",
      lat: -25.00, lon: -42.50, share: 4, tier: 2, operator: "Petrobras", status: "actief", coastal: true,
      note: "Diepzee-offshore olie onder een zoutlaag; snelst groeiende niet-OPEC-bron. Export naar China en Europa." },
    { id: "oil-nigeria", type: "mine", name: "Nigerdelta", country: "Nigeria",
      lat: 5.30, lon: 6.00, share: 2, tier: 2, operator: "diverse", status: "actief",
      note: "Lichte zoete crude (Bonny Light) → Europa en India. De paradox: Nigeria exporteerde crude maar IMPORTEERDE benzine/diesel — tot de Dangote-raffinaderij (2024) begon te draaien." },
    { id: "oil-angola", type: "mine", name: "Cabinda (offshore)", country: "Angola",
      lat: -5.55, lon: 12.20, share: 1.5, tier: 3, operator: "diverse", status: "actief", coastal: true,
      note: "Offshore West-Afrikaanse crude; China is veruit de grootste afnemer (olie-voor-leningen)." },
    { id: "oil-kazachstan", type: "mine", name: "Tengiz / Kashagan", country: "Kazachstan",
      lat: 46.00, lon: 53.00, share: 2, tier: 2, operator: "Tengizchevroil e.a.", status: "actief",
      note: "LANDLOCKED aan de Kaspische Zee. Twee concurrerende exportroutes: de CPC-pijpleiding dwars door RUSLAND naar Novorossiysk (afhankelijk), of via de BTC-corridor naar Ceyhan (om Rusland heen)." },
    { id: "oil-noorwegen", type: "mine", name: "Noordzee", country: "Noorwegen",
      lat: 60.00, lon: 2.50, share: 2, tier: 3, operator: "Equinor", status: "actief", coastal: true,
      note: "Europa's eigen offshore crude/gas — de belangrijkste niet-Russische bron voor NW-Europa, extra belangrijk sinds 2022." },
    { id: "oil-venezuela", type: "mine", name: "Orinoco-gordel", country: "Venezuela",
      lat: 9.00, lon: -63.50, share: 1, tier: 2, operator: "PDVSA", status: "actief",
      note: "GROOTSTE bewezen reserves ter wereld — maar de productie is ingestort (sancties, wanbeheer). De reserves-vs-productie-paradox: een dikke reservestip met een dun stroompijltje. Zware crude → de VS-Golfkust en China." },

    // ============================================== EXPORT-TERMINALS / HAVENS
    { id: "oil-term-rastanura", type: "port", name: "Ras Tanura", country: "Saoedi-Arabië",
      lat: 26.65, lon: 50.16, tier: 1,
      note: "Grootste crude-exportterminal ter wereld, aan de Perzische Golf — alles hier vaart door Hormuz." },
    { id: "oil-term-yanbu", type: "port", name: "Yanbu (Rode Zee)", country: "Saoedi-Arabië",
      lat: 24.09, lon: 38.06, tier: 2,
      note: "Terminus van de Oost-West-pijpleiding (Petroline): Saoedische crude die dwars door het schiereiland naar de Rode Zee wordt gepompt om HORMUZ te vermijden. Vandaar via Suez naar Europa." },
    { id: "oil-term-fujairah", type: "port", name: "Fujairah", country: "VAE",
      lat: 25.12, lon: 56.33, tier: 1,
      note: "Terminus van de Habshan-Fujairah-pijpleiding, aan de GOLF VAN OMAN — buiten de Straat van Hormuz. De belangrijkste fysieke Hormuz-bypass + 's werelds tweede bunkerhaven." },
    { id: "oil-term-jebeldhanna", type: "port", name: "Jebel Dhanna", country: "VAE",
      lat: 24.18, lon: 52.61, tier: 3,
      note: "De reguliere UAE-crude-exportterminal aan de Golf — voor het volume dat wél door Hormuz gaat." },
    { id: "oil-term-imam", type: "port", name: "Bandar-e Emam", country: "Iran",
      lat: 30.43, lon: 49.08, tier: 3,
      note: "Iraanse export-terminal aan de kop van de Golf; het startpunt van de sanctie-tankers naar China." },
    { id: "oil-term-basra", type: "port", name: "Al-Faw / Basra", country: "Irak",
      lat: 29.98, lon: 48.47, tier: 2,
      note: "De Iraakse olieterminals bij de kop van de Perzische Golf." },
    { id: "oil-term-kuwait", type: "port", name: "Mina al-Ahmadi", country: "Koeweit",
      lat: 29.05, lon: 48.20, tier: 3,
      note: "Koeweits belangrijkste crude-exporthaven aan de Golf." },
    { id: "oil-term-primorsk", type: "port", name: "Primorsk", country: "Rusland",
      lat: 60.34, lon: 28.61, tier: 1,
      note: "Russische crude-exporthaven aan de Baltische Zee (eindpunt van de Baltische Pijpleiding). Sinds 2022 het vertrekpunt van de lange omweg om Europa heen naar India." },
    { id: "oil-term-novoros", type: "port", name: "Novorossiysk", country: "Rusland",
      lat: 44.72, lon: 37.80, tier: 1,
      note: "Zwarte-Zeehaven: uitvoer van Russische én Kazachse (CPC) crude. Alles hier moet door de Bosporus en de Dardanellen." },
    { id: "oil-term-kozmino", type: "port", name: "Kozmino (ESPO)", country: "Rusland",
      lat: 42.72, lon: 133.10, tier: 1,
      note: "Pacific-terminus van de ESPO-pijpleiding. De korte, directe uitgang van Russische crude naar China, Japan en (sinds 2022) India — zonder westelijke zeestraten." },
    { id: "oil-term-ceyhan", type: "port", name: "Ceyhan", country: "Turkije",
      lat: 36.87, lon: 35.93, tier: 2,
      note: "Middellandse-Zeeterminus van de BTC-pijpleiding (Azeri/Kazachse crude) én van Kirkuk — omzeilt zowel Hormuz als de Bosporus." },
    { id: "oil-term-corpus", type: "port", name: "Corpus Christi", country: "VS",
      lat: 27.80, lon: -97.40, tier: 1,
      note: "De belangrijkste crude-EXPORTterminal van de VS (Permian-schalie). Het zichtbare bewijs van de ommekeer: hier vertrekt Amerikaanse olie de wereld op." },
    { id: "oil-term-bonny", type: "port", name: "Bonny", country: "Nigeria",
      lat: 4.42, lon: 7.16, tier: 3,
      note: "West-Afrikaanse crude-uitgang (Bonny Light) richting Europa en India." },
    { id: "oil-term-jose", type: "port", name: "José", country: "Venezuela",
      lat: 10.08, lon: -64.68, tier: 3,
      note: "Venezuela's belangrijkste crude-exportterminal aan het Caribisch gebied." },

    // ============================================================ RAFFINADERIJEN
    // Kust-raffinaderijen -> `coastal: true` zodat de tanker tot de kade vaart.
    { id: "oil-ref-jamnagar", type: "refinery", name: "Jamnagar (Reliance)", country: "India",
      lat: 22.35, lon: 69.85, tier: 1, coastal: true, operator: "Reliance",
      note: "Grootste raffinaderij ter wereld, export-georiënteerd. De grootste afnemer van de omgeleide Russische crude sinds 2022 — en een grote product-exporteur (diesel naar Europa en Afrika)." },
    { id: "oil-ref-golfkust", type: "refinery", name: "Golfkust (Houston/Port Arthur)", country: "VS",
      lat: 29.75, lon: -93.90, tier: 1, coastal: true,
      note: "Grootste raffinagecluster ter wereld, gebouwd voor zware crude (Venezuela/Canada) — en tegelijk een grote product-exporteur naar Latijns-Amerika en Europa." },
    { id: "oil-ref-rotterdam", type: "refinery", name: "Rotterdam/Pernis (ARA)", country: "Nederland",
      lat: 51.90, lon: 4.10, tier: 1, coastal: true,
      note: "Europa's raffinage- en handelshub (Amsterdam-Rotterdam-Antwerpen). Sinds 2022 op zoek naar niet-Russische crude: meer Golf, VS, West-Afrika en Noorwegen." },
    { id: "oil-ref-singapore", type: "refinery", name: "Jurong", country: "Singapore",
      lat: 1.26, lon: 103.70, tier: 1, coastal: true,
      note: "Aziatisch raffinage-, opslag- en handelsknooppunt — pal aan de Straat van Malakka/Singapore." },
    { id: "oil-ref-ulsan", type: "refinery", name: "Ulsan", country: "Zuid-Korea",
      lat: 35.50, lon: 129.36, tier: 2, coastal: true,
      note: "Grote Zuid-Koreaanse export-raffinaderij (SK/S-Oil): raffineert Golf-crude en verscheept product door heel Azië." },
    { id: "oil-ref-china", type: "refinery", name: "Zhoushan / Oostkust", country: "China",
      lat: 30.00, lon: 122.00, tier: 1, coastal: true,
      note: "China's snelgroeiende raffinage-cluster (Zhoushan/Dalian e.a.) — inmiddels de op één na grootste raffinagenatie, en de grootste importeur van crude ter wereld." },
    { id: "oil-ref-japan", type: "refinery", name: "Chiba (Tokiobaai)", country: "Japan",
      lat: 35.50, lon: 140.10, tier: 2, coastal: true,
      note: "Grote Japanse importraffinage; vrijwel alle crude komt uit de Golf, door Hormuz en Malakka." },
    { id: "oil-ref-jubail", type: "refinery", name: "Jubail (SATORP)", country: "Saoedi-Arabië",
      lat: 27.00, lon: 49.66, tier: 3, coastal: true,
      note: "Saoedische export-raffinaderij aan de Golf: crude wordt hier al tot product verwerkt vóór de export." },
    { id: "oil-ref-ruwais", type: "refinery", name: "Ruwais (ADNOC)", country: "VAE",
      lat: 24.11, lon: 52.73, tier: 3, coastal: true,
      note: "Een van de grootste raffinaderijen ter wereld; UAE-product-export vanaf de Golf." },

    // ============================================================ VERBRUIKSMARKTEN
    { id: "oil-mkt-europa", type: "market", name: "NW-Europa (Wilhelmshaven)", country: "Duitsland",
      lat: 53.60, lon: 8.08, tier: 2, coastal: true,
      note: "Duitslands crude/product-importpoort. Importeert diesel uit India, de Golf en de VS — het gat dat de weggevallen Russische leveringen sinds 2022 achterlieten." },
    { id: "oil-mkt-wafrika", type: "market", name: "West-Afrika (Lagos)", country: "Nigeria",
      lat: 6.45, lon: 3.40, tier: 3, coastal: true,
      note: "De raffinage-paradox: een regio die crude EXPORTEERT maar jarenlang benzine en diesel moest IMPORTEREN (uit Europa en India) omdat de eigen raffinage stillag." },
    { id: "oil-mkt-latam", type: "market", name: "Latijns-Amerika (Brazilië)", country: "Brazilië",
      lat: -23.00, lon: -43.20, tier: 3, coastal: true,
      note: "Grote importeur van benzine en diesel uit de Amerikaanse Golfkust — ondanks eigen crude-productie." },
    { id: "oil-mkt-oostafrika", type: "market", name: "Oost-Afrika (Mombasa)", country: "Kenia",
      lat: -4.05, lon: 39.67, tier: 3, coastal: true,
      note: "Product-importeur uit de Golf en India; de aanvoerpoort voor Oost-Afrika." },

    // ============================================================ PETROCHEMIE
    // stage `product`: nafta/ethaan -> kraker -> kunststof. De lichte, hoge boog.
    { id: "oil-pchem-jubail", type: "market", name: "Jubail (SABIC)", country: "Saoedi-Arabië",
      lat: 27.30, lon: 49.55, tier: 3, coastal: true,
      note: "Een van 's werelds grootste petrochemieclusters: goedkope nafta/ethaan → krakers → kunststof, geëxporteerd naar de hele wereld." },
    { id: "oil-pchem-antwerpen", type: "market", name: "Antwerpen", country: "België",
      lat: 51.25, lon: 4.30, tier: 3, coastal: true,
      note: "Europa's grootste petrochemiecluster, geïntegreerd met de ARA-raffinage." },
    { id: "oil-pchem-yeosu", type: "market", name: "Yeosu", country: "Zuid-Korea",
      lat: 34.76, lon: 127.66, tier: 3, coastal: true,
      note: "Zuid-Koreaans petrochemie-exportcluster (kunststof naar heel Azië)." },
    { id: "oil-pchem-ningbo", type: "market", name: "Ningbo", country: "China",
      lat: 29.87, lon: 121.55, tier: 3, coastal: true,
      note: "Chinese kraker-nieuwbouw: China bouwt petrochemie bij om zelfvoorzienend te worden in kunststof (en importeert daarvoor juist méér crude)." },
  ],

  // ==========================================================================
  // STROMEN — value in Mb/d (indicatief). stage: erts (crude, dof) -> raffinaat
  // (product, amber) -> product (petrochemie, licht). `via` = echte route langs
  // export-terminals (oil-term-*), raffinaderijen en knelpunten (wp-*).
  //
  //  A) GOLF -> AZIË / EUROPA (de dikste bundel — Hormuz + Malakka)
  //  B) HORMUZ-BYPASS-PIJPLEIDINGEN (Yanbu, Fujairah)
  //  C) RUSLAND-OMLEIDING (Primorsk/Kozmino/Novorossiysk/Druzhba, 2022→)
  //  D) KAZACHSTAN (CPC door Rusland vs BTC-bypass)
  //  E) AMERIKA'S (VS-schalie-export + Canada-pijp + Venezuela-paradox)
  //  F) ATLANTISCH BEKKEN (Nigeria/Angola/Brazilië/Noorwegen)
  //  G) PRODUCT-TRADE (raffinaat: diesel/benzine)
  //  H) PETROCHEMIE (product: kunststof)
  // ==========================================================================
  flows: [
    // === A. GOLF -> AZIË / EUROPA (crude) ===================================
    { from: "oil-saoedi", to: "oil-ref-china", value: 1.8, mode: "ship", stage: "erts",
      via: ["oil-term-rastanura", "wp-hormuz", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Saoedische crude → China: Ras Tanura, door HORMUZ, dan MALAKKA — de dikste twee-knelpunten-bundel van de wereld." },
    { from: "oil-saoedi", to: "oil-ref-jamnagar", value: 0.8, mode: "ship", stage: "erts",
      via: ["oil-term-rastanura", "wp-hormuz"],
      note: "Saoedi → India: door Hormuz, dan recht over de Arabische Zee naar Jamnagar (geen Malakka nodig)." },
    { from: "oil-saoedi", to: "oil-ref-japan", value: 1.0, mode: "ship", stage: "erts",
      via: ["oil-term-rastanura", "wp-hormuz", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Saoedi → Japan: de lange levenslijn van een land dat vrijwel al z'n olie uit de Golf haalt." },
    { from: "oil-saoedi", to: "oil-ref-singapore", value: 0.7, mode: "ship", stage: "erts",
      via: ["oil-term-rastanura", "wp-hormuz", "wp-aceh", "wp-malakka", "wp-singapore"],
      note: "Saoedi → Singapore: crude voor de Aziatische raffinage-/handelshub, pal aan Malakka." },
    { from: "oil-saoedi", to: "oil-ref-rotterdam", value: 0.5, mode: "ship", stage: "erts",
      via: ["oil-term-rastanura", "wp-hormuz", "wp-bab", "wp-rode-zee", "wp-suez", "wp-gibraltar"],
      note: "Saoedi → Europa: door Hormuz, Bab-el-Mandeb, Suez en Gibraltar — de volledige zeestraten-ketting." },
    { from: "oil-irak", to: "oil-ref-jamnagar", value: 1.0, mode: "ship", stage: "erts",
      via: ["oil-term-basra", "wp-hormuz"],
      note: "Iraakse crude → India: Basra-terminals, door Hormuz. India en China zijn Iraks grootste afnemers." },
    { from: "oil-irak", to: "oil-ref-china", value: 1.2, mode: "ship", stage: "erts",
      via: ["oil-term-basra", "wp-hormuz", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Iraakse crude → China, dezelfde Hormuz-Malakka-bundel." },
    { from: "oil-iran", to: "oil-ref-china", value: 1.3, mode: "ship", stage: "erts",
      via: ["oil-term-imam", "wp-hormuz", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Iran → China: onder sancties gaat vrijwel de hele Iraanse export met een 'schaduwvloot' naar China — nog steeds door Hormuz en Malakka." },
    { from: "oil-vae", to: "oil-ref-japan", value: 0.8, mode: "ship", stage: "erts",
      via: ["oil-term-jebeldhanna", "wp-hormuz", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "UAE → Japan via de reguliere Golf-route (Jebel Dhanna, door Hormuz)." },
    { from: "oil-vae", to: "oil-ref-china", value: 0.7, mode: "ship", stage: "erts",
      via: ["oil-term-jebeldhanna", "wp-hormuz", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "UAE → China (Golf-route door Hormuz)." },
    { from: "oil-koeweit", to: "oil-ref-singapore", value: 0.6, mode: "ship", stage: "erts",
      via: ["oil-term-kuwait", "wp-hormuz", "wp-aceh", "wp-malakka", "wp-singapore"],
      note: "Koeweit → Singapore, door Hormuz en Malakka." },
    { from: "oil-koeweit", to: "oil-ref-ulsan", value: 0.6, mode: "ship", stage: "erts",
      via: ["oil-term-kuwait", "wp-hormuz", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Koeweit → Zuid-Korea (Ulsan)." },

    // === B. HORMUZ-BYPASS-PIJPLEIDINGEN =====================================
    { from: "oil-saoedi", to: "oil-term-yanbu", value: 0.5, mode: "pipeline", stage: "erts",
      note: "De Oost-West-pijpleiding (Petroline): Saoedische crude dwars door het schiereiland naar de Rode Zee — om HORMUZ te vermijden." },
    { from: "oil-term-yanbu", to: "oil-ref-rotterdam", value: 0.5, mode: "ship", stage: "erts",
      via: ["wp-suez", "wp-gibraltar"],
      note: "Yanbu → Europa: vanaf de Rode Zee direct door Suez en Gibraltar. De bypass die Hormuz oversloeg." },
    { from: "oil-vae", to: "oil-term-fujairah", value: 0.6, mode: "pipeline", stage: "erts",
      note: "De Habshan-Fujairah-pijpleiding: UAE-crude naar de GOLF VAN OMAN, volledig buiten de Straat van Hormuz om." },
    { from: "oil-term-fujairah", to: "oil-ref-jamnagar", value: 0.4, mode: "ship", stage: "erts",
      note: "Fujairah → India: vertrekt al búiten Hormuz, recht over de Arabische Zee. De bypass in actie." },
    { from: "oil-term-fujairah", to: "oil-ref-singapore", value: 0.3, mode: "ship", stage: "erts",
      via: ["wp-aceh", "wp-malakka", "wp-singapore"],
      note: "Fujairah → Singapore: Hormuz overgeslagen, dan de normale route via Malakka." },

    // === C. RUSLAND-OMLEIDING (2022→) =======================================
    { from: "oil-rusland", to: "oil-ref-jamnagar", value: 1.8, mode: "ship", stage: "erts",
      via: ["oil-term-primorsk", "wp-deense-straten", "wp-dover", "wp-gibraltar", "wp-suez", "wp-rode-zee", "wp-bab"],
      note: "DE GROTE NIEUWE PIJL: Russische crude die vroeger naar Rotterdam ging, gaat nu vanaf Primorsk (Baltisch) de hele weg om Europa heen — Deense Straten, Kanaal, Gibraltar, Suez, Bab — naar India. De langste omweg van de kaart, geboren uit sancties." },
    { from: "oil-rusland", to: "oil-ref-china", value: 1.6, mode: "ship", stage: "erts",
      via: ["oil-term-kozmino", "wp-taiwan"],
      note: "ESPO → Kozmino → China: de korte, directe Pacific-uitgang van Russische crude, zonder westelijke zeestraten. China's belangrijkste alternatief voor Golf-olie." },
    { from: "oil-rusland", to: "oil-ref-jamnagar", value: 0.7, mode: "ship", stage: "erts",
      via: ["oil-term-novoros", "wp-bosporus", "wp-dardanellen", "wp-suez", "wp-rode-zee", "wp-bab"],
      note: "Novorossiysk (Zwarte Zee) → India: door de Bosporus én de Dardanellen, dan Suez. De tweede omgeleide route naar India." },
    { from: "oil-rusland", to: "oil-mkt-europa", value: 0.3, mode: "pipeline", stage: "erts",
      note: "De Druzhba-pijpleiding: het laatste restje Russische crude dat nog over LAND (via Belarus/Polen) Midden-Europa binnenkomt — met uitzonderingen voor Hongarije/Slowakije. Geïllustreerd als landstroom naar NW-Europa." },
    { from: "oil-rusland", to: "oil-ref-rotterdam", value: 0.2, mode: "ship", stage: "erts",
      via: ["oil-term-primorsk", "wp-deense-straten"],
      note: "De gekrompen rest: wat er nog van de ooit dikke Rusland → Rotterdam-stroom over is. Zet het contrast met de dikke India-pijl." },

    // === D. KAZACHSTAN (landlocked: CPC door Rusland vs BTC-bypass) ==========
    { from: "oil-kazachstan", to: "oil-ref-rotterdam", value: 1.3, mode: "ship", stage: "erts",
      via: ["oil-term-novoros", "wp-bosporus", "wp-dardanellen", "wp-gibraltar"],
      note: "De CPC-route: Kazachse Tengiz-crude per pijpleiding dwars door RUSLAND naar Novorossiysk, dan door de Bosporus/Dardanellen en Gibraltar naar Europa. Landlocked én afhankelijk van Russisch grondgebied." },
    { from: "oil-kazachstan", to: "oil-ref-rotterdam", value: 0.5, mode: "pipeline", stage: "erts",
      via: ["oil-term-ceyhan", "wp-gibraltar"],
      note: "De BTC-bypass: Kazachse crude die (trans-Kaspisch + Baku-Tbilisi-Ceyhan) naar de Middellandse Zee wordt geleid — om Rusland én de Golf heen. Geïllustreerd als landcorridor naar Ceyhan, dan per schip." },

    // === E. AMERIKA'S =======================================================
    { from: "oil-vs", to: "oil-ref-rotterdam", value: 1.2, mode: "ship", stage: "erts",
      via: ["oil-term-corpus", "wp-golf-mexico", "wp-florida"],
      note: "DE OMMEKEER: Amerikaanse schalie-crude vertrekt uit Corpus Christi, de Golf van Mexico uit langs Florida, de Atlantische Oceaan over naar Europa. De VS als exporteur — precies andersom dan de 20e eeuw." },
    { from: "oil-vs", to: "oil-ref-china", value: 0.6, mode: "ship", stage: "erts",
      via: ["oil-term-corpus", "wp-golf-mexico", "wp-florida", "wp-atl-brazilie", "wp-kaap", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "VS → China: de lange VLCC-route uit de Golf van Mexico, om Kaap de Goede Hoop (te groot voor Panama), naar Oost-Azië." },
    { from: "oil-canada", to: "oil-ref-golfkust", value: 3.8, mode: "pipeline", stage: "erts",
      note: "Canadese oliezanden → de Amerikaanse Golfkust per pijpleiding (Enbridge/Keystone). Veruit de dikste landstroom van de kaart: bijna alle Canadese export gaat naar één afnemer, de VS." },
    { from: "oil-venezuela", to: "oil-ref-golfkust", value: 0.3, mode: "ship", stage: "erts",
      via: ["oil-term-jose", "wp-caribisch", "wp-golf-mexico"],
      note: "Venezolaanse zware crude → de VS-Golfkust (raffinaderijen gebouwd voor zwaar). Een DUN pijltje — ondanks de grootste reserves ter wereld. De reserves-vs-productie-paradox." },
    { from: "oil-venezuela", to: "oil-ref-china", value: 0.4, mode: "ship", stage: "erts",
      via: ["oil-term-jose", "wp-atl-brazilie", "wp-kaap", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Venezuela → China (olie-voor-leningen): om de Kaap naar Oost-Azië. Ook dun — de productie is de flessenhals, niet de reserves." },

    // === F. ATLANTISCH BEKKEN ===============================================
    { from: "oil-nigeria", to: "oil-ref-rotterdam", value: 0.7, mode: "ship", stage: "erts",
      via: ["oil-term-bonny", "wp-gibraltar"],
      note: "Nigeriaanse lichte zoete crude (Bonny Light) → Europa: langs de West-Afrikaanse kust en door Gibraltar." },
    { from: "oil-nigeria", to: "oil-ref-jamnagar", value: 0.5, mode: "ship", stage: "erts",
      via: ["oil-term-bonny", "wp-kaap", "wp-moz-noord"],
      note: "Nigeria → India: om Kaap de Goede Hoop en over de Indische Oceaan." },
    { from: "oil-angola", to: "oil-ref-china", value: 0.8, mode: "ship", stage: "erts",
      via: ["wp-kaap", "wp-moz-noord", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Angolese offshore-crude → China (grootste afnemer): om de Kaap en door Malakka." },
    { from: "oil-brazilie", to: "oil-ref-china", value: 0.9, mode: "ship", stage: "erts",
      via: ["wp-kaap", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Braziliaanse pré-sal-crude → China: de Zuid-Atlantische Oceaan over, om de Kaap, door Malakka." },
    { from: "oil-brazilie", to: "oil-ref-rotterdam", value: 0.4, mode: "ship", stage: "erts",
      via: ["wp-atl-brazilie", "wp-gibraltar"],
      note: "Brazilië → Europa: over de Atlantische Oceaan en door Gibraltar." },
    { from: "oil-noorwegen", to: "oil-ref-rotterdam", value: 1.5, mode: "ship", stage: "erts",
      note: "Noorse Noordzee-crude → Rotterdam: de korte, veilige, niet-Russische levenslijn van NW-Europa. Extra dik sinds 2022." },

    // === G. PRODUCT-TRADE (raffinaat: diesel/benzine) =======================
    { from: "oil-ref-jamnagar", to: "oil-mkt-europa", value: 0.4, mode: "ship", stage: "raffinaat",
      via: ["wp-bab", "wp-rode-zee", "wp-suez", "wp-gibraltar", "wp-dover"],
      note: "Indiase diesel → NW-Europa: door Suez en Gibraltar. India raffineert (deels omgeleide Russische) crude en verkoopt het product door aan Europa." },
    { from: "oil-ref-jamnagar", to: "oil-mkt-wafrika", value: 0.3, mode: "ship", stage: "raffinaat",
      via: ["wp-bab", "wp-rode-zee", "wp-suez", "wp-gibraltar"],
      note: "DE PARADOX: geraffineerd product (benzine/diesel) uit India → West-Afrika, een crude-EXPORTeur die zelf product moest IMPORTEREN. Kantelt sinds Dangote (2024)." },
    { from: "oil-ref-jubail", to: "oil-mkt-oostafrika", value: 0.3, mode: "ship", stage: "raffinaat",
      via: ["wp-hormuz"],
      note: "Saoedisch product (Jubail) → Oost-Afrika (Mombasa): door Hormuz, dan zuidwaarts over de Arabische Zee." },
    { from: "oil-ref-golfkust", to: "oil-mkt-latam", value: 0.7, mode: "ship", stage: "raffinaat",
      via: ["wp-golf-mexico", "wp-caribisch", "wp-atl-brazilie"],
      note: "Amerikaanse benzine/diesel → Latijns-Amerika: de VS is de dominante productleverancier voor het continent." },
    { from: "oil-ref-golfkust", to: "oil-mkt-europa", value: 0.4, mode: "ship", stage: "raffinaat",
      via: ["wp-golf-mexico", "wp-florida", "wp-dover"],
      note: "Amerikaans product → NW-Europa: de Golf van Mexico uit, de Atlantische Oceaan over." },
    { from: "oil-ref-ruwais", to: "oil-mkt-oostafrika", value: 0.2, mode: "ship", stage: "raffinaat",
      via: ["wp-hormuz"],
      note: "UAE-product (Ruwais) → Oost-Afrika, door Hormuz." },

    // === H. PETROCHEMIE (product: kunststof) ================================
    { from: "oil-ref-jubail", to: "oil-pchem-jubail", value: 0.3, mode: "ship", stage: "product",
      note: "Jubail: raffinaderij → SABIC-kraker. Nafta/ethaan wordt kunststof — de derde daad van de olie. (Korte kust-hop binnen het Jubail-industriecomplex.)" },
    { from: "oil-pchem-jubail", to: "oil-mkt-europa", value: 0.15, mode: "ship", stage: "product",
      via: ["wp-hormuz", "wp-bab", "wp-rode-zee", "wp-suez", "wp-gibraltar", "wp-dover"],
      note: "Saoedische kunststof → Europa: de lichte, hoge boog van olie-als-plastic, de hele zeestraten-ketting langs." },
    { from: "oil-ref-rotterdam", to: "oil-pchem-antwerpen", value: 0.2, mode: "ship", stage: "product",
      note: "ARA-integratie: Rotterdamse raffinage-feed → de Antwerpse krakers (Europa's grootste petrochemiecluster)." },
    { from: "oil-ref-ulsan", to: "oil-pchem-yeosu", value: 0.2, mode: "ship", stage: "product",
      note: "Zuid-Korea: raffinage-feed → de Yeosu-krakers, kunststof-export naar Azië." },
    { from: "oil-ref-china", to: "oil-pchem-ningbo", value: 0.2, mode: "ship", stage: "product",
      note: "China bouwt petrochemie bij (Ningbo) om zelfvoorzienend te worden in kunststof — en importeert daarvoor juist méér crude." },
  ],

  // ==========================================================================
  // SPANNINGEN — waar de olieketen knijpt. Verwijst naar de universele
  // knelpuntenlijst (wp-*). flows-verwijzing: "from-id>to-id".
  // ==========================================================================
  tensions: [
    { id: "oil-t-hormuz", type: "knelpunt", title: "Straat van Hormuz: de moeder van alle knelpunten",
      lat: 26.60, lon: 56.50,
      nodes: ["oil-term-rastanura", "oil-term-basra", "oil-term-imam", "oil-term-kuwait", "oil-term-jebeldhanna",
              "oil-term-yanbu", "oil-term-fujairah"],
      flows: ["oil-saoedi>oil-ref-china", "oil-irak>oil-ref-china", "oil-iran>oil-ref-china",
              "oil-vae>oil-ref-japan", "oil-koeweit>oil-ref-singapore", "oil-saoedi>oil-term-yanbu",
              "oil-vae>oil-term-fujairah"],
      metric: "~20 Mb/d — bijna een derde van alle olie over zee, door één 33 km smalle straat",
      note: "Geen enkel knelpunt komt hierbij in de buurt: bijna alle crude van Saoedi-Arabië, Irak, Iran, Koeweit en de VAE moet door de Straat van Hormuz. Er is geen volwaardig omvaaralternatief — alleen de twee bypass-PIJPLEIDINGEN (Saoedi → Yanbu aan de Rode Zee, UAE → Fujairah aan de Golf van Oman) kunnen een fractie eromheen leiden. Dít is de reden dat de hele wereld naar de Golf kijkt zodra het daar spant." },

    { id: "oil-t-malakka", type: "knelpunt", title: "Straat van Malakka: de Azië-flessenhals",
      lat: 3.00, lon: 100.60,
      nodes: ["oil-ref-china", "oil-ref-japan", "oil-ref-ulsan", "oil-ref-singapore"],
      flows: ["oil-saoedi>oil-ref-china", "oil-saoedi>oil-ref-japan", "oil-irak>oil-ref-china",
              "oil-iran>oil-ref-china", "oil-koeweit>oil-ref-ulsan"],
      metric: "~⅓ van de wereldhandel over zee; voor China/Japan/Korea de olie-levenslijn",
      note: "Direct ná Hormuz komt Malakka: alle Golf-crude naar Oost-Azië knijpt hier voor de tweede keer samen. De 'Malakka-dilemma' — China's grootste strategische kwetsbaarheid, want een blokkade hier snijdt zijn olie-aanvoer af. Alternatieven (Lombok/Sunda) kosten dagen extra. Vandaar de Chinese honger naar de ESPO-pijp en Russische Pacific-crude die Malakka overslaat." },

    { id: "oil-t-rusland", type: "beleid", title: "De Rusland-omleiding (2022→): Europa → India/China",
      lat: 55.00, lon: 45.00,
      nodes: ["oil-rusland", "oil-term-primorsk", "oil-term-novoros", "oil-term-kozmino"],
      flows: ["oil-rusland>oil-ref-jamnagar", "oil-rusland>oil-ref-china", "oil-rusland>oil-mkt-europa",
              "oil-rusland>oil-ref-rotterdam"],
      metric: "de EU-boycot + het G7-prijsplafond herrouteerden ~3–4 Mb/d in maanden",
      note: "Vóór 2022 stroomde Russische crude kort en dik naar Europa. Na de invasie en de sancties werd diezelfde olie in een half jaar omgeleid naar India en China: de langste omweg van de kaart (Primorsk om Europa heen naar India), de ESPO-pijp naar de Pacific, en Novorossiysk door de Bosporus. Een 'schaduwvloot' oude tankers ontwijkt het prijsplafond. Geen zeestraat maar een beleidsbesluit dat de wereldkaart hertekende — het olie-equivalent van uranium's Trans-Kaspische de-risking, maar dan andersom." },

    { id: "oil-t-babsuez", type: "knelpunt", title: "Bab-el-Mandeb / Suez: de Rode Zee-crisis (2024)",
      lat: 12.60, lon: 43.40,
      nodes: ["oil-ref-rotterdam", "oil-ref-jamnagar"],
      flows: ["oil-saoedi>oil-ref-rotterdam", "oil-rusland>oil-ref-jamnagar", "oil-term-yanbu>oil-ref-rotterdam",
              "oil-ref-jamnagar>oil-mkt-europa"],
      metric: "Houthi-aanvallen (2024) → tankers mijden de Rode Zee, +10–14 dagen om de Kaap",
      note: "De kortste route Azië–Europa loopt door Bab-el-Mandeb en Suez. Toen Houthi-aanvallen de Rode Zee in 2024 onveilig maakten, kozen veel tankers de omweg om Kaap de Goede Hoop — dagen langer, duurder, en een levende herinnering dat één zeestraat de hele Oost-West-oliestroom kan verleggen (zoals de Ever Given in 2021 al liet zien)." },

    { id: "oil-t-reserves", type: "concentratie", title: "Reserves ≠ productie ≠ verbruik (OPEC+)",
      lat: 20.00, lon: 45.00,
      nodes: ["oil-saoedi", "oil-venezuela", "oil-rusland", "oil-vs"],
      flows: ["oil-venezuela>oil-ref-golfkust", "oil-venezuela>oil-ref-china", "oil-canada>oil-ref-golfkust"],
      metric: "grootste reserves: Venezuela & de Golf — grootste verbruik: Azië, N-Amerika, Europa",
      note: "Olie's structurele scheefheid: de reserves zitten in de Golf, Venezuela en Rusland, maar het verbruik zit elders — vandaar de eindeloze tankerstromen. En reserves ≠ productie: Venezuela heeft de grootste reserves ter wereld maar produceert bijna niets (dun pijltje), terwijl de VS met minder reserves de grootste producent werd. Saoedi-Arabië en Rusland sturen samen als OPEC+ de productie — en dus de prijs. De kaart laat zien waarom een handvol landen de wereldeconomie in de hand heeft." },

    { id: "oil-t-bosporus", type: "knelpunt", title: "Bosporus & de landlocked Kaspische olie",
      lat: 41.10, lon: 29.05,
      nodes: ["oil-kazachstan", "oil-term-novoros", "oil-term-ceyhan"],
      flows: ["oil-kazachstan>oil-ref-rotterdam", "oil-rusland>oil-ref-jamnagar"],
      metric: "Kazachstan (landlocked) kiest tussen de CPC-pijp dóór Rusland of de BTC-bypass",
      note: "Alle olie uit de Zwarte Zee — Russisch én Kazachs — moet door de Bosporus en de Dardanellen, waar tankers zich opstapelen. Kazachstan zit bovendien landlocked ingeklemd: zijn Tengiz-crude gaat óf via de CPC-pijpleiding dwars door Rusland naar Novorossiysk (afhankelijk van Russisch grondgebied), óf via de BTC-corridor naar Ceyhan aan de Middellandse Zee — om Rusland én de Golf heen. Dezelfde landlocked-keuze als bij het Kazachse uranium, nu voor olie." },
  ],
});
