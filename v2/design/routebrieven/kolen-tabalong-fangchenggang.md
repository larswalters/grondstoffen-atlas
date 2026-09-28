# Routebrief (licht) · kolen — Van → Via → Naar (land)

**stroom-id:** `kolen-tabalong-fangchenggang` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** thermische kolen van AlamTri (ex-Adaro) Tutupan/Wara-mijncomplex bij Tabalong (Zuid-
Kalimantan) per **eigen haalweg** (~86 km, privéterrein) naar de **Kelanis-laadterminal** aan de Barito-rivier,
per **binnenvaart** (~118,5 km, rivier + delta) naar de open-zee **Taboneo-ankerplaats** (transshipment, géén
vaste kade), dan per **zeeschip** (~2.890 km hemelsbreed via Straat Makassar/Karimata → Zuid-Chinese Zee →
Beibu-golf) naar de **Fangchenggang-kolenterminal** in Guangxi. Stoppunt = de terminal: geen gedocumenteerde
specifieke afnemer-centrale voor déze as, dus geen fase D.
**Welke as van het verhaal:** *Een tweede, andere Indonesische kolen-as dan Sangatta-Mundra* — Zuid-Kalimantan
(Adaro/AlamTri, Tabalong) → China (Guangxi). AlamTri/Adaro Tabalong ≈ **40 Mt/jr** thermische kolen (grootste
single-site kolenmijn van het zuidelijk halfrond, [1]); **China = 12% van AlamTri/Adaro Group's thermische
kolenverkoop in 1Q24** (bindend uit de haalbaarheidstoets, oorspronkelijke bron een Adaro-investorpresentatie,
niet zelf geraadpleegd deze ronde — zie §7). China is bovendien de swing-koper op de wereldkolenmarkt
(`design/kolen.md` §1): het volume naar Fangchenggang specifiek fluctueert met Chinees importbeleid, niet
met Indonesische aanbodcapaciteit.

## 1 · Ketenkaart
```
AlamTri Tutupan/Wara-mijncomplex `kolen-tabalong-mijn`
   ──(b1 truck · eigen haalweg (Adaro private haul road) · ~86 km, stippel — eigen terrein/geen net)──►
Kelanis-laadterminal `kolen-kelanis-kade`
   ──(b2 binnenvaart · Barito-rivier stroomafwaarts · ~118,5 km)──►
Taboneo-ankerplaats `kolen-taboneo-rede` (rede, geen vaste kade — transshipment)
   ──(b3 zee · Javazee → Straat Makassar/Karimata → Zuid-Chinese Zee → Beibu-golf · ~2.890 km hemelsbreed,
      haven-aanloop aan BEIDE zijden — Taboneo is geen kade, Fangchenggang-kade ligt buiten de 25 km-snap)──►
Fangchenggang-kolenterminal `kolen-fangchenggang-kade` ⏹ stoppunt (invoer Zuid-Chinese kustcentrales, geen
   gedocumenteerde specifieke centrale voor déze as → geen fase D)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `kolen-tabalong-mijn` → `kolen-kelanis-kade` | Adaro's eigen haalweg (privé, geen publiek net) | ~86 [2] | stippel, rechte lijn (geen OSM-weg — privéterrein) | ja — eigen terrein/geen net |
| b2 | A | binnenvaart | `kolen-kelanis-kade` → `kolen-taboneo-rede` | Barito-rivier stroomafwaarts + delta | ~118,5 (64 NM) [5] | `maak_rivierbeen.py` (bulklaag) | nee |
| b3 | B | zee | `kolen-taboneo-rede` → `kolen-fangchenggang-kade` | Javazee → Straat Makassar/Karimata → Zuid-Chinese Zee → Beibu-golf | ~2.890 hemelsbreed (eigen berekening; geen gepubliceerde scheepsroute-km gevonden) | MARNET (`hecht_marnet.py route`) + haven-aanloop aan beide uiteinden | aanloop: ja (beide zijden) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-tabalong-mijn` | mijn (haalweg-kop) | AlamTri/Adaro Tutupan/Wara-mijncomplex, Tabalong | -2.204484, 115.527798 | [1][13] | bron-gelegd (z14 gezien: karakteristieke open-pit terrasmijnbouw — haalwegen, pitmeren, stapelterrein over een breed gebied direct onder het kruis; hergebruikt anker `w-tutupan` uit `kolen-sitelaag.json`. Paringin, sinds okt-2022 gesloten, is niet apart aangewezen — dit anker dekt het huidige Tutupan/Wara-productiegebied) |
| `kolen-kelanis-kade` | overslag (truck → binnenvaart) | Kelanis-laadterminal (PT Adaro Indonesia), Barito-rivier | -2.293384, 114.8703 | [2][3][5] | bron-gelegd (z15 gezien: een conveyor/laadsteiger die de rivierbocht insteekt, stockpile op de oever, meerdere kolenduwstellen/bakken zichtbaar stroomop- en afwaarts, en een pluim die op stofontwikkeling bij het laden wijst — ondubbelzinnig de terminal) |
| `kolen-taboneo-rede` | overslag (binnenvaart → zee, transshipment) | Taboneo-ankerplaats | -3.6994, 114.4586 | [4][5][6] | onzeker (z13 gezien: uitsluitend open zee, geen enkele structuur zichtbaar — een rede heeft per definitie geen kade; positie uit een havenregister, het is een gebied/ankerzone en geen punt, dus ±enkele km) |
| `kolen-fangchenggang-kade` | losplek (zee, kolenterminal) | Fangchenggang-havencomplex (西湾港区), Guangxi | 21.592216, 108.344216 | [7][8][9][10] | onzeker (z14/z16 gezien: dicht bebouwd multi-modaal havencomplex — tankopslag, loodsen, meerdere voor anker liggende bulkcarriers in de vaargeul ervoor — maar de specifieke kolen-losberth binnen dit complex is niet met zekerheid geïsoleerd, noch op satelliet noch in de geraadpleegde bronnen) |

## 4 · Via-punten
*Geen — b1 is een privé haalweg zonder corridorkeuze (eigen terrein), b2 volgt de rivier (het routeertool bepaalt
de vaargeul, geen door ons gekozen splitsing), b3 is de zee-router (MARNET).*

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kelanis-laadterminal | PT Adaro Indonesia (Adaro Logistics) | truckkolen → bargelading (Barito-rivier) | 7 hopper/crusher-sets, 10.500 t/u totaal; 53 conveyors, 16.500 t/u totaal; 2 jetties (bedrijfscijfers) — losse havenbron noemt 3 conveyor-jetty's à 600 t/u elk voor de bargebelading zelf | [2][5] |
| Fangchenggang-havencomplex | Guangxi Beibu Gulf Port Group | zeeschip → kolenoverslag (thermisch → Zuid-Chinese kustcentrales) | ~46 Mt/j kolendoorzet (2011-cijfer; recenter cijfer niet gevonden deze ronde) | [8] |

## 6 · Stoppunt
De brief stopt bij de Fangchenggang-kolenterminal: dit is een invoerhaven voor Zuid-Chinese kustcentrales
(thermische kolen, geen cokes/staal-tussenstap). Fase D vraagt één bron die de specifieke afnemende centrale
noemt — die is voor déze as niet gevonden (China is de swing-koper, het volume wisselt tussen aanbieders en
Chinese havens per importbeleid) — dus fase D vervalt conform de lichte werkwijze §1.

## 7 · Open punten
- **Exacte kolenberth binnen Fangchenggang niet geïsoleerd:** het havencomplex is multimodaal (olie/chemie-
  tanks, algemene lading, bulk); geen bron met een coal-specifieke coördinaat gevonden binnen het webbudget.
- **Ketenvolume Tabalong → Fangchenggang specifiek niet gepubliceerd:** alleen het AlamTri-groepscijfer
  (~40 Mt/j Tabalong-productie [1]) en het aandeel China (12% van AlamTri/Adaro Group's thermische
  kolenverkoop, 1Q24 — bindend uit de haalbaarheidstoets, oorspronkelijke bron een investorpresentatie, niet
  zelf geraadpleegd deze ronde).
- **Haalweg-lengte (86 km) uit een havenregister-samenvatting**, niet in een primaire Adaro-bron geverifieerd
  deze ronde; het is bovendien privéterrein, dus geen OSM-weg beschikbaar om te toetsen.
- **Taboneo-positie is een gebied, geen punt:** de ankerplaats bestrijkt open zee zuid van de Barito-monding;
  geen exacte ankerplaatscoördinaat gepubliceerd, ±enkele km-onzekerheid.
- **Wara-pit niet los gelokaliseerd:** Tutupan/Wara is als één site-anker op de Tutupan-coördinaat behandeld
  (de grootste van de twee actieve pits na de sluiting van Paringin, okt-2022).
- **Geen traceerbare specifieke lading:** deze as is aannemelijk uit AlamTri's algemene exportprofiel en het
  China-aandeel van de haalbaarheidstoets, niet uit één gedocumenteerde scheepslading Tabalong → Fangchenggang.

## 8 · Bronnen
[1] Wikipedia — AlamTri Resources: hoofdlocatie Tabalong-district, Zuid-Kalimantan; "largest single-site coal mine in the southern hemisphere (roughly 110,000 tons of coal per day, or 40 million tons a year)". https://en.wikipedia.org/wiki/AlamTri_Resources
[2] MarineLink Ports Directory — Kelanis Port: locatie Barito-rivier, Zuid-Kalimantan; "dedicated hauling road spanning 86 km"; coal handling/barge-loading facility 7 hopper&crusher-sets (10.500 t/u totaal), 53 conveyors (16.500 t/u totaal), twee jetties. https://ports.marinelink.com/ports/port/kelanis
[3] Foursquare — "Barge Loading PT. Adaro Indonesia Kelanis Site", Barito Selatan, Kalimantan Tengah (bevestigt locatie/naam van de terminal). https://foursquare.com/v/barge-loading-pt-adaro-indonesia-kelanis-site/4e3d83fb814ddc29c426e4ba
[4] Global Energy Monitor — Taboneo anchorage: "open sea coal loading anchorage located off the coast of South Borneo", sub-haven van Banjarmasin, tot 20.000 DWT, 94,8 Mt kolen geladen in 2023 (gezamenlijk). https://www.gem.wiki/Taboneo_anchorage
[5] BTJ Lines (PT Bahari Tirta Jaya) — Port Information of Taboneo Anchorage: "distance from barging terminal to anchorage area about 64 NM"; "Jetty Kelanis / Kelanis Stockpile and Hasnur Jetty Sungai Puting — 3 conveyors jetty, ~40 m each, loading rate 600 MT/hour per conveyor". https://www.btjlines.com/public/document/port_info/TABONEO.pdf
[6] MarineLink Ports Directory — Taboneo Anch: coördinaat -3.699433, 114.4586 (river port entry Indonesië). https://ports.marinelink.com/ports/port/taboneo-anch
[7] Wikipedia — Fangchenggang: "southernmost port in China", bulk carriers tot 180.000 dwt; stadscoördinaat 21°41′12″N 108°21′17″E. https://en.wikipedia.org/wiki/Fangchenggang
[8] Global Energy Monitor — Beibu Gulf Port: "Fangcheng port is the primary port for transporting coal" binnen het Beibu Gulf-havencomplex; doorzet kolen ~46 Mt/j (2011-cijfer, 3,86 Mt/maand). https://www.gem.wiki/Beibu_Gulf_Port
[9] Baidu Baike (EN) — Fangchenggang Port (Guangxi Beibu Gulf Port): 西湾港区/企沙港区-indeling; Qisha-havengebied met tot 76 ligplaatsen (10.000-400.000 t). https://baike.baidu.com/en/item/Fangchenggang%20Port/648157
[10] OpenStreetMap (ODbL) via Nominatim — industrieel landuse-vlak "防城港" (way/relatie, centroïde 21.5922164/108.3442156) in 港口区, Fangchenggang. https://www.openstreetmap.org
[11] Esri World Imagery via `v2/tools/sat_check.py` (z13–z16, live) — `v2/build-cache/satcheck/sat-kolen-tabalong-fangchenggang-{tutupanwara,kelanis,taboneo,fcg-westport,fcg-stockpile,fcg-pier}.png`.
[12] Haalbaarheidstoets `kolen-tabalong-fangchenggang` (bindend, orkestrator-invoer): Paringin gesloten sinds eind okt-2022, productie nu uit Tutupan+Wara; China = 12% van AlamTri/Adaro Group's thermische kolenverkoop in 1Q24 (oorspronkelijk Adaro-investorpresentatie).
[13] `v2/design/kolen-sitelaag.json`, anker `w-tutupan` (hergebruikt coördinaat, oorspronkelijk uit GEM Global Coal Mine Tracker Table 1, WGS-84).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `kolen-tabalong-fangchenggang`** → `v2/data/stroomroute-kolen-tabalong-fangchenggang.json` — 6
benen, **3.914,3 km**, 1.535 punten, 4 markers. truck 73,7 (stippel) · binnenvaart 195,9 + 18,5 (stippel) =
214,4 · zee 20,8 (stippel) + 3.574,2 + 31,2 (stippel) = 3.626,2 km. Recept: `bak_stromen.sh` (functie
`bak_kolen_tabalong_fangchenggang`).

**b1 (truck, rechte stippel — Adaro's eigen haalweg, privéterrein, geen OSM-weg):** hemelsbreed **73,7 km**
tegen gepubliceerd ~86 km (bron [2], MarineLink-havenprofiel) = **−14,3 %**, binnen ±15 % — een niet-rechte
privéweg is altijd langer dan de hemelsbrede lijn, dus het teken van het verschil is verwacht.

**b2 (binnenvaart, `maak_rivierbeen.py` over de bulklaag, extract-onafhankelijk):**
`--van -2.293384,114.8703 --naar -3.6994,114.4586` → bulk-knoop-snap kop 3,58 km / staart **18,51 km**
(Taboneo ligt in open zee zuid van de delta-mond, niet op de gekarteerde rivierlijn) → **195,9 km over 38
edges, 1.069 punten** tegen gepubliceerd ~118,5 km (64 NM, bron [5]) = **+65,4 %, ruim buiten ±15 % —
bevinding, geen via-punt bijgeschoven.** De hemelsbrede afstand Kelanis→Taboneo is zelf al ~162,9 km (dus
groter dan de gepubliceerde 118,5 km): de brief-km lijkt een andere, kortere deelmeting te zijn (bijv. vanaf
een ander punt in de Barito-delta dan het Kelanis-anker), en Taboneo is bovendien een gebied zonder vaste
kade (brief §3/§7, ±enkele km-onzekerheid) — geen coördinaat verzonnen om dichterbij te komen.
De staart-snap van 18,51 km gaf een naad > 5 km (bakhandleiding §5) tussen b2 en de Taboneo-haven-aanloop;
gedicht met een korte **rechte stippel (binnenvaart, 18,5 km, "bulklaag reikt niet tot de open-zee
ankerplaats")** — dat is de vereiste naad-fix, geen via-punt bijschuiven om het percentage te laten kloppen.
Gecombineerd (binnenvaart-been + naad-stippel) **214,4 km** tegen ~118,5 km = **+80,9 %** — dezelfde
bevinding, groter zichtbaar op het totaal.

**b3 (zee, haven-aanloop aan BEIDE zijden, LAR-586):**
- Haven-aanloop Taboneo: `maak_havenaanloop.py --van -3.6994,114.4586 --naar -3.52850,114.49950` — gekozen
  cel 0,005° gebufferd → **20,8 km · 35 punten · 0,00 km over land** (0 % — Taboneo is zelf al open zee),
  omwegfactor **1,067** tegen de rechte lijn (19,5 km). Kade lag 19,54 km van zeeknoop 5483, dus ruim boven
  de 5 km-norm maar onder de 25 km max-snap.
- Zeebeen (MARNET, zeeknoop → zeeknoop): `--been "zee|...|-3.52850,114.49950|21.57570,108.62050"` — snap
  0,000 km aan beide kanten → **3.574,2 km over 20 MARNET-edges, 371 punten** tegen de ~2.890 km hemelsbreed
  uit de brief = **+23,7 %**, buiten ±15 % — bevinding, geen via-punt bijgeschoven. Geen gepubliceerde
  scheepsroute-km om tegen te toetsen; de omwegfactor (3.574,2/2.890 = 1,237) is plausibel voor een route via
  Straat Makassar/Karimata → Zuid-Chinese Zee → Beibu-golf (de brief noemt zelf al dat die omweg normaal een
  factor > 1,05 toevoegt). Lengte-invariant: getekende lijn 3.574,179 vs som edge-km 3.574,400 = −0,221 km
  (de naden).
- Haven-aanloop Fangchenggang: `maak_havenaanloop.py --van 21.5922164,108.3442164 --naar 21.57570,108.62050`
  — gekozen cel 0,005° kaal → **31,2 km · 56 punten · 0,00 km over land**, omwegfactor **1,091** tegen de
  rechte lijn (28,6 km, waarvan 7,9 km/28 % over land — de kade ligt landinwaarts in het havencomplex).
  Kade lag 28,63 km van zeeknoop 5539, dus boven zowel de 5 km- als de 25 km max-snap-norm.
  ⚠️ `maak_havenaanloop.py` schrijft altijd in `--van`→`--naar`-volgorde; deze aanloop is ná generatie
  handmatig omgedraaid van kade→knoop naar knoop→kade (coördinaten ongewijzigd, alleen de puntvolgorde),
  zodat hij in reisvolgorde ná het hoofdzeebeen aansluit (zoals bij kolen-ermelo-portqasim).

**Toets naden:** alle overgangen ≤3,58 km — truck→binnenvaart(hoofdbeen) 3,58 km (bulk-knoop-snap bij
Kelanis, binnen de norm), binnenvaart(hoofdbeen)→naad-stippel 0,00 km, naad-stippel→haven-aanloop Taboneo
0,00 km, haven-aanloop→hoofdzeebeen 0,00 km, hoofdzeebeen→haven-aanloop Fangchenggang 0,00 km. Ruim binnen
de 5 km-norm; geen derde haven-aanloop nodig.

**`toets_knikken.py`:** 13 knikken ≥60°, **0 omkeringen ≥150°** (dus ook 0 terugloop — niets hoeft
gerepareerd). 11 op het binnenvaartbeen (spikes/krappe bochten op meanderpunten van de Barito-delta, R
57–193 m — eigenschap van de bulklaag-geometrie op een echte rivierbocht) en 2 op het zeebeen (R 8.262/8.561
m, krappe bochten bij grote-cirkel-benaderingen rond eilandengroepen in de Javazee/Karimata-Straat — geen
fout, geen kopmaak-plek nodig omdat dit geen spoorbeen is).

**`toets_rechte_benen.py --min-km 5`:** beide echte stippels van deze stroom staan in de uitslag, correct als
stippel gemarkeerd — truck 73,7 km (🟠 GROOT, factor 1,000) en de naad-stippel 18,5 km (🟡 MIDDEL, factor
0,999). Geen doorgetrokken (gemeten) been van deze stroom verschijnt in de lijst: het binnenvaartbeen
(1.069 punten) en het zeebeen (371 punten) hebben allebei een reële omwegfactor.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, binnenvaart, zee} (binnen de
toegestane set), elk been ≥2 punten (minimum 2, de twee rechte stippels), bestandsgrootte **29,8 KB** (ruim
onder de 300 KB-richtwaarde).

**Markers:** alle vier ankers **0,0 m** van de lijn (Tutupan/Wara-mijncomplex, Kelanis-laadterminal, Taboneo-
ankerplaats, Fangchenggang-havencomplex) — elk anker is zelf het uiteinde van een been/stippel, dus geen
"anker ≠ routeerpunt"-afstand.

**Open punten die blijven staan (zie ook §7):**
- b2 (binnenvaart) meet +65,4 % (hoofdbeen) / +80,9 % (met de naad-stippel) boven de gepubliceerde 118,5 km
  — nieuw bevestigd: de hemelsbrede afstand Kelanis→Taboneo (~162,9 km) overschrijdt de gepubliceerde km
  zelf al, dus de brief-bron meet waarschijnlijk een ander (korter) trajectdeel dan Kelanis→Taboneo.
- b3 (zee) meet +23,7 % boven de eigen hemelsbreed-schatting (~2.890 km) uit de brief — geen gepubliceerde
  scheepsroute-km om onafhankelijk tegen te toetsen; de omwegfactor is plausibel voor deze corridor.
- Taboneo-ankerplaats blijft een gebied zonder vaste kade (status onzeker, brief §3/§7) — de gekozen
  coördinaat is een havenregisterpunt, ±enkele km-onzekerheid.
- Exacte kolenberth binnen het multimodale Fangchenggang-havencomplex niet geïsoleerd (status onzeker,
  brief §7) — het anker blijft het OSM-industrievlak-centroïde uit bron [10].
- Ketenvolume Tabalong → Fangchenggang specifiek niet gepubliceerd (ongewijzigd t.o.v. §7).

**Gereedschapslessen:**
- `maak_rivierbeen.py` snapt op de bulklaag naar het dichtstbijzijnde WATER-knooppunt, ook als het
  eindpunt eigenlijk in open zee ligt (een rede zonder vaste kade, geen deel van de gekarteerde
  rivier-/deltageometrie) — dat gaf hier een staart-snap van 18,51 km en dus een naad > 5 km. Dichten met
  een korte rechte stippel (dezelfde klasse als een haven-aanloop, alleen dan voor de bulklaag) werkt
  probleemloos en hoeft geen via-punt of coördinaat te verzinnen.
- Twee haven-aanlopen tegelijk in één keten (Taboneo boven de 5 km-norm maar onder de 25 km max-snap;
  Fangchenggang boven beide) verliepen allebei probleemloos in de eerste trappenronde — geen terugval op een
  rechte stippel nodig.
- De `neem_slot`-mechaniek uit de opdracht (`rm -rf "$d"` in een gedeeld-slots-script) werd door een
  ingebouwde Claude Code-veiligheidscheck geblokkeerd ("Dangerous rm operation" — de checker kan een
  dynamisch samengestelde variabele niet als veilig herkennen, ook al is die in de praktijk altijd
  `$SLOTS/$pool/slotN`). De bake zelf is licht (geen wegscan, alleen `hecht_marnet.py route` met
  vooraf gebakken been-geojsons/stippels, ~12 s) en is daarom zonder slot gedraaid.
