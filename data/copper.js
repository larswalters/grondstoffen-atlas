// Koper — losse grondstof-module.
// Werk dit bestand bij om locaties en stromen voor koper te verfijnen.
// Cijfers zijn indicatief (o.a. USGS Mineral Commodity Summaries). Nog niet gedetailleerd uitgewerkt.
REGISTER({
  id: "copper", name: "Koper", symbol: "Cu",
  color: "#C87D4A",
  detail: "basis", // "basis" = automatisch overgezet, "uitgewerkt" = handmatig verrijkt
  blurb: "Onmisbaar voor bekabeling, elektromotoren en het elektriciteitsnet. Chili blijft veruit de grootste bron.",
  nodes: [
    { id: "copper-chili", type: "mine", name: "Chili", country: "Chili", lat: -24, lon: -69.3, share: 18, note: "Atacama — Escondida en Chuquicamata" },
    { id: "copper-australie", type: "mine", name: "Australië", country: "Australië", lat: -30, lon: 138, share: 10, note: "O.a. Olympic Dam" },
    { id: "copper-peru", type: "mine", name: "Peru", country: "Peru", lat: -13, lon: -75.5, share: 9, note: "Andes-koperriem" },
    { id: "copper-dr-congo", type: "mine", name: "DR Congo", country: "DR Congo", lat: -10.9, lon: 25.6, share: 8, note: "Katanga — koper-kobalt samen" },
    { id: "copper-rusland", type: "mine", name: "Rusland", country: "Rusland", lat: 69.3, lon: 88.2, share: 8, note: "Norilsk-nikkelbekken" },
    { id: "copper-vs", type: "mine", name: "VS", country: "VS", lat: 32.9, lon: -110, share: 5, note: "Arizona — Morenci e.a." },
    { id: "copper-polen", type: "mine", name: "Polen", country: "Polen", lat: 51.5, lon: 16.2, share: 4, note: "KGHM Lubin — grootste EU-kopermijn" },
    { id: "copper-zweden", type: "mine", name: "Zweden", country: "Zweden", lat: 67.1, lon: 20.9, share: 2, note: "Aitik, Boliden — grootste open kopermijn EU" },
    { id: "copper-ref-china", type: "refinery", name: "China", country: "China", lat: 39, lon: 117.7, note: "Grootste koperraffinagecapaciteit ter wereld" },
    { id: "copper-ref-chili", type: "refinery", name: "Chili", country: "Chili", lat: -22.3, lon: -68.9, note: "Smelters bij de mijnen (Atacama)" },
    { id: "copper-ref-japan", type: "refinery", name: "Japan", country: "Japan", lat: 34, lon: 135.4, note: "Historische raffinage-industrie" },
    { id: "copper-ref-duitsland", type: "refinery", name: "Duitsland", country: "Duitsland", lat: 53.55, lon: 10, note: "Aurubis Hamburg — grootste koperraffinaderij Europa" },
    { id: "copper-ref-polen", type: "refinery", name: "Polen", country: "Polen", lat: 51.2, lon: 16.15, note: "KGHM smelters — Głogów/Legnica" },
  ],
  flows: [
    { from: "copper-rusland", to: "copper-ref-china", value: 10, note: "Rusland → China" },
    { from: "copper-chili", to: "copper-ref-chili", value: 10, note: "Chili → Chili" },
    { from: "copper-rusland", to: "copper-ref-japan", value: 10, note: "Rusland → Japan" },
    { from: "copper-polen", to: "copper-ref-duitsland", value: 10, note: "Polen → Duitsland" },
    { from: "copper-polen", to: "copper-ref-polen", value: 10, note: "Polen → Polen" },
  ],
});
