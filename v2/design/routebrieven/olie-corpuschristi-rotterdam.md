# Routebrief (licht) · olie — Corpus Christi (VS) → Rotterdam/Pernis (Nederland)

**stroom-id:** `olie-corpuschristi-rotterdam` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31) · **status:** gebakken
**Keten in één zin:** Amerikaanse schalie-ruwe olie (WTI, vooral Permian-herkomst) die via de Corpus Christi
Ship Channel-exportterminals bij Ingleside, Texas, per **VLCC/Suezmax** de Golf van Mexico uit vaart — Straat van
Florida, Noord-Atlantische Oceaan, Nauw van Calais/Noordzee — naar de Maasvlakte Olie Terminal (MOT) in Rotterdam,
de gezamenlijke crude-importsteiger die ~1/3 van alle ruwe olie voor het Rotterdam/Pernis-raffinagecluster aanlandt.
**Welke as van het verhaal:** *de Amerikaanse schalie-ommekeer* — de VS als netto-exporteur i.p.v. -importeur.
Corpus Christi exporteerde 130,5 Mt (~956 mln vaten, gem. ~2,6 mln vaten/dag) ruwe olie in 2024, een record en het
zevende recordjaar op rij, goed voor ~50% van alle Amerikaanse ruwe-olie-export en de #3-exportpoort wereldwijd na
Ras Tanura en Al Basrah [1][2][6]. Rotterdam ontvangt jaarlijks 95-100 Mt ruwe olie, hoofdzakelijk uit de VS en de
Noordzee [3].

## 1 · Ketenkaart
```
Corpus Christi Ship Channel-exportterminals `ol-corpuschristi-term` (Ingleside, TX)
   ──(b1 zee · Golf van Mexico → Straat van Florida → Noord-Atlantische Oceaan → Nauw van Calais/Noordzee ·
       ~9.300 km, MARNET; aannemelijk: aggregaatcijfers beide zijden, geen cargoniveau-bron)──►
   Maasvlakte Olie Terminal `ol-rotterdam-mot` (Rotterdam) ── stoppunt (ARA-raffinagecluster)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | Corpus Christi-exportterminals → Maasvlakte Olie Terminal | Golf van Mexico → Straat van Florida → Noord-Atlantische Oceaan → Nauw van Calais/Noordzee | ~9.300 [ontwerp, hemelsbreed-schatting; geen gepubliceerde routelengte] | MARNET (kade → kade) | nee — beide kades ruim binnen zeeknoop-bereik (haalbaarheidstoets: ≤7,7 km) |

Geen leg A/C/D/E: beide uiteinden zijn zelf al de kade (exportterminal resp. importterminal); er is geen
gedocumenteerd land-voortraject of downstream-fabriek die deze specifieke keten met naam verbindt (zie §6).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-corpuschristi-term` | laadplek / exportterminal | South Texas Gateway Terminal (Gibson Energy), Ingleside, Corpus Christi Ship Channel — representatief voor het exportcomplex incl. Enbridge Ingleside Energy Center en Moda, alle binnen ~2 km op dezelfde kanaaloever | 27.82677, -97.19447 | [4][8][9] | bron-gelegd (z15 gezien: tankenpark van ~20 opslagtanks direct aan een kade met twee aangemeerde tankers/lichters aan een steiger die de vaargeul in steekt — komt overeen met de "twee deepwater docks" uit [4]) |
| `ol-rotterdam-mot` | losplek / crude-importsteiger (voedt het raffinagecluster) | Maasvlakte Olie Terminal (BP/Esso/Shell/TotalEnergies/Vopak/Aramco Overseas), Maasvlakte, Rotterdam | 51.97273, 4.06243 | [5][8][9] | bron-gelegd (z15 gezien: tankenpark van ~39 grote opslagtanks op het schiereiland met twee steigers de Nieuwe Waterweg/Noordzee in, tankers afgemeerd — komt overeen met "twee deepwater berths, ULCC tot 400.000 dwt" uit [5]) |

Beide ankers vervangen de v1-checklistpunten (stads-/marktcentroïdes `oil-term-corpus` 27.80,-97.40 en
`oil-ref-rotterdam` 51.90,4.10 uit `data/oil.js`) door site-niveau terminals — een centroïde is geen anker.

## 4 · Via-punten
Geen — b1 is de enige been en wordt kade → kade door de MARNET-router gelegd; er is geen corridorkeuze te
benoemen op dit schaalniveau (open oceaan, geen zeestraat-flessenhals, zoals het ketenontwerp al aangaf).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Maasvlakte Olie Terminal | BP · Esso · Shell · TotalEnergies · Vopak · Aramco Overseas (elk 16,7%) | ruwe olie (VLCC/ULCC) → via pijpleidingnet naar de ARA-raffinaderijen (o.a. Shell Pernis) | 39 tanks × 114.000 m³ = 4,4 mln m³ opslag; ~1/3 van alle Rotterdamse crude-import; pijplijn tot 140 km (Zeeland Refinery, Vlissingen) | [5] |

## 6 · Stoppunt
De brief stopt bij de poort van de Maasvlakte Olie Terminal: dat is de gezamenlijke crude-importsteiger die het
Rotterdam/Pernis-raffinagecluster bevoorraadt via een pijpleidingnet naar de deelnemende raffinaderijen. Geen bron
noemt welk deel van de MOT-aanvoer specifiek uit Corpus Christi komt of welke raffinaderij (Pernis, Vlissingen, …)
de Amerikaanse partij verwerkt — fase C/D/E vervallen, in lijn met de risiconoot van het ketenontwerp.

## 7 · Open punten
- **Geen bron splitst de Corpus Christi-export naar bestemming op cargoniveau** — dit blijft de kern van de
  risiconoot uit het ketenontwerp. Eigen check van de door de haalbaarheidstoets aangehaalde bron
  (discoveryalert.com) bevestigt de daar geclaimde uitspraak "Nederland is de #1-exportmarkt" NIET: het woord
  "Netherlands" komt in die paginatekst niet voor, en er is geen MoU tussen Port of Corpus Christi en Port of
  Rotterdam gevonden (ook niet in Rotterdam's eigen persberichtenoverzicht). De oorspronkelijke, voorzichtigere
  risiconoot van het ketenontwerp is dus de houdbare — de webcheck-verzachting uit de haalbaarheidstoets is niet
  bevestigbaar en wordt niet overgenomen.
- **Welke terminal(s) exact de Rotterdam-gebonden ladingen laden** binnen het Corpus Christi Ship Channel-complex
  (Enbridge Ingleside Energy Center, Moda, South Texas Gateway, Flint Hills, EPIC) is niet gebrond — het anker
  `ol-corpuschristi-term` staat op de best gedocumenteerde en satelliet-bevestigde site (South Texas Gateway) als
  representant van het hele exportcomplex.
- **Welke raffinaderij(en) in het Rotterdam/Pernis-cluster** de Amerikaanse aanvoer via MOT daadwerkelijk verwerkt
  (Shell Pernis specifiek, of een ander ARA-lid) is niet met naam gebrond.
- **Geen gepubliceerde routelengte** voor de b1-corridor; ~9.300 km is een hemelsbreed-ontwerpschatting, de
  bak-agent meet de werkelijke MARNET-afstand.

## 8 · Bronnen
[1] Industrial Info Resources, 2025 — "Lifted by Crude, Port of Corpus Christi Set Export Record in 2024": 130,5 Mt ruwe olie, ~956 mln vaten, +3,5% jr/jr, zevende recordjaar op rij. https://www.industrialinfo.com/iirenergy/industry-news/article/lifted-by-crude-port-of-corpus-christi-set-export-record-in-2024--338383
[2] OilPrice.com — "Corpus Christi Is Now The World's Third Largest Oil Export Port": ~2,3-2,4 mln vaten/dag, #3 wereldwijd na Ras Tanura en Al Basrah, ~50% van alle VS-ruwe-olie-export, 99% naar buitenlandse markten. https://oilprice.com/Energy/Crude-Oil/Corpus-Christi-Is-Now-The-Worlds-Third-Largest-Oil-Export-Port.html
[3] Port of Rotterdam, "Crude oil" — 95-100 Mt ruwe olie/jaar naar Rotterdam, hoofdzakelijk bestemd voor raffinaderijen in Nederland/België/Duitsland; herkomst vooral VS en Noordzee; terminals in Europoort en op de Maasvlakte; ULCC's tot 500.000 dwt. https://www.portofrotterdam.com/en/logistics/cargo/liquid-bulk/crude-oil
[4] Gibson Energy — "South Texas Gateway Terminal": locatie Ingleside TX aan de monding van Corpus Christi Bay, 1 mln vpd vergunde doorzet, 8,6 mln vaten opslag in 20 tanks, twee deepwater docks (gelijktijdig 2 VLCC's), ~12% van de VS-ruwe-olie-export in 2023, tweede-grootste VS-exportterminal naar capaciteit. https://www.gibsonenergy.com/operations/south-texas-gateway-terminal/
[5] Wikipedia (NL) — "Maasvlakte Olie Terminal": eigendom BP/Esso/Shell/TotalEnergies/Vopak/Aramco Overseas elk 16,7%; twee diepwatersteigers tot 400.000 dwt/22 m diepgang; 39 tanks × 114.000 m³ = 4,4 mln m³; pijpleiding tot 140 km naar Zeeland Refinery Vlissingen; ~1/3 van de Rotterdamse crude-import. https://nl.wikipedia.org/wiki/Maasvlakte_Olie_Terminal
[6] discoveryalert.com, maart 2026 — "Port Corpus Christi crude oil exports: US export hub": ~2,4-2,5 mln vaten/dag (piek maart 2026), #3 wereldwijd, ~50% van de VS-export; noemt Europa/Zuid-Korea/Japan/India/China/Latijns-Amerika als afzetmarkten maar NIET Nederland met naam (eigen check, zie §7). https://discoveryalert.com/news/port-corpus-christi-crude-oil-exports-us-export-hub/
[7] Wikipedia (EN) — "Port of Corpus Christi": 2023 ruwe-olie-export ~126,1 Mt (+12,5% jr/jr), 2025-cijfer 127,4 Mt; ~60% van de VS-ruwe-olie-marktaandeel (aug. 2022); geen bestemmingslanden genoemd. https://en.wikipedia.org/wiki/Port_of_Corpus_Christi
[8] OpenStreetMap (ODbL) via Overpass — landuse "Buckeye Partners" (industrial/oil) 27,82677/-97,19447, adrespunt 200 FM 1069 Ingleside 27,82577/-97,19470 (South Texas Gateway Terminal-perceel); relation "Maasvlakte Olie Terminal" (industrial/oil) 51,97273/4,06243. https://www.openstreetmap.org
[9] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-olie-corpuschristi-rotterdam-corpuschristi.png`, `sat-olie-corpuschristi-rotterdam-mot.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze)

**Stroom `olie-corpuschristi-rotterdam`** → `v2/data/stroomroute-olie-corpuschristi-rotterdam.json` — 1 been, **9.589,8 km**, 1.709 punten, 2 markers (0 stippel).
Recept: `bak_stromen.sh` (functie `bak_olie_corpuschristi_rotterdam`).

**b1 (zee, MARNET-route, kade → kade):** `--been "zee|zeeschip Corpus Christi (South Texas Gateway) → Rotterdam (Maasvlakte Olie Terminal)|27.82677,-97.19447|51.97273,4.06243"` — snap Corpus Christi **0,835 km**, snap Rotterdam **1,727 km** (beide ruim binnen de 25 km-norm en de haalbaarheidstoets' ≤7,7 km, geen haven-aanloop gebouwd, conform de bak-aanwijzing). **9.589,8 km**, 1.709 punten, tegen de ontwerp-schatting ~9.300 km (hemelsbreed, geen gepubliceerde routelengte) = **+3,1%**, ruim binnen ±15% — al is die vergelijking hier minder betekenisvol dan bij een gepubliceerde routelengte (§7); de gemeten 9.589,8 km is voortaan de echte referentie. km-uitsplitsing volgens het bake-log: track-graaf 237,6 km (Golfkust-uitloop bij Corpus Christi) + MARNET-zee 9.351,9 km + 1 connector 0,08 km; lengte-invariant (getekende lijn vs som edge-km) **+0,208 km** = de naden, verwaarloosbaar.

**Markers:** `ol-corpuschristi-term` (**0,835 km** van de lijn — anker ≠ routeerpunt: de kade snapt op de dichtstbijzijnde MARNET-zeeknoop, ruim binnen de norm) · `ol-rotterdam-mot` (**1,727 km** van de lijn — zelfde categorie: de MOT-steiger ligt iets landinwaarts van de dichtstbijzijnde zeeknoop bij de Nieuwe Waterweg-monding, ruim binnen de norm).

**Naad:** geen — één been, dus geen naad tussen benen.

**Toets:** `toets_knikken.py` — 10 knikken ≥60° (grotendeels spikes van enkele meters straal in de Golfkust-uitloop bij Corpus Christi en op de Nauw-van-Calais-aanpak; twee krappe bochten van 5-7 km straal bij Florida/de Golfkust-uitloop en één van 5,5 km bij de Rotterdamse aanpak), **1 omkering ≥150° (170,2°, R=3 m, bij 28,897/-95,385)** waarvan **0 terugloop** — de omkering is een scherpe maar échte bocht (pad/hemelsbreed-verhouding 1,1) in de nauwe Corpus Christi Ship Channel-uitloop, geen bevinding. `toets_rechte_benen.py --min-km 5` — de stroom komt niet op de lijst voor (geen enkel been heeft een omwegfactor ≈1,000; dit is een volledig gemeten, gebogen MARNET-route). json geldig: versie 2, punt_formaat lonlat, modaliteit `zee` (in de toegestane set), been ≥2 punten (1.709), bestandsgrootte **33,3 KB** (ruim < 300 KB).

**Gereedschapslessen:**
- Voor een enkelvoudig zeebeen waarbij beide kades ruim binnen de 25 km-max-snap van een zeeknoop liggen, is de bak zelf triviaal (één `--been`-regel, geen via-punten, geen aanloop) — de haalbaarheidstoets uit de brief (≤7,7 km) bleek bij het bakken zelfs iets gunstiger uit te vallen (0,835/1,727 km).
- De "aannemelijk"-kwalificatie van de bestemmingskoppeling (Corpus Christi→Rotterdam specifiek niet cargoniveau bevestigd) hoort uitsluitend in de beennaam en de brief, en is hier ook zo gehouden — de lijnstijl blijft doorgetrokken, want stippel betekent in dit project uitsluitend "hier reikt het net niet", niet "onzeker gekoppeld".
- Eén enkele echte omkering (170,2°) in een nauwe scheepvaartgeul (Corpus Christi Ship Channel) is, gemeten via de pad/hemelsbreed-verhouding, een échte bocht en geen terugloop-artefact — bevestigt de vuistregel uit de bakhandleiding voor spoor/water: de 150°-drempel alleen is geen fout-signaal, de verhoudingsmaat beslist.
