# Zilver · Sindesar Khurd → Dariba (India)

**stroom-id:** `zilver-sindesarkhurd-dariba` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) ·
**status:** gebakken
**Keten in één zin:** zink-lood-zilvererts van de Sindesar Khurd-mijn (Hindustan Zinc, Rajsamand, Rajasthan) per truck over
een lokale weg van ca. 5,5 km, westelijk langs de Rajpura Dariba-put, naar het Dariba Smelting Complex (Hindustan Zinc,
dezelfde gemeente) — **eenbenige keten, bewust kort, aannemelijk: één bron** voor de mijn→smelter-relatie.
**Welke as van het verhaal:** India — Hindustan Zinc, de tweede mijn-tot-smelter-keten naast Rampura Agucha → Chanderiya;
zilver als bijproduct van zink/lood. **Jaarvolume: niet gevonden per site of per been** (groep: 714 t Ag/j geraffineerd,
FY2022-23, HZL integrated report [3]; dat is de hele groep en niet deze stroom, dus geen volume geclaimd).

## 1 · Ketenkaart
```
Sindesar Khurd-mijn `ag-sindesarkhurd-mijn` ──(b1 truck · lokale weg zuidwaarts, west van de Rajpura Dariba-put ·
   hemelsbreed 5,4 km, geen wegkm; gemeten ~5,5 km)──► Dariba Smelting Complex `ag-dariba-smelter` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Sindesar Khurd-mijn → Dariba Smelting Complex (aannemelijk: één bron) | lokale weg Sindesar Khurd → west langs Rajpura Dariba-put → Dariba-poort (geen genummerde weg in OSM) | hemelsbreed 5,4 km, geen wegkm; OSRM-indicatie 5,4 km [1][8] | maak_stroombeen_weg (extract `india`) | nee |

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-sindesarkhurd-mijn` | mijn + concentrator (kop van b1) | Sindesar Khurd-mijn (Hindustan Zinc) | 24.9989, 74.1430 | [6][7][9] | bron-gelegd (z14 + z16 gezien: langgerekt mijnterrein van ca. 1,5 km N-Z met schachtgebouwen, grote concentrator-hallen, transportbanden en rangeersporen; punt ligt op het terrein — HERGEBRUIKT letterlijk uit sitelaag `w-sindesar-khurd`, niet verschoven) |
| `ag-dariba-smelter` | smelter (staart van b1, stoppunt) | Dariba Smelting Complex (Hindustan Zinc) | 24.9510, 74.1330 | [1][7][9] | bron-gelegd (z14 + z16 gezien: industrieterrein met blauw-gedekte smelterhallen, schoorstenen, bezinkbekkens en sporen; punt ligt op de gebouwen — **0,4 km zuidelijker** dan het Photon-punt 24.9543, 74.1324 uit de haalbaarheidstoets, dat net op de rand van het tailingsveld lag; de oranje tailings en de Rajpura Dariba-put liggen direct ten noorden) |

## 4 · Via-punten (b1 — corridorkeuze: west of oost van de Rajpura Dariba-put/tailings)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | weg ten zuiden van de mijnpoort | 24.9884, 74.1371 | hier verlaat de weg het mijncomplex en buigt naar het zuiden (OSRM-geometrie over OSM) [8] |
| b1 | 2 | weg zuidwaarts, noordelijk van de tailings | 24.9755, 74.1349 | houdt de weg op de westelijke lijn, niet over de akkerpaden oostelijk van de tailings [8] |
| b1 | 3 | weg west van de Rajpura Dariba-put | 24.9665, 74.1326 | pint de keuze west langs de put (de weg loopt tussen put en dorpswegen) [7][8] |
| b1 | 4 | weg richting Dariba-poort | 24.9565, 74.1312 | laatste doorgaande stuk vóór de toegang aan de NW-kant van het smeltercomplex [8] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Dariba Smelting Complex | Hindustan Zinc (Vedanta) | zink- en loodconcentraat (met zilver) → zinkkathodes/-ingots en loodkathodes; zilver niet gepubliceerd voor Dariba | zink 250 kt/j, lood 120 kt/j; zilver: geen cijfer | [1][4] |

## 6 · Stoppunt
De brief stopt bij Dariba: HZL noemt Dariba zelf als smelter die "nearby Rajpura Dariba and Sindesar Khurd mines" benut [1], maar publiceert
geen zilverroute vanaf Dariba; de zilverraffinaderij staat volgens HZL in Pantnagar (Uttarakhand, [3]) en de sitelaag legt het zilvergewicht
bewust bij Chanderiya [6] — een volgend been is dus niet gedocumenteerd en wordt niet getekend.

## 7 · Open punten
- **Conflict in de bronnen:** de sitelaag [6] zegt dat Sindesar Khurd-erts naar Chanderiya gaat; de Dariba-pagina [1] noemt Sindesar Khurd juist als
  nabije voeder van Dariba. Er is geen document dat de concentraatstroom per mijn naar een smelter vastlegt; getekend als aannemelijk (één bron, [1]).
- Geen zilvervolume per mijn, smelter of been; groepscijfer 714 t Ag/j (FY2022-23) [3] niet toegerekend. Reserve-ertsgehalte Sindesar Khurd 180 ppm Ag
  (HZL-presentatie 2011, [4]) is ouder dan het peiljaar en is geen productiecijfer.
- Geen gepubliceerde wegkilometer; §2 geeft de hemelsbrede afstand (5,4 km) en een OSRM-indicatie (5,4 km, niet-officieel). De ±15%-toets is indicatie.
- Of het concentraat per truck, interne spoorlijn of band gaat is niet gedocumenteerd; op de satelliet liggen rangeersporen en een transportband naast het
  mijnterrein. Getekend als één truckbeen over de lokale weg (aannemelijk).
- Als lijn op de bol is dit been ca. 5,5 km: bijna onzichtbaar op wereldschaal, zichtbaar als gloedhotspots op de twee ankers (laagste prioriteit).
- Het Dariba-anker is 0,4 km verschoven t.o.v. het Photon-punt (zie §3); `zilver-sitelaag.json` bevat geen Dariba-smelter en is niet aangepast.

## 8 · Bronnen
[1] Hindustan Zinc, "Dariba Smelting Complex" — RLE-zinkroute 250 kt/j, loodsmelter 120 kt/j, "leveraging nearby Rajpura Dariba and Sindesar Khurd mines",
zilver niet genoemd, locatie Rajsamand. https://www.hzlindia.com/what-we-do/metal-smelting-sites/dariba-smelting-complex
[2] Wikipedia, "Hindustan Zinc" — smelters en raffinaderijen Chanderiya, Debari, Dariba (Rajsamand); Pantnagar voor zilver bedoeld; mijnen Rajpura Dariba,
Sindesar Khurd, Kayad, Zawar. https://en.wikipedia.org/wiki/Hindustan_Zinc
[3] Hindustan Zinc Integrated Report FY2022-23, "How we operate our business" — Sindesar Khurd gebouwd 2007 (0,3 Mtpa), Rajpura Dariba Hydro-III 0,21 Mtpa,
nieuwe zilverraffinaderij Pantnagar 500 t, geraffineerd zilver 714 t. https://integratedreport.hzlindia.com/annual-integrated-report-fy-2022-23/how-we-operate-our-business.php
[4] Hindustan Zinc/Vedanta, investeerderspresentatie 2 maart 2011 — Sindesar Khurd: reserves 10,74 Mt, Ag 180 ppm, 0,5 Mtpa (uitbreiding naar 1,5 Mtpa);
Dariba Complex fase III: zinksmelter 210 kt/j, loodsmelter 100 kt/j. https://vedantaresources.com/uploads/investors-presentation/2011-03-02-hzlvisit-final-website.pdf
[5] Webzoekopdracht (1 van 3) naar HZL-materiaal over Sindesar Khurd en Dariba — bevestigt nabijheid van het complex aan beide mijnen en de claim dat
Sindesar Khurd "World's second-largest silver producing mine" is volgens HZL-factsheet (niet zelf geopend, daarom alleen als context). https://www.hzlindia.com/?p=1763
[6] `v2/design/zilver-sitelaag.json` (`w-sindesar-khurd` 24.9989, 74.1430, OSM landuse=quarry via Nominatim; `w-ref-chanderiya`) — hergebruikt anker en bronconflict.
[7] Esri World Imagery via `v2/tools/sat_check.py` (z14 + z16, live) — `v2/build-cache/satcheck/sat-zilver-sindesarkhurd-dariba-mijn-wijd.png` · `…-mijn-z16.png` ·
`…-smelter-wijd.png` · `…-smelter-z16.png`.
[8] Project OSRM (demo-router over OSM) — indicatieve rijafstand mijn → smelter 5,44 km; geometrie over de lokale weg west van Rajpura Dariba (alleen
corridorbevestiging, geen officiële bron). https://router.project-osrm.org
[9] OpenStreetMap-gegevens (Nominatim/Photon, ODbL) uit de haalbaarheidstoets — Sindesar Khurd Mine 24.9989, 74.1430; industrieel gebied Dariba 24.9543, 74.1324. https://www.openstreetmap.org
[10] Wikipedia, "Rajsamand district" — noemt de mijnen Dariba, Sindesar Khurd en Zawar in het district. https://en.wikipedia.org/wiki/Rajsamand_district
[11] `v2/design/routebrieven/zilver-rampuraagucha-pantnagar.md` — de andere HZL-keten; Chanderiya-smelter als stoppunt en de zilverraffinaderij-discussie (Pantnagar).

## 9 · Gebakken
**Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)** — `bash v2/tools/bak_stromen.sh zilver-sindesarkhurd-dariba` → `v2/data/stroomroute-zilver-sindesarkhurd-dariba.json` (1,5 KB, versie 2, `lonlat`).

| been | modaliteit | km | punten | geometrie |
|---|---|---|---|---|
| b1 | truck (doorgetrokken) | 6,0 (weggeometrie 5,5) | 36 | vooraf gebakken weg-geojson `zilver-sindesarkhurd-dariba-weg-sindesarkhurd-dariba.geojson` (profiel `zilver-sindesarkhurd-dariba-sindesarkhurd-dariba`, extract `india`) |

Totaal 6,0 km, 36 punten, 2 markers (`ag-sindesarkhurd-mijn` 24.9989,74.1430 en `ag-dariba-smelter` 24.9510,74.1330, beide 0,0 km van de lijn).

**Recept:** via-punten (lat,lon) 24.9989,74.1430 → 24.9884,74.1371 → 24.9755,74.1349 → 24.9665,74.1326 → 24.9565,74.1312 → 24.9510,74.1330; profiel in `maak_stroombeen_weg.py`; wegscan niet opnieuw gedraaid (geojson al aanwezig); `bak_zilver_sindesarkhurd_dariba` in `bak_stromen.sh` met één `--been-geojson "truck|…"` en twee `--marker`.

**Toets (§5):** km 5,5 tegen hemelsbreed/OSRM 5,4 = +1,9% (indicatie, geen wegkm gepubliceerd); grootste naad 0,72 km (< 5 km); markers 0,0 km van de lijn; `toets_knikken.py`: 2 knikken ≥ 60 gr, 0 omkeringen, 0 terugloop (beide zijn ankerstuk-hechtingen: 77 gr bij 24.99828,74.14471, 149 m van het mijnanker, en 74 gr bij 24.95317,74.13072, 15 m van de lijn; niet gerepareerd, geen terugloop); `toets_rechte_benen`: geen rechte benen ≥ 5 km.

**Toelichting:** geen stippel, geen haven-aanloop, geen vlucht, geen leiding, geen kopie. AANNEMELIJK (één bron) staat in de beennaam, niet in de lijnstijl. Stoppunt Dariba (§6).

**Lessen:** een kort eenbenig weg-been met een eerder gebakken geojson is in één bak-run klaar; de `bak_stromen.sh` gaf na de bak een syntaxfout van een andermans halfaf functie (olie-omisalj-pancevo, regel ~15535), niet van deze functie.
