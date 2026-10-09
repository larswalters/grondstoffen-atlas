# Routebrief (licht) · Lithium · Cauchari-Olaroz → Paso de Jama → Antofagasta (China)

**stroom-id:** `lithium-cauchari-antofagasta` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**Keten in één zin:** lithiumcarbonaat uit de Cauchari-Olaroz-plant (Minera Exar, Jujuy) gaat per **truck** over RN52, Paso de Jama (Ruta 27) en Ruta 23/25/5/26 (~530 km) naar de ATI-kade van Puerto Antofagasta en per **containerschip** over de Stille Oceaan naar China — getekend tot de Yangtze-monding (aannemelijk: één bron voor de Chileense haven, één voor China).
**Welke as van het verhaal:** de reserve-as *Argentijns pekel-carbonaat over de Andes naar Chili* — maar de hoofdroute is Buenos Aires (2024: > 25 kt geproduceerd, 28 kt geëxporteerd via Buenos Aires [3]); sinds feb 2025 is een deel via "noordelijke Chileense havens" toegestaan, eerste lading tien trucks [2][3]. Jaarvolume 2025: 34 kt LCE op 100 %-basis (Lithium Argentina, grafiek "100 % basis") [4]; nameplate 40 kt/j [5]; het Chili-aandeel is niet gepubliceerd. Eenheid: kt LCE/j (carbonaat = LCE 1:1).

## 1 · Ketenkaart
```
Cauchari-Olaroz-plant `li-cauchari-plant` ──(b1 truck · RN52 → Paso de Jama → Ruta 27/23/25/5/26 · ~530 km, aannemelijk)──►
Puerto Antofagasta, ATI `li-antofagasta-kade` ──(b2 zee · haven-aanloop 97 km + containerschip · ~18.900 km, aannemelijk: één bron)──►
Yangtze-monding `li-yangtze-monding` ⏹ stoppunt
├── vertakking (niet getekend): hoofdroute Buenos Aires, RN52 → RN9 → RN34 (zie lithium-olaroz-naraha b1) [2][3]
├── vertakking (niet getekend): Mejillones als alternatieve Chileense haven [1]
└── vertakking (niet getekend): Ganfeng-converters in China (geen fabriek/haven gebrond)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (carbonaat, gesloten trucks/containers, aannemelijk) | `li-cauchari-plant` → `li-antofagasta-kade` | toegangsweg → RN52 → Paso de Jama → Ruta 27 → Ruta 23 → Ruta 25 → Ruta 5 Norte → Ruta 26 | 530 [1] (bedrijfsopgave Antofagasta "530 km"; hemelsbreed 371 km; OSRM 544,1 = OSM-afgeleide indicatie, +2,6 %) | maak_stroombeen_weg, extracts argentina + chili | nee; plantweg (9 km) is de enige kandidaat voor "geen wegpad" → dan korte stippel last mile |
| b2 | B | zee (containerschip) | `li-antofagasta-kade` → `li-yangtze-monding` | Stille Oceaan, 50°N-lane (MARNET) | ~18.900 (kopie: 97,1 aanloop + 18.914,3 zee); hemelsbreed ≈ 18.560 | LETTERLIJKE KOPIE van lithium-atacama-antofagasta: `aanloop-antofagasta.geojson` + MARNET zeeknoop 4664 (-23.80,-71.30) → Yangtze-monding | aanloop: ja, bestaand bestand (kade 92,2 km van de zeeknoop); *aannemelijk: één bron* in de beennaam |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-cauchari-plant` | plant (pekel → Li2CO3) | Minera Exar, Cauchari-Olaroz, procesplant bij de zuidelijke vijvers | -23.6720, -66.7680 | [1][12][13] afleiding; sitelaag-punt -23.7362,-66.7286 is een salarcentroïde, 8,2 km ernaast | aannemelijk (z15 gezien: procesgebouwen met leidingwerk, kampgebouwen en tanks direct onder de vijvervelden; een grindweg ~0,7 km ten westen past bij "Route 70 ~1 km van de plant" [1]; geen naambord, identificatie door afleiding) |
| `li-antofagasta-kade` | overslag truck → zee | Puerto Antofagasta, ATI (frente 2) | -23.6500, -70.4088 | [10] hergebruik uit lithium-atacama-antofagasta | bron-gelegd (hergebruik; z15 vandaag: pier met schip en containerstapels aan de landzijde; welk sitio de lithiumcontainers laadt is open) |
| `li-yangtze-monding` | aanlanding China | Yangtze-monding (bestaand anker) | 31.42704, 121.47618 | [10] | aannemelijk (Ganfeng is Chinees; geen fabriek, geen terminal aangewezen) |

## 4 · Via-punten (alleen b1; coördinaten op de weg gecontroleerd met OSRM-nearest: 0–3 m)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | RN52, aansluiting van de plantweg | -23.6086, -66.7429 | RN52 westwaarts naar Jama, niet oostwaarts naar Susques/RN9 (= de Buenos Aires-route) |
| b1 | 2 | RN52 / Ruta 27, grenspost Paso de Jama | -23.2266, -67.0629 | Paso de Jama, niet Paso de Sico of een zuidelijker pas |
| b1 | 3 | Ruta 23 tussen San Pedro de Atacama en Calama | -22.6068, -68.6729 | noordwaarts naar Calama, niet over de zoutvlakteweg naar Baquedano (corridor van atacama-antofagasta) |
| b1 | 4 | Ruta 25, zuidrand Calama (rondweg, niet het centrum) | -22.4948, -68.9261 | Ruta 25 naar Ruta 5, niet Ruta 24/Chuquicamata |
| b1 | 5 | Ruta 25 / Ruta 5 Norte | -23.1859, -69.6378 | Ruta 5 Norte zuidwestwaarts naar Antofagasta |
| b1 | 6 | Ruta 5 Norte ZW van Baquedano (zelfde punt als atacama-antofagasta b1 via 6) | -23.4488, -70.0523 | houdt Ruta 5 vast |
| b1 | 7 | kruising Ruta 5 / Ruta 26 (zelfde als atacama-antofagasta b2 via 1) | -23.6047, -70.2685 | Ruta 26 naar de stad, niet Ruta 28 via La Negra (langer) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Cauchari-Olaroz | Exar: Ganfeng 46,7 % · Lithium Argentina 44,8 % · JEMSE 8,5 % | pekel → batterijkwaliteit Li2CO3 | 40 kt/j nameplate; 2025: 34 kt LCE (100 %) | [4][5] |

## 6 · Stoppunt
De brief stopt op de Yangtze-monding: Ganfeng heeft recht op 80 % van het aandeel van Lithium Argentina [1][5], maar geen bron noemt de Chinese converter of containerhaven voor deze lading — fase D/E vervallen en de lijn eindigt waar het bewijs eindigt.

## 7 · Open punten
- **Haven niet bevestigd:** Antofagasta en Mejillones staan als "likely embarkation ports" in het plan van 2016/17 [1]; de 2025-bronnen noemen alleen "noordelijke Chileense havens" [2][3]. Antofagasta is gekozen op ankerhergebruik (ATI + aanloop bestaan), niet op een bron die deze lading bij naam noemt. Mejillones/ander terminal blijft mogelijk.
- **Volume per route onbekend:** 2024 ging 28 kt via Buenos Aires [3]; het Chili-deel is een pilot (10 trucks in feb 2025). Het getekende been draagt dus een klein deel van de 34 kt.
- **Plant-anker** is door afleiding gelegd (geen bord op de satelliet); sitelaag-punt `w-li-cauchari-olaroz` ligt 8,2 km ernaast (salarcentroïde) en hoort centraal gelijkgetrokken te worden (niet door mij aangepast).
- **Bestemming China** volgt uit Ganfeng als eigenaar/afnemer, niet uit een zending; Yangtze-monding is een vaarweg-anker, geen terminal.
- **Bak-risico's:** (1) de 9 km plantweg is OSRM-"naamloos", vermoedelijk `service`/`track` — zie de les in lithium-olaroz-naraha §9: `corridorKlassen` met `unclassified`/`residential`/`service` en `eindKlassen` met `track`; lukt dat niet, dan een korte stippel "last mile (geen net op deze korrel)". (2) OSRM noemt het punt op Ruta 23 "Ruta B-195": refs ruim zetten (23, B-195). (3) `pyosmium` is geblokkeerd: `v2/tools/wegscan_puur.py` of een wrapper; extracts argentina + chili (weg-slot).
- Geen eigen bron voor de wegkilometer anders dan [1]; de ±15 %-toets (450–610 km) is dus tegen één bedrijfsopgave.

## 8 · Bronnen
[1] Lithium Americas, NI 43-101 technical report Cauchari-Olaroz (SEC ex. 99.5, 2018): Susques, Jujuy, ~250 km NW van S.S. de Jujuy; "nearest port Antofagasta … 530 km"; RN9/RN52 verhard; gravelweg Route 70 ~1 km van de plant; Antofagasta en Mejillones "likely" havens; Ganfeng-offtake 80 %. https://www.sec.gov/Archives/edgar/data/1440972/000119312518012399/d478086dex995.htm
[2] Reporte Minero, 2025-03-31: Aduana Argentina laat Minera Exar rechtstreeks naar China exporteren via "puertos del norte de Chile"; eerste lading tien trucks in februari, containers; deel blijft via Buenos Aires; geen havennaam. https://www.reporteminero.cl/noticia/noticias/2025/03/productora-de-litio-argentina-obtiene-autorizacion-para-exportar-mineral-a-china
[3] Fundación Andrés Bello, 2025-04-02 (cit. Reporte Minero): zelfde bericht; 2024 > 25.000 t geproduceerd, 28.000 t geëxporteerd via Buenos Aires. https://www.fundacionandresbello.org/?p=12604
[4] Lithium Argentina, homepage: productiegrafiek "100 % basis" 2024 25k, 2025 34k (labels in de paginatekst door elkaar; als verwachting gelezen). https://lithium-argentina.com/
[5] Lithium Argentina, projectpagina Cauchari-Olaroz: Ganfeng 46,7 % / LAR 44,8 % / JEMSE 8,5 %; 40.000 tpa carbonaat; 80 % offtake. https://lithium-argentina.com/projects/cauchari-olaroz
[6] Wikipedia (en), Paso de Jama: grenspas 4.200 m, bereikt via Chileense Ruta 27 en Argentijnse RN52; vrachtverkeer naar de havens van Noord-Chili; Jama 23°14′S 67°01′W. https://en.wikipedia.org/wiki/Paso_de_Jama
[7] OSRM (OSM-afgeleid, indicatie, 2026-10-09): plant → via 1–7 → ATI 544,1 km; RN52 66,0 · Ruta 27 155,8 · Ruta 23 94,0 · Ruta 25 110,4 · Ruta 5 81,8 · Ruta 26 12,1 km; nearest-snaps van de via-punten 0–3 m. https://router.project-osrm.org
[8] Forbes Argentina / El Heraldo (2023-05; via zoeksamenvatting): Exar, 40.000 t/j, verharde wegen incl. verbinding met de haven van Antofagasta. https://www.forbesargentina.com/negocios/con-una-inversion-casi-mil-millones-dolares-comienza-producir-exportar-tercer-proyecto-litio-argentina-n34391
[9] Haalbaarheidstoets M31 golf 9 (bindend): aanpassing plant -23.6720,-66.7680, via-punten, kopie zeebeen.
[10] `v2/design/routebrieven/lithium-atacama-antofagasta.md` §3/§9 en `v2/data/stroomroute-lithium-atacama-antofagasta.json`: anker `li-antofagasta-kade`, aanloop 97,1 km, zee 18.914,3 km; via-punten Ruta 5/26.
[11] `v2/design/routebrieven/lithium-hombremuerto-bessemercity.md` [12]: zeeknoop 4664 (-23.80,-71.30) op 92,24 km van de kade; `lithium-olaroz-naraha.md` §9: RN52-klasse-les.
[12] `v2/design/lithium-sitelaag.json`, `w-li-cauchari-olaroz` (-23.7362,-66.7286, onzeker, salarcentroïde).
[13] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15, live, 2026-10-09): `v2/build-cache/satcheck/sat-lithium-cauchari-antofagasta-{plant-z15,plant-z14,kade-z15}.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)

**Stroom `lithium-cauchari-antofagasta`** → `v2/data/stroomroute-lithium-cauchari-antofagasta.json` (164,0 KB) — 3 benen, 19.556,8 km, 3 markers: truck 545,4 km · zee (stippel, haven-aanloop) 97,1 km · zee 18.914,3 km. Naden tussen alle benen 0,000 km.
Recept: `bak_stromen.sh` (functie `bak_lithium_cauchari_antofagasta`); wegprofiel `lithium-cauchari-antofagasta-plant-ati` in `maak_stroombeen_weg.py` (extracts `argentina` + `chili`, scan via `wegscan_puur.py`, 83 s).

Toelichting per been.
- **b1** (truck, profiel `lithium-cauchari-antofagasta-plant-ati`): plantweg (9,1 km `service`/`unclassified`) → RN52 → Paso de Jama → Ruta 27 → Ruta 23 → Ruta 25 → Ruta 5 Norte → Ruta 26. Per segment: plant→RN52 9,1 · →Jama 66,1 · →Ruta 23 224,3 · →Calama 32,4 · →Ruta 25/5 111,9 · →Baquedano 52,3 · →Ruta 5/26 31,5 · →ATI 17,4 km; alle via-snaps 0,00–0,01 km. Lengtetoets **544,8 km tegen de bedrijfsopgave 530 km = +2,8 % [OK]**; de OSRM-indicatie (544,1 km) valt er 0,1 % naast, maar is OSM-afgeleid en dus geen tweede bron. Getekende lijn 545,4 km. De 9 km plantweg was het bak-risico uit §7: met `corridorKlassen` (tertiary/unclassified/residential/service) en `eindKlassen` met `track` bestaat er een wegpad, dus **geen last-mile-stippel**. Anker-verbindingen: plant→weg 0,04 km; weg→kade **0,53 km (> 0,5 km, bevinding)**: de ATI-pier ligt niet op een gescande straat, de laatste 0,5 km is een recht stuk. De hoofdroute van dit carbonaat is Buenos Aires; dit been draagt alleen de Chileense pilot (§7).
- **b2a** (stippel, zee): haven-aanloop Antofagasta, 97,1 km, **LETTERLIJKE KOPIE** van `aanloop-antofagasta.geojson` (zelfde als `lithium-atacama-antofagasta`; kade 92,2 km van MARNET-zeeknoop 4664). Stippel = hier reikt MARNET niet; geen nieuwe aanloop-poging.
- **b2b** (zee): zeeknoop (-23,80, -71,30) → Yangtze-monding, 18.914,3 km, 83 MARNET-edges, 50°N-lane, **LETTERLIJK dezelfde bak-regel** als atacama. "aannemelijk: één bron" staat in de beennaam, niet in de lijnstijl. Hemelsbreed ≈ 18.560 km, dus +1,9 %.

**Markers** (3, alle uit §3): plant (0,0 km van de lijn) · ATI-kade (0,0 km) · Yangtze-monding (4,45 km van de lijn: de zee-snap van het gedeelde anker is 10,7 km, *anker ≠ routeerpunt*, identiek aan atacama).

**Toets.** `json.load` slaagt: versie 2, punt_formaat lonlat, modaliteiten {truck, zee}, elk been ≥ 46 punten, 164,0 KB. `toets_knikken.py`: truck 23 knikken ≥ 60° (vooral spikes op korte stukken), 4 omkeringen ≥ 150°, waarvan **1 terugloop** (172°, boogstraal 17 m op -23,60286/-70,26168): een overschiet-en-terug van ~0,17 km op de Ruta 5/26-aansluiting, 0,7 km vóór via 7 — knoopgeometrie van de afrit, niet gerepareerd (0,03 % van de km, geen via bijgeschoven); zee 0 knikken. `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de lijst.

**Open punten/bevindingen.**
- Haven niet bij naam bevestigd (Antofagasta uit ankerhergebruik, Mejillones blijft mogelijk); China-bestemming volgt uit eigenaar Ganfeng, geen converter of terminal gebrond.
- Plant-anker door afleiding gelegd; sitelaag-punt `w-li-cauchari-olaroz` (-23,7362/-66,7286) ligt **8,2 km** van het keten-anker en moet centraal gelijkgetrokken worden (niet door deze bake aangepast).
- Wegkilometer rust op één bedrijfsopgave (530 km, NI 43-101 2018).

**Gereedschapslessen:**
- De `RN52`-klasse-les van `lithium-olaroz-naraha` (§9) geldt ook aan de Chileense kant: een profiel met `corridorKlassen` ["tertiary","unclassified","residential","service"] en `eindKlassen` mét `track` gaf in één run 0 "geen wegpad"-fouten; de volledige keten Argentinië → Paso de Jama → Antofagasta (twee extracts) scant in 83 s met `wegscan_puur.py`.
- Via-punten die in de brief al met OSRM-nearest op 0–3 m van de weg waren gecontroleerd leverden alle snaps ≤ 0,01 km op; dat is de goedkoopste vorm van voorwerk (geen via-omwegen, geen bijschuiven).
- Een gedeeld zeebeen is een kopie van het `--stippel-geojson`/`--been`-paar uit de bestaande functie: de haven-aanloop en de MARNET-zeeknoop letterlijk overnemen kost geen aanloop-run en houdt de twee stromen op één lijn.
