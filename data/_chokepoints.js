// _chokepoints.js — UNIVERSELE routepunten op zee, gedeeld door alle grondstoffen.
//
// Twee soorten:
//
//  1. KNELPUNTEN (marker: true, standaard) — echte flessenhalzen: zeestraten,
//     kanalen, kapen. Krijgen een gouden ring op de kaart, zijn aanklikbaar,
//     en grondstoffen verwijzen ernaar in hun `tensions`.
//
//  2. VAARPUNTEN (marker: false) — géén knelpunt, puur navigatie. Ze houden de
//     route op het water. Zonder deze punten trekt de atlas de kortste lijn
//     over de bol, en die loopt vrolijk dwars over Zuid-Amerika of Australië.
//     Berucht geval: Chili → China is bijna exact antipodaal, waardoor "de
//     kortste route" wiskundig onbepaald wordt en de lijn alle kanten op schiet.
//     Vandaar de Pacific-vaarpunten.
//
// Elke grondstof gebruikt ze via `via: ["wp-..."]` in zijn flows.

const WAYPOINTS = {};

function REGISTER_WAYPOINTS(list) {
  list.forEach((wp) => {
    if (wp.marker === undefined) wp.marker = true;
    WAYPOINTS[wp.id] = wp;
  });
}

REGISTER_WAYPOINTS([
  // ======================================================= ECHTE KNELPUNTEN
  { id: "wp-malakka", name: "Straat van Malakka", kind: "zeestraat",
    lat: 3.0, lon: 100.6,
    note: "Kortste zeeroute tussen de Indische Oceaan en Oost-Azië; ±30% van de wereldhandel over zee. Alles wat uit Afrika, het Midden-Oosten, Europa of Zuid-Amerika-via-de-Kaap naar China gaat, vaart hier doorheen. Alternatieven (Sunda, Lombok) kosten dagen extra." },

  { id: "wp-lombok", name: "Straat van Lombok", kind: "zeestraat",
    lat: -8.70, lon: 115.85,
    note: "De diepwaterdoorgang tussen Bali en Lombok. Grote bulkschepen uit West-Australië naar Oost-Azië nemen deze route (niet Malakka): korter, dieper, minder druk." },

  { id: "wp-makassar", name: "Straat van Makassar", kind: "zeestraat",
    lat: -2.00, lon: 118.50,
    note: "Vervolg op Lombok, tussen Borneo en Sulawesi, richting de Zuid-Chinese Zee. Samen met Lombok de standaardroute voor Australische bulk naar China." },

  { id: "wp-taiwan", name: "Straat van Taiwan", kind: "zeestraat",
    lat: 24.60, lon: 119.60,
    note: "Aanvoerroute naar de Chinese oostkusthavens (Ningbo, Shanghai) én het geopolitiek meest beladen water ter wereld. Escalatie hier raakt vrijwel elke grondstofketen tegelijk." },

  { id: "wp-suez", name: "Suezkanaal", kind: "kanaal",
    lat: 30.50, lon: 32.35,
    note: "Kortste route Azië–Europa. Kwetsbaar gebleken: één dwarsliggend schip (2021) of onveiligheid in de Rode Zee legt de route stil en dwingt om te varen via Kaap de Goede Hoop (+10–14 dagen)." },

  { id: "wp-bab", name: "Bab el-Mandeb", kind: "zeestraat",
    lat: 12.60, lon: 43.40,
    note: "De zuidelijke poort van de Rode Zee, en dus van Suez. Wie hier niet door kan, kan Suez ook niet gebruiken — precies wat er tijdens de Rode Zee-crisis gebeurde." },

  { id: "wp-hormuz", name: "Straat van Hormuz", kind: "zeestraat",
    lat: 26.60, lon: 56.50,
    note: "De flessenhals van de Perzische Golf: ±een vijfde van alle olie ter wereld. Geen omvaaralternatief; alleen beperkte pijpleidingcapaciteit eromheen." },

  { id: "wp-panama", name: "Panamakanaal", kind: "kanaal",
    lat: 9.10, lon: -79.70,
    note: "Verbindt de Pacifische kust van Amerika met de Atlantische markten. Werkt op zoetwater uit stuwmeren: bij droogte gaat de capaciteit omlaag — een klimaatgevoelig knelpunt." },

  { id: "wp-kaap", name: "Kaap de Goede Hoop", kind: "kaap",
    lat: -35.20, lon: 19.50,
    note: "De omweg-route wanneer Suez onbruikbaar is, en de standaardroute voor veel bulk van Zuid-Amerika en zuidelijk Afrika naar Azië. Geen fysieke vernauwing, wel een structureel kostenpunt." },

  { id: "wp-gibraltar", name: "Straat van Gibraltar", kind: "zeestraat",
    lat: 35.95, lon: -5.60,
    note: "Toegangspoort tot de Middellandse Zee en dus tot Zuid-Europese havens en het Suezkanaal." },

  { id: "wp-bosporus", name: "Bosporus", kind: "zeestraat",
    lat: 41.10, lon: 29.05,
    note: "Enige uitgang van de Zwarte Zee; relevant voor graan, olie en metalen uit de Zwarte Zee-regio." },

  { id: "wp-deense-straten", name: "Deense Straten", kind: "zeestraat",
    lat: 56.00, lon: 11.30,
    note: "Sont en Grote Belt: de enige toegang tot de Oostzee. Al het kobalt naar de Finse raffinaderij in Kokkola gaat hierdoorheen." },

  { id: "wp-dover", name: "Nauw van Calais", kind: "zeestraat",
    lat: 51.00, lon: 1.50,
    note: "De Straat van Dover: de drukst bevaren zeestraat ter wereld en de korte weg tussen de Noordzee en de Atlantische Oceaan. In een grof raster is hij te smal en valt dicht — dan varen schepen van Antwerpen of Rotterdam 'per ongeluk' noordelijk om Schotland heen. Water forceren houdt het Kanaal open. (De Kanaaltunnel eronder blijft als landverbinding bestaan voor de trein.)" },

  // LANDKNELPUNT — geen zeestraat maar een grenspost. Let op het id: dit begint
  // bewust NIET met "wp-", en `kind: "grensovergang"` zorgt dat searoute.js hem
  // op de LANDkaart openhoudt in plaats van er water te stempelen.
  { id: "grens-kasumbalesa", name: "Kasumbalesa", kind: "grensovergang",
    lat: -12.22, lon: 27.79,
    note: "De grenspost tussen Congo en Zambia. Vrijwel al het kobalt op weg naar Durban wringt zich hierdoorheen — kilometers vrachtwagens, wachttijden van dagen tot weken. Het knelpunt van deze keten ligt niet op zee, maar op een landweg in Centraal-Afrika." },

  // ============================================ VAARPUNTEN (geen knelpunt)
  // Puur om de route op het water te houden. Geen marker, geen paneel.
  { id: "wp-aceh", name: "Noordwest-Sumatra", kind: "vaarpunt", marker: false,
    lat: 5.60, lon: 95.00,
    note: "Aanloop naar de Straat van Malakka vanuit de Indische Oceaan." },

  { id: "wp-singapore", name: "Straat van Singapore", kind: "vaarpunt", marker: false,
    lat: 1.25, lon: 104.10,
    note: "Uitgang van Malakka richting de Zuid-Chinese Zee." },

  { id: "wp-scs", name: "Zuid-Chinese Zee", kind: "vaarpunt", marker: false,
    lat: 9.00, lon: 116.00,
    note: "Open water tussen Borneo en Vietnam; alle Oost-Aziatische aanvoer komt hier samen." },

  { id: "wp-rode-zee", name: "Rode Zee", kind: "vaarpunt", marker: false,
    lat: 20.00, lon: 38.50,
    note: "Tussen Bab el-Mandeb en Suez; de zee is smal, de route ligt vast." },

  { id: "wp-atl-brazilie", name: "Voor de Braziliaanse kust", kind: "vaarpunt", marker: false,
    lat: -6.00, lon: -33.00,
    note: "Buiten de oostpunt van Brazilië om, richting het Caribisch gebied." },

  { id: "wp-pac-zuid", name: "Zuidelijke Stille Oceaan", kind: "vaarpunt", marker: false,
    lat: -26.00, lon: -125.00,
    note: "Open water tussen Zuid-Amerika en Oceanië." },

  { id: "wp-pac-west", name: "Westelijke Stille Oceaan", kind: "vaarpunt", marker: false,
    lat: 3.00, lon: 143.00,
    note: "Open water ten noorden van Papoea, aanloop naar Oost-Azië." },

  { id: "wp-pac-noord", name: "Noordelijke Stille Oceaan", kind: "vaarpunt", marker: false,
    lat: 44.00, lon: 175.00,
    note: "De grote-cirkelroute Oost-Azië – Noord-Amerika loopt hoog over de noordelijke Stille Oceaan." },

  { id: "wp-zuid-australie", name: "Zuid van Australië", kind: "vaarpunt", marker: false,
    lat: -41.00, lon: 140.00,
    note: "Schepen van West-Australië naar Amerika varen zuid om het continent heen — niet eroverheen." },

  { id: "wp-moz-noord", name: "Noord van Madagaskar", kind: "vaarpunt", marker: false,
    lat: -11.50, lon: 44.50,
    note: "Uitgang van het Kanaal van Mozambique richting de Indische Oceaan." },

  { id: "wp-atl-west", name: "Westelijke Atlantische Oceaan", kind: "vaarpunt", marker: false,
    lat: 14.00, lon: -55.00,
    note: "Open water tussen Brazilië en het Caribisch gebied." },

  // Saint-Laurent: Montréal ligt ~1.500 km landinwaarts, de rivier is smaller dan
  // een rastercel. Een kettinkje kleine open-water-schijfjes (eigen `openRadius`)
  // maakt de zeeweg bevaarbaar tot Montréal, zonder elders land te doorbreken.
  // Cabot Strait -> golf -> estuarium -> Québec -> Montréal.
  { id: "wp-cabot", name: "Cabot Strait", kind: "vaarpunt", marker: false,
    lat: 47.60, lon: -59.80,
    note: "De ingang van de Golf van Saint-Laurent, tussen Newfoundland en Nova Scotia." },

  { id: "wp-st-laurent-1", name: "Golf van Saint-Laurent", kind: "vaarpunt", marker: false,
    lat: 48.80, lon: -64.60 },

  { id: "wp-st-laurent-2", name: "Saint-Laurent (estuarium)", kind: "vaarpunt", marker: false,
    lat: 47.80, lon: -69.60, openRadius: 0.8 },

  { id: "wp-st-laurent-2b", name: "Saint-Laurent (Île d'Orléans)", kind: "vaarpunt", marker: false,
    lat: 47.25, lon: -70.50, openRadius: 0.8 },

  { id: "wp-st-laurent-3", name: "Saint-Laurent (Québec)", kind: "vaarpunt", marker: false,
    lat: 46.70, lon: -71.60, openRadius: 0.8 },

  { id: "wp-st-laurent-4", name: "Saint-Laurent (Montréal)", kind: "vaarpunt", marker: false,
    lat: 45.80, lon: -73.20, openRadius: 0.7 },
]);

// ============================================================================
// LANDVERBINDINGEN — de omgekeerde truc.
//
// Voor zeeroutes moeten we water forceren waar het raster een straat dichtslibt
// (Lombok, Suez). Voor LÁNDroutes is het precies andersom: er zijn plekken waar
// treinen en vrachtwagens over water gaan — bruggen en tunnels — en die zijn in
// een raster van 0,25° onzichtbaar.
//
// Zonder de Öresundbrug zou een trein van Bitterfeld naar Skellefteå helemaal
// om de Oostzee heen moeten kruipen, via Polen, de Baltische staten en Finland.
// Met deze lijst bestaat de brug.
const LAND_LINKS = [
  { id: "ll-oresund", name: "Øresundbrug", lat: 55.60, lon: 12.85,
    note: "Kopenhagen–Malmö: de spoorverbinding tussen het vasteland en Zweden." },
  { id: "ll-store-baelt", name: "Storebæltbrug", lat: 55.34, lon: 11.03,
    note: "Verbindt Funen met Seeland; onderdeel van dezelfde Deense spoorbrug-keten." },
  { id: "ll-fehmarn", name: "Fehmarnbelt", lat: 54.55, lon: 11.30,
    note: "Duitsland–Denemarken; nu veerboot, straks tunnel." },
  { id: "ll-kanaaltunnel", name: "Kanaaltunnel", lat: 51.00, lon: 1.50,
    note: "Calais–Folkestone: de enige spoorverbinding tussen het vasteland en Groot-Brittannië." },
  { id: "ll-bosporus", name: "Bosporusbruggen", lat: 41.08, lon: 29.05,
    note: "Istanbul: waar het spoor van Europa naar Azië oversteekt (Marmaray-tunnel)." },
];
