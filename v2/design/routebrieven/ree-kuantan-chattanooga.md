# Routebrief (licht) · Zeldzame aardmetalen · Kuantan (LAMP) → Savannah → Chattanooga (Verenigde Staten)

**stroom-id:** `ree-kuantan-chattanooga` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** Ceriumcarbonaat van de Lynas Advanced Materials Plant (LAMP) in Gebeng gaat per **truck** naar Westports (Port Klang), per **zeeschip**
(MARNET, via Suez en de Atlantische Oceaan) naar de Garden City Terminal in Savannah en per **truck** (I-16, I-75) naar de Grace-fabriek (4000 N Hawthorne St) in Chattanooga.
**Welke as van het verhaal:** de niet-magneethelft van REE: cerium voor FCC-katalysatoren, via de enige grote niet-Chinese scheiding, naar een Amerikaanse katalysatorfabriek.
Volume: **172 containers / 3.248 t materiaal, meerjarig totaal** (laatste B/L 6 okt 2026: 2 x 20 ft, 32,9 t) [1][2]; geen jaarcijfer, eenheid kt materiaal, geen REO.

## 1 · Ketenkaart
```
LAMP Gebeng `ree-lamp-gebeng` (hergebruikt anker, ree-kuantan-japan.md)
  ──(b1 truck · E8 Pantai Timur → Karak Highway → KL–Klang · 336,5 km getekend, LETTERLIJKE KOPIE van ree-kuantan-japan b1)──►
Westports, Port Klang `ree-kuantan-japan-westport-kade` (hergebruikt anker)
  ──(b2 zee · Malakka → Indische Oceaan → Suez → Gibraltar → Atlantisch · ~19.448 km, MARNET)──► zeeknoop 5004 (32.0331, -80.8353)
  ──(b3 zee, haven-aanloop Savannah-rivier · ~46,7 km over water, stippel: MARNET reikt niet)──►
Garden City Terminal, Georgia Ports Authority `ree-garden-city-kade`
  ──(b4 truck, aannemelijk: één bron · I-16 → Macon → I-75 via Atlanta · OSRM-indicatie 592 km)──►
Grace Davison, Chattanooga `ree-grace-chattanooga`
  ⏹ stoppunt: consignee-adres van de lading
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-lamp-gebeng` → `ree-kuantan-japan-westport-kade` | Lebuhraya Pantai Timur (E8) → Karak Highway → KL–Klang | hemelsbreed 258 km, geen wegkm; getekend 336,5 (kopie, +16% op kaartschatting 290) [11] | KOPIE `ree-kuantan-japan-weg-gebeng-westport.geojson` | nee |
| b2 | B | zee | `ree-kuantan-japan-westport-kade` → zeeknoop 5004 | Malakka, Suez, Atlantisch (MARNET kiest) | geen gepubliceerde km; MARNET-proef 19.448 km [9] | MARNET | Westports 2,3 km van zeeknoop 5375: geen aanloop |
| b3 | B | zee | zeeknoop 5004 → `ree-garden-city-kade` | Savannah-rivier | kade 31,1 km van de zeeknoop (> 5 km); maak_havenaanloop 46,7 km over water [9] | maak_havenaanloop (timeout 300) | ja: stippel, MARNET reikt niet; terugval rechte stippel ~31 km |
| b4 | C | truck | `ree-garden-city-kade` → `ree-grace-chattanooga` | I-16 → Macon → I-75 (Atlanta, Cartersville, Dalton) | hemelsbreed 502 km, geen wegkm; OSRM-indicatie 592 km (OSM-gebaseerd) [6] | maak_stroombeen_weg (`us-georgia`, `us-tennessee`) | nee; site ligt aan het wegennet (0 km last mile) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-lamp-gebeng` | fabriek (start) | Lynas Advanced Materials Plant, Gebeng | 4.0034, 103.3775 | [3] hergebruik `ree-kuantan-japan.md` §3 | bron-gelegd (zie die brief: plantcomplex met procesgebouwen) |
| `ree-kuantan-japan-westport-kade` | overslag truck → zee | Westports Malaysia, Pulau Indah | 2.9498, 101.3076 | hergebruik `ree-kuantan-japan.md` §3 | bron-gelegd (z14 in die brief: kadelijn, containerstapels) |
| `ree-garden-city-kade` | losplek zee / overslag zee → truck | Garden City Terminal, Georgia Ports Authority, Savannah | 32.1292, -81.1449 | [4][10] Nominatim/ haalbaarheidstoets; ImportGenius noemt Savannah als lospoort [1][2] | bron-gelegd (z15 gezien, `sat-ree-kuantan-chattanooga-gct.png`: kruis midden in containerstapels, kadefront met portaalkranen aan de Savannah-rivier; terminal-berth zelf niet aanwijsbaar, site-niveau) |
| `ree-grace-chattanooga` | afnemer / fabriek | Grace Davison, 4000 N Hawthorne St, Chattanooga TN 37406 | 35.0860, -85.2472 | [5] Nominatim way 139888317 (huisnummerpunt, adres bevestigd door [1]) | bron-gelegd (z15 gezien, `sat-ree-kuantan-chattanooga-grace.png`: industriecomplex met hallen en tanks ten zuiden van de Tennessee-rivier, I-75 ~1 km oostelijk; bedrijfsnaam niet op het beeld afleesbaar) |

## 4 · Via-punten (alleen b4; b1 = kopie, geen eigen via-punten)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b4 | 1 | I-16 bij Dublin (Laurens Co) | 32.4854, -82.8987 | houdt de lijn op I-16 i.p.v. US-80/US-280; punt uit de OSRM-geometrie, buiten de stad |
| b4 | 2 | I-16 oost van Macon | 32.8196, -83.5889 | laatste punt op I-16 vóór de I-75-aansluiting |
| b4 | 3 | I-75 bij Forsyth | 33.0417, -83.9355 | I-75 noordwaarts i.p.v. I-475 of US-41 |
| b4 | 4 | I-75 Henry Co (McDonough) | 33.4470, -84.1993 | corridorkeuze Atlanta: I-75 door de stad, niet de oostelijke I-285-ring; niet in het centrum |
| b4 | 5 | I-75 bij Marietta (ten noorden van I-285) | 33.9669, -84.5247 | trekt de lijn dwars door Atlanta over I-75 (Downtown Connector, 33.79, -84.39 niet als via-punt) |
| b4 | 6 | I-75 bij Cartersville | 34.1856, -84.7656 | I-75 noordwaarts i.p.v. US-41 |
| b4 | 7 | I-75 bij Dalton | 34.7716, -85.0012 | laatste doorgaande I-75 vóór Chattanooga, buiten het centrum |

Alle punten komen uit de OSRM-geometrie [6] en liggen dus op de weg. Refs: `I 16`, `I 75`. Geofabrik-regio's: `us-georgia`, `us-tennessee`.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| LAMP Gebeng | Lynas | Mt Weld-concentraat → NdPr-oxide, Ce, LaCe-carbonaat, zware REE | NdPr-nameplate ~10.500 t/j (ree-sitelaag) | [3] |
| Grace Chattanooga | W. R. Grace (Grace Davison) | ceriumcarbonaat → FCC-additieven/intermediates (aannemelijk) | niet gepubliceerd | [1][7][8] |

## 6 · Stoppunt
De brief stopt bij Grace Chattanooga: het is de op de Bill of Lading genoemde consignee ("Grace Davison", Chattanooga, product cerium carbonate) [1][2]. Verdere afzet (raffinaderijen) is niet per lading gebrond. Fase E vervalt. Titel en id beloven Chattanooga; het eindpunt klopt.

## 7 · Open punten
- **Chattanooga is het importadres, niet bewezen als bestemming.** ImportGenius geeft het consignee-adres; Grace-katalysatorfabrieken liggen mogelijk elders [1]. Grace beschrijft Chattanooga als FCC-additieven/intermediates-locatie [7], maar welke zeldzame aarde daar nu verwerkt wordt is niet per bron bevestigd (1970: grote REE-verwerker [8]).
- **Transshipment niet gebronnd:** het B/L noemt Tanjung Pelepas als laadhaven en Port Kelang als plaats van ontvangst [1]; MARNET routeert Westports → Savannah rechtstreeks. Het ontwerp tekent Westports als uitvoerhaven.
- **Terminal in Savannah niet gebronnd:** ImportGenius noemt alleen Savannah; Garden City Terminal (GPA) is de containerterminal van de haven (anker aannemelijk, niet per lading) [4].
- **Zeeroute via Suez/Rode Zee is wat MARNET kiest** (19.448 km); of schepen via de Kaap varen is niet gemodelleerd (zelfde aanname als ree-kuantan-pasadena).
- **b4 niet gebrond als route:** geen gepubliceerde wegkm; I-16/I-75 is de gangbare corridor, spoor (CSX/Norfolk Southern) kan even goed. Km-regel is hemelsbreed + OSRM-indicatie.
- **b1** is kopie van een stroom waar alleen Time.com de truckcorridor noemt [11]; LAMP als begin komt al driemaal voor in de atlas.
- **Geen jaarcijfer:** 3.248 t over meerdere jaren; start- en einddatum van de reeks niet gepubliceerd (gratis samenvatting) [1][2]. De claim "grootste VS-Lynas-klant" is niet onderbouwd en weggelaten.

## 8 · Bronnen
[1] ImportGenius, "Grace Davison" (4000 N Hawthorne St, Chattanooga; Lynas Malaysia 172 containers, 3.248.064 kg; laatste B/L HLCUKUL260748136, 6 okt 2026, Port Kelang → Savannah, laadhaven Tanjung Pelepas), gelezen 2026-10-30. https://www.importgenius.com/importers/grace-davison
[2] ImportGenius, "Lynas Malaysia Sdn Bhd" (top-consignee Grace Davison, top-VS-haven Savannah, cerium carbonate 32.920 kg), gelezen 2026-10-30. https://www.importgenius.com/suppliers/lynas-malaysia-sdn-bhd
[3] Lynas Rare Earths, Kuantan, Malaysia (producten NdPr, Ce, LaCe, zware REE). https://lynasrareearths.com/kuantan-malaysia-2/
[4] Wikipedia, "Port of Savannah" (Garden City Terminal, GPA, 1.345 acre, 2.955 m kade, ~29 km van de oceaan; havencoördinaat 32°07′43″N 81°09′07″W). https://en.wikipedia.org/wiki/Port_of_Savannah
[5] OpenStreetMap (ODbL) via Nominatim: 4000 North Hawthorne Street, Chattanooga, way 139888317, 35.0860075 / -85.2472200. https://nominatim.openstreetmap.org
[6] OSRM demo-router (OSM): Garden City → Grace 592,0 km via I-16 en I-75 (stappen en geometrie voor §4). https://router.project-osrm.org/
[7] Grace, Chattanooga-locatie (4000 N Hawthorne St; FCC-intermediates, FCC-additieven sinds 2003, RANEY-katalysatoren; gelezen via zoekresultaat, pagina gaf een certificaatfout). https://grace.com/about-grace/locations/chattanooga/
[8] USGS Minerals Yearbook 1970 (Grace Davison, Chattanooga als grote REE-verwerker). https://search.library.wisc.edu/digital/ADV7JLBE7QKH6C9C/text/AK2WHMSHZYG4RP8C
[9] Eigen metingen vanuit de repo: MARNET-proef Westports → zeeknoop 5004 (19.448 km, haalbaarheidstoets), zeeknoop 5004 op 31,1 km van de kade, maak_havenaanloop 46,7 km; Westports op 2,3 km van zeeknoop 5375.
[10] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-ree-kuantan-chattanooga-{gct,grace}.png`.
[11] `ree-kuantan-japan.md` (b1-kopie, LAMP- en Westports-anker) en `ree-kuantan-pasadena.md` (zelfde b1-kopie, MARNET-aanname Suez).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)

Recept: `bash v2/tools/bak_stromen.sh ree-kuantan-chattanooga` (functie `bak_ree_kuantan_chattanooga`) → `v2/data/stroomroute-ree-kuantan-chattanooga.json` (216,1 KB, versie 2, `lonlat`, 11.071 punten). Titel: *Zeldzame aardmetalen · LAMP Gebeng → Westports → Savannah → Grace Chattanooga*; het eindpunt klopt met het id.

| # | modaliteit | km | naad naar vorig been | opmerking |
|---|---|---|---|---|
| b1 | truck | 336,5 | — | LETTERLIJKE KOPIE `ree-kuantan-japan-weg-gebeng-westport.geojson` (4.673 punten); geen gepubliceerde wegkm (hemelsbreed 258), dus geen ±15%-norm |
| b2 | zee | 19.448,1 | 2,34 km (Westports-snap op zeeknoop 5375, < 5 km) | MARNET Westports → zeeknoop 5004 (32.0331, -80.8353), via Suez; 2.010 punten |
| b3 | zee, STIPPEL | 46,7 | 0 | haven-aanloop Savannah-rivier, knoop → kade |
| b4 | truck | 588,6 | 0 | profiel `ree-kuantan-chattanooga-gct-grace`, 4.379 punten |

Totaal 20.419,9 km, 4 markers (alle 0,0 km van hun lijn), grootste naad 2,34 km. b4: 588,6 km tegen OSRM-indicatie 592 km (-0,6%), hemelsbreed 502 km; geen gepubliceerde wegkm, dus de toets is een indicatie. Eerste mijl 2,05 km en laatste mijl 2,52 km over kleine klassen (service, unclassified, residential): geen last-mile-been nodig.

**Toelichting stippel (b3).** Garden City Terminal ligt 31,1 km van zeeknoop 5004 (> 5 km): haven-aanloop nodig. `maak_havenaanloop.py` slaagde binnen de timeout (3 min 22 s, cel 0,02 graden, 9 punten, 46,7 km, omwegfactor 1,50); de tool maakte de aanloop kade → knoop, hier OMGEKEERD opgeslagen als `ree-kuantan-chattanooga-aanloop-savannah-rev.geojson` (knoop → kade, anders naad 31 km). **Bevinding:** de 1:10M-kust kent de Savannah-rivier niet; de lijn duikt ten zuiden van Tybee (rond 31.93 N) en het laatste stuk (22 km) is een rechte koorde over land naar de kade (25,6 km telt als "over land", geen landkruising midden op de lijn). Schematisch, blijft stippel; de werkelijke vaargeul ligt tot ~4 km noordelijker. Een betere lijn vraagt een rivierlijn uit OSM (Overpass was onbereikbaar).

**Wegbeen b4.** `wegscan_puur.py`, extracts `us-georgia` (354 MB) en `us-tennessee` (186 MB), 7 via-punten op I-16 en I-75 (alle snap 0,00-0,03 km), refs `I 16`, `I 75`, `vensterKm` 40, `eindToegangPrivaat`. Deelstukken: Savannah → Dublin 182,6 · Dublin → oost Macon 78,6 · → Forsyth 41,9 · → McDonough 52,8 · → Marietta 73,2 · → Cartersville 37,3 · → Dalton 73,7 · → Grace 48,5 km. Geen via-punt in een stadscentrum, geen omweg gemeld. Toets_knikken: 21 knikken, 0 omkeringen, 0 terugloop op b4 (de twee omkeringen zitten in de gekopieerde b1: 160 en 158 graden bij Gebeng en Klang, bestaande stroom).

**Niet getekend / aannames.** Geen lucht, leiding, spoor of fase D/E. "Aannemelijk: één bron" staat in de beennaam van b4: Chattanooga is het consignee-adres (§7). Westports als uitvoerhaven en Suez-routering zijn aannames (B/L noemt Tanjung Pelepas); Kaapvaart niet gemodelleerd.

**Lessen.** (1) `maak_havenaanloop.py` schrijft kade → knoop; staat de aanloop ná het zeebeen in de reisvolgorde, dan moet het geojson worden omgekeerd (naad anders 31 km). (2) De wegscan op twee middelgrote extracts (Georgia + Tennessee) duurde 5 min 43 s. (3) Een gelijktijdige edit van een andere agent in `bak_stromen.sh` gaf aan het eind van een bake een melding `command not found` (exit 127) terwijl het json al was geschreven; een tweede bake gaf exit 0 en een identiek resultaat.
