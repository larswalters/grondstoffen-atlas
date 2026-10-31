# Routebrief (licht) · grafiet — Kasiya → Lilongwe-spoorknoop → Nkaya → Nacala (Malawi → Mozambique)

**stroom-id:** `grafiet-kasiya-nacala` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** natuurlijk vlokgrafiet (en rutiel) van het Kasiya-project van Sovereign Metals (40 km NW van Lilongwe, pre-productie) gaat per **spoor** over de Malawische Sena/Nacala-lijn (Lilongwe → Salima → Nkaya, 321,8 km) en daarna de Nacala-corridor (Nayuchi → Cuamba → Monapo → Nacala, 712,4 km) naar de containerterminal van Nacala. Stoppunt = Nacala-kade, geen zeebeen.
**Welke as van het verhaal:** *Malawi als nieuw grafietland* — Kasiya heeft de tweede grote vlokafzetting ter wereld; **275 kt grafiet per jaar bij steady state** (DFS april 2026, 25 jaar mijnleven) [1][2]. **Volume nu nul:** pre-productie, geen bindende afnemer (Mitsui/Traxys alleen niet-bindende MOU's) [3]. Eenheid: kt grafiet/j (concentraat). **Aannemelijk, niet bevestigd:** Nacala is de voorkeurscorridor [3][4], maar mining-technology noemt ook de Sena-lijn naar Beira [2] en de DFS-pagina noemt geen haven [1] — de Beira-variant wordt niet getekend.

## 1 · Ketenkaart
```
Kasiya-site `gr-kasiya-site` (OSM-dorp, onzeker) ──(b1 truck-stippel · last mile · 17,8 km)──► spoorknoop Lilongwe–Mchinji-lijn `gr-kasiya-spoorknoop`
  ──(b2 spoor · Lilongwe → Salima → Nkaya · 321,8 km gemeten)──► Nkaya-knoop `gr-nkaya-knoop` (splitsing Sena west / Nacala-lijn)
  ──(b3-b5 spoor · Nayuchi → Cuamba → Monapo · 642,3 km · LETTERLIJKE KOPIE kolen-moatize-nacala)──► Monapo-knoop `gr-monapo-knoop`
  ──(b6 spoor · Monapo → Nacala-Porto · 70,1 km gemeten)──► Nacala containerterminal `gr-nacala-kade` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (last mile) | `gr-kasiya-site` → `gr-kasiya-spoorknoop` | geen net op deze korrel; laadpunt/spoorspur onbekend, weg niet gemeten | 17,8 hemelsbreed [9][13] (Sovereign plant een 6 km-spoorspur vanaf de plant, niet gebouwd [3]) | `--stippel "truck|…"` | **ja** — reden in de naam |
| b2 | A | spoor | `gr-kasiya-spoorknoop` → `gr-nkaya-knoop` | Sena-lijn (Mchinji–Lilongwe–Salima–Nkaya) [7][8] | **hemelsbreed 218,5 km (knoop-tot-knoop), geen wegkm** en geen gepubliceerde spoorkm; gemeten 321,8 (omwegfactor 1,47: de lijn buigt via Salima) | toets_spoorroute, `BAKE_SUFFIX=-raw`, `--hoofd-km=100`, 1 run | nee |
| b3 | A | spoor | Nkaya → Nayuchi | Nacala-lijn, grens MW/MZ | 99,5 (kopie) | **kopie** `spoorroute-kolen-moatize-nacala-nkaya-nayuchi.geojson` | nee |
| b4 | A | spoor | Nayuchi → Cuamba | Nacala-lijn | 79,6 (kopie) | **kopie** `…-nayuchi-cuamba.geojson` | nee |
| b5 | A | spoor | Cuamba → Monapo | Nacala-lijn (Nampula-corridor) | 463,2 (kopie) | **kopie** `…-cuamba-monapo.geojson` | nee |
| b6 | A | spoor | Monapo → `gr-nacala-kade` | Nacala-lijn, hoofdtak naar Nacala-Porto (niet de kolentak naar Nacala-a-Velha) | 70,1 gemeten, snap 0,36 km; kolenketen meet 71,9 naar Nacala-a-Velha [10] | toets_spoorroute, 1 run | nee |
Totaal spoor gemeten 1.034,2 km (+ 17,8 stippel). Indicatie Nkaya → Nacala: 912 (Nacala-spoor [5]) min 220 (Moatize → Nkaya gemeten [10]) ≈ 692 afgeleid tegen 712,4 gemeten = +3 % (afgeleid, geen directe bron). Geen zeebeen, dus geen haven-aanloop. Gedeeld met een bestaande stroom: b3-b5 (62 % van de spoorkm).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-kasiya-site` | mijn / laadplek | Kasiya-project (Sovereign Metals), OSM-dorp Kasiya | -13.7533, 33.4149 | [9] OSM (village); project 40 km NW Lilongwe [1][2] | **onzeker** (z14 gezien [12]: dorp op een kruising in akkerland, geen mijn of plant zichtbaar — project niet gebouwd; het dorp is geen mijnterrein) |
| `gr-kasiya-spoorknoop` | overslag truck → spoor (aansluitpunt) | spoorknoop op de Lilongwe–Mchinji-lijn, 17,8 km ZZW van het dorp | -13.9136, 33.4184 | [13] router-snap op het 1-op-1-net (0,00 km); naastliggende OSM-spoorvertex -13.8949, 33.3889 op 16,0 km | aannemelijk (z15 gezien [12]: smalle spoorbaan kruist het punt in WNW-OZO-richting; echt laadpunt onbekend) |
| `gr-nkaya-knoop` | knoop (geen overslag) | Nkaya, splitsing Sena-lijn / Nacala-lijn | -15.1173, 35.0230 | [10] letterlijk hergebruikt uit kolen-moatize-nacala (OSM railway=station) | bron-gelegd (z15 gezien [12]: dubbele band spoor/weg loopt NNW-ZZO door het punt, kruising met lokale weg) |
| `gr-monapo-knoop` | knoop (geen overslag) | Monapo, spoorsplitsing | -14.9155, 40.2972 | [10] letterlijk hergebruikt uit kolen-moatize-nacala | aannemelijk (router snapt 1,67 km, zelfde knoop 1945236 als de kolenketen) |
| `gr-nacala-kade` | overslag spoor → schip (stoppunt) | Porto de Nacala — containerterminal oostoever | -14.5383, 40.6673 | [11] letterlijk hergebruikt uit grafiet-balama-laixi / -vidalia; 1 containerberth [6] | bron-gelegd (z15 gezien [12]: kranen en containerstapels op de noordkop van de kade, punt aan de waterkant ~150 m noordwestelijk; spoor snapt op 0,36 km) |

## 4 · Via-punten
Geen via-punten: b2 is één router-run zonder corridorkeuze (één spoorlijn Lilongwe → Salima → Nkaya; Beira-alternatief wordt bewust niet getekend). De runnaden zijn de knopen Nkaya en Monapo (naden 0,000 km, zelfde routeknopen 1899377 en 1945236 als de kolenketen).

## 5 · Verwerkingsknopen
Geen. Geen bron noemt een processing- of containeriseringsplek buiten de mijn; Sovereign heeft alleen een MOU met Nacala Logistics voor spoor, haven en havenhandling van Malingunde-grafietconcentraat, niet voor Kasiya [4].

## 6 · Stoppunt
De brief stopt bij de Nacala-kade: geen bron noemt een afnemer of bestemmingshaven voor Kasiya-grafiet (alleen niet-bindende MOU's met Mitsui en Traxys [3]), dus geen zeebeen en geen fase D/E.

## 7 · Open punten
- **Haven niet bevestigd:** Nacala is de voorkeurscorridor [3][4], maar mining-technology noemt ook de Sena-lijn naar Beira [2]; de DFS-pagina noemt geen haven [1]. De DFS zelf is niet gelezen (alleen de projectpagina). Nacala is aannemelijk (één corridor-bron + Japan-corridorinitiatief), geen bevestiging.
- **Kasiya-anker onzeker:** OSM-dorp, geen mijn of plant zichtbaar; de plant en de 6 km-spoorspur [3] liggen mogelijk dichter bij de lijn dan het dorp. b1 is daarom een stippel van 17,8 km met een aanname-eindpunt.
- **Spoor Lilongwe–Nkaya zonder gepubliceerde km** (alleen hemelsbreed 218,5); de CEAR-lijn is volgens Wikipedia sinds de oorlog niet operationeel op delen van het Sena-traject [7] — status Lilongwe–Nkaya niet gecontroleerd.
- Capaciteit: spoor ~15 % benut, haven Nacala ~41 % benut volgens Sovereign [4]; geen eigen meting.
- De 6 km-spoorspur en een eventueel laadpunt bij de mijn staan niet in OSM; geen coördinaat verzonnen.
- Het jaarvolume 275 kt komt van de projectpagina (peiljaar DFS 2026, steady state); nu 0.

## 8 · Bronnen
[1] Sovereign Metals, Kasiya Project: ~275 kt/j natuurlijk grafiet bij steady state, DFS april 2026, 25 jaar, 24 Mtpa erts, ~40 km van Lilongwe, "existing rail corridor" en "deepwater port" zonder naam. https://sovereignmetals.com.au/kasiya-project/
[2] Mining Technology, Kasiya rutile-graphite project: 40 km NW Lilongwe; trucken naar zeehavens via de Nacala Rail Corridor OF de Sena-lijn naar Beira; 538 Mt reserve, 8,9 Mt grafiet. https://www.mining-technology.com/projects/kasiya-rutile-graphite-project-malawi/
[3] Mining Weekly / Sovereign ASX, 2025-09-11 (via WebSearch-samenvatting; de pagina zelf gaf HTTP 403): Nacala-corridor voorkeursroute voor de komende DFS, 6 km-spoorspur plant → corridor, Mitsui/Traxys-offtake alleen niet-bindende MOU's. https://www.miningweekly.com/article/japans-7bn-nacala-corridor-initiative-boosts-sovereign-metals-kasiya-project-2025-09-11
[4] Stockhead, Sovereign Metals over Malawi-logistiek: Nacala Logistics Corridor via de diepwaterhaven Nacala bevestigd als voorkeurscorridor (scopingfase), spoor ~15 % benut, haven ~41 %; MOU met Nacala Logistics dekt Malingunde, niet Kasiya. https://stockhead.com.au/resources/sovereign-metals-says-malawis-exceptional-logistics-infrastructure-perfect-for-its-kasiya-rutile-project
[5] Wikipedia, Nacala railway: 912 km, stations Nacala, Monapo, Nampula, Cuamba, Nayuchi, Liwonde, Nkaya; Nkaya-Moatize-uitbreiding 2017, Nacala-a-Velha-tak. https://en.wikipedia.org/wiki/Nacala_railway
[6] Wikipedia, Port of Nacala: 931 km spoor, vier stukgoed- en één containerberth, kolenterminal Nacala-a-Velha aan de overzijde van de baai. https://en.wikipedia.org/wiki/Port_of_Nacala
[7] Wikipedia, Rail transport in Malawi: Nkaya-interconnectie Nacala-/Sena-lijn; Sena-lijn verbindt Mchinji, Lilongwe, Salima, Nkaya; Sena-deel naar Beira niet operationeel. https://en.wikipedia.org/wiki/Rail_transport_in_Malawi
[8] Wikipedia, Sena railway: Malawische deel (CEAR) Marka–Mchinji, verbinding met Nacala-lijn bij Nkaya. https://en.wikipedia.org/wiki/Sena_railway
[9] OpenStreetMap (ODbL) via Nominatim: Kasiya, Lilongwe, Central Region = village -13.7533159, 33.4149364. https://nominatim.openstreetmap.org/search?q=Kasiya,Malawi&format=json
[10] Atlas: `v2/design/routebrieven/kolen-moatize-nacala.md` en `bak_kolen_moatize_nacala` (Nkaya, Nayuchi, Cuamba, Monapo, de drie spoorsegmenten Nkaya → Monapo, 642,3 km).
[11] Atlas: `v2/design/routebrieven/grafiet-balama-laixi.md` en `grafiet-balama-vidalia.md` (anker `gr-nacala-kade`, containerterminal oostoever).
[12] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15, 2026-10-31): `v2/build-cache/satcheck/sat-grafiet-kasiya-nacala-kasiya.png`, `-spoorknoop.png`, `-nacala.png`, `-nkaya.png`.
[13] Eigen metingen `toets_spoorroute.mjs` (BAKE_SUFFIX=-raw, 3260717 spoor-edges): Lilongwe-knoop → Nkaya 321,8 km (132 edges, grootcirkel 218,5); Monapo → Nacala 70,1 km (34 edges, snap 0,36 km); last mile hemelsbreed 17,83 km.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
`v2/data/stroomroute-grafiet-kasiya-nacala.json` · versie 2, lonlat · 6 benen · **1.053,4 km** (spoor 1.035,6 + stippel 17,8) · 2.009 punten · 4 markers · 38,6 KB. Functie `bak_grafiet_kasiya_nacala` in `v2/tools/bak_stromen.sh` (geen profiel, geen zee, geen haven-aanloop).

| # | modaliteit | geometrie | km gebakken | brief | stippel |
|---|---|---|---|---|---|
| b1 | truck | `--stippel` Kasiya-dorp → spoorknoop, last mile (geen net op deze korrel) | 17,8 | 17,8 hemelsbreed | ja |
| b2 | spoor | `spoorroute-grafiet-kasiya-nacala-lilongwe-nkaya.geojson` (toets_spoorroute -raw, 1 run) | 322,9 | 321,8 gemeten (hemelsbreed 218,5, geen spoorkm) | nee |
| b3 | spoor | letterlijke kopie `spoorroute-kolen-moatize-nacala-nkaya-nayuchi.geojson` | 99,5 | 99,5 | nee |
| b4 | spoor | letterlijke kopie `…-nayuchi-cuamba.geojson` | 79,6 | 79,6 | nee |
| b5 | spoor | letterlijke kopie `…-cuamba-monapo.geojson` | 463,2 | 463,2 | nee |
| b6 | spoor | `spoorroute-grafiet-kasiya-nacala-monapo-nacala.geojson` | 70,4 | 70,1 gemeten | nee |

**Recept:** `bash v2/tools/bak_stromen.sh grafiet-kasiya-nacala` (16 s, zwaar-slot); de twee eigen spoorroute-geojsons stonden al in `v2/build-cache/ais/graaf/` (brief-fase), de bake lijmt alleen. **Markers (4):** Kasiya-dorp (0,0 km van de lijn), spoorknoop (0,0), Nkaya (0,01), Nacala-kade (0,36 = router-snap). Monapo heeft bewust geen marker: knoop zonder overslag, de router snapt 1,67 km ernaast (marker zou de 0,5 km-toets breken).
**Toets:** naden b1-b6 allemaal 0,000 km · `toets_knikken` 0 knikken, 0 omkeringen · `toets_rechte_benen --min-km 5` meldt alleen b1 (de bedoelde stippel van 17,8 km) · alle modaliteiten in {truck, spoor}. Km-toets: brief geeft voor b2 geen echte spoorkm, dus 322,9 tegen 321,8 gemeten is indicatie (+0,3 %, verschil = haversine-som tegen de meetwaarde), b6 +0,4 %.
**Stippel b1:** eerlijk "geen net op deze korrel" - het Kasiya-anker is alleen het OSM-dorp (onzeker), plant en 6 km-spoorspur van Sovereign staan niet in OSM; het eindpunt is de router-snap op de Lilongwe-Mchinji-lijn.
**Aannemelijk:** Nacala als haven rust op een voorkeurscorridor-bron; staat in de naam van b6 en in de brief, de lijn is doorgetrokken. Beira-variant niet getekend.
**Lessen:** (1) bij een keten die uit eerder gemeten spoorbenen bestaat is bakken een kwestie van lijmen; de meting hoort in de briefstap. (2) Een knoop (Monapo) zonder overslag hoeft geen marker; een marker op de brief-coordinaat zou 1,67 km van de lijn staan.
