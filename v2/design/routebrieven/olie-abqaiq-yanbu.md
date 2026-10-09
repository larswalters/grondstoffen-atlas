# Routebrief (licht) · olie — Abqaiq (Saoedi-Arabië) → Yanbu (Saoedi-Arabië, Rode Zee)

**stroom-id:** `olie-abqaiq-yanbu` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** Arabische ruwe olie vanaf de Abqaiq-stabilisatiefabriek (Ghawar), per **leiding** (de Oost-West-pijpleiding
"Petroline", Saudi Aramco, ~1.200 km dwars door het Arabisch Schiereiland) naar de Yanbu-exportterminal aan de Rode Zee. Eén been,
geen zeebeen: geen bron koppelt een lading aan een bestemming na Yanbu.
**Welke as van het verhaal:** *de Saoedische Hormuz-bypass* — het zusje van de Habshan–Fujairah-leiding (`olie-habshan-chiba`).
Capaciteit 5.000 kb/d (2018), na de ombouw van de tweede (NGL-)buis in maart 2026 opgegeven als 7.000 kb/d [1][4]; voor de stillegging
van 11-09-2026 liep ~4.000 kb/d via de leiding naar Yanbu (peiljaar 2026, Reuters) [5]. Dit is **dezelfde Abqaiq-kop als
`olie-rastanura-zhoushan`, maar een andere as**: die gaat via Ras Tanura de Golf en Hormuz in, deze gaat west naar de Rode Zee. De twee
benen delen geen enkel stuk; alleen het kopanker ligt dicht bij elkaar (zie §3).

## 1 · Ketenkaart
```
Abqaiq Stabilization Plant `ol-abqaiq-stab` ──(b1 leiding · Petroline / East-West Pipeline, OSM-way 56" ·
    ~1.200 km gepubliceerd; kleine stippels bij een kaarteringsgat (~1 km) en bij de laatste ~5,5 km naar de terminal)──►
Yanbu-exportterminal `ol-yanbu-term` (Yanbu Industrial City / King Fahd Industrial Port, Rode Zee) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Abqaiq Stabilization Plant → Yanbu-exportterminal | East-West Crude Oil Pipeline / Petroline (Saudi Aramco), 56"/1420 mm, ondergronds | 1.201 [1]; eigen OSM-meting: 44,9 + 1.166,2 km way + 0,9 km gat + 5,5 km slot ≈ 1.217,5 km (+1,4%) [2] | OSM-ways (`man_made=pipeline`, `name="East-West Pipeline"`, `substance=oil`, gcc-staten): **doorgetrokken** over 1.211 km | gedeeltelijk — twee stippels: (i) ~0,9 km OSM-kaarteringsgat (25.6537,49.3970 → 25.6565,49.4056); (ii) ~5,5 km slot van het way-einde (23.9793,38.2688) naar het terminalanker (OSM kent daar alleen onbenoemde leidingen zonder `substance`) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-abqaiq-stab` | kop van de leiding / stabilisatiefabriek | Abqaiq Stabilization Plant (Saudi Aramco) | 25.9286, 49.6858 | [3][9] — letterlijk `w-abqaiq` uit `olie-sitelaag.json` | aannemelijk (z15 gezien: het punt ligt midden in een groot terrein dat Esri als vervaagd laag-resolutievlak toont (geen details te zien; het ligt naast de stad en past bij het Abqaiq-complex, maar het beeld bewijst het niet) met de woonstad Abqaiq direct NW; het OSM-pijplijnbegin ligt 0,38 km verderop op 25.9256, 49.6840 — dus binnen dezelfde omheining) |
| `ol-yanbu-term` | eindpunt van de leiding / exportterminal | Yanbu-exportterminal (Petroline-terminus) | 23.9330, 38.2500 | [8][9] — letterlijk `w-yanbu` uit `olie-sitelaag.json` | aannemelijk (z15 gezien: punt aan de kop van een steiger met een ligplaats en twee lange loodsen aan land, in het exportgebied van Yanbu; of díe steiger ruwe olie laadt is niet te zien. De zichtbare olie-steigers/tankenpark liggen 1–3 km WNW, de T-steiger met tanker van de Aramco **South Terminal (Al Muajjiz)** op 23.9165, 38.2840 — 3,9 km ZO, zie §7) |

## 4 · Via-punten
Geen. Een leidingbeen volgt de OSM-way; er bestaat geen corridorkeuze. De geometrie is de way zelf (3 ways + één gat, §2).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Abqaiq Stabilization Plant | Saudi Aramco | veldolie Ghawar → gestabiliseerde ruwe olie | ~7.000 kb/d verwerking | [9] |
| Yanbu (South Terminal Al Muajjiz + North Terminal) | Saudi Aramco | leiding → opslag → tanker (en 3 raffinaderijen: SAMREF, YASREF, Aramco Yanbu, tot ~1.000 kb/d) | nominaal 4.500 kb/d laden (Noord 1.500 + Zuid 3.000), effectief ~4.000 kb/d [1][4][6] | [1][4][6] |

## 6 · Stoppunt
De brief stopt op de Yanbu-exportterminal: Yanbu is het laadpunt aan de Rode Zee en geen bron noemt een afnemer of raffinaderij voor
een specifieke lading (Wikipedia/Reuters: richting Azië via Bab el-Mandeb en Europa via Suez, maar op aggregaatniveau [1][5]); een
zeebeen zou dus een verzonnen bestemming zijn. Fase D/E vervallen.

## 7 · Open punten
- **Volume niet cargo-specifiek.** ~4.000 kb/d is wat vóór 11-09-2026 via de leiding naar Yanbu ging (Reuters 24-09-2026) [5]; de 7.000 kb/d
  is een capaciteitsclaim na de ombouw (2026), geen gemeten doorvoer. Een tweede bron voor beide ontbreekt (Wikipedia citeert dezelfde pers).
- **Actuele stand: onderbroken.** Drone-aanvallen op pompstations legden de leiding stil op 11-09-2026; herstart 22-09-2026 op laag volume,
  6–8 weken tot vol vermogen; tankerbeladingen in Yanbu nog niet hervat op 24-09-2026 [1][5]. De keten is dus recent bewezen kwetsbaar.
- **Terminalanker onzeker.** Het sitelaag-anker `w-yanbu` (23.9330, 38.2500) ligt op een steigerkop die op het beeld niet als olielaadplek
  herkenbaar is; de Aramco-berthbeschrijving (South Terminal: drie ligplaatsen 101–103, tot 500.000 DWT) past op de T-steiger op 23.9165,
  38.2840 [6]. De Noord-terminal heb ik niet kunnen plaatsen (de steigers bij 24.0735, 38.0555 zijn de commerciële haven Yanbu Al-Bahr).
  Voorstel centraal: de sitelaag en dit anker samen verleggen naar 23.9165, 38.2840 (dan wordt het slotstuk ~7,2 km in plaats van 5,5 km).
  Ik heb het sitelaag-anker letterlijk gehouden, zoals de opdracht eist.
- **Abqaiq-anker conflict met een andere brief.** `olie-rastanura-zhoushan` gebruikt voor zijn marker `ol-abqaiq` op 25.9400, 49.6600
  (2,9 km NW, in het woongebied); dit anker (`ol-abqaiq-stab`, de sitelaag-waarde) is een eigen id zodat de twee markers niet botsen.
- **OSM-gaten.** Het gat van 0,9 km en het slot van 5,5 km zijn niet bevestigd als echt gat in de leiding; OSM heeft daar alleen
  onbenoemde, onbepaalde leidingen (bijv. ways 231599982/231599984, geen `substance`). Ook ligt de parallelle buis (way 1495004023,
  `substance=gas`, 1.166,2 km, de ombouw-NGL-buis) bewust niet in dit been: één lijn per corridor.
- **Pyosmium geblokkeerd op deze machine** — de ways komen uit Overpass (mirror maps.mail.ru) van 2026-10-09, niet uit de gcc-staten-pbf.

## 8 · Bronnen
[1] Wikipedia, "East–West Crude Oil Pipeline" — 1.201 km, 56"+48", 5 Mbbl/d (2018), 7 Mbbl/d na ombouw 2026, Yanbu North/South 4,5 Mbbl/d, stillegging 11-09-2026, herstart 22-09-2026. https://en.wikipedia.org/wiki/East%E2%80%93West_Crude_Oil_Pipeline
[2] OpenStreetMap/Overpass (ODbL), mirror maps.mail.ru, 2026-10-09 — ways 799372434 (0,5 km) + 1044430260 (44,5 km) + 54729631 (1.166,2 km, 564 knopen), `man_made=pipeline`, `name=East-West Pipeline`, `substance=oil`, `operator=Saudi Aramco` op 54729631; parallelle gasbuis 1495004023. https://www.openstreetmap.org
[3] Wikipedia, "Abqaiq" (via sitelaag): 25°55'43"N 49°41'09"E. https://en.wikipedia.org/wiki/Abqaiq
[4] wisdomandboats (Substack), "Yanbu Analysis: The East-West Pipeline, Port Congestion, & Actual Export Capacity" — 5 Mbbl/d + ~2 Mbbl/d omgebouwde buis, Yanbu-exportcapaciteit 4–4,5 Mbbl/d, SAMREF ~400 / YASREF ~405 / Aramco Yanbu 240 kb/d. https://wisdomandboats.substack.com/p/yanbu-analysis-the-east-west-pipeline
[5] Reuters via Baird Maritime, 24-09-2026 — "Yanbu tanker loadings yet to resume despite Saudi pipeline restart": ~4 mln b/d via de leiding, pompstations beschadigd, tankers nog niet hervat. https://www.bairdmaritime.com/shipping/tankers/yanbu-tanker-loadings-yet-to-resume-despite-saudi-pipeline-restart
[6] Argus Media, "Yanbu gives Aramco limited option for rerouting crude" — nominaal 4,5 mln b/d (Noord 1,5 / Zuid 3,0), effectief ~4 mln b/d; Aramco Yanbu-terminalbeschrijving (North berths 61–64, South berths 101–103, South = Al Muajjiz). https://www.argusmedia.com/en/news-and-insights/latest-market-news/2798868-yanbu-gives-aramco-limited-option-for-rerouting-crude
[7] OpenStreetMap/Nominatim, "محطة المعجيز للنفط الخام" (Al Muajjiz crude terminal, landuse 23.8235, 38.4143) — opslagterrein, niet het laadpunt. https://nominatim.openstreetmap.org
[8] Wikipedia, "Yanbu" — Yanbu Commercial Port en King Fahd Industrial Port, Yanbu Industrial City. https://en.wikipedia.org/wiki/Yanbu
[9] `v2/design/olie-sitelaag.json` (`w-abqaiq`, `w-yanbu`; bronnen B5–B9: Wikipedia, CRS-rapport, wisdomandboats/ENR) — de twee ankers, letterlijk hergebruikt.
[10] `v2/design/routebrieven/olie-rastanura-zhoushan.md` — de Abqaiq-as naar Ras Tanura (afbakening, ander kopanker).
[11] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15), `v2/build-cache/satcheck/`: `sat-olie-abqaiq-yanbu-abqaiq.png`, `-leiding-kop.png`, `-yanbu.png`, `-leiding-eind.png`, `-yanbu-terminals.png`, `-yanbu-south.png`, `-yanbu-north.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)

**Bestand:** `v2/data/stroomroute-olie-abqaiq-yanbu.json` (12,8 KB, versie 2, `lonlat`) · **functie:** `bak_olie_abqaiq_yanbu` in `v2/tools/bak_stromen.sh` · **titel:** "Olie · Abqaiq → Petroline → Yanbu (Rode Zee)". Geen profiel in `maak_stroombeen_weg.py` (geen wegbeen), geen extracts, geen schaduw-run.

| # | modaliteit | km | naad naar vorig been | stippel | been |
|---|---|---|---|---|---|
| 1 | leiding | 44,9 | (kop) | nee | Petroline segment 1: Abqaiq → vóór het gat (OSM 799372434 + 1044430260, 41 punten) |
| 2 | leiding | 0,9 | 0,00 | **ja** | OSM-kaarteringsgat (25.6537,49.3970 → 25.6565,49.4056) |
| 3 | leiding | 1.166,2 | 0,00 | nee | Petroline segment 2: ná het gat → Yanbu (OSM 54729631, 564 punten) |
| 4 | leiding | 5,5 | 0,00 | **ja** | slot naar de exportterminal (23.9793,38.2688 → 23.9330,38.2500) |

**Totaal 1.217,5 km** tegen gepubliceerd 1.201 km (+1,4%, binnen ±15%; Wikipedia-lengte is een pijpleidingslengte, geen wegkm). 609 punten, 2 markers. Alle naden 0,00 km (de beengeojson sluiten op elkaar en op de stippels).

**Markers:** Abqaiq Stabilization Plant (25.9286, 49.6858) ligt 0,38 km van het eerste lijnpunt (OSM-pijplijnbegin binnen dezelfde omheining; markerafstand binnen de ~0,5 km-norm); Yanbu-exportterminal (23.9330, 38.2500) ligt op 0,0 km van de lijn (stippeleinde).

**Recept:** twee OSM-leidingstukken (Overpass-mirror maps.mail.ru, 2026-10-09, `man_made=pipeline`, `substance=oil`) vooraf gestikt tot twee geojson-LineStrings in `v2/build-cache/ais/graaf/olie-abqaiq-yanbu-leiding-{abqaiq-gat,gat-yanbu}.geojson`; `hecht_marnet.py route` met `--been-geojson` / `--stippel` / `--been-geojson` / `--stippel`, geen router, geen zeeknoop, geen haven-aanloop (geen zeebeen).

**Toelichting stippels.** (i) ~0,9 km: OSM kent de leiding niet doorlopend; dit is een kaarteringsgat, niet bevestigd als echt gat. (ii) 5,5 km slot: OSM heeft rond Yanbu alleen onbenoemde leidingen zonder oil-`substance`; het wegen/leiding-einde sluit rechtstreeks op het sitelaag-terminalanker, "last mile, geen net op deze korrel". Beide staan als stippel met reden (rechte stippel-met-reden in `toets_rechte_benen.py`: been 4 omwegfactor 1,002 komt in de lijst, de doorgetrokken delen niet; het 0,9 km-gat valt onder de 5 km-drempel).

**Toets.** `toets_knikken.py`: 10 knikken >= 60 gr, 0 omkeringen, 0 terugloop. Zeven "spikes" zitten in de eerste 44,9 km binnen ~0,5 km van het Abqaiq-complex (R 13-23 m, OSM-geometrie van de leiding op het fabrieksterrein: lusjes in de aansluitpijpen), de overige drie zijn OSM-kleinschaligheid (R 71-1576 m); niets om te repareren. `json.load`: versie 2, `punt_formaat` lonlat, modaliteit alleen `leiding`, elk been >= 2 punten, 12,8 KB.

**Open (uit §7, ongewijzigd, centraal):** (a) terminalanker: de South Terminal (T-steiger, Al Muajjiz) op 23.9165, 38.2840 past beter dan het sitelaag-anker w-yanbu; sitelaag + anker samen verleggen is een centrale beslissing (slot wordt dan ~7,2 km); (b) het Abqaiq-anker wijkt 2,9 km af van marker `ol-abqaiq` in `olie-rastanura-zhoushan` (25.9400, 49.6600) — sitelaag en die brief niet gewijzigd; (c) volume niet cargo-specifiek, peiljaar 2026, keten recent stilgelegd (11-09-2026) en herstart (22-09-2026) — niet in de lijnstijl, wel in de brief; (d) de ways zijn niet uit de gcc-staten-pbf gekruiscontroleerd (pyosmium geblokkeerd).

**Lessen.** (1) Een leidingketen van 1 been gaat in één bake-aanroep: de geometrie wordt vooraf gestikt, de functie is een lijst `--been-geojson` + korte `--stippel`. (2) Een slotstuk waar OSM alleen onbenoemde leidingen heeft is een stippel "last mile, geen net op deze korrel", geen reden om de hele leiding te schrappen.
