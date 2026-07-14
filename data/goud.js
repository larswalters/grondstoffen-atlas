// goud.js — GOUD (Au). Peiljaar ±2024. Volumes in t/jaar (indicatief, afgerond).
// Bron: World Gold Council, USGS MCS 2025, LBMA, Metals Focus. Zie data/goud.md.
//
// De vorm van goud is ánders dan lithium: de MIJNBOUW is wijd verspreid (geen
// enkel land domineert), maar de RAFFINAGE knijpt samen in Zwitserland (Ticino).
// Van daaruit een kleine ring kluis-/handelshubs; China is een eenrichtings-put.
//
// Transport is grotendeels LUCHTVRACHT (mode: "air" -> great-circle-boog; goud
// vliegt écht die boog). Korte hops in Europa/binnenland zijn "road"/"rail"
// (land-A*). De centrale-bank-laag (type "cb" / flow.layer "cb") is een aparte
// toggle die standaard uit staat.

REGISTER({
  id: "goud",
  name: "Goud",
  symbol: "Au",
  color: "#D4AF37",
  flowColor: "#F2C94C",
  detail: "uitgewerkt",
  unit: "t/jaar",
  blurb: "Mijnbouw wijd verspreid over álle continenten, maar de raffinage knijpt " +
    "samen in Zwitserland (Ticino, ~⅔ van de wereld). Van daaruit een kleine ring " +
    "kluishubs (Londen/NY/Zürich/Shanghai/Dubai); China is een eenrichtings-put.",

  nodes: [
    // ---------------------------------------------------------------- MIJNBOUW
    // Wijd verspreid; geen enkele mijn is groter dan ~2,5% van de wereld. Som ≈ 40%;
    // de rest is verspreid klein/artisanaal spul (bewust niet allemaal apart geprikt).
    { id: "au-nevada", type: "mine", name: "Nevada Gold Mines", country: "VS", lat: 40.30, lon: -116.30, share: 2.5, tier: 1, operator: "Barrick/Newmont JV", capacity: "≈ 84 t/j", note: "Grootste complex ter wereld (Carlin/Cortez). Doré grotendeels in de VS zelf geraffineerd." },
    { id: "au-muruntau", type: "mine", name: "Muruntau", country: "Oezbekistan", lat: 41.50, lon: 64.55, share: 2.5, tier: 1, operator: "Navoi MMC (staat)", capacity: "≈ 83 t/j", note: "Grootste open goudmijn; blijft grotendeels binnenlands (eigen raffinage/centrale bank)." },
    { id: "au-grasberg", type: "mine", name: "Grasberg", country: "Indonesië", lat: -4.06, lon: 137.11, share: 1.8, tier: 1, operator: "Freeport/Inalum", capacity: "≈ 59 t/j", note: "Goud als bijproduct van koper (Papoea); via de Gresik-smelter en export." },
    { id: "au-olimpiada", type: "mine", name: "Olimpiada", country: "Rusland", lat: 59.35, lon: 92.65, share: 1.3, tier: 1, operator: "Polyus", capacity: "≈ 44 t/j", note: "Siberië. Rusland absorbeert de eigen mijnproductie — nauwelijks wereldmarkt." },
    { id: "au-boddington", type: "mine", name: "Boddington", country: "Australië", lat: -32.75, lon: 116.36, share: 0.8, tier: 2, operator: "Newmont", capacity: "≈ 27 t/j", note: "West-Australië; raffinage bij Perth Mint." },
    { id: "au-cadia", type: "mine", name: "Cadia", country: "Australië", lat: -33.46, lon: 148.98, share: 0.7, tier: 2, operator: "Newmont", capacity: "≈ 24 t/j", note: "NSW; goud-koper." },
    { id: "au-detour", type: "mine", name: "Detour Lake", country: "Canada", lat: 49.90, lon: -79.70, share: 0.7, tier: 2, operator: "Agnico Eagle", capacity: "≈ 22 t/j", note: "Ontario." },
    { id: "au-malartic", type: "mine", name: "Canadian Malartic", country: "Canada", lat: 48.13, lon: -78.14, share: 0.7, tier: 2, operator: "Agnico Eagle", capacity: "≈ 22 t/j", note: "Québec." },
    { id: "au-kalgoorlie", type: "mine", name: "Kalgoorlie Super Pit", country: "Australië", lat: -30.78, lon: 121.50, share: 0.5, tier: 2, operator: "Northern Star", capacity: "≈ 15 t/j", note: "Iconische open pit (Fimiston)." },
    { id: "au-penasquito", type: "mine", name: "Peñasquito", country: "Mexico", lat: 24.66, lon: -101.55, share: 0.5, tier: 2, operator: "Newmont", capacity: "≈ 16 t/j", note: "Poly-metaal (goud + zilver)." },
    { id: "au-paracatu", type: "mine", name: "Paracatu", country: "Brazilië", lat: -17.22, lon: -46.87, share: 0.5, tier: 2, operator: "Kinross", capacity: "≈ 15 t/j", note: "Minas Gerais." },
    { id: "au-loulo", type: "mine", name: "Loulo-Gounkoto", country: "Mali", lat: 13.00, lon: -11.60, share: 0.6, tier: 1, operator: "Barrick", capacity: "≈ 20 t/j", note: "West-Afrika industrieel — naast enorme artisanale productie in de regio." },
    { id: "au-tarkwa", type: "mine", name: "Tarkwa", country: "Ghana", lat: 5.30, lon: -1.99, share: 0.5, tier: 2, operator: "Gold Fields", capacity: "≈ 17 t/j", note: "Ghana = grootste Afrikaanse producent." },
    { id: "au-obuasi", type: "mine", name: "Obuasi", country: "Ghana", lat: 6.20, lon: -1.66, share: 0.3, tier: 3, operator: "AngloGold Ashanti", capacity: "≈ 11 t/j", note: "Heropend ondergronds." },
    { id: "au-lihir", type: "mine", name: "Lihir", country: "Papoea-N.-Guinea", lat: -3.12, lon: 152.63, share: 0.5, tier: 2, operator: "Newmont", capacity: "≈ 18 t/j", note: "Vulkaaneiland." },
    { id: "au-yanacocha", type: "mine", name: "Yanacocha", country: "Peru", lat: -6.98, lon: -78.51, share: 0.3, tier: 3, operator: "Newmont", capacity: "≈ 10 t/j", note: "Uitgeput rakend; Peru is een grote producent." },
    { id: "au-mponeng", type: "mine", name: "Mponeng", country: "Zuid-Afrika", lat: -26.42, lon: 27.42, share: 0.3, tier: 2, operator: "Harmony", capacity: "≈ 8 t/j", note: "Diepste mijn ter wereld (Witwatersrand); raffinage bij Rand Refinery." },
    { id: "au-shandong", type: "mine", name: "Shandong-cluster", country: "China", lat: 37.35, lon: 120.40, share: 3.0, tier: 1, operator: "Shandong Gold/Zijin e.a.", capacity: "≈ 100 t/j (regio)", note: "China is 's werelds grootste producent — binnenlands geraffineerd en verbruikt, insulair." },
    { id: "au-kazakh", type: "mine", name: "Altyntau (Vasilkovskoye)", country: "Kazachstan", lat: 53.40, lon: 69.40, share: 0.4, tier: 3, operator: "Altyntau", capacity: "≈ 13 t/j", note: "Gaat deels naar de eigen centrale bank; grotendeels binnenlands." },
    { id: "au-sudan", type: "mine", name: "Sudan (artisanaal)", country: "Sudan", lat: 18.00, lon: 34.00, share: 0.6, tier: 2, operator: "artisanaal (informeel)", capacity: "≈ 20 t/j", note: "Grotendeels gesmokkeld → Dubai; het 'grijze' kanaal." },

    // --------------------------------------------------------------- RAFFINAGE
    // Hier knijpt het samen: de vier Zwitserse huizen samen ≈ 65-70% van de wereld.
    { id: "au-ref-valcambi", type: "refinery", name: "Valcambi (Balerna)", country: "Zwitserland", lat: 45.845, lon: 9.005, tier: 1, operator: "Valcambi", capacity: "cap. ≈ 2.000 t/j", note: "Grootste raffinaderij ter wereld — de trechter van Ticino." },
    { id: "au-ref-argor", type: "refinery", name: "Argor-Heraeus (Mendrisio)", country: "Zwitserland", lat: 45.87, lon: 8.98, tier: 1, operator: "Argor-Heraeus", capacity: "cap. ≈ 1.000 t/j", note: "Ticino." },
    { id: "au-ref-pamp", type: "refinery", name: "PAMP (Castel San Pietro)", country: "Zwitserland", lat: 45.87, lon: 9.03, tier: 1, operator: "MKS PAMP", capacity: "cap. ≈ 450 t/j", note: "Ticino; premium-baren." },
    { id: "au-ref-metalor", type: "refinery", name: "Metalor (Neuchâtel)", country: "Zwitserland", lat: 46.99, lon: 6.93, tier: 2, operator: "Metalor", capacity: "cap. ≈ 650 t/j", note: "Buiten Ticino maar Zwitsers; wereldwijde vestigingen." },
    { id: "au-ref-perth", type: "refinery", name: "Perth Mint", country: "Australië", lat: -31.955, lon: 115.87, tier: 2, operator: "The Perth Mint", capacity: "cap. ≈ 400 t/j", note: "Raffineert vrijwel alle Australische productie." },
    { id: "au-ref-rand", type: "refinery", name: "Rand Refinery (Germiston)", country: "Zuid-Afrika", lat: -26.23, lon: 28.16, tier: 2, operator: "Rand Refinery", capacity: "cap. ≈ 600 t/j", note: "Historisch grootste; verwerkt Afrikaanse doré." },
    { id: "au-ref-mmtc", type: "refinery", name: "MMTC-PAMP", country: "India", lat: 28.10, lon: 76.90, tier: 2, operator: "MMTC-PAMP", capacity: "cap. ≈ 200 t/j", note: "India-import + schroot (Rojka Meo, Haryana)." },
    { id: "au-ref-dubai", type: "refinery", name: "Dubai (Emirates Gold/Kaloti)", country: "VAE", lat: 25.20, lon: 55.28, tier: 2, operator: "div. (DMCC-zone)", capacity: "cap. ≈ 500 t/j", note: "Absorbeert Afrikaans/artisanaal goud (o.a. Sudan)." },
    { id: "au-ref-rcm", type: "refinery", name: "Royal Canadian Mint", country: "Canada", lat: 45.37, lon: -75.66, tier: 3, operator: "Royal Canadian Mint", capacity: "cap. ≈ 200 t/j", note: "Ottawa; Noord-Amerikaanse doré." },
    { id: "au-ref-china", type: "refinery", name: "China-intern (Zijin/China Gold)", country: "China", lat: 31.10, lon: 121.30, tier: 2, operator: "Zijin/China Gold", capacity: "cap. ≈ 500 t/j", note: "Insulair — raffineert binnenlands, exporteert vrijwel niet." },
    { id: "au-ref-japan", type: "refinery", name: "Tanaka / Mitsubishi", country: "Japan", lat: 35.68, lon: 139.76, tier: 3, operator: "Tanaka Kikinzoku", capacity: "cap. ≈ 150 t/j", note: "Tech-goud + belegging." },

    // -------------------------------------------------- GATEWAY-LUCHTHAVENS
    // Waar het goud de lucht in gaat; via-punten in de luchtroutes. ZRH is de
    // grote inkomende trechter naar de Ticino-raffinage.
    { id: "au-air-zrh", type: "airport", name: "Zürich (ZRH)", country: "Zwitserland", lat: 47.46, lon: 8.55, tier: 2, note: "De inkomende trechter → weg/spoor naar Ticino." },
    { id: "au-air-lhr", type: "airport", name: "Londen (LHR)", country: "VK", lat: 51.47, lon: -0.46, tier: 2, note: "Naar LBMA / Bank of England-kluis." },
    { id: "au-air-jfk", type: "airport", name: "New York (JFK)", country: "VS", lat: 40.64, lon: -73.78, tier: 2, note: "Naar COMEX / NY Fed." },
    { id: "au-air-dxb", type: "airport", name: "Dubai (DXB)", country: "VAE", lat: 25.25, lon: 55.36, tier: 2, note: "Afrika-corridor + doorvoer naar India." },
    { id: "au-air-hkg", type: "airport", name: "Hongkong (HKG)", country: "Hongkong", lat: 22.31, lon: 113.92, tier: 2, note: "Conduit → Shanghai (China in)." },
    { id: "au-air-sin", type: "airport", name: "Singapore (SIN)", country: "Singapore", lat: 1.36, lon: 103.99, tier: 2, note: "Aziatische kluishub." },
    { id: "au-air-bom", type: "airport", name: "Mumbai (BOM)", country: "India", lat: 19.09, lon: 72.87, tier: 2, note: "Grootste sieraden-invoer." },
    { id: "au-air-del", type: "airport", name: "Delhi (DEL)", country: "India", lat: 28.56, lon: 77.10, tier: 3, note: "Invoer + MMTC-PAMP." },
    { id: "au-air-per", type: "airport", name: "Perth (PER)", country: "Australië", lat: -31.94, lon: 115.97, tier: 2, note: "Uitgang Australië (bij Perth Mint)." },
    { id: "au-air-jnb", type: "airport", name: "Johannesburg (JNB)", country: "Zuid-Afrika", lat: -26.13, lon: 28.24, tier: 2, note: "Afrika-gateway." },
    { id: "au-air-acc", type: "airport", name: "Accra (ACC)", country: "Ghana", lat: 5.60, lon: -0.17, tier: 3, note: "West-Afrika-gateway." },
    { id: "au-air-gru", type: "airport", name: "São Paulo (GRU)", country: "Brazilië", lat: -23.43, lon: -46.47, tier: 3, note: "Zuid-Amerika-gateway." },
    { id: "au-air-yyz", type: "airport", name: "Toronto (YYZ)", country: "Canada", lat: 43.68, lon: -79.63, tier: 3, note: "Uitgang Canada." },
    { id: "au-air-ist", type: "airport", name: "Istanbul (IST)", country: "Turkije", lat: 41.26, lon: 28.74, tier: 3, note: "Sieraden + spil naar het Midden-Oosten." },

    // --------------------------------------------- HANDELS- & KLUISHUBS
    { id: "au-hub-london", type: "hub", name: "Londen (LBMA + Bank of England)", country: "VK", lat: 51.514, lon: -0.088, tier: 1, note: "Prijsbenchmark; BoE-kluis (custodie); het OTC-hart van de goudmarkt." },
    { id: "au-hub-ny", type: "hub", name: "New York (COMEX + NY Fed)", country: "VS", lat: 40.71, lon: -74.01, tier: 1, note: "Futures-benchmark; NY Fed bewaart buitenlands centralebankgoud." },
    { id: "au-hub-zurich", type: "hub", name: "Zürich", country: "Zwitserland", lat: 47.37, lon: 8.54, tier: 1, note: "Grootbanken + kluizen, naast de Ticino-raffinage." },
    { id: "au-hub-shanghai", type: "hub", name: "Shanghai (SGE)", country: "China", lat: 31.23, lon: 121.47, tier: 1, note: "De put: goud stroomt China in, niet uit." },
    { id: "au-hub-dubai", type: "hub", name: "Dubai (DMCC)", country: "VAE", lat: 25.07, lon: 55.14, tier: 2, note: "Spil Afrika ↔ India; 'grijs' goud wordt hier wit." },
    { id: "au-hub-singapore", type: "hub", name: "Singapore", country: "Singapore", lat: 1.29, lon: 103.85, tier: 2, note: "Aziatische kluishub / doorvoer." },
    { id: "au-hub-hongkong", type: "hub", name: "Hongkong", country: "Hongkong", lat: 22.32, lon: 114.17, tier: 2, note: "Conduit naar Shanghai (China in)." },

    // ------------------------------------------------------------- CONSUMPTIE
    { id: "au-mkt-india", type: "market", name: "India (sieraden)", country: "India", lat: 19.08, lon: 72.88, tier: 1, note: "Grootste sieraden- + beleggingsvraag (via Mumbai/Delhi)." },
    { id: "au-mkt-china", type: "market", name: "China (sieraden + belegging)", country: "China", lat: 22.55, lon: 114.06, tier: 1, note: "Wereldgrootste vraag; sieradenfabricage rond Shenzhen." },
    { id: "au-mkt-turkije", type: "market", name: "Turkije (sieraden)", country: "Turkije", lat: 41.01, lon: 28.98, tier: 2, note: "Sieraden + inflatie-belegging." },
    { id: "au-mkt-me", type: "market", name: "Midden-Oosten (Dubai-souk)", country: "VAE", lat: 25.27, lon: 55.30, tier: 2, note: "Sieradenconsumptie." },
    { id: "au-mkt-tech", type: "market", name: "Tech (Japan/Korea/Taiwan)", country: "Japan", lat: 35.18, lon: 136.90, tier: 3, note: "Elektronica — klein aandeel." },
    { id: "au-mkt-west", type: "market", name: "Westerse belegging (baren/munten)", country: "Duitsland", lat: 48.14, lon: 11.58, tier: 3, note: "Duitsland/VS — fysieke belegging." },

    // --------------------------------------------------------------- RECYCLING
    { id: "au-rec-italie", type: "recycler", name: "Arezzo/Vicenza (sieraadschroot)", country: "Italië", lat: 43.46, lon: 11.88, tier: 2, note: "Europees sieraadcentrum → Zwitserse raffinage." },
    { id: "au-rec-india", type: "recycler", name: "India (schroot)", country: "India", lat: 28.65, lon: 77.23, tier: 3, note: "Terug via MMTC-PAMP." },
    { id: "au-rec-me", type: "recycler", name: "Midden-Oosten/Turkije (schroot)", country: "VAE", lat: 25.00, lon: 55.05, tier: 3, note: "Terug via Dubai." },

    // ------------------------------------- CENTRALE BANKEN (optionele laag)
    // type "cb" -> alleen zichtbaar met de CB-toggle. `reserve` (t) = node-grootte.
    { id: "au-cb-us", type: "cb", name: "Fed (Fort Knox e.a. + NY Fed)", country: "VS", lat: 37.13, lon: -85.95, reserve: 8130, tier: 1, note: "Veruit grootste; bewaart ook buitenlands goud (NY Fed)." },
    { id: "au-cb-de", type: "cb", name: "Bundesbank (Frankfurt)", country: "Duitsland", lat: 50.11, lon: 8.68, reserve: 3350, tier: 1, note: "Repatrieerde 2013-17 uit New York/Parijs." },
    { id: "au-cb-it", type: "cb", name: "Banca d'Italia (Rome)", country: "Italië", lat: 41.90, lon: 12.50, reserve: 2450, tier: 2, note: "" },
    { id: "au-cb-fr", type: "cb", name: "Banque de France (Parijs)", country: "Frankrijk", lat: 48.86, lon: 2.35, reserve: 2440, tier: 2, note: "" },
    { id: "au-cb-ru", type: "cb", name: "Bank Rusland (Moskou)", country: "Rusland", lat: 55.75, lon: 37.62, reserve: 2330, tier: 2, note: "Absorbeert de eigen mijnproductie." },
    { id: "au-cb-cn", type: "cb", name: "PBoC (Beijing)", country: "China", lat: 39.90, lon: 116.40, reserve: 2280, tier: 1, note: "Koopt gestaag door; waarschijnlijk ondergerapporteerd." },
    { id: "au-cb-ch", type: "cb", name: "SNB (Bern)", country: "Zwitserland", lat: 46.95, lon: 7.44, reserve: 1040, tier: 2, note: "" },
    { id: "au-cb-jp", type: "cb", name: "Bank of Japan (Tokio)", country: "Japan", lat: 35.686, lon: 139.77, reserve: 846, tier: 3, note: "" },
    { id: "au-cb-in", type: "cb", name: "RBI (Delhi)", country: "India", lat: 28.61, lon: 77.21, reserve: 880, tier: 1, note: "Repatrieerde 100+ t uit de Bank of England (2024)." },
    { id: "au-cb-nl", type: "cb", name: "DNB (Amsterdam)", country: "Nederland", lat: 52.37, lon: 4.90, reserve: 612, tier: 3, note: "Grootste deel al thuis/NY." },
    { id: "au-cb-pl", type: "cb", name: "NBP (Warschau)", country: "Polen", lat: 52.23, lon: 21.01, reserve: 450, tier: 1, note: "Grootste koper 2024 (+90 t); repatrieerde 2019 uit Londen." },
    { id: "au-cb-tr", type: "cb", name: "CBRT (Ankara)", country: "Turkije", lat: 39.93, lon: 32.86, reserve: 600, tier: 2, note: "Wisselt tussen koper en verkoper (binnenlandse dynamiek)." },
  ],

  flows: [
    // ---- 1. MIJN-DORÉ → RAFFINAGE (stage erts) — de convergentie op Ticino ----
    { from: "au-boddington", to: "au-ref-perth", value: 27, mode: "air", stage: "erts", via: ["au-air-per"] },
    { from: "au-cadia", to: "au-ref-perth", value: 24, mode: "air", stage: "erts", via: ["au-air-per"] },
    { from: "au-kalgoorlie", to: "au-ref-perth", value: 15, mode: "air", stage: "erts", via: ["au-air-per"] },
    { from: "au-lihir", to: "au-ref-perth", value: 18, mode: "air", stage: "erts", via: ["au-air-per"], note: "PNG → Perth Mint." },
    { from: "au-tarkwa", to: "au-ref-valcambi", value: 17, mode: "air", stage: "erts", via: ["au-air-acc", "au-air-zrh"], note: "West-Afrika → Ticino." },
    { from: "au-obuasi", to: "au-ref-valcambi", value: 11, mode: "air", stage: "erts", via: ["au-air-acc", "au-air-zrh"] },
    { from: "au-loulo", to: "au-ref-argor", value: 20, mode: "air", stage: "erts", via: ["au-air-acc", "au-air-zrh"], note: "Mali industrieel → Ticino." },
    { from: "au-mponeng", to: "au-ref-rand", value: 8, mode: "air", stage: "erts", via: ["au-air-jnb"], note: "Zuid-Afrika → Rand Refinery." },
    { from: "au-detour", to: "au-ref-rcm", value: 22, mode: "air", stage: "erts", via: ["au-air-yyz"], note: "Canada domestic." },
    { from: "au-malartic", to: "au-ref-valcambi", value: 22, mode: "air", stage: "erts", via: ["au-air-yyz", "au-air-zrh"], note: "Deels naar Zwitserland." },
    { from: "au-nevada", to: "au-ref-valcambi", value: 30, mode: "air", stage: "erts", via: ["au-air-jfk", "au-air-zrh"], note: "Deel naar CH; het meeste blijft domestic (Metalor/Asahi US)." },
    { from: "au-penasquito", to: "au-ref-pamp", value: 16, mode: "air", stage: "erts", via: ["au-air-zrh"], note: "Mexico → Ticino." },
    { from: "au-paracatu", to: "au-ref-argor", value: 15, mode: "air", stage: "erts", via: ["au-air-gru", "au-air-zrh"], note: "Brazilië → Ticino." },
    { from: "au-yanacocha", to: "au-ref-valcambi", value: 10, mode: "air", stage: "erts", via: ["au-air-gru", "au-air-zrh"], note: "Peru → Ticino." },
    { from: "au-grasberg", to: "au-ref-china", value: 40, mode: "air", stage: "erts", via: ["au-air-hkg"], note: "Indonesisch koper-goud → deels China." },
    { from: "au-shandong", to: "au-ref-china", value: 100, mode: "rail", stage: "erts", note: "China insulair (binnenlands)." },
    { from: "au-sudan", to: "au-ref-dubai", value: 20, mode: "air", stage: "erts", via: ["au-air-dxb"], note: "Artisanaal/'grijs' goud → Dubai." },
    // (Olimpiada/Muruntau/Kazachstan = insulair: geen boog naar buiten. Zie de CB-laag.)

    // ---- 2. GERAFFINEERDE BAREN → HUBS (stage raffinaat) — uitwaaieren uit CH ----
    { from: "au-ref-valcambi", to: "au-hub-london", value: 300, mode: "air", stage: "raffinaat", via: ["au-air-zrh", "au-air-lhr"], note: "ZRH → LHR → LBMA/BoE." },
    { from: "au-ref-valcambi", to: "au-hub-ny", value: 150, mode: "air", stage: "raffinaat", via: ["au-air-zrh", "au-air-jfk"], note: "→ COMEX/NY." },
    { from: "au-ref-valcambi", to: "au-hub-hongkong", value: 200, mode: "air", stage: "raffinaat", via: ["au-air-zrh", "au-air-hkg"], note: "→ Hongkong, conduit China." },
    { from: "au-ref-argor", to: "au-hub-dubai", value: 120, mode: "air", stage: "raffinaat", via: ["au-air-zrh", "au-air-dxb"] },
    { from: "au-ref-pamp", to: "au-hub-singapore", value: 80, mode: "air", stage: "raffinaat", via: ["au-air-zrh", "au-air-sin"] },
    { from: "au-ref-metalor", to: "au-hub-zurich", value: 60, mode: "rail", stage: "raffinaat", note: "Neuchâtel → Zürich (kort, over land)." },
    { from: "au-ref-perth", to: "au-hub-london", value: 120, mode: "air", stage: "raffinaat", via: ["au-air-per", "au-air-lhr"], note: "Australische baren → Londen." },
    { from: "au-ref-rand", to: "au-hub-london", value: 150, mode: "air", stage: "raffinaat", via: ["au-air-jnb", "au-air-lhr"], note: "Zuid-Afrikaanse baren → Londen." },
    { from: "au-ref-rcm", to: "au-hub-ny", value: 20, mode: "air", stage: "raffinaat", via: ["au-air-yyz", "au-air-jfk"] },
    { from: "au-ref-dubai", to: "au-hub-dubai", value: 60, mode: "road", stage: "raffinaat", note: "Raffinaderij → DMCC-handelshub (kort)." },

    // ---- 3. INTERBANCAIRE KLUISSTROMEN hub↔hub (stage raffinaat) ----
    { from: "au-hub-london", to: "au-hub-zurich", value: 250, mode: "air", stage: "raffinaat", via: ["au-air-lhr", "au-air-zrh"], note: "Londen ↔ Zürich, de klassieke as." },
    { from: "au-hub-zurich", to: "au-hub-ny", value: 120, mode: "air", stage: "raffinaat", via: ["au-air-zrh", "au-air-jfk"], note: "Arbitrage/EFP naar COMEX." },
    { from: "au-hub-london", to: "au-hub-ny", value: 200, mode: "air", stage: "raffinaat", via: ["au-air-lhr", "au-air-jfk"], note: "2024-25 grote fysieke verschuiving Londen → New York." },
    { from: "au-hub-hongkong", to: "au-hub-shanghai", value: 250, mode: "air", stage: "raffinaat", note: "Hongkong → Shanghai: China in, eenrichting." },

    // ---- 4. HUB → CONSUMPTIE / CHINA-PUT (stage product) ----
    { from: "au-hub-shanghai", to: "au-mkt-china", value: 250, mode: "rail", stage: "product", note: "SGE → sieradenfabricage (binnenlands)." },
    { from: "au-ref-china", to: "au-mkt-china", value: 120, mode: "rail", stage: "product", note: "Binnenlands geraffineerd → sieraden." },
    { from: "au-hub-london", to: "au-mkt-india", value: 200, mode: "air", stage: "product", via: ["au-air-lhr", "au-air-bom"], note: "Londen → India sieraden." },
    { from: "au-hub-dubai", to: "au-mkt-india", value: 180, mode: "air", stage: "product", via: ["au-air-dxb", "au-air-bom"], note: "Dubai → India-corridor." },
    { from: "au-hub-dubai", to: "au-mkt-me", value: 120, mode: "road", stage: "product", note: "Souk-consumptie." },
    { from: "au-ref-mmtc", to: "au-mkt-india", value: 150, mode: "rail", stage: "product", note: "Binnenlands geraffineerd → sieraden." },
    { from: "au-hub-zurich", to: "au-mkt-turkije", value: 90, mode: "air", stage: "product", via: ["au-air-zrh", "au-air-ist"], note: "Turkije sieraden." },
    { from: "au-ref-japan", to: "au-mkt-tech", value: 40, mode: "road", stage: "product", note: "Tech-goud." },
    { from: "au-ref-valcambi", to: "au-mkt-west", value: 120, mode: "rail", stage: "product", note: "Beleggingsbaren/-munten Europa." },

    // ---- 5. RECYCLING → RAFFINAGE (stage erts, feedstock terug) ----
    { from: "au-rec-italie", to: "au-ref-valcambi", value: 120, mode: "road", stage: "erts", note: "Arezzo/Vicenza-schroot → Ticino." },
    { from: "au-rec-india", to: "au-ref-mmtc", value: 100, mode: "rail", stage: "erts", note: "India-schroot." },
    { from: "au-rec-me", to: "au-ref-dubai", value: 90, mode: "road", stage: "erts", note: "Midden-Oosten/Turkije-schroot → Dubai." },

    // ---- 6. CENTRALE-BANK-LAAG (layer: "cb" -> alleen met de toggle) ----
    { from: "au-hub-london", to: "au-cb-pl", value: 90, mode: "air", stage: "raffinaat", layer: "cb", via: ["au-air-lhr"], note: "Polen: grootste koper 2024 (+90 t) + repatriëring." },
    { from: "au-hub-london", to: "au-cb-in", value: 100, mode: "air", stage: "raffinaat", layer: "cb", via: ["au-air-lhr", "au-air-del"], note: "India repatrieerde 100+ t uit de Bank of England (2024)." },
    { from: "au-hub-zurich", to: "au-cb-tr", value: 20, mode: "air", stage: "raffinaat", layer: "cb", via: ["au-air-zrh", "au-air-ist"], note: "Turkije (netto wisselend)." },
    { from: "au-olimpiada", to: "au-cb-ru", value: 44, mode: "air", stage: "raffinaat", layer: "cb", note: "Rusland absorbeert de eigen mijnproductie." },
    { from: "au-shandong", to: "au-cb-cn", value: 30, mode: "rail", stage: "raffinaat", layer: "cb", note: "PBoC accumuleert binnenlands." },
  ],

  // Spanningen (paneel "Knelpunten & spanningen") — de goud-invulling.
  tensions: [
    { id: "au-t-ticino", type: "concentratie", title: "Raffinage-trechter Zwitserland",
      metric: "~65-70% van het wereldgoud door Zwitserse raffinage (Ticino)",
      note: "Winning top-1 ≈ 3% (China); raffinage knijpt samen in vier huizen in Ticino (Valcambi/Argor/PAMP) + Metalor. De kwetsbaarheid zit één stap ná het graven — precies zoals bij lithium, maar dan institutioneel i.p.v. via een zeestraat.",
      lat: 45.85, lon: 9.0,
      nodes: ["au-ref-valcambi", "au-ref-argor", "au-ref-pamp", "au-ref-metalor", "au-air-zrh"],
      flows: ["au-tarkwa>au-ref-valcambi", "au-malartic>au-ref-valcambi", "au-nevada>au-ref-valcambi", "au-loulo>au-ref-argor"] },
    { id: "au-t-china", type: "knelpunt", title: "China: eenrichtings-put",
      metric: "goud stroomt via Hongkong → Shanghai China in; nauwelijks export",
      note: "Chinees mijngoud blijft binnenlands én de wereld levert bij via Hongkong. Pijlen naar binnen, niets naar buiten.",
      lat: 27.0, lon: 118.0,
      nodes: ["au-hub-hongkong", "au-hub-shanghai", "au-mkt-china", "au-ref-china"],
      flows: ["au-hub-hongkong>au-hub-shanghai", "au-hub-shanghai>au-mkt-china"] },
    { id: "au-t-cb", type: "beleid", title: "Centrale banken kopen door",
      metric: "+1.045 t in 2024 (Polen ~90 t voorop); India repatrieerde uit Londen",
      note: "Recordinkopen sinds 2022. Nuance: veel 'koop' is titeloverdracht ín een kluis (blijft in Londen/NY); sommigen repatriëren fysiek (Polen 2019, India 2024). Zet de CB-laag aan om voorraden + stromen te zien.",
      lat: 52.23, lon: 21.01,
      nodes: ["au-cb-pl", "au-cb-in", "au-cb-cn", "au-cb-us"],
      flows: ["au-hub-london>au-cb-pl", "au-hub-london>au-cb-in"] },
    { id: "au-t-dubai", type: "beleid", title: "Dubai & het 'grijze' goud",
      metric: "artisanaal/gesmokkeld goud (o.a. Sudan) wordt via Dubai verhandeld",
      note: "Een groot deel van het Afrikaanse artisanale goud reist buiten de officiële kanalen om via Dubai de markt op — moeilijk te traceren.",
      lat: 25.1, lon: 55.2,
      nodes: ["au-sudan", "au-ref-dubai", "au-hub-dubai"],
      flows: ["au-sudan>au-ref-dubai"] },
  ],
});
