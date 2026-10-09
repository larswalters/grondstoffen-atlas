# Routebrief (licht) · nikkel — Monchegorsk (Severonickel) → Harjavalta (Finland)

**stroom-id:** `nikkel-monchegorsk-harjavalta` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** nikkelmatte/tussenproduct in containers van Severonickel (Kola MMC / Nornickel, Monchegorsk) per **spoor** over de Oktoberspoorweg (Murmansk-lijn: Olenegorsk – Kandalaksha – Petrozavodsk – Volkhov – Mga – Vyborg) naar de Finse grens bij **Vainikkala**, dan over het Finse net (Kouvola – Lahti – Riihimäki – Tampere – Pori-lijn) naar de Nornickel-raffinaderij in Harjavalta (nikkelkathode/-zouten/sulfaat). **Aannemelijk: gedocumenteerd patroon, niet actuele lading.**
**Welke as van het verhaal:** het sanctie-gat — de enige Russische class-1-keten die Europa in loopt, over rail. Bovengrens ≈ **61 kt Ni/j** = ~94% Russische feed (Nornickel-jaarverslag 2021, via Global Witness [1]) × 65 kt Ni/j capaciteit Harjavalta [5] (capaciteit, geen productie of meting; eigen-lading Boliden niet te scheiden). Spoorindicatie: gem. 290 containers/maand over de Finse grens, apr 2024–jan 2025 (alle lading, niet alleen matte) [1] ≈ 3.480/j (eigen optelling).

## 1 · Ketenkaart
```
Severonickel `ni-monchegorsk-severonickel` ──(b1 spoor · Monchegorsk→Olenegorsk→Kandalaksha→Petrozavodsk-lijn · 949,9 km, kopmaak Olenegorsk)──► via 1 Petrozavodsk-lijn
   ──(b2 spoor · Svir/Volkhov-richting · 274,9 km)──► via 2 Volkhov-knoop ──(b3 spoor · Mga → SPb-omleiding → Vyborg · 276,5 km)──► Vainikkala-grensknoop (60.8596,28.3208)
   ──(b4 spoor · Finse net Kouvola–Lahti–Riihimäki–Tampere–Pori · 425,7 km)──► Harjavalta-raffinaderij `ni-harjavalta-raffinaderij` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | spoor | Severonickel → via 1 Petrozavodsk-lijn | Oktoberspoorweg Monchegorsk–Olenegorsk–Apatity–Kandalaksha–Belomorsk–Segezha–Petrozavodsk | eigen Dijkstra 949,9; geen gepubliceerde spoor-km (hemelsbreed 687 km) | `toets_spoorroute` (rusland-noordwest), `-raw`, `--hoofd-km=50 --max-snap=10` | nee |
| b2 | C | spoor | via 1 → via 2 Volkhov-knoop | Murmansk-lijn Petrozavodsk–Svir–Volkhov | eigen Dijkstra 274,9; geen gepubliceerde km | idem | nee |
| b3 | C | spoor | via 2 → Vainikkala-grensknoop | Volkhov–Mga–Sint-Petersburg-omleiding (6,7 km van centrum)–Vyborg–Buslovskaya | eigen Dijkstra 276,5; geen gepubliceerde km | idem (rusland-noordwest) | nee |
| b4 | C | spoor | grensknoop → Harjavalta | Vainikkala–Luumäki–Kouvola–Lahti–Riihimäki–Tampere–Pori-lijn, Kokemäki | eigen Dijkstra 425,7; geen gepubliceerde km | `toets_spoorroute` (finland) | nee |
Totaal **1.927,0 km**, hemelsbreed Monchegorsk–Harjavalta **891 km, geen spoorkm** — de ±15%-toets is alleen een indicatie. Sanity: Kirov Railway SPb–Murmansk is 1.448 km [7], Monchegorsk ligt 145 km ten zuiden van Murmansk [8]; onze Monchegorsk–Volkhov (1.224,8 km) valt daar logisch in. Geen stippel nodig: de 1-op-1-netten snappen op 0,23 km (Severonickel) en 0,19 km (Harjavalta); geen b4b-terreinstippel (de ontwerp-b4b bestaat niet, zie §7).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-monchegorsk-severonickel` | laad-/startpunt raffinaderij | Severonickel-fabriek (Kola MMC), Monchegorsk | 67.9195, 32.8320 | [12] (hergebruikt letterlijk uit `nikkel-norilsk-monchegorsk`), [8] | bron-gelegd (z15 zelf gezien: tankpark en spoorbundel aan de noordkant van het smelter-/raffinaderijcomplex, hallen en schoorstenen direct zuidelijk) |
| `ni-harjavalta-raffinaderij` | losplek/raffinaderij | Norilsk Nickel Harjavalta Oy, Teollisuuskatu 1 | 61.3188, 22.1225 | [5][6][12] | bron-gelegd (z15 zelf gezien: kruis op het hallen- en ketelblok van het fabriekscomplex, tankpark noord, goederenspoor/emplacement zuidwest) |
Het sitelaag-punt `w-harjavalta-nornickel` (61.3220, 22.1280) ligt 461 m ONO van dit anker in een parkeerplaats/bosrand aan de woonwijk — centraal gelijktrekken met `ni-harjavalta-raffinaderij`.

## 4 · Via-punten (alleen b1–b3; geen corridorkeuze in Finland)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1/b2 | 1 | Petrozavodsk-lijn (station op de hoofdlijn, snap 0,30 km) | 61.7723, 34.3751 | een vrije Dijkstra kiest de verkeerde grens (Vartius/Kajaani, 1.589 km); dwingt de Murmansk-lijn af |
| b2/b3 | 2 | Volkhov-knoop (hoofdlijn-junctie, snap 0,00 km) | 59.9217, 32.3074 | houdt de route op de Oktoberspoorweg i.p.v. de Sortavala-sluipweg (direct Petrozavodsk→grens 488,4 km, 63 km korter dan via Volkhov) |
| b3/b4 | 3 | Vainikkala-grensknoop (gedeelde node in finland- en rusland-noordwest-net, snap 0,00 km) | 60.8596, 28.3208 | grensovergang; Wikipedia zet het dorp op 60.8661, 28.2997 (1,4 km verderop) [4] |
Nooit via-punten bij Sint-Petersburg: de route loopt al over de omleiding. Het ontwerp had via 2 op 59.9184, 32.3485 (Volkhov-station); die laat run b2 2,3 km voorbij de junctie en terug rijden (OMKERING 180°, boogstraal 18 m) — vervangen door de junctie zelf (bevinding, zie afwijking).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Severonickel, Monchegorsk | Nornickel (Kola MMC) | converter-matte (Norilsk via Murmansk) → matte/tussenproduct in containers | 145 kt Ni/j raffinage (zie nikkel-norilsk-monchegorsk) | [12] |
| Harjavalta | Norilsk Nickel Harjavalta Oy | matte/tussenproduct (~94% Russisch, 2021) → nikkelkathode, -zouten/-sulfaat, kobaltsulfaat | 65 kt Ni/j nu, 75 kt gepland 2023, >100 kt begin 2026 (aankondiging 2021, niet bevestigd als voltooid) | [1][5] |

## 6 · Stoppunt
Harjavalta: geen bron noemt een afnemer per lading (fase D/E vervalt); eindproduct = nikkelkathode/-sulfaat voor de Europese markt.

## 7 · Open punten
- **Inferentie:** Global Witness beschrijft Murmansk→Monchegorsk en, apart, containers over Vainikkala naar Harjavalta, en koppelt ze niet expliciet [1]; Nornickel AR2020 (Harjavalta verwerkt Russische feed van Kola MMC) en Yle (Vainikkala-treinen, Nort Rail) ondersteunen dat [2][3]. Label: aannemelijk, gedocumenteerd patroon.
- Sanctierisico: US/VK verboden Russische oorsprong (apr 2024); EU niet [3]; het 20e EU-pakket tegen Russische metalen kon niet gelezen worden [9]. Lees als infrastructuur, niet als actuele lading.
- De 290 containers/maand zijn alle lading; het matte-aandeel is niet gepubliceerd [1]. Boliden-materiaal (andere herkomst) niet te scheiden.
- Geen gepubliceerde spoorkilometers voor deze relatie; de ±15%-toets is indicatief.
- Echte kopmaak bij Olenegorsk (68.1397, 33.2323; tak naar Monchegorsk takt aan op de Murmansk-lijn): `toets_knikken` meldt hem; geen fout.
- Ontwerp-b4b (terreinspoor Severonickel als kopie van norilsk-monchegorsk b4b) bestaat niet: die stroom heeft b4b bewust niet gebakken (snap 0,23 km).
- ~50 km Monchegorsk–Olenegorsk loopt gelijk met `nikkel-norilsk-monchegorsk` b4 (omgekeerd): natuurlijke gedeelde infrastructuur, geen kopie.
- Vainikkala-coördinaat 60.86, 28.62 in `nikkel-norilsk-monchegorsk` ligt ~15 km in Rusland; die brief niet meenemen.

## 8 · Bronnen
[1] Global Witness, "Sanctions gap lets Russian-mined nickel flow to Western markets" (2025): 290 containers/maand over de grens, 94% Russische feed, Vainikkala, 65 kt. https://globalwitness.org/en/campaigns/transition-minerals/sanctions-gap-lets-russian-mined-nickel-flow-to-western-markets/
[2] Nornickel AR2020, Kola-Finland (via de haalbaarheidstoets; zelf niet kunnen openen, ECONNRESET). https://ar2020.nornickel.ru/en/business-overview/operational-performance/kola-finland.html
[3] Yle, 26-08-2024: dagelijkse Russische grondstoftreinen bij Vainikkala, Nort Rail, EU/Finland sanctioneren nikkel niet. https://yle.fi/a/74-20106170
[4] Wikipedia, Vainikkala (60.8661, 28.2997). https://en.wikipedia.org/wiki/Vainikkala
[5] NS Energy, Nornickel Harjavalta expansion (2021): 65 → 75 → >100 ktpa, producten. https://www.nsenergybusiness.com/company-news/nornickel-harjavalta-nickel-refinery-expansion/
[6] IndustryAbout, Nornickel Harjavalta (adres Teollisuuskatu 1; site was deze sessie onbereikbaar, overgenomen uit [12][10]). https://www.industryabout.com/country-territories-3/2745-finland/nickel-mining/42868-nornickel-harjavalta-nickel-refinery
[7] Wikipedia, Kirov Railway (SPb–Murmansk 1.448 km). https://en.wikipedia.org/wiki/Kirov_Railway
[8] Wikipedia, Monchegorsk (145 km ten zuiden van Murmansk). https://en.wikipedia.org/wiki/Monchegorsk
[9] Eurometal, 20th sanctions package (kop; inhoud niet gelezen). https://eurometal.net/20th-sanctions-package-to-close-eu-market-to-more-russian-metals/
[10] Esri World Imagery via `sat_check.py` z15: `v2/build-cache/satcheck/sat-nikkel-monchegorsk-harjavalta-*.png` (harjavalta-raffinaderij, harjavalta-sitelaag, monchegorsk-severonickel).
[11] Eigen spoorruns `toets_spoorroute` (BAKE_SUFFIX=-raw, "3260717 spoor-edges", 2026-10-09) en de haalbaarheidstoets van de keten.
[12] `v2/design/routebrieven/nikkel-norilsk-monchegorsk.md` (anker Severonickel, Harjavalta-adres) en `nikkel-sitelaag.json` (B20/B21).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Resultaat:** `v2/data/stroomroute-nikkel-monchegorsk-harjavalta.json` (versie 2, lonlat, 102,9 KB) · 4 benen · **1.948,3 km** · 5.837 punten · 3 markers · 0 stippel · naden 0,000 km.
Recept: functie `bak_nikkel_monchegorsk_harjavalta` in `v2/tools/bak_stromen.sh`; draaien met `bash v2/tools/bak_stromen.sh nikkel-monchegorsk-harjavalta`. Titel: *Nikkel · Monchegorsk (Severonickel) → Vainikkala → Harjavalta (matte per spoor, aannemelijk)*.

| # | modaliteit | been | km gebakken | km router (brief) | tussenuitvoer (`v2/build-cache/ais/graaf/`) |
|---|---|---|---|---|---|
| b1 | spoor | Severonickel → Petrozavodsk-lijn (3.147 pt) | 956,6 | 949,9 (+0,7%) | `spoorroute-nikkel-monchegorsk-harjavalta-b1-monchegorsk-petrozavodsk.geojson` |
| b2 | spoor | Petrozavodsk-lijn → Volkhov-knoop (692 pt) | 277,4 | 274,9 (+0,9%) | `…-b2-petrozavodsk-volkhov.geojson` |
| b3 | spoor | Volkhov-knoop → Vainikkala-grensknoop (560 pt) | 281,8 | 276,5 (+1,9%) | `…-b3-volkhov-vainikkala.geojson` |
| b4 | spoor | Vainikkala → Harjavalta-raffinaderij (1.438 pt) | 432,5 | 425,7 (+1,6%) | `…-b4-vainikkala-harjavalta.geojson` |

Alle vier runs: `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=… --naar=… --naam=nikkel-monchegorsk-harjavalta-<deel> --hoofd-km=50 --max-snap=10`, eerste consoleregel `3260717 spoor-edges`. Snaps 0,23 / 0,30 · 0,30 / 0,00 · 0,00 / 0,00 · 0,00 / 0,19 km; 768 · 233 · 436 · 979 edges; verhoudingen 1,38 · 1,17 · 1,14 · 1,26.
**Markers (3):** Severonickel 67.9195, 32.8320 (0,23 km van de lijn = de net-snap) · Vainikkala-grensknoop 60.8596, 28.3208 (0,00 km, naad b3/b4, extra tussenmarker 'grensovergang') · Harjavalta-raffinaderij 61.3188, 22.1225 (0,19 km). Geen haven-aanloop, geen stippel, geen luchtbeen, geen leiding, geen wegbeen: een keten van vier spoorruns.

**Toets (handleiding §5):**
- km per been tegen de eigen routerkilometers van §2: +0,7% tot +1,9% (de bake meet de lijn zelf, de router telt edge-lengtes); er is **geen gepubliceerde spoor-km** voor deze relatie, dus de ±15%-toets is alleen indicatief. Sanity: SPb–Murmansk 1.448 km (Kirov Railway), Monchegorsk–Volkhov in de bake 1.234,0 km (956,6 + 277,4) past daarbinnen.
- naden tussen opeenvolgende benen **0,000 km** (alle eindpunten delen exact één netknoop); markers ≤ 0,23 km van hun lijn.
- `toets_knikken.py`: 1 knik, op Olenegorsk 68.13970, 33.23230 (180,0°, boogstraal 0 m) — de verwachte **kopmaak** uit §7. Let op: `toets_knikken` rubriceert hem als **TERUGLOOP** (pad ÷ hemelsbreed 99), de klasse die 'gerepareerd hoort te worden'; dat is hier een echte keerlus (volgens het 1-op-1-net takt de tak van Monchegorsk bij Olenegorsk op de Murmansk-lijn aan zonder doorgaande verbinding naar het zuiden, dus de route keert in Olenegorsk om; zo ook in §7 benoemd), geen netfout. Geen andere knik of omkering in b2–b4.
- `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de lijst (geen stippel, geen omwegfactor 1,000).
- `json.load` slaagt: versie 2, punt_formaat lonlat, 4 benen modaliteit `spoor`, elk ≥ 2 punten, 102,9 KB.

**Lessen / bevindingen:**
- De brief-aanwijzingen klopten letterlijk (km, snaps, edges, omkering); er zijn geen via-punten verschoven of bijgesteld.
- `hecht_marnet route` begint de lijn op de netsnap (67.9190, 32.8373), niet op het anker (0,23 km): het terrein-eindstuk Severonickel (b4b van norilsk-monchegorsk) bestaat bewust niet, ook hier niet gebakken.
- De ~50 km Monchegorsk–Olenegorsk loopt gelijk met `nikkel-norilsk-monchegorsk` b4 (omgekeerd): natuurlijke gedeelde infrastructuur, geen kopie.
- Claim blijft 'aannemelijk: gedocumenteerd patroon, EU-sanctierisico': volume (290 containers/maand, alle lading) is een bovengrens, het matte-aandeel en Boliden-materiaal zijn niet te scheiden.
- Centraal nog te doen: registratie (zie het eindrapport), bundel, `?v=`/`BUNDEL_VERSIE`, en sitelaag-punt `w-harjavalta-nornickel` (61.3220, 22.1280) gelijktrekken met anker 61.3188, 22.1225 (461 m ernaast).
