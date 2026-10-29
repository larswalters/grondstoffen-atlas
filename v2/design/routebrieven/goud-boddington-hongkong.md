# Routebrief (licht) · Goud — Boddington → Perth Mint Refinery → Hongkong (Australië)

**stroom-id:** `goud-boddington-hongkong` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 12) ·
**status:** gebakken
**Keten in één zin:** doré-goud van de Boddington-mijn (Newmont, Westelijk Australië) per truck over Albany Highway 30 en
Tonkin Highway 4 naar de Perth Mint Refinery bij Perth Airport, per vrachtvlucht (grootcirkel) PER → HKG naar de
Cathay-vrachtterminal van Hongkong, waar de lijn stopt (afnemer onbekend).
**Welke as van het verhaal:** Australië → Hongkong, de grootste bestemming van de Australische goudexport: 80,3 t Au
(USD 5,82 mrd), 2024, partner 344 [1]. Boddington zelf: 745.000 oz ≈ 23,2 t Au (2023) [2]; welk deel naar Hongkong gaat is niet gepubliceerd.

## 1 · Ketenkaart
```
Boddington-installatie (Newmont) `au-boddington-plant`
  ──(b1 truck · Gold Mine Rd → Bannister-Marradong Rd → Albany Hwy 30 → Tonkin Hwy 4 · OSRM-indicatie 129,6 km, hemelsbreed 93,8)──►
Perth Mint Refinery, Perth Airport `au-ref-perthmint-airport`
  ── naad 1,9 km (geen b2, binnen luchthavenareaal) ──
Qantas Freight Int'l Terminal, PER `au-per-cargo` (hergebruikt uit goud-kalgoorlie-singapore)
  ──(b2 lucht · vlucht PER → HKG, grootcirkel, aannemelijk · 6.035,6 km)──►
Cathay Pacific Cargo Terminal, Chek Lap Kok `au-hkg-vrachtterminal` (hergebruikt anker dia-hkg-cargo) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Boddington-installatie → Perth Mint Refinery | Gold Mine Road, Bannister-Marradong Road, Albany Highway 30, Tonkin Highway 4, Horrie Miller Drive [7] | **hemelsbreed 93,8 km, geen wegkm**; OSRM-indicatie 129,6 km [7] (±15% = indicatie, geen norm) | maak_stroombeen_weg (extract australie) | nee |
| b2 | B | lucht | PER-vrachtterminal → HKG-vrachtterminal | vrachtvlucht PER → HKG, grootcirkel — **aannemelijk: één bron** (Perth Mint noemt vluchten en Hongkong als bestemming [5]; Comtrade geeft de handel [1]), niet voor déze lading | 6.035,6 [berekend, grootcirkel] | maak_luchtbeen | nee — doorgetrokken |

De raffinaderij ligt landside bij Horrie Miller Drive, 1,9 km van `au-per-cargo`: geen b2-truck (haalbaarheidstoets, BINDEND); de naad van 1,9 km is
onder de 5 km-norm. Het ontwerp-been East Perth → PER (kopie van goud-kalgoorlie-singapore b2) vervalt: die route ging 15 km terug.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-boddington-plant` | mijn / verwerkingsinstallatie | Boddington Gold Mine, processing plant (Newmont) | -32.7385, 116.3565 | [2][14] | bron-gelegd (z15 gezien: erts-/verwerkingscomplex met tanks, schoorsteen en transportbanden direct NO van de hoofdpit; het sitelaag-punt -32.75, 116.355 ligt in de pit, 1,3 km zuidelijker) |
| `au-ref-perthmint-airport` | raffinaderij / laadplek | Perth Mint Refinery, Perth Airport estate (OSM landuse industrial, way 555255739) | -31.9617, 115.9684 | [6][14] | bron-gelegd (z15+z17 gezien: industrieel gebouwencluster direct O van Tonkin Hwy en W van Horrie Miller Drive, openbare weg binnen 100 m) |
| `au-per-cargo` | overslag / lucht | Qantas Freight International Terminal, Affleck Road, Perth Airport | -31.9460, 115.9764 | [9][10] | bron-gelegd, letterlijk hergebruikt uit `goud-kalgoorlie-singapore.md` (hier z15 opnieuw gezien: loods-/kantoorcluster ZO van de terminalring; geen bron dat déze terminal Perth Mint-baren afhandelt, zie §7) |
| `au-hkg-vrachtterminal` | overslag / lucht | Cathay Pacific Cargo Terminal, Chek Lap Kok (HKG) | 22.2975, 113.9247 | [11][15] | bron-gelegd, letterlijk hergebruikt `dia-hkg-cargo` (diamant-surat-hongkong.md; zie ook goud-metalor-hongkong.md) |

## 4 · Via-punten (alleen b1; punten uit OSRM-stappen, dus óp een wegvertex [7])
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Gold Mine Road / Bannister-Marradong Road | -32.7838, 116.4809 | pint de oostelijke uitgang van het mijnterrein, sluit de route via Boddington-stad uit |
| b1 | 2 | Albany Highway 30, begin (North Bannister) | -32.6929, 116.5245 | pint Albany Hwy 30 als hoofdcorridor naar het noorden, sluit South Western Hwy via Pinjarra uit |
| b1 | 3 | Tonkin Highway 4, oprit (Kelmscott/Gosnells-rand) | -32.0859, 116.0170 | pint Tonkin Hwy i.p.v. Albany Hwy door Armadale/Gosnells-centrum; óp de snelweg, niet in een stad |
| b1 | 4 | Tonkin Highway afrit Horrie Miller Drive | -31.9765, 115.9706 | pint de afrit naar het luchthavenareaal en de raffinaderij |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Boddington-installatie | Newmont | erts → doré plus Cu-Au-concentraat (concentraat gaat niet naar de Mint) | 745.000 oz Au (2023) ≈ 23,2 t | [2][12] |
| Perth Mint Refinery | The Perth Mint (West-Australische overheid) | doré → LBMA-baren | 1.000 t edelmetaal/j capaciteit; 195,8 t goud van resources-klanten 2025-26 [4]; ≈79% van de Australaziatische mijnproductie (2019) [3] | [3][4] |

## 6 · Stoppunt
De brief stopt bij de Cathay-vrachtterminal in Hongkong: er is geen bron die deze baren aan een Hongkongse afnemer koppelt
(distributeurs als PMHK zijn alleen als lijst gevonden [5]). Fase D vervalt, fase E vervalt.

## 7 · Open punten
- **Boddington → Perth Mint is niet op mijnniveau gebrond:** alleen Perth Mint als verwerker van 79% van de Australaziatische productie [3] en Gold Fields als analoog [13]; aanname = doré naar de Mint.
- **PER → HKG voor déze lading niet gebrond:** Comtrade (motCode 0) geeft de handel, geen vervoerswijze [1]; Perth Mint noemt "flight schedules" en Hongkong als bestemming [5]. Eén directe vlucht aangenomen, geen tussenlanding gebrond.
- **Perth Mint-pagina [4] noemt de luchthavenligging niet;** die komt uit OSM (landuse "Perth Mint Refinery", Perth Airport) [6]. Eerdere briefs schreven het aan [4] toe.
- **`au-per-cargo`:** welke vrachtterminal de Mint gebruikt (Qantas Freight of dnata) is niet gebrond; terminal ZO van de ring, geen naamtag in OSM.
- **Sitelaag-afwijking:** `w-boddington` staat op -32.75, 116.355 (in de pit); de installatie ligt op -32.7385, 116.3565. Niet gewijzigd (sitelagen zijn van de orchestrator).
- **b1 heeft geen gepubliceerde wegkm** (alleen OSRM 129,6 km); Hongkongse afnemer onbekend; concentraatstroom (Cu-Au) is niet gebrond en niet getekend.
- **Volume:** Boddington 23,2 t Au/j (2023) [2]; Australië → Hongkong 80,3 t (2024) [1]. Het aandeel Boddington in die 80,3 t is niet gepubliceerd.

## 8 · Bronnen
[1] UN Comtrade API (preview), Australië export HS 7108, 2024, partner 344 Hongkong: netto 80.289,9 kg, USD 5,82 mrd (wereld 320,3 t). https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=36&period=2024&cmdCode=7108&flowCode=X
[2] Wikipedia, "Boddington Gold Mine": eigenaar Newmont, 745.000 oz (2023), goud + koper, 13 km NW van Boddington. https://en.wikipedia.org/wiki/Boddington_Gold_Mine
[3] Wikipedia, "Perth Mint": ≈79% van de Australaziatische goudproductie (nov 2019), raffinage op apart beveiligd terrein buiten het centrum. https://en.wikipedia.org/wiki/Perth_Mint
[4] The Perth Mint, Refinery: capaciteit 1.000 t/j, 195,8 t goud van resources-klanten 2025-26. https://www.perthmint.com/refinery-treasury/refinery/
[5] The Perth Mint, Shipping and delivery: secure carrier, vluchtschema's, Hongkong als toegestane bestemming; distributeurs Azië: https://www.perthmint.com/customer-care/shipping-and-delivery/ · https://www.perthmint.com/customer-care/find-a-distributor/bullion-distributors/asia/
[6] OpenStreetMap/Nominatim (ODbL, 2026-10-29): "Perth Mint Refinery", landuse industrial, way 555255739, -31.9617/115.9684, Perth Airport. https://nominatim.openstreetmap.org
[7] OSRM (router.project-osrm.org, OSM, 2026-10-29): Boddington-installatie → Perth Mint Refinery 129,6 km via Gold Mine Rd, Bannister-Marradong Rd, Albany Hwy 30, Tonkin Hwy 4, Horrie Miller Dr; stappunten als via-punten.
[8] Wikipedia, "Perth Airport". https://en.wikipedia.org/wiki/Perth_Airport
[9] Qantas Freight, Perth international handling, 24 Affleck Road. https://freight.qantas.com/au-en/freight-terminals/australia/international/international-handling-perth.html
[10] `v2/design/routebrieven/goud-kalgoorlie-singapore.md` (anker `au-per-cargo`, -31.9460/115.9764).
[11] `v2/design/routebrieven/diamant-surat-hongkong.md` en `goud-metalor-hongkong.md` (anker `dia-hkg-cargo` = `au-hkg-vrachtterminal`, 22.2975/113.9247).
[12] Newmont 10-K (doré plus Cu-Au-concentraat, via de haalbaarheidstoets; niet zelf geopend).
[13] Gold Fields 20-F (alle Australische productie bij de Perth Mint, via de haalbaarheidstoets; niet zelf geopend).
[14] Satellietblik Esri World Imagery (z14–z17, 2026-10-29): `v2/build-cache/satcheck/sat-goud-boddington-hongkong-boddington-pit.png`, `-boddington-plant.png`, `-perthrefinery.png`, `-perthrefinery-z17.png`, `-percargo.png`.
[15] Wikipedia, "Hong Kong International Airport". https://en.wikipedia.org/wiki/Hong_Kong_International_Airport

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 12)
`v2/data/stroomroute-goud-boddington-hongkong.json` · 32,6 KB · versie 2, lonlat · 2 benen · 6.165,0 km · 1.480 punten · 4 markers · geen stippel.

| # | modaliteit | km gebakken | km brief | naad naar volgend been |
|---|---|---|---|---|
| b1 | truck (doorgetrokken) | 129,4 | geen wegkm; OSRM-indicatie 129,6 (hemelsbreed 93,8) | 1,9 km (raffinaderij naar au-per-cargo, <5 km) |
| b2 | lucht (doorgetrokken) | 6.035,6 | 6.035,6 grootcirkel | stoppunt |

**Recept:** b1 = profiel `goud-boddington-hongkong-boddington-perthmint` (`maak_stroombeen_weg.py`, extract australie, refs 30 en 4, vensterKm 40, eindToegangPrivaat) via `wegscan_puur.py`; lengtetoets 129,2 km tegen 130 = -0,6 procent (indicatie, geen norm). Snaps 0,00 tot 0,09 km, geen via-punt > 5 km, 17 keerlussen gesnoeid (0,1 km). b2 = `maak_luchtbeen.py` PER naar HKG, 243 punten. Functie `bak_goud_boddington_hongkong` in `bak_stromen.sh`.

**Toelichting:** geen stippel, geen haven-aanloop (geen zeebeen), geen airside-stippel: de raffinaderij ligt landside en het PER-vrachtplatform wordt niet door een truck bereikt. De vlucht PER naar HKG is aannemelijk (een bron voor Perth naar Hongkong, niet voor deze lading), één directe vlucht aangenomen. Markers: allemaal 0,0 km van de lijn. `toets_knikken`: 5 knikken op het truckbeen (vier spikes op via-puntsnaps en bij de plant, één krappe bocht), 0 omkeringen, 0 terugloop. De naad van 1,9 km is een procesgat binnen het luchthavenareaal en blijft staan.

**Lessen:** (1) de brief gaf een OSRM-indicatie, geen gepubliceerde wegkm; de gebakken 129,4 km valt er toevallig op omdat het OSM-pad dezelfde corridor volgt. (2) Het hergebruikte anker au-per-cargo is niet voor deze lading gebrond. (3) Sitelaag w-boddington (-32,75, 116,355) ligt in de pit en staat 1,3 km van het plant-anker; niet gewijzigd (centraal).
