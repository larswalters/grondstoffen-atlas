# Routebrief (licht) · gas — Ichthys LNG (Darwin, Australië) → Yong'an (Kaohsiung, Taiwan)

**stroom-id:** `gas-ichthys-yongan` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** LNG uit de Ichthys-fabriek op Blaydin Point (Darwin Harbour, Noordelijk Territorium) gaat per **LNG-carrier** door Timor-/Banda-/Celebeszee of Straat Makassar en de Zuid-Chinese Zee naar CPC's Yong'an-terminal in Kaohsiung (Taiwan) — aannemelijk: één bron voor de bestemming, CPC's eigen nieuwsbericht over de eerste lading.
**Welke as van het verhaal:** Taiwan als LNG-eiland — CPC koopt 1,75 Mtpa Ichthys-LNG voor 15 jaar vanaf 2017 [1][2] ≈ **2,4 bcm/j** (1,36 bcm/Mt; contractvolume, geen gemeten jaarstroom). Fabriek 8,9 Mtpa (Wikipedia) ≈ 12,1 bcm/j [4]; de sitelaag heeft 8,4 Mtpa (zelfde Wikipedia-lijst, oudere stand).

## 1 · Ketenkaart
```
Ichthys-gasveld (offshore, 889 km subzee-leiding naar Blaydin Point) — NIET GETEKEND (offshore, geen OSM-way)
   ──(b1 aanloop · stippel · 36,4 km kade → zeeknoop 2572 — maak_havenaanloop, ~41 km over water)──►
Ichthys LNG-kade `gas-ic-kade` (steigerkop, Blaydin Point, Darwin Harbour)
   ──(b2 zee · Beagle Gulf → Timor-/Banda-/Celebeszee of Makassar → Zuid-Chinese Zee → Bashi/Straat Taiwan · 4.457 km MARNET)──►
Yong'an LNG-kade `gas-ya-kade` (ligplaats binnen de golfbreker, Kaohsiung) ⏹ stoppunt
   (b3 aanloop · stippel · 12,9 km zeeknoop 9671 → kade)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee (aanloop) | `gas-ic-kade` → zeeknoop 2572 (-12.2000,130.8000) | Darwin Harbour → Beagle Gulf | ~41 (eigen meting, getest) | maak_havenaanloop.py, timeout 600 | ja — net reikt niet (kade 36,4 km van zeeknoop) |
| b2 | B | zee (LNG-carrier, aannemelijk: één bron) | zeeknoop 2572 → zeeknoop 9671 (22.7053,120.2533) | Timorzee/Bandazee → Celebeszee of Makassar → ZCZ → Bashi-kanaal | 4.457 (MARNET, getest) tegen hemelsbreed 4.097 (+8,8%); geen gepubliceerde routelengte, de ontwerpschatting 5.500-6.500 is vervallen | MARNET zeeknoop → zeeknoop | nee |
| b3 | B | zee (aanloop) | zeeknoop 9671 → `gas-ya-kade` | Straat Taiwan → Kaohsiung-havenmond | ~13 (hemelsbreed) | maak_havenaanloop.py, timeout 600; bij mislukken rechte stippel | ja — net reikt niet (kade 12,9 km van zeeknoop) |

Geen leidingbeen: de 889 km-exportleiding Ichthys-veld → Blaydin Point ligt offshore en is niet in OSM gekarteerd [4]; geen tweede been aan Taiwanse zijde (geen Geofabrik-extract Taiwan, geen bron voor een vervolg).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-ic-kade` | LNG-fabriek / laadkade | Ichthys LNG, steigerkop Blaydin Point | -12.5101, 130.9081 | [4][6] sitelaag `w-ichthys` (-12.5215,130.9225, Wikidata) + eigen satellietblik | bron-gelegd (z15 gezien: ~2 km lange trestle-steiger de baai in met een kop in diep water, fabriek met tanks en procestrains op de oever; de sitelaag-fabriekspunt ligt 2 km landwaarts) |
| `gas-ya-kade` | losplek / regas-terminal | CPC Yong'an LNG-terminal, ligplaats aan de steiger binnen de golfbreker | 22.8094, 120.1978 | [3][5][6] Wikipedia-tankparkpunt (22.8098,120.2053) is het tankpark, niet de kade | bron-gelegd (z15 gezien: LNG-carrier aan de steiger in de door een golfbreker omsloten havenkom, zes witte tanks op het terrein ernaast) |

Hergebruik: Darwin-zeeknoop 2572 is dezelfde als in `lithium-finniss-ningbo` (b2 daar); de Blaydin-aanloop is hier nieuw (ander kadepunt, 36,4 km). Geen Taiwan-anker bestond.

## 4 · Via-punten
Geen — b1/b3 zijn aanlopen, b2 is een zeebeen zonder corridorkeuze (MARNET routeert zeeknoop → zeeknoop).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ichthys LNG (Blaydin Point) | INPEX/TotalEnergies (CPC 2,625% belang sinds 2014) | gas → LNG | 8,9 Mtpa (2 trains) ≈ 12,1 bcm/j; eerste lading 22-10-2018 | [2][4][7] |
| Yong'an LNG-terminal | CPC Corporation | LNG → hervergast gas | 7,44 Mtpa (Wikipedia; GEM noemt 10,5 Mtpa — tegenspraak, hier Wikipedia) ≈ 10,1 bcm/j | [3] |

## 6 · Stoppunt
De keten stopt bij de Yong'an-kade: Taiwan heeft geen Geofabrik-extract en geen bron koppelt de hervergaste stroom aan een specifieke afnemer. Fase C/D/E vervallen. Het zeebeen is de volledige keten (kade → kade); de enige doorgetrokken lijn is b2.

## 7 · Open punten
- **Contractstroom, geen gemeten stroom:** CPC koopt 1,75 Mtpa [1][2]; alleen de eerste lading is gedocumenteerd (Pacific Breeze, geladen op de Darwin-fabriek 15-16 nov 2018, aankomst Yung-An 26-11-2018 [5][7]). Dat elke volgende lading uit Darwin komt is niet gevonden.
- **Corridor niet gebrond:** het MARNET-pad (4.457 km) is het kortste; of de carriers via Celebeszee, Makassar of een andere route varen noemt geen bron.
- **Ichthys-gasveld + 889 km-leiding niet getekend** (offshore, geen OSM; geen brongegeven platformcoördinaat in dit onderzoek).
- **Capaciteitstegenspraak Yong'an** 7,44 Mtpa (Wikipedia) tegen 10,5 Mtpa (GEM) — niet opgelost; en fabriek 8,4 (sitelaag) tegen 8,9 Mtpa (Wikipedia-artikel).
- **Eerste-lading-datum wisselt:** Natural Gas World/LNG Industry dateren aankomst 26-11-2018 [5][7]; het ontwerp noemde 16-11 als vertrek. CPC: geladen 16-11, aankomst 26-11 [5].
- Kades zijn site-niveau, niet berth-nauwkeurig (steigerkop is de zichtbare laadplek; Ichthys heeft meerdere ligplaatsen aan de steiger).

## 8 · Bronnen
[1] INPEX, "Ichthys gas sales agreements announced" — CPC 1,75 Mtpa, 15 jaar vanaf 2017. https://www.inpex.com.au/news-and-updates/media-centre/media-releases/ichthys-gas-sales-agreements-announced/
[2] INPEX, 27-06-2013, "Transfer of the Ichthys LNG Project equity interest to CPC" — 2,625% belang. https://inpex.com.au/news-and-updates/media-centre/media-releases/transfer-of-the-ichthys-lng-project-equity-interest-to-cpc-corporation-taiwan
[3] Wikipedia, "Yongan LNG Terminal" — Yong'an District, Kaohsiung; CPC; 7,44 Mtpa; coördinaat 22°48'35"N 120°12'19"E (tankpark). https://en.wikipedia.org/wiki/Yongan_LNG_Terminal
[4] Wikipedia, "Ichthys gas field" — 889 km subzeeleiding naar Bladin Point, 8,9 Mtpa, eerste gas 30-07-2018, eerste LNG-lading 22-10-2018. https://en.wikipedia.org/wiki/Ichthys_gas_field
[5] CPC, "Highlights from the development phase and operational debut of the Ichthys LNG project" — Pacific Breeze laadt in Darwin (Middle Arm/Blaydin Point) ~16-11-2018, aankomst Yongan 26-11-2018. https://www.cpc.com.tw/en/News_Content.aspx?n=2705&s=3803
[6] Esri World Imagery via `v2/tools/sat_check.py` (z15, live, 2026-11-01) — `sat-gas-ichthys-yongan-ichthys-kade.png`, `sat-gas-ichthys-yongan-yongan-kade.png` (eerdere toets-beelden `…-toets-blaydin.png`, `…-toets-yongan.png`).
[7] Natural Gas World, 26-11-2018, "Taiwan's CPC receives first Ichthys LNG" (Yung-An, aankomst 26 nov) https://naturalgasworld.com/taiwans-cpc-receives-first-ichthys-lng-66224 · LNG Industry, 26-11-2018, "Taiwan imports Ichthys LNG cargo" (Pacific Breeze) https://www.lngindustry.com/liquid-natural-gas/26112018/taiwan-imports-ichthys-lng-cargo
[8] `v2/build-cache/marnet-preais` (MARNET-zeeknopen) — eigen meting: zeeknoop 2572 op 36,4 km van `gas-ic-kade`; zeeknoop 9671 op 12,9 km van `gas-ya-kade`. Haalbaarheidstoets (workflow-invoer): aanloop Blaydin 40,8 km, zee 4.457 km getest.

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)

**Bestand:** `v2/data/stroomroute-gas-ichthys-yongan.json` (10,7 KB, versie 2, lonlat, 3 benen, 549 punten, 2 markers). **Recept:** `bak_gas_ichthys_yongan()` in `v2/tools/bak_stromen.sh`; draaien met `bash v2/tools/bak_stromen.sh gas-ichthys-yongan`.

| # | modaliteit | been | km | stippel | naad naar volgend |
|---|---|---|---|---|---|
| 1 | zee | haven-aanloop Blaydin Point (kade → zeeknoop 2572) | 40,8 | ja: net reikt niet | 0,0 |
| 2 | zee | LNG-carrier Ichthys (Darwin) → Yong'an (Kaohsiung) (aannemelijk: een bron), MARNET 2572 → 9671 | 4.457,2 | nee | 0,0 |
| 3 | zee | haven-aanloop Yong'an (zeeknoop 9671 → kade) | 16,5 | ja: net reikt niet | - |

Totaal 4.514,5 km. Markers: `gas-ic-kade` (-12.5101,130.9081) en `gas-ya-kade` (22.8094,120.1978), beide op het uiteinde van hun aanloop (0 km).

**Toets.** b2 4.457 km = brief 4.457 (MARNET, geen gepubliceerde routelengte; hemelsbreed 4.097, +8,8%). Geen naad > 5 km. `toets_knikken`: 4 knikken >= 60 gr (MARNET-routerhoeken in Banda-/Celebeszee en bij Kaohsiung), 0 omkeringen, 0 terugloop. Geen recht been zonder stippel. Json laadt, modaliteit alleen `zee`.

**Aanloop Blaydin (b1).** `maak_havenaanloop.py` vond bij cel 0,02 een pad van 40,8 km (omwegfactor 1,121) zonder landkruising; cel 0,01 gaf geen pad, de eerste trap volstond. Duur ongeveer 4 min. Stippel omdat het kortste pad over water een berekening is, geen waargenomen vaargeul.

**Aanloop Yong'an (b3).** Pad van 16,5 km (omwegfactor 1,278 tegen 12,9 km hemelsbreed; de brief verwachtte ~13): zeeknoop 9671 ligt in de 1:10M-kust 100% over land, dus het pad moet om de landtong en golfbreker heen. 0,80 km grenst aan het kade-uiteinde (korrel van de kust, geen fout). Cel 0,0025 gaf geen pad; trap 0,005 slaagde. Stippel.

**Lessen.** (1) `maak_havenaanloop.py` met een negatieve latitude: geef `--van=-12.5101,130.9081` met een gelijkteken, anders leest argparse het getal als vlag. (2) Beide aanlopen parallel draaien kan (elk ~4 min). (3) Geen via-punten, geen extract, geen leiding, geen kopie nodig.
