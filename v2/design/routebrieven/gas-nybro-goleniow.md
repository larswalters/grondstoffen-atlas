# Routebrief (licht) · gas — Nybro (Denemarken) → Baltic Pipe → Goleniów (Polen)

**stroom-id:** `gas-nybro-goleniow` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) ·
**status:** gebakken
**Keten in één zin:** Noors Noordzeegas komt bij Nybro (West-Jutland) het Deense net in, gaat door het Deense
transmissienet (Egtved, Kleine Belt, Funen, Grote Belt, Zeeland) naar de landing bij Faxe, onderzees 273 km door
de Oostzee naar Pogorzelica en onshore naar het compressorstation Goleniów (Gaz-System): de Poolse pivot weg van Russisch gas.
**Welke as van het verhaal:** Baltic Pipe — 10 bcm/j capaciteit Noorwegen → DK/PL, 3 bcm/j terug [1]; Equinor–PGNiG-contract
2,4 bcm/j 2023–2033 [3]; werkelijke doorzet niet gevonden (zie §7). Operationeel sinds 2022-09-27 [1].

## 1 · Ketenkaart
```
(Noordzee: Europipe II-aftakking Blaabjerg → Nybro — NIET getekend, zie §7)
Nybro-gasbehandelingsanlæg `gas-nybro-plant` (Energinet)
  ──(b1 leiding · Baltic Pipe DK: Nybro–Egtved bestaand net, Egtved–Kleine Belt–Funen–Grote Belt–Zeeland · 280,0 km OSM)──►
Faxe-landing `gas-faxe-landing`
  ──(b2 leiding · Baltic Pipe offshore, Oostzee · 272,7 km OSM, gepubliceerd 275)──►
Pogorzelica-landing `gas-pogorzelica-landing`
  ──(b3 leiding · Poolse onshore-leiding · 83,0 km OSM)──►
Compressorstation Goleniów `gas-goleniow-tlocznia` — stoppunt, invoeding Pools transmissienet (Gaz-System)
```
Totaal doorgetrokken 635,7 km. Geen stippel: alle drie de leidingen zijn in OSM doorlopend gekarteerd.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-nybro-plant` → `gas-faxe-landing` | Baltic Pipe DK (Energinet, DN1000; 9 OSM-ways, o.a. 1362960758 Nybro–Egtved, 1392067292+1204845861+1095495854 Egtved–Funen, 1392191337 Grote Belt, 1055345076 Zeeland) | 280,0 OSM; gepubliceerd: ca. 200–210 nieuwbouw [1][4], geen totaal inclusief bestaand net | OSM-pipeline, vooraf gestikt (`maak_leidingbeen_gas_nybro_goleniow.py`) | nee |
| b2 | B | leiding | `gas-faxe-landing` → `gas-pogorzelica-landing` | Baltic Pipe offshore (Gaz-System, DN900; OSM way 1068926050, zelfde richting omgedraaid) | 272,7 OSM tegen 275 [1][4]: −0,8% | OSM-pipeline, 1 way | nee |
| b3 | C | leiding | `gas-pogorzelica-landing` → `gas-goleniow-tlocznia` | Poolse onshore (OSM-ways 978208595 Baltic Pipe 4,9 km + 6 onbenoemde + 860469159 Szczecin–Gdańsk 41,6 km) | 83,0 OSM; geen gepubliceerde lengte gevonden; hemelsbreed 65 km, geen wegkm | OSM-pipeline, vooraf gestikt | nee |

Fase A (Noordzee, Noorse velden) vervalt: Baltic Pipe takt bij Europipe II af en het Noordzeedeel is bewust niet getekend (bindende toets); de lijn begint bij Nybro.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-nybro-plant` | ontvangstinstallatie (kop) | Nybro Gasbehandlingsanlæg (Energinet), Varde | 55.6707, 8.3682 | [1][6] | bron-gelegd (z15 gezien: omheind installatieterrein met leidingwerk en een bassin in akkerland; OSM-leidingstart 55.6690, 8.3691 ligt 0,2 km zuid aan de rand) |
| `gas-faxe-landing` | landing (b1 → b2) | Faxe Bugt, Zeeland | 55.1880, 12.1262 | [1][8] | aannemelijk (z15: kustakker op klif, kleine installatie 0,5 km westelijk; leiding ondergronds, niets zichtbaar; punt = OSM-beginknoop way 1068926050; DK-leidingeinde 55.1885, 12.1199 ligt 0,4 km westelijk) |
| `gas-pogorzelica-landing` | landing (b2 → b3) | Pogorzelica, Rewal | 54.1122, 15.1446 | [2][4][8] | aannemelijk (z15: duinen/strand met bos erachter; microtunnel onder duin en strand, niets zichtbaar; punt = OSM-eindknoop way 1068926050 = beginknoop way 978208595) |
| `gas-goleniow-tlocznia` | compressorstation (staart, stoppunt) | Tłocznia gazu Goleniów (Gaz-System), Budno | 53.5443, 14.9249 | [2][7] | bron-gelegd (z15 gezien: afgebakend, kaal gegraven terrein met bouwwerken en wolkenslierten, los in akkers en bos; OSM-polygoon way 318517808; leidingeinde 53.5443, 14.9274 ligt 0,16 km oostelijk) |

Hergebruik: geen — Nybro, Faxe, Pogorzelica en Goleniów staan niet in eerdere brieven; sitelaag `gas-sitelaag.json` bevat alleen Świnoujście (regas) voor Polen.

## 4 · Via-punten
Niet van toepassing: drie leidingbenen uit aaneengestikte OSM-ways, geen corridorkeuze door ons te leggen.
Bij de Kleine Belt liggen parallelle Energinet-ways: gekozen zijn de met Baltic Pipe getagde (1204845861 onderzees, 1392067292, 1095495854).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Nybro-ontvangstinstallatie | Energinet | Noors gas via Blaabjerg → Deens transmissienet oostwaarts | deel van 10 bcm/j [1] | [1][6] |
| Compressorstation Faxe/Zeeland (co-gefinancierd door Gaz-System) | Energinet | Deens net → offshore Baltic Pipe, omkeerbaar | 3 bcm/j teruggaand [1] | [1] |
| Compressorstation Goleniów | Gaz-System | Baltic Pipe → Pools net (Goleniów–Lwówek, Gustorzyn) | 10 bcm/j Noorwegen → Polen [1][4] | [1][4][7] |

## 6 · Stoppunt
De brief stopt bij het compressorstation Goleniów: het invoedingspunt van het Poolse transmissienet. Daarna vloeit het gas anoniem
verder (Goleniów–Lwówek e.a.); geen bron volgt een lading naar één fabriek. Fase D/E vervalt.

## 7 · Open punten
- **Doorzet niet gevonden.** Alleen capaciteit (10 bcm/j) en het Equinor-contract (2,4 bcm/j, 2023–2033). Het 2024-cijfer van Gaz-System/Energinet is niet gevonden (Statista-grafiek geeft het verborgen). Jaarvolume op de bol = capaciteit, geen meting.
- **Noordzee en Noorse oorsprong niet getekend** (Europipe II tot Blaabjerg, daarna 105 km offshore naar Nybro [4]); de lijn begint bij Nybro.
- **b1 bevat bestaand net:** Nybro–Egtved (56 km, way 1362960758, zonder naam-tag) en de Grote Belt-kruising (1392191337, Energinet, niet Baltic-Pipe-getagd) zijn geen nieuwbouw; Wikipedia noemt ca. 200 km nieuwbouw, OSM-pad is 280 km.
- **b3: lijnkeuze onzeker.** 41,6 km (way 860469159) is getagd Szczecin–Gdańsk (DN500) en 6 ways zijn zonder tags; het Baltic-Pipe-DN900-traject kan een naastgelegen leiding in dezelfde corridor zijn. Geen aparte bron voor het exacte trace.
- Pogorzelica- en Faxe-landing zijn OSM-knopen op de waterlijn en niet op satelliet te bevestigen (ondergrondse landing).

## 8 · Bronnen
[1] Wikipedia (EN), "Baltic Pipe" — segmenten, 10 bcm/j en 3 bcm/j terug, operationeel 2022-09-27, offshore 275 km (Faxe Zuid – Niechorze-Pogorzelica), ca. 200 km nieuwbouw in DK, Goleniów-uitbreiding. https://en.wikipedia.org/wiki/Baltic_Pipe
[2] Wikipedia (PL), "Baltic Pipe" — landingen Faxe en Niechorze-Pogorzelica, microtunnel onder duinen Pogorzelica (2021), Goleniów–Lwówek, uitbreiding tłocznia Goleniów. https://pl.wikipedia.org/wiki/Baltic_Pipe
[3] Equinor, "Equinor and PGNiG agree long term gas sales contract" (2022-09-23) — ca. 2,4 bcm/j, 2023-01-01 t/m 2033-01-01. https://www.equinor.com/news/20220923-pgnig-long-term-gas-sales-contract
[4] Poland at Sea, "Baltic Pipe system: from the North Sea to the Yamal pipeline" — 105 km Noordzee-spoor, 275 km Faxe Bay → Pogorzelica, 10 bcm. https://polandatsea.com/baltic-pipe-system-from-the-north-sea-to-the-yamal-pipeline
[5] Poland at Sea, "Gaz-System: Baltic Pipe gas flows remain above 60 million kWh per day" (2022-11-04) — startdoorzet, capaciteit 10 bcm/j eind 2022. https://polandatsea.com/?p=12696
[6] OSM/Nominatim (ODbL) — Nybro Gasbehandlingsanlæg, way 119787480 (55.6707, 8.3682). https://nominatim.openstreetmap.org
[7] OSM/Nominatim (ODbL) — Tłocznia gazu Goleniów, Budno, way 318517808 (53.5443, 14.9249). https://nominatim.openstreetmap.org
[8] OSM-pipeline-ways (ODbL), geofabrik-extracts denemarken en polen; ways in §2; API https://api.openstreetmap.org/api/0.6/way/<id>/full
[9] Esri World Imagery via `v2/tools/sat_check.py` (z15, live): `v2/build-cache/satcheck/sat-gas-nybro-goleniow-nybro.png`, `-faxe.png`, `-pogorzelica.png`, `-goleniow.png`.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
`bash v2/tools/bak_stromen.sh gas-nybro-goleniow` (functie `bak_gas_nybro_goleniow`) → `v2/data/stroomroute-gas-nybro-goleniow.json`, 21,5 KB, contract versie 2, lonlat, 3 benen · 1.059 punten · 4 markers · **635,7 km**.
Recept: eerst `python v2/tools/maak_leidingbeen_gas_nybro_goleniow.py` (OSM-API, ways gestikt; drie FeatureCollections `gas-nybro-goleniow-leiding-{dk,offshore,pl}.geojson` in `v2/build-cache/ais/graaf/`), daarna drie `--been-geojson "leiding|…"` in volgorde dk, offshore, pl. Geen zee, geen via-punten, geen haven-aanloop, geen stippel, geen profiel in `maak_stroombeen_weg.py`.

| # | modaliteit | km | punten | naad | toets |
|---|---|---|---|---|---|
| b1 | leiding | 280,0 | 576 | – | brief 280,0 OSM; gepubliceerd ca. 200–210 nieuwbouw, geen totaal (zie hieronder) |
| b2 | leiding | 272,7 | 61 | 0,40 km | gepubliceerd 275: −0,8% |
| b3 | leiding | 83,0 | 422 | 0,00 km | geen gepubliceerde lengte; hemelsbreed 65 km, geen wegkm: indicatie, geen norm |

Naden: grootste 0,40 km (Faxe: DK-leidingeinde 55.1885, 12.1199 tegen OSM-beginknoop offshore 55.1880, 12.1262), procesgat binnen de landing, geen bijschuiven. Binnen b1 stikt de bouwer 9 ways met naden ≤ 0,26 km, binnen b3 ≤ 0,04 km. Markers tot de lijn: Nybro 0,2 km · Faxe 0,0 · Pogorzelica 0,0 · Goleniów 0,16 km (alle ≤ 0,5 km).
Toetsen: `toets_knikken.py` 30 knikken ≥ 60° (b1 16, b3 14), 0 omkeringen, 0 terugloop: kleine radii (2–75 m) zijn OSM-kartering op way-aansluitingen, geen rijdbaarheidsprobleem voor een leiding, niet geknipt. `toets_rechte_benen.py --min-km 5` meldt dit been niet. `json.load` ok; modaliteiten {leiding}.

**Toelichting.** Alles doorgetrokken: OSM heeft alle drie de leidingen doorlopend, dus geen stippel. b1 bevat bestaand Deens net (Nybro–Egtved 56 km, Grote Belt-kruising); de Grote Belt is één recht OSM-segment van 26,6 km (55.3836, 10.7686 → 55.4321, 11.1812), de offshore-way heeft segmenten tot 13,6 km: dat is spaarzame kartering van een subsea-leiding, geen sprong tussen ways. Een lengte van 280 tegen ca. 200 nieuwbouw is dus verwacht en geen afwijking. b3 staat als "aannemelijk: één bron" in de beennaam (41,6 km is getagd Szczecin–Gdańsk, 6 ways onbenoemd; het Baltic-Pipe-trace kan een naastgelegen leiding zijn). Landingen Faxe en Pogorzelica zijn OSM-knopen (ondergronds/microtunnel), niet op satelliet bevestigbaar, status aannemelijk in de markernaam.
**Niet getekend:** Noordzee-deel (Europipe II tot Blaabjerg, 105 km offshore naar Nybro) en de Noorse oorsprong; doorzet (alleen capaciteit 10 bcm/j en contract 2,4 bcm/j).
**Lessen.** (1) Het id belooft Nybro → Goleniów en de lijn eindigt daar: geen afwijking van het ontwerp. (2) `bak_stromen.sh` wordt door parallelle agenten gewijzigd terwijl bash hem leest: de bake schreef het json netjes, daarna volgde "line 11663: syntax error near unexpected token" omdat de regelnummers onder bash verschoven; `bash -n` op het bestand was daarna ok. Het resultaat is dus niet aangetast, maar een bak op een bestand dat net wordt bewerkt mag je voor de zekerheid herhalen. (3) De tussenuitvoer van een eerder afgebroken poging (drie geojsons) was compleet en is hergebruikt; het maak-script is daarna nog eens gedraaid met identiek resultaat.
