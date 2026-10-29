# Routebrief (licht) · Zilver — Neves-Corvo → Ourique → Praias do Sado, Setúbal (Portugal)

**stroom-id:** `zilver-nevescorvo-setubal` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** Cu-, Zn- en Pb-concentraat (met zilver als bijproduct) van de Neves-Corvo-concentrator (Somincor, sinds april 2025 Boliden) per **eigen spoortak** (Ramal de Neves-Corvo, 30,8 km) naar Ourique en over de Linha do Sul via Funcheira, Ermidas-Sado en Águas de Moura naar het Terminal Somincor/Almina op Praias do Sado in de haven van Setúbal (3 treinen per dag, Medway). Zeebeen en afnemers zijn niet gepubliceerd; de keten stopt op de kade.
**Welke as van het verhaal:** *Iberische Pyrietgordel: bijproduct-zilver in basismetaalconcentraat, per spoor naar de kade* — Lusa (op basis van het Boliden-jaarverslag): **58.718 kg zilver in 2025 = ≈ 58,7 t Ag/j** [6]; de eerdere Lundin-opgave van ≈ 1,9 Moz Ag (2023) = 59 t is dezelfde orde [7]. Eenheid in [6] is "concentrado de prata", vermoedelijk contained Ag: onzeker.

## 1 · Ketenkaart
```
Neves-Corvo-concentrator (Somincor/Boliden), Castro Verde `ag-nevescorvo-mijn`
   ──(b1 spoor · Ramal de Neves-Corvo 30,8 km → Ourique → Linha do Sul via Funcheira, Ermidas-Sado, Águas de Moura · ~164 km)──►
Terminal Somincor/Almina, Praias do Sado, haven van Setúbal `ag-setubal-terminal` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `ag-nevescorvo-mijn` → `ag-setubal-terminal` | Ramal de Neves-Corvo (mijn → Ourique) + Linha do Sul (Ourique → Funcheira → Ermidas-Sado → Águas de Moura → Praias Sado) [2][5] | ramal **30,8 km** [2]; Grândola-Norte → Praias do Sado **62 km** [5]; totaal niet gepubliceerd; router 163,5 km (31,2 + 132,3); hemelsbreed ≈ 132 km | toets_spoorroute (2 runs, `BAKE_SUFFIX=-raw`) | nee |

Geen weg-, zee- of leidingbeen. De concentraat-Pb gaat volgens [3] per weg (in containers) en [5] noemt het Midden/Verre Oosten als zeebestemming voor Pb; dat is niet getekend (§7). Mijn → spoorkop 0,6 km en kade → spoor 0,18 km zijn binnen de 2 km-regel, dus geen last-mile-been.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-nevescorvo-mijn` | concentrator / verlading (kop) | Neves-Corvo-mijncomplex met concentrator en tailings, Castro Verde (Somincor/Boliden) | 37.5731, -7.9708 | [1][9] | bron-gelegd (z15 gezien: groot industrieel complex met meerdere hallen, verdikkers en tailingsbekkens oostelijk; z16 spoorkop-blik: poort/laadzone aan de NW-rand op 37.5743, -7.9776, 0,6 km van het anker, daar snapt het net) |
| `ag-setubal-terminal` | overslag / kade (staart, stoppunt) | Terminal Somincor/Almina, Praias do Sado, haven van Setúbal (152 m kade, 1 ligplaats, 600 kt/j) | 38.5095, -8.8498 | [5][9] | bron-gelegd (z16 gezien: lange opslagloods met band naast een kadesteiger aan de Sado, spoor langs de oostzijde; OSM-object "Somincor" industrial op dit punt; spoor snapt op 0,18 km) |

Praias-Sado-station (railhead, "antiga estação") ligt op 38.5139, -8.8423 [9] en wordt door b1 gepasseerd; het is geen apart anker.

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Ourique-station (kruising Ramal ↔ Linha do Sul) | 37.7458, -8.2265 | run-splitsing en de enige corridorkeuze: hier takt de ramal af [2]; 0,01 km snap, bewezen 31,2 + 132,3 km |
| b1 | – | (optioneel) Ermidas-Sado | 38.0028, -8.4140 | alleen ter controle: Ourique → Ermidas 41,4 + Ermidas → terminal 90,3 km = zelfde pad, dus geen extra run nodig |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Neves-Corvo-concentrator | Somincor (Boliden, sinds 16-4-2025; eerder Lundin Mining) | erts → Cu-, Zn- en Pb-concentraat | 2025: 30.665 t Cu, ≈ 110,6 kt Zn-conc, 8.858 t Pb-conc, 58.718 kg Ag | [4][6][8] |
| Terminal Somincor/Almina | Somincor + Almina (gezamenlijke concessie APSS) | 3 treinen/dag, 14 wagons, 28 open-top 20'-containers = 728 t per trein → opslag → graanbulk-schip | 600 kt/j; Somincor-spoor ≈ 380 kt/j (2023) | [5] |

## 6 · Stoppunt
De brief stopt op het Terminal Somincor/Almina: de studie noemt als zeebestemming alleen "Noord-Europa" (Cu/Zn) en "Midden/Verre Oosten" (Pb) zonder haven of smelter [5], dus er is geen gedocumenteerde volgende locatie; fase B-E vervalt.

## 7 · Open punten
- **Afnemers en zeebeen niet gepubliceerd** (alleen windstreken [5]); Pb-concentraat gaat per weg [3] en is niet getekend.
- **Zilvervolume**: 58.718 kg komt uit een Lusa-bericht over het Boliden-jaarverslag; het jaarverslag zelf is niet geopend, de eenheid ("concentrado de prata") is dubbelzinnig. Per-concentraat-aandeel onbekend.
- **Concentraat-treindeel**: het spoor draagt Cu en Zn; Pb dus niet, het zilver in Pb-concentraat reist deels per weg (niet gekwantificeerd).
- **Ontwerpfouten gecorrigeerd** (haalbaarheidstoets): eigenaar Boliden (niet Lundin); corridor via Ourique (pt.wikipedia: Ramal takt af in Ourique [2], niet via Funcheira als eigen tak) en daarna de Linha do Sul naar Praias Sado [5]; spoorkm 163,5 i.p.v. 250-300 [11].
- Spoorkop: de rail-terminal bij de mijn ligt "afstand van de laadzone" met een wegrit voor containers [5]; die ~0,6 km is niet apart getekend.
- v1 (`data/silver.js`) en de zilver-sitelaag kennen Neves-Corvo en Setúbal niet; een site van ≈ 59 t Ag/j ontbreekt (melding aan de orchestrator).

## 8 · Bronnen
[1] Wikipedia (en), "Neves-Corvo mine" — eigen spoortak, export via Setúbal, eigenaar Boliden sinds apr. 2025. https://en.wikipedia.org/wiki/Neves-Corvo_mine
[2] Wikipedia (pt), "Ramal de Neves-Corvo" — 30,8 km, Ourique, Praias-Sado, Medway 2 treinen/dag. https://pt.wikipedia.org/wiki/Ramal_de_Neves-Corvo
[3] Wikipedia (pt), "Mina de Neves-Corvo" — Cu en Zn per spoor, Pb per weg; installaties in de haven van Setúbal. https://pt.wikipedia.org/wiki/Mina_de_Neves-Corvo
[4] Boliden, "Boliden Somincor" — Cu, Zn, Pb en Ag; eigen spoorlink en haven van Setúbal. https://www.boliden.com/operations/mines/boliden-somincor
[5] APA/SIAIA, "Estudo Logístico" (Lagoa Salgada, 2023) §3, §5.2.2, §6.1.2 — Terminal Somincor/Almina: 152 m kade, 600 kt/j, 3 treinen/dag, 728 t/trein, Medway, Grândola-Norte → Praias do Sado 62 km. https://siaia.apambiente.pt/AIADOC/AIA3778/anexo6-estudologistico202531116139.pdf
[6] Lusa via Notícias ao Minuto, productie 2025 (110.600 t Zn-conc, 30.665 t Cu, 8.858 t Pb-conc, 58.718 kg Ag). https://www.noticiasaominuto.com/economia/2950905/concessionaria-reforca-investimento-na-exploracao-na-mina-de-neves-corvo
[7] Lundin Mining, 2024 production release (productie Neves-Corvo; Ag niet opgenomen). https://lundinmining.com/_resources/news/2025/2025-01-16.pdf
[8] Jornal Económico, 16-4-2025, afronding Boliden-overname van Somincor. https://jornaleconomico.sapo.pt/?p=1290504
[9] OpenStreetMap (ODbL) via Nominatim — Ourique 37.7449, -8.2262; Praias-Sado 38.5138, -8.8420; "Somincor" Setúbal 38.5095, -8.8498. https://www.openstreetmap.org
[10] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-zilver-nevescorvo-setubal-{mijn,spoorkop,terminal,praias,ourique}.png`.
[11] `v2/tools/toets_spoorroute.mjs` (`BAKE_SUFFIX=-raw`, 3.260.717 spoor-edges): mijn → Ourique 31,2 km (snap 0,61/0,01), Ourique → terminal 132,3 km (snap 0,01/0,18), 0 bochten >= 60 graden; Grândola-Norte → terminal 57,1 km tegen 62 km [5].

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
**Bestand:** `v2/data/stroomroute-zilver-nevescorvo-setubal.json` (9,3 KB, contract versie 2, lonlat) · functie `bak_zilver_nevescorvo_setubal` in `v2/tools/bak_stromen.sh` · `bash v2/tools/bak_stromen.sh zilver-nevescorvo-setubal`.

| # | modaliteit | km gebakken | brief | naad | stippel |
|---|---|---|---|---|---|
| 1 | spoor mijn → Ourique (Ramal de Neves-Corvo) | 31,5 | ramal 30,8 [2]; router 31,2 | – | nee |
| 2 | spoor Ourique → Terminal Somincor/Almina (Linha do Sul) | 133,0 | router 132,3; Grândola-Norte → Praias 62 [5] | 0,000 km | nee |

Totaal **164,5 km**, 482 punten, 2 markers (`ag-nevescorvo-mijn` 0,61 km en `ag-setubal-terminal` 0,18 km van de lijn). Gebakken km is 0,3 en 0,7 km hoger dan de routerkm door de polylijn; ramal 31,5 tegen 30,8 = +2,3% (norm ±15%). Een totaal is niet gepubliceerd: de km-toets is indicatie.

**Recept:** twee `--been-geojson "spoor|…"`-regels in reisvolgorde, de bestaande tussenuitvoer `spoorroute-zilver-nevescorvo-setubal-{mijn-ourique,ourique-terminal}.geojson` (`BAKE_SUFFIX=-raw`, 3.260.717 spoor-edges; via-punt Ourique-station 37.7458, -8.2265, snap 0,01 km) ongewijzigd hergebruikt; geen herrun nodig. Geen weg-, zee-, lucht- of leidingbeen, geen stippel, geen haven-aanloop, geen kopie van een bestaande stroom.

**Toets (handleiding §5):** 0 knikken >= 60 graden, 0 omkeringen (`toets_knikken.py`); geen doorgetrokken been is een rechte lijn; naad tussen b1 en b2 0,000 km; `json.load` ok, versie 2, punt_formaat lonlat, modaliteit alleen `spoor`, elk been >= 108 punten.

**Bevindingen / lessen:**
- Marker `ag-nevescorvo-mijn` ligt 0,61 km van de lijn (net boven de ~0,5 km-richtlijn): anker is het complexcentrum, de lijn begint bij de spoorkop/poort op 37.5743, -7.9776 (zie §3, snap 0,61). Binnen de 2 km last-mile-regel, dus geen stippel.
- Zilver reist hier als bijproduct in Cu-/Zn-concentraat; de lijn claimt dus het concentraattransport, niet zuiver zilver. Pb-concentraat (per weg) is niet getekend.
- Zeebeen en afnemers niet gepubliceerd: de keten eindigt bewust op de kade (stoppunt).
- Eerdere afgebroken poging liet alleen de tussenuitvoer (spoorroutes, satcheck-beelden) achter; er waren geen restanten van functie of profiel.

