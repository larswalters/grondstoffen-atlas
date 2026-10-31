# Routebrief (licht) · nikkel — Rio Tuba (Palawan) → Hachinohe-havenmond (Japan)

**stroom-id:** `nikkel-riotuba-hachinohe` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** hooggradig en middelgradig saproliet (DSO, 1,59 % Ni) uit de Rio Tuba-dagbouw (RTN, Bataraza, zuidpunt Palawan) gaat per eigen mijn- en plantweg naar de RTN-pier, per zeeschip door de Sulu Sea en de Filipijnse wateren en de Stille Oceaan naar Hachinohe (Aomori), waar PAMCO (36 % aandeelhouder van RTN) er ferronikkel van smelt; de lijn eindigt op de Hachinohe-havenmond, de PAMCO-kade is niet gelegd.
**Welke as van het verhaal:** *het Filipijnse tegenstuk van de Indonesische exportban* — ruw erts naar een Japanse smelter, en bij RTN dezelfde pier als het Coral Bay-HPAL-verhaal (`nikkel-riotuba-niihama`). Volume: **~10 kt Ni/jaar** (917.257 WMT saproliet naar Japan, PAMCO en SMM samen, 1,59 % Ni, 30 % vocht aangenomen), peiljaar 2014 [1]; PAMCO-deel niet gesplitst, huidig volume niet gevonden (indicatie). **Aannemelijk: één bron** voor de bestemming Hachinohe (verkoopcontract RTN-PAMCO t/m dec 2015 [1], bedrijfsniveau), geen bron voor pier en route.

## 1 · Ketenkaart
```
Rio Tuba-pit `ni-riotuba-mijn` ──(b1 truck-stippel · last mile, geen net op deze korrel · 1,9 km)──► weg-begin `ni-riotuba-wegbegin` (plantweg-kop)
   ──(b2 truck · plantweg via Rio Tuba-dorp · 9,2 km, letterlijke kopie)──► RTN-pier `ni-riotuba-pier`
   ──(b3 zee · haven-aanloop, stippel · 286,7 km, letterlijke kopie)──► MARNET-zeeknoop 5444 (8.4000,120.0500)
   ──(b4 zee · MARNET · 4.498,3 km, aannemelijk: één bron)──► Hachinohe-zeeknoop 5690 = havenmond `ni-hachinohe-havenmond` ⏹ stoppunt (kade PAMCO niet gelegd)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (eigen terrein) | `ni-riotuba-mijn` → `ni-riotuba-wegbegin` | mijnterrein Rio Tuba, pit → plant | hemelsbreed 1,9 km, geen wegkm | `--stippel "truck\|last mile … (geen net op deze korrel)"` | **ja** — geen net op deze korrel |
| b2 | A | truck | `ni-riotuba-wegbegin` → `ni-riotuba-pier` | plantweg → Rio Tuba-dorp (8.53, 117.43) → depotweg naar de pier | hemelsbreed 6,5 km, geen wegkm (gemeten 9,2) | **letterlijke kopie** `nikkel-riotuba-niihama-weg-plant-pier.geojson` (b1 van `nikkel-riotuba-niihama`) | nee |
| b3 | B | zee (haven-aanloop) | `ni-riotuba-pier` → zeeknoop 5444 | over water, Sulu Sea, knik 8.4700,117.5250 | 286,0 hemelsbreed, 286,7 getekend | **letterlijke kopie** `nikkel-riotuba-niihama-aanloop-riotuba.geojson` (b2 van `nikkel-riotuba-niihama`) | **ja** — MARNET reikt niet |
| b4 | B | zee | zeeknoop 5444 → zeeknoop 5690 (40.6265, 141.5863) | Sulu Sea, Visayan-zeeën, San Bernardino-straat, Stille Oceaan oostelijk van Japan (routerkeuze, geen bron) | **router 4.498,3** (gemeten, geen landkruising); hemelsbreed 4.168; geen gepubliceerde zeekm | MARNET (zeeknoop → zeeknoop) | nee — **aannemelijk: één bron** in de beennaam |

*Geen haven-aanloop bij Hachinohe en geen b5:* de PAMCO-kade is niet gelegd (zie §3), dus de lijn eindigt waar het bewijs eindigt, op zeeknoop 5690 (precedent `lithium-mtcattlin-lianyungang`). Zeeknoop 5444 komt uit `nikkel-riotuba-niihama` (gekozen boven 5431, 151 km zuidelijker en met een bocht). Geen mijnbeen vanaf een tweede plek: de pit ligt 1,9 km van de plantweg-kop.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-riotuba-mijn` | mijn / laadplek saproliet | Rio Tuba-dagbouw (RTN, Nickel Asia 60 %, PAMCO 36 %), Bataraza | 8.5740, 117.4300 | [1][2][9] | **bron-gelegd** (z15 gezien, `sat-nikkel-riotuba-hachinohe-mijn.png`: het kruis ligt op de grijs-witte mijnterrassen van de open pit, rode tailings en vijvers westelijk; de sitelaag-/Wikipedia-coördinaat 8.5700,117.4190 ligt in een vijver tussen plant en tailings en is **niet** gebruikt) |
| `ni-riotuba-wegbegin` | verbindingspunt (plantweg-kop, geen site) | begin plantweg bij de Coral Bay-plant, Rio Tuba | 8.5585, 117.4225 | **hergebruik letterlijk** `ni-coralbay-plant` uit `nikkel-riotuba-niihama.md` §3 | bron-gelegd (daar z15/z16: tank- en autoclaafbatterij) — hier alleen het begin van de gekopieerde weg |
| `ni-riotuba-pier` | overslag (RTN-pier) | RTN-pier Rio Tuba (RTN financierde de pierfaciliteiten, SMM-lening 2002) [1] | 8.5030, 117.4515 | **hergebruik letterlijk** `nikkel-riotuba-niihama.md` §3; pier in AR 2014 noot 9/15 genoemd, geen coördinaat [1] | **aannemelijk** (daar z16 gezien: pier naar het zuidoosten, twee schepen, tanks aan de wal) |
| `ni-hachinohe-havenmond` | aanlanding (routeeinde, **geen kade**) | Hachinohe-zeeknoop 5690, havenmond | 40.6265, 141.5863 | knoop uit `nikkel-taganito-niihama` (b5 eindigt er, `vertakt_van: 2`); PAMCO-adres 5-2 Toyama Shinden, Kawaragi [3] geeft geen coördinaat | **onzeker** (z14-blik `sat-nikkel-riotuba-hachinohe-hachinohe-knoop.png`: Esri heeft op open water geen beeld, het punt ligt ~5,5 km uit de kust; de kade is niet vastgesteld) |

PAMCO-kade bewust **geen anker**: `ni-hachinohe` (40.578, 141.482) uit `nikkel-taganito-niihama` ligt in zee naast de kade van Mitsubishi Paper (haalbaarheidstoets: z15 water, Nominatim reverse); Photon, Nominatim en Overpass vinden het PAMCO-perceel niet. Sitelaag-fout `w-coralbay-riotuba` (1,4 km van de plant) en mijnpunt: zie §7.

## 4 · Via-punten
Geen. b2 is een kopie van een 9,2 km-weg zonder corridorkeuze (onder het 3–8 via-punten-criterium), b1 een stippel, b3/b4 zee (router of kopie).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Rio Tuba-mijn (beneficiatie, in-pit crusher sinds jul 2014) | RTN (Nickel Asia 60 %, PAMCO 36 %, Sojitz 4 %) | erts → hoog- en middelgradig saproliet (1,59 % Ni) | 2.190.463 WMT saproliet gemijnd 2014; 917.257 WMT naar Japan | [1] |
| PAMCO Hachinohe Works (Kawaragi) | Pacific Metals Co. | saproliet → ferronikkel (granulaat, 20 kg-ingot) | niet gepubliceerd (open punt) | [3][4] |

## 6 · Stoppunt
De brief stopt op de Hachinohe-havenmond: PAMCO Hachinohe is zelf de ferronikkelfabriek en de kade is niet gelegd; er is geen gedocumenteerde afnemer van het ferronikkel in deze bronnen, dus geen fase E.

## 7 · Open punten
- **Alleen peiljaar 2014:** koopcontract RTN-PAMCO liep tot dec 2015 [1]; huidig volume niet gevonden (Nickel Asia FY2025 noemt alleen Japan en China). 917.257 WMT is PAMCO + SMM samen (308.529 hoog + 608.728 midden) [1]; het PAMCO-deel staat niet apart. De stroom kan nu kleiner of verlegd zijn.
- **PAMCO-kade en -perceel niet gelegd** (Kawaragi, 5-2 Toyama Shinden) [3]; `ni-hachinohe` uit `nikkel-taganito-niihama` staat in zee. Lijn en marker eindigen op zeeknoop 5690.
- **b1 en b2 zijn aannemelijk, niet gebrond:** de haulroute pit → pier is niet gedocumenteerd; de plantweg (kopie, 9,2 km, geen wegkm) is de gemeten weg van de Coral Bay-plant naar de pier, hier als best beschikbare weg voor het saproliet; pit → plantweg-kop is stippel.
- **Mijnanker-sitelaag:** `w-coralbay-riotuba` (8.5700,117.4190) ligt in een vijver; de terrassenpit ligt op 8.5740,117.4300 (1,9 km van de plant) — centraal gelijk te trekken, door mij niet gewijzigd.
- **Router-keuze:** MARNET gaat door de Visayan-zeeën en San Bernardino, niet door de Luzon-straat; geen bron voor de gevaren route. 4.498,3 km is router-uitkomst.
- **Overlap voor de centrale toets:** ~77 % van de 4.498 km valt binnen 15 km op `nikkel-taganito-niihama` (b5, Taganito → Hachinohe); ~1.000 km Visayan-deel en de hele oorsprong Rio Tuba zijn nieuw. b2 en b3 zijn letterlijke kopieën van `nikkel-riotuba-niihama`.
- **Aanloop Hachinohe niet gekopieerd:** de aanloop van `nikkel-taganito-niihama` (10,3 km, naar het onzekere `ni-hachinohe`) is bewust weggelaten.

## 8 · Bronnen
[1] Nickel Asia Corporation, Annual Report 2014 (pdf, lokaal gelezen): RTN verkocht 917.257 WMT saproliet naar Japan, 1,59 % Ni (308.529 hoog + 608.728 midden, PAMCO en SMM); noot 31: RTN levert saproliet aan PAMCO t/m dec 2015, PAMCO 36 %; noot 9/15: RTN-pierfaciliteiten. https://nickelasia.com/assets/documents/Annual-Report-2014.pdf
[2] Nickel Asia, Rio Tuba Nickel Mining Corp: Barangay Rio Tuba, zuidpunt Palawan. https://nickelasia.com/subsidiaries/rio-tuba-nickel-mining-corporation
[3] Pacific Metals Co., Overview: Hachinohe Head Office (Manufacturing Works), 5-2 Toyama Shinden, Kawaragi, Hachinohe; producten ferronikkel. https://www.pacific-metals.co.jp/en/corporate/outline.html
[4] Pacific Metals Co., groepspagina: RTN en TMC als joint ventures die de grondstof voor PAMCO's ferronikkel leveren. https://www.pacific-metals.co.jp/en/corporate/group.html
[5] 大平洋金属, Japanse Wikipedia: ferronikkelfabrikant, Hachinohe-fabriek in Kawaragi (青森県八戸市河原木). https://ja.wikipedia.org/wiki/%E5%A4%A7%E5%B9%B3%E6%B4%8B%E9%87%91%E5%B1%9E
[6] `routebrieven/nikkel-riotuba-niihama.md` §2/§3: plantweg 9,2 km, aanloop 286,7 km, zeeknoop 5444, RTN-pier (z16), RTN-pier SMM-persbericht. Extract filipijnen.
[7] `routebrieven/nikkel-taganito-niihama.md` §2/§3/§7: Hachinohe-zeeknoop 5690 (b5 → 40.6265,141.5863), PAMCO-anker onzeker.
[8] `routebrieven/lithium-mtcattlin-lianyungang.md`: precedent einde op zeeknoop zonder kade.
[9] Esri World Imagery z15/z14 (sat_check): `v2/build-cache/satcheck/sat-nikkel-riotuba-hachinohe-mijn.png`, `…-hachinohe-knoop.png`; haalbaarheidstoets (Hachinohe-anker in zee, MARNET 5444 → 5690 = 4.498,3 km); sitelaag `nikkel-sitelaag.json`; Wikipedia Rio Tuba mine (8.570 N, 117.419 E).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Recept:** functie `bak_nikkel_riotuba_hachinohe` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh nikkel-riotuba-hachinohe`); geen profiel, geen wegscan, geen havenaanloop-tool (b2 en b3 zijn letterlijke kopieen). Uitvoer `v2/data/stroomroute-nikkel-riotuba-hachinohe.json` (12,9 KB, versie 2, lonlat).

| # | modaliteit | km | punten | naad | geometrie |
|---|---|---|---|---|---|
| b1 | truck, stippel | 1,9 | 2 | 0 | last mile pit naar plantweg-kop, geen net op deze korrel |
| b2 | truck | 9,2 | 129 | 0 | letterlijke kopie `nikkel-riotuba-niihama-weg-plant-pier.geojson` (brief 9,2 gemeten: 0 %) |
| b3 | zee, stippel | 286,7 | 29 | 0 | letterlijke kopie `nikkel-riotuba-niihama-aanloop-riotuba.geojson` (MARNET reikt niet) |
| b4 | zee | 4.498,3 | 467 | 0 | MARNET zeeknoop 5444 naar 5690, snap 0,000 km beide kanten, 33 edges, 0 track |

Totaal **4.796,1 km**, 627 punten, 3 markers (pit 8.5740,117.4300; RTN-pier 8.5030,117.4515; Hachinohe-havenmond 40.6265,141.5863), alle op 0,0 km van de lijn. Naden 0 km.

**Toelichting.** b1: stippel omdat de haulroute pit naar plantweg niet gedocumenteerd is en er op deze korrel geen net ligt; hemelsbreed 1,9 km, geen wegkm. b3: stippel omdat MARNET bij de pier niet reikt (handgemaakt met een knik op 8.4700,117.5250 over open water, overgenomen). Geen aanloop Hachinohe: kade niet gelegd, lijn eindigt waar het bewijs eindigt. Geen vlucht, geen leiding.

**Toetsen.** toets_knikken: zee 1 krappe bocht (73,7 gr bij 9.0120,123.3283, Visayan-overgang, router); truck 5 knikken, allemaal uit de gekopieerde plantweg (1 echte scherpe bocht, 4 spikes van 11 tot 43 m). toets_rechte_benen: alleen b3 is recht (stippel met reden). json.load ok, modaliteiten {zee, truck}.

**Lessen / bevindingen.** (1) Twee van de vier benen zijn kopieen: bakken kostte een minuut zonder wegscan. (2) Sitelaag `w-coralbay-riotuba` ligt in een vijver (1,4 km van de plant), niet gewijzigd. (3) Overlap: ca 77 % van de zeekm valt binnen 15 km op `nikkel-taganito-niihama` b5. (4) Registratie en bundel centraal.
