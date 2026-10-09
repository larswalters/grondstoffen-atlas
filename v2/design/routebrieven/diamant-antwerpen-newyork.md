# Routebrief (licht) · diamant — Antwerpen (AWDC) → Brussels Airport → JFK → New York (België → VS)

**stroom-id:** `diamant-antwerpen-newyork` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**Keten in één zin:** gepolijste diamant van het AWDC/Diamond Office in Antwerpen gaat per truck over de E19 naar Brucargo (Brussels Airport), vliegt als vrachtvlucht
(grootcirkel BRU → JFK, **aannemelijk: één bron**) naar de South Cargo Area van JFK en rijdt per truck via Van Wyck, Kew Gardens en de Queens-Midtown Tunnel naar de 47th Street Diamond Exchange in Manhattan.
**Welke as van het verhaal:** *Europa → de grootste eindmarkt* — indicatie 4 Mct/j gepolijst (v1 `design/diamant.md` §4d / `data/diamond.js` flow dia-antwerp → dia-mkt-us, natte vinger, peiljaar 2023-24, geen waarheid; eenheid Mct/j = miljoen karaat per jaar) [1].
Geen karaatcijfer in een externe bron. Waarde: België → VS ruim 2,1 mld USD per jaar (AWDC-topman via Brussels Times 2025; Prism News noemt 2,1 mld voor 2024) [3][5] en 438,8 mln USD in mei 2018, polished, de VS grootste bestemming [2] — verouderd en dun, maar de richting klopt.
Waarde per karaat hoog (gepolijst) — hier niet in het gewicht.

## 1 · Ketenkaart
```
AWDC/Diamond Office, Antwerpen `dia-awdc` ──(b1 truck · E19 via Mechelen · letterlijke kopie · 37,4 km)──►
Brucargo, Brussels Airport `dia-brucargo` ──(b2 lucht · vlucht BRU → JFK, grootcirkel, aannemelijk: één bron · 5.883 km)──►
JFK South Cargo Area `dia-jfk-cargo` ──(b3 truck · Van Wyck → Kew Gardens → Queens-Midtown Tunnel · letterlijke kopie · 25,3 km)──►
47th Street Diamond Exchange, Manhattan `dia-ny-47th` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | AWDC Antwerpen → Brucargo | E19 via Mechelen; **letterlijke kopie** (zelfde richting) van `diamant-antwerpen-surat` b1 (`…-weg-awdc-brucargo.geojson`) | hemelsbreed 34,4 km, geen wegkm (kopie 37,4) [1] | kopie | nee |
| b2 | C | lucht | Brucargo (BRU) → JFK South Cargo Area (JFK) | vlucht BRU → JFK, grootcirkel (aannemelijk: één bron) | 5.883,3 grootcirkel [berekend] | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | JFK South Cargo Area → 47th Street Diamond Exchange | Van Wyck → Kew Gardens → LIE → Queens-Midtown Tunnel; **letterlijke kopie** van `diamant-mumbai-newyork` b3 (`…-weg-jfk-47th.geojson`) | hemelsbreed 19,2 km, geen wegkm (kopie 25,3) | kopie | nee |

Geen zeebeen (dus geen haven-aanloop), geen leiding, geen spoor. Het b1-geojson eindigt op 50.9056, 4.4576 (0,14 km van het anker `dia-brucargo`): het luchtbeen **begint op dat eindpunt**
(naad b1→b2 = 0), het b3-geojson begint op `dia-jfk-cargo` zelf (naad b2→b3 = 0). Beide wegbenen eindigen op de openbare weg (0,03 resp. 0,006 km van het anker): geen airside-stippel nodig.

## 3 · Ankers (één per site en per overslag — alle vier HERGEBRUIKT, niet opnieuw gelegd)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-awdc` | handels-/certificeringshub / vertrek | AWDC/Diamond Office, Hoveniersstraat 22, Antwerpen | 51.2152, 4.4187 | [9][12] (`diamant-antwerpen-surat` §3) | bron-gelegd (z15 gezien daar: dicht stedelijk bouwblok in de Diamantwijk, geen eigen terrein) |
| `dia-brucargo` | overslag truck → lucht | Brucargo, Brussels Airport | 50.90628, 4.45584 | [8][12] (`diamant-antwerpen-surat` §3) | bron-gelegd (z15 gezien daar: vrachtloodsen en verhard platform met toestellen, noordrand cargozone) |
| `dia-jfk-cargo` | overslag lucht → truck | JFK South Cargo Area (Cargo Plaza/South Cargo Road), Queens | 40.6587, -73.7952 | [11][12] (`diamant-mumbai-newyork` §3) | bron-gelegd op zoneniveau (z16 gezien daar: rij vrachtloodsen met wide-body vrachttoestellen op het apron); welk pand diamant afhandelt is niet gebrond |
| `dia-ny-47th` | beurs-/handelsgebouw / eindpunt | 47th Street Diamond Exchange, 1196 Avenue of the Americas, Manhattan | 40.7578, -73.9817 | [11][12] (`diamant-mumbai-newyork` §3) | bron-gelegd (z15 gezien daar: dicht bouwblok in de Diamond District, geen eigen terrein) |

Niet opnieuw satelliet-gecheckt: de ankers staan al in de sitelaag/zusterbrieven en worden letterlijk overgenomen (opdracht: hergebruik boven herleggen).

## 4 · Via-punten (alleen landbenen; b1 en b3 zijn kopieën, dus geen nieuwe wegscan)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Antwerpen-Zuid (E19/R1, Wilrijk) | 51.1103, 4.4319 | verlaat het stadsnet op de E19 |
| b1 | 2 | E19 bij Mechelen | 51.0213, 4.4481 | blijft op de E19, niet via de R6/centrum Mechelen |
| b3 | 1 | Van Wyck Expressway, nabij JFK | 40.6504, -73.8051 | enige doorgaande snelweg noordwaarts uit de vrachtzone |
| b3 | 2 | Van Wyck Expressway, Kew Gardens | 40.7033, -73.8166 | doorgaand stuk vóór de knoop met Grand Central Parkway/LIE |
| b3 | 3 | Kew Gardens Interchange | 40.7165, -73.8279 | knoop waar Van Wyck overgaat in de LIE |
| b3 | 4 | Queens-Midtown Tunnel, Queens-portaal | 40.7418, -73.9522 | enige tunnelcorridor Queens → Midtown voor vrachtverkeer |
| b3 | 5 | Queens-Midtown Tunnel, Manhattan-portaal | 40.7463, -73.9719 | uitgang, daarna Manhattan-straatpatroon naar 47th Street |
(Uit `diamant-antwerpen-surat` b1-bronbestand en `diamant-mumbai-newyork` §4.) Geofabrik-regio's: **geen scan nodig** (`belgie` en `us-new-york` bestaan al; beide benen zijn kopieën).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| AWDC/Diamond Office | AWDC | polished/rough → export- en importklaring, certificering | geen capaciteit per ketenbron | [9] |
| Brucargo-kluis | Brink's e.a. (2013) | beveiligd transport vanuit het Diamond Office → kluis → pantserwagen naar het toestel | geen cijfer | [8][10] |
Geen smelter of slijperij: de stenen zijn al gepolijst.

## 6 · Stoppunt
De brief stopt bij de 47th Street Diamond Exchange: het ontwerpeindpunt (grootste eindmarkt) en geen bron koppelt déze lading aan een juwelier of retailer — fase D en E vervallen.

## 7 · Open punten
- **Vervoerswijze en route zijn niet per zending gebrond.** Brussels Airlines vliegt Brussel–JFK dagelijks (route sinds 1-6-2012, Wikipedia) [6][7], maar geen bron noemt een diamantvracht BRU → JFK, vluchtnummer of tussenlanding.
  De lading kan via een hub lopen (de roof van 2013 betrof Antwerpse diamant naar Brussels Airport voor een vlucht naar Zürich [8]). Eén directe grootcirkel is dus schematisch: "van deze terminal naar die", niet "langs deze lijn".
  Dat Antwerpse diamant per beveiligde pantserwagen naar Zaventem en dan per vliegtuig gaat, is wél gebrond [8][10].
- **Volume 4 Mct/j is een natte vinger**; geen Mct-cijfer voor België → VS gevonden. De USD-cijfers zijn dun: 438,8 mln in mei 2018 [2] (jaar volgens ontwerp; de pagina zelf zegt alleen "mei", publicatie 2018-06-10); "ruim 2,1 mld USD per jaar" zonder peiljaar [3];
  2024 volgens Prism News (pagina gaf 503, alleen via zoekresultaat gezien, niet geciteerd) [5]. VRT noemt "iets meer dan 2 miljard euro" per jaar [4] — andere valuta, niet samengevoegd.
- **Handelsbeleid en lab-grown** kunnen het volume drukken, niet de route. Tariefbeeld 2025-26 is in de bronnen tegenstrijdig (15%, 10%, weer 0% in juli 2026); niet uitgezocht, geldt het volume, niet de kaart.
- **b1 en b3: geen echte wegkm** (alleen hemelsbreed 34,4 en 19,2 km); de ±15%-toets is voor deze kopieën een indicatie. b1 eindigt 0,14 km van `dia-brucargo` (binnen de 5 km-norm; niet verschoven).
- **JFK-anker op zoneniveau**, niet op het koerierspand. De terugloop-micro-zigzags in de b3-kopie (Kew Gardens/JFK-zijde, 4–6 m) zijn geërfd uit `diamant-mumbai-newyork`; niet hier aangeraakt.
- Het AWDC-FAQ [9] is niet door mij gelezen (alleen via brief `diamant-antwerpen-surat` [4]); Prism News en idexonline-memo alleen via zoekresultaat.

## 8 · Bronnen
[1] Ketenontwerp + haalbaarheidstoets M31 golf 9 (`diamant-antwerpen-newyork`) en `design/diamant.md` §4d / `data/diamond.js` (dia-antwerp → dia-mkt-us, 4, air) — intern.
[2] Rapaport, 2018-06-10, "Belgium's polished-diamond exports rose in May" (6% naar 438,8 mln USD naar de VS, AWDC-data). https://rapaport.com/?p=32180
[3] Brussels Times, 2025-09-29, "'Tremendous boost' to diamond trade as Antwerp escapes US tariffs" (België → VS "just over $2.1 billion" per jaar, geen jaar). https://www.brusselstimes.com/1764572/major-breakthrough-as-antwerp-diamond-sector-escapes-15-us-import-tariffs
[4] VRT NWS, 2025-09-25, Antwerpse diamantsector en invoertarieven (ruim 2 mld euro per jaar naar de VS, vervoer niet genoemd). https://www.vrt.be/vrtnws/nl/2025/09/25/antwerpse-diamantsector-0-procent-invoertarieven-regering-trump/
[5] Prism News, "Antwerp diamond trade lifts as US tariff exemption returns" (2,1 mld USD in 2024; alleen via zoekresultaat). https://www.prismnews.com/jewelry/diamond-jewelry/antwerp-diamond-trade-lifts-as-us-tariff-exemption-returns
[6] Wikipedia, "Brussels Airlines" (New York JFK sinds 1 juni 2012, dagelijks). https://en.wikipedia.org/wiki/Brussels_Airlines
[7] Wikipedia, "Brussels Airport" (Brussels Airlines-bestemming New York JFK; vracht 795.271 t in 2025). https://en.wikipedia.org/wiki/Brussels_Airport
[8] Wikipedia, "Brussels Airport diamond heist" (Brink's-wagen uit Antwerpen naar het toestel, vlucht naar Zürich, 2013). https://en.wikipedia.org/wiki/Brussels_Airport_diamond_heist
[9] AWDC, G7/EU-sancties-FAQ (Antwerpen = G7-authority; via ontwerp en brief `diamant-antwerpen-surat` [4]). https://www.awdc.be/g7eu-sanctions-faq
[10] IDEX, memo/artikel 37827 over beveiligd diamanttransport Diamond Office → Zaventem (Malca-Amit, Brink's, Ferrari, G4S; kluizen Brink's) — alleen zoekresultaat. https://idexonline.com/FullArticle?Id=37827
[11] Wikipedia, "John F. Kennedy International Airport" en "Diamond District, Manhattan"; ankers JFK en 47th Street uit brief `diamant-mumbai-newyork` (§3, [1][2][6][7]). https://en.wikipedia.org/wiki/Diamond_District,_Manhattan
[12] Brieven `diamant-antwerpen-surat`, `diamant-mumbai-newyork`, `diamant-ramatgan-newyork` (ankers en kopieerbare benen); satellietbeelden `v2/build-cache/satcheck/sat-diamant-antwerpen-surat-{awdc,brucargo}.png`, `sat-diamant-mumbai-newyork-{jfk-cargo,jfk-cargo-z16,47th-street}.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Recept:** `bash v2/tools/bak_stromen.sh diamant-antwerpen-newyork` (functie `bak_diamant_antwerpen_newyork`, LF). Geen wegscan, geen profiel, geen extract: b1 en b3 zijn byte-kopieën onder eigen prefix, b2 komt uit `maak_luchtbeen.py`. Uitvoer `v2/data/stroomroute-diamant-antwerpen-newyork.json`, 30,6 KB, versie 2, lonlat.

| # | modaliteit | km gebakken | punten | naad naar volgende | toets |
|---|---|---|---|---|---|
| b1 | truck | 37,4 | 435 | 0,000 km | hemelsbreed 34,4 km, geen wegkm: +8,7% als indicatie, binnen ±15% |
| b2 | lucht | 5.883,3 | 237 | 0,000 km | grootcirkel, geen bronkm; doorgetrokken |
| b3 | truck | 25,3 | 806 | — | hemelsbreed 19,2 km, geen wegkm: +31,8% als indicatie (omweg door tunnel en Van Wyck, geen norm) |

Totaal 5.946,0 km · 1.478 punten · 4 markers (dia-awdc 26 m, dia-brucargo 26 m, dia-jfk-cargo 0 m, dia-ny-47th 0 m van de lijn). Geen naad > 0 m; geen stippel, geen haven-aanloop, geen airside-stippel (beide wegbenen eindigen op de openbare weg).

- **Vlucht (b2):** grootcirkel BRU → JFK, 5.883,3 km, van het b1-eindpunt (50.9056, 4.4576) naar het b3-beginpunt (40.6587, -73.7952). Doorgetrokken; "aannemelijk: één bron" staat in de beennaam. Niet per zending gebrond, kan via een hub lopen (§7).
- **Kopieën:** b1 = `diamant-antwerpen-surat` b1, b3 = `diamant-mumbai-newyork` b3; geen tweede versie van de geometrie.
- **toets_knikken:** 6 knikken in b1 (spikes 4-50 m bij AWDC en Brucargo, geen omkeringen) en 17 in b3 met 2 terugloop-omkeringen (Kew Gardens 40.71596, -73.82839 en bij JFK); allemaal geërfd uit de kopieën, niet aangeraakt. `toets_rechte_benen --min-km 5`: geen treffer voor deze stroom.
- **Lessen:** (1) bij pure kopieketens is de bake een minuut werk: de tijd zit in het kijken of de naden kloppen. (2) Een bash-run op `bak_stromen.sh` kan tijdens parallelle edits een syntaxisfout melden na een geslaagde bake; `bash -n` achteraf was schoon, dus de fout was een half geschreven bestand van een andere agent.
