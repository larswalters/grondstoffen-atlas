# Routebrief (licht) · Goud · Van → Via → Naar (land)

**stroom-id:** `goud-ity-ticino` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 4) ·
**status:** gebakken
**Keten in één zin:** goud-doré van de Ity-mijn (Endeavour Mining, West-Ivoorkust) per truck naar de
vrachtterminal van Abidjan Félix-Houphouët-Boigny (ABJ), per beveiligde vrachtvlucht (grootcirkel) naar
de vrachtterminal van Zürich Airport (ZRH), en per truck over de A2/Gotthard-as naar de
Valcambi-raffinaderij in Balerna (Ticino).
**Welke as van het verhaal:** West-Afrika (Ivoorkust) → Zwitserland (Ticino) — reserve-as (M31 golf 4),
vergelijkbaar profiel als `goud-loulo-ticino` (Mali). Ity is Endeavour Minings grootste mijn: 2024-piek
343.000 oz Au (~10,7 t), 2025-gids 290.000–330.000 oz, gerealiseerd ≈319.000 oz (~9,9 t Au) [1][2].

## 1 · Ketenkaart
```
Ity-mijn, verwerkingsinstallatie (Endeavour Mining) `au-ity-mijn`
  ──(b1 truck · Zouan-Hounien–Man–Daloa–Yamoussoukro-corridor · ~600 km)──►
Abidjan (ABJ), vrachtterminal `au-abidjan-vrachtterminal`
  ──(b2 lucht · vlucht ABJ → ZRH, grootcirkel, aannemelijk · ~4.840 km)──►
Zürich Airport vrachtterminal (ZRH) `au-zrh-vrachtterminal` (hergebruikt uit goud-loulo-ticino.md)
  ──(b3 truck · A2/Gotthard-as via Bellinzona–Lugano–Chiasso · ~200 km)──►
Valcambi-raffinaderij, Balerna `au-ref-valcambi` (hergebruikt) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Ity-mijn → Abidjan (ABJ) vrachtterminal | mijnweg → Zouan-Hounien → Man → Daloa → Yamoussoukro → Abidjan | hemelsbreed via-punten-som ≈594 km [berekend], geen wegkm [ontwerp ≈600 km; rechte lijn 480–497 km, mindat[3]/berekend] | maak_stroombeen_weg | nee |
| b2 | B | lucht | Abidjan (ABJ) → Zürich (ZRH) | vrachtvlucht ABJ → ZRH (grootcirkel) | ≈4.840 [berekend]; ontwerp ≈4.750 hemelsbreed | maak_luchtbeen | nee — doorgetrokken (aannemelijk: geen bron bevestigt déze specifieke lading; West-Afrikaanse doré-export naar Zwitserse raffinaderijen is industriestandaard, zie §7 en `goud-loulo-ticino.md`) |
| b3 | C | truck | Zürich vrachtterminal (ZRH) → Valcambi, Balerna | A2 Gotthard-as via Bellinzona–Lugano–Chiasso | ≈200 [ontwerp]; hemelsbreed 184,1 [berekend, uit `goud-loulo-ticino.md`] | maak_stroombeen_weg — **letterlijke kopie**, zie §7/bak-aanwijzing | ja, kort last-mile-stukje ZRH-platform → openbaar net (airside), zie §7 |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-ity-mijn` | mijn / laadplek | Ity-mijn, verwerkingsinstallatie (Endeavour Mining, Zouan-Hounien Department, Tonkpi) | 6.8830, -8.1195 | [1][2][osm] | bron-gelegd (z16 gezien: gebouwencluster/verwerkingsinstallatie direct naast een tailings-/waterbekken (blauw-groen), tussen de mijnwegen en open pits van het Ity-complex) |
| `au-abidjan-vrachtterminal` | overslag / lucht | Abidjan Félix-Houphouët-Boigny Int'l (ABJ), cargo-apron W van de startbaan | 5.2628, -3.9298 | [4][osm] | bron-gelegd (z17 gezien: apron met meerdere geparkeerde vrachtvliegtuigen, gebouwencluster direct W ervan en een grote container-/voertuigopslag verder ZW — welk specifiek pand de vrachtafhandelaar (SAGA e.d.) is, is op dit beeld niet te onderscheiden) |
| `au-zrh-vrachtterminal` | overslag / lucht | Zürich Airport vrachtplatform (hergebruikt uit `goud-loulo-ticino.md` / `pgm-springs-zurich.md`, M31 golf 3) | 47.4647, 8.5492 | [loulo-brief] | bron-gelegd (satellietblik al gedaan in `goud-loulo-ticino.md`: vrachtplatform met vrachttoestellen naast een rechthoekig loodsgebouw, O van de hoofdterminal — zelfde fysieke site) |
| `au-ref-valcambi` | losplek / raffinaderij | Valcambi SA, Via Passeggiata 3, Zona Industriale Pian Faloppia, Balerna | 45.8385, 9.0051 | [loulo-brief] | bron-gelegd (hergebruikt uit `goud-loulo-ticino.md`: industrieel gebouwencomplex met zonnepanelendak, direct N van de spoorbundel Balerna-Chiasso) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Zouan-Hounien (departementshoofdstad, ~15 km van Ity [3]) | 6.9198, -8.2089 | de mijnweg sluit hier aan op de regionale doorgaande weg; sluit een directe zuidroute via Guiglo/Soubré uit |
| b1 | 2 | Man (regionale corridorknoop, Tonkpi/Montagnes) | 7.4103, -7.5504 | de route buigt hier oostwaarts richting Daloa; grootste stad op de westelijke corridor |
| b1 | 3 | Daloa (corridorknoop, Haut-Sassandra) | 6.8869, -6.4530 | doorgaande verbindingsweg Man–Yamoussoukro |
| b1 | 4 | Yamoussoukro (hoofdstad, corridorknoop naar Abidjan) | 6.8200, -5.2776 | laatste grote knoop vóór de A1/snelweg-aanloop naar Abidjan |
| b3 | 1–3 | Bellinzona / Lugano / Chiasso | zie `goud-loulo-ticino.md` §4 | identiek aan de b3-via-punten in `goud-loulo-ticino.md` (zelfde ankers, zelfde A2-corridor) — letterlijke kopie, zie §7 |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Valcambi (Balerna) | Valcambi SA (Rajesh Exports) | doré/ruw goud → LBMA-baren | 's werelds grootste goudraffinaderij, cap. ≈2.000 t/j (v1-register) | [loulo-brief][v1] |

## 6 · Stoppunt
De brief stopt bij Valcambi: fase D (afnemer van de geraffineerde baren) is niet gebrond — Valcambi
levert aan een brede, niet-herleidbare afname (kluizen/hubs wereldwijd); geen bron koppelt déze
Ivoorkust-doré aan één specifieke vervolgbestemming. Fase E vervalt.

## 7 · Open punten
- **Reserve-as (M31 golf 4):** deze keten is bewust een reserve met een vergelijkbaar profiel als
  `goud-loulo-ticino` (Mali); de haalbaarheidstoets vraagt geen aanpassing en geen probleem-oplossing —
  alleen bouwen zoals ontworpen.
- **Tongon-mijn (Barrick) niet gebruikt:** de ontwerp-as noemde Ity/Endeavour én Tongon/Barrick als
  alternatieve bronmijnen; deze brief kiest Ity (matcht de stroom-id `goud-ity-ticino`). Tongon (Barrick,
  Noord-Ivoorkust) blijft een aparte, niet-getekende kandidaat.
- **b2-vlucht is aannemelijk, niet chain-specifiek bevestigd:** geen bron bevestigt een specifieke
  ABJ→ZRH-vrachtvlucht voor Ity-doré; West-Afrikaanse doré-export naar Zwitserse raffinaderijen is
  industriestandaard (zelfde redenering als `goud-loulo-ticino.md` voor Mali) en Abidjan heeft
  bevestigde directe luchtvrachtverbindingen richting Zürich [4]. Geen tussenlanding gebrond → één
  directe vlucht.
- **b1-via-punten zijn indicatief** (bekende corridorsteden, niet zelf OSM-wegvertex-geverifieerd binnen
  het webbudget) — de bak-agent routeert over het OSM-wegnet, dus de exacte ligging volgt uit die
  routering. Geen gepubliceerde wegkilometer gevonden binnen het webbudget; de ontwerp-schatting
  (≈600 km) ligt dicht bij de som van de hemelsbrede via-punt-segmenten (≈594 km), wat de gekozen
  corridor aannemelijk maakt maar geen wegkm-bron is.
- **Abidjan-vrachtterminal is site-niveau, niet pand-niveau** — het beeld op z17 toont een cargo-apron
  met vliegtuigen en een gebouwencluster, maar welk specifiek pand de vrachtafhandelaar is (SAGA/Bolloré
  e.d.) is niet te onderscheiden op dit beeld.
- **b3 (ZRH → Valcambi) is een LETTERLIJKE KOPIE-kandidaat:** identieke ankers (47.4647,8.5492 →
  45.8385,9.0051) en identieke corridor als in `goud-loulo-ticino.md` (en `goud-yanacocha-ticino.md`).
  Die eerdere twee brieven bakten dit been elk apart opnieuw (eigen geojson-bestandsnaam) i.p.v. het
  letterlijk te hergebruiken — dat is een afwijking van de eigen projectregel ("gedeeld been = letterlijke
  kopie") die ik hier meld maar niet zelf herstel (ik raak alleen mijn eigen bestanden). **Aanbeveling
  voor de bak-agent van déze keten:** hergebruik letterlijk `goud-loulo-ticino-weg-zrh-valcambi.geojson`
  (en de bijbehorende airside-stippel 47.4647,8.5492 → 47.472087,8.554523) via `--been-geojson`/`--stippel`
  met verwijzing naar dat bestand, in plaats van een derde keer dezelfde route te scannen.

## 8 · Bronnen
[1] Ecofin Agency, 2026 — "How Côte d'Ivoire's Oldest Mine Became Endeavour Mining's Top Gold Producer": Ity-productie piekte op 343.000 oz in 2024; 2025-gids 290.000–330.000 oz. https://www.ecofinagency.com/news/2311-50737-how-cote-d-ivoire-s-oldest-mine-became-endeavour-mining-s-top-gold-producer
[2] Endeavour Mining plc — Ity mine, portfolio-pagina (grootste mijn van de groep). https://www.endeavourmining.com/our-portfolio/ity-mine/
[3] Mindat.org — "Ity mine, Zouan-Hounien Department, Tonkpi, Montagnes, Ivory Coast": 15 km van Zouan-Hounien; 480 km west-noordwest van Abidjan (rechte lijn). https://www.mindat.org/loc-245063.html
[4] Stravex — "Freight forwarding Ivory Coast, by air & sea transport": directe luchtvrachtverbindingen Abidjan (ABJ) via o.a. Zürich, Frankfurt, Parijs, Amsterdam. https://www.stravex.com/en/freight-transport-ivorycoast
[osm] OpenStreetMap (ODbL) via Nominatim — Mine d'Or d'Ity −8,1155514/6,8530835 · Aéroport International Félix Houphouët-Boigny −3,9259573/5,2649283 · Zouan-Hounien −8,2089154/6,9198246 · Man −7,5503719/7,4102584 · Daloa −6,4529859/6,8869233 · Yamoussoukro −5,2776034/6,8200066. https://www.openstreetmap.org
[loulo-brief] `v2/design/routebrieven/goud-loulo-ticino.md` (M31 golf 3, zelfde golffamilie) — hergebruikte ankers `au-zrh-vrachtterminal` (47,4647/8,5492) en `au-ref-valcambi` (45,8385/9,0051), zelf satelliet-gelegd/hergebruikt in die brief; b3-corridor (A2/Gotthard, Bellinzona–Lugano–Chiasso) en de airside-stippel-oplossing eveneens hergebruikt.
[v1] `data/goud.js` — au-ref-valcambi capaciteit ≈2.000 t/j; World Gold Council/USGS/LBMA/Metals Focus (zie `design/goud.md`).
Satellietblik: `v2/build-cache/satcheck/sat-goud-ity-ticino-itymijn-plant.png`,
`sat-goud-ity-ticino-abidjan-cargo.png` (Esri z16–z17, 2026-09-28); ZRH/Valcambi hergebruikt uit
`goud-loulo-ticino.md` (geen nieuwe satellietblik nodig).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 4)

**Stroomroute:** `v2/data/stroomroute-goud-ity-ticino.json` (228,7 KB · versie 2 · punt_formaat lonlat) ·
**4 benen · 5.806,3 km · 12.385 punten · 4 markers · 0 naden (alle < 0,001 km).**

| # | fase | modaliteit | been | km | naad met vorige |
|---|---|---|---|---|---|
| b1 | A | truck | Ity-mijn → Abidjan (ABJ) vrachtterminal | 695,4 | 0,000 |
| b2 | B | lucht | vlucht ABJ → ZRH (grootcirkel, aannemelijk) | 4.841,6 | 0,000 |
| b3-stippel | C | truck | ZRH-vrachtplatform last mile (airside, identiek aan goud-loulo-ticino) | 0,9 | 0,000 |
| b3 | C | truck | ZRH-vrachtplatform → Valcambi, Balerna (A2/Gotthard, letterlijke kopie) | 268,4 | 0,000 |

**Recept:** `bak_goud_ity_ticino()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh goud-ity-ticino`).
- b1: nieuw profiel `goud-ity-ticino-ity-abidjan` in `v2/tools/maak_stroombeen_weg.py` (PROFIELEN),
  gescand met `--bron geofabrik` op extract `ivoorkust` (aanwezig).
- b2: `python v2/tools/maak_luchtbeen.py --van "Abidjan (ABJ)|5.2628,-3.9298" --naar "Zürich (ZRH)|47.4647,8.5492"`.
- b3-stippel + b3: **letterlijk hergebruikt** uit `goud-loulo-ticino` — het geojson-bestand
  `goud-loulo-ticino-weg-zrh-valcambi.geojson` is 1-op-1 gekopieerd naar
  `goud-ity-ticino-weg-zrh-valcambi.geojson` (geen tweede scan gedraaid), met dezelfde
  airside-last-mile-stippel (47,4647/8,5492 → 47,472087/8,554523, 0,914 km).

**Toelichting per bevinding:**
- **b1 (695,0–695,4 km tegen de venster-referentie ~600 km, +15,8%): BEVINDING, geen harde ±15%-
  toets.** De brief geeft geen gepubliceerde wegkm (webbudget uitgeput) — alleen een ontwerp-
  schatting (≈600 km) en een hemelsbreed via-punten-som (≈594 km), beide expliciet als indicatie
  gemarkeerd (routebrief §2/§7). `vensterKm` stond daarom ruim (75) en de router heeft zelf de
  ligging over het OSM-wegnet bepaald; geen via-punt bijgeschoven om een getal te halen. Acht
  keerlussen gesnoeid (708,7 → 695,0 km).
- **b1 knikken/spikes**: 30 knikken ≥60°, waarvan 2 "omkeringen" (≥150°) en **0 terugloop** — de
  echte reparatiedrempel. Alle 30 zijn OSM-scanartefacten (spikes <100 m) of echte scherpe
  bochten in het wegennet (geen lus die de lijn ter plaatse laat blijven staan).
- **b2 (4.841,6 km tegen ≈4.840 km berekend)**: binnen de meetnauwkeurigheid van een grootcirkel —
  geen bevinding. Geen km-toets van toepassing (§5 van de handleiding: een luchtbeen ís de
  grootcirkel per constructie).
- **b3-stippel (0,914 km, airside)**: identiek aan het precedent in `goud-loulo-ticino` — hetzelfde
  fysieke ZRH-vrachtplatform kent geen aansluiting op het openbare net.
- **b3 (268,4 km tegen de "≈200 km [ontwerp]" uit de brief-samenvatting)**: de geometrie is een
  letterlijke kopie van `goud-loulo-ticino`s b3-been (die zelf al op 268,4 km meet — het "≈200 km"
  in de brief-samenvatting was een vroege ontwerpschatting, niet de gemeten lengte van het
  hergebruikte been); hemelsbreed 184,1 km (routebrief §2) klopt met de A2/Gotthard-omweg.
  Geen bevinding: dit is per ontwerp dezelfde lijn als het reeds gevalideerde precedent.
- **Markers**: alle vier ankers liggen op 0,000 km van hun lijn (routeerpunt = anker op elk
  uiteinde).
- **Naden**: alle vier overgangen tussen benen 0,000 km — geen haven-aanloop nodig (geen zeebeen
  in deze keten).

**Lessen / bevindingen voor het rapport (geen eigen bestanden gewijzigd buiten deze stroom):**
- **b3 in `goud-loulo-ticino.md`/`goud-yanacocha-ticino.md` volgde de eigen "gedeeld been =
  letterlijke kopie"-regel niet** (elke brief bakte het ZRH→Valcambi-been apart, met een eigen
  geojson-bestandsnaam voor exact dezelfde route) — hier gecorrigeerd door letterlijk te kopiëren
  in plaats van opnieuw te scannen; niet zelf hersteld in de bestaande brieven (raakt alleen eigen
  bestanden).
- **Geen wegkm-bron voor b1 gevonden binnen het webbudget** — een toekomstige golf zou een
  Ivoiriaanse overheids- of bedrijfsopgave (bijv. een corridorlengte Man–Daloa–Yamoussoukro) kunnen
  opzoeken om de ±15%-norm alsnog hard te maken.

**Registerregel voor `main.js`** (centraal, niet door deze bak-agent zelf toe te voegen):
`{ sleutel: "goud-ity-ticino", bestand: "stroomroute-goud-ity-ticino.json", aan: true }`
