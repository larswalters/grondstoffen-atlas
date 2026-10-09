# Routebrief (licht) · kobalt — Voisey's Bay (Labrador) → Long Harbour (Newfoundland)

**stroom-id:** `kobalt-voiseysbay-longharbour` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** nikkel-kobalt-koper-concentraat van de Voisey's Bay-mijn (Vale Base Metals, Noord-Labrador) per **truck** over sitewegen naar de ladingskade aan Anaktalak Bay, per **zeeschip** langs de Labradorkust en door de Straat van Belle Isle en de Golf van Saint-Laurent naar Long Harbour (Placentia Bay), en ~1,6 km over eigen terrein naar de hydromet-raffinaderij, waar het kobalt als **electrolytic cobalt rounds** uit het concentraat wordt gewonnen [1][2]. Geen fase D: geen bron noemt een afnemer van dit kobalt.
**Welke as van het verhaal:** kobalt als **bijproduct van de nikkelroute**: Vale's eigen Atlantisch-Canadese keten, los van Sudbury en Kristiansand. Het kobalt heeft geen eigen lading; het zit in het nikkelconcentraat [2][3]. **Jaarvolume: 2,5 kt Co/jaar, nameplate (ontwerp, ramp-up, geen gemeten output)** [4][8]; Vale Base Metals maakte in 2025 in totaal 3,2 kt Co (3.242 t) over al zijn sites, niet per site uitgesplitst [5]. De nikkelbrief noemt 2,6 kt; die waarde is niet terug te vinden (§7).

## 1 · Ketenkaart
```
Voisey's Bay-mijn `co-voiseysbay-mijn` ──(b1 truck · sitewegen, STIPPEL · 8,7 km hemelsbreed)──►
Voisey's Bay-kade `co-voiseysbay-kade` (Anaktalak Bay, aannemelijk)
   ──(b2a zee · haven-aanloop, STIPPEL · 177,3 km)──► zeeknoop 645 (57.8113, -60.6748)
   ──(b2b zee · MARNET · Labradorkust → Belle Isle → Golf v. Saint-Laurent · 1.378,9 km)──► zeeknoop 762 (47.7000, -52.5000)
   ──(b2c zee · haven-aanloop Placentia Bay, STIPPEL · 305,0 km)──► Long Harbour-kade `co-longharbour-kade`
   ──(b3 truck · eigen terrein/conveyor, STIPPEL · 1,6 km)──► Long Harbour Processing Plant `co-longharbour-fabriek` ── stoppunt
```
**Eerlijk over de stippel:** 4 van de 5 beenstukken zijn stippel (8,7 + 177,3 + 305,0 + 1,6 = 492,6 van 1.871,5 km = **26% van de lengte**); de doorgetrokken ruggengraat is het MARNET-zeebeen van 1.378,9 km. Alle vijf stukken zijn **letterlijke kopieën** van `nikkel-voiseysbay-longharbour` (b1, b2a, b2b, b2c, b3); alleen titel, beennamen en markers zijn kobalt.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `co-voiseysbay-mijn` → `co-voiseysbay-kade` | sitewegen, geen openbaar net | hemelsbreed 8,7, geen wegkm; Heritage NL zegt ~11 km vanaf de mijn [3] | kopie nikkel b1 (`--stippel`) | ja (eigen terrein) |
| b2a | B | zee | `co-voiseysbay-kade` → zeeknoop 645 | haven-aanloop Anaktalak Bay / Labradorkust | hemelsbreed 177,3, geen gepubliceerde waarde | kopie nikkel b2a (`--stippel`) | ja (kade 177,3 km van de zeeknoop; `maak_havenaanloop.py` gaf in de nikkelbake timeout op alle acht trappen) |
| b2b | B | zee | zeeknoop 645 → zeeknoop 762 | Labradorkust, Straat Belle Isle, Golf van Saint-Laurent, Placentia Bay (zomercorridor) | 1.378,9 MARNET; geen gepubliceerde lengte | MARNET, kopie nikkel b2b (`--been`) | nee |
| b2c | B | zee | zeeknoop 762 → `co-longharbour-kade` | haven-aanloop Placentia Bay | 305,0 gemeten over water, 0,00 km over land (kade 103,9 km hemelsbreed van de knoop) | kopie nikkel b2c (`--stippel-geojson`, `nikkel-voiseysbay-longharbour-aanloop-longharbour.geojson`, reisvolgorde knoop → kade) | ja (MARNET reikt niet tot de kade) |
| b3 | C | truck | `co-longharbour-kade` → `co-longharbour-fabriek` | eigen terrein/transportband | hemelsbreed 1,6; Wikipedia: plant ~2 km zuid van de kade [6] | kopie nikkel b3 (`--stippel`) | ja (eigen terrein) |

b2a ligt als rechte lijn voor ~31% over land (gemeten tegen `ne_10m_land`): de lijn is **schematisch**, geen vaarroute. Totaal b2 (a+b+c) 1.861,2 km tegen ~1.700 indicatief uit het ketenontwerp (+9,5%, geen gepubliceerde lengte). Seizoensijs (Vale-winterprogramma 22 jan–6 apr [2]) is niet gemodelleerd.

## 3 · Ankers (één per site en per overslag; letterlijk hergebruikt uit `nikkel-voiseysbay-longharbour.md` §3, id-prefix `co-`)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-voiseysbay-mijn` | mijn/concentrator | Voisey's Bay Mine (Vale Base Metals) | 56.3347, -62.1031 | [7], oorspronkelijk Wikipedia-coördinaat | bron-gelegd (z15 opnieuw gezien: open pits, concentrator met tailingsvijvers, landingsstrip; kruis op de mijnweg tussen pit en concentrator) |
| `co-voiseysbay-kade` | laadplek/overslag (kandidaat Edward's Cove-cluster) | sitefaciliteit Anaktalak Bay | 56.4115, -62.0800 | [3][7] | **aannemelijk** (z15 opnieuw gezien: tankenpark en opslag-/equipmentterrein aan getijdenwater, siteweg naar de mijn; een ertsladingsdok is niet te zien) |
| `co-longharbour-kade` | overslag zee → land (wharf) | Long Harbour-kade (Vale) | 47.4230, -53.8230 | [6][7] | bron-gelegd (z15 opnieuw gezien: wharf met overkapte conveyor, opslaggebouw en een gemeerd schip) |
| `co-longharbour-fabriek` | raffinaderij (hydromet), stoppunt | Long Harbour Processing Plant (Vale) | 47.4101, -53.8133 | [1][6][7] | bron-gelegd (z15 opnieuw gezien: volledig procescomplex met tanks en bezinkbekkens, ~1,6 km zuid van de wharf) |

Zeeknopen (geen ankers): 645 = 57.8113, -60.6748 en 762 = 47.7000, -52.5000, opnieuw gemeten met `hecht_marnet.marnet_zee` (177,3 en 103,9 km van de kades). Beelden: `v2/build-cache/satcheck/sat-kobalt-voiseysbay-longharbour-{mijn,kade,lh-kade,lh-fabriek,kade-oost}.png`.

## 4 · Via-punten
Geen. Beide truckbenen zijn sitewegen zonder corridorkeuze, het zeebeen is haven → haven en alle verbindingen zijn kopieën.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Long Harbour Processing Plant | Vale Base Metals | nikkel-kobalt-koper-concentraat (Voisey's Bay) → nikkel (plating rounds en melt rounds), koperkathode, **electrolytic cobalt rounds** | ontwerp 50 kt Ni + 5 kt Cu + **2,5 kt Co** per jaar; werkelijk Voisey's Bay & Long Harbour 40,3 kt Ni in 2025; kobaltoutput van de plant niet gepubliceerd | [1][4][5] |

## 6 · Stoppunt
De brief stopt bij de Long Harbour Processing Plant: dat is het eindproduct (kobaltmetaal) en geen bron noemt een afnemer of vervolgzending van dit kobalt (geen fase D, E vervalt). Alleen als reserve-as bakken nadat de prioriteit-1- en -2-ketens staan.

## 7 · Open punten
- **Kobalt is bijproduct, geen eigen stroom.** Er gaat één concentraatlading over de lijn; wat de kaart als "kobalt" toont is de nikkelroute met kobalt als bijproduct [2][3]. Het kobaltaandeel van de lading is niet gepubliceerd.
- **Volume is nameplate**: 2,5 kt Co/j uit Hatch (ontwerp) [4] en de sitelaag `w-longharbour` [8]; de 2,6 kt van de nikkelbrief is niet terug te vinden. Vale rapporteert alleen een VBM-totaal van 3.242 t Co in 2025 [5], zonder uitsplitsing naar Long Harbour. Peiljaar ontwerp, plant in ramp-up.
- **Ertsladingsdok niet gevonden.** Heritage NL noemt de wharf bij Edward's Cove, ~11 km noord van de mijn [3]; z15 toont alleen tankenpark en equipmentterrein (`co-voiseysbay-kade` blijft aannemelijk). Op de oostoever van dezelfde inlet ligt bij ca. 56.414, -62.071 een kleine steiger met containerstapels; die is te klein voor een ertswharf en niet gebruikt.
- **Stippelaandeel 26%** (zie §1) en b2a is voor ~31% een rechte lijn over land; beide zijn "hier reikt het net niet", geen route. Nikkelbrief §9: `maak_havenaanloop.py` liep voor Voisey's Bay vast.
- **Seizoensijs** (22 jan–6 apr) niet gemodelleerd; de lijn is de zomercorridor [2].
- **Sitelaag, centraal:** `w-longharbour` (47.4242, -53.8167) ligt ~1,6 km van `co-longharbour-fabriek`; centraal gelijktrekken. De kobaltsitelaag heeft geen Voisey's Bay-site, dus de marker `co-voiseysbay-mijn` heeft geen sitelaag-tegenhanger.
- **Feed tot 2016:** Wikipedia meldt dat in het begin het meeste concentraat uit Indonesië kwam en dat Long Harbour pas vanaf begin 2016 volledig op Voisey's Bay draaide [6]; huidige stand valt buiten de brief.

## 8 · Bronnen
[1] Vale Base Metals, "Long Harbour": hydromet-plant levert nickel, copper en electrolytic cobalt rounds; ontwerp 50.000 t Ni/j met commercieel koper en kobalt; wharf en crushing-gebouw. https://valebasemetals.com/our-operations/long-harbour/
[2] Vale Base Metals, "Voisey's Bay": al het nikkelconcentraat gaat naar Long Harbour en wordt nikkel, kobalt en koper; winterprogramma 22 jan–6 apr. https://valebasemetals.com/our-operations/voiseys-bay/
[3] Heritage NL, "The Voisey's Bay Mine": nikkel-kobalt-koper-concentraat per truck naar de wharf bij Edward's Cove, ~11 km noord van de mijn. https://www.heritage.nf.ca/articles/economy/voiseys-bay.php
[4] Hatch, "Long Harbour Processing Plant": 50.000 tpa nickel rounds, 5.000 tpa copper cathodes, 2.500 tpa cobalt rounds. https://www.hatch.com/en/Projects/Metals-And-Minerals/Long-Harbour-Processing-Plant
[5] Vale S.A., Form 6-K Q4 2025 (27 jan 2026): VBM by-product cobalt 3.242 t in 2025 (2.079 t in 2024); Voisey's Bay & Long Harbour 40,3 kt Ni. https://www.sec.gov/Archives/edgar/data/917851/000129281426000189/vale20260127_6k.htm
[6] Wikipedia, "Long Harbour Nickel Processing Plant": coördinaat 47°25'27"N 53°49'0"W, ontwerp met bijproducten kobalt en koper, ijsversterkte bulkcarriers, feed uit Indonesië tot ~2016. https://en.wikipedia.org/wiki/Long_Harbour_Nickel_Processing_Plant
[7] `v2/design/routebrieven/nikkel-voiseysbay-longharbour.md` (ankers §3, bakresultaat §9) en `bak_nikkel_voiseysbay_longharbour` in `v2/tools/bak_stromen.sh`; `v2/data/stroomroute-nikkel-voiseysbay-longharbour.json`.
[8] `v2/design/kobalt-sitelaag.json`, site `w-longharbour` (47.4242, -53.8167; 2,5 kt Co/j nameplate, bron daar [B24]).
[9] Canadian Mining Journal 2011 (herdruk), Long Harbour 50.000 t Ni, 4.700 t Cu, 2.500 t Co per jaar (alleen uit een zoekresultaat gezien). https://republicofmining.com/2011/09/26/vale%E2%80%99s-massive-newfoundland-nickel-refinery-takes-shape-by-paul-brent-canadian-mining-journal-%E2%80%93-september-2011/
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15, z16): zie de bestandsnamen in §3.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Resultaat:** `v2/data/stroomroute-kobalt-voiseysbay-longharbour.json` (9,4 KB, contract versie 2, lonlat) · 5 benen · **1.871,5 km** · 433 punten · 4 markers. Recept: `bak_kobalt_voiseysbay_longharbour` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh kobalt-voiseysbay-longharbour`).

| # | modaliteit | km | punten | lijn | toelichting |
|---|---|---|---|---|---|
| b1 | truck | 8,7 | 2 | stippel | sitewegen mijn → kade, hemelsbreed, geen wegkm (Heritage NL ~11); reden: eigen terrein, geen openbaar net; "aannemelijk" in de beennaam |
| b2a | zee | 177,3 | 2 | stippel | haven-aanloop Anaktalak Bay → zeeknoop 645; MARNET reikt niet; rechte lijn ~31% over land, schematisch; `maak_havenaanloop.py` liep in de nikkelbake vast op timeout 300, geen tweede poging |
| b2b | zee | 1.378,9 | 142 | doorgetrokken | MARNET-router zeeknoop 645 → 762, snaps 0,000 km; zomercorridor, geen seizoensijs |
| b2c | zee | 305,0 | 285 | stippel | haven-aanloop Placentia Bay (kade 103,9 km van knoop 762), over water, 0,00 km over land, al in reisvolgorde knoop → kade |
| b3 | truck | 1,6 | 2 | stippel | eigen terrein/transportband kade → fabriek, hemelsbreed |

**Alle vijf benen zijn letterlijke kopieën van `nikkel-voiseysbay-longharbour`** (b1, b2a, b2b, b2c, b3): punten, km, modaliteit en stippelvlag zijn per been gelijk aan het nikkelbestand (gecontroleerd met een vergelijking van `punten` en `km`). Alleen titel, beennamen en markers zijn kobalt. Het b2c-geojson is hetzelfde bestand als bij nikkel (`nikkel-voiseysbay-longharbour-aanloop-longharbour.geojson`), geen kopie. Geen extra extract, geen wegscan, geen nieuw profiel in `maak_stroombeen_weg.py`.

**Toets (handleiding §5):** naden tussen de benen 0,000 / 0,000 / 0,000 / 0,000 km (norm < 5 km) · alle vier markers 0,0 km van hun lijn · totaal 1.871,5 km en 433 punten precies zoals voorspeld · `toets_knikken.py`: 2 knikken (82,7 en 72,9 graden, beide op het MARNET-zeebeen bij 50.0/-54.6 en 49.6/-52.5, krappe maar echte bocht), 0 omkeringen, 0 terugloop · `toets_rechte_benen.py --min-km 5`: de enige rechte benen zijn b1 (8,7 km) en b2a (177,3 km), beide stippel met reden · `json.load` slaagt, versie 2, punt_formaat lonlat, alle modaliteiten in {zee, truck}, elk been >= 2 punten, 9,4 KB. De km-norm van ±15% is niet van toepassing: de brief geeft voor geen enkel been een echte wegkm of gepubliceerde zeelengte (b1 en b2 zijn "hemelsbreed, geen wegkm" resp. "geen waarde").

**Stippelaandeel:** 492,6 van 1.871,5 km = 26% (b1 + b2a + b2c + b3); de doorgetrokken ruggengraat is het MARNET-zeebeen van 1.378,9 km.

**Markers (4):** `co-voiseysbay-mijn` (56.3347, -62.1031) · `co-voiseysbay-kade` (56.4115, -62.0800, aannemelijk) · `co-longharbour-kade` (47.4230, -53.8230) · `co-longharbour-fabriek` (47.4101, -53.8133), coördinaten gelijk aan de `ni-`-markers.

**Lessen / aandachtspunten voor de centrale ronde:**
- Kobalt heeft hier geen eigen geometrie: de kaart toont de nikkelroute met kobalt als bijproduct. Het kobaltaandeel van de lading is niet gepubliceerd (§7); op de bol liggen kobalt en nikkel op exact dezelfde pixels (gloedgewicht telt dan op, zie de kop van `v2/src/gloed.js`).
- De sitelaag `w-longharbour` (47.4242, -53.8167) ligt 1,6 km van `co-longharbour-fabriek`; centraal gelijktrekken. De kobaltsitelaag heeft geen Voisey's Bay-site, dus `co-voiseysbay-mijn` heeft geen sitelaag-tegenhanger.
- Het 2,5 kt Co/j is nameplate (Hatch), geen gemeten output; de 2,6 kt in de nikkelbrief is niet terug te vinden.
- Registerregel: sleutel `co-vl`, bestand `stroomroute-kobalt-voiseysbay-longharbour.json`, grondstof `kobalt`; niet in `stromen-register.json` of de bundel gezet (centraal).
