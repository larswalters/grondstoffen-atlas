# Routebrief (licht) · olie — Van → Via → Naar (land)

**stroom-id:** `olie-tengiz-novorossiysk` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** Kazachse CPC Blend-ruwe olie vanaf het Tengiz-productiecomplex (Tengizchevroil), via de
**CPC-hoofdleiding** (Caspian Pipeline Consortium, ~1.510 km, Atyrau/PS-1 → Kropotkin/PS-2 → Zwarte Zee) naar het
CPC Marine Terminal bij Yuzhnaya Ozereyevka, Novorossiysk — de "CPC-bypass" van Hormuz/de Golf voor Kazachstans olie.
**Welke as van het verhaal:** *Kazachstan landlocked* — een pijpleiding als enige exportader: ~1.200–1.300 kb/d
CPC Blend (peiljaar 2021–2022), **~80% van Kazachstans totale olieproductie** door één leiding [1][2]. Geen vaste
eindafnemer: CPC Blend wordt breed verkocht (ook naar Europa) — stoppunt bij de exportterminal, zoals bij Corpus
Christi→Rotterdam en Habshan→Chiba.

## 1 · Ketenkaart
```
Tengiz-productiecomplex `ol-tengiz-kop` ──(b1 leiding · CPC-hoofdleiding (Caspian Pipeline
    Consortium), via Atyrau/PS-1 → Kalmykia → Stavropol Krai → Krasnodar Krai · ~1.510 km
    gepubliceerd, doorgetrokken op OSM-geometrie)──►
   CPC Marine Terminal `ol-novo-terminal` (Yuzhnaya Ozereyevka, Zwarte Zee-kust) ── stoppunt
   (haven-aanloop over water naar de MARNET-zeeknoop, zie §9)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Tengiz-productiecomplex → CPC Marine Terminal | CPC-hoofdleiding ("Нефтепровод Тенгиз — Новороссийск"), via Atyrau/PS-1, Kalmykia, Stavropol Krai, Krasnodar Krai/Kropotkin-PS-2 | 1.510 km (diameter 1.016–1.067 mm, vijf pompstations) [2]; ontwerp noemt ~1.511 km [ontwerp] | OSM-way(s) `man_made=pipeline`, `name~"Тенгиз - Новороссийск"`/`operator="Каспийский Трубопроводный Консорциум"`/`name=CPC` — pyosmium-scan op de lokale pbf's (kazachstan + rusland-zuid), **43 + 16 matchende ways**, doorlopende keten van kop tot terminalcluster (zie §9) | nee — goede OSM-dekking bevestigd vóór het bouwen (bindende haalbaarheidstoets); geen splitsing bij de grens nodig |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-tengiz-kop` | kop van de leiding / productiecomplex | Tengiz-productiecomplex (Tengizchevroil), Atyrau-oblast | 46.1778, 53.4224 | [3][5][7] | bron-gelegd (z15 gezien: kruispunt van de pijplijn-/wegcorridor met een tank-/pompstationcomplex — bolvormige + cilindrische tanks, procesinstallatie en gebouwen, direct naast de bredere TCO-productiestrook net ten zuiden) |
| `ol-novo-terminal` | overslag leiding → zee (exportterminal, CPC-terminus) | CPC Marine Terminal (onshore tankenpark), Yuzhnaya Ozereyevka, Novorossiysk | 44.6705, 37.6533 | [1][4][5][7] | bron-gelegd (z15 gezien: klein gebouwen-/tankencomplex direct aan de kust met een steiger/pier de zee in — het convergentiepunt van drie CPC-pijplijntakken uit de OSM-data, ~2 km zuidoost van het dorp Yuzhnaya Ozereyevka) |

## 4 · Via-punten (b1 — OSM-waysegmentgrenzen langs de leiding, geen alternatieve corridor)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Тенгиз–Атырау-segmentgrens | 46.3392, 53.4657 | eindpunt CPC-operator-way vanaf de kop, aansluiting op het "Тенгиз - Атырау"-segment [7] |
| b1 | 2 | Atyrau / PS-1 | 47.1683, 51.8731 | pompstation-knoop bij Atyrau, begin van het lange "Атырау - Новороссийск"-segment (in beide extracts identiek) [7] |
| b1 | 3 | KZ/RU-grensnadering | 46.8456, 48.5926 | laatste gedeelde waysegmentgrens vóór de landsgrens, way `312553138` loopt ongewijzigd door in de Rusland-extract [7] |
| b1 | 4 | Kalmykia-knoop | 45.5539, 46.6180 | vertakkingspunt in de OSM-tagging waar de CPC-operator-taggedways doorlopen richting Stavropol [7] |
| b1 | 5 | Stavropol Krai-doorsnede | 45.5504, 41.7664 | opeenvolgende segmentgrenzen door Stavropol Krai, corridor blijft zuidwestwaarts richting Krasnodar [7] |
| b1 | 6 | nadering Krasnodar Krai (CPC-naam) | 45.2584, 38.8770 | begin van de expliciet `name="CPC"`-getagde slotsegmenten richting de terminal [7] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| CPC Marine Terminal | Caspian Pipeline Consortium (CPC-R) | pijplijn-CPC Blend → tankopslag (4× 100.000 m³) → twee single point moorings | doorvoer ~1.200 kb/d (peiljaar 2022, ~1,2% van de wereldvraag) [2] | [1][2][4] |

## 6 · Stoppunt
De brief stopt bij het CPC Marine Terminal: CPC Blend heeft geen gedocumenteerde vaste eindafnemer — de ruwe olie
wordt breed verkocht via de spotmarkt (ook naar Europa, o.a. ExxonMobil-charters zoals de Nordic Zenith [2]). Fase
D/E vervallen; zelfde stoppunt-logica als Corpus Christi→Rotterdam en Habshan→Chiba.

## 7 · Open punten
- **Niet elk tussenliggend waysegment is individueel geverifieerd** — de pyosmium-scan vond 43 (Kazachstan) + 16
  (Rusland-Zuid) matchende ways met grotendeels aansluitende eindpunten; enkele naden tussen genoemde ways zijn niet
  met een exacte coördinaat gedekt (mogelijk ongenoemde tussensegmenten die niet op de trefwoorden matchten). Bij het
  bakken kan dit een klein aantal korte stippel-stukjes opleveren; geen reden om de hele as als stippel te behandelen
  (haalbaarheidstoets: dekking is ruim voldoende).
- **Novorossiysk-2/CPC-kade lag niet in de hergebruiklijst** en is dit keer zelf gelegd (zie §3); geen conflict met
  bestaande ankers uit andere brieven gevonden.
- **Risico bijgewerkt t.o.v. het ontwerp:** naast de eerdere drone-aanvallen (17-02-2025 pompstation, 30-40%
  doorvoerverlies; 29-11 meerpuntbeschadiging) trof op **17-07-2026** een dubbele droneaanval de tanker *Nordic
  Zenith* (ExxonMobil-charter) bij nadering van Novorossiysk/de CPC-kade, onderdeel van de Oekraïense campagne
  *Operation MoLoChKa* tegen de (Russische) schaduwvloot — ondanks dat het schip neutraal/westers eigendom was [2].
  Dit maakt het tracé politiek kwetsbaarder dan het ontwerp aangaf.
- **Haven-aanloop nodig:** de CPC-terminal ligt 16,6 km van de dichtstbijzijnde MARNET-zeeknoop (binnen de 25 km-
  snapgrens, maar > 5 km) → volgens bakhandleiding §2 (LAR-586, 2026-09-28) komt er een haven-aanloop tussen kade en
  zeeknoop, ook al snapt de router zelf al. Geen vervolgbeen na de terminal (§6).
- **Jaarvolume-eenheid:** kb/d (duizend vaten per dag) is de brongegeven eenheid; zie volume-notitie hieronder.

*Volume-notitie:* ~1.200–1.300 kb/d CPC Blend (peiljaar 2021–2022, ~80% van Kazachstans totale olieproductie van
~1.600 kb/d) [1][2]. Bij ~7,3 vaten/ton voor lichte zure ruwe olie ≈ **~60–65 Mt/j** (oorspronkelijke eenheid: kb/d).

## 8 · Bronnen
[1] cpc.ru — Caspian Pipeline Consortium, officiële site (Tengiz→Novorossiysk-2-tracébeschrijving). https://www.cpc.ru/en/pages/home.aspx
[2] Wikipedia, "Caspian Pipeline Consortium" (bijgewerkt 2026-09-11) — lengte 1.510 km, diameter 1.016–1.067 mm, vijf
pompstations, capaciteit tot 1,4 mln vpd/72,5 Mt/j (BEP), doorvoer ~1,2 mln vpd (2022, ~1,2% wereldvraag), 80% van
Kazachse productie (2021), aanvalsgeschiedenis t/m 17-07-2026 (Nordic Zenith, Operation MoLoChKa). https://en.wikipedia.org/wiki/Caspian_Pipeline_Consortium
[3] Wikipedia, "Tengiz Field" — coördinaat 46,15278/53,38333, ADNOC/Chevron/ExxonMobil-productiecomplex Atyrau-oblast. https://en.wikipedia.org/wiki/Tengiz_Field
[4] OpenStreetMap/Nominatim (ODbL) — "Южная Озереевка" (Yuzhnaya Ozereyevka), 44,6828/37,6304, dorpscentroïde (geen anker — het terminalanker ligt ~2 km zuidoost, zie §3). https://www.openstreetmap.org
[5] OpenStreetMap/Nominatim (ODbL) — "TengizChevrOil" POI 46,21053/53,37588 en "Tengizchevroil 3GP Future Growth
Project power station" landuse-vlak 46,1338/53,3753, bevestigt het productiecomplex in de omgeving van het gekozen
pijplijnkop-anker. https://www.openstreetmap.org
[6] EIA — "Kazakhstan" country analysis, olie-exportroutes en CPC-aandeel. https://www.eia.gov/international/analysis/country/KAZ
[7] OpenStreetMap (ODbL) — eigen pyosmium-scan (2026-09-28) op de lokale Geofabrik-extracts `kazachstan` en
`rusland-zuid`: 43 resp. 16 ways `man_made=pipeline` met `name`/`operator` ~ CPC/Caspian/Тенгиз/Кропоткин/
Новороссийск, waaronder `way/325152542` ("Тенгиз - Новороссийск (Тенгиз - Атырау)"), `way/312553138` ("Тенгиз -
Новороссийск (Атырау - Новороссийск)", gedeeld in beide extracts), `way/319604608`/`802869198-201` (`name=CPC`,
slotsegmenten bij de terminal). https://www.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `sat-olie-tengiz-novorossiysk-tengiz-kop.png`,
`sat-olie-tengiz-novorossiysk-novo-terminal.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `olie-tengiz-novorossiysk`** → `v2/data/stroomroute-olie-tengiz-novorossiysk.json` — 4 benen, **1.533,6 km**, 1.193 punten, 2 markers (2 stippel-benen).
Recept: `bak_stromen.sh` (functie `bak_olie_tengiz_novorossiysk`).

**b1 (leiding, been-geojson, segment 1):** eigen pyosmium-scan (geen Overpass) op de lokale pbf's `kazachstan` +
`rusland-zuid`, filter `man_made=pipeline` + naam/operator ~ cpc|caspian|тенгиз|новоросс|кропотк — 5 target-ways in
kazachstan (waarvan `way/312553138` identiek gedeeld met rusland-zuid), 16 in rusland-zuid. Dertien ways in
reisvolgorde gestikt (`way/1089847876`→`325152542` (reversed)→`312553138`→`274735475`→`274735097`→`319494061`→
`319494072`→`319494070`) — **alle acht naden tussen opeenvolgende ways exact 0,000 km** (gedeelde OSM-nodes). Bij de
Kalmykia-knoop (45,5539/46,6180) bestaan twee parallelle/alternatief getagde takken; `319494061/072/070` gekozen
boven `274735428/295` (dat laatste stuk eindigt op 43,7243/45,0901, een naad van 332 km naar het volgende via-punt
tegen 105 km voor de gekozen tak — kleinste eindpunt-naad, conform de bak-aanwijzing). Tengiz-kop (46,17784/53,42240)
→ laatste gedeelde punt vóór het kaarteringsgat (45,68062/43,10336), **1.044,2 km**, 734 punten.

**b1-gat (leiding, stippel):** `--stippel "leiding|…, schematisch — OSM-kaarteringsgat ~105 km in Stavropol Krai
(geen bruggende pipeline-way gevonden, brede scan zonder naamfilter)|45.6806,43.1034|45.5504,41.7664"` —
**104,992 km**, rechte lijn. Dit is géén "enkele km"-naad tussen twee segmentgrenzen zoals de bakhandleiding als
voorbeeld noemt, maar een écht OSM-kaarteringsgat: een bredere scan zonder naamfilter (alle `man_made=pipeline`-ways
binnen 60 km van beide uiteinden, alle substances) vond geen enkele bruggende oliepijplijn, alleen twee ongerelateerde
gasleidingen (`way/310701799`, `way/310714135`, beide `subst=gas`, respectievelijk 52,2 en 14,1 km weg). Niet
dichtgetrokken — het tracé zelf klopt (zie de totaaltoets hieronder), alleen de kartering ontbreekt hier op dit stuk
Stavropol Krai.

**b1 (leiding, been-geojson, segment 2):** ways `319565265`→`274735372`→`802732764`→`319604608`→`802869201`, van de
hervatting na het gat (45,55040/41,76640) tot 44,67067/37,65327 — dit laatste punt ligt **~22 m** van het
terminalanker `ol-novo-terminal` (44,6705/37,6533); de drie korte slottakken naar de losse mooring-aansluitingen
(`way/802869198/199/200`) zijn niet nodig voor de hoofdlijn. **365,2 km**, 420 punten.

⚠️ **Lengtetoets b1 (leiding, drie stukken samen, incl. het gat):** 1.044,2 + 104,992 + 365,2 = **1.514,4 km** tegen
gepubliceerd **1.510 km** (Wikipedia CPC) = **+0,3%**, ruim binnen ±15% — het tracé zelf klopt vrijwel exact,
ondanks het kaarteringsgat.

**b2 (zee, haven-aanloop, stippel-geojson):** CPC Marine Terminal (44,6705/37,6533) ligt 16,6 km van MARNET-zeeknoop
2060 (44,58970/37,82950) — binnen de 25 km-snapgrens maar > 5 km → per bakhandleiding §2 (LAR-586, 2026-09-28) komt
er een haven-aanloop, óók al snapt de router zelf. `maak_havenaanloop.py`: **19,2 km** over water, 37 punten,
omwegfactor 1,155; 0,80 km "over land" grenst aan het kade-uiteinde (de 1:10M-kustkorrel, geen fout). Geen
vervolgbeen ná de terminal (§6 — CPC Blend heeft geen vaste eindafnemer) — de haven-aanloop is het laatste stuk van
de stroom, geen naad ná dit been.

**Naden tussen alle vier de benen:** 0,00 · 0,00 · 0,00 · 0,02 km — geen enkele > 5 km (buiten de bewust gestippelde
105 km binnen b1, die als zodanig benoemd en beargumenteerd blijft staan).

**Toets (`toets_knikken.py`):** 28 knikken ≥ 60° over beide leiding-segmenten (spikes en krappe bochten op
pompstation-/junctieknopen — normaal voor pijplijn-OSM-geometrie, zoals bij de andere olie-brieven), **1 omkering
≥ 150°** (156,0° bij 44,95394/37,93501, "scherpe bocht, echt" — v=1,1, geen terugloop), **0 terugloop** (de enige
klasse die gerepareerd hoort te worden). `toets_rechte_benen.py --min-km 5`: alleen de 105 km-stippel gemarkeerd
(omwegfactor 1,000, verwacht en beargumenteerd — een rechte lijn met reden), geen andere gemeten been eronder.

**Contract:** `json.load` slaagt, `versie` 2, `punt_formaat` `lonlat`, modaliteiten `{leiding, zee}` ⊂ toegestane
set, elk been ≥ 2 punten, bestand **24,4 KB**.

**Gereedschapslessen:**
- **Twee parallelle OSM-tagvarianten bij dezelfde knoop** kies je op kleinste eindpunt-naad naar het volgende
  via-punt, niet op willekeur of way-volgorde — een tak van 105 km naad wint duidelijk van een tak van 332 km.
- **Een écht OSM-kaarteringsgat van >100 km is géén reden om de hele as als stippel te behandelen** — de gemeten
  stukken aan weerszijden bevestigen het tracé (totaal +0,3% t.o.v. gepubliceerd), dus alleen het ontbrekende stuk
  wordt gestippeld, met een expliciete brede-scanverificatie dat er geen bruggende way over het hoofd is gezien.
- **`--stippel`-coördinaten zijn `lat,lon`**, net als overal in dit project — een pyosmium-scan die intern
  `(lon,lat)`-tuples gebruikt (het GeoJSON-formaat) kan bij het overtypen naar een `--stippel`-argument per ongeluk
  omgedraaid worden; de bake-console-uitvoer (die de afstand herberekent) ving dat meteen (149,1 km i.p.v. de
  verwachte ~105 km) — controleer de gerapporteerde stippel-km altijd tegen de eigen berekening vóórdat je verder gaat.
- Een `man_made=pipeline`-way die al ~22 m van het terminalanker eindigt hoeft niet met een extra korte slottak
  verlengd te worden — de laatste segmentgrens ís in de praktijk vaak al het anker.
