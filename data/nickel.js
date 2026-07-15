// ============================================================================
// NIKKEL (Ni) — volledig uitgewerkte module. Peiljaar ±2024.
// Cijfers indicatief/afgerond, o.b.v. USGS MCS 2025, INSG, IEA en bedrijfs-
// rapportages. Eenheid overal: kt Ni-inhoud/jaar (metaalinhoud, niet bruto
// lateriet), zodat de hele keten optelbaar blijft. Zie data/../design/nikkel.md.
//
// DE VORM VAN NIKKEL (de trechter staat op z'n kop t.o.v. koper/lithium):
//   - Bij koper/lithium graaft de wereld breed en RAFFINEERT China. Bij nikkel
//     heeft INDONESIË in tien jaar de mijnbouw ÉN de raffinage naar zich toe
//     getrokken: de exportban op ruw erts (2014 deels, 2020 volledig) dwong de
//     smelters aan land, grotendeels met CHINEES kapitaal (Tsingshan/Huayou) in
//     de parken IMIP (Morowali) en IWIP (Weda Bay). Het erts blíjft dus in het
//     land; wat de zee op gaat is al NPI, matte of MHP. Dát is de nikkel-"aha".
//   - TWEE NIKKELS: class-2 (NPI/ferronikkel, RKEF uit lateriet) -> ROESTVRIJ
//     STAAL (~⅔ van de vraag). class-1 (nikkelsulfaat/kathode, ≥99,8%) -> EV-
//     BATTERIJEN. HPAL (-> MHP) en matte zijn de bruggen die goedkoop lateriet
//     tóch batterijwaardig maken.
//   - SHAKEOUT: de Indonesische overvloed crashte de prijs en legde de klassieke
//     class-1-winning stil (BHP Nickel West 2024, Nieuw-Caledonië in crisis).
//
// STAGES (via `stage`):
//   erts       = ruw lateriet / sulfide-erts of -concentraat op weg naar een
//                smelter — dof/donker staalgrijs.
//   raffinaat  = NPI · ferronikkel · matte · MHP · geraffineerd class-1 ·
//                nikkelsulfaat — volle staalkleur.
//   product    = roestvrij staal / batterijkathode — licht.
//
// TRANSPORT is schip + land (géén nieuwe render-modus, géén nieuw chokepoint):
// alle routes bestaan al (Makassar/Lombok/SCS/Taiwan, Deense Straten, Panama +
// de Pacific-vaarpunten, de Saint-Laurent-keten). Landlocked/inland-nodes via
// het kobalt/koper-corridorpatroon (land-flow -> haven + aparte ship-flow).
//
// BEURSVOORRADEN (type "exchange" / flow.layer "exchange") = de BESTAANDE
// optionele toggle van koper, hergebruikt zonder engine-wijziging. Nikkel-nuance:
// alléén class-1 is LME-leverbaar (NPI/MHP/sulfaat niet) -> de LME-prijs raakte
// los van de fysieke markt; de short-squeeze van maart 2022 (Tsingshan) legde dat bloot.
// ============================================================================

REGISTER({
  id: "nickel",
  name: "Nikkel",
  symbol: "Ni",
  color: "#AEB4BC",       // staal-zilver: de mijn-markers
  flowColor: "#93A7BC",   // koel staalgrijs-blauw: de stromen (stages splitsen goed uit)
  detail: "uitgewerkt",
  unit: "kt Ni/jaar (indicatief)",
  blurb: "Roestvrij staal (⅔) en EV-batterijkathodes. Indonesië heeft binnen tien jaar " +
    "de mijnbouw én de raffinage naar zich toe getrokken via de exportban op ruw erts — " +
    "met Chinees kapitaal in de parken Morowali (IMIP) en Weda Bay (IWIP). Het erts blijft " +
    "in het land; wat de zee op gaat is al NPI, matte of MHP. Twee nikkels (class-1 batterij " +
    "vs. class-2 roestvrij), één prijscrash die de rest opruimt.",

  nodes: [
    // =============================================================== MIJNEN
    // --- Indonesië (~55%): lateriet dat in het land blijft -----------------
    { id: "ni-weda-bay", type: "mine", name: "Weda Bay", country: "Indonesië",
      lat: 0.60, lon: 128.05, share: 15, tier: 1, operator: "Eramet / Tsingshan (IWIP)",
      status: "actief", capacity: "≈ 550 kt Ni/j (groeiend)",
      note: "Halmahera; een van de grootste nikkelmijnen ter wereld. Lateriet gaat rechtstreeks de smelter van het IWIP-park in — niet de zee op." },
    { id: "ni-morowali-mines", type: "mine", name: "Morowali-district", country: "Indonesië",
      lat: -2.35, lon: 121.80, share: 12, tier: 1, operator: "diverse (IMIP-feed)",
      status: "actief", capacity: "feed voor IMIP",
      note: "Centraal-Sulawesi; de laterietmijnen die het Tsingshan-park IMIP voeden. Erts per truck/conveyor naar de smelter ernaast." },
    { id: "ni-sorowako", type: "mine", name: "Sorowako (Vale)", country: "Indonesië",
      lat: -2.53, lon: 121.36, share: 6, tier: 2, operator: "PT Vale Indonesia",
      status: "actief", capacity: "≈ 70 kt Ni/j (matte)",
      note: "Zuid-Sulawesi (Meer van Matano); eigen matte-smelter op locatie. De matte gaat per truck naar Malili en per schip naar Sumitomo in Japan — de oudere, class-1-achtige route." },
    { id: "ni-pomalaa", type: "mine", name: "Pomalaa", country: "Indonesië",
      lat: -4.18, lon: 121.62, share: 8, tier: 2, operator: "Antam / Vale-Huayou",
      status: "actief", capacity: "lateriet; nieuwe HPAL in aanbouw",
      note: "Zuidoost-Sulawesi; klassiek Antam-lateriet, plus de Vale-Huayou-HPAL (project) die het batterijwaardig gaat maken." },
    { id: "ni-obi", type: "mine", name: "Obi (Harita)", country: "Indonesië",
      lat: -1.63, lon: 127.65, share: 8, tier: 2, operator: "Harita Nickel",
      status: "actief", capacity: "lateriet + HPAL",
      note: "Noord-Molukken; Harita's geïntegreerde eiland — lateriet en de eerste Indonesische HPAL (MHP voor batterijen)." },

    // --- Filipijnen (~9%): lateriet dat nog wél als RUW erts vertrekt -------
    { id: "ni-philippines", type: "mine", name: "Surigao / Taganito", country: "Filipijnen",
      lat: 9.50, lon: 125.90, share: 9, tier: 1, operator: "Nickel Asia (NAC)",
      status: "actief", coastal: true, capacity: "≈ 330 kt Ni/j",
      note: "Mindanao; de Filipijnen exporteren nog altijd RUW lateriet naar Chinese smelters — het levende contrast met de Indonesische exportban." },
    { id: "ni-coralbay", type: "mine", name: "Coral Bay (Palawan)", country: "Filipijnen",
      lat: 8.50, lon: 117.60, share: 2, tier: 3, operator: "Sumitomo Metal Mining (HPAL)",
      status: "actief", coastal: true, capacity: "HPAL — MHP/matte",
      note: "Palawan; SMM's HPAL maakt van Filipijns lateriet class-1-tussenproduct (MHP/matte) dat naar de Sumitomo-raffinaderij in Japan vaart." },

    // --- Nieuw-Caledonië (~6%): in crisis door de prijscrash ---------------
    { id: "ni-doniambo", type: "mine", name: "Doniambo (SLN)", country: "Nieuw-Caledonië",
      lat: -22.27, lon: 166.44, share: 3, tier: 1, operator: "SLN (Eramet)",
      status: "actief", coastal: true, capacity: "ferronikkel",
      note: "Nouméa; het historische SLN-ferronikkelbedrijf. In structurele crisis — de goedkope Indonesische NPI heeft de marges weggevaagd (staatssteun/reddingsplannen sinds 2024)." },
    { id: "ni-goro", type: "mine", name: "Goro / Prony", country: "Nieuw-Caledonië",
      lat: -22.30, lon: 167.00, share: 3, tier: 2, operator: "Prony Resources",
      status: "actief", coastal: true, capacity: "NiO / class-1-tussenproduct",
      note: "Zuidpunt van Grande Terre; HPAL-achtige verwerking tot class-1 (batterij). Ook hier drukt de Indonesische overvloed op de levensvatbaarheid." },

    // --- De klassieke sulfide-gordel (class-1, krimpend) -------------------
    { id: "ni-norilsk", type: "mine", name: "Norilsk", country: "Rusland",
      lat: 69.35, lon: 88.20, share: 5, tier: 1, operator: "Nornickel",
      status: "actief", capacity: "≈ 190 kt Ni/j (class-1)",
      note: "Boven de poolcirkel; sulfide-erts met on-site smelting tot matte. Hoogzuiver class-1 (LME-leverbaar), maar sinds 2022 sanctie-gevoelig — steeds meer richting China." },
    { id: "ni-sudbury", type: "mine", name: "Sudbury Basin", country: "Canada",
      lat: 46.49, lon: -81.00, share: 3, tier: 2, operator: "Vale / Glencore",
      status: "actief", capacity: "sulfide-erts",
      note: "Ontario; het oudste grote nikkeldistrict ter wereld (inslagkrater). Sulfide-erts -> matte -> class-1." },
    { id: "ni-voiseys", type: "mine", name: "Voisey's Bay", country: "Canada",
      lat: 56.33, lon: -62.10, share: 2, tier: 2, operator: "Vale",
      status: "actief", coastal: true, capacity: "sulfide-concentraat",
      note: "Labrador; hoogwaardig concentraat dat per schip de Saint-Laurent op gaat naar de smelter (Sudbury / Long Harbour)." },
    { id: "ni-nickelwest", type: "mine", name: "Nickel West / Mt Keith", country: "Australië",
      lat: -30.75, lon: 121.47, tier: 1, operator: "BHP",
      status: "project", potential: "grotendeels stilgelegd (2024)",
      note: "West-Australië; BHP legde Nickel West eind 2024 stil — het duidelijkste symbool van de shakeout die de Indonesische overvloed veroorzaakte. Geen exportstroom meer." },
    { id: "ni-murrin", type: "mine", name: "Murrin Murrin", country: "Australië",
      lat: -28.76, lon: 121.89, share: 2, tier: 2, operator: "Glencore",
      status: "actief", capacity: "lateriet (class-1)",
      note: "West-Australië; een van de weinige Australische mijnen die nog draait — lateriet-HPAL tot class-1, per spoor naar Esperance." },
    { id: "ni-jinchuan-mine", type: "mine", name: "Jinchuan (Gansu)", country: "China",
      lat: 38.40, lon: 102.10, share: 3, tier: 2, operator: "Jinchuan Group",
      status: "actief", capacity: "sulfide-erts",
      note: "China's eigen sulfide-district (Jinchang) — bescheiden t.o.v. de Chinese raffinage-/batterijmacht, maar de klassieke binnenlandse class-1-bron." },
    { id: "ni-brazil", type: "mine", name: "Barro Alto / Onça Puma", country: "Brazilië",
      lat: -14.97, lon: -48.91, share: 2, tier: 3, operator: "Anglo American / Vale",
      status: "actief", capacity: "ferronikkel",
      note: "Goiás/Pará; lateriet -> ferronikkel, grotendeels voor de Atlantische (EU/VS) roestvrij-markt via Vitória." },
    { id: "ni-ambatovy", type: "mine", name: "Ambatovy", country: "Madagaskar",
      lat: -18.83, lon: 48.30, share: 2, tier: 3, operator: "Sumitomo / KMG",
      status: "actief", capacity: "HPAL — class-1",
      note: "Een van 's werelds grootste HPAL-projecten; lateriet -> class-1-briketten/sulfaat, per pijp naar Toamasina en per schip naar Azië." },
    { id: "ni-moa", type: "mine", name: "Moa Bay", country: "Cuba",
      lat: 20.66, lon: -74.94, share: 1, tier: 3, operator: "Sherritt / staat",
      status: "actief", coastal: true, capacity: "gemengd sulfide (Ni+Co)",
      note: "Oost-Cuba; HPAL-tussenproduct dat historisch in Canada werd afgeraffineerd, nu vooral richting China (embargo sluit de VS uit)." },

    // ================================================= SMELTERS / RAFFINAGE
    // --- De Indonesische cluster (de nieuwe trechter) ----------------------
    { id: "ni-ref-imip", type: "refinery", name: "IMIP Morowali", country: "Indonesië",
      lat: -2.83, lon: 122.15, tier: 1, operator: "Tsingshan e.a.", coastal: true,
      capacity: "RKEF-NPI + roestvrij; ook HPAL",
      note: "Het Indonesia Morowali Industrial Park: lateriet -> NPI -> roestvrij staal, ter plekke. De motor van de exportban — captieve kolencentrales, captieve jetty, Chinees kapitaal." },
    { id: "ni-ref-qmb", type: "refinery", name: "QMB / Huayou HPAL (Morowali)", country: "Indonesië",
      lat: -2.62, lon: 121.98, tier: 1, operator: "Huayou / GEM / CATL", coastal: true,
      capacity: "HPAL — MHP (batterij)",
      note: "De HPAL-lijn bij Morowali die lateriet omzet in MHP (mixed hydroxide) — de brug naar batterijnikkel. Vaart naar de Chinese sulfaatraffinage." },
    { id: "ni-ref-iwip", type: "refinery", name: "IWIP Weda Bay", country: "Indonesië",
      lat: 0.42, lon: 127.85, tier: 1, operator: "Tsingshan / Eramet", coastal: true,
      capacity: "RKEF-NPI + HPAL-matte",
      note: "Het Weda Bay-park op Halmahera: NPI voor roestvrij + matte/MHP voor batterijen. Samen met IMIP het zwaartepunt van de wereldnikkelraffinage." },
    { id: "ni-ref-obi", type: "refinery", name: "Harita HPAL (Obi)", country: "Indonesië",
      lat: -1.85, lon: 127.40, tier: 2, operator: "Harita / Ningbo Lygend", coastal: true,
      capacity: "HPAL — MHP",
      note: "De eerste Indonesische HPAL (2021); MHP naar de Chinese en Koreaanse batterijketen." },
    { id: "ni-ref-pomalaa", type: "refinery", name: "Pomalaa HPAL", country: "Indonesië",
      lat: -4.45, lon: 121.45, tier: 3, operator: "Vale / Huayou / Ford",
      status: "project", coastal: true, capacity: "HPAL — MHP (in aanbouw)",
      note: "Groot HPAL-project (Vale-Huayou, met Ford als afnemer) dat het Zuidoost-Sulawesi-lateriet batterijwaardig moet maken." },

    // --- China: batterijchemie + klassiek class-1 --------------------------
    { id: "ni-ref-china-sulphate", type: "refinery", name: "Nikkelsulfaat (Zhejiang)", country: "China",
      lat: 29.95, lon: 121.85, tier: 1, operator: "Huayou / GEM / CNGR", coastal: true,
      capacity: "MHP/matte -> nikkelsulfaat + precursor",
      note: "De Chinese chemie-hub die Indonesische MHP en matte omzet in nikkelsulfaat en kathode-precursor — waar de laterietroute alsnog in de batterij eindigt." },
    { id: "ni-ref-jinchuan", type: "refinery", name: "Jinchuan-raffinaderij", country: "China",
      lat: 38.62, lon: 102.35, tier: 3, operator: "Jinchuan Group",
      capacity: "elektrolytisch class-1",
      note: "Gansu; klassieke class-1-raffinage uit het eigen sulfide-erts — LME-leverbaar, maar klein naast de laterietstroom." },

    // --- De oude class-1-garde (Europa / Rusland / Canada / Japan / Korea) --
    { id: "ni-ref-harjavalta", type: "refinery", name: "Harjavalta", country: "Finland",
      lat: 61.31, lon: 22.14, tier: 2, operator: "Nornickel Harjavalta", coastal: true,
      capacity: "batterijnikkel + sulfaat",
      note: "Finland's enige nikkelraffinaderij; draait historisch op Nornickel-feed en levert de EU-batterijketen. Sinds 2022 een Russisch-verbonden gevoeligheid." },
    { id: "ni-ref-nikkelverk", type: "refinery", name: "Nikkelverk (Kristiansand)", country: "Noorwegen",
      lat: 58.15, lon: 8.00, tier: 2, operator: "Glencore", coastal: true,
      capacity: "hoogzuiver class-1 (99,9%)",
      note: "Een van de zuiverste nikkelraffinaderijen ter wereld; full-plate/briket -> direct LME-leverbaar. Draait op concentraat/matte uit Canada e.a." },
    { id: "ni-ref-sudbury", type: "refinery", name: "Sudbury-smelter/raffinage", country: "Canada",
      lat: 46.68, lon: -80.55, tier: 2, operator: "Vale / Glencore",
      capacity: "matte -> class-1",
      note: "De smelter/raffinage bij het Sudbury-bekken; verwerkt ook het Voisey's-Bay-concentraat tot class-1 voor de Noord-Amerikaanse legeringsmarkt." },
    { id: "ni-ref-kola", type: "refinery", name: "Kola (Monchegorsk)", country: "Rusland",
      lat: 67.94, lon: 32.96, tier: 3, operator: "Nornickel", coastal: true,
      capacity: "class-1 uit Norilsk-matte",
      note: "Het Kola-schiereiland raffineert de Norilsk-matte tot class-1. Sinds de sancties verschuift de afzet van de EU naar China en de binnenlandse markt." },
    { id: "ni-terrafame", type: "refinery", name: "Terrafame (Sotkamo)", country: "Finland",
      lat: 64.10, lon: 28.30, tier: 3, operator: "Terrafame (staat)",
      capacity: "geïntegreerd mijn+sulfaat",
      note: "Oost-Finland; bioloog-heap-leaching met een eigen nikkelsulfaatfabriek — een van de weinige geïntegreerde batterijnikkel-bronnen in de EU." },
    { id: "ni-ref-sumitomo", type: "refinery", name: "Sumitomo Niihama", country: "Japan",
      lat: 33.96, lon: 133.28, tier: 2, operator: "Sumitomo Metal Mining", coastal: true,
      capacity: "class-1 + nikkelsulfaat",
      note: "Shikoku; raffineert de matte/MHP uit Coral Bay (Filipijnen) en Sorowako tot class-1 en sulfaat voor de Japanse batterij-industrie (Panasonic). Over land via de Seto-brug naar Honshu." },
    { id: "ni-ref-korea", type: "refinery", name: "Korea (Gwangyang)", country: "Zuid-Korea",
      lat: 34.90, lon: 127.75, tier: 2, operator: "POSCO / LG", coastal: true,
      capacity: "MHP/matte -> sulfaat + precursor",
      note: "Zuid-Korea's poort voor batterijnikkel: Indonesische MHP/matte -> nikkelsulfaat en kathode-precursor voor LG/SK/Samsung. NIET LME-leverbaar (sulfaat)." },

    // ================================================================ HAVENS
    { id: "ni-port-malili", type: "port", name: "Malili", country: "Indonesië",
      lat: -2.64, lon: 121.06, tier: 3,
      note: "De kusthaven onder Sorowako; hier gaat de Vale-matte per schip naar Japan." },
    { id: "ni-port-esperance", type: "port", name: "Esperance", country: "Australië",
      lat: -33.86, lon: 121.89, tier: 3,
      note: "De nikkel-uitvoerhaven van West-Australië — recht ten zuiden van Murrin Murrin/Kalgoorlie." },
    { id: "ni-port-vitoria", type: "port", name: "Vitória", country: "Brazilië",
      lat: -20.32, lon: -40.30, tier: 3,
      note: "Atlantische uitgang voor het Braziliaanse ferronikkel richting Europa." },
    { id: "ni-port-toamasina", type: "port", name: "Toamasina", country: "Madagaskar",
      lat: -18.15, lon: 49.40, tier: 3,
      note: "De oostkusthaven aan het eind van de Ambatovy-pijpleiding; class-1 de Indische Oceaan op." },

    // ================================================================ MARKT
    // Roestvrij staal ≈ ⅔ van de vraag (class-2), batterij = snelst groeiend
    // (class-1). Afzetmarkten pál aan zee (coastal) zodat de schepen aanmeren.
    { id: "ni-mkt-stainless-china", type: "market", name: "China (roestvrij)", country: "China",
      lat: 22.55, lon: 114.10, tier: 1, coastal: true,
      note: "Veruit de grootste vraag: Tsingshan/Foshan-roestvrijstaal. Draait op Indonesische NPI én — het contrast — nog altijd op ruw Filipijns lateriet in Chinese smelters." },
    { id: "ni-mkt-battery-china", type: "market", name: "China (EV-batterij)", country: "China",
      lat: 30.10, lon: 122.10, tier: 1, coastal: true,
      note: "De Chinese kathode-industrie (CATL/BYD): nikkelsulfaat -> NMC-kathode -> EV. De snelst groeiende nikkelvraag." },
    { id: "ni-mkt-battery-korea", type: "market", name: "Korea (EV-batterij)", country: "Zuid-Korea",
      lat: 35.50, lon: 129.35, tier: 2, coastal: true,
      note: "LG/SK/Samsung-kathode; Korea leunt zwaar op Indonesische MHP via de eigen sulfaatraffinage." },
    { id: "ni-mkt-stainless-eu", type: "market", name: "EU (roestvrij)", country: "Nederland",
      lat: 51.40, lon: 3.60, tier: 2, coastal: true,
      note: "Europese roestvrij-industrie (Outokumpu/Aperam); deels bevoorraad door Braziliaans en Nieuw-Caledonisch ferronikkel." },
    { id: "ni-mkt-battery-eu", type: "market", name: "EU (EV-batterij)", country: "Duitsland",
      lat: 51.30, lon: 12.40, tier: 2,
      note: "De Europese kathode-/celindustrie (BASF, cellenfabrieken); bevoorraad door het schaarse EU-batterijnikkel (Finland/Noorwegen) — een strategische kwetsbaarheid." },
    { id: "ni-mkt-alloy-us", type: "market", name: "VS (superlegeringen)", country: "VS",
      lat: 40.00, lon: -82.00, tier: 3,
      note: "Hoogwaardige nikkel-superlegeringen voor lucht- en ruimtevaart (turbinebladen) — een kleine maar strategische, class-1-gedreven vraag." },
    { id: "ni-mkt-japan", type: "market", name: "Japan (roestvrij · legeringen)", country: "Japan",
      lat: 34.70, lon: 138.20, tier: 3, coastal: true,
      note: "Japanse roestvrij- en legeringsindustrie plus batterijnikkel (Panasonic), grotendeels op de eigen Sumitomo-raffinage." },

    // ============================================================= RECYCLING
    // Roestvrij-staalschroot ≈ ⅓ van de staalinput -> terug de mills in.
    // ALWAYS-ON (net als koper): stage `erts` (feedstock), géén `layer`.
    { id: "ni-rec-eu", type: "recycler", name: "Europa (roestvrij-schroot)", country: "Duitsland",
      lat: 51.20, lon: 6.50, tier: 3,
      note: "EU-roestvrijschroot terug naar de Europese mills — het grootste 'binnenlandse' nikkelaanbod van de EU." },
    { id: "ni-rec-china", type: "recycler", name: "China (roestvrij-schroot)", country: "China",
      lat: 30.50, lon: 120.60, tier: 3,
      note: "Chinees roestvrijschroot terug naar Foshan/Tsingshan — dempt een deel van de importbehoefte." },
    { id: "ni-rec-us", type: "recycler", name: "VS (schroot)", country: "VS",
      lat: 41.00, lon: -81.50, tier: 3,
      note: "Amerikaans nikkel-/roestvrijschroot terug naar de eigen legeringsketen." },

    // ============================ BEURSVOORRADEN (optionele toggle-laag)
    // type "exchange" -> alleen zichtbaar met de beursvoorraden-toggle (koper-
    // patroon, hergebruikt). `stock` (kt Ni) = magazijnvoorraad -> node-grootte.
    // NUANCE: alléén class-1 is LME-leverbaar; NPI/MHP/sulfaat NIET. De 2022-
    // squeeze (Tsingshan) liet zien hoe los deze prijs van de fysieke markt staat.
    { id: "ni-lme-rotterdam", type: "exchange", name: "LME Rotterdam", country: "Nederland",
      lat: 51.90, lon: 4.40, stock: 55, tier: 2, coastal: true, exchange: "LME",
      note: "Europees LME-nikkelmagazijn; historisch veel Russisch class-1 (briket/plaat)." },
    { id: "ni-lme-johor", type: "exchange", name: "LME Johor", country: "Maleisië",
      lat: 1.47, lon: 103.75, stock: 70, tier: 2, coastal: true, exchange: "LME",
      note: "Het grootste Aziatische LME-magazijn, bij Singapore/Malakka — de buffer tussen de class-1-bronnen en de Chinese vraag." },
    { id: "ni-lme-busan", type: "exchange", name: "LME Busan", country: "Zuid-Korea",
      lat: 35.10, lon: 129.04, stock: 30, tier: 3, coastal: true, exchange: "LME",
      note: "Koreaanse LME-locatie; opvangvat voor Aziatisch class-1." },
    { id: "ni-lme-baltimore", type: "exchange", name: "LME Baltimore", country: "VS",
      lat: 39.26, lon: -76.55, stock: 20, tier: 3, coastal: true, exchange: "LME",
      note: "Amerikaans LME-nikkelmagazijn aan de oostkust." },
  ],

  // ==========================================================================
  // STROMEN — value in kt Ni/jaar. stage bepaalt de kleur (erts dof, raffinaat
  // vol staal, product licht). `via` = echte route langs havens (ni-port-*) en
  // de universele knelpunten (wp-* uit data/_chokepoints.js).
  //
  //  A) Intra-Indonesië: mijn -> smelter (erts blijft in het land = de ban)
  //  B) Indonesië -> China roestvrij (NPI/slab) + batterij (MHP/matte->sulfaat)
  //  C) Filipijnen: RUW erts -> China (het contrast) + HPAL -> Japan
  //  D) Nieuw-Caledonië -> Azië (ferronikkel/class-1)
  //  E) De class-1-garde (Rusland/Canada/Europa/Japan)
  //  F) China/Australië/Brazilië/Madagaskar/Cuba -> markt
  //  G) Eindproduct: sulfaat -> kathode; NPI -> roestvrij
  //  H) Recycling -> mills (schroot terug, always-on)
  //  I) Beursvoorraden (layer:"exchange" -> alleen met de toggle)
  // ==========================================================================
  flows: [
    // === A. INTRA-INDONESIË — het erts blíjft in het land (de exportban) =====
    { from: "ni-morowali-mines", to: "ni-ref-imip", value: 300, mode: "road", stage: "erts",
      note: "Morowali-lateriet -> de IMIP-smelter ernaast. Vóór 2020 was dit ruw erts op een schip naar China; de exportban dwong de smelter aan land." },
    { from: "ni-morowali-mines", to: "ni-ref-qmb", value: 120, mode: "road", stage: "erts",
      note: "Deel van hetzelfde lateriet -> de HPAL-lijn (QMB/Huayou) voor batterij-MHP." },
    { from: "ni-weda-bay", to: "ni-ref-iwip", value: 340, mode: "road", stage: "erts",
      note: "Weda-Bay-lateriet -> de IWIP-smelter in het park; NPI én matte, ter plekke." },
    { from: "ni-obi", to: "ni-ref-obi", value: 130, mode: "road", stage: "erts",
      note: "Obi-lateriet -> Harita's eigen HPAL op het eiland." },
    { from: "ni-pomalaa", to: "ni-ref-pomalaa", value: 90, mode: "road", stage: "erts",
      note: "Pomalaa-lateriet -> de nieuwe Vale-Huayou-HPAL (project)." },
    { from: "ni-sorowako", to: "ni-port-malili", value: 70, mode: "road", stage: "raffinaat",
      note: "Vale smelt de matte op locatie; per truck naar de kusthaven Malili." },

    // === B. INDONESIË -> CHINA/KOREA (de twee waaiers) =======================
    { from: "ni-ref-imip", to: "ni-mkt-stainless-china", value: 300, mode: "ship", stage: "product",
      via: ["wp-makassar", "wp-scs"],
      note: "IMIP maakt roestvrij staal ter plekke -> de dikste stroom: door de Straat van Makassar en de Zuid-Chinese Zee naar de Chinese roestvrij-hub." },
    { from: "ni-ref-iwip", to: "ni-mkt-stainless-china", value: 220, mode: "ship", stage: "raffinaat",
      via: ["wp-scs"],
      note: "IWIP-NPI (Halmahera) -> China, via de Celebes-/Zuid-Chinese Zee." },
    { from: "ni-ref-qmb", to: "ni-ref-china-sulphate", value: 120, mode: "ship", stage: "raffinaat",
      via: ["wp-makassar", "wp-scs", "wp-taiwan"],
      note: "Morowali-MHP -> de Chinese sulfaatraffinage: de brug van lateriet naar batterijnikkel." },
    { from: "ni-ref-imip", to: "ni-ref-china-sulphate", value: 90, mode: "ship", stage: "raffinaat",
      via: ["wp-makassar", "wp-scs", "wp-taiwan"],
      note: "IMIP-HPAL-MHP -> Chinese sulfaatchemie." },
    { from: "ni-ref-iwip", to: "ni-ref-korea", value: 80, mode: "ship", stage: "raffinaat",
      via: ["wp-scs", "wp-taiwan"],
      note: "IWIP-matte -> de Koreaanse sulfaatraffinage (POSCO/LG)." },
    { from: "ni-ref-obi", to: "ni-ref-china-sulphate", value: 90, mode: "ship", stage: "raffinaat",
      via: ["wp-scs", "wp-taiwan"],
      note: "Obi-MHP -> Chinese sulfaatchemie." },
    { from: "ni-ref-obi", to: "ni-ref-korea", value: 50, mode: "ship", stage: "raffinaat",
      via: ["wp-scs", "wp-taiwan"],
      note: "Obi-MHP -> Korea." },
    { from: "ni-ref-pomalaa", to: "ni-ref-china-sulphate", value: 60, mode: "ship", stage: "raffinaat",
      via: ["wp-makassar", "wp-scs", "wp-taiwan"], status: "gepland",
      note: "Toekomstige Pomalaa-MHP -> China (project)." },

    // === C. FILIPIJNEN — het contrast: RUW erts -> China, HPAL -> Japan ======
    { from: "ni-philippines", to: "ni-mkt-stainless-china", value: 200, mode: "ship", stage: "erts",
      via: ["wp-scs"],
      note: "RUW Filipijns lateriet -> Chinese NPI-smelters. De Filipijnen kennen géén exportban — precies wat Indonesië in 2020 dichtdraaide. Donkere ertsboog naast de Indonesische raffinaat-bundel." },
    { from: "ni-coralbay", to: "ni-ref-sumitomo", value: 40, mode: "ship", stage: "raffinaat",
      via: ["wp-scs", "wp-taiwan"],
      note: "Coral Bay-HPAL (SMM) -> de Sumitomo-raffinaderij in Japan: de Filipijnse laterietbrug naar class-1." },

    // === D. NIEUW-CALEDONIË -> AZIË (in crisis) ==============================
    { from: "ni-doniambo", to: "ni-mkt-stainless-china", value: 60, mode: "ship", stage: "raffinaat",
      via: ["wp-pac-west", "wp-taiwan"],
      note: "SLN-ferronikkel -> China, over de westelijke Stille Oceaan. De marges zijn door de Indonesische NPI weggevaagd." },
    { from: "ni-goro", to: "ni-mkt-battery-korea", value: 45, mode: "ship", stage: "raffinaat",
      via: ["wp-pac-west", "wp-taiwan"],
      note: "Goro/Prony-class-1 -> de Koreaanse batterijketen." },

    // === E. DE CLASS-1-GARDE (Rusland / Canada / Europa / Japan) =============
    { from: "ni-norilsk", to: "ni-ref-kola", value: 150, mode: "rail", stage: "raffinaat",
      note: "Norilsk-matte -> de Kola-raffinaderij, binnen Rusland over land." },
    { from: "ni-ref-kola", to: "ni-mkt-battery-eu", value: 40, mode: "rail", stage: "product",
      note: "Russisch class-1 -> (historisch) de EU-batterij-/legeringsmarkt; sinds 2022 verschuift dit naar China en de binnenlandse markt." },
    { from: "ni-voiseys", to: "ni-ref-sudbury", value: 45, mode: "ship", stage: "erts",
      via: ["wp-cabot", "wp-st-laurent-1", "wp-st-laurent-2", "wp-st-laurent-2b", "wp-st-laurent-3", "wp-st-laurent-4"],
      note: "Voisey's-Bay-concentraat de Saint-Laurent op naar de Sudbury-smelter." },
    { from: "ni-sudbury", to: "ni-ref-sudbury", value: 90, mode: "road", stage: "erts",
      note: "Sudbury-erts -> de smelter/raffinage ernaast." },
    { from: "ni-ref-sudbury", to: "ni-mkt-alloy-us", value: 70, mode: "rail", stage: "product",
      note: "Canadees class-1 -> de Amerikaanse superlegeringsindustrie, over land." },
    { from: "ni-ref-nikkelverk", to: "ni-mkt-battery-eu", value: 60, mode: "ship", stage: "product",
      via: ["wp-deense-straten"],
      note: "Nikkelverk-hoogzuiver (Kristiansand) -> de EU-batterij-/legeringsmarkt, door de Deense Straten." },
    { from: "ni-ref-harjavalta", to: "ni-mkt-battery-eu", value: 55, mode: "ship", stage: "product",
      via: ["wp-deense-straten"],
      note: "Fins batterijnikkel (Harjavalta) -> de EU-batterijketen, uit de Botnische Golf door de Deense Straten." },
    { from: "ni-terrafame", to: "ni-mkt-battery-eu", value: 35, mode: "rail", stage: "product",
      note: "Terrafame-sulfaat (Sotkamo) -> de EU-batterijindustrie over land — een van de weinige EU-eigen batterijnikkelbronnen." },
    { from: "ni-ref-sumitomo", to: "ni-mkt-japan", value: 70, mode: "rail", stage: "product",
      note: "Sumitomo class-1/sulfaat -> de Japanse batterij-/legeringsmarkt, over de Seto-brug naar Honshu." },

    // === F. CHINA / AUSTRALIË / BRAZILIË / MADAGASKAR / CUBA -> MARKT =========
    { from: "ni-jinchuan-mine", to: "ni-ref-jinchuan", value: 60, mode: "road", stage: "erts",
      note: "Jinchuan-sulfide-erts -> de eigen raffinaderij (Gansu)." },
    { from: "ni-murrin", to: "ni-port-esperance", value: 40, mode: "rail", stage: "raffinaat",
      note: "Murrin-Murrin-class-1 per spoor naar Esperance." },
    { from: "ni-port-esperance", to: "ni-mkt-stainless-china", value: 40, mode: "ship", stage: "raffinaat",
      via: ["wp-lombok", "wp-makassar", "wp-scs"],
      note: "West-Australisch nikkel via Lombok en Makassar naar China." },
    { from: "ni-brazil", to: "ni-port-vitoria", value: 55, mode: "road", stage: "raffinaat",
      note: "Braziliaans ferronikkel per truck/spoor naar Vitória." },
    { from: "ni-port-vitoria", to: "ni-mkt-stainless-eu", value: 55, mode: "ship", stage: "raffinaat",
      note: "Vitória -> de Europese roestvrij-markt, recht de Atlantische Oceaan over." },
    { from: "ni-ambatovy", to: "ni-port-toamasina", value: 45, mode: "pipeline", stage: "raffinaat",
      note: "Ambatovy-slurry/class-1 per pijpleiding naar de kusthaven Toamasina." },
    { from: "ni-port-toamasina", to: "ni-mkt-battery-china", value: 45, mode: "ship", stage: "raffinaat",
      via: ["wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Madagaskar-class-1 de Indische Oceaan over, door Malakka naar de Chinese batterijketen." },
    { from: "ni-moa", to: "ni-mkt-stainless-china", value: 25, mode: "ship", stage: "erts",
      via: ["wp-panama", "wp-pac-west", "wp-taiwan"],
      note: "Cubaans gemengd sulfide via het Panamakanaal en de Stille Oceaan naar China." },

    // === G. EINDPRODUCT: sulfaat -> kathode; class-1 -> markt ================
    { from: "ni-ref-china-sulphate", to: "ni-mkt-battery-china", value: 260, mode: "road", stage: "product",
      note: "Nikkelsulfaat -> NMC-kathode -> de Chinese EV-industrie. Hier eindigt de Indonesische laterietroute alsnog in de batterij." },
    { from: "ni-ref-korea", to: "ni-mkt-battery-korea", value: 120, mode: "road", stage: "product",
      note: "Koreaans nikkelsulfaat/precursor -> LG/SK/Samsung-kathode." },
    { from: "ni-ref-jinchuan", to: "ni-mkt-battery-china", value: 45, mode: "rail", stage: "product",
      note: "Chinees class-1 (Jinchuan) -> de binnenlandse batterij-/legeringsvraag." },

    // === H. RECYCLING -> MILLS (schroot terug, always-on, stage erts) ========
    { from: "ni-rec-china", to: "ni-mkt-stainless-china", value: 150, mode: "road", stage: "erts",
      note: "Chinees roestvrijschroot terug naar de mills — nikkel dat niet opnieuw gewonnen hoeft te worden." },
    { from: "ni-rec-eu", to: "ni-mkt-stainless-eu", value: 90, mode: "road", stage: "erts",
      note: "EU-roestvrijschroot -> de Europese mills; het grootste 'binnenlandse' EU-nikkelaanbod." },
    { from: "ni-rec-us", to: "ni-mkt-alloy-us", value: 40, mode: "road", stage: "erts",
      note: "Amerikaans schroot terug de eigen legeringsketen in." },

    // === I. BEURSVOORRADEN (layer:"exchange" -> alleen met de toggle) ========
    // Alléén class-1 (Nikkelverk/Kola/Sudbury/Sumitomo) is LME-leverbaar.
    { from: "ni-ref-nikkelverk", to: "ni-lme-rotterdam", value: 25, mode: "ship", stage: "raffinaat", layer: "exchange",
      note: "Noors hoogzuiver class-1 -> LME Rotterdam (full-plate/briket, leverbaar)." },
    { from: "ni-ref-kola", to: "ni-lme-rotterdam", value: 30, mode: "rail", stage: "raffinaat", layer: "exchange",
      note: "Russisch class-1 -> LME Rotterdam; historisch een groot deel van de LME-nikkelvoorraad." },
    { from: "ni-ref-sudbury", to: "ni-lme-baltimore", value: 15, mode: "rail", stage: "raffinaat", layer: "exchange",
      note: "Canadees class-1 -> het Amerikaanse LME-magazijn." },
    { from: "ni-ref-sumitomo", to: "ni-lme-busan", value: 12, mode: "ship", stage: "raffinaat", layer: "exchange",
      note: "Japans class-1 -> LME Busan." },
    { from: "ni-lme-johor", to: "ni-mkt-stainless-china", value: 30, mode: "ship", stage: "raffinaat", layer: "exchange",
      via: ["wp-singapore", "wp-scs"],
      note: "Buffer stroomt door naar de vraag: LME Johor -> China. Maar let op: dit is class-1, terwijl China's roestvrij vooral op NPI draait — de LME-prijs is niet de fysieke markt." },
  ],

  // ==========================================================================
  // SPANNINGEN — waar de nikkelketen knijpt. Verwijst naar de universele
  // knelpuntenlijst (wp-*). flows-verwijzing: "from-id>to-id".
  // ==========================================================================
  tensions: [
    { id: "ni-t-indonesia", type: "concentratie", title: "Indonesië: mijn én raffinage in tien jaar",
      lat: -2.5, lon: 122.5,
      nodes: ["ni-morowali-mines", "ni-weda-bay", "ni-ref-imip", "ni-ref-iwip", "ni-ref-qmb", "ni-ref-obi"],
      flows: ["ni-morowali-mines>ni-ref-imip", "ni-weda-bay>ni-ref-iwip",
              "ni-ref-imip>ni-mkt-stainless-china", "ni-ref-qmb>ni-ref-china-sulphate"],
      metric: "Indonesië ≈ 55–60% mijnbouw én de nieuwe raffinage-hub — na de exportban (2020)",
      note: "De nikkel-'aha'. Anders dan bij koper of lithium, waar de wereld breed graaft en China raffineert, heeft Indonesië álles naar zich toe getrokken. De exportban op ruw erts dwong de smelters aan land: het lateriet blíjft in Sulawesi/Halmahera (korte hops mijn->smelter) en gaat pas als NPI, matte of MHP de zee op. Op de kaart een dichte kluwen binnen Indonesië, niet een ertsstroom die vertrekt." },

    { id: "ni-t-class", type: "structureel", title: "Twee nikkels: class-1 (batterij) vs. class-2 (roestvrij)",
      lat: 6.0, lon: 125.0,
      nodes: ["ni-ref-imip", "ni-ref-qmb", "ni-ref-china-sulphate", "ni-mkt-stainless-china", "ni-mkt-battery-china"],
      flows: ["ni-ref-imip>ni-mkt-stainless-china", "ni-ref-qmb>ni-ref-china-sulphate",
              "ni-ref-china-sulphate>ni-mkt-battery-china"],
      metric: "roestvrij ≈ ⅔ van de vraag (class-2/NPI) · batterij = class-1/sulfaat",
      note: "Nikkel is geen één markt maar twee. Class-2 (NPI/ferronikkel, direct uit lateriet via RKEF) gaat naar roestvrij staal — nog altijd tweederde van de vraag. Class-1 (≥99,8%, nikkelsulfaat/kathode) gaat naar EV-batterijen. HPAL (-> MHP) en matte zijn de dure bruggen die goedkoop Indonesisch lateriet tóch batterijwaardig maken — de reden dat de batterijstroom nu óók door Indonesië loopt." },

    { id: "ni-t-china-capital", type: "beleid", title: "Chinees kapitaal, Indonesische grond",
      lat: -1.0, lon: 124.0,
      nodes: ["ni-ref-imip", "ni-ref-qmb", "ni-ref-china-sulphate", "ni-mkt-battery-china"],
      flows: ["ni-ref-qmb>ni-ref-china-sulphate", "ni-ref-imip>ni-ref-china-sulphate",
              "ni-ref-china-sulphate>ni-mkt-battery-china"],
      metric: "Tsingshan/Huayou/CATL bezitten de parken (IMIP/IWIP) én de batterijchemie",
      note: "De geografie is Indonesisch, de waardeketen Chinees. Tsingshan, Huayou, GEM en CATL financierden en bezitten de industrieparken (IMIP/IWIP), en de MHP/matte vaart door naar de Chinese sulfaatraffinage voordat hij als kathode in een batterij belandt. Indonesië heeft de mijn en de smelter; China houdt de chemie en de markt. Onshoring is niet hetzelfde als eigenaarschap." },

    { id: "ni-t-shakeout", type: "beleid", title: "De prijscrash: Indonesië verdringt de rest",
      lat: -29.0, lon: 122.0,
      nodes: ["ni-nickelwest", "ni-murrin", "ni-doniambo", "ni-goro"],
      flows: ["ni-doniambo>ni-mkt-stainless-china", "ni-goro>ni-mkt-battery-korea"],
      metric: "BHP Nickel West stilgelegd (2024) · Nieuw-Caledonië in structurele crisis",
      note: "De keerzijde van de Indonesische overvloed: die crashte de nikkelprijs en maakte hoge-kosten-mijnen verliesgevend. BHP legde Nickel West eind 2024 stil, Nieuw-Caledonië (SLN) overleeft op staatssteun, en tal van Australische mijnen gingen op onderhoud. Geen conjunctuurdip maar een structurele shakeout: de wereld-class-1-kaart dunt zichtbaar uit terwijl de Indonesische massa groeit." },

    { id: "ni-t-straten", type: "knelpunt", title: "De Indonesische straten: Makassar & Lombok",
      lat: -3.5, lon: 118.0,
      nodes: ["wp-makassar", "wp-lombok", "wp-scs", "wp-taiwan", "ni-ref-imip", "ni-ref-iwip"],
      flows: ["ni-ref-imip>ni-mkt-stainless-china", "ni-ref-qmb>ni-ref-china-sulphate",
              "ni-port-esperance>ni-mkt-stainless-china"],
      metric: "vrijwel alle Indonesische nikkelexport knijpt door Makassar/Lombok -> SCS -> Taiwan",
      note: "Omdat de raffinage nu in Indonesië zit, verschuift het knelpunt mee: niet een Chinese haven maar de Indonesische straten. NPI, matte en MHP uit Sulawesi en Halmahera bundelen zich door de Straat van Makassar (en Lombok voor de Australische bulk), de Zuid-Chinese Zee en de Straat van Taiwan naar de Oost-Aziatische vraag. Eén verstoring daar raakt zowel de roestvrij- als de batterijketen." },

    { id: "ni-t-lme", type: "beleid", title: "LME-nikkel: alleen class-1 telt + de 2022-squeeze",
      lat: 1.47, lon: 103.75,
      nodes: ["ni-lme-johor", "ni-lme-rotterdam", "ni-lme-busan", "ni-lme-baltimore"],
      flows: ["ni-ref-nikkelverk>ni-lme-rotterdam", "ni-ref-kola>ni-lme-rotterdam",
              "ni-ref-sudbury>ni-lme-baltimore", "ni-lme-johor>ni-mkt-stainless-china"],
      metric: "class-1-only leverbaar · maart 2022: ~$100k/t, LME schortte de handel op en annuleerde trades",
      note: "Zet de beursvoorraden-laag aan. Cruciale nuance: alléén class-1 (briket/plaat/kathode) is LME-leverbaar — NPI, MHP en sulfaat níet. Daardoor vertegenwoordigt de LME-nikkelprijs niet de echte, laterietgedreven markt. In maart 2022 explodeerde die kloof: een enorme short van Tsingshan (dat juist NPI produceert, geen leverbaar class-1) joeg de prijs naar ~$100.000/t, waarna de LME de handel opschortte en trades annuleerde — een van de grootste beurscrises in de metaalhandel." },
  ],
});
