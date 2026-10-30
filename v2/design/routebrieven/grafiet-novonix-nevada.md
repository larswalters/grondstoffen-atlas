# Routebrief (licht) · grafiet — Chattanooga → I-40 → Tahoe-Reno (VS)

**stroom-id:** `grafiet-novonix-nevada` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) ·
**status:** gebakken
**Keten in één zin:** synthetisch anodemateriaal (AAM) uit NOVONIX Riverside (Chattanooga, Tennessee) gaat per
**truck** (werkaanname) ~3.800 km over I-24, I-40, US-93/I-11 en US-95 naar de Tesla Gigafactory 1 in het Tahoe-Reno
Industrial Center (Storey County, Nevada), waar Panasonic Energy Nevada de cellen maakt — de lange sunbelt-haul
naast de bestaande De Soto-tak (`grafiet-lakecharles-desoto`). **Aannemelijk: één bron** — de bestemming Nevada is niet gebrond (§7).
**Welke as van het verhaal:** *de ex-China buildout, synthetisch, naar de tweede Panasonic-fabriek.* Bindende offtake
van Panasonic Energy: **minimaal 10 kt AAM over 2025–2028** voor zijn Noord-Amerikaanse (U.S.) fabrieken [1]; het aandeel
voor Nevada is niet gepubliceerd. **Jaarvolume 2026: 0 kt AAM/j** (monsters; massaproductie voor Panasonic H2 2027,
volle capaciteit uitgesteld naar sept 2031) [2][3]; nameplate Riverside 20 kt AAM/j [2]. Eenheid kt AAM per jaar, peiljaar 2026.

## 1 · Ketenkaart
```
NOVONIX Riverside, Chattanooga `gr-riverside-fabriek` (naaldcokes → AAM; 2026: monsters)
  ──(b1 truck · I-24 W → Nashville → I-40 W (Memphis, OKC, Amarillo, Albuquerque, Flagstaff, Kingman) → US-93/I-11 Las Vegas
     → US-95 N (Beatty, Tonopah, Mina, Schurz) → US-95A → I-80 W → USA Parkway · OSRM 3.807 km · aannemelijk: één bron)──►
Tesla Gigafactory 1 / Panasonic Energy Nevada, TRIC `gr-gigafactory-nevada` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck (werkaanname; spoor niet uitgesloten) | `gr-riverside-fabriek` → `gr-gigafactory-nevada` | I-24 W (Murfreesboro, Nashville) → I-40 W (Memphis, Little Rock, OKC, Amarillo, Albuquerque, Flagstaff, Kingman) → US-93 (Hoover Dam Bypass) → I-11/US-95 N (Las Vegas, Beatty, Goldfield, Tonopah, Mina, Schurz) → US-95A (Silver Springs, Fernley) → I-80 W → USA Parkway | OSRM-wegafstand 3.807 [7] (router over OSM, 16 via-punten; zonder via-punten 3.744 I-40-variant, 3.644 via I-80/Kansas City); geen gepubliceerde wegkm; hemelsbreed 3.041. ±15%-toets = indicatie (zelfde OSM-bron) | maak_stroombeen_weg (twee scans, §4) | nee — *aannemelijk: één bron; bron noemt U.S.-fabrieken; volume nul tot H2 2027* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-riverside-fabriek` | verwerkingsknoop / laadplek | NOVONIX Riverside, 1029 W 19th St / Riverfront Pkwy, Chattanooga TN | 35.0388, -85.3243 | [1][2][10][12] hergebruik `grafiet-lakecharles-desoto.md` §3 en `w-novonix-riverside` (grafiet-sitelaag) | bron-gelegd (z15 gezien in `sat-grafiet-novonix-nevada-riverside.png`: wit fabrieksdak langs de oostoever van de Tennessee-bocht, kruis op het zuideinde van de hal, I-24-knooppunten ~1 km ZO; dock niet apart te zien, site-niveau) |
| `gr-gigafactory-nevada` | fabriek / losplek (fase D) | Tesla Gigafactory 1 met Panasonic Energy Nevada, Tahoe-Reno Industrial Center, Storey County (1 Electric Ave) | 39.5404, -119.4390 (letterlijk 39.5403926, -119.4390524) | [5][11] hergebruik `lithium-silverpeak-mccarran.md` §3 (`li-gigafactory-fabriek`) | bron-gelegd (z15 gezien in `sat-grafiet-novonix-nevada-tric.png`: langgerekte fabriek met zonnepanelendak, grote parkeer- en vrachtterreinen, omringd door TRIC-loodsen in kale heuvels; welk deel Panasonic is, niet te zien) |

## 4 · Via-punten (b1; lat, lon, óp de rijbaan; uit de haalbaarheidstoets [13], afgeleid van de kortste route en gesnapt tegen OSRM [8])
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | I-24 tussen Smyrna en Murfreesboro | 35.8803, -86.4826 | I-24 naar Nashville i.p.v. I-75 → Knoxville → I-40 (gedeeld ~184 km met `grafiet-lakecharles-desoto` b2) |
| b1 | 2 | I-40 W van Nashville (Dickson) | 36.0257, -87.2788 | I-40 W naar Memphis i.p.v. I-24 NW → Paducah → I-57/I-64 (de De Soto-corridor) |
| b1 | 3 | I-40 bij Memphis, vóór de Mississippi-oversteek | 35.1612, -90.0201 | I-40 naar Arkansas i.p.v. I-55/I-155 |
| b1 | 4 | I-40 (Crosstown) Oklahoma City | 35.4608, -97.5705 | I-40 W door OKC i.p.v. I-44 → Wichita Falls |
| b1 | 5 | Amarillo | 35.2100, -101.8700 | I-40 Texas panhandle i.p.v. I-27/I-70-route naar Denver; ⚠ ligt op een stadsstraat 1,7 km N van de I-40, zie §7 |
| b1 | 6 | I-40 Albuquerque | 35.0850, -106.6500 | I-40 W i.p.v. I-25 N → Denver; splitspunt voor twee wegscans |
| b1 | 7 | I-40 Flagstaff | 35.2000, -111.6000 | I-40 W naar de Colorado i.p.v. I-17 → Phoenix |
| b1 | 8 | Kingman (I-40 × US-93) | 35.2020, -114.0831 | US-93 N naar Hoover Dam i.p.v. I-40 → Needles → I-15 Barstow/Las Vegas |
| b1 | 9 | Hoover Dam Bypass (Colorado-oversteek) | 36.0114, -114.7390 | enige oversteek op deze corridor; dry-run gaf hier "geen wegpad" bij venster 40 km → `vensterKm` ruimer of `corridorKlassen` (§9-noot) |
| b1 | 10 | US-95 N van Las Vegas (Veterans Memorial Hwy) | 36.3302, -115.3147 | US-95 N i.p.v. NV-160 → Pahrump → NV-373 |
| b1 | 11 | US-95 N van Beatty | 36.9836, -116.7244 | doorrijden op US-95 i.p.v. US-6 via Ely/I-15 |
| b1 | 12 | Goldfield (US-95) | 37.7083, -117.2336 | doorgaande US-95, geen alternatief; gedeeld met `lithium-silverpeak-mccarran` |
| b1 | 13 | Tonopah (US-6/US-95) | 38.0680, -117.2300 | US-95 N i.p.v. US-6 W → Bishop (Californië); gedeeld met `lithium-silverpeak-mccarran` |
| b1 | 14 | Mina (US-95/SR-359) | 38.3922, -118.1086 | vervolg US-95 langs Walker Lake (`lithium-silverpeak-mccarran` via 2) |
| b1 | 15 | Schurz (US-95) | 38.9380, -118.8150 | US-95 N naar Fallon/Silver Springs i.p.v. NV-208 → Yerington |
| b1 | 16 | Fernley (US-95A × I-80) | 39.6000, -119.2200 | I-80 W naar de USA Parkway-afrit i.p.v. US-50 → Carson City |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Riverside, Chattanooga | NOVONIX Anode Materials LLC | naaldcokes → synthetisch AAM (grafitisatie) | nameplate 20 kt AAM/j (doel); 2026 monsters, massaproductie H2 2027, volle capaciteit sept 2031 | [2][3][4] |
| Gigafactory Nevada, TRIC | Tesla (eigenaar), Panasonic Energy (celproductie) | AAM → 2170-cellen | niet gepubliceerd voor het AAM-aandeel | [1][5] |

## 6 · Stoppunt
De brief stopt op het terreinanker van de Gigafactory: dat is het enige Nevada-punt dat al bron-gelegd is (`lithium-silverpeak-mccarran`);
fase E (cellen → Tesla-voertuigen en energieopslag op hetzelfde terrein) vervalt, want geen bron noemt een vervolgbestemming van déze AAM.

## 7 · Open punten
- **Bestemming Nevada niet gebrond.** Het persbericht van 2024-02-09 zegt alleen "Panasonic Energy's North American facilities / U.S. plants" [1]; "Nevada" en "Kansas" komen niet voor, noch in dat bericht (0 treffers) noch in de 20-F FY2025 (0 treffers) [3]. Nevada volgt enkel uit: Panasonic heeft twee Amerikaanse celfabrieken (Nevada en De Soto, Kansas). De regel "contract zegt Nevada and Kansas" in `grafiet-lakecharles-desoto.md` §1/§7 is dus niet te herleiden en is in déze brief geschrapt (fout in andermans brief, niet aangeraakt).
- **Modaliteit en vervoerder niet gebrond** (werkaanname truck): ~3.800 km per truck voor een lading van enkele kt is commercieel onwaarschijnlijk; spoor (BNSF/UP) kan, maar is niet gebrond en niet getekend. Geen gepubliceerde wegkm; de ±15%-toets loopt tegen OSRM/OSM.
- **Volume nul tot H2 2027**; going-concern-voorbehoud en ramp-up naar 2031 [3][4]; Nevada-aandeel van de ≥10 kt onbekend.
- **Via-punt 5 (Amarillo)** ligt op een stadsstraat (S Alabama St, OSRM-snap 8 m), de I-40 ligt 1,7 km zuidelijker (35.1948, -101.8699). Geeft de scan een snap > 1 km of een lus, vervang dan door 35.1948, -101.8699. Punt 13 (Tonopah) ligt in het dorp aan de doorgaande US-95.
- **Last mile TRIC:** het lithium-profiel (zelfde eindanker) kreeg 5,86 km last mile over kleine wegklassen met verruimde `eindKlassen` (track/service/unclassified), zonder "geen wegpad". Pas stippel "last mile (geen net op deze korrel)" alleen als dat hier faalt.
- Riverside: laaddock niet aangewezen (site-niveau), kop op privé-terreinwegen → `eindToegangPrivaat`.

## 8 · Bronnen
[1] NOVONIX, Form 6-K ex-99.1, 2024-02-09 (identiek aan het IR-persbericht van 2024-02-08, dat bij ophalen 403 gaf): ≥10.000 t AAM 2025–2028 uit Riverside voor "Panasonic Energy's North American facilities / U.S. plants"; geen Nevada/Kansas. https://www.sec.gov/Archives/edgar/data/1859795/000095017024013060/nvx-ex99_1.htm
[2] NOVONIX Limited, Form 20-F FY2025: offtake Panasonic Energy en PowerCo; massaproductie voor Panasonic H2 2027; Riverside tot 20.000 tpa; 0 treffers voor "Nevada" en "Kansas". https://www.sec.gov/Archives/edgar/data/1859795/000119312526072814/nvx-20251231.htm
[3] NOVONIX 20-F FY2025, risicofactoren (zelfde document als [2]): volumeverplichtingen onder de Panasonic- en PowerCo-offtake hangen af van productkwalificatie; going-concern-voorbehoud en kapitaalbehoud ook genoemd in [4].
[4] WTVC NewsChannel 9, 2026-09-01: volle capaciteit sept 2031 (was dec 2027), massaproductie Panasonic H2 2027, C-monster geleverd, 17,5 acre niet gekocht. https://newschannel9.com/news/local/novonix-backs-off-land-purchase-next-to-chattanooga-plant-slows-production-ramp-up-riverside-synthetic-graphite-panasonic-battery-materials-175-acres
[5] Wikipedia (en), "Gigafactory Nevada": TRIC, Storey County; Panasonic leidt de celproductie (basisovereenkomst 2014, ~US$1,6 mld). https://en.wikipedia.org/wiki/Gigafactory_Nevada
[6] Wikipedia (en), "Interstate 40": I-40 loopt door Tennessee, Arkansas, Oklahoma, Texas, New Mexico en Arizona via Memphis, Little Rock, OKC, Amarillo, Albuquerque en Flagstaff. https://en.wikipedia.org/wiki/Interstate_40
[7] OSRM (router.project-osrm.org, OSM), 2026-10-30: Riverside → TRIC via de 16 via-punten 3.807,5 km / 42,9 u; haalbaarheidstoets: 3.644 (I-80) en 3.744 km (I-40-corridor); tool-dry-run 3.827,8 km (+2,2%).
[8] OSRM `nearest`, 2026-10-30: snap van de 16 via-punten 1–122 m; punt 5 op S Alabama St (Amarillo), 9 op Hoover Dam Bypass, 10 op Veterans Memorial Hwy.
[9] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-grafiet-novonix-nevada-riverside.png` (z15), `sat-grafiet-novonix-nevada-tric.png` (z15).
[10] `v2/design/routebrieven/grafiet-lakecharles-desoto.md` — Riverside-anker 35.0388, -85.3243 (z15) en I-24-corridor Chattanooga–Nashville (b2).
[11] `v2/design/routebrieven/lithium-silverpeak-mccarran.md` — Gigafactory-anker 39.5403926, -119.4390524 (OSM "Tesla Gigafactory 1", z15) en US-95/US-95A-corridor; profiel `lithium-silverpeak-mccarran-silverpeak-gigafactory`.
[12] `v2/design/grafiet-sitelaag.json` — site `w-novonix-riverside` (bron-gelegd).
[13] Haalbaarheidstoets M31 golf 16 (orkestrator-invoer, 2026-10-30): bindende aanpassing, 16 via-punten getest, overlap 4,8% met lakecharles-desoto en 5,2% met lithium-silverpeak-mccarran.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)

**Stroom `grafiet-novonix-nevada`** → `v2/data/stroomroute-grafiet-novonix-nevada.json` (525 KB) — 2 benen, beide truck, doorgetrokken, 0 stippel. **3.830,5 km**, 25.137 punten, 2 markers (`gr-riverside-fabriek` 0,000 km en `gr-gigafactory-nevada` 0,004 km van de lijn). Eindpunt = id: de lijn eindigt in het TRIC bij Tesla/Panasonic Nevada.
Recept: `bak_stromen.sh` (functie `bak_grafiet_novonix_nevada`), twee wegscans via `wegscan_puur.py` (profielen `grafiet-novonix-nevada-riverside-albuquerque` en `grafiet-novonix-nevada-albuquerque-tric`, splitspunt Albuquerque in beide profielen aanwezig, naad 0,000 km).

| been | km (gemeten) | km (indicatie) | afwijking | punten |
|---|---|---|---|---|
| b1a Riverside → Albuquerque (I-24, I-40 W; us-tennessee/-arkansas/-oklahoma/-texas/-new-mexico) | 2.174,0 | 2.238 | -2,9% | 14.272 |
| b1b Albuquerque → TRIC (I-40 W, US-93, I-11/US-95, US-95A, I-80, USA Parkway; us-new-mexico/-arizona/-nevada) | 1.656,5 | 1.569 | +5,6% | 10.865 |
| totaal | 3.830,5 | OSRM 3.807 | +0,6% | 25.137 |

**Toets.** Geen gepubliceerde wegkm: de indicatie is OSRM 3.807 km (zelfde OSM-bron) naar rato hemelsbreed over de twee scans verdeeld, dus de ±15%-toets is alleen een indicatie. Totaal +0,6% t.o.v. OSRM. Naden 0,000 km. `toets_knikken.py`: 0 omkeringen, 0 terugloop (39 spike-achtige knikken, OSM-ruis op knooppunten en afritten; o.a. Albuquerque-splitspunt, Little Rock/North Little Rock, TRIC). `toets_rechte_benen.py`: geen rechte benen. Contract: versie 2, lonlat, modaliteit truck, elk been > 2 punten. Bestand 525 KB (> 300 KB, truckbenen van 1.650 en 2.170 km); de bol leest de bundel.

**Afwijkingen / ⚠-noten.**
- Via-punt 1 (Smyrna, brief 35.8803, -86.4826) lag 1,1 km ZW van de I-24 en gaf een overschiet-en-terug (1,22 km gesnoeide lus plus rest-spike van 173 graden); verplaatst naar de hoofdrijbaan (35.8906, -86.4826). Via-punt 5 (Amarillo, brief 35.2100, -101.8700) gaf een 4,09 km gesnoeide lus; vervangen door de reserve uit §7 (35.1948, -101.8699, op de I-40). Daarna 0 omkeringen. Geen via-punt bijgeschoven om het getal te halen; de km veranderden nauwelijks (2.174,3 naar 2.174,0).
- Hoover Dam Bypass (via 9) gaf in de wegscan geen "geen wegpad": venster 40 km volstond, snap 0,00 km (de dry-run uit §4 faalde daar wel; oorzaak niet onderzocht). Geen corridorKlassen nodig; alleen `eindKlassen` (track/service/unclassified) voor de TRIC-last mile: 5,86 km over kleine klassen, geen stippel nodig.
- Riverside-kop: geen `eindToegangPrivaat` nodig (first mile 0,66 km over service/unclassified, snap 0,01 km).
- Aannemelijk: één bron (Nevada niet gebrond, modaliteit truck is werkaanname, volume nul tot H2 2027): staat in de beennamen, niet in de lijnstijl.
- Geen haven-aanloop, geen vlucht, geen leiding, geen gedeeld been; het eerste stuk I-24 Chattanooga-Nashville en de US-95-Tonopah-Schurz-delen overlappen geometrisch met `grafiet-lakecharles-desoto` b2 resp. `lithium-silverpeak-mccarran` (4,8% en 5,2%, brief §13) maar zijn niet als kopie overgenomen: de scans beginnen en eindigen op andere ankers.

**Gereedschapslessen.** (1) Een brief-via-punt van OSRM-snap ("snap 1-122 m") kan op een parallelle weg liggen, 1 km van de interstate; de snap 0,00 km in de scan zegt dan niets: controleer de eerste scan op "keerlussen gesnoeid" met lengte > 1 km en verplaats het punt naar de hoofdrijbaan. (2) Een scan over vijf staten (Tennessee tot New Mexico, Texas 711 MB) kost ~8 min op één weg-slot plus reus-slot; de reus-pool was het knelpunt (30 min wachten).

