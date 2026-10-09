# Routebrief (licht) · zeldzame aardmetalen — Ningbo Yunsheng → Beilun → Long Beach (VS)

**stroom-id:** `ree-yunsheng-longbeach` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** NdFeB-magneten van Ningbo Yunsheng (hoofdvestiging, Ningbo) gaan per truck over de ringweg/havenweg naar Beilun Container Terminal Phase 2 en per containerschip over de Stille Oceaan naar Long Beach (VS) — aannemelijk: macro-stroom plus invoerrecords, geen contract en geen afnemer met naam aan de kade.
**Welke as van het verhaal:** de Chinese magneetexport naar de VS (dalend: jan–jul 2026 3,5 kt, −16% t.o.v. 2024) vanuit één grote Ningbo-fabriek (14,9 kt NdFeB in 2025, capaciteit 26 kt/j) [1][6].

**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** titel noemt "aannemelijk, geen contract"; géén Beilun-aanloop (kade snapt op 1,95 km van zeeknoop 5849); wél een haven-aanloop bij Long Beach (kade 6,47 km van zeeknoop 4488); het haven-punt 33.7550,−118.2150 lag in het water en is vervangen door een kade op satelliet. Nieuw t.o.v. het ontwerp: één bron die Yunsheng aan de VS koppelt (invoerrecords, §8 [7]).

## 1 · Ketenkaart
```
Ningbo Yunsheng `ree-yunsheng-fabriek` ──(b1 truck · Jiangnan Rd → G1504 → S20 → S1 · hemelsbreed 25 km, geen wegkm)──►
Beilun CT Phase 2 `ree-beilun-kade` ──(b2 zee · MARNET · ~10.800 km)──► zeeknoop 4488 ──(b3 haven-aanloop, stippel · 8,6 km)──►
Long Beach containerkade `ree-longbeach-kade` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | truck | `ree-yunsheng-fabriek` → `ree-beilun-kade` | Jiangnan Donglu → G1504 Ningbo Ring Expressway → S20 Chuanshan → S1 Beilun/Dacheng → Yingbin Lu | hemelsbreed 24,8 km, geen wegkm (OSRM 31,2 is OSM-afgeleid; indicatie) | maak_stroombeen_weg, profiel `ree-yunsheng-longbeach-yunsheng-beilun` (staat er, 30,8 km) | nee |
| b2 | B | zee (aannemelijk: één bron) | `ree-beilun-kade` → zeeknoop 4488 (33.7039,−118.1945) | Oost-Chinese Zee → noordelijke Stille Oceaan | grootcirkel kade↔kade 10.531; router zeeknoop↔zeeknoop 10.780 [13] | MARNET | nee (Beilun 1,95 km) |
| b3 | B | zee (haven-aanloop) | zeeknoop 4488 → `ree-longbeach-kade` | Long Beach-havenbekken | 8,6 (handgelegd; hemelsbreed 6,5) | stippel-geojson (gedaan) | ja — MARNET reikt niet tot de kade (6,47 km > 5 km, LAR-586) |

Beennaam b2: "… (aannemelijk: macro-stroom + invoerrecords, geen contract)". Geen luchtbeen: geen bron zegt dat Yunsheng-magneten vliegen; het BL-record in [7] toont zee (vessel + haven Ningbo).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-yunsheng-fabriek` | magneetfabriek (kop b1) | Ningbo Yunsheng, hoofdvestiging (韵升集团), Ningbo | 29.8825, 121.6193 | [10] sitelaag `w-yunsheng-ningbo`, OSM-naamtag; eigen z15 | bron-gelegd (z15 gezien: complex van lage fabriekshallen tussen woontorens, kruis op de hallen) |
| `ree-beilun-kade` | overslag truck → zee | Beilun Container Terminal Phase 2, Ningbo-Zhoushan | 29.9353, 121.8695 | [11] `kobalt-huayou-gunsan.md` §3 | bron-gelegd (letterlijk hergebruikt; 1,95 km van zeeknoop 5849) |
| `ree-longbeach-kade` | overslag zee → VS | containerkade Long Beach, westkade van het grote terminal in het oostelijk havenbekken (zone Pier J, naam niet aan het punt bevestigd) | 33.7600, −118.2132 | [8][9] | aannemelijk (z15 gezien: portaalkranen langs de westkade, containerstapels, spoorbundel oostelijk; terminal en lijn niet bekend; Wikipedia-havenpunt lag in het water) |

## 4 · Via-punten (alleen b1: ringweg/havenweg i.p.v. stad)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | G1504 Ningbo Ring Expressway, Jiangnan-oprit | 29.9153, 121.6891 | pint de ringweg i.p.v. de stad Ningbo in |
| b1 | 2 | S20 Chuanshan-havenweg, oost | 29.8851, 121.7616 | pint S20 als doorgaande havenweg |
| b1 | 3 | S1 Beilun/Dacheng-havenweg | 29.8931, 121.8052 | pint de aanvoer naar Beilun i.p.v. de kustweg |
Alle drie op trunk/motorway (OSRM-geometrie [12], scan-snap 0,00 km); gescand: 30,8 km, −1,1% op de OSRM-indicatie.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ningbo Yunsheng | Ningbo Yunsheng (韵升) | NdPr-metaal/legeringen (niet gebrond) → afgewerkte NdFeB-magneten | 26 kt NdFeB/j (bedrijfsbreed incl. Baotou); 14,9 kt gemaakt, 14,2 kt verkocht (2025) | [1][10] |

## 6 · Stoppunt
Op de kade van Long Beach: [7] noemt consignees (Eriez Manufacturing, 112 containers; Harman de Mexico, El Paso) maar geen losse haven per zending en geen Long Beach-terminal, dus een landbeen daarheen zou een verzonnen haven-keuze zijn.

## 7 · Open punten
- **Geen contract of afnemer aan de kade.** Alleen invoerrecords (151 zendingen 2006-11 t/m 2026-09, vooral ND-FE-B-magneten) en de macro-stroom [4][5][6]; Yunsheng-volume naar de VS onbekend, en de records zijn een steekproef.
- **Los Angeles of Long Beach?** [7] noemt Los Angeles als eerste en Long Beach als tweede haven; het id kiest Long Beach. Terminal, rederij en Queens Gate/oostelijke inlaat zijn niet bekend.
- **Aanloop b3 is handgelegd, schematisch:** `maak_havenaanloop.py` gaf na 300 s geen pad (exit 124, de 1:10M-kust kent het havenbekken niet). Lijn over water west van de Pier J-staart, om de oostelijke terminals, door de oostelijke golfbrekergap (ca. −118,186…−118,181) naar de knoop; het eerste stuk (ca. 0,3 km kade → water) valt in de 1:10M-kust als land.
- **Wegkm b1 onbekend** (hemelsbreed 24,8 km); of Yunsheng via Beilun CT Phase 2 exporteert is aanname (BL-record noemt alleen "NING BO").
- SCMP-artikel uit het ontwerp [3] niet gelezen (HTTP 403); er staat niets uit op. Yunsheng-Baotou (`w-baotou-yunsheng`) is een ander verhaal en niet getekend.
- Overlap: `ree-baotou-ningbo` en `kobalt-huayou-gunsan` delen alleen het Beilun-anker.

## 8 · Bronnen
[1] Metalnomist, 2026-06: Yunsheng 14.856 t afgewerkte NdFeB (+11%), 14.197 t verkocht, capaciteit 26.000 t/j, Baotou naar 15.000 t/j. https://www.metalnomist.com/2026/06/ningbo-yunsheng-ndfeb-magnet-output.html
[2] SMM, juli 2026: Chinese magneetexport jan–jul 36.880 t, juli 5.375 t, verwachting 2026 ca. 61.600 t. https://news.metal.com/newscontent/104073785-china-rare-earth-permanent-magnet-export-analysis-outlook-july-2026smm-analysis
[3] SCMP, 2026: magneetexport naar de VS blijft dalen (niet gelezen, 403). https://www.scmp.com/economy/global-economy/article/3347326/chinas-rare-earth-magnet-exports-us-keep-falling-europe-gains
[4] Reuters via Kitco, 2026-04-20: maart 5.238 t totaal, 406 t naar de VS (laagste in negen maanden). https://www.kitco.com/news/off-the-wire/2026-04-20/chinas-rare-earth-magnet-exports-fall-16-march
[5] Reuters via Kitco, 2026-03-20: jan–feb naar de VS 994 t (−22,5%), uit zoekresultaat. https://www.kitco.com/news/off-the-wire/2026-03-20/chinas-rare-earth-exports-rise-shipments-us-fall
[6] Silverado, juli-update 2026: magneetexport naar de VS jan–jul 3.521 t (−16% t.o.v. 2024). https://silverado.org/media/china-s-global-exports-of-rare-earths-august-2026-update/
[7] ImportGenius, Ningbo Yunsheng Co., Ltd.: VS-douanerecords, 151 zendingen, havens Los Angeles, Long Beach, Wilmington NC, New York, Newark; voorbeeld-BL ONE MAJESTY 025E, foreign port NING BO. https://www.importgenius.com/suppliers/ningbo-yunsheng-co-ltd
[8] Wikipedia, "Port of Long Beach": havencoördinaat 33°45′18″N 118°12′54″W (in het water), Pier J-terminal. https://en.wikipedia.org/wiki/Port_of_Long_Beach
[9] Esri World Imagery via `sat_check.py`, z14/z15: `v2/build-cache/satcheck/sat-ree-yunsheng-longbeach-{yunsheng,lb-haven,lb-kade,lb-aanloop}.png`.
[10] `v2/design/ree-sitelaag.json`, site `w-yunsheng-ningbo` (OSM, naam-tag 韵升集团).
[11] `v2/design/routebrieven/kobalt-huayou-gunsan.md` §3: Beilun-anker; zeeknoop 5849 op 1,95 km.
[12] OSRM (router.project-osrm.org), eigen meting 2026-10-09: 31,2 km, G1504 → S20 → S1. OSM-afgeleid, geen onafhankelijke bron.
[13] MARNET `hecht_marnet.marnet_zee`, eigen meting 2026-10-09: Long Beach-kade → zeeknoop 4488 op 6,47 km; Beilun → 5849 op 1,95 km.
[14] OSM/Geofabrik `china-latest.osm.pbf` (ODbL), wegscan b1 via pure-Python PBF-lezer.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-ree-yunsheng-longbeach.json` (28,1 KB, versie 2, lonlat) · functie `bak_ree_yunsheng_longbeach` in `v2/tools/bak_stromen.sh` · `bash v2/tools/bak_stromen.sh ree-yunsheng-longbeach`.
**Titel:** Zeldzame aardmetalen · Ningbo Yunsheng → Beilun → Long Beach (NdFeB-magneten, aannemelijk, geen contract).

| # | modaliteit | km gebakken | brief | naad naar vorig been | stippel |
|---|---|---|---|---|---|
| 1 | truck | 30,8 | hemelsbreed 24,8, geen wegkm (OSRM 31,2 indicatie): -1,1% op de indicatie | — | nee |
| 2 | zee (MARNET kade → zeeknoop 4488) | 10.780,4 | router zeeknoop↔zeeknoop ca. 10.780 | 1,95 km (Beilun-snap, < 5 km, geen aanloop nodig) | nee |
| 3 | zee, haven-aanloop Long Beach | 8,5 | 8,6 handgelegd | 0,000 | ja |

Totaal 10.819,7 km · 1.406 punten · 3 markers (fabriek, Beilun, Long Beach-kade; alle op 0,0 km van de lijn). Knikken: 20 ≥ 60°, 0 omkeringen, 0 terugloop (de spikes bij de fabriek en Beilun zijn de ankerstubs, de rest zijn zee-bochten).

**Recept.** b1 = profiel `ree-yunsheng-longbeach-yunsheng-beilun` in `maak_stroombeen_weg.py`, geojson `ree-yunsheng-longbeach-weg-yunsheng-beilun.geojson` uit de wegscan via de pure-Python PBF-lezer (pyosmium geblokkeerd, china-extract); b2 = `--been zee 29.9353,121.8695 → 33.7039,-118.1945`; b3 = `--stippel-geojson` `ree-yunsheng-longbeach-aanloop-longbeach.geojson` (9 punten).
**Aanloop b3.** `maak_havenaanloop.py` gaf na 300 s geen pad (exit 124), dus geen tweede poging: handgelegd op Esri z14/z15 door de oostelijke golfbrekergap. De geojson is voor het bakken omgedraaid naar reisvolgorde (zeeknoop → kade), zodat de naad met b2 0,000 km is. De eerste ca. 0,3 km kade-water liggen in de 1:10M-kust als land.
**Bevindingen / open.** (1) De ±15%-toets op b1 is een indicatie: de brief heeft geen echte wegkm. (2) Beilun als exporthaven van Yunsheng en Long Beach (boven Los Angeles) zijn aannames; staat in de titel en de beennaam van b2. (3) De zeeknoop 4488 ligt in open water: de aanloop is schematisch, geen vaargeul. (4) Geen luchtbeen, geen fase D/E.
**Lessen.** Een handgelegde aanloop moet in reisvolgorde (zeeknoop → kade) in het geojson staan; gelegd vanaf de kade geeft hij een naad van 8,5 km met b2.
