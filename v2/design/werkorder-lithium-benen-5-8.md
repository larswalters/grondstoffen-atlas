---
type: werkorder
datum: 2026-08-05
stroom: lithium-greenbushes-zhangjiagang
status: te beoordelen (twee redactionele besluiten open — zie de kop van sectie C)
---

# Werkorder — lithium benen 5 t/m 8: van de kade van Zhangjiagang tot in Tesla Giga Shanghai

*Uitkomst van de ankerronde van 2026-08-05 (vier zoeklijnen, elk met een eigen weerlegger).
**A1** (ankers) en **A2** (corridors b5/b6) hielden stand op hun dragende kern; **A3**
(corridors b7/b8) is door zijn weerlegger **niet houdbaar** verklaard en staat daarom voluit
in sectie F — met de precieze uitzondering die hieronder wordt verantwoord. **A4** is
gesplitst: deel (a) — het gereconstrueerde bak-recept — is **byte-identiek bewezen** en gaat
mee; deel (b) — de haven-aanloop van Bunbury — is **niet houdbaar** en staat in F.*

**Project:** `C:\automation\Projects\General\grondstoffen-atlas` · **stroom-id:**
`lithium-greenbushes-zhangjiagang` · **brief:**
`v2\design\routebrieven\lithium-greenbushes-zhangjiagang.md` · **werkwijze:**
`v2\design\routebrief-werkwijze.md` · **sjabloon:** `v2\design\werkorder-koper-guixi-de.md`

---

## Uitgangspunt — en wat er wél en niet binnenkomt

De opdracht was: de lithiumketen doortrekken tot in Tesla Giga Shanghai, zodat lithium de
**tweede** stroom wordt die de A–E-belofte helemaal waarmaakt. Dat kan, **en het is meer dan
de vorige ronde bij koper opleverde** — maar met drie harde correcties op de brief en twee
zichtbare procesgaten.

**Wat er binnenkomt.**

* **Benen 5 t/m 8 zijn bouwbaar.** Vier wegbenen, samen ≈ 650 km, van de kade van
  Zhangjiagang tot poort 3 van Giga Shanghai. De keten wordt daarmee **9 benen /
  ≈ 8.484 km**.
* **De drie fabrieksankers zijn satelliet-gelegd** en de twee die de brief noemde en die
  **fout** waren zijn vervangen (Nanjing en Tesla — zie hieronder).
* **Het bak-recept van deze stroom staat vast** en gaat in `v2/tools/bak_stromen.sh`; daarmee
  is het openstaande punt "de recepten van `collahuasi-tongling`, `lobito-duisburg` en
  `lithium` staan nergens" voor lithium dicht.

**Wat er NIET binnenkomt, en dat is een resultaat.**

* **De drie uitgaande laadplekken** (Tianqi, Wuxi, Nanjing) zijn **niet gevonden**. Alle drie
  krijgen een **substituut-kop** met een zichtbaar procesgat — precies besluit (a) uit de
  koper-werkorder. Zie **F3**.
* **De losplek binnen Giga Shanghai** is niet gedocumenteerd. Been 8 eindigt op de **poort**,
  niet op het terrein. Zie **F4**.
* **De haven-aanloop van Bunbury** (het gat van 4.933 m, het grootste van alle vijf stromen)
  wordt deze ronde **niet gedicht** — het voorstel daarvoor brak bij de weerlegging. Zie
  **F2**.

> ### ⚠️ DRIE CORRECTIES OP DE BRIEF DIE JE MOET LEZEN VÓÓR JE IETS BOUWT
>
> 1. **De Tesla-poort uit de brief bestaat niet als poort.** `30.87390, 121.76572` is het
>    rekenkundig midden van **vier OSM-bushaltenodes** (`特斯拉3号门`, alle
>    `highway=bus_stop` / `public_transport=platform|stop_position`; gemiddelde
>    30.873906 / 121.765716 — een identiteit, geen benadering). Het punt ligt **1,0 m van
>    de publieke straat 正嘉路** aan de **westkant van het kanaal** en **60,9 m BUITEN** de
>    fabriekspolygoon. Een been dat daar eindigt eindigt op een openbare weg aan de verkeerde
>    kant van het water. De werkelijke poort 3 ligt op **30.87423, 121.76667** (brug over het
>    kanaal, wachtersgebouw met luifel, vrachtwagens in de rij; 18,2 m **binnen** OSM-way
>    635670279).
> 2. **Het Nanjing-anker uit de brief ligt buiten het hek.** `32.16300, 118.87900` ligt
>    **21,4 m westelijk** van de perceelgrens van way 621624910, in beboste helling met oude
>    funderingen; de terreinmuur loopt er zichtbaar langs. Het stond als "satelliet-gelegd op
>    z16" — en z16 (2,0 m/px) **kan** dat verschil niet zien.
> 3. **Twee lengtes in de brief zijn onmogelijk.** Been 5 staat op "±3–5 km" terwijl kade →
>    poort **hemelsbreed al 6,04 km** is en over de weg **10,26 km**; been 8 staat op
>    "±300 km" terwijl dat de **grootcirkel** is (poort-tot-poort hemelsbreed 308,68 km) en de
>    weg **≈ 376 km** meet. Corrigeer beide **vóór** de lengtetoets draait, anders keurt de
>    toets een correcte lijn af.

---

## A · Ankerlijst

lat, lon in decimale graden, **5 decimalen**, WGS-84. Kolom **rol** onderscheidt wat werkwijze
§2b uit elkaar wil houden: *laadplek/losplek/poort* (waar een lijn aanhecht) · *routeerpunt*
(waar het net begint) · *terreinanker* (het zwaartepunt van een werk) · *substituut* (een
anker dat de plek van een niet-gevonden anker inneemt, mét zichtbaar procesgat).

**Alle passes in deze tabel zijn eigen passes van 2026-08-05, tweemaal onafhankelijk bekeken
(bevinding + weerlegger). PNG's in `v2/build-cache/satcheck/`.**

| id / rol | omschrijving | lat, lon | status | landt in |
|---|---|---|---|---|
| `li-zjg-kade` — **losplek schip** | Kade Zhangjiagang Port Group, bulksectie. Kraanlijn met zeven oranje portaalkranen, apron, general-cargoschip langszij. **ONGEWIJZIGD**, hertoetst op z18 | **31.96800, 120.42050** | **satelliet-gelegd** (z18, 0,51 m/px) | bestaand · marker · kop b5 |
| ↳ terreinstap | Ommuurde bulkbakken met donker bulkmateriaal, 50,0 m ZZW van het kade-anker (het stapelveld; de truck-laadplek zelf is niet gepubliceerd) | 31.96755, 120.42051 | satelliet-gelegd (z18) | brief §2a-3 · géén marker |
| — **havenpoort** | Landzijdige uitgang van de publieke terminal: luifel over meerdere rijstroken met gele markering, opstelruimte, truckparkeerterrein zuidelijk. 617,7 m van het kade-anker | **31.96245, 120.42078** | **satelliet-gelegd** (z18) | brief §2b · ⚠️ **géén marker** (234 m van de lijn, zie E-5) |
| ↳ routeerpunt b5 | Uitrit terminal op **西五节桥街** (OSM way 1014096488, `highway=service`, géén access-tag) — het eerste OSM-wegpunt van de hele keten na de kade | **31.96347, 120.42295** | bevestigd (0,555 km van het kade-anker) | bakprofiel b5 |
| `li-zjg-tianqi` — **poort** | 天齐锂业（江苏）, **东新路 5**. Verharde voorterrein-strook aan de ZUIDzijde van 东新路 met vrachtwagens; ZW procesloodsen + stoompluim, O turquoise bezinkbekkens, ZO witte zwavelzuurtanks | **32.01218, 120.45771** | **satelliet-gelegd** (z18) — ⚠️ zie de statuswaarschuwing onder deze tabel | aansl. (nieuw) · marker · staart b5 / kop b6 |
| ↳ routeerpunt | Projectie op OSM way 432043510 (`highway=tertiary`, 东新路); punt-tot-**segment** 24,9 m. ⚠️ De dichtstbijzijnde graafKNOOP ligt **79,5 m WEST** — de lijn schiet er 75 m voorbij | 32.01239, 120.45763 | bevestigd | bakprofiel · brief |
| — **substituut-kop b6** | Terreinanker/registercentroïde Tianqi (dak van de zonnepanelen-loods aan de westrand, binnen het hek). **PROCESGAT 218,9 m** t.o.v. de poort | 32.01050, 120.45650 | satelliet-gelegd (z18) | ⚠️ **NIET gebruikt als profiel-kop** — zie C2 |
| `li-wx-lgchem` — **losplek** | Laaddock 乐友新能源材料（无锡）, westgevel noordelijke hal: **twee rode opleggers onder een uitkragende laadluifel**; 92 m ZW een tweede dock. 68,0 m van het EIA-anker | **31.52362, 120.47518** | **satelliet-gelegd** (z19, 0,25 m/px) | aansl. (nieuw) · marker · staart b6 |
| ↳ routeerpunt | 新鸿路 (ref X252, OSM way 419872749, `secondary`) — 126,3 m van het laaddock, 186,5 m van het EIA-anker | 31.52432, 120.47413 | bevestigd | bakprofiel |
| — **substituut-kop b7** | **Zuidpoort** 乐友无锡 aan 锡梅路: achthoekig poortpaviljoen met slagboomrijstroken, entreeplein, kantoorblok, parkeerterrein. Valt binnen 15 m samen met de poortcoördinaat uit het adresrecept. **PROCESGAT 310,1 m** t.o.v. het laaddock | **31.52084, 120.47492** | **satelliet-gelegd** (z18) | marker · kop b7 |
| ↳ routeerpunt | 锡梅路 (Ximei Road, OSM way 419872745/761658155, `secondary`) — de adresstraat 锡梅路 167号, 79,1 m van de zuidpoort | 31.52029, 120.47439 | bevestigd | bakprofiel |
| `li-nj-lges` — **terreinanker** | LG-campus New Port, bbox-midden van OSM way 621624910 (33,97 ha; bbox 32.15820,118.87596 .. 32.16403,118.88311). Licht bedrijfsgebouw aan de westzijde, **binnen het hek**; op dezelfde pass het rode LG-logo-monument ZW ervan | **32.16111, 118.87953** | **satelliet-gelegd** (z18) | aansl. (nieuw) · marker · staart b7 |
| ↳ routeerpunt | Interne service-way van de campus, OSM way **1303627568** — **12,3 m** van het terreinanker. ⚠️ Niet way 1303627572 (dat is de way lángs de apron) | 32.16110, 118.87960 | bevestigd | bakprofiel |
| — **substituut-kop b8** | **Hoofdpoort 恒谊路**: poortgebouw met portiek en slagboomrijstroken, daarachter het ceremoniële entreeplein met het **rode LG-logo-monument** in een cirkelplein; oplegger op de boulevard. Bevestigt het vrachtadres 恒毅路 17号 / HENGYI RD NO.17. **PROCESGAT 301,4 m** t.o.v. het terreinanker | **32.15840, 118.87950** | **satelliet-gelegd** (z19) | marker · kop b8 |
| ↳ routeerpunt | 恒谊路 (OSM way 323626513/94676566, `secondary`) — 34,5 m onder de poort | 32.15809, 118.87944 | bevestigd | bakprofiel |
| `li-sh-tesla` — **poort** | **Tesla Giga Shanghai, poort 3 (de echte).** Brug over het kanaal; oostzijde een wachtersgebouw op een verkeerseiland met luifel over de rijstroken; blauwe + twee donkere vrachtwagens; direct oostelijk de fabrieksapron met opleggers. **18,2 m BINNEN** OSM-way 635670279 (`特斯拉上海超级工厂`, `operator=Tesla (Shanghai)`, wikidata Q55642234, 85,97 ha) | **30.87423, 121.76667** | **satelliet-gelegd** (z19, 0,26 m/px) | aansl. (nieuw) · marker · **staart b8 = keten-eind** |
| ↳ routeerpunt | Toegangsweg over de brug, OSM way 1229490502 (`secondary`) op **3,3 m**. ⚠️ way 907920271 (`service`, `access=customers`) op 14,8 m is intern en valt per constructie uit `WEG_ACCESS_WEG` | 30.87426, 121.76668 | bevestigd | bakprofiel |

### Negatieve ankers (mét coördinaat en verbodsstraal — werkwijze §2)

| punt | lat, lon | straal | geldt op | gemeten op de kandidaat-lijn |
|---|---|---|---|---|
| **Bushaltes 特斯拉3号门** — ⚠️ *het EINDPUNT van b8 mag hier niet liggen; de lijn mag er wel langs* | 30.87390, 121.76572 | 0,15 km **eindpunt-only** | b8 | de route passeert de kruising 江山路 × 正嘉路 op ~62 m — **een straal op passage zou een correcte lijn afkeuren** |
| Shanghai binnenring / 人民广场 (vrachtverbod hele dag; sinds 15-10-2025 diesel Euro-IV verboden binnen G1503) | 31.23040, 121.47370 | 15 km | b8 | 31,34 km ✓ |
| Shanghai-havengebied | 31.23000, 121.48000 | 15 km | b6 | 98,57 km ✓ |
| Jiangyin / westelijke Yangtze-oversteek (G2-corridor) | 31.92160, 120.28090 | 10 km | b6 | 17,78 km ✓ |
| Suzhou | 31.29900, 120.61940 | 15 km | b6 | 27,62 km ✓ |
| G4221 沪武高速 bij Jintan (de zuidelijke corridor die S38 daar meedraagt) | 31.72431, 119.29857 | 15 km | b7 | 34,88 km ✓ |
| LG-campus **Jiangning/Binjiang** (de andere LG-locatie in Nanjing; de brief kiest bewust New Port) | 31.85052, 118.56654 | 10 km | b7 · b8 | 42,7 km ✓ (45,4 km van het New Port-campusmidden) |
| Yangshan diepzeehaven | 30.63000, 122.06000 | 20 km | b8 | 39,07 km ✓ |
| Zhangjiagang-kade (b7/b8 mogen niet terugvallen op de Yangtze-oever) | 31.96800, 120.42050 | 15 km | b7 · b8 | 34,47 km ✓ |
| Staal-/houtsectie van dezelfde Zhangjiagang-kade (buizen-/coilstapels, houtbundels) | 31.96757, 120.42185 | 0,15 km | b5 | zie **F12** — dit conflicteert met de productvraag |
| Chemiesteigers Yangzijiang-chemiepark (vloeistofsteigers met leidingtrestle) | 32.01100, 120.45250 | 0,6 km | ⚠️ **alleen b4** | **CONFLICT: b5 én b6 raken op 0,43 km.** Dit anker hoort bij het schip, niet bij een wegbeen — 长江北路 loopt daar volkomen terecht langs. **Zet de straal per been** (E-4) |

**Statuswaarschuwing die letterlijk in de brief moet.** De Tianqi-"poort" (32.01218/120.45771)
is **satelliet-gelegd als vestigingspunt aan 东新路**, niet als gekarteerde deur: op z18 is er
een verharde berm met geparkeerde vrachtwagens, géén poortgebouw, géén slagboom, géén
`barrier`-tag. Dat is precies de klasse *"een registerpunt is een vestiging, geen deur"*. Hij
mag als aanhechtpunt dienen (de weg loopt er op 24,9 m langs) maar niet als "gekarteerde
poort" worden opgeschreven. Zelfde nuance bij de Wuxi-zuidpoort en de Nanjing-hoofdpoort —
dáár is wél een poortgebouw zichtbaar, dus die twee mogen "poort" heten.

**Wat er NIET in staat, en waarom dat een resultaat is.** De brief stelde in §2b vier
overslagen met elk twee ankers in het vooruitzicht. Bij drie ervan (Tianqi, Wuxi, Nanjing) is
het **vertrek**anker niet gevonden en staat er een **substituut** met een gemeten gat van
219 / 310 / 301 m. Bij Giga Shanghai is de losplek niet gedocumenteerd. Zie **F3** en **F4** —
niet weggelaten, en niet vervangen door een gok.

---

## B · Reparaties aan het bestaande deel (benen 1 t/m 4)

### B1 — de brief liegt over twee snap-toleranties bij Bunbury (A4, houdbaar)

De brief §2b zegt *"routeerpunt in de binnenhavengeul ±−33.31930, 115.66230; afstand tot het
kade-anker ±160 m. Verwachte maximale snap 300 m"* en been 3 zegt *"max snap 2 km"*.
**Gemeten, tweemaal onafhankelijk:**

| uiteinde | brief-verwachting | gemeten | factor |
|---|---|---|---|
| kop been 3 (Berth 8 → MARNET) | ≤ 300 m | **4.933,0 m** | 16× |
| staart been 3 (Wusongkou → MARNET) | ≤ 2 km | **13.018 m** | 6,5× |

Dat zijn geen krap uitgevallen toleranties maar **verkeerde verwachtingen**: MARNET *heeft*
geen knoop in de binnenhaven. De eerstvolgende MARNET-zeeknoop na −33.30640/115.61330 ligt
**92,804 km** verderop (Kaap Naturaliste), daarna Fremantle op 140,6 km — er is niets
dichterbij om op te snappen. En het uiteinde hangt **niet af van welk punt je voedt**: anker
(4,933 km) én brief-routeerpunt (4,774 km) snappen op dezelfde knoop.

**Doorvoeren:** vervang beide getallen door de gemeten waarden, met de reden erbij.
⚠️ **Trek het gat niet dicht** — zie **F2**.

### B2 — §6a van de brief staat op de `?v=104`-stand (A4, houdbaar)

De brief-tabel "Wat er GEBAKKEN is" zegt 7.827,0 km / 2.540 punten / b4 128,7 km / 659 punten
en mist het vijfde been. Op schijf staat sinds commit `95535c6`:

| been | modaliteit | km | punten |
|---|---|---|---|
| b1+b2 | truck | 83,1 | 1.094 |
| b3 | zee | 7.606,6 | 785 |
| — | zee, **stippel** | 8,6 | 2 |
| b4 | binnenvaart | **135,2** | **693** |
| — | binnenvaart, **stippel** (ligplaats-aanloop) | **0,6** | **2** |
| **totaal** | | **7.834,1** | **2.576** |

4 markers. `stroom`-id `lithium-greenbushes-zhangjiagang`, `versie` 2, laatste punt
`[120.4205, 31.968]`. Herschrijf §6a hiernaar vóór je de nieuwe stand erin zet.

### B3 — twee brief-lengtes corrigeren vóór de lengtetoets draait

| been | brief | gemeten | actie |
|---|---|---|---|
| b5 | ±3–5 km | hemelsbreed 6,037 km · **over de weg 10,261 km** | vervang door **±10 km** |
| b8 | ±300 km | hemelsbreed **308,68 km** poort-tot-poort · over de weg **≈ 376 km** | vervang door **±375 km**, mét de noot dat de ±300 de grootcirkel was |

b6 (±70 tegen gemeten 67,955 = −2,9 %) en b7 (±180 tegen gemeten 196,3 = +9,1 %) blijven
staan. ⚠️ b7 is **krap binnen ±10 %** en is het eerste getal dat kantelt als kop of staart
schuift — en die kop schuift in deze werkorder (zie C3).

### B4 — het bak-recept vastleggen in `v2/tools/bak_stromen.sh`

A4 heeft het recept van benen 1–4 gereconstrueerd en de weerlegger heeft het **byte-identiek
nagedraaid**: sha256 van de kandidaat en van
`v2/data/stroomroute-lithium-greenbushes-zhangjiagang.json` zijn gelijk na normalisatie van
het veld `gemaakt` (52.821 byte). Drie vrijheidsgraden geven alle drie een identiek bestand:

* `--graaf mississippi` of `rijn` — **identiek**, en het mechanisme is gemeten: het zeebeen
  rapporteert *0 track-edges · 46 MARNET-edges · 0 connectors*, dus de track-graaf doet hier
  niets. ⚠️ Tóch pinnen: een graaf die deze route wél zou dekken kan het antwoord veranderen.
  (Anders dan bij `bak_koper_lobito`, waar `rijn` verplicht bleek.)
* `--been`-uiteinden op het **anker** of op het **routeerpunt** — identiek (snaps 4,933 vs
  4,774 km resp. 13,018 vs 14,460 km, telkens dezelfde knoop).
* `--vermijd northwest` (default) of leeg — identiek (MARNET-zee 9.679 → 9.686 knopen).

⚠️ **Twee dingen die A4 verkeerd opschreef en die je NIET moet overnemen:**

1. A4 zet in het recept de waarschuwing *"`--naar` is de bulklaag-knoop wést van de kade;
   **alleen dán** loopt het pad door de zuidgeul"*. **Weerlegd:** `--naar 31.9733,120.4202`
   én `--naar 31.968,120.4205` geven allebei een pad waarvan de **eerste 693 punten
   byte-identiek** zijn aan het bestand op schijf. Doordat het been tóch geknipt wordt is
   `--naar` **onderbepaald**. Schrijf dat zo op.
2. A4 meldt "3,45 km (70 %) over land" op de rechte Bunbury-lijn met t=0,77; die twee spreken
   elkaar tegen. Hermeten: **3,779 km (76,6 %)**, aaneengesloten t=0 → 0,766.

### B5 — de knipstap van het rivierbeen heeft geen gereedschap (blijft open, wordt genoteerd)

`maak_rivierbeen.py --van 31.4512,121.4769 --naar 31.9715,120.3812` geeft 139,1 km / 712
punten / 19 edges; `rivierbeen-yangtze-zhangjiagang.geojson` op schijf is exact de **eerste
693 punten** daarvan (prefix 693/693 identiek), afgekapt op index 692 = de vertex op 590,0 m
van het kade-anker. **Die knipstap leeft nergens in de repo.** Herbakken zónder knip geeft een
been dat **3,69 km** voorbij de kade doorloopt (laatste punt 3,73 km van het anker). Noteer
dit in de kop van `bak_lithium()` als bekende begrenzing; het bouwen van een `--knip-bij`-vlag
valt buiten deze werkorder (**F8**).

### B6 — `v2/data/aansluitingen.json` (via de generator)

Vier nieuwe aansluitingen in `v2/tools/maak_aansluitingen.py` — `plek` is **[lon, lat]**:
`li-zjg-tianqi` (32.01218/120.45771) · `li-wx-lgchem` (31.52362/120.47518) · `li-nj-lges`
(32.16111/118.87953) · `li-sh-tesla` (30.87423/121.76667).

⚠️ **Draai eerst zonder `--schrijf` en diff** — de bestaande aansluitingen moeten op **0,0 m**
gelijk blijven (de `cu-guixi-spoor`-driftklasse: vergelijk generator↔uitvoer vóór elke
regeneratie).
⚠️ **Geef geen `modi=["weg"]` op goed geluk.** Het landnet heeft wereldwijd 1.883 wegknopen;
bij `cu-guixi-walsdraad` was de dichtstbijzijnde **341,1 km** weg en werd `modi=[]` de juiste
keuze. **Lees de gemeten snap af uit de proefrun** en zet pas dán een modus. Een snap van
tientallen kilometers is een **meetresultaat**, geen aansluiting.
⚠️ `li-zjg-tianqi` stond sinds 2026-07-30 bewust **niet** in het bestand omdat de coördinaat
niet gelegd was ("een aansluiting op een ongelegd punt ís de Waalhaven-klasse"). Die reden is
nu vervallen — noteer dat expliciet in de `noot`.

### B7 — `data/lithium.js`: §6b-variant 1 is nog niet uitgevoerd

Het besluit van 2026-07-30 (node `li-port-zhangjiagang` + node `li-ref-jiangsu`, nieuwe flow
van 17 kt LCE, Sichuan 55 → 38) staat nog steeds open. Het is register-laag en **staat volledig
los** van deze werkorder; voer het uit of laat het staan, maar laat het niet stil verdwijnen.
Geen `?v=`-bump voor dat deel.

### B8 — cache-busting

`stroomroute-lithium-greenbushes-zhangjiagang.json` is een browser-asset.
In `v2/index.html` regel **7** en **250**: `?v=109` → `?v=110`.
In `v2/src/main.js` regel **257**: `laadStroomroute(VECTOR_R, "107", …)` → `"108"`.

---

## C · Nieuwe benen — de vier profielen en het bak-recept

> ### ⚠️ TWEE BESLUITEN DIE HIERONDER LIGGEN
>
> **Besluit 1 — de drie substituut-koppen.** De uitgaande laadplekken bij Tianqi, Wuxi en
> Nanjing zijn niet gevonden. De koppen van b6, b7 en b8 zijn daarom **substituten** met een
> gemeten procesgat van **219 m / 310 m / 301 m**. Dat is exact besluit (a) uit
> `werkorder-koper-guixi-de.md`: aanhechten op een satelliet-gelegd register- of terreinpunt
> mag, **mits het verschil als procesgat in de kaart blijft staan**. Die gaten zijn óók de
> gaten tussen de benen (0,32 en 0,34 km, beide onder 0,5 km) — ze zijn dus zichtbaar
> zonder dat er een tweede uitzondering bijkomt.
> *Alternatief als Lars dat niet wil:* laat b6/b7/b8 op hetzelfde punt beginnen als waar het
> vorige been eindigde. Dan is §2b's twee-ankers-eis **nog maar nominaal** vervuld en is het
> ontbrekende anker **onzichtbaar** — dat is de Waalhaven-richting op.
>
> **Besluit 2 — de corridor van b7/b8 komt uit een NIET-HOUDBARE bevinding, maar via de
> weerlegger.** Zoeklijn A3 is als geheel **niet houdbaar** verklaard en staat voluit in
> **F1**. Wat hieronder in de profielen b7 en b8 staat zijn **niet A3's claims** maar de
> metingen die de **weerlegger zélf onafhankelijk heeft gereproduceerd** (eigen pyosmium-scan
> over 603.618 highway-ways, eigen 1-op-1 replica van de router, eigen sat-passes): "de
> corridorkeuze zelf is solide en door mij onafhankelijk gereproduceerd, inclusief de
> verwerping van S38/G4221 en de drie (vier) arcs … bruikbaar als **corridorbewijs**, niet als
> anker- en last-mile-bewijs." De **ankers** komen daarom uit **A1** (houdbaar), niet uit A3.
> *Alternatief als Lars dat te ver vindt:* bouw alleen b5 en b6 (A2, houdbaar en twee keer
> gemeten) en laat b7/b8 wachten tot een eigen ronde. De keten eindigt dan bij de
> kathodefabriek in Wuxi en lithium wordt **niet** de tweede complete keten.

### C0 · Waarom het vier wegbenen worden en geen stippels

De stippellijn betekent in dit project precies één ding: *hier reikt het net niet* (werkwijze
§7). Gemeten reikt het net overal:

| been | dichtstbijzijnde OSM-weg bij de kop | bij de staart |
|---|---|---|
| b5 | 555 m (西五节桥街, `service`) — ⚠️ **het terminalterrein zélf heeft 0 highway-ways in OSM** | 24,9 m (东新路) |
| b6 | 79 m (东新路-graafknoop) | 126 m (新鸿路 X252) |
| b7 | 79 m (锡梅路) | 12,3 m (campus-service-way 1303627568) |
| b8 | 34,5 m (恒谊路) | 3,3 m (toegangsweg 1229490502) |

Alle vier doorgetrokken. **Eén uitzondering:** de 555 m tussen het kade-anker en het eerste
OSM-wegpunt van b5. Dat is een **karteringsgat**, geen ontbrekende weg — op de tegels lopen de
terminalwegen er wel, OSM heeft ze niet. Gemeten binnen 900 m van de kade: geen enkele
highway binnen het terminalterrein; dichtstbijzijnde 西五节桥街 554,5 m, 中兴北路 658,1 m,
双山路 698,9 m, 中港路 (Y303) 701,9 m. `maak_stroombeen_weg.py` vlagt die aanloop zelf als
`> 0,5 km — bevinding`, en **dat is de juiste uitslag, niet iets om weg te poetsen.**

### C1 · Been 5 — profiel `lithium-zhangjiagang-lastmile`

Zet dit in de `PROFIELEN`-dict van `v2/tools/maak_stroombeen_weg.py` (~regel 96), **niet in
een kopie**. Coördinaten daar zijn **(lon, lat)**.

```python
    # ── Routebrief lithium-greenbushes-zhangjiagang, been 5 (2026-08-05) ──
    # FASE C, last mile: van de publieke kade van 张家港港务集团 naar de poort van
    # 天齐锂业（江苏）, 东新路 5号 in het 扬子江国际化学工业园.
    #
    # ⚠️ DE BRIEF ZEGT ±3-5 KM EN DAT KAN NIET. Hemelsbreed liggen de twee ankers
    #    al 6,037 km uit elkaar: de weg moet zuidwaarts om de monding van het
    #    Zhangjiagang-kanaal en de zuidgeul heen. Gemeten 10,261 km over 51 punten
    #    — tweemaal onafhankelijk gereproduceerd (bevinding + weerlegger, tot op
    #    de meter gelijk).
    # ⚠️ DE EERSTE 0,555 KM IS HAVENTERREIN EN STAAT NIET IN OSM. In het vak
    #    lon 120,413-120,4275 x lat 31,9625-31,970 liggen 5 highway-ways, alle op
    #    lat <= 31,9641 (de zuidrand); boven 31,965 nul. De tool vlagt die aanloop
    #    als "> 0,5 km — bevinding"; dat is de JUISTE uitslag. Niet dichttrekken.
    # ⚠️ eindKlassen BEWUST NIET GEZET. Het beslissende eerste stuk is
    #    西五节桥街 = highway=service, en `service` zit AL in EIND_KLASSEN_DEFAULT
    #    ("residential", "service", "tertiary", "unclassified"). Zetten zou alleen
    #    de cachevingerafdruk veranderen (scan_corridor["id"] = eigen id + de
    #    eindklassen), niet de uitkomst.
    #    ⚠️ CORRECTIE OP DE KOPER-COMMENT: het argument "anders komen de bestaande
    #    profielen niet byte-identiek uit de bake" is ONJUIST — EIND_KLASSEN wordt
    #    per run in _kies_profiel gezet en de scan-id wordt uit het EIGEN id van
    #    elk profiel gebouwd, dus een eindKlassen-sleutel op een nieuw profiel kan
    #    een ander profiel per constructie niet raken. Het besluit klopt wel.
    # ⚠️ ALLE VIA-PUNTEN ZIJN ECHTE OSM-VERTICES uit de eigen wegscan (snap
    #    0-1 m), geen plaatsknopen — de Balingup-val (180,0 graden keerpunt, been
    #    2 van deze zelfde stroom) kan hier per constructie niet optreden.
    "lithium-zhangjiagang-lastmile": {
        "via": [
            ("Kade Zhangjiagang Port Group",            (120.42050, 31.96800)),
            ("中兴北路 × 常金线 X301",                     (120.42398, 31.95890)),
            ("常金线 X301 — vak zuid van 双山岛",           (120.43965, 31.96252)),
            ("常金线 X301 — vak langs het chemiepark",     (120.46944, 31.98062)),
            ("常金线 X301 × 长江北路",                     (120.47170, 31.99419)),
            ("长江北路 × 东新路",                          (120.46199, 32.01353)),
            ("Poort Tianqi Lithium (Jiangsu), 东新路 5",   (120.45771, 32.01218)),
        ],
        "id": "li-zjg-lastmile",
        "naam": "kade Zhangjiagang Port Group → poort Tianqi Lithium (Jiangsu) "
                "(西五节桥街 → 中兴北路 → 常金线 X301 → 长江北路 → 东新路)",
        "extracts": ["china"],
        # 常金线 draagt X301; 中兴北路/长江北路/东新路 zijn ongenummerd en krijgen
        # de zachte factor 3 — gemeten verandert dat de route niet.
        "refs": ["X301"],
        # ⚠️ TAUTOLOGISCH: dit is onze eigen meting, geen gepubliceerde waarde.
        #    De lengtetoets op dit been bewijst dus niets; de echte controle is de
        #    wegblokken-lijst en de verklikkers in sectie E van de werkorder.
        "gepubliceerdKm": 10.26,
        "bronnoot": "eigen Dijkstra over china-latest (2026-08-05) met exact de "
                    "regels van dit gereedschap, twee keer onafhankelijk "
                    "gereproduceerd; geen bron publiceert deze afstand. De "
                    "brief-waarde ±3-5 km is niet reproduceerbaar: de hemelsbrede "
                    "afstand kade→poort is al 6,037 km",
        "vensterKm": 5,
        "uit": "stroombeen-zhangjiagang-lastmile.geojson",
    },
```

**Verwachte uitvoer (vooraf gemeten, twee keer):** 10,261 km · 51 punten · benen
0,694 / 1,533 / 3,666 / 1,525 / 2,337 / 0,507 km · snaps via-punten
0,555 · 0,000 · 0,001 · 0,000 · 0,001 · 0,000 · 0,079 · `kmAanloopVan` **0,555**
(⚠️ vlagt >0,5 — dat ÍS het onbekarteerde haventerrein) · `kmAanloopNaar` 0,079
(punt-tot-segment 0,025) · wegblokken **西五节桥街 185 m → 中兴北路 509 m →
常金线 X301 6.723 m → 长江北路 2.337 m → 东新路 507 m** · `snoei_keerlussen` 0 ·
omkeringen ≥150° **0** · knikken ≥60° **3**.

⚠️ **Twee van die drie knikken zijn géén geografie.** Op 31,97695/120,46699 en
31,97690/120,46709 (10 m uit elkaar) staan knikken van 96,3° en 96,9°: de route springt van de
ene X301-rijbaan via 10,8 m 南海路 naar de andere. Dat is een artefact van de **ongerichte**
graaf (X301, 长江北路 en 中兴北路 zijn alle `oneway=yes` gescheiden rijbanen) en glipt onder
`snoei_keerlussen` door (drempel 25 m). ~10 m groot, dus cosmetisch verwaarloosbaar — maar
schrijf hem niet op als "echte T-kruising".

⚠️ **De staart schiet 75 m voorbij de poort en keert terug.** De laatste graafknoop ligt op
32,012183/120,456867, **79,5 m WEST** van de poort terwijl de lijn uit het oosten komt
(punt-tot-segment 24,9 m). Klein familielid van de Guixi-overschiet (792 m).
**`knip_osm_been.py` is hier NIET bruikbaar**: dat gereedschap knipt één benoemde way, en dit
been loopt over vijf verschillende benoemde wegen. Laat de 75 m staan en noteer hem.

### C2 · Been 6 — profiel `lithium-zhangjiagang-wuxi`

```python
    # ── Routebrief lithium-greenbushes-zhangjiagang, been 6 (2026-08-05) ──
    # FASE D: batterijkwaliteit hydroxide/carbonaat van 天齐锂业（江苏）naar de
    # kathodefabriek 乐友新能源材料（无锡）, 锡梅路 167号, Xinwu, Wuxi.
    #
    # DE CORRIDOR: 东新路 → 长江北路 → 常金线 X301 → 东海路 → S23 靖张高速
    #   (OSM name:en "Zhangjiagang Port Expressway") → G4221 沪武高速 →
    #   张家港枢纽立交 → S19 通锡高速 → afrit Xinwu → 新鸿路 X252.
    #
    # ⚠️ DE KOP IS DE POORT, NIET DE UITGAANDE LAADPLEK. Die laadplek is niet
    #    gevonden (werkorder F3); het procesgat van 218,9 m naar het terreinanker
    #    32.01050/120.45650 blijft daarom bewust bestaan en wordt NIET getekend.
    # ⚠️ DE CORRIDORKEUZE IS ROBUUSTER DAN EERST GEMELD, MAAR HET AANGEVOERDE
    #    BEWIJS KLOPTE NIET. De claim "zonder via-punten kiest de Dijkstra de
    #    S259-route van 61,0 km" is NIET reproduceerbaar: met de refs hieronder en
    #    NUL via-punten (venster 12 én 25 km) komt er exact 67,955 km uit, dezelfde
    #    408 punten. De 61,0 km verschijnt pas als je óók de refs leegmaakt. Wat de
    #    keuze wél draagt is een TIJD-optimale vrije Dijkstra (klassesnelheden,
    #    geen via-punten, geen refs, venster 25 km, dus met S228/S259/G2/G42/S48 in
    #    de zoekruimte): die kiest punt voor punt dezelfde lijn — 67,955 km /
    #    48,6 min tegen 61,3 km / 69,9 min voor S259. Drie onafhankelijke criteria
    #    (via-punten, ref-voorkeur, reistijd) geven dezelfde corridor.
    # ⚠️ S259 锡张线 IS EEN REËEL ALTERNATIEF (werkwijze §2), geen negatief anker:
    #    korter (61,0 km) maar trager, aandeel onbekend.
    # ⚠️ "G2 京沪高速 ligt minimaal 17,4 km van deze lijn" IS FOUT en mag niet in
    #    de brief. Ways met ref exact "G2" liggen 17,29 km weg, maar het
    #    concurrentievak met ref "G2;G42" — dat ÍS 京沪高速 — passeert op 2,02 km
    #    (bij 31,5073/120,4545). De conclusie (deze corridor is niet G2) blijft
    #    staan; het bewijs zat er 8,6x naast. _wegen_graaf matcht op ref.split(";").
    # ⚠️ DE TWEE KNOOPPUNT-VIAS LIGGEN NÁ DE INVOEGING (627 m op de G4221, 466 m
    #    op de S19), niet op het kruis — de overschiet-en-terug-regel.
    # ⚠️ eindKlassen BEWUST NIET GEZET: tertiary (东海路) en secondary zitten al in
    #    WEG_HOUD resp. EIND_KLASSEN_DEFAULT.
    "lithium-zhangjiagang-wuxi": {
        "via": [
            ("Poort Tianqi Lithium (Jiangsu), 东新路 5",    (120.45771, 32.01218)),
            ("长江北路 (Yangtze North Road)",                (120.46633, 32.00489)),
            ("常金线 X301 ná de aansluiting",               (120.47047, 31.98681)),
            ("东海路 → kop van de S23",                     (120.46599, 31.96594)),
            ("S23 靖张高速 ná de toerit",                    (120.47810, 31.95761)),
            ("S23 靖张高速 — middenvak",                     (120.49876, 31.89771)),
            ("S23 靖张高速 — vóór het knooppunt G4221",       (120.52082, 31.83047)),
            ("G4221 沪武高速 ná de invoeging",               (120.53242, 31.80877)),
            ("S19 通锡高速 ná 张家港枢纽立交",                  (120.58071, 31.78839)),
            ("S19 通锡高速 — middenvak west van Changshu",    (120.55646, 31.69145)),
            ("S19 通锡高速 — zuidvak oost van Wuxi",          (120.52141, 31.58316)),
            ("S19 通锡高速 — vóór de afrit Xinwu",            (120.48052, 31.52150)),
            ("新鸿路 X252 ná de afrit",                     (120.47346, 31.52318)),
            # ⚠️ STAART = HET LAADDOCK (z19: twee rode opleggers onder een
            #    laadluifel), NIET het EIA-anker 31.523573/120.475895. Reden is
            #    meetbaar: het EIA-anker ligt 186 m van de gerouteerde lijn en zou
            #    de marker-eis (<= 0,15 km punt-tot-segment) breken; het laaddock
            #    ligt op 126,3 m van 新鸿路. De 68,0 m ertussen zijn de correctie.
            #    Bijvangst: het EIA-anker was het enige anker in de brief met 6
            #    decimalen terwijl werkwijze §2 er 5 eist — dat probleem verdwijnt.
            ("Laaddock 乐友新能源材料（无锡）— westgevel",      (120.47518, 31.52362)),
        ],
        "id": "li-zjg-wuxi",
        "naam": "poort Tianqi (Jiangsu) → laaddock LG Chem/Huayou Wuxi "
                "(东新路 → 常金线 X301 → 东海路 → S23 靖张高速 → G4221 沪武高速 → "
                "张家港枢纽 → S19 通锡高速 → 新鸿路 X252)",
        "extracts": ["china"],
        # ⚠️ X301 BEWUST NIET IN refs: 锡甘线 bij Wuxi draagt dezelfde ref en zou
        #    het staartstuk naar zich toe trekken. (Gemeten: X301 er tóch bij
        #    zetten verandert exact niets — 67,955 km, identiek. De waarschuwing
        #    is dus overbodig maar onschadelijk.) De S19-ways met ref "S19;S58"
        #    matchen gewoon, want _wegen_graaf splitst op ";".
        "refs": ["S23", "G4221", "S19", "X252"],
        # De brief-waarde, NIET onze eigen meting — anders is de toets tautologisch.
        "gepubliceerdKm": 70,
        "bronnoot": "brief been 6 (±70 km) tegen een eigen Dijkstra over "
                    "china-latest (2026-08-05) langs de snelwegcorridor "
                    "S23 → G4221 → S19: 67,955 km = -2,9%. Twee keer onafhankelijk "
                    "gereproduceerd. Het afstand-optimale alternatief over de "
                    "provinciale S259 锡张线 is 61,0 km (-12,9%) — korter maar "
                    "trager (69,9 vs 48,6 min); reëel alternatief, aandeel onbekend",
        "vensterKm": 6,
        "uit": "stroombeen-zhangjiagang-wuxi.geojson",
    },
```

**Verwachte uitvoer (vooraf gemeten met de EIA-staart, twee keer):** 67,955 km · 408 punten ·
`kmAanloopVan` 0,079 · `kmAanloopNaar` 0,199 · wegblokken **东新路 507 · 长江北路 2.337 ·
常金线 X301 3.009 · 东海路 1.333 · S23 18.771 · link 1.292 · G4221 5.088 · 张家港枢纽立交 932 ·
S19 32.868 · link 1.066 · 新鸿路 X252 743 m** · `snoei_keerlussen` 0 · omkeringen ≥150° 0 ·
knikken ≥60° 5.

⚠️ **De staart is verplaatst na die meting.** Met het laaddock in plaats van het EIA-anker
(68,0 m verschil) verwacht je `kmAanloopNaar` ≈ **0,10–0,20** en de totale lengte
**67,9–68,1 km**. Dat is een **verwachting, geen meting** — lees af wat de bake geeft en zet
dát in de brief.

### C3 · Been 7 — profiel `lithium-wuxi-nanjing`

```python
    # ── Routebrief lithium-greenbushes-zhangjiagang, been 7 (2026-08-05) ──
    # FASE E: NCM-kathodepoeder Wuxi → celfabriek LG Energy Solution Nanjing,
    # New Port-campus in de 南京经济技术开发区.
    #
    # DE CORRIDOR IS G42 沪宁高速. OSM draagt hem als ref "G2;G42" met naam
    # 京沪高速 tussen Shanghai en Wuxi, en als ref "G42" naam 沪蓉高速 verder
    # westwaarts — één weg, twee OSM-schrijfwijzen.
    #
    # ⚠️ HET "S38"-ALTERNATIEF IS GEMETEN EN VERWORPEN, twee keer. Wat in Jiangsu
    #    S38 常合高速 heet ligt in OSM als G4221 沪武高速 (805 ways met ref G4221;
    #    slechts 3 ways dragen S38, alle op lon 119,888-119,893 bij Changzhou —
    #    precies de gedeelde-tracé-claim). G4221 ligt op lon 120,4 op lat 31,814-
    #    31,819 (NOORD om Wuxi) en op lon 119,3 op lat 31,72, en nadert Nanjing van
    #    het ZUIDwesten — de verkeerde kant voor de NEDZ op lat 32,16. Gemeten
    #    312,3 km tegen 196,6 km via G42. Verworpen op VORM, niet alleen op lengte.
    # ⚠️ GEEN VIA OP S19 通锡高速. De fabriek ligt er 0,5 km vandaan en de Dijkstra
    #    pakt hem vanzelf. Een via ÓP S19 legde een 180,0-graden keerpunt neer: de
    #    oprit ligt noordelijk van de fabriek, de reis gaat zuidwaarts.
    # ⚠️ VIA-PUNT 8 LIGT BEWUST ÓÓST VAN HET G2503-KNOOPPUNT (dat zit op lon
    #    ≈118,938). Een punt wést ervan gaf 3 km overschiet-en-terug.
    # ⚠️ HET 栖霞大道-VIA LIGT 62 m VAN DE G2503-RIJBAAN, DUS ÓP HET KLAVERBLAD, en
    #    produceert een omkering van 173,6 graden met pad/hemelsbreed 2,08. Dat is
    #    een KNOOPPUNTLUS, geen terugloop (de band voor terugloop is 3,0-10,2), maar
    #    het is wel dezelfde knooppunt-via-regel die op been 8 juist wél is
    #    toegepast. Slaat toets_knikken.py erop aan: schuif dit punt verder
    #    noordwestwaarts ÓP 栖霞大道 en hermeet. Niet vooraf verschuiven — ongemeten.
    # ⚠️ DE KOP IS EEN SUBSTITUUT (de zuidpoort, 310,1 m van het laaddock): welk
    #    dock uitgaand is, is niet gedocumenteerd — b6-staart en b7-kop wezen
    #    anders op DEZELFDE apron en dan is §2b's twee-ankers-eis alleen nominaal
    #    vervuld. Een verzonnen verschil tussen twee docks zou erger zijn.
    #    ⚠️ DE EERSTE ~1 KM IS DAARDOOR NIET VOORGEMETEN: de meting van 196,6 km
    #    liep vanaf het fabrieksanker met een aanloop van 199 m. Verwacht
    #    锡梅路 → 新鸿路 → oprit → S19, dus +0,3 tot +0,6 km. HERMEET.
    # ⚠️ DE STAART IS VERVANGEN. Het briefpunt 32.16300/118.87900 ligt 21,4 m
    #    BUITEN way 621624910, in beboste helling — het was "satelliet-gelegd op
    #    z16" en op 2,0 m/px is dat verschil onzichtbaar. Nieuw: het bbox-midden
    #    van diezelfde way, binnen het hek, 216,0 m van het oude punt.
    "lithium-wuxi-nanjing": {
        "via": [
            ("Zuidpoort 乐友无锡, 锡梅路 (substituut-kop)",  (120.47492, 31.52084)),
            ("G2/G42 京沪高速 — knooppunt 硕放",             (120.45227, 31.50909)),
            ("G42 沪蓉高速 — Wuxi-west / Luoshe",           (120.19721, 31.70953)),
            ("G42 — Changzhou (noord van het centrum)",    (119.98628, 31.84207)),
            ("G42 — Danyang",                              (119.65600, 32.00444)),
            ("G42 — Zhenjiang",                            (119.44875, 32.05524)),
            ("G42 — Jurong 句容",                           (119.19980, 32.04512)),
            ("G42 — Nanjing-oost, vóór knooppunt G2503",   (118.97025, 32.06317)),
            ("G2503 南京绕城高速 — noordwaarts na het knooppunt", (118.95119, 32.10188)),
            ("栖霞大道 S338 — ná de afrit 栖霞",               (118.94392, 32.14829)),
            ("LG ES Nanjing — terreinanker New Port",      (118.87953, 32.16111)),
        ],
        "id": "li-wuxi-nanjing",
        "naam": "laaddock/zuidpoort LG Chem-Huayou Wuxi → LG Energy Solution "
                "Nanjing, New Port (S19 通锡 → G42 沪宁高速 → G2503 南京绕城 → "
                "栖霞大道 S338)",
        "extracts": ["china"],
        # G2 matcht het element "G2" in de OSM-ref "G2;G42"; G25 hoort bij G2503
        # (die ring draagt "G25;G2503"). Zachte voorkeur, factor 3.
        "refs": ["G42", "G2", "G2503", "G25", "S338"],
        "gepubliceerdKm": 180,
        "bronnoot": "brief been 7 (±180 km); onafhankelijk: gepubliceerde "
                    "wegafstanden Wuxi→Nanjing centrum-tot-centrum 174-185 km en "
                    "沪宁高速 is 274 km lang. Eigen corridormeting 196,6 km ruw / "
                    "196,3 na snoei = +9,1% — verklaarbaar doordat beide ankers "
                    "voorbij de stadscentra liggen (fabriek in Xinwu/硕放, campus "
                    "in de NEDZ aan de Yangtze). ⚠️ KRAP BINNEN ±10%: dit is het "
                    "eerste getal dat kantelt, en de kop IS verschoven — hermeet",
        "vensterKm": 40,
        "uit": "stroombeen-wuxi-nanjing.geojson",
    },
```

**Verwachte uitvoer (voorgemeten met de VERVALLEN uiteinden, twee keer onafhankelijk):**
196,6 km ruw → **196,3 km na snoei** (3 keerlussen) · 2 omkeringen ≥150° met pad÷hemelsbreed
**2,42 en 2,08** (beide klaverbladlussen) · `kmAanloopVan` 0,199 · `kmAanloopNaar` 0,100 ·
alle via-punten 0,2–0,7 m van een motorway met de juiste ref, geen enkele op een
`motorway_link`, geen enkele op een plaatsknoop.
**Met de nieuwe kop en staart:** verwacht **195–199 km**, `kmAanloopVan` ≈ 0,08 (锡梅路 op
79,1 m), `kmAanloopNaar` ≈ **0,012** (way 1303627568 op 12,3 m). Puntental niet voorgemeten.

⚠️ **De aanloop naar Nanjing is een KEUZE, geen meetresultaat — en dat hoort in de brief.**
Binnen hetzelfde venster (40 km) en met alleen de refs-whitelist eraf meet de vrije Dijkstra:
Jurong → LG Nanjing **40,7 km** via G42 → G346 → 宝华大道 → 仙林东路/仙林大道 → 天佑路 →
栖霞大道, tegen **48,0 km** via G2503 — over het hele been **183,7 tegen 196,6 km = −6,6 %**.
Er is **geen bron** aangehaald voor een vrachtbeperking in Nanjing (anders dan voor Shanghai).
Het argument "G2503 heeft maar één NEDZ-afrit" zegt iets over G2503, niet waaróm je op G2503
zit. **Neem de Xianlin-variant op als reëel alternatief in §4 van de brief** (aandeel
onbekend) en noteer waarom de expressweg-variant gekozen is (doorgaande snelweg tot de laatste
afrit, minder stadswegen voor een 15-meter-trekker). Dit is de "even plausibele andere route
die niemand heeft uitgesloten" — laat hem niet stil verdwijnen.

⚠️ **De laatste ~9 km loopt anders dan A3 beschreef.** Met de echte `EIND_STRAAL_KM = 12`
(A3 rekende met 8) loopt de last mile over **仙新东路 / 兴漓路 / 恒泰路 / 恒谊路**, niet over
宏运路 / 杨家边路 (die horen bij de alternatieve route). Schrijf de wegblokken op die de bake
werkelijk geeft.

### C4 · Been 8 — profiel `lithium-nanjing-shanghai`

```python
    # ── Routebrief lithium-greenbushes-zhangjiagang, been 8 (2026-08-05) ──
    # FASE E, slot: 2170-cellen van LG ES Nanjing naar Tesla Giga Shanghai,
    # poort 3, 江山路 5000号, 南汇新城镇, Lingang/Pudong. HET EINDE VAN DE KETEN.
    #
    # DE CORRIDOR: G42 沪宁高速 OOSTWAARTS TOT JIADING, DAARNA G1503 上海绕城高速
    # MET DE KLOK MEE OM SHANGHAI HEEN (Qingpu → Songjiang → Jinshan → Fengxian →
    # Lingang), en pas op het laatst 新四平公路 G228 → 江山路 → poort 3.
    #
    # ⚠️ ER GELDT EEN VRACHTVERBOD DOOR HET CENTRUM, EN DAT STUURT DE ROUTE.
    #    Blauwe-plaat vrachtwagens mogen de hele dag niet binnen de binnenring;
    #    sinds 15-10-2025 mogen diesel-vrachtwagens Euro-IV de hele dag niet
    #    binnen G1503, met S20 外环 als aanbevolen omleiding. Deze lijn blijft
    #    31,34 km van 人民广场 — gemeten. Ter vergelijking: een VRIJE Dijkstra
    #    komt op 14,7 km en gaat dus wél de verbodszone in, en is 30 km korter.
    #    Dát verbod is de reden dat we die kortere route niet nemen.
    # ⚠️ VIER ARCS GEMETEN vanaf het knooppunt G42 x G1503 (121,139/31,290):
    #    G1503-zuidwest 108,1 km · S32 申嘉湖 119,7 · S20 外环 + S2 沪芦 122,2 ·
    #    oostelijke arc via Pudong 131,0. De zuidwestarc wint op lengte, ligt het
    #    verst van de verbodszone en raakt als enige de brief-passage Songjiang.
    #    ⚠️ S20+S2 IS GEEN SCHOON ALTERNATIEF: die route komt op 10,9 km van
    #    人民广场 en ligt dus RUIM BINNEN G1503 — hij schendt precies het
    #    Euro-IV-verbod waarmee de gekozen arc wordt gerechtvaardigd. Noem hem in
    #    de brief alleen mét dat voorbehoud.
    # ⚠️ VIA-PUNT 17 LIGT OP 新四平公路 G228, NIET OP HET G1503-KNOOPPUNT 临海路.
    #    Gemeten: een via ÓP dat knooppunt (121.76188, 30.92297) legde een keerlus
    #    van 5,49 km over 41 punten neer. Ná de afslag → 0 keerlussen en het been
    #    381,9 → 376,1 km. Dezelfde les als Joplin/Lenexa.
    # ⚠️ VIA-PUNT 11 IS KUNSHAN EN NIET ANTING. G42 buigt tussen lon 121,14 en
    #    121,16 naar het zuiden; een via bij Anting (121,157/31,272) ligt in
    #    reisrichting VOORBIJ het G1503-knooppunt (121,139/31,290).
    # ⚠️ "G228" staat in refs voor de laatste 3,7 km, maar G228 loopt langs de hele
    #    Chinese kust en parallel aan G1503 tussen Jinshan en Lingang. Buigt de
    #    lijn daar raar af, dan is dit de eerste verdachte.
    # ⚠️ DE KOP IS EEN SUBSTITUUT (hoofdpoort 恒谊路, 301,4 m van het terreinanker):
    #    de uitgaande laadplek van de celfabriek is niet gevonden (werkorder F3).
    # ⚠️ DE STAART IS VERVANGEN EN DIT IS DE BELANGRIJKSTE CORRECTIE VAN DE HELE
    #    RONDE. Het briefpunt 30.87390/121.76572 is HET REKENKUNDIG MIDDEN VAN VIER
    #    OSM-BUSHALTENODES (12376922502..505, alle highway=bus_stop resp.
    #    public_transport=platform/stop_position, bus=yes; gemiddelde 30.873906/
    #    121.765716). Het ligt 1,0 m van de PUBLIEKE straat 正嘉路 op de WESToever
    #    van het kanaal en 60,9 m BUITEN way 635670279. Er is geen barrier=gate en
    #    geen entrance=* binnen 1,8 km. Elk "bewijs" dat dat punt goed snapt is
    #    CIRCULAIR: het meet het anker tegen één van de nodes waaruit het gemiddeld
    #    is. De echte poort ligt 97,8 m verderop, over de brug, 18,2 m BINNEN de
    #    fabriekspolygoon.
    # ⚠️ HET LAATSTE STUK IS NIET MEER GECONTROLEERD OP OVERSCHIET-EN-TERUG. Die
    #    controle liep op het oude (bushalte-)eindpunt. 正嘉路 (way 1338068671) heeft
    #    5 vertices over 869 m; de nieuwe staart hangt aan way 1229490502. CONTROLEER
    #    dit opnieuw — loopt het been over precies één benoemde way voorbij de poort,
    #    dan is knip_osm_been.py hier wél inzetbaar (anders dan bij been 5).
    "lithium-nanjing-shanghai": {
        "via": [
            ("Hoofdpoort LG ES Nanjing, 恒谊路 (substituut-kop)", (118.87950, 32.15840)),
            ("栖霞大道 S338 — vóór de oprit G2503",           (118.94392, 32.14829)),
            ("G2503 南京绕城高速 — zuidwaarts",                (118.95119, 32.10188)),
            ("G42 沪蓉高速 — Nanjing-oost (Qixia)",           (118.97025, 32.06317)),
            ("G42 — Jurong 句容",                            (119.19980, 32.04512)),
            ("G42 — Zhenjiang",                              (119.44875, 32.05524)),
            ("G42 — Danyang",                                (119.65600, 32.00444)),
            ("G42 — Changzhou",                              (119.98628, 31.84207)),
            ("G42 — Wuxi",                                   (120.19721, 31.70953)),
            ("G2/G42 京沪高速 — Suzhou",                       (120.59967, 31.35006)),
            ("G2/G42 — Kunshan (vóór knooppunt G1503)",      (120.99984, 31.33419)),
            ("G1503 上海绕城高速 — zuidwaarts na Jiading",      (121.14262, 31.24131)),
            ("G1503 — Qingpu",                               (121.13800, 31.14649)),
            ("G1503 — Songjiang",                            (121.14908, 31.01539)),
            ("G1503 — Jinshan / Fengxian (zuidkust)",        (121.29025, 30.87814)),
            ("G1503 — Fengxian-oost",                        (121.60383, 30.91048)),
            ("新四平公路 G228 — ná de afrit Lingang",          (121.73564, 30.88459)),
            ("江山路 — westzijde Tesla-terrein",               (121.75945, 30.87586)),
            ("Tesla Giga Shanghai — poort 3 (brug + wachtersgebouw)", (121.76667, 30.87423)),
        ],
        "id": "li-nanjing-shanghai",
        "naam": "LG Energy Solution Nanjing → Tesla Giga Shanghai poort 3 "
                "(G2503 → G42 沪宁高速 → G1503 上海绕城 → G228 新四平公路 → 江山路)",
        "extracts": ["china"],
        "refs": ["G42", "G2", "G2503", "G25", "G1503", "S338", "G228"],
        # ⚠️ DE BRIEF-WAARDE ±300 KM IS DE GROOTCIRKEL EN MOET UIT DE BRIEF:
        #    poort-tot-poort is hemelsbreed 308,68 km (nagerekend), dus een
        #    wegafstand van 300 km is onmogelijk.
        "gepubliceerdKm": 376,
        "bronnoot": "eigen corridormeting 2026-08-05 over china-latest.osm.pbf, "
                    "twee keer onafhankelijk gereproduceerd: 376,1 km ruw / 375,6 "
                    "na snoei. ⚠️ TAUTOLOGISCHE LENGTETOETS — er is geen bron die "
                    "deze rit documenteert. Onafhankelijke kruiscontrole: "
                    "gepubliceerd Nanjing→Shanghai-centrum 297-305 km, Lingang ligt "
                    "daar nog ~70 km voorbij, plus de ringomleiding → ~370-380 km. "
                    "De brief-waarde ±300 km is de GROOTCIRKEL (308,68 km "
                    "hemelsbreed poort-tot-poort)",
        "vensterKm": 40,
        "uit": "stroombeen-nanjing-giga-shanghai.geojson",
    },
```

**Verwachte uitvoer (voorgemeten met de VERVALLEN uiteinden, twee keer onafhankelijk):**
376,1 km ruw → **375,6 km na snoei** (16 keerlussen) · 4 omkeringen ≥150° met pad÷hemelsbreed
**1,96 · 2,08 · 2,42 · 2,66** (alle vier knooppuntlussen) · `kmAanloopVan` 0,100 ·
`kmAanloopNaar` 0,009 · dekking Songjiang 7,17 km · Changzhou 3,68 km.
**Met de nieuwe kop (510 m zuidelijker) en staart (97,8 m oostelijker, over de brug):**
verwacht **374–378 km**, `kmAanloopVan` ≈ 0,035 (恒谊路 op 34,5 m), `kmAanloopNaar` ≈ **0,003**
(way 1229490502 op 3,3 m). Puntental niet voorgemeten.

⚠️ **De omkering van 153,0° bij 31,01827/121,15034** (G1503-knooppunt bij Songjiang) heeft
pad÷hemelsbreed **2,66** — tussen "echte bocht" (1,1–2,0) en "terugloop" (3,0–10,2) in.
Beoordeel hem op het **gebakken** bestand met `toets_knikken.py`. Verplaatsen van het
Songjiang-via naar (121.13557, 31.04141) haalt hem weg voor +0,2 km — keuze voor Lars, niet
vooraf doen.

### C5 · Het complete bak-recept

Dit hoort letterlijk in `v2/tools/bak_stromen.sh`, naast `bak_koper_lobito()`, met `lithium`
in de `case`-regel. De waarschuwing onderin dat bestand (regels ~205-209) mag dan voor
**lithium** vervallen; voor `collahuasi-tongling` blijft hij staan.

⚠️ **`--stroom` blijft `lithium-greenbushes-zhangjiagang`.** Dat is tegelijk de bestandsnaam,
de sleutel in `STROMEN` in `v2/src/main.js` en de HUD-knop; wie hem "netter" maakt breekt de
browser. **Alleen de `--titel` verandert.**

```bash
# ── lithium · Greenbushes → Bunbury → zee → Yangtze → Zhangjiagang → Tianqi →
#    Wuxi → Nanjing → Tesla Giga Shanghai
# Routebrief: v2/design/routebrieven/lithium-greenbushes-zhangjiagang.md (A–E)
# Werkorder:  v2/design/werkorder-lithium-benen-5-8.md
#
# ⚠️ BENEN 1-4 GERECONSTRUEERD 2026-08-05, NIET TERUGGEVONDEN — maar strak
#    vastgelegd: dit commando reproduceerde het bestand van 30-07 TEKEN VOOR TEKEN
#    (52.821 byte, gelijke sha256 na normalisatie van `gemaakt`; 5 benen, 2.576
#    punten, 4 markers), twee keer onafhankelijk nagedraaid. Het bewijs blijft
#    "dit commando produceert dat artefact", nooit "dit was het commando".
# ⚠️ DRIE VRIJHEIDSGRADEN, ALLE DRIE GEMETEN — en anders dan bij Lobito is --graaf
#    hier WÉL vrij:
#      * --graaf mississippi of rijn geeft hetzelfde bestand. Reden is meetbaar:
#        het zeebeen rapporteert 0 track-edges · 46 MARNET-edges · 0 connectors,
#        en beide track-graven liggen aan de andere kant van de wereld. Tóch
#        pinnen: een graaf die deze route wél dekt kan het antwoord veranderen.
#      * de --been-uiteinden mogen het ANKER of het ROUTEERPUNT zijn (snap 4,933
#        vs 4,774 km resp. 13,018 vs 14,460 km, telkens dezelfde knoop).
#      * --vermijd northwest of leeg: identiek. Default laten staan.
#
# ⚠️ HERKOMST VAN DE ZES --been-geojson-BESTANDEN (build-cache is gitignored, dus
#    op een verse clone draait dit niet — geldt voor álle recepten in dit bestand):
#      stroombeen-greenbushes-bunbury.geojson
#          python v2/tools/maak_stroombeen_weg.py --profiel lithium-greenbushes-bunbury
#      rivierbeen-yangtze-zhangjiagang.geojson
#          python v2/tools/maak_rivierbeen.py --marnet "$MARNET" \
#              --van 31.4512,121.4769 --naar 31.9715,120.3812
#          ⚠️ EN DAARNA GEKNIPT, MET EEN GEREEDSCHAP DAT NIET BESTAAT. Gemeten: het
#             ongeknipte been is 139,1 km / 712 punten / 19 edges; het bestand op
#             schijf is exact de eerste 693 punten daarvan, afgekapt op index 692
#             (590,0 m van het kade-anker). Zonder die knip loopt het been 3,69 km
#             voorbij de kade door. ⚠️ `--naar` is ONDERBEPAALD: 31.9733,120.4202
#             en 31.968,120.4205 geven allebei een pad waarvan de eerste 693 punten
#             identiek zijn aan het bestand op schijf.
#      stroombeen-zhangjiagang-lastmile / -wuxi, stroombeen-wuxi-nanjing,
#      stroombeen-nanjing-giga-shanghai.geojson
#          python v2/tools/maak_stroombeen_weg.py --profiel <naam>  (zie werkorder C)
#
# ⚠️ HET GAT VAN 4.933 m TUSSEN BEEN 1 EN BEEN 2 BLIJFT BEWUST OPEN, en het is het
#    grootste van alle vijf stromen (volgende: collahuasi-tongling 1.818 m). Het is
#    GEEN fout uiteinde: -33.30640/115.61330 is MARNET's eigen Bunbury-knoop en de
#    eerstvolgende zeeknoop ligt 92,804 km verderop. Een rechte stippel zou de
#    Nacala-fout zijn — gemeten ligt 3,779 km van de 4,933 km (76,6%) over land,
#    dwars over het schiereiland van Bunbury. Een haven-aanloop uit detour() is
#    óók geen oplossing: het 1:10M-landmasker is daar LOKAAL OMGEKEERD (werkorder
#    F2). Eerst de vaargeul satelliet-leggen, dán een aanloop uit handmatig
#    gelegde punten — de Tongling-regel.
#
# ⚠️ DRIE PROCESGATEN ZIJN BEWUST ZICHTBAAR (werkorder F3): de uitgaande laadplekken
#    bij Tianqi (219 m), Wuxi (310 m) en Nanjing (301 m) zijn NIET GEVONDEN. De
#    koppen van b6/b7/b8 zijn substituten. Die gaten ZIJN de ontbrekende ankers;
#    dichttrekken is de Waalhaven-klasse.
bak_lithium() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|truck Greenbushes → Bunbury Berth 8 (Maranup Ford Rd → South Western Hwy)|$BEEN/stroombeen-greenbushes-bunbury.geojson" \
    --been         "zee|zeeschip Bunbury → Yangtze-monding|-33.31995,115.66385|31.4074,121.4848" \
    --stippel      "zee|overgang zeenet → Yangtze-bulklaag (MARNET houdt hier op)|31.51,121.4187|31.4512,121.4769" \
    --been-geojson "binnenvaart|Yangtze-monding → Zhangjiagang, zuidgeul langs Shuangshan-eiland|$BEEN/rivierbeen-yangtze-zhangjiagang.geojson" \
    --stippel      "binnenvaart|aanloop naar de ligplaats (anker ≠ routeerpunt)|31.9733,120.4202|31.968,120.4205" \
    --been-geojson "truck|last mile kade → poort Tianqi (常金线 X301 → 长江北路 → 东新路)|$BEEN/stroombeen-zhangjiagang-lastmile.geojson" \
    --been-geojson "truck|carbonaat/hydroxide Tianqi → kathodefabriek Wuxi (S23 → G4221 → S19)|$BEEN/stroombeen-zhangjiagang-wuxi.geojson" \
    --been-geojson "truck|kathodepoeder Wuxi → LG ES Nanjing (G42 沪宁高速 → G2503 → 栖霞大道)|$BEEN/stroombeen-wuxi-nanjing.geojson" \
    --been-geojson "truck|2170-cellen Nanjing → Tesla Giga Shanghai poort 3 (G42 → G1503 上海绕城 → G228 → 江山路)|$BEEN/stroombeen-nanjing-giga-shanghai.geojson" \
    --marker "Greenbushes — concentraatloods (laadplek)|-33.86495,116.05505" \
    --marker "Bunbury — Berth 8, scheepslader|-33.31995,115.66385" \
    --marker "Yangtze-monding — overgang zeenet → rivier|31.45120,121.47690" \
    --marker "Zhangjiagang — kade Zhangjiagang Port Group (ertsen/hout/staal)|31.96800,120.42050" \
    --marker "天齐锂业（江苏）— poort 东新路 5 (uitgaande laadplek open)|32.01218,120.45771" \
    --marker "乐友新能源材料（无锡）— laaddock westgevel|31.52362,120.47518" \
    --marker "乐友新能源材料（无锡）— zuidpoort 锡梅路 (uitgaand, substituut)|31.52084,120.47492" \
    --marker "LG Energy Solution Nanjing — New Port-campus|32.16111,118.87953" \
    --marker "LG Energy Solution Nanjing — hoofdpoort 恒谊路 (uitgaand, substituut)|32.15840,118.87950" \
    --marker "Tesla Giga Shanghai — poort 3 (losplek binnen het terrein open)|30.87423,121.76667" \
    --routebrief v2/design/routebrieven/lithium-greenbushes-zhangjiagang.md \
    --uit    v2/data/stroomroute-lithium-greenbushes-zhangjiagang.json \
    --stroom lithium-greenbushes-zhangjiagang \
    --titel  "Lithium · Greenbushes → Zhangjiagang → Tesla Giga Shanghai (spodumeen SC6.0 → 2170-cel)"
}
```

**Per vlag de reden.** `--graaf/--marnet/--ne` = de drie vaste invoerpaden (`--marnet` wijst
naar `build-cache/marnet-preais`, **nooit** naar `v2/data/`). `--been-geojson` 1 = het
OSM-wegbeen van fase A, doorgetrokken en niet over deze graaf geroutet. `--been` 2 = het enige
**geroutete** been (vrij over MARNET, 46 edges, 785 punten, 7.606,6 km = 1,052× grootcirkel).
`--stippel` 3 = het **gemeten** gat tussen MARNET's laatste zeeknoop en de bulklaag (8,6 km,
werkwijze §7). `--been-geojson` 4 = de rivierbulklaag, doorgetrokken want echte
riviergeometrie. `--stippel` 5 = anker ≠ routeerpunt bij de ligplaats (0,6 km).
`--been-geojson` 6 t/m 9 = de vier nieuwe wegbenen, doorgetrokken. **Tien markers**, want zodra
er één `--marker` staat vervangt die lijst de automatische afleiding volledig.

**Resultaat: 9 benen · ≈ 8.484 km (band 8.481–8.489) · ≥ 3.035 punten · 10 markers.**
Nieuw t.o.v. de huidige 5 benen / 7.834,1 km: +10,26 (b5) +67,96 (b6) +≈196,3 (b7) +≈375,6
(b8) km.

---

## D · Wijzigingen in `lithium-greenbushes-zhangjiagang.md`

| sectie | wat er moet gebeuren |
|---|---|
| **kop / statusregel** | "status brief: concept" → **"fasen A–E getekend; drie uitgaande laadplekken open (substituut-koppen, 2026-08-05)"** |
| **nieuw blok onder de kop** | *De substituut-notitie*: b6, b7 en b8 beginnen op een **poort** of **terreinpunt**, niet op de laadplek; de gaten van **219 / 310 / 301 m** zijn de ontbrekende ankers. Been 8 eindigt op de **poort**, niet op het terrein. Doorgetrokken, niet gestippeld — het net reikt tot op 3 tot 126 m |
| **§1 ketenkaart** | ASCII-schema bijwerken: b5 **±10 km** (niet ±4), b8 **±375 km** (niet ±300); b5 loopt naar de **poort** 东新路 5, b8 naar **poort 3** en niet naar het terrein |
| **§2a-3 (kade Zhangjiagang)** | ⚠️ **Conflict opnemen**: de ene pass ziet ommuurde bulkbakken 50 m achter de apron, de andere containerstapels en houtstapels. Beslis *bulk of container* — dit is een vraag aan de brief, niet aan de satelliet (**F12**) |
| **§2a-4 (Tianqi)** | stap 6 invullen: **32.01218, 120.45771**, satelliet-gelegd z18 — ⚠️ mét de statuswaarschuwing dat dit een **vestigingspunt aan 东新路** is en geen gekarteerde deur. Uitsluitingen erbij: chemiesteigers 32.01100/120.45250 (0,6 km, **alleen voor het schip**) |
| **§2a-5 (Wuxi)** | stap 6 invullen: laaddock **31.52362, 120.47518** (z19, twee rode opleggers onder een laadluifel) + zuidpoort **31.52084, 120.47492**. De vier EIA-grenzen (kanaal 伯渎港 noord, 锡梅路 zuid, 新鸿路 west, 通锡高速 oost) kloppen 1-op-1 met het beeld |
| **§2b overslagtabel** | rij 2: vertrekanker Zhangjiagang = **havenpoort 31.96245/120.42078**; rij 3: Tianqi krijgt poort **én** substituut-terreinanker mét het gat van 219 m; rij 4 wordt **twee** rijen (Wuxi en Nanjing), elk met losplek + substituut-vertrekanker; **nieuwe rij 5**: Giga Shanghai, aankomstanker = poort 3, **losplek niet gevonden** |
| **§2b routeerpunten** | ⚠️ **Bunbury-toleranties corrigeren**: "verwachte maximale snap 300 m" → **4.933 m gemeten** (B1) |
| **been 3** | "max snap 2 km" → **13.018 m gemeten** (B1) |
| **been 5** | volledig herschrijven: lengte **10,26 km** (niet ±3–5), corridor bij naam **西五节桥街 → 中兴北路 → 常金线 X301 → 长江北路 → 东新路**, kop = kade met een **aanloop van 0,555 km onbekarteerd haventerrein** (0 highway-ways in OSM binnen het terminalterrein), staart = poort mét de overschiet van 75 m |
| **been 6** | lengte **67,96 km** tegen ±70 = −2,9 %; corridor **S23 靖张高速 → G4221 沪武高速 → 张家港枢纽立交 → S19 通锡高速**; kop = **substituut** (poort i.p.v. laadplek); staart = **laaddock**. Reëel alternatief: **S259 锡张线, 61,0 km, aandeel onbekend**. ⚠️ De G2-claim uit de eerste ronde **niet** overnemen (C2) |
| **been 7** | lengte **≈196 km** tegen ±180 = +9,1 % (krap); corridor **G42 沪宁高速 → G2503 南京绕城 → 栖霞大道 S338**; **S38/常合高速 verworpen op vorm** (312,3 km, nadert Nanjing van het zuidwesten). ⚠️ Nieuw **reëel alternatief**: de Xianlin-aanloop via G346 / 宝华大道 / 仙林大道 — **40,7 tegen 48,0 km**, dus 6,6 % korter over het hele been, en niet uitgesloten |
| **been 7 punt 4** | ⚠️ **32.16300, 118.87900 VERVALT** — 21,4 m buiten de perceelgrens, in beboste helling. Vervangen door **32.16111, 118.87953** (bbox-midden way 621624910, binnen het hek, satelliet-gelegd z18). De campus-tabel eronder draagt **32.16145, 118.87958** — de brief sprak zichzelf al tegen |
| **been 8** | lengte **≈376 km**; ⚠️ **"±300 km" was de grootcirkel** (308,68 km hemelsbreed poort-tot-poort); corridor **G42 → G1503 上海绕城 met de klok mee → G228 新四平公路 → 江山路**; het **vrachtverbod** binnen de binnenring/G1503 opnemen als de reden. Reëel alternatief S20+S2 **mét het voorbehoud** dat die route zélf binnen G1503 ligt |
| **been 8 punt 4** | ⚠️ **30.87390, 121.76572 VERVALT — het is een BUSHALTE.** Vier OSM public-transport-nodes, gemiddelde exact het briefpunt, 1,0 m van de publieke straat 正嘉路 op de westoever, 60,9 m buiten de fabriekspolygoon. Vervangen door **30.87423, 121.76667** (poort 3, 18,2 m binnen way 635670279, satelliet-gelegd z19) |
| **been 8 punt 5** | ⚠️ **30.87358, 121.76849 is een BBOX-CENTROÏDE**, geen gekarteerd punt: het is tot op de vijfde decimaal het midden van de bbox 30.86643,121.76440 .. 30.88073,121.77258 van way 635670279, en het valt op een **haldak**. Bruikbaar als registerknoop, **niet** als losplek. De keten eindigt op de poort |
| **§4 vertakkingen** | nieuwe rij: **爱尔集新能源电池（南京）有限公司 六工厂** (way 676426629, 32.15591/118.88369, 698 m ZO) **en 九工厂** (way 1312600215, 749 m ZW) — twee expliciet LGES-genoemde, genummerde percelen naast het gekozen 乐金化学-blok. Reëel alternatief, aandeel onbekend |
| **§5 openstaande punten** | **sluiten:** punt 5 (de twee Chinese fabrieksadressen — beide gelegd). **Blijft open, scherper:** 5b (welke LG-lijn de 2170-cellen maakt — nu mét de twee 爱尔集-percelen). **Toevoegen:** de drie uitgaande laadplekken (F3) · de Tesla-losplek (F4) · het productconflict bulk-vs-container aan de kade (F12) · welke van de 16 ligplaatsen · hazmat-tijdvensters voor UN2680 op Chinese snelwegen · been-ids ontbreken · de knipstap van het rivierbeen zonder tool |
| **§6a** | volledig herschrijven naar de nieuwe stand (B2 geeft de oude, correcte tussenstand) |
| **§7 wat de kaart tekent** | 9 benen; punt 4 en 5 herschrijven (b5–b8 worden **doorgetrokken** getekend); nieuw punt: de drie procesgaten zijn bewust en benoemd; nieuw punt: het gat van 4.933 m bij Bunbury blijft open mét de reden |
| **§8 checklist** | "elke laadplek satelliet-gelegd" blijft **onafgevinkt** (3 uitgaande laadplekken + de Tesla-losplek ontbreken); "elke overslag heeft twee ankers" mag **met voorbehoud** afgevinkt (drie ervan hebben een substituut) |
| **§9 bronnen** | erbij: OSM ways 1014096488 · 432043510 · 419872749 · 419872745 · 621624910 · 1303627568 · 323626513 · 635670279 · 1229490502 (ODbL) · OSM-nodes 12376922502..505 (de bushaltes) · Esri World Imagery z16–z19 · Shanghai-vrachtverboden (上海本地宝/modiauto, diesel Euro-IV binnen G1503 sinds 15-10-2025) |

**Ook bijwerken buiten de brief:**

* **`v2/design/zoek-chinees-adres-recept.md`** — twee meetvalkuilen erbij: (a) de
  Overpass-spiegel **overpass.osm.ch levert stil een LEEG resultaat voor Chinese bboxen** (het
  is een Zwitserland-instance) — dat leest als "niets gevonden" terwijl het "verkeerde server"
  betekent, dezelfde klasse als het verhuisde MEE-endpoint; `.de` en `kumi.systems` gaven
  herhaald 504/429. (b) **Esri heeft bij Zhangjiagang en Tianqi geen z19** ("Map data not yet
  available"; z19 levert daar **2.521 byte** — exact de bytemaat van de z20-placeholder —
  terwijl Wuxi 10.396, Nanjing 14.846 en Shanghai 14.866 byte echte tegels geven). Dat is de
  **zoomplafond**-faalmodus, net als bij Guixi, en hij vraagt een andere **bron**.
* **`v2/design/routebrief-werkwijze.md` §2** — één zin erbij: *een benoemde OSM-node is geen
  object van het type dat zijn naam suggereert.* `特斯拉3号门` is een bushalte; `贵溪北站` was
  een station-vs-perron-vraag. Een naam is een label, geen rol.
* **`CLAUDE.md`** — de banner noemt voor lithium nog "7.834,1 km / 2.576 punten"; die wordt
  ≈ 8.484 km / ≥ 3.035 punten.

---

## E · Volgorde en controlepunten

### 0 · Nulmeting (vóór je iets aanraakt)

```bash
PYTHONIOENCODING=utf-8 python v2/tools/toets_knikken.py > /tmp/knikken-voor.txt
sha256sum v2/data/stroomroute-*.json v2/data/aansluitingen.json \
          v2/build-cache/ais/graaf/stroombeen-*.geojson
PYTHONIOENCODING=utf-8 python v2/tools/maak_aansluitingen.py   # zónder --schrijf: 27/27 op 0,0 m
```

Vastgelegde stand van **deze** stroom (nagemeten 2026-08-05, moet exact terugkomen):
**5 benen · 7.834,1 km · 2.576 punten · 4 markers**, benen
`truck 83,1 · zee 7.606,6 · zee 8,6 (stippel) · binnenvaart 135,2 · binnenvaart 0,6 (stippel)`,
laatste punt `[120.4205, 31.968]`, bestandsgrootte 52.821 byte.
`toets_knikken` totaal vóór deze ronde: **159 knikken ≥60°, 25 omkeringen ≥150°, 3 terugloop**
(alle drie in `stroomroute-pilot`). ⚠️ Lees dit zelf af — schrijf het niet over.

### 1 · Vier profielen toevoegen (C1–C4) — en meteen de regressietoets

```bash
for p in grafiet-balama-nacala lithium-greenbushes-bunbury grafiet-vidalia-lastmile \
         grafiet-vidalia-us84 grafiet-vidalia-desoto grafiet-desoto-casagrande \
         koper-guixi-fase-d ; do
  PYTHONIOENCODING=utf-8 python v2/tools/maak_stroombeen_weg.py --profiel "$p"
done
sha256sum v2/build-cache/ais/graaf/stroombeen-*.geojson    # identiek aan stap 0
```

**Eis: alle zeven bestaande geojsons byte-identiek.** Zijn ze dat niet, dan is
`EIND_KLASSEN_DEFAULT` of `WEG_HOUD` geraakt → terug.
⚠️ **Reken op wachttijd.** De scan draait over de volledige **china-latest.osm.pbf (1,5 GB)**,
single-worker en in-proces; b7 en b8 hebben bovendien een venster van 40 km over 200–380 km
corridor. Reken op **minuten tot tientallen minuten per profiel**. Een volledige pyosmium-pass
over datzelfde bestand leverde in deze ronde na 25+ minuten **geen uitvoer** (exit 0, leeg
bestand) — loopt de scan vast, dan is dat een **bevinding**, geen aanleiding om alsnog een
stippel te tekenen.

### 2 · De vier benen bakken en de uitvoer lezen

| been | lengte-eis | aanloop kop | aanloop staart | keerlussen | omkeringen ≥150° |
|---|---|---|---|---|---|
| b5 | **10,26 ± 0,3 km**, 51 punten | **0,555** (⚠️ vlagt >0,5 — correct) | ≤ 0,10 | 0 | 0 |
| b6 | **67,9–68,1 km**, ~408 punten | ≤ 0,10 | 0,10–0,20 | 0 | 0 |
| b7 | **195–199 km** | ≤ 0,10 | ≤ 0,05 | ≤ 3 | 2, ratio 2,0–2,5 |
| b8 | **374–378 km** | ≤ 0,05 | ≤ 0,02 | ≤ 16 | 4, ratio 1,9–2,7 |

**Lengtetoets tegen de brief (±10 %):** b5 10,26 tegen **±10** (tautologisch — zie C1) · b6
67,96 tegen **70** = **−2,9 %** ✓ · b7 ≈196 tegen **180** = **+9,1 %** ⚠️ krap · b8 ≈376 tegen
**376** (tautologisch; kruiscontrole 370–380).
⚠️ **b7 is het enige been dat kan zakken**, en zijn kop is verschoven. Zakt hij: dat is een
bevinding over de kop, niet over de corridor — hermeet vóór je aan de via-punten gaat schuiven.

**Wegblokken controleren** (b5 en b6 zijn voorgemeten, zie C1/C2). Wijkt een blok af, dan
heeft de Dijkstra een andere weg gepakt en klopt de corridornaam in de brief niet meer.

### 3 · Verklikkers op de vier geojsons, vóór het herbakken

* **b5** — elk punt tussen lat 31,955 en 32,015 en lon 120,415 en 120,475; de lijn raakt
  西五节桥街 · 中兴北路 · 常金线 X301 · 长江北路 · 东新路 en **niets anders**.
* **b6** — Shanghai-havengebied ≥ 15 km (verwacht 98,6) · Jiangyin ≥ 10 (17,8) · Suzhou ≥ 15
  (27,6) · Wuxi-centrum (verwacht 15,4 — de corridor passeert Wuxi bewust aan de oostkant).
  ⚠️ **Het chemiesteiger-anker (32.01100/120.45250, 0,6 km) wordt door b5 én b6 geraakt op
  0,43 km.** Dat anker hoort bij **been 4** (het schip mag daar niet lossen), niet bij een
  wegbeen — 长江北路 loopt daar volkomen terecht langs. **Zet de verbodsstraal per been**,
  anders zakt een goede lijn.
* **b7** — G4221 bij Jintan ≥ 15 km (verwacht 34,9) · LG Jiangning ≥ 10 (42,7) ·
  Zhangjiagang-kade ≥ 15 (34,5).
* **b8** — 人民广场 ≥ 15 km (verwacht 31,3) · Yangshan ≥ 20 (39,1) · Zhangjiagang-kade ≥ 15
  (34,5) · LG Jiangning ≥ 10 (42,7). ⚠️ **De bushaltes 特斯拉3号门 gelden alleen als
  EINDPUNT-verbod (0,15 km).** De lijn passeert er op ~62 m langs en dat is correct — een
  passage-straal zou een goede lijn afkeuren, precies de Beilun→Guixi-marge-fout.

**Dekkings-marges per punt in de brief** (default 2 km keurt correcte routes af):
Zhangjiagang stad **≥ 6 km** (gemeten 5,40) · Changzhou **5 km** (3,68) · Qixia **6 km**
(4,23) · Songjiang **10 km** (7,17). Óf vervang het Zhangjiagang-passagepunt door het
dichtstbijzijnde lijnpunt **31.89372, 120.49722** (op de S23).

### 4 · Stroom herbakken (C5) en `bak_stromen.sh` bijwerken

Script en gebakken json in **één commit** — lopen ze uit elkaar, dan is het de
`cu-guixi-spoor`-klasse.

### 5 · Meten aan het GEBAKKEN eindproduct (niet aan de meetlat)

* **9 benen**, totaal **8.484 ± 5 km**, ≥ 3.035 punten, **10 markers**.
* **Gaten tussen de benen** — harde eis: **alle gaten ≤ 0,5 km, met precies twee benoemde
  uitzonderingen:**

| overgang | verwacht | oordeel |
|---|---|---|
| b1/b2 → b3 (Bunbury) | **4.933 m** | ⚠️ **UITZONDERING 1** — anker ≠ routeerpunt; MARNET's eerstvolgende zeeknoop ligt 92,8 km verderop. Blijft open (**F2**) |
| b3 → stippel → b4 → stippel | 0 · 0 · 0 | ✓ |
| stippel → b5 (kade) | **555 m** | ⚠️ **UITZONDERING 2** — onbekarteerd haventerrein: 0 highway-ways binnen het terminalterrein van Zhangjiagang Port Group |
| b5 → b6 (Tianqi) | **0 m** | ✓ beide benen hangen aan dezelfde graafknoop |
| b6 → b7 (Wuxi) | **≈ 0,32 km** | ✓ onder 0,5 — **procesgat**: laaddock → zuidpoort, 310 m |
| b7 → b8 (Nanjing) | **≈ 0,34 km** | ✓ onder 0,5 — **procesgat**: terreinanker → hoofdpoort, 301 m |

  **Groeit of verschuift een van de twee uitzonderingen: er is iets misgegaan. Verdwijnt een
  procesgat: het anker is gevonden. Een derde uitzondering is een fout.**
* **Markers ≤ 0,15 km van de lijn — en meet punt-tot-SEGMENT, niet punt-tot-vertex.**
  ⚠️ Dit is een echte meetfout uit de koper-ronde (Guixi stond als 16 m genoteerd terwijl het
  segment 0,8 m was en de vertex 48,9 m). Verwacht: Greenbushes 0,06 · Berth 8 0,08 ·
  Yangtze-monding 0 · Zhangjiagang-kade 0 · **Tianqi-poort 0,025** · **Wuxi-laaddock ≈ 0,13**
  ⚠️ krap · **Wuxi-zuidpoort ≈ 0,08** · **Nanjing-campus ≈ 0,012** · **Nanjing-hoofdpoort
  ≈ 0,035** · **Tesla poort 3 ≈ 0,003**.
  ⚠️ **De havenpoort van Zhangjiagang (31.96245/120.42078) staat bewust NIET in de
  markerlijst**: hij ligt ~234 m van het eerste lijnpunt en zou de eis breken. Hij hoort in de
  brief en in sectie A, niet op de bol.
* **`toets_knikken.py` en diff tegen `/tmp/knikken-voor.txt`** — **de vier andere stromen
  moeten letterlijk ongewijzigd zijn**. Een nieuwe omkering daar is een bevinding, geen ruis.
  ⚠️ De 150°-drempel is op **spoor** geijkt, waar een trein fysiek niet kan omkeren; b5–b8 zijn
  weg. Beoordeel elke nieuwe omkering met **pad ÷ hemelsbreed** (terugloop 3,0–10,2; echte
  bocht/knooppuntlus 1,1–2,7), niet met de drempel alleen. Verwacht: **+6 omkeringen** in de
  lithiumstroom (2 op b7, 4 op b8), alle met ratio 1,9–2,7 = knooppuntlussen.

### 6 · `aansluitingen.json` regenereren (B6)

Eisen: **31 aansluitingen**, de 27 bestaande op **0,0 m** ongewijzigd. Lees de vier nieuwe
snaps af en beslis daarná pas over `modi` — geef geen modus op goed geluk.

### 7 · `?v=`-bump (B8), brief bijwerken (D), pushen

Stuur daarna de klikbare Pages-URL **mét het nieuwe `?v=110`** mee (telefoon + 10 min cache).

### 8 · Wrapup volgens de Definition of Done

Linear, vault, project-`memory/`. Zet in `memory/next-actions.md`: (a) het recept van
`collahuasi-tongling` staat nog steeds nergens; (b) **been-ids ontbreken in álle vijf gebakken
stromen**; (c) het gat van 4.933 m bij Bunbury en van 1.818 m bij `collahuasi-tongling` wachten
op dezelfde behandeling — en die behandeling is **niet** `maak_havenaanloop.py` (zie F2).

---

## F · Wat NIET af komt

### Bevindingen die de weerlegger NIET houdbaar vond (verplicht hier, niet weggelaten)

**F1 · A3 "corridors b7/b8" — niet houdbaar op de anker- en last-mile-lens.** De weerlegger
reproduceerde de corridorgeometrie tot op de decimaal (196,6 / 376,1 km, alle 21 via-punten op
de doorgaande rijbaan, S38/G4221 verworpen, vier arcs gemeten) — **die metingen zijn in sectie
C overgenomen als de meting van de weerlegger, niet als A3's claim** (besluit 2 boven C0). Wat
brak:

1. **Het staartanker is een bushalte, en het bewijs ervoor was circulair.** A3 voert aan: *"de
   router snapt op (30.873976, 121.765731) = 9 m, aanloop staart 9 m, GEEN
   overschiet-en-terug"* — maar die coördinaat is één van de **vier bushaltenodes waaruit het
   anker rekenkundig is gemiddeld**. De "twee vertices van 正嘉路 op 8,3 en 8,9 m" zijn
   diezelfde nodes. A3 degradeerde de ontbrekende satellietpass tot *"de corridor verandert er
   niet door, alleen de status"*; die pass is gedraaid en laat het tegendeel zien — het punt is
   **niet van het type dat de brief claimt**, en het is het **laatste punt van de hele
   A–E-keten**.
2. **De Nanjing-aanloop van been 7 is niet uitgesloten.** Binnen A3's eigen venster geeft de
   vrije Dijkstra 40,7 km via Xianlin tegen 48,0 via G2503 (−6,6 % over het been). A3 voert
   "de vrije Dijkstra kiest vanzelf" wél aan aan de Wuxi-kant (S19) maar past hem niet toe aan
   de Nanjing-kant, waar hij een ándere corridor aanwijst.
3. **Vier kleinere scheuren.** Het 栖霞大道-via ligt 62 m van de G2503-rijbaan (dus ÓP het
   klaverblad) en produceert een omkering van 173,6° — precies de knooppunt-via-regel die A3
   voor been 8 zelf formuleert, niet toegepast op been 7. Het "reële alternatief" S20+S2 komt
   op 10,9 km van 人民广场, dus **binnen G1503**, en schendt het verbod waarmee de gekozen arc
   wordt gerechtvaardigd. A3 rekende met een eindstraal van 8 km terwijl de tool 12 gebruikt,
   en beschrijft daardoor een last mile die de echte bake niet produceert. En in het
   machineleesbare puntenveld staat `lat: 50.909` waar 31.50909 hoort.

*Wat het zou oplossen:* een bron die de uitgaande cellenstroom aan één poort/dock van de
LG-campus koppelt, en een Nanjing-vrachtbeperking (of het ontbreken daarvan) waarmee de
Xianlin-variant te verwerpen of te aanvaarden is.

**F2 · A4 deel (b) "haven-aanloop Bunbury" — niet houdbaar: de landkaart is daar lokaal
omgekeerd.** `maak_havenaanloop.py` is een dunne aanroeper om `bake_marnet.detour()`, en die
routeert over de 1:10M-landpolygonen. Die maskerwaarden zijn bij Bunbury **omgedraaid**,
gemeten tegen eigen passes:

| punt | werkelijkheid (eigen pass) | 1:10M-masker |
|---|---|---|
| −33.30500, 115.65200 | **bulkcarrier onder stoom, kielzog** | **LAND** |
| −33.31500, 115.65900 (binnenhavenmond) | water | **LAND** |
| −33.30800, 115.68500 (Leschenault Inlet) | water | **LAND** |
| −33.29950, 115.64400 (havendam-tip) | steen/land | **water** |
| −33.30245, 115.67330 ("The Cut") | duin + getijgeul | **water** |
| −33.29000, 115.68000 (barrièreduin) | **land** | **water** |

Gevolgen: (i) het pad **kán per constructie niet** door de vaargeul lopen die de satelliet
bewijst, dus de aangevoerde navigatorische bevestiging is onmogelijk; (ii) "0,00 km land
midden op de lijn" is gemeten tegen datzelfde foute masker én `over_land_km(split=True)` sluit
segment 0 en n−2 per constructie uit — terwijl **álle** land in segment 0 zit; (iii) de eerste
hop is geen "kleine knik de baai in" maar **1,5–2,1 km dwars over het haventerrein en de
inlet** naar de keel van een recreatieve getijgeul. Residu-land **14,76 %** tegen **0,58 %**
bij Nacala en **1,37 %** bij Coloso — de precedenten waarop het voorstel zich beroept.

*Wat het zou oplossen:* de vaargeul **satelliet-leggen** (binnenhavenmond ≈ −33.3190/115.6605
→ Koombana Bay ≈ −33.3050/115.6520 → langs de dam-tip → open zee) en de aanloop uit die
**handmatig gelegde** punten bouwen — exact zoals de Tongling-oostgeul is gedaan, en exact de
projectregel *"OSM/1:10M-watervlak is geen waarheid, de satelliet wel"*. Zolang dat niet
gebeurd is, is **het gat als niets tekenen eerlijker** dan een lijn die het haventerrein
oversteekt.

### Niet gevonden — geen coördinaat, geen anker, geen lijn

**F3 · De drie uitgaande laadplekken: Tianqi · Wuxi · Nanjing.** Geprobeerd: 28 eigen
satellietpassen op z16–z19, het nationale emissievergunningregister (geeft één coördinaat per
rechtspersoon, geen installatielijst), het EIA-rapport van de Wuxi-fabriek (levert de vier
四至-grenzen maar geen 成品库/装卸区), Overpass op de perceelpolygonen (geen
`building`-functies, geen `entrance=*`), en Chinese zoektermen op 成品库 / 装卸区 / 出库.
⚠️ **Bij Zhangjiagang en Tianqi kán de satelliet het niet overnemen:** Esri heeft daar **geen
z19** (gereproduceerd op zowel de kade als de fabriek; z19 levert 2.521 byte = de
placeholdermaat). Dat is de **zoomplafond**-faalmodus, dezelfde als bij Guixi, en hij vraagt
een **andere bron** — een terreinplattegrond of EIA-figuur met 成品库/装卸区 — niet een andere
Esri-release. Substituten mét gemeten gat: Tianqi terreinanker 32.01050/120.45650 (219 m) ·
Wuxi zuidpoort 31.52084/120.47492 (310 m) · Nanjing hoofdpoort 32.15840/118.87950 (301 m).

**F4 · De losplek van de 2170-cellen binnen Giga Shanghai.** Er is een **kandidaat**: de
truck-apron aan de NO-gevel op **30.87443, 121.76910** — op z19 een aaneengesloten rij rode,
blauwe en witte opleggers ruggelings tegen het gebouw, met zichtbare dock-luifels en
dock-levellers langs de dakrand; een tweede dockrij langs de NW-gevel. 111,0 m van het
bbox-midden, 233,0 m van de poort. **Maar geen enkele bron wijst DEZE dock aan als de
cel-ontvangst**, en de fabriek heeft er meerdere. Het is de **klasse** die klopt, niet een
gedocumenteerde plek. **Status onzeker, dus geen anker, dus niet in sectie A en niet als
marker.** De keten eindigt op de poort. *Wat het zou oplossen:* een fabrieksplattegrond, een
milieudossier of een leverancierslogistiek-document met een dockaanduiding.

**F5 · Welke LG-entiteit in Nanjing de 2170-lijn draagt — en dit is de zwakste schakel van de
hele ronde.** Zowel b7-staart als b8-kop hangen aan **één** polygoon: OSM-way 621624910, naam
**乐金化学新能源电池有限公司** = "LG **Chem** New Energy Battery" — de naam van **vóór** de
afsplitsing van LG Energy Solution. Binnen 1,3 km liggen echter **twee** percelen die expliciet
naar LG **Energy Solution** zijn genoemd én als **genummerde fabrieken**:
**爱尔集新能源电池（南京）有限公司六工厂** (way 676426629, 8,04 ha, **698,3 m** ZO) en
**九工厂** (way 1312600215, **749 m** ZW). Juist die nummering bevestigt de brief-noot "negen
fabrieken op vijf locaties" (§5 punt 5b) en is dus het sterkste signaal dat de cellijn ergens
**anders** op deze campus staat. Daarnaast noemt de brief zélf een **tweede perceel van
dezelfde naam** op 32.15027/118.88596 dat nergens is behandeld. Het enige harde bewijs dat
overeind blijft is dat **恒谊路** het vrachtadres uit de vrachtdocumenten is en dat de z19-pass
daar het **rode LG-logo-monument** toont — maar dat bewijst *"een LG-poort"*, niet *"de poort
waar de 2170-cellen uitgaan"*. **750 m is groter dan elk procesgat dat deze ronde bewust heeft
laten staan.** *Wat het zou oplossen:* een bron die één van de drie percelen aan de
cilindercel-lijn koppelt.

**F6 · Welke van de 16 ligplaatsen van Zhangjiagang Port Group de spodumeenlading krijgt.**
Onveranderd open (brief §5). Wel scherper: de bulkbakken achter de apron zijn nu gelokaliseerd
(31.96755/120.42051, 50,0 m ZZW van het anker), dus het anker ligt aantoonbaar op een
bulk-sectie — zie echter **F12**.

### Bevindingen uit A1 die NIET worden overgenomen (de weerlegger brak ze)

**F7 · Het "vertuigenveld" op 30.87365, 121.76399 is verkeerd benoemd en krijgt GEEN negatief
anker.** A1 noemt het *"uitgaande autologistiek — honderden geparkeerde auto's in rijen"* en
legt er een verbodsstraal van 0,3 km. De eigen z19-pass (0,26 m/px) toont een
**oplegger-/containeryard**: visgraatrijen trailers van ~12,9 × 2,8 m (gemeten tegen het
gradengrid) met yard-trekkers ertussen — géén personenauto's (die zijn 4,5 m). Dat is
**vracht-staging**, dus juist een plausibele kandidaat voor inkomende cel-opleggers. Netto zou
A1's voorstel een no-go-cirkel over mogelijk het gezochte object leggen. **Niet opnemen.**

**F8 · De coördinaten van de NEDZ-buren als negatieve ankers driften 160–366 m.** Eigen
`out center` per way-id tegen A1: LG Display **365,8 m** (A1 zet hem op 32.15782/118.88466 en
"605,8 m van het campusmidden"; OSM én de brief zelf zeggen 32.15593/118.87780 = **971,4 m**) ·
Autoliv 198,4 · A.O. Smith 263,9 · Heesung 215,9 · 科迈特 160,4 m. A1's claim "alle vier binnen
300 m" meet 498–638 m. Bij LG Display valt de voorgestelde verbodscirkel van 0,4 km daardoor
maar net over het perceel. **Neem deze buren niet als negatieve ankers op** zolang de
coördinaten niet uit één bron met één methode komen — een negatief anker met een foute
coördinaat is erger dan geen negatief anker.

**F9 · A1's routeerpunt-regel voor b7-staart mengt twee ways.** A1 schrijft "way 1303627568 …
174,7 m van het terreinanker, 6 m van de apron-lijn"; gemeten ligt **1303627568** op **12,3 m**
van het terreinanker en 102,7 m van de apron, en de way die **lángs** de apron loopt is
**1303627572** (2,8 m). De annotatie "verwachte snap ≤ 0,20 km" is daardoor misleidend — de
echte snap is 12 m. **Sectie A draagt de gecorrigeerde waarde.** Idem: A1's
apron-beschrijving ("rij witte en rode opleggers") staat niet op 32.16215/118.88132 — daar
ligt op z19 een interne weg met **één** oplegger; de zichtbare opleggerrij staat ~88 m OZO.

**F10 · A1's b5-corridornaam rust op 0,7 m verschil.** 双山路 (way 289112055, `tertiary`) ligt
op **83,6 m** van de havenpoort, 中港路 (Y303) op **84,3 m** — de genoemde corridor is dus niet
door nabijheid bepaald. De corridornaam in sectie C1 komt daarom uit de **gemeten wegblokken**
van de bake (西五节桥街 → 中兴北路 → 常金线 X301 → 长江北路 → 东新路), niet uit A1.

### Blijft onzeker — gaat als openstaand punt de brief in

**F11 · Been-ids ontbreken in álle vijf gebakken stromen.** Werkwijze §2 eist dat
stroomroute-JSON's en markertabellen naar dezelfde `<stroom-id>-b<n>`-ids verwijzen zodat brief
↔ bol 1:1 koppelbaar is zonder mensenwerk. Geen enkel gebakken been draagt er een (de sleutels
zijn overal `['modaliteit','naam','stippel','km','punten']`), en `hecht_marnet route` heeft er
geen vlag voor. Gereedschapswerk, valt buiten deze werkorder — al de derde werkorder waarin het
staat.

**F12 · Het productconflict aan de kade van Zhangjiagang.** §2a-3 van de brief zoekt
*"bulkstapels direct achter de apron (donkere hopen)"*. De ene pass vindt die (ommuurde
gecompartimenteerde bakken met grijze en donkere hopen op 31.96755/120.42051, 50,0 m ZZW), de
andere ziet op dezelfde locatie **containerstapels en houtstapels** en concludeert dat er geen
bulkhopen zijn. Beide passes zijn eigen passes, beide zijn zelf bekeken. Zelfde klasse als
container-vs-bulk bij Beilun. **Dit is een vraag aan de brief, niet aan de satelliet** —
beslis hem in §2a-3 vóór fase C als afgesloten geldt.

**F13 · De knipstap van het rivierbeen heeft geen gereedschap in de repo** (B5). Voorstel: een
`--knip-bij LAT,LON`-vlag in `maak_rivierbeen.py`, of een `knip_rivierbeen.py` naar analogie
van `knip_osm_been.py`. Generator↔uitvoer-driftklasse op een build-cache-bestand.

**F14 · Hazmat-tijdvensters op de b6-corridor.** LiOH·H2O is **UN2680** (klasse 8) en Chinese
snelwegen kennen tijdvensterbeperkingen voor gevaarlijke stoffen. Dat kán de keuze
snelweg-vs-provinciale weg (S19 vs S259) beïnvloeden en is met de gebruikte bronnen niet te
beslissen.

**F15 · Geen vrachtbron voor geen van de vier corridors.** Noch AIS, noch een expediteur, noch
een vergunning legt vast welke route de trucks werkelijk rijden. De corridorkeuzes rusten op
OSM-geometrie + reistijd + de ligging van beide ankers. Dat is sterker dan een gok maar
zwakker dan een document, en het hoort als zodanig in §5 van de brief.

**F16 · Een BUG in `maak_stroombeen_weg.py` die alle bestaande geojsons al dragen.** Het veld
`bron` in de weggeschreven GeoJSON is **hardcoded** op regel ~636:

```python
        "bron": "OpenStreetMap contributors (ODbL) via Geofabrik "
                "mozambique-latest; routebrief grafiet-balama-vidalia been 1",
```

Zelf nagekeken en bevestigd. Alle bestaande `stroombeen-*.geojson` dragen die verkeerde
herkomst; de vier nieuwe zouden hem ook krijgen. **Niet gefixt** (geen repo-wijzigingen deze
ronde) — maar wie hem fixt moet weten dat het de sha256 van álle geojsons verandert en dus de
regressietoets van stap 1 breekt. Fix hem in een **eigen commit**, vóór of na deze werkorder,
nooit ertussen.

**F17 · Meetvalkuil, vast te leggen in het adres-recept.** De Overpass-spiegel
**overpass.osm.ch levert stil een LEEG resultaat voor Chinese bboxen** (het is een
Zwitserland-instance). Dat leest als "niets gevonden" terwijl het "verkeerde server" betekent —
dezelfde klasse als het verhuisde MEE-endpoint. `overpass-api.de` en `kumi.systems` gaven
bovendien herhaald 504/429; plan wachttijd in.

---

**Statuswaarschuwing bij de oplevering.** In de brief mag **geen** van de drie fabrieken als
"satelliet-gelegde losplek mét bekende laaddeur" komen te staan, en de uitgaande laadplekken
mogen **nergens** een coördinaat krijgen. Het is: *"poort/laaddock satelliet-gelegd, uitgaande
expeditie open"*. En de Tesla-keten eindigt op **poort 3**, niet op het terrein — het
terreinpunt uit de brief is een bbox-centroïde en het bushalte-punt is een bushalte. **Een
anker dat niet satelliet-gelegd is, is geen anker — en een benoemde OSM-node is niet
automatisch het object waarnaar hij is vernoemd.**
