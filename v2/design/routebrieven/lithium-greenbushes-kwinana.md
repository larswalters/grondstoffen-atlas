# Routebrief (licht) · Lithium — Greenbushes → Kwinana (Australië)

**stroom-id:** `lithium-greenbushes-kwinana` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat van Talisons Greenbushes-mijn gaat per truck (~223 km, eigen routering) over de South Western Hwy, de Bunbury-omleiding, Forrest Hwy en Kwinana Fwy, daarna via Anketell Rd, Rockingham Rd en Leath Rd naar de noordpoort van Tianqi's hydroxidefabriek TLK, 61 Donaldson Road, Kwinana Beach (Train 1; DWER-licentie L2981 [1]).
**Welke as van het verhaal:** *de Tianqi-streng naar de eigen Australische raffinaderij*, naast de export via Bunbury (zhangjiagang) en de Albemarle-streng (kemerton). Volume: Train 1 vergund op **156.810 t droog concentraat in → 24.000 t/j LiOH·H2O ≈ 21 kt LCE/j** (×0,88), peiljaar 2026 [1]; Train 2 (totaal 48.000 t LiOH/j) staat op hold [1][2]; werkelijke productie niet gepubliceerd, de calciner draaide 40 dagen tussen nov 2024 en jan 2025 [1].
**Afwijkingen van het ontwerp (bindende toets verwerkt):** eigen wegprofiel (geen kopie van kemerton b1); TLK-anker **verlegd van -32.2400,115.7700 (sitelaag, onzeker) naar -32.2150,115.7790** (2,9 km noordoostelijk, bron-gelegd); aanvoer vanuit het zuiden via Anketell Rd, niet via Kenwick (dat is de oostelijke Roe Hwy-aanvoer van mtholland, ~40 km omweg); volume 21 i.p.v. 44 kt LCE (Train 1).

## 1 · Ketenkaart
```
Greenbushes-concentraatloods `li-gb-laadplek` ──(b1 truck · aannemelijk: één bron voor modus en herkomst, route eigen routering ·
South Western Hwy N → Wilman Wadandi Hwy (Bunbury-omleiding) → Forrest Hwy → Kwinana Fwy → Anketell Rd → Rockingham Rd →
Leath Rd → Donaldson Rd · ~223 km)──► TLK Kwinana `li-tlk-fabriek` ⏹ stoppunt (hydroxide gaat per container naar Fremantle, geen afnemer)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (spodumeenconcentraat — aannemelijk: één bron, route eigen routering) | `li-gb-laadplek` → `li-tlk-fabriek` | Maranup Ford Rd/Stanifer St → South Western Hwy (1) → Wilman Wadandi Hwy (101) → Forrest Hwy (1) → Kwinana Fwy (2) → Anketell Rd → Rockingham Rd (1) → Leath Rd → Donaldson Rd | **geen gepubliceerde wegkm voor dit been.** Indicatie ≈ **208** (Greenbushes 250 km ten zuiden van Perth [5] − Kwinana Beach 42 km van Perth CBD [6], collineair gerekend); eigen OSRM **223,2** via de gekozen via-punten (219,4 via Kulija Rd/Mandurah Rd/Mason Rd) [8] (+7% op de indicatie, geen norm); **hemelsbreed 185,3 km, geen wegkm**; deelstuk Forrest Hwy 95,67 km [7] | maak_stroombeen_weg (extract australie, nieuw profiel) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-gb-laadplek` | mijn / laadplek | Greenbushes-concentraatloods (Talison: Tianqi/IGO 51% · Albemarle 49%) | -33.8650, 116.0551 | **hergebruik letterlijk** -33.86495,116.05505 uit `lithium-greenbushes-zhangjiagang.md` §2a(1) [9] | **bron-gelegd** (z18 aldaar; hier z16 herzien: kruis op een lange witte loods tussen de weg en de verwerkingsinstallatie, mijnput oost, tailingsdam west en zuid) |
| `li-tlk-fabriek` | raffinaderij (losplek, stoppunt) | Tianqi Lithium Hydroxide Processing Plant (TLK), 61 Donaldson Road, Lot 201 DP 407762 | -32.2150, 115.7790 | adres en lot [1][2]; lus-geometrie Donaldson Rd [3]; onafhankelijk: v1-negatief anker "Kwinana (TLEA)" -32.21468,115.77858 ligt 53 m ernaast [9] | **bron-gelegd** (z17 live: kruis midden in het procescomplex, kiln/pyro-lijn, twee witte loodsen noord, tankwagens en containers oost, oranje onaffe staalframes zuid = Train 2; ~18 ha; Wayback 2017-10: kale gesloopte gebiedsvlakte, 2020: fabriek staat; past op de ex-BHP/HIsmelt-brownfield [1]) |

## 4 · Via-punten (b1 — corridorkeuzes; lat, lon op de doorgaande weg, geen dorpscentra)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Balingup (South Western Hwy) | -33.7862, 115.9844 | enige noordwaartse route vanaf de mijn; op de highway-vertex, 0 m van een trunk-way |
| b1 | 2 | Donnybrook (South Western Hwy) | -33.5766, 115.8259 | idem, gedeelde Bunbury-corridor |
| b1 | 3 | Boyanup (South Western Hwy) | -33.4836, 115.7279 | idem; laatste punt vóór de Bunbury-omleiding |
| b1 | 4 | SWH → Wilman Wadandi Hwy, nabij Gelorup | -33.3997, 115.6981 | corridorkeuze: Bunbury-omleiding i.p.v. door Bunbury; 22 m van een trunk-way |
| b1 | 5 | Forrest Hwy → Kwinana Fwy (Ravenswood, ten oosten van Mandurah) | -32.5709, 115.8143 | corridorkeuze: Forrest Hwy/Kwinana Fwy i.p.v. Old Coast Rd door Mandurah; 5 m van een motorway-way |
| b1 | 6 | Anketell Rd, oostelijk deel | -32.2088, 115.8425 | corridorkeuze: Kwinana Fwy tot de Anketell Rd-afrit (aanvoer naar de noordpoort) i.p.v. de afrit Kulija Rd/Mandurah Rd (die variant is 3,8 km korter maar komt via Mason Rd van zuid binnen) |
| b1 | 7 | Anketell Rd × Rockingham Rd | -32.2096, 115.7856 | pint Rockingham Rd zuidwaarts; 2 m van een secondary-vertex |
| b1 | 8 | Leath Rd × Donaldson Rd (noordwesthoek) | -32.2128, 115.7765 | pint de noordelijke Donaldson Rd = "northern site road" waarlangs grondstof wordt aangeleverd [1]; 5 m van de way |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| TLK Kwinana, Train 1 | Tianqi Lithium Kwinana Pty Ltd (Tianqi/IGO-JV TLEA) | spodumeenconcentraat (8% vocht, per truck) → LiOH·H2O, bijproduct Na2SO4 | 24.000 t LiOH·H2O/j ≈ 21 kt LCE (vergund, 156.810 t concentraat); Train 2 op hold, totaal 48.000 t | [1][2][10] |

## 6 · Stoppunt
De brief stopt bij de poort van TLK: de enige documentatie na de fabriek is dat hydroxide en sulfaat in containers naar Fremantle Port gaan voor export [1], zonder afnemer of bestemming (fase D vervalt).

## 7 · Open punten
- **De route zelf is niet gebrond.** DWER noemt vrachtwagens als aanvoermodus en Greenbushes als herkomst [1] (geen spoor), maar geen bron geeft de corridor; de Anketell-keuze volgt uit de noordelijke leveringsweg [1] en is +4 km (+2%) tegenover de kortere Kulija/Mandurah Rd-variant (219,4 km).
- **Geen gepubliceerde wegkm** voor Greenbushes → Kwinana; 208 is een afleiding uit twee Wikipedia-afstanden [5][6], 223,2 een eigen OSRM-routering (OSM-net).
- **Welk gebouw precies?** Het anker ligt op het procescomplex, niet op een benoemd gebouw; de perceelgrens (Lot 201) is niet gezien. Early reports spraken van "20 ha aan Mason Road" (Business News, achter betaalmuur [11]); DWER geeft Donaldson Road [1].
- **Werkelijke bezetting onbekend:** Train 1 draaide time-limited, productie niet gepubliceerd; S&P (apr 2026) en mining.com over de rendabiliteit zijn alleen via de haalbaarheidstoets gezien, niet door mij geopend.
- **Sitelaag centraal corrigeren:** `w-li-kwinana` (-32.2400,115.7700) ligt 2,9 km zuidwestelijk van TLK (z16 daar: groot industrieterrein met lange witte loodsen en pier, niet TLK) → -32.2150,115.7790, capaciteit 44 → 21 kt LCE (Train 1). De remark "TLK 2,4 km zuidelijker dan Covalent" in `lithium-mtholland-kwinana.md` klopt niet: TLK ligt 0,83 km oostnoordoost van het Covalent-anker.
- Last mile: geen eigen been; het anker ligt 0,23 km van de noordelijke Donaldson Rd. Optioneel later: truck TLK → Fremantle (`ree-fremantle-kade`), alleen met een afnemer.

## 8 · Bronnen
[1] DWER, decision report licence L2981/2025/1 Tianqi Lithium Kwinana Pty Ltd (2026-03-03) — adres 61 Donaldson Road, Lot 201 DP 407762, 156.810 t/j concentraat, 24.000 t/j LHM, spodumeen van Greenbushes per vrachtwagen, northern site road, export per container naar Fremantle. https://www.der.wa.gov.au/images/documents/our-work/licences-and-works-approvals/Decisions_/L2981/L2981%2003-03-2026%20DR.pdf
[2] DWER, amendment report W5977/2016/1 (2025-07-25) — Train 2 op hold, Train 1 enige draaiende trein. https://der.wa.gov.au/images/documents/our-work/licences-and-works-approvals/Decisions_/W5977/W5977%2025-07-2025%20CEO%20amendment%20AR.pdf
[3] OpenStreetMap (ODbL) via Nominatim — Donaldson Road way 63521670 (lus -32.2231…-32.2129 / 115.7763…115.7847), Mason Road, Kwinana WtE -32.2105/115.7785. https://nominatim.openstreetmap.org
[4] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-lithium-greenbushes-kwinana-tlk-z17.png` (live), `-tlk-2017-wb23264.png`, `-tlk-2020-wb9181.png`, `-donaldson.png`, `-masonrd.png`, `-tlkz16.png` (oud sitelaag-punt), `-greenbushes.png`.
[5] Wikipedia, Greenbushes, Western Australia — "250 km south of Perth". https://en.wikipedia.org/wiki/Greenbushes,_Western_Australia
[6] Wikipedia, Kwinana Beach, Western Australia — 42 km van Perth CBD. https://en.wikipedia.org/wiki/Kwinana_Beach,_Western_Australia
[7] Wikipedia, Forrest Highway — 95,67 km, Ravenswood → East Bunbury. https://en.wikipedia.org/wiki/Forrest_Highway
[8] OSRM-demoroutering (project-osrm.org), Greenbushes → TLK, 2026-10-09: 219,1 km vrij, 219,4 via Kulija Rd, 223,2 via de via-punten §4. http://router.project-osrm.org
[9] `lithium-greenbushes-zhangjiagang.md` §2a(1) (anker `li-gb-laadplek`) en negatieve ankers (Kwinana TLEA -32.21468,115.77858); `lithium-mtholland-kwinana.md` (Covalent -32.2188,115.7714).
[10] WA-regering, "Largest of its kind lithium hydroxide plant launched in Kwinana" (2019-09-10) — twee fasen, 48.000 t/j. https://www.wa.gov.au/government/media-statements/McGowan%20Labor%20Government/Largest-of-its-kind-lithium-hydroxide-plant-launched-in-Kwinana-20190910
[11] Business News, Tianqi-plan Kwinana (alleen kop gezien, betaalmuur). https://businessnews.com.au/node/375722
[12] Geofabrik `australie-latest.osm.pbf` en de weg-scancaches `v2/build-cache/land/weg-australie-*.json` (alle via-punten §4 liggen ≤ 22 m van een gescande trunk/motorway/primary/secondary-way).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Resultaat:** `v2/data/stroomroute-lithium-greenbushes-kwinana.json` (41,6 KB, contract versie 2, `lonlat`) · **1 been · 224,2 km · 1.913 punten · 2 markers** · geen naden (enkel been) · markers 0,007 km (mijn) en 0,000 km (TLK) van de lijn.

| # | modaliteit | km (gemeten) | km (brief) | afwijking | stippel |
|---|---|---|---|---|---|
| b1 | truck — spodumeenconcentraat Greenbushes → Tianqi TLK Kwinana (aannemelijk: één bron, route eigen routering) | 224,2 getekend (wegnet 224,0 + 0,06 plant-verbinding + 0,15 kade-verbinding) | 223,2 (eigen OSRM; geen wegkm), indicatie 208, hemelsbreed 185,3 | **+0,4% t.o.v. OSRM**, +7,8% t.o.v. de indicatie 208, omwegfactor 1,21 — indicatie, geen norm | nee |

**Recept:** profiel `lithium-greenbushes-kwinana-greenbushes-kwinana` in `maak_stroombeen_weg.py` (10 via-punten uit §4 plus de twee ankers, extract `australie`, refs 1/2, `trimStaart`, vensterKm 40, geen `corridorKlassen`) → `lithium-greenbushes-kwinana-weg-greenbushes-kwinana.geojson`; functie `bak_lithium_greenbushes_kwinana()` in `bak_stromen.sh` (één `--been-geojson truck`, twee `--marker`); tussenuitvoer en wegscan-log met prefix `lithium-greenbushes-kwinana-` in `v2/build-cache/ais/graaf/`.
**Toetsen:** snaps alle via-punten ≤ 0,02 km, mijn-anker 0,06 km, TLK-anker 0,15 km · `toets_knikken` 9 knikken ≥ 60° (allemaal spikes van 7–24 m op ankers en junctiepunten), **0 omkeringen, 0 terugloop** · `toets_rechte_benen` geen melding (geen rechte lijn) · `json.load` ok, versie 2, `lonlat`, modaliteit {truck}, 1 been van 1.913 punten · `bak_stromen.sh` LF (0 CRLF), `bash -n` ok.

**Wegbron.** `wegscan_puur.py` (pure-Python PBF-lezer; pyosmium geblokkeerd, Overpass uit) op `australie-latest.osm.pbf` (953 MB, venster 115,05–116,71 / −34,51…−31,56): ~45 s scan, 38.793 ways bewaard, daarna Dijkstra met de gewone `corridor_keten`. Geen terugval op de unie van oude scancaches nodig, dus de les over gevouwen caches (mtholland-kwinana §9) speelde hier niet.

**Afwijkingen van de brief:** geen. De via-punten uit §4 zijn ongewijzigd overgenomen (brief-coördinaten op 5 decimalen); de Anketell-keuze gaf geen uitbuiging, het Kulija-alternatief (219,4 km) is niet nodig gebleken. Het segment Gelorup → Ravenswood is 103,1 km (Wilman Wadandi Hwy + Forrest Hwy, tegen Forrest Hwy 95,67 km [7] plus de Bunbury-omleiding), de rest klopt met de brief: Greenbushes → Balingup 13,3 · → Donnybrook 30,3 · → Boyanup 15,5 · → Gelorup 10,0 · → Ravenswood 103,1 · → Anketell oost 44,0 · → Rockingham Rd 5,5 · → Leath/Donaldson 1,9 · → anker 0,4 km.

**Bevindingen / open (ongewijzigd uit §7 + nieuw):**
- Route nog steeds niet gebrond (DWER noemt alleen modus en herkomst); de +0,4% op OSRM bevestigt alleen dat de router op hetzelfde OSM-net rijdt, niet dat Tianqi deze corridor kiest.
- First mile over kleine klassen 3,04 km en last mile 1,68 km (residential, service, tertiary) — de aansluiting op de Greenbushes-installatie en de Donaldson Rd-lus; geen eigen been (< 2 km, brief §7).
- 8 keerlussen gesnoeid door het tool (dubbel gereden stukken op ankers/junctiepunten), lengte 224,0 → 224,0 km: effect verwaarloosbaar.
- Nog centraal: sitelaag `w-li-kwinana` van −32.2400/115.7700 naar −32.2150/115.7790 en 44 → 21 kt LCE (Train 1); de opmerking in `lithium-mtholland-kwinana` over "2,4 km zuidelijker" corrigeren (het is 0,83 km oostnoordoost van Covalent).
- **Registerregel (centraal):** `{ "sleutel": "li-gkw", "bestand": "stroomroute-lithium-greenbushes-kwinana.json", "grondstof": "lithium", "label": "Greenbushes → Kwinana (Tianqi TLK)", "aan": true, "noot": "M31 · golf 9 (2026-10-09): spodumeenconcentraat per truck (aannemelijk: één bron) van de Greenbushes-loods via de South Western Hwy, Bunbury-omleiding en Kwinana Fwy naar Tianqi's hydroxidefabriek TLK in Kwinana" }` — `li-gk` is bezet (greenbushes-kemerton), daarom een derde letter.

**Lessen voor volgende bakers:** (1) `wegscan_puur.py --profiel <sleutel>` volstaat voor een Australische keten: geen eigen wrapper, geen unie van caches; een weg-slot plus een reus-slot (australie) en ~1 minuut; (2) via-punten die in de brief al op een trunk/motorway-vertex lagen (≤ 22 m) snappen zonder omweg, dus de brief-lijst kan ongewijzigd het profiel in; (3) de ankerkoppeling vanaf de Greenbushes-loods (0,06 km) en de noordpoort-aansluiting op de Donaldson Rd-lus (0,15 km) vragen geen eindKlassen-override.
