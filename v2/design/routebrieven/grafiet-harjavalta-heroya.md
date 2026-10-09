# Routebrief (licht) · Grafiet · Fortum Harjavalta → Pori → Vianode Herøya (Finland → Noorwegen)

**stroom-id:** `grafiet-harjavalta-heroya` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** gerecycled grafietconcentraat uit Fortum's hydrometallurgische batterijrecyclingfabriek in Harjavalta (Satakunta) gaat per **truck** over vt 2 naar de haven van Pori (Mäntyluoto), per **zeeschip** door de Botnische Golf, de Oostzee, de Sont, het Kattegat en het Skagerrak naar de Langesundsfjord en de kade bij Herøya Industripark (Porsgrunn), en vandaar naar Vianode's Via ONE-fabriek op hetzelfde industrieterrein. **Aannemelijk: één bron voor de hele relatie** (zie §7): een MoU zonder site, volume of vervoerswijze; stoppunt = Via ONE.
**Welke as van het verhaal:** de Europese recyclinglus van batterijgrafiet, Finland → Noorwegen. Jaarvolume: **0 kt grafiet/j gedocumenteerd** (peiljaar 2025; het MoU noemt geen tonnage, alleen "potential to scale volumes over time" [1]). Ter vergelijking: Via ONE heeft ~2 kt/j nameplate (peiljaar 2025, sitelaag [10]) en Fortum's Harjavalta-uitbreiding 3.000 t batterijen/j [5] (batterijen, geen grafiet).

## 1 · Ketenkaart
```
Fortum Harjavalta `gr-fortum-harjavalta` ──(b1 truck · vt 2 · gemeten 46,4 km)──► Pori Mäntyluoto-kade `gr-pori-kade`
──(b2 zee · haven-aanloop, stippel, 25,7 km)──► zeeknoop 4537 ──(b3 zee · MARNET · 1.446,3 km)──► zeeknoop 4530 (Langesundsfjord)
──(b4 zee · haven-aanloop, stippel, ~11 km)──► Herøya-kade `gr-heroya-kade` ··(0,6 km, binnen het industrieterrein, geen been)··
Vianode Via ONE `gr-vianode-heroya` ⏹ stoppunt
```

## 2 · Benen
Alle benen **aannemelijk (MoU, één bron)**, zee is werkaanname, volume nul — dat staat in de beennaam, niet in de lijnstijl.
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-fortum-harjavalta` → `gr-pori-kade` | vt 2 (Harjavalta–Nakkila–Pori), laatste 1,1 km service/unclassified naar de kade | hemelsbreed 44 km, geen wegkm gepubliceerd; gemeten 46,4 (+5,5% t.o.v. hemelsbreed) | maak_stroombeen_weg, profiel `grafiet-harjavalta-heroya-fortum-pori` (al aangemaakt, extract `finland`) | nee |
| b2 | B | zee | `gr-pori-kade` → zeeknoop 4537 (61.4685,21.1715) | haven-aanloop Pori (kade 22,3 km hemelsbreed van de knoop > 5 km) | 25,7 (omwegfactor 1,15; 0 km land) | maak_havenaanloop (gelukt, ~1 min) | ja — "hier reikt het net niet" |
| b3 | B | zee | zeeknoop 4537 → zeeknoop 4530 (59.0498,9.7056) | Botnische Golf, Oostzee, Sont, Kattegat, Skagerrak | gemeten 1.446,3 (31 MARNET-edges); hemelsbreed 686; geen gepubliceerde zeekm | MARNET `--been zee` | nee |
| b4 | B | zee | zeeknoop 4530 → `gr-heroya-kade` | haven-aanloop Frierfjord (kade 8,8 km hemelsbreed van de knoop > 5 km) | 11,1 (omwegfactor 1,26; 0 km land) | maak_havenaanloop, **richting knoop → kade** (gelukt) | ja |
Totaal ~1.530 km (truck 46,8 + zee 25,7 + 1.446,3 + 11,1). Geen leiding, geen spoor, geen vlucht, geen fase D/E, geen last-mile-been. Geen gepubliceerde km voor b1 of b3: de ±15%-toets is alleen indicatie.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-fortum-harjavalta` | recycler / laadplek (kop) | Fortum Battery Recycling, Harjavalta (OSM-gebouw "Fortum", Sepänkatu) | 61.3243, 22.1006 | [8][1] | **aannemelijk** (z16 gezien: industrieel erf met loodsen en kleine hal, ten zuiden van een spoorlijn, aan de rand van het Harjavalta-industriegebied; niet aanwijsbaar als de hydromet-fabriek zelf; Nornickel/Boliden liggen ~1,7 km oostzuidoost: negatief anker) |
| `gr-pori-kade` | overslag truck → zee | Port of Pori, Mäntyluoto, noordkade met magazijnen (OSM quay/port) | 61.5959, 21.4966 | [6] | bron-gelegd (z15 gezien: kade aan open water met loodsen, opslagplaatsen, portaalkraan oostelijk en spoor; Mäntyluoto doet container en droge bulk [6]; welk pakhuis niet aan te wijzen) |
| `gr-heroya-kade` | overslag zee → truck/terrein | Herøya, zuidwestkade van het industriepark (OSM quay way 4153733; Grenland Havn-zijde) | 59.1174, 9.6249 | [7][8] | bron-gelegd (z15 gezien: kade met loodsen aan de westpunt van het schiereiland; het park is in 1928 met een eigen zeehaven begonnen [7]; kade is 0,6 km van Via ONE) |
| `gr-vianode-heroya` | losplek / anodefabriek (staart) | Vianode Via ONE, Herøya Industripark — hergebruik sitelaag-anker `w-vianode-heroya` | 59.1228, 9.6245 | [10][2][3] | bron-gelegd (sitelaag, z15: fabriekshal midden in Herøya Industripark; dit budget opnieuw bekeken, ongewijzigd) |
Zeeknopen (router, geen anker): 4537 (61.4685,21.1715) en 4530 (59.0498,9.7056). Negatief anker: Nornickel-raffinaderij 61.3188,22.1225 en Boliden-smelter 61.3175,22.1182 (andere bedrijven, niet hergebruiken).

## 4 · Via-punten (alleen b1; allemaal op vt 2, ref 2 trunk, 0 m uit de OSM-weg, geen stadscentrum)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | vt 2 west van Harjavalta | 61.3446, 22.0253 | pint vt 2 en niet de oude Kokemäenjoki-wegen |
| b1 | 2 | vt 2 bij Nakkila | 61.4068, 21.9161 | houdt de route op vt 2 tussen Harjavalta en Pori |
| b1 | 3 | vt 2 / vt 8 west van Pori | 61.4792, 21.7600 | splitsing vt 2/vt 8, ref "2;8" — de enige corridorkeuze; route blijft op de zuid-/westrand van Pori (centrum 2,5 km noordoostelijk) |
| b1 | 4 | vt 2 noordoost van Pori | 61.5494, 21.5906 | pint de nadering van Mäntyluoto vanaf vt 2 |
Alternatief (spoor Harjavalta–Pori) is niet getekend: geen bron noemt rail voor deze lading.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Harjavalta hydromet | Fortum Battery Recycling | zwarte massa/batterijmateriaal → metaalzouten + grafietconcentraat | uitbreiding naar 3.000 t batterijen/j; geen grafiettonnage | [5][1] |
| Via ONE, Herøya | Vianode | (secundair + synthetisch) grafiet → anodegrafiet | ~2 kt/j nameplate | [10][2] |

## 6 · Stoppunt
De brief stopt bij Via ONE: het MoU noemt geen volgende stap, en Vianode's klant-/celfabrieken zijn niet gedocumenteerd voor deze stroom. Fase D valt weg (geen bron voor wat er ná het anodemateriaal gebeurt); E vervalt.

## 7 · Open punten
- **Alleen een niet-bindend MoU** (13 mei 2025) [1][4]: geen afnemende site, geen transportwijze, geen volume, geen datum. Dat het naar Via ONE gaat is aannemelijk (enige commerciële Vianode-fabriek [2]), niet bevestigd. Dat het per zee gaat is een werkaanname; realistischer is mogelijk een containerfeeder via een hub. Volume 0 kt.
- **Fortum-anker** is een OSM-gebouw met naam Fortum; een B2B-gids noemt Rikkihappotehtaantie 6 (OSM-straat ~61.3224,22.1270, in het industriegebied, 1,7 km oostelijker) [9]. Beide niet als hydromet-fabriek bevestigd; Sepänkatu gekozen (enige Fortum-gebouw in OSM). Verschil voor de lijn: ~2 km.
- **Zee-lengte** 1.446 km is de router, geen gepubliceerde afstand; de eerdere raming 1.800–2.000 km klopt niet (Sont-route).
- **Kade-keuze Pori** (Mäntyluoto noordkade) en **Herøya** (zuidwestkade) zijn afgeleid uit OSM en de bolvorm, niet uit een bron die dit grafiet noemt.
- Vianode-Reuters-bericht (30 sep 2026: partner of verkoop gezocht) is in de haalbaarheidstoets genoemd maar niet door dit budget gelezen; mogelijke afbouw van de lijn.
- Webbudget: 2 van 3 WebSearch gebruikt; Overpass was onbereikbaar (HTTP 500/504); geen 2026-bericht over levering gevonden.

## 8 · Bronnen
[1] Vianode/Fortum persbericht 13-5-2025, MoU: recycled graphite concentrate uit Fortum's Harjavalta-hydromet, geen site/volume/transport. https://news.cision.com/vianode/r/vianode-and-fortum-battery-recycling-join-forces-to-advance-sustainable-ev-battery-recycling-value-c,c4149706
[2] Vianode persbericht 18-3-2025: Via ONE Herøya, productie sinds 2024; eigen recyclingproces. https://news.cision.com/vianode/r/vianode-launches-first-recycled-graphite-product-for-more-sustainable-evs-and-batteries,c4120371
[3] Herøya Industripark, pagina Vianode (geen adres of kade genoemd). https://www.heroya-industripark.no/en/companies-and-businesses-in-the-industrial-park/vianode
[4] S&P Global, 15-5-2025: bevestigt MoU, bestemming niet genoemd. https://autotechinsight.spglobal.com/news/5281900/vianode-fortum-battery-recycling-partner-to-advance-ev-battery-recycling-value-chain
[5] S&P Global: Fortum Harjavalta-uitbreiding naar 3.000 t batterijen/j (jaartal in snippet niet gezien). https://autotechinsight.spglobal.com/news/5261408/fortum-invests-usd28-million-to-boost-ev-battery-recycling-capacity-in-finland
[6] Wikipedia, "Port of Pori": Mäntyluoto container en droge bulk, max. diepgang 12 m. https://en.wikipedia.org/wiki/Port_of_Pori
[7] Wikipedia, "Herøya": industriepark 1,5 km² schiereiland, eigen haven sinds 1928, 59°07'N 9°37'E. https://en.wikipedia.org/wiki/Herøya
[8] OSM via Nominatim: building "Fortum", Sepänkatu, Harjavalta, way 1157997734 (61.32428, 22.10060). https://nominatim.openstreetmap.org/search?q=Fortum+Harjavalta&format=json
[9] OSM via Nominatim: Rikkihappotehtaantie, Harjavalta (61.3224,22.1270); adres uit B2B-gids (niet gelezen als primaire bron).
[10] `v2/design/grafiet-sitelaag.json`, site `w-vianode-heroya` (59.1228, 9.6245, ~2 kt/j).
[11] Esri via `v2/tools/sat_check.py`, `v2/build-cache/satcheck/sat-grafiet-harjavalta-heroya-{fortum,fortum16,pori,heroya-kade,vianode}.png`.
[12] Eigen meting: wegscan `wegscan_puur.py` (finland, 46,4 km, ref 2 trunk); MARNET zee 1.446,3 km; haven-aanlopen 25,7 en 11,1 km; zeeknopen via `hecht_marnet.marnet_zee`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-grafiet-harjavalta-heroya.json` (14,5 KB, versie 2, lonlat) · **functie:** `bak_grafiet_harjavalta_heroya` in `v2/tools/bak_stromen.sh` · **profiel:** `grafiet-harjavalta-heroya-fortum-pori` in `maak_stroombeen_weg.py`.
| # | modaliteit | km | naad | stippel | bron van de geometrie |
|---|---|---|---|---|---|
| 1 | truck | 46,8 | - | nee | wegscan_puur, extract finland, vt 2, 505 punten (46,4 km weg + 0,35 km aanloop) |
| 2 | zee | 25,7 | 0,0 | ja (haven-aanloop Pori, kade → knoop 4537) | maak_havenaanloop |
| 3 | zee | 1.446,3 | 0,0 | nee | MARNET, 31 edges, 160 punten |
| 4 | zee | 11,1 | 0,0 | ja (haven-aanloop Herøya, knoop 4530 → kade) | maak_havenaanloop |
Totaal 1.529,9 km · 703 punten · 4 markers (Fortum, Pori-kade, Herøya-kade, Via ONE). Alle naden 0,0 km.
**Recept:** `bash v2/tools/bak_stromen.sh grafiet-harjavalta-heroya`; alle vier benen zijn vooraf gebakken of via MARNET, de functie hecht ze aan elkaar. Geen letterlijke kopieën, geen vlucht, geen leiding, geen fase D/E.
**Toetsen:** b1 heeft geen gepubliceerde wegkm; gemeten 46,8 tegen hemelsbreed 44 (+6%), alleen indicatie. Markers Fortum, Pori en Herøya liggen op de lijn (0,0 km). De Via ONE-marker ligt 0,6 km van de lijn-eindkade: bewust, binnen het industrieterrein, geen last-mile-been. toets_knikken: 0 omkeringen; 4 spikes (14-56 m radius) aan de ankerzijde van b1 (erf- en kadewegen bij Fortum en Mäntyluoto), 2 krappe bochten in b3 (60,0 N 21,4 O en Sont, straal ~6 km), geen reparatie nodig. toets_rechte_benen: geen treffer voor deze stroom.
**Aannemelijk:** de hele relatie rust op één bron (MoU, 13-5-2025); volume 0; zee is werkaanname. Dat staat in de beennamen, niet in de lijnstijl. Beide stippels zijn haven-aanlopen ("hier reikt het net niet"), geen onzekerheidsaanduiding.
**Open:** Fortum-anker is een OSM-gebouw (alternatief 1,7 km oostelijker); Pori- en Herøya-kade afgeleid uit OSM en satelliet; Reuters-bericht 30-9-2026 (Vianode zoekt partner of verkoop) niet gelezen.
**Lessen:** profiel en tussenuitvoer stonden al klaar; het bakken was alleen de functie plus één run (zwaar-slot, enkele seconden).
