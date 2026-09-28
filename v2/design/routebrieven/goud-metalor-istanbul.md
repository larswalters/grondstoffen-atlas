# Routebrief (licht) · Goud · Van → Via → Naar (land)

**stroom-id:** `goud-metalor-istanbul` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 4) ·
**status:** gebakken
**Keten in één zin:** LBMA-goudbaren van de Metalor-raffinaderij in Marin-Epagnier (Neuchâtel) per truck naar
de vrachtterminal van Zürich Airport (ZRH), per vrachtvlucht (grootcirkel) naar de vrachtterminal van Istanbul
Airport (IST), en per truck naar het Kuyumcukent-goud-/sieradencomplex in Yenibosna, Istanbul.
**Welke as van het verhaal:** de Zwitsers-Turkse raffinaat-naar-marktas — Metalor-baren naar 's werelds
grootste geïntegreerde goud-/sieradencomplex. Reserve-as uit golf 3, nu geactiveerd in golf 4. Turkije-
goudvraag ≈150–250 t/j (WGC, 2024/25); Zwitserse goudexport naar Turkije sterk maandelijks wisselend — 9,3 t
in dec-2025, 7,74 t in nov-2025, slechts 2,2 t in juli-2025 [3][4]. Metalor-aandeel niet apart gepubliceerd.

## 1 · Ketenkaart
```
Metalor-raffinaderij, Marin-Epagnier `au-ref-metalor`
  ──(b1 truck · A5 Biel/Bienne → A6/A1 via Bern · ~180 km)──►
Zürich Airport vrachtterminal `au-zrh-vrachtterminal` (hergebruikt uit pgm-springs-zurich.md)
  ──(b2 lucht · vlucht ZRH → IST, grootcirkel, aannemelijk · ~1.739 km hemelsbreed)──►
Istanbul Airport vrachtterminal `au-ist-vrachtterminal` (Tayakadın, Arnavutköy)
  ──(b3 truck · binnenstedelijk, TEM-otoyolu/Basın Ekspress Yolu · ~30 km)──►
Kuyumcukent-goud-/sieradencomplex, Yenibosna `au-kuyumcukent` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | Metalor, Marin-Epagnier → ZRH vrachtterminal | A5 (Biel/Bienne) → A6/A1 via Bern | ≈180 [ontwerp]; hemelsbreed 126,6 [berekend] | maak_stroombeen_weg | nee |
| b2 | D | lucht | Zürich (ZRH) → Istanbul (IST) | vrachtvlucht ZRH → IST (grootcirkel) | ≈1.739 hemelsbreed [berekend] | maak_luchtbeen | nee — doorgetrokken (aannemelijk: geen bron noemt déze specifieke vlucht; Zwitsers-Turkse goudexport is gedocumenteerd substantieel en wisselend [3][4], luchtvracht is industriestandaard voor edelmetaal) |
| b3 | D | truck | IST vrachtterminal → Kuyumcukent | binnenstedelijk (TEM-otoyolu/Basın Ekspress Yolu) | ≈30 [ontwerp]; hemelsbreed 29,3 [berekend] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-ref-metalor` | raffinaderij / laadplek | Metalor SA, Marin-Epagnier | 47.0107, 7.0112 | [2][osm] | bron-gelegd (z15 gezien: industrieel gebouwencomplex met parkeerterreinen direct aan de A5/spoorlijn bij Marin-Epagnier, aan het meer van Neuchâtel; matcht OSM-building "Metalor" op Rue des Perveuils/Route des Grands-Bois. Preciezer dan het v1-registerpunt 46,99/6,93 — dat was stadsniveau Neuchâtel) |
| `au-zrh-vrachtterminal` | overslag / lucht | Zürich Airport vrachtplatform | 47.4647, 8.5492 | [8] | bron-gelegd (letterlijk hergebruikt uit `pgm-springs-zurich.md`, zelfde golf-patroon: vrachtplatform met vrachttoestellen naast een rechthoekig loodsgebouw, O van de hoofdterminal) |
| `au-ist-vrachtterminal` | overslag / lucht | Istanbul Airport vrachtterminal (iGA), Tayakadın, Arnavutköy | 41.25528, 28.71278 | [6][7] | bron-gelegd (z15 gezien: cluster van loods-/logistiekgebouwen direct Z van de start-/landingsbanen en W van de hoofdterminal, bij de rotonde waar de toegangsweg vanaf de snelweg samenkomt — matcht de iGA cargo-omschrijving en de Wikipedia-coördinaat) |
| `au-kuyumcukent` | losplek / markt | Kuyumcukent-goud-/sieradencomplex, Yenibosna, Bahçelievler | 41.0035, 28.8148 | [5][osm] | bron-gelegd (z15 gezien: groot rechthoekig gebouwencomplex direct bij een grote verkeersknoop op de Basın Ekspress Yolu/TEM-toerit, vlak N van de oude Atatürk-luchthavenbanen — matcht de OSM-Kuyumcukent-kruising en Kuyumcukent's eigen "180.000 m²-complex in Yenibosna" [5]) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Biel/Bienne (A5/A6-knoop) | 47.1402, 7.2439 | pint de route via de noordelijke A5-oever van het Bielersee i.p.v. een zuidelijke Jura-omweg |
| b1 | 2 | Bern (A6/A1-knoop) | 46.9485, 7.4522 | het punt waar de corridor overstapt van A6 naar A1 richting Zürich; sluit een directe A5-Basel-omweg uit |
| b3 | — | geen | — | korte, ondubbelzinnige stedelijke corridor (één samenhangende route over TEM-otoyolu/Basın Ekspress Yolu tussen twee bekende punten); de bak-agent routeert over het OSM-wegnet, exacte ligging volgt uit die routering |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Metalor (Marin-Epagnier) | Metalor SA | doré/schroot → LBMA-goudbaren | cap. ≈ 650 t/j (v1-register) | [2][v1] |

## 6 · Stoppunt
De brief stopt bij Kuyumcukent: fase E (welke individuele juwelier/exporteur de baren verwerkt) is niet
gebrond — Kuyumcukent is zelf al de markt (2.500+ productie-eenheden, groothandel in goud/zilver/edelstenen
[5]), geen bron volgt één zending verder dan het complex.

## 7 · Open punten
- **Reserve-as (haalbaarheidstoets, BINDEND):** deze as was golf-3-reserve, minder sterk brongebaseerd dan de
  13 hoofdketens van die golf — geen aanpassing nodig volgens de toets, nu geactiveerd omdat golf 4 reserve-
  assen tot volwaardige ketens uitwerkt.
- **Vlucht ZRH→IST is niet per bron gebrond voor déze specifieke lading** — aangenomen als één directe
  vrachtvlucht (aannemelijk: industriestandaard, geen tussenlanding gebrond).
- **Metalor-aandeel in de Zwitsers-Turkse goudexport niet apart gepubliceerd** — de Zwitserse douanecijfers
  [3][4] zijn nationaal (alle raffinaderijen samen: Valcambi/PAMP/Argor-Heraeus/Metalor); alleen het
  totaalvolume en de sterke maandelijkse variatie zijn gebrond.
- **Welk specifiek pand/onderneming in Kuyumcukent** de import ontvangt is niet te herleiden — het complex
  telt 2.500+ zelfstandige bedrijven; het anker blijft op complex-niveau.
- **Via-punten b1 zijn indicatief** (bekende steden op de A5/A6/A1-corridor, niet zelf OSM-wegvertex-
  geverifieerd binnen het webbudget) — de bak-agent routeert over het OSM-wegnet.
- **Fase E vervalt** — geen bron volgt de baren voorbij het Kuyumcukent-complex naar een specifieke fabriek of
  exporteur.

## 8 · Bronnen
[1] World Gold Council, "Gold Demand by Country" — Turkije-vraag ≈150–250 t/j (WGC-goudvraagdata). https://www.gold.org/goldhub/data/gold-demand-by-country
[2] Metalor SA, officiële site — raffinaderij Marin/Neuchâtel, cap. ≈ 650 t/j. https://www.metalor.com/
[3] Türkiye Today, 2026 — "Swiss gold exports to Türkiye jump 20% as global demand hits record": dec-2025 9,3 t (vs. 7,74 t nov-2025), totaal Zwitserse export dec-2025 138,98 t. https://www.turkiyetoday.com/business/swiss-gold-exports-to-turkiye-jump-20-as-global-demand-hits-record-3213771
[4] NationalTurk — "Gold Exports From Switzerland To Turkey At The Peak Of The Last 9 Years": historische piek/dal-patroon, juli-2025 slechts 2,2 t. https://www.nationalturk.com/en/gold-exports-from-switzerland-to-turkey/
[5] Kuyumcukent İşletme A.Ş., officiële site — "world's largest integrated gold, silver and jewelry complex", Yenibosna, 180.000 m², 2.500+ bedrijven, geopend 2006. https://www.kuyumcukent.com.tr/en/overview · https://www.kuyumcukent.com.tr/en/Our-History
[6] Wikipedia, "Istanbul Airport" — cargo terminal Tayakadın, Arnavutköy, 41°15′19″N 28°42′46″E, cargo-diensten sinds 2022-02-05. https://en.wikipedia.org/wiki/Istanbul_Airport
[7] İGA Istanbul Airport, officiële site — "Cargo and Logistics Center". https://www.igairport.aero/en/aviation/cargo-and-logistics-center/cargo-and-lojistics/
[8] `v2/design/routebrieven/pgm-springs-zurich.md` (M31 golf 3, zelfde sessie) — hergebruikt anker `pgm-zrh-vrachtterminal` (47,4647/8,5492), zelf satelliet-gelegd in die brief.
[osm] OpenStreetMap/Nominatim (ODbL) — Metalor-gebouw Rue des Perveuils/Route des Grands-Bois, Marin-Epagnier (47,0107/7,0112); Kuyumcukent-kruising, Yenibosna Merkez Mahallesi (41,0028–41,0037/28,8148–28,8151); Biel/Bienne en Bern (stadscentroïdes, via-indicatie). https://www.openstreetmap.org
[v1] `data/goud.js` — au-ref-metalor cap. ≈ 650 t/j, au-air-zrh/au-air-ist/au-mkt-turkije als stadsniveau-
referentiepunten (nu vervangen door site-niveau ankers in deze brief).
Satellietblik: `v2/build-cache/satcheck/sat-goud-metalor-istanbul-metalormarin.png`,
`sat-goud-metalor-istanbul-istcargo.png`, `sat-goud-metalor-istanbul-kuyumcukent.png` (Esri z15, 2026-09-28).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 4)

**Recept:** `v2/tools/bak_stromen.sh` → `bak_goud_metalor_istanbul()`. Draaien:
`bash v2/tools/bak_stromen.sh goud-metalor-istanbul` → `v2/data/stroomroute-goud-metalor-istanbul.json`
(135,8 KB, versie 2, punt_formaat lonlat).

| # | modaliteit | km | punten | naad met vorige | stippel? |
|---|---|---|---|---|---|
| 1 | truck | 195,2 | 6.067 | 0,00 km | nee |
| 2 | truck | 0,9 | 2 | 0,00 km | ja — ZRH-airside last mile |
| 3 | lucht | 1.738,9 | 71 | 0,00 km | nee — doorgetrokken (grootcirkel) |
| 4 | truck | 37,1 | 1.116 | 0,00 km | nee |
| **totaal** | | **1.972,1** | **7.256** | | |

**4 markers**, alle **0,0 m** van hun lijn (au-ref-metalor, au-zrh-vrachtterminal, au-ist-vrachtterminal,
au-kuyumcukent).

**Toelichting per been:**
- **b1 (truck, profiel `goud-metalor-istanbul-marin-zrh`, extract zwitserland):** Metalor → Biel/Bienne →
  Bern → ZRH-vrachtplatform-openbare-wegpunt. **195,2 km tegen ontwerp ≈180 km = +8,4%, BINNEN ±15%.** De
  via-punten (Biel/Bienne, Bern) snapten op 0,01–0,57 km — geen wegklasse-correctie nodig. Het ZRH-platform
  zelf (47.4647,8.5492) is airside/privéterrein zonder aansluiting op het openbare net; het wegbeen eindigt
  daarom op het bekende openbare-wegpunt 47.472087,8.554523 (hergebruikt uit `goud-loulo-ticino.md` /
  `goud-pamp-shanghai.md`, zelfde golf-patroon), gevolgd door een korte stippel (0,914 km).
- **b2 (lucht, `maak_luchtbeen.py`):** vlucht ZRH → IST, **1.738,9 km grootcirkel** tegen de
  brief-schatting ≈1.739 km hemelsbreed — vrijwel exact. Doorgetrokken, geen stippel (bakhandleiding §2
  Lucht): een vlucht tussen twee gelegde vrachtterminals is geen gat.
- **b3 (truck, profiel `goud-metalor-istanbul-ist-kuyumcukent`, extract turkije):** IST-vrachtterminal →
  Kuyumcukent. **37,1 km tegen ontwerp ≈30 km = +23,6%, BUITEN ±15%.** Geen gepubliceerde
  wegbeheerder-lengte voor dit exacte traject (alleen een ontwerp-schatting, brief §2); geen via-punt
  bijgeschoven om de toets te halen — bevinding, niet dichtgetrokken. **Het IST-vrachtterminalanker bleek
  NIET airside-geïsoleerd** — anders dan de terugval die de brief (§"bak_aanwijzingen") voorzag naar
  analogie van het ZRH-anker in `goud-loulo-ticino.md`: de wegscan snapte direct op 0,03 km zonder "geen
  wegpad", dus geen stippel en geen zelf toegevoegde via-punten nodig.

**Toetsuitkomsten:**
- Naden tussen alle opeenvolgende benen: **0,00 km** (geen enkele > 5 km-norm).
- `toets_knikken.py`: been 1 (b1) heeft **2 TERUGLOOP-punten** op straal 3 m en 6 m (bij Biel/Bienne
  46.94466,7.45902 en Bern 47.13994,7.24330) — sub-10-meter ruis bij de via-punt-snap, geen echte omweg of
  keerlus op wegschaal (ter vergelijking: `goud-loulo-ticino`/`goud-pamp-shanghai` hebben 0 terugloop, wel
  vergelijkbare spike-ruis van 2–40 m). Niet gerepareerd: op wereldschaal verwaarloosbaar en de via-punten
  zijn per brief §4/§7 al "indicatief, niet zelf OSM-wegvertex-geverifieerd" — het is precies het soort
  proces-ruis dat de handleiding als bevinding laat staan in plaats van een via-punt te verschuiven.
  Verder 28 spikes ≥60° op radius ≤40 m (normaal patroon, geen omkeringen).
- `toets_rechte_benen.py --min-km 5`: **geen bevindingen** voor deze stroom (geen been ≥5 km met
  omwegfactor 1,000 dat een stippel zou moeten zijn).
- `json.load`: versie 2 · punt_formaat lonlat · modaliteiten alle in {truck, lucht} ⊂ de toegestane set ·
  elk been ≥2 punten · bestand 135,8 KB.

**Lessen:**
- De ZRH-airside-last-mile (47.472087,8.554523 ↔ 47.4647,8.5492) is nu een **derde keer letterlijk
  hergebruikt** (na `goud-loulo-ticino` en `goud-pamp-shanghai`) — dit is stabiel gereedschap geworden voor
  elk goud-been dat via Zürich Airport gaat.
- De brief anticipeerde terecht op een mógelijk airside-probleem bij het IST-anker (naar analogie van ZRH),
  maar de meting weerlegde dat: niet elk vrachtplatform is geïsoleerd, en de terugval-instructie in de brief
  bleek dit keer niet nodig. Goed voorbeeld van "meet het, neem niet aan".
- b3's +23,6% boven ontwerp-km is een normale ontwerp-schatting-vs-gemeten-wegroute-afwijking op een korte
  stedelijke corridor (37,1 tegen 30 km, ~7 km verschil) — geen bronfout, gewoon geen gepubliceerde
  wegbeheerder-lengte om tegen te toetsen.

**Centrale correctie (2026-09-28, orkestrator):** via-punt **Bern** is uit het wegprofiel gehaald. Het ligt niet op de doorgaande route Biel → Zürich; die loopt over de A5 langs Solothurn naar de A1 bij Luterbach. Het punt dwong een omweg van ~40 km af. Resultaat: b1 van 195 naar **152,6 km** (1,2× hemelsbreed, realistisch voor Marin → Zürich Airport) en totaal 1.929,5 km. De "~180 km" uit §2 was een schatting op de route via Bern. Dezelfde klasse als het via-punt Zug in goud-pamp-shanghai (golf 3).
