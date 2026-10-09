# Routebrief (licht) · Zeldzame aardmetalen · Kangankunde → Nacala → Eneabba (Australië)

**stroom-id:** `ree-kangankunde-eneabba` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** monazietconcentraat (55% TREO) van Lindians Kangankunde-project (Balaka-district, Malawi) gaat per **truck** ~765 km (OSRM-indicatie) via de M1, M8, Ntaja/T393, de grens bij Nayuchi en de N13/N1/N8 naar de Nacala-containerterminal, per **zeeschip** (MARNET) naar de haven van Geraldton, en per **truck** ~156 km over de Brand Highway naar Iluka's Eneabba-raffinaderij (aannemelijk: één bron voor de bestemming); de lijn stopt daar.
**Welke as van het verhaal:** de eerste niet-Chinese Afrikaanse monazietstroom naar een westerse raffinaderij. **Bindende offtake 6 kt/j monazietconcentraat gedurende 15 jaar (90 kt, 9.600 t NdPr)** [2][4] ≈ **3,3 kt REO/j** (6 kt × 55% TREO, eigen omrekening); Stage 1 produceert ~15,3 kt/j concentraat (≈ 8,4 kt REO/j; het meerdere is deels aan Gerald Metals gecontracteerd [3]). Peiljaar 2026: **volume nul tot eerste productie Q4 2026**, raffinaderij-commissioning mid-2027 [1][2][5][6].

## 1 · Ketenkaart
```
Kangankunde-project `ree-kangankunde-mijn` (Balaka-district, 13 km ZZW van Balaka)
   ──(b1 truck · M1 → M8 → Ntaja Road (S131) → T393 → grens Nayuchi → N13 (via Cuamba, Nampula) → N1/N8 · ~765 km OSRM, geen wegkm gepubliceerd)──►
Nacala containerterminal `ree-nacala-kade` (oostoever) ──(haven-aanloop 152,1 km, stippel)──► zeeknoop 2148
   ──(b2 zee · MARNET · ~8.915 km knoop-knoop)──► zeeknoop 3877 ──(haven-aanloop 21,6 km, stippel)──►
Port of Geraldton `ree-geraldton-kade` ──(b3 truck · John Willcock Link → Brand Highway · ~156 km OSRM)──►
Iluka Eneabba-raffinaderij `ree-eneabba-raffinaderij` (aannemelijk) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (aannemelijk: modus niet gepubliceerd, spoor 9 km oostelijk) | `ree-kangankunde-mijn` → `ree-nacala-kade` | M1 → M8 → Ntaja Road S131 → T393 → grens Nayuchi/Entre Lagos → N13 (Cuamba–Nampula) → N1/N8 via Namialo en Monapo | hemelsbreed 622 km, geen wegkm; OSRM-indicatie 765,4 km (140,7 Malawi + 624,7 Mozambique) [9] | maak_stroombeen_weg (extracts malawi + mozambique) | nee (toegangsweg 0,9 km tot OSM-weg; stippel alleen als de snap > 2 km blijkt) |
| — | B | zee (haven-aanloop) | `ree-nacala-kade` → zeeknoop 2148 (-15.0, 41.7) | Baai van Nacala → open zee | 152,1 gemeten (kade → knoop, MARNET reikt niet) | **letterlijke kopie** `aanloop-nacala.geojson` (grafiet-balama-laixi) | ja — MARNET reikt niet |
| b2 | B | zee (aannemelijk: één bron) | zeeknoop 2148 → zeeknoop 3877 (-28.6355, 114.4396) | MARNET beslist; geen gepubliceerde zeekm | 8.915,3 gemeten (hemelsbreed kade-kade 7.690) | MARNET (hecht_marnet --been) | nee |
| — | B | zee (haven-aanloop) | zeeknoop 3877 → `ree-geraldton-kade` | haven-aanloop Geraldton, **aankomst** | 21,6 gemeten | **omgekeerde kopie** `ree-kangankunde-eneabba-aanloop-geraldton-aankomst.geojson` (FeatureCollection, uit lithium-kathleenvalley-robstown) | ja — MARNET reikt niet |
| b3 | C | truck (aannemelijk: één bron voor de bestemming) | `ree-geraldton-kade` → `ree-eneabba-raffinaderij` | John Willcock Link → Brand Highway (Highway 1) → Iluka Operations Rd | hemelsbreed 138 km, geen wegkm; OSRM-indicatie 155,7 km [9] | maak_stroombeen_weg (extract australie) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-kangankunde-mijn` | mijn / concentratieplant (laadplek) | Kangankunde-project, deposit-heuvel | -15.1261, 34.9106 | [8] OSM-top; [3] 13 km ZZW Balaka | aannemelijk (z15 gezien: bosbedekte heuvelrug in akkerland; 1,4 km WNW een kaal rood terrein met gebouwtjes en toegangsweg uit het NW = vermoedelijk bouwplaats/plant, ca. -15.1270, 34.9035, niet door een bron benoemd; het anker is het deposit, niet de plant) |
| `ree-nacala-kade` | overslag truck → zee | Porto de Nacala — containerterminal oostoever | -14.5383, 40.6673 | hergebruik letterlijk `grafiet-balama-laixi.md` / `grafiet-balama-vidalia.md` [11] | aannemelijk voor deze lading (daar bron-gelegd: kadekranen en containeryard; Lindian noemt alleen "Nacala Port", niet de terminal; de kolenkade westoever is bewust niet gebruikt) |
| `ree-geraldton-kade` | overslag zee → truck | Port of Geraldton, pier met bulkschuren | -28.7740, 114.5930 | hergebruik letterlijk `lithium-kathleenvalley-robstown.md` [11] | aannemelijk (daar z15 gezien: pier met schuren; welke berth het concentraat lost is onbekend; Geraldton als invoerhaven is aanname) |
| `ree-eneabba-raffinaderij` | fabriek (raffinaderij) | Iluka Eneabba Mine Site, Operations Rd | -29.8702, 115.2695 | [5] 5 km ZZW van het dorp; [8] OSM "Iluka Operations" | aannemelijk (z14/z15 gezien: weg door leeg struikgewas naar een gebouwencompound met witte zandvlakten en een put ~1,8 km ZO op -29.8775, 115.2856, mijnterrein met pits oostelijk; beeld oogt van vóór de bouw; dorpscentroïde -29.8184, 115.2724 is geen anker) |

## 4 · Via-punten (alleen b1 en b3; lat, lon; in profielen `(lon, lat)`)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | M1 × M8, NW van Balaka (buiten het centrum) | -14.9581, 34.8942 | pint M8 oostwaarts naar Ntaja i.p.v. door de M1 naar Liwonde |
| b1 | 2 | Ntaja, begin Ntaja Road (S131) | -15.0703, 35.2270 | pint de S131/T393-route naar de grens i.p.v. een zuidelijke omweg |
| b1 | 3 | Nayuchi, grens Malawi/Mozambique (= Entre Lagos) | -14.9793, 35.8731 | hergebruik letterlijk `kolen-moatize-nacala.md`; pint de grensovergang |
| b1 | 4 | N13, 18 km oostelijk van Cuamba (buiten de stad) | -14.7844, 36.7036 | pint de N13 naar Nampula i.p.v. de Lichinga-tak of het spoor |
| b1 | 5 | N13, westelijke aanloop Nampula | -15.0132, 39.1227 | pint de aanloop vóór de stad; geen stadscentrum |
| b1 | 6 | Namialo (N1 × N12) | -14.9231, 39.9882 | hergebruik letterlijk uit profiel `grafiet-balama-nacala` |
| b1 | 7 | Monapo | -14.9155, 40.2972 | hergebruik letterlijk uit profiel `grafiet-balama-nacala` |
| b3 | 1 | Brand Highway, 4,6 km ten ZO van de pier | -28.7869, 114.6153 | pint de uitgang John Willcock Link → Brand Hwy |
| b3 | 2 | Brand Highway, 7 km ten O van Dongara | -29.2594, 115.0059 | blijft op Highway 1; geen sluiproute |
| b3 | 3 | Brand Hwy × Iluka Operations Rd | -29.8635, 115.2522 | pint de afslag naar de site (1,8 km vóór het anker) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kangankunde-plant (Stage 1) | Lindian Resources | erts (2,9% TREO) → monazietconcentraat 55% TREO, gebagd | ~15,3 kt/j concentraat (nominaal 15 kt/j), 450 kt erts/j, 45 jaar | [1][3] |
| Eneabba rare earths refinery | Iluka Resources | monazietconcentraat → NdPr/Dy/Tb-oxide | voeding 55 kt/j → 17,5 kt/j REO-oxide; commissioning mid-2027, >50% gebouwd (jun. 2026) | [5][13] |

## 6 · Stoppunt
De lijn eindigt bij de Eneabba-raffinaderij: Iluka is de enige met naam genoemde afnemer van Kangankunde-monaziet (binding offtake, voeding Eneabba) en dat is het eindpunt van de gedocumenteerde keten; fase D en E vervallen (producten gaan per road train naar Fremantle [5], geen bron noemt een afnemer van de oxiden).

## 7 · Open punten
- **Modus b1 niet gepubliceerd:** de bron zegt alleen "transported to Nacala Port" [3]; de Nacala-spoorlijn ligt 9 km oostelijk (Nkaya-splitsing -15.1173, 35.0230 uit de kolenbrief). Truck is een werkaanname; spoor Nkaya → Nayuchi → Cuamba → Monapo → Nacala (kolenbrief, ~714 km) blijft het alternatief.
- **Invoerhaven niet gepubliceerd:** geen bron zegt dat Geraldton de invoerhaven is (Iluka heeft wel een scheidingsfabriek bij Narngulu, Geraldton [6]; de EPA noemt Fremantle alleen voor uitvoer [5]); Geraldton en de Nacala-terminal zijn aannemelijk.
- **Volume en looptijd:** 6 kt/j is contract, geen gerealiseerde lading; Stage 1 (15,3 kt/j) is breder dan de Iluka-offtake; een tweede contract met Gerald Metals (45 kt, sept. 2023, bestemming onbekend) [3] is niet getekend. Eerste productie Q4 2026 [1].
- **Plantlocatie Kangankunde onbekend:** anker = deposit (OSM-top); het rode terrein 1,4 km WNW is mogelijk de plant. Toegangsweg is 5 km "unsealed" [3]: wegklasse in OSM controleren (corridorKlassen).
- **Eneabba-terrein niet exact:** de bron geeft alleen "5 km ZZW van het dorp"; het anker is een OSM-wegpunt, de compound ligt 1,8 km ZO. Toegang kan privé zijn (eindToegangPrivaat testen).
- **Km:** b1 en b3 zijn OSRM-indicaties, geen bedrijfsopgave: de ±15%-toets geldt als indicatie. Zeekm is een routeerresultaat.
- **ANSTO-uitslag** (concentraat niet Klasse 7 [12], alleen zoekresultaat gelezen) verklaart waarom een gewone container volstaat; niet als bewijs gebruikt.

## 8 · Bronnen
[1] Lindian Resources, Kangankunde-projectpagina — Q4 2026 eerste productie, Stage 1 20 ktpa / Stage 2 +100 ktpa (doel), reserve 23,7 Mt @ 2,9% TREO, "strategic partnership with Iluka". https://lindianresources.com.au/projects/kangankunde/
[2] Small Caps, "Lindian signs Iluka offtake deal", 2025 — 6.000 t/j × 15 jaar = 90.000 t (9.600 t NdPr), voeding Eneabba, commissioning 2027, 55% TREO / 19,35% NdPr, US$20 mln lening. https://smallcaps.com.au/article/lindian-resources-iluka-offtake-deal-advance-kangankunde-development
[3] NS Energy, Kangankunde project — 90 km N van Blantyre, 13 km Z van Balaka, M1 + 5 km onverhard, Nacala-spoor 9 km oostelijk, gebagd naar Nacala Port, Stage 1 15,3 ktpa @ 55%, Gerald Metals 45.000 t (sept. 2023). https://www.nsenergybusiness.com/projects/kangankunde-rare-earths-project-malawi/
[4] Mining Weekly, "Lindian, Iluka enter binding offtake agreement…", 2025-08-06 (alleen titel via zoekresultaat; pagina 403). https://www.miningweekly.com/article/lindian-iluka-enter-binding-offtake-agreement-for-rare-earth-concentrate-from-malawi-2025-08-06
[5] EPA Western Australia, Eneabba Rare Earth Refinery Project — raffinaderij op de Iluka Eneabba Mine Site, 5 km ZZW van het dorp, 17.500 t/j oxide, road trains naar Fremantle. https://www.epa.wa.gov.au/proposals/eneabba-rare-earth-refinery-project
[6] Wikipedia, Iluka Resources — monaziet uit Eneabba, concentrator 2022, raffinaderij in aanbouw. https://en.wikipedia.org/wiki/Iluka_Resources
[7] Wikipedia, Brand Highway — 370 km Muchea–Geraldton via Eneabba en Dongara (Highway 1). https://en.wikipedia.org/wiki/Brand_Highway
[8] OpenStreetMap/Nominatim — Kangankunde (peak) -15.12613, 34.91059; Iluka Operations (way 229606093) -29.87019, 115.26950; Entre Lagos -14.9888, 35.8931. https://nominatim.openstreetmap.org
[9] OSRM public demo (OSM-gebaseerd, geen publicatie) — Kangankunde → Nayuchi → Nacala 765,4 km; Geraldton → Eneabba 155,7 km. https://router.project-osrm.org
[10] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15) — `v2/build-cache/satcheck/sat-ree-kangankunde-eneabba-{kangankunde,eneabba,eneabba-z15}.png`.
[11] Atlas-brieven: `grafiet-balama-laixi.md` / `-vidalia.md` (Nacala-kade, aanloop-nacala.geojson), `lithium-kathleenvalley-robstown.md` (Geraldton-kade, aanloop), `kolen-moatize-nacala.md` (Nayuchi, Nkaya), profiel `grafiet-balama-nacala` (Namialo, Monapo).
[12] Mining Weekly, "ANSTO ruling gives Lindian transport and cost edge at Kangankunde", 2026-02-26 (betaalmuur; alleen zoeksamenvatting). https://www.miningweekly.com/article/ansto-ruling-gives-lindian-transport-and-cost-edge-at-kangankunde-2026-02-26
[13] Iluka ASX-bericht 2026-06-23 — refinery >50% gebouwd, commissioning mid-2027 (alleen via zoeksamenvatting). https://announcements.asx.com.au/asxpdf/20260623/pdf/070wvw8t4gwxfh.pdf

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)

**Uitvoer:** `v2/data/stroomroute-ree-kangankunde-eneabba.json` (188,1 KB, contract versie 2, punt_formaat lonlat) · functie `bak_ree_kangankunde_eneabba` in `v2/tools/bak_stromen.sh` · profielen `ree-kangankunde-eneabba-mijn-nacala` en `ree-kangankunde-eneabba-geraldton-eneabba` in `v2/tools/maak_stroombeen_weg.py`. **5 benen (2 stippel) · 10.012,2 km · 9.250 punten · 4 markers.**

| # | modaliteit | km (gebakken) | punten | stippel | brief-doel | naad naar vorig been |
|---|---|---|---|---|---|---|
| b1 | truck | 768,2 | 7.395 | nee | 766 (OSRM-indicatie, geen wegkm) → **+0,3%** [indicatie, norm ±15%] | — |
| b1a | zee, haven-aanloop Nacala | 152,1 | 113 | **ja** (MARNET reikt niet) | 152,1 gemeten | 0,00 km |
| b2 | zee (MARNET) | 8.915,3 | 903 | nee | 8.915,3 gemeten | 0,00 km |
| b2a | zee, haven-aanloop Geraldton (aankomst) | 21,6 | 15 | **ja** (MARNET reikt niet) | 21,6 gemeten | 0,00 km |
| b3 | truck | 155,0 | 824 | nee | 156 (OSRM-indicatie, geen wegkm) → **-0,6%** [indicatie] | 0,00 km |

**Markers** (4): Kangankunde-deposit 0,00 km van de lijn · Nacala-containerterminal 0,00 km · Port of Geraldton 0,00 km · Eneabba-raffinaderij 0,00 km.

**Recept** (vanuit de repo-root, `PYTHONIOENCODING=utf-8`; pyosmium geblokkeerd en Overpass onbetrouwbaar, dus `wegscan_puur.py`):
1. b1: `python v2/tools/wegscan_puur.py --profiel ree-kangankunde-eneabba-mijn-nacala` (extracts malawi + mozambique, 9 via-punten, `corridorKlassen` tertiary/unclassified, `eindToegangPrivaat`, `vensterKm` 50). 767,6 km na snoei (774,1 voor 58 keerlusjes van 0,02-0,03 km), lengtetoets +0,2%. Etappes: 26,6 (mijn → M1 x M8) · 39,9 (→ Liwonde, M8/M3) · 75,3 (→ Nayuchi, S131/T393) · 98,9 (→ N13 bij Cuamba) · 306,4 (→ N13 bij Nampula) · 113,3 (→ Namialo, N8) · 39,6 (→ Monapo) · 74,1 (→ Nacala). Alle via-snaps ≤ 0,12 km; plant → weg 0,50 km rechte stub (anker is het deposit, geen plant).
2. b1a: LETTERLIJKE KOPIE van `aanloop-nacala.geojson` (uit `bak_grafiet`, kade → zeeknoop 2148, 152,1 km).
3. b2: `hecht_marnet.py route --been "zee|…|-15.0,41.7|-28.6355,114.4396"` (27 MARNET-edges, geen track-edges; snaps 0,000 km; lengte-invariant +0,083 km).
4. b2a: OMGEKEERDE KOPIE van `lithium-kathleenvalley-robstown-aanloop-geraldton.geojson` (zeeknoop 3877 → kade, 21,6 km, 15 punten) als `ree-kangankunde-eneabba-aanloop-geraldton-aankomst.geojson`.
5. b3: `python v2/tools/wegscan_puur.py --profiel ree-kangankunde-eneabba-geraldton-eneabba` (extract australie, 5 via-punten). 154,9 km, lengtetoets -0,7%; etappes 3,6 · 70,5 · 78,9 · 1,9 km; plant → weg 0,06 km.
6. Bake: `bash v2/tools/bak_stromen.sh ree-kangankunde-eneabba`.

**Toets:** versie 2 / lonlat / modaliteiten {truck, zee} / elk been ≥ 2 punten / 188 KB ✔ · naden alle 0,00 km (geen enkele > 5 km) · `toets_knikken`: 29 knikken ≥ 60° (b1 19, b3 8, zee 2), 1 omkering ≥ 150° en 0 terugloop; de omkering is het einde van b3 bij het raffinaderij-anker (-29.87033, 115.26978, 178,2°, pad ÷ hemelsbreed 1,1 = "scherpe bocht, echt": de weg komt het terrein op en de lijn sluit af) · `toets_rechte_benen --min-km 5`: geen enkel been van deze stroom in de lijst (omwegfactor b1 1,235 · b1a 1,243 · b2 1,18 · b3 1,12).

**Toelichting**
- **Stippel = haven-aanloop Nacala en Geraldton.** MARNET reikt niet tot de kade (Nacala kade → zeeknoop 2148: 152,1 km; Geraldton zeeknoop 3877 → kade: 21,6 km). Beide zijn gemeten kortste paden over water en blijven stippel: "hier reikt het net niet". Geen enkel landbeen is stippel.
- **Aannemelijk (één bron)** voor de modus b1 (truck; spoor Nkaya-Nacala is het alternatief), de Nacala-terminal, Geraldton als invoerhaven en de plek van de raffinaderij: dat staat in de beennamen, de lijnen zijn doorgetrokken. **Volume nul tot eerste productie Q4 2026** (de weg is gemeten, de lading nog niet).
- **⚠️ Via-punt 2 van b1 is Liwonde, niet Ntaja.** De brief (§4) noemt (-15.0703, 35.2270) "Ntaja"; Nominatim zet Liwonde-city op (-15.0702, 35.2268) en Ntaja-dorp op (-14.862, 35.524). De route volgt wel de brief-corridor (M8 → M3 bij Liwonde → S131 "Ntaja Road" → T393 → Nayuchi) en blijft 14 km van het dorp Ntaja; alleen de naam van het via-punt klopt niet.
- **⚠️ Namialo-via-punt is 0,22 km verschoven** van het briefpunt (-14.9231, 39.9882) naar de N8-vertex (-14.921401, 39.98712). Met `corridorKlassen` unclassified snapte het briefpunt (0,10 km) op way 327752328, een losse unclassified-zijweg in een eigen component, en gaf de eerste run "geen wegpad tussen punt 5 en 6". Zelfde plek, nu op de doorgaande weg (profielcommentaar vermeldt het).
- **Plant → weg 0,50 km rechte stub** (net boven de 0,5 km-drempel van het wegtool): het anker is het deposit, de toegangsweg is 5 km onverhard; de eerste 6,4 km van de lijn loopt over residential/unclassified, geen track. Past bij de open punten van §7 (plantlocatie onbekend); bevinding, geen via-punt bijgeschoven.
- **b1 loopt dwars door Nampula** (0,65 km van het centrum): N13 → N8 heeft daar geen corridorkeuze; de aanloop-via-punten liggen buiten de stad.
- **Anker ≠ routeerpunt (Eneabba):** het anker is het OSM-wegpunt van "Iluka Operations"; de compound ligt 1,8 km ZO. De lijn eindigt op het anker (haakse bocht van 178° over de laatste meters), geen last-mile-benen.

**Lessen**
- Een via-punt dat met een ruimere `corridorKlassen` op een zijweg-component snapt geeft "geen wegpad": tel de componenten van de nabije vertices (`fetch_landnet._wegen_graaf`, zelfde afronding op 6 decimalen) en leg het punt op een vertex van de doorgaande weg.
- Controleer de plaatsnaam van een via-punt tegen Nominatim: Ntaja en Liwonde liggen 33 km uit elkaar en de brief had ze verwisseld.
- Een Australië-scan kost ~165 s (953 MB) en vraagt een reus-slot plus een weg-slot; de Malawi + Mozambique-scan ~110 s.
