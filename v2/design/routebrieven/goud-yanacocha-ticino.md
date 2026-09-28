# Routebrief (licht) · Goud · Van → Via → Naar (land)

**stroom-id:** `goud-yanacocha-ticino` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** goud-doré van de Yanacocha-mijn (Newmont, Cajamarca) per truck naar de
vrachtterminal van Jorge Chávez Int'l (LIM, Lima), per vrachtvlucht (grootcirkel) naar de
vrachtterminal van Zürich Airport (ZRH), en per truck over de A4/A2-Gotthard-as naar de
Valcambi-raffinaderij in Balerna, Ticino.
**Welke as van het verhaal:** *Zuid-Amerika (Peru) → Zwitserland (Ticino)* — Peruaanse
goud-doré-export gaat structureel per beveiligde luchtvracht vanaf Lima; Valcambi verwerkte naar
verluidt rond 70% van het Yanacocha-goud [8]. Yanacocha produceerde ≈9-11 t Au/jaar (2023-2024,
fijn goud); Peru totaal ≈100-110 t/j mijnproductie [4][5].

## 1 · Ketenkaart
```
Yanacocha-mijn (Newmont) `au-yanacocha-mijn` ──(b1 truck · Carretera Panamericana Norte /
    Cajamarca-Lima-corridor · ~850 km)──►
   Lima Cargo City, Jorge Chávez Int'l (LIM) `au-lim-vrachtterminal`
   ──(b2 lucht · vlucht LIM → ZRH, grootcirkel, aannemelijk: één directe vlucht (§7) · ~10.280 km)──►
   Zürich Airport vrachtplatform (ZRH) `au-zrh-vrachtterminal`
   ──(b3 truck · A4/A2-Gotthard-as · ~200 km)──►
   Valcambi-raffinaderij, Balerna (Ticino) `au-valcambi-raffinaderij` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Yanacocha-mijn → Lima Cargo City (LIM) | Carretera Panamericana Norte / Cajamarca-Lima-corridor | ~850 [ontwerp; gepubliceerde wegafstand Cajamarca-Lima] | maak_stroombeen_weg | nee |
| b2 | B | lucht | Lima (LIM) → Zürich (ZRH) | vrachtvlucht (grootcirkel), aannemelijk: één directe vlucht i.p.v. via Miami-hub (§7) | ~10.280 [ontwerp/hemelsbreed] | maak_luchtbeen | nee — doorgetrokken (lucht is nooit stippel; onzekerheid zit in de beennaam) |
| b3 | C | truck | Zürich vrachtterminal (ZRH) → Valcambi-raffinaderij, Balerna | A4 (Zürich-Zug-Luzern) → A2/Gotthard-as (Luzern-Bellinzona-Chiasso) | ~200 [ontwerp] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-yanacocha-mijn` | mijn / laadplek | Minera Yanacocha (Newmont, 100%), Los Baños del Inca, Cajamarca | -6.9858, -78.5099 | [1][2][9] | bron-gelegd (z14 gezien: open-pit-complex met meerdere putten, heaps/terrassen (lichte trappenterreinen) en meerdere bezinkvijvers — het punt ligt middenin het mijncomplex, tussen twee putten) |
| `au-lim-vrachtterminal` | overslag / lucht | Lima Cargo City, Av. Elmer Faucett, Callao (Jorge Chávez Int'l, LIM) | -12.0289, -77.1039 | [3][9] | bron-gelegd (z15 gezien: cluster vrachtloodsen direct O van het banenstelsel/de taxiway, aan de landzijde van de terminal — matcht het OSM-kantoorpunt "Lima Cargo City"; exact welk loods van welke cargo-agent (Lima Cargo City / SAASA / Frío Aéreo) is op dit beeld niet te onderscheiden) |
| `au-zrh-vrachtterminal` | overslag / lucht | Zürich Airport vrachtplatform | 47.4647, 8.5492 | [6][9] (hergebruikt uit `pgm-springs-zurich.md`, zelfde golf) | bron-gelegd (satellietblik al gedaan voor `pgm-zrh-vrachtterminal`: vrachtplatform met vrachttoestellen naast een rechthoekig loodsgebouw, direct O van de hoofdterminal — zelfde fysieke site, hergebruikt i.p.v. opnieuw gelegd) |
| `au-valcambi-raffinaderij` | losplek / raffinaderij | Valcambi SA, Via Passeggiata 3, Zona Industriale Pian Faloppia, Balerna (Ticino) | 45.8385, 9.0051 | [7][9] | bron-gelegd (z15 gezien: bedrijfsgebouw met parkeerterrein, direct naast de spoorbundel en de A2-knoop bij Balerna — matcht het OSM-gebouw "Valcambi SA") |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Chilete | -7.2215, -78.8390 | waar de weg vanuit Cajamarca het bergdal afdaalt naar de kust (splitsing binnenland/kust) |
| b1 | 2 | Pacasmayo | -7.4029, -79.5685 | kustplaats waar de Cajamarca-weg aansluit op de doorgaande Panamericana Norte |
| b1 | 3 | Trujillo | -8.1120, -79.0288 | grote kustplaats waar de Panamericana Norte doorheen loopt |
| b1 | 4 | Chimbote | -9.0745, -78.5936 | volgende kustplaats op de doorgaande Panamericana Norte |
| b1 | 5 | Barranca | -10.7541, -77.7609 | volgende kustplaats op de doorgaande Panamericana Norte, richting Lima |
| b1 | 6 | Huacho | -11.1067, -77.6050 | laatste grote kustplaats vóór de Lima-metropoolregio |
| b3 | 1 | Zug | 47.1680, 8.5174 | de A4 vanaf Zürich Airport loopt hier, corridorkeuze A4 vs. A1-omweg |
| b3 | 2 | Luzern | 47.0500, 8.3000 | de A4 sluit hier aan op de A2 zuidwaarts (Gotthard-as) |
| b3 | 3 | Gotthard Base Tunnel (as) | 46.8359, 8.6465 | verplicht punt van de A2-Gotthard-corridor tussen Uri en Ticino |
| b3 | 4 | Bellinzona | 46.1954, 9.0297 | de A2 passeert hier bij het uitkomen in het Ticino-dal |
| b3 | 5 | Chiasso | 45.8333, 9.0333 | grenscorridor-punt vlak vóór de afslag naar Balerna |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Valcambi-raffinaderij (Balerna) | Valcambi SA | doré/ruw goud → LBMA-good-delivery baren | grootste goudraffinaderij ter wereld, cap. ≈ 2.000 t/j (alle bronnen, niet Yanacocha-specifiek) | [7][9] |

## 6 · Stoppunt
De brief stopt bij de poort van Valcambi: de raffinaderij zelf is het eindpunt van deze keten
(doré wordt hier tot LBMA-baren geraffineerd); geen bron koppelt een specifieke vervolgbestemming
(kluis/beurs) aan déze partij Yanacocha-doré specifiek, dus fase D/E vervallen.

## 7 · Open punten
- **De aanname van één directe vlucht LIM→ZRH i.p.v. via Miami staat hier expliciet als
  vereenvoudiging** (zoals het ontwerp en de haalbaarheidstoets al aangaven): een deel van Peru's
  officiële goudexport loopt via een tussenstop, en Miami is een bekend transitpunt voor
  Latijns-Amerikaans doré [10]. Geen bron benoemt de exacte routing van déze specifieke
  Yanacocha→Valcambi-stroom, dus de bol tekent één directe grootcirkel LIM→ZRH.
- **Yanacocha-eigendom is per 2022 gewijzigd**: het ontwerp noemde alleen "Newmont" (feitelijk
  correct voor de huidige situatie); Yanacocha was tot 2022 een joint venture (Newmont 51,35% /
  Buenaventura 43,65% / IFC 5%) en is sinds 2022 100% Newmont-eigendom [2] — nu in de brief
  vermeld, zoals de haalbaarheidstoets voorstelde.
- **Lima Cargo City is één van meerdere cargo-agentschappen op LIM** (naast SAASA en Frío
  Aéreo); het satellietbeeld bevestigt een loodsencluster op deze locatie maar niet welk
  specifiek pand welke agent bedient.
- **Via-puntcoördinaten van b1/b3 zijn bekende plaatsen langs de corridor**, niet zelf
  satelliet- of OSM-geverifieerd binnen het webbudget van deze sessie — de bak-agent routeert
  over het OSM-wegennet, dus de exacte ligging volgt uit die routering.
- **Yanacocha-productiecijfers (≈9-11 t Au/jaar 2023-2024) komen uit de ontwerpopgave** (Newmont-
  jaarverslag/USGS), niet onafhankelijk herverifieerd binnen deze sessie; de Wikipedia-infobox
  geeft een ouder cijfer (0,97 Moz in 2014, toen de mijn nog groter was).

## 8 · Bronnen
[1] OpenStreetMap (ODbL) via Nominatim — landuse "Minera Yanacocha" (quarry), -6,9858/-78,5099,
Los Baños del Inca, Cajamarca. https://www.openstreetmap.org
[2] Wikipedia, "Yanacocha" — vierde grootste goudmijn ter wereld, 251 km² open pit, sinds 2022
100% eigendom en operator Newmont (voorheen JV met Buenaventura en IFC). https://en.wikipedia.org/wiki/Yanacocha
[3] OpenStreetMap (ODbL) via Nominatim — office "Lima Cargo City", Av. Elmer Faucett 2823,
Bocanegra, Callao, -12,0289/-77,1039. https://www.openstreetmap.org
[4] Newmont, Yanacocha-operationspagina (bronopgave uit het ketenontwerp voor de productiecijfers
2023-2024, ≈300-350 koz / 9-11 t Au). https://www.newmont.com/operations-and-projects/south-america/yanacocha/
[5] USGS National Minerals Information Center, Gold Statistics and Information — Peru
mijnproductie ≈100-110 t/j (MCS 2025, bronopgave uit het ketenontwerp). https://www.usgs.gov/centers/national-minerals-information-center/gold-statistics-and-information
[6] Esri World Imagery via `v2/tools/sat_check.py` (z14), hergebruikt anker uit `pgm-springs-zurich.md`
(M31 golf 3) — vrachtplatform met vrachttoestellen O van de Zürich Airport-hoofdterminal, 47,4647/8,5492.
[7] Nominatim (OSM, ODbL) — building "Valcambi SA", Via Passeggiata 3, Zona Industriale Pian
Faloppia, Bisio, Balerna, Ticino, 45,8385/9,0051. https://www.openstreetmap.org
[8] WebSearch-samenvatting (2026-09) — Switzerland refines ~70% of the world's gold; Valcambi
S.A. processed around 70% of the gold from Yanacocha (algemene bronvermelding, geen directe
primaire bron binnen het webbudget van deze sessie gevonden).
[9] Esri World Imagery via `v2/tools/sat_check.py` (z14-z15) — `sat-goud-yanacocha-ticino-mijn.png`,
`sat-goud-yanacocha-ticino-limcargo.png`, `sat-goud-yanacocha-ticino-valcambi.png` in
`v2/build-cache/satcheck/`.
[10] Natural Resource Governance Institute, "Is Peru Losing Out on Gold Exports?" — Yanacocha
eigendomsstructuur (historisch, tot 2022), doré-export via Zwitserland (56% van Peru's
goudexport naar Zwitserland 2005-2015). https://resourcegovernance.org/articles/peru-losing-out-gold-exports

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `goud-yanacocha-ticino`** → `v2/data/stroomroute-goud-yanacocha-ticino.json` — 4 benen,
**11.808,9 km**, 19.194 punten, 4 markers. truck 873,1 + lucht 10.667,8 + truck 0,9 (stippel) +
truck 267,1 = 11.808,9 km. Recept: `bak_stromen.sh` (functie `bak_goud_yanacocha_ticino`).
Bestandsgrootte **382,3 KB** (binnen het normale bereik van de corpus — meerdere bestaande bakes
zitten tussen 300 en 670 KB, geen geïsoleerde uitschieter).

**b1 (truck, doorgetrokken, `maak_stroombeen_weg.py`, profiel `goud-yanacocha-ticino-lim`, extract
`peru`):** Yanacocha-mijn → Chilete → Pacasmayo → Trujillo → Chimbote → Barranca → Huacho → Lima
Cargo City (LIM), over de Carretera Panamericana Norte. **873,1 km tegen ~850 km (ontwerpcijfer) =
+2,7%, binnen ±15%.** Anker-verbindingen 0,41 km (mijn → weg) en 0,12 km (weg → kade), beide onder
de 0,5 km-norm — **geen stippel nodig**, geen deel van dit been ligt op privéterrein of <2 km
airside. 64 keerlussen gesnoeid (878,4 → 872,6 km wegkilometers, dubbel gereden dorpsstukken).

**b2 (lucht, doorgetrokken, `maak_luchtbeen.py` — het EERSTE luchtbeen van deze atlas, §2 Lucht):**
grootcirkel Lima Cargo City (LIM) → Zürich Airport vrachtplatform (ZRH), **10.667,8 km, 428 punten**.
Geen km-toets (een luchtbeen ís de grootcirkel per constructie). Doorgetrokken, geen stippel — lucht
is per regel nooit gestippeld; de onzekerheid over één directe vlucht i.p.v. via Miami staat in de
beennaam en §7, niet in de lijnstijl. Bron voor de modaliteit: Zwitserland raffineert ~70% van 's
werelds goud en Valcambi verwerkte naar verluidt ~70% van het Yanacocha-goud (§8, bron [8]).

**Stippel (truck, last mile, ZRH-platform → openbare weg):** het satelliet-gelegde
`au-zrh-vrachtterminal`-anker (47,4647/8,5492, hergebruikt uit `pgm-springs-zurich.md`) bleek bij het
bakken te snappen op een **geïsoleerde apron-service-way** — gemeten met een BFS over de gescande
graaf: component-grootte 2, dus geen enkel wegpad naar het openbare net binnen het venster. Zelfde
klasse bevinding als eerder bij `pgm-springs-zurich` (ZRH-platform → Kloten-kluis, ook toen "geen
wegpad gevonden, ook niet met eindToegangPrivaat"). Opgelost zoals de bakhandleiding §2 Lucht
voorschrijft ("last mile … zonder openbare weg → stippel"): b3 is gescand vanaf het dichtstbijzijnde
punt op het openbare wegennet (47,472087/8,554523, **0,91 km** van het platform, gemeten met dezelfde
graaf) en die 0,91 km is hier een korte, gemotiveerde stippel. **0,914 km, 2 punten.**

**b3 (truck, doorgetrokken, `maak_stroombeen_weg.py`, profiel `goud-yanacocha-ticino-valcambi`,
extract `zwitserland`):** openbare-wegaansluiting bij ZRH → Zug → Luzern → Gotthard Base Tunnel-as →
Bellinzona → Chiasso → Valcambi-raffinaderij, Balerna, over de A4/A2-Gotthard-as. **267,1 km tegen
~200 km (ontwerpcijfer) = +33,5%, BUITEN ±15% — bevinding, niet dichtgetrokken.** Het brief-cijfer is
uitdrukkelijk een grove schatting ("ontwerpcijfer, A2/Gotthard-as", geen gebronde referentie); de
gemeten legs zijn stuk voor stuk aannemelijk voor de echte snelwegafstand (Luzern → Gotthard
noordportaal bij Erstfeld 46,0 km, Gotthard-as → Bellinzona 98,5 km — de Gotthard Base Tunnel-as ligt
bij het noordportaal, niet bij Bellinzona zelf, dus dat stuk omvat het hele tunnel- en Ticino-
dalstuk). Geen via-punt bijgeschoven. Anker-verbindingen 0,00 km (weg → kade bij Valcambi) — geen
tweede stippel nodig. 121 keerlussen gesnoeid (281,3 → 267,1 km).

**Toets naden:** alle vier overgangen **0,000 km** — elk been begint precies waar het vorige eindigt
(inclusief de stippel).

**`toets_knikken.py`:** b1 (truck) 30 knikken ≥60° waarvan 1 **TERUGLOOP** (175,0°, R≈6 m, bij
-7,22160/-78,83915 — vlak bij het Chilete-via-punt, een kleine OSM-dorpswegjunctie). ⚠️ **Bevinding,
niet gerepareerd:** de terugloop is een lokaal spike-artefact van enkele meters op een dorpsweg-
junctie, niet een verkeerd gelegd via-punt (het Chilete-punt snapt zelf op 0,01 km) — geen via-punt
bijgeschoven om de toets te laten slagen. b3 (truck) 20 knikken ≥60°, allemaal spikes <21 m (geen
omkeringen), OSM-wegdetail. Lucht-been: 0 knikken, 0 omkeringen (verwacht, een grootcirkel heeft geen
scherpe bochten). Totaal 50 knikken ≥60°, 4 omkeringen ≥150°, 1 terugloop.

**`toets_rechte_benen.py --min-km 5`:** geen enkel been van deze stroom komt naar voren — het
luchtbeen wordt per constructie overgeslagen en geen ander been heeft een omwegfactor van 1,000 over
≥5 km.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, lucht} (binnen de
toegestane set {zee, binnenvaart, truck, spoor, leiding, lucht}), elk been ≥2 punten (minimum 2 op de
stippel, 19.194 punten totaal).

**Markers:** alle vier exact op de been-eindpunten (au-yanacocha-mijn, au-lim-vrachtterminal,
au-zrh-vrachtterminal, au-valcambi-raffinaderij) — 0,0 m van de lijn, anker = routeerpunt op elk van
de vier.

**Gereedschapslessen:**
- **Eerste gebruik van `maak_luchtbeen.py` in productie.** Het tool werkt zoals de bakhandleiding
  §2 Lucht beschrijft: milliseconden, geen slot nodig, grootcirkel + puntenaantal in de console.
- **Een hergebruikt anker uit een andere brief (`pgm-springs-zurich`) bleek bij het BAKKEN alsnog een
  eigen probleem te dragen** dat bij het overnemen van de coördinaat niet zichtbaar was: de ZRH-
  vrachtplatform-coördinaat zelf snapt op een geïsoleerde apron-way. Dat de vorige brief hetzelfde
  punt al als "geen wegpad, ook niet met eindToegangPrivaat" documenteerde (voor een ander, kort
  eindstuk) had dit vooraf kunnen voorspellen — bij hergebruik van een anker uit een andere brief is
  het de moeite waard ook diens §9/bekende stippels te lezen, niet alleen de coördinaat.
- **`eindToegangPrivaat` lost een geïsoleerde apron-way niet op** wanneer die way een component van
  grootte 2 is (geen enkele buurverbinding binnen het venster, ongeacht toegangsklasse) — dat is een
  topologisch probleem (geen pad), geen toegangsrestrictie-probleem. De juiste fix is het profiel op
  het dichtstbijzijnde punt van het echte netwerk laten beginnen en het restje als korte stippel af
  te sluiten, precies zoals §2 Lucht voorschrijft voor "airside/privéterrein zonder openbare weg".
- WEBBUDGET niet aangesproken deze bak-ronde (geen WebSearch nodig; de connectiviteitsdiagnose liep
  volledig via een lokale Python-BFS op de al gescande graaf).
