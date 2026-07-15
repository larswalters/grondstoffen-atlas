// ============================================================================
// DIAMANT (C) — volledig uitgewerkte module. Peiljaar ±2023-2024.
// Cijfers indicatief/afgerond, o.b.v. Kimberley Process (KPCS) ruwstatistiek,
// USGS MCS 2025 (Diamond, industrial & gem), De Beers/Alrosa/Debswana-rapportages,
// AWDC (Antwerpen) en GJEPC (India/Surat). Eenheid overal: Mct/jaar (miljoen
// karaat RUW), zodat de keten optelbaar blijft. Wereld-ruwproductie ≈ 110-120 Mct.
// Zie design/diamant.md.
//
// DE VORM VAN DIAMANT (de scherpste DOWNSTREAM-trechter van de atlas):
//   - De WINNING is verspreid: Rusland/Alrosa (#1 op VOLUME, Jakoetië), Botswana/
//     Debswana (Jwaneng = #1 op WAARDE + Orapa), Canada, Angola, Zuid-Afrika,
//     Zimbabwe, Namibië (marien, hoogste waarde/karaat), Lesotho. Let op de
//     VOLUME-vs-WAARDE-splitsing: DRC/Zimbabwe zijn volumineus maar grotendeels
//     industrieel/laagwaardig; Botswana/Namibië/Lesotho klein maar duur.
//   - Het SLIJPEN & POLIJSTEN knijpt samen in ÉÉN Indiase stad: SURAT (Gujarat),
//     ~90-95% van alle stenen (~1 mln slijpers). Scherper nog dan de China-
//     raffinage (lithium/koper) of Ganzhou-scheiding (REE). Alle rough-arcs
//     convergeren op Surat — dat ÍS het aha.
//   - Een INSTITUTIONEEL knelpunt: ANTWERPEN. Ooit de handelshoofdstad, nu het
//     verplichte G7-CERTIFICERINGSKNOOPPUNT tegen Russische (Alrosa) diamant
//     (sanctie maart 2024). Gemodelleerd als de fysieke omweg mijn->Antwerpen->
//     Surat, terwijl de Russische rough zichtbaar OM Antwerpen heen buigt via
//     Dubai / direct India.
//   - Onderliggend: het DE BEERS + ALROSA-DUOPOLIE (kartel-verleden, single-
//     channel ~80-90%, "A Diamond is Forever"; De Beers-sights nu via Gaborone) en
//     de LAB-GROWN-ONTWRICHTING (China/Henan HPHT + India CVD ondergraven vooral
//     de VS-verlovingsring-markt) — die laatste zit in v1 alleen als `tension`
//     (de optionele lab-grown-toggle is een aparte, uitgestelde issue: LAR-471).
//
// STAGES (via `stage`):
//   erts       = ruwe diamant (rough): mijn -> sorteer-/handelshub -> slijperij.
//                Dof/donker.
//   raffinaat  = geslepen & gepolijste diamant (Surat): de trechter. Volle ijsblauw.
//   product    = sieraad / retail (VS #1 / China / Golf / EU / India). Licht.
//
// TRANSPORT is LUCHTVRACHT (hergebruik goud/PGM air-mode: `mode:"air"` = great-
// circle-boog, buiten de A* om) — beveiligde koeriers (Brink's/Malca-Amit/Ferrari
// Group). Alleen korte hops binnen een land (mijn->Gaborone, Surat->Mumbai, hub->
// lokale markt) zijn `road`. GEEN nieuwe render-modus, GEEN nieuw chokepoint (net
// als PGM), GEEN nieuwe marker-types (`hub`/`refinery`/`mine`/`market` bestaan al;
// de ruit-marker van `refinery` past treffend bij de slijperij). De tijdlijn toont
// automatisch "vluchten" (activeHasAir()).
// ============================================================================

REGISTER({
  id: "diamond",
  name: "Diamant",
  symbol: "C",
  color: "#9FD9EF",       // ijsblauw-wit: de mijn-markers (diamant-schittering)
  flowColor: "#CDEEFB",   // lichter ijsblauw: de stromen tegen de donkere bol
  detail: "uitgewerkt",
  unit: "Mct/jaar (ruw, indicatief)",
  blurb: "De winning is verspreid (Rusland #1 op volume, Botswana #1 op waarde, " +
    "Canada, Angola, zuidelijk Afrika), maar het slijpen en polijsten knijpt samen " +
    "in één Indiase stad: Surat (~90-95% van alle stenen) — de scherpste downstream-" +
    "trechter van de atlas. De handel loopt via Antwerpen (nu ook het verplichte " +
    "G7-certificeringsknooppunt tegen Russische diamant) en Dubai. Alles vliegt " +
    "(beveiligde koeriers). Onderliggend: het De Beers/Alrosa-duopolie en de opkomst " +
    "van goedkope lab-grown diamant uit China en India.",

  nodes: [
    // =============================================================== MIJNEN
    // De spreiding + de volume-vs-waarde-splitsing is de opmaat naar de trechter.
    // `share` = % van ~115 Mct wereld op VOLUME; de `note` verraadt telkens het
    // waarde-karakter (edelsteen vs. industrieel).
    { id: "dia-alrosa", type: "mine", name: "Alrosa (Mir/Udachny, Jakoetië)", country: "Rusland",
      lat: 62.53, lon: 113.96, share: 30, tier: 1, operator: "Alrosa",
      status: "actief", capacity: "≈ 35 Mct/j",
      note: "#1 op VOLUME (~30% wereld). Diepe kimberliet-pijpen in Oost-Siberië. Sinds maart 2024 onder G7-sanctie — de afzet herrouteert naar Dubai en direct naar India (om Antwerpen/de G7-markt heen)." },
    { id: "dia-jwaneng", type: "mine", name: "Jwaneng", country: "Botswana",
      lat: -24.60, lon: 24.73, share: 11, tier: 1, operator: "Debswana (De Beers/Botswana 50/50)",
      status: "actief", capacity: "≈ 12 Mct/j",
      note: "De rijkste diamantmijn ter wereld op WAARDE — edelsteen-kwaliteit. Ruw per truck naar de De Beers-aggregatie in Gaborone." },
    { id: "dia-orapa", type: "mine", name: "Orapa", country: "Botswana",
      lat: -21.31, lon: 25.37, share: 10, tier: 1, operator: "Debswana",
      status: "actief", capacity: "≈ 11 Mct/j",
      note: "De grootste Botswaanse mijn op volume (edelsteen + near-gem). Samen met Jwaneng maakt Debswana Botswana tot de #1-waardeproducent ter wereld." },
    { id: "dia-canada", type: "mine", name: "Canada (Diavik/Ekati/Gahcho Kué, NWT)", country: "Canada",
      lat: 64.50, lon: -110.28, share: 14, tier: 1, operator: "Rio Tinto / Burgundy / De Beers",
      status: "actief", capacity: "≈ 16 Mct/j",
      note: "Subarctische kimberliet-clusters (Northwest Territories). Hoogwaardig edelsteen met een 'conflictvrij'-premium; ruw vliegt naar Antwerpen voor certificering + handel." },
    { id: "dia-catoca", type: "mine", name: "Catoca (Lucapa)", country: "Angola",
      lat: -9.42, lon: 20.30, share: 8, tier: 1, operator: "Endiama / Alrosa JV",
      status: "actief", capacity: "≈ 9 Mct/j",
      note: "De grootste Afrikaanse kimberliet-mijn (mix edelsteen/industrieel). Deels Alrosa-belang; ruw naar Antwerpse en Dubai-tenders." },
    { id: "dia-drc", type: "mine", name: "Mbuji-Mayi (MIBA + artisanaal)", country: "DR Congo",
      lat: -6.13, lon: 23.60, share: 8, tier: 2, operator: "MIBA / artisanaal",
      status: "actief", capacity: "≈ 9 Mct/j",
      note: "Volumineus maar GROTENDEELS INDUSTRIEEL/LAAGWAARDIG (alluviaal). Illustreert de volume-vs-waarde-kloof: veel karaat, weinig waarde per karaat." },
    { id: "dia-venetia", type: "mine", name: "Venetia", country: "Zuid-Afrika",
      lat: -22.44, lon: 29.33, share: 5, tier: 2, operator: "De Beers",
      status: "actief", capacity: "≈ 5 Mct/j",
      note: "De grootste Zuid-Afrikaanse mijn (nu overgegaan naar ondergronds). Edelsteen; ruw over de grens naar de De Beers-aggregatie in Gaborone." },
    { id: "dia-marange", type: "mine", name: "Marange (alluviaal)", country: "Zimbabwe",
      lat: -18.92, lon: 32.55, share: 4, tier: 2, operator: "ZCDC",
      status: "actief", capacity: "≈ 5 Mct/j",
      note: "Volumineus, laagwaardig — en beladen (het geweld van 2008, mensenrechten). Ruw via Dubai-/Antwerpse tenders." },
    { id: "dia-namibia", type: "mine", name: "Namdeb / Debmarine (Oranjemund)", country: "Namibië",
      lat: -28.55, lon: 16.45, share: 2, tier: 2, operator: "De Beers/Namibië JV", coastal: true,
      status: "actief", capacity: "≈ 2 Mct/j",
      note: "MARIENE winning — schepen baggeren diamant van de zeebodem voor de kust. Klein op volume, maar de HOOGSTE WAARDE/KARAAT ter wereld." },
    { id: "dia-letseng", type: "mine", name: "Letšeng", country: "Lesotho",
      lat: -29.02, lon: 28.87, share: 1, tier: 3, operator: "Gem Diamonds",
      status: "actief", capacity: "≈ 1 Mct/j",
      note: "De hoogst gelegen diamantmijn, met de hoogste gemiddelde $/karaat — beroemd om uitzonderlijk grote stenen. Naar Antwerpse veilingen." },
    { id: "dia-argyle", type: "mine", name: "Argyle (GESLOTEN 2020)", country: "Australië",
      lat: -16.70, lon: 128.40, share: 0.5, tier: 3, operator: "Rio Tinto (ex)",
      status: "gesloten", capacity: "gesloten sinds 2020",
      note: "Leverde ooit ~90% van de wereld-ROZE diamant. De sluiting in 2020 maakte roze diamant abrupt schaars — het schaarste-verhaal van de atlas. Geen actieve stromen meer." },

    // ==================================== SORTEER-/HANDELSHUBS (`type: hub`)
    // Rough sorteren/verkopen/certificeren (Gaborone/Antwerpen/Dubai) en polished
    // verhandelen (Mumbai/Ramat Gan/New York). Antwerpen = sinds 2024 het G7-
    // certificeringsknooppunt -> de niet-Russische rough gaat er fysiek doorheen.
    { id: "dia-gaborone", type: "hub", name: "Gaborone (De Beers DBGSS / sights)", country: "Botswana",
      lat: -24.65, lon: 25.91, tier: 1,
      note: "De Beers verplaatste de aggregatie én de 'sights'-verkoop van Londen hierheen (2013, beneficiation-deal met Botswana). Sightholders kopen hier de rough en sturen die naar de slijperij." },
    { id: "dia-antwerp", type: "hub", name: "Antwerpen (AWDC)", country: "België",
      lat: 51.22, lon: 4.42, tier: 1,
      note: "De historische handelshoofdstad, en sinds maart 2024 het VERPLICHTE G7-CERTIFICERINGSKNOOPPUNT: niet-Russische rough moet hier worden gecertificeerd om de G7-markt te bereiken. De poort naar Surat." },
    { id: "dia-dubai", type: "hub", name: "Dubai (DMCC / Almas Tower)", country: "VAE",
      lat: 25.09, lon: 55.14, tier: 1,
      note: "De snelst groeiende rough-hub, belastingvrij. Sinds de sanctie ook het herrouterings-luik voor Russische (Alrosa) stenen die de G7-markt niet meer in mogen." },
    { id: "dia-mumbai", type: "hub", name: "Mumbai (Bharat Diamond Bourse)", country: "India",
      lat: 19.07, lon: 72.87, tier: 1,
      note: "'s Werelds grootste diamantbeurs (Bandra Kurla). Het polished-handels-, financierings- en exportcentrum van India — waar de Surat-stenen de wereld in gaan." },
    { id: "dia-ramat-gan", type: "hub", name: "Ramat Gan (Israel Diamond Exchange)", country: "Israël",
      lat: 32.08, lon: 34.81, tier: 3,
      note: "Handel + slijperij voor high-end grote stenen, plus financiering — een dun maar hoogwaardig draadje naast de Indiase volumestroom." },
    { id: "dia-ny", type: "hub", name: "New York (47th Street)", country: "VS",
      lat: 40.76, lon: -73.98, tier: 3,
      note: "De Diamond District in Manhattan: topsegment-handel en zeer grote stenen, pal naast de grootste eindmarkt (VS)." },

    // ==================================================== SLIJPERIJ (`refinery`)
    // Waar rough polished wordt. Surat = de trechter; China = klein.
    { id: "dia-surat", type: "refinery", name: "Surat (slijperij)", country: "India",
      lat: 21.17, lon: 72.83, tier: 1, operator: "Gujaraatse slijp-industrie",
      capacity: "~90-95% van de wereld-slijp/polijst",
      note: "DE TRECHTER van diamant: ~90-95% van alle diamant ter wereld wordt hier geslepen en gepolijst, door ~1 miljoen slijpers. Alle rough-arcs — van Gaborone, Antwerpen en Dubai — komen hier samen. Polished per truck naar de beurs in Mumbai." },
    { id: "dia-china-cut", type: "refinery", name: "Guangzhou/Shenzhen (slijperij)", country: "China",
      lat: 23.13, lon: 113.26, tier: 2, operator: "div.",
      capacity: "secundair",
      note: "De secundaire slijperij, vooral voor de eigen Chinese markt en een deel van de grotere stenen. Klein naast Surat." },

    // ================================================================ MARKT
    // Sieradenvraag. VS veruit #1 (~50%); China #2 (teruggevallen); India groeit.
    { id: "dia-mkt-us", type: "market", name: "VS — sieraden (verlovingsring)", country: "VS",
      lat: 40.00, lon: -83.00, tier: 1,
      note: "De grootste eindmarkt: ~50% van de wereldvraag naar polished. Ook het front van de lab-grown-ontwrichting — kweekdiamant verovert vooral hier het verlovingsring-segment." },
    { id: "dia-mkt-china", type: "market", name: "China / Hongkong — sieraden", country: "China",
      lat: 22.32, lon: 114.17, tier: 1,
      note: "De #2-markt. Sinds ~2022 teruggevallen (vastgoedcrisis + zwak consumentenvertrouwen), maar structureel groot." },
    { id: "dia-mkt-india", type: "market", name: "India — sieraden (binnenlands)", country: "India",
      lat: 28.61, lon: 77.21, tier: 2,
      note: "De snelgroeiende eigen vraag (Delhi/Mumbai) naast de exportslijperij — India wordt zowel de werkbank áls een grote eindmarkt." },
    { id: "dia-mkt-gulf", type: "market", name: "Golf — retail + re-export", country: "VAE",
      lat: 24.47, lon: 54.37, tier: 2,
      note: "Dubai/Abu Dhabi retail plus toeristische doorverkoop — de Golf als koopjes- en luxewinkelbestemming." },
    { id: "dia-mkt-eu", type: "market", name: "EU — luxe (Parijs/Genève)", country: "Frankrijk",
      lat: 48.85, lon: 2.35, tier: 2,
      note: "De Europese luxemerken (LVMH/Richemont); high-end sieraden en horloges." },
    { id: "dia-mkt-japan", type: "market", name: "Japan — sieraden", country: "Japan",
      lat: 35.68, lon: 139.76, tier: 3,
      note: "Een stabiele, koopkrachtige high-end markt." },
  ],

  // ==========================================================================
  // STROMEN — value in Mct/jaar (ruw-equivalent). stage bepaalt de kleur (erts dof,
  // raffinaat vol ijsblauw, product licht). Alles per LUCHT (mode "air": great-
  // circle, hergebruik goud/PGM) behalve korte hops binnen een land (`road`).
  // GEEN `via` nodig voor de air-arcs; de Antwerpen-certificering is gemodelleerd
  // als de fysieke twee-legs-omweg mijn->Antwerpen->Surat.
  //
  //  A) Mijn -> sorteer-/handelshub (rough, erts)
  //  B) Handelshub -> slijperij (rough, erts) — de convergentie op Surat
  //  C) Slijperij -> polished-handel (raffinaat)
  //  D) Polished-hub -> eindmarkt (product) — de sieradenvraag
  // ==========================================================================
  flows: [
    // === A. MIJN -> SORTEER-/HANDELSHUB (stage erts) ========================
    { from: "dia-jwaneng", to: "dia-gaborone", value: 12, mode: "road", stage: "erts",
      note: "Debswana-rough (Jwaneng) -> de De Beers-aggregatie in Gaborone, binnen Botswana over land." },
    { from: "dia-orapa", to: "dia-gaborone", value: 11, mode: "road", stage: "erts",
      note: "Orapa-rough -> Gaborone-aggregatie." },
    { from: "dia-venetia", to: "dia-gaborone", value: 5, mode: "road", stage: "erts",
      note: "Zuid-Afrikaanse De Beers-rough (Venetia) -> de Gaborone-aggregatie over de grens." },
    { from: "dia-namibia", to: "dia-gaborone", value: 2, mode: "air", stage: "erts",
      note: "Mariene Namibische rough -> de De Beers-aggregatie (hoogste waarde/karaat)." },
    { from: "dia-alrosa", to: "dia-dubai", value: 20, mode: "air", stage: "erts",
      note: "Russische rough herrouteert naar DUBAI — om de G7-sanctie/Antwerpen heen (sinds maart 2024)." },
    { from: "dia-alrosa", to: "dia-surat", value: 12, mode: "air", stage: "erts",
      note: "Russische rough DIRECT naar India: Surat slijpt óók niet-G7-goederen — de sanctie stuurt de stroom om, niet weg." },
    { from: "dia-catoca", to: "dia-antwerp", value: 5, mode: "air", stage: "erts",
      note: "Angolese rough -> Antwerpse tenders (certificering + handel)." },
    { from: "dia-catoca", to: "dia-dubai", value: 4, mode: "air", stage: "erts",
      note: "Angolese rough -> Dubai-tenders." },
    { from: "dia-canada", to: "dia-antwerp", value: 16, mode: "air", stage: "erts",
      note: "Canadese rough -> Antwerpen: certificering ('conflictvrij') + handel, dan door naar Surat." },
    { from: "dia-drc", to: "dia-antwerp", value: 5, mode: "air", stage: "erts",
      note: "Congolese rough (deels edelsteen) -> Antwerpen." },
    { from: "dia-drc", to: "dia-surat", value: 4, mode: "air", stage: "erts",
      note: "Congolese industriële/laagwaardige rough -> direct naar de Indiase slijperij." },
    { from: "dia-marange", to: "dia-dubai", value: 5, mode: "air", stage: "erts",
      note: "Zimbabwaanse rough via Dubai-/Antwerpse tenders." },
    { from: "dia-letseng", to: "dia-antwerp", value: 1, mode: "air", stage: "erts",
      note: "Lesothaanse grote stenen -> Antwerpse veilingen." },

    // === B. HANDELSHUB -> SLIJPERIJ (stage erts) — DE CONVERGENTIE OP SURAT ==
    { from: "dia-gaborone", to: "dia-surat", value: 26, mode: "air", stage: "erts",
      note: "De Beers-sightholders sturen de rough naar India — een van de dikste trechter-arcs naar Surat." },
    { from: "dia-antwerp", to: "dia-surat", value: 28, mode: "air", stage: "erts",
      note: "Antwerpen (gecertificeerd) -> Surat: het gros van de wereld-rough gaat via Antwerpen naar de Indiase slijperij." },
    { from: "dia-dubai", to: "dia-surat", value: 24, mode: "air", stage: "erts",
      note: "Dubai-rough -> Surat, inclusief de herrouteerde Russische stenen." },
    { from: "dia-gaborone", to: "dia-antwerp", value: 6, mode: "air", stage: "erts",
      note: "Een deel van de De Beers-rough -> de Antwerpse handel." },
    { from: "dia-antwerp", to: "dia-china-cut", value: 4, mode: "air", stage: "erts",
      note: "Klein deel van de Antwerpse rough -> de Chinese slijperij." },
    { from: "dia-dubai", to: "dia-china-cut", value: 3, mode: "air", stage: "erts",
      note: "Dubai-rough -> de Chinese slijperij." },
    { from: "dia-antwerp", to: "dia-ramat-gan", value: 2, mode: "air", stage: "erts",
      note: "High-end grote stenen -> de Israëlische slijperij (dun draadje)." },

    // === C. SLIJPERIJ -> POLISHED-HANDEL (stage raffinaat) ===================
    { from: "dia-surat", to: "dia-mumbai", value: 40, mode: "road", stage: "raffinaat",
      note: "Surat -> de Bharat Diamond Bourse in Mumbai: het geslepen product naar de handel/export, binnen India over land. De dikste raffinaat-boog." },
    { from: "dia-china-cut", to: "dia-mkt-china", value: 7, mode: "road", stage: "raffinaat",
      note: "Chinese slijperij -> de eigen markt (een binnenlandse lus)." },
    { from: "dia-mumbai", to: "dia-antwerp", value: 8, mode: "air", stage: "raffinaat",
      note: "Polished terug naar de Antwerpse handel voor wereldwijde herverkoop." },
    { from: "dia-mumbai", to: "dia-dubai", value: 6, mode: "air", stage: "raffinaat",
      note: "Polished naar Dubai (handel + re-export)." },
    { from: "dia-ramat-gan", to: "dia-ny", value: 2, mode: "air", stage: "raffinaat",
      note: "Israëlische high-end polished -> het New York-topsegment." },

    // === D. POLISHED-HUB -> EINDMARKT (stage product) — de sieradenvraag =====
    { from: "dia-mumbai", to: "dia-mkt-us", value: 18, mode: "air", stage: "product",
      note: "India -> VS: de grootste eindstroom (~50% van de wereldvraag)." },
    { from: "dia-mumbai", to: "dia-mkt-china", value: 8, mode: "air", stage: "product",
      note: "India -> China/Hongkong." },
    { from: "dia-mumbai", to: "dia-mkt-india", value: 5, mode: "road", stage: "product",
      note: "India -> de eigen binnenlandse markt, over land." },
    { from: "dia-mumbai", to: "dia-mkt-eu", value: 5, mode: "air", stage: "product",
      note: "India -> de Europese luxe." },
    { from: "dia-mumbai", to: "dia-mkt-gulf", value: 3, mode: "air", stage: "product",
      note: "India -> de Golf-retail." },
    { from: "dia-mumbai", to: "dia-mkt-japan", value: 2, mode: "air", stage: "product",
      note: "India -> Japan." },
    { from: "dia-antwerp", to: "dia-mkt-eu", value: 3, mode: "road", stage: "product",
      note: "Antwerpse polished -> de Europese luxe, over land." },
    { from: "dia-antwerp", to: "dia-mkt-us", value: 4, mode: "air", stage: "product",
      note: "Antwerpse high-end polished -> de VS." },
    { from: "dia-dubai", to: "dia-mkt-gulf", value: 3, mode: "air", stage: "product",
      note: "Dubai polished -> de bredere Golf-retail (beveiligde koerier; diamant vliegt, ook regionaal)." },
    { from: "dia-ny", to: "dia-mkt-us", value: 2, mode: "road", stage: "product",
      note: "Het New York-topsegment -> de Amerikaanse eindklant." },
  ],

  // ==========================================================================
  // SPANNINGEN — waar de diamantketen knijpt. Verwijst naar node-ids en flows
  // ("from-id>to-id"). De diamant-knijp is deels GEOGRAFISCH-downstream (Surat),
  // deels INSTITUTIONEEL (Antwerpen-certificering, De Beers/Alrosa-duopolie,
  // G7-sanctie) en deels STRUCTUREEL (lab-grown, waarde-vs-volume).
  // ==========================================================================
  tensions: [
    { id: "dia-t-surat", type: "concentratie", title: "De Surat-trechter: één stad slijpt de hele wereld",
      lat: 21.17, lon: 72.83,
      nodes: ["dia-surat", "dia-antwerp", "dia-dubai", "dia-gaborone"],
      flows: ["dia-antwerp>dia-surat", "dia-dubai>dia-surat", "dia-gaborone>dia-surat"],
      metric: "~90-95% van alle diamant geslepen & gepolijst in Surat (Gujarat), ~1 mln slijpers",
      note: "De scherpste downstream-concentratie van de atlas. Waar de winning breed verspreid is, komt de wáárde-toevoeging — het slijpen en polijsten — vrijwel volledig samen in één Indiase stad. Zelfs Botswaanse, Canadese en Russische rough vliegt naar Surat om daar bewerkt te worden. Een verstoring van Surat (arbeid, energie, water) raakt de hele wereld-diamantvoorziening tegelijk — een nog extremere versie van de China-raffinagetrechter." },

    { id: "dia-t-duopoly", type: "structureel", title: "Het De Beers + Alrosa-duopolie: het kartel-verleden",
      lat: -24.65, lon: 25.91,
      nodes: ["dia-alrosa", "dia-gaborone", "dia-jwaneng", "dia-orapa"],
      flows: ["dia-jwaneng>dia-gaborone", "dia-gaborone>dia-surat", "dia-alrosa>dia-dubai"],
      metric: "De Beers ~30% + Alrosa ~30% · historisch CSO/single-channel ~80-90%",
      note: "De diamantmarkt is decennialang kunstmatig gestuurd. De Beers hield via de Central Selling Organisation ~80-90% van de rough in één kanaal en verkocht schaarste ('A Diamond is Forever'). Nu is het meer een duopolie — De Beers (~30%) via de 'sights' in Gaborone, Alrosa (~30%) uit Rusland. De prijszetting leunt nog altijd op gecontroleerd aanbod, niet op een vrije markt." },

    { id: "dia-t-antwerp", type: "beleid", title: "Antwerpen: van handelshoofdstad naar sanctie-certificering",
      lat: 51.22, lon: 4.42,
      nodes: ["dia-antwerp", "dia-canada", "dia-catoca", "dia-surat"],
      flows: ["dia-canada>dia-antwerp", "dia-antwerp>dia-surat"],
      metric: "sinds maart 2024: niet-Russische rough verplicht via het 'Antwerp node' voor de G7-markt",
      note: "Antwerpen was eeuwenlang de handelshoofdstad van de diamant, maar Surat nam het slijpen over. De G7-sanctie op Russische diamant (maart 2024) gaf Antwerpen een nieuwe, institutionele rol: het verplichte certificeringsknooppunt waar niet-Russische rough z'n herkomst moet aantonen om de G7-markt te bereiken. Een knelpunt zonder zeestraat — de rough maakt fysiek de omweg mijn -> Antwerpen -> Surat." },

    { id: "dia-t-russia", type: "beleid", title: "Alrosa & de G7-sanctie: de stroom buigt om, niet weg",
      lat: 62.53, lon: 113.96,
      nodes: ["dia-alrosa", "dia-dubai", "dia-surat"],
      flows: ["dia-alrosa>dia-dubai", "dia-alrosa>dia-surat"],
      metric: "Rusland ~30% van het volume onder G7-sanctie (maart 2024) -> herrouting Dubai/India",
      note: "Rusland is de grootste producent op volume, en Alrosa staat sinds 2024 op de sanctielijst. Maar diamant is klein, waardevol en makkelijk om te leiden: de Russische stenen verdwijnen niet, ze buigen zichtbaar om Antwerpen/de G7 heen — naar Dubai en direct naar Surat, waar ze net zo goed geslepen worden. Handhaving stuit op de fungibiliteit van een steen die je in een envelop meeneemt." },

    { id: "dia-t-labgrown", type: "structureel", title: "Lab-grown: de synthetische ontwrichting",
      lat: 40.00, lon: -83.00,
      nodes: ["dia-mkt-us", "dia-surat", "dia-mumbai"],
      flows: ["dia-mumbai>dia-mkt-us"],
      metric: "China (Henan/HPHT) + India (CVD) · prijs natuurlijke steen in het VS-verlovingssegment sterk gedaald",
      note: "De grootste bedreiging komt niet uit de grond maar uit de fabriek. Kweekdiamant — chemisch identiek — wordt massaal geproduceerd in China (Henan, HPHT-persen) en India (CVD, deels in Surat zelf) en heeft de prijs van natuurlijke stenen in het Amerikaanse verlovingsring-segment onderuitgehaald. De hele duopolie-schaarstelogica staat onder druk. In deze atlas is lab-grown v1 een spanning; de aparte, optionele toggle-laag (schaduwaanbod dat de VS-markt ondergraaft) is uitgesteld naar een eigen issue." },

    { id: "dia-t-beneficiation", type: "concentratie", title: "Waarde vs. volume: Botswana wil de slijpwaarde terug",
      lat: -21.31, lon: 25.37,
      nodes: ["dia-jwaneng", "dia-orapa", "dia-gaborone", "dia-surat"],
      flows: ["dia-jwaneng>dia-gaborone", "dia-gaborone>dia-surat"],
      metric: "Botswana #1 op WAARDE · Rusland/DRC #1 op VOLUME · de slijpwaarde vangt Surat",
      note: "Diamant kent een scherpe kloof tussen volume en waarde: Rusland en DR Congo produceren de meeste karaat, maar Botswana en Namibië de meeste dollars. En de grootste waardesprong — het slijpen — gebeurt in India, niet in het producentenland. Botswana dwong De Beers al de verkoop naar Gaborone te verplaatsen (2013) en eist nu een groter aandeel én lokale slijperij, om te voorkomen dat de winst het land verlaat naar Surat. Beneficiation als politieke hefboom." },
  ],
});
