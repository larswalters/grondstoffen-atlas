# Routebrief (licht) · koper — Olympic Dam → Port Adelaide

**stroom-id:** `koper-olympicdam-portadelaide` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** koperkathode (+ uranium/goud/zilver) uit BHP's volledig geïntegreerde Olympic Dam-mijn/mill/smelter/raffinaderij (Roxby Downs, Zuid-Australië) per **truck** naar de nieuwe Aurizon-intermodale terminal in Pimba, en sinds oktober 2025 per **spoor** via Port Augusta naar Port Adelaide (Berth 29, binnenhaven) — Australië als vierde herkomstcontinent op de bol, met export zonder gedocumenteerde overzeese smelter.
**Welke as van het verhaal:** *Australische volledig-geïntegreerde bron* — de enige stroom waar kathode al bij de mijn zelf wordt geraffineerd (99,99 % Cu), tegenover de concentraat-trechters van Chili/Peru/Congo. Jaarvolume ≈ 220 kt Cu/jaar (Wikipedia/BHP, "in excess of 220,000 tonnes", jaar niet gespecificeerd — komt overeen met de omvang van de kt Cu/jaar-sitelaag).

## 1 · Ketenkaart
```
Olympic Dam-mijn/smelter/raffinaderij `cu-olympicdam-mijn` ──(b1 truck · Olympic Dam Highway · 92 km)──►
Pimba-terminal `cu-pimba-terminal` (Aurizon intermodale terminal, sinds okt. 2025)
   ──(b2 spoor · Trans-Australian Railway → Adelaide–Port Augusta-lijn → Dry Creek–Port Adelaide-lijn · ~500 km)──►
Port Adelaide-kade `cu-portadelaide-kade` (Inner Harbour, bulkmineralenprecinct Berth 29) ── stoppunt
```
Vóór okt. 2025 reed dit hele traject per truck (11.000+ ritten/jaar); sinds de BHP–Aurizon-deal (aangekondigd juni 2025,
gestart oktober 2025, ~A$972m/A$1,5 mrd) is alleen Olympic Dam→Pimba nog truck en gaat Pimba→Port Adelaide per trein.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A1 | truck | Olympic Dam-mijn → Pimba-terminal | Olympic Dam Highway (Stuart Hwy–Olympic Dam) | 92 [1] | maak_stroombeen_weg (extract australie) | nee |
| b2 | A2 | spoor | Pimba-terminal → Port Adelaide-kade | Trans-Australian Railway → Adelaide–Port Augusta-lijn → Dry Creek–Port Adelaide-lijn | ≈500 [2][3] | toets_spoorroute (BAKE_SUFFIX=-raw, extract australie), 4 sub-runs via de via-punten van §4 | nee |

Geen zee-been: geen bron noemt een overzeese smelter/afnemer voor dit kathodevolume — de keten stopt bij de kade (§6).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-olympicdam-mijn` | mijn + geïntegreerde smelter/raffinaderij (kop b1) | Olympic Dam mining/metallurgical complex, Roxby Downs (BHP) | -30.4400, 136.8731 | [4][8] | bron-gelegd (z15 gezien: open pit NW, tailings-bekkens, indikkers, smelter-/raffinaderijgebouwen en pijpenwerk — het hele geïntegreerde complex op één terrein) |
| `cu-pimba-terminal` | overslag truck → spoor (staart b1 / kop b2) | Aurizon intermodale vrachtterminal, Pimba | -31.2551, 136.7997 | [2][5] | onzeker (z15: kleine nederzetting op de Stuart Hwy/spoor-kruising met bebouwing ZO van de weg; de nieuwe terminal (grootste post, ~A$40m) niet scherp te onderscheiden van bestaande bebouwing — opname mogelijk ouder dan de bouw) |
| `cu-portadelaide-kade` | losplek spoor (staart b2), stoppunt | Port Adelaide, Inner Harbour — bulkmineralenprecinct (generiek havenanker, Berth 29-omgeving) | -34.8330, 138.5075 | [6][7] | onzeker (z15 gezien: kade-/loodsstrook aan de rivier tussen tankopslag en het havenbekken bij Ocean Steamers Rd; geen OSM- of Nominatim-object voor "Berth 29" gevonden — conform de bindende aanpassing blijft dit voorlopig het generieke Inner Harbour-anker) |

## 4 · Via-punten (alleen b2 — de spoorlijn heeft een echte corridorkeuze bij elke aansluiting)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Port Augusta | -32.4925, 137.7658 | hier verlaat de lijn de oost-westas van de Trans-Australian Railway en buigt zuidwaarts naar Adelaide |
| b2 | 2 | Crystal Brook | -33.3500, 138.2000 | aansluiting op de Adelaide–Port Augusta-lijn / Crystal Brook–Broken Hill-lijn; hier is de lijn naar Adelaide gestandaardiseerd i.p.v. naar Broken Hill door te gaan |
| b2 | 3 | Gawler | -34.5973, 138.7449 | nadering Adelaide-metro, laatste knoop vóór de stedelijke vertakkingen |
| b2 | 4 | Dry Creek | -34.8333, 138.5833 | hier splitst de Dry Creek–Port Adelaide-lijn (8 km havenspoor) af van de doorgaande Adelaide-lijn naar de haven |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Olympic Dam-smelter/raffinaderij | BHP | polymetaalerts (ondergronds) → kopperkathode 99,99 % + U₃O₈ + Au/Ag | >220 kt Cu/jaar (jaar niet gespecificeerd) | [4][8] |
| Pimba-terminal | Aurizon (voor BHP Copper SA) | truck-lading → treinlading | ≈1,3 Mt/jaar voor de hele Copper SA-groep (Olympic Dam + Prominent Hill + Carrapateena), ~A$40m grootste post van de deal | [2][5] |

## 6 · Stoppunt
De brief stopt bij de kade van Port Adelaide: het kathodevolume wordt "geëxporteerd via Port Adelaide" (Wikipedia/BHP), maar
geen bron noemt een specifieke overzeese smelter, raffinaderij of afnemer — fase D/E vervallen.

## 7 · Open punten
- **Exacte Berth 29-coördinaat niet gevonden.** OSM/Nominatim/Photon kennen geen object "Berth 29"; Flinders Ports noemt hem
  als onderdeel van de Inner Harbour-berthlijst (18/19/20/25/27/29/…) met "een swing basin net zuid van Berth 27" als enige
  relatieve aanwijzing. Het huidige anker is het generieke Inner Harbour-bulkprecinct — de bak-agent zoekt het exacte
  kade-front via `sat_check.py` (zie bak_aanwijzingen).
- **Pimba-terminal niet scherp op satelliet.** De Esri-opname kan van vóór de bouw (2025) zijn; geen conveyor/opslagpatroon
  te onderscheiden van de bestaande roadhouse-bebouwing. Aannemelijk dat de terminal ten zuidoosten van de kruising ligt.
- **Modaliteit vóór okt. 2025 was puur truck** (ontwerp), **sinds okt. 2025 gemengd truck+spoor** (bindende haalbaarheidstoets)
  — deze brief tekent de actuele (2026) situatie; het ontwerpveld `spoornet_nodig: false` is daarmee achterhaald.
- **Geen per-segment gepubliceerde spoorkm** — alleen het totaal Pimba→Port Adelaide "roughly 500 km" (Aurizon). De
  verdeling over Port Augusta–Crystal Brook–Gawler–Dry Creek is niet apart gebrond; de bake-uitvoer toetst het totaal.
- **Geen overzeese afnemer gedocumenteerd** — de keten stopt bewust bij de kade (§6).
- Olympic Dam-mijncoördinaat (-30.4400, 136.8731) is de Wikipedia-infobox-coördinaat voor het hele mijncomplex, niet een
  puntobject; de satellietblik bevestigt dat dit midden in het geïntegreerde mijn/mill/smelter/raffinaderij-terrein valt.

## 8 · Bronnen
[1] Wikipedia, "Olympic Dam Highway" — sealed 92 km, Stuart Highway (Pimba) → Olympic Dam. https://en.wikipedia.org/wiki/Olympic_Dam_Highway
[2] Aurizon, 16-06-2025, "Aurizon drives down emissions with rail-based logistics solution for BHP Copper South Australia" — nieuwe intermodale terminal Pimba (~A$40m van ~A$100m totaal), rail Pimba↔Port Adelaide (Berth 29), 500 km, 1,3 Mt/jaar over 15 jaar, start okt. 2025, 11.000+ minder truckritten/jaar. https://www.aurizon.com.au/news/2025/aurizon-drives-down-emissions-with-rail-based-logistics-solution-for-bhp-copper-south-australia
[3] Wikipedia, "Trans-Australian Railway" — Port Augusta–Tarcoola–Kalgoorlie hoofdlijn, Pimba ligt aan de kant van deze lijn (Ghan/Indian Pacific passeren Pimba Siding); "Adelaide–Port Augusta railway line" (standaardspoor via Crystal Brook) en "Dry Creek–Port Adelaide railway line" (8 km havenspoor) als aansluitende lijnen naar de haven. https://en.wikipedia.org/wiki/Trans-Australian_Railway · https://en.wikipedia.org/wiki/Adelaide%E2%80%93Port_Augusta_railway_line · https://en.wikipedia.org/wiki/Dry_Creek%E2%80%93Port_Adelaide_railway_line
[4] Wikipedia, "Olympic Dam mine" — BHP-eigendom sinds 2005, 550 km NNW van Adelaide, "2005 metal production is thought to be in excess of 220,000 tonnes of copper... exported through Port Adelaide"; coördinaat -30.44/136.87306. https://en.wikipedia.org/wiki/Olympic_Dam_mine
[5] mining-technology.com, 16-06-2025, "BHP's Copper SA unveils $972m logistics solution with Aurizon" — bevestigt de Pimba-terminal en Berth 29. https://www.mining-technology.com/news/bhp-copper-sa-logistics-aurizon/
[6] Flinders Port Holdings, "Port Adelaide" — berthlijst Inner Harbour (18/19/20/25/27/29/H/K/M/N/Osborne) vs Outer Harbor (OH1-8); swing basin net zuid van Berth 27. https://www.flindersportholdings.com.au/port-adelaide/
[7] Australian Mining / Flinders Ports (2009-vestiging) — Berth 29 als bulkmineralenprecinct (mineraalzanden, zink-, koperconcentraat, zwavel, fosfaat), common-user spoorpad. https://www.australianmining.com.au/leading-the-way-for-safe-and-efficient-ports/
[8] Wikipedia, "Pimba, South Australia" — coördinaat -31.255091/136.799674, kruising Stuart Highway/Woomera-weg, ligt aan de transcontinentale spoorlijn, 175 km N van Port Augusta. https://en.wikipedia.org/wiki/Pimba,_South_Australia
[9] Esri World Imagery via `v2/tools/sat_check.py` (z14-z15, live) — `v2/build-cache/satcheck/sat-koper-olympicdam-portadelaide-mine.png`, `-pimba.png`, `-portaugusta.png`, `-berth29-cand1.png`, `-berth29-cand2.png`, `-berth29-cand3.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `koper-olympicdam-portadelaide`** → `v2/data/stroomroute-koper-olympicdam-portadelaide.json` — 4 benen,
**587,7 km**, 1.159 punten, 3 markers. truck 98,9 km · spoor 180,6 + 114,1 + 194,1 = 488,8 km. Recept:
`bak_stromen.sh` (functie `bak_koper_olympicdam_portadelaide`).

**b1 (truck, weg, `maak_stroombeen_weg.py --profiel koper-olympicdam-portadelaide-olympicdam-pimba`):** eerste
poging gaf "geen wegpad tussen punt 0 en 1" — het BHP-terrein is een gated site, opgelost met
`eindToegangPrivaat: True`. Resultaat **98,9 km / 484 punten** tegen gepubliceerd 92 km (Wikipedia, "Olympic Dam
Highway") = **+7,3%**, binnen ±15%. Anker-verbindingen 0,08 km (plant) / 0,14 km (kade) — beide OK.

**b2 (spoor, drie losse runs op het 1-op-1-net, console bevestigt "3260717 spoor-edges", `BAKE_SUFFIX=-raw`) — VIER
runs volgens de bak-aanwijzing gepland, DRIE uitgevoerd:**
1. Pimba-terminal → Port Augusta (`--van=-31.2551,136.7997 --naar=-32.4925,137.7658`): **180,3 km** (losse run;
   180,6 km na integratie in `hecht_marnet route`), grootcirkel 165,1 km, verhouding 1,09.
2. Port Augusta → Crystal Brook (`--van=-32.4925,137.7658 --naar=-33.3500,138.2000`): **113,8 km** (114,1 km na
   integratie), grootcirkel 103,6 km, verhouding 1,10.
3. Crystal Brook → Port Adelaide-kade (`--van=-33.3500,138.2000 --naar=-34.8330,138.5075`): **194,1 km** (194,1 km
   na integratie), grootcirkel 167,3 km, verhouding 1,16, **0 omkeringen**.

⚠️ **Het vierde deel (Gawler- en Dry Creek-via-punten uit brief §4) is BEWUST LATEN VALLEN, na diagnose.** Eerste
poging: Crystal Brook → Gawler apart gerouteerd gaf **220,8 km** met een omkering van **173,9° (boogstraal ~117 m)**
op -34,8606/138,5785 — een punt vér zuidelijk van Gawler zelf, bij de Islington-rangeerknoop in Adelaide. Gawler →
Port Adelaide-kade gaf daarna **42,5 km** met dezelfde omkering op hetzelfde punt. Diagnose: de Gawler-stations-
knoop hangt aan het 1-op-1-net via een lus door die rangeerknoop — forceren op het exacte via-punt liet de lijn
eerst voorbij Gawler naar de Adelaide-kant rijden en weer terugkeren (overschiet-en-terug op een via-punt, dezelfde
klasse als een via-punt op een zijtak/afrit, bakhandleiding §2). Crystal Brook → Port Adelaide in één ongebroken
run raakt dezelfde rangeerknoop zonder de dubbele passage: **194,1 km, 0 omkeringen, verhouding 1,16** tegen
**263,3 km (220,8+42,5), 1 omkering, verhouding gemiddeld ~1,4** met de geforceerde Gawler-stop. Het Dry Creek-
via-punt bleek toch al overbodig: de Dry Creek–Port Adelaide-havenlijn (8 km) zit in het 1-op-1-net en de directe
run snapt er vanzelf doorheen (bevestigd doordat de eindsnap 0,29 km van het Port Adelaide-kade-anker ligt).

Som b2 = 180,3 + 113,8 + 194,1 = **488,2 km** (na integratie 488,8 km) tegen **~500 km** (Aurizon-persbericht,
"roughly 500 kilometres between Adelaide and Pimba") = **−2,4%**, ruim binnen ±15%. Geen per-segment gepubliceerde
km (brief §7) — alleen het totaal is te toetsen, zoals de bak-aanwijzing al voorschreef.

**Geen zeebeen, geen haven-aanloop:** geen bron noemt een overzeese smelter/raffinaderij/afnemer voor dit
kathodevolume — de keten stopt bewust bij de kade (brief §6); fase D/E vervallen.

**Toets naden:** b1→b2.1 0,552 km (truck-eindpunt vs spoor-startsnap, ruim onder de 5 km-norm) · b2.1→b2.2 0,000 km
· b2.2→b2.3 0,000 km — geen naad boven de norm, geen haven-aanloop nodig om ze te dichten.

**`toets_knikken.py`:** 9 knikken ≥60° (allemaal op b1, de weg), **0 omkeringen ≥150°, 0 terugloop**. De 9 knikken op
b1 zijn spikes/krappe bochten van 10–237 m boogstraal rond het BHP-mijnterrein en de Pimba-terminal (site-wegen,
geen route-lus) — geen fout. Alle drie spoorbenen: 0 knikken, 0 omkeringen.

**`toets_rechte_benen.py --min-km 5`:** geen been van deze stroom in de uitslag — geen doorgetrokken been heeft een
verdachte omwegfactor.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, spoor} (binnen de toegestane set),
elk been ≥2 punten (minimum 112), bestandsgrootte **24,7 KB** (ruim < 300 KB-richtwaarde).

**Markers:** cu-olympicdam-mijn 0,0 m · cu-pimba-terminal 0,1 m · cu-portadelaide-kade **293,1 m** (binnen ~0,5 km;
het generieke Inner Harbour-anker ligt iets van de gerouteerde havenspoorlijn af — anker ≠ exact routeerpunt, geen
last-mile-stippel nodig, alle drie sat_check-kandidaten liggen <1 km van dit anker).

**Gereedschapslessen:**
- Een gated mijnterrein (BHP Olympic Dam) vraagt `eindToegangPrivaat: True` in het wegprofiel, net als de
  Codelco-terreinen — zonder die vlag geeft de scanner "geen wegpad tussen punt 0 en 1" ook al ligt de weg er wel.
- Een spoor-via-punt dat op een rangeerknoop/lus-aansluiting snapt (i.p.v. op de doorgaande hoofdlijn) kan een
  overschiet-en-terug veroorzaken die alleen zichtbaar wordt door het been ZONDER dat via-punt opnieuw te draaien
  en de twee uitkomsten te vergelijken (ratio en omkeringen) — dezelfde diagnosemethode als bij een wegcorridor,
  nu toegepast op spoor. Het corrigeren was hier weglaten van een via-punt dat in de brief als "corridorkeuze"
  stond aangemerkt maar in de netgeometrie geen echte keuze bleek te zijn.
