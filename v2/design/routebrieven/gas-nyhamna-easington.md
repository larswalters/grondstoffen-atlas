# Routebrief (licht) · gas — Nyhamna (Noorwegen) → Easington (Verenigd Koninkrijk)

**stroom-id:** `gas-nyhamna-easington` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) ·
**status:** gebakken
**Keten in één zin:** Ormen Lange-veldgas (twee multiphase-leidingen van het veld naar Nyhamna, Aukra) wordt
in de Nyhamna-gasplant behandeld en gaat via Langeled — 1.168,6 km onderzeese leiding, Noord- en Zuiddeel
aaneengesloten, met het Sleipner Riser-platform als hub naar het Gassled-net — naar het Gassco-terrein bij
Easington (East Riding of Yorkshire), het grootste Britse invoedingspunt voor Noors pijpgas.
**Welke as van het verhaal:** Langeled, de tweede Noorse as naast Europipe II (`gas-karsto-dornum`) — 25,5 bcm/j
ontwerpcapaciteit ≈ 20% van de Britse piekvraag [1]; een verhaal van het VK als pijpgas-afnemer die LNG
(South Hook, Isle of Grain) aanvult. Geen gemeten 2024-doorzet voor Langeled alleen (zie §7).

## 1 · Ketenkaart
```
Ormen Lange-veld (fase A vervalt: 2 multiphase-leidingen, 120 km offshore, veld = geen eigen anker [4])
   ──► Nyhamna-gasplant `gas-nyhamna-plant` ──(b1 leiding · Langeled-Noord · 626,3 km, OSM 1 way)──►
Sleipner Riser-hub `gas-sleipner-riser` ──(b2 leiding · Langeled-Zuid · 542,3 km, OSM 2 ways)──►
Gassco-terminal Easington `gas-easington-gassco` — stoppunt, invoeding Britse NTS (National Gas)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | `gas-nyhamna-plant` → `gas-sleipner-riser` | Langeled-Noord (42″, Gassco/Gassled) | 628 [2] (Wikipedia: 1.166 totaal [1]) → gemeten OSM 626,3 (−0,3%) | OSM-way 174152595 (man_made=pipeline, name=Langeled, substance=gas); geojson vooraf gestikt | nee |
| b2 | B | leiding | `gas-sleipner-riser` → `gas-easington-gassco` | Langeled-Zuid (44″, grootste onderzeese pijp van de Noordzee [1]) | 543 [2] → gemeten OSM 542,3 (−0,1%) | OSM-ways 637286664 + 903170711 (zelfde tags, operator=Gassco), gestikt | nee |

Totaal OSM 1.168,6 km tegen 1.171 (628+543, Gassco) en 1.166 (Wikipedia): binnen ±0,2% — ruim binnen de ±15%-toets.
(Gassco's eigen totaal "1.116 km" op dezelfde pagina [2] rijmt niet met de som van zijn twee delen; niet gebruikt.)

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-nyhamna-plant` | gasplant (kop) | Nyhamna-gasplant (Gassco/Shell/Equinor), Aukra | 62.8480, 6.9430 | [3][4][6][8] | bron-gelegd (z15 gezien: groot, geplaveid procescomplex met rijen compressoren/vaten, tankenpark en een fakkelcirkel aan de westkant, kaai met jetty aan de fjordkant; OSM-leidingstart 62.8500, 6.9420 ligt 0,23 km noordelijk aan de rand) |
| `gas-sleipner-riser` | hub (tussenpunt, geen overslagvolume) | Sleipner Riser-platform, Noordzee — Langeled-Noord ↔ Langeled-Zuid ↔ Gassled-aansluiting | 58.3669, 1.9066 | [1][6] | aannemelijk (OSM: gedeelde eindnode van way 174152595 en 637286664; offshore, niet satelliet-controleerbaar) |
| `gas-easington-gassco` | receptieterminal (staart, stoppunt) | Gassco-terminal (Langeled receiving), Dimlington Road, Easington | 53.6572, 0.1119 | [5][6][7][11] | bron-gelegd (z16 gezien: omheind, apart terrein met compressortrein, filter-/meetgebouwen en een brandwater-vijver, ten westen van de grote Perenco/Rough-complexen; OSM-polygoon "Gassco AS UK Branch" way 151094337; OSM-leidingeinde op het strand 53.6621, 0.1177 ligt 0,67 km verderop) |

Hergebruik: geen — Nyhamna en Easington staan niet in `gas-sitelaag.json` en niet in eerdere brieven. De Wikipedia-coördinaat van
Nyhamna (62.8513, 6.9511) ligt op de kade, die van Easington (53.6548, 0.1198) op de BP/Perenco West Sole-terminal naast het Gassco-terrein: beide verworpen als anker.

## 4 · Via-punten
Niet van toepassing: beide benen zijn leidingen uit aaneengestikte OSM-ways (geen corridorkeuze, zoals bij weg/spoor).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Nyhamna-gasplant | Gassco (operator), Shell als operator Ormen Lange | multiphase-putstroom Ormen Lange → drooggas (Langeled) + condensaat per schip | ~20 bcm/j gerapporteerd (Wikipedia) [3]; Gassco noemt 79,8 MMm³/d (juni 2024) ≈ 29 bcm/j piek [8] | [3][4][8] |
| Sleipner Riser | Gassco/Gassled | Langeled-Noord ↔ -Zuid, aansluiting op het Gassled-net | hub: gas van andere velden kan meelopen | [1] |
| Easington Gassco-terminal | Gassco (leiding), National Gas (net) | Langeled-gas (155 bar) → Britse NTS | tot ±50 MMm³/d bij herstart juni 2024 [9][10] | [5][9] |

## 6 · Stoppunt
De brief stopt bij de Gassco-receptieterminal Easington: dit is het gevraagde Britse invoedingspunt. Vanaf hier is het
gas anoniem Brits netgas (National Gas NTS) — geen bron volgt één molecuul verder. Fase A (Ormen Lange-veld, 120 km
offshore) vervalt: geen eigen veld-anker en de leidingen zijn niet als OSM-way gekarteerd gevonden.

## 7 · Open punten
- **Geen vers jaarvolume voor Langeled alleen.** 25,5 bcm/j is ontwerp, geen doorzet. 2024-aanwijzing: herstart juni 2024 op
  40–50 MMm³/d (≈ 15–18 bcm/j indicatief, mijn eigen rekensom, geen gerapporteerd jaartotaal) [9][10]; Noorse export totaal
  117,6 bcm in 2024 [7]. Ormen Lange loopt terug (subsea-compressie sinds 2025 [4]).
- **Easington = Noors gas, maar niet alleen Ormen Lange**: via het Sleipner Riser-hub mengt Langeled met gas uit Gassled. De
  keten tekent de fysieke leiding, niet een molecuul-herkomst.
- **Gassco-terrein bron-gelegd op OSM-naam + satelliet**, niet op een operator-document dat expliciet "Langeled receiving
  facilities" op dit perceel zegt; de OSM-landuse "Gassco AS UK Branch" is de sterkste aanwijzing (aannemelijk-plus).
- **Onshore stukken** (Langeled-aanlanding Nyhamna → plant ~0,2 km; strand Easington → terminal ~0,7 km) niet getekend: OSM-ways eindigen
  aan de kust; < 5 km, dus geen stippel nodig.
- **Sitelaag mist Nyhamna, Easington en Sleipner Riser** — centrale aanvulling nodig voor de gloed (gewicht: Nyhamna ~20 bcm/j [3]).
- **Sleipner Riser-coördinaat is een OSM-knoop**, geen platform-referentiebron; niet satelliet-toetsbaar.

## 8 · Bronnen
[1] Wikipedia (EN), "Langeled pipeline" — 1.166 km, 25,5 bcm/j, 42″/44″, opening 2006/2007, hub Sleipner Riser, Gassco-operator.
    https://en.wikipedia.org/wiki/Langeled_pipeline
[2] Gassco, transport map — Langeled Noord 628 km (42″) en Zuid 543 km (44″), totaal "1 116" (afwijkend).
    https://gassco.eu/en/transport-map/
[3] Wikipedia (EN), "Nyhamna" — 62.85126/6.95111, landing Ormen Lange sinds 2002, ~20 bcm/j verwerking.
    https://en.wikipedia.org/wiki/Nyhamna
[4] Sokkeldirektoratet/Norskpetroleum, "Ormen Lange" — 2 multiphase-leidingen, 120 km WNW van Nyhamna, export via Langeled en Sleipner naar Easington; productie vanaf 12.09.2007.
    https://www.norskpetroleum.no/en/facts/field/ormen-lange/
[5] Wikipedia (EN), "Easington Gas Terminal" — vier plants (twee Perenco, Centrica, Gassco), 53°39′17″N 0°07′11″E.
    https://en.wikipedia.org/wiki/Easington_Gas_Terminal
[6] OpenStreetMap-bijdragers (ODbL), via Overpass (overpass.openstreetmap.fr, 2026-10-09) — ways 174152595, 637286664, 903170711 (Langeled, Gassco, substance=gas); way 151094337 "Gassco AS UK Branch"; ways 151094363/151094431 (BP West Sole/Rough).
    https://www.openstreetmap.org/way/174152595
[7] Gassco, "Record delivery of natural gas … to Europe in 2024" — 117,6 bcm 2024.
    https://gassco.eu/en/record-delivery-of-natural-gas-through-the-gas-transport-system-to-europe-in-2024/
[8] Gas Processing News, juni 2024 — Nyhamna 79,8 MMm³/d, uitval na scheur op Sleipner Riser.
    https://www.gasprocessingnews.com/news/2024/06/norway-eyes-faster-ramp-up-of-gas-export-to-britain/
[9] Inspenet, juni 2024 — herstart Noors gas naar het VK; Easington via Langeled.
    https://inspenet.com/en/news/norwegian-gas-supply-resumes-great-britain/
[10] Gassco, annual report 2024 (Easington als ontvangstterminal, Dimlington Road HU12 0TG).
    https://gassco.eu/en/annual-report-2024/
[11] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-gas-nyhamna-easington-nyhamna.png`, `-nyhamna-plant.png`, `-easington.png`, `-easington-gassco.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Recept:** `bash v2/tools/bak_stromen.sh gas-nyhamna-easington` (functie `bak_gas_nyhamna_easington`, direct vóór de ankerregel).
Geen profiel in `maak_stroombeen_weg.py` (geen wegbeen), geen extract, geen haven-aanloop, geen stippel, geen via-punten.
Uitvoer: `v2/data/stroomroute-gas-nyhamna-easington.json` (5,7 KB, versie 2, punt_formaat lonlat, 264 punten, 3 markers).

| # | modaliteit | been | km gemeten | km brief | naad naar vorige | punten |
|---|---|---|---|---|---|---|
| b1 | leiding | Langeled-Noord Nyhamna → Sleipner Riser (42 inch, OSM way 174152595) | 626,3 | 628 (Gassco) | — | 196 |
| b2 | leiding | Langeled-Zuid Sleipner Riser → Easington (44 inch, OSM ways 637286664+903170711) | 542,3 | 543 (Gassco) | 0,00 km | 68 |
| | | **totaal** | **1.168,6** | 1.171 (Gassco) / 1.166 (Wikipedia) | | 264 |

**Markers (afstand anker → dichtstbijzijnde lijnpunt):** `gas-nyhamna-plant` 0,23 km · `gas-sleipner-riser` 0,00 km ·
`gas-easington-gassco` 0,67 km (anker ≠ routeerpunt; beide uiteinden < 5 km, dus geen stippel — bakhandleiding §5).

**Toelichting per been:** beide benen zijn doorgetrokken OSM-leiding (man_made=pipeline, name=Langeled, operator=Gassco,
substance=gas), vooraf met Overpass gestikt tot geojson in `v2/build-cache/ais/graaf/gas-nyhamna-easington-leiding-{noord,zuid}.geojson`
en door `hecht_marnet.py route` als `--been-geojson "leiding|…"` overgenomen (niet geroutet). Geen stippel: er is geen gat; de
offshore stukken zijn gewone OSM-vertexafstand (max. segment 19 km), geen kartering-gat. Geen haven-aanloop, vlucht of gedeeld been.
Het Sleipner Riser-anker (offshore OSM-knoop, gedeelde eindnode van b1 en b2) is "aannemelijk", niet satelliet-toetsbaar;
de status staat in de markernaam en in §3, niet in de lijnstijl.

**Toets (handleiding §5):** km binnen 0,3% van Gassco per been, naad 0,00 km; `toets_knikken.py`: 0 knikken, 0 omkeringen;
`toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom; json.load oké, alle modaliteiten `leiding`, elk been ≥ 2 punten.
Eindpunt klopt met het stroom-id (Easington).

**Lessen:** (1) een leiding die al als OSM-keten bestaat is de goedkoopste keten van de atlas: Overpass-geojson vooraf, daarna
één `hecht_marnet`-aanroep van seconden. (2) Gassco's eigen totaal 1.116 km rijmt niet met zijn delen 628+543; de OSM-meting
(1.168,6) valt binnen 0,2% van de som en van Wikipedia. (3) Het jaarvolume van Langeled alleen is niet gemeten (25,5 bcm/j is
ontwerp); de keten tekent de fysieke leiding, niet een molecuulherkomst (Easington krijgt ook Gassled-gas via Sleipner Riser).
(4) Centraal nog te doen: register + bundel, en de sitelaag mist Nyhamna (~20 bcm/j), Easington en Sleipner Riser.
(5) Tool-opmerking: de slot-opruiming met `rm -rf "$d"` wordt door de Claude-Code-veiligheidscheck geblokkeerd; `rm -f sinds; rmdir` werkt.

