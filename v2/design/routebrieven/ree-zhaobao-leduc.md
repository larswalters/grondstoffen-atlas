# Routebrief (licht) · zeldzame aardmetalen — Ningbo Zhaobao (Beilun-kade) → Tacoma → Leduc (Canada)

**stroom-id:** `ree-zhaobao-leduc` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** NdFeB-magneten van Ningbo Zhaobao Magnet gaan per containerschip (ONE Maestro 087E) van Ningbo over de Stille Oceaan naar Tacoma en daarna per truck over I-5, de Coquihalla en de Yellowhead naar Interra Energy Services in Leduc (Alberta) — aannemelijk: één bron (invoer-B/L), terminal en landmodaliteit zijn aannames.
**Welke as van het verhaal:** een nieuwe bestemming op de bol: Chinese magneten naar een Canadese oliedienstverlener via een Amerikaanse haven. Volume 0,0165 kt NdFeB/j (2 B/L van 19 pakken à 8.235 kg, 18-07 en 22-08-2026; mogelijk dubbel geteld, dan 0,008 kt); geen jaarcijfer Zhaobao; peiljaar 2026 [1][2]. Fabriekscapaciteit >11 kt NdFeB/j (bedrijfsopgave) [6].

**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** geen fabrieksanker (Haisi Rd niet te geocoderen): de lijn begint op de Beilun-kade; b2 is meteen een rechte stippel (geen `maak_havenaanloop.py`); b3 draagt "aannemelijk: één bron, modaliteit onbekend" in de beennaam. Het stroom-id noemt Leduc en dat is het eindpunt. Nieuw t.o.v. het ontwerp: Tacoma → Leduc loopt langs de Yellowhead (Hwy 5 en 16 via Jasper), de OSRM-corridor; de route via Calgary is niet gemeten.

## 1 · Ketenkaart
```
Beilun CT Phase 2 `ree-beilun-kade` ──(b1 zee · MARNET · ~9.667 km)──► Tacoma-zeeknoop 7801 (47.3011,-122.4766)
  ──(b2 haven-aanloop, stippel · ~5,8 km schematisch)──► Husky Terminal `ree-tacoma-kade`
  ──(b3 truck · I-5 → BC 11 → TCH 1 → Coquihalla BC 5 → Yellowhead 5/16 → Hwy 216 → Hwy 2 · ~1.350 km, aannemelijk)──►
Interra Energy Services, Leduc `ree-leduc-afnemer` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | zee | `ree-beilun-kade` → Tacoma-zeeknoop 7801 | Oost-Chinese Zee → noordelijke Stille Oceaan (ONE Maestro 087E) [1][2] | grootcirkel kade↔knoop 9.299 (hemelsbreed); router ca. 9.667 [11]; geen gepubliceerde zeekm | MARNET | aanloop: nee (Beilun 1,95 km van zeeknoop 5849) |
| b2 | D | zee (haven-aanloop) | zeeknoop 7801 → `ree-tacoma-kade` | Commencement Bay | schematisch ca. 5,8 (hemelsbreed, kade 5,83 km van de knoop [11]) | rechte `--stippel` (ontwerp: geen pad in 280 s van `maak_havenaanloop.py`) | ja — MARNET reikt niet tot de kade (> 5 km, LAR-586) |
| b3 | D | truck (aannemelijk: één bron, modaliteit onbekend) | `ree-tacoma-kade` → `ree-leduc-afnemer` | I-5 → SR 9 → BC 11 → TCH 1 → BC 5 Coquihalla → YH 5 → YH 16 (Jasper) → AB 216 → AB 2 | hemelsbreed 919 km, geen wegkm (OSRM 1.352 km is OSM-afgeleid; indicatie) [9] | maak_stroombeen_weg, profiel `ree-zhaobao-leduc-husky-leduc` (us-washington + canada) | nee (Leduc-last mile 2,8 km over service/tertiary, binnen 12 km-eindklassen) |
Geen luchtbeen: geen bron zegt dat deze lading vliegt; de B/L noemt een container [2]. Geen kopie van een ander been. Trein Tacoma → Alberta is gebruikelijk (Husky heeft on-dock rail [3]) maar niet door een bron voor deze lading genoemd: de lijn tekent truck.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-beilun-kade` | overslag truck → zee (kop, fabrieksanker Zhaobao niet gevonden) | Beilun Container Terminal Phase 2, Ningbo-Zhoushan | 29.9353, 121.8695 | [13] letterlijk uit `ree-yunsheng-longbeach.md` §3 (ook `kobalt-huayou-gunsan`, `ree-baotou-ningbo`) | bron-gelegd (hergebruikt; 1,95 km van zeeknoop 5849); dat Zhaobao via déze terminal gaat is aannemelijk (B/L noemt alleen Ningbo) |
| `ree-tacoma-kade` | overslag zee → truck | Husky Terminal, Port of Tacoma (Commencement Bay) | 47.2733, -122.4110 | [3][4][5][7] OSM way 626041806 | bron-gelegd (z15 gezien: containerterminal met portaalkranen, containerstapels en spoorbundel, schip aan de oostkade; het kruis ligt op het terrein); terminalkeuze aannemelijk (ONE belt Husky, B/L noemt geen terminal) |
| `ree-leduc-afnemer` | losplek / afnemer | Interra Energy Services (EMFTS Leduc), 3301 Allard Ave, Leduc, Alberta | 53.2914, -113.5170 | [1][8] ArcGIS-match score 100 | bron-gelegd (z15 gezien: bedrijventerrein Leduc Business Park, kruis op een perceel met lage hallen en opslagterrein aan een ringweg; geen bedrijfsbord zichtbaar) |
Zeeknoop (geen anker): Tacoma 47.3011, -122.4766 (id 7801), Beilun 29.9478, 121.8837 (id 5849).

## 4 · Via-punten (alleen b3: corridorkeuze; 8 punten op de doorgaande weg, nooit in een stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | I-5 bij Bellingham | 48.7038, -122.4749 | I-5 noordwaarts i.p.v. I-405 of de kust |
| b3 | 2 | Sumas/Abbotsford grens (SR 9 / BC 11) | 49.0020, -122.2651 | grensovergang Sumas i.p.v. Peace Arch of Aldergrove |
| b3 | 3 | Hope, begin BC 5 | 49.3617, -121.3627 | Coquihalla (BC 5) i.p.v. Fraser Canyon (TCH 1) |
| b3 | 4 | Kamloops west (TCH 1 / BC 5) | 50.6662, -120.4417 | Coquihalla-uiteinde; kiest noordwaarts Yellowhead 5 i.p.v. TCH 1 oost of BC 97 |
| b3 | 5 | Clearwater (YH 5) | 51.6511, -120.0400 | North Thompson-dal; pint YH 5 (Kamloops → Tête Jaune) |
| b3 | 6 | Tête Jaune Cache (YH 5 / YH 16) | 52.9759, -119.4226 | Yellowhead 16 oostwaarts (Jasper) i.p.v. BC 97 naar Prince George |
| b3 | 7 | Hinton (YH 16) | 53.4021, -117.5815 | Yellowhead door Jasper-park en Hinton richting Edmonton |
| b3 | 8 | Edmonton west (YH 16 / AB 216) | 53.5719, -113.6780 | Anthony Henday-ring (216) en Hwy 2 zuid i.p.v. het centrum |
Alle acht op trunk of motorway (OSRM-geometrie [9], scan-snap 0,00–0,01 km); gescand 1.350,2 km, −0,1% op de OSRM-indicatie; maximaal 1,1 km van het OSRM-pad. Een eerder via-punt Merritt (BC 5) is vervallen: de route volgt BC 5 vanzelf.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ningbo Zhaobao Magnet (3 productiebases, locatie niet geocodeerd) | Ningbo Zhaobao Magnet Co., Ltd | NdFeB-blanks → afgewerkte magneten | >11 kt NdFeB/j (2025, bedrijfsopgave) | [6] |
| Interra Energy Services (EMFTS Leduc) | Interra Energy Services Ltd | NdFeB-magneten (HS 8505.11.10); gebruik niet in de bron | niet gepubliceerd | [1] |

## 6 · Stoppunt
Op het adres in Leduc: de B/L noemt Interra Energy Services (3301 Allard Ave) als consignee en geen vervolg; wat de magneten daar worden (olie-dienstverlening) is niet gedocumenteerd, dus geen fase E.

## 7 · Open punten
- **Geen fabrieksanker:** No. 1 Haisi Rd, Zhenhai niet te geocoderen (Nominatim, Photon, ArcGIS); Zhaobao heeft drie productiebases. De lijn begint op de Beilun-kade (aannemelijk: B/L noemt alleen Ningbo).
- **Slechts twee B/L met identiek gewicht en collo (8.235 kg, 19 PKG):** onafhankelijkheid niet vast te stellen; de tweede staat onder "Zhaobao Magnet" zonder Ningbo, het jaarvolume kan dubbel geteld zijn (0,008–0,0165 kt). Alleen de eerste B/L toont vaartuig, haven en container [2]; die container staat als 40-ft reefer geboekt, wat voor magneten vreemd is.
- **Tacoma-terminal onbekend:** Husky is een aanname (ONE belt Husky, [3][5], maar de FMC-overeenkomst Husky/WUT [4] laat ook WUT, 47.2583,-122.3864, open).
- **Tacoma → Leduc onbekend:** in-bond, truck of trein (Husky heeft on-dock rail [3]); de Yellowhead-corridor is de OSRM-keuze, de route via Calgary is niet gemeten. Interra heeft ook een Balzac-site (51.2010,-113.9681), de B/L noemt Leduc.
- **Haven-aanloop b2 schematisch:** rechte stippel van 5,8 km; de eerste ca. 0,8 km vanaf de kade kruist het terminalterrein en valt in de 1:10M-kust als land.
- **Wegkm b3 onbekend** (hemelsbreed 919 km); de canada-pbf mist bij Avola (YH 5) en Jasper (YH 16) ways die OSM nu heeft: per bbox uit api.openstreetmap.org bijgevoegd (`v2/tools/ree_zhaobao_leduc_weg.py`). Het pbf-gat is niet nader onderzocht en kan andere stromen op de canada-extract raken.

## 8 · Bronnen
[1] ImportGenius, Interra Energy Services Ltd: 6 zendingen, B/L PEVHNBUC26060986 (Ningbo → Tacoma, ONE MAESTRO 087E, consignee EMFTS Leduc, 3301 Allard Ave), 22-08-2026 en 18-07-2026 NdFeB 8.235 kg. https://www.importgenius.com/importers/interra-energy-services-ltd
[2] ImportGenius, Ningbo Zhaobao Magnet Co., Ltd: 101 zendingen 2006–2026, shipper No. 1 Haisi Road, Zhenhai, Ningbo; sample-B/L 1 container, marks "ZHAOBAO CANADA", geen Canadese haven; andere VS-havens Long Beach, Los Angeles, Seattle, Newark, Houston. https://www.importgenius.com/suppliers/ningbo-zhaobao-magnet-co-ltd
[3] Northwest Seaport Alliance, Husky Terminal (Tacoma). https://nwseaportalliance.com/cargo-operations/terminals/husky-terminal-husky
[4] FMC, "Two Marine Terminal Agreements at Port of Tacoma Become Effective" (Husky / Washington United Terminals, 2018). https://www.FMC.gov/two-marine-terminal-agreements-at-port-of-tacoma-become-effective/
[5] Terminaldirectory: Husky Terminal & Stevedoring, 1101 Port of Tacoma Rd, carriers o.a. ONE, on-dock rail North Intermodal Yard (ongedateerd). https://blog.getmelrose.com/terminals/us/state/wa/husky-terminal-stevedoring
[6] Beursvermelding Ningbo Zhaobao: slimme productiebase 2025 >11.000 t NdFeB/j. https://berlin.cwiemeevents.com/exhibitors/ningbo-zhaobao-magnet-coltd
[7] OSM/Nominatim, 2026-10-31: Husky Terminal way 626041806 (47.27333,-122.41101); Allard Avenue (Leduc Business Park) way 98248952.
[8] ArcGIS World Geocoder, 2026-10-31: "3301 Allard Ave, Leduc, Alberta T9E 1J9", score 100, 53.29140,-113.51697. https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer
[9] OSRM (router.project-osrm.org), eigen meting 2026-10-31: Husky → Leduc 1.352,4 km (OSM-afgeleid, geen onafhankelijke bron).
[10] OSM/Geofabrik `us-washington-latest.osm.pbf` en `canada-latest.osm.pbf` (ODbL, wegscan met `wegscan_puur.py`) plus ways uit api.openstreetmap.org (way 58330070, 626197240, 626197429, 61314535, 625570772 en ca. 50 andere bij Avola en Jasper).
[11] MARNET `hecht_marnet`, eigen meting 2026-10-31: Beilun-kade → zeeknoop 5849 op 1,95 km; Tacoma-zeeknoop 7801 (47.3011,-122.4766) op 5,83 km van Husky en 8,30 km van WUT; route kade → knoop 9.667,2 km.
[12] Esri World Imagery via `sat_check.py`, z15: `v2/build-cache/satcheck/sat-ree-zhaobao-leduc-{husky,wut,leduc}.png`.
[13] `v2/design/routebrieven/ree-yunsheng-longbeach.md` §3 (Beilun-anker 29.9353, 121.8695, letterlijk hergebruikt).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Bestand:** `v2/data/stroomroute-ree-zhaobao-leduc.json` (versie 2, lonlat, 256,5 KB) · functie `bak_ree_zhaobao_leduc` in `v2/tools/bak_stromen.sh` · profiel `ree-zhaobao-leduc-husky-leduc` in `v2/tools/maak_stroombeen_weg.py` · tussenuitvoer `v2/build-cache/ais/graaf/ree-zhaobao-leduc-*` (weg-geojson 281,8 KB). Totaal 11.023,4 km, 3 benen, 3 markers, naden 0,00 km.

| # | modaliteit | been | km gebakken | km brief | geometrie | stippel |
|---|---|---|---|---|---|---|
| b1 | zee | Beilun CT Phase 2 → Tacoma-zeeknoop 7801 | 9.667,2 | router 9.667 (geen gepubliceerde km) | MARNET, 1.002 punten | nee |
| b2 | zee | haven-aanloop zeeknoop 7801 → Husky Terminal | 5,8 | 5,83 rechte lijn | rechte `--stippel`, 2 punten | ja, MARNET reikt niet tot de kade |
| b3 | truck | Husky Terminal → Leduc (I-5, BC 11, TCH 1, BC 5, YH 5 en 16, AB 216, AB 2) | 1.350,4 | hemelsbreed 919, geen wegkm; OSRM 1.352 (indicatie) | `wegscan_puur.py`, 11.112 punten | nee |

**Markers (3):** Beilun-kade (hergebruikt anker, 1,95 km van de lijnstart = MARNET-snap), Husky Terminal (0,00 km), Interra Leduc (0,00 km).

**Recept:** (1) `python v2/tools/ree_zhaobao_leduc_weg.py --profiel ree-zhaobao-leduc-husky-leduc` (wrapper op `wegscan_puur.py`, extracts us-washington + canada plus OSM-API-ways bij Avola en Jasper) → `ree-zhaobao-leduc-weg-husky-leduc.geojson`; (2) `bash v2/tools/bak_stromen.sh ree-zhaobao-leduc` (zwaar-slot) → het json. Geen lucht, geen leiding, geen kopie, geen fase E.

**Toetsresultaten:** b3 1.350,2 km tegen OSRM 1.352 = −0,1% (indicatie, geen echte wegkm); alle 8 via-punten snappen op 0,00–0,01 km, geen omweg; naden 0,00 km; `toets_rechte_benen --min-km 5` meldt alleen de stippel b2; json.load, versie 2, lonlat, modaliteiten {zee, truck}, elk been ≥ 2 punten.

**Toelichting stippel b2 (haven-aanloop Tacoma):** Husky ligt 5,83 km van zeeknoop 7801 (> 5 km). `maak_havenaanloop.py` is niet gedraaid (ontwerp: geen pad in 280 s), dus een rechte schematische stippel in reisvolgorde knoop → kade; de eerste ca. 0,8 km kruist het terminalterrein (1:10M-kust ziet land).

**Bevindingen (geen via-punt bijgeschoven):**
- Beilun-marker staat 1,95 km van de lijnstart: de MARNET-snap (< 5 km, dus geen aanloop volgens §2); procesgat, blijft staan.
- `toets_knikken`: b3 heeft 1 TERUGLOOP (158 gr, R 7 m) bij 53.4381,-113.4903: een stomp van ca. 0,1 km heen en terug bij een oprit langs Hwy 2 bij Edmonton-zuid; niet gerepareerd. De 172 gr-bocht bij 47.2412,-122.3866 is echt (afrit Port of Tacoma Rd naar I-5 noord).
- Het pbf-gat van de canada-extract bij Avola en Jasper (zie §7) is niet onderzocht en kan andere stromen op de canada-extract raken: melden aan centraal.

**Lessen:** (1) een eindpunt zonder fabrieksanker laat de lijn op de kade beginnen; zeg dat in de beennaam en de ⚠-noot. (2) Een pbf-gat op een corridor repareer je per bbox via de OSM-API in de eigen wrapper, niet in `wegscan_puur.py`. (3) Een 5,8 km-aanloop zonder `maak_havenaanloop`-pad is een eerlijke stippel met reden; geen gemeten been voortzetten.
