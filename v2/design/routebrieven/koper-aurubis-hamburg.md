# Routebrief (licht) · koper — Antofagasta → Brunsbüttel → Aurubis Hamburg → Emmerich

**stroom-id:** `koper-aurubis-hamburg` · **geschreven:** 2026-09-24 · **werkwijze:** licht (M29) · **status:** concept · **Linear:** LAR-563
**Keten in één zin:** Chileens koperconcentraat (Codelco-district Antofagasta, aannemelijk) per bulkcarrier van Puerto Antofagasta (ATI) naar de **Elbehafen Brunsbüttel**, daar gelost, opgeslagen en voorgemengd, per **binnenschip-shuttle** (Schramm, twee 98 m-schepen) ~79 km de Elbe op naar de concentraatkade van **Aurubis Werk Ost** aan het Müggenburger Kanal, in Hamburg gesmolten en geraffineerd tot kathode (~400 kt Cu/j), en als Grade-A-kathode per **spoor** (aannemelijk) ~420 km naar de gietwalsdraadfabriek **Deutsche Giessdraht, Emmerich** — stoppunt: gietwalsdraad.
**Welke as van het verhaal:** de Europese raffinage-as — Zuid-Amerikaans concentraat (Aurubis noemt zelf Chili, Peru, Brazilië [4]) naar Europa's grootste primaire smelter. Jaarvolume: Hamburg zette **0,9–1,3 Mt concentraat/j** in (kalenderjaren 2019–2024: 1,04 · 1,30 · 1,23 · 1,00 · 1,19 · 0,91 Mt [4][5]); de Brunsbüttel-shuttle droeg **>11 Mt in 2007–2017** [1]. Aandeel Chili niet gepubliceerd (Peru 16 % op concernniveau, 2020/21 [7]).

*Correctie op de opdrachtpremisse: de zeeschepen lossen **niet** aan een Aurubis-kade in Hamburg en er wordt ook niet gelichterd — Aurubis schrijft zelf dat de concentraten voor Hamburg "vornehmlich auf dem Seeweg" komen en "über das Hafenterminal in Brunsbüttel umgeschlagen" worden, mét voormenging aldaar [4][5]. Het is een volledige extra overslag (zee → opslag → binnenschip), dus twee benen tussen zee en smelter.*

## 1 · Ketenkaart
Puerto Antofagasta / ATI ──(b1 zee · Panama · ~13.600 km)──► Elbehafen Brunsbüttel ──(b2 binnenvaart · Unterelbe/Norderelbe · ~79 km)──► Aurubis Werk Ost, kade Müggenburger Kanal
──(smelter + raffinaderij Hamburg, ~400 kt Cu/j)──► kathode ──(b3 spoor · Rollbahn + Hollandstrecke · ~420 km, aannemelijk)──► Deutsche Giessdraht Emmerich ──► gietwalsdraad 8 mm (STOP)
  ├── vertakking, niet getekend: Europees schroot per truck → Aurubis Lünen (secundaire hütte, anodes/kathodes [13]) — geen herkomst-anker, dus geen been; wél site-anker (gloed)
  └── vertakking bij de bron, niet getekend: Aurubis koopt óók in Peru, Brazilië, Bulgarije, Georgië, Canada [4] — Antofagasta is één van meerdere herkomsthavens (§7)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `cu-antofagasta-kade` → `cu-brunsbuettel-kade` | Panamakanaal (searoute-referentie; geen gepubliceerde havenafstand gevonden) | ~13.596 (searoute, referentie) | MARNET kade→kade | Elbe-monding → kademuur: waarschijnlijk `maak_havenaanloop.py` |
| b2 | C | binnenvaart | `cu-brunsbuettel-kade` → `cu-hamburg-konzentratkade` | Unterelbe → Norderelbe → Müggenburger Kanal | ~79 (Elbe-km 695 → 618,4 [14] + ~2 km kanaal) | `maak_rivierbeen.py` over de bulklaag (Elbe ≠ Rijn/Mississippi; eigen-collector-tracks Unterelbe als check) | nee |
| b3 | D | spoor (aannemelijk: één bron per uiteinde, geen bron voor de modaliteit zelf) | `cu-hamburg-werkost` → `cu-emmerich-dg` | Rollbahn Hamburg–Bremen–Osnabrück–Münster–Wanne-Eickel → Oberhausen → Hollandstrecke Oberhausen–Wesel–Emmerich | ~420 (355 [15] + ~18 + ~55 [16], afgeleid) | `toets_spoorroute.mjs` via-punt → via-punt | alleen als het 1-op-1-net de DG-aansluiting [12] mist: stippel "last mile (geen net)" naar het site-anker |

Volgordebewijs b1→b2: Hamburg lost de shuttle "per Kran" en voert het concentraat "über Förderbandanlagen zum Lager" [1]; de kraan (Kocks Ardelt, 16 t / 27 m, 2016) staat "auf dem Betriebsgelände der Aurubis AG am Müggenburger Hauptdeich" [2][3]; de Kaja Josephine lost "am Kai des Müggenburger Kanals" [18].

## 3 · Ankers (één per site en per overslag; 4 decimalen, lat, lon)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-antofagasta-kade` | herkomstkade / laadplek | Puerto Antofagasta, frente 2 (ATI, sitios 4–7), molo-binnenzijde | -23.6500, -70.4088 | [8][9] | bron-gelegd (z16 gezien: bulkcarrier aan de binnenzijde van de molo; welk sitio het concentraat laadt is open) |
| `cu-brunsbuettel-kade` | overslag zee → binnenschip | Elbehafen Brunsbüttel, droge-bulkkade (Brunsbüttel Ports) | 53.8878, 9.1740 | [1][14] | bron-gelegd (z16 gezien: kademuur met havenkranen, zeeschip aan de kade, stockpiles en loodsen erachter) |
| `cu-hamburg-konzentratkade` | losplek concentraat | Aurubis Werk Ost, kade Müggenburger Kanal (ZW-oever) | 53.5163, 10.0418 | [2][3][18] | bron-gelegd (z17 gezien: verharde kade met kraanachtige structuur aan de Werk-Ost-oever; reverse-geocode: Müggenburger Straße — overkant = Hovestraße) |
| `cu-hamburg-werkost` | smelter + raffinaderij (terrein) | Aurubis Hamburg, Werk Ost | 53.5140, 10.0400 | [4][6] | bron-gelegd (z15 gezien: hüttecomplex met schoorsteen, zuurfabriek en rangeerterrein) |
| `cu-emmerich-dg` | fabriek | Deutsche Giessdraht GmbH, Kupferstraße 5, Emmerich | 51.8284, 6.2630 | [10][11][12] | bron-gelegd (z16/z17 gezien: fabriekshallen met kade-apron aan de Löwenberger Landwehr, binnenschip afgemeerd ernaast) |
| `cu-luenen-terrein` | vertakking (alleen gloed) | Aurubis Lünen, Kupferstraße 23 | 51.6040, 7.5087 | [13] | bron-gelegd (z15 gezien: hütte met schoorstenen aan het Datteln-Hamm-Kanal) |

## 4 · Via-punten (alleen b3 spoor — corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | Bremen Hbf | 53.0832, 8.8137 | Rollbahn via Bremen i.p.v. Hannover–Ruhr |
| b3 | 2 | Osnabrück Hbf | 52.2729, 8.0616 | Rollbahn doorzetten naar Münster, niet via Löhne/Hamm |
| b3 | 3 | Münster Hbf | 51.9565, 7.6350 | Rollbahn (Haltern–Wanne-Eickel), niet Westmünsterland/Coesfeld |
| b3 | 4 | Oberhausen Hbf | 51.4738, 6.8520 | instap Hollandstrecke, niet via Duisburg/Nederland |
| b3 | 5 | Wesel | 51.6559, 6.6262 | pint de Hollandstrecke Wesel–Emmerich (geen Bocholt-tak) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Elbehafen Brunsbüttel (overslag + opslag + voormenging, geen smelten) | Brunsbüttel Ports GmbH / Schramm-groep, 20-jaarscontract sinds 2007/08 | zeeschip-concentraat → gemengd concentraat op binnenschip | >11 Mt cumulatief 2007–2017 (~1,1 Mt/j); schepen 98 × 14 m, 3 m diepgang | [1][17] |
| Aurubis Hamburg (primaire smelter + raffinaderij) | Aurubis AG | concentraat 0,9–1,3 Mt/j → kathode (~400 kt Cu/j), zwavelzuur, ijzersilicaat | zie in→uit; 2.800+ medewerkers | [4][5][6] |
| Deutsche Giessdraht Emmerich (gietwalsdraad, Southwire-proces) | Aurubis AG (100 % sinds 2018/19; daarvoor JV Aurubis 60 / Codelco 40) | Grade-A-kathode → gietwalsdraad 8 mm | ~240 kt/j productie (2018), tot 300 kt/j capaciteit | [10][11] |

## 6 · Stoppunt
De brief stopt bij het gietwalsdraad in Emmerich: de enige gedocumenteerde afnemer is Prysmian (langjarig walsdraadcontract, sept. 2026, met Emmerich in de datumregel [19]) — een bedrijf, geen fabriek met adres, dus geen fase E-been.

## 7 · Open punten
- **Herkomsthaven/-divisie is aannemelijk, niet gedocumenteerd:** Codelco/Chuquicamata wordt als Aurubis-leverancier genoemd [7] en Codelco is 48 % van de concentraatverschepingen in Antofagasta (303 kt, 2013 [8]) — maar welke Chileense haven (Antofagasta/Mejillones/Ventanas) Aurubis bedient, publiceert niemand; alleen deze ene zeetak wordt getekend.
- **Concentraatkade Hamburg:** oever bevestigd door bron + reverse-geocode; de kraan zelf is op z17 niet eenduidig — 110 m verderop ligt een tweede kraanachtige structuur op de Hovestraße-oever (53.5171, 10.0428). Site-niveau volstaat (licht).
- **Gaan er óók zeeschepen rechtstreeks naar Hamburg?** Aurubis zegt "vornehmlich" via Brunsbüttel [4]; een rechtstreeks aandeel is niet gevonden en wordt niet getekend.
- **Modaliteit b3 ongedocumenteerd:** spoor gekozen op infrastructuurbewijs (Werk-Ost-emplacement op z15; DG-kade met Bahnanschluss [12]). Alternatieven: truck 381 km via A1–A43–B67–A3 (OSRM-referentie) of binnenschip via de DG-kade (Rijn-km ~848–854 [12]) vanuit Olen/Rotterdam. Actualiteit van de DG-spooraansluiting in [12] onbekend.
- **Gepubliceerde zeeafstand ontbreekt** — 13.596 km is een searoute-referentie (zelfde MARNET-familie als onze router, dus geen onafhankelijke toets).
- **Lünen-streng:** schroot heeft geen herkomst-anker → geen stippel getekend (een markt-centroïde is geen anker); Lünen → Emmerich (kathode) is niet gedocumenteerd.

## 8 · Bronnen
[1] Hafen Hamburg, 2017-04-03, "Über 5.000 Binnenschiffe mit Kupfererzkonzentrat beladen", https://www.hafen-hamburg.de/de/presse/news/ueber-5000-binnenschiffe-mit-kupfererzkonzentrat-beladen-35163/
[2] Hafen Hamburg, 2016-11-24, "Brunsbüttel Ports investiert rund 3 Mio. Euro in Hamburg" (kraan op het Aurubis-terrein am Müggenburger Hauptdeich; 16 t / 27 m / 230 t), https://www.hafen-hamburg.de/de/presse/news/brunsbuettel-ports-investiert-rund-3-mio-euro-in-hamburg-34959/
[3] THB, 2016, "Logistik für Aurubis: Neuer Kran greift zu" (Kocks Ardelt; Sophia Soraya / Kaja Josephine), https://www.thb.info/rubriken/maritime-logistik/detail/news/logistik-fuer-aurubis-neuer-kran-greift-zu.html
[4] Aurubis, Umwelterklärung 2022 (p. A-5: herkomstlanden + Brunsbüttel; p. B-65: inzet Standort Hamburg 2019–2021), https://www.aurubis.com/dam/jcr:ba791056-324c-4066-bf17-21ad1fc5d9db/2022_Umweltbericht_DE.pdf
[5] Aurubis, Environmental Statement 2025 (p. 4; p. B-61: input Hamburg site 2022–2024), https://www.aurubis.com/en/dam/jcr:8c6612ef-46af-4014-8e45-dee818f8aa03/2025-Umweltbericht_EN.pdf
[6] Aurubis, Umweltschutz am Standort Hamburg (~400.000 t Reinkupfer/j), https://www.aurubis.com/de/verantwortung/umwelt-energie-und-klima/umweltschutz-an-den-standorten/umweltschutz-am-standort-hamburg
[7] FDCL/Misereor, persbericht 2023-02-15 (Codelco/Chuquicamata als leverancier; Peru 16 %), https://www.fdcl.org/pressrelease/2023-02-15-ignoriert-aurubis-umweltzerstoerung-durch-kupferminen-in-suedamerika/
[8] MundoMaritimo, 2014-05-09, "48% de los embarques de concentrados son de Codelco en Puerto Antofagasta" (303 kt Cu-concentraat 2013, aanvoer per truck), https://www.mundomaritimo.cl/noticias/48-de-los-embarques-de-concentrados-son-de-codelco-en-puerto-antofagasta
[9] Hanseatic Global Terminals, ATI (sitios 4-5, 6, 7 op frente de atraque 2; concentraatloods RAEC), https://latinamerica.hanseaticglobalterminals.com/business-area-section/port-terminals/ati/
[10] Aurubis, persbericht 2018-01-22, overname Codelco-aandeel Deutsche Giessdraht (240 kt/j; JV 60/40), https://www.aurubis.com/en/media/press-releases/press-releases-2018/aurubis-acquires-codelco-s-shares-in-deutsche-giessdraht
[11] Aurubis, Environmental protection at Deutsche Giessdraht (tot 300 kt/j; smelten-gieten-walsen), https://www.aurubis.com/en/responsibility/environment-energy-and-climate/environmental-protection-at-the-sites/environmental-protection-at-dg
[12] Wikipedia (de), Hafen Emmerich (DG-kade Löwenberger Landwehr: 110 m, eigen Drehkran, Bahnanschluss tot op de pier; Rijn-km 847,5–853,8), https://de.wikipedia.org/wiki/Hafen_Emmerich
[13] Aurubis, Sites (Lünen: complexe recyclingmaterialen → anodes/kathodes; Emmerich: gietwalsdraad), https://www.aurubis.com/en/about-us/group/sites
[14] Elbe-km: Lotsenbrüderschaft Elbe, Brunsbüttel ≈ km 695, https://www.elbe-pilot.de/cms/brunsbuettel/ · rudern.de Gewässerkatalog Norderelbe (toegang Peutehafen/Müggenburger Kanal km 618,4), https://gewaesser.rudern.de/norderelbe
[15] Wikipedia (de), Bahnstrecke Wanne-Eickel–Hamburg ("Rollbahn", 355 km), https://de.wikipedia.org/wiki/Bahnstrecke_Wanne-Eickel%E2%80%93Hamburg
[16] Wikipedia (de), Bahnstrecke Oberhausen–Arnhem ("Hollandstrecke", 92 km), https://de.wikipedia.org/wiki/Bahnstrecke_Oberhausen%E2%80%93Arnhem
[17] Hans Schramm, Inland water vessel (sinds 2008 concentraat voor Aurubis, 20 jaar), https://www.hans-schramm.com/inland-water-vessel.html · Hafen Hamburg, Kaja Josephine (98 × 14 m, 3 m), https://www.hafen-hamburg.de/de/schiffe/kaja-josephine-27669/
[18] bildarchiv-hamburg.com, foto "Kaja Josephine – Güterumschlag am Kai des Müggenburger Kanals", https://bildarchiv-hamburg.com/photo/bagger-loescht-eine-ladung-schuettgut-binnenschiff-kaja-josephine-gueterumschlag-uWiDy87uhE
[19] Aurubis Newsroom, 2026-09-06, "Prysmian and Aurubis deepen strategic partnership with landmark long-term copper agreement" (Hamburg/Lünen/Stolberg/Emmerich), https://www.aurubis.com/en/
[20] Aurubis–Codelco, persbericht 2024-02-13 (langjarige grondstofpartnerschap), https://www.aurubis.com/en/media/press-releases/press-releases-2024/Aurubis-and-codelco-drive-innovation-for-sustainability-in-the-copper-industry-working-together-for-more-metals-from-responsible-production
Referentiegereedschap (geen bron): OSRM weg Werk Ost → DG 380,8 km (A1 214 · A1 59 · A43 20 · B67 46 · A3 11); searoute zee 13.596 km. Satellietbeelden: `v2/build-cache/satcheck/sat-{antofagasta-kade,brunsbuettel-pier,aurubis-werkost-kanaalkade-z17,aurubis-hamburg-peute,dg-emmerich-kade-z17,aurubis-luenen}.png`.


## 9 · Gebakken (2026-09-25. lichte werkwijze)

**Stroom `koper-aurubis-hamburg`** → `v2/data/stroomroute-koper-aurubis-hamburg.json` — 9 benen. 14.256 km. 5 markers: zee (stippel) 101 km · zee 13.596 km · binnenvaart (stippel) 12 km · binnenvaart 64 km · spoor (stippel) 3 km · spoor 480 km.
Recept: `bak_stromen.sh` (functie voor deze stroom). Toelichting: aanloop Antofagasta 97.1 km (stippel); zeebeen MARNET 13.596 km via Panama (1.8 km van Gatún); Elbe Brunsbüttel → Hamburg over MARNET (zeevaarweg; de bulklaag valt daar in losse componenten) met stippels voor de Brunsbüttel-kade (4.0 km) en de Norderelbe → Müggenburger Kanal (8.2 km. 1:10M-kust kent de haven niet); spoor Hamburg → Emmerich 480.1 km via Rotenburg–Bremen–Münster–Oberhausen (een vrije Dijkstra koos eerst de omweg via Soltau. 160 km voor Hamburg–Bremen; met via-punt Rotenburg 113 km).
