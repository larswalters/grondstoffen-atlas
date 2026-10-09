# Routebrief (licht) · PGM — Booysendal → N4 → Zondereinde (Zuid-Afrika)

**stroom-id:** `pgm-booysendal-zondereinde` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** PGM-concentraat (Pt+Pd+Rh+Au, "4E") van Northam's Booysendal-mijn en -concentrator (Oostrand Bushveld, bij Steelpoort/Mashishing) per **truck** (aannemelijk: één bron voor de bestemming, geen bron voor modaliteit of corridor) over R540, N4 (Belfast, Middelburg, Pretoria, Brits), R556 en R510 naar de eigen smelter en basismetaalraffinaderij Zondereinde (Northam-dorp, Limpopo); stoppunt = de smelter.
**Welke as van het verhaal:** de interne Northam-keten Oostrand → Westrand: Booysendal heeft geen eigen smelter, Northam bundelt alle concentraat bij Zondereinde [1][2]; het is de tweede Northam-as naast `pgm-zondereinde-hanau`, met een landbeen van ~490 km. Volume: ~15,9 t 4E/j (512.147 oz 4E metaal in concentraat, Booysendal F2025 [4]; F2026 531.668 oz = 16,5 t [4b]; koz ÷ 32,15). Het sitelaag-cijfer 290 koz (9,0 t, [B5]) is verouderd.

## 1 · Ketenkaart
```
Booysendal mijn+concentrator `pgm-booysendal-mijn` ──(b1 truck · R540 → N4 → R556 → R510 · hemelsbreed 278 km, geen wegkm; OSRM-indicatie ~489 km · aannemelijk: één bron)──►
  Zondereinde smelter/BMR `pgm-zondereinde-mijnsmelter` ── stoppunt (vervolg = bestaande stroom `pgm-zondereinde-hanau`)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Booysendal mijn/concentrator → Zondereinde smelter | R540 (Dullstroom–Belfast) → N4 (Belfast–Middelburg–Pretoria–Brits) → R556 → R510 (Northam) | hemelsbreed 278 km, geen wegkm; OSRM 489,1 km (eigen meting, geen bron) | maak_stroombeen_weg | nee — doorgetrokken (aannemelijk staat in de beennaam) |

Geen zee-, spoor-, lucht-, leiding- of binnenvaartbeen, geen fase B/C/D/E. Corridor volgens de bindende toets (R540/N4/R510); geen bron noemt een corridor of modaliteit (§7).

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-booysendal-mijn` | mijn + concentrator (laadplek) | Booysendal Platinum Mine (Northam), tussen Steelpoort en Mashishing | -25.0956, 30.1124 | [3][6][7][9] | bron-gelegd (z14 gezien: kruis op een plantcomplex met gebouwen en wit opslagterrein, tailingsdam met groen water 1,4 km NNW, toegangsweg zuidwaarts; OSM `landuse=industrial` "Booysendal Platinum Mine" way 1164893346, middelpunt -25.0952/30.1129) |
| `pgm-zondereinde-mijnsmelter` | smelter + BMR (losplek, stoppunt) | Northam Zondereinde-complex, Thabazimbi LM, Limpopo — **hergebruikt letterlijk uit `pgm-zondereinde-hanau`** | -24.8333, 27.3669 | [1][10] | bron-gelegd (opnieuw z14 gezien: ommuurd industrieterrein met procesgebouwen en opslagvlakken, de ommuurde tailingsdam 2 km NO) |

## 4 · Via-punten (b1, reisvolgorde; coördinaten op de weg gesnapt, geen stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | R540 ten noorden van Dullstroom (Overpass: `secondary` R540 binnen 80 m) | -25.3599, 30.1494 | pint de R540 naar Belfast/N4 i.p.v. R555 via Stoffberg/Middelburg of de noordelijke N11/N1-route |
| b1 | 2 | N4 ten zuiden van Middelburg (Overpass: `motorway` N4) | -25.8323, 29.4640 | houdt de N4 langs de zuidkant van Middelburg, niet door het stadscentrum |
| b1 | 3 | N4 Pretoria-oost, begin N1/N4-ring (Overpass: `motorway` N4) | -25.7478, 28.2939 | pint de oostelijke ring (N4 met N1) i.p.v. N1-zuid naar Johannesburg |
| b1 | 4 | N4 Platinum Highway, noordwest van Pretoria (Overpass: `motorway` N4) | -25.6540, 28.1238 | pint de N4 westwaarts na de N1/N4-knoop; bewust niet de eerder gebruikte punten Pretoria-centrum (28.1881,-25.7461) of N1/N4-wissel (28.2761,-25.6357, ligt op de N1-zijtak) |
| b1 | 5 | N4/R556-afslag ten westen van Brits (Overpass: `motorway` N4) | -25.7286, 27.6682 | corridorkeuze: R556 noordwaarts (kortste) i.p.v. N4 door Rustenburg-stad en R510 (OSRM: ~13 km langer) |
| b1 | 6 | R556 (Overpass: `secondary` R556) | -25.5354, 27.4288 | houdt de R556 tot de R510-knoop, niet de D1325-sluiproute |
| b1 | 7 | R510 bij Northam (Overpass: `secondary` R510; vervangt de dorpsnode 27.2656/-24.9575, die op een woonstraat ligt) | -24.9560, 27.2615 | R510 naar het complex, niet de D-wegen |

Geofabrik-regio: `zuid-afrika` (hele been). Refs: R540, N4, R556, R510.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Booysendal North- en South-concentrator (South = ex-Everest, 250.000 t/mnd; truckladen) | Northam | UG2/Merensky-erts → PGM- en chroomconcentraat | 512.147 oz 4E in concentraat + 735.706 t chroomconcentraat (F2025) | [3][4] |
| Zondereinde smelter + BMR | Northam | concentraat van "onze drie mijnen" + derden → matte → filterconcentraat | 35 MW, > 1 Moz/j; ovenverbouwing naar 30 MW gepland (F2028) | [1] |

## 6 · Stoppunt
De brief stopt bij Zondereinde: Northam noemt het smelterconcentraat van alle drie de mijnen als voeding [1], en het vervolg (Heraeus Hanau/Port Elizabeth, Johnson Matthey) is al getekend in `pgm-zondereinde-hanau` vanaf hetzelfde anker; geen tweede fase D.

## 7 · Open punten
- **Modaliteit en corridor niet gebrond.** Alleen de bestemming staat in een bron [1][2]; dat het per truck gaat is aannemelijk: Mining Weekly 2020 meldt een nieuwe truck-toegang en -laadfaciliteit bij de South-concentrator voor PGM- en chroomconcentraat, zonder route of bestemming [3]. De corridor (R540/N4/R556/R510) volgt de bindende toets en OSRM; geen operator of vervoerder is gevonden. De echte laadplek ligt waarschijnlijk bij de South-concentrator (~-25.153, 30.145; z14 gezien: procesgebouwen en een grote vierkante tailingsdam, ~10 km ZO van het anker), niet bij het north-anker; de route loopt er over de Boschfontein Road doorheen. Het north-anker blijft (bindend, site-niveau).
- **Alternatief niet gekozen:** OSRM geeft ook 409,8 km (R555 → R33 → N11 → N1 → Bela-Bela → R516/R511) maar 0,6 u trager en eindigend op onverharde D-wegen (D2357/D1639); een operatorkeuze tussen beide is niet gebrond.
- Het Miningmx-stuk 2010 [8] noemt een Oostrand-ovenplan en geen Zondereinde (niet herlezen); Mining Weekly 2016 [2] noemt Zondereinde wel, zonder modaliteit.
- De eerste ~33 km van het anker naar de R540 liggen op lokale wegen (Boschfontein Road e.a.); wegklasse niet gecontroleerd (Overpass viel uit): zie bak-aanwijzingen.
- Sitelaag `w-booysendal` (-24.83, 30.13, 290 koz) ligt ~29 km ten noorden van de plant en is volumeverouderd (512 koz); niet aangepast (sitelagen zijn niet van deze brief).
- De ±15%-toets is een indicatie: de referentie is eigen OSRM-meting, geen gepubliceerde km.

## 8 · Bronnen
[1] Northam, "Metallurgical operations": Zondereinde-smelter en BMR verwerken het concentraat van de drie mijnen; 35 MW, > 1 Moz/j; filterconcentraat naar Heraeus Hanau/Port Elizabeth en Johnson Matthey. https://www.northam.co.za/about-northam/metallurgical-operations
[2] Mining Weekly 2016-12-16, "Booysendal South to reach steady state in 2022": concentraat van de bestaande plants wordt naar de Zondereinde-smelter vervoerd en daar gesmolten (gelezen via de print-versie). https://www.miningweekly.com/article/booysendal-south-to-reach-steady-state-in-2022-2016-12-16
[3] Mining Weekly 2020-10-01, "Booysendal South platinum mine project, South Africa – update": 35 km ten westen van Mashishing, 250.000 t/mnd-concentrator (ex-Everest), nieuwe truck-toegang en -laadfaciliteit voor PGM- en chroomconcentraat. https://www.miningweekly.com/article/booysendal-south-platinum-mine-project-south-africa-2020-10-01
[4] Northam SENS 2025-07-23, voluntary production update F2025: Booysendal 512.147 oz 4E metaal in concentraat; chroomconcentraat 735.706 t. https://sharedata.co.za/sens.asp?id=519808
[4b] Northam SENS 2026-07-13, update F2026: Booysendal 531.668 oz 4E, produceert boven steady state. https://sharedata.co.za/sens.asp?id=553800
[5] Mining Weekly 2026-07-14, Northam F2026 (bevestigt [4b]). https://www.miningweekly.com/article/northam-reports-solid-full-year-production-sales-performance-2026-07-14
[6] Northam, "Booysendal": UG2 North bij Mashishing, Oostrand; geen doorzet of vervoer genoemd. https://www.northam.co.za/about-northam/booysendal
[7] OpenStreetMap (Nominatim/Overpass, ODbL, 2026-10-09): "Booysendal Platinum Mine" way 1164893346; "Everest South Platinum Mine" way 1165010812 (-25.1585/30.1646); refs R540, N4, R556, R510 gecontroleerd binnen 80 m van de via-punten (Overpass faalde op 4 punten, daar alleen OSRM-snap).
[8] Miningmx, "Northam Jubilee to explore furnace plan" (uit het ontwerp, niet herlezen). https://www.miningmx.com/news/platinum/25067-northam-jubilee-to-explore-furnace-plan/
[9] Esri World Imagery via `v2/tools/sat_check.py` (z14): `v2/build-cache/satcheck/sat-pgm-booysendal-zondereinde-booysendal.png`, `…-zondereinde.png`, `…-everest-south.png`.
[10] Routebrief `pgm-zondereinde-hanau.md` (anker `pgm-zondereinde-mijnsmelter`, hergebruikt).
[11] OSRM public demo (router.project-osrm.org), 2026-10-09: 489,1 km / 6,7 u (N4); alternatief 409,8 km / 7,3 u; via Marikana 501,8 km. Indicatie, geen publicatie.
[B5] `v2/design/pgm-sitelaag.json`, `w-booysendal`: ~290 koz 4E, status aannemelijk (verouderd, zie §7).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-pgm-booysendal-zondereinde.json` (86,6 KB, contract versie 2, lonlat) · **recept:** `bash v2/tools/bak_stromen.sh pgm-booysendal-zondereinde` (functie `bak_pgm_booysendal_zondereinde`; b1 via `wegscan_puur.py --profiel pgm-booysendal-zondereinde-booysendal-zondereinde`, extract zuid-afrika).

| # | modaliteit | km (bake) | punten | toets |
|---|---|---|---|---|
| b1 | truck (doorgetrokken) | 489,2 | 4.229 | indicatie: OSRM 489,1 km = 0,0%; hemelsbreed 278 km (geen wegkm, dus geen norm); binnen het verwachte bereik 470-510 km |

Totaal 489,2 km · 4.229 punten · 2 markers (beide op 0,0 m van de lijn) · geen naden (één been) · geen stippel, geen haven-aanloop, geen kopie.

- **Wegtool:** profiel `pgm-booysendal-zondereinde-booysendal-zondereinde` direct onder de ankerregel in `maak_stroombeen_weg.py` (venster 75 km, `corridorKlassen` tertiary en unclassified, `eindToegangPrivaat`, refs R540 N4 R556 R510). Alle zeven via-punten uit §4 hielden; geen enkel verplaatst of geschrapt. Alle acht segmenten snappen ≤ 0,01 km, het laatste stuk naar het smelteranker 0,28 km (plant en weg-stub OK). Segment-km: 50,6 · 108,4 · 122,0 · 30,4 · 47,9 · 35,6 · 72,1 · 22,0; het stuk R540 → N4 zuid van Middelburg (108,4 km tegen ~85 km hemelsbreed) is de echte R540/N4-omweg via Belfast, geen sluipweg. Keerlussen gesnoeid: 20, lengte 488,9 → 488,9 km.
- **Wegklasse eerste ~33 km (open punt §7):** gemeten first mile over kleine klassen 18,1 km (service, tertiary, unclassified) en last mile 8,7 km (residential, service, tertiary, unclassified). De lokale wegen van het anker naar de R540 liggen dus gewoon in OSM; `corridorKlassen` was nodig en volstond, de route nam geen D-weg-sluiproute.
- **Laadplek:** het north-anker is behouden (site-niveau, bindend). De South-concentrator (~-25.153, 30.145) ligt ~10 km ZO op de route; de lijn passeert die plek (een gesnoeide keerlus van 0,02 km op -25.1558, 30.1373).
- **Knikken (`toets_knikken.py`):** 16 knikken >= 60 graden, 0 omkeringen, 0 terugloop; alle zijn korte OSM-spikes (3 tot 97 m) bij kruispunten en de ankerstubs. `toets_rechte_benen.py --min-km 5` meldt niets voor deze stroom.
- **Bevindingen (niet door deze brief te repareren):** sitelaag `w-booysendal` (-24.83, 30.13, 290 koz) ligt ~29 km van de plant en is volumeverouderd (512 koz F2025); centraal corrigeren. De beennaam draagt "aannemelijk: één bron"; modaliteit en corridor blijven ongebrond (§7).
- **Lessen:** (1) `maak_stroombeen_weg.py` is een CRLF-bestand en `bak_stromen.sh` een LF-bestand: per bestand met de eigen regeleinden invoegen (LF-controle bak_stromen.sh: 0 CRLF); (2) een Zuid-Afrika-scan op 75 km duurde 181 s met `wegscan_puur.py`; (3) bij een hemelsbreed-plus-OSRM-norm is een uitkomst van 0,0% tegen de OSRM-indicatie geen onafhankelijk bewijs, omdat beide uit OSM komen: de echte controle is dat alle via-punten snappen en geen D-weg wordt genomen.
