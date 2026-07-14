// Platinagroepmetalen — losse grondstof-module.
// Werk dit bestand bij om locaties en stromen voor platinagroepmetalen te verfijnen.
// Cijfers zijn indicatief (o.a. USGS Mineral Commodity Summaries). Nog niet gedetailleerd uitgewerkt.
REGISTER({
  id: "pgm", name: "Platinagroepmetalen", symbol: "PGM",
  color: "#D8D2C4",
  detail: "basis", // "basis" = automatisch overgezet, "uitgewerkt" = handmatig verrijkt
  blurb: "Platina, palladium, rodium: katalysatoren en elektrolyse. Zuid-Afrika bezit het overgrote deel van de reserves.",
  nodes: [
    { id: "pgm-zuid-afrika", type: "mine", name: "Zuid-Afrika", country: "Zuid-Afrika", lat: -25.5, lon: 27.5, share: 83, note: "Bushveld Complex — verreweg dominant wereldwijd" },
    { id: "pgm-rusland", type: "mine", name: "Rusland", country: "Rusland", lat: 69.3, lon: 88.2, share: 10, note: "Norilsk — palladium als bijproduct van nikkel" },
    { id: "pgm-zimbabwe", type: "mine", name: "Zimbabwe", country: "Zimbabwe", lat: -18.9, lon: 30, share: 4, note: "Great Dyke" },
    { id: "pgm-finland", type: "mine", name: "Finland", country: "Finland", lat: 68, lon: 27, share: 1, note: "Kevitsa/Portimo — kleine EU-PGM-bron" },
    { id: "pgm-canada", type: "mine", name: "Canada", country: "Canada", lat: 47, lon: -84, share: 2, note: "Ontario — palladium bij nikkel" },
    { id: "pgm-ref-zuid-afrika", type: "refinery", name: "Zuid-Afrika", country: "Zuid-Afrika", lat: -25.8, lon: 27.8, note: "Rustenburg — smelters en raffinaderijen" },
    { id: "pgm-ref-rusland", type: "refinery", name: "Rusland", country: "Rusland", lat: 69.3, lon: 88.2, note: "Norilsk Nickel-raffinage" },
    { id: "pgm-ref-finland", type: "refinery", name: "Finland", country: "Finland", lat: 61.3, lon: 22.1, note: "Harjavalta — PGM-recovery" },
    { id: "pgm-ref-vk", type: "refinery", name: "VK", country: "VK", lat: 51.4, lon: -2.4, note: "Johnson Matthey (Royston/Swindon) — katalysator/PGM" },
  ],
  flows: [
    { from: "pgm-zuid-afrika", to: "pgm-ref-zuid-afrika", value: 10, note: "Zuid-Afrika → Zuid-Afrika" },
    { from: "pgm-finland", to: "pgm-ref-finland", value: 10, note: "Finland → Finland" },
    { from: "pgm-finland", to: "pgm-ref-vk", value: 10, note: "Finland → VK" },
  ],
});
