# Routebrief (licht) · kolen — Datong → Qinhuangdao → Haimen (China)

**stroom-id:** `kolen-datong-haimen` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** Shanxi-steenkool gaat per **spoor** over de Daqin-lijn (大秦铁路, 653 km) van Datong naar de
kolenkade van Qinhuangdao, per **kustvaart (binnenlands)** ~2.300 km langs de Chinese kust naar de Huaneng-
kolenterminal Shantou-Haimen (Guangdong), en per **band** over eigen terrein naar de ketelhuizen van de Huaneng
Haimen-centrale — stoppunt, want de centrale zet kolen in één stap om in stroom.
**Welke as van het verhaal:** *binnenlands "noord-kool zuid-transport"* — de ~85 %-laag van de wereldkolenhandel
die geen grens over hoeft. Daqin vervoerde **422 Mt in 2023** (>1/5 van al het Chinese spoorkolenvervoer) [1];
Qinhuangdao's kolendoorzet wordt voor 2024 geschat op **180–200 Mt** [2]; de Haimen-terminal heeft een
capaciteit van **22,7 Mt/jaar**, waarvan 12 Mt/jaar bestemd voor de 6 eigen Haimen-centrale-eenheden en 10,7 Mt
voor overige afnemers in Oost-Guangdong/Jiangxi [3][5]. Het aandeel van déze specifieke keten (Datong-kool via
Qinhuangdao naar Haimen) in dat volume is niet gepubliceerd — zie §7.

## 1 · Ketenkaart
```
Daqin-spoorkop (Hudong, mijn niet gebrond) `kolen-datong-kop`
   ──(b1 spoor · Daqin-lijn 大秦铁路 · 653 km)──► Qinhuangdao-kolenkade `kolen-qhd-kade`
   ──(b2 kustvaart (binnenlands) · Bohai–Gele Zee–Oost-Chinese Zee–Straat Taiwan · ~2.300 km,
       aannemelijk: geen bron voor dit havenpaar)──► Haimen-losligplaats `kolen-haimen-kade`
   ──(b3 leiding/band · eigen terrein Huaneng · ~1 km, stippel)──► Huaneng Haimen-centrale `kolen-haimen-centrale` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-datong-kop` → `kolen-qhd-kade` | Daqin-spoorlijn (大秦铁路), dubbelsporig geëlektrificeerd heavy-haul, via Yangyuan – Shacheng – Zunhua | 653 [1] (toets: 685,1 km over 11 legs, +4,9 %, binnen ±15 %) | spoor (1-op-1-OSM-net) via 3 via-punten (§4) | nee — Daqin-lijn zit volledig in het 1-op-1-spoornet |
| b2 | B | kustvaart (binnenlands) | `kolen-qhd-kade` → `kolen-haimen-kade` | Bohai → Gele Zee → Oost-Chinese Zee → Straat Taiwan; CBCFI-benchmarkroute Qinhuangdao–Guangzhou loopt hetzelfde | ≈ 2.300 (afgeleid; geen operator-cijfer) | MARNET | nee — **aannemelijk: geen bron voor dit havenpaar** (GEM: Haimen "coal source(s): imported" [4]) |
| b3 | C | leiding (transportband, bol-modaliteit "leiding") | `kolen-haimen-kade` → `kolen-haimen-centrale` | eigen terrein Huaneng (terminal is gebouwd als "coal transit base" voor de eigen centrale) | ≈ 1 (op satelliet gemeten) | stippel "leiding" — OSM `man_made=goods_conveyor` niet op naam vindbaar, dus geen way, wel de band-modaliteit uit §2 van de bakhandleiding | ja — net reikt niet, eigen terrein |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-datong-kop` | spoorkop (mijn niet gebrond) | westelijkste OSM-vertex van de Daqin-lijn, ten zuiden van Datong (kandidaat Hudong-emplacement / Tashan-mijnstreek) | 39.9905, 113.2324 | [10][11] | onzeker (z15 gezien: spoorkruising met industrieterrein en een donkere opslagvlek net ZO; geen specifieke mijn- of stationsnaam op het beeld te herkennen — geen bron vindt één mijn met eigen laadstation hier) |
| `kolen-qhd-kade` | overslag spoor → zee | Qinhuangdao-kolenterminal, Port of Qinhuangdao | 39.9290, 119.6440 | [2][11] | bron-gelegd (z15 gezien: rijen geordende kolenstapels op een omvangrijk terreinplateau, laadband naar een steiger met schepen aan de oostzijde) |
| `kolen-haimen-kade` | losplek zee | Huaneng-kolenterminal Shantou-Haimen (losligplaats/coal transit base) | 23.1810, 116.6595 | [3][5][11] | bron-gelegd (z16 gezien: donkere kolenstapels — deels onder tarpaulin — vlak naast een pier die de zee in steekt, direct zuidelijk van de centrale) |
| `kolen-haimen-centrale` | verwerker / afnemer | Huaneng Haimen Power Station, Shantou, Guangdong | 23.1899, 116.6548 | [4][11] | bron-gelegd (z15 gezien: ketelhuizen, schoorstenen en twee ronde silo's op een landtong direct aan zee) |

## 4 · Via-punten (alleen b1 — de spoorlijn heeft een corridorkeuze bij elke aftakking)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Yangyuan (Daqin-vertex) | 40.0160, 113.8160 | OSM-vertex op de benoemde Daqin-way; een vrije Dijkstra zonder dit punt sprong naar een parallelle lijn (verhouding tot 7,2, toets) |
| b1 | 2 | Shacheng (Daqin-vertex) | 40.3238, 115.2013 | idem — pint de hoofdlijn tussen Yangyuan en Zunhua op de Daqin-way-vertex i.p.v. een plaatsnaam-centroïde |
| b1 | 3 | Zunhua-N (Daqin-vertex) | 40.1911, 117.8999 | laatste corridorkeuze vóór het havenemplacement van Qinhuangdao; ná dit punt volgen 3 omkeringen op het emplacement zelf (toets, bekend en acceptabel) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Haimen-terminal ("coal transit base") | Huaneng Power International / Shantou Port Group | kolenschip (kustvaart) → kolenopslag → band | 22,7 Mt/j (21,5 Mt lossen + 1,2 Mt laden); 12 Mt/j voor de 6 Haimen-eenheden, 10,7 Mt voor Oost-Guangdong/Jiangxi; eigen kustschip 华能汕运1 | [3][5][7] |
| Huaneng Haimen Power Station | Huaneng Power International | kolen → elektriciteit (ketelhuis, geen tussenproduct) | 4×1.036 MW operationeel; eenheden 5–6 in aanbouw (dec 2026/feb 2027) | [4] |

## 6 · Stoppunt
De brief stopt bij het ketelhuis van Huaneng Haimen: een centrale zet kolen in één stap om in elektriciteit —
er is geen smelter/raffinaderij-fase en dus geen fase D/E voor deze as (zie de context-opmerkingen bij het ontwerp).

## 7 · Open punten
- **Mijnkop niet gebrond:** geen bron legt één specifieke Datong-mijn met eigen laadstation aan de Daqin-lijn;
  het anker `kolen-datong-kop` is de westelijkste OSM-vertex van de lijn, geen bevestigde mijn (Tashan/Jinneng is
  kandidaat, Hudong het beginemplacement — beide niet op naam in OSM gevonden).
- **Havenpaar Qinhuangdao → Haimen nergens rechtstreeks gebrond:** GEM tagt Haimen als deels "coal source(s):
  imported" [4]; de herkomst-uit-Qinhuangdao is alleen indirect (Huaneng bouwde de terminal als eigen "coal
  transit base" en de terminalcapaciteit is voor 12 Mt/j aan de eigen centrale gekoppeld [3][5]) — status van b2
  blijft *aannemelijk*, en mogelijk is een deel van de aanvoer Indonesische importkool i.p.v. Shanxi-kool.
- **Via-punten b1 zijn ingekort tot 3** (van de 11 die in de toets zijn gemeten); als de bake met deze 3 meer dan
  ±15 % van 653 km afwijkt, moet de bak-agent de fijnere vertexlijst gebruiken (zie bak_aanwijzingen).
- **Band terminal → centrale** niet als `man_made=goods_conveyor` in OSM gekarteerd; stippel "eigen terrein" is
  de veilige aanname (chinaports.org bevestigt wel het fysieke bestaan van de koppeling [5]).
- **Aandeel van déze keten** in het Haimen-volume (welk deel van de 22,7 Mt/j uit Datong/Qinhuangdao komt i.p.v.
  uit andere Noord-Chinese havens) is niet gepubliceerd.
- **Harder gebronde alternatieve keten, niet gecheckt:** de CHN Energy-eigen keten Shendong-mijnen →
  Shuohuang-spoorlijn → Huanghua-haven → Zhuhai Gaolan-kolenterminal → Guohua Taishan-centrale is één
  eigenaar over mijn, spoor, haven, terminal én centrale — mogelijk harder te bronnen dan deze as, maar in
  deze ronde niet onderzocht.

## 8 · Bronnen
[1] Wikipedia (EN), Datong–Qinhuangdao railway — 653 km, 422 Mt vervoerd in 2023. https://en.wikipedia.org/wiki/Datong%E2%80%93Qinhuangdao_railway
[2] Ballast Markets, Port of Qinhuangdao — coördinaat 39,9295°N/119,6436°E; kolendoorzet 2024 geschat op 180–200 Mt. https://content.ballastmarkets.com/ports/qinhuangdao/
[3] PRNewswire, "Huaneng Power International Inc. Obtains Approval on Shantou Port Haimen Terminal Zone Huaneng Coal Transit Base Project" (NDRC-goedkeuring 2012) — terminalcapaciteit 22,7 Mt/jaar. https://www.prnewswire.com/news-releases/huaneng-power-international-inc-obtains-approval-on-shantou-port-haimen-terminal-zone-huaneng-coal-transit-base-project-138916324.html
[4] Global Energy Monitor, Haimen power station — 4×1.036 MW operationeel, eenheden 5–6 in aanbouw; coördinaat 23,1899/116,6548; "Coal source(s): imported". https://www.gem.wiki/Haimen_power_station
[5] China Ports Association (chinaports.org), 2016 — terminalcapaciteit 22,7 Mt/j, waarvan 12 Mt/j voor de 6 Haimen-eenheden en 10,7 Mt voor Oost-Guangdong/Jiangxi; eigen kustschip 华能汕运1. https://www.chinaports.org/site/content/16814.html
[6] Global Energy Monitor, Shantou Port — in 2016 ging ~70 % van het via Shantou Port overgeslagen kolenvolume naar Huaneng Shantou. https://www.gem.wiki/Shantou_Port
[7] 中国上市公司协会 (capco.org.cn), 2019-08-31 — Huaneng Haimen-terminal NDRC-goedkeuring, totale investering ¥2,442 mrd. https://www.capco.org.cn/zxzx/hyxx/201908/20190831/j_2019083114184200015689628917242773.html
[8] 国务院国有资产监督管理委员会 (sasac.gov.cn) — bericht over de opening van het grootste kadeproject van Shantou (Haimen-terminal), aangelegd door CCCC Second Harbor Engineering. http://www.sasac.gov.cn/n2588025/n2588124/c4196394/content.html
[9] Chinese Wikipedia, 秦皇岛港大小码头 — 2013: het historische West Port-kolenterminal (9号码头) sloot; kolenoverslag verhuisde oostwaarts naar nieuwere terminals (context voor het verschil met de oude havendocks). https://zh.wikipedia.org/zh-hans/秦皇岛港大小码头
[10] OpenStreetMap (ODbL), way's met `name=大秦铁路` (`railway=rail`, `usage=main`) in `china-latest.osm.pbf`, 1.392 ways; via-puntcoördinaten uit de projectinterne tag-scan van de toets-ronde (2026-09-26, zie het ontwerp/toets van deze keten). https://www.openstreetmap.org
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16) — `v2/build-cache/satcheck/sat-kolen-datong-haimen-laadstation-hudong.png`, `sat-kolen-datong-haimen-qinhuangdao-kade.png`, `sat-kolen-datong-haimen-centrale.png`, `sat-kolen-datong-haimen-kade-zoom.png`.

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `kolen-datong-haimen`** → `v2/data/stroomroute-kolen-datong-haimen.json` — 8 benen, 2.960,4 km,
1.941 punten, 4 markers: spoor 53,2 km (Datong-kop → Yangyuan) · spoor 130,1 km (Yangyuan → Shacheng) ·
spoor 287,3 km (Shacheng → Zunhua-N) · spoor 170,4 km (Zunhua-N → Qinhuangdao-kade) · zee (stippel,
aanloop Qinhuangdao) 19,5 km · zee 2.257,0 km (Qinhuangdao → Haimen) · zee (stippel, aanloop Haimen)
41,8 km · leiding (stippel) 1,1 km (Haimen-terminal → Haimen-centrale).
Recept: `bak_stromen.sh` (functie `bak_kolen_datong_haimen`). Geen profiel in `maak_stroombeen_weg.py`
nodig — de keten heeft geen truck-been.

**b1 (spoor, Daqin-lijn, 4 runs):** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs`, kop→Yangyuan→
Shacheng→Zunhua-N→Qinhuangdao-kade, elk apart geroutet op het 1-op-1-net (3.260.717 spoor-edges).
Som 53,2 + 130,1 + 287,3 + 170,4 = **641,0 km** tegen de gepubliceerde 653 km = **−1,8 %**, ruim binnen
±15 % — de ingekorte 3-via-lijst uit de brief volstond, de volledige 11-vertexlijst (toets-terugval)
was niet nodig. Elk uiteinde snapt op 0,00–0,50 km van zijn via-punt; 0 omkeringen, 0 terugloop over
alle vier de legs.

**b2 (zee, kustvaart binnenlands Qinhuangdao → Haimen):** de eerste bake riep `--been "zee|…"` direct
kade→kade (39.9290,119.6440 → 23.1810,116.6595), zoals de bak_aanwijzingen voorschreven omdat beide
kades <25 km van een MARNET-zeeknoop liggen. Dat gaf een geldige route (snap 18,7/18,1 km, ruim onder
de 25 km-grens), maar `hecht_marnet.py` voegt bij zo'n snap **geen** automatische aanloopstukken toe —
de getekende zee-lijn begint/eindigt op de zeeknoop zelf, met een procesgat van 18-19 km naar de
werkelijke kade. Dat overschrijdt de naad-norm (≤5 km) fors, dus **gecorrigeerd**: twee
`maak_havenaanloop.py`-runs (timeout 300, beide binnen budget) als `--stippel-geojson` vóór/ná het
hoofdzeebeen. Qinhuangdao-kade → zeeknoop 9650 (39,8014/119,7875): **19,5 km**, 0,43 km ervan grenst
aan het kade-uiteinde (de 1:10M-kustkorrel, geen landkruising midden op de lijn). Haimen zeeknoop 5570
(23,3438/116,6470) → kade: de rechte lijn (18,1 km) loopt voor **81 % over land** — Haimen ligt op een
schiereiland — dus de geroutete aanloop is **41,8 km**, omwegfactor 2,30, ook hier 0,00 km land midden
op de lijn. Na deze correctie snapt het hoofdzeebeen op **0,000 km** aan beide zeeknopen en zijn alle
naden ≤ 0,50 km. Het hoofdzeebeen zelf (2.257,0 km) blijft **aannemelijk**: geen bron legt dit
havenpaar rechtstreeks (brief §7); ~2.300 km afgeleid was een plausibiliteitscheck, geen harde norm —
2.257,0 km ligt daar dicht tegenaan.

**b3 (leiding/band, Haimen-terminal → centrale, stippel):** geen OSM-way voor de transportband over het
eigen Huaneng-terrein — `--stippel "leiding|…"`, 1,1 km hemelsbreed, exact zoals de brief (§1: "~1 km op
satelliet gemeten") voorspelde.

**Toets-bevindingen:**
- **Geen naad > 0,5 km** over alle 8 opeenvolgende benen (na de haven-aanloop-correctie hierboven).
- **Alle 4 markers liggen ≤ 11,1 m van hun been** (Qinhuangdao/Haimen-kade/centrale exact 0,0 m; de
  onzekere Datong-kop 11,1 m — ruim binnen anker≈routeerpunt).
- `toets_knikken.py`: **1 knik ≥ 60°** (105,2°, R ≈ 5.024 m, bij 23,00000/117,00000 op het hoofdzeebeen)
  — een krappe bocht in de MARNET-zeegeometrie zelf, **0 omkeringen, 0 terugloop**. Geen reparatie nodig.
- `toets_rechte_benen.py --min-km 5`: **geen enkel been van deze stroom in de verdachtenlijst** — de
  twee haven-aanlopen zijn over water gerouteerd (omwegfactor 1,04 resp. 2,30, geen rechte kennisclaim)
  en het leiding-stippel (1,1 km) blijft onder de 5 km-drempel.
- JSON-vormtoets: `versie` 2, `punt_formaat` `lonlat`, modaliteiten {spoor, zee, leiding} (alle drie
  toegestaan), elk been ≥ 2 punten, bestand 38,1 KB (< 300 KB) — allemaal in orde.

**Gereedschapslessen:** een zeekade die *binnen* de 25 km-max-snap van `hecht_marnet.py` ligt, krijgt
géén gratis aanloopstuk — dat is anders dan de bak_aanwijzingen van deze ronde veronderstelden ("MARNET
routeert direct kade→kade met twee rechte aanloopstukken"). Een snap tot 25 km wordt zonder waarschuwing
geaccepteerd, maar laat een procesgat van diezelfde orde staan zodra de naad-toets ná de bake loopt. Bij
elke snap > ~5 km is het dus de moeite waard om alsnog `maak_havenaanloop.py` te draaien (zoals al
gedaan bij `grafiet-balama-saemangeum` op een kleinere 10-11 km-snap) — de tool geeft vaak binnen enkele
minuten een geldig kortste-pad-over-water resultaat, ook onder de 25 km-drempel. Tweede les: de
geschreven GeoJSON van `maak_havenaanloop.py --van A --naar B` bewaart de punten in de volgorde
A→B — voor een been dat *aankomt* bij een kade (zeeknoop → kade, niet kade → zeeknoop) moet die
volgorde met de hand omgedraaid worden vóórdat hij als `--stippel-geojson` in de reisvolgorde past;
zonder die omkering plakt de aanloop-lijn in de verkeerde richting aan de rest van de keten.
