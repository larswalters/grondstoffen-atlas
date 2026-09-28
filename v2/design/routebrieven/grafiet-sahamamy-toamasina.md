# Routebrief (licht) · Grafiet · Van → Via → Naar (land)

**stroom-id:** `grafiet-sahamamy-toamasina` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** concept, ⚠️ NIET GEBAKKEN (golf 6): het mijnanker Sahamamy is niet op site-niveau te leggen (alleen commune/district); de brief blijft als onderzoeksnotitie
**Keten in één zin:** vlokgrafiet van de Sahamamy-mijn (Tirupati Graphite, sinds 2025/2026 handelend als Total
Graphite; regio Brickaville/Atsinanana, Oostkust) gaat over de RN2-corridor naar de Toamasina-haven — een
generieke-markt-stoppunt zoals `grafiet-itapecerica-vitoria`, met als extra complicatie dat het mijn-siteanker
dit onderzoeksbudget niet op site-niveau bevestigd kon worden.
**Welke as van het verhaal:** tweede Madagaskar-grafietas naast `grafiet-molo-duisburg` (Zuid-Madagaskar,
NextSource) — deze keten ligt aan de **Oostkust**, dicht bij Toamasina zelf. Sahamamy (sinds 2019) + het
naburige Vatomina samen "fully permitted & currently operational", 36 kt/j nameplate gepland (totalgraphite.com,
2025-2026) [1]; onafhankelijke bron zegt Sahamamy zelf ligt sinds april 2024 op **care and maintenance**
(Major Mines & Projects) [7] — een tegenstrijdigheid die in §7 blijft staan.

## 1 · Ketenkaart
```
Sahamamy-mijn `gr-sahamamy-mijn` (regio Fetraomby, Brickaville-district — ANKER NIET BEVESTIGD)
  ┄┄(b1 truck · RN2 via Brickaville · hemelsbreed ~72 km regio→kade, geen wegkm ·
  NOG NIET BAKBAAR — geen siteanker)┄┄►
  Toamasina-haven `gr-toamasina-kade` (hergebruikt anker, letterlijk `co-toamasina-kade`) ⏹ STOPPUNT
  (geen met naam genoemde buitenlandse afnemer — generieke markt Europa/NA/Azië)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-sahamamy-mijn` → `gr-toamasina-kade` | RN2 (Toamasina ↔ Brickaville-corridor) [8] | hemelsbreed ~72 km (Fetraomby-commune-referentie → kade), geen wegkm — **NIET gebakken deze ronde: geen site-anker** | `maak_stroombeen_weg.py` (extract `madagaskar`) — pas zodra het siteanker gelegd is | n.v.t. (geen geometrie getekend) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-sahamamy-mijn` | mijn (kop) | Sahamamy Graphite Mine, Fetraomby, Brickaville-district, Atsinanana — Tirupati Graphite / Total Graphite | **geen anker** (regio-referentie -18,5833 / 48,9167 = Wikipedia-infobox-coördinaat van de commune Fetraomby, GEEN site) | [2][3][4][5][6] | **onzeker — géén anker.** Nominatim/Wikipedia lokaliseren de mijn tot op commune-niveau (Fetraomby, Brickaville-district — mindat.org: "linker oever Ranofotsy-rivier, 10 km N van Gisimay" [6]); een satellietblik op de commune-referentiecoördinaat (z13 wijd + z16 dicht, `sat-grafiet-sahamamy-toamasina-fetraomby-{wide,close}.png`) toont uitsluitend bos/landbouwmozaïek en één dorpskern ~1,3 km ZO — **geen mijnbouw-infrastructuur zichtbaar** (consistent met de care-and-maintenance-status sinds april 2024 [7]). Een marktcentroïde/dorpscoördinaat is geen anker (werkwijze §1) — dit blijft dus expliciet open, zie §7. |
| `gr-toamasina-kade` | overslag (zeekade, stoppunt) | Ambatovy Bulk Jetty Terminal / Port of Toamasina — **hergebruikt, letterlijke kopie van `co-toamasina-kade`** | -18,1556, 49,4278 | [9], `stroomroute-kobalt-ambatovy-toamasina.json` | bron-gelegd (letterlijk hergebruikt uit `kobalt-ambatovy-toamasina.md`: z15 gezien, finger pier met kranen/hijswerk en bulklading direct aan de kustlijn; ligt 0,04 km van de OSM-industrial-polygon die het ontwerp deze ronde apart via Nominatim vond — dezelfde plek, geen nieuwe polygon-anker nodig conform de haalbaarheidstoets) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | — | n.v.t. — het wegbeen is niet gebakken (geen siteanker). Verwachte corridor: lokale weg Fetraomby → RN2-aansluiting bij/nabij Brickaville → RN2 noordwaarts naar Toamasina [8]; via-punten worden pas gelegd zodra `gr-sahamamy-mijn` een site-anker heeft. | | |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Sahamamy-mijn/plant (vlotatie/wascircuit) | Tirupati Graphite plc / Total Graphite | grafieterts → vlokconcentraat | fase 1: 3.000 t/j oplopend naar 21.000 t/j (fase 2); Sahamamy+Vatomina gecombineerd 36.000 t/j nameplate genoemd, "currently operational" (2025-2026) [1][3][4] — tegenover een onafhankelijke bron die Sahamamy zelf op care-and-maintenance zet sinds april 2024 [7], zie §7 | [1][3][4][7] |

## 6 · Stoppunt
De brief stopt bij de Toamasina-kade (hergebruikt anker `gr-toamasina-kade`): geen bron noemt een met naam
genoemde buitenlandse afnemer, alleen generieke markten ("Europe, North America and Asia", "benchmark buyers")
[1][3] — exact dezelfde eerlijke-stoppunt-situatie als `grafiet-itapecerica-vitoria` en `grafiet-molo-duisburg`.
Fase B (zee) is daarom bewust niet getekend, en fase A (het wegbeen) kan sowieso nog niet gebakken worden zolang
het mijn-siteanker ontbreekt (§3/§7).

## 7 · Open punten
- **BLOKKEREND: het mijn-siteanker (`gr-sahamamy-mijn`) is niet gevonden op site-niveau.** Nominatim geeft voor
  "Sahamamy" vier gelijknamige dorpen in Madagaskar (Ambositra/Ikongo/Alaotra-Mangoro/Brickaville) en voor
  "Vatomina" 0 treffers — precies het probleem dat de haalbaarheidstoets al meldde. Wikipedia/mindat.org lokaliseren
  de mijn wél eenduidig tot **Fetraomby-commune, Brickaville-district, Atsinanana** ("Sahamamy graphite mine,
  Fetraomby… sinds 2019" [2]; mindat: "linker oever Ranofotsy-rivier, 10 km N van Gisimay" [6]) — maar dat is een
  gebiedsaanduiding, geen coördinaat. Een satellietblik op de enige beschikbare referentiecoördinaat (Wikipedia's
  eigen infobox-punt voor de commune Fetraomby, -18,5833/48,9167 — uitdrukkelijk GEEN anker, werkwijze §1) laat
  alleen bos en landbouwpercelen zien, geen mijnbouwterrein. **Vervolgstap vóór het bakken:** een bedrijfskaart/
  RNS-aankondiging van Tirupati/Total Graphite met een concrete locatie, of Overpass/OSM (deze ronde onbereikbaar,
  §werkbudget) op `landuse=quarry`/`man_made=mineshaft` rond Fetraomby — zonder dat anker geen wegbeen (geen
  coördinaat verzinnen, werkwijze §1).
- **Tegenstrijdige operationele status.** totalgraphite.com (bedrijfsbron, 2025-2026) noemt Vatomina & Sahamamy
  samen "fully permitted & currently operational" [1]; Major Mines & Projects (onafhankelijke mijnbouwdatabase)
  zegt dat Sahamamy specifiek sinds **april 2024 op care and maintenance staat** [7]. Beide bronnen zijn recent;
  niet opgelost dit onderzoeksbudget — relevant voor of dit jaarvolume nog een actuele stroom beschrijft.
- **Vatomina als alternatief/aanvullend siteanker niet onderzocht.** Vatomina ligt volgens Major Mines & Projects
  "51 km SW van Tamatave" en Sahamamy "~8 km west van Vatomina" [7] — geen van beide kon dit budget een OSM- of
  Nominatim-treffer krijgen; dezelfde blokkade als hierboven.
  Bedrijfsnaam gecheckt bij het schrijven: bron gebruikt zowel "Tirupati Graphite" (oudere persstukken) als "Total
  Graphite" (totalgraphite.com, 2025-2026 corporate) — beide namen voor dezelfde entiteit, in de brief beide genoemd.
- **Exacte wegcorridor (RN2 vs. lokale ontsluiting Fetraomby) niet bevestigd** — Brickaville ligt aan de RN2, maar
  welke lokale weg Fetraomby (10 km N van Gisimay, aan de Ranofotsy) met de RN2 verbindt is niet gevonden.
- **WEBBUDGET:** 2 van 3 WebSearch-aanroepen gebruikt (Sahamamy/Fetraomby-lokalisatie + Vatomina/Sahamamy-
  locatiedetails via miningdataonline.com); verder Wikipedia-API, Nominatim en WebFetch op totalgraphite.com,
  globalminingreview.com en miningdataonline.com. Overpass (twee mirrors) was deze ronde onbereikbaar (werkwijze-
  regel: "Overpass kan onbereikbaar zijn").

## 8 · Bronnen
[1] Total Graphite (totalgraphite.com), corporate overzicht 2025-2026 — "The Company's Madagascar Vatomina &
Sahamamy projects, spanning 33 km², are fully permitted & currently operational"; "Combined 36ktpa nameplate
production capacity planned across our Madagascar projects"; free-dig saprolitic graphite. https://totalgraphite.com/
[2] Wikipedia (EN), "Fetraomby" — "village and rural commune in the Brickaville district… The Sahamamy graphite
mine has operated there since 2019." https://en.wikipedia.org/wiki/Fetraomby
[3] Mining Digital, "Tirupati Graphite Sahamamy project to commission in June" — "8 km² mining permit area issued
for 40 years"; "located near the Toamasina port of Madagascar"; module 1 3.000 tpy, module 2 18.000 tpy (target
21.000 tpy totaal); JORC-resource ~13 Mt. https://miningdigital.com/supply-chain-and-operations/tirupati-graphite-sahamamy-project-to-commission-in-june
[4] Global Mining Review, "Tirupati Graphite plc commences first flake graphite production at newly constructed
Madagascar plant", 2019-03-28. https://www.globalminingreview.com/exploration-development/28032019/tirupati-graphite-plc-commences-first-flake-graphite-production-at-newly-constructed-madagascar-plant/
[5] Mining Review, "Tirupati Graphite's Vatomina mine in Madagascar opens". https://www.miningreview.com/battery-metals/tirupati-graphites-vatomina-mine-in-madagascar-opens/
[6] Mindat.org — "Sahamamy graphite mine, Fetraomby, Brickaville District, Atsinanana, Madagascar": locatie op de
linkeroever van de Ranofotsy-rivier, 10 km N van Gisimay (via zoekresultaat-snippet; pagina zelf achter Cloudflare
niet rechtstreeks bevraagbaar). https://www.mindat.org/loc-304454.html
[7] Major Mines & Projects (miningdataonline.com), "Madagascar (Sahamamy/Vatomina) Operation" — Vatomina "51 km SW
from Tamatave"; Sahamamy "located approximately 8 km west of the Vatomina Project"; Sahamamy "placed on care and
maintenance in April 2024". https://miningdataonline.com/property/841/Madagascar-Sahamamy-Vatomina-Operation.aspx
[8] Wikipedia (EN), "Vohibinany District"/"Brickaville" — Brickaville aan Route nationale 2 (RN2), tussen Toamasina
en Antananarivo; Fetraomby onderdeel van dit district. https://en.wikipedia.org/wiki/Vohibinany_District ·
https://en.wikipedia.org/wiki/Brickaville
[9] `v2/design/routebrieven/kobalt-ambatovy-toamasina.md` + `v2/data/stroomroute-kobalt-ambatovy-toamasina.json`
(marker `co-toamasina-kade`, -18,1556/49,4278) — hergebruikt anker, bron-gelegd (z15, Ambatovy Bulk Jetty
Terminal/Port of Toamasina).
[10] OpenStreetMap/Nominatim (ODbL), bevraagd 2026-09-28 — "Sahamamy" (4 treffers: Ambositra/Ikongo/Alaotra-
Mangoro/Brickaville-Ranomafana Est), "Vatomina" (0 treffers), "Fetraomby" (commune-relatie, -18,6636/48,9193),
"Ambalakondro" (geen treffer bij Fetraomby). https://nominatim.openstreetmap.org
[11] Wikipedia-API (EN), zoekresultaat "Mining industry of Madagascar" — noemt zowel "Sahamamy graphite mine
(graphite, in Fetraomby)" als "Marovinsty mine, near Vatomandry" als aparte, bestaande grafietmijnen.
https://en.wikipedia.org/wiki/Mining_industry_of_Madagascar
[12] Esri World Imagery via `v2/tools/sat_check.py` (z13 + z16, live) —
`v2/build-cache/satcheck/sat-grafiet-sahamamy-toamasina-fetraomby-{wide,close}.png`.

## 9 · (leeg — voor de bak-agent)
