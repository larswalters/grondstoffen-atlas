# Routebrief (licht) · uranium — Inkai (Kazachstan) → Sint-Petersburg (Rusland)

**stroom-id:** `uranium-inkai-stpetersburg` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** yellowcake (U₃O₈) van de Inkai ISR-mijn (JV Kazatomprom 60% / Cameco 40%, Turkestan-oblast) per **truck** naar het spoorstation Zhanatas — een letterlijke kopie van het eerste been van `uranium-inkai-poti` — daarna per **spoor** dwars door Kazachstan (via Astana/Petropavl, aannemelijk: geografische afleiding) de grens over, en per **spoor** dwars door Rusland (via Jekaterinenburg–Moskou, aannemelijk: geografische afleiding) naar de zeehaven van Sint-Petersburg: de historische **Ruslandroute**, tegenhanger van de Trans-Kaspische as (`uranium-inkai-poti`).
**Welke as van het verhaal:** *de Noordroute die niet gestopt is.* Historisch liep >50% van de Kazachse uraniumexport via Sint-Petersburg (WNN/Interfax, vóór 2022); Kazatomprom's FY2025-jaarverslag bevestigt dat beide routes — Trans-Kaspisch én via Rusland — "fully operational" blijven (geraadpleegd 2026-09-28), zonder een volumeverdeling te geven. Cameco (40%-JV-partner in Inkai) heeft zijn eigen gemarkete aandeel sinds de Russische invasie van 2022 wél volledig naar Trans-Kaspisch verlegd (en.wikipedia.org/wiki/Inkai) — deze as draagt dus hooguit het Kazatomprom-aandeel (60%) of niet-Cameco-gemarket materiaal, niet het Cameco-deel.

## 1 · Ketenkaart
```
Inkai MPP `u-inkai-plant` ──(b1 truck · woestijnweg Suzak-district → Zjambyl-oblast · ~290 km, aannemelijk: één bron
  — letterlijke kopie van b1 in uranium-inkai-poti)──►
Zhanatas-spoorstation `u-zhanatas-station` ──(b2 spoor · Trans-Kazachse hoofdlijn via Astana/Petropavl ·
  aannemelijk: geografische afleiding, ~2.200 km)──►
KZ–RU-grensovergang (Petropavl-regio, niet als apart anker gelegd) ──(b3 spoor · Russische hoofdlijn via
  Jekaterinenburg–Moskou · aannemelijk: geografische afleiding, ~2.800 km)──►
Sint-Petersburg-kade `u-stpetersburg-kade` ── stoppunt
```
Vervolg (niet getekend, buiten deze stroom): Sint-Petersburg → Oostzee → Deense Straten → West-Europa — de route die
sinds 2022 politiek kwetsbaar is geworden (zie `data/uranium.js`, v1: `u-port-stpetersburg → u-enr-nl`) en precies
de reden waarom de Trans-Kaspische as (`uranium-inkai-poti`) is opgebouwd.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Inkai MPP → Zhanatas-station | woestijnweg Suzak-district (Turkestan-oblast) → Zjambyl-oblast | ~290 [webcheck; geen gepubliceerde wegkm] | maak_stroombeen_weg (extract kazachstan) — **letterlijke kopie van b1 in `uranium-inkai-poti`**, hergebruik hetzelfde geojson | nee — *aannemelijk: één bron* (Cameco NI 43-101 2024, §18.2: "shipments of UOC are delivered to the Zhanatas rail station", ongeacht bestemming) |
| b2 | A | spoor | Zhanatas-station → KZ–RU-grensovergang (Petropavl-regio) | Trans-Kazachse hoofdlijn via Astana/Petropavl | ~2.200 [webcheck, geen gepubliceerde lengte] | toets_spoorroute (BAKE_SUFFIX=-raw, extract kazachstan) | nee — *(aannemelijk: geografische afleiding)* |
| b3 | A | spoor | KZ–RU-grensovergang → Sint-Petersburg-kade | Russische hoofdlijn via Jekaterinenburg–Moskou | ~2.800 [webcheck, geen gepubliceerde lengte] | toets_spoorroute (BAKE_SUFFIX=-raw, extracts rusland-oeral, rusland-centraal, rusland-noordwest) | nee — *(aannemelijk: geografische afleiding)* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-inkai-plant` | mijn/plant (laadplek, kop van b1) | Inkai MPP (hoofdverwerkingsfabriek, JV Inkai), bij Taikonur | 45.2855, 67.5255 | [1][2] — hergebruikt uit `uranium-inkai-poti` | bron-gelegd (al gelegd in `uranium-inkai-poti`: z17 gebouwencomplex met tanks en tailingsbekken) |
| `u-zhanatas-station` | overslag truck → spoor | Zhanatas-spoorstation, Zjambyl-oblast | 43.5610, 69.7260 | [1][2] — hergebruikt uit `uranium-inkai-poti` | bron-gelegd (al gelegd in `uranium-inkai-poti`: z16 stationsgebouw + rangeeryard) |
| `u-stpetersburg-kade` | overslag spoor → zee (stoppunt) | Petrolesport-containerterminal, Groot-haven van Sint-Petersburg (Gutujevski-eiland, Morskije Vorota-district) | 59.8909, 30.2376 | [3][4] | bron-gelegd (z15 gezien: rijen containerstapels, kademuren met ligplaatsen, kranen, brug/oprit naar het emplacement en spoorbundel aan de landzijde — de algemene commerciële zeehaven van Sint-Petersburg; **geen publieke bron noemt een specifiek kade-adres voor nucleaire/uraniumlading**, zie §7) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Astana (spoorknoop) | 51.1333, 71.4333 | pint de Trans-Kazachse hoofdlijn op de noordelijke tak via de hoofdstad in plaats van een westelijkere route (bv. via Aktobe–Orenburg) |
| b2 | 2 | Petropavl (grens-nabije spoorknoop) | 54.8833, 69.1667 | laatste Kazachse knoop vóór de Russische grens op deze corridor; pint de KZ–RU-grensovergang in de Petropavl-regio zoals het ketenontwerp aangeeft |
| b3 | 1 | Jekaterinenburg (spoorknoop) | 56.8356, 60.6128 | eerste grote Russische hoofdlijnknoop na de grensovergang; sluit de corridor "via Jekaterinenburg–Moskou" uit het ketenontwerp in plaats van een noordelijkere/zuidelijkere Trans-Sibirische aftakking |
| b3 | 2 | Moskou (spoorknoop) | 55.7558, 37.6178 | verplicht knooppunt tussen de Oeral-lijn en de Moskou–Sint-Petersburg-hoofdlijn; zonder dit punt kan een vrije Dijkstra een andere Russische westwaartse route naar de Oostzee kiezen |

## 5 · Verwerkingsknopen
*(geen — deze stroom bevat geen conversie/verrijking; Sint-Petersburg is een zuiver overslagpunt naar zee, geen verwerkingsknoop)*

## 6 · Stoppunt
De brief stopt bij de zeehaven van Sint-Petersburg: dat is het opgedragen keten-eindpunt (stoppunt in het ketenontwerp). De vervolgreis over de Oostzee naar West-Europese verrijking (Almelo/Tricastin, zie v1 `data/uranium.js`) is bekend maar hoort in een eigen vervolgstroom, niet in `uranium-inkai-stpetersburg` — precies zoals `uranium-inkai-poti` stopt bij Poti en niet doortekent naar Montreal.

## 7 · Open punten
- **Truck-corridor b1 is een letterlijke kopie** van `uranium-inkai-poti`-been b1 — levert geen nieuwe geometrie op; open punten van dat been (geen gepubliceerde wegroute/lengte) gelden hier onveranderd.
- **Beide spoorbenen (samen ~5.000 km) zijn "aannemelijk: geografische afleiding"**, zonder brongelegd tracé — geen bron noemt de exacte grensovergang (welke van de meerdere KZ–RU-spooraansluitingen bij/rond Petropavl) of de exacte Russische hoofdlijn. `toets_spoorroute.mjs` kiest zelf een pad tussen de via-punten in §4; dat pad kan afwijken van het historisch gebruikte tracé.
- **Geen route-specifiek of Inkai-specifiek recent tU/jaar-cijfer.** Het bewijs dat de Ruslandroute nog operationeel is, steunt op een Kazatomprom-brede uitspraak (FY2025-jaarverslag: "continues to export its products through the territory of the Russian Federation and along the Trans-Caspian International Transport Route (TITR) ... both transport routes remain fully operational", kazatomprom.kz, geraadpleegd 2026-09-28), niet op cijfers voor deze exacte as. Historisch: >50% van de Kazachse export via St. Petersburg vóór 2022 (WNN/Interfax); dat aandeel is sindsdien relatief gekrompen ten gunste van Trans-Kaspisch (>60% van de leveringen aan westerse klanten in 2023, 48% in 2025 — NucNet/Kazatomprom) maar niet naar nul.
- **Cameco-kanttekening (uit de haalbaarheidstoets, expliciet vastgelegd):** Cameco (40% JV-partner in Inkai) heeft volgens zijn eigen verklaringen zijn gemarkete aandeel sinds de Russische invasie van 2022 volledig naar de Trans-Kaspische route verlegd (en.wikipedia.org/wiki/Inkai). Materiaal op déze as is dus hooguit het Kazatomprom-aandeel (60%) of niet-Cameco-gemarket materiaal — niet noodzakelijk representatief voor de hele JV-productie.
- **Sint-Petersburg-anker is de algemene commerciële zeehaven (Petrolesport-terminal), niet een bevestigd nucleair-ladingpunt** — geen publieke bron noemt een specifiek kade-adres voor uraniumoverslag in Sint-Petersburg (vergelijkbaar met de "Waalhaven-klasse"-onzekerheid elders in het project, maar hier nooit met bronnen dichtgetrokken).
- **Sanctie-/doorvoerrisico op de Russische spoorwegen** blijft de kernkwetsbaarheid van deze as (zie ketenontwerp); dit is precies waarom de Trans-Kaspische route is opgebouwd als tegenhanger.

## 8 · Bronnen
[1] Cameco Corporation, "2024 Inkai Operation Technical Report" (NI 43-101, effectief 30-09-2024) — §18.2 UOC shipping routes, inclusief de Zhanatas-spoorstation-stap die aan beide bestemmingen (Poti en St. Petersburg) voorafgaat. https://www.cameco.com/sites/default/files/documents/Cameco-2024-Inkai-Technical%20Report.pdf
[2] Wikipedia, "Inkai Uranium Project" — JV Kazatomprom 60%/Cameco 40%, coördinaat hoofdcomplex bij Taikonyr; en.wikipedia.org/wiki/Inkai citeert Cameco's eigen aankondiging dat het na 2022 zijn eigen aandeel volledig naar de Trans-Kaspische route heeft verlegd. https://en.wikipedia.org/wiki/Inkai_Uranium_Project · https://en.wikipedia.org/wiki/Inkai
[3] OpenStreetMap (ODbL), via Photon-geocoder — "ПетроЛесПорт" (Petrolesport), industrieel havengebied, Gutujevski-eiland, Sint-Petersburg, 59.8909/30.2376. https://www.openstreetmap.org
[4] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) — `v2/build-cache/satcheck/sat-uranium-inkai-stpetersburg-petrolesport.png`.
[5] World Nuclear Association, "Uranium and Nuclear Power in Kazakhstan" — landenprofiel, exportvolumes en -routes. https://world-nuclear.org/information-library/country-profiles/countries-g-n/kazakhstan
[6] Eurasianet, jan. 2023 — "Kazakhstan moves uranium exports through Middle Corridor": beschrijft de Ruslandroute (spoor door Rusland naar St. Petersburg) als de historische hoofdroute vóór de opbouw van de Trans-Kaspische as. https://eurasianet.org/kazakhstan-moves-uranium-exports-through-middle-corridor
[7] Interfax / World Nuclear News — historisch cijfer >50% van de Kazachse uraniumexport via St. Petersburg vóór 2022 (genoemd in het ketenontwerp, secundaire vermelding via WNN/Interfax-berichtgeving).
[8] NucNet, mei 2025 — "Share Of Deliveries To Western Nuclear Firms Via Trans-Caspian Route Over 60%, Says Kazatomprom" (cijfer 2023; impliceert het resterende aandeel via de Ruslandroute). https://www.nucnet.org/news/share-of-deliveries-to-western-nuclear-firms-via-trans-caspian-route-over-60-says-kazatomprom-1-5-2025
[9] Kazatomprom, "Kazatomprom Announces 2025 Full Year Financial Results" (kazatomprom.kz, geraadpleegd 2026-09-28) — bevestigt dat zowel de Trans-Kaspische route als de route via Rusland "fully operational" zijn, geen volumepercentage per route. https://www.kazatomprom.kz/en/media/view/announces_2025_full_year_financial_results_
[10] World Nuclear News, "Kazatomprom completes trans-Caspian uranium delivery" — context voor de vergelijking tussen de twee assen. https://www.world-nuclear-news.org/Articles/Kazatomprom-completes-trans-Caspian-uranium-delive
[11] `v2/design/routebrieven/uranium-inkai-poti.md` — zusterbrief, bron voor de hergebruikte ankers `u-inkai-plant`/`u-zhanatas-station` en been b1.
[12] Wikipedia (MediaWiki API, `prop=coordinates`) — Astana 51.1333/71.4333, Petropavl 54.8833/69.1667, Jekaterinenburg 56.8356/60.6128, Moskou 55.7558/37.6178 (via-punten §4). https://en.wikipedia.org/wiki/Astana · /wiki/Petropavl · /wiki/Yekaterinburg · /wiki/Moscow

## 9 · Bak-noot (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `uranium-inkai-stpetersburg`** → `v2/data/stroomroute-uranium-inkai-stpetersburg.json` (165,5 KB) — 6 benen, **5.172,1 km**, 3 markers: truck (stippel) 259,4 km · spoor 1.423,5 km (Zhanatas→Astana) · spoor 500,1 km (Astana→Petropavl) · spoor 630,5 km (Petropavl→Jekaterinenburg) · spoor 1.679,4 km (Jekaterinenburg→Moskou) · spoor 679,2 km (Moskou→Sint-Petersburg-kade).
Recept: `bak_stromen.sh` (functie `bak_uranium_inkai_stpetersburg`). Toelichting per been:

- **b1 (truck, stippel, letterlijke kopie):** exact de bestaande stippel-regel van `uranium-inkai-poti` been b1 hergebruikt (geen nieuwe `maak_stroombeen_weg.py`-run, geen nieuw geojson) — 259,4 km, reden ongewijzigd: geen doorlopende OSM-weg over de ~290 km woestijnsteppe Suzak-district → Zjambyl-oblast (Cameco NI 43-101 §18.2, brief §7).
- **b2 (spoor, 2 deelruns, 1-op-1-net):** `BAKE_SUFFIX=-raw toets_spoorroute.mjs --van=43.5610,69.7260 --naar=51.1333,71.4333` (Zhanatas→Astana) = 1.423,5 km, en `--van=51.1333,71.4333 --naar=54.8833,69.1667` (Astana→Petropavl) = 500,1 km. Samen **1.923,6 km** tegen de webcheck-schatting van ~2.200 km (brief §2) = **−12,6%**, binnen ±15%. Eén omkering (176,2°, boogstraal ~33 m) bij 42,87120/71,38190, onderweg tussen Zhanatas en Astana — geen gepubliceerde plaatsnaam ter plekke, wel op de corridor tussen de Sjoe-lijn en de Astana-hoofdlijn.
- **b3 (spoor, 3 deelruns, 1-op-1-net):** `--van=54.8833,69.1667 --naar=56.8356,60.6128` (Petropavl→Jekaterinenburg) = 630,5 km, `--van=56.8356,60.6128 --naar=55.7558,37.6178` (Jekaterinenburg→Moskou) = 1.679,4 km, `--van=55.7558,37.6178 --naar=59.8909,30.2376` (Moskou→Sint-Petersburg-kade) = 679,2 km. Samen **2.989,1 km** tegen de webcheck-schatting van ~2.800 km (brief §2) = **+6,8%**, binnen ±15%.
- **Naad b2 ↔ b3 op het grens-via-punt (Petropavl-knoop, brief §3: "niet als apart anker gelegd"):** 0,00 km — b2 eindigt en b3 begint op exact dezelfde coördinaat (54,8833/69,1667). De KZ–RU-grensoversteek zelf heeft dus geen eigen anker gekregen (geen bron noemt het exacte grenspunt) en zit "in" deze naad, precies zoals bedoeld.
- Alle vijf spoordeelruns zijn **doorgetrokken, niet gestippeld** — beide spoorbenen zijn "aannemelijk: geografische afleiding" (brief §2/§7), en die kwalificatie staat in de beennaam, niet in de lijnstijl.
- Geen zee-been (brief §6): de keten stopt bewust bij de Sint-Petersburg-kade zelf, dus geen MARNET-zeeknoop-check of haven-aanloop nodig.
- Alle 3 markers uit §3 zijn meegenomen: `u-inkai-plant` en `u-zhanatas-station` letterlijk hergebruikt uit `uranium-inkai-poti` (geen nieuwe satellietpas), `u-stpetersburg-kade` nieuw satelliet-gelegd (z15, brief §3/[4]).

**Toets-bevindingen:**
- Alle naden tussen opeenvolgende benen liggen op **0,00–0,23 km** — ruim binnen de ≤5 km-norm.
- Beide gemeten spoorbenen liggen binnen ±15% van de eigen webcheck-schatting (−12,6% resp. +6,8%); er is geen gepubliceerde bronlengte om tegen te toetsen (brief §7), dus de gebakken km's zijn zelf de nieuwe informatie.
- Markers: Inkai MPP en Zhanatas-station liggen op ~0 m resp. ~0,23 km van hun lijn (identiek aan de naad ernaast); Sint-Petersburg-kade ligt ~0,37 km van het beeneinde (59,89410/30,23910 vs marker 59,8909/30,2376) — allemaal ruim onder de zachte 0,5 km-richtlijn.
- `toets_rechte_benen.py --min-km 5`: alleen b1 (259,4 km, omwegfactor 1,000) staat in de verdachtenlijst — dat is precies het gestippelde been, geen bevinding.
- JSON-vormtoets: `versie` 2, `punt_formaat` `lonlat`, modaliteiten {truck, spoor} (beide toegestaan), elk been ≥2 punten, bestand 165,5 KB (< 300 KB) — allemaal in orde.
- ⚠️ **`toets_knikken.py`: 6 omkeringen (≥150°), ALLE 6 door de tool gelabeld als TERUGLOOP** (verhoudingen v=29,6 · v=5,9 · v=99,0 · v=99,0 (×2) · v=99,0), dus buiten de norm uit `bak_aanwijzingen` ("prima zolang toets_knikken.py geen terugloop laat zien"). Onderzocht, niet dichtgetrokken: de vijf spoordeelruns zijn opnieuw gedraaid met `--keerstraf=100` (4× de default 25 km) — **exact dezelfde 6 locaties met dezelfde boogstraal (22–70 m)** kwamen terug, wat een tie-break-sluipweg uitsluit (die zou bij een hogere straf verdwijnen of verschuiven). De 6 punten liggen alle op of vlak bij een benoemde spoorknoop: 42,87120/71,38190 (onderweg Zhanatas→Astana, geen plaatsnaam bekend) · 54,85950/69,20790 (**vrijwel exact op Petropavl zelf**, de laatste KZ-knoop vóór de grens) · 55,76090/38,97230, 55,77390/37,55660 en 55,79260/37,64210 (**alle drie in/rond het Moskouse spoorknooppuntcomplex**) · 59,87280/30,19490 (**vlak bij de Sint-Petersburg-kade**, het eindpunt van de keten). Dit is dezelfde klasse "kopmaak op een echte junctie" als het Shalkar-knooppunt in `uranium-inkai-poti` §9 — maar hier met een verhouding ruim boven de terugloop-drempel (2,2) in plaats van eronder, dus expliciet als bevinding vastgelegd in plaats van stilzwijgend geaccepteerd. Geen via-punt is verschoven om dit te verbergen.

**Gereedschapslessen:**
- Wanneer de brief geen eigen anker voor een grensovergang legt ("niet als apart anker gelegd"), kan het laatste via-punt vóór de grens (hier Petropavl) dienstdoen als praktisch kop-/staartpunt voor de twee aangrenzende spoordeelruns — de naad daar is dan per constructie 0,00 km en de brief hoeft geen coördinaat te verzinnen voor de grens zelf.
- Een `--keerstraf`-verhoging (25 → 100 km) is een goedkope eerste test om een vermeende terugloop te onderscheiden van een tie-break-sluipweg: blijft de omkering op exact dezelfde plek met dezelfde boogstraal staan, dan is het een structureel kenmerk van de OSM-junctie (een topologische stub/kopmaak) en geen keuze van de router — geen via-punt bijschuiven, gewoon documenteren.
- De terugloop-verhouding (v) kan tot 99,0 oplopen wanneer het venster van ±8 punten vrijwel op dezelfde plek begint én eindigt (hemelsbrede afstand ≈ 0) — dat is geen "extremer" terugloop dan v=3,0, alleen een numerieke plafondwaarde van dezelfde soort artefact bij een zeer korte spike.
