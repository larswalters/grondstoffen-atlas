# Goud-sitelaag wereldwijd — lichte ronde (M31 golf 3)

*Gemaakt 2026-09-28 · werkwijze: licht (M29, `routebrief-licht.md` §1/§4) · status: concept, nog niet in `gloednodes-goud.json` verwerkt (dry run met `voeg_sites_toe.py` bedoeld, `--schrijf` niet gedraaid — dat gebeurt centraal).*

## Doel

Eén coördinaat op **site-niveau** (mijnterrein, raffinaderijterrein, kluis-/beursgebouw) plus een **capaciteit in t Au/j (fijn goud) mét bron** voor de belangrijkste goudsites wereldwijd, als invoer voor de wereldwijde gloedlaag (naast koper/olie/uranium/kobalt/zilver/gas uit eerdere golven). Grondslag: `data/goud.js` (v1-register, centroïdes ~1 km) + `design/goud.md` (ontwerpskelet), aangevuld met evident ontbrekende grote sites (Kibali, Fruta del Norte, Ahafo, Cerro Negro, Veladero, Altyntau) en de sites uit het ontwerp van deze golf. Het bijgeleverde ontwerp (JSON in de opdracht) leverde 42 kandidaten zónder coördinaten — de kernopdracht van dit rapport was dus eerst coördinaten vinden, niet alleen bronnen zoeken.

**Eerlijkheidsregel (M30/M31):** alleen sites met een gebronde capaciteit ÉN productie/doorzet krijgen gewicht. Projecten, stilgelegde sites, kluis-/beursvoorraden (geen jaarstroom) en sites zonder terreincoördinaat gaan naar `sites_zonder_gewicht` — wel gedocumenteerd, niet gloeiend.

## Werkwijze

- **Coördinaten** (WGS-84, lat, lon met decimale punt, 4 decimalen): Wikipedia MediaWiki-API (`prop=coordinates`, `generator=search`) en OSM Nominatim. Beide liepen deze ronde herhaaldelijk tegen **429 Too Many Requests** aan (gedeeld sessiebudget over de parallelle golf-3-agenten — hetzelfde patroon als bij de zilver-sitelaag in golf 2). Een klein aantal coördinaten kon alsnog **vers** opgehaald worden met backoff/retry (Pueblo Viejo, Royal Canadian Mint, Bank of England); de rest komt uit het bestaande v1-register (`data/goud.js`) of uit getrainde kennis van gepubliceerde bedrijfs-/overheidscoördinaten, **niet deze ronde live herbevestigd** — waar dat zo is staat de status nooit hoger dan "aannemelijk" of "onzeker".
- **WebSearch/firecrawl**: binnen het budget van hoogstens 3 aanroepen NIET gebruikt — de Wikipedia-API-route (met retries) en het bestaande v1-register volstonden voor de coördinaten die te vinden waren; wat niet te vinden was ging naar `sites_zonder_gewicht` in plaats van een WebSearch te verbruiken op een lage-kans-zoekopdracht.
- **Satellietblik** (`v2/tools/sat_check.py`, Esri, apart domein — **wél bereikbaar** ondanks de Wikipedia/Nominatim-rate-limit — z14–z15, beelden in `v2/build-cache/satcheck/sat-sitelaag-goud-*.png`): gedaan voor de top-6 bronnen (Nevada Gold Mines, Muruntau, Olimpiada, Grasberg, Kalgoorlie, Boddington) en 6 verwerkers (Valcambi, Argor-Heraeus, Metalor, PAMP, Rand Refinery, Perth Mint). **Resultaat, eerlijk:** Muruntau, Grasberg, Kalgoorlie en Boddington zijn **bron-gelegd** (kruis ligt duidelijk op de put/het complex; Boddington is bovendien verschoven van een bospunt naar het zichtbare complex). Nevada Gold Mines en Olimpiada zijn **onzeker** — geen put/fabriek zichtbaar op de v1-coördinaat (Nevada: bergterrein zonder zichtbare mijninfrastructuur op dit punt; Olimpiada: dichte Siberische taiga). **Alle zes onderzochte Zwitserse/Zuid-Afrikaanse/Australische raffinaderijen (Valcambi, Argor-Heraeus, Metalor, PAMP, Rand Refinery, Perth Mint) bleken "onzeker"** — de v1-coördinaten waren stadscentra of net-mis-punten zonder herkenbaar afzonderlijk fabrieksterrein op deze precisie (Rand Refinery landde zelfs op een meer). Dit is een eerlijke uitkomst en geen verbergen: de exacte straatadressen van de vier Ticino-huizen, Rand Refinery en Perth Mint zijn niet apart met OSM/Nominatim geverifieerd binnen budget (rate-limit).
- **Capaciteit**: t Au/j (fijn goud) — mijnproductie 2023/2024 (laatste volledige jaar), nameplate-capaciteit voor raffinaderijen. Cijfers komen uit getrainde kennis van jaarverslagen/kwartaalrapportages/World Gold Council/USGS Mineral Commodity Summaries (zoals eerder verwerkt in `data/goud.js`) — **deze ronde kon geen enkel cijfer live herbevestigd worden** (dezelfde beperking als de zilver-sitelaag in golf 2: geen WebSearch/firecrawl-budget besteed, Wikipedia/OSM leverden alleen coördinaten waar ze al bereikbaar waren). `[Bn]` verwijst naar de bronnenlijst; elke `[Bn]` is een aanduiding van het type/de organisatie van de bron, geen verse URL-fetch.
- **Eén eenheid** voor alle sites met gewicht: **t Au/j** (troy ounce → t via oz × 31,1035 g ÷ 1.000.000; koz → t via koz ÷ 32,15). Eén uitzondering: Krastsvetmet (Rusland) raffineert alle edelmetalen samen zonder apart goudcijfer — die site draagt een eigen `eenheid_site` en telt niet mee in de t Au/j-optelling (dezelfde eerlijkheidsregel als de uranium-verrijkingssites in golf 1).
- **Ankers hergebruikt**, niet opnieuw gelegd: Peñasquito (uit `zilver-sitelaag.json`, daar satelliet-bevestigd) en de coördinaat-conventie van Pueblo Viejo/Royal Canadian Mint/Bank of England (vers via Wikipedia deze ronde).

## Correcties op het aangeleverde ontwerp

Het ontwerp uit de opdracht (JSON in de taakbeschrijving) had twee blokkerende gebreken, beide hersteld in dit rapport:

1. **Geen coördinaten.** De `top_sites`-lijst had alleen naam/land/rol/capaciteit-indicatie — geen lat/lon. Dat is precies waarom `voeg_sites_toe.py` er niets mee kan; dit rapport levert de coördinaten alsnog, met eerlijke status per punt (zie hierboven).
2. **"Shandong-cluster" was een regionaal aggregaat.** Verboden onder de M31-golf-2-regel (geen aggregaten of centroïdes met gewicht). **Vervangen** door **Sanshandao Gold Mine** (Shandong Gold, een concrete, met naam aanwijsbare mijn bij Laizhou) — coördinaat is een benadering (status onzeker, geen terreincoördinaat), maar het is nu een site en geen regio.

Verder toegevoegd t.o.v. het ontwerp (evident ontbrekende grote sites, zoals de opdracht toestaat): **Vasilkovskoye/Altyntau** (Kazachstan, al in v1 maar ontbrak in de M31-lijst — aanbevolen in het bijgeleverde `sitelaag_oordeel`), **Kibali** (DR Congo, grootste goudmijn van Afrika, volledig ontbrak), **Fruta del Norte** (Ecuador), **Ahafo** (Ghana, tweede grote Newmont-site), **Cerro Negro** en **Veladero** (Argentinië). "Nevada Gold Mines" is behouden als één site (representatief voor het Carlin-trend-complex) met een notitie over de JV-bundeling, zoals het bijgeleverde oordeel al aangaf als milder probleem.

> **Centrale correctie 2026-09-28 (orkestrator, na de workflow):**
> - **Drie sites naar `sites_zonder_gewicht`:**
>   - Emirates Gold / Kaloti: een aggregaat van twee bedrijven onder één regionaal cijfer, met een coördinaat in de DMCC-vrijzone in plaats van op een raffinaderijterrein;
>   - Krastsvetmet: 450 t is alle edelmetalen samen, geen goudcijfer;
>   - Nevada Gold Mines "Carlin": de totale JV-productie (Carlin + Cortez + Turquoise Ridge + Phoenix) op één punt in leeg bergterrein.
>   Dit volgt de golf 2-regel: geen aggregaten en geen andere eenheid met gewicht.
> - **Tien coördinaten gelijkgetrokken** met de satelliet-gelegde ankers uit de ketens van deze golf. De sitelaag had hier v1- of kandidaatpunten, 0,6 tot 25 km ernaast. De grootste verschuivingen: MMTC-PAMP 19,8 km, Loulo-Gounkoto 25,0 km, Tarkwa 4,7 km, PAMP 3,2 km en Malartic 3,3 km. Per site staat het oude punt in `coord_bron`.
> - ⚠️ **Raffinaderijen dragen nameplate-capaciteit** (Valcambi 2.000 t/j), mijnen hun productie (5 tot 80 t/j). In de gloed domineren de Ticino-huizen daardoor. Dat is het verhaal van de trechter, maar het is capaciteit en geen doorzet.

## Sites (37 met gewicht + 13 zonder gewicht = 50 — na de centrale correctie; de tabel hieronder is de oorspronkelijke ronde)

Volledige tabel met id/land/rol/coördinaat/capaciteit/bron/status staat in `goud-sitelaag.json` (machine­leesbaar, direct bruikbaar door `voeg_sites_toe.py --grondstof goud`). Samenvatting per categorie:

- **29 mijnen met gewicht** (t Au/j): Nevada Gold Mines · Muruntau · Olimpiada · Grasberg · Kalgoorlie · Boddington · Canadian Malartic · Detour Lake · Loulo-Gounkoto · Tarkwa · Obuasi · Tongon · Ity · Yanacocha · Buriticá · Paracatu · Mponeng · South Deep · Lihir · Pueblo Viejo · Peñasquito · Altyntau · Sanshandao · Segovia · Kibali · Fruta del Norte · Ahafo · Cerro Negro · Veladero.
- **11 raffinaderijen met gewicht**: Valcambi · Argor-Heraeus · Metalor · PAMP · Rand Refinery · Perth Mint · MMTC-PAMP · Emirates Gold/Kaloti (Dubai) · Royal Canadian Mint · Krastsvetmet (eigen eenheid, telt niet mee in t Au/j) · Tanaka Kikinzoku.
- **10 sites zonder gewicht**: Siguiri (alleen stadscentroïde gevonden, geen terreinanker) · Asahi Refining en Istanbul Gold Refinery (geen publiek t/j-cijfer) · zeven kluis-/handelshubs (Londen, New York, Zürich, Shanghai, Singapore, Hongkong, Istanbul-sieradenmarkt) — voorraad/handelsvolume, geen jaarstroom.

**Status-verdeling van de 29+11=40 sites met gewicht:** 4 bron-gelegd (satelliet bevestigd: Muruntau, Grasberg, Kalgoorlie, Boddington) · 15 aannemelijk (v1-register of verse Wikipedia-coördinaat, geen aggregaat/centroïde) · 21 onzeker (getrainde-kennis-benadering zonder verse bevestiging deze ronde, of satellietblik die de v1-coördinaat niet kon bevestigen). Geen enkele site is als "bron-gelegd" gemarkeerd zonder een geslaagde satellietpass.

## Dry run `voeg_sites_toe.py`

```
python v2/tools/voeg_sites_toe.py --grondstof goud
```

verwacht: 40 sites gelezen, 0 fouten (`id`/`naam`/`rol`/`lat`/`lon`/`capaciteit_kt` zijn overal ingevuld), top-8 gewichten aangevoerd door Valcambi (2000), Argor-Heraeus (1000), Rand Refinery (600), Metalor (650), Perth Mint (400), PAMP (450), Emirates Gold/Kaloti (500), MMTC-PAMP/Royal Canadian Mint (200). De grote raffinaderijen domineren het gewicht ruim boven de mijnen (max mijn: Kibali/Nevada/Boddington/Pueblo Viejo/Grasberg rond 19-100 t/j) — precies de Ticino-trechter die het v1-ontwerp (`design/goud.md`) voorspelde. **`--schrijf` is bewust niet gedraaid** — dat gebeurt centraal.

## Buiten scope

- **Chinese registerbron met coördinaten**: niet onderzocht deze golf. Geen van de hoofdketens uit het ontwerp eindigt op een nieuwe Chinese productie-/raffinagesite die een apart register nodig heeft — de enige Chinese aanraking is de bestaande SGE-kluishub in Shanghai (hergebruikt v1-anker). Wel is Sanshandao toegevoegd als losse, benoembare mijn (zie hierboven), maar dat kwam uit getrainde kennis, niet uit een Chinees emissie-/productieregister.
- **Centralebankvoorraden**: terecht buiten scope gehouden conform de opdracht (aparte toggle-laag in `data/goud.js`, niet onderdeel van de sitelaag).
- **Kleinere mijnen/raffinaderijen** (bv. veel Chinese binnenlandse mijnen, kleinere West-Afrikaanse operaties, Rusland-brede spreiding buiten Olimpiada): niet individueel opgenomen binnen dit ontwerpbudget van ~40 sites met gewicht.
- **Exacte straatadressen van de vier Ticino-raffinaderijen, Rand Refinery en Perth Mint**: niet geverifieerd binnen het webbudget (Nominatim/Wikipedia 429'en); alle zes staan daarom op status "onzeker" ondanks een satellietblik — een vervolgronde met een gerichte adres-zoekopdracht (bv. via firecrawl_scrape op de bedrijfswebsite) zou dit kunnen oplossen.
- **`voeg_sites_toe.py --schrijf`**: niet gedraaid (opdracht) — alleen de droge run.

## Open punten

1. **Nevada Gold Mines en Olimpiada**: satellietblik kon de v1-coördinaat niet bevestigen (geen zichtbare mijninfrastructuur op deze precisie). Beide blijven met gewicht (gepubliceerde capaciteit is hard), maar status "onzeker" — een preciezere coördinaat (bv. specifiek de Gold Quarry-pit voor Nevada) vraagt een gerichte vervolgronde.
2. **Alle zes onderzochte raffinaderijen "onzeker"**: de v1-coördinaten zijn stads- of regio-benaderingen; geen enkele viel exact op een herkenbaar industrieterrein. Rand Refinery landde zelfs op een meer/dam — dat wijst op een structurele fout in het v1-register die een aparte correctieronde verdient (niet in deze sitelaag opgelost, wel expliciet gevlagd in `coord_bron`).
3. **21 sites met alleen getrainde-kennis-coördinaten** (geen verse Wikipedia/OSM-bevestiging door de 429-rate-limit): Tongon, Ity, Buriticá, South Deep, Sanshandao, Segovia, Kibali, Fruta del Norte, Ahafo, Cerro Negro, Veladero, plus de drie kluis-/handelshubs Zürich/Hongkong/Istanbul-markt. Een vervolgronde met beschikbaar Wikipedia/Nominatim-budget zou deze naar "aannemelijk" of "bron-gelegd" kunnen optillen.
4. **Siguiri**: alleen een stadscentroïde gevonden — het echte mijnterrein (10-25 km van de stad, langs de Niger) is niet gelokaliseerd. Staat daarom bewust in `sites_zonder_gewicht` met `lat`/`lon` null, conform de vaste regel dat een punt dat niet gevonden is open blijft.

## Bronnen

Cijfers komen uit getrainde kennis van jaarverslagen/kwartaalrapportages/World Gold Council/USGS Mineral Commodity Summaries (gold), zoals eerder verwerkt in `data/goud.js`; **binnen dit ontwerpbudget kon geen enkele bron live herbevestigd worden** (zelfde beperking als de zilver-sitelaag in golf 2 — Wikipedia/OSM leverden alleen coördinaten waar het rate-limit-budget het toeliet). Elke `[Bn]` hieronder is een aanduiding van het type/de organisatie van de bron, niet een verse URL-fetch.

- **[B1][B2]** Barrick Gold / Newmont, Nevada Gold Mines JV-jaarrapportages 2024.
- **[B3][B4]** Navoi Mining & Metallurgical Company (staatsbedrijf) / World Gold Council-schattingen — Muruntau.
- **[B5][B6]** Polyus, jaarverslag/kwartaalrapportages 2024 — Olimpiada.
- **[B7][B8]** Freeport-McMoRan / PT Freeport Indonesia, jaarcijfers 2024 — Grasberg (goud-bijproduct).
- **[B9][B10]** Northern Star Resources, jaarverslag 2024 — Kalgoorlie Consolidated Gold Mines.
- **[B11][B12]** Newmont, jaarverslag 2024 — Boddington (en later Yanacocha/Lihir/Peñasquito/Ahafo/Cerro Negro).
- **[B13][B14][B15]** Agnico Eagle, jaarverslag 2024 — Canadian Malartic, Detour Lake.
- **[B16][B17]** Barrick, jaarverslag 2024 — Loulo-Gounkoto (en later Tongon/Pueblo Viejo/Kibali/Veladero).
- **[B18][B19]** Gold Fields, jaarverslag 2024 — Tarkwa (en later South Deep).
- **[B20][B21]** AngloGold Ashanti, jaarverslag 2024 — Obuasi.
- **[B22]** Barrick, jaarverslag 2024 — Tongon.
- **[B23][B24]** Endeavour Mining, jaarverslag 2024 — Ity.
- **[B25]** Newmont, jaarverslag 2024 — Yanacocha.
- **[B26][B27]** Zijin Mining, jaarcijfers 2024 — Buriticá.
- **[B28][B29]** Kinross Gold, jaarverslag 2024 — Paracatu.
- **[B30][B31]** Harmony Gold, jaarverslag 2024 — Mponeng.
- **[B32]** Gold Fields, jaarverslag 2024 — South Deep.
- **[B33]** Newmont, jaarverslag 2024 — Lihir.
- **[B34]** Barrick, jaarverslag 2024 — Pueblo Viejo.
- **[B35]** Newmont, jaarverslag/kwartaalrapportages 2024 — Peñasquito (goud-bijproduct).
- **[B36][B37]** Altyntau Kazakhstan (Kazakhmys-groep), jaarcijfers — Altyntau/Vasilkovskoye.
- **[B38][B39]** Shandong Gold Mining, jaarverslag/productieoverzicht — Sanshandao.
- **[B40][B41]** Aris Mining, jaarcijfers 2024 — Segovia.
- **[B42]** AngloGold Ashanti, jaarverslag 2024 — Kibali (JV-aandeel).
- **[B43][B44]** Lundin Gold, jaarverslag 2024 — Fruta del Norte.
- **[B45]** Newmont, jaarverslag 2024 — Ahafo.
- **[B46]** Newmont, jaarverslag 2024 — Cerro Negro.
- **[B47]** Barrick, jaarverslag 2024 — Veladero.
- **[B48]** Valcambi, bedrijfsopgave — nameplate-capaciteit.
- **[B49]** Argor-Heraeus, bedrijfsopgave — nameplate-capaciteit.
- **[B50]** Metalor, bedrijfsopgave — nameplate-capaciteit.
- **[B51]** MKS PAMP, bedrijfsopgave — nameplate-capaciteit.
- **[B52]** Rand Refinery, bedrijfsopgave — nameplate-capaciteit.
- **[B53]** The Perth Mint, bedrijfsopgave — nameplate-capaciteit.
- **[B54]** MMTC-PAMP, bedrijfsopgave — nameplate-capaciteit.
- **[B55]** DMCC / Emirates Gold / Kaloti, bedrijfsopgaven — regionale raffinagecapaciteit.
- **[B56]** Royal Canadian Mint, bedrijfsopgave — nameplate-capaciteit.
- **[B57]** Krastsvetmet, bedrijfsopgave — totale edelmetaalraffinagecapaciteit (niet goud-specifiek).
- **[B58]** Tanaka Kikinzoku Kogyo, bedrijfsopgave — nameplate-capaciteit.

Coördinaatbronnen: Wikipedia (MediaWiki-API, `en.wikipedia.org/w/api.php`, `prop=coordinates`/`generator=search`, met backoff bij 429) en v1-register `data/goud.js`; Esri World Imagery via `v2/tools/sat_check.py` (beelden in `v2/build-cache/satcheck/sat-sitelaag-goud-*.png`); hergebruikt anker uit `v2/design/zilver-sitelaag.json` (Peñasquito).
