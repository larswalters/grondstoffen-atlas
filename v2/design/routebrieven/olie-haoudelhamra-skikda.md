# Routebrief (licht) · olie — Haoud el Hamra → OK1-leiding → Skikda (Algerije)

**stroom-id:** `olie-haoudelhamra-skikda` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) · **status:** gebakken
**Keten in één zin:** Saharan Blend-ruwe olie uit het Hassi Messaoud-veld, per **leiding** vanaf het tankenpark van Haoud el Hamra
over de Sonatrach-hoofdleiding OK1 (34 inch, 1972) door de Atlas en de Constantine-regio naar de Sonatrach-terminal/raffinaderij van Skikda aan de Middellandse Zee.
**Welke as van het verhaal:** *Algerije: Sahara-crude naar de Middellandse Zee* — de OK1 is naast Arzew (OB1) en Bejaia de oostelijke exportader; GEM geeft
30 Mt/j nameplate (~600 kb/d), Saharan Blend totaal ~476 kb/d (Argus, dec 2025). Het aandeel Skikda en de werkelijke OK1-stroom zijn niet gepubliceerd (§7).

## 1 · Ketenkaart
```
Haoud el Hamra `ol-haoud-kop` ──(b1 leiding · OSM-way 379118067 (ongetagd: OK1 of NK1) · 555,8 km, doorgetrokken)──►
  OSM-eind 36.2508,6.4205 ──(b2 leiding · stippel 84,2 km, OK1 niet in OSM)──► Skikda-terminal `ol-skikda-term` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Haoud el Hamra → OSM-eind 36.2508,6.4205 | OK1 (Haoudh El Hamra–Skikda, 34 inch), Hassi Messaoud – Atlas – Constantine-regio; de way is ongetagd, zie §7 | OSM 555,8 [5]; gepubliceerd 646 (GEM) / 645-646 (P&GJ) [1][2] | OSM-way 379118067 (`man_made=pipeline`, `substance=oil`, operator Sonatrach, 273 knopen), letterlijk doorgetrokken | nee |
| b2 | A | leiding | OSM-eind → Skikda-terminal | laatste stuk OK1 naar de kust, niet in OSM | 84,2 hemelsbreed (geen leidingkm) [5] | geen OSM-way | ja, "hier reikt het net niet" |
Totaal b1+b2 = 640,0 km tegen 646 (GEM) = **-0,9%** (alleen indicatie: het stippelstuk is hemelsbreed). Geen zeebeen: de brief stopt in Skikda (bindend, §6), dus geen haven-aanloop.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-haoud-kop` | kop van de leiding / tankenpark Hassi Messaoud-olie | Haoud el Hamra, begin OSM-way 379118067 | 31.8836, 5.9903 | [5][7] | bron-gelegd (z15 gezien: groot tankenpark met ~30 ronde tanks, pompstation- en procesterreinen aan de oostrand, leidingstroken dwars door de woestijn; de OSM-way begint op de oostelijke rand van het complex) |
| `ol-skikda-term` | ontvangst leiding / tankenpark + raffinaderij (stoppunt) | Skikda Sonatrach-terminal/raffinaderij (tankenzone) | 36.8625, 6.9760 | [3][6][7] | aannemelijk (z15 gezien: aaneengesloten tankenpark met drijvende-dak-tanks en procesinstallaties; OSM kent daar 31 `storage_tank`-ways in de zone "Zone Industrielle Pétrochimique Sonatrach"; geen bron noemt het ontvangstpunt van de OK1 exact) |
Geen bestaand anker te hergebruiken: de olie-sitelaag heeft geen Algerije-site; `w-skikda` in de gas-sitelaag is de LNG-installatie op stadsniveau (36.8667, 6.9) en geen anker.

## 4 · Via-punten (alleen b1 — leiding, geen corridorkeuze; punten zijn OSM-lijnpunten ter controle, geen routeringsinvoer)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | ~100 km | 32.7502, 5.8087 | ver van elk ander tracé, Hassi Messaoud – Laghouat-regio [5] |
| b1 | 2 | ~200 km | 33.6236, 5.7605 | idem [5] |
| b1 | 3 | ~300 km | 34.5262, 5.6100 | idem, Atlas [5] |
| b1 | 4 | ~400 km | 35.2503, 5.3923 | westelijkste punt van de lijn [5] |
| b1 | 5 | ~500 km | 35.8914, 6.0047 | de lijn buigt naar het noordoosten richting Constantine [5] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Skikda-raffinaderij (RA1K) + terminal | Sonatrach | OK1-ruwe olie → raffinage / tankopslag → tanker | raffinaderij ~300 kb/d [4]; OK1 nameplate 30 Mt/j ≈ 600 kb/d [1] | [1][4] |

## 6 · Stoppunt
De brief stopt bij de Skikda-terminal: geen bron koppelt een OK1-lading aan één afnemer of tanker (Saharan Blend wordt ook in Arzew en Bejaia geladen en breed verkocht);
fase D/E vervallen, zonder zeebeen. Volume: Saharan Blend-export 375 kb/d (2021) en 476 kb/d (dec 2025) volgens Argus [3]; OK1 nameplate ~600 kb/d [1];
peiljaar 2025, eenheid kb/d, het Skikda-aandeel is onbekend.

## 7 · Open punten
- **Welke leiding is OSM-way 379118067?** Hij draagt alleen `substance=oil` en operator Sonatrach, geen naam of ref. Naast OK1 (34 inch, 1972) bestaat NK1 (30 inch, condensaat, 2009), beide ~646 km;
  de corridor klopt in beide gevallen, de beennaam noemt OK1 met die noot (haalbaarheidstoets [8]).
- **Staartgat van 84,2 km:** OSM eindigt bij 36.2508,6.4205 (satelliet: open akker naast een autoweg, geen station). Een aantal ongetagde `man_made=pipeline`-ways in de regio (o.a. 371660347, 1121190736) is
  niet als OK1 te bewijzen en niet gebruikt; de GK-gasleiding (way 379118074, `substance=gas`) loopt naar Skikda maar is een ander product.
- **Skikda-ankerpunt aannemelijk, niet bron-gelegd:** de exacte ontvangstplek van de OK1 (tankenpark of de raffinaderij-ingang) staat in geen bron; het punt ligt in het OSM-tankenpark.
- **Aandeel Skikda en werkelijke OK1-stroom niet gevonden;** alleen nameplate en Saharan Blend-totalen. Saharan Blend laadt ook in Arzew en Bejaia.
- **Geen afnemer na Skikda** (geen zeebeen, geen fase D/E).

## 8 · Bronnen
[1] GEM.wiki, "Haoudh El Hamra-Skikda Oil Pipeline" (OK1, 646 km, 34 inch, 30 Mt/j, 1972, operating, Sonatrach). https://www.gem.wiki/Haoudh_El_Hamra-Skikda_Oil_Pipeline
[2] Pipeline & Gas Journal, 09-2020, "Sonatrach reports two leaks on OK1 oil pipeline" (645-646 km; start uit het ketenontwerp, de pagina gaf nu 404). https://pgjonline.com/news/2020/09-september/sonatrach-reports-two-leaks-on-ok1-oil-pipeline
[3] Argus Media, Algerijnse Saharan Blend-export (375 kb/d in 2021; 476 kb/d dec 2025; Arzew en Bejaia als overige laadhavens), via een zoekresultaat, niet zelf gelezen. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2664855-algeria-s-feb-crude-exports-up-nearly-a-third
[4] Wikipedia, "Sonatrach" (Skikda-raffinaderij 300 kb/d; >3.900 km ruwe-oliepijpleidingen vanaf Hassi Messaoud). https://en.wikipedia.org/wiki/Sonatrach
[5] OpenStreetMap (ODbL), eigen scan 2026-10-28 op de lokale Geofabrik-extract `algerije`: way 379118067, 555,8 km, 273 knopen, van 36.25076,6.42047 naar 31.88359,5.99027; staartzone 36.2-37.0N/6.3-7.2E doorzocht op andere oliepijpen (geen).
[6] OpenStreetMap, zelfde extract: 31 `storage_tank`-ways bij 36.855-36.867N/6.973-6.982E en "Zone Industrielle Pétrochimique Sonatrach" (way 228946619, 36.8751/6.9408). https://www.openstreetmap.org/way/228946619
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-olie-haoudelhamra-skikda-haoud.png`, `…-skikda.png`, `…-eind-osm.png` (OSM-eind, open akker).
[8] Haalbaarheidstoets keten `olie-haoudelhamra-skikda` (orkestrator, 2026-10-28): GEM OK1/NK1, tankenpark als OSM-begin, Skikda-punt 36.8625,6.9760.
[9] Wikipedia, "Skikda" (36.867N/6.900E, olie- en gasterminal in de haven, petrochemisch complex). https://en.wikipedia.org/wiki/Skikda
[10] Rigzone, "What are Algeria's contributions to global oil markets" (Centraal-Sahara-productie via trunklines naar Arzew, Skikda en Bejaia). https://www.rigzone.com/insights/emerging-trends-and-technology-6/what-are-algerias-contributions-to-global-oil-markets-802/

## 9 · Gebakken (2026-10-28, lichte werkwijze, M31 golf 10)
**Bestand:** `v2/data/stroomroute-olie-haoudelhamra-skikda.json` (6,0 KB, versie 2, lonlat) · functie `bak_olie_haoudelhamra_skikda()` in `v2/tools/bak_stromen.sh` · geen profiel (geen wegbeen).
| # | modaliteit | km gebakken | punten | stippel | naad naar vorig been |
|---|---|---|---|---|---|
| b1 | leiding | 555,8 | 273 | nee, doorgetrokken | - |
| b2 | leiding | 84,2 | 2 | ja, net reikt niet | 5 m |
Totaal 640,0 km tegen 646 gepubliceerd (-0,9%, indicatie: b2 is hemelsbreed). Markers: `ol-haoud-kop` 3 m en `ol-skikda-term` 0 m van de lijn. Geen naad > 5 km.
**Recept:** `python -I -X utf8 v2/tools/maak_leidingbeen_olie_haoudelhamra_skikda.py --schrijf` haalt OSM-way 379118067 uit `algerije-latest.osm.pbf` (1,9 s, kop 3 m van het anker) en schrijft de FeatureCollection `v2/build-cache/ais/graaf/olie-haoudelhamra-skikda-leiding-ok1.geojson`; daarna `bash v2/tools/bak_stromen.sh olie-haoudelhamra-skikda` (b1 via `--been-geojson`, b2 via `--stippel`, 2 markers).
**Toelichting:** b1 is letterlijk de OSM-way, lengte 555,8 km gelijk aan de brief. b2 is een rechte stippel van 84,2 km tussen het OSM-eind en het Skikda-anker: de OK1 is daar niet gekarteerd, de km is hemelsbreed en geen leidingkm. Geen zeebeen, geen haven-aanloop, geen vlucht, geen spoor, geen via-punten, geen gedeelde benen.
**Toets:** `toets_knikken.py` 1 knik (69,9 graden, R 63 m, 35.8248,5.9405, in de OSM-geometrie zelf; geen omkering, geen terugloop). `toets_rechte_benen.py` meldt alleen b2 (stippel met reden, hoort recht). json.load goed, modaliteiten {leiding}, elk been >= 2 punten.
**Lessen:** (1) de OSM-way heeft `layer=-1` en `location=underground` en een Arabische operator-tag, dus de naam kwam uit de brief en niet uit OSM; (2) een enkele way op id ophalen is een script van 1 s, geen component-graaf nodig; (3) beennaam noemt OK1 of NK1 omdat de way ongetagd is.
