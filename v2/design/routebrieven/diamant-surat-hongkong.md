# Routebrief (licht) · diamant — Surat → Mumbai → Hong Kong (land)

**stroom-id:** `diamant-surat-hongkong` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** gepolijste diamant van de Surat Diamond Bourse (GJEPC-omgeving, Gujarat) gaat per truck via de NH48 naar de Bharat Diamond Bourse (Bandra-Kurla Complex, Mumbai), verder naar het CSMIA-vrachtcomplex (Sahar), vliegt als vrachtvlucht (grootcirkel) naar de vrachtterminal van Hong Kong International Airport, en gaat per truck naar het Hong Kong Diamond Exchange Building in Central — de gepolijste as naar de Aziatische eindmarkt.
**Welke as van het verhaal:** *Surat → Mumbai → Hong Kong: de gepolijste as naar de Aziatische eindmarkt* — ~8 Mct/j gepolijst (India → China/Hongkong-markt), mode air [design/diamant.md §4d]. Risico: de Hongkongse/Chinese vraag is teruggevallen sinds ~2022 (vastgoed-/vertrouwenscrisis), wat dit been kwetsbaarder maakt dan de VS-as (`diamant-mumbai-newyork.md`, deze golf).

## 1 · Ketenkaart
```
Surat Diamond Bourse `dia-surat-bourse` ──(b1 truck · NH48 Surat–Mumbai · ~280 km gepubliceerd)──►
Bharat Diamond Bourse (BKC) `dia-bdb` ──(b2 truck · Airport Road/BKC-connector · ~3,9 km hemelsbreed)──►
CSMIA Air Cargo Complex (BOM), Sahar `dia-bom-cargo` ──(b3 lucht · vlucht BOM → HKG, grootcirkel · ~4.273 km)──►
Cathay Pacific Cargo Terminal (HKG) `dia-hkg-cargo` ──(b4 truck · North Lantau Hwy → Tsing Ma Bridge → Kwai Chung → Western Harbour Crossing · ~24 km hemelsbreed)──►
Hong Kong Diamond Exchange Building, Central `dia-hk-exchange` ── stoppunt
```
`dia-bdb` en `dia-bom-cargo` zijn de bestaande Mumbai-ankers uit `diamant-mirny-mumbai.md` (deze golf) — hergebruikt, niet opnieuw gelegd.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Surat Diamond Bourse → Bharat Diamond Bourse (BKC) | NH48 Surat–Mumbai, via Navsari/Vapi/Boisar/Vasai-Virar/Dahisar | ~280 [ontwerp]; via-punten-som 235,6 / hemelsbreed 227,6 (berekend) | maak_stroombeen_weg | nee |
| b2 | B | truck | Bharat Diamond Bourse (BKC) → CSMIA Air Cargo Complex (BOM), Sahar | Airport Road / Western Express Highway-connector, binnen Mumbai (<15 km, geen corridorkeuze) | ~10 [ontwerp]; hemelsbreed 3,9 (berekend, zelfde been als `diamant-mirny-mumbai.md` b4, omgekeerde richting) | maak_stroombeen_weg | nee |
| b3 | B | lucht | CSMIA Air Cargo Complex (BOM) → Cathay Pacific Cargo Terminal (HKG) | vlucht BOM → HKG, grootcirkel | 4.272,8 (berekend, grootcirkel); ontwerp ~4.350 | maak_luchtbeen | nee — doorgetrokken |
| b4 | C | truck | Cathay Pacific Cargo Terminal (HKG) → Hong Kong Diamond Exchange Building | North Lantau Highway → Tsing Ma Bridge → Kwai Chung Interchange → Western Harbour Crossing → Central | via-punten-som 32,4 / hemelsbreed 24,0 (berekend) | maak_stroombeen_weg | nee |

Fase C is toegevoegd op de haalbaarheidstoets: het ontwerp eindigde op de luchthaven zelf; er ontbrak het laatste been naar een concreet Hongkong-anker. Gekozen: het **Hong Kong Diamond Exchange Building** (20 Ice House Street, Central) — een echt diamanthandelsgebouw, geen marktcentroïde en geen gouden/zilveren beurs (Chinese Gold & Silver Exchange Society is voor edelmetaal, niet diamant).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-surat-bourse` | beursgebouw / vertrekpunt (slijperij-omgeving) | Surat Diamond Bourse, DREAM City, Surat, Gujarat | 21.1099, 72.7954 | [1][6] | bron-gelegd (z15 gezien: fors, geïsoleerd gebouwencomplex met eigen wegenstelsel en parkeerterrein in het DREAM City-industriegebied, 5 km NW van het centrum van Surat; wereldwijd grootste kantoorgebouw, GJEPC-omgeving — de individuele slijp-/polijstwerkplaatsen liggen verspreid over Surat en zijn niet op één punt te leggen, zie §7) |
| `dia-bdb` | beursgebouw / doorvoerpunt | Bharat Diamond Bourse, G Block, Bandra-Kurla Complex, Mumbai | 19.0641, 72.8646 | [2][7] (hergebruikt uit `diamant-mirny-mumbai.md`, deze golf) | bron-gelegd (hergebruikt anker, deze golf al satelliet-gelegd) |
| `dia-bom-cargo` | vrachtterminal / vertrek luchtvracht | CSMIA Air Cargo Complex, Sahar, Mumbai | 19.0994, 72.8673 | [3][7] (hergebruikt uit `diamant-mirny-mumbai.md`, deze golf) | bron-gelegd (hergebruikt anker, deze golf al satelliet-gelegd) |
| `dia-hkg-cargo` | vrachtterminal / aankomst luchtvracht | Cathay Pacific Cargo Terminal, Chek Lap Kok, Hong Kong | 22.2975, 113.9247 | [4][8] | bron-gelegd (z15 gezien: apart vrachtgebouwencomplex met loodsen direct aan het platform, meerdere wide-body vrachttoestellen op het apron ernaast, OSM `building`+`amenity=post_depot` "國泰航空貨運站 Cathay Pacific Cargo Terminal") |
| `dia-hk-exchange` | beurs-/handelsgebouw / eindpunt | Hong Kong Diamond Exchange Building, 20 Ice House Street, Central | 22.2797, 114.1570 | [5][9] | bron-gelegd (z16 gezien: dicht stedelijk bouwblok in Central, direct ten zuiden van het havenfront/IFC — typisch voor een handelsdistrict, geen eigen terrein te onderscheiden; OSM-landuse "香港鑽石會大廈 Hong Kong Diamond Exchange Building") |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Navsari | 20.9500, 72.9300 | eerste grotere stad op de NH48 zuidwaarts vanaf Surat (Wikipedia-coördinaat) |
| b1 | 2 | Vapi | 20.3720, 72.9170 | industriestad op de NH48, corridor blijft de doorgaande hoofdweg volgen (Wikipedia-coördinaat) |
| b1 | 3 | Boisar | 19.8036, 72.7560 | corridor buigt hier de Konkankust op richting Mumbai (Wikipedia-coördinaat) |
| b1 | 4 | Vasai-Virar | 19.4700, 72.8000 | laatste grote knoop vóór de Mumbai-stadsgrens, corridor wordt hier Western Express Highway (Wikipedia-coördinaat) |
| b1 | 5 | Dahisar (Mumbai-stadsgrens/toll naka) | 19.2501, 72.8593 | vaste incheckpost waar de NH48 de stad Mumbai binnenkomt (Wikipedia-coördinaat) |
| b4 | 1 | North Lantau Highway | 22.3143, 113.9924 | enige doorgaande snelweg van de luchthaven af richting Tsing Ma Bridge (Wikipedia-coördinaat) |
| b4 | 2 | Tsing Ma Bridge | 22.3514, 114.0742 | vaste brugcorridor tussen Lantau en Kowloon/New Territories, geen alternatieve oeververbinding voor dit vrachtverkeer (Wikipedia-coördinaat) |
| b4 | 3 | Kwai Chung Interchange | 22.3667, 114.1250 | knoop waar de corridor van Route 3 naar de Kowloon-kant buigt (Wikipedia-coördinaat) |
| b4 | 4 | Western Harbour Crossing (HK-portaal) | 22.3014, 114.1567 | enige zinnige tunnelcorridor van Kowloon naar Hong Kong Island richting Central (Wikipedia-coördinaat) |

b2 heeft geen via-punten: een stadsverbinding <4 km binnen Mumbai zonder aanwijsbare corridorkeuze (zelfde been als b4 in `diamant-mirny-mumbai.md`).

## 5 · Verwerkingsknopen
*(geen — deze keten kent geen smelter/raffinaderij. Het slijpen/polijsten gebeurt vóór deze keten in en rond Surat (~90-95% van de wereld); de Surat Diamond Bourse en Bharat Diamond Bourse zijn beurs-/exportgebouwen, het Hong Kong Diamond Exchange Building is een handelsgebouw — geen van drie is een bewerkingslocatie.)*

## 6 · Stoppunt
De brief stopt bij het Hong Kong Diamond Exchange Building: dat is het concrete Hongkong-anker dat de haalbaarheidstoets vroeg (fase C), en geen bron koppelt déze specifieke stroom aan een vervolgbestemming (bv. een individuele juwelier of fabriek in de sieradenwijk) — fase D vervalt.

## 7 · Open punten
- **Geen apart slijperij-/polijstgebouw gevonden voor Surat**: het anker `dia-surat-bourse` is het bourse-/exportgebouw (GJEPC-omgeving, DREAM City); de duizenden individuele slijp-/polijstwerkplaatsen liggen verspreid over Surat (o.a. Varachha, Katargam, Mahidharpura) en zijn niet op één site-anker te leggen — dit is een bewuste rolverdeling (beurs = vertrekpunt van de gepolijste as), geen weggelaten stap.
- **Hongkong-dekking in de Geofabrik china-extract niet bevestigd binnen het webbudget** (bevestigd open punt uit het ontwerp/de haalbaarheidstoets) — te controleren bij het bakken met een pyosmium-scan; is er geen dekking, dan is dat centraal werk (nieuwe extract), geen agent-actie.
- **b1-lengte (~280 km NH48) is niet exact herleidbaar** uit de via-punten-som (235,6 km) — de gepubliceerde ~280 km omvat waarschijnlijk stadsdoorsteken in Surat en Mumbai die de rechte via-puntenketen niet meeneemt; bij het bakken beslist de gemeten wegroute.
- **Geen gepubliceerde vluchtlengte gevonden voor BOM→HKG**: berekende grootcirkel (4.272,8 km); geen bron noemt een tussenlanding voor déze stroom → één directe vlucht aangenomen, zoals de bakhandleiding voorschrijft.
- **Aandeel van déze specifieke as (Mumbai→Hongkong) binnen het totale ~8 Mct/j India→China/Hongkong-volume niet apart gebrond** — het cijfer uit `design/diamant.md` §4d is de totale as, niet cargo- of terminalspecifiek (bevestigd risico uit het ontwerp).
- **Exact pand binnen het Hong Kong Diamond Exchange Building niet verder onderscheiden** (geen individuele handelaar/koerier gebrond) — het gebouw zelf is wel een erkend, specifiek diamanthandelsgebouw (niet de Chinese Gold & Silver Exchange Society, die edelmetaal verhandelt).

## 8 · Bronnen
[1] Wikipedia — "Surat Diamond Bourse" (SDB, DREAM City, Surat; wereldwijd grootste kantoorgebouw, 660.000 m²; 21.10972/72.79528). https://en.wikipedia.org/wiki/Surat_Diamond_Bourse
[2] Wikipedia — "Bharat Diamond Bourse" (BDB, G Block, Bandra-Kurla Complex, Mumbai; 98% van de Indiase diamantexport). https://en.wikipedia.org/wiki/Bharat_Diamond_Bourse
[3] OpenStreetMap/Photon (ODbL) — "C.S.I. Airport Cargo Complex Parking", Sahar Village, Mumbai (19.0994/72.8672). https://www.openstreetmap.org
[4] OpenStreetMap/Photon (ODbL) — "國泰航空貨運站 Cathay Pacific Cargo Terminal", Chun Wan Road, Chek Lap Kok, Hong Kong (building + post_depot, 22.2975/113.9247). https://www.openstreetmap.org
[5] OpenStreetMap/Photon (ODbL) — "香港鑽石會大廈 Hong Kong Diamond Exchange Building", Ice House Street, Central and Western District, Hong Kong (22.2797/114.1570). https://www.openstreetmap.org
[6] OpenStreetMap/Photon (ODbL) — "Surat Diamond Bourse", Majura Taluka, Gujarat (landuse commercial, 21.1099/72.7951; office-node 21.1096/72.7954). https://www.openstreetmap.org
[7] `diamant-mirny-mumbai.md` (deze golf, M31 golf 3) — hergebruikte ankers `dia-bdb` (19.0641/72.8646) en `dia-bom-cargo` (19.0994/72.8673), beide al satelliet-gelegd.
[8] Wikipedia — "Hong Kong International Airport" (HKG, Chek Lap Kok, Islands District). https://en.wikipedia.org/wiki/Hong_Kong_International_Airport
[9] Wikipedia — coördinaten via de MediaWiki-API (prop=coordinates) voor "Tsing Ma Bridge" (22.35139/114.07417), "North Lantau Highway" (22.3143/113.9924), "Western Harbour Crossing" (22.30139/114.15667), "Kwai Chung" (22.36667/114.125), en voor de India-corridor "Navsari" (20.95/72.93), "Vapi" (20.372/72.917), "Boisar" (19.8036/72.756), "Vasai-Virar" (19.47/72.80), "Dahisar" (19.250069/72.859347). https://en.wikipedia.org/w/api.php
[10] GJEPC (Gem & Jewellery Export Promotion Council, India), officiële site — achtergrondbron voor de Surat-slijp-/exportindustrie. https://www.gjepc.org
[11] Kimberley Process Certification Scheme, officiële site — achtergrondbron voor ruw-/gepolijst-handelsstatistiek. https://www.kimberleyprocess.com
[12] `v2/design/diamant.md` §4d (project-brief, intern) — "India → China/Hongkong", 8 Mct/jr, mode air; jaarvolume-bron voor deze as.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `diamant-surat-hongkong`** → `v2/data/stroomroute-diamant-surat-hongkong.json` — 5 benen (1 stippel + 3
truck + 1 lucht), **4.601,8 km**, 5.295 punten, 5 markers, 105,5 KB. Recept: `bak_stromen.sh` (functie
`bak_diamant_surat_hongkong`); twee nieuwe wegprofielen (`diamant-surat-hongkong-surat-bdb`,
`diamant-surat-hongkong-hkgcargo-hkexchange`) in `maak_stroombeen_weg.py`; één luchtbeen met
`maak_luchtbeen.py`; b2 is een gespiegelde kopie van bestaande geometrie (geen scan).

**b1a (truck, stippel, 0,3 km):** `DREAM City interne toegangsweg → NH48-aansluiting`. DREAM City (Surat Diamond
Bourse) heeft in OSM een **eigen, geïsoleerd wegenstelsel** — gemeten met een BFS op de india-scan: het
component vanaf het ankerpunt telt 57 knopen tegen 1.780.308 vanaf Navsari, en het dichtstbijzijnde punt op het
publieke net ligt 17 m van dat interne component (0,33 km hemelsbreed vanaf het anker). Dit is een echt
OSM-topologiegat, geen access-filter — `eindToegangPrivaat` loste het daarom niet op (eerste poging faalde met
"geen wegpad tussen punt 0 en 1"). Korte stippel anker → routeerpunt (bakhandleiding §2, "korter dan ~2 km"),
gemeten 0,325 km.

**b1b (truck, nieuw profiel `diamant-surat-hongkong-surat-bdb`, extract `india`, vensterKm 75):**
`maak_stroombeen_weg.py --profiel diamant-surat-hongkong-surat-bdb --bron geofabrik` — **279,5 km** geroute
(NH48-aansluiting → Navsari → Vapi → Boisar → Vasai-Virar → Dahisar → Bharat Diamond Bourse), tegen ~280 km
ontwerp = **−0,2% [OK]**. `toets_knikken.py`: 39 knikken ≥60°, 2 omkeringen waarvan **1 TERUGLOOP**
(154,1°, R≈9 m, bij 19,23814/72,85904, nabij Vasai-Virar) — bevinding, niet gerepareerd (overige knikken zijn
OSM-spikes op kleine wegklassen). Doorgetrokken (geen stippel).

**b2 (truck, gespiegelde kopie, 8,4 km):** `Bharat Diamond Bourse → CSMIA Air Cargo Complex`. Fysiek hetzelfde
Airport Road/BKC-connector-been als `diamant-mirny-mumbai.md` b4 (CSMIA → BDB), in omgekeerde richting —
letterlijk gespiegelde coördinatenreeks uit `diamant-mirny-mumbai-weg-bom-bdb.geojson`, geen tweede scan
gedraaid (bakhandleiding: hergebruik i.p.v. opnieuw scannen). Geen via-punten (<15 km, binnen Mumbai, geen
corridorkeuze). `toets_knikken.py`: 16 knikken ≥60°, 0 omkeringen — allemaal OSM-spikes.

**b3 (lucht, `maak_luchtbeen.py`):** CSMIA Air Cargo Complex (BOM, 19,0994/72,8673) → Cathay Pacific Cargo
Terminal (HKG, 22,2975/113,9247) — **4.272,8 km** grootcirkel, 172 punten. Komt exact overeen met de
brief-schatting (4.272,8 km). Doorgetrokken; geen tussenlanding gebrond (brief §7) → één directe vlucht.
`toets_knikken.py`: 0 knikken (per constructie recht).

**b4 (truck, nieuw profiel `diamant-surat-hongkong-hkgcargo-hkexchange`, extract `china`, vensterKm 40,
eindToegangPrivaat):** `maak_stroombeen_weg.py --profiel diamant-surat-hongkong-hkgcargo-hkexchange --bron
geofabrik` — **40,8 km** geroute (Cathay Pacific Cargo Terminal → North Lantau Highway → Tsing Ma Bridge →
Kwai Chung Interchange → Western Harbour Crossing → Hong Kong Diamond Exchange Building), tegen ~32,4 km
via-punten-som = **+25,8% [BUITEN ±15% — bevinding, niet dichtgetrokken]**: geen harde gepubliceerde km in de
brief, en de HK-tunnels/bruggen (North Lantau Highway/Tsing Ma Bridge/Western Harbour Crossing) maken een
reële omweg t.o.v. de rechte via-puntenketen die de brief als schatting gaf. `eindToegangPrivaat` liet de
eerste km bij het vrachtterminal (airside) over kleine wegklassen toe zonder aparte stippel (first mile
0,88 km, last mile 0,59 km). `toets_knikken.py`: 15 knikken ≥60°, 1 omkering (**TERUGLOOP**, 162,0°, R≈4 m,
bij 22,36356/114,11914, nabij Kwai Chung Interchange) — bevinding, niet gerepareerd.
**Hongkong-dekking in de china-extract is hiermee bevestigd** (open punt uit §7 opgelost): de china-pbf dekt
Hong Kong volledig (122.566 ways gehouden in de scan) — geen nieuwe extract nodig.

**Toets:** alle 5 naden **0,00 km**, ruim onder de norm van 5 km. `toets_knikken.py` over de hele stroom: 70
knikken ≥60°, 3 omkeringen ≥150° waarvan **2 TERUGLOOP** (b1b en b4, hierboven genoemd) — beide bevindingen,
niet gerepareerd (geen via-punt bijgeschoven om de km-toets te halen). `toets_rechte_benen.py --min-km 5`:
**geen enkel been van deze stroom in de uitslag** (de 0,3 km-stippel blijft onder de toetsdrempel; de vier
overige benen zijn geroute of per constructie recht). json geldig: versie 2, punt_formaat lonlat, modaliteiten
uitsluitend {truck, lucht}, elk been ≥2 punten. Bestandsgrootte **105,5 KB**, ruim onder de ~300 KB-richtnorm.
Alle 5 markers liggen op ~0 m van hun been (elk marker valt samen met een been-uiteinde).

**Gereedschapslessen:** `eindToegangPrivaat` lost alleen een **access-filter** op binnen de eindzone, geen
**component-scheiding** — een site met een eigen, in OSM volledig geïsoleerd wegenstelsel (DREAM City) blijft
"geen wegpad" geven totdat het eerste via-punt verschuift naar het routeerpunt op het publieke net, met de
oorspronkelijke satelliet-gelegde ankercoördinaat behouden en het tussenliggende stukje als korte stippel
(anker ≠ routeerpunt, bakhandleiding §2/§5). Gediagnosticeerd met een BFS-component-telling op de scan-cache
(`fetch_landnet._wegen_graaf` + `_dichtste_knoop`), niet door het venster of de wegklassen te verruimen.
