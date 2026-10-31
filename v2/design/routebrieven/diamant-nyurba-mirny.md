# Routebrief (licht) · Diamant — Nyurba GOK (Nakyn) → Mirny (Rusland)

**stroom-id:** `diamant-nyurba-mirny` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** Ruwe diamant van Alrosa's Nyurba GOK (Nyurbinskaya- en Botuobinskaya-pit, Nakyn-veld, Sakha) gaat per truck over de seizoenswinterweg Nakyn–98K-004 en daarna de regionale weg 98K-004 via Tsjernysjevski naar het Mir-complex/sorteercentrum in Mirny (aannemelijk: alleen de bestemming is gebrond, vervoersmiddel onbevestigd).
**Welke as van het verhaal:** *de noordelijke toevoer van de Nyurba-divisie (19% van Alrosa) naar het sorteercentrum.* Nyurba 7,7 Mct (2017, 19% van Alrosa) [2]; 7,407 Mct in 2013 [1]; sitelaag `w-nyurba` 7,0 Mct/j (orde-grootte). Eenheid Mct/j; waarde per karaat gemengd (edelsteen en near-gem), niet in het gewicht.

## BINDENDE aanpassing (haalbaarheidstoets, toegepast)
Beennaam: winterweg (seizoensgebonden), aannemelijk: alleen bestemming gebrond, vervoer onbevestigd. Profiel `rusland-verrehoosten` MET `corridorKlassen ["unclassified"]` (de winterweg is OSM `highway=unclassified`; zonder die klasse geen pad). Via-punten zoals in §4; ankers `dia-nyurba-nakyn` en `dia-mirny-mijn` behouden. Km: hemelsbreed 316 km, geen wegkm; de OSM-route van 553 km is een indicatie.

## 1 · Ketenkaart
```
Nakyn-complex / Nyurba GOK `dia-nyurba-nakyn` ──(b1 truck · winterweg Nakyn (seizoensgebonden, ca. 300 km) → 98K-004 via Tsjernysjevski ·
 hemelsbreed 316 km, geen wegkm; OSM-route ca. 553 km indicatie, aannemelijk)──► Mir-complex / sorteercentrum Mirny `dia-mirny-mijn` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Nakyn-complex (Nyurba GOK) → Mir-complex, Mirny | zimnik (winterweg) Nakyn → 98K-004 (OSM `unclassified`, `winter_road=yes`, ca. 300 km), daarna 98K-004 zuidwaarts via Tsjernysjevski; aannemelijk: één bron voor de bestemming, vervoer onbevestigd | hemelsbreed 316 km, geen wegkm [1: "300-320 km NO van Mirny", hemelsbreed]; OSM-scan 553,4 km [6] = indicatie | maak_stroombeen_weg (rusland-verrehoosten), 6 via-punten | nee |

Fase C, D en E vervallen: geen bron voor een vervolgbeen uit Mirny binnen deze keten (de vervolgstromen `diamant-mirny-mumbai` en `diamant-mirny-smolensk` beginnen op `dia-mirny-mijn`). Geen vlucht getekend: de Antonov naar Nakyn is een passagiersvlucht [3], geen vrachtbron.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-nyurba-nakyn` | mijn + verwerking / laadplek | Nakyn-verwerkingscomplex Nyurba GOK (fabrieken nr. 15/16), naast de Nyurbinskaya- en Botuobinskaya-pit | 65.0150, 117.0916 | [1][6][7] | bron-gelegd (z15 gezien: groot verwerkingscomplex met zilverkleurige hallen, stortbergen en groen meertje 1,3 km ZZO van de Nyurbinskaya-put; ru-wiki-punt 65.0256,117.0811 ligt IN de put; welke hal fabriek 16 is niet te zien) |
| `dia-mirny-mijn` | mijn + sorteercentrum / bestemming | Mir-put / Alrosa-complex, Mirny (**hergebruikt**) | 62.5258, 113.9842 | `diamant-mirny-mumbai.md` [4], `diamant-aikhal-mirny.md` [5] | bron-gelegd (overgenomen; z15 gezien in beide brieven: rand van de open put met bebouwing; sorteercentrum niet apart te onderscheiden) |

Satellietbeelden: `v2/build-cache/satcheck/sat-diamant-nyurba-mirny-nakyn.png` (z15) en `-pit.png` (z14; de Nyurbinskaya-put ca. 2 km breed, tweede pit NO, complex ZO daarvan).

## 4 · Via-punten (b1, reisvolgorde, alle op winterweg of 98K-004; snap in de haalbaarheidstoets [6])
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | zimnik Nakyn, westwaarts uit het veld | 64.4898, 115.4536 | pint de route op de winterweg i.p.v. mijnwegen en sluipsporen rond Nakyn (97 km hemelsbreed) |
| b1 | 2 | zimnik Nakyn, middenstuk | 64.2865, 113.6092 | houdt de lijn op de ene winterweg over de tientallen km zonder alternatief (+92 km) |
| b1 | 3 | knoop zimnik ↔ 98K-004 (eerste 98K-004-knoop) | 64.3170, 112.4899 | corridorkeuze: hier mondt de winterweg op de doorgaande weg uit (+54 km) |
| b1 | 4 | 98K-004, Sadynski-nasleg, middenstuk | 64.1385, 112.5788 | OP de 98K-004, hergebruik van via-punt 2 van `diamant-aikhal-mirny` [5] |
| b1 | 5 | 98K-004 bij Tsjernysjevski | 63.0090, 112.5236 | corridorkeuze: de weg gaat via Tsjernysjevski (92 km van Mirny), hergebruik uit [5] |
| b1 | 6 | 98K-004, Mirny-aanloop | 62.7979, 113.3721 | laatste stuk op de doorgaande weg vóór de stad, niet door een stadscentrum; hergebruik uit [5] |

Hemelsbreed per segment (km): anker → 1 97,2 · → 2 91,5 · → 3 54,1 · → 4 20,3 · → 5 125,6 · → 6 49,0 · → Mirny 43,5 (via-punt-lijn 481 km; OSM-route 553 km). Punten 4-6 liggen ook op `diamant-aikhal-mirny` b2 (zo'n 225-250 km 98K-004): geen letterlijke kopie, want de start en het eerste stuk verschillen.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Nyurba GOK, fabriek nr. 16 (erts, zware media) en nr. 15 (seizoensfabriek, zand) | Alrosa, Nyurba GOK | erts → ruwe diamant | 7,7 Mct (2017); ru-wiki-tabel Nyurbinskaya 7,2 (2013-14) → 3,5 (2021) + Botuobinskaya 5,7 (2021) | [1][2] |
| Diamond Sorting Center, Mirny | Alrosa | ruw → gesorteerd ruw | niet gebrond (14.000 ct op één tafel, ca. 9 mln USD, 2019) | [3] |

## 6 · Stoppunt
De brief stopt in Mirny, waar het hoofdkantoor van Nyurba GOK zit [1] en het Alrosa-sorteercentrum staat [3]; wat daarna naar markten vliegt is `diamant-mirny-mumbai` en `diamant-mirny-smolensk` (fase C/D/E vervallen).

## 7 · Open punten
- **Geen bron voor het vervoersmiddel Nakyn → Mirny**: de winterweg komt alleen uit OSM [6] (ru-wiki noemt hem niet [1]); vervoer per weg of vlucht (Antonov, Nakyn-vliegveld) is niet gebrond. Wegbeen is daarom aannemelijk; geen vlucht getekend.
- **Bestemming Mirny alleen indirect**: hoofdkantoor in Mirny [1] en sorteercentrum Mirny [3]; geen bron die Nyurba-ruw expliciet naar dat centrum legt.
- **Winterweg is seizoensgebonden** (OSM `winter_road=yes`, deels ijs): de lijn is de winterstand, geen jaarrond-route; km niet bevestigd, de ±15%-toets is geen norm.
- **Afstand Mirny-Nakyn** loopt in ru-wiki uiteen (300 vs 320 km NO) en is hemelsbreed, geen wegkm.
- **Volume** 7,7 Mct is 2017; ru-wiki noemt voor 2021 "12 mln" maar de tabel telt 9,2 (3,5 + 5,7): inconsistent, niet gebruikt. Mirny-deel van de productie niet gebrond. Waarde per karaat niet gevonden.
- **Sitelaag `w-nyurba` (63.2833, 118.3333) is een regio-centroïde** ca. 190 km van het echte Nakyn-complex: centraal gelijktrekken met `dia-nyurba-nakyn` (niet door deze brief gewijzigd).
- **Mijnwegen tussen de put en het complex** (1,3 km) zijn niet getekend; fabriek 16 individueel niet gezien.

## 8 · Bronnen
[1] ru.wikipedia, "Накынское месторождение" (65°01′32″N 117°04′52″E = Nyurbinskaya-put; 300-320 km NO van Mirny; hoofdkantoor GOK in Mirny; fabrieken nr. 15/16; 7,407 Mct 2013; tabel 2012-2021). https://ru.wikipedia.org/wiki/Накынское_месторождение
[2] en.wikipedia, "Alrosa" (Nyurba divisie 7,7 Mct in 2017, 19% van Alrosa; Nakyn-veld met Nyurbinsky- en Botuobinsky-pit). https://en.wikipedia.org/wiki/Alrosa
[3] AFP via Arab News, 2019-07-08, "Russia digs for diamonds to ensure supremacy in global market" (Antonov-passagiersvlucht naar Nakyn; sorteercentrum Mirny, directeur Popov). https://www.arabnews.com/business/russia-digs-for-diamonds-to-ensure-supremacy-in-global-market-1522276
[4] `v2/design/routebrieven/diamant-mirny-mumbai.md` (anker `dia-mirny-mijn`, Mir-put 62.5258,113.9842).
[5] `v2/design/routebrieven/diamant-aikhal-mirny.md` (98K-004-via-punten, Tsjernysjevski 92 km van Mirny, hergebruikt).
[6] OSM (ODbL), Geofabrik `rusland-verrehoosten`, eigen PBF-scan in de haalbaarheidstoets 2026-10-31: "Зимник Накын" verbindt Nakyn met 98К-004 bij 64.317,112.490 (ca. 300 km), route 553,4 km.
[7] Esri World Imagery via `v2/tools/sat_check.py` (`v2/build-cache/satcheck/sat-diamant-nyurba-mirny-nakyn.png`, `-pit.png`; eerdere `-toets-nakyn.png`, `-toets-pit.png`).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Bestand:** `v2/data/stroomroute-diamant-nyurba-mirny.json` (57,9 KB, contract versie 2, lonlat) · functie `bak_diamant_nyurba_mirny` in `v2/tools/bak_stromen.sh` · profiel `diamant-nyurba-mirny-nakyn-mirny` in `v2/tools/maak_stroombeen_weg.py`.

| # | modaliteit | been | km gebakken | km brief | stippel |
|---|---|---|---|---|---|
| b1 | truck | Nakyn-complex Nyurba GOK → Mir-complex/sorteercentrum Mirny (winterweg Nakyn → 98K-004 via Tsjernysjevski) | 553,5 | hemelsbreed 316 (geen wegkm); OSM-scan 553,4 | nee |

Totaal 553,5 km, 2.808 punten, 2 markers (`dia-nyurba-nakyn` 65.0150,117.0916 en `dia-mirny-mijn` 62.5258,113.9842), beide 0,0 km van de lijn. Geen naden (een been).

**Recept:** `wegscan_puur.py --profiel diamant-nyurba-mirny-nakyn-mirny` (extract `rusland-verrehoosten`, refs `98К-004` met Cyrillische К, `corridorKlassen ["unclassified"]`, vensterKm 90, 8 via-punten = 2 ankers + de 6 uit §4) → `bak_stromen.sh diamant-nyurba-mirny`. Alle via-punten snapten op 0,00-0,06 km; geen via-punt verplaatst of weggelaten.

**Toelichting:**
- Het gebakken getal 553,5 km is de OSM-indicatie uit de haalbaarheidstoets (553,4), niet een bevestigde wegkm; tegen de hemelsbrede 316 km is het +75%, maar de ±15%-toets is hier geen norm (brief). Segmenten: 120,1 · 120,4 · 58,9 · 21,2 · 133,2 · 53,4 · 46,2 km; de eerste twee zijn de winterweg (hemelsbreed 97 en 92 km), dus een omwegfactor van ca. 1,3 op de zimnik.
- De lijn is de winterstand: zimnik ca. 300 km (first mile over `unclassified`/`service` 299,4 km), seizoensgebonden. Aannemelijk (alleen de bestemming gebrond, vervoer onbevestigd) staat in de beennaam, niet in de lijnstijl. Geen stippel, geen haven-aanloop, geen vlucht, geen leiding, geen kopie.
- `toets_knikken`: 5 knikken, 1 omkering (177° op 28 m straal bij het startanker, ankerstub van 0,06 km), 0 terugloop; de knik van 102° ligt op de knoop zimnik-98K-004 (64.317,112.490), een echte aansluiting.

**Lessen / bevindingen:**
- `corridorKlassen ["unclassified"]` is voor deze stroom een voorwaarde (de zimnik is OSM unclassified); zonder die klasse bestaat er geen pad.
- Sitelaag `w-nyurba` (63.2833,118.3333) ligt ca. 190 km naast het complex: centraal gelijktrekken met `dia-nyurba-nakyn`.
- Open uit §7 blijven staan: geen bron voor het vervoer, bestemming Mirny indirect, winterweg seizoensgebonden.
