# Routebrief (licht) · gas — Tangguh → Fujian LNG-terminal bij Putian (China)

**stroom-id:** `gas-tangguh-putian` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** LNG van Tangguh LNG (BP, Bintuni-baai, West-Papoea) gaat per **LNG-carrier** over de Ceramzee, Molukken-/Celebeszee, Soeloezee, de Zuid-Chinese Zee en de Straat Taiwan naar de Fujian LNG-terminal (CNOOC) in Meizhou-baai bij Putian — zee-keten, geen landbenen.
**Welke as van het verhaal:** *Indonesisch LNG naar China, Tangguh → Fujian.* Contract 25 jaar, **2,6 Mtpa ≈ 3,5 bcm/j** (BP/CNOOC, 2002/2009) [1][2]; eerste Tangguh-lading naar Fujian juli 2009 [1]. Actuele doorzet van déze lading niet gevonden; de terminal ontving in 2024 in totaal ca. 3,7 Mt uit alle herkomsten [5]. Aannemelijk: één bron (contract) plus één gevolgde lading (dec 2024).

## 1 · Ketenkaart
```
Tangguh LNG-plant (Bintuni-baai) ── eigen steiger, ~1,3 km trestle ── LNG-steiger `gas-tg-steiger`
   ──(b1 zee · haven-aanloop, stippel · ~220,8 km)──► zeeknoop 2569 (-3.0000,131.4000, Ceramzee)
   ──(b2 zee · Ceramzee → Molukkenzee → Celebeszee → Soeloezee → Mindorostraat → Zuid-Chinese Zee → Straat Taiwan
       · 3.732,2 km tussen zeeknopen, MARNET · aannemelijk: één bron)──► zeeknoop 5586 (25.0955,118.9641)
   ──(b3 zee · haven-aanloop, stippel · 13,8 km)──► Fujian LNG-kade `gas-fj-kade` (Meizhou-baai, Putian) ⏹ stoppunt
```
Totaal 3.966,8 km (gemeten test-bake), waarvan stippel 234,6 km (5,9%); hemelsbreed kade → kade 3.430 km.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `gas-tg-steiger` → zeeknoop 2569 | haven-aanloop Berau-/Bintuni-baai, langs de noordkust van het Onin-schiereiland | 220,8 [eigen meting, detour] | `bake_marnet.detour` cel 0,03 (zie §7) | ja — MARNET reikt niet: dichtstbijzijnde zeeknoop op 202,8 km |
| b2 | B | zee | zeeknoop 2569 → zeeknoop 5586 | Ceramzee → Molukkenzee → Celebeszee → Soeloezee → Mindorostraat → Zuid-Chinese Zee → Straat Taiwan | 3.732,2 [test-bake `hecht_marnet route`; ontwerp ~4.000 indicatief] | MARNET | nee (aannemelijk: één bron, staat in de beennaam) |
| b3 | B | zee | zeeknoop 5586 → `gas-fj-kade` | haven-aanloop Meizhou-baai | 13,8 [maak_havenaanloop.py, 0,00 km land] | `maak_havenaanloop.py` | ja — kade 13,0 km van de zeeknoop (> 5 km-regel) |

Fase A (offshore Tangguh-velden Wiriagar/Ofaweri/Vorwata → plant) en C (regas Fujian → gasnet) worden niet getekend: geen enkelvoudig anker voor het offshore veld, en voor het Fujian-gasnet noemt geen bron een invoedingspunt. Fase D/E vervallen.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-tg-steiger` | overslag plant → zee (laadkop) | Tangguh LNG-steiger (oostelijke trestle, schip aan de kop) | -2.4256, 133.1331 | [3][6][7][8] | bron-gelegd (z15/z16 gezien: een LNG-carrier ligt langs de kop van de oostelijke ~1,3 km lange trestle die van het plantterrein de baai in loopt; sitelaag-punt `w-tangguh` -2.4372,133.1361 valt op de bolvormige LNG-tank van het plantterrein, 1,4 km zuidoost van de steiger) |
| `gas-fj-kade` | overslag zee → regas | Fujian LNG-terminal (CNOOC), steigerkop Meizhou-baai | 25.2090, 118.9962 | [4][8][10] | bron-gelegd (z15/z16 gezien: zes bolvormige LNG-tanks aan de noordoever, een ~400 m trestle zuidwaarts naar een laadplatform met meerpalen; GEM-punt 25.2135,118.9983 en OSM-way 1086903630 25.2129,118.9971 liggen op het tankterrein) |

Hergebruik: geen — Tangguh en Fujian komen in geen andere brief of stroom voor. `w-tangguh` in `gas-sitelaag.json` blijft ongewijzigd (zie §7).

## 4 · Via-punten
Geen — alleen zeebenen; MARNET routeert zeeknoop → zeeknoop, b1 en b3 zijn vooraf gebakken aanloop-lijnen.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Tangguh LNG (Train 1-3) | BP Berau (met MI Berau 16,3%, **CNOOC Muturi 13,9%**, e.a.) | aardgas → LNG | 11,4 Mtpa ≈ **15,5 bcm/j** (3 trains, Train 3 sinds 2023) | [3][6][7] |
| Fujian LNG-terminal | CNOOC Fujian LNG Co (CNOOC 60% / Fujian Investment 40%) | LNG → hervergast gas | 6,3 Mtpa ≈ **8,6 bcm/j** (fase I 2,6 + fase II 3,7); 6 tanks van 160.000 m³; 2024 ca. 3,7 Mt ontvangen | [4][5] |

## 6 · Stoppunt
De brief stopt bij de Fujian LNG-kade: het hervergaste gas gaat het Fujian-gasnet in, en geen bron noemt een invoedingspunt of een afnemende fabriek; fase C/D/E vervallen.

## 7 · Open punten
- **Werkelijke doorzet Tangguh → Fujian 2024-25 niet gevonden.** Bekend: contract 2,6 Mtpa [1][2], eerste lading juli 2009 (Min Rong, 138.000 m³) [1], en een lading van de Maran Gas Posidonia die op 31-12-2024 losde en volgens een samenvatting van LNG Prime (paywall; alleen het begin gelezen) in Tangguh was geladen [5]. Het cijfer 3,5 bcm/j is dus de contractwaarde, geen gemeten stroom.
- **Eerste Fujian-lading kwam uit Bontang, niet Tangguh** (OGJ, mei 2009: Tangguh liep vertraagd) [2] — de Tangguh-lading is die van juli 2009 [1].
- **Welke Tangguh-steiger de Fujian-lading laadt is niet bron-bevestigd.** Op z15 liggen drie trestles naast elkaar (west-kop -2.4347,133.1142; midden-kop -2.4276,133.1259; oost-kop met carrier -2.4256,133.1331); een jetty is nieuw bij Train 3 (JOGMEC 2016) [6]. Gekozen is de steiger waar een carrier ligt; verschil tussen de koppen ≤ 1,9 km.
- **Corridor volgens MARNET wijkt af van het ontwerp.** Het ontwerp noemde Halmahera, de Filipijnenzee en de Straat Luzon; MARNET gaat via de Celebes-/Soeloezee en de Mindorostraat de Zuid-Chinese Zee in (lon 121,7 bij lat 10,0; lon 120,0 bij lat 20-22). Echte carrierroute onbekend; geen gepubliceerde zeekm, de ±15%-toets is hier indicatief (3.967 km totaal tegen ontwerp ~4.000).
- **Haven-aanloop Tangguh is schematisch.** `maak_havenaanloop.py` liep vast op de 300 s-time-out (exit 124, eigen meting 2026-10-31); terugval op `bake_marnet.detour` (cel 0,03° gebufferd, 220,8 km, 0,00 km land) en visueel gecontroleerd op een Esri z9-overlay (`sat-gas-tangguh-putian-aanloop-overlay2.png`): het pad volgt de geul door de baaimond en blijft op ~4-14 km van beide oevers. De bevaren geul is niet gemeten; blijft stippel.
- **`w-tangguh` (sitelaag, status "onzeker, veldcentroïde") ligt in werkelijkheid op het plantterrein** (bolvormige LNG-tank gezien op z15); een upgrade naar bron-gelegd is aan de orkestrator, niet aan deze brief.
- **Twee ontwerppunten zijn niet gebruikt:** Wikidata -2.4417,133.1361 ligt op het plantterrein, en het steigerpunt -2.4350,133.1112 uit de haalbaarheidstoets ligt ca. 330 m ten westen van de west-kop in open water (geen steiger).
- **Hanas Putian LNG** (GEM, voorgesteld 5,65 Mtpa) is een ander project dan de CNOOC-terminal in Meizhou-baai.

## 8 · Bronnen
[1] Petromindo, "Tangguh starts LNG shipment to Fujian", 2009 — Min Rong (138.000 m³) vertrok 19-07-2009; 2,6 Mtpa; Tangguh-belangen. https://www.petromindo.com/news/article/tangguh-starts-lng-shipment-to-fujian
[2] OGJ, "CNOOC receives first shipment of Indonesian LNG", 29-05-2009 — eerste lading uit Bontang; 25-jarig contract 2,6 Mtpa uit Tangguh. https://www.ogj.com/pipelines-transportation/article/17278168/cnooc-receives-first-shipment-of-indonesian-lng
[3] Wikipedia, "Tangguh gas field" — Berau Gulf/Bintuni-baai; CNOOC Muturi 13,9%; productie sinds juni 2009. https://en.wikipedia.org/wiki/Tangguh_gas_field
[4] Global Energy Monitor, "Fujian LNG Terminal" — 25.2135,118.9983; fase I 2,6 + fase II 3,7 Mtpa; CNOOC 60% / Fujian 40%. https://www.gem.wiki/Fujian_LNG_Terminal
[5] LNG Prime, 08-01-2025, "China's CNOOC boosts Fujian LNG volumes in 2024" — Maran Gas Posidonia, 31-12-2024; (uit samenvatting van de pagina: 60 schepen, >3,7 Mt in 2024, 6 tanks, 6,3 Mtpa; paywall). https://lngprime.com/asia/chinas-cnooc-boosts-fujian-lng-volumes-in-2024/137285
[6] LNG Industry, "JOGMEC supports Tangguh LNG Project expansion", 11-08-2016 (nieuwe LNG-jetty bij Train 3); Engineering News, "Tangguh Train 3 update", 27-10-2023 (11,4 Mtpa). https://www.lngindustry.com/liquefaction/11082016/JOGMEC-supports-Tangguh-LNG-Project-expansion-2894 · https://engineeringnews.co.za/article/tangguh-liquefied-natural-gas-project-train-3-indonesia-update-2023-10-27
[7] `v2/design/gas-sitelaag.json`, site `w-tangguh` — 11,4 Mtpa × 1,36 = 15,5 bcm/j; coördinaat -2.43722,133.13611.
[8] Esri World Imagery via `v2/tools/sat_check.py` (live, 2026-10-31) — `sat-gas-tangguh-putian-tangguh-steiger.png`, `-tangguh-oostsupsteiger.png`, `-tangguh-westsupsteiger.png`, `-fujian-kade.png`, `-fujian-kop.png`, `-fujian-terminal.png`, `-aanloop-overzicht.png`, `-aanloop-overlay2.png` (in `v2/build-cache/satcheck/`).
[9] `v2/build-cache/marnet-preais` (zeeknopen, `hecht_marnet.marnet_zee`) — knoop 2569 op 202,8 km van de Tangguh-steiger; knoop 5586 op 13,0 km van de Fujian-kade; test-bake `hecht_marnet.py route` 3.732,2 km.
[10] OSM way 1086903630 "FUJIAN LNG-terminal" 25.2129,118.9971 — uit de haalbaarheidstoets van deze golf, niet opnieuw opgehaald.
[11] Ketenontwerp + haalbaarheidstoets M31 golf 19 (workflow-invoer) — Petromindo/OGJ-webcheck, aanpassing ankers.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
Recept: functie `bak_gas_tangguh_putian` in `v2/tools/bak_stromen.sh`; draaien met `bash v2/tools/bak_stromen.sh gas-tangguh-putian`; uitvoer `v2/data/stroomroute-gas-tangguh-putian.json` (8,8 KB, contract versie 2, punt_formaat lonlat).

| # | modaliteit | been | km | punten | stijl |
|---|---|---|---|---|---|
| b1 | zee | haven-aanloop Tangguh LNG-steiger → zeeknoop 2569 (vooraf gebakken `gas-tangguh-putian-aanloop-tangguh.geojson`) | 220,8 | 58 | stippel |
| b2 | zee | LNG-carrier Tangguh LNG → Fujian LNG (aannemelijk: één bron), MARNET zeeknoop 2569 → 5586, 23 edges | 3.732,2 | 387 | doorgetrokken |
| b3 | zee | haven-aanloop Fujian LNG, zeeknoop 5586 → kade (`gas-tangguh-putian-aanloop-fujian.geojson`) | 13,8 | 12 | stippel |

Totaal **3.966,8 km**, 457 punten, naden 0,0 km, 2 markers (`gas-tg-steiger` -2,4256/133,1331 en `gas-fj-kade` 25,2090/118,9962, beide op de lijn, 0,0 km). Geen via-punten, geen extract, geen kopie, geen last mile.

**Stippel:** b1 omdat MARNET niet reikt (zeeknoop 202,8 km van de steiger; maak_havenaanloop.py gaf exit 124, terugval `bake_marnet.detour`; bevaren geul niet gemeten); b3 omdat de kade 13,0 km van zeeknoop 5586 ligt (> 5 km-regel; aanloop gelukt, 0,00 km land). b2 is doorgetrokken; "aannemelijk: één bron" staat in de beennaam.

**Toets:** km b2 3.732,2 tegen ontwerp ~4.000 indicatief (geen gepubliceerde zeekm; de MARNET-corridor loopt via Celebes-/Soeloezee en Mindorostraat); geen naad > 5 km; zee-benen kruisen 0 km land (shapely tegen ne_10m_land); toets_knikken: 1 knik 70,2 gr bij 6,906/121,863 (Soeloezee, krappe bocht R 7,9 km), 0 omkeringen, 0 terugloop; grootste segment 10,0 km (b2).

**Lessen:** het stroom-id noemt het werkelijke eindpunt (Fujian LNG, Putian); een haven-aanloop op 200 km valt buiten maak_havenaanloop.py (time-out) en kan alleen als detour-lijn, dus stippel; Tangguh-steiger = oostelijke trestle waar een carrier ligt, welke trestle de Fujian-lading laadt is niet bron-bevestigd.
