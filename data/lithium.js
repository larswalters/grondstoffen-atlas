// ============================================================================
// LITHIUM — volledig uitgewerkte module (voorbeeld/sjabloon voor de rest)
// Zie data/lithium.md voor het leesbare overzicht van alles wat hier staat.
// ============================================================================
//
// DE KETEN IN HET KORT
//   1. WINNING (stage "erts")
//      a) Hardrock (spodumeen): Australie, Zimbabwe, Brazilie, China, Canada.
//         Ter plekke opgewerkt tot concentraat (~6% Li2O, "SC6"), dan per
//         bulkschip weg.
//      b) Brine (pekel): Chili, Argentinie, China (Qinghai), Bolivia. Maanden
//         indampen in vijvers, ter plekke omgezet naar carbonaat.
//   2. RAFFINAGE (stage "raffinaat"): concentraat/ruw carbonaat -> batterij-
//      kwaliteit carbonaat of hydroxide. HIER zit de flessenhals: ~2/3 van de
//      wereldcapaciteit staat in China.
//   3. KATHODE/CEL (stage "product"): raffinaat -> kathode -> cellen.
//
// CIJFERS: `value` en `share` staan overal in dezelfde eenheid: kiloton LCE
// (lithium carbonate equivalent) per jaar, zodat de hele keten optelbaar is.
// Indicatief en afgerond; peiljaar circa 2024/25, o.b.v. USGS, bedrijfs-
// rapportages en IEA. `share` = aandeel in de wereldPRODUCTIE (actieve mijnen,
// telt op tot circa 93). Projecten hebben GEEN share maar een `potential` --
// anders krijgen niet-producerende plekken dikke bollen op de kaart.
//
// ROUTES: `via` volgt echte vaarroutes langs havens (li-port-*) en de
// universele knelpunten/vaarpunten uit data/_chokepoints.js (wp-*). Zonder
// die punten trekt de atlas de kortste lijn over de bol -- en die loopt dwars
// over land. Let op: Australisch erts vaart via Lombok/Makassar, NIET via
// Malakka; Malakka is de route voor Zimbabwe, Brazilie en de chemie naar Europa.
//
// TIERS: tier 1 = draagt het verhaal (altijd zichtbaar), tier 2 = havens en
// middelgrote locaties (bij inzoomen), tier 3 = detail (dichtbij).
// ============================================================================

REGISTER({
  id: "lithium",
  name: "Lithium",
  symbol: "Li",
  color: "#4FD1C5",
  detail: "uitgewerkt",
  unit: "kt LCE/jaar (indicatief)",
  blurb: "Accu's voor EV's en energieopslag. Australië graaft, Chili en Argentinië pompen — maar China raffineert. Daar ligt de flessenhals.",

  nodes: [
    // ---------------------------------------------------------------- MIJNEN
    // Australië — hardrock (spodumeen)
    { id: "li-greenbushes", type: "mine", name: "Greenbushes", country: "Australië",
      lat: -33.86, lon: 116.06, share: 15, tier: 1,
      operator: "Talison (Tianqi/Albemarle/IGO)", status: "actief",
      capacity: "±1.400 kt concentraat ≈ 185 kt LCE/j",
      note: "Grootste hardrock-lithiummijn ter wereld, en het rijkste erts (±2% Li2O). Export via de haven van Bunbury." },
    { id: "li-pilgangoora", type: "mine", name: "Pilgangoora", country: "Australië",
      lat: -20.98, lon: 118.90, share: 8, tier: 1,
      operator: "Pilbara Minerals", status: "actief",
      capacity: "±700 kt concentraat ≈ 95 kt LCE/j",
      note: "Pilbara — verscheept via Port Hedland, vrijwel volledig naar Chinese en Koreaanse raffinaderijen." },
    { id: "li-wodgina", type: "mine", name: "Wodgina", country: "Australië",
      lat: -21.18, lon: 118.68, share: 5, tier: 2,
      operator: "Mineral Resources / Albemarle", status: "actief",
      capacity: "≈ 60 kt LCE/j",
      note: "Pilbara, vlak bij Pilgangoora; zelfde exportroute via Port Hedland." },
    { id: "li-mt-marion", type: "mine", name: "Mt Marion", country: "Australië",
      lat: -31.10, lon: 121.40, share: 4, tier: 2,
      operator: "Mineral Resources / Ganfeng", status: "actief",
      capacity: "≈ 45 kt LCE/j",
      note: "Bij Kalgoorlie. Ganfeng (China) is JV-partner én afnemer: het erts gaat naar de eigen raffinaderijen." },
    { id: "li-kathleen-valley", type: "mine", name: "Kathleen Valley", country: "Australië",
      lat: -27.35, lon: 120.62, share: 2, tier: 3,
      operator: "Liontown", status: "actief",
      note: "Nieuwste grote Australische mijn (2024); langetermijncontracten met o.a. LG en Tesla." },

    // Zuid-Amerika — brine ("lithiumdriehoek")
    { id: "li-atacama", type: "mine", name: "Salar de Atacama", country: "Chili",
      lat: -23.50, lon: -68.25, share: 20, tier: 1,
      operator: "SQM + Albemarle", status: "actief",
      capacity: "≈ 245 kt LCE/j",
      note: "Rijkste pekel ter wereld en de snelste verdamping (woestijn). Concessie loopt via de staat (Codelco/CORFO)." },
    { id: "li-hombre-muerto", type: "mine", name: "Salar del Hombre Muerto", country: "Argentinië",
      lat: -25.40, lon: -67.00, share: 3, tier: 2,
      operator: "Arcadium (Rio Tinto)", status: "actief",
      note: "Oudste Argentijnse brine-operatie; produceert carbonaat en lithiumchloride." },
    { id: "li-olaroz", type: "mine", name: "Olaroz / Cauchari", country: "Argentinië",
      lat: -23.45, lon: -66.70, share: 5, tier: 2,
      operator: "Arcadium, Ganfeng, Exar", status: "actief",
      note: "Puna-hoogvlakte; snelst groeiende brine-regio, veel Chinese en Japanse investering." },
    { id: "li-uyuni", type: "mine", name: "Salar de Uyuni", country: "Bolivia",
      lat: -20.20, lon: -67.60, potential: "grootste bekende voorraad", tier: 3, status: "project",
      note: "Grootste bekende voorraad, maar veel magnesium en politiek muurvast. Nauwelijks productie." },

    // China — eigen winning (brine + lepidoliet)
    { id: "li-qinghai", type: "mine", name: "Qinghai-brines", country: "China",
      lat: 36.80, lon: 95.40, share: 8, tier: 2, status: "actief",
      capacity: "≈ 95 kt LCE/j",
      note: "Qarhan/Zhabuye — lastige pekel (hoog magnesium), maar wél binnenlandse aanvoer." },
    { id: "li-yichun-mine", type: "mine", name: "Yichun (lepidoliet)", country: "China",
      lat: 27.82, lon: 114.42, share: 9, tier: 2, status: "actief",
      capacity: "≈ 110 kt LCE/j",
      note: "Lepidoliet in Jiangxi: laag gehalte, duur. Dit is de marginale productie die de wereldprijs zet." },

    // Afrika — snelst groeiende nieuwe bron
    { id: "li-bikita", type: "mine", name: "Bikita / Arcadia", country: "Zimbabwe",
      lat: -20.08, lon: 31.33, share: 9, tier: 1,
      operator: "Sinomine, Huayou", status: "actief",
      capacity: "≈ 110 kt LCE/j",
      note: "Vrijwel volledig in Chinese handen; in enkele jaren opgeklommen tot de grootste producent buiten Australië en de driehoek. Export via Beira/Durban." },
    { id: "li-manono", type: "mine", name: "Manono", country: "DR Congo",
      lat: -7.30, lon: 27.40, potential: "een van de grootste onontgonnen hardrock-afzettingen", tier: 3, status: "project",
      note: "Vast in een eigendomsconflict (AVZ vs Zijin); nog geen productie." },

    // Amerika's
    { id: "li-silver-peak", type: "mine", name: "Silver Peak", country: "VS",
      lat: 37.75, lon: -117.63, share: 1, tier: 3,
      operator: "Albemarle", status: "actief",
      note: "Enige actieve Amerikaanse lithiummijn — en klein: zo'n 5 kt LCE per jaar." },
    { id: "li-thacker-pass", type: "mine", name: "Thacker Pass", country: "VS",
      lat: 41.70, lon: -118.05, potential: "±40 kt LCE/j in fase 1", tier: 2,
      operator: "Lithium Americas / GM", status: "project",
      note: "Kleiafzetting in Nevada; moet de Amerikaanse keten losweken van China. In aanbouw." },
    { id: "li-sigma", type: "mine", name: "Vale do Jequitinhonha", country: "Brazilië",
      lat: -16.90, lon: -41.50, share: 4, tier: 2,
      operator: "Sigma Lithium", status: "actief",
      note: "Minas Gerais — 'groen' spodumeenconcentraat; per spoor naar Vitória, dan de Atlantische Oceaan op." },

    // Europa — vrijwel niets in productie
    { id: "li-barroso", type: "mine", name: "Barroso", country: "Portugal",
      lat: 41.80, lon: -7.90, potential: "±25 kt LCE/j", tier: 3,
      operator: "Savannah Resources", status: "project",
      note: "Grootste EU-lithiumproject; lokaal verzet en trage vergunningen." },
    { id: "li-jadar", type: "mine", name: "Jadar", country: "Servië",
      lat: 44.50, lon: 19.30, potential: "±58 kt LCE/j", tier: 3,
      operator: "Rio Tinto", status: "project",
      note: "Groot genoeg voor een flink deel van de Europese EV-vraag, maar politiek omstreden en meermaals stilgelegd." },
    { id: "li-zinnwald", type: "mine", name: "Zinnwald", country: "Duitsland",
      lat: 50.73, lon: 13.50, potential: "±12 kt LCE/j", tier: 3, status: "project",
      note: "Ertsgebergte — klein, maar ligt pal naast de Duitse batterij-industrie." },
    { id: "li-keliber", type: "mine", name: "Keliber", country: "Finland",
      lat: 63.50, lon: 23.60, potential: "±15 kt LCE/j", tier: 3,
      operator: "Sibanye-Stillwater", status: "project",
      note: "Mijn plus eigen hydroxidefabriek: de enige echt gesloten EU-keten in aanbouw." },

    // ---------------------------------------------------------------- HAVENS
    // De plekken waar het erts de zee op gaat of aan land komt. Zonder deze
    // punten zou het concentraat "over land" naar zijn bestemming reizen.
    { id: "li-port-bunbury", type: "port", name: "Bunbury", country: "Australië",
      lat: -33.32, lon: 115.64, tier: 2,
      note: "Exporthaven van Greenbushes; het concentraat gaat per vrachtwagen ±90 km naar de kade." },
    { id: "li-port-hedland", type: "port", name: "Port Hedland", country: "Australië",
      lat: -20.31, lon: 118.58, tier: 2,
      note: "Grootste bulkhaven ter wereld (vooral ijzererts); ook al het Pilbara-lithium vertrekt hier." },
    { id: "li-port-geraldton", type: "port", name: "Geraldton", country: "Australië",
      lat: -28.77, lon: 114.61, tier: 2,
      note: "Uitgang voor het lithium uit de binnenlanden van West-Australië (o.a. Kathleen Valley, Mt Marion)." },
    { id: "li-port-antofagasta", type: "port", name: "Antofagasta / Angamos", country: "Chili",
      lat: -23.65, lon: -70.40, tier: 2,
      note: "Vrijwel de complete Chileense lithiumexport verlaat het land via deze ene havenregio — én het Argentijnse lithium uit de Puna, dat over de Andes hierheen rijdt." },
    { id: "li-port-beira", type: "port", name: "Beira", country: "Mozambique",
      lat: -19.83, lon: 34.84, tier: 2,
      note: "Belangrijkste uitgang voor Zimbabwaans concentraat (naast Durban); per spoor/weg vanaf de mijnen." },
    { id: "li-port-vitoria", type: "port", name: "Vitória", country: "Brazilië",
      lat: -20.32, lon: -40.29, tier: 2,
      note: "Atlantische uitgang voor het concentraat uit Minas Gerais; per spoor vanaf de mijn." },
    { id: "li-port-ningbo", type: "port", name: "Ningbo-Zhoushan", country: "China",
      lat: 29.87, lon: 121.54, tier: 2,
      note: "Aanloophaven voor concentraat; vandaar per spoor/weg naar Jiangxi en Sichuan." },
    { id: "li-port-charleston", type: "port", name: "Charleston", country: "VS",
      lat: 32.78, lon: -79.93, tier: 2,
      note: "Atlantische aanlanding voor de Amerikaanse lithiumchemie in de Carolinas." },
    { id: "li-port-oakland", type: "port", name: "Oakland", country: "VS",
      lat: 37.80, lon: -122.33, tier: 2,
      note: "Pacifische aanlanding voor Aziatisch en Australisch materiaal; vandaar over land naar Nevada." },
    { id: "li-port-rotterdam", type: "port", name: "Rotterdam", country: "Nederland",
      lat: 51.95, lon: 4.14, tier: 2,
      note: "Aanloophaven voor Zuid-Amerikaans carbonaat richting de Duitse chemie; laatste stuk per spoor." },
    { id: "li-port-piraeus", type: "port", name: "Piraeus", country: "Griekenland",
      lat: 37.94, lon: 23.63, tier: 2,
      note: "De Chinese toegangspoort tot Europa (COSCO): via Suez aan land, dan per spoor de Balkan in." },

    // ----------------------------------------------------- RAFFINAGE / CHEMIE
    { id: "li-ref-jiangxi", type: "refinery", name: "Jiangxi (Yichun/Ganzhou)", country: "China",
      lat: 28.30, lon: 115.00, tier: 1,
      capacity: "grootste cluster ter wereld",
      note: "Verwerkt zowel geïmporteerd Australisch concentraat als lokaal lepidoliet. Het zwaartepunt van de hele keten." },
    { id: "li-ref-sichuan", type: "refinery", name: "Sichuan (Suining/Yibin)", country: "China",
      lat: 30.50, lon: 105.60, tier: 1,
      note: "Tweede Chinese cluster, direct gekoppeld aan kathodefabrieken. Draait vooral op geïmporteerd spodumeen." },
    { id: "li-ref-qinghai", type: "refinery", name: "Qinghai-raffinage", country: "China",
      lat: 36.80, lon: 98.50, tier: 2,
      note: "Verwerkt lokale pekel tot carbonaat: goedkoop, maar lagere zuiverheid." },
    { id: "li-ref-kwinana", type: "refinery", name: "Kwinana / Kemerton", country: "Australië",
      lat: -32.24, lon: 115.77, tier: 2, operator: "Tianqi/IGO, Albemarle", coastal: true,
      note: "Australië's poging zelf te raffineren. Moeizaam opgestart en deels teruggeschaald — erts hebben is niet hetzelfde als chemie kunnen maken." },
    { id: "li-ref-carmen", type: "refinery", name: "Salar del Carmen / La Negra", country: "Chili",
      lat: -23.60, lon: -70.35, tier: 1, operator: "SQM, Albemarle", coastal: true,
      note: "Carbonaatfabrieken bij Antofagasta; exporteren via de haven rechtstreeks naar Azië, de VS en Europa." },
    { id: "li-ref-becancour", type: "refinery", name: "Bécancour", country: "Canada",
      lat: 46.34, lon: -72.44, tier: 3, status: "gepland",
      note: "Quebec bouwt een Noord-Amerikaanse keten (raffinage + kathode) op goedkope waterkracht." },
    { id: "li-ref-kings-mountain", type: "refinery", name: "Kings Mountain / Bessemer City", country: "VS",
      lat: 35.30, lon: -81.30, tier: 2, operator: "Albemarle",
      note: "Historisch hart van de Amerikaanse lithiumchemie; wordt onder de IRA heropgebouwd." },
    { id: "li-ref-gwangyang", type: "refinery", name: "Gwangyang", country: "Zuid-Korea",
      lat: 34.94, lon: 127.70, tier: 1, operator: "POSCO", coastal: true,
      note: "Hydroxide voor Koreaanse kathodemakers — bewust gevoed met Australisch en Argentijns materiaal, om China heen. De fabriek staat pal aan de haven." },
    { id: "li-ref-naraha", type: "refinery", name: "Naraha", country: "Japan",
      lat: 37.29, lon: 141.00, tier: 3, operator: "Toyota Tsusho", coastal: true,
      note: "Kleine hydroxidefabriek aan de kust, gevoed met Argentijns carbonaat." },
    { id: "li-ref-bitterfeld", type: "refinery", name: "Bitterfeld", country: "Duitsland",
      lat: 51.62, lon: 12.32, tier: 2, operator: "AMG Lithium", status: "actief",
      note: "Eerste hydroxidefabriek van de EU — maar zonder eigen Europese mijn: de grondstof komt van buiten." },
    { id: "li-ref-kokkola", type: "refinery", name: "Kokkola", country: "Finland",
      lat: 63.84, lon: 23.13, tier: 3, status: "gepland",
      note: "Hydroxidefabriek van Keliber; samen met de mijn de enige gesloten EU-keten." },

    // -------------------------------------------------------- MARKT / CELLEN
    { id: "li-mkt-catl", type: "market", name: "Ningde (CATL)", country: "China",
      lat: 26.66, lon: 119.55, tier: 1,
      note: "Grootste batterijfabrikant ter wereld; koopt raffinaat uit Jiangxi en Sichuan." },
    { id: "li-mkt-byd", type: "market", name: "Shenzhen (BYD)", country: "China",
      lat: 22.60, lon: 114.05, tier: 2,
      note: "Verticaal geïntegreerd: van kathode tot auto." },
    { id: "li-mkt-nevada", type: "market", name: "Giga Nevada", country: "VS",
      lat: 39.54, lon: -119.44, tier: 1,
      note: "Cellen voor de Amerikaanse markt; grondstof nog grotendeels geïmporteerd." },
    { id: "li-mkt-debrecen", type: "market", name: "Debrecen / Göd", country: "Hongarije",
      lat: 47.53, lon: 21.63, tier: 1,
      note: "Grootste Europese celcluster (CATL, Samsung SDI) — draaiend op Aziatische kathodematerialen." },
    { id: "li-mkt-skelleftea", type: "market", name: "Skellefteå", country: "Zweden",
      lat: 64.75, lon: 20.95, tier: 3,
      note: "Europese poging tot een eigen celindustrie; kwetsbaar gebleken zonder eigen chemieketen." },
  ],

  // ==========================================================================
  // STROMEN — value in kt LCE/jaar, stage bepaalt kleur, via = echte vaarroute.
  //
  // De twee grote Aziatische aanvoerroutes:
  //   A) Australië -> China: Lombok -> Makassar -> Zuid-Chinese Zee -> Taiwan
  //   B) Afrika/Brazilië -> China: Malakka -> Singapore -> Zuid-Chinese Zee
  // En de derde, die vaak vergeten wordt:
  //   C) Chili/Argentinië -> Azië: dwars over de Stille Oceaan (géén knelpunt,
  //      maar wél de langste route ter wereld voor een bulkgoed)
  // ==========================================================================
  flows: [
    // === 1. AUSTRALISCH ERTS -> AZIATISCHE RAFFINAGE (de hoofdader) =========
    { from: "li-greenbushes", to: "li-ref-jiangxi", value: 110, mode: "ship", stage: "erts",
      via: ["li-port-bunbury", "wp-lombok", "wp-makassar", "wp-scs", "wp-taiwan", "li-port-ningbo"],
      note: "Greenbushes → Jiangxi: de dikste lithiumstroom ter wereld. Per truck naar Bunbury, dan door de Straat van Lombok en Makassar naar de Chinese oostkust." },
    { from: "li-greenbushes", to: "li-ref-sichuan", value: 55, mode: "ship", stage: "erts",
      via: ["li-port-bunbury", "wp-lombok", "wp-makassar", "wp-scs", "wp-taiwan", "li-port-ningbo"],
      note: "Greenbushes → Sichuan, via Tianqi's eigen raffinaderijen; laatste stuk per spoor de Yangtze op." },
    { from: "li-greenbushes", to: "li-ref-kwinana", value: 20, mode: "road", stage: "erts",
      note: "Het kleine deel dat Australië zélf raffineert; de rest verlaat het land ongeraffineerd." },
    { from: "li-pilgangoora", to: "li-ref-jiangxi", value: 80, mode: "ship", stage: "erts",
      via: ["li-port-hedland", "wp-lombok", "wp-makassar", "wp-scs", "wp-taiwan", "li-port-ningbo"],
      note: "Port Hedland → Chinese oostkust. Pilbara Minerals veilt concentraat aan Chinese chemiebedrijven." },
    { from: "li-pilgangoora", to: "li-ref-gwangyang", value: 15, mode: "ship", stage: "erts",
      via: ["li-port-hedland", "wp-lombok", "wp-makassar", "wp-scs"],
      note: "Australië → Zuid-Korea: bewuste omzeiling van China door POSCO." },
    { from: "li-wodgina", to: "li-ref-sichuan", value: 55, mode: "ship", stage: "erts",
      via: ["li-port-hedland", "wp-lombok", "wp-makassar", "wp-scs", "wp-taiwan", "li-port-ningbo"],
      note: "Wodgina → Sichuan; Albemarle en MinRes verkopen vrijwel alles aan Chinese raffinadeurs." },
    { from: "li-mt-marion", to: "li-ref-jiangxi", value: 45, mode: "ship", stage: "erts",
      via: ["li-port-geraldton", "wp-lombok", "wp-makassar", "wp-scs", "wp-taiwan", "li-port-ningbo"],
      note: "Mt Marion → China; JV-partner Ganfeng is zelf de raffinadeur." },
    { from: "li-kathleen-valley", to: "li-ref-jiangxi", value: 20, mode: "ship", stage: "erts",
      via: ["li-port-geraldton", "wp-lombok", "wp-makassar", "wp-scs", "wp-taiwan", "li-port-ningbo"],
      note: "Nieuwste aanvoerlijn (sinds 2024); contracten deels ook met Korea en de VS." },

    // === 2. AFRIKA & BRAZILIË -> CHINA (via Malakka) ========================
    { from: "li-bikita", to: "li-ref-jiangxi", value: 100, mode: "ship", stage: "erts",
      via: ["li-port-beira", "wp-moz-noord", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan", "li-port-ningbo"],
      note: "Zimbabwe → China via Beira en de Straat van Malakka. Chinese eigenaren, Chinese bestemming — de snelst gegroeide stroom van de laatste jaren." },
    { from: "li-sigma", to: "li-ref-jiangxi", value: 40, mode: "ship", stage: "erts",
      via: ["li-port-vitoria", "wp-kaap", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan", "li-port-ningbo"],
      note: "Brazilië → China: per spoor naar Vitória, om Kaap de Goede Hoop, door Malakka. Bijna een halve wereldreis." },
    { from: "li-sigma", to: "li-ref-kings-mountain", value: 10, mode: "ship", stage: "erts",
      via: ["li-port-vitoria", "wp-atl-brazilie", "wp-atl-west", "li-port-charleston"],
      note: "Brazilië → VS over de Atlantische Oceaan; Sigma bouwt bewust een niet-Chinese afzet op." },

    // === 3. BINNENLANDSE CHINESE AANVOER ====================================
    { from: "li-yichun-mine", to: "li-ref-jiangxi", value: 110, mode: "road", stage: "erts",
      note: "Lokaal lepidoliet → lokale raffinage. Dure productie: valt als eerste stil bij lage prijzen." },
    { from: "li-qinghai", to: "li-ref-qinghai", value: 95, mode: "pipeline", stage: "erts",
      note: "Qinghai-pekel → carbonaat ter plekke." },

    // === 4. ZUID-AMERIKAANSE PEKEL -> WERELDMARKT ===========================
    { from: "li-atacama", to: "li-ref-carmen", value: 245, mode: "pipeline", stage: "erts",
      note: "Geconcentreerde pekel per pijpleiding/truck van de salar naar de carbonaatfabrieken bij Antofagasta." },
    { from: "li-ref-carmen", to: "li-ref-jiangxi", value: 60, mode: "ship", stage: "raffinaat",
      via: ["li-port-antofagasta", "wp-pac-zuid", "wp-pac-west", "wp-taiwan", "li-port-ningbo"],
      note: "Chileens carbonaat → China: dwars over de Stille Oceaan. Geen zeestraat, wel de langste route in de keten." },
    { from: "li-ref-carmen", to: "li-ref-gwangyang", value: 35, mode: "ship", stage: "raffinaat",
      via: ["li-port-antofagasta", "wp-pac-zuid", "wp-pac-west"],
      note: "Chili → Korea: de grootste niet-Chinese afnemer." },
    { from: "li-ref-carmen", to: "li-ref-kings-mountain", value: 25, mode: "ship", stage: "raffinaat",
      via: ["li-port-antofagasta", "wp-panama", "li-port-charleston"],
      note: "Chili → VS door het Panamakanaal; onder de IRA telt Chileens materiaal mee als vrijhandelspartner." },
    { from: "li-ref-carmen", to: "li-ref-bitterfeld", value: 15, mode: "ship", stage: "raffinaat",
      via: ["li-port-antofagasta", "wp-panama", "li-port-rotterdam"],
      note: "Chili → Rotterdam → Bitterfeld. Zonder eigen mijn moet de Europese hydroxide hier vandaan komen." },
    { from: "li-hombre-muerto", to: "li-ref-naraha", value: 10, mode: "ship", stage: "raffinaat",
      via: ["li-port-antofagasta", "wp-pac-zuid", "wp-pac-west"],
      note: "Argentinië → Japan; het carbonaat rijdt eerst over de Andes naar de Chileense kust." },
    { from: "li-olaroz", to: "li-ref-jiangxi", value: 35, mode: "ship", stage: "raffinaat",
      via: ["li-port-antofagasta", "wp-pac-zuid", "wp-pac-west", "wp-taiwan", "li-port-ningbo"],
      note: "Argentinië → China: Ganfeng bezit zowel de salar als de raffinaderij." },
    { from: "li-olaroz", to: "li-ref-gwangyang", value: 15, mode: "ship", stage: "raffinaat",
      via: ["li-port-antofagasta", "wp-pac-zuid", "wp-pac-west"],
      note: "Argentinië → Korea; groeiende alternatieve route." },

    // === 5. RAFFINAAT -> KATHODE- EN CELFABRIEKEN ===========================
    { from: "li-ref-jiangxi", to: "li-mkt-catl", value: 120, mode: "rail", stage: "product",
      note: "Batterijkwaliteit carbonaat/hydroxide → CATL." },
    { from: "li-ref-sichuan", to: "li-mkt-byd", value: 80, mode: "rail", stage: "product",
      note: "Sichuan → BYD; LFP-kathodes vragen carbonaat, geen hydroxide." },
    { from: "li-ref-qinghai", to: "li-mkt-catl", value: 40, mode: "rail", stage: "product",
      note: "Goedkoper carbonaat, vooral voor energieopslag-cellen." },
    { from: "li-ref-jiangxi", to: "li-mkt-debrecen", value: 25, mode: "ship", stage: "product",
      via: ["li-port-ningbo", "wp-taiwan", "wp-scs", "wp-singapore", "wp-malakka", "wp-aceh", "wp-bab", "wp-rode-zee", "wp-suez", "li-port-piraeus"],
      note: "China → Hongarije: door Malakka, langs Bab el-Mandeb, door Suez, aan land in Piraeus. Europa's 'eigen' celfabrieken draaien op Chinese chemie — en op een route met drie knelpunten." },
    { from: "li-ref-gwangyang", to: "li-mkt-nevada", value: 20, mode: "ship", stage: "product",
      via: ["wp-pac-noord", "li-port-oakland"],
      note: "Korea → VS: de grote-cirkelroute hoog over de noordelijke Stille Oceaan, aan land in Oakland. Koreaans hydroxide vult het gat dat Amerikaanse raffinage nog niet dicht." },
    { from: "li-ref-kwinana", to: "li-mkt-nevada", value: 8, mode: "ship", stage: "product",
      via: ["wp-lombok", "wp-makassar", "wp-pac-west", "li-port-oakland"],
      note: "Australisch hydroxide → VS: door dezelfde Indonesische straten als het erts, dan de Stille Oceaan over naar Oakland. Zuid om Tasmanië varen is een omweg die niemand maakt." },
    { from: "li-ref-kings-mountain", to: "li-mkt-nevada", value: 12, mode: "rail", stage: "product",
      note: "De enige volledig binnenlandse Amerikaanse route — nog dun." },
    { from: "li-ref-bitterfeld", to: "li-mkt-debrecen", value: 5, mode: "rail", stage: "product",
      note: "EU-hydroxide → EU-cellen. Dít lijntje probeert Europa dik te maken." },
    { from: "li-ref-bitterfeld", to: "li-mkt-skelleftea", value: 2, mode: "rail", stage: "product",
      note: "Bescheiden — en het laat zien hoe dun de Europese keten nog is." },

    // === 6. GEPLANDE / TOEKOMSTIGE ROUTES ===================================
    { from: "li-thacker-pass", to: "li-ref-kings-mountain", value: 20, mode: "rail", stage: "erts",
      status: "gepland",
      note: "Gepland: Nevada-klei → Amerikaanse raffinage. Moet de VS-keten sluiten." },
    { from: "li-barroso", to: "li-ref-bitterfeld", value: 8, mode: "rail", stage: "erts",
      status: "gepland",
      note: "Gepland: Portugees erts → Duitse hydroxide. De EU-keten, op papier." },
    { from: "li-keliber", to: "li-ref-kokkola", value: 8, mode: "road", stage: "erts",
      status: "gepland",
      note: "Gepland: mijn en raffinaderij in hetzelfde land — voorlopig uniek in Europa." },
  ],

  // ==========================================================================
  // SPANNINGEN — waar de keten kan breken. Verwijst naar de universele
  // knelpuntenlijst (wp-*) waar dat kan; grondstof-specifieke spanningen
  // (exportverboden, concentratie) staan hier volledig.
  // flows-verwijzing: "from-id>to-id".
  // ==========================================================================
  tensions: [
    { id: "li-t-indonesie", type: "knelpunt", title: "Lombok & Makassar: de Australische route",
      lat: -8.70, lon: 115.85,
      nodes: ["wp-lombok", "wp-makassar"],
      flows: ["li-greenbushes>li-ref-jiangxi", "li-greenbushes>li-ref-sichuan",
              "li-pilgangoora>li-ref-jiangxi", "li-pilgangoora>li-ref-gwangyang",
              "li-wodgina>li-ref-sichuan", "li-mt-marion>li-ref-jiangxi",
              "li-kathleen-valley>li-ref-jiangxi"],
      metric: "al het Australische concentraat — ruim een derde van de wereldproductie",
      note: "Grote bulkschepen uit West-Australië nemen niet Malakka maar de diepere Straat van Lombok, dan Makassar richting de Zuid-Chinese Zee. Twee smalle doorgangen door de Indonesische archipel — en Indonesië heeft er zeggenschap over." },

    { id: "li-t-malakka", type: "knelpunt", title: "Straat van Malakka",
      lat: 3.0, lon: 100.6,
      nodes: ["wp-malakka", "wp-singapore"],
      flows: ["li-bikita>li-ref-jiangxi", "li-sigma>li-ref-jiangxi",
              "li-ref-jiangxi>li-mkt-debrecen"],
      metric: "±30% van alle wereldhandel over zee",
      note: "Zimbabwaans en Braziliaans erts gaat hierdoor naar China — en de Chinese batterijchemie komt er weer doorheen terug richting Europa. Wie deze straat sluit, raakt beide richtingen tegelijk." },

    { id: "li-t-raffinage", type: "concentratie", title: "Raffinage: ±twee derde in China",
      lat: 28.3, lon: 111.0,
      nodes: ["li-ref-jiangxi", "li-ref-sichuan", "li-ref-qinghai"],
      flows: [],
      metric: "winning top-1 (Australië) ≈ 35% · raffinage top-1 (China) ≈ 65–70%",
      note: "De kwetsbaarheid zit niet bij het erts maar één stap verderop: wie niet via China raffineert, heeft nauwelijks alternatieven op schaal. Precies daarom bestaan de routes via Korea en de heropbouw in de VS." },

    { id: "li-t-greenbushes", type: "spof", title: "Greenbushes: één mijn, 15% van de wereld",
      lat: -33.86, lon: 116.06,
      nodes: ["li-greenbushes", "li-port-bunbury"],
      flows: ["li-greenbushes>li-ref-jiangxi", "li-greenbushes>li-ref-sichuan", "li-greenbushes>li-ref-kwinana"],
      metric: "±15% van de wereldproductie uit één put",
      note: "Het rijkste erts ter wereld, en alles vertrekt via één haven (Bunbury). Een staking, storm of technisch probleem hier is meteen wereldnieuws op de lithiummarkt." },

    { id: "li-t-zimbabwe", type: "beleid", title: "Zimbabwe: exportverbod op ruw erts",
      lat: -20.08, lon: 31.33,
      nodes: ["li-bikita", "li-port-beira"],
      flows: ["li-bikita>li-ref-jiangxi"],
      metric: "verbod op ruw erts sinds 2022; druk om óók concentraat te verbieden",
      note: "Zimbabwe dwingt verwerking binnen de grenzen af: eerst geen ruw erts meer, en de regering stuurt aan op verplichte verwerking tot lithiumsulfaat in eigen land. Het draaiboek dat Indonesië met nikkel schreef." },

    { id: "li-t-ira", type: "beleid", title: "IRA/FEOC: subsidie dwingt routes af",
      lat: 35.3, lon: -81.3,
      nodes: ["li-ref-kings-mountain", "li-ref-gwangyang", "li-ref-carmen", "li-mkt-nevada", "li-port-charleston"],
      flows: ["li-ref-carmen>li-ref-kings-mountain", "li-ref-gwangyang>li-mkt-nevada",
              "li-ref-kings-mountain>li-mkt-nevada", "li-thacker-pass>li-ref-kings-mountain",
              "li-sigma>li-ref-kings-mountain"],
      metric: "geen subsidie als materiaal via een 'foreign entity of concern' liep",
      note: "Amerikaanse EV-subsidie vervalt zodra er Chinese schakels in de keten zitten. Daarom bestaan de lijnen Chili→VS, Brazilië→VS en Korea→Nevada: juridisch afgedwongen omwegen om China heen." },
  ],
});
