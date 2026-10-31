# Routebrief (licht) · Diamant · Antwerpen (AWDC) → Brussels Airport → Shanghai Pudong → Shanghai Diamond Exchange (België → China)

**stroom-id:** `diamant-antwerpen-shanghai` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** gepolijste diamant van het AWDC/Diamond Office in Antwerpen gaat per truck over de E19 naar Brucargo (Brussels Airport), vliegt als vrachtvlucht (grootcirkel BRU → PVG, **aannemelijk: één bron**) naar het vrachtplatform van Shanghai Pudong (PVG) en rijdt per truck binnenstedelijk Pudong naar het China Diamond Exchange Center (Pudian Rd, Lujiazui), het gebouw van de Shanghai Diamond Exchange (SDE).
**Welke as van het verhaal:** *China-poort: Antwerpen → de enige invoerplek van het vasteland* — de SDE is het hoofdkanaal voor diamantimport in China, leden vooral uit België, India en Israël [1]. Volume: **Mct/j onbekend** (geen karaatcijfer gevonden voor België → SDE; v1 kent alleen dia-antwerp → dia-china-cut 4 Mct/j, ruwe diamant naar Guangzhou/Shenzhen, een ander product [5]). Waarde: SDE-omzet USD 4,24 mld in 2019 (peiljaar 2019) [1]; "USD 2 mld, vooral uit Antwerpen" cumulatief tot 2017 volgens de SDE-president [3]; polished-import USD 2,92 mld (2021) en 2,32 mld jan–sep 2023 (Rapaport, alleen via het ketenontwerp) [4]. Waarde per karaat hoog (gepolijst), niet in het gewicht.

## 1 · Ketenkaart
```
AWDC/Diamond Office, Antwerpen `dia-awdc` ──(b1 truck · E19 via Mechelen · LETTERLIJKE KOPIE diamant-antwerpen-newyork b1 · 37,4 km)──►
Brucargo, Brussels Airport `dia-brucargo` ──(b2 lucht · vlucht BRU → PVG, grootcirkel, aannemelijk: één bron · 9.026,8 km)──►
Shanghai Pudong vrachtplatform `dia-pvg-cargo` ──(b3 truck · Pudong, Yingbin-expresweg/S1-corridor · hemelsbreed 27,7 km, OSRM 43,7 km)──►
China Diamond Exchange Center = SDE, Lujiazui `dia-sde` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | AWDC Antwerpen → Brucargo | E19 via Mechelen; **letterlijke kopie** (noem in beennaam) van `diamant-antwerpen-newyork` b1 | hemelsbreed 34,4 km, geen wegkm (kopie 37,4) [8] | kopie `…-newyork-weg-awdc-brucargo.geojson` | nee |
| b2 | C | lucht | Brucargo (BRU) → PVG-vrachtplatform (PVG) | vlucht BRU → PVG, grootcirkel (**aannemelijk: één bron**) | 9.026,8 grootcirkel [berekend] | maak_luchtbeen | nee, doorgetrokken |
| b3 | C | truck | PVG-vrachtplatform → China Diamond Exchange Center | binnenstedelijk Pudong, richting Century Avenue (geen via-punten, zoals `goud-pamp-shanghai` b3) | hemelsbreed 27,7 km, **geen wegkm**; OSRM-demo 43,7 km (indicatie) | maak_stroombeen_weg (china) | start: korte airside-stippel (§7) |

Geen zeebeen (dus geen haven-aanloop), geen spoor, geen leiding. Het b1-geojson eindigt op 50.9056, 4.4576 (0,14 km van `dia-brucargo`); het luchtbeen **begint op dat eindpunt**, zoals in `diamant-antwerpen-newyork`. Het luchtbeen eindigt op `dia-pvg-cargo`, waar b3 begint.
Brongrond b2: geen bron noemt een diamantvlucht BRU → PVG. Wel: alle diamantimport naar China loopt via de SDE, met leden uit België [1], en Brussels Airport heeft lijnvluchten naar Shanghai-Pudong (Hainan Airlines, Juneyao Air; belly-capaciteit) [6]. Dat is één bron voor de bestemming, dus "aannemelijk" in de beennaam.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-awdc` | handelshub / vertrek | AWDC/Diamond Office, Hoveniersstraat 22, Antwerpen | 51.2152, 4.4187 | [8] (`diamant-antwerpen-surat` §3, `…-newyork` §3) | bron-gelegd, hergebruikt (z15 daar: dicht stedelijk bouwblok in de Diamantwijk) |
| `dia-brucargo` | overslag truck → lucht | Brucargo, Brussels Airport | 50.90628, 4.45584 | [8] (`diamant-antwerpen-newyork` §3) | bron-gelegd, hergebruikt (z15 daar: vrachtloodsen en platform met toestellen) |
| `dia-pvg-cargo` | overslag lucht → truck | Shanghai Pudong International Airport, vrachtplatform (zie §7) | 31.1335, 121.8025 | [8] (`diamant-mumbai-shanghai` §3, `goud-pamp-shanghai` §3) | **aannemelijk**, hergebruikt; eigen z15 (`…-pvg-cargo.png`): kruis aan de westflank van het satellietterminal tussen passagierstoestellen, geen vrachtzone |
| `dia-sde` | beurs-/handelsgebouw / eindpunt | 中国钻石交易中心 (China Diamond Exchange Center), 浦电路, Lujiazui, Pudong | 31.2265, 121.5320 | [2][7] OSM relatie 19575398 | bron-gelegd (z17 `…-sde-z17.png`: kruis op een laagbouwcomplex aan de voet van torens in dicht Lujiazui, tussen laan en Pudian Rd; geen bord of eigen terrein zichtbaar) |
Kandidaat vrachtzone PVG (niet gebruikt): 31.1222, 121.8064 (eigen z16 `…-pvg-cargo-kandidaat.png`: platform met wide-body vrachttoestellen, grote loodsen).

## 4 · Via-punten
Geen. b1 is een kopie (via-punten daar: Antwerpen-Zuid 51.1103, 4.4319 en E19 bij Mechelen 51.0213, 4.4481), b2 is een grootcirkel, b3 is één binnenstedelijke expressway-corridor zonder corridorkeuze. Geofabrik-regio's: **china** voor b3 (extract aanwezig); b1 vraagt geen scan.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Shanghai Diamond Exchange | SDE (opgericht Lujiazui 27-10-2000, 362 leden eind 2019) | import polished/rough → registratie, keuring, invoerklaring, factuur | omzet USD 4,24 mld (2019) | [1] |
| AWDC/Diamond Office | AWDC | export- en importklaring, certificering | geen cijfer | [8] |
Geen smelter of slijperij: de stenen zijn al gepolijst.

## 6 · Stoppunt
De brief stopt bij de SDE: het ontwerpeindpunt en het enige invoerplatform; geen bron koppelt deze lading aan een juwelier of retailer. Fase D en E vervallen.

## 7 · Open punten
- **Geen bron voor een directe stroom of vlucht Antwerpen → SDE.** Alleen: de SDE-president zegt dat de import "vooral uit Antwerpen" komt [3], leden zijn vooral Belgisch, Indiaas en Israëlisch [1], en de AWDC en SDE werken sinds 2010 samen [4]. Vervoerswijze, vluchtnummer en tussenlanding zijn niet gebrond; BRU → PVG kan via een hub lopen (Hongkong is de grotere poort). Eén directe grootcirkel is schematisch.
- **Het adres 2001 Century Avenue is het adres van de Pudong-overheid** (footer van [1]), niet van de SDE; het is niet als bron voor dit anker gebruikt. Het SDE-anker rust op OSM-gebouw `中国钻石交易中心` (Nominatim lookup R19575398: 31.22654, 121.53203, building=commercial, 浦电路) [2][7]; dat dit gebouw de SDE-handelszaal huisvest komt uit het ketenontwerp (arch2o, 2009), niet door mij gelezen.
- **PVG-anker ligt op de passagiersapron**; de vrachtzone ligt ±1,2 km zuidelijker (31.1222, 121.8064, gezien op z16). Bewust hergebruikt (consistentie met `goud-pamp-shanghai`, `pgm-rustenburg-shanghai`, `diamant-mumbai-shanghai`); correctie hoort centraal voor alle vier tegelijk. Effect op b2 <0,03%; b3 wordt ±1,2 km korter of langer.
- **b3: airside.** OSRM-demo snapt het PVG-anker op een weg 538 m verder (31.1350, 121.8079). Laat b3 eindigen/beginnen op de eerste openbare weg die `maak_stroombeen_weg` vindt en sluit af met een korte `--stippel "truck|PVG-vrachtplatform last mile (schematisch — airside/privéterrein)|…"` (patroon `bak_goud_pamp_shanghai`).
- **b3 heeft geen gepubliceerde wegkm**: hemelsbreed 27,7 km, OSRM-demo 43,7 km; de ±15%-toets is een indicatie, geen norm. b3 loopt grotendeels over de corridor van `goud-pamp-shanghai` b3 (eindpunt 3,1 km verder, geen kopie mogelijk).
- **Volume Mct/j onbekend**; België → China/Hongkong samen was USD 727 mln in Q1 2010 (Rapaport) [4]; het mainland-aandeel is niet apart gebrond. Lab-grown en de zwakke Chinese vraag drukken het volume, niet de route.
- GIA-artikel (ontwerpbron) was niet bereikbaar (timeout); Rapaport `?p=16721` gaf 403/geen tekst. Beide alleen via het ontwerp.

## 8 · Bronnen
[1] Shanghai Pudong-overheid, "Shanghai Diamond Exchange" (opgericht Lujiazui 2000-10-27; leden vooral groothandelaren uit België, India, Israël; omzet 4,24 mld USD in 2019, 362 leden). https://english.pudong.gov.cn/2025-06/03/c_499178.htm
[2] OSM Nominatim lookup, relatie 19575398: 中国钻石交易中心, 浦电路, Pudong, 31.2265426, 121.5320333, building=commercial (live 2026-10-31). https://www.openstreetmap.org/relation/19575398
[3] China Daily, 2017-09-05, Antwerp-SDE-overeenkomst (SDE-president Lin Qiang: "$2 billion worth of diamonds, mostly from Antwerp" geïmporteerd via het platform). https://global.chinadaily.com.cn/a/201709/05/WS59bca157a310ded8ac19193d.html
[4] Rapaport, 2010-05-11, "Antwerp Goes to Shanghai" (AWDC-SDE joint venture; België → China + Hongkong polished USD 727 mln in Q1 2010; gaf geen vervoerswijze of SDE-adres). https://rapaport.com/magazine-article/antwerp-goes-to-shanghai/ — plus Rapaport `?p=16721` (SDE-polishedimport 2021/2023, via ontwerp, niet gelezen).
[5] v1 `design/diamant.md` §4 en `data/diamond.js` (dia-antwerp → dia-china-cut 4, air; dia-antwerp → dia-mkt-china niet aanwezig) — intern.
[6] Wikipedia, "Brussels Airport" (Hainan Airlines en Juneyao Air vliegen Brussel–Shanghai-Pudong; geen vrachtdienst BRU–PVG in de cargolijst; geraadpleegd via API 2026-10-31). https://en.wikipedia.org/wiki/Brussels_Airport
[7] Ketenontwerp en haalbaarheidstoets M31 golf 17 (`diamant-antwerpen-shanghai`; webcheck: Nominatim R19575398, arch2o 2009, sat z16/z17) — intern.
[8] Brieven `diamant-antwerpen-newyork` (b1-kopie, ankers AWDC/Brucargo), `diamant-antwerpen-surat`, `diamant-mumbai-shanghai` en `goud-pamp-shanghai` (PVG-anker, b3-patroon).
[9] Esri World Imagery via `v2/tools/sat_check.py` (live 2026-10-31): `v2/build-cache/satcheck/sat-diamant-antwerpen-shanghai-{sde,sde-z17,pvg-cargo,pvg-cargo-kandidaat}.png`.
[10] OSRM-demo (router.project-osrm.org), PVG-anker → SDE: 43,7 km (alleen indicatie), 2026-10-31.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
`bash v2/tools/bak_stromen.sh diamant-antwerpen-shanghai` -> `v2/data/stroomroute-diamant-antwerpen-shanghai.json` (28,9 KB, versie 2, lonlat). Totaal 9.100,5 km · 1.399 punten · 4 markers · 4 benen (1 stippel), naden 0,000 / 0,000 / 0,000 / 0,002 km.
| # | modaliteit | km | geometrie |
|---|---|---|---|
| b1 | truck | 37,4 | letterlijke kopie `diamant-antwerpen-newyork` b1 (E19 via Mechelen), beennaam noemt de kopie |
| b2 | lucht | 9.026,8 | `maak_luchtbeen.py` BRU -> PVG, grootcirkel, 363 punten, doorgetrokken; "aannemelijk: één bron" in de beennaam |
| b3a | truck (stippel) | 0,55 | PVG-vrachtplatform last mile (schematisch — airside/privéterrein), 31.1335,121.8025 -> 31.1360,121.8075 |
| b3b | truck | 35,7 | wegscan china, profiel `diamant-antwerpen-shanghai-pvg-sde`, geen via-punten, 599 punten |
Markers: dia-awdc (0,03 km van de lijn) · dia-brucargo (0,15 km) · dia-pvg-cargo (0,0) · dia-sde (0,0).
- **Km-toets b3:** 35,7 km tegen hemelsbreed 27,7 (+29%) en OSRM-demo 43,7 (-18%). Geen echte wegkm, dus indicatie; het wegtool meldt +27,5% op de gepubliceerde 28. Bevinding, geen via-punt bijgeschoven. b1: kopie 37,4 tegen hemelsbreed 34,4, idem indicatie.
- **Airside-stippel:** de scan begon op het anker met een rechte aanloop van 0,55 km naar de eerste openbare weg (121.8075, 31.1360; OSRM snapte op 538 m, zelfde plek). Die aanloop is uit het wegbeen geknipt (`…-weg-pvg-sde-openbaar.geojson`, scan-origineel blijft `…-weg-pvg-sde.geojson`) en als korte stippel getekend. Het anker staat op het passagiersapron; de vrachtzone (31.1222, 121.8064) is centraal te corrigeren voor alle PVG-stromen, dan moet b2/b3 mee.
- **Vlucht:** doorgetrokken omdat het geen netgat is; claim = "van deze vrachtterminal naar die". Geen bron voor een directe BRU -> PVG diamantvlucht of een tussenlanding (HKG).
- **Kniktoets:** 30 knikken >= 60 gr, 0 omkeringen, 0 terugloop (stedelijke knooppunten Pudong, Yanggao/Century Avenue, korte radii 7-16 m = wegpunt-korrel). Geen haven-aanloop, geen zee, geen spoor, geen leiding, geen via-punten.
- **Lessen:** (1) de wegscan van een reus-extract (china) duurde 405 s; log in `v2/build-cache/ais/graaf/diamant-antwerpen-shanghai-wegscan.log`, tweede run is cache. (2) Een anker airside geeft een rechte aanloop in het scan-geojson; knip die vóór het bakken en maak er een stippel van in plaats van hem als "weg" te tekenen.
