# Routebrief (licht) · goud — Fruta del Norte → Guayaquil → Harjavalta (Ecuador → Finland)

**stroom-id:** `goud-frutadelnorte-harjavalta` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** goudconcentraat van Fruta del Norte (Lundin Gold, Zamora-Chinchipe) per **truck** in containers via Loja en de Cajas naar de containerkade van Guayaquil, per **zeeschip** door het Panamakanaal en de Atlantische Oceaan (MARNET kiest ten noorden van Schotland, niet door het Kanaal) en de Oostzee naar de kade van Pori (Mäntyluoto), en per **truck** over vt 2 naar de Boliden Harjavalta-smelter. **Aannemelijk: één bron** voor de afnemer (persbericht dec 2019); zie §7.
**Welke as van het verhaal:** *Ecuador-goud naar een Scandinavische kopersmelter.* Volume: 2025 productie 498.315 oz = 15,5 t Au; het concentraataandeel van de verkoop is 72% (Q2 2026) [3], dus ca 10 t Au/j in concentraat (indicatie, peiljaar 2025/26; 79.444 oz concentraat in Q2 2026 = 2,47 t, keer vier = 9,9 t). Dat is de héle concentraatstroom naar "various smelters and traders" [2], niet Harjavalta alleen. Boliden Harjavalta maakt zelf 8 t Au/j [4].

## 1 · Ketenkaart
```
Fruta del Norte-plant `au-fdn-plant` ──(b1 truck · 21 km grindweg → E45 Los Encuentros–Yantzaza–Loja → E35 → Cuenca → E582 Cajas → E25 · ~543 km)──►
Guayaquil containerkade `au-fdn-guayaquil-kade` ──(b2 zee · haven-aanloop, stippel, 91,5 km)──► zeeknoop 5155
──(b3 zee · MARNET · ~12.387 km · Panama, Atlantische Oceaan, Skagerrak, Sont, Oostzee, Botnische Golf)──► zeeknoop 4537
──(b4 zee · haven-aanloop Pori, stippel, 25,7 km, omgekeerde kopie)──► Pori Mäntyluoto-kade `au-pori-kade`
──(b5 truck · vt 2 · ~47,7 km)──► Boliden Harjavalta `au-harjavalta-smelter` ── stoppunt
```

## 2 · Benen
Alle benen **aannemelijk: één bron voor de afnemer (2019)**; dat staat in de beennaam, niet in de lijnstijl.
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `au-fdn-plant` → `au-fdn-guayaquil-kade` | 21 km grindweg, E45 (Los Encuentros–Yantzaza–Loja), E35 naar Cuenca, E582 (Cajas–Molleturo), E25, E40 | FDN–Loja 142 km (121 + 21) [2]; rest niet gepubliceerd; OSRM-indicatie met dezelfde via-punten 532 [10]; gemeten 542,9 (+2% op OSRM) | maak_stroombeen_weg, eigen profiel, extract `ecuador` | nee |
| b2 | B | zee | `au-fdn-guayaquil-kade` → zeeknoop 5155 (-2.3600,-80.0093) | Río Guayas / Golf van Guayaquil | 91,5 over water (kade 14,7 km hemelsbreed van de knoop > 5 km) | maak_havenaanloop onder timeout 300 (eerder 228 s) | **ja: haven-aanloop** |
| b3 | B | zee | zeeknoop 5155 → zeeknoop 4537 (61.4685,21.1715) | Panamakanaal, Atlantische Oceaan, ten noorden van Schotland, Skagerrak, Sont/Belt, Oostzee, Botnische Golf | 12.386,7 gemeten (router, geen gepubliceerd getal; ontwerp 13.000) | MARNET `--been zee` | nee |
| b4 | B | zee | zeeknoop 4537 → `au-pori-kade` | haven-aanloop Pori (kade 22,3 km hemelsbreed van de knoop) | 25,7 | LETTERLIJKE KOPIE omgekeerd van `grafiet-harjavalta-heroya-aanloop-pori.geojson` | ja: haven-aanloop |
| b5 | C | truck | `au-pori-kade` → `au-harjavalta-smelter` | vt 2 (Pori–Nakkila–Harjavalta) | hemelsbreed ca 44, geen wegkm gepubliceerd; getest 47,7 (eindigt 0,01 km van de smelter) | maak_stroombeen_weg, NIEUW profiel, extract `finland` | nee |
Totaal ca 13.093 km. Geen leiding, spoor of vlucht; geen fase D/E; geen last-mile-been. Een vlucht is niet nodig: de enige bron noemt containers per schip.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-fdn-plant` | mijn / laadplek (concentraat) | Fruta del Norte, verwerkingsplant en camp | -3.7625, -78.5040 | [2][11] | **aannemelijk** (z15 gezien: gebouwenclaster met platformen en procesinstallaties op een gerooid terrein in regenwoud, wegen naar het westen; plant en kamp niet te scheiden; sitelaag `w-fruta-del-norte` -3.7667,-78.4333 ligt 7,8 km ONO, daar is bos; niet gebruikt) |
| `au-fdn-guayaquil-kade` | overslag truck → zee | Guayaquil, containerterminal Puerto Marítimo, kade-rand | -2.2835, -79.9040 | [1][5][6][9][11] | **aannemelijk** (haven Guayaquil: bron-gelegd [1][5]; terminal niet genoemd. z15 gezien: containerterminal met STS-kranen, containerstapels en een kade aan de Guayas-geul; punt op de kaderand. Fertisa (`cu-fertisa-kade` -2.2543,-79.9082) is bulk en niet gebruikt) |
| `au-pori-kade` | overslag zee → truck | Port of Pori, Mäntyluoto noordkade — hergebruik `gr-pori-kade` (grafiet-harjavalta-heroya) | 61.5959, 21.4966 | [8][12] | bron-gelegd voor de haven; dat dít concentraat hier lost is niet bewezen (z15 gezien: kade aan open water, loodsen, containeropslag, portaalkraan, spoor) |
| `au-harjavalta-smelter` | losplek / smelter | Boliden Harjavalta, Teollisuuskatu 1 — hergebruik `pgm-harjavalta-smelter` (pgm-kevitsa-harjavalta) | 61.3175, 22.1182 | [4][13] | bron-gelegd (z15 gezien: smelter- en procescomplex met rangeerspoor langs de hallen; Nornickel-raffinaderij in hetzelfde complex) |
Zeeknopen (router, geen anker): 5155 (-2.3600,-80.0093) en 4537 (61.4685,21.1715). Pori-aanloop en vt 2-via-punten zijn bestaand en bron-gelegd in `grafiet-harjavalta-heroya.md`.

## 4 · Via-punten (alleen landbenen met een corridorkeuze; lat, lon)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Los Encuentros, aansluiting grindweg op E45 | -3.7490, -78.6230 | einde van de 21 km grindweg [2]; pint de uitrit naar de E45 |
| b1 | 2 | E45 bij Yantzaza (noordrand, niet het centrum) | -3.8000, -78.7590 | houdt de route op de E45 langs Yantzaza |
| b1 | 3 | E35 noord van Loja | -3.8350, -79.2200 | de corridorkeuze: naar Cuenca (E35) en niet via Loja-zuid/Machala |
| b1 | 4 | E582 west van Cuenca (ringweg, niet het centrum) | -2.8680, -79.0860 | pint de Cajas-corridor E582 |
| b1 | 5 | Molleturo (E582) | -2.7200, -79.4130 | sluit de Machala-variant (E25) uit |
Profielinstellingen uit de toets: refs E45, E35, E582, E25, E40; vensterKm 50; `gepubliceerdKm` None (indicatie). b5: via-punten omgekeerd uit het grafiet-profiel (lat, lon): 61.5494,21.5906 · 61.4792,21.7600 · 61.4068,21.9161 · 61.3446,22.0253; uiteinden = ankers.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Fruta del Norte-plant | Lundin Gold | erts → goudconcentraat (+ doré) | 2025: 498.315 oz Au; 2026-guidance 475–525 koz | [2][3] |
| Harjavalta-smelter | Boliden | concentraten → koper, nikkel, goud, zilver | 2025: 162 kt Cu, 8 t Au, 65 t Ag | [4] |

## 6 · Stoppunt
De brief stopt bij de Harjavalta-smelter: één bron noemt hem als bestemming van de eerste zending, en daarna is de afzet "various smelters and traders" [2]. Wat Boliden met het goud doet (baren, afnemers) is niet gebrond: fase D vervalt; E vervalt.

## 7 · Open punten
- **Eén bron voor de afnemer:** alleen het Lundin-persbericht van 13-12-2019 noemt Harjavalta (8 containers, vertrek uit Guayaquil op 8-12-2019) [1]; kranten noemen "Europa" [5][7]. Het AIF 2025 zegt smelters en handelaren zonder namen en "not dependent on any one smelter" [2]. Of er nog Harjavalta-ladingen gaan is niet bevestigd.
- **Tonnage 2019:** 8 containers, 177,9 t [5] tegen 180 t [1] tegen 8 x 22 = 176 t; Au-inhoud niet genoemd.
- **Terminal in Guayaquil niet genoemd** [5][7]; Contecon is een aanname (containers, grootste containerterminal; OSM-gebouw Contecon 2 km WNW van het anker [9]). AIF noemt ook de haven Bolívar [2].
- **Pori niet bewezen:** geen bron zegt via welke Finse haven de Harjavalta-concentraten aankomen; Boliden noemt "the port on the Baltic Sea" [4]. Pori/Mäntyluoto is de aanname (haven bij Harjavalta, liner naar Hamburg en Gent [8]).
- **Gereden route in Ecuador onbekend:** geen bron noemt de weg na Loja. Cuenca/Cajas volgt de haalbaarheidstoets en `koper-mirador-tongling.md`; OSRM geeft als kortste route 414 km (waarschijnlijk via Machala, niet gecontroleerd). 2020: een blokkade van de toegangsweg hield zendingen tegen tot 2-11-2020 (zoekresultaat, niet gelezen).
- **Zeeroute:** MARNET gaat ten noorden van Schotland (815 km van Dover); de corridor is dus niet "Engelse Kanaal". Beide aanlopen zijn schematisch.
- **Plant-anker aannemelijk:** plant en kamp niet te scheiden op z15; sitelaag (7,8 km ernaast) en Wikipedia (15–20 km) niet gebruikt.
- **Q3 2025-aandeel 64% concentraat** komt uit het ontwerp, niet zelf gelezen; Q2 2026 (72%) wel [3].
- Webbudget: 1 van 3 WebSearch; firecrawl niet gebruikt; WebFetch op 5 pagina's (e-mj gaf 403).

## 8 · Bronnen
[1] Lundin Gold, persbericht 13-12-2019, eerste export van goudconcentraat: Boliden Harjavalta, Guayaquil, 8 containers, 180 t, vertrek 8-12. https://lundingold.com/news/lundin-gold-announces-first-export-of-gold-concent-122610/
[2] Lundin Gold, Annual Information Form 2025: 498.315 oz, smelters en traders, FDN 142 km ONO van Loja (121 km E45 + 21 km grind), havens Guayaquil en Bolívar. https://lundingold.com/site/assets/files/111751/f2025-lug-aif-final.pdf
[3] Lundin Gold, Q2 2026: 118.994 oz geproduceerd, 79.444 oz concentraat verkocht van 110.385 (72%), guidance 475–525 koz. https://lundingold.com/news/lundin-gold-reports-second-quarter-2026-results-122856/
[4] Boliden, Harjavalta-smelter: Teollisuuskatu 1, 2025 productie 162 kt Cu, 8 t Au, 65 t Ag, concentraten ook van Kevitsa. https://www.boliden.com/operations/smelters/boliden-harjavalta
[5] Primicias, dec 2019: eerste concentraat, 8 containers, 177,9 t, 3 trucks per dag van 22 t, naar Europa. https://primicias.ec/noticias/economia/mina-fruta-norte-primer-concentrado-oro
[6] Expreso, nov 2019: containers over land naar de haven van Guayaquil, ca 6 trucks per dag. https://www.expreso.ec/actualidad/mineria-ruta-oro-plata-17772.html
[7] Mundo Maritimo, dec 2019: lading in bewaakt gebied in de haven van Guayaquil, geen terminal genoemd. https://mundomaritimo.cl/noticias/ecuador-mina-fruta-del-norte-exporto-su-primer-cargamento-de-concentrado-de-oro-a-traves-del-puerto-de-guayaquil
[8] Wikipedia, "Port of Pori": drie havens, liner naar Hamburg, Gent, Sint-Petersburg, Teesport. https://en.wikipedia.org/wiki/Port_of_Pori
[9] OSM via Nominatim (ODbL): Contecon Guayaquil S.A., gebouw -2.2807,-79.9080. https://nominatim.openstreetmap.org
[10] OSRM (publieke demo, OSM-data), eigen aanroep 2026-10-30: FDN → Guayaquil met de via-punten 532,1 km; kortste 414,0 km. https://router.project-osrm.org
[11] Esri via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-goud-frutadelnorte-harjavalta-{plant,contecon,pori,smelter}.png`.
[12] `v2/design/routebrieven/grafiet-harjavalta-heroya.md`: anker `gr-pori-kade`, aanloop 25,7 km, vt 2-via-punten.
[13] `v2/design/routebrieven/pgm-kevitsa-harjavalta.md`: anker `pgm-harjavalta-smelter`, bron-gelegd.
[14] Haalbaarheidstoets (orkestrator, M31 golf 16): wegbeen 542,9 km, zeeroute 12.386,7 km, aanloop Guayaquil 91,5 km, Pori-weg 47,7 km.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
Functie `bak_goud_frutadelnorte_harjavalta()` in `v2/tools/bak_stromen.sh`; uitvoer `v2/data/stroomroute-goud-frutadelnorte-harjavalta.json` (versie 2, lonlat, 289,0 KB, 14.346 punten). Totaal 13.094,9 km, 5 benen, 4 markers.
| # | modaliteit | km | punten | stippel | herkomst |
|---|---|---|---|---|---|
| b1 | truck | 543,3 | 12.431 | nee | eigen profiel `goud-frutadelnorte-harjavalta-fdn-guayaquil` (extract ecuador, wegscan_puur): 542,9 weggeometrie + 0,26 km plant en 0,09 km kade (rechte stukken) |
| b2 | zee | 91,5 | 73 | ja, haven-aanloop | maak_havenaanloop onder timeout 300: gelukt in 270 s, cel 0,005 gebufferd, 4,42 km over land aan de uiteinden (kade ligt op de 1:10M-kust) |
| b3 | zee | 12.386,7 | 1.300 | nee | MARNET zeeknoop 5155 → 4537, snap 0,000 km aan beide kanten; gelijk aan de toetswaarde van de brief |
| b4 | zee | 25,7 | 15 | ja, haven-aanloop | letterlijke kopie omgekeerd van `grafiet-harjavalta-heroya-aanloop-pori.geojson` (opgeslagen als `goud-frutadelnorte-harjavalta-aanloop-pori.geojson`) |
| b5 | truck | 47,7 | 527 | nee | nieuw profiel `goud-frutadelnorte-harjavalta-pori-harjavalta` (extract finland): 47,4 km weg + 0,3 km kade-stub; geen gepubliceerde wegkm (hemelsbreed ca 44), dus indicatie |
Markers (4, allemaal 0,0 km van de lijn): Fruta del Norte-plant (-3.7625, -78.5040) · Guayaquil-kade (-2.2835, -79.9040) · Pori Mäntyluoto (61.5959, 21.4966) · Boliden Harjavalta (61.3175, 22.1182). Naden tussen alle opeenvolgende benen 0,000 km (de aanlopen sluiten exact op kade en zeeknoop).
**Toets.** b1: 542,9 tegen de toets van de brief 542,9 (OSRM 532 = +2%, FDN-Loja 142 km niet apart gemeten); geen gepubliceerde wegkm voor het geheel, dus geen ±15%-norm maar indicatie. b5: 47,7 tegen 47,7 getest, +8% op hemelsbreed 44. Alle via-punten snappen binnen 0,4 km (Molleturo 0,39 km, plant 0,26 km, Pori-kade 0,30 km); geen via-punt verwijderd of verschoven. `toets_knikken.py`: 40 knikken, 0 omkeringen, 0 terugloop (de spikes zitten in het smeltercomplex en de haven, de krappe bochten in de Andes). `toets_rechte_benen.py --min-km 5`: geen van onze benen gemeld. Bestand onder 300 KB.
**Stippels.** b2 en b4 zijn haven-aanlopen (kade 14,5 resp. 22,3 km van de zeeknoop), geen gat in een net dat er hoort te zijn. Er is geen leiding-, spoor- of vluchtbeen en geen last-mile-stippel: het plantanker ligt op 0,26 km van de weg.
**Lessen.** (1) `maak_havenaanloop.py` leest een negatieve coördinaat alleen als `--van=-2.2835,-79.9040` (met het gelijkteken); `--van -2.2835,...` geeft "expected one argument". (2) De Guayaquil-aanloop duurde 270 s van de 300 s time-out: bij een trage machine rechte stippel als terugval klaarhouden. (3) De grindweg van 21 km (plant tot Los Encuentros) zit gewoon in de scan: 17,06 km first mile over kleine klassen, geen `track` of `eindKlassen` nodig.
**Afwijkingen van het ontwerp.** Geen: het eindpunt is Boliden Harjavalta zoals het id belooft. Open punten §7 blijven staan (afnemer één bron, terminal, Pori, gereden route, plant-anker aannemelijk).
