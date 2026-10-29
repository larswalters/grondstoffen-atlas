# Routebrief (licht) · goud — Dubai (DMCC) → Dubai DXB → Milaan-Malpensa (MXP) → Valcambi (Balerna, Ticino)

**stroom-id:** `goud-dubai-valcambi` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) ·
**status:** gebakken
**Keten in één zin:** herexport-goud (baren/doré) uit de DMCC-raffinagezone in Al Quoz per truck naar de
vrachtterminal van Dubai International (DXB), per beveiligde vrachtvlucht (grootcirkel, aannemelijk: luchthaven van aankomst
niet gebrond) naar de vrachtterminal van Milaan-Malpensa (MXP), en per truck over A8/A9 en de grens bij Chiasso naar Valcambi in Balerna.
**Welke as van het verhaal:** Dubai → Ticino — de grootste goudinstroom in Zwitserland. Zwitserland importeerde in 2025 **420 t Au
(CHF 38,9 mrd)** uit de VAE, fors meer dan in 2024 [1][2]; Valcambi is volgens Swissaid de raffinaderij die vrijwel al dat
VAE-goud binnenhaalt [1]. Eerdere jaren: Comtrade 2023 VAE-export naar Zwitserland 151,9 t (USD 9,6 mrd) [3].
De Dubai-exporteur is niet gebrond: dit is de herexportknoop DMCC-zone, geen bedrijfsspecifieke levering.

## 1 · Ketenkaart
```
DMCC-raffinagezone, Gold and Diamond Park, Al Quoz `au-dmcc-refine`
  ──(b1 truck · Sheikh Zayed Rd / Al Rebat St · 23,2 km gebakken, LETTERLIJKE KOPIE goud-dubai-delhi b1)──►
DXB-vrachtterminal (Emirates SkyCargo) `au-air-dxb`
  ──(b2 lucht · vrachtvlucht DXB → MXP, grootcirkel, aannemelijk: luchthaven niet gebrond · 4.705,9 km)──►
Milano Malpensa Cargo City Sud (MXP) `au-air-mxp`
  ──(b3 truck · A8/A9 naar Chiasso · 69,1 km gebakken, OMGEKEERDE KOPIE goud-valcambi-londen b1)──►
Valcambi SA, Balerna `au-ref-valcambi` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | truck | DMCC-zone Al Quoz → DXB-vrachtterminal | Sheikh Zayed Rd → Al Rebat St/Cargo Village Rd | 23,2 gebakken; geen gepubliceerde wegkm: hemelsbreed 19,8 km, geen wegkm [berekend] | kopie goud-dubai-delhi-weg-dmcc-dxb.geojson | nee |
| b2 | B | lucht | DXB-vrachtterminal → MXP-vrachtterminal | vrachtvlucht DXB → MXP, grootcirkel (aannemelijk: luchthaven niet gebrond; alternatief ZRH 4.766 km) | 4.705,9 grootcirkel [berekend] | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | MXP-vrachtterminal → Valcambi, Balerna | A8 (Gallarate) → A9 (Lomazzo, Como) → Chiasso (grens) → Balerna | 69,1 gebakken; geen gepubliceerde wegkm: hemelsbreed 33,4 km, geen wegkm [berekend] | omgekeerde kopie goud-valcambi-londen-weg-valcambi-mxp.geojson | nee |

## 3 · Ankers (één per site en per overslag — alle vier LETTERLIJK HERGEBRUIKT)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-dmcc-refine` | laadplek (raffinage/handelszone) | Gold and Diamond Park, Al Quoz Industrial 3, Dubai (DMCC) | 25.1261, 55.2089 | [4] (brief goud-dubai-delhi) | bron-gelegd (z15 hier opnieuw gezien: loods-/kantoorcluster op een knoop van Sheikh Zayed Rd in Al Quoz Industrial 3) |
| `au-air-dxb` | overslag truck → lucht | DXB-vrachtterminal (Emirates SkyCargo) | 25.2560, 55.3434 | [4] (goud-dubai-delhi, goud-olimpiada-dubai) | bron-gelegd (z15: vrachtloodsen aan de westkant van het platform, naast de apron met toestellen) |
| `au-air-mxp` | overslag lucht → truck | Milano Malpensa Cargo, Cargo City Sud | 45.6142, 8.7186 | [5] (goud-valcambi-londen, goud-argor-mumbai) | bron-gelegd (z15: rij vrachtloodsen met platform en toestellen aan de zuidkant van de banen; kruis ligt op de loodsen) |
| `au-ref-valcambi` | losplek / raffinaderij | Valcambi SA, Via Passeggiata 3, Balerna | 45.8385, 9.0051 | [6] (goud-loulo-ticino, goud-valcambi-londen) | bron-gelegd (hergebruikt: gebouwencomplex met zonnepanelendak N van de spoorbundel Balerna-Chiasso) |

## 4 · Via-punten (alleen kopieën: de punten zitten in de te kopiëren geojson, hier ter controle)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Trade Centre-kruispunt (Sheikh Zayed Rd) | 25.2225, 55.2867 | corridor verlaat Al Quoz richting Deira/Garhoud (uit goud-dubai-delhi) |
| b1 | 2 | Al Garhoud-kruising | 25.2436, 55.3364 | laatste keuze voor de vrachtterminal-toegangsweg |
| b3 | 1 | Gallarate (A8) | 45.6599, 8.7932 | pint de A8-tak (omgekeerd) |
| b3 | 2 | Lomazzo (A9/A8-knooppunt) | 45.7000, 9.0333 | splitsing A9/A8 |
| b3 | 3 | Como (A9) | 45.8167, 9.0833 | A9 langs het Comomeer |
| b3 | 4 | Chiasso (grens CH-IT) | 45.8333, 9.0333 | enige grensovergang |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Valcambi (Balerna) | Valcambi SA | goud uit VAE → LBMA-baren | ruim 1.000 t/j werkelijk, 2.000 t/j capaciteit [7] | [7] |

## 6 · Stoppunt
De brief stopt bij Valcambi: geen bron koppelt dit VAE-goud aan een volgende bestemming; fase D/E vervalt. De Dubai-kant
(exporteur) blijft de DMCC-zone als geheel: geen bron noemt een specifiek Dubai-bedrijf als afzender van deze lading.

## 7 · Open punten
- **Luchthaven van aankomst niet gebrond (BINDEND uit haalbaarheidstoets):** geen bron noemt MXP of ZRH voor Dubai-goud. MXP is een
  aanname (kortste weg naar Balerna: 69 km, geen Alpenpas), ZRH even denkbaar. Staat in de beennaam als "aannemelijk".
- **Vervoerswijze wél gebrond, route niet:** goud van Dubai naar Zwitserland gaat "fast ausschliesslich per Flugzeug" [8]; Dubai is de
  hub voor Zwitserland, Hongkong en India [8]. Geen bron noemt de vlucht zelf, een vluchtnummer of een tussenlanding: één directe vlucht aangenomen.
- **Exporteur niet gebrond (BINDEND):** Swissaid noemt Valcambi als importeur maar geen Dubai-raffinaderij; Valcambi zegt niet direct
  met Dubai-raffinaderijen te handelen; RTS vond geen bewijs voor een actuele Kaloti-relatie [1][9]. Startlabel: "DMCC-zone, herexport, exporteur niet gebrond".
- **Cijfers (BINDEND):** 420 t / CHF 38,9 mrd = heel 2025 [2]; 316 t (CHF 27 mrd) is alleen jan-sep 2025 [1], niet 2024. Ecofin schrijft 316 t
  aan 2024 toe: peiljaar onzeker. Het jaarvolume is de totale Zwitserse VAE-import, niet alleen Valcambi (die "bijna alles" importeert [1]).
- **Kopieën, geen nieuwe meting:** b1 (+16% tegen hemelsbreed 20 km) en b3 (-11,6% tegen een kaartschatting van 78 km) vallen buiten ±15% maar zijn
  al gebakken en bevonden in hun eigen brief; de toets is hier een indicatie. Via-punten Como/Chiasso/Lomazzo in b3 liggen in kleine steden:
  niet aangepast omdat de kopie letterlijk moet blijven.
- 2026-03: vluchten Dubai-Zwitserland verstoord door het Iran-conflict (37% vliegverkeer) [8]: geen invloed op de geometrie, wel op het jaar 2026.

## 8 · Bronnen
[1] Swissaid, "United Arab Emirates: more than ever a hub for conflict gold": 316 t / CHF 27 mrd jan-sep 2025; Valcambi importeert bijna al het VAE-goud; geen vervoerswijze. https://www.swissaid.ch/en/media/united-arab-emirates-more-than-ever-a-hub-for-conflict-gold/
[2] Swissaid-persbericht 10-09-2026 via Presseportal: 420 t, CHF 38,9 mrd in 2025, bijna het drievoudige van 2024; 38% van de VAE-goudexport naar Zwitserland. https://www.presseportal.ch/de/pm/100072962/100942267
[3] UN Comtrade (public preview API), reporter VAE (784), partner Zwitserland (757), HS 7108, export 2023: netto 151.859,7 kg, USD 9.576.237.686 (aggregaat, geen splitsing monetair/niet-monetair). https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=784&period=2023&cmdCode=7108&flowCode=X&partnerCode=757
[4] Routebrief goud-dubai-delhi (M31 golf 3): ankers DMCC (Gold and Diamond Park, OSM way 231290392) en DXB (Emirates SkyCargo, OSM way 249217154), b1-geojson. v2/design/routebrieven/goud-dubai-delhi.md
[5] Routebrief goud-valcambi-londen (M31 golf 3): MXP Cargo City Sud (OSM 45.61417/8.71859) en b1-geojson Valcambi-MXP. v2/design/routebrieven/goud-valcambi-londen.md
[6] Routebrief goud-loulo-ticino: Valcambi SA, Via Passeggiata 3 (OSM building). v2/design/routebrieven/goud-loulo-ticino.md
[7] RSI, "Viaggio tra i lingotti ticinesi": Valcambi grootste goudraffinaderij ter wereld, capaciteit 2.000 t/j, normaal ca. 1.000 t. https://www.rsi.ch/info/ticino-grigioni-e-insubria/Viaggio-tra-i-lingotti-ticinesi-risparmiati-dai-dazi-di-Trump--3146337.html
[8] Cash.ch (Reuters), 13-03-2026: Dubai centrale hub voor goud naar Zwitserland, Hongkong en India; goud vervoerd "fast ausschliesslich per Flugzeug"; Dubai-vliegverkeer 37% van normaal. https://www.cash.ch/news/top-news/goldtransporte-uber-dubai-laufen-offenbar-zum-teil-wieder-918448
[9] Le Temps, "L'or douteux de Dubai prise suisse" (via zoekresultaat, pagina zelf 403): Valcambi voornaamste Zwitserse importeur van VAE-goud, RTS-onderzoek naar MTM; ICE (juli 2025) noemt >155 t VAE-goud door Valcambi in 2024. https://www.letemps.ch/economie/lor-douteux-dubai-prise-suisse
Satellietblik (Esri z15, 2026-10-29): `v2/build-cache/satcheck/sat-goud-dubai-valcambi-dmcc.png`, `sat-goud-dubai-valcambi-dxb-cargo.png`, `sat-goud-dubai-valcambi-mxp-cargo.png`.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
Bestand `v2/data/stroomroute-goud-dubai-valcambi.json` (32,4 KB, versie 2, lonlat), functie `bak_goud_dubai_valcambi()` in `v2/tools/bak_stromen.sh`.
Titel: "Goud · Dubai (DMCC) → DXB → Milaan-Malpensa (MXP) → Valcambi (Balerna)". Totaal 4.798,2 km, 1.651 punten, 4 markers.

| # | modaliteit | km gebakken | punten | naad naar vorige | bron van de geometrie |
|---|---|---|---|---|---|
| b1 | truck | 23,2 | 478 | n.v.t. | letterlijke kopie `goud-dubai-delhi-weg-dmcc-dxb.geojson` |
| b2 | lucht | 4.705,9 | 190 | 0,00 km | `maak_luchtbeen.py`, grootcirkel DXB (25.2560,55.3434) naar MXP (45.6142,8.7186) |
| b3 | truck | 69,1 | 983 | 0,00 km | omgekeerde kopie `goud-valcambi-londen-weg-valcambi-mxp.geojson` (coordinatenlijst omgekeerd, beennaam en benen-metadata omgedraaid) |

Markers (4, allemaal 0,00 km van hun lijn): au-dmcc-refine, au-air-dxb, au-air-mxp, au-ref-valcambi; allemaal letterlijk hergebruikt.
**Recept:** `cp`-achtige kopie van b1; `maak_luchtbeen.py --van 'DXB-vrachtterminal (Emirates SkyCargo)|25.2560,55.3434' --naar 'MXP-vrachtterminal (Cargo City Sud)|45.6142,8.7186'`; b3 via een korte Python-regel (FeatureCollection, coordinaten omgekeerd); dan `bash v2/tools/bak_stromen.sh goud-dubai-valcambi`. Tussenuitvoer in `v2/build-cache/ais/graaf/goud-dubai-valcambi-{weg-dmcc-dxb,lucht-dxb-mxp,weg-mxp-valcambi}.geojson`.
**Toelichting:**
- Geen stippel, geen haven-aanloop, geen zeebeen, geen airside-stippel: beide wegankers raken het net (kopie-snaps 0,21 km bij DXB en 0,09 km bij MXP). Geen wegscan nodig, geen extract geladen.
- b2 is doorgetrokken; "aannemelijk: luchthaven niet gebrond" staat in de beennaam en de MXP-markernaam, niet in de lijnstijl. Alternatief ZRH (4.766 km) is denkbaar.
- Km-toets (indicatie, geen gepubliceerde wegkm): b1 23,2 tegen hemelsbreed 19,8 (+16%); b3 69,1 tegen kaartschatting 78 (-11,6%): b1 valt net buiten +-15%, het is een kopie uit een eerder gebakken en bevonden brief.
- `toets_knikken`: 27 knikken, 1 omkering (161,6 graden bij 25.22184,55.28260, bij het Trade Centre-kruispunt in b1; "scherpe bocht, echt"), 0 terugloop; alle in de kopieen. `toets_rechte_benen`: geen melding voor deze stroom.
**Lessen:** een keten van uitsluitend kopieen plus een grootcirkel bakt in een minuut en vraagt geen zwaar slot buiten de eindbake; bij een omgekeerde kopie ook de van/naar-metadata omdraaien zodat het bestand niet liegt.

