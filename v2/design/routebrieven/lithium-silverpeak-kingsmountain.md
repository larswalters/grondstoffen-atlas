# Routebrief (licht) · Lithium · Silver Peak → I-40 → Kings Mountain (VS)

**stroom-id:** `lithium-silverpeak-kingsmountain` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) ·
**status:** gebakken
**Keten in één zin:** lithiumcarbonaat uit Albemarle's Silver Peak-brineplant (Clayton Valley, Nevada) gaat per truck
(aannemelijk: één bron voor de bestemming, geen bron voor de vervoerswijze) ruim 4.000 km dwars door de VS (US-6/US-95/US-93
naar Kingman, I-40 oost via Albuquerque, Oklahoma City, Memphis en Knoxville, dan I-26/US-74) naar de Albemarle
conversiefabriek in Kings Mountain (Cleveland County, North Carolina).
**Welke as van het verhaal:** de langste binnenlandse lithiumketen van de atlas: de Amerikaanse brine-mijn voedt de
Amerikaanse conversiefabriek aan de andere kant van het land. Volume klein: ≈5 kt LCE/j Silver Peak (v1/sitelaag,
Albemarle-fabrieksinformatie [5]); Kings Mountain verwerkt "ongeveer 5.000 t lithiumverbindingen per jaar" (Albemarle, 2024-09 [1]);
het aandeel Silver Peak daarin is niet gepubliceerd; ook La Negra (Chili) levert carbonaat aan dezelfde fabriek [1].

## 1 · Ketenkaart
```
Silver Peak-plant `li-silverpeak-plant` ──(b1 truck · NV-265 → US-6/US-95 Tonopah → US-95 zuid (Las Vegas) → US-93 (Hoover-brug)
→ I-40 Kingman → Albuquerque → Oklahoma City → Memphis → Knoxville → Asheville → I-26/US-74 · hemelsbreed 3.230 km, geen wegkm ·
aannemelijk: één bron)──► Kings Mountain-plant `li-kingsmountain-plant` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (lithiumcarbonaat; aannemelijk: [1] noemt de herkomst Silver Peak, niet de vervoerswijze) | `li-silverpeak-plant` → `li-kingsmountain-plant` | NV-265 → US-6/US-95 (Tonopah) → US-95 zuid (Beatty, Las Vegas) → US-93 (Hoover Dam Bypass, Kingman) → I-40 oost (AZ, NM, TX, OK, AR, TN) → I-40 Asheville → I-26 → US-74 | **hemelsbreed 3.230 km, geen wegkm** (via-polyline 3.472 km; eigen schatting ≈4.000 km: I-40 Kingman–Asheville ≈3.160 km uit Wikipedia-staatlengtes [9] plus NV-deel ≈660 en NC-deel ≈210 km, geen bedrijfsopgave); ±15%-toets alleen indicatie | maak_stroombeen_weg (8 extracts) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-silverpeak-plant` | brineplant / laadplek | Albemarle Silver Peak, Clayton Valley, Esmeralda County | 37.7693, -117.5768 | [2][3][5] hergebruikt letterlijk uit `lithium-silverpeak-mccarran.md` (sitelaag `w-li-silverpeak`) | **bron-gelegd** (overgenomen, niet opnieuw gecheckt; z15 daar: kruis midden op het verdampingsvijverveld) |
| `li-kingsmountain-plant` | conversiefabriek / losplek | Albemarle Kings Mountain conversion plant, Kings Mountain, Cleveland County NC | 35.2170, -81.3531 | [1][6][10] Nominatim-adres 348 Holiday Inn Dr = 35.2211,-81.3402 (1,2 km oost); plant ten zuidwesten van de oude groeve; zelfde anker als `lithium-lanegra-kingsmountain` (parallelle golf 16-brief) | **aannemelijk** (z16 gezien: cluster witte hallen, tanks en parkeerterreinen met toegangswegen, de oude groeve met kale wand 0,6 km noordoost, groen bekken noordwest; geen bordje, dus geen bewijs welke hal de conversielijn is [7]); OSM: I-85/US-29 op 0,55 km, het sitelaag-mijnpunt `w-li-kingsmountain` (35.2270,-81.3520) ligt 1,1 km noordnoordoost |

## 4 · Via-punten (b1, alle op trunk of motorway, gemeten op OSM; nooit een stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Tonopah, US-6/US-95 | 38.0754, -117.2433 | vanaf NV-265 oostwaarts over US-6 naar US-95 zuid i.p.v. de noordroute (Mina/Fernley, andere stroom); [10] |
| b1 | 2 | Las Vegas, US-95/I-11 (noordwest) | 36.2047, -115.2444 | pint US-95 door Las Vegas i.p.v. NV-160 via Pahrump of zuidroute via Searchlight naar Needles |
| b1 | 3 | Hoover Dam Bypass (US-93) | 36.0114, -114.7390 | pint de Colorado-oversteek US-93 i.p.v. I-15/I-40 via Barstow |
| b1 | 4 | Kingman, I-40/US-93 | 35.2175, -113.9993 | begin van de I-40-corridor oost |
| b1 | 5 | Albuquerque, I-40 | 35.1059, -106.6469 | pint I-40 i.p.v. I-25/Colorado-omweg (Colorado-extract ontbreekt) |
| b1 | 6 | Oklahoma City, I-40 | 35.4564, -97.5128 | pint I-40 i.p.v. een Tulsa/I-44-route |
| b1 | 7 | Memphis, I-40 (Mississippi-brug) | 35.1530, -90.0483 | pint de Mississippi-oversteek op I-40 (zelfde punt-klasse als `ree-georgia-whitemesa`) |
| b1 | 8 | Knoxville, I-40/I-75 | 35.9602, -83.9734 | pint I-40 oost i.p.v. I-81 via Virginia of I-75 zuid |
| b1 | 9 | Asheville (west), I-40 | 35.5549, -82.6148 | pint de I-40-corridor door de Appalachen tot de I-26-splitsing |
| b1 | 10 | Columbus NC, I-26 | 35.2262, -82.1983 | pint I-26/US-74 naar Kings Mountain i.p.v. I-40 oost via Hickory/Charlotte |

Tien punten (boven de 3-8 van de kaart) omdat dit één landbeen van ruim 4.000 km is; elk punt pint een echte keuze. Hemelsbreed per stuk (km): 45 · 273 · 50 ·
111 · 668 · 830 · 678 · 557 · 131 · 53 · 77 (som 3.472).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Silver Peak-plant | Albemarle | brine → technisch carbonaat + hydroxide | ≈5 kt LCE/j | [2][3][5] |
| Kings Mountain-fabriek | Albemarle | carbonaat (Silver Peak, La Negra) → hydroxide, lithiummetaal, legeringspoeder | ≈5.000 t verbindingen/j | [1] |

## 6 · Stoppunt
De brief stopt aan de conversiefabriek: het is de enige afnemer die één bron met naam noemt [1]; welke klant het hydroxide of lithiummetaal daarna krijgt is
niet publiek gedocumenteerd, dus fase D en E vervallen.

## 7 · Open punten
- **Vervoerswijze onbevestigd:** [1] noemt Silver Peak als herkomst van het carbonaat maar niet hoe het reist; spoor is even goed mogelijk (geen VS-spoornet in raw1op1), truck is de aanname en staat daarom als "aannemelijk: één bron" in de beennaam.
- **Geen wegkilometer gepubliceerd:** alleen hemelsbreed 3.230 km (via-polyline 3.472) en de eigen schatting ≈4.000 km; de ±15%-toets is indicatie.
- **Aandeel Silver Peak in Kings Mountain onbekend;** de 5 kt zijn de totale vestigingscapaciteit, niet de leverstroom. Peiljaar capaciteit: 2024.
- **Bestand verwacht groot** (circa 25.000 punten, ≥500 KB, zoals eerdere lange truckbenen): centraal als noot, niet herbakken. Texas-scan duurt ≈4-5 min.
- **Eind-anker aannemelijk:** het exacte gebouw van de conversielijn niet vastgesteld (z16 toont meerdere hallen); fout kleiner dan 1 km.
- **Hurricane Helene (2024):** de I-40-kloof bij Pigeon River is gesloten geweest; het OSM-net kan een tijdelijke afsluiting dragen; de bak telt de weg, niet het verkeer.
- **Overlap:** eerste ca. 60 km (NV-265 naar US-6) valt samen met `lithium-silverpeak-mccarran`, I-40 Memphis tot Albuquerque (ca. 1.600 km) met `ree-georgia-whitemesa`; andere grondstof en eindpunt, dus geen duplicaat en geen kopie.

## 8 · Bronnen
[1] Albemarle, "Kings Mountain: All the Elements of a Lithium Ecosystem", 2024-09-16: conversiefabriek verwerkt carbonaat uit Silver Peak en La Negra, ≈5.000 t/j. https://www.albemarle.com/us/en/news/kings-mountain-all-elements-lithium-ecosystem
[2] Albemarle, locaties Noord-Amerika (Nevada): Silver Peak actief, technisch carbonaat + hydroxide. https://albemarle.com/locations/north-america/nevada
[3] Albemarle Form 10-K FY2019: brine wordt in Silver Peak tot carbonaat verwerkt; Kings Mountain NC = lithiumproductie. https://www.sec.gov/Archives/edgar/data/915913/000091591320000040/a1231201910-kdocument.htm
[4] Orchestrator-invoer: ketenontwerp en haalbaarheidstoets M31 golf 16 (2026-10-30; geen vervoerswijzebron, wegschatting 3.900-4.100 km).
[5] `v2/design/lithium-sitelaag.json`: `w-li-silverpeak` (5 kt LCE/j, bron-gelegd) en `w-li-kingsmountain`; `data/lithium.js` `li-silver-peak`.
[6] OpenStreetMap (ODbL) via Nominatim: "348 Holiday Inn Drive, Kings Mountain" = 35.2211, -81.3402 (way 16485720). https://nominatim.openstreetmap.org
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15/z16, 2026-10-30): `v2/build-cache/satcheck/sat-lithium-silverpeak-kingsmountain-plant.png`, `sat-lithium-silverpeak-kingsmountain-plant16.png`; Silver Peak: `sat-lithium-silverpeak-mccarran-silverpeak.png`.
[8] `v2/design/routebrieven/lithium-silverpeak-mccarran.md`: anker Silver Peak, NV-265-start, `corridorKlassen` tertiary.
[9] Wikipedia (en), "Interstate 40": lengte 2.556,6 mi, per staat AZ 359,5 · NM 373,5 · TX 177,1 · OK 331,7 · AR 284,7 · TN 455,3 · NC 420,2 mi. https://en.wikipedia.org/wiki/Interstate_40
[10] Eigen scan van de Geofabrik-extracts us-nevada, -arizona, -new-mexico, -oklahoma, -tennessee, -north-carolina (wegscan_puur-lezer, motorway/trunk/primary): via-punten zijn OSM-vertices op de genoemde ref (afstand tot de geschatte plek 0,0-3,2 km; Asheville 5 km noord van de I-26-splitsing, bewust op I-40).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)

**Stroom `lithium-silverpeak-kingsmountain`** → `v2/data/stroomroute-lithium-silverpeak-kingsmountain.json` — **1 been,
3.927,6 km**, 25.586 punten, 2 markers, bestand 531,0 KB. truck 3.927,6 km. Recept: `bak_stromen.sh` (functie
`bak_lithium_silverpeak_kingsmountain`), tussenbestand `v2/build-cache/ais/graaf/lithium-silverpeak-kingsmountain-weg-silverpeak-kingsmountain.geojson`.

**b1 (truck, nieuw profiel `lithium-silverpeak-kingsmountain-silverpeak-kingsmountain`, 8 extracts: us-nevada, -arizona, -new-mexico, -texas, -oklahoma, -arkansas, -tennessee, -north-carolina):**
`wegscan_puur.py` (Texas-scan 393 s, totaal ca. 23 min), 12 via-punten (ankers plus de 10 uit §4), refs US 6, US 95, US 93, I 40, I 26, US 74
(en NV 265 als zachte voorkeur, toegevoegd t.o.v. de brief-aanwijzing), vensterKm 100, corridorKlassen tertiary/unclassified (NV-265),
eindKlassen residential/service/tertiary/unclassified/track, eindToegangPrivaat. Alle via-snaps 0,00-0,11 km (ruim onder de 5 km-norm);
17 keerlussen gesnoeid (3.934,0 → 3.927,4 km). First mile 38,15 km over kleine klassen (tertiary, track, unclassified), last mile 2,36 km.
Segmenten (km, tegen hemelsbreed uit §4): 91,3 (45) · 327,9 (273) · 71,5 (50) · 119,9 (111) · 745,4 (668) · 871,5 (830) · 749,1 (678) ·
623,1 (557) · 182,1 (131) · 60,4 (53) · 91,8 (77); geen segment met een omweg die op een misplaatst via-punt wijst.

**Lengtetoets (indicatie, geen norm):** de brief geeft geen echte wegkm ("hemelsbreed 3.230 km, geen wegkm"; eigen schatting ca. 4.000 km).
Gemeten 3.927,6 km = −1,8% tegen de schatting, omwegfactor 1,22 tegen hemelsbreed (via-polyline 3.472 km: 1,13). Plausibel; de ±15%-toets
is hier alleen indicatie.

**Geen haven-aanloop, geen stippel, geen kopie, geen vlucht:** enige volledig binnenlandse truckketen; geen kade in de keten, de
site-ankers liggen op de weg (0,11 en 0,09 km anker-verbindingen). "aannemelijk: één bron" staat in de beennaam, het been is doorgetrokken.
Fase D/E vervallen (§6).

**Toets:** naad 0,00 km (enig been). Markers 0,000 km van de lijn (bron-gelegd Silver Peak, aannemelijk Kings Mountain).
`toets_knikken.py`: 14 knikken ≥60°, 2 omkeringen ≥150° (Silver Peak toegangsweg 150,9° echte bocht; Asheville 155,9° TERUGLOOP),
`toets_rechte_benen.py --min-km 5`: geen regel voor deze stroom. json: versie 2, punt_formaat lonlat, modaliteiten {truck}, been ≥2 punten.

**Bevindingen:**
- **Terugloop bij Asheville (35,5564, −82,6089):** een spijker van ca. 0,1 km bij het via-punt "Asheville west I-40" (de snap landt op een
  oprit/rijbaanwissel van de dubbele rijbaan; de keerlus-snoei nam al 0,12 km weg). Niet bijgeschoven en niet herbakken; procesgat.
- **Bestand 531 KB / 25.586 punten**, boven de ~300 KB-richtwaarde (verwacht, §7): centraal als noot; de bol leest de bundel (L0/L1).
- Overlap met `lithium-silverpeak-mccarran` (eerste ca. 60 km) en `ree-georgia-whitemesa` (I-40 Memphis-Albuquerque) is bewust, geen kopie.
- I-40 Pigeon River-kloof (Helene): de route volgt I-40 door de Appalachen op het OSM-net; de bak telt de weg, niet het verkeer.

**Gereedschapslessen:**
- **Een truckbeen van 3.900 km over 8 extracts is met `wegscan_puur.py` in één run haalbaar** (ca. 23 min, Texas 393 s; weg- plus reus-slot nodig voor us-texas).
- **Tien tot twaalf via-punten op de doorgaande I-40/US-95 geven nul via-snaps boven 0,11 km:** de OSM-vertices uit de brief (§8 [10]) werken als via-punt zonder bijschuiven.
- **`nohup … &` na `cd … &&` in één regel draait de hele keten op de achtergrond, ook de `cd`:** eerst `cd`, dan een aparte regel voor de achtergrondrun, anders wijst het logbestand naar het verkeerde pad.
