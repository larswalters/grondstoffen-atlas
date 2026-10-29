# Routebrief (licht) · Goud — Paracatu (Brazilië) → Guarulhos → Zürich (Zwitserland)

**stroom-id:** `goud-paracatu-zurich` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) ·
**status:** gebakken
**Keten in één zin:** doré-goud van de Paracatu-mijn (Kinross, Minas Gerais) per truck over MG-188/MG-190/BR-050/SP-330 naar
de vrachtterminal van São Paulo-Guarulhos (GRU), per vrachtvlucht (grootcirkel, aannemelijk) naar het vrachtplatform van
Zürich Airport (ZRH); de lijn eindigt op ZRH — de Zwitserse afnemer is niet gebrond.
**Welke as van het verhaal:** Brazilië → Zwitserland, doré per luchtvracht. Paracatu → Zwitserland 2024: **11,5 t doré bruto ≈ 8,3 t
Au fijn** (FOB USD 638 mln; ComexStat SH 7108, gemeente Paracatu-MG) [1][toets]. Kruiscontrole: 8,3 t = 266.900 oz × ~USD 2.390/oz
(gem. goudprijs 2024) ≈ USD 638 mln, dus FOB en fijn gewicht sluiten op elkaar. Paracatu totaal ≈ 16 t fijn/j [toets]; de rest van
de export gaat o.a. naar Canada (11,0 t doré, context, geen conflict).

## 1 · Ketenkaart
```
Paracatu-mijn, installatiecluster `au-paracatu-mijn`
  ──(b1 truck · MG-188 → BR-352 → MG-190 → BR-050 (Uberaba) → SP-330 Anhanguera → Rodovia Hélio Smidt · hemelsbreed 696 km, geen wegkm)──►
openbare weg bij de GRU-vrachtterminal (Rodovia Hélio Smidt)
  ──(b2 truck · last mile, STIPPEL: airside/privéterrein · ~0,4 km)──►
GRU-vrachtterminal `au-gru-vrachtterminal`
  ──(b3 lucht · vlucht GRU → ZRH, grootcirkel, aannemelijk · 9.609 km berekend)──►
Zürich Airport vrachtplatform `au-zrh-vrachtterminal` (hergebruikt uit goud-loulo-ticino.md) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Paracatu-mijn → openbare weg bij GRU-vrachtterminal | MG-188, BR-352, MG-190, BR-050 (Uberaba), SP-330/SP-348, Rodovia Hélio Smidt | **hemelsbreed 696 km, geen wegkm** (geen gepubliceerde wegkm); OSRM-indicatie 881–884 km [osrm] | maak_stroombeen_weg (extract brazilie) | nee |
| b2 | A | truck | openbare weg → GRU-vrachtplatform (anker) | airside last mile | ≈0,44 km hemelsbreed [berekend] | stippel | **ja** — "last mile (schematisch — airside/privéterrein)" |
| b3 | B | lucht | GRU-vrachtterminal → ZRH-vrachtplatform | vrachtvlucht GRU → ZRH, grootcirkel (aannemelijk: landniveau) | 9.609 hemelsbreed (berekend, anker → anker) | maak_luchtbeen | nee — doorgetrokken |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-paracatu-mijn` | mijn / laadplek | Paracatu — Morro do Ouro, installatiecluster (Kinross Brasil Mineração) | -17.1820, -46.8836 | [2][3][toets] | bron-gelegd (z14 + z15 gezien: gebouwen, tanks en molen direct ten N van de grote pit, tailingsdam W; het Wikipedia-punt -17.1931, -46.8803 ligt in de pit zelf, 1,3 km zuidelijker, en is niet gebruikt) |
| `au-gru-vrachtterminal` | overslag / lucht | São Paulo-Guarulhos (GRU), vrachtterminal (TECA/Terminal de Cargas), W-zijde van het platform | -23.4275, -46.4891 | [4][5][osm] | bron-gelegd, pand **onzeker** (z15 + z16 gezien: rij lange vrachtloodsen aan de W-rand van het platform met wijdrompvrachttoestellen ervoor, ten W van de passagiersterminals; welk loods specifiek TECA is, is niet te onderscheiden) |
| `au-gru-wegaansluiting` | openbare weg (einde b1) | Rodovia Hélio Smidt, W van de vrachtloodsen (OSRM-snap 2 m) | -23.4300, -46.4925 | [osrm] | aannemelijk (z16 gezien: dubbelbaans doorgaande weg ca. 450 m W van het anker; geen publiek wegpad naar het platform zelf — OSRM snapt het anker op de Terminal 1-bordesweg, 159 m verderop, dus airside) |
| `au-zrh-vrachtterminal` | overslag / lucht, stoppunt | Zürich Airport vrachtplatform | 47.4647, 8.5492 | [6] | bron-gelegd — LETTERLIJK hergebruikt uit `goud-loulo-ticino.md` (z14: vrachtplatform met toestellen naast rechthoekige loods, O van de hoofdterminal) |

## 4 · Via-punten (b1; OSRM-knopen, elk op de doorgaande weg gesnapt)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | MG-190 bij Coromandel (noordrand, OSRM 0 m) | -18.4508, -47.2141 | houdt de route op MG-190/BR-352 via Coromandel i.p.v. een zuidelijker pad naar Araxá; naamloze doorgaande weg |
| b1 | 2 | Rodovia Chico Xavier (BR-050), Uberaba-ZW-rand (OSRM 5 m) | -19.7807, -47.9199 | corridorknoop: BR-050 naar São Paulo begint hier; buiten het centrum van Uberaba |
| b1 | 3 | Rodovia Anhanguera (SP-330) bij Araras/Leme (OSRM 2 m) | -22.3595, -47.3949 | houdt de route op de Anhanguera i.p.v. SP-310/SP-304 naar het westen |
| b1 | 4 | Campinas-NW, Anhanguera/Bandeirantes-bundel (OSRM 4 m, naamloos) | -22.9249, -47.1310 | keuze Anhanguera vs Bandeirantes (SP-348) richting São Paulo; Campinas-centrum 8 km ervan af |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Paracatu-installatie | Kinross Gold (Brazilië) | erts → doré (goud + zilver) | Paracatu ≈ 16 t Au fijn/j (2024) [toets]; Kinross-GEO 577.354 oz in 2022 = 18,0 t, GEO incl. zilver [3] | [3][toets] |

## 6 · Stoppunt
De brief stopt op het ZRH-vrachtplatform: ComexStat laat de Braziliaanse goudexport naar Zwitserland alleen via de douane-eenheid
Guarulhos lopen [toets], maar geen bron noemt de Zwitserse afnemer (raffinaderij of bank) van déze doré; fase D en E vervallen.

## 7 · Open punten
- **BINDEND VERWERKT (toets):** mijnanker = installatiecluster -17.1820, -46.8836 (niet de pit); geen wegkm gepubliceerd → "hemelsbreed 696 km,
  geen wegkm", OSRM 881–884 km als indicatie (de ±15%-toets is hier geen norm: een rit over MG/SP-wegen is ~1,27× hemelsbreed).
- Zwitserse afnemer en ZRH als aankomstluchthaven zijn **aannemelijk, niet gebrond** (kan ook GVA of MXP zijn); de vlucht GRU → ZRH is niet
  per vluchtnummer gevonden. Wél bron voor de modaliteit: gold uit het GRU-vrachtterminal was in juli 2019 bestemd voor Zürich en New York
  (GRU Airport in persbericht van de roof) [4][5]. Het overzichtsartikel van Swiss WorldCargo (TECA als GRU-behandelpunt) gaf mij 403: niet gelezen.
- ComexStat (api-comexstat.mdic.gov.br) gaf mij een Cloudflare 403: de cijfers 11,5 t / USD 638 mln / alleen-via-Guarulhos komen uit de
  haalbaarheidstoets [toets], niet uit een eigen lezing; de goudprijs-kruiscontrole hierboven bevestigt FOB tegen fijn gewicht.
- Doré → fijn goud (11,5 → 8,3 t, ≈72%) is uit de toets overgenomen; het doré-gehalte van Paracatu is niet bronnelijk gevonden.
- Paracatu exporteert ook 11,0 t doré naar Canada (2024): geen tweede keten getekend.
- GRU-anker is terrein-niveau; b2 is een korte stippel omdat het platform airside ligt (patroon `goud-loulo-ticino` / `goud-pamp-shanghai`). Via-punt 1
  en 4 liggen in stads-/dorpszone maar op de doorgaande weg: de bak-agent kijkt of de snap < 5 km blijft en of er geen 180°-keerpunt ontstaat.

## 8 · Bronnen
[1] ComexStat, MDIC Brazilië — SH 7108, gemeente Paracatu-MG, 2024. https://comexstat.mdic.gov.br/en/geral (niet zelf te openen; cijfers via [toets])
[2] Wikipedia, "Paracatu mine" — Kinross, Minas Gerais, 17,5 Moz reserves, coördinaat -17,193/-46,8804 (= pit). https://en.wikipedia.org/wiki/Paracatu_mine
[3] Kinross Gold, SEC exhibit 99.1 (FY2022) — Paracatu 577.354 GEO-oz 2022; doré gaat naar raffinaderijen. https://www.sec.gov/Archives/edgar/data/701818/000110465923040149/kgc-20221231xex99d1.htm
[4] County Press / PA, 2019 — "Gold destined for Zurich, New York stolen in Brazil airport heist" (GRU-vrachtterminal, 750 kg). https://www.countypress.co.uk/news/national/17797354.gold-destined-zurich-new-york-stolen-brazil-airport-heist/
[5] Global News, 2019-07-25 — roof van ~750 kg goud en metalen bij een vrachtterminal van Guarulhos. https://globalnews.ca/news/5686379/gold-theft-brazil-airport
[6] `v2/design/routebrieven/goud-loulo-ticino.md` (en `pgm-springs-zurich.md`) — anker `au-zrh-vrachtterminal` 47.4647, 8.5492.
[osrm] OSRM publieke server (router.project-osrm.org), 2026-10-29 — route mijn → Hélio Smidt 881,5 km; met de vier via-punten 883,5 km (MG-188 161 · BR-352 21 · MG-190 132 · LMG-798 39 · BR-050 27 · SP-330/BR-050 347 · SP-348 81 km); nearest-snaps van de via-punten.
[osm] OpenStreetMap (ODbL) via Nominatim — "Terminal de Cargas" bij Terminal 2 -23.4259, -46.4872 (bordesweg, niet gebruikt); Rodovia Hélio Smidt -23.4300, -46.4925.
[toets] haalbaarheidstoets goud-paracatu-zurich (bindend; webcheck ComexStat cities/general 2024 en OSRM).
[v1] `data/goud.js`: au-paracatu → au-ref-argor, mode air, via au-air-gru, au-air-zrh, "Brazilië → Ticino" (v1-checklist; sitelaag `w-paracatu` -17.2167/-46.8667 is een v1-registerpunt, 4,3 km van het cluster, niet gebruikt).
Satellietblik: `v2/build-cache/satcheck/sat-goud-paracatu-zurich-mijn.png` (z14), `-mijn-z15.png`, `-gru.png` (z15), `-gru-teca.png` (z16), Esri, 2026-10-29.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)

`v2/data/stroomroute-goud-paracatu-zurich.json` (186,8 KB, versie 2, lonlat) · functie `bak_goud_paracatu_zurich()` in `v2/tools/bak_stromen.sh` · profiel `goud-paracatu-zurich-paracatu-gru` in `v2/tools/maak_stroombeen_weg.py`.

| # | modaliteit | km | geometrie | stippel? |
|---|---|---|---|---|
| b1 | truck | 885,0 (8.353 punten) | `maak_stroombeen_weg` via `wegscan_puur.py`, extract brazilie | nee, doorgetrokken |
| b2 | truck (last mile GRU) | 0,445 | rechte lijn in de bak-functie | **ja**, airside/privéterrein |
| b3 | lucht | 9.609,2 (386 punten) | `maak_luchtbeen.py`, grootcirkel GRU → ZRH | nee, doorgetrokken |

Totaal 10.494,6 km · 3 markers (`au-paracatu-mijn`, `au-gru-vrachtterminal`, `au-zrh-vrachtterminal`), alle op 0,0 km van hun lijn · naden b1→b2→b3 0,000 km.

**Recept.** b1: vijf via-punten uit §4 (mijn, Coromandel, Uberaba, Araras/Leme, Campinas-NW) plus eindpunt Rodovia Helio Smidt (-23.4300, -46.4925); refs MG-188, BR-352, MG-190, BR-050, SP-330, SP-348; `eindToegangPrivaat`; vensterKm 40. Alle snaps 0,00-0,09 km; segmenten 180,4 / 210,4 / 307,7 / 74,2 / 112,4 km. b2: `--stippel` van het einde van b1 naar het GRU-anker. b3: `maak_luchtbeen.py --van "GRU vrachtterminal|-23.4275,-46.4891" --naar "ZRH vrachtplatform|47.4647,8.5492"`. ZRH-anker letterlijk uit goud-loulo-ticino; geen zee, geen aanloop, geen spoor.

**Toets.** b1 885,0 km tegen OSRM 883,5 km (+0,2%) en tegen hemelsbreed 696 km (x1,27): in lijn met de brief, die hier geen wegkm-norm geeft maar een indicatie. Geen naad > 5 km. `toets_knikken.py`: 0 terugloop; 36 knikken zijn spikes van 3-41 m, vrijwel allemaal op mijn-/terreinwegen bij het installatiecluster; één echte omkering van 158 graden over 10 m bij het via-punt Uberaba ZW-rand (-19.7771, -47.9226): een korte keerlus op de aansluiting, geen omweg (segmentkm sluiten op OSRM), wel een voetnoot. `toets_rechte_benen.py`: geen bevinding voor deze stroom (stippel en luchtbeen uitgezonderd).

**Toelichting stippel b2.** Het GRU-vrachtplatform ligt airside; OSRM snapt het anker op de bordesweg van Terminal 1, dus het wegbeen eindigt op de openbare Rodovia Helio Smidt (ca 450 m W van het anker) en de laatste 0,445 km is "last mile (schematisch — airside/privéterrein)" (patroon goud-loulo-ticino en goud-pamp-shanghai).

**Toelichting vlucht b3.** Doorgetrokken grootcirkel van 9.609 km tussen twee gelegde vrachtterminals. Aannemelijk: de modaliteit (doré per vracht naar Zürich) is gebrond via de GRU-roof van 2019, de specifieke lading, het vluchtnummer en ZRH als aankomstluchthaven niet (§7; kan ook GVA of MXP zijn). De onzekerheid staat in de beennaam, niet in de lijnstijl.

**Lessen.**
- De brazilie-scan (2,06 GB, 44,4 mln nodes in het venster) kostte 867 s voor 885 km corridor met een venster van 40 km; de cache maakt een tweede run direct klaar.
- De OSRM-via-punten uit de brief snapten allemaal op 0-9 m: geen via-punt bijgeschoven of verwijderd.
- Het sitelaagpunt `w-paracatu` (v1) ligt nog 4,3 km van het cluster; niet gelijkgetrokken (sitelagen zijn niet van de bak-agent).
