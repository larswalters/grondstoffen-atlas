# Routebrief (licht) · olie — Puerto Jose → Jamnagar (India)

**stroom-id:** `olie-jose-jamnagar` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Titel:** Olie · Puerto Jose (Venezuela) → Sikka → Jamnagar (India)
**Keten in één zin:** Venezolaanse Orinoco-crude (Merey, Zuata) laadt bij de PDVSA-terminal Jose (SPM, Bahia de Barcelona) op een
VLCC, vaart **om de Kaap de Goede Hoop** naar de Reliance-marineterminal Sikka (Golf van Kutch) en gaat via de eigen pijpleiding
(stippel) naar het Jamnagar-complex van Reliance. Stoppunt bij de raffinaderij.
**Welke as van het verhaal:** Venezuela's olie onder Amerikaanse controle (sancties versoepeld) en India als tweede afnemer. Venezuela
exporteerde in mei 2026 1,25 Mb/d = 1.250 kb/d, waarvan VS 558, **India 427**, Europa 169 kb/d [4]; Jose is >80% van de export [10].
Het aandeel van Jamnagar in die 427 kb/d is niet gepubliceerd; Reliance is een van de drie grootste kopers en kocht in mei direct van
PDVSA, Chevron, Vitol en Trafigura [4]. Peiljaar 2026.

## 1 · Ketenkaart
```
Jose SPM `ol-jose-spm` (PDVSA, Bahia de Barcelona, 10.1389,-64.8277)
  ──(b1 zee · haven-aanloop SPM → zeeknoop 7967 · ~20 km hemelsbreed, schematisch, stippel)──► zeeknoop 7967 (10.2710,-64.7023)
  ──(b2 zee · Atlantische Oceaan → Kaap · ~10.303 km MARNET)──► Kaap-via knoop 70 (-35.0000,18.0000)
  ──(b3 zee · Kaap → Arabische Zee · ~8.902 km MARNET)──► zeeknoop 5321 (22.5734,69.4446)
  ──(b4 zee · haven-aanloop Sikka · 43,5 km, letterlijke kopie olie-primorsk-jamnagar, stippel)──► Sikka-terminal `ol-sikka-terminal`
  ──(b5 leiding · eigen crude-pijp · ~17 km, letterlijke kopie olie-primorsk-jamnagar, stippel)──► Jamnagar `ol-jamnagar-raffinaderij` ── stoppunt
```
Zee totaal ~19.268 km (b1 20,1 + b2 + b3 19.204 + b4 43,5) tegen de ontwerp-schatting ~19.200 km via de Kaap; via Suez zou MARNET
16.013 km meten (Port Said), maar zie §7.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `ol-jose-spm` → zeeknoop 7967 | haven-aanloop Jose | 20,1 hemelsbreed (snap-afstand SPM-zeeknoop; geen gepubliceerde km) | rechte `--stippel` (maak_havenaanloop gaf in de toets geen resultaat na 280 s; geen land gekruist, getoetst tegen NE-land) | ja, MARNET reikt niet tot de SPM |
| b2 | B | zee | zeeknoop 7967 → Kaap-knoop 70 | Caraiben → Atlantische Oceaan → Kaap | ~10.303 [ontwerp ~19.200 totaal; MARNET meet] | MARNET `--been` | nee |
| b3 | B | zee | Kaap-knoop 70 → zeeknoop 5321 | Kaap → Indische Oceaan → Arabische Zee | ~8.902 | MARNET `--been` | nee |
| b4 | B | zee | zeeknoop 5321 → `ol-sikka-terminal` | haven-aanloop Sikka | 43,5 (kopie, rechte lijn 40,7) | `--stippel-geojson` letterlijk `v2/build-cache/ais/graaf/olie-primorsk-jamnagar-aanloop-sikka.geojson` | ja, MARNET reikt niet (40,7 km) |
| b5 | C | leiding | `ol-sikka-terminal` → `ol-jamnagar-raffinaderij` | eigen crude-pijp SPM-terminal-raffinaderij | ~17 (hemelsbreed 16,66; geen gepubliceerde km) | `--stippel` letterlijk de regel van `bak_olie_primorsk_jamnagar` | ja, niet in OSM [13] |

Beennaam b2/b3: "zeeschip Jose → Kaap de Goede Hoop → Sikka (VLCC, aannemelijk: één bron voor de bestemming)". b4/b5: noem "gedeeld been met
olie-primorsk-jamnagar". Stippel = alleen "net reikt niet" (b1, b4, b5); b2/b3 zijn gemeten en doorgetrokken.

## 3 · Ankers
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-jose-spm` | laadplek (SPM-boei) | Jose SPM / Bitor-SPM, einde PDVSA-onderzeeleiding | 10.1389, -64.8277 | [1][2][3] | aannemelijk (z15 gezien: rode tanker langszij een boei, onderzeeleiding komt uit het zuidwesten; OSM-pijp eindigt op 10.13886,-64.82768 = 5 m ernaast; Wikipedia SPM 10.15,-64.83; welk laadpunt de India-ladingen nemen is niet gebrond) |
| `ol-sikka-terminal` | overslag zee → leiding | Reliance/SPTL Marine Terminal Sikka | 22.4990, 69.8330 | [5][7][13] | bron-gelegd (letterlijk hergebruikt uit olie-primorsk-jamnagar: steiger met tankers) |
| `ol-jamnagar-raffinaderij` | losplek / raffinaderij | Jamnagar-raffinaderijcomplex (Reliance) | 22.3500, 69.8500 | [12][13][14] | bron-gelegd (hergebruikt uit olie-primorsk-jamnagar: tankenparken en procesinstallaties over meerdere km2) |

Niet gebruikt: Wikipedia-punt Jose 10.1000,-64.8667 (z14: open water, 1,5 km van elke steiger) en het tankpark/de drie steigers aan de zuidkust
van de baai (10.08-10.10, -64.88 tot -64.85, z14 gezien: drie lange steigers, tankparken en raffinaderij landinwaarts). De keten start bij de SPM.

## 4 · Via-punten
Geen landbenen. Zee-via: **Kaap-knoop 70 (-35.0,18.0)**, de enige corridorkeuze (Kaap i.p.v. Suez), vastgelegd als twee `--been`-regels [11].

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Jamnagar-complex | Reliance Industries | ruwe olie (o.a. Merey) → producten | 1.240 kb/d (sitelaag w-jamnagar; Argus 2020 noemt 1,36 Mb/d) | [12][14][8] |

## 6 · Stoppunt
Bij de raffinaderij: fase D (productexport) is een andere keten; geen bron koppelt Jose-crude aan een afzonderlijke productlading.

## 7 · Open punten
- **Route Kaap of Suez is niet per lading gebrond.** De Kaap is een aanname: VLCC's tot 2 Mb (Vitol/Trafigura, charter Reliance-eenheid) [6][5] en Suez
  laat maximaal 20,1 m diepgang toe [11], dus beladen supertankers nemen vaak de Kaap. Een lichtere lading of Suezmax kan via Suez (MARNET 16.013 km).
- **Bestemming Jamnagar aannemelijk (één bron per lading):** Reliance-eenheid RIL USA laadde in april 2026 de Helios (2 Mb Merey) bij Jose voor Sikka [5];
  Reliance exploiteert alleen Jamnagar. Geen cargo-bron noemt Jamnagar-raffinaderij zelf in 2026. Argus (kennelijk 2020) noemt Jose-VLCC's naar Sikka en Jamnagar [7].
- **Welke SPM/steiger bij Jose** de India-ladingen laadt: niet gebrond; de keten start bij de SPM-boei (aannemelijk).
- **Geen OSM-pijp Orinoco → Jose**; de lading komt via binnenlandse pijpen en treinen het tankpark in, niet getekend. De OSM-pijp tankpark → SPM (way 977785285, 17 punten) is wel
  gekarteerd maar valt buiten het ontwerp (keten begint op de SPM).
- **Jaarvolume Jamnagar-aandeel niet gepubliceerd;** de 427 kb/d (mei 2026) is Venezuela → heel India. Stromen draaien snel onder Amerikaanse licenties.
- Reliance kocht in 2019 25% van de Venezolaanse export en stopte in 2020 door sancties [8]: de stroom is politiek volatiel.
- Haven-aanloop Jose: `maak_havenaanloop.py` gaf in de toets na 280 s geen resultaat: rechte stippel (geen tweede poging).

## 8 · Bronnen
[1] Wikipedia, "Puerto Jose" (SPM 10 09'N 64 50'W, schepen tot 300.000 tdwt, offshore SPM met onderzeese pijpen). https://en.wikipedia.org/wiki/Puerto_Jos%C3%A9
[2] OpenStreetMap, way 977785285 (man_made=pipeline, operator PDVSA, 17 punten, eindigt 10.13886,-64.82768). https://www.openstreetmap.org/way/977785285
[3] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-olie-jose-jamnagar-spm.png` (z15), `sat-olie-jose-jamnagar-terminal.png` (z14), `sat-olie-jose-jamnagar-jose.png`, `sat-olie-jose-jamnagar-jose-jetty.png` (haalbaarheidstoets).
[4] Reuters via MarineLink, juni 2026, "Venezuela's oil exports rose to 1.25 million bpd in May" (VS 558, India 427, Europa 169 kb/d; Reliance direct van PDVSA, Chevron, Vitol, Trafigura). https://www.marinelink.com/news/venezuelas-oil-exports-rose-may-539814
[5] Hydrocarbon Processing, 06-04-2026, "India's Reliance buys Venezuelan oil directly from PDVSA" (supertanker Helios, 2 Mb Merey, Jose naar Sikka, RIL USA). https://www.hydrocarbonprocessing.com/news/2026/04/indias-reliance-buys-venezuelan-oil-directly-from-pdvsa/
[6] Baird Maritime, 2026, "Venezuelan oil exports scale up with first VLCC bookings under US pact" (Nissos Kea, Nissos Kythnos, Arzanah, Vitol/Trafigura, Jose naar India, VLCC tot 2 Mb, Jose tot 70%). https://www.bairdmaritime.com/shipping/tankers/feature-venezuelan-oil-exports-scale-up-with-first-vlcc-bookings-under-us-pact
[7] Argus Media (kennelijk 2020), "Venezuela oil exports accelerate, India awaits cargoes" (Lucky Trader naar Jamnagar, Boston naar Sikka, Jose-lading). https://www.argusmedia.com/en/news-and-insights/latest-market-news/2052218-venezuela-oil-exports-accelerate-india-awaits-cargoes
[8] Bloomberg via AJOT, 25-06-2020 (Reliance 25% van de Venezolaanse export 2019, geen nieuwe aankopen). https://www.ajot.com/news/venezuela-oil-crisis-deepens-with-india-refiners-halting-imports
[9] Swarajya (Bloomberg/Kpler), 2026 (Indiase raffinaderijen ~343 kb/d voor maartlading). https://swarajyamag.com/amp/story/news-brief/indian-refiners-emerge-as-leading-buyers-of-venezuelan-crude-as-china-cuts-imports-amid-us-oil-sanctions
[10] Bloomberg Government, maart 2026 (Jose >80% van de olie-export, 848 kb/d maart-laadprogramma). https://news.bgov.com/environment-and-energy/venezuelas-key-oil-hub-nears-7-year-export-high-under-us-watch
[11] Wikipedia, "Suezmax" (max. diepgang 20,1 m; supertankers beladen om Kaap Agulhas). https://en.wikipedia.org/wiki/Suezmax
[12] Wikipedia, "Jamnagar refinery" (Reliance, 1.240.000 vaten/dag). https://en.wikipedia.org/wiki/Jamnagar_refinery
[13] Routebrief `v2/design/routebrieven/olie-primorsk-jamnagar.md` (ankers Sikka en Jamnagar, aanloop-geojson, stippel Sikka-Jamnagar, geen OSM-pijp).
[14] Sitelaag `v2/design/olie-sitelaag.json`, site `w-jamnagar` (1.240 kb/d, bron-gelegd).
[15] MARNET-meting (`hecht_marnet.py route`, 2026-10-29): 7967 naar knoop 70 = 10.302,8 km, knoop 70 naar 5321 = 8.901,5 km; zeeknoop-snaps SPM 20,1 km, Sikka 40,7 km.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)

`bash v2/tools/bak_stromen.sh olie-jose-jamnagar` → `v2/data/stroomroute-olie-jose-jamnagar.json` (38,0 KB, contract versie 2, lonlat,
5 benen, 2.040 punten, 3 markers). Functie `bak_olie_jose_jamnagar` in `v2/tools/bak_stromen.sh`; geen wegprofiel, geen extract, geen nieuw geojson.

| # | modaliteit | km | naad | stippel | been |
|---|---|---|---|---|---|
| 1 | zee | 20,1 | 0 | ja | haven-aanloop Jose SPM → zeeknoop 7967 (rechte lijn) |
| 2 | zee | 10.302,8 | 0,00 | nee | zeeschip Jose-zeeknoop → Kaap de Goede Hoop (VLCC, aannemelijk) |
| 3 | zee | 8.901,5 | 0,00 | nee | zeeschip Kaap → Sikka-zeeknoop (VLCC, aannemelijk) |
| 4 | zee | 43,5 | 0,00 | ja | haven-aanloop Sikka (letterlijke kopie olie-primorsk-jamnagar) |
| 5 | leiding | 16,7 | 0,00 | ja | eigen crude-pijp Sikka → Jamnagar (letterlijke kopie olie-primorsk-jamnagar) |

Totaal 19.284,6 km (brief ~19.268 km zee + 16,7 leiding). Markers (3): Jose SPM, Sikka-terminal, Jamnagar; alle op hun lijn (0 m, uiteinden van de benen).

**Recept.** b1 `--stippel` rechte lijn (geen `maak_havenaanloop`: de briefronde gaf na 280 s niets; extra getoetst: de lijn snijdt noch `ne_10m_land` noch
`ne_10m_minor_islands`). b2/b3 `--been zee` kade → kade via Kaap-knoop 70 (-35,18); MARNET gaf exact de brief-getallen (10.302,8 en 8.901,5), snaps 0,000 km.
b4 `--stippel-geojson` en b5 `--stippel` zijn letterlijke kopieën van `bak_olie_primorsk_jamnagar` (zelfde geojson `olie-primorsk-jamnagar-aanloop-sikka.geojson`).

**Toelichting stippel.** b1: MARNET reikt niet tot de SPM (zeeknoop 20,1 km). b4: Sikka-terminal 40,7 km van zeeknoop 5321, aanloop over water 43,5 km.
b5: geen OSM-pijp Sikka → Jamnagar. b2/b3 zijn gemeten en doorgetrokken; "aannemelijk: één bron voor de bestemming" en de Kaap-aanname staan in de beennaam en in §7.

**Toets.** Geen ±15%-toets (geen gepubliceerde zeekm; MARNET = brief). Naden 0,00 km. `toets_knikken`: 2 knikken, 0 omkeringen, 0 terugloop (93,3° bij 11,316,-64,813 ten noorden
van de Venezolaanse kust en 112,4° bij 22,543,68,720 in de aanloop van de Golf van Kutch; beide MARNET-bochten, R 5,6–6,4 km, geen reparatie). `toets_rechte_benen`: alleen de twee
stippels (b1, b5), zoals bedoeld.

**Lessen.** (1) Een kale route met twee gedeelde kopieën + twee zee-`--been`-regels bakt in 20 s; geen slot-wachttijd nodig buiten het zwaar-slot. (2) `bash` gaf aan het eind een
syntaxfout van een tegelijk bewerkte andere functie in `bak_stromen.sh` (ná het bakken, `bash -n` daarna schoon): lees-voor-edit blijft nodig. (3) Het id beloofde Jamnagar en het eindpunt is Jamnagar: geen afwijking.
