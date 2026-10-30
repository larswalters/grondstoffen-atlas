# Routebrief (licht) · gas — Permian-gas via GCX (Crockett County) → Agua Dulce (Texas)

**stroom-id:** `gas-waha-aguadulce` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) ·
**status:** gebakken
**Keten in één zin:** Permian-schaliegas gaat via de Gulf Coast Express (GCX, Kinder Morgan Texas Pipeline, 42/48 inch) van de Waha-hub bij Coyanosa naar het Agua Dulce-knooppunt bij Corpus Christi; getekend is het gekarteerde stuk, 570,8 km van 31.0794,-101.5847 (Crockett County) tot 27.7461,-97.8000 (Nueces County), plus 1,4 km stippel naar Valley Crossing CS1.
**Welke as van het verhaal:** *Permian-gas naar de Zuid-Texas-uitvoerhub* (bronzijde van de VS-export naar Mexico en LNG). Volume: capaciteit 2,0 bcf/d ≈ 20,7 bcm/j (eigen omrekening; GEM 20,5), in bedrijf 25 sept. 2019 [1][4]; uitbreiding naar 2,55 bcf/d ≈ 26,4 bcm/j gemeld voor medio 2026, niet bevestigd [3]. Werkelijke doorzet niet gevonden.

## 1 · Ketenkaart
```
Waha-hub bij Coyanosa (Pecos County; hub, geen gelegd anker)  -- OPEN PUNT, niet getekend, ca. 145 km hemelsbreed, 36 inch
  ··(westelijk stuk niet in OSM onder de GCX-naam)··
GCX-begin gekarteerd `gas-gcx-begin` 31.0794,-101.5847 (Crockett County)
  ──(b1 leiding · GCX 42/48" · OSM ref=GCX, 19 ways · 570,8 km, doorgetrokken)──►
GCX-einde `gas-gcx-aguadulce-einde` 27.7461,-97.8000 (Nueces County)
  ──(b2 leiding · korte stippel 1,4 km · interconnect naar Valley Crossing)──► `gas-aguadulce-cs1` 27.7486,-97.8143 (hergebruik) — stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | leiding | `gas-gcx-begin` → `gas-gcx-aguadulce-einde` | Gulf Coast Express Pipeline, ref GCX, 42" (48" laatste 115 km), Kinder Morgan | **570,8 OSM**; gepubliceerd 447,5 mijl ≈ 720 km [2][5] = −20,7%; 365 mijl 42" ≈ 587 km [5] = −2,8% | vooraf gestikt geojson (`maak_leidingbeen_gas_waha_aguadulce.py`, FeatureCollection, 1.201 punten) | nee |
| b2 | C | leiding | `gas-gcx-aguadulce-einde` → `gas-aguadulce-cs1` | afleverpunt Enbridge Valley Crossing [2] | hemelsbreed 1,4 km, geen wegkm | 1 × `--stippel` | ja: interconnect niet gekarteerd, geen net op deze korrel (last mile < 2 km) |

OSM-ways (Overpass 2026-10-30 + OSM-API), ref=GCX, west → oost: 1104116970 (0 km, begin) · 1104120534 · 1104120532 · 1098316526 · 1098316368 · 1098316366 · 1098316364 · 1098316360 · 1098271341 · 1098271340 · 1066747742 · 1080984111 · 1080984060 · 1065312957 · 1059834555 · 1059840794 · 1059833143 · 1059839951 (48") · 1070599581 (48", 85,5 km, eindigt 27.7461,-97.8000). Naden 0-51 m, geen naad > 5 km.
**Weglaten:** de 32 korte stompjes en dubbele ways (< 0,3 km, 12,75"/16" bij kleppen), **ref PHP** (Permian Highway, 1104117804), **ref WHL** (Whistler, 1104120317, begint op dezelfde plek 31.0794,-101.5849) en Hill Country (1104117815) [7]: selecteren op ref=GCX, niet op diameter.
Het ontbrekende westen is volgens [5][6] het **36 inch-stuk van 82 mijl ≈ 132 km** vanaf Waha: dat verklaart waarom OSM pas bij het 42 inch-begin de GCX-ref draagt. Onbenoemde way 1479926878 (99,8 km, 31.1851,-101.8854 → 31.2348,-102.8775, geen ref/substance) is **niet** gebruikt: koppeling aan GCX onbevestigd [8].
Totaal getekend 572,2 km tegen ca. 720 km gepubliceerd (79%, indicatie, geen wegkm); stippel 1,4 km = 0,3%.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-gcx-begin` | begin gekarteerde leiding (geen site) | OSM-leidingbegin ref=GCX, Crockett County | 31.0794, -101.5847 | [7][9] | aannemelijk (z15 gezien: kale struikvlakte, een rechte lichte servituutstrook loopt noordwest door het punt heen en houdt hier niet op; geen faciliteit; het begin is de kartering, niet de leiding) |
| `gas-gcx-aguadulce-einde` | eind GCX in OSM (afleverstation, onbevestigd) | OSM-leidingeinde ref=GCX, Nueces County | 27.7461, -97.8000 | [7] | aannemelijk (z16 gezien: klein omheind grindterrein met leidingapparatuur in een akker, ten noorden van een landweg; dat het GCX-station is staat alleen in de OSM-geometrie) |
| `gas-aguadulce-cs1` | stoppunt, begin Valley Crossing (hergebruik) | Valley Crossing Compressor Station 1, Agua Dulce | 27.7486, -97.8143 | [10][11] | bron-gelegd in `gas-aguadulce-tuxpan.md` (opnieuw gezien z16: omheind terrein met acht compressortreinen); marker staat al in de zusterstroom |

Niet gelegd: **Waha-hub** (OSM-plaatsnode 31.2719,-103.0840 en ontwerpkandidaat 31.2606,-103.0981 zijn dorps-/hubcentroïden, geen faciliteit). Sitelaag `gas-sitelaag.json` heeft geen Waha- of GCX-site.

## 4 · Via-punten
Niet van toepassing: leidingbenen (OSM-way of stippel), geen corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| GCX-hoofdleiding | Gulf Coast Express Pipeline LLC (Kinder Morgan 34% + operator, DCP, ArcLight/Targa-affiliate) | Waha-ontvangstpunten (o.a. EPNG, DCP, Enterprise, Northern Natural) → Agua Dulce-afleverpunten (o.a. Valley Crossing, NET Mexico, HPL) | 2,0 bcf/d ≈ 20,7 bcm/j; 214.280 pk compressie | [2][4] |

## 6 · Stoppunt
De brief stopt op Valley Crossing CS1: GCX levert er volgens [2] direct af aan Enbridge Valley Crossing, en daar neemt `gas-aguadulce-tuxpan` het over, samen Permian → Tuxpan. Geen bron legt dit gas aan één afnemer; fase D en E vervallen. Het gas dat naar HPL, Tejas of Southcross gaat is geen onderdeel van deze stroom.

## 7 · Open punten
- **Westelijke 36 inch-stuk (ca. 132-150 km) is niet getekend:** niet in OSM onder GCX; geen stippel naar een niet gelegd Waha. Het servituut loopt op de satelliet wel door voorbij het OSM-begin [9]. De lijn begint dus 145 km (hemelsbreed) oostelijk van Waha en is 21% korter dan de gepubliceerde 720 km; de titel noemt Crockett County, niet Waha.
- **Waha-hub-anker ontbreekt:** hub, geen faciliteit; ontvangstpunten (EPNG-header, Trans-Pecos, DCP) zijn niet gelegd.
- **Einde 1,4 km oostelijker dan CS1:** de stippel is schematisch; het werkelijke interconnect-punt is niet gevonden. Het grindterrein op 27.7461,-97.8000 is niet als station bevestigd.
- **Doorzet onbekend:** 20,7 bcm/j is capaciteit (2019); de uitbreiding naar 2,55 bcf/d (2026) is een bericht, geen bevestiging [3]. GEM noemt 36 en 42 inch en Coyanosa als begin [4].
- **Whistler (ref WHL) begint op dezelfde coördinaat als GCX** en loopt 107,6 km naast het eerste stuk; een bak die op diameter selecteert krijgt twee leidingen door elkaar.
- Een grote compressor 1,6 km NW van CS1 (27.755,-97.819) is andermans terrein: niet gebruikt.

## 8 · Bronnen
[1] Kinder Morgan, "Gulf Coast Express Pipeline Placed in Service Ahead of Schedule", 24 sept. 2019 — 2,0 bcf/d, Waha → Agua Dulce, in bedrijf 25 sept. 2019. https://ir.kindermorgan.com/news/news-details/2019/Gulf-Coast-Express-Pipeline-Placed-in-Service-Ahead-of-Schedule/default.aspx
[2] NS Energy, "Gulf Coast Express Pipeline" — 447,5 mijl (720 km) 42", 214.280 pk, ontvangst- en afleverpunten incl. Enbridge Valley Crossing. https://www.nsenergybusiness.com/projects/gulf-coast-express-pipeline-waha-texas/
[3] Energies Media, "Kinder Morgan expansion work on the Gulf Coast" — uitbreiding +550 MMcf/d naar 2,55 bcf/d, medio 2026. https://energiesmedia.com/kinder-morgan-expansion-work-on-the-gulf-coast/
[4] Global Energy Monitor wiki, "Gulf Coast Express Pipeline" — Coyanosa → Agua Dulce, 36/42 inch, ca. 20,5 bcm/j, 2019. https://www.gem.wiki/Gulf_Coast_Express_Pipeline
[5] Oil & Gas Journal, "Gulf Coast Express construction to start", 3 jan. 2018 — 82 mijl 36" + 365 mijl 42" = 447 mijl, Waha-hub bij Coyanosa → Agua Dulce, 1,92 bcf/d. https://www.ogj.com/pipelines-transportation/pipelines/article/17295981/gulf-coast-express-construction-to-start
[6] Oil & Gas 360, "$1.7 billion Gulf Coast Express pipeline gets FID" — FID 21 dec. 2017, zelfde lengtes, shippers. https://www.oilandgas360.com/1-7-billion-gulf-coast-express-pipeline-gets-fid-apache-makes-agreement-incremental-takeaway/
[7] OpenStreetMap (ODbL), 19 ways ref=GCX (man_made=pipeline, Kinder Morgan Texas Pipeline LLC, substance gas), PHP 1104117804, WHL 1104120317, Hill Country 1104117815; Overpass en OSM-API 2026-10-30 + us-texas-extract. https://www.openstreetmap.org/way/1070599581
[8] OpenStreetMap (ODbL), way 1479926878 (man_made=pipeline zonder naam/ref). https://www.openstreetmap.org/way/1479926878
[9] Nominatim (OSM), reverse 2026-10-30: 31.0794,-101.5847 = Crockett County; 31.2606,-103.0981 = Pecos County; 27.7461,-97.8000 = Nueces County. https://nominatim.openstreetmap.org
[10] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-gas-waha-aguadulce-begin.png`, `-einde.png`, `-cs1.png`.
[11] Zusterbrief `v2/design/routebrieven/gas-aguadulce-tuxpan.md` — CS1 27.7486,-97.8143 bron-gelegd (TCEQ-order 2024-0247-AIR-E).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)
**Bestand:** `v2/data/stroomroute-gas-waha-aguadulce.json` (26,1 KB, versie 2, lonlat) · **2 benen · 572,2 km · 1.203 punten · 2 markers** · naden 0,005 km (b1 → b2).
Recept: `bak_gas_waha_aguadulce()` in `v2/tools/bak_stromen.sh`; geometrie b1 via `v2/tools/maak_leidingbeen_gas_waha_aguadulce.py` (OSM-API, 19 ways ref=GCX, FeatureCollection) → `v2/build-cache/ais/graaf/gas-waha-aguadulce-leiding-gcx.geojson`; b2 = rechte `--stippel`. Geen profiel in `maak_stroombeen_weg.py` (geen wegbeen).
| # | modaliteit | km gemeten | km brief | afwijking | stijl |
|---|---|---|---|---|---|
| b1 | leiding (GCX 42/48 inch, ref=GCX) | 570,8 | 720 (447,5 mijl); 587 (365 mijl 42 inch) | -20,7% / -2,8% | doorgetrokken |
| b2 | leiding (interconnect GCX-einde → CS1) | 1,4 | niet gepubliceerd | n.v.t. | stippel |
Markers: `gas-gcx-begin` (31.0794, -101.5847; 2 m van de lijn) en `gas-gcx-aguadulce-einde` (27.7461, -97.8000; 0 m). Beide aannemelijk (OSM-leidinguiteinden). CS1 heeft bewust geen marker (staat in `gas-aguadulce-tuxpan`).
**Toelichting stippel b2:** 1,4 km hemelsbreed, "interconnect niet gekarteerd, geen net op deze korrel"; 0,3% van de lengte. De lijn eindigt op CS1 als stoppunt.
**Afwijking van het ontwerp:** het id noemt Waha, maar de lijn begint 145 km (hemelsbreed) oostelijker in Crockett County; het westelijke 36 inch-stuk (ca. 132-150 km) staat niet onder GCX in OSM en is niet getekend (geen stippel naar een niet gelegd Waha). De titel noemt daarom Crockett County. Daardoor is b1 21% korter dan de gepubliceerde 720 km; het 42 inch-deel (587 km) sluit op -2,8%.
**Toetsen:** naden 0,005 km (< 5 km); markers ≤ 2 m van hun lijn; `toets_knikken.py` 13 knikken >= 60 graden (OSM-pijplijnbochten bij kleppen, spike), 0 omkeringen, 0 terugloop; `toets_rechte_benen.py` meldt deze stroom niet; json.load ok, versie 2, lonlat, modaliteit leiding, elk been >= 2 punten, 26,1 KB; `bak_stromen.sh` blijft LF (0 CRLF).
**Lessen:** selecteer GCX op ref, niet op diameter (Whistler WHL begint op dezelfde coördinaat); een ontbrekend westelijk stuk blijft open in plaats van een stippel naar een hubcentroïde; het id kan een hub noemen die het OSM-begin niet haalt: zet het werkelijke begin in de titel.
