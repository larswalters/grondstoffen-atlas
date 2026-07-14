// Nikkel — losse grondstof-module.
// Werk dit bestand bij om locaties en stromen voor nikkel te verfijnen.
// Cijfers zijn indicatief (o.a. USGS Mineral Commodity Summaries). Nog niet gedetailleerd uitgewerkt.
REGISTER({
  id: "nickel", name: "Nikkel", symbol: "Ni",
  color: "#A3A3A3",
  detail: "basis", // "basis" = automatisch overgezet, "uitgewerkt" = handmatig verrijkt
  blurb: "Roestvrij staal en batterijkathodes. Indonesië heeft binnen tien jaar de markt naar zich toe getrokken.",
  nodes: [
    { id: "nickel-indonesie", type: "mine", name: "Indonesië", country: "Indonesië", lat: -2.5, lon: 121, share: 44, note: "Sulawesi — dominant dankzij exportban op ruw erts" },
    { id: "nickel-australie", type: "mine", name: "Australië", country: "Australië", lat: -28, lon: 122, share: 15, note: "Lateriet- en sulfide-ertsen" },
    { id: "nickel-brazilie", type: "mine", name: "Brazilië", country: "Brazilië", lat: -19.5, lon: -43, share: 12, note: "Lateriet in Minas Gerais/Pará" },
    { id: "nickel-rusland", type: "mine", name: "Rusland", country: "Rusland", lat: 69.3, lon: 88.2, share: 7, note: "Norilsk — sulfide-erts" },
    { id: "nickel-filipijnen", type: "mine", name: "Filipijnen", country: "Filipijnen", lat: 9.3, lon: 123.3, share: 5, note: "Lateriet, exporteert vooral ruw erts" },
    { id: "nickel-finland", type: "mine", name: "Finland", country: "Finland", lat: 63.7, lon: 27.2, share: 3, note: "Terrafame Sotkamo — batterijnikkel" },
    { id: "nickel-griekenland", type: "mine", name: "Griekenland", country: "Griekenland", lat: 38.7, lon: 23.3, share: 1, note: "Larco — lateriet, historisch EU-nikkel" },
    { id: "nickel-canada", type: "mine", name: "Canada", country: "Canada", lat: 46.5, lon: -81, share: 3, note: "Sudbury — sulfide-erts" },
    { id: "nickel-ref-indonesie", type: "refinery", name: "Indonesië", country: "Indonesië", lat: -1.3, lon: 121.6, note: "Morowali/Weda Bay — Chinees-gefinancierde smelters" },
    { id: "nickel-ref-china", type: "refinery", name: "China", country: "China", lat: 25, lon: 102.7, note: "Nikkel-ruwijzer- en batterijchemie" },
    { id: "nickel-ref-canada", type: "refinery", name: "Canada", country: "Canada", lat: 46.5, lon: -81, note: "Sudbury — traditionele nikkelraffinage" },
    { id: "nickel-ref-finland", type: "refinery", name: "Finland", country: "Finland", lat: 61.3, lon: 22.1, note: "Harjavalta (Nornickel) — batterijnikkel EU" },
    { id: "nickel-ref-noorwegen", type: "refinery", name: "Noorwegen", country: "Noorwegen", lat: 58.15, lon: 8, note: "Nikkelverk Kristiansand — hoogzuivere raffinage" },
  ],
  flows: [
    { from: "nickel-indonesie", to: "nickel-ref-indonesie", value: 10, note: "Indonesië → Indonesië" },
    { from: "nickel-filipijnen", to: "nickel-ref-china", value: 10, note: "Filipijnen → China" },
    { from: "nickel-finland", to: "nickel-ref-finland", value: 10, note: "Finland → Finland" },
    { from: "nickel-finland", to: "nickel-ref-noorwegen", value: 10, note: "Finland → Noorwegen" },
  ],
});
