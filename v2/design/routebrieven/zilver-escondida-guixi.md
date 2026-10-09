# Zilver · Escondida → Coloso → Beilun → Guixi (Chili → China)

**stroom-id:** `zilver-escondida-guixi` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** zilver in het kopersulfide-concentraat van Escondida (BHP, Atacama), per eigen **slurryleiding**
(~170 km) naar Puerto Coloso, daar gefilterd en per **bulkcarrier** (Stille Oceaan, rechtstreeks, geen hub) naar de
Beilun-ertsterminal (Ningbo-Zhoushan), over de band naar het laadspoor van 北仑港站 en per **spoor** (Yongjin-lijn,
corridor B) naar de Jiangxi Copper-smelter in Guixi, waar het zilver in de anodeslijk/edelmetaalafdeling terechtkomt
(**aannemelijk: één bron** — zie §7). Geometrie = letterlijke kopie van benen 1–10 van `koper-escondida-guixi`.
**Welke as van het verhaal:** Chileens koperconcentraat met zilver naar de grootste zilverproducent van China.
Volume: Escondida **4.952 koz payable Ag in concentraat in 9 mnd tot 31-03-2025 = ca. 154 t Ag (100%-basis; jaargemiddeld
ca. 200 t Ag/j)** [1]; aandeel naar Guixi niet gepubliceerd. Jiangxi Copper groep: 1.383,18 t Ag in 2025 [3], 749,78 t in H1 2026 [4].

## 1 · Ketenkaart
```
Escondida-concentrator `ag-escondida-conc`
  ──(b1–b4 leiding · slurry 9", eigen leiding · ~170 km gepubliceerd; 137,8 km doorgetrokken OSM, 22,8 km stippel)──►
  Puerto Coloso, filterfabriek → laadsteiger `ag-coloso-steiger`
  ──(b5 haven-aanloop 87,8 stip · b6 zee 19.018 · b7 haven-aanloop Beilun 1,3 stip, aannemelijk: één bron)──►
  Beilun-ertsterminal, losberth `ag-beilun-kade`
  ──(b8–b9 band + ertsveld, eigen terrein, 1,5 stip)──► 北仑港站 laadspoor `ag-beilun-laadspoor`
  ──(b10 spoor · Yongjin-vrachtlijn, corridor B · 565,8 gebakken)──► Jiangxi Copper, Guixi `ag-guixi-smelter`  ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | concentrator → pijpenrekken-uitgang (mijnterrein) | slurryleiding Escondida | 4,8 | stippel, kopie koper b1 | ja: terrein, pijpenrekken niet te volgen |
| b2 | A | leiding | uitgang mijnterrein → La Negra | slurryleiding, OSM ways 1530915728 + 1530915724 | 137,8 [8] | `leidingbeen-escondida-coloso.geojson` (kopie b2) | nee |
| b3 | A | leiding | La Negra → Coloso filterfabriek | slurryleiding, ingegraven + twee tunnels | 17,7 | stippel, kopie b3 | ja: geen OSM-way |
| b4 | A | leiding | filterfabriek → laadsteiger | terminalverwerking Coloso | 0,3 | stippel, kopie b4 | ja: terrein |
| b5 | B | zee | laadsteiger → MARNET-zeeknoop 4664 (-23.8,-71.3) | haven-aanloop Coloso | 87,8 | `aanloop-coloso.geojson` (kopie b5) | ja: MARNET reikt niet |
| b6 | B | zee | Coloso → Beilun | Stille Oceaan, rechtstreeks (geen hub) | 19.018,4 [Z1] | MARNET (kopie b6) | nee |
| b7 | B | zee | zeeknoop 5849 → losberth | haven-aanloop Beilun | 1,3 | stippel, kopie b7 | ja: knoop in de geul |
| b8 | C | leiding | losberth → ertsveld | transportband, eigen terrein | 1,2 | stippel, kopie b8 | ja: terrein |
| b9 | C | leiding | ertsveld → laadspoor | ertsveld → 北仑港站 | 0,3 | stippel, kopie b9 | ja: terrein |
| b10 | C | spoor | 北仑港站 → Guixi | Yongjin, Ningbo–Jinhua–Quzhou–Yushan–Guixi | 565,8 gebakken (corridor ~556, +1,8%) [8] | `spoorroute-nieuw-beilun-guixi.geojson` (kopie b10) | nee |
Totaal **19.835,4 km**, 10 benen. Geen been 11 (kathode → walsdraad): zilver verlaat Guixi niet als kathode (§6).

## 3 · Ankers (één per site en per overslag; allen hergebruikt uit `koper-escondida-guixi`)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-escondida-conc` | mijn/concentrator (kop b1) | Escondida-concentrator en indikkers (BHP) | -24.2620, -69.0600 | [8][sat] | bron-gelegd (z15 gezien: maalhal, vier ronde indikkers en bekkens direct naast de open pit; hergebruik koper `cu-escondida-laad`) |
| `ag-coloso-steiger` | overslag leiding → zee | Puerto Coloso, laadsteiger (filterfabriek op -23.7590, -70.4670) | -23.7569, -70.4652 | [8][sat] | bron-gelegd (z15 gezien: filterfabriek op de kustlandtong, pier met afgemeerd schip; hergebruik koper `cu-coloso-kade`) |
| `ag-beilun-kade` | overslag zee → band | Beilun-ertsterminal, losberth, Ningbo-Zhoushan | 29.9364, 121.8830 | [8][sat] | bron-gelegd (z15 gezien: ertssteiger met twee Capesize-bulkers; hergebruik `cu-beilun-kade`) |
| `ag-beilun-laadspoor` | overslag band → spoor | 北仑港站, laadspoor Beilun | 29.92653, 121.87308 | [8][sat] | aannemelijk (z15 gezien: **containeremplacement**, geen bulk; conflict §7; hergebruik `cu-beilun-laadspoor`) |
| `ag-guixi-smelter` | afnemer / losplek | Jiangxi Copper, Guixi-smelter (贵溪冶炼厂), ertslosbundel | 28.3271, 117.2260 | [5][8][sat] | aannemelijk: één bron (z15 gezien: smeltercomplex met spoorbundel; registerpunt 28.33227, 117.22545 ligt 0,6 km noordelijker; hergebruik `cu-guixi-spoor`) |

## 4 · Via-punten
Geen nieuwe: alle benen zijn letterlijke kopieën van gebakken geometrie (spoor: één run Beilun → Guixi, corridor B,
zonder via; leiding: OSM-ways 1530915728/1530915724). Er is geen wegbeen.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Escondida-concentrator + Coloso-filterfabriek | BHP (57,5%, operator) en partners | sulfide-Cu-concentraat met payable Ag → gefilterd concentraat | Ag 4.952 koz/9 mnd (100%-basis) | [1] |
| Guixi-smelter | Jiangxi Copper | concentraat (o.a. Escondida) → kathode + anodeslijk (goud/zilver) | 1,10 mln t Cu/j; Jiangxi-groep 1.383 t Ag in 2025 | [3][5][8] |

## 6 · Stoppunt
Stopt bij de Guixi-smelter: de bron voor Escondida-concentraat noemt de smelter, niet de edelmetaalraffinage; zilver
verlaat Guixi als edelmetaalproduct (geen gedocumenteerde volgende locatie) en niet als kathode, dus fase D/E vervallen
en been 11 van de koperbrief (kathode → walsdraad) wordt bewust niet gekopieerd.

## 7 · Open punten
- **Eén bron voor de koppeling Escondida → Jiangxi:** Miningmx 4-1-2012: Jiangxi ontving in 2012 **20.000–30.000 t Escondida-concentraat**
  (naast ca. 100.000 t van Freeport) [2]. Geen actuele bron; daarom **aannemelijk: één bron** in beennamen en titel.
- **Aandeel zilver naar Guixi niet gepubliceerd.** 154 t Ag/9 mnd is de hele Escondida-mijn (100%, niet BHP-aandeel, geen
  aandeel Jiangxi) [1]; de v1-raming 1.050 t Ag/j (ag-chile-cu, `data/silver.js`) is niet overgenomen (niet geverifieerd).
- **Jiangxi-zilver is groepsbreed** (1.383,18 t in 2025 [3]), niet alleen Guixi; of Guixi's edelmetaalafdeling zilverelektrolyse
  doet staat in [6] op bedrijfsniveau ("电解金和银"), niet voor de smelter apart. Het 2024-plan (1.286 t) is niet teruggevonden:
  het HKEX-PDF was niet leesbaar.
- **Container of bulk bij Beilun?** Het satelliet-gelegde laadspoor 北仑港站 is een containeremplacement (open conflict van de
  koperbrief); Escondida-concentraat kan per container of bulk doorgaan, geen bron beslist; de spoorgeometrie is dezelfde.
- Haven-aanloop Beilun is 1,3 km (<5 km): zou niet verplicht zijn, maar blijft als letterlijke kopie.
- Sitelaag `w-escondida-ag` staat op -24.27, -69.07 (1,4 km van `ag-escondida-conc`) en draagt 1.050 t Ag/j als indicatie:
  centraal gelijktrekken (anker) en het volume herzien (BHP-cijfer 154 t/9 mnd); Guixi ontbreekt in de zilver-sitelaag.

## 8 · Bronnen
[1] BHP Operational Review Q3 FY2025 (SEC 6-K, 4.952 koz payable silver in concentrate YTD tot 31-03-2025, 100%-basis):
https://www.sec.gov/Archives/edgar/data/811809/000119312525083414/d886015d6k.htm
[2] Miningmx, "Smelters, BHP settle 2012 copper charges", 4-1-2012 (Jiangxi 20–30 kt Escondida-concentraat):
https://www.miningmx.com/news/base-metals/26084-smelters-bhp-settle-2012-copper-charges
[3] Securities Times (stcn), Jiangxi Copper jaarverslag 2025, gepubliceerd 26-3-2026 (1.383,18 t Ag, 118,93 t Au): https://stcn.com/article/detail/3702266.html
[4] 10jqka, Jiangxi Copper H1 2026 (749,78 t Ag, 43,73 t Au): https://stock.10jqka.com.cn/20260826/c679302461.shtml
[5] Wikipedia, Jiangxi Copper (Guixi-smelter >1 Mt/j; zilver in productenlijst): https://en.wikipedia.org/wiki/Jiangxi_Copper
[6] zh.wikipedia, 江西铜业 (电解金和银): https://zh.wikipedia.org/wiki/江西铜业
[7] HKEX, Jiangxi Copper resultaten 2024 (niet leesbaar, niet gebruikt): https://www.hkexnews.hk/listedco/listconews/sehk/2025/0327/2025032702751_c.pdf
[8] Routebrief `v2/design/routebrieven/koper-escondida-guixi.md` (ankers, benen 1–10, OSM-ways, 565,8 km spoor; bronnen E1–E3, Z1, C1–C8, J1–J3)
 en `v2/data/stroomroute-koper-escondida-guixi.json` (geometrie, letterlijk gekopieerd).
[sat] Esri World Imagery via `v2/tools/sat_check.py`, z15, 2026-10-09: `v2/build-cache/satcheck/sat-zilver-escondida-guixi-*.png`.
[Z1] atlas-invariant Antofagasta → Shanghai 18.915 km (M23), zie [8].

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Recept:** `bash v2/tools/bak_stromen.sh zilver-escondida-guixi` (functie `bak_zilver_escondida_guixi`, vóór de dispatch, LF) → `v2/data/stroomroute-zilver-escondida-guixi.json`
(66,2 KB, versie 2, punt_formaat lonlat, 10 benen, 5 markers, 3.437 punten, **19.835,4 km**). Geen wegbeen, profiel, extract, vlucht of nieuwe tool; register en bundel zijn centraal (niet geraakt).
Letterlijke kopie van benen 1-10 van `koper-escondida-guixi` (alle 10 benen coördinaat voor coördinaat gelijk, gecontroleerd), zonder been 11 en zonder walsdraad-marker.

| # | modaliteit | km | stippel | toelichting |
|---|---|---|---|---|
| b1 | leiding | 4,8 | ja | terrein Escondida, pijpenrekken niet te volgen |
| b2 | leiding | 137,8 | nee | OSM-slurryleiding (ways 1530915728/1530915724), geojson-kopie |
| b3 | leiding | 17,7 | ja | La Negra → Coloso, geen OSM-way (ingegraven + tunnels) |
| b4 | leiding | 0,3 | ja | terrein Coloso, filterfabriek → laadsteiger |
| b5 | zee | 87,8 | ja | haven-aanloop Coloso: MARNET reikt niet tot knoop 4664 (-23.8,-71.3) |
| b6 | zee | 19.018,4 | nee | MARNET Coloso → Beilun, rechtstreeks, geen hub |
| b7 | zee | 1,3 | ja | haven-aanloop Beilun: knoop in de geul (kopie, < 5 km) |
| b8 | leiding | 1,2 | ja | transportband eigen terrein |
| b9 | leiding | 0,3 | ja | ertsveld → laadspoor, eigen terrein |
| b10 | spoor | 565,8 | nee | Yongjin corridor B, kopie spoorroute-nieuw-beilun-guixi (corridor ~556, +1,8%) |

**Toets (handleiding §5):** naden 0,00 km behalve 0,20 km laadspoor → spoorbeen (anker ≠ routeerpunt); markers 0,00-0,05 km van hun lijn (Guixi 0,05); km gelijk aan de brief;
geen gemeten been met omwegfactor 1,000 (alleen stippels); `toets_knikken.py`: 5 knikken ≥ 60 gr (4 op b6 Ningbo-benadering, 1 echte keerlus 28.3429,117.1975 op b10 bij Guixi), 0 terugloop, geheel geërfd van de koperstroom.
**Open/bevindingen:** zie §7 (één bron Escondida → Jiangxi, container of bulk bij Beilun, sitelaag `w-escondida-ag` 1,4 km van het anker en Guixi ontbreekt in de zilver-sitelaag: centraal).
**Les:** een stroom met dezelfde keten als een bestaande koperstroom is een kopie van de been-regels en geojson-bestanden; alleen namen, markers en stroom-id verschillen.
