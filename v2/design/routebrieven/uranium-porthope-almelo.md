# Routebrief (licht) · uranium — Port Hope → Rotterdam → Almelo

**stroom-id:** `uranium-porthope-almelo` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** UF6/UO2-poeder uit de Port Hope Conversion Facility (Cameco, Ontario) gaat als **haven-aanloop** over Lake Ontario/de Seaway naar de dichtstbijzijnde MARNET-zeeknoop, per **zeeschip** over de Atlantische Oceaan naar Rotterdam RHB, en per **truck** over de A20/A12/A27/A28/A1/A35 naar de Urenco-verrijkingsfabriek in Almelo — stoppunt (aannemelijk: één bron, 2013).
**Welke as van het verhaal:** de eerste as die de daadwerkelijke wereldflessenhals van het v1-verhaal tekent — conversie (Noord-Amerika) → verrijking (~44% Rusland, de rest bij Urenco/Orano/CNNC). Port Hope is vergund tot 12,5 Mkg U als UF6/jaar (12.500 t U/j; Cameco jaarverslag 2015, al geciteerd in `uranium-mcarthurriver-porthope` §5); Urenco breidt Almelo tot 2030 uit met +1,5 miljoen SWU/j capaciteit (Wikipedia/Urenco, 2026) — geen bron geeft een actueel jaarvolume specifiek Port Hope→Almelo.

## 1 · Ketenkaart
```
Port Hope Conversion Facility `u-porthope-conversie` ──(b1 B zee/haven-aanloop · Lake Ontario/Seaway, MARNET reikt niet · ~66 km, stippel)──► MARNET-zeeknoop 4821 (Lake Ontario, 43.4992,-78.8371)
  ──(b2 B zee · Grote Meren/Seaway-zone (marnet_zee) → Atlantische oversteek · ~7.400 km, webcheck)──► Rotterdam RHB `u-rotterdam-kade`
  ──(b3 C truck · A20→A12→A27→A28→A1→A35, via Knp. Gouwe–Lunetten–Rijnsweerd–Hoevelaken–Buren · 189 km)──► Urenco Almelo verrijkingsfabriek `u-almelo-urenco` ── stoppunt
```
**Afwijking t.o.v. het ketenontwerp, volgens de haalbaarheidstoets:** het ontwerp knipte bij "monding St. Lawrence-zeeweg (Montreal/Quebec)". De dichtstbijzijnde bruikbare MARNET-zeeknoop (knoop 4821) ligt niet daar maar 65,9 km van Port Hope, **binnen/nabij Lake Ontario zelf** — ruim buiten de automatische 25 km-snap. Been b1/b2 is daarom herzien tot één doorlopende haven-aanloop + zee-been i.p.v. een knip bij Montreal.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee (haven-aanloop) | Port Hope Conversion Facility → MARNET-zeeknoop 4821 | Lake Ontario/Seaway — geen bruikbare zeeknoop binnen 25 km (65,9 km gemeten in de haalbaarheidstoets) | ~66 [haalbaarheidstoets, hecht_marnet-zeeknoop-check] | `maak_havenaanloop.py` (timeout 300) over de marnet-preais-graaf; lukt dat niet, dan `maak_rivierbeen.py` over dezelfde graaf | ja — net reikt niet binnen de automatische snap |
| b2 | B | zee | MARNET-zeeknoop 4821 → Rotterdam RHB | Grote Meren/Seaway-zone (`marnet_zee(m)`, dezelfde die het Duluth→Rotterdam-ijkpunt van 8.031 km draagt) → Atlantische oversteek | ~7.400 [webcheck: grootcirkel 5.956 km × 1,238 (de Duluth→Rotterdam-inflatiefactor, 8.031/6.485 km); te toetsen bij bakken] | MARNET (`--been "zee\|…\|43.4992,-78.8371\|51.8935,4.4585"`) | nee — Rotterdam-zijde al bevestigd (0,7 km van zeeknoop) |
| b3 | C | truck | Rotterdam RHB → Urenco Almelo | A20 → A12 (Knp. Gouwe) → A27 (Knp. Lunetten) → A28 (Knp. Rijnsweerd) → A1 (Knp. Hoevelaken, via Apeldoorn/Deventer) → A35 (Knp. Buren) → N349 → Bornsestraat/Drienemansweg | 189 [OSRM-webcheck, grondig gerouteerd; het ketenontwerp noemde ~150 km als ruwe schatting] | `maak_stroombeen_weg.py` (extract `nederland`) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-porthope-conversie` | conversie (kop, hergebruikt) | Port Hope Conversion Facility (Cameco), 1 Eldorado Place | 43.9437, -78.2955 | [1], hergebruikt uit `uranium-mcarthurriver-porthope` §3 | bron-gelegd (hergebruikt anker; satellietblik al gedaan in die brief — compact fabrieksterrein aan de Lake Ontario-kust met kleine havenaanleg) |
| `u-rotterdam-kade` | overslag zee → truck | Rotterdam — RHB Stevedoring & Warehousing, Waalhaven Noordzijde 4 | 51.8935, 4.4585 | vaste hergebruik-anker uit de kaart (`routebrief-licht.md` §1) | hergebruikt, niet opnieuw gelegd |
| `u-almelo-urenco` | verrijkingsfabriek (staart — stoppunt) | Urenco Nederland — verrijkingsfabriek, Drienemansweg (bedrijventerrein Bavinkel), Almelo | 52.3391, 6.6922 | [2][3] | bron-gelegd (z15 gezien: aaneengesloten industrieterrein met platte hallen en meerdere loodsen op Drienemansweg/Planthofsweg, Bavinkel-bedrijventerrein zuid van het centrum, langs een klein kanaal; OSM-punten "Urenco"/"Enrichment Technology") |

## 4 · Via-punten (alleen b3 — corridorkeuzes op knooppunten, uit `nl.wikipedia.org`-coördinaten)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | Knooppunt Gouwe (A20 × A12) | 52.0222, 4.6542 | hier verlaat de route de Rotterdamse ring en kiest ze de A12 oostwaarts i.p.v. de A13/A16-richting |
| b3 | 2 | Knooppunt Lunetten (A12 × A27) | 52.0550, 5.1444 | zuidoost van Utrecht schakelt de corridor van de A12 (naar Arnhem) over op de A27 noordwaarts |
| b3 | 3 | Knooppunt Rijnsweerd (A27 × A28) | 52.0919, 5.1611 | bij Utrecht Science Park kiest de route de A28 (Amersfoort) i.p.v. verder op de A27 naar Almere |
| b3 | 4 | Knooppunt Hoevelaken (A28 × A1) | 52.1756, 5.4276 | bij Amersfoort gaat de corridor over op de A1 oostwaarts (Apeldoorn–Deventer) i.p.v. noordwaarts naar Zwolle |
| b3 | 5 | Knooppunt Buren (A1 × A35) | 52.2855, 6.7432 | bij Wierden verlaat de route de A1 (naar Duitsland/Bad Bentheim) voor de A35 naar Almelo |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Port Hope Conversion Facility | Cameco | UO3 → UF6 (voor verrijking elders) + UO2-poeder (CANDU) | vergund 12,5 Mkg U als UF6 + 2,8 Mkg U als UO2/jaar | [4], reeds in `uranium-mcarthurriver-porthope` §5 |
| Urenco Almelo | Urenco Nederland (1/3 NL-staat, 1/3 UK, 1/3 E.ON/RWE) | UF6 (natuurlijk/laag verrijkt) → LEU-UF6 (centrifuge-verrijking, tot 5% U-235; sinds 2025 ook LEU+) | Almelo-specifieke capaciteit niet gevonden binnen het zoekbudget; Urenco Group plant **+1,5 miljoen SWU/j** erbij op Almelo tegen 2030 | [2][3] |

## 6 · Stoppunt
De brief stopt bij Urenco Almelo: dit is de verrijkingsstap uit het ketenontwerp (conversie → verrijking), en er is geen gedocumenteerde vervolgbestemming (splijtstoffabricage) voor déze specifieke lading — fase D vervalt, want geen bron noemt de fabriek na Almelo voor dit materiaal.

## 7 · Open punten
- **Bestemmingsclaim Almelo: aannemelijk, één bron (2013).** De Federal Register-kennisgeving (FR Doc. 2013-15975, 3 juli 2013) bevestigt een concrete overdracht van 591.716 kg UF6 (400.000 kg U) van Cameco Port Hope naar Urenco Almelo voor toll enrichment — dit is een **12 jaar oude** bevestiging van één historische lading, geen bewijs van een lopende actuele stroom. Cameco's eigen site noemt alleen generiek "enrichment plants in the United States, Japan and Europe". Bij het bakken een actuelere bron proberen (Urenco- of Cameco-jaarverslag, NRC-exportvergunning) vóór definitieve vastlegging; alternatieven blijven Urenco Gronau (via Rotterdam/Duisburg) of Orano Tricastin (via Rotterdam/Marseille).
- b2's km is een **extrapolatie**, geen gemeten waarde: de grootcirkelafstand (5.956 km) × de inflatiefactor van het bekende Duluth→Rotterdam-ijkpunt (8.031/6.485 = 1,238) geeft ~7.377 km; dit moet bij het bakken tegen de echte MARNET-uitvoer getoetst worden.
- b3: de werkelijke route (OSRM, 188,8 km) is 26% langer dan de ~150 km-schatting uit het ketenontwerp — het ontwerp noemde kortweg "A12/A1", maar de kortste weg schakelt via A27/A28 om Utrecht/Amersfoort, niet rechtstreeks A12→A1.
- Geen gedocumenteerd jaarvolume specifiek Port Hope→Almelo; alleen de vergunde Port Hope-capaciteit (§5) en de eenmalige 2013-lading (400 t U) zijn gebrond.
- Spoornet niet nodig (bevestigd in het ketenontwerp: `spoornet_nodig: false`).
- MARNET-zeeknoop 4821 is een routeerpunt, geen site — geen satellietblik nodig/mogelijk (open water).

## 8 · Bronnen
[1] Routebrief `uranium-mcarthurriver-porthope.md` §3/§8 — Port Hope Conversion Facility, 1 Eldorado Place, 43.9437/-78.2955, satelliet bevestigd (Cameco jaarverslag 2015 + OSM-adrespunt).
[2] Wikipedia (en), "Urenco Group" — subsidiaries/eigendom (1/3 NL-staat via Ultra-Centrifuge Nederland, 1/3 Uranit/E.ON+RWE, 1/3 UK), Treaty of Almelo 1971, +1,5 mln SWU/j uitbreiding Almelo tegen 2030. https://en.wikipedia.org/wiki/Urenco_Group
[3] Wikipedia (en), "Almelo" — Urenco Nederland als grote werkgever, gas-centrifugemethode, ~5% U-235. https://en.wikipedia.org/wiki/Almelo
[4] Cameco, jaarverslag 2015 — Port Hope Conversion Services, vergunde capaciteit 12,5 Mkg U als UF6 + 2,8 Mkg U als UO2/jaar. https://www.cameco.com/annual_report/2015/mda/our-operations-and-projects/fuel-services/port-hope-conversion-services/
[5] U.S. Federal Register, Vol. 78 No. 128 (3 juli 2013), FR Doc. 2013-15975, p. 40132 — subsequent arrangement: 591.716 kg UF6 (400.000 kg U) van Cameco Port Hope naar Urenco Almelo voor toll enrichment. https://www.govinfo.gov/content/pkg/FR-2013-07-03/pdf/2013-15967.pdf
[6] Photon/OSM (via komoot geocoder, ODbL) — "Urenco", Drienemansweg 1 (office) 52.33537,6.69207; industrieel gebouw Drienemansweg 52.33910,6.69223; "Enrichment Technology" Planthofsweg 52.33846,6.68742. https://photon.komoot.io
[7] Wikipedia (nl), "Knooppunt Gouwe" 52.02222,4.65417 · "Knooppunt Lunetten" 52.0550,5.14444 · "Knooppunt Rijnsweerd" 52.09194,5.16111 · "Knooppunt Hoevelaken" 52.17561,5.42759 · "Knooppunt Buren" 52.28551,6.74323.
[8] OSRM-router (project-osrm.org, publieke demo-server op OSM-data) — routeberekening Rotterdam RHB (4.4585,51.8935) → Urenco Almelo (6.6922,52.3391): 188,8 km via A20/A12/A27/A28/A1/A35.
[9] Haalbaarheidstoets `uranium-porthope-almelo` (bindend invoerdocument bij deze brief) — MARNET-zeeknoop-check: Port Hope op 65,9 km van de dichtstbijzijnde bruikbare zeeknoop (knoop 4821, 43,4992/-78,8371), incl. de Seaway-zone.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `uranium-porthope-almelo`** → `v2/data/stroomroute-uranium-porthope-almelo.json` — 3 benen, **6.609,7 km**, 2.985 punten, 3 markers. zee 67,3 (stippel) + 6.350,7 = 6.418,0 km · truck 191,7 km.
Recept: `bak_stromen.sh` (functie `bak_uranium_porthope_almelo`).

**b1 (zee, haven-aanloop, nieuwe run):** `timeout 300 python v2/tools/maak_havenaanloop.py --naam uranium-porthope-almelo-aanloop-porthope --van 43.9437,-78.2955 --naar 43.4992,-78.8371 --uit v2/build-cache/ais/graaf/uranium-porthope-almelo-aanloop-porthope.geojson` — lukte in de **eerste poging** (geen terugval nodig): gekozen trap cel 0,005° gebufferd, **67,3 km over 56 punten, omwegfactor 1,022, 0,00 km over land**. Tegen de brief (~66 km, haalbaarheidstoets) = **+2,0%, ruim binnen ±15%**. `--stippel-geojson` ingezet zoals de bak-aanwijzing voorschreef.

**b2 (zee, standaard MARNET-router, GEEN stippel):** `--been "zee|…|43.4992,-78.8371|51.8935,4.4585"`. Snap kop 0,000 km (exact op zeeknoop 4821), snap staart **0,727 km** op Rotterdam RHB (dezelfde orde als het vaste RHB-snapgetal elders op de kaart, 0,70 km — geen nieuwe bevinding). Resultaat **6.350,7 km over 687 punten**. **Toets tegen de brief-schatting van ~7.400 km (webcheck-extrapolatie via de Duluth→Rotterdam-inflatiefactor): −14,2%** — net binnen de ±15%-norm, maar aan de rand. De brief zei zelf dat dit getal een extrapolatie was en tegen de echte MARNET-uitvoer getoetst moest worden; de bake-uitvoer (6.350,7 km) is nu het gemeten getal en vervangt de schatting als beste bron. Niet gecorrigeerd of via-punt bijgeschoven — dit is de daadwerkelijke MARNET-routering over Grote Meren/Seaway → Atlantische oversteek.

**b3 (truck, nieuwe wegscan):** profiel `uranium-porthope-almelo-rotterdam-almelo` toegevoegd in `maak_stroombeen_weg.py` (extract `nederland`, refs A20/A12/A27/A28/A1/A35, vensterKm 40). Scan: 80.873 km ruw over het NL-extract, 27 keerlussen gesnoeid (199,9 → 191,6 km), eindklassen binnen 12 km van de ankers meegenomen (first mile 0,24 km, last mile 1,15 km, buiten de lengtetoets). **Resultaat 191,7 km (getekende lijn) tegen gepubliceerd 189 km (OSRM-webcheck) = +1,4%, binnen ±15%.** Het ketenontwerp noemde ~150 km — bevestigd bekend open punt (brief §7), niet dichtgetrokken: de kortste route schakelt via A27/A28 om Utrecht/Amersfoort in plaats van rechtstreeks A12→A1.

**Toets:** naad b1→b2 **0,00 km** (haven-aanloop eindigt exact op de MARNET-zeeknoop). Naad b2→b3 **0,73 km** (Rotterdam-zeesnap tegen het truck-startpunt op de RHB-anker) — ruim binnen de ≤5 km-norm. `toets_knikken.py`: zeebeen 5 knikken/0 omkeringen (2 spikes bij Cape Cod-achtige kustbochten, 3 krappe bochten op open zee — geen terugloop); truckbeen **15 knikken, 2 omkeringen, beide TERUGLOOP** (174,8°/R34m bij Knp. Lunetten 52.05508,5.14382 en 174,4°/R49m bij Knp. Rijnsweerd 52.09085,5.15515). `toets_rechte_benen.py --min-km 5`: **geen enkel been van deze stroom in de lijst** — b1 heeft omwegfactor 1,022 (geen rechte lijn ondanks stippel), b2/b3 zijn reële geroutete geometrie. json geldig: versie 2, punt_formaat lonlat, modaliteiten uitsluitend {zee, truck}, elk been ≥2 punten, bestandsgrootte **55,7 KB** (< 300 KB). Alle 3 markers liggen exact op hun been-uiteinde (Port Hope = start b1, Rotterdam RHB = start b3 op de anker-projectie, Almelo = eind b3).

**Gereedschapslessen:**
- De haven-aanloop Port Hope lukte in één keer, zonder terugval — een gunstige uitzondering op de handleiding-voorbeelden (Hamburg/Honmoku liepen vast op de 300s-timeout); Lake Ontario is klein genoeg voor de fijnste trap (0,005°) om binnen de tijd te convergeren.
- Twee TERUGLOOP-punten op het truckbeen zitten allebei op klaverbladknooppunten (Lunetten, Rijnsweerd) ondanks 27 al gesnoeide keerlussen — hetzelfde "overschiet-en-terug op een via-kruispunt"-patroon dat elders in het project bekend staat (een via-snap op het kruis kan achter de rijrichting liggen). Niet gerepareerd binnen deze lichte bake: de via-punten komen direct uit de brief (Wikipedia-coördinaten van de knooppunten zelf) en bijschuiven om de terugloop weg te poetsen zou tegen de "geen via-punt bijschuiven"-regel ingaan; de hoofdroute (191,7 km, +1,4% van het gepubliceerde getal) is er niet merkbaar door beïnvloed.
- b2's brief-schatting (~7.400 km) bleek bij het meten 14,2% te hoog — de Duluth→Rotterdam-inflatiefactor is blijkbaar geen goede voorspeller voor een Lake Ontario→Rotterdam-traject dat een ander deel van de Seaway/Atlantische route volgt; het gemeten getal (6.350,7 km) is nu de vaste waarde voor deze stroom.
