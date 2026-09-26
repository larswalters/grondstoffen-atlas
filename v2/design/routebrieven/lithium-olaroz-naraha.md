# Routebrief (licht) · lithium — Olaroz (Argentinië) → Buenos Aires → Onahama → Naraha (Japan)

**stroom-id:** `lithium-olaroz-naraha` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** technisch-gradig lithiumcarbonaat van de Sales de Jujuy-plant op de Salar de Olaroz gaat per truck ~1.750 km (RN52 → RN9 → RN34) dwars over Argentinië naar de containerkade van Buenos Aires, per containerschip naar de Onahama-kade in Fukushima, en per truck ~35 km naar de hydroxidefabriek van Toyotsu Lithium in Naraha — de enige lithiumketen van de atlas die China/Korea helemaal omzeilt, en momenteel stilliggend.
**Welke as van het verhaal:** *de omweg om China heen (2)* — Argentijns carbonaat naar Japans eigen hydroxidefabriek, niet over de Andes maar over Argentinië's eigen Atlantische haven. Argentinië 23 kt Li 2025 (8 % van de wereld, USGS), Olaroz 60 kt Li₂CO₃ 2025 (Rio Tinto Q4 2025 [4]); Naraha is de énige klant van dit specifieke traject, ~9–10 kt/j feed op een nameplate van 10 kt/j LiOH (10.000 MT, Toyota Tsusho 2022 [2]) — klein naast Olaroz' totaal, maar volledig gebrond. **Naraha staat sinds medio 2025 op *care and maintenance*** (Arcadium/Rio Tinto 10-K FY2024 [5]; Rio Tinto's eigen operations-pagina bevestigt de stilstand vandaag [1]) — de weg is echt gevaren tot 2025, de lading ligt nu stil.

## 1 · Ketenkaart
```
Olaroz-plant `li-olaroz-plant` ──(b1 truck · RN52→RN9→RN34, via Purmamarca/S.S. de Jujuy/Tucumán/Rosario · ~1.750 km, niet gepubliceerd)──►
Buenos Aires containerkade `li-baires-kade` ──(b2 zee · Atlantische Oceaan om Afrika of via Panama, MARNET beslist · ~18.260 km hemelsbreed)──►
Onahama-kade `li-onahama-kade` ──(b3 truck · Jōban-snelweg/Route 6 noordwaarts · ~35 km)──► Toyotsu Lithium Naraha `li-naraha-fabriek` ⏹ stoppunt

vertakking (niet getekend): rest van Olaroz' ~60 kt/j (~50 kt) naar China/Korea via Antofagasta/Mejillones (Paso de Jama) — niet per fabriek gebrond
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (carbonaat in big bags, containers/gesloten trucks) | `li-olaroz-plant` → `li-baires-kade` | RN 52 (Susques–Purmamarca) → RN 9 (S.S. de Jujuy) → RN 34/RN 9 zuidwaarts (Tucumán-splitsing) → Rosario → Buenos Aires | niet gepubliceerd; ontwerpschatting ~1.750, hemelsbreed 1.477 [6][7] | maak_stroombeen_weg (extract argentina) | nee |
| b2 | B | zee (containerschip) | `li-baires-kade` → `li-onahama-kade` | Atlantische Oceaan, geen zeestraat op de heenweg — MARNET beslist de route (Kaap of Panama) | ≈ 18.260 hemelsbreed; gepubliceerd: geen [7] | MARNET | aanloop: beide kanten (Río de la Plata ~30–38 km, Onahama-kade ~42 km) |
| b3 | C | truck | `li-onahama-kade` → `li-naraha-fabriek` | Jōban-snelweg (E6) / Route 6, langs een extern tussenmagazijn op ~16 km | ~35 (Toyotsu Onahama-seminar 2024-02-02: kade↔extern magazijn ~16 km/~30 min, magazijn↔fabriek resterend deel van ~35 totaal) [7] | maak_stroombeen_weg (extract japan) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-olaroz-plant` | mijn / carbonaatplant | Sales de Jujuy S.A. — Olaroz-plant, Salar de Olaroz, Susques, Jujuy, ~3.900 m | -23.4629, -66.7025 | [6] SEC-resourcecoördinaat | aannemelijk (z15/z16 gezien: het punt ligt op een kruising van bermen/toegangswegen middenin de salarwerken — evaporatiebekkens en wegennet rondom zichtbaar — maar geen los gebouw te onderscheiden op deze korrel) |
| `li-baires-kade` | overslag (laden) | TRP — Terminales Río de la Plata (DP World), Puerto Nuevo, Buenos Aires | -34.5847, -58.3631 | [8][9] OSM/terminal-directories | bron-gelegd (z15/z17 gezien: containenstapels met twee portaalkranen op de pier, direct aan het punt) |
| `li-onahama-kade` | overslag (lossen) | Ōken-ふ頭 (大剣ふ頭) containerterminal, Onahama-haven, Iwaki, Fukushima | 36.9245, 140.8695 | [3][9] havenseminar + OSM | bron-gelegd (z17 gezien: containerstapels + twee kranen op een pier direct naast tankopslag; ligt in het door Fukushima-provincie genoemde 大剣ふ頭-containergebied) |
| `li-naraha-fabriek` | fabriek (losplek + conversieknoop) | Toyotsu Lithium Corp., 楢葉町大字山田岡字仲丸1-40 (楢葉南工業団地), Naraha-machi, Fukushima | 37.2467, 140.9954 | [1][2][10] adres + Digitaal Agentschap ABR-coördinaat | bron-gelegd (z16 gezien: gebouwencomplex met parkeerterrein op het bedrijventerrein-perceel, op de ABR-representatieve coördinaat van het adres uit het persbericht) |

## 4 · Via-punten (alleen b1 — enige landbeen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Purmamarca (RN 52 → RN 9-knoop) | -23.7466, -65.4992 | pint de afdaling van de Puna naar de Quebrada; hier voegt RN 52 zich bij RN 9 i.p.v. verder oost over een zijtak |
| b1 | 2 | San Salvador de Jujuy | -24.1853, -65.2995 | RN 9 passeert de provinciehoofdstad; pint de doorgaande route i.p.v. een stadsomleiding |
| b1 | 3 | Tucumán (RN 34/RN 9-splitsing) | -26.8241, -65.2226 | hier kan de corridor verder over RN 9 of overstappen op RN 34 zuidwaarts naar Rosario/Buenos Aires — pint de zuidelijke keuze |
| b1 | 4 | Rosario | -32.9442, -60.6505 | laatste grote knoop vóór Buenos Aires waar RN 9/RN 34/RN A008 samenkomen |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Toyotsu Lithium, Naraha | Rio Tinto Lithium (75 %) / Toyota Tsusho (25 %; stemrecht 51 % TT) | Li₂CO₃ (technisch-gradig, uit Olaroz) → LiOH·H₂O (batterij-gradig) | nameplate 10.000 t LiOH/j; **sinds medio 2025 op care and maintenance** | [1][2][5] |

## 6 · Stoppunt
De brief stopt aan de poort van Toyotsu Lithium Naraha: dat is de conversieknoop zelf (carbonaat → hydroxide), het hydroxide wordt via Toyota Tsusho Material aan binnen- en buitenlandse afnemers verkocht zonder dat één specifieke vervolgfabriek gebrond is — fase D vervalt.

## 7 · Open punten
- **Welke Chileense... nee, Argentijnse haventerminal exact:** geen bron noemt de terminal bij naam; TRP is de grootste containerterminal van Buenos Aires (DP World) en de meest waarschijnlijke kandidaat, maar niet bevestigd voor déze lading.
- **Operationele status:** Naraha staat sinds medio 2025 op *care and maintenance* [1][5] — de infrastructuur en het bewijs voor de route zijn hard, het huidige vrachtvolume is (nagenoeg) nul. Zelfde behandeling als de grafietketen Balama→Vidalia (M28): de weg wordt getekend, het volume-nul hoort in de tekst.
- **Gepubliceerde weg-km ontbreekt volledig** voor b1 (Olaroz → Buenos Aires); alleen de hemelsbreedafstand (1.477 km) uit de TRS is een indirecte controle, en die geldt voor de Jama-route, niet voor deze. Bake-lengtetoets loopt dus tegen de kaartafstand, niet tegen een gepubliceerd getal.
- **Onahama was in 2023–2024 nog een proefhaven** (eerste trial-import december 2023, uitbreiding gepland FY2024) [3]; vóór 2023 liep de aanvoer via de Keihin-havens (Tokio/Yokohama). Niet bekend of de haven inmiddels de standaardroute is of dat bij hervatting weer via Keihin gegaan wordt.
- **Het externe tussenmagazijn bij Onahama** (~16 km van de kade) is als logistiek knooppunt genoemd maar niet als apart anker gelegd (geen corridorkeuze, blijft binnen fase C).
- **Rest van Olaroz' productie (~50 kt/j) naar China/Korea** is niet per fabriek gedocumenteerd — bewust niet getekend, blijft vertakking in §1.
- **RN 52 bij Olaroz zelf** ligt op grote hoogte (~3.900–4.200 m) en is in OSM mogelijk lager geklasseerd dan `primary`; kan `corridorKlassen` nodig maken bij het bakken (zie §-aanwijzing bak-agent).

## 8 · Bronnen
[1] Rio Tinto, Naraha — ownership 75 %, product lithium hydroxide, nameplate 10.000 t/j, "This operation is currently under Care and Maintenance". https://www.riotinto.com/en/operations/asia/naraha
[2] Toyota Tsusho, persbericht 2022-11-16 — voltooiing Naraha-fabriek, capaciteit 10.000 t/j, feedstock uit Sales de Jujuy, adres 1-40 Nakamaru, Yamadaoka, Naraha-machi, destijds Allkem 75 %/Toyota Tsusho 25 %. https://www.toyota-tsusho.com/english/press/detail/221116_006133.html
[3] Toyotsu Lithium, Onahama-havenseminar 2024-02-02 (pdf) — route SDJ → Buenos Aires → Onahama → fabriek; import sinds okt 2021, dienst gepauzeerd door corona, hervat zomer 2023, eerste Onahama-trial dec 2023; Onahama↔extern magazijn ~16 km/~30 min tegen Keihin↔magazijn ~223 km/~3u10. https://www.o-minato.com/app/download/14331807288/02+豊通リチウム㈱様資料'.pdf
[4] Rio Tinto, Q4 2025 production results (SEC 6-K) — Olaroz 60 kt Li₂CO₃ 2025. https://www.sec.gov/Archives/edgar/data/863064/000086306426000006/ex1_2025-q4results.htm
[5] Arcadium Lithium plc, Form 10-K FY2024 (SEC) — "Excludes 10,000 MT of lithium carbonate to lithium hydroxide capacity at Naraha Plant where Arcadium owns a 75% economic interest... care and maintenance". https://www.sec.gov/Archives/edgar/data/1977303/000197730325000006/lthm-20241231.htm
[6] Arcadium/Allkem, NI 43-101 Technical Report Summary Cauchari-Olaroz (SEC-exhibit) — Olaroz-coördinaat 23°27'46.54"S/66°42'8.94"W, RN 52/Paso de Jama/Antofagasta-corridor voor de algemene export (~530 km, niet dit traject). https://www.sec.gov/Archives/edgar/data/1977303/000114036123050053/ny20009544x9_ex96-2.htm
[7] Eigen berekening (grootcirkel) op de in dit document gelegde ankers; geen gepubliceerde bron voor b1/b2-lengtes.
[8] DP World / Terminal49 — TRP (Terminales Río de la Plata), grootste containerterminal van Argentinië, Puerto Nuevo Buenos Aires. https://www.dpworld.com/en/ports-terminals/argentina/trp
[9] OpenStreetMap (ODbL) via Nominatim — Puerto Nuevo (relatie 4260969), 小名浜臨港道路 大剣ふ頭内線 (way 365012943), 山田岡-kwartier (node 8531838092). https://www.openstreetmap.org
[10] Digitaal Agentschap Japan, Address Base Registry via 全国Q地図 — 福島県双葉郡楢葉町大字山田岡字仲丸, representatief punt 37.246724°/140.995440°. https://qchizu.jp/data/addresses/pages/福島県/双葉郡楢葉町/大字山田岡/字仲丸/
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15–z17) — `v2/build-cache/satcheck/sat-li-olaroz-naraha-olaroz-plant2.png`, `sat-li-olaroz-naraha-baires-trp.png`, `sat-li-olaroz-naraha-onahama-oken3.png`, `sat-li-olaroz-naraha-naraha-fabriek2.png`.


## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `lithium-olaroz-naraha`** → `v2/data/stroomroute-lithium-olaroz-naraha.json` — 5 benen. 22.615,2 km. 4 markers: truck 1.868,9 km · zee (stippel) 32,3 km · zee 20.623,6 km · zee (stippel) 45,5 km · truck 44,9 km.
Recept: `bak_stromen.sh` (functie `bak_lithium_olaroz_naraha`).

Toelichting per been. **b1** (Olaroz-plant → Buenos Aires, `argentina`-extract, profiel `lithium-olaroz-naraha-baires`): RN52 vlak bij de plant loopt over `service`/`track`-mijnwegen op de salarwerken (~3.900–4.200 m, zoals brief §7 voorzag); zonder een corridor-brede `residential` én een verruimde `eindKlassen` (mét `track`) meldde de scan "geen wegpad tussen punt 0 en 1" — met beide erbij snapt de plant op 0,83 km (> 0,5 km, bevinding) en loopt de rest over RN52 → RN9 → RN34/RN9-splitsing bij Tucumán → Rosario → Buenos Aires. Uitkomst 1.868,9 km. Tegen de hemelsbreed-som van de via-punten (~1.562 km, brief §2/§7, géén echte weg-km) is dat **+19,6%**, maar tegen de eigen ontwerpschatting van de briefschrijver (~1.750 km) is dat **+6,8%** — binnen de lichte ±15%-norm; de tool-eigen toets rekent tegen het eerste getal en meldt daarom "buiten ±10%", wat hier een artefact van de referentie is, geen routeerfout. **b2** (zee): beide kades liggen te ver van een MARNET-zeeknoop voor een direct `--been` (Buenos Aires TRP 30,5 km, Onahama-kade 44,9 km, `marnet_zee()`-snippet uit de bak-handleiding §2) → twee `maak_havenaanloop.py`-aanlopen (32,3 km resp. 45,5 km, allebei 0,00 km landkruising midden op de lijn), met het eigenlijke zeebeen tussen de twee zeeknopen (20.623,6 km, MARNET kiest zelf de Kaap- of Panama-route — geen zeestraat op de heenweg, brief §2). De Onahama-aanloop is gegenereerd in AANKOMSTRICHTING (`--van`=zeeknoop, `--naar`=kade, omgekeerd t.o.v. de vertrekconventie): `--been-geojson`/`--stippel-geojson` tekenen de punten letterlijk in bestandsvolgorde zonder automatische omkering, dus alle vijf benen sluiten met naad 0,000 km op elkaar aan (geverifieerd). **b3** (Onahama-kade → Toyotsu Lithium Naraha, `japan`-extract, profiel `lithium-olaroz-naraha-onahama-naraha`): geen tussenliggend via-punt (brief §7, geen corridorkeuze) — de gemeten 44,9 km ligt **+28,3%** boven de gepubliceerde ~35 km (Toyotsu Onahama-havenseminar, brief bron [3]); bevinding, niet dichtgetrokken (geen corridorkeuze om een via-punt op te pinnen).

Volume-nul: Naraha staat sinds medio 2025 op *care and maintenance* (brief §1/§5/[1][5]) — de weg is echt gevaren tot 2025, de lading ligt nu stil. Beide truckbenen zijn **doorgetrokken, niet gestippeld** (werkwijze §7, zelfde behandeling als grafiet Balama→Vidalia): het volume-nul staat in de brieftekst, niet in de lijnstijl. Fase D vervalt (brief §6): Naraha is zelf de conversieknoop en het stoppunt.

Toets: `json.load` slaagt (versie 2, punt_formaat lonlat, alle modaliteiten in {truck, zee}, elk been ≥ 2 punten). Naden tussen alle opeenvolgende benen 0,000 km. `toets_knikken.py`: 110 knikken ≥ 60° (spikes/krappe bochten op weg- en zeegeometrie), 3 omkeringen ≥ 150° maar **0 terugloop** (de enige klasse die gerepareerd hoort te worden) — normaal voor lange weg-/zeegeometrie. `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de verdachtenlijst (beide haven-aanlopen zijn gekromde kortste-paden-over-water, geen rechte lijn; omwegfactor 1,058 resp. 1,014). Bestand **328,0 KB**, boven de ~300 KB-richtwaarde uit de handleiding (buiten de norm — bevinding, niet dichtgetrokken door punten weg te gooien; vergelijkbaar met andere lange, dicht bemonsterde truckbenen elders in dit project, bv. `grafiet-lakecharles-desoto` 422,9 KB).

**Gereedschapslessen:**
- RN52 bij Olaroz is precies het risico dat de brief zelf al noemde (§7): een corridor op grote hoogte kan in OSM lager geklasseerd zijn dan `primary`/`trunk`. Hier bleek het scherper dan `corridorKlassen` alleen kan oplossen — de aansluiting van de plant op RN52 loopt over `service`- én `track`-mijnwegen, dus zowel `corridorKlassen` (corridor-breed `residential` erbij) als `eindKlassen` (binnen de 12 km-eindzone óók `track` toelaten) waren nodig. Zonder één van beide meldt de scan "geen wegpad", zonder duidelijk aan te wijzen wélke klasse ontbreekt.
- `--been-geojson`/`--stippel-geojson` tekenen een bestand letterlijk in zijn eigen puntvolgorde; er is geen automatische richting-detectie in `hecht_marnet.py route`. Een haven-aanloop die als tweede (aankomst-)stippel in de keten dient, moet dus met `--van`/`--naar` omgekeerd gegenereerd worden (zeeknoop → kade) — anders krijg je een naad van tientallen kilometers in plaats van 0,000 km, terwijl de geometrie zelf prima is.
- Twee losse, kleine referentiegetallen (hemelsbreed-som van via-punten vs. de eigen ontwerpschatting van de briefschrijver) kunnen tegengestelde toetsuitslagen geven op precies dezelfde geometrie — meld beide in plaats van er één te kiezen als "het" gepubliceerde getal.
