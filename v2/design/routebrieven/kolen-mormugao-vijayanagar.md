# Routebrief (licht) · Kolen · Mormugao → Vijayanagar (India)

**stroom-id:** `kolen-mormugao-vijayanagar` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** geïmporteerde cokeskool per **spoor** (~376 km, South Western Railway over de Westelijke Ghats) van de JSW-kolenterminal (South West Port Ltd, berth 5A/6A) in Mormugao (Goa) via Margao, Castle Rock, Londa, Hubballi, Gadag en Hosapete naar JSW Steel Vijayanagar Works bij Toranagallu (Karnataka) — stoppunt. De zeepoot ontbreekt bewust (geen bron noemt een laadhaven voor deze lading).
**Welke as van het verhaal:** *Kolenimport aan de Indiase westkust naar het binnenland* — Mormugao was in 2019-20 India's derde cokeskool-terminal (6,7 Mt) [4]; JSW voerde 7,07 Mt (2020-21) en 6,01 Mt (2021-22 t/m feb) cokeskool via de haven in [5]. Het Mormugao-Vijayanagar-verband steunt op één bron (2018) [3]: aannemelijk.

## 1 · Ketenkaart
```
JSW-kolenterminal Mormugao, berth 5A/6A `kolen-mormugao-kade` (aannemelijk: JSW-berth niet te onderscheiden van Adani-berth 7)
   ──(b1 spoor · Vasco - Margao - Castle Rock - Londa - Hubballi - Gadag - Hosapete · ~376 km, aannemelijk: één bron)──►
JSW Steel Vijayanagar Works `kolen-vijayanagar-fabriek` ⏹ stoppunt (laatste ~2 km eigen terrein = stippel)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | spoor | Mormugao-kade → Toranagallu-station (4 spoorruns) | Mormugao - Margao - Castle Rock - Londa - Hubballi - Gadag - Hosapete - Toranagallu (SWR) | Mormugao→Hosapete 343,8 gemeten tegen 352,28 spoorkm Hospet-Vasco (−2,4%) [6]; +31,9 km Hosapete→Toranagallu = 375,7 totaal; het ontwerp-getal 410 is nergens bevestigd | toets_spoorroute (BAKE_SUFFIX=-raw), 4 runs | nee (zie b2) |
| b2 | C | spoor | Toranagallu-station → JSW-fabrieksanker | eigen terrein JSW Vijayanagar | ~2,1 hemelsbreed, geen spoorkm | stippel | ja — last mile (de router volgt een plantlus van 46,6 km i.p.v. 31,9 km; interne ring niet apart gerouteerd) |

Kop: de router snapt het kade-anker op 0,23 km (hoofdnet-knoop 1455885) — geen havenspoor-stippel nodig. Geen zeebeen, geen haven-aanloop.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-mormugao-kade` | overslag zee→spoor | JSW (South West Port Ltd) kolenterminal, Mormugao, berth 5A/6A | 15.4120, 73.7990 | [1][2][7] | aannemelijk (z16/z17 gezien: kolenterminal aan de noordoever van de landtong met een bulkcarrier aan de kade, zwarte kolenstapels, overdekte transportband en spoor met wagons; welk berth JSW is en welke Adani (berth 7) is op het beeld niet te zien) |
| `kolen-vijayanagar-station` | spoor-aankomst | Toranagallu Junction (station) | 15.2029, 76.6631 | [10] | bron-gelegd (z16 gezien: perronsporen en emplacement ten noorden van het township; ~1,3 km van de plantrand, niet 2-3 km) |
| `kolen-vijayanagar-fabriek` | fabriek / losplek | JSW Steel Vijayanagar Works, kolenpark noordrand | 15.1860, 76.6700 | [8] | bron-gelegd (z16 gezien: geïntegreerd staalcomplex van ~10.000 acre, zwarte kolenopslag direct naast de spoorbundel aan de noordrand) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Londa Junction | 15.4489, 74.4955 | knooppunt waar de Ghat-lijn (Castle Rock - Londa) op de hoofdlijn Londa - Hubballi aansluit [7][11]; snap 0,06 km; de Ghat-run raakt Margao (0,27 km) en Castle Rock (0,30 km) vanzelf |
| b1 | 2 | Hubballi Junction | 15.3500, 75.1491 | dwingt de lijn door Hubballi-station; een vrije route (388,6 km) liet Hubballi 3,5 km links liggen via een bypass [11] |
| b1 | 3 | Hosapete Junction | 15.2865, 76.3867 | pint Hubballi - Gadag - Hosapete (de run raakt Gadag 0,44 km) en het eindstuk naar Toranagallu [11] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| JSW-kolenterminal Mormugao (SWPL) | JSW | zeeschip → spoorwagon | 7 Mt/j (2017), uitbreiding naar 14-15 Mt/j gepland; 3,6 Mt/j kolen volgens een 2018-bron | [1][2][3] |
| JSW Steel Vijayanagar Works | JSW Steel | cokeskool (deels import) → cokes → staal | geen capaciteitscijfer in de bronnen; het plant is 10.000 acre | [3][8] |

## 6 · Stoppunt
De brief stopt bij het kolenpark van de fabriek: Vijayanagar maakt cokes en staal op één terrein, dus fase D/E vervalt (geen aparte afnemer stroomafwaarts). De zeepoot naar Mormugao blijft weg omdat geen bron een laadhaven voor deze lading noemt.

## 7 · Open punten
- **Verband één bron:** alleen NBM&CW (2018) zegt dat SWPL-berths in Mormugao de logistiek van Vijayanagar dragen [3]; de gevonden Mormugao-bronnen noemen Vijayanagar niet.
- **JSW-berth ≠ Adani-berth:** op satelliet niet te scheiden; anker is de kolenterminal, status aannemelijk.
- **Km:** 375,7 km gemeten; 352,28 km (Hospet-Vasco) [6] dekt alleen het stuk tot Hosapete; de 410 km van het ontwerp is niet bevestigd en vervalt.
- **Rajya Sabha-antwoord PQ 256 (14-03-2022) niet leesbaar** (redirect); de 7,07 en 6,01 Mt komen uit een zoekresultaat-samenvatting [5].
- **Plantlus:** het 1-op-1-net legt het kolenpark via een plantring van 46,6 km (ratio 1,44); bewust niet getekend, de last mile is een stippel van ~2,1 km.
- **Tweede toevoerroute** (Jaigad/Mangalore/Krishnapatnam) en een geplande captive haven bij Honnavar [3] bestaan; niet getekend.

## 8 · Bronnen
[1] Maritime Gateway, JSW Group import coal Mormugao Port (2017-04-05) — berths 5A/6A, 7 Mt/j, plan 14 Mt/j. https://www.maritimegateway.com/jsw-group-import-coal-mormugao-port/
[2] Down To Earth, Goa increases coal handling capacity of Mormugao Port — SWPL = JSW, 7,5 → 14-15 Mt/j. https://www.downtoearth.org.in/mining/goa-increases-the-coal-handling-capacity-of-mormugao-port-a-protected-natural-harbour-59566
[3] NBM&CW, JSW unveils 2.000 cr port facility in Karnataka (2018-11-23) — SWPL-berths in Mormugao voeden Vijayanagar, 3,6 Mt/j = helft van de behoefte. https://www.nbmcw.com/news/jsw-unveils-2-000-cr-port-facility-in-karnataka.html
[4] Argus Media, Indian coking coal imports hit by port closures — Mormugao 6,7 Mt apr 2019-jan 2020. https://argusmedia.com/ja/news-and-insights/latest-market-news/2089891-indian-coking-coal-imports-hit-by-port-closures
[5] Rajya Sabha PQ 256 (14-03-2022) — JSW-import cokeskool Mormugao 7,07 Mt 2020-21, 6,01 Mt 2021-22 tot feb (niet direct leesbaar). https://rsdebate.nic.in/bitstream/123456789/729207/1/PQ_256_14032022_U1322_p160_p160.pdf
[6] Indian Infrastructure, Hospet-Hubli-Londa-Tinaighat-Vasco da Gama doubling (2025-09-08) — 352,28 km Hospet-Vasco; thegoan.net (2025-09-01): 363 km, vervoer van ijzererts, kolen en staal. https://indianinfrastructure.com/2025/09/08/ministry-of-railways-issues-notification-to-acquire-additional-land-for-hospet-hubli-londa-tinaighat-vasco-da-gama-railway-line-doubling-project-in-goa-karnataka/
[7] Wikipedia, Mormugao Port — spoor via South Western Railway, Castle Rock-lijn (1887), Jindal South West Port twee berths. https://en.wikipedia.org/wiki/Mormugao_Port
[8] Wikipedia, JSW Steel — Vijayanagar Works bij Toranagallu, 10.000 acre. https://en.wikipedia.org/wiki/JSW_Steel
[10] OpenStreetMap/Nominatim, Toranagallu Junction (node 1153239943) — 15.2029326, 76.6631417. https://nominatim.openstreetmap.org/
[11] Wikipedia, stationspagina's (Vasco da Gama 15.3961/73.8117, Castle Rock 15.3979/74.3322, Hubballi 15.35/75.1491, Gadag 15.4366/75.6423, Hosapete 15.2865/76.3867); Londa en Hosapete via Nominatim. https://en.wikipedia.org/wiki/Hosapete_Junction_railway_station
[12] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-kolen-mormugao-vijayanagar-jsw-kade17.png`, `-jsw-kade.png`, `-jsw-emplacement.png`, `-jsw-fabriek.png`.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)

**Recept:** `bash v2/tools/bak_stromen.sh kolen-mormugao-vijayanagar` → `v2/data/stroomroute-kolen-mormugao-vijayanagar.json` (23,0 KB, contract versie 2, punt_formaat lonlat). Functie `bak_kolen_mormugao_vijayanagar` in `v2/tools/bak_stromen.sh`; geen profiel in `maak_stroombeen_weg.py` (alles spoor), geen zee, geen haven-aanloop, geen luchtbeen, geen gedeelde kopie.

**Benen (5, in reisvolgorde):**
| # | modaliteit | km (bake) | punten | naad | beschrijving |
|---|---|---|---|---|---|
| 1 | spoor | 111,0 | 511 | — | Mormugao-kolenterminal → Londa Junction (SWR via Margao en Castle Rock) |
| 2 | spoor | 90,6 | 341 | 0,000 | Londa → Hubballi Junction |
| 3 | spoor | 143,2 | 300 | 0,000 | Hubballi → Hosapete Junction (via Gadag) |
| 4 | spoor | 32,2 | 93 | 0,000 | Hosapete → Toranagallu Junction |
| 5 | spoor, stippel | 2,0 | 2 | 0,076 | last mile Toranagallu → kolenpark JSW (geen net op deze korrel) |

Totaal 379,0 km (376,8 km gemeten spoor plus 2,0 km stippel). De vier spoorruns zijn vooraf gebakken met `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs` (3.260.717 spoor-edges, bevestigd in een controlerun van run 4: 31,9 km, 60 edges, 0 bochten). De haversine-km in de bake wijkt 0,2-0,5 km af van de routerkm (110,8 / 90,1 / 142,9 / 31,9 = 375,7).

**Markers (3):** Mormugao-kade 15.4120, 73.7990 (0,23 km van de lijn, router-snap op hoofdnet-knoop 1455885, geen havenspoor-stippel nodig) · Toranagallu Junction 15.2029, 76.6631 (0,0 km) · JSW-kolenpark 15.1860, 76.6700 (eindpunt van de stippel, 0,0 km).

**Toets:** naden 0,000 / 0,000 / 0,000 / 0,076 km (max 0,08, ver onder 5 km) · km tegen de brief: spoorkm Mormugao→Hosapete 343,8 (bake 344,8) tegen 352,28 spoorkm Hospet-Vasco = −2,4% tot −2,1% (binnen ±15%; die bron dekt alleen tot Hosapete); de 410 km van het ontwerp is niet bevestigd en vervalt · `toets_knikken.py`: 0 knikken, 0 omkeringen · json.load: versie 2, lonlat, alleen modaliteit spoor, elk been ≥ 2 punten · `toets_rechte_benen.py --min-km 5`: geen meldingen voor deze stroom.

**Toelichting stippel (b5):** de last mile Toranagallu Junction → kolenpark (2,0 km recht) is gestippeld omdat het 1-op-1-net het kolenpark alleen bereikt via een plantlus van 46,6 km (ratio 1,44); die interne ring is bewust niet getekend. Stippel betekent hier: hier reikt het net niet / eigen terrein.

**Aannemelijk (beennaam b1):** het verband Mormugao → Vijayanagar steunt op één bron (NBM&CW 2018); het JSW-berth 5A/6A is op satelliet niet te scheiden van Adani-berth 7. De onzekerheid staat in de beennaam en in §3/§7, niet in de lijnstijl.

**Lessen:** (1) de eindpunten van de spoorruns snappen 0,06-0,23 km van hun anker, dus de naden tussen runs zijn 0,000 km omdat elke run op dezelfde junctie-knoop eindigt en begint; (2) in de bake blijft run 1 op 111,0 km hoewel de router 110,8 meldt: de bake telt over de punten.
