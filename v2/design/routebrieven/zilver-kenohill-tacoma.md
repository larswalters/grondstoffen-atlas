# Routebrief (licht) · zilver — Keno Hill → Skagway → Puget Sound (Canada/VS)

**stroom-id:** `zilver-kenohill-tacoma` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**Keten in één zin:** Zilver-loodconcentraat van Hecla's Keno Hill-molen (Yukon) per **truck** (gecontaineriseerd) over de Silver Trail, Klondike Highway en
South Klondike Highway (~630 km) naar de Skagway Ore Terminal, daarna per **bargeschip** door de Inside Passage (MARNET ~1.793 km) naar Puget Sound
(Washington); **stoppunt** op de zeeknoop: Seattle of Tacoma is niet vastgesteld, dus er is geen kade en geen Aziatische smelter getekend.
**⚠️ Eindpunt wijkt af van het id:** het id belooft Tacoma, maar geen bron noemt Tacoma boven Seattle (TRS 2023: "Seattle or Tacoma", Yukon-briefing 2024: alleen
"Washington state", Bellekeno-voorganger via Seattle). Titel en marker zeggen daarom Puget Sound / "haven onbepaald (aannemelijk: Seattle)".
**Welke as van het verhaal:** *Reserve Yukon naar Pacific Northwest* — Keno Hill 3,02 Moz Ag 2025 = ~94 t Ag/j (Hecla 10-K FY2025, overgenomen uit de
haalbaarheidstoets [2]; mijn nog in ramp-up); concentraatvolume 690 DMT Ag-Pb/maand volgens het Hecla-operatieplan jan 2023 [3]. Aandeel zilver per ton concentraat niet gepubliceerd.

## 1 · Ketenkaart
```
Keno Hill-molen `ag-kenohill-molen` ──(b1 truck · Silver Trail YK 11 → Klondike Hwy YK 2 → Alaska Hwy YK 1/2 door Whitehorse → South Klondike Hwy YK 2/AK 98 · ~630 km)──►
  Skagway Ore Terminal `ag-skagway-kade` ──(b2 zee · barge Inside Passage, MARNET · ~1.793 km, aannemelijk: één bron voor de Washington-haven)──►
  zeeknoop 7804 in Puget Sound `ag-pugetsound-eind` ── stoppunt (haven onbepaald)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | molen → Skagway Ore Terminal | YK 11 Silver Trail → YK 2 Klondike Hwy (Stewart Crossing, Carmacks) → Alaska Hwy YK 1/2 (Whitehorse) → South Klondike Hwy YK 2 (Carcross, grens Fraser/Skagway) → AK 98 → Terminal Way | **~630**: 452 Elsa–Whitehorse (TRS) [1] + ~7 molen–Elsa (hemelsbreed, OSM) + 172 Whitehorse-aansluiting–Skagway (Wikipedia) [5]; de som is mijn optelling, geen bedrijfsopgave; hemelsbreed Keno–Skagway ~494 | maak_stroombeen_weg via `wegscan_puur.py` (canada + us-alaska) | nee |
| b2 | B | zee | Skagway-kade → zeeknoop 7804 (Puget Sound) | Lynn Canal, Inside Passage, Strait of Georgia, Juan de Fuca | MARNET **1.792,6** (getest kade-zeeknoop 2964 → 7804, door de Inside Passage langs Lynn Canal en de Strait of Georgia); hemelsbreed ~1.600 (ontwerp), geen gepubliceerde km | MARNET | aanloop: nee (kade 0,6 km van zeeknoop 2964) |
Geen haven-aanloop aan de Puget Sound-kant: er is geen kade gevonden; MARNET-zeeknoop 7804 ligt 7,3–8,5 km van de Seattle-kades en 7801 (Tacoma) 5,8–7,1 km, dus een kade kiezen zou gokken zijn.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-kenohill-molen` | mijn + molen (laad) | Keno Hill-molencomplex (Hecla), 7 km ten oosten van Elsa | 63.9080, -135.3274 | [1][7] OSM landuse (haalbaarheidstoets) | bron-gelegd (z15 gezien: een industrieel complex met gebouwen, pads en een tak van de Silver Trail in boslandschap; het kruis ligt op het complex, Duncan Creek Road 0,2 km; een wolk bedekt de noordrand) |
| `ag-skagway-kade` | overslag (terminal) | Skagway Ore Terminal (AIDEA/Skagway Ore Dock) | 59.4508, -135.3268 | [3][7] OSM way 8991547 "Ore Dock" | bron-gelegd (z15 gezien: concentraatloods met silo's en een lange pier/kade in de baai; het kruis ligt op de loods-kade, Terminal Way eindigt hier) |
| `ag-pugetsound-eind` | eindpunt zonder kade | Washington (Seattle of Tacoma) - haven onbepaald (aannemelijk: Seattle) | 47.5731, -122.4523 | [1][3] zeeknoop 7804, geen kade | onzeker (z13 gezien: open water in Puget Sound tussen Bainbridge Island en West-Seattle, ~5 km uit Seattle; het is een routeknoop, geen overslagplek) |
Zeeknopen (geen ankers): Skagway 59.4545, -135.3188 (id 2964, 0,6 km van de kade); Puget Sound 47.5731, -122.4523 (id 7804).

## 4 · Via-punten (b1; 8 punten op de doorgaande weg, nooit in een centrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Silver Trail bij Mayo (YK 11) | 63.6020, -135.8881 | pint de Silver Trail (tertiary/secondary, deels unpaved) boven de Mayo-Elsa-zijweg; OSM way 661043033 [8] |
| b1 | 2 | Stewart Crossing (YK 2) | 63.3754, -136.6792 | splitsing Silver Trail / Klondike Hwy: zuidwaarts (Whitehorse) en niet noordwaarts (Dawson); way 1262659134 |
| b1 | 3 | Carmacks, Klondike Hwy (YK 2) | 62.0879, -136.2902 | doorgaande weg aan de rand van het dorp, voorkomt het wegennet van Carmacks; way 1262659126 |
| b1 | 4 | Alaska Hwy ten noordwesten van Whitehorse (YK 1;2) | 60.7488, -135.1432 | houdt de route op de Alaska Hwy-bypass i.p.v. straten van het centrum; way 158986370 |
| b1 | 5 | Alaska Hwy ten oosten van Whitehorse (YK 1;2) | 60.6529, -135.0325 | idem, zuidoostzijde van de stad; way 158986386 |
| b1 | 6 | Aansluiting South Klondike Hwy (YK 2) | 60.5897, -134.8712 | waar de Klondike Hwy de Alaska Hwy verlaat richting Carcross; way 1262285832 |
| b1 | 7 | Carcross, Klondike Hwy (YK 2) | 60.1682, -134.7033 | doorgaande weg langs het dorp (106,0 km van Skagway volgens Wikipedia [5]); way 1422514703 |
| b1 | 8 | Grens Fraser/Skagway (YK 2/AK 98) | 59.6297, -135.1643 | grensovergang Canada/VS, enige oversteek; OSM-knoop tussen way 628532613 en AK 98 8991962 |
b2 heeft geen via-punten (router). Profielsleutel-advies: `zilver-kenohill-tacoma-molen-skagway`, extracts `["canada", "us-alaska"]`, `refs ["YK 11","YK 2","YK 1","AK 98"]`,
`corridorKlassen ["tertiary"]` (Silver Trail is deels unpaved tertiary), `vensterKm` 40, `gepubliceerdKm` 630. Eind bij Terminal Way (OSM unclassified, 0,1 km van het anker).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Keno Hill-molen | Hecla Mining (ex-Alexco) | erts → Ag-Pb-concentraat (naar Washington) + Zn-concentraat (naar Greens Creek, niet getekend) | 3,02 Moz Ag in 2025 (~94 t); vergund 440 t erts/dag, 299 t/dag in 2024 | [2][3] |
| Skagway Ore Terminal | AIDEA, gebruikers o.a. Hecla | gecontaineriseerd concentraat → bargeschip | 690 DMT Ag-Pb + 220 DMT Zn per maand (operatieplan jan 2023) | [3] |

## 6 · Stoppunt
Stop op de zeeknoop in Puget Sound: de bron noemt alleen "Seattle of Tacoma" of "Washington state" en daarna "Aziatische smelters" zonder naam; geen fase D/E.

## 7 · Open punten
- **Eindhaven Seattle vs Tacoma niet vastgesteld.** Seattle is aannemelijker (Hecla/Lynden gebruikt Alaska Marine Lines Seattle als bargehaven voor Lucky Friday, 2023 [4]); het AML-adres Georgetown (47.5513, -122.3438, Nominatim) is geen bevestigde kade en ligt 8,5 km van knoop 7804. De lijn eindigt op de zeeknoop zonder kade of aanloop.
- **Aziatische smelters niet benoemd** [3]; het zinkconcentraat (Greens Creek) is een aparte vertakking en wordt niet getekend.
- **Wegkm niet uit één bron:** 630 km is TRS Elsa-Whitehorse + Wikipedia Whitehorse-Skagway + 7 km zelf geschat; de ±15%-toets (535-725 km) is een indicatie.
- **Skagway Ore Terminal:** per okt 2023 eist Skagway gecontaineriseerd erts en een 2023-bericht noemde een herbouw van de Ore Dock met "geen lading tot klaar" [3]; huidige status niet bevestigd. Het anker is de terminal zoals OSM hem kent.
- **Molen-anker is een OSM-landuse-punt**, geen bedrijfsopgave; TRS noemt de molen als Keno Hill Mill zonder coördinaat. Keno Hill is in ramp-up (299 t/dag in 2024 tegen 440 vergund).
- **10-K FY2025 (3,02 Moz)** is in dit blok niet zelf geopend (SEC levert > 10 MB / blokkeert bots); overgenomen uit de haalbaarheidstoets. Sitelaag mist Keno Hill: centraal `w-keno-hill` (63.9080, -135.3274) toevoegen.
- **Bak-risico weg:** canada-pbf is 6,4 GB (reus-slot, ~10-30 min); Whitehorse-bypass en Silver Trail-klasse zijn de punten om op te letten (vias 4/5 projecteren op de trunk bij een keerpunt).

## 8 · Bronnen
[1] Hecla Mining, Technical Report Summary Keno Hill 2023 (SEC EX-96.4): silver-lead concentrate trucked and barged weekly Skagway to Seattle or Tacoma then Asia; zinc to Greens Creek; Elsa-Whitehorse 452 km (via haalbaarheidstoets, bestand te groot voor WebFetch). https://www.sec.gov/Archives/edgar/data/719413/000095017024015673/hl-ex96_4.htm
[2] Hecla Mining, Form 10-K FY2025 — Keno Hill 3,02 Moz Ag 2025 (via haalbaarheidstoets, niet zelf geopend). https://www.sec.gov/Archives/edgar/data/719413/000119312526055059/hl-20251231.htm
[3] Yukon Economic Development, fall 2024 briefing — Hecla exports containerized Ag-Pb and Zn concentrate via Skagway, Pb to Washington state for Asian smelters; 690/220 DMT per maand; Skagway-verordening okt 2023 (gelezen via zoekresultaat, scan-PDF). https://open.yukon.ca/fr/information/3aed6e7f-534d-4a7f-add5-739b501731f0/resource/b732815e-af67-339f-bc9a-dde1e13ad53c/download/ecdev-2024-fall-bn.pdf
[4] Mining News North, 22 jan 2012 — Bellekeno-output barge via Skagway-terminal naar Seattle, daarna truck naar Trail (zoekresultaat; pagina geeft 403). https://www.miningnewsnorth.com/story/2012/01/22/news/port-interests-more-potential-users/2559.html — en Lynden/Hellenic 2023-03-20 (Hecla via Seattle, via haalbaarheidstoets; URL niet bevestigd).
[5] Wikipedia, South Klondike Highway — Skagway-Whitehorse-aansluiting 172,0 km, Carcross 106,0 km, grens 23,1 km. https://en.wikipedia.org/wiki/South_Klondike_Highway ; Klondike Highway (709 km Skagway-Dawson, Silver Trail bij Stewart Crossing). https://en.wikipedia.org/wiki/Klondike_Highway
[6] Zoeksessie 2026-10-09 (Keno Hill, Skagway Ore Terminal; geen bron noemt Tacoma).
[7] OpenStreetMap/Nominatim: Skagway Ore Dock (way 8991547, 59.4507,-135.3267), Terminal Way (way 8991774), Keno City, Elsa (node 107350661, 63.9117,-135.4902), Port of Tacoma (way 4687974).
[8] OSM-kaart-API (api.openstreetmap.org, 2026-10-09): YK 2 way 1262659134/1262659126/1422514703, YK 11 way 661043033, YK 1;2 way 158986370/158986386, YK 2 way 1262285832, grensways 628532613/8991962.
[9] Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-zilver-kenohill-tacoma-molen.png`, `-skagway-kade.png`, `-zeeknoop-pugetsound.png`. MARNET-test: `hecht_marnet.py route` Skagway 59.4545,-135.3188 → 47.5731,-122.4523 = 1.792,6 km, 200 punten.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Bestand:** `v2/data/stroomroute-zilver-kenohill-tacoma.json` (147,3 KB, versie 2, lonlat) · **totaal 2.432,4 km, 6.896 punten, 3 markers** · functie `bak_zilver_kenohill_tacoma` in `v2/tools/bak_stromen.sh` (LF, 0 CRLF) · profiel `zilver-kenohill-tacoma-molen-skagway` in `maak_stroombeen_weg.py`.
| # | modaliteit | km gemeten | km brief | afwijking | naad naar volgend been | stippel |
|---|---|---|---|---|---|---|
| b1 | truck | 639,8 (lengtetoets 639,4) | ~630 (eigen optelling) | +1,5% | 0 | nee |
| b2 | zee | 1.792,6 | MARNET 1.792,6 | 0,0% | 0,61 km (snap kade naar zeeknoop 2964) | nee |
**Recept b1:** `wegscan_puur.py --profiel zilver-kenohill-tacoma-molen-skagway` (canada 6,4 GB + us-alaska, ~8 min), 10 via-lijst (2 ankers + 8 via-punten uit §4), corridorKlassen tertiary, vensterKm 40, trimStaart. Alle via-snaps 0,00-0,01 km, molen-anker snap 0,19 km, kade-eind 0,20 km, last mile 0,30 km; geen via-punt verplaatst of verwijderd, geen omweg. Per segment: molen-Mayo 60,2 · Mayo-Stewart Crossing 51,2 · Stewart Crossing-Carmacks 176,7 · Carmacks-Whitehorse NW 170,7 · Whitehorse-bypass 13,2 + 12,1 · tot Carcross 50,8 · Carcross-grens 81,3 · grens-kade 23,6. Keerlussen gesnoeid: 5 (alle ≤ 0,03 km). Eerste 60 km over kleine klassen (Silver Trail: residential/tertiary/unclassified).
**Recept b2:** `--been "zee|…|59.4508,-135.3268|47.5731,-122.4523"`, snap 0,611 km (Skagway) en 0,000 km (Puget Sound), 42 MARNET-edges, 200 punten, geen aanloop (kade < 5 km van zeeknoop), geen connector.
**Markers (3):** ag-kenohill-molen, ag-skagway-kade, ag-pugetsound-eind; alle 0,000 km van de lijn.
**Toetsen:** geen naad > 5 km · `toets_knikken.py`: 0 omkeringen, 0 terugloop; truck 6 spikes (R 9-57 m) op via-/junctiepunten (63.6018,-135.8872 Mayo; 63.9095,-135.3022 en 63.9064,-135.3288 bij de molen; 63.3826,-136.6814 Stewart Crossing; 60.8103,-135.2050 en 60.5995,-134.8780 rond Whitehorse) en zee 4 krappe bochten (R 3,4-4,8 km) in Chatham Strait/Lynn Canal en Juan de Fuca: echte kronkels in smalle vaarwater, geen fout · `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom · json.load ok, modaliteiten {truck, zee}, elk been >= 2 punten.
**Toelichting:** geen stippel, geen aanloop, geen kopie, geen vlucht, geen leiding. Het eindpunt is de zeeknoop 7804 zonder kade; het id belooft Tacoma, titel en marker zeggen Puget Sound / haven onbepaald (aannemelijk: Seattle). Titel: "Zilver · Keno Hill-molen (Yukon) → Skagway → Puget Sound (Washington, haven onbepaald)". De +1,5% op b1 is een indicatie (brief-km is een optelling van twee bronnen plus 7 km eigen schatting).
**Lessen:** (1) `wegscan_puur.py` draaide de canada-pbf (6,4 GB) met bbox-venster in ~8 minuten; de log staat in `v2/build-cache/ais/graaf/zilver-kenohill-tacoma-wegscan.log`. (2) De 8 via-punten uit de brief waren allemaal goed gelegd (snap <= 0,01 km, geen omweg): de brief hoefde niet te worden aangepast. (3) De sitelaag mist nog Keno Hill (centraal: `w-keno-hill` 63.9080,-135.3274).
