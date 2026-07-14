// Zeldzame aardmetalen — losse grondstof-module.
// Werk dit bestand bij om locaties en stromen voor zeldzame aardmetalen te verfijnen.
// Cijfers zijn indicatief (o.a. USGS Mineral Commodity Summaries). Nog niet gedetailleerd uitgewerkt.
REGISTER({
  id: "rare-earths", name: "Zeldzame aardmetalen", symbol: "REE",
  color: "#C9A227",
  detail: "basis", // "basis" = automatisch overgezet, "uitgewerkt" = handmatig verrijkt
  blurb: "17 elementen voor magneten, windturbines en elektronica. China beheerst zowel winning als scheiding.",
  nodes: [
    { id: "rare-earths-china", type: "mine", name: "China", country: "China", lat: 41.77, lon: 109.98, share: 48, note: "Bayan Obo, Binnen-Mongolië — grootste REE-mijn ter wereld" },
    { id: "rare-earths-vietnam", type: "mine", name: "Vietnam", country: "Vietnam", lat: 22.3, lon: 103.1, share: 15, note: "Lai Chau/Lao Cai" },
    { id: "rare-earths-brazilie", type: "mine", name: "Brazilië", country: "Brazilië", lat: -19.6, lon: -46.9, share: 14, note: "Araxá en omgeving" },
    { id: "rare-earths-rusland", type: "mine", name: "Rusland", country: "Rusland", lat: 60, lon: 90, share: 5, note: "Diverse, nog beperkt ontgonnen" },
    { id: "rare-earths-india", type: "mine", name: "India", country: "India", lat: 17, lon: 82, share: 5, note: "Kustzand-monaziet" },
    { id: "rare-earths-vs", type: "mine", name: "VS", country: "VS", lat: 35.48, lon: -115.53, share: 2, note: "Mountain Pass, Californië" },
    { id: "rare-earths-zweden", type: "mine", name: "Zweden", country: "Zweden", lat: 67.85, lon: 20.2, share: 2, note: "Per Geijer/Kiruna — grootste bekende REE-vondst EU" },
    { id: "rare-earths-noorwegen", type: "mine", name: "Noorwegen", country: "Noorwegen", lat: 59.28, lon: 9.25, share: 1, note: "Fen-complex — REE-project" },
    { id: "rare-earths-groenland", type: "mine", name: "Groenland", country: "Groenland", lat: 60.9, lon: -46, share: 3, note: "Kvanefjeld/Kringlerne — grote reserves" },
    { id: "rare-earths-ref-china", type: "refinery", name: "China", country: "China", lat: 25.85, lon: 114.93, note: "Ganzhou, Jiangxi — wereldcentrum voor scheiding/raffinage" },
    { id: "rare-earths-ref-china-2", type: "refinery", name: "China", country: "China", lat: 40.65, lon: 109.82, note: "Baotou — magneetproductie" },
    { id: "rare-earths-ref-maleisie", type: "refinery", name: "Maleisië", country: "Maleisië", lat: 3.8, lon: 103.3, note: "Lynas Kuantan — grootste scheidingsfabriek buiten China" },
    { id: "rare-earths-ref-estland", type: "refinery", name: "Estland", country: "Estland", lat: 59.4, lon: 27.7, note: "Silmet Sillamäe — enige REE-scheiding in EU" },
    { id: "rare-earths-ref-frankrijk", type: "refinery", name: "Frankrijk", country: "Frankrijk", lat: 46.16, lon: -1.15, note: "La Rochelle (Solvay) — REE-raffinage" },
  ],
  flows: [
    { from: "rare-earths-vietnam", to: "rare-earths-ref-china", value: 10, note: "Vietnam → China" },
    { from: "rare-earths-china", to: "rare-earths-ref-china-2", value: 10, note: "China → China" },
    { from: "rare-earths-vietnam", to: "rare-earths-ref-maleisie", value: 10, note: "Vietnam → Maleisië" },
    { from: "rare-earths-zweden", to: "rare-earths-ref-estland", value: 10, note: "Zweden → Estland" },
    { from: "rare-earths-noorwegen", to: "rare-earths-ref-frankrijk", value: 10, note: "Noorwegen → Frankrijk" },
  ],
});
