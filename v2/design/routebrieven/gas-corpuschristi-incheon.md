# Routebrief (licht) · gas — Corpus Christi (VS) → Incheon (Zuid-Korea)

**stroom-id:** `gas-corpuschristi-incheon` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** Amerikaans schaliegas, al vloeibaar gemaakt bij de Cheniere-terminal Corpus Christi
(Texas), per **LNG-tanker** over de Golf van Mexico → Caribische Zee → **Panamakanaal** → Stille Oceaan →
Straat Luzon/Oost-Chinese Zee → Gele Zee naar de KOGAS-regasterminal Incheon, waar het weer pijpleidinggas
wordt en de Zuid-Koreaanse markt in gaat.
**Welke as van het verhaal:** *VS-Golfkust → Zuid-Korea via Panama — het levende Panama-congestieverhaal.*
Corpus Christi > 25 Mtpa in 2026, oplopend naar 28,9 Mtpa bij volledige Stage 3 (Cheniere/LNG Prime,
peiljaar 2026) [1][2]. Het Panamakanaal is in 2026 zelf weer nieuws: een recidiverende El Niño-droogte
dwong de sluizen half augustus/september 2026 tot een tweede ronde slotverkrapping (36 → 34 → 32
doorvaarten/dag), bovenop een structureel beperkt aantal LNG-geschikte Neopanamax-sluisslots [7][8][9].

## 1 · Ketenkaart
```
Corpus Christi LNG (Cheniere) `gas-corpuschristi-kade`
   ──(b1 zee · haven-aanloop, stippel · ~8,0 km)──► zeeknoop 4843 (Golf van Mexico)
   ──(b2 zee · Golf van Mexico → Caribische Zee → Panamakanaal → Stille Oceaan →
       Straat Luzon/Oost-Chinese Zee → Gele Zee · ~16.500–17.500 km, MARNET)──►
   zeeknoop 5633 (bij Incheon)
   ──(b3 zee · haven-aanloop, stippel · ~24,2 km)──►
   Incheon LNG-terminal (KOGAS) `gas-incheon-kade` ── stoppunt
```
(Bij Panama-congestie de-facto omweg via Suez of de Kaap — substantieel langer; blijft in de tekst, niet
als aparte getekende as, zoals in het ketenontwerp aangegeven.)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | Corpus Christi-kade → zeeknoop 4843 | haven-aanloop, La Quinta Channel → Golf van Mexico | ≈ 8,0 [gemeten, zie §9-voorbereiding] | `maak_havenaanloop.py`, terugval rechte stippel | ja — kade ligt 7,98 km van de zeeknoop (> 5 km, LAR-586-regel) |
| b2 | B | zee | zeeknoop 4843 → zeeknoop 5633 | Golf van Mexico → Caribische Zee → Panamakanaal → Stille Oceaan → Straat Luzon/Oost-Chinese Zee → Gele Zee | ~16.500–17.500 [ontwerp/webcheck, geen gepubliceerde ladingroute-lengte — zwakke meetlat, zie olie-habshan-chiba §9-klasse] | MARNET | nee |
| b3 | B | zee | zeeknoop 5633 → Incheon-kade | haven-aanloop, Gele Zee → KOGAS-jetty | ≈ 24,2 [gemeten] | `maak_havenaanloop.py`, terugval rechte stippel | ja — kade ligt 24,17 km van de zeeknoop (> 5 km én tegen de 25 km-max-snap aan) |

Fase A (Eagle Ford/Permian-schaliegasnet → Corpus Christi) **vervalt** — diffuus pijpleidingnet zonder
enkelvoudig anker, zelfde reden als bij de eerste VS-Golfkust-as (§7). Fase C (Incheon-regasterminal →
KOGAS-nationale net) wordt niet als aparte lijn getekend: de regasterminal is zelf het knooppunt waar LNG
weer pijpleidinggas wordt — zie §6.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-corpuschristi-kade` | overslag leiding/LNG → zee (exportterminal, laadsteiger) | Corpus Christi LNG (Cheniere), La Quinta Channel, San Patricio County, Texas | 27.8797, -97.2645 | [3][6] | bron-gelegd (z17 gezien: LNG-tanker afgemeerd aan een steiger met laadarmen op palen, trestle vanaf het terrein; drie liquefactie-trains met bolvormige + cilindrische opslagtanks op het complex 700 m landinwaarts) |
| `gas-incheon-kade` | overslag zee → leiding (regas-/importterminal, offshore jetty) | KOGAS Incheon LNG-basis (Yeonsu-gu, Songdo-kust) | 37.3377, 126.5831 | [4][5][6] | bron-gelegd (z16 gezien: groene LNG-tanker afgemeerd aan een offshore laadplatform met laadarmen, ~1,3 km trestle verbindt het platform met het tankenpark op het KOGAS-terrein aan de kust — 23 opslagtanks zichtbaar op het overzichtsbeeld) |

## 4 · Via-punten
Niet van toepassing: deze keten heeft geen landbenen met een corridorkeuze (fase A vervalt, fase C wordt
niet getekend). Het zeebeen wordt volledig door MARNET geroutet.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Corpus Christi LNG | Cheniere Energy | pijpleidinggas (Eagle Ford/Permian) → LNG | > 25 Mtpa in 2026 (≈ 34,0 bcm/j; 1 Mt LNG ≈ 1,36 bcm), oplopend naar 28,9 Mtpa (≈ 39,3 bcm/j) bij volledige Stage 3; Stage 3 eerste LNG 30-12-2024, project 75,9% gereed per 30-11-2024 | [1][2] |
| Incheon LNG-terminal | KOGAS (Korea Gas Corporation) | LNG → pijpleidinggas | 23 opslagtanks, totale opslag ≈ 2,88 mln m³ LNG (≈ 1,55 Mt); jetty voor 2 ULCC's tot 100.000 t-klasse; bevoorraadt ~70% van de LNG-vraag van de hoofdstedelijke regio (Seoul/Incheon/Gyeonggi) — geen los Incheon-specifiek jaardoorzetcijfer gevonden (zie §7) | [4][5] |

## 6 · Stoppunt
De brief stopt bij de KOGAS Incheon-regasterminal: hier wordt LNG weer pijpleidinggas en gaat het het
Koreaanse nationale net in. Geen bron koppelt een specifieke lading aan één eindgebruiker (stroomcentrale,
industrie of huishoudens) — fase D/E vervallen. De korte terreinleiding naar het KOGAS-invoedpunt (< 5 km,
uit het ketenontwerp) wordt niet als aparte lijn getekend: er is geen gevonden coördinaat voor een
afzonderlijk net-invoedpunt buiten het terminalterrein, en de regasterminal ís zelf al het punt waar LNG
de pijpleidingmarkt in gaat (geen coördinaat verzonnen, werkwijze §1).

## 7 · Open punten
- **Fase A vervalt (Eagle Ford/Permian → Corpus Christi):** diffuus schaliegasnet, geen enkelvoudig
  brongebied of pijpleidingtracé te wijzen — zelfde situatie als bij de eerste VS-Golfkust-as van dit
  project.
- **b2's km is een ontwerp-/webcheck-schatting** (~16.500–17.500 km via Panama), geen gepubliceerde
  ladingroute-lengte — een zwakke meetlat voor een been van deze lengte (vergelijkbare klasse als
  olie-habshan-chiba §9: de gemeten MARNET-km is de bevinding, niet per se de "fout"). Alternatief bij
  Panama-congestie (Suez/Kaap, substantieel langer) blijft alleen tekstueel vermeld, niet als eigen as
  getekend — conform het ketenontwerp.
- **Panama-risicotekst herzien op verse bronnen (2026):** de acute droogtecrisis van 2023-24 is niet
  "opgelost" gebleven — eind augustus/begin september 2026 dwong een nieuwe, El Niño-gedreven droogte de
  Panama Canal Authority tot een tweede verkrappingsronde (36 → 34 → 32 doorvaarten/dag per 3 en 15
  september 2026; Neopanamax-sluizen van 10 naar 9 dagelijkse slots) [7][8]. LNG/LPG-carriers kregen op
  3 september 2026 een eigen prioriteitsgroep met minimaal 3 gegarandeerde sloten/week, maar de
  concurrentie om een gegarandeerde datum blijft duur: SK Gas betaalde op 30-08-2026 een recordbedrag van
  US$ 5,3 mln voor een prioriteitsslot voor de LPG-tanker G. Spirit (1 september 2026) [9]. Conclusie:
  **structurele LNG-slotschaarste, aangescherpt door een terugkerende droogte**, geen doorlopende
  ononderbroken crisis sinds 2023 — de eerdere formulering "actief, meetbaar knelpunt" alsof het één
  onafgebroken episode was, is hiermee genuanceerd.
- **Incheon-specifiek jaardoorzetcijfer (bcm/j) niet gebrond** — alleen opslag-/steigercapaciteit en het
  aandeel in de regionale vraag zijn gevonden; een Corpus Christi→Incheon-specifiek ladingvolume (los van
  het totale Golfkust→Azië-exportcijfer) is niet apart gebrond.
- **Aandeel van Corpus Christi in Zuid-Korea's totale LNG-import** niet gebrond binnen het webbudget.
- **Zeeknoop-afstanden zijn vooraf gemeten** (Corpus Christi-kade 7,98 km tot zeeknoop 4843; Incheon-kade
  24,17 km tot zeeknoop 5633) met het script uit de bak-handleiding §2 — nog niet bevestigd door een echte
  bake; bij het bakken kan de exacte snap een fractie afwijken.

## 8 · Bronnen
[1] Cheniere Energy / LNG Prime, peiljaar 2026 — Corpus Christi LNG > 25 Mtpa in 2026, oplopend naar
28,9 Mtpa bij volledige voltooiing van Stage 3 (cijfer overgenomen uit het ketenontwerp van deze golf).
[2] Wikipedia, "Cheniere Energy" — Corpus Christi Stage 3: eerste LNG 30-12-2024, Bechtel als
hoofdaannemer, bouw gestart medio 2022, +10 Mt/j capaciteit, project 75,9% gereed per 30-11-2024.
https://en.wikipedia.org/wiki/Cheniere_Energy
[3] OpenStreetMap/Photon (ODbL) — "LNG Train 1/2/3", La Quinta Road, Corpus Christi LNG Terminal, San
Patricio County, Texas (osm_id 1158988516/17/18, ~27,890/-97,270). https://photon.komoot.io
[4] OpenStreetMap/Photon (ODbL) — landuse "한국가스공사 인천 LNG기지" (KOGAS Incheon LNG-basis), Yeonsu-gu,
Incheon (osm_id 228335487, centroïde 37,3525/126,6038). https://photon.komoot.io
[5] Riviera / Korea Times / Offshore Technology (via websearch, geaggregeerd) — Incheon LNG-terminal: 23
opslagtanks (11× 89.400 t, 10× 44.700 t, 2× 62.580 t), totale opslag > 1,55 mln t / ≈ 2,88 mln m³
(10× 100.000 m³ bovengronds + 2× 140.000 m³ + 8× 200.000 m³ ondergronds), regascapaciteit 6.270 t/uur, 8,7
km uit de kust op opgespoten terrein (990.000 m²), jetty voor 2 ULCC's tot 100.000 t, bevoorraadt Seoul/
Incheon/Gyeonggi (~70% van de nationale LNG-vraag). https://www.rivieramm.com/news-content-hub/news-content-hub/big-tanks-and-plans-for-kogas-46090
· https://www.koreatimes.co.kr/business/20240630/kogas-bolsters-energy-security-with-worlds-biggest-lng-terminal
· https://www.offshore-technology.com/projects/inchon/
[6] Esri World Imagery via `v2/tools/sat_check.py` (z14–z17, live) —
`v2/build-cache/satcheck/sat-gas-corpuschristi-incheon-corpuschristi-overzicht.png`,
`sat-gas-corpuschristi-incheon-corpuschristi-kade.png`,
`sat-gas-corpuschristi-incheon-corpuschristi-jetty.png` (LNG-tanker aan de laadsteiger),
`sat-gas-corpuschristi-incheon-incheon-overzicht.png`, `sat-gas-corpuschristi-incheon-incheon-kade.png`,
`sat-gas-corpuschristi-incheon-incheon-jetty2.png` (LNG-tanker aan het offshore laadplatform).
[7] Wikipedia, "Panama Canal" — na de Iran-oorlog verkeerstoename tot 10%, vooral LNG-carriers VS→Azië;
Panama Maritime Authority nam Balboa/Cristobal over (23-02-2026); Transit Slot Auction System, augustus
2026: SK Gas record US$ 5,3 mln voor de LPG-tanker G. Spirit (1 september 2026) tijdens verhoogde vraag
naar transitsloten en droogte-/El-Niño-gerelateerde beperkingen. https://en.wikipedia.org/wiki/Panama_Canal
[8] Rio Times Online, 31-08-2026 — Panama Canal Transits Cut to 34 a Day as Drought Tightens Shipping
Again: El Niño-droogte, Gatún Lake onder verwachting ondanks regenseizoen; 3 september 36→34, 15 september
→32 dagelijkse doorvaarten; Neopanamax-sluizen 10→9 sloten, Panamax 26→25→23; nieuw viergroepen-
boekingssysteem, LNG/LPG als eerste prioriteitsgroep. https://www.riotimesonline.com/panama-canal-transit-cuts-september-2026/
[9] gCaptain, 30-08-2026 — Panama Canal Loosens Neopanamax Booking Rules as Capacity Tightens: "a
deteriorating water outlook", ~8 maanden verwachte El Niño-duur, Neopanamax-capaciteit 63 sloten/week →
9 dagelijkse sloten per 3-09-2026, LNG-vaartuigen minimaal 3 gegarandeerde sloten/week.
https://gcaptain.com/panama-canal-loosens-neopanamax-booking-rules-as-capacity-tightens/

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `gas-corpuschristi-incheon`** → `v2/data/stroomroute-gas-corpuschristi-incheon.json` — 3 benen,
**18.833,3 km**, 1.951 punten, 2 markers. zee 8,0 (stippel) + 18.801,1 + 24,2 (stippel) = 18.833,3 km. Recept:
`bak_stromen.sh` (functie `bak_gas_corpuschristi_incheon`).

**b1 (zee, haven-aanloop Corpus Christi, RECHTE STIPPEL):** `timeout 300 python v2/tools/maak_havenaanloop.py
--van 27.8797,-97.2645 --naar 27.81110,-97.24070` liep vast op `timeout 300` (exit 124) — geen tweede poging.
Rechte stippel **7,979 km** (2 punten) tussen kade en zeeknoop 4843, exact het vooraf gemeten getal uit de brief
(≈8,0 km). Reden voor de haven-aanloop: kade 7,98 km van de zeeknoop, > 5 km (LAR-586), ook al valt dat ruim
binnen de 25 km-max-snap.

**b2 (zee, MARNET, geroutet):** `--been "zee|...|27.81110,-97.24070|37.16690,126.41420"` — snap op beide
zeeknopen 0,000 km. Resultaat **18.801,1 km over 100 MARNET-edges** (1.931 punten). Tegen de brief-schatting
(~16.500–17.500 km, zelf al een ontwerp-/webcheck-schatting, geen gepubliceerde ladingroute-lengte): **+7,4%**
t.o.v. de bovengrens (17.500) en **+13,9%** t.o.v. de ondergrens (16.500) — binnen de ±15%-norm, ondanks de
zwakke meetlat (zelfde klasse als olie-habshan-chiba §9). Lengte-invariant: getekende lijn 18.801,138 km vs som
edge-km 18.801,200 km = −0,062 km (de naden). De route loopt via het Panamakanaal zoals verwacht (`northwest`-
passage blijft dicht); geen via-punt bijgeschoven.

**b3 (zee, haven-aanloop Incheon, GEMETEN):** `timeout 300 python v2/tools/maak_havenaanloop.py --van
37.16690,126.41420 --naar 37.3377,126.5831` vond een pad over water op de trap "cel 0,01° kaal" — **24,2 km,
18 punten, 0,00 km over land**, omwegfactor 1,000 tegen de rechte lijn (24,2 km). Exact het vooraf gemeten
getal uit de brief (≈24,2 km). Reden voor de haven-aanloop: kade 24,17 km van de zeeknoop, > 5 km (LAR-586) én
tegen de 25 km-max-snap aan.

**Toets naden:** alle overgangen **0,000 km** — beide haven-aanlopen sluiten exact aan op de uiteinden van het
geroutete zeebeen (b2 begint/eindigt op dezelfde zeeknopen waar b1/b3 op uitkomen).

**`toets_knikken.py`:** 2 knikken ≥60°, **0 omkeringen ≥150°** (dus 0 terugloop) — beide knikken zijn krappe
bochten op het zeebeen (93,7° bij 34,15270/125,57370 nabij Korea; 71,8° bij 9,11830/-79,80320 bij het
Panamakanaal), geen fout.

**`toets_rechte_benen.py --min-km 5`:** b1 (8,0 km, omwegfactor 1,003) en b3 (24,2 km, omwegfactor 1,001) komen
beide in de uitslag als "stippel" — verwacht en correct: het zijn haven-aanlopen die bewust als stippel staan
(§2 van de handleiding), geen verkapte rechte hoofdbenen.

**json geldig:** versie 2, punt_formaat lonlat, modaliteit uitsluitend {zee} (binnen de toegestane set), elk
been ≥2 punten (minimum 2), bestandsgrootte **37,2 KB** (ruim < 300 KB-richtwaarde).

**Markers:** Corpus Christi LNG (Cheniere) 0,0 m · Incheon LNG-terminal (KOGAS) 0,0 m — beide liggen exact op
hun eigen stippel-uiteinde (kop en staart van de hele stroom), zoals bedoeld.

**Gereedschapslessen:** geen nieuwe — beide haven-aanlopen volgden precies het bakhandleiding-§2-patroon (één
poging onder `timeout 300`, terugval op een rechte stippel bij exit 124, geen tweede poging). Tijdens het
draaien van de bake ontstond eenmalig een `syntax error` in `bak_stromen.sh` doordat een andere golf-2-agent
het bestand op hetzelfde moment bewerkte (parallelle sessies, zie STAP 0 van de opdracht); de bake zelf had op
dat moment al `v2/data/stroomroute-gas-corpuschristi-incheon.json` geschreven en het bestand was bij controle
achteraf weer syntactisch geldig — geen actie nodig.
