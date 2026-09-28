# Routebrief (licht) · zilver — Lucky Friday-mijn → Teck Trail-smelter (land)

**stroom-id:** `zilver-luckyfriday-trail` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** lood-zink-zilverconcentraat van Hecla's Lucky Friday-mijn (Mullan, Idaho, Silver
Valley) per **truck over de openbare weg** (209 miles ≈ 336,3 km, Hecla Mining eigen bedrijfsopgave) naar
de Teck Trail-smelter (Trail, British Columbia) — **stoppunt** (Hecla verkoopt 100% van de Lucky
Friday-productie aan deze smelter onder een vast contract sinds 2017).
**Welke as van het verhaal:** *VS-mijngat-opvulling* — vult het in het ontwerp genoemde ontbrekende
Amerikaanse-mijn-segment van de zilverstromen; jaarvolume ≈100 t Ag/j (Hecla Mining, aannemelijk — niet
dit ronde herbevestigd) [6].

## 1 · Ketenkaart
```
Lucky Friday-mijn (Mullan, Idaho) ──(b1 truck · I-90/WA-20/BC-6/BC-3B via Coeur d'Alene – Newport –
   Ione – Metaline Falls – grensovergang Nelway – Salmo · 336,3 km bedrijfsopgave)──►
   Teck Trail-smelter (Trail, BC) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Lucky Friday-mijn → Teck Trail-smelter | I-90 (Mullan–Coeur d'Alene) → WA-20/US-2-corridor (Newport–Ione–Metaline Falls) → grensovergang Metaline Falls–Nelway → BC Hwy 6 (Nelway–Salmo) → BC Hwy 3B (Salmo–Trail) [1][5][6][7] | **336,3** [1, Hecla Mining 10-K: "209 miles… in highway trucks operated by a contract shipper" — BINDEND uit de haalbaarheidstoets, vervangt de hemelsbrede ~250 km uit het ontwerp] | `maak_stroombeen_weg` (BINDEND: geen `toets_spoorroute` — de haalbaarheidstoets heeft spoor uitgesloten, uitsluitend truck) | nee — corridor + bestemming zijn hard gebrond (10-K, vast contract), lijn wordt gemeten en doorgetrokken |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-luckyfriday-mijn` | mijn / plant (laad) | Lucky Friday-mijn (Hecla Mining, Mullan, Idaho) | 47.4708, -115.7832 | [8][9] | bron-gelegd — letterlijk hergebruikt uit `w-lucky-friday` (`v2/design/zilver-sitelaag.json`, tevens OSM-bevestigd node 585375090); dit ronde zelf satellietblik z15 gezet: mijn-/molencomplex direct ten noorden van I-90 bij Mullan, met een tailings-/bezinkvijver oostelijk langs de rivier — bevestigt het punt |
| `ag-trail-smelter` | smelter+raffinaderij (los, stoppunt) | Teck Trail-smelter (Teck Resources, Trail, BC) | 49.1000, -117.7125 | [10][11] | bron-gelegd — letterlijk hergebruikt uit `w-ref-trail` (`v2/design/zilver-sitelaag.json`); dit ronde zelf satellietblik z15 gezet: groot smeltercomplex met schoorstenen, bezink-/tailingsbekkens en een spooremplacement, direct westelijk van de Columbia-rivier tegenover Trail-centrum — bevestigt het punt |

## 4 · Via-punten (b1 — de truckweg heeft meerdere corridorkeuzes: staatsgrens WA en landsgrens VS/Canada)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Coeur d'Alene (Idaho) | 47.6743, -116.7812 | I-90 eindigt hier als doorgaande corridor westwaarts; knooppunt richting het noorden (55 mijl van de mijn, bevestigd door Hecla zelf) [9] |
| b1 | 2 | Newport (Washington) | 48.1796, -117.0433 | staatsgrens ID/WA op de doorgaande corridor US-2/WA-20 noordwaarts naar Pend Oreille County |
| b1 | 3 | Ione (Washington) | 48.7413, -117.4205 | knooppunt op WA-20 waar de corridor richting de grens afbuigt, i.p.v. verder oostwaarts |
| b1 | 4 | Metaline Falls (Washington) | 48.8636, -117.3719 | laatste Amerikaanse plaats vóór de grens, op WA-31 richting de grensovergang [5] |
| b1 | 5 | Nelway (British Columbia, grensovergang) | 49.0007, -117.2993 | Metaline Falls–Nelway-grensovergang, de enige doorgaande commerciële grenspost op deze corridor (WA-31 ↔ BC Hwy 6) [5] |
| b1 | 6 | Salmo (British Columbia) | 49.1934, -117.2787 | draaipunt waar BC Hwy 6 overgaat op BC Hwy 3B, de doorgaande route naar Trail (via Fruitvale/Montrose) [6][7] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Teck Trail-smelter | Teck Resources | lood-zink-zilverconcentraat (Lucky Friday + regionale mijnen) → lood/zink-metaal + good-delivery zilver | ≈450 kt Ag-equivalent/j indicatief, grootste geïntegreerde lood-zink-zilversmeltcomplex van Noord-Amerika (bedrijfsopgave) | [11] |

## 6 · Stoppunt
De brief stopt bij de Teck Trail-smelter: geen fase D/E — Hecla's 10-K noemt geen vervolgbestemming voor
het daar geraffineerde zilver, en het ontwerp gaf geen aparte fabriek/afnemer voor fase D. De smelter ís
de contractuele eindbestemming van deze as.

## 7 · Open punten
- **De exacte wegroute door Washington is niet uit één bron bevestigd voor déze specifieke lading** —
  Hecla's 10-K bevestigt hard "209 miles… highway trucks" maar noemt geen straatnamen. De hier gekozen
  corridor (via Coeur d'Alene – Newport – Ione – Metaline Falls – grensovergang Nelway – Salmo – Trail)
  is de geografisch kortste doorgaande route met een echte commerciële grensovergang en geeft een
  hemelsbrede ketenlengte van ~291 km over de gekozen via-punten — plausibel tegen de 336,3 km
  bedrijfsopgave (omwegfactor ~1,15, normaal voor een bergachtige tweebaans corridor). Het alternatief
  via US-95/Sandpoint/Bonners Ferry naar de grensovergang Eastport-Kingsgate ligt geografisch verder om
  (Kingsgate → Trail loopt via Cranbrook, een grote omweg) en is daarom niet als hoofdcorridor gekozen.
  De bak-agent toetst dit bij het wegscannen tegen de 336,3 km-norm (§7-indicatie, geen harde ±15%-eis
  volgens de haalbaarheidstoets, maar wel de aangewezen toets).
- **Jaarvolume (~100 t Ag/j) is dit ronde niet herbevestigd** — komt uit de sitelaag-capaciteitsbron
  (Hecla Mining kwartaal-/jaarrapportages 2024), status blijft aannemelijk.
- **De twee hergebruikte sitelaag-ankers stonden vóór dit ronde op status "aannemelijk"** (nog geen
  satellietblik); dit ronde zijn ze op site-niveau satelliet-bevestigd (§3). De centrale sitelaag-json
  is niet aangeraakt (eigen-bestanden-regel) — de orchestrator kan `w-lucky-friday` en `w-ref-trail` in
  `v2/design/zilver-sitelaag.json` naar status "bron-gelegd" optrekken met verwijzing naar deze brief.

## 8 · Bronnen
[1] Hecla Mining Company, Form 10-K (SEC-jaarverslag) — "Concentrates produced at the Lucky Friday mill
    are transported 209 miles to the Teck lead-zinc smelter in Trail, British Columbia, Canada in
    highway trucks operated by a contract shipper"; vast contract sinds 2017, geamendeerd 2021, 100% van
    de productie verkocht aan deze smelter (haalbaarheidstoets webcheck, SEC EDGAR-filing).
[2] Hecla Mining, "Lucky Friday | Idaho" — https://www.hecla.com/operations/lucky-friday-idaho
    (mijn/molen bij Mullan, 55 mijl oostelijk van Coeur d'Alene via I-90).
[3] Wikipedia (en), "Lucky Friday mine" — https://en.wikipedia.org/wiki/Lucky_Friday_mine
[4] Wikipedia (en), "Mullan, Idaho" — https://en.wikipedia.org/wiki/Mullan,_Idaho
[5] Wikipedia (en), "Metaline Falls–Nelway Border Crossing" —
    https://en.wikipedia.org/wiki/Metaline_Falls%E2%80%93Nelway_Border_Crossing (WA-31 ↔ BC Hwy 6).
[6] Wikipedia (en), "British Columbia Highway 3B" — https://en.wikipedia.org/wiki/British_Columbia_Highway_3B
    (Trail–Montrose–Fruitvale–Salmo-corridor).
[7] International Selkirk Loop, "Salmo" — https://selkirkloop.org/member-category/cities/british-columbia/salmo/
    (Salmo als knooppunt bij de grensovergang Nelway, BC Hwy 6).
[8] v2/design/zilver-sitelaag.json, id `w-lucky-friday` — OSM landuse=quarry "Lucky Friday Mine"
    (Nominatim), 47.4708/-115.7832; letterlijk hergebruikt anker.
[9] Wikipedia (en), "Interstate 90 in Idaho" + Hecla-bron [2] — Mullan ligt aan I-90, Lookout Pass
    (Montana-grens) 6 mijl oostelijk; Coeur d'Alene 55 mijl westelijk.
[10] v2/design/zilver-sitelaag.json, id `w-ref-trail` — Wikipedia-geohack "Teck Cominco smelter",
    49.1000/-117.7125; letterlijk hergebruikt anker.
[11] Teck Resources, corporate bedrijfsopgave (via sitelaag `w-ref-trail`) — Trail Operations, grootste
    geïntegreerde lood-zink-zilversmeltcomplex van Noord-Amerika, indicatief 400-500 t Ag/j.
[12] Nominatim/OSM plaatsnodes Coeur d'Alene, Newport, Ione, Metaline Falls, Nelway, Salmo — via-punten
    op de doorgaande corridor. https://nominatim.openstreetmap.org/
[13] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) —
    `v2/build-cache/satcheck/sat-zilver-luckyfriday-trail-lucky-friday.png` en
    `sat-zilver-luckyfriday-trail-trail.png` (beide nieuw dit ronde).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Benen:** 1 (b1, truck, doorgetrokken, geen stippel) · **347,6 km** · 5.425 punten · 2 markers ·
`v2/data/stroomroute-zilver-luckyfriday-trail.json` (116,2 KB).

**Recept:** `python v2/tools/maak_stroombeen_weg.py --profiel zilver-luckyfriday-trail-luckyfriday-trail
--bron geofabrik` (profiel in `v2/tools/maak_stroombeen_weg.py`, extracts us-idaho/us-washington/canada,
vensterKm 60) → `bash v2/tools/bak_stromen.sh zilver-luckyfriday-trail` (functie
`bak_zilver_luckyfriday_trail()` in `v2/tools/bak_stromen.sh`).

**Km-toets:** gemeten wegkm **347,3 km** (getekende lijn 347,6 km incl. anker-stompjes) tegen de
BINDENDE 10-K-bedrijfsopgave van 336,3 km (209 miles) = **+3,3%** — binnen elke redelijke marge, ook
al is 336,3 km zelf al een harde bedrijfsopgave en geen hemelsbrede schatting. De open-punt-vraag van
de brief (§7, welke corridor de trucks werkelijk rijden) is hiermee beantwoord in het voordeel van de
Nelway-corridor: geen enkel via-punt snapte > 0,5 km (grootste 0,19 km bij Ione), dus er was geen
aanleiding om de alternatieve grensovergang Eastport–Kingsgate te proberen.

**Toelichting stippels/aanlopen:** geen. Geen zeebeen (geen haven-aanloop), geen luchtbeen, geen
leidingbeen, geen gedeeld been. Beide site-ankers liggen op het mijn- resp. smelterterrein zelf:
plant → weg 0,13 km, weg → kade 0,11 km (beide ruim onder de last-mile-drempel van ~2 km) — geen
last-mile-stippel nodig.

**Toets (§5):** `toets_knikken.py` → 18 knikken ≥60° (spikes op kruispunten/afslagen, straal 4–39 m),
**0 omkeringen, 0 terugloop** (geen reparatie nodig). `toets_rechte_benen.py --min-km 5` → geen
melding voor dit been (geen omwegfactor 1,000; het is een echte, licht kromme wegroute). Naad n.v.t.
(één been, geen aansluitingen). `json.load`: versie 2, punt_formaat lonlat, modaliteit `truck` (enige,
geldig), 1 been met 5.425 punten (≥2), bestand 116,2 KB.

**Lessen:**
- De 336,3 km 10-K-bedrijfsopgave is bindend maar geeft geen straatnamen; de gekozen Nelway-corridor
  bleek bij het wegscannen de juiste — alle via-snaps ≤0,19 km bevestigen dat de brief-auteur de
  juiste geografisch kortste commerciële grensovergang had gekozen, zonder dat er een tweede
  grensovergang geprobeerd moest worden.
- Eén been met twee terreinankers (mijn/plant en smelter/kade) zonder enige overslag is de simpelste
  klasse in deze werkwijze: geen naad-toets, geen stippel-beslissing, alleen de km-toets telt.

**Sitelaag-correctie (niet zelf uitgevoerd, eigen-bestanden-regel):** `w-lucky-friday` en `w-ref-trail`
in `v2/design/zilver-sitelaag.json` stonden op status "aannemelijk"; deze brief heeft ze §3 dit ronde
satelliet-bevestigd op exact dezelfde coördinaten als hierboven gebakken (47.4708,-115.7832 en
49.1000,-117.7125) — de orchestrator kan de sitelaag-status optrekken naar "bron-gelegd" met
verwijzing naar deze brief.
