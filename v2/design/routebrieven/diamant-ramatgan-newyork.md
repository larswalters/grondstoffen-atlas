# Routebrief (licht) · diamant — Ramat Gan → Ben Gurion → New York (Israël → VS)

**stroom-id:** `diamant-ramatgan-newyork` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**Keten in één zin:** gepolijste high-end diamant van de Israel Diamond Exchange (Diamond Tower, Ramat Gan) gaat per beveiligde truck naar de vrachtterminal van Ben Gurion (TLV), vliegt als vrachtvlucht (grootcirkel, aannemelijk: één bron) naar de vrachtterminal van JFK en rijdt over de Van Wyck Expressway en door de Queens-Midtown Tunnel naar de 47th Street Diamond Exchange in Manhattan.
**Welke as van het verhaal:** *Israël → VS: het dunne high-end draadje* — circa 2 Mct/j gepolijst [v1 design/diamant.md §4c, natte vinger, peiljaar 2023-24; geen karaatcijfer in een externe bron]. De VS nam 36% van de Israëlische polished-export in 2012 [2]. Waarde per karaat ligt veel hoger dan bij de Indiase volumestroom (grote stenen); het gewicht blijft Mct, de waarde staat niet in het gewicht. Zwakste as van de diamantreeks: geen bron noemt déze vlucht.

## 1 · Ketenkaart
```
Israel Diamond Exchange, Diamond Tower `dia-ide` ──(b1 truck · stippel last mile, geen net: Israel-extract ontbreekt · hemelsbreed 13,6 km)──►
Ben Gurion vrachtterminal (Maman, TLV) `dia-tlv-cargo` ──(b2 lucht · vlucht TLV → JFK, grootcirkel, aannemelijk: één bron · ~9.119 km)──►
JFK South Cargo Area `dia-jfk-cargo` ──(b3 truck · Van Wyck → Kew Gardens → Queens-Midtown Tunnel · 25,3 km, kopie)──►
47th Street Diamond Exchange `dia-ny-47th` ── stoppunt
```
`dia-jfk-cargo` en `dia-ny-47th` zijn bestaande ankers uit `diamant-mumbai-newyork.md`; b3 is daarvan een letterlijke kopie.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Israel Diamond Exchange → TLV-vrachtterminal | geen corridor: stippel last mile (geen net op deze korrel: Israel-extract ontbreekt, schematisch) | hemelsbreed 13,6 km, geen wegkm [berekend] | `--stippel` | ja — hier reikt het net niet |
| b2 | B | lucht | TLV → JFK | vlucht TLV → JFK (vrachtvlucht, grootcirkel), aannemelijk: één bron | 9.119 hemelsbreed [berekend, maak_luchtbeen geeft het exacte getal]; ontwerp ~9.117 | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | JFK South Cargo Area → 47th Street Diamond Exchange | Van Wyck Expwy → Kew Gardens Interchange → LIE → Queens-Midtown Tunnel (kopie `diamant-mumbai-newyork` b3) | 25,3 [gebakken, kopie] | letterlijke kopie geojson | nee |

b1 heeft geen echte wegkilometer: er bestaat geen Israel-extract, dus geen wegprofiel; een hemelsbreed getal van 13,6 km is een indicatie, geen norm. De stippel is eerlijk "hier reikt het net niet" (Israël ontbreekt in de 184 extracts, bakhandleiding §3).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-ide` | beursgebouw / vertrekpunt | Israel Diamond Exchange, Diamond Tower, Ramat Gan | 32.0836, 34.8024 | [1][3] | bron-gelegd (z16 gezien: kruis op de hoogbouwcluster van het Bourse-district, torens met lange schaduwen; Wikipedia 32.08357/34.80236, Photon "Diamond Tower" 32.08393/34.80215) |
| `dia-tlv-cargo` | vrachtterminal / vertrek luchtvracht | Maman Cargo Terminal, Ben Gurion Airport (TLV), Lod | 31.9949, 34.9019 | [4][6][8] | bron-gelegd op terminalniveau (z17 gezien: groot loodsgebouw met oranje-wit dak, truckparking aan de oostzijde, en ca. 300 m noordelijker een platform met geparkeerde vrachttoestellen; OSM-gebouw "ממן" op dit punt). Welk pand diamant afhandelt: onzeker |
| `dia-jfk-cargo` | vrachtterminal / aankomst luchtvracht | JFK South Cargo Area, Queens | 40.6587, -73.7952 | [9] | bron-gelegd (hergebruikt uit `diamant-mumbai-newyork.md`, daar z16 gezien: loodsen en wide-body vrachttoestellen langs Cargo Plaza) |
| `dia-ny-47th` | beurs-/handelsgebouw / eindpunt | 47th Street Diamond Exchange, 1196 Avenue of the Americas, Manhattan | 40.7578, -73.9817 | [9] | bron-gelegd (hergebruikt uit `diamant-mumbai-newyork.md`, daar z15 gezien: stedelijk bouwblok in de Diamond District) |

Het TLV-anker ligt aan de landzijde (truckparking en laaddocks oostzijde); een airside-last-mile met extra stippel is dus niet nodig. Het tweede terminalgebouw (Swissport, geopend 2008 [5]) is niet gelegd en niet gebruikt.

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | — | geen | — | stippel, geen routering |
| b3 | 1–5 | Van Wyck nabij JFK · Van Wyck Kew Gardens · Kew Gardens Interchange · Queens-Midtown Tunnel Queens-portaal · Manhattan-portaal | zie `diamant-mumbai-newyork.md` §4 (40.6504,-73.8051 · 40.7033,-73.8166 · 40.7165,-73.8279 · 40.7418,-73.9522 · 40.7463,-73.9719) | letterlijke kopie, geen nieuw profiel |

## 5 · Verwerkingsknopen
*(geen — handelsketen van reeds gepolijste steen; het slijpen in Ramat Gan zelf valt buiten deze keten, geen bron koppelt déze stenen aan een slijperij. Fase D/E vervallen.)*

## 6 · Stoppunt
De brief stopt bij de 47th Street Diamond Exchange: het eindpunt uit het ketenontwerp en een handelsgebouw; geen bron koppelt déze stroom aan een individuele juwelier. Fase D vervalt.

## 7 · Open punten
- **Geen bron voor de directe vlucht TLV → JFK** voor diamant. Wikipedia noemt wel dat El Al het meeste vrachtvolume in de buik van passagiersvluchten vervoert [12] en [7] dat diamant standaard als vracht op lijnvluchten gaat; de vlucht is dus aannemelijk (één bron, beennaam "aannemelijk: één bron"), niet bevestigd. Tussenlanding niet gebrond: één directe vlucht aangenomen.
- **Het TLV-vrachtgebouw is op terminalniveau gelegd**, niet op het pand van een beveiligde koerier (Malca-Amit, Brink's): niet gebrond.
- **b1 is schematisch**: 13,6 km hemelsbreed, geen wegkm. Optioneel centraal: Israel-extract toevoegen (`fetch_landnet.py`, bakhandleiding §3), dan kan b1 alsnog een wegbeen worden.
- **Volume:** circa 2 Mct/j is een v1-natte vinger; geen externe karaatbron gevonden. Alleen dollarwaarden zijn gebrond (polished-export 2012 $5,56 mld, VS 36% [2]).
- **Sitelaag:** `w-ramatgan` in `diamant-sitelaag.json` staat op 32.084/34.81 (status aannemelijk, uit trainingskennis), ca. 0,7 km oostelijk van `dia-ide`; centraal gelijktrekken.
- Het IDE-gebouwcomplex bestaat uit vier gebouwen met loopbruggen [1]; het anker staat op de Diamond Tower, niet op de bruglinken.

## 8 · Bronnen
[1] Wikipedia, "Israel Diamond Exchange" — Ramat Gan, vier gebouwen, Diamond Tower (1992), coördinaat 32.08357/34.80236. https://en.wikipedia.org/wiki/Israel_Diamond_Exchange
[2] Wikipedia, "Diamond industry in Israel" — Diamond District Ramat Gan; VS 36% van de polished-export 2012 (Hongkong 28%, België 8%); polished-export 2012 $5,56 mld. https://en.wikipedia.org/wiki/Diamond_industry_in_Israel
[3] OpenStreetMap (ODbL) via Photon — "מגדל יהלום" (Diamond Tower) 32.08393/34.80215; "בורסת היהלומים" 32.08344/34.80102. https://photon.komoot.io
[4] Maman Group, "Maman Cargo Terminal" — terminal Ben Gurion Airport, ~300.000 t/j, kluizen en beveiligde begeleiding van gevoelige lading. https://en.maman-group.co.il/companies/maman-cargo-terminal/
[5] Ferrovial Newsroom, 2008 — Swissport cargo terminal Ben Gurion (18.000 m², 200.000 t/j). https://newsroom.ferrovial.com/en/?p=5283
[6] OpenStreetMap (ODbL) via Photon — gebouw "ממן" 31.99491/34.90186, Lod/Ben Gurion. https://photon.komoot.io
[7] Israel Diamond Institute, "Transports of diamonds in the world" — diamant gaat overzee als vracht op lijnvluchten, beveiligingsbedrijven laden direct bij het vliegtuig (Malca-Amit, Brink's). https://en.israelidiamond.co.il/diamond-articles/diamonds/transports-diamonds-world/
[8] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-diamant-ramatgan-newyork-ide.png`, `-tlv-maman-z17.png`, `-tlv-cargo-z16.png`, `-tlv-maman.png`, `-tlv-breed.png` (2026-10-09).
[9] `diamant-mumbai-newyork.md` (M31 golf 3) — ankers `dia-jfk-cargo`, `dia-ny-47th` en het gebakken been `diamant-mumbai-newyork-weg-jfk-47th.geojson` (25,3 km).
[10] `data/diamond.js` + `design/diamant.md` §4c (v1) — flow `dia-ramat-gan → dia-ny`, 2 Mct, mode air.
[11] Globes, "Airports Authority awards new cargo terminal contract" — twee terminaloperators (Maman, Swissport) op Ben Gurion. https://en.globes.co.il/en/article-802082
[12] Wikipedia, "Ben Gurion Airport" — vracht 2025; El Al vervoert het meeste vracht in de buik van passagiersvluchten, Challenge Airlines grootste vrachtvliegtuigoperator. https://en.wikipedia.org/wiki/Ben_Gurion_Airport

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Bestand:** `v2/data/stroomroute-diamant-ramatgan-newyork.json` (versie 2, lonlat, 25,1 KB) · functie `bak_diamant_ramatgan_newyork()` in `v2/tools/bak_stromen.sh` · `bash v2/tools/bak_stromen.sh diamant-ramatgan-newyork`. Geen profiel in `maak_stroombeen_weg.py` (b1 stippel, b3 kopie).

| # | modaliteit | been | km gemeten | brief | naad | stippel |
|---|---|---|---|---|---|---|
| b1 | truck | last mile Israel Diamond Exchange → Ben Gurion vrachtterminal | 13,6 | hemelsbreed 13,6, geen wegkm | start | ja, hier reikt het net niet |
| b2 | lucht | vlucht TLV → JFK (vrachtvlucht, grootcirkel, aannemelijk: één bron) | 9.119,2 (366 punten) | 9.119 / ontwerp 9.117 | 0,0 km | nee, doorgetrokken |
| b3 | truck | JFK South Cargo Area → 47th Street Diamond Exchange (kopie diamant-mumbai-newyork b3) | 25,3 (806 punten) | 25,3 | 0,0 km | nee |

Totaal 9.158,1 km · 3 benen · 4 markers (`dia-ide`, `dia-tlv-cargo`, `dia-jfk-cargo`, `dia-ny-47th`, alle op 0,0 km van de lijn).

**Recept.** b2: `python v2/tools/maak_luchtbeen.py --van "Ben Gurion vrachtterminal (Maman, TLV)|31.9949,34.9019" --naar "JFK South Cargo Area|40.6587,-73.7952" --uit v2/build-cache/ais/graaf/diamant-ramatgan-newyork-lucht-tlv-jfk.geojson` (9.119,2 km). b3: letterlijk `diamant-mumbai-newyork-weg-jfk-47th.geojson`, naam met de kopie-verwijzing. b1: `--stippel` tussen de twee ankers.

**Toelichting.**
- **Stippel b1:** er is geen Israel-extract (bakhandleiding §3), dus geen wegprofiel; de stippel is een rechte lijn van 13,6 km, geen wegkm. De ±15%-toets is hier niet van toepassing. Centraal: Israel-extract toevoegen maakt er alsnog een wegbeen van.
- **Vlucht b2:** doorgetrokken grootcirkel tussen twee gelegde vrachtterminals; aannemelijk (één bron: diamant gaat als vracht op lijnvluchten), geen bron voor déze directe vlucht, geen tussenlanding. TLV-anker ligt landzijde: geen airside-stippel, geen haven-aanloop, geen zee.
- **Kopie b3:** de knikkentoets meldt 17 knikken >= 60 graden, waarvan 2 teruglopen; alle liggen in het gekopieerde b3-geometrie (Queens, spikes op klaverbladen en Midtown), niet in nieuw werk. Bevinding hoort bij diamant-mumbai-newyork.

**Lessen.** Een stroom met een hergebruikt Amerikaans staartstuk en een luchtbeen bakt in één run zonder wegscan; de enige nieuwe geometrie is de grootcirkel. Het sitelaag-punt `w-ramatgan` ligt nog ca. 0,7 km van `dia-ide` (centraal gelijktrekken).
