# Routebrief (licht) · grafiet — Pohang (Blue Valley) → Busan → Baltimore → Ultium Cells Lordstown/Warren (Zuid-Korea → VS)

**stroom-id:** `grafiet-pohang-warren` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** synthetisch grafiet-anodemateriaal van POSCO Future M uit het Blue Valley-complex bij Pohang per **truck** (Pohang-Busan-snelweg 65, Ulsan 16, Gyeongbu 1) naar Busan New Port, per **zeeschip** via het Panamakanaal naar Baltimore Seagirt (havens en route aannames) en per **truck** (I-70, Pennsylvania Turnpike I-76, Ohio Turnpike) naar Ultium Cells in Lordstown bij Warren (Ohio; aannemelijk: de bron noemt drie Ultium-fabrieken). Geen spoor, leiding of lucht.
**Welke as van het verhaal:** *eerste Koreaanse export van kunstgrafiet-anode, de Stille Oceaan over naar de GM/LG-celfabriek.* **Jaarvolume: geen tonnage gepubliceerd; volume onbekend, peiljaar 2021-2024 als capaciteit: Pohang 8 kt grafiet/j (2021), fase 2 +10 kt = 18 kt/j [2]** (contract 5-12-2022: KRW 939,3 mld over 6 jaar, 2023-2028 [1][2]).

## 1 · Ketenkaart
```
POSCO Future M, Blue Valley Pohang `gr-pohang-bluevalley` ──(b1 truck · 65 → 16 → 1 → 551 → 55 → 69 · hemelsbreed 117 km, geen wegkm)──►
Busan New Port `gr-busan-kade` ──(b2 haven-aanloop, stippel, 10,1 km)──(b3 zee · MARNET 18.868,9 km · Panama · aannemelijk: haven en route niet gebronnet)──►
Baltimore Seagirt `gr-baltimore-seagirt` ──(b4 truck · I-695 → I-70 → I-76 → Ohio Turnpike · hemelsbreed 423 km, geen wegkm · aannemelijk)──►
Ultium Cells Lordstown/Warren `gr-ultium-lordstown` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | Pohang → Busan New Port | Busan-Pohang-snelweg 65, Ulsan-snelweg 16, Gyeongbu 1, 551/55, Seonakdong-ro 69 | hemelsbreed 117 km, geen wegkm (OSRM-indicatie 148, geen bron) | maak_stroombeen_weg (extract zuid-korea) | nee |
| b2 | B | zee | haven-aanloop Busan (kade → zeeknoop 5621) | Busan New Port → open water | 10,1 [eigen meting, MARNET-snap] | LETTERLIJKE KOPIE `ree-cheongju-sanmarcos-aanloop-busan.geojson` (functie `bak_ree_cheongju_sanmarcos`; md5 5b1e99f8, 6 punten) | **ja** (net reikt niet) |
| b3 | B | zee | Busan → Baltimore Seagirt | Korea-straat, Pacific, Panamakanaal, Caraïben, Atlantische kust, Chesapeake Bay | MARNET-droogloop 18.868,9 (via Panama, gemeten); hemelsbreed 11.348; geen gepubliceerde zeekm | MARNET `35.0485,128.7268 → 39.2573,-76.5468` | aanloop Busan ja (b2); Seagirt snapt 2,67 km, nee |
| b4 | D | truck | Seagirt → Ultium Lordstown | I-95 → I-695 → I-70 → I-70/I-76 (Breezewood) → PA Turnpike → Ohio Turnpike (I-76/I-80, afslag Lordstown) → Hallock Young Rd → Tod Ave SW (SR 45) | hemelsbreed 423 km, geen wegkm (OSRM-indicatie 514, geen bron) | maak_stroombeen_weg (us-maryland, us-pennsylvania, us-ohio) | nee (fabriek 1,7 km van de afslag aan de openbare weg) |
Beennamen: b1 "aannemelijk: haven en vervoerwijze niet gebronnet, geen wegkm"; b3 "aannemelijk: havens, route en vervoerwijze niet gebronnet"; b4 "aannemelijk: contract noemt Ultium Cells, niet de leverfabriek". Lijnstijl doorgetrokken, behalve b2.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-pohang-bluevalley` | fabriek / laadplek | POSCO Future M synthetisch-anodefabriek, Blue Valley Nationaal Industrieterrein, Dong-hae-myeon, Pohang | 35.9780, 129.4966 | [1][2][6][7] (complex bekend, geen adres/coördinaat van het gebouw) | **aannemelijk** (z16 gezien: `sat-grafiet-pohang-warren-pohang-z16.png`, kruis op de westrand van een lange fabrieksrij met paarse daken langs de weg, 0,3 km zuidoost van de snelwegknoop; geen POSCO-opschrift zichtbaar; OSM-straatpunt 35.9822,129.4959 ligt in een dorp, toets-punt 35.9800,129.4955 op de knoop) |
| `gr-busan-kade` | overslag weg → zee | Busan New Port, containerterminal | 35.0731, 128.8338 | hergebruikt letterlijk uit `kobalt-huayou-gunsan.md`; **geen bron noemt de haven** | onzeker (daar z15 gezien: containerstapels en portaalkranen; haven voor deze lading niet gebronnet; 10,12 km van zeeknoop 5621, dus aanloop verplicht) |
| `gr-baltimore-seagirt` | overslag zee → weg | Seagirt Marine Terminal, Baltimore | 39.2573, -76.5468 | hergebruikt letterlijk uit `grafiet-chedde-seadrift.md` / `nikkel-zimplats-springs.md`; **geen bron noemt de haven** | aannemelijk (daar z15 gezien: containerstacks en STS-kranen; 2,67 km van zeeknoop 4839) |
| `gr-ultium-lordstown` | afnemer / stoppunt | Ultium Cells, Tod Avenue SW, Lordstown (postadres Warren), Trumbull County, Ohio | 41.1525, -80.8636 | [4][5][8] (OSM man_made=works) | **aannemelijk** (z15 gezien: `sat-grafiet-pohang-warren-warren.png`, kruis op een enorme rechthoekige fabriekshal met parkeerterrein, naast het oude GM Lordstown-complex; fabriek niet in de bron genoemd) |

## 4 · Via-punten (lat, lon, op de doorgaande rijbaan; geschat op OSRM-geometrie, buiten steden; de bake snapt ze op OSM-ways)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Busan-Pohang-snelweg 65 bij Gyeongju | 35.7291, 129.3068 | pint 65 zuidwaarts (niet kustweg 7/31 of Gyeongju-stad) |
| b1 | 2 | Ulsan-snelweg 16 | 35.5557, 129.1790 | pint de Ulsan-snelweg langs de stad |
| b1 | 3 | Gyeongbu 1 bij Yangsan | 35.4507, 129.0785 | pint Gyeongbu 1 (niet Busan-Ulsan 14 langs de kust) |
| b1 | 4 | Daegu-Busan-snelweg 55 | 35.2551, 128.9830 | pint 55 naar Gimhae/Gangseo |
| b1 | 5 | Seonakdong-ro 69 (Gangseo) | 35.1546, 128.8838 | pint de aanvoer naar Busan New Port |
| b4 | 1 | I-695 west van Baltimore | 39.2843, -76.7357 | beltway, niet door het centrum (hergebruik chedde-seadrift) |
| b4 | 2 | I-70 bij Hancock (MD) | 39.6956, -78.1507 | pint I-70 westwaarts (hergebruik chedde-seadrift) |
| b4 | 3 | PA Turnpike I-76 bij Somerset | 40.0598, -79.1396 | pint de Turnpike (niet I-68/I-79) |
| b4 | 4 | PA Turnpike I-76 bij Cranberry | 40.6533, -80.0629 | pint I-76 ten noorden van Pittsburgh |
| b4 | 5 | Ohio Turnpike I-76/I-80 bij Youngstown | 40.9456, -80.6211 | pint de Turnpike tot afslag Lordstown, buiten Youngstown |
Profielen: `extracts` b1 zuid-korea; b4 us-maryland, us-pennsylvania, us-ohio. `refs` b1 65 16 1 551 55 69; b4 I-695 I-70 I-76 I-80. Profiel-ankers (lon, lat) = §3. Venster b1 40 km, b4 50 km. `eindToegangPrivaat` b1 true (fabriek en terminal).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Pohang Blue Valley | POSCO Future M | naaldcokes uit staalkolenteer → synthetisch anodemateriaal | 8 kt/j (fase 1, dec 2021), +10 kt fase 2 (bouw jan 2023, oplevering 2H 2024) = 18 kt/j; een andere bron noemt 13 kt/j | [2][7] |
| Ultium Cells Lordstown | GM + LG Energy Solution | anode → NCMA-pouchcellen | 35-45 GWh/j (bronnen verschillen); stil jan-aug 2026, herstart half aug 2026 | [4][5] |

## 6 · Stoppunt
De keten stopt bij Ultium Cells Lordstown: het contract levert aan Ultium Cells en deze fabriek is de eerste, OSM-vindbare van drie (Warren, Tennessee, Michigan [1]); de cellen gaan verder naar GM-assemblage, niet gebronnet. Fase E vervalt.

## 7 · Open punten
- **Leverfabriek niet gebronnet.** Het persbericht noemt Ultium Cells en de drie plekken Warren, Tennessee en Michigan, geen levering aan een bepaalde fabriek [1]. Warren/Lordstown is aannemelijk; valt het weg of wordt het Spring Hill (TN), dan is dit been een andere stroom (centraal).
- **Havens, route en vervoerwijze niet gebronnet.** Busan en Baltimore zijn aannames (b1/b3/b4 "aannemelijk"); Panama volgt uit de MARNET-router (Suez 9.267 km ernaast, Panama binnen 3 km), geen bron noemt de route. Baltimore kan ook Philadelphia, Norfolk of Ohio via de Grote Meren zijn.
- **Pohang-anker is een complex.** Blue Valley is bevestigd [6][7], het gebouw niet; geen POSCO-opschrift op de tegels. Ligt 0,3 km van de toets-coördinaat 35.9800,129.4955 (die staat op de snelwegknoop): bij gelijktrekking met keten 1 (zelfde anker) het ene punt kiezen. Sitelaag `w-posco-pohang` (36.0026,129.4168) ligt 7,7 km noordwest in het staalcomplex en is NIET deze site.
- **Ultium Warren stond jan-aug 2026 stil** en herstartte half aug 2026 [4][5]; of de lijn in 2026 loopt is niet nagegaan, volume blijft onbekend.
- **Geen gepubliceerde wegkm** voor b1 en b4; de ±15%-toets is indicatie (OSRM 148 en 514 km zijn geen bron).
- **Persbericht 612** (num=612) gaat over katode-materiaal voor GM (Gwangyang), niet over deze anodelijn; niet gebruikt.
- **Sitelaag-kandidaten (centraal):** Pohang Blue Valley en Ultium Lordstown staan niet in `grafiet-sitelaag.json`.

## 8 · Bronnen
[1] POSCO Future M, persbericht, anodecontract met Ultium Cells (KRW 939,3 mld, 6 jaar; Warren, Tennessee, Michigan; Pohang 8 kt/j in 2021). https://www.poscofuturem.com/en/pr/view.do?num=644
[2] POSCO Future M, persbericht: eerste Koreaanse export van kunstgrafiet-anode, contract dec 2022 (2023-2028), fase 1 8 kt/j + fase 2 10 kt/j, Blue Valley. https://www.poscofuturem.com/en/pr/view.do?num=660
[3] POSCO Future M, persbericht 2022-07-28 (katode GM; niet gebruikt voor deze keten). https://www.poscofuturem.com/en/pr/view.do?num=612
[4] InsideEVs, "GM And LG Restart EV Battery Production In Ohio After Seven-Month Shutdown", aug 2026. https://insideevs.com/news/804775/gm-lg-ultium-cells-production-restart-ohio/
[5] GM Authority, "Ultium Cells Ohio plant production restarting after 7-month shutdown", aug 2026. https://gmauthority.com/blog/2026/08/ultium-cells-ohio-plant-production-restarting-after-7-month-shutdown/
[6] Kbmaeil, bezoek vice-minister 2024-01-29: anodefabriek in Pohang Blue Valley Nationaal Industrieterrein. https://kbmaeil.com/article/202401290383259
[7] POSCO Newsroom (KR): anodefabriek in Blue Valley, 8 kt/j, uitbreiding naar 13 kt/j (via zoekresultaat, pagina gaf 502). https://newsroom.posco.com/kr/?p=94993
[8] OSM Nominatim: Ultium Cells, Tod Avenue SW, Lordstown, man_made=works, 41.1525103, -80.8636186 (way 1165459849). https://nominatim.openstreetmap.org
[9] OSRM-demo (router.project-osrm.org): corridorindicatie b1 148,2 km en b4 513,9 km, via-puntkandidaten (geen gepubliceerde km).
[10] Eigen briefs: `kobalt-huayou-gunsan.md` (Busan), `ree-cheongju-sanmarcos.md` (aanloop kade → knoop), `grafiet-chedde-seadrift.md` (Seagirt, via-punten I-695/Hancock) en MARNET-droogloop (zee 18.868,9 km, snaps 10,12 / 2,67 km).
[sat] `v2/build-cache/satcheck/sat-grafiet-pohang-warren-{pohang,pohang-z16,pohang-z17,warren}.png`; hergebruikt `sat-kobalt-huayou-gunsan-busan-newport.png`, `sat-nikkel-zimplats-springs-seagirt.png`.

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
`bash v2/tools/bak_stromen.sh grafiet-pohang-warren` → `v2/data/stroomroute-grafiet-pohang-warren.json` (227,7 KB, versie 2, lonlat), functie `bak_grafiet_pohang_warren`, 4 benen, 19.530,4 km, 4 markers.

| # | modaliteit | km | naad naar vorig been | toets |
|---|---|---|---|---|
| b1 | truck Pohang → Busan New Port | 147,5 | - | OSRM-indicatie 148 (-0,3%); geen wegkm, hemelsbreed 117 |
| b2 | zee, STIPPEL haven-aanloop Busan | 10,8 (rechte lijn 10,1) | 0,00 | letterlijke kopie `ree-cheongju-sanmarcos-aanloop-busan` (md5 5b1e99f8) |
| b3 | zee MARNET zeeknoop 5621 → Seagirt | 18.868,9 | 0,00 | droogloop gelijk; Seagirt snapt 2,67 km (zeeknoop 4839) |
| b4 | truck Seagirt → Ultium Lordstown | 503,2 | 2,67 (zee-snap < 5 km, geen aanloop) | OSRM-indicatie 514 (-2,1%); geen wegkm, hemelsbreed 423 |

**Recept.** b1: profiel `grafiet-pohang-warren-pohang-busan` (zuid-korea, 6 via-punten uit §4, refs 65 16 1 551 55 69, venster 40, `eindToegangPrivaat`), `wegscan_puur.py`, alle snaps 0,00-0,04 km. b4: profiel `grafiet-pohang-warren-seagirt-lordstown` (us-maryland, us-pennsylvania, us-ohio, via-punten uit §4, refs I-695 I-70 I-76 I-80, venster 50), alle snaps 0,00-0,32 km. b2/b3: MARNET `35.0485,128.7268 → 39.2573,-76.5468`. Markers `gr-pohang-bluevalley`, `gr-busan-kade`, `gr-baltimore-seagirt`, `gr-ultium-lordstown`, alle 0,0 km van hun lijn.

**Stippel.** Alleen b2: Busan-kade ligt 10,1 km van zeeknoop 5621 (> 5 km, LAR-586), dus de bestaande aanloop is letterlijk gekopieerd (net reikt niet). b1, b3, b4 zijn doorgetrokken; "aannemelijk" staat in de beennamen en markernamen, niet in de lijnstijl. Geen lucht, spoor of leiding.

**Bevindingen / lessen.**
- Beide ±15%-toetsen zijn indicatie (geen gepubliceerde wegkm); beide scans liggen binnen 2,1% van de OSRM-indicatie, zonder bijgeschoven via-punt.
- Toets_knikken: 47 knikken >= 60 gr, 2 omkeringen, 0 terugloop; grootste keerlus 0,28 km bij I-70 Hancock (gesnoeid, 7 punten).
- Het id zegt `warren`, het eindpunt is Ultium Cells Lordstown (postadres Warren); titel en markernaam noemen Lordstown/Warren, het id blijft.
- Het gebouw in Blue Valley blijft aannemelijk (open punt §7); het Pohang-anker ligt 0,3 km van het toets-punt 35.9800,129.4955.
- De wegscans duurden 4 en 9 minuten (zuid-korea 132 s, drie VS-staten ~8 min); een tweede run is gecachet.
