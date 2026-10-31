# Routebrief (licht) · zilver — Oyu Tolgoi → Ganqimaodu → Feishang (Mongolië → Binnen-Mongolië)

**stroom-id:** `zilver-oyutolgoi-feishang` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** zilver als bijproduct in het koper-goud-zilverconcentraat van Oyu Tolgoi (Rio Tinto 66% / Erdenes) gaat per **truck** (2 t-zakken) over de eigen betonweg ~105 km naar de grens Gashuun Sukhait, door de Chinese poort Ganqimaodu naar de bonded warehouse ~7 km verder, en vandaar per Chinese truck ~198 km over G242/G335 naar de smelter van Bayannur Feishang Copper (Qingshan, Urad Achterbanner) — **geen zee**, stoppunt = smelter (anode; zilver wordt daarna teruggewonnen).
**Welke as van het verhaal:** *Mongools zilver over land naar China.* OT: **2.180 koz Ag in concentraat in 2025 = 67,8 t Ag/j** (100%-basis; Rio-aandeel 66% = 1.439 koz = 44,8 t) tegen 1.424 koz (44,3 t) in 2024 en 1.086 koz in 2023 [1]. Resource ~1.900 t Ag (geen jaarproductie) [2]. Feishang kocht in 2022 158,2 kt OT-concentraat [5] — zilvergehalte per leverancier niet gepubliceerd.

## 1 · Ketenkaart
```
OT-concentrator/zakkenplant `ag-ot-laad` ──(b1 truck · OT-betonweg + poort Ganqimaodu · 107,9 km gemeten, 105 + ~7 gepubliceerd)──► bonded warehouse `ag-ot-bonded`
  ──(b2 truck · G242 → G335 via Bayan Baolige · 191,7 km gemeten, ~198 OSRM)──► Feishang-smelter `ag-ot-smelter` ── stoppunt
```
Grens Gashuun Sukhait/Ganqimaodu `ag-ot-grens` ligt op b1 (marker, geen overslag: dezelfde trucks rijden door [3][4]).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ag-ot-laad` → `ag-ot-bonded` | OT-betonweg → Gashuun Sukhait → poort Ganqimaodu → G242 zuid | gemeten 107,9; gepubliceerd 105 (OT LLC [6]) + ~7 (NI 43-101 [3]) = ~112 → −3,7% | LETTERLIJKE KOPIE `stroombeen-ot-bonded.geojson` (koper-oyutolgoi-feishang b1) | nee |
| b2 | C | truck (aannemelijk: één bron voor de afnemer) | `ag-ot-bonded` → `ag-ot-smelter` | G242 (甘临一级公路) → afrit → G335 via Bayan Baolige | gemeten 191,7; ~198 uit OSRM — **geen onafhankelijke publicatie** (G242 Ganqimaodu–Linhe 183 km [7]) | LETTERLIJKE KOPIE `stroombeen-bonded-feishang.geojson` (koper-oyutolgoi-feishang b2) | nee |

Geen nieuw wegprofiel, geen wegscan: beide benen bestaan al als geojson in `v2/build-cache/ais/graaf/` (korte uitleg in §9 van de koperbrief). Spoor ontbreekt bewust: de grensspoorlink Gashuun Sukhait–Ganqimaodu (32,6 km) is in aanbouw (spoorleggen sinds 2026-09, gepland 2027 [8]); nu truck.

## 3 · Ankers (één per site en per overslag — alle vier HERGEBRUIKT letterlijk uit `koper-oyutolgoi-china.md` §3)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-ot-laad` | laadplek (concentrator + zakkenplant) | Oyu Tolgoi | 43.0480, 106.8360 | brief koper [4][9] | bron-gelegd (z15 hier opnieuw gezien: groot molengebouw met koepelvormige opslaghal, indikkers en bassins; open putten ~1,5 km oostelijk; kruis aan de rand van de plant) |
| `ag-ot-grens` | grensovergang (marker) | Gashuun Sukhait (MN) / Ganqimaodu (CN) | 42.4146, 107.5692 | OSM `border_control` via koperbrief | bron-gelegd (z15 gezien: Mongoolse grenspostcomplex met vrachtwagenopstel noordelijk, Chinese poort + spoorterrein en vrachtwagenparkeerplaatsen zuidoost) |
| `ag-ot-bonded` | overslag (bonded warehouse "Huafang") | logistiekzone Ganqimaodu | 42.3740, 107.5990 | [3] (~7 km van grens), koperbrief | aannemelijk (z15 gezien: loodsencomplex met blauwe daken naast het spooremplacement; welke loods Huafang is, is niet gebleken) |
| `ag-ot-smelter` | smelter (stoppunt) | Bayannur Feishang Copper (巴彦淖尔市飞尚铜业), Qingshan-industriepark | 40.9694, 106.8530 | MEE-register [10] | bron-gelegd (z15 gezien: dicht bebouwd industriepark op een wegenraster, kruis op een fabriekscluster met hallen; registerpunt CGCS2000 = WGS-84) |
Satellietbeelden: `v2/build-cache/satcheck/sat-zilver-oyutolgoi-feishang-{laad,grens,bonded,smelter}.png` (Esri z15, 2026-10-31).

## 4 · Via-punten (hergebruik koperbrief §4; alleen waar een corridorkeuze bestaat)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | OT-weg ZO van de mijn | 42.9945, 106.9657 | pint de OT-betonweg i.p.v. de Tavan Tolgoi-kolenweg |
| b1 | 2 | middenstuk OT-weg | 42.7729, 107.3890 | zelfde keuze |
| b1 | 3 | Tsagaan Khad | 42.5785, 107.5437 | begin laatste wegvak (18,6 km) [6] |
| b1 | 4 | Chinese poort Ganqimaodu | 42.4089, 107.5743 | "door de poort" i.p.v. langs S212 |
| b2 | 1 | start G242 ten zuiden van de poortzone | 42.3887, 107.5711 | G242 zuid i.p.v. S212 oost |
| b2 | 2 | afrit G242 → G335 | 41.2704, 107.3697 | westelijk af naar G335 i.p.v. door naar Linhe (+~40 km) |
| b2 | 3 | Bayan Baolige op G335 | 41.0790, 107.0729 | G335-corridor door de rayonhoofdplaats (op de doorgaande vertex, niet het centrum) |
Geen nieuwe via-punten nodig: de geometrie wordt gekopieerd, niet opnieuw gescand.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Oyu Tolgoi-concentrator | Oyu Tolgoi LLC (Rio Tinto 66%, Erdenes 34%) | erts → Cu-Au-Ag-concentraat | 2.180 koz Ag in concentraat (2025) = 67,8 t | [1] |
| Feishang Copper, Qingshan | Feishang Group (飞尚集团) | concentraat (2022: 451 kt, waarvan 158 kt OT) → anodeplaat (ruwkoper) + zwavelzuur; goud/zilver als bijproduct | 100 kt/j ruwkoper | [5][11] |

## 6 · Stoppunt
Stop bij de smelter Feishang: die levert anode, en geen bron noemt de raffinaderij waar anodes en edelmetaal heen gaan; fase D is niet in één zin gegeven en wordt niet getekend (zelfde stoppunt als koper-oyutolgoi-feishang).

## 7 · Open punten
- **Zilver per leverancier:** het cijfer 2.180 koz is de totale OT-productie in concentraat; welk deel in de 158,2 kt (2022) naar Feishang ging en of Feishang het zilver betaalt/terugwint is niet gepubliceerd. De keten is as-niveau; afnemer Feishang = aannemelijk (één bron, 2022) — in de beennaam van b2.
- **Dubbeling:** geometrie identiek aan `koper-oyutolgoi-feishang` b1/b2 (twee stromen over dezelfde lijn); gewenst, want het zilver reist mee in hetzelfde concentraat.
- **Bonded-loods:** Huafang niet aan een gebouw gekoppeld; anker `ag-ot-bonded` ligt 2,07 km hemelsbreed oostelijk van het wegeind van b1/b2 (107.5740, 42.3764, op G242); naad tussen b1 en b2 is 0 km. Marker blijft op het loodsencomplex staan zoals in de koperstroom.
- **Wegkm b2:** 191,7 gemeten tegen ~198 (OSRM): geen onafhankelijke publicatie, ±15%-toets alleen indicatie.
- **Blokkade:** juni 2026 blokkeerden demonstranten de koperexport van OT naar China [12][2]; de duur en het effect op de zilverstroom zijn niet bevestigd. Truck blijft de gebakken modaliteit.
- **Sitelaag:** `zilver-sitelaag.json` heeft geen Oyu Tolgoi-site; centraal toevoegen met `ag-ot-laad` en 67,8 t Ag/j.

## 8 · Bronnen
[1] Rio Tinto, Form 20-F FY2025 (2026-02-19), productietabel zilver in concentraat: Oyu Tolgoi 66,0% — 2.180 / 1.424 / 1.086 koz (2025/2024/2023), Rio-aandeel 1.439 koz — https://www.sec.gov/Archives/edgar/data/863064/000162828026009531/rio-20251231.htm
[2] Wikipedia, Oyu Tolgoi mine — afzetting "1,900 tonnes of silver"; juni 2026 export-blokkade — https://en.wikipedia.org/wiki/Oyu_Tolgoi_mine
[3] Oyu Tolgoi NI 43-101 Technical Report (Entrée Resources, okt. 2021, §23-4): verkoop bij de Huafang bonded warehouse ~7 km van de grens, afhaal per truck of trein — https://www.sec.gov/Archives/edgar/data/1271554/000127956921001447/ex991.htm
[4] E&MJ, "Oyu Tolgoi: A Nation Changer" (2013): Mongoolse trucks vanaf de bagging plant, 2 t-zakken, 16 per truck — https://www.e-mj.com/features/oyu-tolgoi-a-nation-changer/
[5] 腾讯新闻/巴彦淖尔 (2023-12-28): Feishang 2022 — 158,2 kt OT-concentraat via Ganqimaodu — https://news.qq.com/rain/a/20231228A00J8W00
[6] Oyu Tolgoi LLC, weg Tsagaan Khad–Gashuun Sukhait (105 km gepland, laatste 18,6 km) — https://www.ot.mn/ws2272197365-en/
[7] 中国建筑 (2019-03): G242 Ganqimaodu–Linhe 183 km — https://www.cscec.com/xwzx_new/gsyw_new/201903/2916864.html
[8] 腾讯新闻 (2026-09-03): grensspoorlink Ganqimaodu–Gashuun Sukhait, spoorleggen, 2027 in bedrijf — https://news.qq.com/rain/a/20260903A036W300
[9] Brief `koper-oyutolgoi-china.md` — ankers, via-punten, bronnen [1]–[19] aldaar (o.a. Rio Q4 2025 6-K: 345 kt Cu in concentraat 2025).
[10] MEE-emissievergunningregister 91150800772247433C001P (Feishang, 106.85298 / 40.96935) — https://permit.mee.gov.cn/perxxgkinfo/syssb/xkgg/xkgg!licenseInformation.action
[11] 百度百科, 巴彦淖尔市飞尚铜业有限公司 (阳极板 10万吨/j) — https://baike.baidu.com/item/巴彦淖尔市飞尚铜业有限公司/9252504
[12] AP News, "Protesters block copper exports to China from Rio Tinto mine in Mongolia" (juni 2026) — https://apnews.com/article/mongolia-china-tinto-copper-mine-protest-tolgoi-f7c438c2666d8c52a0015533630302ad
[13] Esri World Imagery via `sat_check.py`, `v2/build-cache/satcheck/sat-zilver-oyutolgoi-feishang-*.png` (z15) en geometrie in `v2/build-cache/ais/graaf/stroombeen-ot-bonded.geojson` (377 pt) / `stroombeen-bonded-feishang.geojson` (858 pt).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Bestand:** `v2/data/stroomroute-zilver-oyutolgoi-feishang.json` (26,1 KB, versie 2, lonlat) · **totaal 299,6 km · 1.235 punten · 4 markers** · functie `bak_zilver_oyutolgoi_feishang` in `v2/tools/bak_stromen.sh` (LF, `bash -n` schoon).
**Recept:** `bash v2/tools/bak_stromen.sh zilver-oyutolgoi-feishang` — twee `--been-geojson truck`, geen wegscan, geen profiel, geen extract.

| # | modaliteit | km gemeten | km brief | afwijking | naad naar vorig | stippel |
|---|---|---|---|---|---|---|
| b1 | truck | 107,9 (377 pt) | ~112 (105 + ~7) | -3,7% | - | nee |
| b2 | truck | 191,7 (858 pt) | ~198 (OSRM, geen publicatie) | -3,2% | 0,00 km | nee |

- **Markers:** laad 0,0 km, grens 0,02 km, smelter 0,0 km van de lijn; **bonded 2,07 km** (aannemelijk: loods Huafang niet identificeerbaar, anker op het loodsencomplex, lijn eindigt op de weg; identiek aan de koperstroom).
- **Kopie:** b1 en b2 zijn letterlijke kopieen van `stroombeen-ot-bonded.geojson` en `stroombeen-bonded-feishang.geojson` (koper-oyutolgoi-feishang); de beennamen noemen KOPIE. b2 draagt (aannemelijk: een bron voor de afnemer) in de naam.
- **Toetsen:** `toets_knikken` 5 knikken op b2 (spikes tot 104 gr, op de G335 bij 41.06,107.07), 0 omkeringen, 0 terugloop (zelfde als de koperstroom); `toets_rechte_benen` geen treffer; geen stippel, geen aanloop, geen vlucht, geen zee.
- **Les:** een stroom die hetzelfde concentraat meedraagt als een bestaande stroom bakt in een minuut zonder wegscan; de hemelsbreed-noot geldt niet: b2 heeft geen onafhankelijke wegkm, de -3,2% is een indicatie.
- **Open (centraal):** sitelaag zilver mist Oyu Tolgoi (`ag-ot-laad`, 67,8 t Ag/j); geometrie dubbel met koper-oyutolgoi-feishang is bewust; zilvergehalte per leverancier en juni-2026-blokkade onbevestigd (zie §7).
