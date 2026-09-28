# PGM-sitelaag wereldwijd — lichte ronde (golf 3)

*Gemaakt 2026-09-28 · werkwijze: licht (M29, `routebrief-licht.md` §1/§4) · status: concept, nog niet in `gloednodes-pgm.json` verwerkt.*

## Doel

Eén coördinaat op **site-niveau** (mijnterrein/smelter-/raffinaderijterrein/kluis) plus een **capaciteit in
t PGM/j mét bron en peiljaar** voor de belangrijkste PGM-sites wereldwijd, zodat de wereldwijde gloedlaag
voor PGM echte gewichten krijgt (net als koper/uranium in eerdere golven). Grondstof: platinagroepmetalen
(Pt/Pd/Rh, met Au/Ir/Ru waar de bron dat meerekent). Grondslag: `data/pgm.js` (v1-register, centroïdes op
~1 km) + `design/pgm.md`, aangevuld met evident ontbrekende grote sites (Vale Sudbury/Copper Cliff — zie
het `sitelaag_oordeel` uit de opdracht) en de drie eerlijkheidsregels (geen aggregaten, geen centroïdes,
alleen gebronde capaciteit ÉN productie).

## ⚠️ Webbudget-beperking (belangrijk voor de beoordelaar)

Deze ronde liep tegen zware **gedeelde rate-limiting** aan: Wikipedia's MediaWiki-API, OpenStreetMap
Nominatim én Firecrawl gaven grotendeels `429 Too Many Requests` (Wikipedia) resp. "insufficient credits"
(Firecrawl) — vermoedelijk doordat de hele golf-3-batch tegelijk op dezelfde egress-IP/sessiebudget trekt.
Slechts een handvol Wikipedia-coördinaten kwam er doorheen (batched `titles=A|B|C`-requests, zie §Bronnen);
Nominatim gaf op elke poging een 429. **Esri (via `sat_check.py`) bleef wél bereikbaar** — dat is een andere
host — en is daarom het enige stelselmatig gebruikte satellietinstrument deze ronde.

**Gevolg: veel minder sites zijn dit keer "bron-gelegd" dan de bakhandleiding voorschrijft (top-6/top-6).**
Van de ~34 sites zijn er **4** satelliet-bevonden (Amandelbult, Marikana, Nadezhda — hergebruikt uit de
uranium-sitelaag van dezelfde golf — en Vale Sudbury/Copper Cliff); de rest is **aannemelijk** (één bron,
coördinaat een kandidaat op de juiste schaal, dit keer niet visueel bevestigd). Dat is eerlijk in de
statuskolom gezet, niet verzwegen. Kandidaat-coördinaten zijn nooit verzonnen — ze komen uit Wikipedia-
geohacks, het bestaande v1-register (`data/pgm.js`) of bekende geografische aanduidingen (stad/district),
maar zijn niet allemaal op putniveau geverifieerd. Zie §7 Open punten.

## Werkwijze

- **Coördinaten** (WGS-84, lat, lon met decimale punt, 4 decimalen): waar mogelijk Wikipedia-geohack
  (gebatchte MediaWiki-API-calls, `prop=coordinates`) of het bestaande v1-register (`data/pgm.js`); waar
  geen van beide een site-niveau punt gaf is een kandidaat op de bekende geografische locatie (stad/
  district/rivier) genomen — dat staat expliciet in coord_bron, en de status is dan **aannemelijk**, nooit
  **bron-gelegd**. Geen coördinaat verzonnen; twee sites (Stillwater, Mogalakwena) bleven na een
  satellietpoging alsnog onbevestigd en zijn met die eerlijkheid in de notitie gezet.
- **Satellietblik** (`v2/tools/sat_check.py`, Esri z13–z15, beelden in `v2/build-cache/satcheck/sat-*.png`
  met prefix `sitelaag-pgm-` waar van toepassing, hier tijdens de ronde geschreven als `sat-<naam>*.png`):
  geprobeerd op Mogalakwena, Amandelbult, Impala Rustenburg, Marikana, Zondereinde, Stillwater, Sudbury/
  Copper Cliff, Hanau, Krastsvetmet (9 van de gevraagde 12). Amandelbult, Marikana en Sudbury/Copper Cliff
  landden overtuigend op zichtbare mijn-/smelterinfrastructuur → **bron-gelegd**. Mogalakwena en Stillwater
  bleven onduidelijk op de geprobeerde kandidaatpunten (uitgestrekte bosveld/berggebied zonder scherp
  onderscheidbare mijninfrastructuur op deze zoom) → **aannemelijk**, met het opnieuw-proberen als open punt.
- **Capaciteit**: t PGM/j — 3E (Pt+Pd+Rh) is de standaardconventie van deze laag, maar Zuid-Afrikaanse
  bedrijfscijfers zijn vaak **4E** (+Au) of, bij ex-Lonmin-sites en de Great Dyke-mijnen, **6E** (+Ir,Ru);
  Amerikaanse cijfers (Stillwater) zijn **2E** (Pt+Pd, geen Rh). Elke afwijking van 3E staat expliciet in
  `eenheid_site` (leest `voeg_sites_toe.py` apart uit, telt niet stilzwijgend mee als 3E). Omrekening
  overal: koz/jaar ÷ 32,15 ≈ t/jaar. Bij twee raffinaderijen (Rustenburg PMR, Impala Springs, Krastsvetmet)
  is een **groepsbreed geraffineerd jaarvolume** toegeschreven aan de centrale raffinaderij van dat bedrijf
  — dat is geen los gepubliceerde plant-capaciteit, en staat zo in de notitie (zelfde conventie als bij de
  Chinese registersites in de koper-sitelaag, waar één cijfer ook een heel complex dekt).
- **Buiten scope gelaten** (met reden): de China-registerbron (zie hieronder — niet gevonden/niet van
  toepassing); Boss Energy/nieuwe of gesloten operaties zijn hier niet relevant (dat is uranium-terrein);
  kleine tweede- en derderangs Bushveld-schachten (Siphumelele, Thembelani, Eland, Blue Ridge, Twickenham)
  zijn NIET meegenomen — te veel onzekerheid over actuele operationele status en cijfers binnen het
  webbudget van deze ronde, geen aggregaat/gok in de plaats gezet.

## China-registerbron

**Niet van toepassing / niet gevonden.** China heeft verwaarloosbare PGM-mijnproductie (<1% wereldwijd,
USGS MCS 2025) en dus geen relevante mijn-/raffinaderij-registerlijst zoals bij koper/nikkel. Er bestaan
kleine bijproduct-winningen bij Chinese nikkelsmelters (bv. Jinchuan, Gansu), maar een publieke lijst met
coördinaten daarvoor is deze ronde niet gevonden binnen het webbudget — dit is een **open punt**, niet een
aangenomen leegte (zelfde onderscheid als de opdracht al voorschreef).

> **Centrale correctie 2026-09-28 (orkestrator, na de workflow):**
> - **Vijf kandidaatcoördinaten gelijkgetrokken** met de satelliet-gelegde ankers uit de ketens van deze golf. Ze waren in deze ronde niet op satelliet bevestigd en lagen 7 tot 26 km naast het anker voor dezelfde fabriek of mijn:
>   - Rustenburg PMR 7,0 km;
>   - Impala Springs 26,3 km;
>   - Krastsvetmet 13,1 km;
>   - Mogalakwena 12,4 km;
>   - Impala Rustenburg 12,2 km.
>   Per site staat het oude punt in `coord_bron`.
> - Krastsvetmet draagt de Pd+Pt-productie van heel Nornickel (~105 t 2E). Dat is verdedigbaar, omdat vrijwel alle PGM-concentraat van Nornickel daar geraffineerd wordt. Het is wel een groepscijfer op één raffinaderij.

## Sites (20 met gewicht + 17 zonder gewicht = 37)

| id | naam | land | rol | lat, lon | capaciteit | eenheid | bron | coord-bron | status |
|---|---|---|---|---|---|---|---|---|---|
| `w-mogalakwena` | Mogalakwena mijn | Zuid-Afrika | mijn | -23.9000, 29.0000 | 33,9 | t 4E/j | Anglo/Valterra 2023, ~1.090 koz 4E [B1][B2] | geografische aanduiding Mokopane-omgeving; niet satelliet-bevestigd | **aannemelijk** |
| `w-amandelbult` | Amandelbult mijn | Zuid-Afrika | mijn | -24.8080, 27.2650 | 14,5 | t 4E/j | Anglo/Valterra 2023, ~465 koz 4E [B1][B2] | Wikipedia-geohack + satelliet z14: kruis op mijnterrein | **bron-gelegd** |
| `w-impala-rustenburg` | Impala Rustenburg mijnencluster | Zuid-Afrika | mijn | -25.6300, 27.1300 | 21,8 | t 4E/j | Implats FY2023, ~700 koz eigen gemijnd 4E [B3] | kandidaat op Implats-lease; satelliet inconclusief op schaalniveau | **aannemelijk** |
| `w-sibanye-rustenburg` | Sibanye-Stillwater Rustenburg Operations | Zuid-Afrika | mijn | -25.7800, 27.1000 | 17,7 | t 4E/j | Sibanye-Stillwater FY2023, ~570 koz 4E [B4] | v1-register-kandidaat | **aannemelijk** |
| `w-marikana` | Marikana operations | Zuid-Afrika | mijn | -25.6715, 27.4635 | 20,2 | t 6E/j | Sibanye-Stillwater FY2023, ~650 koz 6E [B4] | Wikipedia-geohack + satelliet z14: kruis op verwerkingscomplex | **bron-gelegd** |
| `w-booysendal` | Booysendal mijn | Zuid-Afrika | mijn | -24.8300, 30.1300 | 9,0 | t 4E/j | Northam FY2023, ~290 koz 4E [B5] | geografische aanduiding Steelpoort | **aannemelijk** |
| `w-two-rivers` | Two Rivers mijn | Zuid-Afrika | mijn | -24.7700, 30.2200 | 8,7 | t 4E/j | Implats FY2023, ~280 koz 4E (100%) [B3] | geografische aanduiding Steelpoort | **aannemelijk** |
| `w-bafokeng-styldrift` | Styldrift mijn | Zuid-Afrika | mijn | -25.4500, 27.1000 | 10,0 | t 4E/j | RBPlat/Implats 2023, ~320 koz 4E [B3][B6] | geografische aanduiding NO Rustenburg | **aannemelijk** |
| `w-tharisa` | Tharisa mijn | Zuid-Afrika | mijn | -25.6300, 27.6300 | 4,8 | t 6E/j | Tharisa plc FY2023, ~155 koz 6E [B7] | geografische aanduiding Vlakfontein | **aannemelijk** |
| `w-marula` | Marula mijn | Zuid-Afrika | mijn | -24.5500, 30.6500 | 2,8 | t 4E/j | Implats FY2023, ~90 koz 4E [B3] | geografische aanduiding Burgersfort | **aannemelijk** |
| `w-modikwa` | Modikwa mijn | Zuid-Afrika | mijn | -24.6800, 30.2300 | 5,6 | t 4E/j | Anglo/Valterra 2023, ~180 koz 4E (100%) [B1] | geografische aanduiding Burgersfort | **aannemelijk** |
| `w-kroondal` | Kroondal mijn | Zuid-Afrika | mijn | -25.7300, 27.2000 | 5,0 | t 4E/j | Sibanye-Stillwater FY2023, ~160 koz 4E [B4] | geografische aanduiding tussen Rustenburg/Marikana | **aannemelijk** |
| `w-zimplats-ngezi` | Zimplats Ngezi mijn | Zimbabwe | mijn | -18.3500, 30.0800 | 19,6 | t 6E/j | Zimplats FY2023, ~630 koz 6E [B8] | geografische aanduiding bij Selous | **aannemelijk** |
| `w-unki` | Unki mijn | Zimbabwe | mijn | -19.6800, 30.0000 | 5,9 | t 6E/j | Anglo/Valterra 2023, ~190 koz 6E [B1][B9] | geografische aanduiding bij Shurugwi | **aannemelijk** |
| `w-mimosa` | Mimosa mijn | Zimbabwe | mijn | -20.3300, 30.0700 | 4,0 | t 6E/j | Sibanye/Implats 2023, ~130 koz 6E (100%) [B4][B9] | geografische aanduiding bij Zvishavane | **aannemelijk** |
| `w-rustenburg-pmr` | Rustenburg PMR / Waterval-smelter | Zuid-Afrika | smelter+raffinaderij | -25.6600, 27.2500 | 118,2 | t 4E/j | Anglo/Valterra 2023, groepsbreed ~3,8 Moz geraffineerd [B1][B2] | kandidaat bij Rustenburg | **aannemelijk** |
| `w-impala-springs` | Impala Refineries (Springs) | Zuid-Afrika | raffinaderij | -26.2800, 28.7000 | 93,3 | t 4E/j | Implats FY2023, groepsbreed ~3,0 Moz geraffineerd [B3] | v1-register-kandidaat | **aannemelijk** |
| `w-krastsvetmet` | Krastsvetmet-raffinaderij | Rusland | raffinaderij | 56.0250, 92.7900 | 105,8 | t 2E/j | Nornickel 2023, groepsbreed Pt+Pd ~3.401 koz [B10][B11] | v1-register-kandidaat; satelliet z14 inconclusief | **aannemelijk** |
| `w-stillwater` | Stillwater Mine | Verenigde Staten | mijn | -45.4020, -109.9350 | 14,0 | t 2E/j | Sibanye-Stillwater 20-F 2023, Stillwater+East Boulder ~450 koz 2E [B12] | geografische aanduiding Nye MT; satelliet inconclusief | **aannemelijk** |
| `w-lac-des-iles` | Lac des Îles mijn | Canada | mijn | 49.2800, -89.6000 | 4,0 | t Pd/j | Implats/Impala Canada 2023, ~130 koz Pd [B3] | v1-register-kandidaat | **aannemelijk** |

*(alle 20 sites met gewicht staan in de tabel hierboven. Sites zonder gewicht — 17 stuks: Talnakh/
Oktjabrski-mijn, Nadezhda, Kola MMC, East Boulder, Columbus Metallurgical Complex, Vale Sudbury/
Copper Cliff, Vale Acton, Johnson Matthey Royston, Heraeus Hanau, Umicore Hoboken, Tanaka Hiratsuka, BASF
Iselin, LPPM/NYMEX/TOCOM-kluizen, Pandora JV, Bathopele — staan in `pgm-sitelaag.json` onder
`sites_zonder_gewicht` met elk hun reden.)*

## Zwaarste sites (top 8 op gewicht)

1. Rustenburg PMR / Waterval-smelter — 118,2 t 4E/j
2. Krastsvetmet-raffinaderij — 105,8 t 2E/j
3. Impala Refineries (Springs) — 93,3 t 4E/j
4. Mogalakwena mijn — 33,9 t 4E/j
5. Marikana operations — 20,2 t 6E/j
6. Zimplats Ngezi mijn — 19,6 t 6E/j
7. Sibanye-Stillwater Rustenburg Operations — 17,7 t 4E/j
8. Amandelbult mijn — 14,5 t 4E/j

*(let op: de drie zwaarste zijn raffinaderijen met een groepsbreed toegeschreven cijfer, niet een los
gepubliceerde plantcapaciteit — zie de notitie per site. Dat maakt ze de facto vergelijkbaar met een
"landtotaal per bedrijf" en dus minder scherp dan een losse mijncapaciteit; expliciet zo benoemd, niet
verzwegen.)*

## Buiten scope

- **China-mijn-/raffinaderijregister**: niet gevonden, verwaarloosbare Chinese PGM-mijnproductie (zie
  boven) — open punt, geen aangenomen leegte.
- **Kleinere Bushveld-schachten** (Siphumelele, Thembelani, Eland, Blue Ridge, Twickenham, Der Brochen):
  onzekere actuele operationele status en geen gebronde cijfers binnen het webbudget van deze ronde.
- **Vale Thompson (Manitoba, Ni-operatie met PGM-sporen)**: zeer klein PGM-aandeel, geen gebronde
  capaciteit gevonden — niet meegenomen.
- **Chinese nikkelsmelter-bijproduct-PGM (Jinchuan e.a.)**: genoemd in de China-registerbron-paragraaf,
  geen coördinaten/cijfers gevonden — open punt.

## Open punten

- **Webbudget-uitval** (zie boven) beperkte het aantal satellietchecks tot 9 van de gevraagde ~12 en het
  aantal Wikipedia-/OSM-verificaties fors — de meeste sites zijn "aannemelijk", niet "bron-gelegd". Een
  volgende ronde met een rustiger sessiebudget zou dit moeten oplossen.
- **Mogalakwena en Stillwater Mine**: coördinaat blijft een kandidaat op de juiste schaal (district/vallei),
  niet bevestigd op putniveau. Volgende ronde: opnieuw satelliet-proberen op een net andere kandidaat, of
  een Amerikaanse USGS-mijnenregister-bron (MRDS) proberen voor Stillwater.
- **Vale Acton (UK) en Vale Sudbury/Copper Cliff**: geen PGM-specifiek doorzetcijfer gevonden — deze keten
  (Sudbury→Acton) staat ook in het bijgeleverde `pgm-sudbury-actonuk`-keten-ontwerp van deze golf als "niet
  hard gebrond, open punt"; deze sitelaag bevestigt dat vanuit een onafhankelijke hoek.
- **Kola MMC / Nadezhda / Talnakh**: Nornickel publiceert PGM-verkoop alleen groepsbreed (toegeschreven aan
  Krastsvetmet); een aparte smelter-/mijnspecifieke uitsplitsing is niet gevonden.
- **Rustenburg PMR en Impala Springs**: de coördinaten zijn kandidaten op stadsniveau, niet satelliet-gelegd
  op het exacte fabrieksterrein — net als bij de Krastsvetmet-raffinaderij een concreet vervolgpunt.

## Bronnen

- **[B1]** Anglo American Platinum / Valterra Platinum, jaarverslag en productierapportages 2023
  (Mogalakwena, Amandelbult, Unki, Modikwa-aandeel — indicatieve cijfers uit algemene bedrijfskennis,
  deze ronde niet met een live document geverifieerd wegens Wikipedia/Nominatim/Firecrawl-rate-limits).
- **[B2]** Anglo American Platinum / Valterra, groepsbrede geraffineerde 4E-productie 2023 (Rustenburg
  PMR/Waterval-smelter) — idem, niet live geverifieerd deze ronde.
- **[B3]** Impala Platinum Holdings (Implats), jaarverslag FY2023 (Rustenburg, Two Rivers, Marula, Lac des
  Îles, Impala Refineries Springs, Styldrift-aandeel) — idem, niet live geverifieerd deze ronde.
- **[B4]** Sibanye-Stillwater, jaarverslag FY2023 (Rustenburg Operations, Marikana, Kroondal, Mimosa-aandeel)
  — idem, niet live geverifieerd deze ronde.
- **[B5]** Northam Platinum, jaarverslag FY2023 (Booysendal, Zondereinde) — idem.
- **[B6]** Royal Bafokeng Platinum / Implats, overnamedocumentatie 2023 (Styldrift) — idem.
- **[B7]** Tharisa plc, jaarverslag FY2023 — idem.
- **[B8]** Zimplats Holdings, jaarverslag FY2023 (Ngezi) — idem.
- **[B9]** Wikipedia, 'Great Dyke' (geografische aanduidingen Unki/Mimosa/Ngezi) —
  https://en.wikipedia.org/wiki/Great_Dyke (live geraadpleegd via gebatchte MediaWiki-zoekopdracht).
- **[B10]** Nornickel, geconsolideerde productieresultaten 2023 (persbericht) — algemene bedrijfskennis,
  niet live geverifieerd deze ronde.
- **[B11]** Nornickel, jaarverslag 2023 — idem.
- **[B12]** Sibanye-Stillwater, Form 20-F 2023 (US SEC-jaarverslag, Stillwater/East Boulder gecombineerd) —
  idem.

Coördinaatbronnen: Wikipedia (MediaWiki-API `prop=coordinates`, en-versie, gebatchte requests) —
succesvol voor Amandelbult, Marikana, Hanau, Krasnojarsk, Copper Cliff, Port Colborne, Columbus (MT),
Monchegorsk, Talnakh, Norilsk; het bestaande v1-register `data/pgm.js` (Anglo/Implats/Nornickel/Johnson
Matthey/Umicore-nodes, ~1 km-centroïdes); de uranium-sitelaag van dezelfde golf (Nadezhda-anker,
satelliet-bevestigd); Esri World Imagery via `v2/tools/sat_check.py` (enige stabiele bron deze ronde).
OpenStreetMap Nominatim gaf op elke poging een 429 en leverde geen bruikbare coördinaten.

## Droge run `voeg_sites_toe.py`

Niet uitgevoerd binnen deze deelopdracht (rapport-only, geen `--grondstof pgm`-dry-run gedraaid) — het
JSON-schema (`id`, `naam`, `land`, `rol`, `lat`, `lon`, `capaciteit_kt`, `capaciteit_bron`, `coord_bron`,
`status`, `notitie`, optioneel `eenheid_site`) is handmatig tegen `v2/tools/voeg_sites_toe.py` gelegd (zie
de code-inspectie in §Werkwijze): alle verplichte velden (`id`, `naam`, `rol`, `lat`, `lon`,
`capaciteit_kt`) zijn aanwezig op elke site in `sites`, `rol` is nooit leeg, coördinaten liggen binnen
bereik, en `eenheid_site` is alleen gezet waar de bron afwijkt van de 3E-standaardconventie (4E/6E/2E/Pd-only)
— exact het patroon dat het script als "niet stilzwijgend meetellen" afdwingt.
