# Routebrief (licht) · Nikkel — Punta Gorda (Cuba) → Panamakanaal → Yangtze-monding (China)

**stroom-id:** `nikkel-puntagorda-yangtze` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** nikkelproduct van de staatsfabriek Ernesto Che Guevara (Cubaniquel, Moa) gaat per **truck** over de Carretera a Punta Gorda naar de Punta Gorda-steiger en per **bulkschip** (Windward Passage, Panamakanaal, Stille Oceaan, Straat van Tsugaru en Korea-straat, door MARNET gekozen) naar China; Chinese haven en afnemer staan in geen bron, dus het eindpunt is het conventie-anker Yangtze-monding (aannemelijk: één bron, secundair). De fabriek draait onder capaciteit en staat onder VS-sancties [3][5].
**Welke as van het verhaal:** *Cubaanse staatsnikkel naar China*, de tweede Cubaanse as naast de Sherritt-JV-lijn naar Canada (`nikkel-moa-fortsaskatchewan`). Volume: **ca. 20 kt Ni/j (indicatie)**: 2025 minder dan 20 kt volgens Diario de Cuba (via zoekresultaat, pagina gaf 403) [3], 18,5 kt in 2016 bij 30 kt capaciteit [6], plan 19 kt in 2018 [5]; hoeveel daarvan naar China gaat is niet uitgesplitst (heel Cuba 2024: China 53,1 M USD van ca. 88,5 M USD aan matte en tussenproducten) [2]. Eenheid kt Ni/j, peiljaar 2025.

## 1 · Ketenkaart
```
Che Guevara-fabriek `ni-cheguevara-fabriek` ──(b1 truck · Carretera a Punta Gorda · 4,7 km)──► Punta Gorda-steiger `ni-puntagorda-pier` (onzeker)
 ──(b2 zee, STIPPEL · haven-aanloop · 70,9 km, KOPIE)──► MARNET-zeeknoop 8163 (21.1135,-74.4068)
 ──(b3 zee · Windward Passage, Panamakanaal, Stille Oceaan · 17.590,0 km)──► MARNET-eindknoop 9654 (31.5100,121.4187)
 ──(b4 zee · overgangsstippel · 8,6 km, KOPIE)──► Yangtze-monding `ni-yangtze-monding` ⏹ stoppunt (Chinese afnemer niet gebronnd)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (aannemelijk: één bron voor deze schakel) | `ni-cheguevara-fabriek` → `ni-puntagorda-pier` | Carretera a Punta Gorda (OSM highway=secondary) + fabrieksservicewegen | 4,7 gemeten; hemelsbreed 2,7 km, **geen wegkm**: de ±15%-toets is indicatie (+65%, de eerste 1,4 km gaat over service-ways binnen en langs het fabrieksterrein) [8] | `maak_stroombeen_weg` (profiel staat al in het script) | nee |
| b2 | B | zee (haven-aanloop) | `ni-puntagorda-pier` → zeeknoop 8163 | — | 70,9 gemeten (rechte lijn 70,5) [9] | **letterlijke kopie** `kobalt-moa-fortsaskatchewan-aanloop-moa.geojson` | **ja**: MARNET reikt niet tot de kade (> 25 km) |
| b3 | B | zee (bulkschip, aannemelijk: één bron voor de bestemming) | zeeknoop 8163 → eindknoop 9654 | Windward Passage, Caribische Zee, Panamakanaal, Stille Oceaan (grootcirkel langs de Aleoeten), Straat van Tsugaru, Korea-straat, Oost-Chinese Zee | **17.590,0** (eigen MARNET-run 2026-11-01, 91 edges, snaps 0,000; ontwerp indicatie 18.000–19.500; geen gepubliceerde lengte) | MARNET `--been zee` | nee |
| b4 | B | zee (overgang) | 31.5100,121.4187 → 31.4512,121.4769 | MARNET houdt hier op | 8,6 [10] | **letterlijke kopie** van de overgangsstippel in `bak_nikkel_taganito_yangtze` / `bak_lithium` | ja: MARNET reikt niet |

Totaal 17.674,2 km (proefbake naar de scratchpad, niet in het register). Geen last-mile-been: het eindanker `ni-yangtze-monding` ligt 2,7 km voorbij b4 (binnen de naadnorm). Fase D/E vervallen (§6).
Overlap, eerlijk: b2 is dezelfde aanloop als `nikkel-moa-fortsaskatchewan` (zelfde steiger, zelfde zeeknoop); b3 loopt tot de Panamacorridor gelijk aan andere Atlantisch-Pacifische lijnen; b1 en het zeebeen vanaf 8163 zijn nieuw.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-cheguevara-fabriek` | fabriek / laadplek (sinter, eerste anker) | Fábrica de Níquel Ernesto Che Guevara (Cubaniquel), tussen de rivieren Moa en Yagrumaje, ~2 km van het dorp Punta Gorda | 20.6363, -74.8805 | [1][8] (OSM works) | **bron-gelegd** (z15 gezien, `sat-nikkel-puntagorda-yangtze-plant.png`: tankpark met een twintigtal ronde tanks, productiehallen, schoorsteenpluim, kruis op de hal; tailingsvijver ten zuidoosten) |
| `ni-puntagorda-pier` | overslag land → zee | Punta Gorda-steiger, Bahía de Moa; **hergebruik letterlijk** `ni-moa-laad` uit `nikkel-moa-fortsaskatchewan.md` §3 | 20.6372, -74.8549 | [7][9] | **onzeker** (z15/z16 gezien, `sat-nikkel-puntagorda-yangtze-pier.png` en `-pier-z16.png`: kleine steiger op de kaap bij het dorp, geen kraan of laadbrug; havendata noemt een offshore-terminal met lichters) |
| `ni-yangtze-monding` | aanlanding China (stoppunt, conventie-anker) | Yangtze-monding; **hergebruik letterlijk** uit `nikkel-taganito-yangtze.md` §3 | 31.42704, 121.47618 | [10] | aannemelijk (conventie; MARNET-eindknoop 10,7 km ervandaan) |

Markers voor de bak (tekst `nikkel-taganito-yangtze` voor de Yangtze): `Yangtze-monding — aanlanding China (stoppunt, conventie-anker), aannemelijk|31.42704,121.47618`.

## 4 · Via-punten (alleen b1; corridorkeuze op de Carretera a Punta Gorda)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Carretera a Punta Gorda, oost van de fabriek | 20.6336, -74.8698 | voert de lijn van de fabrieksweg naar de doorgaande secundaire weg (z15: weg buigt hier om de fabriek naar het oosten); snap 0,03 km |
| b1 | 2 | Carretera a Punta Gorda, westrand van het dorp | 20.6313, -74.8606 | vóór het dorp, op de doorgaande weg en niet in de dorpsstraten; snap 0,07 km |

Extracts: `cuba`; refs: geen (OSM-ways zonder ref); `vensterKm` 12. Bake `python v2/tools/wegscan_puur.py --profiel nikkel-puntagorda-yangtze-cheguevara-pier` (16 s, pyosmium geblokkeerd).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Che Guevara-fabriek, Moa | Cubaniquel (staatsbedrijf; geen Sherritt-aandeel) | lateriet → nikkel (Caron-proces: ammoniaklooi, calcinatie en sinterstap; productvorm niet bewezen) | ontwerp 30 kt; 2016 18,5 kt, 2018 plan 19 kt, 2025 < 20 kt | [1][3][5][6] |

## 6 · Stoppunt
De brief stopt aan de Yangtze-monding: bronnen noemen China als hoofdafnemer maar geen haven, smelter of fabriek [2][3][4]; fase D vervalt (geen bron noemt een fabriek), E vervalt.

## 7 · Open punten
- **Pier onzeker.** Geen bron zegt dat deze fabriek via de Punta Gorda-steiger verscheept; de steiger is op z16 klein, havendata spreekt van een offshore-terminal met lichters [7]. Alternatief is de Moa-haven (OSM landuse industrial 20.6548,-74.9061; havendata: zwavel en nikkel) [7][8], de haven van de Sherritt-lijn; niet getekend.
- **Bestemming één bron, secundair.** Alleen aggregaten: China eerste bestemming voor Cubaanse nikkelmatte en tussenproducten (2024: 53,1 M USD) [2], Diario de Cuba noemt China hoofdafnemer [3]; geen lading-, haven- of fabriekscijfer. Een SMM-bericht van 2018 zegt dat Cuba vooral Che Guevara-productie naar China exporteert (5.000 t tussenproduct apr–okt 2018) [4].
- **Productvorm en volume.** Of het sinter, oxide of een tussenproduct is, zeggen de bronnen niet; 20 kt is een bovengrens voor 2025, geen verscheping naar China. v1 (`data/nickel.js`) rekent 25 kt Ni voor Moa naar China als natte-vingercijfer en noemt het gemengd sulfide: dat is de Sherritt-JV, niet deze fabriek.
- **Stilgevallen of gesanctioneerd.** Fabriek onder capaciteit, VS-sancties 2026 over de Cubaanse nikkelsector (data per bron verschillend; SCMP gaf 403, alleen via zoekresultaat) [3]; Chinese apparatuur geplaatst (april 2026) [2]. De lijn toont infrastructuur, geen bewezen actieve lading.
- **Routekeuze zee onbewezen.** MARNET kiest de noordelijke Stille-Oceaanroute via Tsugaru; geen bron noemt de vaarroute of het Panamakanaal.
- **b1 omweg.** +65% ten opzichte van hemelsbreed komt uit de service-ways rond het fabrieksterrein; geen gepubliceerde wegkm.
- **Sitelaag.** `w-moa-puntagorda` (kobalt-sitelaag) is een kaap-coördinaat, geen fabriek; niet aangeraakt.
- **Oude brief.** `nikkel-moa-fortsaskatchewan.md` labelt de plant bij Punta Gorda als Moa-JV; dat is de staatsfabriek, de JV-plant ligt bij Moa-stad (alleen gemeld).

## 8 · Bronnen
[1] es.wikipedia, Empresa de Níquel Comandante Ernesto Che Guevara (Caron-proces, plant ~5 km van Moa en ~2 km van Punta Gorda; staatsbedrijf). https://es.wikipedia.org/wiki/Empresa_de_Níquel_Comandante_Ernesto_Che_Guevara
[2] Periódico Cubano, 12-04-2026, "China invierte en la fábrica de níquel en Moa tras la salida de la canadiense Sherritt": Chinese sedimentator in de Che Guevara-fabriek; China 2024 eerste bestemming voor Cubaanse nikkelmatte en tussenproducten, 53,1 M USD (Nederland 35,4). https://www.periodicocubano.com/china-invierte-en-la-fabrica-de-niquel-en-moa-tras-la-salida-de-la-canadiense-sherritt/
[3] Diario de Cuba, 2026 (pagina gaf 403, alleen via zoekresultaat): Che Guevara in 2025 minder dan 20 kt van meer dan 30 kt ontwerp; China hoofdafnemer; VS-sancties over het nikkelcircuit. https://diariodecuba.com/economia/1787397937_68577.html
[4] SMM, Cuba Ni+Co-productie (2018): Cuba exporteert vooral de Che Guevara-productie naar China; ca. 5.000 t hydrometallurgisch tussenproduct apr–okt 2018 (3,5% van de Chinese invoer). https://news.metal.com/es/newscontent/100913088-[smm-analysis]-what-is-the-impact-of-the-production-of-nickel-and-cobalt-sulfides-in-cuba-exceeding-50-000-tons
[5] OnCuba News/EFE, 13-12-2018: Che Guevara plan 19 kt Ni; China hoofdafnemer van Cubaans nikkel, ca. 600 M USD/j. https://oncubanews.com/cuba/produccion-de-niquel-y-cobalto-cubanos-alcanzara-las-50-mil-toneladas-segun-previsiones
[6] Diario Las Américas/EFE, 17-06-2016: Che Guevara 18.500 t/j bij 30.000 t capaciteit, China hoofdklant. https://www.diariolasamericas.com/eficiencia-socios-extranjeros-y-apertura-eeuu-retos-del-niquel-cubano-n3883292
[7] BANSAR, Punta Gorda (offshore-terminal, lichters, max LOA 134 m, diepgang 8,5 m, 20.6333,-74.8500) en Moa-haven (zwavel en nikkel). https://www.bansarchina.com/largest-cuba-ports/
[8] OpenStreetMap (ODbL) via Photon: works Che Guevara 20.6363,-74.8805; locality Punta Gorda 20.6363,-74.8546; Carretera a Punta Gorda (secondary); Puerto de Moa (landuse industrial). Weggeometrie uit de lokale Geofabrik-extract `cuba`.
[9] Eigen briefs `kobalt-moa-fortsaskatchewan.md` en `nikkel-moa-fortsaskatchewan.md` (steiger-anker, aanloop 70,9 km, zeeknoop 8163).
[10] Eigen brief `nikkel-taganito-yangtze.md` en functie `bak_nikkel_taganito_yangtze` (Yangtze-monding, eindknoop 9654, overgangsstippel 8,6 km).
[11] Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-nikkel-puntagorda-yangtze-{plant,pier,pier-z16}.png`.

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
**Recept:** `bash v2/tools/bak_stromen.sh nikkel-puntagorda-yangtze` (functie `bak_nikkel_puntagorda_yangtze`) → `v2/data/stroomroute-nikkel-puntagorda-yangtze.json` (37,7 KB, versie 2, punt_formaat lonlat). b1 = profiel `nikkel-puntagorda-yangtze-cheguevara-pier` (wegscan_puur.py, extract `cuba`, 2 via-punten; uitvoer `nikkel-puntagorda-yangtze-weg-cheguevara-pier.geojson` uit de cache hergebruikt, 4,677 km, 65 punten); b2 en b4 letterlijke kopieën; b3 MARNET.

| # | modaliteit | been | km | punten | lijnstijl |
|---|---|---|---|---|---|
| b1 | truck | Che Guevara-fabriek → Punta Gorda-steiger (Carretera a Punta Gorda) | 4,7 | 65 | doorgetrokken |
| b2 | zee | haven-aanloop steiger → zeeknoop 8163, kopie `kobalt-moa-fortsaskatchewan-aanloop-moa.geojson` | 70,9 | 49 | stippel (MARNET reikt niet tot de kade) |
| b3 | zee | zeeknoop 8163 → MARNET-eindknoop 9654 (Windward Passage, Panamakanaal, Stille Oceaan, Tsugaru, Korea-straat), snaps 0,000 | 17.590,0 | 1.807 | doorgetrokken |
| b4 | zee | overgang → Yangtze-bulklaag, kopie uit `bak_nikkel_taganito_yangtze` | 8,6 | 2 | stippel (MARNET reikt niet) |
| | | **totaal** | **17.674,2** | 1.923 | |

**Markers (3):** `ni-cheguevara-fabriek` (20.6363, -74.8805; op de lijn), `ni-puntagorda-pier` (20.6372, -74.8549; op de lijn), `ni-yangtze-monding` (31.42704, 121.47618; 2,69 km voorbij het einde van b4, binnen de naadnorm).

**Toets:** km per been gelijk aan de proefbake en de brief (4,7 / 70,9 / 17.590,0 / 8,6; totaal 17.674,2). b1: geen gepubliceerde wegkm, hemelsbreed 2,7 km, dus de +-15%-toets is indicatie (+73% hemelsbreed, zie open punt omweg). Naden 0,000 km tussen alle benen. `toets_knikken.py`: 6 knikken >= 60 gr, 0 omkeringen, 0 terugloop (truck: 5 spikes/bochten tussen 65 en 95 gr op service-ways rond het fabrieksterrein en in de dorpsbebouwing; zee: 71,8 gr bij 9.118,-79.803, de Panamakanaal-bocht). `toets_rechte_benen.py --min-km 5`: alleen de overgangsstippel b4 (8,6 km, bedoeld). json.load slaagt, versie 2, lonlat, modaliteiten {truck, zee}, elk been >= 2 punten.

**Toelichting stippel/aanloop:** b2 is een haven-aanloop omdat de steiger 70,9 km over water van zeeknoop 8163 ligt (> 5 km, LAR-586); letterlijke kopie, dezelfde aanloop als `kobalt-moa-fortsaskatchewan` en `nikkel-moa-fortsaskatchewan`. b4 is de bestaande overgangsstippel naar de Yangtze-bulklaag. "Aannemelijk: een bron" voor de bestemming staat in de beennaam van b3, niet in de lijnstijl. Geen vlucht, leiding of spoor.

**Lessen:** (1) Het wegprofiel stond al in `maak_stroombeen_weg.py` en de cache-uitvoer van b1 lag er al: geen nieuwe wegscan nodig, alleen de functie en een zwaar-slot voor de bake (~1 min). (2) Een zee-keten met twee kopieën en één wegbeen bakt in één run. (3) Eindpunt in het id (Yangtze-monding) valt samen met het werkelijke eindpunt: geen afwijking van het ontwerp.

**Registerregel (centraal):** `{ "sleutel": "ni-py", "bestand": "stroomroute-nikkel-puntagorda-yangtze.json", "grondstof": "nikkel", "label": "Punta Gorda → Yangtze-monding", "aan": true, "noot": "M31 · golf 20 (2026-11-01): Cubaans nikkel van de Che Guevara-fabriek per truck naar Punta Gorda en per bulkschip via het Panamakanaal naar China (aannemelijk), eindpunt Yangtze-monding" }`
