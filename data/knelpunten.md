# Universele knelpunten (gedeeld door alle grondstoffen)

Deze lijst hoort bij `data/_chokepoints.js`. Het zijn de fysieke doorgangen
waar meerdere grondstofketens doorheen moeten. Elke grondstof verwijst ernaar
via `via: ["wp-..."]` in zijn stromen; de grondstof-specifieke toelichting
("waarom is dít knelpunt voor lithium belangrijk") staat in de `tensions`
van de grondstof zelf.

| id | naam | soort | positie | waarom het telt |
|---|---|---|---|---|
| `wp-malakka` | Straat van Malakka | zeestraat | 3.0 N, 100.6 O | ±30% van de wereldhandel over zee. Route voor alles uit Afrika, het Midden-Oosten, Europa en Zuid-Amerika-via-de-Kaap naar China. |
| `wp-lombok` | Straat van Lombok | zeestraat | 8.7 Z, 115.9 O | De diepwaterdoorgang die grote bulkschepen uit West-Australië nemen — **niet** Malakka. |
| `wp-makassar` | Straat van Makassar | zeestraat | 2.0 Z, 118.5 O | Vervolg op Lombok, tussen Borneo en Sulawesi, richting de Zuid-Chinese Zee. |
| `wp-taiwan` | Straat van Taiwan | zeestraat | 24.6 N, 119.6 O | Aanvoer naar Ningbo/Shanghai; geopolitiek meest beladen water ter wereld. |
| `wp-suez` | Suezkanaal | kanaal | 30.5 N, 32.4 O | Kortste route Azië–Europa; omvaren = +10–14 dagen via de Kaap. |
| `wp-bab` | Bab el-Mandeb | zeestraat | 12.6 N, 43.4 O | De zuidpoort van de Rode Zee: wie hier niet door kan, kan Suez niet gebruiken. |
| `wp-hormuz` | Straat van Hormuz | zeestraat | 26.6 N, 56.5 O | ±een vijfde van alle olie; geen omvaaralternatief. |
| `wp-panama` | Panamakanaal | kanaal | 9.1 N, 79.7 W | Pacifisch Amerika ↔ Atlantische markten; capaciteit daalt bij droogte. |
| `wp-kaap` | Kaap de Goede Hoop | kaap | 35.2 Z, 19.5 O | Omweg als Suez dicht is; standaardroute Zuid-Amerika → Azië. |
| `wp-gibraltar` | Straat van Gibraltar | zeestraat | 36.0 N, 5.6 W | Toegang tot de Middellandse Zee. |
| `wp-bosporus` | Bosporus | zeestraat | 41.1 N, 29.1 O | Enige uitgang van de Zwarte Zee. |

## Vaarpunten (géén knelpunt)

Deze staan óók in `_chokepoints.js`, maar met `marker: false`. Ze krijgen geen
gouden ring en staan niet in het spanningen-paneel. Hun enige taak: **de route
op het water houden**. Zonder deze punten trekt de atlas de kortste lijn over
de bol — en die loopt dwars over continenten.

Berucht geval: **Chili → China is bijna exact antipodaal** (de tegenvoeter van
Antofagasta ligt in Zuid-China). Bij antipodale punten is "de kortste route"
wiskundig onbepaald, waardoor de lijn alle kanten op schiet. Vandaar de
Pacific-vaarpunten.

| id | waar | waarvoor |
|---|---|---|
| `wp-aceh` | Noordwest-Sumatra | aanloop naar Malakka vanuit de Indische Oceaan |
| `wp-singapore` | Straat van Singapore | uitgang Malakka → Zuid-Chinese Zee |
| `wp-scs` | Zuid-Chinese Zee | waar alle Oost-Aziatische aanvoer samenkomt |
| `wp-rode-zee` | Rode Zee | tussen Bab el-Mandeb en Suez |
| `wp-pac-zuid` | Zuidelijke Stille Oceaan | Zuid-Amerika → Oceanië |
| `wp-pac-west` | Westelijke Stille Oceaan | ten noorden van Papoea → Oost-Azië |
| `wp-zuid-australie` | Zuid van Australië | om het continent héén, niet eroverheen |
| `wp-moz-noord` | Noord van Madagaskar | uitgang Kanaal van Mozambique |
| `wp-atl-brazilie` | Voor de Braziliaanse kust | om de oostpunt van Brazilië |
| `wp-atl-west` | Westelijke Atlantische Oceaan | Brazilië → Caribisch gebied |

## Gebruik per grondstof

- **Routes worden automatisch gezocht.** De atlas rekent zelf een pad uit dat
  alleen over water gaat (of, voor trein/weg/pijp, alleen over land). Je hoeft
  dus géén punten meer met de hand langs de kust te prikken — alleen de
  knelpunten waar de route dóór moét.
- **Nieuwe grondstof toevoegen:** zet de knelpunt-id's in `via`, en geef havens
  mee. Fabrieken die pál aan de kade staan krijgen `coastal: true`, dan mogen
  ze zelf de zee op zonder aparte haven-node.
- **Ontbreekt er een doorgang** (Straat van Hormuz voor olie, Bab-el-Mandeb
  voor Suez-verkeer)? Toevoegen in `_chokepoints.js`, hier documenteren, klaar.
- **Grondstof-specifieke spanning** (exportverbod, sanctie, concentratie):
  hoort NIET hier maar in de `tensions` van de grondstof, eventueel mét
  verwijzing naar een `wp-*` id.

## Landverbindingen (`LAND_LINKS`)

De omgekeerde truc. Voor zeeroutes forceren we **water** waar het raster een
straat dichtslibt (Lombok, Suez). Voor lándroutes forceren we **land** waar
treinen en vrachtwagens over water gaan — bruggen en tunnels zijn onzichtbaar in
een raster van 0,25°.

Zonder de Øresundbrug zou een trein van Bitterfeld naar Skellefteå helemaal om
de Oostzee heen kruipen, via Polen, de Baltische staten en Finland.

| id | naam | waar | waarom |
|---|---|---|---|
| `ll-oresund` | Øresundbrug | 55.6 N, 12.9 O | Kopenhagen–Malmö: het spoor naar Zweden |
| `ll-store-baelt` | Storebæltbrug | 55.3 N, 11.0 O | Funen–Seeland, zelfde Deense keten |
| `ll-fehmarn` | Fehmarnbelt | 54.6 N, 11.3 O | Duitsland–Denemarken |
| `ll-kanaaltunnel` | Kanaaltunnel | 51.0 N, 1.5 O | de enige spoorlink met Groot-Brittannië |
| `ll-bosporus` | Bosporusbruggen | 41.1 N, 29.1 O | waar het spoor van Europa naar Azië oversteekt |

## Nu in gebruik door

| knelpunt | lithium |
|---|---|
| wp-lombok + wp-makassar | 8 stromen — **al het Australische erts** én het hydroxide naar de VS |
| wp-malakka | 3 stromen — Zimbabwe → China, Brazilië → China, chemie → Europa |
| wp-taiwan | 9 stromen — vrijwel alle aanvoer naar de Chinese oostkust |
| wp-panama | 2 stromen — Chili → VS en Chili → Rotterdam |
| wp-kaap | 1 stroom — Brazilië → China |
| wp-suez + wp-bab | 1 stroom — China → Hongarije |
| ll-oresund e.a. | 1 stroom — Bitterfeld → Skellefteå (spoor over de Oostzee) |

*(tabel aanvullen zodra volgende grondstoffen zijn uitgewerkt)*
