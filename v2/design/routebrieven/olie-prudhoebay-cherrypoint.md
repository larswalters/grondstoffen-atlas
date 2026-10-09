# Routebrief (licht) · Olie · Prudhoe Bay → Valdez → Cherry Point (VS)

**stroom-id:** `olie-prudhoebay-cherrypoint` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** Alaska North Slope-ruwe olie vanaf Pump Station 1 (Prudhoe Bay) per **leiding** (Trans-Alaska Pipeline, 1.281 km, OSM-compleet) naar de Valdez Marine Terminal, per **tanker** buitenom Vancouver Island en door de Straat van Juan de Fuca naar de steiger van BP Cherry Point (Blaine/Ferndale, Washington), met een korte steigerleiding naar de raffinaderij **(aannemelijk: één bron voor de bestemming)**.
**Welke as van het verhaal:** *de enige Amerikaanse binnenlandse crude-as zonder spoor of schip-naar-schip* — TAPS draagt 463 kb/d (2025; 2024: 465; piek 2.033 kb/d in 1988) [1]; het aandeel dat naar Cherry Point gaat is niet gepubliceerd, ruwweg de helft van de Alaska-lading gaat naar Californië en sinds 2026 gaan enkele ladingen naar Azië [4]. Cherry Point (BP, 225–236 kb/d) werd in 1971 gebouwd om Valdez-crude te verwerken [3][5].

## 1 · Ketenkaart
```
Prudhoe Bay PS1 `ol-prudhoe-ps1` ──(b1 leiding · TAPS: Brooks Range → Yukon → Fairbanks → Delta Junction → Thompson Pass · 1.281 km OSM / 1.288 gepubliceerd)──►
Valdez Marine Terminal `ol-valdez-term` / berth `ol-valdez-kade` ──(b2 zee · Golf van Alaska → buitenom Vancouver Island → Juan de Fuca-monding (via-punt) → Haro/Boundary Pass · 2.341 km)──►
Cherry Point-steiger `ol-cherrypoint-pier` ──(b3 haven-aanloop 12 km stippel; b4 steigerleiding 0,8 km stippel + 2,6 km OSM)──► BP Cherry Point-raffinaderij `ol-cherrypoint-raf` (stoppunt)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Prudhoe Bay PS1 → Valdez Marine Terminal | Trans-Alaska Pipeline System (Alyeska), 48" | 1.288 (800,3 mi) [2]; OSM 1.281,1 = −0,5% [6] | OSM-way's `man_made=pipeline`, `substance=oil`, name "Trans-Alaska Pipeline (System)": 429 ways, 8.526 punten, één component (ondergronds 597 + bovengronds 626 + surface 58 km) | nee |
| b2a | B | zee | Valdez-berth → Juan de Fuca-monding (MARNET-knoop 7815, 48.4862,-124.7292) | Golf van Alaska, buitenom Haida Gwaii en Vancouver Island | 2.139,4 (MARNET, gemeten) | MARNET kade → knoop | nee (kade 1,4 km van zeeknoop 2618) |
| b2b | B | zee | Juan de Fuca-monding → Cherry Point-steiger **(aannemelijk: één bron)** | Straat van Juan de Fuca → Haro Strait/Boundary Pass → zeeknoop 3197 | 202,1 (MARNET, gemeten) | MARNET knoop → kade | aanloop: ja (12,2 km) |
| b3 | B | zee | zeeknoop 3197 (48.7537,-122.7764) → Cherry Point-steiger | haven-aanloop, LAR-586 | 12,2 (rechte stippel) | `maak_havenaanloop.py` onder timeout 300, anders stippel | ja — 1:10M-kust kent de steiger niet |
| b4a | C | leiding | steigerkop → wal-eind trestle (48.8659,-122.7524) | steiger-trestle | 0,84 [eigen meting] | stippel | ja — trestle niet in OSM |
| b4b | C | leiding | wal-eind → raffinaderij (48.8844,-122.7423) | steigerleiding BP | 2,6 [6] | OSM-way 99341833 (`substance=oil`, naamloos), omgedraaid (pier → raffinaderij) | nee |

Totaal ≈ 1.281 + 2.342 + 12 + 3,4 ≈ 3.639 km. **Ontwerpafwijking:** de haalbaarheidstoets mat één zeebeen van 2.270,5 km, maar dat pad loopt door de **Binnenpassage** (Hecate Strait → Queen Charlotte Strait → Johnstone Strait → noordelijke Straat van Georgia); crude-tankers naar Cherry Point komen via Juan de Fuca en Rosario Strait [3], het ontwerp noemt zelf "Golf van Alaska → Juan de Fuca". Daarom is het zeebeen gesplitst op de Juan de Fuca-monding (corridorkeuze, §4): 2.139,4 + 202,1 = **2.341,5 km** (hemelsbreed 2.009 km, +17% — kustroute).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-prudhoe-ps1` | kop van de leiding | Prudhoe Bay Pump Station 1 (Alyeska) | 70.2563, -148.6194 | [2][6] (Wikipedia 70.2572,-148.6189; OSM-pijpknoop op 5 m) | bron-gelegd (z15: pompstation met twee witte tanks en procesgebouwen, bovengrondse TAPS-buis loopt NW→ZO langs het terrein, ijsvlakte-toendra eromheen) |
| `ol-valdez-term` | einde van de leiding / terminal | Valdez Marine Terminal (Alyeska) | 61.0830, -146.3684 | [2][6] (OSM-pijpeinde, surface-way 529753950) | bron-gelegd (z15: terminalcomplex aan Port Valdez: tankpark in een dijkvak 1 km west, tankgroep aan de weststeiger, punt op de terminalweg 0,8 km zuid van de oostelijke steiger) |
| `ol-valdez-kade` | overslag leiding → zee | Valdez-tankerberth (oostelijke steiger, laadarmen) | 61.0899, -146.3685 | eigen satellietblik; [2] (vier tankerberths) | bron-gelegd (z17: steigerplatform met laadarmen en trestle aan de oostelijke steiger; tweede steigercomplex 1,2 km west) — MARNET-zeeknoop 2618 (61.1024,-146.3760) op 1,4 km, geen aanloop |
| `ol-cherrypoint-pier` | overslag zee → leiding | BP Cherry Point-tankersteiger (NW-berth) | 48.8631, -122.7630 | [3][7]; haalbaarheidstoets | bron-gelegd (z17: rode tanker afgemeerd aan de steigerkop van de lange trestle; tweede berth 0,6 km ZO; tweede tanker voor anker) |
| `ol-cherrypoint-raf` | stoppunt / raffinaderij | BP Cherry Point-raffinaderij | 48.8844, -122.7423 | [3][5][6]; Wikipedia 48.885,-122.738 (0,3 km) | bron-gelegd (z15: process-units en groot tankpark; punt op de NW-hoek van het tankpark, waar de OSM-steigerleiding begint) |

## 4 · Via-punten
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2a/b2b | 1 | Juan de Fuca-monding (MARNET-knoop 7815) | 48.4862, -124.7292 | pint de **buitenroute** (Golf van Alaska → Cape Flattery) i.p.v. de MARNET-kortste route door de Binnenpassage (2.270,5 km, afgewezen); einde b2a = begin b2b op dezelfde knoop (naad 0) |
b1 (leiding) heeft geen via-punten: de geometrie is de OSM-way zelf. Controlepunten op de lijn (niet als via te gebruiken): Yukon River-brug 0,3 km, Delta Junction 1,2 km, Thompson Pass 0,4 km, Fairbanks/Fox 2,6 km, Atigun Pass 3,7 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Valdez Marine Terminal | Alyeska (BP, ConocoPhillips, ExxonMobil) | TAPS-crude → 18 opslagtanks → tanker | 9,18 mln vaten opslag, vier tankerberths [2]; doorvoer 463 kb/d (2025) [1] | [1][2] |
| BP Cherry Point-raffinaderij | BP | ANS-crude (tanker), Canadese pijpleidingcrude, Bakken per spoor → benzine/diesel/straalbrandstof/gecalcineerde cokes | 225 kb/d [3] – ~236 kb/d [5] | [3][5] |

## 6 · Stoppunt
De brief stopt bij de BP Cherry Point-raffinaderij: één bron koppelt Valdez-crude aan dit afnemende complex [3][5]; geen bron geeft ladingen of productexport per route. Fase D/E vervallen.

## 7 · Open punten
- **Bestemming = aannemelijk, één bron.** Wikipedia en AK Business Magazine (2018) noemen ANS als hoofdcrude van Cherry Point; er is geen 2026-bron voor Cherry Point zelf. Alaska Beacon (13-5-2026: ~helft naar Californië, enkele ladingen naar Daesan/Indonesië) gaf HTTP 403 en is niet onafhankelijk gelezen. Cherry Point krijgt ook Canadese pijpleidingcrude en Bakken per spoor [3]. Fallback: inkorten tot Valdez en het id corrigeren naar `olie-prudhoebay-valdez`.
- **Het aandeel van de 463 kb/d dat naar Cherry Point gaat is niet gepubliceerd**; het jaarvolume is het TAPS-totaal.
- **Corridor binnen Washington:** MARNET kiest Haro Strait/Boundary Pass; Wikipedia noemt Rosario Strait [3]. Verschil enkele km, niet getekend.
- **Binnenpassage-uitsluiting is eigen redenering** (bron [3] noemt de Juan de Fuca-aanvoer, geen bron over een uitsluitingszone gevonden).
- **Naad b1 → b2a 2,2 km:** het OSM-pijpeinde ligt 0,8 km van de berth en de MARNET-zeeknoop 1,4 km van de berth in Port Valdez; geen OSM-pier op de terminal (Overpass onbereikbaar, pier-query 504). Procesgat voor §9.
- **Pier→raffinaderij-way 99341833 is naamloos en zonder operator**; verband afgeleid uit de ligging (begint aan de trestlewal, eindigt bij het tankpark).
- **pyosmium is op deze machine geblokkeerd** (beleid voor toepassingsbeheer); het stik-script leest de pbf met een pure-Python-lezer (zie §9-aanwijzing).

## 8 · Bronnen
[1] Alyeska Pipeline, Historic Throughput — 2025 gemiddeld 462.821 b/d, 2024 464.784, piek 1988 2.032.928 b/d. https://alyeska-pipe.com/historic-throughput/
[2] Wikipedia, Trans-Alaska Pipeline System — 800,3 mi (1.288 km), 48", Valdez-terminal 18 tanks / 9,18 mln vaten / vier tankerberths. https://en.wikipedia.org/wiki/Trans-Alaska_Pipeline_System
[3] Wikipedia, Cherry Point Refinery — BP, 225.000 b/d, "most crude from the Alaska North Slope", via Juan de Fuca en Rosario Strait naar de eigen pier, 48.885,-122.738. https://en.wikipedia.org/wiki/Cherry_Point_Refinery
[4] Alaska Beacon, 13-5-2026, "More Alaska crude flows to Asia as Strait of Hormuz stays shut" (via haalbaarheidstoets; niet zelf gelezen, 403). https://alaskabeacon.com/2026/05/13/more-alaska-crude-flows-to-asia-as-strait-of-hormuz-stays-shut/
[5] Alaska Business Magazine, oktober 2018, "Where does all that oil go?" — Cherry Point ~236.000 b/d, gebouwd 1971 voor Valdez-crude. https://digital.akbizmag.com/issue/october-2018/where-does-all-that-oil-go/
[6] OpenStreetMap (ODbL) — eigen scan us-alaska en us-washington (2026-10-09): 429 TAPS-ways → pad PS1 → Valdez 1.281,1 km; Washington-way 99341833. Overpass-mirror maps.mail.ru bevestigt de Valdez-ways 8992395 en 529753950.
[7] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-olie-prudhoebay-cherrypoint-{prudhoe-ps1,valdez-term,valdez-kade,valdez-west,cherrypoint-pier,cherrypoint-kade,cherrypoint-raf}.png`.
[8] MARNET (`v2/build-cache/marnet-preais`, `hecht_marnet.py route`) — drie proefruns 2026-10-09: 2.270,5 km (Binnenpassage, afgewezen), 2.139,4 + 202,1 km (gekozen).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)

**Stroom `olie-prudhoebay-cherrypoint`** → `v2/data/stroomroute-olie-prudhoebay-cherrypoint.json` (188,7 KB, versie 2, lonlat) — 6 benen, **3.638,3 km**, 8.805 punten, 5 markers (2 stippels: haven-aanloop en trestle). Recept: `bash v2/tools/bak_stromen.sh olie-prudhoebay-cherrypoint` (functie `bak_olie_prudhoebay_cherrypoint`; geen profiel in `maak_stroombeen_weg.py`, geen extract bij de bake).

| # | modaliteit | been | km | punten | stippel | naad naar vorig been |
|---|---|---|---|---|---|---|
| 1 | leiding | TAPS Prudhoe Bay PS1 → Valdez Marine Terminal (OSM-ways gestikt, doorgetrokken) | 1.281,1 | 8.526 | nee | — |
| 2 | zee | Valdez-berth → Juan de Fuca-monding (MARNET, via-punt = knoop 7815) | 2.139,4 | 225 | nee | 2,20 km |
| 3 | zee | Juan de Fuca-monding → Cherry Point-steiger (aannemelijk: één bron) | 202,1 | 27 | nee | 0,00 km |
| 4 | zee | haven-aanloop Cherry Point (zeeknoop 3197 → steigerkop, over water) | 12,3 | 5 | ja | 0,00 km |
| 5 | leiding | steiger-trestle (steigerkop → wal) | 0,8 | 2 | ja | 0,00 km |
| 6 | leiding | BP-steigerleiding (OSM-way 99341833, pier → raffinaderij) | 2,6 | 20 | nee | 0,00 km |

**Markers (alle 5 uit §3, vervangen de automatische afleiding):** `ol-prudhoe-ps1` 70.2563,-148.6194 · `ol-valdez-term` 61.0830,-146.3684 · `ol-valdez-kade` 61.0899,-146.3685 · `ol-cherrypoint-pier` 48.8631,-122.7630 · `ol-cherrypoint-raf` 48.8844,-122.7423. Afstand tot de lijn: 0,00 km, behalve `ol-valdez-kade` 0,77 km (anker op de berth, niet op het routeerpunt: de MARNET-lijn begint op 61.1024,-146.3760, 1,4 km van de berth; bewust geen via bijgeschoven).

**Toets.** b1: 1.281,1 km tegen gepubliceerd 1.288 = **−0,5%** (norm ±15%). Zee b2a+b2b: 2.341,5 km tegen hemelsbreed 2.009 km = +17% (kustroute; geen gepubliceerde ladingroute, dus indicatie). Naden: alleen b1 → b2a **2,20 km** (< 5 km, procesgat: OSM-pijpeinde en MARNET-zeeknoop 2618 liggen in Port Valdez op 0,8 resp. 1,4 km van de berth, geen OSM-pier op de terminal); zee-naad b2a/b2b 0,00 km; aanloop sluit op zeeknoop 3197 en op de steigerkop (0,00 km). `toets_knikken`: 16 knikken ≥ 60°, **0 omkeringen**, 0 terugloop: 1 krappe bocht in b2a (55.7156,-134.3663, 88°, R 4,7 km), 4 in b2b (Juan de Fuca, 68–92°, R 5–7 km), 11 spikes in b6 (5–27 m jogs in de OSM-steigerleiding, geen fout). `toets_rechte_benen --min-km 5`: geen melding voor deze stroom (de aanloop is 12,3 km met omwegfactor 1,004, de trestle is 0,8 km). `json.load` slaagt, versie 2, punt_formaat lonlat, modaliteiten {leiding, zee}, elk been ≥ 2 punten, 188,7 KB (< 300 KB, geen DP nodig).

**Toelichting per bijzonder been.**
- *b1 leiding (doorgetrokken):* OSM heeft de hele TAPS (429 ways, één component, 8.526 punten); geometrie uit de klaargezette `olie-prudhoebay-cherrypoint-leiding-taps.geojson` (stik-script `v2/tools/maak_leidingbeen_olie_prudhoebay_cherrypoint.py`, pure-Python-PBF-lezer omdat pyosmium op deze machine geblokkeerd is). Geen stippel: de leiding is gemeten, niet geschematiseerd.
- *b2 zee gesplitst op de Juan de Fuca-monding:* de MARNET-kortste route kade → kade loopt door de Binnenpassage (2.270,5 km, afgewezen); het via-punt (knoop 7815, einde b2a = begin b2b) dwingt de buitenroute af.
- *b4 haven-aanloop (stippel):* de steiger ligt 12,2 km van zeeknoop 3197 (LAR-586, > 5 km). `maak_havenaanloop.py` slaagde nu binnen de timeout (3 m 05 s): 12,3 km over water, 5 punten, 0,00 km over land. Het tool schrijft kade → zeeknoop; de bake verwacht reisvolgorde, dus is een omgedraaide kopie gemaakt (`…-aanloop-cherrypoint-rev.geojson`) en gebruikt via `--stippel-geojson`. Eerdere toets-run (300 s) gaf geen pad; dit is dus een eerste succes, geen tweede poging na een timeout.
- *b5 trestle (stippel):* de 0,84 km steiger-trestle staat niet in OSM; rechte lijn tussen de steigerkop en het wal-eind van b6.
- *b6 (doorgetrokken):* OSM-way 99341833 is naamloos en zonder operator; het verband met de BP-pier/raffinaderij is afgeleid uit de ligging (§7).
- *Geen vlucht, geen wegbeen, geen spoor, geen kopie van een andere stroom* (olie-westridge-ulsan deelt alleen ~200 km kanaal; niet gekopieerd).

**Lessen.**
- Een klaargezet intermediair bestand (hier de aanloop) kan richting kade → knoop hebben terwijl de bake reisvolgorde knoop → kade verwacht; `hecht_marnet.py` draait --been-geojson niet om. Draai het geojson om vóór gebruik, anders ontstaat een naad van 12 km.
- `maak_havenaanloop.py` is niet deterministisch snel: dezelfde invoer liep eerder op 300 s vast en slaagde later in 185 s (gedeelde CPU); een tussenbestand uit een eerdere poging kan ook al bestaan.
- De slot-functie uit de taakbeschrijving gebruikt `rm -rf "$d"` met een variabel pad, wat de veiligheidscontrole van Claude Code blokkeert; slots met letterlijke paden (`mkdir`, later `rm -f …/sinds` + `rmdir`) werken wel.

**Meldingen aan de eigenaar (niet door deze bake aangepast).** Sitelaag olie mist Prudhoe PS1, Valdez Marine Terminal en BP Cherry Point; sitelaag-coördinaat Cherry Point gelijktrekken met 48.8844,-122.7423. pyosmium geblokkeerd op deze machine. Registerregel (centraal): sleutel `ol-pc`.
