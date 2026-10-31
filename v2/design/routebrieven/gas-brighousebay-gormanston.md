# Routebrief (licht) · gas — Brighouse Bay (Schotland) → Gormanston (Ierland)

**stroom-id:** `gas-brighousebay-gormanston` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) ·
**status:** gebakken
**Keten in één zin:** Brits netgas (NTS) wordt bij Beattock/Moffat afgetakt, gaat door een 36-inch landleiding naar het
compressorstation Brighouse Bay (Dumfries and Galloway) en vandaar door Interconnector 2 (IC2, 30 inch, 193 km, onder de
Ierse Zee) naar het Gas Networks Ireland-terrein (AGI) bij Gormanston, County Meath: de aanvoerader van ruim drie kwart van de Ierse gasvraag.
**Welke as van het verhaal:** Ierland als pijpgas-importeur van het Britse net sinds Kinsale Head en Corrib opraken (Kinsale sloot in 2020;
Corrib dekte 22% van de Ierse vraag in 2023/24); via Moffat kwam in gasjaar 2023/24 60.177 GWh binnen (≈ 5,4 bcm/j, zie §7: inclusief Noord-Ierland en Man) [1][2].

## 1 · Ketenkaart
```
Britse NTS bij Beattock/Moffat (fase A: 36-inch landleiding Beattock → Brighouse Bay, NIET getekend: OSM-kartering onvolledig [1])
   ──► Brighouse Bay compressor `gas-brighousebay-compressor` ──(b1 leiding · IC2 · 193,1 km, OSM 5 ways)──►
Gormanston AGI `gas-gormanston-agi` — stoppunt, invoeding Ierse transmissienet (en South-North-pijpleiding)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | `gas-brighousebay-compressor` → `gas-gormanston-agi` | UK-Ireland Interconnector 2 (IC2, 30 inch, Gas Networks Ireland, in dienst 2002/2003); IC1 (24 inch, 162 km [1]) loopt parallel en wordt niet getekend | 192 [1] → gemeten OSM 193,1 (+0,6%) | OSM-ways 440429967 + 440424760 + 902882373 + 902882374 + 174267017 (man_made=pipeline, name=UK-Ireland Interconnector 2 (IC2), substance=gas, diameter=600), vooraf gestikt | nee |

Way-lengtes: 440429967 1,2 km · 440424760 107,6 · 902882373 53,1 · 902882374 30,3 · 174267017 0,9 = 193,1 km; vier naden 0,000 km (de ways delen eindnodes).
OSM-richting is Gormanston → Brighouse Bay; het geojson wordt omgedraaid tot Brighouse Bay → Gormanston. Land alleen bij de twee aanlandingen (ways 440429967 en 174267017, `location=underground`).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-brighousebay-compressor` | compressorstation (kop) | Brighouse Bay compressorstation (Gas Networks Ireland UK), Dumfries and Galloway | 54.7890, -4.1096 | [1][3][4] | bron-gelegd (z15 gezien: klein geplaveid industrieterrein met compressorgebouwen en leidingwerk midden in weiland aan een toegangsweg, 1 km van de kust; OSM kent er 6 schoorsteenknopen; OSM-leidingbegin 54.78900, -4.10958 ligt op het anker) |
| `gas-gormanston-agi` | AGI / aanlanding (staart, stoppunt) | Gormanston AGI (Gas Networks Ireland), County Meath | 53.6386, -6.2227 | [1][2][3][4] | bron-gelegd (z15 gezien: omheind klein terrein tussen akkers ten westen van de spoorlijn en de kust, ~50 m NO van het kruis; OSM-leidingeinde 53.63856, -6.22275 ligt op het anker; hek met motor_vehicle=private) |

Hergebruik: geen: noch Ierland noch Schotland staat in `gas-sitelaag.json` of in eerdere brieven. De Brits-Ierse aanvoer (Beattock) is geen eigen anker (niet gevonden, zie §7).

## 4 · Via-punten
Niet van toepassing: één leidingbeen uit aaneengestikte OSM-ways (geen corridorkeuze zoals bij weg/spoor).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Brighouse Bay compressorstation | Gas Networks Ireland (UK) | Brits NTS-gas (85 bar uit Beattock) → 140 bar in IC1/IC2 | niet gevonden per station | [1] |
| Moffat Entry Point (Beattock, NTS-aftakking) | National Gas / Gas Networks Ireland | NTS → Beattock-compressoren → Brighouse Bay | technische capaciteit 386,9 GWh/d (≈ 35 mscm/d [5]); piekdag 2023/24 Moffat 303,5 GWh/d | [2][5] |
| Gormanston AGI | Gas Networks Ireland | IC1+IC2-gas → Ierse transmissienet; South-North-pijpleiding (156 km) naar Noord-Ierland begint hier | niet gevonden | [1][2] |

## 6 · Stoppunt
De brief stopt bij Gormanston: dit is het gevraagde Ierse invoedingspunt en het enige AGI waar de twee interconnectors aanlanden; daarna is het gas anoniem Iers netgas
(Dublin, Cork, Corrib-gas, SNP). Fase A (Britse aanvoer Beattock → Brighouse Bay) vervalt: niet volledig in OSM gekarteerd en de lijn eindigt waar het bewijs eindigt.

## 7 · Open punten
- **Volume**: geen jaartotaal voor IC2 alleen gevonden. Moffat 2023/24 = 60.177 GWh [2, tabel A1-5], ≈ 5,4 bcm/j (eigen omrekening via GNI's 386,9 GWh/d = 35 mscm/d [5];
  ~11,05 kWh/m³). Dit is **inclusief Noord-Ierland (SNIP, via Twynholm) en Man**, dus een bovengrens voor Gormanston. Peiljaar gasjaar 2023/24 (okt-sep).
  Aandeel: Moffat leverde 78% van de Ierse (ROI) vraag in 2023/24, 77,6% in kalenderjaar 2023 [2].
- **IC1 en IC2 delen dezelfde corridor en dezelfde aanlanding**: de lijn tekent IC2 (OSM-ways, 30 inch); het volume is dat van beide samen. IC1 niet in OSM-vorm getrokken.
- **Brits aanvoerstuk Beattock → Brighouse Bay** (36 inch, twee overlandleidingen, 2 compressorstations) niet getekend; OSM-kartering niet volledig gecontroleerd. De ketenkop is het compressorstation, niet de NTS-aftakking.
- **Brighouse Bay-coördinaat** is de OSM-leidinguiteinde + z15-blik (aannemelijk-plus: geen operator-document met coördinaat); de bron-brief gaf 54.7890, -4.1096, bevestigd.
- **Geen verwerking voorbij Gormanston** (geen fabriek of afnemer met één bron; de vraag is verspreid over het Ierse net).
- **Sitelaag mist Moffat, Brighouse Bay en Gormanston**: centrale aanvulling nodig voor de gloed.
- **Kinsale-veld sloot in 2020** [1]: de keten is dus nu de hoofdaanvoer, niet een reserve.

## 8 · Bronnen
[1] Wikipedia (EN), "United Kingdom–Ireland natural gas interconnectors": IC1 1991/93 (24 inch, 162 km), IC2 2003 (30 inch, 120 mile = 192 km), Beattock/Brighouse Bay/Gormanston, SNP 156 km, Kinsale 1978–2020.
    https://en.wikipedia.org/wiki/United_Kingdom%E2%80%93Ireland_natural_gas_interconnectors
[2] Gas Networks Ireland, "Network Development Plan 2024" (gasjaar 2023/24): Moffat 60.177 GWh (tabel A1-5, incl. NI en Man), ROI-aandeel 78%, 77,6% in 2023, piekdag 303,5 GWh/d, capaciteit 386,9 GWh/d, Corrib 22%.
    https://www.gasnetworks.ie/sites/default/files/2025-10/Network-Development-Plan-2024.pdf
[3] OpenStreetMap-bijdragers (ODbL), OSM-API 0.6, 2026-10-31: ways 174267017, 902882374, 902882373, 440424760, 440429967 (man_made=pipeline, IC2, operator Gas Networks Ireland, diameter 600, substance gas); bbox-schoorsteennodes bij Brighouse Bay.
    https://www.openstreetmap.org/way/440424760
[4] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-gas-brighousebay-gormanston-brighouse.png`, `sat-gas-brighousebay-gormanston-gormanston.png` (z15, 2,8 m/px).
[5] Gas Networks Ireland, "Winter Outlook 2024": Moffat Entry Point technische capaciteit 35 mscm/d (uit zoekresultaat-uittreksel, document niet zelf geopend).
    https://www.gasnetworks.ie/winter-outlook-2024.pdf
[6] Gas Networks Ireland, bedrijfssite (bronstartpunt van de ontwerpketen): https://www.gasnetworks.ie

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)
`bash v2/tools/bak_stromen.sh gas-brighousebay-gormanston` → `v2/data/stroomroute-gas-brighousebay-gormanston.json` (2,0 KB, contract versie 2, lonlat).

| # | modaliteit | been | km gemeten | km brief | stippel |
|---|---|---|---|---|---|
| 1 | leiding | UK-Ireland Interconnector 2 (IC2, 30 inch) Brighouse Bay naar Gormanston (OSM ways, ~192 km; IC1 parallel niet getekend) | 193,1 (65 punten) | 192 (Wikipedia) | nee |

Totaal 193,1 km, naad geen (één been), 2 markers (`gas-brighousebay-compressor`, `gas-gormanston-agi`), beide op 0,0 km van de lijn. Afwijking +0,6% tegen de gepubliceerde 192 km.
**Recept:** `bak_gas_brighousebay_gormanston()` in `bak_stromen.sh`: één `--been-geojson "leiding|…"` op het vooraf gestikte `gas-brighousebay-gormanston-leiding-ic2.geojson` (FeatureCollection, gemaakt door `maak_leidingbeen_gas_brighousebay_gormanston.py --schrijf` uit de 5 OSM-ways, omgedraaid tot Brighouse Bay naar Gormanston).
**Leiding:** doorgetrokken, geen stippel: OSM kent de hele IC2 inclusief het offshore-deel als man_made=pipeline, dus geen gat. Geen weg-, zee-, spoor- of luchtbeen, geen haven-aanloop, geen via-punten, geen gedeeld been, geen extract, geen profiel in `maak_stroombeen_weg.py`.
**Toets:** `toets_knikken.py` 0 knikken en 0 omkeringen; json.load ok (versie 2, lonlat, modaliteit leiding, 65 punten).
**Lessen:** (1) een leiding met volledige OSM-dekking is één regel; vooraf stikken en als FeatureCollection aanleveren. (2) IC1 en IC2 delen corridor en aanlanding: het volume (Moffat 60.177 GWh incl. Noord-Ierland en Man) is van beide samen en een bovengrens voor Gormanston. (3) De sitelaag mist Moffat, Brighouse Bay en Gormanston (centraal aan te vullen). (4) Tijdens het bakken meldde bash eenmalig `line 15418: s: command not found`: het gedeelde `bak_stromen.sh` werd door een andere agent tegelijk bewerkt; `bash -n` is daarna schoon en de bake is geslaagd.
