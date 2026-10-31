# Routebrief (licht) · gas — Mellitah (Libië) → Greenstream → Gela (Italië)

**stroom-id:** `gas-mellitah-gela` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) ·
**status:** gebakken
**Keten in één zin:** Libisch gas uit Wafa en Bahr Essalam wordt in het Mellitah-complex (Mellitah Oil and Gas, NOC/Eni)
behandeld en gecomprimeerd en gaat via de Greenstream-onderzeeleiding (32 inch, tot ruim 1.100 m diep, Agip Gas BV) naar de
Eni-ontvangstterminal bij Gela op Sicilië, waar het in het Italiaanse net (Snam) wordt ingevoed.
**Welke as van het verhaal:** de enige Libië-keten van de atlas, en de enige Noord-Afrikaanse pijp die in Sicilië aanlandt —
capaciteit 8 bcm/j bij opening, later 11 bcm/j (bronnen verschillen, 9 bcm/j bij Interfax) [1][5]; werkelijke doorzet gekelderd:
ca. 2,5 bcm in 2023, 1,4 bcm in 2024, ca. 1,0–1,1 bcm in 2025 (22-jaarslaagte) [2][3]. Peiljaar 2025. De bol toont capaciteit, geen stroom.

## 1 · Ketenkaart
```
Wafa-veld (530 km van Mellitah, niet in OSM — niet getekend) + Bahr Essalam offshore [1][5]
   ──► Mellitah-complex `gas-mellitah-complex` ──(b1 leiding · Greenstream · ~502 km, OSM 2 ways)──►
Gela-terminal `gas-gela-terminal` — stoppunt, invoeding Italiaans net (Snam)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | `gas-mellitah-complex` → `gas-gela-terminal` | Greenstream (32″, Agip Gas BV / Eni) | gepubliceerd 510 [5] / 520 [4] / 540 [1]; gemeten OSM 502,1 (−1,5% t.o.v. 510; −3,4% t.o.v. 520) | OSM-ways 310845241 (onderzee, 501,0) + 310833747 (onshore Gela, 1,2); geojson vooraf gestikt (`maak_leidingbeen_gas_mellitah_gela.py`) | nee |

Way 310835025 (OSM-naam "Gela - Enna", operator Snam, 900 mm) is een Snam-binnenlandleiding en geen Greenstream: weggelaten
(het ketenontwerp telde hem ten onrechte mee). Binnen de ±15%-toets ten opzichte van elke gepubliceerde lengte (510–540).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-mellitah-complex` | gasbehandeling + compressie (kop) | Mellitah-complex (Mellitah Oil and Gas, NOC/Eni), kust West-Libië | 32.8547, 12.2395 | [1][5][6][8] | bron-gelegd (z15 gezien: groot, geplaveid procescomplex met rijen compressoren/vaten, tankenpark, lange jetty de zee in en een hoofdweg langs de zuidwestzijde; OSM-leidingstart 32.8570, 12.2439 ligt 0,48 km noordoostelijk aan de kustrand) |
| `gas-gela-terminal` | ontvangstterminal (staart, stoppunt) | Gela-terminal Greenstream (Eni), naast de Gela-raffinaderij, Sicilië | 37.0459, 14.2981 | [1][6][8] | aannemelijk (z16 gezien: omheind perceel met gebouw, parkeerplaats en groen, naast een open verhard platform, direct oostelijk van de grote raffinaderij met tankpark; punt = eindknoop van OSM-way 310833747 (Eni, underground), geen operatordocument dat dit perceel als "Greenstream receiving terminal" benoemt) |

Hergebruik: geen — Mellitah, Gela en Greenstream staan niet in `gas-sitelaag.json` en niet in eerdere brieven. De OSM-leidingeinden zelf
(Libië 32.8570, 12.2439; Gela 37.0373, 14.2932 → 37.0459, 14.2981) zijn de routeerpunten; ankers ≠ routeerpunten waar vermeld.

## 4 · Via-punten
Niet van toepassing: leidingbeen uit aaneengestikte OSM-ways, geen corridorkeuze (geen weg/spoor).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mellitah-complex | Mellitah Oil and Gas BV (50/50 NOC/Eni) | Wafa- en Bahr Essalam-gas → drooggas + compressie voor Greenstream (en Libische binnenlandse vraag) | pijpcapaciteit 8–11 bcm/j; doorzet 2025 ca. 1,0–1,1 bcm | [1][2][3][5][7] |
| Gela-terminal | Eni (Greenstream BV, Eni/NOC) | Greenstream-aanlanding → Snam Rete Gas (o.a. Gela–Enna) | aankomst 2024 1,406 bcm, 2025 0,959 bcm | [2][8] |

## 6 · Stoppunt
De brief stopt bij de Gela-ontvangstterminal: dit is het enige Italiaanse aanlandpunt van Greenstream, daarna is het gas anoniem Italiaans
netgas (Snam). Fase A (Wafa → Mellitah, 530 km) vervalt: niet als OSM-leiding gekarteerd, dus niet getekend in plaats van geraden.

## 7 · Open punten
- **Doorzet is een bandbreedte, geen meting van één bron:** 2023 ca. 2,5 bcm (Agenzia Nova), 2024 1,406 bcm, 2025 ca. 0,96 bcm aankomst in
  Gela (Agenzia Nova, via zoekresultaat; pagina zelf gaf HTTP 403) en 105 mn cfd ≈ 1,1 bcm/j (MEES, eigen omrekening) [2][3]. 1,0–1,1 bcm gebruikt als peiljaar-2025.
- **Capaciteit verschilt per bron:** 8 bcm/j bij opening, 9 bcm/j (Interfax 2011), 11 bcm/j (Wikipedia); lengte 510/520/540 km. Geen officiële Eni-bron gelezen.
- **Mellitah-anker is een complexpunt**, niet de compressorhal: bron-gelegd op satelliet (z15), maar geen operatorcoördinaat gevonden.
- **Gela-anker aannemelijk:** het gebouwperceel ligt op het OSM-leidingeinde; een document dat dit perceel de Greenstream-terminal noemt ontbreekt.
- **Offshore-geometrie is grof** (OSM, 14 punten over 502 km); de lijn is vrijwel recht, de werkelijke legging kan lokaal afwijken.
- **Onshore stukken niet getekend:** Mellitah-complex → kust (0,48 km) en Gela-aanlanding → terminal (0 km): < 5 km, dus geen stippel.
- **Wafa → Mellitah (530 km), Bahr Essalam-platform en de Libische binnenlandse afname** (ca. 2 bcm/j volgens OGJ 2004) staan niet in OSM en niet op de bol.
- **Sitelaag mist Mellitah en Gela** — centrale aanvulling nodig (gewicht: capaciteit 8–11 bcm/j, doorzet ~1 bcm).
- **Politiek risico:** Libische onrust en onderhoudsuitval (juni 2024 zes dagen stop [6]) bepalen de doorzet; de lijn toont het bestaan van de route.

## 8 · Bronnen
[1] Wikipedia (EN), "Greenstream pipeline" — 540 km, Mellitah → Gela, >1.100 m diep, 32 inch, 8 → 11 bcm/j, Agip Gas BV (Eni/NOC), start 2004.
    https://en.wikipedia.org/wiki/Greenstream_pipeline
[2] Agenzia Nova, "Libya threatens Greenstream following false reports about Eni's minimal flows" en verwante berichten — Gela-aankomst 1,406 bcm (2024), 0,959 bcm (2025), ca. 2,5 bcm (2023); via zoekresultaat, pagina 403.
    https://www.agenzianova.com/en/news/Libya-threatens-greenstream-following-false-reports-about-Eni%27s-minimal-flows-to-Italy./
[3] MEES, 16-1-2026, "Libya gas exports fall to 22-year low" — 2025: 105 mn cfd (−22%), capaciteit 8 bcm/j, zesde jaarlijkse daling.
    https://www.mees.com/2026/1/16/oil-gas/libya-gas-exports-fall-to-22-year-low/a8ef8230-f2e2-11f0-a93a-418710887809
[4] Oil & Gas Journal, "Libya to Italy gas pipeline inaugurated" — 520 km, 32 inch, max. diepte 1.127 m, Wafa tot 4 en Bahr Essalam tot 6 bcm/j.
    https://www.ogj.com/pipelines-transportation/article/17292207/libya-to-italy-gas-pipeline-inaugurated
[5] Interfax Energy, "Greenstream volumes ramp up" (3-11-2011) — 510 km, max. 9 bcm/j, Mellitah-installatie, Mellitah Oil & Gas 50/50 Eni/NOC.
    https://interfaxenergy.com/natural-gas-news-analysis/africa/greenstream-volumes-ramp-up
[6] MEES, 14-6-2024, "Libya-Italy gas collapse on Mellitah outage" — ongepland onderhoud Mellitah-complex, herstart 19 juni.
    https://www.mees.com/2024/6/14/economics-finance/libya-italy-gas-collapse-on-mellitah-outage/9fa198b0-2a43-11ef-a26f-d9f438778881
[7] Wikipedia (EN), "Greenstream pipeline" — Wafa-veld 530 km van Mellitah, Bahr Essalam, Bouri; Mellitah-compressorstation en Gela-terminal vermeld.
    https://en.wikipedia.org/wiki/Greenstream_pipeline
[8] OpenStreetMap-bijdragers (ODbL), OSM-API, 2026-10-31 — ways 310845241 (GreenStream pipeline, Agip Gas BV, underwater, 9 nodes), 310833747 (Eni, underground), 310835025 (Gela–Enna, Snam, uitgesloten); wikidata Q192380.
    https://www.openstreetmap.org/way/310845241
[9] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-gas-mellitah-gela-mellitah.png`, `-mellitah-kust.png`, `-gela.png`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Bestand:** `v2/data/stroomroute-gas-mellitah-gela.json` (1,0 KB, versie 2, lonlat) · **1 been, 502,2 km, 13 punten, 2 markers** · register `gas-mg`.
**Recept:** `bash v2/tools/bak_stromen.sh gas-mellitah-gela` (functie `bak_gas_mellitah_gela`): één `--been-geojson "leiding|…"` uit
`v2/build-cache/ais/graaf/gas-mellitah-gela-leiding-greenstream.geojson` (FeatureCollection, vooraf gestikt door `v2/tools/maak_leidingbeen_gas_mellitah_gela.py`
uit OSM-ways 310845241 + 310833747), plus twee `--marker`. Geen MARNET-route, geen wegscan, geen extract, geen via-punten.

| # | modaliteit | km | punten | stippel | naad |
|---|---|---|---|---|---|
| b1 | leiding (Greenstream, doorgetrokken) | 502,2 | 13 | nee | n.v.t. |

**Toets:** km 502,2 tegen gepubliceerd 510 / 520 / 540 = -1,5% / -3,4% / -7,0%: binnen ±15% (geen wegkm; leidinglengte, dus normwaardig). Geen naden (één been).
Markers: Mellitah 0,48 km van de lijn (anker ≠ routeerpunt, kust; < 5 km, dus geen stippel), Gela 0,00 km. `toets_knikken`: 2 knikken van ca. 83 graden, R 96-120 m, bij
37.0440,14.2987 en 37.0450,14.2973 (de OSM-aanlanding bij Gela; geen terugloop, 0 omkeringen). `json.load` goed, versie 2, punt_formaat lonlat, modaliteit leiding, 13 punten.
**Bevinding `toets_rechte_benen`:** b1 staat op 🔴 GROOT met omwegfactor 1,000 (13 punten over 502 km; het langste segment loopt van 33.0453,12.3384 naar 37.0367,14.2932, ca. 480 km).
Bewust niet bijgewerkt: de onderzeeleiding is in OSM zo grof gekarteerd en een tussenpunt zou een verzonnen coördinaat zijn. De lijn passeert Malta op ca. 55 km westelijk; de echte legging kan lokaal afwijken.
**Geen** stippel, haven-aanloop, kopie, vlucht of via-punt (zie §4/§6). Eindpunt = id (Gela).
**Lessen:** (1) een vooraf gestikte OSM-leiding is met één `--been-geojson` in 17 s gebakken, zwaar-slot nauwelijks nodig; (2) de bake-console eindigt met een `bash`-syntaxfout
op een regel in een ANDERMANS functie (gelijktijdige edit in `bak_stromen.sh`, regel ~15051 op dat moment); onze functie is ongemoeid en het json was al geschreven, later was `bash -n` weer schoon;
(3) sitelaag mist Mellitah en Gela: centraal aanvullen (anker-coördinaten in §3).
