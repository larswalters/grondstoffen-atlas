# Routebrief (licht) · lithium — Salar de Atacama → Salar del Carmen → Antofagasta (→ China)

**stroom-id:** `lithium-atacama-antofagasta` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** geconcentreerde lithiumchloride-oplossing (~6 % Li) uit SQM's verdampingsvijvers op de Salar de Atacama gaat per **tankwagen** ("cistern trucks") over Ruta B-385 (in OSM: Ruta B-39) naar Baquedano en over Ruta 5 naar de Planta Química de Litio Carmen bij Antofagasta, wordt daar tot batterijkwaliteit **lithiumcarbonaat** (210 kt/j) omgezet, gaat in big bags in **containers** per truck over Ruta 26 naar de ATI-kade van Puerto Antofagasta en per **containerschip** over de Stille Oceaan naar China — getekend tot de Yangtze-monding (aannemelijk: één bron, 72 % van de Chileense carbonaatexport).
**Welke as van het verhaal:** as 2 — Chileense pekel → carbonaat in containers naar China/Korea. Chili 56 kt Li-inhoud 2025 (≈ 298 kt LCE, 19 % van de wereld) [6]; SQM/Nova Andino Litio verkocht 233,1 kt LCE in 2025 (Q4 66,2 kt, record) [3]; Chili exporteerde jan–nov 2025 207,4 kt carbonaat waarvan 151,8 kt naar China (73 %) [5], december 18,3 kt waarvan 11,7 kt China en 5,6 kt Korea [4] → jaar ≈ 226 kt, China ≈ 164 kt (72 %). Eenheid ontwerp: kt LCE/j (carbonaat = LCE 1:1; oorspronkelijk: t Li2CO3 resp. t Li-inhoud × 5,323).

## 1 · Ketenkaart
```
SQM Salar de Atacama `li-atacama-laad` ──(b1 truck · LiCl-oplossing · B-39/B-385 → Baquedano → Ruta 5 · ~255 km)──► PQL Carmen `li-carmen-plant`
   ═══ knoop: LiCl → Li2CO3 210 kt/j (+ LiOH 40 kt/j) ═══
   ──(b2 truck · big bags in containers · Ruta 5 → Ruta 26 · ~20 km)──► Puerto Antofagasta, ATI `li-antofagasta-kade`
   ──(b3 zee · containerschip · Stille Oceaan · ~18.900 km, aannemelijk: één bron)──► Yangtze-monding `li-yangtze-monding` ⏹ stoppunt
   ├── vertakking (niet getekend): Albemarle Salar de Atacama → La Negra (27 km ZO van Antofagasta, > 85 kt/j) [8]
   ├── vertakking (niet getekend): Mejillones (80 km N van Carmen) en Iquique als alternatieve uitvoerhavens [1][2]
   └── vertakking (niet getekend): Zuid-Korea (2e afnemer, dec 2025 5,6 kt) en Japan [4]
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (tankwagens, LiCl-oplossing ~6 % Li; géén pijpleiding — v1 `pipeline` is fout) | `li-atacama-laad` → `li-carmen-plant` | plantweg (OSM `service`, compacted) → Ruta B-39 (TRS: B-385 "Baquedano–Salar"; tertiary, chipseal/asfalt) → Baquedano → Ruta 5 Norte zuidwest | ~255 [1] ("approximately 255 km from the Salar de Atacama"; Antofagasta–salar via B-385 272 km); via-keten 211 hemelsbreed | maak_stroombeen_weg, extract chili, `corridorKlassen: ["tertiary","unclassified"]`, refs B-39 + 5 | nee; alleen de plantweg (10–16 km `service`) kan buiten de 12 km-eindzone vallen → dan korte stippel "plantweg (geen net op deze korrel)" |
| b2 | C | truck (carbonaat in big bags, 20'-containers) | `li-carmen-plant` → `li-antofagasta-kade` | Ruta 5 noord (3 km) → Ruta 26 / Av. Salvador Allende → havenpoort | 15–20 [1][2] ("ports of Antofagasta (15 km west of the Salar del Carmen)"; plant "20 km east of Antofagasta"); via-keten 19 | maak_stroombeen_weg, extract chili (tweede profiel) | nee |
| b3 | B | zee (containerschip) | `li-antofagasta-kade` → `li-yangtze-monding` | Stille Oceaan; MARNET kiest de 50°N-lane (atlas-maat Antofagasta→Shanghai 18.915) | ~18.900; hemelsbreed 18.560 | letterlijke kopie `aanloop-antofagasta.geojson` (97 km, stippel) + MARNET zeeknoop 4664 -23.80,-71.30 → Yangtze-monding | aanloop: ja (bestaand bestand); *aannemelijk: één bron* in de beennaam |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-atacama-laad` | laadplek (LiCl-oplossing → tankwagens) | SQM Salar de Atacama, lithiumplant aan de zuidrand van het vijverveld | -23.5675, -68.4000 | [1][7][11] OSM-landuse "SQM Salar de Atacama" -23.5406,-68.3913 | bron-gelegd (z15 gezien: rij procesgebouwen en tanks aan de zuidrand van het pondsysteem, direct onder de bruin-gele concentraatvijvers; de plantweg vertrekt op de ZW-hoek; de tankwagen-laadplaats zelf is niet apart te onderscheiden — site-niveau) |
| `li-carmen-plant` | verwerkingsknoop (LiCl → Li2CO3/LiOH) | SQM Planta Química de Litio Carmen, Ruta 5 km ~1374 | -23.6335, -70.2600 | [1][2][9][11] | bron-gelegd (z15 gezien: fabriekscomplex direct ten oosten van Ruta 5 — hallen, tanks, silo's — met een veld groen-witte vijvers ten zuiden; es.wikipedia's coördinaat -23.6469,-70.2817 is de salar zelf, 2 km west) |
| `li-antofagasta-kade` | overslag truck → zee (containers) | Puerto Antofagasta, frente 2 / ATI (445 m kade, 12,2 m, 4 MHC, 120.000 TEU) | -23.6500, -70.4088 | [10][13] = bestaand `cu-antofagasta-kade` | bron-gelegd (hergebruik; z16 `sat-antofagasta-kade.png`: molo met schip aan de binnenzijde, containerstapels op de landzijde van frente 2 — welk sitio de lithiumcontainers laadt is open) |
| `li-yangtze-monding` | aanlanding China (zeeknoop) | Yangtze-monding (bestaand anker) | 31.42704, 121.47618 | [4][5] + koper-chuquicamata-china.md | aannemelijk (bestemming China 72 %; geen fabriek, geen containerterminal aangewezen) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | plantweg, zuidpoort SQM-complex (einde OSM way 169735104) | -23.5700, -68.4060 | de tankwagens verlaten het terrein aan de zuidkant, niet via B-355 (Toconao) noordwaarts |
| b1 | 2 | Ruta B-39 na de samenkomst van de twee plantwegen (way 28358078) | -23.6669, -68.5939 | pint B-39 westwaarts; welke van de twee `service`-linkwegen (recht zuid 10,9 km of diagonaal 16 km) SQM rijdt is open — de router kiest |
| b1 | 3 | Ruta B-39, knoop bij km ~64 (ways 363390368/28358078) | -23.5471, -68.8387 | pint B-39 tegenover de parallelle tracks (959774757, 1269262632) |
| b1 | 4 | Ruta B-39, bocht naar NW (way 363390368 westeind) | -23.4941, -69.4078 | B-39 door naar Baquedano i.p.v. tracks noord naar Ruta 25/Sierra Gorda |
| b1 | 5 | Ruta B-39 vlak vóór Baquedano (way 244605849 west) | -23.3409, -69.7926 | aansluiting op Ruta 5 bij Baquedano — zuidwest, niet B-330 noord |
| b1 | 6 | Ruta 5 Norte ZW van Baquedano (way 3,47 km) | -23.4488, -70.0523 | Ruta 5 richting Carmen/Antofagasta, niet B-400 of Ruta 25 |
| b2 | 1 | kruising Ruta 5 / Ruta 26 (way 13 punten, oosteind) | -23.6047, -70.2685 | Ruta 26 naar Antofagasta i.p.v. Ruta 5 → Ruta 28 via La Negra (langer) |
| b2 | 2 | Ruta 26 op de Cuesta | -23.6253, -70.3438 | pint de Ruta 26-corridor |
| b2 | 3 | Av. Salvador Allende (Ruta 26 in de stad) | -23.6287, -70.3960 | stadsinrit naar de haven vanaf het NO |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Salar de Atacama, verdampingsvijvers + lithiumplant | SQM / Nova Andino Litio (Codelco-partnerschap 2025) | pekel (pomp, ≤ 1.600 L/s) → LiCl-oplossing ~6 % Li, per pomp en HDPE-leiding in tankwagens | lithiumsulfaat 45 kt/j nominaal; LiCl-tonnage niet gepubliceerd | [1][7] |
| Planta Química de Litio Carmen, Ruta 5 bij Antofagasta | SQM / Nova Andino Litio | LiCl-oplossing → Li2CO3 (batterij/technisch) en LiOH; big bags → containers | Li2CO3 210 kt/j (eind 2025) → 240 kt/j (2028); LiOH 40 kt/j → 100 kt/j (eind 2026) | [2] |
| Puerto Antofagasta / ATI | EPA / ATI (Hanseatic Global Terminals) | containers en break-bulk; "port of exit for … lithium in its various formats" | 120.000 TEU/j | [10] |

## 6 · Stoppunt
De brief stopt op de Yangtze-monding: China neemt 72 % van het Chileense carbonaat, maar geen bron noemt de Chinese fabriek of haven waar SQM-carbonaat wordt gelost — fase D/E vervallen en de lijn eindigt waar het bewijs eindigt.

## 7 · Open punten
- **B-385 ≠ OSM:** de Chili-extract kent 0 ways met ref B-385; de weg Baquedano–salar staat als **Ruta B-39** (tertiary, chipseal/asfalt) [11]. De M25-fout "geen wegpad" komt daarvandaan → `corridorKlassen` tertiary verplicht.
- **Plantweg SQM → B-39:** twee `service`-wegen (compacted, 10,9 en 16 km); welke SQM rijdt is niet gebrond; ze liggen deels buiten de 12 km-eindzone → mogelijk een korte stippel.
- **Tankwagen-laadplaats** binnen het SQM-complex niet onderscheiden (site-anker). **ATI-sitio** voor lithiumcontainers onbekend.
- **Chinese bestemming:** havens/fabrieken niet per lading gedocumenteerd; Yangtze-monding is een vaarweg-anker, geen containerterminal. Korea (2e afnemer) en Japan niet getekend.
- **Alternatieve havens** Mejillones/Iquique en de Albemarle-spiegelketen naar La Negra niet getekend (vertakkingen §1).
- **Volume per been:** LiCl-tonnage op b1 niet gepubliceerd (≈ 210 kt Li2CO3 ⇒ ~39 kt Li-inhoud); b2/b3 dragen SQM's carbonaat, jaar 2025: Chili-totaal ≈ 226 kt, waarvan SQM het grootste deel (niet uitgesplitst).

## 8 · Bronnen
[1] SQM, Technical Report Summary Salar de Atacama (SEC 20-F FY2023, ex. 96-1, 2024): "transported via cistern trucks to the Salar del Carmen"; "via route B-385"; "Route B-385 which connects Baquedano to the Salar de Atacama"; "connects to the Route 5 highway"; 255 km / 272 km; "20 km east of the city of Antofagasta"; "packed in large bags and later consolidated in containers … ports of Antofagasta (15 km west …), Mejillones (80 km north …)"; capaciteit 195 kt / 26 kt (2023). https://www.sec.gov/Archives/edgar/data/909037/000110465924044246/tm2410667d1_ex96-1.htm
[2] SQM, Form 20-F FY2025: carbonaatcapaciteit 210 kt/j (eind 2025), hydroxide 40 kt/j; doel 240 kt (2028) en 100 kt LiOH (eind 2026); "shipped in containers or break-bulk … Antofagasta, Tocopilla, Mejillones and Iquique"; Salar 210 km O van Antofagasta, B-385. https://www.sec.gov/Archives/edgar/data/0000909037/000090903726000023/sqm-20251231.htm
[3] SQM, 6-K 4Q2025 earnings release (2026-03): Nova Andino Litio verkoop 2025 233,1 kt, Q4 66,2 kt; 2026 > +10 %. https://www.sec.gov/Archives/edgar/data/909037/000090903726000012/a6-k_4q2025earningsrelease.htm
[4] SMM, Chileense douane december 2025: 18.341 t carbonaat, China 11.705, Zuid-Korea 5.572, Japan 596. https://news.metal.com/newscontent/103716528
[5] SMM, Chileense douane november 2025: jan–nov 207,4 kt, China 151,8 kt. https://news.metal.com/newscontent/103656230-chiles-lithium-exports-in-nov-2025-carbonate-down-sulfate-up
[6] USGS, Mineral Commodity Summaries 2026 — Lithium: Chili 56.000 t Li (2025), wereld 290.000 t. https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-lithium.pdf
[7] IHEAL (OpenEdition), over de Salar de Atacama: pekel "concentrada con un 6 % de litio … conducida por bombas y tuberías HDP a camiones aljibes". https://books.openedition.org/iheal/10362?lang=en
[8] Albemarle, La Negra: "27 kilometers southeast of Antofagasta", > 85.000 t batterijkwaliteit/j. https://www.albemarle.com/cl/en/what-we-offer/reliable-supply/la-negra
[9] es.wikipedia, Salar del Carmen: 23°38′49″S 70°16′54″W, 30 km per spoor O van de haven, "SQM Salar del Carmen" lithiumplant. https://es.wikipedia.org/wiki/Salar_del_Carmen
[10] Hanseatic Global Terminals, ATI: kade 445 m / 12,2 m, 4 MHC, 120.000 TEU, "port of exit for minerals (copper and lithium in its various formats)". https://latinamerica.hanseaticglobalterminals.com/business-area-section/port-terminals/ati/
[11] OpenStreetMap (ODbL), Geofabrik-extract `chili` (2026-09 scan met pyosmium): Ruta B-39 tertiary ways 244605849 · 1301418714 · 1322735813 · 363390368 · 28358078 · 871608988; plantwegen `service` 169735104 · 871603551 · 169735105; Ruta 5 motorway; Ruta 26 trunk; 0 ways met ref B-385; Nominatim: landuse "SQM Salar de Atacama" -23.5406,-68.3913; ATI -23.6540,-70.4034. https://www.openstreetmap.org
[12] Esri World Imagery via `v2/tools/sat_check.py` (z13–z15, live): `v2/build-cache/satcheck/sat-lithium-atacama-antofagasta-{sqm-salar-z14,sqm-liplant-z15,salar-uitrit-z13,carmen-z13,carmen-z14,carmen-z15}.png`; kade: `sat-antofagasta-kade.png` (z16, 2026-09-24).
[13] `v2/design/routebrieven/koper-aurubis-hamburg.md` §3/§9 — anker `cu-antofagasta-kade` -23.6500,-70.4088 en `v2/build-cache/ais/graaf/aanloop-antofagasta.geojson` (97,1 km, zeeknoop -23.80,-71.30).
[14] `v2/tools/fetch_landnet.py`, corridor `li-atacama-lanegra` (M25, Albemarle): refs B-39/5, gepubliceerdKm 260, via's Baquedano -23.3291,-69.8336 en Ruta 5 -23.4463,-70.0385.

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `lithium-atacama-antofagasta`** → `v2/data/stroomroute-lithium-atacama-antofagasta.json` — 4 benen. 19.274,2 km. 4 markers: truck 262,8 km · zee (stippel) 97,1 km · zee 18.914,3 km.
Recept: `bak_stromen.sh` (functie `bak_lithium_atacama_antofagasta`). Toelichting: twee wegscans over de `chili`-extract (profielen `lithium-atacama-carmen` en `lithium-carmen-antofagasta` in `maak_stroombeen_weg.py`, `--bron geofabrik`). Been b1 (SQM Salar de Atacama → PQL Carmen) bevestigt §7 van de brief: 0 ways met ref B-385 op de extract, de weg heet er **Ruta B-39** (tertiary) — zonder `corridorKlassen: ["tertiary","unclassified"]` geeft de scan "geen wegpad", precies de bekende M25-fout. Uitkomst 232,4 km weggeometrie tegen ~255 gepubliceerd (**−8,9%**, binnen ±15%); de compacted plantweg tussen het SQM-anker en de zuidpoort is 7,61 km — buiten de standaard-eindzone, dus die aanloop staat als apart, doorgetrokken stuk (geen stippel: de weg ís gescand, alleen de 12 km-drempel snijdt de aparte rapportage af). Been b2 (PQL Carmen → ATI-kade) komt op 21,9 km tegen ~19 gepubliceerd (**+15,4%, net buiten de ±15%-norm — bevinding, niet dichtgetrokken**: de 19 km in de brief is zelf al een afgeleide via-keten, geen citaat). Zeebeen: de kade ligt 97 km van de dichtstbijzijnde MARNET-zeeknoop → letterlijke kopie van de bestaande haven-aanloop `aanloop-antofagasta.geojson` (gedeeld met `koper-aurubis-hamburg`, zelfde kade `cu-antofagasta-kade` = `li-antofagasta-kade`), gevolgd door het MARNET-zeebeen vanaf zeeknoop −23,80/−71,30 naar de bestaande Yangtze-monding-marker: **18.914,3 km**, nagenoeg gelijk aan de brief-schatting (~18.900, atlas-maat Antofagasta→Shanghai 18.915). Toets: `toets_knikken.py` geeft 0 omkeringen/0 terugloop over alle vier de benen (10 knikken ≥60°, allemaal spikes/krappe bochten op de weg-geometrie, geen enkele ≥150°); `toets_rechte_benen.py --min-km 5` vindt geen been van deze stroom (geen ongeteste rechte lijn); naden tussen opeenvolgende benen 0,00 km; json geldig (versie 2, punt_formaat lonlat, alle modaliteiten in {truck, zee}, 96,0 KB).

**Gereedschapslessen:**
- B-385 bestaat niet in OSM (0 ways op de `chili`-extract); de corridor heet er Ruta B-39 en vraagt `corridorKlassen: ["tertiary","unclassified"]` om niet op "geen wegpad" te stranden.
- Een compacted plantweg die verder van het anker ligt dan de standaard-eindzone (12 km) hoeft geen stippel te worden: de scan vindt hem gewoon zolang het eerste via-punt dichter bij de weg staat dan het anker zelf (hier 7,61 km) — het blijft wel een aparte, apart gerapporteerde aanloop en geen onderdeel van de lengtetoets.
- Twee onafhankelijke schattingen in dezelfde brief kunnen elkaar tegenspreken zonder dat er een meetfout is: de brief geeft voor been b2 zowel "15 km" (bron, hemelsbreed-achtig) als "19 km" (eigen via-keten) — de gemeten weggeometrie (21,9 km) ligt tussen beide in en net buiten de ±15%-marge op de laagste van de twee.
