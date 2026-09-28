# Routebrief (licht) · zilver — Valcambi, Balerna (Zwitserland) → Milaan-Malpensa (MXP) → Londen Heathrow (LHR) → Londen (VK)

**stroom-id:** `zilver-valcambi-londen` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** good-delivery zilverbaren van de Valcambi-raffinaderij in Ticino, per vrachtwagen naar de
vrachtterminal van Milaan-Malpensa, per beveiligde vrachtvlucht (grootcirkel) naar Heathrow, per vrachtwagen over
de M4 naar de LBMA-kluis in de City of London.
**Welke as van het verhaal:** de vraagkant-as van het structurele zilvertekort — Zwitserse raffinaderijen leveren
good-delivery baren aan de Londense LBMA-markt/kluizen, die het tekort tussen bijproduct-aanbod en industriële
vraag (zonnepanelen) aftappen [1][2]. Valcambi staat naast goud óók op de **LBMA Good Delivery-lijst voor zilver**
[9][10] — de kernaanname van deze as (geen aparte goud-only status). Geaggregeerde markt-as, geen
bedrijfsspecifieke zending (haalbaarheidstoets: expliciet erkend, geen blokkerende aanpassing).

## 1 · Ketenkaart
```
Valcambi-raffinaderij, Balerna `ag-ref-valcambi` ──(b1 truck · A2/A9 Ticino → Malpensa · ~69 km)──►
   Milaan-Malpensa vrachtterminal (Cargo City Sud) `ag-mxp-cargo`
   ──(b2 lucht · vrachtvlucht MXP → LHR, grootcirkel · ~937 km)──►
   Londen Heathrow vrachtterminal (IAG Cargo/World Cargo Centre) `ag-lhr-cargo`
   ──(b3 truck · M4 → City of London · ~36 km)──►
   LBMA-kluis / Bank of England, City of London `ag-hub-london` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | Valcambi, Balerna → MXP-vrachtterminal | A2 (Chiasso) → A9 (Como–Lomazzo) → A8 (Gallarate), Ticino → Malpensa — **letterlijke kopie** van `goud-valcambi-londen`-been b1 | 69,1 [gebakken, `goud-valcambi-londen-weg-valcambi-mxp.geojson`] | maak_stroombeen_weg (reeds gebakken geojson hergebruiken, geen nieuwe scan) | nee |
| b2 | D | lucht | MXP-vrachtterminal → LHR-vrachtterminal | vrachtvlucht MXP → LHR, grootcirkel — **letterlijke kopie** van `goud-valcambi-londen`-been b2 | 936,5 [gebakken, `goud-valcambi-londen-lucht-mxp-lhr.geojson`] | maak_luchtbeen (reeds gebakken geojson hergebruiken) | nee — doorgetrokken |
| b3 | D | truck | LHR-vrachtterminal → LBMA-kluis, City of London | M4 → Chiswick (A4) → Hammersmith → Hyde Park Corner → Fleet Street — **letterlijke kopie** van `goud-valcambi-londen`-been b3 | 35,5 [gebakken, `goud-valcambi-londen-weg-lhr-boe.geojson`] | maak_stroombeen_weg (reeds gebakken geojson hergebruiken) | nee |

## 3 · Ankers (één per site en per overslag) — allemaal letterlijk hergebruikt uit `goud-valcambi-londen.md` §3
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-ref-valcambi` | raffinaderij / laadplek | Valcambi SA, Via Passeggiata 3, Zona Industriale Pian Faloppia, Balerna | 45.8385, 9.0051 | [1][3][9][11] | bron-gelegd (hergebruik `au-ref-valcambi` — z15 gezien: bedrijfsgebouw met platte daken tussen de spoorbundel en de A2, direct naast de snelweg-op/afrit; Valcambi is naast goud ook LBMA Good Delivery-erkend voor zilver [9][10], dus letterlijk hetzelfde site-anker geldt) |
| `ag-mxp-cargo` | vrachtterminal | Milano Malpensa Cargo, Cargo City Sud | 45.6142, 8.7186 | [4][5][11] | bron-gelegd (hergebruik `au-mxp-cargo` — z14 gezien: vrachtloodsen + verhard platform met meerdere vrachttoestellen, aparte brandweerpost "Aeroportuale Malpensa" ernaast) |
| `ag-lhr-cargo` | vrachtterminal | Heathrow World Cargo Centre / IAG Cargo, tussen noord- en zuidbaan | 51.4605, -0.4629 | [6][7][11] | bron-gelegd (hergebruik `au-lhr-cargo` — z15 gezien: vrachtloodsen + platform met geparkeerde vrachtvliegtuigen, bij de zuidportaal van de Heathrow Cargo Tunnel) |
| `ag-hub-london` | LBMA-kluis / beursgebouw | Bank of England, Threadneedle Street, City of London | 51.5139, -0.0883 | [8][11] | bron-gelegd (hergebruik `au-hub-london` — bekend landmark, financieel hart City of London; Bank of England is één van de LBMA-erkende kluishouders in Londen, voor zowel goud als zilver) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze) — letterlijk hergebruikt uit `goud-valcambi-londen.md` §4
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
twee vrachtterminals (`ag-mxp-cargo`, `ag-lhr-cargo`), al opgenomen als ankers in §3.

## 6 · Stoppunt
De brief stopt bij de LBMA-kluis/Bank of England in de City of London: dit is het eindpunt van het ketenontwerp
("LBMA-kluis / Bank of England") en geen bron noemt een vervolgbestemming ná de Londense kluis — fase E vervalt.

## 7 · Open punten
- **Geen zilver-specifiek jaarvolume voor de as Zwitserland→VK gevonden** — al expliciet erkend in ontwerp en
  haalbaarheidstoets. Aggregaat handelscontext: Zwitserland is #6 zilverexporteur wereldwijd ($3,6 mld, +87,8%
  j-o-j), het VK #1 ($8,2 mld, +125,9% j-o-j) — waardecijfers 2025, geen bilaterale fysieke tonnage CH→VK [12].
  De analoge goud-as heeft wél maandcijfers (16–58 t/maand CH→VK, Zwitserse douane); voor zilver is dat cijfer
  deze ronde niet gevonden. Blijft open punt, geen blocker — precies zoals bij de analoge goud-as.
- **Malpensa i.p.v. Zürich als vertrekluchthaven** is aannemelijk (kortste weg vanuit Ticino, hergebruikt de
  goud-as) maar niet apart voor zilver bedrijfsbevestigd.
- **Aanname dat zilverbaren exact hetzelfde Malpensa→Heathrow-vluchttracé volgen als goudbaren** (zelfde
  raffinaderij, zelfde beveiligde bullion-luchtvrachtketen) is aannemelijk maar niet apart bevestigd voor zilver;
  geen tussenlanding aangenomen (bakhandleiding §2: bij ontbreken van een hub-bron geldt de directe vlucht).
- **LBMA-kluis in de City vs. bij Heathrow** — commerciële LBMA-kluizen (Brink's, Malca-Amit, Loomis) liggen vaak
  bij Heathrow zelf; Bank of England is wél een echte, in de City gevestigde LBMA-kluis (voor goud én zilver) en
  is hier als anker gekozen conform het ontwerp — een alternatieve Heathrow-kluis is niet uitgesloten.
- **Wegkilometers b1/b3 zijn een letterlijke kopie van de reeds gebakken `goud-valcambi-londen`-geometrie** — geen
  aparte lengtetoets nodig voor zilver, want het is exact dezelfde route/geojson (zelfde raffinaderij, zelfde
  vrachtterminals, zelfde kluis); wel een andere lading (zilverbaren i.p.v. goudbaren).

## 8 · Bronnen
[1] Wikipedia, "Valcambi" — bedrijfsbeschrijving, Balerna, Zwitserland, dochter van Rajesh Exports/REL Singapore;
    "specializing in gold, silver, platinum and palladium". https://en.wikipedia.org/wiki/Valcambi
[2] The Silver Institute / Metals Focus, "World Silver Survey" — structureel zilvertekort, industriële vraag
    (zonnepanelen) > bijproduct-aanbod, kluisvoorraden LBMA/COMEX/SGE aftappen. https://www.silverinstitute.org/
[3] OpenStreetMap/Nominatim (ODbL) — Valcambi SA, Via Passeggiata 3, Zona Industriale Pian Faloppia, Balerna,
    45.83850/9.00506. https://www.openstreetmap.org
[4] Wikipedia, "Milan Malpensa Airport" — coördinaat 45.6300/8.72306. https://en.wikipedia.org/wiki/Milan_Malpensa_Airport
[5] OpenStreetMap/Nominatim (ODbL) — "Milano Malpensa Cargo", Cargo City Sud, Lonate Pozzolo, 45.61417/8.71859.
    https://www.openstreetmap.org
[6] Wikipedia, "Heathrow Airport" — coördinaat 51.4775/-0.46139. https://en.wikipedia.org/wiki/Heathrow_Airport
[7] OpenStreetMap/Photon (ODbL) — "IAG Cargo", landuse industrial locality, Sealand Road, Hillingdon,
    51.46048/-0.46293. https://photon.komoot.io
[8] Wikipedia, "Bank of England" — coördinaat 51.51389/-0.08833. https://en.wikipedia.org/wiki/Bank_of_England
[9] LBMA, "Good Delivery Current List - Silver" — Valcambi als geaccrediteerde zilver-Good-Delivery-refiner.
    https://www.lbma.org.uk/good-delivery/silver-current-list
[10] WebSearch-webcheck 2026-09-28, "LBMA Good Delivery List silver Valcambi accredited refiner" — bevestigt:
    "Valcambi is an accredited LBMA Good Delivery refiner for gold and silver and an accredited LPPM Good
    Delivery refiner for platinum and palladium."
[11] `v2/design/routebrieven/goud-valcambi-londen.md` — bron-brief voor de vier letterlijk hergebruikte ankers
    (§3) en de drie letterlijk hergebruikte, reeds gebakken benen (§2, §9: b1 69,1 km / b2 936,5 km / b3 35,5 km).
[12] worldstopexports.com, "Silver Exports by Country 2025" — Zwitserland #6 ($3,6 mld, 6,4%, +87,8% j-o-j), VK
    #1 ($8,2 mld, 14,5%, +125,9% j-o-j); wereldtotaal $56,5 mld 2025. Waardecijfers, geen bilaterale tonnage.
    https://www.worldstopexports.com/silver-exports-country/

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Recept:** `bak_zilver_valcambi_londen()` in `v2/tools/bak_stromen.sh` (draaien: `bash v2/tools/bak_stromen.sh
zilver-valcambi-londen`). Alle drie de benen zijn **letterlijke geometrische kopieën** van de reeds gebakken keten
`goud-valcambi-londen` — `--been-geojson` wijst rechtstreeks naar de bestaande bestanden in
`v2/build-cache/ais/graaf/`, géén nieuwe wegscan, géén nieuwe luchtbeen-run. Uitvoer:
`v2/data/stroomroute-zilver-valcambi-londen.json` (45,4 KB, contract-versie 2, `punt_formaat: lonlat`).

| # | modaliteit | km | punten | naam | stippel | herkomst |
|---|---|---|---|---|---|---|
| b1 | truck | 69,1 | 983 | Valcambi, Balerna → Malpensa-vrachtterminal (A2/A9/A8) | nee | kopie `goud-valcambi-londen-weg-valcambi-mxp.geojson` |
| b2 | lucht | 936,5 | 39 | vlucht MXP → LHR (vrachtvlucht, grootcirkel) | nee — doorgetrokken | kopie `goud-valcambi-londen-lucht-mxp-lhr.geojson` |
| b3 | truck | 35,5 | 1.321 | Heathrow World Cargo Centre → Bank of England, City of London (M4/A4) | nee | kopie `goud-valcambi-londen-weg-lhr-boe.geojson` |

**Totaal:** 1.041,1 km · 2.343 punten · 4 markers (`ag-ref-valcambi` · `ag-mxp-cargo` · `ag-lhr-cargo` ·
`ag-hub-london`, allemaal letterlijk hergebruikt uit `goud-valcambi-londen.md` §3).

**Toets (bakhandleiding §5):**
- Km per been: b1 en b3 zijn een letterlijke kopie van de al gemeten goud-geometrie (69,1 / 35,5 km) — geen
  aparte lengtetoets nodig, zelfde route, andere lading (brief §7/§9). b2 is een grootcirkel (936,5 km, geen
  km-toets van toepassing).
- **Naden:** alle drie de overgangen 0,00 km (been-geojsons sluiten exact op elkaar aan, zoals bij de
  goud-as — geen haven-aanloop nodig, geen kade in deze keten).
- **Markers:** alle vier op 0,0 m van de lijn (anker = routeerpunt op elk van de vier punten).
- `toets_knikken.py`: b1 16 spikes en b3 13 spikes (alle <60 m straal, OSM-precisie-artefacten in de
  brongeometrie van de goudkopie, dus **niet nieuw** — identiek aan wat de goud-as al droeg), b2 0 knikken
  (grootcirkel). **0 omkeringen, 0 terugloop** op alle drie de benen.
- `toets_rechte_benen.py --min-km 5`: geen van de drie benen verschijnt in de wereldwijde verdachtenlijst
  (geen been heeft een omwegfactor ≈1,000 — de doorgetrokken wegbenen volgen echte, gekromde weggeometrie en
  het luchtbeen wordt door het tool bewust overgeslagen, bakhandleiding §2 Lucht).
- `json.load`: slaagt, `versie == 2`, `punt_formaat == "lonlat"`, alle drie de modaliteiten (`truck`/`lucht`)
  in de toegestane set, elk been ≥ 2 punten, bestand 45,4 KB (ver onder ~300 KB).

**Toelichting per been:**
- **b1/b3 (truck, letterlijke kopie):** geen enkele stippel — de goud-as had voor deze twee wegbenen al een
  doorgetrokken, echt gekarteerde corridor (A2/A9/A8 resp. M4/A4) en die geometrie geldt onveranderd voor
  zilverbaren over dezelfde weg.
- **b2 (lucht, doorgetrokken):** grootcirkel MXP → LHR, geen stippel — een vlucht tussen twee satelliet-gelegde
  vrachtterminals is per bakhandleiding §2 geen gat in het net. Geen tussenlanding aangenomen (brief §7); geen
  aparte lading-bevestiging voor zilver op dit tracé (aannemelijk: hergebruik van de goud-as, brief §7/§10).
- **Geen fase E, geen haven-aanloop, geen leiding/binnenvaart/spoor** — de keten bestaat uit precies twee
  modaliteiten (truck + lucht), zoals de goud-as.

**Lessen:** een letterlijke geometrische kopie van een reeds bak-getoetste keten levert bij hergebruik dezelfde
knikken/spikes op als het origineel (b1: 16, b3: 13) — dat is geen nieuwe bevinding, het is de brongeometrie die
al bij `goud-valcambi-londen` §9 stond. Geen enkele gedeelde-bestand-edit was nodig in `maak_stroombeen_weg.py`
(geen nieuwe `PROFIELEN`-sleutel), want `--been-geojson` wijst rechtstreeks naar het bestaande, al gebakken
bestand — precies zoals de haalbaarheidstoets voorschreef.

**Open punten (ongewijzigd t.o.v. §7):** geen zilver-specifiek jaarvolume CH→VK gevonden; Malpensa i.p.v. Zürich
en het gedeelde vluchttracé blijven aannames op basis van de goud-as (niet apart voor zilver bedrijfsbevestigd);
LBMA-kluis in de City vs. een commerciële Heathrow-kluis blijft een ontwerpkeuze, geen uitsluiting.
