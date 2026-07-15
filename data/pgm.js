// ============================================================================
// PLATINAGROEPMETALEN (PGM: Pt/Pd/Rh) — volledig uitgewerkte module. Peiljaar ±2024.
// Cijfers indicatief/afgerond, o.b.v. USGS MCS 2025, Johnson Matthey PGM Market
// Report, WPIC en bedrijfsrapportages. Eenheid overal: t 3E/jaar (Pt+Pd+Rh
// gecombineerd, "3E"), zodat de hele keten optelbaar blijft. Zie design/pgm.md.
//
// DE VORM VAN PGM (de meest EXTREME twee-landen-concentratie van de atlas):
//   - Bijna al het PLATINA en RODIUM komt uit één geologische formatie: het
//     BUSHVELD-complex in Zuid-Afrika (een dichte kluwen diepe schachtmijnen bij
//     Rustenburg + de Noord- en Oost-rand). Bijna al het PALLADIUM komt uit één
//     Russische mijn: NORILSK (Nornickel), als bijproduct van Ni-Cu-sulfide.
//     Twee metalen, twee landen, twee eindmarkten. Dát is de PGM-"aha".
//   - PGM VLIEGT (net als goud): geraffineerd Pt/Pd/Rh is per kilo even waardevol
//     als goud -> beveiligde LUCHTVRACHT (mode "air": great-circle-boog, buiten de
//     A* om). Alleen de concentraat-/matte-hops binnen een land (en de Zimbabwaanse
//     matte naar Zuid-Afrika) gaan over land (road/rail). GEEN nieuwe render-modus,
//     GEEN nieuw chokepoint/vaarpunt (derde grondstof na koper/nikkel die niets aan
//     _chokepoints.js toevoegt).
//   - DE VRAAG HANGT AAN DE UITLAATPIJP: ~80-90% van het rodium, het gros van het
//     palladium en ~40% van het platina gaat in AUTOKATALYSATOREN. Emissienormen
//     sturen alles; draaien de Pt/Pd-prijzen om, dan SUBSTITUEREN autobouwers het
//     ene metaal voor het andere. De hedge tegen de EV-transitie is WATERSTOF
//     (Pt in PEM-elektrolysers/brandstofcellen; iridium voor de elektrolyser-anode).
//   - EEN WESTERSE MIDSTREAM (Johnson Matthey/BASF/Umicore/Heraeus/Tanaka) máákt de
//     katalysatoren én wint het metaal terug uit gebruikte katalysatoren = de
//     RECYCLING-kringloop (~25% van het aanbod).
//
// STAGES (via `stage`):
//   erts       = PGM-erts / concentraat / matte op weg naar een raffinaderij
//                (mijn -> smelter) — dof/donker platina-grijs.
//   raffinaat  = geraffineerd Pt/Pd/Rh (sponge/ingot/zouten) dat de lucht in gaat.
//   product    = autokatalysator / brandstofcel / sieraad / industrie — licht.
//
// TRANSPORT is LUCHTVRACHT (hergebruik goud-air-mode) + korte landhops:
// refined metal via de JNB-gateway de wereld in; concentraat/matte road/rail.
// De tijdlijn toont automatisch "vluchten" (activeHasAir()) — 0 engine-wijziging.
//
// RECYCLING (type "recycler" + node/flow.layer "recycle") = optionele toggle-laag,
// hergebruik van het REE-patroon met 0 engine-wijziging (de chip verschijnt via
// hasRecycle()). Beursvoorraden/exchange-laag (Pt/Pd-futures) bewust UITGESTELD.
// ============================================================================

REGISTER({
  id: "pgm",
  name: "Platinagroepmetalen",
  symbol: "PGM",
  color: "#D5D8DC",       // helder platina-wit: de mijn-markers
  flowColor: "#B7C1CE",   // koel zilver-grijs: de stromen (stages splitsen goed uit)
  detail: "uitgewerkt",
  unit: "t 3E/jaar (Pt+Pd+Rh, indicatief)",
  blurb: "Platina, palladium en rodium: katalysatoren, waterstof en sieraden. De scherpste " +
    "twee-landen-concentratie van de atlas — Zuid-Afrika (het Bushveld-complex) levert het gros " +
    "van het platina en rodium, Rusland (Norilsk) domineert het palladium. Geraffineerd metaal " +
    "vliegt (net als goud) via een handvol westerse edelmetaalhuizen, die de katalysatoren óók " +
    "recyclen. De vraag hangt aan de autokatalysator; de hedge is waterstof.",

  nodes: [
    // =============================================================== MIJNEN
    // --- Zuid-Afrika (~60% van 3E): het Bushveld, Pt/Rh-dominant ------------
    { id: "pgm-mogalakwena", type: "mine", name: "Mogalakwena", country: "Zuid-Afrika",
      lat: -24.10, lon: 28.95, share: 10, tier: 1, operator: "Anglo American Platinum",
      status: "actief", capacity: "grootste PGM-openpit ter wereld",
      note: "Noordelijke rand van het Bushveld (Mokopane); de enige grote open-pit — relatief Pd/Ni-rijk (Platreef). Erts per truck/conveyor naar de Amplats-raffinage bij Rustenburg." },
    { id: "pgm-impala-rust", type: "mine", name: "Impala Rustenburg", country: "Zuid-Afrika",
      lat: -25.55, lon: 27.42, share: 9, tier: 1, operator: "Impala Platinum (Implats)",
      status: "actief", capacity: "diepe schachtmijnen",
      note: "Het hart van de Westelijke rand; diepe, arbeidsintensieve Merensky/UG2-schachten. Concentraat -> de Impala-raffinaderij bij Springs." },
    { id: "pgm-sib-rustenburg", type: "mine", name: "Sibanye Rustenburg", country: "Zuid-Afrika",
      lat: -25.78, lon: 27.10, share: 7, tier: 2, operator: "Sibanye-Stillwater",
      status: "actief", capacity: "ex-Amplats Rustenburg-schachten",
      note: "De voormalige Amplats-Rustenburgmijnen, sinds 2016 van Sibanye. Westelijke rand, Pt/Rh-rijk." },
    { id: "pgm-marikana", type: "mine", name: "Marikana", country: "Zuid-Afrika",
      lat: -25.68, lon: 27.78, share: 6, tier: 2, operator: "Sibanye-Stillwater (ex-Lonmin)",
      status: "actief", capacity: "UG2/Merensky-schachten",
      note: "De ex-Lonmin-mijnen op de Westelijke rand — beladen geschiedenis (2012). Nu Sibanye; eigen smelt-/raffinagecapaciteit in de regio." },
    { id: "pgm-amandelbult", type: "mine", name: "Amandelbult", country: "Zuid-Afrika",
      lat: -24.58, lon: 27.30, share: 5, tier: 2, operator: "Anglo American Platinum",
      status: "actief", capacity: "Pt-rijk (Merensky/UG2)",
      note: "Noordwestelijke Bushveld (bij Thabazimbi); een van de Pt-rijkste Amplats-mijnen. -> Rustenburg PMR." },
    { id: "pgm-bafokeng", type: "mine", name: "Bafokeng / Styldrift", country: "Zuid-Afrika",
      lat: -25.38, lon: 27.05, share: 4, tier: 2, operator: "Royal Bafokeng Platinum (Implats)",
      status: "actief", capacity: "moderne mechaniseerbare mijn",
      note: "De RBPlat-mijnen (BRPM/Styldrift), sinds 2023 van Implats — relatief ondiep en mechaniseerbaar. -> Springs." },
    { id: "pgm-northam", type: "mine", name: "Northam Zondereinde", country: "Zuid-Afrika",
      lat: -24.90, lon: 27.20, share: 5, tier: 2, operator: "Northam Platinum",
      status: "actief", capacity: "diepste PGM-schachtmijn + eigen smelter",
      note: "Onafhankelijke producent op de Westelijke rand, met een eigen smelter op locatie. Matte -> eindraffinage." },
    { id: "pgm-two-rivers", type: "mine", name: "Two Rivers (Oostrand)", country: "Zuid-Afrika",
      lat: -25.00, lon: 30.12, share: 6, tier: 2, operator: "Implats / ARM e.a.",
      status: "actief", capacity: "Oostelijke Bushveld-cluster",
      note: "Staat voor de Oostelijke rand (Two Rivers, Mototolo, Modikwa, Booysendal): UG2-rijk, meer Pd dan de Westrand. -> Springs." },

    // --- Rusland (~25% van 3E): palladium-reus -----------------------------
    { id: "pgm-norilsk", type: "mine", name: "Norilsk", country: "Rusland",
      lat: 69.35, lon: 88.20, share: 25, tier: 1, operator: "Nornickel",
      status: "actief", capacity: "≈ 40% van het wereld-palladium",
      note: "Boven de poolcirkel; PGM (vooral PALLADIUM + platina) als bijproduct van het Ni-Cu-sulfide-erts. De op één na grootste PGM-bron ter wereld, maar sinds 2022 sanctie-/zelfsanctie-gevoelig." },

    // --- Zimbabwe (~8%): de Great Dyke --------------------------------------
    { id: "pgm-zimplats", type: "mine", name: "Zimplats", country: "Zimbabwe",
      lat: -18.60, lon: 30.40, share: 5, tier: 1, operator: "Zimplats (Implats)",
      status: "actief", capacity: "Great Dyke, grootste Zim-producent",
      note: "De Great Dyke bij Ngezi; smelt tot matte en stuurt die (nog) over land naar Zuid-Afrika voor eindraffinage. Zimbabwe dreigt met een ruw-matte-exportverbod om lokale verwerking af te dwingen." },
    { id: "pgm-mimosa", type: "mine", name: "Mimosa", country: "Zimbabwe",
      lat: -20.30, lon: 30.05, share: 2, tier: 3, operator: "Sibanye / Implats (JV)",
      status: "actief", capacity: "Great Dyke (zuid)",
      note: "Zuidelijke Great Dyke bij Zvishavane; concentraat/matte naar Zuid-Afrika." },
    { id: "pgm-unki", type: "mine", name: "Unki", country: "Zimbabwe",
      lat: -19.66, lon: 30.00, share: 1, tier: 3, operator: "Anglo American Platinum",
      status: "actief", capacity: "Great Dyke (Shurugwi)",
      note: "Amplats' Zimbabwaanse mijn met eigen smelter; matte -> Zuid-Afrikaanse eindraffinage." },

    // --- Noord-Amerika (~5%): het enige niet-ZA/RU-schakelpunt -------------
    { id: "pgm-stillwater", type: "mine", name: "Stillwater", country: "VS",
      lat: 45.38, lon: -109.90, share: 3, tier: 1, operator: "Sibanye-Stillwater",
      status: "actief", capacity: "enige Amerikaanse PGM-erts (Pd/Pt)",
      note: "Montana; de enige primaire PGM-mijn van de VS — palladium-rijk (J-M Reef). -> de eigen smelter/raffinage in Columbus." },
    { id: "pgm-lac-des-iles", type: "mine", name: "Lac des Îles", country: "Canada",
      lat: 49.18, lon: -89.60, share: 2, tier: 3, operator: "Impala Canada",
      status: "actief", capacity: "palladium-mijn",
      note: "Ontario, ten noorden van Thunder Bay; een van de weinige zuivere palladiummijnen. Concentraat naar Noord-Amerikaanse raffinage." },
    { id: "pgm-sudbury", type: "mine", name: "Sudbury (PGM-bijproduct)", country: "Canada",
      lat: 46.49, lon: -81.00, share: 2, tier: 3, operator: "Vale / Glencore",
      status: "actief", capacity: "PGM bij Ni-Cu",
      note: "Het Sudbury-bekken levert PGM als bijproduct van de nikkel-/kopersulfide-raffinage — hetzelfde district als bij nikkel." },

    // --- Finland (~1%): PGM als nikkelbijproduct ---------------------------
    { id: "pgm-kevitsa", type: "mine", name: "Kevitsa", country: "Finland",
      lat: 67.70, lon: 26.90, share: 1, tier: 3, operator: "Boliden",
      status: "actief", capacity: "Ni-Cu-PGM",
      note: "Fins-Lapland; PGM als bijproduct van het nikkel-/koper-erts. De enige noemenswaardige EU-PGM-bron; concentraat naar de Europese raffinage." },

    // ================================================= SMELTERS / RAFFINAGE
    // --- Zuid-Afrika: de trechter ------------------------------------------
    { id: "pgm-ref-rustenburg", type: "refinery", name: "Rustenburg PMR (Amplats)", country: "Zuid-Afrika",
      lat: -25.95, lon: 27.30, tier: 1, operator: "Anglo American Platinum",
      capacity: "grootste PGM-raffinaderij ter wereld",
      note: "De Precious Metals Refinery bij Rustenburg — het zwaartepunt van de wereld-PGM-raffinage. Erts van de West- en Noordrand -> geregistreerd Pt/Pd/Rh, dat via JNB de lucht in gaat." },
    { id: "pgm-ref-springs", type: "refinery", name: "Impala Refineries (Springs)", country: "Zuid-Afrika",
      lat: -26.28, lon: 28.70, tier: 1, operator: "Impala Platinum",
      capacity: "base + precious metal refining",
      note: "Bij Johannesburg; raffineert het Implats-concentraat én de Zimbabwaanse/Oostrand-matte tot geraffineerd metaal." },
    // --- Rusland ------------------------------------------------------------
    { id: "pgm-ref-krasnoyarsk", type: "refinery", name: "Krastsvetmet (Krasnoyarsk)", country: "Rusland",
      lat: 56.01, lon: 92.87, tier: 1, operator: "Krastsvetmet / Nornickel",
      capacity: "class-1 Pt/Pd/Rh",
      note: "Zuid-Siberië; raffineert de Norilsk-PGM tot geregistreerd metaal. Historisch London/Zürich good-delivery; sinds 2022 verschuift de afzet richting Azië." },
    // --- Noord-Amerika ------------------------------------------------------
    { id: "pgm-ref-columbus", type: "refinery", name: "Columbus (Sibanye-Stillwater)", country: "VS",
      lat: 45.63, lon: -109.25, tier: 2, operator: "Sibanye-Stillwater",
      capacity: "raffinage + autokat-recycling",
      note: "Montana; raffineert het Stillwater-erts én is een van 's werelds grootste recyclers van gebruikte autokatalysatoren." },
    // --- De westerse edelmetaalhuizen (raffinage + fabricage + recycling) ---
    { id: "pgm-fab-jm", type: "refinery", name: "Johnson Matthey (Royston)", country: "VK",
      lat: 52.05, lon: -0.02, tier: 1, operator: "Johnson Matthey",
      capacity: "autokat + PGM-raffinage + brandstofceltech",
      note: "'s Werelds grootste autokatalysator-maker en een van de grootste PGM-recyclers/raffineurs; ook een sleutelspeler in brandstofcel-/waterstoftech." },
    { id: "pgm-fab-basf", type: "refinery", name: "BASF Catalysts", country: "Duitsland",
      lat: 49.48, lon: 8.44, tier: 2, operator: "BASF",
      capacity: "mobiele-emissie-katalysatoren + recycling",
      note: "Ludwigshafen e.o.; grote maker van autokatalysatoren (met fabrieken op alle continenten) en PGM-recycler." },
    { id: "pgm-fab-umicore", type: "refinery", name: "Umicore (Hoboken)", country: "België",
      lat: 51.17, lon: 4.34, tier: 2, operator: "Umicore",
      capacity: "edelmetaalraffinage + autokat + recycling",
      note: "Antwerpen; een van 's werelds meest geïntegreerde edelmetaal-recyclers — wint PGM terug uit gebruikte katalysatoren en elektronica, en maakt er nieuwe katalysatoren mee." },
    { id: "pgm-fab-heraeus", type: "refinery", name: "Heraeus (Hanau)", country: "Duitsland",
      lat: 50.13, lon: 8.92, tier: 2, operator: "Heraeus Precious Metals",
      capacity: "PGM-chemie + industrie + recycling",
      note: "Hanau; edelmetaalchemie voor industrie, glas, chemie en de waterstof-/elektrolyse-keten, plus PGM-recycling." },
    { id: "pgm-fab-tanaka", type: "refinery", name: "Tanaka / Japanse edelmetaalhuizen", country: "Japan",
      lat: 35.90, lon: 139.55, tier: 3, operator: "Tanaka / Furuya",
      capacity: "autokat + industrie + recycling",
      note: "Bij Tokio; de Japanse PGM-fabricage en -recycling voor de eigen auto- en elektronica-industrie." },

    // ================================================================ GATEWAY
    { id: "pgm-air-jnb", type: "airport", name: "Johannesburg (JNB)", country: "Zuid-Afrika",
      lat: -26.13, lon: 28.24, tier: 2,
      note: "OR Tambo — de uitgaande trechter: vrijwel al het Zuid-Afrikaanse geraffineerde PGM vliegt hierlangs de wereld in." },

    // ================================================================ MARKT
    // Autokatalysator dominant; waterstof = de groeicurve; sieraad + industrie.
    { id: "pgm-mkt-autocat-china", type: "market", name: "China (autokatalysator)", country: "China",
      lat: 31.20, lon: 121.45, tier: 1,
      note: "De grootste automarkt ter wereld — de grootste autokat-vraag (Pd/Rh voor benzine). Ook een groeiende eigen recycling-/fabricageketen." },
    { id: "pgm-mkt-autocat-eu", type: "market", name: "EU (autokatalysator)", country: "Duitsland",
      lat: 48.78, lon: 9.18, tier: 1,
      note: "De Europese auto-industrie (Stuttgart e.o.); historisch diesel-zwaar = platina-intensief. Bevoorraad door JM/BASF/Umicore." },
    { id: "pgm-mkt-autocat-us", type: "market", name: "Noord-Amerika (autokatalysator)", country: "VS",
      lat: 42.33, lon: -83.05, tier: 2,
      note: "Detroit; de Noord-Amerikaanse auto-industrie, grotendeels benzine (Pd/Rh), deels bevoorraad door het eigen Stillwater/Columbus-metaal." },
    { id: "pgm-mkt-autocat-japan", type: "market", name: "Japan (autokatalysator)", country: "Japan",
      lat: 35.08, lon: 137.15, tier: 2,
      note: "Toyota-regio; Japanse autokat-vraag, bevoorraad via de eigen Tanaka-fabricage." },
    { id: "pgm-mkt-autocat-india", type: "market", name: "India (autokatalysator)", country: "India",
      lat: 18.52, lon: 73.85, tier: 3,
      note: "Pune; snelst groeiende autokat-vraag door de strengere BS6-emissienorm." },
    { id: "pgm-mkt-hydrogen", type: "market", name: "Waterstof (PEM / brandstofcel)", country: "Nederland",
      lat: 51.50, lon: 6.80, tier: 2,
      note: "De vraag-hedge tegen de EV-transitie: platina in PEM-elektrolysers (groene H₂) en brandstofcellen (FCEV); iridium is kritiek voor de elektrolyser-anode. Nu klein, structureel groeiend." },
    { id: "pgm-mkt-jewelry", type: "market", name: "Sieraad (China/India/Japan)", country: "China",
      lat: 22.55, lon: 114.10, tier: 2,
      note: "Platina-sieraden — vooral China (Shenzhen), India en Japan. Concurreert met goud en wisselt met de relatieve prijs." },
    { id: "pgm-mkt-industrial", type: "market", name: "Industrie (glas/chemie/elektronica)", country: "Zwitserland",
      lat: 47.55, lon: 7.60, tier: 3,
      note: "Glasvezel-bushings, chemische katalysatoren (salpeterzuur), petroraffinage en elektronica — een stabiele, brede industriële PGM-vraag." },

    // ============================================================= RECYCLING
    // Gebruikte autokatalysatoren -> terug naar de westerse raffinaderijen die ze
    // óók máken. type "recycler" + node/flow.layer "recycle": OPTIONELE toggle-laag
    // (REE-patroon, 0 engine-wijziging). ~25% van het aanbod. Default UIT.
    { id: "pgm-rec-eu", type: "recycler", name: "Europa (autokat-schroot)", country: "België",
      lat: 50.85, lon: 5.70, tier: 3, layer: "recycle",
      note: "Ingezamelde gebruikte katalysatoren uit Europa -> Umicore/JM/BASF, die het Pt/Pd/Rh terugwinnen. Grootste 'binnenlandse' EU-PGM-bron." },
    { id: "pgm-rec-us", type: "recycler", name: "VS (autokat-schroot)", country: "VS",
      lat: 41.50, lon: -87.60, tier: 3, layer: "recycle",
      note: "Amerikaanse gebruikte autokatalysatoren -> de Sibanye-Stillwater-recycling in Columbus (Montana)." },
    { id: "pgm-rec-japan", type: "recycler", name: "Japan (autokat-schroot)", country: "Japan",
      lat: 35.40, lon: 139.30, tier: 3, layer: "recycle",
      note: "Japans autokat- en elektronicaschroot (Kanagawa/industrieregio) -> terug via de Tanaka-recycling." },
    { id: "pgm-rec-china", type: "recycler", name: "China (autokat-schroot)", country: "China",
      lat: 30.60, lon: 120.30, tier: 3, layer: "recycle",
      note: "China's snelgroeiende eigen autokat-recycling — dempt een deel van de importbehoefte." },
  ],

  // ==========================================================================
  // STROMEN — value in t 3E/jaar. stage bepaalt de kleur (erts dof, raffinaat
  // vol platina, product licht). Refined metal reist per LUCHT (mode "air":
  // great-circle-boog via de JNB-gateway); concentraat/matte over land (road/rail).
  //
  //  A) Intra-Zuid-Afrika + Zimbabwe->ZA: mijn/matte -> raffinaderij (erts, land)
  //  B) Rusland/Noord-Amerika/Finland: erts -> raffinage (land)
  //  C) Zuid-Afrika -> wereld: geraffineerd metaal via JNB de lucht in (raffinaat)
  //  D) Rusland -> wereld (raffinaat, air)
  //  E) Fabrikant -> automarkt / waterstof / industrie (product)
  //  F) Recycling (layer:"recycle" -> alleen met de toggle): autokats terug
  // ==========================================================================
  flows: [
    // === A. INTRA-ZUID-AFRIKA + ZIMBABWE -> ZA (erts, over land) =============
    { from: "pgm-mogalakwena", to: "pgm-ref-rustenburg", value: 55, mode: "road", stage: "erts",
      note: "Mogalakwena-concentraat -> de Amplats-raffinage bij Rustenburg." },
    { from: "pgm-amandelbult", to: "pgm-ref-rustenburg", value: 28, mode: "road", stage: "erts",
      note: "Amandelbult (Pt-rijk) -> Rustenburg PMR." },
    { from: "pgm-sib-rustenburg", to: "pgm-ref-rustenburg", value: 38, mode: "road", stage: "erts",
      note: "Sibanye-Rustenburgconcentraat -> de raffinage ernaast." },
    { from: "pgm-marikana", to: "pgm-ref-rustenburg", value: 32, mode: "road", stage: "erts",
      note: "Marikana (Sibanye) -> Rustenburg-verwerking." },
    { from: "pgm-northam", to: "pgm-ref-rustenburg", value: 28, mode: "road", stage: "erts",
      note: "Northam smelt tot matte op locatie; de matte -> eindraffinage." },
    { from: "pgm-impala-rust", to: "pgm-ref-springs", value: 48, mode: "rail", stage: "erts",
      note: "Impala-Rustenburgconcentraat -> de Impala-raffinaderij bij Springs." },
    { from: "pgm-bafokeng", to: "pgm-ref-springs", value: 22, mode: "rail", stage: "erts",
      note: "RBPlat/Styldrift (nu Implats) -> Springs." },
    { from: "pgm-two-rivers", to: "pgm-ref-springs", value: 33, mode: "rail", stage: "erts",
      note: "De Oostelijke Bushveld-rand (Pd-rijker) -> Springs." },
    { from: "pgm-zimplats", to: "pgm-ref-springs", value: 26, mode: "road", stage: "erts",
      note: "Zimplats-matte over land (via Beitbridge) naar Zuid-Afrika voor eindraffinage — zolang Zimbabwe geen eigen raffinage heeft." },
    { from: "pgm-mimosa", to: "pgm-ref-springs", value: 11, mode: "road", stage: "erts",
      note: "Mimosa-concentraat/matte -> Zuid-Afrika." },
    { from: "pgm-unki", to: "pgm-ref-springs", value: 6, mode: "road", stage: "erts",
      note: "Unki-matte -> Zuid-Afrikaanse eindraffinage." },

    // === B. RUSLAND / NOORD-AMERIKA / FINLAND -> RAFFINAGE (erts, land) ======
    { from: "pgm-norilsk", to: "pgm-ref-krasnoyarsk", value: 90, mode: "rail", stage: "erts",
      note: "Norilsk-PGM (vooral palladium) -> de Krastsvetmet-raffinage in Krasnoyarsk, binnen Rusland over land." },
    { from: "pgm-stillwater", to: "pgm-ref-columbus", value: 18, mode: "road", stage: "erts",
      note: "Stillwater-erts -> de eigen smelter/raffinage in Columbus (Montana)." },
    { from: "pgm-lac-des-iles", to: "pgm-ref-columbus", value: 9, mode: "rail", stage: "erts",
      note: "Lac des Îles-palladiumconcentraat -> Noord-Amerikaanse raffinage." },
    { from: "pgm-sudbury", to: "pgm-ref-columbus", value: 7, mode: "rail", stage: "erts",
      note: "Sudbury-PGM (Ni-Cu-bijproduct) -> raffinage." },
    { from: "pgm-kevitsa", to: "pgm-fab-umicore", value: 5, mode: "rail", stage: "erts",
      note: "Fins Ni-Cu-PGM-concentraat -> de Europese edelmetaalraffinage (Umicore), over land om de Oostzee." },

    // === C. ZUID-AFRIKA -> WERELD (raffinaat, LUCHTVRACHT via JNB) ===========
    { from: "pgm-ref-rustenburg", to: "pgm-fab-jm", value: 45, mode: "air", stage: "raffinaat", via: ["pgm-air-jnb"],
      note: "Geraffineerd Zuid-Afrikaans Pt/Rh -> Johnson Matthey (VK) voor autokat-fabricage. De dikste luchtboog uit Afrika." },
    { from: "pgm-ref-rustenburg", to: "pgm-fab-basf", value: 30, mode: "air", stage: "raffinaat", via: ["pgm-air-jnb"],
      note: "ZA-metaal -> BASF (Duitsland)." },
    { from: "pgm-ref-rustenburg", to: "pgm-mkt-autocat-china", value: 42, mode: "air", stage: "raffinaat", via: ["pgm-air-jnb"],
      note: "ZA-metaal rechtstreeks naar de Chinese autokat-/fabricageketen — de grootste vraag." },
    { from: "pgm-ref-rustenburg", to: "pgm-mkt-jewelry", value: 20, mode: "air", stage: "raffinaat", via: ["pgm-air-jnb"],
      note: "Platina -> de Aziatische sieraadmarkt (Shenzhen)." },
    { from: "pgm-ref-rustenburg", to: "pgm-mkt-autocat-india", value: 8, mode: "air", stage: "raffinaat", via: ["pgm-air-jnb"],
      note: "ZA-metaal -> de groeiende Indiase autokat-vraag (BS6)." },
    { from: "pgm-ref-springs", to: "pgm-fab-umicore", value: 26, mode: "air", stage: "raffinaat", via: ["pgm-air-jnb"],
      note: "Implats-metaal (incl. de Zim-matte) -> Umicore (België)." },
    { from: "pgm-ref-springs", to: "pgm-fab-tanaka", value: 22, mode: "air", stage: "raffinaat", via: ["pgm-air-jnb"],
      note: "ZA-metaal -> de Japanse edelmetaalhuizen (Tanaka)." },
    { from: "pgm-ref-springs", to: "pgm-fab-heraeus", value: 18, mode: "air", stage: "raffinaat", via: ["pgm-air-jnb"],
      note: "ZA-metaal -> Heraeus (Duitsland) voor industrie/waterstof." },

    // === D. RUSLAND -> WERELD (raffinaat, LUCHTVRACHT) =======================
    { from: "pgm-ref-krasnoyarsk", to: "pgm-fab-basf", value: 28, mode: "air", stage: "raffinaat",
      note: "Russisch palladium -> de Europese autokat-fabricage (BASF). Historisch de grootste Pd-stroom; sinds 2022 onder sanctie-/zelfsanctiedruk." },
    { from: "pgm-ref-krasnoyarsk", to: "pgm-mkt-autocat-china", value: 40, mode: "air", stage: "raffinaat",
      note: "Russisch palladium -> China, in toenemende mate de nieuwe afzet nu de westerse markt terugtrekt." },
    { from: "pgm-ref-krasnoyarsk", to: "pgm-fab-jm", value: 16, mode: "air", stage: "raffinaat",
      note: "Russisch Pd/Pt -> Johnson Matthey (VK)." },

    // === E. FABRIKANT -> AUTOMARKT / WATERSTOF / INDUSTRIE (product) =========
    { from: "pgm-fab-jm", to: "pgm-mkt-autocat-eu", value: 40, mode: "rail", stage: "product",
      note: "JM-katalysatoren (VK) -> de Europese auto-industrie, over land via de Kanaaltunnel." },
    { from: "pgm-fab-basf", to: "pgm-mkt-autocat-eu", value: 42, mode: "road", stage: "product",
      note: "BASF-katalysatoren -> de Europese auto-industrie." },
    { from: "pgm-fab-umicore", to: "pgm-mkt-autocat-eu", value: 30, mode: "road", stage: "product",
      note: "Umicore-katalysatoren -> de Europese auto-industrie." },
    { from: "pgm-fab-basf", to: "pgm-mkt-autocat-china", value: 20, mode: "air", stage: "product",
      note: "BASF levert ook de Chinese markt (deels via lokale fabrieken) — hier als luchtstroom vereenvoudigd." },
    { from: "pgm-fab-tanaka", to: "pgm-mkt-autocat-japan", value: 26, mode: "road", stage: "product",
      note: "Tanaka-katalysatoren -> de Japanse auto-industrie." },
    { from: "pgm-ref-columbus", to: "pgm-mkt-autocat-us", value: 22, mode: "rail", stage: "product",
      note: "Amerikaans metaal (Stillwater + recycling) -> de Noord-Amerikaanse auto-industrie." },
    { from: "pgm-fab-heraeus", to: "pgm-mkt-hydrogen", value: 14, mode: "road", stage: "product",
      note: "Heraeus-platina/iridium -> PEM-elektrolysers en brandstofcellen: de groeicurve die de EV-daling moet opvangen." },
    { from: "pgm-fab-jm", to: "pgm-mkt-hydrogen", value: 10, mode: "rail", stage: "product",
      note: "JM-brandstofcel-/elektrolysetech -> de Europese waterstofketen, over land via de Kanaaltunnel." },
    { from: "pgm-fab-heraeus", to: "pgm-mkt-industrial", value: 12, mode: "road", stage: "product",
      note: "Heraeus-PGM -> glasvezel, chemie en elektronica — de brede industriële vraag." },

    // === F. RECYCLING (layer:"recycle" -> alleen met de toggle) =============
    // Gebruikte autokatalysatoren -> terug naar de raffinaderijen die ze máken.
    { from: "pgm-rec-eu", to: "pgm-fab-umicore", value: 30, mode: "road", stage: "erts", layer: "recycle",
      note: "Europees autokat-schroot -> Umicore-recycling: Pt/Pd/Rh terug de keten in zonder nieuwe mijnbouw." },
    { from: "pgm-rec-eu", to: "pgm-fab-jm", value: 14, mode: "rail", stage: "erts", layer: "recycle",
      note: "Europees autokat-schroot -> JM-recycling (VK), over land via de Kanaaltunnel." },
    { from: "pgm-rec-us", to: "pgm-ref-columbus", value: 22, mode: "rail", stage: "erts", layer: "recycle",
      note: "Amerikaans autokat-schroot -> de Sibanye-Stillwater-recycling in Columbus." },
    { from: "pgm-rec-japan", to: "pgm-fab-tanaka", value: 12, mode: "road", stage: "erts", layer: "recycle",
      note: "Japans autokat-/elektronicaschroot -> Tanaka-recycling." },
    { from: "pgm-rec-china", to: "pgm-mkt-autocat-china", value: 15, mode: "road", stage: "erts", layer: "recycle",
      note: "China's groeiende eigen autokat-recycling -> terug de binnenlandse markt in." },
  ],

  // ==========================================================================
  // SPANNINGEN — waar de PGM-keten knijpt. Verwijst naar node-ids en
  // flows ("from-id>to-id"). De PGM-knijp is niet geografisch (een zeestraat)
  // maar STRUCTUREEL: twee landen, twee metalen, de autokat-leiband, de ZA-stroomcrisis.
  // ==========================================================================
  tensions: [
    { id: "pgm-t-concentration", type: "concentratie", title: "Twee landen, twee metalen: Bushveld & Norilsk",
      lat: -25.7, lon: 27.4,
      nodes: ["pgm-mogalakwena", "pgm-impala-rust", "pgm-sib-rustenburg", "pgm-norilsk", "pgm-ref-rustenburg"],
      flows: ["pgm-mogalakwena>pgm-ref-rustenburg", "pgm-impala-rust>pgm-ref-springs",
              "pgm-norilsk>pgm-ref-krasnoyarsk"],
      metric: "Zuid-Afrika ≈ 70% van Pt + ~80% van Rh · Rusland ≈ 40% van Pd",
      note: "De scherpste bron-concentratie van de atlas na de zeldzame aardmetalen — maar hier gesplitst over twee metalen én twee landen. Bijna al het platina en rodium komt uit één geologische formatie (het Bushveld bij Rustenburg), bijna al het palladium uit één Russische mijn (Norilsk). Een schok in het ene land raakt een ánder metaal dan een schok in het andere: een Zuid-Afrikaanse stroomstoring knijpt Pt/Rh, een Russische sanctie knijpt Pd." },

    { id: "pgm-t-autocat", type: "structureel", title: "De autokatalysator-leiband + Pt↔Pd-substitutie",
      lat: 40.0, lon: 40.0,
      nodes: ["pgm-mkt-autocat-china", "pgm-mkt-autocat-eu", "pgm-mkt-autocat-us", "pgm-fab-jm", "pgm-fab-basf"],
      flows: ["pgm-fab-jm>pgm-mkt-autocat-eu", "pgm-fab-basf>pgm-mkt-autocat-eu",
              "pgm-ref-rustenburg>pgm-mkt-autocat-china"],
      metric: "~80-90% van Rh, het gros van Pd en ~40% van Pt gaat in autokatalysatoren",
      note: "De PGM-vraag hangt aan de uitlaatpijp. Emissienormen (Euro/China/US/BS6) bepalen hoeveel metaal per auto nodig is; benzinemotoren gebruiken vooral Pd/Rh, diesel vooral Pt. Toen palladium in 2019-2022 duurder werd dan platina, begonnen autobouwers Pt terug te substitueren in benzinekatalysatoren — een levende marktdynamiek die de twee metalen aan elkaar koppelt. De grote onzekerheid eronder: de EV-transitie schrapt op termijn de autokat volledig (hybrides rekken het)." },

    { id: "pgm-t-rhodium", type: "spof", title: "Rodium: minuscuul volume, extreme prijs, één land",
      lat: -25.9, lon: 27.3,
      nodes: ["pgm-ref-rustenburg", "pgm-sib-rustenburg", "pgm-mogalakwena"],
      flows: ["pgm-sib-rustenburg>pgm-ref-rustenburg", "pgm-ref-rustenburg>pgm-mkt-autocat-china"],
      metric: "~24 t Rh/jaar wereldwijd · ~80% uit Zuid-Afrika · piek ~$29.000/oz (2021)",
      note: "Rodium is het onzichtbare breekpunt. Nauwelijks 24 ton per jaar, maar onmisbaar voor de NOx-reductie in benzinekatalysatoren en voor ~80% uit hetzelfde Bushveld afkomstig. De piepkleine markt maakt de prijs extreem volatiel: in 2021 raakte rodium ~$29.000 per ounce — een veelvoud van goud. Een enkele verstoring in de Zuid-Afrikaanse raffinage tikt direct door in de autoproductie wereldwijd." },

    { id: "pgm-t-russia", type: "beleid", title: "Palladium & Rusland: Norilsk + sanctierisico",
      lat: 69.35, lon: 88.2,
      nodes: ["pgm-norilsk", "pgm-ref-krasnoyarsk", "pgm-fab-basf", "pgm-mkt-autocat-china"],
      flows: ["pgm-norilsk>pgm-ref-krasnoyarsk", "pgm-ref-krasnoyarsk>pgm-fab-basf",
              "pgm-ref-krasnoyarsk>pgm-mkt-autocat-china"],
      metric: "Rusland ≈ 40% van het wereld-palladium, uit één mijn (Norilsk)",
      note: "Palladium is de Russische kant van de PGM-medaille: ~40% van de wereld uit Nornickels Norilsk. PGM viel grotendeels buiten de formele sancties na 2022 (te kritiek), maar 'zelfsanctie' door westerse kopers en logistieke frictie verlegden de stroom richting Azië. De westerse auto-industrie zit zo met een structurele afhankelijkheid van één vijandige leverancier voor een metaal zonder makkelijk alternatief — behalve Pt-substitutie en recycling." },

    { id: "pgm-t-hydrogen", type: "structureel", title: "De waterstof-ommekeer: Pt/Ir voor elektrolyse & brandstofcellen",
      lat: 51.5, lon: 6.8,
      nodes: ["pgm-mkt-hydrogen", "pgm-fab-heraeus", "pgm-fab-jm"],
      flows: ["pgm-fab-heraeus>pgm-mkt-hydrogen", "pgm-fab-jm>pgm-mkt-hydrogen"],
      metric: "Pt in PEM-elektrolysers + brandstofcellen · Ir kritiek voor de anode",
      note: "De hedge tegen de EV-transitie. Terwijl de accu-elektrische auto de autokat-vraag bedreigt, opent groene waterstof een nieuwe: PEM-elektrolysers en brandstofcellen draaien op platina, en de anode op iridium — óók een platinagroepmetaal, en nog schaarser dan rodium. Nu nog een dun draadje naast de dikke autokat-bundel, maar de structurele groeirichting die bepaalt of de PGM-vraag na piek-ICE overeind blijft." },

    { id: "pgm-t-eskom", type: "beleid", title: "Zuid-Afrika: stroomcrisis knijpt de smelters",
      lat: -25.95, lon: 27.3,
      nodes: ["pgm-ref-rustenburg", "pgm-ref-springs", "pgm-impala-rust", "pgm-sib-rustenburg"],
      flows: ["pgm-impala-rust>pgm-ref-springs", "pgm-mogalakwena>pgm-ref-rustenburg"],
      metric: "Eskom-load-shedding + diepe, dure schachten + lage Pt/Pd-prijzen (2023-24)",
      note: "Bovenop de geologische concentratie ligt een operationele: de Zuid-Afrikaanse mijnen zijn diep, arbeidsintensief en stroom-hongerig — en Eskom levert die stroom onbetrouwbaar (jarenlange load-shedding). Samen met de ingezakte Pt/Pd-prijzen sinds 2023 duwt dat de hoogste-kosten-schachten richting sluiting en herstructurering. De wereldvoorziening van Pt en Rh hangt zo niet alleen aan één land, maar aan het elektriciteitsnet van dat land." },
  ],
});
