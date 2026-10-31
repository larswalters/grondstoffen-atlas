# Routebrief (licht) · diamant — Ramat Gan → Ben Gurion → Brussel → Antwerpen (Israël → België)

**stroom-id:** `diamant-ramatgan-antwerpen` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** gepolijste (en ruwe) diamant van de Israel Diamond Exchange (Diamond Tower, Ramat Gan) gaat per beveiligde truck (stippel, geen net) naar de Maman-vrachtterminal van Ben Gurion (TLV), vliegt als vrachtvlucht (grootcirkel, aannemelijk: één bron voor de handelsstroom, vlucht niet gebrond) naar Brucargo op Brussels Airport (BRU) en rijdt over de E19 via Mechelen naar de AWDC / het Diamond Office in de Antwerpse Diamantwijk. Richting = de gebronde (Israël exporteert naar België).
**Welke as van het verhaal:** *Israëlische diamant terug naar de Antwerpse handel* — België was in 2023 de derde bestemming van Israëls diamantexport (HS 7102): 524 mln USD, 7,98% van het totaal, na de VS (3,51 mld, 53%) en Hongkong (669 mln, 10,1%) [1]; Wikipedia noemt voor 2012 ook België met 8% van de polished-export (steun, ouder) [2]. **Volume in Mct/j: niet gevonden** (geen karaatcijfer per bestemming); alleen waarde. HS 7102 omvat ruw én gepolijst, het gewicht blijft Mct en de waarde per karaat verschilt sterk, die staat niet in het gewicht.

## 1 · Ketenkaart
```
Israel Diamond Exchange, Diamond Tower `dia-ide` ──(b1 truck · stippel last mile, geen net: Israel-extract ontbreekt · hemelsbreed 13,6 km, geen wegkm; letterlijke kopie)──►
Maman Cargo Terminal, Ben Gurion (TLV) `dia-tlv-cargo` ──(b2 lucht · vlucht TLV → BRU, grootcirkel, aannemelijk: één bron · 3.255,3 km)──►
Brucargo, Brussels Airport `dia-brucargo` ──(b3 truck · E19 via Mechelen · 37,4 km, letterlijke kopie)──►
AWDC / Diamond Office, Hoveniersstraat 22, Antwerpen `dia-awdc` ── stoppunt
```
Alle vier ankers bestaan al en worden letterlijk hergebruikt; b1 en b3 zijn letterlijke kopieën, alleen b2 (de vlucht) is nieuw.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Israel Diamond Exchange → TLV-vrachtterminal | geen corridor: stippel last mile (geen net op deze korrel, Israel-extract ontbreekt, schematisch); kopie beenregel `diamant-ramatgan-hongkong` b1 / `-newyork` b1 | hemelsbreed 13,6 km, geen wegkm [berekend] | `--stippel` (letterlijke beenregel) | ja — hier reikt het net niet |
| b2 | B | lucht | TLV → BRU | vlucht TLV → BRU (vrachtvlucht, grootcirkel, aannemelijk: één bron) | 3.255,3 grootcirkel [`maak_luchtbeen`, proefrun, 132 punten]; roame geeft ca. 2.020 mijl = 3.251 km [6] | maak_luchtbeen.py | nee — doorgetrokken |
| b3 | C | truck | Brucargo → AWDC / Diamond Office | E19 via Mechelen (en R1 Antwerpen-Zuid); kopie `diamant-jwaneng-antwerpen` b4 (richting Brucargo → Antwerpen, geen omkering nodig) | 37,4 [gebakken kopie]; OSRM-routing 37,7 km [10] (geen bedrijfs-/overheidsopgave); hemelsbreed ca. 34,4 km | letterlijke kopie geojson `diamant-jwaneng-antwerpen-weg-brucargo-antwerpen.geojson` (435 punten, FeatureCollection) | nee |

b1 heeft geen wegkilometer-toets (hemelsbreed, indicatie). b3 is een bestaande bake, binnen ±15% van de OSRM-lengte (−0,8%).

## 3 · Ankers (één per site en per overslag) — alle hergebruikt, geen nieuwe gelegd
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-ide` | beursgebouw / vertrekpunt | Israel Diamond Exchange, Diamond Tower, Ramat Gan | 32.0836, 34.8024 | [4][11] (`diamant-ramatgan-newyork`) | bron-gelegd (daar z16 gezien: hoogbouwcluster van het Bourse-district; Wikipedia 32°5′0,84″N 34°48′8,51″E = 32.08357/34.80236) |
| `dia-tlv-cargo` | vrachtterminal / vertrek luchtvracht | Maman Cargo Terminal, Ben Gurion Airport (TLV), Lod | 31.9949, 34.9019 | [5][11] | bron-gelegd op terminalniveau (daar z17 gezien: groot loodsgebouw met truckparking oostzijde, platform met vrachttoestellen ca. 300 m noordelijker); welk pand diamant afhandelt: onzeker. Landzijde: geen airside-stippel |
| `dia-brucargo` | vrachtterminal / aankomst luchtvracht, overslag lucht → truck | Brucargo, Brussels Airport (BRU), Machelen | 50.90628, 4.45584 | [12] (`diamant-antwerpen-newyork`, `-ekati-antwerpen`) | bron-gelegd (daar z15 gezien: vrachtloodsen en verhard platform met geparkeerde toestellen, noordrand cargozone) |
| `dia-awdc` | handels-/certificeringshub / eindpunt | AWDC / Diamond Office, Hoveniersstraat 22, Antwerpen | 51.2152, 4.4187 | [9][12] | bron-gelegd (daar z15 gezien: dicht stedelijk bouwblok in de Diamantwijk, geen eigen terrein) |

Geen nieuwe satellietblik: alle vier staan letterlijk op de coördinaat van de bron-brief (beelden `v2/build-cache/satcheck/sat-diamant-ramatgan-newyork-ide.png`, `-tlv-maman-z17.png`, en de Brucargo-/AWDC-beelden van `diamant-antwerpen-newyork`). Het b3-geojson begint op 50.9056, 4.4576 (0,145 km van `dia-brucargo`, binnen de 5 km-norm; niet verschoven) en eindigt 0,026 km van `dia-awdc`; het luchtbeen eindigt op het anker. Brucargo is landzijde bereikbaar: geen airside-stippel.

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | — | geen | — | stippel, geen routering |
| b3 | 1–2 | E19 bij Mechelen · E19/R1-knooppunt Antwerpen-Zuid (Wilrijk) | 51.0213, 4.4481 · 51.1103, 4.4319 | letterlijke kopie, geen nieuw profiel; zie `diamant-jwaneng-antwerpen.md` §4: E19 vastpinnen i.p.v. een N-weg door Mechelen, en om de Antwerpse ring i.p.v. dwars door de stad |

## 5 · Verwerkingsknopen
*(geen fysieke bewerking: handelsketen van reeds gepolijste steen; de Diamond Office doet import-/exportafhandeling in één loket [9], de IDE is een handelsvloer met ca. 1.500 bedrijven [4]. Fase D/E vervallen.)*

## 6 · Stoppunt
De brief stopt bij de AWDC / het Diamond Office in Antwerpen: het eindpunt van het ketenontwerp en het Belgische handelsloket; geen bron koppelt déze stroom aan een individuele slijperij of juwelier. Fase D vervalt.

## 7 · Open punten
- **De vlucht TLV → BRU is niet gebrond.** Alleen de handelsstroom (Israël → België, 524 mln USD in 2023) is gebrond [1]; dat diamant per directe vrachtvlucht op BRU aankomt, noemt geen geopende bron. Wat wél vaststaat: Antwerpse diamant gaat per bepantserde Brink's-wagen naar Brussels Airport [7][8], en Brussels Airlines staat als non-stop BRU–TLV-dienst geboekt (marketingcarrier, frequentie niet getoond) [6]. Een tussenlanding of de weg via Zürich/Londen is niet uitgesloten. Beennaam: aannemelijk.
- **Verouderde of secundaire cijfers.** Wikipedia 2012 (België 8% van de polished) alleen als steun [2]. Trading Economics toont voor Israël → België een diamantpost van 311,19 mln USD (UN Comtrade, jaar op de pagina onduidelijk, pagina onhandig te lezen) [3]; Rapaport meldde via zoekresultaat 420 mln USD voor 2017 (+20%, niet geopend) [13]. Alles waarde, geen karaat; HS 7102 = ruw + gepolijst + industrie.
- **Oorlog 2026.** De IDE ging in maart 2026 op noodmodus (Rapaport, via brief `diamant-ramatgan-hongkong` §7 [12 daar], niet opnieuw geopend) en Israëlische vluchten waren verstoord; Brussels Airlines-vluchten naar Tel Aviv waren volgens een Belgisch nieuwsitem opgeschort tot eind oktober (datum onduidelijk, via zoekresultaat). De kaart toont de vaste vorm van de handelsstroom, niet de huidige operatie.
- **Richting:** in omgekeerde richting (Antwerpen → Israël) bestaat een wekelijkse zending volgens een Hebreeuwse nieuwssite (bhol.co.il, 403, via zoekresultaat) [14]; deze keten tekent de gebronde exportrichting Israël → België.
- **b1 is schematisch** (13,6 km hemelsbreed, geen wegkm); optioneel centraal een Israel-extract (`fetch_landnet.py`). Sitelaag `w-ramatgan` staat 0,7 km van `dia-ide` (centraal gelijktrekken).
- **Maman:** het pand dat diamant afhandelt is onzeker; de Maman-pagina noemt kluizen en beveiligde begeleiding maar geen diamant [5].

## 8 · Bronnen
[1] Trendeconomy, "Israel exports of Diamonds (HS 7102)", 2023: VS 3,51 mld USD (53%), Hongkong 669 mln (10,1%), België 524 mln (7,98%, 3e), India 326 mln. https://trendeconomy.com/data/h2/Israel/7102
[2] Wikipedia, "Diamond industry in Israel" — polished-export 2012 netto 5,56 mld USD; VS 36%, Hongkong 28%, België 8%; diamant 9,28% van de export 2023 (OEC). https://en.wikipedia.org/wiki/Diamond_industry_in_Israel
[3] Trading Economics (UN Comtrade), Israël export naar België, rij "Diamonds, whether or not worked, but not mounted or set" 311,19 mln USD (jaar onduidelijk). https://tradingeconomics.com/israel/exports/belgium/pearls-precious-stones-metals-coins
[4] Wikipedia, "Israel Diamond Exchange" — Ramat Gan, coördinaat 32°5′0,84″N 34°48′8,51″E, vier verbonden gebouwen, ca. 1.500 bedrijven. https://en.wikipedia.org/wiki/Israel_Diamond_Exchange
[5] Maman Group, "Maman Cargo Terminal" (kluizen, beveiligde begeleiding van gevoelige lading). https://en.maman-group.co.il/companies/maman-cargo-terminal/
[6] Roame, vluchtkaart BRU–TLV (Brussels Airlines non-stop, ca. 2.020 mijl grootcirkel). https://roame.travel/flightmap/BRU/TLV
[7] Wikipedia, "Brussels Airport diamond heist" (2013) — diamant per Brink's-wagen van Antwerpen naar het platform van Brussels Airport. https://en.wikipedia.org/wiki/Brussels_Airport_diamond_heist
[8] CBS News, 19-2-2013, heist op Brussels Airport — 200 mln USD dagelijkse handel in de Antwerpse diamantwijk, bepantserde wagen naar de luchthaven. https://www.cbsnews.com/news/diamond-heist-at-brussels-airport-sparks-hunt-for-8-masked-men-and-an-estimated-50m-in-gems/
[9] Wikipedia, "Antwerp World Diamond Centre" — Hoveniersstraat, Diamond Office (sinds 1945, one-stop import/export), ca. 1.800 dealers. https://en.wikipedia.org/wiki/Antwerp_World_Diamond_Centre
[10] Brief `diamant-jwaneng-antwerpen.md` (b4, bron [11] daar: OSRM Brucargo → AWDC 37,7 km) en geojson `v2/build-cache/ais/graaf/diamant-jwaneng-antwerpen-weg-brucargo-antwerpen.geojson` (37,41 km, 435 punten).
[11] Briefs `diamant-ramatgan-newyork.md` en `diamant-ramatgan-hongkong.md` — ankers `dia-ide`, `dia-tlv-cargo`, stippel b1.
[12] Briefs `diamant-antwerpen-newyork.md` en `diamant-ekati-antwerpen.md` — ankers `dia-brucargo`, `dia-awdc`.
[13] Rapaport (via zoekresultaat, niet geopend): Israëlische export naar België 2017 +20% tot 420 mln USD.
[14] bhol.co.il/news/125764 (403, via zoekresultaat): zending Antwerpen → Israël, wekelijkse zending van Antwerpse handelaren.
[15] `maak_luchtbeen.py` TLV → BRU: 3.255,3 km grootcirkel, 132 punten (proefrun 2026-10-31, uitvoer in scratchpad, niet in build-cache). Eigen berekening.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
`bash v2/tools/bak_stromen.sh diamant-ramatgan-antwerpen` -> `v2/data/stroomroute-diamant-ramatgan-antwerpen.json` (12,0 KB, versie 2, lonlat). Functie `bak_diamant_ramatgan_antwerpen` in `v2/tools/bak_stromen.sh`; geen profiel, geen extract, geen scan, geen zee, geen haven-aanloop, geen leiding.

| been | modaliteit | km | punten | geometrie |
|---|---|---|---|---|
| b1 | truck | 13,6 | 2 | stippel (letterlijke beenregel uit `bak_diamant_ramatgan_hongkong` b1) |
| b2 | lucht | 3.255,3 | 132 | `maak_luchtbeen.py` TLV -> BRU, doorgetrokken |
| b3 | truck | 37,4 | 435 | letterlijke kopie geojson `diamant-jwaneng-antwerpen-weg-brucargo-antwerpen.geojson` |

Totaal 3.306,3 km, 569 punten, 4 markers (`dia-ide`, `dia-tlv-cargo`, `dia-brucargo`, `dia-awdc`; alle op 0,0 km van hun lijn, awdc 0,03 km).

**Recept:** `python v2/tools/maak_luchtbeen.py --van "Maman Cargo Terminal TLV|31.9949,34.9019" --naar "Brucargo BRU|50.90628,4.45584" --uit v2/build-cache/ais/graaf/diamant-ramatgan-antwerpen-lucht-tlv-bru.geojson`, daarna de bake-functie.

**Toelichting.**
- b1 is een stippel omdat hier het net niet reikt (Israel-extract ontbreekt): hemelsbreed 13,6 km, geen wegkm, dus geen km-toets. Naad b1 -> b2: 0,0 km.
- b2 is doorgetrokken (vlucht tussen twee gelegde vrachtterminals); vlucht niet gebrond, "aannemelijk: een bron" staat in de beennaam. Beide ankers landzijde, geen airside-stippel. Eigen berekening 3.255,3 km tegen roame ca. 3.251 km (+0,1%).
- b3 is een kopie; naad b2 -> b3 is 0,145 km (norm 5 km). 37,4 km tegen OSRM 37,7 km (-0,8%, geen bedrijfsopgave).
- Geen haven-aanloop, geen leiding.

**Toets.** Naden max. 0,145 km. `toets_knikken.py`: 6 knikken >= 60 graden, alle in het gekopieerde b3-geojson bij Brucargo-uiteinde en AWDC-uiteinde (spikes op straatniveau, R 3-50 m), 0 omkeringen, 0 terugloop; bevinding bij `diamant-jwaneng-antwerpen`, niet hier gerepareerd. `toets_rechte_benen.py --min-km 5` meldt alleen de bedoelde stippel b1.

**Lessen.** (1) Een keten met twee letterlijke kopieen en een grootcirkel is in minuten gebakken: de brief vooraf met de geojson-paden en kilometers maakt de functie triviaal. (2) bak_stromen.sh wordt door parallelle agenten bewerkt: een lopende bash-run kan aan het eind een parse-fout melden (regel 15665) terwijl het json al geschreven is; `bash -n` achteraf bleek schoon.
