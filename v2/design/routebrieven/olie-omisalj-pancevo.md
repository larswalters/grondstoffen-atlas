# Routebrief (licht) · olie — Omišalj (Kroatië) → JANAF-oosttak via Sisak, Slavonski Brod en Novi Sad → NIS-raffinaderij Pančevo (Servië)

**stroom-id:** `olie-omisalj-pancevo` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) · **status:** gebakken
**Keten in één zin:** Niet-Russische ruwe olie die per tanker aan de JANAF-steiger bij Omišalj (Krk) aankomt, gaat per **leiding** — Jadranski naftovod Omišalj–Sisak, dan de oosttak Sisak–Slavonski Brod–Sotin–Novi Sad — naar de NIS-raffinaderij Pančevo; ~544 km OSM doorgetrokken, plus twee stippels (1,9 en 22,5 km), geen zee- of landbeen.
**Welke as van het verhaal:** *de sanctie-kwetsbare Servische slagader* — Pančevo krijgt al zijn ruwe olie via JANAF [1][2]; sinds de OFAC-sancties op NIS (9-10-2025) viel de aanvoer stil (raffinaderij stil 2-12-2025, herstart half jan 2026) en loopt hij op tijdelijke OFAC-licenties, de laatste bekende tot 30-9-2026 [3][4]. **Volume: ~96 kb/d** = Pančevo-capaciteit 4,8 Mt/j × 7,33 / 365 (capaciteit, geen gemeten doorzet) [2][5]; peiljaar 2025. Het JANAF-NIS-transportcontract loopt tot eind 2026 [2].

## 1 · Ketenkaart
```
[tanker aan de steiger, herkomst niet gebronnen]
JANAF-terminal Omišalj `ol-omisalj-terminal` ──(b1 leiding, STIPPEL · terminal-intern · 1,9 km)──► begin Omišalj–Sisak (45,2069/14,5481)
  ──(b2 leiding · Jadranski naftovod Omišalj–Sisak 36" · 177,1 km OSM, LETTERLIJKE KOPIE van olie-omisalj-szazhalombatta)──► JANAF Sisak `ol-sisak-hub`
  ──(b3 leiding · JANAF-oosttak Sisak–Slavonski Brod–Sotin–Novi Sad · 367,1 km OSM, 2 naden)──► NIS Novi Sad `ol-nis-novisad` (leiding passeert, naad 1,2 km)
  … einde OSM-leiding (45,0054/20,5401) ──(b4 leiding, STIPPEL · OSM eindigt · 22,5 km)──► NIS Pančevo `ol-nis-pancevo` ── stoppunt
```
Geen zeebeen: aanvoer per tanker is wel de logica van Omišalj, maar geen bron noemt herkomsthaven of schip voor deze lading.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Omišalj-terminal → begin Omišalj–Sisak | terminal-interne leidingen | 1,9 hemelsbreed | `--stippel`, **kopie** van b1 van `olie-omisalj-szazhalombatta` | **ja** — OSM-manifold niet doorlopend |
| b2 | A | leiding | begin Omišalj–Sisak → Sisak | Jadranski naftovod Omišalj–Sisak 36" | 177,1 OSM tegen 176 planlengte 1966 (+0,6%) [6][7] | **kopie**: eerste 9 ways van a1 van `olie-omisalj-szazhalombatta` (276522179 … 275828600) | nee |
| b3 | A | leiding | Sisak → einde OSM bij Pančevo | Jadranski naftovod: Sisak–Slavonski Brod 155,2 · Brod–Sotin 143,9 · Servië-deel 66,6 = 365,7 + 1,4 naad | 367,1 OSM, **geen gepubliceerde lengte** (indicatie) [7] | OSM-ways, gestikt (§4), eigen `maak_leidingbeen_olie_omisalj_pancevo.py` | nee (naad 0,28 en 1,19 km gestikt, zie §7) |
| b4 | B | leiding | einde OSM (45,0054/20,5401) → `ol-nis-pancevo` | geen gekarteerde leiding | 22,5 hemelsbreed | `--stippel` | **ja** — OSM-leiding eindigt, buis niet gekarteerd [7][8] |

Totaal 568,6 km (b1 1,9 + b2 177,1 + b3 367,1 + b4 22,5); stippel 24,4 km (4,3%), rest doorgetrokken. Fase C/D/E vervallen: geen bron koppelt deze lading aan een afnemer voorbij de raffinaderij. Geofabrik-regio's (context): `kroatie`, `servie`.
b2 en het begin van b3 zijn dezelfde lijn als `olie-omisalj-szazhalombatta` tot Sisak; de **Sisak–Gola-tak** wordt NIET meegenomen.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-omisalj-terminal` | kop / laadplek | JANAF-terminal Omišalj, Krk (HR) — **hergebruik letterlijk** uit `olie-omisalj-szazhalombatta.md` | 45.2208, 14.5331 | [6][7] | bron-gelegd (daar: tankenpark ~20 tanks, tankschip aan de steiger) |
| `ol-sisak-hub` | overslag/pompstation, splitsing | JANAF Sisak (HR) — **hergebruik letterlijk** uit `olie-omisalj-szazhalombatta.md` | 45.4375, 16.4115 | [6][7] | bron-gelegd (daar: omheind tankenpark ~12 tanks) |
| `ol-nis-novisad` | doorvoer/tankpark op de leiding | NIS-raffinaderij Novi Sad (RS) — oostelijke tankgroep | 45.2780, 19.8720 | [1][2][7][9] | bron-gelegd (z15 gezien: groot tankenpark met ~30 tanks en procesunits, de OSM-leiding loopt 0,3–1,3 km noordelijk langs het terrein, een weg ertussen) |
| `ol-nis-pancevo` | eindpunt / losplek raffinaderij | NIS-raffinaderij Pančevo (RS) — OSM-landuse `refinery`, way 68321105 | 44.8310, 20.6860 | [2][5][8] | bron-gelegd (z15 gezien: procesunits en tankenpark met ~50 bol- en dakentanks aan de oostrand van Pančevo, het punt ligt tussen de procesunits en de tankparken; de petrochemie van HIP ligt 2,5 km westelijk en is niet dit terrein) |
Het OSM-einde (45.0054/20.5401, open akkerland, z15 gezien: geen leiding of werkterrein zichtbaar, ondergrondse buis) is geen anker.

## 4 · Via-punten (stik-knopen; geen wegbeen — alleen waar een way-overgang of corridorkeuze de streng vastlegt)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | begin Omišalj–Sisak (way 276522179) | 45.2069, 14.5481 | gat met b1; zelfde ways 276522179, 859729756/55/54, 275847497/96, 263222529, 276191744, 275828600 als in `olie-omisalj-szazhalombatta` |
| b2/b3 | 2 | Sisak | 45.4375, 16.4115 | way 275828600 eindigt; naad 18 m naar 847788794. **Sluit uit:** 580473505 (Sisak–Virje–Gola, naar Hongarije) |
| b3 | 3 | Sisak–Slavonski Brod | 45.1712, 17.9515 | 847788794 (140,7 km) eindigt, begint 1165593222 (14,5 km, 'Sisak-Slavonski Brod') |
| b3 | 4 | Slavonski Brod-naad | 45.1673, 18.1274 → 45.1670, 18.1310 | **naad 0,28 km**: 1165593222 → 879643929 (Brod–Sotin, 82,3 km, in omgekeerde richting). Knikken 80–90° bij 18,12–18,15 (pompstation/aftakking) zijn OSM-vorm |
| b3 | 5 | Sotin | 45.2794, 19.1333 | 879643929 → 1057915310 (0,9 km) → 1055540678 (60,7 km, naamloos, oil) |
| b3 | 6 | Novi Sad west | 45.3073, 19.8736 | 1055540678 eindigt; 1165598505 (2,6 km) zakt naar 45.2850/19.8625 |
| b3 | 7 | **naad NIS Novi Sad** | 45.2850, 19.8625 → 45.2794, 19.8755 | **rechte naad 1,19 km** over/langs het raffinaderijterrein tussen 1165598505 en 1165601440 (OSM-gat in de buis); gestikt, niet gestippeld, op bindend advies toets |
| b3 | 8 | Novi Sad oost → einde | 45.2851, 19.8940 → 45.0054, 20.5401 | 1165601440 (2,0 km), dan 1055818470 (62,0 km, naamloos, oil) = einde OSM |
**Uitsluiten bij het stikken:** 879643929 mag niet vooruit gelezen worden (richting omkeren), Sisak–Gola-tak (580473505, 1050335120) en alle MOL-ways, Virje–Lendava 1050320058, Druzhba-ways. Overpass was bij dit onderzoek onbereikbaar: de geometrie komt via de OSM-API (way- en node-cache `v2/build-cache/olie-omisalj-pancevo-osmapi-cache.json`).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| JANAF Omišalj (tankpark + steiger) | JANAF | tankers → Adria-pijpleiding | ontwerp 34 Mt/j | [10] |
| JANAF Sisak (tankpark, splitsing) | JANAF | doorvoer naar oost (Brod/Sotin) en west/noord (Gola) | opslagterminal | [10] |
| NIS Novi Sad-raffinaderij | NIS | tankpark/doorvoer op de leiding | 2,6 Mt/j (verwerking) | [2] |
| NIS Pančevo-raffinaderij | NIS (Gazprom Neft hoofdaandeelhouder; MOL-overname 56,15% gemeld) | ruwe olie (uitsluitend JANAF) → producten | 4,8 Mt/j ≈ 96 kb/d | [2][5][11] |

## 6 · Stoppunt
De brief stopt bij de NIS-raffinaderij Pančevo: de buis eindigt daar, producten gaan naar de Servische markt en geen bron koppelt deze lading aan een specifieke eindafnemer.

## 7 · Open punten
- **Volume**: alleen de capaciteit (4,8 Mt/j) — "alle ruwe olie via JANAF" [5]; feitelijke doorzet of contractvolume niet gevonden (een tekst noemde 10 Mt in 3 jaar, **niet** bevestigd).
- **Sanctietoestand na 30-9-2026**: OFAC-licentie voor JANAF-transport naar NIS liep tot 30-9-2026 [3]; MOL-onderhandelingslicentie tot 30-10-2026, MOL ontkent een getekend akkoord (Wikipedia, 21-10-2026) [11]. Of verlengd is niet gecontroleerd.
- **Stippel b4 (22,5 km)**: de OSM-leiding stopt bij 45.0054/20.5401, 22,5 km voor de raffinaderij; het werkelijke tracé daarna is niet gevonden en wordt niet verzonnen (hemelsbreed).
- **Naden in b3**: 0,28 km bij Slavonski Brod en 1,19 km langs NIS Novi Sad zijn OSM-gaten, rechtstreeks gestikt; de ±15%-toets is voor b3 een indicatie (geen gepubliceerde lengte).
- **Herkomst van de lading** niet gebronnen, dus geen zeebeen. 14 knikken ≥ 60° in b3 (Brod, Sotin, Novi Sad) zijn OSM-vorm, niet gerepareerd.
- `ol-nis-novisad` en `ol-nis-pancevo` zijn site-niveau (z15), niet op de meter gelegd.

## 8 · Bronnen
[1] Wikipedia, "Adria pipeline" — leiding loopt in Servië tot Novi Sad en verder naar Pančevo. https://en.wikipedia.org/wiki/Adria_pipeline
[2] Wikipedia, "Naftna Industrija Srbije" — Pančevo 4,8 Mt/j, Novi Sad 2,6 Mt/j, sancties 9-10-2025, MOL-bericht 21-10-2026. https://en.wikipedia.org/wiki/Naftna_Industrija_Srbije
[3] N1, 29-8-2026, "OFAC extends JANAF licence for oil transport to NIS until September 30". https://n1info.rs/english/news/ofac-extends-janaf-licence-for-oil-transport-to-nis-until-september-30/
[4] Hydrocarbon Processing, 2-1-2026, "Serbia's NIS gets US approval to resume production in its refinery" (36 dagen stil, licentie tot 23-1-2026). https://hydrocarbonprocessing.com/news/2026/01/serbias-nis-gets-us-approval-to-resume-production-in-its-refinery/
[5] N1, 1-10-2025, "Croatian JANAF says it secured license to continue shipping oil for Serbia's NIS" — Pančevo 4,8 Mt/j, alle ruwe olie via JANAF, contract tot eind 2026. https://n1info.rs/english/news/croatian-janaf-says-it-secured-license-to-continue-shipping-oil-for-serbias-nis/
[6] `v2/design/routebrieven/olie-omisalj-szazhalombatta.md` — ankers Omišalj en Sisak, planlengte 176 km, b2-kopie (ways en bak-functie).
[7] OpenStreetMap (ODbL) via OSM-API api.openstreetmap.org/api/0.6, 2026-10-31: ways 847788794, 1165593222, 879643929, 1057915310, 1055540678, 1165598505, 1165601440, 1055818470 (substance=oil, Jadranski naftovod) en bbox-controle Pančevo (geen oliebuis). https://www.openstreetmap.org
[8] OSM way 68321105 "NIS Rafinerija nafte Pancevo" (industrial=refinery, operator Naftna Industrija Srbije). https://www.openstreetmap.org/way/68321105
[9] Esri World Imagery via `v2/tools/sat_check.py` (z14/z15): `v2/build-cache/satcheck/sat-olie-omisalj-pancevo-{pancevo-raffinaderij,pancevo-z15,osm-einde,novisad}.png`.
[10] Wikipedia, "Jadranski naftovod" — ~759 km, ontwerp 34 Mt/j, terminals Omišalj/Sisak/Virje/Slavonski Brod. https://en.wikipedia.org/wiki/Jadranski_naftovod
[11] BTA, 9-1-2026, "Serbia's NIS contracts import of first oil quantities for 2026" (eerste JANAF-lading, raffinaderij herstart). https://www.bta.bg/en/news/1040749-serbia-s-nis-contracts-import-of-first-oil-quantities-for-2026

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)
**Bestand:** `v2/data/stroomroute-olie-omisalj-pancevo.json` (37,1 KB, versie 2, punt_formaat lonlat). **Recept:** `bak_olie_omisalj_pancevo()` in `v2/tools/bak_stromen.sh`; geometrie uit `python v2/tools/maak_leidingbeen_olie_omisalj_pancevo.py --schrijf` (a1/a2 in `v2/build-cache/ais/graaf/`). Geen profiel, geen wegscan, geen zee- of luchtbeen, geen haven-aanloop.

| # | modaliteit | been | km gebakken | brief | stijl |
|---|---|---|---|---|---|
| b1 | leiding | last mile Omišalj-terminal → begin Omišalj–Sisak | 1,9 | 1,9 hemelsbreed | stippel |
| b2 | leiding | Jadranski naftovod Omišalj–Sisak (OSM, kopie van olie-omisalj-szazhalombatta) | 177,1 | 177,1 OSM / 176 planlengte | doorgetrokken |
| b3 | leiding | JANAF-oosttak Sisak–Slavonski Brod–Sotin–Novi Sad (OSM) | 367,1 | 367,1 OSM (geen gepubliceerde lengte) | doorgetrokken |
| b4 | leiding | OSM-leiding eindigt → NIS Pančevo | 22,5 | 22,5 hemelsbreed | stippel |

Totaal 568,6 km (1.847 punten, 4 markers); stippel 24,4 km (4,3%). Naden: b1→b2 0 m, b2→b3 18 m (Sisak), b3→b4 0 m; de interne naden in b3 (0,28 km Slavonski Brod, 1,19 km NIS Novi Sad) zijn gestikt. Markers: `ol-omisalj-terminal` 0 m, `ol-sisak-hub` 3 m, `ol-nis-novisad` 0,32 km, `ol-nis-pancevo` 0 m van de lijn (alle ≤ 0,5 km).

**Toetsen:** `toets_knikken`: 17 knikken ≥ 60° (3 in b2, 14 in b3), 0 omkeringen, 0 terugloop; ze zijn OSM-vorm (pompstations, Brod, Sotin, Novi Sad) en niet gerepareerd. `toets_rechte_benen --min-km 5`: alleen b4 (22,5 km, bedoelde stippel). Km-toets b3 is een indicatie (geen gepubliceerde lengte); b2 +0,6% tegen 176 km planlengte.

**Toelichting stippels:** b1 is terminal-intern (OSM-manifold niet doorlopend, letterlijke kopie van b1 van olie-omisalj-szazhalombatta). b4: de OSM-leiding stopt bij 45,0054/20,5401 in open akker, 22,5 km voor de raffinaderij; het werkelijke tracé is niet gevonden en niet verzonnen. Geen aanloop, vlucht of weg.

**Lessen:** (1) de leiding-tussenuitvoer (a1/a2 uit de OSM-API-cache) bestond al uit het maakscript; bakken was één functie en één run (15 s). (2) Een parallelle edit van bak_stromen.sh tijdens de run gaf aan het eind van de run een regel "nty,: command not found" uit een andermans halve functie, zonder gevolg voor deze bak (json geschreven). (3) Eindpunt = id (Pančevo), maar het laatste stuk is stippel omdat OSM de buis daar niet kent.
