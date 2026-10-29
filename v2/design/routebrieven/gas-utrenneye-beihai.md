# Gas · Utrenneye (Rusland) → Beihai (China)

**stroom-id:** `gas-utrenneye-beihai` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** gesanctioneerd Arctisch LNG van Arctic LNG 2 (Novatek) op Utrenneye, Gydan-schiereiland, per ijsklasse-tanker naar de PipeChina-terminal Beihai bij Tieshan Port in Guangxi; getekend is de westelijke winter-/FSU-route via de Noorse kust, Suez en Malakka, niet de zomerroute oostwaarts langs de Noordelijke Zeeroute.
**Welke as van het verhaal:** Russisch sanctie-LNG naar China, 41 ladingen / 2,6 Mt in minder dan tien maanden (aug 2025–jun 2026, Kpler via Reuters) [1] = ≈ 3,5 bcm over die periode, ≈ 4 bcm/j geannualiseerd (eigen rekensom, 1 Mt ≈ 1,36 bcm) — circa een zesde van de nameplate 19,8 Mtpa. Beihai is de enige ontvanger van het project [6]; een tweede PipeChina-terminal (Longkou, Shandong, 5 Mt/j) staat in aanbouw [1].

## 1 · Ketenkaart
```
Arctic LNG 2, Utrenneye (Gydan) `gas-utrenneye-lng`
  ──(b1a zee · haven-aanloop, ijs · 18,7 km over water, stippel)──► MARNET-zeeknoop 4712 (70.9064, 73.5021)
  ──(b1 zee · Barentszzee → Noorse kust → Gibraltar → Suez → Bab el-Mandeb → Malakka → Zuid-Chinese Zee
       · 22.667,5 km MARNET; aannemelijk: één bron)──► MARNET-zeeknoop 5543 (21.4173, 109.6930)
  ──(b1b zee · haven-aanloop Tieshan · 18,0 km over water, stippel)──► Beihai LNG-terminal `gas-beihai-lng` ⏹ stoppunt
```
Fase A (Salmanovskoye-veld → fabriek) en C (Beihai → PipeChina-net) vervallen — zie §7.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1a | B | zee | `gas-utrenneye-lng` → zeeknoop 4712 | haven-aanloop Ob-baai (ijs) | 18,7 over water (15,4 hemelsbreed) [MARNET-meting + `maak_havenaanloop.py`] | `--stippel-geojson`, `gas-utrenneye-beihai-aanloop-utrenneye-plant.geojson` | ja: hier reikt het net niet |
| b1 | B | zee | zeeknoop 4712 → zeeknoop 5543 | westelijke route via Suez (MARNET kent geen NSR; zomerlading gaat oostwaarts) | 22.667,5 [MARNET-test, eigen]; geen gepubliceerde lengte; grootcirkel 5.972 | MARNET (knoop → knoop) | nee |
| b1b | B | zee | zeeknoop 5543 → `gas-beihai-lng` | haven-aanloop Tieshan Port | 18,0 over water (17,1 hemelsbreed) [idem] | `--stippel-geojson`, `gas-utrenneye-beihai-aanloop-beihai.geojson` | ja: hier reikt het net niet |

De route-check bevestigt Gibraltar (4 km van de lijn), Suez (2 km), Bab el-Mandeb (10 km), Malakka (16 km) en Noordkaap (6 km); géén Kanaal. Totaal 22.704,2 km. De route volgt de Suez-lading (Buran, jan 2026 [6]), geen directe lading Utrenneye → Beihai: de meeste lading loopt via transshipment (§7).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-utrenneye-lng` | productie + laadplek (LNG-complex) | Arctic LNG 2 / Utrenny LNG Terminal, Utrenneye, Gydan | 70.9952, 73.8295 | [5] GEM (70.99517, 73.8295); [10] OSM-relatie Арктик СПГ-2 (middelpunt 70.9963, 73.8319) | aannemelijk (z14/z16 gezien: opgespoten kadeterrein met havenbassin op het SW-hoekpunt van het OSM-industrievlak; het Esri-beeld is van vóór de GBS-platforms, dus geen trains of laadarmen zichtbaar) |
| `gas-beihai-lng` | losplek + regasterminal | Beihai LNG-terminal (PipeChina), Tieshan Port | 21.4490, 109.5317 | [4] GEM (21.448966, 109.531699) | bron-gelegd (z15 gezien: tankpark met zes ronde tanks op een aangelegd schiereiland, L-vormige steiger langs de zuidkant en een steiger aan de oostkant) |
Afwijking van het ontwerp: de pier 71.0093, 73.7895 (OSM-node Arktik SPG-2) blijkt op z16 een bevrachtings-/bouwkade met kranen en kleine schepen, 3,4 km noordwestelijk van het complex, zonder LNG-laadarmen; de lange smalle steiger ernaast (≈ 1,2 km, 71.0105 → 71.0000 bij 73.778) heeft op de kop geen installaties. Dat anker is dus niet gebruikt; het complexpunt uit [5]/[10] wel (zelfde zeeknoop 4712: 15,4 km tegen 15,5 km). Niet mengen: GEM-fase III Beihai (21.4506, 109.5254; Guangxi Gas Group) en het PetroChina-Beihai-punt 21.4995, 109.5242.

## 4 · Via-punten
Niet van toepassing: b1 is MARNET-routing (geen corridorkeuze door ons); b1a en b1b zijn haven-aanlopen. Fase A en C zijn niet getekend.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Arctic LNG 2 | Novatek 60 % · CNPC 10 % · CNOOC 10 % · TotalEnergies 10 % · JOGMEC 7,5 % · Mitsui 2,5 % | gas (Salmanovskoye) → LNG | 3 trains, nameplate 19,8 Mtpa ≈ 26,9 bcm/j; T1 stilgelegd, T2 in bedrijf, T3 in aanbouw/uitgesteld [5][1] | [3][5] |
| Beihai LNG-terminal | National Pipe Network Group Beihai LNG (PipeChina 80 % · Guangxi Beibu Gulf Port Group 20 %) | LNG → regasgas | fase I+II 6 Mtpa ≈ 8,2 bcm/j in bedrijf; fase III 6 Mtpa in aanbouw | [4][1] |

## 6 · Stoppunt
De brief stopt aan de kade van Beihai: geen bron koppelt de hervergaste stroom aan één punt in het PipeChina-net, en geen bron noemt één afnemer; fase C, D en E vervallen.

## 7 · Open punten
- **Noordelijke Zeeroute niet getekend.** MARNET kent hem niet; de zomerlading (Christophe de Margerie, Voskhod, 2025) gaat oostwaarts [7] en is veel korter. De getekende lijn is de winterroute (Buran via Suez [6]); niet gemeten wat de NSR-lengte is.
- **Transshipment Murmansk (Saam FSU) en Koryak (Kamtsjatka) niet getekend:** de Arctic Vostok laadde in Kamtsjatka, de Arctic Metagaz in Murmansk [2]; de leveringen begonnen vanuit Kamtsjatka [1]. Een directe lijn Utrenneye → Beihai slaat dat over.
- **LNG-laadplek niet gezien:** het Esri-beeld toont geen GBS-platforms; tankers laden aan een van de twee productie-eenheden [8]. Het anker is dus het complexpunt, geen kade.
- **Tellingen verschillen per aanbieder:** 23 ladingen / 1,3 Mt in 2025 (LSEG) [6] tegen 41 / 2,6 Mt aug 2025–jun 2026 (Kpler) [1]; een Reuters-samenvatting in een zoekresultaat noemt 26 (tot 13 juli 2026) resp. 31 ladingen in 2026 — niet zelf geopend, niet gebruikt.
- **Haven-aanlopen schematisch:** kortste pad over water op de 1:10M-kust (omwegfactor 1,21 en 1,06), niet de vaargeul; b1a in werkelijkheid ijs.
- **Fase A vervallen:** geen coördinaat van de Salmanovskoye-putlocaties gevonden. **Fase C vervallen:** geen gebrond invoedingspunt.

## 8 · Bronnen
[1] Reuters via The Moscow Times, 22-6-2026 — 41 ladingen / 2,6 Mt in minder dan tien maanden; Beihai 6 Mt/j, Longkou 5 Mt/j; leveringen vanuit Kamtsjatka; twee trains klaar. https://www.themoscowtimes.com/2026/06/22/china-prepares-second-lng-terminal-to-receive-cargoes-from-sanctioned-russian-arctic-lng-2-project-reuters-a93070
[2] gCaptain, 30-9-2025 — Arctic Vostok (Kamtsjatka) legt aan in Beihai; Arctic Metagaz (Murmansk); La Perouse via Europa/Afrika; Christophe de Margerie en Voskhod via de NSR. https://gcaptain.com/tanker-carrying-7th-sanctioned-arctic-lng-2-cargo-berths-at-china-port/
[3] Wikipedia, "Arctic LNG 2" — 3 trains, 19,8 Mtpa, GBS, sancties, transshipment Murmansk/Kamtsjatka. https://en.wikipedia.org/wiki/Arctic_LNG_2
[4] Global Energy Monitor, "Beihai LNG Terminal (PipeChina)" — 21.448966, 109.531699; eigenaren; fase I–III. https://www.gem.wiki/Beihai_LNG_Terminal_(PipeChina)
[5] Global Energy Monitor, "Arctic LNG 2 Terminal" — 70.99517, 73.8295; 3 × 6,6 Mtpa; eigenaren; train-status. https://www.gem.wiki/Arctic_LNG_2_Terminal
[6] Reuters via Baird Maritime, 26-1-2026 — 23 ladingen / 1,3 Mt in 2025 (LSEG); Buran via Suez; Beihai enige importeur. https://www.bairdmaritime.com/shipping/tankers/gas/china-receives-first-gas-in-2026-from-russias-arctic-lng-2-project
[7] Reuters via PGJ Online, 29-9-2025 — Christophe de Margerie en Voskhod laden bij Arctic LNG 2 en varen oostwaarts via de NSR. https://pgjonline.com/news/2025/september/arctic-lng-2-tankers-ship-sanctioned-russian-cargoes-to-asia-via-northern-sea-route
[8] The Barents Observer, 12-8-2025 — tanker laadt bij een van de twee productie-eenheden in Utrenneye. https://www.thebarentsobserver.com/news/sanctioned-gas-carriers-make-port-calls-at-banned-arctic-terminals/434955
[9] Ketenontwerp en haalbaarheidstoets M31 golf 13 (orkestrator): zeeknopen 4712/5543, 22.667,5 km MARNET-test.
[10] OpenStreetMap-relatie 18865038, "Арктик СПГ-2" (landuse=industrial; bbox 70.9893–71.0034, 73.8081–73.8501), via Nominatim. https://www.openstreetmap.org/relation/18865038
[11] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16): `v2/build-cache/satcheck/sat-gas-utrenneye-beihai-utrenneye-osm.png`, `…-kade-z16.png`, `…-kadez16.png`, `…-laadsteiger-kop.png`, `…-laadsteiger-wortel.png`, `…-gbs.png`, `…-beihai-terminal.png`.
[12] MARNET (`v2/build-cache/marnet-preais`): zeeknoop 4712 op 15,4 km van het complexpunt, 5543 op 17,1 km van de Beihai-kade; `maak_havenaanloop.py` (timeout 300, beide geslaagd).

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
**Bestand:** `v2/data/stroomroute-gas-utrenneye-beihai.json` (41,7 KB, versie 2, lonlat) · functie `bak_gas_utrenneye_beihai` in `v2/tools/bak_stromen.sh` (LF, geen profiel in `maak_stroombeen_weg.py`: geen wegbeen). Recept: `bash v2/tools/bak_stromen.sh gas-utrenneye-beihai`.

| # | modaliteit | km | punten | stippel | naam |
|---|---|---|---|---|---|
| 1 | zee | 18,7 | 17 | ja | haven-aanloop Utrenneye (schematisch, over water, ijs) |
| 2 | zee | 22.667,5 | 2.344 | nee | LNG-tanker Utrenneye → Beihai, westelijke route via Suez (aannemelijk: één bron) |
| 3 | zee | 18,0 | 9 | ja | haven-aanloop Beihai (schematisch, over water) |

Totaal 22.704,2 km, 2.370 punten, 2 markers (`gas-utrenneye-lng`, `gas-beihai-lng`; beide 0,0 km van de lijn). Naden 0,00 km (max 0,00).
**Toets:** MARNET-been 22.667,5 km = de brief (geen gepubliceerde lengte, dus geen ±15 %-norm). `toets_knikken.py`: 4 knikken >= 60 gr (krappe bochten R 7-9 km bij de Noorse kust, Barentszzee en Gibraltar), 0 omkeringen, 0 terugloop. `toets_rechte_benen.py` meldt niets voor deze stroom. `json.load` ok, modaliteit alleen zee.
**Aanlopen:** beide kwamen vooraf uit `maak_havenaanloop.py` (timeout 300, geslaagd) als `--stippel-geojson` in reisvolgorde; de 1:10M-kust, dus schematisch en geen vaargeul. De Utrenneye-aanloop is in werkelijkheid ijs.
**Niet getekend:** NSR-zomerroute, transshipment Murmansk en Koryak, fase A en C (zie §7). Geen vlucht, leiding, extract of letterlijke kopie.
**Les:** de functie en de aanloop-geojsons stonden al klaar van het ontwerp; bakken was één run via het zwaar-slot, zonder herstel.
