# Routebrief (licht) · diamant — Dubai (DMCC) → DXB → Ben Gurion (TLV) → Ramat Gan (Verenigde Arabische Emiraten → Israël)

**stroom-id:** `diamant-dubai-ramatgan` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** ruwe diamant (rough) van de Dubai Diamond Exchange (DMCC, Almas Tower, JLT) per truck naar de DXB-vrachtterminal,
als vrachtvlucht (grootcirkel DXB → TLV, **aannemelijk: handelsstroom gebrond, vlucht niet**) naar de Maman Cargo Terminal van Ben Gurion, en
per truck (stippel, geen Israel-extract) naar de Israel Diamond Exchange in Ramat Gan — de Golf-tak die de Israel-lus sluit.
**Welke as van het verhaal:** *Dubai-rough → Israëlische slijpers*. Gedocumenteerd is de **waarde**: de VAE leverden in 2021 voor
**244 mln USD** aan rough aan Israël (**11,8%** van de Israëlische rough-invoer) [1]. Een karaatcijfer voor deze boog is **niet gevonden**; de v1-atlas
heeft de boog `dia-dubai → dia-ramat-gan` niet (alleen `dia-antwerp → dia-ramat-gan`, 2 Mct/j) [5]. Context: Israël importeerde in 2025 in totaal
3,71 Mct (669,8 mln USD, Kimberley-Process-cijfer, rough/polished niet gesplitst) [2]. Eenheid Mct/j = miljoen karaat per jaar; de waarde per
karaat is hier niet in het gewicht verwerkt.

## 1 · Ketenkaart
```
DMCC / Almas Tower `dia-dmcc-almas` ──(b1 truck · Sheikh Zayed Road E11 → Airport Road · letterlijke kopie diamant-dubai-surat b1 · 31,2 km)──►
DXB-vrachtterminal (Cargo Village) `dia-dxb-vracht` ──(b2 lucht · vlucht DXB → TLV, grootcirkel, aannemelijk · 2.126,6 km)──►
Maman Cargo Terminal, Ben Gurion `dia-tlv-cargo` ──(b3 truck · stippel last mile, geen net · omgekeerde kopie diamant-ramatgan-newyork b1 · 13,6 km)──►
Israel Diamond Exchange, Diamond Tower, Ramat Gan `dia-ide` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | DMCC/Almas Tower → DXB-vrachtterminal | Sheikh Zayed Road (E11) → Airport Road; **letterlijke kopie** (GEEN omkering: het bestand loopt al DMCC → DXB) van `diamant-dubai-surat` b1 | hemelsbreed 29,0 km, geen wegkm (gebakken kopie 31,2 km; eerder +7,6% ten opzichte van hemelsbreed als indicatie) [8] | kopie geojson | nee |
| b2 | B | lucht | DXB-vrachtterminal → Maman Cargo Terminal (TLV) | vlucht DXB → TLV (vrachtvlucht, grootcirkel), aannemelijk: handelsstroom gebrond, vlucht niet | 2.126,6 grootcirkel [berekend, `maak_luchtbeen`, 87 punten] | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | Maman Cargo Terminal → Israel Diamond Exchange | geen corridor: last mile zonder net (Israel-extract ontbreekt); **omgekeerde kopie** van de stippel in `diamant-ramatgan-newyork` b1 | hemelsbreed 13,6 km, geen wegkm [berekend] | `--stippel` | ja — hier reikt het net niet |

Geen zeebeen (dus geen haven-aanloop), geen leiding, geen spoor. Het DXB-wegbeen eindigt 0,22 km van het anker op de openbare weg: geen
extra airside-stippel nodig (zoals in `diamant-dubai-surat`). Het TLV-anker ligt aan de landzijde (truckparking/laaddocks): geen airside-stippel.
De ±15%-toets geldt voor b1 en b3 niet als norm: alleen hemelsbreed, geen echte wegkm.

## 3 · Ankers (één per site en per overslag — alle vier HERGEBRUIKT, niet opnieuw gelegd)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-dmcc-almas` | handelshub / vertrek | DMCC/Dubai Diamond Exchange, Almas Tower, JLT | 25.0689, 55.1412 | [3][8] (`diamant-dubai-surat`) | bron-gelegd (daar z15 gezien: 68-verdiepingentoren in het JLT-hoogbouwcluster aan de Sheikh Zayed Road) |
| `dia-dxb-vracht` | overslag truck → lucht | DXB Cargo Village / SkyCargo-loodsen, Al Garhoud | 25.2574524, 55.3405972 | [8] (`diamant-dubai-surat`, `-mbujimayi-dubai`) | bron-gelegd (daar z15 gezien: rij vrachtloodsen en apron NW van de terminals) |
| `dia-tlv-cargo` | overslag lucht → truck | Maman Cargo Terminal, Ben Gurion Airport (TLV), Lod | 31.9949, 34.9019 | [9] (`diamant-ramatgan-newyork`) | bron-gelegd op terminalniveau (daar z17 gezien: groot loodsgebouw, truckparking oostzijde); welk pand diamant afhandelt: onzeker |
| `dia-ide` | beursgebouw + slijpersdistrict / bestemming | Israel Diamond Exchange, Diamond Tower, Ramat Gan | 32.0836, 34.8024 | [9] (`diamant-ramatgan-newyork`; Wikipedia 32.08357/34.80236) | bron-gelegd (daar z16 gezien: hoogbouwcluster van het Bourse-district) |

Alle vier de ankers staan al satelliet-gelegd in de genoemde zusterbrieven (`v2/build-cache/satcheck/sat-diamant-dubai-surat-{dmcc-almas,dxb-vracht}.png`,
`sat-diamant-ramatgan-newyork-{ide,tlv-maman-z17}.png`); niets verschoven, daarom geen nieuwe check.

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | — | geen | — | één doorgaande stadsweg, letterlijke kopie; geen nieuw profiel |
| b3 | — | geen | — | stippel, geen routering |
Geofabrik-regio's: geen (b1 `gcc-staten` is al gebakken; b3 heeft geen extract: Israël ontbreekt, bakhandleiding §3).

## 5 · Verwerkingsknopen
Geen fysieke bewerking onderweg: DMCC is veiling/handel; de Maman-terminal is overslag, beveiliging en douane [4]. Het slijpen gebeurt ná het stoppunt in Ramat Gan.

## 6 · Stoppunt
De brief stopt bij de Israel Diamond Exchange: handels- en slijperijdistrict, het eindpunt uit het ketenontwerp; geen bron koppelt déze lading
aan één slijperij — fase D en E vervallen.

## 7 · Open punten
- **Geen bron voor een vrachtvlucht DXB → TLV met rough.** Gebrond is de handelsstroom (244 mln USD, 11,8% in 2021 [1]), dat de DMCC sinds
  14 december 2022 een kantoor in het IDE-hoofdkantoor heeft en dat dagelijkse directe vluchten Dubai en Tel Aviv verbinden [3], en dat
  diamant als beveiligde vracht op lijnvluchten gaat [6]. Calcalist 2018: toen nog geen directe vluchten (via een derde land) — verouderd [7]. Tussenlanding niet gebrond:
  één directe vlucht aangenomen; de grootcirkel loopt over Saoedi-Arabië en Jordanië en is schematisch.
- **Oorlog 2026:** na het begin van het Iran-conflict (1 maart 2026) werden vluchten naar de VAE geannuleerd en sloot de IDE-handelsvloer; de DMCC werkte
  op afstand [2b]. De kaart toont de vaste vorm, niet de tijdelijke ontregeling; de huidige route is onbekend.
- **Volume:** geen karaatcijfer voor het UAE-aandeel; het ketenontwerp noemde "ca. 2 Mct/j (v1)", maar dat getal hoort in v1 bij `dia-antwerp → dia-ramat-gan`, niet bij Dubai.
  Centraal te kiezen: een natte-vinger-gewicht of alleen de dollarwaarde tonen.
- **b3 is schematisch:** 13,6 km hemelsbreed, geen wegkm. Optioneel centraal: Israel-extract toevoegen (`fetch_landnet.py`), dan wordt b3 een wegbeen.
- **Sitelaag:** `w-ramatgan` in `diamant-sitelaag.json` staat op 32.084/34.81, ca. 0,7 km van `dia-ide` (aannemelijk uit trainingskennis); centraal gelijktrekken.
- De 2021-cijfers zijn waarde in USD en rough; het 2025-cijfer (3,71 Mct) is een totaal zonder splitsing; geen UAE-aandeel in carats gevonden.
- Antwerpen is waarschijnlijk de grotere rough-bron voor Israël (zie `dia-antwerp → dia-ramat-gan`); niet apart onderzocht.

## 8 · Bronnen
[1] Israel Diamond Institute, "Israel axes tariffs UAE" (7 juni 2022): UAE 244 mln USD, 11,8% van Israëls rough-invoer 2021; Israëls rough-export naar de VAE 188 mln USD. https://en.israelidiamond.co.il/news/israel/israel-axes-tariffs-uae/
[2] TheGlobalEconomy.com (Kimberley Process), Israel diamond imports 2025: 3.708.102 ct, 669,83 mln USD; exports 2.002.626 ct, 579,45 mln USD. https://www.theglobaleconomy.com/Israel/diamond_exports_carats/
[2b] Rapaport, "Iran War Disrupts Diamond Trade in Dubai, Israel" (1-2 maart 2026): vluchtannuleringen naar de VAE, tenders uitgesteld, IDE-handelsvloer dicht. https://rapaport.com/news/iran-war-disrupts-diamond-trade-in-dubai-israel/
[3] DMCC, "Dubai's DMCC opens representative office in Tel Aviv" (14 dec 2022): kantoor in het IDE-hoofdkantoor, eerste directe commerciële vlucht Dubai–Tel Aviv, dagelijkse vluchten. https://dmcc.ae/latest-news/dubais-dmcc-opens-representative-office-tel-aviv-boost-israeli-trade-through-uae
[4] Maman Group, "Maman Cargo Terminal" (Ben Gurion; kluizen en beveiligde begeleiding). https://en.maman-group.co.il/companies/maman-cargo-terminal/
[5] v1 `data/diamond.js` + `design/diamant.md` §4 (flows `dia-antwerp → dia-ramat-gan` 2 Mct, `dia-ramat-gan → dia-ny` 2 Mct; geen Dubai → Ramat Gan) — intern.
[6] Israel Diamond Institute, "Transports of diamonds in the world" (diamant als vracht op lijnvluchten, beveiligingsbedrijven laden bij het vliegtuig). https://en.israelidiamond.co.il/diamond-articles/diamonds/transports-diamonds-world/
[7] Calcalist, 27-11-2018, "Diamond Trade Binds Israel and the UAE Together" (toen geen directe vluchten). https://www.calcalistech.com/ctech/articles/0,7340,L-3750800,00.html
[8] Brieven `diamant-dubai-surat` (ankers + b1-kopie) en `-mbujimayi-dubai`; bestand `v2/build-cache/ais/graaf/diamant-dubai-surat-weg-dmcc-dxb.geojson` (406 punten, 31,2 km).
[9] Brief `diamant-ramatgan-newyork` (ankers `dia-ide`, `dia-tlv-cargo`; stippel b1) + Wikipedia, "Israel Diamond Exchange". https://en.wikipedia.org/wiki/Israel_Diamond_Exchange
[10] DMCC/Dubai Diamond Exchange en IDE, samenwerkingsovereenkomst (17 sept 2020): wederzijdse kantoren in Almas Tower en Ramat Gan. https://mediaoffice.ae/en/news/2020/september/17-09/dubai-diamond-exchange-and-israel-diamond-exchange-sign-landmark-agreement

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
**Bestand:** `v2/data/stroomroute-diamant-dubai-ramatgan.json` (11,1 KB, versie 2, lonlat) · functie `bak_diamant_dubai_ramatgan` in `v2/tools/bak_stromen.sh` · titel: Diamant · Dubai (DMCC) → DXB → Ben Gurion (TLV) → Ramat Gan.
**Recept:** geen profiel, geen wegscan, geen zee. b1 en b2 en b3 zijn kopieën of een luchtbeen; `hecht_marnet.py route` stikt ze.

| # | modaliteit | km | punten | naad | opmerking |
|---|---|---|---|---|---|
| b1 | truck | 31,2 | 406 | — | letterlijke kopie `diamant-dubai-surat-weg-dmcc-dxb.geojson` (niet omgekeerd); hemelsbreed 29,0 km, geen wegkm |
| b2 | lucht | 2.126,6 | 87 | 0,00 | doorgetrokken grootcirkel DXB → TLV (`maak_luchtbeen.py`) |
| b3 | truck (stippel) | 13,6 | 2 | 0,00 | rechte last-mile-stippel, geen Israel-extract |
Totaal **2.171,4 km**, 3 benen, 4 markers (`dia-dmcc-almas`, `dia-dxb-vracht`, `dia-tlv-cargo`, `dia-ide`), naden 0,00 km, markers 0,00-0,02 km van hun lijn.

**Toelichting.**
- *Stippel b3:* uitsluitend "hier reikt het net niet" (bakhandleiding §3: Israël ontbreekt). Omgekeerde kopie van de stippel in `diamant-ramatgan-newyork` b1; centraal werk als Israel-extract komt.
- *Vlucht b2:* aannemelijk (handelsstroom gebrond, vlucht niet), staat in de beennaam; doorgetrokken. Geen tussenlanding; de Iran-oorlog van 2026 is niet verwerkt.
- *Geen haven-aanloop, geen airside-stippel:* b1 eindigt 0,22 km van het DXB-anker op de openbare weg; het TLV-anker ligt landzijde.
- *km-toets:* niet van toepassing als norm (alleen hemelsbreed); b1 +7,6% ten opzichte van hemelsbreed als indicatie.

**Lessen / bevindingen.**
- `toets_knikken.py` meldt 6 knikken >= 60 graden op b1, alle in de bochten van de gedeelde DMCC-kopie (JLT-aansluiting en Al Garhoud-aanloop, 5-55 m straal), 0 omkeringen en 0 terugloop; dit is de bestaande kopie uit `diamant-dubai-surat`, ongewijzigd gelaten.
- `toets_rechte_benen.py`: alleen de stippel b3 (omwegfactor 1,000, met reden).
- Open voor centraal: volume (geen karaatcijfer, ontwerp-getal 2 Mct/j hoort bij Antwerpen), sitelaag `w-ramatgan` 0,7 km van `dia-ide`, registerregel (sleutel `dia-dr`).
