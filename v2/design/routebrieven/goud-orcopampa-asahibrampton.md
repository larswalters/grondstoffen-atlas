# Routebrief (licht) · Goud — Orcopampa → Lima → Brampton (Peru → Canada)

**stroom-id:** `goud-orcopampa-asahibrampton` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) ·
**status:** gebakken
**Keten in één zin:** doré van de Orcopampa-mijn (Buenaventura, Arequipa) per truck naar het vliegveldje SPOR, per vlucht
(grootcirkel) naar de vrachtterminal van Lima (LIM), per vrachtvlucht (grootcirkel, aannemelijk) naar Toronto Pearson (YYZ) en per truck
naar Asahi Refining Canada in Brampton, Ontario (raffinaderij, stoppunt).
**Welke as van het verhaal:** Zuid-Peru → Canada: doré van een bijna uitgeputte Andesmijn naar de Asahi-raffinaderij. Volume **≈ 1,75 t Au/j** (56.385 oz
verkocht in 2025, 2024: 70.627 oz = 2,20 t; koz ÷ 32,15; Buenaventura 20-F FY2025 [1]). Welk deel naar Asahi Canada gaat is niet gepubliceerd:
Asahi Refining Canada is 17,13% van de totale verkopen (2024: 17,54%), voor vier mijnen samen [1].

## 1 · Ketenkaart
```
Orcopampa-plant (CIL + flotatie) `au-orcopampa-plant`
  ──(b1 truck · AR-660 → AR-655 · 5,6 wegkm [OSRM][5])──► SPOR-apron (NO-kop van de gravelbaan) `au-orcopampa-spor`
  ──(b2 lucht · vlucht SPOR → LIM, grootcirkel, aannemelijk · 630 km)──► Lima Cargo City (LIM) `au-lim-vrachtterminal` (hergebruikt)
  ──(b3 lucht · vlucht LIM → YYZ, grootcirkel, aannemelijk · 6.200 km)──► Toronto Pearson cargo-apron (YYZ) `au-yyz-vrachtterminal` (hergebruikt)
  ──(b4a stippel airside 0,09 km · b4 truck · Britannia Rd E → Courtneypark Dr E → Dixie Rd → Steeles Ave E → Glidden Rd · ca 13 wegkm [5])──►
Asahi Refining Canada, 130 Glidden Road, Brampton `au-asahi-brampton` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Orcopampa-plant → SPOR-apron | AR-660 → AR-655 (mijnweg ten ZO van het dorp, langs de pit, naar de NO-kop van de baan) | **5,56 wegkm** (OSRM [5]); hemelsbreed 4,4 [berekend] | maak_stroombeen_weg (extract peru) | nee; waar de scan op `track` stukloopt: eindigt op de dichtstbijzijnde weg + korte stippel (§7) |
| b2 | B | lucht | SPOR → LIM | vlucht SPOR → LIM, grootcirkel (aannemelijk: één bron voor de bereikbaarheid, geen bron voor de doré-vlucht) | **630,1** grootcirkel [berekend] | maak_luchtbeen | nee, doorgetrokken; onzekerheid in de beennaam |
| b3 | C | lucht | LIM → YYZ | vrachtvlucht LIM → YYZ, grootcirkel (aannemelijk: één bron voor "Asahi-vlucht in Lima" [1], bestemming Canada volgt uit de verkooptabel, niet uit de vlucht) | **6.199,7** grootcirkel [berekend] | maak_luchtbeen | nee, doorgetrokken |
| b4a | D | truck | YYZ-platform → openbare weg (43.6786, -79.6345) | eigen terrein, airside (patroon `goud-guyana-ottawa` b4) | 0,09 [guyana-brief] | `--stippel` | ja: airside |
| b4 | D | truck | YYZ landside → Asahi Brampton | Britannia Rd E → Courtneypark Dr E → Dixie Rd → Steeles Ave E → West Dr → Glidden Rd | **ca 13,0 wegkm** (OSRM [5]); hemelsbreed 7,06 [berekend] | **letterlijke kopie** van het YYZ → Brampton-been van `goud-jacobina-asahibrampton` | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-orcopampa-plant` | mijn / laadplek | Orcopampa-verwerkingsplant (Buenaventura, CIL + flotatie, 3.000 t erts/dag [1]) | -15.2718, -72.3297 | [1][sat] | bron-gelegd (z16 gezien: gebouwencomplex met tanks, indikkers en een groen bassin, direct ten NO van de open pit met tailingsdam; kruis ligt op het complex) |
| `au-orcopampa-spor` | overslag / lucht | Orcopampa Airport (SPOR), apron op de NO-kop van de 1.980 m gravelbaan | -15.3077, -72.3471 | [2][4][sat] | **aannemelijk** (z17 gezien: gravelbaan ZW–NO, aan de NO-kop een kaal verhard vlak met keerlus en aansluitende weg; geen gebouwen of toestellen, dus de apronpositie is mijn aanwijzing, geen bron. Wikipedia -15.3125,-72.35 ligt midden langs de baan naast een grindgroeve, OSM-node -15.3153,-72.3533 aan de ZW-kop) |
| `au-lim-vrachtterminal` | overslag / lucht | Lima Cargo City, Jorge Chávez Int'l (LIM) | -12.0289, -77.1039 | letterlijk uit `goud-yanacocha-ticino.md` [6] | bron-gelegd (daar z15: loodsencluster O van de banen, landzijde) |
| `au-yyz-vrachtterminal` | overslag / lucht | Toronto Pearson cargo-apron (Cargo 1/2/3) | 43.6785, -79.6335 | letterlijk uit `goud-guyana-ottawa.md` [7] | bron-gelegd (daar z15+z16: apron tussen drie vrachtloodsen met wide-bodies) |
| `au-asahi-brampton` | losplek / raffinaderij | Asahi Refining Canada Ltd, 130 Glidden Road, Brampton (L6W) | 43.6907, -79.7196 | [3][4] (OSM-adrespunt 130 Glidden Road: 43.690744, -79.7196236) | **aannemelijk** (z16 gezien: punt ligt op een groenstrook bij de Glidden Road-aansluiting op de snelweg, omgeven door bedrijfsgebouwen; welk pand de raffinaderij is, is niet te zien; naam staat niet in OSM). Afstand tot YYZ-anker 7,06 km, consistent met OSRM 13,0 wegkm |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | AR-660 / AR-655-splitsing, ZO-rand van Orcopampa | -15.2729, -72.3381 | OSRM-manoeuvrepunt [5]; sluit de dorpskern en een route door het dorp uit, de weg loopt hier langs de pit naar het zuiden (z16: weg van de plant westwaarts langs de noordrand van de pit) |
| b1 | 2 | AR-655 halverwege | -15.2964, -72.3345 | OSRM-manoeuvrepunt [5]; pint de AR-655 langs de rivier/akkers naar de NO-kop van de baan, niet naar de ZW-kop (OSM-node) |
| b4 | – | **geen eigen via-punten: kopie.** Terugval bij ontbreken van het jacobina-been (OSRM-manoeuvrepunten [5], niet satelliet-gelegd): Britannia Rd E 43.6778,-79.6373 · Courtneypark Dr E 43.6660,-79.6315 · Dixie Rd 43.6636,-79.6581 · Steeles Ave E 43.6952,-79.7011 · West Dr 43.6907,-79.7062 · Glidden Rd 43.6952,-79.7129 | | corridor is het stuk Dixie Rd – Steeles Ave E; geen stadscentrum; eindanker 43.6907,-79.7196 |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Orcopampa-plant | Buenaventura (100%, huurconcessie tot 2043) | erts → doré (CIL) + flotatieconcentraat | 3.000 t erts/dag; 220.951 t verwerkt in 2025 | [1] |
| Asahi Refining Canada (Brampton) | Asahi Holdings (sinds 2015, ex Johnson Matthey) | doré → LBMA-baren | niet gepubliceerd | [3][8] |

## 6 · Stoppunt
De brief stopt bij Asahi Brampton: het 20-F noemt Asahi als afnemer van de doré van Orcopampa, Tambomayo, Coimolache en La Zanja [1]; wat de raffinaderij met de baren doet is niet gebrond. Fase E vervalt.

## 7 · Open punten
- **Binnen gelegd uit de haalbaarheidstoets:** been A is geen last mile (5,56 wegkm, OSRM [5]); beennamen b2 en b3 zijn "aannemelijk"; LIM/YYZ-anker hergebruikt; b4 kopie van het Brampton-been van goud-jacobina (zie onder).
- **Geen bron voor de vlucht SPOR → LIM met doré.** Het 20-F zegt alleen dat de mijn per lijnvlucht vanuit Lima bereikbaar is, over de weg 1.350 km via Arequipa (319 km) [1]; Wikipedia: het veld bedient de mijn [2]. Een zoekopdracht vond geen dienstregeling. Alternatief is een wegtransport naar Lima (niet getekend).
- **Bestemming Canada volgt uit de verkooptabel** (Asahi Refining Canada 17,13%), niet uit de vlucht: het 20-F zegt dat Buenaventura de goud aflevert bij "Asahi's designated flight" op Lima airport [1]. Niet bekend waarheen die vlucht gaat (YYZ aangenomen).
- **Risico: de mijn is bijna uitgeput.** Verkocht 56.385 oz in 2025 (min 20% t.o.v. 2024), reserves niet aangevuld, "approximately 1 more year of LOM" [1]; sluitingsplan goedgekeurd 2023 [1]. Het volume bestaat dus voor 2025, maar de stroom kan snel verdwijnen. Het aandeel van Orcopampa in de Asahi-leveringen is onbekend.
- **SPOR-apron is mijn aanwijzing** (geen gebouwen zichtbaar); **Asahi-pand niet te onderscheiden** (OSM-adrespunt, geen bedrijfsnaam). Wegkm b1 en b4 komen van de OSRM-demo-router, geen bedrijfs-/overheidsopgave.
- **b4 hangt af van `goud-jacobina-asahibrampton`:** op het moment van schrijven bestaat die brief niet (geen bestand, geen bak-functie, geen geojson in `v2/build-cache/ais/graaf/`). Bak-agent: wacht tot het been gebakken is en kopieer het geojson letterlijk; bestaat het niet, bak het been dan zelf over de terugval-via-punten (§4, extract canada, vensterKm 15) en laat jacobina het van jou kopiëren, nooit twee versies.
- De sitelaag kent alleen Asahi USA (Salt Lake City, w-ref-asahi, lat/lon null); Brampton staat er niet in.
- Eigen punt: de brief noemt Asahi-doré "per vlucht"; de eerste Lima-opslag/veiligheidsafhandeling (Lima Cargo City is een van meerdere agenten) is niet te onderscheiden.

## 8 · Bronnen
[1] Compañía de Minas Buenaventura, 20-F FY2025 (verkopen Orcopampa 56.385 oz / 70.627 oz, Asahi Refining Canada 17,13%, aflevering bij Asahi's vlucht in Lima, bereikbaarheid 1.350 km / 319 km / lijnvlucht, 1 jaar LOM, plant 3.000 t/d). https://www.sec.gov/Archives/edgar/data/1013131/000110465926053101/tmb-20251231x20f.htm
[2] Wikipedia, "Orcopampa Airport" — 15°18'45"S 72°21'00"W, baan 03/21 1.980 m gravel, bedient de Buenaventura-mijn. https://en.wikipedia.org/wiki/Orcopampa_Airport
[3] Asahi Refining, "About us" — Asahi Refining Canada, 130 Glidden Road, Brampton. https://www.asahirefining.com/about-us/
[4] OpenStreetMap (ODbL) via Nominatim/Photon — Orcopampa Airport node 1042081081 (-15.3152776,-72.3532851); adrespunt 130 Glidden Road (43.690744,-79.7196236). https://nominatim.openstreetmap.org
[5] OSRM publieke demo-router (OSM, 2026-10-31): plant → SPOR-NO-kop 5.555 m (AR-660, AR-655); YYZ-landside → Glidden Road 13.010 m. https://router.project-osrm.org
[6] `v2/design/routebrieven/goud-yanacocha-ticino.md` — anker `au-lim-vrachtterminal` (-12.0289, -77.1039).
[7] `v2/design/routebrieven/goud-guyana-ottawa.md` — anker `au-yyz-vrachtterminal` (43.6785, -79.6335), airside-stippel 0,09 km naar 43.6786, -79.6345.
[8] BullionVault 2014-12 / zoekresultaten — Asahi Holdings koopt Johnson Matthey goud-/zilverraffinage incl. Brampton (2015). https://www.bullionvault.com/gold-news/market-fundamentals/johnson-matthey-exits-gold-silver-refining-after-160-years-12152014
[sat] Satellietblik (Esri z15-z17, 2026-10-31): `v2/build-cache/satcheck/sat-goud-orcopampa-asahibrampton-plant.png`, `-plant16.png`, `-spor.png`, `-spor16.png`, `-asahi.png`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Bestand:** `v2/data/stroomroute-goud-orcopampa-asahibrampton.json` (15,6 KB, versie 2, lonlat) · functie `bak_goud_orcopampa_asahibrampton()` in `v2/tools/bak_stromen.sh` · profiel `goud-orcopampa-asahibrampton-plant-spor` in `maak_stroombeen_weg.py`. **Totaal 6.848,4 km, 5 benen, 5 markers, alle naden 0,000 km.**

| # | modaliteit | km gebakken | km brief | afwijking | stippel |
|---|---|---|---|---|---|
| b1 | truck plant → SPOR-apron | 5,6 | 5,56 (OSRM, geen officiele opgave) | +0,7% (OK) | nee |
| b2 | lucht SPOR → LIM | 630,1 | 630,1 | 0 | nee, doorgetrokken (aannemelijk) |
| b3 | lucht LIM → YYZ | 6.199,7 | 6.199,7 | 0 | nee, doorgetrokken (aannemelijk) |
| b4a | truck last mile YYZ-platform | 0,08 | 0,09 | afronding | ja, airside |
| b4 | truck YYZ → Asahi Brampton | 12,9 | ca 13,0 (OSRM, hemelsbreed 7,06) | -0,8% (indicatie) | nee |

**Recept.** b1: `wegscan_puur.py --profiel goud-orcopampa-asahibrampton-plant-spor` (extract peru, venster 10 km, refs AR-660 en AR-655, `eindKlassen` en `eindToegangPrivaat`, 3 segmenten 0,9 / 2,7 / 1,9 km, alle snaps <= 0,07 km, scan 58 s; de laatste 4,6 km lopen over tertiary, track en unclassified, dus de scan kwam wel door de gravelweg). b2 en b3: `maak_luchtbeen.py` (FeatureCollection, 27 en 249 punten). b4: het geojson `goud-jacobina-asahibrampton-weg-yyz-asahi.geojson` wordt LETTERLIJK hergebruikt (zelfde bestand, 310 punten, begint op 43.6786,-79.6345 en eindigt op het Asahi-anker); geen tweede versie. Markers: de vijf ankers uit §3. Bake: `bash v2/tools/bak_stromen.sh goud-orcopampa-asahibrampton`.

**Toelichting.**
- **b4a is een stippel** omdat het YYZ-vrachtplatform airside ligt (patroon goud-guyana-ottawa b4): 0,08 km van 43.6785,-79.6335 naar de openbare weg 43.6786,-79.6345.
- **b2 en b3 zijn vluchten**, doorgetrokken; "aannemelijk: een bron" staat in de beennaam. Geen bron dat doré via SPOR vliegt of dat de Asahi-vlucht naar YYZ gaat (§7); geen tussenlanding aangenomen.
- **b4 hangt aan de bake van goud-jacobina-asahibrampton**: dat been was klaar (01:22) voordat dit bakte; mijn bak verwijst naar hetzelfde bestand. Wordt het jacobina-been herbakken, dan moet deze stroom opnieuw gebakken worden om dezelfde lijn te houden.
- Geen zeebeen, geen haven-aanloop, geen fase D/E; stoppunt Asahi Brampton.
- `toets_knikken.py`: 30 knikken (2 op b1, 28 op het Brampton-been; kruispunten van ca 90 gr), 0 omkeringen, 0 terugloop. `toets_rechte_benen.py --min-km 5`: geen bevinding voor deze stroom. Markers 0,0 km van hun lijn.
- Km van b1 en b4 komen van de OSRM-demo-router (geen bedrijfs- of overheidsopgave): de +-15%-toets is een indicatie, geen norm.

**Lessen.** (1) Een peru-wegscan is licht (58 s, weg-slot). (2) Het Brampton-been bestaat al na de bake van jacobina; wie het deelt moet wachten tot dat bestand er staat (hier ca 8 min). (3) Mijn bijna uitgeput (circa 1 jaar LOM): de stroom kan snel vervallen.
