# Routebrief (licht) · gas — West Natuna (Indonesië) → WNTS → Pulau Sakra, Jurong Island (Singapore)

**stroom-id:** `gas-westnatuna-sakra` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) ·
**status:** gebakken
**Keten in één zin:** Gas uit de West Natuna-velden (Block B-consortium, operator Conoco/ConocoPhillips) gaat via één
doorlopende onderzeese leiding, de West Natuna Transportation System (WNTS, 28 inch), door de Natuna Zee en de Straat van
Singapore naar de ontvangstinstallatie op Pulau Sakra (Jurong Island): Singapores eerste pijpgasimport, koper Sembcorp Gas.
**Welke as van het verhaal:** Indonesisch pijpgas naar Singapore (stroom, petrochemie op Jurong Island) — ontwerpcapaciteit
325 MMscf/d ≈ 3,4 bcm/j [1][2][3]; actuele doorzet niet gevonden, peiljaar 2001 (verouderd, zie §7). Eerste gas januari 2000
of 2001 (bronnen verschillen) [1][3].

## 1 · Ketenkaart
```
West Natuna Block B-velden (Anoa, Kakap, Belida, Buntal, Tembang, Belanak; platform niet gematcht)
  `gas-wnts-begin`  (OSM-begin WNTS, offshore)
  ──(b1 leiding · WNTS 28-inch trunk, Natuna Zee en Straat van Singapore · 596,1 km OSM; gepubliceerd 640–656)──►
Pulau Sakra, Jurong Island — ontvangstinstallatie  `gas-sakra-landing`  (stoppunt; koper Sembcorp Gas)
```
Totaal doorgetrokken 596,1 km, één FeatureCollection. Geen stippel: OSM heeft de leiding doorlopend (way 182146492).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-wnts-begin` → `gas-sakra-landing` | West Natuna Transportation System (WNTS), OSM way 182146492 (man_made=pipeline, substance=gas, submarine=yes, 120 knopen) | 596,1 OSM tegen 656 [1][5] (−9,1%) en 640 [2][3][6] (−6,9%); hemelsbreed 489 km, geen wegkm | OSM-pipeline, 1 way (`maak_leidingbeen_gas_westnatuna_sakra.py`), FeatureCollection | nee |

Beennaam: `leiding|West Natuna Transportation System (WNTS) West Natuna → Pulau Sakra (aannemelijk: één bron, peiljaar 2001)`.
Fase B/C/D/E vervallen: de leiding is de hele keten; geen zee-, spoor- of wegbeen, geen haven-aanloop.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-wnts-begin` | kop leiding (gasverzamelpunt Block B) | WNTS-begin, South Natuna Sea Block B, offshore | 5.2275, 105.5915 | [4][6] | aannemelijk (OSM-way-begin; platform Block B niet gematcht; Esri z14 toont hier "Map data not yet available", open zee: niets te zien) |
| `gas-sakra-landing` | ontvangstinstallatie (staart, stoppunt) | Pulau Sakra, Jurong Island | 1.2520, 103.6989 | [3][4][8] | bron-gelegd (z15 gezien: zuidwestpunt van het opgespoten Sakra-land, groene strook aan de kustlijn; 0,3 km noordoostwaarts de installaties, tankenparken en pieren van Jurong Island; punt = OSM-eindknoop way 182146492) |

Hergebruik: geen — Singapore en Natuna staan niet in eerdere brieven of in `gas-sitelaag.json`. Wel raakt `goud-kalgoorlie-singapore` Singapore (Changi, Anson Road), maar dat is een ander terrein, geen gedeeld anker of been.

## 4 · Via-punten
Niet van toepassing: één OSM-leiding, geen corridorkeuze door ons te leggen. De way heeft grote segmenten (tot 69 km; 5 van > 30 km):
spaarzame kartering van een subsea-leiding, geen sprong tussen ways. Gecontroleerd tegen `ne_10m_land` en minor islands: 0 snijpunten met land.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| WNTS-begin (offshore verzameling Block B + 2 andere PSC's, 17 velden) | Conoco/ConocoPhillips Indonesia (operator), later Medco | velden → 28-inch trunk | 325 MMscf/d (3,4 bcm/j) [2][3] | [1][2][3] |
| Ontvangstinstallatie Singapore | ConocoPhillips Singapore Operations; koper Sembcorp Gas | WNTS → Jurong Island (Sembcorp Gas, stroom, petrochemie) | 325 MMscf/d contract, 22 jaar [1] | [1][3] |

## 6 · Stoppunt
De brief stopt bij de ontvangstinstallatie op Pulau Sakra: één bron noemt Sembcorp Gas als koper met levering aan Jurong Island [1],
maar daarna verdwijnt het gas anoniem in stroom, brandstof en crackers; geen bron volgt een lading naar één fabriek. Fase D/E vervalt.

## 7 · Open punten
- **Actuele doorzet niet gevonden.** Alleen contract/capaciteit (325 MMscf/d, 3,4 bcm/j) en een opstartvolume 1,55 bcm/j uit het ketenontwerp (niet zelf teruggevonden). Jaarvolume op de bol = capaciteit, peiljaar 2001, geen meting.
- **2025–2026: Indonesië stuurt gas terug naar binnenlands gebruik.** SKK Migas zegt dat Natuna-gas dat nu naar Singapore stroomt wordt omgeleid [7]; WNTS–Pemping (naar Batam/PLN) is in aanleg, tie-in overeengekomen, gas-in gemeld oktober 2026 [7]. De leiding bestaat en wordt getekend; de export kan dalen.
- **Begin-platform onbekend:** 5.2275, 105.5915 is alleen het OSM-way-begin. Geen bron noemt het platform of een coördinaat; open zee, geen satellietbeeld.
- **Lengte:** OSM 596,1 km tegen 656 [1] en 640 [2][3][6] (−7 tot −9%); binnen de ±15%-norm. Diameter: 28 inch [5] tegen 18 inch [2] — we volgen [5].
- **Startjaar:** Petromindo noemt 3 januari 2000 (in een artikel van 2001), Global Energy Monitor 2001 [1][6]; niet beslecht.
- **Naam Sakra:** geen enkele geraadpleegde bron noemt Pulau Sakra als aanlanding (alleen Jurong Island [3][8]); de naam komt uit het ketenontwerp en de OSM-eindknoop. Sakra Jetty is Exxon-eigendom [8], dus niet de gasinstallatie.

## 8 · Bronnen
[1] Petromindo, "First gas delivery from Natuna to Singapore" (2001) — 656 km, operator Conoco, eerste gas 3 januari. https://www.petromindo.com/news/article/press-release-first-gas-delivery-from-natuna-to-singapore ; ook "Indonesia, Singapore launch West Natuna gas project": 325 MMscf/d, 22 jaar, Sembcorp Gas, Jurong Island. https://www.petromindo.com/news/article/indonesia-singapore-launch-west-natuna-gas-project
[2] Offshore Technology, "Natuna Gas Project" — 640 km, 3,4 bcm/j, 325 mmscf/d, velden Anoa/Kakap/Belida/Buntal/Tembang/Belanak, koper SembGas. https://www.offshore-technology.com/projects/natuna/
[3] Wikipedia (EN), "Jurong Island" — gas uit West Natuna arriveert via een 640 km onderzeese leiding. https://en.wikipedia.org/wiki/Jurong_Island
[4] OSM-API (ODbL), way 182146492 — West Natuna Transportation System (WNTS), man_made=pipeline, substance=gas, submarine=yes, 120 knopen, 596,1 km, begin 5.22755, 105.59151, eind 1.25196, 103.69888. https://api.openstreetmap.org/api/0.6/way/182146492/full
[5] Oil & Gas Journal, "Indonesia-Singapore line gets sales pacts" — 28-inch, 300-mijl onderzeese leiding. https://www.ogj.com/home/article/17230326/indonesia-singapore-line-gets-sales-pacts
[6] Global Energy Monitor, "West Natuna Transportation System Gas Pipeline" — 640 km, 3,4 bcm/j, start 2001, operator CIIL, eigenaar Medco. https://www.gem.wiki/West_Natuna_Transportation_System_Gas_Pipeline
[7] Listrik Indonesia, "PLN EPI, WNTS, dan SKK Migas sepakati penyambungan pipa Natuna–Pemping" — tie-in WNTS–Pemping, omleiding Singapore-gas naar binnenlands gebruik. https://listrikindonesia.com/detail/19118/pln-epi-wnts-dan-skk-migas-sepakati-penyambungan-pipa-natunapemping ; S&P Global (2025-08-22, niet te openen: 403) https://www.spglobal.com/commodity-insights/en/news-research/latest-news/lng/082225-indonesia-launches-multiparty-gas-swap-system-to-secure-domestic-supply
[8] Wikipedia (EN), "Jurong Island" — Sakra Jetty (ExxonMobil), Oasis@Sakra; Nominatim (ODbL): Oasis @ Sakra 1.2686, 103.7050. https://nominatim.openstreetmap.org
[9] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-gas-westnatuna-sakra-sakra.png` (z15), `-begin.png` (z14, geen data offshore).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
**Bestand:** `v2/data/stroomroute-gas-westnatuna-sakra.json` (3,0 KB, versie 2, lonlat) · **functie:** `bak_gas_westnatuna_sakra()` in `v2/tools/bak_stromen.sh` · **recept:** `bash v2/tools/bak_stromen.sh gas-westnatuna-sakra`.
**Titel:** Gas · West Natuna (Block B) → WNTS-leiding → Pulau Sakra, Jurong Island (Singapore). Eindpunt klopt met het id (Pulau Sakra); het beginpunt is alleen het OSM-way-begin van de WNTS offshore, geen gematcht platform.

| # | modaliteit | been | km gemeten | km brief | punten | stippel |
|---|---|---|---|---|---|---|
| 1 | leiding | West Natuna Transportation System (WNTS) West Natuna naar Pulau Sakra (aannemelijk: een bron, peiljaar 2001) | 596,1 | 656 Petromindo / 640 Offshore Technology en GEM | 120 | nee |

Totaal 596,1 km · 1 been · 2 markers · naden: geen (een been). Afwijking t.o.v. 656 is -9,1%, t.o.v. 640 is -6,9%: binnen de norm, en dit is een echte leidinglengte (hemelsbreed 489 km, geen wegkm).
**Markers:** WNTS-begin 0,006 km van de lijn, Pulau Sakra 0,005 km (beide staan op de OSM-way-uiteinden, anker gelijk aan routeerpunt).
**Toelichting leiding:** doorgetrokken, want OSM heeft de hele onderzeese leiding als een way (182146492, man_made=pipeline, substance=gas, submarine=yes). Geen offshore- of ontbrekend stuk, dus geen stippel. Het grootste segment (69 km) is spaarzame kartering van een subsea-leiding, geen naad tussen ways. Geometrie vooraf gestikt door `v2/tools/maak_leidingbeen_gas_westnatuna_sakra.py` (FeatureCollection, `v2/build-cache/ais/graaf/gas-westnatuna-sakra-leiding.geojson`, 0 snijpunten met land).
**Niet getekend:** geen zee-, spoor- of wegbeen, geen haven-aanloop, geen via-punten, geen kopie, geen luchtbeen (dus geen profiel in `maak_stroombeen_weg.py`); fase B/C/D/E vervallen.
**Toets:** `toets_knikken` 0 knikken, 0 omkeringen, 0 terugloop. `toets_rechte_benen --min-km 5`: geen melding voor deze stroom. json.load, versie 2, punt_formaat lonlat, modaliteit leiding, 120 punten.
**Open (uit §7, niet beslecht):** actuele doorzet onbekend (capaciteit 325 MMscf/d, peiljaar 2001); export kan dalen door de WNTS-Pemping-omleiding 2025-2026; begin-platform en de naam Sakra als aanlanding in geen bron bevestigd.
**Lessen:** (1) een-been-pijp met vooraf gestikt geojson bakt in ~17 s onder het zwaar-slot. (2) Een gelijktijdige edit van een andere agent in `bak_stromen.sh` kan tijdens een run een kortstondige syntaxfout (regel ~13160, andermans functie) geven nadat het bestand al geschreven is; `bash -n` achteraf was schoon en het json stond er. (3) Een offshore leiding heeft geen satellietbeeld: het anker blijft aannemelijk.
