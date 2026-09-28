# Routebrief (licht) · Kolen · Mount Arthur (Muswellbrook) → Newcastle → Hekinan (Japan)

**stroom-id:** `kolen-muswellbrook-hekinan` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** thermische kolen van de Mount Arthur-mijn (BHP) bij Muswellbrook, Hunter Valley (NSW), per
**spoor** ~140 km via Muswellbrook–Singleton–Maitland naar de PWCS-kolenterminal op Kooragang Island, Port of
Newcastle, per **zeeschip** ~7.700–7.900 km over de Tasmanzee en de westelijke Stille Oceaan (geen
Zuid-Chinese-Zee-doorsteek) naar de kolenkade van Hekinan Thermal Power Station (JERA), Aichi — stoppunt: de
kolen wordt daar verstookt, er is geen fysiek product om verder te volgen.
**Welke as van het verhaal:** *Australië-thermisch (Hunter Valley/NSW → Newcastle) → Japan — de vaste, premium
JERA-relatie gemeten.* Newcastle is 's werelds grootste én drukste kolenexporthaven (150,5 Mt in 2013, sindsdien
gegroeid) [1][2]; JERA (fusie Chubu Electric + TEPCO Fuel & Power) neemt ~13% van de Australische thermische-
kolenexport af [7], en Hekinan is Japans grootste kolencentrale (4.100 MW, operator JERA) [5][6]. Zoals het
ontwerp zelf al zegt: dit is de best gedocumenteerde maar ook meest voor de hand liggende as — het nieuwe zit in
de gemeten geometrie, niet in een nieuw handelsverhaal. De exacte Newcastle→Hekinan-tonnage is niet gebrond op
ladingniveau — open punt tot het bakken (JERA/METI-importstatistiek).

## 1 · Ketenkaart
```
Mount Arthur-mijn (BHP) `kolen-arthur-laad`
  ──(b1 spoor · Main Northern-lijn via Muswellbrook–Singleton–Maitland · ~140 km)──►
  PWCS Kooragang Island `kolen-newcastle-kade`
  ──(b2 zee · Tasmanzee → westelijke Stille Oceaan, haven-aanloop beide kanten · ~7.700–7.900 km)──►
  Hekinan Thermal Power Station `kolen-hekinan-kade` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Mount Arthur-laadstation → PWCS Kooragang Island | Main Northern-lijn (Aurizon) via Muswellbrook–Singleton–Maitland-junctie | ~140 (eigen schatting: rechte-lijnsom via-punten 117 km + bochtmarge; gepubliceerde lijnlengte niet gevonden) | toets_spoorroute (extract australie) | nee — laadstation-spur bij de mijn en kade-aansluiting bij PWCS blijven mogelijk korte stippels |
| b2 | B | zee | PWCS Kooragang Island → Hekinan Thermal Power Station | Tasmanzee → westelijke Pacific-route (geen Zuid-Chinese-Zee) | ~7.687 (eigen grote-cirkelberekening) tegen ~7.900 (ontwerp-webcheck) | MARNET (hecht_marnet.py route); beide uiteinden > 5 km van hun MARNET-zeeknoop | aanloop: **ja, beide kanten** (Newcastle 46,5 km, Hekinan 22,7 km tot de dichtstbijzijnde zeeknoop — bakhandleiding §2, sinds 2026-09-28) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-arthur-laad` | mijn / laadstation | Mount Arthur coal mine (BHP), Muswellbrook, NSW — grootste kolenmijn van NSW | -32.3340, 150.8530 | [3] | bron-gelegd (z14 gezien: enorme open dagbouwput met terrassen, stockpiles, verwerkingscomplex en wegen; anker ligt op de rand van het actieve mijnterrein) |
| `kolen-newcastle-kade` | overslag zee | Port Waratah Coal Services, Kooragang Island, Port of Newcastle | -32.8785, 151.7735 | [1][2][8] | bron-gelegd (z15 gezien: kilometerslange kolenstockyards met laadkranen op rails, spoorlijnen, twee bulkcarriers gemeerd aan de kade) |
| `kolen-hekinan-kade` | losplek zee / stoppunt | Hekinan Thermal Power Station (JERA), kolenstockyard + jetty, Kinuura-baai | 34.8478, 136.9535 | [5][9] | bron-gelegd (z16 gezien: kolenstockyard met acht lange stapels en onlaadkranen op rails, twee bulkcarriers gemeerd aan de westkade, conveyors naar het centraleterrein ernaast) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Muswellbrook | -32.2674, 150.8903 | eerste stationspunt waar het mijn-laadspoor op de Main Northern-lijn aansluit [3][4] |
| b1 | 2 | Singleton | -32.5718, 151.1654 | doorgaand punt op de Main Northern-lijn, sluit een omweg via lokale mijnsidings uit |
| b1 | 3 | Maitland-junctie | -32.7381, 151.5520 | hier splitst de Main Northern-lijn van de North Coast-lijn — pint de route naar Newcastle in plaats van noordwaarts [4] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Hekinan Thermal Power Station | JERA (Chubu Electric + TEPCO Fuel & Power) | thermische kolen → elektriciteit | 4.100 MW, grootste kolencentrale van Japan; 1e unit 1991 | [5][6] |

## 6 · Stoppunt
De brief stopt bij de kolenkade/stockyard van Hekinan Thermal Power Station: de kolen wordt daar verstookt tot
elektriciteit, er is geen verder fysiek grondstofproduct om te volgen (dezelfde redenering als de kolenbrief
Sangatta→Mundra) — fase D/E bestaan hier niet.

## 7 · Open punten
- **Mijnkeuze binnen het Hunter Valley-cluster:** het ontwerp liet de exacte mijn open ("exacte mijn te kiezen
  bij bake"); Mount Arthur is gekozen als grootste NSW-mijn met een bronvermeld spoorbeen naar Newcastle [3],
  maar geen bron legt een specifieke Newcastle→Hekinan-lading bij Mount Arthur alleen (blend-praktijk in de
  Hunter Valley Coal Chain, net als bij Goonyella/BMA-cokeskool).
- **Exacte Newcastle→Hekinan-tonnage niet gebrond** — JERA neemt ~13% van de Australische thermische export af
  [7], Port of Newcastle >150 Mt/jr totaal [1][2]; geen bron splitst dit naar één schip-naar-schip-relatie.
  Te verifiëren via JERA/METI-importstatistiek bij het bakken.
- **Gepubliceerde spoorlijnlengte Muswellbrook–Newcastle niet gevonden** — ~140 km is een eigen schatting uit de
  via-punten; de bake meet het exacte getal over het 1-op-1-spoornet.
- **Zeebeen-afstand:** eigen grote-cirkelberekening (7.687 km) tegen het ontwerp-webcheck (~7.900 km, een
  geschatte vaarroute); de bake meet het exacte MARNET-getal.
- **Beide zee-uiteinden liggen > 5 km van hun MARNET-zeeknoop** (Newcastle 46,5 km, Hekinan 22,7 km) — beide
  krijgen een haven-aanloop per de regel van 2026-09-28 (bakhandleiding §2), ook al snapt Hekinan binnen de
  25 km-marge.
- **Laadstation-spur bij Mount Arthur en kade-aansluiting bij PWCS** zijn niet apart geverifieerd op het
  1-op-1-spoornet; mogelijk korte stippels net als bij Goonyella (loadout-spur, kade-aansluiting).

## 8 · Bronnen
[1] Wikipedia, Port of Newcastle — 's werelds grootste/drukste kolenexporthaven, coördinaten -32.91667/151.8,
    faciliteiten PWCS/NCIG op Kooragang Island. https://en.wikipedia.org/wiki/Port_of_Newcastle
[2] Wikipedia, Hunter Valley Coal Chain — doorvoer 150,5 Mt (2013, tegen 68 Mt in 2000); mijn → spoor (vrijwel
    uitsluitend) → Port of Newcastle → PWCS/NCIG-stockyards → schip. https://en.wikipedia.org/wiki/Hunter_Valley_Coal_Chain
[3] Wikipedia, Mount Arthur coal mine — grootste kolenmijn van NSW, BHP, 20 Mtpa capaciteit, coördinaten
    -32.334/150.853, "coal is moved by Aurizon via the Main Northern railway line to the Port of Newcastle for
    export". https://en.wikipedia.org/wiki/Mount_Arthur_coal_mine
[4] Wikipedia, Maitland railway station — junctiestation van de Main Northern-lijn en de North Coast-lijn,
    coördinaten -32.738073/151.552016. https://en.wikipedia.org/wiki/Maitland_railway_station
[5] Wikipedia, Hekinan Thermal Power Station — operator JERA, grootste kolencentrale van Japan (4.100 MW),
    gebouwd op ingepolderd land aan de westkust van Kinuura-baai, coördinaten 34.83528/136.96219.
    https://en.wikipedia.org/wiki/Hekinan_Thermal_Power_Station
[6] Wikipedia, Chubu Electric Power — Hekinan Thermal Power Station (Coal, 4.100 MW); alle thermische centrales
    per april 2019 overgedragen aan JERA (joint venture Chubu Electric + TEPCO Fuel & Power).
    https://en.wikipedia.org/wiki/Chubu_Electric_Power
[7] IEEFA, "Hunter Valley coal contracts point to terminal decline" — JERA neemt ~13% van de Australische
    thermische-kolenexport af. https://ieefa.org/resources/hunter-valley-coal-contracts-point-terminal-decline
[8] OpenStreetMap (via Photon) — Port Waratah Coal Services Kooragang, landuse-vlak, coördinaten
    -32.878501/151.7735145. https://photon.komoot.io/
[9] OpenStreetMap (via Photon) — 碧南火力発電所 (Hekinan Thermal Power Station), landuse-vlak, coördinaten
    34.840963/136.9604189 (centroïde; anker verfijnd op satellietbeeld naar de kolenkade).
    https://photon.komoot.io/
[10] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16) —
    `v2/build-cache/satcheck/sat-kolen-muswellbrook-hekinan-arthur-laad.png`,
    `sat-kolen-muswellbrook-hekinan-newcastle-kade.png`, `sat-kolen-muswellbrook-hekinan-hekinan-kade-v2.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom:** `kolen-muswellbrook-hekinan` · **bestand:** `v2/data/stroomroute-kolen-muswellbrook-hekinan.json`
(28,3 KB) · **recept:** `bak_kolen_muswellbrook_hekinan` in `v2/tools/bak_stromen.sh` · **8 benen, 3 markers,
totaal 8.331,9 km.**

**b1 (spoor, vier runs op het 1-op-1-net, extract australie, `BAKE_SUFFIX=-raw`):** kop→via/via→via/via→staart
(geen `--via`-vlag op de spoorrouter) — Mount Arthur → Muswellbrook 25,9 km + Muswellbrook → Singleton 49,4 km
+ Singleton → Maitland-junctie 46,8 km + Maitland-junctie → PWCS Kooragang Island 30,0 km = **152,1 km**, plus
de mijn-laadspoor-stippel (4,4 km) = **156,5 km totaal tegen de brief-schatting ~140 km (+11,8 %, binnen
±15 %)**. Het Mount Arthur-anker snapt 4,37 km van het hoofdnet (mijnemplacement niet in het 1-op-1-net,
Goonyella/Jinzhou-klasse) → `--stippel "spoor|laadspoor Mount Arthur-mijn → hoofdspoor|…"`. De PWCS-kade-
aansluiting snapt 0,41 km — onder de marker-/stippelnorm, geen aparte stippel (anders dan bij Goonyella's
HPCT).

**b2 (zee, MARNET-router, BEIDE kanten een haven-aanloop, LAR-586 2026-09-28):** Newcastle-kade ligt 46,5 km
van zeeknoop 2707 (`-33,00000/152,25000`, > 25 km max-snap) → `--been zee` gebruikt de ZEEKNOOP rechtstreeks
als beginpunt; `maak_havenaanloop.py --van -32.8785,151.7735 --naar -33.00000,152.25000` gaf in één poging een
geslaagd pad (49,8 km, 46 punten, 2,81 km over land — uitsluitend aan het kade-uiteinde, de kustkorrel, geen
fout) als `--stippel-geojson` vóór het zeebeen. Hekinan-kade ligt 23,6 km van zeeknoop 5771
(`34,64220/137,01940`, < 25 km max-snap, dus binnen het automatische snapbereik) → `--been zee` gebruikt de
KADE rechtstreeks als eindpunt (`hecht_marnet.py` snapt intern), en een tweede `maak_havenaanloop.py --van
34.64220,137.01940 --naar 34.8478,136.9535` (zeeknoop→kade, in reisvolgorde) dicht de resterende naad (24,5
km, 9 punten, 0,00 km over land). Hoofdzeebeen **8.101,1 km** — tegen de brief-schatting 7.700–7.900 km
(+2,6 % tot +5,2 %, ruim binnen ±15 %). Totaal b2 = **8.175,4 km**. MARNET kiest zelf de Tasmanzee/westelijke-
Pacific-route (geen Zuid-Chinese-Zee-doorsteek afgedwongen — corridornoot, geen via-punt).

**Toets naden:** alle overgangen ≤0,41 km (spoor→spoor 0,00 km overal · spoor(PWCS-kade)→haven-aanloop
Newcastle 0,41 km · haven-aanloop→hoofdzeebeen 0,00 km · hoofdzeebeen→haven-aanloop Hekinan 0,00 km). Ruim
binnen de 5 km-norm.

**`toets_knikken.py`:** 4 knikken ≥60°, 2 omkeringen ≥150°, waarvan **1 TERUGLOOP** — been 2 (Mount Arthur →
Muswellbrook) bij -32,34920/150,99260 (175,6°, R~91 m, v=3,5). ⚠️ **Getest met `--keerstraf=0`** (turnstraf
volledig uit): identiek resultaat (25,6 km, dezelfde omkering op hetzelfde punt) — de router kiest deze route
dus al als absoluut kortste pad, ongeacht bochtvoorkeur; **topologisch afgedwongen door het 1-op-1-net**, geen
routerkeuze die met een andere straf te vermijden was (zelfde methode/uitkomst als de emplacement-gaten bij
Jinzhou/Chuqui/Matarani — de laadinfrastructuur bij Mount Arthur hangt kennelijk via een lus/doodlopende spur
aan het hoofdnet). Niet gerepareerd door een via-punt bij te schuiven (werkwijze §5: buiten de norm = bevinding,
geen shotgun-fix) — blijft staan als bevinding. Verder: 1 "scherpe bocht, echt" bij -32,73890/151,55450 (176,8°,
R~22 m, v=1,5, kopmaak bij de Maitland-junctie) en 2 krappe bochten (R 3,9/6,4 km) in het MARNET-zeebeen —
normale routekeuzes, geen fout.

**`toets_rechte_benen.py --min-km 5`:** geen been van deze stroom in de uitslag — de mijn-laadspoor-stippel
(4,4 km) blijft onder de 5 km-drempel, en beide haven-aanlopen zijn via het `detour()`-waterpad gerouteerd
(omwegfactor 1,073/1,035), geen ongeteste rechte lijn.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {zee, spoor} (binnen de toegestane
set), elk been ≥2 punten (minimum 2, de stippel), bestandsgrootte **28,3 KB** (ruim onder de 300 KB-richtwaarde).

**Markers:** alle 3 op 0,0 m van hun been (Mount Arthur, PWCS Kooragang Island en Hekinan Thermal Power Station
vallen elk samen met een been-uiteinde).

**Open punten die blijven staan (zie ook §7 van de brief):**
- Mijnkeuze binnen het Hunter Valley-cluster blijft aannemelijk — geen bron legt een specifieke
  Newcastle→Hekinan-lading bij Mount Arthur alleen vast.
- Exacte Newcastle→Hekinan-tonnage niet gebrond op ladingniveau (JERA ~13 %-aggregaat, Port of Newcastle
  >150 Mt/jr totaal) — niet te verifiëren binnen de lichte werkwijze.
- Eén TERUGLOOP op been 2 (Mount Arthur → Muswellbrook) — eigenschap van het lokale 1-op-1-net rond de
  mijn-laadfaciliteiten (bevestigd topologisch afgedwongen, zie hierboven), niet van een gekozen via-coördinaat.
- Gepubliceerde spoorlijnlengte Muswellbrook–Newcastle blijft ongevonden; de bake meet nu het exacte getal
  (152,1 km over de vier segmenten).

**Gereedschapslessen:**
- Een out-and-back-TERUGLOOP vlak bij een geïsoleerd mijnemplacement is met `--keerstraf=0` te onderscheiden
  van een routerkeuze: blijft de omkering bij nul turnstraf identiek staan, dan is hij topologisch afgedwongen
  door het net zelf en niet iets dat via-punten kunnen oplossen (bevestiging van de Jinzhou-baotou-les, nu met
  de tegenovergestelde test — straf omlaag i.p.v. omhoog — voor hetzelfde bewijs).
- `maak_havenaanloop.py` schrijft altijd in `--van`→`--naar`-volgorde. Bij een haven-aanloop die ná het
  hoofdzeebeen komt (Hekinan is hier de aankomstzijde), moet je `--van`/`--naar` dus VOORAF omdraaien
  (zeeknoop→kade) in plaats van de kade-eerst-volgorde die voor de hand ligt vanuit hoe je het pad bedenkt —
  de eerste poging (kade→zeeknoop) gaf een naad van 23,6 km tussen het hoofdzeebeen en de aanloop-stippel;
  regenereren met omgedraaide `--van`/`--naar` loste het op naar 0,00 km (zelfde les als
  `kolen-ermelo-portqasim`, hier vooraf toegepast in plaats van achteraf handmatig de coördinaten omgedraaid).
- Twee haven-aanlopen tegelijk (Newcastle > 25 km, Hekinan < 25 km maar > 5 km) vragen elk een andere
  `--been zee`-parameterkeuze: de zeeknoop-coördinaat wanneer de kade buiten het automatische max-snap-bereik
  ligt, de kade-coördinaat zelf wanneer ze erbinnen ligt (`hecht_marnet.py` snapt dan intern) — beide kanten
  blijven een aparte stippel-geojson nodig zodra de kade > 5 km van haar zeeknoop ligt (LAR-586).
