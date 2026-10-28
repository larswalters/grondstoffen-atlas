# Routebrief (licht) · kolen — Gevra OCP (SECL) → NTPC Korba STPS (India)

**stroom-id:** `kolen-gevra-korba` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) · **status:** gebakken
**Keten in één zin:** thermische kolen (G-11) uit de dagbouw Gevra OCP (SECL/Coal India, Korba-veld, Chhattisgarh) gaan per **spoor** (merry-go-round, MGR; Gevra-aftakking, wye bij Kusmunda) naar de pit-head-centrale NTPC Korba STPS in Jamnipali (2.600 MW) — stoppunt, want kolen worden daar elektriciteit. Eén kort been; titel noemt het werkelijke eindpunt (de centrale), zoals het id.
**Welke as van het verhaal:** *India-binnenland: 's werelds grootste kolenmijn voedt de naastgelegen centrale.* Gevra produceerde **55,8 Mt ROM in 2025** (GEM; 59,1 Mt in 2023) [3]; NTPC Korba heeft een gecontracteerde **145,12 LMT = 14,5 Mt per jaar** uit "SECL Gevra OCP, G-11" in zijn CERC-formulier (5-jaarsdata 2017-18 t/m 2021-22; peiljaar van het aandeel niet gegeven) [4]. Aandeel Gevra → Korba ≈ 26% van de mijn (afgeleid, 14,5 / 55,8, jaren verschillen). Aannemelijk: één operatorbron voor de levering, geen onafhankelijke tweede.

## 1 · Ketenkaart
```
Gevra OCP (put + kolenverwerking aan de noordrand) `kolen-gevra-laad`
   ──(b1 spoor · Gevra-lijn → wye bij Kusmunda (omkering) → Korba-aftakking/MGR · router 23,1 km,
       CERC-opgave 14,80 km "MGR" · aannemelijk: één bron)──► NTPC Korba STPS `kolen-korba-stps` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A+C | spoor | `kolen-gevra-laad` → `kolen-korba-stps` | Gevra-sporen → Kusmunda/Gevra Road-wye → Champa–Gevra Road-aftakking → centrale (MGR-lus) [1][5][6] | **gepubliceerd: 14,80 km** ("Transportation distance … MGR", CERC-formulier NTPC [4]); router 23,1 km (23,5 over de 106 punten), hemelsbreed 15,0 km, verhouding 1,54; ±15%-toets mislukt (+56%): zie §7 | toets_spoorroute (1-op-1-net), één run, geen via | nee — doorgetrokken; "aannemelijk" staat in de beennaam |

Geen zee, weg, leiding, lucht, haven-aanloop of kopie. Geen fase D/E (geen bron noemt een vervolg voor de elektriciteit). Last mile: snap kop **1,89 km** (< 2 km) en staart **0,69 km**: geen stippel; wel een zichtbare naad van 1,9 km tussen site-anker en lijnbegin (§7).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-gevra-laad` | mijn / laadplek | Gevra OCP (SECL), Korba-veld — **letterlijk hergebruikt** `w-gevra` uit `v2/design/kolen-sitelaag.json` (GEM 22,336312 / 82,545748) | 22.3363, 82.5457 | [3][7] | bron-gelegd (z15 hier gezien: kruis op de noordrand van een ~5 km grote terrasput met haul roads; kolenverwerking met bandcorridors en spoorbundel 0,6–1,0 km noordwest op ca. 22.344, 82.532, hoofdspoor door Gevra-stad op lat 22.350) |
| `kolen-korba-stps` | verwerker / losplek | NTPC Korba Super Thermal Power Station, Jamnipali (7 eenheden, 2.600 MW) | 22.3858, 82.6816 | [1][4] | bron-gelegd (z15 gezien: kruis op het ketelhuis met schoorstenen en rook; kolenopslag/bunkers aan de noordzijde, MGR-lussen oost en rond, koeltorens en schakelveld zuid) |

Hergebruik: `w-gevra` (sitelaag). Geen eerder anker voor Korba of een andere Indiase centrale in de bestaande brieven/markers (Mundra, Dhamra en Vindhyachal zijn alleen sites in de sitelaag).

## 4 · Via-punten
Geen. Het spoornet kent geen directe verbinding tussen het Gevra-hoofdspoor en de Korba-aftakking: zonder omkering vraagt de router 147-153 km, dus de **wye bij Kusmunda (22.3514, 82.6364, ~1 km noordwest van station Gevra Road 22.3492, 82.6461 [6])** is topologisch dwingend; via-punten helpen niet. Lijnbeeld: spoor oostwaarts (lat ≈ 22.350–22.355) tot de wye, daar een omkering (178,7°, boogstraal ~318 m, ~2,4 km uit- en terugweg langs twee evenwijdige sporen), dan noordoostwaarts via 22.373, 82.665 naar de centrale. Satelliet (z15, wye): spoorboog met afsplitsende lijnen en geulbrug, geen kruising met een ander net.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Gevra OCP | South Eastern Coalfields Ltd (Coal India), 100% | ROM-kolen (subbitumineus, thermisch, G-11) → spoor/MGR | 55,8 Mt (2025); vergunning 70 Mtpa (EC 2024); piek 49 Mtpa eerder gerapporteerd | [3] |
| NTPC Korba STPS | NTPC Ltd | kolen (Gevra, Kusmunda) → elektriciteit; Hasdeo-water | 2.600 MW; gecontracteerd Gevra 14,5 Mt/j (CERC-5-jaarsformulier) | [1][4] |

## 6 · Stoppunt
De brief stopt bij de centrale: de kolen houden er op als grondstof (verstookt tot elektriciteit); geen bron noemt een fysiek vervolgproduct.

## 7 · Open punten
- **Spoorkm wijkt af van de operatoropgave:** CERC-formulier noemt 14,80 km MGR-transportafstand [4]; router 23,1 km. Oorzaak waarschijnlijk (a) de OSM-topologie dwingt de wye-omkering en kent de directe MGR niet, (b) de kop snapt 1,89 km van het anker op het hoofdspoor (de eigen Gevra-sporen ontbreken). Geen gepubliceerde spoorlijn-lengte buiten die 14,80 km; de lijn is dus een **indicatieve corridor, geen gemeten MGR**.
- **MGR-tracé niet gekarteerd en niet gebrond:** parlementsantwoord (3-12-2019) koppelt Korba aan Gevra via MGR [5]; het precieze tracé noemt geen bron. Status **aannemelijk** (levering gebrond, route niet).
- **Aandeel 14,5 Mt** staat op het contract (CERC), niet op werkelijke aanvoer; jaren verschillen met GEM 2025.
- **Verlenging naar NSPCL Bhilai** (NTPC-tender 18-1-2023): geen route of bewijs, blijft weg (haalbaarheidstoets).
- **Sitelaag:** `kolen-sitelaag.json` heeft `w-gevra`, `w-kusmunda` en `w-dipka` maar geen Korba STPS; centrale kan centraal als site (rol centrale, 2.600 MW) toegevoegd worden.

## 8 · Bronnen
[1] en.wikipedia, Korba Super Thermal Power Station — 22.3858, 82.6816; 2.600 MW; kolen uit Kusmunda en Gevra; Champa–Gevra Road-aftakking. https://en.wikipedia.org/wiki/Korba_Super_Thermal_Power_Station
[2] en.wikipedia, Korba Coalfield — Gevra grootste dagbouw van India; Champa–Korba spoor 1955; Kusmunda 50 Mtpa. https://en.wikipedia.org/wiki/Korba_Coalfield
[3] Global Energy Monitor, Gevra Coal Mine — 22.336312, 82.545748; SECL 100%; 55,8 Mt (2025), 59,11 Mt (2023). https://www.gem.wiki/Gevra_Coal_Mine
[4] NTPC/CERC, O&M-pro-forma Korba STPS (2017-18 t/m 2021-22) — "SECL Gevra OCP for 145.12 LMT with G-11 grade", Mode MGR, afstand 14.80. https://cercind.gov.in/2024/draft_reg/O&M_data/NTPC/Korba Final.pdf
[5] Rajya Sabha, antwoord 3-12-2019 (PQ 250) — Korba en Sipat via MGR aan SECL Gevra resp. Dipka gekoppeld; alleen via zoekresultaat gezien, PDF niet geopend (redirect). https://rsdebate.nic.in/bitstream/123456789/704189/2/PQ_250_03122019_S165_p134_p135.pdf
[6] en.wikipedia, Gevra Road railway station — 22°20′57″N 82°38′46″E; Gevra Road–Champa-lijn. https://en.wikipedia.org/wiki/Gevra_Road_railway_station
[7] `v2/design/kolen-sitelaag.json`, site `w-gevra` (bron-gelegd) — hergebruikt anker.
[8] Esri World Imagery via `v2/tools/sat_check.py` en OSM-spoornet via `toets_spoorroute.mjs` (2026-10-28) — `v2/build-cache/satcheck/sat-kolen-gevra-korba-gevra.png`, `-korba-stps.png`, `-kusmunda-wye.png`.

## 9 · Gebakken (2026-10-28, lichte werkwijze, M31 golf 10)
**Recept:** `bash v2/tools/bak_stromen.sh kolen-gevra-korba` (functie `bak_kolen_gevra_korba`). Geometrie: een run `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs` (1-op-1-net, geen via, `--hoofd-km=100`), tussenuitvoer hergebruikt: `v2/build-cache/ais/graaf/spoorroute-kolen-gevra-korba-gevra-korba.geojson`. Uitvoer `v2/data/stroomroute-kolen-gevra-korba.json` (2,6 KB, versie 2, lonlat).

| # | modaliteit | been | km | punten | stippel | naad |
|---|---|---|---|---|---|---|
| 1 | spoor | trein Gevra OCP naar NTPC Korba STPS (via wye Kusmunda; aannemelijk: één bron) | 23,5 | 106 | nee | n.v.t. |

Totaal 23,5 km, 2 markers: `kolen-gevra-laad` (22.3363, 82.5457, hergebruikt `w-gevra`) en `kolen-korba-stps` (22.3858, 82.6816).

**Toets (handleiding §5):**
- Km: 23,5 (router 23,1 over de bake-meting) tegen 14,80 km MGR-opgave: +59%. De brief geeft geen echte spoorkm van het net maar de MGR-afstand, dus indicatie en geen norm; het afwijkende getal is een bevinding, geen via-punt bijgeschoven.
- Naden: geen (één been). Marker `kolen-gevra-laad` ligt 1,63 km van de lijn (snap kop 1,89 km; eigen Gevra-sporen ontbreken in OSM), marker Korba 0,69 km; beide onder de 5 km, de Gevra-naad boven de 0,5 km-richtwaarde (anker is niet het routeerpunt).
- `toets_knikken.py`: 1 knik, de omkering van 178,7 graden bij 22.3514, 82.6364 (wye Kusmunda), gemeld als TERUGLOOP. OSM-topologie dwingt die (zonder omkering vraagt de router 147-153 km); niet verholpen. `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom.
- Contract: json.load goed, versie 2, punt_formaat lonlat, modaliteit spoor, 106 punten.

**Toelichting:** geen stippel, geen haven-aanloop, geen vlucht, geen leiding, geen kopie (alleen spoor). Het wegblijven van de MGR in OSM verklaart een deel van de +59%; de rest zit in de wye-omkering (~2,4 km uit en terug) en de kop-snap.

**Lessen:** (1) een lijn die gedwongen door een wye omkeert is een eerlijke OSM-uitkomst voor een pit-head-MGR; een via-punt lost het niet op. (2) Draait `bak_stromen.sh` terwijl andere agenten de file aanvullen, dan kan bash een regel van andermans functie lezen en een vreemde melding (`line N: e: command not found`) geven nadat de bake al geslaagd is; het eigen json is dan volledig.
