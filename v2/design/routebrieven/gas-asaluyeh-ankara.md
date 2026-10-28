# Routebrief (licht) · gas — Asaluyeh (South Pars) → Qom → Qazvin → Bazargan → Erzurum → Ankara (Iran–Turkije)

**stroom-id:** `gas-asaluyeh-ankara` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) · **status:** gebakken
**Keten in één zin:** Iraans pijpgas uit de South Pars-verwerking bij Asaluyeh gaat over de Iraanse nationale gastrunk (Qom, Karaj, Qazvin, Zanjan, langs Tabriz) naar de grens bij Bazargan/Gürbulak en over de BOTAŞ-trunk (Doğubayazıt, Erzurum, Erzincan, Sivas) naar een pijpleidingknoop ten zuiden van Ankara, waar het Turkse net begint. Eén doorlopende OSM-pijpleiding, geen zee.
**Welke as van het verhaal:** de Iraanse pijpgasroute naar Turkije, de tweede Turkse gasbron na Rusland. **7,6 bcm in 2025** (13% van de Turkse invoer), contract 9,6 bcm/j, leidingcapaciteit 14 bcm/j [1][3][4]. Het contract liep **2026-07-29 af** zonder bekende verlenging; de gaslevering ging in 2026 door en H1 2026 was 4,5 bcm (+34%) volgens de haalbaarheidstoets [5].

## 1 · Ketenkaart
```
South Pars-verwerking Asaluyeh `gas-asaluyeh-start` (27.5067, 52.6283)
  ──(b1 leiding · Iraanse nationale gastrunk via Qom–Karaj–Qazvin–Zanjan · 1.790,8 km OSM)──►
Grens Bazargan/Gürbulak (39.3924, 44.4211; geen site, splitspunt b1/b2)
  ──(b2 leiding · BOTAŞ-trunk Doğubayazıt–Erzurum–Tercan · 411,6 km OSM)──► Tercan (39.8447, 40.1476; knoop, geen site)
  ──(b3 leiding · BOTAŞ-trunk Erzincan–Sivas–Kırşehir–Ankara · 712,6 km OSM)──►
Ankara-trunk `gas-ankara-trunk` (39.6009, 32.8141; pijpleidingknoop 37 km ZZO van het centrum) ═══ stoppunt ═══
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-asaluyeh-start` → grens Bazargan | Iraanse gastrunk Asaluyeh–Qom–Qazvin–Bazargan (aannemelijk: contract verlopen 2026-07-29, leveringen gaan door) | **1.790,8** OSM-gemeten; geen gepubliceerde Asaluyeh–Bazargan-lengte (IGAT-11 plan 1.200 km is een ander traject [2]) | OSM-pipeline, 7 ways gestikt | nee |
| b2 | B | leiding | grens Bazargan → Tercan | BOTAŞ-trunk Gürbulak–Erzurum–Tercan | **411,6** OSM-gemeten | OSM-pipeline, ways 361380970 e.v. + dicht gemapte way 1000438319 | nee (2 naden 4,1 en 3,0 km, doorgetrokken) |
| b3 | B | leiding | Tercan → `gas-ankara-trunk` | BOTAŞ-trunk Erzincan–Sivas–Ankara | **712,6** OSM-gemeten | OSM-pipeline, BOTAŞ-ways | nee (max naad 0 m) |

Totaal doorgetrokken **2.915,0 km** (naden 0,4 km in b1, 7,1 km in b2) tegen Wikipedia Tabriz–Ankara **2.577 km** [1]: +13,1%, alleen indicatie (de bron laat het beginpunt Tabriz en de Iraanse trunk-aansluiting open; ons pad is Asaluyeh–Ankara). Stippel: 0 km.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-asaluyeh-start` | gasverwerking (kop) | South Pars-verwerkingscomplex, Asaluyeh | 27.5067, 52.6283 | [2][5][6] | bron-gelegd (z15 gezien: op de NO-rand van een groot complex met tankparken en procesinstallaties, langs een bundel leidingen en wegen die het complex uit loopt; OSM-pijpleiding loopt over dit punt) |
| `gas-bazargan-grens` | grensknoop (geen anker/marker) | Bazargan/Gürbulak, splitspunt b1/b2 | 39.3924, 44.4211 | [6][7] | z15 gezien: onverharde grensstrook ZO van het douaneterrein met vrachtwagenparkeerplaatsen; leidingtracé liggen niet zichtbaar. Een installatie (mogelijk meetstation) op ca. 39.399, 44.396 (niet gebruikt) |
| `gas-ankara-trunk` | stoppunt (overgang naar Turks binnenlandnet) | BOTAŞ-trunk bij Gölbaşı, ZZO van Ankara | 39.6009, 32.8141 | [5][6][8] | aannemelijk (z15 gezien: open steppe naast een snelweg, geen installatie binnen 2 km, alleen een boerderij op 400 m; de OSM-way loopt hier door naar het westen) |

Geen hergebruik van een bestaand anker mogelijk (geen Iraanse of Turkse gasanker in andere brieven; `gas-anapa-kiyikoy` ligt aan de Zwarte Zee).

## 4 · Via-punten
Niet van toepassing (leidingbenen: OSM-geometrie, geen corridorkeuze door ons).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| South Pars-verwerking Asaluyeh | NIOC/POGC | veldgas → droog verkoopgas in de IGAT-lijnen | niet gevonden in een bron met jaar | [2] |
| Grensovergang Bazargan–Gürbulak | NIGC/BOTAŞ | Iraans net → Turkse trunk (Tabriz–Ankara) | 14 bcm/j ontwerp, 9,6 bcm/j contract | [1][3] |
| Ankara (Blue Stream-aansluiting) | BOTAŞ | Iraans gas voegt zich bij het binnenlandse net | niet gekwantificeerd | [1] |

## 6 · Stoppunt
De brief eindigt waar de Turkse trunk het Ankara-net ingaat: vanaf hier is het gas anoniem (binnenlands net en Blue Stream-aansluiting [1]); geen bron volgt één molecuul naar een afnemer. Fase D/E vervallen.

## 7 · Open punten
- **Kop is een OSM-pad, geen site-polygoon**: 27.5067, 52.6283 ligt op een bundel leidingen aan de rand van het complex, niet op een genoemde fase (SP1–24). Titel noemt South Pars zoals het ontwerp; welke IGAT-lijn (2, 3, 4, 8) dit is vermeldt OSM niet (`خط سراسری لوله گاز`, `substance=gas`).
- **Afwijking van de haalbaarheidstoets**: eigen Dijkstra over alle gas-ways (substance gas of leeg, gedeelde OSM-knopen) vindt geen gat boven 5 km tussen Asaluyeh en Bazargan (max 0,3 km) en geen stippel nodig; de toets noemde zes gaten tot 19,6 km. Waarschijnlijk telde die alleen way-uiteinden, niet gedeelde tussenknopen (bv. ways 541577765, 549965417, 551378541, 551130543, 394185395, 393821112). Bak-agent: controleer met `toets_knikken.py`.
- **Turkse kant**: de BOTAŞ-way 586497767 bevat één rechte koorde van 94,2 km (39.9533, 41.5247 → 39.8022, 40.4390). Deze is vervangen door de dicht gemapte gas-way 1000438319 (611 punten, geen operator-tag, 132,2 km), met naden van 4,1 en 3,0 km aan de uiteinden; +19,8 km tegen het koordepad. Niet bevestigd dat 1000438319 dezelfde leiding is.
- Grof gemapte stukken die wel doorgetrokken zijn: 8,1 km tussen twee punten bij 35.4252, 50.2351 en 7,0 en 7,4 km in Turkije (39.4244, 44.3702 en 39.8498, 39.9705).
- Contract-actualiteit: geen bericht van sept/okt 2026 gevonden; 7,6 bcm (2025) is het laatste volledige jaar [3][4]. Sancties en de Iraanse oorlog (maart 2026 aanval op South Pars, export hersteld eind maart) [5].
- Wikipedia noemt het beginpunt Tabriz en 2.577 km; de lengte-toets is daarom alleen een indicatie. Ankara-eind ligt 37 km ZZO van het centrum, niet bij het BOTAŞ-compressorstation Etimesgut/Yapracık (39.8549, 32.5925, 28 km elders) [8].

## 8 · Bronnen
[1] Wikipedia, "Tabriz–Ankara pipeline" (2.577 km, 14 bcm/j, ca. 11 bcm/j invoer, contract 25 jaar tot midden 2026, Blue Stream-aansluiting voor Ankara) https://en.wikipedia.org/wiki/Tabriz%E2%80%93Ankara_pipeline
[2] Wikipedia, "Iran Gas Trunkline" (IGAT-1 t/m 11, South Pars/Asalouyeh, IGAT-11 Asalouyeh–Bazargan 1.200 km gepland) https://en.wikipedia.org/wiki/Iran_Gas_Trunkline
[3] PGJ Online, "Turkey-Iran gas pipeline deal nears expiry as supply talks stall", 2026-04-18 (9,6 bcm/j contract, 7,6 bcm in 2025 = 13% van de invoer, verloop juli 2026) https://pgjonline.com/news/2026/april/turkey-iran-gas-pipeline-deal-nears-expiry-as-supply-talks-stall
[4] IENE, "Turkey says Iran gas pipeline contract nearing expiry, no talks yet on extension", 2026-04-20 (Reuters-bericht, zelfde cijfers) https://www.iene.eu/energy-news/turkey-says-iran-gas-pipeline-contract-nearing-expiry-no-talks-yet-on-extension-p8432.html
[5] Haalbaarheidstoets gas-asaluyeh-ankara (doorgegeven, niet zelf herladen): contract verlopen 2026-07-29 (Iran International 2026-08-21), H1 2026 invoer 4,5 bcm, South Pars-aanval maart 2026 (energyintel/Bloomberg-abstract). Eigen OSM-scan: pure-python PBF-scan (`gas-galkynysh-khorgos-pbfscan.py --alle`) op lokale Geofabrik-extracts iran en turkije, daarna Dijkstra over gedeelde knopen; ODbL https://www.openstreetmap.org/copyright
[6] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-gas-asaluyeh-ankara-{asaluyeh-start,bazargan-grens,ankara-trunk}.png`
[7] OSM-way 361380970 (eerste BOTAŞ-way na de grens), way 393821112 (Iraanse eindway, 39.3924, 44.4211): zelfde knoop aan beide kanten van de grens.
[8] Photon/OSM (komoot): "BOTAŞ Ankara Kompresör İstasyonu" 39.8549, 32.5925, industrial, Etimesgut/Yapracık; "BOTAŞ" company Gölbaşı 39.7890, 32.8067 (kantoor, niet gebruikt). https://photon.komoot.io

## 9 · Gebakken (2026-10-28, lichte werkwijze, M31 golf 10)
**Bestand:** `v2/data/stroomroute-gas-asaluyeh-ankara.json` (105,7 KB, versie 2, lonlat) · functie `bak_gas_asaluyeh_ankara` in `v2/tools/bak_stromen.sh` · titel "Gas · Asaluyeh → Bazargan → Ankara (Iran–Turkije)".

| # | modaliteit | km | punten | naad naar vorig | stippel |
|---|---|---|---|---|---|
| b1 | leiding | 1.790,8 | 3.273 | — | nee |
| b2 | leiding | 411,6 | 1.021 | 0,00 km | nee |
| b3 | leiding | 712,6 | 1.125 | 0,00 km | nee |

Totaal **2.915,0 km** · 5.419 punten · 2 markers (`gas-asaluyeh-start` 0,002 km en `gas-ankara-trunk` 0,005 km van de lijn). Geen stippel, geen zee, geen kopie.

**Recept:** drie voorgebakken FeatureCollections uit de eigen pure-python PBF-scan (iran, turkije) in `v2/build-cache/ais/graaf/gas-asaluyeh-ankara-leiding-*.geojson`, als `--been-geojson "leiding|…"` achter elkaar in `hecht_marnet.py route`. Beennamen volgen de corridors uit §2; b1 draagt "aannemelijk: contract verlopen 2026-07-29, leveringen gaan door".

**Toets:** km per been gelijk aan de brief (de OSM-lengte is zelf de meting; geen gepubliceerde Asaluyeh–Bazargan-lengte, totaal +13,1% tegen Wikipedia Tabriz–Ankara, alleen indicatie). Naden 0,0 km (max 0,0). `toets_knikken.py`: 21 knikken ≥ 60°, **0 omkeringen ≥ 150°**, 0 terugloop; de brief verwachtte 0 boven 100°, maar er zijn er 2 (117,4° en 115,2°, R 13 m, bij 36.0940,50.0060 in b1) plus 6 tot 95° met R 3-4 m bij 35.1365,50.4202: kartering-spikes in de OSM-leiding (kleine zigzag op meterschaal), geen lus en geen rijdbaarheidsprobleem voor een leiding. `toets_rechte_benen.py` meldt niets voor deze stroom.

**Open (uit §7, ongewijzigd):** kop is een OSM-leidingpad, geen genoemde SP-fase · way 1000438319 niet bevestigd · grof gemapte stukken (8,1 km bij 35.4252,50.2351; 7,0 en 7,4 km in Turkije) doorgetrokken · levering na 2026-07-29 onbevestigd · Ankara-eind is een leidingknoop.

**Lessen:** een volledig voorgebakken leiding-stroom bakt in één `route`-aanroep (~1 min, geen wegscan, geen slot behalve het zware); `route` neemt de lijn letterlijk over en meldt "vooraf gebakken lijn", dus de toets is de naad-rapportage plus `toets_knikken`.
