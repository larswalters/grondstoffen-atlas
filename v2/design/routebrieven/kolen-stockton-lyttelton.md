# Routebrief (licht) · Kolen · Stockton → Ngakawau → Lyttelton (Nieuw-Zeeland)

**stroom-id:** `kolen-stockton-lyttelton` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** cokeskool van de Stockton-mijn (Denniston Plateau, BT Mining) per **truck** ~7,4 km over de private mijnweg (Burma Road) naar het bovenstation van de Stockton-kabelbaan, per **kabelbaan** (OSM aerialway=goods, ~2,2 km) omlaag naar het laadstation bij Ngakawau, per **spoor** ~393 km (Stillwater-Ngakawau-lijn, Midland-lijn: Otira-tunnel, Arthurs Pass, Rolleston, Christchurch, Lyttelton-tunnel) naar de kolenterminal van Lyttelton Port (Cashin Quay) — stoppunt: daar verscheept de lading naar Japan, Zuid-Korea, China, India (en volgens Wikipedia ook Zuid-Afrika, Brazilie), dus de lijn stopt bij de kade.
**Welke as van het verhaal:** *Nieuw-Zeelandse cokeskool: bergspoor en kabelbaan naar één haven* — Stockton leverde 0,98 Mt in 2021 van de 1,32 Mt kolen op de lijn (Wikipedia) [2]; Bathurst voorziet voor NZ-activiteiten ~1,1 Mtpa export (FY25E) [6]. Volume Stockton: 0,98 Mt kolen per jaar (2021) [2]; de productie loopt terug (Stockton richting sluiting, Tawhai-tunnel dicht 2024-25 volgens de haalbaarheidstoets, niet zelf geverifieerd).

## 1 · Ketenkaart
```
Stockton-mijn `kolen-stockton-mijn` ──(b1 truck · Burma Road, private mijnweg · 7,4 km)──► kabelbaan-bovenstation `kolen-stockton-kabelbaan-boven`
   ──(b2 kabelbaan · aerialway=goods, 2,2 km)──► Ngakawau-laadstation `kolen-ngakawau-laadstation`
   ──(b3 spoor · Stillwater-Ngakawau-lijn + Midland-lijn · ~393 km)──► Lyttelton-kolenterminal `kolen-lyttelton-kolenterminal` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Stockton-mijn → kabelbaan-bovenstation | Burma Road (private service-ways, access=private; laatste ~50 m track access=no) | 7,4 (Bathurst-presentatie "7,4 km haul road", via WebSearch-samenvatting) [7]; OSM-meting 7,3 | maak_stroombeen_weg (profiel `kolen-stockton-lyttelton-mijn-kabelbaan` staat er al) | nee — privé maar in OSM gekarteerd |
| b2 | A | leiding (kabelbaan) | kabelbaan-bovenstation → Ngakawau-laadstation | Stockton-kabelbaan (OSM way 153734257, aerialway=goods, resource=coal, 17 punten) | 2,3 (Bathurst-presentatie) [7]; OSM-geometrie 2,208 (−4%) | vooraf gemaakt geojson (FeatureCollection, way omgekeerd: OSM loopt Ngakawau → boven, lading omlaag) | nee |
| b3 | B | spoor | Ngakawau-laadstation → Lyttelton-kolenterminal | Stillwater-Ngakawau-lijn → Stillwater → Midland-lijn → Rolleston → Lyttelton-tunnel | 393 (Wikipedia, Ngakawau-Lyttelton) [2]; gemeten 393,3 (+0,1%; router meldt 388,8 over 764 edges) | toets_spoorroute, één run, geen via-punten | nee |

Totaal ca. 403 km. Geen zeebeen, geen haven-aanloop, geen stippel. Naden: b1→b2 0,05 km, b2→b3 ~0,1 km, spooreind → anker 0,26 km.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-stockton-mijn` | mijn | Stockton Mine, Denniston Plateau (BT Mining = Bathurst 65% / Talleys 35%) | -41.6619, 171.8764 | [4] GEM (exact); Wikipedia-kandidaat -41.668/171.867 ligt 1,0 km SW en geeft 9,1 km weg, GEM-punt geeft precies 7,4 km | bron-gelegd op site-niveau (z15 gezien: één grote dagbouwcomplex met terrassen, haulroads, kolenhopen en tailingsvijvers; punt ligt op een groene hellingstrook tussen twee putten naast de haulroad, niet op één bepaalde put) |
| `kolen-stockton-kabelbaan-boven` | overslag truck → kabelbaan | bovenstation Stockton-kabelbaan | -41.6283, 171.8889 | [9] OSM way 153734257 (einde) | bron-gelegd (z15 gezien: open plek in het bos aan het einde van de verharde mijnweg; de kabelbaanlijn is een smalle bosdoorsnijding noordwaarts) |
| `kolen-ngakawau-laadstation` | overslag kabelbaan → spoor | Ngakawau-laadstation / CHPP-loadout | -41.6105, 171.8772 | [9] OSM way 153734257 (begin) + OSM-spoorsidings (service=spur) [8] | bron-gelegd (z15 gezien: laadinstallatie en spoorbundel aan de monding van de Ngakawau-rivier, strand en dorp ernaast) |
| `kolen-lyttelton-kolenterminal` | losplek / verscheping | Lyttelton Port Company, kolenterminal Cashin Quay (opslag tot 335.000 t, shiloader) | -43.6053, 172.7367 | [5] GEM; OSM: Coal Dump Private Siding | bron-gelegd (z15+z16 gezien: groot zwart kolenstockyard ~200 m NW van het punt, containerkade en bulkschip; punt ligt op het oostelijke uiteinde van Cashin Quay bij de laadkade) |

## 4 · Via-punten (alleen b1; b3 draait zonder via-punten)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Burma Road noord | -41.6550, 171.8925 | de weg draait hier van de mijnvlakte naar het noordoosten; pint de Burma Road-corridor (OSM way 459262325/459262329) |
| b1 | 2 | Burma Road oost | -41.6342, 171.9037 | oostelijkste punt van de lus langs de plateaurand (way 1059440887), pint de route tegen de zijtakken van de Fly Creek Mine Road |
| b3 | — | geen | — | één run gaf passages binnen 0,2-2,2 km van Westport, Inangahua, Reefton, Stillwater, Otira, Arthurs Pass, Springfield, Rolleston en Addington, geen omweg via Greymouth |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Stockton CHPP + rail-loadout, Ngakawau | BT Mining (Bathurst 65% / Talleys 35%) | ROM-kolen via kabelbaan → gewassen kolen → trein | CHPP-capaciteit niet gevonden | [7][8] |
| Lyttelton kolenterminal | Lyttelton Port Company (Christchurch City Holdings) | trein → stockyard → schip | tot 2,5 Mt/j (oude opgave), 335 kt opslag, doorvoer 2,1 Mt in FY2011 | [5] |

## 6 · Stoppunt
De brief stopt bij de kolenterminal van Lyttelton: de lading gaat vanaf de kade naar meerdere landen (Japan, Zuid-Korea, China, India) en er is geen enkele afnemer voor deze lading met naam gevonden, dus fase C/D/E vervalt. Parcels per barge Westport → Port Kembla [1] zijn een zijtak en niet getekend.

## 7 · Open punten
- **Mijnanker op site-niveau:** het GEM-punt ligt in de concessie, niet op een specifieke put; welke put nu de haulroad voedt is niet vast te stellen. Wikipedia-kandidaat (-41,668/171,867) is niet gebruikt.
- **7,4 km en 2,3 km komen uit een samenvatting van een Bathurst-presentatie** (WebSearch-resultaat); de bronpagina zelf is niet teruggevonden in de gedownloade pdf's. De OSM-metingen (7,3 en 2,208 km) sluiten er wel op aan.
- **Kabelbaan als "leiding":** modaliteit `leiding` staat voor de kabelbaan (binding van de haalbaarheidstoets); in de beennaam staat dat het een kabelbaan is. OSM-richting is omgekeerd aan de lading en in het geojson omgedraaid.
- **Productie loopt terug:** Stockton richting sluiting, Tawhai-tunnel-afsluiting 2024-25 (haalbaarheidstoets, niet geverifieerd); het jaarvolume 0,98 Mt is van 2021.
- **b3 eindigt 0,26 km vóór het anker** (spoor eindigt op het emplacement, geen coördinaat voor de exacte siding); geen stippel getekend.
- **Kolenvolume Lyttelton-terminal per jaar** niet gevonden (alleen FY2011).
- **Sitelaag:** kolen-sitelaag kent geen NZ-site; Stockton-mijn en Lyttelton-terminal zijn kandidaten (centraal).

## 8 · Bronnen
[1] Wikipedia, Stockton Mine — kolen per ropeway naar Ngakawau, per spoor naar Lyttelton, export Japan/India/China/Zuid-Afrika/Brazilie, barge Westport → Port Kembla. https://en.wikipedia.org/wiki/Stockton_Mine
[2] Wikipedia, Stillwater–Ngākawau line — 984.951 t uit Stockton in 2021 van 1.321.541 t, Ngakawau-Lyttelton 393 km, 12,5 uur. https://en.wikipedia.org/wiki/Stillwater%E2%80%93Ng%C4%81kawau_line
[3] Wikipedia, Midland line (New Zealand) — Rolleston-Greymouth 212 km, Otira-tunnel 8.554 m, 2,1 Mt kolen in 2003. https://en.wikipedia.org/wiki/Midland_line_(New_Zealand)
[4] Global Energy Monitor, Stockton Mine — coördinaat -41.661884/171.87644, BT Mining 65/35, per spoor naar Lyttelton. https://www.gem.wiki/Stockton_Mine
[5] Global Energy Monitor, Lyttelton Port Coal Terminal — LPC, 335 kt opslag, tot 2,5 Mt/j, 2,1 Mt FY2011. https://www.gem.wiki/Lyttelton_Port_Coal_Terminal
[6] Bathurst Resources, presentatie AusIMM NZ-tak (Tacon, 2024-08-25) — FY24 1,7 Mt NZ-productie, 1,1 Mtpa export naar Japan, Zuid-Korea, China, India. https://www.ausimm.com/globalassets/pdf-files/publications/_ausimm-proceedings/nz-branch-24_08_25/24_08_25richard_tacon.pdf
[7] WebSearch-samenvatting van een Bathurst Resources-presentatie: "7,4 km haul road en 2,3 km aerial cableway naar stockpile en rail loadout bij Ngakawau" (bronpagina niet zelf geopend); zie ook TTPP, Bathurst operations in BCZ (ACML 2-5 haul road en aerial, CHPP Ngakawau). https://ttpp.nz/wp-content/uploads/2024/06/Bathurst-operations-in-BCZ.pdf
[8] OpenStreetMap via Geofabrik-extract nieuw-zeeland (lokaal): aerialway-way 153734257, Burma Road en service-ways, spoor-spurs bij Ngakawau.
[9] Haalbaarheidstoets kolen-stockton-lyttelton (golf 19): spoorrun 388,2 km, kabelbaan-ID, Lyttelton-siding.
[10] Esri World Imagery via sat_check.py (z15/z16): `v2/build-cache/satcheck/sat-kolen-stockton-lyttelton-mijn-gem.png`, `-kabelbaan-boven.png`, `-ngakawau.png`, `-lyttelton-z16.png`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)

**Bestand:** `v2/data/stroomroute-kolen-stockton-lyttelton.json` (30,3 KB, versie 2, punt_formaat lonlat) · functie `bak_kolen_stockton_lyttelton` in `v2/tools/bak_stromen.sh` · profiel `kolen-stockton-lyttelton-mijn-kabelbaan` in `v2/tools/maak_stroombeen_weg.py` (stond er al).
**Titel:** Kolen · Stockton-mijn (Denniston Plateau) → kabelbaan → Ngakawau → Midland-lijn → Lyttelton (Nieuw-Zeeland).

| # | modaliteit | been | km gebakken | km brief | afwijking | punten | naad |
|---|---|---|---|---|---|---|---|
| 1 | truck | Stockton-mijn → Burma Road (private mijnweg) → kabelbaan-bovenstation | 7,4 | 7,4 (Bathurst, via samenvatting) | 0% | 111 | – |
| 2 | leiding | Stockton-kabelbaan (aerialway, OSM way 153734257) → Ngakawau-laadstation | 2,2 | 2,3 (Bathurst) / OSM 2,208 | -4% | 17 | 0,003 km |
| 3 | spoor | Ngakawau → Stillwater-Ngakawau-lijn → Midland-lijn → Lyttelton-kolenterminal | 393,3 | 393 (Wikipedia) | +0,1% | 1352 | 0,085 km |

Totaal 402,9 km · 3 benen, alle doorgetrokken (0 stippel) · 4 markers (de 4 ankers van §3, afstand tot lijn 0,00 / 0,00 / 0,004 / 0,239 km) · naden max 0,085 km.

**Recept:**
- b1: `wegscan_puur.py --profiel kolen-stockton-lyttelton-mijn-kabelbaan` (extract nieuw-zeeland, 2 via-punten uit §4, `corridorKlassen ["service"]`, `eindToegangPrivaat`); snaps 0,00-0,05 km; geojson `kolen-stockton-lyttelton-weg-mijn-kabelbaan.geojson`.
- b2: OSM-way 153734257 omgekeerd (bovenstation → Ngakawau), FeatureCollection `kolen-stockton-lyttelton-leiding-kabelbaan.geojson`, `--been-geojson "leiding|…"`.
- b3: `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs` een run zonder via-punten (routeKm 388,8 over 764 edges; getekende lengte 393,3), `spoorroute-kolen-stockton-lyttelton-ngakawau-lyttelton.geojson`; snap 0,08 km bij Ngakawau, 0,24 km bij Lyttelton.
- Bake: `bash v2/tools/bak_stromen.sh kolen-stockton-lyttelton`, via het zwaar-slot; geen zee, dus MARNET alleen geladen, niet gebruikt.

**Toelichting per bijzonderheid:**
- Geen stippel, geen haven-aanloop, geen vlucht, geen kopie van een andere stroom. Er is geen zeebeen: de lijn stopt bij de kade van Lyttelton (export naar meerdere landen).
- Leiding = kabelbaan: modaliteit `leiding` is bindend (haalbaarheidstoets); "Stockton-kabelbaan (aerialway…)" staat in de beennaam. OSM-richting omgedraaid (lading gaat omlaag).
- Spoor eindigt 0,24 km voor het anker (emplacement/siding niet als coördinaat bekend): onder de 5 km-grens, geen stippel.
- toets_knikken: 3 knikken in b1 (truck, mijnterrein, 0 omkeringen, 0 terugloop), allen binnen 0,1 km van het mijnanker (spikes in de privé-mijnwegen); b2 en b3 geen knikken. toets_rechte_benen: geen enkel been van deze stroom gemeld.

**Lessen / open:**
- 7,4 en 2,3 km blijven afkomstig uit een WebSearch-samenvatting; de gemeten waarden (7,4 / 2,2 / 393,3) sluiten er wel op aan.
- Mijnanker staat op site-niveau (GEM-punt), niet op een put; Wikipedia-kandidaat niet gebruikt.
- Productie loopt terug (0,98 Mt in 2021): een mogelijke sluiting van Stockton valt buiten wat de lijn kan tonen.
- Sitelaag kent geen NZ-site: Stockton-mijn en Lyttelton-terminal zijn kandidaten (centraal).
- Register en bundel niet aangeraakt (centraal). Registerregel: sleutel `kolen-sl`, label "Stockton → Lyttelton".
