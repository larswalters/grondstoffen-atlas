# Routebrief (licht) · diamant — Mirny → Moskou → Mumbai (India)

**stroom-id:** `diamant-mirny-mumbai` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** Russische ruwe diamant uit het Mir/Udachny-cluster (Alrosa, Sacha-republiek) gaat per truck van de mijn/sorteercentrum naar Mirny Airport (MJZ), vliegt als vrachtvlucht (grootcirkel) naar Sheremetyevo (SVO, Alrosa's eigen verkooporganisatie in Moskou), vliegt door naar Chhatrapati Shivaji Maharaj Intl (BOM, Mumbai) en gaat per truck naar de Bharat Diamond Bourse (BKC) — de sanctie-omweg om de G7-markt heen: niet-G7-bestemde rough hoeft niet via het Antwerpse traceerbaarheidsnode.
**Welke as van het verhaal:** *Rusland (Alrosa/Jakoetië) → Moskou → Mumbai: de sanctie-omweg om de G7-markt heen.* Sinds 1 september 2024 moet G7-bestemde rough via het Antwerpse G7-certificeringsnode (blockchain-traceerbaarheid, ≥0,5 ct); rough die voor beneficiation/verwerking in een niet-G7-land is bestemd is daarvan vrijgesteld [12]. India (en Dubai) blijven Russische diamant importeren [13]; deze as bestaat zolang de VS/EU/VK-eindmarkt de Indiase gepolijste re-export niet zelf blokkeert. Alrosa's nettowinst daalde 77% in 2024 (RUB 19,3 mrd tegen 85,2 mrd, omzet −26%) door de sancties en een zwakke markt [13].

## 1 · Ketenkaart
```
Alrosa Mirny — mijn/sorteercentrum `dia-mirny-mijn` ──(b1 truck · stadsverbinding Mirny · ~2,2 km)──►
Mirny Airport (MJZ) `dia-mirny-mjz` ──(b2 lucht · vlucht MJZ → SVO, grootcirkel · ~4.150 km)──►
Sheremetyevo-Cargo (SVO), Moskou `dia-svo-cargo` ──(b3 lucht · vlucht SVO → BOM, grootcirkel · ~5.049 km)──►
CSMIA Air Cargo Complex (BOM), Mumbai `dia-bom-cargo` ──(b4 truck · Airport Road/BKC-connector · ~3,9 km)──►
Bharat Diamond Bourse (BKC) `dia-bdb` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Mirny-mijn/sorteercentrum → Mirny Airport (MJZ) | stadsweg binnen Mirny (Alrosa-bedrijfsstad); geen doorgaande corridorkeuze | ~2,2 hemelsbreed (berekend uit ankers); ontwerp noemt ~3 km wegafstand [ontwerp] | maak_stroombeen_weg | nee |
| b2 | A | lucht | Mirny Airport (MJZ) → Sheremetyevo-Cargo (SVO) | vlucht MJZ → SVO, grootcirkel | 4.150,4 (berekend, grootcirkel) | maak_luchtbeen | nee — doorgetrokken |
| b3 | B | lucht | Sheremetyevo-Cargo (SVO) → CSMIA Air Cargo Complex (BOM) | vlucht SVO → BOM, grootcirkel | 5.049,0 (berekend, grootcirkel) | maak_luchtbeen | nee — doorgetrokken |
| b4 | C | truck | CSMIA Air Cargo Complex (BOM) → Bharat Diamond Bourse (BKC) | Airport Road → Western Express Highway/BKC-connector, binnen Mumbai (<15 km, geen corridorkeuze) | ~3,9 hemelsbreed (berekend uit ankers) | maak_stroombeen_weg | nee |

Fase C is toegevoegd op de haalbaarheidstoets: de keten mag niet eindigen op de luchthaven zelf zonder het laatste been naar de beurs (§ regel truckbeen vrachtterminal→beurs/kluis). `dia-bdb` is het bestaande Mumbai-anker uit de andere ketens van deze golf (Bandra-Kurla Complex) — hergebruikt, niet opnieuw gelegd.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-mirny-mijn` | mijn / laadplek (sorteercentrum) | Mir-mijn / Alrosa mijnbouw- en verwerkingscomplex, Mirny | 62.5258, 113.9842 | [6][7][14] | bron-gelegd (z15 gezien: rand van de open put met direct aangrenzend een industrieel gebouwencluster en toegangswegen — het Mirny-mijncomplex; géén apart sorteergebouw op deze resolutie te onderscheiden, zie §7) |
| `dia-mirny-mjz` | vrachtterminal / vertrek luchtvracht | Mirny Airport (MJZ), thuisbasis Alrosa Mirny Air Enterprise | 62.5344, 114.0222 | [6][14] | bron-gelegd (z14 gezien: luchthaventerminal + bijgebouwen/platform direct aan de start-/landingsbaan; klein regionaal vliegveld, geen aparte vrachtloods te onderscheiden — Alrosa's eigen luchtvaartdochter is hier gevestigd) |
| `dia-svo-cargo` | vrachtterminal / aankomst+vertrek luchtvracht | Sheremetyevo-Cargo (Терминал «Шереметьево-Карго»), Moskou | 55.9696, 37.4362 | [8][11][14] | bron-gelegd (z15 gezien: apart vrachtgebouw ten zuiden van het passagiersapron, met vrachtvliegtuigen op het platform ernaast — OSM `building=transportation`, naam "Терминал Шереметьево-Карго") |
| `dia-bom-cargo` | vrachtterminal / aankomst luchtvracht | CSMIA Air Cargo Complex, Sahar, Mumbai | 19.0994, 72.8673 | [9][11][14] | bron-gelegd (z15 gezien: gebouwencluster net ten noorden van de start-/landingsbaan, bij de OSM-POI "C.S.I. Airport Cargo Complex Parking"; individuele vrachttoestellen op deze resolutie niet scherp te onderscheiden) |
| `dia-bdb` | beursgebouw / bestemming | Bharat Diamond Bourse, G Block, Bandra-Kurla Complex, Mumbai | 19.0641, 72.8646 | [10][11][14] | bron-gelegd (z15 gezien: herkenbaar torencomplex aan de rivierbocht in BKC, exact op de OSM-landuse-polygoon "Bharat Diamond Bourse"; hergebruikt uit een eerdere keten van deze golf) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
*(geen — b1 en b4 zijn beide korte stadsverbindingen (<4 km) zonder aanwijsbare corridorkeuze; de weg-tool routeert zelf over het lokale net.)*

## 5 · Verwerkingsknopen
*(geen — deze keten kent geen smelter/raffinaderij; Mirny is winning + sortering, Sheremetyevo is Alrosa's verkooporganisatie (geen fysieke bewerking), Bharat Diamond Bourse is een beurs-/exportgebouw, geen slijperij. Het slijpen (~90-95% van de wereld in Surat, ~250 km zuidelijk van Mumbai) valt buiten deze keten — zie § stoppunt.)*

## 6 · Stoppunt
De brief stopt bij de Bharat Diamond Bourse: dit is precies het punt dat de haalbaarheidstoets vraagt (truckbeen vrachtterminal → beurs), en er is voor déze specifieke stroom geen bron die een vervolgbeen (bv. naar een Surat-slijperij) aan Mirny-rough koppelt — fase D vervalt.

## 7 · Open punten
- **Geen apart sorteergebouw gevonden voor Mirny**: het anker `dia-mirny-mijn` combineert winning en sortering op het mijncomplex; Alrosa's exacte lokale sorteer-/verpakkingslocatie (vóór transport naar het vliegveld) is niet als apart adres gebrond.
- **Mirny-specifiek aandeel niet uitgesplitst**: Alrosa's totaalvolume (~35 Mct/j, ~30% wereldvolume) is niet apart naar Mirny/Mir- vs. Udachny-cluster verdeeld (bevestigd open punt uit het ketenontwerp).
- **Geen gepubliceerde vluchtlengte**: MJZ→SVO en SVO→BOM zijn berekende grootcirkels (er bestaat geen gekarteerd luchtwegennet); de werkelijke vluchtroute kan door omvliegen langer zijn.
- **Aandeel via Dubai vs. direct India niet per lading gebrond**: de risico-tekst en eerdere ketens (§4a van `design/diamant.md`) noemen beide routes; dat Mirny-rough specifiek via Moskou→Mumbai gaat (i.p.v. via Dubai) is aannemelijk uit Alrosa's eigen Moskou-verkooporganisatie, niet per zending bevestigd.
- **CSMIA-vrachtcomplex-anker** is op OSM-POI-niveau gelegd (parking van het complex); het exacte vrachtgebouw/platform kon op z15 niet los van de bebouwing onderscheiden worden.
- **BDB is een beurs/exportgebouw, geen slijperij**: de rough die hier binnenkomt gaat vermoedelijk door naar Surat om geslepen te worden (buiten deze keten, zie §6).

## 8 · Bronnen
[1] Forbes India, 2024 — "Diamonds in the Rough: G7 ban on Russian-origin diamonds will reflect heavily on Indian exports". https://www.forbesindia.com/article/news/diamonds-in-the-rough-g7-ban-on-russianorigin-diamonds-will-reflect-heavily-on-indian-exports/90321/1
[2] Gulf News, 2024 — "As Russian diamonds face heavier sanctions, is it all advantage Antwerp?". https://gulfnews.com/business/analysis/as-russian-diamonds-face-heavier-sanctions-is-it-all-advantage-antwerp-1.1708941910026
[3] GJEPC (Gem & Jewellery Export Promotion Council, India). https://www.gjepc.org
[4] Alrosa, officiële site. https://www.alrosa.ru/en
[5] `v2/design/diamant.md` (project-brief) §3a (jaarvolume Alrosa), §4a (luchtvracht-bron Mirny→Moskou→India).
[6] Wikipedia — "Mirny Airport" (MJZ, 62.5344/114.0222; thuisbasis Alrosa Mirny Air Enterprise). https://en.wikipedia.org/wiki/Mirny_Airport
[7] Wikipedia — "Mir mine" (62.5258/113.9842, open put Mirny, sinds 2009 ondergronds actief). https://en.wikipedia.org/wiki/Mir_mine
[8] Wikipedia — "Sheremetyevo International Airport" (55.9728/37.4147, passagiersterminals; het Cargo-gebouw ligt noordelijker, zie [11]). https://en.wikipedia.org/wiki/Sheremetyevo_International_Airport
[9] Wikipedia — "Chhatrapati Shivaji Maharaj International Airport" (BOM, 19.0886/72.8681). https://en.wikipedia.org/wiki/Chhatrapati_Shivaji_Maharaj_International_Airport
[10] Wikipedia — "Bharat Diamond Bourse" (G Block, Bandra-Kurla Complex; handelt 98% van de Indiase diamantexport). https://en.wikipedia.org/wiki/Bharat_Diamond_Bourse
[11] OpenStreetMap (ODbL) via Photon — "Терминал «Шереметьево-Карго»" (building=transportation, 55.96955/37.43619); "C.S.I. Airport Cargo Complex Parking" (19.09940/72.86726); "Bharat Diamond Bourse" (landuse=commercial-polygon, centroïde 19.06410/72.86458). https://photon.komoot.io
[12] AWDC (Antwerp World Diamond Centre) — "G7/EU sanctions FAQ": Antwerpen als eerste G7-importnode vanaf 1 september 2024 (≥0,5 ct), beneficiation-rough voor niet-G7-landen vrijgesteld. https://www.awdc.be/g7eu-sanctions-faq
[13] Rapaport, 2025 — "Alrosa's Profit Plunges 77% for the Full Year"; RUB 19,3 → 85,2 mrd, omzet −26%; India/Dubai blijven Russische rough importeren, het maart-2024-verbod sloot de derde-land-route naar het Westen. https://rapaport.com/news/alrosas-profit-plunges-77-for-the-full-year/
[14] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15, live) — `v2/build-cache/satcheck/sat-diamant-mirny-mumbai-mir-mine.png`, `-mjz-airport.png`, `-svo-cargo.png`, `-bom-cargo.png`, `-bdb.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `diamant-mirny-mumbai`** → `v2/data/stroomroute-diamant-mirny-mumbai.json` — 4 benen (2 truck, 2 lucht),
**9.211,4 km**, 666 punten, 5 markers, 14,4 KB. Recept: `bak_stromen.sh` (functie `bak_diamant_mirny_mumbai`);
twee nieuwe wegprofielen (`diamant-mirny-mumbai-mijn-mjz`, `diamant-mirny-mumbai-bom-bdb`) in
`maak_stroombeen_weg.py`; twee luchtbenen met `maak_luchtbeen.py` — **de eerste lucht-bake van dit project**,
letterlijk volgens `bakhandleiding-licht.md` §2 "Lucht". Geen zeebeen, geen haven-aanloop, geen stippel.

**b1 (truck, nieuw profiel `diamant-mirny-mumbai-mijn-mjz`, extract `rusland-verrehoosten`, vensterKm 15):**
`maak_stroombeen_weg.py --profiel diamant-mirny-mumbai-mijn-mjz --bron geofabrik` — **3,5 km** geroute (getekende
lijn 3,6 km incl. anker-verbindingsstukjes) over de stadswegen van Mirny (Alrosa-bedrijfsstad), geen via-punten
(geen corridorkeuze binnen de stad). Anker-verbindingsstukjes plant → weg 0,01 km en weg → kade 0,07 km (beide
OK). Doorgetrokken (geen stippel).

**b2 (lucht, `maak_luchtbeen.py`):** MJZ (62,5344/114,0222) → SVO (55,9696/37,4362) — **4.150,4 km** grootcirkel,
168 punten. Doorgetrokken; komt exact overeen met de brief-schatting (4.150,4 km).

**b3 (lucht, `maak_luchtbeen.py`):** SVO (55,9696/37,4362) → BOM (19,0994/72,8673) — **5.049,0 km** grootcirkel,
203 punten. Doorgetrokken; komt exact overeen met de brief-schatting (5.049,0 km).

**b4 (truck, nieuw profiel `diamant-mirny-mumbai-bom-bdb`, extract `india`, vensterKm 15):**
`maak_stroombeen_weg.py --profiel diamant-mirny-mumbai-bom-bdb --bron geofabrik` — **8,3 km** geroute (getekende
lijn 8,4 km incl. anker-verbindingsstukjes) over Airport Road/Western Express Highway-verbindingswegen in Mumbai,
geen via-punten (geen corridorkeuze binnen de stad). Anker-verbindingsstukjes plant → weg 0,03 km en weg → kade
0,06 km (beide OK). 7 kleine keerlussen gesnoeid (dubbel gereden stukjes bij kruispunten, 0,1 km totaal).
Doorgetrokken (geen stippel).

**⚠️ Lengtetoets BUITEN de norm op beide truckbenen — bevinding, geen fout:** de brief geeft voor b1 en b4 alleen
een **hemelsbreed**-schatting uit de ankers (~2,2 resp. ~3,9 km), geen gepubliceerde wegkm. b1: 3,5 km tegen ~2,2
km hemelsbreed = **+59,1%**; tegen de indicatieve ~3 km wegschatting uit het ontwerp = **+16,7%** (net buiten
±15%). b4: 8,3 km tegen ~3,9 km hemelsbreed = **+114%**. Beide zijn de gemeten stadswegroute rond gebouwen/
kruispunten in een dichtbebouwde bedrijfsstad (Mirny) resp. luchthavenzone (Sahar/BKC) — een hemelsbreed-getal is
per definitie geen wegtoets en een router die om gebouwen heen rijdt is per constructie langer. Geen via-punt
bijgeschoven om het getal te halen (conform de norm).

**Toetsen:** `toets_knikken.py` — b1: 8 knikken ≥60° (7 spikes + 1 echte scherpe bocht bij het mijnterrein,
R 9 m); b4: 16 knikken ≥60° (allemaal spikes bij Mumbai-kruispunten, R 4–39 m); beide luchtbenen 0 knikken.
**Totaal 24 knikken, 1 omkering ≥150° (de scherpe bocht bij b1, geen terugloop), 0 terugloop** over de hele
stroom — geen actie nodig. `toets_rechte_benen.py --min-km 5` — geen melding voor deze stroom (beide luchtbenen
worden per constructie overgeslagen — ze zijn grootcirkels; beide truckbenen zijn geen rechte lijn, omwegfactor
> 1,000). `json.load` slaagt: versie 2, `punt_formaat` lonlat, modaliteiten `truck`/`lucht` ∈ toegestane set, elk
been ≥ 2 punten (68–227), bestandsgrootte 14,4 KB (ruim onder ~300 KB). Naden tussen alle vier opeenvolgende
benen: **0,000 km** (elk been begint exact waar het vorige eindigt — dezelfde ankercoördinaat, geen snap-gat).
Markers: alle 5 op ≤ 0,1 m van hun been (exact op het ankerpunt).

**Toelichting stippels/haven-aanlopen/vluchten:** geen stippel in deze keten. **Twee vluchten**, beide
doorgetrokken grootcirkels tussen satelliet-gelegde vrachtterminals (bron: geen bron noemt een tussenlanding/hub
voor Mirny-rough, dus één directe vlucht per etappe — de aanname staat al in brief §7). Geen haven-aanloop nodig:
er zit geen zeebeen in deze keten (Rusland → Moskou → Mumbai gaat volledig over truck + lucht).

**Gereedschapslessen:** de eerste lucht-bake bevestigt `bakhandleiding-licht.md` §2 letterlijk — `maak_luchtbeen.py`
gaf op beide etappes exact de km uit de brief (grootcirkel is per definitie de bron, dus geen afwijking mogelijk),
en `hecht_marnet.py route` nam de vier `--been-geojson`-vlaggen in reisvolgorde over zonder verdere routering
(modaliteit `lucht` werd zonder waarschuwing herkend). Geen nieuwe tool-issues; het enige aandachtspunt is dat een
hemelsbreed-schatting bij een korte stadsrit ruim binnen ±15% kan uitvallen (zoals hierboven) — dat is een
eigenschap van de toetswaarde, niet van het gereedschap.
