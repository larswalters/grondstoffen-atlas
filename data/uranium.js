// Uranium — losse grondstof-module.
// Werk dit bestand bij om locaties en stromen voor uranium te verfijnen.
// Cijfers zijn indicatief (o.a. USGS Mineral Commodity Summaries). Nog niet gedetailleerd uitgewerkt.
REGISTER({
  id: "uranium", name: "Uranium", symbol: "U",
  color: "#A3E635",
  detail: "basis", // "basis" = automatisch overgezet, "uitgewerkt" = handmatig verrijkt
  blurb: "Splijtstof voor kernenergie. Kazachstan is met afstand de grootste producent, Canada en Australië volgen.",
  nodes: [
    { id: "uranium-australie", type: "mine", name: "Australië", country: "Australië", lat: -29, lon: 137, share: 28, note: "Grootste bekende reserves ter wereld" },
    { id: "uranium-kazachstan", type: "mine", name: "Kazachstan", country: "Kazachstan", lat: 47.5, lon: 66.9, share: 13, note: "Grootste producent (ISR-winning)" },
    { id: "uranium-canada", type: "mine", name: "Canada", country: "Canada", lat: 58.7, lon: -105, share: 10, note: "Athabasca-bekken, Saskatchewan" },
    { id: "uranium-namibie", type: "mine", name: "Namibië", country: "Namibië", lat: -22.9, lon: 15.2, share: 7, note: "Husab en Rössing" },
    { id: "uranium-oekraine", type: "mine", name: "Oekraïne", country: "Oekraïne", lat: 48.7, lon: 33.6, share: 2, note: "Ingulska — Europees uranium" },
    { id: "uranium-tsjechie", type: "mine", name: "Tsjechië", country: "Tsjechië", lat: 49.7, lon: 15.9, share: 1, note: "Rožná (historisch) — laatste EU-uraanmijn" },
    { id: "uranium-ref-canada", type: "refinery", name: "Canada", country: "Canada", lat: 58.7, lon: -105, note: "Conversie en verrijking nabij de mijnen" },
    { id: "uranium-ref-frankrijk", type: "refinery", name: "Frankrijk", country: "Frankrijk", lat: 45.4, lon: 4.9, note: "Verrijking (Orano)" },
    { id: "uranium-ref-rusland", type: "refinery", name: "Rusland", country: "Rusland", lat: 55, lon: 61.4, note: "Verrijkingscapaciteit (Rosatom)" },
  ],
  flows: [
    { from: "uranium-tsjechie", to: "uranium-ref-frankrijk", value: 10, note: "Tsjechië → Frankrijk" },
    { from: "uranium-kazachstan", to: "uranium-ref-rusland", value: 10, note: "Kazachstan → Rusland" },
  ],
});
