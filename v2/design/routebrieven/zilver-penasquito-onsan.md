# Routebrief (licht) · zilver — Peñasquito → Manzanillo → Onsan (Zuid-Korea)

**stroom-id:** `zilver-penasquito-onsan` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** zink-loodconcentraat met meegesleept zilver van de Peñasquito-mijn (Newmont, Zacatecas) per **truck**
(~800 km, geen gepubliceerd exact tracé) naar de multi-purpose/mineraalterminal in de binnenhaven van Manzanillo, per
**zeeschip** de Grote Oceaan over (~11.900 km grootcirkel) naar de Onsan-kade bij Ulsan, en over eigen terrein naar de
Korea Zinc Onsan-smelter — **stoppunt** (de smelter ís de bestemming van het ontwerp; geen fase D/E).
**Welke as van het verhaal:** *transpacifische zink-loodconcentraat-route* — Peñasquito's Zn/Pb-concentraat draagt zilver
mee als bijproduct (mijn ~650 t Ag/jaar, 2,5% van de wereldmijnproductie, Silver Institute/USGS 2024 [1]); Onsan is
"'s werelds grootste base-metaal-smeltcomplex" en wint zilver terug uit wereldwijd concentraat [2].

## 1 · Ketenkaart
```
Peñasquito-mijn `ag-penasquito-mijn` ──(b1 truck · Fresnillo–Zacatecas–Guadalajara–Colima · ~800 km [3], geometrie-corridor
   aannemelijk: geen gepubliceerd tracé)──► Manzanillo-terminal `ag-manzanillo-timsa` (binnenhaven, TIMSA/OCUPA-zone)
   ──(b2 zee · haven-aanloop Manzanillo, stippel · ~154 km)──► zeeknoop 4859
   ──(b3 zee · MARNET, transpacifisch · grootcirkel-orde ~11.900 km)──► zeeknoop bij Onsan
   ──(b4 zee · haven-aanloop Onsan, stippel · ~6 km)──► Onsan-kade `ag-onsan-kade`
   ──(b5 truck · eigen terrein, stippel · ~0,9 km)──► Korea Zinc Onsan-smelter `ag-onsan-smelter` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Peñasquito-mijn → Manzanillo-terminal | Fresnillo → Zacatecas → Guadalajara → Colima (Fed 54D/200D, aannemelijk — geen gepubliceerd exact tracé [3]) | 800 [3, webcheck] (via-punten hemelsbreed 729) | maak_stroombeen_weg (extract `mexico`, groot venster i.v.m. de afstand) | nee — corridor zelf aannemelijk (één bron voor de afstand), lijn wordt gemeten en doorgetrokken |
| b2 | B | zee (haven-aanloop) | Manzanillo-terminal → zeeknoop 4859 (17.98400,-103.40330) | schematisch, over water — MARNET reikt niet tot de kade | 154,2 [gemeten, hecht_marnet] | maak_havenaanloop.py, terugval rechte stippel | ja — net reikt niet (kade > 5 km van de zeeknoop, ook al snapt de router binnen 25 km) |
| b3 | B | zee | zeeknoop 4859 → zeeknoop bij Onsan (35.46180,129.39080) | Grote Oceaan-oversteek | grootcirkel-orde 11.878 [gemeten]; MARNET meet de vaarafstand | MARNET | nee |
| b4 | B | zee (haven-aanloop) | zeeknoop bij Onsan → Onsan-kade | schematisch, over water — kade ligt 5,6 km van de zeeknoop | 5,6 [gemeten, hecht_marnet] | maak_havenaanloop.py, terugval rechte stippel | ja — net reikt niet binnen de 5 km-regel (LAR-586) |
| b5 | C | truck | Onsan-kade → Korea Zinc Onsan-smelter | eigen terrein, Onsan-industriezone | 0,9 [gemeten, hemelsbreed] | stippel (site < 2 km, geen apart net bevestigd) | ja — eigen terrein / geen net op deze korrel |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-penasquito-mijn` | mijn / mill | Peñasquito-mijn (Newmont), Mazapil, Zacatecas | 24.6377, -101.6982 | [4][10] | bron-gelegd (z14 gezien: gebouwencluster/mill direct N van de open pit, grote tailingsvijver ZW ervan; OSM-landuse "Mina Peñasquito" 24.6090–24.6660 / -101.7583…-101.6353) |
| `ag-manzanillo-timsa` | overslag (binnenhaven, multi-purpose/mineraalterminal) | Manzanillo binnenhaven-terminalcomplex (TIMSA/OCUPA-zone), Colima | 19.0810, -104.2975 | [5][6][10] | bron-gelegd (z16 gezien: aaneengesloten stacking yards + portaalkranen op de schiereiland-kade in de binnenlagune San Pedrito; generieke havencentroïde 19.0500,-104.3200 ligt 2,9 km verderop op het strand, niet op een kade) |
| `ag-onsan-kade` | losplek (haven, bij de smelter) | Onsan-havenkade nabij Korea Zinc-smelter, Ulsan | 35.4180, 129.3600 | [2][7][10] | bron-gelegd (z16 gezien: stacking yard direct aan een kademuur, bulkcarriers/lichters voor anker op de rede; ligt 0,9 km ZO van het smelterregister-punt) |
| `ag-onsan-smelter` | smelter (stoppunt) | Korea Zinc Onsan-smelter (power station-blok) | 35.4234, 129.3525 | [8][10] | bron-gelegd (z14 gezien: groot geïntegreerd industriecomplex met tankparken en procesgebouwen; OSM-landuse "Korea Zinc Onsan Smelter power station" 35.4229–35.4238 / 129.3516…129.3534) |

## 4 · Via-punten (alleen b1 — de truckweg heeft een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Fresnillo | 23.1750, -102.8675 | eerste grote knooppunt zuidwaarts vanaf de mijn; corridorkeuze tussen een directe staatsweg en de doorgaande route via Fresnillo [9] |
| b1 | 2 | Zacatecas (stad) | 22.7736, -102.5736 | aansluiting op de doorgaande noord-zuidcorridor (Fed 54D) richting Guadalajara [9] |
| b1 | 3 | Guadalajara | 20.6767, -103.3475 | grote draaischijf waar de corridor van zuid naar westzuidwest naar de Pacific-kust ombuigt (Fed 54D/200D "Siglo XXI") [9] |
| b1 | 4 | Colima (stad) | 19.2433, -103.7247 | laatste knooppunt vóór de kustafdaling naar Manzanillo [9] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Korea Zinc Onsan-smelter | Korea Zinc | Zn/Pb-concentraat (wereldwijd, incl. Mexico) → refined lead/zinc + zilver teruggewonnen | grootste base-metaal-smeltcomplex ter wereld (500.000 t/j refined lead) | [2][8] |

## 6 · Stoppunt
De brief stopt bij de Korea Zinc Onsan-smelter: het ketenontwerp noemt geen vervolgstap (geen fase D/E), de smelter
ís de eindbestemming van deze as, en zilver wordt daar als bijproduct uit het Zn/Pb-concentraat teruggewonnen.

## 7 · Open punten
- **Bestemming Korea Zinc blijft "aannemelijk: één bron"** — de directe koppeling Manzanillo→Korea Zinc steunt op een
  verouderde Goldcorp 6-K (2009/2010, vóór Newmont's overname in 2019) [11]. Onafhankelijke, recentere onderbouwing
  toegevoegd: CRU (2019) noemt concentraatverstoringen bij "Newmont Goldcorp's Peñasquito mine in Mexico, an important
  supplier" als oorzaak van een terugval in Zuid-Koreaanse concentraat-import, en Onsan's hogere primaire productie
  hangt samen met "increased availability of concentrates" [2] — bevestigt de route-as, niet de zending zelf.
  Newmont's huidige 10-K bevestigt niets op zendingsniveau. Risico-label blijft **aannemelijk**, niet onzeker.
- **Truckcorridor niet gepubliceerd** — Wood Mackenzie/Newmont noemen alleen de afstand (~800 km) [3], geen tracé. De
  via-punten (Fresnillo–Zacatecas–Guadalajara–Colima, Fed 54D/200D) zijn een aannemelijke hoofdroute; de bak-agent moet
  het exacte tracé met `maak_stroombeen_weg.py` over het `mexico`-extract vinden (grote vensterKm i.v.m. de afstand).
- **Exacte concentraatkade binnen Manzanillo niet gepind** — de binnenhaven-lagune bevat meerdere multi-purpose-
  terminals naast elkaar (TIMSA "Instalación de Usos Múltiples No. 2", OCUPA "No. 1", plus de containerterminal SSA);
  `ag-manzanillo-timsa` ligt op het schiereiland-complex maar niet op een specifiek bevestigd TIMSA-bulkbekken. TIMSA
  behandelt aantoonbaar koper-, zink-, lood- en ijzerconcentraat [5].
- **Zeeknoop-afstand Manzanillo blijft groot ook met de precieze kade** — generiek 152,9 km, precieze terminal 154,2 km:
  het verschil zit 'm niet in de kadekeuze maar in hoe ver MARNET's 1:10M-zeeknoop uit de kust ligt hier. Haven-aanloop
  is dus sowieso nodig, ongeacht welke Manzanillo-kade precies wordt gekozen.
- **Onsan-kade is een plausibele nabijgelegen kade, geen bevestigd Korea Zinc-eigen dok** — mining-journal noemt een
  "dedicated wharf" die grondstof uit Zuid-Amerika (incl. Bolivia) ontvangt [7], maar de exacte coördinaat van dát dok
  is niet gevonden; `ag-onsan-kade` is satelliet-gelegd op een plausibele stacking yard/kade 0,9 km van het
  smelterregister-punt, binnen dezelfde Onsan-industriehaven.
- **Jaarvolume via déze specifieke route niet gepubliceerd** — Peñasquito's totale zilverproductie is ~650 t Ag/jaar
  (2,5% van de wereldmijnproductie, Silver Institute/USGS 2024 [1]), volledig als bijproduct van het Zn/Pb-Au-doré-
  pakket; welk deel daarvan specifiek via Manzanillo naar Onsan gaat is nergens gekwantificeerd (Newmont noemt alleen
  generiek "smelters in Mexico, Noord-Amerika, Azië en Europa").

## 8 · Bronnen
[1] The Silver Institute / Metals Focus, World Silver Survey; USGS Mineral Commodity Summaries 2025 — Peñasquito
    ~650 t Ag/jaar, 2,5% van de wereldmijnproductie (v1-register `data/silver.js`).
[2] CRU Group, "South Korea a key player in international lead and battery markets" (2019) — concentraatverstoringen
    bij Peñasquito raakten Zuid-Koreaanse import; Onsan = grootste refined-lead-producent (500.000 t/j).
    https://www.crugroup.com/en/communities/thought-leadership/2019/south-korea-a-key-player-in-international-lead-and-battery-markets/
[3] Wood Mackenzie, "Peñasquito zinc mine" report (afstand Peñasquito→Manzanillo ~800 km, webcheck).
    https://www.woodmac.com/reports/metals-penasquito-zinc-mine-16251765/
[4] Newmont Corporation, Form 10-K FY2024/2025 (ARS) — Peñasquito-mijnbeschrijving, Zacatecas.
    https://www.sec.gov/Archives/edgar/data/1164727/000110465925023965/tm252653d2_ars.pdf
[5] PortalPortuario, "México: Hutchison Ports TIMSA invierte más de USD 2.6 millones para el manejo de minerales" —
    TIMSA behandelt koper-, zink-, lood- en ijzerconcentraat + pellets, tot 3 bulkschepen tegelijk.
    https://portalportuario.cl/mexico-hutchison-ports-timsa-invierte-mas-de-usd-2-6-millones-para-el-manejo-de-minerales/
[6] ASIPONA Manzanillo, "Terminales e Instalaciones" — terreinlijst incl. OCUPA (Instalación No. 1) en TIMSA
    (Instalación No. 2), elk ~85.000 m².
    https://www.puertomanzanillo.com.mx/esps/0020303/terminales-e-instalaciones.html
[7] Mining Journal, "Korea Zinc not able to export Onsan sulphuric acid" — dedicated pier ontvangt grondstof uit
    Zuid-Amerika incl. Bolivia (ore/rock unloading). https://www.mining-journal.com/base-metals/news-analysis/4395429/korea-zinc-able-export-onsan-sulphuric-acid
[8] Wikipedia / OpenStreetMap — Korea Zinc Company (Onsan-smelter, Ulsan); OSM-landuse "Korea Zinc Onsan Smelter
    power station" 35.4229–35.4238/129.3516–129.3534. https://en.wikipedia.org/wiki/Korea_Zinc
[9] Wikipedia (Engelstalig), coördinaten Fresnillo / Zacatecas City / Guadalajara / Colima City — steden op de
    aannemelijke truckcorridor (Fed 54D/200D); geen bevestigde brontekst voor het exacte wegtracé.
[10] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16, live) — `v2/build-cache/satcheck/sat-zilver-penasquito-
    onsan-mijn.png`, `sat-zilver-penasquito-onsan-manzanillo-timsa.png`, `sat-zilver-penasquito-onsan-koreazinc-
    smelter-zuid.png`, `sat-zilver-penasquito-onsan-korea-zinc-overzicht.png`.
[11] Goldcorp Inc., Form 6-K (2009/2010) — vroege zinkconcentraatzendingen via Manzanillo naar Korea Zinc (vóór
    Newmont's 2019-overname; verouderde bron, aangevuld door bron [2]).
    https://www.sec.gov/Archives/edgar/data/0000919239/000119907309000877/ex99_1.htm

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `zilver-penasquito-onsan`** → `v2/data/stroomroute-zilver-penasquito-onsan.json` — 5 benen,
**13.104,4 km**, 8.764 punten, 4 markers. truck 943,8 + 0,9 = 944,7 km · zee 154,2 (stippel) + 11.999,9 +
5,6 (stippel) = 12.159,7 km. Recept: `bak_stromen.sh` (functie `bak_zilver_penasquito_onsan`); wegprofiel
`zilver-penasquito-onsan-mijn-manzanillo` in `maak_stroombeen_weg.py`.

**b1 (truck, geofabrik mexico-extract, doorgetrokken):** `maak_stroombeen_weg.py --profiel
zilver-penasquito-onsan-mijn-manzanillo` — via Fresnillo → Zacatecas → Guadalajara → Colima, alle vier de
via-snaps ≤0,43 km. **943,6/943,8 km tegen 800 km (Wood Mackenzie webcheck, geen exact tracé) = +18,0%,
buiten de ±15%-norm.** ⚠️ **Bevinding, niet dichtgetrokken:** de via-punten liggen op de brief-corridor
(hemelsbreed-som 729 km) en snappen goed; het verschil zit in de werkelijke wegomweg (23 keerlus-snoeisels,
958,0 → 943,6 km) tegen een afstand die Wood Mackenzie alleen als webcheck-cijfer noemt, geen gepubliceerd
tracé. Geen via-punt bijgeschoven om het getal te halen (werkwijze §5).

**b2 (zee, stippel, haven-aanloop Manzanillo):** `maak_havenaanloop.py --van 19.0810,-104.2975 --naar
17.98400,-103.40330` liep vast op `timeout 300` (exit 124) — geen tweede poging. Rechte stippel, **154,2 km**
tegen de rechte-lijn-afstand van de brief (154,2 km, brief §2): de Manzanillo-terminal ligt ver van de
MARNET-zeeknoop af (het verschil zit niet in de kadekeuze maar in hoe ver deze zeeknoop uit de kust ligt,
brief §7).

**b3 (zee, MARNET, beide uiteinden al zeeknopen):** `--been "zee|...|17.98400,-103.40330|35.46180,129.39080"`
— snap 0,000 km aan beide kanten (dit been snapt direct op de al gemeten zeeknopen). **11.999,9 km over 53
MARNET-edges** (1.230 punten) tegen de grootcirkel-orde van ~11.878 km uit de brief = **+1,0%**, ruim binnen
±15% (verwacht: MARNET's transpacifische vaarroute ligt langer dan de grootcirkel). Lengte-invariant:
getekende lijn 11.999,950 km vs som edge-km 12.000,100 km = −0,150 km (de naden).

**b4 (zee, stippel, haven-aanloop Onsan):** `maak_havenaanloop.py --van 35.46180,129.39080 --naar
35.4180,129.3600` liep eveneens vast op `timeout 300` (exit 124) — geen tweede poging. Rechte stippel,
**5,6 km**, exact zoals de brief opgeeft (LAR-586: ook binnen de 25 km-snap een aanloop nodig zodra de kade
> 5 km van de zeeknoop ligt).

**b5 (truck, stippel, eigen terrein):** rechte stippel Onsan-kade → Korea Zinc Onsan-smelter, **0,9 km**,
binnen de 2 km-last-mile-drempel van de lichte werkwijze — geen apart wegprofiel nodig, zoals de brief
voorschrijft.

**Toets naden:** alle vier de overgangen (b1→b2, b2→b3, b3→b4, b4→b5) **0,00 km** — met name de twee
haven-aanloop-snaps en de mijn→terminal-snap sluiten naadloos aan, omdat elk been eindigt/begint op exact
hetzelfde punt als het volgende (de weg-anker, de zeeknoop, de kade-anker).

**`toets_knikken.py`:** truck-been 30 knikken ≥60°, waarvan 1 omkering (160,3° bij 22,77463,-102,62395,
straal ~11 m, gemarkeerd "scherpe bocht, echt") en 0 terugloop; de overige 29 zijn kleine-straal-spikes
(R 2–53 m) op kruisingen/rangeerknopen langs de Fed 54D/200D-corridor, geen fout. Zeebeen 0 knikken/0
omkeringen (MARNET-router, geen bochten mogelijk op deze schaal).

**`toets_rechte_benen.py --min-km 5`:** beide haven-aanloop-stippels (b2 154,2 km/omwegfactor 1,000, b4
5,6 km/omwegfactor 0,998) worden gemeld — verwacht, want dat zijn al gestippelde rechte lijnen met een
reden; geen actie nodig. b5 (0,9 km) valt onder de `--min-km 5`-drempel.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, zee} (binnen de toegestane
set), elk been ≥2 punten (minimum 2), bestandsgrootte **185,0 KB** (< 300 KB-richtwaarde).

**Markers:** alle vier ankers (Peñasquito-mijn, Manzanillo-terminal, Onsan-kade, Korea Zinc Onsan-smelter)
op **0,0 m** van de lijn — elk anker is rechtstreeks als been-uiteinde gebruikt, geen los routeerpunt.

**Gereedschapslessen:** geen nieuwe — dit volgt exact het patroon van `bak_kobalt_moa_fortsaskatchewan`
(zee-stippel bij timeout, geen tweede poging) en `bak_olie_habshan_chiba`/`bak_olie_rastanura_zhoushan`
(LAR-586-haven-aanloop binnen de 25 km-snap). Enige afwijking van de norm is b1's +18,0% wegomweg, en dat
is inherent aan het ontbreken van een gepubliceerd tracé, niet aan het gereedschap.
