# Routebrief (licht) · lithium — Wodgina → Port Hedland → Zhenjiang (Xinminzhou-haven)

**stroom-id:** `lithium-wodgina-qinzhou` (id behouden — het eindpunt is **Zhenjiang, niet Qinzhou**, zie §6/§7) · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat (SC5,5–6) van de Wodgina-plant (MinRes 50 % / Albemarle 50 %) gaat per **road train** over de Wodgina Access Road en de Great Northern Highway naar de Utah Point-bulkfaciliteit in Port Hedland (de weg- en haven-aanloopbenen zijn letterlijke kopieën van lithium-pilgangoora-gwangyang), per **bulkcarrier** ~6.050 km via Lombok–Makassar–Taiwanstraat naar de Yangtze-monding en per binnenvaartgeul ~250 km stroomopwaarts naar de Xinminzhou-haven bij Zhenjiang — het door Albemarle opgegeven afhaalpunt van zijn Wodgina-veilingen. De chemische converter (Albemarle Qinzhou of een koper) wordt niet getekend.
**Welke as van het verhaal:** Albemarles Wodgina-aandeel gaat als concentraat naar de Chinese markt via een afhaalpunt aan de Yangtze, niet rechtstreeks naar zijn eigen kustfabriek. Volume (peiljaar 2025): Albemarle-aandeel **8 kt Li-metaal ≈ 43 kt LCE/j** [2]; mijn totaal ≈ 16 kt Li ≈ 85 kt LCE; naamplaat 750 kt SC5,5/j ≈ 100 kt LCE [1][11]. *Eenheid: kt LCE = kt Li × 5,323; sitelaag: kt SC × 5,5 % × 2,473.*

## 1 · Ketenkaart
```
Wodgina-plant `li-wodgina-plant` ──(b1 truck · Wodgina Access Road → Great Northern Hwy (NH95) · hemelsbreed 110 km, geen wegkm)──► GNH zuidzijde graafgat
   ──(b2 stippel 0,36 km OSM-gat — kopie pilgangoora)──► GNH-stadsnet Port Hedland ──(b3 truck · GNH → Utah Road · 8,7 km — kopie)──►
Utah Point Berth 4 `li-porthedland-utahpoint` (aannemelijk) ──(b4 haven-aanloop stippel 80,5 km — kopie)──► zeeknoop 3883 (-19.6000, 118.6000)
   ──(b5 zee · Lombok–Makassar–Taiwanstraat · ~6.050 km, MARNET; bestemming aannemelijk: afhaalpunt Zhenjiang)──► Yangtze-monding `li-yangtze-monding`
   ──(b6 stippel 8,6 km zeenet → bulklaag — kopie bak_lithium · b7 binnenvaart ~250 km · b8 aanloop-stippel 4,6 km)──► Xinminzhou-kade `li-zhenjiang-kade` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (road trains, onbevestigd) | `li-wodgina-plant` → GNH zuidzijde graafgat (-20.377913, 118.575136) | Wodgina Access Road (9 km, privé-/mijnweg) → Great Northern Hwy (NH95/NH1) | hemelsbreed 110 km, geen wegkm [2]; indicatie OSRM 103,9 km [9] | maak_stroombeen_weg (nieuw profiel, extract australie, `eindToegangPrivaat`) | nee |
| b2 | A | truck (stippel) | GNH zuidzijde → GNH-stadsnet noordzijde (-20.374731, 118.574874) | OSM-topologiegat | 0,355 gemeten | letterlijke kopie `bak_lithium_pilgangoora_gwangyang` (`--stippel`) | ja — geen net op deze korrel |
| b3 | A | truck | GNH-stadsnet → `li-porthedland-utahpoint` | GNH → Utah Road | 8,7 gebakken (25 = profielwaarde, geen toets) [7] | letterlijke kopie `lithium-pilgangoora-gwangyang-weg-southhedland-utahpoint.geojson` | nee |
| b4 | B | zee (stippel) | Utah Point → zeeknoop 3883 | haven-aanloop | 80,5 gebakken | letterlijke kopie `…-aanloop-utahpoint.geojson` (`--stippel-geojson`) | ja — MARNET reikt niet (79,7 km) |
| b5 | B | zee (bulkcarrier) | zeeknoop 3883 (-19.6000, 118.6000) → Yangtze-monding (routeerpunt 31.4074, 121.4848) | Lombok–Makassar–Taiwanstraat (MARNET beslist) | 6.049,3 gemeten (proefrun 2026-10-09; geen publicatie) | MARNET; aannemelijk: één bron in de beennaam | nee |
| b6 | B | zee (stippel) | MARNET-eindknoop 31.51, 121.4187 → bulklaag 31.4512, 121.4769 | — | 8,6 | letterlijke kopie `bak_lithium` (`--stippel`) | ja — net reikt niet |
| b7 | B | binnenvaart (zelfde zeeschip) | Yangtze-bulkknoop (31.4512, 121.4769) → bulk-eind (32.2200, 119.5508) | Yangtze, zuidgeul langs Shiyezhou, dan noordwaarts | 250,1 gemeten (35 edges) | `maak_rivierbeen.py` (proefrun gelukt, geen kopie) | nee |
| b8 | B | binnenvaart (stippel) | bulk-eind (32.2200, 119.5508) → `li-zhenjiang-kade` | open water NW-waarts langs het kadefront | 4,58 hemelsbreed | rechte `--stippel`, op z14 over open water gezien | ja — bulklaag reikt niet (4,6 km); anker ≠ routeerpunt |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-wodgina-plant` | mijn / concentratorplant | Wodgina — verwerkingsplant, drie treinen (MinRes/Albemarle) | -21.1811, 118.6752 | [1][5] + sat z16 | bron-gelegd (z16 gezien: industrieel complex met tanks en transportbanden, indikkerdome 0,5 km ZW, twee open putten ZO; Wikipedia-coördinaat valt erop. Sitelaag `w-li-wodgina` (-21.1912, 118.6711) ligt 1,2 km ZZW op een putrand, 10-K-DMS (-21.1903, 118.6736) 1,1 km Z — beide binnen 2 km, geen eigen been) |
| `li-porthedland-utahpoint` | laadkade (bulk) | Utah Point Bulk Handling Facility, Berth 4 | -20.3153, 118.5585 | hergebruik: lithium-pilgangoora-gwangyang §3 | aannemelijk (zelfde publieke bulkfaciliteit als Pilgan; MinRes noemt geen berth [1]) |
| `li-yangtze-monding` | overgang zee → rivier | Yangtze-monding (Wusong/Luojing) | 31.42704, 121.47618 | hergebruik: lithium-bikita-zhangjiagang §3 (routeerpunten 31.4074, 121.4848 / 31.4512, 121.4769) | bestaand anker |
| `li-zhenjiang-kade` | losplek (stoppunt) | Xinminzhou-haven, Zhenjiang — bulkkade met pier | 32.2540, 119.5233 | [3][4] + sat z14/z16 | aannemelijk (z16 gezien: pier/kaderand aan de hoofdgeul met bulkschepen langszij, houtstapels en loodsen erachter; welke terminal Albemarles lading krijgt is niet vastgesteld, havenkantoor 32.2795, 119.5471 is niet de kade) |

## 4 · Via-punten (alleen b1; lat, lon uit OSRM-geometrie over OSM, nog op een trunk-vertex te projecteren)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Wodgina Access Road, midden | -21.1622, 118.6791 | verlaat de plant via de enige aansluitweg [6] i.p.v. een interne haul road |
| b1 | 2 | Access Road × Great Northern Hwy | -21.1309, 118.7060 | pint de afslag naar het noorden (Port Hedland) i.p.v. GNH zuidwaarts naar Newman |
| b1 | 3 | GNH, ~60 km ten N van de afslag | -20.7103, 118.4912 | houdt de doorgaande GNH aan i.p.v. een sluipweg door de Pilbara-mijnwegen |
| b1 | 4 | GNH vóór het graafgat (zuidzijde) | -20.377913, 118.575136 | = eindanker van b1, gemeten OSM-gat (kopie pilgangoora) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Wodgina-concentrator (3 treinen: kogelmolen, flotatie, magneetscheiding) | MARBL JV: MinRes 50 % (operator) / Albemarle 50 % | erts → spodumeenconcentraat 5,5–6 % Li2O | 750 kt SC/j ≈ 100 kt LCE; Albemarle-aandeel 2025 = 8 kt Li | [1][2] |
| Zhenjiang-afhaalpunt → Albemarle-converter | Albemarle (niet getekend) | concentraat → carbonaat/hydroxide (Qinzhou, Meishan, Xinyu: Albemarle-fabrieken) | Qinzhou-capaciteit niet gepubliceerd | [2] |

## 6 · Stoppunt
De brief stopt op de Xinminzhou-kade: Albemarle biedt zijn Wodgina-concentraat aan met afhaalpunt Zhenjiang (veiling 05-03-2025 FCA Zhenjiang Xinminzhou Port [3]; 30-07-2026 14.700 dmt, pickup Zhenjiang Port [4]), maar de afnemer is onbekend en geen bron noemt een landbeen naar een fabriek — fase C/D/E vervalt. **Het ontwerpeindpunt Qinzhou is niet bewezen**: het 10-K noemt Qinzhou alleen als bestemming van Greenbushes-concentraat [2], MinRes zegt voor Wodgina alleen "global markets" [1].

## 7 · Open punten
- **Qinzhou niet bewezen:** geen bron koppelt Wodgina-concentraat aan Qinzhou; het fabrieksanker (Haitian Road 6) is nergens gevonden en wordt niet getekend. Id blijft `…-qinzhou` zolang de keten niet centraal is hernoemd (voorkeur orkestrator: `lithium-wodgina-zhenjiang`, registersleutel dan `li-wz`).
- **Terminal in Xinminzhou niet vastgesteld** (kade 32.2540, 119.5233 = aannemelijk); de SMM-pagina noemt alleen "Zhenjiang Port" [4], de Albemarle-pagina (alleen via zoekresultaat gelezen, 403) "Zhenjiang Xinminzhou Port" [3]; de veiling van jan 2026 (~17,8 kt) komt uit de haalbaarheidstoets en is niet zelf gecontroleerd.
- **Wegkilometer b1 ongepubliceerd:** 10-K geeft ligging (~110 km SSE), Wikipedia 90 km zuid [5]; de ±15 %-toets is indicatief (OSRM 103,9 km).
- **b1 overlapt 91 % met het Pilgangoora-been** op de GNH: twee lijnen op dezelfde weg, bewust (andere mijn).
- **Utah Point-berth voor Wodgina onbevestigd**; Lumsden Point (medio 2026) mogelijk alternatief — zie pilgangoora-brief.
- **Yangtze-pad** door de bulklaag volgt de zuidgeul en eindigt 4,6 km vóór de kade; b8 is een rechte stippel over open water, geen hand-gelegde vaargeul.
- **Sitelaag-centroïde `w-li-wodgina`** ligt 1,2 km van de plant (putrand) — centraal gelijk te trekken met `li-wodgina-plant`.
- Geen bron voor het aandeel dat via Zhenjiang gaat; veilingen beslaan alleen Albemarles helft, MinRes' helft ongedocumenteerd.

## 8 · Bronnen
[1] MinRes, Wodgina — 750 ktpa SC5,5, drie treinen, "transported by road to Port Hedland for export to global markets", 50/50 JV. https://www.mineralresources.com.au/our-business/lithium/wodgina/
[2] Albemarle 10-K FY2025, Item 2 — Wodgina ~110 km SSE van Port Hedland (21°11'25"S, 118°40'25"E), NH1 → NH95 → Wodgina camp road, alle wegen verhard; productie 8 kt Li (2025); Qinzhou/Meishan/Xinyu "Owned". https://www.sec.gov/Archives/edgar/data/915913/000091591326000018/alb-20251231.htm
[3] Albemarle, Bidding Events: Spodumene Concentrate, 05-03-2025 — 15.804,61 dmt, FCA Zhenjiang Xinminzhou Port, origin Wodgina. https://www.albemarle.com/us/en/event/2025-03-05/bidding-events-spodumene-concentrate
[4] SMM, 30-07-2026 — Albemarle-veiling 14.700 dmt Wodgina-concentraat, SC6 CIF $2.113/t, pickup Zhenjiang Port. https://news.metal.com/en/newscontent/104033823-albemarle-auction-result-14700-dmt-spodumene-concentrate-sold-at-cif-sc6-2113ton
[5] Wikipedia, Wodgina mine — 90 km ten zuiden van Port Hedland, coördinaat -21.181141, 118.675201. https://en.wikipedia.org/wiki/Wodgina_mine
[6] Stantec, Great Northern Highway Intersection and Wodgina Access Road — 9 km toegangsweg + kruispunt. https://www.stantec.com/en/projects/australia-projects/g/great-northern-highway-intersection-and-wodgina-access-road
[7] Brief lithium-pilgangoora-gwangyang (§2–§4, §9) — Utah Point-anker, GNH-gat 0,355 km, kopiebestanden b2–b4. v2/design/routebrieven/lithium-pilgangoora-gwangyang.md
[8] Brieven lithium-bikita-zhangjiagang en lithium-greenbushes-zhangjiagang — Yangtze-monding, overgangsstippel 8,6 km. v2/design/routebrieven/
[9] OSRM (OSM-wegrouting), 2026-10-09: plant (-21.1811, 118.6752) → GNH South Hedland 103,9 km, via Wodgina Access Road en NH95; indicatie, geen publicatie. https://router.project-osrm.org
[10] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16, live, 2026-10-09): `v2/build-cache/satcheck/sat-lithium-wodgina-qinzhou-wodgina-site.png`, `…-wodgina-plant.png`, `…-kade-z16.png`, `…-aanloop-z14-pad.png`, `…-rivier-overzicht-pad.png`.
[11] `v2/design/lithium-sitelaag.json` — `w-li-wodgina`, 100 kt LCE nameplate.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Recept:** `bash v2/tools/bak_stromen.sh lithium-wodgina-qinzhou` (functie `bak_lithium_wodgina_qinzhou`) → `v2/data/stroomroute-lithium-wodgina-qinzhou.json` (49,2 KB, versie 2, punt_formaat lonlat). **Totaal 6.506,4 km · 2.488 punten · 4 markers · 8 benen · alle naden 0,000 km.** Eindpunt **Zhenjiang (Xinminzhou-haven)**, niet Qinzhou (id blijft; registerlabel noemt Zhenjiang).

| # | modaliteit | km gebakken | punten | stippel | bron van de geometrie |
|---|---|---|---|---|---|
| b1 | truck | 104,3 | 442 | nee | nieuw profiel `lithium-wodgina-qinzhou-plant-southhedland` (maak_stroombeen_weg, extract australie, Overpass-bron) → `lithium-wodgina-qinzhou-weg-plant-southhedland.geojson` |
| b2 | truck | 0,355 | 2 | ja — OSM-topologiegat | letterlijke kopie `--stippel` uit bak_lithium_pilgangoora_gwangyang |
| b3 | truck | 8,7 | 51 | nee | letterlijke kopie `lithium-pilgangoora-gwangyang-weg-southhedland-utahpoint.geojson` |
| b4 | zee | 80,5 | 73 | ja — MARNET reikt niet (79,7 km) | letterlijke kopie `lithium-pilgangoora-gwangyang-aanloop-utahpoint.geojson` |
| b5 | zee | 6.049,3 | 628 | nee | MARNET (42 edges; zeeknoop 3883 → Yangtze-routeerpunt; eindsnap 13,0 km naar knoop 31.51,121.4187) |
| b6 | zee | 8,6 | 2 | ja — net reikt niet | letterlijke kopie `--stippel` uit bak_lithium |
| b7 | binnenvaart | 250,0 | 1.288 | nee | `lithium-wodgina-qinzhou-rivier-yangtze-xinminzhou.geojson` (maak_rivierbeen.py, proefrun hergebruikt) |
| b8 | binnenvaart | 4,6 | 2 | ja — bulklaag reikt niet | rechte `--stippel` over open water (z14 gezien) |

**Toets (handleiding §5).** b1 104,3 km tegen de indicatie 110 (hemelsbreed, geen wegkm) = −5,2 % en tegen OSRM 103,9 km = +0,4 % [OK, indicatief]; geen keerlussen gesnoeid; segmenten 2,9 + 4,6 + 52,8 + 43,9 km (afrit plant → Access Road-midden → GNH-afslag → GNH ~53 km N → graafgat). Totaal 6.506 km tegen de verwachte ~6.515 (b1 is 9 km korter dan de 113 uit het ontwerp). Naden: alle 0,000 km (b1/b2, b2/b3, b3/b4, b4/b5 op −19,6/118,6, b5-eind/b6, b6/b7, b7/b8). Markers: Utah Point 0,000 km, Xinminzhou-kade 0,000 km, plant 0,095 km, Yangtze-monding 2,672 km van de lijn (zie hieronder). `toets_knikken`: 7 knikken ≥ 60°, 0 omkeringen, 0 terugloop; de drie op b1 (−21.1316/118.7062 de T-kruising Access Road × GNH, 92,8°; −20.3909/118.5765, 88,8°; −21.1704/118.6754, 82,5° bij de plant) zijn echte afslagen/plantgeometrie, geen lus. `toets_rechte_benen --min-km 5`: alleen b6 (stippel, bekend). json.load: versie 2, modaliteiten {truck, zee, binnenvaart}, elk been ≥ 2 punten.

**Toelichting per stippel/aanloop.**
- **b2** — de twee GNH-componenten bij South Hedland delen geen knoop (0,355 km); gemeten, niet dichtgetrokken. Zelfde bestand en zelfde coördinaten als Pilgangoora.
- **b4** — Utah Point ligt 79,7 km van zeeknoop 3883 (AU-binnenkant heeft geen MARNET-graaf); de aanloop is een kortste-pad-over-water uit maak_havenaanloop.py (geen tweede poging gedaan, bestand hergebruikt).
- **b6** — MARNET eindigt op 31.51,121.4187; de bulklaag begint op 31.4512,121.4769. Letterlijke kopie.
- **b8** — de bulklaag eindigt 4,6 km vóór de kade; de rechte lijn is op z14 gecontroleerd en ligt over open water langs het kadefront (niet door de zandbank/kaap). Geen hand-gelegde vaargeul.
- Geen luchtbenen, geen spoor, geen leiding, geen fase C/D/E.

**Afwijkingen van het ontwerp / bevindingen.**
1. **Routeanker b1 ≠ plantanker.** Met het plantanker (−21.1811, 118.6752) als eerste via-punt faalde de wegtool met "geen wegpad tussen punt 0 en 1": de plant snapt (0,055 km) op OSM-way 1223332170 (service, 8 vertices), een stub die 73–119 m van de Access Road-component hangt (OSM-topologiegat binnen het plantterrein). Het profiel start daarom op de dichtstbijzijnde knoop van het verbonden net (−21.181825, 118.674628 = begin Wodgina Access Road, ~0,1 km van de plant). De marker blijft op het plantanker; de lijn begint 0,095 km ervandaan (procesgat binnen de verwerkingsknoop, blijft staan).
2. **Wegscan via Overpass, niet Geofabrik.** pyosmium is op deze machine geblokkeerd door toepassingsbeheer (niet omzeild). `--bron overpass` in het gedeelde tool gebruikt twee spiegels die beide 500/time-out gaven; de scan is daarom gedraaid met een wrapper buiten de repo (scratchpad) die dezelfde `_ways_uit_overpass`-vorm levert maar via maps.mail.ru en overpass-api.de in tegels van 0,25° (zelfde `weg_houden`-filter, query beperkt tot dezelfde klassen als het filter toelaat). 2.197 ways in de graaf. Eén tegel (−20.08/118.84, ten noorden van het eindanker, niet op de route) bleef falen en is overgeslagen. Het resultaat is niet getoetst tegen een Geofabrik-scan; de indicatie is wel OSRM (103,9) ↔ 104,3 km.
3. **Marker Yangtze-monding ligt 2,67 km van de lijn:** bestaand anker 31.42704, 121.47618 (hergebruikt letterlijk, zoals lithium-bikita-zhangjiagang), de lijn loopt via de overgangsstippel (31.51, 121.4187 → 31.4512, 121.4769). Anker ≠ routeerpunt, geen fout.
4. **Wegkilometer b1 ongepubliceerd:** de ±15 %-toets is alleen indicatief (10-K geeft hemelsbreed ~110 km); b1 overlapt ~91 % met het Pilgangoora-been op de GNH, bewust.
5. **Eindpunt Zhenjiang, niet Qinzhou** (zie §6/§7); bestemming aannemelijk: één bron (Albemarle-veilingen) en in de beennamen b5/b7/b8 vermeld.

**Lessen.**
- Een plantanker kan op een losse OSM-stub van een paar vertices snappen: lees bij "geen wegpad" eerst de componentgrootte van het anker voordat je een via-punt aanpast; hier was het een routeanker op het verbonden net, geen via-punt-bijschuiving.
- Een Overpass-tegelwrapper met schijfcache en vaste rasteroorsprong is robuust tegen 504's; kies de tegelrand-oorsprong niet uit het profiel (een ankerwijziging van 1 m verschoof anders het hele raster en maakte de cache ongeldig).
- Het slot-semafoorscript van de kaart gebruikt `rm -rf "$d"`, dat de veiligheidscheck blokkeert; mkdir-acquire met `rmdir` als release werkt gelijkwaardig.
