# Routebrief (licht) · diamant — Van → Via → Naar (land): Williamson (Tanzania) → Dar es Salaam → Brussel → Antwerpen

**stroom-id:** `diamant-williamson-antwerpen` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** ruwe diamant van de Williamson-mijn (Mwadui, Kishapu, Shinyanga; Pink Diamonds/Taifa Group + Tanzaniaanse
staat) gaat per **truck** (T8 → T3 → T1, de Centrale Corridor) naar de vrachtapron van Julius Nyerere Intl Airport (DAR), per
**vrachtvlucht** (grootcirkel, aannemelijk) naar Brucargo op Brussels Airport (BRU) en per **truck** (E19) naar het AWDC/Diamond Office
in Antwerpen, waar de Bonas-tenders worden gehouden.
**Welke as van het verhaal:** de enige Oost-Afrikaanse diamantmijn: klein volume, hoge waarde per karaat. **~0,4 Mct/j** (≈50.000 ct per
productiecyclus × 8 cycli) [1]; de sitelaag heeft 0,15 Mct (resttoewijzing, onzeker). Roze stenen tot circa 700.000 USD/ct [4].
Peiljaar 2026. De route mijn → DAR is **nergens gebrond** (zie §7).

## 1 · Ketenkaart
```
Williamson-plant, Mwadui `dia-williamson-plant` ──(b1 truck · T8 → T3 → T1 · ~1.005 km wegkm, webcheck 1.020)──►
Julius Nyerere Intl (DAR), vrachtapron `dia-dar-vrachtplatform` ──(b2 lucht · grootcirkel DAR → BRU · 7.235 km, aannemelijk)──►
Brucargo, Brussels Airport `dia-brucargo` (hergebruikt) ──(b3 truck · E19 · 44,7 km, letterlijke kopie)──►
AWDC/Diamond Office, Antwerpen `dia-awdc` (hergebruikt) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `dia-williamson-plant` → `dia-dar-vrachtplatform` | T8 (Mwadui–Nzega) → T3 (Nzega–Igunga–Singida–Manyoni–Dodoma–Morogoro) → T1 (Morogoro–Chalinze–Dar) | **1.005** = som van drie Wikipedia-plaatsopgaven (Shinyanga–Singida 300 + Singida–Dodoma 252 + Dodoma–Dar 453) [5][6][7]; webcheck OSRM 1.020,5 (T8 100 · T3 716 · T1 182) [10]; hemelsbreed 723,5 | maak_stroombeen_weg (nieuw profiel) | nee; eindstuk DAR: korte stippel (§3, airside) |
| b2 | B | lucht | `dia-dar-vrachtplatform` → `dia-brucargo` | vlucht DAR → BRU, grootcirkel (aannemelijk: één bron noemt alleen "DAR-luchthaven → Antwerpen") | 7.235,0 grootcirkel (berekend) | maak_luchtbeen | nee, doorgetrokken |
| b3 | C | truck | `dia-brucargo` → `dia-awdc` | E19 via Mechelen | 44,7 (kopie van `diamant-ekati-antwerpen` b3, 787 punten) | letterlijke kopie | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-williamson-plant` | mijn/plant (kop) | Williamson Diamonds, verwerkingsplant aan de westrand van de pit, Mwadui | -3.5213, 33.6031 | [1][4][11] | bron-gelegd (z16 gezien: staalconstructie met transportbanden en een tank op de westrand van de open pit, grijze tailings ten westen, haulweg naar het westen; Mwadui-dorp ligt 2 km ZW) |
| `dia-dar-vrachtplatform` | vrachtterminal (lucht) | Julius Nyerere Intl (DAR), "Cargo Apron" + vrachtloods | -6.8695, 39.2057 | [9][11] | bron-gelegd (z16 gezien: wit gedekte loods direct naast het apron west van Terminal 2/3; OSM-way 135694161 `ref=Cargo Apron` ligt op dit punt). Airside: zie hieronder |
| `dia-brucargo` | vrachtterminal (lucht) | Brucargo, Brussels Airport | 50.90628, 4.45584 | `diamant-ekati-antwerpen.md` §3 (letterlijk hergebruikt) | bron-gelegd (daar z15 gezien) |
| `dia-awdc` | handels-/tenderhub (eind) | AWDC/Diamond Office, Hoveniersstraat, Antwerpen | 51.21520, 4.41870 | `diamant-ekati-antwerpen.md` §3 (letterlijk hergebruikt) | bron-gelegd als hub; dat deze Bonas-tender daar viewt: aannemelijk (alleen "Antwerpen" gebrond [1][2]) |

Sitelaag: `w-williamson` staat op -3.5167, 33.5833 (status onzeker) = **2,3 km** west-noordwest van de plant, in Mwadui-dorp (z14 gezien: woonwijk); niet door mij gewijzigd, centraal gelijktrekken met `dia-williamson-plant`.
**Airside-patroon (DAR):** het vrachtplatform ligt airside (geen wegpad tot het apron). Het wegbeen eindigt op de dichtstbijzijnde openbare weg (de luchthaventoegangsweg ~0,4 km west van het anker); sluit af met `--stippel "truck|DAR-vrachtplatform last mile (schematisch — airside/privéterrein)|<weg-eind>|-6.8695,39.2057"`. Ligt het weg-eind ≤ 0,5 km van het anker en gaat het been er gewoon heen, dan vervalt de stippel.

## 4 · Via-punten (alleen b1; b2 is lucht, b3 is de kopie). Allemaal van OSRM/OSM-wegmanoeuvres (óp de doorgaande weg), buiten stadscentra
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | T8-vork ten O van Shinyanga | -3.6099, 33.5337 | T8 rechtdoor naar Nzega i.p.v. links naar Shinyanga-stad (keuze Mwadui–Nzega: 90 km T8 direct, geen stadsdoorkruising) |
| b1 | 2 | T3, Nzega-oost (rotonde) | -4.2164, 33.2243 | Nzega: T8 gaat over in T3; pint de route op de doorgaande weg ten O van de stad |
| b1 | 3 | T3, Igunga-west | -4.2941, 33.7731 | sluit het alternatief Nzega–Tabora–Itigi–Manyoni uit; Nzega–Igunga–Singida (146 km rechtdoor) |
| b1 | 4 | T3, 15 km ten N van Singida | -4.6846, 34.6864 | pint de Igunga-aanvoer (en sluit de Meatu-variant uit) vóór het stadscentrum van Singida |
| b1 | 5 | T3, Dodoma-oost | -6.1408, 35.9036 | na Dodoma door op T3 richting Morogoro (240 km); geen route door het centrum nodig |
| b1 | 6 | T1, Morogoro-oost ("Dar es Salaam Road") | -6.7878, 37.7307 | verlaat Morogoro op de T1 oostwaarts; geen sluipweg door het centrum |
| b1 | 7 | T1, Chalinze-vork | -6.6382, 38.3523 | splitsing T1 (Dar) / T13 (Segera-Tanga): corridorkeuze; T1 naar Dar |

Profiel (lon, lat; eerste en laatste = ankers): refs `["T8","T3","T1"]`, extract `["tanzania"]`, `gepubliceerdKm` 1005, `vensterKm` 75 (de weg wijkt tot ~150 km van de grootcirkel af), eindzone: DAR-toegangsweg (service/unclassified).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Williamson-plant (Mwadui) | Pink Diamonds (Taifa Group) met Tanzaniaanse staat | kimberliet → ruwe diamant (roze stenen: tot 700.000 USD/ct) | ~0,4 Mct/j (8 cycli × 50.000 ct) | [1][3][4] |
| AWDC/Diamond Office / tendervenster Bonas | AWDC; Bonas Group (verkoopkanaal) | rough → tender (viewing in Antwerpen, bv. WDL-2606 sluit 6-11-2026) → koper | n.v.t. (handel/certificering) | [1] |

## 6 · Stoppunt
De brief stopt bij het AWDC/Diamond Office: het verkoopkanaal van Williamson-rough is een Antwerpse tender (Bonas), en geen bron noemt een
vervolgbestemming (slijperij) per partij; fase D/E vervallen.

## 7 · Open punten
- **Route mijn → DAR is niet gebrond.** Reuters/EastAfrican (2017) bevestigen alleen dat Williamson-rough via de hoofdluchthaven van Dar es Salaam naar Antwerpen werd geëxporteerd [2]; niets zegt hoe het van Mwadui naar DAR komt (weg ~1.000+ km óf eigen luchtbrug). Mwadui heeft een luchthaven (OSM-node -3.5000, 33.6170, runway langs de oostrand van de pit [9]) maar **geen bron noemt een vlucht Mwadui → DAR**: daarom truck, de vlucht blijft ongetekend.
- **b2 is aannemelijk:** geen bron noemt een directe vlucht DAR → BRU; DAR heeft geen vrachtlijn naar Europa in de Wikipedia-lijst (Air Tanzania Dubai/Mumbai/Kinshasa; Astral/Kenya Airways Nairobi) [8]; een echte tussenlanding (DXB/ADD/NBO/AMS) is niet gebrond. Eén grootcirkel aangenomen (bakhandleiding §2).
- **b1-km is een som van plaatsopgaven**, geen gepubliceerde routelengte; Wikipedia noemt ook Shinyanga–Dodoma 475 km [5] (andere route, 928 totaal). De ±15%-toets (855–1.155) is dus een indicatie. De route volgt OSRM/OSM (T8 → T3 → T1) en gaat NIET door Shinyanga-stad.
- **Eigendom:** Petra verkocht (7-2-2025) zijn volledige belang aan Pink Diamonds Investments (Taifa, tot USD 16 mln) [3]; afronding en het staatsaandeel niet bevestigd; bij Bonas staat de mijn per 2025 op Pink Diamonds [1]. Productie klein en laagvoorspelbaar; peiljaar 2026 = één bron.
- **Het exacte tender-/handelsadres in Antwerpen** (Bonas-kantoor) is niet gevonden; anker `dia-awdc` blijft het generieke hubanker.
- **DAR-vrachtplatform:** geen vrachtterminal-operator aangewezen; anker is het OSM-"Cargo Apron" + loods (site-niveau).

## 8 · Bronnen
[1] Bonas Group, Williamson-mijn (±50.000 ct per cyclus, 8 cycli, eigenaar Pink Diamonds sinds 2025, tender WDL-2606, viewings Antwerpen), https://www.bonasgroup.com/en/miners/show/williamson
[2] Reuters, "Tanzania says to nationalise diamond consignment seized from Petra" (2017; via zoekresultaat samengevat: 71.654 ct, DAR-luchthaven → Antwerpen), https://www.reuters.com/article/business/finance/tanzania-says-to-nationalise-diamond-consignment-seized-from-petra-diamonds-idUSKCN1BK0T2/ · EastAfrican, https://www.theeastafrican.co.ke/tea/business/petra-suspends-mining-after-diamonds-seizure-by-tanzania-1373672 · Rapaport, https://rapaport.com/news/petra-halts-williamson-mine-after-diamond-seizure/
[3] Engineering News/Mining Weekly, "Petra's entire interest in Williamson headed for Tanzania's Pink Diamonds" (2025-02-07), https://www.engineeringnews.co.za/article/petras-entire-interest-in-williamson-headed-for-tanzanias-pink-diamonds-2025-02-07
[4] Wikipedia, "Williamson diamond mine" (23 km NO van Shinyanga, -3.5167/33.6, >19 Mct sinds 1940, roze stenen tot 700.000 USD/ct [Guardian 2020]), https://en.wikipedia.org/wiki/Williamson_diamond_mine
[5] Wikipedia, "Shinyanga" (475 km over de weg ten NW van Dodoma; 175 km van Mwanza), https://en.wikipedia.org/wiki/Shinyanga
[6] Wikipedia, "Singida" (Singida–Dodoma 252 km, –Shinyanga 300 km), https://en.wikipedia.org/wiki/Singida
[7] Wikipedia, "Dodoma" (453 km ten W van Dar es Salaam, 260 km van Morogoro), https://en.wikipedia.org/wiki/Dodoma
[8] Wikipedia, "Julius Nyerere International Airport" (vracht 29.088 t in 2024; vrachtbestemmingen Dubai, Kinshasa, Lubumbashi, Mumbai, Nairobi), https://en.wikipedia.org/wiki/Julius_Nyerere_International_Airport
[9] OpenStreetMap (ODbL) via Overpass/Nominatim — way 135694161 (`aeroway=apron`, `ref=Cargo Apron`, -6.8695/39.2057); node "Mwadui Airport" (-3.5000/33.6170). https://www.openstreetmap.org
[10] OSRM-demo (OSM-gebaseerd, webcheck, geen gepubliceerde bron), `router.project-osrm.org`, route plant → DAR-anker 1.020,5 km via T8/T3/T1.
[11] Esri World Imagery via `v2/tools/sat_check.py` (live) — `v2/build-cache/satcheck/sat-diamant-williamson-antwerpen-{mwadui,mwadui-plant,mwadui-plant2,dar-cargo}.png`.
[12] `v2/design/routebrieven/diamant-ekati-antwerpen.md` (ankers Brucargo/AWDC, b3 E19) · `design/diamant.md`, `data/diamond.js`, `v2/design/diamant-sitelaag.json` (`w-williamson`).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
Recept: `bash v2/tools/bak_stromen.sh diamant-williamson-antwerpen` (functie `bak_diamant_williamson_antwerpen`) → `v2/data/stroomroute-diamant-williamson-antwerpen.json`
(versie 2, lonlat, 205,4 KB, 3 benen · 10.597 punten · **8.298,9 km** · 4 markers). Ketenid noemt het werkelijke eindpunt (Antwerpen); geen afwijking van het ontwerp.

| # | modaliteit | km gemeten | km brief | naad | beschrijving |
|---|---|---|---|---|---|
| b1 | truck | **1.019,2** (9.519 pt) | 1.005 (som plaatsopgaven) · OSRM-webcheck 1.020,5 | — | Williamson-plant → DAR-vrachtapron, T8 → T3 → T1; **+1,4%** t.o.v. 1.005, −0,1% t.o.v. de webcheck |
| b2 | lucht | **7.235,0** (291 pt) | 7.235,0 | 0,000 km | vlucht DAR → BRU, grootcirkel, doorgetrokken (aannemelijk: één bron) |
| b3 | truck | **44,7** (787 pt) | 44,7 | 0,000 km | letterlijke kopie van `diamant-ekati-antwerpen` b3 (E19), zelfde beennaam als `bak_diamant_namdeb_gaborone` |

Alle drie de benen zijn doorgetrokken: **geen stippel, geen haven-aanloop** (er is geen zeebeen, dus geen MARNET). Markers: alle vier op 0,000 km van de lijn.

**b1, het wegbeen.** `--bron overpass` (pyosmium is geblokkeerd). De standaard-Overpass-vraag van het tool (alle `highway`-ways in de bbox van het hele corridorvenster, ±6° × 3,5°) was voor de mirrors te zwaar (HTTP 500/504 en afgebroken verbindingen, ook op een triviale test), dus draaide ik `maak_stroombeen_weg.py` via een wrapper in de scratchpad die dezelfde `main()` en dezelfde `weg_houden()` gebruikt maar het wegnet in 37 tegels van 0,75° ophaalt (alleen de WEG_HOUD-klassen motorway t/m primary/secondary + links) plus de kleine eindklassen (residential/service/tertiary/unclassified) in 13 km-vensters rond plant en DAR-anker. Alleen `maps.mail.ru` gaf antwoord; de tegels zijn lokaal gecachet. De graaf bevat 34.629 ways. Alle snaps ≤ 0,08 km; alle zeven via-punten snappen op ≤ 0,01 km, dus geen één is fout gelegd. Segmenten: plant → T8-vork 15,8 · → Nzega 95,7 · → Igunga 63,3 · → Singida-noord 130,2 · → Dodoma-oost 279,5 · → Morogoro-oost 248,5 · → Chalinze 75,4 · → DAR 110,9 km.
- **First mile:** 5,15 km over kleine klassen (OSM-wegen zonder naam bij Mwadui, als in de brief voorspeld: de T8-aansluiting op −3.5245, 33.5589); plant → eerste weg 0,08 km. Geen last-mile-stippel nodig.
- **Last mile (DAR):** het weg-eind valt **0,04 km** van het anker (≤ 0,5 km), dus de brief-regel "stippel vervalt" geldt. De laatste 0,74 km loopt over OSM-`service`-wegen langs de vrachtloodsen en maakt een lus van ~0,4 km naar het ZW van het anker. Dat die wegen openbaar zijn is niet vastgesteld (op de satelliet liggen ze tussen de hangars en de cargoloods); is het airside, dan is dit laatste stuk net als bij de andere luchthavens een schematisch stuk zonder wegbewijs. Bevinding, niet verholpen.
- **Knikken:** `toets_knikken` meldt 28 scherpe knikken op b1 (3–73 m straal), allemaal junctievertices van de luchthavenwegen en de ankerstubs; 0 omkeringen, 0 terugloop. De ruim 17 knikken in het deel dat uit b3 komt (Brucargo/Mechelen) zijn de al bekende van `diamant-ekati-antwerpen`.
- **Lengtetoets:** 1.019,1 km (na 20 gesnoeide keerlussen van ≤ 0,03 km) tegen 1.005 = +1,4% [OK]; ligt binnen ±15% (855–1.155), maar de 1.005 is een som van plaatsopgaven, dus dit is een indicatie. De OSRM-webcheck (1.020,5) en onze gemeten 1.019,2 liggen 1,3 km uit elkaar: dezelfde OSM-weg onder twee routers, geen onafhankelijke bevestiging.

**b2, de vlucht.** `maak_luchtbeen.py --van 'DAR-vrachtplatform|-6.8695,39.2057' --naar 'Brucargo BRU|50.90628,4.45584'` gaf 7.235,0 km over 291 punten, precies de berekende waarde in de brief. Eén grootcirkel, geen tussenlanding (geen bron noemt er één), met "aannemelijk: één bron" in de beennaam en niet in de lijnstijl. De bol tilt het been zelf op (`stroomstijl.js`).

**b3, de kopie.** Hetzelfde bestand en dezelfde beennaam als `bak_diamant_namdeb_gaborone`; niet opnieuw gerouteerd, dus geen extract `belgie` nodig.

**Lessen.** (1) Bij een corridor van meer dan 6° breed is de ene Overpass-vraag over de hele bbox onhaalbaar: tegel hem en cache de antwoorden. (2) Een wegbeen met een via-punt per corridorkeuze (zeven) en zachte refs T8/T3/T1 reproduceerde de OSRM-lengte binnen 0,1%, zonder dat een via-punt bijgeschoven hoefde te worden. (3) Open punten uit §7 veranderen niet door de bake: de route mijn → DAR blijft ongebrond, b2 blijft aannemelijk, en de sitelaag `w-williamson` (−3.5167, 33.5833) ligt nog 2,3 km van de plant en moet centraal gelijkgetrokken worden.
