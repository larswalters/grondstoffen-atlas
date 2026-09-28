# Routebrief (licht) · uranium — Rössing → Walvis Bay

**stroom-id:** `uranium-rossing-walvisbay` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31) ·
**status:** gebakken
**Keten in één zin:** Namibisch uraanoxide (yellowcake) van de Rössing-mijn (Arandis, CNNC 68,6%) per **truck**
over de B2 naar de haven van Walvis Bay — vandaar (niet getekend) overwegend naar China, waar geen gepubliceerd
loshavenanker bestaat.
**Welke as van het verhaal:** *Chinees staatseigendom — Namibisch erts naar China.* Rössing produceerde 2.920 tU
(~6,4 Mlbs U3O8) in 2023, peiljaar 2023 [1]; "een meerderheid van de gecombineerde Rössing+Husab-productie gaat
direct naar China" [1]. Namibische uraanexport (incl. Rössing) was in 2025 goed voor ruim 22% van de nationale
export [1][webcheck].

## 1 · Ketenkaart
```
Rössing-fabriek `u-rossing-plant` ──(b1 truck · B2 Arandis–Swakopmund–Walvis Bay · ~90 km, aannemelijk)──►
   Walvis Bay-haven `u-walvisbay-haven` ── stoppunt
   ├── vertakking (niet getekend): overwegend naar China (CNNC-conversielijn) — geen gepubliceerde loshaven
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `u-rossing-plant` → `u-walvisbay-haven` | B2 (Arandis–Swakopmund–Walvis Bay) | ~90 [2][3][webcheck] | maak_stroombeen_weg (extract namibie) | nee — B2 is gekarteerde hoofdweg |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-rossing-plant` | mijn / verwerkingsfabriek (laadplek) | Rössing Uranium Ltd, verwerkingsfabriek, Arandis | -22.4635, 15.0405 | [3][4][sat] | bron-gelegd (z16 gezien: industrieel complex met tanks, procesgebouwen en een conveyor tussen de open pit en een tailingsbekken; ~2 km NNO van de put op 22.48417°S/15.04889°E [3]) |
| `u-walvisbay-haven` | overslag / losplek (stoppunt) | NamPort containerterminal, Walvis Bay | -22.9465, 14.4840 | [5][6][sat] | bron-gelegd (z16 gezien: containerterminal op landtong met containerstapels en kade; NamPort meldt uraniumoxide als bulk-, stukgoed- én containerlading [6] — exacte berth niet te onderscheiden) |

## 4 · Via-punten (geen corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| — | — | — | — | B2 is de enige doorgaande verharde weg Arandis–Swakopmund–Walvis Bay door de Namibwoestijn; geen alternatieve route, dus geen corridorkeuze om te pinnen. |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Rössing-fabriek (Arandis) | CNNC (68,6%) / Rio Tinto-erfenis | uraanerts → yellowcake (U3O8, drums) | 2.920 tU/jaar (2023) [1]; historisch ~106–109 t U3O8/jr specifiek naar China (2004/2005) [design] | [1] |

## 6 · Stoppunt
De brief stopt bij Walvis Bay-haven (bindende keuze uit de haalbaarheidstoets): geen bron geeft een specifieke
Chinese loshaven voor de CNNC-conversielijn, en een marktcentroïde of giswerk-anker is geen toegestaan anker —
het "overwegend naar China"-verhaal blijft tekst, zonder getekend zeebeen.

## 7 · Open punten
- **Modaliteit gecorrigeerd t.o.v. het ketenontwerp:** het ontwerp noemt "spoor" (TransNamib Arandis–Walvis
  Bay), maar geen bron bevestigt dat de TransNamib-lijn de **uitgaande** yellowcake vervoert — de lijn draagt
  wél aantoonbaar **inkomende** zwavelzuur voor de Rössing-fabriek [7][8]. Voor de buurmijn Husab (5 km
  zuidelijker, zelfde B2-corridor) is expliciet gedocumenteerd dat verzegelde yellowcake-drums "direct over de
  weg" naar Walvis Bay gaan [webcheck-analogie]. Bij gebrek aan een directe Rössing-specifieke bronzin is dit
  been getekend als **truck, aannemelijk: analogie met Husab** — geen citaat-bron voor Rössing zelf gevonden.
- **Geen enkele gepubliceerde km-waarde voor Rössing→Walvis Bay specifiek:** ~90 km is afgeleid uit "mijn ligt
  80 km NO van Walvis Bay" [3] + "B2 Arandis–Walvis Bay 77 km" [2] + het laatste stuk mijn→Arandis. Bake-toets
  bepaalt de echte wegafstand.
- **Welke NamPort-terminal** (container- of bulkterminal) de uraniumlading werkelijk gebruikt is niet
  aanwijsbaar — Namport noemt uraniumoxide zelf als bulk/stukgoed/container [6]. Anker op de containerterminal
  gelegd (drums worden op de mijn al in zeecontainers verpakt [4][webcheck]), niet gebrond per zending.
- **Fase B (zee) blijft open per de haalbaarheidstoets:** geen gepubliceerd Chinees loshavenanker; niet
  getekend.
- **Jaarvolume-discrepantie:** WISE-Uranium geeft 2.920 tU (2023) [1]; World Nuclear Association geeft 2.476 tU
  voor hetzelfde jaar [9] — vermoedelijk boekhoudverschil (kalenderjaar vs. omrekenfactor); WISE-cijfer
  aangehouden conform het ketenontwerp.

## 8 · Bronnen
[1] The Oregon Group, "Namibia's Strategic Ascent in the Global Uranium Supply Chain" (2025) — CNNC 68,6%,
Rössing 2.920 tU (2023), "meerderheid Rössing+Husab direct naar China". https://theoregongroup.substack.com/p/namibias-strategic-ascent-in-the
[2] geodatos.net — wegafstand Arandis–Walvis Bay 77 km. https://www.geodatos.net/en/distances/from-arandis-to-walvis-bay
[3] Wikipedia, "Rössing uranium mine" — coördinaat 22°29′03″S 15°02′56″E, CNNC 68,6%, mijn 80 km (50 mijl) NO
van Walvis Bay. https://en.wikipedia.org/wiki/R%C3%B6ssing_uranium_mine
[4] World Nuclear Association / Husab-analogie, Wikipedia "Husab Mine" — yellowcake-drums verzegeld en
gecontaineriseerd op het mijnterrein, "transported directly by road" naar Walvis Bay; Husab ligt 5 km zuidelijk
van Rössing op dezelfde B2-corridor. https://en.wikipedia.org/wiki/Husab_Mine
[5] Namibian Ports Authority (NamPort) — containerterminal Walvis Bay, gecommissioneerd 2019.
https://www.namport.com.na/port-engineering/container-terminal/592/
[6] NamPort / vakpers — uraniumoxide (yellowcake) als bulk-, stukgoed- en containerlading door Walvis Bay, max.
3 dagen opslag i.v.m. stralingsprotocol. https://www.namport.com.na/services/cargo-handling/461/
[7] Freight News, "Namibian miner invests in Walvis Bay port" — Rio Tinto Rössing-zwavelzuuropslag in de haven.
https://www.freightnews.co.za/article/namibian-miner-invests-in-walvis-bay-port
[8] African Development Bank, contract award — spoorlijn-upgrade Walvis Bay–Kranzberg incl. pakket
Arandis–Kranzberg (zwavelzuurtransport TransNamib Tsumeb–Arandis/Walvis Bay). https://www.afdb.org/en/documents/contract-awards-namibia-upgrading-railway-line-between-walvis-bay-and-kranzberg-works-package-c002-arandis-kranzberg-namibia-transport-infrastructure-improvement-project
[9] World Nuclear Association, "Uranium in Namibia" — Rössing 2.476 tU (2023), CNNC-aandeel bevestigd.
https://world-nuclear.org/information-library/country-profiles/countries-g-n/namibia
[10] WISE-Uranium, "Issues at Rössing Uranium Mine, Namibia" — productiehistorie, CNUC-overname 2018/2019.
https://www.wise-uranium.org/umoproe.html
[11] CNNC, 16-08-2024 (uit ketenontwerp, niet apart herbevestigd). https://en.cnnc.com.cn/2024-08/16/c_1023404.htm
[sat] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16) —
`v2/build-cache/satcheck/sat-uranium-rossing-walvisbay-rossing-plant.png`,
`sat-uranium-rossing-walvisbay-container2.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze)

**Stroom `uranium-rossing-walvisbay`** → `v2/data/stroomroute-uranium-rossing-walvisbay.json` — 1 been. 106,6 km. 2 markers: truck 106,6 km.
Recept: `bak_stromen.sh` (functie `bak_uranium_rossing_walvisbay`). Toelichting: b1 (truck Rössing → Walvis Bay) is één wegscan (`maak_stroombeen_weg.py --profiel uranium-rossing-walvisbay --bron geofabrik`, extract `namibie`) zonder via-punten (B2 is de enige gekarteerde hoofdweg, geen corridorkeuze) — het tool volgt zelf de B2/toegangsweg-combinatie, ankerstukjes 0,08 km (plant → weg) en 0,28 km (weg → kade) beide binnen de norm. Lengtetoets: 106,3 km weggeometrie (106,6 km met de twee ankerstukjes) tegen ~90 km gepubliceerd = **+18,1%, buiten ±15%** — bevinding, niet dichtgetrokken: geen bron geeft een directe km-waarde voor dit traject, ~90 km is zelf al afgeleid uit twee losse cijfers (Wikipedia 80 km hemelsbreed + B2 Arandis–Walvis Bay 77 km, brief §7/§2), en de gescande weg volgt logischerwijs een langere route dan de indicatieve schatting. Geen stippel (B2 is gekarteerd); fase B (zee) niet getekend, conform de bindende haalbaarheidstoets van brief §6 (geen gepubliceerd Chinees loshavenanker).

Stippels: geen. Het hele been is doorgetrokken — B2 is een gekarteerde hoofdweg en het net reikt tot beide ankers.

Gereedschapslessen: (a) geen via-punten nodig gebleken — de scanner (`corridor_keten`) volgt zelf de enige doorgaande weg tussen de twee ankers zonder een keuze te moeten maken, precies zoals de brief voorzag. (b) de lengtetoets is hier de scherpste vondst van deze bake: de brief zelf had al gewaarschuwd dat ~90 km een indicatieve, niet-gebronde afleiding is, en de gemeten 106,3–106,6 km bevestigt dat de echte wegafstand een stuk langer is dan die schatting — geen enkele reden om aan de geometrie te sleutelen, de brief-schatting was de zwakke schakel, niet de scan. (c) `toets_knikken.py`: 18 knikken ≥60° (allemaal spikes met straal <100 m, normale OSM-wegvertices bij kruisingen/rotondes rond de twee ankers), 0 omkeringen ≥150°, 0 terugloop. `toets_rechte_benen.py --min-km 5`: het been verschijnt niet in de verdachtenlijst (geen rechte lijn — echte gescande weggeometrie, 793 punten). Toetsen geslaagd: `json.load`/versie 2/punt_formaat lonlat/modaliteit {truck}/been ≥2 punten/bestand 16,5 KB, allemaal binnen de norm. Beide markers op resp. 0,08 en 0,28 km van hun been (beide ruim binnen ~0,5 km — anker = vrijwel exact routeerpunt).
