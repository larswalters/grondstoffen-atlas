# Routebrief (licht) · Uranium · Honeymoon → Port Adelaide → Oakland → Metropolis Works (Australië → VS)

**stroom-id:** `uranium-honeymoon-metropolis` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** Yellowcake (U3O8 in drums, 20ft-zeecontainers) uit de Honeymoon-ISR-mijn (Boss Energy, Zuid-Australië) gaat per **truck** over de Barrier Highway (A32) en de A20/M2 naar Outer Harbor (Port Adelaide), per **zeeschip** over de Stille Oceaan naar Oakland (Californië, aannemelijk: gedocumenteerde route uit 2012/2013) en per **truck** (I-80, I-29, I-70, I-64, I-57, I-24) naar de Honeywell/ConverDyn-conversiefabriek Metropolis Works (Illinois) — stoppunt.
**Welke as van het verhaal:** *Australië naar de VS-conversie* — Boss kondigt de eerste zending naar Metropolis aan (Q3 2024). Volume: nameplate 2,45 Mlb U3O8/j = ca. 940 t U/j (WNN 4-7-2024, doel jaar 3), FY25-doel minstens 850.000 lb ≈ 330 t U/j; eerste zending 57.000 lb ≈ 22 t U [1][2][3]. Deel van de productie gaat naar een Europese utility (niet getekend).

## 1 · Ketenkaart
```
Honeymoon-fabriek `u-honeymoon-fabriek` ──(b1 A truck · Yarramba Rd/Mooleulooloo Rd → A32 Barrier Hwy (Olary, Yunta, Burra) → A20/M2 · OSRM 511 km, hemelsbreed 392 km, geen wegkm)──►
  Outer Harbor `u-portadelaide-outerharbor` ──(b2a zee haven-aanloop 17,6 km tot zeeknoop 6042, stippel)──► MARNET-zeeknoop 6042
  ──(b2b zee · Zuidelijke Oceaan → Stille Oceaan · 13.840,5 km MARNET)──► zeeknoop 4864 (Golden Gate/Treasure Island)
  ──(b2c zee haven-aanloop 7,4 km, stippel)──► Oakland `u-oakland-kade` (aannemelijk)
  ──(b3 C truck · I-80 → I-29 → I-435 → I-70 → I-64 → I-57 → I-24 → US-45 · OSRM 3.569 km, geen wegkm)──► Metropolis Works `u-metropolis-conversie` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Honeymoon-fabriek → Outer Harbor | Honeymoon-mijnweg (Yarramba Rd, Mooleulooloo Rd) → Barrier Highway A32 → A20/M2 Gawler → Port Adelaide; aannemelijk: modaliteit/haven niet door Boss bevestigd [8][10] | hemelsbreed 392 km, geen wegkm; OSRM 511 km (eigen run) = indicatie, geen norm | maak_stroombeen_weg (australie, reus: 1 scan tegelijk) | nee |
| b2a | B | zee (haven-aanloop) | Outer Harbor-kade → zeeknoop 6042 (-34.9107,138.4332) | over water om Lefevre-schiereiland, schematisch | 16,6 hemelsbreed [13]; aanloop 17,6 gemeten (eigen run, 0,00 km over land) | maak_havenaanloop.py; geojson staat klaar | ja — net reikt niet tot de kade |
| b2b | B | zee | zeeknoop 6042 → zeeknoop 4864 (37.8421,-122.3958) | Zuidelijke Oceaan, Stille Oceaan; haven Oakland uit NRC-meldingen (2012, 2013) [4][5]; aanvoerhaven voor Boss 2024 niet gepubliceerd | 13.840,5 [13: MARNET-dry-run, 1.409 punten] | MARNET | nee |
| b2c | B | zee (haven-aanloop) | zeeknoop 4864 → Oakland-kade | San Francisco Bay, ten noorden van Treasure Island, onder de Bay Bridge door | 6,7 hemelsbreed [13]; aanloop 7,4 (met de hand over water, 18 punten) | handmatig geojson (maak_havenaanloop hing, timeout 300); staat klaar, richting knoop → kade | ja — net reikt niet tot de kade |
| b3 | C | truck | Oakland-kade → Metropolis Works | Maritime St → I-880 → I-80 (Donner, Winnemucca, Salt Lake, Cheyenne, Lincoln) → NE-2/IA-2 → I-29 → I-435 → I-70 → I-64 → I-57 → I-24 → US-45; aannemelijk: inland-modus niet gepubliceerd [4][5][12] | hemelsbreed 2.947 km, geen wegkm; OSRM 3.569 km (eigen run) = indicatie | maak_stroombeen_weg (8 extracts, zie §4) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-honeymoon-fabriek` | mijn / fabriek (laadplek, kop) | Honeymoon ISR-fabriek (Boss Energy), 80 km NW Broken Hill | -31.7430, 140.6615 | Wikipedia-infoboxpunt -31.74095,140.66236 [6], op z16 verschoven naar de fabriek | bron-gelegd (z15+z16 gezien: verwerkingsfabriek met hallen, drie zwarte vijvers en tanks, krachtlijn en rode mijnweg, airstrip 1,5 km zuidoost) |
| `u-portadelaide-outerharbor` | overslag truck → zee (**hergebruikt**) | Outer Harbor containerterminal, Port of Adelaide | -34.7694, 138.4920 | letterlijk uit `uranium-olympicdam-portadelaide` §3 [9] | aannemelijk (z15 opnieuw gezien: containerstapels, kranen en kade; niet als uranium-berth bevestigd) |
| `u-oakland-kade` | overslag zee → truck | Port of Oakland, containerterminal Outer Harbor (Berths 20-26, noordkade) | 37.8095, -122.3320 | haven Oakland uit [4][5]; terminal onbekend, positie via OSM-terminalnamen [14] en satelliet | **aannemelijk** (z15 gezien: pier met containerstapels, kranen en een containerschip aan de noordkade, open water in de Bay; of Hapag-Lloyd hier lost is niet bekend) |
| `u-metropolis-conversie` | UF6-fabriek (stoppunt, **hergebruikt**) | Honeywell/ConverDyn Metropolis Works, Illinois | 37.1718, -88.7570 | letterlijk uit `uranium-smithranch-metropolis` §3 [1][2] | bron-gelegd (in die brief z16: ommuurd terrein met tanks en hallen aan de Ohio) |

## 4 · Via-punten (landbenen; (lat, lon) hier, in het profiel (lon, lat); alle op de doorgaande weg, OSRM-manoeuvre- of geometriepunten [12])
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Yarramba Road (mijnweg) | -31.7522, 140.5135 | pint de mijnweg west/zuidwest; tertiary/unpaved, corridorKlassen nodig |
| b1 | 2 | Mooleulooloo Road | -32.1304, 140.7368 | verbinding naar de A32 bij Olary; zonder dit punt kiest de router een andere korte weg |
| b1 | 3 | Olary, Barrier Highway | -32.2809, 140.3297 | aansluiting op de A32 |
| b1 | 4 | Yunta, Barrier Highway | -32.5860, 139.5548 | houdt de route op de A32, niet op een zijweg |
| b1 | 5 | A32 tussen Terowie en Burra | -33.4505, 138.8952 | **vervangt** het ontwerppunt in Terowie (zijstraat Second Street); op de weg, niet in het dorp |
| b1 | 6 | A32 ten zuiden van Burra | -33.8512, 138.8687 | **vervangt** het ontwerppunt in Burra (Copperhouse St, ca. 4 km omweg door het centrum) |
| b1 | 7 | Sturt Highway bij Gawler (by-pass) | -34.5956, 138.7293 | pint A20/M2 naar Port Adelaide, buiten het centrum |
| b3 | 1 | I-80 Donner Pass | 39.3400, -120.3455 | corridorkeuze Sierra Nevada: I-80, niet I-5 of US-50 |
| b3 | 2 | I-80 bij Winnemucca | 40.9798, -117.7301 | houdt I-80 door Nevada (alternatief US-50) |
| b3 | 3 | I-80 oostelijk van Salt Lake (Parleys Canyon) | 40.7486, -111.7003 | I-80 door Utah, niet I-84/I-15 |
| b3 | 4 | I-80 Cheyenne | 41.1164, -104.9007 | I-80 door Wyoming |
| b3 | 5 | I-80/US-77 Lincoln | 40.8140, -96.7552 | keuzepunt: hier verlaat OSRM I-80 voor NE-2/IA-2/I-29 naar Kansas City (alternatief: I-80 verder naar Des Moines) |
| b3 | 6 | I-29/I-435 Kansas City | 39.3421, -94.7416 | pint I-435 en I-70 oost |
| b3 | 7 | I-70/I-64 St. Louis | 38.7166, -90.2975 | wissel van I-70 naar I-64 |
| b3 | 8 | I-57 bij Whittington | 38.2760, -88.9363 | pint I-57 zuid naar I-24, niet I-64 verder naar Evansville |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Honeymoon | Boss Energy | uraniumhoudende oplossing (NIMCIX) → U3O8-drums | nameplate 2,45 Mlb/j ≈ 940 t U/j; FY25 ≥ 850.000 lb ≈ 330 t U | [1][2][3] |
| Metropolis Works | Honeywell / ConverDyn | U3O8 → UF6 | vergund ~15.000 t U/j (sitelaag) | [1][9] |

## 6 · Stoppunt
De brief stopt bij Metropolis Works (conversie), het opgegeven eindpunt en de gedocumenteerde afnemer ("first shipment of 57,000 lbs to the Honeywell facility in Metropolis" [1][2]); fase D vervalt: geen bron noemt de UF6-bestemming van deze lading.

## 7 · Open punten
- **Afwijking van het ontwerp:** het ontwerp nam Portsmouth VA als aanvoerhaven (aanname, analogie met UF6-uitvoer). De zoekronde vond voor Adelaide-UOC naar Honeywell Metropolis een gepubliceerde route via **Oakland**: NRC-melding 0212-637 (Uranium One Australia, de toenmalige Honeymoon-eigenaar, 120 drums in 2 containers, Hapag-Lloyd Adelaide → Oakland, daarna inland naar Metropolis) [4] en 0413-868 (BHP, 336 drums) [5]; meer meldingen 2010–2013 alleen als zoekresultaat gezien. Portsmouth heeft geen importbron. Daarom Oakland, en het truckbeen is 3.569 km in plaats van 1.393 km.
- **Actuele Boss-route onbevestigd:** de bronnen zijn van 2012/2013; Boss noemt alleen "shipment to Metropolis" [1][2]. Haven Adelaide is gepubliceerd [4][5] (Port Adelaide is een van de uranium-uitvoerhavens [7]), de Oakland-terminal niet.
- **Modaliteit Oakland → Metropolis niet gepubliceerd:** de NRC-meldingen zeggen alleen "inland transportation" (RSB Logistic Services, Paducah KY); ETA 10 dagen (2012: 6 → 16 maart). Spoor (BNSF/UP-intermodal, er ligt een BNSF-ramp in Oakland [14]) is evengoed mogelijk; getekend als truck, consistent met de andere Metropolis-ketens.
- **Km zijn OSRM, geen wegkm:** b1 511 km, b3 3.569 km; de ±15%-toets is indicatie. Zwaar bakwerk: b3 loopt over 8 extracts (us-california een reus), ± 55.000 punten (>1 MB).
- **Sitelaag-fout (niet gewijzigd, gemeld):** `w-honeymoon` in `uranium-sitelaag.json` staat op -30.15, 139.8333 ("indicatief, Frome-bekken") — ca. 175 km van de echte fabriek (-31.7430, 140.6615).
- **Zending naar Europese utility** [3] bewust niet getekend (haven/afnemer onbekend).
- Nameplate (2,45 Mlb) is een doel voor jaar 3 [3], geen gerealiseerd jaarvolume.

## 8 · Bronnen
[1] Boss Energy, Quarterly Activities Report september 2024 (ASX 2024-10-23): eerste zending 57.000 lb naar Honeywell Metropolis, goedkeuring voor bulkzendingen. https://announcements.asx.com.au/asxpdf/20241023/pdf/069fy1qtk1knqj.pdf
[2] Boss Energy, Quarterly Activities Report december 2024 (ASX 2025-01-29): 57 Klb aangekomen, 78 Klb onderweg, 120 Klb in containers op Honeymoon. https://announcements.asx.com.au/asxpdf/20250129/pdf/06dxg8kfs900xh.pdf
[3] World Nuclear News, "First Honeymoon shipment bound for Europe", 4-7-2024: drums, nameplate 2,45 Mlb/j. https://world-nuclear-news.org/articles/first-honeymoon-shipment-bound-for-europe
[4] NRC, RSB Logistic advance notification REF 0212-637 REVISED (Uranium One Australia → Honeywell; Adelaide 14-2-2012 → Oakland 6-3-2012 → Metropolis). https://www.nrc.gov/docs/ML1213/ML12136A169.pdf
[5] NRC, RSB Logistic advance notification REF 0413-868 (BHP Olympic Dam → Honeywell; Adelaide 11-3-2013 → Oakland 2-4-2013). https://www.nrc.gov/docs/ML1317/ML13179A297.pdf
[6] Wikipedia (en), "Honeymoon Uranium Mine" — 80 km NW van Broken Hill, coördinaat -31.74095, 140.66236. https://en.wikipedia.org/wiki/Honeymoon_Uranium_Mine
[7] SA Department for Energy and Mining, uranium — Port Adelaide als uitvoerhaven (alleen als zoekresultaat, 403). https://energymining.sa.gov.au/industry/minerals-and-mining/mineral-commodities/uranium
[8] NS Energy, Honeymoon-projectbeschrijving: eindproduct in drums en zeecontainers voor wegtransport en export (zoekresultaat). https://www.nsenergybusiness.com/?p=291814
[9] Routebrieven `uranium-olympicdam-portadelaide` (Outer Harbor-anker) en `uranium-smithranch-metropolis` (Metropolis-anker).
[10] Senate-rapport uranium c04-7: Olympic Dam-UOC per weg naar de Port Adelaide-kade (zoekresultaat). https://aph.gov.au/Parliamentary_Business/Committees/Senate/Former_Committees/uranium/report/c04-7
[11] Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-uranium-honeymoon-metropolis-fabriek16.png`, `-outerharbor15.png`, `-oakland-outerharbor15.png`, `-oakland15.png`, `-oakland-aanloop13.png` (2026-10-30).
[12] OSRM publieke demo-server (project-osrm.org): b1 511,5 km via de zeven via-punten; b3 Oakland → Metropolis 3.569 km, manoeuvrepunten als via-punten.
[13] `hecht_marnet.py route` dry-run 2026-10-30: kade Outer Harbor snap 16,603 km (knoop 6042), Oakland-kade snap 6,674 km (knoop 4864), MARNET 13.840,5 km; aanlopen met `maak_havenaanloop.py` resp. met de hand.
[14] OpenStreetMap via Overpass: Port of Oakland-terminalvlakken (Trapac, SSA, Hanjin, Berths 32-34) en BNSF Oakland International Gateway.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
**Bestand:** `v2/data/stroomroute-uranium-honeymoon-metropolis.json` (607,9 KB, versie 2, lonlat, 5 benen, 29.069 punten, 4 markers) · **totaal 18.013,5 km**, waarvan 25,0 km stippel (0,14%). Recept: `bak_uranium_honeymoon_metropolis()` in `v2/tools/bak_stromen.sh`; profielen `uranium-honeymoon-metropolis-fabriek-outerharbor` en `-oakland-metropolis` in `v2/tools/maak_stroombeen_weg.py`.

| # | modaliteit | km gemeten | km brief | afwijking | stijl |
|---|---|---|---|---|---|
| b1 | truck | 513,7 | 511 (OSRM-indicatie, geen wegkm) | +0,5% | doorgetrokken |
| b2a | zee (aanloop Outer Harbor) | 17,6 | 17,6 | 0 | stippel |
| b2b | zee (MARNET 6042 → 4864) | 13.840,5 | 13.840,5 | 0 | doorgetrokken |
| b2c | zee (aanloop Oakland) | 7,4 | 7,4 | 0 | stippel |
| b3 | truck | 3.634,3 | 3.569 (OSRM-indicatie, geen wegkm) | +1,8% | doorgetrokken |

**Naden:** alle vier 0,00 km (max 0,00 km, ruim onder 5 km). **Markers:** alle vier 0,0 km van de lijn.

**Toelichting per stippel/aanloop:**
- b2a haven-aanloop Outer Harbor: kade 16,6 km van zeeknoop 6042, gemeten met `maak_havenaanloop.py` (17,6 km, 0,00 km over land); stippel omdat MARNET niet tot de kade reikt (richting kade → knoop).
- b2c haven-aanloop Oakland: kade 6,7 km van knoop 4864; met de hand over water gelegd (18 punten, ten noorden van Treasure Island, onder de Bay Bridge door) omdat `maak_havenaanloop.py` hing; stippel omdat MARNET niet tot de kade reikt (richting knoop → kade). "Aannemelijk" staat in de beennamen en in §3/§7, niet in de lijnstijl.

**Afwijkingen / bevindingen:**
- b1 en b3: geen echte wegkm; de ±15%-toets is indicatie (beide ruim binnen).
- b3 vroeg `vensterKm` 100 in plaats van 40: bij 40 gaf de scan "geen wegpad tussen punt 3 en 4" omdat I-80 in Wyoming (Rock Springs/Rawlins) 80-90 km van de rechte lijn Parleys-Cheyenne ligt (en I-29 bij Nebraska City ~65 km van Lincoln-Kansas City). Via-punten onveranderd.
- Bestand 607,9 KB (truckbeen b3 599 KB, 24.090 punten) is boven de norm van ~300 KB; bekend zwaar (brief §7), niet verkleind.
- toets_knikken: 31 knikken, 3 omkeringen, 2 TERUGLOOP van ca. 0,1 km: bij I-57 Whittington (38,2704, -88,9270; via-punt 38,2760, -88,9363 ligt op een aftak) en bij de Oakland-kade (37,8260, -122,3001; oprit Bay Bridge/I-880). Niet gerepareerd. Het Lincoln-via-punt gaf een keerlus van 1,59 km die de tool al gesnoeid heeft.
- toets_rechte_benen: geen enkel been van deze stroom gemarkeerd.
- Sitelaag-fout (gemeld, niet gewijzigd): `w-honeymoon` in `uranium-sitelaag.json` staat ca. 175 km van de fabriek.
- Hergebruikte ankers: `u-portadelaide-outerharbor` (uit uranium-olympicdam-portadelaide), `u-metropolis-conversie` (uit uranium-smithranch-metropolis); geen gedeelde benen (geen kopie).

**Lessen:**
- Bij een westoost-corridor over de Rockies/Great Plains (Wyoming, Nebraska-Iowa) ligt de doorgaande weg tot ~90 km van de rechte lijn tussen twee via-punten: `vensterKm` 100 en een rescan (caches zijn per venster gehasht; us-california alleen is al 5-6 min).
- Een venster-fout toont zich als "geen wegpad" tussen twee via-punten, zonder snap-melding; de nulgeteld-index in de melding is 0-gebaseerd (punt 3 = het vierde via-punt).

