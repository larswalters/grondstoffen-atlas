# Routebrief (licht) · grafiet — Zavallya-mijn/fabriek (Oekraïne) → Reni-Donauhaven → Constanța (Roemenië)

**stroom-id:** `grafiet-zavallya-constanta` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** Oekraïens verwerkt battery-grade grafiet (Zavalievsky Graphite, deels uit geïmporteerd
Afrikaans vlokerts) per **truck** door oorlogsgebied naar de kleine Donau-rivierhaven Reni, per **binnenschip**
over de Donau-Sulina-route en de Zwarte Zee-kust naar Constanța (Roemenië) — stoppunt, want geen bron noemt een
Europese eindafnemer bij naam.
**Welke as van het verhaal:** Oekraïne-oorlogscorridor via de Donau-rivierhavens naar de EU. Nominale
plantcapaciteit 20 kt/j; werkelijk maart 2026 19,14 t (87% yield, geïmporteerd Afrikaans vlokerts, volledig
verkocht aan één niet-genoemde Europese batterijklant à US$3.000/t) [1]; juli 2026 nieuwe campagne met
doeltarget ~1.200 t, waarvan ~660 t al gecontracteerd aan Europese afnemers (~€377.140), levering t/m nov. 2026
[6] — actueler en groter dan de maart-verkoop, maar nog altijd < 6% van de nominale 20 kt/j.

## 1 · Ketenkaart
```
Zavallya-mijn/fabriek (Zavalievsky Graphite / Volt Resources) `gr-zavallya-mijn`
  ──(b1 truck · Balta–Podilsk–Artsyz–Bolhrad · hemelsbreed 334,0 km, geen wegkm)──►
Reni-Donauhaven `gr-reni-haven`
  ──(b2 binnenvaart · Donau-Sulina-route + Zwarte Zee-kust, maak_rivierbeen.py · 226,3 km [eigen meting])──►
Constanța-haven, Roemenië `gr-constanta-kade` ⏹ stoppunt (fase D vervalt — geen bron voor de Europese
  eindafnemer)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-zavallya-mijn` → `gr-reni-haven` | regionale weg Kirovohrad-oblast → Balta → Podilsk → Artsyz → Bolhrad (Odesa-oblast/Budjak-regio) | hemelsbreed 334,0 (kop-staart), via-punten-som 367,9 km; **geen wegkm** — bron noemt alleen "road, rail, river, sea freight" zonder specifieke lijn [2] | maak_stroombeen_weg (extract `oekraine`) | nee |
| b2 | B | binnenvaart | `gr-reni-haven` → `gr-constanta-kade` | Donau (Kiliazijtak) → Sulina-doorvaart → Zwarte Zee-kust naar Constanța | 226,3 km [eigen meting, `maak_rivierbeen.py`-testrun, zie §7] | maak_rivierbeen (bulklaag) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-zavallya-mijn` | mijn/fabriek | Zavallya-mijn/fabriek (Zavalievsky Graphite / Volt Resources), Kirovohrad Oblast — **letterlijk hergebruikt uit de grafiet-sitelaag (`w-zavallya`)** | 48,2167, 30,0199 | sitelaag `v2/design/grafiet-sitelaag.json` (`w-zavallya`) | **bron-gelegd** (hergebruikt, reeds satellietgelegd in de sitelaag-ronde: "kruis bij het dorp Zavallya, direct N van de zichtbare, deels met water gevulde open pit"; niet opnieuw gecheckt — zie §7) |
| `gr-reni-haven` | overslag truck → binnenvaart | Reni-Donauhaven (Ренійський морський торговельний порт) | 45,4586, 28,2814 | [toets] geteste routecoördinaat (bindende haalbaarheidstoets), eigen satellietblik | **aannemelijk** (z15 gezien, dit onderzoeksbudget, prefix `grafiet-zavallya-constanta-reni-haven`: bebouwd gebied direct aan de Donau-oever in de kern van Reni, met bootjes op de rivier zichtbaar; het OSM-havenbekken (`ДП "Ренійський морський торговельний порт"`) ligt ~1,3 km zuidelijker — geen scherp afgebakende kade op deze resolutie te onderscheiden, zie §7) |
| `gr-constanta-kade` | overslag binnenvaart → stoppunt | Constanța-haven, Roemenië | 44,1733, 28,6383 | [7] Wikipedia "Port of Constanța" (exacte coördinaatmatch), [toets] | **bron-gelegd** (z15 gezien, prefix `grafiet-zavallya-constanta-constanta-kade`: gelegen op de rand van de haven-industriezone — tankopslag/olieterminal direct ten zuiden, containerterminal met kranen en kademuren ~0,7–0,9 km zuidoostelijk zichtbaar; het punt zelf ligt in het stedelijk/havenadministratief gebied bij de historische kern, niet op een specifieke kade — zie §7) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Balta | 47,9400, 29,6219 | de corridor blijft hier op de zuidwaartse as; sluit een oostelijke omweg via Pervomaisk/Voznesensk (Mykolaiv-oblast) uit |
| b1 | 2 | Podilsk | 47,7419, 29,5350 | doorgaande route zuidwaarts; sluit een afbuiging naar Odesa-stad uit |
| b1 | 3 | Artsyz | 45,9944, 29,4322 | route komt de Budjak-regio binnen; knoop richting de Bolhrad–Reni-as i.p.v. verder oostwaarts naar Izmail |
| b1 | 4 | Bolhrad | 45,6672, 28,6128 | laatste knoop vóór Reni; sluit de alternatieve bestemming Izmail uit (Izmail ligt ~30 km oostelijker, buiten deze keten — zie §7 van het ketenontwerp) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Zavallya-fabriek (verwerking) | Zavalievsky Graphite (Volt Resources 70%) | eigen Oekraïens erts + geïmporteerd Afrikaans vlokerts → battery-grade grafietconcentraat/-poeder | nominaal 20 kt/j, werkelijk sterk wisselend (maart 2026: 19,14 t/campagne; juli 2026-target ~1.200 t) | sitelaag `w-zavallya`, [1][6] |

## 6 · Stoppunt
De brief stopt bij Constanța: fase D (Europese eindafnemer) is niet gebrond — de Europese batterijklant uit de
maart 2026-verkoop en de juli 2026-contracten worden in geen enkele bron met naam genoemd, en "onward European
distribution" ná Constanța is nergens gedocumenteerd. Fase E vervalt.

## 7 · Open punten
- **BINDEND VERWERKT (haalbaarheidstoets):** been B krijgt modaliteit **binnenvaart** (niet zee/MARNET) via
  `maak_rivierbeen.py` over de bulklaag — MARNET's zeenet reikt niet tot de Donau-delta (Izmail-zeeknoop op
  132,1 km, Reni op 147,2 km, zelfs Sulina op 121,3 km van de dichtstbijzijnde zeeknoop, eigen meting). Een
  testrun Reni→Constanța-kade slaagde meteen op 226,3 km over 30 edges (snap 3,83 km / 8,30 km) — vlak bij de
  "hemelsbreed ~230 km"-schatting uit het ketenontwerp.
- **BINDEND VERWERKT (haalbaarheidstoets):** **Reni** gekozen i.p.v. Izmail als vertrekhaven — een gelijke
  testrun Izmail→Constanța gaf 298,6 km, duidelijk verder van de hemelsbrede schatting af dan Reni's 226,3 km.
- **BINDEND VERWERKT (haalbaarheidstoets):** Constanța-haven zelf ligt op 4,35 km van de dichtstbijzijnde
  MARNET-zeeknoop — geen haven-aanloop nodig aan het Constanța-eind (LAR-586: drempel > 5 km).
- **BINDEND VERWERKT (haalbaarheidstoets):** het extract `roemenie` is niet nodig — er ligt geen wegbeen op
  Roemeens grondgebied (been B eindigt zelf op de kade als binnenvaartbeen); alleen `oekraine` is nodig voor
  been A.
- **CORRECTIE OP HET KETENONTWERP:** het ontwerp noemt voor been A "hemelsbreed ~220 km, geen wegkm" — eigen
  meting van de kop-staart-grootcirkel (Zavallya 48,2167/30,0199 → Reni 45,4586/28,2814) geeft **334,0 km**,
  substantieel meer. De via-punten-som (Balta–Podilsk–Artsyz–Bolhrad) komt op 367,9 km. Geen gepubliceerde
  wegkilometer gevonden binnen het webbudget; de ±15%-toets geldt daarom als indicatie, niet als norm.
- **Via-punten b1 zijn indicatief** (bekende steden op de aannemelijke corridor, uit Wikipedia-coördinaten),
  niet zelf OSM-wegvertex-geverifieerd binnen het webbudget — de bak-agent routeert over het echte OSM-wegnet
  (extract `oekraine`) en kan afwijken; het gat Podilsk→Artsyz (191,7 km) heeft geen tussenliggend via-punt
  omdat er geen aanwijsbare corridorkeuze op dat traject is gevonden.
- **`gr-reni-haven`-anker is site-niveau, status aannemelijk, niet bron-gelegd** — de geteste routecoördinaat
  (45,4586/28,2814, uit de haalbaarheidstoets) ligt op satelliet in bebouwd gebied aan de Donau-oever, maar het
  OSM-havenbekken (`ДП "Ренійський морський торговельний порт"`, landuse=industrial) centreert ~1,3 km
  zuidelijker (45,4263/28,2926); de spoorhalte "Рені-Порт" ligt op 45,4420/28,2866, eveneens zuidelijker. Reni
  is een kleine rivierhaven met een langgerekte oeverzone — het gekozen punt kan bij het bakken alsnog
  verschuiven naar het daadwerkelijke havenbekken zonder de gemeten 226,3 km/routing wezenlijk te veranderen.
- **`gr-constanta-kade`-anker is de algemene Wikipedia-havencoördinaat, geen specifieke kade** — satellietblik
  toont het punt in het stedelijk/havenadministratief gebied nabij de historische kern (Ovidiu-plein-regio),
  niet direct op een aanlegsteiger; de echte container-/bulkterminals liggen ~0,7–0,9 km zuidoostelijk. Voor
  deze lichte werkwijze (site-niveau) acceptabel, maar minder scherp dan de andere lichte brieven.
- **Oorlogsrisico op de corridor** (drones/mijnen in Kirovohrad/Odesa-oblast) is in geen enkele bron
  gekwantificeerd; het ontwerp noemt dit risico zonder cijfers, en dat blijft zo.
- **De juli 2026-campagne verwerkt niet per se eigen Oekraïens erts** — net als de maart 2026-verkoop kan de
  feedstock (deels) geïmporteerd Afrikaans vlokerts zijn; geen bron specificeert de ertsherkomst voor de
  juli-campagne apart. De keten is daarmee eerder een **verwerkingsknoop** dan een pure winningsketen, zoals het
  ontwerp al signaleerde.
- Geen bron noemt de Europese eindafnemer(s) met naam — fase D vervalt bewust (§6).

## 8 · Bronnen
[1] Euromaidan Press, 2026-03-19 — "Ukraine's graphite plant proves Western supply chains can bypass China": 19,14 t battery-grade grafiet maart 2026, 87% yield, geïmporteerd Afrikaans erts, volledig verkocht aan één Europese batterijklant à US$3.000/t. https://euromaidanpress.com/2026/03/19/ukraine-zavalievsky-graphite-restarts-african-ore/
[2] Volt Resources Limited — "Zavalievsky Graphite Operation": locatie, 70%-eigendomsaandeel Volt Resources, nominale capaciteit ~7,3 kt/j gemiddeld 2017-2021 (piek jaren '80 60 kt/j), "excellent transport infrastructure covering road, rail, river, and sea freight", strategie levering aan Europese/Noord-Amerikaanse batterijcelmakers. https://voltresources.com/assets/zavalievsky-graphite/
[3] GMK Center, 2026 — "Danube ports: how to save an important logistics route": Izmail 13,4 Mt (2024), Reni 3,4 Mt, Ust-Dunaysk 0,5 Mt; ondiepte en beperkt spoor als knelpunten; geen grafietvermelding. https://gmk.center/en/posts/danube-ports-how-to-save-an-important-logistics-route/
[4] Container News, 2026 — "Danube River Maintains Ukraine's Container Operations": Izmail/Reni als Donau-havens die exportvolumes handhaafden tijdens de oorlog; Donau→Constanța-route als alternatief voor de Zwarte Zee-havens. https://container-news.com/danube-river-maintains-ukraines-container-operations/
[5] Wikipedia, "Reni, Ukraine" / "Reni Commercial Seaport": Reni-haven aan de linkeroever van de Donau, beschadigd door de Russische invasie van 2022; coördinaat 45,42083/28,29028. https://en.wikipedia.org/wiki/Reni,_Ukraine
[6] Kalkine Media, 2026-07-16 — "Zavalievsky Graphite Launches July 2026 Production Campaign on Back of €377,140 in European Customer Orders": doeltarget ~1.200 t grafietconcentraat (80-94% TGC), ~660 t gecontracteerd aan Europese klanten (~€377.140), leveringen juli–nov. 2026 op prepayment. https://kalkine.com.au/news/announcements/zavalievsky-graphite-launches-july-2026-production-campaign-on-back-of-377140-in-european-customer-orders
[7] Wikipedia, "Port of Constanța": ligging Constanța, Roemenië, 85 nmi van de Sulina-doorvaart van de Donau; coördinaat 44,17333/28,63833 (identiek aan het gebruikte anker). https://en.wikipedia.org/wiki/Port_of_Constan%C8%9Ba
[8] Wikipedia, "Port of Izmail": vergelijkingscoördinaat 45,33911/28,79736, gebruikt in de haalbaarheidstoets om Reni vs. Izmail als vertrekhaven te vergelijken. https://en.wikipedia.org/wiki/Port_of_Izmail
[toets] Bindende haalbaarheidstoets 2026-09-28 (keten-id `grafiet-zavallya-constanta`): MARNET-zeeknoop-afstanden, testruns `maak_rivierbeen.py` Reni/Izmail → Constanța, aanpassing modaliteit been B naar binnenvaart, Roemenië-extract vervalt.
[sitelaag] `v2/design/grafiet-sitelaag.json` (`w-zavallya`, bron-gelegd, satellietblik reeds gedaan in de sitelaag-ronde) — letterlijk hergebruikt anker.
[osm] OpenStreetMap (ODbL) via Nominatim — Reni-Port spoorhalte 45,44204/28,28660 · Ренійський морський торговельний порт (industrial) 45,42626/28,29258. https://www.openstreetmap.org
Satellietblik: `v2/build-cache/satcheck/sat-grafiet-zavallya-constanta-reni-haven.png`,
`sat-grafiet-zavallya-constanta-constanta-kade.png` (Esri z15, 2026-09-28).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Benen (gemeten):**
| # | modaliteit | km | markers | recept |
|---|---|---|---|---|
| b1 | truck | 536,7 | 2 (kop+staart) | `maak_stroombeen_weg.py --profiel grafiet-zavallya-constanta-zavallya-reni --bron geofabrik` (extract `oekraine`) |
| b2 | binnenvaart | 226,2 | 2 (kop+staart) | `maak_rivierbeen.py --marnet v2/build-cache/marnet-preais --van 45.4586,28.2814 --naar 44.1733,28.6383` (bulklaag) |
| **totaal** | | **762,9** | **3 markers** | `bash v2/tools/bak_stromen.sh grafiet-zavallya-constanta` |

Bestand `v2/data/stroomroute-grafiet-zavallya-constanta.json`, 113,6 KB, versie 2, `punt_formaat: lonlat`,
modaliteiten `{truck, binnenvaart}` — beide toegestaan, elk been ≥ 2 punten.

**Toelichting per afwijking:**
- **b1 (truck) ligt ver boven de via-punten-som/hemelsbreed uit het ontwerp** (536,7 km gemeten tegen
  367,9 km via-punten-som / 334,0 km hemelsbreed uit §7 — omwegfactor ≈ 1,46 t.o.v. de via-punten-som).
  **Geen bevinding buiten norm**: dit stroomontwerp zegt zelf dat de ±15%-toets hier **indicatief** is, geen
  harde norm (geen gepubliceerde wegkilometer — bron [2] noemt alleen "road, rail, river, and sea freight"
  zonder specifieke lijn). Alle via-snaps bleven ≤ 1,27 km (Zavallya 0,07 · Balta 0,08 · Podilsk 0,17 ·
  Artsyz 0,91 · Bolhrad 1,27 · Reni 0,03 km) — dus geen wegklasse-fout op een via-punt. Het langste
  deelstuk (Podilsk→Artsyz, gemeten 275,6 km tegen een hemelsbrede afstand van 191,7 km, brief §7) heeft
  geen tussenliggend via-punt, exact zoals de brief al meldde ("geen aanwijsbare corridorkeuze op dat
  traject binnen het webbudget"); de gemeten lijn blijft binnen de verwachte bounding box
  (lon 28,28–30,27 / lat 45,30–48,22) — geen sluipweg via een andere regio, dus het is een reële OSM-
  routegeometrie in oorlogsgebied, geen meetfout. `keerlussen gesnoeid: 17` (0,7 km, normale ruis).
  `toets_knikken.py`: 30 knikken ≥ 60° op b1, **0 omkeringen ≥ 150°, 0 terugloop** — allemaal kleine-radius
  OSM-spikes (R 3–149 m), geen rijdbaarheidsprobleem. `toets_rechte_benen.py --min-km 5`: geen van beide
  benen verschijnt in de verdachtenlijst (omwegfactor niet 1,000 op beide — reële geometrie, geen stippel nodig).
- **b2 (binnenvaart) is exact de bindende haalbaarheidstoets-testrun**: 226,2 km over 30 edges (brief noemde
  226,3 km — 0,1 km afronding), snap Reni 3,83 km / Constanța 8,30 km, identiek aan §7[toets]. Geen
  haven-aanloop: MARNET's zeenet reikt niet tot de Donau-delta (dit been is binnenvaart, geen zee) en
  Constanța ligt zelf al binnen 5 km van de MARNET-zeeknoop (LAR-586 is hier sowieso niet van toepassing,
  want dit been eindigt niet op een zeebeen). De bulklaag-router gaf meteen een pad — geen "geen pad", dus
  geen stippel-terugval nodig.
- **Naad tussen b1 en b2**: 3,83 km (eind b1 = Reni-marker exact; begin b2 = het bulklaag-anker-snap-punt
  op 3,83 km daarvandaan) — binnen de 5 km-norm van bakhandleiding §5, geen haven-aanloop of herbake nodig.
- **Marker Constanța-kade ligt 8,30 km van het eindpunt van b2** (de bulklaag-router snapt op knoop 43128,
  8,30 km van het Wikipedia-havenanker) — dit is een **anker ≠ routeerpunt**-geval, al voorzien in de brief
  (§7[toets]: "dit zijn ANKER-snaps op de bulklaag, geen aparte haven-aanloop nodig"). De bulklaag heeft een
  grovere knoopdichtheid dan het zeenet; dichttrekken zou de Waalhaven-klasse zijn. Blijft bewust staan.
- **Extract `roemenie` niet gebruikt** (bindend uit de haalbaarheidstoets, §7): been B eindigt zelf op de
  kade als binnenvaartbeen, geen wegbeen op Roemeens grondgebied.
- **`gr-reni-haven` blijft status aannemelijk (niet bron-gelegd)**, zoals al in §3/§7 vermeld — niet
  opnieuw gecheckt tijdens het bakken; het gebakken been sluit op het exacte markerpunt aan (naad 0,00 km
  aan de b1-kant).

**Lessen:**
- Een lang wegbeen zonder gepubliceerde referentie-km en zonder via-punt over een groot deeltraject (hier
  191,7 km hemelsbreed zonder tussenpunt) kan met een reëel, niet-verzonnen OSM-tracé toch 40-50% boven de
  via-punten-som uitkomen — de brief had dit al voorzien door de ±15%-toets hier expliciet als indicatie te
  labelen in plaats van norm, wat precies het juiste besluit bleek.
- De bulklaag-snap-afstand (hier 3,83/8,30 km) is een eigenschap van de knoopdichtheid van
  `marnet-preais`'s bulklaag, niet van de kwaliteit van het anker — de brief onderkende dat vooraf, wat een
  onnodige "geen pad"-terugval of herbake voorkwam.

**Registerregel voor de orkestrator:** `{ sleutel: "gr-zc", bestand: "stroomroute-grafiet-zavallya-constanta.json", grondstof: "grafiet", aan: true }`
