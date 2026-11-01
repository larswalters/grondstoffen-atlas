# Routebrief (licht) · Koper · Saindak → Balochistan-weg → Karachi (Pakistan)

**stroom-id:** `koper-saindak-karachi` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** blisterkoper van de Saindak-mijn en -smelter (Saindak Metals Ltd, MCC, Chagai, Balochistan) per **truck/trailer in Frontier Corps-convooi** over de Balochistan-snelwegen (N-40 via Dalbandin en Nushki, dan N-25 via Kalat, Surab, Khuzdar en Bela) naar de **Karachi-haven**; één truckbeen, stoppunt bij de haven (kade niet gebronnen).
**Welke as van het verhaal:** Pakistan, nieuw land en nieuwe corridor: Saindak-koper naar Chinese afnemers. Gemiddeld **ca. 15,8 kt blisterkoper per jaar** (Pakistan Monthly Review 2024) [1], EPZ-toestemming 12-13 kt per jaar [1]; blister is 96-99% koper, dus ruwweg 15 kt Cu per jaar (indicatie). Peiljaar: gemiddelde over de projectduur, geen kalenderjaar [1].

## 1 · Ketenkaart
Saindak-plant `cu-saindak-laad` ──(b1 truck · Saindak → N-40 (Dalbandin, Nushki) → N-25 (Kalat, Surab, Khuzdar, Bela) → Karachi · hemelsbreed 723 km, geen wegkm)──► Karachi-haven `cu-karachi-kade` ── stoppunt (kade niet gebronnen)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `cu-saindak-laad` → `cu-karachi-kade` | Saindak → N-40 (RCD-snelweg: Dalbandin, Nushki) → N-25 (Kalat, Surab, Khuzdar, Bela, Hub) → Karachi; route NIET gebronnen, wel: trailers in convooi onder Frontier Corps-escort, weging bij Hub en in Karachi [1][3] | hemelsbreed 723 km, geen wegkm; de ±15%-toets is indicatie. Wegtest (toets, wegscan): 1.199 km, geen bron | maak_stroombeen_weg (nieuw profiel, extract pakistan) | nee |

Geen zeebeen, geen haven-aanloop, geen afnemer: de brief stopt bij de haven (§6). Het spoor Saindak–Taftan (40 km) is verwaarloosd en niet in gebruik, dus geen spoorbeen [1]. Geen last-mile-been: het landbeen begint op het plantanker.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-saindak-laad` | mijn / smelter / laadplek | Saindak-plant (Saindak Metals Ltd, MCC), OSM-industrieterrein | 29.2421, 61.6125 | [1][5] | **bron-gelegd** (z15 gezien: verwerkingsterrein met gebouwencluster en conveyor, twee open pits N/NO, tailings en bekken ten zuiden; het punt ligt aan de noordrand van de installatie bij de pit-conveyor, 0,3 km van de gebouwen) |
| `cu-karachi-kade` | haven / stoppunt | Port of Karachi, Wikipedia-marker, Keamari-schiereiland | 24.8350, 66.9820 | [4] | **onzeker** (z15 gezien: havenschiereiland met kademuren en terreinstapels tussen het Keamari-geul en het oostbekken; de exacte blisterkoper-kade is niet te wijzen) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Gegeven (lat, lon); in het profiel (lon, lat). Eerste en laatste punt zijn de ankers.
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | N-40 ten oosten van Saindak (Taftan-weg) | 28.9583, 61.5869 | zonder dit punt vindt het wegtool geen pad: de 31-32 km plant → N-40 is `tertiary` (profiel met corridorKlassen tertiary); pint de N-40 |
| b1 | 2 | Dalbandin (N-40) | 28.8900, 64.4000 | pint de N-40 langs Dalbandin (customs-station [1]); sluit zuidelijke Makran-wegen via Panjgur uit |
| b1 | 3 | Nushki (N-40) | 29.5500, 66.0000 | pint de N-40 tot Nushki; laat daarna de keuze Quetta (N-25 noord) of Kalat (N-25 zuid) aan de router |

Router-uitkomst (profiel gedraaid 2026-11-01): Nushki → Kalat (0,7 km) → Surab (2,4) → Khuzdar (0,7) → Wadh (0,5) → Bela (3,6) → Hub (11,1) → Karachi; Quetta (87 km) en Mastung (43 km) worden gemeden. Segmenten: plant → N-40 32,6 · → Dalbandin 288,8 · → Nushki 198,3 · → Karachi 684,6 km; snaps 0,00 tot 0,30 km.

## 5 · Verwerkingsknopen
Geen: de Saindak-smelter (blisterkoper, 96-99% Cu, in blokken [1]) is het begin van de keten; blister blijft blister tot de haven.

## 6 · Stoppunt
De brief stopt in de Karachi-haven: bronnen noemen "Karachi port" en China als bestemming, maar geen benoemde raffinaderij, haven-kade of schip [1][3]. Fase D en E vervallen.

## 7 · Open punten
- **Wegkilometers niet gebronnen:** hemelsbreed 723 km, geen wegkm; de gemeten 1.199 km (omwegfactor 1,66, via Dalbandin en Nushki) is een OSM-lengte, geen bedrijfsopgave. Mine → Taftan 40 km en Saindak → Dalbandin zijn alleen als losse afstanden genoemd, niet als routelengte [1].
- **Corridor niet gebronnen:** FC-convooi, weging bij Hub [1]. Nushki → Kalat → Surab is de keuze van de router; een zoekresultaat noemt aanvallen op convooien op de Quetta-Taftan-weg (Mastung) en op de Quetta-Karachi-weg (niet geopend), wat ook op een route via Quetta kan wijzen (87 km van de gemeten lijn).
- **Haven Karachi of Port Qasim:** [1] schrijft "Karachi port (Port Qasim, per EPZ records)" en noemt een zending van juli 2018 naar Port Qasim; het ontwerp en de toets kozen Karachi-haven (marker uit Wikipedia). Kade onbekend; Port Qasim ligt 40 km oostelijker (hemelsbreed), dus de lijn eindigt kort. Aanname, geen bewijs.
- **Mijn kan stilvallen:** juli 2026 waarschuwde Saindak Metals voor stop binnen een maand door onveilige wegen [2][3]; de regering beloofde extra beveiliging; stand daarna niet gevonden. De weg is echt, de lading onzeker.
- **Volume:** 15,8 kt blister is een gemiddelde over de levensduur; recent jaarvolume niet gevonden; destinatie China niet gekwantificeerd [3].
- **Sitelaag:** Saindak staat niet in `koper-sitelaag.json`; centraal te beoordelen (anker `cu-saindak-laad` kan als site).
- **Smelter/afnemer in China:** niet genoemd.

## 8 · Bronnen
[1] Pakistan Monthly Review, "Saindak" (Volume 6, No. 5, 2024): 15.810 t blister per jaar gemiddeld, EPZ 12-13 kt, trailers in FC-convooi naar Karachi port (Port Qasim), spoor Saindak-Taftan verwaarloosd, https://pakistanmonthlyreview.com/?p=5254
[2] Miningmx / Financial Times, "Insurgency threatens major China-backed Pakistan mine", 2026-07-15, https://www.miningmx.com/news/gold/65908-insurgency-threatens-major-china-backed-pakistan-mine/
[3] Daily Pakistan, "Balochistan violence endangers $750 million copper export pipeline to China", 2026-07-16 (vrijwel alle output naar China; wegvervoer grootste kwetsbaarheid), https://en.dailypakistan.com.pk/16-Jul-2026/balochistan-violence-endangers-750-million-copper-export-pipeline-to-china
[4] Wikipedia, "Port of Karachi" (coördinaat 24.835, 66.982), https://en.wikipedia.org/wiki/Port_of_Karachi
[5] OSM-industrieterrein Saindak (29.2421, 61.6125), via het ontwerp en de haalbaarheidstoets; Wikipedia, "Port Qasim" (24.7667, 67.3333), https://en.wikipedia.org/wiki/Port_Qasim
[6] Zoekresultaten, niet geopend (403): Tribune, "Pak steps up security for Saindak mine", https://tribune.com.pk/story/2618485/pak-steps-up-security-for-saindak-mine · OpIndia, convooiaanval, https://www.opindia.com/news-updates/pakistan-baloch-rebels-attack-truck-convoy-carrying-copper-7-army-personnel-killed-and-11-injured/
[7] Satellietblik `v2/tools/sat_check.py`, Esri World Imagery z14 en z15, 2026-11-01, in `v2/build-cache/satcheck/`: `sat-koper-saindak-karachi-cu-saindak-laad.png`, `...-laad15.png`, `sat-koper-saindak-karachi-cu-karachi-kade.png`, `...-kade15.png`
[8] Haalbaarheidstoets `koper-saindak-karachi` (2026-11-01): enkel truckbeen, profiel pakistan, corridorKlassen tertiary, vensterKm 75, proef 1.199 km
[9] Wegscan `python v2/tools/wegscan_puur.py --profiel koper-saindak-karachi-saindak-karachi` (2026-11-01): 1.199,2 km, snaps max 0,30 km, `v2/build-cache/ais/graaf/koper-saindak-karachi-weg-saindak-karachi.geojson`
[10] Zoekresultaten (profit.pakistantoday.com.pk 2026-07-15, engineeringnews.co.za 2026-07-16): regering belooft extra beveiliging, exploitant sluit stop niet uit

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
**Bestand:** `v2/data/stroomroute-koper-saindak-karachi.json` (versie 2, lonlat, 109,0 KB) · **functie:** `bak_koper_saindak_karachi` in `v2/tools/bak_stromen.sh` · **titel:** Koper · Saindak (Pakistan) → Karachi.

| # | modaliteit | been | km | punten | stippel |
|---|---|---|---|---|---|
| b1 | truck | blisterkoper Saindak-plant → Karachi-haven (N-40 Dalbandin/Nushki → N-25 Kalat/Surab/Khuzdar/Bela/Hub; FC-convooi, corridor niet gebronnen, geen wegkm gepubliceerd) | 1.199,5 | 5.608 | nee (doorgetrokken, gemeten) |

Totaal 1.199,5 km, 2 markers: `cu-saindak-laad` (29.2421, 61.6125, bron-gelegd) en `cu-karachi-kade` (24.8350, 66.9820, onzeker).

**Recept:** profiel `koper-saindak-karachi-saindak-karachi` in `maak_stroombeen_weg.py` (extract pakistan, vensterKm 75, corridorKlassen tertiary, refs N-40/N-25), gescand met `wegscan_puur.py --profiel`; geojson `v2/build-cache/ais/graaf/koper-saindak-karachi-weg-saindak-karachi.geojson` als `--been-geojson "truck|…"`. Geen zee, geen haven-aanloop, geen kopie, geen lucht, geen leiding, geen stippel.

**Toets:** de brief geeft geen echte wegkm (hemelsbreed 723 km), dus de +-15%-toets is indicatie: 1.199,5 km = omwegfactor 1,66 over de N-40/N-25, geen waarde om tegen te toetsen. Naden: één been, geen naad. Markers liggen op de lijneinden (0 km). `toets_knikken`: 14 knikken >= 60 gr, 0 omkeringen, 0 terugloop (alle spikes 9 tot 174 m, wegtopologie bij Nushki en Karachi-haven); `toets_rechte_benen`: het been is geen rechte lijn.

**Lessen:** (1) het via-punt op de N-40 ten oosten van Saindak was nodig omdat de 31 km plant -> N-40 `tertiary` is (corridorKlassen). (2) Quetta (87 km) en Mastung (43 km) liggen naast de lijn: de corridor Nushki -> Kalat -> Surab is de keuze van de router, niet gebronnen. (3) De Karachi-kade is een Wikipedia-marker; Port Qasim (EPZ-records) ligt 40 km oostelijker. (4) Saindak staat niet in `koper-sitelaag.json`: centraal beoordelen.
