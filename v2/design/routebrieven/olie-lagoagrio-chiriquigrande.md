# Routebrief (licht) · olie — Lago Agrio (Ecuador) → Balao → Charco Azul (Panama)

**stroom-id:** `olie-lagoagrio-chiriquigrande` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken (2026-10-29)
**Keten in één zin:** Ecuadoraanse ruwe olie per **leiding** (SOTE, 497,7 km over de Andes) van het Lago Agrio-station naar het Balao-terminal bij Esmeraldas, per **tanker** (aannemelijk: één bron) langs de Pacifische kust naar de PTP-terminal Charco Azul (Panama, Pacifische kant).
**Welke as van het verhaal:** *de Ecuador-Andes-leiding en de sprong naar Panama* — SOTE-capaciteit 360 kb/d [1]; productie Ecuador 2025 gem. 468 kb/d, waarvan Petroecuador 373 kb/d [5]; Panama noemt het BCE als 40% van de exportbestemmingen (periode onbekend) [5]. Aandeel Panama op SOTE-olie is eigen rekensom, ~140 kb/d (aanname: 40% van 360 kb/d), geen bron.
**⚠️ Eindpunt wijkt af van het id (ontwerp: Chiriquí Grande):** de leiding Charco Azul → Chiriquí Grande (PTP, 135 km OSM) wordt **niet getekend**: PTP stroomt sinds de ombouw 2008/09 van de Atlantische naar de Pacifische kant [2][3][4][8]; Ecuadoraanse olie over de landengte is alleen voor 2003 gedocumenteerd [2][7]. Zie §6, §7.

## 1 · Ketenkaart
```
Lago Agrio-station `ol-lagoagrio` ──(b1 leiding · SOTE via Baeza, Papallacta, Quito-zuid, Santo Domingo,
   Quininde · OSM-stitch 501,4 km, gepubliceerd 497,7 km)──► leidingeind Balao ──(b2 stippel 1,6 km)──►
Balao-kust `ol-balao-kust` ──(b3 stippel haven-aanloop 73,3 km)──► zeeknoop 346 ──(b4 zee · MARNET 1.103 km)──►
zeeknoop 8933 ──(b5 stippel aanloop 96,5 km via 8,0000/-82,7000)──► Charco Azul Muelle 1 `ol-charcoazul-muelle` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Lago Agrio-station → leidingeind Balao | SOTE (Sistema Oleoducto Trans-Ecuatoriano), Baeza-Papallacta-Quito-Santo Domingo-Esmeraldas | 497,7 [1]; eigen stitch 501,4 (+0,7%), naden 0,2-1,8 km, totaal 4,9 | `maak_leidingbeen_olie_lagoagrio_chiriquigrande.py` (152 OSM-ways) | nee (naden < 2 km) |
| b2 | A | leiding | leidingeind Balao → Balao-kust | SPM/laadleiding, niet in OSM | 1,6 (hemelsbreed, geen wegkm) | `--stippel` | ja: reikt het net niet |
| b3 | B | zee | Balao-kust → zeeknoop 346 (1,2000/-80,3000) | haven-aanloop | 73,3 | `--stippel` (aanloop liep eerder 2x in time-out) | ja: MARNET reikt niet (kade 73,3 km van knoop) |
| b4 | B | zee | zeeknoop 346 → zeeknoop 8933 (7,4167/-82,8000) | Pacifische kust Colombia-Panama, geen kanaal | 1.103 MARNET; hemelsbreed kade-kade 879, geen routekm | MARNET | nee |
| b5 | B | zee | zeeknoop 8933 → Charco Azul Muelle 1 | haven-aanloop via 8,0000/-82,7000 (0 km land; recht 7,1 km land) | 96,5 (65,8 + 30,7) | `--stippel` x2 | ja: MARNET reikt niet (kade 89,2 km) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-lagoagrio` | kop leiding / station | Petroecuador-station Lago Agrio (SOTE-begin) | 0.0781, -76.8770 | [1][9][12] | bron-gelegd (z15: stationscomplex aan de oostrand van Nueva Loja; twee groepen witte ronde tanks 0,4 en 0,8 km van het punt, vliegveld 2 km NO) |
| `ol-balao-kust` | overslag leiding → zee (kustpunt Terminal Petrolero de Balao) | OSM-haven-node Terminal Petrolero de Balao | 0.9842, -79.6770 | [11] | bron-gelegd (z15: weg uit het installatieterrein eindigt hier op het strand bij een kleine constructie; SPM zelf niet zichtbaar) |
| `ol-balao-eind` | routeerpunt, geen marker | einde SOTE-way (installatieterrein bij de kust) | 0.9701, -79.6795 | [1][9] | bron-gelegd (z15: terrein met gebouwen/platte daken, 1,6 km ZZW van de kust; groot tankenpark Balao 1,6 km ZW) |
| `ol-charcoazul-muelle` | losplek, stoppunt | PTP Charco Azul, steiger met tanker (ontwerp: Muelle 1, nummer niet in bron) | 8.2154, -82.8749 | [2][3] | bron-gelegd (z15: lange steiger vanaf de kust, VLCC-achtige tanker aan de kop; tweede steiger 0,5 km zuidelijker) |
| (geen marker) | opslag | Charco Azul-tankpark | 8.1981, -82.8765 | [2] | bron-gelegd (z15: vijf witte tanks, kleinere tanks 0,6 km N); ligt 2 km van de steiger, niet op een been |

## 4 · Via-punten
Geen routering: b1 is een OSM-stitch, b4 loopt over de router. Controlepunten op de gestikte leiding (km vanaf Lago Agrio): km 25 (0.0875,-77.0449) · km 100 (-0.1020,-77.5905) · Baeza 0,6 km ernaast op km 162 · km 175 (-0.4295,-77.9884) · Papallacta 1,6 km op km 196 · Quito (centrum) 7,1 km ten noorden op km 245 (leiding passeert Quito-zuid/Cayagama) · km 300 (-0.2902,-78.8532) · Santo Domingo 3,0 km op km 342 · Quininde 0,0 km op km 418 · einde km 501 (0.9701,-79.6795). Stippel b5: via-punt 8.0000,-82.7000 (open water, Golf van Chiriquí; verbindt zeeknoop 8933 met de steiger zonder land te snijden).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Lago Agrio-station | Petroecuador | veldolie Oriente → SOTE | SOTE 360 kb/d | [1] |
| Balao-terminal (+ Esmeraldas-raffinaderij) | Petroecuador | SOTE → tankers (geen VLCC) / raffinaderij | niet gebrond | [1][6] |
| Charco Azul (PTP, Pacifische kant) | Petroterminal de Panamá | tanker → opslag | 3 supertankersteigers, 3 tanks 2,5 Mbbl (Wikipedia) | [2][3] |

## 6 · Stoppunt
De brief stopt aan de steiger van Charco Azul: de enige gedocumenteerde Panama-bestemming van Pacifische olie met opslag en tanker-steigers is PTP, maar geen bron toont Ecuadoraanse olie die de landengte nog oversteekt (PTP stroomt oost → west), dus fase C naar Chiriquí Grande vervalt; fase D/E vervallen.

## 7 · Open punten
- **Fase C niet getekend, wel klaar:** OSM-stitch PTP steiger Charco Azul → Chiriquí Grande, 133,4 km (130 gepubliceerd, +2,6%), 32 ways, geen naden; reserve-geojson `olie-lagoagrio-chiriquigrande-leiding-ptp-reserve.geojson`. Tekenen kan zodra een bron Ecuador-olie (Pacific → Atlantic) na 2009 toont; PTP-boeien 8.9687,-82.108 niet tekenen.
- **Panama = één bron:** BCE noemt 40% Panama, maar als distributiehub herverdeeld naar Azië/Europa [5]; geen bron noemt Charco Azul als ontvangsthaven. Periode van het cijfer onbekend.
- **Balao-SPM niet gevonden** (niet in OSM, niet op z15); Balao kan geen VLCC laden, OCP Punta Gorda (privé) wel en SOTE kreeg een uitbreiding Balao → Punta Gorda [6]; Punta Gorda-anker niet gelegd.
- **b1: ~15% van de stitch (74 km) heeft geen naam én geen operator** en kan OCP zijn (parallelle corridor); Poliducto-, Pesados- en OCP-ways zijn uitgesloten. Q3 2025 stonden SOTE/OCP stil door erosie van de Coca-rivier (ontwerp, niet nagetrokken).
- **b4-knik:** MARNET-net is hier schaars (knopen 346 → 5159 → 5179 → 5172 → 5171 → 5170 → 267 → 8933); zigzag bij 6,4092/-82,6753 en 6,9000/-81,4000 (130-138 gr, 0 omkeringen ≥ 150 gr), 1.103 km tegen 745 km grootcirkel tussen de knopen. Alternatief: zee stoppen op knoop 5170 (6.4090,-82.6750, 787 km) + stippel naar 8,0000/-82,7000 (177 km) = totaal ~995 km.
- Aanloop Balao snijdt 0,5 km land (1:10M-korrel, onvermijdelijk); jaarvolume voor b3/b4 niet gebrond.

## 8 · Bronnen
[1] Wikipedia (es), Oleoducto Transecuatoriano — 497,7 km, 360 kb/d, Lago Agrio → Balao/Esmeraldas, 1972. https://es.wikipedia.org/wiki/Oleoducto_Transecuatoriano
[2] Wikipedia (en), Trans-Panama pipeline — 130 km, 860 kb/d, Charco Azul 3 steigers + 3 tanks 2,5 Mbbl, heropend 2003 voor Ecuadoraanse olie, ombouw 2008/09. https://en.wikipedia.org/wiki/Trans-Panama_pipeline
[3] Petroterminal de Panamá — 130 km, stroomrichting Atlantisch → Pacifisch, Pacifische terminal ten zuiden van Puerto Armuelles. https://petroterminal.com/en/home-en/?lang=en
[4] GEM.wiki, Trans-Panama Pipeline — 131 km, 860 kb/d, omgekeerd 2008-2009. https://www.gem.wiki/Trans-Panama_pipeline
[5] eldiario.ec, 4-4-2025 — BCE: Panama 40% van de bestemmingen (hub), productie 2025 468 kb/d. https://www.eldiario.ec/zona-2/como-estan-las-exportaciones-de-petroleo-de-ecuador-en-2025-04042025/
[6] Pipeline & Gas Journal, 29-6-2021 — Balao kan geen VLCC; Punta Gorda (OCP) wel; SOTE-uitbreiding. https://pgjonline.com/news/2021/june/eyeing-asian-market-ecuador-begins-crude-exports-in-larger-vessels
[7] Energy Intelligence, 5-10-2003 — Napo via de trans-Panama-leiding; EnCana/Taurus-deal. https://www.energyintel.com/0000017b-a7a1-de4c-a17b-e7e3ffba0000
[8] OGJ — BP begint oost-west-transport door Panama (ombouw). https://www.ogj.com/pipelines-transportation/pipelines/article/17275345/bp-begins-east-west-crude-pipeline-shipments-across-panama
[9] OpenStreetMap-bijdragers (ODbL), Geofabrik-extracts ecuador en panama — `man_made=pipeline`, `substance=oil` (eigen stitch). https://download.geofabrik.de/south-america/ecuador.html
[10] MARNET (`v2/build-cache/marnet-preais`), `hecht_marnet.py route` droogloop 2026-10-29: knoop-knoop 1.103,1 km, totaal 1.775,9 km.
[11] OSM node 775626990 "Terminal Petrolero de Balao" (0.9842,-79.6770). https://www.openstreetmap.org/node/775626990
[12] Wikipedia (en), Lago Agrio (Nueva Loja) 0.0847,-76.8828. https://en.wikipedia.org/wiki/Lago_Agrio
[13] Esri World Imagery via `sat_check.py` z14-z15: `sat-olie-lagoagrio-chiriquigrande-{lagoagrio,balao,balao-breed,charcoazul-tank,charcoazul-muelle,chiriquigrande}.png`.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
`bash v2/tools/bak_stromen.sh olie-lagoagrio-chiriquigrande` (functie `bak_olie_lagoagrio_chiriquigrande`) → `v2/data/stroomroute-olie-lagoagrio-chiriquigrande.json`, 101,8 KB, contract versie 2, 6 benen, 5.017 punten, 3 markers, totaal 1.775,9 km (= droogloop).

| # | modaliteit | km | geometrie | stippel |
|---|---|---|---|---|
| b1 | leiding | 501,4 (gepubliceerd 497,7, +0,7%) | OSM-stitch SOTE, vooraf gebakken geojson | nee |
| b2 | leiding | 1,6 (hemelsbreed, geen wegkm) | SPM-laadleiding Balao | ja: niet in OSM |
| b3 | zee | 73,3 | haven-aanloop Balao, rechte lijn | ja: MARNET reikt niet |
| b4 | zee | 1.103,1 | MARNET zeeknoop 346 → 8933, 115 punten | nee |
| b5 | zee | 65,8 | aanloop Charco Azul deel 1 via 8,0000/-82,7000 | ja: MARNET reikt niet |
| b6 | zee | 30,7 | aanloop Charco Azul deel 2 naar de PTP-steiger | ja: MARNET reikt niet |

**Recept:** b1 `--been-geojson` leiding (bestaand FeatureCollection `olie-lagoagrio-chiriquigrande-leiding-lagoagrio-balao.geojson`); b2, b3, b5, b6 `--stippel`; b4 `--been` zee 1.2000,-80.3000 → 7.4167,-82.8000. Markers ol-lagoagrio, ol-balao-kust, ol-charcoazul-muelle. Geen wegbeen, geen profiel in `maak_stroombeen_weg.py`, geen slotgebruik behalve zwaar-slot voor de bake.

**Toets:** naden alle <= 0,001 km (geen naad > 5 km); markers 0,000-0,001 km van de lijn; b1 binnen +0,7% van de gepubliceerde 497,7 km; `toets_knikken`: b4 4 knikken, 0 omkeringen, 0 terugloop; b1 een spike van 37 m straal bij -0.28696,-78.62663 (Quito-zuid, OSM-stitch); `toets_rechte_benen`: alleen de drie zee-aanlopen (omwegfactor 1,000, alle stippel met reden).
**Toelichting stippel:** b2 SPM niet in OSM; b3 kade 73,3 km van zeeknoop 346 (maak_havenaanloop liep eerder 2x in time-out, dus recht); b5/b6 kade 89,2 km van zeeknoop 8933, via open water zonder land. **Aanloop Balao** snijdt ~0,5 km land (1:10M-korrel).
**Eindpunt wijkt af van het id:** de lijn eindigt bij Charco Azul (Pacifische PTP-kant), niet in Chiriquí Grande; fase C niet getekend (reserve-geojson klaar, 133,4 km).
**Lessen:** (1) b4 is een zigzag-route door een schaars MARNET-net (1.103 km tegen 879 km hemelsbreed); knikken bij 6.90000,-81.40000 (138 gr) en 6.40920,-82.67530 (130 gr). Het alternatief (zee stoppen op knoop 5170 + stippel naar 8,0/-82,7, ~995 km) is niet gekozen. (2) Panama als bestemming is een aannemelijke, niet-gebronde schakel: in de beennaam, niet in de lijnstijl.
