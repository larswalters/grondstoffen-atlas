# Routebrief (licht) · Uranium — Smith Ranch-Highland (Wyoming) → Metropolis Works (Illinois)

**stroom-id:** `uranium-smithranch-metropolis` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken
**Keten in één zin:** yellowcake (U₃O₈) van de Smith Ranch-Highland ISR-mijn (Cameco Resources, Converse County,
Wyoming — de grootste uraanproductiefaciliteit van de VS) per **truck** dwars door Wyoming, Nebraska en Iowa
(I-25 → I-80, bewust om Colorado heen) en zuidwaarts door Illinois (I-39/I-74/I-57) naar de Honeywell/ConverDyn
Metropolis Works-conversiefabriek — de enige commerciële UF6-conversiefabriek van de VS, stoppunt.
**Welke as van het verhaal:** de binnenlandse VS-schakel tussen ISR-mijnbouw in het Powder River Basin en de
Amerikaanse UF6-conversiecapaciteit (~15.000 tU/j, ~20% van de wereldcapaciteit) — geen zeetraject, één lange
binnenlandse truckcorridor die bewust Colorado mijdt (extract ontbreekt daar, zie §7).

## 1 · Ketenkaart
```
Smith Ranch-Highland ISR-mijn `u-smithranch-mijn` ──(b1 A truck · I-25 zuid (Douglas–Cheyenne) → I-80 oost
(Wyoming–Nebraska–Iowa) → I-39/I-74/I-57 zuid door Illinois · ~2.090 km, indicatie)──►
Honeywell/ConverDyn Metropolis Works `u-metropolis-conversie` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Smith Ranch-Highland ISR-mijn → Honeywell/ConverDyn Metropolis Works | I-25 zuid (Douglas–Cheyenne) → I-80 oost (Wyoming–Nebraska–Iowa) → I-39 zuid → I-74 → I-57 zuid → lokale weg naar de fabriek | ~2.090 [1, indicatie — algemene Wyoming-brede claim "over 1.300 miles", niet route-specifiek; ±15%-toets geldt als indicatie, niet als norm] | maak_stroombeen_weg (extracts us-wyoming, us-nebraska, us-iowa, us-illinois) | nee — *aannemelijk: één bron voor de mijnkeuze* (geen bron bevestigt individueel dat specifiek Smith Ranch-Highland i.p.v. een andere Cameco-ISR-site deze route volgt; SRH is de grootste/oudste WY-ISR-site en daarmee de meest aannemelijke keuze, zie §7) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-smithranch-mijn` | mijn (ISR, kop) | Smith Ranch-Highland (Cameco Resources), Converse County, Wyoming | 43.0537, -105.6851 | [2][6] | bron-gelegd (z15 gezien: verwerkingscomplex met gebouwen, tanks en verharde erven midden in de steppe, toegangswegen naar een doorgaande onverharde hoofdweg, windturbines in de omgeving — Wikipedia-infobox-coördinaat pageid 17670884, 4 decimalen, exact op het complex) |
| `u-metropolis-conversie` | conversiefabriek (U₃O₈ → UF6, stoppunt) | Honeywell Uranium Hexafluoride Processing Facility / ConverDyn Metropolis Works, Illinois | 37.1718, -88.7570 | [3][7] | bron-gelegd (z16 gezien: groot ommuurd fabrieksterrein met tanks, hallen en verharde erven, eigen toegangsweg naar een wegkruising 3 km NW van de stad Metropolis, aan een inham van de Ohio-rivier) — **⚠️ correctie op de sitelaag:** het bestaande anker `w-metropolis` in `v2/design/uranium-sitelaag.json` staat op 37.1500,-88.7333 (status "aannemelijk", "geen satellietblik deze ronde") — dat punt ligt **~3,2 km ZO, midden in de stad Metropolis** (stadscentrum-achtig, geen terrein). Deze brief gebruikt daarom de Wikipedia-infobox-coördinaat (pageid 1801875) i.p.v. het letterlijk hergebruikte sitelaag-punt; zie §7 en het rapport aan de orkestrator — de sitelaag zelf is niet gewijzigd (buiten mijn bestanden). |

## 4 · Via-punten (b1 — corridorkeuzes op I-25/I-80/I-39/I-74/I-57)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Douglas, WY (I-25-knooppunt) | 42.7561, -105.3878 | dichtstbijzijnde I-25-oprit bij de mijn (~35 km); pint de I-25-corridor i.p.v. een diagonale sluiproute door Colorado |
| b1 | 2 | Cheyenne, WY (I-25/I-80-knooppunt) | 41.1400, -104.8202 | hier draait de route van zuid (I-25) naar oost (I-80) — de "Casper–Cheyenne → I-80 oost"-knik uit het ketenontwerp |
| b1 | 3 | North Platte, NE (I-80-knooppunt) | 41.1239, -100.7654 | enige doorgaande I-80-corridor door West-Nebraska, geen alternatieve hoofdroute |
| b1 | 4 | Lincoln, NE (I-80-knooppunt) | 40.8136, -96.7026 | laatste grote knooppunt in Nebraska vóór de Missouri-oversteek |
| b1 | 5 | Council Bluffs, IA (I-80, Missouri-oversteek) | 41.2619, -95.8608 | staatsgrens-oversteek Nebraska→Iowa, enige I-80-brug in deze corridor |
| b1 | 6 | Des Moines, IA (I-80-knooppunt) | 41.5868, -93.6250 | hoofdknooppunt in Iowa vóór de afslag zuidwaarts naar Illinois |
| b1 | 7 | LaSalle-Peru/Utica, IL (I-80/I-39-knooppunt) | 41.3283, -89.1310 | hier verlaat de route I-80 en gaat zuidwaarts op I-39 — pint de "zuidwaarts door Illinois (I-39/I-57)"-knik |
| b1 | 8 | Marion, IL (I-57-knooppunt) | 37.7273, -88.9331 | laatste hoofdweg-knooppunt vóór de lokale aansluiting naar Metropolis Works, i.p.v. via US-45 direct vanaf Mount Vernon |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Metropolis Works | Honeywell / ConverDyn (Honeywell-Ge­neral Atomics JV, verkoopagent) | U₃O₈ (yellowcake, binnenlands + geïmporteerd) → UF6 | vergunde/nominale capaciteit ~15.000 tU/j als UF6, ~20% van de wereldconversiecapaciteit; enige commerciële VS-conversiefabriek | [3][4][7] |

## 6 · Stoppunt
De brief stopt bij Metropolis Works: dat is het opgedragen keten-eindpunt (naar_site = stoppunt). Metropolis
Works is zelf de conversiestap (U₃O₈ → UF6); geen bron noemt een specifieke vervolgbestemming (verrijker) voor
déze zending, dus fase D vervalt.

## 7 · Open punten
- **De sitelaag-anchor `w-metropolis` (37.1500,-88.7333) ligt ~3,2 km van de echte fabriek** — een stadspunt in
  Metropolis zelf, niet het terrein. Deze brief gebruikt de satelliet-bevestigde Wikipedia-coördinaat
  (37.1718,-88.7570) voor `u-metropolis-conversie`. De sitelaag zelf is bewust niet aangepast (buiten mijn
  bestanden) — gemeld voor de orkestrator/sitelaag-beheerder.
- **Km-schatting (~2.090 km, "over 1.300 miles") is een algemene Wyoming-brede claim** uit één artikel
  (Cowboy State Daily/WSGS), niet specifiek bevestigd voor déze route Smith Ranch-Highland → Metropolis. Per de
  haalbaarheidstoets geldt de ±15%-toets hier als indicatie, niet als harde norm.
- **Geen bron bevestigt individueel dat specifiek Smith Ranch-Highland** (i.p.v. Lost Creek, Lance of een andere
  Cameco/Wyoming-ISR-site) deze exacte route volgt — de bron spreekt over "Wyoming-producenten" in het algemeen.
  Smith Ranch-Highland is als grootste/oudste WY-ISR-site de meest aannemelijke keuze, niet individueel bevestigd.
- **Geen actueel (2024/25) productiecijfer voor Smith Ranch-Highland gevonden binnen het webbudget** — alleen het
  historische gemiddelde 2002-2011 (~15 miljoen lbs U₃O₈, ~680 tU/j) is beschikbaar.
- **us-colorado-extract ontbreekt** (bevestigd: niet in `v2/build-cache/geofabrik/`) — geen blokkerend probleem,
  want de gekozen corridor (I-25 → I-80 via Nebraska/Iowa → Illinois) vermijdt Colorado bewust; wel de reden
  waarom een kortere Denver/I-70-route niet gekozen kan worden.
- **De laatste-mijl-aansluiting van de mijn op I-25 (via Douglas, WY) is niet individueel gebrond** — bij het
  bakken kan blijken dat het ISR-terrein > ~2 km van het gekarteerde net ligt; dan volgt daar een stippel
  "last mile (geen net op deze korrel)" volgens de vaste regels van de kaart.
- **Overlap:** geen — stroom-id bestaat nog niet in `v2/data/`, en geen andere golf-5-as of bestaande stroom raakt
  Wyoming/Nebraska/Iowa/Illinois op deze corridor (bevestigd in de haalbaarheidstoets).

## 8 · Bronnen
[1] Cowboy State Daily / Wyoming State Geological Survey, sept. 2025 — "Wyoming In Running For Major Uranium
Facility In Push For U.S. Fuel Security": "over 1,300 miles" voor uraantransport van Wyoming-producenten naar
Metropolis, Illinois (algemene claim, niet route-specifiek).
https://cowboystatedaily.com/2025/09/03/wyoming-in-running-for-major-uranium-facility-in-push-for-u-s-fuel-security/
[2] Wikipedia, "Smith Ranch-Highland" (pageid 17670884) — "largest uranium production facility in the United
States", ISR-methode, Smith Ranch + Highland als één operatie met centrale verwerkingsfaciliteit, 15 miljoen lbs
U₃O₈ geproduceerd 2002-2011, coördinaat 43.05373611,-105.68508889.
https://en.wikipedia.org/wiki/Smith_Ranch-Highland
[3] Wikipedia, "Honeywell Uranium Hexafluoride Processing Facility" (pageid 1801875) — "located 1.9 miles (3 km)
northwest of Metropolis, Illinois", nominale capaciteit 15.000 tU/j als UF6, ConverDyn (Honeywell/General
Atomics) als exclusief verkoopagent, coördinaat 37.171768,-88.757039.
https://en.wikipedia.org/wiki/Honeywell_Uranium_Hexafluoride_Processing_Facility
[4] v2/design/uranium-sitelaag.json — bestaand anker `w-metropolis` (37.1500,-88.7333, status "aannemelijk"),
capaciteitsbron Honeywell/NRC ~15.000 tU/j UF6, "enige uraanconversiefabriek van de VS"; hergebruikt voor de
capaciteitscijfers, niet voor de coördinaat zelf (zie §3/§7).
[5] Wyoming State Geological Survey — "WSGS 2024 Uranium Summary" (achtergrondbron voor Wyoming-uraanproductie,
niet individueel geciteerd op een SRH-2024/25-cijfer binnen het webbudget).
https://www.wsgs.wyo.gov/products/wsgs-2024-uranium-summary.pdf
[6] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) —
`v2/build-cache/satcheck/sat-uranium-smithranch-metropolis-smithranch.png`.
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15+z16, live) —
`v2/build-cache/satcheck/sat-uranium-smithranch-metropolis-metropolis.png` (sitelaag-punt, stadscentrum-achtig) en
`v2/build-cache/satcheck/sat-uranium-smithranch-metropolis-metropolis2.png` (Wikipedia-coördinaat, echte fabriek).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Eén been, geometrie via `maak_stroombeen_weg.py`** (profiel `uranium-smithranch-metropolis`,
extracts us-wyoming/us-nebraska/us-iowa/us-illinois, `--bron geofabrik`, vensterKm 70):

| # | modaliteit | van → naar | km | markers | stippel? |
|---|---|---|---|---|---|
| b1 | truck | Smith Ranch-Highland ISR-mijn → Metropolis Works | 2.161,9 | — | nee |

**Totaal: 2.161,9 km · 16.938 punten · 2 markers · 347,9 KB.**

**Toets (bakhandleiding §5):**
- **Lengte:** 2.161,9 km tegen de indicatie ~2.090 km (algemene Wyoming-brede claim, geen
  route-specifieke wegkm) = **+3,4%** — de ±15%-toets geldt hier zoals afgesproken als
  indicatie, niet als harde norm; +3,4% ligt ruim binnen elke redelijke marge.
- **Naden:** 0,00 km (enig been, geen aansluitend been).
- **Markers:** beide op 0,000 km van de lijn (de mijn- en fabrieksankers zijn zelf het
  begin/eind van de getekende geometrie).
- **`toets_knikken.py`:** 59 knikken ≥ 60°, **0 omkeringen ≥ 150°, 0 terugloop** — allemaal
  kleine straal-spikes (4–58 m) op een echte wegkaart (klaverbladlussen/op-/afritten op de
  I-25/I-80/I-39/I-57-knooppunten); geen enkele hoort gerepareerd te worden.
- **`toets_rechte_benen.py --min-km 5`:** geen match voor dit been (omwegfactor ≠ 1,000 —
  het volgt een echte, kromme wegcorridor, geen kaarsrechte lijn).
- **JSON-contract:** `versie` 2 · `punt_formaat` "lonlat" · modaliteit `truck` (geldige sleutel)
  · been heeft 16.938 ≥ 2 punten · bestand 347,9 KB.
  ⚠️ **Bevinding:** 347,9 KB ligt net boven de indicatieve ~300 KB uit de handleiding §5.3 —
  komt van de hoge puntdichtheid over een lang been (2.162 km, geen simplify toegepast door
  `maak_stroombeen_weg.py`); geen actie ondernomen (geen norm, alleen een indicatie).

**Stippels/aanlopen/vluchten/leiding:** geen — deze stroom heeft alleen fase A (truck), geen
zee/spoor/leiding/lucht (bak_aanwijzingen bevestigd). Geen last-mile-stippel nodig: de scan
vond een doorlopend wegpad tot vlak bij beide ankers (plant → weg 0,06 km, weg → kade 0,03 km),
beide ruim onder de "> ~2 km"-drempel voor een last-mile-stippel.

**Lessen / bevindingen voor het rapport:**
- De km-indicatie (~2.090 km, één Wyoming-brede krantenclaim) hield goed stand tegen de
  gemeten routegeometrie (+3,4%) — een toevallige bevestiging, geen brongegeven dat déze
  precieze corridor beschrijft (brief §7 blijft van kracht: SRH als mijnkeuze is aannemelijk,
  niet individueel gebrond).
- us-colorado ontbreekt inderdaad lokaal (bevestigd), maar blokkeerde niets: de corridor
  mijdt Colorado bewust via Wyoming/Nebraska/Iowa/Illinois.
- **Sitelaag-discrepantie voor de orkestrator (niet zelf gewijzigd):** `v2/design/uranium-sitelaag.json`
  anker `w-metropolis` (37.1500,-88.7333, status "aannemelijk") ligt ~3,2 km ZO van de echte
  fabriek — deze stroom gebruikt de satelliet-/Wikipedia-bevestigde coördinaat (37.1718,-88.7570)
  als eigen anker `u-metropolis-conversie` in plaats van het sitelaag-punt.
