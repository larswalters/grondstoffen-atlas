// ============================================================================
// AARDGAS / LNG (CH4) — volledig uitgewerkte module. Peiljaar ±2023-2024.
// Cijfers indicatief/afgerond in bcm/jaar (miljard m3 gas-equivalent), o.b.v.
// IEA (Gas Market Report / WEO), IGU World LNG Report, EIA, Energy Institute
// Statistical Review 2024 en bedrijfsrapportages (QatarEnergy, Cheniere, Equinor,
// Gazprom/Novatek, Sonatrach). Wereldproductie ~4000 bcm; LNG-handel ~550 bcm.
// Zie design/gas.md. Tweede ECHT NIEUWE grondstof na zilver (M13) — de 12e.
//
// DE VORM VAN GAS (bepaald door de natuurkunde: gas is nauwelijks te verplaatsen):
//   - TWEE GESCHEIDEN LEVERSYSTEMEN. Over land zit gas vast in PIJPLEIDINGEN
//     (regionaal, captive: wie aan het andere eind zit is je enige klant/
//     leverancier — Rusland<->Europa was, Rusland->China, Turkmenistan->China,
//     Noorwegen->Europa). Echt globaal wordt gas pas na VLOEIBAARMAKING tot LNG
//     (-162 C) in een handvol peperdure exportterminals.
//   - DE LIQUEFACTIE-STAP IS DE TRECHTER (institutioneel/kapitaal, geen zeestraat):
//     pas na vloeibaarmaking is een molecuul een verhandelbare, omleidbare
//     wereldgrondstof. Capaciteit geconcentreerd bij DRIE POLEN: VS-Golfkust
//     (flexibele cargo's), Qatar (Ras Laffan, alles via HORMUZ), Australie (-> Azie).
//   - TWEE LEVENDE HER-ROUTERINGEN: de Europa-pivot 2022 (Nord Stream weg -> LNG +
//     FSRU's in maanden, TTF-piek) en de Russische pivot naar het oosten (Power of
//     Siberia + Arctisch LNG) — de kaart beweegt mee met oorlog en sancties.
//
// STAGES (via `stage`):
//   erts       = veldgas + PIJPLEIDINGGAS (de lage donkere captive land-arcs) ->
//                ook de korte veld->liquefactie-hop. Dof/donker.
//   raffinaat  = LNG (vloeibaar gemaakt — de heldere oceaan-arcs = het verhaal).
//   product    = hervergast/geleverd (stroom/industrie/verwarming). Licht.
//
// TRANSPORT is LNG-tanker (ship) + pipeline (beide bestaan; pipeline kwam met olie).
// GEEN nieuwe render-modus, GEEN nieuwe marker-types (liquefactie = refinery, regas
// = port, opslag = reserve), GEEN nieuw chokepoint: 4e grondstof na nikkel/olie/
// zilver die volledig op de bestaande routekaart draait (Hormuz/Malakka/Suez/Bab/
// Rode Zee/Gibraltar/Panama/Kaap/Lombok/Makassar/SCS/Taiwan/Florida). Qatar's
// Hormuz-afhankelijkheid is SCHERPER dan olie: geen Yanbu/Fujairah-bypass.
//
// OPSLAG (type "reserve" / flow.layer "reserve") = de BESTAANDE optionele toggle van
// olie (SPR), hergebruikt zonder engine-wijziging (hasReserves() generiek op
// n.type==="reserve"). De EU-winter-vulgraad (90%-mandaat) = de geopolitieke metric
// na 2022. Default uit.
// ============================================================================

REGISTER({
  id: "gas",
  name: "Aardgas",
  symbol: "LNG",
  color: "#4FB6D6",       // koel gas-/vlamblauw: de veld-markers
  flowColor: "#A9E0EF",   // lichter cyaan: de stromen tegen de donkere bol
  detail: "uitgewerkt",
  unit: "bcm/jaar (indicatief)",
  blurb: "Aardgas is de grondstof die je nauwelijks kunt verplaatsen. Over land zit het " +
    "vast in pijpleidingen (regionaal, captive — Rusland<->Europa, Rusland->China, " +
    "Centraal-Azie->China); echt globaal wordt het pas na vloeibaarmaking tot LNG (-162 C) " +
    "in een handvol dure exportterminals (VS-Golfkust, Qatar, Australie) — dat is de " +
    "trechter, niet een zeestraat. Sinds 2022 verving Europa Russische pijp door LNG. " +
    "Qatar's LNG kan alleen via Hormuz.",

  nodes: [
    // ==================================================== GASVELDEN (mine)
    // De drie exportpolen (VS/Qatar/Australie) + de captive pijp-reuzen
    // (Rusland/Turkmenistan/Noorwegen). Iran = het scherpste reserves != export.
    // --- VS: de schalie-ommekeer, grootste producent ------------------------
    { id: "gas-us", type: "mine", name: "VS-schalie (Appalachia/Permian/Haynesville)", country: "VS",
      lat: 31.50, lon: -93.80, share: 24, tier: 1, operator: "div. (EQT/ExxonMobil e.a.)",
      status: "actief", capacity: "~1.030 bcm/j",
      note: "Grootste gasproducent ter wereld. Marcellus (Appalachia) is het grootste bekken; het Golfkust-gas (Permian/Haynesville) voedt de LNG-terminals + pijp naar Mexico. Van importeur naar #1 LNG-exporteur in ~10 jaar." },

    // --- Rusland: de pivot naar het oosten ----------------------------------
    { id: "gas-russia", type: "mine", name: "Rusland (West-Siberie: Nadym-Pur-Taz/Yamal)", country: "Rusland",
      lat: 66.00, lon: 76.50, share: 16, tier: 1, operator: "Gazprom/Novatek",
      status: "actief", capacity: "~640 bcm/j",
      note: "2e producent. Leverde decennia ~150 bcm/j pijpgas aan Europa; sinds 2022 gekrompen tot een draadje en pivot naar China (Power of Siberia) + Arctisch LNG (Yamal/Sabetta)." },
    { id: "gas-russia-east", type: "mine", name: "Rusland-Oost (Sachalin-offshore)", country: "Rusland",
      lat: 52.50, lon: 143.30, share: 2, tier: 3, operator: "Gazprom (was Shell)",
      status: "actief", capacity: "~30 bcm/j",
      note: "Aparte oostelijke productie (Sachalin-schelf), niet verbonden met de West-Siberische velden. Voedt Sachalin-2-LNG -> Japan/Korea." },

    // --- Qatar / Iran: hetzelfde veld, tegenovergestelde export -------------
    { id: "gas-qatar", type: "mine", name: "Qatar (North Field)", country: "Qatar",
      lat: 25.55, lon: 51.25, share: 12, tier: 1, operator: "QatarEnergy",
      status: "actief", capacity: "~180 bcm/j",
      note: "'s Werelds grootste gasveld (offshore, gedeeld met Iran). Gas komt aan land en gaat als LNG via Ras Laffan de zee op — alles door de Straat van Hormuz. North Field-uitbreiding onderweg." },
    { id: "gas-iran", type: "mine", name: "Iran (South Pars)", country: "Iran",
      lat: 27.45, lon: 52.60, share: 6, tier: 2, operator: "NIOC",
      status: "actief", capacity: "~260 bcm/j",
      note: "ZELFDE VELD als Qatar's North Field (South Pars). Ondanks reusachtige reserves nauwelijks export — sancties + eigen groot binnenlands verbruik. Het scherpste reserves != export-contrast (zoals Venezuela bij olie)." },

    // --- Australie: naar Azie ------------------------------------------------
    { id: "gas-australia-nw", type: "mine", name: "Australie NW Shelf/Gorgon/Ichthys", country: "Australie",
      lat: -21.00, lon: 116.00, share: 9, tier: 1, operator: "Woodside/Chevron/INPEX",
      status: "actief", capacity: "~110 bcm/j",
      note: "Offshore gas van de West-Australische schelf -> Karratha/Darwin-LNG. Top-exporteur naar NO-Azie (Japan/Korea/China)." },
    { id: "gas-australia-qld", type: "mine", name: "Australie Queensland (steenkoolgas)", country: "Australie",
      lat: -26.40, lon: 150.50, share: 3, tier: 2, operator: "Santos/Shell/Origin",
      status: "actief", capacity: "~40 bcm/j",
      note: "Coal-bed methane (CBM) uit het Surat/Bowen-bekken -> Gladstone-LNG op Curtis Island. Australie's oostelijke exportbron." },

    // --- Captive pijp-reuzen: Turkmenistan / Noorwegen / Azerbeidzjan -------
    { id: "gas-turkmenistan", type: "mine", name: "Turkmenistan (Galkynysh)", country: "Turkmenistan",
      lat: 38.50, lon: 62.20, share: 2, tier: 2, operator: "Turkmengaz",
      status: "actief", capacity: "~80 bcm/j",
      note: "4e reserves ter wereld, maar LANDLOCKED -> volledig captive aan de Centraal-Azie-China-pijp. China is vrijwel de enige klant." },
    { id: "gas-norway", type: "mine", name: "Noorwegen (Troll/Ormen Lange)", country: "Noorwegen",
      lat: 60.50, lon: 4.90, share: 3, tier: 1, operator: "Equinor",
      status: "actief", capacity: "~120 bcm/j",
      note: "Europa's #1 leverancier NA het wegvallen van Rusland — offshore velden aangeland en per (subsea-)pijp naar VK/Duitsland/Belgie. De betrouwbare buur." },
    { id: "gas-azerbaijan", type: "mine", name: "Azerbeidzjan (Shah Deniz)", country: "Azerbeidzjan",
      lat: 40.20, lon: 49.60, share: 1, tier: 3, operator: "BP/SOCAR",
      status: "actief", capacity: "~25 bcm/j",
      note: "Zuidelijke Gascorridor: Shah Deniz -> Sangachal -> TANAP -> TAP -> Italie/Balkan — de pijp die Europa om Rusland heen aanlegde." },

    // --- Algerije / Nigeria / Maleisie: Med- + Atlantisch + ZO-Azie-LNG -----
    { id: "gas-algeria", type: "mine", name: "Algerije (Hassi R'Mel)", country: "Algerije",
      lat: 32.90, lon: 3.30, share: 2, tier: 2, operator: "Sonatrach",
      status: "actief", capacity: "~100 bcm/j",
      note: "Sahara-gas -> LNG (Arzew/Skikda) EN pijp (Transmed/Medgaz) naar Zuid-Europa. Op de kaart getekend via z'n LNG (de Med-pijpleidingen zijn subsea en vallen buiten het land-routeringsraster)." },
    { id: "gas-nigeria", type: "mine", name: "Nigeria (Nigerdelta/NLNG)", country: "Nigeria",
      lat: 5.30, lon: 6.80, share: 2, tier: 2, operator: "NLNG (NNPC/Shell/TotalEnergies/Eni)",
      status: "actief", capacity: "~50 bcm/j",
      note: "Associated gas uit de Nigerdelta -> Bonny Island-LNG -> Europa/Azie. West-Afrika's grootste LNG-bron." },
    { id: "gas-malaysia", type: "mine", name: "Maleisie (Sarawak)", country: "Maleisie",
      lat: 4.40, lon: 114.00, share: 2, tier: 3, operator: "Petronas",
      status: "actief", capacity: "~75 bcm/j",
      note: "Sarawak-offshore-gas -> het grote Bintulu-LNG-complex -> Japan/Korea/China. Een van 's werelds oudste LNG-exporteurs." },

    // ===================================== LIQUEFACTIE-TERMINALS (refinery)
    // DE TRECHTER: hier wordt captive gas een verhandelbare wereldgrondstof.
    // Elke terminal `coastal:true` — de LNG-tanker gaat er direct de zee op.
    // --- VS-Golfkust: flexibele cargo's, fannen oost EN west -----------------
    { id: "gas-lng-sabinepass", type: "refinery", name: "Sabine Pass (Cheniere)", country: "VS",
      lat: 29.73, lon: -93.87, tier: 1, operator: "Cheniere", coastal: true, capacity: "~40 bcm/j",
      note: "Grootste VS-LNG-terminal (Louisiana). Flexibele bestemming-cargo's: varen naar de hoogste prijs (TTF/JKM) — de zwing-leverancier die in 2022 naar Europa herorienteerde." },
    { id: "gas-lng-corpus", type: "refinery", name: "Corpus Christi + Golfkust-cluster", country: "VS",
      lat: 27.83, lon: -97.05, tier: 1, operator: "Cheniere/Venture Global e.a.", coastal: true, capacity: "~35 bcm/j",
      note: "Texas/Louisiana-export (+ Calcasieu Pass/Plaquemines/Freeport nieuwbouw). Golfkust->Azie-cargo's vechten om Panamakanaal-slots." },

    // --- Qatar: het grootste complex, alles via Hormuz ----------------------
    { id: "gas-lng-raslaffan", type: "refinery", name: "Ras Laffan", country: "Qatar",
      lat: 25.90, lon: 51.55, tier: 1, operator: "QatarEnergy", coastal: true, capacity: "~110 bcm/j",
      note: "'s Werelds grootste LNG-complex. ALLE cargo's moeten door de Straat van Hormuz — geen enkele bypass (anders dan olie's Yanbu/Fujairah). North Field-uitbreiding verdubbelt de capaciteit." },

    // --- Australie: naar NO-Azie --------------------------------------------
    { id: "gas-lng-karratha", type: "refinery", name: "Karratha (NW Shelf/Pluto)", country: "Australie",
      lat: -20.60, lon: 116.77, tier: 1, operator: "Woodside", coastal: true, capacity: "~40 bcm/j",
      note: "West-Australisch LNG -> Japan/Korea/China via Lombok/Makassar en de Zuid-Chinese Zee." },
    { id: "gas-lng-gladstone", type: "refinery", name: "Gladstone (Curtis Island)", country: "Australie",
      lat: -23.77, lon: 151.30, tier: 2, operator: "Santos/Shell/ConocoPhillips", coastal: true, capacity: "~30 bcm/j",
      note: "Queensland CBM-LNG op Curtis Island (oostkust) -> Japan/Azie via de Coral Zee en de westelijke Stille Oceaan." },
    { id: "gas-lng-darwin", type: "refinery", name: "Darwin (Ichthys/Bayu-Undan)", country: "Australie",
      lat: -12.42, lon: 130.87, tier: 2, operator: "INPEX/Santos", coastal: true, capacity: "~15 bcm/j",
      note: "Noord-Australisch LNG (Ichthys-gas 890 km subsea aangevoerd) -> Japan, de kortste Australie->NO-Azie-route." },

    // --- Rusland: Arctisch + Pacific ----------------------------------------
    { id: "gas-lng-sabetta", type: "refinery", name: "Sabetta (Yamal LNG)", country: "Rusland",
      lat: 71.27, lon: 72.06, tier: 2, operator: "Novatek", coastal: true, capacity: "~25 bcm/j",
      note: "Arctisch LNG op het Jamal-schiereiland: west over de Barentszzee naar Europa, oost over de Noordelijke Zeeroute naar China (alleen 's zomers ijsvrij). Arctic LNG 2 gesanctioneerd." },
    { id: "gas-lng-sakhalin", type: "refinery", name: "Sachalin-2 (Prigorodnoje)", country: "Rusland",
      lat: 46.63, lon: 143.40, tier: 2, operator: "Gazprom (was Shell)", coastal: true, capacity: "~15 bcm/j",
      note: "Russisch Pacific-LNG op Zuid-Sachalin -> Japan/Korea (kort). Japan bleef afnemen ondanks de sancties (energiezekerheid)." },

    // --- Algerije / Nigeria / Maleisie --------------------------------------
    { id: "gas-lng-arzew", type: "refinery", name: "Arzew/Skikda", country: "Algerije",
      lat: 35.80, lon: -0.27, tier: 2, operator: "Sonatrach", coastal: true, capacity: "~20 bcm/j",
      note: "Algerijns LNG (naast de Transmed/Medgaz-pijpleidingen) -> Zuid-Europa over de West-Middellandse Zee." },
    { id: "gas-lng-bonny", type: "refinery", name: "Bonny Island (NLNG)", country: "Nigeria",
      lat: 4.42, lon: 7.16, tier: 2, operator: "NLNG", coastal: true, capacity: "~30 bcm/j",
      note: "West-Afrikaans LNG -> Europa (via Gibraltar) + Azie (om de Kaap). Nigeria's belangrijkste gasexport." },
    { id: "gas-lng-bintulu", type: "refinery", name: "Bintulu (Petronas)", country: "Maleisie",
      lat: 3.20, lon: 113.05, tier: 2, operator: "Petronas", coastal: true, capacity: "~30 bcm/j",
      note: "Groot ZO-Aziatisch LNG-complex -> Japan/Korea/China via de Zuid-Chinese Zee en de Straat van Taiwan." },

    // ===================================== REGAS / IMPORT-TERMINALS (port)
    // Waar LNG landt en het net in gaat. Europa (nieuw bekken) + China/India
    // landen aan de kust en pijpen landinwaarts; Japan/Korea/Taiwan zijn zelf
    // kustmarkten (zie hieronder). Alle `coastal:true`.
    { id: "gas-regas-nl", type: "port", name: "Rotterdam/Eemshaven (Gate + EemsEnergy)", country: "Nederland",
      lat: 53.44, lon: 6.84, tier: 1, coastal: true,
      note: "Noordwest-Europese LNG-gateway; ontvangt US/Qatar/Nigeria/Yamal-cargo's en voedt het Duitse/NW-Europese net." },
    { id: "gas-regas-de", type: "port", name: "Wilhelmshaven/Brunsbuttel (FSRU's)", country: "Duitsland",
      lat: 53.60, lon: 8.10, tier: 1, coastal: true,
      note: "IN MAANDEN GEBOUWD na 2022 — het symbool van de pivot. Duitsland had voor de oorlog 0 LNG-terminals; drijvende FSRU's overbrugden het gat toen Nord Stream wegviel." },
    { id: "gas-regas-uk", type: "port", name: "Isle of Grain/Milford Haven", country: "VK",
      lat: 51.45, lon: 0.45, tier: 2, coastal: true,
      note: "VK-import + doorvoer naar het continent (interconnector, tweerichting via de Kanaaltunnel-corridor)." },
    { id: "gas-regas-es", type: "port", name: "Barcelona/Sines (Iberische hub)", country: "Spanje",
      lat: 41.35, lon: 2.15, tier: 2, coastal: true,
      note: "Grootste EU-regascapaciteit, MAAR beperkte pijpuitgang noordwaarts (het 'Iberische eiland' — de Pyreneeen als flessenhals)." },
    { id: "gas-regas-cn", type: "port", name: "Rudong/Yangshan (Oost-China)", country: "China",
      lat: 32.55, lon: 121.20, tier: 1, coastal: true,
      note: "Chinese LNG-landing (Jiangsu-kust), naast de pijp uit Rusland (Power of Siberia) en Centraal-Azie. China = nu 's werelds #1 LNG-importeur." },
    { id: "gas-regas-in", type: "port", name: "Dahej", country: "India",
      lat: 21.70, lon: 72.55, tier: 2, coastal: true,
      note: "Grootste Indiase regasterminal (Gujarat); gas <-> kunstmest/ammoniak + stroom." },

    // ============================================= VERBRUIKSMARKTEN (market)
    // Continentale markten (EU/China/India) landinwaarts; eiland-/kustmarkten
    // (Japan/Korea/Taiwan/Brazilie) `coastal:true` -> de LNG-tanker landt er direct.
    { id: "gas-mkt-eu", type: "market", name: "NW-Europa (stroom/industrie/verwarming)", country: "Duitsland",
      lat: 50.90, lon: 9.00, tier: 1,
      note: "Het NIEUWE LNG-hart: sinds 2022 gevoed door LNG (via NL/DE/UK) + Noorse/Azerische pijp i.p.v. Russische pijp. Zet de TTF-benchmark." },
    { id: "gas-mkt-china", type: "market", name: "China (Oost — stroom/industrie)", country: "China",
      lat: 31.00, lon: 117.00, tier: 1,
      note: "Grootste LNG-importeur; combineert kust-LNG met pijpgas uit Rusland (POS) en Centraal-Azie (Turkmenistan). Gas verdringt kolen in de kuststeden." },
    { id: "gas-mkt-india", type: "market", name: "India (West — stroom/kunstmest)", country: "India",
      lat: 22.30, lon: 74.50, tier: 2,
      note: "Groeiende importeur; gas is cruciaal voor kunstmest/ammoniak. Prijsgevoelig — schakelt bij hoge JKM terug naar kolen." },
    { id: "gas-mkt-japan", type: "market", name: "Japan (Tokyo Bay)", country: "Japan",
      lat: 35.43, lon: 139.95, tier: 1, coastal: true,
      note: "Decennialang #1 LNG-importeur (versneld na Fukushima 2011). Vrijwel geen eigen productie -> volledig LNG-afhankelijk; lange-termijncontracten met Qatar/Australie/VS." },
    { id: "gas-mkt-korea", type: "market", name: "Zuid-Korea (Gwangyang/Incheon)", country: "Zuid-Korea",
      lat: 34.95, lon: 127.70, tier: 1, coastal: true,
      note: "Top-3 LNG-importeur, geen eigen productie. Landt cargo's aan de zuidkust (na de Straat van Taiwan)." },
    { id: "gas-mkt-taiwan", type: "market", name: "Taiwan (Yong'an/Taichung)", country: "Taiwan",
      lat: 22.85, lon: 120.20, tier: 2, coastal: true,
      note: "Volledig LNG-afhankelijk met WEINIG opslag (~2 weken) -> extreem kwetsbaar voor een blokkade-scenario. Het scherpste energiezekerheidsrisico van de atlas." },
    { id: "gas-mkt-us", type: "market", name: "VS binnenland (stroom/industrie)", country: "VS",
      lat: 32.50, lon: -90.00, tier: 1,
      note: "Grootste gasverbruiker ter wereld, vrijwel volledig op EIGEN productie (Henry Hub-benchmark, structureel goedkoop). Het pijp-net dat de VS zelfvoorzienend maakt." },
    { id: "gas-mkt-latam", type: "market", name: "Latijns-Amerika (Santos/Brazilie)", country: "Brazilie",
      lat: -23.96, lon: -46.30, tier: 3, coastal: true,
      note: "LNG-import als BACKUP bij droogte: valt de waterkracht weg, dan springen gascentrales bij -> spot-cargo's uit de VS-Golfkust." },

    // ================================================ OPSLAG (reserve, toggle)
    // Optionele laag: hergebruikt het olie-SPR-patroon (type "reserve" / layer
    // "reserve") met 0 engine-wijziging. `stock` in bcm -> markergrootte. Default uit.
    { id: "gas-store-eu", type: "reserve", name: "EU-opslag (Rehden/Bergermeer)", country: "Duitsland/NL",
      lat: 52.75, lon: 8.60, stock: 100, tier: 2,
      note: "De WINTER-VULGRAAD is de geopolitieke metric na 2022: de EU verplicht 90% vulling per 1 november. Grote ondergrondse bergingen (Rehden = de grootste van Duitsland)." },
    { id: "gas-store-ua", type: "reserve", name: "Oekraine-opslag (West-Oekraine)", country: "Oekraine",
      lat: 48.70, lon: 24.00, stock: 30, tier: 3,
      note: "De grootste ondergrondse opslag van Europa (Bilche-Volytsko-Uherske e.a.) — strategisch als extra EU-buffer, maar risicovol in oorlogstijd." },
    { id: "gas-store-us", type: "reserve", name: "VS (Golfkust-zoutkoepels + Henry Hub)", country: "VS",
      lat: 30.20, lon: -92.10, stock: 130, tier: 2,
      note: "Grootste + meest liquide opslag; de Henry Hub-hub (Louisiana) zet de Amerikaanse benchmarkprijs. Zomer-injectie, winter-onttrekking." },
    { id: "gas-store-cn", type: "reserve", name: "China strategische opslag", country: "China",
      lat: 38.50, lon: 117.00, stock: 30, tier: 3,
      note: "In opbouw (ondergrondse berging + LNG-tanks) als buffer tegen LNG-prijspieken en winterse vraagpieken." },
  ],

  flows: [
    // === A. VELD -> LIQUEFACTIE-TERMINAL (stage erts, korte pijp-hop) ========
    { from: "gas-us", to: "gas-lng-sabinepass", value: 40, mode: "pipeline", stage: "erts",
      note: "Schaliegas -> de Golfkust-liquefactie (Louisiana). Het binnenlandse pijp-net dat het Appalachia/Permian-gas naar de exportkust brengt." },
    { from: "gas-us", to: "gas-lng-corpus", value: 35, mode: "pipeline", stage: "erts",
      note: "Permian-gas -> de Texas-liquefactie (Corpus Christi + Golfkust-cluster)." },
    { from: "gas-qatar", to: "gas-lng-raslaffan", value: 110, mode: "pipeline", stage: "erts",
      note: "North Field-gas komt aan land en gaat naar Ras Laffan — de aanloop naar 's werelds grootste LNG-complex." },
    { from: "gas-australia-nw", to: "gas-lng-karratha", value: 40, mode: "pipeline", stage: "erts",
      note: "NW Shelf-gas -> Karratha." },
    { from: "gas-australia-nw", to: "gas-lng-darwin", value: 15, mode: "pipeline", stage: "erts",
      note: "Ichthys-gas (offshore WA) 890 km subsea/over land naar Darwin." },
    { from: "gas-australia-qld", to: "gas-lng-gladstone", value: 30, mode: "pipeline", stage: "erts",
      note: "Queensland-steenkoolgas -> Curtis Island (Gladstone)." },
    { from: "gas-russia", to: "gas-lng-sabetta", value: 25, mode: "pipeline", stage: "erts",
      note: "Jamal-veldgas -> de Arctische liquefactie in Sabetta." },
    { from: "gas-russia-east", to: "gas-lng-sakhalin", value: 15, mode: "pipeline", stage: "erts",
      note: "Sachalin-schelfgas -> Prigorodnoje (Sachalin-2)." },
    { from: "gas-algeria", to: "gas-lng-arzew", value: 20, mode: "pipeline", stage: "erts",
      note: "Hassi R'Mel-gas dwars door de Sahara naar de Arzew-liquefactie aan de kust." },
    { from: "gas-nigeria", to: "gas-lng-bonny", value: 30, mode: "pipeline", stage: "erts",
      note: "Nigerdelta-gas -> Bonny Island." },
    { from: "gas-malaysia", to: "gas-lng-bintulu", value: 30, mode: "pipeline", stage: "erts",
      note: "Sarawak-gas -> het Bintulu-complex." },

    // === B. LNG-TANKERSTROMEN: liquefactie -> regas/eilandmarkt (raffinaat) ==
    // De heldere oceaan-arcs — het verhaal. Elke leg landt op een port of coastal.
    // --- VS-Golfkust -> Europa (oost) ---------------------------------------
    { from: "gas-lng-sabinepass", to: "gas-regas-nl", value: 15, mode: "ship", stage: "raffinaat",
      via: ["wp-florida"],
      note: "VS-Golfkust -> NW-Europa: de Golf van Mexico uit langs Florida, de Atlantische Oceaan over naar Eemshaven. De post-2022-pijl." },
    { from: "gas-lng-sabinepass", to: "gas-regas-de", value: 12, mode: "ship", stage: "raffinaat",
      via: ["wp-florida"],
      note: "VS -> de nieuwe Duitse FSRU (Wilhelmshaven) — het symbool van de Europa-pivot." },
    { from: "gas-lng-sabinepass", to: "gas-regas-uk", value: 8, mode: "ship", stage: "raffinaat",
      via: ["wp-florida"],
      note: "VS-Golfkust -> Isle of Grain (VK), de Theemsmonding in." },
    { from: "gas-lng-sabinepass", to: "gas-mkt-latam", value: 5, mode: "ship", stage: "raffinaat",
      via: ["wp-caribisch"],
      note: "VS-Golfkust -> Brazilie (Santos): spot-cargo's die bijspringen als de Braziliaanse waterkracht wegvalt." },
    // --- VS-Golfkust -> Azie (west, via Panama — het live knelpunt) ----------
    { from: "gas-lng-corpus", to: "gas-mkt-japan", value: 12, mode: "ship", stage: "raffinaat",
      via: ["wp-panama", "wp-pac-noord"],
      note: "VS-Golfkust -> Japan via het PANAMAKANAAL: cargo's vechten om de slots; de droogte van 2023-24 dwong omleiding via Suez of de Kaap." },
    { from: "gas-lng-corpus", to: "gas-mkt-korea", value: 8, mode: "ship", stage: "raffinaat",
      via: ["wp-panama", "wp-pac-noord"],
      note: "VS-Golfkust -> Korea via Panama en de noordelijke Stille Oceaan (bij Panama-congestie om de Kaap)." },
    // --- Qatar -> Azie + Europa (alles via Hormuz) ---------------------------
    { from: "gas-lng-raslaffan", to: "gas-mkt-japan", value: 20, mode: "ship", stage: "raffinaat",
      via: ["wp-hormuz", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Qatar -> Japan: door Hormuz de Arabische Zee over, dan Malakka en de Zuid-Chinese Zee — twee straten achter elkaar." },
    { from: "gas-lng-raslaffan", to: "gas-mkt-korea", value: 15, mode: "ship", stage: "raffinaat",
      via: ["wp-hormuz", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Qatar -> Korea, langs dezelfde Hormuz-Malakka-route." },
    { from: "gas-lng-raslaffan", to: "gas-regas-cn", value: 20, mode: "ship", stage: "raffinaat",
      via: ["wp-hormuz", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Qatar -> China (Rudong): langlopende contracten met de Chinese importeurs." },
    { from: "gas-lng-raslaffan", to: "gas-regas-in", value: 18, mode: "ship", stage: "raffinaat",
      via: ["wp-hormuz"],
      note: "Qatar -> India (Dahej): kort door Hormuz en over de Arabische Zee — India's dichtstbijzijnde grote leverancier." },
    { from: "gas-lng-raslaffan", to: "gas-regas-nl", value: 12, mode: "ship", stage: "raffinaat",
      via: ["wp-hormuz", "wp-bab", "wp-rode-zee", "wp-suez", "wp-gibraltar"],
      note: "Qatar -> Europa via Bab-el-Mandeb, de Rode Zee en Suez — sterk gegroeid na 2022." },
    // --- Australie -> NO-Azie ------------------------------------------------
    { from: "gas-lng-karratha", to: "gas-mkt-japan", value: 18, mode: "ship", stage: "raffinaat",
      via: ["wp-lombok", "wp-makassar", "wp-scs", "wp-taiwan"],
      note: "West-Australie -> Japan via Lombok/Makassar en de Zuid-Chinese Zee." },
    { from: "gas-lng-karratha", to: "gas-regas-cn", value: 12, mode: "ship", stage: "raffinaat",
      via: ["wp-lombok", "wp-makassar", "wp-scs", "wp-taiwan"],
      note: "West-Australie -> China (Rudong)." },
    { from: "gas-lng-darwin", to: "gas-mkt-japan", value: 12, mode: "ship", stage: "raffinaat",
      via: ["wp-makassar", "wp-scs", "wp-taiwan"],
      note: "Darwin -> Japan: de kortste Australie->NO-Azie-route." },
    { from: "gas-lng-gladstone", to: "gas-mkt-japan", value: 10, mode: "ship", stage: "raffinaat",
      via: ["wp-pac-west"],
      note: "Gladstone (oostkust) -> Japan via de Coral Zee en de westelijke Stille Oceaan." },
    // --- Maleisie / Rusland-Pacific -> NO-Azie -------------------------------
    { from: "gas-lng-bintulu", to: "gas-mkt-japan", value: 15, mode: "ship", stage: "raffinaat",
      via: ["wp-scs", "wp-taiwan"],
      note: "Maleisie (Bintulu) -> Japan via de Zuid-Chinese Zee en de Straat van Taiwan." },
    { from: "gas-lng-bintulu", to: "gas-regas-cn", value: 10, mode: "ship", stage: "raffinaat",
      via: ["wp-scs"],
      note: "Maleisie -> China (Rudong)." },
    { from: "gas-lng-sakhalin", to: "gas-mkt-japan", value: 12, mode: "ship", stage: "raffinaat",
      note: "Sachalin-2 -> Japan: kort langs de Japanse kust. Japan bleef afnemen ondanks de sancties." },
    // --- Rusland-Arctisch -> Europa + China (empirisch te checken) -----------
    { from: "gas-lng-sabetta", to: "gas-regas-nl", value: 10, mode: "ship", stage: "raffinaat",
      note: "Yamal-LNG -> Europa: west over de Barentszzee en de Noorse Zee naar de Noordzee (jaarrond ijsvrij)." },
    { from: "gas-lng-sabetta", to: "gas-regas-cn", value: 6, mode: "ship", stage: "raffinaat",
      note: "Yamal-LNG -> China over de NOORDELIJKE ZEEROUTE langs de Siberische kust — alleen 's zomers ijsvrij; anders west + om de Kaap of via Suez." },
    // --- Nigeria -> Europa + Azie -------------------------------------------
    { from: "gas-lng-bonny", to: "gas-regas-nl", value: 12, mode: "ship", stage: "raffinaat",
      via: ["wp-gibraltar"],
      note: "Nigeria -> Europa: langs de West-Afrikaanse kust omhoog, door Gibraltar naar de Noordzee." },
    { from: "gas-lng-bonny", to: "gas-regas-in", value: 6, mode: "ship", stage: "raffinaat",
      via: ["wp-kaap"],
      note: "Nigeria -> India/Azie om de Kaap de Goede Hoop." },
    // --- Algerije -> Zuid-Europa --------------------------------------------
    { from: "gas-lng-arzew", to: "gas-regas-es", value: 12, mode: "ship", stage: "raffinaat",
      note: "Algerije -> Spanje: kort over de West-Middellandse Zee (naast de Medgaz-pijp)." },

    // === C. PIJPLEIDINGGAS: veld -> markt (stage erts) =======================
    // De lage, donkere captive land-arcs — de geopolitiek van de vaste leiding.
    { from: "gas-norway", to: "gas-mkt-eu", value: 30, mode: "pipeline", stage: "erts",
      note: "Noorwegen = Europa's #1 leverancier na Rusland. De dikke betrouwbare pijl (subsea naar VK/DE/BE, hier als landcorridor over Scandinavie getekend)." },
    { from: "gas-russia", to: "gas-mkt-eu", value: 8, mode: "pipeline", stage: "erts",
      note: "De GEKROMPEN restpijl: TurkStream + het laatste beetje transit — na 2022 een fractie van de ~150 bcm die Rusland ooit aan Europa leverde." },
    { from: "gas-russia", to: "gas-mkt-china", value: 22, mode: "pipeline", stage: "erts",
      note: "POWER OF SIBERIA: de oostwaartse pivot (bron Oost-Siberie). Rusland ruilt de verloren Europese captive-markt in voor de Chinese; POS-2 gepland maar traag." },
    { from: "gas-turkmenistan", to: "gas-mkt-china", value: 30, mode: "pipeline", stage: "erts",
      note: "De Centraal-Azie-China-pijp: landlocked Turkmenistan is volledig captive aan China — de enige grote klant." },
    { from: "gas-azerbaijan", to: "gas-mkt-eu", value: 10, mode: "pipeline", stage: "erts",
      note: "De Zuidelijke Gascorridor (TANAP/TAP): Azeri-gas via Turkije en de Balkan naar Europa — bewust om Rusland heen aangelegd." },
    { from: "gas-us", to: "gas-mkt-us", value: 60, mode: "pipeline", stage: "erts",
      note: "Het Amerikaanse binnenlandse pijp-net: veruit het grootste verbruik draait op eigen productie (Henry Hub, structureel goedkoop)." },

    // === D. LEVERING: regas-poort -> binnenlandse markt (stage product) ======
    { from: "gas-regas-nl", to: "gas-mkt-eu", value: 20, mode: "pipeline", stage: "product",
      note: "Rotterdam/Eemshaven -> het Duitse/NW-Europese net." },
    { from: "gas-regas-de", to: "gas-mkt-eu", value: 12, mode: "pipeline", stage: "product",
      note: "De Duitse FSRU's -> het binnenlandse net." },
    { from: "gas-regas-uk", to: "gas-mkt-eu", value: 6, mode: "pipeline", stage: "product",
      note: "VK -> continent via de Kanaaltunnel-corridor (interconnector, tweerichting)." },
    { from: "gas-regas-es", to: "gas-mkt-eu", value: 4, mode: "pipeline", stage: "product",
      note: "Spanje -> Frankrijk over de Pyreneeen: DUN — de beperkte pijpuitgang die van Iberie een 'eiland' maakt ondanks veel regascapaciteit." },
    { from: "gas-regas-cn", to: "gas-mkt-china", value: 40, mode: "pipeline", stage: "product",
      note: "Chinese kust-LNG -> het binnenland." },
    { from: "gas-regas-in", to: "gas-mkt-india", value: 18, mode: "pipeline", stage: "product",
      note: "Dahej -> het Indiase net (stroom + kunstmest)." },

    // === E. OPSLAG-VULLING onder de toggle (layer:"reserve", alleen aan) =====
    // De zomer-vulling van de winterbuffer, buiten de dagelijkse leverstroom om
    // (de olie-SPR-nuance). Default uit.
    { from: "gas-mkt-eu", to: "gas-store-eu", value: 12, mode: "pipeline", stage: "erts", layer: "reserve",
      note: "De EU vult in de zomer richting het 90%-mandaat per 1 november — de winterbuffer opbouwen." },
    { from: "gas-regas-nl", to: "gas-store-eu", value: 6, mode: "pipeline", stage: "erts", layer: "reserve",
      note: "LNG-instroom die deels rechtstreeks de bergingen in gaat." },
    { from: "gas-mkt-eu", to: "gas-store-ua", value: 4, mode: "pipeline", stage: "erts", layer: "reserve",
      note: "West-Oekraiense caverns als extra Europese buffer (strategisch, maar risicovol in oorlogstijd)." },
    { from: "gas-mkt-us", to: "gas-store-us", value: 15, mode: "pipeline", stage: "erts", layer: "reserve",
      note: "Henry Hub-zoutkoepels: zomer-injectie, winter-onttrekking — de meest liquide opslag ter wereld." },
    { from: "gas-mkt-china", to: "gas-store-cn", value: 6, mode: "pipeline", stage: "erts", layer: "reserve",
      note: "China bouwt strategische buffer op tegen LNG-prijspieken en winterse vraagpieken." },
  ],

  // ==========================================================================
  // SPANNINGEN — waar de gasketen 'knijpt'. De knijp is deels een zeestraat
  // (Hormuz/Panama) maar vooral STRUCTUREEL: de liquefactie-flessenhals en de
  // captive pijpleiding-relaties die met oorlog/sancties meebewegen.
  // ==========================================================================
  tensions: [
    { id: "gas-t-hormuz", type: "knelpunt", title: "Qatar's Hormuz-afhankelijkheid: geen enkele bypass",
      lat: 26.57, lon: 56.25,
      nodes: ["gas-lng-raslaffan", "gas-qatar"],
      flows: ["gas-lng-raslaffan>gas-mkt-japan", "gas-lng-raslaffan>gas-regas-nl", "gas-lng-raslaffan>gas-regas-cn"],
      metric: "Qatar ~20% van 's werelds LNG — alles door Hormuz, GEEN pijpleiding-bypass (anders dan olie)",
      note: "Qatar's hele LNG-export moet fysiek door de Straat van Hormuz. Waar olie de Hormuz-flessenhals kan omzeilen met de Yanbu- en Fujairah-bypass-pijpleidingen, heeft LNG die uitweg NIET: gas moet vloeibaar gemaakt bij Ras Laffan en kan alleen over zee weg. De scherpste enkelvoudige zeestraat-afhankelijkheid van de hele atlas." },

    { id: "gas-t-liquefaction", type: "structureel", title: "De liquefactie-flessenhals: de echte trechter",
      lat: 25.00, lon: -90.00,
      nodes: ["gas-lng-sabinepass", "gas-lng-corpus", "gas-lng-raslaffan", "gas-lng-karratha"],
      flows: ["gas-us>gas-lng-sabinepass", "gas-qatar>gas-lng-raslaffan", "gas-australia-nw>gas-lng-karratha"],
      metric: "een liquefactie-trein kost $10-20 mld -> capaciteit bij 3 polen (VS-Golfkust/Qatar/Australie)",
      note: "Gas' equivalent van de China-raffinage bij lithium: niet een zeestraat maar de kapitaalintensieve vloeibaarmaking bepaalt hoeveel gas globaal verhandelbaar is. Over land is gas captive aan een pijpleiding; pas na liquefactie is een molecuul een omleidbare wereldgrondstof. Die capaciteit zit geconcentreerd bij drie exportpolen — dat is de echte trechter." },

    { id: "gas-t-europe-pivot", type: "beleid", title: "De Europa-pivot van 2022",
      lat: 53.60, lon: 8.10,
      nodes: ["gas-regas-de", "gas-regas-nl", "gas-russia"],
      flows: ["gas-lng-sabinepass>gas-regas-de", "gas-russia>gas-mkt-eu"],
      metric: "~150 bcm Russische pijp vervangen door LNG + FSRU's in maanden; TTF-prijspiek najaar 2022",
      note: "Na de Nord Stream-sabotage (sep 2022) en het wegvallen van de Oekraine-transit verving Europa in recordtempo ~150 bcm Russische pijpgas door LNG uit de VS en Qatar. Duitsland, dat 0 LNG-terminals had, bouwde drijvende FSRU's (Wilhelmshaven/Brunsbuttel) in maanden. Zichtbaar op de kaart: de Russische pijl naar Europa krimpt tot een draadje terwijl een waaier LNG-arcs op de nieuwe Duitse/Nederlandse terminals landt." },

    { id: "gas-t-russia-east", type: "beleid", title: "Rusland's pivot naar het oosten",
      lat: 55.00, lon: 108.00,
      nodes: ["gas-russia", "gas-mkt-china", "gas-lng-sabetta"],
      flows: ["gas-russia>gas-mkt-china", "gas-russia>gas-mkt-eu"],
      metric: "Power of Siberia (+POS-2 gepland) + Arctisch LNG — de Europese markt ingeruild voor China",
      note: "Rusland verloor z'n grootste captive-markt (Europa) en probeert die te vervangen door China: Power of Siberia levert al, POS-2 is gepland maar onderhandelt traag (China dicteert de prijs). Daarnaast Arctisch LNG (Yamal/Sabetta) dat west EN oost kan. De les van gas: een pijpleiding is jaren te bouwen — je kunt een captive-markt niet zomaar omleggen zoals een tanker." },

    { id: "gas-t-price-zones", type: "structureel", title: "Drie prijszones: de arbitrage stuurt de cargo's",
      lat: 40.00, lon: -40.00,
      nodes: ["gas-lng-sabinepass", "gas-regas-nl", "gas-mkt-japan"],
      flows: ["gas-lng-sabinepass>gas-regas-de", "gas-lng-corpus>gas-mkt-japan"],
      metric: "Henry Hub (VS, goedkoop) « TTF (Europa) « JKM (Azie) — LNG-arbitrage koppelt, transport scheidt",
      note: "Omdat gas duur te verschepen is, bestaan drie los-gekoppelde prijszones: het goedkope Amerikaanse Henry Hub, het Europese TTF en het Aziatische JKM. De flexibele VS-cargo's varen naar de hoogste prijs — dat is hoe Amerikaans gas in 2022 massaal naar Europa i.p.v. Azie ging. LNG-arbitrage brengt de zones dichter bij elkaar, maar transportkosten en terminalcapaciteit houden ze gescheiden." },

    { id: "gas-t-panama", type: "knelpunt", title: "Het Panama-LNG-knelpunt (live)",
      lat: 9.00, lon: -79.50,
      nodes: ["gas-lng-corpus", "gas-lng-sabinepass"],
      flows: ["gas-lng-corpus>gas-mkt-japan", "gas-lng-corpus>gas-mkt-korea"],
      metric: "droogte 2023-24 -> minder kanaal-slots -> VS-Golfkust->Azie omgeleid via Suez of de Kaap",
      note: "Een gas-eigen accent bovenop het olie-net: VS-Golfkust->Azie-cargo's zijn afhankelijk van het Panamakanaal, en LNG-tankers hebben geen prioriteit bij de slots. De droogte van 2023-24 verlaagde de waterstand en dwong veel cargo's om te varen via Suez of om de Kaap — duurder en langer. Een levend knelpunt dat laat zien hoe kwetsbaar zelfs de 'flexibele' Amerikaanse export is." },
  ],
});
