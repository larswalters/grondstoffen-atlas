// Grafiet — losse grondstof-module.
// Werk dit bestand bij om locaties en stromen voor grafiet te verfijnen.
// Cijfers zijn indicatief (o.a. USGS Mineral Commodity Summaries). Nog niet gedetailleerd uitgewerkt.
REGISTER({
  id: "graphite", name: "Grafiet", symbol: "C",
  color: "#8B95A5",
  detail: "basis", // "basis" = automatisch overgezet, "uitgewerkt" = handmatig verrijkt
  blurb: "Anodemateriaal in vrijwel elke lithium-ionbatterij. China leidt in zowel natuurlijk als synthetisch grafiet.",
  nodes: [
    { id: "graphite-china", type: "mine", name: "China", country: "China", lat: 45, lon: 127, share: 24, note: "Heilongjiang — grootste vlokgrafiet-reserves" },
    { id: "graphite-mozambique", type: "mine", name: "Mozambique", country: "Mozambique", lat: -14.5, lon: 40.5, share: 18, note: "Snel groeiende exportmijnen" },
    { id: "graphite-brazilie", type: "mine", name: "Brazilië", country: "Brazilië", lat: -18, lon: -43.5, share: 8, note: "Minas Gerais/Bahia" },
    { id: "graphite-madagaskar", type: "mine", name: "Madagaskar", country: "Madagaskar", lat: -19.5, lon: 47, share: 6, note: "Kwaliteitsvlokgrafiet" },
    { id: "graphite-tanzania", type: "mine", name: "Tanzania", country: "Tanzania", lat: -6.5, lon: 37, share: 6, note: "Diverse nieuwe projecten" },
    { id: "graphite-noorwegen", type: "mine", name: "Noorwegen", country: "Noorwegen", lat: 69.5, lon: 17.3, share: 2, note: "Skaland — hoogwaardig vlokgrafiet" },
    { id: "graphite-oekraine", type: "mine", name: "Oekraïne", country: "Oekraïne", lat: 48.4, lon: 35, share: 3, note: "Zavalievsky — Europees grafiet" },
    { id: "graphite-ref-china", type: "refinery", name: "China", country: "China", lat: 36.6, lon: 114.5, note: "Verwerking tot batterij-anodemateriaal (synthetisch + natuurlijk)" },
    { id: "graphite-ref-japan", type: "refinery", name: "Japan", country: "Japan", lat: 35, lon: 137, note: "Synthetisch grafiet, hoge zuiverheid" },
    { id: "graphite-ref-zweden", type: "refinery", name: "Zweden", country: "Zweden", lat: 58.4, lon: 15.6, note: "Talga (Luleå-regio) — batterij-anodemateriaal EU" },
  ],
  flows: [
    { from: "graphite-china", to: "graphite-ref-china", value: 10, note: "China → China" },
    { from: "graphite-china", to: "graphite-ref-japan", value: 10, note: "China → Japan" },
    { from: "graphite-noorwegen", to: "graphite-ref-zweden", value: 10, note: "Noorwegen → Zweden" },
  ],
});
