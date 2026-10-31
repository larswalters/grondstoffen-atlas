# Routebrief (licht) · olie — Uzen → Atyrau → Samara (Kazachstan → Rusland)

**stroom-id:** `olie-uzen-samara` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) ·
**status:** gebakken
**Keten in één zin:** Mangystau-ruwe olie vanaf het KazTransOil-pompstation bij Uzen/Zhanaozen, per **leiding** (Uzen-Atyrau-Samara,
1016 mm, voorverwarmd) via het knooppunt Atyrau/PS-1 naar het Transneft-knooppunt in Samara-oblast; stoppunt daar (twee doorgetrokken
leidingbenen, geen zee, geen weg).
**Welke as van het verhaal:** *Kazachstans tweede exportader* naast de CPC: sectie Atyrau-Samara **11,134 Mt in 2025 ≈ 224 kb/d** (11,134 x 7,33 / 365;
KazTransOil) [1]; H1 2026 5,095 Mt [2]. Voor Uzen-Atyrau is geen eigen doorvoercijfer gevonden. Peiljaar 2025.

## 1 · Ketenkaart
```
Uzen-pompstation `ol-uzen-kop` ──(b1 leiding · Uzen-Atyrau, OSM way 274735631 · 698,9 km)──► Atyrau/PS-1 `ol-atyrau-ps1`
   ──(b2 leiding · Atyrau-Samara, OSM way 274735055 · 698,5 km)──► Transneft-knooppunt Samara-oblast `ol-samara-knoop` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Uzen → Atyrau/PS-1 | Uzen-Atyrau-Samara-leiding ("Узень - Атырау", KR-6), via Beyneu-regio en Kulsary | OSM 698,1 km (way) + 0,8 km slotstuk; gepubliceerd: samen met b2 "meer dan 1380 km", 1232 km in Kazachstan [3] | `maak_leidingbeen_olie_uzen_samara.py` (OSM-way 274735631, `--been-geojson`) | nee — 0,8 km recht slotstuk naar het anker, geen OSM |
| b2 | A | leiding | Atyrau/PS-1 → Transneft-knooppunt Samara-oblast | Atyrau-Samara ("Атырау - Самара", KazTransOil, 1016 mm), via Oeral-oblast naar Samara-oblast | OSM 698,1 km (way) + 0,4 km voorstuk; totaal b1+b2 1.397,4 km tegen ">1380" = +1,3% [3] | idem (OSM-way 274735055) | nee — 0,4 km recht voorstuk, geen OSM |

Totaal b1+b2: **1.397,4 km** gemeten, doorgetrokken (bindende haalbaarheidstoets: twee leidingbenen, geen stippel). Beide ways zijn grof gekarteerd (401
resp. 161 knopen, bron-tag een Utexas-kaart [4]); de km-toets steunt dus op de OSM-lengte tegen de gepubliceerde ">1380 km" en is een indicatie, geen ±15%-norm.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-uzen-kop` | kop van de leiding / pompstation | Uzen-pompstation (KazTransOil), ~3,7 km WNW van Zhanaozen, Mangystau | 43.3590, 52.8260 | [4][5] | bron-gelegd (z15 gezien: tankpark met ~15 witte tanks, pompstationgebouwen direct noordelijk van het punt, de stad Zhanaozen ZO; OSM-begin way 274735631 ligt op 4 m) |
| `ol-atyrau-ps1` | overslag leiding → leiding (pompstation-knoop) | Atyrau/PS-1 (KazTransOil), Atyrau-oblast | 47.1683, 51.8731 | letterlijk uit `olie-tengiz-novorossiysk.md` §4 (b1 via-punt 2) [4] | bron-gelegd (z15 hier opnieuw gezien: tankpark met ~17 witte tanks vlak ZW, leidingcorridor N-Z langs het punt; OSM-einde b1 op 0,77 km, begin b2 op 0,37 km) |
| `ol-samara-knoop` | eindknoop / stoppunt | Transneft-knooppunt (naamloos OSM-eind), gemeente Domashka, Kinelsky rayon, Samara-oblast, ~40 km ten oosten van Samara-stad | 52.9910, 50.5372 | [4][6] | aannemelijk (z15 gezien: twee grote tankparken, ~60 witte tanks, met pompgebouwen ertussen; naam van het station niet bevestigd, vijf OSM-oliewegen komen er samen) |

## 4 · Via-punten
Geen: een leidingbeen volgt de OSM-way zelf; er is geen corridorkeuze. Ter oriëntatie (niet gerouteerd) ligt de lijn bij 100 km op 43.955,53.397; 300 km 45.147,55.157 (Beyneu-regio);
600 km 47.049,53.086 (voor Atyrau); b2 bij 300 km 49.650,51.422 en 600 km 52.231,50.747.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Uzen-Atyrau-Samara-leiding | KazTransOil (KZ) / Transneft-Privolzhje (RU) | Mangystau-ruwe olie → Transneft-systeem | doorvoer Atyrau-Samara 11,134 Mt in 2025 ≈ 224 kb/d; ontwerp 15,75 Mt/j volgens ru.wikipedia, max 30 Mt | [1][3] |

## 6 · Stoppunt
De brief stopt bij het Transneft-knooppunt in Samara-oblast: vandaar loopt de olie in het Transneft-systeem verder (o.a. Druzhba naar Duitsland, 2,146 Mt in 2025 [1]), maar
geen bron legt deze lading aan één vervolgstation vast. Fase D/E vervallen.

## 7 · Open punten
- **Geen eigen volume voor Uzen-Atyrau** (alleen sectie Atyrau-Samara bekend); het volume is dus een ondergrens voor wat uit Uzen komt plus Atyrau-instroom.
- **Eindknoop is een naamloos Transneft-knooppunt** (OSM-eind, niet Samara-stad); het volume dat daar uitgaat is niet te splitsen per afnemer. Marker "aannemelijk".
- **Naad bij Atyrau:** de twee OSM-ways raken elkaar niet (1,14 km); beide recht gestikt op het reeds gelegde anker, geen OSM-geometrie (~0,8 + 0,4 km).
- **Grove geometrie:** knopen om de ~2-17 km (Utexas-kaartbron); lengte en tracé zijn schematisch, de leiding ligt ondergronds ("location=underground").
- **Risico:** drone-aanvallen op Transneft kunnen de doorvoer verstoren; de olie verlaat Samara in het Russische net (Ust-Luga, Novorossiysk, Druzhba), niet getekend.
- **Geen sitelaag-site** voor Uzen of Samara in `olie-sitelaag.json`; voorstel voor de sitelaag: Uzen-pompstation 43.3590,52.8260 (bron-gelegd).

## 8 · Bronnen
[1] KazTransOil JSC persbericht, 16-01-2026 — 2025: 47,033 Mt totaal, Atyrau-Samara 11,134 Mt (+7%), 2,146 Mt via Transneft naar Duitsland. https://kaztransoil.kz/en/press_centre/news/5629-kaztransoils-consolidated-crude-oil-transportation-volume-in-2025-totaled-47033-million-tonnes
[2] Baird Maritime, "KazTransOil sees busier H1 2026" — Atyrau-Samara 5,095 Mt in H1 2026. https://www.bairdmaritime.com/offshore/transport/kaztransoil-sees-busier-h1-2026-as-main-pipeline-oil-volumes-rise
[3] ru.wikipedia, "Нефтепровод Узень — Атырау — Самара" — >1380 km, 1232 km in Kazachstan, 15,75 Mt doorvoer, max 30 Mt, voorverwarmd, KazTransOil tot de grens, Transneft-Privolzhje in Rusland. https://ru.wikipedia.org/wiki/Нефтепровод_Узень_—_Атырау_—_Самара
[4] OpenStreetMap (ODbL) via de OSM-API, 2026-10-31 — way/274735631 ("Узень - Атырау", KR-6, operator KazTransOil, substance=oil, 1016 mm, 401 knopen, 698,1 km) en way/274735055 ("Атырау - Самара", name:en Atyrau - Samara, 161 knopen, 698,1 km); Atyrau-anker uit `olie-tengiz-novorossiysk.md`. https://www.openstreetmap.org/way/274735631
[5] Wikipedia (en), "Zhanaozen" — stadscoördinaat 43,3378 / 52,8553 (de Uzen-pompstationlocatie ligt ~3,7 km WNW ervan). https://en.wikipedia.org/wiki/Zhanaozen
[6] OpenStreetMap/Nominatim reverse (ODbL) — eindknoop 52.9910,50.5372 = Domashka selskoe poselenie, Kinelsky rayon, Samara-oblast. https://nominatim.openstreetmap.org
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-olie-uzen-samara-uzen-kop.png`, `-atyrau-ps1.png`, `-samara-knoop.png`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
`bash v2/tools/bak_stromen.sh olie-uzen-samara` (functie `bak_olie_uzen_samara`) -> `v2/data/stroomroute-olie-uzen-samara.json` (11,9 KB, contract versie 2, punt_formaat lonlat, 563 punten, 3 markers). Titel: "Olie · Uzen (Mangystau) → Atyrau → Samara (Uzen-Atyrau-Samara-leiding)".

| # | modaliteit | been | km | punten | stijl |
|---|---|---|---|---|---|
| b1 | leiding | Uzen → Atyrau/PS-1 (OSM way 274735631) | 698,9 | 402 | doorgetrokken |
| b2 | leiding | Atyrau/PS-1 → Transneft-knooppunt Samara-oblast (OSM way 274735055; aannemelijk: één bron voor het eindknooppunt) | 698,5 | 161 | doorgetrokken |

Totaal **1.397,4 km** tegen gepubliceerd "meer dan 1380 km" = +1,3% (indicatie: grof gekarteerde ways, Utexas-kaartbron). Naad b1/b2 = 0 m (beide recht gestikt op het anker Atyrau). Markers (alle drie op de lijn: 48 m, 0 m, 5 m): `ol-uzen-kop` 43.3590,52.8260 (bron-gelegd) · `ol-atyrau-ps1` 47.1683,51.8731 (bron-gelegd, hergebruik olie-tengiz-novorossiysk) · `ol-samara-knoop` 52.9910,50.5372 (aannemelijk).

**Recept:** geometrie met `python v2/tools/maak_leidingbeen_olie_uzen_samara.py --schrijf` (OSM-API, geen pbf) naar `olie-uzen-samara-leiding-uzen-atyrau.geojson` en `...-atyrau-samara.geojson` (beide FeatureCollection) in `v2/build-cache/ais/graaf/`; bake = twee `--been-geojson "leiding|…"` regels in reisvolgorde plus drie `--marker`. Geen router, geen via-punten, geen wegscan, geen slot behalve het zware slot voor de bake.

**Toelichting per leiding:** beide benen zijn volledige OSM-`man_made=pipeline`-ways (KazTransOil, 1016 mm), dus doorgetrokken; er is geen stippel, geen haven-aanloop, geen vlucht en geen letterlijke kopie. Het 0,8 km voorstuk-slotstuk (b1) en 0,4 km (b2) bij Atyrau is recht gestikt op het anker en is geen OSM-geometrie. De leiding ligt ondergronds; het tracé is schematisch.

**Toetsbevindingen:** `toets_knikken.py`: 9 knikken >= 60 gr, 1 omkering (173 gr, R 186 m bij 47.1650,51.8729 = de gestikte naad bij Atyrau, geen terugloop), 0 terugloop; de overige knikken zijn grof-OSM-bochten (o.a. 66,7 gr spike op 46.920,53.949). `toets_rechte_benen.py --min-km 5`: geen rij voor deze stroom.

**Lessen:** (1) een stroom van uitsluitend OSM-leiding bakt zonder zee of weg in een paar seconden; (2) de OSM-way-begin/-eindpunten kunnen enkele honderden meters van een gelegd anker liggen, het tool stikt recht op het anker en dat geeft een korte spike (hier de omkering bij Atyrau); (3) sitelaag heeft geen Uzen- of Samara-site: voorstel Uzen-pompstation 43.3590,52.8260.
