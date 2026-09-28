# Routebrief (licht) · zilver — Antamina → Huarmey (land)

**stroom-id:** `zilver-antamina-huarmey` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** koper-zink-concentraat (met zilver als bijproduct) van de Yanacancha-concentrator van
Compañía Minera Antamina (BHP/Glencore/Teck/Mitsubishi JV, San Marcos, Áncash, ~3.155 m) via een **eigen
begraven mineroducto van 302 km** (60% vast/40% water, max. hoogte 4.669 m, daling 3.140 m, ~34 u, ~300 m³/u)
naar Puerto Punta Lobitos (Huarmey), waar het concentraat gefilterd (65% → 9,5% vocht) en per zeeschip
verscheept wordt — **stoppunt**, geen gedocumenteerde smelterbestemming binnen budget gevonden.
**Welke as:** *het unieke pijpleiding-gereedschap van deze atlas* — Antamina is de enige stroom die zijn hele
land-been via een eigen mineraalpijpleiding aflegt i.p.v. weg/spoor. Jaarvolume: Antamina produceerde
410.000 t koperconcentraat in 2024 (15% van Peru's koperproductie) [1]; zilver reist mee met het concentraat,
geen aparte jaaropgave gevonden binnen budget — v1-schatting **~520 t Ag/j** (2,0% wereldaandeel) aangehouden
als indicatie [10].

## 1 · Ketenkaart
```
Yanacancha-concentrator `ag-antamina-concentrator` ──(b1 leiding · mineroducto Antamina-Huarmey ·
   ~302 km, stippel)──► Puerto Punta Lobitos `ag-huarmey-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding (slurry, 60% vast) | Yanacancha-concentrator → Puerto Punta Lobitos | mineroducto Antamina-Huarmey (geopend 01-07-2001), via Aquia/Cajacay (Bolognesi) en Cochapeti/Huayan (Huarmey) | 302–304 [1][2][3][4] | stippel "leiding" via 4 via-punten (§4); OSM Overpass onbereikbaar binnen budget (§7) | ja — leiding niet gekarteerd (verwacht); via-punten geven een schematische, geen gemeten corridor |

## 3 · Ankers
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-antamina-concentrator` | mijn/concentrator (kop van de leiding) | Yanacancha-concentrator, Compañía Minera Antamina, San Marcos, Huari | -9.5615, -77.0400 | [2][3][7][8] | bron-gelegd (z15 gezien: verwerkingscomplex met gebouwen, tanks en wegennet, ~600 m NW van het arbeidscamp Yanacancha en de relaves-dam) |
| `ag-huarmey-kade` | overslag leiding → zee (ontwatering/filtratie + laadsteiger) | Puerto Punta Lobitos, Huarmey | -10.1035, -78.1788 | [2][3][7][8] | bron-gelegd (z15 gezien: pier met zeeschip langszij, gebouwencluster en sportveld op het schiereiland, golfbreker) |

## 4 · Via-punten (b1 — de leiding heeft geen net)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Aquia (Bolognesi) | -10.0745, -77.1447 | gemeenschap die expliciet genoemd wordt als liggend op de corridor van het mineroducto (paro-berichtgeving) [5] |
| b1 | 2 | Cajacay / Santa Rosa (Bolognesi, Fortaleza-vallei) | -10.1747, -77.3355 | Bolognesi-gemeenschap op de corridor, aan de Carretera Pativilca–Huaraz (km 107) die de "ruta sur" van de leiding volgt [6] |
| b1 | 3 | Cochapeti (Huarmey) | -9.9801, -77.6958 | eerste Huarmey-provincie-nederzetting lager in de vallei, op de overgang naar de kuststrook |
| b1 | 4 | Huayan (Huarmey, aan de Carretera Huarmey–Recuay) | -9.9079, -77.7933 | laatste vallei-nederzetting vóór de kust, op de doorgaande weg Huarmey–Recuay die de leidingcorridor kruist |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Puerto Punta Lobitos — ontwatering/filtratie | Compañía Minera Antamina | slurry 60% vast (via leiding) → concentraat 90,5% vast (9,5% vocht) | mineroducto 1,4 Mt/j; ~300 m³/u, ~34 u transporttijd, 3.140 m hoogteverval | [2][3] |

## 6 · Stoppunt
De brief stopt bij Puerto Punta Lobitos: geen bron noemt binnen budget een specifieke smelterbestemming voor
het concentraat na de kade — fase B (zee) en verder vervallen bewust; fase D/E zijn niet van toepassing.

## 7 · Open punten
- **Leiding niet gekarteerd in OSM.** Overpass (zowel overpass-api.de als de kumi-mirror) was binnen het
  websearch/tool-budget van deze sessie niet bereikbaar (timeout/406) → niet bevestigd of `man_made=pipeline`
  ontbreekt of alleen onbereikbaar was. Bij het bakken dus eerst een eigen Overpass-poging, anders stippel
  "leiding (schematisch — geen OSM-way)".
- **Via-punten zijn bekende gemeenschappen op/nabij de corridor (RPP/Antamina-nieuwspagina's), geen gemeten
  tracé** — de leiding volgt zelf een bergroute met vier klepstations (VS-1..4 op km 125/143/162/177,
  hoogste punt 4.669 m) [2] die niet 1-op-1 op deze dorpen valt. Een hemelsbrede meting via deze 4 punten kan
  dus flink afwijken van de gepubliceerde 302 km — rapporteren bij het bakken, geen harde ±15%-eis hier.
  Onduidelijk uit de bronnen: passeren b1's `via`-punten ook Chavín de Huántar (uit één bron als "getroffen
  gemeenschap" genoemd, maar zuidelijker en buiten de rechte corridor Yanacancha→Huarmey) — niet meegenomen.
- **Twee infrastructuurclusters bij San Marcos**: satellietbeeld toont zowel een verwerkingscomplex als
  (600 m zuidoostelijker) het rijenwoningen-arbeidscamp "Campamento Yanacancha" (OSM-landuse) — het anker is
  op het verwerkingscomplex gelegd, niet geverifieerd tegen een naamsbron op perceelniveau.
- **Zilver-jaarvolume niet apart gebrond** binnen budget; v1-schatting (~520 t Ag/j) aangehouden als indicatie,
  geen hard peiljaar.
- **Geen bron bevestigt een vaste smelterbestemming** voor het concentraat na Puerto Punta Lobitos.

## 8 · Bronnen
[1] Wikipedia (EN) — Antamina mine: JV Teck/BHP/Glencore/Mitsubishi, 410.000 t koperconcentraat in 2024 (15%
    van Peru's productie), 4.300 m hoogte, GBC-herstart 2025-2027. https://en.wikipedia.org/wiki/Antamina_mine
[2] Wikipedia (ES) — Mineroducto de Antamina: 302 km, Yanacancha-concentrator (San Marcos, Huari, 3.155 m) →
    Puerto Punta Lobitos (Huarmey, 15 m), diameter 25 cm, 4 klepstations (km 125/143/162/177), hoogste punt
    4.669 m, geopend 01-07-2001, 60/40 vast/water. https://es.wikipedia.org/wiki/Mineroducto_de_Antamina
[3] Antamina — Proceso de producción: 304 km, 65% → 9,5% vocht na filtratie, glasvezel-monitoring.
    https://www.antamina.com/proceso-productivo/
[4] Canadian Mining Journal — "Antamina blows your mind": onafhankelijke bevestiging van de mineroducto-lengte
    en -werking (~302–304 km, Andes → Puerto Punta Lobitos).
    https://www.canadianminingjournal.com/featured-article/antamina-blows-your-mind/
[5] RPP Perú — Áncash: paro en el corredor minero de Antamina (Aquia, Bolognesi) als gemeenschap op de
    mineroducto-corridor. https://rpp.pe/peru/actualidad/ancash-paro-en-el-corredor-minero-de-antamina-que-reclama-la-comunidad-de-aquia-y-que-responde-la-minera-noticia-1366043
[6] Antamina — nieuwspagina Santa Rosa de Cajacay (Bolognesi, Fortaleza-vallei, corridorgemeenschap).
    https://www.antamina.com/noticias/santa-rosa-de-cajacay/
[7] OpenStreetMap (ODbL) via Photon/Nominatim — Minera Antamina-landuse (-9,5540/-77,0476), Campamento
    Yanacancha (-9,5805/-77,0262), Puerto Punta Lobitos-Antamina-landuse (-10,1035/-78,1788), Aquia
    (-10,0745/-77,1447), Cajacay/Santa Rosa (-10,1747/-77,3355), Cochapeti (-9,9801/-77,6958), Huayan
    (-9,9079/-77,7933; "Carretera Huarmey - Recuay"). https://www.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) —
    `v2/build-cache/satcheck/sat-zilver-antamina-huarmey-mijn2.png`,
    `sat-zilver-antamina-huarmey-yanacancha.png`, `sat-zilver-antamina-huarmey-kade.png`.
[9] Infobae (2025-09-18) — Antamina, vierde grootste mijn van Peru, uitbreiding tot 2036 (context
    productie/JV). https://www.infobae.com/peru/2025/09/18/antamina-la-cuarta-mina-mas-grande-del-peru-y-una-de-las-10-mas-importantes-del-mundo-ampliara-sus-operaciones-hasta-2036/
[10] `v2/design/zilver.md` / `data/silver.js` (v1-checklist) — ag-antamina: ~520 t Ag/j, 2,0% wereldaandeel,
    bijproduct van koper/zink (Glencore/BHP/Teck JV).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom:** `zilver-antamina-huarmey` · **bestand:** `v2/data/stroomroute-zilver-antamina-huarmey.json`
(1,72 KB) · **recept:** `bak_zilver_antamina_huarmey()` in `v2/tools/bak_stromen.sh`

**Benen (1, opgesplitst in 5 stippel-segmenten, in reisvolgorde):**
| # | modaliteit | km hemelsbreed | stippel? |
|---|---|---|---|
| b1.1 | leiding | Yanacancha-concentrator → Aquia — 58,2 km | ja |
| b1.2 | leiding | Aquia → Cajacay/Santa Rosa — 23,7 km | ja |
| b1.3 | leiding | Cajacay/Santa Rosa → Cochapeti — 45,0 km | ja |
| b1.4 | leiding | Cochapeti → Huayan — 13,4 km | ja |
| b1.5 | leiding | Huayan → Puerto Punta Lobitos — 47,5 km | ja |

**Totaal:** 187,8 km · 10 punten · 2 markers (beide 0,0 km van de lijn — de ankers zijn zelf de
segment-uiteinden). Naden: alle vijf op 0,00 km (elk segment sluit exact aan op het vorige uiteinde,
geen aparte snap nodig). `toets_knikken.py`: 0 knikken ≥60°, dus 0 omkeringen, 0 terugloop.
`toets_rechte_benen.py --min-km 5`: alle vijf segmenten gemeld als rechte lijn (omwegfactor 1,000) —
verwacht en correct, want dit zijn bewust rechte stippels met reden in de naam, niet gemeten geometrie.
JSON: `versie 2`, `punt_formaat lonlat`, modaliteit `leiding` ∈ de toegestane set, elk been = 2 punten —
laadt schoon.

**Toelichting per stippel — waarom vijf segmenten in plaats van één been.** `hecht_marnet.py`'s
`--stippel`-vlag accepteert precies twee coördinaten per aanroep (`MODALITEIT|NAAM|VAN|NAAR`); er is
geen meerpunts-variant. De 6 invoerpunten uit de bak-aanwijzing (kop → 4 via-punten → staart) zijn
daarom als 5 opeenvolgende `--stippel`-segmenten met modaliteit `leiding` geketend — elk segment sluit
exact aan op het vorige uiteinde (naad 0,00 km), dus de lijn is visueel en topologisch één doorlopende
schematische pijpleiding, alleen intern in vijf stukken opgeknipt. Geen zeebeen: de brief stopt bewust
bij de Huarmey-kade (§6), dus geen haven-aanloop-check nodig.

**Eigen Overpass-poging (vóór het bakken, deze sessie):** `curl` naar `overpass-api.de/api/interpreter`
met `way["man_made"="pipeline"]` in bbox (-10.5,-78.5,-9.0,-76.5) gaf **HTTP 406**; de kumi-mirror
(`overpass.kumi.systems`) gaf een **timeout** (30 s, geen respons). Beide onbereikbaar — dezelfde
uitkomst als in de sessie die de brief schreef (§7). Nog steeds niet vastgesteld of OSM `man_made=pipeline`
voor deze corridor werkelijk ontbreekt of alleen deze twee keer onbereikbaar was.

**Grootste bevinding — de hemelsbrede stippel via de 4 via-punten is 37,9% korter dan de gepubliceerde
lengte, precies zoals de brief voorspelde.** Totaal gemeten: 187,8 km tegen de gepubliceerde 302 km
(Wikipedia ES; Antamina.com noemt 304) = **−37,9%**, ver buiten de gebruikelijke ±15%-norm van
`bakhandleiding-licht.md` §5. Dit is echter GEEN routerfout of een verkeerd gelegd anker: de brief §7
kondigde dit expliciet aan ("een hemelsbrede stippel via deze punten kan afwijken van de gepubliceerde
302 km") en zonderde deze stroom bewust uit van de harde ±15%-eis, omdat de echte mineroducto een
bergcorridor volgt met een hoogste punt van 4.669 m en vier klepstations (km 125/143/162/177) die niet
1-op-1 op de vier corridorgemeenschappen (Aquia, Cajacay/Santa Rosa, Cochapeti, Huayan) vallen — die
zijn gedocumenteerde nederzettingen ÓP de corridor, geen gemeten tracépunten. Een hemelsbrede stippel
tussen vier zulke punten snijdt onvermijdelijk bochten van de echte bergroute af. **Buiten de norm,
niet dichtgetrokken — bevinding, geen fout.**

**Gereedschapslessen:**
- `--stippel` is strikt tweepunts; een meerpunts-schematische lijn (kop→via1→via2→…→staart) wordt een
  keten van losse `--stippel`-aanroepen met modaliteit en naam die het segment benoemen. Zolang elk
  segment op het vorige uiteinde begint, blijft de naad 0,00 km en leest de gebakken lijn als één
  doorlopende stippel, ondanks de interne opsplitsing in het JSON.
- Een brief die vooraf al waarschuwt dat een schematische stippel buiten de ±15%-norm kan vallen (hier
  §7) hoeft bij het bakken niet opnieuw ter discussie te staan — de afwijking bevestigt de brief, in
  plaats van hem te weerleggen. Rapporteren in §9 volstaat; geen via-punt bijschuiven om het percentage
  te verbeteren (dat zou de "bekende gemeenschap"-bronstatus van de via-punten juist ondermijnen).
- Twee onafhankelijke Overpass-eindpunten (overpass-api.de, kumi-mirror) faalden op verschillende
  manieren (406 resp. timeout) binnen dezelfde sessie — een derde poging op een ander uur/mirror is nog
  niet uitgesloten, maar viel buiten het WEBBUDGET van deze bake.

**Open punten (naar de brief, niet dichtgetrokken):**
- OSM `man_made=pipeline` voor deze corridor is nog steeds niet bevestigd óf weerlegd — Overpass bleef
  in twee sessies onbereikbaar.
- De 37,9%-afwijking van de gepubliceerde 302 km is een gevolg van de schematische via-puntkeuze, geen
  gemeten tracéfout — een toekomstige OSM-pijpleidinggeometrie (als die ooit bevraagbaar wordt) zou de
  lijn dichter bij 302 km kunnen brengen zonder de via-puntkeuze te hoeven wijzigen.
- De overige open punten uit de brief (§7: twee infrastructuurclusters bij San Marcos, het niet-gebronde
  zilver-jaarvolume, het ontbrekende smelterbestemming-bewijs) blijven ongewijzigd — dit bakwerk raakt
  alleen de geometrie van been b1.
