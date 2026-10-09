# Routebrief (licht) · olie — Unecha (Rusland) → Druzhba-1 via Wit-Rusland, Oekraïne en Slowakije → MOL Duna, Százhalombatta (Hongarije)

**stroom-id:** `olie-unecha-szazhalombatta` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** Russische transitolie (Urals/REB) per **leiding** — Druzhba-hoofdstreng van het Unecha-knooppunt (Bryansk) via
Wit-Rusland naar de Mozyr-splitsing, de zuidtak door Oekraïne (Brody, Karpaten) en de Druzhba-1-tak door Slowakije (Ipeľ) naar de MOL
Duna-raffinaderij bij Százhalombatta, 1.395 km OSM-som in vier benen, zonder zee.
**Welke as van het verhaal:** *de laatste Russische landroute naar de EU* — Hongarije en Slowakije krijgen als enige nog Russische ruwe
olie per leiding. **~165 kb/d (mei 2026, Hongarije + Slowakije samen)**, tegen 200–235 kb/d vóór de onderbreking van 27-1 tot 23-4-2026
(Russische drone-aanval bij Brody) [3][2]; peiljaar 2026. Aandeel Hongarije alleen: niet gevonden. De Duna-raffinaderij is op Russische
blend gebouwd (MOL: andere kwaliteiten hooguit ~35%) [5][6].

## 1 · Ketenkaart
```
Unecha-knooppunt `ol-unecha-kop` ──(a1 leiding · Druzhba-hoofdstreng RU/BY · 282,7 km OSM-som)──► Mozyr-splitsing `ol-mozyr-splitsing`
  ──(a2 leiding · Druzhba Mozyr→Brody, BY/UA · 394,0 km, één way)──► Brody-knooppunt `ol-brody-hub`
  ──(a3 leiding · Druzhba Brody→Karpaten→Mukachevo-zuid→SK/UA-grens bij Budince · ~319 km OSM-som incl. 13 naden)──►
  SK/UA-grensknoop (via-punt, geen anker) ──(a4 leiding · Transpetrol Slowakije via Ipeľ → Barátság I · 399,6 km, 2 naden)──►
  MOL Duna-raffinaderij `ol-mol-duna` (Százhalombatta) ── stoppunt
```
Dit is **Druzhba-1 via Slowakije**. De directe **Druzhba-2** via Mukachevo → Záhony → Hongaarse Barátság II (naar Tiszaújváros en Százhalombatta)
is gekarteerd en korter (1.278,8 km) maar wordt **niet getekend**; de naïeve kortste-pad-stik zou hem kiezen en moet hem dus uitsluiten.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| a1 | A | leiding | Unecha-knooppunt → Mozyr-splitsing | Druzhba-hoofdstreng Unecha → Klimavichy → Gomel-regio → Mozyr (Transneft / Gomeltransneft Druzhba) | 282,7 **OSM-som, geen bronlengte** [7][8] | OSM-ways 314285969, 137838986, 314286194, 314287482, 274735180, 1227331716, 274735017 | nee |
| a2 | A | leiding | Mozyr-splitsing → Brody-knooppunt | Druzhba zuidtak Mozyr → Brody (Gomeltransneft / UkrTransNafta) | 394,0 OSM, één way, geen bronlengte [7] | OSM-way 274735521 'Дружба Броди-2' (doorloopt de grens BY→UA) | nee |
| a3 | A | leiding | Brody-knooppunt → SK/UA-grensknoop bij Budince | Druzhba Brody → Karpaten → Mukachevo-zuid → Slowaakse grens | ~319 OSM-som incl. 13 naden (13,1 km) [8] | OSM-ways 580531824, 225572946, 882145409, 882145415, 875106707, 875106699, 580531828, 923057409 (+ korte tussenways) | nee — naden ≤1,5 km gestikt, geen stippel |
| a4 | A | leiding | SK/UA-grensknoop → Százhalombatta | Druzhba-1: Transpetrol Slowakije → Ipeľ → grens Drégelypalánk → MOL Barátság I | 399,6 OSM-som; Hongarije-deel 129,5 tegen **130 gepubliceerd** (−0,4%) [1][7] | OSM-ways 564620618 (201,3), 793405601 (68,2), 580260776 (129,5); naad 0,6 km bij de grens | nee |

Geen leg B/C/D/E: de pijp eindigt in de raffinaderij; geen bron noemt een vervolg dat deze keten aan een eindafnemer koppelt.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-unecha-kop` | kop van de keten (Druzhba-knooppunt) | Unecha-knooppunt, Bryansk (RU) — OSM-eindknoop van way 314285969; stadscentroïde 52,8461/32,6767 is géén anker | 52.7649, 32.6805 | [7][9] | aannemelijk (z15 gezien: brede leidingstrook kruist het punt in bos; een omheind tankenpark van ~10 tanks ligt 0,8 km ZO — vermoedelijk het pompstation, niet bevestigd; binnen 2 km, dus geen stippel) |
| `ol-mozyr-splitsing` | splitsing noord-/zuidtak | Mozyr-knooppunt (BY) — OSM-knoop tussen way 274735017 en 274735521 | 51.9206, 29.2628 | [1][7] | bron-gelegd (z15 gezien: tankenpark van ~15 tanks met pompgebouwen en leidingstrook, punt ligt midden in het terrein) |
| `ol-brody-hub` | overslag/hub (aansluiting Odesa–Brody) | Brody-knooppunt (UA) — OSM-knoop tussen way 274735521 en 580531824; plaatscentroïde 50,0831/25,1477 is géén anker | 50.0660, 25.1261 | [1][2][7] | bron-gelegd (z15 gezien: tankenpark met pompstation aan de westrand van Brody, punt op de zuidoostrand van het terrein; in jan-2026 drone-schade [2]) |
| `ol-mol-duna` | eindpunt / losplek raffinaderij | MOL Duna-raffinaderij, Százhalombatta (HU) — OSM-eindknoop van way 580260776 | 47.2879, 18.9072 | [5][7] | bron-gelegd (z15 gezien: pijpeinde in bos aan de oostrand van het tankenpark, ~150 m van de dichtstbijzijnde tanks, de Donau 0,3 km oostwaarts; procesinstallaties ~1 km WZW) |

## 4 · Via-punten (stik-knopen; alleen waar een corridorkeuze of een way-overgang de streng vastlegt — geen wegbeen)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| a1 | 1 | aansluiting op de hoofdstreng | 52.7474, 32.7678 | way 314285969 is een 6,4 km spur van het Unecha-knooppunt naar de doorgaande streng; vanaf hier gaat way 137838986 west |
| a1 | 2 | Gomel-regio, way-overgang | 52.1825, 29.8869 | kiest de Gomeltransneft-streng boven eventuele parallelle leidingen in Wit-Rusland |
| a3 | 3 | Karpaten, eerste naad | 49.0376, 23.5260 | begin van de 13 naden (0,05–1,49 km); stik met tolerantie 1,5 km |
| a3 | 4 | Mukachevo-zuid, splitsing Druzhba-1 / -2 | 48.4680, 22.7456 | **de corridorkeuze**: way 923057409 gaat naar Slowakije, way 580412172 (Barátság II) naar Záhony; sluit alle Barátság-II-ways uit |
| a3/a4 | 5 | SK/UA-grensknoop bij Budince | 48.5418, 22.1594 | uiteinde a3 = begin a4 (way 564620618); 0 m naad. NB: het dorp Budkovce ligt op 48,63/21,93, ~20 km NW [9] |
| a4 | 6 | Slowakije, way-overgang | 48.3077, 19.6899 | 564620618 → 793405601, naad 0,03 km; sluit aan op de Ipeľ-tak (Wikipedia: Druzhba-1 takt af bij de Ipeľ) |
| a4 | 7 | SK/HU-grensnaad | 48.1035, 18.8887 → 48.1003, 18.8956 | 793405601 → MOL 580260776 (Barátság I), naad 0,6 km bij Drégelypalánk; sluit uit: 566241458 (Barátság II) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| MOL Duna-raffinaderij, Százhalombatta | MOL Nyrt. | Russische REB via Druzhba-1 (en -2) → producten | 8,1 Mt/j ≈ **163–165 kb/d** [5][6]; CDU AV-3 brand 20-10-2025, herstel klaar 22-9-2026, gefaseerde herstart vanaf oktober 2026 [5] | [5][6] |
| Mozyr / Brody (pompstations, hubs) | Gomeltransneft Druzhba / UkrTransNafta | doorvoer, geen verwerking | geen apart cijfer gevonden | — |

## 6 · Stoppunt
De brief stopt bij de MOL Duna-raffinaderij: de pijp eindigt daar, het product wordt in Hongarije verwerkt en verkocht, en geen bron koppelt deze lading aan een specifieke eindafnemer. Het upstream-deel (Almetyevsk → Unecha, Wikipedia) en de
noordtak vanaf Mozyr (Polen/Duitsland) zijn niet deze keten en worden niet getekend.

## 7 · Open punten
- **Druzhba-2 niet getekend** (Mukachevo → Záhony → Barátság II, 1.278,8 km kortste pad, OSM-ways 580412172, 993324535, 580412171, 1154984406, 566241458); Tiszaújváros (MOL Tisza, einde way 580412171 op 47,8753/20,9973) is een open punt en geen anker.
- **Anker-benaming:** het ontwerp noemde 48,5418/22,1594 "Budkovce-pompstation"; dat is de SK/UA-grensknoop bij Budince/Ruská (z15: open akkerland langs een rechte N–Z-strook). Het pompstation Budkovce zelf (dorp op 48,63/21,93) is niet als punt gevonden, dus niet getekend.
- **Unecha is een OSM-knoop**, geen satelliet-bevestigd pompstation; of het tankenpark 0,8 km ZO de LPDS Unecha is, is niet bevestigd.
- **Geen bronlengte** voor a1–a3 (alleen OSM-som); de ±15%-toets is daar een indicatie. Parallelle leidingen (Wit-Rusland, Karpaten) kunnen maken dat het kortste pad niet de actieve strang is.
- **Flowstatus:** laatste bevestiging mei 2026; geen nieuwer bericht gevonden. Het MOL-herstel na de brand (AV-3) loopt tot oktober 2026, dus de raffinaderij draait niet op volle sterkte in het peiljaar.
- Slowaakse tak naar Slovnaft (Bratislava; OSM-ways 801992210, 1030213900) is niet getekend. Pyosmium is op deze machine door een beleid geblokkeerd (zie bak-noot).

## 8 · Bronnen
[1] Wikipedia, "Druzhba pipeline" — route (Almetyevsk → Mazyr, zuidtak via Brody, splitsing bij Uzhhorod, Druzhba-1 via Ipeľ en Drégelypalánk naar Százhalombatta, Unecha-knooppunt). https://en.wikipedia.org/wiki/Druzhba_pipeline
[2] Wikipedia, "2026 Druzhba pipeline dispute" — stilstand 27-1-2026 (drone bij Brody), herstel 23-4-2026. https://en.wikipedia.org/wiki/2026_Druzhba_pipeline_dispute
[3] UNITED24 Media, 4-6-2026, naar Reuters 3-6-2026 — mei 2026 ~165 kb/d (HU + SK), vóór de onderbreking 200–235 kb/d, april ~55 kb/d. https://united24media.com/world/russian-oil-returns-to-hungary-and-slovakia-as-druzhba-pipeline-operations-stabilize-19496
[4] Reuters, 23-4-2026, flow naar Slowakije hervat (ontwerp-startbron; niet zelf geopend). https://www.reuters.com/business/energy/druzhba-oil-flow-slovakia-resumed-early-thursday-slovak-ministry-says-2026-04-23/
[5] Oil & Gas Journal, 25-9-2026, "MOL wraps repairs on major unit at Hungarian refinery" — 8,1 Mt/j (~163 kb/d), AV-3 brand 20-10-2025, herstel 22-9-2026. https://www.ogj.com/refining-processing/news/55407912/mol-wraps-repairs-on-major-unit-at-hungarian-refinery
[6] Zoekresultaat-samenvatting (2026-10-09) — Duna ~165 kb/d, IEA 162 kb/d, MOL: Russische olie 100% via Druzhba, andere blends hooguit 35%; IEA-pagina gaf 401 en is niet geopend. https://prod.iea.org/articles/hungary-oil-security-policy
[7] OpenStreetMap (ODbL) — way-geometrie via api.openstreetmap.org/api/0.6/way/<id>/full voor de 12 ways in a1, a2 (274735521) en a3 (580531824) / a4: lengtes en eindcoördinaten gemeten 2026-10-09. https://www.openstreetmap.org
[8] Eigen endpoint-graaf (golf-7-scan van de Geofabrik-extracts oekraine/slowakije/hongarije; naadtolerantie 1,5 km, Barátság-II-ways uitgesloten) — a3 319,7 km met 13 naden (13,1 km), a4 399,6 km met 2 naden (0,65 km); controle op de haalbaarheidstoets (1.395 km). Intern.
[9] Wikipedia-coördinaten: Unecha 52,8461/32,6767, Budkovce 48,63/21,93, Budince 48,53/22,15, Százhalombatta 47,3004/18,9136. https://en.wikipedia.org/wiki/Budince
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-olie-unecha-szazhalombatta-{unecha,mozyr,brody,budkovce,molduna}.png`.

## 9 · Bak-noot (door de bak-agent)

### Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
Bestand `v2/data/stroomroute-olie-unecha-szazhalombatta.json` (versie 2, `lonlat`, 38,5 KB) · functie `bak_olie_unecha_szazhalombatta()` in
`v2/tools/bak_stromen.sh` · stik-script `v2/tools/maak_leidingbeen_olie_unecha_szazhalombatta.py` · geen profiel in `maak_stroombeen_weg.py`
(geen wegbeen) · geen zee, geen haven-aanloop, geen stippel, geen luchtbeen.

| # | modaliteit | van → naar | gemeten km | brief (OSM-som) | punten | naad naar volgend been |
|---|---|---|---|---|---|---|
| a1 | leiding | Unecha → Mozyr | 282,7 | 282,7 | 328 | 0 m |
| a2 | leiding | Mozyr → Brody | 394,0 | 394,0 | 375 | 0 m |
| a3 | leiding | Brody → Karpaten → Mukachevo-zuid → SK/UA-grens | 320,6 | ~319 | 484 | 0 m |
| a4 | leiding | SK/UA-grens → MOL Duna | 389,3 | 399,6 | 728 | — |
| | | **totaal** | **1.386,6** | ~1.395 | 1.915 | geen stippel |

**Markers (4, 3–5 m van de lijn):** `ol-unecha-kop` 52.7649,32.6805 · `ol-mozyr-splitsing` 51.9206,29.2628 · `ol-brody-hub` 50.0660,25.1261 · `ol-mol-duna` 47.2879,18.9072.
De SK/UA-grensknoop 48.5418,22.1594 is een via-punt (uiteinde a3 = begin a4, node 8568721963), geen marker.

**Recept.** pyosmium is geblokkeerd, dus de geometrie komt per way-id uit de OSM-API (`ways.json` + `nodes.json`, ODbL, cache
`olie-unecha-szazhalombatta-osmapi-cache.json`) en wordt gestikt op **gedeelde OSM-nodes** (verbonden ⇔ gedeelde node) in een vaste, expliciete
way-volgorde — geen vrij kortste pad, want dat kiest Druzhba-2 via Záhony (1.278,8 km). Uitgesloten: 580412172, 993324535, 580412171,
1154984406, 566241458, 524599878, 1051144390, 553875773, 1429407850, 579799445, 243984479. Uitvoer `v2/build-cache/ais/graaf/olie-unecha-szazhalombatta-leiding-a1..a4.geojson`,
bake via `bash v2/tools/bak_stromen.sh olie-unecha-szazhalombatta`.

**Toets (handleiding §5).** Geen naad > 0 m (alle benen en alle ways sluiten op gedeelde nodes) · geen stippel · `toets_knikken.py`: 26 knikken ≥ 60°,
**0 omkeringen** (de knikken zijn de OSM-polylijn zelf, o.a. spikes van 10 m op overground-stukjes in de Karpaten) · `toets_rechte_benen.py --min-km 5`: geen
recht been in deze stroom · json: versie 2, `lonlat`, alle benen `leiding` met ≥ 2 punten · km-toets: alleen de Hongaarse helft heeft een bronlengte
(125,0 km na de join tegen 130 gepubliceerd, **−3,8%**; zonder join zou het 129,5 zijn, −0,4%). a1–a3 hebben geen bronlengte: de OSM-som ís de maat en de ±15%-toets is daar leeg.

**Toelichting per afwijking van het ontwerp.**
- **De 13 "naden" van a3 (13,1 km) bestaan niet.** De ontwerp-scan zag de korte overground/underground-stukjes in de Karpaten (882141768–83, 882145406–15, 875106699–716,
  880564101–04, 1267221088–91) niet allemaal; met alle 56 ways van de keten zijn ze onderling via gedeelde nodes verbonden. Er is dus niets "gestikt met tolerantie 1,5 km", a3 heeft nul naden en
  de eerste Karpaten-"naad" van het ontwerp is gewoon een kort stukje way (225572946 → 882145406).
- **a4-join bij Ipeľ (afwijking van de brief-naad van 0,6 km).** Way 793405601 (Slowaaks) en 580260776 (Hongaars) zijn dezelfde buis twee keer gekarteerd, ~40 m uit elkaar, over
  ~4,5 km vlak voor de grens; 793405601 loopt bovendien nog 1 km voorbij en keert via een spur terug. Met de brief-naad zou de lijn daar ~9 km heen-en-weer tekenen (180°-omkeringen).
  Het stik-script kapt 793405602/793405601 op het eerste punt binnen 100 m van de Hongaarse lijn (48.0881,18.9444) en vervolgt op 580260776 vanaf het dichtstbijzijnde punt
  (48.0873,18.9446): join **84 m**, weggelaten 5,3 km Slowaaks staartje en 4,5 km Hongaars kopstuk (dubbele kartering). a4 wordt daardoor 389,3 i.p.v. 399,6 km. De join zelf toont
  als één spike (100°) in `toets_knikken` op 48.0881,18.9444.
- Het pompstation Budkovce is niet getekend (§7); a3 eindigt op de SK/UA-grensknoop 48.5418,22.1594 (gedeelde node van way 923057409 en 564620618).

**Lessen.** (1) Een ontwerp-scan die ways selecteert op naam/tag mist korte tussenstukjes; zoek bij een naad eerst een gedeelde node (OSM-API `ways.json?ways=` + `nodes.json?nodes=`
in batches van 100/700 is genoeg, geen pyosmium of Overpass nodig). (2) Een grensovergang kan door twee landen dubbel gekarteerd zijn: controleer de laatste kilometers van het ene been tegen het eerste stuk van het
volgende vóór je een naad accepteert. (3) Parallelle Druzhba-strengen (BY en Karpaten) zijn niet uitgesloten behalve de genoemde ways; het kortste pad is niet per se de actieve strang.
(4) De slot-routine uit de opdracht gebruikt `rm -rf` op een variabel pad en wordt door de veiligheidscheck geweigerd; vrijgeven kan met `rm -f $SLOT/sinds; rmdir $SLOT`.
