# Routebrief (licht) · Grafiet — Matawinie → QC-131 / A-40 → Bécancour (Canada) — project-as, volume nul

**stroom-id:** `grafiet-matawinie-becancour` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** vlokgrafietconcentraat (97,5 % C) van de Matawinie-mijn van Nouveau Monde Graphite (NMG) bij Saint-Michel-des-Saints (Québec) gaat per **truck** over QC-131, A-40/A-55 en de Pont Laviolette naar de geplande NMG-anodefabriek in het industriepark van Bécancour, waar het tot actief anodemateriaal (AAM) voor Panasonic en GM wordt verwerkt. **Project-as: volume nul** — er rolt vandaag geen lading.
**Welke as van het verhaal:** *de Noord-Amerikaanse ex-China anode-keten, natuurlijk* (naast Balama → Vidalia en de synthetische Novonix-as). Mijn nominaal ~106 kt/j concentraat [1]; fabriek fase 1 13 kt/j AAM, daarna 44 kt/j [2][4]; offtake Panasonic 18 kt/j (7 jaar) en GM 18 kt/j (6 jaar) = ~85 % van 42 kt [3]. **Peiljaar 2026: 0 kt/j** — bouwstart mijn fase 2 mei 2026 (alleen via de toetsstap, zelf niet gelezen), productie einde 2028; Bécancour-FID verwacht 2H 2026 [4]. Het been draagt daarom "(aannemelijk: één bron; volume nul tot 2028)" in zijn naam.

## 1 · Ketenkaart
```
Matawinie-mijn + concentrator `gr-matawinie-mijn` ──(b1 truck · 9 km toegangsweg → QC-131 → Joliette-noord → A-40 → A-55 → Pont Laviolette → A-30 ·
   hemelsbreed 127 km, geen wegkm · aannemelijk: één bron)──► NMG-anodefabriek Bécancour `gr-nmg-becancour` (proxy: li-bc-fabriek; kavel niet gelegd) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (concentraat per camion over QC-131 is gedocumenteerd voor de mijn-uitgang [5]; de exacte weg naar Bécancour niet) | `gr-matawinie-mijn` → `gr-nmg-becancour` | toegangsweg (Rue des Aulnaies) → QC-131 → Saint-Zénon → Joliette-noord → QC-158/QC-345 of A-31 → A-40 (Berthierville) → A-40/A-55 (Trois-Rivières-noord) → Pont Laviolette → A-30 → QC-132/QC-261 | **hemelsbreed 127,4 km, geen wegkm, geen bedrijfsopgave**; OSRM-indicatie 179,3 km (kortste, via QC-347/348/Louiseville) en 192,4 km langs de via-punten van §4 [7]; MELCC: Bécancour "à moins de 200 km" van de mijn [5] | maak_stroombeen_weg (nieuw profiel, extract `canada`) | nee — *aannemelijk: één bron; volume nul tot 2028* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-matawinie-mijn` | mijn + concentrator (laadplek) | NMG Matawinie-mijn, 5 km west van Saint-Michel-des-Saints | 46.7335, -73.9672 | [1][5][6] | bron-gelegd (z15 gezien: kaal industrieel plateau met rijen lange hallen/containers en bezinkvijvers, brede toegangsweg zuidwaarts het bos in) |
| `gr-nmg-becancour` | verwerker / losplek (stoppunt) | NMG Bécancour Battery Material Plant, PIPB — **proxy: Nemaska-fabriek** | 46.3583, -72.3938 | letterlijk hergebruik van `li-bc-fabriek` uit `lithium-whabouchi-becancour.md` §3 [8]; NMG-kavel zelf niet gelegd [2][4] | **aannemelijk** (z15 gezien: groot bouw-/fabrieksterrein met geparkeerde voertuigen, witte hal ten NO en een tweede grote hal met parkeerterrein ten ZW — vermoedelijk Ultium CAM, dat NMG buur noemt [3]; of de NMG-kavel hier ligt is niet te zien) |

Hergebruik: Saint-Michel-des-Saints (Nominatim 46.6786, -73.9177) is alleen een oriëntatiepunt, geen anker. Sitelaag `w-nmg-becancour` staat op 46.3400, -72.3500 (v1-coördinaat, onbevestigd), **3,9 km** van dit proxy — centraal gelijk te trekken, door mij niet aangeraakt.

## 4 · Via-punten (b1; alle óp de doorgaande weg, geen stadscentrum; punten uit de OSRM-routegeometrie, dus op de OSM-weg)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | QC-131 bij Route Louis-Cyr, ná de afslag QC-347 | 46.2940, -73.5656 | QC-131 blijft zuidwaarts naar Joliette i.p.v. QC-347/348 naar Louiseville (de kortere OSRM-route, 179 km) |
| b1 | 2 | QC-131 noord van Joliette (Chemin Barrette) | 46.1376, -73.4203 | rondom Joliette via de noordkant, niet door het centrum (46.02, -73.44) |
| b1 | 3 | A-40 bij Berthierville | 46.1478, -73.1109 | pint de insteek op A-40 oostwaarts; de verbinding Joliette → A-40 (QC-158/QC-345 óf A-31 + A-40, ~30 km langer) laat ik bij de router |
| b1 | 4 | A-40/A-55 noord van Trois-Rivières | 46.3406, -72.6176 | A-55 zuidwaarts richting de brug i.p.v. A-40 door Trois-Rivières/QC-138 |
| b1 | 5 | Pont Laviolette (A-55, OSM-way 84720761) | 46.3073, -72.5613 | enige vaste oeversteek van de Saint-Laurent bij Trois-Rivières/Bécancour [8] |
| b1 | 6 | A-30 × QC-132 / Boulevard Bécancour | 46.3466, -72.4312 | A-30 oostwaarts uitrijden naar de PIPB-ingang (QC-261, Chemin Louis-Riel), naadcontrole richting het anker |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Matawinie-mijn + concentrator | NMG | erts → vlokgrafietconcentraat 97,5 % C | ~106 kt/j, levensduur 25 j (MELCC-analyse 2021: 100 kt/j, 26 j) | [1][5] |
| Bécancour Battery Material Plant | NMG | concentraat → actief anodemateriaal (vormen, zuiveren, coaten) | fase 1: 13 kt/j AAM (gekocht brownfield 143.000 m², hal 22.000 m², naast kavel 200.000 m²); fase 2: 44 kt/j; offtake Panasonic 18 + GM 18 kt/j | [2][3][4] |

## 6 · Stoppunt
De brief stopt bij de anodefabriek in Bécancour: afname door Panasonic (Nevada en Kansas, 13 kt/j) en GM is gebrond maar per fabriek niet gedocumenteerd of niet gelegd [3][4]; fase D en E vervallen (één bron noemt wel de afnemers, niet de afname-site met adres en tonnage).

## 7 · Open punten
- **Volume nul:** mijn in aanbouw (productie einde 2028), Bécancour-FID 2H 2026, productiestart ~mid-2027 volgens een oud schema [3][4]; als lading zijn dit **project-assen** (zoals `grafiet-lakecharles-desoto`, `lithium-whabouchi-becancour`).
- **Route naar Bécancour niet beschreven:** MELCC noemt truck over QC-131 richting Montréal, Detroit **of** een Bécancour-fabriek; 50 % naar Montréal en 50 % naar Detroit was de aanname, tot 60 % naar Bécancour de optie [5]. De route Joliette → A-40 → A-55 is de keuze van deze brief (bindend uit de toets), geen bedrijfsopgave; de kortere OSRM-route over QC-347/348 is een alternatief (−13 km). Een spoorroute is niet gebrond.
- **NMG-kavel in Bécancour niet gelegd:** NMG noemt 200.000 m² + gekochte brownfield 143.000 m² "directly adjacent", zonder adres [2][4]. Proxy = Nemaska-fabriek, ~0,6 km van Ultium CAM; **aannemelijk, niet bron-gelegd**.
- **Mijnnaad:** de nieuwe toegangsweg (~9 km, naar QC-131 net ten zuiden van Saint-Michel, bij Jecc Mécanique [5]) staat in OSM niet als doorgaande weg; de route snapt op de dichtstbijzijnde OSM-weg (Rue des Aulnaies, ~1,5 km van het anker, <2 km → geen last-mile-been) en loopt waarschijnlijk via het centrum van Saint-Michel naar QC-131. Naadwerk, geen via-punt bijschuiven.
- **A-31:** niet gepind (zou ~30 km omweg geven t.o.v. de MELCC-grens "<200 km"); mag de router kiezen.
- **Canada-bake:** extract 6,4 GB; Overpass was tijdens het schrijven onbereikbaar (500/504); er is geen weg-scancache voor oost-Québec (bbox-tot -74,8 °W).
- Mijn bouwstart 20-05-2026 komt uit het ontwerp/de toets (Mining Weekly, 403 voor WebFetch), zelf niet gelezen.

## 8 · Bronnen
[1] NMG, Matawinie Mine — ~106.000 tpy concentraat, 97,5 % C, 25 jaar, nagenoeg 8 km toegangsweg naar Hwy 131, US$335 mln senior debt. https://nmg.com/matawinie-mine/
[2] NMG, Bécancour Battery Material Plants — 200.000 m² PIPB, 13 kt/j daarna 44 kt/j, cluster Ultium CAM/Eco-Pro/Nemaska/Vale, "much of the Matawinie Mine's production" als feedstock. https://nmg.com/becancour/
[3] Electric Autonomy, 2024-02-15 — Panasonic en GM elk 18 kt/j AAM (7 resp. 6 jaar), ~85 % van 42 kt, GM-buur in Bécancour, productiestart mid-2027. https://electricautonomy.ca/2024/02/15/nmg-panasonic-energy-gm-anode-deal/
[4] NMG, 2026-02-25 — brownfield 143.000 m² (hal 22.000 m²) naast kavel 200.000 m², Panasonic 13 kt/j voor Nevada en Kansas, FID 2H 2026. https://nmg.com/acquisition-of-brownfield-site-in-becancour/
[5] MELCC, analyse/décret 47-2021 — concentraat per camion over route 131 richting Montréal/Détroit of Bécancour-fabriek, "à moins de 200 km", chemin d'accès 9 km, 15–20 camions/dag. https://www.environnement.gouv.qc.ca/evaluations/decret/2021/47-2021-rae.pdf
[6] Esri World Imagery via `v2/tools/sat_check.py`, 2026-10-09 — `v2/build-cache/satcheck/sat-grafiet-matawinie-becancour-mijn.png` (z15) en `…-pipb.png` (z15).
[7] OSRM (router.project-osrm.org), 2026-10-09 — mijn → proxy 179,3 km (via QC-131/347/348); langs de via-punten van §4 192,4 km; via-punten gesnapt op de routegeometrie.
[8] `v2/design/routebrieven/lithium-whabouchi-becancour.md` §3 (`li-bc-fabriek`) en Nominatim/OSM 2026-10-09: Pont Laviolette way 84720761 (46.3073, -72.5613); Saint-Michel-des-Saints 46.6786, -73.9177.
[9] `v2/design/grafiet-sitelaag.json` (`w-nmg-becancour`) en `data/graphite.js` (`gr-ref-quebec`) — v1-coördinaat 46.34/-72.35, onbevestigd.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Resultaat:** `v2/data/stroomroute-grafiet-matawinie-becancour.json` (64,3 KB, contract versie 2, `punt_formaat` lonlat) · **één been, truck, doorgetrokken, 194,1 km, 3.135 punten, 2 markers**, geen stippel, geen zee/spoor/leiding/vlucht, geen haven-aanloop. Titel: *Grafiet · Matawinie → Bécancour (Canada) — project-as, volume nul*. Functie `bak_grafiet_matawinie_becancour()` in `v2/tools/bak_stromen.sh`; profiel `grafiet-matawinie-becancour-matawinie-becancour` in `v2/tools/maak_stroombeen_weg.py` (extract canada).

| # | modaliteit | km (gebakken) | km (brief) | afwijking | naad |
|---|---|---|---|---|---|
| b1 | truck | 194,1 (weggeometrie 192,4 + anker-stubs 1,33 + 0,40) | 192,4 (OSRM langs de via-punten; kortste OSRM 179,3; hemelsbreed 127,4) | +0,9% t.o.v. 192,4 · +8,2% t.o.v. de kortste OSRM — **indicatie, geen norm** (geen echte wegkm) | n.v.t. (één been) |

**Recept.** Weggeometrie via `maak_stroombeen_weg.py --bron overpass` (pyosmium is door het toepassingsbeheerbeleid geblokkeerd, het tool zelf wijst Overpass aan als gelijkwaardige bron). 7 segmenten over 8 punten: mijn → QC-131 Route Louis-Cyr 66,0 km · → QC-131 noord Joliette 23,7 · → A-40 Berthierville 33,3 · → A-40/A-55 Trois-Rivières-noord 44,9 · → Pont Laviolette 5,1 · → A-30 × QC-132 15,3 · → proxy-anker 4,3. Snaps van de via-punten 0,00–0,01 km, behalve de mijn (1,33 km, zie hieronder) en de Pont Laviolette (1,19 km: de brug is in OSM één lange way met spaarzame vertices). Alle via-punten uit de brief zijn ongewijzigd gebruikt; geen enkel via-punt is verschoven of bijgeschoven.
**Wegklassen.** 35.120 ways in de graaf; 9.716 kleine-klasse-ways binnen 12 km van de ankers deden mee. First mile over kleine klassen 8,98 km (residential/service/tertiary/unclassified: Rue des Aulnaies en Saint-Michel), last mile 0,70 km (unclassified).
**Toets (handleiding §5).** Lengtetoets +0,2% tegen 192 (`gepubliceerdKm`, = OSRM langs de via-punten, dus een rekenkundige gelijkenis en geen onafhankelijke wegkm). Markers 0,0 km van de lijn (het anker is begin- resp. eindpunt). `toets_knikken.py`: 14 knikken ≥ 60° (alle 6–79 m spikes op OSM-kruispunten bij Joliette, Pont Laviolette en Louis-Cyr), **0 omkeringen, 0 terugloop**; `toets_rechte_benen.py`: geen treffer voor deze stroom. json.load OK, versie 2, lonlat, modaliteit `truck`, 3.135 punten, 64,3 KB.
**Keerlussen gesnoeid:** 43 (192,5 → 192,4 km).

**Bevindingen / toelichting (geen stippel, geen aanloop, geen vlucht, geen leiding in dit been).**
- **Mijn-naad 1,33 km (⚠️ > 0,5 km, < 2 km → geen last-mile-stippel):** de nieuwe 9 km-toegangsweg staat niet doorgaand in OSM; de lijn begint met een rechte anker-stub van 1,33 km naar de dichtstbijzijnde OSM-weg en loopt dan over Rue des Aulnaies/Saint-Michel naar QC-131, precies de verwachting uit §7. Blijft staan als procesgat; geen via-punt bijgeschoven.
- **Eind-naad 0,40 km** tot het proxy-anker li-bc-fabriek (zelfde orde als lithium-whabouchi-becancour, 0,25 km): binnen norm.
- **A-31 vs QC-158/QC-345:** de router koos het korte pad (192,4 km, binnen MELCC "moins de 200 km"); de A-31-variant (+~30 km) is dus niet gekozen.
- **Volume nul / aannemelijk:** het been draagt "(aannemelijk: kavel niet gelegd; volume nul tot 2028)" in zijn naam; de lijnstijl is doorgetrokken (stippel betekent alleen "hier reikt het net niet").
- **Eindanker = proxy.** Sitelaag `w-nmg-becancour` (46,3400, −72,3500) ligt 3,9 km van het proxy-anker (46,3583, −72,3938): centraal gelijk te trekken.
- **Gereedschapsles (Overpass):** overpass-api.de reset de verbinding en kumi gaf 500; de bbox-query van `_ways_uit_overpass` (3,5° × 2,5°, alle highway-klassen rond Montréal) is hier te zwaar. Gedraaid via een wrapper in de scratchpad (tool ongewijzigd) die `_ways_uit_overpass` vervangt door getegelde `around`-queries per via-segment op mail.ru + private.coffee: hoofdklassen (motorway–secondary + links) 70 km, tertiary/unclassified 40 km, alle kleine klassen 12,5 km rond beide ankers; hetzelfde `weg_houden`-filter en dezelfde Dijkstra. Het `bron`-veld van de weg-geojson blijft hard-coded op "Geofabrik mozambique-latest; routebrief grafiet-balama-vidalia" (cosmetisch, niet in het stroomroute-json). Een herbake van dit profiel vraagt dezelfde wrapper of een werkende Overpass-spiegel.
- **Niet aangeraakt:** register, bundel, sitelagen, `v2/src/*.js`, `v2/index.html`.
