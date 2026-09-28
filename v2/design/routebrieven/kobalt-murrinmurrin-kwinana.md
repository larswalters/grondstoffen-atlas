# Routebrief (licht) · kobalt — Murrin Murrin (Australië) → Kwinana → Tongxiang (China)

**stroom-id:** `kobalt-murrinmurrin-kwinana` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 4) · **status:** gebakken
**Keten in één zin:** LME-grade nikkel/kobalt-briketten van Glencore's Murrin Murrin HPAL-plant (Laverton Shire, WA) gaan per **truck** naar het spoorhoofd Leonora, per **spoor** via Kalgoorlie naar het bulkprecinct Kwinana, per **zeeschip** (via Lombok/Makassar/Zuid-Chinese Zee, v1-patroon) naar de containerkade Ningbo Beilun, en per **truck** — letterlijke kopie van `kobalt-huayou-gunsan` been 1 — naar de Huayou-raffinaderij in Tongxiang (Zhejiang), waar metaal tot batterijchemicaliën (kobalttetroxide/-sulfaat) wordt verwerkt.
**Welke as van het verhaal:** de enige noemenswaardige Australische kobaltproductie (reserve-as, golf 4) — ~2,2 kt Co/jaar in 2025 (2,1–3,0 kt/jaar 2021–2025) [3], tegenover ~1 kt/jaar in de v1-checklist. Murrin Murrin is **anders dan de DRC-ketens**: het erts wordt volledig ter plekke geraffineerd tot verkoopklaar LME-metaal (geen ruw hydroxide-export) [5] — de Chinese schakel is hier dus conversie tot batterijchemicaliën, niet primaire raffinage.

## 1 · Ketenkaart
```
Murrin Murrin-plant `co-murrinmurrin-plant` ──(b1 truck · toegangsweg → Goldfields Highway · hemelsbreed ~56 km)──►
  Leonora-spoorhoofd `co-leonora-spoorhoofd`
  ──(b2 spoor · Kalgoorlie–Leonora-lijn via Malcolm/Menzies · 259 km, gepubliceerd)──►
  Kalgoorlie (via-punt, spoorknoop)
  ──(b3 spoor · Eastern Goldfields Railway via Broad Arrow/Southern Cross/Merredin/Northam · ~642 km, webcheck)──►
Kwinana-kade `co-kwinana-kade`
  ──(b4 zee-aanloop · ~20,9 km, stippel — LAR-586, kade > 5 km van zeeknoop)──► zeeknoop 8982
  ──(b5 zee · Indische Oceaan → Lombok/Makassar → Zuid-Chinese Zee → Oost-Chinese Zee · ~7.300 km, indicatief)──►
Ningbo Beilun-kade `co-ningbo-kade` (hergebruikt anker)
  ──(b6 truck · G60/G92 Tongxiang–Ningbo · 192,2 km — letterlijke kopie van kobalt-huayou-gunsan been b1)──►
Huayou Tongxiang-raffinaderij `co-tongxiang-raffinaderij` (hergebruikt anker) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `co-murrinmurrin-plant` → `co-leonora-spoorhoofd` | eigen toegangsweg → Goldfields Highway | hemelsbreed ~56 km, geen wegkm [1][10] | maak_stroombeen_weg (extract `australie`) | nee |
| b2 | A | spoor | `co-leonora-spoorhoofd` → Kalgoorlie (via-punt) | Kalgoorlie–Leonora-lijn (standaardspoor, via Malcolm/Menzies) | 259 [gepubliceerd, Wikipedia "Leonora railway line" [8]] | toets_spoorroute (`BAKE_SUFFIX=-raw`) | nee |
| b3 | A | spoor | Kalgoorlie (via-punt) → `co-kwinana-kade` | Eastern Goldfields Railway (via Broad Arrow/Southern Cross/Merredin/Northam) | ~642 [webcheck; som gepubliceerde deeltrajecten Northam–Kalgoorlie 505,4 km [9] + indicatief Perth–Northam ~97 km + Kwinana-industriespoor ~40 km] | toets_spoorroute (meerdere runs via de via-punten) | nee |
| b4 | B | zee (haven-aanloop) | `co-kwinana-kade` → zeeknoop 8982 | Kwinana bulkprecinct → open water Cockburn Sound | 20,9 [haalbaarheidstoets: `hecht_marnet.marnet_zee`, gemeten] | `maak_havenaanloop.py` (timeout 300; bij "geen pad" terugval rechte stippel) | ja — LAR-586: kade > 5 km van de zeeknoop |
| b5 | B | zee | zeeknoop 8982 → `co-ningbo-kade` | Indische Oceaan → Lombok/Makassar-straat → Zuid-Chinese Zee → Oost-Chinese Zee (v1-patroon `co-murrin→co-ref-huayou` [zie brontabel]) | ~7.300 [indicatief; hemelsbreed 6.925 km deze sessie gemeten; exacte MARNET-km bij bakken] | MARNET `--been "zee\|…\|-32.0565,115.7160\|29.9353,121.8695"` (Ningbo snapt <5 km, geen aparte aanloop nodig) | nee |
| b6 | C | truck | `co-ningbo-kade` → `co-tongxiang-raffinaderij` | G60/G92 Tongxiang–Ningbo (Hangzhou-ringweg-corridor) | 192,2 — **letterlijke kopie** van `kobalt-huayou-gunsan` been b1 (profiel `kobalt-huayou-gunsan-tongxiang-ningbo`) | `stroombeen-weg-kobalt-huayou-gunsan-tongxiang-ningbo.geojson` hergebruiken, geen nieuwe scan | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-murrinmurrin-plant` | mijn/raffinaderij (kop van b1) | Murrin Murrin HPAL nikkel-kobaltplant (Glencore), Laverton Shire | -28.7680, 121.8940 | [1][4][10] | bron-gelegd (z16/z17 gezien: autoclaaf-/tankenpark met schoorstenen, procesgebouwen, opslagtanks en tailings-vijvers — `sat-kobalt-murrinmurrin-kwinana-plant2.png`) |
| `co-leonora-spoorhoofd` | overslag truck → spoor | Leonora (railhead van de Kalgoorlie–Leonora-lijn) | -28.8845, 121.3308 | [8][10] | aannemelijk (z16 gezien: regionale kern Leonora bevestigd — `sat-kobalt-murrinmurrin-kwinana-leonora2.png`; specifieke spoorbundel niet apart te onderscheiden op dit beeld) |
| `co-kwinana-kade` | overslag spoor → zee | Kwinana Bulk Jetty (Fremantle Ports), Kwinana Beach | -32.2414, 115.7576 | [6][7][10] | bron-gelegd (z16 gezien: pier met transportband/pijpleiding het water in, tankenpark/industrieterrein erachter — `sat-kobalt-murrinmurrin-kwinana-jetty.png`) |
| `co-ningbo-kade` | overslag zee → truck (hergebruikt) | Beilun Container Terminal Phase 2, Ningbo-Zhoushan | 29.9353, 121.8695 | `kobalt-tfm-quzhou.md`/`kobalt-huayou-gunsan.md` §3 [12] | bron-gelegd (hergebruikt anker, niet opnieuw satelliet-gecheckt) |
| `co-tongxiang-raffinaderij` | raffinaderij / losplek (hergebruikt) | Zhejiang Huayou Cobalt — nikkel-kobaltsmelterij, Tongxiang Economic Development Zone | 30.6167, 120.5629 | `kobalt-huayou-gunsan.md` §3 [11] | bron-gelegd (hergebruikt anker — MEE-emissieregister, decimaal én DMS exact overeenkomend) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Malcolm (junctie ex-Laverton-tak) | -28.9365, 121.5140 | pint de lijn op de doorgaande Leonora-tak i.p.v. de gesloten Malcolm–Laverton-aftakking (1960 gesloten) [8] |
| b2 | 2 | Menzies | -29.6936, 121.0289 | enige tussenstation op de 259 km-lijn, voorkomt een vrije-Dijkstra-omweg rond de Menzies-railwaygroep |
| b3 | 1 | Broad Arrow | -30.4484, 121.3297 | pint de uitgang van Kalgoorlie op de Eastern Goldfields Railway i.p.v. een lokaal rangeerspoor |
| b3 | 2 | Southern Cross | -31.2306, 119.3278 | vast punt op het gepubliceerde deeltraject Northam–Kalgoorlie [9] |
| b3 | 3 | Merredin | -31.4820, 118.2790 | tussenstad op de doorgaande hoofdlijn, voorkomt een sluipweg via een zijtak |
| b3 | 4 | Northam | -31.6531, 116.6661 | splitsingspunt waar de Perth–Kalgoorlie-lijn de Avon-vallei in duikt [9] |
Been b1 (plant → Leonora): geen via-punten — enige toegangsweg, geen corridorkeuze gevonden. Been b6 is een letterlijke kopie (eigen via-punten al vastgelegd in `kobalt-huayou-gunsan.md` §4).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Murrin Murrin HPAL-plant | Glencore (Minara Resources) | lateriet-erts → LME-grade nikkel- én kobaltbriketten (HPAL + waterstofreductie, ter plekke) | Co 2,2 kt/j (2025), Ni 32 kt/j (2025) [3] | [1][3][4][5] |
| Huayou Tongxiang-raffinaderij | Zhejiang Huayou Cobalt | nikkel-/kobaltmetaal → kobalttetroxide/-sulfaat (batterijchemicaliën) | vergunning 913300007368873961001P, geen productiecijfer gebrond | `kobalt-huayou-gunsan.md` §5 [11] |

## 6 · Stoppunt
De brief stopt bij de Huayou Tongxiang-raffinaderij: dit is een bron-gelegd, herbruikt anker (in tegenstelling tot het onopgeloste Quzhou-eindpunt van `kobalt-tfm-quzhou`) en fase D is hiermee bereikt. Geen bron noemt een specifieke vervolgafnemer (batterijfabrikant) voor juist déze Australische aanvoerstroom — fase E vervalt.

## 7 · Open punten
- **Rol van de Kwinana-kade niet eenduidig gebrond:** de enige gevonden primaire bron (WA-overheid, 1998) beschrijft de bulkjetty vooral als **importfaciliteit voor zwavel** t.b.v. het HPAL-proces [6]; dat nikkel-/kobaltbriketten er ook worden **geëxporteerd** komt uit secundaire/niet nader gespecificeerde bronnen. Aannemelijk, niet zelf primair bevestigd.
- **Leonora-spoorhoofd niet als aparte spoorbundel satelliet-gezien** — alleen de plaats zelf bevestigd; welk exact laadspoor Glencore gebruikt is niet gevonden.
- **b1-wegkm is hemelsbreed** (~56 km); geen gepubliceerde route-lengte voor de toegangsweg gevonden.
- **b3-spoorkm is een webcheck-optelling** van drie gepubliceerde deeltrajecten (Wikipedia) plus twee schattingen (Perth–Northam, Kwinana-industriespoor) — geen enkele bron geeft de doorgaande Kalgoorlie–Kwinana-afstand.
- **Modaliteit spoor voor het uitgaande product niet apart gebrond:** de Kalgoorlie–Leonora-lijn wordt volgens Wikipedia vooral gebruikt voor **inkomend** zwavel/ammoniak t.b.v. de regionale nikkelindustrie, niet expliciet voor uitgaande Murrin Murrin-briketten [8] — dezelfde onzekerheid als bij de Kwinana-kade.
- **Zeeroute-lengte** (~7.300 km) is een hemelsbreed-indicatie; exacte MARNET-km volgt bij het bakken.
- **Aandeel van deze route in Murrin Murrin's totale kobaltproductie** niet gebrond — v1 (`data/cobalt.js`) modelleert 100 % naar Huayou (enige kobaltstroom, share 1), maar geen bron bevestigt dat al het metaal specifiek naar Tongxiang gaat i.p.v. andere LME-afnemers.

## 8 · Bronnen
[1] Wikipedia, "Murrin Murrin Mine" — locatie 45 km oost van Leonora, Glencore-eigendom, coördinaat -28.7675/121.89389. https://en.wikipedia.org/wiki/Murrin_Murrin_Mine
[2] Wikipedia, "Nickel mining in Western Australia" — 2023: 2.100 t kobalt bij Murrin Murrin. https://en.wikipedia.org/wiki/Nickel_mining_in_Western_Australia
[3] miningdataonline.com, "Murrin Murrin Mine" — productietabel Co 2021–2025 (2,5/3,0/2,1/2,5/2,2 kt) en Ni 2021–2025 (30/36/31/34/32 kt). https://miningdataonline.com/property/429/Murrin-Murrin-Mine.aspx
[4] Glencore Australia, "The Murrin Murrin Operations". https://www.glencore.com.au/operations-and-projects/minara/who-we-are/murrin-murrin
[5] Glencore Australia, "Producing nickel and cobalt at Murrin Murrin" — HPAL-autoclaven, waterstofreductie tot LME-grade briketten ter plekke. https://www.glencore.com.au/operations-and-projects/minara/who-we-are/producing-nickel-and-cobalt-at-murrin-murrin
[6] Western Australian Government, media statement "New bulk cargo jetty at Kwinana to service nickel project at Murrin Murrin" (1998-10-30) — Fremantle Port Authority $7 mln, Brambles $11 mln, 15-jaar contract Anaconda Nickel, primair zwavelimport ~500 kt/j. https://www.wa.gov.au/government/media-statements/Court%20Coalition%20Government/New-bulk-cargo-jetty-at-Kwinana-to-service-nickel-project-at-Murrin-Murrin-19981030
[7] Global Energy Monitor wiki, "Kwinana Bulk Terminal" — Fremantle Ports-eigendom, ~30 km zuid van Fremantle, Kwinana Bulk Berth 2. https://www.gem.wiki/Kwinana_Bulk_Terminal
[8] Wikipedia, "Leonora railway line" — Kalgoorlie–Leonora, 259 km, standaardspoor sinds 1974, verhuurd aan Arc Infrastructure, primair zwavel/ammoniak voor de regionale nikkelindustrie. https://en.wikipedia.org/wiki/Leonora_railway_line
[9] Wikipedia, "Eastern Goldfields Railway" — Northam–Southern Cross 281,9 km, Southern Cross–Boorabbin 97,7 km, Boorabbin–Kalgoorlie 125,8 km; onderdeel van de standaardspoor-verbinding Perth–oostkust. https://en.wikipedia.org/wiki/Eastern_Goldfields_Railway
[10] OpenStreetMap via Nominatim/Photon (ODbL) — "Kwinana Bulk Jetty" (pier, -32.2414/115.7576), "Murrin Murrin Mine" (quarry-centroïde), "Malcolm" (locality), "Kalgoorlie" (railway station), opgevraagd 2026-09-28. https://www.openstreetmap.org
[11] `v2/design/routebrieven/kobalt-huayou-gunsan.md` §3/§5/§8 — hergebruikt anker `co-tongxiang-raffinaderij` (MEE-emissieregister, vergunning 913300007368873961001P).
[12] `v2/design/routebrieven/kobalt-tfm-quzhou.md` §3 — hergebruikt anker `co-ningbo-kade` (Beilun Container Terminal Phase 2, OSM/Nominatim).
[13] Esri World Imagery via `v2/tools/sat_check.py` (z13/z16/z17, live) — `v2/build-cache/satcheck/sat-kobalt-murrinmurrin-kwinana-overview.png`, `-plant.png`, `-plant2.png`, `-leonora.png`, `-leonora2.png`, `-jetty.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 4)

**Benen (in reisvolgorde), km, punten, naad met het vorige been:**

| # | modaliteit | km | punten | naad | been |
|---|---|---|---|---|---|
| 1 | truck | 65,9 | 196 | 0,000 | Murrin Murrin HPAL-plant → Leonora-spoorhoofd |
| 2 | spoor | 261,0 | 271 | 0,499 | Leonora-spoorhoofd → Kalgoorlie (direct) |
| 3 | spoor | 251,8 | 259 | 0,000 | Kalgoorlie → Southern Cross (direct) |
| 4 | spoor | 119,3 | 221 | 0,000 | Southern Cross → Merredin |
| 5 | spoor | 163,7 | 250 | 0,000 | Merredin → Northam |
| 6 | spoor | 158,3 | 520 | 0,000 | Northam → Kwinana-kade |
| 7 | zee (stippel) | 22,5 | 38 | 0,259 | haven-aanloop Kwinana (LAR-586) |
| 8 | zee | 7.271,1 | 751 | 0,000 | zeeschip Kwinana → Ningbo Beilun-kade |
| 9 | truck | 192,2 | 879 | 1,950 | Ningbo Beilun-kade → Huayou Tongxiang-raffinaderij (letterlijke kopie omgekeerd van kobalt-huayou-gunsan b1) |

**Totaal: 8.505,8 km · 3.385 punten · 5 markers.** Alle naden ≤ 5 km (max 1,95 km, de
Ningbo-zeesnap). `toets_knikken.py`: 30 knikken ≥ 60°, waarvan 2 omkeringen ≥ 150°
(spoor-kopmaak bij Kalgoorlie 172,9° en truck-junctie bij Tongxiang 176,3°), **0
terugloop** (de enige categorie die reparatie vraagt). `toets_rechte_benen.py
--min-km 5`: geen treffers. JSON-contract: `versie 2`, `punt_formaat lonlat`, alle
modaliteiten geldig, elk been ≥ 2 punten, bestand 68,2 KB. Markers ≤ 0,1 m van hun lijn.

**Recept:** `bak_kobalt_murrinmurrin_kwinana()` in `v2/tools/bak_stromen.sh`, profielsleutel
`kobalt-murrinmurrin-kwinana-plant-leonora` in `v2/tools/maak_stroombeen_weg.py`.

**Toelichting per stippel/aanloop:**
- **b1 (truck, geen stippel):** `maak_stroombeen_weg.py` vond een doorgaand pad over de
  eigen toegangsweg + Goldfields Highway, 65,9 km tegen de hemelsbrede brief-schatting van
  56,4 km (+16,8%) — de brief geeft zelf "geen wegkm", dus dit is een **indicatie**, geen
  harde ±15%-toets.
- **b2 (spoor, geen stippel):** één directe Dijkstra-run Leonora→Kalgoorlie geeft 261,0 km
  tegen 259 km gepubliceerd (Wikipedia "Leonora railway line", +0,8%) — de brief-via-punten
  Malcolm/Menzies bleken **niet nodig**: de vrije Dijkstra volgde hier al de juiste lijn.
- **b3 (spoor, geen stippel, 4 runs, AFWIJKING VAN DE BRIEF):** Broad Arrow is **niet**
  gebruikt als via-punt. Een Wikipedia-coördinaatcheck bevestigt dat de plaats 38 km
  **noord** van Kalgoorlie ligt, aan de Kalgoorlie–Leonora-weg — dus op de b2-corridor
  (de zijtak naar Leonora), niet op de westwaartse Eastern Goldfields Railway naar Perth.
  Met Broad Arrow als via-punt gaf het eerste deelsegment een sanity-fout (route 34,3 km <
  grootcirkel 35,6 km) en samen met het tweede segment 319,3 km Kalgoorlie→Southern Cross
  tegen 251,3/251,8 km voor de directe run — een echte omweg. Gebruikt: Kalgoorlie →
  Southern Cross (direct) → Merredin → Northam → Kwinana-kade = 693,1 km tegen de
  indicatieve webcheck-schatting ~642 km uit de brief (+8,0%, indicatie, geen harde norm).
- **b4 (zee, STIPPEL — LAR-586):** Kwinana-kade ligt 20,9 km van zeeknoop 8982 (>5 km, dus
  verplicht ondanks <25 km max-snap). `maak_havenaanloop.py` vond een pad over water: 22,5 km,
  38 punten, geen landkruising midden op de lijn.
- **b5 (zee, geen stippel):** MARNET-route zeeknoop 8982 → Ningbo Beilun-kade, 7.271,1 km
  (brief-indicatie ~7.300 km, hemelsbreed 6.925 km); Ningbo snapt op 1,95 km, geen aparte
  aanloop nodig.
- **b6 (truck, LETTERLIJKE KOPIE, omgekeerde richting):** puntenvolgorde omgedraaid t.o.v.
  `kobalt-huayou-gunsan-weg-tongxiang-ningbo.geojson` (stroom kobalt-huayou-gunsan, been b1)
  → `kobalt-murrinmurrin-kwinana-weg-ningbo-tongxiang.geojson`, geen nieuwe wegscan, 192,2 km.

**Lessen:**
- Een gepubliceerde treinlijnlengte (Wikipedia) kan een brief-via-punt overbodig maken: de
  vrije Dijkstra volgt de doorgaande hoofdlijn vaak vanzelf als er geen echte alternatieve
  route bestaat (b2).
- Een brief-via-punt kan zelf op de verkeerde corridor liggen (zijtak i.p.v. doorgaande lijn)
  — een Wikipedia-coördinaatcheck (`en.wikipedia.org/wiki/Broad_Arrow,_Western_Australia`)
  en een korte testrun zonder het via-punt waren hier de goedkoopste manier om dat vast te
  stellen, vóór het via-punt in de definitieve functie terechtkwam (b3).
- Een sanity-fout van de spoorrouter ("route < grootcirkel") is een bruikbaar alarmsignaal
  voor een fout gelegd via-punt, niet alleen een curiositeit.
