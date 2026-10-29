# Routebrief (licht) · nikkel — Zapolyarny (Pechenga) → Kola → Monchegorsk (Rusland)

**stroom-id:** `nikkel-zapolyarny-monchegorsk` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** koper-nikkelconcentraat van de Zapolyarny-concentrator (Kola MMC / Nornickel, Pechenga-district) gaat per **spoor** over de Pechenga-tak (OSM-relatie "Кола - Никель") naar het knooppunt Kola bij Moermansk en verder over de Oktoberspoorweg via Olenegorsk naar de metallurgie in Monchegorsk (Severonickel). **Aannemelijk: één bron voor de bestemming.**
**Welke as van het verhaal:** de mijnzijde van Kola, eindelijk als eigen keten: sinds de sluiting van de smelter in Nikel (23-12-2020) moet het Pechenga-concentraat naar Monchegorsk. Jaarvolume per route niet gepubliceerd; context: Zapolyarny-erts ~6 Mt/j (doel 7 Mt/j in 2030) [1], Severonickel-raffinage 145 kt Ni/j capaciteit (sitelaag-peiljaar 2024, [6]), Nornickel-groep 205 kt Ni (2024) [7].

## 1 · Ketenkaart
```
Zapolyarny-concentrator `ni-zapolyarny-concentrator` ──(b1 spoor · Pechenga-tak Zapolyarny–Titovka–Kola, daarna Murmansk-lijn Kola–Olenegorsk–Monchegorsk · 284,1 km, één run, geen via-punten)──► Severonickel `ni-monchegorsk-severonickel` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Zapolyarny-concentrator → Severonickel Monchegorsk (aannemelijk: één bron) | OSM-relatie Кола - Никель (Pechenga-tak) → knooppunt Kola (route-km ~153) → Murmansk-lijn → Olenegorsk-zone (km ~250) → Monchegorsk | 284,1 eigen OSM-route; hemelsbreed 185,6 km, **geen gepubliceerde spoorkm** | `BAKE_SUFFIX=-raw toets_spoorroute.mjs`, één run | nee |
Totaal 284,1 km, snap 0,36 km (routeerpunt Zapolyarny) en 0,23 km (Severonickel), 0 bochten >= 60 graden. Er is geen spoorkilometer gepubliceerd voor deze relatie: de ±15%-toets is een indicatie (verhouding 1,53 op de grootcirkel: de route loopt van Zapolyarny zuidoost naar Kola en daarna zuid langs de Murmansk-lijn, geen rechte lijn). Geen last-mile-been en geen stippel: de 1-op-1-netten snappen binnen 0,4 km van beide uiteinden.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-zapolyarny-concentrator` | laadplek (concentrator, kop spoor) | Zapolyarny-concentrator, Kola MMC | 69.4090, 30.7890 | [2][3][4], eigen satellietblik | **aannemelijk** (z15 gezien: groot fabriekscomplex met hallen, bandbruggen en een spoorbundel van enkele sporen direct oost, tailingsvijvers ZW; geen naambord, de bronnen noemen alleen "ore-dressing plant in Zapolyarny") |
| routeerpunt (geen anker) | spoorsnap kop | Zapolyarny stad/station | 69.4167, 30.8000 | Wikipedia-coordinaat van de stad [8] | alleen routeerpunt: 69.4090,30.7890 gaf 1 omkering |
| `ni-monchegorsk-severonickel` | losplek/raffinaderij | Severonickel-fabriek (Kola MMC), Monchegorsk | 67.9195, 32.8320 | hergebruikt letterlijk uit `nikkel-norilsk-monchegorsk` [9] | bron-gelegd (daar z16 gezien) |
Het sitelaag-punt `w-kola-severonickel` (67.922, 32.825) ligt ~0,4 km ten noordwesten van dit anker: niet verschuiven (centraal).

## 4 · Via-punten
Geen. Bindende toets: een spoorbeen, een run, geen via-punten; de vrije Dijkstra rijdt de Pechenga-tak naar Kola en de Murmansk-lijn naar Monchegorsk (gemeten: route passeert 68.8627,32.9997 bij km ~153 en 68.1425,33.3107 bij km ~250). Er is geen corridorkeuze die een via-punt rechtvaardigt.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Zapolyarny-concentrator | Kola MMC (Nornickel) | erts Pechenga-mijnen (25 km strook Nikel–Zapolyarny) → Cu-Ni-concentraat | erts ~6 Mt/j [1]; concentraattonnage niet gepubliceerd | [1][2] |
| Severonickel, Monchegorsk | Kola MMC (Nornickel) | matte en concentraat → elektrolytisch nikkel (tankhouses) | 145 kt Ni/j (sitelaag, [6]) | [5][6] |

## 6 · Stoppunt
Severonickel Monchegorsk: een bron (Arctic Today, juli 2026 [1]) noemt Monchegorsk als bestemming van het Zapolyarny-concentraat; geen bron noemt een volgende fabriek per lading (D/E vervalt). Het eindproduct (nikkelkathode) is al beschreven in `nikkel-norilsk-monchegorsk`.

## 7 · Open punten
- **Bestemming één bron, vervoerswijze niet gebronnen.** Arctic Today [1]: concentraat "transported from Zapolyarny to metallurgical facilities in Monchegorsk" zonder vervoerswijze en zonder de naam Severonickel. Nornickel zegt in 2020 [3] dat concentraat naar "concentrate shipment hubs" gaat, de Kola-pagina [2] "Kola site enterprises in Russia and Finland". Spoor is afgeleid uit de infrastructuur (OSM-spoor Zapolyarny–Kola–Monchegorsk doorlopend), niet gelezen. De Finland-richting (Harjavalta) is niet getekend.
- **Concentratorlocatie aannemelijk**, niet bron-gelegd: bron plaatst de fabriek in Zapolyarny [4], het exacte terrein is satelliet-afgeleid (geen naambord).
- Een gelezen zoekresultaat meldt een in 2020 goedgekeurd project (Glavgosexpertiza) voor een concentraat-verlaad-knooppunt op het Kola MMC-terrein (200 kt droog concentraat/j, containers en wagons): bron niet zelf geopend, locatie onbekend; zou de gedeelde ladingvorm kunnen veranderen.
- Sanctierisico: de keten is Russisch en binnenlands (geen grensovergang); lees als infrastructuur, niet als gemeten lading.
- Kilometer: 284,1 km is de OSM-route, geen gepubliceerde spoorkm; 45% (131 van 284 km, Kola → Monchegorsk) loopt gelijk met `nikkel-norilsk-monchegorsk` b4 (natuurlijke gedeelde infrastructuur, geen letterlijke kopie mogelijk: b4 begint in Moermansk); ~155 km Zapolyarny–Titovka–Kola is nieuw.
- Vainikkala-fout in `nikkel-norilsk-monchegorsk` (60.86, 28.62 ligt in Rusland): niet meegenomen, melding voor centraal.

## 8 · Bronnen
[1] Arctic Today (herpublicatie Barents Observer, T. Nilsen, 2026-07-01), "Zapolyarny mine goes deeper": concentraat van Zapolyarny naar Monchegorsk; 6 Mt erts/j, doel 7 Mt 2030. https://www.arctictoday.com/zapolyarny-mine-goes-deeper-to-secure-operations-for-another-two-decades/
[2] Nornickel, Kola site: delving "25 km between Nikel and Zapolyarny", Zapolyarny Concentrator, concentraat naar Kola-vestigingen in Rusland en Finland. https://nornickel.com/business/assets/kola-division-russia/
[3] The Barents Observer, 2020-12 (Potanin, "historic event"): smelter Nikel dicht 23-12-2020, Zapolyarny-concentraat naar "concentrate shipment hubs", modernisering Monchegorsk. https://thebarentsobserver.com/en/industry-and-energy/2020/12/potanin-historic-event-nornickel
[4] ru-Wikipedia, Кольская горно-металлургическая компания: ore-dressing plant in Zapolyarny; Severonickel verwerkt matte van Pechenganickel en de Zapolyarny-afdeling. https://ru.wikipedia.org/wiki/Кольская_горно-металлургическая_компания
[5] Nornickel AR2020, Kola-Finland: Kola-raffinage verhoogt nikkelvoeding naar Harjavalta (63,4 kt in 2020). https://ar2020.nornickel.ru/en/business-overview/operational-performance/kola-finland.html
[6] Interne sitelaag `v2/design/nikkel-sitelaag.json` (site w-kola-severonickel, 145 kt Ni/j, bronnen B18/B19).
[7] Nornickel, productieresultaten 2024: 205 kt Ni; zie `nikkel-norilsk-monchegorsk` bron [3].
[8] en-Wikipedia, Zapolyarny, Murmansk Oblast (stad 69.4167, 30.8000). https://en.wikipedia.org/wiki/Zapolyarny,_Murmansk_Oblast
[9] Routebrief `nikkel-norilsk-monchegorsk` (anker Severonickel 67.9195, 32.8320 en route Kola-Monchegorsk). Zie ook `nikkel-monchegorsk-harjavalta` (Olenegorsk 68.1397, 33.2323).
[10] OpenStreetMap, spoorrelatie 1186669 "Кола - Никель" (43 leden, route=railway). https://www.openstreetmap.org/relation/1186669
[11] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-nikkel-zapolyarny-monchegorsk-zapolyarny.png` (z15), `…-zapolyarny-overzicht.png` (z14), `…-kola-overzicht.png` (z13).
[12] Interne haalbaarheidstoets `nikkel-zapolyarny-monchegorsk` (2026-10-29): proefroute 284,1 km, snaps 0,36/0,23 km, 0 bochten.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
**Bestand:** `v2/data/stroomroute-nikkel-zapolyarny-monchegorsk.json` (18,4 KB, contract versie 2, lonlat). **Recept:** `bash v2/tools/bak_stromen.sh nikkel-zapolyarny-monchegorsk` (functie `bak_nikkel_zapolyarny_monchegorsk`). **Titel:** Nikkel · Zapolyarny → Kola → Monchegorsk (Rusland).

| # | modaliteit | been | km | doorgetrokken |
|---|---|---|---|---|
| b1 | spoor | Zapolyarny-concentrator → Kola (Pechenga-tak) → Monchegorsk Severonickel (Murmansk-lijn; aannemelijk: een bron) | 285,1 (gebakken polylijn; routerkm 284,1) | ja, 1020 punten |

Totaal 285,1 km. Geen stippel, geen haven-aanloop, geen zee, geen via-punten, geen letterlijke kopie. Recept: `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=69.4167,30.8000 --naar=67.9195,32.8320 --naam=nikkel-zapolyarny-monchegorsk-zapolyarny-severonickel --hoofd-km=50 --max-snap=10` (een run, vooraf gedraaid in de brief-fase), daarna `--been-geojson` in de functie.

**Markers (2):** concentrator 69.4090,30.7890 (aannemelijk), 0,25 km van de lijnkop; Severonickel 67.9195,32.8320, 0,23 km van de lijnstaart.

**Toets (§5):** geen gepubliceerde spoorkm, dus de 15%-toets is een indicatie: 285,1 km tegen hemelsbreed 185,6 km (verhouding 1,53, verklaard door de omweg via Kola). Naden: geen (een been). `toets_knikken`: 0 knikken en 0 omkeringen. `toets_rechte_benen --min-km 5`: stroom niet gemeld. json.load: versie 2, punt_formaat lonlat, modaliteit spoor, 1020 punten.

**Lessen:** (1) het routeerpunt op de stad (69.4167,30.8000) in plaats van het fabrieksanker vermijdt de omkering aan de lijnkop; de marker blijft op het anker. (2) Tijdens het bakken gaf `bash -n` een korte syntaxfout op een regel die een andere agent op dat moment toevoegde; herhaald gaf het geen fout meer (gelijktijdige edits aan bak_stromen.sh). (3) De Vainikkala-coordinaat in nikkel-norilsk-monchegorsk (60.86, 28.62, in Rusland) blijft een melding voor centraal.
