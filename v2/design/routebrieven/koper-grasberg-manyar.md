# Routebrief (licht) · koper — Grasberg → Manyar (Gresik)

**stroom-id:** `koper-grasberg-manyar` · **geschreven:** 2026-09-24 · **werkwijze:** licht (M29) · **status:** concept · **Linear:** LAR-557
**Keten in één zin:** koper-goudconcentraat van de Grasberg-mill (PT Freeport Indonesia, ~2.900 m, Papoea) als slurry door drie parallelle **leidingen** van 115 km naar Portsite/Amamapare aan de Arafurazee (filteren, drogen, loods), per **zeeschip** naar de PTFI-smelter Manyar in het JIIPE-industriegebied bij Gresik (Oost-Java) — alternatief PT Smelting Gresik — daar tot **kathode**, en (aannemelijk, één bron) per **truck** binnen JIIPE naar de koperfoliefabriek van Hailiang.
**Welke as van het verhaal:** *Indonesische downstreaming* — Grasberg-concentraat naar de eigen binnenlandse smelters i.p.v. export. PTFI produceert ~3,0 Mt concentraat/jaar (raming 2025: 2,964 Mt, waarvan 1,45 Mt export onder vergunning [9]); binnenlandse smeltcapaciteit 3,0 Mt = Manyar 1,7 [6][7] + PT Smelting 1,3 [11]. 2026 ligt lager door de gefaseerde herstart van de Grasberg Block Cave na de modderstroom van 08-09-2025 (guidance 2026 ≈ 1,0 mrd lb Cu; 2027–29 gem. 1,6 mrd lb) [8].

## 1 · Ketenkaart
```
Grasberg-mill `cu-grasberg-mill` ──(b1 leiding · mijnweg Tembagapura–Timika–Portsite · 3 × 115 km, stippel)──► Portsite `cu-portsite-kade`
   (ontwateren → loods 135 kt → laden aan de steiger, afladen op Sea Buoy A met bakken)
   ──(b2 zee · Arafura–Banda–Flores–Javazee · ~2.690 km hemelsbreed, MARNET)──► Manyar-kade `cu-manyar-kade` (JIIPE, Gresik)
   ═══ knoop: PTFI Manyar-smelter `cu-manyar-smelter` (1,7 Mt in → ~480 kt kathode) ═══
   ├── alternatief: PT Smelting Gresik `cu-gresik-ptsmelting` (1,3 Mt in) — 6 km zuidelijker, zelfde zeebeen
   ├── vertakking (niet getekend): concentraatexport onder vergunning (2025: 1,27 Mt vergund [10]) naar smelters in Japan, China, India, Spanje (Atlantic Copper)
   ──(b3 truck · binnen JIIPE · ~2 km, aannemelijk: één bron)──► Hailiang koperfolie `cu-hailiang-fabriek` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding (slurry, 65 % vaste stof) | Grasberg-mill → Portsite-kade | leiding- en wegcorridor mill → Tembagapura → Timika → Portsite ("116 km road and pipeline") | 115 [1][3] | stippel "leiding" via 4 via-punten (§4); OSM heeft géén `man_made=pipeline` in de bbox [16] | ja — net reikt niet (leiding niet gekarteerd); via-keten meet ~90 km hemelsbreed, bergtraject met haarspelden zit er niet in |
| b2 | B | zee | Portsite-kade → Manyar-kade | — (eerste lading 14-06-2024: MV Unitama Lily, 22.000 t, Amamapare → PTFI-smelterhaven JIIPE) [6] | ≈ 2.687 hemelsbreed; gepubliceerd: geen | MARNET | aanloop: waarschijnlijk aan beide kanten (Portsite ligt ~12 km de riviermonding in; JIIPE-pier in de Straat van Madura) |
| b3 | D | truck | Manyar-smelter → Hailiang-foliefabriek (beide in JIIPE) | JIIPE-estateweg | ≈ 1,9 hemelsbreed | maak_stroombeen_weg (als de JIIPE-wegen in het extract zitten, anders stippel "binnen estate") | nee — *aannemelijk: één bron* [14] |

Laadproces Portsite (geen eigen been): schepen laden aan de kade tot de maximale kade-diepgang en worden op dieper water (Sea Buoy A) afgeladen met pendelbakken [1][4] — de drager blijft het zeeschip, dus kade → kade.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-grasberg-mill` | mijn / mill (kop van de leiding) | Grasberg mill- en concentratorcomplex (MP74, ~2.900 m) | -4.0905, 137.1155 | [2][16][17] | bron-gelegd (z15 gezien: gebouwencluster met grote hallen en ronde indikker in het dal 3 km ZO van de Grasberg-put; OSM "HEAT Road" 1,6 km NW) |
| `cu-portsite-kade` | overslag leiding → zee (ontwatering + laadsteiger) | Portsite / Amamapare, PTFI | -4.8290, 136.8405 | [4][5][16][17] | bron-gelegd (z15 gezien: kadefront aan de rivier, zuidzijde van de terreinplaat, tussen de grote loods en de filter-/kilngebouwen, vaartuigen langszij; 354 m van het OSM-landuse-centrum "Portsite") |
| `cu-manyar-kade` | losplek zee | kade-eiland met pier + trestle, oostkust JIIPE | -7.0855, 112.6500 | [6][17] | **onzeker** (z15 gezien: pier en trestle vanaf het smelterperceel, maar de opname is van vóór de oplevering — Wayback 2026-08-05 is dezelfde opname; PTFI-smelterhaven of JIIPE/BMS-haven niet te onderscheiden) |
| `cu-manyar-smelter` | verwerkingsknoop | PTFI Manyar-smelter, KEK JIIPE, Gresik | -7.0890, 112.6270 | [13][16][17] | bron-gelegd (z15 gezien: ~220 ha-perceel in aanbouw aan de oostrand van JIIPE tegen de kust = 100 ha + 120 ha ondersteunend [13]; OSM-knoop "manyar smelter" 1,4 km NO) |
| `cu-gresik-ptsmelting` | alternatieve losplek / smelter | PT Smelting, Roomo, Manyar, Gresik | -7.1400, 112.6400 | [11][12][16][17] | bron-gelegd (z15 gezien: smeltercomplex met schoorstenen en zuurfabriek, eigen steiger naar het NO; OSM-landuse "Smelting" op de NW-hoek) |
| `cu-hailiang-fabriek` | fabriek (fase D) | PT Hailiang Nova Material Indonesia — koperfolie, JIIPE | -7.0740, 112.6194 | [14][15][16] | aannemelijk (OSM-landuse; z14: hallen op het perceel; afname alleen als intentie gebrond) |

## 4 · Via-punten (alleen b1 — de leiding heeft geen net)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Tembagapura (Mile 68) | -4.1424, 137.0907 | de leiding volgt de mijnweg het Aghawagon-dal af, dwars door de mijnstad (OSM-town-node) |
| b1 | 2 | knooppunt mijnweg / Jalan Freeport Lama, N van Timika | -4.4349, 136.9001 | einde bergtraject; de corridor buigt hier naar het zuiden (OSM way 108924824) |
| b1 | 3 | Timika, Jalan Freeport Lama | -4.5389, 136.8956 | de corridor passeert Timika langs de oostzijde van het vliegveld (OSM way 1552793152) |
| b1 | 4 | corridor-aankomst Portsite | -4.8130, 136.8465 | de rechte weg-/leidingcorridor komt uit het NNO het terrein op (z14 gezien [17]) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Portsite-ontwatering | PTFI | slurry 65 % vaste stof → concentraat 9 % vocht | 3 vacuümfilters + 1 persfilter, 3 kilns, loods 135.000 t, > 100 schepen/jaar | [1][4] |
| Manyar-smelter (JIIPE) | PT Freeport Indonesia | concentraat → kathode (+ goud/zilver, H₂SO₄) | 1,7 Mt concentraat/j → ~480 kt kathode/j (PTFI-cijfer via [7]; andere bronnen 600–650 kt) | [6][7] |
| PT Smelting (Roomo) | PT Smelting (Mitsubishi Materials / PTFI) | concentraat → kathode | 1,3 Mt concentraat/j → ~350 kt kathode/j na de uitbreiding van 2023 | [11] |

Status Manyar: brand zuurfabriek 14-10-2024 → herstart juni/juli 2025 → stil sinds Q4-2025 (concentraattekort na de GBC-modderstroom) → concentraatvoeding hervat augustus 2026, kathode sinds september 2026, opvoeren met de mijn (GBC 65 % H2-2026 → 80 % medio 2027 → normaal eind 2027) [7][8].

## 6 · Stoppunt
De brief stopt aan de poort van Hailiang's foliefabriek: de kathode-afname (~100 kt/j) is één keer als intentie gebrond [14], er is geen offtake-contract gevonden, en voor de folie zelf bestaat geen benoemde afnemer — fase E vervalt.

## 7 · Open punten
- **Manyar-loskade niet aanwijsbaar:** de Esri-opname toont het smelterperceel in aanbouw en de nieuwste Wayback-release (26334, 2026-08-05) is dezelfde opname → uitsluiting op opnamedatum. Het pier-anker `cu-manyar-kade` blijft *onzeker*; het zeebeen mag ook op het terreinanker eindigen met een procesgat van 2,6 km. Vraagt een niet-Esri-bron.
- **Leiding niet in OSM** (Overpass 2026-06, 0 × `man_made=pipeline`) → stippel via 4 punten, ~90 km i.p.v. 115 km gepubliceerd. De OSM-mijnweg ("Timika to Tembagapura Road", "HEAT Road") deelt de corridor en zou als doorgetrokken proxy kunnen dienen — bewust niet gedaan (geleende geometrie); besluit Lars.
- Tussen via 3 en 4 is de stippel een rechte lijn; de echte corridor buigt om het vliegveld van Timika (afwijking enkele km).
- Portsite: welke kadeplek de concentraatlader is, is op z15 niet te onderscheiden; de positie van Sea Buoy A (afladen met bakken) is onbekend — geen anker.
- PT Smelting: alleen een terreinanker; de steigerkop (concentraatlossing) is niet gelegd. Aandeel Manyar vs PT Smelting per lading onbekend (eerste lading: 12 kt / 10 kt [6]).
- Kathodecapaciteit Manyar: bronnen lopen van 480 tot 650 kt/j; hier het PTFI-cijfer 480 kt aangehouden.
- Exportvertakking per land (Japan/China/India/Spanje) is niet per land gebrond (zoekbudget op); alleen genoemd, niet getekend.
- b3 bestaat als intentie (2024); Hailiang draait sinds 2024 (proefexport) met fase 1 = 50 kt folie/j [15]. Of de JIIPE-estatewegen in het OSM-extract zitten blijkt bij het bakken.

## 8 · Bronnen
[1] Freeport-McMoRan, Form 10-K FY2003 — "three parallel 115-kilometer pipelines", slurry ~65 % solids, laden aan de kade + pendelbakken. https://www.sec.gov/Archives/edgar/data/0000831259/000083125904000007/f10k2003.htm
[2] Freeport-McMoRan, Form 10-K FY2022 — mill op ~2.900 m, maalcapaciteit naar ~240.000 t erts/dag. https://www.sec.gov/Archives/edgar/data/831259/000083125923000013/fcx-20221231.htm
[3] Mining Technology, Grasberg Open Pit — "116 km road and pipeline", drie leidingen naar Amamapare. https://www.mining-technology.com/projects/grasbergopenpit/
[4] PT Freeport Indonesia, Drying & Shipping — filters, kilns, loods 135.000 t, concentraatsteiger + Sea Buoy A, > 100 schepen/jaar. https://ptfi.co.id/en/drying-and-shipping
[5] Shipnext, Amamapare IDAMA — -4,8333/136,85; LOA 250 m; diepgang 4,0 m + tij; bar 6,7 m. https://shipnext.com/port/581fd9b354e6080aa866a85a
[6] PTFI, 14-06-2024 — eerste lading MV Unitama Lily 22.000 t naar de PTFI-smelterhaven in KEK JIIPE; capaciteit 1,7 Mt. https://ebk.ptfi.co.id/highlight-news/freeport-delivers-first-shipment-of-copper-concentrate-to-its-new-smelter
[7] SMM, 17-09-2026 — Manyar herstart (voeding aug, kathode sep 2026), 1,7 Mt in / ~480 kt kathode, GBC-herstelpad. https://news.metal.com/newscontent/104119501-freeport-indonesia-restarts-manyar-copper-smelter-as-gbc-mine-recovery-supports-gradual-ramp-up
[8] Freeport-McMoRan, update herstartplan Grasberg (2025) — GBC-herstart Q2-2026, 2026 ≈ 1,0 mrd lb Cu, 2027–29 gem. 1,6 mrd lb. https://investors.fcx.com/investors/news-releases/news-release-details/2025/Freeport-Provides-Update-on-Restart-Plans-for-Grasberg-Minerals-District/default.aspx
[9] Reuters via TradingView, 2025 — PTFI concentraatproductie geraamd 2,964 Mt, export 1,45 Mt. https://tw.tradingview.com/news/reuters.com,2025:newsml_P8N3SR01Y:0-freeport-indonesia-estimates-copper-concentrate-output-at-2-964-mln-tons-exports-at-1-45-mln-tons-in-2025
[10] MarketScreener, 2025 — exportvergunning 1,27 Mt concentraat. https://in.marketscreener.com/quote/stock/FREEPORT-MCMORAN-INC-12574/news/Freeport-Indonesia-says-has-export-permit-for-1-27-million-tons-of-copper-concentrate-49356237/
[11] Mitsubishi Materials, 15-12-2023 — PT Smelting-uitbreiding 1,0 → 1,3 Mt concentraat, kathode ~300 → ~350 kt. https://www.mmc.co.jp/corporate/en/news/2023/news20231215.html
[12] PT Smelting — adres Roomo Village, Manyar District, Gresik. https://www.ptsmelting.com/
[13] JIIPE, Freeport Smelter Development — 100 ha + 120 ha ondersteunend terrein. https://www.jiipe.com/en/home/blogDetail/id/350
[14] Jatimpedia, 30-10-2024 — afnemers: PT Hailiang Group (JIIPE, ~100 kt kathode/j), Antam (goud); kathode-export naar China/Europa. https://jatimpedia.id/smelter-freeport-sudah-berproduksi-ini-pembeli-katoda-tembaga-dan-emas-produksinya/
[15] JIIPE, 2023 — Hailiang Nova Material Indonesia koperfoliefabriek, eerste steen 20-06-2023, fase 1 50 kt/j. https://www.jiipe.com/id/home/blogDetail/id/383
[16] OpenStreetMap (ODbL) via Nominatim/Overpass — landuse "Portsite" -4,8263/136,8388 · landuse "Smelting" -7,1367/112,6371 · landuse "Hailiang Nova Material Indonesia" -7,0740/112,6194 · knoop "manyar smelter" -7,0780/112,6338 · town Tembagapura -4,1424/137,0907 · ways "Timika to Tembagapura Road", "Jalan Freeport Lama", "HEAT Road"; 0 × `man_made=pipeline` in bbox -5,0…-3,9 / 136,6…137,4 (kumi, basis 2026-06-01). https://www.openstreetmap.org
[17] Esri World Imagery via `v2/tools/sat_check.py` (z13–z15, live + Wayback 26334) — `v2/build-cache/satcheck/sat-mill-z15.png`, `sat-portsite-z15.png`, `sat-portsite2-z14.png`, `sat-manyar-z15.png`, `sat-manyar-wb-z15-wb26334.png`, `sat-ptsmelting-z15.png`, `sat-jiipe-z14.png`.


## 9 · Gebakken (2026-09-25. lichte werkwijze)

**Stroom `koper-grasberg-manyar`** → `v2/data/stroomroute-koper-grasberg-manyar.json` — 7 benen. 2.974 km. 6 markers: leiding (stippel) 92 km · zee (stippel) 63 km · zee 2.817 km · truck (stippel) 2 km.
Recept: `bak_stromen.sh` (functie voor deze stroom). Toelichting: de slurryleiding is een schematische stippel langs de HEAT-corridor (89.6 km hemelsbreed over 6 punten; OSM heeft geen pipeline-way); aanloop Portsite 53.2 km over water (stippel); zeebeen MARNET 2.816.7 km; aanloop Manyar 6.7 km (stippel. loskade onzeker); loskade → smelter en fase D naar Hailiang als stippels (eigen terrein resp. aannemelijk); PT Smelting als gestippelde vertakking.
