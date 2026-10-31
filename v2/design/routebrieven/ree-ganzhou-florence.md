# Routebrief (licht) · Zeldzame aardmetalen · JL MAG Ganzhou → Xiamen → Long Beach → Bosch Steering Florence (VS)

**stroom-id:** `ree-ganzhou-florence` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Titel (bol):** Zeldzame aardmetalen · JL MAG Ganzhou → Xiamen → Long Beach → Bosch Steering Florence KY (speed-magneten, aannemelijk: één bron)
**Keten in één zin:** Speed-magneten (HS 8505.11, kleine sensormagneten, NdFeB niet bevestigd) van JL MAG in Ganzhou gaan per truck (G76) naar de containerhaven Xiamen, per containerschip naar Long Beach en per truck (I-15, I-40, I-44, I-64, I-71) naar Bosch Automotive Steering in Florence, Kentucky.
**Welke as van het verhaal:** China naar het Amerikaanse binnenland, magneetmaker → Tier-1 stuurinrichtingen. Lopend totaal 15 containers / 7.885 kg = 0,0079 kt magneten (peiljaar 2026, laatste B/L 2026-10-16: 743 kg, daarvoor 600 kg op 2026-09-30 en 2026-09-13) [1][2]; JL MAG bedrijfsbreed 29,3 kt blanks gemaakt en 20,9 kt afgewerkt verkocht in 2024 [3], capaciteit 38,0 kt NdFeB/j (sitelaag `w-jlmag-ganzhou`) [4].

**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** geen in de keten. Eén verscherping: het adres 4175 Aero Parkway is geen los logistiek notify-adres maar ligt op de Bosch-steeringcampus (OSM: "Bosch Automotive Building" op 3 m; Bosch Automotive Steering, 15 Spiral Dr, 0,17 km oostelijker; drie gebouwen in Florence) [5][11]. Het eindpunt blijft het ontwerp-eindpunt.

## 1 · Ketenkaart
```
JL MAG Ganzhou `ree-ganzhou-jlmag` ──(b1 truck · G76 Xiamen-Chengdu · 445,3 km, KOPIE ree-ganzhou-elpaso b1)──►
Xiamen Haicang CT `ree-xiamen-haicang` ──(b2 aanloop, stippel · 5,7 km, KOPIE)──► zeeknoop 5576
──(b3 zee · MARNET · Taiwanstraat → noordelijke Stille Oceaan · 11.479,5 km, KOPIE)──► zeeknoop 4488
──(b4 aanloop Long Beach, stippel · 8,5 km, KOPIE)──► Long Beach-kade `ree-longbeach-kade`
──(b5 truck · I-710 → I-10 → I-15 → I-40 → I-44 → I-64 → I-71 · hemelsbreed 3.043 km, geen wegkm, aannemelijk)──► Bosch Steering Florence `ree-florence-bosch` ⏹
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | `ree-ganzhou-jlmag` → `ree-xiamen-haicang` | G76 Xiamen-Chengdu (S61), LETTERLIJKE KOPIE ree-ganzhou-elpaso b1 | 445,3 (gebakken in die stroom; geen wegkm) [12] | kopie `ree-ganzhou-elpaso-weg-ganzhou-haicang.geojson` | nee |
| b2 | D | zee (haven-aanloop) | `ree-xiamen-haicang` → zeeknoop 5576 (24.4515,117.9163) | kade 5,7 km van de knoop (> 5 km, LAR-586), LETTERLIJKE KOPIE ree-ganzhou-elpaso b2 | 5,7 (rechte lijn) [12] | kopie `--stippel`-regel uit `bak_ree_ganzhou_elpaso` | **ja** (net reikt niet) |
| b3 | D | zee (aannemelijk: haven uit handelsdata) | zeeknoop 5576 → zeeknoop 4488 (33.7039,-118.1945) | Taiwanstraat, noordelijke Stille Oceaan; B/L Xin Ya Zhou 177E, COSCO SEA3 roept Xiamen en Long Beach aan [1][10]; KOPIE ree-ganzhou-elpaso b3 | 11.479,5 (MARNET, snap 0,000) [12] | MARNET | nee |
| b4 | D | zee (haven-aanloop) | zeeknoop 4488 → `ree-longbeach-kade` | Long Beach-havenbekken, kade 6,47 km van de knoop; KOPIE ree-ganzhou-elpaso b4 | 8,5 (handgelegd) [12] | kopie `ree-yunsheng-longbeach-aanloop-longbeach.geojson` | **ja** |
| b5 | D | truck (aannemelijk: één bron, productregel speed magnet, route niet bekend) | `ree-longbeach-kade` → `ree-florence-bosch` | I-710/I-105/I-605/I-10 → I-15 (Cajon Pass) → I-40 (Barstow, Needles, Santa Rosa, Amarillo) → I-44 (Oklahoma City, Tulsa, Springfield) → I-64 (St. Louis, Illinois, Indiana) → I-265/KY 841 → I-71 | hemelsbreed 3.043 km, geen wegkm (OSRM 3.527 is OSM-afgeleid, indicatie) [7] | maak_stroombeen_weg, 9 extracts | nee |
Beennamen: b3 "… (aannemelijk: haven uit handelsdata)"; b5 "… (aannemelijk: één bron, productregel speed magnet)". Geen luchtbeen: de B/L noemt een containerschip. Geen last-mile-been: b1 en b5 eindigen op de site-ankers (Florence-anker 54 m van de weg). b1-b4 zijn 77 procent van de km en bewust kopie; nieuw zijn alleen b5 en de afnemer.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-ganzhou-jlmag` | magneetfabriek (kop b1) | JL MAG Rare-Earth, 81 West Jinling Rd, Ganzhou (hergebruikt letterlijk uit ree-ganzhou-elpaso, sitelaag `w-jlmag-ganzhou`) | 25.8406, 114.8663 | [4][12] | bron-gelegd (hergebruikt; daar: industrieel complex in de Ganzhou-zone) |
| `ree-xiamen-haicang` | overslag truck → zee | Xiamen Haicang Container Terminal (hergebruikt letterlijk uit ree-ganzhou-elpaso) | 24.4585, 117.9720 | [12] | bron-gelegd (hergebruikt; daar: containerstapels en kranen; terminal voor deze lading niet bevestigd) |
| `ree-longbeach-kade` | overslag zee → truck | containerkade Long Beach (hergebruikt letterlijk uit ree-yunsheng-longbeach) | 33.7600, -118.2132 | [12] | aannemelijk (hergebruikt; terminal niet bevestigd) |
| `ree-florence-bosch` | afnemer (staart b5) | Robert Bosch Automotive Steering, 4175 Aero Parkway, Florence KY 41042 | 39.0185, -84.6458 | [1][5] ArcGIS score 100, Nominatim 39.0184/-84.6458 | bron-gelegd (z15/z16 gezien: kruis op een groot wit distributiegebouw direct aan Aero Parkway, in een bedrijventerrein zuidoostelijk van de CVG-vrachtplatforms; B/L-notify noemt Bosch Automotive Steering; OSM-gebouwnaam Bosch) [6] |
Geen markt- of stadscentroïde als anker. Het Spiral Dr-adres (39.0189, -84.6439, plantnaam in OSM) ligt 0,17 km verder en bevestigt de campus, niet als apart anker.

## 4 · Via-punten (alleen b5; b1 is kopie, b2-b4 zee/aanloop)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b5 | 1 | Long Beach-kade (anker) | 33.7600, -118.2132 | kop op de kade (weg op 275 m) |
| b5 | 2 | I-15 Cajon Pass | 34.3114, -117.4747 | pint I-15 noordwaarts naar Barstow i.p.v. I-10 oost via Blythe/Phoenix; letterlijk uit profiel `ree-mountainpass-yokohama-mountainpass-longbeach` (gescand, op de weg) |
| b5 | 3 | I-40 bij Needles | 34.8218, -114.5965 | pint I-40 door de Mojave i.p.v. I-15 via Las Vegas en US-93 (OSRM-vertex, 1 m van de weg) |
| b5 | 4 | I-40 Santa Rosa NM | 34.9472, -104.6782 | pint I-40 door New Mexico (OSRM-vertex, 0 m; geen stad, wel doorgaande weg) |
| b5 | 5 | I-40 Amarillo | 35.1948, -101.8699 | pint I-40 door de Texas Panhandle i.p.v. US-287/I-27 zuidwaarts; letterlijk uit profiel `grafiet-novonix-nevada` (op de hoofdrijbaan) |
| b5 | 6 | I-44 Turner Turnpike, noord van Oklahoma City | 35.5993, -97.4246 | pint de afslag van I-40 naar I-44 (Tulsa, Springfield) i.p.v. I-40 door naar Memphis; OSRM-vertex 4 m van de weg |
| b5 | 7 | I-44 bij Lebanon MO | 37.6193, -92.6919 | pint I-44 door de Ozarks naar St. Louis, geen I-70 via Kansas City (OSRM-vertex, 5 m) |
| b5 | 8 | I-64 Illinois, oost van Belleville | 38.4946, -89.6018 | pint de oversteek van de Mississippi en I-64 oostwaarts i.p.v. I-70/I-57 (OSRM-vertex, 5 m) |
| b5 | 9 | I-71 zuid van Carrollton | 38.5651, -85.1933 | pint I-71 noordoostwaarts naar Florence i.p.v. I-64 door naar Lexington en I-75 (OSRM-vertex, 1 m) |
| b5 | 10 | Bosch Steering (anker) | 39.0185, -84.6458 | staart; 54 m van de weg, geen aparte last-mile-via |
Refs b5 (zacht): I 710, I 105, I 605, I 10, I 15, I 40, I 44, I 64, I 265, I 71. Regio's: us-california, us-arizona, us-new-mexico, us-texas, us-oklahoma, us-missouri, us-illinois, us-indiana, us-kentucky (geen Kansas: I-44 raakt Kansas niet, gemeten op de OSRM-route). Venster 75 km; eindToegangPrivaat True. Alle vias liggen op de doorgaande weg, geen stadscentrum; snap > 0,5 km = via verleggen langs de snelweg.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| JL MAG Ganzhou | JL MAG Rare-Earth Co., Ltd | NdPr-metaal/legeringen → magneten | 38,0 kt NdFeB/j bedrijfsbreed; 29,3 kt blanks, 20,9 kt afgewerkt (2024) | [3][4] |
| Bosch Steering Florence | Robert Bosch Automotive Steering LLC | magneten (speed magnets) → stuursystemen (EPS, kolommen) | niet gepubliceerd; plant ~1.300 medewerkers in Noord-Kentucky (2015) | [11] |

## 6 · Stoppunt
Bij de Bosch-steeringcampus in Florence: de B/L noemt Robert Bosch Automotive Steering als notify party op dit adres; wat Bosch met de speed-magneten in de stuursystemen doet en waar die heen gaan is niet gebrond.

## 7 · Open punten
- **Productregel is "8505.11 Speed Magnet"**: kleine sensormagneten, NdFeB niet bevestigd; het volume is daarom magneten, geen REO [1].
- **Vervoer in de VS onbekend** (truck, intermodaal of LTL) en de Xiamen-terminal; de route over land is aangenomen (OSRM-kortste weg over I-15/I-40/I-44/I-64/I-71) en geen bron noemt een corridor.
- **Losplaats Long Beach of Los Angeles:** de importerspagina noemt Long Beach voor de laatste B/L, de leverancierspagina Los Angeles [1][2]; Long Beach-anker uit de bestaande kopie behouden. De laad-haven Amoy komt uit de haalbaarheidstoets, niet uit mijn eigen fetch.
- **Aantallen niet consistent:** de pagina's tonen 15 containers en 7.885 kg tegenover drie zichtbare zendingen van 1.943 kg [1]; "lopend totaal" zonder jaarvolume.
- **Geen wegkm** voor b5 (hemelsbreed 3.043 km, OSRM 3.527,2 km); de ±15%-toets is een indicatie. Wikipedia noemt wel I-40 (4.114 km totaal, westeinde Barstow) maar geen deellengte [8][9].
- **Bestandsgrootte:** b5 met 9 extracts en 3.500 km wordt waarschijnlijk > 300 KB (vlag, geen fout). Zelfde begin als `ree-ganzhou-elpaso`; alleen b5 en afnemer zijn nieuw (toegestaan, andere afnemer en binnenlandbeen).

## 8 · Bronnen
[1] ImportGenius, Robert Bosch LLC Distribution: 15 ctrs / 7.885 kg, B/L FLXT00004182605A 2026-10-16, Xin Ya Zhou 177E, Long Beach, notify Robert Bosch Automotive Steering 4175 Aero Parkway Florence KY, "8505.11 Speed Magnet", 743 kg. https://www.importgenius.com/importers/robert-bosch-llc-distribution
[2] ImportGenius, JL MAG Rare-Earth: zelfde zendingen (2026-10-16 743 kg, 2026-09-30 600 kg), leverancierspagina noemt Los Angeles. https://www.importgenius.com/suppliers/jl-mag-rare-earth-co-ltd
[3] SMM 2025-04-01, JL MAG 2024: ca. 29.300 t blanks, 20.900 t afgewerkt, bezetting > 90%. https://news.metal.com/newscontent/103258207/JL-MAG-Rare-Earth-Sets-New-Highs-with-Over-90-Capacity-Utilization-in-2024
[4] `v2/design/ree-sitelaag.json`, site `w-jlmag-ganzhou` (25,8406 / 114,8663; 38,0 kt NdFeB/j).
[5] Nominatim: 4175 Aero Parkway = "Bosch Automotive Building" 39.01844/-84.64578; 15 Spiral Drive = Bosch Automotive Steering 39.01890/-84.64393. ArcGIS World Geocoder: 4175 Aero Pkwy 39.01845/-84.64576, 15 Spiral Dr 39.01856/-84.64294 (score 100). https://nominatim.openstreetmap.org
[6] Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-ree-ganzhou-florence-bosch.png` (z15) en `…-bosch-z16.png`.
[7] OSRM (router.project-osrm.org), eigen meting 2026-10-31: Long Beach-kade → Florence 3.527,2 km; vertices en nearest-snaps van de via-punten; route raakt geen Kansas. OSM-afgeleid.
[8] Wikipedia, Interstate 40: 2.556,61 mi (4.114,46 km); westelijk uiteinde op I-15 in Barstow. https://en.wikipedia.org/wiki/Interstate_40
[9] Wikipedia, Interstate 44: Oklahoma City – St. Louis. https://en.wikipedia.org/wiki/Interstate_44
[10] Container News 2024-07-05, COSCO SEA3: Kaohsiung – Xiamen – Yantian – Long Beach; OOCL London Xiamen → Long Beach. https://container-news.com/cosco-launches-maiden-voyage-of-transpacific-service
[11] Cincinnati Business Courier via NOLN 2015-12-11: Bosch Automotive Steering, 15 Spiral Drive, Florence, drie gebouwen, ~1.300 medewerkers. https://www.noln.net/articles/919-one-of-cincinnati-s-largest-manufacturers-plans-expansion
[12] `v2/design/routebrieven/ree-ganzhou-elpaso.md` §2/§3/§9 en functie `bak_ree_ganzhou_elpaso`: b1-b4, ankers jlmag, Haicang en Long Beach.
[13] Haalbaarheidstoets M31 golf 19 voor `ree-ganzhou-florence` (workflow-invoer).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Bestand:** `v2/data/stroomroute-ree-ganzhou-florence.json` (562,0 KB: boven de 300 KB-vlag, alleen een vlag; b5 heeft 22.914 punten). Functie `bak_ree_ganzhou_florence` in `v2/tools/bak_stromen.sh`, profiel `ree-ganzhou-florence-longbeach-bosch` in `v2/tools/maak_stroombeen_weg.py`. Totaal 15.464,2 km, 5 benen, 4 markers, 2 stippel (2 van 5 benen, 0,1 procent van de km), alle naden 0,00 km.

| # | modaliteit | km | stippel | herkomst |
|---|---|---|---|---|
| b1 | truck | 445,3 | nee | LETTERLIJKE KOPIE ree-ganzhou-elpaso b1 (`ree-ganzhou-elpaso-weg-ganzhou-haicang.geojson`) |
| b2 | zee | 5,7 | ja: net reikt niet | LETTERLIJKE KOPIE `--stippel`-regel ree-ganzhou-elpaso b2 (Haicang, kade 5,7 km van knoop 5576) |
| b3 | zee | 11.479,5 | nee | MARNET kade-knoop 5576 naar knoop 4488, snap 0,000, kopie b3 |
| b4 | zee | 8,5 | ja: net reikt niet | LETTERLIJKE KOPIE `ree-yunsheng-longbeach-aanloop-longbeach.geojson` (Long Beach, kade 6,47 km van knoop 4488) |
| b5 | truck | 3.525,2 | nee | NIEUWE wegscan `wegscan_puur.py`, profiel `ree-ganzhou-florence-longbeach-bosch`, 9 extracts |

**Toets b5:** 3.524,9 km (getekend 3.525,2) tegen OSRM-indicatie 3.527,2 km = -0,1 procent; er is geen echte wegkm, dus de +-15 procent-toets is een indicatie. Hemelsbreed 3.043 km (omwegfactor 1,16). Segmenten: Long Beach-kade naar Cajon 130,4 (OSRM 126,9), Cajon naar Needles 314,8, Needles naar Santa Rosa 1.035,5, naar Amarillo 268,6, naar OKC 435,3, naar Lebanon MO 513,4, naar Belleville 324,2, naar Carrollton 422,1, naar Bosch 80,8. Alle via-snaps 0,00-0,27 km, geen via verlegd of weggelaten. Kop snapt 0,27 km, staart 0,05 km. Eerste mijl 0,99 km en laatste mijl 1,99 km over kleine klassen (residential, service, unclassified).
**Markers (4):** jlmag, Haicang, Long Beach-kade en Bosch liggen 0,000 km van de lijn. Geen luchtbeen, spoor, binnenvaart, leiding of last-mile-been; fase E vervalt (stoppunt Bosch-steeringcampus).
**Knikken:** 43 knikken >= 60 graden; de twee teruglopen van b5 zijn een 23 m-rampluskje bij 34.0656,-118.1641 (I-710/I-10-knooppunt) en een 9 m-wiebel op de kade 33.7669,-118.2129; b1 heeft er twee in de Haicang-terminal (kopie, niet aangeraakt). Rechte lijnen: alleen de twee gedocumenteerde stippels.
**Laatste km bij Florence:** de scanner kent geen eenrichting; de laatste 12 km van b5 zijn 12,1 km tegen OSRM 13,3 km (zelfde corridor, I-71 naar Aero Parkway), en de lijn eindigt met enkele spikes van 4-10 m op de Aero Parkway-aansluiting bij het anker (geen last-mile-been).
**Lessen:** (1) ree-gf is bezet, registersleutel `ree-gfl`. (2) Een 9-extract-scan op het reuzenpaar us-california/us-texas kostte ca. 10 min met een weg- en een reus-slot (Texas 272 s). (3) Een parallelle edit op `bak_stromen.sh` gaf eenmalig een syntaxfout bij de eerste run (andermans functie halverwege geschreven); een tweede run was schoon. (4) Een 3.500 km-truckbeen levert ca. 560 KB; de vlag is verwacht.
