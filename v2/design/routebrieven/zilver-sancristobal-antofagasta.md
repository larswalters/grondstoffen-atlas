# Zilver · San Cristóbal → Ollagüe/Calama → Mejillones (land)

**stroom-id:** `zilver-sancristobal-antofagasta` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** zink-zilver- en loodzilverconcentraat van de San Cristóbal-mijn/concentrator (Minera San
Cristóbal, Nor Lípez, Potosí, Bolivia; sinds 2023 San Cristóbal Mining Inc., voorheen Sumitomo) per **spoor**
(eigen MSC-tak → Uyuni-Antofagasta-lijn/FCAB, grens bij Avaroa/Ollagüe, via Calama) naar de Mineral Concentrate
Terminal van Puerto Mejillones aan de Chileense Pacifickust — stoppunt, want de smelterbestemming is sinds de
2023-eigendomswissel niet meer gepubliceerd.
**Welke as van het verhaal:** Andes-concentraat naar de Chileense kust — landlocked Bolivia, zink-lood-
bijproduct zilver over de smalspoor-mijnlijnen van het Altiplano en de FCAB (Antofagasta plc). 2024: 338.000 t
zink-zilverconcentraat + 103.000 t loodzilverconcentraat = 441.000 t/j; Ag-gehalte zelf niet apart gepubliceerd
(zie §7).

## 1 · Ketenkaart
```
San Cristóbal-concentrator `ag-sancristobal-planta`
  ──(b1 spoor · MSC-tak, spoorwijdte 1 m, aangelegd 2005-2007 · 65 km gepubliceerd)──►
  Julaca-aansluiting (Uyuni-Antofagasta-lijn)
  ──(b2 spoor · FCAB, via grens Avaroa/Ollagüe)──►
  grens Avaroa (BO) / Ollagüe (CL)
  ──(b3 spoor · FCAB, via Calama)──►
  Mineral Concentrate Terminal, Puerto Mejillones `ag-mejillones-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | San Cristóbal-concentrator → Julaca-aansluiting | MSC-tak (eigen lijn, spoorwijdte 1 m, 2005-2007) | 65 [gepubliceerd, 1][2] | toets_spoorroute (BAKE_SUFFIX=-raw, extract bolivia) | nee |
| b2 | A | spoor | Julaca-aansluiting → grens Avaroa/Ollagüe | Ferrocarril Uyuni-Antofagasta (FCAB, Grupo México/Antofagasta plc) | geen gepubliceerde deellengte — router meet | toets_spoorroute (extract bolivia, via-punt op de grens) | nee |
| b3 | A | spoor | grens Ollagüe → Mejillones-kade | FCAB (Ferrocarril Antofagasta a Bolivia), via Calama | geen gepubliceerde deellengte — router meet | toets_spoorroute (extract chili, via Calama) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-sancristobal-planta` | mijn/concentrator (kop van het spoor) | Minera San Cristóbal — concentrator, Nor Lípez, Potosí | -21.1266, -67.2098 | [3][7] | bron-gelegd (z17 gezien: groene fabriekshallen (SAG-mill/flotatie), witte sferische tank, thickener-bekken en tailingsvijver, direct ZW van de open pit langs de toegangsweg) |
| `ag-mejillones-kade` | overslag spoor → zee | Mineral Concentrate Terminal, Puerto Mejillones (Terminal de Graneles del Norte) | -23.0598, -70.3788 | [4][7] | bron-gelegd (z16 gezien: pier van ~700 m met een afgemeerd schip, opslaggebouw en conveyortracé vanaf de kust; haven-aanloop nodig — zie §7/§9) |

## 4 · Via-punten (spoorbenen — corridorkeuze/grens)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1/b2 | 1 | Julaca-aansluiting (Uyuni-Antofagasta-lijn) | -20.9113, -67.5673 | hier voegt de MSC-tak zich bij de doorgaande Bolivia-Chili-hoofdlijn; enige geloofwaardige aansluiting in dezelfde municipio als de mijn (Colcha K), bevestigd door OSM-plaatsnaam + een zichtbare lijnkruising op satelliet [7] |
| b2/b3 | 2 | grens Avaroa (BO) / Ollagüe (CL) | -21.2833, -68.1833 | de grensovergang van de FCAB (werkwijze §6: zee/spoor-router gaat via-punt→via-punt); pint het corridorpad zodat het niet via een andere pas afwijkt |
| b3 | 3 | Calama | -22.4624, -68.9272 | de bron noemt Calama expliciet op de route van het concentraat (§8 [5]); knooppunt met de Chuquicamata-mijntak, dus een echte corridorkeuze |

## 5 · Verwerkingsknopen
(geen — de brief stopt bij de kade; er zit geen smelter/fabriek in deze keten, zie §6.)

## 6 · Stoppunt
De brief stopt bij de Mineral Concentrate Terminal in Puerto Mejillones: sinds de 2023-eigendomsoverdracht
(Sumitomo Corporation → San Cristóbal Mining Inc., Canada) is de smelterbestemming van het concentraat niet
meer gepubliceerd (vóór 2023 mogelijk Sumitomo-eigen smelters in Japan) — fase B (zee) en verder vervallen
bewust, in één zin beargumenteerd.

## 7 · Open punten
- **Ag-tonnage niet apart gepubliceerd** — MSC/Wikipedia geeft alleen concentraat-tonnages (338.000 t
  Zn-Ag + 103.000 t Pb-Ag, 2024); een oudere v1-registerraming (`design/zilver.md`, ~400 t Ag/j, "indicatief")
  is in deze sessie niet geverifieerd en dus niet als harde bron overgenomen.
- **Julaca als aansluitpunt is aannemelijk, niet bevestigd** — geen bron noemt de naam van de aansluitknoop
  expliciet; Julaca ligt in dezelfde municipio als de mijn en op de Uyuni-Antofagasta-corridor, satelliet toont
  een lijnkruising bij een klein spoorgehucht, maar een tweede onafhankelijke bron ontbreekt binnen budget.
- **Grenspunt Avaroa/Ollagüe is de dorpscoördinaat** (Wikipedia-geohack), niet de exacte spoorgrensmarkering —
  binnen budget niet nader te bepalen; als via-punt voor de router is die precisie voldoende.
- **Exacte Mejillones-pier bevestigd via nieuwsbericht + satelliet, niet via een operator-tekening** — een
  MundoMaritimo-artikel (sept. 2026) bevestigt de nieuwe Terminal de Concentrado/Mineral Concentrate Terminal
  bij Puerto Mejillones met de route Ollagüe → Calama → Mejillones; het satellietbeeld toont een pier met
  schip en conveyor op deze locatie, maar geen bron geeft de kade-coördinaat letterlijk.
- **Haven-aanloop is groot (~125 km)** — de dichtstbijzijnde MARNET-zeeknoop ligt ver uit de kust (gemeten,
  zie §9); dit is bekend gedrag voor deze kust (Antofagasta/San Antonio/Matarani-klasse uit
  `bakhandleiding-licht.md` §2, daar Mejillones al met ~136 km genoemd) en geen aanwijzing dat het ankerpunt
  fout ligt.
- **Antofagasta-haven (ATI) bewust niet gebruikt** — de haalbaarheidstoets liet de keuze open tussen
  Antofagasta en Mejillones; bronnenonderzoek (§8 [4][5]) bevestigt eenduidig dat MSC-concentraat via de
  nieuwe, speciaal gebouwde terminal in Mejillones verscheept wordt, niet via Antofagasta stad.

## 8 · Bronnen
[1] Wikipedia, "San Cristóbal mine (Bolivia)" — 65 km spoortak (aangelegd 2005-2007, milieuvergunning 2005),
2023-eigendomswissel Sumitomo → San Cristóbal Mining Inc., 2024-productie 338.000 t zink-zilverconcentraat +
103.000 t loodzilverconcentraat, 502.079 t verscheept via havenfaciliteiten in 27.134 containers.
https://en.wikipedia.org/wiki/San_Crist%C3%B3bal_mine_(Bolivia)
[2] Wikipedia, "History of rail transport in Bolivia" — MSC bouwde een 65 km-tak (spoorwijdte 1 m) van de
concentratorfabriek naar de Uyuni-Antofagasta-lijn; gemiddeld ~1.300 t zink-zilver- + ~300 t loodzilver-
concentraat/dag (oudere raming). https://en.wikipedia.org/wiki/History_of_rail_transport_in_Bolivia
[3] OpenStreetMap/Nominatim (ODbL) — landuse "Minera San Cristóbal" (-21,1153/-67,2130), municipio Colcha K,
provincie Nor Lípez, Potosí; "Julaca" plaatsknoop (-20,9113/-67,5673); "Ollagüe" plaatsknoop
(-21,2242/-68,2535). https://www.openstreetmap.org
[4] MundoMaritimo, "Puerto Mejillones realizó con éxito primer embarque de Minerales de San Cristóbal"
(sept. 2026) — eerste lading (schip Seminole Princess, ~4.000 t) vanaf de nieuwe Terminal de Concentrado de
Minerales (geopend 4 juli 2026) in Puerto Mejillones; mineraal komt per spoor aan in gesloten containers, via
gesloten galerijen naar een opslaggebouw van 124 m, verscheept via een 700 m lange gesloten tubulaire
transportband; vorig jaar 345.000 t zink-zilver- + 90.000 t loodzilverconcentraat naar Mejillones-baai.
https://www.mundomaritimo.cl/noticias/puerto-mejillones-realizo-con-exito-primer-embarque-de-minerales-de-san-cristobal
[5] MundoMaritimo, "Minera San Cristóbal opta por puerto chileno" — route: het mineraal komt Chili binnen via
Ollagüe, passeert Calama, en eindigt bij Puerto Mejillones voor verscheping.
https://www.mundomaritimo.cl/noticias/minera-san-cristobal-opta-por-puerto-chileno
[6] Wikipedia, "Ferrocarril de Antofagasta a Bolivia" (FCAB) — route Antofagasta/Mejillones–Ollagüe–Uyuni–
Oruro–La Paz; sinds 1906 een tweede haven/lijn bij Mejillones naast Antofagasta; eigenaar sinds 1982 Antofagasta
plc (transportdivisie); "sulphuric acid transported uphill and copper comes down", ook concentraten van andere
mineralen en lithiumpekel. https://en.wikipedia.org/wiki/Ferrocarril_de_Antofagasta_a_Bolivia
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15-z17) —
`v2/build-cache/satcheck/sat-zilver-sancristobal-antofagasta-planta.png`,
`sat-zilver-sancristobal-antofagasta-planta2.png` (verificatiebeeld op z17),
`sat-zilver-sancristobal-antofagasta-julaca.png`, `sat-zilver-sancristobal-antofagasta-mejillones.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom:** `zilver-sancristobal-antofagasta` · **bestand:** `v2/data/stroomroute-zilver-sancristobal-antofagasta.json`
(31,2 KB) · **recept:** `bak_zilver_sancristobal_antofagasta()` in `v2/tools/bak_stromen.sh` · **4 benen, geen zeebeen
(stoppunt op de kade) · 635,7 km totaal · 1.530 punten · 5 markers.**

| # | modaliteit | van → naar | km | toets |
|---|---|---|---|---|
| b1 | spoor | San Cristóbal-concentrator → Julaca-aansluiting | 88,4 | tegen 65 km gepubliceerd: **+36,0%**, buiten ±15% (bevinding, zie hieronder) |
| b2 | spoor | Julaca-aansluiting → grens Avaroa/Ollagüe | 76,6 | geen gepubliceerde deellengte — alleen de bake-uitkomst gerapporteerd; verhouding tegen de grootcirkel 1,00 (vrijwel recht, doorgetrokken/gemeten, geen stippel — zie hieronder) |
| b3a | spoor | grens Ollagüe → Calama | 206,5 | geen gepubliceerde deellengte |
| b3b | spoor | Calama → Mejillones-kade | 264,2 | geen gepubliceerde deellengte; 1 omkering (179,7°) bij Calama zelf |

**Toets (handleiding §5):** geen naad > 5 km tussen opeenvolgende benen (alle naden 0,00 km) ·
`toets_knikken.py` — 1 knik ≥60° / 1 omkering ≥150° op b3b (179,7°, boogstraal ~0 m, bij -22,45970,-68,92260 =
vrijwel exact het Calama-startpunt) — beoordeeld als **scherpe bocht, echt** (kopmaak-plek op een knooppunt met de
Chuquicamata-mijntak, geen terugloop) · `toets_rechte_benen.py --min-km 5` — deze stroom komt **niet** voor in de
uitslag (geen been ≥5 km met verhouding ≈1,000 werd gevlagd, ook b2's 1,00 niet — de tool vlagt kennelijk alleen
gestippelde rechte lijnen ≥5 km) · `json.load` slaagt, `versie` 2, `punt_formaat` lonlat, modaliteit overal `spoor`
(toegestane set), elk been ≥2 punten, bestand 31,2 KB (ruim binnen ~300 KB) · alle 5 markers ≤0,5 km van hun been
(kop/staart en de drie via-punten liggen op de geroutete lijn).

**Bevinding b1 (+36,0% tegen gepubliceerd)** — niet dichtgetrokken. De brief noemt zelf al dat Julaca als
aansluitpunt *aannemelijk, niet bevestigd* is (§7: geen bron noemt de aansluitknoop met naam) en dat het
gepubliceerde "65 km" uit Wikipedia een tak-lengte is zonder routebeschrijving. Het 1-op-1-net routeert 88,4 km
tussen de twee ankers (verhouding tegen de grootcirkel: 88,4/44,2 = 1,98) — een reëel spoortracé over dit terrein
(Altiplano-zoutvlakte-rand, geen rechte lijn mogelijk) kan die omweg dragen, maar zonder een tweede onafhankelijke
bron voor het exacte tracé is dit een bevinding en geen fout die met een ander via-punt gladgestreken hoort te
worden — een via-schuif zou het getal laten kloppen zonder een echte reden.

**Geen haven-aanloop gebouwd:** de keten stopt op de Mejillones-kade (geen zeebeen in deze stroom), dus een
MARNET-zeeverbinding is hier niet relevant, conform de bak-aanwijzing in de brief. Wel gemeten met het
`hecht_marnet`-snippet uit de bakhandleiding: de dichtstbijzijnde MARNET-zeeknoop (id 4664, -23,80000/-71,30000)
ligt op **124,9 km** van de kade — bevestigt de ~125 km uit §7 (dezelfde grootte-orde als de bekende
Mejillones-136km-noot in de handleiding). Puur context/open punt, geen been gebouwd.

**Geen last-mile-stippel bij Mejillones:** de kade zelf is het stoppunt van de hele keten (geen b4/b5 in deze
bake); de laatste ~700 m conveyor-strook uit de bak-aanwijzing is niet apart getekend omdat er na de kade geen
volgend been meer bestaat om een naad mee te vormen.

**Gereedschapslessen:**
- Vier losse spoorruns (kop→via, via→staart per corridorkeuze) i.p.v. één keten met `--via` — de spoorrouter kent
  geen `--via`-vlag, dus elke corridorkeuze in de brief (Julaca, de grens, Calama) wordt een eigen run-paar met
  `--hoofd-km=100` voor dit kleine/geïsoleerde net, precies zoals de handleiding voorschrijft.
- Alle vier de runs snapten op **hetzelfde component (22.494 km)** ondanks dat b1/b2 en b3a/b3b uit verschillende
  Geofabrik-extracts (bolivia/chili) komen — het 1-op-1-net (`BAKE_SUFFIX=-raw`) is één wereldwijd net, niet per
  extract gesneden, dus de landsgrens-overgang bij Ollagüe routeert zonder aparte stitch-stap.
- De 9,20 km-snap op het grenspunt is geen wegklasse-fout (er is geen weg, dit is spoor) maar een bron-precisie-
  probleem dat de brief al vooraf benoemde (§7: dorpscoördinaat i.p.v. exacte spoorgrensmarkering) — bevestigt de
  handleidingsregel "eerst de precisie van het punt zelf nakijken vóór je een snap > 5 km als foutmelding leest".
- De 179,7°-omkering bij Calama viel binnen 12 m van het startpunt van b3b — een klassiek kopmaak-patroon op een
  knooppuntstation (hier: aansluiting met de Chuqui-mijntak), overeenkomstig de valkuilen-checklist §6.
