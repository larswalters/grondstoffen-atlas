# Routebrief (licht) · olie — Agadem (Niger) → Niger-Benin Export Pipeline → Seme-Kpodji (Benin)

**stroom-id:** `olie-agadem-seme` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** Crude uit het Agadem Rift Basin (CNPC, Zuidoost-Niger) per **leiding** (NBEP, 20", WAPCO Bénin) via Zinder/SORAZ, Dosso en de grens bij Gaya naar de Beninse kust bij Seme-Kpodji; de lijn eindigt waar OSM eindigt, de lading en afnemer zijn niet gedocumenteerd.
**Welke as van het verhaal:** *Niger-crude via de langste leiding van Afrika naar de Beninse kust* (sinds 2024 de eerste uitvoerweg van Niger). Volume: capaciteit 110 kb/d (OSM-tag + Wikipedia [1][2], peiljaar 2024); werkelijk 2024 onzeker, 52 kb/d (AfDB) tot 107 kb/d (Wereldbank) uit het ketenontwerp, niet zelf gecontroleerd; Agadem-capaciteit 20 → 90 kb/d na fase 2 [3]. Export onderbroken juni-aug 2024 [1][4].

## 1 · Ketenkaart
```
Agadem-OSM-begin `ol-agadem-kop` (15.3362, 13.2759; ~14 km van Koulélé) ──(b1 leiding · NBEP via Zinder/SORAZ, Dosso, Gaya ·
  1.869,9 km OSM-som, 3 ways gestikt, doorgetrokken, 0 stippel)──► OSM-einde kust Seme-Kpodji `ol-seme-eind` (6.3654, 2.6240) ── stoppunt
  (offshore buis naar de SPM ~15 km uit de kust staat niet in OSM: niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Agadem-OSM-begin → OSM-einde Seme-Kpodji | Niger-Benin Export Pipeline (NBEP) via Zinder (SORAZ), Dosso, grens Gaya/Malanville | eigen OSM-som 1.869,9 (Niger 1.228,9 + Benin 640,9) [2]; gepubliceerd 1.950 (Wikipedia [1]) en 1.980 [3][5] = −4,1% / −5,6% | OSM-ways 1164438280 (Niger, 37 nodes) + 1225590062 (2 nodes, omgekeerd) + 1225590061 (Benin, 192 nodes, ref NBEP), naden 0,0 m, `maak_leidingbeen_olie_agadem_seme.py` | nee — volledig doorgetrokken |
Naam van het been: "Niger-Benin Export Pipeline (NBEP): Agadem → Zinder → Gaya → Seme-Kpodji (3 OSM-ways, gemeten, aannemelijk: grof gekarteerd Niger-deel, kop en einde = OSM-uiteinden)". Geen zeebeen (bindende toets): geen bron noemt afnemer of bestemming van de lading.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-agadem-kop` | kop van de leiding / veldzijde | OSM-begin NBEP, Agadem Rift Basin (Koulélé-gebied) | 15.3362, 13.2759 | [2] OSM-begin way 1164438280; [1] noemt Koulélé als begin; Koulélé-dorp 15.2833, 13.4000 (Nominatim [6]) | onzeker (z14 gezien: alleen woestijn, duinen en wadi's, geen installatie; ook op Koulélé-dorp z14 niets; de lijn begint waar OSM begint) |
| `ol-seme-eind` | einde: strand-landing richting SPM/terminal Seme-Kpodji | OSM-einde NBEP, kust Seme-Kpodji | 6.3654, 2.6240 | [2] OSM-einde way 1225590061; [1][5] | onzeker (z15 gezien: onbebouwde strandrand tussen woonwijken en de brekers, geen tankpark of installatie op het punt; het zichtbare tankpark ligt ~6,5 km oostelijker, zie §7) |

## 4 · Via-punten (b1 is een gestikte OSM-lijn: geen routering; alleen controlepunten op de lijn)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Zinder/SORAZ-zijde (ketenkm 493, lijn 6 km van Zinder, 29 km van SORAZ 14.1859, 8.7844) | 13.8522, 9.0106 | controle corridor Zinder; koorde van 73 km, SORAZ zelf ligt niet op de lijn [2][6] |
| b1 | 2 | waygrens Niger/Benin (ketenkm 1.228,9) | 11.8911, 3.3577 | stikplek 0 m, grens bij Gaya [2] |
| b1 | 3 | Gaya (lijn op 9,6 km) | 11.8775, 3.3616 | controle grensovergang [2] |
| b1 | 4 | Gogounou-zijde (lijn op 16,5 km; pompstation genoemd [5]) | 10.9798, 2.8577 | controle Benin-corridor [2][5] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Agadem-velden / CPF's (Koulélé, Goumeri) | CNPC | ruwe olie uit de velden → leiding | 90 kb/d na fase 2 [3] | [3] |
| SORAZ-raffinaderij (Zinder) | CNPC 60% / Niger 40% | ~20 kb/d van het veld → binnenlands product, buiten de NBEP-export | niet gebrond | [1] |
| Terminal Seme-Kpodji + SPM | WAPCO Bénin | leiding → tankopslag (2 Mbbl) → 2x28" buis → SPM ~15 km uit de kust | NBEP 110 kb/d (tag); buizen 1 Mb/d | [1][5] |

## 6 · Stoppunt
De brief stopt bij het OSM-einde aan de kust bij Seme-Kpodji: de lading gaat daar op tankers, maar geen bron koppelt een lading of afnemer aan één raffinaderij. Fase D en E vervallen; geen zeebeen.

## 7 · Open punten
- **Beide ankers onzeker (bindend):** bij Agadem is op Esri z14 geen installatie zichtbaar (OSM-begin en Koulélé-dorp); de leiding begint waar OSM begint, niet aantoonbaar bij een CPF. Goumeri-CPF (15.9543, 12.5699 [6]) is wel een installatie maar ligt 89 km van de lijn en is geen anker.
- **Seme-eindpunt:** OSM eindigt op het strand (6.3654, 2.6240); op z16 staat ~6,5 km oostelijker een bouwterrein met twee grote ronde tanks in een bund (ca. 6.3756, 2.6818), mogelijk het tankpark van het terminal (2 Mbbl [1]). Geen bron geeft er een coördinaat voor, dus geen anker en geen been; het stuk OSM-einde → tankpark blijft ongetekend.
- **Niger-deel grof gekarteerd:** 37 nodes over 1.229 km, koorden tot 128 km (ketenkm 624-752), 120 km en 113 km; de echte lijn wijkt daarvan af, SORAZ ligt 29 km van de lijn. Ook het laatste Beninse segment (7.0290, 2.6338 → 6.3654, 2.6240) is één rechte koorde van 74 km.
- **Offshore stuk** (2x28" naar de SPM ~15 km uit de kust [1]) staat niet in OSM: niet getekend.
- **Afnemer en lading ongedocumenteerd:** geen zeebeen, geen bestemming.
- **Volume werkelijk 2024** (52-107 kb/d) niet zelf gecontroleerd; aecweek en dabafinance geven geen exportvolume [3][4].
- **Lengtebronnen verschillen** (1.950 Wikipedia / 1.980 aecweek en Bluewater; Niger-deel 1.275, Benin-deel 675-685): de OSM-som ligt 4-6% eronder, binnen de ±15%-norm.
- v1-checklist (`data/oil.js`, `design/olie.md`) en de olie-sitelaag bevatten geen Niger- of Benin-site: geen coördinaat om te hergebruiken.

## 8 · Bronnen
[1] Wikipedia, "Niger–Benin Oil Pipeline" — 1.950 km (Niger 1.275, Benin 675), 20", acht pompstations, terminal Seme-Kpodji met 2 Mbbl opslag, SPM ~15 km uit de kust via 2x28", 110 kb/d capaciteit, SORAZ ~20 kb/d, onderbreking juni-aug 2024. https://en.wikipedia.org/wiki/Niger%E2%80%93Benin_Oil_Pipeline
[2] OpenStreetMap (ODbL), lokale Geofabrik-extracts niger + benin, eigen pure-Python pbf-scan 2026-10-29: ways 1164438280, 1225590062, 1225590061 (`man_made=pipeline`, `substance=oil`, operator WAPCO Bénin, ref NBEP, flow_rate 110000 b/d); som 1.869,9 km, 229 punten. https://www.openstreetmap.org/way/1225590061
[3] AEC Week, "Niger's petroleum minister joins AEW 2026…" — Agadem 20 → 90 kb/d na fase 2, leiding 1.980 km, naar Seme (geen exportvolume). https://aecweek.com/news/nigers-petroleum-minister-joins-aew-2026-amid-renewed-export-infrastructure-drive
[4] Daba Finance, 2024-08-19 — export hervat na onderbreking van juni 2024, terminal Seme-Kpodji (geen volume). https://dabafinance.com/en/news/niger-resumes-oil-exports-through-benin-after-pipeline-reopened
[5] Bluewater, "Contract award for the delivery of an export CALM buoy – Cotonou – Benin" — leiding 1.980 km waarvan 685 km in Benin, CALM-boei bij Seme-Kpodji, pompstations Gogounou en Tchatchou. https://www.bluewater.com/contract-award-for-the-delivery-of-an-export-calm-buoy-cotonou-benin/
[6] Nominatim (OSM), 2026-10-29: Koulélé 15.2833, 13.4000; Goumeri CPF 15.9543, 12.5699; SORAZ 14.1859, 8.7844; Agadem-dorp 16.8416, 13.2852. https://nominatim.openstreetmap.org
[7] Esri World Imagery via `v2/tools/sat_check.py`, `v2/build-cache/satcheck/sat-olie-agadem-seme-*.png`: agadem-osmbegin (z14), koulele-dorp (z14), seme-osmeinde (z15), seme-z13, seme-omgeving (z14), seme-tankpark (z16).
[8] Zoekresultaten, niet geopend: Africacheck (terminalstation Agadem, 403), gouv.bj (startpersbericht), Energy Voice (Bluewater CALM). Cijfers AfDB/Wereldbank komen uit het ketenontwerp.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
**Recept:** `python v2/tools/maak_leidingbeen_olie_agadem_seme.py --schrijf` (draaide al; 3 OSM-ways uit de lokale extracts niger + benin) -> `bash v2/tools/bak_stromen.sh olie-agadem-seme` (functie `bak_olie_agadem_seme`, zwaar-slot) -> `v2/data/stroomroute-olie-agadem-seme.json` (5,0 KB, versie 2, lonlat).

| # | modaliteit | km gebakken | km brief | punten | naad | stippel |
|---|---|---|---|---|---|---|
| b1 | leiding | 1.869,9 | 1.869,9 OSM-som (gepubliceerd 1.950 / 1.980 = -4,1% / -5,6%) | 229 | n.v.t. (enig been) | nee |

Totaal 1.869,9 km, 2 markers (`ol-agadem-kop` 15.3362, 13.2759; `ol-seme-eind` 6.3654, 2.6240), beide op 4 m van de lijn. Geen via-punten, geen zee, geen haven-aanloop, geen stippel, geen kopie, geen vlucht.

**Leiding:** doorgetrokken, want OSM heeft de volledige NBEP (man_made=pipeline, ref NBEP, 3 ways, naden 0 m). Het been is een vooraf gebakken FeatureCollection en is dus niet over een graaf geroutet; kop en einde zijn de OSM-uiteinden, niet aantoonbaar een CPF of tankpark (beide ankers onzeker, zie §7).

**Toets:** km binnen de +-15%-norm tegen de gepubliceerde lengte; geen naad (één been); `toets_knikken.py`: 2 knikken >= 60 graden, 0 terugloop. (a) 152,8 graden, 573 m, bij 15.3408, 13.2852: een korte OSM-uitstulping van ca. 1 km direct na het begin (de eerste node ligt oostelijk, de lijn loopt dan terug naar het westen); (b) 62,7 graden spike bij 8.0351, 2.5736 in Benin. Beide zijn OSM-geometrie en zijn niet aangepast. `toets_rechte_benen.py`: geen melding voor deze stroom (het Niger-deel bestaat uit lange OSM-koorden, tot 128 km, maar is geen stippel-kandidaat omdat OSM de leiding heeft).

**Lessen:** (1) een leidingbeen vraagt een FeatureCollection, geen kale Feature; (2) een bak zonder zeebeen heeft geen MARNET-snap en dus geen naadrisico; (3) de lengte van een grof gekarteerde OSM-leiding (hier 229 punten over 1.870 km) is een ondergrens, de werkelijke buis is langer en bochtiger.
