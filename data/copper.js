// ============================================================================
// KOPER (Cu) — volledig uitgewerkte module. Peiljaar ±2024.
// Cijfers indicatief/afgerond, o.b.v. USGS MCS 2025, ICSG, IEA en bedrijfs-
// rapportages. Eenheid overal: kt Cu-inhoud/jaar (metaalinhoud, niet bruto erts),
// zodat de hele keten optelbaar blijft. Zie data/../design/koper.md voor de brief.
//
// DE VORM VAN KOPER (bijna lithium, één stap verderop):
//   - MIJNBOUW is breed verspreid, met een duidelijk ANDES-zwaartepunt (Chili/Peru).
//   - RAFFINAGE knijpt samen in CHINA (~50% van de wereldsmeltcapaciteit): Andes-
//     concentraat vaart de Stille Oceaan over naar Chinese smelters en komt als
//     kathode terug. Dát is de koper-"aha", zoals China bij lithium.
//   - TWEEDE trechter: de Afrikaanse COPPERBELT (DR Congo/Zambia) die géén concentraat
//     maar SX-EW-KATHODE is, en die eerst over LAND (via de grenspost Kasumbalesa)
//     naar Durban/Dar es Salaam/Lobito moet vóór hij de wereldmarkt op kan.
//
// TWEE PRODUCTVORMEN (via `stage`):
//   erts       = sulfide-CONCENTRAAT (~25-30% Cu) op weg naar een smelter — dof/donker.
//   raffinaat  = KATHODE (incl. SX-EW, direct bij de oxide-mijn geraffineerd) — volle
//                koperkleur. SX-EW-mijnen zenden dus al `raffinaat` uit bij de bron.
//   product    = halffabricaat (draadstaven/buizen) — licht.
//
// TRANSPORT is schip + land (géén luchtroute-modus): hergebruikt de zee-A*/land-A*-
// routes en de scheeps-voyages. Copperbelt-corridors zijn `rail`/`road` mijn->haven
// (via Kasumbalesa), dan een aparte `ship`-stroom haven->markt — net als kobalt.
//
// BEURSVOORRADEN (type "exchange" / flow.layer "exchange") zijn een aparte optionele
// toggle die standaard UIT staat — het koper-equivalent van de goud-CB-laag.
// Nuance: beursvoorraad is BUFFER-/handelsvoorraad, geen verbruik.
// ============================================================================

REGISTER({
  id: "copper",
  name: "Koper",
  symbol: "Cu",
  color: "#C87D4A",
  flowColor: "#E0965A",
  detail: "uitgewerkt",
  unit: "kt Cu/jaar (indicatief)",
  blurb: "Onmisbaar voor het elektriciteitsnet, kabels, motoren en EV's. Mijnbouw " +
    "breed verspreid met een Andes-zwaartepunt (Chili/Peru) — maar ~50% van de " +
    "raffinage staat in China. Concentraat vaart de Stille Oceaan over naar Chinese " +
    "smelters en komt als kathode terug. De Afrikaanse Copperbelt reist als kathode " +
    "eerst over land naar de kust.",

  nodes: [
    // ================================================================== MIJNEN
    // --- Chili (~24% van de wereld): het hart van de Andes-productie ---------
    { id: "cu-escondida", type: "mine", name: "Escondida", country: "Chili",
      lat: -24.27, lon: -69.07, share: 5.5, tier: 1, operator: "BHP (+ Rio Tinto/JECO)",
      status: "actief", capacity: "≈ 1.050 kt Cu/j",
      note: "Grootste kopermijn ter wereld (Atacama). Sulfide-concentraat via Antofagasta; ook een SX-EW-kathodelijn." },
    { id: "cu-collahuasi", type: "mine", name: "Collahuasi", country: "Chili",
      lat: -20.98, lon: -68.68, share: 2.7, tier: 1, operator: "Anglo American / Glencore",
      status: "actief", capacity: "≈ 560 kt Cu/j",
      note: "Hooggelegen sulfide-mijn; concentraat per pijp/truck naar de kust (Patache/Collahuasi-haven)." },
    { id: "cu-elteniente", type: "mine", name: "El Teniente", country: "Chili",
      lat: -34.10, lon: -70.36, share: 2.1, tier: 2, operator: "Codelco",
      status: "actief", capacity: "≈ 440 kt Cu/j",
      note: "Grootste ondergrondse kopermijn ter wereld; eigen smelter Caletones vlakbij." },
    { id: "cu-chuquicamata", type: "mine", name: "Chuquicamata", country: "Chili",
      lat: -22.29, lon: -68.90, share: 1.6, tier: 2, operator: "Codelco",
      status: "actief", capacity: "≈ 350 kt Cu/j",
      note: "Iconische open pit (nu ook ondergronds) met eigen smelter/raffinaderij bij Calama." },
    { id: "cu-lospelambres", type: "mine", name: "Los Pelambres", country: "Chili",
      lat: -31.75, lon: -70.51, share: 1.6, tier: 2, operator: "Antofagasta plc",
      status: "actief", capacity: "≈ 350 kt Cu/j",
      note: "Centraal-Chili; concentraat per pijpleiding naar de haven Punta Chungo." },

    // --- Peru (~10-12%): de tweede Andes-poot -------------------------------
    { id: "cu-cerroverde", type: "mine", name: "Cerro Verde", country: "Peru",
      lat: -16.53, lon: -71.60, share: 2.0, tier: 2, operator: "Freeport-McMoRan",
      status: "actief", capacity: "≈ 450 kt Cu/j",
      note: "Bij Arequipa; sulfide-concentraat via Matarani. Een van de grootste concentrators ter wereld." },
    { id: "cu-antamina", type: "mine", name: "Antamina", country: "Peru",
      lat: -9.54, lon: -77.06, share: 2.0, tier: 2, operator: "BHP/Glencore/Teck/Mitsubishi",
      status: "actief", capacity: "≈ 450 kt Cu/j",
      note: "Koper-zink; concentraat per 300 km-pijpleiding naar de kusthaven Punta Lobitos." },
    { id: "cu-lasbambas", type: "mine", name: "Las Bambas", country: "Peru",
      lat: -14.10, lon: -72.30, share: 1.6, tier: 2, operator: "MMG (China)",
      status: "actief", capacity: "≈ 350 kt Cu/j",
      note: "Concentraat per truck over de omstreden 'mineralencorridor' naar Matarani — vaak geblokkeerd door protesten." },
    { id: "cu-quellaveco", type: "mine", name: "Quellaveco", country: "Peru",
      lat: -17.10, lon: -70.70, share: 1.4, tier: 3, operator: "Anglo American / Mitsubishi",
      status: "actief", capacity: "≈ 300 kt Cu/j",
      note: "Nieuwe grote mijn (2022) in Moquegua; concentraat naar Ilo." },

    // --- Afrikaanse Copperbelt (DR Congo / Zambia): kathode, landlocked ------
    { id: "cu-kamoa", type: "mine", name: "Kamoa-Kakula", country: "DR Congo",
      lat: -10.76, lon: 25.28, share: 2.0, tier: 1, operator: "Ivanhoe / Zijin",
      status: "actief", capacity: "≈ 450 kt Cu/j (groeiend)",
      note: "Rijkste grote koperafzetting ter wereld; hoogwaardig sulfide-concentraat + sinds 2025 eigen smelter (blister). Reist per spoor via de Lobito-corridor." },
    { id: "cu-tenke", type: "mine", name: "Tenke Fungurume", country: "DR Congo",
      lat: -10.60, lon: 26.10, share: 1.8, tier: 1, operator: "CMOC (China)",
      status: "actief", capacity: "≈ 400 kt Cu/j",
      note: "Oxide-erts → SX-EW-KATHODE ter plekke (plus kobalt). Reist als afgewerkt metaal over land, zónder smelter-tussenstop." },
    { id: "cu-kolwezi", type: "mine", name: "Kolwezi (KCC)", country: "DR Congo",
      lat: -10.72, lon: 25.47, share: 1.4, tier: 2, operator: "Glencore (Kamoto)",
      status: "actief", capacity: "≈ 300 kt Cu/j",
      note: "SX-EW-kathode + kobalt; het dichtste koper-kobaltweefsel op aarde." },
    { id: "cu-kansanshi", type: "mine", name: "Kansanshi", country: "Zambia",
      lat: -12.10, lon: 26.40, share: 1.2, tier: 2, operator: "First Quantum",
      status: "actief", capacity: "≈ 250 kt Cu/j",
      note: "Grootste kopermijn van Afrika (Solwezi); mix van concentraat en SX-EW-kathode, eigen smelter." },
    { id: "cu-sentinel", type: "mine", name: "Sentinel (Kalumbila)", country: "Zambia",
      lat: -12.30, lon: 25.30, share: 1.0, tier: 3, operator: "First Quantum",
      status: "actief", capacity: "≈ 220 kt Cu/j",
      note: "Sulfide-concentraat; exporteert deels westwaarts via Walvis Bay." },

    // --- Overig: breed verspreid --------------------------------------------
    { id: "cu-grasberg", type: "mine", name: "Grasberg", country: "Indonesië",
      lat: -4.06, lon: 137.11, share: 3.0, tier: 1, operator: "Freeport / Inalum",
      status: "actief", capacity: "≈ 750 kt Cu/j",
      note: "Reuzenmijn in de Papoease hooglanden (koper-goud); concentraat via de kusthaven Amamapare naar Chinese/Japanse smelters én de nieuwe Manyar-smelter." },
    { id: "cu-morenci", type: "mine", name: "Morenci", country: "VS",
      lat: 33.06, lon: -109.36, share: 1.7, tier: 2, operator: "Freeport-McMoRan",
      status: "actief", capacity: "≈ 380 kt Cu/j",
      note: "Grootste Amerikaanse kopermijn (Arizona); grotendeels SX-EW-KATHODE — blijft binnenlands." },
    { id: "cu-bingham", type: "mine", name: "Bingham Canyon", country: "VS",
      lat: 40.52, lon: -112.15, share: 0.8, tier: 3, operator: "Rio Tinto (Kennecott)",
      status: "actief", capacity: "≈ 180 kt Cu/j",
      note: "Utah; concentraat → eigen Kennecott-smelter/raffinaderij → binnenlandse markt." },
    { id: "cu-buenavista", type: "mine", name: "Buenavista del Cobre", country: "Mexico",
      lat: 30.98, lon: -110.30, share: 1.5, tier: 3, operator: "Grupo México",
      status: "actief", capacity: "≈ 330 kt Cu/j",
      note: "Sonora, vlak onder Arizona; SX-EW-kathode + concentraat, grotendeels naar de VS over land." },
    { id: "cu-oyutolgoi", type: "mine", name: "Oyu Tolgoi", country: "Mongolië",
      lat: 43.00, lon: 106.85, share: 1.5, tier: 2, operator: "Rio Tinto / Erdenes",
      status: "actief", capacity: "≈ 330 kt Cu/j (ondergronds groeiend)",
      note: "Concentraat gaat vrijwel volledig over de grens naar Chinese smelters — geen zee nodig." },
    { id: "cu-norilsk", type: "mine", name: "Norilsk (Cu-Ni)", country: "Rusland",
      lat: 69.35, lon: 88.20, share: 2.0, tier: 2, operator: "Nornickel",
      status: "actief", capacity: "≈ 430 kt Cu/j",
      note: "Koper als medeproduct van nikkel/palladium boven de poolcirkel; grotendeels binnenlands geraffineerd." },
    { id: "cu-kazakhstan", type: "mine", name: "Aktogay / Kounrad", country: "Kazachstan",
      lat: 46.80, lon: 79.70, share: 1.5, tier: 3, operator: "KAZ Minerals",
      status: "actief", capacity: "≈ 330 kt Cu/j",
      note: "Kazachse kathode reist per spoor de grens over naar China (Xinjiang)." },
    { id: "cu-mountisa", type: "mine", name: "Mount Isa", country: "Australië",
      lat: -20.72, lon: 139.49, share: 0.8, tier: 3, operator: "Glencore",
      status: "actief", capacity: "≈ 180 kt Cu/j",
      note: "Queensland; concentraat via Townsville naar Aziatische smelters (eigen smelter sluit 2025)." },
    { id: "cu-olympicdam", type: "mine", name: "Olympic Dam", country: "Australië",
      lat: -30.44, lon: 136.88, share: 0.8, tier: 3, operator: "BHP",
      status: "actief", capacity: "≈ 200 kt Cu/j",
      note: "Zuid-Australië; koper-uranium-goud, ter plekke geraffineerd tot kathode." },
    { id: "cu-kghm", type: "mine", name: "KGHM (Lubin/Polkowice)", country: "Polen",
      lat: 51.40, lon: 16.20, share: 1.8, tier: 2, operator: "KGHM (staat)",
      status: "actief", capacity: "≈ 400 kt Cu/j",
      note: "Grootste EU-kopermijn; geïntegreerd met de eigen smelter/raffinaderij Głogów." },
    { id: "cu-aitik", type: "mine", name: "Aitik", country: "Zweden",
      lat: 67.07, lon: 20.95, share: 0.5, tier: 3, operator: "Boliden",
      status: "actief", capacity: "≈ 110 kt Cu/j",
      note: "Grootste open kopermijn van de EU (boven de poolcirkel); concentraat naar Rönnskär." },
    { id: "cu-china-mine", type: "mine", name: "Julong / Zijinshan", country: "China",
      lat: 29.65, lon: 91.70, share: 1.6, tier: 2, operator: "Zijin Mining e.a.",
      status: "actief", capacity: "≈ 350 kt Cu/j",
      note: "Chinese binnenlandse winning (Tibet/Fujian) — bescheiden t.o.v. de enorme Chinese raffinage." },
    { id: "cu-cobrepanama", type: "mine", name: "Cobre Panamá", country: "Panama",
      lat: 8.85, lon: -80.68, tier: 3, operator: "First Quantum", status: "project",
      potential: "≈ 350 kt Cu/j (stilgelegd sinds eind 2023)",
      note: "Een van de grootste nieuwe mijnen ter wereld — na een grondwettelijke uitspraak en protesten stilgelegd. Symbool van de vergunningsdruk op nieuw koper." },

    // ============================================= SMELTERS / RAFFINAGE
    // Hier knijpt het samen: China ≈ de helft van de wereldsmeltcapaciteit.
    { id: "cu-ref-jiangxi", type: "refinery", name: "Jiangxi Copper (Guixi)", country: "China",
      lat: 28.30, lon: 117.20, tier: 1, operator: "Jiangxi Copper",
      capacity: "grootste smelter ter wereld (~1.200 kt/j)",
      note: "De spil van de Chinese smelttrechter; draait op geïmporteerd Andes- en Indonesisch concentraat plus schroot." },
    { id: "cu-ref-tongling", type: "refinery", name: "Tongling", country: "China",
      lat: 30.95, lon: 117.82, tier: 1, operator: "Tongling Nonferrous",
      note: "Tweede Chinese reus (Anhui, aan de Yangtze); importeert concentraat via de oostkusthavens." },
    { id: "cu-ref-daye", type: "refinery", name: "Daye", country: "China",
      lat: 30.10, lon: 114.97, tier: 2, operator: "Daye Nonferrous",
      note: "Hubei; verwerkt o.a. Grasberg-concentraat." },
    { id: "cu-ref-xiangguang", type: "refinery", name: "Yanggu Xiangguang", country: "China",
      lat: 36.11, lon: 115.77, tier: 2, operator: "Yanggu Xiangguang",
      note: "Shandong; moderne flash-smelter op geïmporteerd concentraat." },
    { id: "cu-ref-jinchuan", type: "refinery", name: "Jinchuan (Jinchang)", country: "China",
      lat: 38.50, lon: 102.19, tier: 3, operator: "Jinchuan Group",
      note: "Gansu; verwerkt o.a. het Mongoolse Oyu Tolgoi-concentraat over land." },
    { id: "cu-ref-chuqui", type: "refinery", name: "Chuquicamata-smelter (Calama)", country: "Chili",
      lat: -22.46, lon: -68.93, tier: 2, operator: "Codelco",
      note: "Smelter/raffinaderij bij de mijn; Chili exporteert zowel concentraat als kathode." },
    { id: "cu-ref-caletones", type: "refinery", name: "Caletones", country: "Chili",
      lat: -34.28, lon: -70.44, tier: 3, operator: "Codelco",
      note: "Smelter van El Teniente, hoog in de Andes." },
    { id: "cu-ref-ilo", type: "refinery", name: "Ilo", country: "Peru",
      lat: -17.63, lon: -71.34, tier: 3, operator: "Southern Copper", coastal: true,
      note: "Kustsmelter/raffinaderij; verwerkt Peruaans concentraat tot kathode aan de Stille Oceaan." },
    { id: "cu-ref-japan", type: "refinery", name: "Saganoseki (Pan Pacific)", country: "Japan",
      lat: 33.24, lon: 131.88, tier: 2, operator: "JX / Pan Pacific Copper", coastal: true,
      note: "Grote Japanse kustsmelter; Japan importeert concentraat en exporteert kathode." },
    { id: "cu-ref-toyo", type: "refinery", name: "Toyo (Niihama)", country: "Japan",
      lat: 33.96, lon: 133.28, tier: 3, operator: "Sumitomo Metal Mining", coastal: true,
      note: "Shikoku; hoogwaardige kathode + verwerkt binnenlands schroot." },
    { id: "cu-ref-onsan", type: "refinery", name: "Onsan (LS-Nikko)", country: "Zuid-Korea",
      lat: 35.42, lon: 129.35, tier: 3, operator: "LS-Nikko Copper", coastal: true,
      note: "Ulsan; een van de grootste raffinaderijen ter wereld op één locatie." },
    { id: "cu-ref-aurubis", type: "refinery", name: "Aurubis Hamburg", country: "Duitsland",
      lat: 53.53, lon: 10.00, tier: 2, operator: "Aurubis", coastal: true,
      note: "Grootste koperraffinaderij van Europa; draait óók op enorme hoeveelheden schroot (secundair koper)." },
    { id: "cu-ref-glogow", type: "refinery", name: "KGHM Głogów", country: "Polen",
      lat: 51.66, lon: 16.09, tier: 3, operator: "KGHM",
      note: "Geïntegreerd met de Poolse mijn — mijn en smelter in één keten, uniek in de EU." },
    { id: "cu-ref-india", type: "refinery", name: "Dahej (Hindalco/Birla)", country: "India",
      lat: 21.70, lon: 72.60, tier: 3, operator: "Hindalco (Birla Copper)", coastal: true,
      note: "Gujarat; India importeert concentraat. (Vedanta's Tuticorin ligt sinds 2018 stil — een gat in de Aziatische capaciteit.)" },

    // ================================================================= HAVENS
    { id: "cu-port-antofagasta", type: "port", name: "Antofagasta / Mejillones", country: "Chili",
      lat: -23.65, lon: -70.40, tier: 2,
      note: "De koperhavenregio van Noord-Chili; vrijwel het complete Chileense concentraat en veel kathode verlaat hier het land." },
    { id: "cu-port-valparaiso", type: "port", name: "Valparaíso / San Antonio", country: "Chili",
      lat: -33.04, lon: -71.63, tier: 3,
      note: "Uitgang voor Centraal-Chili (Los Pelambres, El Teniente/Caletones)." },
    { id: "cu-port-callao", type: "port", name: "Callao", country: "Peru",
      lat: -12.05, lon: -77.15, tier: 2,
      note: "Hoofdhaven van Peru (bij Lima); overslag voor het noordelijke concentraat (o.a. Antamina)." },
    { id: "cu-port-matarani", type: "port", name: "Matarani", country: "Peru",
      lat: -17.00, lon: -72.10, tier: 3,
      note: "Zuid-Peru; exporthaven voor Cerro Verde en Las Bambas." },
    { id: "cu-port-amamapare", type: "port", name: "Amamapare", country: "Indonesië",
      lat: -4.85, lon: 136.90, tier: 3,
      note: "Freeports kusthaven onder de Grasberg-hooglanden; het concentraat gaat per pijp/rail naar de kade." },
    { id: "cu-port-townsville", type: "port", name: "Townsville", country: "Australië",
      lat: -19.25, lon: 146.82, tier: 3,
      note: "Queensland; uitgang voor het concentraat van Mount Isa." },
    { id: "cu-port-shanghai", type: "port", name: "Shanghai (Yangshan)", country: "China",
      lat: 30.62, lon: 122.07, tier: 2,
      note: "Grootste invoerpoort voor koperconcentraat en kathode; vandaar per spoor/binnenvaart de Yangtze-smelters in." },
    { id: "cu-port-ningbo", type: "port", name: "Ningbo-Zhoushan", country: "China",
      lat: 29.87, lon: 121.54, tier: 2,
      note: "Aanloophaven voor concentraat richting Jiangxi/Anhui; 's werelds drukste bulkhaven." },
    { id: "cu-port-durban", type: "port", name: "Durban", country: "Zuid-Afrika",
      lat: -29.87, lon: 31.03, tier: 2,
      note: "De hoofd-uitgang van de Copperbelt: ±2.700 km over land vanaf Kolwezi, dwars door Zambia en Zimbabwe." },
    { id: "cu-port-dar", type: "port", name: "Dar es Salaam", country: "Tanzania",
      lat: -6.82, lon: 39.29, tier: 3,
      note: "Oostelijke uitgang via de TAZARA-spoorcorridor; korter dan Durban." },
    { id: "cu-port-walvis", type: "port", name: "Walvis Bay", country: "Namibië",
      lat: -22.95, lon: 14.50, tier: 3,
      note: "Atlantische uitgang voor Zambisch koper — recht de oceaan op richting Europa/Amerika." },
    { id: "cu-port-lobito", type: "port", name: "Lobito", country: "Angola",
      lat: -12.36, lon: 13.55, tier: 3,
      note: "De Lobito-corridor: nieuwe/gerenoveerde spoorlijn naar de Atlantische Oceaan — verreweg de kortste weg naar zee voor het westelijke Copperbelt-koper." },
    { id: "cu-port-rotterdam", type: "port", name: "Rotterdam", country: "Nederland",
      lat: 51.95, lon: 4.14, tier: 3,
      note: "Aanloophaven voor de Europese markt; ook een LME-magazijnlocatie." },

    // ================================================================ MARKT
    { id: "cu-mkt-china-grid", type: "market", name: "China (net · bouw · EV)", country: "China",
      lat: 31.80, lon: 119.97, tier: 1,
      note: "Veruit de grootste vraag (~50%+): elektriciteitsnet, bouw, airco, elektronica en EV's." },
    { id: "cu-mkt-china-semis", type: "market", name: "Chinese draadstaven / semi's", country: "China",
      lat: 29.50, lon: 120.10, tier: 2,
      note: "Walserijen (Zhejiang/Jiangsu) die kathode omzetten in draadstaven, buizen en plaat." },
    { id: "cu-mkt-germany", type: "market", name: "Duitsland (kabels · auto)", country: "Duitsland",
      lat: 51.00, lon: 9.50, tier: 2,
      note: "Europees zwaartepunt: kabelfabrieken en de auto-industrie." },
    { id: "cu-mkt-usa", type: "market", name: "VS (net · bouw · EV)", country: "VS",
      lat: 39.00, lon: -84.00, tier: 2,
      note: "Grotendeels bevoorraad door binnenlandse SX-EW-kathode plus Mexicaans en Chileens koper." },
    { id: "cu-mkt-india", type: "market", name: "India", country: "India",
      lat: 22.50, lon: 78.50, tier: 3,
      note: "Snelst groeiende vraag; import gevoelig sinds Tuticorin stilligt." },
    { id: "cu-mkt-japankorea", type: "market", name: "Japan / Korea (elektronica)", country: "Japan",
      lat: 34.95, lon: 136.85, tier: 3, coastal: true,
      note: "Hoogwaardige semi's en elektronica (rond Nagoya); draaien op de eigen kustsmelters." },

    // ============================================================= RECYCLING
    // Schroot ≈ een derde van het aanbod. Nieuw schroot (fabricage-afval) en oud
    // schroot (end-of-life) gaan terug naar de smelters — stage `erts` (feedstock).
    { id: "cu-rec-europe", type: "recycler", name: "Europa (schroot)", country: "Duitsland",
      lat: 50.90, lon: 6.90, tier: 3,
      note: "EU-koperschroot → Aurubis (grootste secundaire smelter) + export naar China." },
    { id: "cu-rec-usa", type: "recycler", name: "VS (schroot, LA-export)", country: "VS",
      lat: 33.75, lon: -118.19, tier: 3, coastal: true,
      note: "De VS is een netto-schrootexporteur; historisch grote stroom over de Stille Oceaan naar Chinese smelters." },
    { id: "cu-rec-japan", type: "recycler", name: "Japan (schroot)", country: "Japan",
      lat: 35.50, lon: 139.70, tier: 3,
      note: "Binnenlands schroot terug naar Toyo/Saganoseki — Japan raffineert veel secundair koper." },

    // ============================ BEURSVOORRADEN (optionele toggle-laag)
    // type "exchange" -> alleen zichtbaar met de beursvoorraden-toggle.
    // `stock` (kt Cu) = magazijnvoorraad -> node-grootte. NUANCE: dit is buffer-/
    // handelsvoorraad, GEEN verbruik. LME/SHFE/COMEX zijn de prijszetters.
    { id: "cu-lme-rotterdam", type: "exchange", name: "LME Rotterdam", country: "Nederland",
      lat: 51.90, lon: 4.40, stock: 120, tier: 2, coastal: true, exchange: "LME",
      note: "Europees LME-magazijncluster; de referentievoorraad voor de Atlantische markt." },
    { id: "cu-lme-johor", type: "exchange", name: "LME Johor", country: "Maleisië",
      lat: 1.47, lon: 103.75, stock: 160, tier: 2, coastal: true, exchange: "LME",
      note: "Vlak bij Singapore/Malakka; het grootste Aziatische LME-magazijn — buffer tussen Afrika/Amerika en China." },
    { id: "cu-lme-busan", type: "exchange", name: "LME Busan", country: "Zuid-Korea",
      lat: 35.10, lon: 129.04, stock: 90, tier: 2, coastal: true, exchange: "LME",
      note: "Koreaanse LME-locatie; opvangvat voor Aziatische kathode." },
    { id: "cu-lme-kaohsiung", type: "exchange", name: "LME Kaohsiung", country: "Taiwan",
      lat: 22.62, lon: 120.30, stock: 60, tier: 3, coastal: true, exchange: "LME",
      note: "Taiwanees LME-magazijn." },
    { id: "cu-comex-neworleans", type: "exchange", name: "COMEX (New Orleans)", country: "VS",
      lat: 29.95, lon: -90.07, stock: 70, tier: 3, coastal: true, exchange: "COMEX",
      note: "Amerikaanse COMEX-magazijnen; in 2025 opgestuwd door de dreiging van Amerikaanse koperheffingen (arbitrage LME↔COMEX)." },
    { id: "cu-shfe-shanghai", type: "exchange", name: "SHFE (Shanghai, bonded)", country: "China",
      lat: 31.23, lon: 121.47, stock: 180, tier: 2, coastal: true, exchange: "SHFE",
      note: "Shanghai Futures Exchange + de bonded-voorraden: de Chinese prijs- en voorraadmotor." },
  ],

  // ==========================================================================
  // STROMEN — value in kt Cu/jaar. stage bepaalt de kleur (erts=concentraat dof,
  // raffinaat=kathode vol koper, product=halffabricaat licht). `via` = echte route
  // langs havens (cu-port-*) en de universele knelpunten (wp-* / grens-*).
  //
  //  A) Andes-CONCENTRAAT -> Chinese smelters (de hoofdtrechter, Stille Oceaan)
  //  B) Andes-concentraat -> eigen Chileense/Peruaanse smelters
  //  C) Andes/US/Mexico-KATHODE -> markt
  //  D) Copperbelt-KATHODE -> kust over land (Kasumbalesa) -> markt over zee
  //  E) Indonesië/Australië/Mongolië/Kazachstan -> Aziatische smelters
  //  F) Smelter -> halffabricaat/markt
  //  G) Recycling -> smelters (schroot terug)
  //  H) Beursvoorraden (layer:"exchange" -> alleen met de toggle)
  // ==========================================================================
  flows: [
    // === A. ANDES-CONCENTRAAT -> CHINESE SMELTERS (de koper-"aha") ===========
    { from: "cu-escondida", to: "cu-ref-jiangxi", value: 260, mode: "ship", stage: "erts",
      via: ["cu-port-antofagasta", "wp-pac-zuid", "wp-pac-west", "wp-taiwan", "cu-port-ningbo"],
      note: "Escondida → Jiangxi Copper: de dikste concentraatstroom ter wereld, dwars over de Stille Oceaan naar de grootste smelter ter wereld." },
    { from: "cu-collahuasi", to: "cu-ref-tongling", value: 150, mode: "ship", stage: "erts",
      via: ["cu-port-antofagasta", "wp-pac-zuid", "wp-pac-west", "wp-taiwan", "cu-port-shanghai"],
      note: "Collahuasi → Tongling; Anglo/Glencore-concentraat naar de Yangtze-smelters." },
    { from: "cu-lospelambres", to: "cu-ref-daye", value: 120, mode: "ship", stage: "erts",
      via: ["cu-port-valparaiso", "wp-pac-zuid", "wp-pac-west", "wp-taiwan", "cu-port-ningbo"],
      note: "Centraal-Chileens concentraat → Hubei." },
    { from: "cu-cerroverde", to: "cu-ref-xiangguang", value: 130, mode: "ship", stage: "erts",
      via: ["cu-port-matarani", "wp-pac-zuid", "wp-pac-west", "wp-taiwan", "cu-port-shanghai"],
      note: "Cerro Verde (Peru) → Shandong." },
    { from: "cu-antamina", to: "cu-ref-jiangxi", value: 140, mode: "ship", stage: "erts",
      via: ["cu-port-callao", "wp-pac-zuid", "wp-pac-west", "wp-taiwan", "cu-port-ningbo"],
      note: "Antamina → Jiangxi; koper-zink-concentraat via Callao." },
    { from: "cu-lasbambas", to: "cu-ref-tongling", value: 120, mode: "ship", stage: "erts",
      via: ["cu-port-matarani", "wp-pac-zuid", "wp-pac-west", "wp-taiwan", "cu-port-shanghai"],
      note: "Las Bambas → Tongling; MMG (China) bezit zowel de mijn als de afnemer." },

    // === B. ANDES-CONCENTRAAT -> EIGEN SMELTERS (kort, over land) ============
    { from: "cu-escondida", to: "cu-ref-chuqui", value: 90, mode: "rail", stage: "erts",
      note: "Deel van het Escondida-concentraat blijft in Chili (Codelco-smelter bij Calama)." },
    { from: "cu-elteniente", to: "cu-ref-caletones", value: 120, mode: "rail", stage: "erts",
      note: "El Teniente → de eigen smelter Caletones, hoog in de Andes." },
    { from: "cu-quellaveco", to: "cu-ref-ilo", value: 100, mode: "rail", stage: "erts",
      note: "Quellaveco → de kustsmelter Ilo." },
    { from: "cu-bingham", to: "cu-mkt-usa", value: 60, mode: "rail", stage: "raffinaat",
      note: "Bingham Canyon → eigen Kennecott-smelter → binnenlandse markt (volledig Amerikaans)." },

    // === C. KATHODE -> MARKT (raffinaat) ====================================
    { from: "cu-ref-chuqui", to: "cu-mkt-china-grid", value: 150, mode: "ship", stage: "raffinaat",
      via: ["cu-port-antofagasta", "wp-pac-zuid", "wp-pac-west", "wp-taiwan", "cu-port-shanghai"],
      note: "Chileense kathode → China: dezelfde Stille-Oceaan-route, maar nu als afgewerkt metaal." },
    { from: "cu-ref-ilo", to: "cu-mkt-china-grid", value: 80, mode: "ship", stage: "raffinaat",
      via: ["wp-pac-zuid", "wp-pac-west", "wp-taiwan", "cu-port-shanghai"],
      note: "Peruaanse kustkathode → China." },
    { from: "cu-ref-caletones", to: "cu-mkt-germany", value: 70, mode: "ship", stage: "raffinaat",
      via: ["cu-port-valparaiso", "wp-panama", "cu-port-rotterdam"],
      note: "Chileense kathode → Europa door het Panamakanaal, aan land in Rotterdam." },
    { from: "cu-morenci", to: "cu-mkt-usa", value: 120, mode: "rail", stage: "raffinaat",
      note: "Morenci-SX-EW-kathode → Amerikaanse markt, volledig over land (geen smelter, geen zee)." },
    { from: "cu-buenavista", to: "cu-mkt-usa", value: 90, mode: "rail", stage: "raffinaat",
      note: "Mexicaanse kathode → VS: recht de grens over. Mexico is een van de grootste VS-leveranciers." },

    // === D. AFRIKAANSE COPPERBELT — KATHODE OVER LAND, DAN ZEE ==============
    //  Landcorridor (rail/road via Kasumbalesa) tot de kust, dan een aparte
    //  scheeps-stroom vanaf de haven — precies zoals kobalt.
    { from: "cu-tenke", to: "cu-port-durban", value: 200, mode: "road", stage: "raffinaat",
      via: ["grens-kasumbalesa"],
      note: "SX-EW-kathode op vrachtwagens, ±2.700 km dwars door Zambia en Zimbabwe, door de grenspost Kasumbalesa." },
    { from: "cu-kolwezi", to: "cu-port-durban", value: 150, mode: "road", stage: "raffinaat",
      via: ["grens-kasumbalesa"],
      note: "Glencore-kathode volgt dezelfde zuidelijke corridor." },
    { from: "cu-kansanshi", to: "cu-port-durban", value: 100, mode: "rail", stage: "raffinaat",
      via: ["grens-kasumbalesa"],
      note: "Zambische kathode naar Durban." },
    { from: "cu-tenke", to: "cu-port-dar", value: 80, mode: "rail", stage: "raffinaat",
      note: "Oostelijke uitgang via de TAZARA-corridor naar Dar es Salaam." },
    { from: "cu-kamoa", to: "cu-port-lobito", value: 160, mode: "rail", stage: "raffinaat",
      note: "Kamoa-Kakula (blister/kathode) → de Lobito-corridor: de kortste weg naar zee, westwaarts naar de Atlantische Oceaan." },
    { from: "cu-sentinel", to: "cu-port-walvis", value: 60, mode: "rail", stage: "raffinaat",
      note: "Zambisch koper westwaarts naar Walvis Bay (Namibië)." },

    { from: "cu-port-durban", to: "cu-mkt-china-grid", value: 260, mode: "ship", stage: "raffinaat",
      via: ["wp-moz-noord", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan", "cu-port-shanghai"],
      note: "Durban → China: de Copperbelt-kathode over de Indische Oceaan, door Malakka naar de Chinese markt." },
    { from: "cu-port-dar", to: "cu-mkt-china-grid", value: 80, mode: "ship", stage: "raffinaat",
      via: ["wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan", "cu-port-ningbo"],
      note: "Dar es Salaam → China." },
    { from: "cu-port-durban", to: "cu-mkt-germany", value: 60, mode: "ship", stage: "raffinaat",
      via: ["wp-kaap", "cu-port-rotterdam"],
      note: "Deel van de Copperbelt-kathode → Europa, om Kaap de Goede Hoop." },
    { from: "cu-port-lobito", to: "cu-mkt-germany", value: 90, mode: "ship", stage: "raffinaat",
      via: ["cu-port-rotterdam"],
      note: "Lobito → Rotterdam: recht de Atlantische Oceaan over, zónder Kaap of Malakka." },
    { from: "cu-port-walvis", to: "cu-mkt-germany", value: 40, mode: "ship", stage: "raffinaat",
      via: ["cu-port-rotterdam"],
      note: "Walvis Bay → Europa: recht de Atlantische Oceaan op naar Rotterdam." },

    // === E. INDONESIË / AUSTRALIË / MONGOLIË / KAZACHSTAN -> AZIË ============
    { from: "cu-grasberg", to: "cu-ref-daye", value: 180, mode: "ship", stage: "erts",
      via: ["cu-port-amamapare", "wp-makassar", "wp-scs", "wp-taiwan", "cu-port-shanghai"],
      note: "Grasberg-concentraat → Chinese smelter, via de Straat van Makassar." },
    { from: "cu-grasberg", to: "cu-ref-japan", value: 90, mode: "ship", stage: "erts",
      via: ["cu-port-amamapare", "wp-scs", "wp-taiwan"],
      note: "Grasberg → Japan (Saganoseki); Freeport levert al decennia aan Japanse smelters." },
    { from: "cu-mountisa", to: "cu-ref-tongling", value: 80, mode: "ship", stage: "erts",
      via: ["cu-port-townsville", "wp-lombok", "wp-makassar", "wp-scs", "wp-taiwan", "cu-port-ningbo"],
      note: "Australisch concentraat via Townsville en de Indonesische straten naar China." },
    { from: "cu-oyutolgoi", to: "cu-ref-jinchuan", value: 120, mode: "rail", stage: "erts",
      note: "Oyu Tolgoi → China over land: het concentraat steekt de grens over naar de Gansu-smelter." },
    { from: "cu-kazakhstan", to: "cu-mkt-china-grid", value: 90, mode: "rail", stage: "raffinaat",
      note: "Kazachse kathode per spoor de grens over naar Xinjiang." },
    { from: "cu-olympicdam", to: "cu-mkt-japankorea", value: 70, mode: "ship", stage: "raffinaat",
      via: ["cu-port-townsville", "wp-lombok", "wp-makassar", "wp-scs", "wp-taiwan"],
      note: "Zuid-Australische kathode (Olympic Dam) → Oost-Azië." },

    // === F. SMELTER -> HALFFABRICAAT / MARKT (product) ======================
    { from: "cu-ref-jiangxi", to: "cu-mkt-china-semis", value: 220, mode: "rail", stage: "product",
      note: "Chinese kathode → draadstaven en buizen (walserijen Zhejiang/Jiangsu)." },
    { from: "cu-ref-tongling", to: "cu-mkt-china-grid", value: 180, mode: "rail", stage: "product",
      note: "Tongling-kathode → het Chinese elektriciteitsnet en de bouw." },
    { from: "cu-ref-daye", to: "cu-mkt-china-semis", value: 120, mode: "rail", stage: "product" },
    { from: "cu-ref-aurubis", to: "cu-mkt-germany", value: 110, mode: "rail", stage: "product",
      note: "Aurubis-kathode → Duitse kabel- en auto-industrie." },
    { from: "cu-ref-glogow", to: "cu-mkt-germany", value: 60, mode: "rail", stage: "product",
      note: "Poolse kathode → Midden-Europese fabricage." },
    { from: "cu-ref-onsan", to: "cu-mkt-japankorea", value: 90, mode: "ship", stage: "product",
      note: "Koreaanse kathode → Japanse/Koreaanse elektronica, over de Straat van Korea." },
    { from: "cu-ref-japan", to: "cu-mkt-japankorea", value: 80, mode: "road", stage: "product" },
    { from: "cu-ref-india", to: "cu-mkt-india", value: 50, mode: "rail", stage: "product",
      note: "Dahej-kathode → de snelgroeiende Indiase vraag." },

    // === G. RECYCLING -> SMELTERS (schroot terug, stage erts) ===============
    { from: "cu-rec-europe", to: "cu-ref-aurubis", value: 120, mode: "road", stage: "erts",
      note: "Europees koperschroot → Aurubis; secundair koper is ±40% van de Aurubis-input." },
    { from: "cu-rec-usa", to: "cu-ref-jiangxi", value: 90, mode: "ship", stage: "erts",
      via: ["wp-pac-noord", "cu-port-ningbo"],
      note: "Amerikaans schroot over de Stille Oceaan naar Chinese smelters — historisch een van de grootste schrootstromen ter wereld." },
    { from: "cu-rec-japan", to: "cu-ref-toyo", value: 50, mode: "road", stage: "erts",
      note: "Japans schroot → Sumitomo Toyo (over de Seto-brug naar Shikoku)." },

    // === H. BEURSVOORRADEN (layer:"exchange" -> alleen met de toggle) =======
    { from: "cu-ref-jiangxi", to: "cu-shfe-shanghai", value: 60, mode: "rail", stage: "raffinaat", layer: "exchange",
      note: "Chinese kathode → SHFE/bonded-voorraden: de Shanghai-buffer." },
    { from: "cu-ref-aurubis", to: "cu-lme-rotterdam", value: 40, mode: "road", stage: "raffinaat", layer: "exchange",
      note: "Europese kathode → LME Rotterdam." },
    { from: "cu-port-durban", to: "cu-lme-johor", value: 55, mode: "ship", stage: "raffinaat", layer: "exchange",
      via: ["wp-moz-noord", "wp-aceh", "wp-malakka", "wp-singapore"],
      note: "Copperbelt-kathode → LME Johor, het Aziatische opvangmagazijn bij Singapore." },
    { from: "cu-ref-chuqui", to: "cu-lme-busan", value: 40, mode: "ship", stage: "raffinaat", layer: "exchange",
      via: ["cu-port-antofagasta", "wp-pac-zuid", "wp-pac-west", "wp-taiwan"],
      note: "Chileense kathode → LME Busan." },
    { from: "cu-ref-onsan", to: "cu-lme-kaohsiung", value: 20, mode: "ship", stage: "raffinaat", layer: "exchange",
      via: ["wp-taiwan"],
      note: "Koreaanse kathode → LME Kaohsiung." },
    { from: "cu-morenci", to: "cu-comex-neworleans", value: 30, mode: "rail", stage: "raffinaat", layer: "exchange",
      note: "Amerikaanse kathode → COMEX-magazijnen; in 2025 opgestuwd door de heffingsdreiging (arbitrage met de LME)." },
    { from: "cu-lme-johor", to: "cu-mkt-china-grid", value: 45, mode: "ship", stage: "raffinaat", layer: "exchange",
      via: ["wp-singapore", "wp-scs", "wp-taiwan", "cu-port-shanghai"],
      note: "Buffer stroomt door naar de vraag: LME Johor → Chinese markt. Voorraad ≠ verbruik, maar hij beweegt wél." },
  ],

  // ==========================================================================
  // SPANNINGEN — waar de koperketen knijpt. Verwijst naar de universele
  // knelpuntenlijst (wp-* / grens-*). flows-verwijzing: "from-id>to-id".
  // ==========================================================================
  tensions: [
    { id: "cu-t-china-smelt", type: "concentratie", title: "China: ~50% van de smeltcapaciteit",
      lat: 29.5, lon: 116.5,
      nodes: ["cu-ref-jiangxi", "cu-ref-tongling", "cu-ref-daye", "cu-ref-xiangguang", "cu-ref-jinchuan"],
      flows: ["cu-escondida>cu-ref-jiangxi", "cu-collahuasi>cu-ref-tongling",
              "cu-cerroverde>cu-ref-xiangguang", "cu-antamina>cu-ref-jiangxi",
              "cu-grasberg>cu-ref-daye"],
      metric: "mijnbouw top-1 (Chili) ≈ 24% · raffinage top-1 (China) ≈ 50%",
      note: "Zoals bij lithium zit de kwetsbaarheid niet bij het graven maar één stap verderop: de wereld graaft breed, maar de helft van het erts wordt in China gesmolten. Andes-concentraat vaart de Stille Oceaan over en komt als kathode terug — een dikke bundel bogen die convergeert op de Chinese oostkust." },

    { id: "cu-t-escondida", type: "spof", title: "Escondida: één mijn, de grootste ter wereld",
      lat: -24.27, lon: -69.07,
      nodes: ["cu-escondida", "cu-collahuasi", "cu-port-antofagasta"],
      flows: ["cu-escondida>cu-ref-jiangxi", "cu-escondida>cu-ref-chuqui"],
      metric: "≈ 1.050 kt Cu/j uit één mijn — ±5% van de wereld",
      note: "De Atacama-woestijn is het zwaartepunt van de wereldkoperwinning, en Escondida is de grootste put. Een staking (zoals in 2017), een aardbeving of een watertekort in de droogste woestijn ter wereld is meteen wereldnieuws op de kopermarkt." },

    { id: "cu-t-copperbelt", type: "knelpunt", title: "Copperbelt: kathode die eerst over land moet",
      lat: -12.22, lon: 27.79,
      nodes: ["cu-tenke", "cu-kolwezi", "cu-kamoa", "cu-kansanshi", "grens-kasumbalesa",
              "cu-port-durban", "cu-port-dar", "cu-port-lobito", "cu-port-walvis"],
      flows: ["cu-tenke>cu-port-durban", "cu-kolwezi>cu-port-durban", "cu-kansanshi>cu-port-durban",
              "cu-tenke>cu-port-dar", "cu-kamoa>cu-port-lobito", "cu-sentinel>cu-port-walvis"],
      metric: "DR Congo + Zambia landlocked — grenspost Kasumbalesa: files van dagen",
      note: "De tweede trechter. Anders dan de Andes reist de Copperbelt niet als concentraat maar als SX-EW-KATHODE, en anders dan de zee-routes moet hij eerst honderden tot duizenden kilometers over LAND: zuid naar Durban (via Kasumbalesa), oost naar Dar es Salaam (TAZARA), of west naar Lobito/Walvis Bay. De keuze tussen die corridors is een geopolitiek gevecht (VS-Lobito vs. China-TAZARA)." },

    { id: "cu-t-sxew", type: "structureel", title: "Concentraat vs. kathode: twee productvormen",
      lat: -6.0, lon: 60.0,
      nodes: ["cu-escondida", "cu-tenke", "cu-morenci", "cu-ref-jiangxi"],
      flows: ["cu-escondida>cu-ref-jiangxi", "cu-tenke>cu-port-durban", "cu-morenci>cu-mkt-usa"],
      metric: "sulfide-concentraat → smelter · oxide-erts → SX-EW-kathode bij de bron",
      note: "Koper reist in twee vormen. Sulfide-erts wordt tot concentraat (~30% Cu) verwerkt en moet nog naar een smelter — dat is de lange reis naar China. Oxide-erts wordt bij de mijn met SX-EW direct tot kathode geraffineerd (Copperbelt, Morenci, Buenavista) en reist meteen als afgewerkt metaal, zónder smelter-tussenstop. Op de kaart: donkere concentraatbogen die knijpen bij China, tegenover volle koperkleurige kathode die direct de markt op gaat." },

    { id: "cu-t-exchange", type: "beleid", title: "Beursvoorraden: LME · SHFE · COMEX",
      lat: 1.47, lon: 103.75,
      nodes: ["cu-lme-johor", "cu-shfe-shanghai", "cu-comex-neworleans", "cu-lme-rotterdam"],
      flows: ["cu-port-durban>cu-lme-johor", "cu-ref-jiangxi>cu-shfe-shanghai",
              "cu-morenci>cu-comex-neworleans", "cu-lme-johor>cu-mkt-china-grid"],
      metric: "buffer-, geen verbruiksvoorraad — de prijszetters van de wereld",
      note: "Zet de beursvoorraden-laag aan om de magazijnen van de LME, SHFE en COMEX te zien. Belangrijke nuance: dit is handels-/buffervoorraad, geen consumptie. In 2025 zoog de dreiging van Amerikaanse koperheffingen enorme hoeveelheden koper naar de COMEX-magazijnen in de VS — een prijsvervorming die puur uit beleid ontstond, niet uit vraag." },
  ],
});
