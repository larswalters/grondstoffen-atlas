# Routebrief (licht) · olie — Omišalj (Kroatië) → Adria-pijpleiding via Sisak en Gola → MOL Duna, Százhalombatta (Hongarije)

**stroom-id:** `olie-omisalj-szazhalombatta` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 12) · **status:** gebakken
**Keten in één zin:** Niet-Russische ruwe olie die per tanker aan de JANAF-steiger bij Omišalj (eiland Krk) aankomt, gaat per **leiding** — de Adria-pijpleiding
(Jadranski naftovod: Omišalj–Sisak 36", Sisak–Virje–Gola 28") en bij Gola over in MOL's Adria-kőolajvezeték (Csurgó, Osijek-Budapest, Sziszek-Budapest) — naar de
MOL Duna-raffinaderij bij Százhalombatta; ~477 km OSM doorgetrokken, plus twee korte stippels (3,1 km), geen zee- of landbeen.
**Welke as van het verhaal:** *de reserve-route voor Hongarije en Slowakije* — Druzhba lag van 27-1 tot 23-4-2026 stil en Kroatië kreeg de rol van alternatief; JANAF
verplaatste al in februari 2026 niet-Russische crude naar MOL [3]. **Volume: ~41 kb/d contract** (MOL-JANAF take-or-pay 2,05 Mt/j voor 2026, ×7,33/365 — afgesproken
volume, niet gemeten doorzet) [4]; 2,1 Mt/j (~42 kb/d) gold voor 2025 [5]. Ter vergelijking: ontwerpcapaciteit JANAF 34 Mt/j ≈ 680 kb/d, Omišalj-doorzet 8,1 Mt in 2020 ≈ 160 kb/d [2];
Kroatië noemt voor het Omišalj–Hongarije-deel 11–15 Mt/j, onafhankelijk nog niet getoetst [4][6]. Peiljaar 2026. Dit is een **tweede route naar MOL**, geen volledige Druzhba-vervanger.

## 1 · Ketenkaart
```
[tanker aan de steiger, herkomst niet gebronnen]
JANAF-terminal Omišalj `ol-omisalj-terminal` ──(b1 leiding, STIPPEL · terminal-interne leidingen, OSM-manifold niet doorlopend · 1,9 km)──►
  begin Omišalj–Sisak (45,2069/14,5481) ──(b2 leiding · Jadranski naftovod Omišalj–Sisak 36" → Sisak–Virje–Gola 28" · 285,1 km OSM, ~283 gepubliceerd)──►
  JANAF Sisak `ol-sisak-hub` (overslag/tankpark, middenin b2) … Gola → HR/HU-grens (46,1861/17,0823) ──(b3 leiding · MOL Adria-kőolajvezeték · 191,6 km OSM)──►
  einde Sziszek-Budapest (47,2777/18,9086) ──(b4 leiding, STIPPEL · binnen het raffinaderijterrein · 1,1 km)──► MOL Duna `ol-mol-duna` ── stoppunt
```
b2 is bij Sisak één doorgetrokken lijn (het knooppunt zit op de lijn, geen nieuw been). Géén zeebeen: de aanvoer per tanker is wel gedocumenteerd [3] maar zonder herkomsthaven.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Omišalj-terminal → begin Omišalj–Sisak | terminal-interne leidingen (36"-aansluiting) | 1,9 hemelsbreed, geen bronlengte | `--stippel` | **ja** — OSM kent alleen losse manifold-stukjes (zigzag), geen doorlopende lijn tot de leiding |
| b2 | A | leiding | begin Omišalj–Sisak → Sisak → Virje → Gola → HR/HU-grens | Jadranski naftovod (JANAF): Omišalj–Sisak 36", Sisak–Virje–Gola 28" | 285,1 OSM tegen 176 + 107 = 283 gepubliceerd (planlengtes 1966, **+0,7%**) [1][7] | OSM-ways, gestikt (§4) | nee |
| b3 | B | leiding | HR/HU-grens → einde Sziszek-Budapest bij Százhalombatta | MOL Adria-kőolajvezeték: Csurgó, Osijek-Budapest, Sziszek-Budapest | 191,6 OSM, **geen gepubliceerde lengte** [7] | OSM-ways, gestikt (§4) | nee |
| b4 | B | leiding | einde Sziszek-Budapest → `ol-mol-duna` | binnen MOL-terrein | 1,1 hemelsbreed | `--stippel` | **ja** — OSM-gat in de buis, eindpunt ligt tussen de tankparken [8] |

Totaal 479,7 km tegen ~520 uit het ontwerp en 408 hemelsbreed; b2+b3 samen 476,7 km. Gestippeld 3,1 km (0,6%), de rest doorgetrokken. Fase C/D/E vervallen: geen bron koppelt deze lading aan een afnemer voorbij MOL Duna.
Geofabrik-regio's (voor context, de geometrie komt uit de OSM-pijplijnlaag): `kroatie`, `hongarije`.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-omisalj-terminal` | kop / laadplek (tankpark en steiger) | JANAF-terminal Omišalj, eiland Krk (HR) | 45.2208, 14.5331 | [2][7][8] | bron-gelegd (z15 gezien: tankenpark van ~20 tanks op het smalle schiereiland, een rood tankschip aan de steiger op de noordpunt) |
| `ol-sisak-hub` | overslag/pompstation, splitsing naar Slavonski Brod | JANAF Sisak (HR) — OSM-eindknoop van way 275828600 | 45.4375, 16.4115 | [1][2][7] | bron-gelegd (z15 gezien: omheind tankenpark van ~12 tanks met pompgebouwen, het punt ligt midden in het terrein, 3 m van de OSM-pijp) |
| `ol-mol-duna` | eindpunt / losplek raffinaderij | MOL Duna-raffinaderij, Százhalombatta (HU) — **hergebruik letterlijk** uit `olie-unecha-szazhalombatta.md` | 47.2879, 18.9072 | [9] | bron-gelegd (z15 gezien: oostrand van het tankenpark, bos en de Donau 0,3 km oostwaarts; een tweede tankgroep ligt 1,1 km ZZW waar de Sziszek-Budapest-buis eindigt) |
Het anker `ol-mol-duna` is gedeeld met stroom `olie-unecha-szazhalombatta` (zelfde marker, geen tweede punt); de benen zijn niet gedeeld (Druzhba komt uit het noorden via Barátság I).

## 4 · Via-punten (stik-knopen; geen wegbeen — alleen waar een corridorkeuze of way-overgang de streng vastlegt)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | begin Omišalj–Sisak (way 276522179) | 45.2069, 14.5481 | het gat met b1 (1,9 km vanaf het anker); de buis loopt langs de kust naar 45,2315/14,5587 en gaat dan noord |
| b2 | 2 | baai-onderkruising | 45.2430, 14.5950 → 45.2380, 14.5885 | way 859729755 (`location=underwater`, 0,75 km) is de echte leiding; gestikt op gelijke eindpunten, geen stippel |
| b2 | 3 | Sisak | 45.4375, 16.4115 | way 275828600 (104,1 km) eindigt hier; naad 20 m naar 580473505. **Sluit uit:** 847788794 (Sisak–Slavonski Brod, 28") |
| b2 | 4 | Gola-knoop | 46.0942, 17.0147 | **de corridorkeuze**: Sisak–Virje–Gola (580473505) loopt door naar Hongarije; sluit 1050320058 (Virje–Lendava, 12", naar Slovenië) uit |
| b2/b3 | 5 | HR/HU-grens | 46.1861, 17.0823 | uiteinde b2 = begin b3 (way 930166671 'Adria-kőolajvezeték'), naad 0 m |
| b3 | 6 | Csurgó-knoop | 46.3046, 17.3817 | Budapest-Csurgó (970100735) loopt hier in Osijek-Budapest (970100734, 5,8 km spoel) en dan door 970087404 → 970041355 → 969606494 |
| b3 | 7 | Sziszek-Budapest | 46.9686, 18.4815 | wayovergang naar 968260293 → 968438280 (einde 47,2777/18,9086) |
**Uitsluiten bij het stikken** (andere buizen met dezelfde Hongaarse namen): Barátság I en II (580260776, 566241458 = Druzhba), 553875773 (MOL-pijp naar het oosten), Adria-Wien (236430356, TAL-aftakking in Oostenrijk), Slavonski Brod–Sotin (879643929).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| JANAF Omišalj (tankpark + steiger) | JANAF | tankers → Adria-pijpleiding | doorzet 8,1 Mt in 2020 (6,6 Mt in 2019); ontwerp 34 Mt/j | [2] |
| JANAF Sisak (tankpark, splitsing) | JANAF | doorvoer, geen verwerking | opslagterminal; geen apart cijfer | [2] |
| MOL Duna-raffinaderij, Százhalombatta | MOL Nyrt. | ruwe olie (Adria én Druzhba) → producten | 8,1 Mt/j ≈ 163 kb/d; CDU AV-3 brand 20-10-2025, herstel klaar 22-9-2026 | [9][10] |

## 6 · Stoppunt
De brief stopt bij de MOL Duna-raffinaderij: de buis eindigt daar, het product wordt in Hongarije verwerkt, en geen bron koppelt deze lading aan een specifieke eindafnemer. De aftakkingen naar Slovnaft (Bratislava), Serbië (Pančevo, Novi Sad) en Slovenië (Lendava) zijn niet deze keten.

## 7 · Open punten
- **Volume**: alleen het contractvolume (2,05 Mt/j in 2026, take-or-pay, aangekondigd 6-8-2026) [4]; de feitelijk geleverde tonnen naar MOL zijn niet gevonden. Slovnaft hield in okt-2025 een geschil met JANAF over 90.000 t [6].
- **Herkomst van de lading**: tankers met niet-Russische crude (acht tankers voor MOL tot begin april 2026, alleen uit een kop) [3]; geen herkomsthaven, dus geen zeebeen.
- **Geen gepubliceerde lengte voor b3**; b2 is vergeleken met de planlengtes van 1966 (176 + 107 km), niet met as-built [1]. De ±15%-toets is voor b3 een indicatie.
- **Twee OSM-gaten** zijn stippel (b1 1,9 km, b4 1,1 km); de eerste omdat de terminal-leidingen in OSM een manifold van losse stukken zijn, de tweede omdat Sziszek-Budapest 1,1 km voor het MOL-anker ophoudt.
- **Parallelle MOL-buizen**: de Hongaarse ways heten deels 'Osijek-Budapest' en 'Budapest-Csurgó'; of dit de actief gebruikte strang is, is niet gecontroleerd (alleen de naam en de gedeelde eindpunten).
- Capaciteitsclaims van Kroatië (11–15 Mt/j) zijn niet onafhankelijk getoetst [4][6]. Druzhba loopt sinds 23-4-2026 ook weer [3]: dit is dus een tweede route, geen vervanging.
- `ol-sisak-hub` en `ol-omisalj-terminal` zijn site-niveau (z15), niet op de meter gelegd.

## 8 · Bronnen
[1] Wikipedia, "Adria oil pipeline" — route Omišalj → Sisak → Virje → Gola → Százhalombatta, planlengtes 1966 (176 / 107 km), Hongaarse sectie 10 Mt/j. https://en.wikipedia.org/wiki/Adria_oil_pipeline
[2] Wikipedia, "Jadranski naftovod" — ~759 km totaal, ontwerp 34 Mt/j, terminals Omišalj/Sisak/Virje/Slavonski Brod, doorzet 6,6 Mt (2019) en 8,1 Mt (2020). https://en.wikipedia.org/wiki/Jadranski_naftovod
[3] Wikipedia, "2026 Druzhba pipeline dispute" — 25-2-2026 JANAF verplaatst niet-Russische crude naar Hongarije en Slowakije, begin maart 'significante hoeveelheden' voor MOL, Druzhba-zuidtak weer open 23-4-2026. https://en.wikipedia.org/wiki/2026_Druzhba_pipeline_dispute
[4] Hungarian Conservative, 6-8-2026, "MOL and JANAF Seal New Adriatic Pipeline Deal" — 2,05 Mt take-or-pay voor 2026 (terugwerkend vanaf 1-1), 2,1 Mt in 2025, Kroatië claimt 11–15 Mt/j. https://www.hungarianconservative.com/articles/current/mol-janaf-adriatic-pipeline-supply-route-oil-transit-energy-hungary-croatia/
[5] PGJ Online, 20-12-2025, "Croatia's JANAF and MOL close in on expanded oil transport deal" — 2,1 Mt/j in het lopende contract, MOL vroeg 2–11 Mt. https://pgjonline.com/news/2025/december/croatias-janaf-and-mol-close-in-on-expanded-oil-transport-deal
[6] Zoekresultaat-samenvatting (2026-10-29; pagina's niet zelf geopend) — JANAF: Omišalj–Hongarije 12,9–14,5 Mt/j, Slovnaft-geschil 90.000 t. https://www.portfolio.hu/en/energy/20250925/croatia-refutes-claims-that-it-could-not-supply-hungary-with-oil-788632 · https://ceenergynews.com/oil-gas/plenkovic-janaf-capacity-prices/
[7] OpenStreetMap (ODbL) via Overpass (overpass-api.de), 2026-10-29: ways 276522179, 859729754–56, 275847496/97, 263222529, 276191744, 275828600, 580473505, 1050335120 (Jadranski naftovod) en 930166671, 970100735, 970100734, 970087404, 970041355, 969606494, 968260293, 968438280 (MOL); lengtes en eindpunten gemeten. https://www.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py` (z14/z15): `v2/build-cache/satcheck/sat-olie-omisalj-szazhalombatta-{omisalj,omisalj-terminal,omisalj-zuid,sisak,molduna}.png`.
[9] `v2/design/routebrieven/olie-unecha-szazhalombatta.md` — anker `ol-mol-duna` 47.2879/18.9072 (bron-gelegd), Duna 8,1 Mt/j ≈ 163 kb/d.
[10] Oil & Gas Journal, 25-9-2026, "MOL wraps repairs on major unit at Hungarian refinery" — AV-3 brand 20-10-2025, herstel 22-9-2026 (via [9]). https://www.ogj.com/refining-processing/news/55407912/mol-wraps-repairs-on-major-unit-at-hungarian-refinery

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 12)
**Bestand:** `v2/data/stroomroute-olie-omisalj-szazhalombatta.json` (35,8 KB, versie 2, lonlat) · functie `bak_olie_omisalj_szazhalombatta` in `v2/tools/bak_stromen.sh` · geen profiel, geen zee-, weg- of luchtbeen.
| # | modaliteit | km | punten | naad | opmerking |
|---|---|---|---|---|---|
| 1 | leiding, **stippel** | 1,9 | 2 | 0 | Omišalj-terminal naar begin way 276522179 (OSM-manifold niet doorlopend) |
| 2 | leiding | 285,1 | 1282 | 0,0 | Jadranski naftovod, a1 (brief 283 planlengte, +0,7%) |
| 3 | leiding | 191,6 | 505 | 0,0 | MOL Adria-kőolajvezeték, a2 (geen gepubliceerde lengte: indicatie) |
| 4 | leiding, **stippel** | 1,1 | 2 | 0,0 | einde Sziszek-Budapest naar `ol-mol-duna` (OSM-gat in het terrein) |
Totaal 479,7 km, 1791 punten, 3 markers (`ol-omisalj-terminal`, `ol-sisak-hub`, `ol-mol-duna`; alle op of binnen 3 m van de lijn). Stippel 3,1 km (0,6%).
**Recept:** `python v2/tools/maak_leidingbeen_olie_omisalj_szazhalombatta.py --schrijf` (leest de Overpass-cache, schrijft a1 en a2 als FeatureCollection), daarna `bash v2/tools/bak_stromen.sh olie-omisalj-szazhalombatta`.
**Toets:** km binnen de norm (b2 +0,7%; b3 zonder bronlengte), naden 0 tot 20 m (Sisak-overgang 19,8 m is binnen het gestikte stuk), markers op de lijn, knikken: 8 >= 60 graden, 0 omkeringen, 0 terugloop (spikes bij de wayovergangen Virje/Gola en Csurgó, niet gerepareerd). Alle modaliteiten `leiding`.
**Stippels:** b1 en b4 zijn terminal- resp. raffinaderij-interne leidingen waar OSM een gat of losse manifold-stukken heeft; ze zijn "hier reikt het net niet", geen onzekerheid over de keten.
**Wijkt niet af van het ontwerp:** eindpunt is MOL Duna zoals het id belooft; geen zeebeen omdat de tankerherkomst niet gebronnen is.
**Lessen:** een leidingketen waarvan OSM de buis volledig kent (Adria-pijpleiding) bakt zonder profiel of slot en zonder stippel van betekenis; de stikscript-aanpak (way-voor-way, uitsluitlijst voor Druzhba en TAL) werkt.
