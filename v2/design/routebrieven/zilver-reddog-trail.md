# Routebrief (licht) · zilver — Red Dog → Vancouver Wharves → Teck Trail (Alaska / Canada)

**stroom-id:** `zilver-reddog-trail` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** zilverhoudend zink-/loodconcentraat van de Red Dog-mijn (Teck/NANA, Alaska) per truck over de
privé-haulroad (DMTS, 84 km) naar de DeLong Mountain-terminal, per barge + zeeschip (juli–oktober) naar Vancouver Wharves
(North Vancouver), per **spoor** (aannemelijk: één bron) naar de Teck Trail-smelter — **stoppunt** (Teck's eigen smelter).
**Welke as van het verhaal:** *Noordwest-Amerika: Arctisch concentraat naar de grootste Noord-Amerikaanse Zn-Pb-Ag-smelter.*
Jaarvolume **ca. 70–95 t Ag/j, indicatief**: mijn-Ag 283 t (2008) [1] resp. ~202 t (6,5 Moz, 2023, schatting) [9] × 34 % van het
Red Dog-zinkconcentraat naar Trail (2018) [2]; geen recent Ag-cijfer van Teck, Ag zit vooral in het loodconcentraat (ook naar Trail [2]).

## 1 · Ketenkaart
```
Red Dog-mijn/concentrator ──(b1 truck · DMTS-haulroad · 84 km)──► DeLong Mountain-terminal (barges, lichteren ~5 km offshore)
  ──(b2a zee-stippel · haven-aanloop · ~287 km)──► Beringstraat (MARNET-knoop 2) ──(b2b zee · router · ~4.520 km)──► Vancouver Wharves
  ──(b3 spoor · aannemelijk: één bron · 1.107,8 km gemeten)──► Teck Trail-smelter ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ag-reddog-mijn` → `ag-reddog-delong` | Red Dog Mine Road = DMTS-haulroad (OSM `highway=tertiary`, privé) [3][7] | **84** (52 mijl, AIDEA) [3] | `maak_stroombeen_weg` (nieuw profiel, `us-alaska`) | nee; valt de scan uit (osmium geblokkeerd, Overpass down bij schrijven) → `--stippel` met reden |
| b2a | B | zee | DeLong-terminal → Beringstraat-knoop | — (barges lichteren ~5 km offshore; ijsvrij ~100 dagen) [2][3] | ~287 grootcirkel (gemeten), geen norm | stippel (`--stippel "zee\|haven-aanloop …"`) | **ja: MARNET reikt niet tot de Chukchi-kust** (kade 89,5 km van zeeknoop 957, doodlopend; `maak_havenaanloop` gaf time-out) |
| b2b | B | zee | Beringstraat (65.9622,-169.1502) → `ag-vancouver-wharves` | Beringstraat – Bering Zee – Golf van Alaska – Juan de Fuca – Burrard Inlet | **~4.522** (router; ontwerpschatting 5.800 te hoog), geen norm | MARNET (`--been "zee\|…"`) | nee; Wharves-kant zeeknoop 7818 op 2,0 km → geen aanloop |
| b3 | C | spoor | `ag-vancouver-wharves` → `ag-trail-smelter` | BNSF Stevens Pass – Spokane – Sandpoint – Eastport – CP Yahk/Creston/Nelson (door het net gekozen) | **1.107,8** gemeten; hemelsbreed 393 km, **geen spoorkm gepubliceerd** → geen ±15 %-norm | `toets_spoorroute.mjs` (`BAKE_SUFFIX=-raw`), één run | nee — doorgetrokken; "aannemelijk: één bron" staat in de beennaam |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-reddog-mijn` | mijn + concentrator (laad) | Red Dog-mijn en concentrator (Teck/NANA) | 68.0724, -162.8591 | [1][2][7] | bron-gelegd (z14 gezien: concentrator-/molencomplex direct oost van het kruis, dagbouwpit met oranje meer NE, tailingsmeer SW) |
| `ag-reddog-delong` | haven/terminal (overslag truck → barge) | Red Dog Port Site / DeLong Mountain Terminal | 67.5817, -164.0424 | [3][7] | bron-gelegd (z15 gezien: kruis op de transportband tussen twee concentraatloodsen NE en het havencomplex met tanks/containers SW; kade zelf offshore — barges) |
| `ag-vancouver-wharves` | overslag zee → spoor | Vancouver Wharves, 50 Philip Ave, North Vancouver (Pembina) | 49.3155, -123.1141 | [4][5][6][7] | **aannemelijk** (z15 gezien: bulkterminal met loodsen, schip aan de kade en lustrack; kruis op het spoorbundel/emplacement aan de noordrand; OSM-station "Vancouver Wharves Terminal"; spoor-snap 0,01 km). Eén bron + oud nieuws voor Wharves als Red Dog-terminal — **niet Neptune** |
| `ag-trail-smelter` | smelter + raffinaderij (los, stoppunt) | Teck Trail-smelter | 49.1000, -117.7125 | brief `zilver-luckyfriday-trail` | bron-gelegd — letterlijk hergebruikt (bron-brief: `zilver-luckyfriday-trail.md` §3; z15 daar gezien) |

## 4 · Via-punten (alleen b1; b2 = router, b3 = één spoorrun zonder via)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Red Dog Mine Road, noordsegment | 67.9667, -163.0145 | OSM-segment van de haulroad (Nominatim); pint de weg weg van de mijn |
| b1 | 2 | Red Dog Mine Road, middensegment | 67.7867, -163.4777 | idem; houdt de lijn op de enige doorgaande weg |
| b1 | 3 | Red Dog Mine Road, zuidsegment | 67.5944, -164.0056 | idem; ~3 km voor de terminal (Port Site-segment) |

De haulroad is één weg zonder corridorkeuze: de via-punten zijn OSM-wegsegmenten, geen keuze. Geofabrik-extract: `us-alaska`
(144 MB, aanwezig); profiel `corridorKlassen: ["tertiary"]`, `eindToegangPrivaat: True`, `gepubliceerdKm: 84`.
b3 **geen via-punten**: Northport/Waneta-via (ontwerp) en een Spokane-centrum-via (omkering bij 47.65,-117.44) zijn getest en
verworpen. Controleplaatsen langs de gemeten lijn (alle ≤ 5,2 km): Everett, Stevens Pass, Wenatchee, Spokane, Sandpoint,
Bonners Ferry, Eastport, Yahk, Creston, Nelson, Castlegar. Twee 177°-omkeringen (Yahk-wye 49.0782,-116.1269; smelteranker
49.0990,-117.7145) zijn echte kopmaakplekken/ankervorm — via-punten niet schuiven.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Red Dog-concentrator | Teck Alaska (land NANA) | Zn-Pb-Ag-erts → zink- en loodconcentraat | zinkconcentraat 574 kt verkocht 2024; zink 462,7 kt 2025 (afnemend, reserves slinken) | [2][10] |
| Vancouver Wharves | Pembina (PKM Canada Marine Terminal) | import zink-/loodconcentraat → spoor | 4 Mt droge bulk/j totaal, 3 klasse-I-spoorwegen | [4] |
| Teck Trail Operations | Teck | Zn-Pb-concentraat → Zn, Pb, Ag (good delivery) | zie `zilver-luckyfriday-trail` §5 | [2] |

## 6 · Stoppunt
De brief stopt bij Teck Trail: geen fase D/E — geen bron noemt een fabriek of afnemer van het Trail-zilver, en Trail is de
bestemming van het concentraat (Teck-eigen, 34 % van het Red Dog-zinkconcentraat in 2018 [2]).

## 7 · Open punten
- **Vancouver-terminal is aannemelijk, niet bevestigd:** 1990 North Shore News (via zoeksamenvatting), Pembina "import zink- en
  loodconcentraat voor binnenlandse smelters" [4] en de 2005 Trail-staking (Red Dog-concentraat opgeslagen in Vancouver [5]);
  Teck noemt de terminal niet. Neptune is een niet-onderbouwde gok en niet gebruikt.
- **Modaliteit Vancouver → Trail aannemelijk:** 1989 Northern Miner "Burlington Northern's Vancouver terminal" (alleen snippet, paywall) [6];
  Pembina meldt spoor met drie klasse-I-spoorwegen [4]; Teck Trail-prospectus 2009 noemt openbare weg (sluit spoor niet uit). Weg via BC Hwy 3/3B (~650 km) is het alternatief.
- **Actualiteit:** Red Dog draait (2025: zink 462,7 kt, afnemend; seizoen start juli [10]); of Trail nu nog via Vancouver Wharves levert is niet bevestigd.
- **Recent Ag-volume niet gepubliceerd** door Teck; 6,5 Moz (2023) komt uit een zoeksamenvatting van North of 60 Mining News, niet zelf gelezen (Cloudflare 403).
- **Haulroad-scan niet getest:** osmium/Overpass onbereikbaar op schrijfdag; privétoegang in OSM (`access`) onbekend. Faalt de scan → b1 als stippel (84 km van ~6.000: acceptabel).
- **b2a is 287 km schematisch:** Arctische MARNET-dekking ontbreekt; knoop 2 is de enige aangesloten knoop. Zeeroute naar Vancouver via Unimak Pass niet onafhankelijk gecontroleerd (router bepaalt).
- **Sitelaag:** Red Dog en Vancouver Wharves ontbreken in `zilver-sitelaag.json` (centraal: `ag-reddog-mijn`, gewicht uit [1][9]). Greens Creek → Trail kan b3 later als letterlijke kopie hergebruiken.

## 8 · Bronnen
[1] Wikipedia, "Red Dog mine" (283 t Ag 2008; 144 km N van Kotzebue) — https://en.wikipedia.org/wiki/Red_Dog_mine
[2] Teck Resources, Annual Information Form FY2018 (34 % Zn-concentraat naar Trail; Pb-concentraat ook; ~100 dagen seizoen; opslag, verscheping juli–okt) — https://www.sec.gov/Archives/edgar/data/886986/000119312519055171/d677438dex991.htm
[3] AIDEA, DMTS Project Fact Sheet 2023 (52-mijl haulroad, offshore conveyor naar lichteraars, 2 loodsen) — https://www.aidea.org/Portals/0/ProjectFactSheets/DMTS%20Project%20Fact%20Sheet%202023.pdf
[4] Pembina, Vancouver Wharves (125 acre, 4 kaaien, 3 klasse-I-spoorwegen, import Zn-/Pb-concentraat) — https://www.pembina.com/operations/facilities/vancouver-wharves/
[5] Mining News North, "Teck Cominco resolves smelter strike", 2005-10-30 (via haalbaarheidstoets; zelf 403) — https://www.miningnewsnorth.com/story/2005/10/30/news/teck-cominco-resolves-smelter-strike/1310.html
[6] Northern Miner, "Alaska's Red Dog" (1989; snippet via haalbaarheidstoets) — https://northernminer.com/news/alaska-s-red-dog/1000174658
[7] Nominatim/OSM: Red Dog Mine Road (3 segmenten, tertiary), Red Dog Port Site — https://nominatim.openstreetmap.org/
[8] Brief `zilver-luckyfriday-trail.md` (anker `ag-trail-smelter`) en bak-/spoortoets van deze brief (`toets_spoorroute.mjs`, 1.107,8 km; `hecht_marnet`: knoop 957 op 89,5 km, knoop 2 op 287 km, knoop 7818 op 2,0 km).
[9] North of 60 Mining News, "Red Dog ends 2023 with solid production" (~6,5 Moz Ag, schatting; via zoeksamenvatting) — https://miningnewsnorth.com/story/2024/02/23/news-nuggets/red-dog-ends-2023-with-solid-production/8407.html
[10] Teck 40-F FY2025 MD&A en North of 60 "Red Dog output drops as reserves dwindle" (2026-02-20) — https://www.sec.gov/Archives/edgar/data/886986/000088698626000004/teck-20251231xexx993mda.htm
[11] Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-zilver-reddog-trail-{mijn,delong,vancouverwharves}.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Recept:** `bash v2/tools/bak_stromen.sh zilver-reddog-trail` (functie `bak_zilver_reddog_trail`); uitvoer `v2/data/stroomroute-zilver-reddog-trail.json`
(versie 2, lonlat, 90 KB, 4 benen, 6.009,3 km, 4 markers). Hulpbestand: `v2/tools/zilver_reddog_haulroad_nominatim.py` (b1).

| # | modaliteit | km gemeten | norm / bron | naad naar volgende | geometrie |
|---|---|---|---|---|---|
| b1 | truck | **82,8** | 84 (AIDEA, 52 mijl) = **-1,4 %** | 0,00 km | doorgetrokken: zes OSM-ways "Red Dog Mine Road" (W406680950, W406682670, W406680951, W1216571725, W1216571731, W1216384800) via Nominatim-lookup, 465 punten |
| b2a | zee | 287,4 | geen norm (grootcirkel) | 0,00 km | **stippel**: MARNET reikt niet tot de Chukchi-kust |
| b2b | zee | 4.522,2 | geen norm (router; ontwerp 5.800 te hoog) | 2,03 km (Wharves-zeeknoop 7818, < 5 km, geen aanloop) | MARNET-router knoop 2 -> Wharves, via Unimak Pass-zone en Juan de Fuca |
| b3 | spoor | 1.116,9 (hecht_marnet-lengte; `toets_spoorroute.mjs` zelf: 1.107,8) | geen spoorkm gepubliceerd; hemelsbreed 393 km | - | doorgetrokken, `BAKE_SUFFIX=-raw`, 1.278 edges, snap 0,01/0,16 km |

**Markers (4):** `ag-reddog-mijn` 0 m van de lijn, `ag-reddog-delong` 0 m, `ag-vancouver-wharves` 7 m, `ag-trail-smelter` 132 m (spoor eindigt op de rail-snap 0,16 km van het anker; < 0,5 km).

**Toelichting per afwijking / keuze**
- **b1 is niet via `maak_stroombeen_weg.py` gebakken.** pyosmium/osmium is op deze machine geblokkeerd (toepassingsbeheer, bewust niet omzeild) en alle Overpass-spiegels
  gaven 500/403/verbroken verbinding (2026-10-09). De weg is toch OSM-geometrie: Nominatim kent de Red Dog Mine Road als zes ways (`highway=tertiary`) en levert hun volle geometrie
  (`lookup ... polygon_geojson=1`). Eén naadvrije keten mijn -> Port Site, naden tussen de ways 0-62 m (node-afronding), ankerstub mijn 0,26 km. De laatste way loopt 1,08 km voorbij
  het Port Site-anker door en is op de ankerprojectie geknipt (anders een TERUGLOOP-knik in `toets_knikken`); stub naar het anker 0,05 km. Het profiel
  `zilver-reddog-trail-reddog-delong` (vensterKm 40, `corridorKlassen ["tertiary"]`, `eindToegangPrivaat`) staat klaar in `maak_stroombeen_weg.py` maar is **niet gedraaid**; de drie via-punten uit §4 zijn
  gecontroleerd tegen Nominatim (zij liggen op de ways W406680950/W406680951/W1216384800), de router-run met `--bron geofabrik` is open tot osmium gedeblokkeerd is. De privé-status (`access`) van de haulroad blijkt niet uit deze data.
- **b2a stippel** (kade 89,5 km van zeeknoop 957, doodlopend; barges lichteren ca. 5 km offshore; geen `maak_havenaanloop`-run, time-out al vastgesteld). Stippel = "hier reikt het net niet".
- **b2b**: 45 MARNET-edges, 476 punten; Wharves-snap 2,02 km. "aannemelijk: een bron" staat in de beennaam; doorgetrokken.
- **b3**: twee omkeringen (Yahk-wye 49.0782,-116.1269 = TERUGLOOP in `toets_knikken`, kopmaakplek; smelteranker 49.0990,-117.7145 = echte scherpe bocht) blijven staan, zoals de brief voorschrijft.
- `toets_knikken` b2b: zes krappe bochten (68-98 graden, boogstraal 1,3-7 km) in de Juan de Fuca-/Salish Sea-uitloop: MARNET-vorm, geen omkering. `toets_rechte_benen`: alleen de stippel b2a (met reden).
- Eén 90-graden-spike (35 m straal) in b1 aan het einde, door de 50 m-ankerstub naar het Port Site-kruis (kruis staat naast de weg).

**Lessen:** (1) Valt de wegscan uit door osmium/Overpass, dan kan Nominatim `lookup` met `polygon_geojson=1` per benoemde OSM-way de volle geometrie leveren; ketenen op de eindpunten (naad < 100 m)
en snij de laatste way op de ankerprojectie (de OSM-way loopt vaak voorbij het site-anker). `reverse` (zoom 17-18, `polygon_geojson`) vindt de ontbrekende ways in de gaten tussen de benoemde segmenten.
(2) De slot-helper met `rm -rf "$d"` wordt door de veiligheidscontrole geweigerd; een helper met alleen literale paden (`rm -f`/`rmdir`) werkt.
(3) Sitelaag: Red Dog (`ag-reddog-mijn`) en Vancouver Wharves ontbreken nog in `zilver-sitelaag.json` (centraal).
