# Routebrief (licht) · Zilver · Dexing-koperconcentraat → Guixi-smelter (China)

**stroom-id:** `zilver-dexing-guixi` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 12) · **status:** gebakken
**Keten in één zin:** zilver in het koperconcentraat van de Dexing-kopermijn (Jiangxi Copper, Jiangxi) gaat per **spoor** over de lokale 乐德铁路 (Leping-Dexing, 64 km) en de 皖赣铁路 (Leping-Guixi, 89,2 km) naar de Jiangxi Copper-smelter in Guixi; de keten stopt daar (**aannemelijk: één bron** voor modaliteit en bestemming, zie §7).
**Welke as van het verhaal:** *Chinees binnenlands koperzilver: de mijn die Guixi voedt.* Volume: Dexing **4.508 koz Ag in 2021 = ca. 140 t Ag/j** (GlobalData-snippet, 11,88 Mt erts/j) [5]; Jiangxi Copper groep 1.383 t Ag in 2025 [7]. Het mijnaandeel dat per spoor Guixi bereikt is niet gepubliceerd.

## 1 · Ketenkaart
```
Dexing-mijn/concentrator, Tongkuang (registerpunt) `ag-dexing-mijn`
  ──(b1 last mile 0,6 km stippel, geen net op deze korrel)──► railhead (rails eindigen hier)
  ──(b2 spoor · 乐德铁路 Dexing-Leping 64 + 皖赣铁路 Leping-Guixi 89,2 = 153,2 gepubliceerd · 152,7 gemeten · aannemelijk: één bron)──►
Jiangxi Copper, Guixi-smelter `ag-guixi-smelter`  ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | mijnanker → railhead | eigen terrein/stad Tongkuang | 0,6 hemelsbreed | `--stippel` | ja: last mile (geen net op deze korrel) |
| b2 | A | spoor | railhead 29.0485,117.7098 → Guixi-smelter | Dexing - Leping - Guixi (aannemelijk: één bron) | **153,2 gepubliceerd** (64 [1] + 89,2 [2]) · gemeten 152,7 (-0,3%) | `maak_spoorbeen_raw.py --extract china`, één run zonder via | nee |
Totaal ca. 153,3 km, 2 benen. Geen fase B-E: geen zee, geen weg, geen leiding.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-dexing-mijn` | mijn/concentrator (kop b1) | Dexing-kopermijn, mijnstad Tongkuang (铜矿街道) | 29.0432, 117.7074 | [3][8][sat] | **onzeker** (z14/z15 gezien: mijnstad met woonblokken en spoorbundel; de put ligt ca. 2-3 km ZO (grote terrasput rechtsonder op z14); het punt is het registerpunt van het mijnkantoor, niet de put en niet de concentrator) |
| `ag-guixi-smelter` | afnemer/losplek (staart b2) | Jiangxi Copper, Guixi-smelter (贵溪冶炼厂) | 28.3271, 117.2260 | [7][sat] | aannemelijk: één bron (z15 gezien: groot smeltercomplex met uitgebreide spoorbundel; hergebruik letterlijk uit `zilver-escondida-guixi` `ag-guixi-smelter`) |

Railhead (routeerpunt, geen marker): 29.0485, 117.7098, 0,63 km van het mijnanker; de ruwe OSM-rails eindigen daar (snap 3 m). z15 gezien: spoorbundel door de oostrand van de stad, aan de oostkant een groot gebied met parallelle sporen (rangeer-/stapelterrein of residu).

## 4 · Via-punten
Geen. Eén Dijkstra-run over de ruwe OSM-ways (`landnet-raw.bin` mist de Ledexian-lijn): 894 punten, 0 omkeringen. Een via bij Leping geeft nep-omkeringen. Geen wegbeen, geen profiel in `maak_stroombeen_weg.py`.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Dexing-mijn + concentrator | Jiangxi Copper | erts → koperconcentraat met Ag | 11,88 Mt erts/j; Ag 4.508 koz (2021) | [5] |
| Guixi-smelter | Jiangxi Copper | concentraat → kathode + anodeslijk (goud/zilver) | >1 Mt Cu/j; groep 1.383 t Ag in 2025 | [4][7] |

## 6 · Stoppunt
Stopt bij de Guixi-smelter, net als `zilver-escondida-guixi`: zilver verlaat Guixi als edelmetaalproduct (geen gedocumenteerde volgende locatie), dus fase D/E vervallen. Een regel in de beennaam, niet de lijnstijl, draagt "aannemelijk: één bron".

## 7 · Open punten
- **Eén bron voor modaliteit en bestemming:** alleen zh.wikipedia 乐德铁路 zegt dat de lijn Dexing-koper via Leping en de 皖赣铁路 naar de Guixi-smelter brengt [1]. De lijn eindigt volgens [1] bij het 泗洲铜矿 (Sizhou) en niet noodzakelijk bij de put of concentrator; of de OSM-railhead (29.0485,117.7098) die plek is, is niet bevestigd.
- **Heden onbevestigd:** geen Jiangxi Copper-document gevonden dat de concentraatstroom per spoor beschrijft; of de lijn nu nog wordt bereden is niet getoetst (OSM heeft de rails).
- **Zilveraandeel:** 140 t Ag/j (2021) komt uit één GlobalData-snippet [5]; het aandeel dat via Guixi loopt en het aandeel in concentraat staan nergens. Een oudere bron noemt 51.400 kg Ag in zelfgemijnd concentraat in 2005 (zoekfragment van een HKEX-jaarverslag 2006, PDF niet leesbaar, niet gebruikt).
- **Mijnanker onzeker:** put 2-3 km ZO, concentrator niet gevonden; het punt blijft een registerpunt.
- **Staart:** de laatste ca. 5 km naar de smelter lopen samen met b10 van `zilver-escondida-guixi`/`koper-escondida-guixi` (via 28.3429,117.1975); geen letterlijke kopie nodig, wel dezelfde bocht.
- **Sitelaag:** `zilver-sitelaag.json` heeft geen Dexing-site; `koper-sitelaag.json` evenmin gevonden (site-26 volgens de toets). Centraal gelijktrekken.

## 8 · Bronnen
[1] zh.wikipedia, 乐德铁路 (64 km, 1986 geopend, Leping-Dexing, vervoert Dexing-koper naar de Guixi-smelter): https://zh.wikipedia.org/wiki/乐德铁路
[2] zh.wikipedia, 皖赣铁路 (贵溪至乐平 89,2 km, gebouwd 1966-1970): https://zh.wikipedia.org/wiki/皖赣铁路
[3] zh.wikipedia, 德兴铜矿 (Jiangxi Copper-mijn, Dexing): https://zh.wikipedia.org/wiki/德兴铜矿
[4] Wikipedia, Jiangxi Copper (Dexing, Guixi-smelter >1 Mt/j): https://en.wikipedia.org/wiki/Jiangxi_Copper
[5] GlobalData, China five largest silver mines 2021 (Dexing 4.508 koz Ag; zoekfragment, pagina niet zelf gelezen): https://www.globaldata.com/data-insights/mining/china--five-largest-silver-mines-in-2090635/
[6] HKEX, Jiangxi Copper jaarverslag 2006 (PDF niet leesbaar): https://www.hkexnews.hk/listedco/listconews/sehk/2006/0509/0358/EWF105e.pdf
[7] Routebrief `v2/design/routebrieven/zilver-escondida-guixi.md` (anker Guixi; Jiangxi-groep 1.383,18 t Ag in 2025, stcn.com/article/detail/3702266.html)
[8] Routebrief `v2/design/routebrieven/koper-escondida-guixi.md` (binnenlands erts Dexing via de 皖赣 bij 贵溪北站, C5/C7) en `v2/data/stroomroute-zilver-escondida-guixi.json`
[9] OSM, ruwe 1-op-1-spoorways China: `v2/build-cache/raw1op1/china.geojson`, gemeten met `maak_spoorbeen_raw.py`
[sat] Esri World Imagery via `v2/tools/sat_check.py`, z14/z15, 2026-10-29: `v2/build-cache/satcheck/sat-zilver-dexing-guixi-*.png`

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 12)
**Functie:** `bak_zilver_dexing_guixi()` in `v2/tools/bak_stromen.sh`; uitvoer `v2/data/stroomroute-zilver-dexing-guixi.json` (18,9 KB, versie 2, lonlat). Geen profiel in `maak_stroombeen_weg.py` (geen wegbeen).

| # | modaliteit | km gemeten | km bron | punten | stippel | naad |
|---|---|---|---|---|---|---|
| 1 | truck | 0,6 | 0,6 hemelsbreed | 2 | ja: last mile (geen net op deze korrel) | n.v.t. |
| 2 | spoor | 152,7 | 153,2 (64 + 89,2) | 894 | nee | 3 m |
Totaal 153,3 km, 896 punten, 2 markers: `ag-dexing-mijn` (29.0432, 117.7074; 0,0 km van de lijn) en `ag-guixi-smelter` (28.3271, 117.2260; 0,05 km van de lijn).

**Recept:** b2 = `python v2/tools/maak_spoorbeen_raw.py --extract china --van 29.0485,117.7098 --naar 28.3271,117.2260 --naam zilver-dexing-guixi --uit` (geojson `spoorroute-zilver-dexing-guixi-dexing-guixi.geojson`, FeatureCollection, één run zonder via); in de functie als `--been-geojson "spoor|…"`. b1 = `--stippel "truck|…|29.0432,117.7074|29.0485,117.7098"`. Bake: `bash v2/tools/bak_stromen.sh zilver-dexing-guixi`.

**Toets:** b2 -0,3% tegen 153,2 km (norm ±15%: goed); geen naad > 5 km; markers binnen 0,5 km van de lijn; `toets_knikken.py`: 4 knikken >= 60 graden, alle 1-2 m spikes bij 28.9998,117.4034 en 28.9979,117.3590 (railknooppuntfragmenten), 0 omkeringen, 0 terugloop; `toets_rechte_benen`: alleen de bewuste stippel is recht.

**Toelichting stippel:** b1 is 0,6 km hemelsbreed tussen het registerpunt van het mijnkantoor en de plek waar de ruwe OSM-rails eindigen; geen net op deze korrel, geen eigen been.

**Lessen / bevindingen:** (1) het zilveraandeel dat via Guixi loopt en of de railhead de Sizhou-mijn is, blijft open (§7). (2) Het id belooft Guixi en de lijn eindigt daar: geen afwijking. (3) De laatste ca. 5 km lopen samen met b10 van `zilver-escondida-guixi`, geen kopie gemaakt. (4) Geen sitelaag-wijziging gedaan: Dexing ontbreekt in `zilver-sitelaag.json`, centraal gelijktrekken.
