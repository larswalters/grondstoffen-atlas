# Routebrief (licht) · Kolen · RB Kolubara (Vreoci, bruinkool) → industrieel spoor → TENT Obrenovac (Servië)

**stroom-id:** `kolen-kolubara-nikolatesla` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) · **status:** gebakken
**Keten in één zin:** **bruinkool** (geen steenkool) uit het Kolubara-bekken (Elektroprivreda Srbije, RB Kolubara) gaat vanaf het verwerkings- en laadcomplex Vreoci per **EPS-industrieel spoor** (Obrenovac-Vreoci, normaalspoor, los van Srbija Kargo)
naar de kolenontvangst van TPP Nikola Tesla A+B (TENT) in Obrenovac; de verbranding tot stroom is het einde. Eén been, geen zee.
**Welke as van het verhaal:** *Balkan-bruinkool voor de eigen centrale* (nieuw land en regio op de kolenbol). RB Kolubara: **22,6 Mt in 2025**, ca. 90% naar TENT, TE Kolubara en TE Morava samen [2]; spoorlijn tot 37 Mt/j [1]. Peiljaar 2025, TENT-aandeel niet apart gebrond.

## 1 · Ketenkaart
```
Prerada/laadstation Vreoci `kolen-kolubara-laad`
   ──(b1 spoor · industrielijn Vreoci → Obrenovac, noordwaarts door het Kolubara-bekken · router 32,5 km, gepubliceerd 32,45 km)──►
Kolenontvangst TENT Obrenovac `kolen-tent-kolenontvangst` ⏹ stoppunt (centrale verbrandt de kool)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-kolubara-laad` → `kolen-tent-kolenontvangst` | Industrieel spoor Obrenovac-Vreoci (EPS/TENT, normaalspoor): van Vreoci noordwaarts langs de westrand van het bekken naar Obrenovac (tussenpunten zie §4) | **32,45 km** (Wikipedia, hoofdlijn Obrenovac-Vreoci) [1]; router 32,5 km (+0,2%), hemelsbreed 28,9 km (1,13), 55 edges, 98 punten, 0 bochten ≥60° | toets_spoorroute (1-op-1-net, geen via) | nee |

Product in de beennaam: *trein Kolubara (bruinkool) → TENT*. Fase C vervalt (beide ankers op het industriespoor: snap 0,13 en 0,07 km). Geen fase D/E, geen zee/weg/leiding/lucht, geen haven-aanloop, geen kopie.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-kolubara-laad` | mijn / laadplek | Prerada en laadstation Vreoci (RB Kolubara, velden C/E), bedrijfspunt bekken | 44.4289, 20.2864 | [2][3][4] | bron-gelegd (z15 gezien: scheidings-/verwerkingsinstallatie met bandbruggen, bunkers en een spoorbundel die noordwaarts het terrein uit loopt; pit C/E noordwest en de Tamnava-groeve aan de overkant). Exacte laadspoor niet apart aangewezen (site-niveau) |
| `kolen-tent-kolenontvangst` | losplek / verwerker | Kolenontvangst TPP Nikola Tesla A+B (EPS), Obrenovac | 44.6717, 20.1572 | [1][5] | bron-gelegd (z15/z16 gezien: kolenopslag met twee stapel-/afzetmachines en bandbruggen naar de ketelblokken, spoorbundel met rangeeremplacement zuid van het complex, Sava ten oosten). Anker ligt aan de westrand van het ketelhuis, 0,07 km van het spoor |

Hergebruik: geen bestaand anker (geen Servische kolensite in de sitelaag; kolen-hambach was ook Europees maar ander terrein). Wikipedia-centralepunt TENT A (OSM way 180603115) 44.6714, 20.1604 ligt 0,26 km oostelijker, op het ketelhuis, en is niet gebruikt [5].

## 4 · Via-punten
Geen (bindend uit de haalbaarheidstoets). De route is één Dijkstra over het 1-op-1-net en volgt de corridor zonder omweg of keerpunt (0 bochten ≥60°). Gemeten volgorde, ter controle (geen via): 44.4374, 20.2806 → 44.4799, 20.2863 → 44.4983, 20.2604 → 44.5149, 20.2072 → 44.5640, 20.1671 → 44.5982, 20.1499 (OSM `railway=yard` way 187916404 op ca. 44.601, 20.151) → 44.6229, 20.1554 → 44.6680, 20.1567.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| RB Kolubara (velden C, E, G, Tamnava-West; Vreoci scheiding en Tamnava-West breekinstallatie) | EPS | bruinkool → werkspoor | 22,6 Mt (2025); 22 tot 40 Mt in andere bronnen | [2][3] |
| TPP Nikola Tesla A+B | EPS | bruinkool → stroom | 2.814 MW totaal EPS-park (A 1.650, B 1.240 volgens Wikipedia, interne tegenspraak) | [1] |

## 6 · Stoppunt
De brief stopt bij de kolenontvangst van TENT: de bruinkool wordt daar verbrand en er is geen volgende fysieke locatie van de lading (asafvoer is een ander product).

## 7 · Open punten
- **Bruinkool is geen steenkool:** centraal beslissen of de bol dit onder `kolen` toelaat (zoals bij Hambach); het stroom-id blijft staan.
- **Het ontwerp zegt "ca. 90% naar TENT"; Wikipedia zegt 90% naar TENT, TE Kolubara en TE Morava samen** [2]. Het TENT-aandeel is niet gebrond; volume is dus de RB Kolubara-productie, geen TENT-levering.
- **Productiecijfers lopen uiteen** (22,6 Mt in 2025 [2]; ca. 30 Mt/j verbruik in een artikel van 2010; 37 Mt is spoorcapaciteit [1], geen verbruik).
- **Het ankerpunt is het bedrijfspunt, geen pit:** de pit-ankers zijn OSM-quarries (Tamnava West, OSM way 174402881, centroïde 44.4839, 20.2116; Veliki Crljeni way 822359107 44.4666, 20.2676) en niet als marker opgenomen: de band van pit naar Vreoci is geen been.
- **Laadstation Tamnava** (4 sporen, 2 laad) [web-samenvatting, niet geverifieerd] is niet apart gelegd; alleen Vreoci (7 sporen, 4 laad). OSM-station Vreoci staat op 44.4490, 20.2795 (2,2 km noord van het anker) en is een personenstation.
- **TE Kolubara A (Veliki Crljeni) en TE Morava** worden niet getekend. "Vorbis B" (Wikipedia, losstation) is niet te plaatsen en niet gebruikt.
- Servische bron-opgave van de spoorlijn (EPS-jaarverslag) niet geraadpleegd: 32,45 km komt uit Wikipedia.

## 8 · Bronnen
[1] en.wikipedia, TPP Nikola Tesla — Obrenovac-Vreoci 32,45 km, spoor tot 37 Mt/j, laadstations Vreoci en Tamnava, 44°40′18″N 20°09′26″E. https://en.wikipedia.org/wiki/TPP_Nikola_Tesla
[2] en.wikipedia, RB Kolubara — 22,6 Mt in 2025, ca. 90% naar TENT, TE Kolubara, TE Morava; bekken 44°25′44″N 20°17′11″E. https://en.wikipedia.org/wiki/RB_Kolubara
[3] EPS, Kopovi — velden C, E, Tamnava-West, G; scheiding Vreoci (C/E), breekinstallatie Tamnava-West. https://www.eps.rs/eng/Poslovanje-ugalj/Pages/Kopovi.aspx
[4] OSM (lokale Geofabrik-extract servie, 2026-10-31): station Vreoci node 313235264, quarries Tamnava west/zuid/oost en Veliki Crljeni, Polje B/D/E (landuse=quarry, resource=coal, operator EPS).
[5] OSM way 180603115 Termoelektrana Nikola Tesla A (44.6714, 20.1604) en web-samenvatting TENT-spoor: Vreoci 7 sporen/4 laad, Tamnava 4/2, Obrenovac A 5 sporen/2 los. https://en.wikipedia.org/wiki/Kolubara ; https://gem.wiki/Nikola_Tesla_power_station
[6] Haalbaarheidstoets keten kolen-kolubara-nikolatesla (2026-10-31): route 32,5 km, snaps 0,13 en 0,07 km, geen omkeringen.
[7] Esri World Imagery via `v2/tools/sat_check.py` (2026-10-31): `v2/build-cache/satcheck/sat-kolen-kolubara-nikolatesla-vreoci.png`, `-prerada.png`, `-tent.png`, `-tentend.png`.
[8] toets_spoorroute (BAKE_SUFFIX=-raw, hoofd-km 100): `v2/build-cache/ais/graaf/spoorroute-kolen-kolubara-nikolatesla-tamnava-tent.geojson`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)
- **Bestand:** `v2/data/stroomroute-kolen-kolubara-nikolatesla.json` (versie 2, lonlat, 2,5 KB), functie `bak_kolen_kolubara_nikolatesla` in `v2/tools/bak_stromen.sh`. Register en bundel centraal, niet door de bak-agent.
- **Been:** b1 spoor, doorgetrokken, 98 punten, **32,7 km** in het json (router 32,5 km, som van de puntafstanden 32,73 km) tegen 32,45 km gepubliceerd (Wikipedia): +0,8%, binnen de +-15%-toets. Geen via-punten, geen stippel, geen haven-aanloop, geen kopie, geen vlucht, geen leiding.
- **Markers:** 2, `kolen-kolubara-laad` (44.4289, 20.2864) op 0,13 km van de lijn en `kolen-tent-kolenontvangst` (44.6717, 20.1572) op 0,07 km. Naad tussen benen: n.v.t. (een been).
- **Recept:** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs "--van=44.4289,20.2864" "--naar=44.6717,20.1572" "--naam=kolen-kolubara-nikolatesla-tamnava-tent" --hoofd-km=100` gaf het geojson `spoorroute-kolen-kolubara-nikolatesla-tamnava-tent.geojson` (al op schijf, hergebruikt, niet opnieuw gerouteerd); daarna `bash v2/tools/bak_stromen.sh kolen-kolubara-nikolatesla` (15 s).
- **Toets:** toets_knikken 0 knikken, 0 omkeringen; toets_rechte_benen meldt niets voor dit id; json: versie 2, punt_formaat lonlat, modaliteit spoor, >= 2 punten.
- **Bruinkool:** het product is bruinkool, geen steenkool; de titel noemt dat. Centraal beslissen of de bol dit onder kolen toelaat (zoals Hambach).
- **Les:** een 1-op-1-spoorrun zonder via over een kort industrielijntje geeft in een keer een schone lijn (snap 0,13 / 0,07 km); de gemeten km hoefde niet bijgesteld.
