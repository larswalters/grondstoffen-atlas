# Routebrief (licht) · nikkel — Talnakh → Nadezhda (Norilsk, Rusland)

**stroom-id:** `nikkel-talnakh-nadezhda` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** nikkel-koper-concentraat van de Talnakh-concentrator (Nornickel Polar Division) gaat als slurry door de **leiding** Pulpoprovod TOF-NMZ (OSM `man_made=pipeline`, 20,8 km doorlopend) naar de ertskant van Norilsk, de Nadezhda-metallurgische fabriek; het laatste stuk (8,5 km) is gestippeld omdat de OSM-keten daar ophoudt. Ontwerp zei spoor; de haalbaarheidstoets (bindend) wees uit dat spoor 47,8 km met een omkering geeft en dat de pijp wél gekarteerd is, dus modaliteit **leiding**. Titel/id noemen het echte eindpunt: Nadezhda.
**Welke as van het verhaal:** de ertskant van het Norilsk-complex, de schakel vóór converter-matte en de Arctische afvoer (zie `nikkel-norilsk-monchegorsk`, dat bij Nadezhda begint). Nornickel-groep 205 kt Ni in 2024 [6]; het Talnakh-aandeel is niet apart gepubliceerd (peiljaar 2024, groepscijfer).

## 1 · Ketenkaart
```
Talnakh-concentrator `ni-talnakh-concentrator` ──(b1 leiding · Pulpoprovod TOF-NMZ, OSM 15 ways · 20,8 km, aannemelijk: één bron)──►
   OSM-pijpeinde 69.3667,88.1381 ──(b2 leiding, stippel · OSM-keten eindigt · ~8,5 km hemelsbreed)──► Nadezhda-fabriek `ni-nadezhda-fabriek` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `ni-talnakh-concentrator` → OSM-pijpeinde (69.3667, 88.1381) | Pulpoprovod ТОФ-НМЗ (slurry), 15 aaneengesloten ways | 20,8 (gemeten uit OSM-geometrie; geen gepubliceerde lengte) [3][4] | OSM-ways → FeatureCollection (`--been-geojson "leiding\|…"`) | nee, doorgetrokken |
| b2 | A | leiding | OSM-pijpeinde → `ni-nadezhda-fabriek` | stuk zonder genoemde OSM-way (naamloze pijpen in dit gebied dragen geen naam of substance, zie §7) | hemelsbreed 8,5 km, geen leidingkm | `--stippel "leiding\|…"` | ja, reden: OSM-keten eindigt |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-talnakh-concentrator` | concentrator (kop pijp) | Talnakhskaya obogatitelnaya fabrika (TOF), Talnakh | 69.5040, 88.3668 | [3][5][8] OSM-polygoon way 93390151/93612934 | bron-gelegd (z15 gezien: één grote vlakke hal met transportbrug en spoorbundel aan de oostkant, tailingsvijver ten zuidwesten; de pijp begint 0,13 km ten NW op 69.5032, 88.3642) |
| `ni-nadezhda-fabriek` | smelter (staart pijp) | Nadezhda Metallurgical Plant, Norilsk | 69.3275, 87.9521 | hergebruikt letterlijk uit `nikkel-norilsk-monchegorsk` [9] | bron-gelegd (daar z15 gezien: groot fabriekscomplex met rookpluim en spoorbundel) |

Opmerking: het sitelaag-punt van Talnakh (69.53, 88.34, w-norilsk-talnakh-nadezhda) is een mijndistrict-centroïde; de concentrator ligt 3 km zuidoostelijker op bovenstaand punt (OSM + satelliet).

## 4 · Via-punten
Geen: een leiding volgt de OSM-ways, geen corridorkeuze (b1 is vooraf gestikt, b2 is een rechte stippel).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Talnakh-concentrator (TOF) | Nornickel Polar Division | rijke en medistige sulfide-erts Talnakh/Oktyabrsky → Ni-pyrrhotiet- en Cu-concentraat; hydrotransport naar de metallurgische fabrieken | niet apart gepubliceerd; groep 205 kt Ni (2024) | [1][6] |
| Nadezhda Metallurgical Plant | Nornickel Polar Division | concentraat → converter-matte (zie `nikkel-norilsk-monchegorsk`) | idem | [2][6] |

## 6 · Stoppunt
De brief stopt bij Nadezhda: de matte-keten vanaf hier is al getekend in `nikkel-norilsk-monchegorsk` (b1 spoor naar Dudinka); fase D/E vervalt. Geen aansluitend been, dus geen naad met die stroom (het ankerpunt is identiek, het andere been begint er).

## 7 · Open punten
- **Pijp of spoor niet in een bedrijfsbron bevestigd:** alleen OSM-naam (Pulpoprovod TOF-NMZ) en ru-Wikipedia (TOF levert concentraat per hydrotransport aan de metallurgische fabrieken, Nadezhda genoemd) [1][3]; een Nornickel-document dat de leidingroute noemt is niet gevonden. Vandaar *aannemelijk: één bron*.
- **Laatste 8,5 km gestippeld:** de benoemde OSM-keten eindigt op 69.3667, 88.1381. In het gebied liggen naamloze `man_made=pipeline`-ways (o.a. 266932019, 952480428, 266932294, 266932452) die 0,17 km verder doorlopen en 0,94 km ten oosten van het Nadezhda-anker eindigen; zonder naam of substance zijn ze niet aan deze pijp toe te schrijven en blijven buiten de doorgetrokken lijn. Een betere bron (Nornickel, vergunning) kan b2 later kleiner maken.
- Het concentraat gaat volgens ru-Wikipedia óók naar de Medny-fabriek (Copper plant); het aandeel Nadezhda is niet gepubliceerd.
- Een spoorverbinding Talnakh–Norilsk bestaat in OSM (toets: 47,8 km, omkering 69.3228, 88.2173) maar is niet als route voor dit concentraat bevestigd; niet getekend.
- Talnakh-aandeel van de 205 kt Ni niet gepubliceerd.

## 8 · Bronnen
[1] ru-Wikipedia, "Талнахская обогатительная фабрика": levert concentraten aan Medny en Nadezhda-fabriek, shop voor hydrotransport. https://ru.wikipedia.org/wiki/Талнахская_обогатительная_фабрика
[2] ru-Wikipedia, "Надеждинский металлургический завод (Норильск)": gebouwd voor Talnakh/Oktyabrsky-ertsen, in bedrijf sinds 1979. https://ru.wikipedia.org/wiki/Надеждинский_металлургический_завод_(Норильск)
[3] OpenStreetMap (ODbL), ways Пульпопровод ТОФ-НМЗ (man_made=pipeline, slurry): 104522117, 104522086, 104522180, 104522114, 104522095, 104522107, 104522153, 104522167, 315356242, 315356243, 104522127, 104522139, 104641842, 104641821, 203572312, bv. https://www.openstreetmap.org/way/104522167
[4] OSM API, gestikt en gemeten (20,82 km, 231 punten, één naad van 11 m tussen 104641821 en 203572312): https://api.openstreetmap.org/api/0.6/way/203572312/full
[5] OSM, Talnakhskaya obogatitelnaya fabrika (way 93390151, 93612934) en en-Wikipedia "Talnakh" (district 25 km noord van Norilsk Central). https://en.wikipedia.org/wiki/Talnakh
[6] Nornickel, persbericht 27-01-2025: 205 kt Ni in 2024. https://nornickel.com/news-and-media/press-releases-and-news/nornickel-announces-consolidated-production-results-for-2024/
[7] ru-Wikipedia, "Экология Норильска": noemt een lozing van koperconcentraat op het pulpoprovod van de Talnakh-fabriek (bevestigt dat een slurryleiding bestaat). https://ru.wikipedia.org/wiki/Экология_Норильска
[8] Esri World Imagery via `v2/tools/sat_check.py` z15: `v2/build-cache/satcheck/sat-nikkel-talnakh-nadezhda-concentrator.png`, `…-pijpeinde.png` (pijpeinde: industrieterrein met smelterhallen en schoorstenen, aansluitend aan de Norilsk-fabrieken; de pijp zelf is op dit beeld niet zeker te onderscheiden).
[9] Routebrief `v2/design/routebrieven/nikkel-norilsk-monchegorsk.md` (anker `ni-nadezhda-fabriek` en b1 vanaf Nadezhda).
[10] Interne haalbaarheidstoets `nikkel-talnakh-nadezhda` (2026-10-30): spoortoets 47,8 km omkering; OSM-pijpketen 20,8 km; aanpassing leiding.
[11] cyclowiki Norilsk (Nadezhda krijgt product van de TOF, geen transportwijze): via de toets, niet zelf opnieuw geraadpleegd.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)

**Stroom `nikkel-talnakh-nadezhda`** → `v2/data/stroomroute-nikkel-talnakh-nadezhda.json` (5,2 KB) — 2 benen, **29,3 km**, 220 punten, 2 markers. leiding 20,8 km (doorgetrokken) + 8,5 km (stippel).
Recept: `bak_stromen.sh` (functie `bak_nikkel_talnakh_nadezhda`); b1 vooraf gestikt met `v2/tools/maak_leidingbeen_nikkel_talnakh_nadezhda.py --schrijf` (OSM-API, 15 ways in vaste volgorde) naar `v2/build-cache/ais/graaf/nikkel-talnakh-nadezhda-leiding-b1.geojson` (FeatureCollection, `--been-geojson "leiding|…"`). Geen profiel in `maak_stroombeen_weg.py`, geen zee, spoor, weg, haven-aanloop of lucht; geen slot voor wegscan, wel een zwaar-slot voor de bake.

| been | modaliteit | km | punten | naad | opmerking |
|---|---|---|---|---|---|
| b1 | leiding, doorgetrokken | 20,8 | 218 | n.v.t. | Pulpoprovod TOF-NMZ, 15 OSM-ways, 69.5032,88.3642 → 69.3667,88.1381 |
| b2 | leiding, stippel | 8,5 | 2 | 0,002 km | reden: OSM-keten eindigt; hemelsbreed, geen leidingkm |

Markers: `ni-talnakh-concentrator` 69.5040,88.3668 (0,13 km van de lijn = kop pijp ligt 0,13 km NW van het anker, zoals in §3) en `ni-nadezhda-fabriek` 69.3275,87.9521 (0,00 km).

**Toets (§5 handleiding):** geen gepubliceerde leidinglengte, dus de ±15%-toets is een indicatie: gemeten OSM-lengte 20,82 km tegen 20,8 km in de brief. Naden 0,000 en 0,002 km. `json.load` ok, versie 2, `punt_formaat` lonlat, modaliteit leiding, elk been ≥ 2 punten. `toets_knikken`: 6 knikken ≥ 60° (OSM-geometrie van de pijp, boogstralen 26–91 m), 0 omkeringen, 0 terugloop. `toets_rechte_benen`: alleen b2, per constructie een stippel met reden.

**Wijkt af van de brief:** de brief noemt 231 punten, de gestikte lijn heeft er 218 (gedeelde nodes tussen opeenvolgende ways worden één keer geteld); lengte (20,82 km), begin en eind komen overeen. De naad van 11 m tussen way 104641821 en 203572312 is in de stikker toegestaan (grens 50 m) en wordt in de console gemeld.

**Open:** geen bedrijfsbron voor de pijp (aannemelijk: één bron, in de beennaam); de naamloze pijp-ways na het benoemde einde blijven buiten de lijn; Talnakh-aandeel van de 205 kt Ni en het Medny-aandeel niet gepubliceerd.

**Lessen:** (1) een OSM-pijpketen hoeft geen gedeelde node tussen alle ways te hebben, een naad van enkele meters is dan geen stik-fout maar een karteringsnaad; het patroon `maak_leidingbeen_*.py` kreeg daarvoor een drempel van 50 m. (2) Een keten van twee leidingbenen is in één minuut gebakken: de tijd zit in het zoeken van de ways, niet in het gereedschap.
