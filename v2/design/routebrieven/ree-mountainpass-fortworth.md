# Routebrief (licht) · zeldzame aardmetalen — Mountain Pass → Fort Worth (Verenigde Staten)

**stroom-id:** `ree-mountainpass-fortworth` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) ·
**status:** gebakken
**Keten in één zin:** NdPr-oxide van Mountain Pass gaat per truck (modaliteit niet gepubliceerd) ~2.250 km
over I-15 → I-11/US-93 → I-40 → US-287 naar de Independence-fabriek in Fort Worth, waar MP Materials het
op eigen terrein tot NdPr-metaal en gesinterde NdFeB-magneten verwerkt — de enige koper/REE-achtige keten
van de atlas zónder zee én zonder overslagpunt.
**Welke as van het verhaal:** de Amerikaanse mine-to-magnet-landketen (as 4 van 6 in het REE-ontwerp).
MP Materials produceerde in FY2025 50.692 t REO in concentraat en 2.599 t NdPr-oxide, waarvan 1.994 t
verkocht (Q1 2026: 917 t) [1]; Independence draait sinds januari 2025 op commerciële NdPr-metaalproductie
en bouwt naar ~1.000 t NdFeB-magneten/jaar [2]. De vroegere concentraat-rondreis naar China (Shenghe-
offtake) is op 2025-04-17 gestopt na het 125%-tarief [3]; China importeerde jan–okt 2024 nog 46,9 kt ruw
REE-erts uit de VS (98% van zijn ertsimport) [4] — die stroom bestaat niet meer en wordt hier niet getekend.

## 1 · Ketenkaart
Mountain Pass mijn+scheiding ──(b1 truck, aannemelijk · I-15→I-11/US-93→I-40→US-287 · ~2.250 km)──►
Independence Fort Worth (metaal+magneetfabriek) ──(b2 D, eigen terrein · 0 km)──► gesinterde NdFeB-magneten ⏹ stoppunt

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck (aannemelijk: modaliteit niet gepubliceerd; MP's 10-K noemt alleen "immediately adjacent to Interstate 15 … within a one-hour drive of a major railhead" [5]; spooralternatief 2.312 km gemeten in M28, niet getekend) | `ree-mp-laad` → `ree-fw-fabriek` | I-15 (Mountain Pass→Las Vegas) → US-93/I-11 (Boulder City) → I-40 (Kingman–Flagstaff–Albuquerque–Amarillo) → US-287 (Amarillo–Wichita Falls–Fort Worth) | ~2.250 (OSRM/OSM; geen publicatie) | maak_stroombeen_weg (extracts us-california/nevada/arizona/new-mexico/texas; profiel her te gebruiken uit `fetch_landnet.py`) | nee |
| b2 | D | eigen terrein | `ree-fw-fabriek` (NdPr-metaal) → `ree-fw-fabriek` (NdFeB-magneten) | zelfde perceel, geen been | 0 | marker + verwerkingsknoop, geen geometrie | — |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-mp-laad` | mijn / laadplek | Mountain Pass mijn- en scheidingsfabriek (MP Materials, San Bernardino County, CA) | 35.4786, -115.5325 | [6][7] Wikipedia-geohack + MP-facilities | bron-gelegd (z15 gezien: open pit met bermwegen, twee tailings-bekkens, verwerkingsgebouwen en I-15 net ten zuiden — het complex uit [6][7], geen laadloods apart te onderscheiden) |
| `ree-fw-fabriek` | losplek / metaal- en magneetfabriek | MP Materials "Independence" facility, 13840 Independence Parkway, Fort Worth, TX 76177 | 32.9845, -97.2498 | [8] adres MP Materials + [9] geocode | bron-gelegd (z15 gezien: middelgroot bedrijfspand in een logistiek/industriepark direct bij de I-35W-afrit, spoorlijn ernaast — consistent met het 250.000 sq ft-pand uit [8]) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Las Vegas (I-15/US-93-knoop) | 36.1750, -115.1372 | pint I-15 als vertrekcorridor i.p.v. een directe woestijnroute |
| b1 | 2 | Boulder City-omgeving (US-93/I-11) | 36.0125, -114.7414 | overstap I-15 → US-93/I-11 richting Kingman |
| b1 | 3 | Kingman, AZ (US-93/I-40-knoop) | 35.1894, -114.0530 | overstap US-93/I-11 → I-40 oostwaarts |
| b1 | 4 | Flagstaff, AZ (op I-40) | 35.1983, -111.6513 | pint I-40 als doorgaande corridor i.p.v. een noordelijker route (US-89/I-17) |
| b1 | 5 | Albuquerque, NM (op I-40) | 35.0844, -106.6504 | pint I-40 door New Mexico i.p.v. afbuigen via I-25 |
| b1 | 6 | Amarillo, TX (I-40/US-287-knoop) | 35.2220, -101.8313 | overstap I-40 → US-287 zuidoostwaarts |
| b1 | 7 | Wichita Falls, TX (op US-287) | 33.9137, -98.4934 | pint US-287 als doorgaande corridor naar Fort Worth i.p.v. US-82/US-81 |
| b1 | 8 | Decatur/Justin-omgeving, TX (US-287 laatste stuk) | 33.2343, -97.5861 | laatste corridorkeuze vóór de aansluiting op het Fort Worth-stadsnet (US-287 i.p.v. FM-wegen) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Independence, Fort Worth | MP Materials | NdPr-metaal (sinds jan 2025) → NdFeB-magneten | ~1.000 t NdFeB/jaar (opschaling vanaf eind 2025) | [2] |
| Vertakking (niet getekend) | onbekende Aziatische afnemers (Japan/Zuid-Korea/breder Azië) via LA/Long Beach | het merendeel van MP's NdPr-oxide gaat nog steeds naar Azië, niet naar Independence — 10-K 2024: "primarily to customers in Japan, South Korea and broader Asia" [5] | onbekend | [5] |
| Historisch, niet getekend | Shenghe Resources (China) | concentraat-rondreis Mountain Pass↔China, offtake liep formeel door tot jan 2026 maar zendingen stopten 2025-04-17 na het 125%-tarief | 37.500 t erts-export 2024 → 14.000 t 2025 (USGS) | [3][4] |

## 6 · Stoppunt
De brief stopt bij Independence: dat is de enige gedocumenteerde eindfabriek op de eigen keten van MP Materials.
Fase E (GM als afnemer van de magneten) is in één zin gegeven — GM heeft ~1.000 t/jaar magneten gecontracteerd
voor zijn Ultium-EV-motoren en de eerste levering vanaf Independence vond plaats in september 2026 [10] — maar
GM's eigen fabriek is nergens genoemd, dus wordt geen been getekend.

## 7 · Open punten
- **Modaliteit b1:** nergens gepubliceerd; truck is de enige eerlijke aanname (10-K noemt alleen de ligging
  naast I-15 en "binnen een uur van een spoorkop" [5]); het gemeten spooralternatief (2.312 km, M28) is niet getekend.
- **Gepubliceerde km:** geen bron voor Mountain Pass→Fort Worth; de bake-toets loopt tegen OSRM (~2.250 km).
- **Meerderheid van de NdPr-oxide-stroom:** gaat naar Azië (Japan/Zuid-Korea) via een niet nader genoemde
  route/haven (vermoedelijk LA/Long Beach) — geen kade, geen afnemer met naam en adres gevonden; niet getekend.
- **GM-fabriek:** locatie van GM's eigen magneetafname (Ultium-motoren) niet gepubliceerd.
- **10X Northlake-magneetfabriek** (Texas, gepland): niet in bronnen bevestigd op adresniveau; niet getekend.
- **v1-correctie (buiten deze opdracht):** `data/rare-earths.js`/`_chokepoints.js` moeten de gestopte
  Mountain-Pass-rondreis (2025-04-17), de Lynas-Kalgoorlie-tussenstap en de Tengchong-poorten (i.p.v. Ruili)
  nog verwerken — zie het REE-ontwerpdocument.

## 8 · Bronnen
[1] MP Materials, Q4 & FY2025 Results (investor news, 2026-01-21 e.v.): 50.692 t REO-concentraat, 2.599 t NdPr-oxide geproduceerd, 1.994 t verkocht, Q1 2026 917 t NdPr — https://investors.mpmaterials.com/investor-news/news-details/2026/MP-Materials-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx
[2] MP Materials, "MP Materials Restores U.S. Rare Earth Magnet Production" (2025-01-22): commerciële NdPr-metaalproductie op Independence, ~1.000 t NdFeB/jaar bij opschaling — https://mpmaterials.com/news//mp-materials-restores-u-s-rare-earth-magnet-production/
[3] Reuters via TradingView (2025-04-17): MP Materials stopt China-bound concentraatzendingen na het 125%-tarief; Shenghe-offtake liep formeel door tot jan 2026 — https://www.tradingview.com/news/reuters.com,2025:newsml_L4N3QV1OL:0-mp-materials-stops-china-bound-rare-earth-shipments-over-tariffs/
[4] 一带一路网 (yidaiyilu.gov.cn): China importeerde jan–okt 2024 46,9 kt ruw REE-erts uit de VS = 98% van zijn ertsimport — https://www.yidaiyilu.gov.cn/p/01S3P0ID.html
[5] MP Materials Corp., Form 10-K FY2024 (SEC): Mountain Pass "immediately adjacent to Interstate 15 and within a one-hour drive of a major railhead"; NdPr-oxide "primarily to customers in Japan, South Korea and broader Asia" — https://www.sec.gov/Archives/edgar/data/1801368/000180136825000009/mp-20241231.htm
[6] Wikipedia, "Mountain Pass Rare Earth Mine": 35°28′43″N 115°31′57″W (35.47861, -115.53250), San Bernardino County, CA — https://en.wikipedia.org/wiki/Mountain_Pass_mine
[7] MP Materials, Facilities: Mountain Pass mijn- en scheidingscomplex — https://mpmaterials.com/facilities/
[8] Community Impact (2024-04-05 / 2024-05-22): MP Materials Independence, 13840 Independence Parkway, Fort Worth TX 76177, 250.000 sq ft — https://communityimpact.com/dallas-fort-worth/keller-roanoke-northeast-fort-worth/business/2024/04/05/mp-materials-receives-585m-for-north-fort-worth-manufacturing-facility/
[9] OpenStreetMap/Nominatim, geocode van 13840 Independence Parkway, Fort Worth, TX 76177 → 32.9845224, -97.2498267 — https://nominatim.openstreetmap.org/
[10] Telemetry Agency / GreenCars / Rare Earth Exchanges (2026-09-17 e.v.): eerste NdFeB-magneten van Independence geleverd aan GM, contract ~1.000 t/jaar voor Ultium-EV-motoren, commerciële leveringen vanaf Q4 2026 — https://www.telemetryagency.com/post/september-17-2026-mp-materials-making-permanent-magnets-in-texas · https://www.greencars.com/news/mp-materials-starts-making-permanent-magnets-for-gm-evs-in-texas

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `ree-mountainpass-fortworth`** → `v2/data/stroomroute-ree-mountainpass-fortworth.json` — 1 been ·
2.026,5 km · 12.362 punten · 2 markers. Recept: `bak_stromen.sh` (functie `bak_ree_mountainpass_fortworth`),
profiel `ree-mountainpass-fortworth-mountainpass-fortworth` in `maak_stroombeen_weg.py` (via-punten 1-op-1
hergebruikt uit de bestaande corridordefinitie in `fetch_landnet.CORRIDORS`, alleen omgezet naar (lon, lat)).

| # | modaliteit | km | stippel? | toelichting |
|---|---|---|---|---|
| 1 | truck | 2.026,5 | nee | `maak_stroombeen_weg.py --profiel ree-mountainpass-fortworth-mountainpass-fortworth --bron geofabrik` over de vijf VS-extracts (california/nevada/arizona/new-mexico/texas), I-15 → US-93/I-11 → I-40 → US-287, 8 via-punten in reisvolgorde; getekende lijn incl. anker-verbindingen 2.026,5 km tegen de brief-indicatie ~2.250 km (OSRM/OSM, geen publicatie) = **-10,0%** — geen ±15%-toets mogelijk (`gepubliceerdKm: None`, brief §7), alleen referentie |

**Fase D** (NdPr-metaal → gesinterde NdFeB-magneten, brief b2) is **geen apart been** getekend: 0 km, zelfde
perceel, eigen terrein. De fabrieksmarker op `ree-fw-fabriek` draagt zowel de losplek- als de D-knooprol
(naam vermeldt beide fasen).

**Toets:** 1 been, dus geen naden tussen benen · markers **0,0 km** van de lijn (beide uit §3; de anker-
verbindingsstukjes plant→weg 1,00 km en weg→kade 0,02 km zijn door `hecht_marnet` al in de getekende lijn
opgenomen, dus de markers zelf vallen exact op het beginpunt/eindpunt) · `toets_knikken.py`: **0 omkeringen,
0 terugloop** (31 spikes < 60°/kleine straal — junctie-ruis op het VS-wegnet, geen fout) ·
`toets_rechte_benen.py --min-km 5`: been 1 komt niet in de lijst voor (12.362 punten, geen rechte lijn) ·
JSON: `versie 2`, `punt_formaat lonlat`, modaliteit `truck` (in de toegestane set), 1 been ≥ 2 punten,
bestand 261,4 KB (< 300 KB).

**Bevindingen (buiten de norm, niet dichtgetrokken):**
- Plant → eerste wegvertex is 1,00 km (norm ≤ 0,5 km) — de N-onverharde/mijnwegen rond de Mountain Pass-
  scheidingsfabriek zijn dun gekarteerd in OSM; de eerste bruikbare vertex op een `unclassified`-weg ligt op
  1,00 km van het satelliet-gelegde ankerpunt. Doorgetrokken (de weg bestaat, alleen het eerste stuk is
  ongekarteerd), geen stippel.
- Geen ±15%-toets tegen een gepubliceerde lengte mogelijk (brief §7: geen bron voor Mountain Pass→Fort
  Worth); de bake-uitkomst (2.026,5 km) ligt 10% onder de eigen brief-indicatie van ~2.250 km — beide zijn
  schattingen (OSRM resp. deze scan), geen van beide is een publicatie.

**Gereedschapslessen:**
- `maak_stroombeen_weg.py` had een latente bug voor elk profiel met `gepubliceerdKm: None` én een geslaagde
  routering: de lengtetoets en de JSON-afwijkingsvelden deelden onvoorwaardelijk door `gepubliceerdKm`,
  wat een `TypeError`/`UnboundLocalError` gaf zodra een been zonder publicatie wél een pad vond (de
  bestaande profielen met `None` waren allemaal bewust-verwachte mislukkingen, dus dit pad was nooit
  eerder geraakt). Gefixt met een `is None`-guard: rapporteert de scanuitkomst als referentie in plaats van
  te crashen; `afwijkingPct`/`binnenTolerantie` worden dan `null` in de geojson-properties. Kleine, gerichte
  edit, geen ander profiel geraakt.
- De via-puntenlijst uit `fetch_landnet.CORRIDORS` (id `ree-mountainpass-fortworth`) stond al klaar in
  (lon, lat) — geen omzetting nodig buiten het overtypen naar het `PROFIELEN`-dict-formaat.

**Open na het bakken (ongewijzigd t.o.v. §7):** modaliteit blijft aannemelijk (nergens gepubliceerd) ·
geen gepubliceerde km om tegen te toetsen · de meerderheid van de NdPr-oxide-stroom naar Azië (Japan/
Zuid-Korea, vermoedelijk via LA/Long Beach) is niet getekend (geen kade/afnemer met naam+adres) · GM's
eigen magneetafnamefabriek en de geplande 10X Northlake-fabriek zijn niet op adresniveau bevestigd ·
v1-correcties aan `data/rare-earths.js`/`_chokepoints.js` (buiten deze opdracht).
