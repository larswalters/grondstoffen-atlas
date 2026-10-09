# Routebrief (licht) · PGM — Lac des Iles (Canada) → Sudbury → Kristiansand (Noorwegen)

**stroom-id:** `pgm-lacdesiles-kristiansand` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** Pd-rijk Ni-Cu-PGE-concentraat van de Lac des Iles-concentrator (Impala Canada, 100% Implats, ca. 85 km noordwestelijk van Thunder Bay) gaat per **truck** via Hwy 527 en Hwy 11/17 langs de noordoever van Lake Superior naar de Glencore-smelter in Falconbridge (Sudbury), vandaar per **spoor** (CN, Toronto en Montréal) naar de Glencore-terminal in Québec en per **zeeschip** naar Glencore Nikkelverk in Kristiansand, waar het PGM- en goudhoudende materiaal wordt verwerkt. Aannemelijk: één bron voor de huidige route (zie §7).
**Welke as van het verhaal:** de enige grote primaire Pd-mijn van Noord-Amerika en hoe haar concentraat over de Atlantische Glencore-as naar Europese raffinage gaat. **Jaarvolume: 8,7 t 6E/j** (281 koz 6E in concentraat, FY2024 = juli 2023–juni 2024; Pd 242 koz = 7,5 t; koz ÷ 32,15) [1]. Mix: ca. 86% Pd, 7% Pt, 6% Au (3E-reserveverhouding juni 2024) [1]. FY2023: 291 koz.

## 1 · Ketenkaart
```
Lac des Iles-mill `pgm-lacdesiles-mijn` ──(b1 truck · Mine Road → Hwy 527 → Hwy 11/17 → Hwy 17 via Nipigon, Wawa,
    Sault Ste. Marie, Blind River · hemelsbreed 718 km, geen wegkm)──► Glencore Sudbury Smelter `pgm-sudbury-smelter` (Falconbridge)
   ──(b2 spoor · eigen emplacement, stippel · 0,2 km; letterlijke kopie nikkel b0)──► spoornet
   ──(b3 spoor · CN Bala Sub + CN Kingston Sub via MacMillan Yard en Taschereau Yard · 1.293,6 km; letterlijke kopie nikkel b1)──►
   Glencore-terminal Port of Québec `pgm-quebec-kade` (Beauport, aannemelijk)
   ──(b4 zee · Saint-Laurent, Cabotstraat, Noord-Atlantische Oceaan, Skagerrak · 5.452,4 km; letterlijke kopie nikkel b2)──► zeeknoop 4030
   ──(b5 haven-aanloop, stippel · 6,5 km; kopie kobalt b2a)──► Nikkelverk-kade `pgm-nikkelverk-kade` ── stoppunt
```
Gedeeld met `nikkel-sudbury-kristiansand` en `kobalt-sudbury-kristiansand`: alles ná het smelteranker is kopie (ca. 87% van de km); nieuw is alleen b1.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-lacdesiles-mijn` → `pgm-sudbury-smelter` | Mine Road (17 km) → Hwy 527 (95 km) → Hwy 11/17 → Hwy 17 (Nipigon, Wawa, Sault Ste. Marie, Blind River) → Sudbury/Falconbridge; aannemelijk: één bron | hemelsbreed 718 km, geen wegkm; OSRM-indicatie (OSM-routing, geen scheidsrechter) 1.120–1.165 km | maak_stroombeen_weg | nee (mijnweg: zie §7) |
| b2 | A | spoor | `pgm-sudbury-smelter` → spoornet | Falconbridge-emplacement (kopie nikkel b0) | 0,16 gemeten snap [4] | stippel-regel uit `bak_nikkel_sudbury_kristiansand` | ja (net reikt niet tot de smelterdeur) |
| b3 | B | spoor | spoornet → `pgm-quebec-kade` | CN Bala Sub, CN Kingston Sub (kopie nikkel b1) | 465,7 + 541,0 + 286,9 gebakken; geen gepubliceerde lengte [4] | 3 geojson `spoorroute-nikkel-sudbury-kristiansand-*` | nee |
| b4 | C | zee | `pgm-quebec-kade` → zeeknoop Kristiansand | Saint-Laurent → Cabotstraat → Skagerrak (kopie nikkel b2) | 5.452,4 (MARNET; 22 schepen/j gebrond [3]) | MARNET `--been` | nee |
| b5 | C | zee | zeeknoop 4030 → `pgm-nikkelverk-kade` | haven-aanloop Kristiansand (kopie kobalt b2a) | hemelsbreed 6,47, geen gepubliceerde waarde | rechte stippel | ja (kade 6,47 km > 5 km van de zeeknoop) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-lacdesiles-mijn` | mijn + concentrator (kop van het truckbeen) | Lac des Iles-mill, Impala Canada | 49.1625, -89.6192 | [1][2][5][6] | bron-gelegd (z15 en z16 gezien: concentratorgebouw met transportbanden, turquoise tailingsvijver ZO, dagbouwpit NO). Verschoven van het OSM-quarrypunt 49.1602, -89.6259 (~0,55 km ZW, op de rand van het tailingsveld) naar het mill-dak |
| `pgm-sudbury-smelter` | smelter (eind truck, kop spoor) | Glencore Sudbury Smelter (Falconbridge) | 46.5786, -80.7993 | hergebruikt letterlijk `nikkel-sudbury-kristiansand.md` §3 `ni-sudbury-smelter` [4] | bron-gelegd (daar z15 gezien: industrieel complex met schoorsteen, rangeeremplacement) |
| `pgm-quebec-kade` | overslag spoor → zee | Glencore-terminal, Port of Québec, Beauport | 46.8330, -71.2035 | hergebruikt letterlijk `ni-quebec-kade` [3][4] | aannemelijk (steiger in Beauport niet te onderscheiden) |
| `pgm-nikkelverk-kade` | losplek + raffinaderij (stoppunt) | Glencore Nikkelverk, Kolsdalen, Kristiansand | 58.1388, 7.9713 | hergebruikt letterlijk `ni-nikkelverk-kade` [4][7] | bron-gelegd (daar z15 gezien: industrieterrein met pier aan de fjord) |

## 4 · Via-punten (alleen b1; spoorvia-punten MacMillan 43.8119, -79.5111 en Taschereau 45.4686, -73.6861 zijn gekopieerd uit nikkel §4)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Hwy 527 / Hwy 11/17-knoop NO van Thunder Bay | 48.4973, -89.1361 | de mijnweg komt hier op de Trans-Canada, ten oosten van de stad; zonder punt kan een router via Thunder Bay-centrum (+15 km heen en terug). Punt komt uit een OSRM-stap, wordt door de bake gesnapt |
| b1 | 2 | Hwy 11/17-splitsing bij Nipigon, kant Hwy 17 | 49.0204, -88.2437 | echte corridorkeuze: Hwy 17 (Lake Superior-noordoever) tegenover Hwy 11 noordwaarts (Longlac, Cochrane) |
| b1 | 3 | Hwy 17 / Hwy 101-knoop bij Wawa (niet het dorpscentrum) | 47.9708, -84.7845 | pint Hwy 17 aan de Superior-kust; de via-punt uit `u-keylake-blindriver` ligt in Wawa-centrum en is hier bewust niet hergebruikt |
| b1 | 4 | Hwy 17 bij Blind River | 46.1857, -82.9268 | pint Hwy 17 langs Noord-Channel boven Manitoulin (Sault Ste. Marie wordt vanzelf gepasseerd) en tussen Sault en Sudbury |
Sault Ste. Marie krijgt geen via-punt: de Hwy 17-omleiding volgt vanzelf, een punt in de stad dwong op de test een omweg door het centrum af.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Lac des Iles-concentrator | Impala Canada (Implats 100%) | Pd-rijk erts → Ni-Cu-PGE-concentraat, "sold under contract to Glencore" | molen 3,9 Mt erts/j; 281 koz 6E in concentraat FY2024 | [1] |
| Sudbury Smelter (Falconbridge) | Glencore Sudbury INO | concentraat (o.a. LDI via truck, 2010-contract) → Ni-Cu-PGM-matte | matte ca. 140 kt/j naar Québec | [2][3][8] |
| Nikkelverk | Glencore | matte → Ni, Cu, Co en PGM-/goudhoudend materiaal | ca. 92 kt Ni/j (Glencore) | [2][4][7] |

## 6 · Stoppunt
De brief stopt bij Nikkelverk: de 2010-bron zegt dat het PGM- en goudhoudende materiaal daar "further processed" wordt; geen bron noemt een afnemer van het Nikkelverk-edelmetaal, dus geen fase D.

## 7 · Open punten
- **De huidige route is niet bevestigd.** Truck naar Sudbury en verwerking in Kristiansand rusten op een Xstrata-contract van 2010 (twee jaar plus één, einde 2012, 100 à 200 t per partij in 40 t-trucks naar Falconbridge) [2][8]; Implats noemt in 2025 alleen "sold under contract to Glencore" [1]. Glencore heeft Xstrata overgenomen (mijn eigen kennis, niet in de bronnen). Smelter en route blijven aannemelijk: één bron.
- **Geen gepubliceerde wegkm.** b1 heeft alleen hemelsbreed 718 km; de OSRM-indicatie (1.120–1.165 km, routes via Hwy 17) is OSM-routing en dus geen onafhankelijke toets. De ±15%-toets geldt als indicatie.
- **Mijn sluit in zomer 2027** (verlengd van mei 2026) [9]; nu nog operationeel.
- **Mine Road (17 km vanaf Hwy 527)**: OSM-wegklasse niet bevestigd (Overpass viel uit). Is het een privé-mijnweg buiten de openbare klassen, dan eindigt b1 op de laatste openbare weg met een stippel "last mile (geen net op deze korrel)".
- **Sitelaag-afwijking (alleen melden):** `pgm-sitelaag.json` `w-lac-des-iles` staat op 49.28, -89.6, ongeveer 13 km ten noorden van het gelegde mill-anker (49.1625, -89.6192), en is niet satelliet-bevestigd.
- Welke steiger in Beauport Glencore's terminal is, en welke spoorexploitant: zie nikkelbrief §7. Raglan-vertakking niet getekend.
- Het PGM-aandeel in het Nikkelverk-eindproduct en wat er daarna mee gebeurt staat in geen bron; geen fase D of E.

## 8 · Bronnen
[1] Implats, Impala Canada fact sheet 2025 (FY2024: 281 koz 6E in concentraat, Pd 242 koz, Pt 19 koz; "currently sold under contract to Glencore"; 3E-verhouding Pd 86,5%/Pt 7,2%/Au 6,3%). https://implats.co.za/pdf/fact-sheets/2025/fact-sheet-impala-canada.pdf
[2] North American Palladium, prospectus-supplement (SEC, 2010): concentraat per truck naar Xstrata Sudbury, PGM-/goudmateriaal verder naar Kristiansand, contract 2 jaar + 1. https://www.sec.gov/Archives/edgar/data/0000887701/000104746910004238/a2198286zsuppl.htm
[3] Glencore Canada, "Port facilities": ca. 22 schepen/j Québec → Kristiansand; matte per spoor van de Sudbury Smelter. https://www.glencore.ca/en/sudburyino/what-we-do/port-facilities
[4] `v2/design/routebrieven/nikkel-sudbury-kristiansand.md` (§2-§4, §9) en `kobalt-sudbury-kristiansand.md` (b2a); `bak_nikkel_sudbury_kristiansand` en `bak_kobalt_sudbury_kristiansand` in `v2/tools/bak_stromen.sh`.
[5] Impala Canada fact sheet 2024 (FY2023: 291 koz 6E; mine ten noorden van Thunder Bay, underground en dagbouw plus concentrator). https://implats.co.za/pdf/fact-sheets/2024/fact-sheet-impala-canada.pdf
[6] Wikipedia, "Lac des Îles igneous complex" (49.1667, -89.6, regio-aanduiding, niet het anker). https://en.wikipedia.org/wiki/Lac_des_%C3%8Eles_igneous_complex
[7] Nikkelverk, "At a glance". https://www.nikkelverk.no/en/who-we-are/at-a-glance
[8] North American Palladium, jaarinformatieformulier FY2010 (SEC 40-F, ex-1.1): offtake met Xstrata, smelten in Falconbridge, raffineren in Nikkelverk, trucks 40 t, contract tot 2012. https://www.sec.gov/Archives/edgar/data/0000887701/000114420411019323/v215932_ex1-1.htm
[9] Kenora Online, mijn verlengd tot zomer 2027. https://yourkenora.ca/?p=457253
[10] OSRM (router.project-osrm.org, OSM-routing, indicatie): mijn → Falconbridge 1.120–1.164 km via Hwy 527, 11/17, 17.
[11] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-pgm-lacdesiles-kristiansand-mijn.png` (z15), `-mijn-z16.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Uitvoer:** `v2/data/stroomroute-pgm-lacdesiles-kristiansand.json` (270 KB, versie 2, lonlat) · totaal 7.890,3 km · 7 benen (2 stippel) · 6 markers · recept `bak_pgm_lacdesiles_kristiansand` in `v2/tools/bak_stromen.sh`, profiel `pgm-lacdesiles-kristiansand-mijn-smelter` in `maak_stroombeen_weg.py`. Registerregel: sleutel `pgm-lk`.

| # | modaliteit | km gebakken | brief | naad | stippel |
|---|---|---|---|---|---|
| 1 | truck Lac des Iles-mill → Sudbury Smelter | 1.137,6 | indicatie 1.150 (OSRM, geen wegkm): -1,1% | 0 | nee |
| 2 | spoor Falconbridge-emplacement | 0,2 | 0,16 | 0 | ja (net reikt niet tot de smelterdeur), letterlijke kopie |
| 3-5 | spoor Sudbury → MacMillan → Taschereau → Québec | 465,7 + 541,0 + 286,9 | 1.293,6 gebakken (nikkel) | 0 | nee, letterlijke kopie van 3 geojson |
| 6 | zee Québec-kade → Nikkelverk-kade | 5.452,4 | 5.452,4 MARNET | 1,51 (Québec-snap 1,6 km, zoals nikkel) | nee, letterlijke kopie van de beenregel |
| 7 | zee haven-aanloop zeeknoop 4030 → kade | 6,5 | 6,47 hemelsbreed | 0 | ja (rechte stippel, kopie kobalt) |

**Recept b1:** `wegscan_puur.py --profiel pgm-lacdesiles-kristiansand-mijn-smelter` (extract canada 6,4 GB, 8 min, weg- en reus-slot); refs 527, 11, 17, Trans-Canada Highway; vensterKm 75; corridorKlassen tertiary + unclassified; eindToegangPrivaat. Snaps 0,09 km (mill) en 0,05 km (smelter), alle vier via-punten 0,00 km. Eerste 17 km vanaf de mill lopen over kleine klassen (first mile 41,55 km totaal over residential/service/unclassified), dus de Mine Road zit in het OSM-net en hoeft geen stippel last mile. Lijn passeert Nipigon (0,1 km), Wawa (1,5 km), Sault Ste. Marie (2,2 km); Thunder Bay-centrum op 15,5 km, Sudbury-centrum op 6,1 km (geen centrumomweg).
**⚠ Via-punt 1 verplaatst:** het brief-punt 48.4973, -89.1361 lag 45 m naast de weg en gaf een 180-graden-spike van 90 m. Vervangen door 48.5002, -89.1310 (Hwy 11/17, 0,5 km ONO van de 527-knoop). Km veranderde niet noemenswaardig (1.137,6); toets_knikken: 0 omkeringen in b1.
**Toets:** `toets_knikken.py`: b1 15 knikken, geen terugloop (alleen spikes op ankers, 13-74 m); de twee TERUGLOOP-bevindingen zitten in de gekopieerde spoorbenen (MacMillan Yard 43.6673, -79.4652 en 43.8263, -79.5153, bekend uit de nikkelbrief). `toets_rechte_benen.py`: alleen de haven-aanloop (6,5 km, stippel met reden). Markers 0,0 tot 0,12 km van hun lijn. `json.load` ok, 2 / lonlat, modaliteiten {truck, spoor, zee}.
**Toelichting stippels:** b2 en b7 zijn letterlijke kopieen van nikkel respectievelijk kobalt. Er is geen lucht-, leiding- of binnenvaartbeen.
**Lessen / open:** (1) de Xstrata-route uit 2010 blijft aannemelijk, niet bevestigd. (2) Wegkm is OSM-gemeten, geen bedrijfsopgave: de -1,1% is dus geen onafhankelijke toets. (3) `pgm-sitelaag` `w-lac-des-iles` (49.28, -89.6) staat circa 13 km boven het mill-anker: centraal gelijktrekken. (4) Een via-punt dat uit een OSRM-stap komt moet worden getoetst op ligging op de weg (45 m ernaast gaf een spike).
