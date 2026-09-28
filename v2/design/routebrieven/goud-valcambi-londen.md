# Routebrief (licht) · goud — Valcambi, Balerna (Zwitserland) → Milaan-Malpensa (MXP) → Londen Heathrow (LHR) → Londen (VK)

**stroom-id:** `goud-valcambi-londen` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** good-delivery goudbaren van de Valcambi-raffinaderij in Ticino, per vrachtwagen naar de
vrachtterminal van Milaan-Malpensa, per beveiligde vrachtvlucht (grootcirkel) naar Heathrow, per vrachtwagen over
de M4 naar de LBMA-kluis in de City of London.
**Welke as van het verhaal:** de Zwitserland–VK-goudas — Zwitserse raffinaderijen (Valcambi, PAMP, Argor-Heraeus,
Metalor) leveren het merendeel van hun good-delivery-baren aan de Londense LBMA-markt per beveiligde luchtvracht;
Zwitserland–VK is al decennia de grootste bilaterale goudhandelsas ter wereld [9][10][13]. Geaggregeerde
markt-as, geen bedrijfsspecifieke route (haalbaarheidstoets: expliciet erkend, geen blokkerende aanpassing).

## 1 · Ketenkaart
```
Valcambi-raffinaderij, Balerna `au-ref-valcambi` ──(b1 truck · A2/A9 Ticino → Malpensa · ~78 km)──►
   Milaan-Malpensa vrachtterminal (Cargo City Sud) `au-mxp-cargo`
   ──(b2 lucht · vrachtvlucht MXP → LHR, grootcirkel · ~935 km)──►
   Londen Heathrow vrachtterminal (IAG Cargo/World Cargo Centre) `au-lhr-cargo`
   ──(b3 truck · M4 → City of London · ~25 km)──►
   LBMA-kluis / Bank of England, City of London `au-hub-london` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | Valcambi, Balerna → MXP-vrachtterminal | A2 (Chiasso) → A9 (Como–Lomazzo) → A8 (Gallarate) → SS336, Ticino → Malpensa | ~78 [eigen kaartlezing; ontwerp ≈75] | maak_stroombeen_weg | nee |
| b2 | D | lucht | MXP-vrachtterminal → LHR-vrachtterminal | vrachtvlucht MXP → LHR, grootcirkel | ~935 [eigen grootcirkelberekening MXP 45.6142/8.7186 → LHR 51.4605/-0.4629; ontwerp ≈960] | maak_luchtbeen | nee — doorgetrokken |
| b3 | D | truck | LHR-vrachtterminal → LBMA-kluis, City of London | M4 → Chiswick (A4) → Hammersmith → Hyde Park Corner → Fleet Street | ~25 [eigen kaartlezing] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-ref-valcambi` | raffinaderij / laadplek | Valcambi SA, Via Passeggiata 3, Zona Industriale Pian Faloppia, Balerna | 45.8385, 9.0051 | [1][2][16] | bron-gelegd (z15 gezien: bedrijfsgebouw met platte daken en parkeerterrein tussen de spoorbundel en de A2, direct naast de snelweg-op/afrit — v1-punt 45.845/9.005 hier op siteniveau verfijnd) |
| `au-mxp-cargo` | vrachtterminal | Milano Malpensa Cargo, Cargo City Sud | 45.6142, 8.7186 | [3][4][16] | bron-gelegd (z14 gezien: vrachtloodsen + verhard platform met meerdere vrachttoestellen aan de zuidkant van de start-/landingsbanen, aparte brandweerpost "Aeroportuale Malpensa" ernaast) |
| `au-lhr-cargo` | vrachtterminal | Heathrow World Cargo Centre / IAG Cargo, tussen noord- en zuidbaan | 51.4605, -0.4629 | [5][6][7][16] | bron-gelegd (z15 gezien: vrachtloodsen + platform met geparkeerde vrachtvliegtuigen, direct bij de zuidportaal van de Heathrow Cargo Tunnel — die tunnel verbindt sinds 1968 de vrachtterminal met de rest van het luchthaventerrein) |
| `au-hub-london` | LBMA-kluis / beursgebouw | Bank of England, Threadneedle Street, City of London | 51.5139, -0.0883 | [8][12][16] | bron-gelegd (bekend landmark, financieel hart City of London; hergebruikt v1-anker, coördinaat nu op Wikipedia-geocoördinaat bevestigd — Bank of England is één van de LBMA-erkende kluishouders in Londen) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Chiasso (grensovergang CH–IT) | 45.8333, 9.0333 | verplichte grenspassage A2 → Italiaans net, enige route Ticino → Lombardije hier |
| b1 | 2 | Como (A9) | 45.8167, 9.0833 | A9 volgt de doorgaande corridor langs het Comomeer naar het zuiden |
| b1 | 3 | Lomazzo (A9/A8-knooppunt) | 45.7000, 9.0333 | splitsing A9/A8 — hier kiest de corridor de A8 richting Malpensa/Gallarate |
| b1 | 4 | Gallarate (A8) | 45.6599, 8.7932 | laatste grote plaats vóór de afslag naar Malpensa, pint de A8-tak |
| b3 | 1 | M4 J4/J4b, Heathrow-spur | 51.4870, -0.4595 | enige snelwegaansluiting vanaf de vrachtzone naar het Londense hoofdnet |
| b3 | 2 | Chiswick Roundabout (A4) | 51.4911, -0.2814 | overgang M4 → A4, doorgaande corridor naar centraal Londen |
| b3 | 3 | Hammersmith Flyover (A4) | 51.4912, -0.2240 | vaste doorgaande A4-tak door West-Londen, geen alternatieve route |
| b3 | 4 | Hyde Park Corner | 51.5027, -0.1543 | knooppunt waar de corridor van A4 naar het centrum/City buigt |
| b3 | 5 | Fleet Street | 51.5137, -0.1119 | laatste doorgaande straat vóór de City of London, pint de eindnadering |

## 5 · Verwerkingsknopen
Geen tussenliggende verwerkingsknoop — b1/b3 zijn wegbenen zonder overslag onderweg; de enige overslagen zijn de
twee vrachtterminals (au-mxp-cargo, au-lhr-cargo), al opgenomen als ankers in §3.

## 6 · Stoppunt
De brief stopt bij de LBMA-kluis/Bank of England in de City of London: dit is het eindpunt van het ketenontwerp
("Londen (LBMA-kluizen)") en geen bron noemt een vervolgbestemming ná de Londense kluis — fase E vervalt.

## 7 · Open punten
- **Geaggregeerde markt-as, geen bedrijfsspecifieke route** — vier Zwitserse raffinaderijen samen, al expliciet
  erkend in ontwerp en haalbaarheidstoets.
- **Malpensa i.p.v. Zürich als vertrekluchthaven** is aannemelijk (kortste weg vanuit Ticino) maar niet
  bedrijfsbevestigd — ook al erkend in de haalbaarheidstoets.
- **Geen tussenlanding bevestigd** — aanname is één directe vlucht MXP → LHR (bakhandleiding §2: bij ontbreken
  van een hub-bron geldt de directe vlucht).
- **LBMA-kluis in de City vs. bij Heathrow** — het ketenontwerp noemt expliciet "LBMA-kluis City of London"; in
  werkelijkheid liggen veel commerciële LBMA-kluizen (Brink's, Malca-Amit, Loomis) juist bij Heathrow zelf om
  logistieke redenen. Bank of England (Threadneedle Street) is wél een echte, in de City gevestigde LBMA-kluis en
  is hier als anker gekozen conform het ontwerp — een alternatieve, bedrijfsspecifieke Heathrow-kluis is niet
  uitgesloten.
- **Geen jaartotaal-bron voor de fysieke tonnage Zwitserland → VK** — alleen volatiele maandcijfers 2025-2026
  (16-84 t/maand) en een CHF-waarde voor 2023-2024; zie volumenotitie hieronder.
- **Wegkilometers b1 (~78 km) en b3 (~25 km) zijn eigen kaartlezing**, geen gepubliceerde bronwaarde — wordt bij
  het bakken met `maak_stroombeen_weg.py` definitief gemeten.

*Volumenotitie:* geen gepubliceerd jaartotaal in fysieke tonnage specifiek voor de as Zwitserland→VK gevonden.
Maandcijfers uit de Zwitserse douanestatistiek (via persberichten) tonen een sterk wisselende bandbreedte:
mei 2025 16,0 t · juni 2025 +424% t.o.v. mei · februari 2026 19,8 t · maart 2026 57,6 t [9][10] — op jaarbasis
een orde van grootte van enkele honderden tot mogelijk >500 t/j, consistent met het ontwerp ("enkele honderden
tonnen/jaar"). Zwitserland exporteerde in 2024 in totaal 2.123 t goud wereldwijd (105,2 mld USD) [11] — dit is
géén VK-specifiek cijfer. Oorspronkelijke eenheid: metrische tonnen (t), zoals door Zwitserse douane gerapporteerd.

## 8 · Bronnen
[1] Wikipedia, "Valcambi" — bedrijfsbeschrijving, gevestigd in Balerna, Zwitserland, dochter van Rajesh Exports/REL Singapore. https://en.wikipedia.org/wiki/Valcambi
[2] OpenStreetMap/Nominatim (ODbL) — Valcambi SA, Via Passeggiata 3, Zona Industriale Pian Faloppia, Balerna, 45.83850/9.00506. https://www.openstreetmap.org
[3] Wikipedia, "Milan Malpensa Airport" — coördinaat 45.6300/8.72306. https://en.wikipedia.org/wiki/Milan_Malpensa_Airport
[4] OpenStreetMap/Nominatim (ODbL) — "Milano Malpensa Cargo", Cargo City Sud, Lonate Pozzolo, 45.61417/8.71859. https://www.openstreetmap.org
[5] Wikipedia, "Heathrow Airport". https://en.wikipedia.org/wiki/Heathrow_Airport
[6] Wikipedia, "Heathrow Cargo Tunnel" — tunnel verbindt sinds 1968 Terminals 1-3 met de vrachtterminal; Terminal 4 (1986) gebouwd naast de vrachtterminal. https://en.wikipedia.org/wiki/Heathrow_Cargo_Tunnel
[7] OpenStreetMap/Photon (ODbL) — "IAG Cargo", landuse industrial locality, Sealand Road, Hillingdon, 51.46048/-0.46293. https://photon.komoot.io
[8] Wikipedia, "Bank of England" — coördinaat 51.51389/-0.08833. https://en.wikipedia.org/wiki/Bank_of_England
[9] Kitco News, 21-04-2026 — "Gold exports from Switzerland up 30% in March as deliveries to UK jump" (Zwitserse douanedata: VK-leveringen feb 2026 19,8 t → mrt 2026 57,6 t). https://www.kitco.com/news/off-the-wire/2026-04-21/gold-exports-switzerland-30-march-deliveries-uk-jump
[10] Discoveryalert, 2026 — "Swiss June Gold Exports Jump 44% as Bullion Returns to UK" (mei 2025 16,0 t → juni 2025 +424%). https://discoveryalert.com.au/news/switzerland-gold-market-role-2025-exports/
[11] Wikipedia, "List of countries by gold exports" — Zwitserland totaal 2024: 2.123 t / 105,2 mld USD (International Trade Centre/Trade Map). https://en.wikipedia.org/wiki/List_of_countries_by_gold_exports
[12] LBMA — Good Delivery List (erkende raffinaderijen incl. Valcambi, PAMP, Argor-Heraeus, Metalor). https://www.lbma.org.uk/good-delivery/list
[13] Swiss Federal Customs Administration (BAZG) — jaarlijkse edelmetaalstatistiek "goud-export naar het VK". https://www.gate.ezv.admin.ch/
[14] Valcambi SA — bedrijfswebsite. https://www.valcambi.com/
[15] Esri World Imagery via `v2/tools/sat_check.py` (z14-z15) — `sat-goud-valcambi-londen-valcambi.png`, `sat-goud-valcambi-londen-mxp-cargo.png`, `sat-goud-valcambi-londen-lhr-cargo2.png`, `sat-goud-valcambi-londen-boe.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `goud-valcambi-londen`** → `v2/data/stroomroute-goud-valcambi-londen.json` — 3 benen (truck fase D →
lucht fase D → truck fase D → stoppunt), **1.041,1 km**, 2.343 punten, 4 markers, 45,4 KB. Recept:
`bak_stromen.sh` (functie `bak_goud_valcambi_londen`); twee nieuwe wegprofielen
`goud-valcambi-londen-valcambi-mxp` en `goud-valcambi-londen-lhr-boe` in `maak_stroombeen_weg.py` (er bestond nog
geen luchtbeen-bake in dit project — dit is de eerste, samen met de andere golf-3-luchtstromen).

**b1 (truck, nieuw profiel, extracts `zwitserland`+`italie`, vensterKm 50):** `maak_stroombeen_weg.py --profiel
goud-valcambi-londen-valcambi-mxp --bron geofabrik` — **69,1 km** geroute (getekende lijn 69,1 km incl.
anker-verbindingsstukjes 0,01/0,09 km, beide OK) over de vier via-punten uit de brief §4 (Chiasso → Como →
Lomazzo → Gallarate), A2 (Chiasso-grensovergang) → A9 (langs het Comomeer) → A8 (naar Malpensa). 106 keerlussen
gesnoeid (77,0 → 69,0 km, dubbel gereden stukken, vooral bij Valcambi en rond Gallarate). First mile 0,06 km /
last mile 1,60 km over kleine wegklassen (service/unclassified).

**⚠️ Lengtetoets BUITEN de norm:** 69,1 km tegen het ~78 km-ontwerpcijfer (routebrief §2/§7, "eigen kaartlezing,
geen aparte gepubliceerde bron") = **−11,6%**, net buiten ±10% maar binnen ±15% (bakhandleiding §5). Bevinding,
geen fout: de vier via-punten uit de brief pinnen de enige doorgaande corridor A2→A9→A8; geen via-punt
bijgeschoven om het getal te halen. De bake-uitvoer (69,1 km) is de echte controle, niet het ontwerpcijfer.

**b2 (lucht, `maak_luchtbeen.py`, DOORGETROKKEN):** `python v2/tools/maak_luchtbeen.py --van "Milaan-Malpensa
(MXP) vrachtterminal|45.6142,8.7186" --naar "Londen Heathrow (LHR) vrachtterminal|51.4605,-0.4629" --uit
$BEEN/goud-valcambi-londen-lucht-mxp-lhr.geojson` — grootcirkel **936,5 km**, 39 punten. Tegen het
brief-ontwerpcijfer ~935 km (eigen grootcirkelberekening in de opdracht, +0,2%) en de ontwerp-indicatie ≈960 km
(−2,4%) — een luchtbeen heeft geen ±15%-km-toets (zijn km = grootcirkel per constructie, bakhandleiding §5). Geen
tussenlanding: geen bron in de brief noemt een hub (§7), dus één directe vrachtvlucht MXP → LHR conform §2
"Lucht".

**b3 (truck, nieuw profiel, extract `groot-brittannie`, `eindKlassen` tertiary/unclassified/residential/service,
vensterKm 40):** `maak_stroombeen_weg.py --profiel goud-valcambi-londen-lhr-boe --bron geofabrik` — **35,5 km**
geroute (getekende lijn 35,5 km incl. anker-verbindingsstukjes 0,05/0,06 km, beide OK) over de vijf via-punten
uit de brief §4 (M4 J4/J4b → Chiswick Roundabout → Hammersmith Flyover → Hyde Park Corner → Fleet Street). 109
keerlussen gesnoeid (37,2 → 35,4 km). First mile 4,08 km / last mile 1,25 km over kleine wegklassen
(residential/service/tertiary/unclassified) — nodig om de laatste meters bij de Bank of England (City of Londen,
smalle straten) te bereiken; de lijn eindigt zonder aparte last-mile-stippel exact op het Bank of England-anker
(0,000 km, zie markers hieronder), dus de door de brief geopperde mogelijke stippel bij de kluis zelf bleek bij
de bake niet nodig — de scanner vond een doorgaande, toegankelijke straatroute (o.a. Threadneedle Street zelf)
tot op het anker.

**⚠️ Lengtetoets BUITEN de norm:** 35,5 km tegen het ~25 km-ontwerpcijfer (routebrief §2/§7, "eigen kaartlezing,
geen aparte gepubliceerde bron") = **+41,6%**, ruim buiten ±15%. Bevinding, geen fout: het ontwerpcijfer was een
hemelsbrede/kaartlees-schatting; de echte rijroute M4→A4→Hyde Park Corner→Fleet Street door West-Londen en de
City is aantoonbaar langer dan een rechte-lijn-schatting. Vergelijkbaar met de +41,3%- en +101,0%-bevindingen op
de zuster-golf-3-keten `pgm-zondereinde-hanau` (zelfde golf, zelfde soort indicatief ontwerpcijfer). Geen
via-punt bijgeschoven om het getal te halen.

**Toetsen:** `toets_knikken.py` — b1 (truck): 16 knikken ≥60°, **0 omkeringen, 0 terugloop**; b2 (lucht): 0
knikken, 0 omkeringen (per constructie recht); b3 (truck): 13 knikken ≥60°, **0 omkeringen, 0 terugloop** — alle
29 knikken zijn kleine-straal-spikes (1–29 m) bij kruispunten/rotondes, geen enkele hoort volgens de
toets-documentatie gerepareerd te worden. `toets_rechte_benen.py --min-km 5` — geen ⚠️-vlag voor deze stroom
(niet in de uitvoer-lijst; lucht wordt per ontwerp overgeslagen, b1 en b3 zijn geen verdachte rechte lijnen).
`json.load` slaagt: `versie` 2, `punt_formaat` lonlat, modaliteiten `{truck, lucht}` ⊂ toegestane set, elk been ≥
2 punten (983 / 39 / 1.321), bestandsgrootte 45,4 KB (ruim onder ~300 KB). Naden tussen b1↔b2 en b2↔b3: **0,000
km** (elk been-geojson start exact op het eindpunt van het vorige — de truckbenen sluiten rechtstreeks aan op het
vrachtterminal-eind van de vlucht). Markers: alle vier ankers zijn letterlijk het eindpunt van hun been (0,000 km
tot de lijn) — routeerpunt = anker op elke overslag.

**Toelichting stippels/haven-aanlopen/vluchten:** geen stippel in deze stroom (géén kades, dus geen
haven-aanloop nodig, conform de bak-aanwijzing in de brief). Eén vlucht (b2), doorgetrokken conform
bakhandleiding §2: anker = de satelliet-gelegde vrachtterminals aan beide kanten (brief §3, bron-gelegd), geen
tussenlanding aangenomen (§7). De truckbenen sluiten rechtstreeks aan op het vrachtterminal-eind van de vlucht —
geen apart terminalbeen nodig, want het MXP- resp. LHR-vrachtterminalanker ís al het overslagpunt truck ↔ lucht.

**Gereedschapslessen:** de eerste luchtbeen-bake in dit project — `maak_luchtbeen.py` werkte zonder aanpassing
op de eerste poging (geen slot nodig, milliseconden). Beide wegprofielen liepen in één scan door zonder
`eindToegangPrivaat` of extra via-punten; alleen `eindKlassen` was nodig bij b3 om de laatste stedelijke meters
tot de Bank of England mee te nemen. Beide length-bevindingen (−11,6% / +41,6%) komen uit een indicatief
ontwerpcijfer zonder gepubliceerde bronwaarde, niet uit een verkeerd gelegde corridor — de via-punten uit de
brief pinnen in beide gevallen de enige doorgaande route.

**Open punten (ongewijzigd t.o.v. §7 van de brief):** geaggregeerde marktas · Malpensa i.p.v. Zürich aannemelijk
maar niet bedrijfsbevestigd · geen tussenlanding bevestigd · LBMA-kluis City of Londen vs. Heathrow-kluizen ·
geen jaartotaal-bron voor de fysieke tonnage Zwitserland→VK · beide wegkilometers waren eigen kaartlezing, nu
door de bake definitief gemeten (69,1 / 35,5 km) — beide buiten ±15% zoals hierboven vastgelegd.
