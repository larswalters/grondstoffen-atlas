# Routebrief (licht) · olie — Kozmino (Rusland) → Dalian (China)

**stroom-id:** `olie-kozmino-dalian` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** ESPO-pijpleidingcrude van het Pacific-exportterminal Kozmino (Nachodka-baai, Primorje) per
**zeeschip** door de Japanse Zee, de Straat van Korea/Tsushima en de Gele Zee naar het PetroChina
Dalian-raffinagecluster (Ganjingzi-district, Liaoning) — stoppunt bij de raffinaderij, geen tweede leg.
**Welke as van het verhaal:** ESPO-Pacific — de Stille-Oceaan-helft van Ruslands olie-omleiding sinds 2022 (de
Baltische helft is al gedekt door `olie-primorsk-jamnagar`). Kozmino verscheept overwegend naar Chinese havens:
in januari 2025 gingen 34 van 37 ESPO-ladingen (elk ~100.000 t) naar China, 3 naar India [9]; in december 2023
ging minstens 85% van het record-volume (925.000 vaten/dag) naar China [10]; in 2019 was dat 77,6% (23,5 van
30,3 mln ton, jan–nov) [11]. Dalian specifiek is **aannemelijk: één bron** — geen bron bevestigt een lading tot
op kade-niveau, het is de dichtstbijzijnde grote raffinagecluster met een eigen crude-kade.

## 1 · Ketenkaart
```
Kozmino-exportterminal `ol-kozmino-kade` (Transneft, ESPO-pijplijnterminus, Nachodka-baai, Primorje)
   ──(b1 zee · Japanse Zee → Straat van Korea/Tsushima → Gele Zee ·
       ~1.400 km [ontwerp-schatting; MARNET meet de exacte lengte] ·
       haven-aanloop aan beide zijden)──► Dalian-raffinagecluster `ol-dalian-raffinaderij`
       (PetroChina Dalian Petrochemical, Ganjingzi-district) ── stoppunt (aannemelijk: één bron)
```
Risiconoot: de kortste, minst-knelpunt-gevoelige route van alle olie-ketens in de atlas (geen grote zeestraat
onderweg) — juist daarom politiek aantrekkelijk voor Rusland/China, maar gevoelig voor secundaire
VS-sancties op Chinese afnemers/banken (zoals `olie-rastanura-zhoushan`/Kharg-Dongjiakou-klasse). Een gerichte
webcheck op "Port Kozmino ESPO China sanctions 2026" leverde geen nieuwe disruptie op buiten het bekende
2022-prijsplafond-sanctiepakket [12] — geen aanwijzing voor een actuele blokkade van deze specifieke as.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `ol-kozmino-kade` → `ol-dalian-raffinaderij` | Japanse Zee–Straat van Korea/Tsushima–Gele Zee | ~1.400 [ontwerp; MARNET meet exact] | MARNET | aanloop: ja (beide zijden — zie §7) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-kozmino-kade` | laadplek / kade | Kozmino-exportterminal (Transneft, ESPO-terminus), Nachodka-baai, Primorje | 42.7185, 133.0090 | [1][2][3][8] | bron-gelegd (z17 gezien: pier met single point mooring aan de kop, een geladen ruwe-olietanker langszij de steiger, pijpleiding-trestle over de havendam naar een tankenpark met blauwe daken aan land) |
| `ol-dalian-raffinaderij` | losplek / raffinaderij | PetroChina Dalian Petrochemical (Dalian Petrochemical Refinery, CNPC), Ganjingzi-district, Liaoning | 38.9788, 121.6539 | [4][5][6][8] | bron-gelegd (z16 gezien: uitgestrekte velden ronde opslagtanks (deels floating-roof), procesinstallaties en pijpleidingracks over meerdere km² langs de kust, met een eigen tanker-jetty de zee in aan de zuidoostzijde) |

## 4 · Via-punten
Geen — b1 is een zeeleg; MARNET routeert kade→kade en de genoemde zeestraat (Tsushima/Korea) ligt al in de
routeergraaf. Geen corridorkeuze op het water die een handmatig via-punt vraagt.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Dalian-raffinagecluster | PetroChina (CNPC) | ESPO-ruwe olie (mix) → benzine/diesel/petrochemie | 20,5 mln ton/jaar ruwverwerking, 48 raffinage- + 7 chemie-eenheden [5] | [5][6] |

## 6 · Stoppunt
De brief stopt bij het Dalian-raffinagecluster: dit is de bestemming uit het ketenontwerp en fase D/E
(productexport vanaf Dalian) is een aparte keten met eigen bestemmingen. Geen bron in deze ronde koppelt een
specifieke ESPO-lading aan een specifieke productstroom — conform de haalbaarheidstoets is dit het bewuste
stoppunt, met de Dalian-bestemming zelf al gemarkeerd als **aannemelijk: één bron**.

## 7 · Open punten
- **Dalian specifiek is aannemelijk, niet cargo-niveau bevestigd.** Kozmino verscheept naar meerdere Chinese
  havens (Rizhao, Yantai, Ningbo, Huizhou e.a.) naast Dalian; geen bron in deze ronde koppelt een specifieke
  ESPO-lading aan het PetroChina Dalian-complex. Conform de haalbaarheidstoets is dit gemarkeerd in de
  beennaam/§1, niet in de lijnstijl (het been blijft doorgetrokken).
- **Beide ankers liggen ver van een MARNET-zeeknoop** — gemeten met `hecht_marnet.marnet_zee()`:
  Kozmino-kade **56,5 km** tot de dichtstbijzijnde zeeknoop (2596, 42,70000/133,70000), Dalian-raffinaderij
  **8,33 km** tot zeeknoop 5650 (38,94870/121,74220). Kozmino zit ruim buiten de normale 25 km-snapgrens →
  vraagt een expliciete `maak_havenaanloop.py`-poging (kortste pad over water door Nachodka-baai en de Japanse
  Zee naar de zeeknoop); lukt die niet binnen de 300 s-timeout, dan een rechte stippel-aanloop met reden
  (zoals bij `olie-primorsk-jamnagar` b1, waar de Primorsk-aanloop op dezelfde manier faalde). Dalian zit
  binnen de 25 km maar boven de 5 km-drempel uit de bakhandleiding (2026-09-28) → ook daar een haven-aanloop,
  óók al snapt de router in principe direct.
- **~1.400 km is een ontwerp-schatting zonder gepubliceerde bron** — MARNET meet de exacte lengte via de
  Japanse Zee–Tsushima–Gele Zee-corridor; een afwijking > 15% is een bevinding voor §9, geen reden om
  via-punten bij te schuiven.
- **Jaarvolume niet op Dalian-niveau gepubliceerd** — zie §1 voor de Kozmino→China-aandelen (77,6%–92% van de
  ladingen, 2019–2025); geen bron splitst dat naar het Dalian-complex specifiek.
- **Kozmino-jettygeometrie**: de zichtbare terminal bestaat uit een havendam met pijplijn-trestle naar een
  SPM-kop in de baai (waar de geziene tanker ligt) plus een tweede, groter tankenpark ~1,5 km landinwaarts
  (satelliet gezien bij 42,735/133,042, terrassen/aarde-werk consistent met de aangekondigde
  capaciteitsuitbreiding na 2025 [7]) — dat tweede tankenpark is niet apart geankerd (licht-werkwijze: één
  anker per site/overslag; de kade is de site voor deze keten).

## 8 · Bronnen
[1] Wikipedia, "Port Kozmino" — coördinaten 42.730874/133.027267 (Wikipedia-punt, niet satelliet-gelegd), Nachodka-baai, Transneft, ESPO-terminus sinds eind 2012, terminal geopend 28-12-2009. https://en.wikipedia.org/wiki/Port_Kozmino
[2] Wikipedia, "Eastern Siberia–Pacific Ocean oil pipeline" — pijpleidingsysteem van Transneft voor export van Russische ruwe olie naar Japan/China/Korea, terminus Kozmino. https://en.wikipedia.org/wiki/Eastern_Siberia%E2%80%93Pacific_Ocean_oil_pipeline
[3] Transneft, officiële site. https://www.transneft.ru/en/
[4] Wikipedia (via websearch-snippet), "List of oil refineries" — Dalian Petrochemical Refinery (PetroChina, CNPC), 400.000 vaten/dag.
[5] IndustryAbout.com, "PetroChina - Dalian Oil Refinery" — adres 1 Shanzhong Street, Ganjingzi-district, Dalian; 20,5 mln ton/jaar ruwverwerking, 48 raffinage- + 7 chemie-eenheden. https://www.industryabout.com/country-territories-3/61-china/oil-refining/109-petrochina-dalian-oil-refinery
[6] OpenStreetMap (ODbL) via Nominatim — relation 6882281 "大连石化" (landuse=industrial), Ganjingzi-district, Dalian, centroïde 38,9787516/121,6539101, boundingbox 38,9580347–39,0001862 / 121,6257243–121,6668540. https://www.openstreetmap.org
[7] S&P Global/GEM/Wikipedia via `v2/design/olie-sitelaag.json` (anker w-kozmino, hergebruikt voor de coördinaat-kruiscontrole) — ESPO-pijpleiding max. afgifte 1,6 mln vaten/dag (80 mln ton/jaar-ontwerp na de 2025-uitbreiding); dit verklaart het waargenomen aarde-/terraswerk bij het landtankenpark.
[8] Esri World Imagery via `v2/tools/sat_check.py` (z14–z17, live) — `v2/build-cache/satcheck/sat-olie-kozmino-dalian-kozmino-jetty.png` (definitief kade-anker), `sat-olie-kozmino-dalian-kozmino.png` en `-kozmino-tankfarm.png` (oriëntatie/tankenpark), `sat-olie-kozmino-dalian-dalianrefinery.png` en `-dalianrefinery-zoom.png` (raffinaderij-anker).
[9] Hellenic Shipping News / S&P Global Commodity Insights — januari 2025: 37 ESPO-ladingen vanaf Kozmino, 34 naar China, 3 naar India. https://www.hellenicshippingnews.com/russias-espo-crude-exports-from-kozmino-port-at-record-high-in-dec-kommersant/
[10] OilPrice.com — december 2023: ESPO-export vanaf Kozmino record 925.000 vaten/dag, minstens 85% naar China. https://oilprice.com/Latest-Energy-News/World-News/Russia-to-Boost-Exports-of-Chinas-Favorite-Russian-Crude-in-July.html
[11] PortNews.ru — 250-miljoenste-ton-mijlpaal ESPO-export via Kozmino; 2019-cijfer jan–nov 30,3 mln ton totaal, 23,5 mln ton (77,6%) naar China. https://en.portnews.ru/news/289309/
[12] Wikipedia, "2022 Russian crude oil price cap sanctions" (webcheck uit de haalbaarheidstoets — geen nieuwe disruptie gevonden buiten dit reeds bekende sanctiepakket).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `olie-kozmino-dalian`** → `v2/data/stroomroute-olie-kozmino-dalian.json` — 3 benen, **2.075,6 km**, 285 punten, 2 markers (2 stippel).
Recept: `bak_stromen.sh` (functie `bak_olie_kozmino_dalian`).

**b1 (zee, stippel, haven-aanloop Kozmino):** `--stippel-geojson "zee|haven-aanloop Kozmino (schematisch, over water — kade 56,5 km van de MARNET-zeeknoop)|…"`. `maak_havenaanloop.py` lukte (geen timeout): **60,5 km**, 72 punten, kortste-pad-over-water tussen de kade (42,7185/133,0090) en zeeknoop 2596 (42,70000/133,70000). Omwegfactor 1,071 t.o.v. de rechte lijn (56,5 km, waarvan 27% "over land" op de 1:10M-kustlijn); de gekozen trap (cel 0,005° gebufferd) laat 0,39 km "land" over, uitsluitend aan het kade-uiteinde zelf (de 1:10M-kustkorrel — een kade ligt daar per definitie óp land, geen echte landkruising midden op de lijn).

**b2 (zee, MARNET-route, zeeknoop → zeeknoop):** `--been "zee|zeeschip Kozmino → Dalian (Japanse Zee – Straat van Korea/Tsushima – Gele Zee)|42.70000,133.70000|38.94870,121.74220"` — snap 0,000 km aan beide zijden (begint/eindigt letterlijk op de zeeknoop). **2.006,8 km**, 211 punten, tegen de ontwerp-schatting **~1.400 km = +43,3%**, ruim boven de ±15%-norm en ook boven de bandbreedte die de bak-aanwijzing zelf al als mogelijk aanmerkte (~1.400–1.700 km, vergelijkbaar met olie-primorsk-jamnagar's +22,6%). Dit is een **bevinding**, geen reden om iets bij te schuiven: de 1.400 km was expliciet een ontwerp-schatting zonder gepubliceerde bron (brief §1/§7), en MARNET routeert hier zichtbaar niet in een rechte lijn maar volgt de kustcontour van de Japanse Zee en de bocht om het Koreaanse schiereiland via de Straat van Korea/Tsushima naar de Gele Zee — een substantieel langere weg dan de hemelsbrede ~1.400 km. `toets_knikken.py` bevestigt dat dit geen artefact is: 0 knikken ≥60°, 0 omkeringen — een gladde, geloofwaardige zeeroute, geen zigzag die de km opblaast.

**b3 (zee, stippel, haven-aanloop Dalian):** `--stippel "zee|haven-aanloop Dalian (schematisch — kade 8,33 km van de MARNET-zeeknoop; maak_havenaanloop.py-timeout, geen tweede poging)|38.94870,121.74220|38.9788,121.6539"`. `maak_havenaanloop.py` liep vast op de 300 s-timeout (exit 124, dezelfde faalmodus als de Primorsk-aanloop bij `olie-primorsk-jamnagar`) → conform de bak-aanwijzing **geen tweede poging**, rechte stippel. **8,3 km**, 2 punten, omwegfactor 1,000 (per definitie, het is de rechte lijn).

**Markers:** `ol-kozmino-kade` (0,000 km — eerste punt van b1, exact het anker) · `ol-dalian-raffinaderij` (0,000 km — laatste punt van b3, exact het anker). Geen anker≠routeerpunt-afwijking: beide haven-aanlopen eindigen letterlijk op het anker, zoals verwacht.

**Naden:** b1→b2 0,000 km · b2→b3 0,000 km — beide aanlopen eindigen letterlijk op het beginpunt van het volgende segment (geen procesgat, geen dichtgetrokken naad).

**Toets:** `toets_knikken.py` — **0 knikken ≥60°, 0 omkeringen ≥150°, 0 terugloop** over het hele hoofdzeebeen (211 punten) — geen bevinding, bevestigt een gladde MARNET-route zonder omweg-artefacten. `toets_rechte_benen.py --min-km 5` — b3 (8,3 km, omwegfactor 0,996 — geldt als de rechte-lijn-referentie) staat op de lijst als 🟡 MIDDEL (stippel): correct, het is de bewuste rechte terugval-stippel na de timeout, geen bevinding op zichzelf; b1 (60,5 km, geroutet over water) staat er terecht niet op. json geldig: versie 2, punt_formaat lonlat, modaliteiten allemaal `zee` (in de toegestane set), elk been ≥2 punten (72/211/2), bestandsgrootte **6,1 KB** (ruim < 300 KB).

**Open punt bevestigd, niet opgelost:** de +43,3%-afwijking op b2 en de Dalian-bestemming als "aannemelijk: één bron" (brief §1/§7) blijven beide staan zoals de brief ze al noemde — dit bakwerk verifieert de geometrie, het verandert niets aan de brondekking.

**Gereedschapslessen:**
- Een 56,5 km-rechte-lijn met 27% "over land" hoeft geen slechte haven-aanloop-kandidaat te zijn: `maak_havenaanloop.py`'s eigen trapsgewijze zoektocht (van grof-gebufferd naar fijn-kaal) vond hier alsnog een schoon pad van 60,5 km met slechts 0,39 km resterend "land", uitsluitend op het kade-uiteinde (de 1:10M-kustkorrel). Beoordeel de haalbaarheid dus aan de uitkomst van het tool, niet aan de rechte-lijn-vooraf-schatting.
- Een grote km-afwijking (+43,3%) op een zuiver zeebeen zonder enige knik/omkering (`toets_knikken.py` 0/0/0) is het duidelijkste signaal dat de afwijking in de **ontwerp-schatting** zit en niet in de geometrie: een gladde, kustvolgende MARNET-route die consequent langer is dan een hemelsbrede aanname, is precies het patroon dat de bakhandleiding als "bevinding, niet dichtschuiven" aanmerkt.
