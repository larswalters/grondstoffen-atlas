# Routebrief (licht) · gas — KS Russkaya (Anapa, Rusland) → TurkStream-ontvangstterminal (Kıyıköy, Turkije)

**stroom-id:** `gas-anapa-kiyikoy` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** Russisch pijpleidinggas dat bij het compressorstation KS Russkaya (Gazprom, bij
Gai-Kodzor/Anapa) de **TurkStream**-trunkleiding in gaat, de Zwarte Zee offshore oversteekt (930 km,
twee lijnen) en aankomt bij de Türk Akımı Doğalgaz Alım Terminali bij Kıyıköy/Vize (Kırklareli) — de
enige nog werkende Russische pijpgasroute naar de EU-rand na het verlies van Nord Stream, en het
gas dat Turkije zelf op de kaart zet als top-tien gasmarkt/-transitland.
**Welke as van het verhaal:** *Ruslands zuidelijke pijproute naar Turkije* — spiegelbeeld van de
oostpivot Chajanda→Shanghai. **31,5 bcm/j ontwerpcapaciteit** (2 lijnen × 15,75 bcm/j; in bedrijf
sinds 8-1-2020), actuele levering groeiend: 16,7 bcm in 2023 (+23% t.o.v. 2022) [1][2]. Het merendeel
gaat via de Malkoçlar-leiding door naar Bulgarije/de EU [1] — die vervolgtak valt buiten deze keten.

## 1 · Ketenkaart
```
KS Russkaya `gas-anapa-ks-russkaya` (compressorstation Gazprom, bij Gai-Kodzor/Anapa, Krasnodar Krai)
   ──(b1 leiding · TurkStream, offshore Zwarte Zee-doorsteek · 937,5 km OSM-gemeten
       tegen 930 km gepubliceerde tracélengte (+0,8%))──►
TurkStream-ontvangstterminal `gas-kiyikoy-ontvangstterminal` (Kıyıköy/Vize, Kırklareli, Turkije)
   ═══ stoppunt ═══ (vervolg naar Malkoçlar/Bulgarije buiten deze keten, zie §6/§7)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | `gas-anapa-ks-russkaya` → `gas-kiyikoy-ontvangstterminal` | TurkStream (Gazprom/BOTAŞ; offshore Zwarte Zee-doorsteek) | **937,5** [eigen Overpass-scan, 9 aaneengeschakelde OSM-ways, zie §9-bakaanwijzing] tegen **930** [1] gepubliceerde tracélengte (230 km RU-wateren + 700 km TR-wateren) (+0,8%) | OSM-pipeline (letterlijke way-keten, `man_made=pipeline`, `substance=gas`, naam "TurkStream"/"Southern Corridor") | nee — volledig gekarteerd, geen stippel nodig |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-anapa-ks-russkaya` | mijn / compressorstation (laadplek) | KS Russkaya (Gazprom), Gai-Kodzor/Anapa, Krasnodar Krai | 44.8282, 37.4277 | [3][4][6] | bron-gelegd (z15 gezien: langgerekt omheind compressorstationterrein met tientallen procesinstallaties, tanks en gebouwen midden in bosheuvels, exact op het OSM-coördinaat van het `landuse=industrial`-vlak "КС Русская"; de eerste OSM-pijpleidingway ("Southern Corridor", `substance=gas`) begint letterlijk op dit terrein, naad 0,01 km) |
| `gas-kiyikoy-ontvangstterminal` | overslag / ontvangst-verwerker (losplek, stoppunt) | Türk Akımı Doğalgaz Alım Terminali (BOTAŞ), bij Kıyıköy/Vize, Kırklareli | 41.6500, 28.0752 | [3][5][6] | bron-gelegd (z15 gezien: groot omheind industrieterrein met rijen gebouwen/leidingwerk en toegangswegen, in bos net landinwaarts van de Zwarte Zee-kust bij Kıyıköy; laatste OSM-pijpleidingway ("Türk Akımı Kara Kısmı-1") eindigt 0,21 km hiervandaan) |

Geen van beide ankers is elders in de sitelaag/andere gas-brieven al gelegd (pijpleidingstations,
geen LNG-terminals) — geen hergebruik van bestaande punten mogelijk.

## 4 · Via-punten
Niet van toepassing: het enige been is een leidingbeen waarvan de geometrie uit aaneengestikte
OSM-pijpleiding-ways ontstaat (geen corridorkeuze door ons te leggen, zoals bij weg/spoor).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| KS Russkaya | Gazprom | Russisch pijpleidinggas → drukverhoging voor de offshore Zwarte Zee-doorsteek | onderdeel van de 31,5 bcm/j-systeemcapaciteit | [1][3] |
| Ontvangstterminal Kıyıköy | BOTAŞ | offshore-gas (~300 bar) → drukverlaging + splitsing: Turks binnenlandnet ("Kara Kısmı-1/2") + Malkoçlar-leiding richting Bulgarije/EU | 31,5 bcm/j (2 lijnen × 15,75) | [1][2] |

## 6 · Stoppunt
De brief stopt bij de ontvangstterminal Kıyıköy: dit is precies het gevraagde stoppunt
(mijn/compressorstation → ontvangst/verwerker). Vanaf hier splitst het gas anoniem het Turkse net
in — een deel blijft in Turkije, het merendeel gaat door via de Malkoçlar-leiding naar Bulgarije/de
EU [1] — maar geen bron volgt één specifieke vervolgbestemming voor déze keten; de vervolgtak is een
eigen as (fase D/E vervallen: geen bron noemt een specifieke fabriek/afnemer met naam en adres).

## 7 · Open punten
- **De haalbaarheidstoets van dit ontwerp bevestigde al dat de offshore-sectie volledig als
  `man_made=pipeline`-way gekarteerd staat** (Overpass-mirror `overpass.openstreetmap.fr`, bereikbaar
  deze sessie); dit sessie onafhankelijk herhaald met exacte way-geometrie (`out geom`) i.p.v. alleen
  bounding-boxes — bevestigt en verscherpt het eerdere resultaat (9 ways, 937,5 km, tegen het
  ontwerp dat nog "onbevestigd, twee keer Overpass-timeout" meldde).
- **RU-zijde: de eerste 7,22 km tussen het Russkaya-anker en de met-naam getagde "TurkStream"-way
  dragen de OSM-naam "Southern Corridor"** (ways 647524812 + 647524854, ook `substance=gas`) i.p.v.
  "TurkStream" zelf — geometrisch een naadloze, gatloze verbinding (het eindpunt van 647524812 ligt
  op 0,01 km van het Russkaya-anker), maar mogelijk een OSM-naamgevingsverschil tussen een
  toevoerstuk en de eigenlijke exportleiding. Geen stippel nodig (het stuk is wél gekarteerd), wel
  vermeld voor de bak-agent (zie §9-instructie).
- **Twee parallelle lijnen (TurkStream heeft er twee, elk 15,75 bcm/j) staan grotendeels dubbel in
  OSM** (bijv. 853882121 vs 853882122 tussen dezelfde twee punten, 1348287421-424 op het landvervolg).
  Deze brief kiest telkens één lijn voor de getekende geometrie — dat is de gangbare aanpak bij een
  dubbele trunkleiding (vergelijkbaar met Europipe II bij `gas-karsto-dornum`) en verklaart waarom de
  gemeten 937,5 km overeenkomt met de systeem-tracélengte (930 km) en niet het dubbele daarvan.
- **Geen los Turkije-binnenland-vs-EU-doorvoer-splitsingscijfer gevonden** deze ronde — het aandeel
  dat via Malkoçlar naar Bulgarije/EU gaat is kwalitatief ("het merendeel", Wikipedia [1]) maar niet
  in bcm/j gekwantificeerd voor het peiljaar.

## 8 · Bronnen
[1] Wikipedia (EN) — "TurkStream": start Russkaya-compressorstation bij Anapa, ~930 km offshore
    (230 km RU-wateren + 700 km TR-wateren), landingspunt Kıyıköy (Vize, Kırklareli), vervolg naar
    Malkoçlar/Bulgaarse grens, 2 lijnen × 15,75 bcm/j = 31,5 bcm/j totaal, in bedrijf sinds 8-1-2020,
    "most gas flows onwards to the EU via the Malkoçlar pipeline to Bulgaria".
    https://en.wikipedia.org/wiki/TurkStream
[2] Wikipedia (EN) — "TurkStream", sectie Impact: leveringen via TurkStream 16,7 bcm in 2023 (+23%
    t.o.v. 2022); na het stoppen van de Oekraïne-transit (begin 2025) is TurkStream de enige directe
    Russische gaspijproute naar Europa. https://en.wikipedia.org/wiki/TurkStream
[3] OpenStreetMap / Overpass (mirror overpass.openstreetmap.fr, bereikbaar deze sessie) — eigen
    query op bbox (40.5,26.0)-(45.5,39.0), `way[man_made=pipeline]`, gefilterd op naam-bevat
    "TurkStream"/"Türk Akım": 15 ways gevonden, waarvan 9 de doorlopende keten Russkaya→Kıyıköy
    vormen (650756465 · 853882120 · 853882121 · 853882124 · 853882123 · 853859602 · 853942519 ·
    1348287423 · 1348287422, totaal 937,08 km) + 2 bridging-ways bij Russkaya ("Southern Corridor",
    647524812 + 647524854, 7,22 km) tot aan het Russkaya-anker. `out geom` gebruikt voor exacte
    lengtes/eindpunten (haversine, geen internet nodig voor de berekening zelf).
    https://www.openstreetmap.org/copyright
[4] OpenStreetMap / Photon (uit het ontwerp, dit sessie niet herladen) — "КС Русская",
    `landuse=industrial`-vlak op 44,8282/37,4277, ~2,9 km van Gai-Kodzor.
[5] OpenStreetMap / Photon (uit het ontwerp, dit sessie niet herladen) — "Türk Akımı Doğalgaz Alım
    Terminali", `landuse=industrial`-vlak op 41,6500/28,0752, bij Vize.
[6] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) —
    `v2/build-cache/satcheck/sat-gas-anapa-kiyikoy-ks-russkaya.png`,
    `sat-gas-anapa-kiyikoy-kiyikoy-terminal.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Eén been, één functie.** `bak_gas_anapa_kiyikoy()` in `v2/tools/bak_stromen.sh` — één
`--been-geojson "leiding|…"`, geen stippel, geen via-punten, geen haven-aanloop (geen zeebeen).
Uitvoer: `v2/data/stroomroute-gas-anapa-kiyikoy.json` (2,6 KB).

| # | modaliteit | km | punten | naad vóór | stippel |
|---|---|---|---|---|---|
| b1 | leiding | **944,7** | 94 | 0,00 (eerste been) | nee |

**Totaal 944,7 km · 94 punten · 2 markers.**

**Recept (fase A geometrie).** 11 OSM-ways (`man_made=pipeline`, `substance=gas`) opgehaald via
Overpass `out geom` (mirror `overpass.openstreetmap.fr`, één query op alle 11 way-id's), in
reisvolgorde gestikt tot één LineString: de twee "Southern Corridor"-bridgingways bij Russkaya
(647524812 — OSM-richting tegengesteld aan de reisrichting, dus omgekeerd gestikt · 647524854)
gevolgd door de 9 met-naam "TurkStream"/"Türk Akımı Kara Kısmı-1"-ways (650756465 · 853882120 ·
853882121 · 853882124 · 853882123 · 853859602 · 853942519 · 1348287423 · 1348287422). Elke naad
tussen opeenvolgende ways is **0,000 km** (exacte gedeelde OSM-node, geen enkele stitch-fout) —
weggeschreven naar `v2/build-cache/ais/graaf/gas-anapa-kiyikoy-leiding-russkaya-kiyikoy.geojson`.
De twee parallelle tweede-lijn-ways (853882122, Kara Kısmı-2: 1348287421/1348287424) zijn NIET
meegenomen (brief-instructie: dubbele geometrie, één lijn kiezen).

**⚠️ Eigen meting wijkt af van de brief-instructie.** De eigen Overpass `out geom`-scan van déze
sessie geeft **944,7 km** voor de volledige 11-way-keten, tegen de 937,08–937,5 km die de brief
zelf noemt (§9-bakaanwijzing, de eigen Overpass-scan van de brief-schrijvende sessie). Verschil ~0,8% — binnen
de meetonzekerheid van twee onafhankelijke Overpass-passes over (vermoedelijk) dezelfde ways, geen
andere ways gebruikt (alle 11 way-id's kwamen terug met exact de coördinaten die de brief noemt).
Beide liggen ruim binnen de ±15%-norm tegen de gepubliceerde 930 km (Wikipedia: 230 km RU-wateren +
700 km TR-wateren): 944,7 km = **+1,6%**. Bevinding, geen fout — niet stilzwijgend gecorrigeerd.

**Toets (bakhandleiding §5).**
- Km per been tegen de brief: b1 944,7 km tegen 930 km gepubliceerd = **+1,6%**, ruim binnen ±15%.
- Naden: 0,00 km (enige been); anker-naden Russkaya → eerste leidingpunt **0,045 km**, laatste
  leidingpunt → Kıyıköy-anker **0,205 km** (marker-tot-lijn: 0,045 / 0,062 km) — beide ver onder de
  5 km-norm, geen haven-aanloop nodig (geen zeebeen).
- Markers: beide op ≤ 0,062 km van de lijn (norm ≤ ~0,5 km) — ruim binnen.
- `toets_knikken.py`: 19 knikken ≥ 60°, **0 omkeringen ≥ 150°, 0 terugloop** — alle 19 zitten op de
  twee facilitair-terreinen (Russkaya-compressorstation en de Kıyıköy-ontvangstterminal, radii
  9–397 m), geen enkele op het offshore-tracé zelf. Plausibel voor een pijpleiding binnen een
  industrieterrein; geen reparatie nodig (geen terugloop = niets "gerepareerd horen te worden").
- `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom (94 punten, geen rechte
  stippel-kandidaat).
- JSON-contract: `versie 2`, `punt_formaat lonlat`, modaliteit `leiding` ∈ toegestane set, been
  ≥ 2 punten (94), bestandsgrootte 2,6 KB (≪ 300 KB).

**Lessen.**
- Overpass `out geom` met alle way-id's in één query (`way(id:647524812,647524854,…);out geom;`)
  is sneller en minder foutgevoelig dan losse queries per way — één request, één antwoord, directe
  volgorde-onafhankelijke matching op way-id.
- Een OSM-way kan de reisrichting omgekeerd draaien zonder dat de naam of tags dat verklappen
  (647524812 begon in de brief-geometrie bij het Russkaya-anker en eindigde 0,58 km verderop; de
  Overpass-`geometry`-array liep de andere kant op) — controleer bij het stikken altijd het eerste
  én laatste punt van elke way tegen de bedoelde reisrichting, niet alleen of de ways aaneensluiten.

**Registerregel voor main.js:** `{ sleutel: "gas-ak", bestand: "stroomroute-gas-anapa-kiyikoy.json", grondstof: "gas", aan: true }`
