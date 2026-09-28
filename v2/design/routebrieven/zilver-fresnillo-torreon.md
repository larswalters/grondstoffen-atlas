# Routebrief (licht) · zilver — Fresnillo/Saucito → Torreón (Mexico)

**stroom-id:** `zilver-fresnillo-torreon` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken (2026-09-28)
**Keten in één zin:** zilverdoré/-concentraat van het Fresnillo/Saucito-mijnencomplex (Fresnillo plc, Zacatecas)
per **truck** (~270 km hemelsbreed, ~331 km over de weg) naar de Met-Mex Peñoles-raffinaderij in Torreón
(Industrias Peñoles) — **stoppunt** (de raffinaderij ís de bestemming van het ontwerp; geen fase D/E).
**Welke as van het verhaal:** *Mexico-binnenlandse as* — 's werelds grootste primaire zilverbedrijf naar
's werelds grootste zilverraffinaderij, over land binnen één land (jaarvolume ≈1.048 t Ag/j, Fresnillo plc
jaarverslag 2024/2025 [1][6]).

## 1 · Ketenkaart
```
Fresnillo/Saucito-mijnencomplex `ag-fresnillo-mijn` ──(b1 truck · Fed 45/45D → 40D/49D via Río Grande –
   Cuencamé – Ciudad Lerdo · 331 km webcheck / 270 km hemelsbreed)──► Met-Mex Peñoles-raffinaderij
   `ag-penoles-torreon` (Torreón, Coahuila) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Fresnillo/Saucito-mijnencomplex → Met-Mex Peñoles-raffinaderij | MEX 45/45D (Fresnillo–Río Grande) → MEX 40D/49D (Cuencamé–Ciudad Lerdo–Torreón) [5] | 331 [5, webcheck route-planner] (hemelsbreed 270, geen bedrijfs-/overheidsopgave binnen budget) | maak_stroombeen_weg (extract `mexico`, groot venster i.v.m. de afstand) | nee — corridor + relatie zijn goed gebrond (Fresnillo plc AR24, 99,6% van de productie naar Peñoles' Met-Mex [1]), lijn wordt gemeten en doorgetrokken |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-fresnillo-mijn` | mijn / plant (laad) | Fresnillo/Saucito-mijnencomplex (Fresnillo plc, Zacatecas) | 23.1580, -102.8600 | [6][8] | bron-gelegd — hergebruik letterlijk van `w-fresnillo-saucito` (`v2/design/zilver-sitelaag.json`), zelf al satelliet z14→z16 gelegd: tailings-/plantcomplex NW van Fresnillo-stad (23.156–23.166, -102.855…-102.862) |
| `ag-penoles-torreon` | raffinaderij (los, stoppunt) | Met-Mex Peñoles-raffinaderij (Industrias Peñoles, Torreón, Coahuila) | 25.5278, -103.4417 | [2][3][4][8] | bron-gelegd (dit ronde vernieuwd: z16 gezien op 25.5278,-103.4417 — aaneengesloten industrieel complex met tanks, een donkere bezink-/tailingsvijver en spooraansluiting direct ZW van het centrum van Torreón; verschoven van de vroegere stadscentroïde 25.5500,-103.4200 die in de bebouwde kom viel — OSM landuse=industrial "Met-Mex Peñoles", way 116771096, bbox 25.5219–25.5338/-103.4456…-103.4368) |

## 4 · Via-punten (b1 — de truckweg heeft een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Río Grande (Zacatecas) | 23.8269, -103.0338 | eerste grote plaats noordwaarts vanaf de mijn; corridorkeuze tussen de doorgaande Fed 45/45D en lokale zijwegen [5][9] |
| b1 | 2 | Cuencamé (Durango) | 24.8700, -103.6978 | draaischijf waar de corridor van Fed 45/45D overgaat op Fed 40D/49D richting La Laguna; ligt zelf aan de "Carretera Durango–Torreón" [5][9] |
| b1 | 3 | Ciudad Lerdo (Durango) | 25.5366, -103.5252 | laatste plaats vóór Torreón, in de La Laguna-conurbatie (Gómez Palacio–Lerdo–Torreón) [5][9] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Met-Mex Peñoles-raffinaderij (Torreón) | Industrias Peñoles | doré/concentraat (Fresnillo, Peñasquito e.a. Mexicaanse mijnen) → good-delivery zilverbaren + lood/zink | ≈1.800 t Ag/j, "'s werelds grootste zilverraffinaderij" (bedrijfsopgave) | [2][6] |

## 6 · Stoppunt
De brief stopt bij de Met-Mex Peñoles-raffinaderij: het ketenontwerp noemt geen vervolgstap (geen fase D/E),
de raffinaderij ís de eindbestemming van deze as, en de zilverdoré wordt daar tot good-delivery baren verwerkt.

## 7 · Open punten
- **Geen gepubliceerde exacte wegkilometer binnen budget** — alleen een route-planner webcheck (331 km,
  mejoresrutas.com, geen bedrijfs-/overheidsopgave) en de hemelsbreed-afstand (270 km). De ±15%-toets geldt
  hier als **indicatie**, niet als harde norm (haalbaarheidstoets-punt 1); de bak-agent kan bij het bakken
  alsnog een echte bedrijfs-/overheidsopgave zoeken.
- **Welk deel van de 1.048 t Ag/j precies via déze truckcorridor gaat, is niet op zendingsniveau bevestigd** —
  Fresnillo plc's jaarverslag 2024 zegt dat 99,6% van de productie naar Peñoles' Met-Mex-complex gaat voor
  smelten/raffineren [1], wat de relatie en de bestemming Torreón goed onderbouwt, maar geen aparte
  ladingscijfers per corridor geeft.
- **Drie via-punten zijn OSM-plaatsnodes, geen wegprojectie** — de bak-agent projecteert ze op de doorgaande
  MEX 45/45D-/40D-/49D-corridor met `maak_stroombeen_weg.py` (venster ruim genomen i.v.m. de afstand van
  ~270 km).
- **Exacte laadplek binnen het Fresnillo/Saucito-complex niet apart bevestigd** — het hergebruikte sitelaag-
  anker is het zichtbare plant-/tailingscomplex (satellietblik van een eerdere ronde), geen aparte poort-
  coördinaat.

## 8 · Bronnen
[1] Fresnillo plc, Annual Report and Accounts 2024 — tijdens 2024 werd 99,6% van de productie verkocht aan
    Peñoles' metallurgisch complex Met-Mex voor smelten en raffineren (websearch-samenvatting van het rapport).
    https://www.fresnilloplc.com/media/gf3fqvci/fresnillo-financial-statements-ar24-web.pdf
[2] Industrias Peñoles, "Metals" (corporate site) — Met-Mex Peñoles Torreón: loodsmelter + lood-zilver-
    raffinaderij + elektrolytische zinkfabriek; grootste zilverraffinaderij ter wereld.
    https://www.penoles.com.mx/en/our-operations/metals.html
[3] Wikipedia (en), "Met-Mex Peñoles" — locatiebeschrijving Torreón, Coahuila, Mexico.
    https://en.wikipedia.org/wiki/Met-Mex_Pe%C3%B1oles
[4] OpenStreetMap/Nominatim — landuse=industrial "Met-Mex Peñoles" (way 116771096), Torreón, bbox
    25.5219–25.5338 / -103.4456…-103.4368. https://nominatim.openstreetmap.org/
[5] mejoresrutas.com, "Distancia Fresnillo → Torreón" — 331 km wegroute via Río Grande, Cuencamé, La Lomas/
    Ciudad Lerdo, MEX 40D/49D (route-planner webcheck, geen bedrijfs-/overheidsopgave).
    https://mx.mejoresrutas.com/distancias/fresnillo-zac-mx/torre%C3%B3n-coa-mx/
[6] v2/design/zilver-sitelaag.json, id `w-fresnillo-saucito` — satelliet z14→z16 gelegd tailings-/plantcomplex
    NW van Fresnillo-stad; capaciteit ≈1.048 t Ag/j (Fresnillo plc jaarverslag 2024/2025, Fresnillo+Saucito-
    district, 33,7 Moz Ag).
[7] C:/automation/Projects/General/grondstoffen-atlas/data/silver.js (v1-register) — oorspronkelijke checklist-
    relatie: Fresnillo-doré → Torreón, Mexico binnenlands (flow ag-fresnillo → ag-ref-penoles).
[8] Esri World Imagery via `v2/tools/sat_check.py` (z16, live) —
    `v2/build-cache/satcheck/sat-zilver-fresnillo-torreon-penoles.png` (nieuw dit ronde) +
    `v2/build-cache/satcheck/sat-sitelaag-zilver-fresnillo{,2,3}.png` (hergebruikt).
[9] Nominatim/OSM plaatsnodes Río Grande (Zacatecas), Cuencamé (Durango), Ciudad Lerdo (Durango) — via-punten
    op de doorgaande MEX 45/45D→40D/49D-corridor. https://nominatim.openstreetmap.org/

## 9 · Bak-noot (2026-09-28, lichte werkwijze, M31 golf 5)

**Eén been (b1, truck, doorgetrokken, geen stippel): 329,1 km / 2.453 punten / 1 been / 5 markers.**
Fresnillo/Saucito-mijnencomplex (23,1580, -102,8600) → Río Grande (23,8269, -103,0338) → Cuencamé
(24,8700, -103,6978) → Ciudad Lerdo (25,5366, -103,5252) → Met-Mex Peñoles-raffinaderij Torreón
(25,5278, -103,4417). Geen zeebeen, geen spoorbeen, geen fase D/E — 100% binnenlands, stoppunt bij
de raffinaderij zoals §6 voorschrijft.

**Recept.** `python v2/tools/maak_stroombeen_weg.py --profiel zilver-fresnillo-torreon-fresnillo-torreon
--bron geofabrik` (extract `mexico`, `vensterKm: 60` i.v.m. de afstand van ~270 km hemelsbreed; de drie
via-punten uit §4 als tussenstops, geprojecteerd op de doorgaande MEX 45/45D-/40D-/49D-corridor —
geen van de drie snapte > 5 km, dus geen wegklasse-correctie nodig). Daarna
`bash v2/tools/bak_stromen.sh zilver-fresnillo-torreon` (functie `bak_zilver_fresnillo_torreon`,
één `--been-geojson` met de vooraf gebakken weglijn).

**KM-toelichting (§7).** De wegscan geeft **328,7 km** (getekende lijn 329,1 km incl. de twee korte
anker-aanlopen). Getoetst tegen het route-planner-webcheck van **331 km** (mejoresrutas.com) =
**-0,7%**, ruim binnen zelfs een harde ±15%-norm — al geldt die toets hier volgens §7 uitsluitend als
**indicatie**, niet als norm, omdat 331 km geen bedrijfs-/overheidsopgave is. De hemelsbrede afstand
(270 km) is niet gebruikt als referentie voor de lengtetoets; de gemeten wegomwegfactor t.o.v.
hemelsbreed is 1,22, een plausibele omwegfactor voor een 270 km-corridor over twee snelwegen met een
draaipunt bij Cuencamé.

**Ankers en aanlopen.** Beide ankers snappen ruim binnen de norm: plant → weg **0,09 km**, weg → kade
**0,31 km** (beide `[OK]`, geen last-mile-stippel nodig — de brief-verwachting "check dit bij het
bakken" komt uit op: geen stippel nodig). De drie via-punten (Río Grande, Cuencamé, Ciudad Lerdo)
snapten alle drie op de doorgaande weg zonder handmatige correctie.

**Stippels/haven-aanlopen/luchtbenen/leiding: geen** — deze keten heeft er geen (geen zeebeen, geen
leiding, geen luchtbeen, zoals de brief al aangaf).

**Toets (handleiding §5).** `toets_knikken.py`: 35 knikken ≥60° (allemaal wegbochten met boogstraal
4–137 m, typisch voor gescande weggeometrie), **0 omkeringen ≥150°, 0 terugloop** — geen fout gevonden.
`toets_rechte_benen.py --min-km 5`: dit been staat NIET in de lijst van verdachte rechte benen (het is
een gemeten, gebogen weglijn, geen omwegfactor ≈1,000). JSON-contract: `versie == 2`,
`punt_formaat == "lonlat"`, modaliteit `truck` ∈ de toegestane set, 1 been met 2.453 punten (≥2),
bestand 53,3 KB (ruim onder de ~300 KB-norm), naad = 0,00 km (enige been, dus alleen de ankersnaps
tellen en die zijn hierboven al gerapporteerd).

**Lessen.** Geen bijzondere lessen — de brief was compleet en de wegscan sloeg direct aan zonder
wegklasse-correcties, stippels of naadproblemen. Enige les die past bij de eerdere golf-4-waarschuwing
(Bingham Canyon → Garfield 100% stippel): deze keten is het spiegelbeeld daarvan — een volledig
doorgetrokken, gemeten wegbeen, wat laat zien dat de "geen stippel-golf" haalbaar is zolang het brief-
onderzoek (hier: drie OSM-plaatsnodes als corridorkeuze, twee satelliet-gelegde ankers) op orde is.

**Registerregel (centraal, main.js):** `{ sleutel: "zilver-fresnillo-torreon", bestand:
"stroomroute-zilver-fresnillo-torreon.json", aan: true }`.
