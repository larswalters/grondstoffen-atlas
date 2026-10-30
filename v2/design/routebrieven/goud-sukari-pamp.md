# Routebrief (licht) · Goud — Sukari (Egypte) → Marsa Alam → Cairo → Zürich → MKS PAMP Castel San Pietro (Zwitserland)

**stroom-id:** `goud-sukari-pamp` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) ·
**status:** gebakken
**Keten in één zin:** doré van de Sukari-goudmijn (Oostelijke Woestijn, Egypte) per truck over de Marsa Alam-weg naar
Marsa Alam Intl (RMF), per vrachtvlucht naar Cairo (CAI) en per vrachtvlucht naar Zürich (ZRH), daar per truck over de
Gotthard-as naar MKS PAMP in Castel San Pietro (Ticino); de laatste twee schakels zijn **aannemelijk, één bron**.
**Welke as van het verhaal:** Noord-Afrika/Rode Zee → Zwitserland: Sukari-doré naar MKS PAMP, de eerste keten die Egypte
en de Rode Zee op de bol zet. Volume **500.000 oz = 15,6 t Au/j** (Sukari 2025, AngloGold Ashanti Annual Report 2025,
koz ÷ 32,15; mijnniveau, 100%- of 50%-basis niet vastgesteld) [1]; alle goud en zilver van Sukari gaat naar MKS PAMP [1].

## 1 · Ketenkaart
```
Sukari-verwerkingsinstallatie `au-sukari-plant`
  ──(b1 truck · mijnweg → Marsa Alam → weg naar RMF · osm-meting 96 km)──►
Marsa Alam Intl vrachtplatform (RMF) `au-rmf-vrachtplatform`   [last mile airside = stippel 0,45 km]
  ──(b2 lucht · vlucht RMF → CAI, grootcirkel, aannemelijk · 596,5 km)──►
Cairo Intl vrachtplatform (CAI) `au-cai-vrachtplatform`
  ──(b3 lucht · vlucht CAI → ZRH, grootcirkel, aannemelijk · 2.744,9 km)──►
Zürich Airport vrachtplatform (ZRH) `au-zrh-vrachtterminal`   [last mile airside = stippel 0,9 km, hergebruikt]
  ──(b4 truck · A2 Gotthard-as · omgekeerde letterlijke kopie goud-pamp-shanghai b1 · 263,3 km)──►
MKS PAMP, Castel San Pietro `au-pamp-raffinaderij` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Sukari-plant → RMF, openbare weg bij de terminal | mijnweg → Marsa Alam (km 24) → weg Marsa Alam–RMF; refs niet vastgesteld | osm-meting 96 km (indicatie, geen bronopgave); hemelsbreed 68 km, geen wegkm [osm] | maak_stroombeen_weg, profiel `goud-sukari-pamp-sukari-rmf` (gemeten 96,1 km, +0,1%) | nee |
| b1s | A | truck | RMF openbare weg → vrachtplatform | airside, geen openbare weg | 0,45 hemelsbreed | `--stippel` | **ja** — "RMF-vrachtplatform last mile (schematisch — airside/privéterrein)" |
| b2 | B | lucht | RMF → CAI | vrachtvlucht RMF → CAI (aannemelijk: één bron, 2015, toen verder naar Canada) | 596,5 grootcirkel | maak_luchtbeen | nee — doorgetrokken |
| b3 | B | lucht | CAI → ZRH | vrachtvlucht CAI → ZRH (aannemelijk: geen bron voor deze route) | 2.744,9 grootcirkel | maak_luchtbeen | nee — doorgetrokken |
| b4s | C | truck | ZRH vrachtplatform → openbare weg | airside | 0,9 | `--stippel` (letterlijk als pamp-shanghai, omgekeerd) | **ja** — ZRH last mile |
| b4 | C | truck | ZRH-openbare weg → MKS PAMP | A2/A4 Gotthard-as | 263,3 [kopie pamp-shanghai b1] | **omgekeerde letterlijke kopie** `goud-pamp-shanghai-weg-pamp-zrh.geojson` | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-sukari-plant` | mijn / verwerking | Sukari Gold Mines, verwerkingsinstallatie | 24.9561, 34.7102 | [1][4][osm] | bron-gelegd (z14 gezien: gebouwen- en tankcluster direct W van de dagbouwput, groot lichtgekleurd tailingsveld W ervan, zonnepanelenveld N) |
| `au-rmf-vrachtplatform` | overslag / lucht | Marsa Alam Intl (RMF), terminalapron | 25.5550, 34.5912 | [5][osm] | aannemelijk (z16 gezien: terminal met groot apron ZW van de forecourt; geen apart vrachtgebouw te onderscheiden, RMF is een charterluchthaven; OSM-puntje ligt op de baan en is niet gebruikt) |
| `au-rmf-weg` | routeerpunt (openbare weg) | weg bij de RMF-terminal, forecourt | 25.5565, 34.5947 | [osm] | bron-gelegd (z16: forecourtlus O van de parkeerplaats; snap 0,05 km) |
| `au-cai-vrachtplatform` | overslag / lucht | Cairo Intl (CAI), vrachtapron O van de taxibaan | 30.1270, 31.4156 | [2][3] | aannemelijk (z16 gezien: apron met geparkeerde breedrompvrachttoestellen naast grote hangars met blauwe daken; welke hal Cairo Cargo is niet te onderscheiden) |
| `au-zrh-vrachtterminal` | overslag / lucht | Zürich Airport vrachtplatform (hergebruikt, goud-loulo-ticino.md) | 47.4647, 8.5492 | [7] | bron-gelegd (hergebruikt) |
| `au-pamp-raffinaderij` | raffinaderij | MKS PAMP SA, Via alle Zocche 1, Castel San Pietro (hergebruikt, goud-pamp-shanghai.md) | 45.8546, 9.0025 | [7] | bron-gelegd (hergebruikt) |

## 4 · Via-punten (b1, op de gemeten OSM-route; b4 zit in de kopie)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Mijnweg op de weg bij Marsa Alam (km 24) | 25.0559, 34.8453 | punt waar de mijnweg de doorgaande weg bereikt; pint de route aan de Marsa Alam-kant |
| b1 | 2 | weg Marsa Alam–RMF, km 42 | 25.1683, 34.8299 | pint de noordwaartse route (binnenwegen, geen kuststrook) |
| b1 | 3 | weg Marsa Alam–RMF, km 60 | 25.3053, 34.7376 | idem |
| b1 | 4 | weg Marsa Alam–RMF, km 78 | 25.4411, 34.6721 | vlak voor de luchthavenafslag |
Alle vier liggen op de eerst zonder via-punten gemeten route (identiek resultaat); b1 heeft geen echte alternatieve corridor.
Geofabrik-regio: `egypte`. b4: `zwitserland` (in de kopie).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Sukari-plant | Sukari Gold Mines (AngloGold Ashanti 50%, Egyptische staat) | erts → doré | 500 koz in 2025 | [1] |
| MKS PAMP, Castel San Pietro | MKS PAMP SA | doré → LBMA-baren | vestiging ≈ 450 t/j (sitelaag, bedrijfsopgave) | [1][7] |

## 6 · Stoppunt
De brief stopt bij MKS PAMP in Castel San Pietro: het jaarverslag noemt alleen "MKS PAMP", niet de vestiging, en
Ticino is de aannemelijke keuze. Fase D vervalt: geen bron koppelt deze baren aan een vervolgbestemming.

## 7 · Open punten
- **Geen bron voor het vervoer van Sukari naar PAMP.** [1] zegt alleen dat al het goud en zilver naar MKS PAMP gaat; Castel San Pietro (Zwitserland) is aannemelijk, niet bevestigd.
- **RMF → CAI** rust op persberichten 2015–2017 (22 dozen / 390–404 kg met een privévliegtuig, toen verder naar Canada, een keer met Gulf Air) [2][3]; de huidige afnemer is een andere.
- **CAI → ZRH heeft geen bron**: aannemelijk; geen carrier of tussenlanding gevonden, dus één directe vlucht.
- **Wegkm is een eigen OSM-meting** (96 km), geen bron; de 70–90 km uit het ontwerp was een hemelsbrede schatting.
- **Cargo-ankers RMF en CAI zijn platformniveau, geen pand**; RMF heeft geen aanwijsbaar vrachtgebouw.
- **Volume is mijnniveau** (Sukari-aandeel van AGA 50%); attributable niet vastgesteld.
- **Sitelaag** kent Sukari niet (`goud-sitelaag.json`); kandidaat-site 24.9561, 34.7102 (centraal toevoegen).
- Stroom-id noemt PAMP; titel noemt Castel San Pietro (aannemelijk: AR noemt alleen MKS PAMP).

## 8 · Bronnen
[1] AngloGold Ashanti, Annual Report 2025 (p. 70): "All gold and silver production from Sukari is sold to MKS PAMP"; Sukari 500.000 oz. https://www.sec.gov/Archives/edgar/data/1973832/000197383226000070/a12025agaukannualreport_25.pdf
[2] Egypt Today, 2017 — "Sukari mine exports 404kg of Egypt's gold to Canada" (Marsa Alam → Cairo Airport, 22 dozen, Gulf Air; alleen via zoekresultaat gelezen, site blokkeert). https://www.egypttoday.com/Article/3/34693/Sukari-mine-exports-404kg-of-Egypt’s-gold-to-Canada
[3] CairoScene, 22-11-2015 — "390 KG Of Egyptian Gold Heading To Canada": 16 pakketten van Marsa Alam naar Cairo Airport, daarna Canada. https://cairoscene.com/Business/390-KG-Of-Egyptian-Gold-Heading-to-Canada
[4] Mining Technology, "Sukari Gold Mine": mijn 23 km ZW van Marsa Alam. https://www.mining-technology.com/projects/sukarigoldmine/
[5] Wikipedia, "Marsa Alam International Airport": 60 km ten noorden van Marsa Alam. https://en.wikipedia.org/wiki/Marsa_Alam_International_Airport
[6] Egypt Independent, "Egypt flies 206 kgs gold to Canada for sale" (privévliegtuig uit Marsa Alam; alleen titel/snippet gezien). https://www.egyptindependent.com/egypt-flies-206-kgs-gold-canada-sale
[7] `v2/design/routebrieven/goud-pamp-shanghai.md` (anker PAMP + ZRH, b1 A2 Gotthard 263,3 km) en `goud-loulo-ticino.md` (ZRH-anker, airside-patroon).
[osm] OpenStreetMap (ODbL) via Nominatim: Sukari Gold Mine 24,956075/34,710229 · Marsa Alam Intl 25,5567332/34,586225 (op de baan) · Cairo Intl 30,1140505/31,4245461. Route: Geofabrik-extract egypte.
Satellietblik: `v2/build-cache/satcheck/sat-goud-sukari-pamp-sukari.png`, `-rmf.png`, `-rmf-terminal.png`, `-cai.png`, `-cai-cargo.png` (Esri z14–z16, 2026-10-30).
Voorbereid (build-cache/ais/graaf): `goud-sukari-pamp-weg-sukari-rmf.geojson` (96,1 km), `…-lucht-rmf-cai.geojson`, `…-lucht-cai-zrh.geojson`, `…-weg-zrh-pamp.geojson` (omgekeerd).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)

**Stroom:** `goud-sukari-pamp` · **bestand:** `v2/data/stroomroute-goud-sukari-pamp.json` (138,8 KB) ·
**recept:** `bak_goud_sukari_pamp()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh goud-sukari-pamp`).

**6 benen · 3.702,2 km · 7.384 punten · 6 markers.** Gemeten truckbenen en vluchten zijn doorgetrokken; de twee
last-mile-stukjes bij RMF en ZRH zijn stippel (airside), verder geen gat. Geen zee, geen haven-aanloop.

| # | fase | modaliteit | km | naad met vorig been | stippel? |
|---|---|---|---|---|---|
| b1 | A | truck | 96,2 | — (start) | nee |
| b1s | A | truck | 0,4 | 0,000 km | **ja** — RMF-vrachtplatform last mile (airside) |
| b2 | B | lucht | 596,5 | 0,000 km | nee (doorgetrokken, aannemelijk) |
| b3 | B | lucht | 2.744,9 | 0,000 km | nee (doorgetrokken, aannemelijk) |
| b4s | C | truck | 0,9 | 0,000 km | **ja** — ZRH-vrachtplatform last mile (airside) |
| b4 | C | truck | 263,3 | 0,000 km | nee (omgekeerde letterlijke kopie) |

**Recept:** b1 = profiel `goud-sukari-pamp-sukari-rmf` (extract egypte, wegscan_puur, 4 via-punten, al gebakken vóór
deze run: `goud-sukari-pamp-weg-sukari-rmf.geojson`, niet opnieuw gescand) · b2 en b3 = `maak_luchtbeen.py` (al
klaar) · b4 = byte-gelijke, omgekeerde kopie van `goud-pamp-shanghai-weg-pamp-zrh.geojson` (6.154 punten, getoetst
op `a[::-1] == b`) · stippels als `--stippel` in de functie. De bake zelf draaide in één run (`hecht_marnet.py route`,
zwaar-slot), alle benen "vooraf gebakken lijn".

**Toelichting per been:**
- b1 truck, **96,2 km tegen 96 km = +0,2%**. Dit is een EIGEN OSM-meting uit de brief (geen bedrijfs- of
  overheidsopgave; hemelsbreed 68 km, geen wegkm), dus de ±15%-toets is hier een indicatie en geen onafhankelijke
  bevestiging: het getal bevestigt alleen dat de herbake identiek is aan de meting.
- b1s stippel, **0,389 km** gemeten tegen 0,45 hemelsbreed in de brief: het RMF-apron (25,5550/34,5912) is
  airside en heeft geen aansluiting op het openbare net; het wegbeen eindigt op de forecourt (25,5565/34,5947).
- b2 vlucht RMF → CAI, grootcirkel 596,5 km, **aannemelijk**: één bron (persberichten 2015-2017, 22 dozen /
  390-404 kg met een privévliegtuig, toen verder naar Canada). Doorgetrokken (geen gat in het net). Vrachtplatform
  RMF is apron-niveau, geen aanwijsbaar vrachtgebouw.
- b3 vlucht CAI → ZRH, grootcirkel 2.744,9 km, **aannemelijk, geen bron voor deze route**: één directe vlucht
  aangenomen, geen carrier of tussenlanding gevonden. Vrachtplatform CAI is apron-niveau.
- b4s stippel, **0,914 km**: ZRH-vrachtplatform last mile, patroon van `goud-loulo-ticino` / `goud-pamp-shanghai`
  (omgekeerde richting: platform naar openbare weg 47,472087/8,554523).
- b4 truck, **263,3 km** (A2 Gotthard-as), letterlijke kopie, niet opnieuw gescand. Dit is OSM-weglengte en komt
  ruim boven de ~200 km hemelsbrede schatting die elders in de golf is gebruikt (zie `goud-pamp-shanghai` §9); hier
  geldt 263,3 km als de brief-waarde, dus geen afwijking.

**Ankers, status ongewijzigd t.o.v. §3:** `au-sukari-plant` en `au-rmf-weg` bron-gelegd; `au-rmf-vrachtplatform` en
`au-cai-vrachtplatform` aannemelijk (apron, geen aanwijsbaar cargo-pand); `au-zrh-vrachtterminal` en
`au-pamp-raffinaderij` bron-gelegd (hergebruikt). De vestiging Castel San Pietro blijft aannemelijk: het jaarverslag
noemt alleen "MKS PAMP". Markers: alle 6 uit §3, in de bake als `--marker` gezet (ook het routeerpunt `au-rmf-weg`).

**Toets (bakhandleiding §5):**
- Naden tussen alle zes de benen: **0,000 km**.
- `toets_knikken.py --bestand`: b1 6 knikken waarvan 1 omkeringsbocht (152 gr bij 25,3062/34,7398, "scherpe bocht,
  echt", v=1,4) en 5 spikes straatniveau (R 11-102 m) · luchtbenen 0 · b4 29 knikken (kopie, bergweg) · **0 terugloop**.
- `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de uitslag (luchtbenen worden overgeslagen,
  stippels zijn < 5 km).
- Markers: alle 6 op **0,000 km** van hun lijn.
- `json.load` slaagt, `versie` 2, `punt_formaat` lonlat, modaliteiten {truck, lucht}, elk been >= 2 punten, 138,8 KB.

**Open punten (uit §7, ongewijzigd):** geen bron voor vervoer Sukari naar PAMP; RMF-CAI op persberichten 2015-2017;
CAI-ZRH zonder bron; wegkm is eigen meting; cargo-ankers RMF/CAI op platformniveau; volume op mijnniveau; Sukari
ontbreekt in de sitelaag (centraal: kandidaat 24,9561/34,7102).

**Gereedschapslessen:**
- De brief was bij aanvang van deze run al volledig voorbereid (profiel, drie geojsons, kopie): de bake-agent hoefde
  alleen de functie te schrijven en te draaien. Een eerdere afgebroken poging had geen restanten van de functie.
- Eén fout in mijn eigen edit: een `\n` in een Python-string via een heredoc kwam letterlijk in `bak_stromen.sh`
  terecht (`" \n    --marker`), met `unrecognized arguments: n` van `hecht_marnet.py`. Opgelost met `chr(92)` in de
  replace; `bash -n` vangt dit niet. Voor een regelinvoeging met een backslash-vervolg: schrijf de regel via Write of
  gebruik `chr(92)`, en draai altijd meteen de bake.
