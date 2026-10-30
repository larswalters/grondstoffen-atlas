# Routebrief (licht) · diamant — Aikhal → Mirny (Rusland)

**stroom-id:** `diamant-aikhal-mirny` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** Ruwe diamant van Alrosa's Aikhal-divisie (Jubilee-put, Aikhal-GOK) gaat per truck van de Jubilee-put naar het GOK-terrein bij Aikhal en vandaar over de regionale weg 98K-004 (via Tsjernysjevski) naar het Mir-complex/sorteercentrum in Mirny (aannemelijk: één bron voor de bestemming, vervoersmiddel onbevestigd).
**Welke as van het verhaal:** *de toevoertrechter van de grootste Alrosa-divisie naar het sorteercentrum.* Aikhal MPD >30% van de Alrosa-productie (2017) [3]; Jubilee-put 10,16 Mct + Aikhal ondergronds 2,48 Mct (2017) [3]; sitelaag `w-aikhal` 9,5 Mct/j (orde-grootte, onzeker). Eenheid Mct/j; waarde per karaat gemengd (edelsteen en near-gem), niet in het gewicht.

## BINDENDE aanpassing (haalbaarheidstoets, toegepast)
b1 eindigt op het GOK-complex (65.9322, 111.4890), niet op het kandidaatpunt 65.9269,111.4972 (dat ligt IN de open Aikhal-put). Geen via-punt bij Udachny: de 98K-004 passeert Udachny op ca. 60 km. b2 eindigt op het bestaande anker `dia-mirny-mijn` (Mir-put), niet op een apart sorteercentrum (niet gelokaliseerd).

## 1 · Ketenkaart
```
Jubilee-put `dia-aikhal-jubilee` ──(b1 truck · mijn-/servicewegen · 32,0 km gemeten, hemelsbreed 14,6)──►
Aikhal-GOK `dia-aikhal-gok` ──(b2 truck · 98K-004 via Tsjernysjevski · 464,7 km gemeten, Wikipedia 469, aannemelijk)──►
Mir-complex / sorteercentrum Mirny `dia-mirny-mijn` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Jubilee-put → Aikhal-GOK | mijn- en servicewegen Jubilee – Aikhal (unclassified/service), geen corridorkeuze; ertstransport, geen diamanttransport | hemelsbreed 14,6 km, geen wegkm; Wikipedia noemt put "20 km van Aykhal" [2] (geen wegkm); toets gemeten 32,0 [7] | maak_stroombeen_weg (rusland-verrehoosten) | nee |
| b2 | B | truck | Aikhal-GOK → Mir-complex, Mirny | regionale weg 98K-004 (Anabar / Mirny–Udachny) via Tsjernysjevski; aannemelijk: één bron voor de bestemming, vervoersmiddel onbevestigd | 469 km (Wikipedia "469 km from Mirny" [1], wegkm niet bevestigd); toets 464,7 (-0,9%) [7] | maak_stroombeen_weg, 4 via-punten | nee |

Fase C, D en E vervallen: geen bron voor een vervolgbeen uit Mirny binnen deze keten (de vervolgstromen `diamant-mirny-mumbai` en `diamant-mirny-smolensk` beginnen op hetzelfde anker).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-aikhal-jubilee` | mijn / laadplek | Jubilee-put (Yubileynaya), Aikhal MPD | 66.0010, 111.2315 | [2][7] | bron-gelegd (z14 gezien: grote terrassenput met kruis op het groene meertje in de put, afvalbergen en mijnwegen eromheen; OSM-groeve 66.0010, Wikipedia 66.0003,111.2317 binnen 0,1 km) |
| `dia-aikhal-gok` | verwerking / overslag | Aikhal-GOK-complex (ertsverwerking), Aykhal | 65.9322, 111.4890 | [1][7] | aannemelijk (z15 gezien: industrieel complex met schoorstenen en gebouwen, stad Aykhal met rode flats direct NO, open put ZO; één bron voor de functie, niet voor het exacte gebouw). NIET het Wikipedia-punt 65.9269,111.4972: dat ligt IN de put |
| `dia-mirny-mijn` | mijn + sorteercentrum / bestemming | Mir-put / Alrosa-complex, Mirny (**hergebruikt**) | 62.5258, 113.9842 | `diamant-mirny-mumbai.md` [4][5] | bron-gelegd (overgenomen; z15 opnieuw gezien: rand van de open put met bebouwing; sorteercentrum niet apart te onderscheiden) |

## 4 · Via-punten (b2, reisvolgorde, alle OP de 98K-004, snap <= 5 m [7])
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | 98K-004, ca. 116 km ten zuiden van Aikhal | 65.1424, 112.4535 | pint de route op de doorgaande weg i.p.v. de dorps- en mijnwegen rond Aikhal/Udachny; afrit Udachny blijft ca. 60 km opzij |
| b2 | 2 | 98K-004, Sadynski-nasleg, midden van het traject | 64.1385, 112.5788 | houdt de route op de hoofdweg in het dunbevolkte middenstuk (km 232) |
| b2 | 3 | 98K-004 bij Tsjernysjevski | 63.0090, 112.5236 | corridorkeuze: de weg gaat via Tsjernysjevski (92 km van Mirny [6]) en niet via Udachny (km 365) |
| b2 | 4 | 98K-004, Mirny-aanloop | 62.7979, 113.3721 | laatste stuk op de doorgaande weg vóór de stad, niet door een stadscentrum (km 419) |

Segmenten (km): GOK → 1 116,0 · → 2 116,0 · → 3 133,2 · → 4 53,4 · → Mirny 46,2 (som 464,8). Via-punt 4 ligt in het Mirny-district, niet in het stadscentrum.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Aikhal-GOK (verwerking) | Alrosa Aikhal MPD | erts → ruwe diamant | 12,6 Mct (2017: Jubilee 10,16 + ondergronds 2,48) | [3] |
| Diamond Sorting Center, Mirny | Alrosa | ruw → gesorteerd ruw | niet gebrond | [4][8] |

## 6 · Stoppunt
De brief stopt in Mirny: Aikhal-ruw gaat volgens Alrosa naar het sorteercentrum [8] dat in Mirny staat [4]; wat daarna naar markten vliegt is `diamant-mirny-mumbai` en `diamant-mirny-smolensk` (fase C/D/E vervallen).

## 7 · Open punten
- **Geen bron voor het vervoersmiddel Aikhal → Mirny** (weg of vlucht via Aykhal Airport [1]): alleen de bestemming is gebrond. Wegbeen is daarom aannemelijk; geen vlucht getekend.
- **Sorteercentrum Mirny niet gelokaliseerd** (OSM, Nominatim): het anker is mijn plus sortering op het Mir-complex.
- **b1 is ertstransport over mijnwegen**, geen diamanttransport; gemeten 32,0 km tegen hemelsbreed 14,6 en Wikipedia 20 km (geen wegkm): de km-toets is indicatie.
- **b2 wegkm niet bevestigd**: 469 km is Wikipedia's afstand Aykhal-Mirny [1]; een winterweg-/ijsweg-variant is niet onderzocht.
- **Volume** 9,5 Mct/j is orde-grootte (sitelaag); peiljaar 2017 voor 12,6 Mct [3]; Mirny-deel van de Aikhal-productie niet gebrond.
- **GOK-gebouw** niet individueel gezien; site-niveau volstaat. De Aikhal-sitelaagcoordinaat (65.955, 111.51) ligt in de stad, niet op het GOK-terrein (centraal gelijktrekken).

## 8 · Bronnen
[1] en.wikipedia, "Aykhal" (469 km van Mirny; Aykhal Airport; 65.9333, 111.5). https://en.wikipedia.org/wiki/Aykhal
[2] en.wikipedia, "Yubileynaya diamond mine" (66.0003, 111.2317; 20 km van Aykhal; 3,6 Mct/j capaciteit). https://en.wikipedia.org/wiki/Yubileynaya_diamond_mine
[3] en.wikipedia, "Alrosa" (Aikhal MPD >30% van Alrosa 2017; Jubilee 10,16 Mct, Aikhal ondergronds 2,48 Mct, tabel 2017). https://en.wikipedia.org/wiki/Alrosa
[4] AFP via Arab News, 2019-07-08 — "Russia digs for diamonds to ensure supremacy in global market" (Mirny-sorteercentrum onder directeur Popov; sortering in Mirny). https://www.arabnews.com/business/russia-digs-for-diamonds-to-ensure-supremacy-in-global-market-1522276
[5] `v2/design/routebrieven/diamant-mirny-mumbai.md` (anker `dia-mirny-mijn`, Mir-put 62.5258,113.9842).
[6] en.wikipedia, "Chernyshevsky, Sakha Republic" (92 km van Mirny, op de weg Lensk-Mirny; Udachny 508 km van Mirny). https://en.wikipedia.org/wiki/Chernyshevsky,_Sakha_Republic
[7] OSM (ODbL), Geofabrik `rusland-verrehoosten`, eigen PBF-scan (haalbaarheidstoets, 2026-10-30): b1 32,0 km, b2 464,7 km (414 km op primary 98K-004); Esri World Imagery via `v2/tools/sat_check.py` (`v2/build-cache/satcheck/sat-diamant-aikhal-mirny-jubilee.png`, `-gok.png`, `-mir.png`). Nominatim reverse voor de plaatsnamen bij de via-punten.
[8] Israeli Diamond Industry, 2017-07-23 — "Alrosa finds two huge diamonds in Yakutia" (Aikhal-diamanten gaan naar Alrosa's Diamond Sorting Center). https://en.israelidiamond.co.il/?p=6719

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
**Bestand:** `v2/data/stroomroute-diamant-aikhal-mirny.json` (43,9 KB, versie 2, `lonlat`) · functie `bak_diamant_aikhal_mirny` in `v2/tools/bak_stromen.sh` · profielen `diamant-aikhal-mirny-jubilee-gok` en `diamant-aikhal-mirny-gok-mirny` in `v2/tools/maak_stroombeen_weg.py` · tussenuitvoer `v2/build-cache/ais/graaf/diamant-aikhal-mirny-weg-jubilee-gok.geojson` en `-weg-gok-mirny.geojson`.

| # | modaliteit | been | km gebakken | brief | naad |
|---|---|---|---|---|---|
| 1 | truck | Jubilee-put → Aikhal-GOK (mijn- en servicewegen) | 32,1 | hemelsbreed 14,6 / Wikipedia 20 (geen wegkm) | - |
| 2 | truck | Aikhal-GOK → Mir-complex Mirny (98K-004 via Tsjernysjevski) | 464,8 | 469 (Wikipedia, -0,9%) | 0,00 km |

Totaal 496,9 km, 2.111 punten, 3 markers (`dia-aikhal-jubilee`, `dia-aikhal-gok`, `dia-mirny-mijn`), allen 0,0 km van de lijn. Geen stippel, geen zee, geen haven-aanloop, geen lucht, geen leiding, geen letterlijke kopie.

**Recept.** b1: wegscan `rusland-verrehoosten`, alleen de ankers als via-punten, vensterKm 20, eindKlassen residential/service/tertiary/unclassified; ankersnap 0,02 en 0,04 km. b2: wegscan zelfde extract, 4 via-punten OP de 98K-004 (alle snaps 0,00 km), `refs ["98К-004"]` met Cyrillische К, vensterKm 90; 1 keerlus gesnoeid (0,02 km bij 65.9344,111.5258). Daarna `bak_stromen.sh diamant-aikhal-mirny` (hecht_marnet, twee `--been-geojson`, drie markers).

**Toets (handleiding §5).** b2: 464,7 km tegen 469 = -0,9% (norm ±15%, OK). b1: 32,0 km tegen de 20 km van Wikipedia = +60%; dat is geen wegkm en hemelsbreed is 14,6 km, dus de ±15%-toets is hier indicatie, geen norm (zoals in de brief al aangekondigd). Naad b1 → b2 0,00 km; markers 0,0 km van hun lijn. `toets_knikken`: 11 knikken, 0 terugloop; de scherpe punten liggen rond Aykhal en bij de Mir-put (spikes van 2-47 m straal, geen terugloop). Geen omwegfactor 1,000 (`toets_rechte_benen`). Bestand 43,9 KB, `json.load` slaagt, `versie` 2, `punt_formaat` lonlat, modaliteiten alleen `truck`.

**Toelichting.**
- *Aannemelijk:* alleen de bestemming (Aikhal-ruw naar het sorteercentrum Mirny [8][4]) is gebrond; het vervoersmiddel Aikhal → Mirny (weg of vlucht via Aykhal Airport) niet. Daarom een doorgetrokken wegbeen met "aannemelijk: één bron voor de bestemming, vervoersmiddel onbevestigd" in de beennaam; geen luchtbeen getekend (zou een tweede aanname zijn zonder vrachtbron).
- *b1* is ertstransport over mijnwegen, geen diamanttransport; 32,0 km tegen hemelsbreed 14,6 is een omwegfactor van 2,2, wat past bij een mijnweg rond de Aikhal-put en de stad. Geen wegkm gepubliceerd.
- *b2* begint op het GOK-anker, loopt eerst door de rand van Aykhal (spikes rond 65.935,111.53) en pakt dan de 98K-004; de geometrie volgt Tsjernysjevski (via-punt 3), niet Udachny.
- *Ankers:* `dia-aikhal-gok` blijft aannemelijk (functie en complex herkend op z15, niet het exacte gebouw); `dia-mirny-mijn` letterlijk uit `diamant-mirny-mumbai`; geen nieuwe satellietrun nodig, de beelden `v2/build-cache/satcheck/sat-diamant-aikhal-mirny-{jubilee,gok,mir}.png` staan er al.

**Lessen / voor centraal.**
- Sitelaag `w-aikhal` (65.955,111.51) ligt in de stad Aykhal, ca. 2,7 km van het GOK-anker en niet op het GOK-terrein: centraal gelijktrekken als dezelfde faciliteit (niet door deze bak-agent gewijzigd).
- Het id noemt Mirny als eindpunt en de lijn eindigt daar (Mir-put/Alrosa-complex): geen afwijking.
- De Cyrillische К in de `refs` is nodig: een Latijnse K matcht de OSM-`ref` niet. Een kleine wegprofielfunctie met alleen ankers als via-punten (b1) volstaat voor een mijnweg binnen 15 km; `eindKlassen` zonder `track` zette de lijn op `service/unclassified` en ging in één keer door.
