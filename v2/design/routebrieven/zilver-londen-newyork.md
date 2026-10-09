# Routebrief (licht) · zilver — Londen (LBMA-kluis, proxy) → Londen Heathrow → New York JFK (VK → VS)

**stroom-id:** `zilver-londen-newyork` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) ·
**status:** gebakken
**Keten in één zin:** good-delivery zilverbaren (1.000-oz) uit een Londense LBMA-kluis (proxy: Bank of England, City) per truck
via de A4/M4 naar het Heathrow World Cargo Centre, als belly-vracht op passagiersvluchten (grootcirkel LHR → JFK) naar de
vrachtterminal van JFK (New York). Eindpunt = JFK-vrachtterminal: het COMEX-depot is niet door een bron genoemd (§6, §7).
**Welke as van het verhaal:** de COMEX-arbitrage-aanvoer, een **momentopname** (nov 2024–feb 2025): ~45 Moz (≈1.400 t Ag)
stroomde sinds de VS-verkiezingsdag de COMEX-depots in, uit alle herkomsten tezamen, het Londense/vliegdeel onbekend [1].
Geen jaarvolume; zilver gaat normaal per schip, de vlucht is "highly unusual" en gedreven door een prijsverschil > $1/oz [1].
In okt. 2025 liep de richting om (New York → Londen, vrachtvluchten) [2] — de stroom is dus omkeerbaar en episodisch.

## 1 · Ketenkaart
```
LBMA-kluis Londen (proxy: Bank of England) `ag-hub-london`
  ──(b1 truck · A4/M4 City → Heathrow · kopie, omgekeerd · 35,5 km gebakken)──►
Heathrow World Cargo Centre (LHR) `ag-lhr-cargo`
  ──(b2 lucht · vlucht LHR → JFK, belly-vracht, grootcirkel, aannemelijk · 5.539,7 km)──►
JFK South Cargo Area (JFK) `ag-jfk-cargo` ── stoppunt (COMEX-depot niet gevonden)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | Bank of England (kluis-proxy) → Heathrow World Cargo Centre | M4/A4: Fleet St → Hyde Park Corner → Hammersmith → Chiswick → M4 J4 — **letterlijke kopie, omgekeerd** van `goud-valcambi-londen-weg-lhr-boe` (= `zilver-valcambi-londen` b3) | **hemelsbreed 26,6 km, geen wegkm**; gebakken 35,5 (OSM-weggeometrie, ontwerp 25 was eigen kaartlezing) [8][9] | geen nieuwe scan: omgedraaid exemplaar `zilver-londen-newyork-weg-boe-lhr.geojson` (1.321 punten) | nee |
| b2 | D | lucht | LHR-vrachtterminal → JFK-vrachtterminal | vlucht LHR → JFK, belly-vracht op **commerciële passagiersvluchten**, grootcirkel — **aannemelijk: één bron, luchthavens niet in de bron genoemd** [1] | 5.539,7 (grootcirkel op de twee ankers, getest) | maak_luchtbeen | nee — doorgetrokken |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-hub-london` | LBMA-kluis (proxy) | Bank of England, Threadneedle Street, City of London — **letterlijk hergebruik** uit `zilver-valcambi-londen.md` | 51.5139, -0.0883 | [8][9] | bron-gelegd als locatie; **als zilverkluis onzeker** (BoE is een goudkluis, zilver ligt vooral bij HSBC/JPMorgan/Brink's/Loomis/Malca-Amit). z15 gezien (nu): dicht City-weefsel, kruis op het Bank-kruispunt |
| `ag-lhr-cargo` | vrachtterminal / vertrek lucht | Heathrow World Cargo Centre / IAG Cargo, zuid van de noordbaan — **letterlijk hergebruik** uit `zilver-valcambi-londen.md` | 51.4605, -0.4629 | [8][9] | bron-gelegd. z15 gezien: groot loodsgebouw met platform direct ten zuiden van de rolbaan, cargo-complex langs de Bath Road/Cargo Tunnel-zijde, vrachtvliegtuigen op het apron |
| `ag-jfk-cargo` | vrachtterminal / aankomst lucht | JFK South Cargo Area (Cargo Plaza/South Cargo Road), Queens — **letterlijk hergebruik** = `dia-jfk-cargo` = `pgm-jfk-cargo` | 40.6587, -73.7952 | [6][7] | bron-gelegd. z15 gezien (nu): rij loodsen en apron met geparkeerde wide-body toestellen tussen Van Wyck-zijde en de rolbanen, kruis op de vrachtstrook |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Geen nieuwe via-punten: b1 is een letterlijke kopie van de bestaande, gebakken geometrie (via-punten in
`goud-valcambi-londen.md` §4: M4 J4/J4b · Chiswick · Hammersmith · Hyde Park Corner · Fleet Street). Geen wegscan, geen profiel.

## 5 · Verwerkingsknopen
Geen. Geen overslag onderweg behalve de twee vrachtterminals (ankers §3); geen kade, geen haven-aanloop, geen spoor, geen leiding.

## 6 · Stoppunt
De keten stopt bij de JFK-vrachtterminal: geen bron noemt het COMEX-depot, de vault-operator of het truckbedrijf ("trucks collected them in
New York, drivers generally didn't know what they were hauling" [1]); de kandidaten uit het ontwerp (Brink's, HSBC, JPMorgan, Loomis, MTB)
zijn eigen kennis, geen bron — dus geen depotanker en geen eindbeen JFK → depot (zou een verzonnen coördinaat zijn). Fase E vervalt.

## 7 · Open punten
- **COMEX-depot onbekend** — CME-depotenlijst is niet gevonden/gelezen binnen het webbudget; het depot wordt pas getekend als een bron
  deze lading aan een adres koppelt. Dan volgt een eindbeen JFK → depot (Van Wyck/Belt Pkwy of via Manhattan), eigen brief/golf.
- **Luchthavens zijn aannames:** [1] noemt alleen "commercial passenger flights from London to New York" (belly-cargo); LHR en JFK zijn de
  grootste vrachtparen maar EWR/LGA/Gatwick zijn niet uitgesloten; geen bron noemt carrier, vluchtnummers of tussenlanding (dus één directe vlucht).
- **Episodisch en omkeerbaar:** momentopname nov 2024–feb 2025 [1]; richting omgekeerd in okt. 2025 [2]. Het Londense aandeel van de ~45 Moz is
  onbekend; v1 had 1.500 t LBMA → COMEX per schip (`data/silver.js`, geen waarheid). Geen jaarvolume gevonden.
- **Kluisanker is een proxy** (zelfde als `zilver-valcambi-londen`); alternatief zonder proxy = keten laten starten bij `ag-lhr-cargo` (niet gekozen).
- **Wegkilometers b1:** geen gepubliceerde wegkm (ontwerp 25 km = kaartlezing); bij hemelsbreed 26,6 km is 35,5 km gebakken plausibel
  (omweg via M4 J4 en 4,1 km kleine wegen in de cargozone), de ±15%-toets is hier alleen indicatie.
- **[2] is een zwakke bron** (JPost-doorgeefartikel, byline PR, geen carrier/volume): alleen gebruikt voor "de richting kantelde".
- Jaarvolume-eenheid: 45 Moz × 31,1 = ≈1.400 t Ag in ~3 maanden, alle herkomsten (geen t Ag/j).

## 8 · Bronnen
[1] SupplyChainBrain (Bloomberg), 2025-02-03 — "Traders Load US-Bound Planes With Gold and Silver in Tariff Bet": zilverbaren in verzegelde houten kisten op commerciële passagiersvluchten Londen → New York, 1.000-oz-baren gelijk in Londen en COMEX, ~45 Moz naar COMEX-depots sinds de verkiezingsdag, trucks halen op, geen luchthaven/carrier/depot genoemd. https://www.supplychainbrain.com/articles/41138-traders-load-us-bound-planes-with-gold-and-silver-in-tariff-bet
[2] Jerusalem Post, 2025-10-12 (doorgeefartikel, zwakke bron) — vrachtvliegtuigen verplaatsen zilver van New York naar Londen. https://www.jpost.com/business-and-innovation/precious-metals/article-870270
[3] WebSearch-webcheck 2026-10-09 — geen enkele bron noemt JFK, vluchten of COMEX-vaults; secundaire sites geven Bloomberg door (okt. 2025: omgekeerde richting).
[4] CME Group, zilver — depotenlijst niet gelezen (URL niet geverifieerd): https://www.cmegroup.com/trading/metals/silver/
[5] v1 `data/silver.js` (ag-ex-lbma → ag-ex-comex 1.500, ship, geen waarheid) en `design/zilver.md`.
[6] Wikipedia, "John F. Kennedy International Airport" — 40.63972/-73.77889. https://en.wikipedia.org/wiki/John_F._Kennedy_International_Airport
[7] `v2/design/routebrieven/diamant-mumbai-newyork.md` en `pgm-amandelbult-iselin.md` — anker JFK South Cargo Area 40.6587/-73.7952 (OSM Cargo Plaza & Central Cargo Road 40.65875/-73.79520), satelliet-gelegd.
[8] `v2/design/routebrieven/zilver-valcambi-londen.md` (anker-bron [6][7][8] daar: Wikipedia Heathrow 51.4775/-0.46139; OSM/Photon IAG Cargo 51.46048/-0.46293; Wikipedia Bank of England 51.51389/-0.08833).
[9] `v2/design/routebrieven/goud-valcambi-londen.md` §9 — gebakken b3 35,5 km, 1.321 punten, bestand `goud-valcambi-londen-weg-lhr-boe.geojson`.
Satellietblik: `v2/build-cache/satcheck/sat-zilver-londen-newyork-jfk-cargo.png`, `-lhr-cargo.png`, `-boe.png` (Esri z15, 2026-10-09).
Hemelsbreed (haversine, R 6371,0088): BoE–LHR-terminal 26,6 km; LHR–JFK 5.539,7 km (= maak_luchtbeen).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Bestand:** `v2/data/stroomroute-zilver-londen-newyork.json` (31,1 KB, versie 2, `lonlat`) · functie `bak_zilver_londen_newyork()` in `v2/tools/bak_stromen.sh`
· recept: `bash v2/tools/bak_stromen.sh zilver-londen-newyork` (geen PROFIELEN-sleutel, geen extract, geen wegscan).

| # | modaliteit | been | km gebakken | punten | naad |
|---|---|---|---|---|---|
| b1 | truck | Bank of England, City of London → Heathrow World Cargo Centre (M4/A4; letterlijke kopie, omgekeerd, van `goud-valcambi-londen-weg-lhr-boe`) | 35,5 | 1.321 | — |
| b2 | lucht | vlucht LHR → JFK (belly-vracht op passagiersvluchten, grootcirkel; aannemelijk: één bron) | 5.539,7 | 223 | 0,000 km |

Totaal 5.575,2 km · 1.544 punten · 3 markers (`ag-hub-london`, `ag-lhr-cargo`, `ag-jfk-cargo`, alle 0,0 km van de lijn). Beide benen doorgetrokken, 0 stippels,
0 haven-aanlopen (geen zeebeen), geen extracts.

**Toelichting**
- **b1:** geen nieuwe scan. Het omgedraaide exemplaar `v2/build-cache/ais/graaf/zilver-londen-newyork-weg-boe-lhr.geojson` is de coördinatenlijst van het goud-origineel
  in omgekeerde volgorde (eerste punt -0,0883/51,5139, laatste -0,4629/51,4605); het origineel is niet aangeraakt. Geen gepubliceerde wegkm (hemelsbreed 26,6 km, geen wegkm):
  de ±15%-toets is alleen indicatie; 35,5 km is +33% op hemelsbreed (M4-omweg via J4 en cargozone-wegen), ontwerp 25 km was kaartlezing. Toets_knikken: 13 spikes
  (<= 92 gr, 3-29 m) in het stadsdeel, 0 omkeringen, 0 terugloop — dezelfde als bij de goud-/zilver-valcambi-kopie, geen reparatie.
- **b2:** `python v2/tools/maak_luchtbeen.py --van "LHR cargo|51.4605,-0.4629" --naar "JFK cargo|40.6587,-73.7952" --uit …/zilver-londen-newyork-lucht-lhr-jfk.geojson`
  → 5.539,7 km grootcirkel, 223 punten, doorgetrokken (geen stippel: een vlucht tussen twee gelegde terminals is geen gat). Aannemelijk: [1] noemt alleen
  "commercial passenger flights from London to New York"; LHR en JFK zijn aannames (§7), de lijnstijl blijft doorgetrokken, de aanname staat in de beennaam.
- **Geen stippel / aanloop:** JFK is het eindpunt van het luchtbeen (geen truckbeen erna, dus geen airside-last-mile); geen zeebeen, dus geen haven-aanloop; geen spoor/leiding/binnenvaart.
- **Stoppunt:** JFK-vrachtterminal (COMEX-depot door geen bron genoemd, §6).
- Registerregel (centraal): sleutel `ag-ln` (vrij; niet in het register).

**Lessen:** (1) de slot-snippet uit de taakomschrijving gebruikt `rm -rf "$d"` met variabelen en wordt door de veiligheidscheck van Claude Code geweigerd;
`rm -f "$d/sinds"; rmdir "$d"` doet hetzelfde zonder die weigering. (2) Een omgekeerde kopie van een bestaand geojson is genoeg voor `--been-geojson`; hecht_marnet routeert
zo'n "vooraf gebakken lijn" niet opnieuw, dus de km blijven exact die van het origineel.
