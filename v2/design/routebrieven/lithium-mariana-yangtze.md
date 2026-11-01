# Routebrief (licht) · Lithium — Güemes-plant → Antofagasta → Yangtze-monding (Argentinië → Chili → China)

**stroom-id:** `lithium-mariana-yangtze` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** lithiumchloride (LiCl) van Ganfeng's Mariana-project (Salar de Llullaillaco) wordt in de LiCl-plant in het Parque Industrial General Güemes (Salta) gemaakt, gaat per **spoor** (10 containers, 240 t, eerste export feb 2026) over de C14 Salta-Socompa en de FCAB naar Puerto Antofagasta en per **containerschip** naar China — getekend tot de Yangtze-monding (aannemelijk: één bron voor de trein; haven en Chinese afnemer niet gebronnen).
**Welke as van het verhaal:** Argentijnse pekel-LiCl naar China. 20 kt LiCl/j nameplate ≈ 17 kt LCE/j (×0,87; peiljaar 2025-26, nameplate, gestart feb 2025) [4]; eerste export 240 t LiCl ≈ 0,2 kt LCE (feb 2026) [2][3]. Eenheid: kt LCE/j.

## 1 · Ketenkaart
```
Güemes-plant `li-mariana-plant` ──(b1 spoor · C14 Salta → Tolar Grande → Socompa → FCAB Palestina → La Negra · 956,3 km net, aannemelijk)──► Puerto Antofagasta `li-antofagasta-kade`
   ──(b2 zee · haven-aanloop, LETTERLIJKE KOPIE · 97,1 km stippel)──► ──(b3 zee · containerschip · LETTERLIJKE KOPIE · 18.914,3 km)──► Yangtze-monding `li-yangtze-monding` ⏹ stoppunt
   ├── niet getekend: pekel Salar de Llullaillaco → Güemes (tankcontainers per spoor; eigen station nog te bouwen) [1]
   └── niet getekend: alternatieve haven Rosario (≈1.170 km net) — geen bron noemt een haven
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | spoor (container, aannemelijk: trein bronbaar [2][3], haven niet gebronnen) | `li-mariana-plant` → `li-antofagasta-kade` | Ramal C14 Belgrano (Salta, San Antonio de los Cobres, Tolar Grande, Socompa) → FCAB (Palestina, La Negra) → Antofagasta | net 956,3 (1-op-1-OSM); gepubliceerd 571 AR + 330 CL [5][6] + Güemes-Salta ≈ 49 (afgeleid) ≈ 950, dus +0,7 % (de bron noemt als totaal 941, maar 571+330 = 901: bron inconsistent) | toets_spoorroute (BAKE_SUFFIX=-raw, hoofd-km 500, één run, geen via) | nee (kop snapt 1,32 km, staart 0,10 km: geen naad) |
| b2 | B | zee (haven-aanloop) | `li-antofagasta-kade` → zeeknoop -23,80/-71,30 | over water, 97 km (kade > 5 km van zeeknoop) | 97,1 (kopie) | letterlijke kopie `aanloop-antofagasta.geojson` uit `bak_lithium_atacama_antofagasta` | ja: "hier reikt MARNET niet" |
| b3 | B | zee (containerschip, aannemelijk: één bron, China als bestemming) | zeeknoop -23,80/-71,30 → `li-yangtze-monding` | Stille Oceaan, MARNET 50°N-lane | 18.914,3 (kopie van b4 uit atacama; hemelsbreed ≈ 18.560) | MARNET, letterlijk als in `bak_lithium_atacama_antofagasta` | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-mariana-plant` | verwerkingsknoop (LiCl) en spoorkop | Ganfeng LiCl-plant, Parque Industrial General Güemes (parkcentroide; pand niet gevonden) | -24.7035, -65.0331 | [1][2][9][12] | onzeker (z15 gezien: punt ligt in open terrein tussen bebouwde parkblokken, spoor ligt ~1,3 km ervandaan; twee nieuwe blauwgedekte complexen in het zuidpark op -24.7143,-65.0255 en -24.7180,-65.0215, geen bron wijst Ganfeng aan) |
| `li-antofagasta-kade` | overslag spoor → zee | Puerto Antofagasta, ATI | -23.6500, -70.4088 | [11] = `lithium-atacama-antofagasta` | bron-gelegd (hergebruik; z16 `sat-antofagasta-kade.png`: containerstapels op frente 2) |
| `li-yangtze-monding` | aanlanding China (conventie-anker) | Yangtze-monding | 31.42704, 121.47618 | [11] | aannemelijk (bestemming China; Chinese haven en fabriek niet gebronnen) |

Niet gelegd (open punten, geen anker): Mariana-pozen/-plant op de salar (satelliet z14 ≈ -24.7985,-68.2405, ~15-18 km van het spoor; Ganfeng zegt dat het pekelstation nog gebouwd wordt [1]).

## 4 · Via-punten
Geen. De enige corridorkeuze (Socompa-lijn via Palestina/La Negra, niet via Baquedano) volgt uit de railtopologie; één router-run kiest hem. Controle op de gemeten lijn (afstand tot lijn, km vanaf kop): Salta 1,0 km · San Antonio de los Cobres 0,1 km (km 245) · Socompa-grens 0,0 km (km 620) · La Negra 4,2 km (km 909) · Antofagasta 0,1 km (km 958); Baquedano ligt 50,8 km ernaast (de lijn gaat er terecht niet langs).
Omkeringen in de lijn: vier bij Campo Quijano (-24.7589..-24.8533, -65.7108..-65.7446) = de twee zigzags El Alisal/Chorrillos van de C14 [6]; één bij de kop-maakplek van de haven (-23.6329,-70.3911, 2 km ten NW van de kade).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mariana, Salar de Llullaillaco | Litio Minera Argentina (Ganfeng) | pekel → geconcentreerde pekel, tankcontainers per spoor naar Güemes | LiCl-tonnage niet gepubliceerd; 120 MW zonnepark off-grid [1] | [1][3] |
| LiCl-plant Güemes | Litio Minera Argentina (Ganfeng) | concentraat → lithiumchloride, 24 t per container | 20 kt LiCl/j ≈ 17 kt LCE/j nameplate | [2][3][4] |
| Puerto Antofagasta | EPA/ATI | containers per trein → schip | zie `lithium-atacama-antofagasta` | [11] |

## 6 · Stoppunt
Fase B naar de Yangtze-monding: Ganfeng noemt alleen "per trein vanuit Güemes" en "voor China" — geen haven, geen Chinese afnemer; fase D/E vervallen en de lijn eindigt waar het bewijs eindigt.

## 7 · Open punten
- **Haven onbewezen:** Antofagasta is de aanname (de Salta-Antofagasta-lijn vervoert al lithiumcarbonaat en pekel [5][6]); Rosario (≈ 1.170 km net) is het alternatief. Staat in de beennaam als aannemelijk.
- **Plantpand Güemes** niet gevonden: parkcentroide, status onzeker; spoor snapt 1,32 km. Twee kandidaat-complexen in het zuidpark (zie §3); het noordelijke is POSCO's [lithium-saldeoro-guemes §3].
- **Mariana-pozen/kamp, pekelstation en de pekelrit salar → spoor (21 km)** niet getekend: geen anker, station nog niet gebouwd [1].
- **Geen gepubliceerde spoorkm voor Güemes-Antofagasta.** Toets op delen: Salta-Socompa 571 km [6] tegen gemeten Güemes-Socompa 620 minus Güemes-Salta ≈ 49 = 571; Socompa-Antofagasta 330 [6] tegen gemeten 338 (+2 %). De bron geeft als totaal 941 (infobox 931) maar 571+330 = 901: tegenspraak in de bron, dus alleen de delen zijn gebruikt. Indicatie, geen ±15 %-norm.
- **Volume:** 20 kt LiCl/j is nameplate (Reuters 2025-02-12 [7] niet opengebracht, cijfer uit [4]); gerealiseerde export tot nu 240 t.
- **Gedeelde kopie:** de aanloop-kopie en het zeebeen zijn gedeeld met `lithium-atacama-antofagasta`; wijzig niets aan die bestanden.

## 8 · Bronnen
[1] Ganfeng Lithium LATAM, Proyecto Mariana: pekel in tankcontainers per spoor naar Güemes, eigen spoorstation in aanbouw, fabriek Güemes sinds 2022, 430 km van Salta, 95 km van Tolar Grande, 120 MW solar. https://ganfenglithium-latam.com/proyecto-mariana/
[2] Ganfeng LATAM, 18-02-2026, "De Salta al mundo": eerste export LiCl, 10 containers à 24 t = 240 t, "traslado en tren" vanuit de plant in General Güemes, geen haven genoemd. https://ganfenglithium-latam.com/en/2026/02/18/de-salta-al-mundo-ganfeng-lithium-exporto-cloruro-de-litio-por-primera-vez-desde-su-planta-de-proceso-en-general-guemes/
[3] Panorama Minero, eerste export Ganfeng: 240 t LiCl per spoor vanuit Güemes, aangegeven voor China. https://panorama-minero.com/en/news/ganfeng-completed-its-first-export-lithium-from-salta-to-the-world-a-milestone-for-argentine-mining
[4] Mase/LM Neuquén, 12-02-2025: Ganfeng opent Argentijnse plant, 20.000 t LiCl; geplande spoorverbinding pekel naar de fabriek. https://mase.lmneuquen.com/mineria/el-gigante-chino-ganfeng-inaugura-su-planta-argentina-20000-toneladas-litio-n1173613
[5] es.wikipedia, Ferrocarril Antofagasta-Salta: 941 km (571 AR + 330 CL; infobox 931), Palestina, La Negra, vracht litiumcarbonaat en salmuera. https://es.wikipedia.org/wiki/Ferrocarril_Antofagasta-Salta
[6] en.wikipedia, Salta-Antofagasta railway: 941 km, twee zigzags (El Alisal, Chorrillos), Palestina-kruising, La Negra, 22 km tot Antofagasta. https://en.wikipedia.org/wiki/Salta%E2%80%93Antofagasta_railway
[7] Reuters, 12-02-2025, "China's Ganfeng starts lithium production at Argentina's Mariana project" (door ontwerp aangeleverd; 403, niet gelezen). https://www.reuters.com/markets/commodities/chinas-ganfeng-starts-lithium-production-argentinas-mariana-project-2025-02-12/
[8] iProfesional, Proyecto Mariana, eerste export LiCl (zoekresultaat: 10 containers, trein vanuit Güemes, geen haven). https://www.iprofesional.com/energia/448568-proyecto-mariana-ganfeng-concreta-primera-exportacion-de-cloruro-de-litio-desde-salta
[9] OSM/Nominatim, Parque Industrial General Güemes -24.70351,-65.03312. https://www.openstreetmap.org
[10] Rail Journal, Argentina launches new freight service (ontwerp; 403, niet gelezen). https://www.railjournal.com/freight/argentina-launches-new-freight-service/
[11] `v2/design/routebrieven/lithium-atacama-antofagasta.md` §3/§9 en `bak_lithium_atacama_antofagasta` in `v2/tools/bak_stromen.sh`: anker `li-antofagasta-kade` -23.6500,-70.4088, `aanloop-antofagasta.geojson` (97,1 km), MARNET zeeknoop -23.80,-71.30 → Yangtze-monding 18.914,3 km.
[12] Esri World Imagery via `v2/tools/sat_check.py` (z15/z16, 2026-11-01): `v2/build-cache/satcheck/sat-lithium-mariana-yangtze-{guemes-park,guemes-park-z15,guemes-zuid-z16}.png`; `v2/design/routebrieven/lithium-saldeoro-guemes.md` §3 (twee complexen in het zuidpark).
[13] `v2/tools/toets_spoorroute.mjs` (BAKE_SUFFIX=-raw, hoofd-km 500): 956,3 km over 579 edges, snaps 1,32/0,10 km, grootcirkel 557,7 km; geojson `v2/build-cache/ais/graaf/spoorroute-lithium-mariana-yangtze-guemes-antofagasta.geojson` (3.649 punten).

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)

**Stroom `lithium-mariana-yangtze`** → `v2/data/stroomroute-lithium-mariana-yangtze.json` (108,7 KB): 3 benen, 19.969,5 km, 3 markers. Spoor 958,1 km, zee (stippel, haven-aanloop) 97,1 km, zee 18.914,3 km. Naden: spoor-aanloop 0,102 km (spoorkop snapt vanaf het routeerpunt), aanloop-zee 0,000 km.
Recept: `bak_stromen.sh`, functie `bak_lithium_mariana_yangtze` (geen wegprofiel, geen wegscan, geen vlucht, geen leiding). Het spoorbeen is het vooraf gebakken `spoorroute-lithium-mariana-yangtze-guemes-antofagasta.geojson` (toets_spoorroute, BAKE_SUFFIX=-raw, hoofd-km 500, geen via), als `--been-geojson` doorgetrokken. Bake in één run via het zwaar-slot.

Toelichting per been.
- **b1** (spoor): C14 Salta-Socompa, FCAB Palestina, La Negra, Antofagasta. Gebakken lengte 958,1 km (3.649 punten) tegen circa 950 uit 571 AR + 330 CL + Güemes-Salta circa 49 = +0,9 procent; de bron noemt 941 maar 571+330 = 901, dus alleen de delen zijn indicatie. Geen echte wegkm, geen norm. Doorgetrokken: trein bronbaar, haven niet; dat staat in de beennaam.
- **b2** (stippel, zee): haven-aanloop Antofagasta, 97,1 km, 46 punten, LETTERLIJKE KOPIE van `aanloop-antofagasta.geojson`. Stippel = hier reikt MARNET niet.
- **b3** (zee): zeeknoop -23,80/-71,30 naar Yangtze-monding, 18.914,3 km, 1.939 punten, LETTERLIJK dezelfde regel als atacama. Naad-invariant -0,381 km.

**Markers** (3, uit §3): Güemes-plant 1,32 km van de lijn (parkcentroide, onzeker; het spoor snapt daar) · ATI-kade 0,0 km · Yangtze-monding 4,45 km (zee-snap van het gedeelde anker 10,7 km, anker is niet routeerpunt).

**Toets.** json.load: versie 2, punt_formaat lonlat, modaliteiten {spoor, zee}, elk been >= 46 punten, 108,7 KB. `toets_knikken.py`: spoor 5 omkeringen >= 150 graden, waarvan 2 door de tool als terugloop gemarkeerd bij Campo Quijano (-24,7589/-65,7446 en -24,7631/-65,7419, radius 50 en 112 m): dat zijn de zigzags El Alisal/Chorrillos van de C14, echt spoor, niet gerepareerd; de andere 3 zijn scherpe bochten (2 zigzag, 1 kopmaakplek haven -23,6329/-70,3911); zee 0 knikken. `toets_rechte_benen.py` leest alleen de gebundelde stromen: deze stroom staat er nog niet in; geen rechte lijn buiten de stippel (46 punten).

**Open punten/bevindingen.**
- Haven onbewezen (Antofagasta aanname, Rosario alternatief); plantpand Güemes niet gevonden (parkcentroide, 1,32 km van het spoor).
- Pekelrit Salar de Llullaillaco naar spoor (21 km), pozen en pekelstation niet getekend.
- Het sitelaag-punt van Mariana staat niet op dit plant-anker: centraal gelijktrekken als de sitelaag het bevat.

**Gereedschapslessen:**
- Een vooraf gebakken spoorgeojson uit de build-cache gaat als `--been-geojson "spoor|..."` rechtstreeks de functie in; de bake herrout het niet (regel "vooraf gebakken lijn") en kost geen router-run.
- Gedeelde haven-aanloop en MARNET-zeebeen overnemen kost niets: dezelfde twee regels als in `bak_lithium_atacama_antofagasta`.
- De terugloop-vlag van toets_knikken bij een bergspoor met zigzags is geen fout; de brief had de plek al benoemd.
