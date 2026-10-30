# Routebrief (licht) · nikkel — Nouméa (Nieuw-Caledonië) → Shunan (Japan)

**stroom-id:** `nikkel-doniambo-shunan` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** ferronikkel van de SLN/Eramet-smelter Doniambo (Nouméa) gaat per zeeschip vanaf de eigen kade over de Koraalzee, Bismarckzee en Filipijnenzee en door het Bungo-kanaal en de Suo-nada naar de Nippon Steel Yamaguchi Works, Shunan-gebied (ex Nisshin Steel, ex NSSC), aan de Tokuyama-baai; de enige gedocumenteerde band is aandeelhouderschap (aannemelijk: één bron).
**Welke as van het verhaal:** *SLN naar zijn Japanse aandeelhouder* — Nisshin Steel nam in 1991 10 % van SLN en kocht in ruil SLN-producten af [1][2]; Nisshin ging via NSSC (2019) in Nippon Steel op (2025-04-01) [5]. Volume: circa 50 kt Ni/j gemiddeld (SLN-site, jaar niet vermeld) [3]; sitelaag 55 kt Ni/j nameplate. Aandeel naar Shunan: niet gebronnen, geen tonnage op het been.

## 1 · Ketenkaart
```
Doniambo-kade `ni-doniambo-kade` (Nouméa) ──(b1 zee · haven-aanloop Baai van Nouméa · ~21 km, stippel)──►
   MARNET-zeeknoop 2735 (-22.4000,166.3000) ──(b2 zee · MARNET · ~7.618 km)──► MARNET-zeeknoop 5738 (33.7500,131.9000)
   ──(b3 zee · haven-aanloop Suo-nada → Tokuyama-baai · ~38 km, stippel)──► Shunan-kade `ni-shunan-kade`
   ═══ site-anker Shunan Works `ni-shunan-fabriek` (geen eigen been: kade en walserij liggen op één terrein) ═══ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `ni-doniambo-kade` → zeeknoop 2735 | Baai van Nouméa, rifdoorgang | 21,0 (gemeten door maak_havenaanloop, 8 punten, geen land) [toets] | maak_havenaanloop | ja — MARNET reikt niet tot de kade (kade 21,0 km van de zeeknoop) |
| b2 | B | zee | zeeknoop 2735 → zeeknoop 5738 | Koraalzee, Bismarckzee, Filipijnenzee, Bungo-kanaal (door router bevestigen) | 7.618 [toets, MARNET-meting van de haalbaarheidstoets; hemelsbreed knoop-knoop circa 7.230] | MARNET | nee |
| b3 | B | zee | zeeknoop 5738 → `ni-shunan-kade` | Suo-nada, Tokuyama-baai | 38,0 (gemeten door maak_havenaanloop, 60 punten, 0,76 km kadegrens) [toets] | maak_havenaanloop | ja — MARNET reikt niet tot de kade (kade 35,8 km van de zeeknoop) |

Zee-beennaam voor de bak (aannemelijk-vlag): `zeeschip Doniambo-kade → Shunan-kade (aannemelijk: één bron, alleen aandeelhouderband Nisshin/Nippon Steel; geen bron noemt een levering)`. Geen truckbeen: de Shunan-kade ligt aan de zuidrand van het fabrieksterrein, de walserij 0,2 km noordelijk [4]. Geen fase C/D/E.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-doniambo-kade` | laadkade (kop van b1) | SLN-kade Doniambo, Nouméa | -22.2585, 166.4355 | [3][6] | bron-gelegd (z16 gezien: schip langszij de zuidoostkade van het smelterterrein, ertsstrook en kolenhopen erachter; de ertssteiger met scheepslosser ligt 0,5 km NW) |
| `ni-doniambo-fabriek` | smelter (site-anker, geen marker) | SLN Doniambo ferronikkelfabriek | -22.2540, 166.4410 | [3][6] | bron-gelegd (z15–z16 gezien: ovenhallen met schoorstenen, ertsdroogstapels en bandtransporteurs, 0,9 km van de kade; sitelaag-anker `w-doniambo-sln` -22.27/166.44 is een stadscentroïde, 1,8 km ernaast) |
| `ni-shunan-kade` | losplek (staart van b3) | Kade Nippon Steel Yamaguchi Works, Shunan-gebied (Tokuyama-baai) | 34.0537, 131.7745 | [4][6] | bron-gelegd (z17 gezien: aanlegsteiger aan de zuidkade van het fabrieksterrein met een kleine coaster langszij; direct erachter walserij en opslag) |
| `ni-shunan-fabriek` | fabriek (site-anker, geen marker) | Nippon Steel Yamaguchi Works, Shunan-gebied (Nomuraminami-machi 4976) | 34.0590, 131.7772 | [4][6] | bron-gelegd (GEM-coördinaat; z16 gezien: groot walserij-/staalcomplex, hallen en slijpstraat, ~0,6 km van de kade) |

## 4 · Via-punten
Geen — er is geen landbeen. De corridor van b2 kiest de router; b1 en b3 zijn schematische haven-aanlopen over water.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| SLN Doniambo | Eramet 60 %, STCPI 30 %, Nisshin/Nippon Steel circa 10 % | lateriet-erts → ferronikkel (+ matte) | circa 50 kt Ni/j gemiddeld; drie elektrische ovens tot 65 MW [3] | [1][3] |
| Nippon Steel Yamaguchi Works, Shunan-gebied | Nippon Steel (sinds 2025-04-01) | schroot en legering → roestvrij staal, elektrische ovens | 3 ovens van 433 kt/j, één stilgelegd sinds maart 2024 [4] | [4][5] |

## 6 · Stoppunt
De brief stopt bij de Shunan-kade: het ferronikkel wordt hier (aannemelijk) in de elektrische ovens van het roestvrijstaalbedrijf gesmolten, en geen bron noemt een volgende locatie of een leveringscontract. Fase D en E vervallen.

## 7 · Open punten
- **Geen bron noemt een levering Doniambo → Shunan.** De band is eigendom: Nisshin Steel 10 % van SLN sinds 1991, met de afspraak SLN-producten af te nemen [2]; dat Nippon Steel nog steeds minderheidsaandeelhouder is staat alleen in de haalbaarheidstoets (Mining Weekly feb 2023), niet door mij herverifieerd. Eramet noemt het ferronikkel elders vooral voor Chinese roestvrijstaalmakers [7].
- **Smelt Shunan ferronikkel?** GEM noemt Shunan schrootgebaseerd en noemt ferronikkel niet [4]; het naburige Hikari-gebied kan de nikkelafnemer zijn. Gelezen als aannemelijk, niet bevestigd.
- **Naam achterhaald:** NSSC is op 2025-04-01 opgegaan in Nippon Steel; de site heet nu Nippon Steel Yamaguchi Works (Shunan-gebied) [5].
- **Zeeafstand:** 7.618 km MARNET-meting [toets], hemelsbreed knoop-knoop circa 7.230; geen gepubliceerde scheepsafstand, de ±15 %-toets is een indicatie.
- **Kades niet gebronnen:** de Shunan-ligplaats is op beeld een kleine steiger (coaster), geen bron noemt de ligplaats voor ferronikkel; de Doniambo-ligplaats is de zuidoostkade met schip langszij, niet de ertssteiger.
- **Sitelaag-correctie (centraal):** `w-doniambo-sln` staat 1,8 km te ver ZZW; voorstel -22.2540/166.4410.

## 8 · Bronnen
[1] Wikipedia (fr), Société Le Nickel — Nisshin Steel 10 % van SLN sinds 1991, Doniambo gesticht 1912. https://fr.wikipedia.org/wiki/Soci%C3%A9t%C3%A9_Le_Nickel
[2] Reference for Business, Eramet — Nisshin kocht SLN-producten in ruil voor een groeiend belang, 10 % in 1994. https://www.referenceforbusiness.com/history2/24/Eramet.html
[3] SLN/Eramet, sln.eramet.com — circa 50 000 t Ni/j gemiddeld, drie ovens van 65 MW, site Doniambo. https://sln.eramet.com/en/
[4] GEM.wiki, Nippon Stainless Steel Yamaguchi Works (Shunan Area) — 4976 Nomuraminami-machi, 34,059009/131,777221, drie EAF van 433 kt/j, één stil sinds maart 2024. https://www.gem.wiki/Nippon_Stainless_Steel_Yamaguchi_Works_(Shunan_Area)_steel_plant
[5] Wikipedia (ja), Nippon Steel Stainless — Shunan = ex Nisshin Steel, NSSC opgegaan in Nippon Steel op 2025-04-01. https://ja.wikipedia.org/wiki/%E6%97%A5%E9%89%84%E3%82%B9%E3%83%86%E3%83%B3%E3%83%AC%E3%82%B9
[6] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-nikkel-doniambo-shunan-doniambo-kade.png`, `-doniambo-fabriek.png`, `-shunan-kade.png`, `-shunan-kade-z17.png`, `-shunan-fabriek.png`.
[7] Eramet, antwoorden op vragen aandeelhouders AV 28-05-2021 — SLN-ferronikkel vooral voor roestvrijstaalmakers, met name China (via zoekresultaat, pdf niet leesbaar). https://www.eramet.com/wp-content/uploads/2023/03/Eramet-Answers-to-shareholders-written-questions-General-Meeting-28May2021.pdf
[toets] Haalbaarheidstoets (2026-10-30) + eigen meting: zeeknoop 2735 op 21,0 km van de kade, zeeknoop 5738 op 35,8 km van de kade; MARNET 7.618,2 km; aanloop-geojsons `nikkel-doniambo-shunan-aanloop-doniambo.geojson` en `-aanloop-shunan.geojson` staan al in `v2/build-cache/ais/graaf/`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
**Uitvoer:** `v2/data/stroomroute-nikkel-doniambo-shunan.json` (16,6 KB, versie 2, lonlat) via `bash v2/tools/bak_stromen.sh nikkel-doniambo-shunan` (functie `bak_nikkel_doniambo_shunan`). Totaal 7.677,2 km, 849 punten, 2 markers, alleen zee.

| # | modaliteit | km gemeten | km brief | naad | punten |
|---|---|---|---|---|---|
| b1 | zee, stippel (haven-aanloop Nouméa) | 21,0 | 21,0 | 0 | 8 |
| b2 | zee, MARNET zeeknoop 2735 → 5738, doorgetrokken | 7.618,2 | 7.618 (MARNET-meting; geen gepubliceerde afstand) | 0,00 | 781 |
| b3 | zee, stippel (haven-aanloop Shunan/Tokuyama-baai) | 38,0 | 38,0 | 0,00 | 60 |

**Markers:** `ni-doniambo-kade` (-22.2585, 166.4355) en `ni-shunan-kade` (34.0537, 131.7745), beide 0,0 km van de lijn. De twee fabrieksankers zijn geen marker.

**Recept:** b1 = bestaand `nikkel-doniambo-shunan-aanloop-doniambo.geojson` (maak_havenaanloop, kade → knoop, volgorde klopt). b2 = `--been zee` met beide zeeknopen exact opgegeven (snap 0,000 km, 30 MARNET-edges). b3 = `nikkel-doniambo-shunan-aanloop-shunan-rev.geojson`.

**Toelichting stippels:** beide aanlopen zijn stippel omdat MARNET niet tot de kade reikt (21,0 en 35,8 km van de zeeknoop); het pad is kortste pad over water en geen waargenomen vaargeul. Het hoofdbeen b2 is doorgetrokken; "aannemelijk: één bron" staat in de beennaam, niet in de lijnstijl.

**Toets:** geen naad > 0,01 km; km binnen de indicatie (7.618,2 tegen 7.618); `toets_knikken`: 1 knik 64 gr, straal 9,3 km bij -20.90/163.50 (rifbocht in de Koraalzee), 0 omkeringen; `toets_rechte_benen`: alleen de 8-punts aanloop Nouméa (21,0 km, stippel met reden) valt op. Contract: versie 2, punt_formaat lonlat, modaliteit {zee}, elk been >= 2 punten.

**Afwijkingen van het ontwerp:** de Shunan-aanloop is door maak_havenaanloop kade → knoop geschreven; voor de reisvolgorde knoop → kade is hij omgekeerd opgeslagen als `-aanloop-shunan-rev.geojson` (zonder omkering een naad van 35,8 km). Het eindpunt klopt met het id (Shunan).

**Lessen:** (1) een kade-eerst geschreven haven-aanloop moet voor het laatste been van een stroom worden omgekeerd; `hecht_marnet` oriënteert --stippel-geojson niet zelf. (2) Open punten uit §7 blijven staan: geen bron noemt een levering; sitelaag `w-doniambo-sln` 1,8 km ZZW van de smelter (centraal: voorstel -22.2540, 166.4410).
