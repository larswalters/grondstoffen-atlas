# Routebrief (licht) · olie — NWO-tankenpark Wilhelmshaven (Duitsland) → Nord-West-Oelleitung → Köln, leidingeinde (Duitsland)

**stroom-id:** `olie-wilhelmshaven-koeln` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Keten in één zin:** Ruwe olie die per tanker bij de NWO-Löschbrücke in Wilhelmshaven wordt gelost, gaat via het NWO-tankenpark (1,6 Mm³) door de Nord-West-Oelleitung (71 cm, ondergronds) langs Emsland, Ochtrup en Hünxe naar de Köln-regio: **één leidingbeen, 330,4 km OSM-som in 26 ways**, geen zee-, spoor- of wegbeen. Het OSM-einde ligt in Köln-Müngersdorf; de leiding loopt volgens de bronnen door naar Wesseling (391 km).
**Welke as van het verhaal:** *Duitse kustpoort naar Rijn-Ruhr* — Wilhelmshaven is de diepwaterpoort (tankers tot 320.000 tdw) waar het Rijnland-Ruhrgebied zijn crude binnenkrijgt. **~283 kb/d (2024)** doorvoer van de héle NWO-leiding (14,1 Mt × 7,33 vat/t ÷ 365) [2]; 2025 ca. 10,9 Mt (≈ 219 kb/d) [2]; capaciteit 16,3 Mt/j (≈ 327 kb/d) [1][2][4]. Welk deel Köln bereikt is niet gepubliceerd. Herkomst aanvoer 2022: 39,5% Europa, 37,5% Noord-/Zuid-Amerika, 9,9% ex-Sovjet, 7,9% Afrika, 4,9% Midden-Oosten [1] — geen laadhaven genoemd.

## 1 · Ketenkaart
```
(tankers, herkomst per regio, geen haven)  ──► NWO-Löschbrücke / tankenpark Wilhelmshaven `ol-nwo-wilhelmshaven`
  ──(a1 leiding · Nord-West-Oelleitung, Wilhelmshaven → Emsland (Lingen-tak) → Ochtrup → Hünxe → Köln · 330,4 km OSM-som, 26 ways)──►
  leidingeinde Köln-Müngersdorf `ol-nwo-koeln-eind` ── stoppunt (leiding loopt ondergronds door naar Wesseling, niet gekarteerd)
```
Geen zeebeen: geen bron koppelt deze lading aan een laadhaven. Geen via-punten: het been is één OSM-leidingstreng (`man_made=pipeline substance=oil`, operator Nord-West Oelleitung GmbH) die op gedeelde nodes gestikt wordt.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| a1 | B | leiding | NWO-tankenpark Wilhelmshaven → Köln, leidingeinde | Nord-West-Oelleitung (NWO), 71 cm [1][2] | **330,4 OSM-som tegen 391 gepubliceerd** (Wilhelmshaven–Wesseling incl. takken) [1][2]: −15,5%, net buiten de ±15%-norm | `v2/tools/maak_leidingbeen_olie_wilhelmshaven_koeln.py` (26 OSM-ways) | nee — 5 naden (0,33 km totaal) recht gestikt |

Ways in volgorde (Wilhelmshaven → Köln): 37246878, 1170483426, 331053888, 1167228169, 1167982648, 1167228167, 802175179, 1167982649, 1167982650, 1170470432, 1167982651, 1167982652, 199070486, 1167982653, 1170046316, 95474852, 57882826, 57882823, 57857300, 56383213, 824960260, 751120616, 165992666, 166970499, 199084814, 945532321. Takken (Gelsenkirchen, Hamburg/NDO) zijn weggelaten.
Norm: de −15,5% is een indicatie, geen fout: de gepubliceerde 391 km eindigt in Wesseling (ca. 15–20 km voorbij het OSM-einde) en telt takken mee; zonder dat stuk −11 tot −13%. Fase C/D/E vervallen: geen bron noemt een vervolg van deze lading na de leiding.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-nwo-wilhelmshaven` | begin leiding / tankenpark + losbrug | NWO-tankenpark Wilhelmshaven (Heppenser Groden) — OSM-beginpunt way 37246878 | 53.5563, 8.1458 | [1][2][7][8][9] | bron-gelegd (z15 gezien: het punt ligt aan de noordwestrand van een tankenpark met ca. 35 drijfdak-tanks, 9 grote en rijen kleinere, achter de Jade-dijk; de Löschbrücke loopt 0,8 km vanaf de dijk oostwaarts de Jade in) |
| `ol-nwo-koeln-eind` | einde OSM-leiding, Köln | NWO-leidingeinde Köln-Müngersdorf — eindpunt way 945532321 | 50.9438, 6.8503 | [7][8] | onzeker (z15 gezien: woonwijk Köln-Müngersdorf langs een rechte groene strook, geen terrein of site; de leiding loopt ondergronds door, een 14 m-fragment way 944271639 op 50.9338, 6.8501 wijst naar het zuiden) |

Sitelaag `olie-sitelaag.json` heeft geen Wilhelmshaven- of Köln-site (`oil-mkt-europa` in v1 `data/oil.js` is een marktcentroïde op 53.60, 8.08 en geen anker); `ankers_hergebruik`: geen.

## 4 · Via-punten (leiding: geen corridorkeuze; alleen de kartering-naden)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| a1 | 1 | naad voor way 1167228169 (70 m, km 92,5) | 52.8309, 7.5806 → 52.8305, 7.5797 | OSM-hiaat ten noorden van Emsland (ondergronds); recht gestikt |
| a1 | 2 | naad voor way 802175179 (89 m, km 126,6) | 52.5551, 7.3802 → 52.5543, 7.3800 | Emsland, nabij de Lingen-tak (raffinaderij Lingen ligt 4,8 km van de lijn); recht gestikt |
| a1 | 3 | naad voor way 751120616 (121 m, km 231,9) | 51.7113, 6.8222 → 51.7102, 6.8219 | Rhede/Wesel-regio; recht gestikt |
| a1 | 4 | naad voor way 199084814 (28 m, km 257,6) | 51.4990, 6.8195 → 51.4988, 6.8194 | Rijn-Ruhrgebied; recht gestikt |
| a1 | 5 | naad voor way 945532321 (25 m, km 315,8) | 51.0394, 6.9443 → 51.0393, 6.9440 | Köln-noord; de laatste way loopt van hier naar het einde in Müngersdorf |
Totaal 0,33 km naad, geen stippel (kartering-hiaat van een ondergrondse leiding, geen net-gat).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| NWO Wilhelmshaven (Löschbrücke + tankenpark) | Nord-West Oelleitung GmbH: Ruhr Oel 33,7%, BP 25,6%, Shell 20,4%, Holborn/Oilinvest 20,3% | tankers → tanks → NWO- en NDO-leiding | tankenpark 1,6 Mm³; 1 berth tot 320.000 tdw + 2 tot 130.000 tdw; 2024: 183 tankers, 18,4 Mt omgeslagen | [1][2][4] |
| NWO-leiding Wilhelmshaven → Wesseling | NWO | ruwe olie, batches zonder scheidingsmolch | 16,3 Mt/j; 2024 14,1 Mt, 2025 ca. 10,9 Mt | [1][2][4] |
| raffinaderijen aan de leiding | Emsland (Lingen), Gelsenkirchen-Scholven en -Horst, Shell Rheinland Werk Süd Wesseling | crude → product | NWO noemt nu Lingen, Scholven en Horst [2]; Wesseling crude-verwerking 2025 beëindigd (was 7 Mt/j), Godorf (9 Mt/j) blijft draaien en krijgt crude via de Rotterdam-Rhein-Pipeline [5][6] | [2][5][6] |

## 6 · Stoppunt
De brief stopt bij het OSM-einde van de NWO in Köln-Müngersdorf: daar eindigt de gekarteerde leiding, geen bron noemt een afnemer voor dit eindstuk, en het stuk tot Wesseling (ca. 15–20 km) staat niet in OSM en wordt niet getekend (geen stippel naar Wesseling); vóór Wilhelmshaven geen zeebeen omdat geen bron een laadhaven noemt.

## 7 · Open punten
- **Volume voor het Köln-deel onbekend.** 14,1 Mt (2024) is de doorvoer van de héle NWO naar meerdere raffinaderijen [2]; geen bron splitst per afnemer of per kilometer. Het volume op het zuidelijke eind kan veel lager zijn.
- **Wesseling staat niet meer als afnemer.** Shell staakte de crude-verwerking daar in 2025 [5][6]; NWO noemt Wesseling niet meer onder de aangesloten raffinaderijen [2]. Of de leiding nog crude tot Köln/Wesseling voert of daar rust, is niet gevonden.
- **Eindpunt is geen site** (z15: woonwijk); het werkelijke leidingeinde (Wesseling, ca. 15–20 km verder) is niet gekarteerd, dus niet getekend. Fragment way 944271639 (14 m, 50.9338, 6.8501) is niet gestikt.
- **Km-toets net buiten norm** (−15,5%; indicatie, zie §2). De gepubliceerde 391 km is inclusief takken; geen eigen lengtebron zonder takken.
- **Löschbrücke niet als anker of been getekend**: geen bron-coördinaat; z15 toont de brug 0,8 km oostwaarts vanaf de dijk (8,153–8,166 O), ca. 1,2 km van het OSM-beginpunt van de leiding. Geen aanvoerleiding brug → tankenpark gevonden.
- **Herkomst crude alleen per regio** (2022) [1]; geen laadhaven, dus geen zeebeen. Het jaarvolume 2024 is niet gesplitst naar herkomst.
- **Takken** naar Lingen (ca. 5 km van de lijn) en Gelsenkirchen (ca. 15 km) en de NDO (Hamburg, 142 km) zijn niet getekend.
- **Naden** (0,33 km) zijn aangenomen kartering-hiaten, niet onafhankelijk bevestigd; parallelle leidingen (RRP, RMR liggen in dezelfde regio) zijn niet gestikt.

## 8 · Bronnen
[1] Wikipedia (de), "Nord-West Oelleitung" — 391 km, 71 cm, 16,3 Mt/j, 18,2 Mt (2020), herkomst 2022, aandeelhouders, Löschbrücke, tanklager. https://de.wikipedia.org/wiki/Nord-West_Oelleitung
[2] NWO GmbH, "Daten und Fakten" — 2024: 18,4 Mt omgeslagen, 14,1 Mt via NWO; 2025: ca. 10,9 Mt; tankers; aangesloten raffinaderijen; berths. https://nwowhv.de/datenundfakten/
[3] NWO GmbH, startpagina — 1956/1958, 140 medewerkers, 170 ha. https://www.nwowhv.de
[4] Global Energy Monitor, "North-West Oil Pipeline Network" — 391 km, 28 inch, 328.000 b/d (16,3 Mt/j), eigenaren. https://www.gem.wiki/North-West_Oil_Pipeline_Network
[5] Wikipedia (de), "Rheinland Raffinerie" (Energy and Chemicals Park Rheinland) — Godorf 9 Mt/j en Süd 7 Mt/j, Wesseling crude-verwerking 2025 beëindigd, crude via RRP, Süd aan NWO. https://de.wikipedia.org/wiki/Rheinland_Raffinerie
[6] ZfK, "Künftig ohne Rohöl: Shell will Raffinerie-Standort Wesseling umbauen" — crude-verwerking Wesseling stopt, Godorf blijft; Argus "Rohölverarbeitung in Wesseling endet Mitte März" (alleen titel gelezen). https://www.zfk.de/unternehmen/nachrichten/kuenftig-ohne-rohoel-shell-will-raffinerie-standort-wesseling-umbauen · https://argusmedia.com/es/news-and-insights/latest-market-news/2661960-roholverarbeitung-in-wesseling-endet-mitte-marz
[7] OpenStreetMap (ODbL) — way-geometrie via api.openstreetmap.org/api/0.6/ways.json en nodes.json (26 ways, gemeten 2026-10-30, cache `v2/build-cache/olie-wilhelmshaven-koeln-osmapi-cache.json`); Overpass-controle way 944271639 en 945532321. https://api.openstreetmap.org/api/0.6/way/37246878
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-olie-wilhelmshaven-koeln-nwo-wilhelmshaven.png`, `…-nwo-koeln-eind.png`.
[9] Wikipedia (de), "Heppenser Groden" — tanklager van de NWO op de Heppenser Groden (alleen zoekfragment gelezen). https://de.wikipedia.org/wiki/Heppenser_Groden
[10] v1 `data/oil.js` (`oil-mkt-europa`, marktcentroïde Wilhelmshaven) en `design/olie.md` — checklist/startpunt, geen anker.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)
**Bestand:** `v2/data/stroomroute-olie-wilhelmshaven-koeln.json` (17,8 KB, versie 2, lonlat) · **1 been · 330,4 km · 927 punten · 2 markers** · geen naad tussen benen (één been).
Recept: `bak_olie_wilhelmshaven_koeln()` in `v2/tools/bak_stromen.sh`; geometrie via `v2/tools/maak_leidingbeen_olie_wilhelmshaven_koeln.py --schrijf` (OSM-API, 26 ways, FeatureCollection) → `v2/build-cache/ais/graaf/olie-wilhelmshaven-koeln-leiding-a1.geojson`, als `--been-geojson` doorgetrokken. Geen profiel in `maak_stroombeen_weg.py` (geen wegbeen), geen zee, haven-aanloop, vlucht of stippel.
| # | modaliteit | km gemeten | km brief | afwijking | stijl |
|---|---|---|---|---|---|
| a1 | leiding (NWO, 71 cm) | 330,4 | 391 (Wilhelmshaven-Wesseling incl. takken) | -15,5% (indicatie) | doorgetrokken |
Markers: `olie-nwo-wilhelmshaven` (53.5563, 8.1458; 0,003 km van de lijn, bron-gelegd) en `olie-nwo-koeln-eind` (50.9438, 6.8503; 0,005 km, onzeker: woonwijk, OSM-leidingeinde).
**Toelichting leiding:** doorgetrokken omdat OSM de leiding heeft (`man_made=pipeline`, NWO). De 5 naden (samen 0,33 km, max 121 m) zijn recht gestikt; het stuk tot Wesseling (15-20 km) is niet gekarteerd en niet getekend, dus de lijn eindigt waar het bewijs eindigt en er is geen stippel. De afwijking van -15,5% is een indicatie: de 391 km loopt tot Wesseling en telt takken mee.
**Afwijking van het ontwerp:** het id noemt Köln en dat klopt, maar het eindpunt is het OSM-leidingeinde in Müngersdorf (geen site), niet Wesseling.
**Toetsen:** kleinste en grootste naad < 5 km tussen benen (één been); langste OSM-segment binnen het been 5,10 km (recht stuk ten zuiden van Wilhelmshaven, geen naad; naden max 0,12 km); markers <= 5 m van hun lijn; `toets_knikken.py` 28 knikken >= 60 graden (OSM-leidingbochten, spikes 25-190 m), 0 omkeringen, 0 terugloop; `toets_rechte_benen.py` meldt deze stroom niet; json.load ok, versie 2, lonlat, modaliteit leiding, been >= 2 punten, 17,8 KB; `bak_stromen.sh` blijft LF (0 CRLF).
**Lessen:** bij een leidingketen met alleen een OSM-streng volstaat één `--been-geojson` + twee markers; de Löschbrücke blijft zonder bron-coördinaat buiten beeld. Tijdens het bakken gaf bash een syntaxfout op een regel van een andere agent (gelijktijdige edit van `bak_stromen.sh`): het bakken was al klaar, een `bash -n` achteraf is schoon; herhaal de run niet.
