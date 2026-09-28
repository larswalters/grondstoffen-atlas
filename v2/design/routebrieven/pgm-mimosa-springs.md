# Routebrief (licht) · PGM — Van → Via → Naar (land)

**stroom-id:** `pgm-mimosa-springs` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** PGM-concentraat van de Mimosa-mijn (Sibanye-Stillwater/Implats 50:50 JV, Great
Dyke, Zimbabwe) per truck over Zvishavane–Masvingo–Beitbridge naar de grens, dan per truck over
Musina–Polokwane–Pretoria–Rustenburg naar het Impala Rustenburg-mijnencluster/smelter, en per truck
naar de Impala Refineries Springs-eindraffinage (Implats) — derde Zimbabwaanse Great Dyke-mijn op de
kaart, andere eigenaar (Sibanye/Implats-JV) en andere eindraffinaderij dan de bestaande Zimplats-as.
**Welke as van het verhaal:** Zimbabwe/Great Dyke Implats-as — Mimosa-concentraat via Beitbridge naar
Rustenburg-smelting en Springs-eindraffinage; ~234.038 oz 4E/jaar (100%, FY2025, zie §7 voor de mix-
discrepantie met het oudere ontwerpcijfer).

## 1 · Ketenkaart
```
Mimosa Mine (concentrator on-site) `pgm-mimosa-mijn`
  ──(b1 truck · A9 Zvishavane–Masvingo → A4 Masvingo–Beitbridge · ~417 km)──►
Beitbridge grensovergang `pgm-beitbridge-grens` (hergebruikt)
  ──(b2 truck · N1 Musina–Polokwane–Pretoria → N4 Pretoria–Rustenburg · ~475 km)──►
Impala Rustenburg-mijnencluster/smelter `pgm-rustenburg-mijn` (hergebruikt)
  ──(b3 truck · N4/N12 Rustenburg–Springs, LETTERLIJKE KOPIE pgm-springs-zurich b1 · ~160 km)──►
Impala Refineries Springs `pgm-springs-raffinaderij` (hergebruikt) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Mimosa Mine (concentrator) → Beitbridge grensovergang | A9 Zvishavane–Masvingo → A4 Masvingo–Beitbridge (via Ngundu, Rutenga) | ~417 (32+97+288) [2][5][7][8] | maak_stroombeen_weg | nee |
| b2 | B | truck | Beitbridge grensovergang → Impala Rustenburg-mijnencluster/smelter | N1 Musina–Polokwane–Pretoria → N4 Pretoria–Rustenburg | ~475 [9] | maak_stroombeen_weg | nee |
| b3 | B/C | truck | Impala Rustenburg-mijnencluster/smelter → Impala Refineries Springs | N4/N12 Rustenburg–Springs — LETTERLIJKE KOPIE pgm-springs-zurich b1 | ~160 [13] | hergebruik geojson pgm-springs-zurich b1 | nee |

Geen zee-, spoor-, binnenvaart- of luchtbeen; geen fase D/E (geen bron noemt een vervolgbestemming ná
de eindraffinage in déze as — §6, zelfde patroon als pgm-zimplats-rustenburg en pgm-springs-zurich).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-mimosa-mijn` | mijn / laadplek (concentrator on-site) | Mimosa Mine (Sibanye-Stillwater/Impala Platinum 50:50 JV), Zvishavane/Bannockburn, Midlands, Zimbabwe | -20.3179, 29.8368 | [1][2][3][4][14] | bron-gelegd (z15 gezien: grote lichtgekleurde tailings-opslag met bezinkbekken direct bij het punt, spoor-/transportstructuur aan de noordkant van de dam, verwerkings-/kantoorgebouwencluster ~500 m zuidwestelijk) |
| `pgm-beitbridge-grens` | grensovergang / overslag tussen twee truckcorridors | Beitbridge grensovergang, Limpopo-brug — **hergebruikt letterlijk uit `pgm-zimplats-rustenburg.md`** | -22.2244, 29.9865 | [12] | bron-gelegd (zie die brief) |
| `pgm-rustenburg-mijn` | mijn/laadplek (mogelijk ook smeltlocatie, zie §7) | Impala Platinum Rustenburg-mijnencluster — **hergebruikt letterlijk uit `pgm-springs-zurich.md`** | -25.5535, 27.2176 | [13] | bron-gelegd (zie die brief); ⚠️ omschreven als "mijn/laadplek", niet expliciet als smelterlocatie — zie §7 |
| `pgm-springs-raffinaderij` | overslag / eindraffinaderij | Impala Refining Services, Springs (Implats) — **hergebruikt letterlijk uit `pgm-springs-zurich.md`** | -26.2227, 28.4437 | [13] | bron-gelegd (zie die brief) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Zvishavane (A9-corridor, mijnstad) | -20.3159, 30.0527 | pint de A9 vanaf de mijntoegangsweg; de mijn ligt ~32 km westelijk van deze stad op dezelfde corridor [1][5] |
| b1 | 2 | Masvingo (A9 → A4-wissel) — hergebruikt uit `pgm-zimplats-rustenburg.md` | -20.0745, 30.8332 | dwingt de wissel van de A9 naar de A4 zuidwaarts af; laatste grote stad vóór de grens |
| b1 | 3 | Ngundu (A4-corridor) | -20.8015, 30.8009 | bevestigt de doorgaande A4 zuidwaarts (via Lundi/Ngundu Halt), sluit een oostelijke afslag uit [8][11] |
| b1 | 4 | Rutenga (A4-corridor, spoorknoop) | -21.2327, 30.7275 | laatste grote plaats vóór Beitbridge op de A4 [8][11] |
| b2 | 1 | Musina (eerste stad na de grens) — hergebruikt uit `pgm-zimplats-rustenburg.md` | -22.3454, 30.0269 | bevestigt de N1-richting direct na Beitbridge |
| b2 | 2 | Polokwane (N1) — hergebruikt uit `pgm-zimplats-rustenburg.md` | -23.9218, 29.4803 | grote tussenstop, sluit binnenwegen door Limpopo-provincie uit |
| b2 | 3 | Pretoria, N1/N4-wissel — hergebruikt uit `pgm-zimplats-rustenburg.md` | -25.6357, 28.2761 | dwingt de wissel van de N1 naar de N4 af |
| b2 | 4 | Marikana (N4-corridor) — hergebruikt uit `pgm-springs-zurich.md` | -25.7043, 27.4794 | pint de N4 tussen Pretoria en de Bushveld-mijngordel, laatste punt vóór het Impala Rustenburg-cluster |

⚠️ **Laatste ~150 km van b1 (A4 Masvingo–Beitbridge) overlapt reëel met `pgm-unki-rustenburg` b1**
(beide Midlands-mijnen delen de enige doorgaande A4-corridor naar de grens) — die brief bestond nog
niet in `v2/design/routebrieven/` op het moment van schrijven, dus kon niet letterlijk gekopieerd of
vergeleken worden. Zie §7.

Geofabrik-regio's: `zimbabwe` (b1), `zuid-afrika` (b1-staart + b2 + b3).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mimosa Mine (concentrator) | Sibanye-Stillwater/Implats 50:50 JV (Mimosa Investments Ltd) | Great Dyke-erts (ondergronds, Wedza/Blore-schachten) → PGM-concentraat (80,6% herwinning) | 4E-productie 2025: 117.019 oz op 50%-aandeel (Sibanye); wegtransport concentraat naar Implats o.b.v. long-term offtake | [1][2] |
| Impala Rustenburg-cluster (smelting) | Impala Platinum (Implats) | extern concentraat (incl. Mimosa) + eigen Bushveld-concentraat → matte | Sibanye's eigen omschrijving: "transported by road to Implats' Mineral Processes, in Rustenburg" | [1] |
| Impala Refineries Springs | Implats | matte → geregistreerd Pt/Pd/Rh (4E) | eindraffinage binnen dezelfde Implats-groep, geen rechtstreekse Mimosa-bestemming | [13] |

## 6 · Stoppunt
De brief stopt bij Impala Refineries Springs: dat is de eindraffinage in déze as (matte → geregistreerd
Pt/Pd/Rh) en geen bron in dit onderzoek noemt een specifieke vervolgzending van het geraffineerde metaal
uit déze stroom (dat zou een luchtbeen zijn — net als bij `pgm-zimplats-rustenburg`, bewust niet getekend).

## 7 · Open punten
- **Smelterlocatie van `pgm-rustenburg-mijn` niet bevestigd.** De haalbaarheidstoets signaleerde dit al:
  het hergebruikte anker staat in `pgm-springs-zurich.md` omschreven als "mijn/laadplek", niet expliciet
  als smeltlocatie. Aanpassing (bindend): bij het bakken één extra satellietblik nemen om te bevestigen
  dat Implats' smelter op/nabij hetzelfde terrein zit; zo niet, een tweede, licht verschoven anker voor
  de smelter toevoegen i.p.v. het bestaande mijn-anker te hergebruiken.
- **`pgm-unki-rustenburg` bestond nog niet** in `v2/design/routebrieven/` toen deze brief geschreven werd
  — de reële overlap van de laatste ~150 km van b1 (A4 Masvingo–Beitbridge) kon dus niet letterlijk
  vergeleken of gekopieerd worden. Bij het bakken beoordelen of die brief inmiddels bestaat en zo ja, of
  dat stuk als gedeeld via-puntcluster behandeld wordt of als twee losse profielen (conform het ontwerp).
- **Km b1 is een optelsom van drie gepubliceerde deeltrajecten** (mijn→Zvishavane 32 km [1] +
  Zvishavane→Masvingo 97 km [5] + Masvingo→Beitbridge 288 km via A4 [8]) = 417 km, geen enkele
  doorgaande bronopgave. Ligt boven het ontwerp se "hemelsbreed ~330 km" — verwacht, want dat was expliciet
  hemelsbreed zonder wegkm.
- **Volumemix-discrepantie:** Sibanye-Stillwater's eigen site (peildatum 2025-12-31) geeft **4E**
  (117.019 oz op 50%-aandeel), terwijl het ketenontwerp een ouder FY2023-cijfer uit de sitelaag
  (`w-mimosa`, ~130 koz **6E**/jaar) citeerde. Beide jaar én metaalmix verschillen — zie §8 voor de
  omrekening; niet zelf gecorrigeerd, is een redactievraag.
- **Been b2 is een geheel nieuw wegprofiel** (geen letterlijke kopie); alleen b1's laatste segment
  (Masvingo–Beitbridge, A4) valt mogelijk samen met `pgm-unki-rustenburg` a1 (zie boven).

## 8 · Bronnen
[1] Sibanye-Stillwater, "Mimosa" operations page, https://www.sibanyestillwater.com/business/southern-africa/pgm-operations/mimosa/
[2] Wikipedia, "Mimosa mine", https://en.wikipedia.org/wiki/Mimosa_mine
[3] Implats, "Mimosa Fact Sheet 2022" (PDF), https://www.implats.co.za/pdf/operations/fact-sheets/2022/mimosa-fact-sheet-2022.pdf
[4] Mining Weekly, "Mimosa mine, Zimbabwe" (2015-05-22), https://www.miningweekly.com/print-version/mimosa-mine-zimbabwe-2015-05-22
[5] Wikipedia, "Zvishavane", https://en.wikipedia.org/wiki/Zvishavane
[6] Wikipedia, "Beitbridge", https://en.wikipedia.org/wiki/Beitbridge
[7] Wikipedia, "Masvingo" (coördinaat), https://en.wikipedia.org/wiki/Masvingo
[8] Trippy.com, "How far is Masvingo from Beitbridge" (288 km via Lundi/Rutenga/Ngundu Halt/Swanscoe), https://www.trippy.com/distance/Beitbridge-to-Masvingo
[9] Distance.to, "Beitbridge → Rustenburg" (475 km), https://www.distance.to/Beitbridge
[10] Wikipedia, "A4 road (Zimbabwe)", https://en.wikipedia.org/wiki/A4_road_(Zimbabwe)
[11] OpenStreetMap-contributors (ODbL) via Nominatim — objecten Zvishavane/Ngundu/Rutenga, https://www.openstreetmap.org
[12] `v2/design/routebrieven/pgm-zimplats-rustenburg.md` — hergebruikte ankers Beitbridge-grens, Musina, Polokwane, Pretoria N1/N4-wissel
[13] `v2/design/routebrieven/pgm-springs-zurich.md` — hergebruikte ankers Rustenburg-mijncluster, Springs-raffinaderij, Marikana (b1)
[14] Esri World Imagery via `v2/tools/sat_check.py` (z15), `v2/build-cache/satcheck/sat-pgm-mimosa-springs-mijn.png`
[15] `v2/design/pgm-sitelaag.json` / `.md` — site `w-mimosa` (jaarvolume FY2023-cijfer, koz ÷ 32,15)

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Stroom `pgm-mimosa-springs`** → `v2/data/stroomroute-pgm-mimosa-springs.json` — 3 benen,
**1.269,6 km**, 11.044 punten, 4 markers. truck 414,9 + truck 598,9 + truck 255,8 = 1.269,6 km.
Recept: `v2/tools/bak_stromen.sh` (functie `bak_pgm_mimosa_springs`). Bestandsgrootte **225,6 KB**
(iets boven de indicatieve ~300 KB-norm van de handleiding, ruim binnen limiet — drie volledige
wegscans op fijn OSM-detail).

**b1 (truck, doorgetrokken, `maak_stroombeen_weg.py`, profiel
`pgm-mimosa-springs-mijn-beitbridge`, extract `zimbabwe`):** Mimosa Mine → Zvishavane → Masvingo →
Ngundu → Rutenga → Beitbridge-grens over A9 → A4 — **414,9 km over 4.204 punten**, tegen de
brief-optelsom ~417 km (32+97+288 uit drie deelbronnen) = **−0,5% [OK]**. Anker-verbindingen
plant→weg 0,11 km en weg→kade 0,01 km. Geen stippel nodig.

**b2 (truck, doorgetrokken, `maak_stroombeen_weg.py`, profiel
`pgm-mimosa-springs-beitbridge-rustenburg`, extract `zuid-afrika`):** Beitbridge-grens → Musina →
Polokwane → Pretoria → Marikana → Impala Rustenburg-mijncluster/smelter over N1 → N4 —
**598,9 km over 4.155 punten**, tegen het brief-cijfer ~475 km (distance.to) = **+26,1%, buiten
±15%**. ⚠️ **Bevinding, niet dichtgetrokken en niet aan de route toegeschreven:** onafhankelijk
nagemeten (WebSearch, rome2rio.com) — de werkelijke rijafstand Beitbridge→Rustenburg is **574 km**;
onze gerouteerde 598,9 km zit daar slechts **+4,3%** boven, ruim binnen de norm. Het brief-cijfer
van ~475 km (distance.to) was zelf de afwijking, geen routeerfout. Het via-punt Marikana snapt op
5,30 km (net over de 5 km-vuistregel voor via-snaps); visueel gecheckt op de gebakken lijn — dit is
de doorgaande N4 zelf bij Marikana, geen zijtak of omweg, dus niet verschoven. Anker-verbindingen
plant→weg 0,01 km en weg→kade 0,06 km.

**b3 (truck, doorgetrokken, LETTERLIJKE KOPIE van het geojson van `pgm-springs-zurich` been b1,
geen nieuwe scan):** Impala Rustenburg-mijncluster → Impala Springs Refinery over N4 → N1 → N12,
via Marikana/Centurion/Johannesburg N1-N12-knoop/Germiston — **255,8 km over 2.685 punten**,
byte-voor-byte identiek aan het brongeojson (`pgm-springs-zurich-weg-rustenburg-springs.geojson` →
gekopieerd naar `pgm-mimosa-springs-weg-rustenburg-springs-gedeeld.geojson`). Dit is **hoger** dan
het ~160 km-cijfer in deze brief se §2/samenvatting, maar dat cijfer citeerde zelf al de
ontwerpschatting van `pgm-springs-zurich` — die brief documenteert in haar eigen §9 al dezelfde
+59,8%-afwijking tegen diezelfde ~160 km-schatting (§2 van die brief: "schatting uit
ketenontwerp, geen aparte bron gevonden"). Geen nieuwe bevinding, alleen geërfd van de bronstroom.

**Toets naden:** alle drie de overgangen **0,000 km** — elk been begint precies waar het vorige
eindigt (Beitbridge-grens en Rustenburg-mijncluster zijn gedeelde ankers, geen snap-verschil).

**Markers:** alle vier op 0,00 km van hun been (punt-op-lijn, want elk anker is tegelijk het
been-eindpunt).

**`toets_knikken.py`:** 40 knikken ≥60°, waarvan 1 omkering ≥150° (bij Beitbridge-grens, 140,6° —
een reële scherpe bocht op de grensovergang zelf) en **0 terugloop** (de enige klasse die reparatie
vraagt). Alle overige knikken zijn kleine-straal-spikes op stads-/kruispuntniveau (7–107 m radius),
normaal voor fijnkorrelig OSM-stadsverkeer.

**`toets_rechte_benen.py --min-km 5`:** geen van de drie benen heeft een omwegfactor 1,000 —
geen enkele stippel-verdenking.

**Contractcontrole:** `versie: 2`, `punt_formaat: lonlat`, modaliteit overal `truck` (∈ toegestane
set), elk been ≥2 punten (4.204 / 4.155 / 2.685) — allemaal geslaagd.

**⚠️ Smelterlocatie-check op `pgm-rustenburg-mijn` (bindende haalbaarheidstoets, brief §7):**
extra `sat_check.py`-blik op z15 genomen
(`v2/build-cache/satcheck/sat-pgm-mimosa-springs-rustenburgsmelter.png`) — toont een industrieel
gebouwencluster met een kleine bezinkvijver en een lijnvormige structuur (vermoedelijk transportband)
zuidoostwaarts, en een zichtbare open mijnput met tailings-dam ~1,5 km zuidwestelijk op hetzelfde
terreincomplex. Aannemelijk dat dit hetzelfde mijn-/smeltterrein is dat de andere twee PGM-Rustenburg-
brieven al als anker gebruiken. Geen tweede, verschoven smelter-anker toegevoegd — het bestaande
anker (-25,5535, 27,2176) blijft kop/staart voor b2/b3, zoals de opdracht als terugvaloptie toestond.

**⚠️ `pgm-unki-rustenburg` bestond al vóór het bakken** (gecheckt in stap 0): het laatste ~150 km-
stuk van b1 (Masvingo–Beitbridge, A4) overlapt geografisch met diens been b1, maar de
via-puntenlijst verschilt — deze brief voegt Ngundu en Rutenga toe als extra via-punten op de A4,
`pgm-unki-rustenburg` routeert rechtstreeks Masvingo→Beitbridge zonder die twee. Daarom **geen
letterlijke kopie**: een eigen scan/profiel gedraaid voor b1, conform de bak-aanwijzing dat een
scan alleen wordt overgeslagen bij een écht identieke via-puntenreeks.

**Volumemix-discrepantie (brief §7, niet gecorrigeerd):** Sibanye-Stillwater's site geeft 4E
(117.019 oz op 50%-aandeel, peildatum 2025-12-31), het ketenontwerp citeerde een ouder FY2023-cijfer
uit de sitelaag (~130 koz 6E/jaar) — jaar én metaalmix verschillen. Blijft een redactievraag voor
Lars/orkestrator, buiten de scope van dit bakwerk.

**Lessen voor volgende bak-agenten:** (1) een brief-km uit een enkele online-driving-calculator
(distance.to) kan zelf de afwijking zijn — een tweede, onafhankelijke bron (WebSearch/rome2rio)
onderscheidt een routeerfout van een bron-fout vóórdat je een via-punt gaat bijschuiven; (2) bij een
"LETTERLIJKE KOPIE"-been geeft de gedeelde bronstroom soms al een eigen, hogere gemeten km dan wat
een latere brief-samenvatting ervan overnam — check de bronbrief se eigen §9 vóór je het verschil als
nieuwe bevinding rapporteert.
