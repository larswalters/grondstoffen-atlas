# Routebrief (licht) · Uranium — Novosibirsk → Adana → Akkuyu (Rusland/Turkije, peiljaar 2023)

**stroom-id:** `uranium-novosibirsk-akkuyu` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) ·
**status:** gebakken
**Keten in één zin:** VVER-1200-splijtstof (eerste kernlading Akkuyu-1) van TVEL NZHK in Novosibirsk gaat per truck naar het vrachtplatform van
Tolmachevo (OVB, aannemelijk), per vrachtvlucht (grootcirkel) naar het vrachtplatform van Adana Şakırpaşa (ADA) en per truck (O-51, D400 via Mersin en
Silifke) naar de kerncentrale Akkuyu — **stoppunt**: de reactor.
**Welke as van het verhaal:** *Rosatom-brandstof per lucht naar Turkije: NZHK → Akkuyu.* Volume: de eerste partij kernbrandstof kwam april 2023 aan [1][2]
(nacht ervoor per vliegtuig uit Rusland, daarna 3 trucks); aantal assemblages per zending niet gepubliceerd. Eigen schatting voor een volle kern:
≈ 79 t U (163 assemblages × ~0,48 t U, Rooppur-analogie [9]) — geen gepubliceerd cijfer. Eenheid t U/j, peiljaar 2023.

## 1 · Ketenkaart
```
TVEL Novosibirsk Chemical Concentrates Plant (NZHK) `u-nzhk`
  ──(b1 truck · LETTERLIJKE KOPIE van uranium-novosibirsk-rooppur b1 · Ob-oversteek, door de stad · 30,5 km gemeten · aannemelijk: geen bron noemt de rit)──►
Tolmachevo (OVB) vrachtplatform `u-ovb-vrachtplatform`   [b1s stippel 0,26 km airside, LETTERLIJKE KOPIE uit rooppur]
  ──(b2 lucht · vlucht OVB → ADA, grootcirkel 4.065,5 km · aannemelijk: vertrekluchthaven niet genoemd)──►
Adana Şakırpaşa (ADA) vrachtapron `u-ada-vrachtapron`   [b2s stippel 0,53 km airside/last mile → openbare weg Dumlupınar]
  ──(b3 truck · O-51 ring N van Mersin → D400 via Silifke · hemelsbreed 182,6 km, geen wegkm · aannemelijk: bron noemt alleen "3 trucks overland")──►
Akkuyu kerncentrale (Büyükeceli, Mersin) `u-akkuyu` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | NZHK → OVB landside | Ob-oversteek, door Novosibirsk (router-keuze) | 30,5 gemeten (rooppur-bake); geen wegkm | **kopie** `uranium-novosibirsk-rooppur-weg-nzhk-ovb.geojson` | nee — *aannemelijk* |
| b1s | D | truck | OVB landside → vrachtplatform | luchthaventerrein | 0,26 (eigen meting) | **kopie** stippel 55.0042,82.6428 → 55.0065,82.6420 | **ja — airside, geen wegpad** |
| b2 | D | lucht | OVB → ADA | vrachtvlucht: "brought by air the night before from Russia to Adana Airport" [1][2] | grootcirkel 4.065,5 (berekend) | maak_luchtbeen | nee — doorgetrokken, *aannemelijk: vertrekluchthaven niet genoemd* |
| b2s | D | truck | ADA vrachtapron → openbare weg | apron/terminal → Dumlupınar (secondary) | 0,53 (eigen meting) | rechte stippel | **ja — airside/privéterrein, geen wegpad** |
| b3 | D | truck | ADA landside → Akkuyu | O-51 (ring N van Mersin) → D400 (Mersin–Silifke–Büyükeceli) | **hemelsbreed 182,6 km, geen wegkm**; OSRM-indicatie 212 [13]; gescand 213,5 | maak_stroombeen_weg (turkije) | nee — *aannemelijk: bron noemt alleen 3 trucks overland* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-nzhk` | fabriek (kop) | Novosibirsk Chemical Concentrates Plant (TVEL/Rosatom) | 55.0909, 82.9847 | HERGEBRUIK uit `uranium-novosibirsk-rooppur.md` (OSM-way 51916722) [1][9] | bron-gelegd (rooppur: z15 gezien, groot industrieterrein oostrand Novosibirsk) |
| `u-ovb-vrachtplatform` | overslag truck → lucht | Tolmachevo (OVB) vrachtplatform, apron met pakhuis ten zuiden van de baan | 55.0065, 82.6420 | HERGEBRUIK uit rooppur-brief | **aannemelijk** (vrachtterminal niet bij naam te vinden) |
| `u-ada-vrachtapron` | overslag lucht → truck | Adana Şakırpaşa (ADA), betonnen apron voor het terminalgebouw ten zuiden van de baan | 36.9840, 35.2930 | [6] wiki-luchthaven 36.9819, 35.2803 (midden baan); apron eigen keuze | **onzeker** (z15 + z16 gezien: baan 05/23 met één groot betonnen platform met geparkeerde toestellen en een terminalgebouw aan de oostzijde; geen herkenbare vrachtloods of vrachtterminal, geen bron noemt de plek) |
| `u-ada-landside` | routeerpunt (geen marker) | Dumlupınar (secondary), oostrand luchthaven | 36.9834, 35.2989 | [11] Nominatim-reverse (snap 0,00 km in de scan) | routeerpunt, geen anker |
| `u-akkuyu` | reactor (eindpunt) | Akkuyu NPP, Büyükeceli (Mersin) | 36.1444, 33.5411 | [5] wiki-coördinaat 36.14444, 33.54111 | bron-gelegd (z15 gezien: omheind centralecomplex met reactor- en turbinegebouwen aan de kust, havenhoofden en bouwterrein ten zuiden; kruis op de reactorgebouwen) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze; op de doorgaande weg)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | — | geen (kopie) | — | zie rooppur-brief: router-keuze Ob-oversteek |
| b3 | 1 | O-51 noordelijke ring buiten Mersin | 36.8893, 34.6413 | sluit D400 door het centrum van Mersin uit; OSM-motorway ref O-51 (snap 0,00 km) |
| b3 | 2 | D400 oost van Silifke | 36.3815, 34.0336 | D400-trunk ~8 km vóór Silifke; houdt de lijn op de kustweg (snap 0,00 km) |

Zonder via-punten kiest de router D400 dwars door Mersin (200,4 km); met de twee via-punten rijdt hij O-51 + D400 (213,5 km, = OSRM 212). Gescand met `wegscan_puur.py`-wrapper, extract `turkije`, venster 55 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| NZHK (Novosibirsk) | TVEL / Rosatom | uraniumoxide → VVER-assemblages | ≈ 1.200 t HM/j (sitelaag-indicatie, alle klanten) | [1][sitelaag] |
| Akkuyu (4 × VVER-1200, 4.800 MWe) | Akkuyu Nuclear / Rosatom | splijtstof → elektriciteit | 163 assemblages per kern; eenheid 1 eerste lading 2023, eenheid 2 batch eind dec 2024 [4][8] | [4][8] |

## 6 · Stoppunt
De brief stopt bij de reactor: Akkuyu is de enige afnemer en geen bron noemt een volgende locatie (E vervalt). Fase D is hier de hele keten: NEI noemt NZHK als
fabrikant, de nachtvlucht naar Adana en de 3 trucks naar de site [1]; luchthaven van vertrek en het wegtracé zijn aanvullingen.

## 7 · Open punten
- **ADA-vrachtplatform niet te identificeren** (z15/z16): één groot betonplatform met terminalgebouw, geen vrachtloods; punt 36.9840, 35.2930 is de apron (status onzeker). Wikipedia beschrijft ADA nu als overwegend general aviation [6]; bronnen zeggen alleen "Adana Airport" [1][2].
- **Vertrekluchthaven niet genoemd:** OVB is aannemelijk (NZHK in Novosibirsk, rooppur-analogie); een vrachtterminal is niet bij naam gevonden.
- **Wegroute Adana → Akkuyu niet gepubliceerd:** bron noemt alleen "loaded on three trucks and transported to the Akkuyu site over land" [1][2]; O-51/D400 is de kortste weg (OSRM 212, scan 213,5), geen bron-wegkm (hemelsbreed 182,6 km).
- **Laatste ~3,9 km binnen het Akkuyu-terrein** lopen over service/unclassified (scan); deels privéterrein, geen bron voor de poort.
- **Eén vlucht getekend:** geen vluchtenlijst, geen tussenlanding genoemd; aantal assemblages per zending onbekend.
- **Eenheid 2 (eind dec 2024):** een zoekuittreksel (niet gelezen) zegt "land and sea" in lekdichte containers, dus mogelijk niet per vlucht [8]; hier is alleen de gedocumenteerde vlucht van april 2023 getekend.
- **Sitelaag:** `uranium-sitelaag.json` heeft geen Akkuyu-site (centraal bijwerken, niet aangepast).

## 8 · Bronnen
[1] Nuclear Engineering International, 2023-04-27 — "First fuel delivered to Türkiye's Akkuyu NPP": brandstof van NZHK/TVEL, de nacht ervoor per vliegtuig uit Rusland naar Adana Airport, daarna drie trucks over land. https://www.neimagazine.com/news/first-fuel-delivered-to-trkiyes-akkuyu-npp-10797897
[2] Turkse ministerie van Energie, 2023-04-27 — "Türkiye's first nuclear plant gains official nuclear facility status with arrival of fuel": naar Adana Airport, drie trucks naar de Akkuyu-site. https://enerji.gov.tr/news-detail?id=21146
[3] NucNet, 2023-04-28 — "Russia delivers first batch of fuel for Akkuyu nuclear station": NZHK als fabrikant; geen transportdetails. https://www.nucnet.org/news/russia-delivers-first-batch-of-fuel-for-akkuyu-nuclear-station-4-5-2023
[4] World Nuclear Association — Nuclear Power in Turkey: Akkuyu bij Mersin, eerste kernbrandstof april 2023, 163 assemblages/kern. https://world-nuclear.org/information-library/country-profiles/countries-t-z/turkey
[5] Wikipedia, "Akkuyu Nuclear Power Plant" — 36.14444 N 33.54111 E (API). https://en.wikipedia.org/wiki/Akkuyu_Nuclear_Power_Plant
[6] Wikipedia, "Adana Airport" — 36.98194 N 35.28028 E, baan 05/23 2.750 m, nu general aviation. https://en.wikipedia.org/wiki/Adana_Airport
[7] World Nuclear News, 2023-03-01 — "Nuclear fuel to be delivered to Akkuyu 'this spring'". https://world-nuclear-news.org/articles/nuclear-fuel-to-be-delivered-to-akkuyu-this-spring
[8] WebSearch-samenvatting 2026-10-31 (pagina's niet gelezen; genoemd: Akkuyu Nuclear, NEI) — Akkuyu-2 brandstofbatch eind december 2024 van NZHK, mogelijk land en zee; zoekresultaat https://neimagazine.com/?p=66259
[9] `v2/design/routebrieven/uranium-novosibirsk-rooppur.md` — NZHK- en OVB-anker, b1 (30,5 km) en OVB-stippel; 163 assemblages × ~0,48 t U (eigen schatting).
[11] OpenStreetMap via Nominatim reverse — Dumlupınar (secondary) 36.98342, 35.29889. https://nominatim.openstreetmap.org
[12] OSM-pbf `turkije` (Geofabrik) via `wegscan_puur.py`: O-51 en D400 als trunk/motorway-ways, via-punten 36.8893, 34.6413 en 36.3815, 34.0336.
[13] Haalbaarheidstoets (OSRM-indicatie 212 km, O-51 Adana–Silifke, dan D400).
[sitelaag] `v2/design/uranium-sitelaag.json` — NZHK-capaciteit ~1.200 t HM/j.
Eigen scans en berekeningen: `maak_luchtbeen.py` OVB → ADA 4.065,5 km (164 punten); wegscan 2026-10-31. Satellietblik: `v2/build-cache/satcheck/sat-uranium-novosibirsk-akkuyu-ada.png`, `-ada-apron.png` (z16), `-akkuyu.png` (Esri z15, 2026-10-31).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
Recept: `bash v2/tools/bak_stromen.sh uranium-novosibirsk-akkuyu` (functie `bak_uranium_novosibirsk_akkuyu`) → `v2/data/stroomroute-uranium-novosibirsk-akkuyu.json`
(68,2 KB, versie 2, punt_formaat lonlat, 5 benen, 3.430 punten, 4 markers, totaal 4.310,6 km). Wegprofiel `uranium-novosibirsk-akkuyu-ada-akkuyu` (extract `turkije`,
`wegscan_puur.py`, refs O-51 en D400, venster 55 km); luchtbeen via `maak_luchtbeen.py`; b1/b1s zijn kopieën uit `bak_uranium_novosibirsk_rooppur`.

| # | modaliteit | been | km gebakken | km brief | naden | toets |
|---|---|---|---|---|---|---|
| b1 | truck | NZHK → OVB landside (kopie rooppur, doorgetrokken) | 30,5 | geen wegkm; 30,5 gemeten (rooppur) | — | identiek aan rooppur |
| b1s | truck | OVB landside → vrachtplatform (stippel, kopie) | 0,26 | 0,26 | 0,0 | airside, geen wegpad |
| b2 | lucht | OVB → ADA, grootcirkel (doorgetrokken) | 4.065,5 | 4.065,5 | 0,0 | berekend |
| b2s | truck | ADA-vrachtapron → Dumlupınar (stippel) | 0,53 | 0,53 | 0,0 | airside, geen wegpad |
| b3 | truck | ADA landside → Akkuyu (O-51, D400; doorgetrokken) | 213,8 | hemelsbreed 182,6, geen wegkm; OSRM 212 | 0,0 | +0,8% tegen OSRM (indicatie, geen norm) |

Markers (afstand tot de lijn 0,0 km, ze liggen op de lijnuiteinden): `u-nzhk`, `u-ovb-vrachtplatform`, `u-ada-vrachtapron` (onzeker), `u-akkuyu`.
Geen naad > 5 km; `toets_rechte_benen.py --min-km 5` toont geen rechte doorgetrokken lijn; `toets_knikken.py`: 37 knikken, 0 terugloop (spikes in de stadsdoorsteek
Novosibirsk, de kopie uit rooppur, en op het Akkuyu-terrein/aansluitingen D400).

**Toelichting per stippel/vlucht**
- **b1s en b2s (stippel):** de vrachtplatforms van OVB en ADA liggen airside zonder gekarteerd wegpad; het wegbeen eindigt op de openbare weg en de korte stippel
  (0,26 en 0,53 km) overbrugt het platform. Stippel = "hier reikt het net niet".
- **b2 (vlucht):** één grootcirkel OVB → ADA, doorgetrokken; *aannemelijk: vertrekluchthaven niet genoemd* staat in de beennaam. Eén vlucht, geen tussenlanding.
- **Geen** haven-aanloop, zee- of spoorbeen, geen leiding.

**Lessen**
- `wegscan_puur.py` schreef in het geojson `bron` de tekst "mozambique-latest; routebrief grafiet-balama-vidalia" (vaste tekst van het gereedschap, niet de werkelijke extract): bron is
  Geofabrik turkije. Gemeld, niet aangepast.
- Via-punten O-51 ring en D400 oost van Silifke gaven snap 0,00 km en geen omweg (213,5 km tegen 200,4 km zonder, door Mersin).
- Een eerdere scan in de scratchpad-wrapper gaf hetzelfde resultaat (213,5 km, 2.758 punten); herhaald met het profiel in `maak_stroombeen_weg.py`.
- Registratie, bundel en sitelaag (Akkuyu ontbreekt in `uranium-sitelaag.json`) zijn centraal.
