# Routebrief (licht) · diamant — Dubai (DMCC) → DXB → JFK → New York (VAE → VS)

**stroom-id:** `diamant-dubai-newyork` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) ·
**status:** gebakken
**Keten in één zin:** diamant van de Dubai Diamond Exchange (DMCC, Almas Tower, JLT) per truck naar de DXB-vrachtterminal, als vrachtvlucht (grootcirkel DXB → JFK, **aannemelijk: handelsstroom gebrond, vlucht niet**) naar de South Cargo Area van JFK en per truck via Van Wyck en de Queens-Midtown Tunnel naar de 47th Street Diamond Exchange in Manhattan.
**Welke as van het verhaal:** *Dubai → VS: de grootste eindmarkt vanuit de Golf-hub* — VAE-export HS 7102 in 2023 naar de VS 1,66 mld USD = 8,61% van 19,3 mld, vierde bestemming [1]. Geen Mct-cijfer gevonden (alleen waarde, rough en polished niet gesplitst); eenheid Mct/j blijft dus **onbekend**, de waarde per karaat verschilt sterk per type en zit niet in het gewicht.

## 1 · Ketenkaart
```
DMCC / Almas Tower `dia-dmcc-almas` ──(b1 truck · Sheikh Zayed Road E11 → Airport Road · kopie · 31,2 km)──►
DXB-vrachtterminal (Cargo Village) `dia-dxb-vracht` ──(b2 lucht · vlucht DXB → JFK, grootcirkel, aannemelijk · 10.999 km)──►
JFK South Cargo Area `dia-jfk-cargo` ──(b3 truck · Van Wyck → Kew Gardens → Queens-Midtown Tunnel · kopie · 25,3 km)──►
47th Street Diamond Exchange `dia-ny-47th` ── stoppunt
```
Alle vier de ankers zijn hergebruikt, niet opnieuw gelegd; b1 en b3 zijn letterlijke kopieën. Nieuw is alleen het luchtbeen b2.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | DMCC/Almas Tower → DXB-vrachtterminal | Sheikh Zayed Road (E11) → Airport Road; **letterlijke kopie** `diamant-dubai-surat-weg-dmcc-dxb.geojson` (= `diamant-dubai-antwerpen` b1) | hemelsbreed 29,0 km, geen wegkm (kopie 31,2 km; +7,6% is indicatie, geen norm) | kopie | nee |
| b2 | B | lucht | DXB-vrachtterminal → JFK South Cargo Area | vlucht DXB → JFK, grootcirkel (aannemelijk: handelsstroom gebrond, vlucht niet) | 10.999,2 grootcirkel [berekend, `maak_luchtbeen.py`, 441 punten] | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | JFK South Cargo Area → 47th Street Diamond Exchange | Van Wyck Expwy → Kew Gardens Interchange → LIE → Queens-Midtown Tunnel; **letterlijke kopie** `diamant-mumbai-newyork-weg-jfk-47th.geojson` | hemelsbreed 19,2 km, geen wegkm (kopie 25,3 km) | kopie | nee |

Geen zeebeen (geen haven-aanloop). Het DXB-platform ligt airside, maar het b1-geojson eindigt op de openbare weg 0,22 km van het anker en het b3-geojson begint 0,006 km van het JFK-anker: geen last-mile-stippel nodig (zelfde oordeel als `diamant-dubai-surat`). Geen leiding, geen spoor.

## 3 · Ankers (één per site en per overslag, alle vier hergebruikt)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-dmcc-almas` | handelshub / vertrek | DMCC / Dubai Diamond Exchange, Almas Tower, JLT | 25.0689, 55.1412 | [2][3][10] (`diamant-dubai-surat`) | bron-gelegd (z15 gezien: kruis midden in het JLT-hoogbouwcluster langs de Sheikh Zayed Road, torens met lange schaduwen) |
| `dia-dxb-vracht` | overslag truck → lucht | DXB Cargo Village / SkyCargo-loodsen, Al Garhoud | 25.2574524, 55.3405972 | [7][10] (`diamant-dubai-surat`, `-dubai-antwerpen`) | bron-gelegd op zoneniveau (z15 gezien: kruis op het loodsen- en terminalcluster aan de westrand van het apron, wide-bodies op het platform ernaast; welk pand diamant afhandelt niet te zien) |
| `dia-jfk-cargo` | overslag lucht → truck | JFK South Cargo Area (Cargo Plaza/South Cargo Road), Queens | 40.6587, -73.7952 | [6][11] (`diamant-mumbai-newyork`; in het ontwerp stond lon,lat — hier lat,lon) | bron-gelegd (z15 gezien: kruis op een lang loodsgebouw langs een taxibaan met wide-body vrachttoestellen, vrachtloodsen ten noordoosten ervan) |
| `dia-ny-47th` | beurs / eindpunt | 47th Street Diamond Exchange, 1196 Avenue of the Americas, Manhattan | 40.7578, -73.9817 | [8][11] (`diamant-mumbai-newyork`) | bron-gelegd (z15 gezien: dicht bouwblok in de Diamond District, geen eigen terrein te onderscheiden) |

## 4 · Via-punten
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | — | geen | — | letterlijke kopie; één doorgaande stadsweg |
| b3 | 1–5 | Van Wyck nabij JFK · Van Wyck Kew Gardens · Kew Gardens Interchange · Queens-Midtown Tunnel Queens-portaal · Manhattan-portaal | zie `diamant-mumbai-newyork.md` §4 (40.6504,-73.8051 · 40.7033,-73.8166 · 40.7165,-73.8279 · 40.7418,-73.9522 · 40.7463,-73.9719) | letterlijke kopie, geen nieuw profiel |
Geofabrik-regio's (kopieën, geen nieuwe scan): b1 `gcc-staten`; b3 `us-new-york`.

## 5 · Verwerkingsknopen
Geen fysieke bewerking. DMCC is veiling en handel (rough én polished komen er samen), JFK is overslag en douane, de 47th Street is handelsdistrict; geen slijperij in deze keten.

## 6 · Stoppunt
De brief stopt bij de 47th Street Diamond Exchange: dat is het eindpunt uit het ontwerp, en geen bron koppelt déze lading aan een juwelier of retailer — fase D vervalt, fase E vervalt.

## 7 · Open punten
- **De vlucht DXB → JFK is een aanname:** geen bron gevonden die een Dubai-JFK-vracht met diamant noemt (alleen de handelsstroom [1] en de DMCC-New York-banden [2][3]); geen bron noemt vluchtnummer, vrachtterminal of tussenlanding. Eén directe vlucht aangenomen; de lijn zegt "van deze vrachtterminal naar die", niet "langs deze luchtweg".
- **Bestemming binnen de VS niet gebrond:** de VAE-export naar de VS [1] zegt niets over New York of JFK; een deel gaat vermoedelijk naar andere VS-steden. Aannemelijk, niet gebrond.
- **Rough en polished niet gesplitst** in HS 7102 [1]; de pagina-destinatielijst zelf is niet teruggelezen (certificaatfout op trendeconomy.com): totaal 2023 19,3 mld wel gezien, de 1,66 mld / 8,61% komt uit de haalbaarheidstoets (1,66/19,3 = 8,6%, consistent).
- **Derde keten die in dezelfde 47th Street-kopie eindigt** (naast mumbai-newyork, antwerpen-newyork, ramatgan-newyork): weinig nieuws, de DXB-JFK-lijn bestaat nog niet.
- b1 en b3: geen onafhankelijke wegkm; JFK-anker op zoneniveau, niet op het pand van een koerier; `dia-dxb-vracht` op zoneniveau.

## 8 · Bronnen
[1] TrendEconomy, "UAE exports of HS 7102 Diamonds" (2023: 19,3 mld totaal; VS 1,66 mld = 8,61% volgens haalbaarheidstoets). https://trendeconomy.com/data/h2/UnitedArabEmirates/7102
[2] WAM, 2022-06-10, "DMCC boosts Dubai-US relations through agreement with Brooklyn Chamber of Commerce" (Dubai Diamond Exchange promotie in New York). https://www.wam.ae/en/details/1395303056237
[3] DMCC persbericht 2022-06-10 (zelfde overeenkomst). https://landing.dmcc.ae/hubfs/C5-Migrated-Files/Press%20Releases/2022/10_Jun_2022_-_DMCC_Boosts_Dubai-US_Relations_Through_Agreement_with_Brooklyn_Chamber_of_Commerce.pdf?hsLang=en
[4] Rapaport, "A tale of two diamond hubs" (DMCC rough-export 2021 12,96 mld; via zoekresultaat, niet volledig gelezen). https://rapaport.com/magazine-article/a-tale-of-two-diamond-hubs-2/
[5] SkyJems, "Encyclopedia Dubai" (Dubai-luchthavens als vrachthub met verbindingen naar o.a. New York; via zoekresultaat). https://skyjems.ca/pages/encyclopedia-dubai
[6] Wikipedia, "John F. Kennedy International Airport". https://en.wikipedia.org/wiki/John_F._Kennedy_International_Airport
[7] Wikipedia, "Dubai International Airport" (Cargo Village; geen diamant of JFK-vracht genoemd). https://en.wikipedia.org/wiki/Dubai_International_Airport
[8] Wikipedia, "Diamond District, Manhattan". https://en.wikipedia.org/wiki/Diamond_District,_Manhattan
[9] Esri World Imagery via `sat_check.py` (z15): `v2/build-cache/satcheck/sat-diamant-dubai-newyork-{dmcc-almas,dxb-vracht,jfk-cargo,47th}.png`.
[10] Briefs `diamant-dubai-surat` en `diamant-dubai-antwerpen` (ankers `dia-dmcc-almas`, `dia-dxb-vracht`; b1-kopie).
[11] Briefs `diamant-mumbai-newyork`, `-antwerpen-newyork`, `-ramatgan-newyork` (ankers `dia-jfk-cargo`, `dia-ny-47th`; b3-kopie, 5 via-punten).
[12] Ketenontwerp en haalbaarheidstoets M31 golf 20 (intern); v1 `data/diamond.js`, `design/diamant.md` (dia-dubai, dia-ny).

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
`bash v2/tools/bak_stromen.sh diamant-dubai-newyork` → `v2/data/stroomroute-diamant-dubai-newyork.json` (34,4 KB, versie 2, lonlat, 1.653 punten, 4 markers). Functie `bak_diamant_dubai_newyork`; geen profiel, geen wegscan, geen zee.

| # | modaliteit | been | km gebakken | brief | stippel |
|---|---|---|---|---|---|
| b1 | truck | DMCC/Almas Tower → DXB-vrachtterminal (kopie `diamant-dubai-surat` b1) | 31,2 | hemelsbreed 29,0, geen wegkm (+7,6%: indicatie) | nee |
| b2 | lucht | vlucht DXB → JFK (grootcirkel, aannemelijk) | 10.999,2 | 10.999,2 berekend | nee, doorgetrokken |
| b3 | truck | JFK South Cargo Area → 47th Street Diamond Exchange (kopie `diamant-mumbai-newyork` b3) | 25,3 | hemelsbreed 19,2, geen wegkm | nee |

Totaal 11.055,7 km. Naden 0,00 km (b1/b2 en b2/b3). Markers (alle vier hergebruikt) liggen 0,018 / 0 / 0 / 0 km van hun lijn.

**Recept.** b1 en b3 zijn byte-gelijke kopieën (`cmp` getoetst) van de geojsons van de moederstromen, in `v2/build-cache/ais/graaf/` onder de prefix `diamant-dubai-newyork-`. b2 uit `maak_luchtbeen.py --van DXB-vrachtterminal|25.2574524,55.3405972 --naar JFK South Cargo Area|40.6587,-73.7952` (441 punten, FeatureCollection). De vlag-functie gebruikt `--been-geojson` voor alle drie; hecht_marnet routeert niets ("vooraf gebakken lijn").

**Toelichting.**
- Vlucht: een grootcirkel tussen twee gelegde vrachtterminals, doorgetrokken; "aannemelijk" staat in de beennaam (handelsstroom gebrond, vlucht, vluchtnummer en terminal niet).
- Geen stippels: b1 eindigt 0,22 km en b3 begint 0,006 km van het anker op de openbare weg, dus geen airside last-mile-stippel. Geen haven-aanloop, leiding of spoor.
- Toets: knikken b1 6 (0 omkeringen), lucht 0, b3 17 met 2 TERUGLOOP-omkeringen (40.71596,-73.82839 bij Kew Gardens Interchange, 175,9 gr; 40.65773,-73.80736 bij Van Wyck/JFK, 154,1 gr, R 4-6 m). Die zitten in de gekopieerde b3-geometrie en horen bij de moederstroom `diamant-mumbai-newyork` (en de andere 47th-Street-kopieën); hier niet aangeraakt.
- Rechte-benen-toets: geen bevinding voor deze stroom.

**Lessen.** (1) Een keten van twee kopieën plus één luchtbeen is een bak van één commando. (2) De 47th Street-kopie draagt twee lokale terugloop-knikken mee naar elke stroom die haar hergebruikt; repareren kan alleen centraal bij de bron. (3) Zoals eerder: de ±15%-toets is hier geen norm omdat er geen echte wegkm bestaan.
