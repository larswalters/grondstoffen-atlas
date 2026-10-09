# Routebrief (licht) · olie — Omsk (Rusland) → Atasu (Kazachstan) → Dushanzi (China)

**stroom-id:** `olie-atasu-dushanzi` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** Russische transitolie (Omsk) en Kazachse olie stromen per **leiding** (Omsk–Pavlodar–Atasu, dan de
Kazakhstan–China-leiding Atasu–Alashankou, dan Alashankou–Dushanzi) naar de Dushanzi-raffinaderij (PetroChina, Karamay, Xinjiang). Geen zee.
**Welke as van het verhaal:** *de enige directe oliepijp van Centraal-Azië naar China — en het Russische transitdeel.*
Volume (peiljaar 2024): Atasu–Alashankou **~225 kb/d (11,2 Mt/j)** = ~10 Mt Russisch + ~1,2 Mt Kazachs (× 7,33 vaten/t ÷ 365) [1][2][3];
Alashankou–Dushanzi **max ~200 kb/d (10 Mt/j, capaciteit)** [1][9] — de brief claimt daar niet meer. Omsk–Atasu: ~10 Mt/j Russisch (~200 kb/d) [2][3].
⚠️ Het stroom-id noemt Atasu; de lijn begint (aannemelijk) bij Omsk — titel en kop zijn daarop aangepast, het id blijft.

## 1 · Ketenkaart
```
Omsk-pijpeinde `ol-omsk-kop` ──(b1 leiding · Omsk–Pavlodar–Shymkent-trunk · OSM 1.078,8 km, geen gepubliceerde km)──►
Atasu/Zhanaarka-pompstation `ol-atasu` ──(b2 leiding · Kazakhstan–China Pipeline LLP · 962,2 km OSM / 965 pub.)──►
Alashankou-meetstation `ol-alashankou` (CN/KZ-grens) ──(b3 stippel · naad 0,26 km)──(b4 leiding · CNPC · 237,6 km OSM / 246 pub.)──►
Dushanzi-raffinaderij `ol-dushanzi` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A0 | leiding | Omsk-pijpeinde → Atasu | Omsk–Pavlodar–Shymkent-trunk (Russische transit) | OSM 1.078,8 = 222,4 RU + 856,3 KZ; **geen gepubliceerde km voor dit stuk** [6] | OSM-ways 274735502 (RU) + 274735349 + 306438883 + 578833603 (KZ), naden 13 m / 0 / 0 — **aannemelijk** (één bron voor de route, Mapbox-way zonder naam) | nee |
| b2 | A | leiding | Atasu → Alashankou | Kazakhstan–China Oil Pipeline (KCP: KazTransOil + CNODC) | 962,2 OSM tegen 965 [2] / 987 [1]: −0,3% / −2,5% | OSM-way 269866896 (omgekeerd) | nee |
| b3 | — | leiding | Alashankou (naad) | — | 0,26 (OSM-naad tussen way 269866896 en 306288031) | rechte stippel | ja, 0,26 km |
| b4 | C | leiding | Alashankou → Dushanzi | Alashankou–Dushanzi-ruwe-olieleiding (CNPC) | 237,6 OSM tegen 246 [1]: −3,4% | OSM-ways 306288031 + 306295784 + 578818723 (omgekeerd) + 306295791 | nee |

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-omsk-kop` | kop van de Russische aanvoer | Omsk-pijpeinde bij het tankenpark | 55.0936, 73.2278 | [6][7] | aannemelijk (z15 gezien: open terrein ~0,3 km zuid van een groot tankenpark met tientallen witte tanks — het Omsk-raffinaderij/transportcomplex; geen bron noemt dit exacte punt) |
| `ol-atasu` | pompstation / kop KCP | Atasu/Zhanaarka-pompstation | 48.6513, 71.6150 | [1][6][7] | bron-gelegd (z15 gezien: tankenpark met 3–4 witte tanks + pompstation, meersporig emplacement ~0,5 km NW, dorp oostelijk) |
| `ol-alashankou` | grensmeetstation | Alashankou-meetstation (CN/KZ) | 45.1883, 82.5555 | [1][6][7] | bron-gelegd (z15 gezien: ommuurd tankenpark met 4 ronde tanks en rood dak, stad Alashankou direct zuidelijk) |
| `ol-dushanzi` | eind / raffinaderij | Dushanzi-raffinaderij (PetroChina) | 44.3678, 84.8488 | [4][6][7][9] | bron-gelegd (z15 gezien: klein ommuurd station tussen grote tankenparken en procesinstallaties — raffinagecomplex; poort/exacte unit niet te onderscheiden) |

⚠️ Het Alashankou-SPOORstation van `uranium-kharasan-alashankou` (45.1703, 82.5705) is NIET hergebruikt: ander object, 2,3 km zuidoostelijk.

## 4 · Via-punten
Geen: een leiding heeft geen corridorkeuze en elk been is vooraf gebakken uit OSM. De segmentgrenzen staan in §9 van de bak-agent.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Atasu/Zhanaarka | KazTransOil / Transneft-aanvoer; KCP | Russische transit + Kumkol–Atasu → KCP-hoofdleiding | 20 Mt/j ontwerp (praktisch iets > 10) [2][3] | [1][2][3] |
| Alashankou-meetstation | Kazakhstan-China Pipeline LLP / CNPC | KCP → CNPC-leiding naar Dushanzi | 10 Mt/j (Alashankou–Dushanzi) [1] | [1][9] |
| Dushanzi-raffinaderij | PetroChina (CNPC) | ruwe olie → producten | 10 Mt/j (~200 kb/d) raffinage [9] | [9] |

## 6 · Stoppunt
De brief stopt bij de Dushanzi-raffinaderij (OSM-pijpeinde in het complex): daarna zijn producten naar markten niet aan één bron te koppelen; fase D/E vervallen.

## 7 · Open punten
- **b1 (Omsk → Atasu) is aannemelijk:** één bron (Wikipedia: Russische olie komt via Omsk–Pavlodar–Shymkent bij Zhanaarka binnen) [1]; de OSM-lijn heeft geen naam (Mapbox-bron) en geen gepubliceerde km, het exacte Omsk-eindpunt is een pijpeinde bij het tankenpark. De ±15%-toets is hier niet te doen; de lijn passeert Pavlodar op 13,7 km.
- Times of Central Asia noemt alleen Atasu–Alashankou, niet Omsk/Pavlodar [2]; Rusland wil +2,5 Mt (Transneft-voorstel 2025) [3]. Volumes zijn 2024; geen 2025/2026-bevestiging.
- Gepubliceerde lengtes zijn inconsistent (965 / 987 / 2.228 / 2.798 km, per stuk); OSM-som Atasu → Dushanzi 1.200,1 km (Wikipedia: 987 + 246 = 1.233).
- Way 578818723 (20,9 km, 3 punten) draagt `fixme=replace` in OSM: rechte lijn tussen twee echte punten, geometrie te grof.
- Kazachse bijvoeding (Atyrau–Kenkiyak–Kumkol, 2.820 km in OSM) is niet getekend: ~1,2 Mt/j, buiten het ontwerp.
- Het Wikipedia-districtscoördinaat Dushanzi (45.6, 84.87) is onbruikbaar (45 km noordelijk); het OSM-pijpeinde is gebruikt.

## 8 · Bronnen
[1] Wikipedia, "Kazakhstan–China oil pipeline" — https://en.wikipedia.org/wiki/Kazakhstan%E2%80%93China_oil_pipeline (Zhanaarka–Alashankou 987 km, 20 Mt/j; Alashankou–Dushanzi 246 km, 10 Mt/j; Omsk–Pavlodar–Shymkent sluit bij Zhanaarka aan)
[2] Times of Central Asia, 01-08-2025 — https://timesca.com/russia-seeks-to-boost-oil-transit-to-china-via-kazakhstan/ (~10 Mt Russisch in 2024; Atasu–Alashankou 965 km, 20 Mt/j)
[3] GIS Reports, "Kazakhstan strategic crossroads" — https://www.gisreportsonline.com/r/kazakhstan-strategic-crossroads/ (2024: ~10 Mt Russisch + 1,2 Mt Kazachs; +2,5 Mt voorstel 2025)
[4] Wikipedia, "Dushanzi District" — https://en.wikipedia.org/wiki/Dushanzi_District (districtscoördinaat 45.6/84.87, niet de raffinaderij)
[5] GEM.wiki, "Kazakhstan–China Oil Pipeline" — https://www.gem.wiki/Kazakhstan%E2%80%93China_Oil_Pipeline (Atasu–Alashankou 965 km, 813 mm, 20 Mtpa, KazTransOil 50% + CNODC 50%)
[6] OpenStreetMap (ODbL), Geofabrik-extracts kazachstan, china, rusland-siberie; eigen PBF-scan (pyosmium geblokkeerd) 2026-10-09 — man_made=pipeline, substance=oil; way-id's in §2
[7] Esri World Imagery via v2/tools/sat_check.py (z15): sat-olie-atasu-dushanzi-omsk-kop / -atasu-kop / -alashankou-meetstation / -dushanzi-eind / -grens-ru-kz (z14)
[8] KazTransOil, Pavlodar–Shymkent 1.640,4 km — https://kaztransoil.kz/en/press_centre/news/5077-kaztransoil-jsc-connects-new-11-km-section-of-the-pavlodar-shymkent-main-oil-pipeline-bypassing-the-village-of-shubarssu
[9] Oil & Gas Journal, "China to boost refining capacity, import Kazakh oil" — https://www.ogj.com/refining-processing/article/17235666/china-to-boost-refining-capacity-import-kazakh-oil (Dushanzi 10 Mt/j, ~200 kb/d, Kazachs zwavelrijk ruw)
[10] GEM.wiki, Shymkent–Chardzhou — https://gem.wiki/Shymkent-Chardzhou_Oil_Pipeline (Surgut–Omsk–Pavlodar–Shymkent > 3.000 km)

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Recept:** `bash v2/tools/bak_stromen.sh olie-atasu-dushanzi` (functie `bak_olie_atasu_dushanzi`, LF) -> `v2/data/stroomroute-olie-atasu-dushanzi.json` (18,7 KB). Alle drie leidingbenen zijn vooraf gebakken FeatureCollections uit OSM `man_made=pipeline` (eigen pure-python PBF-scan `olie-atasu-dushanzi-pbfscan.py`, pyosmium geblokkeerd) in `v2/build-cache/ais/graaf/olie-atasu-dushanzi-leiding-*.geojson`.

| # | modaliteit | been | km | punten | stippel |
|---|---|---|---|---|---|
| 1 | leiding | Omsk-pijpeinde -> Atasu/Zhanaarka (aannemelijk) | 1.078,8 | 368 | nee |
| 2 | leiding | Atasu -> Alashankou (way 269866896, omgekeerd) | 962,2 | 328 | nee |
| 3 | leiding | Alashankou-naad tussen twee OSM-ways | 0,3 | 2 | ja, 0,26 km |
| 4 | leiding | Alashankou -> Dushanzi (vier ways) | 237,6 | 202 | nee |

**Totaal 2.278,9 km · 900 punten · 4 markers** (ol-omsk-kop, ol-atasu, ol-alashankou, ol-dushanzi). Naden tussen benen 0,00 km (max 0,26 km = de bewuste stippel); markers 3-5 m van hun lijn; geen zee, geen haven-aanloop, geen wegbeen, geen via-punten, geen kopie van een andere stroom, geen vlucht.

**Toets.** Km tegen de brief: b2 962,2 tegen 965 (-0,3%) / 987 (-2,5%); b4 237,6 tegen 246 (-3,4%); b1 heeft geen gepubliceerde km (alleen OSM 1.078,8), dus geen +-15%-toets, indicatie via de lijn die Pavlodar op 13,7 km passeert. `toets_knikken`: 0 omkeringen, 0 terugloop; 12 knikken >= 60 graden over de hele leiding, normaal voor een pijpleiding die de OSM-tracering volgt, waarvan 1 spike (85,9 graden, R 132 m) bij 48,6527/71,6138 vlak voor het Atasu-anker op het einde van b1 (de aansluiting op het pompstation, niet gerepareerd). `toets_rechte_benen --min-km 5`: geen vlag voor deze stroom. json.load slaagt, versie 2, punt_formaat lonlat, modaliteit alleen leiding, elk been >= 2 punten.

**Stippel b3 (0,26 km).** Geen gat in het net maar een OSM-naad: de KCP-way 269866896 eindigt op 45.18834/82.55547 en de CNPC-way 306288031 begint op 45.18645/82.55350, beide in het Alashankou-meetstation. Rechte stippel, geen gedeelde node in OSM; blijft staan als procesgat binnen de knoop.

**Lessen.** (1) Het stroom-id noemt Atasu maar de lijn begint bij Omsk; titel en kop zijn daarop aangepast, het id blijft. (2) b1 blijft aannemelijk (een bron, naamloze Mapbox-way); de rest is door OSM, de gepubliceerde km en de satelliet gedekt. (3) Way 578818723 (20,9 km, 3 punten) heeft `fixme=replace`: rechte lijn, geometrie te grof, niet verbeterd. (4) Een keten die helemaal uit OSM-leiding bestaat bakt in een paar seconden: de tijd zit in het voorbakken van de ways, niet in `hecht_marnet.py`.

**Registerregel (centraal):** `{ sleutel: "olie-ad", bestand: "stroomroute-olie-atasu-dushanzi.json", grondstof: "olie", label: "Omsk -> Dushanzi", aan: true, noot: "M31 · golf 8 (2026-10-09): Russische transitolie en Kazachse olie per leiding van Omsk via Atasu en Alashankou naar de Dushanzi-raffinaderij." }`
