# Routebrief (licht) · uranium — Poti (Georgië) → Montreal → Blind River (Canada)

**stroom-id:** `uranium-poti-blindriver` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken (2026-10-09)
**Keten in één zin:** U₃O₈-concentraat (Cameco's 40%-aandeel van JV Inkai) gaat vanuit de Zwarte-Zeehaven Poti per gecharterd **zeeschip** door de Bosporus, de Middellandse Zee en over de Atlantische Oceaan de Saint-Laurent op naar de haven van Montreal, en daarna per **truck** (aannemelijk: modaliteit niet gepubliceerd) over Hwy 417/17 naar de Blind River-raffinaderij (Ontario) — stoppunt; vervolgstroom van `uranium-inkai-poti`.
**Welke as van het verhaal:** *Trans-Kaspische route naar Noord-Amerika.* Sinds 2022 neemt Cameco zijn Inkai-aandeel via de Middle Corridor af in plaats van via Sint-Petersburg [1][2]. Volume: Cameco's 40% van Inkai (4.090 t U/j 100%-basis, 2023, sitelaag `w-inkai`) ≈ **1.640 t U/j**; Cameco-guidance 2026: 4,2 Mlb U₃O₈ ≈ 1.615 t U [8]. Geen route-specifiek tonnage gepubliceerd; het Trans-Kaspische aandeel in Westerse export schommelt (64% in 2023, 26% in 2024, Kazatomprom) [4].

## 1 · Ketenkaart
```
Poti-kade `u-poti-kade` ──(b1a zee/haven-aanloop · 13,6 km, stippel)──► MARNET-zeeknoop 2134 (42.2115,41.5099)
  ──(b1b zee · Zwarte Zee → Bosporus → Gibraltar → Atlantisch → Saint-Laurent · 10.481 km gemeten MARNET)──► Montreal-kade `u-montreal-kade` (aannemelijk: terminal niet gepubliceerd)
  ──(b2 truck · A-40 → Hwy 417 → Hwy 17 via Ottawa–Pembroke–North Bay–Sudbury · hemelsbreed 739 km, geen wegkm)──► Blind River-raffinaderij `u-blindriver-raffinaderij` ── stoppunt
```
Vervolg (niet getekend): Blind River → Port Hope = al op de bol als b3 van `uranium-mcarthurriver-porthope`.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1a | B | zee (haven-aanloop) | Poti-kade → MARNET-zeeknoop 2134 | schematisch, havenmond Rioni | 13,6 [MARNET-snap, sat] | rechte stippel (`maak_havenaanloop.py` hing in de haalbaarheidstoets, 200 s) | ja — het net reikt niet tot de kade |
| b1b | B | zee | Poti-kade → Montreal-kade | Zwarte Zee–Bosporus–Middellandse Zee–Gibraltar–Atlantische Oceaan–Golf/Rivier Saint-Laurent (gecharterd schip, Cameco 2024 §18.2) | grootcirkel 8.349; MARNET-dry-run 10.481 [1][11] | MARNET (`--been zee`) | nee — snap Montreal 3,4 km (< 5 km) → geen aanloop |
| b2 | C | truck | Montreal-kade → Blind River-raffinaderij | A-40 (Métropolitaine/Félix-Leclerc) → Hwy 417 → Ottawa → Hwy 17 (Pembroke, Mattawa, North Bay, Sudbury-ZW-bypass, Espanola) — **aannemelijk: modaliteit niet gepubliceerd** | hemelsbreed 739 km, geen wegkm (OSRM-indicatie ≈ 861 km, geen publicatie) [12] | maak_stroombeen_weg (extract canada) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-poti-kade` | laadplek zee (kop), hergebruikt | Poti Sea Port, Georgië | 42.1550, 41.6560 | [1], letterlijk uit `uranium-inkai-poti` §3 | bron-gelegd (z15 gezien in die brief: kademuur met kranen, tankopslag, havenbekken met golfbrekers aan de rivier-monding); ligt 13,6 km van zeeknoop 2134 → aanloop |
| `u-montreal-kade` | overslag zee → truck | Port of Montreal, containerterminal Viau-zijde (oostelijke havenzone, Hochelaga-Maisonneuve/Mercier) | 45.5900, -73.5065 | [1][10], coördinaat eigen satellietblik | **onzeker: terminal niet gepubliceerd** (Cameco: "port of Montreal"); z15 gezien: containeryard met stapels en portaalkranen aan een kadewand langs de Saint-Laurent, aan de oostkant van de havenstrook |
| `u-blindriver-raffinaderij` | raffinaderij (staart — stoppunt), hergebruikt | Blind River Refinery (Cameco), 328 Eldorado Road | 46.1810, -83.0174 | [6], letterlijk uit `uranium-mcarthurriver-porthope` §3 | bron-gelegd (z15 gezien in die brief: omheind fabrieksterrein met hallen en een bekken aan de North Channel van Lake Huron) |

## 4 · Via-punten (b2: corridorkeuze Ottawa-dal/Hwy 17 tegenover Hwy 401/Hwy 7 en de Sudbury-bypass; alle punten op de doorgaande weg, geen stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | A-40 → Hwy 417 bij de Québec–Ontario-grens | 45.5391, -74.3894 | pint de Ottawa-dalcorridor (A-40 → 417) tegenover A-20/Hwy 401 naar Toronto |
| b2 | 2 | Hwy 417, ten westen van Ottawa (Kanata/Stittsville) | 45.3091, -75.9061 | route gaat langs de westrand van Ottawa, niet door het centrum |
| b2 | 3 | Hwy 17 bij Pembroke (doorgaande weg) | 45.8001, -77.1272 | Hwy 17 langs de Ottawa-rivier tegenover Hwy 60/7 naar Algonquin |
| b2 | 4 | Hwy 17 bij Mattawa | 46.3115, -78.7047 | laatste doorgaande stuk vóór North Bay, pint de noordelijke Hwy 17-route |
| b2 | 5 | North Bay (Hwy 17/11-knoop, buiten centrum) | 46.3299, -79.4702 | splitsing Hwy 11 (Toronto) tegenover Hwy 17 westwaarts naar Sudbury |
| b2 | 6 | Sudbury Southwest By-Pass (Hwy 17) | 46.4333, -80.9727 | pint de bypass i.p.v. de Kingsway door de stad (centrum 46.4927/-80.9912 liggen al in `mcarthurriver-porthope` b3; hier bewust niet gebruikt) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Blind River-raffinaderij | Cameco | uraanconcentraat (Inkai-aandeel via Poti–Montreal) → UO₃ | 's werelds grootste commerciële uraanraffinaderij; eigendom Inkai-materiaal gaat pas over bij ontvangst in Blind River [1][6] | [1][6] |

## 6 · Stoppunt
De brief stopt bij Blind River: dat is de gedocumenteerde bestemming van Cameco's Inkai-aandeel (§18.2); verder (UO₃ → Port Hope) staat al op de bol in `uranium-mcarthurriver-porthope` b3 en wordt niet gedupliceerd; fase D/E vervallen.

## 7 · Open punten
- **Montreal-terminal niet gepubliceerd:** Cameco noemt alleen "the port of Montreal"; het anker is een eigen keuze (containerterminal Viau-zijde, 3,4 km van MARNET-zeeknoop 6358) en kan een andere kade zijn (Maisonneuve, Contrecoeur, Old Port). Status onzeker; geen tweede bron gevonden (zoekbudget).
- **Modaliteit Montreal → Blind River niet gepubliceerd:** truck is aannemelijk (tractor-trailer met uraanconcentraat op Hwy 17 naar Blind River gedocumenteerd [7]; NRC-notices tonen wegtransport via Sault Ste. Marie [9]); trein is niet uitgesloten. Geen wegkm gepubliceerd; OSRM-indicatie 861 km (OSM-gebaseerd, dus dezelfde bron als de scan, geen onafhankelijke toets).
- **Haven-aanloop Poti is een rechte stippel:** `maak_havenaanloop.py` gaf in de haalbaarheidstoets geen resultaat binnen 200 s; geen tweede poging.
- **Hwy 17 Sudbury–Blind River (~140 km) overlapt in tegenrichting `uranium-mcarthurriver-porthope` b3** (geen letterlijke kopie mogelijk: andere richting/profiel); b2 telt ~15% overlap met die stroom.
- **Zending niet continu:** alleen Cameco's 40%-aandeel; Kazatomprom's 60% gaat vooral via Sint-Petersburg of naar Azië; eerste TITR-zending einde sept. 2022 gedispatcht, medio dec. 2022 in een Canadese haven aangekomen [2][3][5]; latere zendingen zonder datum.
- **Bake-risico:** `pyosmium` is op deze machine geblokkeerd (beleid voor toepassingsbeheer) en Overpass gaf op 2026-10-09 een 500 → de wegscan van b2 (extract canada, 6,4 GB) heeft een werkende bron nodig (`--bron overpass` of ontblokkering).

## 8 · Bronnen
[1] Cameco, "2024 Inkai Operation Technical Report" (NI 43-101, eff. 30-09-2024) §18.2 — Zhanatas → Aktau → Alyat → Poti → Bosporus → Atlantic → port of Montreal → Blind River Refinery; vóór 2022 Sint-Petersburg → Montreal. https://www.cameco.com/sites/default/files/documents/Cameco-2024-Inkai-Technical%20Report.pdf
[2] World Nuclear News — "Kazatomprom completes trans-Caspian uranium delivery" (gecharterd schip, Canadese haven). https://www.world-nuclear-news.org/Articles/Kazatomprom-completes-trans-Caspian-uranium-delive
[3] Eurasianet, jan. 2023 — "Kazakhstan moves uranium exports through Middle Corridor" (dispatch sept. 2022, aankomst dec. 2022). https://eurasianet.org/kazakhstan-moves-uranium-exports-through-middle-corridor
[4] Astana Times, 2024 — Kazachstan verhoogt uraniumzendingen via TITR (2.300 t in 2024). https://astanatimes.com/2024/05/kazakhstan-increases-uranium-shipments-via-trans-caspian-international-transport-route
[5] NucNet, 20-12-2022 — "Uranium shipment arrives in Canada via non-Russian route". https://www.nucnet.org/news/uranium-shipment-arrives-in-canada-via-non-russian-route-12-3-2022
[6] Cameco, Refining: Blind River (328 Eldorado Road). https://www.cameco.com/businesses/fuel-services/refining-blind-river
[7] Mining.com — "Cameco's tractor-trailer with uranium concentrate involved in minor accident" (Hwy 17 Wawa–Sault Ste. Marie, lading voor Blind River). https://www.mining.com/?p=910917
[8] Cameco, Form 6-K FY2026 (SEC EDGAR) — Inkai 2026: 10,4 Mlb (100%), Cameco-aandeel 4,2 Mlb. https://www.sec.gov/Archives/edgar/data/0001009001/000119312526205080/d103546dex991.htm
[9] U.S. NRC, export-notificaties Cameco Blind River (oppervlaktetransport via Sault Ste. Marie). https://www.nrc.gov/docs/ML0525/ML052570712.pdf
[10] Wikipedia, "Port of Montreal" — 45.547 / -73.530 (havenstrook; terminals Viau, Maisonneuve, Contrecoeur). https://en.wikipedia.org/wiki/Port_of_Montreal
[11] MARNET dry-run `hecht_marnet.py route` (marnet-preais, 2026-10-09): Poti-kade → Montreal-kade 10.481,4 km, 1.119 punten, snaps 13,579 km (Poti → zeeknoop 2134) en 3,377 km (Montreal → zeeknoop 6358, 45.6176/-73.4884); uitvoer in scratchpad, niet gebakken.
[12] OSRM-demo (OSM) router.project-osrm.org, 2026-10-09 — Montreal-kade → Blind River 861 km via A-40/Hwy 417/Hwy 17 met Sudbury-bypass; gebruikt voor de via-puntcoördinaten (route-vertices), niet als gepubliceerde km.
[13] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-uranium-poti-blindriver-montreal-overzicht.png` (z14), `…-montreal-viau.png` (z15), `…-montreal-maisonneuve.png` (z15).
[14] Eigen routebrieven: `uranium-inkai-poti.md` §3 (Poti-kade), `uranium-mcarthurriver-porthope.md` §3 (Blind River).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
`v2/data/stroomroute-uranium-poti-blindriver.json` · 175,7 KB · 3 benen · **11.354,7 km** · 8.745 punten · 3 markers · registersleutel voorstel `u-pb` (centraal). Recept: `bash v2/tools/bak_stromen.sh uranium-poti-blindriver` (functie `bak_uranium_poti_blindriver`).

| # | modaliteit | km | punten | naad naar vorig been | opmerking |
|---|---|---|---|---|---|
| b1a | zee, haven-aanloop **stippel** | 13,6 | 2 | 0,00 | rechte stippel Poti-kade → zeeknoop 2134; `maak_havenaanloop.py` hing in de haalbaarheidstoets, geen tweede poging |
| b1b | zee (MARNET kade → kade) | 10.481,4 | 1.119 | 0,00 | Zwarte Zee, Bosporus, Gibraltar, Atlantisch, Saint-Laurent; identiek aan de dry-run uit §8[11]; snap Montreal 3,377 km (< 5 km) dus geen aanloop |
| b2 | truck | 859,7 | 7.624 | **3,38** (zee-eindknoop 6358 → kade, < 5 km) | ±15%-toets = indicatie: wegscan 859,3 km tegen OSRM-indicatie 861 (−0,2%) en hemelsbreed 739 (+16%; geen wegkm, dus geen norm) |

**b2-scan:** via-snaps 0,21 / 0,00 / 0,00 / 0,00 / 0,01 / 0,00 / 0,01 / 0,14 km (alle zeven stukken ≤ 170 km, omwegfactor per stuk 1,07–1,25; het Montreal-stuk is het hoogst door de eilandstad); first mile direct op WEG_HOUD, last mile 1,77 km over residential/service bij Blind River; 11 keerlussen gesnoeid (≤ 0,02 km); `toets_knikken`: 0 omkeringen, 16 knikken ≥ 60° (8 zee: Dardanellen, Bosporus, Egeïsche Zee, Straat van Messina, Saint-Laurent bij Sorel en Québec = kustnet-hoeken; 8 truck-spikes in de Montreal-wegenknoop, bij Sudbury en bij het Blind River-terrein, R 4–74 m = OSM-zigzag/afrit); `toets_rechte_benen` meldt alleen de Poti-stippel (haven-aanloop mét reden).
**Markers:** alle drie op 0,0 km van de lijn.
**Stippel/aanloop:** alleen b1a (het net reikt niet tot de Poti-kade, 13,6 km). Geen vlucht, geen leiding, geen spoor, geen letterlijke kopie (Hwy 17 Sudbury–Blind River overlapt tegenrichting met `uranium-mcarthurriver-porthope` b3; ander profiel, geen kopie mogelijk).
**Recept b2:** profiel `uranium-poti-blindriver-montreal-blindriver` in `maak_stroombeen_weg.py` (extract `canada`, refs 40/417/17, venster 50 km); wegbron **Overpass, getegeld** — de standaard-`--bron overpass` vraagt de hele bbox (Montreal–Blind River, ~12° × 2,5°) met alle highway-klassen en gebruikt twee spiegels die op 2026-10-09 een 500 gaven. Eigen driver in de scratchpad (`uranium_poti_blindriver_weg.py`) patcht alleen in zijn eigen proces `_ways_uit_overpass`: 1° × 0,5°-tegels binnen 95 km van de via-lijn voor motorway…secondary(+link), plus 2 × 16 subtegels voor residential/service/tertiary/unclassified binnen 12 km van beide ankers, gecachet per tegel, spiegels `maps.mail.ru` (werkt, soms 504) → kumi → private.coffee. Zelfde `fl.weg_houden`-filter, dezelfde Dijkstra: 138.956 ways gehouden. Het gereedschap zelf is niet gewijzigd.
**Lessen:** (1) bij `--bron overpass` op een route van > ~300 km hoort een tegel-driver, niet de hele-bbox-vraag; (2) in een dicht stadsgebied (Montreal) de kleine klassen per subtegel van 0,07° ophalen, één vraag van 24 km zijde liep op 504; (3) het slot-hulpfragment `neem_slot` met `rm -rf "$d"` / `rm -rf "$SLOT"` wordt door de ingebouwde veiligheidscontrole van Claude Code geweigerd (variabele in een rm -rf): gebruik `rm -f "$SLOT/sinds"; rmdir "$SLOT"`; (4) het Montreal-anker (Viau-zijde) blijft een eigen keuze en dus onzeker.
