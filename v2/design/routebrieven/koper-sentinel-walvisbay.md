# Routebrief (licht) · koper — Sentinel (Kalumbila) → Walvis Bay (Namibië)

**stroom-id:** `koper-sentinel-walvisbay` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** sulfide-concentraat van de Sentinel-mijn (First Quantum, Kalumbila) per **truck** over de Trans-Caprivi-corridor — Solwezi → Mutanda → Kasempa → Kaoma → Mongu → Senanga → Sesheke → grens **Katima Mulilo** → Namibische B8/B1/B2 → **Walvis Bay-haven** — een derde uitgang voor Zambisch koper naast Kasumbalesa→Durban (TFM) en Lobito→Duisburg (Kamoa). Stoppunt bij de kade: geen gedocumenteerde overzeese afnemer.
**Welke as van het verhaal:** Copperbelt-westcorridor. Sentinel produceerde ≈189 kt Cu-inhoud in 2025 (Sentinel+Kansanshi samen 370 kt) [1][2]; sinds eind 2025 upgradet Western Corridor Limited het 371 km-tracé Mutanda–Katima Mulilo naar verhard wegdek, expliciet gepresenteerd als "de snelste route naar Walvis Bay" [3][4]. Het aandeel van het Sentinel-volume dat specifiek via Walvis Bay gaat (i.p.v. Durban/Dar es Salaam/Kasumbalesa) is in geen bron gekwantificeerd — copper.js noemt alleen "deels westwaarts" [5].

## 1 · Ketenkaart
Sentinel-mijn (Kalumbila) `cu-sentinel-mijn` ──(b1 truck · Solwezi–Mutanda–Kasempa–Kaoma–Mongu–Senanga–Sesheke · ~570 km, aannemelijk: aandeel Walvis Bay t.o.v. Durban/Dar es Salaam niet gekwantificeerd)──► grens Katima Mulilo/Sesheke (Zambezi-brug)
  ──(b2 truck · Namibische B8/B1/B2 — Rundu–Otavi–Otjiwarongo–Karibib · ~1.470 km)──► Walvis Bay-haven `cu-walvisbay-kade` ── stoppunt (geen gedocumenteerde overzeese afnemer)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `cu-sentinel-mijn` → grens Katima Mulilo/Sesheke (aannemelijk: aandeel Walvis Bay niet gekwantificeerd) | Zambia: Solwezi-uitvalsweg (FQM-investering) → Mutanda–Kasempa–Kaoma–Mongu–Senanga–Sesheke (het 371 km-WCL-upgradetracé) | Sentinel–Solwezi 150 [1]; Mutanda–grens 371 (officieel, WCL/Zambiaanse overheid) [3][4]; Solwezi–Mutanda ~45 (geschat, niet gepubliceerd) → totaal ≈566 | maak_stroombeen_weg (extract `zambia`) | nee — corridor bestaat als weg; aandeel-onzekerheid staat in de naam, niet in de lijnstijl |
| b2 | A | truck | grens Katima Mulilo/Sesheke → `cu-walvisbay-kade` | Namibische **B8** (Katima Mulilo–Rundu–Otavi) → **B1** (Otavi–Otjiwarongo–Karibib-afslag) → **B2** (Karibib–Swakopmund–Walvis Bay) — de Trans-Caprivi-corridor, offici­eel "Walvis Bay-Ndola-Lubumbashi Development Road" [4][6] | opgeteld uit de Wikipedia-routebeschrijving (Katima Mulilo–Rundu 510, Rundu–Otavi–Karibib–Walvis Bay ~960) ≈1.470; totale corridor Walvis Bay–Lubumbashi 2.700 km [4] — geen stapsgewijze officiële bron per traject | maak_stroombeen_weg (extract `namibie`) | nee |

Geen zee-been, geen haven-aanloop-vraagstuk: de brief stopt bij de kade (stoppunt, §6).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-sentinel-mijn` | mijn / laadplek | Sentinel-mijn (Kalumbila), First Quantum Minerals | -12.2600, 25.3025 | [1][2] | **bron-gelegd** (z14 gezien: grote open pit met gelaagde bermen, ertsstapels aan de oostrand, plant-/tankhouse-gebouwencluster direct ten zuiden van de put, landingsbaan ten zuiden — sat-koper-sentinel-walvisbay-cu-sentinel-mijn.png) |
| `cu-walvisbay-kade` | overslag / kade (stoppunt) | Walvis Bay-containerterminal, gereclameerd havenhoofd | -22.9500, 14.4860 | [7][8] | **bron-gelegd**, exacte bulkkade voor kopererts **aannemelijk** (z15/z17 gezien: containerstapels en portaalkranen op het gereclameerde havenhoofd, ligplaatsen langs de kade; ouder havenbekken met tankopslag zuidoostelijk — sat-koper-sentinel-walvisbay-cu-walvisbay-bulkkade.png). Welke specifieke kade (container vs. bulk) kopererts gebruikt is niet gebrond → open punt |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Solwezi (provinciehoofdstad, regionale FQM-wegknoop) | -12.1833, 26.3858¹ | Sentinel–Solwezi is de gepubliceerde 150 km-aftakking [1]; Solwezi is de enige aansluiting op het regionale wegennet vóór Mutanda |
| b1 | 2 | Mutanda | -12.4000, 26.2400 | start van het officiële 371 km-WCL-upgradetracé [3][4]; sluit de directe Solwezi–Chingola-route (naar Kasumbalesa/Durban) uit |
| b1 | 3 | Kasempa | -13.4550, 25.8350 | ligt op het WCL-tracé; president Hichilema noemt Kasempa expliciet als tussenstap [3] |
| b1 | 4 | Kaoma | -14.8000, 24.8000 | WCL-tracé; splitst van de Mongu-noordroute (naar Zambezi-vlakte-binnenland) af |
| b1 | 5 | Mongu | -15.2775, 23.1319 | WCL-tracé; provinciehoofdstad Western Province, verplichte doorgang op de T1/M10-as richting Senanga |
| b1 | 6 | Senanga | -16.1167, 23.2667 | WCL-tracé, laatste grote plaats vóór de Zambezi-vlakte richting Sesheke |
| b1 | 7 | Sesheke | -17.4667, 24.3000 | Zambiaanse grensstad; sluit de oostelijkere Livingstone/Kazungula-route (naar Botswana/Durban) uit |
| b1 | 8 | Grensovergang Katima Mulilo-brug (Zambezi) | -17.4717, 24.2499 | verplichte grenspost Zambia/Namibië; enige wegverbinding op dit deel van de Zambezi [9] |
| b2 | 1 | Rundu (B8) | -17.9170, 19.7670 | eerste grote Namibische stad op de B8, sluit de route vast op de Trans-Caprivi-as [4] |
| b2 | 2 | Otavi (B8→B1) | -19.6642, 17.3306² | wisselpunt van de B8 op de noord-zuid-hoofdas B1; sluit een omweg via Grootfontein-oost uit |
| b2 | 3 | Otjiwarongo (B1) | -20.4642, 16.6528 | B1 door Otjiwarongo, vaste tussenstop op de corridor naar Karibib [4] |
| b2 | 4 | Karibib (B1→B2) | -21.9381, 15.8544 | wisselpunt van de B1 op de B2 richting Swakopmund/Walvis Bay; sluit de Windhoek-omweg uit |

¹ Solwezi-coördinaat uit Wikipedia-infobox, DMS→decimaal afgerond op 4 decimalen.
² Otavi-coördinaat afgeleid; niet apart satellietgecheckt (via-punt, geen anker).

## 5 · Verwerkingsknopen
Geen — dit is een mijn-tot-havenkade-keten zonder smelter of raffinaderij onderweg (concentraat blijft concentraat tot de kade).

## 6 · Stoppunt
De brief stopt bij de Walvis Bay-kade: geen bron noemt een overzeese afnemer of vervolgbestemming voor dit specifieke volume — Walvis Bay is voor Zambisch koper "een derde uitgang" naast Durban en Lobito, niet gekoppeld aan een benoemde smelter (§7).

## 7 · Open punten
- **Aandeel Walvis Bay in het Sentinel-volume:** geen bron kwantificeert dit t.o.v. Durban/Dar es Salaam/Kasumbalesa (v1 copper.js noemt alleen "deels westwaarts") [5]. Jaarvolume van dít been is dus onbekend; ≈189 kt Cu-inhoud (2025) is het totale Sentinel-volume, niet het Walvis Bay-deel [1].
- **Sentinel–Solwezi–Mutanda:** de 150 km Sentinel–Solwezi is gepubliceerd [1], het stuk Solwezi–Mutanda (~45 km) is een kaartschatting, geen bron.
- **Namibische trajectkilometers (b2):** opgeteld uit een Wikipedia-routebeschrijving, niet als los cijfer per subtraject gepubliceerd; bij het bakken bepaalt de OSM-route het echte getal.
- **Exacte Walvis Bay-kade:** container- vs. bulkterminal voor kopererts niet gebrond; het anker staat op de containerterminal (grootste, meest zichtbare kade), de werkelijke bulklosplek kan de oudere haven zuidoostelijk zijn (zichtbaar op de overzichtsopname).
- **Sentinel-mijnweg → Solwezi:** het exacte tracé van de mijnpoort naar de Solwezi-hoofdweg is niet gekarteerd als apart via-punt (site-niveau, geen last-mile-been per de lichte werkwijze).

## 8 · Bronnen
[1] Wikipedia, "Sentinel mine" (coördinaten 12°15′36″S 25°18′09″E, First Quantum Minerals, 150 km west van Solwezi, ≈300 kt concentraat/jaar), https://en.wikipedia.org/wiki/Sentinel_mine
[2] Wikipedia, "Kalumbila Mine" (FQM Trident Limited, 2020 recordproductie 251.216 t, maalcapaciteit 3→6 Mt/jaar, exporteert via havens in Tanzania/Zuid-Afrika/Namibië), https://en.wikipedia.org/wiki/Kalumbila_Mine
[3] Infrastructure News, "Fastest Trade Route to Walvis Bay Port Launched by Western Corridor Limited in Zambia" (371 km Mutanda–Kasempa–Kaoma–Mongu–Senanga–Sesheke–Katima Mulilo, citaat president Hichilema, bituminering van het huidige grindtracé, bruggen over de Lalafuta en Luena), 2025-11-25, https://infrastructurenews.co.za/2025/11/25/fastest-trade-route-to-walvis-bay-port-launched-by-western-corridor-limited-in-zambia/
[4] Wikipedia, "Walvis Bay-Ndola-Lubumbashi Development Road" (voorheen Trans-Caprivi Highway/Corridor; volledige routebeschrijving Walvis Bay–Swakopmund–Karibib–Okahandja–Otjiwarongo–Otavi–Rundu–Katima Mulilo–Sesheke–Kazungula–Livingstone–Choma–Lusaka–Kabwe–Kapiri Mposhi–Ndola–Kitwe–Chingola–Kasumbalesa–Lubumbashi; totaal 2.700 km; wegnummers B2/B1/B8 Namibië, M10/T1/T2/T3 Zambia), https://en.wikipedia.org/wiki/Walvis_Bay-Ndola-Lubumbashi_Development_Road
[5] `data/copper.js` (v1), node `cu-sentinel` — "Sulfide-concentraat; exporteert deels westwaarts via Walvis Bay", geen kwantificering
[6] Zawya, persbericht Western Corridor Limited (corroboreert [3]), https://www.zawya.com/en/press-release/africa-press-releases/fastest-trade-route-to-walvis-bay-port-launched-by-western-corridor-limited-in-zambia-sbg0qcki
[7] Haalbaarheidstoets `koper-sentinel-walvisbay` (2026-09-28) — aanpassing: kade-anker Port of Walvis Bay SADC Gateway ≈-22.9102, 14.5354 (OSM-industrieterrein); bij satellietcheck bleek dit dicht bij, maar niet exact op, de zichtbare containerterminal-kade — anker verschoven naar de satelliet-bevestigde kadelijn (-22.9500, 14.4860)
[8] Satellietblik `v2/tools/sat_check.py`, Esri World Imagery z13–z17, 2026-09-28: `sat-koper-sentinel-walvisbay-cu-sentinel-mijn.png` (z14) · `sat-koper-sentinel-walvisbay-cu-walvisbay-overzicht.png` (z13, havenoverzicht) · `sat-koper-sentinel-walvisbay-cu-walvisbay-haven.png` (z15) · `sat-koper-sentinel-walvisbay-cu-walvisbay-bulkkade.png` (z17, kadedetail) — alle in `v2/build-cache/satcheck/`
[9] Wikipedia, "Katima Mulilo Bridge" (17°28′18″S 24°14′59.73″E; brug over de Zambezi tussen Namibië en Zambia, geopend 2004, verbindt de Zambiaanse Copperbelt met de Namibische diepzeehaven Walvis Bay), https://en.wikipedia.org/wiki/Katima_Mulilo_Bridge
[10] Wikipedia-infoboxen (coördinaten, DMS→decimaal), geraadpleegd 2026-09-28: Mutanda (Zambia) 12°24′00″S 26°14′24″E · Kasempa 13°27′18″S 25°50′06″E · Kaoma (Zambia) 14°48′00″S 24°48′00″E · Mongu 15°16′39″S 23°7′55″E · Senanga 16°07′00″S 23°16′00″E · Sesheke 17°28′00″S 24°18′00″E · Katima Mulilo 17°30′14″S 24°16′30″E · Rundu 17°55′S 19°46′E · Otjiwarongo 20°27′51″S 16°39′10″E · Karibib 21°56′17″S 15°51′16″E · Solwezi 12°08′36″S 26°23′09″E
[11] The Globe and Mail, "The world is scrambling for Zambia's critical minerals, with Canadian miners at the forefront" (2025-productiecijfers Sentinel/Kansanshi, achtergrond Trans-Caprivi-upgrade), https://www.theglobeandmail.com/business/article-the-world-is-scrambling-for-zambias-critical-minerals-with-canadian/
[12] Mining.com, "First Quantum begins production at $2.1bn Sentinel copper mine in Zambia" (bouwgeschiedenis, $2,3 mrd, ~6.000 werknemers), https://www.mining.com/first-quantum-begins-production-at-2-1bn-sentinel-copper-mine-in-zambia/

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `koper-sentinel-walvisbay`** → `v2/data/stroomroute-koper-sentinel-walvisbay.json` — 2 benen, beide truck. **2.407,4 km**, 3 markers. Bestand 278,6 KB.
Recept: `bak_stromen.sh` (functie `bak_koper_sentinel_walvisbay`). Toelichting per been:
- **b1 (truck, Zambia):** `maak_stroombeen_weg.py --profiel koper-sentinel-walvisbay-sentinel-katimamulilo` (venster 75 km, extract `zambia`). Eerste poging gaf *"geen wegpad tussen punt 0 en 1"* (mijn → Solwezi) — de Sentinel-mijn hangt alleen via tertiary/unclassified-wegen aan het net, ver buiten de standaard 12 km-eindzone-straal → `corridorKlassen: ["tertiary", "unclassified"]` toegevoegd (corridor-breed, niet alleen bij de ankers). Daarna faalde het opnieuw tussen punt 4 en 5 (Kaoma → Mongu): de Wikipedia-centroïde van Mongu (23,1319/−15,2775) snapte op een volledig geïsoleerde straatjesstomp van 10 knopen (gemeten met een component-BFS over de gebouwde graaf — geen enkele verbinding met het net). Via-punt verschoven naar **294 m** verderop, op de M10-doorgaande weg zelf (23,1344278/−15,2764746), die wél in het grote net zit (snap <5 cm) — geen coördinaat verzonnen, hetzelfde als de via-punt-projectie-klasse uit eerdere sessies ("punten 300–500 m vóóruit leggen"). Daarna routeerde het been door: **985,8 km** na 8 gesnoeide keerlussen (1.064,5 → 985,0 km ruw, +0,8 km tekengeometrie).
- **b2 (truck, Namibië):** `maak_stroombeen_weg.py --profiel koper-sentinel-walvisbay-katimamulilo-walvisbay` (venster 40 km, extract `namibie`), zonder aanpassingen geslaagd: **1.421,6 km** na 13 gesnoeide keerlussen.
- Naad tussen b1 en b2 = **0,00 km** (zelfde grenscoördinaat, geen knoop nodig — gewoon aansluitend been, zoals de brief aangaf).
- Alle 3 markers uit §3 zijn meegenomen; geen fase C/D/E (geen verwerkingsknoop, brief §5) en geen zee-been (brief stopt bij de kade, §6).

**Toets-bevindingen (buiten de norm, niet dichtgetrokken):**
- **b1 valt BUITEN de ±15%-norm: 985,8 km tegen ~566 km uit de brief (+74,0%).** Gemeten per subtraject: Sentinel→Solwezi 158,2 km (tegen 150 gepubliceerd, +5,5%, binnen norm) · Solwezi→Mutanda 33,4 km (tegen ~45 geschat) · Mutanda→Kasempa 147,3 · Kasempa→Kaoma 219,1 · Kaoma→Mongu 190,6 · Mongu→Senanga 103,6 · Senanga→Sesheke 206,4 · Sesheke→grens 5,9 km — samen Mutanda→grens 872,9 km tegen de "371 km" uit het WCL-persbericht (brief §2/[3][4]). Die 371 km is **geometrisch niet houdbaar** als punt-tot-punt-routeafstand Mutanda→grens: de rechte grootcirkellijn tussen die twee punten is zelf al ~603 km, dus 371 km kan onmogelijk de volledige routelengte via Kasempa/Kaoma/Mongu/Senanga/Sesheke beschrijven. Vermoedelijke verklaring: de bronregel beschrijft de lengte van het specifieke wegverbeteringsproject (het te bitumineren tracé-gedeelte), niet de totale afstand tussen de genoemde plaatsen. Geen via-punt is bijgeschoven om het getal te halen (de werkregel) — dit is een bevinding over de brief-bronnering, geen routeerfout: 8 echte keerlussen zijn al gesnoeid en elk via-punt snapt op ≤2,4 km van zijn corridor (zie hieronder).
- **b2 valt WEL binnen de norm:** 1.421,2 km (tool) / 1.421,6 km (gebakken) tegen ~1.470 km opgeteld-Wikipedia-cijfer = **−3,3%**.
- **Anker-verbinding Sentinel-mijn → weg = 0,75 km** — iets boven de zachte richtlijn van 0,5 km (het anker staat op de put/plantcluster, de dichtstbijzijnde graafknoop ligt op de mijnpoort-toegangsweg); alle overige snaps (weg → grens 0,01–0,04 km, grens → Namibische net 0,01–0,37 km, weg → Walvis Bay-kade 0,42 km) liggen ruim onder 0,5 km.
- `toets_knikken.py`: b1 heeft knikken waarvan geen enkele "terugloop" (de categorie die reparatie zou vragen); b2 heeft 24 knikken, 1 omkering (178,1° bij de grensbrug zelf, een echte scherpe bocht op het emplacement) en 0 terugloop. Alle overige gerapporteerde hoeken zijn spikes/krappe bochten op de OSM-geometrie (rotondes, kruisingen), niet gerepareerd.
- `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de verdachtenlijst — beide benen zijn doorgetrokken (geen stippel nodig).
- JSON-vormtoets: `versie` 2, `punt_formaat` `lonlat`, modaliteit `{truck}` (toegestaan), elk been ≥2 punten, bestand 278,6 KB (< 300 KB) — allemaal in orde.

**Gereedschapslessen:**
- `corridorKlassen` is soms nodig vanaf de EERSTE meter van een been, niet alleen op een tussenliggend deelstuk: hier hing de mijn zelf al buiten de 12 km-eindzone-straal aan alleen kleine wegklassen, dus zonder corridor-brede toelating faalde zelfs het eerste sub-traject (mijn → eerste via-punt).
- Een via-punt kan op een geometrisch correcte, dichtbij liggende OSM-coördinaat landen die tóch een geïsoleerde graafcomponent is (10 knopen, geen enkele verbinding met het net) — een snap-afstand van slechts 0,23 km verhulde dit volledig; alleen een expliciete component-connectiviteitscheck (BFS vanaf elk anker) legde het bloot. Deze klasse is subtieler dan de eerdere ">5 km snap = fout gelegd"-vuistregel: hier was de snap-afstand klein maar de component fataal klein.
- Een gepubliceerde "X km"-lengte in een persbericht kan een deelproject beschrijven in plaats van de volledige punt-tot-puntafstand — controleerbaar met een simpele grootcirkelcheck vooraf (hier: 371 km beweerd tegen 603 km rechte lijn, een contradictie die de bron zelf ontkracht).
