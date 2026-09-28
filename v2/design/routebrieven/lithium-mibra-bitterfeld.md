# Routebrief (licht) · lithium — Mibra (Brazilië) → Vitória → Hamburg → Bitterfeld (Duitsland)

**stroom-id:** `lithium-mibra-bitterfeld` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat van AMG's eigen Mibra-mijn/-concentrator (Volta Grande, Nazareno, Minas Gerais) — waar sinds 2024 óók de technisch-gradig Li-zoutconversie op hetzelfde terrein staat — gaat per **truck** naar de exporthaven **Porto de Vitória**, per **bulkschip** de Zuid-Atlantische Oceaan over naar **Hamburg**, en per **truck** naar AMG Lithium's hydroxideraffinaderij in **Bitterfeld-Wolfen**, waar het tot battery-grade LiOH·H₂O wordt gezuiverd — herstelt de golf 2-fout (niet Chili/Lanegra maar Mibra/Brazilië voedt Bitterfeld).
**Welke as van het verhaal:** AMG's eigen mijn-tot-raffinaderijketen (twee eigen sites, één bedrijf). Mibra: spodumeenproductie ~90 kt/j nu → 130 kt/j na uitbreiding (AMG-bedrijfspagina; IBRAM/persberichten 2026 bevestigen de uitbreiding) [1][5]. Bitterfeld: eerste-fase battery-grade LiOH ~20 kt/j (≈18 kt LCE, al `w-li-bitterfeld` in de sitelaag), doel 100 kt LiOH/j in 2030 (AMG/Fastmarkets, juli 2025) [3][4].

## 1 · Ketenkaart
```
AMG Mibra-mijn/concentrator+chem.plant `li-mibra-plant` ──(b1 truck · BR-265→BR-356→ES-297→BR-101 · ~619 km, OSRM-referentie)──►
Porto de Vitória `li-vitoria-kade` (hergebruikt anker)
  ──(b2 zee · haven-aanloop, stippel, 102,7 km — letterlijke kopie uit lithium-cirilo-vitoria.md b2)──► zeeknoop 900 (-20,00000,-39,50000)
  ──(b3 zee · Zuid-Atlantische Oceaan, MARNET beslist · hemelsbreed ~9.446 km, geen zeekm-citaat)──► Hamburg CTB-kade `li-hamburg-ctb-kade`
  ──(b4 truck · A7→A2→A14→B6/B185→B183 · ~363 km, OSRM-referentie)──► AMG Lithium Bitterfeld `li-bitterfeld-plant` ⏹ stoppunt (battery-grade LiOH·H₂O)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `li-mibra-plant` → `li-vitoria-kade` | LMG-841 → BR-265 (São João del-Rei–Barbacena–Mercês) → BR-265/MGC-265 → MG-285 → MG-447 (Cataguases) → BR-356 (Muriaé–Itaperuna) → RJ-186 → ES-297 (Mimoso do Sul) → BR-101 (Itapemirim–Vitória) | ~619 (OSRM-wegreferentie over reëel OSM-net; geen officiële bronopgave) [10] | maak_stroombeen_weg, extract `brazilie` | nee |
| b2 | B | zee (haven-aanloop) | `li-vitoria-kade` → zeeknoop 900 | Baía de Vitória → open Atlantische kust | 102,7 (gemeten; letterlijke kopie van b2 uit `lithium-cirilo-vitoria.md` §9) | **letterlijke kopie** `lithium-cirilo-vitoria-aanloop-vitoria.geojson` | ja — haven-aanloop (bestaand, hergebruikt) |
| b3 | B | zee (bulkschip) | zeeknoop 900 → `li-hamburg-ctb-kade` | Zuid-Atlantische Oceaan → Noordzee, geen zeestraat; kade < 5 km van zeeknoop 3944 (1,8 km gemeten) → geen tweede haven-aanloop nodig | hemelsbreed ~9.446 (eigen berekening tussen de twee zeeknopen); geen zeekm-citaat — MARNET bepaalt de route | MARNET | nee; *aannemelijk: route via China niet uitgesloten, zie §7* |
| b4 | C | truck | `li-hamburg-ctb-kade` → `li-bitterfeld-plant` | A7 (Wedemark–Lehrte) → A2 (Peine–Hohe Börde/Magdeburg) → A14 → B6/B185 (Bernburg) → B183 (Südliches Anhalt) | ~363 (OSRM-wegreferentie over reëel OSM-net; geen officiële bronopgave) [10] | maak_stroombeen_weg, extracts `de-hamburg`+`de-niedersachsen`+`de-sachsen-anhalt` | nee |

## 3 · Ankers (één per site en per overslag; 4 decimalen, lat, lon)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-mibra-plant` | mijn + concentrator + chem.-conversieterrein (één site) | AMG Brasil, Mina/Complexo Volta Grande (Mibra), Rodovia LMG-841, Zona Rural, Nazareno, MG | -21.0834, -44.5893 | [1][2][6][9] | bron-gelegd (z15/z16 gezien: open-pit mijncomplex met meerdere putten en een tailings-/loogveld aan weerszijden van een rivierbocht, plus een cluster proces-/fabrieksgebouwen direct aan de pit-rand — AMG's eigen materiaal zegt expliciet dat het technisch-gradig conversieproces "installed at the Mibra Mine site" wordt/is [2], dus fase A vervalt als los been: dit ÉÉN anker dekt mijn, concentrator én chemisch conversieterrein) |
| `li-vitoria-kade` | overslag truck → zee | Porto de Vitória, Vila Rubim / Cais Comercial | -20.3238, -40.3477 | [8] = hergebruik uit `lithium-cirilo-vitoria.md` §3 | bron-gelegd (hergebruikt; oorspronkelijk z15 satelliet-gelegd voor die brief) |
| `li-hamburg-ctb-kade` | overslag zee → truck | HHLA Container Terminal Burchardkai, Waltershofer Hafen, Hamburg | 53.5290, 9.9278 | [11][12] | bron-gelegd (z15 gezien: containerterminal met kraanbanen en stacks op de kop van het Waltershofer schiereiland, kade direct aan het diepe vaarwater; welk specifiek kadevak lithiumzout-containers laadt is niet per lading gebrond — zie §7) |
| `li-bitterfeld-plant` | raffinaderij (battery-grade LiOH) | AMG Lithium GmbH, Liebigstraße 10, Chemiepark Bitterfeld-Wolfen Areal A | 51.6522, 12.2580 | [3][13][14] | bron-gelegd (z15 gezien: industrieel chemiepark-complex bij de Liebigstraße, binnen Areal A; **verbetering** t.o.v. het bestaande sitelaag-anker `w-li-bitterfeld` (51.6167,12.3167, status "aannemelijk", stadscentroïde) — niet op het specifieke ketelhuis/gebouw uitgezoomd, wel op het juiste bedrijventerrein aan het juiste adres) |

## 4 · Via-punten (b1 en b4 — corridorkeuzes op de doorgaande weg)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | São João del-Rei (BR-265) | -21.1490, -44.2516 | pint de oostwaartse BR-265-corridor vanaf de lokale AMG-0445/LMG-841-toegangswegen |
| b1 | 2 | Barbacena (BR-265×BR-040-kruising) | -21.2004, -43.7492 | pint doorgaan op BR-265/BR-040 i.p.v. BR-040 zuidwaarts naar Rio |
| b1 | 3 | Mercês (BR-265/MGC-265) | -21.2334, -43.4242 | pint de doorgaande Zona-da-Mata-corridor |
| b1 | 4 | Cataguases (MG-285/MG-447) | -21.3640, -42.6742 | pint de afslag naar MG-447 i.p.v. verder op MG-285 |
| b1 | 5 | Muriaé (BR-356) | -21.1267, -42.3395 | pint instap op BR-356 richting Itaperuna |
| b1 | 6 | Itaperuna, RJ (BR-356→RJ-186) | -21.2095, -41.8550 | pint de statgrensoversteek MG→RJ→ES via RJ-186 |
| b1 | 7 | Itapemirim, ES (ES-297→BR-101) | -20.9252, -41.0778 | pint de instap op BR-101 noordwaarts naar Vitória |
| b4 | 1 | Wedemark (A7) | 52.5451, 9.7982 | pint de A7 zuidwaarts voorbij Hamburgs zuidrand |
| b4 | 2 | Lehrte (A7×A2) | 52.3903, 9.9593 | pint de overstap op A2 i.p.v. verder op A7 naar Hannover |
| b4 | 3 | Peine (A2) | 52.3362, 10.2684 | pint de doorgaande A2-corridor oostwaarts |
| b4 | 4 | Hohe Börde (A2×A14, bij Magdeburg) | 52.1613, 11.5446 | pint de overstap op A14 zuidwaarts i.p.v. A2 verder oost |
| b4 | 5 | Bernburg (A14→B6/B185) | 51.8041, 11.6978 | pint de afslag van de snelweg naar de B-wegen |
| b4 | 6 | Südliches Anhalt (B183) | 51.7332, 12.0079 | pint het laatste stuk B183 naar Bitterfeld-Wolfen |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Volta Grande/Mibra-complex (mijn + concentrator + chem.-conversie) | AMG Brasil S.A. (100%) | ROM-erts → spodumeenconcentraat → technisch-gradig Li-zout | ~90 kt spodumeen/j nu → 130 kt/j na uitbreiding; technisch-gradig-volume niet los gepubliceerd | [1][5][9] |
| AMG Lithium Bitterfeld-Wolfen | AMG Lithium GmbH | technisch-gradig Li2CO3/LiOH → battery-grade LiOH·H2O | eerste fase ~20 kt LiOH/j (≈18 kt LCE); doel 100 kt/j in 2030 | [3][4] |

## 6 · Stoppunt
De brief stopt bij battery-grade LiOH·H2O in Bitterfeld: dat is het eindproduct van AMG's eigen raffinaderij en geen bron noemt een specifieke Europese batterijfabriek als vaste afnemer voor deze ronde (fase D vervalt).

## 7 · Open punten
- **⚠️ Belangrijkste vondst, contrair aan de ontwerpaanname:** Fastmarkets citeert AMG-CEO Fabiano Costa (juli 2025, evenement "Lithium Business Brazil"): *"Our current plan is to have a chemical converter plant in Brazil, instead of sending the spodumene concentrate to China first and then Germany, **as we currently do**."* [15] Dit suggereert dat de vandaag werkelijk gevaren route mogelijk **Mibra → China (tolling-conversie) → Bitterfeld** is, niet de rechtstreekse Atlantische oversteek die deze brief tekent — consistent met de "tolling arrangements until 2026" die de S&P Global-bron in het ontwerp al noemde. AMG's eigen value-chain-pagina [2] beschrijft de Brazilië-conversiefabriek nog in de toekomende tijd ("will be realized"). Deze brief tekent desondanks de **rechtstreekse** as, want dat is wat de haalbaarheidstoets (bindend) opdraagt en wat AMG als eigen structurele mijn-tot-raffinaderijketen presenteert [9] — maar een volgende ronde zou moeten checken of een aparte keten `lithium-mibra-china` de vandaag werkelijk gevaren lading beter dekt.
- **Braziliaans conversieterrein niet apart satellietgelegd, maar wél colocatie-bewijs:** AMG's eigen tekst plaatst de technisch-gradig-fabriek "at the Mibra Mine site" [2] — vandaar één anker; geen los adres voor een chemisch-conversiegebouw gevonden.
- **Exacte laadkade Vitória en Hamburg per lading niet gebrond** (zie ook `lithium-cirilo-vitoria.md` §7 voor Vitória).
- **Truck- en zeekm zijn referentieschattingen** (OSRM resp. eigen grootcirkelberekening tussen zeeknopen), geen gepubliceerde bronopgave — wordt bij het bakken vervangen door de gemeten weg-/zeegeometrie.
- **Bitterfeld-anker op bedrijventerreinniveau**, niet op het specifieke ketelhuis — sitelaag-correctie voorgesteld in §3, nog niet doorgevoerd in `lithium-sitelaag.json`.
- **Volume Braziliaans tussenproduct** (technisch-gradig Li-zout) niet gepubliceerd; alleen mijn- en Bitterfeld-eindvolumes zijn bekend.

## 8 · Bronnen
[1] AMG Lithium, "About Us", https://amglithium.com/company/about-us (Mibra: "mining expertise... for more than half a century and production of spodumene concentrate")
[2] AMG Lithium, "Value Chain", https://amglithium.com/company/value-chain ("a lithium chemical plant for the conversion of spodumene concentrate to technical grade lithium salts to be installed at the Mibra Mine site")
[3] Fastmarkets, 2025-07-16, Leticia Simionato, "Brazilian lithium producers plan expansions amid falling prices" — AMG-CEO Fabiano Costa-citaat, 100 kt LiOH/j-doel 2030, 14% EU-marktaandeel, https://www.fastmarkets.com/insights/brazilian-lithium-producers-plan-expansions-amid-falling-prices/
[4] AMG-persmateriaal / sitelaag `w-li-bitterfeld` (18 kt LCE-equivalent eerste fase), v2/design/lithium-sitelaag.json
[5] IBRAM, "AMG revê projeção de mina em Nazareno", https://ibram.org.br/noticia/amg-reve-projecao-de-mina-em-nazareno/ (uitbreidingsproject Mina Volta Grande)
[6] AMG Brasil, bedrijfspagina 404 met contactadressen (Critical Minerals Unit: "Rodovia LMG 841, Volta Grande, Zona Rural, Nazareno, MG, Brasil, Cep: 36370-000"), https://amg-br.com/business/critical-minerals/spodumene-concentrate/
[7] Wood Mackenzie, "Mibra — Lithium mine Report" (titel/metadata via zoekresultaat, volledige tekst niet geraadpleegd — betaald rapport), https://www.woodmac.com/reports/metals-mibra-lithium-mine-553862/
[8] `v2/design/routebrieven/lithium-cirilo-vitoria.md` §3/§9 — ankers `li-vitoria-kade` en het gebakken been b2 (haven-aanloop 102,7 km), hergebruikt.
[9] S&P Global Commodity Insights, 2024-09-23, interview AMG Lithium-CEO ("a supply chain connecting Mibra Mine (spodumene) in Brazil to a German Refinery in Bitterfeld, with tolling arrangements until 2026") — URL uit de opdracht niet ophaalbaar (403/leeg via curl en WebFetch), inhoud overgenomen uit de haalbaarheidstoets van de opdracht zelf.
[10] OSRM (router.project-osrm.org, routeert over OpenStreetMap-wegdata — dezelfde bron als de Geofabrik-extracts van de bake), driving-route `li-mibra-plant`→`li-vitoria-kade` (619,2 km) en `li-hamburg-ctb-kade`→`li-bitterfeld-plant` (362,7 km), opgevraagd 2026-09-28. Geen officiële bronopgave, referentieschatting (patroon uit `koper-aurubis-hamburg.md` §8).
[11] OpenStreetMap/Nominatim (ODbL) — "Container Terminal Burchardkai", Waltershof, Hamburg, https://www.openstreetmap.org
[12] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16, live): `v2/build-cache/satcheck/sat-lithium-mibra-bitterfeld-{mibra-estanho,mibra-plant,hamburg-ctb,arealA-wide}.png`.
[13] OpenStreetMap Overpass (maps.mail.ru-spiegel) — quarry-vlak met notitie "Estanho" (tin) op -21.0889799,-44.5921449 binnen het Volta Grande-mijncomplex; Nominatim "Liebigstraße", Chemiepark Bitterfeld-Wolfen Areal A.
[14] StepStone/TGZ Chemie/IWR/Chemietechnik-zoekresultaten (adresbevestiging Liebigstraße 10, 06766 Bitterfeld-Wolfen; Areal A), o.a. https://tgzchemie.de/news/schluesseluebergabe-an-die-amg-lithium-gmbh-im-technologie/
[15] Fastmarkets, zie [3] — CEO-citaat over de huidige (2025) routing via China, zie §7.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Stroom `lithium-mibra-bitterfeld`** → `v2/data/stroomroute-lithium-mibra-bitterfeld.json` — 4 benen,
**10.760,0 km**, 19.060 punten, 4 markers. truck 655,0 + zee 102,7 (stippel) + zee 9.646,1 + truck 356,2
km. Recept: `bak_stromen.sh` (functie `bak_lithium_mibra_bitterfeld`).

**b1 (truck, `maak_stroombeen_weg.py --profiel lithium-mibra-bitterfeld-mibra-vitoria --bron geofabrik`,
extract `brazilie`):** AMG Mibra-mijn → São João del-Rei → Barbacena → Mercês → Cataguases → Muriaé →
Itaperuna → Itapemirim → Porto de Vitória, **655,0 km** (13.139 punten, na 55 gesnoeide keerlussen van
654,8 → 654,6 km ruw). Tegen de OSRM-wegreferentie van 619,2 km uit de bak-aanwijzingen = **+5,8%**,
binnen ±10%. ⚠️ **Eerste run met alleen `refs: ["BR-265","BR-356","BR-101"]` gaf 742,4 km (+19,9%,
buiten de indicatie):** zonder soft-preference op de staatswegen RJ-186/ES-297 koos de scanner tussen
Itaperuna en Itapemirim een omweg van 207,9 km tegen 86,6 km hemelsbreed (ratio 2,4). `refs` uitgebreid
naar `["BR-265","BR-356","RJ-186","ES-297","BR-101"]` (exact de wegen uit de brief-corridor, geen
via-punt bijgeschoven) → dat segment viel terug naar 120,2 km en het totaal naar 654,6 km/+5,8%. Geen
`corridorKlassen`/`eindToegangPrivaat` nodig; anker-verbindingen (buiten de lengtetoets): plant → weg
0,34 km, weg → kade 0,01 km.

**b2 (zee, stippel, LETTERLIJKE KOPIE):** geen nieuwe `maak_havenaanloop.py`-run — het bestaande
geojson `v2/build-cache/ais/graaf/lithium-cirilo-vitoria-aanloop-vitoria.geojson` (been b2 uit de
gebakken stroom `lithium-cirilo-vitoria`, functie `bak_lithium_cirilo_vitoria`) is rechtstreeks
hergebruikt via `--stippel-geojson`. **102,7 km · 87 punten**, Porto de Vitória → zeeknoop 900,
identiek aan de eerder gebakken uitkomst.

**b3 (zee, MARNET, geen stippel):** `--been "zee|...|-20.00000,-39.50000|53.5290,9.9278"`, startend op
de zeeknoop van b2. Snap zeeknoop 0,000 km, snap Hamburg CTB-kade **1,791 km** (ruim onder de
5 km-drempel uit de bak-aanwijzingen — geen tweede haven-aanloop aan de Duitse kant nodig, bevestigt de
vooraf gedane zeeknoop-check op zeeknoop 3944/1,8 km). Resultaat **9.646,1 km over 86 MARNET-edges**
(1.010 punten) tegen de eigen hemelsbreed-berekening ~9.446 km tussen de zeeknopen uit de brief = **+2,1%**
(geen gepubliceerde zeekm-bron, dus indicatie, geen norm). Lengte-invariant: getekende lijn 9.646,112 km
vs som edge-km 9.646,500 km = -0,388 km (de naden).

**b4 (truck, `maak_stroombeen_weg.py --profiel lithium-mibra-bitterfeld-hamburg-bitterfeld --bron
geofabrik`, extracts `de-hamburg`+`de-niedersachsen`+`de-sachsen-anhalt`):** HHLA Container Terminal
Burchardkai → Wedemark → Lehrte → Peine → Hohe Börde → Bernburg → Südliches Anhalt → AMG Lithium
Bitterfeld-Wolfen, **356,2 km** (4.824 punten, na 66 gesnoeide keerlussen van 356,3 → 356,2 km ruw).
Tegen de OSRM-wegreferentie van 362,7 km = **-1,9%**, binnen ±10%. ⚠️ **Eerste run zonder
`eindToegangPrivaat` gaf "geen wegpad tussen punt 0 en 1"** — de containerterminal-toegangswegen bij
Burchardkai vielen buiten het default-toegangsfilter (airside/privéterrein-klasse, bakhandleiding §2,
zelfde familie als de vrachtplatform-last-mile bij goud/PGM). `eindToegangPrivaat: True` toegevoegd aan
het profiel, geen `eindKlassen`-wijziging nodig. Anker-verbindingen: plant → weg 0,02 km, weg → kade
0,06 km.

**Toets naden:** b1→b2 en b2→b3 **0,000 km** (letterlijk gedeeld eindpunt/zeeknoop). b3→b4 **1,791 km**
(= de zee→Hamburg-kade-snap zelf, ruim onder de 5 km-norm — geen tweede haven-aanloop, geen fix nodig).

**`toets_knikken.py`:** 36 knikken ≥60°, **0 omkeringen ≥150°, 0 terugloop**. Alle 27 spikes op b1 en
9 spikes op b4 zijn kleine-straal (4–60 m) OSM-zigzag op via-punten/kruisingen/anker-aansluitingen —
geen van alle is een omkering. Het zeebeen b3 heeft 0 knikken.

**`toets_rechte_benen.py --min-km 5`:** geen been van deze stroom in de uitslag — ook b2 (de stippel,
102,7 km) wordt niet als verdachte rechte lijn aangemerkt.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, zee} (binnen de
toegestane set), elk been ≥2 punten (minimum 87), bestandsgrootte **392,3 KB** — boven de ~300 KB-
richtwaarde uit de handleiding (§5.3), door de twee lange, dicht bemonsterde truckbenen (17.963 punten
samen) plus het 1.010-punts zeebeen; geen harde norm, wel een bevinding voor het rapport.

**Markers:** alle vier de ankers uit §3 op **0,0 m** van de lijn (li-mibra-plant, li-vitoria-kade,
li-hamburg-ctb-kade, li-bitterfeld-plant) — elk anker is zelf het been-uiteinde, geen losse snap.

**Gereedschapslessen:** een refs-lijst die alleen de nationale hoofdwegen noemt (BR-265/BR-356/BR-101)
en de tussenliggende staatswegen (RJ-186/ES-297) weglaat, kan de scanner een grove omweg laten kiezen
op precies het stuk zonder soft-preference — voeg bij een gemengde nationaal/staats-corridor ALLE
benoemde wegen uit de brief toe aan `refs`, niet alleen de grootste. En: een containerterminal-anker
(Hamburg CTB) vraagt vaak `eindToegangPrivaat` net als een mijnterrein of vrachtplatform — de
toegangswegen binnen een haventerminal zijn typisch met een access-restrictie gekarteerd.

⚠️ **Belangrijkste inhoudelijke bevinding (brief §7, GEEN bak-blokkade):** het Fastmarkets-citaat van
AMG-CEO Fabiano Costa (juli 2025) suggereert dat de vandaag werkelijk gevaren route mogelijk via China
(tolling) loopt i.p.v. rechtstreeks Mibra→Bitterfeld. Deze brief tekent bewust de rechtstreekse
Atlantische as die de haalbaarheidstoets opdraagt en die AMG als eigen structurele mijn-tot-
raffinaderijketen presenteert — een vervolgronde zou moeten uitzoeken of een aparte keten
`lithium-mibra-china` de vandaag werkelijk gevaren lading beter dekt.
