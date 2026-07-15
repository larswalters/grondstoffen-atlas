// ============================================================================
// ZILVER (Ag) — volledig uitgewerkte module. Peiljaar ±2023-2024.
// Cijfers indicatief/afgerond, o.b.v. The Silver Institute / Metals Focus
// (World Silver Survey), USGS MCS 2025 en bedrijfsrapportages (Fresnillo,
// Peñoles, KGHM). Eenheid overal: t fijn zilver/jaar, zodat de hele keten
// optelbaar blijft. Wereldmijnproductie ≈ 26.000 t (~830 Moz). Zie design/zilver.md.
//
// DE VORM VAN ZILVER (fundamenteel anders dan alle eerdere grondstoffen):
//   - GEEN WINNINGS-TRECHTER. ~70-75% van al het zilver is BIJPRODUCT van
//     zink/lood-, koper- en goudmijnen. De zilver-stippen zitten bovenop
//     andermans mijnen (Mexico, Peru, China, KGHM-koper in Polen, Chili,
//     Australië, Bolivia). Je kunt zilver niet opschalen zonder meer zink of
//     koper te willen -> het aanbod is INELASTISCH (volgt de zink/koper/goud-
//     cyclus, niet de zilverprijs). Elke mijn-node vermeldt z'n hoofdmetaal.
//   - DE CONCENTRATIE ZIT DOWNSTREAM, AAN DE VRAAGKANT. Industrie is >50% van
//     de vraag, met ZONNEPANELEN (fotovoltaïsch) als grootste én snelst
//     groeiende toepassing, geconcentreerd in de Chinese zonnecel-industrie.
//   - STRUCTUREEL TEKORT: al enkele jaren vraag > aanbod; het gat wordt gedicht
//     door de bovengrondse KLUISVOORRADEN (LBMA-Londen, COMEX-New York, SGE-
//     Shanghai) af te tappen -> de optionele exchange-toggle toont dat.
//
// STAGES (via `stage`):
//   erts       = mijn (bijproduct) -> doré / concentraat op weg naar smelter/
//                raffinaderij — dof/donkergrijs. Óók recyclingschroot -> raffinage.
//   raffinaat  = good-delivery baar (1000 oz) — volle zilverkleur.
//   product    = industrieel eindproduct (solar / elektronica / sieraad) — licht.
//
// TRANSPORT is schip + land (industrieel metaal ~1/80 van goud's waarde per gram
// -> het vaart, het vliegt niet). GEEN nieuwe render-modus, GEEN nieuw chokepoint:
// derde grondstof na nikkel/olie die volledig op de bestaande routekaart draait
// (Pacific-vaarpunten, Panama, Gibraltar, Suez/Rode Zee/Bab, Malakka, Deense
// Straten). Inland-origins bij een ship-flow: 1e via = een haven (gathering-leg
// routeert auto als land, olie/koper-patroon).
//
// BEURSVOORRADEN (type "exchange" / flow.layer "exchange") = de BESTAANDE
// optionele toggle van koper/nikkel, hergebruikt zonder engine-wijziging. Nuance:
// COMEX "registered" (leverbaar) vs "eligible" (gekluisd, niet leverbaar) — de
// 2021 "silver squeeze" legde het verschil tussen papier- en fysieke markt bloot.
// ============================================================================

REGISTER({
  id: "silver",
  name: "Zilver",
  symbol: "Ag",
  color: "#AEB6BF",       // koel metallic zilvergrijs: de mijn-markers
  flowColor: "#C8D0D8",   // lichter zilvergrijs: de stromen tegen de donkere bol
  detail: "uitgewerkt",
  unit: "t/jaar (indicatief)",
  blurb: "De meeste zilver komt niet uit zilvermijnen: ~70-75% valt als bijproduct " +
    "uit zink/lood-, koper- en goudmijnen (Mexico #1, Peru, China, KGHM-Polen) — het " +
    "aanbod is inelastisch. Tegelijk stuwt de energietransitie de industriële vraag, " +
    "zonnepanelen voorop en geconcentreerd in China, naar recordhoogte. Resultaat: een " +
    "structureel tekort dat de kluisvoorraden (LBMA-Londen, COMEX-New York, Shanghai) aftapt.",

  nodes: [
    // =============================================================== MIJNEN
    // De spreiding + het bijproduct-karakter ÍS het verhaal: veel losse stippen
    // bovenop andermans mijnen, geen enkele winnings-trechter. `note` benoemt
    // telkens het hoofdmetaal waar het zilver een bijproduct van is (of "primair").
    // --- Mexico (#1, ~25% wereld): de winnings- én raffinage-anker ----------
    { id: "ag-fresnillo", type: "mine", name: "Fresnillo / Saucito", country: "Mexico",
      lat: 23.18, lon: -102.87, share: 4.0, tier: 1, operator: "Fresnillo plc",
      status: "actief", capacity: "≈ 1.050 t Ag/j",
      note: "Zacatecas; PRIMAIR zilver — Fresnillo is het grootste primaire zilverbedrijf ter wereld. Doré per truck naar de Peñoles-raffinaderij in Torreón." },
    { id: "ag-penasquito", type: "mine", name: "Peñasquito", country: "Mexico",
      lat: 24.66, lon: -101.55, share: 2.5, tier: 1, operator: "Newmont",
      status: "actief", capacity: "≈ 650 t Ag/j",
      note: "Zacatecas; poly-metaal — zilver als bijproduct van GOUD + zink/lood. Een van 's werelds grootste zilverbronnen." },

    // --- China (#2, ~13%): grotendeels gesloten binnenlands systeem ---------
    { id: "ag-china", type: "mine", name: "China lood-zink/koper-cluster (Hunan)", country: "China",
      lat: 27.80, lon: 112.90, share: 13.0, tier: 1, operator: "div. (staat + privaat)",
      status: "actief", capacity: "≈ 3.400 t Ag/j",
      note: "Bijproduct van LOOD/ZINK + koper (Hunan/Yunnan/Binnen-Mongolië). China is #2-producent maar raffineert en verbruikt vrijwel alles binnenlands — een gesloten keten." },

    // --- Peru (#3, ~13%): primair + koper-bijproduct ------------------------
    { id: "ag-uchucchacua", type: "mine", name: "Uchucchacua", country: "Peru",
      lat: -10.62, lon: -76.92, share: 1.5, tier: 2, operator: "Buenaventura",
      status: "actief", capacity: "≈ 400 t Ag/j",
      note: "Oyón (Andes); PRIMAIR zilver (+ lood/zink). Concentraat over de Andes naar Callao, dan de Stille Oceaan over naar Aziatische smelters." },
    { id: "ag-antamina", type: "mine", name: "Antamina", country: "Peru",
      lat: -9.53, lon: -77.05, share: 2.0, tier: 1, operator: "Glencore/BHP/Teck JV",
      status: "actief", capacity: "≈ 520 t Ag/j",
      note: "Ancash; bijproduct van KOPER/zink — het zilver reist mee met het koperconcentraat naar de Chinese smelters." },

    // --- Polen / Chili: koper-bijproduct (de grootste 'onzichtbare' bron) ---
    { id: "ag-kghm", type: "mine", name: "KGHM (Lubin/Polkowice)", country: "Polen",
      lat: 51.40, lon: 16.20, share: 5.0, tier: 1, operator: "KGHM",
      status: "actief", capacity: "≈ 1.300 t Ag/j",
      note: "Neder-Silezië; bijproduct van KOPER — KGHM is de grootste bijproduct-zilverbron ter wereld uit één onderneming. Doré naar de eigen Głogów-smelter." },
    { id: "ag-chile-cu", type: "mine", name: "Chileense koper (Escondida-cluster)", country: "Chili",
      lat: -24.27, lon: -69.07, share: 4.0, tier: 1, operator: "BHP e.a.",
      status: "actief", capacity: "≈ 1.050 t Ag/j",
      note: "Atacama; bijproduct van KOPER — het zilver zit in het koperconcentraat dat over de Stille Oceaan naar Chinese smelters vaart." },

    // --- Australië / Bolivia / Kazachstan: zink-lood-bijproduct -------------
    { id: "ag-cannington", type: "mine", name: "Cannington", country: "Australië",
      lat: -21.87, lon: 140.92, share: 1.5, tier: 2, operator: "South32",
      status: "actief", capacity: "≈ 400 t Ag/j",
      note: "Queensland; bijproduct van LOOD/ZINK — een van 's werelds grootste zilvermijnen. Concentraat per spoor naar Townsville." },
    { id: "ag-sancristobal", type: "mine", name: "San Cristóbal", country: "Bolivia",
      lat: -21.05, lon: -67.15, share: 1.5, tier: 2, operator: "Sumitomo",
      status: "actief", capacity: "≈ 400 t Ag/j",
      note: "Potosí (Altiplano); bijproduct van ZINK/LOOD. Landlocked -> concentraat per spoor/truck naar de Chileense kust (Antofagasta), dan per schip naar Azië." },
    { id: "ag-kazzinc", type: "mine", name: "Kazzinc (Ridder)", country: "Kazachstan",
      lat: 50.20, lon: 83.53, share: 1.5, tier: 3, operator: "Glencore/Kazzinc",
      status: "actief", capacity: "≈ 400 t Ag/j",
      note: "Oost-Kazachstan; bijproduct van ZINK/LOOD + koper. Landlocked -> deels binnenlands geraffineerd, deels over land naar de Chinese raffinage." },

    // --- VS / Zweden / Rusland: primair + koper-bijproduct ------------------
    { id: "ag-greens-creek", type: "mine", name: "Greens Creek", country: "VS (Alaska)",
      lat: 58.07, lon: -134.63, share: 1.0, tier: 2, operator: "Hecla", coastal: true,
      status: "actief", capacity: "≈ 270 t Ag/j",
      note: "Admiralty Island; PRIMAIR zilver (+ zink). Eiland-mijn -> doré per schip langs de Pacific-kust naar de raffinage in de Pacific-Noordwest." },
    { id: "ag-us-cu", type: "mine", name: "Bingham Canyon (Kennecott)", country: "VS (Utah)",
      lat: 40.52, lon: -112.15, share: 1.0, tier: 3, operator: "Rio Tinto",
      status: "actief", capacity: "≈ 260 t Ag/j",
      note: "Utah; bijproduct van KOPER/goud. Doré over land naar de Amerikaanse edelmetaalraffinage." },
    { id: "ag-garpenberg", type: "mine", name: "Garpenberg", country: "Zweden",
      lat: 60.30, lon: 16.10, share: 1.0, tier: 3, operator: "Boliden",
      status: "actief", capacity: "≈ 260 t Ag/j",
      note: "Dalarna; bijproduct van ZINK/LOOD. Een van de modernste ondergrondse mijnen; concentraat naar de Boliden-smelter Rönnskär." },
    { id: "ag-dukat", type: "mine", name: "Dukat", country: "Rusland",
      lat: 62.55, lon: 155.50, share: 1.5, tier: 2, operator: "Polymetal", coastal: true,
      status: "actief", capacity: "≈ 400 t Ag/j",
      note: "Magadan (Verre Oosten); PRIMAIR zilver. Sinds 2022 verschuift de afzet van Europa naar Azië — doré via de Zee van Ochotsk naar Chinese raffinage." },

    // ================================================= RAFFINAGE / SMELTERS
    // Zilver komt vrij in twee stromen: primaire doré -> edelmetaalraffinage, én
    // bijproduct in base-metaal-smelters (zink/koper/lood) die het terugwinnen.
    // Peñoles (Torreón) = 's werelds grootste zilverraffinaderij.
    { id: "ag-ref-penoles", type: "refinery", name: "Met-Mex Peñoles (Torreón)", country: "Mexico",
      lat: 25.55, lon: -103.42, tier: 1, operator: "Industrias Peñoles",
      capacity: "≈ 1.800 t Ag/j",
      note: "GROOTSTE zilverraffinaderij ter wereld — de niet-Chinese trechter. Verwerkt de Mexicaanse doré tot good-delivery baren; per truck naar Veracruz/Manzanillo, dan de zee op naar COMEX/LBMA." },
    { id: "ag-ref-kghm", type: "refinery", name: "KGHM Głogów-smelter", country: "Polen",
      lat: 51.66, lon: 16.08, tier: 1, operator: "KGHM",
      capacity: "≈ 1.300 t Ag/j",
      note: "De grootste zilver-output uit één koper-smelter. Good-delivery baren over land (Kanaaltunnel) naar de LBMA-kluizen in Londen." },
    { id: "ag-ref-china", type: "refinery", name: "China oostkust-smelters (Jiangxi Copper e.a.)", country: "China",
      lat: 30.00, lon: 121.90, tier: 1, operator: "div.", coastal: true,
      capacity: "≈ 4.000 t Ag/j",
      note: "INSULAIR — raffineert het binnenlandse lood-zink/koper-zilver ÉN geïmporteerd Zuid-Amerikaans/Australisch concentraat. Baren naar de SGE-kluis in Shanghai." },
    { id: "ag-ref-korea", type: "refinery", name: "Korea Zinc / LS-Nikko (Onsan)", country: "Zuid-Korea",
      lat: 35.42, lon: 129.34, tier: 1, operator: "Korea Zinc", coastal: true,
      capacity: "≈ 2.000 t Ag/j",
      note: "Onsan; 's werelds grootste base-metaal-smeltcomplex — wint zilver terug uit zink/lood-concentraat van over de hele wereld (Peru/Bolivia/Australië)." },
    { id: "ag-ref-valcambi", type: "refinery", name: "Valcambi (Balerna, Ticino)", country: "Zwitserland",
      lat: 45.845, lon: 9.005, tier: 2, operator: "Valcambi",
      capacity: "≈ 600 t Ag/j",
      note: "Ticino; good-delivery baren (ook goud). Vooral premium-/beleggingszilver; baren over land naar Londen." },
    { id: "ag-ref-aurubis", type: "refinery", name: "Aurubis (Hamburg)", country: "Duitsland",
      lat: 53.53, lon: 10.05, tier: 2, operator: "Aurubis", coastal: true,
      capacity: "≈ 1.200 t Ag/j",
      note: "Europa's grootste koper-smelter; zilver als bijproduct — levert de Europese industrie direct, plus recyclingschroot terug in de keten." },
    { id: "ag-ref-japan", type: "refinery", name: "Mitsubishi / Dowa", country: "Japan",
      lat: 34.90, lon: 136.60, tier: 3, operator: "Mitsubishi Materials", coastal: true,
      capacity: "≈ 500 t Ag/j",
      note: "Tech-zilver + geïmporteerd concentraat; voedt de Japanse elektronica-/halfgeleiderindustrie. Verwerkt ook urban-mining-schroot." },
    { id: "ag-ref-us", type: "refinery", name: "VS-raffinage (Pacific-Noordwest)", country: "VS",
      lat: 46.20, lon: -123.90, tier: 3, operator: "Asarco (Grupo México) e.a.", coastal: true,
      capacity: "≈ 300 t Ag/j",
      note: "Pacific-Noordwest (Columbia-monding); verwerkt Alaskaanse doré (Greens Creek, per schip langs de kust) + koper-bijproduct (Bingham, over land). Levert de Amerikaanse industrie + munten." },
    { id: "ag-ref-boliden", type: "refinery", name: "Boliden Rönnskär", country: "Zweden",
      lat: 64.70, lon: 21.23, tier: 3, operator: "Boliden", coastal: true,
      capacity: "≈ 400 t Ag/j",
      note: "Scandinavisch zink/koper-smeltcomplex; zilver uit het Garpenberg-concentraat + e-waste. Baren de Oostzee op via de Deense Straten." },

    // ================================================================ HAVENS
    { id: "ag-port-veracruz", type: "port", name: "Veracruz", country: "Mexico",
      lat: 19.16, lon: -96.13, tier: 3,
      note: "Atlantische uitgang van Mexico — Peñoles-baren de Golf van Mexico op richting COMEX en Europa." },
    { id: "ag-port-callao", type: "port", name: "Callao (Lima)", country: "Peru",
      lat: -12.05, lon: -77.15, tier: 2,
      note: "De Peruaanse exporthaven; concentraat van de Andes-mijnen de Stille Oceaan op naar Aziatische smelters." },
    { id: "ag-port-antofagasta", type: "port", name: "Antofagasta / Mejillones", country: "Chili",
      lat: -23.65, lon: -70.40, tier: 2,
      note: "Noord-Chileense haven; verzamelt Chileens koperconcentraat én het landlocked Boliviaanse zink/lood-concentraat." },
    { id: "ag-port-townsville", type: "port", name: "Townsville", country: "Australië",
      lat: -19.25, lon: 146.82, tier: 3,
      note: "Noordoost-Australië; het Cannington-lood/zilver-concentraat de Koraalzee op richting Oost-Azië." },
    { id: "ag-port-rotterdam", type: "port", name: "Rotterdam", country: "Nederland",
      lat: 51.95, lon: 4.14, tier: 2,
      note: "Europese gateway; overslag van baren tussen het continent en de Londense kluizen." },
    { id: "ag-port-nhava", type: "port", name: "Nhava Sheva (Mumbai)", country: "India",
      lat: 18.95, lon: 73.00, tier: 2,
      note: "India's grootste containerhaven; invoer van baren voor de sieraden- én de groeiende solar-industrie." },

    // ================================================================ MARKT
    // Industrie > 50% van de vraag; zonnepanelen = de grootste én snelst
    // groeiende post, geconcentreerd in China. Ship-endpoints coastal.
    { id: "ag-mkt-china-solar", type: "market", name: "China — zonnepanelen (PV)", country: "China",
      lat: 32.00, lon: 121.60, tier: 1, coastal: true,
      note: "De grootste én snelst groeiende zilvervraag: zilverpasta in zonnecellen (Jiangsu-kustcluster, Nantong/Yangtze-monding). De energietransitie trekt zilver hierheen — de kern van het structurele tekort." },
    { id: "ag-mkt-china-elec", type: "market", name: "China — elektronica / EV", country: "China",
      lat: 22.55, lon: 114.06, tier: 1, coastal: true,
      note: "Shenzhen; contacten, connectoren, EV-vermogenselektronica. Na solar de tweede industriële pijler." },
    { id: "ag-mkt-india", type: "market", name: "India — sieraden + zilverwerk", country: "India",
      lat: 19.08, lon: 72.88, tier: 1, coastal: true,
      note: "Grootste sieraden-/beleggingsvraag ter wereld (+ zilverwerk); India importeert enorme hoeveelheden fysiek metaal en heeft nu ook een groeiende solar-vraag." },
    { id: "ag-mkt-eu", type: "market", name: "EU — industrie (PV / elektronica)", country: "Duitsland",
      lat: 50.90, lon: 7.00, tier: 2,
      note: "Europese fotovoltaïsche + elektronica- + auto-industrie; bevoorraad door Aurubis en de Londense kluizen." },
    { id: "ag-mkt-us", type: "market", name: "VS — industrie + belegging", country: "VS",
      lat: 40.00, lon: -83.00, tier: 2,
      note: "Amerikaanse elektronica-, solar- en muntenvraag; getrokken uit de COMEX-voorraden in New York." },
    { id: "ag-mkt-japan-korea", type: "market", name: "Japan/Korea — elektronica", country: "Japan",
      lat: 35.68, lon: 139.76, tier: 2, coastal: true,
      note: "Halfgeleiders, contacten, elektronica; leunt op de eigen Mitsubishi/Dowa-raffinage." },

    // ============================================================= RECYCLING
    // ~15-18% van het totale aanbod (industrieel/fotografisch/sieraadschroot).
    // ALWAYS-ON (koper/nikkel-patroon): stage `erts` (feedstock terug), géén `layer`.
    { id: "ag-rec-eu", type: "recycler", name: "Umicore (Hoboken)", country: "België",
      lat: 51.17, lon: 4.35, tier: 3,
      note: "E-waste-/edelmetaalrecycling; wint zilver terug uit elektronicaschroot -> terug de Europese raffinage in." },
    { id: "ag-rec-japan", type: "recycler", name: "Japan (urban mining)", country: "Japan",
      lat: 35.70, lon: 139.72, tier: 3,
      note: "Japans e-waste ('urban mining') terug naar Mitsubishi/Dowa — een van de hoogste recyclinggraden ter wereld." },
    { id: "ag-rec-us", type: "recycler", name: "VS (industrieel + fotografisch schroot)", country: "VS",
      lat: 41.00, lon: -81.50, tier: 3,
      note: "Amerikaans industrieel en fotografisch zilverschroot terug de eigen industrieketen in." },
    { id: "ag-rec-india", type: "recycler", name: "India (sieraadschroot)", country: "India",
      lat: 19.35, lon: 72.82, tier: 3,
      note: "Sieraadschroot blijft grotendeels binnen de Indiase sieradenketen circuleren." },

    // ============================ BEURSVOORRADEN (optionele toggle-laag)
    // type "exchange" -> alleen zichtbaar met de beursvoorraden-toggle (koper/
    // nikkel-patroon, hergebruikt). `stock` (t Ag) = kluisvoorraad -> node-grootte.
    // Het aftappen (layer:"exchange"-flows) toont het structurele tekort.
    { id: "ag-ex-lbma", type: "exchange", name: "LBMA (Londen — kluizen)", country: "VK",
      lat: 51.51, lon: -0.09, stock: 22000, tier: 1, coastal: true, exchange: "LBMA",
      note: "Grootste bovengrondse zilvervoorraad ter wereld; OTC-hart + prijsbenchmark. De kluizen lopen leeg wanneer de fysieke vraag (India/China) het metaal wegtrekt." },
    { id: "ag-ex-comex", type: "exchange", name: "COMEX (New York — registered)", country: "VS",
      lat: 40.71, lon: -74.01, stock: 9000, tier: 1, coastal: true, exchange: "COMEX",
      note: "Futures-benchmark. Cruciale nuance: 'registered' (leverbaar) vs 'eligible' (gekluisd, niet leverbaar) — de 2021 'silver squeeze' legde dat verschil bloot." },
    { id: "ag-ex-sge", type: "exchange", name: "Shanghai (SGE/SHFE)", country: "China",
      lat: 31.23, lon: 121.47, stock: 3000, tier: 2, coastal: true, exchange: "SGE",
      note: "De Chinese benchmark-/kluislaag; de voorraad trekt richting de binnenlandse zonnepanelen-vraag — het zichtbare uiteinde van het tekort." },
  ],

  // ==========================================================================
  // STROMEN — value in t Ag/jaar. stage bepaalt de kleur (erts dof, raffinaat
  // vol zilver, product licht). `via` = echte route langs havens (ag-port-*) en
  // de universele knelpunten/vaarpunten (wp-* uit data/_chokepoints.js).
  //
  //  A) Mijn -> raffinage/smelter (doré + concentraat convergeren)
  //  B) Raffinage -> kluis/industrie (good-delivery baren uitwaaieren)
  //  C) Interbancaire kluisstromen kluis<->kluis
  //  D) Kluis/raffinage -> industriële eindvraag (de solar-pull)
  //  E) Recycling -> raffinage (schroot terug, always-on)
  //  F) Beursvoorraden (layer:"exchange" -> alleen met de toggle): het aftappen
  // ==========================================================================
  flows: [
    // === A. MIJN -> RAFFINAGE/SMELTER (stage erts) ===========================
    { from: "ag-fresnillo", to: "ag-ref-penoles", value: 1050, mode: "road", stage: "erts",
      note: "Fresnillo-doré -> Torreón. Mexico binnenlands: de winning én de raffinage van de niet-Chinese keten liggen in één land." },
    { from: "ag-penasquito", to: "ag-ref-penoles", value: 650, mode: "road", stage: "erts",
      note: "Peñasquito-doré (goud/zink-bijproduct) -> Torreón, over land." },
    { from: "ag-china", to: "ag-ref-china", value: 3400, mode: "road", stage: "erts",
      note: "Chinees lood-zink/koper-zilver -> de oostkust-smelters. Binnenlands, gesloten keten." },
    { from: "ag-uchucchacua", to: "ag-ref-korea", value: 400, mode: "ship", stage: "erts",
      via: ["ag-port-callao", "wp-pac-west", "wp-scs", "wp-taiwan"],
      note: "Peruaans primair concentraat: over de Andes naar Callao (gathering), dan de Stille Oceaan over naar Korea Zinc." },
    { from: "ag-antamina", to: "ag-ref-china", value: 520, mode: "ship", stage: "erts",
      via: ["ag-port-callao", "wp-pac-west", "wp-scs", "wp-taiwan"],
      note: "Peruaans koperconcentraat draagt het zilver mee naar de Chinese smelters — bijproduct van een bijproduct." },
    { from: "ag-kghm", to: "ag-ref-kghm", value: 1300, mode: "road", stage: "erts",
      note: "KGHM-koperdoré -> de eigen Głogów-smelter, binnen Polen." },
    { from: "ag-chile-cu", to: "ag-ref-china", value: 1050, mode: "ship", stage: "erts",
      via: ["ag-port-antofagasta", "wp-pac-zuid", "wp-pac-west", "wp-scs", "wp-taiwan"],
      note: "Chileens koperconcentraat de Stille Oceaan over naar China — het zilver reist mee met het koper." },
    { from: "ag-cannington", to: "ag-ref-korea", value: 400, mode: "ship", stage: "erts",
      via: ["ag-port-townsville", "wp-pac-west", "wp-scs", "wp-taiwan"],
      note: "Australisch lood/zilver-concentraat: per spoor naar Townsville, dan via de westelijke Stille Oceaan naar Korea." },
    { from: "ag-sancristobal", to: "ag-ref-korea", value: 400, mode: "ship", stage: "erts",
      via: ["ag-port-antofagasta", "wp-pac-zuid", "wp-pac-west", "wp-taiwan"],
      note: "Landlocked Bolivia: zink/lood-concentraat per spoor over de Andes naar Antofagasta, dan de Stille Oceaan over." },
    { from: "ag-kazzinc", to: "ag-ref-china", value: 400, mode: "rail", stage: "erts",
      note: "Landlocked Kazachstan: zink/lood-concentraat over land naar de Chinese raffinage (Kazachstan grenst aan Xinjiang)." },
    { from: "ag-greens-creek", to: "ag-ref-us", value: 270, mode: "ship", stage: "erts",
      note: "Alaskaanse doré per schip langs de Pacific-kust naar de Pacific-Noordwest-raffinage." },
    { from: "ag-us-cu", to: "ag-ref-us", value: 260, mode: "road", stage: "erts",
      note: "Bingham-Canyon-doré (koper/goud-bijproduct) over land naar de raffinage." },
    { from: "ag-garpenberg", to: "ag-ref-boliden", value: 260, mode: "road", stage: "erts",
      note: "Garpenberg-concentraat -> de Boliden-smelter Rönnskär, binnen Zweden." },
    { from: "ag-dukat", to: "ag-ref-china", value: 400, mode: "ship", stage: "erts",
      via: ["wp-taiwan"],
      note: "Russisch Verre-Oosten-doré via de Zee van Ochotsk en de Japanse Zee naar de Chinese raffinage (afzet sinds 2022 naar Azië verschoven)." },

    // === B. RAFFINAGE -> KLUIS/INDUSTRIE (stage raffinaat) ===================
    { from: "ag-ref-penoles", to: "ag-ex-comex", value: 900, mode: "ship", stage: "raffinaat",
      via: ["ag-port-veracruz", "wp-florida"],
      note: "Peñoles-baren: per truck naar Veracruz (gathering), de Golf van Mexico uit langs Florida naar COMEX/New York. De grootste bilaterale zilverstroom." },
    { from: "ag-ref-penoles", to: "ag-ex-lbma", value: 500, mode: "ship", stage: "raffinaat",
      via: ["ag-port-veracruz", "wp-florida", "ag-port-rotterdam"],
      note: "Peñoles-baren de Atlantische Oceaan over naar de Londense kluizen." },
    { from: "ag-ref-kghm", to: "ag-ex-lbma", value: 700, mode: "road", stage: "raffinaat",
      note: "KGHM-baren over land (via de Kanaaltunnel) naar de LBMA-kluizen in Londen." },
    { from: "ag-ref-valcambi", to: "ag-ex-lbma", value: 300, mode: "road", stage: "raffinaat",
      note: "Zwitserse premium-baren over land naar Londen (belegging)." },
    { from: "ag-ref-korea", to: "ag-ex-sge", value: 800, mode: "ship", stage: "raffinaat",
      via: ["wp-taiwan"],
      note: "Koreaanse baren naar de SGE-kluis in Shanghai." },
    { from: "ag-ref-china", to: "ag-ex-sge", value: 2500, mode: "rail", stage: "raffinaat",
      note: "Binnenlands geraffineerde Chinese baren -> de Shanghai-kluis." },
    { from: "ag-ref-aurubis", to: "ag-mkt-eu", value: 900, mode: "road", stage: "raffinaat",
      note: "Aurubis levert de Europese industrie direct (zilver als koper-bijproduct)." },

    // === C. INTERBANCAIRE KLUISSTROMEN kluis<->kluis (stage raffinaat) =======
    { from: "ag-ex-lbma", to: "ag-ex-comex", value: 1500, mode: "ship", stage: "raffinaat",
      note: "Londen -> New York: de grote fysieke verschuiving 2021-2024 (squeeze + COMEX-premies trokken metaal de Atlantische Oceaan over)." },
    { from: "ag-ex-lbma", to: "ag-ex-sge", value: 600, mode: "ship", stage: "raffinaat",
      via: ["wp-gibraltar", "wp-suez", "wp-rode-zee", "wp-bab", "wp-malakka", "wp-scs", "wp-taiwan"],
      note: "Londen -> Shanghai via Suez: China trekt fysiek metaal aan onder het tekort." },

    // === D. KLUIS/RAFFINAGE -> INDUSTRIËLE EINDVRAAG (stage product) — de pull
    { from: "ag-ex-sge", to: "ag-mkt-china-solar", value: 2600, mode: "rail", stage: "product",
      note: "De grootste pull: SGE-Shanghai -> de Chinese zonnecel-industrie. De dikste product-boog van de hele keten." },
    { from: "ag-ex-sge", to: "ag-mkt-china-elec", value: 900, mode: "rail", stage: "product",
      note: "SGE -> de Chinese elektronica-/EV-industrie (Shenzhen)." },
    { from: "ag-ref-china", to: "ag-mkt-china-solar", value: 1200, mode: "rail", stage: "product",
      note: "Binnenlands geraffineerd zilver direct de solar-lijn in — zonder tussenstop in de kluis." },
    { from: "ag-ex-lbma", to: "ag-mkt-india", value: 700, mode: "ship", stage: "product",
      via: ["wp-gibraltar", "wp-suez", "wp-rode-zee", "wp-bab", "ag-port-nhava"],
      note: "Londen -> India via Suez: sieraden, zilverwerk en steeds meer solar." },
    { from: "ag-ex-comex", to: "ag-mkt-us", value: 800, mode: "road", stage: "product",
      note: "COMEX -> de Amerikaanse industrie + munten, over land." },
    { from: "ag-ref-japan", to: "ag-mkt-japan-korea", value: 500, mode: "road", stage: "product",
      note: "Japans tech-zilver -> de eigen halfgeleider-/elektronica-industrie." },
    { from: "ag-ref-korea", to: "ag-mkt-china-solar", value: 600, mode: "ship", stage: "product",
      via: ["wp-taiwan"],
      note: "Koreaanse baren -> de Chinese solar-industrie (import onder het tekort)." },

    // === E. RECYCLING -> RAFFINAGE (stage erts, feedstock terug, always-on) ==
    { from: "ag-rec-eu", to: "ag-ref-aurubis", value: 500, mode: "road", stage: "erts",
      note: "Umicore-e-waste -> de Europese raffinage; zilver dat niet opnieuw gewonnen hoeft te worden." },
    { from: "ag-rec-japan", to: "ag-ref-japan", value: 400, mode: "road", stage: "erts",
      note: "Japanse urban mining -> Mitsubishi/Dowa." },
    { from: "ag-rec-us", to: "ag-mkt-us", value: 400, mode: "road", stage: "erts",
      note: "Amerikaans industrieel/fotografisch schroot terug de eigen industrieketen in." },
    { from: "ag-rec-india", to: "ag-mkt-india", value: 300, mode: "road", stage: "erts",
      note: "Indiaas sieraadschroot blijft binnen de eigen sieradenketen circuleren." },

    // === F. BEURSVOORRADEN (layer:"exchange" -> alleen met de toggle) ========
    // Het STRUCTURELE TEKORT getoond als voorraad die de kluizen verlaat richting
    // de fysieke (industriële) markt. Default uit.
    { from: "ag-ex-lbma", to: "ag-mkt-china-solar", value: 400, mode: "ship", stage: "product", layer: "exchange",
      via: ["wp-gibraltar", "wp-suez", "wp-rode-zee", "wp-bab", "wp-malakka", "wp-scs", "wp-taiwan"],
      note: "Bovengrondse Londense voorraad -> de Chinese solar-industrie: het gat tussen vraag en aanbod dichten." },
    { from: "ag-ex-comex", to: "ag-mkt-us", value: 300, mode: "road", stage: "product", layer: "exchange",
      note: "COMEX 'registered' voorraad -> de Amerikaanse industrie." },
    { from: "ag-ex-sge", to: "ag-mkt-china-solar", value: 500, mode: "rail", stage: "product", layer: "exchange",
      note: "De Shanghai-kluis loopt leeg richting de binnenlandse solar-vraag." },
  ],

  // ==========================================================================
  // SPANNINGEN — waar de zilverketen 'knijpt'. Anders dan de andere grondstoffen
  // is de knijp NIET geografisch (geen enkel chokepoint), maar structureel:
  // inelastisch bijproduct-aanbod tegenover een surgende, concentrerende vraag.
  // ==========================================================================
  tensions: [
    { id: "ag-t-byproduct", type: "structureel", title: "De bijproduct-paradox: aanbod dat niet luistert naar de prijs",
      lat: 30.0, lon: -60.0,
      nodes: ["ag-kghm", "ag-chile-cu", "ag-antamina", "ag-penasquito", "ag-cannington", "ag-sancristobal"],
      flows: ["ag-kghm>ag-ref-kghm", "ag-chile-cu>ag-ref-china", "ag-antamina>ag-ref-china"],
      metric: "~70-75% van al het zilver is bijproduct (lood/zink ~30% · koper ~23% · goud ~15%)",
      note: "De kern-'aha' van zilver. Slechts ~25-30% komt uit primaire zilvermijnen; de rest valt eruit bij het delven van zink, lood, koper en goud. Gevolg: het aanbod reageert nauwelijks op de zilverprijs — je kunt zilver niet opschalen zonder meer zink of koper te willen. De zilver-stippen op de kaart zitten letterlijk bovenop andermans mijnen. Géén winnings-trechter zoals China bij lithium of Zwitserland bij goud." },

    { id: "ag-t-solar", type: "concentratie", title: "De solar-pull: de energietransitie trekt zilver naar China",
      lat: 31.30, lon: 120.60,
      nodes: ["ag-mkt-china-solar", "ag-ex-sge", "ag-ref-china"],
      flows: ["ag-ex-sge>ag-mkt-china-solar", "ag-ref-china>ag-mkt-china-solar", "ag-ref-korea>ag-mkt-china-solar"],
      metric: "fotovoltaïsch ≈ 1/5 van de wereldvraag — de grootste én snelst groeiende post",
      note: "Waar het aanbod diffuus is, concentreert de vraag zich. Zilverpasta in zonnecellen is de snelst groeiende toepassing geworden, en de zonnecel-productie zit overweldigend in China. De dikste product-boog van de keten loopt dan ook van de Shanghai-kluis naar de Jiangsu/Zhejiang-solarcluster. De 'knijp' van zilver ligt niet in de grond maar in de fabriek." },

    { id: "ag-t-deficit", type: "structureel", title: "Het structurele tekort: de kluizen lopen leeg",
      lat: 45.0, lon: 0.0,
      nodes: ["ag-ex-lbma", "ag-ex-comex", "ag-ex-sge"],
      flows: ["ag-ex-lbma>ag-mkt-china-solar", "ag-ex-comex>ag-mkt-us", "ag-ex-sge>ag-mkt-china-solar"],
      metric: "meerjarig vraag > aanbod -> aftap van bovengrondse voorraden (LBMA/COMEX/SGE)",
      note: "Omdat het aanbod inelastisch is en de vraag surgt, is de markt al enkele jaren in tekort. Dat gat wordt niet gedicht door meer te mijnen (dat kan niet zomaar) maar door de bovengrondse kluisvoorraden af te tappen. Zet de beursvoorraden-toggle aan: de voorraad-nodes (Londen veruit grootst) met stromen die de kluizen uit richting de industrie lopen — het tekort visueel gemaakt." },

    { id: "ag-t-mexico", type: "concentratie", title: "Mexico: winning én raffinage in één land",
      lat: 24.5, lon: -102.5,
      nodes: ["ag-fresnillo", "ag-penasquito", "ag-ref-penoles"],
      flows: ["ag-fresnillo>ag-ref-penoles", "ag-penasquito>ag-ref-penoles", "ag-ref-penoles>ag-ex-comex"],
      metric: "Mexico #1 (~25% winning) · Peñoles (Torreón) = grootste zilverraffinaderij ter wereld",
      note: "Het enige stuk van de keten dat wél samenknijpt (buiten China). Mexico is de grootste producent, mét Fresnillo (grootste primaire zilverbedrijf) én Peñoles (grootste raffinaderij) — één land draagt zowel de winning als de raffinage van de niet-Chinese keten. Van Torreón waaieren de baren uit naar COMEX en Londen." },

    { id: "ag-t-comex", type: "beleid", title: "COMEX/LBMA: registered vs. eligible + de 2021 squeeze",
      lat: 45.5, lon: -37.0,
      nodes: ["ag-ex-lbma", "ag-ex-comex"],
      flows: ["ag-ex-lbma>ag-ex-comex", "ag-ref-penoles>ag-ex-comex"],
      metric: "'registered' (leverbaar) « 'eligible' (gekluisd) · 2021: r/WallStreetBets 'silver squeeze'",
      note: "De papier-versus-fysiek-nuance. Van al het zilver in de COMEX-magazijnen is maar een deel 'registered' (daadwerkelijk leverbaar tegen futures); de rest is 'eligible' (gekluisd, niet leverbaar). In 2021 probeerde een online beweging die kloof uit te buiten ('silver squeeze') — wat een zichtbare fysieke verschuiving van Londen naar New York op gang bracht. De beursprijs is niet hetzelfde als het metaal in de kluis." },

    { id: "ag-t-nochoke", type: "knelpunt", title: "Geen winnings-knelpunt — de knijp is de vraag",
      lat: 3.0, lon: 100.6,
      nodes: ["wp-malakka", "wp-suez", "wp-taiwan"],
      flows: ["ag-ex-lbma>ag-ex-sge", "ag-ex-lbma>ag-mkt-india"],
      metric: "derde grondstof (na nikkel/olie) die volledig op de bestaande routekaart draait — 0 nieuwe chokepoints",
      note: "Anders dan lithium/koper (China-raffinage), goud (Zwitserland) of uranium (Russische verrijking) heeft zilver géén enkel geografisch knelpunt in de keten. Het reist als gewoon industrieel metaal over de bestaande zee/land-routes (Suez, Malakka, de Pacific). Dát is de boodschap: de kwetsbaarheid van zilver is niet een zeestraat maar de combinatie van inelastisch bijproduct-aanbod en een surgende, in China concentrerende vraag." },
  ],
});
