# Routebrief (licht) · uranium — Elektrostal → Domodedovo → Pápa → Paks (Rusland/Hongarije, peiljaar 2022)

**stroom-id:** `uranium-elektrostal-paks` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken
**Keten in één zin:** VVER-440-splijtstofelementen van TVEL Elemash (Elektrostal) gaan per truck over de Moskouse
kleine ring (А-107) naar het vrachtplatform van Moskou-Domodedovo (aannemelijk), per Il-76-vrachtvlucht van Volga-Dnepr
(grootcirkel, via Belarus-Polen-Slowakije) naar de Hongaarse luchtmachtbasis Pápa en per spoor (niet via Boedapest) naar
de kerncentrale Paks — **stoppunt**: de reactor. Peiljaar 2022 (de luchtroute duurde tot de herrouting eind 2022).
**Welke as van het verhaal:** *De VVER-lock-in na februari 2022: Russische brandstof voor een Russisch reactorontwerp, over
een luchtbrug omdat de spoorroute door Oekraïne dichtging.* Volume **≈ 50 t U/j** (eigen schatting: 4 eenheden × 42 t UO2 =
168 t UO2 ≈ 148 t U in de kernen [8], brandstof blijft gemiddeld drie jaar [8] → ~1/3 herlaad per jaar; geen
gepubliceerd leveringscijfer, per zending niet bekend [1][2][4]). Eenheid t U/j, peiljaar 2022.

## 1 · Ketenkaart
```
TVEL Elemash, Elektrostal `u-elemash`
  ──(b1 truck · А-107 kleine ring oost/zuid → А-105 · hemelsbreed 55 km, geen wegkm · aannemelijk: geen bron noemt de truck)──►
Moskou-Domodedovo vrachtplatform (DME) `u-dme-vrachtplatform`   [wegeinde А-105 + stippel 1,25 km airside]
  ──(b2 lucht · vlucht DME → LHPA, grootcirkel 1.667 km · aannemelijk: bron noemt alleen "Moskou" [1][3])──►
Pápa-vliegbasis (LHPA) platform `u-papa-platform`   [stippel 0,68 km naar het spoor]
  ──(b3 spoor · Pápa–Győrszabadhegy–Komárom–Székesfehérvár–Pusztaszabolcs–Dunaújváros · hemelsbreed 134 km, spoor 267 km ·
     aannemelijk: reconstructie uit Facebook-waarnemingen [1])──► Paks kerncentrale `u-paks-centrale` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | Elemash → А-105 bij DME-terminalcomplex | А-107 (oost/zuid) → А-105; niet door Moskou (M-7 gaf 88,8 km) | hemelsbreed 55 km, geen wegkm; gemeten 91,8 | maak_stroombeen_weg (extract rusland-centraal) | nee — *aannemelijk: modaliteit niet in een bron* |
| b1s | D | truck | А-105-eind → DME-vrachtplatform | luchthaventerrein | 1,25 (eigen meting) | rechte stippel | **ja — airside, geen wegpad (ZRH-patroon)** |
| b2 | D | lucht | DME → Pápa LHPA | Volga-Dnepr Il-76 via Belarus, Polen, Slowakije [2] | grootcirkel 1.666,6; 6 en 19-20 april 2022 [1][2][4] | maak_luchtbeen | nee — doorgetrokken, *aannemelijk: vertrekluchthaven* |
| b2s | D | spoor | Pápa-platform → spooraansluiting | vliegbasisspoor | 0,68 (eigen meting) | rechte stippel | **ja — net reikt niet (0,68 km)** |
| b3 | D | spoor | Pápa → Paks | Pápa–Győrszabadhegy–Komárom–Székesfehérvár–Pusztaszabolcs–Dunaújváros–Paks | hemelsbreed 134; gemeten 270,1 (7 runs); zonder via-punten 290,9 via Boedapest | toets_spoorroute (7 runs) | nee — *aannemelijk: één bron* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-elemash` | fabriek (kop) | TVEL Elemash Machine-Building Plant, Elektrostal | 55.7875, 38.4875 | [9] wiki-coördinaat | bron-gelegd (z15 gezien: industrieterrein met een grote fabriekshal en bijgebouwen aan de noordoostrand van de stad, bos eromheen; welke hal splijtstof maakt niet te zien). Sitelaag `w-tvel-elektrostal` (55.7833, 38.4333) ligt 3,4 km westelijker; OSM-adres K. Marksa 12 (55.7902, 38.4685) is stadsfabriek met spoor — onze keuze volgt wiki |
| `u-dme-vrachtplatform` | overslag weg → lucht | Domodedovo (DME), groot apron zuidoost van de terminals | 55.4106, 37.9126 | [11][12] | **onzeker** (z15/z16: betonnen apron met vrachtachtige toestellen op het gras ten zuiden; welk gebouw/apron vracht afhandelt is niet aan te wijzen; OSM-"DMD Cargo" 55.3733, 37.7869 is een magazijnpark 8 km west, niet gebruikt) |
| `u-papa-platform` | overslag lucht → spoor | Pápa Air Base (LHPA), platform met hangars west van de baan | 47.3578, 17.4945 | [10] wiki-baan 47.3639, 17.4972 | bron-gelegd (z16 gezien: witte hangars en apron direct west van de baan; luchtmachtbasis, geen civiele vrachtafhandeling) |
| `u-paks-centrale` | reactor (eindpunt) | Paks kerncentrale, spoorterrein aan de westzijde | 46.5776, 18.8487 | [8] wiki 46.5725, 18.8542 | bron-gelegd (z16 gezien: spoorlijn en technisch terrein met loodsen; de vier reactorhallen liggen 0,7 km ZO) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze; op de doorgaande weg/lijn)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | А-107 ten zuiden van Elektrostal/Noginsk | 55.7410, 38.4562 | kleine ring in plaats van de M-7 door Moskou (88,8 km); snapt 0,01 km |
| b1 | 2 | А-107 oost van Ramenskoje | 55.6246, 38.3659 | houdt de ring aan |
| b1 | 3 | А-107 bij Bronnitsy-oost | 55.4300, 38.3068 | idem |
| b1 | 4 | А-107 zuidpunt ten zuiden van Domodedovo | 55.3696, 38.0915 | pint de zuidelijke aanloop naar de А-105 |
| b1 | 5 | А-105 bij het DME-terminalcomplex (routeerpunt) | 55.4173, 37.8966 | eind van het openbare net; daarna stippel |
| b3 | 1 | Pápa station | 47.3398, 17.4601 | sluit een omkering bij de aansluiting uit (apron→Győrszabadhegy direct gaf 1 bocht ≥ 60°) |
| b3 | 2 | Győrszabadhegy | 47.6631, 17.6481 | noordroute langs Győr, niet via Veszprém/Boedapest [1] |
| b3 | 3 | Komárom | 47.7502, 18.1116 | corridor langs de Donau [1] |
| b3 | 4 | Székesfehérvár | 47.1836, 18.4244 | [1]; zonder via-punten rijdt de router via Boedapest (290,9 km) |
| b3 | 5 | Pusztaszabolcs | 47.1396, 18.7612 | knoop richting Dunaújváros [1] |
| b3 | 6 | Dunaújváros | 46.9606, 18.9135 | lijn naar Paks [1]; eindpunt = `u-paks-centrale` (snap 0,05 km) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Elemash (Elektrostal) | TVEL / Rosatom | uranium-oxidepoeder → VVER-440-splijtstofassemblages | ≈ 1.200 t HM/j (sitelaag-indicatie, alle TVEL-klanten) | [6][9] |
| Paks (4 × VVER-440) | MVM Paks | splijtstof → ~2.000 MWe | 42 t UO2 per reactor [8] | [8] |

## 6 · Stoppunt
De brief stopt bij de reactor van Paks: het is de enige afnemer van deze brandstof (E vervalt) en geen bron noemt een volgende
locatie. Fase D is hier de hele keten: WNA en ANS koppelen Paks-brandstof aan TVEL en de fabriek Elemash [6][7] — het
zendingsbewijs voor déze vluchten ontbreekt.

## 7 · Open punten
- **Het Moskouse vertrekveld is niet bevestigd:** bronnen zeggen "Moskou" / "Moskou international airport" [1][3]. DME is *aannemelijk* op grond van
  de Bratislava-vlucht van 2 maart 2022 (Il-76 landde in Domodedovo, volgens een zoekresultaat van aeroTELEGRAPH, niet zelf gelezen [11]); Volga-Dnepr heeft
  zijn hoofdbasis in Oeljanovsk en een hub in Krasnojarsk [13], dus DME is geen vanzelfsprekende keuze.
- **De DME-vrachtterminal is niet gevonden** (OSM-Overpass onbereikbaar, geen bron): het anker is een apron-punt en `onzeker`.
- **De truck Elektrostal → luchthaven** is een aanname (geen bron noemt hoe de assemblages naar het vliegveld gaan); ook helikopter
  of een andere luchthaven is niet uit te sluiten. Hemelsbreed 55 km, geen wegkm; gemeten 91,8 km is een OSM-scan, geen norm.
- **Pápa → Paks per spoor is een reconstructie** uit Facebook-waarnemingen (twee museumrijtuigen naar Pápa op 5 april, treinen terug op 23 april [1]);
  Telex en BBJ noemen geen spoor [3][4]. Het ontwerp zegt 200 km; de haalbaarheidstoets (267 km) en deze scan (267,1 + 3,0 km) kloppen onderling.
- **Peiljaar 2022:** sinds december 2022 gaat de brandstof per schip via Bulgarije en per trein door Roemenië (haalbaarheidstoets, niet zelf bevestigd);
  Framatome (2027) en Westinghouse (2028) diversifiëren [7]. Vluchten: 6 april, 19-20 april, retour Pápa → Moskou 24 april 2022 [1].
- **Elemash-coördinaat:** sitelaag-punt ligt 3,4 km van het wiki-punt en onze anker — centraal gelijktrekken. Het wegbeen begint 0,81 km van het anker (eerste mijl 1,56 km over kleine wegen).
- **Pápa-spooraansluiting:** de dichtstbijzijnde spoor-knoop ligt 0,68 km west van het platform; of het vliegbasisspoor daar echt aansluit is niet gezien.
- **Per zending geen volume** bekend; het jaarvolume (≈ 50 t U/j) is een eigen schatting uit de reactorkernen.

## 8 · Bronnen
[1] Daily News Hungary (it), 2022 — Volga-Dnepr, Moskou, Pápa, trein naar Paks, data 5/6/19/23/24 april: https://dailynewshungary.com/it/ecco-come-il-combustibile-nucleare-arriva-ora-dalla-russia-allungheria/
[2] Hungary Today, 2022 — Il-76 over Belarus, Polen en Slowakije; eerste levering ~2 weken voor 20 april: https://hungarytoday.hu/hungary-paks-fuel-nucelar-energy-russia/
[3] Telex, 2022-04-07 — vliegtuig "vanuit Moskou" landt in Pápa (Volga-Dnepr): https://telex.hu/belfold/2022/04/07/rendkivuli-biztonsagi-intezkedesek-mellett-hozott-nuklearis-futoanyagot-papara-egy-orosz-gep
[4] BBJ/Budapest Times, 2022-04-20 — tweede levering per lucht: https://BBJ.HU/economy/energy/power/hungary-gets-another-delivery-of-paks-fuel-by-air
[5] NucNet, 2022-04 — eerste Paks-zending uit Rusland per lucht: https://www.nucnet.org/news/paks-nuclear-station-gets-fuel-shipment-from-russia-by-air-4-4-2022
[6] ANS, 2020-10-15 — gewijzigde brandstof voor Paks getest bij TVEL Elemash, Elektrostal: https://www.ans.org/news/tag-rosatom/step-1604059365/
[7] WNA, Hungary — Paks-brandstof historisch van TVEL; Framatome contract okt 2024 (vanaf 2027), Westinghouse nov 2025 (vanaf 2028): https://world-nuclear.org/information-library/country-profiles/countries-g-n/hungary
[8] Wikipedia, Paks Nuclear Power Plant — 42 t UO2 per reactor, brandstof gemiddeld 3 jaar, coördinaat 46.5725, 18.8542: https://en.wikipedia.org/wiki/Paks_Nuclear_Power_Plant
[9] Wikipedia, ELEMASH Machine-Building plant — coördinaat 55.7875, 38.4875, onderdeel van TVEL: https://en.wikipedia.org/wiki/ELEMASH_Machine-Building_plant
[10] Wikipedia, Pápa Air Base — LHPA, 47°21'50"N 17°29'50"E, baan 16/34 2.399 m: https://en.wikipedia.org/wiki/P%C3%A1pa_Air_Base
[11] aeroTELEGRAPH, 2022-03 — Il-76 vloog van Bratislava naar Moskou (Domodedovo) voor Slowaakse brandstof (via zoekresultaat): https://www.aerotelegraph.com/ilyushin-il-76-flog-trotz-sanktionen-von-bratislava-nach-moskau
[12] OpenStreetMap via Photon — Domodedovo aerodrome 55.4087, 37.9094 (ODbL): https://www.openstreetmap.org
[13] Wikipedia, Volga-Dnepr Airlines — hoofdbasis Oeljanovsk Vostochny, hub Krasnojarsk: https://en.wikipedia.org/wiki/Volga-Dnepr_Airlines
Satellietblik (Esri z15–z16, 2026-10-09): `v2/build-cache/satcheck/sat-uranium-elektrostal-paks-{u-elemash,elemash-wiki,u-dme,dme-a,u-papa,u-paks}.png`.

## 9 · Gebakken
**Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)** · `v2/data/stroomroute-uranium-elektrostal-paks.json` (35,2 KB, contract 2, lonlat) · `bash v2/tools/bak_stromen.sh uranium-elektrostal-paks` (functie `bak_uranium_elektrostal_paks`) · totaal 2.035,6 km, 11 benen (2 stippel), 4 markers.

| # | modaliteit | been | km gemeten | brief | naad |
|---|---|---|---|---|---|
| 1 | truck | Elemash → А-105 bij DME (А-107 kleine ring) | 92,6 | hemelsbreed 55, geen wegkm (scan 91,8) | 0 |
| 2 | truck, stippel | DME-vrachtplatform last mile (airside) | 1,3 | 1,25 | 0 |
| 3 | lucht | vlucht DME → LHPA, grootcirkel | 1.666,6 | 1.666,6 | 0 |
| 4 | spoor, stippel | Pápa-platform → spooraansluiting | 0,7 | 0,68 | 0 |
| 5-11 | spoor | s1 t/m s7: Pápa station, Győrszabadhegy, Komárom, Székesfehérvár, Pusztaszabolcs, Dunaújváros, Paks | 3,2 + 41,0 + 37,2 + 82,1 + 28,8 + 26,9 + 55,2 = 274,4 | 270,1 (spoorrouterkm) | 0 |

Markers: `u-elemash`, `u-dme-vrachtplatform`, `u-papa-platform`, `u-paks-centrale` (alle 0,0-0,05 km van hun lijn).
**Recept:** wegbeen = `PROFIELEN["uranium-elektrostal-paks-elemash-dme"]` via de pure-Python wrapper (`build-cache/ais/graaf/uranium-elektrostal-paks-wegscan-wrapper.py`, pyosmium geblokkeerd); luchtbeen = `maak_luchtbeen.py` DME → LHPA; spoor = `BAKE_SUFFIX=-raw toets_spoorroute.mjs`, 7 runs (hoofd-km 100, max-snap 60); alles samengevoegd door `hecht_marnet.py route`.
**Stippels:** (a) DME-vrachtplatform 1,25 km: airside, geen wegpad, ZRH-patroon; (b) Pápa-platform 0,68 km: het net reikt niet, het vliegbasisspoor is niet gezien. De vlucht en de rest zijn doorgetrokken. Geen zee, haven-aanloop, leiding of kopie.
**Toets:** km binnen 1,6% (spoor) en 0,9% (weg) van de brief of scan; geen naad > 0 m; geen omkering of terugloop. toets_knikken: 9 scherpe hoeken (78-94 graden, straal 1-49 m) op het wegbeen, alle in de fabrieksstraten rond Elemash en bij de А-105-aansluiting, geen reparatie nodig. toets_rechte_benen: geen treffer voor deze stroom.
**Lessen:** (1) de wegscan van het anker begint op het OSM-net; het eerste stuk loopt over kleine straten in Elektrostal, dat geeft de spikes. (2) Het spoorbeen was +1,6% boven de lopende som uit de runs omdat de bake de polylijn meet, niet de routerkm. (3) Het DME-anker blijft onzeker; een vrachtterminal-OSM-object zou het moeten vervangen. (4) Het id noemt Paks en de lijn eindigt in Paks, dus geen afwijking van het ontwerp.
