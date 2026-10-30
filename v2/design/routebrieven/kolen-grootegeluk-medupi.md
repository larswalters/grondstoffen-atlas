# Routebrief (licht) · kolen — Grootegeluk-wasserij → Medupi-kolenopslag (Zuid-Afrika)

**stroom-id:** `kolen-grootegeluk-medupi` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Keten in één zin:** Thermische steenkool van de Grootegeluk-mijn (Exxaro, Waterberg, Limpopo) gaat na de wasserij over een **overlandband** (OSM `man_made=goods_conveyor`, 3 ways, 7,5 km gestikt; Wikipedia noemt 5,4 km) naar de kolenopslag van Eskoms **Medupi**-centrale bij Lephalale — mine-mouth, geen weg, spoor of zee. Stoppunt: de kolenopslag, want de centrale zet de kool in één stap om in stroom.
**Welke as van het verhaal:** *Zuid-Afrikaanse Eskom-kool, mijn naar centrale op een steenworp* — contractvolume **14,6 Mt kolen per jaar**, 40 jaar (Exxaro–Eskom, 2008; Wikipedia [1][2]; contractwaarde, geen gemeten verbruik). Mijnvolume: 18,8 Mt eindproduct per jaar (Wikipedia [1], geen jaartal); Exxaro noemt 17 Mt per jaar (geen jaartal) [3].

## 1 · Ketenkaart
```
Grootegeluk-wasserij `kolen-grootegeluk-wasserij`
   ──(b1 leiding/band · overlandband Grootegeluk → Medupi · OSM 7,5 km, Wikipedia 5,4 km)──►
Medupi-kolenopslag `kolen-medupi-kolenopslag` ⏹ stoppunt (centrale 1,4 km verder, binnen het terrein)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding (band) | `kolen-grootegeluk-wasserij` → `kolen-medupi-kolenopslag` | overlandband Grootegeluk → Medupi, OSM-ways 546218313 + 546218315 + 546218312 (alle `man_made=goods_conveyor`, geen naam) | OSM gestikt **7,49 km** (hemelsbreed 5,95); Wikipedia **5,4 km** [2] → +39 %, alleen de laatste way is 5,57 km (+3 %); indicatie, de ±15 %-toets geldt niet als norm | `--been-geojson "leiding\|…"` — vooraf gestikt FeatureCollection `v2/build-cache/ais/graaf/kolen-grootegeluk-medupi-leiding-band.geojson` (11 punten) | nee — doorgetrokken (OSM heeft de band) |

Overige kolenstromen van deze mijn worden bewust niet getekend: de 7 km-band naar Matimba [1] en het spoor voor semi-zachte cokeskool naar Mittal SA (2,5 Mt per jaar, afnemerslocatie niet gevonden) — zie §7.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-grootegeluk-wasserij` | mijn / wasserij (kop van b1) | Grootegeluk-wasserij, beginpunt van de OSM-band | -23.6497, 27.5584 | [6][7] | bron-gelegd (z15 gezien: wasserij- en laadcomplex met rijen kolenstapels en een spoorlus, bandlijnen lopen vanaf het kruis naar ZO; de pit ligt 4 km ZW) |
| `kolen-medupi-kolenopslag` | losplek / kolenopslag Medupi (staart van b1) | Medupi-kolenopslag, eindpunt van de OSM-band | -23.7026, 27.5493 | [2][5][6][7] | bron-gelegd (z15 gezien: zwarte kolenstockyard met stacker-/reclaimerrijen direct W van de ketelhuizen en koeltorens van Medupi) |

Hergebruik: de sitelaag-mijn `w-grootegeluk` (-23.67167, 27.52889, Wikipedia-geohack [1][4]) ligt op de **put**, 3,9 km ZW van de wasserij (z14 gezien: pit-werkzaamheden onder het kruis); de wasserij is het eigenlijke bandbegin — zie §7 voor het gelijktrekken.

## 4 · Via-punten
Geen: een band volgt één gekarteerd OSM-pad, er is geen corridorkeuze. Geen weg-, spoor- of zeebeen in deze keten, dus geen extracts, geen haven-aanloop en geen MARNET.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Grootegeluk-wasserij (dense-media beneficiation, GG6-uitbreiding) | Exxaro Coal (100 %) | ROM-kool → thermische kool (+ cokes- en metallurgische kool) | RoM 51,4 Mt (2024, GEM); 18,8 Mt eindproduct (Wikipedia, geen jaartal); 17 Mt per jaar (Exxaro, geen jaartal) | [1][3][4] |
| Medupi Power Station | Eskom | kool → elektriciteit | 6 × 794 MW = 4.764 MW; commerciele werking 31 juli 2021; kooltoevoer 14,6 Mt per jaar contractueel | [2][5] |

## 6 · Stoppunt
De brief stopt bij de kolenopslag van Medupi: de centrale (GEM-punt -23.7050, 27.5638, ~1,4 km verder) zet de kool in één stap om in stroom, er is geen fase D en E vervalt; een last-mile-been binnen het centraleterrein wordt niet getekend.

## 7 · Open punten
- **Bandlengte:** OSM 7,5 km tegen Wikipedia 5,4 km (+39 %); de eerste twee ways maken een lus via een knoop bij -23.6539, 27.5636, de laatste way (5,57 km) komt wel overeen. Eén gestikte lijn, tekent het OSM-pad zoals gekarteerd; geen controle of OSM de Wikipedia-lengte of een extra aftakking tekent.
- **Geen `man_made=pipeline`:** de band staat als `goods_conveyor` zonder naam of substance; getekend als doorgetrokken leiding op besluit van de haalbaarheidstoets (de strenge kaartregel noemt alleen pipeline).
- **Sitelaag w-grootegeluk** ligt 3,9 km van de wasserij, op de put; centraal gelijktrekken (door mij niet gewijzigd). GEM geeft twee Grootegeluk-coordinaten (-23.6571, 27.5667 en -23.6717, 27.5289); het eerste ligt 0,5 km van de bandknoop.
- **Volume:** 14,6 Mt per jaar is een contractwaarde uit 2008, geen gemeten levering; Eskom-afname is door storingen bij Matimba en Medupi in 2024 gedrukt [8]. Geen meting per jaar gevonden.
- **Matimba-band (7 km) en Mittal-spoor (2,5 Mt per jaar):** bestaan volgens Wikipedia [1], niet getekend (Matimba: tweede band zonder eigen bronkaart; Mittal: afnemerslocatie niet gevonden).
- **Aandeel Medupi in Grootegeluk:** GEM noemt "some 22 Mtpa" voor Medupi plus Matimba samen, onverenigbaar met de ROM-cijfers; niet overgenomen.

## 8 · Bronnen
[1] Wikipedia (EN), Grootegeluk Coal Mine: 23°40′18″S 27°31′44″E, 18,8 Mt eindproduct, 14,6 Mt per jaar voor Medupi (40 jaar), 7 km band naar Matimba, 2,5 Mt semi-zachte cokeskool. https://en.wikipedia.org/wiki/Grootegeluk_Coal_Mine
[2] Wikipedia (EN), Medupi Power Station: 6 × 794 MW, commerciele werking 31 juli 2021, Exxaro-contract 14,6 Mt per jaar 40 jaar, 5,4 km overlandband. https://en.wikipedia.org/wiki/Medupi_Power_Station
[3] Exxaro, Operations: Grootegeluk 17 Mt per jaar (geen jaartal), voedt Medupi en Matimba. https://www.exxaro.com/operations/
[4] Global Energy Monitor, Grootegeluk coal mine: ROM 2017–2024 (2024: 51,4 Mt), twee coordinaten. https://www.gem.wiki/Grootegeluk_coal_mine
[5] Global Energy Monitor, Medupi power station: -23.704973, 27.563839; Exxaro Grootegeluk als bron; jaarvoorraad op terrein (2023). https://www.gem.wiki/Medupi_power_station
[6] OpenStreetMap (ODbL), ways 546218313, 546218315 en 546218312 (`man_made=goods_conveyor`), via de OSM-API 0.6 opgehaald 2026-10-30. https://www.openstreetmap.org/way/546218312
[7] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15): `v2/build-cache/satcheck/sat-kolen-grootegeluk-medupi-wasserij.png`, `sat-kolen-grootegeluk-medupi-medupi-opslag.png`, `sat-kolen-grootegeluk-medupi-put.png`.
[8] WebSearch-samenvatting 2026-10-30: Exxaro-contract 14,6 Mt per jaar (Engineering News, 2014) en interimresultaten augustus 2024 over storingen bij Matimba en Medupi. https://www.engineeringnews.co.za/article/grootegeluk-medupi-expansion-nearing-completion-2014-12-12 en https://iol.co.za/business-report/companies/2024-08-16-a-37-slump-in-exxaros-interim-earnings-drags-down-its-shares-on-jse/

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)
**Bestand:** `v2/data/stroomroute-kolen-grootegeluk-medupi.json` (0,8 KB, versie 2, lonlat) · **functie:** `bak_kolen_grootegeluk_medupi` in `v2/tools/bak_stromen.sh` · **titel:** Kolen · Grootegeluk → Medupi (Zuid-Afrika, overlandband).

| # | modaliteit | km | punten | naam | stippel |
|---|---|---|---|---|---|
| 1 | leiding | 7,5 | 11 | overlandband Grootegeluk-wasserij → Medupi-kolenopslag (OSM-band, 7,5 km; Wikipedia 5,4 km) | nee |

Totaal 7,5 km, 2 markers (wasserij -23.6497,27.5584; kolenopslag -23.7026,27.5493, beide op de uiteinden van de lijn, afstand 0 km). Geen naden (één been).

**Recept:** `hecht_marnet.py route` met alleen `--been-geojson "leiding|…|$BEEN/kolen-grootegeluk-medupi-leiding-band.geojson"` (FeatureCollection met één LineString, vooraf gestikt uit OSM-ways 546218313 vooruit + 546218315 en 546218312 omgekeerd) en twee `--marker`. Geen profiel in `maak_stroombeen_weg.py`, geen extract, geen via-punt, geen MARNET-snap, geen haven-aanloop, geen vlucht, geen letterlijke kopie.

**Leiding (band):** doorgetrokken, want OSM heeft het tracé (`man_made=goods_conveyor`, geen `pipeline`, geen naam of substance; getekend als leiding op besluit van de haalbaarheidstoets). Geen stippel: er is geen gat in het net.

**Toets:** `json.load` slaagt, versie 2, punt_formaat lonlat, modaliteit leiding, 11 punten. Lengte 7,5 km tegen Wikipedia 5,4 km = +39 procent: buiten ±15 procent, maar de brief noemt dit al een indicatie (eerste twee ways lussen via -23.6539,27.5636; laatste way 5,57 km = +3 procent). `toets_knikken.py`: 3 knikken, 0 omkeringen, 0 terugloop (twee spikes van 9 m bij de lus-knoop -23.6539,27.5636, één krappe bocht van 329 m radius bij -23.6602,27.5732); dit volgt het gekarteerde OSM-pad. `toets_rechte_benen.py --min-km 5`: dit been wordt niet gemeld.

**Lessen:** (1) een band als `goods_conveyor` past in de leiding-modaliteit; een vooraf gestikt FeatureCollection volstaat zonder extra tooling. (2) OSM-lengte kan sterk van de publicatie afwijken door een lus in de eerste ways; dit blijft een bevinding, geen reden om het pad recht te trekken. (3) Sitelaag w-grootegeluk ligt 3,9 km van de wasserij (op de put); centraal gelijktrekken, niet door deze bake gewijzigd.

