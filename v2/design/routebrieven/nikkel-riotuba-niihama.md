# Routebrief (licht) · nikkel — Rio Tuba/Coral Bay HPAL (Palawan) → Niihama (Ehime)

**stroom-id:** `nikkel-riotuba-niihama` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** nikkel-kobalt-mixed sulfide (MS) uit de Coral Bay HPAL-plant (CBNC, SMM) naast de Rio Tuba-mijn (Bataraza, zuidpunt Palawan) gaat per lokale weg naar de RTN-pier, per zeeschip door de Sulu Sea, Mindoro-straat, Luzon-straat en langs Okinawa naar de Seto-binnenzee en lost bij de Niihama Nickel Refinery (SMM, Ehime) voor elektrolytisch nikkel.
**Welke as van het verhaal:** *tweede Filipijnse HPAL-patroon, via de zuidwestelijke corridor* — naast Taganito (Mindanao, Filipijnenzee) de oudste HPAL (2005) op Palawan; nameplate 24 kt Ni/jaar als MS [6] (peiljaar 2025, capaciteit; record-productie 2012: 23,9 kt Ni [8], 2024-productie niet gevonden). **Zwakste aanvulling van de golf**; Coral Bay kan binnen enkele jaren stoppen [4] (zie §7). Aannemelijk: één bron voor de bestemming Niihama, geen bron voor pier en route.

## 1 · Ketenkaart
```
Coral Bay HPAL-plant `ni-coralbay-plant` ──(b1 truck · lokale weg via Rio Tuba-dorp · 9,2 km gemeten)──► RTN-pier `ni-riotuba-pier`
   ──(b2 zee · haven-aanloop, stippel · 286,7 km)──► MARNET-zeeknoop 5444 (8.4000,120.0500)
   ──(b3 zee · MARNET · 3.521,9 km)──► MARNET-zeeknoop 5746 (34.0720,133.0479)
   ──(b4 zee · haven-aanloop, stippel · 25,7 km, letterlijke kopie)──► Niihama Nickel Refinery `ni-niihama-refinery` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-coralbay-plant` → `ni-riotuba-pier` | plantweg → Rio Tuba-dorp (8.53, 117.43) → depotweg naar de pier; één corridor, geen keuze | hemelsbreed 6,5 km, geen wegkm (gemeten 9,2) | maak_stroombeen_weg (profiel `nikkel-riotuba-niihama-plant-pier`, extract filipijnen, via `wegscan_puur.py`) | nee |
| b2 | B | zee (haven-aanloop) | `ni-riotuba-pier` → zeeknoop 5444 | over water, Sulu Sea; knik via 8.4700,117.5250 om de kaap bij 117.49/8.50 | 286,0 hemelsbreed, 286,7 getekend (eigen meting) | handgemaakt geojson (maak_havenaanloop hing: timeout 300) | ja — MARNET reikt niet (knopen daar 150+ km uit elkaar) |
| b3 | B | zee | zeeknoop 5444 → zeeknoop 5746 | Sulu Sea, Mindoro-straat, Luzon-straat, Okinawa, Seto-binnenzee | 3.521,9 (MARNET, gemeten; toets 3.521,9) | MARNET | nee |
| b4 | B | zee (haven-aanloop) | zeeknoop 5746 → `ni-niihama-refinery` | — | 25,7 (kopie) | letterlijke kopie `nikkel-taganito-niihama-aanloop-niihama.geojson` | ja — zelfde aanloop als taganito b4 |

Geen mijnbeen: de plant ligt tegen de Rio Tuba-mijn aan [1][2][5]; het erts gaat door de eigen mijn-/plantinfrastructuur (limoniet naar de HPAL), niet over de openbare weg. Zeeknoop 5444 is gekozen boven 5431 (7.1436,117.3625): 5431 ligt 151 km zuidelijk van de pier en geeft 3.849 km + een bocht tegen 3.522 km + rechte aanloop (toets).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-coralbay-plant` | verwerking (HPAL, MS) | Coral Bay Nickel Corporation, Rio Tuba, Bataraza | 8.5585, 117.4225 | [1][2][5] | bron-gelegd (z15/z16 gezien: tank-/autoclaafbatterij en procesgebouwen, rode tailings en mijnterrassen direct noordoost; deels onder wolk) |
| `ni-riotuba-pier` | overslag (pier, MS-uitvoer) | RTN-pier Rio Tuba (SMM-persbericht: Coral Bay gebruikt "RTN's existing port facilities") | 8.5030, 117.4515 | [1] | aannemelijk (z16 gezien: pier van de kust naar het zuidoosten, twee schepen afgemeerd, tanks/opslag aan de wal; geen bron geeft een coördinaat) |
| `ni-niihama-refinery` | losplek + raffinaderij | Niihama Nickel Refinery, SMM | 33.9669, 133.2658 | [10] | bron-gelegd — hergebruikt uit `nikkel-taganito-niihama` (z15: industrieterrein met havenbekken) |

Sitelaag-punt `w-coralbay-riotuba` (8.5700, 117.4190, Wikipedia/Mindat [9]) ligt ~1,4 km noord op het mijn-/tailinggebied, niet op de plant; dat is een sitelaag-fout (niet door mij gewijzigd, zie §7).

## 4 · Via-punten
Geen. b1 volgt één corridor (plantweg → dorp → pier) zonder splitsing waar een keuze bestaat; de weg is 9,2 km, onder het 3–8 via-punten-criterium. De zeebenen routeren via MARNET, niet via via-punten.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Coral Bay HPAL (CBNC) | SMM (100% sinds begin 2025; Nickel Asia verkocht 15,625%) | limoniet (RTN) → MS | 24 kt Ni + 2,5 kt Co/jaar nameplate; productie 2012 23,9 kt Ni (record) | [6][7][8] |
| Niihama Nickel Refinery | SMM | MS → elektrolytisch Ni (+ Co) | 65 kt kathode/jaar (sitelaag) | [10] |

## 6 · Stoppunt
Niihama (elektrolytisch nikkel/kobalt): geen bron noemt een vervolgfabriek die specifiek dit metaal afneemt; fase D en E vervallen (zelfde argument als `nikkel-taganito-niihama`).

## 7 · Open punten
- **Pier niet gedocumenteerd:** RTN-pier is aannemelijk (SMM noemt RTN's havenfaciliteiten, geen coördinaat); het MS-schip legt mogelijk elders (rede/steiger) aan.
- **Wegkm onbekend:** b1 is 9,2 km gemeten (toets-indicatie ~9), geen publicatie; weg door Rio Tuba-dorp niet bevestigd als MS-route.
- **Haven-aanloop b2 is handgemaakt:** `maak_havenaanloop.py` hing 300 s op het 286 km-pad (geen tweede poging); één knik (8.4700,117.5250) over open water omdat de rechte lijn 0,2 km NE-land schampte. Echte vaarroute (Balabac of rondom Palawan-zuidpunt) onbekend; MARNET-knopen in de Sulu Sea zijn grof.
- **Toekomst:** SMM verwacht stopzetting van het CBNC-plant binnen enkele jaren [4]; petitie (dec 2025) en milieuklacht lopen [3]. Status nu operating, niet gegarandeerd; stroom kan ophouden te bestaan.
- **Productie 2024** niet gevonden (alleen nameplate 24 kt Ni en Co 2,5 kt [6]).
- **Sitelaag `w-coralbay-riotuba`** (8.5700, 117.4190) staat ~1,4 km van de plant: centraal gelijk te trekken met `ni-coralbay-plant`.
- **Start-keerpunt b1:** `toets_knikken` meldt een omkering van 177° bij 8.55845,117.42150 (de ankerstub ~80 m naast de eerste wegvertex), geen terugloop.

## 8 · Bronnen
[1] SMM-persbericht 2005-03 over Coral Bay (plant naast Rio Tuba Mine, gebruikt RTN's port facilities, MS naar Niihama) — via de haalbaarheidstoets; smm.co.jp was vandaag niet bereikbaar, niet zelf herlezen. https://www.smm.co.jp/en/news/release/uploaded_files/20060328e.pdf
[2] Coral Bay Nickel Corporation, bedrijfspagina: HPAL in Rio Tuba, Bataraza; lijn 1 2005, lijn 2 2009. https://cbnc.com.ph/the-company
[3] FoE Japan, 2026-06-08: petitie tegen CBNC/RTNMC, alle MS naar SMM-fabrieken in Japan. https://foejapan.org/en/issue/20260608/29927/
[4] FoE Japan, 2025-12-05: SMM verwacht stopzetting CBNC binnen enkele jaren. https://foejapan.org/en/issue/20251205/27117/
[5] Nickel Asia, Rio Tuba Nickel Mining Corp: Barangay Rio Tuba, zuidpunt Palawan; levert limoniet aan het aangrenzende CBNC. https://nickelasia.com/subsidiaries/rio-tuba-nickel-mining-corporation
[6] Argus, 2025-01-07: SMM wordt volledig eigenaar; Coral Bay 24.000 t Ni + 2.500 t Co per jaar. https://argusmedia.com/es/news-and-insights/latest-market-news/2644488-smm-to-wholly-own-philippine-coral-bay-nickel-smelter
[7] Tribune (PH), 2025-02-03: Sumitomo krijgt 100% CBNC. https://tribune.net.ph/2025/02/03/sumitomo-secures-full-cbnc-ownership
[8] Nickel Asia jaarverslag 2012 (record 23.891 t Ni in MS) en OneMine 2004-paper (MS naar Niihama voor MCLE-elektrowinning), via zoekresultaat. https://nickelasia.com/assets/documents/Annual-Report-2012.pdf · https://onemine.org/documents/development-of-process-design-for-coral-bay-nickel-project
[9] Wikipedia, Rio Tuba mine (8.570 N, 117.419 E; 46,8 kt Ni in 2022 uit de mijn, Nickel Asia). https://en.wikipedia.org/wiki/Rio_Tuba_mine
[10] Esri World Imagery z12/z15/z16 (sat_check, `v2/build-cache/satcheck/sat-nikkel-riotuba-niihama-*.png`); Niihama-anker en aanloop uit `routebrieven/nikkel-taganito-niihama.md`; sitelaag `nikkel-sitelaag.json` (B13 Wood Mackenzie, B29 SMM).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
`bash v2/tools/bak_stromen.sh nikkel-riotuba-niihama` -> `v2/data/stroomroute-nikkel-riotuba-niihama.json` (11,9 KB, versie 2, punt_formaat lonlat): **4 benen · 3.843,5 km · 570 punten · 3 markers · naden 0 km**.

| # | modaliteit | km (gebakken) | punten | brief | stippel |
|---|---|---|---|---|---|
| b1 | truck | 9,2 | 129 | geen wegkm, hemelsbreed 6,5 (indicatie ~9) | nee |
| b2 | zee (haven-aanloop RTN-pier -> zeeknoop 5444) | 286,7 | 29 | 286,0 hemelsbreed | ja |
| b3 | zee (MARNET 5444 -> 5746) | 3.521,9 | 369 | 3.521,9 (toets) | nee |
| b4 | zee (haven-aanloop Niihama, letterlijke kopie taganito b4) | 25,7 | 43 | 25,7 | ja |

**Recept (volgorde van de functie `bak_nikkel_riotuba_niihama`):** `--been-geojson truck` (weg-plant-pier) -> `--stippel-geojson` (aanloop-riotuba) -> `--been zee 8.4000,120.0500 -> 34.0720,133.0479` -> `--stippel-geojson` (kopie `nikkel-taganito-niihama-aanloop-niihama.geojson`); markers: plant, pier, refinery. Profiel `nikkel-riotuba-niihama-plant-pier` (extract filipijnen, `wegscan_puur.py`, `corridorKlassen` tertiary/unclassified/service, `eindToegangPrivaat`).

**Toets (handleiding §5):** naden 0,00 km tussen alle benen · markers 0,0 km van de lijn · b3 3.521,9 km = brief (0%) · b1 9,2 km tegen indicatie ~9 (geen wegkm, dus de ±15%-toets is een indicatie: +2%) · `toets_knikken`: b1 1 omkering (176,7° op 8.55845,117.42150 = ankerstub 80 m naast de eerste wegvertex, geen terugloop), zee 0 omkeringen, 0 terugloop · `toets_rechte_benen`: alleen de twee stippels (b2 1,002; b4) zijn recht, beide met reden · json.load, modaliteiten {truck, zee}, elk been ≥ 2 punten.

**Toelichting stippel/aanloop:**
- **b2 (stippel, 286,7 km):** MARNET heeft in de zuidwestelijke Sulu Sea geen knopen binnen bereik van de pier (dichtstbijzijnde zeeknoop 5444 op 8.4000,120.0500 ligt 286 km oostwaarts; 5431 op 7.1436,117.3625 ligt 151 km zuidelijk en geeft 3.849 km + een bocht). `maak_havenaanloop.py` hing (timeout 300, exit 124, geen tweede poging); daarom handgemaakt geojson met 29 punten en één knik op 8.4700,117.5250 over open water (de rechte lijn schampte 0,2 km NE-land bij 117.49/8.50). De echte vaarroute (rond de zuidpunt van Palawan of via Balabac) is onbekend.
- **b4 (stippel, 25,7 km):** letterlijke kopie van de aanloop van `nikkel-taganito-niihama` (zelfde zeeknoop 5746 en dezelfde Seto-binnenzee-aanloop); niets herberekend.
- Geen vlucht, geen leiding, geen via-punten (b1 is een enkele corridor van 9 km).

**Lessen:**
- Het wegtool met een pure-Python PBF-lezer (`wegscan_puur.py`) haalt de Filipijnse extract in ~2,5 min; privaat/plantweg in de eindzone vroeg `eindToegangPrivaat` + `service` in `corridorKlassen`.
- Bij een zeeknoop die een haven niet kan bereiken (kade > 150 km van de dichtstbijzijnde zeeknoop) is een handgemaakte stippel met één knik sneller en eerlijker dan een tweede router-poging; controleer wel op landschampen (NE 1:10M) en kies de knoop die de MARNET-lijn rechtstreeks aansluit (5444, niet 5431).
- Het stroom-id noemt het werkelijke eindpunt (Niihama); geen afwijking.
- Open voor de orkestrator: sitelaag-punt `w-coralbay-riotuba` (8.5700,117.4190) staat ~1,4 km van de plant (8.5585,117.4225) en moet centraal worden gelijkgetrokken.
