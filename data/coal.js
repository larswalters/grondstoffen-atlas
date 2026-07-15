// ============================================================================
// KOLEN (C) — volledig uitgewerkte module. Peiljaar ±2023.
// Cijfers indicatief/afgerond, o.b.v. IEA (Coal 2023), Energy Institute
// (Statistical Review of World Energy 2024), USGS en bedrijfs-/havenrapportages
// (Coal India, Adaro, BHP-Mitsubishi/BMA, Teck, Glencore, Newcastle, RBCT).
// Eenheid overal: Mt/jaar (miljoen ton), zodat de hele keten optelbaar blijft.
// Wereldproductie ≈ 8.700 Mt; wereld-zeehandel ≈ 1.350 Mt (~15%). Zie design/kolen.md.
//
// DE VORM VAN KOLEN (fundamenteel anders dan de andere grondstoffen):
//   - GEEN MONDIALE FLESSENHALS, want kolen is overweldigend BINNENLANDS. De
//     reuzen (China ~50% van de wereld, India, VS, Rusland) delven ÉN verbranden
//     hun eigen kolen; slechts ~15% gaat over zee. De kaart toont daarom grote
//     BINNENLANDSE BLOKKEN (mijn -> centrale, korte land/kust-hops) tegenover een
//     dunnere, geopolitiek beladen ZEEHANDELSLAAG.
//   - CHINA = SWING-KOPER: 's werelds grootste producent MAAR OOK grootste
//     importeur. Z'n marginale importvraag zet de zeeprijs; z'n beleid legt hele
//     stromen om. India = #2-importeur + veruit grootste COKESKOOL-importeur.
//   - TWEE KOLEN: thermisch (steenkool -> elektriciteitscentrales) vs.
//     metallurgisch/COKESKOOL (-> cokesovens -> hoogoven-staal). Premium harde
//     cokeskool zit geconcentreerd in het Australische Bowen Basin. Gedragen via
//     `note` + een aparte `tension` (nikkel-patroon), niet via `stage`.
//
// STAGES (via `stage`) — hier de ketenpositie gedolven -> verhandeld -> verbrand:
//   erts       = gedolven kolen op weg naar haven/centrale (mijn->haven gathering
//                én de grote binnenlandse mijn->centrale-hops) — dof/donker antraciet.
//   raffinaat  = INTERNATIONAAL VERHANDELDE BULK (de zeekruisingen + de Mongolië-
//                landcorridor) — volle kolenkleur. Hier leeft elk ban/her-
//                routeringsverhaal. Binnenlandse kolen kruist deze laag NIET ->
//                verhandelde kolen leest visueel anders (de ~85/15-splitsing).
//   product    = eindgebruik: importterminal/hub -> centrale (stroom) — licht.
//
// TRANSPORT is schip (bulkcarriers) + land (spoor). GEEN nieuwe render-modus,
// GEEN nieuwe marker-types (alleen mine/port/market). Één nieuw chokepoint:
// grens-gashuunsukhait (Mongolië-China-Gobi-grens) in data/_chokepoints.js -
// het grondstof-eigen "nieuwe element", exact het grens-kasumbalesa/grens-ruili-
// patroon. GEEN optionele toggle-laag (kolen heeft geen zinvol CB/beurs/recycling-
// equivalent). Inland-origins bij een ship-flow: 1e via = een haven (gathering-leg
// routeert auto als land, olie/koper-patroon).
// ============================================================================

REGISTER({
  id: "coal",
  name: "Kolen",
  symbol: "C",
  color: "#6B5D4F",       // warm antraciet-bruingrijs: de mijn-markers (wármer dan grafiet's koele grijs)
  flowColor: "#C2A878",   // warm taupe/as: de stromen zichtbaar tegen de donkere bol
  detail: "uitgewerkt",
  unit: "Mt/jaar (indicatief)",
  blurb: "Kolen is de grondstof die de energietransitie zou moeten doden, maar op " +
    "recordhoogte staat — gedreven door China en India. De vorm is anders dan de andere " +
    "grondstoffen: geen mondiale trechter, want ~85% wordt verbrand waar het gedolven wordt " +
    "(China #1, India, VS). Slechts ~15% van de ~8.700 Mt gaat over zee, en op die dunnere " +
    "laag is China zowel grootste producent als grootste importeur — de swing-koper. Twee " +
    "kolen naast elkaar: thermisch (steenkool -> stroom) en cokeskool (-> staal).",

  nodes: [
    // =============================================================== MIJNEN
    // Eerst de BINNENLANDSE REUZEN (delven + verstoken thuis), dan de EXPORTEURS
    // die de zeehandelslaag voeden. `share` = % van ~8.700 Mt wereldproductie.
    // `note` benoemt telkens thermisch/cokeskool + binnenlands/export.

    // --- China (~50% van de wereld): de "Drie West", grotendeels binnenlands ---
    { id: "coal-shanxi", type: "mine", name: "Shanxi (kolenbasis)", country: "China",
      lat: 37.87, lon: 112.55, share: 16.0, tier: 1, operator: "div. (staat + privaat)",
      status: "actief", capacity: "≈ 1.400 Mt/j",
      note: "Thermisch + cokeskool; het hart van China's 'Drie West' (Shanxi/Shaanxi/Binnen-Mongolië ≈ 70% van de Chinese output). Binnenlands: per spoor naar Qinhuangdao, dan kustvaart zuid naar de Guangdong-centrales ('noord-kool zuid-transport')." },
    { id: "coal-innermongolia", type: "mine", name: "Binnen-Mongolië (Ordos)", country: "China",
      lat: 39.60, lon: 109.80, share: 15.0, tier: 1, operator: "div. (Shenhua e.a.)",
      status: "actief", capacity: "≈ 1.300 Mt/j",
      note: "Thermisch; grootste provincie-output ter wereld. Ook het ontvangstpunt van de Mongoolse cokeskool-import over de Gobi-grens (Ganqimaodu)." },

    // --- India (#2): thermisch + cokeskool, tóch importeur -------------------
    { id: "coal-india", type: "mine", name: "Jharkhand / Odisha (Coal India)", country: "India",
      lat: 23.70, lon: 85.30, share: 11.0, tier: 1, operator: "Coal India Ltd",
      status: "actief", capacity: "≈ 950 Mt/j",
      note: "Thermisch (Odisha) + cokeskool (Jharkhand/Dhanbad); India is #2-producent. Verstookt vrijwel alles binnenlands, maar importeert tóch premium thermisch én cokeskool omdat de eigen kool asrijk/ongeschikt is." },

    // --- VS: Powder River (thermisch, binnenlands) + Appalachen (cokeskool, export)
    { id: "coal-us-powder", type: "mine", name: "Powder River Basin", country: "VS (Wyoming)",
      lat: 44.50, lon: -105.50, share: 4.0, tier: 1, operator: "Peabody / Arch",
      status: "actief", capacity: "≈ 330 Mt/j",
      note: "Thermisch, laag-zwavel; bijna volledig binnenlands. De Amerikaanse kolenvraag daalt structureel (gas + hernieuwbaar) — het krimpende blok van de kaart." },
    { id: "coal-us-appalachia", type: "mine", name: "Appalachen (West Virginia)", country: "VS",
      lat: 38.00, lon: -81.50, share: 2.0, tier: 2, operator: "div.",
      status: "actief", capacity: "≈ 170 Mt/j",
      note: "Cokeskool + thermisch; het export-deel gaat per spoor naar Hampton Roads (Norfolk) en de Atlantische Oceaan over naar Europees en Indiaas staal — de swing-leverancier die bijspringt als Rusland/Australië wegvalt." },

    // --- Rusland: Kuzbass — landlocked Siberië, de post-2022 oost-draai -------
    { id: "coal-russia-kuzbass", type: "mine", name: "Kuzbass (Kemerovo)", country: "Rusland",
      lat: 54.00, lon: 86.50, share: 5.0, tier: 1, operator: "SUEK / div.",
      status: "actief", capacity: "≈ 440 Mt/j",
      note: "Thermisch + cokeskool; diep in Siberië -> 4.000+ km spoor naar de Pacific-havens. Na de EU-embargo (aug 2022) draaide de afzet van de Baltische havens naar de Pacific (Vostochny) en per overbelast spoor (Trans-Siberië/BAM) richting China/India." },

    // --- Indonesië: #1 thermisch-exporteur, dichtbij de Aziatische vraag -----
    { id: "coal-indonesia", type: "mine", name: "Oost-Kalimantan", country: "Indonesië",
      lat: -0.50, lon: 117.00, share: 9.0, tier: 1, operator: "Bumi / Adaro / Kideco",
      status: "actief", capacity: "≈ 775 Mt/j",
      note: "#1 THERMISCH-EXPORTEUR ter wereld; goedkoop, laag-calorisch, pal naast China/India. Kolen per rivierpont naar transhipment-ankerplaatsen (Bontang), dan bulkschip -> de kortste zeehandelsroute van allemaal." },

    // --- Australië: Bowen (cokeskool #1) + Hunter (thermisch) ----------------
    { id: "coal-australia-qld", type: "mine", name: "Bowen Basin (Queensland)", country: "Australië",
      lat: -22.30, lon: 148.00, share: 2.8, tier: 1, operator: "BHP-Mitsubishi (BMA) / Anglo / Glencore",
      status: "actief", capacity: "≈ 245 Mt/j",
      note: "#1 METALLURGISCHE (COKESKOOL)-EXPORTEUR; premium harde cokeskool voor hoogoven-staal. Per spoor naar Hay Point/Dalrymple Bay. Kernslachtoffer én -winnaar van de China-ban: afzet verschoof naar India/Japan/Korea." },
    { id: "coal-australia-nsw", type: "mine", name: "Hunter Valley (NSW)", country: "Australië",
      lat: -32.50, lon: 151.00, share: 2.2, tier: 1, operator: "Glencore / Yancoal",
      status: "actief", capacity: "≈ 190 Mt/j",
      note: "Thermisch (hoog-calorisch); per spoor naar Newcastle — 's werelds grootste kolen-exporthaven. Vaste leverancier van Japan/Korea/Taiwan." },

    // --- Zuid-Afrika: Mpumalanga -> Richards Bay (afzet post-2022 naar India)
    { id: "coal-southafrica", type: "mine", name: "Mpumalanga (Highveld)", country: "Zuid-Afrika",
      lat: -26.00, lon: 29.20, share: 3.0, tier: 1, operator: "Glencore / Thungela / Exxaro",
      status: "actief", capacity: "≈ 230 Mt/j",
      note: "Thermisch; binnenlands (Eskom) + export via Richards Bay. De afzet verschoof sinds 2022 van Europa naar India/Azië (Europa kocht kortstondig terug tijdens de gascrisis)." },

    // --- Colombia: Cerrejón -> Atlantisch (Europa/Azië) ----------------------
    { id: "coal-colombia", type: "mine", name: "Cerrejón (La Guajira)", country: "Colombia",
      lat: 11.10, lon: -72.60, share: 0.7, tier: 2, operator: "Glencore",
      status: "actief", capacity: "≈ 55 Mt/j",
      note: "Thermisch; Atlantische export -> Europa (piekte in 2022 door de gascrisis) en Azië via Panama." },

    // --- Mongolië: Tavan Tolgoi — COKESKOOL zonder kust, over de Gobi --------
    { id: "coal-mongolia", type: "mine", name: "Tavan Tolgoi (Zuid-Gobi)", country: "Mongolië",
      lat: 43.60, lon: 105.50, share: 0.7, tier: 1, operator: "Erdenes Tavan Tolgoi",
      status: "actief", capacity: "≈ 60 Mt/j",
      note: "COKESKOOL, landlocked -> per truck/spoor over de Gobi-grens (grens-gashuunsukhait) naar de Chinese staalindustrie. Backfilde de Australische cokeskool tijdens de China-ban." },

    // --- Canada: Elk Valley -> Vancouver (cokeskool naar Aziatisch staal) ----
    { id: "coal-canada", type: "mine", name: "Elk Valley (BC)", country: "Canada",
      lat: 49.90, lon: -114.90, share: 0.6, tier: 2, operator: "Teck",
      status: "actief", capacity: "≈ 25 Mt/j",
      note: "Metallurgische cokeskool; per spoor naar Westshore/Vancouver, dan de Stille Oceaan over naar de Japanse/Koreaanse hoogovens." },

    // --- Mozambique: Moatize — nieuwe mijn, lange landcorridor ---------------
    { id: "coal-mozambique", type: "mine", name: "Moatize (Tete)", country: "Mozambique",
      lat: -16.10, lon: 33.70, share: 0.2, tier: 3, operator: "Vulcan (ex-Vale)",
      status: "actief", capacity: "≈ 12 Mt/j",
      note: "Cokeskool + thermisch; per spoor (de Nacala-corridor, ~900 km) naar de kust -> India/Azië. De koper/Copperbelt-parallel: waarde ligt niet bij de mijn maar aan het eind van een lange landweg." },

    // ================================================================ HAVENS
    // Exportterminals + de binnenlandse Chinese transhipment-hub Qinhuangdao.
    { id: "coal-port-newcastle", type: "port", name: "Newcastle", country: "Australië",
      lat: -32.92, lon: 151.78, tier: 2,
      note: "'s Werelds grootste kolen-exporthaven; de Hunter-thermisch de Grote Oceaan op richting Japan/Korea/Taiwan/China." },
    { id: "coal-port-haypoint", type: "port", name: "Hay Point / Dalrymple Bay", country: "Australië",
      lat: -21.28, lon: 149.30, tier: 2,
      note: "De cokeskool-exportterminals van het Bowen Basin; premium harde cokeskool naar het Aziatische en Indiase staal." },
    { id: "coal-port-kalimantan", type: "port", name: "Bontang-ankerplaats", country: "Indonesië",
      lat: -0.10, lon: 117.55, tier: 2,
      note: "Transhipment-ankerplaats voor de Oost-Kalimantan-thermisch: van rivierpont naar bulkcarrier, richting China/India/Vietnam." },
    { id: "coal-port-richards-bay", type: "port", name: "Richards Bay (RBCT)", country: "Zuid-Afrika",
      lat: -28.80, lon: 32.08, tier: 2,
      note: "Grootste kolenterminal van Afrika; sinds 2022 vooral richting India/Azië i.p.v. Europa." },
    { id: "coal-port-vostochny", type: "port", name: "Vostochny / Nachodka", country: "Rusland",
      lat: 42.75, lon: 133.08, tier: 2, coastal: true,
      note: "De Pacific-poort van de Russische kolen-oost-draai; ontvangt het Kuzbass-kool per Trans-Siberisch spoor en verscheept het naar China/Japan/Korea/India." },
    { id: "coal-port-cerrejon", type: "port", name: "Puerto Bolívar", country: "Colombia",
      lat: 12.23, lon: -71.98, tier: 3,
      note: "De exporthaven van Cerrejón; Colombiaanse thermisch de Caribische Zee op richting Europa en (via Panama) Azië." },
    { id: "coal-port-hampton", type: "port", name: "Hampton Roads (Norfolk)", country: "VS",
      lat: 36.90, lon: -76.30, tier: 3,
      note: "De Atlantische kolen-exporthaven van de VS; Appalachische cokeskool/thermisch naar Europa en India." },
    { id: "coal-port-ridley", type: "port", name: "Ridley Terminal (Prince Rupert)", country: "Canada",
      lat: 54.23, lon: -130.32, tier: 3,
      note: "De open-kust kolenexportterminal van Brits-Columbia (Prince Rupert) — de kortste route van Noord-Amerika naar Azië. Canadese cokeskool de noordelijke Stille Oceaan over naar het Japanse/Koreaanse staal. (Westshore/Roberts Bank ligt ingesloten in de Salish Sea en valt in het grove raster dicht.)" },
    { id: "coal-port-nacala", type: "port", name: "Nacala", country: "Mozambique",
      lat: -14.54, lon: 40.68, tier: 3,
      note: "Het eindpunt van de Nacala-spoorcorridor uit Moatize; kolen de Indische Oceaan op naar India/Azië." },
    { id: "coal-port-qinhuangdao", type: "port", name: "Qinhuangdao", country: "China",
      lat: 39.90, lon: 119.60, tier: 2, coastal: true,
      note: "De binnenlandse transhipment- en benchmarkhaven: Shanxi-kolen komt hier per spoor aan en gaat per kustvaart naar de Zuid-Chinese centrales. Het hart van 'noord-kool zuid-transport'." },

    // ================================================================ MARKT
    // Centrales (thermisch) + staalfabrieken (cokeskool). Ship-endpoints coastal.
    { id: "coal-mkt-china-power", type: "market", name: "China — kustcentrales (Guangdong)", country: "China",
      lat: 23.10, lon: 113.30, tier: 1, coastal: true,
      note: "De grootste importvraag ter wereld: de zuidelijke kustprovincies verstoken binnenlandse kolen (per kustvaart uit Qinhuangdao) én geïmporteerde thermisch uit Indonesië/Australië/Rusland. China = swing-koper." },
    { id: "coal-mkt-china-steel", type: "market", name: "China — staal (Hebei/Tangshan)", country: "China",
      lat: 39.63, lon: 118.18, tier: 1, coastal: true,
      note: "'s Werelds grootste staalindustrie -> grootste cokeskool-sink: binnenlandse cokeskool (Shanxi) + Mongolië (over de Gobi) + Australië/Rusland/Canada over zee." },
    { id: "coal-mkt-india-power", type: "market", name: "India — kustcentrales (Mundra/Gujarat)", country: "India",
      lat: 22.75, lon: 69.70, tier: 1, coastal: true,
      note: "Geïmporteerd hoog-calorisch thermisch voor de west-kustcentrales (Adani/Tata) — bovenop de enorme binnenlandse Coal-India-productie." },
    { id: "coal-mkt-india-steel", type: "market", name: "India — staal (Odisha/Paradip)", country: "India",
      lat: 20.26, lon: 86.67, tier: 1, coastal: true,
      note: "#1 COKESKOOL-IMPORTEUR ter wereld: de oostkust-staalindustrie (SAIL/Tata/JSW) leunt op Australische/Amerikaanse/Mozambikaanse cokeskool omdat de eigen kool ongeschikt is voor cokes." },
    { id: "coal-mkt-japan", type: "market", name: "Japan — stroom + staal (Chubu)", country: "Japan",
      lat: 34.90, lon: 137.00, tier: 1, coastal: true,
      note: "Grote thermisch- + cokeskool-importeur; vaste, premium Australische leverancierrelatie. Nam extra Australische kolen op tijdens de China-ban." },
    { id: "coal-mkt-korea", type: "market", name: "Zuid-Korea — stroom + staal (POSCO)", country: "Zuid-Korea",
      lat: 35.99, lon: 129.38, tier: 1, coastal: true,
      note: "Thermisch (centrales) + cokeskool (POSCO-staal, Pohang). Ving Australische kolen op die China tijdens de ban weerde." },
    { id: "coal-mkt-taiwan", type: "market", name: "Taiwan — stroom (Taichung)", country: "Taiwan",
      lat: 24.00, lon: 120.50, tier: 2, coastal: true,
      note: "Thermisch-importeur; Taichung is een van 's werelds grootste kolencentrales. Leunt op Australisch en Indonesisch kool." },
    { id: "coal-mkt-vietnam", type: "market", name: "Vietnam — stroom (Haiphong)", country: "Vietnam",
      lat: 20.85, lon: 106.75, tier: 2, coastal: true,
      note: "De snelst groeiende Zuidoost-Aziatische kolenimporteur; nieuwe centrales trekken Indonesisch thermisch aan." },
    { id: "coal-mkt-eu", type: "market", name: "EU — Rotterdam/ARA -> Ruhr", country: "Nederland",
      lat: 51.95, lon: 4.10, tier: 2, coastal: true,
      note: "De ARA-hub (Amsterdam-Rotterdam-Antwerpen) voedt de Duitse centrales en het Ruhr-staal. Structureel dalend, met een kortstondige heropleving in 2022 (gascrisis) op Colombiaanse/Amerikaanse/Zuid-Afrikaanse kolen." },
    { id: "coal-mkt-us", type: "market", name: "VS — binnenlandse centrales (Midwest)", country: "VS",
      lat: 39.80, lon: -89.60, tier: 2,
      note: "De Amerikaanse binnenlandse burn: Powder-River- en Appalachen-thermisch per spoor naar de centrales. Een structureel krimpend, volledig binnenlands blok." },
  ],

  // ==========================================================================
  // STROMEN — value in Mt/jaar. stage bepaalt de kleur (erts dof, raffinaat vol
  // kolenkleur, product licht). `via` = echte route langs havens (coal-port-*) en
  // de universele knelpunten/vaarpunten (wp-* uit data/_chokepoints.js) + de
  // nieuwe Mongolië-landcorridor (grens-gashuunsukhait).
  //
  //  A) Binnenlandse kolen (de ~85%): mijn -> centrale/staal (erts + product)
  //  B) Zeehandel THERMISCH: exporteur -> centrale (raffinaat)
  //  C) Zeehandel COKESKOOL: exporteur -> staalfabriek (raffinaat)
  //  D) Mongolië-landcorridor: cokeskool over de Gobi-grens (raffinaat)
  // ==========================================================================
  flows: [
    // === A. BINNENLANDSE KOLEN — de ~85%, geen zeekruising ===================
    { from: "coal-shanxi", to: "coal-port-qinhuangdao", value: 1000, mode: "rail", stage: "erts",
      note: "Shanxi-kolen per spoor naar de transhipment-benchmarkhaven Qinhuangdao — de eerste leg van 'noord-kool zuid-transport'." },
    { from: "coal-port-qinhuangdao", to: "coal-mkt-china-power", value: 1000, mode: "ship", stage: "product",
      via: ["wp-taiwan"],
      note: "Kustvaart zuid langs de Chinese kust naar de Guangdong-centrales — de grootste binnenlandse kolenstroom ter wereld, geheel over eigen kustwater." },
    { from: "coal-innermongolia", to: "coal-mkt-china-steel", value: 900, mode: "rail", stage: "erts",
      note: "Ordos-kolen over land naar de Hebei/Tangshan-staal- en stroomcluster. Binnenlands, gesloten." },
    { from: "coal-india", to: "coal-mkt-india-steel", value: 700, mode: "rail", stage: "erts",
      note: "Coal India -> de binnenlandse staal-/stroomindustrie (Odisha/Jharkhand), grotendeels binnenlands over land." },
    { from: "coal-us-powder", to: "coal-mkt-us", value: 300, mode: "rail", stage: "erts",
      note: "Powder River Basin -> de Amerikaanse Midwest-centrales, per spoor. Volledig binnenlands." },
    { from: "coal-us-appalachia", to: "coal-mkt-us", value: 100, mode: "rail", stage: "erts",
      note: "Appalachische thermisch -> binnenlandse centrales; het niet-geëxporteerde deel." },
    { from: "coal-russia-kuzbass", to: "coal-port-vostochny", value: 300, mode: "rail", stage: "erts",
      note: "Kuzbass -> 4.000+ km Trans-Siberisch spoor naar de Pacific-haven Vostochny. Het overbelaste spoor ís het knelpunt van de Russische oost-draai." },

    // === B. ZEEHANDEL THERMISCH — exporteur -> centrale (raffinaat) ==========
    { from: "coal-indonesia", to: "coal-mkt-china-power", value: 200, mode: "ship", stage: "raffinaat",
      via: ["coal-port-kalimantan", "wp-makassar", "wp-scs", "wp-taiwan"],
      note: "Indonesische thermisch -> Zuid-China: de kortste en grootste zeehandelsroute ter wereld (gathering per rivierpont, dan bulkcarrier)." },
    { from: "coal-indonesia", to: "coal-mkt-india-power", value: 130, mode: "ship", stage: "raffinaat",
      via: ["coal-port-kalimantan", "wp-singapore", "wp-malakka", "wp-aceh"],
      note: "Indonesische thermisch -> de Indiase westkust via Malakka en rond Zuid-India." },
    { from: "coal-indonesia", to: "coal-mkt-vietnam", value: 45, mode: "ship", stage: "raffinaat",
      via: ["coal-port-kalimantan", "wp-scs"],
      note: "-> de snelgroeiende Vietnamese centralevraag." },
    { from: "coal-indonesia", to: "coal-mkt-korea", value: 25, mode: "ship", stage: "raffinaat",
      via: ["coal-port-kalimantan", "wp-makassar", "wp-scs", "wp-taiwan"],
      note: "Indonesische thermisch -> Korea (aanvulling op het Australische kool)." },
    { from: "coal-australia-nsw", to: "coal-mkt-japan", value: 80, mode: "ship", stage: "raffinaat",
      via: ["coal-port-newcastle", "wp-pac-west"],
      note: "Hunter-thermisch -> Japan: de vaste, premium leverancierrelatie van de atlas." },
    { from: "coal-australia-nsw", to: "coal-mkt-korea", value: 45, mode: "ship", stage: "raffinaat",
      via: ["coal-port-newcastle", "wp-pac-west", "wp-taiwan"],
      note: "-> Korea; nam extra Australisch kool op toen China het weerde (de ban-omlegging)." },
    { from: "coal-australia-nsw", to: "coal-mkt-taiwan", value: 30, mode: "ship", stage: "raffinaat",
      via: ["coal-port-newcastle", "wp-pac-west", "wp-scs"],
      note: "-> Taiwan (Taichung)." },
    { from: "coal-australia-nsw", to: "coal-mkt-india-power", value: 25, mode: "ship", stage: "raffinaat",
      via: ["coal-port-newcastle", "wp-lombok", "wp-aceh"],
      note: "Australisch hoog-calorisch thermisch -> India, via de Lombok-diepwaterroute en rond Zuid-India." },
    { from: "coal-australia-nsw", to: "coal-mkt-china-power", value: 40, mode: "ship", stage: "raffinaat",
      via: ["coal-port-newcastle", "wp-pac-west", "wp-scs", "wp-taiwan"],
      note: "Australische thermisch -> China: grotendeels weggevallen tijdens de ban (okt 2020), hervat na begin 2023." },
    { from: "coal-southafrica", to: "coal-mkt-india-power", value: 60, mode: "ship", stage: "raffinaat",
      via: ["coal-port-richards-bay", "wp-moz-noord"],
      note: "Richards Bay -> India: de emblematische post-2022 verschuiving (van Europa naar India), rond de noordpunt van Madagaskar." },
    { from: "coal-southafrica", to: "coal-mkt-china-power", value: 20, mode: "ship", stage: "raffinaat",
      via: ["coal-port-richards-bay", "wp-moz-noord", "wp-malakka", "wp-scs", "wp-taiwan"],
      note: "Zuid-Afrikaans thermisch -> China via de Indische Oceaan en Malakka." },
    { from: "coal-southafrica", to: "coal-mkt-eu", value: 12, mode: "ship", stage: "raffinaat",
      via: ["coal-port-richards-bay", "wp-kaap", "wp-dover"],
      note: "De 2022-piek: Zuid-Afrikaans kool om de Kaap naar Europa toen de gascrisis de vraag opstuwde (grotendeels weer weggeëbd)." },
    { from: "coal-colombia", to: "coal-mkt-eu", value: 30, mode: "ship", stage: "raffinaat",
      via: ["coal-port-cerrejon", "wp-atl-west", "wp-dover"],
      note: "Colombiaanse thermisch -> Europa (ARA); piekte in 2022 door de gascrisis, structureel dalend." },
    { from: "coal-colombia", to: "coal-mkt-china-power", value: 15, mode: "ship", stage: "raffinaat",
      via: ["coal-port-cerrejon", "wp-caribisch", "wp-panama", "wp-pac-west", "wp-scs", "wp-taiwan"],
      note: "Colombiaans kool -> Azië via het Panamakanaal en de Stille Oceaan." },
    { from: "coal-port-vostochny", to: "coal-mkt-china-power", value: 90, mode: "ship", stage: "raffinaat",
      via: ["wp-taiwan"],
      note: "Russische Pacific-kolen -> China: de oost-draai na de EU-embargo (aug 2022)." },
    { from: "coal-port-vostochny", to: "coal-mkt-japan", value: 25, mode: "ship", stage: "raffinaat",
      note: "Russisch kool -> Japan over de Japanse Zee (verminderd maar niet weg na 2022)." },

    // === C. ZEEHANDEL COKESKOOL — exporteur -> staalfabriek (raffinaat) ======
    { from: "coal-australia-qld", to: "coal-mkt-india-steel", value: 55, mode: "ship", stage: "raffinaat",
      via: ["coal-port-haypoint", "wp-lombok", "wp-aceh"],
      note: "DE GROOTSTE COKESKOOL-STROOM: Bowen Basin -> de Indiase oostkust-staalindustrie. India is #1 cokeskool-importeur; Australië #1 exporteur." },
    { from: "coal-australia-qld", to: "coal-mkt-japan", value: 35, mode: "ship", stage: "raffinaat",
      via: ["coal-port-haypoint", "wp-pac-west"],
      note: "Premium harde cokeskool -> Japanse hoogovens." },
    { from: "coal-australia-qld", to: "coal-mkt-korea", value: 25, mode: "ship", stage: "raffinaat",
      via: ["coal-port-haypoint", "wp-pac-west", "wp-taiwan"],
      note: "-> POSCO-staal (Pohang)." },
    { from: "coal-australia-qld", to: "coal-mkt-china-steel", value: 30, mode: "ship", stage: "raffinaat",
      via: ["coal-port-haypoint", "wp-pac-west", "wp-scs", "wp-taiwan"],
      note: "Australische cokeskool -> Chinees staal: het zwaarst getroffen door de ban, hervat na begin 2023." },
    { from: "coal-canada", to: "coal-mkt-japan", value: 20, mode: "ship", stage: "raffinaat",
      via: ["coal-port-ridley", "wp-pac-noord"],
      note: "Elk Valley-cokeskool per spoor naar Ridley/Prince Rupert, dan de noordelijke Stille Oceaan over -> Japans staal (grote-cirkelroute)." },
    { from: "coal-canada", to: "coal-mkt-korea", value: 12, mode: "ship", stage: "raffinaat",
      via: ["coal-port-ridley", "wp-pac-noord", "wp-taiwan"],
      note: "-> Koreaans staal." },
    { from: "coal-us-appalachia", to: "coal-mkt-eu", value: 25, mode: "ship", stage: "raffinaat",
      via: ["coal-port-hampton", "wp-dover"],
      note: "Appalachische cokeskool -> Europees staal over de noordelijke Atlantische Oceaan." },
    { from: "coal-us-appalachia", to: "coal-mkt-india-steel", value: 18, mode: "ship", stage: "raffinaat",
      via: ["coal-port-hampton", "wp-atl-brazilie", "wp-kaap", "wp-moz-noord", "wp-aceh"],
      note: "US-cokeskool -> India-staal om de Kaap: de swing-leverancier die bijsprong toen Rusland/Australië-stromen omgelegd werden." },
    { from: "coal-mozambique", to: "coal-mkt-india-steel", value: 8, mode: "ship", stage: "raffinaat",
      via: ["coal-port-nacala", "wp-moz-noord", "wp-aceh"],
      note: "Moatize-cokeskool via de Nacala-spoorcorridor en de Indische Oceaan -> India-staal." },

    // === D. MONGOLIË-LANDCORRIDOR — cokeskool over de Gobi-grens (raffinaat) ==
    { from: "coal-mongolia", to: "coal-mkt-china-steel", value: 55, mode: "rail", stage: "raffinaat",
      via: ["grens-gashuunsukhait"],
      note: "DE LANDCORRIDOR: Tavan-Tolgoi-cokeskool per truck/spoor over de Gobi-grens (Gashuun Sukhait / Ganqimaodu) naar het Chinese staal. Verving de Australische cokeskool tijdens de ban — het enige nieuwe knelpunt van kolen, en het ligt op het land." },
  ],

  // ==========================================================================
  // SPANNINGEN — waar de kolenketen 'knijpt'. Anders dan bijna alle andere
  // grondstoffen is dat NIET één geografische trechter: de knijp is de
  // BINNENLANDSHEID (~85% verstookt waar gedolven) + een dunne, politiek
  // beladen zeelaag waarop China de swing-koper is.
  // ==========================================================================
  tensions: [
    { id: "coal-t-domestic", type: "structureel", title: "Kolen is binnenlands: ~85% wordt verbrand waar het gedolven wordt",
      lat: 38.0, lon: 108.0,
      nodes: ["coal-shanxi", "coal-innermongolia", "coal-india", "coal-us-powder"],
      flows: ["coal-shanxi>coal-port-qinhuangdao", "coal-innermongolia>coal-mkt-china-steel", "coal-port-qinhuangdao>coal-mkt-china-power"],
      metric: "wereldproductie ~8.700 Mt · zeehandel ~1.350 Mt (~15%)",
      note: "De kern-'aha' van kolen. Anders dan lithium (China-raffinage) of goud (Zwitserland) heeft kolen géén mondiale flessenhals, omdat het grotendeels helemaal niet reist: China, India, de VS en Rusland delven én verstoken hun eigen kolen. Op de kaart zijn de dikste stromen binnenlands (Shanxi->Qinhuangdao->Guangdong; Ordos->Hebei-staal), dof gekleurd, zonder ook maar één zeekruising. De hele geopolitiek speelt zich af op de dunne ~15% die wél over zee gaat." },

    { id: "coal-t-china-swing", type: "concentratie", title: "China: grootste producent én grootste importeur — de swing-koper",
      lat: 20.0, lon: 114.0,
      nodes: ["coal-mkt-china-power", "coal-indonesia", "coal-port-vostochny"],
      flows: ["coal-indonesia>coal-mkt-china-power", "coal-port-vostochny>coal-mkt-china-power", "coal-australia-nsw>coal-mkt-china-power"],
      metric: "China ~50% van de wereldproductie én #1 kolenimporteur — de marginale koper zet de zeeprijs",
      note: "China produceert de helft van al het kolen ter wereld en importeert er tóch het meest van. Die combinatie maakt China de swing-koper: z'n marginale importvraag (uit Indonesië, Australië, Rusland) bepaalt de internationale prijs, en z'n binnenlandse productie- of veiligheidsbeleid kan de zeemarkt in één klap doen zwellen of krimpen. Wie op de zeelaag handelt, handelt in feite op de Chinese marge." },

    { id: "coal-t-ban", type: "beleid", title: "De China-Australië-kolenban (2020-2023): een keten die zichzelf omlegde",
      lat: -25.0, lon: 150.0,
      nodes: ["coal-australia-nsw", "coal-australia-qld", "coal-mkt-japan", "coal-mkt-india-steel"],
      flows: ["coal-australia-qld>coal-mkt-china-steel", "coal-australia-qld>coal-mkt-india-steel", "coal-australia-nsw>coal-mkt-japan"],
      metric: "okt 2020 informele ban -> Australisch kool omgelegd naar India/Japan/Korea; China backfilde met Indonesië/Rusland/Mongolië",
      note: "Toen de diplomatieke betrekkingen bevroren, verbood China eind 2020 informeel Australische thermisch én cokeskool. In plaats van te verdampen legde de handel zichzelf om: Australisch kool vond nieuwe kopers in India, Japan en Korea, terwijl China de gaten vulde met Indonesisch/Russisch thermisch en Mongoolse/Russische/Amerikaanse cokeskool. Begin 2023 werd de ban stilletjes opgeheven, maar de nieuwe patronen bleven deels bestaan — een levend bewijs dat kolenstromen elastisch zijn zolang er genoeg havens zijn." },

    { id: "coal-t-coking", type: "concentratie", title: "Twee kolen: thermisch (stroom) vs. cokeskool (staal)",
      lat: -20.0, lon: 140.0,
      nodes: ["coal-australia-qld", "coal-mkt-india-steel", "coal-mkt-china-steel"],
      flows: ["coal-australia-qld>coal-mkt-india-steel", "coal-australia-qld>coal-mkt-japan", "coal-mongolia>coal-mkt-china-steel"],
      metric: "cokeskool ~1,1 Gt (vs. thermisch ~7,3 Gt) · premium harde cokeskool ~Bowen Basin · India = #1 importeur",
      note: "Kolen is niet één grondstof maar twee. Het leeuwendeel is thermisch (steenkool) dat in centrales tot stroom wordt verbrand. Een kleiner, hoogwaardiger deel is metallurgische cokeskool, die in cokesovens tot cokes wordt gebakken voor de hoogoven — de grondstof van bijna al het primaire staal. De premium harde cokeskool zit sterk geconcentreerd in het Australische Bowen Basin, en de grootste importeur is India, waar de eigen kool ongeschikt is voor cokes. Het is het staal, niet de stroom, dat de langste en meest geconcentreerde kolenroutes trekt." },

    { id: "coal-t-mongolia", type: "knelpunt", title: "Mongolië -> China over de Gobi: cokeskool zonder kust",
      lat: 42.9, lon: 105.9,
      nodes: ["coal-mongolia", "coal-mkt-china-steel"],
      flows: ["coal-mongolia>coal-mkt-china-steel"],
      metric: "Tavan Tolgoi -> Ganqimaodu/Gashuun Sukhait: het enige nieuwe knelpunt van kolen, en het ligt op het land",
      note: "Waar bijna elke andere grondstof op een zeestraat knijpt, ligt kolens ene nieuwe knelpunt op een landgrens: de Gobi-overgang Gashuun Sukhait / Ganqimaodu, waar Mongoolse cokeskool per truck en spoor China binnenrolt richting de staalfabrieken. Landlocked Mongolië heeft geen alternatief — al z'n export hangt aan die ene buur. Tijdens de China-Australië-ban schoot deze corridor omhoog als de vervanger van de Australische cokeskool. Zelfde patroon als Kasumbalesa (kobalt) en Ruili (zeldzame aardmetalen): een grenspost, geen zeestraat." },

    { id: "coal-t-transition", type: "structureel", title: "De grondstof die de energietransitie zou doden — op recordhoogte",
      lat: 22.0, lon: 82.0,
      nodes: ["coal-shanxi", "coal-india", "coal-indonesia"],
      flows: ["coal-indonesia>coal-mkt-india-power", "coal-indonesia>coal-mkt-china-power"],
      metric: "wereldvraag ~8,7 Gt (2023) — recordniveau, gedreven door China + India",
      note: "De paradox die de hele kaart draagt: ondanks klimaatbeleid, dalend Westers verbruik en de opkomst van hernieuwbaar staat de mondiale kolenvraag op een recordhoogte. De reden zit in Azië — de Chinese en Indiase elektriciteits- en staalgroei trekken meer kolen aan dan het Westen afbouwt. Het krimpende blok (VS/EU) is reëel maar klein tegenover de groeiende binnenlandse burn van de twee reuzen. Kolen is niet aan het verdwijnen; het is aan het verschuiven — geografisch, naar het oosten." },
  ],
});
