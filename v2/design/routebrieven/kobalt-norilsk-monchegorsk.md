# Routebrief (licht) · kobalt — Norilsk → Dudinka → Moermansk → Monchegorsk (Kola-kobaltwerkplaats, Rusland)

**stroom-id:** `kobalt-norilsk-monchegorsk` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** converter-matte van de Nadezhda-smelter (Norilsk, Nornickel Polar Division) gaat per **spoor** over het geïsoleerde Norilsk-industrienet naar Dudinka, per **binnenvaart** de Jenisej af naar de Jenisej-golf, per **zee** (eigen Arc7-ijsbrekervloot, jaarrond, Karskiye Vorota) naar Moermansk en per **spoor** naar Monchegorsk, waar Kola MMC in de kobaltafdeling van de nikkelelektrolyse metallisch kobalt 99,9% maakt (**aannemelijk: één bron** dat dit kobalt uit Norilsk-matte komt).
**Welke as van het verhaal:** *de enige Russische kobaltproducent, aan de Arctische keten.* Kola MMC hervatte op 8-12-2025 de kobaltwerkplaats: tot **3,0 kt Co/j** metallisch kobalt 99,9% (capaciteit, geen productie; 5,3 mld roebel geïnvesteerd) [1]; vóór de brand van sept. 2022 was dat 2,5 kt/j, daarna ca. 1,0 kt/j uit concentraat [1][2]. Werkelijke 2025-output is niet gepubliceerd. **Deze lijn is een letterlijke kopie van `nikkel-norilsk-monchegorsk` (b1–b5)** — zelfde matte, zelfde route; het verhaal verschilt (kobalt-afdeling), de geometrie niet. Geen Harjavalta/Finland-vertakking.

## 1 · Ketenkaart
```
Nadezhda-fabriek `co-nadezhda-fabriek` ──(b1 spoor · Norilsk-industrienet via Kajerkan · 78,0 km)──► Dudinka-kade `co-dudinka-kade`
  ──(b2 binnenvaart · Jenisej, bulklaag · 430,2 km)──► bulk-knoop Jenisej-golf (71.8288, 82.7783)
  ──(b3 zee, stippel · naad rivier↔zeeknoop 2338 · 20,2 km)──► MARNET-zeeknoop 2338 (71.9829, 82.4669)
  ──(b4 zee · Karazee → Karskiye Vorota → Barentszzee · 2.124,5 km, aannemelijk)──► Moermansk-terminal `co-moermansk-terminal`
  ──(b5 spoor · Oktoberspoorweg Moermansk–Kola–Olenegorsk–Monchegorsk · 145,7 km, aannemelijk)──► Kola MMC `co-monchegorsk-kola` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `co-nadezhda-fabriek` → `co-dudinka-kade` | Norilsk-industriespoor Norilsk → Kajerkan → Dudinka (geïsoleerd net) | 78,0 (gemeten, 1-op-1-net) [8] | **kopie** nikkel b1: `spoorroute-nikkel-norilsk-monchegorsk-nadezhda-dudinka.geojson` | nee |
| b2 | B | binnenvaart | `co-dudinka-kade` → bulk-knoop Jenisej-golf | Jenisej stroomafwaarts (bulklaag: ligging van het water, geen bevaarbaarheidsbewijs) | 430,2 (gemeten) [8] | **kopie** nikkel b2: `nikkel-norilsk-monchegorsk-rivier-dudinka-bulkknoop.geojson` | nee |
| b3 | B | zee | bulk-knoop → zeeknoop 2338 | naad rivier↔MARNET (20,2 km > 5 km-norm) | 20,2 (gemeten naad) [8] | **kopie** nikkel b3: `--stippel "zee\|…\|71.82880,82.77830\|71.9829,82.4669"` | **ja** — net reikt niet |
| b4 | B | zee | zeeknoop 2338 → `co-moermansk-terminal` | Karazee → Karskiye Vorota → Barentszzee; Arc7-ijsbrekers jaarrond [5][8] | 2.124,5 (MARNET) [8] | **kopie** nikkel b4: `--been "zee\|…\|71.9829,82.4669\|68.9737,33.0658"` — beennaam **(aannemelijk: één bron)** | nee |
| b5 | C | spoor | `co-moermansk-terminal` → `co-monchegorsk-kola` | Oktoberspoorweg Moermansk → Kola → Olenegorsk → Monchegorsk | 145,7 gemeten tegen 142,1 gepubliceerd (+2,5%) [8] | **kopie** nikkel b5: `spoorroute-nikkel-norilsk-monchegorsk-moermansk-severonickel.geojson` — beennaam **(aannemelijk: één bron)** | nee |

Geen last-mile-been: het spoor reikt tot 0,23 km van het Kola-anker (gemeten in de nikkelbak [8]). Haven-aanloop Moermansk: kade ligt 1,2 km van zeeknoop 6906 (≤ 5 km) → geen aanloop.

## 3 · Ankers (één per site en per overslag — letterlijk hergebruikt uit `nikkel-norilsk-monchegorsk` §3)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-nadezhda-fabriek` | smelter / kop spoor | Nadezhda Metallurgical Plant, Norilsk | 69.3275, 87.9521 | [3][8] (nikkelbrief, z15 gezien: groot fabriekscomplex met rookpluim, spoorbundel ten westen) | bron-gelegd (hergebruikt) |
| `co-dudinka-kade` | overslag spoor→binnenvaart | Dudinka-havenkade, Jenisej | 69.4030, 86.1680 | [8] (z17 gezien: kadekranen langs de oever, spoor erlangs) | bron-gelegd (hergebruikt) |
| `co-moermansk-terminal` | overslag zee→spoor | Nornickel Murmansk Transport Division, Портовый проезд 31/1 | 68.9737, 33.0658 | [8][9] adres uit bedrijvenregister; geen Nornickel-kenmerk van buurbedrijf te onderscheiden | **aannemelijk** (hergebruikt) |
| `co-monchegorsk-kola` | losplek / kobaltwerkplaats | Kola MMC, Monchegorsk (Severonickel-terrein; kobaltafdeling in de nikkelelektrolyse) | 67.9195, 32.8320 | [1][3][8] | bron-gelegd (z15 eigen blik 2026-10-09: ruim fabrieksterrein met elektrolyse-/smelterhallen, tanks en schoorstenen ten zuiden en een uitgebreide spoorbundel ten oosten; kruis ligt aan de noordrand op het emplacement. De kobaltafdeling zelf is niet aan te wijzen — ze zit in hetzelfde complex) |

Zeeknoop 2338 (71.9829, 82.4669) en bulk-knoop (71.8288, 82.7783) zijn naadpunten van de kopieën, geen ankers/markers van deze stroom.

## 4 · Via-punten
Geen. De landbenen zijn letterlijke kopieën van gemeten spoorbenen (geen wegbeen, geen nieuwe corridorkeuze); de zee-leg wordt door MARNET gerouteerd.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Nadezhda Metallurgical Plant, Norilsk | Nornickel Polar Division | erts/concentraat Talnakh → converter-matte | groepscijfer, niet apart voor Co gepubliceerd | [3][8] |
| Kola MMC, Monchegorsk — kobaltwerkplaats | Nornickel (Kola MMC) | kobaltconcentraat uit de nikkelelektrolyse → metallisch kobalt 99,9% (chloride-extractie-elektrolyse) | tot **3,0 kt Co/j** (capaciteit na herstart 8-12-2025); 2,5 kt/j voor brand 2022; ~1,0 kt/j tussentijds | [1][2][3] |

## 6 · Stoppunt
De keten stopt bij de Kola-kobaltwerkplaats: Interfax noemt de Russische industrie als afnemer maar geen afnemer met naam of adres [2], dus fase D/E vervalt. Metallisch elektrolytkobalt is het eindproduct.

## 7 · Open punten
- **Voeding niet voor kobalt apart bewezen.** Interfax noemt alleen "cobalt concentrate" als bron [1][2]; Barents Observer zegt dat het complex ertsconcentraat van Zapolyarny én matte van Nadezhda verwerkt en dat de brand in de kobaltafdeling van elektrolysewerkplaats 2 begon [3]. Dat de kobaltstroom uit Norilsk-matte komt (via dezelfde Dudinka–Moermansk–Monchegorsk-keten) is **aannemelijk, één bron**, niet bewezen; ook Kola's eigen Zapolyarny-concentraat [4] kan de voeding zijn. Daarom `(aannemelijk: één bron)` in de beennamen b4/b5.
- Werkelijke 2025-output niet gepubliceerd; 3,0 kt Co/j is capaciteit (gloedgewicht = capaciteit, niet productie).
- `co-moermansk-terminal` is aannemelijk, niet bron-gelegd (zie nikkelbrief [8]).
- Kobaltsitelaag `w-norilsk` (69.35, 88.20) draagt de 3 kt Kola-capaciteit op de Norilsk-centroïde, ~9 km van `co-nadezhda-fabriek`; een site Kola MMC op 67.9195, 32.8320 ontbreekt. Centraal gelijktrekken (sitelagen niet aangeraakt).
- Visueel dubbel: de lijn valt exact op `nikkel-norilsk-monchegorsk` (zelfde kopie); geen afwijking te verwachten.
- Sancties: geen documentatie van afnemers of export; Harjavalta-vertakking (Finland) bewust niet getekend.

## 8 · Bronnen
[1] Interfax, "Nornickel restores cobalt workshop at Kola MMC with capacity of 3,000 tonnes", dec. 2025 (gelezen 2026-10-09). https://interfax.com/newsroom/top-stories/115189/
[2] Interfax, "Norilsk Nickel restoring cobalt production after 2022 fire, targets 3,000 tonnes annually from 2025" (gelezen 2026-10-09). https://interfax.com/newsroom/top-stories/109943/
[3] The Barents Observer, "Major fire at Russia's largest nickel electrolysis workshop", 2022-09 — Monchegorsk, ~120 km ten zuiden van Moermansk, voeding Zapolyarny-erts + matte uit Nadezhda. https://thebarentsobserver.com/en/industry-and-energy/2022/09/major-fire-russias-largest-nickel-electrolysis-workshop
[4] Nornickel, Kola site — Zapolyarny-concentrator, concentraat naar Kola-ondernemingen. https://nornickel.com/business/assets/kola-division-russia/
[5] Nornickel AR2023, Logistics & sales of goods — Moermansk-terminal, spoor naar Kola Division (niet bereikbaar in deze sessie, ECONNRESET; geciteerd via nikkelbrief [5]). https://ar2023.nornickel.com/business-overview/logistics-sales-of-goods
[6] Nornickel, persbericht 16-12-2015 — "Kola MMC put into operation the first in Russia industrial production of commodity cobalt" (alleen kop gelezen). https://nornickel.com/news-and-media/press-releases-and-news/kola-mmc-put-into-operation-the-first-in-russia-industrial-production-of-commodity-cobalt/
[7] Nornickel 2022 Sustainability Report — Polar Division matte naar Kola MMC (alleen via zoekresultaat, pagina niet bereikbaar). https://sr2022.nornickel.ru/en/overview/about-nornickel.html
[8] Routebrief `nikkel-norilsk-monchegorsk.md` (2026-09-26, §2/§3/§8/§9) en `v2/data/stroomroute-nikkel-norilsk-monchegorsk.json` — alle km, ankers en snaps; bronnen [1]–[17] daarin.
[9] 2GIS — Портовый проезд 31/1, Мурманск (via nikkelbrief [11]). https://2gis.ru/murmansk/firm/70000001024889816
[10] Esri World Imagery via `sat_check.py`, z15 — `v2/build-cache/satcheck/sat-kobalt-norilsk-monchegorsk-kola-mmc.png`.
[11] Kobaltsitelaag `v2/design/kobalt-sitelaag.json` (`w-norilsk`, capaciteit 3 kt Co/j Kola-circuit).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Bestand:** `v2/data/stroomroute-kobalt-norilsk-monchegorsk.json` (56,2 KB; versie 2, `lonlat`) · **5 benen · 2.798,6 km · 3.144 punten · 4 markers.**

| # | modaliteit | km | punten | naad naar vorig been | opmerking |
|---|---|---|---|---|---|
| b1 | spoor | 78,0 | 233 | — | letterlijke kopie nikkel b1 (1-op-1-net, niet opnieuw gerouteerd) |
| b2 | binnenvaart | 430,2 | 2.187 | 3,08 km | letterlijke kopie nikkel b2 (bulklaag; kop 1,3 km van het Dudinka-anker, zie bevindingen) |
| b3 | zee (**stippel**) | 20,2 | 2 | 0,00 km | kopie nikkel b2b: naad bulk-knoop Jenisej-golf ↔ MARNET-zeeknoop 2338 (> 5 km-norm) |
| b4 | zee | 2.124,5 | 227 | 0,00 km | MARNET kade-snap 0,000 / 1,159 km, 17 MARNET-edges, geen via-punt; beennaam "(aannemelijk: één bron)" |
| b5 | spoor | 145,7 | 495 | 1,20 km | letterlijke kopie nikkel b5 (+2,5% tegen 142,1 gepubliceerd); beennaam "(aannemelijk: één bron)" |

**Recept:** functie `bak_kobalt_norilsk_monchegorsk` in `v2/tools/bak_stromen.sh`; dezelfde vijf beenregels, dezelfde volgorde en dezelfde geojsons als `bak_nikkel_norilsk_monchegorsk` (b4/b5 met "(aannemelijk: één bron)" in de naam), vier markers (de twee naadmarkers van de nikkelbak laten vervallen). Geen scan, rivier-, spoor- of MARNET-run herhaald; geen extract nodig; geen wegprofiel. Draaien: `bash v2/tools/bak_stromen.sh kobalt-norilsk-monchegorsk` (± 40 s).

**Toets:** km per been identiek aan de nikkelbak (0,0%); b5 +2,5% (±15% ok). Geometrie van b1/b2/b4/b5 punt-voor-punt gelijk aan `stroomroute-nikkel-norilsk-monchegorsk.json`. Naden max 3,08 km (< 5 km). `toets_knikken.py`: 7 knikken, 2 omkeringen, beide **terugloop op het Moermansk-emplacement** (178,1° R 57 m en 165,8° R 20 m bij 68.9768,33.0685 / 68.9732,33.0663) = kopmaken op het kaderangeerterrein, dezelfde twee als in de nikkelstroom; de andere knikken (Jenisej-bochten R 163/181 m, zeebochten) zijn bronrivier/MARNET-geometrie. `toets_rechte_benen.py --min-km 5`: alleen b3 (omwegfactor 0,999) en dat is de bedoelde stippel mét reden. json.load ok, modaliteiten ⊂ {zee, binnenvaart, spoor}, elk been ≥ 2 punten.

**Stippel met reden:** alleen b3 — "hier reikt het net niet": de bulklaag-rivier eindigt in de Jenisej-golf 20,2 km van MARNET-zeeknoop 2338. Geen haven-aanloop bij Moermansk (kade 1,2 km van zeeknoop 6906). Geen vlucht, geen leiding, geen last-mile-stippel (spoor reikt 0,23 km van het Kola-anker).

**Bevindingen (niet dichtgetrokken):**
- Marker **Dudinka-havenkade** ligt 1.265 m van de lijn (b1 eindigt 69.3915/86.2046, b2 begint 69.4052/86.1363; anker 69.4030/86.1680): kade-anker ≠ routeerpunt van het geïsoleerde spoor- en rivierbeen; de naad van 3,08 km tussen b1 en b2 is dezelfde als in de nikkelstroom. Marker **Nadezhda** staat 731 m van het spoor-uiteinde (terreinanker ≠ spoorkop). Boven de ~0,5 km-richtlijn; geërfd uit de nikkelbak, niet verschoven.
- Aannemelijkheid van de kobaltvoeding uit Norilsk-matte: één bron (§7); staat in de beennaam b4/b5, niet in de lijnstijl.
- Visueel dubbel met `nikkel-norilsk-monchegorsk` (identieke geometrie); de kobaltkleur ligt over de nikkellijn.
- Gloed/sitelaag (centraal): `w-norilsk` (69.35, 88.2) staat ~9 km van `co-nadezhda-fabriek` en draagt de 3 kt Kola-capaciteit; Kola MMC (67.9195, 32.8320) ontbreekt als site.

**Registerregel voor de orkestrator:** `{ "sleutel": "co-nm", "bestand": "stroomroute-kobalt-norilsk-monchegorsk.json", "grondstof": "kobalt", "label": "Norilsk → Monchegorsk (Kola-kobalt)", "aan": true, "noot": "M31 · golf 7 (2026-10-09): matte van Nadezhda per spoor, Jenisej, Arc7-zee en spoor naar de Kola-kobaltwerkplaats (aannemelijk: één bron)" }`

**Lessen:** (1) Een letterlijke kopie van een bestaande stroom bakt in ± 40 s: de geojsons staan in `$BEEN`, hecht_marnet routeert alleen het MARNET-been. (2) Geërfde markerafstanden (731 m / 1.265 m) horen bij het origineel; wie ze wil verbeteren doet dat in beide stromen tegelijk. (3) Het slot-recept met `rm -rf "$d"` wordt door de permissiecheck geweigerd; literal-pad `mkdir`/`rmdir` volstaat voor de slots.
