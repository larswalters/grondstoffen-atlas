# Routebrief (licht) · gas — Sabine Pass (VS) → Rotterdam (Nederland)

**stroom-id:** `gas-sabinepass-rotterdam` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** Amerikaans schaliegas dat via het VS-pijpleidingnet (Appalachia/Permian/Haynesville, diffuus) bij de **Sabine Pass LNG Terminal** (Cheniere) tot **LNG** wordt verwerkt, per **LNG-carrier** de Golf van Mexico uit vaart — Straat van Florida, Atlantische Oceaan, Het Kanaal/Noordzee — naar de **Gate terminal** (Vopak/Gasunie) op de Maasvlakte, Rotterdam, waar het wordt hervergast en (niet getekend, korte terreinleiding) het Nederlandse GTS-gasnet invoedt.
**Welke as van het verhaal:** *de Europa-pivot van 2022* — de Atlantische LNG-route die na de wegval van Russisch pijpleidinggas het TTF-prijsgebied bevoorraadt. Sabine Pass: ~30 Mtpa (~41 bcm/j) nominale liquefactiecapaciteit, alle 6 treinen operationeel (peiljaar 2024–2026, bron Cheniere [1][2]). Gate: 12 bcm/j basis → 16–20 bcm/j na de 4e-tank-uitbreiding (peiljaar 2026, bron gateterminal.com/Wikipedia [3][4]). Het specifieke Sabine Pass→Rotterdam-cargovolume is **niet los gebrond** — LNG-tankers arbitreren tussen TTF (Europa) en JKM (Azië), dus dit is een corridor-/capaciteitsillustratie, geen gemeten ladingstroom (conform het ketenontwerp en de haalbaarheidstoets).

## 1 · Ketenkaart
```
(diffuus VS-schaliegasnet — geen enkelvoudig anker, fase A vervalt)
   ──► Sabine Pass LNG Terminal `gas-sabinepass-laad` (Cameron Parish, Louisiana)
   ──(b1 zee · Golf van Mexico → Straat van Florida → Atlantische Oceaan → Het Kanaal/Noordzee ·
       ~8.500–9.000 km ontwerp, aannemelijk: geen cargoniveau-bron)──►
   Gate terminal `gas-gate-kade` (Maasvlakte, Rotterdam) ═══ knoop: regasificatie ═══
   ── stoppunt (voedt GTS Nederlands gasnet, korte terreinleiding niet getekend) ──
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | Sabine Pass LNG Terminal → Gate terminal Rotterdam | Golf van Mexico → Straat van Florida → Atlantische Oceaan → Het Kanaal/Noordzee | ~8.500–9.000 [ontwerpschatting; geen gepubliceerde routelengte — zie §7] | MARNET (kade → kade) | nee — beide kades binnen 2 km van een MARNET-zeeknoop, geen haven-aanloop nodig (zie §3) |

**Fase A vervalt** (conform de haalbaarheidstoets): het diffuse Appalachia/Permian/Haynesville-schaliegasnet heeft geen enkelvoudig anker en een stippel zou een niet-bestaande specifieke route suggereren; de keten begint feitelijk bij de terminal. **Fase C** (Gate-regas → GTS-invoedingspunt, <5 km terreinleiding) is **niet getekend**: geen OSM-pijpleiding-way gevonden voor dit terreinstuk en geen tweede coördinaat gebrond (zie §7) — het stoppunt van de brief is daarmee het Gate-terminalpunt zelf.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-sabinepass-laad` | laadplek / LNG-exportterminal (liquefactie) | Sabine Pass LNG Terminal (Sabine Pass Liquefaction LLC / Cheniere Energy Partners), Cameron Parish, Louisiana | 29.75410, -93.87410 | [1][2][5] | bron-gelegd (z15 gezien: uitgestrekt tankenpark met tientallen procesinstallaties op een schiereiland aan het Sabine-Neches-kanaal, met een havenbekken en een aangemeerde tanker aan een steiger — komt overeen met "1.000+ acres, drie berths, vijf opslagtanks van 17 Bcfe" uit [1]) |
| `gas-gate-kade` | losplek / LNG-importterminal (regasificatie) | Gate terminal (Vopak/Gasunie/Royal Vopak), Maasvlakte, Rotterdam | 51.97110, 4.06890 | [3][4][6] | aannemelijk (Wikipedia-geocoördinaat van de terminal-entiteit; satellietblik op de brede havenscène tussen Yangtzehaven en Nijlhaven bevestigt een groot LNG/olie-tankterminalcomplex met meerdere steigers de vaargeul in, maar op deze schaal (z14–z16) is de exacte Gate-steiger niet scherp te onderscheiden van de direct aangrenzende Maasvlakte Olie Terminal — de bak-agent moet dit vóór het bakken verscherpen, conform de haalbaarheidstoets-aanpassing) |

Bestaand anker **Rotterdam RHB** (51.8935, 4.4585, Waalhaven) is terecht **niet hergebruikt**: dat is een andere kade (koper-entrepot in de Waalhaven), niet de Gate-kade op de Maasvlakte.

## 4 · Via-punten
Geen — b1 is het enige been en wordt kade → kade door de MARNET-router gelegd (open oceaan, geen zeestraat-flessenhals te benoemen op dit schaalniveau, zoals het ketenontwerp al aangaf).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Gate terminal | Vopak / Gasunie | LNG (carrier) → hervergast aardgas naar het GTS-landelijke net | 12 bcm/j basis (3 tanks × ~180.000 m³) → 16–20 bcm/j na de 4e tank (verwacht 2026), 3 laad-/losseigers, 35 ha terrein | [3][4] |

## 6 · Stoppunt
De brief stopt bij het regasificatiepunt van de Gate terminal: dat is de LNG-importterminal die het Nederlandse GTS-gasnet voedt. Geen bron karteert de korte terreinleiding (<5 km) naar het exacte GTS-invoedingspunt als doorlopende OSM-way, en er is geen gedocumenteerd downstream-eindpunt (fabriek/centrale) dat deze specifieke keten met naam verbindt — fase C/D/E vervallen, in lijn met het ketenontwerp.

## 7 · Open punten
- **Fase A** (diffuus schaliegasnet) is bewust niet getekend — geen enkelvoudig anker, zie §2.
- **Geen gepubliceerde routelengte** voor b1; ~8.500–9.000 km is een ontwerpschatting. Ter vergelijking: de naburige, al gebakken corridor `olie-corpuschristi-rotterdam` (vergelijkbare Golfkust-VS → Rotterdam-corridor) meet **9.589,8 km** gemeten — bruikbaar als plausibiliteitscontrole bij het bakken, geen directe bron voor déze keten.
- **Het Gate-kade-anker is nog geen satellietgelegd site-anker** (status aannemelijk, Wikipedia-coördinaat) — bij het bakken eerst een z16/z17-pass om de Gate-steiger scherp te scheiden van de aangrenzende Maasvlakte Olie Terminal, dan de zeeknoop-afstand herberekenen. Met de huidige coördinaat (51.97110, 4.06890) snapt de kade op **1,84 km** van MARNET-zeeknoop 6812 (51.98760, 4.06970) — ruim binnen de 25 km- én de >5 km-haven-aanloopgrens, dus voorlopig **geen haven-aanloop** nodig; dit kan verschuiven zodra het echte anker gelegd is.
- **Fase C** (Gate → GTS-invoedingspunt) is niet getekend: geen OSM-pijpleiding-way gevonden voor dit terreinstuk en geen tweede coördinaat gebrond — een verzonnen eindpunt zou tegen de "geen coördinaat verzinnen"-regel ingaan.
- **Het specifieke Sabine Pass→Rotterdam-cargovolume is niet gebrond** (cargo-diversie TTF/JKM) — corridor-illustratie, geen gemeten stroom, conform het ketenontwerp en de haalbaarheidstoets.

## 8 · Bronnen
[1] Cheniere Energy — "Sabine Pass" (where we work): locatie Cameron Parish LA, ~4 zeemijl van de Golfkust, ~30 mtpa / 4,7+ bcf/d, zes operationele treinen, 1.000+ acres, kanaaldiepte 40 ft, drie berths, vijf opslagtanks (17 Bcfe), eerste LNG 2016, 3.460+ ladingen sinds start. https://www.cheniere.com/about/where-we-work/sabine-pass
[2] Global Energy Monitor (gem.wiki) — "Sabine Pass LNG Terminal": coördinaten 29,7540967/-93,8740512, capaciteit ~29,5 mtpa (T1–T6 operationeel), Stage 5-uitbreiding voorgesteld (+20 mtpa), eigenaar Sabine Pass Liquefaction LLC (Cheniere Energy Partners LP, 100%). https://www.gem.wiki/Sabine_Pass_LNG_Terminal
[3] Gate terminal (Vopak/Gasunie) — "Profiel: Facts & Figures": doorzetcapaciteit 12 bcm/jaar, opslag 3 tanks (netto/bruto ~180.000/200.000 m³), 35 ha terrein, drie kaaimuren, "Tank 4 Project" in ontwikkeling. https://www.gateterminal.com/en/gate-terminal/profiel/facts-figures/
[4] Wikipedia (NL) — "Gate terminal": eerste Nederlandse LNG-importterminal (2011), coördinaten 51,97111/4,06889, drie tanks à ~180.000 m³, twee aanlegsteigers in de Nijlhaven (Nieuwe Waterweg-zijde), tanks aan de Yangtzehaven-zijde, vierde tank verwacht 2026 (totaal 20 mrd m³/jaar). https://nl.wikipedia.org/wiki/Gate_terminal
[5] Wikipedia (EN) — "Sabine Pass": coördinaten 29,72639/-93,86333, natuurlijke doorgang Sabine Lake → Golf van Mexico, grens Jefferson County TX / Cameron Parish LA — geografische context voor het terminalanker. https://en.wikipedia.org/wiki/Sabine_Pass
[6] OpenStreetMap (via Photon-geocoder) — landuse "Gate terminal" (Maasvlakteweg 991, Rotterdam) + waterway "Nijlhaven"/"Yangtzehaven", Maasvlakte Rotterdam. https://www.openstreetmap.org
[7] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16) — `v2/build-cache/satcheck/sat-gas-sabinepass-rotterdam-sabinepass.png`, `…-gate-wide.png`, `…-gate-nijlhaven.png`.
[8] Lokale zeeknoop-afstandsberekening via `v2/tools/hecht_marnet.py` (MARNET-net `v2/build-cache/marnet-preais`, geen internet nodig) — zie §7.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `gas-sabinepass-rotterdam`** → `v2/data/stroomroute-gas-sabinepass-rotterdam.json` — 1 been, **9.220,6 km**, 1.067 punten, 2 markers (0 stippel).
Recept: `bak_stromen.sh` (functie `bak_gas_sabinepass_rotterdam`).

**b1 (zee, MARNET-route, kade → kade):** `--been "zee|LNG-carrier Sabine Pass → Rotterdam Gate (Golf van Mexico → Straat van Florida → Atlantische Oceaan → Het Kanaal/Noordzee)|29.75410,-93.87410|51.97110,4.06890"` — snap Sabine Pass **0,995 km**, snap Gate-kade **1,836 km** (beide ruim binnen de 25 km-norm én de >5 km-haven-aanloopgrens uit LAR-586 — bevestigt de vooraf berekende 1,40/1,84 km uit §7/bak_aanwijzingen; **geen haven-aanloop gebouwd**, conform de bak-aanwijzing). **9.220,6 km**, 1.067 punten, tegen de ontwerpschatting ~8.500–9.000 km = **+2,5% tot +8,5%**, binnen ±15%; tegen de vergelijkbare, al gebakken corridor `olie-corpuschristi-rotterdam` (9.589,8 km) is dit **−3,8% korter** — geografisch consistent (Sabine Pass ligt noordoostelijker langs de Golfkust dan Corpus Christi, dus dichter bij de uitgang naar de Straat van Florida). km-uitsplitsing volgens het bake-log: track-graaf 29,0 km (Golfkust-uitloop bij Sabine Pass) + MARNET-zee 9.191,3 km + 1 connector 0,044 km; lengte-invariant (getekende lijn vs som edge-km) **+0,266 km** = de naden, verwaarloosbaar.

**Markers:** `gas-sabinepass-laad` (**0,995 km** van de lijn — anker ≠ routeerpunt: de kade snapt op de dichtstbijzijnde MARNET-zeeknoop in het Sabine-Neches-kanaal, ruim binnen de norm; status bron-gelegd) · `gas-gate-kade` (**1,836 km** van de lijn — zelfde categorie; status **blijft aannemelijk**, zie hieronder).

**Naad:** geen — één been, dus geen naad tussen benen.

**Toelichting Gate-anker (open punt uit §7, ná satellietpass):** vóór het bakken is een gerichte z15-pass gedraaid op het Gate-terminalcomplex (`v2/tools/sat_check.py`, beelden `v2/build-cache/satcheck/sat-gas-sabinepass-rotterdam-gate-{a,b,nijlhaven,wide}.png`). Op de coördinaat en in de directe omgeving ligt een reëel tank-/steigercomplex met twee aanlegsteigers de Nijlhaven-monding in en twee aangemeerde tankers — consistent met de Wikipedia-beschrijving van Gate ("tanks aan de Yangtzehaven-zijde, twee aanlegsteigers in de Nijlhaven"). Op deze schaal (z14–z16) is de Gate-steiger echter nog steeds **niet scherp te scheiden** van de direct aangrenzende Maasvlakte Olie Terminal — geen enkele objectieve grens (naam-tag, hek, aparte pier-geometrie) is zichtbaar te trekken tussen de twee complexen op het beeld. Het anker is daarom **niet geüpgraded naar bron-gelegd** en blijft **aannemelijk**; de coördinaat is ongewijzigd gebleven, dus de zeeknoop-afstand (1,836 km, gemeten bij het bakken) valt exact binnen de vooraf berekende 1,84 km — een haven-aanloop was en is niet nodig.

**Toets:** `toets_knikken.py` — 7 knikken ≥60° (twee spikes van 19-22 m straal bij de Sabine Pass-havenuitloop, twee spikes van 26-28 m straal bij het Nauw van Calais, drie krappe bochten van 2,2-6,8 km straal op de Golfkust-uitloop, bij Florida en bij de Rotterdamse aanpak), **2 omkeringen ≥150° waarvan 0 terugloop** (beide bij 29,731/-93,868, R≈20 m, in de nauwe havenuitloop van Sabine Pass — échte kopmaak-bochten in een scheepvaartkanaal, geen bevinding). `toets_rechte_benen.py --min-km 5` — de stroom komt niet op de lijst voor (geen enkel been heeft een omwegfactor ≈1,000; dit is een volledig gemeten, gebogen MARNET-route). json geldig: versie 2, punt_formaat lonlat, modaliteit `zee` (in de toegestane set), been ≥2 punten (1.067), bestandsgrootte **20,3 KB** (ruim < 300 KB).

**Gereedschapslessen:**
- Voor een enkelvoudig zeebeen waarbij beide kades ruim binnen de 25 km-max-snap van een zeeknoop liggen, is de bak zelf triviaal (één `--been`-regel, geen via-punten, geen aanloop) — de vooraf lokaal berekende zeeknoop-afstanden uit de brief (1,40/1,84 km) kwamen bij het bakken vrijwel exact terug (0,995/1,836 km), wat bevestigt dat die vooraf-berekening (§7) betrouwbaar was en geen haven-aanloop-ronde nodig maakte.
- Een gerichte z15-satellietpass kan een terminal-anker *bevestigen als reëel complex* zonder het naar bron-gelegd te kunnen upgraden — wanneer twee aangrenzende havencomplexen (Gate/LNG en Maasvlakte Olie Terminal) op de tegel-resolutie geen zichtbare grens dragen, blijft "aannemelijk" de eerlijke status; dat is geen tekortkoming van de pass maar de uitkomst ervan (vergelijk de Tongling-klasse: een zoomplafond levert soms een uitsluiting, hier levert het een bevestiging-zonder-upgrade).
- De plausibiliteitscheck tegen een naburige, al gebakken corridor van vergelijkbare vorm (Golfkust-VS → Rotterdam) werkt ook als *richtingscontrole*: Sabine Pass (noordoostelijker) kwam terecht korter uit dan Corpus Christi (zuidelijker), niet alleen "binnen dezelfde orde van grootte".
