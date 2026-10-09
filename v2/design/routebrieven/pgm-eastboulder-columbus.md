# Routebrief (licht) · PGM — East Boulder Mine → Big Timber → Columbus (Verenigde Staten)

**stroom-id:** `pgm-eastboulder-columbus` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** platinagroepmetaal (2E, Pd-dominant: Pd ~77% / Pt ~23%) als concentraat per **truck** van de
East Boulder Mine (Sibanye-Stillwater, Sweet Grass County) over East Boulder Road → Boulder River Road (MT-298) →
Big Timber → I-90 oostwaarts naar het Columbus Metallurgical Complex (smelter + base metal refinery) — **stoppunt**:
de PGM-rijke filter cake gaat daarna naar niet bij naam genoemde externe raffinaderijen (zelfde stoppunt als `pgm-stillwater-columbus`).
**Welke as van het verhaal:** de tweede Amerikaanse J-M Reef-mijn: Amerika's enige PGM-productie loopt via twee mijnen
naar één smelter. East Boulder alleen: **65.225 oz 2E in H1 2025** [2] → ruim 130 koz/j ≈ **4,1 t 2E/j** (verdubbeld
halfjaar, indicatie; koz ÷ 32,15); US-totaal 2025 284.069 oz 2E ≈ 8,8 t [3]. Mix 2E (Pd+Pt). Capaciteit concentrator 1.800 tpd [1].

## 1 · Ketenkaart
```
East Boulder Mine `pgm-eastboulder-laad` ──(b1 truck · East Boulder Rd → MT-298 → Big Timber → I-90 · ~119 km OSRM)──►
Columbus Metallurgical Complex `pgm-columbus-smelter` (smelter + base metal refinery, aannemelijk: één bron)
   ═══ knoop: PGM-rijke filter cake (2E) ═══ ── stoppunt (afnemer "third-party refiner" niet gedocumenteerd)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-eastboulder-laad` → `pgm-columbus-smelter` | East Boulder Road (NFS #205) → Main Boulder Road/**MT-298** (Boulder River Road, McLeod) → Big Timber → **I-90** oost → Columbus (MT-78, Pike Ave) | OSRM-indicatie 119 km (OSM-gebaseerd, **geen wegkm**); hemelsbreed 67 km; deel mijn→McLeod 16 mi ≈ 26 km gepubliceerd [4] (OSRM 25 km) | maak_stroombeen_weg — profiel `pgm-eastboulder-columbus` (us-montana) | nee — beide uiteinden aan het wegnet |

Beennaam: `East Boulder Mine → Columbus Metallurgical Complex (East Boulder Road → MT-298 → Big Timber → I-90) (aannemelijk: één bron)`.
Truck is aannemelijk, één bron voor de bestemming [1]; geen bron noemt de modaliteit expliciet (zie §7). Geen zee-/spoor-/luchtbeen.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-eastboulder-laad` | mijn / concentrator (laadplek) | East Boulder Mine (Sibanye-Stillwater), East Boulder River-vallei, Sweet Grass County | 45.5040, -110.0860 | [1][4][5] | bron-gelegd (z14+z15 gezien: concentrator-/verwerkingsgebouwen en wegen direct ZUID van het groene tailingsbekken; OSM-node 45.5080,-110.0830 lag op de bekkenrand, verschoven ~0,5 km ZZW naar de gebouwen) |
| `pgm-columbus-smelter` | smelter + base metal refinery (stoppunt) | Columbus Metallurgical Complex (Sibanye-Stillwater), Columbus | 45.6330, -109.2400 | [1][5], **letterlijk hergebruikt uit `pgm-stillwater-columbus` §3** | bron-gelegd (daar z15; hier z15 opnieuw gezien: industrieterrein met gebouwen tegen de spoorlijn en de landingsbaan van Columbus, zuidrand van het dorp) |

## 4 · Via-punten (b1 — vijf, allemaal óp de doorgaande weg)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | East Boulder Road × Main Boulder Road | 45.6234, -110.1353 | einde van de bosweg: vanaf hier de Boulder River Road noordwaarts (OSRM-snap 3 m, ~21 km) in plaats van zijwegen naar het zuiden |
| b1 | 2 | MT-298 bij Eightmile Bridge | 45.7236, -109.9968 | pint MT-298 (Boulder Road) langs de rivier naar Big Timber, niet via zijroads/Springcreek (OSRM-snap 2 m) |
| b1 | 3 | Big Timber — I-90-oprit oostzijde | 45.8313, -109.9080 | corridorkeuze west- of oostoprit: oost = geen terugrijden door het centrum van Big Timber; ligt NIET in het stadscentrum |
| b1 | 4 | I-90 bij Reed Point | 45.7094, -109.5917 | pint de snelweg I-90 i.p.v. het parallelle oude US-10/county-wegnet (OSRM-snap < 5 m) |
| b1 | 5 | I-90-afrit Columbus (MT-78) | 45.6491, -109.2529 | pint de afrit naar Columbus en de laatste ~2 km naar het anker via MT-78/Pike Ave en 1st Ave S (OSRM-snap 5 m) |

Bak-agent: snap per via-punt toetsen op het `us-montana`-extract (≤ 5 km, liefst < 100 m); zijtak = fout gelegd.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| East Boulder-concentrator | Sibanye-Stillwater | ondergronds 2E-erts → verdikt concentraat | 1.800 tpd [1]; 65.225 oz 2E in H1 2025 [2] | [1][2] |
| Columbus Metallurgical Complex | Sibanye-Stillwater | concentraat Stillwater + East Boulder → matte → PGM-rijke filter cake (~60% PGM) | VS samen 284.069 oz 2E (2025) [3] | [1][3] |

## 6 · Stoppunt
De brief stopt bij het Columbus-complex: de filter cake gaat volgens de eigen rapportage naar externe raffinaderijen zonder
naam of locatie [1][3]; het bewijs eindigt waar de bron eindigt (zelfde stoppunt als `pgm-stillwater-columbus`). Fase B–E vervallen.

## 7 · Open punten
- **Modaliteit niet expliciet bebron:** bronnen zeggen alleen "thickened concentrate is transported to the smelter" [1]; truck is afgeleid
  (de mijn ligt ~26 km op een bosweg; geen spoorlijn naar de mijn gevonden). Een spoor-omlading in Big Timber/Columbus is niet uitgesloten, niet gedocumenteerd.
- **Wegkm:** geen operator- of overheidsopgave voor het gehele traject; 119 km is OSRM op OSM (geen onafhankelijke toets, de ±15%-toets is hier
  een indicatie). Alleen het stuk mijn → McLeod (16 mi, Forest Service [4]) is gepubliceerd.
- **Volume:** East Boulder-jaarvolume niet apart gepubliceerd; 4,1 t is H1 2025 × 2 (restructurering in 2024–25; 230 koz/j uit 2020 [6] is verouderd).
- **Operationele status 2026** niet geverifieerd na H1 2025; East Boulder was toen in productie [2]. Uitbreiding (Lewis Gulch-tailings) goedgekeurd 2024 [4].
- **Last mile:** laadplek binnen het mijnterrein (concentrator-expeditie) niet aanwijsbaar; anker staat op de gebouwen, geen aparte last-mile.
- **Overlap met `pgm-stillwater-columbus`:** alleen de laatste ~2 km (Columbus); geen kopie nodig, eigen geometrie.

## 8 · Bronnen
[1] Mining Technology — Stillwater and East Boulder projects (East Boulder 20 km W van Stillwater; concentrator 1.800 tpd; verdikt concentraat naar smelter Columbus). https://www.mining-technology.com/projects/stillwater-and-east-boulder/
[2] Sibanye-Stillwater, Form 6-K H1 2025 (SEC) — East Boulder 65.225 oz 2E, Stillwater 75.898 oz, VS 141.124 oz. https://www.sec.gov/Archives/edgar/data/1786909/000178690925000031/form6-kh135.htm
[3] Sibanye-Stillwater, handelsmitteilung/trading update FY2025 — VS-productie 284.069 oz 2E (boerse-online/IRW). https://www.boerse-online.de/dpa-afx/irw-news-sibanye-stillwater-handelsmitteilung-und-produktionsupdate-fuer-das-am-31-dezember-2025-endende-geschaeftsjahr-503316.html
[4] USDA Forest Service, Custer Gallatin — East Boulder Mine Amendment 004 Expansion EIS (mijn Sweet Grass County, ~16 mi ten zuiden van McLeod op NFS Road #205; via zoekresultaat, pagina zelf 403). https://www.fs.usda.gov/r01/custergallatin/projects/61385
[5] Wikipedia — Stillwater Mining Company (East Boulder Mine bij Big Timber, smelter + base metal refinery Columbus). https://en.wikipedia.org/wiki/Stillwater_Mining_Company
[6] Vorige brief `v2/design/routebrieven/pgm-stillwater-columbus.md` (Columbus-anker, volume 460–490 koz 2E peiljaar 2023, East Boulder OSM-node 45.5080,-110.0830) — intern.
[7] OSRM (router.project-osrm.org, OSM-data) — route 118,975 km, snaps via-punten; Nominatim: McLeod 45.6622,-110.1139. https://router.project-osrm.org
[8] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-pgm-eastboulder-columbus-mijn.png` (z15), `-mijn-z14.png`, `-mijn-z15.png`, `-smelter.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Resultaat:** `v2/data/stroomroute-pgm-eastboulder-columbus.json` — 1 been, **118,2 km**, 1.053 punten, 2 markers (beide ankers uit §3), 23,1 kB, contract versie 2, geen stippel.

| # | modaliteit | been | km gemeten | indicatie | afwijking |
|---|---|---|---|---|---|
| b1 | truck | East Boulder Mine → Columbus Metallurgical Complex (East Boulder Road → MT-298 → Big Timber → I-90) (aannemelijk: één bron) | 118,2 | OSRM 119 (geen wegkm) | -0,7% |

Segmenten van het wegtool: anker → East Boulder Rd × Main Boulder Rd 20,4 km · → Eightmile Bridge 17,3 · → Big Timber I-90-oprit oost 16,9 · → Reed Point 30,1 · → afrit Columbus 30,5 · → anker Columbus 2,9. Alle via-punten snapten op 0,00 km; anker-verbindingen 0,21 km (mijn) en 0,09 km (smelter). Naden: één been, dus geen naad; markers 0,0 km van de lijn.

**Recept.** Profiel `pgm-eastboulder-columbus` in `v2/tools/maak_stroombeen_weg.py` (extract us-montana, 5 via-punten uit §4, refs I-90/MT-298/MT-78, vensterKm 40, `corridorKlassen` tertiary+unclassified), gescand met `python v2/tools/wegscan_puur.py --profiel pgm-eastboulder-columbus` (20 s scan, pyosmium geblokkeerd). Uitvoer `v2/build-cache/ais/graaf/pgm-eastboulder-columbus-weg-eastboulder-columbus.geojson`; functie `bak_pgm_eastboulder_columbus` in `v2/tools/bak_stromen.sh`, gebakken met `bash v2/tools/bak_stromen.sh pgm-eastboulder-columbus`.

**Toelichting.**
- **Geen stippel, geen aanloop, geen vlucht, geen leiding, geen kopie:** beide uiteinden liggen aan het wegnet (snap 0,21 en 0,09 km).
- **Km-toets is een indicatie:** er is geen gepubliceerde wegkm voor het hele traject (hemelsbreed 67 km; alleen mijn → McLeod 16 mi ≈ 26 km). De gemeten 118,2 km valt 0,7% onder de OSRM-referentie van 119 km; het stuk mijn → Main Boulder Road + MT-298 tot McLeod komt in de buurt van de 26 km uit de Forest Service-opgave.
- **Eindpunt gelijk aan het id:** de lijn eindigt in Columbus, geen afwijking van het ontwerp.
- **Toetsen:** `toets_knikken.py` 11 knikken (kruispunten, o.a. oprit Big Timber en afrit Columbus), 0 omkeringen, 0 terugloop; `toets_rechte_benen.py --min-km 5` meldt dit been niet.

**Lessen.**
- **corridorKlassen was nodig:** met alleen de standaardklassen (en de eindklassen binnen 12 km van de ankers) hield de wegset bij 45.6224, -110.1291 op: "geen wegpad tussen punt 1 en 2". De Boulder River Road is in OSM `tertiary` (ref S-298), de East Boulder Road `unclassified`; `corridorKlassen: ["tertiary","unclassified"]` loste het op zonder via-punt te verschuiven. De eindklassen reikten niet tot de Main Boulder Road, die 13 km van het anker ligt.
- **Eén keerlus gesnoeid** (45.7236, -109.9968, 5 punten, 0,22 km) bij het via-punt Eightmile Bridge: het punt ligt iets naast de doorgaande lijn; lengte 118,1 → 117,9 km in het wegtool, geen invloed op de toets.
- **Open punten uit §7 blijven staan:** truck niet expliciet bebron, geen wegkm, geen apart East Boulder-volume, status 2026 niet geverifieerd.
