# Routebrief (licht) · Nikkel — Taganito (Claver) → Yangtze-monding (China)

**stroom-id:** `nikkel-taganito-yangtze` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** saproliet- en limonieterts van de Taganito-mijn (Nickel Asia/TMC, Claver, Surigao del Norte) gaat als directe ertsexport van de eigen pier per bulkschip over zee (Filipijnenzee, oostelijk om Taiwan, tussen Ishigaki en Miyako de Oost-Chinese Zee in) naar China; Chinese haven en smelter staan in geen bron, dus het eindpunt is het conventie-anker Yangtze-monding (aannemelijk: één bron voor de bestemming).
**Welke as van het verhaal:** *Filipijns erts naar Chinese NPI-smelters* — de grootste Filipijnse ertsstroom naar China en de andere helft van Taganito: waar `nikkel-taganito-niihama` de HPAL-route (mixed sulfide naar Japan) toont, laat deze lijn het ruwe erts zien dat Indonesië sinds de exportban niet meer mag leveren. Volume 2014: 1.610 kt WMT saproliet (1,54 % Ni) + 798 kt WMT limoniet (0,98 % Ni) naar Chinese klanten = **ca. 23 kt Ni/j** (indicatie, aangenomen 30 % vocht; op natte basis ca. 33 kt) [1].

## 1 · Ketenkaart
```
Taganito-mijn `ni-taganito-laad` (marker, 0,46 km van de pier, geen eigen been; ertsstockpile → pier)
   → Taganito/Claver-pier `ni-thpal-pier` ──(b1 zee · haven-aanloop, stippel · 65,9 km, KOPIE)──► MARNET-zeeknoop 8314
   ──(b2 zee · MARNET · ca. 2.660 km)──► MARNET-eindknoop 9654 ──(b3 zee · overgangsstippel · 8,6 km, KOPIE)──►
   Yangtze-monding `ni-yangtze-monding` ⏹ stoppunt (Chinese haven en smelter niet gebronnd)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee (haven-aanloop) | `ni-thpal-pier` → zeeknoop 8314 (9.8356, 125.3465) | Surigao-regio | 65,9 (gemeten over water; hemelsbreed 60,5, pier > 5 km van de knoop) [8] | **letterlijke kopie** van `nikkel-taganito-niihama-aanloop-claver.geojson` (bak_nikkel_taganito_niihama) | ja: MARNET reikt niet tot de kade |
| b2 | B | zee (bulkschip, aannemelijk: één bron voor de bestemming) | zeeknoop 8314 → eindknoop 9654 (31.5100, 121.4187) | Filipijnenzee, oostelijk om Luzon en Taiwan, tussen Ishigaki en Miyako (Ryukyu), Oost-Chinese Zee | **2.659,6** (eigen MARNET-meting 2026-10-31, snaps 0,000; hemelsbreed 2.443,9; geen gepubliceerde lengte) [8] | MARNET (`--been zee`) | nee |
| b3 | B | zee (overgang) | 31.5100, 121.4187 → 31.4512, 121.4769 | MARNET houdt hier op | 8,6 [5] | **letterlijke kopie** van de overgangsstippel in `bak_lithium` / `bak_lithium_uis_yangtze` | ja: MARNET reikt niet |

Geen landbeen: TMC laadt het erts bij de eigen pier (Taganito Special Economic Zone), de ertsstockpile ligt aan de pier [1][2][6]. Het anker `ni-yangtze-monding` ligt 2,7 km voorbij het einde van b3: binnen de naadnorm (5 km), geen eigen been. Totaal ca. 2.734 km (gemeten in proefbake).
Overlap, eerlijk: b1 en b3 zijn kopieën, b2 loopt 84–93 % op de baan van andere lijnen naar de Chinese kust (`lithium-finniss-ningbo`, `nikkel-obi-ningbo`); geen bestaande stroom heeft de combinatie Filipijnen → China.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-taganito-laad` | mijn / laadplek (erts-stockpile) | Taganito Mining Corporation (Nickel Asia), Brgy. Taganito, Claver | 9.5464, 125.8193 | **hergebruik letterlijk** uit `nikkel-taganito-niihama.md` §3 [3] | bron-gelegd (z15 hier zelf opnieuw gezien: ertsstockyard op de landtong direct ten oosten van de pier, mijnterrassen landinwaarts naar het zuiden) |
| `ni-thpal-pier` | overslag land → zee (TMC-pier, gedeeld met THPAL) | Taganito/Claver-pier (TMC/THPAL) | 9.5490, 125.8160 | **hergebruik letterlijk** uit `nikkel-taganito-niihama.md` §3 [3][1] | bron-gelegd (z15 gezien: lange laadsteiger loodrecht op de kust, tweede kadearm ernaast, stockyard aan de wortel) |
| `ni-yangtze-monding` | aanlanding China (stoppunt, conventie-anker) | Yangtze-monding | 31.42704, 121.47618 | **hergebruik letterlijk** uit `lithium-uis-yangtze.md` §3 (`li-yangtze-monding`) [5] | aannemelijk (conventie-anker; geen Chinese haven of afnemer gebrond; MARNET-eindknoop 10,7 km ervandaan) |

Markers voor de bak (tekst van lithium-uis-yangtze letterlijk): `Yangtze-monding — aanlanding China (stoppunt, conventie-anker), aannemelijk|31.42704,121.47618`.

## 4 · Via-punten
Geen: alle benen zijn zee/MARNET of kopieën (zee = router, geen via-punten).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Taganito-mijn (TMC) | Nickel Asia 65 % / PAMCO ca. 33,5 % | dagbouw → saproliet (1,4–1,7 % Ni) + limoniet voor export | 2014 verkocht 7.088 kt WMT erts, waarvan 4.023 kt limoniet naar THPAL en 3.064 kt export (Japan + China); China: 1.610 kt saproliet + 798 kt limoniet | [1] |
| Chinese NPI-smelters (niet getekend) | onbekend, niet genoemd | saproliet in elektro-/RKEF-ovens → high-grade NPI (10–12 % Ni); limoniet in hoogovens → medium-/low-grade NPI | n.v.t. | [1] |

## 6 · Stoppunt
De brief stopt aan de Yangtze-monding: AR 2014 noemt alleen "Chinese customers" met vaste tonnages per kwaliteit, geen haven, afnemer of smelter; fase D vervalt (geen bron noemt een fabriek), E vervalt.

## 7 · Open punten
- **Chinese haven en smelter niet gebronnd.** Eindpunt is de conventie (precedent `lithium-uis-yangtze`); de echte bestemmingen (Lianyungang, Fangchenggang en dergelijke) staan in geen bron en worden niet getekend. Dit is het hoofdbezwaar tegen het eerder afgewezen `hinatuan-lianyungang`, hier deels opgelost omdat mijn en pier wel gebronnd zijn.
- **Peiljaar 2014.** Nickel Asia noemt later alleen dat saproliet voor ferronikkel/NPI naar Japan en China gaat; een actueler volume is niet gevonden. De Chinese tonnages zijn ruwe ertstonnages: 23 kt Ni is een indicatie bij aangenomen 30 % vocht.
- **Pier is gedeeld.** TMC-pier dient ook de THPAL-limoniet en de MS-export (`nikkel-taganito-niihama`); of het Chinese erts via dezelfde kade of via de Taganito-ertskade loopt, is niet onderscheiden (AR 2014: "TMC pier facilities").
- **Routekeuze zee onbewezen.** MARNET kiest de Ryukyu-poort (oostelijk van Taiwan); een Taiwanstraat-route is niet getoetst en geen bron noemt de vaarroute.
- **Chinese afnemers in AR 2014 niet naar haven uitgesplitst** ("a number of Chinese customers", Note 31).

## 8 · Bronnen
[1] Nickel Asia Corporation, Annual Report 2014 (p. 4 productmix, p. 16 TMC-verkopen, Note 31 p. 71 pier + Chinese afnemers): 1.610.412 WMT saproliet (1,54 % Ni) en 797.996 WMT limoniet (0,98 % Ni) naar Chinese klanten. https://nickelasia.com/assets/documents/Annual-Report-2014.pdf
[2] Nickel Asia, Taganito Mining Corporation (Claver, Surigao del Norte; export saproliet/limoniet, levert aan THPAL). https://nickelasia.com/subsidiaries/taganito-mining-corporation
[3] `v2/design/routebrieven/nikkel-taganito-niihama.md` §3 en §9 (ankers laadplek/pier, aanloop-claver 65,9 km, zeeknoop 8314) — OSM (ODbL) via Nominatim, landuse "Taganito Mining Corporation".
[4] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-nikkel-taganito-yangtze-pier.png` en `-laad.png` (z15).
[5] `v2/design/routebrieven/lithium-uis-yangtze.md` §2–§3 en functie `bak_lithium_uis_yangtze` in `bak_stromen.sh`: Yangtze-monding 31.42704/121.47618, MARNET-eindknoop 9654, overgangsstippel 8,6 km.
[6] Nickel Asia, 1H 2016 shipments (Taganito: saproliet + limoniet, limoniet naar THPAL). https://nickelasia.com/assets/documents/Nickel_Asia_Reports_8.54_Million_Wet_Metric_Tons_of_Ore_Shipments_In_the_1H_of_2016_-_July_15_2016.pdf
[7] Nickel Asia, Annual Report 2015 (TMC 2015: 2,50 Mt saproliet en 5,24 Mt limoniet, waarvan 4,43 Mt naar THPAL). https://new.nickelasia.com/assets/documents/Annual-Report-2015.pdf
[8] Haalbaarheidstoets nikkel-taganito-yangtze (2026-10-31, orkestrator) + eigen proefbake in de scratchpad (hecht_marnet route: b1 kopie 65,9; MARNET 8314 → 9654 = 2.659,6 km, snaps 0,000; stippel 8,556 km; totaal 2.734,1 km).
[9] Sitelaag `v2/design/nikkel-sitelaag.json` (`w-taganito-thpal`, 9.5407/125.8134, THPAL-plant; bron-gelegd) (coord_bron: EMB Caraga THPAL-document).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Recept:** `bash v2/tools/bak_stromen.sh nikkel-taganito-yangtze` (functie `bak_nikkel_taganito_yangtze`) → `v2/data/stroomroute-nikkel-taganito-yangtze.json` (7,2 KB, versie 2, punt_formaat lonlat). Geen wegprofiel, geen extract, geen via-punten: alleen zee.

| # | modaliteit | been | km | punten | lijnstijl |
|---|---|---|---|---|---|
| b1 | zee | haven-aanloop Claver/Taganito-pier → zeeknoop 8314, letterlijke kopie `nikkel-taganito-niihama-aanloop-claver.geojson` | 65,9 | 52 | stippel (MARNET reikt niet tot de kade) |
| b2 | zee | zeeknoop 8314 → MARNET-eindknoop 9654 (Filipijnenzee, oostelijk om Taiwan, Ryukyu-poort), snaps 0,000 | 2.659,6 | 276 | doorgetrokken |
| b3 | zee | overgang zeenet → Yangtze-bulklaag, letterlijke kopie uit `bak_lithium_uis_yangtze` | 8,6 | 2 | stippel (MARNET reikt niet) |
| | | **totaal** | **2.734,1** | 330 | |

**Markers (3):** `ni-taganito-laad` (9.5464, 125.8193; 0,46 km van de lijn), `ni-thpal-pier` (9.5490, 125.8160; op de lijn), `ni-yangtze-monding` (31.42704, 121.47618; 2,69 km voorbij het einde van b3, binnen de naadnorm 5 km).

**Toets:** km per been gelijk aan de proefbake in de brief (65,9 / 2.659,6 / 8,6 / totaal 2.734,1); naden b1-b2 en b2-b3 0,000 km; geen landbeen dus geen ±15%-toets op wegkm (de zee-km zijn eigen meting, geen publicatie). `toets_knikken.py`: 3 knikken >= 60 gr (109 gr bij 10.50,126.40 R 5,6 km; 82 gr bij 30.90,122.89; 80 gr bij 10.59,125.56), 0 omkeringen, 0 terugloop. `toets_rechte_benen.py --min-km 5`: alleen de overgangsstippel b3 (8,6 km, bedoeld rechte stippel).

**Toelichting stippel/aanloop:** b1 is een haven-aanloop omdat de pier 65,9 km (over water) van zeeknoop 8314 ligt (> 5 km, LAR-586); letterlijke kopie, geen tweede versie. b3 is de bestaande overgangsstippel naar de Yangtze-bulklaag (precedent `lithium-uis-yangtze`). "Aannemelijk: één bron" voor de bestemming staat in de beennaam van b2, niet in de lijnstijl: b2 is gemeten en doorgetrokken. Geen vlucht, leiding, truck of spoor.

**Lessen:** (1) Een volledig zeeketen met twee letterlijke kopieën bakt in één run (~1 min, geen slot-druk); kopieën hergebruiken de bestaande geojson via `$BEEN`. (2) `bak_stromen.sh` is een gedeeld bestand: een gelijktijdige edit van een andere agent tijdens de run gaf een melding "syntax error near unexpected token exit" aan het einde van de run (bash leest het script incrementeel); de bake zelf was klaar en het bestand is daarna syntactisch in orde (`bash -n`). (3) Het 109-graden-knikpunt bij 10.50,126.40 is een router-bocht op het MARNET-net direct na de aanloop, geen terugloop.

**Registerregel (centraal):** `{ "sleutel": "ni-ty", "bestand": "stroomroute-nikkel-taganito-yangtze.json", "grondstof": "nikkel", "label": "Taganito → Yangtze-monding", "aan": true, "noot": "M31 · golf 19 (2026-10-31): Filipijns erts van Taganito per bulkschip oostelijk om Taiwan naar China, eindpunt Yangtze-monding" }`
