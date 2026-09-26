# Routebrief (licht) · kobalt — Kolwezi (KCC) → Durban → Kokkola (Finland)

**stroom-id:** `kobalt-kcc-kokkola` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** kobalthydroxide van Glencore's Kamoto Copper Company (KCC, Luilu-plant, Kolwezi) per **truck** over de zuidelijke Copperbelt-uitweg (identiek tracé aan `koper-tfm-durban` vanaf Likasi) naar de containerkade Durban DCT Pier 2, per **zeeschip** om de Kaap naar de Botnische Golf, naar de Umicore-raffinaderij op Kokkola Industrial Park (KIP) — Europa's enige grote kobaltraffinaderij buiten China — waar op hetzelfde terrein ook precursor voor kathodemateriaal wordt gemaakt.
**Welke as van het verhaal:** *Europa's enige schakel.* Glencore won in 2025 eigen **36,1 kt kobalt** (KCC + Mutanda, −5%; Q1 2026 −39% door het DRC-quotum) [1]. Umicore en Glencore hebben sinds 2019 een langlopende, revolverende hydroxide-overeenkomst die levert "to Umicore's cobalt refineries globally, including Kokkola" [2]; Kokkola raffineert ~15 kt Co/j [4]. Het Kokkola-aandeel van Glencore's 36,1 kt en de exacte Afrikaanse laadhaven zijn niet gepubliceerd — Durban is de branche-default (Fastmarkets: hydroxide "is usually sent by trucks to the … port of Durban") [5]; in de beennaam als "aannemelijk" gemarkeerd.

## 1 · Ketenkaart
```
KCC Luilu-plant `co-kcc-luilu` ──(b1 truck · RN39 Kolwezi→Likasi + koper-tfm-durban-tracé · ~3.100 km)──►
Durban DCT Pier 2 `cu-durban-kade` ──(b2 zee · om de Kaap · Skagerrak · Oostzee · ~14.500 km, laadhaven aannemelijk)──►
Port of Kokkola `co-kokkola-kade` ═══ knoop: Umicore-raffinaderij `co-kip-umicore` (kobaltmetaal/sulfaat/tetroxide)
  └─ knoop, zelfde terrein (fase D, één bron): Umicore-precursorlijn voor kathodemateriaal ⏹ stoppunt
(vertakking, niet getekend: Mutanda -10.7950,25.8015, tweede Glencore-mijn in dezelfde Copperbelt-poort)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `co-kcc-luilu` → `cu-durban-kade` | RN39 Kolwezi→Likasi, dan **identiek** aan `koper-tfm-durban` b1: RN1 → Kasumbalesa → T3/T2 → Chirundu → A1/A4 → Beitbridge → N1/N3 | ~3.100 (400 Kolwezi–Kasumbalesa [7] + rest = koper-tfm-durban b1, 2.982 km gebakken) | nieuw profiel `kobalt-kcc-durban`: kop `co-kcc-luilu`, dezelfde 12 via-punten als `koper-tfm-durban` §4 (niet letterlijk hetzelfde bestand — ander beginpunt), staart `cu-durban-kade`; extracts congo-drc/zambia/zimbabwe/zuid-afrika | nee |
| b2 | B | zee | `cu-durban-kade` → `co-kokkola-kade` | Kaap de Goede Hoop → Atlantische Oceaan → Kanaal → Skagerrak → Kattegat/Deense Straten → Oostzee → Botnische Golf (Kvarken) | ~14.500 (MARNET, Durban-zeeknoop 5202 → Kokkola-zeeknoop 8821, 64.0369,22.7535) | MARNET; kop = letterlijke kopie van `aanloop-durban.geojson` (17,8 km, uit `koper-kolwezi-durban`); staart = nieuwe haven-aanloop (Kokkola-zeeknoop ligt ~23–25 km weg, buiten `--max-snap 25`) | aanloop ja (beide kanten), hoofdboog nee |
| — | C | — | (vervalt) | `co-kokkola-kade` → `co-kip-umicore` ligt < 3 km (havenweg) | ~1,3 | geen eigen been (lichte werkwijze); `co-kip-umicore` blijft marker | n.v.t. (< 2 km → geen stippel nodig) |
| — | D | — | Umicore-raffinaderij → Umicore-precursorlijn | zelfde KIP-terrein | < 1 | geen been, alleen genoemd in §5 (één bron: Umicore "cobalt refinery and cathode precursor operations in Finland" [3]) | n.v.t. |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-kcc-luilu` | mijn / laadplek (kop) | KCC (Glencore 75%) Luilu hydrometallurgische plant, Kolwezi | -10.7205, 25.3620 | [1][8][9] — gecorrigeerd t.o.v. de eerdere geohack -10.7148,25.3855 (identiek aan de M25-corridorkop, 2,6 km ernaast) | **bron-gelegd** (z16 gezien: tankhouse-hallen, thickeners, tankparken en turquoise leach-/opslagvijvers op één industrieel complex; kruis ligt tussen de procesgebouwen, niet meer op kale mijngrond) |
| `cu-durban-kade` | overslag truck → container → zeeschip | Durban Container Terminal Pier 2 (Bayhead) — **hergebruikt anker** | -29.8790, 31.0160 | `koper-kolwezi-durban` §3 | bron-gelegd (elders al gelegd, hier hergebruikt) |
| `co-kokkola-kade` | overslag zee → land (Deep Port / Silverstone) | Kokkolan syväsatama (Deep Port), Port of Kokkola | 63.8645, 23.0270 | [10] OSM `landuse=industrial "Kokkolan syväsatama"` (centroïde 63.86598,23.02857) + satelliet | **bron-gelegd** (z16 gezien: pier met kranen, bulklading in hopen, vaartuig(en) aan de kade — de werkkant van de Deep Port) |
| `co-kip-umicore` | verwerkingsknoop (marker) | Umicore Finland Oy, Kokkola Industrial Park (heavy-industry-zone "Suurteollisuusalue") | 63.8580, 23.0490 | [3][4][8] — geen bron geeft een straatadres of plot-nummer; OSM kent binnen KIP wel `Boliden Kokkola` (63.8631,23.0540) maar geen `Umicore`-object [10] | **onzeker** (z14/z16 gezien: tankfarm en procesgebouwen tussen de Boliden-zinkfabriek en de kade, kenmerkend voor een chemisch/metallurgisch bedrijf — welk perceel precies Umicore is, is op dit beeld niet van de buren te onderscheiden) |

Vertakking (niet getekend): Mutanda Mining (Glencore), -10.7950, 25.8015 [1][8] — tweede Copperbelt-kobaltmijn van Glencore, deelt dezelfde Kasumbalesa-poort als KCC; geen eigen volumecijfer richting Kokkola gevonden.

## 4 · Via-punten (b1 — identiek aan `koper-tfm-durban` §4 vanaf Likasi)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 0 | RN39, ZO van Kolwezi | -10.86, 25.53 | pint de RN39-corridor naar Likasi (nieuw stuk, niet in de copper-brief) |
| b1 | 1–12 | Likasi … Buccleuch | — | letterlijk de 12 punten uit `koper-kolwezi-durban.md` §4 (Likasi, Lubumbashi, **Kasumbalesa**, Ndola, Kabwe, Lusaka, **Chirundu**, Harare, Masvingo, **Beitbridge**, Polokwane, Buccleuch) — niet herhaald, zie dat bestand |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| KCC Luilu-plant, Kolwezi | Glencore (75%) | erts/tussenproduct → kobalthydroxide (+ koperkathode) | Glencore eigen kobalt (KCC+Mutanda) 36,1 kt Co in hydroxide, 2025 (−5%) | [1] |
| Umicore-raffinaderij, KIP Kokkola | Umicore | hydroxide → kobaltmetaal/-sulfaat/-tetroxide | 15 kt Co/j nameplate (Jervois-toll-recht 6.250 t tot 2093; Jervois zelf in herstructurering 2025) | [4] |
| Umicore-precursorlijn, zelfde terrein (fase D, knoop) | Umicore | raffinaat → kathodeprecursor | niet gekwantificeerd; één bron noemt de lijn | [3][6] |

## 6 · Stoppunt
De brief stopt op het Umicore-terrein in Kokkola: de raffinaderij én de precursorlijn liggen op hetzelfde KIP-perceel (fase D = een knoop, geen been), en geen bron noemt een klantfabriek voor het kathodemateriaal erna — fase E vervalt.

## 7 · Open punten
- **Afrikaanse laadhaven niet gebrond:** Durban vs Dar es Salaam vs (sinds 2025/2026) Lobito per spoor — Durban is de branche-default [5], v1's Lobito→Kokkola-route heeft geen bron en is vervallen.
- **Kokkola-aandeel van Glencore's 36,1 kt niet gepubliceerd** — het jaarvolume van déze specifieke as (KCC→Kokkola) is dus onbekend; de kaart tekent de weg, niet het volume.
- **`co-kip-umicore` is site-niveau, niet perceel-niveau:** Umicore's exacte kavel binnen KIP kon niet van buurbedrijven (Boliden-zink, Kemira, Yara) worden onderscheiden op deze pass; vraagt een niet-satelliet-bron (plotkaart/vergunning) voor een scherpere ankercheck.
- **Kokkola-zeeknoop ligt net buiten `--max-snap 25`** (~23–25 km) → de bak-agent heeft `maak_havenaanloop.py` nodig voor de staart van b2; de 1:10M-kust bij de Botnische scherenkust kan traag/onvolledig zijn (terugval: rechte stippel).
- **RN39 Kolwezi–Likasi mogelijk lage wegklasse in OSM** (zoals de OT-weg bij Oyu Tolgoi) → check `corridorKlassen` bij het bakken.
- Mutanda's aandeel in het Kokkola-volume: geen bron.

## 8 · Bronnen
[1] Glencore, Full Year 2025 Production Report (2026-01-29) — eigen kobalt KCC+Mutanda 36,1 kt (−5%), Q1 2026 −39%. https://www.glencore.com/media-and-insights/news/full-year-2025-production-report
[2] Umicore, "Umicore and Glencore develop partnership for sustainable cobalt supply in battery materials" — langlopende hydroxide-overeenkomst sinds 2019, levering "to Umicore's cobalt refineries globally, including Kokkola". https://www.umicore.com/en/media/newsroom/umicore-and-glencore-develop-partnership-for-sustainable-cobalt-supply-in-battery-materials/
[3] Umicore, "Umicore to acquire cobalt refinery and cathode precursor operations in Finland" — raffinage + precursor op één terrein. https://www.umicore.com/en/media/newsroom/umicore-to-acquire-cobalt-refinery-and-cathode-precursor-operations-in-finland/
[4] WoodMac, "Metals — Umicore Kokkola Cobalt Refinery" — 15 kt/j nameplate. https://www.woodmac.com/reports/metals-umicore-kokkola-cobalt-refinery-150024099/
[5] Fastmarkets, "DRC logistical issues remain in focus for cobalt supply chain" (2026-04-01) — hydroxide "usually sent by trucks to the South African port of Durban, where it gets sent into China". https://www.fastmarkets.com/insights/drc-logistical-issues-remain-cobalt-supply-chain/
[6] Umicore Finland, site-/sustainability-pagina — raffinage + kathodeprecursor op het Kokkola-terrein, in bedrijf 2026. https://www.umicore.fi/en/our-sites/
[7] Fastmarkets, "African copper, cobalt logistics chain under pressure as truckers avoid DRC" — 400 km Kolwezi–Kasumbalesa. https://www.fastmarkets.com/insights/african-copper-cobalt-logistics-chain-under-pressure-as-truckers-avoid-drc/
[8] Ontwerp + haalbaarheidstoets `kobalt-kcc-kokkola.json` (interne invoer, 2026-09-26) — MARNET-zeeknoopafstanden, KCC-anker-correctie, sea-knoop-ids 5202/8821, DRC-quotumcijfers.
[9] `v2/design/routebrieven/koper-kolwezi-durban.md` — hergebruikte via-punten (§4) en anker `cu-durban-kade` (§3).
[10] OpenStreetMap via Nominatim (ODbL), bevraagd 2026-09-26 — "Kokkolan syväsatama" (63.86598,23.02857, industrial), "Boliden Kokkola" (63.8631,23.0540, man_made=works), "Suurteollisuusalue" (63.85949,23.05285, industrial). https://www.openstreetmap.org
[11] Ecofin Agency, "Cobalt prices steady as DRC's new export quota circular brings clarity" — quotum 96.600 t/j 2026–2027, CMOC ~31,2 kt. https://www.ecofinagency.com/news-industry/0512-51143-cobalt-prices-steady-as-drc-s-new-export-quota-circular-brings-clarity-to-the-market
[12] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16) — `sat-kobalt-kcc-kokkola-kcc-luilu.png`, `sat-kobalt-kcc-kokkola-luilu-detail.png`, `sat-kobalt-kcc-kokkola-kip.png`, `sat-kobalt-kcc-kokkola-syvasatama.png`, `sat-kobalt-kcc-kokkola-kade-detail2.png`.

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `kobalt-kcc-kokkola`** → `v2/data/stroomroute-kobalt-kcc-kokkola.json` — 4 benen, **18.458,9 km**, 30.236 punten, 4 markers. truck 3.044,8 · zee (stippel) 17,8 · zee 15.370,9 · zee (stippel) 25,4 km.
Recept: `bak_stromen.sh` (functie `bak_kobalt_kcc_kokkola`).

**b1 (truck, nieuw profiel `kobalt-kcc-durban`):** `maak_stroombeen_weg.py --profiel kobalt-kcc-durban --bron geofabrik` — kop `co-kcc-luilu` (-10,7205/25,3620) → nieuw RN39-punt ZO van Kolwezi (nieuw stuk, niet in koper-tfm-durban) → dezelfde 12 via-punten als `koper-tfm-durban` §4 vanaf Likasi (Likasi/Lubumbashi/Kasumbalesa/Ndola/Kabwe/Lusaka/Chirundu/Harare/Masvingo/Beitbridge/Polokwane/Buccleuch) → staart `cu-durban-kade` (-29,8790/31,0160). Extracts congo-drc/zambia/zimbabwe/zuid-afrika (324.519 km ruw, 806.294 unieke ways, 188 s). ⚠️ Het nieuwe via-punt "RN39 ZO van Kolwezi" snapte in de eerste run **8,05 km** (boven de 5 km-drempel) — precies de door de brief voorspelde lage OSM-wegklasse (Oyu Tolgoi-precedent, §7); met `corridorKlassen: ["tertiary"]` toegevoegd snapt het op **3,65 km** en zakt de lengtetoets van −0,7% naar **−1,8%**, nog ruim binnen ±15%. Gemeten: **3.044,8 km / 28.625 punten**, tegen de brief-schatting "~3.100 (400 Kolwezi–Kasumbalesa + rest = koper-tfm-durban b1, 2.982 km gebakken)" = **−1,8%**, binnen ±15%. Alle via-snaps ≤3,65 km. Anker-verbindingen (buiten de lengtetoets): plant→weg 0,31 km, weg→kade 0,09 km.

**b2a (zee, haven-aanloop, letterlijke kopie, stippel):** exact `v2/build-cache/ais/graaf/aanloop-durban.geojson` (17,8 km, 6 punten) uit `bak_koper_durban`/`koper-kolwezi-durban` — geen nieuwe scan, byte-identiek hergebruikt. Snap van de Durban-kade naar de dichtstbijzijnde MARNET-zeeknoop was al bekend op 16,708 km. Naad b1→b2a **0,00 km**.

**b2b (zee, hoofdboog, nieuw, MARNET):** `--been "zee|zeeschip Durban DCT Pier 2 → Port of Kokkola …|-29.8790,31.0160|63.8645,23.0270"` — snap Durban-kade 16,708 km (op de reeds bekende zeeknoop 5202-buurt), snap Kokkola-kade **23,363 km** (zeeknoop 8821, 64,0369/22,7535 — precies de ~23–25 km uit de brief). 108 MARNET-edges, **15.370,9 km / 1.591 punten** (lengte-invariant: getekende lijn 15.370,945 vs. som edge-km 15.371,400 = −0,455 km naad binnen het been). Tegen de brief-schatting "~14.500 (MARNET, Durban-zeeknoop 5202 → Kokkola-zeeknoop 8821)" is dit **+6,0%**, binnen ±15% — de om-de-Kaap-route via Skagerrak/Kattegat/Oostzee/Botnische Golf ligt iets langer dan de brief-indicatie. Naad b2a→b2b **0,04 km**.

**b2c (zee, haven-aanloop, nieuw, stippel):** `timeout 300 python v2/tools/maak_havenaanloop.py --naam kobalt-kcc-kokkola-kokkola --van 64.0369,22.7535 --naar 63.8645,23.0270 --uit …` — pad gevonden op de **eerste trap** (cel 0,02° gebufferd, minste land midden op de lijn): **25,4 km, 14 punten**, 0,00 km over land (exit 0, geen tweede poging nodig). ⚠️ **Richting is bewust omgedraaid t.o.v. de eerste run**: de eerste poging (`--van kade --naar zeeknoop`) gaf een geojson in de verkeerde reisrichting — de reisvolgorde is Durban→hoofdboog(eindigt op de zeeknoop)→aanloop(zeeknoop→kade), dus het bestand moest van zeeknoop náár kade lopen. De eerste run gaf daardoor een naad van 23,36 km (= de hele aanloopafstand, want leg 3 en leg 4 begonnen allebei bij de kade); na het herdraaien met omgekeerde `--van`/`--naar` is de naad **0,00 km**. Tegen de brief-schatting "~23–25 km, buiten --max-snap 25" klopt de gemeten 25,4 km. Naad b2b→b2c **0,00 km**.

**Fase C (geen been, lichte werkwijze):** conform brief en bak-aanwijzing — `co-kokkola-kade` → `co-kip-umicore` (<3 km havenweg) krijgt geen eigen been, alleen de marker `Umicore Finland Oy, Kokkola Industrial Park` (63,858/23,049). Marker ligt 1,298 km van de getekende lijn — verwacht (anker ≠ routeerpunt, geen been getekend naar dit punt).

**Fase D (niet gebakken):** conform brief §5/§6 — Umicore-raffinaderij → Umicore-precursorlijn (zelfde KIP-terrein) is niet getekend, alleen genoemd (één bron: [3]).

**Toets:** km-som **18.458,9 km**. Elk gemeten been binnen ±15% (b1 −1,8%, b2b +6,0%). Naden **0,00 / 0,04 / 0,00 km**, ruim onder de norm van 5 km. `toets_knikken.py`: **69 knikken ≥60°, 1 omkering (76,9° op de MARNET-zeeboog bij Skagerrak, 55,3056/12,6825), 0 TERUGLOOP** — alle overige knikken zijn korte OSM-spikes/krappe bochten op het truck-been (Kolwezi/Durban-omgeving), niets dat gerepareerd hoeft te worden. `toets_rechte_benen.py --min-km 5`: **geen enkel been van deze stroom in de uitslag** — beide haven-aanloop-stippels zijn via een water-pad/`detour()` gerouteerd (omwegfactor 1,085/1,086), geen ongeteste rechte lijn boven 5 km. json geldig: versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, zee}, elk been ≥2 punten. Bestandsgrootte **610,4 KB** — boven de ~300 KB-richtnorm uit de handleiding, maar identiek van orde aan het bestaande `koper-tfm-durban` (609,7 KB): het truck-been erft de fijnkorrelige 1-op-1-OSM-geometrie van de wegscan (28.625 punten over 3.045 km), geen artefact van deze bake. Markers: Luilu/Durban/Kokkola-kade alle **0,000 km** van de lijn; Umicore-KIP **1,298 km** (bewust, geen been naar dit punt).

**Gereedschapslessen:**
- Een nieuw via-punt op een corridor die de brief al als "mogelijk lage OSM-wegklasse" aanmerkt (RN39 Kolwezi–Likasi, Oyu Tolgoi-precedent) snapt inderdaad >5 km zonder `corridorKlassen`; met `["tertiary"]` erbij komt de snap ruim binnen de norm zonder de lengtetoets uit de tolerantie te duwen.
- Een `maak_havenaanloop.py`-run moet in de **reisvolgorde** lopen, niet in de volgorde waarin `--van`/`--naar` het handigst uitkomt: als de voorgaande zee-boog al op de zeeknoop eindigt, hoort de aanloop van zeeknoop náár kade te gaan (niet andersom), anders meet de naad-toets de hele aanloopafstand als gat. Zichtbaar aan een naad die exact gelijk is aan de lengte van het aanlopende been zelf.
- Een gedeeld been (hier: de Durban-kop-aanloop) hergebruiken als exact dezelfde `$BEEN/aanloop-durban.geojson` bevestigt de eerder gemeten 17,8 km en 16,708 km-snap zonder nieuwe scan — precies het `bak_koper_durban`-precedent.
