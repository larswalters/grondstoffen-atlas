# Routebrief (licht) · Zeldzame aardmetalen · JL MAG Ganzhou → Yantian → Long Beach → Tesla Fremont (VS)

**stroom-id:** `ree-ganzhou-fremont` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Titel (bol):** Zeldzame aardmetalen · JL MAG Ganzhou → Yantian → Long Beach → Tesla Fremont (NdFeB-magneten, aannemelijk: haven uit handelsdata)
**Keten in één zin:** NdFeB-magneten van JL MAG's hoofdfabriek in Ganzhou per truck naar Yantian (Shenzhen), per containerschip over de Stille Oceaan naar Long Beach en per truck (I-5, Tejon Pass, I-580 Altamont) naar Tesla's autofabriek in Fremont.
**Welke as van het verhaal:** de Chinese NdFeB-magneten naar een Amerikaanse autofabriek (magneetmaker → OEM). JL MAG: 29,3 kt blanks gemaakt en 20,9 kt afgewerkte magneten verkocht in 2024, capaciteit 38,0 kt NdFeB/j bedrijfsbreed [4][7]; het Tesla-aandeel is niet gepubliceerd. Handelsrecords: Tesla 71 containers / 965.841 kg, lopend totaal over meerdere jaren, geen jaarvolume [2].

**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** haven Oakland vervalt, Long Beach ervoor in de plaats (ImportGenius koppelt Tesla aan Long Beach, geen Tesla- of JL MAG-record op Oakland gevonden [2][11]); geen Oakland-stukken en geen Oakland-satellietcheck. Het Tesla-anker snapt op een geïsoleerd component van privéwegen: het wegbeen eindigt op een via-punt op een openbare weg 0,38 km noordwestelijk. Titel noemt "aannemelijk".

## 1 · Ketenkaart
```
JL MAG Ganzhou `ree-ganzhou-jlmag` ──(b1 truck · G4511 via Longnan–Heyuan–Huizhou · 424 km, KOPIE ree-ganzhou-hanau)──►
Yantian-containerterminal `ree-yantian-kade` ──(b2 zee-aanloop, stippel · 6,6 km, KOPIE)──► zeeknoop 4553
──(b3 zee · MARNET · Zuid-Chinese Zee → Taiwanstraat → noordelijke Stille Oceaan · ~11.930 km)──► zeeknoop 4488
──(b4 haven-aanloop Long Beach, stippel · 8,5 km, KOPIE ree-yunsheng-longbeach)──► Long Beach-kade `ree-longbeach-kade`
──(b5 truck · I-710/I-5 → Tejon Pass → I-580 Altamont → Fremont · ~637 km, aannemelijk)──► Tesla Fremont `ree-fremont-tesla` ⏹
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | `ree-ganzhou-jlmag` → `ree-yantian-kade` | G4511 (Longnan) → Heyuan → Huizhou, LETTERLIJKE KOPIE ree-ganzhou-hanau b1 | 424,2 (gebakken; geen gepubliceerde wegkm, hemelsbreed 368) [8] | kopie `ree-ganzhou-hanau-weg-ganzhou-yantian.geojson` | nee |
| b2 | C | zee | `ree-yantian-kade` → zeeknoop 4553 (22.55820,114.33610) | haven-aanloop Yantian, KOPIE ree-ganzhou-hanau (kade 6,6 km van de knoop, LAR-586) | 6,6 [8][10] | kopie van de `--stippel`-regel | **ja** (net reikt niet) |
| b3 | C | zee (aannemelijk) | zeeknoop 4553 → zeeknoop 4488 (33.7039,-118.1945) | Zuid-Chinese Zee, Taiwanstraat of Filipijnen, noordelijke Stille Oceaan | 11.929,5 (eigen MARNET-meting, router) [10] | MARNET | nee |
| b4 | C | zee | zeeknoop 4488 → `ree-longbeach-kade` | haven-aanloop Long Beach, KOPIE ree-yunsheng-longbeach (kade 6,47 km van knoop 4488) | 8,5 [9] | kopie `ree-yunsheng-longbeach-aanloop-longbeach.geojson` (reisvolgorde knoop → kade) | **ja** |
| b5 | D | truck (aannemelijk) | `ree-longbeach-kade` → `ree-fremont-tesla` | I-710/I-5 → Tejon Pass (I-5) → I-5/I-580 → Altamont (I-580) → Fremont | hemelsbreed 534,8 km, geen wegkm; haalbaarheidstoets-scan 636,7 (indicatie) [11] | maak_stroombeen_weg (extract us-california) | nee |

Beennamen: b3 "… (aannemelijk: haven uit handelsdata)", b5 "… (aannemelijk: één bron, Fremont-adres uit Global Witness)". Geen luchtbeen: geen bron zegt dat deze magneten vliegen.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-ganzhou-jlmag` | magneetfabriek (kop b1) | JL MAG Rare-Earth, Ganzhou (hergebruikt `w-jlmag-ganzhou`) | 25.8406, 114.8663 | [7] sitelaag; [8] | bron-gelegd (hergebruikt letterlijk; sitelaag: industrieel gebouwencomplex in de Ganzhou-ontwikkelingszone) |
| `ree-yantian-kade` | overslag truck → zee | Yantian International Container Terminals, Shenzhen | 22.5734, 114.2741 | [8] | bron-gelegd (hergebruikt letterlijk uit ree-ganzhou-hanau; z15 daar: containerstapels en kadekranen) |
| `ree-longbeach-kade` | overslag zee → truck | containerkade Long Beach, westkade oostelijk havenbekken (zone Pier J, terminal niet bevestigd) | 33.7600, -118.2132 | [9] | aannemelijk (hergebruikt letterlijk uit ree-yunsheng-longbeach; z15 daar: portaalkranen en stapels) |
| `ree-fremont-tesla` | autofabriek (staart b5) | Tesla Fremont Factory, 45500 Fremont Blvd, Fremont | 37.4950, -121.9425 | [3][6] | bron-gelegd (z15 gezien: één groot fabriekscomplex met witte daken, goederenspoor en rangeerbundel direct oostelijk; kruis midden op het complex) |

## 4 · Via-punten (alleen b5; b1 is een kopie, b2–b4 zijn zee/aanloop)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b5 | 1 | Long Beach-kade (anker) | 33.7600, -118.2132 | kop; begint op de kade, niet in het havencentrum |
| b5 | 2 | Tejon Pass (Grapevine, I-5) | 34.8167, -118.8667 | pint I-5 over de Tehachapi/Grapevine-pas i.p.v. CA-99 door Bakersfield |
| b5 | 3 | Altamont Pass (I-580) | 37.7406, -121.6394 | pint de Central Valley → Bay Area-doorsteek via I-580, niet via Pacheco Pass (CA-152) |
| b5 | 4 | openbare weg bij Tesla (Quantum Drive) | 37.4977, -121.9451 | 0,38 km van het anker; het anker zelf ligt op privéterrein, laatste via op een openbare straat (z16: kruis op de noordrand van het complex, [12]) |
Refs: I 710, I 5, I 580, I 880/I 680 (zacht). Regio's: us-california. Scan-snaps van de drie tussenpunten nog te meten door de bak-agent (≤ 0,5 km; groter = via verleggen langs de snelweg, niet "bijna goed").

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| JL MAG Ganzhou | JL MAG Rare-Earth Co., Ltd | NdPr-metaal/legeringen → NdFeB-magneten | 38,0 kt NdFeB/j bedrijfsbreed; 29,3 kt blanks, 20,9 kt afgewerkt verkocht (2024) | [4][7] |
| Tesla Fremont | Tesla, Inc. | motoronderdelen (o.a. magneten) → voertuigen | 100.000 Model S/X + 550.000 Model 3/Y per jaar (fabriek, niet magneten) | [3] |

## 6 · Stoppunt
Bij Tesla's fabriek in Fremont: Global Witness noemt dit adres als bestemming van JL MAG-zendingen in 2023, en een auto is geen magneetketen meer; de motor- of rotorassemblage in de fabriek is niet publiek per leverancier.

## 7 · Open punten
- **Haven is aangenomen.** Global Witness noemt Fremont maar geen laad- of loshaven en geen JL MAG-vestiging [1]; Long Beach komt uit ImportGenius (Tesla #2 importeur, 71 containers) [2]. De Tesla-records lijken Long Beach te noemen maar tonen geen losse zending; de leverancierspagina noemt ook Los Angeles, Houston, Oakland en Tacoma als aankomstplaats van JL MAG-zendingen (zonder Tesla-koppeling).
- **Exporthaven Yantian onbewezen:** het enige voorbeeld-BL gaat Amoy (Xiamen) → Long Beach met consignee Robert Bosch, niet Tesla [2]; Yantian is hergebruikt uit ree-ganzhou-hanau. JL MAG-vestiging die levert (Ganzhou, Baotou, Ningbo) niet gepubliceerd.
- **Terminal in Long Beach onbekend;** de kade is een kadepunt, geen terminalnaam (zie ree-yunsheng-longbeach §7). Het stuk over de VS-weg is een aanname (geen bron noemt vervoer over land, ook niet trein; Tesla's eigen sporen zijn verwijderd [3]).
- **Geen wegkm** voor b5 (hemelsbreed 534,8; scan 636,7); de ±15%-toets is een indicatie.
- **Yicai 2020:** de Tesla-JL MAG-overeenkomst (21 sept 2020, orderbasis, geen hoeveelheden) noemt geen fabriek en geen Fremont [5]; dit is alleen contextbewijs dat de relatie bestaat.
- Het ontwerp noemde 38,0 kt als capaciteit uit SMM; de SMM-pagina noemt alleen 29,3 kt blanks en 20,9 kt verkocht [4]; het capaciteitscijfer staat in de sitelaag [7].

## 8 · Bronnen
[1] Global Witness, 23 mei 2024, Myanmar's rare-earth boom: JL Mag maakte in 2023 talrijke zendingen magneten naar Tesla's Fremont-fabriek (geen haven, geen aantallen). https://www.globalwitness.org/en/campaigns/natural-resource-governance/fuelling-the-future-poisoning-the-present-myanmars-rare-earth-boom/
[2] ImportGenius, JL MAG Rare-Earth Co., Ltd (Ganzhou), 274 zendingen 2006–2026; Tesla 71 containers / 965.841 kg, Long Beach; voorbeeld-BL Amoy → Long Beach. https://www.importgenius.com/suppliers/jl-mag-rare-earth-co-ltd
[3] Wikipedia, "Tesla Fremont Factory": 45500 Fremont Blvd, 37,495 N 121,9425 W; sporen verwijderd; capaciteit. https://en.wikipedia.org/wiki/Tesla_Fremont_Factory
[4] SMM, JL MAG 2024: 29.300 t blanks (+39,5%), 20.900 t verkocht, bezetting > 90%. https://news.metal.com/newscontent/103258207/JL-MAG-Rare-Earth-Sets-New-Highs-with-Over-90-Capacity-Utilization-in-2024
[5] Yicai Global, 23 sept 2020: JL Mag levert permanente magneten aan Tesla (Model 3 RWD), orderbasis. https://www.yicaiglobal.com/news/china-jl-mag-rare-earth-hits-limit-up-on-tesla-permanent-magnet-deal
[6] Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-ree-ganzhou-fremont-tesla.png` (z15), `…-lastvia.png` (z16).
[7] `v2/design/ree-sitelaag.json`, site `w-jlmag-ganzhou` (25,8406 / 114,8663; 38,0 kt NdFeB/j bedrijfsbreed).
[8] `v2/design/routebrieven/ree-ganzhou-hanau.md` §2/§3/§9: b1-kopie (424,2 km), Yantian-anker en -aanloop (6,6 km, zeeknoop 4553).
[9] `v2/design/routebrieven/ree-yunsheng-longbeach.md` §2/§3/§9: Long Beach-kade en handgelegde aanloop (8,5 km, zeeknoop 4488, kade 6,47 km).
[10] MARNET (`hecht_marnet.py route`), eigen meting 2026-10-29: zeeknoop 4553 → 4488 = 11.929,5 km.
[11] Haalbaarheidstoets M31 golf 11 voor `ree-ganzhou-fremont` (workflow-invoer): Oakland vervalt, Long Beach; truck 636,7 km; Tesla-anker op geïsoleerd component.
[12] OSM Nominatim, reverse op 37,4977/-121,9451: Quantum Drive (residential), Warm Springs, Fremont. https://nominatim.openstreetmap.org

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
Bestand `v2/data/stroomroute-ree-ganzhou-fremont.json` (186,1 KB, versie 2, lonlat), functie `bak_ree_ganzhou_fremont` in `bak_stromen.sh`, profiel `ree-ganzhou-fremont-longbeach-fremont` in `maak_stroombeen_weg.py`. Totaal 12.992,0 km, 5 benen, 4 markers, alle naden 0,000 km.

| # | modaliteit | km gebakken | bron / norm | stippel | geometrie |
|---|---|---|---|---|---|
| b1 | truck | 424,2 | geen wegkm, hemelsbreed 368 (indicatie) | nee | LETTERLIJKE KOPIE ree-ganzhou-hanau b1 |
| b2 | zee | 6,6 | gemeten | ja: net reikt niet (kade 6,6 km van knoop 4553) | LETTERLIJKE KOPIE stippel-regel ree-ganzhou-hanau |
| b3 | zee | 11.929,5 | eigen MARNET-meting 11.929,5 | nee | MARNET knoop 4553 naar knoop 4488, snap 0,000 km |
| b4 | zee | 8,5 | gebakken 8,5 | ja: handgelegd, kade 6,47 km van knoop 4488 | LETTERLIJKE KOPIE geojson ree-yunsheng-longbeach (knoop naar kade), naad met b3 = 0,000 km |
| b5 | truck | 623,2 | geen wegkm; scan 636,7 = indicatie, -2,2% t.o.v. 637 | nee | nieuw profiel, extract us-california |

**Markers:** ree-ganzhou-jlmag, ree-yantian-kade en ree-longbeach-kade liggen op de lijn (0,000 km); ree-fremont-tesla ligt 0,378 km van het lijn-eindpunt (Quantum Drive, privaat terrein; geen last-mile-been).

**Recept b5.** Scan via `wegscan_puur.py` (us-california, ~9 min scan + Dijkstra). Via-punten (lon, lat): Long Beach-kade, Tejon Pass op de I-5, Altamont Pass (I-580), Quantum Drive. Segmenten 153,5 + 421,4 + 48,1 km. Route: centrum Los Angeles, I-5 noord over Grapevine, Central Valley, I-580 Altamont, Fremont; niet CA-99 en niet Pacheco.
- **Via verlegd (⚠):** het brief-via Tejon (-118.8667, 34.8167) snapte op 1,12 km van de I-5. Verlegd 1,1 km naar een punt op de gescande I-5 (-118.8825, 34.8169), zelfde corridor; snap nu 0,01 km, km 623,2 i.p.v. 623,5. Altamont snapt op 0,45 km (binnen 0,5).
- **Geen last-mile-stippel** bij Tesla: de lijn eindigt op het via op Quantum Drive, 0,38 km van het anker.
- Eerste mijl over kleine klassen 2,44 km (service, unclassified), laatste mijl 0,34 km.

**Toets.** Contract ok (versie 2, lonlat, modaliteiten in de set, elk been >= 2 punten). `toets_rechte_benen`: alleen de Yantian-stippel (factor 1,002, stippel met reden). `toets_knikken`: b5 15 spikes van 5-10 m op kruispunten, geen omkering; b3 twee krappe bochten bij de Long Beach-aanvaart (R 3-6 km, MARNET).

**Bevinding (niet door mij te wijzigen).** De gedeelde b1-kopie (ree-ganzhou-hanau, 424,2 km) heeft een TERUGLOOP bij 23.7447,114.7008 (11 m, 152,5 graden) en een scherpe bocht (175 graden) bij Yantian 22.5723,114.2753; dat zit in het bronbestand van ree-ganzhou-hanau.

**Lessen.** (1) `maak_stroombeen_weg.py` heeft gemengde regeleinden (CRLF met enkele LF-regels): voeg in via een bytes-edit op de ankerregel zonder aanname over het regeleinde, anders is een `replace` stil een no-op. (2) De scan-cache hangt aan de via-punten: een verlegd via kost een volledige herscan (us-california ~9 min). (3) Wikipedia-coordinaat van een pas ligt vaak naast de snelweg: eerst de snap meten en de via naar de gescande weg verleggen.
