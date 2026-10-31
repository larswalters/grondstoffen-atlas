# Zilver · Zhezkazgan-smelter → Balkhash-PMP (Kazachstan)

**stroom-id:** `zilver-zhezkazgan-balkhash` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) ·
**status:** gebakken (2026-10-31)
**Keten in één zin:** koperelektrolyse-slijk (zilver- en goudhoudend) van de Zhezkazgan Copper Smelter (Kazakhmys
Smelting, Ulytau-regio) per **weg** naar het slijkterrein van de Precious Metals Plant (PMP) van de Balkhash-smelter
(Balkhashtsvetmet, regio Karaganda), waar zilver in baren en korrels en goud in baren wordt gemaakt; stoppunt bij de PMP.
**Welke as van het verhaal:** Kazachstan, binnenlands edelmetaalcircuit van Kazakhmys: het slijk van de ene
koper-smelter gaat naar de edelmetaalfabriek van de andere. Volume: Balkhash-PMP 670 t Ag/j capaciteit (bron [1], geen
peiljaar); Kazachstan als geheel 697,5 t Ag/j geraffineerd in 2024 [2]; slijk Zhezkazgan 850 t slijk/j capaciteit [1];
het zilveraandeel van dat slijk is niet gepubliceerd (indicatie of onbekend, zie §7).

## 1 · Ketenkaart
```
Zhezkazgan-smelter, slijkopslag `ag-zhezkazgan-smelter`
  ──(b1 truck · weg Zhezkazgan–Karaganda-corridor, dan Shet–Balkhash · hemelsbreed 555 km, geen wegkm)──►
Balkhash-smelter, PMP-slijkterrein `ag-balkhash-pmp` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | Zhezkazgan-smelter → Balkhash-PMP-slijkterrein | weg Zhezkazgan – Zhana-Arka – Shet – Balkhash (KAZ14, KAZ22, KAZ01; OSM-meting, geen bronnoemer) (aannemelijk: één bron) | hemelsbreed 555 km, geen wegkm; OSM-meting haalbaarheidstoets 695,5 km | maak_stroombeen_weg (extract kazachstan, nieuw profiel) | nee |

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-zhezkazgan-smelter` | smelter / slijkopslag (kop) | Zhezkazgan Copper Smelter (Kazakhmys Smelting) | 47.7769, 67.7211 | [1][7] (OSM-smelter 47.7739, 67.7173 + sat) | bron-gelegd (z14 gezien: donkere smelterhallen in een groot industrieterrein ZO van de stad, rookpluimen naar ZW, slakken- en residuveld oostelijk; punt ligt op de hallen) |
| `ag-balkhash-pmp` | edelmetaalfabriek / slijkterrein (staart) | Balkhash-smelter (Balkhashtsvetmet), PMP-slijkterrein | 46.8338, 74.9461 | [1][4][7] (OSM Balkhashtsvetmet) | aannemelijk (z14 gezien: smeltercomplex met hallen, spoorbundel en slakkenberg, stad ten O, meer ten Z; punt ligt op het complex, maar het PMP-gebouw zelf is niet aan te wijzen) |

Beelden: `v2/build-cache/satcheck/sat-zilver-zhezkazgan-balkhash-zhezkazgan.png` en `…-balkhash.png`.
Sitelaag (`zilver-sitelaag.json`) heeft geen Zhezkazgan- of Balkhash-site; er is dus niets hergebruikt (melding aan centraal).

## 4 · Via-punten (alleen b1; drie, in reisvolgorde, geen stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Zhana-Arka-district, op de trunk NO van Zhezkazgan | 48.454, 70.095 | pint de noordelijke corridor (de route buigt naar breedte 48,7; met venster 120 km vond OSM geen wegpad); open steppe, Nominatim: Zhana-Arka-district, Ulytau |
| b1 | 2 | Shet-district, op de doorgaande weg ten Z van Karaganda | 48.681, 72.003 | hoogste punt van de boog; de gemeten route loopt hier (niet langs de spoorlijn via Mointy; een zuidelijker wegpad is niet getoetst); open land, geen plaats |
| b1 | 3 | Shet-district, op de weg naar Balkhash | 47.821, 74.154 | pint de afdaling naar Balkhash en dwingt de aansluiting op de KAZ01-trunk af; open land, geen plaats |

Alle drie komen uit de bake van de haalbaarheidstoets (695,5 km via trunk en primary, geen stad); bak-agent: een
via-punt dat > 5 km snapt is fout gelegd.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Zhezkazgan Copper Smelter | Kazakhmys Smelting | koperconcentraat → kathode, zwavelzuur, **elektrolyse-slijk** | slijk 850 t/j | [1] |
| Balkhash PMP | Kazakhmys Smelting (Balkhashtsvetmet) | slijk uit Zhezkazgan (en eigen) → zilver in baren en korrels, goud in baren | Ag 670 t/j, Au 11 t/j; elders op de site Ag "tot 400 t", Au "tot 10 t" | [1][3] |

## 6 · Stoppunt
De brief stopt bij het slijkterrein van de Balkhash-PMP: er is geen gepubliceerde afnemer of exportroute van het
Balkhash-zilver (de LBMA-leverbare 1.000 oz-baren zijn bron [3], maar geen bestemming), dus export wordt niet getekend.

## 7 · Open punten
- **Zilveraandeel van het Zhezkazgan-slijk onbekend**; alleen 850 t slijk/j capaciteit [1]. Volume is indicatie of onbekend.
- **PMP-gebouw niet gelokaliseerd** binnen het Balkhash-complex; anker is het smeltercomplex (aannemelijk).
- **Tegenstrijdige capaciteit:** op dezelfde site 670 t Ag/j en "tot 400 t Ag/j" [1]; Interfax 2010 noemt "400 tonnen ingots per maand" [3], wat niet bij 670 t/j past (waarschijnlijk drukfout of 400 kg). Niets hiervan is als vast cijfer gebruikt.
- **Eén bedrijfsbron voor de modaliteit weg** ("transported by road", [1]); spoor Zhezkazgan–Mointy–Balkhash loopt parallel, geen bron noemt het.
- **Geen gepubliceerde wegkilometer.** Een zoektocht (RU) geeft alleen hemelsbreed ca. 580 km tussen de steden [8]; anker-tot-anker 555 km hemelsbreed; de ±15%-toets is hier indicatie, geen norm. De OSM-wegmeting (695,5 km) is een eigen meting, geen bron.
- **Corridor is uit OSM afgeleid, niet uit een bron**; de via-punten kozen de bocht naar breedte 48,7.
- **Kazachstan 697,5 t Ag/j [2] is nationaal** (inclusief Kazzinc, Ust-Kamenogorsk); het Balkhash-aandeel is niet gepubliceerd.
- Geen last mile: beide ankers liggen op het terrein; de aansluiting op de openbare weg is niet apart gemeten.

## 8 · Bronnen
[1] Kazakhmys Smelting, "Zhezkazgan Copper Smelter" en "Balkhash Copper Smelter / PMP" — slijk per weg naar het PMP-slijkterrein (850 t/j), Ag 670 t/j, Au 11 t/j; elders Ag tot 400 t, Au tot 10 t, geen peiljaar. https://kazakhmys-smelting.kz/en
[2] Astana Times, 2026-01 — Kazachstan 697,5 t geraffineerd zilver in 2024 (−21,2%), jan–nov 2025 567,5 t; noemt Kazzinc/Ust-Kamenogorsk, niet Balkhash. https://astanatimes.com/2026/01/kazakhstans-silver-production-drops-as-prices-hit-record-highs/
[3] Interfax, 2010-07-22 — Kazakhmys lid van de LBMA, 1.000 oz-zilverbaren van het Balkhash-complex, gietlijn sinds zomer 2009. https://interfax.com/newsroom/top-stories/63426/
[4] Wikipedia, "Balkhashtsvetmet" — smeltercomplex van Kazakhmys; Kounrad-mijn 12 km N. https://en.wikipedia.org/wiki/Balkhashtsvetmet
[5] Wikipedia, "Jezkazgan" — smelter/metallurgisch complex ZO van de stad (1973), wegen E018/E123. https://en.wikipedia.org/wiki/Jezkazgan
[6] Wikipedia, "Balkhash (city)" — industriestad aan de N-oever van het Balkhashmeer, koper sinds 1937. https://en.wikipedia.org/wiki/Balkhash_(city)
[7] OpenStreetMap/Nominatim (ODbL) — smelter Zhezkazgan 47.7739, 67.7173; Balkhashtsvetmet 46.8338, 74.9461; via-punten in Zhana-Arka- en Shet-district. https://www.openstreetmap.org
[8] Freedom Travel, route Zhezkazgan–Balkhash (afstand hemelsbreed ca. 580 km, geen autokm) en eigen berekening 555 km tussen de ankers. https://freedom-travel.kz/routes/zhezkazgan-balhash/
[9] Esri World Imagery via `v2/tools/sat_check.py` (z14) — `sat-zilver-zhezkazgan-balkhash-zhezkazgan.png`, `sat-zilver-zhezkazgan-balkhash-balkhash.png`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Bestand:** `v2/data/stroomroute-zilver-zhezkazgan-balkhash.json` (33,6 KB, versie 2, lonlat) · functie `bak_zilver_zhezkazgan_balkhash` in `v2/tools/bak_stromen.sh` · profiel `zilver-zhezkazgan-balkhash-zhezkazgan-balkhash` in `maak_stroombeen_weg.py`.

| # | modaliteit | km | punten | naad | stippel |
|---|---|---|---|---|---|
| b1 | truck, Zhezkazgan-smelter naar Balkhash-PMP (KAZ14, KAZ22, KAZ01; aannemelijk: een bron) | 695,8 | 1.706 | n.v.t. | nee |

Totaal 695,8 km, 2 markers (beide ankers uit §3, 0,0 km van de lijn). Geen zee, geen haven-aanloop, geen lucht, geen leiding, geen kopie.

**Recept:** `python v2/tools/wegscan_puur.py --profiel zilver-zhezkazgan-balkhash-zhezkazgan-balkhash` (extract kazachstan, 46 s scan, venster 230 km, refs KAZ14/KAZ22/KAZ01, geen corridorKlassen) en daarna `bash v2/tools/bak_stromen.sh zilver-zhezkazgan-balkhash` (een `--been-geojson`, twee `--marker`).

**Toets:** de lengtetoets is hier indicatie (geen gepubliceerde wegkm): 695,8 km tegen de OSM-haalbaarheidsmeting 695,5 km en hemelsbreed 555 km (omwegfactor 1,25). Snaps van de vijf via-punten 0,03 tot 0,08 km, geen via-punt bijgeschoven. Segmenten 199,3 / 157,4 / 205,4 / 133,5 km, geen omweg. First mile 0,88 km (service), last mile 4,50 km (kleine klassen binnen de 12 km-eindzone), ankerverbindingen 0,06 en 0,08 km. Twee keerlussen van 0,03 km gesnoeid.

**Bevindingen:** `toets_knikken.py` meldt 25 knikken (60 graden of meer), 0 omkeringen, 0 terugloop; het zijn spikes op wegvertices (12 tot 60 m) en krappe bochten, geen reparatie nodig. `toets_rechte_benen.py` vlagt het been niet. De wegmeting is een eigen OSM-meting, geen bron; de corridor (noordelijke boog via Zhana-Arka en Shet naar breedte 48,7) is uit OSM afgeleid en het spoor parallel is niet gebrond. Sitelaag mist Zhezkazgan en Balkhash (kandidaat-sites voor centraal).

**Lessen:** met venster 120 km vond OSM geen wegpad; 230 km volstaat. De via-punten uit de haalbaarheidstoets snapten allemaal binnen 0,1 km, dus ze liggen op de doorgaande weg.
