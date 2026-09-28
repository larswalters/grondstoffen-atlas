# Routebrief (licht) · gas — Ras Laffan (Qatar) → Rotterdam (Nederland)

**stroom-id:** `gas-raslaffan-rotterdam` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 4) ·
**status:** gebakken
**Keten in één zin:** Aardgas uit het North Field komt via dezelfde offshore verzamelleiding als de
Japan-as aan land bij Ras Laffan, wordt er tot LNG verwerkt (QatarEnergy LNG) en vaart als LNG-tanker
via de Straat van Hormuz, Bab-el-Mandeb en (geografisch) het Suezkanaal naar de Gate terminal
(Vopak/Gasunie) op de Maasvlakte, Rotterdam — de reserve-as die Qatar's Europa-groei sinds 2022 langs
een ander stratenpaar toont dan de Atlantische Sabine Pass-as.
**Welke as van het verhaal:** *de Suez-as, ondergraven door haar eigen risico* — geografisch de kortste
Qatar→Europa-route, maar sinds de Houthi-aanvallen (eind 2023) mijdt de wereldwijde LNG-vloot de Rode
Zee/Suez vrijwel volledig en vaart om de Kaap; Suezkanaal-verkeer stond begin 2026 nog ~60% onder het
niveau van vóór de crisis [8][9][10][11]. Ras Laffan-cijfer identiek aan as 2 (`gas-raslaffan-chiba`):
~77 Mtpa huidige liquefactiecapaciteit, oplopend naar >126 Mtpa na de North Field East/South-uitbreiding
(peiljaar 2025–2027) [6][7]; een Europa-specifiek cargovolume voor déze as is niet los gebrond (§7).

## 1 · Ketenkaart
```
North Field (offshore gasveld, gedeeld met as gas-raslaffan-chiba) ── stoppunt: geen site-anker (§7) ──
   (b1 leiding · offshore subsea trunkline · ~80 km, stippel — letterlijke kopie van as 2)──►
   Ras Laffan LNG-laadkade `gas-raslaffan-kade` (hergebruikt anker uit gas-raslaffan-chiba)
   ──(b2a zee · haven-aanloop Ras Laffan · ~41,6 km, stippel-geojson — letterlijke kopie van as 2)──►
   ──(b2b zee · Perzische Golf → Hormuz → Arabische Zee → Bab-el-Mandeb → Rode Zee → Suezkanaal →
       Middellandse Zee → Gibraltar → Atlantische kust/Noordzee · ~11.000–12.000 km, MARNET;
       praktijk 2024–2026 overwegend via Kaap de Goede Hoop omgeleid, zie §7)──►
   Gate terminal `gas-gate-kade` (hergebruikt anker uit gas-sabinepass-rotterdam)
   ── stoppunt (voedt GTS-net, terreinleiding niet getekend, conform as 1) ──
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | North Field (offshore) → Ras Laffan-kade | offshore verzamelleiding (subsea gathering) — gedeeld been met `gas-raslaffan-chiba` | 84,7 (gemeten in as 2) | **letterlijke kopie**: dezelfde `--stippel`-regel als `bak_gas_raslaffan_chiba` (geen geojson-bestand, rechte lijn 26.6191,51.9500 → 25.9265,51.5955) | ja — subsea, niet gekarteerd, zie as 2 §7 |
| b2a | B | zee | Ras Laffan-kade → MARNET-zeeknoop 4090 | haven-aanloop, kade 41,5 km van de zeeknoop (LAR-586) | 41,6 (gemeten in as 2) | **letterlijke kopie**: `v2/build-cache/ais/graaf/gas-raslaffan-chiba-aanloop-raslaffan.geojson` hergebruiken, niet opnieuw bakken | ja — haven-aanloop |
| b2b | B | zee | zeeknoop 4090 → Gate-kade Rotterdam | Golf → Hormuz → Arabische Zee → Bab-el-Mandeb → Rode Zee → Suez → Middellandse Zee → Gibraltar → Noordzee (MARNET kiest zelf; zie §7 voor de Kaap-praktijk) | ~11.000–12.000 (ontwerp-indicatie, ongebrond) | MARNET (kade → kade) | nee, Gate-kade ligt < 5 km van een zeeknoop (1,836 km, gemeten in as 1) — geen tweede haven-aanloop |

**Fase C vervalt** (conform as 1, `gas-sabinepass-rotterdam` §2): geen OSM-pijpleiding-way voor de
terreinleiding Gate-regas → GTS-invoedingspunt gevonden, geen tweede coördinaat gebrond.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-raslaffan-kade` | overslag leiding→zee / LNG-laadkade | Ras Laffan LNG-laadsteiger (QatarEnergy LNG-complex) | 25.9265, 51.5955 | [1][2] — **hergebruikt letterlijk** uit `gas-raslaffan-chiba.md` §3 | bron-gelegd (satellietblik reeds gedaan in as 2, z16: kade-eiland met opslagtanks en trestle-toegangswegen; geen nieuwe pass nodig) |
| `gas-gate-kade` | losplek / LNG-importterminal (regasificatie), stoppunt | Gate terminal (Vopak/Gasunie), Maasvlakte, Rotterdam | 51.97110, 4.06890 | [4][5] — **hergebruikt letterlijk** uit `gas-sabinepass-rotterdam.md` §3 | aannemelijk (satellietblik reeds gedaan in as 1, z15: reëel tank-/steigercomplex, maar niet scherp te scheiden van de aangrenzende Maasvlakte Olie Terminal — status blijft aannemelijk, geen nieuwe pass nodig) |

## 4 · Via-punten
Geen — beide landbenen (b1, fase C vervalt) zijn korte/ongekarteerde stippel-verbindingen zonder
corridorkeuze; het zeebeen (b2a+b2b) routeert kade → kade over MARNET.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ras Laffan LNG-complex | QatarEnergy LNG | pijpleidinggas (North Field) → LNG | ~77 Mtpa huidig, >126 Mtpa na uitbreiding (2025–2027) ≈ 104,7–171,4 bcm/j (1 Mt LNG ≈ 1,36 bcm) | [6][7] |
| Gate terminal | Vopak / Gasunie | LNG (carrier) → hervergast aardgas → GTS-landelijke net | 12 bcm/j basis (3 tanks × ~180.000 m³) → 16–20 bcm/j na de 4e tank (verwacht 2026) | [4][5] |

## 6 · Stoppunt
De brief stopt bij het regasificatiepunt van de Gate terminal, zelfde gronden als as 1
(`gas-sabinepass-rotterdam` §6): geen bron koppelt één specifieke Ras Laffan-lading aan Rotterdam, en
er is geen gedocumenteerd downstream-eindpunt (fabriek/centrale) dat déze as met naam verbindt. Fase
D/E vervallen.

## 7 · Open punten
- **Geen site-anker voor fase A** — gedeeld met as 2 (`gas-raslaffan-chiba` §7): North Field is een
  offshore veld van >6.000 km² zonder kade op één punt; fase A begint "in het veld" en eindigt gemeten
  op het Ras Laffan-kade-anker.
- **Ras Laffan-kade ligt 41,5 km van de MARNET-zeeknoop** — bakhandleiding §0.5/bakregel "gedeeld been =
  letterlijke kopie": zowel b1 als de haven-aanloop b2a zijn al gebakken in as 2 en worden **niet
  opnieuw** gezocht of gebakken, alleen het bestaande geojson/de bestaande `--stippel`-regel hergebruikt.
- **Gate-kade-anker blijft aannemelijk** — al satellietgecheckt in as 1; op z14–z16 niet scherp te
  scheiden van de aangrenzende Maasvlakte Olie Terminal. Geen nieuwe pass nodig (bakhandleiding: bestaande
  ankers letterlijk hergebruiken).
- **Geen Europa-specifiek cargovolume gebrond voor déze as** — alleen het Qatar-totaal (§0) en het
  kwalitatieve "Europa-aandeel structureel gegroeid sinds de Nord Stream-uitval (2022)", niet op
  cargo-niveau.
- **⚠️ Belangrijkste bevinding van deze as: de geografisch kortste route (Suez) is sinds eind 2023
  grotendeels NIET de praktijkroute.** Houthi-aanvallen op scheepvaart in de Rode Zee/Bab-el-Mandeb
  (onderdeel van het Midden-Oosten-conflict 2023–heden [8]) deden Rode Zee-verkeer met 57,5% en
  Suez-containerverkeer met 90% (dec 2023–mrt 2024) kelderen; begin 2026 lag het Suezkanaal-verkeer nog
  ~60% onder het pre-crisisniveau, met de Kaap-omleiding 74–191% boven 2023-niveaus (10–14 dagen /
  4.000–5.000 zeemijl extra per reis) [9]. De wereldwijde LNG-vloot behoort tot de gebruikers die de
  route structureel meden, met Qatar als grootste LNG-gebruiker van de Rode Zee/Suez-corridor [10][11].
  De Houthi-aanvallen pauzeerden na het Gaza-staakt-het-vuren van oktober 2025, maar een multinationaal
  maritiem advies van april 2026 hield de Bab-el-Mandeb-doorvaart op een "matig" dreigingsniveau en de
  Houthi's dreigden met hervatting bij een instortend bestand of escalatie van de 2026-Iran-oorlog [10].
  **Voor het bakken:** deze brief tekent de MARNET-kortste-padroute (via Suez, zoals de ontwerp-as
  vraagt); de bak-agent hoeft géén Kaap-omweg te forceren — MARNET routeert zelf kortste-pad en dat is
  precies het punt: de kaart toont de geografische route, de risicotekst legt uit waarom de praktijk
  daarvan afwijkt (zelfde behandeling als het Hormuz-risico bij as 2, geen routeer-ingreep).

## 8 · Bronnen
[1] Wikipedia, "Ras Laffan Industrial City" — 25,8575/51,53889, hergebruikt uit `gas-raslaffan-chiba.md`.
    https://en.wikipedia.org/wiki/Ras_Laffan_Industrial_City
[2] OpenStreetMap/Photon (ODbL) — "Port Gate 2", hergebruikt uit `gas-raslaffan-chiba.md`. https://www.openstreetmap.org
[3] Wikipedia, "South Pars/North Dome Gas-Condensate field" — North Field-referentiecoördinaat, hergebruikt.
    https://en.wikipedia.org/wiki/South_Pars/North_Dome_Gas-Condensate_field
[4] Gate terminal (Vopak/Gasunie), "Profiel: Facts & Figures" — 12 bcm/j, Tank 4-project, hergebruikt uit
    `gas-sabinepass-rotterdam.md`. https://www.gateterminal.com/en/gate-terminal/profiel/facts-figures/
[5] Wikipedia (NL), "Gate terminal" — 51,97111/4,06889, hergebruikt uit `gas-sabinepass-rotterdam.md`.
    https://nl.wikipedia.org/wiki/Gate_terminal
[6] QatarEnergy, officiële website — North Field-uitbreiding/LNG-capaciteit. https://www.qatarenergy.qa
[7] IEA, Global LNG Capacity Tracker. https://www.iea.org/data-and-statistics/data-tools/global-lng-capacity-tracker
[8] Wikipedia, "Red Sea crisis" — Houthi-aanvallen op scheepvaart sinds eind 2023, deel van het
    Midden-Oosten-conflict 2023–heden. https://en.wikipedia.org/wiki/Red_Sea_crisis
[9] ISDO, "Analysis of maritime geopolitics on early 2026: The Red Sea Factor" (feb 2026) — Rode Zee-verkeer
    −57,5%, Suez-containerverkeer −90% (dec 2023–mrt 2024), begin 2026 nog 60% onder pre-crisisniveau,
    Kaap-omleiding +74–191%, 4.000–5.000 zeemijl/10–14 dagen extra. https://isdo.ch/analysis-of-maritime-geopolitics-on-early-2026-the-red-sea-factor/
[10] S&P Global Market Intelligence, research (feb 2026, via zoekresultaten) — Bab-el-Mandeb "matig"
    dreigingsniveau (april 2026), Houthi-pauze na Gaza-bestand okt. 2025, dreiging met hervatting.
    https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/02/red-sea-shipping-reopens
[11] PressReader (Business Weekly Zimbabwe, wire-content) — LNG-vloot mijdt Rode Zee, Qatar grootste
    LNG-gebruiker van de corridor. https://www.pressreader.com/zimbabwe/business-weekly-zimbabwe/20240119/281827173626046
[12] `gas-raslaffan-chiba.md` / `gas-sabinepass-rotterdam.md` (deze repo) — bron van de hergebruikte
    ankers, geojson-bestanden en km-metingen.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 4)

**Recept:** `bak_gas_raslaffan_rotterdam()` in `v2/tools/bak_stromen.sh`, direct vóór de
dispatch-ankerregel. Geen nieuw wegprofiel, geen nieuwe satellietpas, geen nieuwe
Geofabrik-extract — conform de bak-aanwijzing van de brief.

| # | modaliteit | km | punten | stippel? | recept |
|---|---|---|---|---|---|
| b1 | leiding | 84,7 | 2 | ja (rechte lijn) | **letterlijke kopie** van `bak_gas_raslaffan_chiba`'s `--stippel`-regel (26,6191/51,9500 → 25,9265/51,5955) — geen nieuwe geometrie gezocht |
| b2a | zee | 41,6 | 20 | ja (`--stippel-geojson`) | **letterlijke kopie**: verwijst naar het bestaande `v2/build-cache/ais/graaf/gas-raslaffan-chiba-aanloop-raslaffan.geojson` van as 2; `maak_havenaanloop.py` niet opnieuw gedraaid |
| b2b | zee | 11.891,6 | 1.247 | nee | **nieuw** MARNET-been, kade → kade, zeeknoop 4090 (26,30000/51,60000) → Gate-kade Rotterdam (51,97110/4,06890) |
| **totaal** | | **12.017,9** | **1.269** | | 2 markers |

**Naden:** b1→b2a **0,000 km**, b2a→b2b **0,000 km** — beide identiek aan as 2, zoals
verwacht (dezelfde gedeelde geometrie). b2b snapt zelf op 0,000 km bij de kop (zeeknoop)
en op 1,836 km bij de staart (Gate-kade Rotterdam) — dezelfde ~1,8 km die in as 1
(`gas-sabinepass-rotterdam`) al gemeten is: anker ≠ routeerpunt, binnen de 5 km-norm,
geen tweede haven-aanloop nodig.

**`toets_knikken.py`:** 3 knikken ≥60° (70,5° bij 22,70000/60,40000 · 64,9° bij
52,00000/3,90000 · 64,2° bij 36,80000/-9,25000), **0 omkeringen ≥150°, 0 terugloop** —
alle drie zijn gewone bochten in de MARNET-vaargeul (Hormuz-omgeving, Noordzee-invaart,
Portugese kust), geen routerfout.

**`toets_rechte_benen.py --min-km 5`:** b1 en b2a verschijnen als **GROOT (stippel)**
met omwegfactor 1,000/1,002 — precies zoals verwacht (rechte stippel/schematische
aanloop, dezelfde uitslag als as 2). b2b (11.891,6 km, 1.247 punten) verschijnt terecht
niet in die lijst: geen rechte lijn, een echte gerouteerde zeecorridor.

**km-toets (zacht, ±15% indicatief):** de brief geeft ~11.000–12.000 km als
ontwerp-indicatie voor b2b (geen gepubliceerde ladingroute-lengte). Gemeten b2b =
11.891,6 km, totaal 12.017,9 km — **binnen** de gegeven bandbreedte. Geen bevinding.

**MARNET-routekeuze (bevinding voor de brief, geen bak-keuze):** MARNET kiest zelf de
geografisch kortste route en routeert **via Hormuz → Bab-el-Mandeb → Rode Zee → Suez**
(het been passeert 22,70000/60,40000 nabij Hormuz/Arabische Zee, 36,80000/-9,25000 bij
Portugal — dus via Gibraltar/Atlantische kust, niet via de Kaap). Dit bevestigt §7 van de
brief: de **kaart** toont de geografisch kortste (Suez-)route, terwijl de **praktijk**
sinds eind 2023 grotendeels via de Kaap de Goede Hoop omleidt vanwege de Rode-Zee-crisis
— dat verschil is precies de "as ondergraven door haar eigen risico"-kern van deze brief,
en is bewust niet in de kaart geforceerd.

**JSON-contract:** `versie` 2, `punt_formaat` lonlat, alle modaliteiten in
{zee, leiding} ⊂ de toegestane set, elk been ≥ 2 punten, bestandsgrootte 23,0 KB (ruim
onder de norm).

**Lessen:** geen nieuwe — deze as bevestigt dat een reserve-as volledig uit hergebruikte
benen/ankers kan worden samengesteld zonder nieuw veldwerk, zolang de gedeelde stukken
(hier: b1 en b2a met as 2) letterlijk worden gekopieerd in plaats van herbakken.
