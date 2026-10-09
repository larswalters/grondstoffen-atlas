# Routebrief (licht) · olie — Fishkhabur (Irak-Turkije) → Iraq-Turkey Pipeline → Ceyhan-exportterminal (Turkije)

**stroom-id:** `olie-kirkuk-ceyhan` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** Noord-Iraakse (Kirkuk- en KRG-)ruwe olie die bij Fishkhabur de Turks-Iraakse grens passeert, per **leiding** —
de Turkse sectie van de Iraq-Turkey Pipeline (ITP, BOTAŞ) via Cizre en Zuidoost-Anatolië — naar de Ceyhan-exportterminal.
**Welke as van het verhaal:** *de Hormuz-bypass van Irak* — Kirkuk-Ceyhan (970 km, 1,5 mln vpd nameplate) liep 2023–sept 2025 dicht
(ICC-arbitrage), herstartte sept 2025 en voerde maart 2026 ~250 kb/d uit, toen Hormuz dichtging [1][3]. Titel is Fishkhabur-start
(bindende toets): de federale Kirkuk-Baiji-Mosul-lijn is in herstel, de Kirkuk-lading loopt in 2026 via de KRG-leiding die bij Fishkhabur aansluit [1][3].

## 1 · Ketenkaart
```
Fishkhabur `ol-fishkhabur-kop` ──(b1 leiding · ITP Turks deel, 32 OSM-ways · 614,8 km OSM, doorgetrokken)──►
  OSM-eind lon 36.15 ──(b2 leiding · stippel 28,4 km, geen OSM-way)──► BTC-OSM-eind 36.9051,35.9365
  ──(b3 leiding · stippel 6,1 km, kopie van olie-sangachal-ceyhan)──► Ceyhan-terminal `ol-ceyhan-term` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Fishkhabur → OSM-eind lon 36.15 | Iraq-Turkey Pipeline (Kirkuk-Ceyhan), Turks deel: Fishkhabur – Cizre – oost-west door Zuidoost-Anatolië | EIA: Fishkhabur–Ceyhan 400 mijl ≈ 644 km [2]; eigen OSM-som 614,8 km = −4,5% van dat totaal [5] | OSM-ways `man_made=pipeline`+`substance=oil`, operator BOTAŞ, BTC uitgesloten; 32 ways (27 met operator BOTAŞ, 5 zonder operatortag), stitch 0 m (`maak_leidingbeen_olie_kirkuk_ceyhan.py`) | nee |
| b2 | A | leiding | OSM-eind (37.0951,36.1495) → BTC-OSM-eind (36.9051,35.9365) | laatste ~28 km naar de kust | ~28 [5] (hemelsbreed, geen leidingkm) | geen OSM-way | ja — "hier reikt het net niet" |
| b3 | B | leiding | BTC-OSM-eind → Ceyhan-terminal | slot over het terminalterrein | 6,1 (hemelsbreed) | **letterlijke kopie** van de stippel van `olie-sangachal-ceyhan` (`bak_olie_sangachal_ceyhan()`) | ja — terminalterrein zonder OSM-way |
Totaal b1–b3 = 649,3 km tegen EIA 644 km = **+0,8%** (alleen indicatie: de brongetallen zijn afgerond op 100 mijl). Geen zeebeen (bindend).

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-fishkhabur-kop` | kop van de Turkse sectie, aansluiting KRG-leiding + (herstelde) federale lijn | Fishkhabur (Irak-Turkije-grens, Tigris) | 37.1335, 42.4221 | [1][2][5][6] | aannemelijk (z15 gezien: klein terrein met paar witte gebouwtjes op het kruis, rechte tracé-achtige strook noord- en zuidwaarts, akkers, de Tigris 0,7 km zuid — geen groot pompstation zichtbaar; OSM-leiding begint er 7 m vandaan) |
| `ol-ceyhan-term` | overslag leiding → tanker, stoppunt | Ceyhan-exportterminal (BOTAŞ/BTC, Yumurtalik-baai) — **hergebruikt anker** `w-ceyhan-btc` uit `olie-sangachal-ceyhan.md` / `olie-sitelaag.json` | 36.8500, 35.9333 | [8][9] | bron-gelegd (overgenomen; nu z14 gezien: ligt ~0,25 km zuid van de T-kop van een ~2,3 km lange laadsteiger in de baai, het tankpark staat ~5 km noordelijker aan de kust) |

## 4 · Via-punten (alleen b1 — leiding, geen corridorkeuze; punten zijn OSM-lijnpunten ter controle, geen routeringsinvoer)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Cizre (way-grens 284454158/161) | 37.3380, 42.1960 | eerste knik na Fishkhabur; de lijn gaat eerst ruim 20 km noordwaarts [5] |
| b1 | 2 | ~150 km | 37.4576, 41.0370 | hoofdas oost-west, ver van elke ander tracé [5] |
| b1 | 3 | ~300 km | 37.4445, 39.4081 | idem [5] |
| b1 | 4 | ~450 km | 37.4540, 37.7503 | idem [5] |
| b1 | 5 | ~600 km | 37.1707, 36.2628 | nadering OSM-eind, 15 km vóór het gat [5] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ceyhan-exportterminal (BOTAŞ) | BOTAŞ (ITP) / BTC Co (BTC-deel) | pijp-ruwe olie → tankopslag → tanker | ITP nameplate 1,5 mln vpd (46"+40"); 2026 werkelijk ~200–250 kb/d [1][2][3] | [1][2][3] |

## 6 · Stoppunt
De brief stopt bij de Ceyhan-terminal: geen bron koppelt één Kirkuk-lading aan één raffinaderij of afnemer (Kirkuk-blend wordt op de
Middellandse-Zeemarkt verkocht); fase D/E vervallen. Volume 2026: **~250 kb/d** (maart 2026, Wikipedia [1]); Rudaw 25-03-2026: ~200 kb/d
met 250 aangekondigd en 300 "in de nabije toekomst" [3]. Peiljaar 2026, kb/d, enkele bron.

## 7 · Open punten
- **Alleen het Turkse deel is gemeten.** De OSM-lijn Baiji–Fishkhabur (269,6 km, één gestitchte lijn) en Kirkuk–Baiji (52 km, gaten) bestaan, maar worden
  niet getekend: bindend start bij Fishkhabur, de federale lijn is in herstel [1]. Optioneel later een been b0.
- **Het volume komt uit één bron** (Wikipedia, Rudaw wijkt af); het jaarakkoord aug 2026 (750 kb/d) heeft in een zoekronde geen tweede bron opgeleverd.
- **Gat van ~28 km** vóór de kust: waarom OSM bij lon 36.15 ophoudt is niet onderzocht; de stippel is een rechte lijn, geen tracé.
- **Anker Ceyhan** ligt 0,25 km uit de steigerkop in open water en 5–6 km van het tankpark; ongewijzigd (sitelaag "onzeker") — voor een
  latere ankercheck. Geen haven-aanloop: er is geen zeebeen (bindend); de terminal ligt 7,7 km van MARNET-zeeknoop 3786 (zie `olie-sangachal-ceyhan.md`).
- **Way 191693918** (71 punten op de lijn) draagt de naam "BOTAŞ Doğalgaz Boru Hatı" maar `substance=oil`; behouden omdat de lijn ononderbroken en
  de totale lengte plausibel is. Sabotage-/stilstandrisico van de Iraakse kant blijft buiten dit been.

## 8 · Bronnen
[1] Wikipedia, "Kirkuk–Ceyhan Oil Pipeline" (970 km, 1,5 mln vpd, ICC-uitspraak maart 2023, herstart sept 2025, 250 kb/d maart 2026, Baiji–Fishkhabur in herstel, jaarakkoord aug 2026 750 kb/d). https://en.wikipedia.org/wiki/Kirkuk%E2%80%93Ceyhan_Oil_Pipeline
[2] U.S. EIA, "Turkey" country analysis (2016), tabel 1: Kirkuk–Fishkhabur 220 mijl, Fishkhabur–Ceyhan 400 mijl, 1,5 mln vpd. https://www.eia.gov/international/content/analysis/countries_long/Turkey/turkey.pdf
[3] Rudaw, 25-03-2026: Kirkuk-export via de KRG-leiding naar Ceyhan ~200 kb/d, 250 aangekondigd. https://www.rudaw.net/english/business/25032026
[4] S&P Global, juli 2025: Turkije zegt de pijpleidingakkoorden op (ingang 27-07-2026), via een zoekresultaat, niet zelf gelezen. https://www.spglobal.com/commodity-insights/en/news-research/latest-news/crude-oil/072125-turkey-cancels-pipeline-agreements-with-iraq-in-latest-row-impacting-kurdish-crude
[5] OpenStreetMap (ODbL) — eigen scan 2026-10-09 op `turkije`/`irak` (Geofabrik): 614,8 km Fishkhabur → 37.0951,36.1495, 1.028 punten; Iraks deel 269,6 km; BTC uitgesloten op operator/naam.
[6] Esri World Imagery via `v2/tools/sat_check.py` (z15/z14): `v2/build-cache/satcheck/sat-olie-kirkuk-ceyhan-fishkhabur.png`, `…-fishkhabur-z14.png`.
[7] Idem, Ceyhan z14: `v2/build-cache/satcheck/sat-olie-kirkuk-ceyhan-ceyhan.png`.
[8] `v2/design/routebrieven/olie-sangachal-ceyhan.md` — anker `ol-ceyhan-term` en de stippel van 6,1 km, letterlijk hergebruikt.
[9] `v2/design/olie-sitelaag.json` — `w-ceyhan-btc` 36.8500, 35.9333 (status "onzeker").
[10] Haalbaarheidstoets keten `olie-kirkuk-ceyhan` (orkestrator, 2026-10-09): bindende aanpassing Fishkhabur-start, 614,8 km uit 31 BOTAŞ-ways, stippels naar Ceyhan.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-olie-kirkuk-ceyhan.json` (21,2 KB, versie 2, lonlat) · **functie:** `bak_olie_kirkuk_ceyhan()` in `v2/tools/bak_stromen.sh` · **recept:** `bash v2/tools/bak_stromen.sh olie-kirkuk-ceyhan` (15 s, zwaar-slot) · **registersleutel:** `olie-kic` (`olie-kc` is bezet door een andere stroom).

| # | modaliteit | km | punten | naad | wat |
|---|---|---|---|---|---|
| 1 | leiding (doorgetrokken) | 614,8 | 1.028 | 0 | ITP Turks deel Fishkhabur → OSM-eind 37.09513,36.14954 (`olie-kirkuk-ceyhan-leiding-itp.geojson`, FeatureCollection) |
| 2 | leiding (stippel) | 28,4 | 2 | 0,00 | OSM-gat naar BTC-OSM-eind 36.90509,35.93652 |
| 3 | leiding (stippel) | 6,1 | 2 | 0,00 | BTC-OSM-eind → Ceyhan-terminal 36.8500,35.9333, letterlijke kopie uit `olie-sangachal-ceyhan` (punten en km identiek, nagelopen) |

Totaal 649,3 km · 1.032 punten · 2 markers (`ol-fishkhabur-kop` 7 m van de lijn, `ol-ceyhan-term` 0,1 m) · geen naad > 0,00 km.

**Toets.** b1 614,8 km tegen EIA ~644 km = -4,5% (brongetal afgerond op 100 mijl, dus indicatie, geen norm); b1-b3 samen 649,3 km = +0,8%. `toets_knikken.py`: 2 knikken, 0 omkeringen, 0 terugloop. `toets_rechte_benen.py`: alleen de twee stippels (per constructie recht, reden in de naam).

**Stippels.** b2 is "hier reikt het net niet": OSM houdt bij lon 36.15 op, de reden van het gat is niet onderzocht, de lijn is hemelsbreed (geen leidingkm, geen tracé). b3 is het terminalterrein zonder OSM-way, overgenomen uit de Sangachal-stroom zodat beide stromen dezelfde laatste 6,1 km delen.

**Geen haven-aanloop, geen zeebeen** (bindend in de brief): de terminal ligt 7,7 km van MARNET-zeeknoop 3786, maar er snapt niets op de router. Mocht er ooit een tankerbeen vanaf Ceyhan komen, dan is een aanloop dan wél verplicht (LAR-586).

**Bevindingen / lessen.**
- Spike in b1 bij 37.38259,38.50201: knik 101 graden, straal 13 m. Dit is OSM-bronvorm (een korte zaagtand in een BOTAS-way), geen routering; niet aangeraakt. Tweede knik 61 graden, straal 607 m bij 37.18607,36.46343 = een echte bocht.
- Way 191693918 heet "Dogalgaz" maar draagt `substance=oil`; behouden (lijn ononderbroken).
- Registersleutel: `olie-kc` is in gebruik, daarom `olie-kic`.
- Het Ceyhan-anker blijft "onzeker" (0,25 km uit de steigerkop, 5-6 km van het tankpark); ongewijzigd, sitelaag niet aangeraakt.
- Het stroom-id noemt Kirkuk maar de lijn start bij Fishkhabur (bindende toets): titel en markers zeggen Fishkhabur, het id blijft staan. Eindpunt Ceyhan klopt met het id.
- Open: volume 2026 uit één bron; optioneel een b0 Baiji-Fishkhabur (OSM 269,6 km) en Kirkuk-Baiji (52 km, gaten).
