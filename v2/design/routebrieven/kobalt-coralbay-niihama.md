# Routebrief (licht) · kobalt — Coral Bay HPAL (Rio Tuba, Palawan) → Niihama (Japan)

**stroom-id:** `kobalt-coralbay-niihama` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** het kobalt zit in het nikkel-kobalt mixed sulfide (MS) van de Coral Bay HPAL-plant (CBNC, SMM) naast de Rio Tuba-mijn (Bataraza, zuidpunt Palawan); het MS gaat per lokale weg naar de pier, per zeeschip door de Sulu Sea, Mindoro-straat, Luzon-straat en langs Okinawa naar de Seto-binnenzee en lost bij de Niihama Nickel Refinery (SMM, Ehime), Japans raffinaderij voor nikkel en kobalt.
**Welke as van het verhaal:** *tweede Sumitomo-HPAL, via de zuidwestelijke corridor* — naast Taganito (Mindanao). Volume: **2,5 kt Co/jaar nameplate** (Argus 2025-01, capaciteit, geen productiejaar) [1]; geen actueel productiecijfer gevonden. Aannemelijk: één bron voor de bestemming Niihama; geen bron voor pier en route.
**⚠️ Dubbel met de nikkelstroom:** alle vier de benen zijn een **letterlijke kopie** van `nikkel-riotuba-niihama` b1–b4 (zelfde lading in het MS, andere grondstoflaag; precedent `kobalt-taganito-niihama`). Valt die nikkelstroom centraal af, dan valt deze mee.

## 1 · Ketenkaart
```
Coral Bay HPAL-plant `co-coralbay-plant` ──(b1 truck · lokale weg via Rio Tuba-dorp · 9,2 km gemeten, kopie)──► RTN-pier `co-riotuba-pier`
   ──(b2 zee · haven-aanloop, stippel · 286,7 km, kopie)──► MARNET-zeeknoop 5444 (8.4000,120.0500)
   ──(b3 zee · MARNET · 3.521,9 km, kopie)──► MARNET-zeeknoop 5746 (34.0720,133.0479)
   ──(b4 zee · haven-aanloop, stippel · 25,7 km, kopie)──► Niihama Nickel Refinery `co-niihama-refinery` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `co-coralbay-plant` → `co-riotuba-pier` | plantweg → Rio Tuba-dorp → depotweg naar de pier; één corridor — **letterlijke kopie** nikkel b1 | hemelsbreed 6,5 km, geen wegkm; gebakken 9,2 [5] | kopie `nikkel-riotuba-niihama-weg-plant-pier.geojson`, geen nieuw profiel | nee |
| b2 | B | zee (haven-aanloop) | `co-riotuba-pier` → zeeknoop 5444 | over water, Sulu Sea — **letterlijke kopie** nikkel b2 | 286,0 hemelsbreed; 286,7 gebakken | kopie `nikkel-riotuba-niihama-aanloop-riotuba.geojson` | **ja** — MARNET reikt niet tot de pier (knopen 150+ km uit elkaar) |
| b3 | B | zee | zeeknoop 5444 → 5746 | Sulu Sea, Mindoro-straat, Luzon-straat, Okinawa, Seto-binnenzee; **aannemelijk: één bron voor de bestemming** — **letterlijke kopie** nikkel b3 | 3.521,9 (MARNET, gemeten) | MARNET (`--been`, zelfde coördinaten als nikkel b3) | nee |
| b4 | B | zee (haven-aanloop) | zeeknoop 5746 → `co-niihama-refinery` | **letterlijke kopie** nikkel b4 (= taganito b4) | 23,2 hemelsbreed; 25,7 gebakken | kopie `nikkel-taganito-niihama-aanloop-niihama.geojson` | **ja** — kade > 5 km van de zeeknoop |

Geen mijnbeen: de plant ligt tegen de Rio Tuba-mijn aan (RTNMC levert limoniet aan het aangrenzende CBNC) [3][4]. De 3.800 km uit het ontwerp was indicatief; gemeten is 3.521,9 + twee aanlopen = 3.843,5 km totaal.

## 3 · Ankers (één per site en per overslag) — hergebruik uit `nikkel-riotuba-niihama.md` §3
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-coralbay-plant` | verwerking (HPAL, MS met het kobalt) | Coral Bay Nickel Corporation, Rio Tuba, Bataraza | 8.5585, 117.4225 | [2][3][4] | bron-gelegd (hergebruik `ni-coralbay-plant`; z15 hier opnieuw gezien: compact procesterrein met tanks en gebouwen, mijnterrassen en rode tailings direct noordoost, de landingsbaan van Rio Tuba 1,5 km zuidoost) |
| `co-riotuba-pier` | overslag (pier, MS-uitvoer) | RTN-pier Rio Tuba | 8.5030, 117.4515 | [5] | aannemelijk (hergebruik `ni-riotuba-pier`; z15 hier gezien: kruis op de kop van een pier die vanaf de kust het water in loopt, schepen aan de kop, tanks en depot aan de wal; geen bron geeft een coördinaat of noemt deze pier voor het MS) |
| `co-niihama-refinery` | losplek + raffinaderij (Ni + Co) | Niihama Nickel Refinery, SMM | 33.9669, 133.2658 | [5][6] | bron-gelegd (hergebruik `ni-`/`co-niihama-refinery`; z15 hier gezien: kadegebonden industrieblok tussen twee havenbekkens aan de westrand van Niihama) |

Sitelaag-punt `w-coralbay-riotuba` (8.5700, 117.4190; `nikkel-sitelaag.json`) ligt ~1,4 km noord, op het mijn-/tailinggebied, niet op de plant; centraal gelijk te trekken met `co-coralbay-plant`. De kobalt-sitelaag heeft **geen** Coral Bay-site en het verkeerde Niihama-anker (zie §7).

## 4 · Via-punten
Geen. b1 is een kopie van een weg van 9,2 km zonder corridorkeuze; b2/b4 zijn haven-aanlopen, b3 is MARNET (zee = router, geen via-punten). Er is geen eigen wegprofiel.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Coral Bay HPAL (CBNC) | SMM, 100% sinds begin 2025 (Nickel Asia verkocht 15,625%) | limoniet (RTNMC) → Ni-Co mixed sulfide | 24 kt Ni + **2,5 kt Co/jaar** nameplate | [1][3][4] |
| Niihama Nickel Refinery | SMM | MS (Coral Bay, Taganito) → elektrolytisch Ni en Co (MCLE) | Co-tonnage niet gepubliceerd | [5][6] |

## 6 · Stoppunt
Niihama (elektrolytisch kobalt): geen bron noemt een vervolgafnemer van dit specifieke kobalt; fase D en E vervallen (zelfde argument als `kobalt-taganito-niihama`).

## 7 · Open punten
- **Pier niet gedocumenteerd:** RTN-pier is aannemelijk; geen bron noemt een coördinaat of dat het MS daar laadt. Echte vaarroute rond Palawan/Balabac onbekend: b2 is een handgemaakte stippel met één knik.
- **Bestemming:** FoE Japan zegt "SMM's factories in Japan", niet Niihama [3]; Niihama volgt uit het SMM-persbericht 2005 en de OneMine-paper (MS voor MCLE in Niihama) [5][6]. SMM noemt ook Harima (nikkelsulfaat) als MS-afnemer; waar de Co-fractie heen gaat is niet gepubliceerd.
- **Volume:** 2,5 kt Co is nameplate (2025); Wood Mackenzie noemt 750 t Co nameplate in 2007, een nieuws-item (ongedateerd) ~2.000 t Co/jaar. Geen productiejaar 2023–2025.
- **Toekomst:** SMM verwacht stopzetting van CBNC binnen enkele jaren [7]; juni 2026 draait de plant nog [3]. De stroom kan ophouden te bestaan.
- **b1-km:** geen gepubliceerde wegkilometer (hemelsbreed 6,5, gebakken 9,2); de ±15%-toets is een indicatie, geen norm.
- **Kobalt-sitelaag** mist Coral Bay (2,5 kt Co) en `w-niihama` staat op 33.9496, 133.2316 (~3 km west); centraal toevoegen/rechttrekken. Niet door mij gewijzigd.
- **Afhankelijkheid:** de benen bestaan alleen zolang `nikkel-riotuba-niihama` (gebakken, nog niet in het register) blijft staan.

## 8 · Bronnen
[1] Argus, 2025-01-07: SMM wordt volledig eigenaar van CBNC; capaciteit 24.000 t Ni en 2.500 t Co per jaar (2026-10-09 opgehaald). https://argusmedia.com/es/news-and-insights/latest-market-news/2644488-smm-to-wholly-own-philippine-coral-bay-nickel-smelter
[2] Coral Bay Nickel Corporation, bedrijfspagina: Rio Tuba, Bataraza; lijn 1 commercieel 2005, lijn 2 2009 (2026-10-09 opgehaald). https://cbnc.com.ph/the-company
[3] FoE Japan, 2026-06-08: CBNC 100% SMM, HPAL in zuid-Palawan sinds 2005, alle MS naar SMM-fabrieken in Japan, plant operating (2026-10-09 opgehaald). https://foejapan.org/en/issue/20260608/29927/
[4] Nickel Asia, Rio Tuba Nickel Mining Corp: Barangay Rio Tuba, zuidpunt Palawan; levert limoniet aan het aangrenzende CBNC (2026-10-09 opgehaald). https://nickelasia.com/subsidiaries/rio-tuba-nickel-mining-corporation
[5] Eigen repo: `routebrieven/nikkel-riotuba-niihama.md` en `v2/data/stroomroute-nikkel-riotuba-niihama.json` (ankers, benen, SMM-persbericht 2005 via die brief: MS naar Niihama, RTN-havenfaciliteiten; smm.co.jp onbereikbaar, niet zelf herlezen) · Esri World Imagery z15, `v2/build-cache/satcheck/sat-kobalt-coralbay-niihama-co-{coralbay-plant,riotuba-pier,niihama-refinery}.png`.
[6] OneMine, Development of Process Design for Coral Bay Nickel Project (2004): HPAL, sulfidefase, MS naar Niihama voor MCLE-elektrowinning; Wood Mackenzie Niihama-assetnotitie: kobaltproductie sinds 1975 uit gemengde Ni-Co-sulfiden. https://onemine.org/documents/development-of-process-design-for-coral-bay-nickel-project · https://woodmac.com/reports/metals-niihama-nickel-refinery-17241284
[7] FoE Japan, 2025-12-05: SMM verwacht stopzetting van CBNC binnen enkele jaren. https://foejapan.org/en/issue/20251205/27117/
[8] Wikipedia, Rio Tuba mine (8.570 N, 117.419 E; 46,8 kt Ni in 2022 uit de mijn). https://en.wikipedia.org/wiki/Rio_Tuba_mine

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-kobalt-coralbay-niihama.json` (12,3 KB, versie 2, lonlat) · **functie:** `bak_kobalt_coralbay_niihama` in `v2/tools/bak_stromen.sh` · **recept:** alleen `hecht_marnet.py route`, geen scan, geen nieuw wegprofiel, geen herbake van aanlopen; vier benen letterlijk uit `$BEEN` van `nikkel-riotuba-niihama` (b3 = dezelfde MARNET-coordinaten) en `nikkel-taganito-niihama` (b4-aanloop).

| # | modaliteit | km gebakken | km brief | stippel | punten | naad naar volgende |
|---|---|---|---|---|---|---|
| b1 | truck | 9,2 | hemelsbreed 6,5, geen wegkm (indicatie) | nee | 129 | 0,00 km |
| b2 | zee (haven-aanloop pier → knoop 5444) | 286,7 | 286,0 hemelsbreed | ja | 29 | 0,00 km |
| b3 | zee (MARNET 5444 → 5746) | 3.521,9 | 3.521,9 | nee | 369 | 0,00 km |
| b4 | zee (haven-aanloop knoop 5746 → Niihama) | 25,7 | 23,2 hemelsbreed | ja | 43 | - |

Totaal **3.843,5 km**, 570 punten, 3 markers (plant, pier, raffinaderij), allemaal op 0,0 km van de lijn. Naden alle 0,00 km. Geen last-mile-been, geen via-punten.

**Toelichting stippels:** b2 en b4 zijn haven-aanlopen (stippel = MARNET reikt niet): de RTN-pier ligt 286,7 km van zeeknoop 5444 (handgemaakt, een knik over open water, echte vaarroute rond Palawan onbekend); de Niihama-kade ligt 23,2 km van zeeknoop 5746 (snap binnen 25 km maar kade > 5 km van de knoop). Beide zijn kopieen, niet opnieuw gerouteerd.
**Toets:** `json.load` goed, modaliteiten {truck, zee}, elk been >= 2 punten. `toets_knikken.py`: 8 knikken >= 60 gr, 1 omkering (b1, 176,7 gr bij 8.55845,117.42150, "scherpe bocht, echt", plantterrein) en 4 spikes in b1 (kopie, in de nikkelstroom hetzelfde); 0 terugloop; zee 3 krappe bochten (Seto-binnenzee, Ryukyu) zoals in de nikkelstroom. `toets_rechte_benen.py --min-km 5`: alleen b2 (omwegfactor 1,002), en die is stippel met reden.
**Lessen:** een volledig gedeelde keten (precedent kobalt-taganito-niihama) bakt in een minuut zonder scan of aanloop-run. Bij het bakken gaf bash een eenmalige "ga: command not found" op een regel ver onder mijn functie: een andere agent bewerkte gelijktijdig `bak_stromen.sh` (bash leest het script lazy); de bake zelf was klaar en `bash -n` is schoon.
**Open (zie ook §7):** pier niet gedocumenteerd; productiecijfer 2023-2025 ontbreekt (2,5 kt Co nameplate); kobalt-sitelaag mist Coral Bay en heeft Niihama op 33.9496,133.2316; `w-coralbay-riotuba` ligt 1,4 km van de plant; de stroom hangt aan `nikkel-riotuba-niihama` (nog niet in het register).
