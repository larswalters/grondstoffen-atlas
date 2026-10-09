# Routebrief (licht) · PGM — Kevitsa → Via Ajos (Kemi) → Harjavalta (Finland)

**stroom-id:** `pgm-kevitsa-harjavalta` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** Ni-Cu-concentraat met Pt/Pd-bijproduct van Boliden's Kevitsa-mijn (Sodankylä, Lapland) gaat per **truck**
(76 t-combinaties, Vt4/E75 via Rovaniemi) naar de haven Ajos in Kemi, daar in een pakhuis, en van Ajos per **spoor** (Oulu – Kokkola –
Seinäjoki – Parkano – Tampere – Kokemäki) naar de Boliden-smelter in Harjavalta; stoppunt = de smelter.
**Welke as van het verhaal:** de enige PGM-productie van de EU, een Europees Ni-Cu-bijproduct. Peiljaar **2025**: 33.583 oz Pt + 29.627 oz Pd
in concentraat = 63,2 koz = **~1,97 t 2E/j** (Pt ~1,04 t + Pd ~0,92 t; geen Rh/Au; koz ÷ 32,15) [4]. Het concentraat zelf: ~300 kt Cu+Ni/j [2][3].
⚠️ Klein tegenover de Bushveld; en Kevitsa heeft een afbouwplan (§7) — "rijdt nu" geldt voor 2025.

## 1 · Ketenkaart
```
Kevitsa-concentrator `pgm-kevitsa-concentrator` ──(b1 truck · Vt4/E75 · ~306 km [VR: "lähes 300"])──► Ajos, Kemi `pgm-ajos-kade` (pakhuis)
──(b2 spoor · Oulu–Ylivieska–Kokkola–Seinäjoki–Parkano–Tampere–Kokemäki · hemelsbreed 498, gemeten ~704–714 km)──► Boliden Harjavalta `pgm-harjavalta-smelter` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-kevitsa-concentrator` → `pgm-ajos-kade` | mijnweg → Vt4/E75 (Sodankyläntie, Valtatie 4, Kemintie, Nelostie, Jäämerentie) → Kemi → Ajos | ~300 wegkm (VR Linked 2018) [1]; gemeten 306,5 (+2,2%) | maak_stroombeen_weg (profiel `pgm-kevitsa-harjavalta-kevitsa-ajos`) | nee |
| b2 | B/C | spoor | `pgm-ajos-kade` → `pgm-harjavalta-smelter` | Kemi–Oulu · Pohjanmaan rata (Oulu–Ylivieska–Kokkola–Seinäjoki) · Seinäjoki–Parkano–Tampere · Tampere–Pori-lijn naar Harjavalta | hemelsbreed 497,8 km, **geen spoorkm gepubliceerd**; router 704,4 / bake-geometrie 714,3 km (verhouding 1,41) | toets_spoorroute (4 runs, BAKE_SUFFIX=-raw) | nee |

Geen zeebeen: een deel van het concentraat is in het verleden per schip uit Ajos vertrokken [5] en Rönnskär wordt als tweede smelter genoemd [7], maar geen bron geeft voor 2025 een volume of schip — niet getekend (§7).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-kevitsa-concentrator` | mijn + concentrator (kop) | Boliden Kevitsa, Sodankylä | 67.6945, 26.9334 | [4][8] | bron-gelegd (z15: concentratorhallen met silo/koepel aan de zuidoostrand van de pit, tailingbekken ervoor; het Wikipedia-punt 67.6940,26.9280 lag 0,22 km westelijker op bijgebouwen — verschoven naar de hoofdhal). Geen spoor op het terrein, alleen wegen |
| `pgm-ajos-kade` | overslag truck → spoor | Port of Kemi, Ajos, kade/pakhuiszone | 65.6650, 24.5210 | [1][5] | bron-gelegd (z15: pier met pakhuizen, kranen en spoorlijnen die vanuit het noordoosten het terrein in lopen; zoekpunt 65.6635,24.5240 lag 0,22 km oostelijker bij de Metsä-hal). **Welk pakhuis het Baltic Bulk-pakhuis van 3.000 m² [5] is, is niet aan te wijzen** |
| `pgm-harjavalta-smelter` | losplek spoor / smelter (staart) | Boliden Harjavalta, Teollisuuskatu 1 | 61.3175, 22.1182 | [6] | bron-gelegd (z16: rangeerspoor met wagons langs de grote smelter-/opslaghallen midden in het complex). Sitelaag `w-harjavalta-boliden` (61.3200,22.1250, aannemelijk) ligt 0,46 km oostelijker aan de rand — verschoven naar het spoor. Nornickel's raffinaderij ligt in hetzelfde complex; de perceelgrens is niet gezien |

## 4 · Via-punten (alleen waar een corridorkeuze of sluipweg bestaat; allemaal op de doorgaande weg/lijn)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Rovaniemi — Vt4 noord van het centrum | 66.5425, 25.8179 | pint Vt4/E75 (Sodankyläntie) in plaats van een zijweg door het Rovaniemi-gebied; OSM-vertex, snap 0,00 km |
| b1 | 2 | Tervola — Nelostie | 66.0869, 24.7729 | houdt de route op Vt4/E75 Rovaniemi–Kemi; OSM-vertex, snap 0,00 km |
| b2 | 1 | Ylivieska — op de Pohjanmaan rata | 64.0405, 24.4824 | pint Oulu → Ylivieska → Kokkola (hoofdlijn) tegen een oostelijke sluipweg |
| b2 | 2 | Seinäjoki — noord van het station | 62.7745, 22.8873 | splitst de lange Kokkola–Seinäjoki-run; spoorknoop op de doorgaande lijn |
| b2 | 3 | Parkano — op de Seinäjoki–Tampere-lijn | 61.9857, 23.1425 | de corridorkeuze zelf: Seinäjoki–Tampere via Parkano (88,7 km, verhouding 1,00) en niet via Haapamäki |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kevitsa | Boliden | erts (10,2 Mt gemalen 2025) → Ni-Cu-concentraat met 33.583 oz Pt + 29.627 oz Pd | ontwerpcapaciteit 9,9 Mtpa; ~300 kt concentraat/j | [4][2] |
| Ajos (Port of Kemi) | Kemin Satama / Baltic Bulk | concentraat per truck → pakhuis 3.000 m² → trein (2×/week in 2018) | niet gepubliceerd; 12–13 trucks/dag in 2021 (20–24 ladingen/dag in 2018) | [1][3][5] |
| Harjavalta | Boliden | Ni-Cu-concentraat → koper, nikkelmatte, Au, Ag, zwavelzuur | 2025: 162 kt Cu, 34 kt Ni, 8 t Au, 65 t Ag; enige nikkelsmelter van West-Europa | [6] |

## 6 · Stoppunt
De brief stopt bij de Harjavalta-smelter: Boliden noemt Kevitsa als toeleverancier [6][7], maar geen bron zegt waar het Pt/Pd na de smelter heen gaat (de koperraffinaderij in Pori is genoemd [6], geen PGM-afnemer) — geen fase D getekend.

## 7 · Open punten
- **Spoorlengte onbekend:** VR noemt geen spoorkm; 704–714 km is gemeten op OSM, geen toets tegen een bron (de ±15%-norm geldt hier niet).
- **Twee omkeringen uit de OSM-topologie, zo gelaten:** Kemi (65.7318,24.5802: Ajos-aftakking) en Tampere (61.4951,23.7740: Seinäjoki-lijn en Pori-lijn hebben bij Lielahti geen directe schakel, de route rijdt station Tampere in en terug). Echte kopmaak of OSM-gat — niet uitgezocht.
- **Verdeling spoor/schip niet gedocumenteerd:** [1] noemt 2×/week trein, [5] een eerste rikastelaivaus uit Ajos in 2013, [7] noemt ook Rönnskär. Geen volume per route; Ajos → Rönnskär (hergebruik `ag-ronnskar-kade` 64.6704,21.2699, zilver-garpenberg-ronnskar) is mogelijk, niet getekend.
- **Rovaniemi:** een Vt4/E75 die buiten het centrum langs loopt is niet gevonden; de weg loopt in OSM ~0,3 km van het centrum. Geen ringweg-alternatief onderzocht.
- **Ajos-pakhuis** (welk gebouw, welk havenspoor) en de **Boliden/Nornickel-perceelgrens** in Harjavalta niet aangewezen.
- **Kevitsa-sluiting:** het sluitingsdreigement uit de Finse pers (Kauppalehti) is hier niet zelf gelezen; Boliden's eigen rapport noemt een sluitingsplan (update vóór sept. 2027) en een herziening met een mogelijke Stage 5 [4]. Peiljaar 2025.
- **Pt/Pd-fractie per trein** niet gedocumenteerd; Kevitsa en Harjavalta staan niet in de pgm-sitelaag (centraal toevoegen als site: Kevitsa 67.6945,26.9334 · Harjavalta 61.3175,22.1182).

## 8 · Bronnen
[1] VR Logistiikka/Linked, 2018, "Kellontarkkaa rikasteliikennettä Kevitsasta Kemiin" — ~300 km, 20–24 ladingen/dag, pakhuis in Kemi, trein 2×/week. https://logistics.vr.fi/fi/vr-logistiikka/linked/artikkeli/kellontarkkaa-rikasteliikennetta-kevitsasta-kemiin-120420181226/
[2] Yle, 26-4-2021 — ~300.000 t concentraat/j, ~25–30 transporten per werkdag, Ajos → trein → Harjavalta. https://yle.fi/a/3-11901777
[3] VR Group, 26-4-2021, "VR Transpointin ja Bolidenin yhteistyö laajenee" — Sodankylä → Harjavalta, 12–13 trucks/dag, 76 t. https://www.vrgroup.fi/fi/vrgroup/uutiset/kevitsan-kaivoskuljetusten-tehostamiseksi-loydettiin-uusia-innovaatioita-vr-transpointin-ja-bolidenin-yhteistyo-laajenee-260420210744/
[4] Boliden, Summary Report Kevitsa — Mineral Resources and Reserves 31-12-2025 (Pt/Pd in concentraat 2025, 10.155 kt gemalen, sluitingsplan). https://www.boliden.com/4900d3/globalassets/operations/exploration/mineral-resources-and-mineral-reserves-pdf/2025/mineral-resources-and-mineral-reserves-kevitsa-2025-12-31.pdf
[5] Kemin Satama, Vuosikertomus 2012 — Baltic Bulk-pakhuis 3.000 m² op Ajos, eerste Kevitsa-concentraat dec. 2012, eerste verscheping jan. 2013. https://www.portofkemi.fi/wp-content/uploads/2018/07/kemin-satama-vuosikertomus-2012.pdf
[6] Boliden, "Boliden Harjavalta" — adres, productie 2025, Kevitsa als toeleverancier, Pori-raffinaderij. https://www.boliden.com/operations/smelters/boliden-harjavalta
[7] E&MJ, overname Kevitsa door Boliden (via zoeksnippet; niet zelf gelezen, 403) — concentraat naar Harjavalta en Rönnskär. https://www.e-mj.com/leading-developments/boliden-acquiring-first-quantum-s-kevitsa-mine-in-northern-finland/
[8] Wikipedia (MediaWiki-API), "Kevitsa mine" — 67.693992, 26.928048 (zoekpunt, niet het anker). https://en.wikipedia.org/wiki/Kevitsa_mine
[9] OpenStreetMap via Overpass (maps.mail.ru-spiegel; ODbL) — Vt4/E75-vertices voor de via-punten, wegnet voor b1. https://www.openstreetmap.org
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15/z16) — `pgm-kevitsa-harjavalta-kevitsa|ajos|harjavalta|harjavalta16` in `v2/build-cache/satcheck/`.
[11] Eigen metingen: `toets_spoorroute.mjs` (vier runs, 1-op-1-spoornet), `maak_stroombeen_weg.py` (306,5 km, +2,2%), `hecht_marnet.py` (naden 0,00–0,07 km).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
Bestand `v2/data/stroomroute-pgm-kevitsa-harjavalta.json` (106,8 KB, contract versie 2, `lonlat`), functie `bak_pgm_kevitsa_harjavalta` in
`v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh pgm-kevitsa-harjavalta`), profiel `pgm-kevitsa-harjavalta-kevitsa-ajos` in
`v2/tools/maak_stroombeen_weg.py`. Totaal **1.020,9 km · 5.640 punten · 3 markers**. Geen zee, stippel, haven-aanloop, lucht of leiding.

| # | modaliteit | km | punten | naad naar vorig been | toets |
|---|---|---|---|---|---|
| b1 | truck (Vt4/E75) | 306,6 | 3.915 | — | ~300 wegkm (VR Linked 2018): +2,2% |
| b2a | spoor Ajos → Ylivieska | 240,4 | 553 | 0,05 km | geen spoorkm gepubliceerd: indicatie |
| b2b | spoor Ylivieska → Seinäjoki | 210,1 | 493 | 0,00 km | idem |
| b2c | spoor Seinäjoki → Parkano | 89,6 | 119 | 0,00 km | idem |
| b2d | spoor Parkano → Harjavalta | 174,2 | 560 | 0,00 km | idem |

b2 samen 714,3 km (hemelsbreed 497,8; verhouding 1,43 incl. de omkeringen) tegen 704,4 km in de vrije run: een indicatie, geen ±15%-norm.
Markers (3): `pgm-kevitsa-concentrator` 0,00 km van de lijn · `pgm-ajos-kade` 0,00 km · `pgm-harjavalta-smelter` 0,05 km. Alle naden <= 0,05 km.

**Recept.** b1: wegprofiel (extract finland) gebakken via de maps.mail.ru Overpass-spiegel (pyosmium geblokkeerd, standaardspiegels 5xx;
een herbake zonder die wrapper faalt). b2: vier runs `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs` (Ajos-Ylivieska-Seinäjoki-Parkano-Harjavalta),
`hecht_marnet.py` neemt de vier geojson als vooraf gebakken lijn. Bake via het zwaar-slot, ongewijzigd uit de brief-fase.

**Toelichting per bijzonder been.** Geen stippel, aanloop, vlucht of leiding: Ajos-kade en Harjavalta snappen op 0,05 km van het spoor. Het
spoor is doorgetrokken (gemeten net); de verdeling spoor/schip (Rönnskär) is niet getekend omdat geen bron een volume noemt.

**Knikken en rechte benen.** `toets_knikken.py`: truck 8 knikken (1 omkering van 168,9 graden bij 65.71555,24.61349 in Kemi: een korte haarspeld
van ~0,1 km op een aansluiting, geen terugloop; de rest zijn spikes op mijnwegen bij Kevitsa en op aansluitingen); b2a 1 omkering bij Kemi
(65.73180,24.58020, Ajos-aftakking, geen terugloop); b2d 1 **TERUGLOOP** bij Tampere (61.49510,23.77400): de route rijdt ~0,8 km het station in en
dezelfde weg terug (~1,6 km totaal), omdat de Pohjanmaan-/Seinäjoki-lijn en de Pori-lijn bij Lielahti in OSM geen directe schakel hebben. **Bewust
gelaten** (OSM-topologie, geen via-punt bijgeschoven): ~0,2% van de 714 km. `toets_rechte_benen.py --min-km 5`: geen been van deze stroom.

**Lessen.**
1. Het gebruik van `rm -rf "$d"` in de slot-helper wordt door de veiligheidscheck geweigerd; slot nemen kan met `mkdir` op een letterlijk pad en
   vrijgeven met `rmdir` op een letterlijk pad (geen stale-opruiming: laat dat aan de andere agenten).
2. De brief-agent had alle benen en de functie al gebakken; deze fase was bake, toets en vastleggen. Tussenuitvoer in `v2/build-cache/ais/graaf/`
   (gitignored) blijft staan; wegbenen zijn alleen via de maps.mail.ru-spiegel te herbakken (centraal melden).
