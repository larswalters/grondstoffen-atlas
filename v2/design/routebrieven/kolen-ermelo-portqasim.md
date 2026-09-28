# Routebrief (licht) · Kolen · Mpumalanga (Ermelo/Kriel) → Richards Bay → Port Qasim (Pakistan)

**stroom-id:** `kolen-ermelo-portqasim` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** thermische kolen uit de Mpumalanga Highveld-Coalink-cluster (representatief:
Kriel Colliery, Seriti Resources) per **spoor** ~580+ km over de Coalink-lijn (Ermelo–Vryheid–Empangeni,
25kV AC/3kV DC) naar Richards Bay Coal Terminal (RBCT), per **zeeschip** ~7.500 km via het
Mozambiekkanaal/Indische Oceaan naar de Arabische Zee (géén Malakka — andere zeestraat dan de bestaande
Sangatta–Mundra-keten) naar de kolenkade van het Port Qasim Power Project (CPEC, 2×660 MW) bij Karachi,
waar de kolen direct bij de centrale gelost en verstookt wordt — stoppunt.
**Welke as van het verhaal:** *Zuid-Afrika → Pakistan, CPEC-kolenimport* — RBCT-doorvoer 52,08 Mt (2024) →
57,66 Mt (2025, +11%, herstellend na de Transnet-spoorcrisis; nameplate ~91 Mt/jr) [9]; Zuid-Afrika→Pakistan
specifiek **2,37 Mt in 2024** (van 43,99 Mt totale Aziatische afzet vanuit Richards Bay, 84,5% van het geheel)
[9]. Port Qasim Power Project draait sinds 2016/2018 op geïmporteerde kolen (Indonesië primair; Zuid-Afrika/
Botswana/Australië aanvullend), verbruik ~4,66 Mt/jr [3].

## 1 · Ketenkaart
```
Kriel Colliery (Coalink-cluster, aannemelijk) `kolen-kriel-mijn`
  ──(b1 spoor · Coalink-lijn Ermelo–Vryheid–Empangeni · ~580+ km, aannemelijk: clusterkeuze)──►
Richards Bay Coal Terminal `kolen-rbct-kade`
  ──(b2 zee · Mozambiekkanaal/Indische Oceaan → Arabische Zee · ~7.500 km,
     MARNET + haven-aanloop beide zijden — beide kades >25 km van hun zeeknoop)──►
Port Qasim Power Project-kade `kolen-portqasim-kade` ⏹ stoppunt (kolen → elektriciteit, geen fase D/E)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-kriel-mijn` → `kolen-rbct-kade` | Coalink-lijn Ermelo–Vryheid–Empangeni (dual-voltage 25kV AC/3kV DC, 44 exportmijnen) | 580 (Ermelo→Richards Bay, gepubliceerd) [4]; Kriel→Ermelo niet apart gepubliceerd (aannemelijk inbegrepen) | toets_spoorroute (BAKE_SUFFIX=-raw, extract zuid-afrika) | nee — gemeten been, mijnkeuze zelf is aannemelijk (§7) |
| b2 | B | zee | `kolen-rbct-kade` → `kolen-portqasim-kade` | Mozambiekkanaal → Indische Oceaan → Arabische Zee (geen Malakka) | ~7.500 (webcheck; grote cirkel Richards Bay–Karachi ≈6.800 km + kustvolging) | MARNET tot zeeknoop 5200 (-28.4494,32.9205, 94,2 km van RBCT) resp. zeeknoop 4085 (24.8174,66.9757, 40,0 km van Port Qasim) + haven-aanloop-stippel beide zijden | ja — beide kades > 25 km max-snap én > 5 km LAR-586-regel |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-kriel-mijn` | mijn / laadplek (Coalink-cluster, representatief) | Kriel Colliery, Seriti Coal (Pty) Ltd, open dagbouw bij Kriel, Mpumalanga | -26.2258, 29.1360 | [1][7][8] | bron-gelegd (z15 gezien: grote open dagbouwput met turquoise waswater, trapsgewijze afgravingen, haalwegen en een spoorverbinding direct ten oosten van de put); mijnkeuze binnen de Coalink-cluster blijft **aannemelijk** (§7) |
| `kolen-rbct-kade` | overslag spoor → zee | Richards Bay Coal Terminal, laadkade/stockyard | -28.8187, 32.0523 | [2][4][8] | bron-gelegd (z15 gezien: kilometerslange kolenstockyards, meerdere bulkcarriers gemeerd aan de kade, conveyors naar de scheepsladers en een spoorbundel/emplacement landinwaarts) |
| `kolen-portqasim-kade` | losplek zee / verwerkingsknoop / stoppunt | Port Qasim Power Project (CPEC), kolenkade aan het centraleterrein | 24.7808, 67.3701 | [3][6] | bron-gelegd (z16 gezien: twee koeltorens, een groot zwart kolenstockpile naast een conveyor en een steiger met meerdere afmeerdukdalven de vaargeul in — de kolenkade ligt direct bij de centrale) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Ermelo — kop van de gepubliceerde Coalink-lijn | -26.5333, 29.9833 | begin van de gemeten 580 km Ermelo→Richards Bay [4]; hier komt (buiten deze brief om) de aansluiting vanaf de mijnencluster binnen |
| b1 | 2 | Vryheid — lijnknoop tussen de twee bouwsegmenten | -27.7705, 30.7886 | vaste tussenstop tussen het geüpgradede Ermelo–Vryheid-stuk en het nieuwere Vryheid–Empangeni-stuk [4] |
| b1 | 3 | Empangeni — vóór de laatste kusttak naar RBCT | -28.7461, 31.8972 | einde van het Vryheid–Empangeni-segment (210 km, 10,5 km tunnels/67 bruggen) vlak vóór de aftakking naar RBCT [4] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Richards Bay Coal Terminal (RBCT) | RBCT Company (consortium Zuid-Afrikaanse kolenexporteurs) | spoorkolen (44 mijnen) → scheepslading | doorvoer 52,08 Mt (2024) → 57,66 Mt (2025, +11%); nameplate ~91 Mt/jr | [9] |
| Port Qasim Power Project (CPEC) | Port Qasim Energy Holding (Al-Mirqab Capital 49% / PowerChina 51%) | geïmporteerde kolen → elektriciteit | 2×660 MW = 1.320 MW; jaarverbruik ~4,66 Mt kolen (Indonesië primair; Zuid-Afrika/Botswana/Australië aanvullend) | [3] |

## 6 · Stoppunt
De brief stopt bij de kolenopslag/centrale van Port Qasim Power Project: kolen wordt daar in één stap tot
elektriciteit verstookt (geen cokes/staal-tussenstap zoals bij metallurgische kolen), dus fase D/E bestaat
hier per definitie niet — zelfde patroon als kolen-sangatta-mundra.

## 7 · Open punten
- **Mijnkeuze blijft aannemelijk:** de Coalink-lijn bedient 44 mijnen zonder gepubliceerde single-mine-
  herkomst voor Pakistaanse lading; Kriel Colliery (Seriti) is gekozen als representatieve, grote Seriti-
  operatie op de lijn, niet als gebronde oorsprong — erkend in het ontwerp en de haalbaarheidstoets
  (vergelijkbaar met het olie-Japan-aggregaatprobleem).
- **Kriel Colliery levert primair aan het naastgelegen Kriel Power Station (Eskom, binnenlands)** — geen
  bron bevestigt een specifiek exportvolume van Kriel Colliery zelf naar RBCT/Pakistan; het spoorbeen
  vertegenwoordigt de cluster, geen geverifieerde single-mine-ladingstroom.
- **Kriel→Ermelo-afstand niet apart gepubliceerd:** de gemeten 580 km dekt alleen Ermelo→Richards Bay
  (Wikipedia/Class 19E); de nieuwe 90 km-tak Broodsnyersplaas→Ermelo wijst op minstens enkele tientallen
  km extra tussen de mijnencluster en Ermelo — verwacht een positief verschil tussen bake-km en de 580 km
  in §2 bij het bakken, geen via-punt bijschuiven om het getal te laten kloppen.
- **Beide zeeknopen liggen ver van hun kade** (RBCT 94,2 km tot zeeknoop 5200; Port Qasim 40,0 km tot
  zeeknoop 4085) — ruim boven de 25 km max-snap én de 5 km-haven-aanloopregel (LAR-586); beide zijden
  krijgen dus een haven-aanloop-stippel, geen doorgetrokken MARNET-snap tot de kade zelf.
- **RBCT-capaciteit wordt gedeeld** met Eskom-binnenlandse vraag en concurrerende exportbestemmingen
  (India/Azië); de Pakistaanse afname hangt aan de operationele status van één CPEC-centrale (politiek/
  financieel kwetsbaar) — zoals in het ontwerp genoemd.
- **Ketenvolume:** Zuid-Afrika→Pakistan 2,37 Mt/jr (2024, Zuid-Afrikaanse Aziatische exportstatistiek) is
  het enige gebronde ketencijfer; het volume van déze specifieke as (Kriel→RBCT→Port Qasim) is niet apart
  gepubliceerd.

## 8 · Bronnen
[1] Global Energy Monitor, Kriel Coal Mine — coördinaat -26.225785/29.136045 (exact); eigenaar Seriti Coal Pty Ltd (100%, via Anglo American-overname 2018); productie 2017 5,4 Mt → 2025 4,01 Mt. https://www.gem.wiki/Kriel_Coal_Mine
[2] Wikipedia, Port of Richards Bay — coördinaat 28°49′05″S 32°03′07″E; nameplate 91 Mt/jr; RBCT-kade zes berths/vier scheepsladers, 276 ha-terrein, 8,2 Mt opslagcapaciteit. https://en.wikipedia.org/wiki/Port_of_Richards_Bay
[3] Wikipedia, Port Qasim Power Project — 2×660 MW, Port Qasim Energy Holding (Al-Mirqab Capital 49%/PowerChina 51%), operationeel sinds nov. 2017/apr. 2018; kolenbron Indonesië primair + Zuid-Afrika/Botswana/Australië aanvullend; verbruik 4,66 Mt/jr. https://en.wikipedia.org/wiki/Port_Qasim_Power_Project
[4] Wikipedia, South African Class 19E — Coalink-lijn Ermelo→Richards Bay 580 km; 44 exportmijnen in Mpumalanga; dual-voltage 25kV AC/3kV DC; bouwsegmenten Ermelo–Vryheid (geüpgraded) en Vryheid–Empangeni (210 km, 10,5 km tunnels/67 bruggen) + nieuwe 90 km-tak Broodsnyersplaas–Ermelo. https://en.wikipedia.org/wiki/South_African_Class_19E
[5] Wikipedia, Ermelo, Mpumalanga — coördinaat 26°32′S 29°59′E; "de spoorlijn die de kolenvelden verbindt met de Haven van Richards Bay". https://en.wikipedia.org/wiki/Ermelo,_South_Africa
[6] Wikipedia, Port Qasim — coördinaat 24°46′N 67°20′E; Coal, Clinker & Cement Terminal (CCCT), 8 Mt/jr, ~$180 mln, voltooid ~2011 (algemene kolenterminal in de haven, niet per se de CPEC-centralekade). https://en.wikipedia.org/wiki/Port_Qasim
[7] Web search (meerdere bronnen), Kriel Colliery / Seriti Resources locatie en overname South32-Zuid-Afrikaanse kolenactiva (2021, incl. Kriel-cluster); GPS-varianten -26,225785/29,136045 en -26,2284/29,1389 (ondergronds). https://www.gem.wiki/Kriel_coal_mine · https://seritiza.com/business/seriti-power/kriel/
[8] OpenStreetMap (ODbL) via Nominatim — "Kriel" plaats 26,2589°S/29,2628°E · "Richards Bay Coal Terminal" landuse-vlak -28,81867/32,05228 · "Vryheid" -27,77049/30,78857 · "Empangeni" -28,74611/31,89722. https://www.openstreetmap.org
[9] Haalbaarheidstoets M31 golf 2 (2026-09-28) — RBCT-doorvoer 52,08 Mt (2024) / 57,66 Mt (2025, +11%, herstellend na de Transnet-spoorcrisis; nameplate ~91 Mt/jr; CNBC Africa/Mining Weekly, jan. 2025); Zuid-Afrika→Pakistan 2,37 Mt (2024, van 43,99 Mt totale Aziatische afzet vanuit Richards Bay, 84,5%; Zuid-Afrikaanse Aziatische exportstatistiek). Bindend verwerkt in §1/§5 van deze brief.
[10] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16, live) — `v2/build-cache/satcheck/sat-kolen-ermelo-portqasim-kriel-colliery.png`, `sat-kolen-ermelo-portqasim-rbct-kade.png`, `sat-kolen-ermelo-portqasim-portqasim-plant.png`, `sat-kolen-ermelo-portqasim-portqasim-zoom.png`.
[11] `v2/tools/hecht_marnet.py` (zeeknoop-afstandscheck, live) — RBCT-kade → zeeknoop 5200 (-28,4494/32,9205) op 94,2 km; Port Qasim-kade → zeeknoop 4085 (24,8174/66,9757) op 40,0 km.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `kolen-ermelo-portqasim`** → `v2/data/stroomroute-kolen-ermelo-portqasim.json` — 7 benen,
**7.869,7 km**, 2.805 punten, 6 markers. spoor 137,8+229,6+216,8+37,6 = 621,8 km · zee 101,5 (stippel) +
7.102,8 + 43,6 (stippel) = 7.247,9 km. Recept: `bak_stromen.sh` (functie `bak_kolen_ermelo_portqasim`).

**b1 (spoor, vier losse runs op het 1-op-1-net, console bevestigt "3260717 spoor-edges", `BAKE_SUFFIX=-raw`,
extract zuid-afrika):**
1. Kriel Colliery → Ermelo: **137,8 km** (losse run 137,4 km over 109 edges, grootcirkel 91,1 km, verhouding
   1,51; snap kop 14,30 km op het hoofdnet-component 47.640 km — geen doorlopende OSM-spoorlijn tot in de
   dagbouwput; snap staart 1,79 km).
2. Ermelo → Vryheid: **229,6 km** (losse run 228,4 km over 214 edges, grootcirkel 159,0 km, verhouding 1,44;
   snap 1,79/1,26 km).
3. Vryheid → Empangeni: **216,8 km** (losse run 215,7 km over 312 edges, grootcirkel 153,5 km, verhouding
   1,41; snap 1,26/2,01 km).
4. Empangeni → Richards Bay Coal Terminal: **37,6 km** (losse run 37,0 km over 58 edges, grootcirkel 17,1 km,
   verhouding 2,16 — de laatste kusttak, geen doorgaande hoofdlijn; snap 2,01/0,52 km).

Som **621,8 km**. ⚠️ **Ermelo→RBCT alleen (229,6+216,8+37,6 = 484,0 km) ligt −16,6 % onder de gepubliceerde
580 km (Ermelo→Richards Bay, Wikipedia Class 19E) — buiten de ±15 %-norm.** De brief verwachtte het
omgekeerde (§7: Kriel→Ermelo-stuk niet apart gepubliceerd, dus een positief verschil bij het optellen van de
héle as); in plaats daarvan ligt zelfs het Ermelo→RBCT-deelstuk zónder de Kriel-kop al onder de gepubliceerde
lengte. Bevinding, geen via-punt bijgeschoven om het getal te halen (zie de gereedschapslessen hieronder).

**b2 (zee, MARNET-route zeeknoop 5200 → zeeknoop 4085, beide zijden een haven-aanloop, LAR-586):**
- Haven-aanloop RBCT: `maak_havenaanloop.py --van -28.8187,32.0523 --naar -28.4494,32.9205` — alle acht
  trappen getoetst, gekozen cel 0,01° gebufferd (minste land midden op de lijn) → **101,5 km · 44 punten ·
  0,89 km over land, uitsluitend aan het kade-uiteinde (geen landkruising midden op de lijn)**, omwegfactor
  1,078 tegen de rechte lijn (94,2 km, waarvan 1,5 km/2 % al over land).
- Zeebeen (MARNET, tussen de twee zeeknopen): `--been "zee|...|-28.4494,32.9205|24.8174,66.9757"` — snap
  0,000 km aan beide kanten (de zeeknopen zijn zelf de eindpunten) → **7.102,8 km over 20 MARNET-edges**
  (724 punten) tegen de indicatieve ~7.500 km uit de brief = **−5,3 %**, ruim binnen ±15 %. Lengte-invariant:
  getekende lijn 7.102,850 vs som edge-km 7.102,700 = +0,150 km (de naden).
- Haven-aanloop Port Qasim: `maak_havenaanloop.py --van 24.7808,67.3701 --naar 24.8174,66.9757` — gekozen
  cel 0,005° kaal → **43,6 km · 56 punten · 12,00 km over land, uitsluitend aan het kade-uiteinde** (Port
  Qasim ligt landinwaarts in een riviermonding, vandaar het hogere aandeel; geen landkruising midden op de
  lijn), omwegfactor 1,089 tegen de rechte lijn (40,0 km, waarvan 36,6 km/91 % al over land).
  ⚠️ `maak_havenaanloop.py` schrijft altijd in `--van`→`--naar`-volgorde; de Port Qasim-aanloop is ná
  generatie voor invoeging handmatig omgedraaid van kade→knoop naar knoop→kade (coördinaten ongewijzigd,
  alleen de puntvolgorde), zodat hij in reisvolgorde ná het hoofdzeebeen aansluit.

**Toets naden:** alle overgangen ≤0,52 km — spoor→spoor 0,00 km overal, spoor(RBCT-kade)→haven-aanloop RBCT
0,52 km, haven-aanloop→hoofdzeebeen 0,00 km, hoofdzeebeen→haven-aanloop Port Qasim 0,00 km. Ruim binnen de
5 km-norm; geen tweede haven-aanloop nodig.

**`toets_knikken.py`:** 4 knikken ≥60°, 2 omkeringen ≥150°, waarvan **1 TERUGLOOP** — been 2 (Ermelo→Vryheid)
bij −27,81280/30,82550 (180,0°, R~0 m, v=12,9). ⚠️ **Bevinding, niet dichtgetrokken** (werkwijze §5: buiten de
norm = bevinding) — geen van de drie via-punten ligt in de buurt van dit punt; eigenschap van het 1-op-1-
OSM-net op dat stuk zelf. Verder: 1 scherpe bocht "echt" bij −26,55780/29,99490 (180,0°, R~0 m, kopmaak bij
Ermelo, v=1,5) en 1 spike bij −28,76640/31,91120 (143,1°, R~41 m, gedeeld tussen beide segmenten rond het
Empangeni-knooppunt) — beide kopmaak-plekken op een emplacement/spooraansluiting, geen fout.

**`toets_rechte_benen.py --min-km 5`:** geen been van deze stroom in de uitslag — beide haven-aanlopen hebben
een omwegfactor > 1 (1,078 resp. 1,089) en worden dus niet als verdachte rechte lijn aangemerkt.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {zee, spoor} (binnen de toegestane
set), elk been ≥2 punten (minimum 44), bestandsgrootte **52,7 KB** (ruim onder de 300 KB-richtwaarde).

**Markers:** Richards Bay Coal Terminal 0,0 m · Port Qasim 0,0 m (beide exacte uiteinden van hun
haven-aanloop-geojson) · Ermelo 1.606,9 m · Vryheid 1.224,9 m · Empangeni 2.014,0 m (via-punt corridorkeuze —
komt overeen met de spoorrouter-snapafstanden per uiteinde, anker ≠ routeerpunt) · **Kriel Colliery
14.303,1 m** (anker ≠ routeerpunt — de mijn-eigen railaansluiting op de put ontbreekt in OSM, de kop-snap van
de spoorrouter was al 14,30 km; §7 van de brief noemt de mijnkeuze zelf al aannemelijk, geen coördinaat
verzonnen om dichterbij te komen).

**Open punten die blijven staan (zie ook §7):**
- Ermelo→RBCT meet −16,6 % onder de gepubliceerde 580 km, tegengesteld aan de in de brief verwachte richting
  (zie b1 hierboven) — nieuw open punt, niet in de brief voorzien.
- Mijnkeuze binnen de Coalink-cluster blijft aannemelijk (44 mijnen); de Kriel-railaansluiting ontbreekt in
  OSM (14,30 km snap tot het hoofdnet).
- Beide zeeknopen liggen ver van hun kade (RBCT 94,2 km, Port Qasim 40,0 km) — nu opgelost met een
  haven-aanloop-stippel aan beide zijden, geen doorgetrokken MARNET-snap tot de kade zelf.
- Eén TERUGLOOP op been 2 (Ermelo→Vryheid) — eigenschap van het lokale 1-op-1-net, niet van een gekozen
  via-coördinaat.
- Ketenvolume van déze specifieke as niet apart gepubliceerd (alleen het Zuid-Afrika→Pakistan-totaal,
  2,37 Mt/jr 2024, is gebrond) — ongewijzigd t.o.v. §7.

**Gereedschapslessen:**
- Een gemeten spoorbeen kan zelfs ONDER de gepubliceerde lengte van de beschreven exportlijn uitkomen wanneer
  de brief een specifieke, mogelijk opgewaardeerde lijn beschrijft (de Coalink-lijn met tunnels/bruggen) en de
  router over het bredere 1-op-1-hoofdnet een kortere aansluiting vindt — de ±15 %-norm signaleert dat
  verschil correct, maar "buiten de norm" betekent hier eerder dat het OSM-net de specifieke exportroute niet
  1-op-1 volgt, niet dat er een foute via-keuze is.
- Twee haven-aanlopen tegelijk in één keten (beide kades > 25 km én > 5 km van hun zeeknoop, LAR-586)
  verlopen probleemloos wanneer beide `maak_havenaanloop.py`-trappenreeksen meteen een geslaagd pad geven —
  geen enkele trap hoefde terug te vallen op een rechte stippel.
- `maak_havenaanloop.py` schrijft altijd in `--van`→`--naar`-volgorde; bij een aanloop die ná een zeebeen komt
  (een aankomst-been) moet de output-geojson vóór gebruik in `--stippel-geojson` op reisvolgorde gedraaid
  worden (knoop→kade), anders klopt de naad-toets niet.
