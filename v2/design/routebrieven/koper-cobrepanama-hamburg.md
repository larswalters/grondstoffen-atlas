# Routebrief (licht) · koper — Punta Rincón (Cobre Panamá) → Brunsbüttel → Aurubis Hamburg (Duitsland)

**stroom-id:** `koper-cobrepanama-hamburg` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** Cobre Panamá-koperconcentraat (voorraad, sinds juni 2025 geëxporteerd) per **bulkcarrier** vanaf de privéhaven Punta Rincón (First Quantum) over de Atlantische route (Caribische Zee, Atlantische Oceaan, Kanaal, Noordzee, **zonder Panamakanaal**) naar de **Elbehafen Brunsbüttel**, per Schramm-binnenschip ~79 km de Elbe op naar de concentraatkade van **Aurubis Werk Ost, Hamburg** (**aannemelijk: één bron** voor de bestemming) — stoppunt: de concentraatkade, geen been naar de smelter zelf.
**Welke as van het verhaal:** de herstart van Panama-koper na de sluiting (23-11-2023) richting Europa's grootste primaire smelter. Nameplate **> 300 kt Cu/j** (peiljaar 2020 [1]); de mijn staat sinds nov. 2023 stil, geëxporteerd wordt **voorraad: ca. 120 kt concentraat** (goedgekeurd mei 2025 [2][4]). Eerste lading Lipsi (**35.000 dwt** laadvermogen, vertrek 18-6-2025 [2][3]); de geladen tonnage en het aandeel Aurubis zijn **niet gepubliceerd**. Eenheid kt Cu/j: **onbekend** (eenmalige voorraadexport, geen jaarstroom).

## 1 · Ketenkaart
Punta Rincón, haven First Quantum `cu-puntarincon-kade` ──(b1 haven-aanloop · stippel · ~111 km)──► MARNET-zeeknoop 54 (open Caribische kust, 9.7500,-80.0000)
──(b2 zee · Atlantische route · ~9.289 km, aannemelijk: één bron)──► Elbemonding ──(b3 stippel ~4,0 km)──► Elbehafen Brunsbüttel `cu-brunsbuettel-kade`
──(b4 stippel 4,0 · b5 binnenvaart Unterelbe/Norderelbe ~63,8 · b6 stippel 8,2 km)──► Aurubis Werk Ost, kade Müggenburger Kanal `cu-hamburg-konzentratkade` (STOP)
  └── niet getekend: mijn → haven (concentrator 8.8520,-80.6448 → Punta Rincón, ~19 km hemelsbreed): vervoerswijze niet gebronnen (§7)

## 2 · Benen
Geometrie van b3–b6 = **letterlijke kopie** van benen 3–6 van `koper-aurubis-hamburg` (zelfde als `zilver-antofagasta-hamburg`); b1 en b2 zijn nieuw.
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `cu-puntarincon-kade` → zeeknoop 54 | haven-aanloop Punta Rincón (open zee) | ~111 (hemelsbreed, geen gepubliceerde km) | `--stippel` recht (of `maak_havenaanloop`, timeout 300) | ja: kade 111 km van de zeeknoop, MARNET reikt niet |
| b2 | B | zee | zeeknoop 54 → zeeknoop Elbemonding (53.8771, 9.2273) | Caribische Zee → Atlantische Oceaan → Kanaal → Noordzee; géén Panamakanaal (zeeknoop 55 ligt in het Gatúnmeer, bewust niet) | ~9.289 (MARNET-test; eigen schatting, geen gepubliceerde afstand) | MARNET `--been` | nee |
| b3 | B | zee | zeeknoop → `cu-brunsbuettel-kade` | haven-aanloop Brunsbüttel (kade 3,7 km van de zeeknoop) | 4,0 | `aanloop-brunsbuettel-aankomst.geojson` (kopie koper b3) | ja: schematisch |
| b4 | C | binnenvaart | `cu-brunsbuettel-kade` → zeeknoop | vertrek Schramm-shuttle | 4,0 | `aanloop-brunsbuettel.geojson` (kopie b4) | ja: schematisch |
| b5 | C | binnenvaart | (53.8771, 9.2273) → (53.5451, 9.9273) | Unterelbe → Norderelbe (zeevaarweg in MARNET) | 63,8 gebakken; Elbe-km 695 → 618,4 = 76,6 gepubliceerd (Hafen Hamburg, zie koper-aurubis-hamburg [14]) | MARNET `--been` (kopie b5) | nee |
| b6 | C | binnenvaart | Norderelbe → `cu-hamburg-konzentratkade` | Müggenburger Kanal | 8,2 | rechte `--stippel` (kopie b6) | ja: 1:10M-kust kent de haven niet |
Haven-aanloop-regel: Punta Rincón ligt 111 km van de zeeknoop (b1), Brunsbüttel 3,7 km (b3/b4); beide aanlopen zitten in de benen, geen extra. Aanloop b1 is op NE-land getoetst: 0 km over land. **Been A (truck mijn → haven) vervalt** (bindende toets): de voorraad lag bij de haven, vervoerswijze mijn-haven niet gebronnen, OSM heeft geen band of leiding.
Testbake (alleen scratchpad): 6 benen · 9.480,2 km (111,4 + 9.288,8 + 4,0 + 4,0 + 63,8 + 8,2).

## 3 · Ankers (één per site en per overslag; 4 decimalen, lat, lon)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-puntarincon-kade` | laadkade (zee) | Punta Rincón, havendam met kade (privéhaven First Quantum, op het terrein Cobre Panamá) | 9.0204, -80.6964 | [1][2][5] | bron-gelegd (z16 gezien: L-vormige havendam met kadeuitstulping aan de kust, centrale/plantterrein en wegen direct ten oosten; het eerdere pier-anker 9.0115 lag op een landtong zonder kade) |
| `cu-brunsbuettel-kade` | overslag zee → binnenschip | Elbehafen Brunsbüttel, droge-bulkkade | 53.8878, 9.1740 | [8] (letterlijk hergebruikt uit koper-aurubis-hamburg) | bron-gelegd (daar z16: kademuur met havenkranen) |
| `cu-hamburg-konzentratkade` | losplek concentraat | Aurubis Werk Ost, kade Müggenburger Kanal | 53.5163, 10.0418 | [8] (hergebruik) | aannemelijk (bestemming: één bron [2]); kade daar z17 bron-gelegd |
| `cu-hamburg-werkost` | smelter (terrein) | Aurubis Hamburg, Werk Ost | 53.5140, 10.0400 | [8] (hergebruik) | bron-gelegd (daar z15: hüttecomplex) |
| `cu-cobrepanama-concentrator` | mijn (context, geen been) | Cobre Panamá concentrator / dagbouwcomplex, Donoso | 8.8520, -80.6448 | [1] | bron-gelegd (z14 gezien: concentrator en pit-complex, tailingsdepot noordwaarts; geen marker, geen been) |

## 4 · Via-punten
Geen landbenen: geen via-punten. Zee = MARNET kade → kade; binnenvaart = kopie van koper-aurubis-hamburg.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Cobre Panamá concentrator + haven Punta Rincón | First Quantum (Minera Panamá) | erts → concentraat, opslag, verscheping | 85 Mt erts/j, > 300 kt Cu/j nameplate (2020); stil sinds 11-2023, nu voorraadexport | [1][5] |
| Elbehafen Brunsbüttel (overslag + voormenging) | Brunsbüttel Ports / Schramm | zee → binnenschip | ~1,1 Mt concentraat/j | [8] |
| Aurubis Hamburg (primaire smelter) | Aurubis AG | concentraat 0,9–1,3 Mt/j → kathode | ~400 kt Cu/j | [8] |

## 6 · Stoppunt
De brief stopt bij de concentraatkade van Aurubis Werk Ost: Bloomberg noemt alleen Aurubis als afnemer, geen haven, geen vervolgkeuze; verder dan de kade is hetzelfde als koper-aurubis-hamburg en wordt hier niet herhaald.

## 7 · Open punten
- **Bestemming Aurubis = één bron** (Bloomberg 2025-06-27 via Wikipedia en gcaptain, anonieme bronnen, Aurubis reageerde niet) [2][3][4]; de rest van de voorraad ging naar Japan, Zuid-Korea en andere kopers [2]. Haven van lossing niet genoemd: Brunsbüttel is aanname uit het Aurubis-patroon.
- **Geladen tonnage Lipsi onbekend:** 35.000 dwt is laadvermogen, geen lading. De in de toets genoemde "ruim 33 kt volgens het Panamese ministerie" is in mijn bronnen niet teruggevonden en wordt niet als feit overgenomen.
- **Mijn → haven vervoerswijze niet gebronnen** (ontwerp-been A geschrapt): op z14 loopt een rechte lijnstructuur NO-waarts van het plantterrein (mogelijk transportband), niet als bron te gebruiken; wegen ter plaatse OSM-tertiary [ontwerp, niet geverifieerd]. Bij de haven zelf zijn transportbanden bevestigd (weegschalen op banden, AMP 2023 [6]).
- **Aanloop Punta Rincón ~111 km is een rechte stippel** (eigen verbinding zonder net); Atlantische route zonder Panamakanaal is hier een routekeuze, geen bron (de haven ligt Caribisch).
- **Volume:** geen jaarvolume; nameplate stamt uit 2020, mijn stil, 2026-herstart zwak gebronnen (30–40 kt Cu uit voorraadertsen, SMM 2026 [9]).
- Geen gepubliceerde zeeafstand Punta Rincón → Brunsbüttel; 9.289 km is een MARNET-uitkomst (geen onafhankelijke toets).

## 8 · Bronnen
[1] Wikipedia (en), Cobre mine, Panama (nameplate > 300 kt Cu/j, Punta Rincón, export 2025, Aurubis), https://en.wikipedia.org/wiki/Cobre_mine,_Panama
[2] Bloomberg, 2025-06-27, "First Quantum starts shipping stockpiled copper from Panama mine" (Lipsi 18-6-2025, ~120 kt voorraad, Aurubis via anonieme bronnen), https://www.bloomberg.com/news/articles/2025-06-27/first-quantum-starts-shipping-stockpiled-copper-from-panama-mine
[3] gCaptain, 2025, idem (Lipsi, 35.000 dwt, privéhaven Punta Rincón), https://gcaptain.com/first-quantum-starts-shipping-stockpiled-copper-from-panama-mine/
[4] La República / Bloomberg Línea, 2025, "First Quantum reanuda exportaciones desde Cobre Panamá tras 19 meses de cierre" (120.000 t voorraad, Lipsi, Aurubis, rest naar Japan en Zuid-Korea), https://www.larepublica.co/globoeconomia/first-quantum-reanuda-exportaciones-desde-cobre-panama-tras-19-meses-de-cierre-4168365
[5] Energiminas, 2024-01-30, "Cobre Panamá propone traslado de las más de 120.000 toneladas de concentrado de cobre que almacena en puerto Punta Rincón", https://energiminas.com/2024/01/30/cobre-panama-propone-traslado-de-las-mas-de-120000-toneladas-de-concentrado-de-cobre-que-almacena-en-puerto-punta-rincon
[6] La Prensa (Panamá), 2023-03-13, "Minera reactiva operaciones y despacha barcos con concentrado de cobre" (AMP: weegschalen op transportbanden in Punta Rincón), https://www.prensa.com/economia/minera-reactiva-operaciones-y-despacha-barcos-con-concentrado-de-cobre/
[7] Canadian Mining Journal, 2019-06-24, "First Quantum ships first concentrate from Cobre Panama" (eerste export 19-6-2019 vanaf Punta Rincón), https://canadianminingjournal.com/news/copper-first-quantum-ships-first-concentrate-from-cobre-panama
[8] Eigen brief `v2/design/routebrieven/koper-aurubis-hamburg.md` (Brunsbüttel-kade, Werk Ost-kade en benen 3–6; bronnen Hafen Hamburg 2017, Aurubis Umwelterklärung 2022/2025 aldaar)
[9] SMM (metal.com), 2026-07, "Cobre Panama mine restart accelerates…" (voorraaderts, 2026-guidance 30–40 kt Cu), https://news.metal.com/newscontent/104036547-cobre-panama-mine-restart-accelerates-imported-copper-concentrate-spot-tcs-continue-to-deteriorate-smm-copper-concentrat
Satellietbeelden: `v2/build-cache/satcheck/sat-koper-cobrepanama-hamburg-{puntarincon-pier,puntarincon-z15,mijn-z14}.png`. Testbake: scratchpad, niet in de repo.


## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
Recept: `bak_koper_cobrepanama_hamburg()` in `v2/tools/bak_stromen.sh`; draaien met `bash v2/tools/bak_stromen.sh koper-cobrepanama-hamburg` → `v2/data/stroomroute-koper-cobrepanama-hamburg.json` (19,8 KB, versie 2, lonlat). Geen landbenen, geen extract, geen wegprofiel.
| # | modaliteit | been | km gebakken | punten | stippel |
|---|---|---|---|---|---|
| b1 | zee | haven-aanloop Punta Rincón → zeeknoop 54 | 111,4 | 2 | ja (eigen verbinding zonder net) |
| b2 | zee | MARNET zeeknoop 54 → Elbemonding, Atlantische route zonder Panamakanaal | 9.288,8 | 973 | nee |
| b3 | zee | haven-aanloop Brunsbüttel (kopie koper-aurubis-hamburg) | 4,0 | 4 | ja |
| b4 | binnenvaart | vertrek Schramm-shuttle (kopie) | 4,0 | 4 | ja |
| b5 | binnenvaart | Unterelbe → Norderelbe via MARNET (kopie) | 63,8 | 9 | nee |
| b6 | binnenvaart | Norderelbe → Müggenburger Kanal (kopie rechte stippel) | 8,2 | 2 | ja |
Totaal 9.480,2 km · 994 punten, gelijk aan de testbake. Markers (4): Punta Rincón 9.0204,-80.6964; Brunsbüttel 53.8878,9.1740; concentraatkade 53.5163,10.0418; Werk Ost 53.5140,10.0400 (0,28 km van zijn lijn, rest 0,0). De concentrator (mijn) is bewust geen marker.
**Toelichting stippel b1:** `maak_havenaanloop` onder timeout 300 gaf exit 124 (geen tweede poging) → rechte stippel kade → zeeknoop 54 (hemelsbreed 111,4 km, geen gepubliceerde km); 0 km over land getoetst tegen NE 10m land en minor islands. De dichtstbijzijnde zeeknoop 55 ligt in het Gatúnmeer en is bewust niet gebruikt.
**Toelichting b3 t/m b6:** letterlijke kopieën van benen 3 t/m 6 van `koper-aurubis-hamburg` (aanloop-brunsbuettel-aankomst.geojson, aanloop-brunsbuettel.geojson, dezelfde MARNET-`--been` en dezelfde rechte stippel). Elbe 63,8 + 4,0 + 8,2 = 76,0 km tegen 76,6 gepubliceerd.
**Toets:** geen landkilometers te toetsen (geen wegbeen); naden alle 0,0 km (max 0,0 km); markers ≤ 0,28 km van hun lijn; `toets_knikken` 2 knikken (spikes 80 en 86 graden op 50.3375,-0.7643, MARNET-kanaalroute, geen omkeringen, geen terugloop) = bevinding, niet gerepareerd; `toets_rechte_benen --min-km 5` meldt alleen de twee stippels (b1 en b6) zoals bedoeld.
**Aannemelijk:** de bestemming Aurubis is één bron (Bloomberg); dat staat in de beennaam van b2 en in de markernaam, niet in de lijnstijl.
**Lessen:** bij een kade 111 km van de zeeknoop en open zee ertussen loopt `maak_havenaanloop` tegen de timeout aan; direct de rechte stippel nemen scheelt 5 minuten. Een keten die voor 4 van 6 benen kopieert is in één bake-run klaar zonder slot-werk buiten het zwaar-slot.
