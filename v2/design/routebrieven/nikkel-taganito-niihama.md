# Routebrief (licht) · nikkel — Taganito (Claver) → Niihama (Ehime) — met vertakking Hachinohe

**stroom-id:** `nikkel-taganito-niihama` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** limoniet uit de Taganito-mijn (Nickel Asia/TMC, Claver) gaat per eigen mijnweg naar de aangrenzende Taganito HPAL-fabriek (THPAL, Sumitomo Metal Mining/Nickel Asia), waar het als mixed sulfide (MS, ~57 % Ni) van dezelfde kade per zeeschip naar de Niihama Nickel Refinery (SMM, Ehime, Shikoku) vertrekt voor elektrolytische kathode; een aparte, kleinere stroom hooggradig saproliet gaat als DSO vanaf dezelfde Claver-kade naar de ferronikkelfabriek PAMCO Hachinohe (bedrijfsniveau gebrond).
**Welke as van het verhaal:** *het Filipijnse contrast* — waar Indonesië sinds de exportban mijn én smelter in eigen land houdt, verschepen de Filipijnen nog altijd ruw/nauwelijks bewerkt erts; Taganito is de HPAL-helft van dat contrast (MS naar Japanse class-1-raffinage) met een DSO-vertakking ernaast. THPAL 36 kt Ni-inhoud/jaar in MS (SMM); Niihama 65 kt kathode/jaar (SMM).

## 1 · Ketenkaart
```
Taganito-mijn `ni-taganito-laad` ──(b1 truck · eigen mijnweg, privaat terrein · km n.g.)──► THPAL-fabriek `ni-thpal-plant`
   (interne overslag, geen eigen been, ~1,2 km: MS naar de aangrenzende kade)
   → THPAL-kade `ni-thpal-pier` ──(b2 zee · haven-aanloop, stippel · ~51 km)──► MARNET-zeeknoop 8314
   ──(b3 zee · MARNET · 3.043,8 km)──► MARNET-zeeknoop 5746 ──(b4 zee · haven-aanloop, stippel · ~25 km)──►
   Niihama Nickel Refinery `ni-niihama-refinery` (SMM) ⏹ stoppunt (kathode, geen gedocumenteerde vervolgfabriek)

Vertakking (vanaf THPAL-kade/zeeknoop 8314, saproliet DSO — bedrijfsniveau gebrond):
   `ni-thpal-pier` ──(b5 zee · MARNET, vertakt van b2 · schatting ~3.300–3.800 km)──► Hachinohe-zeeknoop
   ──(b6 zee · haven-aanloop, stippel · ~11,7 km)──► PAMCO Hachinohe `ni-hachinohe` ⏹ stoppunt (ferronikkel)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-taganito-laad` → `ni-thpal-plant` | eigen mijnweg TMC → THPAL (aangrenzend terrein) | ~3–8 [1][6] (hemelsbreed 1,2) | maak_stroombeen_weg, `eindToegangPrivaat: True` (OSM-bbox is overwegend `unclassified`/`service access=private`/`track`) | nee, tenzij het extract geen weg geeft → dan stippel "eigen terrein" |
| b2 | B | zee (haven-aanloop) | `ni-thpal-pier` → MARNET-zeeknoop 8314 (9.8356, 125.3465) | — | ~51,4 hemelsbreed [8]; omweg-factor 1,086 in de toets ⇒ ~56 gerouteerd | maak_havenaanloop | ja — MARNET reikt hier niet tot de kade |
| b3 | B | zee | MARNET-zeeknoop 8314 → MARNET-zeeknoop 5746 (34.0720, 133.0479) | Filipijnenzee → oostelijk om Kyushu → Bungo-kanaal/Seto-binnenzee | 3.043,8 [8] (proefroute, getoetst) | MARNET | nee |
| b4 | B | zee (haven-aanloop) | MARNET-zeeknoop 5746 → `ni-niihama-refinery` | — | ~24,8 [8] | maak_havenaanloop | ja — snap net onder de max-snap-grens; Niihama-kade ligt in de Seto-binnenzee buiten het net |
| b5 | A' | zee | `ni-thpal-pier` → Hachinohe-zeeknoop | Filipijnenzee → Stille Oceaan → Hachinohe (Aomori) | schatting 3.300–3.800 hemelsbreed [3][5][8] (niet gemeten in de toets) | MARNET, **vertakt_van b2** (aftakking bij zeeknoop 8314) | nee |
| b6 | A' | zee (haven-aanloop) | Hachinohe-zeeknoop → `ni-hachinohe` | — | ~11,7 [8] | maak_havenaanloop | ja |

THPAL-fabriek → THPAL-kade (geen eigen been, ~1,2 km): MS gaat over het eigen terrein van fabriek naar kade, zoals Portsite bij de Grasberg-brief.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-taganito-laad` | mijn / laadplek (erts + DSO-stockpile) | Taganito Mining Corporation (Nickel Asia), Brgy. Taganito, Claver | 9.5464, 125.8193 | [1][6] | bron-gelegd (z17 gezien: wit ertsstockpile direct naast de laadsteiger, mijnterrassen zichtbaar landinwaarts naar het zuidwesten) |
| `ni-thpal-plant` | verwerking (HPAL-autoclaven) | Taganito HPAL Nickel Corporation (THPAL) | 9.5395, 125.8106 | [2][4][6] | bron-gelegd (z14/z16 gezien: ronde tank-/autoclaafinstallatie en procesgebouwen, rode/bruine tailings-vijver ten zuidoosten) |
| `ni-thpal-pier` | overslag (kade, gedeeld door b2 en de vertakking) | Taganito/Claver-laadsteiger (TMC/THPAL) | 9.5490, 125.8160 | [6][8] | bron-gelegd (z17 gezien: laadsteiger met bulkcarrier aangemeerd, opslagloodsen op de kade) |
| `ni-niihama-refinery` | losplek + raffinaderij (site-anker, geen apart C-been) | Niihama Nickel Refinery, SMM (Besshi-Niihama-district) | 33.9669, 133.2658 | [2][7] | bron-gelegd (z15 gezien: industrieterrein aan het water, met een kleine kade/havenbekken pal ten zuiden van het complex) |
| `ni-hachinohe` | losplek (ferronikkelfabriek, DSO) | PAMCO (Pacific Metals Co.) Hachinohe, Kawaraki-havengebied | 40.578, 141.482 | [3][5] | **onzeker** (z16 gezien: havenindustrieterrein met kades bij de Kawaraki-havenwijk, maar geen naam-tag op de kaart — welk perceel PAMCO is, is niet vastgesteld) |

## 4 · Via-punten
Geen — beide landbenen (b1) zijn korter dan het corridorkeuze-criterium (3–8 km, eigen terrein zonder splitsing); alle overige benen zijn zee/MARNET (§1 van de werkwijze: zee routeert via de router, geen via-punten).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| THPAL (Taganito) | SMM / Nickel Asia (Taganito HPAL Nickel Corp.) | limonieterts → mixed sulfide (MS, ~57 % Ni) | 36 kt Ni-inhoud/jaar in MS (capaciteit bereikt FY2017; 44.056 dmt MS in 2021) | [2][4] |
| Coral Bay HPAL (Palawan, niet getekend) | Sumitomo/Rio Tuba | limonieterts → MS | ~24 kt Ni-inhoud/jaar, naar dezelfde Japanse raffinaderijen (alleen genoemd) | [2] |
| Niihama Nickel Refinery | SMM | MS → elektrolytisch Ni-kathode (+ Co) | 65 kt kathode-Ni/jaar; enige elektrolytisch-nikkelraffinaderij van Japan | [2] |
| PAMCO Hachinohe | Pacific Metals Co. | saproliet-DSO → ferronikkel | niet gepubliceerd (tonnage TMC→PAMCO niet gevonden — open punt) | [3][5] |

## 6 · Stoppunt
Twee stoppunten, elk in één zin: de hoofdstroom stopt bij Niihama-kathode — geen bron noemt een specifieke roestvrijstaal- of batterijfabriek die dit metaal afneemt; de DSO-vertakking stopt bij PAMCO Hachinohe — dat is zelf al de ferronikkelfabriek en er is geen vervolgafnemer gedocumenteerd.

## 7 · Open punten
- **PAMCO Hachinohe-kade niet exact gelegd:** de Kawaraki-havenwijk is bevestigd (industrieterrein, kades), maar geen enkele OSM-naam-tag of kaartlaag wijst het PAMCO-perceel aan; vraagt een niet-OSM-bron (bedrijfskaart/vergunning) of een gerichte Wayback-pass.
- **Tonnage TMC → PAMCO per jaar** is niet gevonden (alleen bedrijfsniveau: NAC/TMC verkoopt hooggradig saproliet vooral aan PAMCO, 33,5 % aandeelhouder van TMC); zonder cijfer geen jaarvolume op b5/b6.
- **km b5 (Claver → Hachinohe-zeeknoop) is een schatting**, niet gemeten met `hecht_marnet route` in deze sessie; bakken moet het echte getal leveren.
- **THPAL-kade en Taganito-mijnkade lijken hetzelfde overslagpunt** (0,5 km uit elkaar, satellietbeeld toont één laadsteiger met stockpile) — bij het bakken beide benen (b1-eind en b2-start/b5-start) op ditzelfde punt laten samenvallen, geen tweede anker verzinnen.
- **Coral Bay (Palawan)** is een gelijkaardige, niet-getekende bijstroom naar dezelfde Japanse raffinaderijen — alleen genoemd in §5, niet gemodelleerd.
- **Fase D/E vervallen:** geen bron noemt een fabriek die Niihama-kathode of Hachinohe-ferronikkel specifiek afneemt.

## 8 · Bronnen
[1] Nickel Asia Corporation, Taganito Mining Corporation (subsidiary page): mijnsite in Brgy. Hayanggabon/Urbiztondo/Taganito/Cagdianao, Claver, Surigao del Norte; levert limoniet aan THPAL. https://nickelasia.com/subsidiaries/taganito-mining-corporation
[2] Sumitomo Metal Mining: THPAL/Niihama-sustainability-artikel (MS-productie, jaarvolumes) en Niihama Nickel Refinery-locatiepagina (enige Japanse elektrolytisch-Ni/Co-raffinaderij, adres Nishibara-cho 3-chome, Niihama, Ehime). https://www.smm.co.jp/en/sustainability/activity_highlights/article_12/ · https://www.smm.co.jp/en/corp_info/location/domestic/nickel/ · https://www.smm.co.jp/en/corp_info/location/domestic/
[3] Pacific Metals Co., Ltd. (PAMCO), bedrijfssite: ferronikkelproducent, hoofdvestiging/fabriek Hachinohe, Aomori; koopt saproliet-erts rechtstreeks uit de Filipijnen. https://www.pacific-metals.co.jp/en/
[4] Caraga EMB (DENR), THPAL-projectdocument (PDF): capaciteit en procesbeschrijving Taganito HPAL. https://caraga.emb.gov.ph/wp-content/uploads/2016/08/THPAL.pdf
[5] 大平洋金属株式会社 (Pacific Metals Co.), Japanse Wikipedia: ferronikkelfabrikant met hoofdvestiging in Hachinohe, Aomori. https://ja.wikipedia.org/wiki/大平洋金属
[6] OpenStreetMap (ODbL) via Nominatim — landuse "Taganito Mining Corporation" 9.5464/125.8193 · landuse "Taganito HPAL Nickel Plant" 9.5395/125.8106 · landuse "THPAL Dormitory" 9.5359/125.8274 · place "Claver" 9.5730/125.7327. https://www.openstreetmap.org
[7] OpenStreetMap (ODbL) via Nominatim — landuse 住友金属鉱山 別子事業所 (SMM Besshi Works) 33.9669/133.2658, postcode 792-8555 (zelfde postcode als het adres van de Niihama Nickel Refinery). https://www.openstreetmap.org
[8] Toets/haalbaarheidsronde `nikkel-taganito-niihama` (ontwerp + toets, 2026-09-26): proefzeebeen MARNET-zeeknoop 8314 → 5746 = 3.043,8 km; haven-aanlopen Claver ~51,4 km (omweg 1,086) en Hachinohe ~11,7 km; Niihama-snap ~24,8 km net onder max-snap.

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `nikkel-taganito-niihama`** → `v2/data/stroomroute-nikkel-taganito-niihama.json` — 6 benen. 7.152,5 km. 5 markers: truck 1,9 km · zee (stippel) 65,9 km · zee 3.043,8 km · zee (stippel) 25,7 km · zee (vertakking) 4.004,9 km · zee (stippel, vertakking) 10,3 km.
Recept: `bak_stromen.sh` (functie `bak_nikkel_taganito_niihama`) voor b1-b4; de vertakking (b5/b6) is ná de hoofdbake aangehecht via `voeg_been_toe.py --vertakt-van`, geen herbake van b1-b4 (besluit Lars 2026-08-06: bakken is geen deliverable).

Toelichting per been:
- **b1** (truck, Taganito-mijn → THPAL-plant): nieuwe wegscan, profiel `nikkel-taganito-niihama-taganito-thpal` in `maak_stroombeen_weg.py` (extract filipijnen, `corridorKlassen` ruim + `eindToegangPrivaat: True` — de OSM-bbox rond Claver is overwegend `unclassified`/`service access=private`). Het extract gaf een doorlopend wegpad (geen stippel nodig): **1,9 km** getekende geometrie tegen het brief-venster van 3-8 km — de twee terreinen liggen dichter bij elkaar dan het ontwerp veronderstelde (hemelsbreed is al maar 1,2 km).
- **THPAL-plant → THPAL-kade**: bewust GEEN eigen been (Portsite-patroon uit de Grasberg-brief) — de MS "verschijnt" op de kade; het procesgat van 1,21 km tussen b1's eind en b2's begin blijft bewust staan (binnen de norm van ≤5 km).
- **b2** (zee, haven-aanloop Claver/THPAL-kade, stippel): `maak_havenaanloop.py` — 65,9 km, omwegfactor 1,089, 0% over land (geen landkruising midden op de lijn).
- **b3** (zee, MARNET-zeeknoop 8314 → 5746, doorgetrokken): **3.043,8 km** — komt vrijwel exact overeen met de brief-toets (3.043,8 km, proefroute getoetst), 0,0%.
- **b4** (zee, haven-aanloop Niihama, stippel): `maak_havenaanloop.py` — 25,7 km, snap net onder de max-snap-grens, 0% over land. Tegen de brief-schatting ~24,8 km = +3,6%, binnen ±15%.
- **b5** (zee, vertakking MARNET-zeeknoop 8314 → Hachinohe-zeeknoop 5690, doorgetrokken, `vertakt_van: 2`): niet gemeten in de brief-toets (schatting was 3.300-3.800 km hemelsbreed) — de bake-console geeft **4.004,9 km** als het gemeten getal, en dat is hier leidend, niet de schatting (per opdracht). Naad tot been 2: 0 m.
- **b6** (zee, haven-aanloop PAMCO Hachinohe, stippel, `vertakt_van: 5`): rechte lijn van **10,3 km** (Hachinohe-zeeknoop → PAMCO-anker). `maak_havenaanloop.py` bevestigde op dezelfde twee punten vooraf 0% landkruising, zowel op de rechte lijn (10,3 km) als op het kortste pad over water (11,1 km, omwegfactor 1,077) — de rechte stippel is hier geometrisch gelijkwaardig aan het gerouteerde alternatief. Tegen de brief-schatting ~11,7 km = −11,9%, binnen ±15%. Naad tot been 5: 0 m. Marker "PAMCO Hachinohe" draagt de status **onzeker** (§3/§7): geen OSM-naam-tag bevestigt welk perceel in het Kawaraki-havengebied van PAMCO is — dat is een positie-onzekerheid, apart van de klassieke stippel-conventie ("hier reikt het net niet"); beide redenen gelden hier tegelijk voor dit been.

Alle 5 markers liggen op 0,000 km van hun lijn (elk marker is het exacte start- of eindpunt van een been).

**Toets-bevindingen (buiten de norm, niet dichtgetrokken):**
- **b1 (1,9 km) valt buiten het brief-venster van 3-8 km** — het extract gaf een kortere weg dan het ontwerp voorzag; geen via-punt bijgeschoven om binnen het venster te komen.
- **b2 (65,9 km) valt buiten ±15% van de brief-schatting** (~56 km gerouteerd, uit een hemelsbreed van 51,4 km): een directe nameting van de grootcirkelafstand tussen dezelfde twee coördinaten (THPAL-kade 9,5490/125,8160 → zeeknoop 8314 9,8356/125,3465) geeft 60,5 km, niet 51,4 km — het verschil zit dus al in de brief-schatting zelf, niet in de haven-aanloop-routering (die zelf een plausibele omwegfactor van 1,089 draagt).
- `toets_knikken.py`: 10 knikken ≥60° over de drie doorgetrokken benen (b1, b3, b5), waarvan **0 omkeringen ≥150°** en dus **0 terugloop** — geen reparatie nodig. De 4 "spikes" op b1 zitten op het korte mijnweg-stuk (OSM-detailruis op een weg van 1,9 km); de "krappe bochten" op b3 en b5 delen twee coördinaten (10,50000/126,40000 en 10,58500/125,56270) — de MARNET-router neemt daar een scherpe hoek op zowel de hoofdstroom als de vertakking, want beide beginnen op hetzelfde zeeknoop 8314 in de Filipijnenzee.
- `toets_rechte_benen.py --min-km 5`: alleen **b6** (10,3 km, stippel, omwegfactor 1,000) staat op de verdachtenlijst — verwacht, want b6 is bewust een schematische haven-aanloop-stippel; geen doorgetrokken been van deze stroom staat erop.
- JSON-vormtoets: `versie` 2, `punt_formaat` `lonlat`, modaliteiten {truck, zee} (beide toegestaan), elk been ≥2 punten, bestand 18,8 KB (≪ 300 KB) — allemaal in orde.

**Gereedschapslessen:**
- `voeg_been_toe.py` kent geen `--stippel-geojson`-equivalent — alleen `hecht_marnet.py` onderscheidt geometrie (gerouteerd vs. rechte lijn) van epistemische status (doorgetrokken vs. stippel). Een vertakkingsbeen aanhechten met gerouteerde-maar-gestippelde geometrie kan met dit tool niet; voor b6 maakte dat geometrisch niets uit (0% landkruising op de rechte lijn), maar bij een langere of aan land grenzende vertakkings-stippel zou dit een gereedschapsgat worden.
- Een brief-schatting voor een haven-aanloop (b2: ~51,4 km hemelsbreed) kan zelf afwijken van een directe nameting tussen dezelfde twee coördinaten (60,5 km) — vermoedelijk een ander of afgerond ankerpaar in de ontwerpronde. Bevinding, niet gecorrigeerd in dit bakwerk; de rest van de brief blijft ongewijzigd.
- Twee vertakkingsbenen die op hetzelfde MARNET-zeeknoop beginnen (hier 8314) delen dezelfde "krappe bocht"-coördinaten in `toets_knikken.py` — verwacht gedrag, geen fout.
