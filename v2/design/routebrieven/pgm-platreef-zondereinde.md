# Routebrief (licht) · PGM — Platreef → N1/R516 → Zondereinde-smelter (Zuid-Afrika)

**stroom-id:** `pgm-platreef-zondereinde` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** PGM-concentraat (Pt+Pd+Rh+Au plus Ni/Cu, de mix van de Platreef-concentrator) van de nieuwe Platreef-mijn (Ivanplats/Ivanhoe, Mokopane, Limpopo) per **truck** (aannemelijk: één bron voor de bestemming) over N11, N1 (Mokopane–Bela-Bela), R516 en R511 naar de Northam Zondereinde-smelter; stoppunt = de smelter (vervolg = bestaande stroom `pgm-zondereinde-hanau`).
**Welke as van het verhaal:** Noordrand-Bushveld → Westrand: de eerste concentraatverkoop van Platreef ging eind Q4 2025 naar Northam [1][2]; Northam koopt 50% van fase 1 (20.000 t concentraat/j, minus ten hoogste 5.000 t; peiljaar 2021 offtake, productie sinds 18-11-2025) [1][2]. PGM-gehalte niet gebrond; mijn fase 2 (Q4 2027) mikt op ca. 450 koz PGM = 14,0 t/j voor de hele mijn (koz ÷ 32,15) [2].

## 1 · Ketenkaart
```
Platreef-mijn+concentrator `pgm-platreef-mijn` ──(b1 truck · N11 → N1 → R516 → R511 · hemelsbreed 181 km, geen wegkm; OSRM-indicatie 257 km · aannemelijk: één bron)──►
  Zondereinde smelter/BMR `pgm-zondereinde-mijnsmelter` ── stoppunt (vervolg = bestaande stroom `pgm-zondereinde-hanau`)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Platreef-mijn/concentrator → Zondereinde smelter | N11 (Mokopane) → R518 → N1 (Mookgophong, Modimolle) → R516 (Bela-Bela, Rooiberg Road) → R511 → D-wegen naar de poort | hemelsbreed 181 km, geen wegkm; OSRM 256,7 km (eigen meting, geen bron) | maak_stroombeen_weg | nee — doorgetrokken (aannemelijk staat in de beennaam) |

Geen zee-, spoor-, lucht-, leiding- of binnenvaartbeen, geen fase B/C/D/E, geen gedeeld been met een bestaande stroom (Zondereinde is alleen het gedeelde eindanker). Corridorkeuze gemeten: via Thabazimbi (R518 → R510) geeft OSRM 308,6 km (+20%), dus N1/R516 is de korte corridor.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-platreef-mijn` | mijn + concentrator (laadplek) | Platreef Underground Platinum Mine (Ivanplats/Ivanhoe), Ga-Magongwa, Mokopane | -24.0828, 28.9585 | [3][5][6] | bron-gelegd (z15 gezien: ommuurd verwerkingscomplex met schachtgebouwen en procesgebouwen, lichte tailingsdam 1 km NO, waterbekken, zonnepark; N11 loopt 1,3 km oostelijk; OSM `landuse=industrial` way 868132328 met middelpunt -24.0828/28.9585) |
| `pgm-zondereinde-mijnsmelter` | smelter + BMR (losplek, stoppunt) | Northam Zondereinde-complex, Thabazimbi LM, Limpopo — **hergebruikt letterlijk uit `pgm-zondereinde-hanau` en `pgm-booysendal-zondereinde`** | -24.8333, 27.3669 | [4] | bron-gelegd (in die brieven z14–z16 gezien: ommuurd industrieterrein met procesgebouwen en opslagvlakken, tailingsdam 2 km NO; niet opnieuw bekeken) |

## 4 · Via-punten (b1, reisvolgorde; coördinaten op de doorgaande weg, geen stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | R516 Rooiberg Road, ~6 km west van Bela-Bela (OSRM-nearest: Rooiberg Road op 1 m) | -24.8915, 28.1793 | pint de N1 + R516-corridor (257 km) tegen de route via Thabazimbi (309 km); **vervangt** het ontwerppunt "R516-afslag" -24.8858, 28.2845 omdat dat op de rotonde Chris Hani Way / Rooiberg Road in Bela-Bela-stad ligt (stadscentrum-regel) |
| b1 | 2 | R516/R511-knoop (OSRM-nearest op 1 m, ontwerppunt letterlijk) | -24.8878, 27.5299 | pint de R511 noordwaarts naar het smelterterrein i.p.v. een zijroute; hier eindigt de R516 |

Geofabrik-regio: `zuid-afrika` (hele been). Refs: N11, N1, R516, R511. Meer dan twee via-punten niet nodig: de toets met drie tussenpunten gaf 314 km (bindend: gebruik er twee). Waarom geen punt op de N1: de weg is daar de enige doorgaande route.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Platreef-concentrator (fase 1) | Ivanplats (Ivanhoe) | erts → concentraat (Cu, Au, Pd, Pt, Ni, Rh); 80% van nameplate halverwege 2026 | fase 1: 40.000 t concentraat/j totaal, helft naar Northam; fase 2 doel ca. 450 koz PGM/j (Q4 2027) | [1][2] |
| Zondereinde smelter + BMR | Northam | concentraat van de drie eigen mijnen en van derden → matte → filterconcentraat | 35 MW, > 1 Moz/j; verwerkt ook concentraat van derden (Platreef niet bij naam genoemd) | [4] |

## 6 · Stoppunt
De brief stopt bij Zondereinde: Northam koopt het Platreef-concentraat [1], heeft daar zijn smelter, en het vervolg (toll-raffinage bij Heraeus Hanau/Port Elizabeth, Johnson Matthey) is al getekend in `pgm-zondereinde-hanau` vanaf hetzelfde anker [4]; geen tweede fase D.

## 7 · Open punten
- **Bestemming aannemelijk, niet gebrond.** [1][2] noemen Northam als koper maar geen smelterlocatie; [4] zegt dat Zondereinde concentraat van derden verwerkt, zonder Platreef te noemen. De andere 50% van fase 1 gaat naar Heron Metals (Trafigura-JV) [1]: bestemming onbekend, niet getekend.
- **Modaliteit en corridor niet gebrond.** Truck is indirect gesteund: de zoekmachine-samenvatting van het Ivanhoe-persbericht van 2026-01-12 meldt bulktrucks bij de eerste verkoop en omzet zodra de trucks de mijnpoort verlaten; de pagina zelf bleek leeg en is NIET gelezen [7]. Geen vervoerder, geen route gevonden; corridor = OSRM-kortste (eigen meting).
- **Mijnanker alleen een OSM-terrein** (way 868132328): de concentratorpoort en laadplek zijn niet aangewezen; de poort ligt waarschijnlijk aan een toegangsweg naar de N11, 1,3 km oost.
- **De laatste ~16 km (R511 → D2357 → D1639 → toegangsweg) liggen op D-wegen** van onbekende klasse; OSRM snapt het smelteranker op 279 m van de dichtstbijzijnde weg. De bake heeft waarschijnlijk `corridorKlassen` (tertiary, unclassified) en `eindToegangPrivaat` nodig (zoals bij `pgm-booysendal-zondereinde`).
- **PGM-gehalte van het concentraat niet gebrond**, dus geen t PGM/j voor déze stroom; alleen 20.000 t concentraat/j (Northam-deel) en fase 2 ca. 450 koz PGM/j voor de hele mijn (mix niet gegeven; Pt+Pd+Rh+Au waarschijnlijk).
- **Barchart-pagina van het Ivanhoe-update [3] kon niet gelezen worden** (lege respons); alleen genoemd als bronstartpunt.
- Sitelaag: `w-mogalakwena` (-23.9805, 28.916) is een andere mijn (Valterra), ~12 km NNW; Platreef staat niet in `pgm-sitelaag.json` (kandidaat: `pgm-platreef-mijn`, bron-gelegd; niet aangepast, sitelagen zijn niet van deze brief).
- De ±15%-toets is een indicatie: de referentie is eigen OSRM-meting (256,7 km), geen gepubliceerde wegkm.

## 8 · Bronnen
[1] Miningmx, B. Ryan, 2021-12-09, "Northam strikes strategic deal to buy platinum from Robert Friedland's Ivanplats mine": Northam koopt 50% van het fase-1-concentraat (20.000 t/j van 40.000; optie ten hoogste -5.000 t), andere 50% naar Heron Metals (Trafigura); Northam laat concentraat toll-raffineren door Heraeus. https://www.miningmx.com/news/platinum/48340-northam-strikes-strategic-deal-to-buy-platinum-from-robert-friedlands-ivanplats-mine/
[2] NS Energy, 2026-01-13, "Ivanhoe Mines reports progress at Platreef Mine after production start": opening en start concentraatproductie 18-11-2025, eerste verkoop aan Northam eind Q4 2025, fase 2 Q4 2027 ca. 450.000 oz PGM. https://www.nsenergybusiness.com/news/ivanhoe-mines-reports-progress-at-platreef-mine-after-production-start/
[3] Barchart/Ivanhoe, "Ivanhoe Mines announces update on Platreef" (niet leesbaar, lege respons; alleen bronstartpunt). https://www.barchart.com/story/news/36993863/ivanhoe-mines-announces-update-on-platreef-the-world-s-largest-precious-metals-mine-under-development
[4] Northam, "Metallurgical operations": Zondereinde-smelter 35 MW, > 1 Moz/j, verwerkt concentraat van de drie mijnen en van derden; filterconcentraat naar Heraeus Hanau/Port Elizabeth en Johnson Matthey. https://www.northam.co.za/about-northam/metallurgical-operations
[5] OpenStreetMap (Nominatim), way 868132328 "Platreef Underground Platinum Mine", landuse industrial, -24.08278/28.95848. https://www.openstreetmap.org/way/868132328
[6] Esri World Imagery via `v2/tools/sat_check.py` (z14 en z15, live): `v2/build-cache/satcheck/sat-pgm-platreef-zondereinde-platreef.png` en `sat-pgm-platreef-zondereinde-platreef-z14.png`.
[7] Zoekresultaat-samenvatting (WebSearch 2026-10-29) van het Ivanhoe-persbericht 2026-01-12 (newsfilecorp release 280041, pagina leeg): bulktrucks, omzet bij vertrek van de mijnpoort — NIET zelf gelezen. https://www.newsfilecorp.com/release/280041/Ivanhoe-Mines-Announces-Update-on-Platreef-the-Worlds-Largest-Precious-Metals-Mine-Under-Development
[8] OSRM publieke demo (`router.project-osrm.org`), 2026-10-29: Platreef → Zondereinde 256,7 km, 4,34 u (N11 15, R518 5, N1 102, R516 89, R511 20, D-wegen ~16 km); via Thabazimbi 308,6 km; nearest-snaps van de via-punten 1-2 m, smelteranker 279 m. https://project-osrm.org
[9] Wikipedia, "Mokopane" (-24.1833, 29.0167; mijn- en verkeersknoop aan de N1): oriëntatie, ligging ten opzichte van de N11/N1. https://en.wikipedia.org/wiki/Mokopane
[10] Eigen routebrieven `pgm-zondereinde-hanau` en `pgm-booysendal-zondereinde` (eigen routebrieven): letterlijk hergebruikt anker `pgm-zondereinde-mijnsmelter`; Booysendal-profiel als voorbeeld voor de D-wegen. `v2/design/routebrieven/pgm-zondereinde-hanau.md`, `v2/design/routebrieven/pgm-booysendal-zondereinde.md`.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
**Bestand:** `v2/data/stroomroute-pgm-platreef-zondereinde.json` (32,0 KB, contract versie 2, lonlat) · **recept:** `bash v2/tools/bak_stromen.sh pgm-platreef-zondereinde` (functie `bak_pgm_platreef_zondereinde`; b1 via `wegscan_puur.py --profiel pgm-platreef-zondereinde-platreef-zondereinde`, extract zuid-afrika).

| # | modaliteit | km (bake) | punten | toets |
|---|---|---|---|---|
| b1 | truck (doorgetrokken) | 253,6 | 1.537 | indicatie: OSRM 256,7 km = -1,2% (profiel 257: -1,4%); hemelsbreed 181 km (geen wegkm, dus geen norm); binnen het verwachte bereik 245-270 km |

Totaal 253,6 km · 1.537 punten · 2 markers (beide op 0,0 km van de lijn) · geen naden (één been) · geen stippel, geen haven-aanloop, geen kopie, geen vlucht.

- **Wegtool:** profiel `pgm-platreef-zondereinde-platreef-zondereinde` direct onder de ankerregel in `maak_stroombeen_weg.py` (venster 40 km, `corridorKlassen` tertiary en unclassified, `eindToegangPrivaat`, refs N11 N1 R516 R511). Beide via-punten uit §4 hielden; geen enkel verplaatst of geschrapt. Segment-km: 146,5 (mijn -> Rooiberg Road) · 70,0 (-> R516/R511-knoop) · 36,7 (-> smelteranker). Snaps 0,00-0,01 km, behalve het smelteranker: 0,28 km naar de dichtstbijzijnde weg (kort ankerstuk, zoals verwacht). Keerlussen gesnoeid: 7, lengte 253,3 -> 253,3 km (dubbel gereden stukken, 0,02 km elk).
- **Wegklasse (open punt §7):** first mile 2,92 km over `service`, last mile 16,34 km over residential, service, tertiary en unclassified. De D-wegen naar de smelterpoort liggen dus in OSM; `corridorKlassen` en `eindToegangPrivaat` waren nodig en volstonden. De route nam de N1/R516-corridor (253,6 km), niet de Thabazimbi-route (308,6 km).
- **Knikken (`toets_knikken.py`):** 22 knikken >= 60 graden, 0 omkeringen, 0 terugloop; allemaal korte OSM-spikes (4 tot 97 m) bij kruispunten en de ankerstubs, plus één krappe bocht (R 300 m) bij -24,7838/27,4118. `toets_rechte_benen.py --min-km 5` meldt niets voor deze stroom.
- **Markers:** één per anker (`pgm-platreef-mijn`, `pgm-zondereinde-mijnsmelter`), beide letterlijk uit §3. Het Zondereinde-anker is hergebruikt uit `pgm-zondereinde-hanau`, niet opnieuw bekeken.
- **Eindpunt = id:** het id noemt Zondereinde en de lijn eindigt op het Zondereinde-anker; geen afwijking.
- **Lessen:** (1) het via-punt op Rooiberg Road (ipv in Bela-Bela-stad) gaf in één poging een schone N1/R516-lijn zonder omweg; (2) vensterKm 40 volstond, 75 was niet nodig; (3) de scan van de zuid-afrika-extract duurde 159 s, een tweede run met hetzelfde profiel komt uit de cache.

