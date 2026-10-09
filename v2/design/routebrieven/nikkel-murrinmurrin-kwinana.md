# Routebrief (licht) · nikkel — Murrin Murrin (Australië) → Leonora → Fremantle (Australië)

**stroom-id:** `nikkel-murrinmurrin-kwinana` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** LME-grade nikkelbriketten van Glencore's Murrin Murrin HPAL-plant (Laverton Shire, WA) gaan per **truck** naar Leonora, per **spoor** via Kalgoorlie, Southern Cross, Merredin en Northam naar Kewdale en de Fremantle North Quay-containerkade. Geen zeebeen en geen afnemer: de lijn stopt waar het bewijs stopt (aannemelijk: één bron voor de uitvoer via Fremantle).
**Welke as van het verhaal:** de enige grote Australische nikkelproducent die nog draait (Nickel West is stilgelegd) — 32 kt Ni in 2025, 34 kt in 2024 [2]; Glencore noemt 40,4 kt Ni voor 2022 [1]. Eenheid kt Ni per jaar.
**Afwijking van het ontwerp (bindende toets):** het id noemt Kwinana, maar de lijn eindigt op **Fremantle North Quay**. De Kwinana Bulk Jetty is in de enige primaire bron een zwavel-IMPORTjetty [5]; nikkelexport daar is niet gebrond.

## 1 · Ketenkaart
```
Murrin Murrin-plant `ni-murrinmurrin-plant`
  ──(b1 truck · eigen toegangsweg → Goldfields Highway · hemelsbreed 56 km, geen wegkm)──►
Leonora-spoorhoofd `ni-leonora-spoorhoofd`
  ──(b2 spoor · Kalgoorlie–Leonora-lijn · 259 km gepubliceerd)──► Kalgoorlie
  ──(b3-b5 spoor · Eastern Goldfields Railway via Southern Cross, Merredin · Kalgoorlie→Northam 505,4 km gepubliceerd)──► Northam
  ──(b6 spoor · Avon-vallei via Midland · ~110 km indicatie, geen gepubliceerde lengte)──► Kewdale (via-punt)
  ──(b7 spoor · Kewdale → Fremantle, kopie ree-mtweld-kuantan · ~20 km schatting)──►
Fremantle North Quay `ni-fremantle-kade` ⏹ stoppunt (aannemelijk: één bron)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-murrinmurrin-plant` → `ni-leonora-spoorhoofd` | eigen toegangsweg → Goldfields Hwy; **letterlijke kopie kobalt-murrinmurrin-kwinana b1** | hemelsbreed 56 km, geen wegkm; gemeten 65,9 (+16,8%, indicatie) [3] | kopie geojson | nee |
| b2 | A | spoor | Leonora → Kalgoorlie | Kalgoorlie–Leonora-lijn; **kopie kobalt b2** | 259 [7]; gemeten 261,0 | kopie geojson | nee |
| b3 | A | spoor | Kalgoorlie → Southern Cross | Eastern Goldfields Railway; **kopie kobalt b3** | 251,8 gemeten (deel van 505,4 [8]) | kopie geojson | nee |
| b4 | A | spoor | Southern Cross → Merredin | idem; **kopie kobalt b4** | 119,3 gemeten | kopie geojson | nee |
| b5 | A | spoor | Merredin → Northam | idem; **kopie kobalt b5** | 163,7 gemeten (b3–b5 samen 534,8 tegen 505,4 = +5,8%) | kopie geojson | nee |
| b6 | A | spoor | Northam → Kewdale | Avon-vallei-lijn via Midland (nieuwe run, geen corridorkeuze) | indicatie ~110, geen gepubliceerde lengte; gemeten 120,1 (hemelsbreed 77,2) | toets_spoorroute | nee |
| b7 | B | spoor | Kewdale → Fremantle North Quay | Fremantle-lijn; **kopie ree-mtweld-kuantan b2b** | ~20 schatting [9]; gemeten 42,7 (indicatie) | kopie geojson | nee |
Geen zeebeen, geen haven-aanloop, geen Kwinana. Fremantle North Quay snapt op 0,5 km van het spoor (binnen de norm).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-murrinmurrin-plant` | mijn/HPAL-plant | Murrin Murrin (Glencore), Laverton Shire | -28.7680, 121.8940 | [1][3]; hergebruik `co-murrinmurrin-plant` (kobalt-brief) | bron-gelegd (z15 opnieuw gezien: procesgebouwen en tankenpark in het midden, tailings-vijvers oost, grote pit- en afvalvlakken westelijk) |
| `ni-leonora-spoorhoofd` | overslag truck → spoor | Leonora (railhead) | -28.8845, 121.3308 | [7]; hergebruik `co-leonora-spoorhoofd` | aannemelijk (z15 gezien: de stad Leonora met het spoor net westelijk ervan; ankerpunt ligt in het stadscentrum, de exacte laadplek is niet te onderscheiden) |
| `ni-fremantle-kade` | overslag spoor → (zee, niet getekend) | Fremantle North Quay containerterminal | -32.0438, 115.7449 | [9]; hergebruik `ree-fremantle-kade` | bron-gelegd (z15 opnieuw gezien: containerkranen, stacks en schepen aan het kadefront, de ingang van de Swan-rivier ernaast) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | — | geen | — | enige toegangsweg, geen corridorkeuze (kopie); Malcolm/Menzies waren niet nodig [kobalt-brief §9] |
| b2 | — | geen | — | directe run volgt de enige lijn (261,0 km tegen 259) |
| b3–b5 | 1 | Southern Cross | -31.2306, 119.3278 | runsplitsing op het gepubliceerde deeltraject [8] |
| b3–b5 | 2 | Merredin | -31.4820, 118.2790 | tussenstad op de doorgaande hoofdlijn |
| b3–b6 | 3 | Northam | -31.6531, 116.6661 | splitsing waar de lijn de Avon-vallei in duikt (gebruikt als snap -31.6460, 116.6713) |
| b6–b7 | 4 | Kewdale | -31.9761, 115.9423 | splitst de run: voorkomt een Dijkstra-omweg via de goudlijn (ree-mtweld-kuantan §4) |
Broad Arrow is bewust géén via-punt (ligt op de b2-zijtak, kobalt-brief §9).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Murrin Murrin HPAL | Glencore (Minara Resources) | lateriet → LME-grade nikkel- en kobaltbriketten ter plekke | 40 kt Ni + 2,5 kt Co nameplate; 2022 werkelijk 40,4 kt Ni; 2025 32 kt Ni | [1][2][4] |

## 6 · Stoppunt
De brief stopt op Fremantle North Quay: één bron noemt de containerroute naar Fremantle (zwak, spoorfoto-onderschrift) en geen enkele bron noemt de bestemming of afnemer van het nikkel — dus geen zeebeen en geen fase D/E.

## 7 · Open punten
- **Uitvoerroute niet primair gebrond.** Glencore noemt "domestic and export markets" maar geen haven of vervoersmodaliteit [1]; de WA-bronnen noemen Kwinana alleen als zwavel-importjetty en Fremantle Port/Westrail alleen als projectimpact [5][6]. Dat de briketten per trein naar Fremantle gaan is aannemelijk (één bron, containers), niet bevestigd.
- **Esperance als alternatief.** v1 (`data/nickel.js`, `ni-port-esperance`) laat het nikkel per spoor naar Esperance gaan, en een WMC-brief aan de WA-regelaar beschrijft Leonora → Esperance als exportroute voor nikkelconcentraat (andere operatie) [11]. Niet getekend: de haalbaarheidstoets koos Fremantle; b1-b2 blijven in beide gevallen geldig.
- **Rail-head:** Malcolm (reisblog) of Leonora (kobaltbrief) liggen op dezelfde lijn; het Leonora-anker staat in het stadscentrum, niet op een gezien laadspoor.
- **b1 is hemelsbreed** (56 km, geen wegkm); de ±15%-toets is hier indicatie, geen norm.
- **b6/b7-lengtes zijn schattingen** (Northam-Kewdale ~110, Kewdale-Fremantle ~20); geen bron geeft de doorgaande lengte, gemeten 120,1 en 42,7 km.
- **Product op het spoor niet bevestigd:** de Leonora-lijn draagt volgens Wikipedia vooral inkomend zwavel/ammoniak [7].
- **Afnemer/bestemming onbekend** — Chinese of Europese afnemers zijn niet gebrond; geen zeebeen getekend.

## 8 · Bronnen
[1] Glencore Australia, "The Murrin Murrin Operations" — 2022: 40,4 kt Ni, 3,3 kt Co; briketten voor binnenlandse en exportmarkt. https://glencore.com.au/operations-and-projects/minara/who-we-are/murrin-murrin
[2] miningdataonline, "Murrin Murrin Mine" — Active; Ni 2021-2025 30/36/31/34/32 kt. https://miningdataonline.com/property/429/Murrin-Murrin-Mine.aspx
[3] Wikipedia, "Murrin Murrin Mine" — coördinaat -28.7675/121.8939, ~45 km oost van Leonora. https://en.wikipedia.org/wiki/Murrin_Murrin_Mine
[4] Mining Technology, "Murrin Murrin Nickel-Cobalt Project" — ontwerp 40 kt Ni, briketten; 2006: 31.524 t Ni. https://www.mining-technology.com/projects/murrin/
[5] WA Government, "New bulk cargo jetty at Kwinana to service nickel project at Murrin Murrin" (1998) — zwavelimport; 74 Westrail-wagons, 168 containers; Brambles-loods. https://www.wa.gov.au/government/media-statements/Court%20Coalition%20Government/New-bulk-cargo-jetty-at-Kwinana-to-service-nickel-project-at-Murrin-Murrin-19981030
[6] WA Government, "Official opening of Anaconda Nickel's Murrin Murrin project" (1997) — project raakt Fremantle Port en het Westrail-net. https://www.wa.gov.au/government/media-statements/Court%20Coalition%20Government/Official-opening-of-Anaconda-Nickel's-Murrin-Murrin-project-19970915
[7] Wikipedia, "Leonora railway line" — Kalgoorlie-Leonora 259 km. https://en.wikipedia.org/wiki/Leonora_railway_line
[8] Wikipedia, "Eastern Goldfields Railway" — Northam-Southern Cross 281,9 km, Southern Cross-Boorabbin 97,7, Boorabbin-Kalgoorlie 125,8. https://en.wikipedia.org/wiki/Eastern_Goldfields_Railway
[9] `v2/design/routebrieven/ree-mtweld-kuantan.md` §3/§4/§8 — anker Fremantle North Quay, Kewdale-via-punt, spoor Kewdale-Fremantle.
[10] `v2/design/routebrieven/kobalt-murrinmurrin-kwinana.md` — ankers plant/Leonora, benen b1-b5 (kopieën), Broad Arrow-bevinding. RailPictures-foto 644994 (containers naar Fremantle) was 403 en is alleen via de haalbaarheidstoets bekend. https://web.railpictures.net/photo/644994
[11] ERA WA, WMC Resources-brief — nikkelconcentraat per spoor Leonora → Esperance (andere operatie). https://www.erawa.com.au/cproot/3316/2/kalesp_wmc.pdf
[12] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-nikkel-murrinmurrin-kwinana-plant.png`, `-leonora.png`, `-fremantle.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)

**Bestand:** `v2/data/stroomroute-nikkel-murrinmurrin-kwinana.json` · 36,9 KB · versie 2, lonlat · 7 benen, 1.025,2 km, 1.784 punten, 3 markers. Recept: `bak_nikkel_murrinmurrin_kwinana` in `v2/tools/bak_stromen.sh` (geen profiel, geen scan, geen stippel, geen zeebeen, geen aanloop).

| # | modaliteit | km | brief | afwijking | geometrie |
|---|---|---|---|---|---|
| b1 | truck plant → Leonora | 65,9 | hemelsbreed 56, geen wegkm | +16,8% (indicatie) | letterlijke kopie kobalt-murrinmurrin-kwinana b1 |
| b2 | spoor Leonora → Kalgoorlie | 261,0 | 259 | +0,8% | kopie kobalt b2 |
| b3 | spoor Kalgoorlie → Southern Cross | 251,8 | deel van 505,4 | b3-b5 samen 534,8 (+5,8%) | kopie kobalt b3 |
| b4 | spoor Southern Cross → Merredin | 119,3 | idem | idem | kopie kobalt b4 |
| b5 | spoor Merredin → Northam | 163,7 | idem | idem | kopie kobalt b5 |
| b6 | spoor Northam → Kewdale | 120,8 | indicatie ~110 | +9,8% (indicatie) | toets_spoorroute, al gedraaid (brief noemde 120,1; console 120,8) |
| b7 | spoor Kewdale → Fremantle North Quay | 42,7 | ~20 schatting | indicatie | kopie ree-mtweld-kuantan (bak_ree_mtweld_kuantan, been 3) |

**Markers:** `ni-murrinmurrin-plant` (0,0 km van de lijn), `ni-leonora-spoorhoofd` (0,0 km), `ni-fremantle-kade` (0,51 km: kadepunt ligt naast het spoor, bekend uit ree-mtweld-kuantan).

**Naden:** alle 0 m behalve Leonora (b1 eindigt op het anker, b2 begint op het spoor): 499 m, het procesgat van de kobalt-stroom, blijft staan. Geen naad > 5 km.

**Toelichting.** Geen stippel: elk been is een gemeten of gekopieerd spoor/weg. Geen haven-aanloop: er is geen zeebeen en de lijn stopt op de kade. Geen vlucht of leiding. b1-b5 en b7 zijn letterlijke kopieën (noemt de beennaam); alleen b6 is nieuw. De km-toets is voor b1, b6, b7 een indicatie (brief geeft hemelsbreed of een schatting); de gepubliceerde b2 (+0,8%) en b3-b5 (+5,8%) vallen binnen de ±15%.

**Toetsen.** `toets_knikken`: 5 knikken, 2 omkeringen (Kalgoorlie-zijpunt in b2, Kewdale-Fremantle in b7), 0 terugloop; allemaal uit de gekopieerde benen en als echte spoorbocht beoordeeld. `toets_rechte_benen --min-km 5`: geen bevinding voor deze stroom. `bak_stromen.sh` is LF (0 CRLF).

**Lessen.** (1) De drie gedeelde ankers waren al gelegd; hergebruik kostte geen satellietrun. (2) Het id noemt Kwinana, de lijn eindigt op Fremantle: titel en kop zeggen dat. (3) Open punten uit §7 blijven: uitvoerroute Fremantle is aannemelijk (één bron), Esperance niet getekend, Leonora-anker in het stadscentrum.
