# Routebrief (licht) · lithium — Bougouni (Mali) → San Pedro (Ivoorkust) → Yangpu (China)

**stroom-id:** `lithium-bougouni-yangpu` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) ·
**status:** gebakken
**Keten in één zin:** spodumeenconcentraat van de Ngoualana-mijn/DMS-fabriek van Kodal Minerals bij Kola
(Cercle de Bougouni, Zuid-Mali) gaat per truck ~880 km naar een eigen bulkstockpile in de haven van San
Pedro (Ivoorkust), per bulkschip ~15.000 km rond Kaap de Goede Hoop naar Yangpu (Hainan, China), en
vandaar per truck naar de Xingzhihai-lithiumzoutfabriek van Hainan Mining in het Yangpu New Materials
Industrial Park — de nieuwste en best gebronde West-Afrikaanse lithium-as van de atlas.
**Welke as van het verhaal:** *de nieuwste bron meteen aan China gebonden.* Mali produceerde in 2025
9,4 kt Li-inhoud (van 0,77 kt in 2024, USGS) — bijna alles van Bougouni (fase 1, tweede lithiummijn van
Mali) en Goulamina (Ganfeng, groter maar zonder openbare exportroute). Hainan Mining nam in 2023 de
controlerende belang in Bougouni voor US$118 mln en bouwt tegelijk zijn eigen 20 kt/j LiOH-fabriek in
Yangpu — mijn, schip én raffinage in één eigenaarschap, het eerste schip voer al: vertrek San Pedro
30‑11‑2025, aankomst Hainan 07‑01‑2026 (28.735 DMT), tweede lading 20 kt in lading begin 2026 [1][2][4].

## 1 · Ketenkaart
```
Ngoualana-put + DMS-fabriek `li-bougouni-plant` ──(b1 truck · RN7/A3 via Sikasso–Zégoua/Pogo–
Ferkessédougou–Yamoussoukro–Soubré · ~880 km, aannemelijk tracé)──► San Pedro bulkterminal
`li-sanpedro-tipsp` ──(b2 zee · Golf van Guinee–Kaap–Indische Oceaan–Malakka–Zuid-Chinese Zee ·
~15.000 km, MARNET)──► Yangpu-kade `li-yangpu-kade` (SDIC Yangpu Port, Hainan)
──(b3 truck · havenweg binnen Yangpu New Materials Industrial Park · < 10 km, stippel)──►
Xingzhihai-lithiumzoutfabriek `li-yangpu-xingzhihai` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (spodumeenconcentraat, bulk) | `li-bougouni-plant` → `li-sanpedro-tipsp` | RN7 Bougouni–Sikasso → grens Zégoua/Pogo → Ferkessédougou → Bouaké → Yamoussoukro → Soubré → San Pedro (gevestigde corridor, "één grensovergang") | 880 [2][3] | maak_stroombeen_weg (extracts mali + ivoorkust; 5 via-punten §4; lengtetoets ±15% is de controle) | nee — *aannemelijk tracé, één bron voor de bestemming* |
| b2 | B | zee (bulkcarrier) | `li-sanpedro-tipsp` → `li-yangpu-kade` | Golf van Guinee → Kaap de Goede Hoop → Indische Oceaan → Straat Malakka → Zuid-Chinese Zee ("over 10.000 km", Hainan Mining zegt korter dan MARNET's Kaap-route meet) [4][6] | ≈15.000 (MARNET) | MARNET; San Pedro zeeknoop ≈1,6 km (geen aanloop); Yangpu zeeknoop ≈25 km (aanloop nodig, geen AIS in Hainan) | aanloop Yangpu: ja (stippel) |
| b3 | C | truck | `li-yangpu-kade` → `li-yangpu-xingzhihai` | havenweg/estateweg Yangpu Economic Development Zone → New Materials Industrial Park | ≈5–10 (geen publicatie) | maak_stroombeen_weg indien EDZ-wegen in het extract zitten; anders stippel | ja — *last mile binnen het park, net reikt niet tot de fabriekspoort* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-bougouni-plant` | mijn / DMS-fabriek (laadplek) | Ngoualana open pit + Stage 1 DMS-plant, Kodal Minerals/LMLB, commune Kola (Cercle de Bougouni) | 11.3413, -7.4886 | [2][3][12][13][14][16] | bron-gelegd (z17 gezien: verwerkingsgebouw met toren/transportbrug, tanks en stockyard aan een rode haalweg; de ovale open put met bermen ligt ~700 m NNW aan de rivier — exact het beeld dat Kodal's eigen "Ngoualana open pit"-updates beschrijven; site ligt in de commune Kola die Kodal zelf als project-commune noemt naast Bougouni) |
| `li-sanpedro-tipsp` | overslag (kade/stockpile) | Terminal Industriel Polyvalent de San Pedro (TIPSP, ARISE P&L/S.Energies), Port Autonome de San Pedro | 4.7490, -6.6180 | [5][8][9][10][16] | bron-gelegd (z17-z18 gezien: bulkstockpile met stacker/reclaimer-mond en spooraansluiting op een schiereiland tussen twee havenarmen, apart van het containerterminal ernaast — matcht TIPSP's 13,8 ha / 600.000 t-opslag voor "mining ores incl. lithium") |
| `li-yangpu-kade` | overslag (losplek) | SDIC Yangpu Port-havenzone, Yangpu Economic Development Zone, Hainan | 19.7680, 109.1510 | [4][6][16] | onzeker (z15 gezien: een havensteiger los van de petrochemische tankopslag verderop, maar welke specifieke berth de Bougouni-lading loste is niet gepubliceerd — bak-agent routeert op de MARNET-zeeknoop + aanloop, niet op dit exacte punt) |
| `li-yangpu-xingzhihai` | fabriek (fase C-eind) | Hainan Xingzhihai New Materials (海南星之海新材料), Yangpu New Materials Industrial Park, Danzhou | 19.7180, 109.1570 | [4][7][11] | onzeker (geregistreerd adres bekend — Binhai Ave. 75, hoek Deyiling Rd/Lianhuashan Rd, Yangpu New Materials Industrial Park [7] — maar niet satelliet- of MEE-registerbevestigd; coördinaat is de best passende plek binnen het nieuwe industrieterrein aan de havenzone, geen vastgelegd anker) |

## 4 · Via-punten (alleen b1 — de enige landcorridor met een keuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Sikasso | 11.3166, -5.6778 | RN7 oostwaarts vanaf Bougouni; enige geasfalteerde corridor naar de grens |
| b1 | 2 | grens Zégoua (ML) / Pogo (CI) | 10.4828, -5.6531 | de "ene grensovergang" die Kodal zelf noemt [2][3] |
| b1 | 3 | Ferkessédougou | 9.5940, -5.1976 | knooppunt A3/N1 zuidwaarts, na de grenscorridor |
| b1 | 4 | Yamoussoukro | 6.8200, -5.2776 | hoofdstad-knooppunt op de doorgaande N1/A3 richting de Zuidkust |
| b1 | 5 | Soubré | 5.7850, -6.5933 | laatste knooppunt vóór de aftakking naar San Pedro |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ngoualana DMS-plant | Kodal Mining UK / LMLB (49% Kodal, 51% Hainan Mining) | ertsvoeding 1 Mt/j → spodumeenconcentraat SC 5,3–5,5% Li2O | 125 kt SC/j fase 1-doel; werkelijk 2025 41.916 DMT (5,33% Li2O); 2026-forecast ~118.000 DMT | [2][3] |
| Xingzhihai-lithiumzoutfabriek | Hainan Mining (海南矿业) | spodumeenconcentraat → batterijkwaliteit LiOH·H2O (+ sinds medio 2026 ook Li2CO3) | 20 kt/j LiOH fase 1 (US$164 mln investering) | [4][6] |

Omrekening jaarvolume (context.eenheid_capaciteit = kt LCE): 125 kt SC 5,5% Li2O/j × 2,473 × 0,055 ≈
17 kt LCE/j; 20 kt LiOH/j × 0,88 ≈ 17,6 kt LCE/j — de twee eindes van de keten komen daarmee grofweg
overeen (oorspronkelijke eenheden: kt spodumeenconcentraat resp. kt LiOH·H2O, zoals opgegeven door Kodal
resp. Hainan Mining, 2025/2026-cijfers).

## 6 · Stoppunt
De brief stopt bij de Xingzhihai-lithiumzoutfabriek: dat is het enige stroomafwaartse punt dat één bron
(Hainan Mining zelf) expliciet aan deze Bougouni-lading koppelt ("zal direct naar Xingzhihai's
productielijnen gaan" [4]). Geen bron noemt welke batterij- of kathodefabriek het LiOH/Li2CO3 vervolgens
koopt — fase D vervalt.

## 7 · Open punten
- **Ivoriaans tracé (b1) is niet gepubliceerd** — alleen "~880 km, één grensovergang, gevestigde
  corridor via Sikasso" [2][3]. De hier gekozen via-Yamoussoukro-route geeft over de via-punten ~1.014 km
  hemelsbreed, dus ruim boven de gepubliceerde 880 km; een westelijker tak (bv. via Daloa i.p.v.
  Yamoussoukro) is even plausibel en onbeslisbaar zonder extra bron — de bake-lengtetoets (±15% op de
  gevolgde weggeometrie, niet op de rechte lijn via de punten) is de echte controle.
- **`li-bougouni-plant` is satelliet-gelegd maar niet register-bevestigd** — geen enkele bron geeft een
  officiële coördinaat voor de Ngoualana-put of de DMS-fabriek; het punt is gevonden door de commune Kola
  (die Kodal zelf als project-commune naast Bougouni noemt [13][14]) satellietsgewijs af te zoeken op
  mijnbouw-signatuur (put, haalwegen, verwerkingsgebouw). Sterk visueel bewijs, geen documentbron voor de
  coördinaat zelf.
- **`li-yangpu-kade` en `li-yangpu-xingzhihai` zijn beide onzeker** — de SDIC Yangpu-havenzone bevat
  meerdere steigers (petrochemie, containers, algemene lading) en geen bron zegt welke de Bougouni-lading
  loste; de Xingzhihai-fabriek heeft een geregistreerd adres [7] maar geen satelliet- of MEE-registerpas is
  gelukt binnen deze sessie (de bak-agent kan §1–§3 van `bakhandleiding-licht.md` gebruiken om het
  MEE-emissieregister of een fijnere satellietpas op Binhai Ave. 75 te proberen).
- **Fase C-lengte (b3) is een schatting** (~5–10 km, "onder 2 km → stippel" volgens de lichte werkwijze) —
  zonder bevestigde fabriekscoördinaat is dit been sowieso een stippel.
- **Goulamina (Ganfeng, 506 kt SC/j — 4× groter dan Bougouni) draagt het "Mali-lithium"-verhaal beter**
  maar exporteert via Abidjan zonder gepubliceerde route na de kade [9][10] → alleen genoemd, niet
  getekend, zoals in het ontwerp voorzien.
- **Productievolume loopt fors achter op het fase 1-doel** — 2025 werkelijk 41.916 DMT tegen het 125 kt/j-
  doel (verklaard door een meet-/kalibratiefout op de transportband, sinds hersteld) [2]; de brief tekent
  de ontwerpcapaciteit, niet het ramp-up-cijfer.

## 8 · Bronnen
[1] Kodal Minerals, "Bougouni Project First Shipment of Spodumene Concentrates Departs Port of San Pedro", 01-12-2025 — 28.950 t geladen, vertrek 30-11-2025, ~880 km wegtransport, US$24 mln eerste opbrengst. https://kodalminerals.com/bougouni-project-first-shipment-of-spodumene-concentrates-departs-port-of-san-pedro/
[2] Kodal Minerals, "Bougouni Lithium Project – Operations Update", 05-02-2026 — aankomst Hainan 07-01-2026 (28.735 DMT, US$27,25 mln), tweede lading 20.000 t, Ngoualana-mijnstatistieken, 2025-jaarproductie 41.916 DMT (herzien), 2026-forecast 118.000 DMT. https://kodalminerals.com/bougouni-lithium-project-operations-update/
[3] Kodal Minerals, "Bougouni Lithium Project" (projectpagina) — 350 km², Madina- en Kolassokoro-concessies, Ngoualana/Boumou/Sogola-Baoulé-prospecten, Stage 1 DMS 125 kt SC/j. https://kodalminerals.com/operations/bougouni-lithium-project/
[4] Hainan Mining (海南矿业), "First Shipment of Lithium Concentrate from Bougouni Lithium Mine Arrives at Yangpu Port, Hainan", 09-01-2026 — 30.000 t aangekomen, direct naar Xingzhihai-productielijnen, US$118 mln overname 2023, zero-tariff-import. https://www.hnmining.com/en/news_show.php?id=806
[5] Arise P&L, "Ivory Coast — Terminal Industriel Polyvalent De San Pedro" — 13,8 ha, kade 270 m/14 m diepgang, 600.000 t opslag, "mining ores such as … Lithium". https://www.arisepl.com/location/ivory-coast/
[6] S&P Global / Fastmarkets, "Hainan Mining to invest $164 million in 20,000-tpy lithium hydroxide plant", 2021. https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/082421-chinas-hainan-mining-to-invest-164-million-in-lithium-hydroxide-plant
[7] Tianyancha (天眼查), bedrijfsprofiel 海南星之海新材料有限公司 — geregistreerd adres 海南省儋州市洋浦经济开发区滨海大道75号洋浦新材料产业园德义岭路与莲花山路交叉处东南角. https://www.tianyancha.com/company/3487051581
[8] Ecofin Agency, "Mali's Lithium Finds a Gateway in Two Ivorian Ports", 24-10-2025 — Kodal koos San Pedro (50t-bulktrucks, kostenvoordeel), Ganfeng koos Abidjan. https://www.ecofinagency.com/news/2410-49787-malis-lithium-finds-a-gateway-in-two-ivorian-ports
[9] LogistAfrica, "Ivory Coast: Abidjan and San Pedro Emerge as Key Hubs for Malian Lithium", 30-10-2025. https://logistafrica.com/en/logistic/ivory-coast-abidjan-and-san-pedro-emerge-as-key-hubs-for-malian-lithium/
[10] Mysteel, "Key Lithium Mining Projects in Mali: Goulamina and Bougouni" — Goulamina (Ganfeng) vs Bougouni vergelijking. https://www.mysteel.net/analysis/5112006-key-lithium-mining-projects-in-mali-goulamina-and-bougouni
[11] Baidu Baike (百度百科), 星之海锂盐厂 — Xingzhihai lithiumzoutfabriek, dochter van Hainan Mining, in het Yangpu New Materials Industrial Park; producten batterijkwaliteit LiOH en Li2CO3. https://baike.baidu.com/item/星之海锂盐厂/67208533
[12] Mining-Technology, "Bougouni Lithium Project, Mali" — Madina- en Kolassokoro-concessies (2016 verworven), 180 km zuid van Bamako. https://www.mining-technology.com/projects/bougouni-lithium-project-mali/
[13] Dry Bulk magazine, "Bougouni lithium project E&D update", 31-05-2019 — gemeenschapsoverleg met "village chiefs and mayors of the two main communes of Bougouni and Kola". https://www.drybulkmagazine.com/dry-bulk/31052019/bougouni-lithium-project-ed-update-bulk-sample-mining-contract-terminated/
[14] Mining Review, "Kodal Minerals – Bougouni lithium project comes on stream" — Ngoualana/Sogola-Baoulé/Boumou/Kola-prospecten. https://www.miningreview.com/magazine-article/kodal-minerals-bougouni-lithium-project-comes-on-stream/
[15] NAI 500, "Kodal's first Bougouni trucks test Mali lithium route", 20-10-2025 — corridor "toward Sikasso and into Côte d'Ivoire … the country's most established export route". https://nai500.com/blog/2025/10/kodal-s-first-bougouni-trucks-test-mali-lithium-route/
[16] OpenStreetMap (ODbL) via Nominatim — Kola-dorpsknoop 11,3411/-7,4739 (Cercle de Bougouni); Port Autonome de San Pédro-landuse 4,7394/-6,6195; Yangpu Economic Development Zone-grens 19,7634/109,2036 · Esri World Imagery via `v2/tools/sat_check.py` (z12–z18) — `sat-lithium-bougouni-yangpu-plant-z17b.png`, `sat-lithium-bougouni-yangpu-tipsp.png`, `sat-lithium-bougouni-yangpu-sanpedro-kade.png`, `sat-lithium-bougouni-yangpu-terminal2.png`.


## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `lithium-bougouni-yangpu`** → `v2/data/stroomroute-lithium-bougouni-yangpu.json` — 4 benen,
18.879,6 km, 4 markers: truck 1.150,2 km · zee 17.698,8 km · zee (stippel) 20,4 km · truck 10,2 km.
Recept: `bak_stromen.sh` (functie `bak_lithium_bougouni_yangpu`).

**Toelichting per been:**
- **b1 (truck, Ngoualana-plant → San Pedro TIPSP):** 1.150,2 km tegen de gepubliceerde ~880 km =
  **+30,7% (buiten ±15%, bevinding — niet dichtgetrokken)**; profiel
  `lithium-bougouni-yangpu-plant-sanpedro` (`maak_stroombeen_weg.py`, extracts mali + ivoorkust,
  corridorKlassen tertiary/unclassified). De via-punten uit §4 gaven zelf al ~1.014 km hemelsbreed
  (brief §7), dus de gevolgde weggeometrie ligt zowel boven de gepubliceerde 880 km als boven die
  hemelsbreed-som — het Ivoriaanse tracé blijft onbevestigd.
- **b2 (zee, San Pedro → Yangpu-zeeknoop):** 17.698,8 km, MARNET-route via Kaap de Goede Hoop. San
  Pedro snapt op 1,58 km van de dichtstbijzijnde zeeknoop (geen aanloop nodig). Dit ligt **+18,0%**
  boven de briefschatting van ~15.000 km (bevinding — die schatting was zelf geen onafhankelijke
  bron, alleen een verwachting van de MARNET-meting).
- **b3 (zee, stippel, haven-aanloop Yangpu):** 20,4 km over water (`maak_havenaanloop.py`,
  omwegfactor 1,054, 0 km landkruising). **Correctie op de briefschatting van "~25 km":** de gemeten
  zeeknoop-afstand tot de Yangpu-kade is **19,38 km** — onder de 25 km-afbreekgrens van
  `--max-snap`, maar nog ruim boven de 5 km-naadnorm van de toets, dus toch een aparte aanloop nodig
  (Hainan heeft geen AIS, dus de rechte-pad-over-water-terugval is aanvaardbaar, zoals de brief al
  voorzag).
- **b4 (truck, Yangpu-kade → Xingzhihai):** 10,2 km, **doorgetrokken — geen stippel nodig**, anders
  dan de briefaanname ("net reikt niet"): de china-extract heeft wél een havenweg/estateweg binnen
  de Yangpu New Materials Industrial Park die beide onzekere ankers verbindt (profiel
  `lithium-bougouni-yangpu-yangpu-xingzhihai`, corridorKlassen tertiary/unclassified/residential/
  service). Gemeten 9,4 km weggeometrie tegen de schatting van 5-10 km = +17,5%, binnen de
  bandbreedte van de schatting zelf. "Onzeker" staat in de ankernamen/marker (brief §3), niet in de
  lijnstijl.

**Toets:** naden 1,58 / 0,00 / 0,00 km (San Pedro-zeeknoop-snap ruim onder de 5 km-norm, de overige
twee naden 0,000 km na het herdraaien van de haven-aanloop in reisvolgorde — zie gereedschapslessen);
alle 4 markers op 0,000 km van hun lijn; `toets_knikken.py` geeft 27 knikken ≥60° waarvan **0
omkeringen en 0 terugloop** (de enige klasse die gerepareerd hoort te worden); `toets_rechte_benen.py
--min-km 5` geeft geen treffer voor deze stroom (de haven-aanloop heeft een omwegfactor van 1,054,
geen rechte lijn); json: versie 2, punt_formaat lonlat, modaliteiten {truck, zee}, elk been ≥2
punten, bestand 219,5 KB.

**Gereedschapslessen:**
- De briefschatting "Yangpu ligt ~25 km van de dichtstbijzijnde zeeknoop" bleek bij meting 19,38 km
  — onder de `--max-snap`-afbreekgrens van 25 km, maar nog ruim boven de 5 km-naadnorm van de toets.
  `--been zee` tekent de lijn NIET door tot de opgegeven kade-coördinaat zodra de snap-afstand
  meerdere km bedraagt (het been eindigt letterlijk op de gesnapte zeeknoop, `connector: 0.000` in
  de console) — een haven-aanloop blijft dus nodig zodra de naad de 5 km-norm overschrijdt, ook als
  de afstand onder de 25 km-afbreekgrens ligt.
- `maak_havenaanloop.py --van/--naar` schrijft de geometrie letterlijk in díe volgorde weg; voor de
  reisvolgorde in `hecht_marnet.py route` moet de uitvoer van zeeknoop → kade lopen (niet
  kade → zeeknoop), anders ontstaat een omgekeerde naad ter grootte van de oorspronkelijke
  snap-afstand. Eerste poging (`--van` kade `--naar` zeeknoop) gaf een naad van 19,376 km tussen de
  aanloop en het truckbeen erna; herdraaien met omgewisselde `--van`/`--naar` loste het op.
- Been b3 (Yangpu-kade → Xingzhihai) bleek geen stippel nodig te hebben: de briefaanname ("net
  reikt niet") was voorzichtig, maar de china-extract bevat wél een havenweg/estateweg binnen de
  Yangpu New Materials Industrial Park. Eerst `maak_stroombeen_weg.py --bron geofabrik` proberen
  vóórdat een stippel wordt aangenomen, ook bij twee onzekere ankers.

**Open blijft:** de twee onzekere Yangpu-ankers (kade en fabriek) zijn niet satelliet- of
registerbevestigd binnen deze sessie (brief §7, MEE-registerendpoint recent verhuisd); het
Ivoriaanse tracé van b1 blijft onbeslisbaar zonder extra bron.
