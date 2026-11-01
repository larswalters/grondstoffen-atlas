# Routebrief (licht) · olie — Sharara (Libië) → Sharara-Zawiya-leiding → Zawiya (Libië)

**stroom-id:** `olie-sharara-zawiya` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Titel:** Olie · Sharara → Sharara-Zawiya-leiding → Zawiya (Libië)
**Keten in één zin:** ruwe olie van het El Sharara-veld (Akakus JV: NOC met Repsol, OMV, TotalEnergies, Equinor) in de Murzuq-woestijn gaat per
**30-inch-leiding** (1998, via het boosterstation Hamada) door de Jebel Nafusa naar de Zawiya-olieterminal en -raffinaderij (NOC) aan de kust, 40 km west van Tripoli.
**Welke as van het verhaal:** *Libië's grootste actieve veld naar zijn eerste exportkeuze.* Capaciteit Sharara 300 kb/d (Wikipedia), 300-320 kb/d (Hydrocarbon
Processing); leidingcapaciteit ca. 9,96 Mt/j (GEM, ca. 200 kb/d bij 7,3 vaten/ton, eigen omrekening); werkelijk wisselend door sluitingen (jan. 2024, sept. 2026) [1][2][3][5]. Peiljaar 2024-26.
Zawiya-raffinaderij 120 kb/d [4]. De bol toont capaciteit, geen gemeten stroom.

## 1 · Ketenkaart
```
Sharara-veldinstallatie `ol-sharara-kop` ──(b1 leiding · Sharara-Zawiya-leiding, via Hamada · 622,5 km OSM, doorgetrokken)──►
  Zintan-OSM-uiteinde `ol-zintan-osm-eind` ──(b2 leiding · ~100 km hemelsbreed · STIPPEL, niet in OSM)──►
  Zawiya-tankenpark `ol-zawiya-tankpark` ── stoppunt (geen gebronde exportbestemming → geen zeebeen)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Sharara-kop → Zintan-OSM-uiteinde | Sharara-Zawiya-leiding 30", via Hamada-boosterstation (OSM `substance=oil`) | 622,5 gemeten; deel van 723 gepubliceerd [2][6]; Sharara→Hamada 338,7 tegen 340 gepubliceerd [2][6] | OSM-ways 273080145 (497,0) + 1109123294 (0,1) + 102162888 (125,5), per way-id uit de OSM-API, naden 0,0 (`maak_leidingbeen_olie_sharara_zawiya.py`) | nee |
| b2 | A | leiding | Zintan-OSM-uiteinde → Zawiya-tankpark | zelfde leiding, ontbrekend stuk | 99,8 hemelsbreed; Hamada→Zawiya 383 gepubliceerd = 283,8 OSM + 99,8 = 383,6 (+0,2%) | `--stippel "leiding\|…"` met reden: niet in OSM, schematisch | **ja** (14% van het geheel) |

Toets: 622,5 + 99,8 = 722,3 km tegen 723 gepubliceerd = −0,1% (binnen ±15%). Overlap: Hamada–Mellitah (way 273079900, 374,8 km) is een andere leiding en wordt niet gebruikt;
`gas-mellitah-gela` begint in Mellitah, 50 km westelijker — geen gedeeld been.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-sharara-kop` | veldinstallatie, kop van de leiding | El Sharara-veldinstallatie (OSM-leidingbegin, Murzuq) | 26.5817, 12.2080 | [3][7][8] | bron-gelegd (z15 gezien: omheinde verwerkings-/pompinstallatie met twee witte tanks, vlak ten noorden van het leidingbegin; 1,15 km ten westen van het Wikipedia-veldpunt 26.5767/12.2181, dat op het basiskamp ligt) |
| `ol-zintan-osm-eind` | knooppunt (geen site) | uiteinde gekarteerde leiding aan de weg Gharyan-Nalut, Zintan | 31.9523, 12.3141 | [7][8] | onzeker (z14 gezien: leiding kruist de weg; een recht, vrijgemaakt leidingtracé loopt zichtbaar noordwaarts door, dus de OSM-kartering stopt hier, de leiding niet) |
| `ol-zawiya-tankpark` | eindterminal / raffinaderij (stoppunt) | Zawiya-olieterminal en -raffinaderij (NOC), tankenpark aan de kust | 32.7885, 12.7000 | [2][4][7][8][9] | bron-gelegd (z15 gezien: groot tankenpark met ~35 tanks en procesinstallatie 0,6 km uit de kust, tweede tankenpark 0,5 km zuidwestelijk; Wikipedia-punt 32.7834/12.7019 ligt in hetzelfde complex, 0,6 km zuidoostelijk) |

Hergebruik: geen — Libië heeft geen olie-ankers in de sitelaag of eerdere brieven; Mellitah (`gas-mellitah-complex` 32.8547/12.2395) is een ander complex en niet gebruikt.
Hamada-boosterstation (29.5105, 12.9690; z15: omheind station met tanks, 1,3 km ten noorden van de leiding) is geen marker: tussenpunt, niet nodig als corridorkeuze.

## 4 · Via-punten
Niet van toepassing: leidingbeen uit aaneengestikte OSM-ways (geen weg/spoor, geen corridorkeuze).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Sharara-veld | Akakus Oil Operations (NOC, Repsol, OMV, TotalEnergies, Equinor) | winning → leidinginvoer | 300 kb/d capaciteit; 308 kb/d vóór de sluiting van maart 2018 [1] | [1][3][5] |
| Hamada-boosterstation | Akakus / NOC | drukverhoging halverwege (km ~340) | niet gebronnen | [1][2] |
| Zawiya-terminal + raffinaderij | NOC (Zawia Oil Refining Company) | leiding → tankopslag → export en raffinage | raffinaderij 120 kb/d; leiding ca. 9,96 Mt/j | [2][4][5] |

## 6 · Stoppunt
De brief stopt bij het Zawiya-tankenpark: de leiding eindigt daar, en geen bron noemt een haven of afnemer van de geëxporteerde lading (één lading naar Turkije okt. 2024, haven niet gebronnen),
dus geen zeebeen; fase D/E vervallen (raffinageproducten gaan naar de Libische binnenlandse markt, niet gebronnen per site).

## 7 · Open punten
- **~100 km (14%) is stippel:** het stuk Zintan → Zawiya staat niet in OSM. Op z14 loopt het vrijgemaakte tracé zichtbaar door ten noorden van Zintan; niet nagetekend (geen bewijs voor de exacte ligging, schatting zou verzinnen zijn).
- **Zawiya-anker op het tankenpark**, niet op een gedocumenteerde ontvangstklep of laadpier; de exportjetty/SPM (kust ca. 32.797, 12.676) is niet gelegd.
- **Exportbestemming ontbreekt:** geen zeebeen; Zawiya is zowel raffinaderij (120 kb/d) als exportterminal [2][5], de verdeling raffinage/export is niet gebronnen.
- **Volume is capaciteit, geen doorzet:** sluitingen (jan. 2024; klep 7 dicht 21-26 sept. 2026, ca. 942.000 vaten verlies; lek km 538 maart 2026) maken de werkelijke doorzet onbekend [5][10].
- **Leidingcapaciteit en lengte verschillen per bron** (723 / 725 / 726 km; GEM 9,96 Mt/j); Hamada→Zawiya soms 18" (ICE-bron) tegen 30".
- **Aftakking Hamada-Mellitah/El Feel** (way 273079900, 374,8 km) kan bij uitval Sharara-olie naar Mellitah brengen [10]; niet getekend (andere leiding).
- **Sitelaag olie kent Sharara en Zawiya niet** — centrale aanvulling nodig.
- **Politiek risico:** sluitingen door gewapende groepen en drone-aanvallen bepalen de feitelijke doorzet.

## 8 · Bronnen
[1] NS Energy, "El Sharara Oil Field" — 723 km, 30 inch, 1998, 340 + 383 km, Hamada-booster, Zawiya 45 km west van Tripoli. https://www.nsenergybusiness.com/?p=261289
[2] GEM.wiki, "El Sharara-Az-Zawiyah Oil Pipeline" — 723/725 km, 30 inch, 9,96 Mt/j, Akakus Oil Operations, 1998. https://www.gem.wiki/El_Sharara-Az-Zawiyah_Oil_Pipeline
[3] Wikipedia, "El Sharara oil field" — 26,5767/12,2181, 300 kb/d, 3 mld vaten reserves, sluitingen 2024 en sept. 2026. https://en.wikipedia.org/wiki/El_Sharara_oil_field
[4] Wikipedia, "Zawiya Refinery" — 40 km west van Tripoli, 120 kb/d, NOC. https://en.wikipedia.org/wiki/Zawiya_Refinery
[5] Hydrocarbon Processing, 28-09-2026 — klep 7 heropend, 300-320 kb/d, Zawiya-raffinaderij 120 kb/d, export. https://hydrocarbonprocessing.com/news/2026/09/update-libya-reopens-sharara-zawiya-pipeline-after-closure/
[6] OpenStreetMap-API (ODbL) — ways 273080145, 1109123294, 102162888 (`man_made=pipeline`, `substance=oil`); eigen meting 2026-11-01: som 622,5 km, Hamada-kruising op 338,7 km. https://www.openstreetmap.org/way/273080145
[7] OpenStreetMap/Overpass (ODbL, overpass.private.coffee) — alle pijpleidingen in bbox 31,5-33,2/11,5-13,2, 2026-11-01: geen gekarteerd stuk Zintan-uiteinde → Zawiya. https://overpass.private.coffee/api/interpreter
[8] Esri World Imagery via `v2/tools/sat_check.py` (z14-z15) — `sat-olie-sharara-zawiya-sharara-kop.png`, `-osm-eind-zintan.png`, `-zawiya-complex.png`, `-zawiya-tankpark.png`, `-hamada-pompstation.png` (v2/build-cache/satcheck/).
[9] Wikipedia-API (MediaWiki) — coördinaten El Sharara 26,576696/12,21805; Zawiya-raffinaderij 32,7834/12,7019 uit het ketenontwerp, niet door de API bevestigd. https://en.wikipedia.org/w/api.php
[10] Rigzone, 23-03-2026, "Fire Hits Oil Production at Major Libyan Field" — lek en brand km 538 bij Bir al-Marhan (Hamada), omleiding naar El Feel/Mellitah (alleen zoekresultaat gelezen). https://www.rigzone.com/news/fire_hits_oil_production_at_major_libyan_field-23-mar-2026-183267-article/

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
**Bestand:** `v2/data/stroomroute-olie-sharara-zawiya.json` (9,5 KB, versie 2, lonlat) · **functie:** `bak_olie_sharara_zawiya` in `v2/tools/bak_stromen.sh` · **totaal 722,3 km, 434 punten, 3 markers.**

| # | modaliteit | km gebakken | km brief | naad | stippel |
|---|---|---|---|---|---|
| b1 | leiding (OSM, doorgetrokken) | 622,5 | 622,5 (723 gepubliceerd voor het geheel) | 0 | nee |
| b2 | leiding (ontbrekend stuk) | 99,8 | 99,8 hemelsbreed | 0,003 km | ja, niet in OSM |

**Recept:** `python v2/tools/maak_leidingbeen_olie_sharara_zawiya.py` (OSM-API, ways 273080145 + 1109123294 + 102162888, FeatureCollection, 432 punten) en dan `bash v2/tools/bak_stromen.sh olie-sharara-zawiya`. Geen extract, wegscan, zeerouter, haven-aanloop, lucht of kopie; geen profiel in `maak_stroombeen_weg.py`.

**Toelichting stippel b2:** het stuk Zintan-uiteinde (31.9523, 12.3141) naar het Zawiya-tankenpark (32.7885, 12.7000) staat niet in OSM; rechte schematische lijn van 99,8 km (14 procent), reden in de beennaam. Totaal 722,3 tegen 723 gepubliceerd is -0,1 procent.

**Toets:** naden 0 en 0,003 km; markers 0,003 / 0,0 / 0,0 km van de lijn; `toets_knikken` 1 knik van 76 graden (R 559 m, bij 27.249/12.410, geen omkering of terugloop; OSM-geometrie); `toets_rechte_benen` meldt alleen de stippel b2 als rechte lijn, het doorgetrokken been b1 niet.

**Lessen:** (1) Libië heeft geen Geofabrik-extract, dus een OSM-leiding via de OSM-API per way-id is hier de route. (2) Het Zintan-punt is een OSM-uiteinde, geen site; de leiding loopt zichtbaar door, het eerlijke antwoord is een stippel met reden. (3) Sitelaag olie kent Sharara en Zawiya niet; centrale aanvulling nodig. (4) Volume is capaciteit, geen doorzet (sluitingen 2024 en 2026).
