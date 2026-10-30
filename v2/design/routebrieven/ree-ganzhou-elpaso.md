# Routebrief (licht) · Zeldzame aardmetalen · JL MAG Ganzhou → Xiamen → Long Beach → Nidec El Paso (VS)

**stroom-id:** `ree-ganzhou-elpaso` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Titel (bol):** Zeldzame aardmetalen · JL MAG Ganzhou → Xiamen → Long Beach → Nidec El Paso (NdFeB-magneten, aannemelijk: notify-adres uit handelsdata)
**Keten in één zin:** NdFeB-magneten van JL MAG in Ganzhou gaan per truck (G76) naar de containerhaven Xiamen (Haicang), per containerschip over de Stille Oceaan naar Long Beach en per truck (SR-91, I-10 via Phoenix, Tucson en Deming) naar het Nidec-adres 490-A Bill Burnett Dr in El Paso.
**Welke as van het verhaal:** Chinese magneten naar een Tier-1 motorleverancier aan de Mexicaanse grens, via Xiamen en niet via Yantian (andere haven en ander eindpunt dan `ree-ganzhou-fremont`). Nidec-zendingen: 41 containers / 59,7 t, lopend totaal over meerdere jaren, laatste B/L 2026-10-28 [1]; geen jaarvolume. JL MAG bedrijfsbreed: 29,3 kt blanks gemaakt in 2024, capaciteit 38,0 kt NdFeB/j [2][3].

**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** geen; zoals ontworpen, met de b1-via-punten uit de toets (alle drie binnen 5 m van de 厦蓉高速, OSRM [5]) en de Haicang-aanloop als rechte stippel. Het Nidec-adres is een notify-adres, geen bevestigde fabriek.

## 1 · Ketenkaart
```
JL MAG Ganzhou `ree-ganzhou-jlmag` ──(b1 truck · G76 Xiamen-Chengdu · hemelsbreed 348 km, geen wegkm)──►
Xiamen Haicang CT `ree-xiamen-haicang` ──(b2 aanloop, stippel · 5,7 km)──► zeeknoop 5576
──(b3 zee · MARNET · Taiwanstraat → noordelijke Stille Oceaan · 11.479,5 km)──► zeeknoop 4488
──(b4 aanloop Long Beach, stippel · 8,5 km, KOPIE)──► Long Beach-kade `ree-longbeach-kade`
──(b5 truck · SR-91 → I-10 · hemelsbreed 1.140 km, geen wegkm, aannemelijk)──► Nidec El Paso `ree-elpaso-nidec` ⏹
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-ganzhou-jlmag` → `ree-xiamen-haicang` | G76 Xiamen-Chengdu (Ganzhou, Ruijin, Longyan, Zhangzhou), refs G76 S61 | hemelsbreed 348 km, geen wegkm (OSRM 436,2 is OSM-afgeleid, indicatie) [5] | maak_stroombeen_weg (extract china) | nee |
| b2 | B | zee (haven-aanloop) | `ree-xiamen-haicang` → zeeknoop 5576 (24.4515,117.9163) | Xiamen-baai; kade 5,7 km van de knoop (> 5 km, LAR-586) | 5,7 (rechte stippel; `maak_havenaanloop.py` vond hier geen pad in 300 s) [8] | KOPIE van de `--stippel`-regel uit `bak_kobalt_obi_ganzhou`, in reisvolgorde kade → knoop (omgekeerd) | **ja** (net reikt niet) |
| b3 | B | zee (aannemelijk: haven uit handelsdata) | zeeknoop 5576 → zeeknoop 4488 (33.7039,-118.1945) | Taiwanstraat, noordelijke Stille Oceaan | 11.479,5 (eigen MARNET-proef, snap 0,000 km) [12] | MARNET | nee |
| b4 | B | zee (haven-aanloop) | zeeknoop 4488 → `ree-longbeach-kade` | Long Beach-havenbekken; kade 6,47 km van de knoop | 8,5 (handgelegd) [9] | LETTERLIJKE KOPIE `ree-yunsheng-longbeach-aanloop-longbeach.geojson` (knoop → kade) | **ja** |
| b5 | D | truck (aannemelijk: één bron, notify-adres) | `ree-longbeach-kade` → `ree-elpaso-nidec` | SR-91, CA-60, I-10 via Blythe, Phoenix, Tucson, Deming, El Paso | hemelsbreed 1.140 km, geen wegkm (OSRM 1.332,3 is OSM-afgeleid, indicatie) [5] | maak_stroombeen_weg (us-california, us-arizona, us-new-mexico, us-texas) | nee |
Beennamen: b3 "… (aannemelijk: haven uit handelsdata)"; b5 "… (aannemelijk: één bron, Nidec-notify-adres, waarschijnlijk logistiek)". Geen luchtbeen: de B/L toont zee (vessel OOCL London) [1]. Geen last-mile-been: b1 eindigt 0,14 km van het Haicang-anker op de weg, b5 op het anker (2 m van Bill Burnett Dr).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-ganzhou-jlmag` | magneetfabriek (kop b1) | JL MAG Rare-Earth, Ganzhou (hergebruikt `w-jlmag-ganzhou`, bron-brief `ree-ganzhou-fremont`) | 25.8406, 114.8663 | [3][10] | bron-gelegd (hergebruikt letterlijk; sitelaag: industrieel complex in de ontwikkelingszone; OSRM-weg op 3 m) |
| `ree-xiamen-haicang` | overslag truck → zee | Xiamen Haicang Container Terminal (hergebruikt `co-xiamen-haicang`, bron-brief `kobalt-obi-ganzhou` §3) | 24.4585, 117.9720 | [8] | bron-gelegd (hergebruikt letterlijk; z16 daar: containerstapels, kranen op de kadelijn; terminal voor deze lading niet bevestigd, B/L noemt alleen Xiamen) |
| `ree-longbeach-kade` | overslag zee → truck | containerkade Long Beach, westkade oostelijk havenbekken (hergebruikt uit `ree-yunsheng-longbeach`) | 33.7600, -118.2132 | [9] | aannemelijk (hergebruikt letterlijk; terminal niet bevestigd) |
| `ree-elpaso-nidec` | afnemer / logistiek adres (staart b5) | Nidec Automotive Motor Americas LLC, 490-A Bill Burnett Dr, El Paso TX 79928 | 31.6963, -106.2685 | [1][6] ArcGIS-geocode score 100 | aannemelijk (z15/z16 gezien: braak hoekperceel op de kruising Bill Burnett Dr/Rojas Dr, kruis 2 m van de weg [5]; ten noorden en oosten witte distributiehallen met trailerparkeerplaatsen; geen herkenbaar Nidec-pand) [7] |

## 4 · Via-punten (alleen landbenen b1 en b5)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | G76 bij Ruijin, oost | 25.9256, 115.9775 | pint G76/G35 oostwaarts uit Ganzhou (4 m van de 厦蓉高速, OSRM [5]) |
| b1 | 2 | G76 bij Longyan, zuid | 24.9336, 117.1186 | pint de doorsteek Jiangxi-Fujian over G76 en niet een kustroute (4 m van de weg) |
| b1 | 3 | G76 bij Zhangzhou, noord | 24.6239, 117.5704 | pint de aanvoer naar Xiamen vanuit het noordwesten (4 m van de weg) |
| b5 | 1 | Long Beach-kade (anker) | 33.7600, -118.2132 | kop op de kade (nearest weg 275 m) |
| b5 | 2 | SR-91 Riverside Fwy, Anaheim Hills | 33.8688, -117.7300 | pint SR-91/CA-60 naar I-10 i.p.v. I-10 door downtown LA (uit `ree-cheongju-sanmarcos` §4) |
| b5 | 3 | I-10 bij Blythe | 33.6478, -114.3233 | pint I-10 door de Colorado-woestijn, geen I-8 |
| b5 | 4 | I-10 Tonopah, west van Phoenix | 33.5542, -113.2575 | pint I-10 langs Phoenix, geen I-8 zuid |
| b5 | 5 | I-10 Benson | 31.9651, -110.2650 | pint I-10 oostwaarts na Tucson |
| b5 | 6 | I-10 Deming | 32.2457, -107.1539 | pint I-10 door New Mexico (OSRM Deming → Nidec: 131 km, één weg) |
| b5 | 7 | Nidec-anker | 31.6963, -106.2685 | staart; ligt 2 m van Bill Burnett Dr, dus geen aparte last-mile-via |
Alle b5-via-punten komen letterlijk uit het profiel `ree-cheongju-sanmarcos-longbeach-sanmarcos` (gescand, snaps ≤ 0,27 km). Refs b5 ["I 10"]; vensterKm 75 (Phoenix ligt ca. 50 km van de rechte lijn Tonopah-Benson). Regio's b1: china; b5: us-california, us-arizona, us-new-mexico, us-texas.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| JL MAG Ganzhou | JL MAG Rare-Earth Co., Ltd | NdPr-metaal/legeringen → NdFeB-magneten | 38,0 kt NdFeB/j bedrijfsbreed; 29,3 kt blanks (2024) | [2][3] |
| Nidec El Paso (notify-adres) | Nidec Automotive Motor Americas LLC | magneten → (vermoedelijk) naar motorfabrieken over de grens | niet gepubliceerd | [1][13] |

## 6 · Stoppunt
Bij het Nidec-adres in El Paso: de B/L noemt dit adres als importeur en notify party; welke fabriek of welk magazijn de magneten verder verwerkt is niet gebrond, dus de lijn eindigt waar het bewijs eindigt.

## 7 · Open punten
- **Het adres is een logistiek punt, geen fabriek.** 490-A Bill Burnett Dr ligt in een distributiepark; een zoekresultaat noemt voor Nidec El Paso een warehouse op 9 Butterfield Trail Blvd (niet geverifieerd) [13]. Of de Mexicaanse fabrieken verder leveren is niet gebrond.
- **Laadvestiging onbewezen:** de B/L noemt shipper "JL MAG Ganzhou ETDZ", receipt Xiamen [1]; of de container in Ganzhou geladen is, is niet gezien (anker aannemelijk).
- **Terminal in Xiamen onbekend:** de B/L noemt alleen Amoy/Xiamen; Haicang is het eerder gelegde anker. Het vervoer over land in de VS (vrachtwagen, spoor of in-bond) is niet gebrond.
- **Geen wegkm** voor b1 (hemelsbreed 348, OSRM 436,2) en b5 (hemelsbreed 1.140, OSRM 1.332,3); de ±15%-toets is een indicatie. De Wikipedia-lengte van G76 (2.192,2 km) betreft de hele weg, geen deellengte [4].
- Zelfde begin als `ree-ganzhou-fremont` en `ree-ganzhou-hanau`; alleen de kop is gedeeld, geen been.

## 8 · Bronnen
[1] ImportGenius, JL MAG Rare-Earth Co., Ltd: Nidec 41 containers / 59.659 kg, laatste B/L 2026-10-28; B/L BANQ1077434257, OOCL London 126E, Amoy → Long Beach, notify Nidec 490 A Bill Burnett Dr. https://www.importgenius.com/suppliers/jl-mag-rare-earth-co-ltd
[2] SMM, JL MAG 2024: 29.300 t blanks, bezetting > 90%. https://news.metal.com/newscontent/103258207/JL-MAG-Rare-Earth-Sets-New-Highs-with-Over-90-Capacity-Utilization-in-2024
[3] `v2/design/ree-sitelaag.json`, site `w-jlmag-ganzhou` (25,8406 / 114,8663; 38,0 kt NdFeB/j bedrijfsbreed).
[4] Wikipedia, "G76 Xiamen-Chengdu Expressway": 2.192,2 km bij gereedkomen, oostelijk uiteinde Xiamen. https://en.wikipedia.org/wiki/G76_Xiamen%E2%80%93Chengdu_Expressway
[5] OSRM (router.project-osrm.org), eigen meting 2026-10-30: Ganzhou → Haicang 436,2 km; Long Beach → Nidec 1.332,3 km; Deming → Nidec 131,0 km; b1-via-punten op 厦蓉高速 (4 m); Nidec-anker 2 m van Bill Burnett Dr. OSM-afgeleid, geen onafhankelijke bron.
[6] ArcGIS World Geocoder, "490 Bill Burnett Dr, El Paso": 31.69625, -106.26853, score 100 (Nominatim zet de straat 0,4 km noordoostelijker, 31.6988/-106.2655). https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer
[7] Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-ree-ganzhou-elpaso-nidec.png` (z15) en `…-nidec-z16.png` (z16).
[8] `v2/design/routebrieven/kobalt-obi-ganzhou.md` §3/§9 en functie `bak_kobalt_obi_ganzhou`: Haicang-anker (24.4585,117.9720), zeeknoop 5576 (24.4515,117.9163), rechte stippel 5,7 km.
[9] `v2/design/routebrieven/ree-yunsheng-longbeach.md` §2/§3/§9: Long Beach-kade en handgelegde aanloop (8,5 km, zeeknoop 4488, kade 6,47 km).
[10] `v2/design/routebrieven/ree-ganzhou-fremont.md` en functie `bak_ree_ganzhou_fremont`: patroon voor Long Beach-aanloop-kopie en JL MAG-anker.
[11] `v2/design/routebrieven/ree-cheongju-sanmarcos.md` §4/§9 en profiel `ree-cheongju-sanmarcos-longbeach-sanmarcos`: I-10-via-punten, scan 2.278 km, venster 75.
[12] MARNET (`hecht_marnet.py route`), eigen proef 2026-10-30: 24.4515,117.9163 → 33.7039,-118.1945 = 11.479,5 km, snaps 0,000 km.
[13] Nidec, wereldwijde bases (https://www.nidec.com/en/worldwide_new/hq/nidec_automotive_motor_americas_el_paso_wearhouse; pagina laadt kaartdata dynamisch) en een zoekresultaat dat een El Paso-warehouse noemt: adres niet bevestigd.
[14] Haalbaarheidstoets M31 golf 16 voor `ree-ganzhou-elpaso` (workflow-invoer): via-punten b1, Nidec-anker, aanloop-kopieen.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
Bestand `v2/data/stroomroute-ree-ganzhou-elpaso.json` (271,2 KB, versie 2, lonlat), functie `bak_ree_ganzhou_elpaso` in `bak_stromen.sh`, profielen `ree-ganzhou-elpaso-ganzhou-haicang` en `ree-ganzhou-elpaso-longbeach-nidec` in `maak_stroombeen_weg.py`. Totaal 13.283,3 km, 5 benen, 4 markers, alle naden 0,000 km. Eindpunt = id (Nidec El Paso, notify-adres), geen afwijking van het ontwerp.

| # | modaliteit | km gebakken | bron / norm | stippel | geometrie |
|---|---|---|---|---|---|
| b1 | truck | 445,3 | geen wegkm; OSRM 436,2 (indicatie), +2,1% | nee | nieuw profiel, extract china, 5 via-punten incl. ankers |
| b2 | zee | 5,7 | gemeten (rechte lijn) | ja: net reikt niet (Haicang-kade 5,7 km van knoop 5576, LAR-586) | omgekeerde letterlijke kopie van de `--stippel`-regel in `bak_kobalt_obi_ganzhou` (kade naar knoop) |
| b3 | zee | 11.479,5 | MARNET-proef 11.479,5 | nee | MARNET knoop 5576 naar 4488, snaps 0,000 km |
| b4 | zee | 8,5 | gebakken 8,5 | ja: handgelegd, kade 6,47 km van knoop 4488 | LETTERLIJKE KOPIE `ree-yunsheng-longbeach-aanloop-longbeach.geojson` (knoop naar kade) |
| b5 | truck | 1.344,3 | geen wegkm; OSRM 1.332,3 (indicatie), +0,9% | nee | nieuw profiel, extracts us-california, us-arizona, us-new-mexico, us-texas, 7 via-punten incl. ankers |

**Markers:** alle vier op de lijn (0,000 km). Geen last-mile-been, geen lucht, spoor, binnenvaart of leiding.

**Recept b1.** `wegscan_puur.py` (china, 536 s scan). Via (lon, lat) = de drie brief-punten plus beide ankers, refs G76 en S61, venster 40 km (volstond). Segmenten 133,7 + 183,6 + 69,8 + 58,0 km, snaps 0,00-0,16 km. Eerste mijl 0,38 km, laatste mijl 1,16 km over kleine klassen.

**Recept b5.** `wegscan_puur.py` (4 extracts, venster 75 km, ~12 min scan). Via (lon, lat) = de brief-punten letterlijk uit `ree-cheongju-sanmarcos-longbeach-sanmarcos` plus het Nidec-anker. Segmenten 51,6 + 359,5 + 100,4 + 374,3 + 325,7 + 132,5 km, snaps <= 0,27 km, route I-10 via Phoenix en Tucson. Eerste mijl 0,99 km, laatste mijl 0,00 km; 10 keerlussen gesnoeid. `eindToegangPrivaat` True.

**Toets.** Contract ok (versie 2, lonlat, modaliteiten zee en truck, elk been >= 2 punten). Geen naad > 0,000 km. `toets_rechte_benen --min-km 5`: alleen de Haicang-aanloop (rechte stippel, verwacht). `toets_knikken`: b1 heeft 2 TERUGLOOP-meldingen (172,0 en 170,5 graden, 24.4813,117.9662 en 24.4820,117.9614) bij het Haicang-knooppunt van de G76; b5 heeft 1 scherpe bocht (176 graden, 13 m) vlak bij het Nidec-anker plus spikes van 5-20 m op afritten bij Long Beach en El Paso.

**Bevindingen.** (1) b1 doorloopt aan het Haicang-eind (puntindex 3017-3027) een lus van ~1 km over de motorway_link-ramp 606025654/606025655 tegen de rijrichting in (de scanner kent geen eenrichting) naar de residential 606340311, tegen ~0,4 km voor de rechte doorsteek; OSRM rijdt hier rechtdoor over de G76 en dan via 24.4685,117.976 terug. Niet bijgeschoven: een via-punt om dit te verhelpen zou een tweede volledige china-scan (9 min) kosten voor 1 km op 13.283 km; de lijn eindigt wel correct op de kade. (2) Geen gepubliceerde wegkm: de +-15%-toets (b1 371-502, b5 1.132-1.532) is een indicatie op OSM-afgeleide OSRM-lengtes. (3) Nidec-adres is een notify-/logistiek adres, geen bevestigde fabriek; Haicang-terminal voor deze lading niet bevestigd.

**Lessen.** (1) Een korte omgekeerde stippelkopie (kade naar knoop) is een gewone `--stippel`-regel met omgedraaide coordinaten; naad 0,000 km. (2) Een via-set die al elders gescand is (I-10 Long Beach naar Deming) herbruik je letterlijk; alleen de staart verandert. (3) De scanner negeert eenrichtingsverkeer: bij een snelwegeind op een knooppunt kan de lijn een ramp tegen de rijrichting volgen; check de laatste kilometers naast OSRM.
