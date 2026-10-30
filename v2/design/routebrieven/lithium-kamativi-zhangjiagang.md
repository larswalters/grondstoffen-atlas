# Routebrief (licht) · lithium — Kamativi → Beira → Zhangjiagang (Zimbabwe → China)

**stroom-id:** `lithium-kamativi-zhangjiagang` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat van de Kamativi-mijn (Kamativi Mining Company, **Yahua** via Sichuan PD Technology — niet Zhejiang Huayou, zoals sitelaag en ontwerp zeiden [1][3][6]; Matabeleland Noord) gaat per **truck** via de A8 naar Bulawayo, de A5 naar Harare en de A3/N6 naar Forbes/Machipanda en over de EN6 naar de kade van Beira, per **bulkcarrier** via Malakka naar de Yangtze-monding en over de Yangtze naar Zhangjiagang. Beira is gebronnd voor het eerste convooi (2024) [1]; Zhangjiagang is *aannemelijk: één bron* (SunSirs noemt voor de Yahua-lading Zhangjiagang of Guangzhou-Nansha, projectie) [2].
**Welke as van het verhaal:** tweede Zimbabwaanse Chinese-eigenaarmijn naast Bikita en Arcadia: in het westen van het land, 600 km hemelsbreed van de Beira-corridor. Eerste convooi 31-01-2024 (±300 t, eerste partij 5.000 t naar China via Beira) [1]; exportstop feb. 2026, Yahua kreeg in apr. 2026 zes maanden quota, concentraatverbod jan. 2027, lithiumsulfaatfabriek (75 kt/j) pas gepland vanaf juli 2027 [3][4]. **Volume:** naamplaat fase 1+2 samen 350 kt spodumeenconcentraat/j uit 2,3 Mt erts (bedrijfsopgave 2024, zoekresultaat) [6] ≈ 30 kt LCE (sitelaag B18, indicatie; eigen omrekening 350 kt SC × 5 % Li2O × 2,473 geeft 43 kt) — geen gepubliceerde productie 2025. Eenheid: kt LCE per jaar.

## 1 · Ketenkaart
```
Kamativi-plant `li-kamativi-plant` (put, plant en tailingsdam, Matabeleland Noord)
  ──(b1 truck · A8 → Bulawayo → A5 Gweru–Kwekwe–Chegutu–Harare → A3 Ruwa–Rusape–Mutare · 1.019,6 km gemeten, geen wegkm gebronnd)──►
Forbes/Machipanda-grens `li-forbes-grens` (hergebruikt)
  ──(b2 truck · EN6 Manica–Chimoio–Inchope–Dondo · 286,9 km — LETTERLIJKE KOPIE lithium-arcadia-beira b2; b3 stippel 1,8 km haventerrein)──►
Beira general-cargo-kade `li-beira-kade` (hergebruikt)
  ──(b4 stippel 7,8 km haven-aanloop · b5 zee 12.946,0 km — LETTERLIJKE KOPIE lithium-arcadia-beira; b6 stippel 8,6 km)──►
Yangtze-monding `li-yangtze-monding` (hergebruikt)
  ──(b7 binnenvaart 135,2 km + b8 stippel 0,6 km — LETTERLIJKE KOPIE)──► Zhangjiagang-kade `li-zjg-kade` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `li-kamativi-plant` → `li-forbes-grens` | A8 (Kamativi → Bulawayo) → A5 → A3/N6 | **hemelsbreed 601 km, geen wegkm**; deelbronnen Bulawayo–Harare 439 [7], Harare–Mutare 270,8 + ~8 Mutare–Forbes [8]; gemeten 1.019,6 (+7,3% t.o.v. ontwerp 950, indicatie) | maak_stroombeen_weg (zimbabwe), profiel `lithium-kamativi-zhangjiagang-plant-forbes` | nee |
| b2 | A | truck | `li-forbes-grens` → Beira-havenweg-inrit | EN6 — **letterlijke kopie** `lithium-arcadia-beira-weg-forbes-beira.geojson` | 286,9 (289 Mozambique Expert, via [11]) | kopie | nee |
| b3 | A | truck | havenweg-inrit → `li-beira-kade` | eigen terrein Beira — kopie van de stippel in arcadia-beira | 1,8 | stippel (kopie) | ja, eigen terrein |
| b4 | B | zee | `li-beira-kade` → MARNET-zeeknoop Beira | haven-aanloop — kopie van de centraal gelegde stippel | 7,8 (kade ligt 7,777 km van de zeeknoop > 5 km) | stippel (kopie) | ja, MARNET reikt niet |
| b5 | B | zee | zeeknoop Beira → Yangtze-routeerpunt | Mozambiquekanaal → Malakka — **letterlijke kopie** arcadia-beira b5 (bron bikita) | 12.946,0 | MARNET (kopie) | nee |
| b6 | B | zee | zeenet → Yangtze-bulklaag | overgang — kopie | 8,6 | stippel (kopie) | ja, net reikt niet |
| b7 | B | binnenvaart | Yangtze-monding → Zhangjiagang | zuidgeul Shuangshan — kopie `rivierbeen-yangtze-zhangjiagang.geojson` | 135,2 | kopie | nee |
| b8 | B | binnenvaart | routeerpunt → `li-zjg-kade` | aanloop ligplaats — kopie | 0,6 | stippel (kopie) | ja, anker ≠ routeerpunt |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-kamativi-plant` | mijn + plant / laadplek | Kamativi Tin and Lithium Mine, Kamativi Mining Company (Yahua) | -18.3315, 27.0505 | [1][3][4]; satellietblik z15 (`sat-lithium-kamativi-zhangjiagang-li-kamativi-site.png`) | **bron-gelegd** (z15 gezien: kruis op het plantterrein — thickeners en gebouwen W, witte uitlooggrond, open put O, tailingsdam met wit oppervlak Z); verlegd 0,9 km ZZW van het sitelaag-punt |
| `li-forbes-grens` | grensovergang | Forbes (ZW) / Machipanda (MZ) | -19.0052, 32.7123 | hergebruik, letterlijk uit lithium-arcadia-beira §3 [11] | bron-gelegd |
| `li-beira-kade` | overslag truck → zee | Beira, general-cargo-terminal Cornelder | -19.8150, 34.8340 | hergebruik uit [11]/[12]; Beira gebronnd voor Kamativi [1] | bron-gelegd (kade-ligplaats ongebrond) |
| `li-yangtze-monding` | overgang zee → rivier | Yangtze-monding | 31.42704, 121.47618 | hergebruik uit [11] | bron-gelegd |
| `li-zjg-kade` | losplek (stoppunt) | Zhangjiagang, kade Port Group | 31.96800, 120.42050 | hergebruik uit [11]; bestemming uit [2] | **aannemelijk** (één bron, projectie) |

## 4 · Via-punten (alleen b1; b2–b8 zijn kopieën)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Bulawayo-noord, A8 (8 km voor het centrum) | -20.0896, 28.5567 | pint de A8-aankomst bij Bulawayo; de corridor Kamativi → Harare loopt via Bulawayo (geen directe weg naar het noordoosten) |
| b1 | 2 | Gweru-noord, A5 (8 km voorbij het centrum) | -19.3925, 29.8249 | pint de A5 naar Harare ná de doorgang door Gweru |
| b1 | 3 | Kwekwe-noord, A5 (8 km voorbij het centrum) | -18.8606, 29.7976 | pint de A5 ná Kwekwe, tegen een route over zijwegen |
| b1 | 4 | Chegutu-oost, A5 (8 km voorbij het centrum) | -18.1202, 30.2204 | pint de A5 richting Harare ná Chegutu |
| b1 | 5 | Ruwa, A3-inrit | -17.8902, 31.2427 | pint de A3 oost ná de Harare-doorgang (zelfde punt als de Forbes-brieven) |
| b1 | 6 | Rusape, A3 (kruispunt A14) | -18.5335, 32.1257 | pint de doorgaande A3 naar Mutare i.p.v. de A14 naar Nyanga |
Alle via-punten snapten op 0,00–0,13 km van het gescande net; refs A8/A5/A3, extract zimbabwe, venster 75 km. Via-punten 1–4 liggen bewust buiten de stadscentra (centrumpunten uit het ontwerp zijn vervangen: de gemeten route veranderde 1.020,2 → 1.019,6 km).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kamativi-plant (fase 1+2) | Kamativi Mining Company / Sichuan PD Technology (Yahua) | erts uit open put en oude dumps → spodumeenconcentraat | fase 1 300 kt erts/j + 50 kt SC/j; fase 1+2 2,3 Mt erts/j → 350 kt SC/j (bedrijfsopgave 2024) | [5][6] |
| Lithiumsulfaatfabriek (gepland) | idem | concentraat → lithiumsulfaat | 75 kt/j, start gepland juli 2027 — niet getekend | [4] |

## 6 · Stoppunt
De brief stopt op de kade van Zhangjiagang: geen bron noemt de Chinese converter voor Kamativi-concentraat (Yahua draait zijn lithiumzoutfabrieken in Sichuan, niet gebronnd voor deze lading), en SunSirs geeft voor de Yahua-lading alleen de aankomsthaven (Zhangjiagang of Guangzhou-Nansha) [2]. Fase D vervalt, fase E vervalt; geen Sichuan-benen.

## 7 · Open punten
- **Eigenaar:** sitelaag `w-li-kamativi` en het ketenontwerp noemen Zhejiang Huayou; de bronnen zeggen Yahua / Sichuan PD Technology / Kamativi Mining Company [1][3][4][6]. Sitelaag niet aangepast (andermans bestand) — centraal herstellen, ook het anker (-18.3241, 27.0526 staat ~1 km N van het plantterrein; de sitelaag-notitie "kruis naast put en tailingsdam Z" klopt niet met het z15-beeld).
- **Zhangjiagang is een projectie** (SunSirs 2026-07-02, "Zhangjiagang of Guangzhou-Nansha", ligt in dezelfde tabel onder "Port Bella", niet verder verklaard) — de kade-ligplaats in Beira is niet gebronnd; Durban (SunSirs noemt het voor andere lading) is geen bron voor Kamativi.
- **Wegkm b1 niet gebronnd:** alleen deelbronnen (718,8 km Bulawayo–Forbes); Kamativi–Bulawayo (gemeten 302 km, hemelsbreed 259) heeft geen publicatie. De ±15%-toets is een indicatie.
- **Harare-doorgang:** de gemeten lijn gaat over de A5/Samora Machel door het centrum (0,3 km van het CBD-punt) naar de A3; een ringweg-variant is niet onderzocht (omweg-effect klein: Chegutu → Ruwa 121,8 km tegen ~112 km hemelsbreed).
- **Last mile plant:** het anker ligt 0,65 km van de eerste weg van het net (eerste mijl over kleine klassen 1,61 km) — onder de 2 km-grens, dus doorgetrokken, wel > 0,5 km.
- **Volume:** geen productiecijfer 2025; capaciteit uit een bedrijfsopgave in een zoekresultaat (bronpagina niet geopend), de LCE-omrekening is eigen werk en ongelijk aan de sitelaag (30 tegen 43 kt LCE).
- Bij Beira dezelfde 7,8 km haven-aanloop als arcadia-beira (rechte stippel, `maak_havenaanloop.py` vastgelopen): geen eigen versie gebouwd.

## 8 · Bronnen
[1] SMM/metal.com, 02-02-2024 — Yahua Group's Kamativi Mine begins shipping lithium concentrate: eerste convooi 31-01-2024, ±300 t, naar de haven van Beira, eerste partij 5.000 t naar China; fase 1 300 kt erts/j. https://news.metal.com/newscontent/102611200
[2] SunSirs, 02-07-2026 — Zimbabwe lithium exports: Beira hoofdroute (landtransport 3–7 dagen), Yahua/Kamativi 20–22 kt per schip, gebundeld 8–12 juni 2026, projectie aankomst Zhangjiagang of Guangzhou-Nansha 15–20 juli. https://www.sunsirs.com/uk/detail_news-34127.html
[3] Kitco/Reuters, 14-04-2026 — China's Yahua gets lithium export quota from Zimbabwe: zes maanden quota concentraat, Yahua exploiteert Kamativi, exportstop feb. 2026. https://www.kitco.com/news/off-the-wire/2026-04-14/chinas-yahua-industrial-group-gets-lithium-export-quota-zimbabwe
[4] Mining Index, 19-08-2026 — Kamativi Mining Company onder Sichuan Yahua; lithiumsulfaatfabriek 75 kt/j, start gepland juli 2027, concentraatverbod jan. 2027. https://www.miningindex.co.zw/?p=111362
[5] NewsDay, 16-07-2024 — Kamativi delays completion of processing plant: fase 1 april 2024, fase 2 uitgesteld naar sept. https://newsday.co.zw/business/article/200029656/kamativi-delays-completion-of-processing-plant
[6] Zoekresultaat (WebSearch 2026-10-30, bedrijfsopgave 2024, bronpagina's asianmetal/ZBC niet geopend): Kamativi is een JV onder Sichuan PD Technology (Yahua); fase 1 300 kt erts + 50 kt SC/j; fase 1+2 2,3 Mt erts, 350 kt SC/j. Mining Weekly/Engineering News 14-04-2026 (Yahua-quota) alleen als zoekresultaat gezien.
[7] Wikipedia, "A5 road (Zimbabwe)" — Harare–Bulawayo, ca. 439 km. https://en.wikipedia.org/wiki/A5_road_(Zimbabwe)
[8] Wikipedia, "R5 road (Zimbabwe)" — A3/R5 Harare–Mutare 270,8 km (via [11]); Mutare–Forbes ~8 km uit dezelfde brief.
[9] Wikipedia, "Kamativi" — plaats Kamativi -18.5333, 27.1167; mijn naast de plaats. https://en.wikipedia.org/wiki/Kamativi
[10] OpenStreetMap Nominatim — Kamativi (village) -18.3220, 27.0545 · Dete -18.6166, 26.8613 · Gweru -19.4616, 29.8206 · Kwekwe -18.9284, 29.8140 · Chegutu -18.1305, 30.1460. https://nominatim.openstreetmap.org
[11] `v2/design/routebrieven/lithium-arcadia-beira.md` — ankers Forbes/Beira/Yangtze/Zhangjiagang, b2–b8 (EN6 286,9 km, zee 12.946,0 km, Yangtze 135,2 km, haven-aanloop Beira) en de via-punten Ruwa, Rusape.
[12] `v2/design/routebrieven/lithium-bikita-zhangjiagang.md` — oorsprong van de Beira-, zee- en Yangtze-benen.
[13] `v2/design/lithium-sitelaag.md` — `w-li-kamativi`, capaciteit B18 (30 kt LCE-indicatie, niet primair gedocumenteerd).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)
`bash v2/tools/bak_stromen.sh lithium-kamativi-zhangjiagang` → `v2/data/stroomroute-lithium-kamativi-zhangjiagang.json` (269 KB, versie 2, lonlat, 14.407,1 km, 8 benen, 5 markers). Functie `bak_lithium_kamativi_zhangjiagang` in `bak_stromen.sh`, profiel `lithium-kamativi-zhangjiagang-plant-forbes` in `maak_stroombeen_weg.py` (b1 was al gescand; geojson uit build-cache hergebruikt, geen herscan, geen nieuwe slot-run voor de scan).

| # | modaliteit | km | naad | stippel | toets |
|---|---|---|---|---|---|
| b1 | truck | 1.020,2 (weg 1.019,6) | 0 | nee | +7,3% tegen de indicatie 950 km (hemelsbreed 601 km, geen wegkm: indicatie, geen norm) |
| b2 | truck | 286,9 | 0,01 | nee | letterlijke kopie arcadia-beira b2; -0,7% tegen 289 (Mozambique Expert) |
| b3 | truck | 1,8 | 0 | ja, eigen terrein Beira | kopie |
| b4 | zee | 7,8 | 0 | ja, haven-aanloop (kade 7,777 km van de zeeknoop) | kopie, rechte stippel (maak_havenaanloop vastgelopen bij arcadia) |
| b5 | zee | 12.946,0 | 0 | nee | kopie MARNET Beira → Yangtze-routeerpunt |
| b6 | zee | 8,6 | 0 | ja, net reikt niet | kopie |
| b7 | binnenvaart | 135,2 | 0 | nee | kopie rivierbeen-yangtze-zhangjiagang.geojson |
| b8 | binnenvaart | 0,6 | 0 | ja, anker ≠ routeerpunt | kopie |

**Markers (5):** Kamativi-plant (0,0 km van de lijn), Forbes/Machipanda (0,0), Beira-kade (0,0), Yangtze-monding (2,7 km van de lijn: anker ≠ routeerpunt, zelfde als arcadia-beira, buiten de 0,5 km-norm maar bewust), Zhangjiagang-kade (0,0).
**Recept:** b1 = wegscan zimbabwe (profiel met 6 via-punten op A8/A5/A3, snap 0,00-0,13 km); b2-b8 = regels van `bak_lithium_arcadia_beira` letterlijk gekopieerd (geen tweede versie).
**Toetsen:** geen naad > 5 km (max 0,01 km); `toets_knikken` 0 terugloop (b1 29 knikken, geen omkering); `toets_rechte_benen --min-km 5` meldt alleen de stippels b4 en b6 (die horen stippel te zijn); json.load, versie 2, punt_formaat lonlat, modaliteiten {truck, zee, binnenvaart}, elk been >= 2 punten.
**Toelichting stippels:** b3 = Beira-havenstraten hangen niet aan het doorgaande OSM-net; b4 = kade 7,8 km van de MARNET-zeeknoop, rechte stippel; b6 = MARNET houdt voor de Yangtze op; b8 = ligplaats is niet het routeerpunt. Geen lucht, spoor of leiding.
**Lessen / bevindingen:** (1) De gemeten lijn gaat door het Harare-centrum (A5 naar A3), ringweg niet onderzocht. (2) Plant-anker 0,65 km van de eerste weg, doorgetrokken (aanloop zit in het geojson). (3) Eigenaar Yahua, sitelaag w-li-kamativi noemt Huayou en ligt ~0,9 km N van het plantterrein: centraal te herstellen, niet aangeraakt. (4) Tijdens de bake gaf bash een eenmalige fout op regel 13682 (een restant van andermans functie, olie_nuevoteapa_salinacruz): het script werd door een andere agent bewerkt terwijl bash het las; geen effect op deze uitvoer, het bestand parseert (bash -n OK).
