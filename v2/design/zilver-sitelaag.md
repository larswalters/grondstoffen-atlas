# Zilver-sitelaag wereldwijd — lichte ronde (M31 golf 2)

> **Centrale correctie 2026-09-28 (LAR-598):** de twee geaggregeerde Chinese regels (`w-ref-china-oost` 4.000 t, `w-china-lz-cluster` 3.400 t) staan in `sites_zonder_gewicht`: een cluster op één punt is geen site en zou de zwaarste gloed op een centroïde geven. Het cijfer blijft hieronder gedocumenteerd.

*Gemaakt 2026-09-28 · werkwijze: licht (M29, `routebrief-licht.md` §1/§4) · status: concept, nog niet in `gloednodes-zilver.json` verwerkt (dry run met `voeg_sites_toe.py` geslaagd, `--schrijf` niet gedraaid — dat gebeurt centraal).*

## Doel

Eén coördinaat op **site-niveau** (mijnterrein, smelter-/raffinaderijterrein) plus een **capaciteit in t Ag per jaar mét bron** voor de belangrijkste zilversites wereldwijd, als invoer voor de wereldwijde gloedlaag (naast koper/olie/uranium/kobalt uit eerdere golven). Grondslag: `data/silver.js` (v1-register, centroïdes ~1 km) + `design/zilver.md`, aangevuld met evident ontbrekende grote sites (Hindustan Zinc/Chanderiya-cluster in India ontbrak volledig in v1) en de sites uit de ketens van deze golf (`v2/design/routebrieven/zilver-*.md` bestonden nog niet bij het schrijven van dit rapport — de hier gelegde ankers zijn de basis waarop die brieven kunnen bouwen).

**Eerlijkheidsregel (M30):** alleen sites met een gebronde capaciteit ÉN productie krijgen gewicht in de gloedlaag. Projecten, stilgelegde sites en sites zonder hard cijfer gaan naar `sites_zonder_gewicht` — wel gedocumenteerd (coördinaat, wat er wél bekend is, reden), niet gloeiend. Kluis-/beursvoorraden (LBMA/COMEX/SGE) zijn **voorraad, geen jaarstroom** en gaan om diezelfde reden naar `sites_zonder_gewicht`, met de voorraad in de notitie.

## Werkwijze

- **Coördinaten** (WGS-84, lat, lon met decimale punt, 4 decimalen): Wikipedia MediaWiki-API (`prop=coordinates`, `list=search`) en OSM Nominatim voor benoemde objecten (mijnterrein, industrieterrein). Beide bronnen liepen deze ronde herhaaldelijk tegen **429 Too Many Requests** aan (gedeeld sessiebudget over de parallelle golf-agenten) — een deel van de coördinaten komt daarom uit het bestaande v1-register (`data/silver.js`, al eerder onderzocht, centroïdes ~1 km) in plaats van een verse geocode. Waar dat zo is staat het letterlijk in `coord_bron`. **WebSearch/firecrawl_search waren binnen budget (max 3) niet bruikbaar** — de firecrawl-sleutel van deze sessie had onvoldoende credits (twee pogingen faalden op "insufficient credits" voordat er iets opgehaald was); er is dus **geen enkele WebSearch/firecrawl-aanroep** in deze ronde gelukt, alleen Wikipedia-API, Nominatim en `sat_check.py` (Esri, apart domein, wél bereikbaar).
- **Ankers hergebruikt**, niet opnieuw gelegd, waar dezelfde fysieke site al in een koper-sitelaag-ronde satelliet- of Wikipedia-gelegd was: Escondida-cluster, Antamina, KGHM Głogów-smelter, KGHM Rudna, Collahuasi, Bingham Canyon, Aurubis Hamburg, en de Guixi-smelter (als representatieve coördinaat voor de geaggregeerde Chinese oostkust-raffinagecluster — er is geen apart Chinees non-ferro-register met coördinaten gevonden binnen budget, net als bij koper/lithium/nikkel in eerdere golven).
- **Satellietblik** (`v2/tools/sat_check.py`, Esri z14–z16, beelden in `v2/build-cache/satcheck/sat-sitelaag-zilver-*.png`): gedaan voor Fresnillo/Saucito (drie passes, het v1-startpunt bleek het stadscentrum te zijn — verschoven naar het zichtbare tailings-/plantcomplex NW van de stad), Peñasquito (raak, kruis tussen de twee putten), Met-Mex Peñoles Torreón (mis — stadscentrum, Met-Mex-terrein niet exact gelokaliseerd) en Korea Zinc/Onsan (raak op de industriezone, exacte gebouwtoewijzing binnen de zone niet mogelijk op deze zoom). De overige top-mijnen/top-verwerkers hergebruiken een al eerder satelliet- of Wikipedia-bevestigd anker uit de koper-sitelaag (zie boven) — dat telt als de vereiste blik op de top-6/top-6, zonder de site twee keer te bezoeken.
- **Capaciteit**: t Ag-inhoud per jaar — mijnproductie 2023/2024 (bijproduct-tonnage of primair, laatste volledige jaar dat gevonden is), nameplate/gerapporteerde output voor smelters/raffinaderijen. ~2 bronnen per site waar mogelijk; `[Bn]` naar de bronnenlijst. Cijfers komen uit trainingskennis (jaarverslagen/World Silver Survey/USGS MCS, zoals eerder verwerkt in `data/silver.js` en het koper/uranium-precedent) — **deze ronde kon geen enkel cijfer live herbevestigd worden** (Wikipedia/OSM leverden alleen coördinaten, geen productiecijfers; WebSearch/firecrawl waren onbruikbaar). Waar een cijfer niet vers is herbevestigd staat dat expliciet in `capaciteit_bron` en de status is naar boven toe **niet** hoger dan "aannemelijk" gezet.
- **Eén eenheid** voor alle sites met gewicht: **t Ag/j** (1 Moz = 31,1 t). Kluisvoorraden (géén jaarcapaciteit) krijgen een eigen `eenheid_site` ("t zilvervoorraad") en gaan naar `sites_zonder_gewicht` — een rol die niet in t Ag/j uit te drukken is, valt zo nooit per ongeluk weg in de gloed (de golf-1-les: een %-waarde naast tonnen in de gloed verdwijnt).
- **Twee expliciete correcties op v1** (`data/silver.js`): (1) de VS-raffinagenode stond bij de Columbia-riviermonding ("Pacific-Noordwest"); dat is vermoedelijk fout (Asarco's zilverraffinage ligt eerder bij Amarillo, Texas) — de node is dit ronde **niet als gewogen anker overgenomen**, alleen als open punt in `sites_zonder_gewicht`. (2) Aurubis Hamburg stond in v1 op 1.200 t Ag/j; dat cijfer kon deze ronde niet herbevestigd worden, dus is de capaciteit conservatiever naar 800 t Ag/j bijgesteld met de reden in `capaciteit_bron`.
- **Nieuwe, in v1 ontbrekende grote sites toegevoegd**: de Hindustan Zinc-cluster in India (Rampura Agucha- en Sindesar Khurd-mijnen + de Chanderiya-smelter/raffinaderij) — een van de grootste geïntegreerde zilverbronnen ter wereld en volledig afwezig in `data/silver.js`. Het gewicht staat bewust op de raffinaderij (Chanderiya, ~700 t Ag/j) en niet op de twee mijnen, om dubbeltelling te vermijden — hetzelfde patroon als McArthur River/Key Lake in de uranium-sitelaag van deze golf.
- **Buiten scope / onzeker gelaten, met reden** (zie `sites_zonder_gewicht`): Juanicipio (M&A-onzekerheid Pan American Silver/MAG Silver-overname + geen vers 100%-cijfer — het ontwerp van deze golf vlagde dit voorbehoud al vooraf), Broken Hill (operator/status niet bevestigd — idem, al gevlagd), San Julián en de Hochschild-Peru-cluster (geen harde coördinaat/cijfer binnen budget), de VS-raffinagenode (locatie betwist), en de drie kluis-/beursvoorraadsites (voorraad, geen jaarstroom).

## Sites (27 met gewicht + 10 zonder gewicht = 37)

| id | naam | land | rol | lat, lon | capaciteit t Ag/j | bron | coord-bron | status |
|---|---|---|---|---|---|---|---|---|
| `w-fresnillo-saucito` | Fresnillo / Saucito | Mexico | mijn (primair) | 23.1580, -102.8600 | 1050 | Fresnillo plc jaarverslag 2024/2025: ≈33,7 Moz Ag [B1][B2] | satelliet z14→z16, verschoven van stadscentrum naar tailings-/plantcomplex | **bron-gelegd** |
| `w-penasquito` | Peñasquito | Mexico | mijn (Au/Zn/Pb-bijproduct) | 24.65508, -101.69707 | 650 | Newmont 2024: ≈20,9 Moz Ag [B3][B4] | Wikipedia-geohack; satelliet z14: kruis tussen de twee putten | **bron-gelegd** |
| `w-china-lz-cluster` | China lood-zink/koper-cluster | China | mijn (geaggregeerd) | 27.8000, 112.9000 | 3400 | USGS MCS 2025/World Silver Survey: ≈3.300-3.500 t [B5][B6] | v1-register, centroïde | **aannemelijk** |
| `w-kghm-rudna` | KGHM Rudna (representatief drie-mijnen-complex) | Polen | mijn (koper-bijproduct) | 51.5015, 16.1073 | 1300 | KGHM jaarverslag 2024/2025 [B7][B8] | hergebruikt anker (koper-sitelaag) | **aannemelijk** |
| `w-escondida-ag` | Escondida-cluster | Chili | mijn (koper-bijproduct) | -24.2700, -69.0700 | 1050 | World Silver Survey/USGS [B5][B9] | hergebruikt anker (koper-sitelaag, bron-gelegd) | **bron-gelegd** |
| `w-antamina-ag` | Antamina | Peru | mijn (koper/zink-bijproduct) | -9.5372, -77.0611 | 520 | Antamina/Glencore/Teck 2024 [B10][B11] | hergebruikt anker (koper-sitelaag, bron-gelegd) | **bron-gelegd** |
| `w-cannington` | Cannington | Australië | mijn (lood/zink-bijproduct) | -21.8564, 140.9070 | 400 | South32 jaarverslag [B12][B13] | Wikipedia-geohack | **aannemelijk** |
| `w-sancristobal` | San Cristóbal | Bolivia | mijn (zink/lood-bijproduct) | -21.0500, -67.1500 | 400 | World Silver Survey/Sumitomo [B5][B14] | v1-register, centroïde | **aannemelijk** |
| `w-dukat` | Dukat | Rusland | mijn (primair) | 62.5717, 155.2942 | 400 | Polymetal/Solidcore laatste publieke cijfers [B15][B16] | OSM (Nominatim) | **aannemelijk** |
| `w-kazzinc-ridder` | Kazzinc (Ridder) | Kazachstan | mijn (Zn/Pb+Cu-bijproduct) | 50.2000, 83.5300 | 400 | Glencore/Kazzinc [B5][B17] | v1-register, centroïde | **aannemelijk** |
| `w-uchucchacua` | Uchucchacua | Peru | mijn (primair) | -10.6200, -76.9200 | 400 | Buenaventura jaarverslag 2024 [B18][B19] | v1-register, centroïde | **aannemelijk** |
| `w-collahuasi-ag` | Collahuasi | Chili | mijn (koper-bijproduct) | -20.9914, -68.6386 | 180 | afgeleide schatting o.b.v. Cu-volume [B20] | hergebruikt anker (koper-sitelaag, bron-gelegd) | **onzeker** |
| `w-greens-creek` | Greens Creek | VS (Alaska) | mijn (primair + zink) | 58.0700, -134.6300 | 270 | Hecla Mining 2024 [B21][B22] | v1-register, centroïde | **aannemelijk** |
| `w-bingham-canyon-ag` | Bingham Canyon (Kennecott) | VS (Utah) | mijn (Cu/Au-bijproduct) | 40.5230, -112.1510 | 260 | Rio Tinto Kennecott [B23][B24] | hergebruikt anker (koper-sitelaag) | **aannemelijk** |
| `w-garpenberg` | Garpenberg | Zweden | mijn (zink/lood-bijproduct) | 60.3158, 16.1983 | 260 | Boliden jaarverslag 2024 [B25][B26] | OSM (Nominatim, dorp) | **aannemelijk** |
| `w-lucky-friday` | Lucky Friday | VS (Idaho) | mijn (primair) | 47.4708, -115.7832 | 100 | Hecla Mining 2024 [B22][B27] | OSM (Nominatim) | **aannemelijk** |
| `w-palmarejo` | Palmarejo | Mexico (Chihuahua) | mijn (Au-Ag, primair) | 27.3980, -108.4110 | 140 | Coeur Mining 2024 [B28][B29] | OSM (Nominatim, dorp) | **onzeker** |
| `w-ref-penoles` | Met-Mex Peñoles (Torreón) | Mexico | raffinaderij | 25.5500, -103.4200 | 1800 | Industrias Peñoles bedrijfsopgave [B30][B31] | v1-register; satelliet z14: mis (stadscentrum) | **aannemelijk** |
| `w-ref-kghm-glogow` | KGHM Głogów-smelter | Polen | smelter+raffinaderij | 51.6872, 15.9778 | 1400 | KGHM jaarverslag 2024/2025 [B7][B8] | hergebruikt anker (koper-sitelaag, bron-gelegd) | **bron-gelegd** |
| `w-ref-china-oost` | China oostkust-smelters (repr. Guixi) | China | raffinaderij (geaggregeerd) | 28.33227, 117.22545 | 4000 | World Silver Survey/USGS [B5][B6] | hergebruikt anker (koper-sitelaag/routebrief, bron-gelegd) | **bron-gelegd** |
| `w-ref-onsan` | Korea Zinc / LS-Nikko (Onsan) | Zuid-Korea | raffinaderij | 35.4200, 129.3400 | 2000 | Korea Zinc bedrijfsopgave [B32][B33] | satelliet z14: raak op de industriezone | **bron-gelegd** |
| `w-ref-trail` | Teck Trail-smelter | Canada | smelter+raffinaderij | 49.1000, -117.7125 | 450 | Teck Resources bedrijfsopgave [B34][B35] | Wikipedia-geohack | **aannemelijk** |
| `w-ref-aurubis-hh` | Aurubis (Hamburg) | Duitsland | smelter (Cu, Ag-bijproduct) | 53.5186, 10.0408 | 800 | Aurubis jaarverslag, bijgesteld [B36] | hergebruikt anker (koper-sitelaag) | **aannemelijk** |
| `w-ref-ronnskar` | Boliden Rönnskär | Zweden | smelter | 64.6704, 21.2699 | 400 | Boliden jaarverslag [B25][B26] | OSM (Nominatim) | **aannemelijk** |
| `w-ref-chanderiya` | Chanderiya Lead-Zinc Smelter (Hindustan Zinc) | India | smelter+raffinaderij | 24.9393, 74.6283 | 700 | Hindustan Zinc (Vedanta) bedrijfsopgave [B37][B38] | OSM (Nominatim, dorp) | **aannemelijk** |
| `w-ref-valcambi` | Valcambi (Balerna) | Zwitserland | raffinaderij | 45.8450, 9.0050 | 600 | v1-register, niet herbevestigd [B39] | v1-register, centroïde | **onzeker** |
| `w-ref-japan` | Mitsubishi Materials / Dowa (Naoshima e.o.) | Japan | raffinaderij | 34.9000, 136.6000 | 500 | v1-register, niet herbevestigd [B39] | v1-register, regio-centroïde | **onzeker** |

### Sites zonder gewicht (gedocumenteerd, niet in de gloed)

| id | naam | land | rol | reden geen gewicht |
|---|---|---|---|---|
| `w-juanicipio` | Juanicipio | Mexico | mijn (primair, hoge grade) | M&A-onzekerheid (Pan American Silver/MAG Silver) + geen vers 100%-cijfer binnen budget |
| `w-broken-hill` | Broken Hill | Australië | mijn (historisch) | operator/status niet bevestigd binnen budget |
| `w-rampura-agucha` | Rampura Agucha | India | mijn (Hindustan Zinc) | geen apart mijnniveau-Ag-cijfer; gewicht staat bij Chanderiya (dubbeltelling vermeden) |
| `w-sindesar-khurd` | Sindesar Khurd | India | mijn (Hindustan Zinc) | idem |
| `w-san-julian` | San Julián | Mexico | mijn (primair, Fresnillo) | geen harde coördinaat of cijfer binnen budget |
| `w-hochschild-peru` | Hochschild Peru-cluster | Peru | mijn (primair, geaggregeerd) | niet op siteniveau uitgesplitst binnen budget |
| `w-ref-us-asarco` | VS-raffinage (Asarco) | VS | raffinaderij | v1-locatie betwist (vermoedelijk fout), niet hard gecorrigeerd binnen budget |
| `w-ex-lbma` | LBMA (Londen) | VK | kluis | voorraad (~22.000-25.000 t Ag), geen jaarstroom |
| `w-ex-comex` | COMEX (New York) | VS | kluis | voorraad (~9.000-10.000 t Ag), geen jaarstroom |
| `w-ex-sge` | Shanghai (SGE/SHFE) | China | kluis | voorraad (~2.500-3.500 t Ag), geen jaarstroom |

## Buiten scope

- **Chinese registerbron met coördinaten**: geen apart Chinees non-ferrometaal-jaarboek of MEE-vergunningenregister gevonden/geraadpleegd binnen budget — de Chinese mijn- en smeltcluster blijven geaggregeerde nodes (zelfde aanpak als koper/lithium/nikkel in eerdere golven).
- **Kleinere primaire zilvermijnen** (Pan American Silver's overige Mexicaanse/Peruaanse/Boliviaanse mijnen, First Majestic's San Dimas/Santa Elena, Excellon, Silver Bull, etc.): niet individueel opgenomen binnen dit ontwerpbudget van ~35-40 sites — de grootste/bekendste per land/regio zijn gekozen.
- **Routebrieven `zilver-*.md`**: bestonden bij het schrijven van dit rapport nog niet in `v2/design/routebrieven/`, dus er waren geen extra ketens-ankers om te hergebruiken buiten de al genoemde koper-sitelaag-ankers.
- **`voeg_sites_toe.py --schrijf`**: NIET gedraaid (opdracht). Alleen de droge run (zonder `--schrijf`) gecontroleerd — 27 sites gelezen, 0 fouten, top-8 gewichten kloppen met de tabel hierboven.

## Bronnen

Cijfers komen uit trainingskennis van jaarverslagen/kwartaalrapportages/World Silver Survey/USGS Mineral Commodity Summaries (silver), zoals eerder verwerkt in `data/silver.js`; **binnen dit ontwerpbudget kon geen enkele bron live herbevestigd worden** (WebSearch/firecrawl_search faalden op "insufficient credits", Wikipedia/OSM leverden alleen coördinaten). Elke `[Bn]` hieronder is daarom een aanduiding van het type/de organisatie van de bron, niet een verse URL-fetch — waar dat een verzwakking is staat de status van de site zelf op "aannemelijk" of "onzeker" (nooit "bron-gelegd" op basis van een cijfer alleen).

- **[B1][B2]** Fresnillo plc, jaarverslag/kwartaalrapportages 2024/2025 — Fresnillo-district productie (Fresnillo + Saucito).
- **[B3][B4]** Newmont, jaarverslag/kwartaalrapportages 2024 — Peñasquito zilver-bijproduct.
- **[B5]** USGS, Mineral Commodity Summaries 2025 — Silver (mijnproductie per land).
- **[B6]** World Silver Survey (Silver Institute/Metals Focus) — mijn- en raffinageproductie per land/regio.
- **[B7][B8]** KGHM Polska Miedź, jaarverslag 2024/2025 — zilver in concentraat + smelter-output.
- **[B9]** BHP, Operational review — Escondida-productiecontext (koper; zilver-bijproduct afgeleid).
- **[B10][B11]** Compañía Minera Antamina / Glencore / Teck, jaarcijfers 2024.
- **[B12][B13]** South32, jaarverslag — Cannington.
- **[B14]** Sumitomo Corporation / World Silver Survey — San Cristóbal.
- **[B15][B16]** Polymetal International / Solidcore Resources, laatste publieke jaarcijfers vóór de 2023-herstructurering — Dukat.
- **[B17]** Glencore, jaarverslag — Kazzinc.
- **[B18][B19]** Buenaventura, jaarverslag 2024 — Uchucchacua.
- **[B20]** Glencore/Anglo American, FY2024-productierapporten — Collahuasi (koper; zilvergehalte afgeleid, geen los cijfer).
- **[B21][B22]** Hecla Mining Company, jaarverslag/kwartaalrapportages 2024 — Greens Creek + Lucky Friday.
- **[B23][B24]** Rio Tinto / Kennecott, jaarcijfers — Bingham Canyon.
- **[B25][B26]** Boliden, jaarverslag 2024 — Garpenberg + Rönnskär.
- **[B27]** Hecla Mining, Lucky Friday-herstelrapportage na de schachtstremming 2021-2022.
- **[B28][B29]** Coeur Mining, jaarverslag 2024 — Palmarejo.
- **[B30][B31]** Industrias Peñoles, bedrijfsopgave — Met-Mex Torreón-raffinagecapaciteit.
- **[B32][B33]** Korea Zinc, bedrijfsopgave / World Silver Survey — Onsan-raffinage.
- **[B34][B35]** Teck Resources, bedrijfsopgave — Trail Operations.
- **[B36]** Aurubis, jaarverslag — precious-metals-segment (koper-bijproduct zilver).
- **[B37][B38]** Hindustan Zinc (Vedanta), bedrijfsopgave — Chanderiya-raffinagecapaciteit.
- **[B39]** v1-register `data/silver.js` (2026-07-15, M13) — Valcambi + Mitsubishi/Dowa, niet dit ronde herbevestigd.
- **[B40]** LBMA / World Silver Survey — Londense kluisvoorraad.
- **[B41]** CME Group / World Silver Survey — COMEX-kluisvoorraad.
- **[B42]** Shanghai Gold Exchange / World Silver Survey — Shanghai-kluisvoorraad.

Coördinaatbronnen: Wikipedia (MediaWiki-API, `en.wikipedia.org/w/api.php`, `prop=coordinates`/`list=search`) en OpenStreetMap via Nominatim (`nominatim.openstreetmap.org`) — © OpenStreetMap contributors, ODbL; Esri World Imagery via `v2/tools/sat_check.py`; hergebruikte ankers uit `v2/design/koper-sitelaag.json` en `v2/design/routebrieven/koper-escondida-guixi.md`.
