# Routebrief (licht) · olie — Habshan (VAE) → Fujairah (VAE) → Chiba (Japan)

**stroom-id:** `olie-habshan-chiba` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31) · **status:** gebakken
**Keten in één zin:** Murban-ruwe olie vanaf het Habshan-verzamelknooppunt (ADNOC Onshore), per **leiding**
(de Habshan-Fujairah-pijpleiding, "Hormuz-bypass") naar de Fujairah-exportterminal aan de Golf van Oman, per
**VLCC** over de Golf van Oman → Arabische Zee → Straat Malakka → Zuid-Chinese Zee → Oost-Chinese Zee naar de
ENEOS-raffinaderij op de Chikusa-kust bij Ichihara, Tokiobaai.
**Welke as van het verhaal:** *de Hormuz-bypass* — VAE-crude die de Straat van Hormuz fysiek omzeilt via een
48"-pijpleiding (1,5–1,8 mln vpd, uitbreiding naar 3 mln vpd gepland 2027, ~50% gereed) [1][2][11][12]. Fujairah
exporteert ~840 kb/d–1,1 mln vpd Murban (peiljaar 2024–2026); Japan neemt structureel ~30% van ADNOC's totale
Murban-export af, via IFAD-partners INPEX/ENEOS [bronopgave]. Dat 30%-cijfer is een **aggregaat over heel ADNOC's
Murban-export**, niet cargo- of terminalspecifiek — zie §7.

## 1 · Ketenkaart
```
Habshan-verzamelknooppunt `ol-habshan` ──(b1 leiding · Habshan–Fujairah-pijpleiding "Hormuz-bypass",
    via Sweihan · ~406 km gepubliceerd, gedeeltelijk stippel)──►
   Fujairah-exportterminal `ol-fujairah-term` (Golf van Oman, buiten Hormuz)
   ──(b2 zee · Golf van Oman → Arabische Zee → Straat Malakka → Zuid-Chinese Zee → Oost-Chinese Zee ·
       ~9.700 km, MARNET)──►
   Chiba-raffinaderij (ENEOS) `ol-chiba-ref` (Chikusa-kaigan, Ichihara, Tokiobaai) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Habshan-verzamelknooppunt → Fujairah-exportterminal | Habshan-Fujairah oil pipeline (48", "Hormuz-bypass"), via Sweihan | 406 (14 km offshore) [5]; eigen OSM-meting: som 5 waysegmenten 402,0 km + intern gat 17,3 km ≈ 419 km [7] | OSM-way (5 segmenten, `man_made=pipeline`, `name="Habshan–Fujairah oil pipeline"`, gcc-staten-extract) — **grotendeels doorgetrokken**, één stippel over het interne kaarteringsgat | gedeeltelijk — één stippel van ~17 km tussen twee OSM-waysegmenten (bij Sweihan/Al Ain); de rest van het tracé is als way gekarteerd |
| b2 | B | zee | Fujairah-exportterminal → Chiba-raffinaderij (ENEOS) | Golf van Oman → Arabische Zee → Straat Malakka → Zuid-Chinese Zee → Oost-Chinese Zee | ~9.700 [ontwerp/webcheck; grote cirkel Fujairah–Chiba 7.878 km, routeafstand langer via Malakka] | MARNET (kade → kade) | nee — beide kades naar verwachting ruim binnen zeeknoop-bereik (25 km); definitief bij het bakken |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-habshan` | kop van de leiding / verzamelknooppunt (ADNOC Onshore/ADCO) | Habshan-pijplijnkop (Habshan–Fujairah-leiding) | 23.8285, 53.4915 | [5][7][14] | bron-gelegd (z15 gezien: kruispunt van de pijplijn-/wegcorridor in de woestijn; ~700 m NNO een klein tank-/pompstationcomplex met 2 bolvormige + 2 cilindrische tanks — een pompstation langs de leiding, geen open terrein) |
| `ol-fujairah-term` | overslag leiding → zee (exportterminal, Hormuz-bypass-terminus) | Fujairah-exportterminal (FOIZ/ADNOC-tankenpark, Habshan-Fujairah-pijplijneind) | 25.2135, 56.3419 | [5][7][8][14] | bron-gelegd (z15 gezien: gebouwencomplex direct naast een groot tankenpark tegen de bergvoet, kade/havenbekken met tankers op ~1 km afstand — pijplijneind valt op de rand van het FOIZ-tankenterrein) |
| `ol-chiba-ref` | losplek / raffinaderij (fase C-knoop) | Chiba-raffinaderij (ENEOS), Chikusa-kaigan 1, Ichihara, Tokiobaai | 35.5195, 140.0430 | [9][10][14] | bron-gelegd (z16 gezien: dicht tankenpark + destillatietorens/procesinstallaties direct aan de kust, tanker afgemeerd aan een steiger — het adres 千種海岸1 matcht deze kuststrook; de raffinagestrook van Ichihara telt meerdere naburige operators, dus het exacte ENEOS-hek binnen dit complex is niet 100% te onderscheiden van een aangrenzende installatie) |

## 4 · Via-punten (alleen b1 — de leiding heeft geen alternatieve corridor, wel OSM-waysegmentgrenzen)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | OSM-waysegmentgrens 1 | 24.0062, 53.8696 | einde eerste gekarteerde pijplijnsegment, corridor buigt richting Sweihan [7] |
| b1 | 2 | OSM-waysegmentgrens 2 | 24.1650, 54.3779 | volgende segmentgrens, corridor loopt oostwaarts door het binnenland [7] |
| b1 | 3 | einde OSM-segment vóór het gat | 24.5977, 55.3998 | laatste gekarteerde punt vóór de ~17 km-onderbreking bij Sweihan/Al Ain [7] |
| b1 | 4 | hervatting OSM-segment ná het gat | 24.5749, 55.2302 | eerste gekarteerde punt ná de onderbreking, richting het Hajar-gebergte [7] |
| b1 | 5 | OSM-waysegmentgrens 5 | 25.1913, 56.1326 | laatste segmentgrens vóór de afdaling naar de Fujairah-kust [7] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Fujairah-exportterminal (FOIZ) | ADNOC / diverse tank-tenants (FOT, VOPAK Horizon, ADNOC-cavernes) | pijplijn-Murban → tankopslag → VLCC-lading | Fujairah-export ~840 kb/d–1,1 mln vpd Murban; regionale opslag > 10 mln m³ (FOIZ, alle tenants) [1][8] | [1][2][8] |
| Chiba-raffinaderij (ENEOS) | ENEOS Holdings | ruwe olie (o.a. Murban) → brandstoffen/nafta | niet in deze brief gebrond (§7) | [9][10] |

## 6 · Stoppunt
De brief stopt bij de poort van de Chiba/Ichihara-raffinaderij: geen bron koppelt één specifieke lading aan één
Japanse raffinaderij — het "Japan 30%"-cijfer is een aggregaat over heel ADNOC's Murban-export, niet cargo- of
terminalspecifiek. ENEOS/INPEX als IFAD-partners maken Chiba een aannemelijke, maar niet gebronde eindbestemming;
fase D/E (producten vanaf de raffinaderij) vervallen.

## 7 · Open punten
- **Het "Japan 30%"-cijfer is een aggregaat, geen cargo-niveau bron** — geen bron koppelt één specifieke
  Fujairah-lading aan Chiba/ENEOS specifiek; de keten blijft terminal-niveau aanname (zoals de haalbaarheidstoets
  al aangaf).
- **Het ~17 km-kaarteringsgat in de OSM-pijplijn** (tussen 24,5977/55,3998 en 24,5749/55,2302, bij Sweihan/Al Ain)
  is niet onafhankelijk bevestigd als "hier ligt geen leiding" — het kan een kartering-omissie zijn; bij het bakken
  blijft dit stuk een stippel, tenzij een latere OSM-editie het alsnog dekt.
- **v1-checklist-ankers verworpen na satellietcheck:** `oil-term-fujairah` (25.12, 56.33) bleek bij z14-controle in
  de stad Fujairah/bij het vliegveld te liggen, niet bij de exportterminal (10,5 km verschil) — vervangen door het
  OSM-pijplijneind bij het FOIZ-tankenpark. `oil-ref-japan` (35.50, 140.10) bleek in landbouwgebied ten zuidoosten
  van de raffinagestrook te liggen (5,2 km verschil) — vervangen door het ENEOS-adrespunt Chikusa-kaigan 1.
- **Exact ENEOS-hek binnen de Ichihara-raffinagestrook** niet 100% te onderscheiden van naburige operators
  (meerdere raffinage-/petrochemiebedrijven delen deze ~10 km kuststrook) — anker blijft op site-/complexniveau.
- **Fujairah-kade-zeeknoop en Chiba-kade-zeeknoop nog niet gemeten** (MARNET-snap ≤25 km wordt bij het bakken
  bevestigd); de ~9.700 km is een ontwerp-/webcheck-schatting, geen MARNET-uitkomst.
- **Jaarvolume-eenheid:** kb/d (duizend vaten/dag) als brongegeven; zie volume-notitie hieronder voor Mt/j.

*Volume-notitie:* Fujairah-terminaal totaal 840–1.100 kb/d Murban × 365 dagen ≈ 306–402 mln vaten/jaar; bij
~7,3 vaten/ton voor Murban-achtige lichte ruwe olie ≈ **~42–55 Mt/j** (oorspronkelijke eenheid: kb/d; dit is het
totale Fujairah-exportvolume, niet het Japan-specifieke aandeel — zie §7).

## 8 · Bronnen
[1] MEES, 18-10-2024 — "ADNOC flexes crude export options with expansion of Hormuz-bypass pipeline". https://www.mees.com/2024/10/18/refining-petrochemicals/adnoc-flexes-crude-export-options-with-expansion-of-hormuz-bypass-pipeline/0c709ab0-8d48-11ef-914d-53b11a707cb3
[2] CNBC, 12-03-2026 — Straat van Hormuz-context, pijpleidingcapaciteit 1,5–1,8 mln vpd. https://www.cnbc.com/2026/03/12/strait-of-hormuz-oil-pipelines-iran-war-saudi-arabia-uae.html
[3] GEM.wiki, "Habshan–Fujairah Oil Pipeline". https://www.gem.wiki/Habshan%E2%80%93Fujairah_Oil_Pipeline
[4] ICE Insights, "Prospects of Murban as a benchmark". https://www.ice.com/insights/market-pulse/energy/prospects-of-murban-as-a-benchmark
[5] Wikipedia, "Habshan–Fujairah oil pipeline" — lengte 406 km (14 km offshore), capaciteit 1,5 mln vpd, diameter 48", eigenaar Mubadala, bouw 2008–2011, operationeel juni 2012, kosten $3,3 mrd, aannemer CPECC, route via Sweihan. https://en.wikipedia.org/wiki/Habshan%E2%80%93Fujairah_oil_pipeline
[6] Wikipedia, "Habshan" — 23,7816/53,5744, olie-/gasveld ADNOC, Al Dhafra-regio. https://en.wikipedia.org/wiki/Habshan
[7] OpenStreetMap/Overpass (ODbL) — 5 ways `man_made=pipeline`, `name="Habshan–Fujairah oil pipeline"` in bbox 22,5–25,5/52,5–57,0, gcc-staten-extract; eigen meting (Overpass-query 2026-09-28): som 402,0 km, kop 23,8285/53,4915, eind 25,2135/56,3419, intern gat 17,3 km tussen 24,5977/55,3998 en 24,5749/55,2302. https://www.openstreetmap.org
[8] S&P Global Commodity Insights — Fujairah crude storage/FOIZ-context, ADNOC-cavernes 42 mln vaten, FOT 1,177 mln m³ onshore-opslag. https://www.spglobal.com/energy/en/news-research/latest-news/crude-oil/052522-adnocs-fujairah-crude-oil-storage-caverns-set-to-open-in-2023-sources
[9] OpenStreetMap/Nominatim (ODbL) — landuse "Ichihara refinery" 35,5360/140,0600, Ichihara-industriecomplex. https://www.openstreetmap.org
[10] Wikipedia (ja), via zoekindex "石油コンビナート"/"千種海岸" — adres ENEOS(株)千葉製油所: 千葉県市原市千種海岸1番地; MediaWiki-coördinaat 千種海岸: 35,51197/140,05475. https://ja.wikipedia.org
[11] The National, 15-05-2026 — uitbreiding Habshan-Fujairah-leiding naar 3 mln vpd, gepland 2027. https://www.thenationalnews.com
[12] EnergyNow — uitbreiding ~50% gereed. https://energynow.com
[13] Institute for Energy Research — capaciteitscijfers Hormuz-bypass-pijpleidingen. https://www.instituteforenergyresearch.org
[14] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16) — `sat-olie-habshan-chiba-habshan-kop.png`, `sat-olie-habshan-chiba-fujairah-eind.png`, `sat-olie-habshan-chiba-eneos-tanks.png`, `sat-olie-habshan-chiba-chikusa-kaigan.png` (verificatiebeeld), `sat-olie-habshan-chiba-fujairah-v1.png` en `sat-olie-habshan-chiba-chiba-ref.png` (beide v1-checklist-ankers, verworpen — zie §7).

## 9 · Gebakken (2026-09-28, lichte werkwijze)

**Stroom `olie-habshan-chiba`** → `v2/data/stroomroute-olie-habshan-chiba.json` — 4 benen, **12.129,2 km**, 2.055 punten, 3 markers (1 stippel been).
Recept: `bak_stromen.sh` (functie `bak_olie_habshan_chiba`).

**b1 (leiding, been-geojson, segment 1):** vijf OSM-ways (`man_made=pipeline`, `name~"Habshan–Fujairah oil pipeline"`, gcc-staten-extract, ids 451508619/586125766/225206383/360437230/360499797) opgehaald met een eigen pyosmium-scan op de lokale pbf (geen Overpass nodig) en per waysegment op eindpunt-nabijheid gestikt tot twee doorlopende LineStrings, in reisvolgorde. Segment 1 (ways 451508619+586125766+225206383): Habshan-kop (23,8285/53,4915) → laatste gekarteerde punt vóór het gat (24,5977/55,3998), **236,9 km**, 332 punten.

**b1-gat (leiding, stippel):** `--stippel "leiding|…, schematisch — OSM-kaarteringsgat ~17 km bij Sweihan/Al Ain (brief §7)|24.5977,55.3998|24.5749,55.2302"` — rechte lijn over het interne kaarteringsgat, **17,3 km**. Niet onafhankelijk bevestigd als échte fysieke onderbreking (kan een OSM-omissie zijn, §7) — blijft daarom een stippel, geen doorgetrokken gok.

**b1 (leiding, been-geojson, segment 2):** ways 360437230+360499797, van de hervatting na het gat (24,5749/55,2302) tot het Fujairah-pijplijneind (25,2135/56,3419), **165,1 km**, 522 punten.

⚠️ **Lengtetoets b1 (totaal, drie stukken samen):** 236,9 + 17,3 + 165,1 = **419,3 km** tegen gepubliceerd 406 km (14 km offshore) = **+3,3%**, ruim binnen ±15% en vrijwel gelijk aan de eigen OSM-som uit de brief (402,0 + 17,3 ≈ 419 km) — de brief-aanwijzing en de bake komen coordinaat voor coördinaat overeen.

**b2 (zee, geroutet):** `--been "zee|VLCC Fujairah-exportterminal → Chiba-raffinaderij (…)|25.2135,56.3419|35.5195,140.0430"` — geen haven-aanloop nodig, beide kades snapten al vooraf ruim binnen de 25 km-norm (Fujairah 10,47 km, Chiba 7,67 km). MARNET-route via de Golf van Oman, Arabische Zee, Straat Malakka, Zuid- en Oost-Chinese Zee — geen Hormuz-doorvaart (het hele punt van de Hormuz-bypass-leiding), **11.709,9 km**, 1.199 punten.

⚠️ **Lengtetoets b2 buiten de norm, bevinding niet dichtgetrokken:** 11.709,9 km tegen de gepubliceerde ~9.700 km (ontwerp/webcheck-schatting, brief §2) = **+20,7%**, buiten ±15%. De brief markeerde deze schatting zelf al als "ontwerp/webcheck", niet als gemeten of gepubliceerde ladingroute-lengte, en de grote cirkel Fujairah–Chiba is zelf al 7.878 km — de MARNET-route via Malakka is substantieel langer dan de webcheck-schatting veronderstelde. Geen via-punt bijgeschoven om het getal te halen; de gemeten km is de bevinding (zelfde klasse als olie-bonny-vadinar §9).

**Naad b1→b2:** het leiding-eind (segment 2) staat exact op het Fujairah-anker (25,2135/56,3419); het zeebeen routeert vanaf de dichtstbijzijnde MARNET-zeeknoop, **10,47 km** verderop (zeeknoop 8407, 25,1378/56,4038) — **naad > 5 km**, bevinding: anker ≠ routeerpunt, binnen de 25 km-snapgrens die de brief al aangaf, niet dichtgetrokken met een extra stippel.

> **Bijgewerkt 2026-09-28 (LAR-586):** de naad is alsnog dichtgezet met een haven-aanloop Fujairah over water (`maak_havenaanloop.py`: 12,2 km, 9 punten, 2,2 km over land alleen aan de kadekant) als stippel tussen leiding en zeebeen. Keten nu 12.141,4 km in vijf benen, geen naad > 0,5 km.

**Markers:** `ol-habshan` (kop, 0,00 km van de lijn) · `ol-fujairah-term` (overslag leiding→zee, 0,00 km van de lijn — leiding-eind; het zeebeen begint op 10,47 km ervandaan, zie naad-bevinding) · `ol-chiba-ref` (losplek/stoppunt, 7,67 km van het routeerpunt — anker ≠ routeerpunt, binnen de snapgrens).

**Toets:** `toets_knikken.py` — 17 knikken ≥60°, waarvan **0 omkeringen ≥150° en 0 terugloop** (de enige klasse die reparatie verdient); de knikken op de leiding-segmenten zijn OSM-waysegmentgrenzen/spikes in de bronleiding zelf, de vier op het zeebeen zijn krappe bochten in de MARNET-graaf (o.a. bij de Ryukyu-eilanden en de Straat van Hormuz-mond). `toets_rechte_benen.py --min-km 5` — 1 been gevonden (🟡 MIDDEL, stippel, omwegfactor 0,998, het gat-been): correct geclassificeerd als stippel-met-reden, geen bevinding op zichzelf. json geldig: versie 2, punt_formaat lonlat, modaliteiten `leiding`/`zee` (in de toegestane set), elk been ≥2 punten (332/2/522/1.199), bestandsgrootte **38,7 KB** (ruim < 300 KB).

**Gereedschapslessen:**
- `pyosmium` draait op deze machine zonder problemen (in tegenstelling tot een eerdere, gedateerde notitie in de projectgeschiedenis) — vijf specifieke way-ids uit een lokale Geofabrik-pbf halen en op eindpunt-nabijheid stikken kost een paar seconden en had geen Overpass-fallback nodig.
- De vijf OSM-waysegmenten kwamen in exact de volgorde en met exact de coördinaten die de briefschrijver al had opgegeven (via-punten 1–5) — de brief-aanwijzing bleek hier volledig betrouwbaar vóór het bakken, inclusief het interne kaarteringsgat van 17,3 km.
- Een brief-km die zichzelf al als "ontwerp/webcheck-schatting" markeert (geen gepubliceerde ladingroute-lengte) is een zwakke meetlat voor een lang zeebeen: +20,7% op zo'n schatting is eerder een correctie van de schatting dan een routefout, vooral op een traject van bijna 12.000 km waar de MARNET-route zichtbaar via Malakka meanderd i.p.v. de grote cirkel te volgen.
- Een leiding-eind dat exact op het anker staat en een zeebeen dat op de dichtstbijzijnde zeeknoop begint, geven een naad die precies gelijk is aan de eerder gemeten snap-afstand (10,47 km) — dit is geen bakfout maar het rechtstreekse gevolg van "zee snapt op de zeeknoop, niet op de kade" (handleiding §2); binnen de 25 km-norm blijft dit een geaccepteerde anker≠routeerpunt-bevinding.
