# Routebrief (licht) · gas — Karratha/Pluto (Australië) → Rudong (China)

**stroom-id:** `gas-karratha-rudong` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** aardgas van het offshore Pluto-veld (Carnarvon Basin) gaat per **subzee-leiding** (180 km, 36″) naar Pluto LNG op de Burrup Peninsula bij Karratha, wordt daar tot LNG verwerkt en per **LNG-carrier** via de Straat Lombok/Makassar en de Zuid-Chinese Zee naar de PetroChina Jiangsu LNG-terminal op Yangguang (Sunshine) Island bij Rudong, Jiangsu verscheept — de gevestigde Australië→Oost-China-as, een andere corridor dan Qatar→VS.
**Welke as van het verhaal:** Australië (NW Shelf/Carnarvon) als tweede, gevestigde LNG-bron voor China naast Qatar en de VS; Pluto Trein 2 (Scarborough-backfill) is nog aan het opstarten — het volhoudvermogen van deze as op de langere termijn hangt aan een gasveld dat nog niet volledig produceert [1].

## 1 · Ketenkaart
```
Pluto-gasveld (offshore, Carnarvon Basin, ~174-190 km NW Karratha, 85 m water) — niet getekend, geen brongegeven platformcoördinaat
   ──(b1 leiding · 36″ subzee-trunkline · 180 km gepubliceerd · NIET GEBAKKEN — open punt)──►
Pluto LNG-plant `gas-kr-pluto` (Burrup Peninsula, Karratha, West-Australië)
   ──(b2 zee · Indische Oceaan → Straat Lombok/Makassar → Celebeszee → Zuid-Chinese Zee → Straat Taiwan →
       Oost-Chinese Zee · ~6.000–6.500 km ontwerp (grote cirkel 5.927 km) · MARNET, haven-aanloop beide kanten)──►
Rudong LNG-terminal `gas-rd-eiland` (PetroChina Jiangsu LNG, Yangguang/Sunshine Island, Nantong, Jiangsu) ⏹ stoppunt
   └── (b3 leiding · eiland→vasteland-causeway → Jiangsu-gasnet — NIET GEBAKKEN, mainland-eindpunt niet gebrond)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Pluto-gasveld → `gas-kr-pluto` | 36″ subzee-trunkline Pluto A-platform → Burrup LNG Park | 180 [1][2] | **open punt** — platformcoördinaat niet gebrond (bronnen geven alleen richting+afstand: "174–190 km NW van Karratha, 85 m water") | n.v.t., niet getekend |
| b2 | B | zee (LNG-carrier) | `gas-kr-pluto` → `gas-rd-eiland` | Indische Oceaan → Lombok/Makassar → Celebeszee → ZCZ → Taiwanstraat → OCZ | ~6.000–6.500 (ontwerp); grote cirkel 5.927 [ontwerp/eigen berekening] | MARNET (kade → kade) | nee — maar wél haven-aanloop aan beide zijden (zie §3/bak-aanwijzingen) |
| b3 | C | leiding | `gas-rd-eiland` → invoedingspunt Jiangsu-gasnet | eiland→vasteland-causeway (waargenomen op satelliet, lengte >10 km) | onbekend (ontwerp veronderstelde "<5 km", niet bevestigd) | **open punt** — vastelandeindpunt niet gebrond | n.v.t., niet getekend |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-kr-pluto` | overslag leiding → zee / LNG-plant | Pluto LNG (Woodside), Burrup Peninsula, Karratha | -20.5905, 116.7755 | [1][2][8][9] | bron-gelegd (z15/z16 gezien: tankfarm met cilindrische en bolvormige tanks, procestrains en twee steigers/jetty's die de baai in lopen — Pluto-complex naast andere LNG-installaties op hetzelfde schiereiland; zeeknoop 3878 op 5,97 km, dus binnen de nieuwe haven-aanloop-drempel van >5 km) |
| `gas-rd-eiland` | overslag zee → leiding / regas-terminal | PetroChina Jiangsu LNG-terminal, Yangguang (Sunshine) Island, Rudong/Nantong | 32.528814, 121.428128 | [3][4][5][8][9] | bron-gelegd (z14/z16 gezien: vier grote bolvormige LNG-tanks + procesinstallatie op een kunstmatig opgespoten eiland, met lange trestle-jetty's de rivierdelta in — eiland deelt de kunstmatige landmassa met drie andere LNG-terminals van Guoxin/GCL-Poly/China Resources [6][7]; zeeknoop 9669 op 33,02 km — fors verder dan de 5,0 km van het oude Wikipedia-infoboxpunt van Karratha, en ver boven de 25 km-norm) |

## 4 · Via-punten
Geen — b2 is een zeebeen zonder corridorkeuze (MARNET routeert kade→kade); b1 en b3 zijn niet getekend (open punten).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Pluto LNG (Trein 1 + Trein 2) | Woodside Energy | offshore gas → LNG | Trein 1: 5,9 Mtpa (operationeel, sinds 2012) ≈ 8,0 bcm/j; Trein 2: ~5 Mtpa (opstartend, Scarborough-backfill, eerste LNG verwacht 2026) ≈ 6,8 bcm/j; totaal ≈ 10,9 Mtpa ≈ **14,8 bcm/j** bij volledige opstart | [1] |
| PetroChina Jiangsu LNG-terminal | PetroChina Jiangsu LNG Co (Kunlun Energy 55% / Pacific Energy 35% / Jiangsu Guoxin 10%) | LNG → hervergast gas | 10,0 Mtpa naamplaat over 3 fasen (3,5+3,0+3,5) ≈ **13,6 bcm/j**; sinds mei 2011 > 69 Mt LNG ontvangen, ≈ 100 bcm geëxporteerd naar het net | [3][5] |

## 6 · Stoppunt
De brief stopt bij de PetroChina Jiangsu LNG-terminal op Yangguang Island: geen bron koppelt de hervergaste stroom aan één specifiek invoedingspunt of vervolgtraject in het Jiangsu-gasnet, en de eiland→vasteland-causeway die op satelliet zichtbaar is, is aanmerkelijk langer dan de "korte terreinleiding <5 km" die het ontwerp veronderstelde — fase C wordt daarom niet getekend. Fase D/E vervallen (geen bron noemt een specifieke afnemersfabriek).

## 7 · Open punten
- **Fase A (leiding, Pluto-gasveld → Pluto LNG) niet getekend.** Geen bron geeft een coördinaat voor het Pluto A-platform of het gasveld zelf — alleen richting+afstand ("174–190 km NW van Karratha, 85 m water" [1][2]). Geen coördinaat verzonnen; de 180 km/36″-pijpleiding staat wel in de tekst en de knoop-tabel, maar krijgt geen geometrie.
- **Fase C (leiding, Rudong-eiland → Jiangsu-gasnet) niet getekend, en het ontwerp's aanname is gecorrigeerd.** Satellietbeeld toont een lange trestle-causeway van het kunstmatige eiland naar het vasteland (waargenomen lengte >10 km over sterk verslibd getijdengebied), niet de "<5 km" uit het ketenontwerp — consistent met de haalbaarheidstoets' opmerking over de lange pier/vaargeul bij Rudong. Het exacte invoedingspunt in het Jiangsu-gasnet is niet gebrond.
- **"CNOOC/PetroChina" uit het ontwerp is niet één rechtspersoon.** Het satellietgelegde anker is specifiek de **PetroChina** Jiangsu LNG-terminal (Kunlun Energy/Guoxin); Yangguang Island draagt daarnaast aparte terminals van Guoxin, GCL-Poly (Huidong) en China Resources [6][7] — een eventuele CNOOC-koppeling is in deze pas niet onafhankelijk bevestigd.
- **Karratha/Pluto-zeeknoopafstand herbepaald:** het satelliet-gelegde site-anker (-20.5905, 116.7755) ligt op 5,97 km van zeeknoop 3878 — dichter bij de grens dan de 5,0 km van het oude Wikipedia-infoboxpunt, maar nog steeds boven de nieuwe >5 km-drempel voor een haven-aanloop.
- **Jaarvolume Karratha→Rudong-specifiek niet gebrond** — de cijfers in §5 zijn de totale Pluto-productie resp. de totale PetroChina-Rudong-doorvoer, geen cargo-niveau koppeling tussen de twee.
- **Trein-1-capaciteit wisselt per bron** (Wikipedia: 5,9 Mtpa [1]; het ketenontwerp noemde 4,9 Mtpa) — hier de Wikipedia-waarde aangehouden en de afwijking hier genoteerd i.p.v. stilzwijgend gecorrigeerd.

## 8 · Bronnen
[1] Wikipedia, "Pluto LNG" — Burrup Peninsula, Woodside; Trein 1 5,9 Mtpa (sinds 2012), Trein 2 ~5 Mtpa (Scarborough-backfill, eerste LNG verwacht 2026); Pluto A-platform 174 km NW Karratha, 85 m water; infoboxcoördinaat -20.61008,116.77545. https://en.wikipedia.org/wiki/Pluto_LNG
[2] Offshore Technology, "Pluto Liquefied Natural Gas (LNG) Project, Northern Carnarvon Basin" — 180 km/36″ subzee-pijpleiding Pluto A-platform → Burrup LNG Park, 190 km NW Karratha, 85 m water. https://www.offshore-technology.com/projects/pluto/
[3] Global Energy Monitor (GEM.wiki), "Rudong LNG Terminal (PetroChina)" — coördinaat 32.528814,121.428128, Sunshine Island, Nantong, Jiangsu; eigenaar PetroChina Jiangsu LNG Co (Kunlun Energy 55% / Pacific Energy 35% / Jiangsu Guoxin 10%); 10,0 Mtpa over 3 fasen. https://www.gem.wiki/Rudong_LNG_Terminal_(PetroChina)
[4] China Daily (regionaal Nantong), 20-12-2023 — "PetroChina Jiangsu LNG Terminal achieves high efficiency amidst winter chill", Yangkou Port. https://regional.chinadaily.com.cn/nantong/yangkouport/2023-12/20/c_949174.htm
[5] Nantong Municipal Government, 07-01-2026 — "PetroChina Jiangsu LNG Terminal in Rudong achieves new high in handling capacity": >69 Mt LNG ontvangen uit 27 landen sinds mei 2011, ≈100 bcm geëxporteerd. http://en.nantong.gov.cn/2026-01/07/c_1153805.htm
[6] Nantong Municipal Government, "Jiangsu Rudong Yangkou Port Economic Development Zone" — vier LNG-terminals (PetroChina/Guoxin/GCL Huidong/China Resources) op Yangguang (Sunshine) Island. http://en.nantong.gov.cn/yangkouport/
[7] Global Energy Monitor (GEM.wiki), "Rudong LNG Terminal" (GCL-Poly) — apart terminalproject op hetzelfde eilandcluster, niet als anker gebruikt. https://www.gem.wiki/Rudong_LNG_Terminal
[8] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16, live, 2026-09-28) — `sat-gas-karratha-rudong-pluto-wiki.png`, `sat-gas-karratha-rudong-pluto-plant.png`, `sat-gas-karratha-rudong-rudong-island.png`, `sat-gas-karratha-rudong-rudong-plant.png`, `sat-gas-karratha-rudong-rudong-mainland.png`.
[9] `v2/build-cache/marnet-preais` (MARNET-zeeknopen) — eigen meting via `hecht_marnet.marnet_zee()`: zeeknoop 3878 (-20.62240,116.72940) op 5,97 km van `gas-kr-pluto`; zeeknoop 9669 (32.63010,121.09680) op 33,02 km van `gas-rd-eiland`.
[10] Ketenontwerp + haalbaarheidstoets M31 golf 2 (workflow-invoer, orkestrator) — jaarvolume-indicatie Woodside, Scarborough-backfillrisico, webcheck Wikipedia "Pluto LNG" (locatie/offshore-afstand/capaciteit).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `gas-karratha-rudong`** → `v2/data/stroomroute-gas-karratha-rudong.json` — 3 benen, **6.272,1 km**, 680 punten, 2 markers (2 stippel: beide haven-aanlopen). Recept: `bak_stromen.sh` (functie `bak_gas_karratha_rudong`).

**b1 (leiding, Pluto-gasveld → Pluto LNG) en b3 (leiding, Rudong-eiland → Jiangsu-gasnet): NIET GETEKEND**, exact zoals de brief voorschreef — geen brongegeven platformcoördinaat resp. geen gebrond vastelandeindpunt (§2/§7). De bake bevat dus alleen b2 (zee) plus twee haven-aanlopen.

**Been 1 (zee, stippel, haven-aanloop Karratha/Pluto LNG):** `-20.5905,116.7755 → -20.62240,116.72940`, **5,97 km** rechte stippel. `maak_havenaanloop.py` liep vast op `timeout 300` (exit 124, twee keer getest — eenmaal in de aanloopronde, geen tweede poging na de eerste time-out); ondanks de verwachting in de bak-aanwijzing ("relatief kleine aanloop, timeout 300 zou vlot moeten lukken") bleek dit stuk kust dus toch te duur voor het A*-tool binnen de tijdslimiet. Rechte stippel met reden, conform het protocol.

**Been 2 (zee, MARNET-route, kade → kade — enige gemeten been):** `--been "zee|LNG-carrier Pluto LNG (Karratha) → Rudong LNG-terminal (Yangguang eiland)|-20.62240,116.72940|32.63010,121.09680"` (tussen de twee zeeknopen, niet de kades zelf — zie de haven-aanlopen). **6.229,9 km**, 644 punten. Tegen de ontwerpschatting ~6.000–6.500 km: **binnen bereik**. Tegen de grote cirkel kop→staart (zelf herberekend: **5.927,3 km**, identiek aan de brief's eigen berekening): **+5,1%** — een realistische omweg via Lombok/Makassar/Zuid-Chinese Zee/Straat Taiwan (geen gepubliceerde ladingroute-lengte om exact tegen te toetsen, dus de ±15%-norm is hier zacht, zoals de brief al aangaf). km-uitsplitsing volgens het bake-log: 0 track-edges, 40 MARNET-edges, 0 connectors; lengte-invariant (getekende lijn vs som edge-km) **−0,245 km**, verwaarloosbaar.

**Been 3 (zee, stippel-geojson, haven-aanloop Rudong):** `32.63010,121.09680 → 32.52881,121.42813`, **36,2 km** over water, 34 punten, 0,00 km over land, omwegfactor 1,096. Gelukt ondanks het sterk verslibde Jiangsu-getijdengebied (dezelfde klasse als de M31-golf-1-aanlopen bij Fujairah/Ras Tanura/Aktau, maar hier — in tegenstelling tot de verwachting "FORSE aanloop" in de bak-aanwijzing — wél een pad gevonden op de 1:10M-kustlijn, in de eerste poging).

**Markers:** `gas-kr-pluto` (**0,0 km** van de lijn, kop van de keten) · `gas-rd-eiland` (**0,0 km** van de lijn, staart/stoppunt) — alleen deze twee, geen aftakkingen, zoals de bak-aanwijzing voorschreef.

**Naad:** alle drie de naden tussen opeenvolgende benen zijn **0,00 km** (been 1→2 en been 2→3 sluiten exact aan op de gedeelde zeeknoop-coördinaten). ⚠️ **Gereedschapsles onderweg:** de eerste versie van been 3 (`maak_havenaanloop.py --van <kade> --naar <zeeknoop>`) gaf een geojson met puntvolgorde kade→zeeknoop; `hecht_marnet.py`'s `--stippel-geojson` leest een vooraf gebakken lijn **letterlijk in bestandsvolgorde** (geen automatische heroriëntatie op de reisrichting), dus geplaatst ná het zeebeen (dat op de zeeknoop eindigt) gaf dat een naad van 33,02 km — het geografisch juiste eindpunt van de héle keten verschoof daardoor naar de zeeknoop in plaats van de kade. Fix: `maak_havenaanloop.py` opnieuw gedraaid met **omgekeerde `--van`/`--naar`** (zeeknoop → kade), zodat de puntvolgorde de reisrichting volgt. Generiek: **de volgorde waarin je `--van`/`--naar` aan `maak_havenaanloop.py` geeft, is de puntvolgorde die `--been-geojson`/`--stippel-geojson` letterlijk overneemt — kies die volgorde op basis van de plek van het been in de keten, niet op basis van welk punt "logisch" het startpunt is.**

**Toets:** `toets_knikken.py` — 2 knikken ≥60° (twee spikes van 13-14 m straal bij 1,100/119,500, midden in de Straat Makassar/Celebeszee — kleine MARNET-routeringsartefacten, geen kopmaak-plek), **0 omkeringen ≥150°**. `toets_rechte_benen.py --min-km 5` — been 1 (6,0 km, omwegfactor 1,006) staat op de lijst als 🟡 MIDDEL, precies zoals verwacht: het is een stippel met reden (haven-aanloop, rechte lijn na een mislukte routeerpoging), geen bevinding. Been 3 (36,2 km) komt niet op de lijst (omwegfactor 1,096, geen rechte lijn). json geldig: versie 2, punt_formaat lonlat, modaliteit `zee` (in de toegestane set), elk been ≥2 punten (2/644/34), bestandsgrootte **13,5 KB** (ruim < 300 KB).

**Gereedschapslessen:**
- Bevestigt de >5 km-haven-aanlooproregel (LAR-586) opnieuw: zonder de aanlopen was de bake op beide zijden gestopt bij een zeeknoop die kilometers van de echte kade ligt (5,97 en 33,02 km) — met de aanlopen sluit de keten exact op de brief-ankers aan.
- De puntvolgorde-valkuil bij `--stippel-geojson`/`--been-geojson` (hierboven) is een generieke les voor élke haven-aanloop die ná een ander been in de keten komt te staan, niet specifiek voor deze stroom.
- Een `maak_havenaanloop.py`-timeout is niet voorspelbaar uit de hemelsbrede afstand alleen: de korte Karratha-aanloop (6 km) liep vast terwijl de veel langere en geografisch lastigere Rudong-aanloop (33 km, sterk verslibd getijdengebied) in de eerste poging lukte — de bak-aanwijzing van de brief ("relatief kleine aanloop, timeout 300 zou vlot moeten lukken" resp. "FORSE aanloop") bleek op dit puntenpaar precies omgekeerd uit te komen dan verwacht. Geen tweede poging gedaan, conform protocol.
