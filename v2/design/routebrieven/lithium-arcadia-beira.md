# Routebrief (licht) · lithium — Arcadia → Beira → Zhangjiagang (Zimbabwe → China)

**stroom-id:** `lithium-arcadia-beira` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) · **status:** gebakken
**Keten in één zin:** lithiumsulfaat (Li2SO4·H2O, tussenchemisch product) van de nieuwe Huayou-fabriek op de Arcadia-mijn (Prospect Lithium Zimbabwe/Zhejiang Huayou, Goromonzi, 38 km O van Harare) gaat per **truck** over de A3/R5 Highway naar Forbes/Machipanda en over de EN6 naar de general-cargo-kade van Beira, per **bulkcarrier** door het Mozambiquekanaal en de Straat Malakka naar de Yangtze-monding en over de Yangtze naar de kade van Zhangjiagang — de Chinese aanlandingshaven is *aannemelijk: algemeen Zimbabwe→China-handelspatroon*, geen zending-specifieke bron voor dit sulfaatproduct.
**Welke as van het verhaal:** as 6 (M31 golf 6) — Zimbabwaans hardrock ná het concentraat-exportverbod: een eigen lithiumsulfaatfabriek op de mijn zelf, die (deels) het concentraat-exportmodel van de as `lithium-bikita-zhangjiagang` vervangt. Eerste lithiumsulfaat-zending van Afrika ooit: 28-04-2026, twee maanden na de concentraatbevriezing van 25-02-2026 [1]. Fabriek: US$ 400 mln, voltooid okt. 2025, naamplaat 50 kt lithiumsulfaat/j (CNBC Africa noemt mogelijk tot 60 kt) [1][2] ≈ 29 kt LCE-indicatie — **eigen omrekening** (Li2SO4·H2O ≈10,9 % Li × 5,323), door geen bron in LCE bevestigd. Vervangt deels de eerdere spodumeenconcentraat-capaciteit van dezelfde site (~450 kt SC/j ≈ 63 kt LCE, sitelaag [B17]).

## 1 · Ketenkaart
```
Arcadia-mijn + Huayou-lithiumsulfaatfabriek `li-arcadia-plant` (Goromonzi, 38 km O van Harare)
  ──(b1 truck · A3/R5 Highway via Ruwa–Marondera–Rusape–Nyazura–Mutare · ≈241 km)──►
Forbes/Machipanda-grens `li-forbes-grens` (hergebruikt anker)
  ──(b2 truck · EN6 via Manica–Chimoio–Inchope–Dondo · 289 km — letterlijke kopie, gedeeld met
     lithium-bikita-zhangjiagang b1 [Forbes→Beira-deel])──►
Beira general-cargo-kade `li-beira-kade` (hergebruikt anker)
  ──(b3 zee · Mozambiquekanaal → Malakka → Zuid-Chinese Zee · 12.946,0 km + 8,6 km stippel —
     letterlijke kopie bak_lithium/lithium-bikita-zhangjiagang; bestemming aannemelijk: één patroon)──►
Yangtze-monding `li-yangtze-monding` (hergebruikt anker)
  ──(b4 binnenvaart · Yangtze, zuidgeul Shuangshan · 135,2 km + 0,6 km stippel — letterlijke kopie
     bak_lithium)──►
Zhangjiagang-kade `li-zjg-kade` (hergebruikt anker) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `li-arcadia-plant` → `li-forbes-grens` | mijnweg → A3/R5 Highway (Ruwa, Marondera, Rusape, Nyazura, Mutare) → Forbes/Machipanda-grenspost | ≈241 (270,8 km Harare–Mutare [3] − 38 km, Arcadia ligt al voorbij Harare op deze corridor + 8 km Mutare→Forbes; geen aparte hemelsbrede berekening) | maak_stroombeen_weg (extract zimbabwe) | nee |
| b2 | A | truck | `li-forbes-grens` → `li-beira-kade` | EN6 (Manica, Chimoio, Inchope, Dondo) — **letterlijke kopie**, gedeeld been met `lithium-bikita-zhangjiagang` (Forbes→Beira-deel van diens been b1) | 289 (Mozambique Expert [7], reeds gebrond en gebakken in lithium-bikita-zhangjiagang) | maak_stroombeen_weg (kopie geojson-subset) | nee; mogelijk korte "eigen terrein"-stippel bij Beira-haventerrein — zie de bevinding daarover in lithium-bikita-zhangjiagang.md §9 |
| b3 | B | zee | `li-beira-kade` → `li-yangtze-monding` | Mozambiquekanaal → Malakka → Zuid-Chinese Zee — **letterlijke kopie** `bak_lithium`/`lithium-bikita-zhangjiagang` (incl. de bestaande stippel-overgang zeenet→Yangtze-bulklaag) | 12.946,0 + 8,6 stippel (reeds gemeten en gebakken) | MARNET (kopie) | ja, 8,6 km (overgang zeenet → Yangtze-bulklaag, net reikt niet) |
| b4 | B | binnenvaart | `li-yangtze-monding` → `li-zjg-kade` | Yangtze, zuidgeul Shuangshan — **letterlijke kopie** (`rivierbeen-yangtze-zhangjiagang.geojson` + aanloop-stippel, `bak_lithium`) | 135,2 + 0,6 stippel (reeds gemeten en gebakken) | maak_rivierbeen (kopie) | ja, 0,6 km (anker ≠ routeerpunt) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-arcadia-plant` | mijn + fabriek / laadplek | Arcadia-mijn + Huayou-lithiumsulfaatfabriek (Prospect Lithium Zimbabwe/Zhejiang Huayou), Goromonzi | -17.7715, 31.4243 | [5] | **hergebruik**, letterlijk anker `w-li-arcadia` uit `lithium-sitelaag.md` — bron-gelegd (z15 gezien, sitelaag: kruis exact op de blauwe-daken procesgebouwen, 38 km O van Harare); geen nieuwe `sat_check` nodig |
| `li-forbes-grens` | grensovergang | Forbes Border Post (ZW) / Machipanda (MZ), N6 | -19.0052, 32.7123 | [4] | hergebruik, letterlijk anker uit `lithium-bikita-zhangjiagang.md` (bron-gelegd) |
| `li-beira-kade` | overslag truck → zee | Beira, general-cargo-terminal Cornelder de Moçambique | -19.8150, 34.8340 | [4] | hergebruik, letterlijk anker uit `lithium-bikita-zhangjiagang.md` (bron-gelegd) |
| `li-yangtze-monding` | overgang zee → rivier | Yangtze-monding (Wusong/Luojing) | 31.42704, 121.47618 | [4] | hergebruik, bestaand anker (koper-tfm-durban / lithium-bikita-zhangjiagang) |
| `li-zjg-kade` | losplek (stoppunt) | Zhangjiagang — kade Zhangjiagang Port Group | 31.96800, 120.42050 | [4] | hergebruik, bestaand anker (lithium-greenbushes-zhangjiagang); bestemming *aannemelijk: één patroon* |

## 4 · Via-punten (alleen b1 — nieuw been; b2 is een letterlijke kopie, zie de via-punten 5–8 van been b1 in `lithium-bikita-zhangjiagang.md` §4 voor het Forbes→Beira-deel, hier niet herhaald)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Ruwa, A3-inrit (Goromonzi-district) | -17.8972, 31.2371 | pint de corridor oostwaarts vanaf de Arcadia-mijn/fabriek naar de doorgaande A3 i.p.v. terug Harare-centrum in |
| b1 | 2 | Marondera, A3 (kruispunt met de P3 naar Murehwa) | -18.1901, 31.5455 | pint de doorgaande A3 oost i.p.v. de P3 noordwaarts [3] |
| b1 | 3 | Rusape, A3 (kruispunt met de A14 naar Nyanga) | -18.5335, 32.1257 | pint de doorgaande A3 naar Mutare i.p.v. de A14 naar de Eastern Highlands [3] |
| b1 | 4 | Nyazura, A3 (kruispunt met de R6 naar Chivhu) | -18.7141, 32.1675 | pint de doorgaande A3 oost i.p.v. de R6 zuid naar Chivhu [3][6] |
| b1 | 5 | Mutare, A3/N6-aansluiting richting Forbes | -18.9747, 32.6705 | pint de afslag naar de Forbes/Machipanda-grenspost i.p.v. verder de stad in [6] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Huayou-lithiumsulfaatfabriek, Arcadia-mijn | Zhejiang Huayou Cobalt (Prospect Lithium Zimbabwe) | erts/concentraat op site → 50 kt/j lithiumsulfaat (Li2SO4·H2O), tussenproduct voor Li2CO3/LiOH elders | US$ 400 mln, voltooid okt. 2025, productiestart Q1 2026, eerste export 28-04-2026 | [1][2] |
| Arcadia-concentratorplant (bestaand, deels vervangen) | idem | ~450 kt SC/j naamplaat ≈ 63 kt LCE-indicatie | vóór het concentraatverbod (jan. 2027) parallel in bedrijf | [5][B17] |

## 6 · Stoppunt
De brief stopt op de kade van Zhangjiagang: geen bron (Reuters/MINING.COM [1], CNBC Africa [2], noch enige andere in de haalbaarheidstoets nagekeken bron — CNBC Africa/Mining Weekly/Ecofin Agency/Discovery Alert) noemt een haven of schip voor de eerste sulfaatzending; de Beira-route en Zhangjiagang als Chinese aanlandingshaven zijn *aannemelijk: algemeen Zimbabwe→China-handelspatroon*, hergebruikt van de gebrondere `lithium-bikita-zhangjiagang`-as (waar hetzelfde patroon wél voor het concentraat is aangetoond, SunSirs). Fase C/D (converter/afnemer) is voor dit sulfaatproduct niet gebrond — geen bron koppelt deze specifieke lading aan een Chinese fabriek; fase D vervalt, fase E vervalt.

## 7 · Open punten
- **Geen zending-specifieke bron voor haven/schip** van de eerste Arcadia-sulfaatzending (27/28-04-2026) — bevestigd nagekeken (haalbaarheidstoets): CNBC Africa, Mining Weekly, Ecofin Agency en Discovery Alert melden alleen de exportgebeurtenis zelf, geen havennaam. Het "aannemelijk"-label blijft daarom terecht, geen overclaim.
- **Wegkm b1 (Arcadia → Forbes) is een berekening, geen directe bron**: geen artikel geeft de rit Arcadia–Forbes als geheel; ≈241 km is 270,8 km Harare–Mutare (Wikipedia R5/A3 Highway [3]) − 38 km (Arcadia ligt al voorbij Harare op de corridor) + 8 km (Mutare→Forbes) — de ±15%-toets geldt hier als echte norm (binding uit de haalbaarheidstoets), niet als indicatie.
- **Via-punten b1 zijn corridor-junctions uit Wikipedia/OSM, niet zelf op de exacte wegvertex geverifieerd** binnen het webbudget — de bak-agent routeert over het echte OSM-wegnet (extract zimbabwe), dus de precieze ligging volgt uit die routering.
- **Beira-ligplaats** voor dit sulfaatproduct blijft ongebrond (al zo genoteerd in de hergebruikte `lithium-bikita-zhangjiagang`-brief voor het concentraat).
- **LCE-omrekening (29 kt) is een eigen aanname** (Li2SO4·H2O ≈10,9 % Li × 5,323) — door geen bron in LCE bevestigd; de fabriek publiceert alleen tonnage lithiumsulfaat.
- **Overlap concentraat/sulfaat op dezelfde site**: de sitelaag [B17] noteert nog de oude concentraatcapaciteit (~450 kt SC/j ≈ 63 kt LCE); hoe de mix concentraat/sulfaat na het exportverbod van jan. 2027 verdeeld wordt is niet gepubliceerd — deze brief tekent uitsluitend de nieuwe sulfaat-as.

## 8 · Bronnen
[1] Reuters via MINING.COM, 28-04-2026 — "China's Huayou reports first lithium salt exports from Zimbabwe": eerste Afrikaanse lithiumsulfaat-zending, omvang niet vrijgegeven, twee maanden na de concentraatbevriezing van 25-02-2026, fabriek US$ 400 mln voltooid okt. 2025, naamplaat 50.000 t/j lithiumsulfaat, concentraatverbod vanaf jan. 2027, geen havennaam genoemd. https://www.mining.com/web/chinas-huayou-reports-first-lithium-salt-exports-from-zimbabwe/
[2] CNBC Africa, 17-10-2025 — "Huayou to start Zimbabwe lithium sulphate production early 2026": locatie Arcadia-mijn (Prospect Lithium Zimbabwe), capaciteit >50.000 t/j (mogelijk tot 60.000 t), US$ 400 mln, productiestart Q1 2026, geen route/haven genoemd. https://www.cnbcafrica.com/2025/huayou-to-start-zimbabwe-lithium-sulphate-production-early-2026
[3] Wikipedia, "R5 road (Zimbabwe)" — A3/R5 Highway Harare–Mutare, 270,8 km, via Marondera (kruising P3) en Rusape (kruising A14), aansluiting op de Beira-corridor via Machipanda Border Post. https://en.wikipedia.org/wiki/R5_road_(Zimbabwe)
[4] `v2/design/routebrieven/lithium-bikita-zhangjiagang.md` (M29, dezelfde sessie) — hergebruikte ankers `li-forbes-grens`/`li-beira-kade`/`li-yangtze-monding`/`li-zjg-kade` en de benen Forbes→Beira (EN6, 289 km), zee (12.946,0 km + 8,6 km stippel) en binnenvaart (135,2 km + 0,6 km stippel), letterlijk gekopieerd.
[5] `v2/design/lithium-sitelaag.md` / `lithium-sitelaag.json` — anker `w-li-arcadia` (Arcadia Lithium, Huayou/Prospect Lithium Zimbabwe), -17,7715/31,4243, bron-gelegd (Nominatim + z15-satellietblik), capaciteitsindicatie [B17].
[6] OpenStreetMap (ODbL) via Nominatim — Ruwa -17,89716/31,23709 · Marondera -18,19010/31,54554 · Rusape -18,53348/32,12568 · Nyazura -18,71412/32,16746 · Mutare -18,97466/32,67047 · Goromonzi -17,85544/31,37610. https://www.openstreetmap.org
[7] Mozambique Expert — "Mozambique's EN6: Beira to Zimbabwe" — EN6 Beira–Machipanda 289 km (al gebrond in lithium-bikita-zhangjiagang.md, bron [13] daar). https://www.mozambiqueexpert.com/en/mozambiques-en6-beira-to-zimbabwe/

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**7 benen · 13.662,2 km · 8.034 punten · 5 markers.** `v2/data/stroomroute-lithium-arcadia-beira.json` (160,5 KB).

| # | modaliteit | km | naad met vorige | stippel | recept |
|---|---|---|---|---|---|
| b1 | truck | 283,1 | 0,000 km | nee | **NIEUW** — profiel `lithium-arcadia-beira-plant-forbes` in `maak_stroombeen_weg.py`, extract zimbabwe |
| b2 | truck | 286,9 | 0,006 km | nee | **letterlijke kopie** — Forbes→Beira-subsegment (idx 2948→einde) van `lithium-bikita-zhangjiagang-weg-bkplant-beira.geojson`, opgeslagen als `lithium-arcadia-beira-weg-forbes-beira.geojson` |
| b3 | truck | 1,8 | 0,000 km | ja — eigen terrein | letterlijke kopie (coördinaten) uit `bak_lithium_bikita_zhangjiagang` |
| b4 | zee | 12.946,0 | 7,777 km ⚠️ | nee | letterlijke kopie (coördinaten) uit `bak_lithium_bikita_zhangjiagang` — **de naad is een INGEËRFDE eigenschap van de gekopieerde bron** (Beira-kade snapt op 7,777 km van haar MARNET-zeeknoop; dezelfde 7,777 km staat identiek in `stroomroute-lithium-bikita-zhangjiagang.json`), geen nieuwe fout en niet dichtgetrokken — een haven-aanloop bouwen zou de brontekst van `bak_lithium_bikita_zhangjiagang` moeten wijzigen, en dat is een andere agent se functie |
| b5 | zee | 8,6 | 0,000 km | ja — zeenet→Yangtze-bulklaag | letterlijke kopie |
| b6 | binnenvaart | 135,2 | 0,000 km | nee | letterlijke kopie — gedeeld bestand `rivierbeen-yangtze-zhangjiagang.geojson` |
| b7 | binnenvaart | 0,6 | 0,000 km | ja — anker≠routeerpunt | letterlijke kopie |

**Markers:** alle 5 ankers uit §3 op de lijn: Arcadia-plant 0,1 m · Forbes-grens 0,1 m · Beira-kade 0,0 m · Yangtze-monding 2.687 m (anker ≠ routeerpunt, zelfde afstand als in de bronbrief — de brief-stippel b5 loopt van de MARNET-eindknoop naar de Yangtze-bulklaag, niet naar dit anker) · Zhangjiagang-kade 0,0 m.

**Toets (bakhandleiding §5):**
- `toets_knikken.py`: b1 24 knikken / 1 omkering (0 terugloop, "scherpe bocht, echt" bij de Mutare/Forbes-aansluiting — geen probleem); b2 3 knikken / 1 omkering (0 terugloop); zee 2 krappe bochten (geen omkering); binnenvaart 0 knikken. **0 TERUGLOOP overal** = geen reparatie nodig.
- `toets_rechte_benen.py --min-km 5`: alleen de twee gekopieerde zee-stippels (8,6 km) vallen op met omwegfactor 1,005 — identiek aan lithium-bikita-zhangjiagang en lithium-greenbushes-zhangjiagang, geen nieuwe bevinding.
- `json.load` slaagt: `versie: 2`, `punt_formaat: "lonlat"`, alle modaliteiten in {truck, zee, binnenvaart}, elk been ≥ 2 punten, bestand 160,5 KB.

**Bevinding b1 (km-toets, BUITEN de norm):** gemeten 281,3 km weggeometrie (283,1 km getekende lijn incl. anker-stukjes) tegen ≈241 km gepubliceerd = **+16,7%**, buiten zowel ±10% als de ±15%-norm die de brief zelf als *bindend* aanmerkt (§7: "de ±15%-toets geldt hier als bindende norm, niet als indicatie" — het gepubliceerde cijfer is zelf een berekening, geen directe bron). Niet gecorrigeerd door een via-punt te verplaatsen: elk segment afzonderlijk heeft een plausibele omwegfactor (1,1–1,4× hemelsbreed, typisch voor de Zimbabwaanse highveld-A3 door Marondera/Rusape/Nyazura/Mutare), geen enkel via-punt geeft een aanwijsbare 180°-omweg of ligt op een zijtak. Het Ruwa-via-punt (west van de Arcadia-mijn, terwijl de rit verder oostwaarts gaat) is zoals in de brief bedoeld: het pint de corridor naar de doorgaande A3 in plaats van terug Harare-centrum in, en draagt zelf geen extreme uitbuiging (24,2 km hemelsbreed vs 33,6 km gemeten, factor 1,39). Conclusie: de brief onderschat de echte wegkilometers van deze corridor.

**Bevinding b1 (anker→weg, net onder de last-mile-drempel):** Arcadia-plant → eerste WEG_HOUD-knoop = 1,82 km (< de 2 km-drempel voor een last-mile-stippel), dus doorgetrokken zonder stippel — geen fout, wel genoteerd omdat het aan de kant van de drempel zit.

**Geen luchtbeen, geen leidingbeen, geen spoorbeen in deze keten.** Fase D vervalt (brief §6): geen bron koppelt deze specifieke sulfaatlading aan een Chinese fabriek.

**Les:** een Forbes→Beira-subsegment knippen uit een bestaand geojson (op de vertex met de kleinste kwadratische afstand tot het ankerpunt) reproduceert de bronlengte tot op 0,7% (286,9 km tegen de brief-eigen 289 km) — dit is een herbruikbaar patroon voor een volgende keten die maar een deel van een bestaand been deelt in plaats van het hele been.

**Centraal hersteld (2026-09-28, integratie golf 6):** de van lithium-bikita-zhangjiagang geërfde naad van 7,8 km (Beira-kade → MARNET-zeeknoop) is gedicht met een haven-aanloop Beira. `maak_havenaanloop.py` liep vast (exit 124), dus volgens handleiding §2 een rechte stippel (7,8 km); het zeebeen start nu op de zeeknoop -19.8701,34.7882. 8 benen, 13.670 km.
