// ============================================================================
// URANIUM (U) — volledig uitgewerkte module. Peiljaar ±2023/24.
// Cijfers indicatief/afgerond, o.b.v. WNA Nuclear Fuel Report, IAEA/OECD-NEA
// "Red Book", USGS MCS en bedrijfsrapportages. Eenheid overal: tU/jaar (ton
// uranium-inhoud), zodat de hele keten optelbaar blijft. Zie ../design/uranium.md.
//
// DE VORM VAN URANIUM (bewust ANDERS dan de batterijmetalen):
//   Bij lithium/koper/REE zit de knijp bij de RAFFINAGE (China/Indonesië). Bij
//   uranium ligt de flessenhals TWEE stappen verderop en in een VIJANDIGE staat:
//   winning breed verspreid, maar ~44% van de wereldVERRIJKING (SWU) in RUSLAND.
//   Dat is een institutionele knijp zoals de Zwitserse goudraffinage — geen
//   zeestraat, wél een keiharde afhankelijkheid.
//
// DE 4-STAPS KETEN, gemapt op de 3 bestaande stages:
//   erts       = winning -> yellowcake (U3O8) + CONVERSIE -> UF6. Nog "feed",
//                niet verrijkt -> dof/donker.
//   raffinaat  = VERRIJKING -> verrijkt UF6. De flessenhals, volle uraankleur.
//   product    = SPLIJTSTOFFABRICAGE -> brandstofelementen -> reactor (markt).
//
// DRIE DINGEN DIE DE ATLAS NOG NIET HAD:
//   1. Twee LANDLOCKED-routeringen. Kazachstan (~43% van de winning!) exporteert
//      of per spoor door Rusland, of via de nieuwe TRANS-KASPISCHE route (Aktau ->
//      Kaspische Zee -> Bakoe -> Poti -> Bosporus) om Rusland heen. Niger (~4%,
//      verstoord na de coup van 2023) moet over land naar Cotonou (Benin).
//   2. De VVER-brandstof-LOCK-IN: Rusland (TVEL) levert splijtstof voor zijn eigen
//      reactorontwerpen in Midden-Europa (Paks, Dukovany, Kozloduy) — eenrichting.
//   3. De CANDU-UITZONDERING: Canadese zwaarwaterreactoren draaien op NATUURLIJK
//      uranium en slaan de verrijking (en dus de Russische knijp) volledig over.
//
// TRANSPORT is schip + land (kleine, hoogwaardige vracht in verzegelde vaten/
// cilinders): hergebruikt de zee-A*/land-A*-routes en de scheeps-voyages. Géén
// nieuwe render-modus. De Kaspische oversteek en de Dardanellen zijn nieuwe
// vaarpunten in _chokepoints.js (alleen uranium gebruikt ze).
//
// OPTIONELE "MILITAIRE KRINGLOOP"-LAAG (type:"military" / flow.layer:"secondary",
// filter showMilitary) — de vijfde optionele toggle-laag (na goud-CB, koper-exchange,
// REE-recycle, olie-reserve), default UIT. Down-geblend wapen-HEU ("Megatons to
// Megawatts"), tails-herverrijking en strategische reserves (US DOE / Rosatom):
// secundair aanbod dat het gat vult tussen winning (~60 kt) en reactorbehoefte (~65 kt).
// Chip alleen bij uranium; rode "kringloop"-marker (grootte ∝ √voorraad).
// ============================================================================

REGISTER({
  id: "uranium",
  name: "Uranium",
  symbol: "U",
  color: "#A3E635",
  flowColor: "#BEF264",
  detail: "uitgewerkt",
  unit: "tU/jaar (indicatief)",
  blurb: "Splijtstof voor kernenergie. Winning breed verspreid (Kazachstan ~43%, " +
    "maar landlocked) — de flessenhals ligt twee stappen verderop: ~44% van de " +
    "wereldverrijking staat in Rusland. Kazachstan exporteert door Rusland óf via " +
    "de Trans-Kaspische route eromheen; Russische splijtstof houdt Midden-Europa's " +
    "reactoren in de greep.",

  nodes: [
    // ================================================================== MIJNEN
    // Winning -> yellowcake (U3O8). `share` = % van de wereldmijnproductie
    // (≈ 60.000 tU/jaar; reactorbehoefte ≈ 65.000 tU, het gat vullen voorraden).
    { id: "u-mine-kz", type: "mine", name: "Kazachstan (ISR)", country: "Kazachstan",
      lat: 44.00, lon: 67.80, share: 43, tier: 1, operator: "Kazatomprom (+ JV's)",
      status: "actief", capacity: "≈ 21.000 tU/j",
      note: "Veruit de grootste producent: in-situ-loging (ISR) in de Chu-Sarysu- en Syrdarja-bekkens. LANDLOCKED — het yellowcake moet fysiek langs of om Rusland heen. JV's met Cameco, Orano, CGN en Rosatom." },
    { id: "u-mine-ca", type: "mine", name: "Athabasca (Cigar Lake/McArthur)", country: "Canada",
      lat: 58.10, lon: -104.50, share: 15, tier: 1, operator: "Cameco / Orano",
      status: "actief", capacity: "≈ 9.000 tU/j",
      note: "Het rijkste uraanerts ter wereld (Saskatchewan). Voedt de conversie in Port Hope én de Canadese CANDU-reactoren (natuurlijk uranium)." },
    { id: "u-mine-na", type: "mine", name: "Husab / Rössing", country: "Namibië",
      lat: -22.60, lon: 15.10, share: 11, tier: 1, operator: "CGN / CNNC (China)",
      status: "actief", capacity: "≈ 6.500 tU/j",
      note: "Twee grote woestijnmijnen bij Swakopmund — vrijwel volledig in CHINEES bezit. Export via Walvis Bay, bestemming Chinese conversie/verrijking." },
    { id: "u-mine-au", type: "mine", name: "Olympic Dam", country: "Australië",
      lat: -30.44, lon: 136.88, share: 9, tier: 2, operator: "BHP",
      status: "actief", capacity: "≈ 5.000 tU/j",
      note: "Uranium als medeproduct van koper/goud (Zuid-Australië). Australië verrijkt zelf niet — het erts gaat naar Westerse verrijkers." },
    { id: "u-mine-uz", type: "mine", name: "Navoi (Kyzylkum)", country: "Oezbekistan",
      lat: 41.50, lon: 64.50, share: 7, tier: 2, operator: "Navoiuran",
      status: "actief", capacity: "≈ 3.500 tU/j",
      note: "ISR in de Kyzylkum-woestijn; ook landlocked, historisch geëxporteerd via Rusland." },
    { id: "u-mine-ru", type: "mine", name: "Priargunsky", country: "Rusland",
      lat: 50.10, lon: 118.00, share: 5, tier: 2, operator: "Rosatom (ARMZ)",
      status: "actief", capacity: "≈ 2.500 tU/j",
      note: "Bij Krasnokamensk (Transbaikal); Ruslands belangrijkste eigen mijn, voedt de binnenlandse conversie in Seversk." },
    { id: "u-mine-ne", type: "mine", name: "Arlit (SOMAIR)", country: "Niger",
      lat: 18.74, lon: 7.39, share: 4, tier: 2, operator: "Orano",
      status: "actief", capacity: "≈ 2.000 tU/j (verstoord)",
      note: "LANDLOCKED in de Sahara; historisch per truck ±1.200 km naar Cotonou (Benin). Na de coup van 2023 en de breuk met Frankrijk grotendeels stilgevallen." },
    { id: "u-mine-cn", type: "mine", name: "China (CNNC)", country: "China",
      lat: 41.80, lon: 111.00, share: 2, tier: 3, operator: "CNNC",
      status: "actief", capacity: "≈ 1.500 tU/j",
      note: "Bescheiden binnenlandse winning (Binnen-Mongolië/Xinjiang) — klein t.o.v. China's snelgroeiende reactorvloot, die vooral op import draait." },
    { id: "u-mine-us", type: "mine", name: "Wyoming (ISR, heropstart)", country: "VS",
      lat: 42.90, lon: -107.50, tier: 3, operator: "Cameco/UEC e.a.", status: "project",
      potential: "heropstartende ISR-productie",
      note: "De VS wil de eigen mijnbouw heropbouwen om minder afhankelijk te zijn van Russische verrijking. Voorlopig klein." },

    // ============================================= CONVERSIE (U3O8 -> UF6)
    // Handvol fabrieken wereldwijd; nog "feed" (stage erts), niet verrijkt.
    { id: "u-conv-ca", type: "refinery", name: "Port Hope (conversie)", country: "Canada",
      lat: 43.95, lon: -78.29, tier: 2, operator: "Cameco",
      note: "Een van de weinige commerciële conversiefabrieken ter wereld (U3O8 -> UF6), aan het Ontariomeer." },
    { id: "u-conv-fr", type: "refinery", name: "Malvési (conversie)", country: "Frankrijk",
      lat: 43.19, lon: 2.99, tier: 2, operator: "Orano", coastal: true,
      note: "Orano-conversie bij Narbonne (U3O8 -> UF4 -> UF6), vlak bij de Middellandse Zee; levert door aan de verrijking in Tricastin." },
    { id: "u-conv-ru", type: "refinery", name: "Seversk (conversie)", country: "Rusland",
      lat: 56.60, lon: 84.89, tier: 3, operator: "Rosatom/TVEL",
      note: "Russische conversie (Tomsk); feed voor de Russische verrijking." },

    // ================================ VERRIJKING (UF6 -> verrijkt UF6) = DE KNIJP
    // stage raffinaat: de waarde-toevoegende stap waar de wereld op vastloopt.
    { id: "u-enr-ru", type: "refinery", name: "Novouralsk (Rosatom/TVEL)", country: "Rusland",
      lat: 57.25, lon: 60.08, tier: 1, operator: "Rosatom (TVEL)",
      capacity: "~44% van de wereld-SWU",
      note: "DE FLESSENHALS. Rusland beheerst bijna de helft van alle verrijkingscapaciteit ter wereld (Novouralsk/Zelenogorsk/Seversk/Angarsk). Wie geen alternatief heeft, hangt hieraan vast — de uraan-Ticino." },
    { id: "u-enr-nl", type: "refinery", name: "Urenco Almelo", country: "Nederland",
      lat: 52.35, lon: 6.66, tier: 1, operator: "Urenco",
      note: "Het hart van de Westerse (niet-Russische) verrijking: het oorspronkelijke Urenco-centrifugecomplex. Samen met Gronau, Capenhurst en Eunice de tegenhanger van Rosatom." },
    { id: "u-enr-fr", type: "refinery", name: "Georges Besse II (Tricastin)", country: "Frankrijk",
      lat: 44.33, lon: 4.73, tier: 2, operator: "Orano",
      note: "De Franse centrifugeverrijking; met Urenco de ruggengraat van de Europese onafhankelijkheid." },
    { id: "u-enr-us", type: "refinery", name: "Urenco USA (Eunice, NM)", country: "VS",
      lat: 32.44, lon: -103.13, tier: 2, operator: "Urenco",
      note: "De enige commerciële verrijkingsfabriek van de VS. Te klein om de Amerikaanse reactorvloot te dekken -> de VS kocht jarenlang Russische SWU (tot het verbod van 2024)." },
    { id: "u-enr-cn", type: "refinery", name: "CNNC Lanzhou", country: "China",
      lat: 36.06, lon: 103.79, tier: 3, operator: "CNNC",
      note: "China's binnenlandse verrijking; groeit mee met de eigen reactorvloot. Verwerkt o.a. Namibisch (Chinees) uranium." },

    // ================================ SPLIJTSTOFFABRICAGE (verrijkt U -> elementen)
    // stage product: verrijkt uranium -> brandstofelementen -> reactor.
    { id: "u-fab-us", type: "refinery", name: "Westinghouse (Columbia, SC)", country: "VS",
      lat: 33.93, lon: -80.93, tier: 2, operator: "Westinghouse", coastal: true,
      note: "Grote Amerikaanse splijtstoffabriek; Westinghouse kwalificeert óók VVER-brandstof om de Russische lock-in in Midden-Europa te breken. (coastal: het down-geblende Russische LEU landde hier via de Atlantische Oceaan — Megatons to Megawatts.)" },
    { id: "u-fab-fr", type: "refinery", name: "Framatome (Romans)", country: "Frankrijk",
      lat: 45.05, lon: 5.05, tier: 2, operator: "Framatome",
      note: "Franse splijtstofelementen voor de eigen (grootste in Europa) reactorvloot." },
    { id: "u-fab-ru", type: "refinery", name: "TVEL (Elektrostal)", country: "Rusland",
      lat: 55.79, lon: 38.45, tier: 1, operator: "Rosatom (TVEL)",
      note: "Russische splijtstoffabricage — en het VVER-MONOPOLIE: elementen op maat voor Russische reactorontwerpen in binnen- en buitenland." },
    { id: "u-fab-se", type: "refinery", name: "Westinghouse (Västerås)", country: "Zweden",
      lat: 59.62, lon: 16.55, tier: 3, operator: "Westinghouse",
      note: "Zweedse fabriek waar Westinghouse zijn niet-Russische VVER-brandstof maakt — de sleutel om Midden-Europa los te weken van TVEL." },

    // ================================================= REACTOREN / CONSUMPTIE
    { id: "u-mkt-us", type: "market", name: "VS (kernvloot)", country: "VS",
      lat: 35.50, lon: -84.00, tier: 1,
      note: "Grootste reactorvloot ter wereld (~93 reactoren). Grote SWU-behoefte; jarenlang deels met Russische verrijking gevuld." },
    { id: "u-mkt-fr", type: "market", name: "Frankrijk (kernvloot)", country: "Frankrijk",
      lat: 47.50, lon: 2.50, tier: 1,
      note: "~56 reactoren; ~70% van de Franse stroom. Vrijwel gesloten eigen keten (Orano-conversie/verrijking, Framatome-brandstof)." },
    { id: "u-mkt-cn", type: "market", name: "China (kust)", country: "China",
      lat: 30.50, lon: 121.00, tier: 1, coastal: true,
      note: "Snelst groeiende reactorvloot ter wereld; bouwt tientallen reactoren tegelijk. Zuigt uranium en verrijkingsdiensten aan." },
    { id: "u-mkt-ru", type: "market", name: "Rusland (kernvloot)", country: "Rusland",
      lat: 55.00, lon: 40.00, tier: 2,
      note: "Eigen reactoren op eigen brandstof; Rosatom is bovendien de grootste exporteur van reactoren én splijtstof ter wereld." },
    { id: "u-mkt-ca", type: "market", name: "Ontario (CANDU)", country: "Canada",
      lat: 44.30, lon: -77.60, tier: 2,
      note: "CANDU-zwaarwaterreactoren (Bruce/Darlington) draaien op NATUURLIJK uranium — géén verrijking nodig. De uitzondering die de Russische knijp volledig overslaat." },
    { id: "u-vver-hu", type: "market", name: "Paks (VVER)", country: "Hongarije",
      lat: 46.57, lon: 18.85, tier: 2,
      note: "Russisch VVER-ontwerp; draait op TVEL-brandstof en breidt uit met Rosatoms Paks II. Symbool van de Midden-Europese lock-in." },
    { id: "u-vver-cz", type: "market", name: "Dukovany (VVER)", country: "Tsjechië",
      lat: 49.09, lon: 16.15, tier: 3,
      note: "VVER-reactoren die overstappen op Westinghouse-brandstof — de eerste barsten in de Russische lock-in." },
    { id: "u-vver-bg", type: "market", name: "Kozloduy (VVER)", country: "Bulgarije",
      lat: 43.75, lon: 23.77, tier: 3,
      note: "Bulgaarse VVER-vloot; kwalificeert eveneens Westinghouse-brandstof als alternatief voor TVEL." },

    // =================================================== HAVENS & CORRIDORS
    { id: "u-port-aktau", type: "port", name: "Aktau", country: "Kazachstan",
      lat: 43.65, lon: 51.16, tier: 2,
      note: "Kazachstans Kaspische haven — het beginpunt van de Trans-Kaspische route die Rusland omzeilt." },
    { id: "u-port-baku", type: "port", name: "Bakoe", country: "Azerbeidzjan",
      lat: 40.37, lon: 49.85, tier: 2,
      note: "Aanlanding aan de westkant van de Kaspische Zee; verder per spoor door de Kaukasus (Bakoe-Tbilisi-corridor)." },
    { id: "u-port-poti", type: "port", name: "Poti", country: "Georgië",
      lat: 42.15, lon: 41.67, tier: 2,
      note: "Georgische Zwarte-Zeehaven; hier gaat de Trans-Kaspische lading het schip op richting de Bosporus en Europa." },
    { id: "u-port-stpetersburg", type: "port", name: "St.-Petersburg", country: "Rusland",
      lat: 59.90, lon: 30.30, tier: 3,
      note: "De historische uitgang voor Centraal-Aziatisch uranium naar het Westen — over de Oostzee. Precies de route die de Trans-Kaspische corridor probeert te de-risken." },
    { id: "u-port-rotterdam", type: "port", name: "Rotterdam", country: "Nederland",
      lat: 51.95, lon: 4.14, tier: 3,
      note: "Aanlanding voor de Europese verrijking (Almelo/Tricastin); laatste stuk over land." },
    { id: "u-port-cotonou", type: "port", name: "Cotonou", country: "Benin",
      lat: 6.35, lon: 2.42, tier: 3,
      note: "De zeehaven waar het Nigerese uranium na ±1.200 km over land aankwam — richting de Franse conversie." },
    { id: "u-port-walvis", type: "port", name: "Walvis Bay", country: "Namibië",
      lat: -22.95, lon: 14.50, tier: 3,
      note: "Atlantische uitgang voor het Namibische (Chinees-eigen) uranium." },
    { id: "u-port-adelaide", type: "port", name: "Adelaide", country: "Australië",
      lat: -34.85, lon: 138.50, tier: 3,
      note: "Zuid-Australische uitgang voor Olympic Dam-uranium richting de Westerse verrijkers." },
    { id: "u-port-china", type: "port", name: "Shanghai (Yangshan)", country: "China",
      lat: 30.62, lon: 122.07, tier: 3,
      note: "Invoerpoort voor geïmporteerd uranium; vandaar per spoor het binnenland in (o.a. Lanzhou)." },

    // ============================ MILITAIRE KRINGLOOP (optionele toggle-laag)
    // type "military" -> alleen zichtbaar met de militaire-kringloop-toggle.
    // `stock` (tU-equivalent) = secundaire voorraad -> node-grootte. NUANCE: dit is
    // GÉÉN mijnbouw maar secundair aanbod (down-blend/tails/reserves) dat het gat
    // tussen winning (~60 kt) en reactorbehoefte (~65 kt) vult.
    { id: "u-mil-ru-heu", type: "military", name: "Down-blending wapen-HEU (Rosatom)", country: "Rusland",
      lat: 59.40, lon: 28.50, stock: 500, tier: 2, coastal: true,
      note: "De Russische down-blending van hoogverrijkt wapen-uranium (HEU) tot reactor-LEU. Het hart van 'Megatons to Megawatts' (1993–2013): kernkoppen die als reactorbrandstof eindigden. Export historisch over de Oostzee naar het Westen." },
    { id: "u-mil-ru-tails", type: "military", name: "Tails-herverrijking (Rosatom)", country: "Rusland",
      lat: 56.85, lon: 60.60, stock: 300, tier: 3,
      note: "Rusland herverrijkt de verarmde 'tails' (het afvalstroompje van de verrijking) opnieuw tot bruikbare feed — een secundaire bron die alleen bij grote, goedkope centrifugecapaciteit rendabel is. Ook Westerse tails gingen hierheen." },
    { id: "u-mil-us-doe", type: "military", name: "US DOE (down-blend + reserve)", country: "VS",
      lat: 33.35, lon: -81.65, stock: 250, tier: 3,
      note: "Het Amerikaanse ministerie van Energie down-blendt eigen overtollig militair HEU en houdt een strategische uraniumvoorraad (o.a. Savannah River) — een binnenlandse buffer los van de Russische keten." },
    { id: "u-mil-us-reserve", type: "military", name: "VS strategische U-reserve", country: "VS",
      lat: 35.93, lon: -84.31, stock: 150, tier: 3,
      note: "De nieuwe Amerikaanse strategische uraniumreserve (aangekondigd 2020): binnenlands gewonnen en verrijkt uranium als buffer tegen de afhankelijkheid van Russische SWU en HALEU." },
  ],

  // ==========================================================================
  // STROMEN — value in tU/jaar (indicatief). stage bepaalt kleur/hoogte:
  // erts (yellowcake/UF6-feed) dof -> raffinaat (verrijkt) vol -> product (splijtstof)
  // licht. `via` = echte route langs havens (u-port-*) en knelpunten (wp-*).
  //
  //  A) KAZACHSTAN — de twee concurrerende exportroutes (kern van dit ontwerp)
  //  B) CANADA — conversie + de CANDU-uitzondering (natuurlijk uranium)
  //  C) NAMIBIË/AUSTRALIË/NIGER — erts naar verrijking (China / West / Frankrijk)
  //  D) CONVERSIE -> VERRIJKING (feed naar de flessenhals)
  //  E) VERRIJKING -> SPLIJTSTOF (het verrijkte product)
  //  F) SPLIJTSTOF -> REACTOREN + de VVER-lock-in
  //  G) CHINA — binnenlandse keten
  // ==========================================================================
  flows: [
    // === A. KAZACHSTAN: DE TWEE ROUTES ======================================
    { from: "u-mine-kz", to: "u-enr-ru", value: 9000, mode: "rail", stage: "erts",
      note: "Kazachs uranium per spoor de grens over naar de Russische verrijking. De korte, historische afhankelijkheid: veel Kazatomprom-productie loopt via Rosatom." },
    // Trans-Kaspische route (om Rusland heen) — opgeknipt per modus/leg:
    { from: "u-mine-kz", to: "u-port-aktau", value: 6000, mode: "rail", stage: "erts",
      note: "Trans-Kaspisch, leg 1: per spoor van de ISR-velden naar de Kaspische haven Aktau." },
    { from: "u-port-aktau", to: "u-port-baku", value: 6000, mode: "ship", stage: "erts",
      via: ["wp-kaspisch-n", "wp-kaspisch-m", "wp-kaspisch-z"],
      note: "Trans-Kaspisch, leg 2: per schip de Kaspische Zee over naar Bakoe. De ingesloten zee is de kern van de de-risking om Rusland heen." },
    { from: "u-port-baku", to: "u-port-poti", value: 6000, mode: "rail", stage: "erts",
      note: "Trans-Kaspisch, leg 3: per spoor door de Kaukasus (Bakoe-Tbilisi-corridor) naar de Zwarte-Zeehaven Poti." },
    { from: "u-port-poti", to: "u-enr-nl", value: 6000, mode: "ship", stage: "erts",
      via: ["wp-bosporus", "wp-dardanellen", "wp-gibraltar", "u-port-rotterdam"],
      note: "Trans-Kaspisch, leg 4: Poti -> Zwarte Zee -> Bosporus/Dardanellen -> Middellandse Zee -> Gibraltar -> Rotterdam -> Urenco Almelo. De volledige omweg om Rusland heen." },
    // Historische Rusland-transitroute naar het Westen (die de Trans-Kaspische de-riskt):
    { from: "u-mine-kz", to: "u-port-stpetersburg", value: 4000, mode: "rail", stage: "erts",
      note: "De andere weg naar het Westen: per spoor dwars door Rusland naar St.-Petersburg. Kort, maar volledig afhankelijk van Russische doorvoer." },
    { from: "u-port-stpetersburg", to: "u-enr-nl", value: 4000, mode: "ship", stage: "erts",
      via: ["wp-deense-straten", "u-port-rotterdam"],
      note: "St.-Petersburg -> Oostzee -> Deense Straten -> Rotterdam -> Almelo. Dit is de route die door de sancties politiek kwetsbaar werd — vandaar de Trans-Kaspische omweg." },

    // === B. CANADA: CONVERSIE + DE CANDU-UITZONDERING =======================
    { from: "u-mine-ca", to: "u-conv-ca", value: 6000, mode: "rail", stage: "erts",
      note: "Athabasca-yellowcake -> conversie in Port Hope (over land, binnen Canada)." },
    { from: "u-mine-ca", to: "u-mkt-ca", value: 2500, mode: "rail", stage: "product",
      note: "DE UITZONDERING: Canadees natuurlijk uranium gaat rechtstreeks naar de CANDU-reactoren — géén verrijking, dus geen Russische knijp." },
    { from: "u-conv-ca", to: "u-enr-us", value: 3500, mode: "rail", stage: "erts",
      note: "Canadees UF6 -> Urenco USA (Eunice): grensoverschrijdend over land, om de Westerse verrijking te voeden." },

    // === C. NAMIBIË / AUSTRALIË / NIGER -> VERRIJKING ========================
    { from: "u-mine-na", to: "u-port-walvis", value: 6500, mode: "rail", stage: "erts",
      note: "Namibisch yellowcake -> Walvis Bay (kort, over land)." },
    { from: "u-port-walvis", to: "u-enr-cn", value: 6500, mode: "ship", stage: "erts",
      via: ["wp-kaap", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "u-port-china"],
      note: "Namibië -> China: om Kaap de Goede Hoop, door Malakka naar Shanghai, dan per spoor naar de verrijking in Lanzhou. Chinees uranium naar de Chinese keten." },
    { from: "u-mine-au", to: "u-port-adelaide", value: 5000, mode: "rail", stage: "erts",
      note: "Olympic Dam -> Adelaide (over land)." },
    { from: "u-port-adelaide", to: "u-enr-nl", value: 5000, mode: "ship", stage: "erts",
      via: ["wp-kaap", "u-port-rotterdam"],
      note: "Australisch uranium -> Europa: over de zuidelijke Indische Oceaan, om Kaap de Goede Hoop, naar Rotterdam/Almelo. Australië verrijkt niet zelf." },
    { from: "u-mine-ne", to: "u-port-cotonou", value: 2000, mode: "road", stage: "erts",
      note: "Niger -> Cotonou: ±1.200 km per truck door de Sahel naar de kust. De tweede landlocked-corridor — en sinds de coup grotendeels stilgevallen." },
    { from: "u-port-cotonou", to: "u-conv-fr", value: 2000, mode: "ship", stage: "erts",
      via: ["wp-gibraltar"],
      note: "Cotonou -> de Atlantische Oceaan op, door Gibraltar naar de Franse conversie in Malvési." },

    // === D. CONVERSIE -> VERRIJKING (feed naar de flessenhals) ===============
    { from: "u-conv-fr", to: "u-enr-fr", value: 5000, mode: "rail", stage: "erts",
      note: "Malvési-UF6 -> verrijking in Tricastin (over land, Zuid-Frankrijk)." },
    { from: "u-mine-ru", to: "u-conv-ru", value: 2500, mode: "rail", stage: "erts",
      note: "Priargunsky-yellowcake -> Russische conversie in Seversk." },
    { from: "u-conv-ru", to: "u-enr-ru", value: 2500, mode: "rail", stage: "erts",
      note: "Seversk-UF6 -> Russische verrijking (Novouralsk)." },
    { from: "u-mine-uz", to: "u-enr-ru", value: 3500, mode: "rail", stage: "erts",
      note: "Oezbeeks uranium -> Russische verrijking: nog een landlocked-buur die via Rusland loopt." },

    // === E. VERRIJKING -> SPLIJTSTOF (het verrijkte product, raffinaat) ======
    { from: "u-enr-ru", to: "u-fab-ru", value: 6000, mode: "rail", stage: "raffinaat",
      note: "Verrijkt Russisch UF6 -> TVEL-splijtstoffabricage (Elektrostal)." },
    { from: "u-enr-nl", to: "u-fab-se", value: 3500, mode: "rail", stage: "raffinaat",
      note: "Urenco Almelo -> Westinghouse Västerås: over land, over de Öresundbrug naar Zweden." },
    { from: "u-enr-nl", to: "u-fab-fr", value: 2500, mode: "rail", stage: "raffinaat",
      note: "Almelo -> Framatome Romans (Frankrijk)." },
    { from: "u-enr-fr", to: "u-fab-fr", value: 4000, mode: "rail", stage: "raffinaat",
      note: "Tricastin -> Framatome Romans (kort, Zuid-Frankrijk)." },
    { from: "u-enr-us", to: "u-fab-us", value: 3500, mode: "rail", stage: "raffinaat",
      note: "Urenco USA (Eunice) -> Westinghouse Columbia — de binnenlandse Amerikaanse keten." },

    // === F. SPLIJTSTOF -> REACTOREN + DE VVER-LOCK-IN (product) ==============
    { from: "u-fab-us", to: "u-mkt-us", value: 4000, mode: "rail", stage: "product",
      note: "Amerikaanse splijtstofelementen -> de eigen reactorvloot." },
    { from: "u-fab-fr", to: "u-mkt-fr", value: 5500, mode: "rail", stage: "product",
      note: "Franse splijtstof -> de Franse reactoren." },
    { from: "u-fab-ru", to: "u-mkt-ru", value: 3500, mode: "rail", stage: "product",
      note: "Russische splijtstof -> de eigen reactoren." },
    // De VVER-lock-in: Rusland -> Midden-Europa (eenrichting)
    { from: "u-fab-ru", to: "u-vver-hu", value: 1500, mode: "rail", stage: "product",
      note: "TVEL -> Paks: Russische brandstof voor een Russisch reactorontwerp — de Midden-Europese lock-in, dwars door Oekraïne/Wit-Rusland over land." },
    { from: "u-fab-ru", to: "u-vver-cz", value: 1000, mode: "rail", stage: "product",
      note: "TVEL -> Dukovany: dezelfde afhankelijkheid, nu onder druk." },
    { from: "u-fab-ru", to: "u-vver-bg", value: 1000, mode: "rail", stage: "product",
      note: "TVEL -> Kozloduy." },
    // Westinghouse breekt in (de-risking):
    { from: "u-fab-se", to: "u-vver-cz", value: 900, mode: "rail", stage: "product",
      note: "Westinghouse (Västerås) -> Dukovany: niet-Russische VVER-brandstof — de eerste barst in de lock-in." },
    { from: "u-fab-se", to: "u-vver-bg", value: 700, mode: "rail", stage: "product",
      note: "Westinghouse -> Kozloduy: Bulgarije weg van TVEL." },

    // === G. CHINA — binnenlandse keten ======================================
    { from: "u-mine-cn", to: "u-enr-cn", value: 1500, mode: "rail", stage: "erts",
      note: "Chinees binnenlands uranium -> CNNC-verrijking (Lanzhou)." },
    { from: "u-enr-cn", to: "u-mkt-cn", value: 6000, mode: "rail", stage: "product",
      note: "Verrijkt + gefabriceerd -> de Chinese kustreactoren. China's vraag overtreft de eigen winning ruimschoots." },

    // === Projecten (gepland) ================================================
    { from: "u-mine-us", to: "u-enr-us", value: 1500, mode: "rail", stage: "erts",
      status: "gepland",
      note: "Gepland: heropstartende Amerikaanse ISR-mijnbouw -> Urenco USA, om de eigen keten te sluiten en de Russische SWU-afhankelijkheid af te bouwen." },

    // === H. MILITAIRE KRINGLOOP (layer:"secondary" -> alleen met de toggle) ===
    // Secundair aanbod: down-geblend wapen-HEU, tails-herverrijking, reserves.
    { from: "u-mil-ru-heu", to: "u-fab-us", value: 400, mode: "ship", stage: "raffinaat", layer: "secondary",
      via: ["wp-deense-straten"],
      note: "'Megatons to Megawatts' (1993–2013): Russisch down-geblend wapen-HEU als LEU over de Oostzee en de Atlantische Oceaan naar de Amerikaanse splijtstofketen — twee decennia lang ~10% van de Amerikaanse kernstroom. Beëindigd in 2013." },
    { from: "u-mil-ru-heu", to: "u-mkt-ru", value: 200, mode: "rail", stage: "product", layer: "secondary",
      note: "Rusland down-blendt óók voor de eigen reactoren: overtollig militair HEU dat als binnenlandse reactorbrandstof eindigt." },
    { from: "u-mil-ru-tails", to: "u-enr-ru", value: 300, mode: "rail", stage: "erts", layer: "secondary",
      note: "Herverrijkte tails terug de verrijking in als goedkope feed — een secundaire kringloop die Ruslands enorme centrifugecapaciteit benut." },
    { from: "u-mil-us-doe", to: "u-mkt-us", value: 250, mode: "rail", stage: "product", layer: "secondary",
      note: "Down-geblend Amerikaans militair HEU + DOE-voorraad -> de eigen reactorvloot, over land." },
    { from: "u-mil-us-reserve", to: "u-mkt-us", value: 150, mode: "rail", stage: "product", layer: "secondary",
      note: "De strategische reserve als buffer richting de reactoren — geen mijnbouw, wél leveringszekerheid." },
  ],

  // ==========================================================================
  // SPANNINGEN — waar de uraniumketen knijpt. Verwijst naar de universele
  // knelpuntenlijst (wp-*). flows-verwijzing: "from-id>to-id".
  // ==========================================================================
  tensions: [
    { id: "u-t-verrijking", type: "concentratie", title: "Verrijking: ~44% in Rusland",
      lat: 57.25, lon: 60.08,
      nodes: ["u-enr-ru", "u-enr-nl", "u-enr-fr", "u-enr-us"],
      flows: ["u-mine-kz>u-enr-ru", "u-mine-uz>u-enr-ru", "u-conv-ru>u-enr-ru"],
      metric: "winning top-1 (Kazachstan) ≈ 43% · verrijking top-1 (Rusland) ≈ 44% SWU",
      note: "De kern van uranium: de kwetsbaarheid zit niet bij het graven maar TWEE stappen verderop, bij de verrijking — en bijna de helft daarvan staat in Rusland. Een institutionele knijp zonder zeestraat, zoals de Zwitserse goudraffinage: wie er niet omheen kan (Urenco/Orano/CNNC), hangt vast aan Rosatom." },

    { id: "u-t-kaspisch", type: "knelpunt", title: "Kazachstan: landlocked, om Rusland heen",
      lat: 42.00, lon: 50.70,
      nodes: ["u-mine-kz", "u-port-aktau", "u-port-baku", "u-port-poti", "u-port-stpetersburg"],
      flows: ["u-mine-kz>u-enr-ru", "u-mine-kz>u-port-aktau", "u-port-aktau>u-port-baku",
              "u-port-baku>u-port-poti", "u-mine-kz>u-port-stpetersburg"],
      metric: "~43% van de wereldwinning — maar zonder eigen zeehaven",
      note: "De grootste uraniumproducent ter wereld heeft geen kust. Zijn erts moet óf per spoor door Rusland (kort, maar afhankelijk), óf via de nieuwe Trans-Kaspische route eromheen: Aktau -> Kaspische Zee -> Bakoe -> de Kaukasus -> Poti -> Bosporus -> Europa. Twee zichtbaar concurrerende bogen, en de keuze ertussen is pure geopolitiek." },

    { id: "u-t-vver", type: "beleid", title: "VVER-lock-in: Russische brandstof in de EU",
      lat: 46.57, lon: 18.85,
      nodes: ["u-fab-ru", "u-vver-hu", "u-vver-cz", "u-vver-bg", "u-fab-se"],
      flows: ["u-fab-ru>u-vver-hu", "u-fab-ru>u-vver-cz", "u-fab-ru>u-vver-bg",
              "u-fab-se>u-vver-cz", "u-fab-se>u-vver-bg"],
      metric: "reactoren van Russisch ontwerp draaien op splijtstof die alleen Rusland maakte",
      note: "Midden-Europa (Paks, Dukovany, Kozloduy) bouwde Russische VVER-reactoren — en die draaien op splijtstofelementen die alleen TVEL leverde. Een eenrichtings-afhankelijkheid die pas nu barst, doordat Westinghouse (Västerås) niet-Russische VVER-brandstof kwalificeert." },

    { id: "u-t-niger", type: "spof", title: "Niger: landlocked en verstoord",
      lat: 18.74, lon: 7.39,
      nodes: ["u-mine-ne", "u-port-cotonou"],
      flows: ["u-mine-ne>u-port-cotonou", "u-port-cotonou>u-conv-fr"],
      metric: "~4% van de wereld — ±1.200 km over land, sinds de coup van 2023 grotendeels stil",
      note: "Nigers uranium (lang de Franse steunpilaar) moet per truck honderden kilometers door de Sahel naar Cotonou. Na de coup van 2023 en de breuk met Orano/Frankrijk viel die corridor grotendeels stil — een tweede landlocked-flessenhals, nu politiek dichtgeklapt." },

    { id: "u-t-ban", type: "beleid", title: "VS-verbod op Russische SWU (2024) + HALEU",
      lat: 32.44, lon: -103.13,
      nodes: ["u-enr-us", "u-enr-ru", "u-mine-us"],
      flows: ["u-conv-ca>u-enr-us", "u-mine-us>u-enr-us"],
      metric: "VS verbood Russisch verrijkt uranium (2024) — maar Rusland is de enige HALEU-leverancier",
      note: "De VS kochten jarenlang Russische verrijking; in 2024 kwam een invoerverbod. Het addertje: voor de nieuwe SMR's/geavanceerde reactoren is HALEU (hoger verrijkt) nodig, en dat leverde tot nu toe alléén Rusland commercieel. Vandaar de haast met Urenco USA en de heropstart van de eigen mijnbouw." },

    { id: "u-t-candu", type: "structureel", title: "CANDU: natuurlijk uranium, geen verrijking",
      lat: 44.30, lon: -77.60,
      nodes: ["u-mine-ca", "u-conv-ca", "u-mkt-ca"],
      flows: ["u-mine-ca>u-mkt-ca"],
      metric: "zwaarwaterreactoren draaien op natuurlijk uranium — de flessenhals valt weg",
      note: "Niet elke reactor heeft verrijking nodig. De Canadese CANDU-zwaarwaterreactoren draaien op NATUURLIJK uranium en slaan de hele verrijkingsstap — en dus de Russische knijp — over. Het verklaart waarom Canada erts, conversie én reactoren in één binnenlandse keten kan houden." },

    { id: "u-t-military", type: "beleid", title: "Militaire kringloop: van kernkoppen naar reactorbrandstof",
      lat: 52.0, lon: 40.0,
      nodes: ["u-mil-ru-heu", "u-mil-ru-tails", "u-mil-us-doe", "u-mil-us-reserve"],
      flows: ["u-mil-ru-heu>u-fab-us", "u-mil-us-doe>u-mkt-us", "u-mil-ru-tails>u-enr-ru"],
      metric: "secundair aanbod vult het gat mijn (~60 kt) ↔ reactorbehoefte (~65 kt)",
      note: "Zet de militaire-kringloop-laag aan. Niet al het reactoruranium komt uit een mijn: onder 'Megatons to Megawatts' (1993–2013) werd het hoogverrijkte uranium uit ~20.000 ontmantelde Russische kernkoppen down-geblend tot reactor-LEU — twee decennia lang goed voor ~10% van de Amerikaanse stroom. Daarnaast herverrijkt Rusland zijn verarmde tails, en houden de VS (DOE) en Rosatom strategische reserves. Dit secundaire aanbod vult het structurele gat tussen winning (~60 kt) en reactorbehoefte (~65 kt) — geen mijnbouw, wél een geopolitieke buffer die de afhankelijkheden verzacht óf verscherpt." },
  ],
});
