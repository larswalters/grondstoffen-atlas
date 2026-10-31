# Routebrief (licht) · Lithium — North American Lithium → Port de Québec → Tesla Robstown (Canada → VS)

**stroom-id:** `lithium-nal-robstown` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat (~5,0% Li2O) van de North American Lithium-mijn (La Corne, Abitibi; Elevra, ex-Sayona/Piedmont) gaat per truck 60,8 km naar de Solurail-transload in Val-d'Or, per CN-spoor 768 km naar het Port de Québec (Beauport), per bulkschip 6.154 km via Cabotstraat, Atlantische Oceaan en Floridastraat naar Corpus Christi en per truck 43 km naar Tesla's raffinaderij in Robstown (spodumeen → lithiumhydroxide).
**Welke as van het verhaal:** de Amerikaanse eigen-raffinage-as met Noord-Amerikaanse grondstof: Canadees hardrock naar een VS-raffinaderij, naast Kathleen Valley (Australië). Jaarvolume **≈ 17 kt LCE/j** = Piedmonts 50%-afname van NAL, 113 kt droog SC6/j × 6% × 2,473 [2 §16.5] (eigen omrekening, plafond); Tesla-contract zelf ~125 kt SC6 over 2023–2025 ≈ 6 kt LCE/j [4]; NAL totaal FY26 197.967 dmt ≈ 24 kt LCE [1]. Peiljaar 2025/26. Het werkelijk naar Robstown verscheepte volume is niet gepubliceerd.

## 1 · Ketenkaart
```
NAL La Corne `li-nal-plant` ──(b1 truck · Route du Lithium → Route 111 → Route 117 · 60,8 km, KOPIE nal-quebec b1)──► Solurail-transload Val-d'Or `li-nal-valdor`
  ──(b2 spoor · CN via Senneterre, La Tuque, Shawinigan, Trois-Rivières · 768,3 km, KOPIE nal-quebec b2)──► Port de Québec, Beauport `li-nal-quebec-kade` (aannemelijk)
  ──(b3 zee · MARNET · 6.153,8 km, aannemelijk: één bron)──► Corpus Christi Inner Harbor `li-corpuschristi-kade` (aannemelijk)
  ──(b4 truck · I-37 → TX 44 → US 77/I-69E → CR 28 · 42,7 km, KOPIE kathleenvalley b4)──► Tesla Lithium Refinery `li-robstown-tesla` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `li-nal-plant` → `li-nal-valdor` | Route du Lithium → Route 111 → Route 117 (Bd Tétrault) → Rue Roland-Massé | 60,8 gebakken; hemelsbreed 33 km, geen wegkm; TRS "60 km" [2], OSRM 61,0 = indicatie | letterlijke kopie `lithium-nal-quebec-weg-plant-valdor.geojson` | nee |
| b2 | A | spoor | `li-nal-valdor` → `li-nal-quebec-kade` | CN Abitibi/La Tuque-lijn → Hervey-Jonction → Shawinigan → Trois-Rivières → Québec | 768,3 eigen netmeting, geen gepubliceerde spoorkm [2][9] | letterlijke kopie `spoorroute-lithium-nal-quebec-valdor-beauport.geojson` | nee |
| b3 | B | zee (aannemelijk: één bron) | `li-nal-quebec-kade` → `li-corpuschristi-kade` | Saint-Laurent → Cabotstraat → Atlantische Oceaan → Floridastraat → Golf van Mexico (MARNET beslist) | 6.153,8 eigen MARNET-meting (snaps 1,26 en 1,43 km; 262,7 track + 5.890,6 MARNET); geen gepubliceerde zeekm | MARNET (`--been`, kade → kade) | nee, geen aanloop (zie §7) |
| b4 | C | truck (aannemelijk: één bron) | `li-corpuschristi-kade` → `li-robstown-tesla` | Stroman Rd/N Port Ave → I-37 → TX 358/44 → US 77/I-69E → FM 2826 → CR 28 | 42,7 gebakken; hemelsbreed 34 km, geen wegkm; OSRM 42,3 = indicatie [10] | letterlijke kopie `lithium-kathleenvalley-robstown-weg-corpuschristi-tesla.geojson` | nee |

Totaal 7.025,6 km, 88% nieuw (alleen b3). Naden: b2→b3 ~1,4 km (spoorsnap 0,19 + zeesnap 1,26), b3→b4 1,43 km, beide < 5 km.

## 3 · Ankers (alle vijf hergebruikt letterlijk, geen nieuw anker)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-nal-plant` | mijn/concentrator | NAL-procescomplex, La Corne | 48.4059, -77.8305 | brief `lithium-nal-quebec` [9], [2] | bron-gelegd (sat z15, `sat-lithium-nal-quebec-plant.png`: procescomplex met hal en opslag naast tailingsdam, pit noordelijk) |
| `li-nal-valdor` | overslag truck → spoor | Solurail-transload, Rue Roland-Massé, Val-d'Or | 48.1101, -77.7734 | brief `lithium-nal-quebec` [9], [2 §16.6] | aannemelijk (sat z16: grindterrein met loodsen, spoorbundel ~100 m oostwaarts) |
| `li-nal-quebec-kade` | overslag spoor → zee | Port de Québec, sector Beauport | 46.8330, -71.1985 | brief `lithium-nal-quebec` [9]; "FOB Port of Québec" [1]; lading vertrok uit Québec [6][8] | aannemelijk (sat z15/z16: droge-bulkterminal met hopen en schepen; terminal/kade NAL niet gepubliceerd) |
| `li-corpuschristi-kade` | losplek (bulk, aannemelijk) | Corpus Christi Inner Harbor, zuidoever W van de Harbor Bridge | 27.8112, -97.4045 | brief `lithium-kathleenvalley-robstown` [10] | aannemelijk (sat z15: bulkschip aan kade bij groot magazijn; terminalnaam onbekend) |
| `li-robstown-tesla` | fabriek | Tesla Lithium Refinery, County Road 28, Robstown | 27.7093, -97.7306 | brief `lithium-kathleenvalley-robstown` [10], [3] | bron-gelegd (sat z15: terrein met kiln, tanks, magazijn en twee afvalvijvers) |

Beelden: `v2/build-cache/satcheck/sat-lithium-nal-quebec-{plant,valdor,valdor-z16,beauport,beauport-z16}.png`, `sat-lithium-kathleenvalley-robstown-{corpuschristi,tesla}.png`.

## 4 · Via-punten (alleen b1 en b4 hebben er; allemaal uit de kopie, niet opnieuw gelegd)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Route du Lithium × Route 111 | 48.4154, -78.0035 | mijnweg gaat eerst 14 km west, slaat daar zuid op Route 111 (geen Barraute/R386) |
| b1 | 2 | Route 111 bij La Corne (zuid) | 48.3427, -77.9958 | houdt de doorgaande Route 111 |
| b1 | 3 | Route 111 Saint-Mathieu–Val-d'Or | 48.2882, -77.9950 | zelfde corridor |
| b1 | 4 | Route 111 N van Chemin Sullivan | 48.1871, -77.8606 | laatste punt vóór Route 117 (ring W-zijde, geen centrum) |
| b4 | 1 | I-37 na oprit MLK Dr | 27.8002, -97.4225 | I-37 westwaarts i.p.v. stadsstraten |
| b4 | 2 | begin TX 44, Corpus Christi-West | 27.7821, -97.4723 | TX 44 i.p.v. door via I-37/US 77 |
| b4 | 3 | US 77/I-69E bij FM 2826 | 27.7780, -97.6650 | aansluiting richting CR 30 → CR 28 |
| b4 | 4 | CR 28 (OSM-vertex, 0,21 km N van anker) | 27.7107, -97.7292 | fabrieksanker snapt op een geïsoleerd service-component |

b2 (spoor) heeft geen verplicht via-punt; Hervey-Jonction 46.8530, -72.4701 is optioneel en ongebruikt (totaal blijft 768,3 km). Extracts: b1 `canada`; b4 `us-texas`.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| NAL-concentrator La Corne | Elevra Lithium | erts → spodumeenconcentraat ~5,0% | ontwerp 184.511 t/j (5,82%); FY26 197.967 dmt ≈ 24 kt LCE | [1][2] |
| Tesla Lithium Refinery, Robstown | Tesla | spodumeenconcentraat (NAL, Kathleen Valley) → LiOH | geen tonnage gepubliceerd; Tesla-contract ~125 kt SC6 over 2023–2025 | [3][4][5] |

## 6 · Stoppunt
Brief stopt bij de raffinaderij in Robstown: enige met naam genoemde afnemer van NAL-concentraat in de VS [3]; het vervolg (LiOH naar Tesla-fabrieken, "diverse" volgens IIR) is niet gebrond als locatie of volume, dus fase D/E vervalt.

## 7 · Open punten
- **Geen zending Québec → Corpus Christi gepubliceerd.** Tesla ← NAL volgt uit IIR (Piedmont-concentraat uit NAL, haven niet genoemd) [3] en het Piedmont-Tesla-contract [4]; Argus (2026) noemt NAL en Kathleen Valley, maar de pagina gaf bij herlezen geen tekst (alleen via brief [10]). Daarom *aannemelijk: één bron* in b3/b4; de lijn is wel gemeten en doorgetrokken.
- **Contractperiode:** Piedmont-Tesla liep tot eind 2025 (optie +3 jaar) [4]; verlenging en de Elevra-fusie (2025) veranderden de structuur; het 6-K noemt geen afnemers [1].
- **Beauport-terminal en Corpus Christi-terminal niet gepubliceerd** (kade en berth onzeker); laadhaven Québec bevestigd: "FOB Port of Québec" [1], lading AAL Moon 1 aug 2023 [6][8].
- **Corpus Christi-zeeknoop:** dichtstbijzijnde zeeknoop 4842 ligt 6,4 km van de kade (> 5 km, LAR-586), maar de router hecht via de VS-trackgraaf op 1,43 km (naad < 5 km); op last van de haalbaarheidstoets geen haven-aanloop, net als bij kathleenvalley b3/b4.
- **Zeeroute is een routeerresultaat** (Cabotstraat, Floridastraat; 0 landconflicten in de landtoets), geen bron; km zelf gemeten.
- Wegkm b1/b4 niet gepubliceerd (indicaties OSRM); spoor 768,3 km eigen netmeting; twee bekende keerpunten Shawinigan in b2; Tesla-marker 0,21 km voorbij het routeeinde van b4.
- Sitelaag `lithium-sitelaag.json` heeft geen NAL-site (centraal toevoegen, zie brief [9]).

## 8 · Bronnen
[1] Elevra Lithium, Form 6-K (juni 2026): NAL FY26 197.967 dmt, 5,0%; prijs FOB Port of Québec; geen afnemers genoemd — https://www.sec.gov/Archives/edgar/data/1739016/000114036126029882/ef20078904_6k.htm
[2] S-K 1300 TRS NAL Project (2025): §16.5 Piedmont 50% = 113.000 t droog SC6/j; §16.6 truck → Val-d'Or → CN naar Québec City port — https://www.sec.gov/Archives/edgar/data/1728205/000172820525000047/ex963s-k1300nalproject.htm
[3] Industrial Info Resources, Tesla start Robstown-raffinaderij: concentraat uit NAL (Piedmont), haven niet genoemd — https://www.industrialinfo.com/iirenergy/industry-news/article/tesla-starts-up-us-first-large-scale-lithium-refinery-in-texas--337356
[4] SmallCaps, Piedmont-Tesla-overeenkomst: ~125.000 t SC6, H2 2023 – eind 2025, +3 jaar optie, bron NAL — https://smallcaps.com.au/article/piedmont-lithium-tesla-agreement-spodumene-offtake-north-american-project
[5] Argus Media, 15-01-2026, Tesla begint Robstown (NAL en Kathleen Valley; pagina bij herlezen leeg, inhoud via [10]) — https://www.argusmedia.com/en/news-and-insights/latest-market-news/2776390-tesla-begins-ops-at-texas-lithium-refinery
[6] Kitco, 30-03-2023, NAL herstart, leveringen naar Port of Québec City — https://www.kitco.com/news/article/2023-03-30/commercial-production-begins-north-american-lithium-project-quebec
[7] Mining Weekly, 18-10-2022, Sayona/Solurail spoorcontract C$43 mln — https://www.miningweekly.com/article/sayona-secures-rail-link-for-nal-spodumene-2022-10-18
[8] Piedmont, eerste commerciële zending NAL uit Québec, 1-8-2023 — https://www.businesswire.com/news/home/20230801263159/en/Piedmont-Lithium-Announces-First-Commercial-Shipments-From-North-American-Lithium
[9] Eigen brief `v2/design/routebrieven/lithium-nal-quebec.md` (ankers, b1/b2, gebakken 2026-10-09)
[10] Eigen brief `v2/design/routebrieven/lithium-kathleenvalley-robstown.md` (Corpus Christi-kade, b4, Tesla-anker, Argus-samenvatting)
[11] Eigen MARNET-meting `hecht_marnet.py route` kade → kade, 2026-10-31: 6.153,8 km, 1.383 punten, 0 landconflicten

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)

**Uitvoer:** `v2/data/stroomroute-lithium-nal-robstown.json` (84,1 KB, contract versie 2, punt_formaat lonlat) · functie `bak_lithium_nal_robstown` in `v2/tools/bak_stromen.sh` · geen nieuwe profielen. **4 benen · 7.025,6 km · 4.317 punten · 5 markers.**

| # | modaliteit | km (gebakken) | punten | stippel | brief-doel | naad naar vorig been |
|---|---|---|---|---|---|---|
| b1 | truck | 60,8 | 610 | nee | kopie nal-quebec b1; geen wegkm gepubliceerd (hemelsbreed 33, OSRM 61,0 = indicatie) → **−0,3%** t.o.v. OSRM [indicatie] | — |
| b2 | spoor | 768,3 | 1.935 | nee | kopie nal-quebec b2; geen spoorkm gepubliceerd, eigen netmeting | 0,20 km |
| b3 | zee (MARNET + VS-trackgraaf) | 6.153,8 | 1.383 | nee | 6.153,8 proefrun (identiek) | 1,11 km |
| b4 | truck | 42,7 | 389 | nee | kopie kathleenvalley b4; OSRM 42,3 indicatie → **+0,9%** [indicatie] | **1,43 km** (procesgat in de havenkom, < 5 km) |

**Markers** (5): La Corne 0,00 km van de lijn · Solurail Val-d'Or 0,00 km · Beauport 0,14 km · Corpus Christi-kade 0,00 km · Tesla 0,21 km (anker ≠ routeerpunt: lijn eindigt op de CR 28-vertex).

**Recept** (vanuit de repo-root, `PYTHONIOENCODING=utf-8`):
1. b1, b2, b4: letterlijke kopie van de bestaande geojson (`lithium-nal-quebec-weg-plant-valdor.geojson`, `spoorroute-lithium-nal-quebec-valdor-beauport.geojson`, `lithium-kathleenvalley-robstown-weg-corpuschristi-tesla.geojson`); geen wegscan, geen spoorrun.
2. b3: `hecht_marnet.py route --been "zee|…|46.8330,-71.1985|27.8112,-97.4045"` (262 track-edges + 84 MARNET-edges + 1 connector; snap Beauport 1,257 km, snap Corpus Christi 1,432 km; 5.890,6 km MARNET + 262,7 km track; lengte-invariant +0,483 km = de naden).
3. Bake: `bash v2/tools/bak_stromen.sh lithium-nal-robstown` (zwaar-slot).

**Toets:** versie 2 / lonlat / modaliteiten truck, spoor, zee, truck binnen de set / elk been ≥ 2 punten / 84,1 KB ✔ · `toets_knikken`: 22 knikken ≥ 60° waarvan 7 omkeringen en 5 terugloop (b2: de twee bekende Shawinigan-keerpunten uit de kopie; b3: Corpus Christi; b4: CR 28-knooppunt en TX 44 × US 77, ook uit de kopie) · `toets_rechte_benen --min-km 5`: geen been van deze stroom in de lijst · naden 0,20 / 1,11 / 1,43 km, alle < 5 km · markers allemaal ≤ 0,21 km van hun lijn.

**Toelichting**
- **Geen stippel, geen haven-aanloop, geen leiding, geen vlucht.** Corpus Christi: de dichtstbijzijnde zeeknoop 4842 ligt 6,4 km van de kade (> 5 km), maar de router hecht via de VS-trackgraaf op 1,43 km; de naad b3 → b4 is daarmee < 5 km en er is, net als bij lithium-kathleenvalley-robstown, bewust geen aanloop (op last van de haalbaarheidstoets).
- **Aannemelijk (één bron):** b3 en b4 staan zo in de beennaam; de lijn is doorgetrokken. Geen zending Québec → Corpus Christi gepubliceerd (§7).
- **b3 staart:** het laatste deel (≈ 262 km) volgt VS-trackgraaf-edges langs de Texaanse kust (Freeport-ingang bij 28.90, -95.38, daarna kustwaarts naar Port Aransas en Corpus Christi); identiek aan de staart van kathleenvalley b3. Een scherpe bocht (170°, R 3 m) bij de Freeport-ingang en een terugloop in het Inner Harbor bij Corpus Christi (27.819, -97.430) zijn routerresultaat, niet nader onderzocht.
- **Verschil met de brief:** naad b2 → b3 is 1,11 km (brief schatte 1,4 km); spoorsnap 0,19 + zeesnap 1,26 telt niet lineair op.

**Lessen**
- Een stroom die alleen uit kopieën plus één MARNET-been bestaat bakt in één commando (~2 min incl. het laden van de graaf); de beennaam noemt de kopie, de brief bewaart de herkomst.
