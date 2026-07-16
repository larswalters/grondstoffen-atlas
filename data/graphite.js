// ============================================================================
// GRAFIET (C) — volledig uitgewerkte module. Peiljaar ±2023-2024.
// Cijfers indicatief/afgerond, o.b.v. USGS Mineral Commodity Summaries 2025
// (Graphite, natural), Benchmark Mineral Intelligence / IEA Critical Minerals
// (anode-/verwerkingsaandeel) en bedrijfsrapportages (Syrah, Talga, Novonix,
// NMG, POSCO Future M, BTR). Eenheid overal: kt/jaar. Zie design/grafiet.md.
//
// DE VORM VAN GRAFIET (een REE-achtige verwerkingstrechter, met TWEE feedstocks):
//   - Grafiet is HET anodemateriaal in vrijwel elke lithium-ionbatterij (grootste
//     celcomponent naar massa, ~1 kg/kWh). Het komt uit twee grondstofstromen:
//       (1) NATUURLIJK vlokgrafiet — gedolven (China #1 ~65% van natuurlijk,
//           Mozambique/Balama, Madagascar, Brazilië, Tanzania, +Europa).
//       (2) SYNTHETISCH grafiet — uit petroleum-NAALDCOKES (of koolteerpek),
//           gegrafitiseerd bij ~3000 °C (energie-intensief, hoge zuiverheid).
//   - Beide moeten door DEZELFDE VERWERKINGSTRECHTER: spheronisatie + zuivering
//     (99,95%+) + coating voor natuurlijk, grafitisatie voor synthetisch. Die
//     stap zit ~90%+ IN CHINA — Shandong (natuurlijk) + Binnen-Mongolië
//     (synthetisch, op goedkope kolenstroom). ZELFS ex-China-vlok vaart naar
//     China om verwerkt te worden -> de mijn is niet waar de knijp zit.
//   - GEOPOLITIEK: in december 2023 legde China EXPORTVERGUNNINGEN op grafiet-
//     anodemateriaal (natuurlijk + synthetisch) — na gallium/germanium, vóór de
//     bredere REE-controles (2025). Het Westen bouwt ex-China anodecapaciteit
//     (Syrah Vidalia/Louisiana uit Balama-vlok, Novonix/Tennessee, Talga/Zweden,
//     NMG/Québec, POSCO/Korea) onder IRA-FEOC + EU-CRMA — klein en traag.
//
// STAGES (via `stage`):
//   erts       = vlokgrafiet-concentraat + synthetische naaldcokes-feedstock op
//                weg naar de verwerker — dof/donkergrijs. Óók recyclaat.
//   raffinaat  = gecoat sferisch / gegrafitiseerd anodepoeder — vol grafietgrijs.
//   product    = batterijcel / gigafabriek (EV/opslag) — licht.
//
// TRANSPORT is schip + land. GEEN nieuwe render-modus, GEEN nieuw chokepoint:
// vierde grondstof (na nikkel/olie/zilver) die volledig op de bestaande route-
// kaart draait (Malakka/Singapore/SCS/Taiwan voor Azië-aanvoer; Kaap + Panama +
// Golf van Mexico/Florida voor de trans-Atlantische Balama->Vidalia-lijn; Suez/
// Bab/Gibraltar + Rotterdam voor China->EU). Inland-origins bij een ship-flow:
// 1e via = een haven (gathering-leg routeert auto als land, olie/koper-patroon).
//
// RECYCLING (type "recycler" / flow.layer "recycle") = de BESTAANDE optionele
// toggle van REE/PGM, hergebruikt zonder engine-wijziging. Batterijgrafiet-
// terugwinning is nog nascent/klein (Redwood/Li-Cycle/Ascend + EU-batterij-
// verordening) -> bewust bescheiden, default uit.
// ============================================================================

REGISTER({
  id: "graphite",
  name: "Grafiet",
  symbol: "C",
  color: "#78828F",       // grafietgrijs: de mijn-markers
  flowColor: "#B6BEC8",   // lichter grijs: de stromen tegen de donkere bol
  detail: "uitgewerkt",
  unit: "kt/jaar (indicatief)",
  recycleHint: "Batterij-/anodegrafiet-recycling tonen (nog nascent, klein aandeel)",
  blurb: "Grafiet is het anodemateriaal in vrijwel elke lithium-ionbatterij. Twee " +
    "feedstocks — natuurlijk vlokgrafiet (China #1, Mozambique, Madagascar) en synthetisch " +
    "grafiet uit petroleum-naaldcokes — komen samen op dezelfde knijp: de omzetting tot " +
    "gecoat sferisch/gegrafitiseerd anodepoeder zit ~90%+ in China (Shandong natuurlijk, " +
    "Binnen-Mongolië synthetisch). Zelfs Afrikaans vlok vaart naar China om verwerkt te " +
    "worden. In december 2023 legde China exportvergunningen op grafiet-anodemateriaal.",

  nodes: [
    // ============================================= WINNING — NATUURLIJK VLOK
    // `share` = ~% van de natuurlijke vlokgrafiet-winning (~1,6 Mt/jaar). China
    // domineert de winning ÉN de verwerking; de rest vaart grotendeels naar China.
    { id: "gr-china-flake", type: "mine", name: "Heilongjiang (Luobei/Jixi)", country: "China",
      lat: 47.60, lon: 130.80, share: 65, tier: 1, operator: "div. (BTR e.a.)",
      status: "actief", capacity: "≈ 900 kt/j",
      note: "Grootste natuurlijk vlokgrafiet ter wereld — én het startpunt van de binnenlandse verwerkingsketen. Vlok per spoor naar de Shandong-spheronisatie." },
    { id: "gr-mozambique", type: "mine", name: "Balama (Twigg)", country: "Mozambique",
      lat: -13.29, lon: 38.53, share: 13, tier: 1, operator: "Syrah Resources",
      status: "actief", capacity: "≈ 350 kt/j (nameplate)",
      note: "Grootste vlokmijn buiten China. Het vlok gaat twee kanten op: het leeuwendeel naar de Chinese verwerking, én een deel naar Syrah's eigen anodefabriek in Vidalia (Louisiana) — het niet-Chinese draadje." },
    { id: "gr-madagascar", type: "mine", name: "Molo / Ampanihy", country: "Madagaskar",
      lat: -23.70, lon: 44.80, share: 6, tier: 2, operator: "NextSource e.a.",
      status: "actief", capacity: "≈ 150 kt/j",
      note: "Groot, hoogwaardig vlok. Grotendeels naar China/Korea voor spheronisatie — de winning is niet waar de waarde zit." },
    { id: "gr-brazil", type: "mine", name: "Minas Gerais (Nacional de Grafite)", country: "Brazilië",
      lat: -17.50, lon: -42.00, share: 7, tier: 2, operator: "Nacional de Grafite / SGL",
      status: "actief", capacity: "≈ 100 kt/j",
      note: "Gevestigde producent (amorf + vlok). Deels binnenlands verwerkt, deels de lange haul om de Kaap naar China." },
    { id: "gr-tanzania", type: "mine", name: "Mahenge / Epanko", country: "Tanzania",
      lat: -8.70, lon: 36.70, share: 3, tier: 3, operator: "EcoGraf/Magnis e.a.",
      status: "project", capacity: "≈ 60 kt/j (opstartend)",
      note: "Nieuwe projecten met hoogwaardig vlok; bestemd voor de Aziatische (en beoogd westerse) anodeketen." },
    { id: "gr-norway", type: "mine", name: "Skaland (Senja)", country: "Noorwegen",
      lat: 69.45, lon: 17.30, share: 1, tier: 3, operator: "Skaland Graphite",
      status: "actief", capacity: "≈ 15 kt/j",
      note: "Hoogwaardigste vlok van Europa. Over land/spoor (Narvik) naar Talga's anodefabriek in Luleå." },
    { id: "gr-ukraine", type: "mine", name: "Zavallya (Zavalievsky)", country: "Oekraïne",
      lat: 48.23, lon: 30.40, share: 2, tier: 3, operator: "Zavalievsky Graphite",
      status: "actief", capacity: "≈ 20 kt/j",
      note: "Europees vlok, oorlog-verstoord. Over land naar de EU-verwerking — het schaarse Europese alternatief." },
    { id: "gr-srilanka", type: "mine", name: "Bogala/Kahatagaha (via Colombo)", country: "Sri Lanka",
      lat: 6.93, lon: 79.90, share: 1, tier: 3, operator: "Bogala Graphite", coastal: true,
      status: "actief", capacity: "≈ 8 kt/j",
      note: "VEIN-/klompgrafiet — de zeldzame ~99% zuivere natuurlijke vorm (geen zuivering nodig). Klein maar uniek; naar Japan voor premium-toepassingen." },

    // ======================================= WINNING — SYNTHETISCHE FEEDSTOCK
    // Synthetisch grafiet start niet in een mijn maar bij NAALDCOKES (petroleum-
    // cokes uit olieraffinage of koolteerpek uit staal). Twee bronnen tonen het
    // contrast: premium VS-naaldcokes (deels geëxporteerd) vs. de Chinese
    // naaldcokes die de Binnen-Mongolië-grafitisatie voedt.
    { id: "gr-nc-us", type: "mine", name: "Naaldcokes VS (Lake Charles/Seadrift)", country: "VS",
      lat: 30.20, lon: -93.20, tier: 2, operator: "Phillips 66 / Seadrift Coke", coastal: true,
      status: "actief", capacity: "premium needle coke",
      note: "Premium petroleum-naaldcokes — de grondstof voor synthetisch anode. Binnenlands (Novonix) én export naar Aziatische grafitiseerders. Géén mijn-share: het is een raffinage-bijproduct." },
    { id: "gr-nc-china", type: "mine", name: "Naaldcokes China (Liaoning/Shandong)", country: "China",
      lat: 38.90, lon: 121.60, tier: 2, operator: "Sinopec e.a.", coastal: true,
      status: "actief", capacity: "bulk needle coke",
      note: "Binnenlandse petroleum-/koolteer-naaldcokes die de Binnen-Mongolië-grafitisatie voedt. Géén mijn-share." },

    // ==================================== VERWERKING / ANODEMATERIAAL (raffinaat)
    // DE TRECHTER: spheronisatie/zuivering (natuurlijk) + grafitisatie (synthetisch),
    // ~90%+ in China. Daarnaast de dunne ex-China buildout (Vidalia/Talga/Novonix/
    // NMG/POSCO/Japan) die er tegenin bouwt.
    { id: "gr-ref-shandong", type: "refinery", name: "China — sferisch/natuurlijk anode (Shandong/Qingdao)", country: "China",
      lat: 36.10, lon: 120.30, tier: 1, operator: "BTR / Ningbo Shanshan", coastal: true,
      capacity: "≈ dominant (natuurlijk)",
      note: "DE trechter voor natuurlijk grafiet: spheronisatie + zuivering tot 99,95%+ + coating. Verwerkt binnenlands ÉN geïmporteerd vlok (Mozambique/Madagascar/Brazilië). ~90%+ van al het sferische anode ter wereld komt hier vandaan." },
    { id: "gr-ref-innermongolia", type: "refinery", name: "China — synthetisch anode / grafitisatie (Binnen-Mongolië)", country: "China",
      lat: 40.60, lon: 109.00, tier: 1, operator: "BTR / Putailai / Shanshan",
      capacity: "≈ dominant (synthetisch)",
      note: "DE trechter voor synthetisch grafiet: grafitisatie bij ~3000 °C — extreem energie-intensief, daarom hier op goedkope kolenstroom (Wuhai/Baotou). Het CO2-intensieve schaduwzijde van 'schone' batterijen." },
    { id: "gr-ref-japan", type: "refinery", name: "Japan — synthetisch anode (Resonac/Mitsubishi Chem)", country: "Japan",
      lat: 35.00, lon: 136.90, tier: 2, operator: "Resonac / Mitsubishi Chemical", coastal: true,
      capacity: "≈ premium",
      note: "Premium synthetisch anode voor hoogwaardige cellen; deels op VS-/Japanse naaldcokes. Klein volume, hoge kwaliteit." },
    { id: "gr-ref-korea", type: "refinery", name: "POSCO Future M (Pohang/Sejong)", country: "Zuid-Korea",
      lat: 36.02, lon: 129.36, tier: 2, operator: "POSCO Future M", coastal: true,
      capacity: "≈ grootste ex-China",
      note: "De grootste anodeproducent buiten China. Natuurlijk (uit Mozambique/Tanzania-vlok) + synthetisch; de belangrijkste niet-Chinese verwerkingsknoop, gericht op IRA-/CRMA-conforme cellen." },
    { id: "gr-ref-vidalia", type: "refinery", name: "Syrah Resources — Vidalia", country: "VS (Louisiana)",
      lat: 31.57, lon: -91.42, tier: 1, operator: "Syrah Resources",
      capacity: "≈ 11,25 kt/j (fase 1)",
      note: "Actief sferisch grafiet uit Balama-vlok (Mozambique) — de zeldzame niet-Chinese natuurlijke-anodeknoop. IRA-FEOC-conform, levert Tesla e.a. Binnenwater: het vlok komt per barge de Mississippi op vanuit New Orleans." },
    { id: "gr-ref-novonix", type: "refinery", name: "Novonix — Chattanooga", country: "VS (Tennessee)",
      lat: 35.05, lon: -85.30, tier: 3, operator: "Novonix",
      capacity: "≈ opschalend",
      note: "Synthetisch anode uit VS-naaldcokes; IRA-gedreven Amerikaanse buildout." },
    { id: "gr-ref-sweden", type: "refinery", name: "Talga — Luleå (Vittangi)", country: "Zweden",
      lat: 65.58, lon: 22.15, tier: 2, operator: "Talga Group", coastal: true,
      capacity: "≈ opschalend",
      note: "EU natuurlijk anode (Talnode) uit eigen Vittangi-vlok + Skaland. Het schaarse volledig-Europese draadje in de anodeketen (CRMA)." },
    { id: "gr-ref-quebec", type: "refinery", name: "Nouveau Monde Graphite — Bécancour", country: "Canada",
      lat: 46.34, lon: -72.35, tier: 3, operator: "Nouveau Monde Graphite",
      capacity: "≈ opschalend",
      note: "Geïntegreerd natuurlijk anode (Matawinie-mijn → Bécancour-anodefabriek); onderdeel van de Noord-Amerikaanse ex-China keten." },

    // ================================================================ HAVENS
    { id: "gr-port-nacala", type: "port", name: "Nacala", country: "Mozambique",
      lat: -14.54, lon: 40.67, tier: 2,
      note: "Diepwaterhaven aan het einde van de Nacala-corridor; het Balama-vlok gaat hier de Indische Oceaan op (China) of rond de Kaap (Vidalia/VS)." },
    { id: "gr-port-toamasina", type: "port", name: "Toamasina (Tamatave)", country: "Madagaskar",
      lat: -18.15, lon: 49.41, tier: 3,
      note: "Grootste haven van Madagaskar; het vlok van Molo de Indische Oceaan op richting Azië." },
    { id: "gr-port-mtwara", type: "port", name: "Mtwara", country: "Tanzania",
      lat: -10.27, lon: 40.19, tier: 3,
      note: "Zuid-Tanzaniaanse haven bij de Mahenge/Epanko-projecten; vlok richting de Aziatische verwerking." },
    { id: "gr-port-vitoria", type: "port", name: "Vitória", country: "Brazilië",
      lat: -20.32, lon: -40.29, tier: 3,
      note: "Exporthaven voor het Minas-Gerais-grafiet; de Atlantische Oceaan op richting Azië/VS." },
    { id: "gr-port-neworleans", type: "port", name: "New Orleans", country: "VS",
      lat: 29.95, lon: -90.07, tier: 2,
      note: "Golf-gateway voor Syrah Vidalia: het Balama-vlok wordt hier gelost en gaat per barge de Mississippi op naar de anodefabriek." },
    { id: "gr-port-rotterdam", type: "port", name: "Rotterdam", country: "Nederland",
      lat: 51.95, lon: 4.14, tier: 2,
      note: "Europese gateway; het Chinese anodepoeder komt hier binnen op weg naar de EU-gigafabrieken." },

    // ================================================================ MARKT
    // Gigafabrieken/cellenfabrieken. China veruit de grootste anode-vraag.
    // Ship-endpoints coastal.
    { id: "gr-mkt-china-battery", type: "market", name: "China — gigafabrieken (CATL/BYD)", country: "China",
      lat: 26.66, lon: 119.55, tier: 1, coastal: true,
      note: "'s Werelds grootste anode-/batterijvraag (Ningde, Fujian + het hele oostkust-cluster). De dikste product-bogen van de keten eindigen hier." },
    { id: "gr-mkt-korea-japan", type: "market", name: "Korea/Japan — cellenfabrieken", country: "Zuid-Korea",
      lat: 35.50, lon: 129.30, tier: 2, coastal: true,
      note: "LG/Samsung SDI/SK On/Panasonic — premium cellen. Leunt op eigen POSCO/Resonac-anode én (onder exportvergunning) Chinees anode." },
    { id: "gr-mkt-eu", type: "market", name: "EU — gigafabrieken (DE/HU/PL)", country: "Duitsland",
      lat: 50.98, lon: 11.00, tier: 2,
      note: "De Europese gigafabrieken zijn sterk afhankelijk van Chinees anode; de CRMA wil dat terugdringen met eigen capaciteit (Talga) — vooralsnog dun." },
    { id: "gr-mkt-us", type: "market", name: "VS — battery belt (Tesla/Ultium)", country: "VS",
      lat: 36.50, lon: -86.60, tier: 2,
      note: "Het Amerikaanse batterij-cluster (TN/KY/NV/GA). IRA-FEOC sluit Chinees anode uit vanaf 2025 → dwingt de vraag naar Syrah/Novonix/NMG/POSCO." },

    // ============================================================= RECYCLING
    // OPTIONELE toggle-laag (layer "recycle" op nodes én flows) — hergebruikt het
    // REE/PGM-patroon met 0 engine-wijziging. Batterijgrafiet-terugwinning is nog
    // NASCENT (het meeste verbruikte grafiet wordt nu verbrand/gestort); de EU-
    // batterijverordening (gerecycleerd-gehalte vanaf ~2027) trekt het op gang.
    { id: "gr-rec-us", type: "recycler", name: "Redwood Materials (Nevada)", country: "VS",
      lat: 39.54, lon: -119.40, tier: 3, layer: "recycle",
      note: "Wint anodegrafiet terug uit afgedankte batterijen; nog opschalend, gericht op de eigen VS-anodeketen." },
    { id: "gr-rec-eu", type: "recycler", name: "EU-batterijrecycling (Skellefteå)", country: "Zweden",
      lat: 64.75, lon: 20.95, tier: 3, layer: "recycle",
      note: "De EU-batterijverordening dwingt gerecycleerd-gehalte af → grafiet-terugwinning terug de Europese anodeketen (Talga) in." },
    { id: "gr-rec-china", type: "recycler", name: "China-batterijrecycling (Brunp/GEM)", country: "China",
      lat: 30.50, lon: 114.30, tier: 3, layer: "recycle",
      note: "Grootste batterijrecyclingbasis ter wereld (Hubei); grafiet-terugwinning schaalt het snelst hier." },
  ],

  // ==========================================================================
  // STROMEN — value in kt/jaar. stage bepaalt de kleur (erts dof, raffinaat vol
  // grafietgrijs, product licht). `via` = echte route langs havens (gr-port-*) en
  // de universele knelpunten/vaarpunten (wp-* uit data/_chokepoints.js).
  //
  //  A) Mijn/feedstock -> verwerking (vlok + naaldcokes convergeren op China)
  //  B) Verwerking -> gigafabriek (anodepoeder de cellenfabrieken in)
  //  C) Recycling -> verwerking (layer:"recycle" -> alleen met de toggle)
  // ==========================================================================
  flows: [
    // === A. MIJN/FEEDSTOCK -> VERWERKING (stage erts) =========================
    { from: "gr-china-flake", to: "gr-ref-shandong", value: 900, mode: "rail", stage: "erts",
      note: "Binnenlands vlok -> de Shandong-spheronisatie. China verwerkt z'n eigen vlok (én dat van de rest van de wereld)." },
    { from: "gr-mozambique", to: "gr-ref-shandong", value: 220, mode: "ship", stage: "erts",
      via: ["gr-port-nacala", "wp-moz-noord", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Het emblematische feit: ex-China vlok (Balama) VAART NAAR CHINA om verwerkt te worden. Nacala -> Indische Oceaan -> Malakka -> China." },
    { from: "gr-mozambique", to: "gr-ref-vidalia", value: 60, mode: "ship", stage: "erts",
      via: ["gr-port-nacala", "wp-kaap", "wp-atl-west", "wp-florida", "gr-port-neworleans"],
      note: "Het niet-Chinese draadje: Balama-vlok rond de Kaap over de Atlantische Oceaan naar Syrah's eigen anodefabriek in Vidalia (Louisiana)." },
    { from: "gr-madagascar", to: "gr-ref-shandong", value: 70, mode: "ship", stage: "erts",
      via: ["gr-port-toamasina", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Madagascar-vlok -> de Chinese verwerking (Toamasina -> Malakka -> Shandong)." },
    { from: "gr-madagascar", to: "gr-ref-korea", value: 40, mode: "ship", stage: "erts",
      via: ["gr-port-toamasina", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Een deel naar POSCO (het ex-China alternatief) — de diversificatie die nog dun is." },
    { from: "gr-tanzania", to: "gr-ref-korea", value: 45, mode: "ship", stage: "erts",
      via: ["gr-port-mtwara", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Tanzaniaans vlok -> POSCO Korea (Mtwara -> Malakka)." },
    { from: "gr-brazil", to: "gr-ref-shandong", value: 60, mode: "ship", stage: "erts",
      via: ["gr-port-vitoria", "wp-kaap", "wp-aceh", "wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Braziliaans vlok -> China: de lange haul om de Kaap de Goede Hoop en dwars over de Indische Oceaan." },
    { from: "gr-norway", to: "gr-ref-sweden", value: 15, mode: "rail", stage: "erts",
      note: "Skaland (Senja) -> Talga Luleå, over het Noord-Scandinavische spoor (via Narvik). Europees vlok in een Europese fabriek." },
    { from: "gr-ukraine", to: "gr-ref-sweden", value: 20, mode: "rail", stage: "erts",
      note: "Zavallya -> de EU-verwerking over land (via de Øresundbrug). Oorlog-verstoord, maar het schaarse Europese vlok." },
    { from: "gr-srilanka", to: "gr-ref-japan", value: 12, mode: "ship", stage: "erts",
      via: ["wp-malakka", "wp-singapore", "wp-scs", "wp-taiwan"],
      note: "Sri Lankaans vein-grafiet (~99% zuiver) -> Japan voor premium-toepassingen; via Colombo en de Straat van Malakka." },
    // --- synthetische feedstock (naaldcokes -> grafitisatie) ---
    { from: "gr-nc-us", to: "gr-ref-novonix", value: 120, mode: "road", stage: "erts",
      note: "VS-naaldcokes -> Novonix (Tennessee): binnenlands synthetisch anode." },
    { from: "gr-nc-us", to: "gr-ref-japan", value: 90, mode: "ship", stage: "erts",
      via: ["wp-golf-mexico", "wp-caribisch", "wp-panama", "wp-pac-noord"],
      note: "Premium VS-naaldcokes de Golf uit, door Panama en over de Stille Oceaan naar de Japanse grafitisatie." },
    { from: "gr-nc-china", to: "gr-ref-innermongolia", value: 700, mode: "rail", stage: "erts",
      note: "Chinese naaldcokes -> de Binnen-Mongolië-grafitisatie (op goedkope kolenstroom). De synthetische trechter." },

    // === B. VERWERKING -> GIGAFABRIEK (stage product) ========================
    { from: "gr-ref-shandong", to: "gr-mkt-china-battery", value: 700, mode: "rail", stage: "product",
      note: "De dikste boog van de keten: Chinees natuurlijk anode -> de CATL/BYD-gigafabrieken. Binnenlands, kort." },
    { from: "gr-ref-innermongolia", to: "gr-mkt-china-battery", value: 650, mode: "rail", stage: "product",
      note: "Chinees synthetisch anode -> de gigafabrieken. Samen met Shandong beheerst China de anode-toevoer." },
    { from: "gr-ref-shandong", to: "gr-mkt-korea-japan", value: 180, mode: "ship", stage: "product",
      via: ["wp-taiwan"],
      note: "Chinees anode -> de Korea/Japan-cellenfabrieken. Sinds dec 2023 exportvergunning-plichtig — de hefboom zichtbaar." },
    { from: "gr-ref-shandong", to: "gr-mkt-eu", value: 160, mode: "ship", stage: "product",
      via: ["wp-scs", "wp-singapore", "wp-malakka", "wp-bab", "wp-rode-zee", "wp-suez", "wp-gibraltar", "gr-port-rotterdam"],
      note: "Chinees anode -> de EU-gigafabrieken via Suez en Rotterdam: de Europese afhankelijkheid waar de CRMA tegen wil bouwen." },
    { from: "gr-ref-vidalia", to: "gr-mkt-us", value: 45, mode: "rail", stage: "product",
      note: "Syrah's US anode -> de battery belt. IRA-FEOC-conform (Balama-vlok, VS-verwerkt)." },
    { from: "gr-ref-novonix", to: "gr-mkt-us", value: 100, mode: "road", stage: "product",
      note: "Novonix synthetisch anode -> de Amerikaanse cellenfabrieken." },
    { from: "gr-ref-quebec", to: "gr-mkt-us", value: 40, mode: "road", stage: "product",
      note: "NMG Québec-anode -> de VS (Noord-Amerika geïntegreerd, over land)." },
    { from: "gr-ref-korea", to: "gr-mkt-korea-japan", value: 130, mode: "road", stage: "product",
      note: "POSCO-anode -> de Koreaanse cellenfabrieken (LG/Samsung SDI/SK On)." },
    { from: "gr-ref-japan", to: "gr-mkt-korea-japan", value: 110, mode: "ship", stage: "product",
      note: "Japans synthetisch anode -> de Korea/Japan-cellenfabrieken, over de Straat van Korea (korte zee-hop)." },
    { from: "gr-ref-sweden", to: "gr-mkt-eu", value: 30, mode: "rail", stage: "product",
      note: "Talga EU-anode -> de EU-gigafabrieken: de dunne, volledig-Europese lijn tegenover de dikke Chinese." },

    // === C. RECYCLING -> VERWERKING (layer:"recycle" -> alleen met de toggle) =
    // Stage erts (feedstock terug). Default uit; nascent volume.
    { from: "gr-rec-us", to: "gr-ref-novonix", value: 25, mode: "road", stage: "erts", layer: "recycle",
      note: "Redwood-teruggewonnen grafiet -> US-anode; de Amerikaanse gesloten-kringloop-ambitie (nog klein)." },
    { from: "gr-rec-eu", to: "gr-ref-sweden", value: 15, mode: "rail", stage: "erts", layer: "recycle",
      note: "EU-batterijrecycling -> Talga: de batterijverordening dwingt gerecycleerd-gehalte af." },
    { from: "gr-rec-china", to: "gr-ref-shandong", value: 40, mode: "rail", stage: "erts", layer: "recycle",
      note: "China-recycling -> de Shandong-verwerking; de grootste recyclingbasis schaalt grafiet-terugwinning het snelst." },
  ],

  // ==========================================================================
  // SPANNINGEN — waar de grafietketen 'knijpt'. Net als REE is de knijp niet een
  // zeestraat maar de VERWERKING: twee feedstocks die op de Chinese anode-
  // verwerking convergeren, sinds dec 2023 met een exportvergunning-hefboom.
  // ==========================================================================
  tensions: [
    { id: "gr-t-china-processing", type: "raffinage", title: "De anode-verwerkingstrechter: ~90%+ China",
      lat: 38.0, lon: 115.0,
      nodes: ["gr-ref-shandong", "gr-ref-innermongolia"],
      flows: ["gr-china-flake>gr-ref-shandong", "gr-nc-china>gr-ref-innermongolia", "gr-ref-shandong>gr-mkt-china-battery"],
      metric: "China ~90%+ van spheronisatie/zuivering (natuurlijk) én grafitisatie (synthetisch)",
      note: "De kern-'aha' van grafiet — de REE-Ganzhou-parallel. Winning is verspreid, maar de omzetting tot bruikbaar anodepoeder (sferisch maken + zuiveren tot 99,95% voor natuurlijk; grafitiseren bij ~3000 °C voor synthetisch) zit overweldigend in China: Shandong voor natuurlijk, Binnen-Mongolië voor synthetisch (op goedkope kolenstroom). Niet de mijn maar de fabriek is de knijp." },

    { id: "gr-t-flake-to-china", type: "concentratie", title: "Zelfs ex-China vlok vaart naar China",
      lat: 3.0, lon: 80.0,
      nodes: ["gr-mozambique", "gr-madagascar", "gr-brazil", "gr-ref-shandong"],
      flows: ["gr-mozambique>gr-ref-shandong", "gr-madagascar>gr-ref-shandong", "gr-brazil>gr-ref-shandong"],
      metric: "Mozambique/Madagascar/Brazilië-vlok -> Chinese spheronisatie (de mijn ≠ de waarde)",
      note: "Het gevolg van de trechter: een land kan het vlok wél delven, maar zonder verwerking blijft het afhankelijk. Balama (Mozambique), Molo (Madagaskar) en Minas Gerais (Brazilië) sturen het leeuwendeel van hun vlok naar China om er anodemateriaal van te laten maken — de winning is niet waar de geopolitieke hefboom ligt." },

    { id: "gr-t-export-controls", type: "beleid", title: "China's grafiet-exportvergunningen (dec 2023)",
      lat: 41.5, lon: 111.0,
      nodes: ["gr-ref-shandong", "gr-ref-innermongolia", "gr-mkt-korea-japan", "gr-mkt-eu"],
      flows: ["gr-ref-shandong>gr-mkt-korea-japan", "gr-ref-shandong>gr-mkt-eu"],
      metric: "dec 2023: vergunningplicht op natuurlijk sferisch + synthetisch anodemateriaal",
      note: "De verwerkingsdominantie omgezet in een actieve hefboom. In december 2023 stelde China exportvergunningen in op grafiet-anodemateriaal — na gallium/germanium (juli 2023) en vóór de bredere zeldzame-aardcontroles (2025). Het raakt precies de landen die hun cellen bouwen maar hun anode uit China halen (Korea/Japan/EU)." },

    { id: "gr-t-synthetic-natural", type: "structureel", title: "Twee grafieten: vlok vs. synthetisch (naaldcokes)",
      lat: 34.0, lon: 128.0,
      nodes: ["gr-china-flake", "gr-ref-shandong", "gr-nc-us", "gr-nc-china", "gr-ref-innermongolia"],
      flows: ["gr-nc-china>gr-ref-innermongolia", "gr-nc-us>gr-ref-japan"],
      metric: "natuurlijk (gedolven vlok) ~50% · synthetisch (uit petroleum-naaldcokes) ~50% en groeiend",
      note: "Grafiet komt uit twee werelden. Natuurlijk vlok wordt gedolven en sferisch gemaakt; synthetisch grafiet wordt uit petroleum-naaldcokes gegrafitiseerd bij ~3000 °C — duurder en zeer energie-/CO2-intensief, maar met betere cycluslevensduur/snellaadgedrag, dus groeiend in aandeel. Beide komen samen op de Chinese verwerking; de synthetische route hangt bovendien aan de olie-/staalketen (naaldcokes)." },

    { id: "gr-t-west-buildout", type: "concentratie", title: "De ex-China buildout: dun tegenover de trechter",
      lat: 40.0, lon: -60.0,
      nodes: ["gr-ref-vidalia", "gr-ref-sweden", "gr-ref-novonix", "gr-ref-quebec", "gr-ref-korea"],
      flows: ["gr-mozambique>gr-ref-vidalia", "gr-ref-vidalia>gr-mkt-us", "gr-ref-sweden>gr-mkt-eu"],
      metric: "Syrah Vidalia (VS) · Talga (SE) · Novonix (VS) · NMG (CA) · POSCO (KR) — samen nog een fractie",
      note: "Onder IRA-FEOC (VS) en de CRMA (EU) racet het Westen om eigen anodecapaciteit. Syrah Vidalia (Balama-vlok, in Louisiana verwerkt) is de emblematische niet-Chinese knoop; Talga (volledig Europees), Novonix (synthetisch, VS), NMG (Canada) en POSCO (Korea) bouwen mee. Samen vormen ze nog een fractie van de Chinese capaciteit — de trechter is voorlopig niet omzeild." },

    { id: "gr-t-battery-demand", type: "vraag", title: "Anode = de grootste celcomponent naar massa",
      lat: 26.66, lon: 119.55,
      nodes: ["gr-mkt-china-battery", "gr-mkt-us", "gr-mkt-eu"],
      flows: ["gr-ref-shandong>gr-mkt-china-battery", "gr-ref-innermongolia>gr-mkt-china-battery"],
      metric: "~1 kg grafiet per kWh — grafiet is naar massa het grootste onderdeel van een Li-ionbatterij",
      note: "Waarom dit ertoe doet: er zit meer grafiet in een lithium-ionbatterij dan lithium, nikkel of kobalt (~1 kg/kWh). De EV- en opslaggroei trekt de anode-vraag hard omhoog, en grafiet staat op de kritieke-grondstoffenlijsten van zowel de VS als de EU. De vraag concentreert in China's gigafabrieken (Ningde/CATL), met de EU/VS-clusters afhankelijk van geïmporteerd of net-opgebouwd anode." },
  ],
});
