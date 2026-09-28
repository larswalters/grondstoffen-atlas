# Routebrief (licht) · kobalt — Moa Bay (Cuba) → Halifax → Fort Saskatchewan (Canada)

**stroom-id:** `kobalt-moa-fortsaskatchewan` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31) ·
**status:** gebakken
**Keten in één zin:** kobalt (als mixed-sulfide-neerslag/MSP, samen met nikkel) van de Sherritt/GNC Moa-JV-plant in
Cuba per **zeeschip** om de VS heen naar Halifax, en per **spoor** over de CN-transcontinentale hoofdlijn (via
Moncton — bewust om de Maine-VS-kortsluiting heen) naar de Sherritt-raffinaderij in Fort Saskatchewan, Alberta —
het enige westerse kobalttraject en, per ontwerpdatum, het meest onderbroken: de mijn ligt sinds februari 2026
grotendeels stil door brandstofschaarste en de raffinaderij is sinds 22-06-2026 gesloten na de VS-Cuba-sancties
op de metaalsector (mei 2026) [1][3][5].
**Welke as van het verhaal:** *Cuba → Canada* — decennia Sherritt-GNC-samenwerking (Moa JV, 50/50) [2][6], nu
stilgevallen. De brief tekent de bestaande infrastructuur/route, geen actieve lading.

## 1 · Ketenkaart
```
Moa Bay-laadkade `co-moa-laad` ──(b1 zee · haven-aanloop, stippel · ~9 km schematisch)──►
MARNET-zeeknoop 8163 (21.1135,-74.4068) ──(b2 zee · Caribische Zee → Atlantische Oceaan, om de VS heen ·
~2.900 km indicatief)──► Halifax-kade `co-halifax-kade` (aannemelijk: één bron voor de exacte kade)
──(b3 spoor · CN-hoofdlijn via Moncton/Québec/Winnipeg/Saskatoon/Edmonton · ~5.000 km indicatief)──►
Fort Saskatchewan-raffinaderij `co-fortsask-raffinaderij` ⏹ stoppunt (raffinaderij gesloten, geen vervolg gebrond)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee (haven-aanloop) | `co-moa-laad` → MARNET-zeeknoop 8163 | — | schematisch, exact bij het bakken | `maak_havenaanloop.py`, terugval rechte stippel | ja — MARNET reikt niet tot de kade (75,7 km, ruim boven de default max-snap) |
| b2 | B | zee | MARNET-zeeknoop 8163 (21.1135,-74.4068) → `co-halifax-kade` | Caribische Zee → Atlantische Oceaan — bewust om de VS heen (sanctie-gevoelige route) | ~2.900 (indicatief; exact bij MARNET-bake) [1] | MARNET `--been "zee\|…\|21.1135,-74.4068\|44.6735,-63.6032"` | nee |
| b3 | C | spoor | `co-halifax-kade` → `co-fortsask-raffinaderij` | CN-hoofdlijn: Halifax → Moncton → Québec → Winnipeg → Saskatoon → Edmonton (Moncton-omweg vermijdt de historische Maine-VS-kortsluiting) | ~5.000 spoor (hemelsbreed ~3.700) [4], te bakken in 6 losse runs | `toets_spoorroute.mjs` (`BAKE_SUFFIX=-raw`, 6× kop→via/via→staart) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-moa-laad` | laadplek (mijn/plant aan zee) | Punta Gorda-aanlegsteiger, Bahía de Moa (Sherritt/GNC Moa JV, Ernesto Che Guevara-plant ~1,6 km landinwaarts) | 20.6372, -74.8549 | [2][8][9], satelliet | **onzeker** (z18 gezien: kleine aanlegsteiger met afgemeerde vaartuigen op de landtong bij Punta Gorda-dorp; geen zichtbare laadbrug/kraan voor bulk-MSP op dit beeld — de door havendata genoemde "offshore terminal" is op deze resolutie niet te onderscheiden, zie §7) |
| `co-halifax-kade` | overslag zee → spoor | Richmond Terminals, Halifax (multipurpose breakbulk-kade met kade-eigen spoor) | 44.6735, -63.6032 | [7][9], satelliet | **aannemelijk** (z16 gezien: lange kade met kraanwerf, loodsen, spoortakken die vanaf het vasteland aankomen, schip aan de kade — past bij breakbulk+rail, maar geen bron noemt Sherritt/MSP hier met naam) |
| `co-fortsask-raffinaderij` | losplek / raffinaderij (eindpunt, gesloten) | Sherritt Metals Facility, Fort Saskatchewan, Alberta | 53.7198, -113.1904 | [6][9], satelliet | **bron-gelegd** (z16 gezien: raffinaderijcomplex met bolvormige opslagtanks, een rode/oranje tailingsvijver (ijzerresidu, kenmerkend voor Sherritt's HPAL/ammoniakloog-proces) en een spooraansluiting aan de noordoostzijde) |

## 4 · Via-punten (been b3 — corridorkeuze op de CN-hoofdlijn)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | Moncton — spoorstation/CN-junctie | 46.0833, -64.7861 | splitsing waar de route bewust via de Canadese Maritimes loopt i.p.v. de kortere Maine-VS-doorsteek (sanctie-conform) [3][9] |
| b3 | 2 | Québec — Gare du Palais, oeversprong Saint-Laurent | 46.8178, -71.2139 | enige spoorbrug/-oeveroversteek op deze lijn tussen de Maritimes en het binnenland [9] |
| b3 | 3 | Winnipeg — Union Station | 49.8889, -97.1343 | knoop tussen de oostelijke en de westelijke tak van de CN-transcontinentale hoofdlijn (Prairies) [9] |
| b3 | 4 | Saskatoon — CN Chappell Yard | 52.1052, -106.7505 | rangeerknoop op de hoofdlijn tussen Winnipeg en Edmonton [9] |
| b3 | 5 | Edmonton — CN-knoop vóór de aftakking | 53.5462, -113.4912 | laatste corridorkeuze vóór de kopse aansluiting op de Sherritt-raffinaderij [9] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Fort Saskatchewan-raffinaderij | Sherritt International | mixed-sulfide-neerslag (Ni+Co) → geraffineerd nikkel + kobalt | ~38.200 t/jaar Ni+Co gecombineerd (100%-basis, nominaal) — sinds 22-06-2026 stilgelegd | [3][5][6] |

## 6 · Stoppunt
De brief stopt bij de Fort Saskatchewan-raffinaderij: dit is zelf het eindpunt van de aangeleverde grondstof
(geraffineerd metaal), de raffinaderij ligt sinds 22-06-2026 stil, en geen bron noemt een afzetmarkt voor
toekomstige output — fase D/E vervallen.

## 7 · Open punten
- **`co-moa-laad` is niet satelliet-bevestigd als bulklaadpunt.** Punta Gorda-jetty is een kleine
  aanlegsteiger (vissersvaartuigen); havendata noemt "Port of Punta Gorda" als offshore-terminal voor de
  Moa-regio (LOA 134 m, diepgang 8,5 m) [8], maar toont geen zichtbare laadbrug/kraaninstallatie op deze
  resolutie. Coördinaat niet verzonnen — blijft **onzeker**.
- **`co-halifax-kade` is niet bij naam bevestigd voor Sherritt-lading.** Richmond Terminals is de meest
  plausibele breakbulk+rail-kade in Halifax [7]; geen bron noemt de kade expliciet voor MSP-zakken.
- **Spoorlengte is een schatting.** ~5.000 km (hemelsbreed ~3.700) komt uit het ontwerp, geen gepubliceerde
  officiële lengte gevonden — exact bij het bakken (6 aparte kop→via/via→staart-runs, zie bak-aanwijzingen).
- **Heropening onbekend.** De Moa-mijn ligt sinds februari 2026 grotendeels stil door brandstofschaarste en
  Fort Saskatchewan is sinds 22-06-2026 gesloten na de VS-Cuba-sancties op de metaalsector van mei 2026 [1][3][5];
  per ontwerpdatum (2026-09-28) is een heropening niet gedocumenteerd. De kaart tekent de infrastructuur van een
  niet-actieve as.
- **Jaarvolume is groepsniveau, niet corridor-specifiek.** Het cijfer (~3,5–4 kt Co/jaar nominaal) is het totaal
  van de Moa JV vóór stillegging, niet uitgesplitst naar wat specifiek via Halifax–Fort Saskatchewan liep.

## 8 · Bronnen
[1] CBC News, 22-06-2026 — "Sherritt to shut down its Fort Saskatchewan refinery"; sluiting na opraken van de
mixed-sulfide-voorraad uit Moa. https://www.cbc.ca/news/canada/edmonton/sherritt-fort-sask-refinery-9.7250254
[2] Sherritt International — "Metals Production"; Moa JV 50/50 Sherritt/General Nickel Company, mijn + HPAL-plant
in Moa, Cuba, mixed sulphides per zeeschip naar Halifax en per spoor naar Fort Saskatchewan.
https://sherritt.com/operations/metals/
[3] Jacobin, 06-2026 — "The Imperial Plunder of Cuba Has Begun"; VS-Treasury breidt Cuba-sancties uit naar de
metaal-/mijnsector (mei 2026). https://jacobin.com/2026/06/trump-cuba-canada-mining-sherritt
[4] Wikipedia/algemeen — Canadian National Railway transcontinentale hoofdlijn (voormalig National
Transcontinental Railway + Grand Trunk Pacific): Moncton–Québec–Winnipeg–Saskatoon–Edmonton, sinds de fusie
in CN opgegaan; Intercolonial Railway-doorlooprecht Moncton–Halifax. https://en.wikipedia.org/wiki/Canadian_National_Railway
[5] Skillings.net — "Sherritt International shuts Canada's only cobalt refinery amid US-Cuba sanctions fallout".
https://skillings.net/sherritt-international-shuts-canadas-only-cobalt-refinery-amid-us-cuba-sanctions-fallout/
[6] Sherritt International, 2024 Annual Information Form — Moa JV-productie (~33 kt Ni + ~3,5-4 kt Co/jaar
nominaal); Fort Saskatchewan-raffinaderijcapaciteit ~38.200 t/jaar Ni+Co gecombineerd (100%-basis).
https://sherritt.com/wp-content/uploads/2025/04/2024-AIF-Final-2025-03-25.pdf
[7] Port of Halifax — Richmond Terminals: multipurpose-kade met on-dock CN-spoor, breakbulk/RoRo, centraal
gelegen met snelweg- en spoortoegang. https://www.porthalifax.ca/facilities/hpa-facilities/richmond-terminals/
[8] Havendata — "Port of Punta Gorda", offshore-terminal Cuba, max LOA 134 m / diepgang 8,5 m; Port of Moa
handelt zwavel en nikkel. https://www.bansarchina.com/largest-cuba-ports/
[9] OpenStreetMap via Nominatim (ODbL) — Punta Gorda-kaap (20.6363,-74.8546); Richmond Terminals-pier
(44.6735,-63.6032); Moncton-spoorstation (46.0833,-64.7861); Gare du Palais Québec (46.8178,-71.2139); Winnipeg
Union Station (49.8889,-97.1343); CN Chappell Yard Saskatoon (52.1052,-106.7505); Edmonton-centrum
(53.5462,-113.4912). https://www.openstreetmap.org
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15-z18, live) —
`v2/build-cache/satcheck/sat-kobalt-moa-fortsaskatchewan-moa-puntagorda.png`,
`sat-kobalt-moa-fortsaskatchewan-moa-plant-close.png`, `sat-kobalt-moa-fortsaskatchewan-moa-settlement-close.png`,
`sat-kobalt-moa-fortsaskatchewan-halifax-richmond.png`, `sat-kobalt-moa-fortsaskatchewan-fortsask-refinery.png`.
[11] Mining.com / Discovery Alert — bevestiging sanctie-tijdlijn (Sherritt schortte Cuba-JV-deelname op
07-05-2026). https://www.mining.com/us-sanctions-shut-canadas-only-cobalt-refinery/ ·
https://discoveryalert.com.au/sherritt-alberta-refinery-shutdown-cobalt-supply-chain-2026/

## 9 · Gebakken (2026-09-28, lichte werkwijze)

**Stroom `kobalt-moa-fortsaskatchewan`** → `v2/data/stroomroute-kobalt-moa-fortsaskatchewan.json` — 8 benen,
**7.854,2 km**, 9.386 punten, 8 markers. zee 70,9 (stippel) + 2.943,5 = 3.014,4 km · spoor 297,8 + 704,6 + 2.477,7 +
766,7 + 520,0 + 73,0 = 4.839,8 km. Recept: `bak_stromen.sh` (functie `bak_kobalt_moa_fortsaskatchewan`).

**b1 (zee, stippel, haven-aanloop Moa Bay):** `maak_havenaanloop.py --van 20.6372,-74.8549 --naar
21.1135,-74.4068` — pad over water gevonden op de eerste getoetste trap (cel 0,005° kaal), **70,9 km · 49 punten ·
0,00 km over land**, omwegfactor 1,005 tegen de rechte lijn (70,5 km). Geen terugval nodig.

**b2 (zee, MARNET, geen aanloop nodig aan de Halifax-kant):** `--been "zee|...|21.1135,-74.4068|44.6735,-63.6032"`
— snap Moa-zeeknoop 0,000 km, snap Halifax-kade 3,788 km (beide ruim onder `--max-snap` 25 km). Resultaat
**2.943,5 km over 38 MARNET-edges** (314 punten) tegen de indicatieve ~2.900 km uit de brief = **+1,5%**, ruim
binnen ±15%. Lengte-invariant: getekende lijn 2.943,457 km vs som edge-km 2.943,400 km = +0,057 km (de naden).
Kruist niet de VS-kust (het punt bij 20,9153/-73,8116 is een krappe bocht van 93,3° / straal 5.169 m bij het
vertrek van de Cubaanse kust, geen omkering).

**b3 (spoor, zes losse runs op het 1-op-1-net, console bevestigt "3260717 spoor-edges", `BAKE_SUFFIX=-raw`):**
1. Halifax → Moncton (`--van=44.6735,-63.6032 --naar=46.0833,-64.7861`): **297,8 km** (losse run 296,4 km over
   207 edges, grootcirkel 182,0 km, verhouding 1,63 — het kleine verschil komt van de snap-aanpassing tijdens de
   integratie in `hecht_marnet route`).
2. Moncton → Québec: **704,6 km** (losse run 701,7 km, grootcirkel 499,0 km, verhouding 1,41).
3. Québec → Winnipeg: **2.477,7 km** (losse run 2.469,8 km, grootcirkel 1.935,4 km, verhouding 1,28).
4. Winnipeg → Saskatoon: **766,7 km** (losse run 763,8 km, grootcirkel 716,0 km, verhouding 1,07).
5. Saskatoon → Edmonton: **520,0 km** (losse run 518,3 km, grootcirkel 480,2 km, verhouding 1,08).
6. Edmonton → Fort Saskatchewan-raffinaderij: **73,0 km** (losse run 71,1 km, grootcirkel 27,7 km, verhouding 2,57
   — de kopse aansluiting op de raffinaderij, geen doorgaande hoofdlijn).

Som **4.839,8 km tegen ~5.000 km (hemelsbreed ~3.700 km) uit de brief = −3,2%, ruim binnen ±15%.**
⚠️ **Er is geen gepubliceerd totaal voor de héle as** (Moa → Halifax → Fort Saskatchewan) om tegen te toetsen —
alleen de indicatieve ~2.900 km (zee) en ~5.000 km (spoor) uit het ontwerp, elk apart getoetst zoals hierboven.

**Toets naden:** alle overgangen **0,00 km** behalve b2 (zee) → b3.1 (spoor Halifax): **4,75 km** — het zeebeen
eindigt op zijn eigen MARNET-zeeknoop-snap (3,788 km van de Halifax-kade-anker), het spoorbeen begint op de
hoofdnet-snap bij het spoorstation (44,67500/-63,61590); binnen de norm van ≤5 km, maar wel het grootste gat van
deze bake.

**`toets_knikken.py`:** 7 knikken ≥60°, 5 omkeringen ≥150°, waarvan **4 TERUGLOOP** — allemaal binnen been b3.3
(Québec → Winnipeg, 2.477,7 km): 178,1° bij 48,2392/-79,0305 (R~89 m, v=3,4) · 168,4° bij 46,5591/-72,7309
(R~50 m, v=4,1) · 163,8° bij 46,5514/-72,7401 (R~64 m, v=3,4) · 159,6° bij 49,0715/-84,1130 (R~53 m, v=3,2).
⚠️ **Bevinding, niet dichtgetrokken** (werkwijze §5: buiten de norm = bevinding) — deze vier terugloops zitten alle
vier op het traject door Ontario/Québec op de transcontinentale hoofdlijn (geen van de vijf via-punten ligt in de
buurt) en zijn eigenschap van het 1-op-1-OSM-net op die stukken zelf, niet van een gekozen via-coördinaat; het
uitzoeken van een alternatieve netconnectiviteit rond elk van de vier punten valt buiten de scope van deze lichte
bake. Verder: 1 krappe bocht (142,2°, R~159 m) bij Winnipeg-vertrek en 1 scherpe bocht "echt" (170,2°, R~40 m) bij
de kopse aansluiting Edmonton→Fort Saskatchewan — beide kopmaak-plekken op een emplacement/spooraansluiting, geen
fout.

**`toets_rechte_benen.py --min-km 5`:** geen been van deze stroom in de uitslag — ook b1 (de stippel, omwegfactor
1,005) wordt niet als verdachte rechte lijn aangemerkt.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {zee, spoor} (binnen de toegestane set),
elk been ≥2 punten (minimum 49), bestandsgrootte **175,6 KB** (< 300 KB-richtwaarde).

**Markers:** co-moa-laad 0 m · Moncton 176,6 m · Winnipeg 123,2 m · Saskatoon 143,9 m · co-fortsask-raffinaderij
228,1 m — allemaal ruim binnen ~0,5 km. Drie markers liggen verder: Québec 507,2 m (net over de norm, oeversprong-
station ligt net naast de gerouteerde hoofdlijn) · **co-halifax-kade 1.018,0 m** (anker ≠ routeerpunt — het
zeebeen eindigt op de MARNET-zeeknoop-snap 3,788 km verderop dan de kade-anker, zie de naad-toets hierboven) ·
**Edmonton 3.352,5 m** (anker ≠ routeerpunt — het OSM-viapunt bij Edmonton-centrum ligt een stuk van de
gerouteerde CN-hoofdlijn af; bevinding, niet bijgeschoven om de afstand te halen, werkwijze §3).

**Open punten die blijven staan (zie ook §7):** co-moa-laad en co-halifax-kade blijven resp. onzeker/aannemelijk
(geen bulklaadbrug resp. geen naam-bevestiging gevonden); de spoorlengte (~5.000 km) was een schatting zonder
gepubliceerde officiële lengte, nu vervangen door de gemeten 4.839,8 km; heropening van de as (mijn stilgevallen
februari 2026, raffinaderij gesloten 22-06-2026) blijft ongedocumenteerd op ontwerpdatum.

**Gereedschapslessen:**
- Een spoorbeen met een kopse aansluiting op een geïsoleerde fabrieksspur (hier Edmonton→Fort Saskatchewan, 73,0
  km tegen 27,7 km grootcirkel = verhouding 2,57) hoort een hogere omwegfactor te hebben dan een doorgaande
  hoofdlijn — dat is geen fout, de trein maakt hier letterlijk een kop.
- Vier TERUGLOOPS op één spoorbeen van bijna 2.500 km, allemaal ver van elke gekozen via-coördinaat, bevestigen
  opnieuw dat de omkeringsklasse een eigenschap van het 1-op-1-OSM-net op die specifieke stukken is, niet van de
  gekozen via-punten (dezelfde les als bij `nikkel-sudbury-kristiansand`, MacMillan Yard) — bij een lichte bake
  is het rapporteren van de vier coördinaten voldoende, het narekenen van de lokale netconnectiviteit per punt is
  een aparte, zwaardere ronde.
- De grootste naad van deze bake (4,75 km) zit precies op de enige zee→spoor-overslag — een MARNET-zeeknoop-snap
  van een paar kilometer van de kade-anker is normaal voor een kust met weinig zeeknoop-dichtheid en hoort niet
  tot een tweede haven-aanloop te leiden zolang de naad zelf onder de 5 km-norm blijft.
