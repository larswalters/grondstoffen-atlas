# Routebrief (licht) · kobalt — Kolwezi → Luau → Lobito (Angola)

**stroom-id:** `kobalt-kolwezi-lobito` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** kobalt (als hydroxide/artisanaal-formeel materiaal, samen met koperkathode) van het spoorstation Kolwezi, kort over een nieuw stuk baan naar de bestaande Kamoa-railhead, dan per **spoor** over de Benguela-lijn (CFB/Lobito Atlantic Railway, via de grensstations Dilolo/Luau) ~1.710 km naar de mineralenterminal van Porto do Lobito — het westerse, VS-gesteunde alternatief voor de truckroute Kolwezi→Durban.
**Welke as van het verhaal:** *de Lobito-corridor* — staatskobalt (EGC, Entreprise Générale du Cobalt) en CMOC-koper per trein naar de Atlantische Oceaan in ~7 dagen tegen 25 dagen truck naar Durban [1][6]. Eerste EGC/Trafigura-lading: **587 t kobalt + 500 t koperkathode** (ExportFocus Africa, 31-08-2026, niet verder geverifieerd als jaarcijfer) [2]. Jaarvolume over déze corridor is nergens gepubliceerd — de kaart tekent de weg, niet het volume.

## 1 · Ketenkaart
```
Kolwezi-spoorstation `co-kolwezi-laad` ──(b1 spoor · nieuw stuk naar de railhead · ~22 km, onzeker)──►
Kamoa-railhead `co-kamoa-railhead` ──(b2 spoor · Benguela-lijn/CFB, letterlijke kopie van koper-lobito-duisburg b2, via Dilolo/Luau-grens · 1.689,4 km)──►
Lobito mineralenterminal `co-lobito-kade` ──(b3 zee · haven-aanloop, kopie, stippel · 8,6 km)──► stoppunt (bestemming niet gedocumenteerd)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Kolwezi-spoorstation → Kamoa-railhead | 1-op-1-spoornet (congo-drc), geen publicatie | ~22 hemelsbreed | `toets_spoorroute.mjs` (nieuwe run, `BAKE_SUFFIX=-raw`) | nee, tenzij het net hier niet aaneengesloten blijkt |
| b2 | A | spoor | Kamoa-railhead → Lobito mineralenterminal | Benguela-lijn/CFB, via Dilolo/Luau (grens) — **letterlijke kopie van `koper-lobito-duisburg` been 2** | 1.689,4 (gebakken; LAR noemt de as 1.300 Lobito→Luau + 450 Luau→Kolwezi ≈ 1.750) [4][6] | kopie van `spoorroute-kamoa-lobito.geojson` | nee |
| b3 | B | zee | Lobito mineralenterminal → haven-nadering | — **letterlijke kopie van `koper-lobito-duisburg` been 3** (bestaande, gestippelde haven-aanloop) | 8,6 | kopie geojson | ja — ligplaats/bestemming niet vastgesteld; hier stopt de brief |

Som b1+b2+b3 ≈ **1.720 km** tegen LAR's ~1.739 km voor de hele as — binnen ±15%.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-kolwezi-laad` | laadplek / kop van de as | Gare de Kolwezi (CFB-spoorstation en -emplacement) | -10.71495, 25.48365 | OSM/Nominatim (`railway=station` node 983144007) [8], satelliet | **onzeker** (z15/z17 gezien: stationsgebouw direct op een brede spoorbundel met meerdere evenwijdige sporen, midden in de stad — reëel spoorterrein, maar niet bevestigd als hét EGC/LAR-laadpunt; zie §7) |
| `co-kamoa-railhead` | aansluiting (kopie) | railhead waar `spoorroute-kamoa-lobito.geojson` begint (koperbrief `koper-lobito-duisburg`) | -10.66270, 25.28730 | hergebruikt anker, koperbrief | bron-gelegd (in de koperbrief al gelegd; hier alleen hergebruikt als naad tussen b1 en b2) |
| `co-lobito-kade` | losplek / eind van de as | Porto do Lobito — mineralenterminal LAR (Trafigura/Mota-Engil/Vecturis) | -12.34709, 13.54900 | hergebruikt anker, koperbrief (§1b: Rotterdam RHB · Tongling · Beilun · Yangtze-monding · Duisburg · Kamoa · **Lobito**) | open (ligplaats in het water, Esri-beeld van vóór de bouw — ongewijzigd overgenomen) |

## 4 · Via-punten (alleen b2 — grensovergang, overgenomen uit de gekopieerde geometrie)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Dilolo — Congolees grensstation | -10.69886, 22.34423 | de enige spoorgrens tussen Copperbelt en Angola op deze lijn (OSM `railway=station`) [9] |
| b2 | 2 | Luau — Angolees grensstation, hier begint de Benguela-lijn op LAR's eigen kilometrering | -10.70491, 22.22639 | zelfde grensovergang, Angolese kant (OSM `railway=station`) [10] |

## 5 · Verwerkingsknopen
Geen. Dit is een kop-tot-kade-transport zonder tussenraffinage: het kobalt reist als hydroxide/artisanaal-formeel
materiaal en wordt onderweg niet bewerkt. De enige knoop is de overslag spoor→zee op de kade zelf (§3, `co-lobito-kade`).

## 6 · Stoppunt
De brief stopt bij de haven-nadering van Lobito: geen bron noemt de ligplaats binnen de mineralenterminal
(zelfde open punt als in `koper-lobito-duisburg`) en geen bron noemt de bestemming van het kobalt na Lobito —
Trafigura/Fastmarkets spreken alleen van "global markets", de wél gedocumenteerde bestemming (VS) geldt voor
de koperkathode in dezelfde lading [1][2]. Fase B (zee) wordt daarom niet getekend.

## 7 · Open punten
- **`co-kolwezi-laad` is een fallback, geen bevestigd laadpunt.** Het ontwerp wees naar het "Dango Multimodal
  Platform" in Kolwezi als zoeksleutel — onderzoek wijst uit dat Dango juist **halverwege de corridor in de
  provincie Huambo ligt** ("het laatste operationele station vóór Huambo"), gebruikt als weg-spoor-omleiding
  tijdens de overstroming van april 2026 [5][7], niet als laadpunt in Kolwezi. Er bestaat dus geen "Dango-
  platform Kolwezi"; conform de bindende correctie valt de kop terug op het CFB-spoorstation Kolwezi, status
  **onzeker**. De echte EGC/LAR-laadlus in Kolwezi (dry port vs. Gécamines-emplacement) is nergens bij naam
  of coördinaat gedocumenteerd.
- **Nieuw stuk b1 (Kolwezi-station → Kamoa-railhead) is nog niet gebakken.** Het 1-op-1-spoornet in
  `congo-drc.geojson` is tussen lon 25,27 en 25,49 aaneengesloten (eerder gemeten), maar dat is niet in déze
  sessie opnieuw geverifieerd — mislukt de run, dan wordt dit stuk een stippel "hier reikt het net niet".
- **Kobaltvolume over LAR niet uitgesplitst.** Het enige cijfer is de eerste lading (587 t kobalt + 500 t
  koperkathode, ExportFocus Africa) [2] — één bron, geen jaarcijfer, niet geverifieerd tegen een tweede bron.
- **TFM's eigen RR2-spoorsectie** (3,7 km, geopend 2026-01-20, sluit aan op het nationale net bij Fungurume)
  [3] geeft CMOC-kobalt een tweede, wél gebronde spoorkop — maar geen bron documenteert een verscheping via
  Lobito over die aansluiting, dus niet getekend.
- **Lobito-ligplaats blijft open** — ongewijzigd overgenomen uit `koper-lobito-duisburg`: Esri-beeld dateert
  vermoedelijk van vóór de bouw van de mineralenterminal.
- Bestemmingshaven/-koper van het kobalt na Lobito is in geen van de geraadpleegde bronnen genoemd.

## 8 · Bronnen
[1] Trafigura, persbericht 09-02-2026 — "EGC and Trafigura ship copper and cobalt to global markets via the Lobito Atlantic Railway"; ~7 dagen Kolwezi→Lobito tegen 25 dagen truck naar Durban; eerste lading "initially to customers in the U.S." (koper). https://www.trafigura.com/news-and-insights/press-releases/2026/egc-and-trafigura-ship-copper-and-cobalt-to-global-markets-via-the-lobito-atlantic-railway/
[2] ExportFocus Africa, 31-08-2026 — "Congo's EGC targets battery makers after fulfilling cobalt export quotas"; eerste EGC/Trafigura-lading 587 t kobalt + 500 t koperkathode, ~5 dagen. https://exportfocusafrica.com/2026/08/31/congos-egc-targets-battery-makers-after-fulfilling-cobalt-export-quotas/
[3] Fastmarkets, 12-02-2026 — "Entreprise Générale du Cobalt announces shipments to Swiss traders"; noemt ook TFM's RR2-spoorsectie (3,7 km, geopend 20-01-2026, aansluiting nationaal net, volledig TFM-gefinancierd). https://www.fastmarkets.com/insights/entreprise-generale-du-cobalt-announces-shipments-to-swiss-traders/
[4] Lobito Atlantic Railway, "About the Project" — 1.300 km Lobito→Luau (grens) + 450 km verlenging naar Kolwezi, kortste route van Kolwezi naar een Afrikaanse haven. https://www.lobitoatlantic.com/about-the-project/
[5] Lobito Atlantic Railway, 14-05-2026 — "Lobito Atlantic Railway has marked the arrival of the first cobalt shipment at the port of Lobito"; lading "coordinated through the Dango Multimodal Platform". https://www.lobitoatlantic.com/news-resources/social-media/lobito-atlantic-railway-has-marked-the-arrival-of-the-first-cobalt-shipment-at-the-port-of-lobito/
[6] Reuters (Open Interest), 24-06-2026 — "Congo pivots westward under cover of cobalt controls"; LAR als westers alternatief voor de TAZARA-route naar Dar es Salaam. https://www.reuters.com/commentary/reuters-open-interest/congo-pivots-westward-under-cover-cobalt-controls-2026-06-24/
[7] Mining Weekly / Lobito Atlantic Railway, 13/14-04-2026 — overstroming beschadigt de Benguela-lijn (Cavaco-dijkbreuk, Halo-rivierbruggen tussen Cubal en Caimbambo); Dango Multimodal Platform (weg-spoor-omleidingshub) = "het laatste operationele station vóór Huambo", eerste trein 20-04-2026, eerste lading koper/zwavel via Dango 24-04-2026. https://www.miningweekly.com/article/trains-through-angolas-lobito-critical-mineral-corridor-suspended-by-floods-2026-04-13 · https://www.lobitoatlantic.com/news-resources/news/lobito-atlantic-railway-ensures-continuity-of-the-railway-with-multimodal-operation-in-dango/
[8] OpenStreetMap (ODbL) via Nominatim — "Gare de Kolwezi" (building, node 983268780, -10,71428/25,48239) en het spoorstation-knooppunt "Kolwezi" (`railway=station`, node 983144007, -10,71495/25,48365). https://www.openstreetmap.org
[9] OpenStreetMap (ODbL) via Nominatim — grensstation "Dilolo" (`railway=station`, node 8746080946, -10,69886/22,34423, aan de RN39). https://www.openstreetmap.org
[10] OpenStreetMap (ODbL) via Nominatim — grensstation "Luau" (`railway=station`, node 8746050618, -10,70491/22,22639, aan de EN230/EN250). https://www.openstreetmap.org
[11] `v2/data/stroomroute-koper-lobito-duisburg.json` — bron van de gekopieerde benen (been 2 "trein Kamoa-Kakula → Lobito", 1.689,4 km / 3.469 punten; been 3 "haven-aanloop Lobito", 8,6 km, stippel) en van de hergebruikte ankers Kamoa-railhead en Lobito-kade.
[12] Esri World Imagery via `v2/tools/sat_check.py` (z15/z17, live) — `v2/build-cache/satcheck/sat-kobalt-kolwezi-lobito-kolwezi-station.png`, `sat-kobalt-kolwezi-lobito-kolwezi-station-close.png`.

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `kobalt-kolwezi-lobito`** → `v2/data/stroomroute-kobalt-kolwezi-lobito.json` — 3 benen, **1.727,7 km**, 3.573 punten, 5 markers. spoor 29,7 + 1.689,4 = 1.719,1 km · zee 8,6 km (stippel).
Recept: `bak_stromen.sh` (functie `bak_kobalt_kolwezi_lobito`).

**b1 (spoor, nieuwe scan):** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=-10.71495,25.48365 --naar=-10.6627,25.2873 --naam=kobalt-kolwezi-lobito-kolwezi-railhead --hoofd-km=100`, op het 1-op-1-net ("3260717 spoor-edges" bevestigd in de consoleregel). Snap 0,06 km (Kolwezi) / 0,42 km (Kamoa-railhead), beide op hetzelfde hoofdnet-component (47.640 km — een klein geïsoleerd spoornet, vandaar `--hoofd-km=100` in plaats van de default 1.000). Resultaat **29,7 km over 36 edges tegen 22,2 km hemelsbreed (verhouding 1,32)**. Geen gepubliceerde km beschikbaar (brief: "geen (hemelsbreed ~22 km)"), dus geen ±15%-toets mogelijk op dit been zelf — wel plausibel voor een kort emplacement-tot-emplacement-stuk. Eén knik ≥60° (156,6°, boogstraal ~23 m, bij -10.71590,25.48530) vlak bij het beginpunt: `toets_knikken.py` classificeert hem als "scherpe bocht, echt" (pad/hemelsbreed-verhouding 1,3, géén terugloop) — dit is kopmaken op het spoorstation-emplacement, geen routeerfout.

**b2 (spoor, letterlijke kopie):** exact `v2/build-cache/ais/graaf/spoorroute-kamoa-lobito.geojson` uit `bak_koper_lobito` (koper-lobito-duisburg) — geen nieuwe scan. **1.689,4 km, 3.469 punten**, ongewijzigd. Naad b1→b2 **0,417 km** (kop b2 op -10,66270/25,28730 tegen staart b1 op -10,65900/25,28670) — binnen de norm van ≤5 km, een klein procesgat op het Kamoa-railhead-emplacement.

**b3 (zee, letterlijke kopie, stippel):** ⚠️ **afwijking van de bak-aanwijzing gemeten en gecorrigeerd:** de samenvatting van de briefschrijver noemde "kopie stippel-geojson", maar been 3 van `bak_koper_lobito` zelf is een **rechte `--stippel`** (geen geojson-bestand): `-12,34709/13,549 → -12,2702/13,5406`, 8,598 km. Dat is hier letterlijk overgenomen (dezelfde twee coördinaten), in plaats van een niet-bestaand geojson-pad te verzinnen — de werkregel "letterlijke kopie van het geojson/de --been-regel van de moederstroom" (bakhandleiding §2) geldt ook als die regel zelf een `--stippel` is. Naad b2→b3 **0,229 km** (staart b2 op -12,34890/13,54800 tegen kop b3 op -12,34709/13,549).

**Geen b4 (zee naar een bestemmingshaven):** conform de brief (§6/§7) noemt geen bron de bestemming van het kobalt na Lobito — geen lijn getekend, de keten stopt bij de haven-nadering.

**Toets:** km-som **1.727,7 km tegen LAR ~1.739 km voor de hele as = −0,6%**, ruim binnen ±15%. Naden b1→b2 **0,417 km** en b2→b3 **0,229 km**, beide < 5 km (geen publicatie om been 2/3 apart tegen te toetsen, dus gold alleen de "geen naad > 5 km"-eis, precies zoals de bak-aanwijzing al zei). `toets_knikken.py`: **1 knik ≥60°, 0 terugloop** (de kopmaak-bocht van b1; b2 heeft 0 knikken/0 omkeringen). `toets_rechte_benen.py --min-km 5`: **b3 (8,6 km, omwegfactor 1,000) wordt terecht als stippel gevonden** — precies wat de norm eist, geen ongeteste rechte lijn. json geldig: versie 2, punt_formaat lonlat, modaliteiten uitsluitend {spoor, zee}, elk been ≥2 punten, bestandsgrootte 66,8 KB (< 300 KB). Alle 5 markers liggen op hun been of het gekopieerde ankerpunt van de stippel.

**Gereedschapslessen:**
- `BAKE_SUFFIX=-raw` is op een klein geïsoleerd spoornet (hier component 47.640 km, niet het hoofdnet van 1.144.150 km) niet genoeg op zichzelf: zonder `--hoofd-km=100` had de hoofdnet-eis (default 1.000 km) het punt naar een ver, verkeerd net kunnen laten terugvallen.
- Een "gedeeld been met een bestaande stroom" is niet altijd een geojson-bestand — soms is de moederregel zelf al een rechte `--stippel`. Kopieer dan de `--stippel`-coördinaten, niet een fictief geojson-pad dat de briefsamenvatting suggereert maar dat op schijf niet bestaat.
- Eén scherpe bocht vlak bij een emplacement-beginpunt is meestal kopmaken, geen routeerfout — de pad/hemelsbreed-verhouding van `toets_knikken.py` (hier 1,3) onderscheidt dat betrouwbaar van een echte terugloop (die zou dicht bij 1 of ver boven 3 liggen, zie de handleiding).
