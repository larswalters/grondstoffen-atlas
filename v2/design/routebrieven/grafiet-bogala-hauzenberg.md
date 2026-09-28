# Routebrief (licht) · grafiet — Bogala-mijn (Sri Lanka) → Colombo → Hamburg → Hauzenberg (Duitsland)

**stroom-id:** `grafiet-bogala-hauzenberg` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken
**Keten in één zin:** Sri Lankaans premium ader-/klompgrafiet van de ondergrondse Bogala-mijn per **truck**
naar de Jaya Container Terminal in Colombo, per **containerschip** (MARNET) naar de Container Terminal
Burchardkai in Hamburg, per **truck** over de A7/A3-as naar Graphit Kropfmühl GmbH in Hauzenberg (Bayern) —
de eigendoms-as van het Bogala-mijnaandeel, en de tweede niet-Chinese afnemer op de kaart.
**Welke as van het verhaal:** eigendoms-as Sri Lanka → Duitse moedermaatschappij-verwerker. Bogala
Graphite Lanka Plc produceert ≈3,2 kt/j vlokconcentraat [B12]; Graphit Kropfmühl GmbH bezit **86,46 %**
van Bogala Graphite Lanka Plc [3] — sinds de op 2025-10-10 aangekondigde verkoop door AMG Critical
Materials N.V. is Graphit Kropfmühl (incl. Hauzenberg én het Bogala-belang) eigendom van **Asbury
Carbons Inc.** (VS), transactie voltooid volgens Asbury's eigen persbericht [4][5][6].

## 1 · Ketenkaart
```
Bogala-mijn `gr-bogala-mijn` ──(b1 truck · A1 Colombo-Kandy Road via Kegalle-Warakapola-
Nittambuwa-Kadawatha · hemelsbreed 54,0 km, geen wegkm)──► Jaya Container Terminal, Colombo
`gr-colombo-jct` ──(b2a zee · haven-aanloop, stippel, ~8,9 km — kade 8,89 km van MARNET-zeeknoop
5328, > 5 km-drempel sinds LAR-586)──► zeeknoop 5328 ──(b2b zee · Indische Oceaan → Rode Zee →
Suez → Middellandse Zee → Gibraltar → Noordzee → Elbe-estuarium, MARNET · niet gemeten, orde
duizenden km)──► Container Terminal Burchardkai, Hamburg `gr-hamburg-burchardkai` ──(b3 truck ·
A7 Hamburg-Hannover-Kassel-Würzburg → A3 Würzburg-Nürnberg-Regensburg-Passau → B12 Passau-
Hauzenberg · hemelsbreed 605,1 km, geen wegkm)──► Graphit Kropfmühl GmbH, Hauzenberg
`gr-hauzenberg-kropfmuhl` ⏹ stoppunt (fase D vervalt — geen bron voor afzet ná verwerking)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-bogala-mijn` → `gr-colombo-jct` | lokale weg Aruggammana → Kegalle, dan A1 (Colombo–Kandy Road) via Warakapola–Nittambuwa–Kadawatha in de haven | hemelsbreed 54,0 km (kop-staart), via-punten-som 81,7 km; **geen wegkm** — orde ~90–100 km verwacht over de A1, geen gepubliceerde bedrijfs-/overheidsopgave binnen webbudget | maak_stroombeen_weg (extract `sri-lanka`) | nee |
| b2a | B | zee | `gr-colombo-jct` → zeeknoop 5328 (6,99460, 79,78960) | haven-aanloop — kade ligt 8,89 km van de dichtstbijzijnde MARNET-zeeknoop [eigen meting, `hecht_marnet`] | ~8,9 [eigen meting] | maak_havenaanloop | **ja** — haven-aanloop, "hier reikt het net niet" (§HAVEN-AANLOOP, >5 km-regel sinds LAR-586) |
| b2b | B | zee (MARNET) | zeeknoop 5328 → `gr-hamburg-burchardkai` | Indische Oceaan → Arabische Zee → Rode Zee → Suez → Middellandse Zee → Straat van Gibraltar → Golf van Biskaje → Het Kanaal → Noordzee → Elbe-estuarium (Hamburg snapt op 1,41 km van zeeknoop 3944, géén aparte aanloop nodig) | niet gemeten, orde duizenden km (MARNET bepaalt) | MARNET | nee |
| b3 | C | truck | `gr-hamburg-burchardkai` → `gr-hauzenberg-kropfmuhl` | A7 (Hamburg–Hannover–Kassel–Würzburg) → A3 (Würzburg–Nürnberg–Regensburg–Passau) → B12/lokale weg (Passau–Hauzenberg) | hemelsbreed 605,1 km (kop-staart), via-punten-som 726,8 km; **geen wegkm** — orde ~830–850 km verwacht (optelling bekende A7/A3-segmentlengtes), geen gepubliceerde bedrijfsopgave voor déze route | maak_stroombeen_weg (extract `de-hamburg` + `de-niedersachsen` + `de-hessen` + `de-bayern`) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-bogala-mijn` | mijn (ondergronds, ader-/klompgrafiet) | Bogala-mijn, Aruggammana, Kegalle District — **hergebruik sitelaag-anker `w-bogala` (letterlijk)** | 7,1164, 80,3106 | [1][2], sitelaag `v2/design/grafiet-sitelaag.json` (`w-bogala`) | **aannemelijk** (ongewijzigd t.o.v. sitelaag: z15 gezien, kleine bebouwingscluster in bos, geen zichtbare mijninfrastructuur — ondergrondse ader-mijn, kleine voetafdruk; Wikipedia-coördinaat 7,11583/80,31 bevestigt binnen ~65 m [1]) |
| `gr-colombo-jct` | overslag truck → zee | Jaya Container Terminal, Colombo (Kochchikade) | 6,9449, 79,8527 | [8] OSM/Nominatim (exacte match: 6,94486/79,85270) | **bron-gelegd** (z15 gezien, dit onderzoeksbudget: kruis op de rand van de containeropslag/-terminal direct N van de stad, kranen en containerstapels rondom zichtbaar — nieuw satellietgelegd, niet gedaan in de ontwerpronde) |
| `gr-hamburg-burchardkai` | overslag zee → truck | Container Terminal Burchardkai, Waltershof, Hamburg | 53,5328, 9,9223 | [9] OSM/Nominatim | **bron-gelegd** (z15 gezien: kruis midden in een containeropslagveld met rijen containerstapels en kraanbanen aan de Elbe-kade — duidelijk het containerterminal) |
| `gr-hauzenberg-kropfmuhl` | losplek / verwerker | Graphit Kropfmühl GmbH, Langheinrichstraße 1, 94051 Hauzenberg (Kropfmühl), Bayern — **verplaatst en hernoemd t.o.v. sitelaag-anker `w-amg-hauzenberg`** (was gemeentecentrum 48,6516/13,6237) | 48,6218, 13,6599 | [7] Nominatim-adrespunt (haalbaarheidstoets), sitelaag `w-amg-hauzenberg` (basis, gecorrigeerd) | **bron-gelegd** (z15 gezien, dit onderzoeksbudget: kruis op een cluster industriële gebouwen aan de rand van het dorp Kropfmühl, met een turkooise bezink-/verwerkingsvijver direct ten westen — duidelijk beter dan het oude gemeentecentrum-anker, dat ~4,2 km verderop lag) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Kegalle | 7,2532, 80,3454 | waar de lokale mijnweg aansluit op de doorgaande A1 (Colombo–Kandy Road) — sluit een noordelijkere omweg via Mawanella uit |
| b1 | 2 | Warakapola | 7,2250, 80,1965 | de A1 blijft hier doorgaand richting Colombo; sluit een afslag naar de A6/Kurunegala-richting uit |
| b1 | 3 | Nittambuwa | 7,1441, 80,0965 | kruising A1 × A6 (Puttalam-weg) — pint dat de stroom op de A1 blijft, niet naar de noordkust afbuigt |
| b1 | 4 | Kadawatha | 7,0021, 79,9512 | laatste doorgaande punt op de A1 vóór de afslag naar de havenwegen van Colombo — sluit een route via het stadscentrum uit |
| b3 | 1 | Hannover | 52,3745, 9,7386 | de A7 blijft hier zuidwaarts; sluit een oostelijke omweg via de A2 uit |
| b3 | 2 | Kassel | 51,3158, 9,4978 | A7/A44-knoop — pint dat de stroom op de A7 blijft, niet oostwaarts over de A44 |
| b3 | 3 | Würzburg | 49,7780, 9,9435 | A7/A3-knoop — hier verlaat de route de A7 en gaat de A3 op richting het zuidoosten |
| b3 | 4 | Nürnberg | 49,4539, 11,0773 | de A3 blijft doorgaand; sluit een afslag via de A6/A9 uit |
| b3 | 5 | Regensburg | 49,0195, 12,0975 | de A3 blijft doorgaand langs de Donau; sluit een noordelijke omweg via de A93 uit |
| b3 | 6 | Passau | 48,5748, 13,4610 | einde van de A3 vóór de Oostenrijkse grens — hier buigt de route af naar de B12/lokale weg naar Hauzenberg, in plaats van de grens over te steken |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Graphit Kropfmühl GmbH, Hauzenberg (Kropfmühl) | Asbury Carbons Inc. (VS), sinds de op 2025-10-10 aangekondigde overname van AMG Critical Materials N.V. — voorheen "AMG Hauzenberg" | natuurlijk vlokgrafiet (Bogala + andere mijnen/marktbronnen) → verwerkte grafietproducten (SPG/AAM, refractair, dispersies) | GK verwerkt >25.000 t/j natuurlijk grafiet uit eigen mijnen in Afrika/Azië plus marktbronnen; geen apart cijfer voor het Bogala-aandeel gevonden | [7], [4][5][6] |

## 6 · Stoppunt
De brief stopt bij Graphit Kropfmühl Hauzenberg: fase D (afnemer van de daar verwerkte grafietproducten)
is niet gebrond — geen bron koppelt een specifieke vervolgbestemming aan déze Bogala-feedstock. Fase E
vervalt.

## 7 · Open punten
- **BINDEND VERWERKT (haalbaarheidstoets):** bestemmingsanker hernoemd naar "Graphit Kropfmühl GmbH,
  Hauzenberg (sinds 2025/2026 eigendom van Asbury Carbons Inc, VS; voorheen AMG)" en verplaatst naar
  48,6218/13,6599 (Langheinrichstraße 1, Kropfmühl) na satellietblik — was gemeentecentrum, 4,2 km
  verderop. Eigendomspercentage gecorrigeerd naar **86,46 %** [3] i.p.v. 79,58 % (verouderde
  Wikipedia-waarde [1]).
- **⚠️ Closing-datum onzeker:** de AMG-Asbury-transactie werd op 2025-10-10 aangekondigd met
  "verwachte closing eind 2025" [4], maar Asbury's eigen persbericht "Announces Completion of Graphit
  Kropfmühl GmbH Acquisition" is gedateerd medio/eind juli 2026 [5] — de closing liep dus later dan
  oorspronkelijk verwacht. Op de peildatum van deze brief (2026-09-28) is de overname in elk geval
  voltooid.
- **BINDEND VERWERKT (haalbaarheidstoets):** de verplichte haven-aanloop-stippel bij Colombo (~8,9 km,
  been b2a) is toegevoegd — de kade ligt 8,89 km van MARNET-zeeknoop 5328, boven de 5 km-drempel sinds
  LAR-586, óók al snapt de router ruim binnen de 25 km.
  b2a is een STIPPEL, geen doorgetrokken been.
- **BINDEND VERWERKT (haalbaarheidstoets):** fase C krijgt nu een gekozen Europese haven (Hamburg,
  Container Terminal Burchardkai) met een echte corridor + zes via-punten, i.p.v. de eerdere
  hemelsbrede schatting. Hamburg is gekozen op **twee gemeten gronden**: (1) hemelsbreed 605 km tegen
  776 km voor Rotterdam — Hamburg ligt aantoonbaar dichter bij Hauzenberg; (2) Hamburg Burchardkai snapt
  op 1,41 km van zijn MARNET-zeeknoop (géén haven-aanloop nodig), een gegeven dat pas met deze meting
  bekend werd. **Geen bron bevestigt dat Graphit Kropfmühl daadwerkelijk via Hamburg importeert** — de
  havenkeuze is een aannemelijke, gemeten keuze van deze brief, geen gedocumenteerd feit.
- **Kwantitatieve koppeling Bogala → Hauzenberg niet gevonden**: alleen een sterke
  eigendomsindicatie (86,46 %-belang [3]), geen gepubliceerd tonnagecijfer dat specifiek Bogala-vlok aan
  Hauzenberg koppelt. Het jaarvolume in §"Keten in één zin" (3,2 kt/j) is Bogala's totale productie,
  niet per se allemaal naar Hauzenberg.
- Colombo Jaya Container Terminal is dit onderzoeksbudget voor het eerst satellietgelegd (was in de
  ontwerpronde nog niet gedaan) — OSM-naam en -positie bevestigd vrijwel exact (6,94486/79,85270).
- Via-punten b1/b3 zijn bekende steden op de doorgaande corridor (A1 resp. A7/A3), niet zelf
  OSM-wegvertex-geverifieerd binnen het webbudget — de bak-agent routeert over het echte wegnet en kan
  ze op de vertex projecteren.
- Fase D/E vervallen bewust: geen bron voor de afzet ná Hauzenberg-verwerking, specifiek voor
  Bogala-feedstock.

## 8 · Bronnen
[1] Wikipedia, "Bogala Graphite Mine" — locatie 7,11583°N/80,31000°O, vein-grafiet, Graphit Kropfmühl AG 79,58 % (verouderd t.o.v. [3]), Alterna GK LLC 10,33 %. https://en.wikipedia.org/wiki/Bogala_Graphite_Mine
[2] Wikipedia, "Graphite mining in Sri Lanka" — vein-/klompgrafiet, Sri Lanka enige commerciële producent; Bogala + Kahatagaha totaal 9.000–10.000 t/j. https://en.wikipedia.org/wiki/Graphite_mining_in_Sri_Lanka
[3] Daily FT, "US firm AMG takes over Bogala Graphite's owning company of German origin" — Graphit Kropfmühl GmbH bezit 86,46 % van Bogala Graphite Lanka PLC. https://www.ft.lk/business/US-firm-AMG-takes-over-Bogala-Graphite-s-owning-company-of-German-origin/34-784111
[4] AMG Critical Materials N.V., persbericht 2025-10-10 — "Announces Sale of Graphit Kropfmühl GmbH to Asbury Carbons": $65 mln enterprise value, verkochte entiteiten incl. de mijn in Duitsland en het meerderheidsbelang in Sri Lanka, verwachte closing eind 2025. https://amg-nv.com/investors/press-release/amg-critical-materials-n-v-announces-sale-of-graphit-kropfmuhl-gmbh-to-asbury-carbons/
[5] Businesswire, "Asbury Advanced Materials Announces Completion of Graphit Kropfmühl GmbH Acquisition" (2026). https://www.businesswire.com/news/home/20260729506571/en/Asbury-Advanced-Materials-Announces-Completion-of-Graphit-Kropfmhl-GmbH-Acquisition
[6] Businesswire, "Asbury Carbons Signs Intent to Acquire Graphit Kropfmühl GmbH ('GK')" (2025-10-14). https://secure.businesswire.com/news/home/20251014554959/en/Asbury-Carbons-Signs-Intent-to-Acquire-Graphit-Kropfmhl-GmbH-GK
[7] Bayern International — bedrijfsprofiel Graphit Kropfmühl GmbH: adres Langheinrichstr. 1, 94051 Hauzenberg; >25.000 t/j natuurlijk grafiet verwerkt uit eigen mijnen (Afrika/Azië) + marktbronnen. https://www.bayern-international.de/en/company-database/company-details/graphit-kropfmuehl-gmbh-2771
[8] OpenStreetMap/Nominatim (ODbL) — "Jaya Container Terminal", Colombo: 6,94486/79,85270 (landuse=container_terminal, way/419827605). https://www.openstreetmap.org
[9] OpenStreetMap/Nominatim (ODbL) — "Container Terminal Burchardkai", Waltershof, Hamburg: 53,53284/9,92229 (landuse=industrial, relation/15625871). https://www.openstreetmap.org
[10] `v2/design/grafiet-sitelaag.json` — hergebruikte ankers `w-bogala` (7,1164/80,3106) en `w-amg-hauzenberg` (48,6516/13,6237, basis voor de correctie).
[eigen meting] `v2/tools/hecht_marnet.py` (`marnet_zee`, `v2/build-cache/marnet-preais`) — zeeknoop-afstand Colombo Jaya CT 8,89 km (knoop 5328) en Hamburg Burchardkai 1,41 km (knoop 3944).
Satellietblik: `v2/build-cache/satcheck/sat-grafiet-bogala-hauzenberg-colombo-jct.png`,
`sat-grafiet-bogala-hauzenberg-hamburg-burchardkai.png`, `sat-grafiet-bogala-hauzenberg-kropfmuhl.png`
(Esri z15, 2026-09-28).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Recept:** `v2/tools/bak_stromen.sh` → `bak_grafiet_bogala_hauzenberg()`; draaien met
`bash v2/tools/bak_stromen.sh grafiet-bogala-hauzenberg`. Weg-tekengeometrie uit
`v2/tools/maak_stroombeen_weg.py` (profielen `grafiet-bogala-hauzenberg-bogala-colombo` en
`grafiet-bogala-hauzenberg-hamburg-hauzenberg`, direct ná de PROFIELEN-ankerregel).
Uitvoer: `v2/data/stroomroute-grafiet-bogala-hauzenberg.json` (408,1 KB).

| # | modaliteit | km | punten | naad met vorige | toelichting |
|---|---|---|---|---|---|
| b1 | truck | 93,2 | 3.034 | 0,00 km (start) | Bogala-mijn → Kegalle → Warakapola → Nittambuwa → Kadawatha → Jaya Container Terminal Colombo (lokale weg → A1); **geen gepubliceerde wegkm** — hemelsbreed 54,0 km was alleen referentie, geen norm. |
| b2a | zee (**stippel**) | 8,9 | 2 | 0,00 km | Haven-aanloop Colombo, VERPLICHT (LAR-586: kade 8,89 km van MARNET-zeeknoop 5328, boven de 5 km-drempel). `maak_havenaanloop.py` liep vast op `timeout 300` (**exit 124**) → per bakhandleiding §2 geen tweede poging, rechte stippel-terugval. |
| b2b | zee (MARNET) | 13.125,0 | 1.373 | 0,00 km | Colombo → Hamburg, kade-coördinaten (router snapt zelf: Colombo op zeeknoop 5328/8,89 km via de aanloop, Hamburg op zeeknoop 3944/1,41 km — geen tweede aanloop nodig, onder de 5 km-drempel). |
| b3 | truck | 852,5 | 17.516 | 1,41 km (= de Hamburg-zeesnap, binnen de 5 km-norm) | Container Terminal Burchardkai → Hannover → Kassel → Würzburg → Nürnberg → Regensburg → Passau → Graphit Kropfmühl GmbH Hauzenberg (A7 → A3 → B12/lokale weg); orde ~830-850 km verwacht, gemeten 851,8 km vóór de anker-verbindingsstukjes — **binnen de verwachte orde**. |

**Totaal: 14.079,6 km · 21.925 punten · 4 markers** (één per anker uit §3, letterlijk de coördinaten
uit die tabel). `toets_knikken.py`: 0 omkeringen ≥150°, 0 terugloop op alle vier de benen (de
gerapporteerde "spikes" zijn kleine-straal OSM-zigzags, geen kopmaak-artefact). `toets_rechte_benen.py`:
alleen de b2a-stippel heeft omwegfactor 1,000 — verwacht, want dat IS een rechte stippel. Markers
allemaal ≤ 0,1 m van hun lijn. `json.load` slaagt, `versie: 2`, `punt_formaat: lonlat`, modaliteiten
`{truck, zee}` (beide in de toegestane set), elk been ≥ 2 punten.

**⚠️ Bevinding — anker-verbinding Hamburg-kant 0,62 km (> 0,5 km-norm).** Het dichtstbijzijnde OSM-punt
bij Container Terminal Burchardkai (0,31 km van het anker) is een geïsoleerd eiland van 20 knopen /
2 `highway=service`-ways zonder enige verbinding met het publieke wegnet — gemeten met een eigen
BFS-componenttoets op de gebakken graaf (component 20 knopen tegen het hoofdcomponent van 963.864/
868.157 knopen). Dit is een OSM-karteringsgat in het terminalterrein, geen "site > 2 km van het net"
(de kade lag namelijk al op 0,31-0,62 km). Opgelost binnen het eigen profiel: `eindKlassen` laat
`service` bewust weg (alleen `residential`/`tertiary`/`unclassified`), waardoor het anker op 0,62 km
snapt op een knoop in het hoofdcomponent en de Dijkstra gewoon doorroutet. Zonder die profielaanpassing
gaf de scan `⚠️ corridor niet gerouteerd: geen wegpad tussen punt 0 en 1`.

**⚠️ Bevinding — bestandsgrootte 408,1 KB**, boven de indicatieve ~300 KB uit de bakhandleiding §5. Komt
van de twee lange weg-geojson-benen (3.034 + 17.516 punten over 93 resp. 852 km) — geen fout, wel iets
zwaarder dan de meeste lichte stromen; geen actie ondernomen (geen norm, alleen indicatie).

**Lessen voor de volgende bak-agent:** een havenanker dat op de kaart een goede kade lijkt kan bij een
grote containerterminal tóch een geïsoleerd OSM-service-wegeiland als dichtstbijzijnde punt hebben —
een BFS-componenttoets op de gebakken graaf (in plaats van alleen de snap-afstand) vangt dat vóór de
Dijkstra faalt. `eindKlassen` per profiel weglaten van een klasse is dan een gerichte, eigen-profiel-
alleen fix; het raakt geen andere stroom.
