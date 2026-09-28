# Routebrief (licht) · uranium — Van → Via → Naar (land)

**stroom-id:** `uranium-malvesi-tricastin` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken
**Keten in één zin:** UF4 van Orano Malvési (Comurhex I, conversie U3O8→UF4, Narbonne) gaat over het Franse
spoornet naar Orano Tricastin (Comurhex II conversie UF4→UF6 + Georges Besse II-verrijking, Pierrelatte) —
stoppunt; Frankrijks binnenlandse nucleaire-zelfvoorzieningsas.
**Welke as van het verhaal:** Frankrijk conversie → verrijking, prioriteit 3 van M31 golf 5. Malvési converteert
~15.000 tU/j indicatief [1]; het specifiek voor déze been gevonden cijfer is **320 t uranium per treinlading,
1×/week** (2017) [2] ≈ 16.640 tU/j — dezelfde orde van grootte als de generieke fabriekscapaciteit.

## 1 · Ketenkaart
```
Orano Malvési — Comurhex I (conversie U3O8→UF4), Narbonne `u-malvesi`
  ──(b1 B spoor · Narbonne–Béziers–Montpellier–Nîmes–Avignon–Pierrelatte, sinds 2014 · ~187 km hemelsbreed,
     geen gepubliceerde spoorkm)──►
Orano Tricastin — Comurhex II (UF4→UF6) + Georges Besse II-verrijking, Pierrelatte `u-tricastin` ── stoppunt
```
**Afwijking t.o.v. het ketenontwerp:** het ontwerp nam `truck` aan (A9→A7) als aanname zonder bron. Onderzoek
vond een specifieke, gedateerde bron voor **spoor** sinds 2014 (zie §7 voor een tegensprekende bron over
trucks) — been b1 is daarom **spoor**, niet truck. `spoornet_nodig` in het ontwerp stond op `false`; dat klopt
niet meer voor deze keten. Fase D (Tricastin → Framatome Romans-sur-Isère) is **vervallen**: geen bron binnen
het webbudget bevestigt déze specifieke levering (zie §7) — conform de regel van de haalbaarheidstoets/het
ontwerp zelf ("vervalt tenzij een bron de levering noemt").

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | spoor | Orano Malvési → Orano Tricastin | Narbonne-Malvési-aftakking (4,9 km, vernieuwd 2020 [3]) → hoofdlijn Béziers–Montpellier–Nîmes–Avignon–Pierrelatte | hemelsbreed 187 [ontwerp]; geen gepubliceerde spoorkm — te meten bij het bakken | `toets_spoorroute.mjs` (`BAKE_SUFFIX=-raw`), 4 losse runs kop→via→via→via→staart | nee |

## 3 · Ankers (één per site en per overslag — beide letterlijk hergebruikt uit `v2/design/uranium-sitelaag.json`)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-malvesi` | conversie (kop) | Orano Malvési — Comurhex I, Narbonne, Aude | 43.2074, 2.9812 | `w-malvesi` in `uranium-sitelaag.json` [1] | aannemelijk (hergebruikt letterlijk, geen nieuwe satellietblik deze ronde) |
| `u-tricastin` | conversie + verrijking (staart, stoppunt) | Orano Tricastin — Comurhex II + Georges Besse II, Pierrelatte, Drôme | 44.3250, 4.7167 | `w-tricastin-conversie`/`w-tricastin-verrijking` in `uranium-sitelaag.json` [1] | bron-gelegd (hergebruikt letterlijk; satellietblik al gedaan in de sitelaag-ronde: kruis midden op het grote industriecomplex tussen het Donzère-Mondragon-kanaal en de Rhône) |

## 4 · Via-punten (b1 — corridorkeuzes op de spoorlijn, Wikipedia-gare-coördinaten)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Gare de Narbonne (aansluiting Malvési-tak op het hoofdnet) | 43.1906, 3.0057 | hier komt de private aftakking naar Malvési op de hoofdlijn — sluit een route via Perpignan/Toulouse uit |
| b1 | 2 | Gare de Nîmes | 43.8325, 4.3663 | corridorkeuze: hoofdlijn richting Avignon/Rhônevallei i.p.v. de aftakking naar Alès/Le Grau-du-Roi |
| b1 | 3 | Gare d'Avignon-Centre | 43.9419, 4.8047 | corridorkeuze: verder noordwaarts langs de Rhône richting Pierrelatte/Valence i.p.v. de lijn naar Marseille |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Orano Malvési | Orano | U3O8 (yellowcake) → UF4 | ~15.000 tU/j indicatief | [1] |
| Orano Tricastin | Orano | UF4 → UF6 (Comurhex II) + UF6 → LEU-UF6 (Georges Besse II, ~12% wereld-SWU) | conversie ~15.000 tU/j; verrijking ~7.800 tU feed-equivalent/j | [1] |

## 6 · Stoppunt
De brief stopt bij Orano Tricastin: dit is het eindpunt van het ketenontwerp (conversie → verrijking) en fase D
(→ Framatome Romans-sur-Isère) vervalt bij gebrek aan een bron voor déze specifieke levering (§7). Fase E
vervalt eveneens.

## 7 · Open punten
- **Modaliteit-tegenspraak tussen bronnen.** Wikipedia (FR), "Usine Orano Malvési" [2], geeft een specifiek,
  gedateerd verhaal: tot 2013 per truck (A9/A7), na een blokkade-actie op 12-09-2013 overgeschakeld op **spoor**
  (wekelijks, zaterdagochtend), met een concreet 2017-cijfer (320 t U/week). Een tweede bron, homonuclearus.fr
  (23-04-2020) [4], noemt echter "trois à cinq camions qui empruntent l'A9 et l'A7" voor dezelfde route, zonder
  jaartal-context. Gekozen: **spoor** (specifieker gedateerd, recentere primaire bron over de fabriek zelf) —
  bij het bakken opnieuw toetsen (Orano-jaarverslag of ASNR-inspectierapport) als een sterkere bron voorhanden is.
- **Geen gepubliceerde spoorkm.** Alleen de hemelsbrede 187 km uit het ketenontwerp; de echte spoorafstand via
  Narbonne–Béziers–Montpellier–Nîmes–Avignon–Pierrelatte is substantieel langer (geen kortere rechte lijn) en
  wordt gemeten door `toets_spoorroute.mjs` bij het bakken — de ±15%-toets is dus niet toepasbaar als norm.
- **Jaarvolume gedateerd.** Het 320 t/week-cijfer is uit 2017 (9 jaar oud); geen recenter cijfer gevonden binnen
  het webbudget. De generieke Malvési-capaciteit (~15.000 tU/j, [1]) is fabrieksbreed, niet been-specifiek.
- **Fase D vervalt.** Geen citeerbare bron binnen het webbudget bevestigt dat Tricastin-verrijkt uranium naar
  Framatome Romans-sur-Isère gaat voor déze keten. Sterker nog: een gedocumenteerd incident (ASNR/
  sortirdunucleaire.org, 22-12-2023 [5]) toont UF6-aanvoer bij Framatome Romans-sur-Isère **vanuit Nederland**
  (vermoedelijk Urenco Almelo), niet vanuit Tricastin — dit weerspreekt eerder een exclusieve Tricastin→Romans-
  koppeling dan dat het die bevestigt. Anker `w-framatome-romans` (45.0500, 4.9667, status onzeker in de
  sitelaag) is daarom niet gebruikt.
- **Exact spoortracé bij Tricastin/Pierrelatte** (welke aansluiting het fabrieksterrein bereikt) niet gevonden
  binnen het webbudget — de drie via-punten pinnen alleen de hoofdcorridor; de bak-agent moet dit op het
  1-op-1-spoornet (`landnet-raw`) controleren.
- `spoornet_nodig: false` uit het ketenontwerp is **achterhaald** door dit onderzoek — deze keten heeft het
  spoornet wél nodig.

## 8 · Bronnen
[1] `v2/design/uranium-sitelaag.json`/`.md` — ankers `w-malvesi` (43.2074/2.9812, aannemelijk), `w-tricastin-conversie`/`w-tricastin-verrijking` (44.3250/4.7167, bron-gelegd), `w-framatome-romans` (45.0500/4.9667, onzeker, niet gebruikt); capaciteitscijfers [B16][B17][B19] in die brief (Orano-bedrijfspagina's, Orano Annual Activity Report 2024, World Nuclear Association "Uranium Enrichment").
[2] Wikipedia (fr), "Usine Orano Malvési" — coördinaten 43°12'49"N/2°58'48"E; overschakeling van truck naar spoor in 2014 na de blokkade-actie van 12-09-2013; "En 2017, un train de 320 tonnes d'uranium est expédié chaque semaine" naar Pierrelatte. https://fr.wikipedia.org/wiki/Usine_Orano_Malv%C3%A9si
[3] Raildusud (blog spoorwaarnemer), "Narbonne-Bize : Azurail a rénové 4,9 km de voie pour l'usine nucléaire Orano" (14-09-2020) — vernieuwd traject Narbonne–Malvési, 4,9 km, 60 kg/m-rails hergebruikt van de lijn Nîmes-Montpellier, werk juli-augustus 2020, €2,3 mln; rest van de lijn (voorbij Orano, richting Bize) bedreigd met sluiting (CGT Cheminots). https://raildusud.canalblog.com/archives/2020/09/14/38507904.html
[4] Homonuclearus.fr, "Rails et Routes acheminent des tomates et de l'Uranium" (23-04-2020) — noemt "trois à cinq camions qui empruntent l'A9 et l'A7" voor het traject Malvési→Pierrelatte; tegenstrijdig met [2], zie §7. https://homonuclearus.fr/rails-routes-acheminent-tomates-luranium/
[5] Sortir du nucléaire (FBFC/Romans-sur-Isère-dossierpagina) — UF6-transport vanuit Nederland arriveerde 22-12-2023 slecht verzegeld bij Framatome Romans-sur-Isère (ASNR-inspectiedossier). https://www.sortirdunucleaire.org/FBFC
[6] Wikipedia (fr) — gare-coördinaten: Gare de Narbonne 43.190609/3.005662; Gare de Nîmes 43.832516/4.36634; Gare d'Avignon-Centre 43.94185/4.80472; Gare de Pierrelatte 44.374941/4.703961 (via MediaWiki API, `prop=coordinates`).
[7] Usinenouvelle.com, "Orano mise gros dans l'enrichissement au Tricastin" — investering €1,7 mrd, +30% verrijkingscapaciteit Georges Besse II, opstart vanaf 2028 (algemene Tricastin-context, geen Romans-sur-Isère-koppeling gevonden). https://www.usinenouvelle.com/article/orano-mise-gros-dans-l-enrichissement-au-tricastin.N2199208
[8] ASNR, "Usines Framatome de fabrication de combustibles nucléaires de Romans-sur-Isère" — regelgevend toezichtsdossier, noemt URE-verwerking maar geen expliciete herkomstketen. https://reglementation-controle.asnr.fr/controle/l-asnr-en-region/auvergne-rhone-alpes/usines-framatome-de-fabrication-de-combustibles-nucleaires-de-romans-sur-isere
[9] Wikipedia (en), "Franco-Belge de Fabrication du Combustible" — FBFC/Framatome heeft ook een fabricagevestiging ÓP het Tricastin-terrein zelf, naast Romans-sur-Isère en Dessel (BE); geen bronvermelding voor de Tricastin→Romans-transportketen. https://en.wikipedia.org/wiki/Franco-Belge_de_Fabrication_du_Combustible
[haalbaarheidstoets] Bindend invoerdocument bij deze brief (keten-id `uranium-malvesi-tricastin`) — geen aanpassing nodig, ankers letterlijk hergebruikt, fase D voorwaardelijk laten staan.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Eén been (b1, spoor), vier losse runs in reisvolgorde** (bakhandleiding §2 — een vrije
Dijkstra tussen de site-ankers koos een omweg; geen `--via`-flag op de spoorrouter):

| run | van → naar | modaliteit | km | punten |
|---|---|---|---|---|
| b1a | Orano Malvési → Gare de Narbonne | spoor | 7,1 | 49 |
| b1b | Gare de Narbonne → Gare de Nîmes | spoor | 171,0 | 614 |
| b1c | Gare de Nîmes → Gare d'Avignon-Centre | spoor | 46,5 | 178 |
| b1d | Gare d'Avignon-Centre → Orano Tricastin | spoor | 67,3 | 271 |
| **totaal** | | | **291,9** | **1.112** |

2 markers (`u-malvesi`, `u-tricastin`). `v2/data/stroomroute-uranium-malvesi-tricastin.json`, 19,4 KB.
Recept: `bak_uranium_malvesi_tricastin()` in `v2/tools/bak_stromen.sh` (draaien: `bash v2/tools/bak_stromen.sh
uranium-malvesi-tricastin`). Geometrie: `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs` per run, prefix
`spoorroute-uranium-malvesi-tricastin-<van>-<naar>.geojson` in `v2/build-cache/ais/graaf/`.

**Km-toets:** geen gepubliceerde spoorkm om tegen te toetsen (alleen de hemelsbrede 187 km uit het
ontwerp) — de brief zegt zelf dat de ±15%-norm hier niet geldt, alleen indicatie. Gemeten 291,9 km
tegen 187 km hemelsbreed = **+56,1%**, een normale omwegfactor voor een reële spoorcorridor met
drie corridorkeuzes (Narbonne/Nîmes/Avignon) tegen een rechte lijn.

**Naden:** alle vier op **0,000 km** — de vier runs sluiten exact op elkaar aan (elke `van` van run
n+1 is letterlijk de `naar` van run n).

**Markers:** `u-malvesi` 110,6 m van de lijn · `u-tricastin` 328,1 m — beide binnen de 0,5 km-norm
(bakhandleiding §5.1); het verschil is anker ≠ exacte routeerpunt op het fabrieksterrein/emplacement.

**Toets_rechte_benen:** geen been van deze stroom in de lijst met omwegfactor ≈ 1,000 (alle vier
liggen tussen 1,28 en 2,60 — reële corridors, geen verzonnen rechte lijn).

**Toets_knikken — één terugloop-klasse, bewust niet dichtgeschoven:**
- **b1a + b1b delen precies dezelfde terugloop** op 43,1870/3,0011 (180°, boogstraal ~0-55 m,
  ~0,5 km voorbij Gare de Narbonne) — onafhankelijk gemeten bij twee losse routeerruns
  (`--keerstraf` 25 én 150 geven 'm allebei, op exact dezelfde coördinaat) en dus geen
  routeerartefact van één run. Aannemelijk de echte kop-maak-junctie waar de private
  Narbonne-Malvési-aftakking (4,9 km, vernieuwd 2020, brief §2/[3]) op de hoofdlijn aansluit —
  een private aftakking die richting het zuiden afbuigt vóór de trein noordwaarts naar
  Béziers/Montpellier kan, is een bekend patroon voor dit soort industriële zijlijnen. Niet
  onderzocht binnen het webbudget of dit een letterlijke kopmaak-beweging is of een gladde
  wissel-boog; staat als open punt.
- **b1a heeft daarnaast een tweede, kleinere terugloop** op 43,1950/3,0106 (177°, ~30 m) — zelfde
  klasse, net ervoor.
- **b1d heeft een terugloop** op 43,9380/4,8325 (180°, ~25 m, net na Avignon-Centre) en een
  "scherpe bocht, echt" bij 44,3695/4,7034 (161°, ~28 m, kort voor Tricastin) — de laatste is
  door het tool zelf al als geometrisch echt geclassificeerd (geen reparatie nodig).
- **b1b (Narbonne→Nîmes) is bewust op `--keerstraf=150` gebakken** (i.p.v. de default 25): bij 25
  koos de router een extra terugloop-lus bij 43,8138/4,5126 (108 m boogstraal, ten oosten van
  Nîmes) zonder dat het de route korter maakte; op 150 verdwijnt die lus op exact dezelfde lengte
  (168,0 km bij 25 → 168,0 km bij 150 vóór de laatste snap, 171,0 km in de uiteindelijke bake).
  b1a en b1d bleven op de default 25 — 150 gaf daar juist een omweg (b1d: 110,9 i.p.v. 67,3 km).
- Per saldo: van 5 terugloop-punten (bij default 25 op alle vier) naar **4**, zonder een via-punt
  te verschuiven.

**Geen stippel:** beide site-ankers liggen op het fabrieksterrein/emplacement zelf (Comurhex I
Narbonne, Comurhex II/Georges Besse II Pierrelatte) — geen haven-aanloop, geen zee-been, geen
last-mile-been nodig.

**Fase D vervalt** (brief §6/§7): geen bron binnen het webbudget bevestigt dat Tricastin-verrijkt
uranium naar Framatome Romans-sur-Isère gaat voor déze keten; een gedocumenteerd incident toont
juist UF6-aanvoer bij Romans vanuit Nederland. Niet getekend.

**Modaliteit-correctie t.o.v. het ketenontwerp:** SPOOR, niet truck (brief §1/§7) — Wikipedia (fr)
documenteert de overschakeling in 2014, met een gedateerd 2017-cijfer (320 t U/week); een
tegensprekende bron (homonuclearus.fr, 2020) noemt 3-5 vrachtwagens voor dezelfde route. Gekozen
voor spoor als specifiekere, gedateerde bron; niet binnen het webbudget verder getoetst tegen een
Orano-jaarverslag of ASNR-inspectierapport. `spoornet_nodig: false` uit het ketenontwerp is hiermee
achterhaald — deze keten heeft het spoornet wél nodig (gemeld, ketenontwerp-bestand niet aangeraakt).

**Lessen voor de volgende bak-agent:**
- Een terugloop die op **hetzelfde punt** verschijnt in twee onafhankelijk geroutete benen (b1a en
  b1b delen 43,1870/3,0011) én bij verschillende `--keerstraf`-waarden onveranderd blijft, is
  vermoedelijk een echte kop-maak-junctie, geen routeerartefact — niet wegdrukken met een hogere
  straf, want die straft dan ook de segmenten waar hij wél helpt (zie b1d hieronder).
- `--keerstraf` is **per been** te kiezen, niet globaal: 150 hielp b1b (zelfde lengte, lus weg) en
  verpestte b1d (110,9 i.p.v. 67,3 km, nieuwe terugloop verder noordelijk). Test per been, kies per
  been.

**Open punten (ongewijzigd van §7, niet onderzocht binnen het webbudget van deze bak-ronde):**
modaliteit-tegenspraak spoor/truck · geen gepubliceerde spoorkm · jaarvolume-cijfer uit 2017 ·
exact spoortracé bij het Tricastin-fabrieksterrein · de aard van de Narbonne-Malvési-terugloop
(kopmaak vs. wissel-artefact).
