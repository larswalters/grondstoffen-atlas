# Routebrief (licht) · koper — Bingham Canyon → Garfield (Verenigde Staten)

**stroom-id:** `koper-binghamcanyon-garfield` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 4) ·
**status:** gebakken (2026-09-28, lichte werkwijze, M31 golf 4)
**Keten in één zin:** koperconcentraat gaat van de put van Bingham Canyon Mine (Rio Tinto/Kennecott) via de
Copperton-concentrator per transportband en een 17-mijl (~27 km) slurry-pijpleiding rechtstreeks naar de eigen
smelter + raffinaderij in Garfield/Magna — één volledig geïntegreerde, binnenlandse mijn-tot-kathode-lus zonder
enige zeeschakel.
**Welke as van het verhaal:** het VS-contrastpunt tegenover de intercontinentale Andes- en Afrika-assen. Bingham
Canyon + Garfield leveren samen **~1 % van de wereldkopervoorziening** [1]; Kennecott mined copper **125,1 kt**
in 2025 [6]; de Garfield-raffinaderij heeft een capaciteit van **335 kt/j** (smelter ~300 kt/j) [1].

## 1 · Ketenkaart
Bingham Canyon Mine ──(b1 leiding+band, stippel · ~27 km)──► Garfield-smelter/raffinaderij ⏹ stoppunt (kathode)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding (slurry-pijpleiding vanaf de Copperton-concentrator; mijn→Copperton per transportband) | `cu-bingham-mijn` → `cu-garfield-smelter` | eigen Kennecott-infrastructuur, geen publieke weg/spoor | hemelsbreed ~23 km, geen wegkm; gepubliceerd 17 mijl (~27 km) voor het leidingdeel Copperton→Garfield [2][3] | stippel (geen doorlopend publiek net) | ja — particuliere mijninfrastructuur, geen publiek gekarteerde doorlopende lijn |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-bingham-mijn` | mijn / laadplek | Bingham Canyon Mine (Rio Tinto/Kennecott Utah Copper) | 40.5230, -112.1510 | [4], hergebruikt van `koper-sitelaag.json` (`w-bingham-canyon`) | bron-gelegd (z14 gezien: rand-tot-rand van de grootste open kopermijn ter wereld, duidelijke terraslagen rond het middelpunt) |
| `cu-garfield-smelter` | smelter + raffinaderij | Kennecott Garfield-smelter/raffinaderij (Magna, UT) | 40.7231, -112.2000 | [1][5], hergebruikt van `koper-sitelaag.json` (`w-kennecott-smelter`) | bron-gelegd (z14 gezien: industriecomplex met schoorsteen/tankpark aan de zuidoever van het Great Salt Lake, direct naast de I-80-knoop) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
*(geen — één stippelbeen zonder corridorkeuze op eigen terrein)*

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Garfield-smelter + raffinaderij | Rio Tinto / Kennecott Utah Copper LLC | concentraat → kathode | smelter ~300 kt/j · raffinaderij 335 kt/j | [1] |

## 6 · Stoppunt
De keten stopt bij de kathode uit de Garfield-raffinaderij: het ontwerp bedoelt deze as uitdrukkelijk als een
gesloten mijn-tot-raffinaderij-lus (contrastpunt), en geen bron noemt een specifieke afnemersfabriek voor deze
kathode — fase D vervalt.

## 7 · Open punten
- Exacte lengte/tracé van het transportbandtraject mijn → Copperton-concentrator niet gevonden (alleen "conveyor
  belts and pipelines" genoemd [2], geen kilometeropgave); Copperton zelf is geen apart anker (geen eigen bron
  met coördinaat, en de sitelaag behandelt de keten al als één geïntegreerde mijn→smelter-flow).
- OSM draagt bij Garfield/Magna wél losse `man_made=pipeline`-fragmenten (bv. way 33408010, 33408137, 33412223 —
  laag 1, geen `substance`-tag), maar geen bevestigde doorlopende lijn van mijn tot smelter → daarom stippel i.p.v.
  een gestikte `leiding`-geometrie; extract `us-utah` staat wel klaar mocht een latere agent dit alsnog proberen.
- Geen downstream-afnemer voor de kathode gevonden — bewust, zie §6.

## 8 · Bronnen
[1] Wikipedia, "Kennecott Utah Copper" (en.wikipedia.org/wiki/Kennecott_Utah_Copper) — mijn+smelter 1% wereldkoper,
    raffinaderij 335 kt/j, smelter ~300 kt/j, mijn 24 km ZW van Salt Lake City
[2] Wikipedia, "Bingham Canyon Mine" (en.wikipedia.org/wiki/Bingham_Canyon_Mine) — "the open-pit owners replaced
    an antiquated 1000-car railroad with conveyor belts and pipelines for transporting the ore and waste"
[3] Wikipedia, "Copperton Low Line" (en.wikipedia.org/wiki/Copperton_Low_Line) — spoorlijn Bingham→Garfield is
    "replaced by a system of conveyors and a 17-mile-long slurry pipeline"; huidig spoor alleen nog lokaal bij de
    smelter
[4] Wikipedia-geohack "Bingham Canyon Mine" (coördinaat mijn-middelpunt)
[5] OSM `landuse=industrial` "Kennecott Smelter" (Photon-zoekopdracht, geverifieerd op satelliet)
[6] `v2/design/koper-sitelaag.json`, site `w-bingham-canyon` — Rio Tinto Q4 2025-productiecijfer (125,1 kt mined
    copper 2025, 123,4 kt 2024) en site `w-kennecott-smelter` (bron-brief voor beide hergebruikte ankers)
[7] osmium-scan `v2/build-cache/geofabrik/us-utah-latest.osm.pbf` (bbox 40.60–40.80 N / -112.30…-112.05 O): 80
    `man_made=pipeline`/`goods_conveyor`-ways gevonden, geconcentreerd rond Garfield/Magna (40.71–40.76 N),
    geen tag die het slurry-tracé mijn→smelter eenduidig als één doorlopende lijn identificeert

## 9 · Bak-noot (gebakken 2026-09-28, lichte werkwijze, M31 golf 4)

**Recept:** `v2/tools/bak_stromen.sh` → `bak_koper_binghamcanyon_garfield()` — één `--stippel`-been,
geen wegscan/spoorrun/haven-aanloop nodig (privéterrein, geen zee). Draaien: `bash v2/tools/bak_stromen.sh
koper-binghamcanyon-garfield`.

**Benen:**

| # | modaliteit | km | punten | stippel | omschrijving |
|---|---|---|---|---|---|
| b1 | leiding | 22,6 | 2 | ja | Kennecott slurry-pijpleiding + transportband Bingham Canyon Mine → Copperton-concentrator → Garfield-smelter (schematisch — particuliere mijninfrastructuur, geen doorlopend publiek net) |

**Totaal:** 22,6 km · 2 punten · 2 markers (`cu-bingham-mijn`, `cu-garfield-smelter`).

**Toelichting op de stippel:** b1 is bewust een rechte hemelsbrede lijn tussen de twee ankers — geen
OSM-way, geen operator-geopubliceerde tracégeometrie voor de transportband mijn→Copperton, en de
gevonden `man_made=pipeline`-fragmenten bij Garfield/Magna (osmium-scan `us-utah`, 80 ways, laag 1,
geen `substance`-tag) vormen geen bevestigde doorlopende lijn mijn→smelter. Stippel = "hier reikt het
net niet", niet "aannemelijk" — dat laatste staat al in de beennaam/brief (§7) waar van toepassing.

**Km-toets:** de brief geeft zelf geen echte wegkm voor dit been (§2: "hemelsbreed ~23 km, geen
wegkm"); de gebakken hemelsbrede lengte is **22,6 km**, wat de brief-schatting bevestigt. Het
gepubliceerde 17-mijl (~27 km) cijfer [3] geldt uitsluitend het leidingdeel Copperton→Garfield (dus een
deelstrekking van dit ene been, niet de hele mijn→smelter-afstand) en is geen doel voor de ±15%-toets
op déze hemelsbrede lijn.

**Toets (handleiding §5):**
- `toets_knikken.py`: 0 knikken ≥ 60°, 0 omkeringen — verwacht bij een 2-punts rechte stippel.
- `toets_rechte_benen.py --min-km 5`: been 1 heeft omwegfactor 0,999 (🟡 MIDDEL) — dit ÍS een stippel
  met reden, dus geen bevinding; precies het patroon dat de toets verwacht bij een gestippeld been.
- Naad: geen (eerste en enige been).
- Markers: beide ankers liggen op de lijn zelf (0,0 m) — ze zijn de lijn-eindpunten.
- JSON: `versie 2`, `punt_formaat lonlat`, modaliteit `leiding` (geldig), 2 punten, 0,87 KB.

**Lessen/open punten:** zie routebrief §7 (transportbandtraject mijn→Copperton niet gevonden, geen
Copperton-anker, OSM-pijplijnfragmenten stitchen niet door, geen downstream-afnemer). Geen nieuwe
lessen uit het bakken zelf — de brief had de stippelkeuze al goed voorbereid.
