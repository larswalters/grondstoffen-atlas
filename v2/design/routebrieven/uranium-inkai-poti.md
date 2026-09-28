# Routebrief (licht) · uranium — Inkai (Kazachstan) → Poti (Georgië)

**stroom-id:** `uranium-inkai-poti` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31) · **status:** gebakken
**Keten in één zin:** yellowcake (U₃O₈) van de Inkai ISR-mijn (JV Inkai: Kazatomprom 60% / Cameco 40%, Turkestan-oblast) per **truck** naar het spoorstation Zhanatas (Zjambyl-oblast — géén directe rail-aansluiting bij de mijn), per **spoor** dwars door Kazachstan naar Aktau, per **zeeschip** de Kaspische Zee over naar de Bakoe-haven bij Alyat, per **spoor** door de Kaukasus naar Poti — het Trans-Kaspische omweg-traject dat de Russische doorvoerroute (Sint-Petersburg) de-riskt.
**Welke as van het verhaal:** *Trans-Kaspische omweg om Rusland* — Kazachstan levert ~43% van de wereldmijnproductie (WNA/Kazatomprom, 2023/24: ≈21.000 tU/jaar) maar is landlocked; sinds 2022 gaat een groeiend deel van de westerse leveringen via deze Middle Corridor i.p.v. door Rusland. Kazatomprom/NucNet (2025): **>60% van de leveringen aan westerse kernenergiebedrijven** liep in 2023 via de Trans-Kaspische route (TITR); Astana Times (2024): 2.300 t uranium via Azerbeidzjan, +4,5% t.o.v. 2022.

## 1 · Ketenkaart
```
Inkai MPP `u-inkai-plant` ──(b1 truck · woestijnweg Suzak-district → Zjambyl-oblast · ~290 km hemelsbreed, aannemelijk: één bron)──►
Zhanatas-spoorstation `u-zhanatas-station` ──(b2 spoor · Trans-Kazachse lijn (Zhanatas/Shu → Kyzylorda-regio → Aral → Saksaulskaya → Beyneu) · geen gepubliceerde km)──►
Aktau-kade `u-aktau-kade` ──(b3 zee · Kaspische Zee-oversteek, MARNET · 468,1 km getest)──►
Alyat/Bakoe-kade `u-alat-kade` (geverifieerd: geen geforceerd vaarpunt nodig) ──(b4 spoor · Bakoe–Tbilisi–Poti-lijn, via Tbilisi · ~800 km, TRACECA) ──►
Poti-kade `u-poti-kade` ── stoppunt
```
Vervolg (niet getekend, buiten deze stroom): Poti → Bosporus → Middellandse Zee → Atlantische Oceaan → **Montreal** → Cameco Blind River Refinery (Ontario) — voor het eerst met havenprecisie gevonden (Cameco 2024 Inkai NI 43-101 Technical Report §18.2), maar dat is een vervolgstroom, geen onderdeel van `uranium-inkai-poti`.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Inkai MPP → Zhanatas-station | woestijnweg Suzak-district (Turkestan-oblast) → Zjambyl-oblast | ~290 [webcheck; geen gepubliceerde wegkm] | maak_stroombeen_weg (extract kazachstan) | nee — *aannemelijk: één bron* (Cameco 2024, §18.2: "shipments of UOC are delivered to the Zhanatas rail station") |
| b2 | A | spoor | Zhanatas-station → Aktau-kade | Trans-Kazachse lijn: Zhanatas/Shu-knoop → Kyzylorda-regio → Aral → Saksaulskaya → Beyneu → Mangystau-tak | geen gepubliceerd [1-op-1-net meet het] | toets_spoorroute (BAKE_SUFFIX=-raw, extract kazachstan) | nee |
| b3 | A | zee | Aktau-kade → Alyat/Bakoe-kade | Kaspische Zee-oversteek (TITR/Middle Corridor) | 468,1 [webcheck, hecht_marnet.py] | MARNET | nee — geverifieerd: geen geforceerd vaarpunt nodig |
| b4 | A | spoor | Alyat/Bakoe-kade → Poti-kade | Bakoe–Tbilisi–Poti-spoorlijn (Kaukasus-doorsteek), via Tbilisi | ~800 [TRACECA: Poti-Baku Container Block Train, totale lengte] | toets_spoorroute (BAKE_SUFFIX=-raw, extracts azerbeidzjan + georgie) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-inkai-plant` | mijn/plant (laadplek, kop van b1) | Inkai MPP (hoofdverwerkingsfabriek, JV Inkai), bij Taikonur | 45.2855, 67.5255 | [2][3][11] | bron-gelegd (z17 gezien: gebouwencomplex met blauwe/gele daken, tanks, wegverharding en een verdampings-/tailingsbekken 500 m ZO; Wikipedia-coördinaat 45.28222/67.53667 lag 1,1 km ernaast, midden in de wellfield-sporen — hier verschoven naar het echte gebouwencomplex) |
| `u-zhanatas-station` | overslag truck → spoor | Zhanatas-spoorstation, Zjambyl-oblast | 43.5610, 69.7260 | [3][12] | bron-gelegd (z16 gezien: stationsgebouw + rangeeryard met meerdere sporen aan de rand van de stad Zhanatas, naast de bekende fosfaatmijn-put) |
| `u-aktau-kade` | overslag spoor → zee | Aktau-zeehaven (Kazmortransflot-terrein), Kazachstan | 43.6005, 51.2287 | [4][13] | bron-gelegd (z15 gezien: havenbekken met golfbrekers, aanlegsteigers, tankopslag en spoorbundel aan de kade) |
| `u-alat-kade` | overslag zee → spoor | Bakı Dəniz Ticarət Limanı (Baku International Sea Trade Port), Alyat, Qaradağ | 39.9764, 49.4408 | [1][5][13] | bron-gelegd (z16 gezien: kadewand met containers, ferry-/ro-ro-hellingbaan, golfbreker en schip aan de kade — de moderne vervanger (2018) van de oude Baku-stadskade) |
| `u-poti-kade` | overslag spoor → zee (stoppunt) | Poti Sea Port, Georgië | 42.1550, 41.6560 | [6][13] | bron-gelegd (z15 gezien: kademuur met kranen, tankopslag, havenbekken met golfbrekers aan de rivier-monding) |

## 4 · Via-punten (alleen b4 — corridorkeuze Bakoe–Tbilisi vs. Bakoe–Kars)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|
| b4 | 1 | Tbilisi (spoorknoop) | 41.7151, 44.8271 | hier splitst de Zuid-Kaukasus-spoorlijn: de Bakoe–Tbilisi–Kars-lijn (naar Turkije) tegenover de doorgaande lijn naar Poti/Batumi — zonder dit punt kan een vrije Dijkstra de Kars-tak nemen |

## 5 · Verwerkingsknopen
*(geen — deze stroom bevat geen conversie/verrijking; Poti is een zuiver overslagpunt, geen verwerkingsknoop)*

## 6 · Stoppunt
De brief stopt bij Poti: dat is het opgedragen keten-eindpunt. De daadwerkelijke vervolgreis (Bosporus → Middellandse Zee → Atlantische Oceaan → Montreal → Cameco Blind River Refinery) staat wél met havenprecisie in Cameco's eigen NI 43-101-rapport van 2024 [3] — een nieuwe, sterkere bron dan de oorspronkelijke ketendefinitie aannam — maar hoort in een eigen vervolgstroom, niet in `uranium-inkai-poti`.

## 7 · Open punten
- **Truck-corridor b1 (Inkai → Zhanatas, ≈290 km) heeft geen gepubliceerde wegroute of lengte** — alleen het feit dát er getruckt wordt naar Zhanatas staat gebrond [3]; de weg zelf (klasse, via-punten) moet bij het bakken uit OSM/Geofabrik komen en kan `corridorKlassen`/langere `vensterKm` vragen (woestijnsteppe, weinig hoofdwegen).
- **Spoorcorridor b2 (Zhanatas → Aktau) is niet stap-voor-stap gebrond** — de aannemelijke route loopt via de Shu-aansluiting en de Trans-Aral-lijn (Kyzylorda–Aral–Saksaulskaya–Beyneu–Mangystau), maar geen bron noemt de tussenstations; lengte volgt uit het 1-op-1-spoornet, niet uit een publicatie. Dit is een aanmerkelijk langere/anders gevormde route dan de oorspronkelijke ketendefinitie ("Kyzylorda–Beyneu–Aktau" rechtstreeks vanaf de mijn) veronderstelde.
- **Aandeel Inkai specifiek in een zending is niet gepubliceerd** — de 2022/2023-zendingen worden in de bronnen als "Kazatomprom + JV Inkai gezamenlijk" genoemd, zonder tU-verdeling per partner.
- **Baku/Alyat-kade ligt 49,4 km van de dichtstbijzijnde MARNET-zeeknoop** (getest, ruim boven de norm van 25 km) → vraagt een haven-aanloop (`maak_havenaanloop.py`, zoals bij Matarani/San Antonio) bovenop het geverifieerde Aktau–Alyat-zeebeen van 468,1 km.
- **Reserve-as:** de Rusland-route (Sint-Petersburg) blijft operationeel en goedkoper zolang er geen sancties op Kazachs uranium liggen — dit is een de-riskingroute naast, niet in plaats van, de Noord-route.

## 8 · Bronnen
[1] World Nuclear News, 2022/2023 — "Kazatomprom completes trans-Caspian uranium delivery": route via TITR, aankomst Poti, verlading op gecharterd schip naar een Canadese haven; JV Inkai-aandeel (Cameco 40%). https://www.world-nuclear-news.org/Articles/Kazatomprom-completes-trans-Caspian-uranium-delive
[2] Wikipedia, "Inkai Uranium Project" — coördinaat 45°16'56"N 67°32'12"E, JV Kazatomprom 60%/Cameco 40%, hoofdcomplex bij Taikonyr. https://en.wikipedia.org/wiki/Inkai_Uranium_Project
[3] Cameco Corporation, "2024 Inkai Operation Technical Report" (NI 43-101, effectief 30-09-2024) — §4.1 locatie (45°20'N/67°30'E, Suzak-district); §5.1 toegang (geen spoor tot Taikonur, alleen wegtransport); §18.2 UOC shipping routes: "shipments of UOC are delivered to the Zhanatas rail station in Kazakhstan and then moved to the port of Aktau... to the port of Alyat near Baku... to the Black Sea port of Poti, Georgia... through the Bosporus Strait... to the port of Montreal before delivery to Cameco's Blind River Refinery." https://www.cameco.com/sites/default/files/documents/Cameco-2024-Inkai-Technical%20Report.pdf
[4] Wikipedia/SeaRates, "Aktau" (haven) — 43.60049°N, 51.22873°E, UN/LOCODE KZAAU, grootste haven van Kazachstan. https://en.wikipedia.org/wiki/Aktau
[5] EVRASCON / TRACECA, "New Baku International Sea Trade Port" — greenfield-terrein bij Alyat (Qaradağ), 70 km zuid van Baku, geopend 2018, 12 ligplaatsen. https://evrascon.com/en/our-projects/new-baku-international-sea-trade-port/
[6] Wikipedia/SeaRates, "Poti Sea Port" — 42.155°N/41.656°E, grootste haven van Georgië, beheerd door APM Terminals. https://en.wikipedia.org/wiki/Poti_Sea_Port
[7] TRACECA, "Poti-Baku Container Block Train" — totale lengte 800 km, Poti Sea Port (Georgië) naar Baku Sea Port (Azerbeidzjan). https://traceca-org.org/en/investments/investment-projects/detail/?tx_tracecainvprojectstable_pi3%5Buid%5D=31
[8] Eurasianet, jan. 2023 — "Kazakhstan moves uranium exports through Middle Corridor": TITR sinds 2018 als alternatief voor de Sint-Petersburg-route; dispatch eind sept. 2022, aankomst Canadese haven medio dec. 2022. https://eurasianet.org/kazakhstan-moves-uranium-exports-through-middle-corridor
[9] NucNet, mei 2025 — "Share Of Deliveries To Western Nuclear Firms Via Trans-Caspian Route Over 60%, Says Kazatomprom" (cijfer 2023). https://www.nucnet.org/news/share-of-deliveries-to-western-nuclear-firms-via-trans-caspian-route-over-60-says-kazatomprom-1-5-2025
[10] Astana Times, 2024 — Kazachstan verhoogt uraniumzendingen via TITR: 2.300 t via Azerbeidzjan in 2024, +4,5% t.o.v. 2022, bestemmingen o.a. Frankrijk/Canada/Roemenië/India/VS. https://astanatimes.com/2024/05/kazakhstan-increases-uranium-shipments-via-trans-caspian-international-transport-route
[11] OpenStreetMap/Nominatim (ODbL) — plaats Тайқоңыр 45.2099/67.5336 (hamlet, Suzak-district), 8,4 km zuid van het ankerpunt, consistent met "MA Area ligt bij Taikonur". https://www.openstreetmap.org
[12] OpenStreetMap/Nominatim (ODbL) — stad Жаңатас 43.5568/69.7266 (Sarysu-district, Zjambyl-oblast). https://www.openstreetmap.org
[13] Esri World Imagery via `v2/tools/sat_check.py` (z15–z17, live) — `v2/build-cache/satcheck/sat-uranium-inkai-poti-inkai-final.png`, `sat-uranium-inkai-poti-zhanatas2.png`, `sat-uranium-inkai-poti-aktau.png`, `sat-uranium-inkai-poti-alat2.png`, `sat-uranium-inkai-poti-poti.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze)

**Stroom `uranium-inkai-poti`** → `v2/data/stroomroute-uranium-inkai-poti.json` — 6 benen. 3.973,1 km. 5 markers: truck (stippel) 259,4 km · spoor 2.417,1 km · zee 468,1 km · zee (stippel) 49,4 km · spoor 470,9 km · spoor 308,2 km.
Recept: `bak_stromen.sh` (functie `bak_uranium_inkai_poti`). Toelichting per leg:
- **b1 (truck, stippel):** `maak_stroombeen_weg.py --profiel uranium-inkai-poti-inkai-zhanatas` (venster 75 km, extract `kazachstan`, geen via-punten) meldde *"geen wegpad tussen punt 0 en 1"* — geen doorlopende OSM-weg over de ~290 km woestijnsteppe Suzak-district → Zjambyl-oblast. Geen tweede poging; rechte stippel, 259,4 km (grootcirkel, korter dan de ~290 km hemelsbreed uit de brief omdat dat cijfer een ruwere schatting was).
- **b2 (spoor, 1-op-1-net):** `BAKE_SUFFIX=-raw toets_spoorroute.mjs --van=43.5610,69.7260 --naar=43.6005,51.2287 --hoofd-km=1000` → 2.407,0 km (tool), 2.417,1 km gebakken (naad-verschil, zie hieronder). **Geen gepubliceerde lengte om tegen te toetsen (brief §7) — dit is nieuwe informatie.** Eén omkering (179,7°, boogstraal ~118 m) bij 47,8187/59,6491 = het spoorknooppunt **Shalkar** op de Trans-Aral-lijn (Aral → Shalkar → Beyneu) — een kopmaak op een echte junctie, geen verzonnen sluiproute (verhouding route/grootcirkel 1,62; de route dipt eerst zuidwaarts naar de Shu/Turkestan-mainline vóór hij westwaarts via Kyzylorda/Aral/Shalkar/Beyneu naar Mangystau/Aktau buigt — geografisch aannemelijk, geen bron noemt de tussenstations).
- **b3 (zee):** MARNET Aktau-kade → Alyat-zeeknoop (40,21240/49,93290) = 468,1 km, **exact** de al vooraf getoetste waarde (brief §2). Aktau snapt automatisch op 7,4 km (< 25 km-norm); Alyat-kade zelf ligt op 49,4 km, dus het hoofdzeebeen eindigt op de zeeknoop.
- **b3b (haven-aanloop Alyat, stippel):** `maak_havenaanloop.py --van 39.9764,49.4408 --naar 40.21240,49.93290` liep vast op `timeout 300` (exit 124). Geen tweede poging — rechte stippel, 49,4 km.
- **b4 (spoor, 1-op-1-net, twee runs via Tbilisi):** Alyat → Tbilisi 465,1 km (tool) / 470,9 km (gebakken) + Tbilisi → Poti 303,1 km (tool) / 308,2 km (gebakken) = **779,1 km gebakken** tegen de TRACECA-schatting van 800 km (Poti-Baku Container Block Train) = **−2,6%**, ruim binnen ±15%. Zonder het Tbilisi-via-punt kan een vrije Dijkstra bij Tbilisi de Bakoe–Tbilisi–Kars-lijn (Turkije) nemen i.p.v. de doorgaande lijn naar Poti.
- Alle 5 markers uit §3 zijn meegenomen; geen fase D/E (Poti is een zuiver overslagpunt, brief §5/§6).

**Toets-bevindingen (buiten de norm, niet dichtgetrokken):**
- **Naad been 2→3 (spoor → zee) = 6,80 km** — boven de norm van ≤5 km. De spoorlijn eindigt op de Aktau-kade zelf, het zeebeen begint op de MARNET-zeeknoop 7,4 km verderop (§2 van de brief noemt deze snap-afstand al). Anker ≠ routeerpunt; niet dichtgetrokken.
  > **Bijgewerkt 2026-09-28 (LAR-586):** alsnog dichtgezet met een haven-aanloop Aktau. `maak_havenaanloop.py` liep vast op `timeout 300` (exit 124), dus een rechte stippel van 7,4 km (kade → zeeknoop 9455), geen tweede poging. De resterende naad spoor → aanloop is 0,6 km (spoorsnap). Keten nu 3.980,5 km in zeven benen.
- **Marker Aktau-zeehaven ligt 587,9 m van de lijn** — iets boven de zachte richtlijn van ~0,5 km, verklaard door dezelfde spoor↔zeeknoop-snap (het anker ligt tussen de twee eindpunten van been 2 en been 3 in). De overige 4 markers liggen op 0–33 m.
- **"Gebakken" km ligt 8-10 km hoger dan wat `toets_spoorroute.mjs` zelf rapporteert** voor elk van de drie spoorbenen (b2: 2.407,0 → 2.417,1; b4a: 465,1 → 470,9; b4b: 303,1 → 308,2) — een bekend, klein verschil tussen de router-uitvoer en de door `hecht_marnet.py` herberekende som van de vooraf gebakken lijn (naden/afronding), geen fout in de geometrie zelf.
- `toets_knikken.py`: 4 knikken ≥60°, waarvan 2 omkeringen (≥150°), **0 terugloop** — de enige categorie die reparatie zou vragen. Beide omkeringen zijn echte spoorknopen (Shalkar op b2; een scherpe bocht bij 39,9713/49,3993 op b4a, dicht bij de Bakoe-kade — kopmaak-achtig emplacementsgedrag, geen sluipweg).
- `toets_rechte_benen.py --min-km 5`: beide rechte legs (b1 259,4 km; b3b 49,4 km) staan terecht in de verdachtenlijst als **stippel** — dat is precies waarom ze gestippeld zijn, geen bevinding.
- JSON-vormtoets: `versie` 2, `punt_formaat` `lonlat`, modaliteiten {truck, spoor, zee} (alle toegestaan), elk been ≥2 punten, bestand 90,2 KB (< 300 KB) — allemaal in orde.

**Gereedschapslessen:**
- Een `maak_stroombeen_weg.py`-profiel met een ruim venster (75 km) en geen via-punten kan alsnog "geen wegpad" opleveren als er over honderden kilometers steppe/woestijn simpelweg geen doorlopende OSM-weg van de juiste klasse ligt — dit is de eerste stroom van het project waar dat voor een héél been (niet alleen een last-mile-stukje) gebeurt.
- `maak_havenaanloop.py` timede voor het eerst uit op een Kaspische kust in plaats van een Atlantische/Pacifische — de 300 s-grens en de "geen tweede poging"-regel golden hier onveranderd.
- De omkering bij Shalkar (47,8187/59,6491) is het eerste voorbeeld in dit project van een `toets_knikken.py`-omkering die overeenkomt met een **benoemd, bekend spoorknooppunt** op een geïsoleerd continentaal net — een nuttige tegenhanger van de eerdere Norilsk/Moermansk-emplacementsvoorbeelden.
