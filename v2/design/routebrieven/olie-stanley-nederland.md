# Routebrief (licht) · olie — Stanley (Noord-Dakota) → Patoka (Illinois) → Nederland (Texas, VS)

**stroom-id:** `olie-stanley-nederland` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) ·
**status:** gebakken
**Keten in één zin:** Bakken-schalie-olie per **pijpleiding** over twee aaneengesloten leidingen — de Dakota Access
Pipeline (DAPL: Noord-Dakota → Zuid-Dakota → Iowa → Illinois) tot de Patoka-tankhub en vandaar de Energy Transfer
Crude Oil Pipeline (ETCOP: Illinois → Missouri → Kentucky/Tennessee → Mississippi → Arkansas → Louisiana → Texas) tot de
Energy Transfer-terminal Nederland bij Port Arthur (Golfkust-exporthub). Samen het "Bakken system" [1].
**Welke as van het verhaal:** de **Bakken-trunk naar de Golfkust** — de grootste Noord-Amerikaanse leidingas van
schalie-olie naar de exporthaven; vult naast `olie-hardisty-cushing` (Keystone, Canadese zandolie) en
`olie-corpuschristi-rotterdam` (Permian). Jaarvolume: DAPL ca **540 kb/d** (mei 2026, ca. 4% VS-productie [3]), nameplate
750 kb/d (sinds 2021, ca. 40% van de Bakken-productie [1]); ETCOP 360 kb/d basis, uitbreidbaar tot 570 kb/d [2][7].
Peiljaar 2026. Het aandeel Bakken-olie dat daadwerkelijk Nederland haalt is niet gepubliceerd (§7).

## 1 · Ketenkaart
```
Stanley-terminal `ol-stanley-terminal` (Mountrail County, ND — kop van de DAPL)
  ──(b1 leiding · Dakota Access Pipeline: Stanley–Ramberg–Epping–Trenton–Watford City, dan ZO door ND → SD (Redfield-streek)
      → IA (Cambridge-streek) → IL · ~1.886 km [1])──►
Patoka-tankhub `ol-patoka-hub` (Marion County, IL — DAPL-einde, ETCOP-begin, multi-pijpleiding-hub)
  ──(b2 leiding · Energy Transfer Crude Oil Pipeline: IL → MO → KY/TN → MS → AR → LA (Lake Charles) → TX · ~1.197 km [2])──►
Nederland-terminal `ol-nederland-terminal` (Jefferson County, TX, bij Port Arthur) ── stoppunt (opslag-/exportknoop)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Stanley-terminal → Patoka-hub | Dakota Access Pipeline (OSM-naam "Dakota Access Pipeline", segmenten "Stanley - Ramberg", "…- Trenton - Watford City", "ND L/R 1 - ND L/R 2", "IL L/R 2 - Patoka"; operator DAPL-ETCO Operations Management) | 1.886 (1.172 mi) [1]; OSM-som uit haalbaarheidstoets 1.883,6 (−0,1%) | OSM-pipeline, stikken per way-id (nieuw tool, patroon `maak_leidingbeen_olie_prudhoebay_cherrypoint.py`) | nee |
| b2 | B | leiding | Patoka-hub → Nederland-terminal | Energy Transfer Crude Oil Pipeline / "ETCOP Pipeline" / "ETCOP Line Sunoco" (zelfde operator) | ~1.197 (678 mi omgebouwde Trunkline + 66 mi nieuw = 744 mi) [2]; OSM-som 1.195,3 (−0,2%) | OSM-pipeline, zelfde methode | nee |

Totaal ~3.079 km, 0 stippel verwacht (OSM heeft beide leidingen aaneengesloten; haalbaarheidstoets). Stikken zonder zijtakken:
DAPL-ways zonder "Vernon to Marathon/Plains" en zonder "DAPL Delivery" (operator Bridger Pipeline) — dat zijn afleverstukken, geen trunk.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-stanley-terminal` | kop van de leiding / laadterminal | DAPL-terminal Stanley, Mountrail County ND | 48.3043, -102.4601 | [1][8][9] | bron-gelegd (z15 gezien: omheind terrein met twee lichtgele opslagtanks en een gebouw/pompstation langs een landweg midden in akkerland; kruis op het hek-complex — dit is het OSM-uiteinde van "Dakota Access Pipeline / Stanley - Ramberg") |
| `ol-patoka-hub` | overslag / tankhub (DAPL → ETCOP) | Patoka-tankhub (meerdere operators), ETCOP-begin | 38.7852, -89.0777 | [1][2][4][8][9] | bron-gelegd (z15 gezien: aaneengesloten tankenpark — kolommen ronde tanks met bermen en leidingstraten; kruis op een tank aan de oostrand; dorp Patoka zelf ligt 38.7517/-89.0958 [4] en is geen anker). Het DAPL-eindpunt 38.7666, -89.0417 is een klein afsluiter-/meetterrein 3,7 km ZO; de naad met b2 is 0,09 km (haalbaarheidstoets) |
| `ol-nederland-terminal` | losplek / opslag- en exportknoop (stoppunt) | Energy Transfer-terminal Nederland (Neches-rivier), Port Arthur-regio | 29.9952, -93.9949 | [2][5][6][9] | bron-gelegd (z15 gezien: enorm tankenpark van ca. honderd ronde tanks ten ZW van de Neches met scheepsdokken aan de rivier; kruis op een tankweg aan de westrand — dit is het OSM-einde van "Etcop Transmission Line") |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1, b2 | — | geen | — | een leiding volgt een vaste buis, geen corridorkeuze; geometrie komt uit OSM-ways, niet uit een router. Enige informatieve punt: de naad bij Patoka (zie ankers) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Patoka-hub | meerdere (o.a. DAPL/ETCO-partners) | DAPL (+ andere leidingen) → ETCOP (+ andere afnemers) | hubopslag; DAPL kan er ook anders heen | [1][2] |
| Nederland-terminal | Energy Transfer | ETCOP → opslag → schip/barge/raffinaderijleidingen | ca. 33 mln vaten in 84 tanks, >2 mb/d via 24 leidingaansluitingen, 3 scheepsdokken + 3 bargeberths (fact sheet 2023) | [6] |

## 6 · Stoppunt
De brief stopt bij de Nederland-terminal: dat is een opslag-/exportknoop zonder één vaste afnemer voor déze lading; vanaf
hier verdwijnt de olie in raffinaderijen langs de Golfkust en in de export. Geen bron koppelt Bakken-olie uit deze leiding
aan één raffinaderij of tanker. Fase C/D/E vervallen.

## 7 · Open punten
- **Het Bakken-aandeel dat Nederland haalt is niet gepubliceerd.** De keten is het Bakken-systeem (DAPL + ETCOP, Wikipedia noemt ze als één systeem [1]),
  niet bewezen Bakken-olie in Nederland: Patoka is een hub waar ook andere olie bij- en afstroomt. ETCOP-basiscapaciteit (360 kb/d [7]) ligt onder de DAPL-doorvoer (ca. 540 kb/d [3]) —
  een deel van de DAPL-olie gaat dus elders heen. Zo labelen, niet als 1-op-1-stroom.
- **ETCOP-doorzet niet apart gevonden.** Alleen capaciteiten (450–570 kb/d volgens Wikipedia-oud [2]; 360 → 570 kb/d volgens RBN [7]); geen gemeten doorzet.
- **Haalbaarheidstoets nog niet in OSM-geometrie gebakken.** Eigen scan ND en IL bevestigt de naamgeving en de operator (9 resp. 17 ways); SD, IA, MO, KY, TN, MS, AR, LA, TX niet opnieuw gescand (Overpass onbereikbaar, Texas-pbf traag).
- **Ways staan dubbel in de extracts IL, MO, KY, AR, MS** (grensways): ontdubbelen op way-id; ETCOP-naden tot 2,0 km (Louisiana/Texas) vragen stiktolerantie 3 km (bij 1 km geen pad, haalbaarheidstoets).
- **Nederland-anker is hub-niveau:** welk tankenpark exact de ETCOP-ontvangst is (Energy Transfer-perceel binnen het groter geheel) is op het beeld niet te scheiden; capaciteitscijfers komen uit een zoeksamenvatting van de fact sheet (PDF-tekst niet uitleesbaar).
- Geen cargo-/afnemersniveau voorbij Nederland — bewust (§6).

## 8 · Bronnen
[1] Wikipedia, "Dakota Access Pipeline" — 1.172 mi / 1.886 km, Stanley ND → Patoka IL, 750 kb/d nameplate, ca. 40% Bakken, "Bakken system" met ETCOP. https://en.wikipedia.org/wiki/Dakota_Access_Pipeline
[2] Wikipedia, "Trunkline Pipeline" — ETCOP Patoka → Nederland, 678 mi omgebouwd + 66 mi nieuw, capaciteit 450–570 kb/d, aansluiting op DAPL bij Patoka. https://en.wikipedia.org/wiki/Trunkline_Pipeline
[3] Valley News Live (AP), 21-05-2026 — DAPL ca. 540.000 vaten/dag, ca. 4% VS-productie. https://www.valleynewslive.com/2026/05/21/decade-after-standing-rock-protests-contentious-segment-dakota-access-oil-pipeline-gets-ok/
[4] Wikipedia, "Patoka, Illinois" — dorpscoördinaat 38.7517/-89.0958 (geen anker). https://en.wikipedia.org/wiki/Patoka,_Illinois
[5] Wikipedia, "Nederland, Texas" — stadscoördinaat 29.9689/-94.0008 (geen anker). https://en.wikipedia.org/wiki/Nederland,_Texas
[6] Energy Transfer, Nederland Terminal fact sheet (mei 2023; cijfers via zoeksamenvatting, PDF niet uitleesbaar). https://www.energytransfer.com/wp-content/uploads/2023/05/Nederland-5-19-23.pdf
[7] RBN Energy, "Energy Transfer Crude Oil Pipeline (ETCOP)" — 30 inch Patoka → Nederland, 360 kb/d basis → 570 kb/d, in dienst Q2 2017 (zoeksamenvatting). https://rbnenergy.com/analytics/maps/midi/crude-oil-pipelines/energy-transfer-crude-oil-pipeline-etcop
[8] OSM-pbf-scan (Geofabrik us-north-dakota, us-illinois; eigen, 2026-10-29) plus haalbaarheidstoets (alle staten, 1.883,6 + 1.195,3 km). Operator "DAPL-ETCO Operations Management, LLC", substance=oil.
[9] Esri World Imagery via `v2/tools/sat_check.py` (z15): `sat-olie-stanley-nederland-stanley.png`, `-patoka.png`, `-patoka-etco.png`, `-nederland.png` in `v2/build-cache/satcheck/`.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)

**Stroom `olie-stanley-nederland`** → `v2/data/stroomroute-olie-stanley-nederland.json` (132,3 KB, versie 2, lonlat) — 2 benen, **3.079,2 km**, 6.418 punten, 3 markers, 0 stippel. Recept: `bash v2/tools/bak_stromen.sh olie-stanley-nederland` (functie `bak_olie_stanley_nederland`; geen profiel in `maak_stroombeen_weg.py`, geen router, geen zee).

| # | modaliteit | been | km | punten | stippel | naad naar vorig been |
|---|---|---|---|---|---|---|
| 1 | leiding | Dakota Access Pipeline, Stanley ND → Patoka IL (22 OSM-ways, gestikt) | 1.883,7 | 3.545 | nee | — |
| 2 | leiding | Energy Transfer Crude Oil Pipeline, Patoka IL → Nederland-terminal TX (67 OSM-ways, gestikt) | 1.195,5 | 2.873 | nee | 0,09 km |

**Markers (alle 3 uit §3):** `ol-stanley-terminal` 48.3043,-102.4601 (0,00 km van de lijn) · `ol-patoka-hub` 38.7852,-89.0777 (0,02 km: de DAPL-lijn passeert het tankenpark en loopt nog ~3,7 km door tot het eindterrein) · `ol-nederland-terminal` 29.9952,-93.9949 (0,00 km).

**Toets.** b1 1.883,7 km tegen gepubliceerd 1.886 = **-0,1%**; b2 1.195,5 km tegen 1.197 = **-0,1%** (norm +-15%). Enige naad 0,09 km (< 5 km). `toets_knikken`: 298 knikken, 0 omkeringen, 0 terugloop (de spikes zijn OSM-leidingzigzags en bochten). Geen rechte benen. json.load ok, versie 2, lonlat, modaliteit alleen leiding.

**Toelichting.**
- *Nieuw tool* `v2/tools/maak_leidingbeen_olie_stanley_nederland.py` (pure-Python-PBF-lezer, `pyosmium` is geblokkeerd): per extract een cache `olie-stanley-nederland-pbfpipes-<extract>.json` met kandidaat-ways; per been ontdubbelen op way-id, stikken over gedeelde OSM-nodes en daarna kortste pad (Dijkstra) tussen de knopen bij kop en eind; losse uiteinden binnen 3 km worden gestikt en gemeld.
- *b1:* filter name ~ "Dakota Access", zonder "Vernon/Marathon/Plains" en "DAPL Delivery" (Bridger); 8 naden van 0,02-0,03 km. Kop- en eindknoop 3 en 5 m van de ankers.
- *b2:* filter name/operator ~ "ETCO" (woordgrens) of "Energy Transfer Crude", substance=oil, zonder "Dakota Access"; includeert ook "ETCO Nederland Discharge"-ways, het kortste pad kiest zelf de trunk. Eén stik van 1,46 km (OSM-onderbreking), verder 0,01 km. Eindknoop 2 m van het Nederland-anker.
- *Geen stippel, geen aanloop, geen vlucht, geen kopie, geen via-punten* (leiding volgt een vaste buis).

**Lessen.**
- Een regex met "etco" matcht ook TETCO (Texas Eastern, gas), Metco, Transpetco en Assetco: gebruik een woordgrens (`etco`) en eis substance=oil, anders stikt het pad over gasleidingen. (Ik schreef eerst per ongeluk een backspace-teken in plaats van `` via een python-heredoc; de b2-run eindigde toen 59 km voor de terminal - controleer de eindknoop-afstand in de toolconsole.)
- Texas (710 MB) en Louisiana scannen duurt enkele minuten; de cache maakt een tweede run direct klaar.

**Meldingen aan de eigenaar (niet door deze bake aangepast).** Sitelaag olie mist de Nederland-terminal en de Patoka-hub (Motiva Port Arthur ligt 12 km verderop); het Bakken-aandeel dat Nederland haalt is niet gepubliceerd (§7). Registerregel (centraal): sleutel `olie-sn`.
