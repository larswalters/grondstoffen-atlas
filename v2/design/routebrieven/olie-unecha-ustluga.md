# Routebrief (licht) · olie — Unecha (Rusland) → BPS-2 → Ust-Luga (Rusland)

**stroom-id:** `olie-unecha-ustluga` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** Russische exportolie per **leiding** over de Baltische Pijpleiding-2 (BPS-2, Transneft) van het pompstation Unecha
NPS-1 (Bryansk, kop op de Druzhba-splitsing) via Smolensk, Andreapol en het Novgorod/Pskov-gebied naar het tankenpark van Transneft-Baltika
in Ust-Luga (Loega-baai, Leningrad oblast): één been, 994,6 km OSM-som, geen zee, geen via-punten, stoppunt bij de tankopslag.
**Welke as van het verhaal:** *de tweede Russische Baltische uitgang* — BPS-2 voert olie uit het Druzhba-stelsel (ook Kazachse transitolie
via Atyrau–Samara [4]) rechtstreeks naar de Oostzee, zodat Wit-Rusland en Oekraïne niet meer nodig zijn. Ust-Luga exporteert **~700 kb/d**
(Valora Analitik, 29-3-2026; haventotaal, ook producten) [3]; BPS-2 ontwerpcapaciteit **30 Mt/j ≈ 600 kb/d** (eerste fase; tweede fase
50 Mt/j) [2] — indicatie voor deze keten; peiljaar 2025/26. Terminal in 2026 meermaals aangevallen (25-3, 29-3, 14-8), laden tijdelijk gestaakt [1][5].

## 1 · Ketenkaart
```
Unecha NPS-1 `ol-unecha-nps1` (Transneft, Bryansk; BPS-2-kop)
  ──(a1 leiding · BPS-2 Unecha → Smolensk → Andreapol → Pskov/Novgorod → Ust-Luga · 994,6 km OSM-som, 998 gepubliceerd [1])──►
Nefteb aza Ust-Luga `ol-ustluga-tankenpark` (Transneft-Baltika) ── stoppunt
```
Niet getekend: de tak naar Kirishi (172 km [1]) en het schip dat vanaf de steigers vertrekt.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| a1 | A | leiding | `ol-unecha-nps1` → `ol-ustluga-tankenpark` | Baltic Pipeline System-2 (Transneft), Unecha–Andreapol–Ust-Luga | 994,6 OSM-som (12 ways) tegen **998 gepubliceerd** (−0,3%) [1][6] | OSM-ways in §4, `man_made=pipeline`, `substance=oil`, laatste way `name:en` "Baltic Pipeline System-2" | nee |

De 1.300 km uit ru.wikipedia [2] is het hele systeem incl. de (later geschrapte) Kirishi-tak, geen norm voor deze keten. Geen leg B/C/D/E.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-unecha-nps1` | kop / pompstation | Unecha NPS-1 (Transneft), Bryansk — OSM-beginknoop 2037730125 van way 173115751 | 52.7668, 32.9295 | [1][6][7] | bron-gelegd (z15+z16 gezien: omheind tankenpark met ronde tanks en pompgebouwen, het punt ligt op grasland aan de westrand, ~80 m van de eerste pompgebouwen) |
| `ol-ustluga-tankenpark` | eindpunt / tankopslag | Nefteb aza Ust-Luga (Transneft-Baltika) — OSM-eindknoop 3700486239 van way 333903684 | 59.6856, 28.4412 | [1][6][7] | bron-gelegd (z15 gezien: tankenpark van ~10 witte tanks met pompgebouwen tussen spoorbundel en bos, punt op de oostrand tussen de tanks; punt ligt binnen het OSM-landuse-vlak van de nefteb aza, way 337522652) |

`ol-unecha-kop` van olie-unecha-szazhalombatta (52.7649, 32.6805) ligt 17 km westelijker op de Druzhba-streng en wordt **niet** hergebruikt.
`w-ustluga` (sitelaag 59.6603, 28.2769, Wikipedia-plaatscoördinaat) ligt 9 km van de oliehaven: eigen anker, geen hergebruik. De steigers zelf
(laadkades in de Loega-baai) zijn niet gelegd; de brief stopt bij de tankopslag.

## 4 · Via-punten
Geen. De leiding volgt de OSM-ways zelf; er is geen corridorkeuze (alleen BPS-2 ligt op dit tracé, de Kirishi-tak is niet meegenomen).
Stikvolgorde van de 12 ways (reisvolgorde; 10 naden delen een OSM-node, twee naden zijn open):
173115751 (86,1) → 282239195 (13,6) → 333885244 (134,1) → 333885251 (269,5) → **naad 0,016 km** → 318819120 (14,8) → **naad 0,604 km** →
819499320 (48,0) → 500430998 (8,2) → 508649116 (71,5) → 508204510 (3,3) → 824058814 (2,6) → 500430997 (59,0) → 333903684 (284,0).
Som 994,6 km over 2.634 punten. De naad van 0,6 km (56,6611/32,1049 → 56,6655/32,0993, bij Andreapol) wordt gestikt, niet gestippeld.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Unecha NPS-1 / Andreapol (pompstations) | Transneft | doorvoer, geen verwerking | acht pompstations langs BPS-2 [1] | [1] |
| Nefteb aza Ust-Luga | Transneft-Baltika | ruwe olie → tankopslag → schip | haven ~700 kb/d export (incl. producten); 32,9 Mt in 2025 [3] | [3][7] |

## 6 · Stoppunt
De brief stopt bij het tankenpark van Ust-Luga: de leiding eindigt daar en geen bron koppelt een lading aan een bestemmingshaven buiten de
Oostzee; het zeebeen is een aparte keten (zie olie-primorsk-jamnagar voor het patroon).

## 7 · Open punten
- **Flowstatus 2026:** de terminal is op 25-3, 29-3 en 14-8-2026 aangevallen en het laden was tijdelijk gestaakt [1][5]; de infrastructuur bestaat. Het
  actuele volume van BPS-2 is niet gevonden; 600 kb/d is de ontwerpcapaciteit, geen meting.
- **Haventotaal ≠ pijpleidingvolume:** de 700 kb/d / 32,9 Mt van Ust-Luga bevat producten en ook Kazachse transitolie; het aandeel dat per BPS-2 aankomt is niet gebrond.
- **Tak naar Kirishi (172 km)** en een eventuele aansluiting van BPS-1 niet getekend; sommige OSM-ways zonder naam, dus of elke way exact de actieve strang is, is niet per Transneft-bron bevestigd.
- **Laadsteigers** in de Loega-baai niet als anker gelegd.

## 8 · Bronnen
[1] Wikipedia, "Baltic Pipeline System-II" — Unecha–Ust-Luga 998 km, Kirishi-tak 172 km, in bedrijf maart 2012, acht pompstations. https://en.wikipedia.org/wiki/Baltic_Pipeline_System-II
[2] ru.wikipedia, "Балтийская трубопроводная система — 2" — route Unecha–Andreapol–Ust-Luga, 30 resp. 50 Mt/j, systeem ca. 1.300 km. https://ru.wikipedia.org/wiki/Балтийская_трубопроводная_система_—_2
[3] Valora Analitik, 29-3-2026, "Ucrania ataca Ust-Luga" — ~700.000 vaten/dag export, 32,9 Mt in 2025. https://www.valoraanalitik.com/?p=567499
[4] Interfax, 25-8-2025 — Kazachse olie via Atyrau–Samara en Transneft naar Ust-Luga en Novorossiysk. https://interfax.com/newsroom/top-stories/113421/
[5] Wikipedia, "Ust-Luga" — drone-aanvallen 25-3, 29-3 en 14-8-2026, laden tijdelijk gestaakt; terminal 59.6603/28.2769 (plaats). https://en.wikipedia.org/wiki/Ust-Luga
[6] OpenStreetMap (ODbL) via api.openstreetmap.org/api/0.6/ways + /nodes, 2026-11-01 — de 12 ways, lengtes en naden; node 2037730125 (52.76677/32.92951), node 3700486239 (59.68558/28.44117). https://www.openstreetmap.org
[7] OpenStreetMap, way 337522652 "Нефтебаза Усть-Луга" (Transneft-Baltika, landuse=industrial, liquid_bulk) — eindknoop ligt erbinnen; Nominatim-zoekopdracht bevestigt de naam. https://www.openstreetmap.org/way/337522652
[8] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-olie-unecha-ustluga-unecha.png`, `-unecha-z16.png`, `-ustluga.png` (z15/z16).
[9] Wikipedia, "Baltic Pipeline System" — BPS-2 als tweede streng van Unecha naar Ust-Luga met tak naar Kirishi. https://en.wikipedia.org/wiki/Baltic_Pipeline_System

## 9 · Bak-noot (door de bak-agent)

**Gebakken (2026-11-01, lichte werkwijze, M31 golf 20).** `v2/data/stroomroute-olie-unecha-ustluga.json` (51,3 KB, versie 2, lonlat).
- **Benen:** a1 leiding 995,2 km, 2.625 punten, doorgetrokken (geen stippel, geen zee, geen haven-aanloop). Totaal 995,2 km, 2 markers (Unecha NPS-1 en tankenpark Ust-Luga, beide 3 m van de lijn).
- **Km-toets:** 995,2 tegen 998 gepubliceerd = -0,3% (norm +-15%). Naden: geen (enkel één been).
- **Recept:** `bak_olie_unecha_ustluga` in `v2/tools/bak_stromen.sh`; geometrie via `v2/tools/maak_leidingbeen_olie_unecha_ustluga.py` (OSM-API per way-id, cache `olie-unecha-ustluga-osmapi-cache.json`), uitvoer `v2/build-cache/ais/graaf/olie-unecha-ustluga-leiding-a1.geojson` (FeatureCollection).
- **Leiding:** 12 OSM-ways in reisvolgorde, 10 naden op gedeelde nodes (0 m), twee open naden gestikt met een rechte verbinding: 0,016 km en 0,604 km (56,6655/32,0993 bij Andreapol). Totaal 995,22 km tegen OSM-som 994,6 plus naden 0,6.
- **Toetsen:** `toets_knikken.py` 17 knikken, 0 omkeringen, 0 terugloop (OSM-bochten van de leiding, geen reparatie); `toets_rechte_benen.py` geen vlag voor deze stroom; json.load ok, modaliteit leiding.
- **Lessen:** vooraf de zwaarste vraag (is de actieve strang de OSM-som?) blijft open voor sommige naamloze ways; flowstatus 2026 en laadsteigers zoals in §7. Geen overlap met olie-unecha-szazhalombatta.
